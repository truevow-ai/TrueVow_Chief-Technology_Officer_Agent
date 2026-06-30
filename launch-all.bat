@echo off
echo ============================================
echo   TrueVow Platform — Start All Services
echo ============================================
echo.
echo 1/2 Starting Observability Stack...
docker-compose -f shared-libraries/observability/docker-compose.yml up -d
echo 2/2 Starting OSS Tools (Chatwoot, Mattermost, Novu, PostHog)...
docker-compose -f shared-libraries/oss-tools/docker-compose.yml up -d
echo.
echo ============================================
echo   All services starting!
echo ============================================
echo.
echo Observability:
echo   Jaeger UI:  http://localhost:16686
echo.
echo OSS Tools:
echo   Chatwoot:   http://localhost:3007
echo   Mattermost: http://localhost:8065
echo   Novu:       http://localhost:4200
echo   PostHog:    http://localhost:8010
echo.
echo Check all containers: docker ps
pause
