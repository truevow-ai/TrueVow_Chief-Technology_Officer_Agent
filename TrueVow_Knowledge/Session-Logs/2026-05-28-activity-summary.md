# Activity Summary — 2026-05-28

**Services scanned:** 16
**Repos with git:** 13
**New commits found:** 159

## Commits by Service

- [[Customer Success CORE Service]] — 3 commit(s)
  - `0ee17e4` docs: add CS-Split milestone checkpoint and implementation checklist (_Admin_, 2026-02-15)
  - `84862af` feat: split CS-Support into Core (LLM-free) and First-Line (LLM-enabled) (_Admin_, 2026-02-15)
  - `e58e7cd` testing 13 feb (_Admin_, 2026-02-13)
- [[Financial Management Service]] — 5 commit(s)
  - `8187c83` refactor: Phase 2a - Move database/ to infra/database/ (_Admin_, 2026-03-06)
  - `859d737` refactor: Phase 1 - Create standard directory structure (apps, services, libs, config, infra) (_Admin_, 2026-03-06)
  - `900ecbe` All Tests passed (_Admin_, 2026-02-13)
- [[First Line Support Service]] — 1 commit(s)
  - `7d054ab` feat: split CS-Support into Core (LLM-free) and First-Line (LLM-enabled) (_Admin_, 2026-02-15)
- [[Internal Ops Service]] — 3 commit(s)
  - `6348e91` all tests done 13 Feb (_Admin_, 2026-02-13)
  - `e3924f6` feat(security): Implement production security enhancements (_Admin_, 2026-02-10)
  - `e502bb4` feat: Initial commit with security enhancements and test suite (_Admin_, 2026-02-10)
- [[SaaS Administration Service]] — 30 commit(s)
  - `4cb1345` fix: Dograh adapter — add workflow_configurations (idle_timeout=18s) + max_call_duration (600s) (_Admin_, 2026-05-28)
  - `07d91f1` fix: Dograh adapter — unique edge labels (not all 'Next') (_Admin_, 2026-05-28)
  - `fad80f2` feat: AssemblyAI bridge adapter — STT config bridge (_Admin_, 2026-05-28)
- [[Sales Ops Service]] — 2 commit(s)
  - `e08ea4d` orchestrator agent with skills implemented (_Admin_, 2026-03-16)
  - `087091c` Orchestrator given Skills (_Admin_, 2026-03-15)
- [[Tenant Application Service]] — 30 commit(s)
  - `3d0e55d` docs: session checkpoint - bridge comparison, latency analysis, code cleanup (_Admin_, 2026-05-28)
  - `f3124b4` docs: Dograh response #5 — workflow config + max call duration fixed, workflow 11 synced (_Admin_, 2026-05-28)
  - `295d7d4` docs: Dograh response #4 + AssemblyAI bridge handoff for sub-agent (_Admin_, 2026-05-28)
- [[Tenant Billing Service]] — 19 commit(s)
  - `43b0461` feat: register platform add-ons (auto_unlock, outbound_agent) in Billing Service (_Admin_, 2026-05-28)
  - `c5a83c8` feat(billing): add event ingestion endpoint for SaaS Admin integration (_Admin_, 2026-05-20)
  - `de803d0` fix(billing): fix test infrastructure and improve pass rate (_Admin_, 2026-05-19)
- [[Tenant CONNECT Service]] — 7 commit(s)
  - `0525645` docs: add comprehensive SaaS Admin CONNECT integration guide (_Shah@IntakelyAI_, 2025-12-08)
  - `21cfc48` docs: add comprehensive CONNECT service onboarding guide (_Shah@IntakelyAI_, 2025-12-08)
  - `6f6b6e7` docs: add comprehensive CONNECT architecture documentation (_Shah@IntakelyAI_, 2025-12-08)
- [[Tenant Customer Portal Service]] — 19 commit(s)
  - `5e25468` feat: add-ons management panel in billing page (_Admin_, 2026-05-28)
  - `755e368` feat: add auto_unlock addon — automatic A+ lead unlocking (_Admin_, 2026-05-28)
  - `8d492db` feat: fix TrueVow calendar — real API integration, unlock A+ leads, external sync (_Admin_, 2026-05-28)
- [[Tenant LEVERAGE Service]] — 8 commit(s)
  - `e321d02` docs: add database connection guide and template script for coding agents - verified working with 19 leverage schema tables - includes psycopg3 + Supabase pooler connection method - 5 critical rules for reliable connections (_Admin_, 2026-05-03)
  - `bec1acf` feat: align billing service with LEVERAGE integration guide - case-based pricing with updated overage rates (SOLO , GROWTH , TEAM ) - restructured check_case_limit() response to match Billing Service open-case format (authorized, source, price_cents, validations_unlimited) - free unlimited validations within opened cases - added INTEGRATION_LEVERAGE.md guide - updated all billing tests and mocks to match new response format - 135 tests passing (_Admin_, 2026-04-29)
  - `e7d7130` docs: create comprehensive SaaS Admin DRAFT integration guide (_Shah@IntakelyAI_, 2025-12-08)
- [[Tenant SETTLE Service]] — 30 commit(s)
  - `471c149` feat(admin): implement all stubbed admin endpoints (13 endpoints) (_Admin_, 2026-05-18)
  - `99c9119` fix(pipeline): wire contribution pipeline end-to-end (_Admin_, 2026-05-18)
  - `c1d18f2` feat(Cohort W+X): rich fields, reputation scoring, anomaly detection + admin UI (_Admin_, 2026-05-18)
- [[TrueVow Website]] — 2 commit(s)
  - `515c85b` docs: update SETTLE admin agent instructions with recent progress (_Shah@IntakelyAI_, 2025-12-07)
  - `1785f66` Website Fist Draft Finalized and Working (_Shah@IntakelyAI_, 2025-11-16)

## Config Changes
- Detected during scan — review [[Cross-Service]] for details
