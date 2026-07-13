---
source: Truevow_Tenant_Customer_Portal_Service/.opencode/skills/phase-2-advanced-filters/SKILL.md
service: Truevow_Tenant_Customer_Portal_Service
type: customer-portal
stack: ["nextjs", "typescript", "playwright", "sentry"]
imported: 2026-06-30T22:32:04.899165+00:00
skill_name: phase-2-advanced-filters
---
---
name: phase-2-advanced-filters
description: Implement advanced filter controls on SETTLE query page. Use when adding filter inputs, outcome type dropdown, date range pickers, medical bills range, reputation slider, or comparative negligence filters.
---

# Phase 2.2: Advanced Filter Controls

## Overview

Add 9 new optional filter fields to the SETTLE query page for more precise settlement range queries.

## Files to Modify

1. `lib/api/settle-client.ts` - Add fields to EstimateRequest type
2. `app/(dashboard)/dashboard/settle/query/page.tsx` - Add filter controls UI

## New Filter Fields

| Field | UI Control | Type |
|-------|-----------|------|
| outcome_type | Dropdown | Settlement, Jury Verdict, Arbitration Award, Mediation, Judge's Decision |
| date_range_from | Date picker | Date |
| date_range_to | Date picker | Date |
| medical_bills_min | Number input | Float |
| medical_bills_max | Number input | Float |
| exclude_outliers | Toggle checkbox | Boolean (default: true) |
| min_reputation_score | Slider 0-1 | Float |
| comparative_negligence_min | Number input 0-100 | Float |
| comparative_negligence_max | Number input 0-100 | Float |

## Type Updates

Add to `EstimateRequest` in `lib/api/settle-client.ts`:

```typescript
export interface EstimateRequest {
  // ... existing fields
  outcome_type?: string;
  date_range_from?: string;
  date_range_to?: string;
  medical_bills_min?: number;
  medical_bills_max?: number;
  exclude_outliers?: boolean;
  min_reputation_score?: number;
  comparative_negligence_min?: number;
  comparative_negligence_max?: number;
}
```

## UI Structure

```
┌─────────────────────────────────────────────────┐
│ Advanced Filters ▼                              │
│ ┌─────────────────────────────────────────────┐ │
│ │ Outcome Type:    [Settlement        ▼]      │ │
│ │ Date Range:      [2024-01-01] to [2026-05-19]│
│ │ Medical Bills:   $[     ] to $[     ]       │ │
│ │ Comp. Negligence: [  ]% to [  ]%            │ │
│ │ Min Reputation:  [████████░░] 0.8           │ │
│ │ ☑ Exclude Outliers                           │ │
│ │ [Apply Filters] [Clear]                      │ │
│ └─────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────┘
```

## Implementation Steps

1. Update EstimateRequest type
2. Add state for all filter fields
3. Create collapsible Advanced Filters section
4. Add Apply Filters and Clear buttons
5. Pass filters to estimate API call
6. Test with mock data

## Validation

- [ ] All 9 filters render correctly
- [ ] Filters pass through to backend
- [ ] Apply Filters triggers new query
- [ ] Clear resets all filters to defaults
- [ ] Types compile with 0 errors
