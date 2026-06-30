# Cleanup Plan — TrueVow_Tenant_Application_Service

> Generated: 2026-05-29

## Phase 1: Organize Root

- 3 .bat files at repository root
  → Move to a subfolder (scripts/)

- 2 .ipynb files at repository root
  → Move to a subfolder (notebooks/)

- 10 .md files at repository root
  → Move to a subfolder (docs/)

## Phase 2: Consolidate Models

- Multiple models/ directories exist — choose one
  → C:\Users\yasha\OneDrive\Documents\TrueVow\Cursor\TrueVow_Tenant_Application_Service\models, C:\Users\yasha\OneDrive\Documents\TrueVow\Cursor\TrueVow_Tenant_Application_Service\app\models — one is likely stale or shadowing the other.

## Phase 3: Organize Tests

- 46 test files flat in tests/ — no subfolder organization
  → Group by domain: billing/, voice/, draft/, integration/, etc.

## Phase 4: Clean Migrations

- Both migrations/ and database/ exist — possible dual ORM setup
  → One ORM configuration is likely stale. Review and archive the unused one.

- Archive folder found: docs/archive/
  → Archive folders should be outside the repo or explicitly tagged for deletion review.

