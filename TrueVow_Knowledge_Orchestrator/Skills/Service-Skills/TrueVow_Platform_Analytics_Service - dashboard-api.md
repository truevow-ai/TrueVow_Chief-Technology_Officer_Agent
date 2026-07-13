---
source: TrueVow_Platform_Analytics_Service/.opencode/skills/dashboard-api/SKILL.md
service: TrueVow_Platform_Analytics_Service
type: analytics
stack: ["python", "fastapi"]
imported: 2026-06-30T22:32:05.183683+00:00
skill_name: dashboard-api
---
---
name: dashboard-api
description: Dashboard statistics endpoints for all 12 analytics dashboards.
---

# Dashboard API

## Overview
This skill covers the dashboard statistics endpoints that power all 12 analytics dashboards.

## When to Use
- Adding new dashboard endpoints
- Modifying existing dashboard metrics
- Debugging dashboard data issues
- Implementing new aggregation queries

## Implementation Steps
1. Identify which dashboard the endpoint supports (1-12)
2. Add response model in `app/api/v1/endpoints/dashboards/executive.py`
3. Create endpoint with proper query parameters
4. Implement aggregation query using fact/dimension tables
5. Test endpoint returns correct response shape
6. Update documentation

## Validation Checklist
- [ ] Response model has proper type annotations
- [ ] Endpoint has proper docstrings
- [ ] Query uses correct fact/dimension tables
- [ ] Handles empty data gracefully (returns zeros)
- [ ] Period parameters are validated
- [ ] Response matches expected shape

## Files to Modify
- `app/api/v1/endpoints/dashboards/executive.py` — All dashboard endpoints
- `app/aggregations/models/` — Aggregation model imports
- `app/warehouse/facts/` — Fact table imports
- `app/warehouse/dimensions/` — Dimension table imports

## Dashboard Endpoints
1. Executive: GET /api/v1/analytics/platform/overview
2. Revenue: GET /api/v1/analytics/revenue/mrr
3. Customer Lifecycle: GET /api/v1/analytics/customer/lifecycle
4. Intake Funnel: GET /api/v1/analytics/intake/funnel
5. Lead Funnel: GET /api/v1/analytics/intake/funnel (same as 4)
6. Settlement: GET /api/v1/analytics/settlement/intelligence
7. Compliance: GET /api/v1/analytics/compliance/intelligence
8. Product Usage: GET /api/v1/analytics/product/usage
9. Customer Success: GET /api/v1/analytics/customer-success/overview
10. Platform Operations: GET /api/v1/analytics/platform/operations
11. Marketing Funnel: GET /api/v1/analytics/marketing/funnel
12. Internal Operations: GET /api/v1/analytics/internal/operations
