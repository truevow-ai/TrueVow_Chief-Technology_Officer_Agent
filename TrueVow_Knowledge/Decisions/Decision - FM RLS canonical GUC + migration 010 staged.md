---
category: decision
title: "FM RLS canonical GUC + migration 010 staged"
importance: 8
tags: []
file_paths: []
created: 2026-06-25T20:49:41.178490+00:00
updated: 2026-06-25T20:49:41.178490+00:00
memory_id: 1eae6b2d-6290-430c-89b5-9985d68133f2
---

# FM RLS canonical GUC + migration 010 staged

Canonical RLS GUC for FM is app.current_tenant_id (set by app/core/database.py get_db_session). Migration 008 + compliance/001_rls_policies.sql wrongly use app.current_legal_entity_id (app never sets it). Staged migration 010_missing_tables_and_rls_fix creates approval_policy, reconciliation_adjustment_batch, treasury_sync_batch (had ORM models but no DDL anywhere) + tenant RLS, and fixes 008 treasury_bank_* RLS. Verified offline (py_compile + alembic history single head 009->010). NOT applied; DB down until 2026-06-26. Also fixed MockBillingAdapter NameError in ar billing_sync_routes.

---
**Category:** `decision` | **Importance:** 8/10
**Files:** N/A
