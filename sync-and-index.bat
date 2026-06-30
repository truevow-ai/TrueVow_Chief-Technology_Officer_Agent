@echo off
echo.
echo === TrueVow Knowledge Pipeline ===
echo.
echo [1/2] Syncing git activity...
cd /d "%~dp0shared-libraries\knowledge-sync"
call npm run sync
echo.
echo [2/2] Reindexing knowledge vault...
cd /d "%~dp0shared-libraries\knowledge-indexer"
call npm run index
echo.
echo === Done. Vault is up-to-date. ===
pause
