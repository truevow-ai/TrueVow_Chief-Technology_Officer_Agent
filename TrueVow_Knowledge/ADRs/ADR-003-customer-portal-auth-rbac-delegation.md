# ADR-003: Customer Portal Auth+RBAC Delegation to Shared Libraries

**Status:** Accepted  
**Date:** 2026-07-01  
**Deciders:** Yasha (CTO)

## Context

The Customer Portal had a 272-line local `lib/auth/guard.ts` file that mirrored `@truevow/rbac-engine` and `@truevow/auth-client` but with simplified, divergent logic. It maintained its own copies of `RoleLevel`, `Permission`, `ROLE_REGISTRY`, and `PERMISSION_RULES` that were inconsistent with the canonical definitions in the shared libraries. The local guard used simple single-level threshold checks while the shared rbac-engine has a rich permission matrix with domain restrictions and approval chains.

Additionally, the Customer Portal did not import either shared library, meaning domain enforcement, cross-domain token exchange, and impersonation tracking were unavailable.

## Decision

`lib/auth/guard.ts` is rewritten to delegate all RBAC logic to `@truevow/rbac-engine` and `@truevow/auth-client`. The local enums and constants are replaced with imports from the shared libraries. The API surface (`withAuth`, `withPermission`, `withLevel`, `withTenantScope`) is preserved for backward compatibility with existing route handlers.

Shared libraries are added as `file:` dependencies in `package.json`. The rewritten guard now supports domain-aware permission checks, cross-domain impersonation, and approval chain awareness.

## Consequences

- **Positive:** Single source of truth for role hierarchy, permissions, and domain configuration.
- **Positive:** Backward compatible — no API route changes needed.
- **Positive:** Domain enforcement, impersonation tracking, and approval chains now available.
- **Risk:** Env var naming mismatch (`CLERK_APP_1_*` vs `CLERK_APP1_*`) between local `.env.local` and shared `domain-config.ts`. Needs alignment when the shared auth-client is used for domain config.
- **Risk:** `pnpm install` must be run to resolve the `file:` dependencies before the guard works at runtime.

## Affected Services

- `Truevow_Tenant_Customer_Portal_Service`
- `shared-libraries/auth-client`
- `shared-libraries/rbac-engine`
