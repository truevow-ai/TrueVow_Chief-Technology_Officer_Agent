---
category: architecture
title: "Platform Analytics Service - 5-Layer Event Architecture"
importance: 8
tags: ["analytics", "events", "warehouse", "dashboards", "star-schema", "platform"]
file_paths: []
created: 2026-06-25T02:09:41.937754+00:00
updated: 2026-06-25T02:09:41.937754+00:00
memory_id: b3933a17-717b-4a55-99ea-d1e00c2ab766
---

# Platform Analytics Service - 5-Layer Event Architecture

5-layer SaaS analytics following Stripe/Shopify/HubSpot pattern. Layer 2: Event Stream (ingestion from all platform services). Layer 3: Raw Event Store (append-only, retention policies). Layer 4: Dimensional Warehouse (star schema, SCD Type 2). Layer 5: Aggregations (pre-computed daily/monthly). Layer 6: Analytics APIs (REST endpoints, 12 dashboards). Stack: Python/FastAPI, port 3071. Depends on: ALL services (ingests events from all). Key insight: centralized analytics for entire TrueVow platform.

---
**Category:** `architecture` | **Importance:** 8/10
**Files:** N/A
