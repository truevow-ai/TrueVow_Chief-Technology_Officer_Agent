---
category: context
title: "Sentry SDK Implemented \u2014 Tenant Application Service"
importance: 8
tags: ["sentry", "monitoring", "error-tracking", "installed", "intake", "progress"]
file_paths: []
created: 2026-06-25T02:52:30.391821+00:00
updated: 2026-06-25T02:52:30.391821+00:00
memory_id: b884fb59-77c3-4c00-a41d-e26b0b8289d0
---

# Sentry SDK Implemented — Tenant Application Service

Sentry SDK installed in Tenant Application Service (INTAKE). Files created: app/shared/sentry_init.py (FastAPI integration with Starlette, SQLAlchemy, transaction tracing), .env.local updated with SENTRY_DSN placeholder. Next steps: Set actual DSN in .env.local, add 'from app.shared.sentry_init import init_sentry; init_sentry(app)' to main.py. Shared library available at shared-libraries/sentry/ for all Python services. Next.js configs at shared-libraries/sentry/nextjs/ for Portal, Sales Ops, CS CORE. Remaining: install into FM, Analytics, SaaS Admin, Billing, and all Next.js frontends.

---
**Category:** `context` | **Importance:** 8/10
**Files:** N/A
