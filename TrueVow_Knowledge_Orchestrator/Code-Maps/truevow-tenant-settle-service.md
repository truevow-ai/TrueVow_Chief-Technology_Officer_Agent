# Code Structure Map — Tenant SETTLE Service

> Auto-generated: 2026-05-29
> Repository: `TrueVow_Tenant_SETTLE-Service`

## File Breakdown

| Extension | Count |
|-----------|-------|
| .py | 206 |
| .md | 117 |
| .json | 26 |
| .ps1 | 17 |
| .sql | 15 |
| .txt | 12 |
| .tsx | 6 |
| (none) | 4 |
| .js | 2 |
| .html | 2 |
| .mako | 1 |
| .css | 1 |
| .sh | 1 |
| .bat | 1 |
| .local | 1 |
| .ini | 1 |
| .yml | 1 |
| .template | 1 |

## Directory Tree

```
```

## Component Graph

```mermaid
graph TD
```

## Issues Found (15)

### MEDIUM

- **Both migrations/ and database/ exist — possible dual ORM setup**
  > One ORM configuration is likely stale. Review and archive the unused one.
  > _C:\Users\yasha\OneDrive\Documents\TrueVow\Cursor\TrueVow_Tenant_SETTLE-Service\database_

- **"override_tracking.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_SETTLE-Service\app\api\v1\endpoints\override_tracking.py, ..\..\TrueVow_Tenant_SETTLE-Service\app\services\override_tracking.py
  > _..\..\TrueVow_Tenant_SETTLE-Service\app\api\v1\endpoints\override_tracking.py_

- **"reports.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_SETTLE-Service\app\api\v1\endpoints\reports.py, ..\..\TrueVow_Tenant_SETTLE-Service\app\models\reports.py
  > _..\..\TrueVow_Tenant_SETTLE-Service\app\api\v1\endpoints\reports.py_

- **"trend_reports.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_SETTLE-Service\app\api\v1\endpoints\trend_reports.py, ..\..\TrueVow_Tenant_SETTLE-Service\app\services\trend_reports.py
  > _..\..\TrueVow_Tenant_SETTLE-Service\app\api\v1\endpoints\trend_reports.py_

- **"verdicts.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_SETTLE-Service\app\api\v1\endpoints\verdicts.py, ..\..\TrueVow_Tenant_SETTLE-Service\app\models\verdicts.py
  > _..\..\TrueVow_Tenant_SETTLE-Service\app\api\v1\endpoints\verdicts.py_

- **"waitlist.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_SETTLE-Service\app\api\v1\endpoints\waitlist.py, ..\..\TrueVow_Tenant_SETTLE-Service\app\models\waitlist.py
  > _..\..\TrueVow_Tenant_SETTLE-Service\app\api\v1\endpoints\waitlist.py_

- **"router.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_SETTLE-Service\app\api\v1\router.py, ..\..\TrueVow_Tenant_SETTLE-Service\DOCKET-Service\app\api\v1\router.py
  > _..\..\TrueVow_Tenant_SETTLE-Service\app\api\v1\router.py_

- **"config.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_SETTLE-Service\app\core\config.py, ..\..\TrueVow_Tenant_SETTLE-Service\DOCKET-Service\app\core\config.py
  > _..\..\TrueVow_Tenant_SETTLE-Service\app\core\config.py_

- **"database.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_SETTLE-Service\app\core\database.py, ..\..\TrueVow_Tenant_SETTLE-Service\DOCKET-Service\app\core\database.py
  > _..\..\TrueVow_Tenant_SETTLE-Service\app\core\database.py_

- **"client.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_SETTLE-Service\app\services\integrations\internal_ops\client.py, ..\..\TrueVow_Tenant_SETTLE-Service\app\services\integrations\platform\client.py
  > _..\..\TrueVow_Tenant_SETTLE-Service\app\services\integrations\internal_ops\client.py_

- **"main.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_SETTLE-Service\app\main.py, ..\..\TrueVow_Tenant_SETTLE-Service\DOCKET-Service\app\main.py
  > _..\..\TrueVow_Tenant_SETTLE-Service\app\main.py_

- **"README.md" appears in 6 locations**
  > Found at: ..\..\TrueVow_Tenant_SETTLE-Service\database\migrations\README.md, ..\..\TrueVow_Tenant_SETTLE-Service\database\schemas\README.md, ..\..\TrueVow_Tenant_SETTLE-Service\DOCKET-Service\README.md...
  > _..\..\TrueVow_Tenant_SETTLE-Service\database\migrations\README.md_

- **"Dockerfile" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_SETTLE-Service\DOCKET-Service\Dockerfile, ..\..\TrueVow_Tenant_SETTLE-Service\Dockerfile
  > _..\..\TrueVow_Tenant_SETTLE-Service\DOCKET-Service\Dockerfile_

- **"requirements.txt" appears in 3 locations**
  > Found at: ..\..\TrueVow_Tenant_SETTLE-Service\DOCKET-Service\requirements.txt, ..\..\TrueVow_Tenant_SETTLE-Service\scripts\data-collection\requirements.txt, ..\..\TrueVow_Tenant_SETTLE-Service\requirements.txt
  > _..\..\TrueVow_Tenant_SETTLE-Service\DOCKET-Service\requirements.txt_

### LOW

- **Archive folder found: docs/archive/**
  > Archive folders should be outside the repo or explicitly tagged for deletion review.
  > _C:\Users\yasha\OneDrive\Documents\TrueVow\Cursor\TrueVow_Tenant_SETTLE-Service\docs\archive_



## Related Service
- [[Cross-Service/truevow-tenant-settle-service|Service Page]]
