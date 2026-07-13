---
category: architecture
title: "SaaS Administration Service - Central Hub"
importance: 9
tags: ["saas-admin", "hub", "central", "tenant-management", "auth", "database", "architecture"]
file_paths: []
created: 2026-06-25T02:09:39.620236+00:00
updated: 2026-06-25T02:09:39.620236+00:00
memory_id: 501f9d40-7586-424b-932c-7b9b766c69c4
---

# SaaS Administration Service - Central Hub

Centralized admin dashboard and tenant management. Stack: Python (FastAPI likely), centralized database TrueVow-Saas-Admin. Manages: core_tenants, pricing_subscriptions (was subscription_tenants), pricing_tiers (was subscription_plans), system_notifications (was notifications). BREAKING CHANGE Jan 2026: standardized table names. Acts as authentication gateway for all spoke services. Manages global DRAFT rule templates. Port: admin dashboard. Dependencies: ALL services depend on SaaS Admin for auth and tenant context.

---
**Category:** `architecture` | **Importance:** 9/10
**Files:** N/A
