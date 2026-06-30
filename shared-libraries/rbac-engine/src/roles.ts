/**
 * TrueVow Role Hierarchy — Level A through D
 * 
 * Aligns with existing lib/rbac-constants.ts roles but adds
 * domain-aware trust levels for the 3-Clerk architecture.
 * 
 * Level A: Platform Admin (God mode — SaaS Admin, Finance, RevOps)
 * Level B: Operational (CSM, Sales Manager, Support Lead)
 * Level C: Standard Staff (Sales Rep, Support Agent, Operations)
 * Level D: External (Tenant Admin, Attorney, Paralegal, Client)
 */
import { ClerkDomain } from '@truevow/auth-client'

// ─── Trust Level Hierarchy ────────────────────────────────────────
export enum RoleLevel {
  A = 'A',  // Platform Admin — highest trust
  B = 'B',  // Operational — elevated privileges
  C = 'C',  // Standard Staff — day-to-day operations
  D = 'D',  // External — tenant-scoped only
}

// ─── Role Definitions ─────────────────────────────────────────────
export interface RoleDefinition {
  id: string
  label: string
  level: RoleLevel
  domain: ClerkDomain
  canImpersonate: boolean
  requiresStepUpAuth: boolean
  maxSessionMinutes: number
  description: string
}

/**
 * Complete role registry mapping role IDs to their definitions.
 * These align with the roles in SaaS Admin's lib/rbac-constants.ts
 */
export const ROLE_REGISTRY: Record<string, RoleDefinition> = {
  // ─── Level A: Platform Admin (Clerk App 1) ──────────────────
  SUPER_ADMIN: {
    id: 'SUPER_ADMIN',
    label: 'Super Administrator',
    level: RoleLevel.A,
    domain: ClerkDomain.PLATFORM_OPERATORS,
    canImpersonate: true,
    requiresStepUpAuth: false,
    maxSessionMinutes: 480,
    description: 'Full platform access. Can configure all services, manage billing, and impersonate tenants.',
  },
  ADMIN: {
    id: 'ADMIN',
    label: 'Administrator',
    level: RoleLevel.A,
    domain: ClerkDomain.PLATFORM_OPERATORS,
    canImpersonate: true,
    requiresStepUpAuth: false,
    maxSessionMinutes: 480,
    description: 'Platform admin with full operational access.',
  },
  FINANCE: {
    id: 'FINANCE',
    label: 'Finance',
    level: RoleLevel.A,
    domain: ClerkDomain.PLATFORM_OPERATORS,
    canImpersonate: false,
    requiresStepUpAuth: true,
    maxSessionMinutes: 240,
    description: 'Financial operations: billing, invoicing, discounts, reimbursements. Step-up auth for adjustments.',
  },
  MANAGEMENT: {
    id: 'MANAGEMENT',
    label: 'Management',
    level: RoleLevel.A,
    domain: ClerkDomain.PLATFORM_OPERATORS,
    canImpersonate: false,
    requiresStepUpAuth: false,
    maxSessionMinutes: 480,
    description: 'Regional and executive management oversight.',
  },

  // ─── Level B: Operational (Clerk App 1) ─────────────────────
  CUSTOMER_SUCCESS: {
    id: 'CUSTOMER_SUCCESS',
    label: 'Customer Success Manager',
    level: RoleLevel.B,
    domain: ClerkDomain.PLATFORM_OPERATORS,
    canImpersonate: true,
    requiresStepUpAuth: false,
    maxSessionMinutes: 480,
    description: 'CSM: tenant config, plan changes, impersonation. performed_by: CSM, on_behalf_of: Tenant.',
  },
  CLIENT_ONBOARDING_MANAGER: {
    id: 'CLIENT_ONBOARDING_MANAGER',
    label: 'Client Onboarding Manager',
    level: RoleLevel.B,
    domain: ClerkDomain.PLATFORM_OPERATORS,
    canImpersonate: true,
    requiresStepUpAuth: false,
    maxSessionMinutes: 480,
    description: '3-day setup window, customer sign-off before go-live.',
  },
  OPERATIONS: {
    id: 'OPERATIONS',
    label: 'Operations',
    level: RoleLevel.B,
    domain: ClerkDomain.PLATFORM_OPERATORS,
    canImpersonate: false,
    requiresStepUpAuth: false,
    maxSessionMinutes: 480,
    description: 'Internal operations management.',
  },

  // ─── Level C: Standard Staff (Clerk App 1 + App 2) ─────────
  SALES: {
    id: 'SALES',
    label: 'Sales Representative',
    level: RoleLevel.C,
    domain: ClerkDomain.SALES_SUPPORT,
    canImpersonate: false,
    requiresStepUpAuth: false,
    maxSessionMinutes: 480,
    description: 'Sales CRM operations. LLM zone — PII redaction enforced.',
  },
  SUPPORT: {
    id: 'SUPPORT',
    label: 'Support Agent',
    level: RoleLevel.C,
    domain: ClerkDomain.SALES_SUPPORT,
    canImpersonate: false,
    requiresStepUpAuth: false,
    maxSessionMinutes: 480,
    description: 'First-line support. LLM zone — narrow APIs only, no direct tenant DB.',
  },
  STAFF: {
    id: 'STAFF',
    label: 'Staff',
    level: RoleLevel.C,
    domain: ClerkDomain.PLATFORM_OPERATORS,
    canImpersonate: false,
    requiresStepUpAuth: false,
    maxSessionMinutes: 480,
    description: 'General platform staff.',
  },
  MARKETING: {
    id: 'MARKETING',
    label: 'Marketing',
    level: RoleLevel.C,
    domain: ClerkDomain.PLATFORM_OPERATORS,
    canImpersonate: false,
    requiresStepUpAuth: false,
    maxSessionMinutes: 480,
    description: 'Marketing operations — no tenant data access.',
  },

  // ─── Level D: External (Clerk App 3) ────────────────────────
  OWNER: {
    id: 'OWNER',
    label: 'Tenant Owner',
    level: RoleLevel.D,
    domain: ClerkDomain.TENANTS,
    canImpersonate: false,
    requiresStepUpAuth: false,
    maxSessionMinutes: 480,
    description: 'Law firm owner. Full tenant-scoped access.',
  },
  BILLING_ADMIN: {
    id: 'BILLING_ADMIN',
    label: 'Tenant Billing Admin',
    level: RoleLevel.D,
    domain: ClerkDomain.TENANTS,
    canImpersonate: false,
    requiresStepUpAuth: false,
    maxSessionMinutes: 480,
    description: 'Manages tenant billing. Can upgrade/downgrade — no approval needed.',
  },
  ATTORNEY: {
    id: 'ATTORNEY',
    label: 'Attorney',
    level: RoleLevel.D,
    domain: ClerkDomain.TENANTS,
    canImpersonate: false,
    requiresStepUpAuth: false,
    maxSessionMinutes: 480,
    description: 'Attorney within tenant law firm.',
  },
  PARALEGAL: {
    id: 'PARALEGAL',
    label: 'Paralegal',
    level: RoleLevel.D,
    domain: ClerkDomain.TENANTS,
    canImpersonate: false,
    requiresStepUpAuth: false,
    maxSessionMinutes: 480,
    description: 'Paralegal within tenant law firm.',
  },
  CLIENT: {
    id: 'CLIENT',
    label: 'Client',
    level: RoleLevel.D,
    domain: ClerkDomain.TENANTS,
    canImpersonate: false,
    requiresStepUpAuth: false,
    maxSessionMinutes: 240,
    description: 'End client of a tenant law firm. Customer Portal access only.',
  },
} as const

// ─── Helper Functions ─────────────────────────────────────────────
export function getRoleById(roleId: string): RoleDefinition | undefined {
  return ROLE_REGISTRY[roleId]
}

export function getRolesByLevel(level: RoleLevel): RoleDefinition[] {
  return Object.values(ROLE_REGISTRY).filter(r => r.level === level)
}

export function getRolesByDomain(domain: ClerkDomain): RoleDefinition[] {
  return Object.values(ROLE_REGISTRY).filter(r => r.domain === domain)
}

export function isRoleHigherOrEqual(role: string, threshold: RoleLevel): boolean {
  const def = ROLE_REGISTRY[role]
  if (!def) return false
  const order: Record<RoleLevel, number> = { A: 4, B: 3, C: 2, D: 1 }
  return order[def.level] >= order[threshold]
}

export function canRoleImpersonate(roleId: string): boolean {
  return ROLE_REGISTRY[roleId]?.canImpersonate ?? false
}
