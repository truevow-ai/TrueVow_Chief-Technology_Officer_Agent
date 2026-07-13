---
source: Truevow_Tenant_Customer_Portal_Service/.opencode/skills/phase-2-confidence-score/SKILL.md
service: Truevow_Tenant_Customer_Portal_Service
type: customer-portal
stack: ["nextjs", "typescript", "playwright", "sentry"]
imported: 2026-06-30T22:32:05.025833+00:00
skill_name: phase-2-confidence-score
---
---
name: phase-2-confidence-score
description: Implement confidence score UI for SETTLE analysis and query pages. Use when adding confidence score display, factor breakdown, or data quality warnings to SETTLE pages.
---

# Phase 2.1: Confidence Score UI

## Overview

Add confidence score display to SETTLE analysis and query pages, showing factor-level breakdown and data quality warnings.

## Files to Modify

1. `lib/api/settle-client.ts` - Add types
2. `app/(dashboard)/dashboard/settle/analysis/page.tsx` - Add display
3. `app/(dashboard)/dashboard/settle/query/page.tsx` - Add display

## Type Definitions

Add to `lib/api/settle-client.ts`:

```typescript
export interface ConfidenceFactor {
  score: number;
  max: number;
  weight: number;
  detail: string;
}

export interface ConfidenceScoreData {
  overall: number;
  label: string;
  factors: {
    comp_set_depth: ConfidenceFactor;
    reputation_distribution: ConfidenceFactor;
    jurisdiction_coverage: ConfidenceFactor;
    injury_type_specificity: ConfidenceFactor;
    data_recency: ConfidenceFactor;
    outlier_rate: ConfidenceFactor;
    completeness: ConfidenceFactor;
  };
  warnings: string[];
}
```

## UI Structure

```
┌─────────────────────────────────────────────────┐
│ Data Confidence Score: 72/100 (Strong)          │
│ ┌─────────────────────────────────────────────┐ │
│ │ Factor          Score  Bar     Detail        │ │
│ │ Comp Set Depth   8/10  ████████  64 cases    │ │
│ │ Reputation      10/10  ██████████ High rep   │ │
│ │ Jurisdiction    10/10  ██████████ County     │ │
│ │ Injury Spec     10/10  ██████████ 100% match │ │
│ │ Data Recency     6/10  ██████    45 days ago │ │
│ │ Outlier Rate    10/10  ██████████ 3% outliers│ │
│ │ Completeness    10/10  ██████████ All filled │ │
│ └─────────────────────────────────────────────┘ │
│ ⚠ Data recency could be improved                │
└─────────────────────────────────────────────────┘
```

## Implementation Steps

1. Add types to `lib/api/settle-client.ts`
2. Create `ConfidenceScoreDisplay` component
3. Add to analysis page below estimate results
4. Add to query page below estimate results
5. Test with mock data

## Validation

- [ ] Types compile with 0 errors
- [ ] Score displays correctly
- [ ] Factor bars render proportionally
- [ ] Warnings show when present
- [ ] Works on both analysis and query pages
