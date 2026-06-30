# Code Structure Map — Tenant LEVERAGE Service

> Auto-generated: 2026-05-29
> Repository: `TrueVow_Tenant_LEVERAGE_Service`

## File Breakdown

| Extension | Count |
|-----------|-------|
| .sql | 1946 |
| .md | 128 |
| .py | 125 |
| .html | 58 |
| .json | 57 |
| .ps1 | 19 |
| .js | 15 |
| .css | 6 |
| .tsx | 4 |
| .bak | 2 |
| .ini | 2 |
| .xml | 1 |
| .ts | 1 |
| .mako | 1 |
| .local | 1 |
| .txt | 1 |

## Directory Tree

```
```

## Component Graph

```mermaid
graph TD
```

## Issues Found (10)

### HIGH

- **46 test files flat in tests/ — no subfolder organization**
  > Group by domain: billing/, voice/, draft/, integration/, etc.
  > _..\..\TrueVow_Tenant_LEVERAGE_Service\tests_

### MEDIUM

- **50 .md files at repository root**
  > Move to a subfolder (docs/)
  > _C:\Users\yasha\OneDrive\Documents\TrueVow\Cursor\TrueVow_Tenant_LEVERAGE_Service_

- **"email_validation.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_LEVERAGE_Service\app\api\v1\endpoints\email_validation.py, ..\..\TrueVow_Tenant_LEVERAGE_Service\app\services\email_validation.py
  > _..\..\TrueVow_Tenant_LEVERAGE_Service\app\api\v1\endpoints\email_validation.py_

- **"README.md" appears in 8 locations**
  > Found at: ..\..\TrueVow_Tenant_LEVERAGE_Service\client\browser_extension\README.md, ..\..\TrueVow_Tenant_LEVERAGE_Service\client\desktop_app\README.md, ..\..\TrueVow_Tenant_LEVERAGE_Service\client\word_addin\README.md...
  > _..\..\TrueVow_Tenant_LEVERAGE_Service\client\browser_extension\README.md_

- **"styles.css" appears in 3 locations**
  > Found at: ..\..\TrueVow_Tenant_LEVERAGE_Service\client\browser_extension\styles.css, ..\..\TrueVow_Tenant_LEVERAGE_Service\client\desktop_app\styles.css, ..\..\TrueVow_Tenant_LEVERAGE_Service\web\draft\styles.css
  > _..\..\TrueVow_Tenant_LEVERAGE_Service\client\browser_extension\styles.css_

- **"validation_engine.js" appears in 3 locations**
  > Found at: ..\..\TrueVow_Tenant_LEVERAGE_Service\client\browser_extension\validation_engine.js, ..\..\TrueVow_Tenant_LEVERAGE_Service\client\desktop_app\validation_engine.js, ..\..\TrueVow_Tenant_LEVERAGE_Service\client\word_addin\validation_engine.js
  > _..\..\TrueVow_Tenant_LEVERAGE_Service\client\browser_extension\validation_engine.js_

- **"index.html" appears in 3 locations**
  > Found at: ..\..\TrueVow_Tenant_LEVERAGE_Service\client\desktop_app\index.html, ..\..\TrueVow_Tenant_LEVERAGE_Service\htmlcov\index.html, ..\..\TrueVow_Tenant_LEVERAGE_Service\web\draft\index.html
  > _..\..\TrueVow_Tenant_LEVERAGE_Service\client\desktop_app\index.html_

- **"package.json" appears in 3 locations**
  > Found at: ..\..\TrueVow_Tenant_LEVERAGE_Service\client\desktop_app\package.json, ..\..\TrueVow_Tenant_LEVERAGE_Service\client\word_addin\package.json, ..\..\TrueVow_Tenant_LEVERAGE_Service\package.json
  > _..\..\TrueVow_Tenant_LEVERAGE_Service\client\desktop_app\package.json_

- **"IMPLEMENTATION_PROGRESS.md" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_LEVERAGE_Service\docs\00-main\IMPLEMENTATION_PROGRESS.md, ..\..\TrueVow_Tenant_LEVERAGE_Service\docs\01-main\IMPLEMENTATION_PROGRESS.md
  > _..\..\TrueVow_Tenant_LEVERAGE_Service\docs\00-main\IMPLEMENTATION_PROGRESS.md_

- **"WORKING_CACHE.md" appears in 2 locations**
  > Found at: ..\..\TrueVow_Tenant_LEVERAGE_Service\docs\00-main\WORKING_CACHE.md, ..\..\TrueVow_Tenant_LEVERAGE_Service\docs\01-main\WORKING_CACHE.md
  > _..\..\TrueVow_Tenant_LEVERAGE_Service\docs\00-main\WORKING_CACHE.md_



## Related Service
- [[Cross-Service/truevow-tenant-leverage-service|Service Page]]
