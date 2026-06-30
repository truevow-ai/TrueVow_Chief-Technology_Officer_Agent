/**
 * JIT Access Primitives (Shared Library)
 * Reusable just-in-time elevation logic for all TrueVow services.
 */

export interface JitSession {
  id: string;
  userId: string;
  scopes: string[];
  expiresAt: Date;
  status: 'active' | 'expired' | 'revoked';
  createdAt: Date;
  ipAddress: string;
  actions: Array<{ timestamp: Date; action: string; resource: string }>;
}

/**
 * Check if a JIT session is still valid.
 */
export function isSessionValid(session: JitSession): boolean {
  if (session.status !== 'active') return false;
  return new Date() < session.expiresAt;
}

/**
 * Check if a session has a specific scope.
 */
export function hasScope(session: JitSession, scope: string): boolean {
  if (!isSessionValid(session)) return false;
  return session.scopes.includes(scope);
}

/**
 * Calculate remaining time for a session in seconds.
 */
export function remainingSeconds(session: JitSession): number {
  if (!isSessionValid(session)) return 0;
  return Math.max(0, Math.floor((session.expiresAt.getTime() - Date.now()) / 1000));
}

/**
 * Validate elevation request parameters.
 */
export function validateElevationRequest(params: {
  durationMinutes: number;
  maxDurationMinutes: number;
  scopes: string[];
  allowedScopes: string[];
}): { valid: boolean; errors: string[] } {
  const errors: string[] = [];

  if (params.durationMinutes <= 0) {
    errors.push('Duration must be positive');
  }
  if (params.durationMinutes > params.maxDurationMinutes) {
    errors.push(`Duration ${params.durationMinutes}m exceeds max ${params.maxDurationMinutes}m`);
  }
  if (params.scopes.length === 0) {
    errors.push('At least one scope required');
  }

  const invalidScopes = params.scopes.filter(s => !params.allowedScopes.includes(s));
  if (invalidScopes.length > 0) {
    errors.push(`Invalid scopes: ${invalidScopes.join(', ')}`);
  }

  return { valid: errors.length === 0, errors };
}
