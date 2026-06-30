# Code Structure Map — SaaS Administration Service

> Auto-generated: 2026-05-29
> Repository: `TrueVow_SaaS_Administration_Service`

## File Breakdown

| Extension | Count |
|-----------|-------|
| .ts | 939 |
| .md | 485 |
| .tsx | 286 |
| .js | 205 |
| .sql | 149 |
| .py | 55 |
| .json | 25 |
| .ps1 | 17 |
| .sh | 17 |
| .txt | 15 |
| (none) | 4 |
| .css | 1 |
| .ini | 1 |
| .yml | 1 |
| .local | 1 |
| .example | 1 |
| .yaml | 1 |
| .tsbuildinfo | 1 |

## Directory Tree

```
```

## Component Graph

```mermaid
graph TD
```

## Issues Found (471)

### MEDIUM

- **"page.tsx" appears in 198 locations**
  > Found at: ..\..\TrueVow_SaaS_Administration_Service\app\(auth)\get-clerk-id\page.tsx, ..\..\TrueVow_SaaS_Administration_Service\app\(auth)\login\[...rest]\page.tsx, ..\..\TrueVow_SaaS_Administration_Service\app\(auth)\login\page.tsx...
  > _..\..\TrueVow_SaaS_Administration_Service\app\(auth)\get-clerk-id\page.tsx_

- **"route.ts" appears in 579 locations**
  > Found at: ..\..\TrueVow_SaaS_Administration_Service\app\(auth)\sign-in\callback\route.ts, ..\..\TrueVow_SaaS_Administration_Service\app\api\admin\connect\analytics\member-performance\route.ts, ..\..\TrueVow_SaaS_Administration_Service\app\api\admin\connect\analytics\network-growth\route.ts...
  > _..\..\TrueVow_SaaS_Administration_Service\app\(auth)\sign-in\callback\route.ts_

- **"layout.tsx" appears in 5 locations**
  > Found at: ..\..\TrueVow_SaaS_Administration_Service\app\(auth)\layout.tsx, ..\..\TrueVow_SaaS_Administration_Service\app\(dashboard)\customer-support\layout.tsx, ..\..\TrueVow_SaaS_Administration_Service\app\(dashboard)\layout.tsx...
  > _..\..\TrueVow_SaaS_Administration_Service\app\(auth)\layout.tsx_

- **"route-AmmarZayn.ts" appears in 2 locations**
  > Found at: ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\[provider]\stats\route-AmmarZayn.ts, ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\[provider]\sync-booking\route-AmmarZayn.ts
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\[provider]\stats\route-AmmarZayn.ts_

- **"PORT_CONFIGURATION.md" appears in 2 locations**
  > Found at: ..\..\TrueVow_SaaS_Administration_Service\docs\00-main\PORT_CONFIGURATION.md, ..\..\TrueVow_SaaS_Administration_Service\docs\01-setup\PORT_CONFIGURATION.md
  > _..\..\TrueVow_SaaS_Administration_Service\docs\00-main\PORT_CONFIGURATION.md_

- **"README.md" appears in 14 locations**
  > Found at: ..\..\TrueVow_SaaS_Administration_Service\docs\00-main\README.md, ..\..\TrueVow_SaaS_Administration_Service\docs\01-setup\README.md, ..\..\TrueVow_SaaS_Administration_Service\docs\02-architecture\README.md...
  > _..\..\TrueVow_SaaS_Administration_Service\docs\00-main\README.md_

- **"WORKING_CACHE.md" appears in 2 locations**
  > Found at: ..\..\TrueVow_SaaS_Administration_Service\docs\00-main\WORKING_CACHE.md, ..\..\TrueVow_SaaS_Administration_Service\docs\01-main\WORKING_CACHE.md
  > _..\..\TrueVow_SaaS_Administration_Service\docs\00-main\WORKING_CACHE.md_

- **"useKeyboardShortcuts.ts" appears in 2 locations**
  > Found at: ..\..\TrueVow_SaaS_Administration_Service\hooks\useKeyboardShortcuts.ts, ..\..\TrueVow_SaaS_Administration_Service\lib\hooks\useKeyboardShortcuts.ts
  > _..\..\TrueVow_SaaS_Administration_Service\hooks\useKeyboardShortcuts.ts_

- **"middleware.ts" appears in 5 locations**
  > Found at: ..\..\TrueVow_SaaS_Administration_Service\lib\api\middleware.ts, ..\..\TrueVow_SaaS_Administration_Service\lib\integrations\draft-service\middleware.ts, ..\..\TrueVow_SaaS_Administration_Service\lib\security\guardrails\middleware.ts...
  > _..\..\TrueVow_SaaS_Administration_Service\lib\api\middleware.ts_

- **"validation.ts" appears in 3 locations**
  > Found at: ..\..\TrueVow_SaaS_Administration_Service\lib\api\validation.ts, ..\..\TrueVow_SaaS_Administration_Service\lib\security\validation.ts, ..\..\TrueVow_SaaS_Administration_Service\lib\utils\validation.ts
  > _..\..\TrueVow_SaaS_Administration_Service\lib\api\validation.ts_

- **"index.ts" appears in 14 locations**
  > Found at: ..\..\TrueVow_SaaS_Administration_Service\lib\auth\index.ts, ..\..\TrueVow_SaaS_Administration_Service\lib\database\repositories\index.ts, ..\..\TrueVow_SaaS_Administration_Service\lib\database\index.ts...
  > _..\..\TrueVow_SaaS_Administration_Service\lib\auth\index.ts_

- **"tenants.ts" appears in 2 locations**
  > Found at: ..\..\TrueVow_SaaS_Administration_Service\lib\database\repositories\tenants.ts, ..\..\TrueVow_SaaS_Administration_Service\lib\queries\tenants.ts
  > _..\..\TrueVow_SaaS_Administration_Service\lib\database\repositories\tenants.ts_

- **"client.ts" appears in 11 locations**
  > Found at: ..\..\TrueVow_SaaS_Administration_Service\lib\integrations\billing-service\client.ts, ..\..\TrueVow_SaaS_Administration_Service\lib\integrations\connect\client.ts, ..\..\TrueVow_SaaS_Administration_Service\lib\integrations\draft-service\client.ts...
  > _..\..\TrueVow_SaaS_Administration_Service\lib\integrations\billing-service\client.ts_

- **"types.ts" appears in 3 locations**
  > Found at: ..\..\TrueVow_SaaS_Administration_Service\lib\integrations\connect\types.ts, ..\..\TrueVow_SaaS_Administration_Service\lib\integrations\draft\types.ts, ..\..\TrueVow_SaaS_Administration_Service\lib\integrations\settle\types.ts
  > _..\..\TrueVow_SaaS_Administration_Service\lib\integrations\connect\types.ts_

- **"encryption.ts" appears in 2 locations**
  > Found at: ..\..\TrueVow_SaaS_Administration_Service\lib\integrations\credential-vault\encryption.ts, ..\..\TrueVow_SaaS_Administration_Service\lib\encryption.ts
  > _..\..\TrueVow_SaaS_Administration_Service\lib\integrations\credential-vault\encryption.ts_

- **"service.ts" appears in 2 locations**
  > Found at: ..\..\TrueVow_SaaS_Administration_Service\lib\integrations\credential-vault\service.ts, ..\..\TrueVow_SaaS_Administration_Service\lib\integrations\crm\service.ts
  > _..\..\TrueVow_SaaS_Administration_Service\lib\integrations\credential-vault\service.ts_

- **"client.py" appears in 8 locations**
  > Found at: ..\..\TrueVow_SaaS_Administration_Service\lib\integrations\crm\casepeer\client.py, ..\..\TrueVow_SaaS_Administration_Service\lib\integrations\crm\clio\client.py, ..\..\TrueVow_SaaS_Administration_Service\lib\integrations\crm\cloudlex\client.py...
  > _..\..\TrueVow_SaaS_Administration_Service\lib\integrations\crm\casepeer\client.py_

- **"timesheet.ts" appears in 2 locations**
  > Found at: ..\..\TrueVow_SaaS_Administration_Service\lib\security\timeTracking\timesheet.ts, ..\..\TrueVow_SaaS_Administration_Service\shared\types\timesheet.ts
  > _..\..\TrueVow_SaaS_Administration_Service\lib\security\timeTracking\timesheet.ts_

- **"server.ts" appears in 2 locations**
  > Found at: ..\..\TrueVow_SaaS_Administration_Service\lib\supabase\server.ts, ..\..\TrueVow_SaaS_Administration_Service\lib\websocket\server.ts
  > _..\..\TrueVow_SaaS_Administration_Service\lib\supabase\server.ts_

- **"billing-service.test.ts" appears in 2 locations**
  > Found at: ..\..\TrueVow_SaaS_Administration_Service\tests\api\v1\billing\billing-service.test.ts, ..\..\TrueVow_SaaS_Administration_Service\tests\api\v1\tenant-app-phase2\billing-service.test.ts
  > _..\..\TrueVow_SaaS_Administration_Service\tests\api\v1\billing\billing-service.test.ts_

- **"usage.test.ts" appears in 2 locations**
  > Found at: ..\..\TrueVow_SaaS_Administration_Service\tests\api\v1\tenant-portal\usage.test.ts, ..\..\TrueVow_SaaS_Administration_Service\tests\api\v1\tenants\usage.test.ts
  > _..\..\TrueVow_SaaS_Administration_Service\tests\api\v1\tenant-portal\usage.test.ts_

- **"tenants.test.ts" appears in 2 locations**
  > Found at: ..\..\TrueVow_SaaS_Administration_Service\tests\api\v1\tenants.test.ts, ..\..\TrueVow_SaaS_Administration_Service\tests\integration\api\tenants.test.ts
  > _..\..\TrueVow_SaaS_Administration_Service\tests\api\v1\tenants.test.ts_

### LOW

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\(dashboard)\admin\connect\compliance\violations**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\(dashboard)\admin\connect\compliance\violations_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\(dashboard)\admin\connect\members\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\(dashboard)\admin\connect\members\[id]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\(dashboard)\sales\pipeline\cycle\[lead_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\(dashboard)\sales\pipeline\cycle\[lead_id]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\(dashboard)\workflows\[tenantId]\[workflowId]\audit**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\(dashboard)\workflows\[tenantId]\[workflowId]\audit_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\(dashboard)\workflows\[tenantId]\[workflowId]\variants**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\(dashboard)\workflows\[tenantId]\[workflowId]\variants_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\admin\connect\analytics\member-performance**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\admin\connect\analytics\member-performance_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\admin\connect\analytics\network-growth**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\admin\connect\analytics\network-growth_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\admin\connect\api-keys\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\admin\connect\api-keys\[id]_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\admin\connect\api-keys\[id]\revoke**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\admin\connect\api-keys\[id]\revoke_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\admin\connect\api-keys\tenant**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\admin\connect\api-keys\tenant_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\admin\connect\api-keys\tenant\[tenantId]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\admin\connect\api-keys\tenant\[tenantId]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\admin\connect\compliance\report**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\admin\connect\compliance\report_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\admin\connect\compliance\violations**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\admin\connect\compliance\violations_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\admin\connect\compliance\violations\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\admin\connect\compliance\violations\[id]_

- **Deep nesting (depth 8): ..\..\TrueVow_SaaS_Administration_Service\app\api\admin\connect\compliance\violations\[id]\resolve**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\admin\connect\compliance\violations\[id]\resolve_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\admin\connect\members\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\admin\connect\members\[id]_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\admin\connect\members\[id]\approve**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\admin\connect\members\[id]\approve_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\admin\connect\members\[id]\reject**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\admin\connect\members\[id]\reject_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\admin\connect\members\[id]\suspend**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\admin\connect\members\[id]\suspend_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\admin\connect\members\[id]\verify-insurance**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\admin\connect\members\[id]\verify-insurance_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\admin\connect\members\[id]\verify-license**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\admin\connect\members\[id]\verify-license_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\admin\connect\vetting\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\admin\connect\vetting\[id]_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\admin\connect\vetting\[id]\complete**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\admin\connect\vetting\[id]\complete_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\admin\connect\vetting\due**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\admin\connect\vetting\due_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\admin\draft\rules\[rule_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\admin\draft\rules\[rule_id]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\admin\draft\templates\stats**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\admin\draft\templates\stats_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\admin\settle\analytics\compliance**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\admin\settle\analytics\compliance_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\admin\settle\analytics\contributions**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\admin\settle\analytics\contributions_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\admin\settle\analytics\data-quality**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\admin\settle\analytics\data-quality_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\admin\settle\analytics\usage**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\admin\settle\analytics\usage_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\admin\settle\api-keys\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\admin\settle\api-keys\[id]_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\admin\settle\api-keys\[id]\revoke**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\admin\settle\api-keys\[id]\revoke_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\admin\settle\api-keys\[id]\rotate**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\admin\settle\api-keys\[id]\rotate_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\admin\settle\api-keys\tenant**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\admin\settle\api-keys\tenant_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\admin\settle\api-keys\tenant\[tenantId]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\admin\settle\api-keys\tenant\[tenantId]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\admin\settle\contributions\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\admin\settle\contributions\[id]_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\admin\settle\contributions\[id]\approve**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\admin\settle\contributions\[id]\approve_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\admin\settle\contributions\[id]\reject**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\admin\settle\contributions\[id]\reject_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\admin\settle\contributions\pending**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\admin\settle\contributions\pending_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\admin\settle\founding-members\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\admin\settle\founding-members\[id]_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\admin\settle\founding-members\[id]\contributions**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\admin\settle\founding-members\[id]\contributions_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\admin\settle\founding-members\[id]\status**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\admin\settle\founding-members\[id]\status_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\admin\audit-log\export**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\admin\audit-log\export_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\admin\health\run**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\admin\health\run_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\admin\integrations\catalog**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\admin\integrations\catalog_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\admin\plg-rules\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\admin\plg-rules\[id]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\admin\plg-rules\dry-run**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\admin\plg-rules\dry-run_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\admin\plg-rules\nlp-translate**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\admin\plg-rules\nlp-translate_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\admin\plg-rules\resolve**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\admin\plg-rules\resolve_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\admin\pricing\addons**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\admin\pricing\addons_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\admin\pricing\tiers**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\admin\pricing\tiers_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\admin\tenant-instances\[tenant_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\admin\tenant-instances\[tenant_id]_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\admin\tenant-instances\[tenant_id]\health**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\admin\tenant-instances\[tenant_id]\health_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\admin\tenant-instances\provision**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\admin\tenant-instances\provision_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\admin\tenants\[tenant_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\admin\tenants\[tenant_id]_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\admin\tenants\[tenant_id]\billing-summary**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\admin\tenants\[tenant_id]\billing-summary_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\admin\tenants\[tenant_id]\integrations**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\admin\tenants\[tenant_id]\integrations_

- **Deep nesting (depth 8): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\admin\tenants\[tenant_id]\integrations\[credential_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\admin\tenants\[tenant_id]\integrations\[credential_id]_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\admin\tenants\[tenant_id]\override**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\admin\tenants\[tenant_id]\override_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\admin\tenants\[tenant_id]\plan**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\admin\tenants\[tenant_id]\plan_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\admin\tenants\[tenant_id]\upgrade**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\admin\tenants\[tenant_id]\upgrade_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\admin\tenants\provisioning**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\admin\tenants\provisioning_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\admin\users\[admin_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\admin\users\[admin_id]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\admin\webhooks\billing**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\admin\webhooks\billing_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\admin\webhooks\billing\subscription-updated**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\admin\webhooks\billing\subscription-updated_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\analytics\intake\rescore**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\analytics\intake\rescore_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\analytics\intake\score**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\analytics\intake\score_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\analytics\portal-events\metrics**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\analytics\portal-events\metrics_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\analytics\recommendations\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\analytics\recommendations\[id]_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\analytics\recommendations\[id]\outcome**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\analytics\recommendations\[id]\outcome_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\analytics\recommendations\evaluate**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\analytics\recommendations\evaluate_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\analytics\recommendations\outcomes**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\analytics\recommendations\outcomes_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\auth\2fa\disable**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\auth\2fa\disable_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\auth\2fa\setup**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\auth\2fa\setup_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\auth\2fa\verify**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\auth\2fa\verify_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\auth\sso\login**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\auth\sso\login_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\auth\sso\login\[provider]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\auth\sso\login\[provider]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\auth\sso\providers**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\auth\sso\providers_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\billing\adjustments\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\billing\adjustments\[id]_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\billing\adjustments\[id]\review**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\billing\adjustments\[id]\review_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\billing\dashboard\settle-progress**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\billing\dashboard\settle-progress_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\billing\outcomes\invoices**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\billing\outcomes\invoices_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\billing\outcomes\tracking**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\billing\outcomes\tracking_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\billing\prepaid\apply**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\billing\prepaid\apply_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\billing\prepaid\balance**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\billing\prepaid\balance_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\billing\prepaid\balance\[tenant_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\billing\prepaid\balance\[tenant_id]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\billing\prepaid\credits**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\billing\prepaid\credits_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\billing\stripe\create-subscription**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\billing\stripe\create-subscription_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\billing\stripe\webhook**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\billing\stripe\webhook_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\billing\tenants\[tenant_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\billing\tenants\[tenant_id]_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\billing\tenants\[tenant_id]\credits**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\billing\tenants\[tenant_id]\credits_

- **Deep nesting (depth 8): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\billing\tenants\[tenant_id]\credits\purchase**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\billing\tenants\[tenant_id]\credits\purchase_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\billing\tenants\[tenant_id]\pillar-status**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\billing\tenants\[tenant_id]\pillar-status_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\billing\tenants\[tenant_id]\settle**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\billing\tenants\[tenant_id]\settle_

- **Deep nesting (depth 8): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\billing\tenants\[tenant_id]\settle\activate**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\billing\tenants\[tenant_id]\settle\activate_

- **Deep nesting (depth 8): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\billing\tenants\[tenant_id]\settle\quote**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\billing\tenants\[tenant_id]\settle\quote_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\billing\usage\[tenant_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\billing\usage\[tenant_id]_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\billing\usage\[tenant_id]\current-period**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\billing\usage\[tenant_id]\current-period_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\billing\usage\invoice-items**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\billing\usage\invoice-items_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\billing\usage-pricing-rules\[rule_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\billing\usage-pricing-rules\[rule_id]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\business-development\calls\webhook**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\business-development\calls\webhook_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\customer-portal\auth\magic-link**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\customer-portal\auth\magic-link_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\customer-portal\auth\validate**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\customer-portal\auth\validate_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\customer-portal\tenants\[tenant_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\customer-portal\tenants\[tenant_id]_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\customer-portal\tenants\[tenant_id]\intake**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\customer-portal\tenants\[tenant_id]\intake_

- **Deep nesting (depth 8): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\customer-portal\tenants\[tenant_id]\intake\dashboard**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\customer-portal\tenants\[tenant_id]\intake\dashboard_

- **Deep nesting (depth 8): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\customer-portal\tenants\[tenant_id]\intake\leads**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\customer-portal\tenants\[tenant_id]\intake\leads_

- **Deep nesting (depth 8): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\customer-portal\tenants\[tenant_id]\intake\sessions**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\customer-portal\tenants\[tenant_id]\intake\sessions_

- **Deep nesting (depth 8): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\customer-portal\tenants\[tenant_id]\intake\test-data**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\customer-portal\tenants\[tenant_id]\intake\test-data_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\customer-portal\tenants\[tenant_id]\settings**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\customer-portal\tenants\[tenant_id]\settings_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\customer-portal\tenants\[tenant_id]\users**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\customer-portal\tenants\[tenant_id]\users_

- **Deep nesting (depth 8): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\customer-portal\tenants\[tenant_id]\users\[clerk_user_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\customer-portal\tenants\[tenant_id]\users\[clerk_user_id]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\customer-portal\tickets\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\customer-portal\tickets\[id]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\customer-success\calls\webhook**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\customer-success\calls\webhook_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\customers\[tenant_id]\contacts**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\customers\[tenant_id]\contacts_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\customers\[tenant_id]\contacts\[contact_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\customers\[tenant_id]\contacts\[contact_id]_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\customers\[tenant_id]\contacts\duplicates**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\customers\[tenant_id]\contacts\duplicates_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\customers\[tenant_id]\contacts\export**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\customers\[tenant_id]\contacts\export_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\customers\[tenant_id]\contacts\import**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\customers\[tenant_id]\contacts\import_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\customers\[tenant_id]\contacts\merge**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\customers\[tenant_id]\contacts\merge_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\customers\[tenant_id]\contacts\relationships**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\customers\[tenant_id]\contacts\relationships_

- **Deep nesting (depth 8): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\customers\[tenant_id]\contacts\relationships\[contact_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\customers\[tenant_id]\contacts\relationships\[contact_id]_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\customers\[tenant_id]\contacts\search**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\customers\[tenant_id]\contacts\search_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\dashboard\overview\diagnostics**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\dashboard\overview\diagnostics_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\dashboard\overview\test**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\dashboard\overview\test_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\founding\contact\[contact_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\founding\contact\[contact_id]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\[provider]\stats**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\[provider]\stats_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\[provider]\sync-booking**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\[provider]\sync-booking_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\[provider]\sync-lead**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\[provider]\sync-lead_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\[provider]\test**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\[provider]\test_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\crm\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\crm\[id]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\crm\connect**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\crm\connect_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\crm\connections**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\crm\connections_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\crm\disconnect**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\crm\disconnect_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\crm\internal**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\crm\internal_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\crm\internal\clio**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\crm\internal\clio_

- **Deep nesting (depth 8): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\crm\internal\clio\sync-lead**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\crm\internal\clio\sync-lead_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\crm\internal\mycase**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\crm\internal\mycase_

- **Deep nesting (depth 8): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\crm\internal\mycase\sync-lead**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\crm\internal\mycase\sync-lead_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\crm\oauth**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\crm\oauth_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\crm\oauth\authorize**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\crm\oauth\authorize_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\crm\oauth\callback**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\crm\oauth\callback_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\crm\providers**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\crm\providers_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\crm\sync**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\crm\sync_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\crm\sync-booking**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\crm\sync-booking_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\crm\sync-lead**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\crm\sync-lead_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\email\domains**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\email\domains_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\email\domains\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\email\domains\[id]_

- **Deep nesting (depth 8): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\email\domains\[id]\ip-addresses**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\email\domains\[id]\ip-addresses_

- **Deep nesting (depth 8): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\email\domains\[id]\verify**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\email\domains\[id]\verify_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\email\test**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\email\test_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\grafana\dashboards**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\grafana\dashboards_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\grafana\dashboards\[uid]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\grafana\dashboards\[uid]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\grafana\setup**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\grafana\setup_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\grafana\test**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\grafana\test_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\helpscout\sync**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\helpscout\sync_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\twilio\configure**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\twilio\configure_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\twilio\phone**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\twilio\phone_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\twilio\phone\[phone_number]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\twilio\phone\[phone_number]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\twilio\provision**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\integrations\twilio\provision_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\leads\[lead_id]\assign**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\leads\[lead_id]\assign_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\leads\[lead_id]\convert-to-tenant**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\leads\[lead_id]\convert-to-tenant_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\leads\[lead_id]\duplicates**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\leads\[lead_id]\duplicates_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\leads\[lead_id]\process**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\leads\[lead_id]\process_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\leads\[lead_id]\score**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\leads\[lead_id]\score_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\marketing\analytics\sequences**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\marketing\analytics\sequences_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\marketing\analytics\sequences\[sequence_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\marketing\analytics\sequences\[sequence_id]_

- **Deep nesting (depth 8): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\marketing\analytics\sequences\[sequence_id]\performance**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\marketing\analytics\sequences\[sequence_id]\performance_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\marketing\campaigns\[campaign_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\marketing\campaigns\[campaign_id]_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\marketing\campaigns\[campaign_id]\execute**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\marketing\campaigns\[campaign_id]\execute_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\marketing\gtm\strategies**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\marketing\gtm\strategies_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\marketing\gtm\strategies\[strategy_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\marketing\gtm\strategies\[strategy_id]_

- **Deep nesting (depth 8): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\marketing\gtm\strategies\[strategy_id]\execute**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\marketing\gtm\strategies\[strategy_id]\execute_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\marketing\outreach\sequences**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\marketing\outreach\sequences_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\marketing\outreach\sequences\[sequence_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\marketing\outreach\sequences\[sequence_id]_

- **Deep nesting (depth 8): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\marketing\outreach\sequences\[sequence_id]\start**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\marketing\outreach\sequences\[sequence_id]\start_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\oauth\authorize\[integration]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\oauth\authorize\[integration]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\oauth\callback\[integration]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\oauth\callback\[integration]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\onboarding\attorneys\[attorneyId]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\onboarding\attorneys\[attorneyId]_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\onboarding\attorneys\[attorneyId]\specializations**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\onboarding\attorneys\[attorneyId]\specializations_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\onboarding\law-firm\internal-status**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\onboarding\law-firm\internal-status_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\onboarding\law-firm\progress**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\onboarding\law-firm\progress_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\onboarding\law-firm\step-1**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\onboarding\law-firm\step-1_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\onboarding\law-firm\step-2**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\onboarding\law-firm\step-2_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\onboarding\law-firm\step-3**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\onboarding\law-firm\step-3_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\onboarding\law-firm\step-4**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\onboarding\law-firm\step-4_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\onboarding\law-firm\step-5**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\onboarding\law-firm\step-5_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\onboarding\milestone\complete**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\onboarding\milestone\complete_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\onboarding\sequences\template**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\onboarding\sequences\template_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\onboarding\sequences\template\[templateKey]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\onboarding\sequences\template\[templateKey]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\onboarding\sequences\templates**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\onboarding\sequences\templates_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\calendar\integrations**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\calendar\integrations_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\calls\webhook**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\calls\webhook_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\closing\activities**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\closing\activities_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\closing\activities\[lead_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\closing\activities\[lead_id]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\founding-members\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\founding-members\[id]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\llm\agents**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\llm\agents_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\llm\conversations**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\llm\conversations_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\llm\conversations\[conversation_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\llm\conversations\[conversation_id]_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\llm\conversations\start**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\llm\conversations\start_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\llm\performance**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\llm\performance_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\nudges\[lead_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\nudges\[lead_id]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\onboarding\progress**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\onboarding\progress_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\onboarding\progress\[tenant_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\onboarding\progress\[tenant_id]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\onboarding\start**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\onboarding\start_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\onboarding\tasks**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\onboarding\tasks_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\onboarding\tasks\[task_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\onboarding\tasks\[task_id]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\onboarding\templates**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\onboarding\templates_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\onboarding\tenants**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\onboarding\tenants_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\onboarding\tenants\[tenant_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\onboarding\tenants\[tenant_id]_

- **Deep nesting (depth 8): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\onboarding\tenants\[tenant_id]\tasks**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\onboarding\tenants\[tenant_id]\tasks_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\pipeline\advance**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\pipeline\advance_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\pipeline\automation**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\pipeline\automation_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\pipeline\cycle**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\pipeline\cycle_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\pipeline\cycle\[lead_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\pipeline\cycle\[lead_id]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\pipeline\stages**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\pipeline\stages_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\pipeline\stuck**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\pipeline\stuck_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\provisioning\start**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\provisioning\start_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\provisioning\status**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\provisioning\status_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\provisioning\status\[tenant_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\provisioning\status\[tenant_id]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\provisioning\workflows**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\provisioning\workflows_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\qualification\[lead_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\qualification\[lead_id]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\qualification\assess**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\qualification\assess_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\qualification\criteria**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\qualification\criteria_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\referrals\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\referrals\[id]_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\referrals\[id]\convert**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\sales\referrals\[id]\convert_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\security\audit\report**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\security\audit\report_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\security\compliance\check**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\security\compliance\check_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\security\remediation\actions**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\security\remediation\actions_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\security\threats\[event_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\security\threats\[event_id]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\settle\contributions\[contribution_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\settle\contributions\[contribution_id]_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\settle\contributions\[contribution_id]\approve**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\settle\contributions\[contribution_id]\approve_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\settle\contributions\[contribution_id]\reject**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\settle\contributions\[contribution_id]\reject_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\settle\contributions\pending**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\settle\contributions\pending_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\settle\founding-members\[member_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\settle\founding-members\[member_id]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\settle\waitlist\entries**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\settle\waitlist\entries_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\settle\waitlist\entries\[entry_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\settle\waitlist\entries\[entry_id]_

- **Deep nesting (depth 8): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\settle\waitlist\entries\[entry_id]\approve**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\settle\waitlist\entries\[entry_id]\approve_

- **Deep nesting (depth 8): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\settle\waitlist\entries\[entry_id]\reject**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\settle\waitlist\entries\[entry_id]\reject_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\ai\analyze**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\ai\analyze_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\ai\capabilities**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\ai\capabilities_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\ai\capabilities\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\ai\capabilities\[id]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\ai\chat**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\ai\chat_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\analytics\dashboard**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\analytics\dashboard_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\attachments\[attachment_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\attachments\[attachment_id]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\attachments\upload**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\attachments\upload_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\automation-rules\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\automation-rules\[id]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\calendar\availability**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\calendar\availability_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\calendar\events**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\calendar\events_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\calls\webhook**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\calls\webhook_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\case\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\case\[id]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\contact\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\contact\[id]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\cs-territories\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\cs-territories\[id]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\email\gmail**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\email\gmail_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\email\gmail\parse**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\email\gmail\parse_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\email\outlook**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\email\outlook_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\email\outlook\parse**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\email\outlook\parse_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\email\send**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\email\send_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\email\webhook**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\email\webhook_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\kb\articles**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\kb\articles_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\kb\articles\[article_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\kb\articles\[article_id]_

- **Deep nesting (depth 8): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\kb\articles\[article_id]\embedding**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\kb\articles\[article_id]\embedding_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\kb\file-search**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\kb\file-search_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\kb\file-search\generate**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\kb\file-search\generate_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\kb\file-search\ingest-faq**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\kb\file-search\ingest-faq_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\kb\file-search\search**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\kb\file-search\search_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\kb\file-search\upload**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\kb\file-search\upload_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\kb\search**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\kb\search_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\on-duty\schedule**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\on-duty\schedule_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\portal\tickets**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\portal\tickets_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\portal\tickets\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\portal\tickets\[id]_

- **Deep nesting (depth 8): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\portal\tickets\[id]\messages**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\portal\tickets\[id]\messages_

- **Deep nesting (depth 8): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\portal\tickets\[id]\reply**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\portal\tickets\[id]\reply_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\recordings\[recording_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\recordings\[recording_id]_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\recordings\[recording_id]\export**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\recordings\[recording_id]\export_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\recordings\reminders**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\recordings\reminders_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\sla\escalate**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\sla\escalate_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\sla\escalated**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\sla\escalated_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\sla\initialize**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\sla\initialize_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\sla\metrics**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\sla\metrics_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\sla\policies**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\sla\policies_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\sla\policies\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\sla\policies\[id]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\sla\tickets**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\sla\tickets_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\templates\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\templates\[id]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\tickets\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\tickets\[id]_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\tickets\[id]\assign**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\tickets\[id]\assign_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\tickets\[id]\collision**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\tickets\[id]\collision_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\tickets\[id]\escalate**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\tickets\[id]\escalate_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\tickets\[id]\messages**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\tickets\[id]\messages_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\tickets\[id]\participants**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\tickets\[id]\participants_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\tickets\[id]\reply**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\tickets\[id]\reply_

- **Deep nesting (depth 8): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\tickets\[id]\reply\chat**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\tickets\[id]\reply\chat_

- **Deep nesting (depth 8): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\tickets\[id]\reply\facebook**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\tickets\[id]\reply\facebook_

- **Deep nesting (depth 8): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\tickets\[id]\reply\sms**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\tickets\[id]\reply\sms_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\tickets\[id]\send-survey**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\tickets\[id]\send-survey_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\tickets\[id]\tags**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\tickets\[id]\tags_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\video\zoom**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\video\zoom_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\video\zoom\meeting**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\video\zoom\meeting_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\video\zoom\webhook**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\video\zoom\webhook_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\webhooks\chat**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\webhooks\chat_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\webhooks\facebook**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\webhooks\facebook_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\webhooks\form**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\webhooks\form_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\webhooks\sms**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\webhooks\sms_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\workflows\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\workflows\[id]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\workflows\templates**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\support\workflows\templates_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tasks\[task_id]\comments**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tasks\[task_id]\comments_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tasks\[task_id]\dependencies**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tasks\[task_id]\dependencies_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tasks\[task_id]\dependencies\[dependency_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tasks\[task_id]\dependencies\[dependency_id]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tasks\[task_id]\time-log**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tasks\[task_id]\time-log_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\team-chat\channels\[channel_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\team-chat\channels\[channel_id]_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\team-chat\channels\[channel_id]\members**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\team-chat\channels\[channel_id]\members_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\team-chat\channels\[channel_id]\messages**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\team-chat\channels\[channel_id]\messages_

- **Deep nesting (depth 8): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\team-chat\channels\[channel_id]\messages\[message_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\team-chat\channels\[channel_id]\messages\[message_id]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\activity\recent**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\activity\recent_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\billing\downgrade**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\billing\downgrade_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\billing\invoices**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\billing\invoices_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\billing\invoices\[invoice_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\billing\invoices\[invoice_id]_

- **Deep nesting (depth 8): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\billing\invoices\[invoice_id]\pdf**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\billing\invoices\[invoice_id]\pdf_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\billing\overview**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\billing\overview_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\billing\plans**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\billing\plans_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\billing\plans\compare**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\billing\plans\compare_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\billing\tier**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\billing\tier_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\billing\upgrade**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\billing\upgrade_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\billing\usage**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\billing\usage_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\billing\usage\monthly**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\billing\usage\monthly_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\billing\usage\recent**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\billing\usage\recent_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\billing\usage\record**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\billing\usage\record_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\billing\usage\summary**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\billing\usage\summary_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\connect\members**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\connect\members_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\connect\referrals**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\connect\referrals_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\connect\stats**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\connect\stats_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\draft\analytics**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\draft\analytics_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\draft\analytics\dashboard**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\draft\analytics\dashboard_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\draft\analytics\statistics**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\draft\analytics\statistics_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\draft\documents**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\draft\documents_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\draft\feature-flags**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\draft\feature-flags_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\draft\feature-flags\disable-server-side**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\draft\feature-flags\disable-server-side_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\draft\feature-flags\disclaimer**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\draft\feature-flags\disclaimer_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\draft\feature-flags\enable-server-side**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\draft\feature-flags\enable-server-side_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\draft\feature-flags\status**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\draft\feature-flags\status_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\draft\rules**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\draft\rules_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\draft\rules\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\draft\rules\[id]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\draft\stats**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\draft\stats_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\draft\sync**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\draft\sync_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\draft\sync\rules**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\draft\sync\rules_

- **Deep nesting (depth 8): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\draft\sync\rules\encrypted**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\draft\sync\rules\encrypted_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\draft\sync\version**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\draft\sync\version_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\draft\templates**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\draft\templates_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\draft\templates\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\draft\templates\[id]_

- **Deep nesting (depth 8): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\draft\templates\[id]\apply**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\draft\templates\[id]\apply_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\draft\validation**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\draft\validation_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\draft\validation\history**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\draft\validation\history_

- **Deep nesting (depth 8): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\draft\validation\history\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\draft\validation\history\[id]_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\draft\validation\log**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\draft\validation\log_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\intake\leads**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\intake\leads_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\intake\process**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\intake\process_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\intake\session**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\intake\session_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\intake\session\[session_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\intake\session\[session_id]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\intake\sessions**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\intake\sessions_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\intake\sessions\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\intake\sessions\[id]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\intake\start**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\intake\start_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\intake\stats**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\intake\stats_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\intake\voice**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\intake\voice_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\settle\settlements**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\settle\settlements_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\settle\settlements\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\settle\settlements\[id]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\settle\stats**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\settle\stats_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\usage\export**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\usage\export_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\usage\overview**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\usage\overview_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\users\[user_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenant\users\[user_id]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\calendar**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\calendar_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\calendar\assignments**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\calendar\assignments_

- **Deep nesting (depth 8): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\calendar\assignments\[assignment_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\calendar\assignments\[assignment_id]_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\calendar\connections**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\calendar\connections_

- **Deep nesting (depth 8): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\calendar\connections\[connection_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\calendar\connections\[connection_id]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\config**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\config_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\contacts**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\contacts_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\draft**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\draft_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\draft\analytics**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\draft\analytics_

- **Deep nesting (depth 8): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\draft\analytics\dashboard**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\draft\analytics\dashboard_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\draft\feature-flags**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\draft\feature-flags_

- **Deep nesting (depth 8): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\draft\feature-flags\disclaimer**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\draft\feature-flags\disclaimer_

- **Deep nesting (depth 8): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\draft\feature-flags\status**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\draft\feature-flags\status_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\draft\rules**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\draft\rules_

- **Deep nesting (depth 8): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\draft\rules\[rule_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\draft\rules\[rule_id]_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\draft\sync**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\draft\sync_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\draft\templates**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\draft\templates_

- **Deep nesting (depth 8): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\draft\templates\[template_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\draft\templates\[template_id]_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\draft\validation**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\draft\validation_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\feature-access**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\feature-access_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\fsm-script**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\fsm-script_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\modules**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\modules_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\phone-numbers**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\phone-numbers_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\recording-config**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\recording-config_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\settings**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\settings_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\settings\notifications**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\settings\notifications_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\settings\voice-ai**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\settings\voice-ai_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\subscription**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\subscription_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\subscription\change-plan**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\subscription\change-plan_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\usage**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\usage_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\usage-limits**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\tenants\[tenant_id]\usage-limits_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\test-runner\[run_id]\stream**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\test-runner\[run_id]\stream_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\time-tracking\calendar\[entry_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\time-tracking\calendar\[entry_id]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\time-tracking\notifications\[notification_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\time-tracking\notifications\[notification_id]_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\time-tracking\notifications\[notification_id]\read**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\time-tracking\notifications\[notification_id]\read_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\time-tracking\outcomes\[outcome_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\time-tracking\outcomes\[outcome_id]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\time-tracking\reports\daily**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\time-tracking\reports\daily_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\time-tracking\reports\monthly**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\time-tracking\reports\monthly_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\time-tracking\reports\weekly**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\time-tracking\reports\weekly_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\time-tracking\self-reported\[entry_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\time-tracking\self-reported\[entry_id]_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\time-tracking\self-reported\[entry_id]\approve**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\time-tracking\self-reported\[entry_id]\approve_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\time-tracking\self-reported\[entry_id]\reject**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\time-tracking\self-reported\[entry_id]\reject_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\time-tracking\session\current**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\time-tracking\session\current_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\time-tracking\session\start**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\time-tracking\session\start_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\time-tracking\session\stop**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\time-tracking\session\stop_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\verify\certificates\[certificateRef]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\verify\certificates\[certificateRef]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\verify\certificates\by-interaction**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\verify\certificates\by-interaction_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\verify\certificates\by-interaction\[interactionType]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\verify\certificates\by-interaction\[interactionType]_

- **Deep nesting (depth 8): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\verify\certificates\by-interaction\[interactionType]\[interactionId]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\verify\certificates\by-interaction\[interactionType]\[interactionId]_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\verify\certificates\pending**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\verify\certificates\pending_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\verify\public\[certificateRef]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\verify\public\[certificateRef]_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\verify\public\[certificateRef]\download.ots**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\verify\public\[certificateRef]\download.ots_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\webhooks\cs-support\subscription-updated**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\webhooks\cs-support\subscription-updated_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\webhooks\cs-support\tenant-created**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\webhooks\cs-support\tenant-created_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\webhooks\platform\milestone**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\webhooks\platform\milestone_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\webhooks\sales-crm\subscription-updated**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\webhooks\sales-crm\subscription-updated_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\webhooks\sales-crm\tenant-created**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\webhooks\sales-crm\tenant-created_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\v1\webhooks\sales-crm\tenant-status-changed**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\v1\webhooks\sales-crm\tenant-status-changed_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\workflows\[tenantId]\[workflowId]\approvals**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\workflows\[tenantId]\[workflowId]\approvals_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\workflows\[tenantId]\[workflowId]\approve**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\workflows\[tenantId]\[workflowId]\approve_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\workflows\[tenantId]\[workflowId]\audit-logs**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\workflows\[tenantId]\[workflowId]\audit-logs_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\workflows\[tenantId]\[workflowId]\bridge-config**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\workflows\[tenantId]\[workflowId]\bridge-config_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\workflows\[tenantId]\[workflowId]\bridge-health**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\workflows\[tenantId]\[workflowId]\bridge-health_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\workflows\[tenantId]\[workflowId]\comments**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\workflows\[tenantId]\[workflowId]\comments_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\workflows\[tenantId]\[workflowId]\commit**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\workflows\[tenantId]\[workflowId]\commit_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\workflows\[tenantId]\[workflowId]\llm-config**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\workflows\[tenantId]\[workflowId]\llm-config_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\workflows\[tenantId]\[workflowId]\policy-changes**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\workflows\[tenantId]\[workflowId]\policy-changes_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\workflows\[tenantId]\[workflowId]\reads**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\workflows\[tenantId]\[workflowId]\reads_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\workflows\[tenantId]\[workflowId]\reject**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\workflows\[tenantId]\[workflowId]\reject_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\workflows\[tenantId]\[workflowId]\reviewers**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\workflows\[tenantId]\[workflowId]\reviewers_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\workflows\[tenantId]\[workflowId]\reviewers\audit**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\workflows\[tenantId]\[workflowId]\reviewers\audit_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\workflows\[tenantId]\[workflowId]\reviewers\seed**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\workflows\[tenantId]\[workflowId]\reviewers\seed_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\workflows\[tenantId]\[workflowId]\settings**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\workflows\[tenantId]\[workflowId]\settings_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\workflows\[tenantId]\[workflowId]\status-transitions**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\workflows\[tenantId]\[workflowId]\status-transitions_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\workflows\[tenantId]\[workflowId]\submit**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\workflows\[tenantId]\[workflowId]\submit_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\workflows\[tenantId]\[workflowId]\sync-dograh**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\workflows\[tenantId]\[workflowId]\sync-dograh_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\workflows\[tenantId]\[workflowId]\variants**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\workflows\[tenantId]\[workflowId]\variants_

- **Deep nesting (depth 7): ..\..\TrueVow_SaaS_Administration_Service\app\api\workflows\[tenantId]\[workflowId]\variants\config**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\workflows\[tenantId]\[workflowId]\variants\config_

- **Deep nesting (depth 6): ..\..\TrueVow_SaaS_Administration_Service\app\api\workflows\reviewers\[reviewerId]\digest-bulk**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_SaaS_Administration_Service\app\api\workflows\reviewers\[reviewerId]\digest-bulk_

- **Archive folder found: docs/archive/**
  > Archive folders should be outside the repo or explicitly tagged for deletion review.
  > _C:\Users\yasha\OneDrive\Documents\TrueVow\Cursor\TrueVow_SaaS_Administration_Service\docs\archive_



## Related Service
- [[Cross-Service/truevow-saas-administration-service|Service Page]]
