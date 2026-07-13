# Code Structure Map — Tenant Customer Portal Service

> Auto-generated: 2026-05-29
> Repository: `Truevow_Tenant_Customer_Portal_Service`

## File Breakdown

| Extension | Count |
|-----------|-------|
| .ts | 90 |
| .tsx | 74 |
| .md | 33 |
| .json | 7 |
| .mjs | 4 |
| .css | 3 |
| .ps1 | 3 |
| .txt | 3 |
| .webm | 2 |
| .py | 2 |
| .js | 2 |
| .sql | 1 |
| .html | 1 |
| .xml | 1 |
| .local | 1 |
| .tsbuildinfo | 1 |

## Directory Tree

```
```

## Component Graph

```mermaid
graph TD
```

## Issues Found (32)

### MEDIUM

- **24 .md files at repository root**
  > Move to a subfolder (docs/)
  > _C:\Users\yasha\OneDrive\Documents\TrueVow\Cursor\Truevow_Tenant_Customer_Portal_Service_

- **"page.tsx" appears in 52 locations**
  > Found at: ..\..\Truevow_Tenant_Customer_Portal_Service\app\(auth)\sign-in\[[...sign-in]]\page.tsx, ..\..\Truevow_Tenant_Customer_Portal_Service\app\(auth)\sign-up\[[...sign-up]]\page.tsx, ..\..\Truevow_Tenant_Customer_Portal_Service\app\(dashboard)\dashboard\billing\invoices\page.tsx...
  > _..\..\Truevow_Tenant_Customer_Portal_Service\app\(auth)\sign-in\[[...sign-in]]\page.tsx_

- **"layout.tsx" appears in 3 locations**
  > Found at: ..\..\Truevow_Tenant_Customer_Portal_Service\app\(dashboard)\layout.tsx, ..\..\Truevow_Tenant_Customer_Portal_Service\app\draft-testing\layout.tsx, ..\..\Truevow_Tenant_Customer_Portal_Service\app\layout.tsx
  > _..\..\Truevow_Tenant_Customer_Portal_Service\app\(dashboard)\layout.tsx_

- **"route.ts" appears in 55 locations**
  > Found at: ..\..\Truevow_Tenant_Customer_Portal_Service\app\api\analytics\track\route.ts, ..\..\Truevow_Tenant_Customer_Portal_Service\app\api\billing\addons\route.ts, ..\..\Truevow_Tenant_Customer_Portal_Service\app\api\billing\dashboard\route.ts...
  > _..\..\Truevow_Tenant_Customer_Portal_Service\app\api\analytics\track\route.ts_

- **"globals.css" appears in 2 locations**
  > Found at: ..\..\Truevow_Tenant_Customer_Portal_Service\app\globals.css, ..\..\Truevow_Tenant_Customer_Portal_Service\styles\globals.css
  > _..\..\Truevow_Tenant_Customer_Portal_Service\app\globals.css_

- **"Breadcrumb.tsx" appears in 2 locations**
  > Found at: ..\..\Truevow_Tenant_Customer_Portal_Service\components\ui\Breadcrumb.tsx, ..\..\Truevow_Tenant_Customer_Portal_Service\lib\components\settle\Breadcrumb.tsx
  > _..\..\Truevow_Tenant_Customer_Portal_Service\components\ui\Breadcrumb.tsx_

- **"ToastProvider.tsx" appears in 2 locations**
  > Found at: ..\..\Truevow_Tenant_Customer_Portal_Service\components\ui\ToastProvider.tsx, ..\..\Truevow_Tenant_Customer_Portal_Service\lib\components\settle\ToastProvider.tsx
  > _..\..\Truevow_Tenant_Customer_Portal_Service\components\ui\ToastProvider.tsx_

- **"video.webm" appears in 2 locations**
  > Found at: ..\..\Truevow_Tenant_Customer_Portal_Service\test-results\phase-2-features-Phase-2-3-c9cf5-atterns-table-displays-data-chromium\video.webm, ..\..\Truevow_Tenant_Customer_Portal_Service\test-results\phase-2-features-Phase-2-3-ce551-erns-page-loads-with-header-chromium\video.webm
  > _..\..\Truevow_Tenant_Customer_Portal_Service\test-results\phase-2-features-Phase-2-3-c9cf5-atterns-table-displays-data-chromium\video.webm_

- **"playwright.config.ts" appears in 2 locations**
  > Found at: ..\..\Truevow_Tenant_Customer_Portal_Service\tests\e2e\playwright.config.ts, ..\..\Truevow_Tenant_Customer_Portal_Service\playwright.config.ts
  > _..\..\Truevow_Tenant_Customer_Portal_Service\tests\e2e\playwright.config.ts_

### LOW

- **Deep nesting (depth 6): ..\..\Truevow_Tenant_Customer_Portal_Service\app\(dashboard)\dashboard\billing\subscribe\[service]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\Truevow_Tenant_Customer_Portal_Service\app\(dashboard)\dashboard\billing\subscribe\[service]_

- **Deep nesting (depth 6): ..\..\Truevow_Tenant_Customer_Portal_Service\app\(dashboard)\dashboard\connect\referrals\new**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\Truevow_Tenant_Customer_Portal_Service\app\(dashboard)\dashboard\connect\referrals\new_

- **Deep nesting (depth 6): ..\..\Truevow_Tenant_Customer_Portal_Service\app\(dashboard)\dashboard\intake\lead\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\Truevow_Tenant_Customer_Portal_Service\app\(dashboard)\dashboard\intake\lead\[id]_

- **Deep nesting (depth 6): ..\..\Truevow_Tenant_Customer_Portal_Service\app\(dashboard)\dashboard\leverage\cases\[caseId]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\Truevow_Tenant_Customer_Portal_Service\app\(dashboard)\dashboard\leverage\cases\[caseId]_

- **Deep nesting (depth 6): ..\..\Truevow_Tenant_Customer_Portal_Service\app\(dashboard)\dashboard\leverage\cases\new**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\Truevow_Tenant_Customer_Portal_Service\app\(dashboard)\dashboard\leverage\cases\new_

- **Deep nesting (depth 6): ..\..\Truevow_Tenant_Customer_Portal_Service\app\(dashboard)\dashboard\team\edit\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\Truevow_Tenant_Customer_Portal_Service\app\(dashboard)\dashboard\team\edit\[id]_

- **Deep nesting (depth 6): ..\..\Truevow_Tenant_Customer_Portal_Service\app\api\cs-support\tickets\[id]\messages**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\Truevow_Tenant_Customer_Portal_Service\app\api\cs-support\tickets\[id]\messages_

- **Deep nesting (depth 6): ..\..\Truevow_Tenant_Customer_Portal_Service\app\api\cs-support\tickets\[id]\reply**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\Truevow_Tenant_Customer_Portal_Service\app\api\cs-support\tickets\[id]\reply_

- **Deep nesting (depth 6): ..\..\Truevow_Tenant_Customer_Portal_Service\app\api\intake\leads\[id]\call**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\Truevow_Tenant_Customer_Portal_Service\app\api\intake\leads\[id]\call_

- **Deep nesting (depth 6): ..\..\Truevow_Tenant_Customer_Portal_Service\app\api\intake\leads\[id]\notes**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\Truevow_Tenant_Customer_Portal_Service\app\api\intake\leads\[id]\notes_

- **Deep nesting (depth 6): ..\..\Truevow_Tenant_Customer_Portal_Service\app\api\intake\leads\[id]\reminders**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\Truevow_Tenant_Customer_Portal_Service\app\api\intake\leads\[id]\reminders_

- **Deep nesting (depth 6): ..\..\Truevow_Tenant_Customer_Portal_Service\app\api\intake\leads\[id]\sms**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\Truevow_Tenant_Customer_Portal_Service\app\api\intake\leads\[id]\sms_

- **Deep nesting (depth 6): ..\..\Truevow_Tenant_Customer_Portal_Service\app\api\intake\leads\[id]\status**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\Truevow_Tenant_Customer_Portal_Service\app\api\intake\leads\[id]\status_

- **Deep nesting (depth 6): ..\..\Truevow_Tenant_Customer_Portal_Service\app\api\intake\leads\[id]\unlock**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\Truevow_Tenant_Customer_Portal_Service\app\api\intake\leads\[id]\unlock_

- **Deep nesting (depth 6): ..\..\Truevow_Tenant_Customer_Portal_Service\app\api\leverage\case\[caseId]\damages**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\Truevow_Tenant_Customer_Portal_Service\app\api\leverage\case\[caseId]\damages_

- **Deep nesting (depth 7): ..\..\Truevow_Tenant_Customer_Portal_Service\app\api\leverage\case\[caseId]\damages\save**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\Truevow_Tenant_Customer_Portal_Service\app\api\leverage\case\[caseId]\damages\save_

- **Deep nesting (depth 6): ..\..\Truevow_Tenant_Customer_Portal_Service\app\api\leverage\case\[caseId]\deadlines**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\Truevow_Tenant_Customer_Portal_Service\app\api\leverage\case\[caseId]\deadlines_

- **Deep nesting (depth 7): ..\..\Truevow_Tenant_Customer_Portal_Service\app\api\leverage\case\[caseId]\deadlines\save**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\Truevow_Tenant_Customer_Portal_Service\app\api\leverage\case\[caseId]\deadlines\save_

- **Deep nesting (depth 6): ..\..\Truevow_Tenant_Customer_Portal_Service\app\api\leverage\case\[caseId]\detail**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\Truevow_Tenant_Customer_Portal_Service\app\api\leverage\case\[caseId]\detail_

- **Deep nesting (depth 6): ..\..\Truevow_Tenant_Customer_Portal_Service\app\api\leverage\case\[caseId]\disbursement**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\Truevow_Tenant_Customer_Portal_Service\app\api\leverage\case\[caseId]\disbursement_

- **Deep nesting (depth 7): ..\..\Truevow_Tenant_Customer_Portal_Service\app\api\leverage\case\[caseId]\disbursement\save**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\Truevow_Tenant_Customer_Portal_Service\app\api\leverage\case\[caseId]\disbursement\save_

- **Deep nesting (depth 6): ..\..\Truevow_Tenant_Customer_Portal_Service\app\api\leverage\case\[caseId]\economics**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\Truevow_Tenant_Customer_Portal_Service\app\api\leverage\case\[caseId]\economics_

- **Deep nesting (depth 6): ..\..\Truevow_Tenant_Customer_Portal_Service\app\api\leverage\case\[caseId]\events**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\Truevow_Tenant_Customer_Portal_Service\app\api\leverage\case\[caseId]\events_



## Related Service
- [[Cross-Service/truevow-tenant-customer-portal-service|Service Page]]
