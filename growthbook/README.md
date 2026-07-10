# Growthbook Self-Hosted — Platform Service

Location: `growthbook/` in the CTO agent repo (platform infra, not per-repo).
Deploy alongside SigNoz, Infisical, Chatwoot on Fly.io shared infra.

**Start:** `cd growthbook && docker compose up -d` → `http://localhost:3000`
**Source of truth:** a maintained fork at `growthbook/growthbook`; pull stable releases.
**Do NOT self-build** — use the official image (`growthbook/growthbook:latest`) per `docker-compose.yml`.

## TrueVow use-cases
- **Feature flags per firm** — toggle TRACE Phase 2 features per early-access firm without a deploy.
- **A/B test INTAKE voice bridges** — measure which bridge converts better per caller cohort.
- **Usage dashboards** — surface adoption metrics for CSM (replaces scattered analytics).
- **Rollout control** — enable new products (SETTLE Phase 2, LEVERAGE GA) per tenant, not all-at-once global.

## Per-repo SDK wiring (when ready)
| Service | SDK | Flag example |
|---|---|---|
| TRACE | `growthbook` (Python) | `gb.isOn("trace-phase2-provider-export", { attributes: { firmId } })` |
| Customer Portal | `@growthbook/growthbook-react` | Feature-gate sidebar modules per subscription tier |
| SaaS Admin | `growthbook` (Python) or direct API | Admin toggle for per-firm feature enablement |
| INTAKE | `growthbook` (Python) | A/B voice bridge routing per tenant |
