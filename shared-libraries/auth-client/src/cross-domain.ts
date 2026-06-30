/**
 * Cross-Domain Token Exchange Orchestration
 * 
 * Manages authenticated requests that cross Clerk app boundaries:
 * - CSM impersonation: Clerk App 1 → Clerk App 3 (scoped)
 * - Service-to-service: Clerk App 1 → Clerk App 2 (narrow APIs)
 * - Blocked paths: Clerk App 2/3 → Clerk App 1 (never allowed)
 */
import { ClerkDomain, getDomainConfig, isCrossDomainAllowed } from './domain-config'
import { TokenManager, TokenType, type TokenPayload } from './token-manager'

// ─── Types ────────────────────────────────────────────────────────
export interface CrossDomainRequest {
  sourceDomain: ClerkDomain
  targetDomain: ClerkDomain
  userId: string
  purpose: 'impersonation' | 'service_call' | 'data_access'
  tenantId?: string
  scopes: string[]
}

export interface CrossDomainResult {
  allowed: boolean
  token: string | null
  reason: string
  auditEntry: AuditEntry
}

export interface AuditEntry {
  timestamp: string
  action: string
  sourceDomain: ClerkDomain
  targetDomain: ClerkDomain
  userId: string
  tenantId?: string
  allowed: boolean
  reason: string
}

// ─── Allowed Cross-Domain Paths ───────────────────────────────────
const ALLOWED_CROSS_PATHS: Array<{
  from: ClerkDomain
  to: ClerkDomain
  purposes: string[]
  requireScopes: boolean
}> = [
  // Platform Operators → Tenants (CSM impersonation, tenant management)
  {
    from: ClerkDomain.PLATFORM_OPERATORS,
    to: ClerkDomain.TENANTS,
    purposes: ['impersonation', 'data_access', 'service_call'],
    requireScopes: true,
  },
  // Platform Operators → Sales/Support (admin oversight)
  {
    from: ClerkDomain.PLATFORM_OPERATORS,
    to: ClerkDomain.SALES_SUPPORT,
    purposes: ['data_access', 'service_call'],
    requireScopes: true,
  },
]

// ─── Cross-Domain Exchange ────────────────────────────────────────
export class CrossDomainExchange {
  private tokenManager: TokenManager

  constructor(sourceDomain: ClerkDomain) {
    this.tokenManager = new TokenManager(sourceDomain)
  }

  /**
   * Request a cross-domain token exchange.
   * Validates the path, generates a scoped token, and creates an audit entry.
   */
  async requestExchange(request: CrossDomainRequest): Promise<CrossDomainResult> {
    const auditBase = {
      timestamp: new Date().toISOString(),
      action: 'cross_domain_exchange',
      sourceDomain: request.sourceDomain,
      targetDomain: request.targetDomain,
      userId: request.userId,
      tenantId: request.tenantId,
    }

    // Check if cross-domain access is allowed at the domain level
    if (!isCrossDomainAllowed(request.sourceDomain, request.targetDomain)) {
      return {
        allowed: false,
        token: null,
        reason: `Cross-domain access from ${request.sourceDomain} to ${request.targetDomain} is blocked`,
        auditEntry: { ...auditBase, allowed: false, reason: 'Domain-level block' },
      }
    }

    // Check if the specific path + purpose is allowed
    const allowedPath = ALLOWED_CROSS_PATHS.find(
      p => p.from === request.sourceDomain
        && p.to === request.targetDomain
        && p.purposes.includes(request.purpose)
    )

    if (!allowedPath) {
      return {
        allowed: false,
        token: null,
        reason: `Purpose '${request.purpose}' not allowed from ${request.sourceDomain} to ${request.targetDomain}`,
        auditEntry: { ...auditBase, allowed: false, reason: 'Purpose not in allowed list' },
      }
    }

    // Scopes required for all cross-domain access
    if (allowedPath.requireScopes && request.scopes.length === 0) {
      return {
        allowed: false,
        token: null,
        reason: 'Cross-domain access requires explicit scopes',
        auditEntry: { ...auditBase, allowed: false, reason: 'No scopes provided' },
      }
    }

    // Generate the scoped token
    try {
      const tokenType = request.purpose === 'impersonation'
        ? TokenType.IMPERSONATION
        : TokenType.SCOPED

      const token = await this.tokenManager.generateScopedToken({
        issuerId: request.sourceDomain,
        subjectId: request.userId,
        targetDomain: request.targetDomain,
        type: tokenType,
        scopes: request.scopes,
        tenantId: request.tenantId,
        performedBy: request.purpose === 'impersonation' ? request.userId : undefined,
        onBehalfOf: request.purpose === 'impersonation' ? request.tenantId : undefined,
      })

      return {
        allowed: true,
        token,
        reason: 'Exchange approved',
        auditEntry: { ...auditBase, allowed: true, reason: `Approved: ${request.purpose}` },
      }
    } catch (err) {
      const reason = err instanceof Error ? err.message : 'Token generation failed'
      return {
        allowed: false,
        token: null,
        reason,
        auditEntry: { ...auditBase, allowed: false, reason },
      }
    }
  }

  /**
   * Validate an incoming cross-domain token.
   * Used by receiving services to verify the token was legitimately issued.
   */
  async validateIncomingToken(token: string, expectedDomain: ClerkDomain): Promise<{
    valid: boolean
    payload: TokenPayload | null
    error: string | null
  }> {
    try {
      const payload = await this.tokenManager.verifyScopedToken(token)

      // Verify the token targets this domain
      if (payload.domain !== expectedDomain) {
        return {
          valid: false,
          payload: null,
          error: `Token targets ${payload.domain}, not ${expectedDomain}`,
        }
      }

      // Verify token hasn't expired (jose does this, but double-check)
      if (payload.exp < Math.floor(Date.now() / 1000)) {
        return { valid: false, payload: null, error: 'Token expired' }
      }

      return { valid: true, payload, error: null }
    } catch (err) {
      return {
        valid: false,
        payload: null,
        error: err instanceof Error ? err.message : 'Token validation failed',
      }
    }
  }
}

/**
 * Create a cross-domain exchange handler for a specific domain
 */
export function createCrossDomainExchange(sourceDomain: ClerkDomain): CrossDomainExchange {
  return new CrossDomainExchange(sourceDomain)
}
