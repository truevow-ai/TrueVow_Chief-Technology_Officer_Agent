@echo off
echo === TrueVow OSS Tools Launcher ===
echo.
echo Pulling Chatwoot, Mattermost, Novu, PostHog...
echo This may take 5-10 minutes on first run.
echo.
cd /d "%~dp0"
docker-compose -f shared-libraries/oss-tools/docker-compose.yml up -d
echo.
echo Done. Check status:
echo   docker ps
echo.
echo URLs:
echo   Chatwoot:   http://localhost:3007
echo   Mattermost: http://localhost:8065
echo   Novu:       http://localhost:4200
echo   PostHog:    http://localhost:8010
pause
