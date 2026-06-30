# Code Structure Map — Financial Management Service

> Auto-generated: 2026-05-29
> Repository: `TrueVow_Financial_Management_Service`

## File Breakdown

| Extension | Count |
|-----------|-------|
| .py | 2717 |
| (none) | 1039 |
| .pyi | 610 |
| .md | 164 |
| .tsx | 106 |
| .txt | 95 |
| .test | 70 |
| .html | 67 |
| .typed | 65 |
| .h | 60 |
| .pyx | 46 |
| .ts | 39 |
| .exe | 37 |
| .pyd | 32 |
| .pxd | 25 |
| .yaml | 23 |
| .http | 21 |
| .rst | 19 |
| .c | 17 |
| .cpp | 15 |
| .hpp | 13 |
| .cc | 10 |
| .js | 9 |
| .mako | 6 |
| .cfg | 6 |
| .json | 5 |
| .ps1 | 5 |
| .pxi | 5 |
| .css | 4 |
| .apache | 4 |
| .bsd | 4 |
| .pump | 4 |
| .bat | 3 |
| .dll | 3 |
| .tab | 3 |
| .local | 2 |
| .sh | 2 |
| .pem | 2 |
| .asm | 2 |
| .obj | 2 |
| .xslt | 2 |
| .ini | 2 |
| .xml | 1 |
| .info | 1 |
| .tsbuildinfo | 1 |
| .cmd | 1 |
| .psf | 1 |
| .xsd | 1 |
| .tmpl | 1 |
| .zi | 1 |
| .apache2 | 1 |
| .mit | 1 |
| .fish | 1 |
| .example | 1 |
| .yml | 1 |

## Directory Tree

```
```

## Component Graph

```mermaid
graph TD
```

## Issues Found (557)

### MEDIUM

- **7 .md files at repository root**
  > Move to a subfolder (docs/)
  > _C:\Users\yasha\OneDrive\Documents\TrueVow\Cursor\TrueVow_Financial_Management_Service_

- **"middleware.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\app\auth\middleware.py, ..\..\TrueVow_Financial_Management_Service\app\core\middleware.py
  > _..\..\TrueVow_Financial_Management_Service\app\auth\middleware.py_

- **"roles.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\app\auth\roles.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\sql\roles.py
  > _..\..\TrueVow_Financial_Management_Service\app\auth\roles.py_

- **"loader.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\app\core\seed\loader.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\yaml\loader.py
  > _..\..\TrueVow_Financial_Management_Service\app\core\seed\loader.py_

- **"config.py" appears in 12 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\app\core\config.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\config.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\flake8\options\config.py...
  > _..\..\TrueVow_Financial_Management_Service\app\core\config.py_

- **"exceptions.py" appears in 26 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\app\core\exceptions.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\_pytest\config\exceptions.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\attr\exceptions.py...
  > _..\..\TrueVow_Financial_Management_Service\app\core\exceptions.py_

- **"logging.py" appears in 5 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\app\core\logging.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\_pytest\logging.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\utils\logging.py...
  > _..\..\TrueVow_Financial_Management_Service\app\core\logging.py_

- **"retry.py" appears in 4 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\app\core\retry.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\utils\retry.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\util\retry.py...
  > _..\..\TrueVow_Financial_Management_Service\app\core\retry.py_

- **"reconciliation_routes.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\app\modules\general_ledger\api\routes\reconciliation_routes.py, ..\..\TrueVow_Financial_Management_Service\app\modules\intercompany\api\routes\reconciliation_routes.py
  > _..\..\TrueVow_Financial_Management_Service\app\modules\general_ledger\api\routes\reconciliation_routes.py_

- **"main.py" appears in 12 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\app\main.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\_pytest\main.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\dotenv\main.py...
  > _..\..\TrueVow_Financial_Management_Service\app\main.py_

- **"README.md" appears in 7 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\docs\00-main\ADRs\README.md, ..\..\TrueVow_Financial_Management_Service\docs\README.md, ..\..\TrueVow_Financial_Management_Service\frontend\__tests__\README.md...
  > _..\..\TrueVow_Financial_Management_Service\docs\00-main\ADRs\README.md_

- **"PRODUCTION_DEPLOYMENT_CHECKLIST.md" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\docs\00-main\PRODUCTION_DEPLOYMENT_CHECKLIST.md, ..\..\TrueVow_Financial_Management_Service\PRODUCTION_DEPLOYMENT_CHECKLIST.md
  > _..\..\TrueVow_Financial_Management_Service\docs\00-main\PRODUCTION_DEPLOYMENT_CHECKLIST.md_

- **"TEST_EXECUTION_REPORT.md" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\docs\00-main\TEST_EXECUTION_REPORT.md, ..\..\TrueVow_Financial_Management_Service\frontend\TEST_EXECUTION_REPORT.md
  > _..\..\TrueVow_Financial_Management_Service\docs\00-main\TEST_EXECUTION_REPORT.md_

- **"page.tsx" appears in 23 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\frontend\app\(dashboard)\ap\vendors\page.tsx, ..\..\TrueVow_Financial_Management_Service\frontend\app\(dashboard)\ar\invoices\page.tsx, ..\..\TrueVow_Financial_Management_Service\frontend\app\(dashboard)\chart-of-accounts\[id]\edit\page.tsx...
  > _..\..\TrueVow_Financial_Management_Service\frontend\app\(dashboard)\ap\vendors\page.tsx_

- **"layout.tsx" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\frontend\app\(dashboard)\layout.tsx, ..\..\TrueVow_Financial_Management_Service\frontend\app\layout.tsx
  > _..\..\TrueVow_Financial_Management_Service\frontend\app\(dashboard)\layout.tsx_

- **"index.html" appears in 18 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\frontend\coverage\lcov-report\components\common\index.html, ..\..\TrueVow_Financial_Management_Service\frontend\coverage\lcov-report\components\layout\index.html, ..\..\TrueVow_Financial_Management_Service\frontend\coverage\lcov-report\components\pages\ar\index.html...
  > _..\..\TrueVow_Financial_Management_Service\frontend\coverage\lcov-report\components\common\index.html_

- **"apiClient.ts.html" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\frontend\coverage\lcov-report\lib\api\apiClient.ts.html, ..\..\TrueVow_Financial_Management_Service\frontend\coverage\lcov-report\lib\apiClient.ts.html
  > _..\..\TrueVow_Financial_Management_Service\frontend\coverage\lcov-report\lib\api\apiClient.ts.html_

- **"apiClient.ts" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\frontend\lib\api\apiClient.ts, ..\..\TrueVow_Financial_Management_Service\frontend\lib\apiClient.ts
  > _..\..\TrueVow_Financial_Management_Service\frontend\lib\api\apiClient.ts_

- **"greenlet.h" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Include\site\python3.13\greenlet\greenlet.h, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\greenlet\greenlet.h
  > _..\..\TrueVow_Financial_Management_Service\venv\Include\site\python3.13\greenlet\greenlet.h_

- **"error.py" appears in 5 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\_pytest\_py\error.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cffi\error.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pyasn1\type\error.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\_pytest\_py\error.py_

- **"util.py" appears in 16 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\_pytest\assertion\util.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\testing\util.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\ecdsa\util.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\_pytest\assertion\util.py_

- **"compat.py" appears in 14 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\_pytest\config\compat.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\_pytest\compat.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\util\compat.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\_pytest\config\compat.py_

- **"expression.py" appears in 4 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\_pytest\mark\expression.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypyc\irbuild\expression.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\dialects\mysql\expression.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\_pytest\mark\expression.py_

- **"structures.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\_pytest\mark\structures.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\requests\structures.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\requests\structures.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\_pytest\mark\structures.py_

- **"_version.py" appears in 13 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\_pytest\_version.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\asyncpg\_version.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\dateutil\_version.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\_pytest\_version.py_

- **"fixtures.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\_pytest\fixtures.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\testing\fixtures.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mako\testing\fixtures.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\_pytest\fixtures.py_

- **"nodes.py" appears in 4 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\_pytest\nodes.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\black\nodes.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\nodes.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\_pytest\nodes.py_

- **"py.typed" appears in 65 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\_pytest\py.typed, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohappyeyeballs\py.typed, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohttp\py.typed...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\_pytest\py.typed_

- **"python.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\_pytest\python.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\pygments\lexers\python.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\_pytest\python.py_

- **"scope.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\_pytest\scope.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\scope.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\rich\scope.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\_pytest\scope.py_

- **"warnings.py" appears in 4 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\_pytest\warnings.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\testing\warnings.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\warnings.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\_pytest\warnings.py_

- **"impl.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohappyeyeballs\impl.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\ddl\impl.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\pool\impl.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohappyeyeballs\impl.py_

- **"types.py" appears in 15 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohappyeyeballs\types.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\asyncpg\pgproto\types.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\asyncpg\types.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohappyeyeballs\types.py_

- **"utils.py" appears in 28 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohappyeyeballs\utils.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\asyncpg\utils.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\charset_normalizer\utils.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohappyeyeballs\utils.py_

- **"INSTALLER" appears in 75 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohappyeyeballs-2.6.1.dist-info\INSTALLER, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohttp-3.13.3.dist-info\INSTALLER, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiosignal-1.4.0.dist-info\INSTALLER...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohappyeyeballs-2.6.1.dist-info\INSTALLER_

- **"LICENSE" appears in 88 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohappyeyeballs-2.6.1.dist-info\LICENSE, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohttp-3.13.3.dist-info\licenses\vendor\llhttp\LICENSE, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiosignal-1.4.0.dist-info\licenses\LICENSE...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohappyeyeballs-2.6.1.dist-info\LICENSE_

- **"METADATA" appears in 75 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohappyeyeballs-2.6.1.dist-info\METADATA, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohttp-3.13.3.dist-info\METADATA, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiosignal-1.4.0.dist-info\METADATA...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohappyeyeballs-2.6.1.dist-info\METADATA_

- **"RECORD" appears in 75 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohappyeyeballs-2.6.1.dist-info\RECORD, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohttp-3.13.3.dist-info\RECORD, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiosignal-1.4.0.dist-info\RECORD...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohappyeyeballs-2.6.1.dist-info\RECORD_

- **"WHEEL" appears in 75 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohappyeyeballs-2.6.1.dist-info\WHEEL, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohttp-3.13.3.dist-info\WHEEL, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiosignal-1.4.0.dist-info\WHEEL...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohappyeyeballs-2.6.1.dist-info\WHEEL_

- **"helpers.py" appears in 5 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohttp\_websocket\helpers.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohttp\helpers.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiosqlite\tests\helpers.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohttp\_websocket\helpers.py_

- **"models.py" appears in 7 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohttp\_websocket\models.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\charset_normalizer\models.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\fastapi\dependencies\models.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohttp\_websocket\models.py_

- **"reader.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohttp\_websocket\reader.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\yaml\reader.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohttp\_websocket\reader.py_

- **"abc.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohttp\abc.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\rich\abc.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohttp\abc.py_

- **"client.py" appears in 6 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohttp\client.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\dmypy\client.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\websockets\asyncio\client.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohttp\client.py_

- **"http.py" appears in 4 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohttp\http.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\fastapi\security\http.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\websockets\legacy\http.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohttp\http.py_

- **"log.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohttp\log.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\log.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohttp\log.py_

- **"multipart.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohttp\multipart.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\multipart\multipart.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohttp\multipart.py_

- **"pytest_plugin.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohttp\pytest_plugin.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\anyio\pytest_plugin.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohttp\pytest_plugin.py_

- **"resolver.py" appears in 4 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohttp\resolver.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\resolution\legacy\resolver.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\resolution\resolvelib\resolver.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohttp\resolver.py_

- **"streams.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohttp\streams.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\websockets\streams.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohttp\streams.py_

- **"test_utils.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohttp\test_utils.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\passlib\tests\test_utils.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohttp\test_utils.py_

- **"LICENSE.txt" appears in 19 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohttp-3.13.3.dist-info\licenses\LICENSE.txt, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\click-8.3.1.dist-info\licenses\LICENSE.txt, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\colorama-0.4.6.dist-info\licenses\LICENSE.txt...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohttp-3.13.3.dist-info\licenses\LICENSE.txt_

- **"REQUESTED" appears in 28 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohttp-3.13.3.dist-info\REQUESTED, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiosqlite-0.22.1.dist-info\REQUESTED, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic-1.12.1.dist-info\REQUESTED...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohttp-3.13.3.dist-info\REQUESTED_

- **"top_level.txt" appears in 46 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohttp-3.13.3.dist-info\top_level.txt, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiosignal-1.4.0.dist-info\top_level.txt, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic-1.12.1.dist-info\top_level.txt...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohttp-3.13.3.dist-info\top_level.txt_

- **"__main__.py" appears in 26 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiosqlite\tests\__main__.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\__main__.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\black\__main__.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiosqlite\tests\__main__.py_

- **"__version__.py" appears in 4 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiosqlite\__version__.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpx\__version__.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\requests\__version__.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiosqlite\__version__.py_

- **"context.py" appears in 5 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiosqlite\context.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\context.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypyc\irbuild\context.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiosqlite\context.py_

- **"core.py" appears in 7 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiosqlite\core.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\certifi\core.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\click\core.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiosqlite\core.py_

- **"cursor.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiosqlite\cursor.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\asyncpg\cursor.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\engine\cursor.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiosqlite\cursor.py_

- **"api.py" appears in 11 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\autogenerate\api.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cffi\api.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\charset_normalizer\api.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\autogenerate\api.py_

- **"base.py" appears in 36 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\ddl\base.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\operations\base.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\script\base.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\ddl\base.py_

- **"mssql.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\ddl\mssql.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\passlib\handlers\mssql.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\ddl\mssql.py_

- **"mysql.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\ddl\mysql.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\passlib\handlers\mysql.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\ddl\mysql.py_

- **"oracle.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\ddl\oracle.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\passlib\handlers\oracle.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\ddl\oracle.py_

- **"ops.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\operations\ops.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypyc\ir\ops.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\operations\ops.py_

- **"environment.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\runtime\environment.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\environment.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\runtime\environment.py_

- **"migration.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\runtime\migration.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\migration.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\runtime\migration.py_

- **"alembic.ini.mako" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\templates\async\alembic.ini.mako, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\templates\generic\alembic.ini.mako, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\templates\multidb\alembic.ini.mako
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\templates\async\alembic.ini.mako_

- **"env.py" appears in 5 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\templates\async\env.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\templates\generic\env.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\templates\multidb\env.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\templates\async\env.py_

- **"README" appears in 4 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\templates\async\README, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\templates\generic\README, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\templates\multidb\README...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\templates\async\README_

- **"script.py.mako" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\templates\async\script.py.mako, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\templates\generic\script.py.mako, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\templates\multidb\script.py.mako
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\templates\async\script.py.mako_

- **"bootstrap.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\testing\plugin\bootstrap.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\testing\plugin\bootstrap.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\testing\plugin\bootstrap.py_

- **"assertions.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\testing\assertions.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mako\testing\assertions.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\testing\assertions.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\testing\assertions.py_

- **"requirements.py" appears in 5 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\testing\requirements.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\packaging\requirements.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\resolution\resolvelib\requirements.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\testing\requirements.py_

- **"exc.py" appears in 6 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\util\exc.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\itsdangerous\exc.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\passlib\exc.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\util\exc.py_

- **"langhelpers.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\util\langhelpers.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\util\langhelpers.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\util\langhelpers.py_

- **"context.pyi" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\context.pyi, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\multiprocessing\context.pyi
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\context.pyi_

- **"entry_points.txt" appears in 20 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic-1.12.1.dist-info\entry_points.txt, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\anyio-3.7.1.dist-info\entry_points.txt, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\black-23.11.0.dist-info\entry_points.txt...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic-1.12.1.dist-info\entry_points.txt_

- **"_compat.py" appears in 10 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\anyio\_core\_compat.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\attr\_compat.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\click\_compat.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\anyio\_core\_compat.py_

- **"_exceptions.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\anyio\_core\_exceptions.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpcore\_exceptions.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpx\_exceptions.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\anyio\_core\_exceptions.py_

- **"_resources.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\anyio\_core\_resources.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\anyio\abc\_resources.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\anyio\_core\_resources.py_

- **"_sockets.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\anyio\_core\_sockets.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\anyio\abc\_sockets.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\anyio\_core\_sockets.py_

- **"_streams.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\anyio\_core\_streams.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\anyio\abc\_streams.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\anyio\_core\_streams.py_

- **"_subprocesses.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\anyio\_core\_subprocesses.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\anyio\abc\_subprocesses.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\anyio\_core\_subprocesses.py_

- **"_synchronization.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\anyio\_core\_synchronization.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpcore\_synchronization.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\anyio\_core\_synchronization.py_

- **"_tasks.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\anyio\_core\_tasks.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\anyio\abc\_tasks.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\anyio\_core\_tasks.py_

- **"_testing.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\anyio\_core\_testing.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\anyio\abc\_testing.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\anyio\_core\_testing.py_

- **"text.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\anyio\streams\text.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\rich\text.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\anyio\streams\text.py_

- **"_base.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\asyncpg\exceptions\_base.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pathspec\_backends\hyperscan\_base.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pathspec\_backends\re2\_base.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\asyncpg\exceptions\_base.py_

- **"uuid.pyx" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\asyncpg\pgproto\codecs\uuid.pyx, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\asyncpg\pgproto\uuid.pyx
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\asyncpg\pgproto\codecs\uuid.pyx_

- **"consts.pxi" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\asyncpg\pgproto\consts.pxi, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\asyncpg\protocol\consts.pxi
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\asyncpg\pgproto\consts.pxi_

- **"cpythonx.pxd" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\asyncpg\pgproto\cpythonx.pxd, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\asyncpg\protocol\cpythonx.pxd
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\asyncpg\pgproto\cpythonx.pxd_

- **"pgproto.pyx" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\asyncpg\pgproto\pgproto.pyx, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\asyncpg\protocol\codecs\pgproto.pyx
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\asyncpg\pgproto\pgproto.pyx_

- **"connection.py" appears in 12 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\asyncpg\connection.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpcore\_async\connection.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpcore\_sync\connection.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\asyncpg\connection.py_

- **"introspection.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\asyncpg\introspection.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\typing_inspection\introspection.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\asyncpg\introspection.py_

- **"pool.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\asyncpg\pool.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\psycopg2\pool.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\asyncpg\pool.py_

- **"_config.py" appears in 4 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\attr\_config.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpx\_config.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mako\testing\_config.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\attr\_config.py_

- **"converters.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\attr\converters.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\attrs\converters.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\attr\converters.py_

- **"exceptions.pyi" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\attr\exceptions.pyi, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\bindings\_rust\exceptions.pyi, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\asyncio\exceptions.pyi
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\attr\exceptions.pyi_

- **"filters.py" appears in 4 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\attr\filters.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\attrs\filters.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mako\filters.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\attr\filters.py_

- **"setters.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\attr\setters.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\attrs\setters.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\attr\setters.py_

- **"validators.py" appears in 4 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\attr\validators.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\attrs\validators.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\v1\validators.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\attr\validators.py_

- **"cache.py" appears in 6 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\black\cache.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mako\cache.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\commands\cache.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\black\cache.py_

- **"concurrency.py" appears in 4 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\black\concurrency.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\fastapi\concurrency.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\util\concurrency.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\black\concurrency.py_

- **"debug.py" appears in 4 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\black\debug.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\flake8\main\debug.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\commands\debug.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\black\debug.py_

- **"ranges.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\black\ranges.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\dialects\postgresql\ranges.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\black\ranges.py_

- **"report.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\black\report.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\report.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\black\report.py_

- **"driver.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\blib2to3\pgen2\driver.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypyc\test-data\driver\driver.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\blib2to3\pgen2\driver.py_

- **"literals.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\blib2to3\pgen2\literals.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\literals.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypyc\codegen\literals.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\blib2to3\pgen2\literals.py_

- **"parse.py" appears in 5 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\blib2to3\pgen2\parse.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\parse.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\deprecated\parse.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\blib2to3\pgen2\parse.py_

- **"token.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\blib2to3\pgen2\token.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\pygments\token.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\blib2to3\pgen2\token.py_

- **"cacert.pem" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\certifi\cacert.pem, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\certifi\cacert.pem
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\certifi\cacert.pem_

- **"lock.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cffi\lock.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\commands\lock.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cffi\lock.py_

- **"legacy.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\charset_normalizer\legacy.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\flake8\api\legacy.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\event\legacy.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\charset_normalizer\legacy.py_

- **"version.py" appears in 12 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\charset_normalizer\version.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\dotenv\version.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\version.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\charset_normalizer\version.py_

- **"_utils.py" appears in 6 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\click\_utils.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpcore\_utils.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpx\_utils.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\click\_utils.py_

- **"parser.py" appears in 4 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\click\parser.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\dotenv\parser.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\cli\parser.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\click\parser.py_

- **"ansi.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\colorama\ansi.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\rich\ansi.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\colorama\ansi.py_

- **"win32.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\colorama\win32.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\passlib\win32.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\colorama\win32.py_

- **"asn1.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\asn1\asn1.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\rsa\asn1.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\asn1\asn1.py_

- **"backend.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\backends\openssl\backend.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pathspec\backend.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\backends\openssl\backend.py_

- **"hmac.pyi" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\bindings\_rust\openssl\hmac.pyi, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\hmac.pyi
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\bindings\_rust\openssl\hmac.pyi_

- **"algorithms.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\decrepit\ciphers\algorithms.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\primitives\ciphers\algorithms.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\decrepit\ciphers\algorithms.py_

- **"padding.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\primitives\asymmetric\padding.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\primitives\padding.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\rich\padding.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\primitives\asymmetric\padding.py_

- **"argon2.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\primitives\kdf\argon2.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\passlib\handlers\argon2.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\primitives\kdf\argon2.py_

- **"pbkdf2.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\primitives\kdf\pbkdf2.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\passlib\handlers\pbkdf2.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\passlib\utils\pbkdf2.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\primitives\kdf\pbkdf2.py_

- **"scrypt.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\primitives\kdf\scrypt.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\passlib\handlers\scrypt.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\primitives\kdf\scrypt.py_

- **"ssh.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\primitives\serialization\ssh.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\ecdsa\ssh.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\primitives\serialization\ssh.py_

- **"totp.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\primitives\twofactor\totp.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\passlib\totp.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\primitives\twofactor\totp.py_

- **"hashes.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\primitives\hashes.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\utils\hashes.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\primitives\hashes.py_

- **"extensions.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\x509\extensions.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\psycopg2\extensions.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\ext\declarative\extensions.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\x509\extensions.py_

- **"LICENSE.APACHE" appears in 4 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography-46.0.4.dist-info\licenses\LICENSE.APACHE, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\packaging-26.0.dist-info\licenses\LICENSE.APACHE, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\packaging\LICENSE.APACHE...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography-46.0.4.dist-info\licenses\LICENSE.APACHE_

- **"LICENSE.BSD" appears in 4 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography-46.0.4.dist-info\licenses\LICENSE.BSD, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\packaging-26.0.dist-info\licenses\LICENSE.BSD, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\packaging\LICENSE.BSD...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography-46.0.4.dist-info\licenses\LICENSE.BSD_

- **"_parser.py" appears in 4 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\dateutil\parser\_parser.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\packaging\_parser.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\packaging\_parser.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\dateutil\parser\_parser.py_

- **"_common.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\dateutil\tz\_common.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\dateutil\_common.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\dateutil\tz\_common.py_

- **"tz.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\dateutil\tz\tz.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\psycopg2\tz.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\dateutil\tz\tz.py_

- **"cli.py" appears in 6 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\dotenv\cli.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\flake8\main\cli.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic_settings\sources\providers\cli.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\dotenv\cli.py_

- **"errors.py" appears in 10 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\ecdsa\errors.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httptools\parser\errors.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\errors.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\ecdsa\errors.py_

- **"cors.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\fastapi\middleware\cors.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\starlette\middleware\cors.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\fastapi\middleware\cors.py_

- **"gzip.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\fastapi\middleware\gzip.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\starlette\middleware\gzip.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\fastapi\middleware\gzip.py_

- **"httpsredirect.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\fastapi\middleware\httpsredirect.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\starlette\middleware\httpsredirect.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\fastapi\middleware\httpsredirect.py_

- **"trustedhost.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\fastapi\middleware\trustedhost.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\starlette\middleware\trustedhost.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\fastapi\middleware\trustedhost.py_

- **"wsgi.py" appears in 4 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\fastapi\middleware\wsgi.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpx\_transports\wsgi.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\starlette\middleware\wsgi.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\fastapi\middleware\wsgi.py_

- **"constants.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\fastapi\openapi\constants.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\jose\constants.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\fastapi\openapi\constants.py_

- **"applications.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\fastapi\applications.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\starlette\applications.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\fastapi\applications.py_

- **"background.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\fastapi\background.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\starlette\background.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\fastapi\background.py_

- **"datastructures.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\fastapi\datastructures.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\starlette\datastructures.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\websockets\datastructures.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\fastapi\datastructures.py_

- **"requests.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\fastapi\requests.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\starlette\requests.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\fastapi\requests.py_

- **"responses.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\fastapi\responses.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\starlette\responses.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\fastapi\responses.py_

- **"routing.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\fastapi\routing.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\starlette\routing.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\fastapi\routing.py_

- **"staticfiles.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\fastapi\staticfiles.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\starlette\staticfiles.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\fastapi\staticfiles.py_

- **"templating.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\fastapi\templating.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\starlette\templating.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\fastapi\templating.py_

- **"testclient.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\fastapi\testclient.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\starlette\testclient.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\fastapi\testclient.py_

- **"websockets.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\fastapi\websockets.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\starlette\websockets.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\fastapi\websockets.py_

- **"default.py" appears in 4 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\flake8\formatting\default.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpx\_transports\default.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\plugins\default.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\flake8\formatting\default.py_

- **"options.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\flake8\main\options.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\options.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypyc\options.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\flake8\main\options.py_

- **"pycodestyle.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\flake8\plugins\pycodestyle.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pycodestyle.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\flake8\plugins\pycodestyle.py_

- **"pyflakes.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\flake8\plugins\pyflakes.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pyflakes\scripts\pyflakes.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\flake8\plugins\pyflakes.py_

- **"reporter.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\flake8\plugins\reporter.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\resolution\resolvelib\reporter.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pyflakes\reporter.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\flake8\plugins\reporter.py_

- **"checker.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\flake8\checker.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\checker.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pyflakes\checker.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\flake8\checker.py_

- **"defaults.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\flake8\defaults.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\defaults.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\flake8\defaults.py_

- **"connection_pool.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpcore\_async\connection_pool.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpcore\_sync\connection_pool.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpcore\_async\connection_pool.py_

- **"http_proxy.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpcore\_async\http_proxy.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpcore\_sync\http_proxy.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpcore\_async\http_proxy.py_

- **"http11.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpcore\_async\http11.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpcore\_sync\http11.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\websockets\http11.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpcore\_async\http11.py_

- **"http2.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpcore\_async\http2.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpcore\_sync\http2.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpcore\_async\http2.py_

- **"interfaces.py" appears in 4 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpcore\_async\interfaces.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpcore\_sync\interfaces.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\engine\interfaces.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpcore\_async\interfaces.py_

- **"socks_proxy.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpcore\_async\socks_proxy.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpcore\_sync\socks_proxy.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpcore\_async\socks_proxy.py_

- **"auto.py" appears in 4 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpcore\_backends\auto.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\uvicorn\loops\auto.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\uvicorn\protocols\http\auto.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpcore\_backends\auto.py_

- **"mock.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpcore\_backends\mock.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpx\_transports\mock.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\engine\mock.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpcore\_backends\mock.py_

- **"sync.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpcore\_backends\sync.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\orm\sync.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpcore\_backends\sync.py_

- **"_api.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpcore\_api.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpx\_api.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\truststore\_api.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpcore\_api.py_

- **"_models.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpcore\_models.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpx\_models.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpcore\_models.py_

- **"LICENSE.md" appears in 7 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpcore-1.0.9.dist-info\licenses\LICENSE.md, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpx-0.25.2.dist-info\licenses\LICENSE.md, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\idna-3.11.dist-info\licenses\LICENSE.md...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpcore-1.0.9.dist-info\licenses\LICENSE.md_

- **"parser.pyi" appears in 4 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httptools\parser\parser.pyi, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\email\parser.pyi, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\html\parser.pyi...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httptools\parser\parser.pyi_

- **"protocol.py" appears in 4 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httptools\parser\protocol.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\rich\protocol.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\websockets\legacy\protocol.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httptools\parser\protocol.py_

- **"_types.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpx\_types.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\tomli\_types.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\uvicorn\_types.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\httpx\_types.py_

- **"codec.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\idna\codec.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\idna\codec.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\idna\codec.py_

- **"idnadata.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\idna\idnadata.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\idna\idnadata.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\idna\idnadata.py_

- **"intranges.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\idna\intranges.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\idna\intranges.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\idna\intranges.py_

- **"package_data.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\idna\package_data.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\idna\package_data.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\idna\package_data.py_

- **"uts46data.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\idna\uts46data.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\idna\uts46data.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\idna\uts46data.py_

- **"_parse.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\iniconfig\_parse.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\yarl\_parse.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\iniconfig\_parse.py_

- **"_json.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\itsdangerous\_json.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\metadata\_json.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\psycopg2\_json.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\itsdangerous\_json.py_

- **"serializer.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\itsdangerous\serializer.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\ext\serializer.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\yaml\serializer.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\itsdangerous\serializer.py_

- **"exclusions.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mako\testing\exclusions.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\testing\exclusions.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mako\testing\exclusions.py_

- **"lexer.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mako\lexer.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\pygments\lexer.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mako\lexer.py_

- **"lookup.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mako\lookup.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\lookup.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mako\lookup.py_

- **"_speedups.cp313-win_amd64.pyd" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\markupsafe\_speedups.cp313-win_amd64.pyd, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\simplejson\_speedups.cp313-win_amd64.pyd
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\markupsafe\_speedups.cp313-win_amd64.pyd_

- **"common.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\plugins\common.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypyc\common.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\rsa\common.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\plugins\common.py_

- **"dataclasses.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\plugins\dataclasses.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\v1\dataclasses.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\dataclasses.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\plugins\dataclasses.py_

- **"testutil.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\test\testutil.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypyc\test\testutil.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypyc\test-data\fixtures\testutil.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\test\testutil.py_

- **"visitors.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\test\visitors.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\sql\visitors.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\test\visitors.py_

- **"constants.pyi" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\asyncio\constants.pyi, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\tkinter\constants.pyi
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\asyncio\constants.pyi_

- **"log.pyi" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\asyncio\log.pyi, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\distutils\log.pyi
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\asyncio\log.pyi_

- **"queues.pyi" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\asyncio\queues.pyi, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\multiprocessing\queues.pyi
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\asyncio\queues.pyi_

- **"subprocess.pyi" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\asyncio\subprocess.pyi, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\subprocess.pyi
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\asyncio\subprocess.pyi_

- **"abc.pyi" appears in 4 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\collections\abc.pyi, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\importlib\resources\abc.pyi, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\importlib\abc.pyi...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\collections\abc.pyi_

- **"process.pyi" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\concurrent\futures\process.pyi, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\multiprocessing\process.pyi
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\concurrent\futures\process.pyi_

- **"util.pyi" appears in 6 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\ctypes\util.pyi, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\distutils\util.pyi, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\importlib\util.pyi...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\ctypes\util.pyi_

- **"config.pyi" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\distutils\command\config.pyi, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\distutils\config.pyi, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\logging\config.pyi
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\distutils\command\config.pyi_

- **"cmd.pyi" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\distutils\cmd.pyi, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\cmd.pyi
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\distutils\cmd.pyi_

- **"errors.pyi" appears in 4 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\distutils\errors.pyi, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\email\errors.pyi, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\pyexpat\errors.pyi...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\distutils\errors.pyi_

- **"spawn.pyi" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\distutils\spawn.pyi, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\multiprocessing\spawn.pyi
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\distutils\spawn.pyi_

- **"sysconfig.pyi" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\distutils\sysconfig.pyi, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\sysconfig.pyi
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\distutils\sysconfig.pyi_

- **"message.pyi" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\email\mime\message.pyi, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\email\message.pyi
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\email\mime\message.pyi_

- **"text.pyi" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\email\mime\text.pyi, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\msilib\text.pyi
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\email\mime\text.pyi_

- **"client.pyi" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\http\client.pyi, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\xmlrpc\client.pyi
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\http\client.pyi_

- **"server.pyi" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\http\server.pyi, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\xmlrpc\server.pyi
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\http\server.pyi_

- **"parse.pyi" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\lib2to3\pgen2\parse.pyi, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\urllib\parse.pyi
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\lib2to3\pgen2\parse.pyi_

- **"token.pyi" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\lib2to3\pgen2\token.pyi, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\token.pyi
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\lib2to3\pgen2\token.pyi_

- **"tokenize.pyi" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\lib2to3\pgen2\tokenize.pyi, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\tokenize.pyi
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\lib2to3\pgen2\tokenize.pyi_

- **"main.pyi" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\lib2to3\main.pyi, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\unittest\main.pyi
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\lib2to3\main.pyi_

- **"handlers.pyi" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\logging\handlers.pyi, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\wsgiref\handlers.pyi
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\logging\handlers.pyi_

- **"connection.pyi" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\multiprocessing\dummy\connection.pyi, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\multiprocessing\connection.pyi
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\multiprocessing\dummy\connection.pyi_

- **"model.pyi" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\pyexpat\model.pyi, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\xml\parsers\expat\model.pyi
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\pyexpat\model.pyi_

- **"types.pyi" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\wsgiref\types.pyi, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\types.pyi
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\wsgiref\types.pyi_

- **"build.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\build.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypyc\build.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\build.py_

- **"constant_fold.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\constant_fold.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypyc\irbuild\constant_fold.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\constant_fold.py_

- **"errorcodes.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\errorcodes.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\psycopg2\errorcodes.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\errorcodes.py_

- **"git.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\git.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\vcs\git.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\git.py_

- **"infer.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\infer.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\ext\mypy\infer.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\infer.py_

- **"messages.py" appears in 4 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\messages.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pyflakes\messages.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\websockets\asyncio\messages.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\messages.py_

- **"operators.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\operators.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\dialects\postgresql\operators.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\sql\operators.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\operators.py_

- **"plugin.py" appears in 4 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\plugin.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\pygments\plugin.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytest_asyncio\plugin.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\plugin.py_

- **"state.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\state.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\orm\state.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\state.py_

- **"visitor.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\visitor.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypyc\irbuild\visitor.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\visitor.py_

- **"Makefile" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypyc\doc\Makefile, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypyc\external\googletest\make\Makefile
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypyc\doc\Makefile_

- **"gtest-port.h" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypyc\external\googletest\include\gtest\internal\custom\gtest-port.h, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypyc\external\googletest\include\gtest\internal\gtest-port.h
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypyc\external\googletest\include\gtest\internal\custom\gtest-port.h_

- **"gtest-printers.h" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypyc\external\googletest\include\gtest\internal\custom\gtest-printers.h, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypyc\external\googletest\include\gtest\gtest-printers.h
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypyc\external\googletest\include\gtest\internal\custom\gtest-printers.h_

- **"gtest.h" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypyc\external\googletest\include\gtest\internal\custom\gtest.h, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypyc\external\googletest\include\gtest\gtest.h
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypyc\external\googletest\include\gtest\internal\custom\gtest.h_

- **"mapper.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypyc\irbuild\mapper.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\orm\mapper.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypyc\irbuild\mapper.py_

- **"prepare.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypyc\irbuild\prepare.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\operations\prepare.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypyc\irbuild\prepare.py_

- **"registry.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypyc\primitives\registry.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\passlib\registry.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\event\registry.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypyc\primitives\registry.py_

- **"_spdx.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\packaging\licenses\_spdx.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\packaging\licenses\_spdx.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\packaging\licenses\_spdx.py_

- **"_elffile.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\packaging\_elffile.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\packaging\_elffile.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\packaging\_elffile.py_

- **"_manylinux.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\packaging\_manylinux.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\packaging\_manylinux.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\packaging\_manylinux.py_

- **"_musllinux.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\packaging\_musllinux.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\packaging\_musllinux.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\packaging\_musllinux.py_

- **"_structures.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\packaging\_structures.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\packaging\_structures.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\packaging\_structures.py_

- **"_tokenizer.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\packaging\_tokenizer.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\packaging\_tokenizer.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\packaging\_tokenizer.py_

- **"markers.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\packaging\markers.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\packaging\markers.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\packaging\markers.py_

- **"metadata.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\packaging\metadata.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\operations\build\metadata.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\packaging\metadata.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\packaging\metadata.py_

- **"pylock.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\packaging\pylock.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\utils\pylock.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\packaging\pylock.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\packaging\pylock.py_

- **"specifiers.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\packaging\specifiers.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\packaging\specifiers.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\packaging\specifiers.py_

- **"tags.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\packaging\tags.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\packaging\tags.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\packaging\tags.py_

- **"_gen_files.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\passlib\crypto\_blowfish\_gen_files.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\passlib\crypto\scrypt\_gen_files.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\passlib\crypto\_blowfish\_gen_files.py_

- **"des.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\passlib\crypto\des.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\passlib\utils\des.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\passlib\crypto\des.py_

- **"misc.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\passlib\handlers\misc.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\utils\misc.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\passlib\handlers\misc.py_

- **"windows.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\passlib\handlers\windows.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\platformdirs\windows.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\platformdirs\windows.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\passlib\handlers\windows.py_

- **"hash.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\passlib\hash.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\commands\hash.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\passlib\hash.py_

- **"zip-safe" appears in 4 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\passlib-1.7.4.dist-info\zip-safe, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pyasn1-0.6.2.dist-info\zip-safe, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\python_dateutil-2.8.2.dist-info\zip-safe...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\passlib-1.7.4.dist-info\zip-safe_

- **"gitignore.py" appears in 4 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pathspec\_backends\hyperscan\gitignore.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pathspec\_backends\re2\gitignore.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pathspec\_backends\simple\gitignore.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pathspec\_backends\hyperscan\gitignore.py_

- **"pathspec.py" appears in 4 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pathspec\_backends\hyperscan\pathspec.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pathspec\_backends\re2\pathspec.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pathspec\_backends\simple\pathspec.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pathspec\_backends\hyperscan\pathspec.py_

- **"_typing.py" appears in 4 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pathspec\_typing.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\dialects\_typing.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\orm\_typing.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pathspec\_typing.py_

- **"status_codes.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\cli\status_codes.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\requests\status_codes.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\requests\status_codes.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\cli\status_codes.py_

- **"check.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\commands\check.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\operations\check.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\commands\check.py_

- **"configuration.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\commands\configuration.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\configuration.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\commands\configuration.py_

- **"download.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\commands\download.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\network\download.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\commands\download.py_

- **"freeze.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\commands\freeze.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\operations\freeze.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\commands\freeze.py_

- **"help.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\commands\help.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\requests\help.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\requests\help.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\commands\help.py_

- **"index.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\commands\index.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\models\index.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\commands\index.py_

- **"wheel.py" appears in 6 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\commands\wheel.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\distributions\wheel.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\models\wheel.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\commands\wheel.py_

- **"auth.py" appears in 5 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\network\auth.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\requests\auth.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\requests\auth.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\network\auth.py_

- **"session.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\network\session.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\ext\asyncio\session.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\orm\session.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\network\session.py_

- **"pyproject.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\pyproject.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic_settings\sources\providers\pyproject.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\pyproject.py_

- **"COPYING" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\msgpack\COPYING, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip-26.0.1.dist-info\licenses\src\pip\_vendor\msgpack\COPYING
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\msgpack\COPYING_

- **"ext.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\msgpack\ext.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\dialects\postgresql\ext.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\msgpack\ext.py_

- **"android.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\platformdirs\android.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\platformdirs\android.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\platformdirs\android.py_

- **"macos.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\platformdirs\macos.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\platformdirs\macos.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\platformdirs\macos.py_

- **"unix.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\platformdirs\unix.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\platformdirs\unix.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\platformdirs\unix.py_

- **"_mapping.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\pygments\formatters\_mapping.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\pygments\lexers\_mapping.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\pygments\styles\_mapping.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\pygments\formatters\_mapping.py_

- **"console.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\pygments\console.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\rich\console.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\pygments\console.py_

- **"scanner.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\pygments\scanner.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\simplejson\scanner.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\yaml\scanner.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\pygments\scanner.py_

- **"style.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\pygments\style.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\rich\style.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\pygments\style.py_

- **"_impl.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\pyproject_hooks\_impl.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sniffio\_impl.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\pyproject_hooks\_impl.py_

- **"_internal_utils.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\requests\_internal_utils.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\requests\_internal_utils.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\requests\_internal_utils.py_

- **"adapters.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\requests\adapters.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\requests\adapters.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\requests\adapters.py_

- **"certs.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\requests\certs.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\requests\certs.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\requests\certs.py_

- **"cookies.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\requests\cookies.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\requests\cookies.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\requests\cookies.py_

- **"hooks.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\requests\hooks.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\requests\hooks.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\requests\hooks.py_

- **"packages.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\requests\packages.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\requests\packages.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\requests\packages.py_

- **"sessions.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\requests\sessions.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\requests\sessions.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\starlette\middleware\sessions.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\requests\sessions.py_

- **"_windows.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\rich\_windows.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\truststore\_windows.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\rich\_windows.py_

- **"color.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\rich\color.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\v1\color.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\color.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\rich\color.py_

- **"json.py" appears in 9 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\rich\json.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\deprecated\json.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\v1\json.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\rich\json.py_

- **"status.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\rich\status.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\starlette\status.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\rich\status.py_

- **"pyopenssl.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\contrib\pyopenssl.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\urllib3\contrib\pyopenssl.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\contrib\pyopenssl.py_

- **"socks.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\contrib\socks.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\urllib3\contrib\socks.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\contrib\socks.py_

- **"six.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\packages\six.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\six.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\packages\six.py_

- **"proxy.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\util\proxy.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\urllib3\util\proxy.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\websockets\proxy.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\util\proxy.py_

- **"queue.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\util\queue.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\util\queue.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\util\queue.py_

- **"request.py" appears in 4 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\util\request.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\request.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\urllib3\contrib\emscripten\request.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\util\request.py_

- **"response.py" appears in 5 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\util\response.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\response.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\urllib3\contrib\emscripten\response.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\util\response.py_

- **"ssl_.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\util\ssl_.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\urllib3\util\ssl_.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\util\ssl_.py_

- **"ssl_match_hostname.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\util\ssl_match_hostname.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\urllib3\util\ssl_match_hostname.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\util\ssl_match_hostname.py_

- **"ssltransport.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\util\ssltransport.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\urllib3\util\ssltransport.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\util\ssltransport.py_

- **"timeout.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\util\timeout.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\urllib3\util\timeout.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\util\timeout.py_

- **"url.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\util\url.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\engine\url.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\urllib3\util\url.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\util\url.py_

- **"wait.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\util\wait.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\urllib3\util\wait.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\util\wait.py_

- **"_collections.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\_collections.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\util\_collections.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\urllib3\_collections.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\_collections.py_

- **"connectionpool.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\connectionpool.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\urllib3\connectionpool.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\connectionpool.py_

- **"fields.py" appears in 4 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\fields.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\v1\fields.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\fields.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\fields.py_

- **"filepost.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\filepost.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\urllib3\filepost.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\filepost.py_

- **"poolmanager.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\poolmanager.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\urllib3\poolmanager.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\poolmanager.py_

- **"NOTICE" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\propcache-0.4.1.dist-info\licenses\NOTICE, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\yarl-1.22.0.dist-info\licenses\NOTICE
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\propcache-0.4.1.dist-info\licenses\NOTICE_

- **"sql.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\psycopg2\sql.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\testing\fixtures\sql.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\psycopg2\sql.py_

- **"decoder.py" appears in 5 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pyasn1\codec\ber\decoder.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pyasn1\codec\cer\decoder.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pyasn1\codec\der\decoder.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pyasn1\codec\ber\decoder.py_

- **"encoder.py" appears in 5 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pyasn1\codec\ber\encoder.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pyasn1\codec\cer\encoder.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pyasn1\codec\der\encoder.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pyasn1\codec\ber\encoder.py_

- **"class_validators.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\deprecated\class_validators.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\v1\class_validators.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\class_validators.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\deprecated\class_validators.py_

- **"decorator.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\deprecated\decorator.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\v1\decorator.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\decorator.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\deprecated\decorator.py_

- **"tools.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\deprecated\tools.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\v1\tools.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\tools.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\deprecated\tools.py_

- **"datetime_parse.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\v1\datetime_parse.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\datetime_parse.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\v1\datetime_parse.py_

- **"env_settings.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\v1\env_settings.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\env_settings.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\v1\env_settings.py_

- **"error_wrappers.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\v1\error_wrappers.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\error_wrappers.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\v1\error_wrappers.py_

- **"generics.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\v1\generics.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\generics.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\v1\generics.py_

- **"mypy.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\v1\mypy.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\mypy.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\testing\fixtures\mypy.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\v1\mypy.py_

- **"networks.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\v1\networks.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\networks.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\v1\networks.py_

- **"schema.py" appears in 5 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\v1\schema.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\schema.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\sql\schema.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\v1\schema.py_

- **"typing.py" appears in 4 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\v1\typing.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\typing.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\util\typing.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic\v1\typing.py_

- **"Buenos_Aires" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\America\Argentina\Buenos_Aires, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\America\Buenos_Aires
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\America\Argentina\Buenos_Aires_

- **"Catamarca" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\America\Argentina\Catamarca, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\America\Catamarca
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\America\Argentina\Catamarca_

- **"Cordoba" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\America\Argentina\Cordoba, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\America\Cordoba
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\America\Argentina\Cordoba_

- **"Jujuy" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\America\Argentina\Jujuy, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\America\Jujuy
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\America\Argentina\Jujuy_

- **"Mendoza" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\America\Argentina\Mendoza, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\America\Mendoza
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\America\Argentina\Mendoza_

- **"Indianapolis" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\America\Indiana\Indianapolis, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\America\Indianapolis
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\America\Indiana\Indianapolis_

- **"Louisville" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\America\Kentucky\Louisville, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\America\Louisville
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\America\Kentucky\Louisville_

- **"Jamaica" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\America\Jamaica, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Jamaica
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\America\Jamaica_

- **"Istanbul" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Asia\Istanbul, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Europe\Istanbul
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Asia\Istanbul_

- **"Nicosia" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Asia\Nicosia, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Europe\Nicosia
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Asia\Nicosia_

- **"Singapore" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Asia\Singapore, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Singapore
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Asia\Singapore_

- **"West" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Australia\West, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Brazil\West
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Australia\West_

- **"Central" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Canada\Central, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\US\Central
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Canada\Central_

- **"Eastern" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Canada\Eastern, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\US\Eastern
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Canada\Eastern_

- **"Mountain" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Canada\Mountain, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\US\Mountain
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Canada\Mountain_

- **"Pacific" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Canada\Pacific, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\US\Pacific
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Canada\Pacific_

- **"GMT" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Etc\GMT, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\GMT
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Etc\GMT_

- **"GMT-0" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Etc\GMT-0, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\GMT-0
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Etc\GMT-0_

- **"GMT+0" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Etc\GMT+0, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\GMT+0
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Etc\GMT+0_

- **"GMT0" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Etc\GMT0, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\GMT0
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Etc\GMT0_

- **"Greenwich" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Etc\Greenwich, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Greenwich
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Etc\Greenwich_

- **"UCT" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Etc\UCT, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\UCT
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Etc\UCT_

- **"Universal" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Etc\Universal, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Universal
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Etc\Universal_

- **"UTC" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Etc\UTC, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\UTC
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Etc\UTC_

- **"Zulu" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Etc\Zulu, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Zulu
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Etc\Zulu_

- **"Kwajalein" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Pacific\Kwajalein, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Kwajalein
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Pacific\Kwajalein_

- **"Samoa" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Pacific\Samoa, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\US\Samoa
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Pacific\Samoa_

- **"aioodbc.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\connectors\aioodbc.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\dialects\mssql\aioodbc.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\connectors\aioodbc.py_

- **"asyncio.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\connectors\asyncio.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\testing\asyncio.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\uvicorn\loops\asyncio.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\connectors\asyncio.py_

- **"pyodbc.py" appears in 3 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\connectors\pyodbc.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\dialects\mssql\pyodbc.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\dialects\mysql\pyodbc.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\connectors\pyodbc.py_

- **"provision.py" appears in 6 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\dialects\mssql\provision.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\dialects\mysql\provision.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\dialects\oracle\provision.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\dialects\mssql\provision.py_

- **"dml.py" appears in 4 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\dialects\mysql\dml.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\dialects\postgresql\dml.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\dialects\sqlite\dml.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\dialects\mysql\dml.py_

- **"reflection.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\dialects\mysql\reflection.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\engine\reflection.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\dialects\mysql\reflection.py_

- **"_py_util.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\engine\_py_util.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\sql\_py_util.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\engine\_py_util.py_

- **"events.py" appears in 6 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\engine\events.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\orm\events.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\pool\events.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\engine\events.py_

- **"result.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\engine\result.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\ext\asyncio\result.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\engine\result.py_

- **"strategies.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\engine\strategies.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\orm\strategies.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\engine\strategies.py_

- **"engine.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\ext\asyncio\engine.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\future\engine.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\ext\asyncio\engine.py_

- **"scoping.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\ext\asyncio\scoping.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\orm\scoping.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\ext\asyncio\scoping.py_

- **"compiler.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\ext\compiler.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\sql\compiler.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\ext\compiler.py_

- **"instrumentation.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\ext\instrumentation.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\orm\instrumentation.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\ext\instrumentation.py_

- **"authentication.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\starlette\middleware\authentication.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\starlette\authentication.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\starlette\middleware\authentication.py_

- **"server.py" appears in 5 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\uvicorn\server.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\websockets\asyncio\server.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\websockets\legacy\server.py...
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\uvicorn\server.py_

- **"router.py" appears in 2 locations**
  > Found at: ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\websockets\asyncio\router.py, ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\websockets\sync\router.py
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\websockets\asyncio\router.py_

### LOW

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\frontend\app\(dashboard)\chart-of-accounts\[id]\edit**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\frontend\app\(dashboard)\chart-of-accounts\[id]\edit_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\frontend\app\(dashboard)\treasury\bank-accounts\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\frontend\app\(dashboard)\treasury\bank-accounts\[id]_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\frontend\app\(dashboard)\treasury\bank-accounts\[id]\edit**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\frontend\app\(dashboard)\treasury\bank-accounts\[id]\edit_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\frontend\app\(dashboard)\treasury\bank-accounts\new**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\frontend\app\(dashboard)\treasury\bank-accounts\new_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\frontend\app\(dashboard)\treasury\fx-conversions\new**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\frontend\app\(dashboard)\treasury\fx-conversions\new_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\frontend\coverage\lcov-report\components\pages\ar**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\frontend\coverage\lcov-report\components\pages\ar_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\frontend\coverage\lcov-report\components\pages\chart-of-accounts**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\frontend\coverage\lcov-report\components\pages\chart-of-accounts_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\frontend\coverage\lcov-report\components\pages\dashboard**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\frontend\coverage\lcov-report\components\pages\dashboard_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\frontend\coverage\lcov-report\components\pages\dimensions**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\frontend\coverage\lcov-report\components\pages\dimensions_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\frontend\coverage\lcov-report\components\pages\journal-entries**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\frontend\coverage\lcov-report\components\pages\journal-entries_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\frontend\coverage\lcov-report\components\pages\payroll**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\frontend\coverage\lcov-report\components\pages\payroll_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\frontend\coverage\lcov-report\components\pages\periods**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\frontend\coverage\lcov-report\components\pages\periods_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\frontend\coverage\lcov-report\components\pages\reports**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\frontend\coverage\lcov-report\components\pages\reports_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\frontend\coverage\lcov-report\components\pages\treasury**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\frontend\coverage\lcov-report\components\pages\treasury_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohttp-3.13.3.dist-info\licenses\vendor**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohttp-3.13.3.dist-info\licenses\vendor_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohttp-3.13.3.dist-info\licenses\vendor\llhttp**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\aiohttp-3.13.3.dist-info\licenses\vendor\llhttp_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\templates\async**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\templates\async_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\templates\generic**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\templates\generic_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\templates\multidb**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\templates\multidb_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\testing\plugin**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\testing\plugin_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\testing\suite**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\alembic\testing\suite_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\asyncpg\pgproto\codecs**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\asyncpg\pgproto\codecs_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\asyncpg\protocol\codecs**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\asyncpg\protocol\codecs_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\asn1**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\asn1_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\backends**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\backends_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\backends\openssl**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\backends\openssl_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\bindings**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\bindings_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\bindings\_rust**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\bindings\_rust_

- **Deep nesting (depth 8): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\bindings\_rust\openssl**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\bindings\_rust\openssl_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\bindings\openssl**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\bindings\openssl_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\decrepit**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\decrepit_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\decrepit\ciphers**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\decrepit\ciphers_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\primitives**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\primitives_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\primitives\asymmetric**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\primitives\asymmetric_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\primitives\ciphers**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\primitives\ciphers_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\primitives\kdf**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\primitives\kdf_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\primitives\serialization**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\primitives\serialization_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\primitives\twofactor**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\cryptography\hazmat\primitives\twofactor_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\multipart\tests\test_data**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\multipart\tests\test_data_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\multipart\tests\test_data\http**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\multipart\tests\test_data\http_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\test\meta**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\test\meta_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\_typeshed**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\_typeshed_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\asyncio**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\asyncio_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\collections**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\collections_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\concurrent**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\concurrent_

- **Deep nesting (depth 8): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\concurrent\futures**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\concurrent\futures_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\ctypes**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\ctypes_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\curses**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\curses_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\dbm**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\dbm_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\distutils**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\distutils_

- **Deep nesting (depth 8): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\distutils\command**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\distutils\command_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\email**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\email_

- **Deep nesting (depth 8): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\email\mime**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\email\mime_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\encodings**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\encodings_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\ensurepip**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\ensurepip_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\html**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\html_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\http**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\http_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\importlib**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\importlib_

- **Deep nesting (depth 8): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\importlib\metadata**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\importlib\metadata_

- **Deep nesting (depth 8): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\importlib\resources**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\importlib\resources_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\json**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\json_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\lib2to3**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\lib2to3_

- **Deep nesting (depth 8): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\lib2to3\fixes**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\lib2to3\fixes_

- **Deep nesting (depth 8): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\lib2to3\pgen2**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\lib2to3\pgen2_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\logging**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\logging_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\msilib**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\msilib_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\multiprocessing**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\multiprocessing_

- **Deep nesting (depth 8): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\multiprocessing\dummy**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\multiprocessing\dummy_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\os**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\os_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\pydoc_data**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\pydoc_data_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\pyexpat**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\pyexpat_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\sqlite3**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\sqlite3_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\tkinter**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\tkinter_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\unittest**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\unittest_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\urllib**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\urllib_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\venv**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\venv_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\wsgiref**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\wsgiref_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\xml**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\xml_

- **Deep nesting (depth 8): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\xml\dom**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\xml\dom_

- **Deep nesting (depth 8): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\xml\etree**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\xml\etree_

- **Deep nesting (depth 8): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\xml\parsers**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\xml\parsers_

- **Deep nesting (depth 8): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\xml\sax**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\xml\sax_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\xmlrpc**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\xmlrpc_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\zoneinfo**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stdlib\zoneinfo_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stubs**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stubs_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stubs\mypy-extensions**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypy\typeshed\stubs\mypy-extensions_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypyc\external\googletest**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypyc\external\googletest_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypyc\external\googletest\include**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypyc\external\googletest\include_

- **Deep nesting (depth 8): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypyc\external\googletest\include\gtest**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypyc\external\googletest\include\gtest_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypyc\external\googletest\make**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypyc\external\googletest\make_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypyc\external\googletest\src**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypyc\external\googletest\src_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypyc\test-data\driver**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypyc\test-data\driver_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypyc\test-data\fixtures**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\mypyc\test-data\fixtures_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\passlib\_data\wordsets**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\passlib\_data\wordsets_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\passlib\crypto\_blowfish**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\passlib\crypto\_blowfish_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\passlib\crypto\scrypt**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\passlib\crypto\scrypt_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\passlib\ext\django**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\passlib\ext\django_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\passlib\utils\compat**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\passlib\utils\compat_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pathspec\_backends\hyperscan**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pathspec\_backends\hyperscan_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pathspec\_backends\re2**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pathspec\_backends\re2_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pathspec\_backends\simple**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pathspec\_backends\simple_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pathspec\patterns\gitignore**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pathspec\patterns\gitignore_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\cli**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\cli_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\commands**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\commands_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\distributions**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\distributions_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\index**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\index_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\locations**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\locations_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\metadata**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\metadata_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\metadata\importlib**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\metadata\importlib_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\models**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\models_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\network**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\network_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\operations**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\operations_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\operations\build**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\operations\build_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\operations\install**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\operations\install_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\req**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\req_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\resolution**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\resolution_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\resolution\legacy**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\resolution\legacy_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\resolution\resolvelib**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\resolution\resolvelib_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\utils**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\utils_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\vcs**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_internal\vcs_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\cachecontrol**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\cachecontrol_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\cachecontrol\caches**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\cachecontrol\caches_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\certifi**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\certifi_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\dependency_groups**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\dependency_groups_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\distlib**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\distlib_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\distro**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\distro_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\idna**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\idna_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\msgpack**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\msgpack_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\packaging**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\packaging_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\packaging\licenses**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\packaging\licenses_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\pkg_resources**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\pkg_resources_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\platformdirs**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\platformdirs_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\pygments**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\pygments_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\pygments\filters**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\pygments\filters_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\pygments\formatters**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\pygments\formatters_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\pygments\lexers**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\pygments\lexers_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\pygments\styles**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\pygments\styles_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\pyproject_hooks**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\pyproject_hooks_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\pyproject_hooks\_in_process**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\pyproject_hooks\_in_process_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\requests**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\requests_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\resolvelib**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\resolvelib_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\resolvelib\resolvers**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\resolvelib\resolvers_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\rich**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\rich_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\tomli**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\tomli_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\tomli_w**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\tomli_w_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\truststore**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\truststore_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\contrib**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\contrib_

- **Deep nesting (depth 8): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\contrib\_securetransport**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\contrib\_securetransport_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\packages**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\packages_

- **Deep nesting (depth 8): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\packages\backports**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\packages\backports_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\util**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip\_vendor\urllib3\util_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip-26.0.1.dist-info\licenses\src**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip-26.0.1.dist-info\licenses\src_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip-26.0.1.dist-info\licenses\src\pip**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip-26.0.1.dist-info\licenses\src\pip_

- **Deep nesting (depth 8): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip-26.0.1.dist-info\licenses\src\pip\_vendor**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pip-26.0.1.dist-info\licenses\src\pip\_vendor_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pyasn1\codec\ber**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pyasn1\codec\ber_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pyasn1\codec\cer**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pyasn1\codec\cer_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pyasn1\codec\der**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pyasn1\codec\der_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pyasn1\codec\native**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pyasn1\codec\native_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic_settings\sources\providers**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pydantic_settings\sources\providers_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Africa**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Africa_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\America**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\America_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\America\Argentina**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\America\Argentina_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\America\Indiana**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\America\Indiana_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\America\Kentucky**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\America\Kentucky_

- **Deep nesting (depth 7): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\America\North_Dakota**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\America\North_Dakota_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Antarctica**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Antarctica_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Arctic**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Arctic_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Asia**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Asia_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Atlantic**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Atlantic_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Australia**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Australia_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Brazil**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Brazil_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Canada**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Canada_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Chile**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Chile_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Etc**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Etc_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Europe**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Europe_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Indian**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Indian_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Mexico**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Mexico_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Pacific**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\Pacific_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\US**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\pytz\zoneinfo\US_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\dialects\mssql**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\dialects\mssql_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\dialects\mysql**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\dialects\mysql_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\dialects\oracle**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\dialects\oracle_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\dialects\postgresql**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\dialects\postgresql_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\dialects\sqlite**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\dialects\sqlite_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\ext\asyncio**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\ext\asyncio_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\ext\declarative**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\ext\declarative_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\ext\mypy**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\ext\mypy_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\testing\fixtures**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\testing\fixtures_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\testing\plugin**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\testing\plugin_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\testing\suite**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\sqlalchemy\testing\suite_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\urllib3\contrib\emscripten**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\urllib3\contrib\emscripten_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\uvicorn\protocols\http**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\uvicorn\protocols\http_

- **Deep nesting (depth 6): ..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\uvicorn\protocols\websockets**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Financial_Management_Service\venv\Lib\site-packages\uvicorn\protocols\websockets_



## Related Service
- [[Cross-Service/truevow-financial-management-service|Service Page]]
