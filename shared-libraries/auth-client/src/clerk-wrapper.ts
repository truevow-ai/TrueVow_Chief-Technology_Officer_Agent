/**
 * Universal Clerk Wrapper for TrueVow 3-Domain Architecture
 * 
 * Every service imports this instead of @clerk/nextjs directly.
 * The wrapper auto-selects the correct Clerk app based on the
 * service's domain assignment.
 */
import { ClerkDomain, getDomainConfig, getServiceDomain, type DomainConfig } from './domain-config'

// ─── Types ────────────────────────────────────────────────────────
export interface AuthenticatedUser {
  userId: string
  email: string | null
  role: string
  domain: ClerkDomain
  orgId: string | null
  tenantId: string | null
  sessionId: string
  metadata: Record<string, unknown>
}

export interface AuthResult {
  authenticated: boolean
  user: AuthenticatedUser | null
  error: string | null
  domain: ClerkDomain
}

export interface ClerkWrapperConfig {
  serviceId: string
  onAuthFailure?: (error: string) => void
  onAuthSuccess?: (user: AuthenticatedUser) => void
}

// ─── Wrapper Class ────────────────────────────────────────────────
export class ClerkWrapper {
  private readonly serviceId: string
  private readonly domain: ClerkDomain
  private readonly domainConfig: DomainConfig
  private readonly onAuthFailure?: (error: string) => void
  private readonly onAuthSuccess?: (user: AuthenticatedUser) => void

  constructor(config: ClerkWrapperConfig) {
    this.serviceId = config.serviceId
    this.domain = getServiceDomain(config.serviceId)
    this.domainConfig = getDomainConfig(this.domain)
    this.onAuthFailure = config.onAuthFailure
    this.onAuthSuccess = config.onAuthSuccess
  }

  /**
   * Get the domain this service belongs to
   */
  getDomain(): ClerkDomain {
    return this.domain
  }

  /**
   * Get the full domain configuration
   */
  getConfig(): DomainConfig {
    return this.domainConfig
  }

  /**
   * Validate a session token from an incoming request.
   * Uses the Clerk Backend SDK to verify the JWT against
   * this service's Clerk app keys.
   */
  async verifyToken(token: string): Promise<AuthResult> {
    try {
      const { verifyToken: clerkVerifyToken } = await import('@clerk/backend')

      const { sub: userId, ...claims } = await clerkVerifyToken(token, {
        secretKey: this.domainConfig.clerkSecretKey,
      })

      const user: AuthenticatedUser = {
        userId,
        email: (claims as Record<string, unknown>).email as string | null ?? null,
        role: ((claims as Record<string, unknown>).metadata as Record<string, unknown>)?.role as string ?? 'unknown',
        domain: this.domain,
        orgId: (claims as Record<string, unknown>).org_id as string | null ?? null,
        tenantId: this.extractTenantId(claims as Record<string, unknown>),
        sessionId: (claims as Record<string, unknown>).sid as string ?? '',
        metadata: (claims as Record<string, unknown>).metadata as Record<string, unknown> ?? {},
      }

      this.onAuthSuccess?.(user)
      return { authenticated: true, user, error: null, domain: this.domain }
    } catch (err) {
      const errorMsg = err instanceof Error ? err.message : 'Token verification failed'
      this.onAuthFailure?.(errorMsg)
      return { authenticated: false, user: null, error: errorMsg, domain: this.domain }
    }
  }

  /**
   * Check if this service is allowed to access a target domain
   */
  canAccessDomain(targetDomain: ClerkDomain): boolean {
    // Same domain always allowed
    if (this.domain === targetDomain) return true

    // Platform operators can access anything via scoped tokens
    if (this.domain === ClerkDomain.PLATFORM_OPERATORS) return true

    // Cross-domain blocked for Sales/Support and Tenants
    return false
  }

  /**
   * Check if this service requires PII redaction on responses
   */
  requiresPiiRedaction(): boolean {
    return this.domainConfig.piiRedactionRequired
  }

  /**
   * Check if LLM access is allowed for this service's domain
   */
  isLlmAllowed(): boolean {
    return this.domainConfig.llmAccessAllowed
  }

  /**
   * Check if direct tenant DB access is allowed
   */
  canAccessTenantDB(): boolean {
    return this.domainConfig.allowDirectTenantDB
  }

  /**
   * Get the Clerk publishable key for client-side init
   */
  getPublishableKey(): string {
    return this.domainConfig.clerkPublishableKey
  }

  /**
   * Extract tenant ID from JWT claims based on domain
   */
  private extractTenantId(claims: Record<string, unknown>): string | null {
    // Tenants domain: tenant_id is in the claims directly
    if (this.domain === ClerkDomain.TENANTS) {
      return (claims.tenant_id as string) ?? (claims.org_id as string) ?? null
    }

    // Platform operators may have tenant context during impersonation
    if (this.domain === ClerkDomain.PLATFORM_OPERATORS) {
      const metadata = claims.metadata as Record<string, unknown> | undefined
      return (metadata?.impersonating_tenant as string) ?? null
    }

    // Sales/Support: never get direct tenant ID
    return null
  }
}

// ─── Factory Function ─────────────────────────────────────────────
/**
 * Create a ClerkWrapper instance for a specific service.
 * This is the main entry point all services use.
 * 
 * @example
 * ```typescript
 * import { createAuthClient } from '@truevow/auth-client'
 * 
 * const auth = createAuthClient('saas-admin')
 * const result = await auth.verifyToken(request.headers.get('Authorization'))
 * ```
 */
export function createAuthClient(serviceId: string, options?: Omit<ClerkWrapperConfig, 'serviceId'>): ClerkWrapper {
  return new ClerkWrapper({ serviceId, ...options })
}
