# Firecrawl Self-Host — Condensed Reference
Source: https://docs.firecrawl.dev/contributing/self-host
Full guide: https://github.com/firecrawl/firecrawl/blob/main/SELF_HOST.md

## Prerequisites
- Docker + `docker compose`
- Git clone of the Firecrawl repo

## Required .env (minimal)
```
PORT=3002
HOST=0.0.0.0
USE_DB_AUTHENTICATION=false
BULL_AUTH_KEY=<random-string>
PLAYWRIGHT_MICROSERVICE_URL=http://playwright-service:3000/scrape
REDIS_URL=redis://redis:6379
REDIS_RATE_LIMIT_URL=redis://redis:6379
```

## Deploy
```bash
git clone https://github.com/firecrawl/firecrawl
cd firecrawl
cp apps/api/.env.example .env   # fill in the above
docker compose build
docker compose up -d
# → API at http://localhost:3002
# → Bull Queue UI at http://localhost:3002/admin/<BULL_AUTH_KEY>/queues
```

## Fly.io deploy (use their compose as-is)
```bash
cd firecrawl
fly launch --org truevow --name truevow-firecrawl
fly deploy    # uses their docker-compose.yml + .env
```

## Key limitations (self-hosted vs cloud)
- `/agent` and `/browser` endpoints NOT supported
- Screenshots work IF Playwright service is running
- Supabase auth NOT available in self-host
- Fire-engine (IP blocks, robot detection) NOT available

## Test
```bash
curl -X POST http://localhost:3002/v2/crawl \
    -H 'Content-Type: application/json' \
    -d '{"url": "https://docs.firecrawl.dev"}'
```

## Troubleshooting common issues
- "Supabase client not configured" → ignore (self-host limitation)
- "Bypassing authentication" → ignore (self-host limitation)
- Redis connection refused → check REDIS_URL + Redis container
- Docker fails to start → check logs + .env vars
