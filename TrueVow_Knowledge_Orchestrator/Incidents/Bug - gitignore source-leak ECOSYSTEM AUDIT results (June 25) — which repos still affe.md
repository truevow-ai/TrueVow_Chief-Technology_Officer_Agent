---
category: bug
title: "gitignore source-leak ECOSYSTEM AUDIT results (June 25) \u2014 which repos still affected"
importance: 8
tags: ["gitignore", "audit", "ecosystem", "cross-service"]
file_paths: []
created: 2026-06-25T03:49:16.759705+00:00
updated: 2026-06-25T03:49:16.759705+00:00
memory_id: 8daa9fa8-6631-4ae5-8113-94668f36b102
---

# gitignore source-leak ECOSYSTEM AUDIT results (June 25) — which repos still affected

Audited all sibling git repos for the gitignore source-leak (advisory 64bc43bf). NONE have run the fix yet (advisory just issued). CONFIRMED UNFIXED SOURCE LEAKS (real lib/ source hidden from git): TrueVow_Financial_Management_Service (frontend/lib + frontend/__tests__/lib), TrueVow_Tenant_Application_Service (app/portal/lib, dograh server ui/src/lib, scripts/lib), TrueVow-Tenant_Billing-Service (ui/lib; ALSO its .gitignore has an embedded NULL/control byte — corrupted). LATENT (dangerous unanchored lib/ rule present but no active source leak yet): TrueVow_Internal_Ops_Service, TrueVow_Tenant_SETTLE-Service, TrueVow_Tenant_LEVERAGE_Service. NOT GIT REPOS AT ALL (no version control — separate severe issue): TrueVow_Dialogflow_Intake_Service, TrueVow_Platform_Analytics_Service, TrueVow_Tenant_VERIFY_Service, TrueVow_TWIML_SoftPhone_App. CLEAN: Website, Customer_Success_CORE, First_Line_Support, Sales_Ops, Tenant_CONNECT, Customer_Portal, cartesia_test. SaaS_Admin already fixed. Each affected repo agent: run docs/01-main/ECOSYSTEM_ADVISORY_GITIGNORE_SOURCE_LEAK.md (in SaaS Admin).

---
**Category:** `bug` | **Importance:** 8/10
**Files:** N/A
