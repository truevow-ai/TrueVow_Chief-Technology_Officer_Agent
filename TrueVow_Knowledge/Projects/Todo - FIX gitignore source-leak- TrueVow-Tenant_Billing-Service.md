---
category: todo
title: "FIX gitignore source-leak: TrueVow-Tenant_Billing-Service"
importance: 8
tags: ["gitignore", "todo", "assigned"]
file_paths: []
created: 2026-06-25T04:04:47.977447+00:00
updated: 2026-06-25T04:04:47.977447+00:00
memory_id: 291ef12a-922c-4bf1-b8d8-e61ce5050558
---

# FIX gitignore source-leak: TrueVow-Tenant_Billing-Service

ASSIGNED to the TrueVow-Tenant_Billing-Service agent. Real lib/ source is currently hidden from git (confirmed). Run the playbook: TrueVow_SaaS_Administration_Service/docs/01-main/ECOSYSTEM_ADVISORY_GITIGNORE_SOURCE_LEAK.md (fix .gitignore: anchor/remove stray lib/ + logs/; secrets-scan; commit recovered source in reviewed batches by explicit path; verify clean-clone build). REPORT RESULT via memory.py remember category=bug title='TrueVow-Tenant_Billing-Service gitignore RESULT' content='FIXED n files | CLEAN | BLOCKED + reason; secrets found?'. NOTE: reporting.py agent-checkin is broken — report via memory.

---
**Category:** `todo` | **Importance:** 8/10
**Files:** N/A
