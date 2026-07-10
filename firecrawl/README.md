# Firecrawl + Camofox — Self-Hosted Web Scraping

Location: `firecrawl/` and `camofox/` in the CTO agent repo (platform infra).
These two run as platform services on Fly.io shared infra, NOT inside individual repos.

## How they pair
- **Firecrawl** (149k stars, AGPL) → bulk scraping + search + crawl. Returns clean Markdown or structured JSON. Handles volume, pagination, proxies.
- **Camofox** (7.5k stars, MIT) → anti-detection stealth browser. Drop-in replacement for Playwright/Puppeteer that bypasses Cloudflare, bot detection, anti-scraping. Handles the *hard* sites Firecrawl can't reach.

## Which repos use them

| Service | Tool | Why |
|---|---|---|
| **SETTLE** | Firecrawl + Camofox | Verdict/settlement data scraping. Currently broken — bot detection blocks the scraper. Firecrawl for bulk crawl of known legal databases; Camofox for anti-detection on Cloudflare-protected sites. |
| **Sales Ops** | Firecrawl | Lead enrichment — search + scrape attorney firm websites. Replaces the current fragile Playwright scraper that returns 403 on 40% of PI firm sites. |
| **Orchestrator (you)** | `agent-reach` skill | Web research. Firecrawl MCP gives your orchestrator real-time web data. |

## Quick start
```bash
# Firecrawl (self-hosted)
cd firecrawl && docker compose up -d   # http://localhost:3002

# Camofox (stealth browser)
cd camofox && npm install && npm start  # http://localhost:9377
```

## Wiring into SETTLE's scraper service
Replace the current `settle_data_scraping_factory/` implementation:
- Primary: Firecrawl API (`firecrawl-py` SDK) for bulk verdict search/crawl.
- Fallback (Cloudflare-blocked sites): Camofox REST API for anti-detection browser access.
- Both must run on Fly.io inside the HIPAA boundary (self-hosted, no data to Firecrawl cloud).

## Wiring into Sales Ops lead enrichment
Replace the current Playwright/Cheerio enrichment pipeline:
- Firecrawl `search` + `scrape` for targeted attorney-website extraction.
- Camofox as escalation when a site returns Cloudflare 403.
