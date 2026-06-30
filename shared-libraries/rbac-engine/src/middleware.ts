/**
 * RBAC Middleware — Permission Enforcement for Next.js API Routes
 * 
 * Wraps API route handlers with domain-aware permission checks.
 * Works with the auth-client ClerkWrapper for token validation.
 */
import { type ClerkDomain } from '@truevow/auth-client'
import { hasPermission, requiresApproval, Permission } from './permissions'
import { ROLE_REGISTRY, RoleLevel, isRoleHigherOrEqual } from './roles'

// ─── Types ────────────────────────────────────────────────────────
export interface RBACContext {
  userId: string
  roleId: string
  domain: ClerkDomain
  tenantId?: string
  isImpersonating: boolean
  performedBy?: string
  onBehalfOf?: string
}

export interface PermissionCheckResult {
  allowed: boolean
  reason: string
  requiresApproval: boolean
  approvalRoles?: string[]
}

// ─── Permission Enforcement ───────────────────────────────────────
/**
 * Check if the current user context has a specific permission.
 * Returns detailed result including approval requirements.
 */
export function checkPermission(
  context: RBACContext,
  permission: Permission
): PermissionCheckResult {
  // Verify role exists
  const roleDef = ROLE_REGISTRY[context.roleId]
  if (!roleDef) {
    return {
      allowed: false,
      reason: `Unknown role: ${context.roleId}`,
      requiresApproval: false,
    }
  }

  // Domain check: role must match the domain
  if (roleDef.domain !== context.domain) {
    return {
      allowed: false,
      reason: `Role ${context.roleId} belongs to domain ${roleDef.domain}, not ${context.domain}`,
      requiresApproval: false,
    }
  }

  // Permission check
  if (!hasPermission(context.roleId, permission, context.domain)) {
    return {
      allowed: false,
      reason: `Role ${context.roleId} (Level ${roleDef.level}) does not have permission: ${permission}`,
      requiresApproval: false,
    }
  }

  // Check if approval is required
  const approvers = requiresApproval(permission)
  if (approvers) {
    return {
      allowed: true,
      reason: `Permission granted but requires approval from: ${approvers.join(', ')}`,
      requiresApproval: true,
      approvalRoles: approvers,
    }
  }

  return {
    allowed: true,
    reason: 'Permission granted',
    requiresApproval: false,
  }
}

/**
 * Require a minimum role level for access.
 * Used for simple guards like "must be Level A or B".
 */
export function requireLevel(
  context: RBACContext,
  minimumLevel: RoleLevel
): PermissionCheckResult {
  if (!isRoleHigherOrEqual(context.roleId, minimumLevel)) {
    return {
      allowed: false,
      reason: `Requires Level ${minimumLevel} or higher. Current: ${context.roleId}`,
      requiresApproval: false,
    }
  }

  return {
    allowed: true,
    reason: `Level check passed (minimum: ${minimumLevel})`,
    requiresApproval: false,
  }
}

/**
 * Create an RBAC guard for Next.js API route handlers.
 * 
 * @example
 * ```typescript
 * import { createRBACGuard, Permission } from '@truevow/rbac-engine'
 * 
 * const guard = createRBACGuard(Permission.BILLING_SET_TIER)
 * 
 * export async function POST(request: Request) {
 *   const context = extractRBACContext(request) // from auth-client
 *   const result = guard(context)
 *   if (!result.allowed) {
 *     return Response.json({ error: result.reason }, { status: 403 })
 *   }
 *   // proceed...
 * }
 * ```
 */
export function createRBACGuard(
  ...requiredPermissions: Permission[]
): (context: RBACContext) => PermissionCheckResult {
  return (context: RBACContext) => {
    for (const perm of requiredPermissions) {
      const result = checkPermission(context, perm)
      if (!result.allowed) return result
    }

    return {
      allowed: true,
      reason: 'All permissions granted',
      requiresApproval: false,
    }
  }
}

/**
 * Enforce impersonation rules:
 * - Only roles with canImpersonate=true can impersonate
 * - Impersonation context must have performed_by and on_behalf_of
 */
export function validateImpersonation(context: RBACContext): PermissionCheckResult {
  if (!context.isImpersonating) {
    return { allowed: true, reason: 'Not impersonating', requiresApproval: false }
  }

  const roleDef = ROLE_REGISTRY[context.roleId]
  if (!roleDef?.canImpersonate) {
    return {
      allowed: false,
      reason: `Role ${context.roleId} cannot impersonate tenants`,
      requiresApproval: false,
    }
  }

  if (!context.performedBy || !context.onBehalfOf) {
    return {
      allowed: false,
      reason: 'Impersonation requires performed_by and on_behalf_of fields',
      requiresApproval: false,
    }
  }

  return {
    allowed: true,
    reason: `Impersonation validated: ${context.performedBy} on behalf of ${context.onBehalfOf}`,
    requiresApproval: false,
  }
}
