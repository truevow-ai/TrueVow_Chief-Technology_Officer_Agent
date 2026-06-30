/**
 * Permission Matrix — Domain-Aware Permission Checks
 * 
 * Maps permissions to roles and domains, enforcing:
 * - Level A: can do anything in their domain
 * - Level B: operational permissions (CSM, onboarding)
 * - Level C: day-to-day operations (sales, support)
 * - Level D: tenant-scoped only
 * 
 * Also enforces approval gates:
 * - Finance approval needed for: discounts, invoice adjustments, reimbursements
 * - Customer self-service: upgrades/downgrades — no approval needed
 */
import { ClerkDomain } from '@truevow/auth-client'
import { RoleLevel, ROLE_REGISTRY, type RoleDefinition } from './roles'

// ─── Permission IDs ───────────────────────────────────────────────
export enum Permission {
  // Tenant Management
  TENANT_CREATE = 'tenant:create',
  TENANT_READ = 'tenant:read',
  TENANT_UPDATE = 'tenant:update',
  TENANT_DELETE = 'tenant:delete',
  TENANT_IMPERSONATE = 'tenant:impersonate',

  // Billing & Subscriptions
  BILLING_READ = 'billing:read',
  BILLING_SET_TIER = 'billing:set_tier',
  BILLING_ADJUST_INVOICE = 'billing:adjust_invoice',
  BILLING_APPLY_DISCOUNT = 'billing:apply_discount',
  BILLING_PROCESS_REIMBURSEMENT = 'billing:process_reimbursement',
  BILLING_SELF_SERVICE_CHANGE = 'billing:self_service_change',

  // User Management
  USER_CREATE = 'user:create',
  USER_READ = 'user:read',
  USER_UPDATE = 'user:update',
  USER_DELETE = 'user:delete',
  USER_MANAGE_ROLES = 'user:manage_roles',

  // Support
  TICKET_CREATE = 'ticket:create',
  TICKET_READ = 'ticket:read',
  TICKET_ASSIGN = 'ticket:assign',
  TICKET_CLOSE = 'ticket:close',

  // Sales CRM
  LEAD_CREATE = 'lead:create',
  LEAD_READ = 'lead:read',
  LEAD_UPDATE = 'lead:update',

  // Settings
  SETTINGS_READ = 'settings:read',
  SETTINGS_UPDATE = 'settings:update',

  // Audit
  AUDIT_READ = 'audit:read',

  // Integrations
  INTEGRATION_MANAGE = 'integration:manage',
}

// ─── Permission-to-Role Mapping ───────────────────────────────────
export interface PermissionRule {
  permission: Permission
  allowedLevels: RoleLevel[]
  allowedRoles?: string[]        // Override: specific roles (if not by level)
  requiresApproval?: string[]    // Roles that must approve
  domainRestriction?: ClerkDomain[]  // Only these domains
}

export const PERMISSION_RULES: PermissionRule[] = [
  // Tenant Management — Level A + B only
  { permission: Permission.TENANT_CREATE, allowedLevels: [RoleLevel.A, RoleLevel.B] },
  { permission: Permission.TENANT_READ, allowedLevels: [RoleLevel.A, RoleLevel.B, RoleLevel.C] },
  { permission: Permission.TENANT_UPDATE, allowedLevels: [RoleLevel.A, RoleLevel.B] },
  { permission: Permission.TENANT_DELETE, allowedLevels: [RoleLevel.A] },
  { permission: Permission.TENANT_IMPERSONATE, allowedLevels: [RoleLevel.A, RoleLevel.B], allowedRoles: ['SUPER_ADMIN', 'ADMIN', 'CUSTOMER_SUCCESS', 'CLIENT_ONBOARDING_MANAGER'] },

  // Billing — Level A sets tiers; Finance approves adjustments
  { permission: Permission.BILLING_READ, allowedLevels: [RoleLevel.A, RoleLevel.B, RoleLevel.D] },
  { permission: Permission.BILLING_SET_TIER, allowedLevels: [RoleLevel.A], allowedRoles: ['SUPER_ADMIN', 'ADMIN', 'FINANCE'] },
  { permission: Permission.BILLING_ADJUST_INVOICE, allowedLevels: [RoleLevel.A], requiresApproval: ['FINANCE', 'ADMIN'] },
  { permission: Permission.BILLING_APPLY_DISCOUNT, allowedLevels: [RoleLevel.A], requiresApproval: ['FINANCE', 'ADMIN', 'MANAGEMENT'] },
  { permission: Permission.BILLING_PROCESS_REIMBURSEMENT, allowedLevels: [RoleLevel.A], requiresApproval: ['FINANCE'] },
  // Self-service: tenants can upgrade/downgrade without approval
  { permission: Permission.BILLING_SELF_SERVICE_CHANGE, allowedLevels: [RoleLevel.D], allowedRoles: ['OWNER', 'BILLING_ADMIN'], domainRestriction: [ClerkDomain.TENANTS] },

  // User Management — Level A full, Level B read, Level D own tenant
  { permission: Permission.USER_CREATE, allowedLevels: [RoleLevel.A] },
  { permission: Permission.USER_READ, allowedLevels: [RoleLevel.A, RoleLevel.B, RoleLevel.C] },
  { permission: Permission.USER_UPDATE, allowedLevels: [RoleLevel.A, RoleLevel.B] },
  { permission: Permission.USER_DELETE, allowedLevels: [RoleLevel.A] },
  { permission: Permission.USER_MANAGE_ROLES, allowedLevels: [RoleLevel.A] },

  // Support — Level B + C + D
  { permission: Permission.TICKET_CREATE, allowedLevels: [RoleLevel.A, RoleLevel.B, RoleLevel.C, RoleLevel.D] },
  { permission: Permission.TICKET_READ, allowedLevels: [RoleLevel.A, RoleLevel.B, RoleLevel.C, RoleLevel.D] },
  { permission: Permission.TICKET_ASSIGN, allowedLevels: [RoleLevel.A, RoleLevel.B, RoleLevel.C] },
  { permission: Permission.TICKET_CLOSE, allowedLevels: [RoleLevel.A, RoleLevel.B, RoleLevel.C] },

  // Sales CRM — LLM Zone (Clerk App 2)
  { permission: Permission.LEAD_CREATE, allowedLevels: [RoleLevel.A, RoleLevel.C], domainRestriction: [ClerkDomain.PLATFORM_OPERATORS, ClerkDomain.SALES_SUPPORT] },
  { permission: Permission.LEAD_READ, allowedLevels: [RoleLevel.A, RoleLevel.B, RoleLevel.C], domainRestriction: [ClerkDomain.PLATFORM_OPERATORS, ClerkDomain.SALES_SUPPORT] },
  { permission: Permission.LEAD_UPDATE, allowedLevels: [RoleLevel.A, RoleLevel.C], domainRestriction: [ClerkDomain.PLATFORM_OPERATORS, ClerkDomain.SALES_SUPPORT] },

  // Settings — Level A only
  { permission: Permission.SETTINGS_READ, allowedLevels: [RoleLevel.A, RoleLevel.B] },
  { permission: Permission.SETTINGS_UPDATE, allowedLevels: [RoleLevel.A] },

  // Audit — Level A only
  { permission: Permission.AUDIT_READ, allowedLevels: [RoleLevel.A] },

  // Integrations — Level A only
  { permission: Permission.INTEGRATION_MANAGE, allowedLevels: [RoleLevel.A] },
]

// ─── Permission Check Functions ───────────────────────────────────
export function hasPermission(
  roleId: string,
  permission: Permission,
  domain?: ClerkDomain
): boolean {
  const roleDef = ROLE_REGISTRY[roleId]
  if (!roleDef) return false

  const rule = PERMISSION_RULES.find(r => r.permission === permission)
  if (!rule) return false

  // Domain restriction check
  if (rule.domainRestriction && domain) {
    if (!rule.domainRestriction.includes(domain)) return false
  }

  // Specific role override
  if (rule.allowedRoles) {
    return rule.allowedRoles.includes(roleId)
  }

  // Level-based check
  return rule.allowedLevels.includes(roleDef.level)
}

export function requiresApproval(permission: Permission): string[] | null {
  const rule = PERMISSION_RULES.find(r => r.permission === permission)
  return rule?.requiresApproval ?? null
}

export function getPermissionsForRole(roleId: string): Permission[] {
  const roleDef = ROLE_REGISTRY[roleId]
  if (!roleDef) return []

  return PERMISSION_RULES
    .filter(rule => {
      if (rule.allowedRoles) return rule.allowedRoles.includes(roleId)
      return rule.allowedLevels.includes(roleDef.level)
    })
    .map(rule => rule.permission)
}
