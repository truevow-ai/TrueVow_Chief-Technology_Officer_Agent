/**
 * @truevow/auth-client — Public API
 * 
 * Universal Clerk authentication wrapper for TrueVow 3-domain architecture.
 * All services import from this package instead of @clerk/nextjs directly.
 */

// Domain configuration
export {
  ClerkDomain,
  TrustLevel,
  SERVICE_DOMAIN_MAP,
  getDomainConfig,
  getServiceDomain,
  isCrossDomainAllowed,
  type DomainConfig,
} from './domain-config'

// Clerk wrapper
export {
  ClerkWrapper,
  createAuthClient,
  type AuthenticatedUser,
  type AuthResult,
  type ClerkWrapperConfig,
} from './clerk-wrapper'

// Token management
export {
  TokenManager,
  TokenType,
  createTokenManager,
  type TokenPayload,
  type ScopedTokenRequest,
} from './token-manager'

// Cross-domain exchange
export {
  CrossDomainExchange,
  createCrossDomainExchange,
  type CrossDomainRequest,
  type CrossDomainResult,
  type AuditEntry,
} from './cross-domain'
