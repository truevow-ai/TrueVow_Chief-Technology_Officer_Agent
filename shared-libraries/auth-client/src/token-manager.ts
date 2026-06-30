/**
 * Token Manager — Scoped Token Generation & Validation
 * 
 * Handles:
 * - Service-to-service authentication tokens
 * - Scoped tokens for cross-domain access
 * - CSM impersonation tokens (performed_by / on_behalf_of)
 * - Token TTL enforcement per domain
 */
import * as jose from 'jose'
import { ClerkDomain, getDomainConfig, TrustLevel } from './domain-config'

// ─── Token Types ──────────────────────────────────────────────────
export enum TokenType {
  SESSION = 'session',               // Standard user session
  SERVICE = 'service',               // Service-to-service
  IMPERSONATION = 'impersonation',   // CSM acting on behalf of tenant
  SCOPED = 'scoped',                 // Narrowly scoped for specific operation
}

export interface TokenPayload {
  sub: string           // User or service ID
  type: TokenType
  domain: ClerkDomain
  iss: string           // Issuing service
  aud: string           // Target service/domain
  iat: number           // Issued at
  exp: number           // Expiration
  // Impersonation fields
  performed_by?: string   // CSM user ID
  on_behalf_of?: string   // Tenant ID being impersonated
  // Scoped fields
  scopes?: string[]       // Allowed operations
  tenant_id?: string      // Tenant context
  // Security
  jti: string             // Unique token ID for revocation
}

export interface ScopedTokenRequest {
  issuerId: string        // Service creating the token
  subjectId: string       // User/service the token is for
  targetDomain: ClerkDomain
  type: TokenType
  scopes?: string[]
  tenantId?: string
  performedBy?: string    // For impersonation
  onBehalfOf?: string     // For impersonation
  ttlOverride?: number    // Override default TTL (seconds)
}

// ─── Token Manager ────────────────────────────────────────────────
export class TokenManager {
  private readonly signingSecret: Uint8Array
  private readonly issuerDomain: ClerkDomain

  constructor(domain: ClerkDomain) {
    this.issuerDomain = domain
    // Use a dedicated signing secret per domain
    const secretEnv = this.getSigningSecretEnvKey(domain)
    const secret = process.env[secretEnv]
    if (!secret) {
      throw new Error(`Missing signing secret env var: ${secretEnv}`)
    }
    this.signingSecret = new TextEncoder().encode(secret)
  }

  /**
   * Generate a scoped token for cross-domain or service-to-service auth
   */
  async generateScopedToken(request: ScopedTokenRequest): Promise<string> {
    this.validateTokenRequest(request)

    const domainConfig = getDomainConfig(request.targetDomain)
    const ttl = request.ttlOverride ?? domainConfig.tokenTTLSeconds
    const now = Math.floor(Date.now() / 1000)

    const payload: TokenPayload = {
      sub: request.subjectId,
      type: request.type,
      domain: request.targetDomain,
      iss: request.issuerId,
      aud: request.targetDomain,
      iat: now,
      exp: now + ttl,
      jti: crypto.randomUUID(),
      ...(request.scopes && { scopes: request.scopes }),
      ...(request.tenantId && { tenant_id: request.tenantId }),
      ...(request.performedBy && { performed_by: request.performedBy }),
      ...(request.onBehalfOf && { on_behalf_of: request.onBehalfOf }),
    }

    const jwt = await new jose.SignJWT(payload as unknown as jose.JWTPayload)
      .setProtectedHeader({ alg: 'HS256', typ: 'JWT' })
      .setIssuedAt(payload.iat)
      .setExpirationTime(payload.exp)
      .setJti(payload.jti)
      .sign(this.signingSecret)

    return jwt
  }

  /**
   * Verify and decode a scoped token
   */
  async verifyScopedToken(token: string): Promise<TokenPayload> {
    try {
      const { payload } = await jose.jwtVerify(token, this.signingSecret)
      return payload as unknown as TokenPayload
    } catch (err) {
      if (err instanceof jose.errors.JWTExpired) {
        throw new Error('Token expired')
      }
      if (err instanceof jose.errors.JWSSignatureVerificationFailed) {
        throw new Error('Invalid token signature')
      }
      throw new Error(`Token verification failed: ${err instanceof Error ? err.message : 'Unknown error'}`)
    }
  }

  /**
   * Generate an impersonation token (CSM acting on behalf of tenant)
   * Only allowed from Platform Operators domain
   */
  async generateImpersonationToken(
    csmUserId: string,
    tenantId: string,
    scopes: string[],
    ttlSeconds?: number
  ): Promise<string> {
    if (this.issuerDomain !== ClerkDomain.PLATFORM_OPERATORS) {
      throw new Error('Impersonation tokens can only be issued from Platform Operators domain')
    }

    return this.generateScopedToken({
      issuerId: 'saas-admin',
      subjectId: csmUserId,
      targetDomain: ClerkDomain.TENANTS,
      type: TokenType.IMPERSONATION,
      scopes,
      tenantId,
      performedBy: csmUserId,
      onBehalfOf: tenantId,
      ttlOverride: ttlSeconds ?? 1800, // 30 min default for impersonation
    })
  }

  /**
   * Generate a service-to-service token
   */
  async generateServiceToken(
    sourceService: string,
    targetDomain: ClerkDomain,
    scopes: string[]
  ): Promise<string> {
    return this.generateScopedToken({
      issuerId: sourceService,
      subjectId: `service:${sourceService}`,
      targetDomain,
      type: TokenType.SERVICE,
      scopes,
      ttlOverride: 300, // 5 min for service tokens
    })
  }

  /**
   * Validate a token request before generation
   */
  private validateTokenRequest(request: ScopedTokenRequest): void {
    // Impersonation only from Platform Operators
    if (request.type === TokenType.IMPERSONATION) {
      if (this.issuerDomain !== ClerkDomain.PLATFORM_OPERATORS) {
        throw new Error('Only Platform Operators can issue impersonation tokens')
      }
      if (!request.performedBy || !request.onBehalfOf) {
        throw new Error('Impersonation requires performed_by and on_behalf_of')
      }
    }

    // Sales/Support cannot get tokens for Platform domain
    const targetConfig = getDomainConfig(request.targetDomain)
    if (this.issuerDomain === ClerkDomain.SALES_SUPPORT && targetConfig.trustLevel === TrustLevel.HIGH) {
      throw new Error('Sales/Support domain cannot access Platform Operators domain')
    }

    // Tenant domain cannot get tokens for other domains
    if (this.issuerDomain === ClerkDomain.TENANTS && request.targetDomain !== ClerkDomain.TENANTS) {
      throw new Error('Tenant domain can only issue tokens within its own domain')
    }
  }

  /**
   * Get the env var name for the signing secret based on domain
   */
  private getSigningSecretEnvKey(domain: ClerkDomain): string {
    switch (domain) {
      case ClerkDomain.PLATFORM_OPERATORS: return 'TOKEN_SIGNING_SECRET_APP1'
      case ClerkDomain.SALES_SUPPORT: return 'TOKEN_SIGNING_SECRET_APP2'
      case ClerkDomain.TENANTS: return 'TOKEN_SIGNING_SECRET_APP3'
    }
  }
}

/**
 * Create a TokenManager for a specific domain
 */
export function createTokenManager(domain: ClerkDomain): TokenManager {
  return new TokenManager(domain)
}
