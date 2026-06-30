/**
 * @truevow/rbac-engine — Public API
 */

// Roles
export {
  RoleLevel,
  ROLE_REGISTRY,
  getRoleById,
  getRolesByLevel,
  getRolesByDomain,
  isRoleHigherOrEqual,
  canRoleImpersonate,
  type RoleDefinition,
} from './roles'

// Permissions
export {
  Permission,
  PERMISSION_RULES,
  hasPermission,
  requiresApproval,
  getPermissionsForRole,
  type PermissionRule,
} from './permissions'

// Middleware
export {
  checkPermission,
  requireLevel,
  createRBACGuard,
  validateImpersonation,
  type RBACContext,
  type PermissionCheckResult,
} from './middleware'
