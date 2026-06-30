# Code Structure Map — Tenant Application Service

> Auto-generated: 2026-05-29
> Repository: `TrueVow_Tenant_Application_Service`

## File Breakdown

| Extension | Count |
|-----------|-------|
| .py | 1136 |
| .json | 461 |
| (none) | 365 |
| .md | 231 |
| .tsx | 216 |
| .ts | 126 |
| .mdx | 113 |
| .sql | 59 |
| .yaml | 54 |
| .sh | 33 |
| .html | 31 |
| .js | 21 |
| .svg | 15 |
| .txt | 10 |
| .tf | 10 |
| .ps1 | 9 |
| .example | 7 |
| .bat | 7 |
| .css | 6 |
| .toml | 6 |
| .m4a | 6 |
| .ini | 4 |
| .mjs | 4 |
| .mts | 4 |
| .dll | 4 |
| .yml | 4 |
| .local | 3 |
| .template | 3 |
| .ico | 3 |
| .ipynb | 2 |
| .mako | 1 |
| .so | 1 |
| .0 | 1 |
| .1 | 1 |
| .conf | 1 |
| .gif | 1 |
| .fly | 1 |
| .ort | 1 |
| .exe | 1 |
| .tfvars | 1 |
| .pcm | 1 |

## Directory Tree

```
```

## Component Graph

```mermaid
graph TD
```

## Issues Found (234)

### HIGH

- **46 test files flat in tests/ — no subfolder organization**
  > Group by domain: billing/, voice/, draft/, integration/, etc.
  > _..\..\TrueVow_Tenant_Application_Service\tests_

- **Multiple models/ directories exist — choose one**
  > C:\Users\yasha\OneDrive\Documents\TrueVow\Cursor\TrueVow_Tenant_Application_Service\models, C:\Users\yasha\OneDrive\Documents\TrueVow\Cursor\TrueVow_Tenant_Application_Service\app\models — one is likely stale or shadowing the other.
  > _C:\Users\yasha\OneDrive\Documents\TrueVow\Cursor\TrueVow_Tenant_Application_Service_

### MEDIUM

- **3 .bat files at repository root**
  > Move to a subfolder (scripts/)
  > _C:\Users\yasha\OneDrive\Documents\TrueVow\Cursor\TrueVow_Tenant_Application_Service_

- **2 .ipynb files at repository root**
  > Move to a subfolder (notebooks/)
  > _C:\Users\yasha\OneDrive\Documents\TrueVow\Cursor\TrueVow_Tenant_Application_Service_

- **10 .md files at repository root**
  > Move to a subfolder (docs/)
  > _C:\Users\yasha\OneDrive\Documents\TrueVow\Cursor\TrueVow_Tenant_Application_Service_

- **Both migrations/ and database/ exist — possible dual ORM setup**
  > One ORM configuration is likely stale. Review and archive the unused one.
  > _C:\Users\yasha\OneDrive\Documents\TrueVow\Cursor\TrueVow_Tenant_Application_Service\database_

- **"auth.py" appears in 6 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\api\v1\endpoints\auth.py, ..\..\TrueVow_Tenant_Application_Service\app\middleware\auth.py, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\mcp_server\auth.py...
  > _..\..\TrueVow_Tenant_Application_Service\app\api\v1\endpoints\auth.py_

- **"draft.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\api\v1\endpoints\draft.py, ..\..\TrueVow_Tenant_Application_Service\app\routes\draft.py
  > _..\..\TrueVow_Tenant_Application_Service\app\api\v1\endpoints\draft.py_

- **"health.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\api\v1\endpoints\health.py, ..\..\TrueVow_Tenant_Application_Service\app\core\health.py
  > _..\..\TrueVow_Tenant_Application_Service\app\api\v1\endpoints\health.py_

- **"intake.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\api\v1\endpoints\intake.py, ..\..\TrueVow_Tenant_Application_Service\app\api\v2\endpoints\intake.py, ..\..\TrueVow_Tenant_Application_Service\app\models\intake.py
  > _..\..\TrueVow_Tenant_Application_Service\app\api\v1\endpoints\intake.py_

- **"portal.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\api\v1\endpoints\portal.py, ..\..\TrueVow_Tenant_Application_Service\app\models\portal.py
  > _..\..\TrueVow_Tenant_Application_Service\app\api\v1\endpoints\portal.py_

- **"waitlist.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\api\v1\endpoints\waitlist.py, ..\..\TrueVow_Tenant_Application_Service\app\core\access_control\waitlist.py, ..\..\TrueVow_Tenant_Application_Service\app\services\booking\waitlist.py
  > _..\..\TrueVow_Tenant_Application_Service\app\api\v1\endpoints\waitlist.py_

- **"router.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\api\v1\router.py, ..\..\TrueVow_Tenant_Application_Service\app\api\v2\router.py, ..\..\TrueVow_Tenant_Application_Service\app\services\calendar\router.py
  > _..\..\TrueVow_Tenant_Application_Service\app\api\v1\router.py_

- **"admin_alert_system.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\core\access_control\admin_alert_system.py, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\session\admin_alert_system.py
  > _..\..\TrueVow_Tenant_Application_Service\app\core\access_control\admin_alert_system.py_

- **"rate_limiter.py" appears in 4 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\core\access_control\rate_limiter.py, ..\..\TrueVow_Tenant_Application_Service\app\middleware\rate_limiter.py, ..\..\TrueVow_Tenant_Application_Service\app\services\security\rate_limiter.py...
  > _..\..\TrueVow_Tenant_Application_Service\app\core\access_control\rate_limiter.py_

- **"session_persistence.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\core\access_control\session_persistence.py, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\session\session_persistence.py
  > _..\..\TrueVow_Tenant_Application_Service\app\core\access_control\session_persistence.py_

- **"middleware.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\core\feature_flags\middleware.py, ..\..\TrueVow_Tenant_Application_Service\app\core\middleware.py, ..\..\TrueVow_Tenant_Application_Service\app\observability\middleware.py
  > _..\..\TrueVow_Tenant_Application_Service\app\core\feature_flags\middleware.py_

- **"service.py" appears in 13 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\core\feature_flags\service.py, ..\..\TrueVow_Tenant_Application_Service\app\services\dashboard\service.py, ..\..\TrueVow_Tenant_Application_Service\app\services\data_retention\service.py...
  > _..\..\TrueVow_Tenant_Application_Service\app\core\feature_flags\service.py_

- **"config.py" appears in 8 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\core\config.py, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\telephony\providers\ari\config.py, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\telephony\providers\cloudonix\config.py...
  > _..\..\TrueVow_Tenant_Application_Service\app\core\config.py_

- **"database.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\core\database.py, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\db\database.py
  > _..\..\TrueVow_Tenant_Application_Service\app\core\database.py_

- **"event_handlers.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\core\event_handlers.py, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\pipecat\event_handlers.py
  > _..\..\TrueVow_Tenant_Application_Service\app\core\event_handlers.py_

- **"exceptions.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\core\exceptions.py, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\pipecat\exceptions.py
  > _..\..\TrueVow_Tenant_Application_Service\app\core\exceptions.py_

- **"logging.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\core\logging.py, ..\..\TrueVow_Tenant_Application_Service\app\observability\logging.py
  > _..\..\TrueVow_Tenant_Application_Service\app\core\logging.py_

- **"outbox.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\core\outbox.py, ..\..\TrueVow_Tenant_Application_Service\app\events\outbox.py
  > _..\..\TrueVow_Tenant_Application_Service\app\core\outbox.py_

- **"tracing.py" appears in 4 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\core\tracing.py, ..\..\TrueVow_Tenant_Application_Service\app\observability\tracing.py, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\mcp_server\tracing.py...
  > _..\..\TrueVow_Tenant_Application_Service\app\core\tracing.py_

- **"audit.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\middleware\audit.py, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\workflow\audit.py
  > _..\..\TrueVow_Tenant_Application_Service\app\middleware\audit.py_

- **"tenant.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\middleware\tenant.py, ..\..\TrueVow_Tenant_Application_Service\app\models\tenant.py
  > _..\..\TrueVow_Tenant_Application_Service\app\middleware\tenant.py_

- **"usage_tracking.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\middleware\usage_tracking.py, ..\..\TrueVow_Tenant_Application_Service\app\services\billing\usage_tracking.py
  > _..\..\TrueVow_Tenant_Application_Service\app\middleware\usage_tracking.py_

- **"auth_audit.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\models\auth_audit.py, ..\..\TrueVow_Tenant_Application_Service\app\services\security\auth_audit.py
  > _..\..\TrueVow_Tenant_Application_Service\app\models\auth_audit.py_

- **"campaign_attribution.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\models\campaign_attribution.py, ..\..\TrueVow_Tenant_Application_Service\app\services\analytics\campaign_attribution.py
  > _..\..\TrueVow_Tenant_Application_Service\app\models\campaign_attribution.py_

- **"user.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\models\user.py, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\routes\user.py
  > _..\..\TrueVow_Tenant_Application_Service\app\models\user.py_

- **"metrics.py" appears in 4 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\monitoring\metrics.py, ..\..\TrueVow_Tenant_Application_Service\app\observability\metrics.py, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\routes\metrics.py...
  > _..\..\TrueVow_Tenant_Application_Service\app\monitoring\metrics.py_

- **"route.ts" appears in 15 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\portal\app\api\auth\login\route.ts, ..\..\TrueVow_Tenant_Application_Service\app\portal\app\api\auth\logout\route.ts, ..\..\TrueVow_Tenant_Application_Service\app\portal\app\api\auth\me\route.ts...
  > _..\..\TrueVow_Tenant_Application_Service\app\portal\app\api\auth\login\route.ts_

- **"page.tsx" appears in 41 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\portal\app\bookings\page.tsx, ..\..\TrueVow_Tenant_Application_Service\app\portal\app\certificates\[ref]\page.tsx, ..\..\TrueVow_Tenant_Application_Service\app\portal\app\certificates\page.tsx...
  > _..\..\TrueVow_Tenant_Application_Service\app\portal\app\bookings\page.tsx_

- **"globals.css" appears in 3 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\portal\app\globals.css, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\evals\visualizer\src\app\globals.css, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\ui\src\app\globals.css
  > _..\..\TrueVow_Tenant_Application_Service\app\portal\app\globals.css_

- **"layout.tsx" appears in 3 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\portal\app\layout.tsx, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\evals\visualizer\src\app\layout.tsx, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\ui\src\app\layout.tsx
  > _..\..\TrueVow_Tenant_Application_Service\app\portal\app\layout.tsx_

- **"AppLayout.tsx" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\portal\components\layout\AppLayout.tsx, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\ui\src\components\layout\AppLayout.tsx
  > _..\..\TrueVow_Tenant_Application_Service\app\portal\components\layout\AppLayout.tsx_

- **"ContextualSidebar.tsx" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\portal\components\layout\ContextualSidebar.tsx, ..\..\TrueVow_Tenant_Application_Service\app\portal\components\ContextualSidebar.tsx
  > _..\..\TrueVow_Tenant_Application_Service\app\portal\components\layout\ContextualSidebar.tsx_

- **"client.ts" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\portal\lib\api\client.ts, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\sdk\typescript\src\client.ts
  > _..\..\TrueVow_Tenant_Application_Service\app\portal\lib\api\client.ts_

- **"index.ts" appears in 21 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\portal\lib\auth\index.ts, ..\..\TrueVow_Tenant_Application_Service\app\portal\lib\db\index.ts, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\mcp_server\ts_validator\src\index.ts...
  > _..\..\TrueVow_Tenant_Application_Service\app\portal\lib\auth\index.ts_

- **"middleware.ts" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\portal\lib\auth\middleware.ts, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\ui\src\middleware.ts
  > _..\..\TrueVow_Tenant_Application_Service\app\portal\lib\auth\middleware.ts_

- **"README.md" appears in 34 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\portal\lib\auth\README.md, ..\..\TrueVow_Tenant_Application_Service\app\portal\README.md, ..\..\TrueVow_Tenant_Application_Service\app\services\compliance\README.md...
  > _..\..\TrueVow_Tenant_Application_Service\app\portal\lib\auth\README.md_

- **"tsconfig.json" appears in 5 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\portal\tsconfig.json, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\mcp_server\ts_validator\tsconfig.json, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\evals\visualizer\tsconfig.json...
  > _..\..\TrueVow_Tenant_Application_Service\app\portal\tsconfig.json_

- **"base.py" appears in 8 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\booking\calendar\base.py, ..\..\TrueVow_Tenant_Application_Service\app\services\integrations\video\base.py, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\filesystem\base.py...
  > _..\..\TrueVow_Tenant_Application_Service\app\services\booking\calendar\base.py_

- **"scheduler.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\data_retention\scheduler.py, ..\..\TrueVow_Tenant_Application_Service\app\services\notifications\scheduler.py
  > _..\..\TrueVow_Tenant_Application_Service\app\services\data_retention\scheduler.py_

- **"engine.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\guardrail\engine.py, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\fsm_engine\engine.py
  > _..\..\TrueVow_Tenant_Application_Service\app\services\guardrail\engine.py_

- **"client.py" appears in 8 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\integrations\api_gateway\client.py, ..\..\TrueVow_Tenant_Application_Service\app\services\integrations\billing\client.py, ..\..\TrueVow_Tenant_Application_Service\app\services\integrations\crm\clio\client.py...
  > _..\..\TrueVow_Tenant_Application_Service\app\services\integrations\api_gateway\client.py_

- **"saas_admin_client.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\integrations\crm\saas_admin_client.py, ..\..\TrueVow_Tenant_Application_Service\app\services\verification\blockchain\saas_admin_client.py
  > _..\..\TrueVow_Tenant_Application_Service\app\services\integrations\crm\saas_admin_client.py_

- **"fsm_session_store.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\deepgram_agent\fsm_session_store.py, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\intake_engine\fsm\fsm_session_store.py
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\deepgram_agent\fsm_session_store.py_

- **"env.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\alembic\env.py, ..\..\TrueVow_Tenant_Application_Service\operations\database\migrations\env.py
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\alembic\env.py_

- **"models.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\db\models.py, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\pricing\models.py
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\db\models.py_

- **"create_workflow.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\mcp_server\tools\create_workflow.py, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\examples\python\create_workflow.py
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\mcp_server\tools\create_workflow.py_

- **"node_types.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\mcp_server\tools\node_types.py, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\routes\node_types.py
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\mcp_server\tools\node_types.py_

- **"types.ts" appears in 6 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\mcp_server\ts_validator\src\types.ts, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\sdk\typescript\src\types.ts, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\ui\src\app\workflow\[workflowId]\components\workflow-tester\types.ts...
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\mcp_server\ts_validator\src\types.ts_

- **"package-lock.json" appears in 5 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\mcp_server\ts_validator\package-lock.json, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\evals\visualizer\package-lock.json, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\examples\typescript\package-lock.json...
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\mcp_server\ts_validator\package-lock.json_

- **"package.json" appears in 5 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\mcp_server\ts_validator\package.json, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\evals\visualizer\package.json, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\examples\typescript\package.json...
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\mcp_server\ts_validator\package.json_

- **"knowledge_base.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\routes\knowledge_base.py, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\schemas\knowledge_base.py, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\workflow\tools\knowledge_base.py
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\routes\knowledge_base.py_

- **"main.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\routes\main.py, ..\..\TrueVow_Tenant_Application_Service\app\main.py
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\routes\main.py_

- **"workflow_recording.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\routes\workflow_recording.py, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\schemas\workflow_recording.py
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\routes\workflow_recording.py_

- **"workflow.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\routes\workflow.py, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\schemas\workflow.py, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\sdk\python\src\dograh_sdk\workflow.py
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\routes\workflow.py_

- **"errors.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\campaign\errors.py, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\workflow\errors.py, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\sdk\python\src\dograh_sdk\errors.py
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\campaign\errors.py_

- **"runner.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\campaign\runner.py, ..\..\TrueVow_Tenant_Application_Service\tests\load\runner.py
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\campaign\runner.py_

- **"registry.py" appears in 5 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\configuration\registry.py, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\integrations\registry.py, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\pricing\registry.py...
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\configuration\registry.py_

- **"constants.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\gender\constants.py, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\workflow\node_specs\constants.py, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\constants.py
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\gender\constants.py_

- **"AGENTS.md" appears in 8 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\integrations\AGENTS.md, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\telephony\providers\AGENTS.md, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\telephony\AGENTS.md...
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\integrations\AGENTS.md_

- **"app.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\smart_turn\app.py, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\app.py
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\smart_turn\app.py_

- **"provider.py" appears in 7 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\telephony\providers\ari\provider.py, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\telephony\providers\cloudonix\provider.py, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\telephony\providers\plivo\provider.py...
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\telephony\providers\ari\provider.py_

- **"serializers.py" appears in 7 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\telephony\providers\ari\serializers.py, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\telephony\providers\cloudonix\serializers.py, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\telephony\providers\plivo\serializers.py...
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\telephony\providers\ari\serializers.py_

- **"strategies.py" appears in 4 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\telephony\providers\ari\strategies.py, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\telephony\providers\cloudonix\strategies.py, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\telephony\providers\telnyx\strategies.py...
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\telephony\providers\ari\strategies.py_

- **"transport.py" appears in 7 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\telephony\providers\ari\transport.py, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\telephony\providers\cloudonix\transport.py, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\telephony\providers\plivo\transport.py...
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\telephony\providers\ari\transport.py_

- **"routes.py" appears in 6 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\telephony\providers\cloudonix\routes.py, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\telephony\providers\plivo\routes.py, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\telephony\providers\telnyx\routes.py...
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\telephony\providers\cloudonix\routes.py_

- **"CLAUDE.md" appears in 6 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\telephony\providers\CLAUDE.md, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\CLAUDE.md, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\CLAUDE.md...
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\telephony\providers\CLAUDE.md_

- **"_base.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\workflow\node_specs\_base.py, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\sdk\python\src\dograh_sdk\typed\_base.py
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services\workflow\node_specs\_base.py_

- **"conftest.py" appears in 5 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\tests\conftest.py, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\conftest.py, ..\..\TrueVow_Tenant_Application_Service\tests\integration\conftest.py...
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\tests\conftest.py_

- **"alembic.ini" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\alembic.ini, ..\..\TrueVow_Tenant_Application_Service\alembic.ini
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\alembic.ini_

- **"Dockerfile" appears in 3 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\Dockerfile, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\ui\Dockerfile, ..\..\TrueVow_Tenant_Application_Service\operations\infrastructure\gcp\docker\Dockerfile
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\Dockerfile_

- **"pyproject.toml" appears in 3 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\pyproject.toml, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\sdk\python\pyproject.toml, ..\..\TrueVow_Tenant_Application_Service\pyproject.toml
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\pyproject.toml_

- **"pytest.ini" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\pytest.ini, ..\..\TrueVow_Tenant_Application_Service\pytest.ini
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\pytest.ini_

- **"requirements.txt" appears in 3 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\requirements.txt, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\examples\python\requirements.txt, ..\..\TrueVow_Tenant_Application_Service\requirements.txt
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\requirements.txt_

- **"create.mdx" appears in 5 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\api-reference\agents\runs\create.mdx, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\api-reference\api-keys\create.mdx, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\api-reference\campaigns\create.mdx...
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\api-reference\agents\runs\create.mdx_

- **"get.mdx" appears in 5 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\api-reference\agents\runs\get.mdx, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\api-reference\agents\get.mdx, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\api-reference\campaigns\get.mdx...
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\api-reference\agents\runs\get.mdx_

- **"list.mdx" appears in 6 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\api-reference\agents\runs\list.mdx, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\api-reference\agents\list.mdx, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\api-reference\api-keys\list.mdx...
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\api-reference\agents\runs\list.mdx_

- **"archive.mdx" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\api-reference\agents\archive.mdx, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\api-reference\api-keys\archive.mdx
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\api-reference\agents\archive.mdx_

- **"update.mdx" appears in 5 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\api-reference\agents\update.mdx, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\api-reference\campaigns\update.mdx, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\api-reference\telephony-configs\phone-numbers\update.mdx...
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\api-reference\agents\update.mdx_

- **"inbound.mdx" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\api-reference\calls\inbound.mdx, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\integrations\telephony\inbound.mdx
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\api-reference\calls\inbound.mdx_

- **"delete.mdx" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\api-reference\telephony-configs\phone-numbers\delete.mdx, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\api-reference\telephony-configs\delete.mdx
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\api-reference\telephony-configs\phone-numbers\delete.mdx_

- **"api-keys.mdx" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\api-reference\api-keys.mdx, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\configurations\api-keys.mdx
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\api-reference\api-keys.mdx_

- **"campaigns.mdx" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\api-reference\campaigns.mdx, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\core-concepts\campaigns.mdx
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\api-reference\campaigns.mdx_

- **"overview.mdx" appears in 3 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\api-reference\overview.mdx, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\integrations\telephony\overview.mdx, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\integrations\overview.mdx
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\api-reference\overview.mdx_

- **"introduction.mdx" appears in 5 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\contribution\introduction.mdx, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\deployment\introduction.mdx, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\sdks\introduction.mdx...
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\contribution\introduction.mdx_

- **"webhooks.mdx" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\developer\webhooks.mdx, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\integrations\telephony\webhooks.mdx
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\developer\webhooks.mdx_

- **"end-call.mdx" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\voice-agent\tools\end-call.mdx, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\voice-agent\end-call.mdx
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\voice-agent\tools\end-call.mdx_

- **"favicon.ico" appears in 3 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\favicon.ico, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\evals\visualizer\src\app\favicon.ico, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\ui\src\app\favicon.ico
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\favicon.ico_

- **"file.svg" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\evals\visualizer\public\file.svg, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\ui\public\file.svg
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\evals\visualizer\public\file.svg_

- **"globe.svg" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\evals\visualizer\public\globe.svg, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\ui\public\globe.svg
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\evals\visualizer\public\globe.svg_

- **"next.svg" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\evals\visualizer\public\next.svg, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\ui\public\next.svg
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\evals\visualizer\public\next.svg_

- **"vercel.svg" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\evals\visualizer\public\vercel.svg, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\ui\public\vercel.svg
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\evals\visualizer\public\vercel.svg_

- **"window.svg" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\evals\visualizer\public\window.svg, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\ui\public\window.svg
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\evals\visualizer\public\window.svg_

- **"eslint.config.mjs" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\evals\visualizer\eslint.config.mjs, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\ui\eslint.config.mjs
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\evals\visualizer\eslint.config.mjs_

- **"next.config.ts" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\evals\visualizer\next.config.ts, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\ui\next.config.ts
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\evals\visualizer\next.config.ts_

- **"pnpm-lock.yaml" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\evals\visualizer\pnpm-lock.yaml, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\ui\pnpm-lock.yaml
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\evals\visualizer\pnpm-lock.yaml_

- **"postcss.config.mjs" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\evals\visualizer\postcss.config.mjs, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\ui\postcss.config.mjs
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\evals\visualizer\postcss.config.mjs_

- **"LICENSE" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\sdk\python\LICENSE, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\sdk\typescript\LICENSE
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\sdk\python\LICENSE_

- **"utils.ts" appears in 3 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\ui\src\app\workflow\[workflowId]\components\workflow-tester\utils.ts, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\ui\src\components\workflow\conversation\utils.ts, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\ui\src\lib\utils.ts
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\ui\src\app\workflow\[workflowId]\components\workflow-tester\utils.ts_

- **"client.gen.ts" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\ui\src\client\client\client.gen.ts, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\ui\src\client\client.gen.ts
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\ui\src\client\client\client.gen.ts_

- **"types.gen.ts" appears in 3 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\ui\src\client\client\types.gen.ts, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\ui\src\client\core\types.gen.ts, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\ui\src\client\types.gen.ts
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\ui\src\client\client\types.gen.ts_

- **"utils.gen.ts" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\ui\src\client\client\utils.gen.ts, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\ui\src\client\core\utils.gen.ts
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\ui\src\client\client\utils.gen.ts_

- **"filters.ts" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\ui\src\lib\filters.ts, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\ui\src\types\filters.ts
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\ui\src\lib\filters.ts_

- **"fly.toml" appears in 3 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\fly.toml, ..\..\TrueVow_Tenant_Application_Service\operations\infrastructure\flyio\fly.toml, ..\..\TrueVow_Tenant_Application_Service\fly.toml
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\fly.toml_

- **"config_loader.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\intake_engine\fsm\config_loader.py, ..\..\TrueVow_Tenant_Application_Service\app\services\voice\fsm_engine\config_loader.py
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\intake_engine\fsm\config_loader.py_

- **"domain_signals.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\fsm_engine\domain_signals.py, ..\..\TrueVow_Tenant_Application_Service\scripts\archive\domain_signals.py
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\fsm_engine\domain_signals.py_

- **"normalizer.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\app\services\voice\fsm_engine\normalizer.py, ..\..\TrueVow_Tenant_Application_Service\scripts\archive\normalizer.py
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\fsm_engine\normalizer.py_

- **"default.json" appears in 12 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\config\_archived_old_fsm\old_fsm_backup_20260502_015214\flows\car_accident\default.json, ..\..\TrueVow_Tenant_Application_Service\config\_archived_old_fsm\old_fsm_backup_20260502_015214\flows\dog_bite\default.json, ..\..\TrueVow_Tenant_Application_Service\config\_archived_old_fsm\old_fsm_backup_20260502_015214\flows\other_pi\default.json...
  > _..\..\TrueVow_Tenant_Application_Service\config\_archived_old_fsm\old_fsm_backup_20260502_015214\flows\car_accident\default.json_

- **"questions.json" appears in 42 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\config\_archived_old_fsm\old_fsm_backup_20260502_015214\practice_modules\_core\questions.json, ..\..\TrueVow_Tenant_Application_Service\config\_archived_old_fsm\old_fsm_backup_20260502_015214\practice_modules\assault_defense\questions.json, ..\..\TrueVow_Tenant_Application_Service\config\_archived_old_fsm\old_fsm_backup_20260502_015214\practice_modules\asylum\questions.json...
  > _..\..\TrueVow_Tenant_Application_Service\config\_archived_old_fsm\old_fsm_backup_20260502_015214\practice_modules\_core\questions.json_

- **"blocklist_ref.json" appears in 40 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\config\_archived_old_fsm\old_fsm_backup_20260502_015214\practice_modules\assault_defense\blocklist_ref.json, ..\..\TrueVow_Tenant_Application_Service\config\_archived_old_fsm\old_fsm_backup_20260502_015214\practice_modules\asylum\blocklist_ref.json, ..\..\TrueVow_Tenant_Application_Service\config\_archived_old_fsm\old_fsm_backup_20260502_015214\practice_modules\car_accident\blocklist_ref.json...
  > _..\..\TrueVow_Tenant_Application_Service\config\_archived_old_fsm\old_fsm_backup_20260502_015214\practice_modules\assault_defense\blocklist_ref.json_

- **"scoring_rules.json" appears in 40 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\config\_archived_old_fsm\old_fsm_backup_20260502_015214\practice_modules\assault_defense\scoring_rules.json, ..\..\TrueVow_Tenant_Application_Service\config\_archived_old_fsm\old_fsm_backup_20260502_015214\practice_modules\asylum\scoring_rules.json, ..\..\TrueVow_Tenant_Application_Service\config\_archived_old_fsm\old_fsm_backup_20260502_015214\practice_modules\car_accident\scoring_rules.json...
  > _..\..\TrueVow_Tenant_Application_Service\config\_archived_old_fsm\old_fsm_backup_20260502_015214\practice_modules\assault_defense\scoring_rules.json_

- **"sol_rules.json" appears in 40 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\config\_archived_old_fsm\old_fsm_backup_20260502_015214\practice_modules\assault_defense\sol_rules.json, ..\..\TrueVow_Tenant_Application_Service\config\_archived_old_fsm\old_fsm_backup_20260502_015214\practice_modules\asylum\sol_rules.json, ..\..\TrueVow_Tenant_Application_Service\config\_archived_old_fsm\old_fsm_backup_20260502_015214\practice_modules\car_accident\sol_rules.json...
  > _..\..\TrueVow_Tenant_Application_Service\config\_archived_old_fsm\old_fsm_backup_20260502_015214\practice_modules\assault_defense\sol_rules.json_

- **"default_questions.json" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\config\_archived_old_fsm\old_fsm_backup_20260502_015214\templates\default_questions.json, ..\..\TrueVow_Tenant_Application_Service\config\templates\default_questions.json
  > _..\..\TrueVow_Tenant_Application_Service\config\_archived_old_fsm\old_fsm_backup_20260502_015214\templates\default_questions.json_

- **"sms_templates.json" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\config\_archived_old_fsm\old_fsm_backup_20260502_015214\templates\sms_templates.json, ..\..\TrueVow_Tenant_Application_Service\config\templates\sms_templates.json
  > _..\..\TrueVow_Tenant_Application_Service\config\_archived_old_fsm\old_fsm_backup_20260502_015214\templates\sms_templates.json_

- **"system_states.json" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\config\_archived_old_fsm\old_fsm_backup_20260502_015214\templates\system_states.json, ..\..\TrueVow_Tenant_Application_Service\config\templates\system_states.json
  > _..\..\TrueVow_Tenant_Application_Service\config\_archived_old_fsm\old_fsm_backup_20260502_015214\templates\system_states.json_

- **"taxonomy.yaml" appears in 9 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\config\domains\bankruptcy\taxonomy.yaml, ..\..\TrueVow_Tenant_Application_Service\config\domains\business_law\taxonomy.yaml, ..\..\TrueVow_Tenant_Application_Service\config\domains\criminal_defense\taxonomy.yaml...
  > _..\..\TrueVow_Tenant_Application_Service\config\domains\bankruptcy\taxonomy.yaml_

- **"firm_config.json" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\config\firms\florida_test_firm\firm_config.json, ..\..\TrueVow_Tenant_Application_Service\config\firms\oakwood_law_firm\firm_config.json
  > _..\..\TrueVow_Tenant_Application_Service\config\firms\florida_test_firm\firm_config.json_

- **"response_normalization.json" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\config\keywords\global\response_normalization.json, ..\..\TrueVow_Tenant_Application_Service\config\keywords\response_normalization.json
  > _..\..\TrueVow_Tenant_Application_Service\config\keywords\global\response_normalization.json_

- **"pack.yaml" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\config\languages\english\pack.yaml, ..\..\TrueVow_Tenant_Application_Service\config\languages\spanish\pack.yaml
  > _..\..\TrueVow_Tenant_Application_Service\config\languages\english\pack.yaml_

- **"cd.json" appears in 50 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\config\statute_buckets\AK\cd.json, ..\..\TrueVow_Tenant_Application_Service\config\statute_buckets\AL\cd.json, ..\..\TrueVow_Tenant_Application_Service\config\statute_buckets\AR\cd.json...
  > _..\..\TrueVow_Tenant_Application_Service\config\statute_buckets\AK\cd.json_

- **"fl.json" appears in 50 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\config\statute_buckets\AK\fl.json, ..\..\TrueVow_Tenant_Application_Service\config\statute_buckets\AL\fl.json, ..\..\TrueVow_Tenant_Application_Service\config\statute_buckets\AR\fl.json...
  > _..\..\TrueVow_Tenant_Application_Service\config\statute_buckets\AK\fl.json_

- **"pi.json" appears in 51 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\config\statute_buckets\AK\pi.json, ..\..\TrueVow_Tenant_Application_Service\config\statute_buckets\AL\pi.json, ..\..\TrueVow_Tenant_Application_Service\config\statute_buckets\AR\pi.json...
  > _..\..\TrueVow_Tenant_Application_Service\config\statute_buckets\AK\pi.json_

- **"smoke_test.json" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\config\workflows\smoke_firm\smoke_test.json, ..\..\TrueVow_Tenant_Application_Service\config\workflows\test_firm\smoke_test.json
  > _..\..\TrueVow_Tenant_Application_Service\config\workflows\smoke_firm\smoke_test.json_

- **"env.example" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\config\env.example, ..\..\TrueVow_Tenant_Application_Service\env.example
  > _..\..\TrueVow_Tenant_Application_Service\config\env.example_

- **"index.html" appears in 3 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\docs\archive\index.html, ..\..\TrueVow_Tenant_Application_Service\web\demo\index.html, ..\..\TrueVow_Tenant_Application_Service\web\draft\index.html
  > _..\..\TrueVow_Tenant_Application_Service\docs\archive\index.html_

- **"GEMINI_LIVE_API_REFERENCE.md" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\docs\GEMINI_LIVE_API_REFERENCE.md, ..\..\TrueVow_Tenant_Application_Service\GEMINI_LIVE_API_REFERENCE.md
  > _..\..\TrueVow_Tenant_Application_Service\docs\GEMINI_LIVE_API_REFERENCE.md_

- **"docker-compose.yml" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\operations\database\docker-compose.yml, ..\..\TrueVow_Tenant_Application_Service\operations\infrastructure\gcp\docker\docker-compose.yml
  > _..\..\TrueVow_Tenant_Application_Service\operations\database\docker-compose.yml_

- **"deployment.yaml" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\operations\infrastructure\gcp\kubernetes\deployment.yaml, ..\..\TrueVow_Tenant_Application_Service\operations\infrastructure\k8s\deployment.yaml
  > _..\..\TrueVow_Tenant_Application_Service\operations\infrastructure\gcp\kubernetes\deployment.yaml_

- **"main.tf" appears in 5 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\operations\infrastructure\gcp\terraform\modules\database\main.tf, ..\..\TrueVow_Tenant_Application_Service\operations\infrastructure\gcp\terraform\modules\gke\main.tf, ..\..\TrueVow_Tenant_Application_Service\operations\infrastructure\gcp\terraform\modules\networking\main.tf...
  > _..\..\TrueVow_Tenant_Application_Service\operations\infrastructure\gcp\terraform\modules\database\main.tf_

- **"variables.tf" appears in 5 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\operations\infrastructure\gcp\terraform\modules\database\variables.tf, ..\..\TrueVow_Tenant_Application_Service\operations\infrastructure\gcp\terraform\modules\gke\variables.tf, ..\..\TrueVow_Tenant_Application_Service\operations\infrastructure\gcp\terraform\modules\networking\variables.tf...
  > _..\..\TrueVow_Tenant_Application_Service\operations\infrastructure\gcp\terraform\modules\database\variables.tf_

- **"test_simple_bridge.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\tests\legacy\test_simple_bridge.py, ..\..\TrueVow_Tenant_Application_Service\tests\test_simple_bridge.py
  > _..\..\TrueVow_Tenant_Application_Service\tests\legacy\test_simple_bridge.py_

- **"app.js" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_Application_Service\web\draft\app.js, ..\..\TrueVow_Tenant_Application_Service\web\app.js
  > _..\..\TrueVow_Tenant_Application_Service\web\draft\app.js_

### LOW

- **Deep nesting (depth 6): ..\..\TrueVow_Tenant_Application_Service\app\portal\app\api\auth\login**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\portal\app\api\auth\login_

- **Deep nesting (depth 6): ..\..\TrueVow_Tenant_Application_Service\app\portal\app\api\auth\logout**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\portal\app\api\auth\logout_

- **Deep nesting (depth 6): ..\..\TrueVow_Tenant_Application_Service\app\portal\app\api\auth\me**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\portal\app\api\auth\me_

- **Deep nesting (depth 6): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server_

- **Deep nesting (depth 7): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api_

- **Deep nesting (depth 8): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\alembic**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\alembic_

- **Deep nesting (depth 8): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\assets**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\assets_

- **Deep nesting (depth 8): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\db**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\db_

- **Deep nesting (depth 8): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\errors**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\errors_

- **Deep nesting (depth 8): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\mcp_server**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\mcp_server_

- **Deep nesting (depth 8): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\native**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\native_

- **Deep nesting (depth 8): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\routes**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\routes_

- **Deep nesting (depth 8): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\schemas**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\schemas_

- **Deep nesting (depth 8): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\services_

- **Deep nesting (depth 8): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\tasks**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\tasks_

- **Deep nesting (depth 8): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\tests**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\tests_

- **Deep nesting (depth 8): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\utils**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\api\utils_

- **Deep nesting (depth 7): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\config**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\config_

- **Deep nesting (depth 8): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\config\coturn**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\config\coturn_

- **Deep nesting (depth 7): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\deploy**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\deploy_

- **Deep nesting (depth 8): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\deploy\templates**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\deploy\templates_

- **Deep nesting (depth 7): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs_

- **Deep nesting (depth 8): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\api-reference**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\api-reference_

- **Deep nesting (depth 8): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\configurations**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\configurations_

- **Deep nesting (depth 8): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\contribution**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\contribution_

- **Deep nesting (depth 8): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\core-concepts**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\core-concepts_

- **Deep nesting (depth 8): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\deployment**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\deployment_

- **Deep nesting (depth 8): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\developer**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\developer_

- **Deep nesting (depth 8): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\getting-started**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\getting-started_

- **Deep nesting (depth 8): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\images**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\images_

- **Deep nesting (depth 8): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\integrations**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\integrations_

- **Deep nesting (depth 8): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\logo**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\logo_

- **Deep nesting (depth 8): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\sdks**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\sdks_

- **Deep nesting (depth 8): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\voice-agent**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\docs\voice-agent_

- **Deep nesting (depth 7): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\evals**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\evals_

- **Deep nesting (depth 8): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\evals\stt**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\evals\stt_

- **Deep nesting (depth 8): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\evals\visualizer**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\evals\visualizer_

- **Deep nesting (depth 7): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\examples**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\examples_

- **Deep nesting (depth 8): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\examples\python**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\examples\python_

- **Deep nesting (depth 8): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\examples\typescript**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\examples\typescript_

- **Deep nesting (depth 7): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\grafana**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\grafana_

- **Deep nesting (depth 8): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\grafana\alerts**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\grafana\alerts_

- **Deep nesting (depth 8): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\grafana\dashboards**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\grafana\dashboards_

- **Deep nesting (depth 7): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\nginx**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\nginx_

- **Deep nesting (depth 7): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\pipecat**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\pipecat_

- **Deep nesting (depth 7): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\scripts**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\scripts_

- **Deep nesting (depth 8): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\scripts\lib**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\scripts\lib_

- **Deep nesting (depth 7): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\sdk**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\sdk_

- **Deep nesting (depth 8): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\sdk\codegen**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\sdk\codegen_

- **Deep nesting (depth 8): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\sdk\python**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\sdk\python_

- **Deep nesting (depth 8): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\sdk\typescript**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\sdk\typescript_

- **Deep nesting (depth 7): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\ui**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\ui_

- **Deep nesting (depth 8): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\ui\public**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\ui\public_

- **Deep nesting (depth 8): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\ui\scripts**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\ui\scripts_

- **Deep nesting (depth 8): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\ui\src**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\dograh\server\ui\src_

- **Deep nesting (depth 6): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\intake_engine\fsm**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\intake_engine\fsm_

- **Deep nesting (depth 6): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\intake_engine\normalizer**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\intake_engine\normalizer_

- **Deep nesting (depth 6): ..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\intake_engine\workflow**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\app\services\voice\bridges\intake_engine\workflow_

- **Deep nesting (depth 6): ..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\aav**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\aav_

- **Deep nesting (depth 6): ..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\art**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\art_

- **Deep nesting (depth 6): ..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\azc**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\azc_

- **Deep nesting (depth 6): ..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\bat**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\bat_

- **Deep nesting (depth 6): ..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\bnt**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\bnt_

- **Deep nesting (depth 6): ..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\ccs**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\ccs_

- **Deep nesting (depth 6): ..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\cel**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\cel_

- **Deep nesting (depth 6): ..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\cus**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\cus_

- **Deep nesting (depth 6): ..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\dra**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\dra_

- **Deep nesting (depth 6): ..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\esx**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\esx_

- **Deep nesting (depth 6): ..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\gmq**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\gmq_

- **Deep nesting (depth 6): ..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\gmw**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\gmw_

- **Deep nesting (depth 6): ..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\grk**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\grk_

- **Deep nesting (depth 6): ..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\inc**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\inc_

- **Deep nesting (depth 6): ..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\ine**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\ine_

- **Deep nesting (depth 6): ..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\ira**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\ira_

- **Deep nesting (depth 6): ..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\iro**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\iro_

- **Deep nesting (depth 6): ..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\itc**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\itc_

- **Deep nesting (depth 6): ..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\jpx**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\jpx_

- **Deep nesting (depth 6): ..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\map**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\map_

- **Deep nesting (depth 6): ..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\miz**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\miz_

- **Deep nesting (depth 6): ..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\myn**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\myn_

- **Deep nesting (depth 6): ..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\poz**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\poz_

- **Deep nesting (depth 6): ..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\roa**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\roa_

- **Deep nesting (depth 6): ..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\sai**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\sai_

- **Deep nesting (depth 6): ..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\sem**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\sem_

- **Deep nesting (depth 6): ..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\sit**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\sit_

- **Deep nesting (depth 6): ..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\tai**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\tai_

- **Deep nesting (depth 6): ..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\trk**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\trk_

- **Deep nesting (depth 6): ..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\urj**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\urj_

- **Deep nesting (depth 6): ..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\zle**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\zle_

- **Deep nesting (depth 6): ..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\zls**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\zls_

- **Deep nesting (depth 6): ..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\zlw**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\lang\zlw_

- **Deep nesting (depth 6): ..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\voices\!v**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\models\piper\piper\espeak-ng-data\voices\!v_

- **Deep nesting (depth 6): ..\..\TrueVow_Tenant_Application_Service\operations\infrastructure\gcp\terraform\modules\database**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\operations\infrastructure\gcp\terraform\modules\database_

- **Deep nesting (depth 6): ..\..\TrueVow_Tenant_Application_Service\operations\infrastructure\gcp\terraform\modules\gke**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\operations\infrastructure\gcp\terraform\modules\gke_

- **Deep nesting (depth 6): ..\..\TrueVow_Tenant_Application_Service\operations\infrastructure\gcp\terraform\modules\networking**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\operations\infrastructure\gcp\terraform\modules\networking_

- **Deep nesting (depth 6): ..\..\TrueVow_Tenant_Application_Service\operations\infrastructure\gcp\terraform\modules\redis**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Tenant_Application_Service\operations\infrastructure\gcp\terraform\modules\redis_

- **Archive folder found: docs/archive/**
  > Archive folders should be outside the repo or explicitly tagged for deletion review.
  > _C:\Users\yasha\OneDrive\Documents\TrueVow\Cursor\TrueVow_Tenant_Application_Service\docs\archive_



## Related Service
- [[Cross-Service/truevow-tenant-application-service|Service Page]]
