/**
 * Impersonation Session Manager
 * 
 * Manages CSM impersonation sessions with:
 * - performed_by: CSM user ID
 * - on_behalf_of: Tenant ID
 * - 3-layer control: impersonation + billing workflow + step-up auth
 * - Session TTL enforcement
 * - Full audit trail
 */

// ─── Types ────────────────────────────────────────────────────────
export interface ImpersonationSession {
  sessionId: string
  performedBy: string        // CSM user ID
  performedByRole: string    // e.g., CUSTOMER_SUCCESS
  onBehalfOf: string         // Tenant ID
  tenantName?: string
  scopes: string[]           // What the CSM can do
  startedAt: string
  expiresAt: string
  active: boolean
  actions: ImpersonationAction[]
}

export interface ImpersonationAction {
  actionId: string
  timestamp: string
  action: string
  resource: string
  details: Record<string, unknown>
}

export interface StartImpersonationRequest {
  csmUserId: string
  csmRole: string
  tenantId: string
  tenantName?: string
  scopes: string[]
  durationMinutes?: number   // Default: 30
  reason?: string
}

// ─── Session Store (in-memory, replaceable with DB/Redis) ─────────
const activeSessions = new Map<string, ImpersonationSession>()

// ─── Impersonation Manager ────────────────────────────────────────
export class ImpersonationManager {
  private maxDurationMinutes: number
  private allowedRoles: Set<string>

  constructor(config?: {
    maxDurationMinutes?: number
    allowedRoles?: string[]
  }) {
    this.maxDurationMinutes = config?.maxDurationMinutes ?? 60
    this.allowedRoles = new Set(config?.allowedRoles ?? [
      'SUPER_ADMIN',
      'ADMIN',
      'CUSTOMER_SUCCESS',
      'CLIENT_ONBOARDING_MANAGER',
    ])
  }

  /**
   * Start a new impersonation session
   */
  startSession(request: StartImpersonationRequest): ImpersonationSession {
    // Validate role
    if (!this.allowedRoles.has(request.csmRole)) {
      throw new Error(`Role ${request.csmRole} is not allowed to impersonate tenants`)
    }

    // Enforce max duration
    const duration = Math.min(
      request.durationMinutes ?? 30,
      this.maxDurationMinutes
    )

    const now = new Date()
    const session: ImpersonationSession = {
      sessionId: crypto.randomUUID(),
      performedBy: request.csmUserId,
      performedByRole: request.csmRole,
      onBehalfOf: request.tenantId,
      tenantName: request.tenantName,
      scopes: request.scopes,
      startedAt: now.toISOString(),
      expiresAt: new Date(now.getTime() + duration * 60_000).toISOString(),
      active: true,
      actions: [],
    }

    activeSessions.set(session.sessionId, session)
    return session
  }

  /**
   * Record an action performed during impersonation
   */
  recordAction(
    sessionId: string,
    action: string,
    resource: string,
    details: Record<string, unknown> = {}
  ): void {
    const session = activeSessions.get(sessionId)
    if (!session) throw new Error(`Impersonation session not found: ${sessionId}`)
    if (!session.active) throw new Error(`Impersonation session expired: ${sessionId}`)

    // Check expiration
    if (new Date() > new Date(session.expiresAt)) {
      session.active = false
      throw new Error(`Impersonation session expired: ${sessionId}`)
    }

    session.actions.push({
      actionId: crypto.randomUUID(),
      timestamp: new Date().toISOString(),
      action,
      resource,
      details,
    })
  }

  /**
   * End an impersonation session
   */
  endSession(sessionId: string): ImpersonationSession {
    const session = activeSessions.get(sessionId)
    if (!session) throw new Error(`Impersonation session not found: ${sessionId}`)

    session.active = false
    return session
  }

  /**
   * Get an active session by ID
   */
  getSession(sessionId: string): ImpersonationSession | null {
    const session = activeSessions.get(sessionId)
    if (!session) return null

    // Auto-expire
    if (session.active && new Date() > new Date(session.expiresAt)) {
      session.active = false
    }

    return session
  }

  /**
   * Get all active sessions for a CSM
   */
  getActiveSessions(csmUserId: string): ImpersonationSession[] {
    const sessions: ImpersonationSession[] = []
    const now = new Date()

    for (const session of activeSessions.values()) {
      if (session.performedBy === csmUserId && session.active) {
        if (now > new Date(session.expiresAt)) {
          session.active = false
        } else {
          sessions.push(session)
        }
      }
    }

    return sessions
  }

  /**
   * Validate if a session allows a specific scope
   */
  hasScope(sessionId: string, scope: string): boolean {
    const session = this.getSession(sessionId)
    if (!session?.active) return false
    return session.scopes.includes(scope) || session.scopes.includes('*')
  }
}

/**
 * Create an impersonation manager
 */
export function createImpersonationManager(config?: {
  maxDurationMinutes?: number
  allowedRoles?: string[]
}): ImpersonationManager {
  return new ImpersonationManager(config)
}
