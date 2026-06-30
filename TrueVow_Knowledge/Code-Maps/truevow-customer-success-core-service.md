# Code Structure Map — Customer Success CORE Service

> Auto-generated: 2026-05-29
> Repository: `TrueVow_Customer_Success_CORE_Service`

## File Breakdown

| Extension | Count |
|-----------|-------|
| .md | 200 |
| .ts | 194 |
| .tsx | 46 |
| .ps1 | 13 |
| .py | 10 |
| .js | 9 |
| .txt | 6 |
| (none) | 4 |
| .json | 3 |
| .css | 1 |
| .sql | 1 |
| .local | 1 |
| .code-workspace | 1 |
| .tsbuildinfo | 1 |

## Directory Tree

```
```

## Component Graph

```mermaid
graph TD
```

## Issues Found (51)

### MEDIUM

- **7 .md files at repository root**
  > Move to a subfolder (docs/)
  > _C:\Users\yasha\OneDrive\Documents\TrueVow\Cursor\TrueVow_Customer_Success_CORE_Service_

- **"page.tsx" appears in 10 locations**
  > Found at: ..\..\TrueVow_Customer_Success_CORE_Service\app\(auth)\sign-in\[[...sign-in]]\page.tsx, ..\..\TrueVow_Customer_Success_CORE_Service\app\(dashboard)\analytics\page.tsx, ..\..\TrueVow_Customer_Success_CORE_Service\app\(dashboard)\dashboard\page.tsx...
  > _..\..\TrueVow_Customer_Success_CORE_Service\app\(auth)\sign-in\[[...sign-in]]\page.tsx_

- **"layout.tsx" appears in 2 locations**
  > Found at: ..\..\TrueVow_Customer_Success_CORE_Service\app\(dashboard)\layout.tsx, ..\..\TrueVow_Customer_Success_CORE_Service\app\layout.tsx
  > _..\..\TrueVow_Customer_Success_CORE_Service\app\(dashboard)\layout.tsx_

- **"route.ts" appears in 85 locations**
  > Found at: ..\..\TrueVow_Customer_Success_CORE_Service\app\api\intelligence\health\calculate\route.ts, ..\..\TrueVow_Customer_Success_CORE_Service\app\api\intelligence\health\route.ts, ..\..\TrueVow_Customer_Success_CORE_Service\app\api\intelligence\metrics\route.ts...
  > _..\..\TrueVow_Customer_Success_CORE_Service\app\api\intelligence\health\calculate\route.ts_

- **"index.ts" appears in 3 locations**
  > Found at: ..\..\TrueVow_Customer_Success_CORE_Service\components\shared\index.ts, ..\..\TrueVow_Customer_Success_CORE_Service\libs\core\repositories\index.ts, ..\..\TrueVow_Customer_Success_CORE_Service\libs\core\security\index.ts
  > _..\..\TrueVow_Customer_Success_CORE_Service\components\shared\index.ts_

- **"README.md" appears in 3 locations**
  > Found at: ..\..\TrueVow_Customer_Success_CORE_Service\docs\01-main\SAAS_ADMIN_IMPLEMENTATION\README.md, ..\..\TrueVow_Customer_Success_CORE_Service\docs\word\README.md, ..\..\TrueVow_Customer_Success_CORE_Service\README.md
  > _..\..\TrueVow_Customer_Success_CORE_Service\docs\01-main\SAAS_ADMIN_IMPLEMENTATION\README.md_

- **"AUTOMATED_TEST_REPORT.md" appears in 2 locations**
  > Found at: ..\..\TrueVow_Customer_Success_CORE_Service\docs\AUTOMATED_TEST_REPORT.md, ..\..\TrueVow_Customer_Success_CORE_Service\AUTOMATED_TEST_REPORT.md
  > _..\..\TrueVow_Customer_Success_CORE_Service\docs\AUTOMATED_TEST_REPORT.md_

- **"client.ts" appears in 2 locations**
  > Found at: ..\..\TrueVow_Customer_Success_CORE_Service\lib\intelligence\client.ts, ..\..\TrueVow_Customer_Success_CORE_Service\libs\core\intelligence\client.ts
  > _..\..\TrueVow_Customer_Success_CORE_Service\lib\intelligence\client.ts_

- **"api-key.ts" appears in 2 locations**
  > Found at: ..\..\TrueVow_Customer_Success_CORE_Service\libs\core\auth\api-key.ts, ..\..\TrueVow_Customer_Success_CORE_Service\libs\core\middleware\api-key.ts
  > _..\..\TrueVow_Customer_Success_CORE_Service\libs\core\auth\api-key.ts_

- **"post-onboarding-flows.ts" appears in 2 locations**
  > Found at: ..\..\TrueVow_Customer_Success_CORE_Service\libs\core\services\post-onboarding-flows.ts, ..\..\TrueVow_Customer_Success_CORE_Service\scripts\scheduled-jobs\post-onboarding-flows.ts
  > _..\..\TrueVow_Customer_Success_CORE_Service\libs\core\services\post-onboarding-flows.ts_

### LOW

- **Deep nesting (depth 6): ..\..\TrueVow_Customer_Success_CORE_Service\app\api\intelligence\recommendations\[id]\acted**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Customer_Success_CORE_Service\app\api\intelligence\recommendations\[id]\acted_

- **Deep nesting (depth 6): ..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\analytics\agent\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\analytics\agent\[id]_

- **Deep nesting (depth 7): ..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\analytics\agent\[id]\comparison**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\analytics\agent\[id]\comparison_

- **Deep nesting (depth 6): ..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\analytics\trends\analyze**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\analytics\trends\analyze_

- **Deep nesting (depth 6): ..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\analytics\trends\feedback**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\analytics\trends\feedback_

- **Deep nesting (depth 6): ..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\analytics\trends\pain-points**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\analytics\trends\pain-points_

- **Deep nesting (depth 6): ..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\analytics\trends\summary**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\analytics\trends\summary_

- **Deep nesting (depth 6): ..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\analytics\usage\churn-risk**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\analytics\usage\churn-risk_

- **Deep nesting (depth 6): ..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\analytics\usage\event**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\analytics\usage\event_

- **Deep nesting (depth 6): ..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\analytics\usage\feature-adoption**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\analytics\usage\feature-adoption_

- **Deep nesting (depth 6): ..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\analytics\usage\summary**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\analytics\usage\summary_

- **Deep nesting (depth 6): ..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\expansion\triggers\evaluate**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\expansion\triggers\evaluate_

- **Deep nesting (depth 6): ..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\integrations\internal-ops\revops**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\integrations\internal-ops\revops_

- **Deep nesting (depth 7): ..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\integrations\internal-ops\revops\activities**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\integrations\internal-ops\revops\activities_

- **Deep nesting (depth 6): ..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\integrations\internal-ops\tasks**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\integrations\internal-ops\tasks_

- **Deep nesting (depth 6): ..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\integrations\internal-ops\time-tracking**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\integrations\internal-ops\time-tracking_

- **Deep nesting (depth 6): ..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\kb\articles\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\kb\articles\[id]_

- **Deep nesting (depth 7): ..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\kb\articles\[id]\helpful**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\kb\articles\[id]\helpful_

- **Deep nesting (depth 6): ..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\onboarding\law-firm\internal-status**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\onboarding\law-firm\internal-status_

- **Deep nesting (depth 6): ..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\onboarding\law-firm\progress**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\onboarding\law-firm\progress_

- **Deep nesting (depth 6): ..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\onboarding\law-firm\step-1**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\onboarding\law-firm\step-1_

- **Deep nesting (depth 6): ..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\onboarding\law-firm\step-2**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\onboarding\law-firm\step-2_

- **Deep nesting (depth 6): ..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\onboarding\law-firm\step-3**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\onboarding\law-firm\step-3_

- **Deep nesting (depth 6): ..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\onboarding\law-firm\step-4**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\onboarding\law-firm\step-4_

- **Deep nesting (depth 6): ..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\onboarding\law-firm\step-5**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\onboarding\law-firm\step-5_

- **Deep nesting (depth 6): ..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\onboarding\milestone\complete**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\onboarding\milestone\complete_

- **Deep nesting (depth 6): ..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\onboarding\sequences\template**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\onboarding\sequences\template_

- **Deep nesting (depth 7): ..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\onboarding\sequences\template\[templateKey]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\onboarding\sequences\template\[templateKey]_

- **Deep nesting (depth 6): ..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\onboarding\sequences\templates**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\onboarding\sequences\templates_

- **Deep nesting (depth 6): ..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\playbooks\[id]\execute**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\playbooks\[id]\execute_

- **Deep nesting (depth 6): ..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\playbooks\[id]\stats**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\playbooks\[id]\stats_

- **Deep nesting (depth 6): ..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\playbooks\executions\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\playbooks\executions\[id]_

- **Deep nesting (depth 7): ..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\playbooks\executions\[id]\outcome**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\playbooks\executions\[id]\outcome_

- **Deep nesting (depth 6): ..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\renewal\campaign\start**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\renewal\campaign\start_

- **Deep nesting (depth 6): ..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\renewal\campaign\step**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\renewal\campaign\step_

- **Deep nesting (depth 6): ..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\renewal\risk\calculate**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\renewal\risk\calculate_

- **Deep nesting (depth 6): ..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\tickets\[id]\activity**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\tickets\[id]\activity_

- **Deep nesting (depth 6): ..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\tickets\[id]\notes**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\tickets\[id]\notes_

- **Deep nesting (depth 6): ..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\webhooks\platform\milestone**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\webhooks\platform\milestone_

- **Deep nesting (depth 6): ..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\workflows\[id]\execute**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\workflows\[id]\execute_

- **Deep nesting (depth 6): ..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\workflows\[id]\executions**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Customer_Success_CORE_Service\app\api\v1\workflows\[id]\executions_



## Related Service
- [[Cross-Service/truevow-customer-success-core-service|Service Page]]
