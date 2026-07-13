# Cleanup Plan — TrueVow_Tenant_SETTLE-Service

> Generated: 2026-05-29

## Phase 1: Clean Migrations

- Both migrations/ and database/ exist — possible dual ORM setup
  → One ORM configuration is likely stale. Review and archive the unused one.

- Archive folder found: docs/archive/
  → Archive folders should be outside the repo or explicitly tagged for deletion review.

