/**
 * TrueVow 3-Domain Clerk Authentication Configuration
 * Maps services to their Clerk application domains
 */

// ─── Domain Identifiers ───────────────────────────────────────────
export enum ClerkDomain {
  PLATFORM_OPERATORS = 'platform-operators',   // Clerk App 1 — HIGH TRUST
  SALES_SUPPORT = 'sales-support',             // Clerk App 2 — LLM ZONE
  TENANTS = 'tenants',                         // Clerk App 3 — EXTERNAL
}

// ─── Trust Levels ─────────────────────────────────────────────────
export enum TrustLevel {
  HIGH = 'high',       // Platform operators — full internal access
  MEDIUM = 'medium',   // Sales & First-Line Support — scoped, LLM zone
  EXTERNAL = 'external' // Tenants & customers — tenant-scoped only
}

// ─── Service-to-Domain Mapping ────────────────────────────────────
export const SERVICE_DOMAIN_MAP: Record<string, ClerkDomain> = {
  // Clerk App 1 — Platform Operators (HIGH TRUST)
  'saas-admin': ClerkDomain.PLATFORM_OPERATORS,
  'internal-ops': ClerkDomain.PLATFORM_OPERATORS,
  'cs-support-core': ClerkDomain.PLATFORM_OPERATORS,
  'financial-management': ClerkDomain.PLATFORM_OPERATORS,
  'billing-service': ClerkDomain.PLATFORM_OPERATORS,

  // Clerk App 2 — Sales & First-Line Support (LLM ZONE)
  'sales-ops': ClerkDomain.SALES_SUPPORT,
  'first-line-support': ClerkDomain.SALES_SUPPORT,

  // Clerk App 3 — Tenants & Customers (EXTERNAL)
  'tenant-app': ClerkDomain.TENANTS,
  'customer-portal': ClerkDomain.TENANTS,
  'settle': ClerkDomain.TENANTS,
  'connect': ClerkDomain.TENANTS,
  'verify': ClerkDomain.TENANTS,
  'draft': ClerkDomain.TENANTS,
} as const

// ─── Domain Configuration ─────────────────────────────────────────
export interface DomainConfig {
  domain: ClerkDomain
  trustLevel: TrustLevel
  clerkPublishableKey: string
  clerkSecretKey: string
  allowedOrigins: string[]
  tokenTTLSeconds: number
  requireMFA: boolean
  allowDirectTenantDB: boolean
  piiRedactionRequired: boolean
  llmAccessAllowed: boolean
}

/**
 * Get domain configuration from environment variables
 * Each Clerk app has its own set of keys in env
 */
export function getDomainConfig(domain: ClerkDomain): DomainConfig {
  switch (domain) {
    case ClerkDomain.PLATFORM_OPERATORS:
      return {
        domain,
        trustLevel: TrustLevel.HIGH,
        clerkPublishableKey: process.env.CLERK_APP1_PUBLISHABLE_KEY || '',
        clerkSecretKey: process.env.CLERK_APP1_SECRET_KEY || '',
        allowedOrigins: (process.env.CLERK_APP1_ALLOWED_ORIGINS || '').split(',').filter(Boolean),
        tokenTTLSeconds: 1800, // 30 min
        requireMFA: false,     // MFA on step-up only
        allowDirectTenantDB: true,
        piiRedactionRequired: false,
        llmAccessAllowed: false,
      }

    case ClerkDomain.SALES_SUPPORT:
      return {
        domain,
        trustLevel: TrustLevel.MEDIUM,
        clerkPublishableKey: process.env.CLERK_APP2_PUBLISHABLE_KEY || '',
        clerkSecretKey: process.env.CLERK_APP2_SECRET_KEY || '',
        allowedOrigins: (process.env.CLERK_APP2_ALLOWED_ORIGINS || '').split(',').filter(Boolean),
        tokenTTLSeconds: 900,  // 15 min — shorter for LLM zone
        requireMFA: false,
        allowDirectTenantDB: false,   // BLOCKED — must use narrow APIs
        piiRedactionRequired: true,   // All responses PII-redacted
        llmAccessAllowed: true,       // Can call LLM providers
      }

    case ClerkDomain.TENANTS:
      return {
        domain,
        trustLevel: TrustLevel.EXTERNAL,
        clerkPublishableKey: process.env.CLERK_APP3_PUBLISHABLE_KEY || '',
        clerkSecretKey: process.env.CLERK_APP3_SECRET_KEY || '',
        allowedOrigins: (process.env.CLERK_APP3_ALLOWED_ORIGINS || '').split(',').filter(Boolean),
        tokenTTLSeconds: 1800, // 30 min
        requireMFA: false,
        allowDirectTenantDB: true,    // Tenant-scoped access to own DB
        piiRedactionRequired: false,
        llmAccessAllowed: false,
      }
  }
}

/**
 * Resolve which Clerk domain a service belongs to
 */
export function getServiceDomain(serviceId: string): ClerkDomain {
  const domain = SERVICE_DOMAIN_MAP[serviceId]
  if (!domain) {
    throw new Error(`Unknown service: ${serviceId}. Must be one of: ${Object.keys(SERVICE_DOMAIN_MAP).join(', ')}`)
  }
  return domain
}

/**
 * Check if cross-domain access is allowed between two domains
 */
export function isCrossDomainAllowed(sourceDomain: ClerkDomain, targetDomain: ClerkDomain): boolean {
  // Platform operators can access any domain (via scoped tokens)
  if (sourceDomain === ClerkDomain.PLATFORM_OPERATORS) return true

  // Sales/Support CANNOT access Platform or Tenants directly
  if (sourceDomain === ClerkDomain.SALES_SUPPORT) return false

  // Tenants CANNOT access Platform or Sales directly
  if (sourceDomain === ClerkDomain.TENANTS) return false

  return sourceDomain === targetDomain
}
