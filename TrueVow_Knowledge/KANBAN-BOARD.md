---
kanban-plugin: basic
---

## 🔴 Blocked



## 🟡 Deferred — Waiting on Signal

- [ ] Tenant App cleanup — 🟢 awaiting bridges all-green signal from user (Q9: maintenance, can wait)


## 🟡 In Progress — Phase 3: Production Hardening

- [ ] **Auth + RBAC integration** — wire `auth-client` + `rbac-engine` into Customer Portal (P1)
- [ ] **Observability stack** — deploy existing docker-compose (Prometheus + Grafana + Jaeger + Loki) (P1)
- [ ] **Security utils** — wire PII redaction, audit logging, anti-exfil into Tenant App + SaaS Admin (P2)
- [ ] **CI/CD pipeline** — GitHub Actions test pipeline for all services (P2)
- [ ] **CONNECT integration hub** — minimal implementation (P3)


## 🟡 Pending

- [ ] Read LiveKit repo (separate from Tenant App Service)
- [ ] Scan remaining Dograh/Dograh Fork repos
- [ ] Investigate Internal Ops nested .env.local anomaly
- [ ] Fix 4/5 Supabase project DNS (Supabase-side ticket)


## 🟢 Done

- [x] Vault scaffolded — 61 files, ADRs, Incidents, Templates
- [x] Vector index — 556 chunks searchable
- [x] Git ingestion — 159 commits tracked across 13 repos
- [x] Code mapper — all 16 services mapped
- [x] Agent harnesses — 3 templates, framework-agnostic
- [x] Customer Portal unblocked
- [x] LEVERAGE started, DB connected
- [x] Platform Analytics DB fixed (pooler URL)
- [x] Start scripts for all 3 services
- [x] DNS audit completed
- [x] Batch DB fix audit — Platform Analytics was the only broken one
- [x] Obsidian installed, graph configured
- [x] Dataview + Kanban plugins installed
- [x] Dashboard + Kanban board created
- [x] Hermes pattern lift — `.triage.yaml` (220 lines) + orchestrator harness updated with 3-verb gate (2026-06-02)
- [x] Vault reindexed post-Hermes-lift — 577 chunks, 64 files
- [x] Policies section added to `.triage.yaml` — 8 categories: persistence, git, secrets, destructive, production, cross-service, audit, agents (2026-06-02)
- [x] Agent harnesses annotated with Worker/Service/Support type (arXiv 2601.13671 taxonomy)
- [x] Vault reindexed post-policies-lift — 587 chunks, 65 files
- [x] Skills system implemented — `Skills/` directory with 10 atomic skills, `Templates/SKILL.md`, 3 harnesses refactored to reference skills (2026-06-02)
- [x] Feedback Agent now has weekly Skills Audit step (closes the improvement loop)
- [x] Vault reindexed post-skills-implementation — 689 chunks, 76 files
- [x] `Projects/` directory created — 1 active project (tenant-app-bridges), `Templates/Project.md` (2026-06-02)
- [x] `Agent/` self-documentation folder created — 6 files: README, log, questions, state, changelog, self-assessment (2026-06-02)
- [x] Vault reindexed post-projects+agent — 772 chunks, 85 files
- [x] Bridges work intake — read progress logs, identified real 6-bridge list, wrote project page (2026-06-02)
- [x] Hybrid tracking workflow chosen — git hook + 60-sec daily check-in (2026-06-02)
- [x] Weekly bridges audit completed — 15 sessions, 6 bridges, 5 patterns (2026-06-02)
- [x] 6 new skills built — log-test-result, log-blocker, log-task-completion, daily-checkin, backfill-project-from-repos, audit-week-of-sessions (2026-06-02)
- [x] Restart Platform Analytics to pick up new DB pooler URL — port 3071 live (2026-06-02)
- [x] Vault reindexed post-skills-extraction — 843 chunks, 85 files
- [x] Q6-Q12 user questions answered, open-questions.md updated (2026-06-02)


## 📌 Ideas / Future

- [ ] Phase 5: Agent team subagents
- [ ] Phase 5: Self-improving flywheel metrics
- [ ] Custom TrueVow health dashboard (if Obsidian isn't enough)
- [ ] OMI-style auto-capture (voice/screen → vault)
- [ ] CI/CD event webhooks → auto-incident creation
