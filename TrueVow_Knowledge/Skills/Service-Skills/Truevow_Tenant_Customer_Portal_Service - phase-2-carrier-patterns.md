---
source: Truevow_Tenant_Customer_Portal_Service/.opencode/skills/phase-2-carrier-patterns/SKILL.md
service: Truevow_Tenant_Customer_Portal_Service
type: customer-portal
stack: ["nextjs", "typescript", "playwright", "sentry"]
imported: 2026-06-30T22:32:04.958415+00:00
skill_name: phase-2-carrier-patterns
---
---
name: phase-2-carrier-patterns
description: Implement carrier patterns analytics page for SETTLE. Use when creating defendant category settlement patterns page, carrier analytics table, or settlement rate analysis by defendant type.
---

# Phase 2.3: Carrier Patterns Analytics

## Overview

Create a new analytics page at `/dashboard/settle/carrier-patterns` that displays defendant category settlement patterns from anonymized settlement contributions.

## Files

1. **New page**: `app/(dashboard)/dashboard/settle/carrier-patterns/page.tsx`
2. **API client update**: `lib/api/settle-client.ts` — add CarrierPattern, CarrierPatternsResponse types and `getCarrierPatterns()` method
3. **API proxy route**: `app/api/settle/carrier-patterns/route.ts` — forwards to SETTLE backend
4. **Sidebar update**: `app/(dashboard)/layout.tsx` — add navigation link

## Type Definitions

```typescript
export interface CarrierPattern {
  defendant_category: string;
  defendant_industry: string | null;
  case_count: number;
  avg_settlement_range: { low: number; median: number; high: number };
  settlement_rate: number;
  avg_time_to_resolution_days: number | null;
  trial_rate: number;
  lowball_indicator: number;
  median_settlement: number | null;
  p25_settlement: number | null;
  p75_settlement: number | null;
}

export interface CarrierPatternsResponse {
  patterns: CarrierPattern[];
  total_cases: number;
  jurisdiction: string | null;
  case_type: string | null;
  methodology: string;
}
```

## API Client Method

```typescript
async getCarrierPatterns(params?: {
  jurisdiction?: string;
  case_type?: string;
  injury_category?: string[];
  defendant_category?: string;
  min_case_count?: number;
}): Promise<CarrierPatternsResponse>
```

## API Proxy Route

`GET /api/settle/carrier-patterns` → `GET {SETTLE_BACKEND_URL}/api/v1/analytics/carrier-patterns`

## UI Structure

```
┌─────────────────────────────────────────────────────────────────┐
│ Defendant Category Settlement Patterns                          │
│ Historical data from anonymized settlement contributions.       │
│ Not predictive.                                                 │
│                                                                 │
│ Filters: [Jurisdiction ▼] [Case Type ▼] [Injury Category ▼]    │
│                                                                 │
│ ┌──────────┬──────┬─────────┬────────────┬─────────────┬───────┐│
│ │ Category │ Cases│ Median  │ Settle Rate│ Below Median │ Trial ││
│ ├──────────┼──────┼─────────┼────────────┼─────────────┼───────┤│
│ │ Business │  342 │ $89,000 │    78%     │     23%     │  12%  ││
│ │ (Health) │      │         │            │             │       ││
│ └──────────┴──────┴─────────┴────────────┴─────────────┴───────┘│
│                                                                 │
│ 1,247 total cases analyzed                                      │
└─────────────────────────────────────────────────────────────────┘
```

## Implementation Steps

1. Add types to `lib/api/settle-client.ts`
2. Add `getCarrierPatterns()` method to SettleClient class
3. Create API proxy route at `app/api/settle/carrier-patterns/route.ts`
4. Create page at `app/(dashboard)/dashboard/settle/carrier-patterns/page.tsx`
5. Add sidebar navigation link in `app/(dashboard)/layout.tsx`

## Validation

- [ ] Page loads at /dashboard/settle/carrier-patterns
- [ ] Table displays all columns correctly
- [ ] Filters work (jurisdiction, case type, injury category)
- [ ] Loading state shows while fetching
- [ ] Empty state shows when no patterns available
- [ ] Methodology disclaimer displays
- [ ] Currency formatting correct
- [ ] Percentage formatting correct
- [ ] Sidebar includes Carrier Patterns link
