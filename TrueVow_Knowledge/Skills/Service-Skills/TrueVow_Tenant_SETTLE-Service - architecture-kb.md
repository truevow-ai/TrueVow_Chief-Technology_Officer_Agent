---
source: TrueVow_Tenant_SETTLE-Service/.opencode/skills/architecture-kb/SKILL.md
service: TrueVow_Tenant_SETTLE-Service
type: settlement-engine
stack: ["python", "nextjs", "postgresql", "alembic", "docker"]
imported: 2026-06-30T22:32:05.035461+00:00
skill_name: architecture-kb
---
# Architecture Knowledge Base — SETTLE Service Current State

**Last Updated:** 2026-06-23
**When to use:** Any agent needs to understand what exists in the codebase, where to find things, or what the current implementation status is.

---

## TrueVow 3-Product Ecosystem

| Product | Description | Pricing |
|---|---|---|
| **INTAKE (Benjamin)** | AI receptionist for PI attorneys | $499 / $1,299 / $1,999/mo |
| **LEVERAGE** | 50-state PI Case Intelligence. 34 endpoints. Damages, SOL, compliance. | $99/mo ecosystem |
| **SETTLE** | Settlement Intelligence Network. Comparable case matching. Port 8002 dev / 8004 prod. | TBD (pilot/free) |

## 5-Stage Attorney Journey

```
Stage 1: INTAKE (lead capture)
  -> Stage 2: LEVERAGE (compliance -- SOL, jurisdiction)
    -> Stage 3: LEVERAGE (damages -- economic calculations)
      -> Stage 4: LEVERAGE + SETTLE (negotiation -- comparable settlements)
        -> Stage 5: SETTLE (network effect -- industry-wide intelligence)
```

## Current Implementation Status

**ALL Phases 1-5: DONE. 186/186 unit tests. 14/14 E2E tests. 23/24 DOCKET tests.**

| Phase | Scope | Status |
|---|---|---|
| Phase 1 | Core engine, gate, contributions, anonymizer, anomaly, reputation, injury classifier, PDF, auth, billing, storage, email, Sentry | DONE |
| Phase 2 | Verdict research (17-filter), confidence score (7-factor), advanced filters (9), carrier analytics | DONE |
| Phase 2.5 | Trend studies / market reports | DONE |
| Phase 3.1-3.5 | Multiplier model, overdemand cliff, override tracking, weekly digest, recency weighting | DONE |
| Phase 4 | Outcome distribution, trial risk indicators | DONE |
| Phase 5 | DOCKET-Service (CourtListener scraper) | DONE |

## Service Layer (22+ modules at `app/services/`)

| Module | File | Purpose |
|---|---|---|
| Estimator | `estimator.py` | Percentile + 3-tier multiplier + recency weighting |
| Intelligence Gate | `intelligence_gate.py` | Hierarchical: county (n>=50) -> state (n>=10 pilot) -> suppressed |
| Confidence Score | `confidence_score.py` | 7-factor weighted scoring (10-95) |
| Injury Classifier | `injury_classifier/` (6 files) | Deterministic 17-tag, regex-based, zero LLM |
| Carrier Patterns | `carrier_patterns.py` | Defendant category analytics |
| Outcome Distribution | `outcome_distribution.py` | Settlement/verdict rate analysis |
| Overdemand Cliff | `overdemand_cliff.py` | Demand threshold detection |
| Override Tracking | `override_tracking.py` | Tracks attorney overrides |
| Reputation Service | `reputation_service.py` | 4-tier trust scoring |
| Anomaly Detector | `anomaly_detector.py` | 6 anomaly checks |
| Trend Reports | `trend_reports.py` | Quarterly market reports |
| Weekly Digest | `weekly_digest.py` | Intelligence digest emails |
| Verdict Search | `verdict_search.py` | Internal 17-filter search (admin) |
| Contributor | `contributor.py` | Contribution workflow |
| Anonymizer | `anonymizer.py` | PHI/PII detection |
| Validator | `validator.py` | Input validation |
| PDF Generator | `reports/pdf_generator.py` | 4-page WeasyPrint PDF |
| Billing | `billing/stripe_service.py` | Stripe integration |
| Email | `notifications/email_service.py` | Resend notifications |
| Storage | `storage/s3_service.py` | AWS S3 |
| Platform Client | `integrations/platform/client.py` | Platform integration |
| Internal Ops | `integrations/internal_ops/client.py` | Internal ops integration |

## API Endpoints (10 files, 40+ endpoints)

| Group | File | Prefix | Key Routes |
|---|---|---|---|
| Query | `query.py` | `/api/v1/query` | POST /estimate, GET /health |
| Contribute | `contribute.py` | `/api/v1/contribute` | POST /submit, GET /stats |
| Reports | `reports.py` | `/api/v1/reports` | POST /generate, GET /my-reports, GET /template |
| Admin | `admin.py` | `/api/v1/admin` | 26 routes (contributions, members, keys, analytics) |
| Waitlist | `waitlist.py` | `/api/v1/waitlist` | POST /join, admin CRUD |
| Stats | `stats.py` | `/api/v1/stats` | /founding-members, /database |
| Carrier | `carrier_analytics.py` | `/api/v1/analytics` | /carrier-patterns |
| Verdicts | `verdicts.py` | `/api/v1/internal/verdicts` | Search, stats, CRUD (admin) |
| Trends | `trend_reports.py` | `/api/v1/trends` | 3 trend endpoints |
| Overrides | `override_tracking.py` | `/api/v1/overrides` | Override tracking |

## Key Files Quick Reference

| File | Purpose |
|---|---|
| `app/main.py` | FastAPI app, lifespan, CORS |
| `app/core/config.py` | Settings (SETTLE_ prefix env vars) |
| `app/core/auth.py` | API key auth, access levels |
| `app/core/database.py` | SupabaseRESTClient (httpx, NOT asyncpg) |
| `app/models/case_bank.py` | EstimateRequest/Response, ComparableCase, ContributionRequest |
| `app/models/verdicts.py` | Verdict search models |
| `database/schemas/settle_supabase.sql` | Production schema |
| `docs/01-main/IMPLEMENTATION_PROGRESS.md` | Status tracker |
| `docs/01-main/WORKING_CACHE.md` | Session handoff cache |
| `fly.toml` | Fly.io deployment config |

## Database

- **Client:** SupabaseRESTClient (custom httpx-based). Chainable: `.table().select().eq().ilike().cs().order().limit().execute()`
- **NOT asyncpg/SQLAlchemy** — uses REST API
- **440 approved contributions**, 29 pending, 469 total
- **Alembic head:** `ed2900358f69`
