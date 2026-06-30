@echo off
REM Quick log wrapper — drop-in for any developer
REM Usage: log "file-write" "Changed billing route"
REM        log "blocker" "DB connection failing"
REM        log "task-complete" "Finished invoice generation"

if "%~1"=="" (
  echo Usage: log ^<action^> ^<detail^> [service]
  echo Actions: task-start, task-complete, task-fail, file-write, file-read, blocker, decision, question, commit, deploy, session-start, session-end
  exit /b 1
)

set AGENT=%~3
if "%AGENT%"=="" set AGENT=default
set SERVICE=%~4
if "%SERVICE%"=="" set SERVICE=

python "%~dp0TrueVow_Knowledge\Skills\vault-log.py" --agent "%AGENT%" --action "%~1" --detail "%~2" --service "%SERVICE%"
