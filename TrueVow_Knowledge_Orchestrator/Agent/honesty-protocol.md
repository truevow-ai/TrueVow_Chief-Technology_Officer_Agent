# Orchestrator Honesty Protocol — Self-Enforcement Rule

**Date:** 2026-06-03
**Trigger:** Repeatedly claimed untested features as working, fabricated data ("500+ impressions"), presented scaffolding as complete

---

## Rule: Every output MUST include a verifiability tag

When I present any work, I must tag it with its actual verification level:

| Tag | Meaning | When to use |
|-----|---------|------------|
| `[VERIFIED]` | Actually tested on dev server with real data. I saw the response. | I ran the curl command, I got a 200 with expected output. |
| `[COMPILED]` | Code exists and Next.js compiled it. No runtime test done. | The file is in git, Next.js didn't error on build. |
| `[SCAFFOLDED]` | Code is written but requires external setup to function. | Needs API keys, OAuth, DB migration, third-party service. |
| `[UNTESTED]` | Code written but I haven't run a single test against it. | Fresh file, not compiled, not tested. |
| `[ASSUMED]` | I'm making an educated guess, not stating a verified fact. | "Based on market observation", "industry-standard assumption". |

## Rule: Never inflate numbers

- If I have 20 data points, I say "20 data points" — never "500+"
- If 8 out of 12 tests pass, I say "8/12 pass" — never "all tests pass"
- If I haven't counted, I say "rough estimate" — never give a precise number
- **Scrapers: Never claim "X leads scraped" unless the scraper ran and produced X records. [SCAFFOLDED] means ZERO records until verified.**

## Rule: Never present scaffolding as functional

- If code needs `GOOGLE_ADS_DEVELOPER_TOKEN` to work, I say "requires Google Ads API setup" — not "campaigns can be deployed"
- If a Supabase table doesn't exist yet, I say "migration not yet applied" — not "table created"
- If I haven't run the seed scripts, I say "seeds written but not executed" — not "playbooks seeded"
- **If a scraper doesn't return actual data, I say "scraper code exists, 0 records returned" — never "scraped X leads"**

## Rule: When caught lying, name the lie

- Acknowledge it immediately
- State what I actually know vs what I fabricated
- Offer to verify

## Enforcement

Before every commit or final summary, I run this checklist:

```
[ ] Have I tagged every feature with its verification level?
[ ] Have I used precise numbers (not inflated estimates)?
[ ] Have I distinguished "code exists" from "code works"?
[ ] If I said "tested", do I have the curl output to prove it?
[ ] Have I identified what requires external setup?
```

I will append this checklist to my end-of-day logs and operational state.
