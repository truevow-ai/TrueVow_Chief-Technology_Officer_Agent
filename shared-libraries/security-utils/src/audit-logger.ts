/**
 * Audit Logger — Structured Security Event Logging
 * 
 * Captures all security-relevant events across domains:
 * - Authentication events (login, logout, token exchange)
 * - Authorization events (permission checks, denials)
 * - Impersonation sessions (start, end, actions)
 * - Cross-domain access attempts
 * - PII redaction events
 */
import { type ClerkDomain } from '@truevow/auth-client'

// ─── Event Types ──────────────────────────────────────────────────
export enum AuditEventType {
  // Auth
  AUTH_LOGIN = 'auth.login',
  AUTH_LOGOUT = 'auth.logout',
  AUTH_TOKEN_EXCHANGE = 'auth.token_exchange',
  AUTH_TOKEN_EXPIRED = 'auth.token_expired',
  AUTH_MFA_CHALLENGE = 'auth.mfa_challenge',
  AUTH_MFA_SUCCESS = 'auth.mfa_success',
  AUTH_MFA_FAILURE = 'auth.mfa_failure',

  // RBAC
  RBAC_PERMISSION_GRANTED = 'rbac.permission_granted',
  RBAC_PERMISSION_DENIED = 'rbac.permission_denied',
  RBAC_ROLE_CHANGED = 'rbac.role_changed',

  // Impersonation
  IMPERSONATION_START = 'impersonation.start',
  IMPERSONATION_END = 'impersonation.end',
  IMPERSONATION_ACTION = 'impersonation.action',
  IMPERSONATION_DENIED = 'impersonation.denied',

  // Cross-Domain
  CROSS_DOMAIN_REQUEST = 'cross_domain.request',
  CROSS_DOMAIN_GRANTED = 'cross_domain.granted',
  CROSS_DOMAIN_DENIED = 'cross_domain.denied',

  // Data Access
  DATA_ACCESS = 'data.access',
  DATA_MODIFICATION = 'data.modification',
  DATA_EXPORT = 'data.export',

  // PII
  PII_REDACTION = 'pii.redaction',
  PII_ACCESS_ATTEMPT = 'pii.access_attempt',

  // System
  SYSTEM_CONFIG_CHANGE = 'system.config_change',
  SYSTEM_ERROR = 'system.error',
}

// ─── Audit Entry ──────────────────────────────────────────────────
export interface AuditLogEntry {
  id: string
  timestamp: string
  eventType: AuditEventType
  domain: ClerkDomain
  userId: string
  roleId?: string
  tenantId?: string
  serviceId: string
  action: string
  resource?: string
  outcome: 'success' | 'failure' | 'denied'
  metadata: Record<string, unknown>
  // Impersonation context
  performedBy?: string
  onBehalfOf?: string
  // Request context
  ipAddress?: string
  userAgent?: string
  requestId?: string
}

// ─── Logger Interface ─────────────────────────────────────────────
export interface AuditLogSink {
  write(entry: AuditLogEntry): Promise<void>
}

// ─── Console Sink (default, replaceable) ──────────────────────────
class ConsoleAuditSink implements AuditLogSink {
  async write(entry: AuditLogEntry): Promise<void> {
    const level = entry.outcome === 'denied' ? 'warn' : 'info'
    console[level](`[AUDIT] ${entry.eventType}`, {
      userId: entry.userId,
      domain: entry.domain,
      action: entry.action,
      outcome: entry.outcome,
      ...(entry.performedBy && { performedBy: entry.performedBy }),
      ...(entry.onBehalfOf && { onBehalfOf: entry.onBehalfOf }),
    })
  }
}

// ─── Audit Logger Class ───────────────────────────────────────────
export class AuditLogger {
  private sinks: AuditLogSink[]
  private serviceId: string
  private domain: ClerkDomain

  constructor(serviceId: string, domain: ClerkDomain, sinks?: AuditLogSink[]) {
    this.serviceId = serviceId
    this.domain = domain
    this.sinks = sinks ?? [new ConsoleAuditSink()]
  }

  /**
   * Log a security audit event
   */
  async log(
    eventType: AuditEventType,
    params: {
      userId: string
      action: string
      outcome: 'success' | 'failure' | 'denied'
      roleId?: string
      tenantId?: string
      resource?: string
      performedBy?: string
      onBehalfOf?: string
      metadata?: Record<string, unknown>
      ipAddress?: string
      userAgent?: string
      requestId?: string
    }
  ): Promise<void> {
    const entry: AuditLogEntry = {
      id: crypto.randomUUID(),
      timestamp: new Date().toISOString(),
      eventType,
      domain: this.domain,
      serviceId: this.serviceId,
      userId: params.userId,
      action: params.action,
      outcome: params.outcome,
      roleId: params.roleId,
      tenantId: params.tenantId,
      resource: params.resource,
      performedBy: params.performedBy,
      onBehalfOf: params.onBehalfOf,
      metadata: params.metadata ?? {},
      ipAddress: params.ipAddress,
      userAgent: params.userAgent,
      requestId: params.requestId,
    }

    // Write to all sinks (fire-and-forget for non-critical, await for critical)
    await Promise.allSettled(this.sinks.map(sink => sink.write(entry)))
  }

  /**
   * Add a custom log sink (e.g., Supabase, external SIEM)
   */
  addSink(sink: AuditLogSink): void {
    this.sinks.push(sink)
  }
}

/**
 * Create an audit logger for a specific service
 */
export function createAuditLogger(
  serviceId: string,
  domain: ClerkDomain,
  sinks?: AuditLogSink[]
): AuditLogger {
  return new AuditLogger(serviceId, domain, sinks)
}
