# Project: Tenant App — Voice Bridges

**Slug:** tenant-app-bridges
**Status:** active (orchestrator-tracked)
**Started:** ~2026-05-26 (user estimate)
**Last updated:** 2026-06-02
**Last audit:** 2026-06-02 — [[Session-Log/2026-06-02-bridges-audit]]
**Owner:** human (you) — primary, with orchestrator (me) for vault tracking
**Services in scope:** [[Tenant Application Service]] + [[SaaS Administration Service]] (some bridge work touches both)

---

## Goal
Get the voice bridges testable end-to-end. Each bridge is a thin adapter layer between TrueVow's call flow and a specific voice infrastructure provider (LiveKit, Cartesia, AssemblyAI, Groq, Dograh, Gemini Live). When a call comes in, the right bridge(s) handle STT → LLM → TTS → transport. "Done" = all 6 bridges can run a test call successfully.

## In Scope

### Bridges (6, per user 2026-06-02)
- **LiveKit bridge** — WebRTC transport
- **Cartesia bridge** — TTS / voice synthesis
- **Assembly bridge** — AssemblyAI STT / speech-to-text
- **Groq bridge** (xAI) — LLM inference (fast inference provider)
- **Dograh bridge** — voice workflow orchestration (Dograh fork in repo)
- **Gemini Live bridge** — Google's real-time voice

## Per-Bridge Status (from audit 2026-06-02)

### 1. xAI/Groq Bridge — ✅ STABLE ON MAIN
- **Tests:** 24/24 battery passing, permanent regression
- **Branch:** main (commit `314cdf6`, squash-merged 2026-06-02)
- **Deployed:** local (port 3023, grok_demo.html)
- **Last session:** 2026-06-02 — P0/P1 fixes (tool name, sample rate, VAD, AGC, dead code)
- **Risks:** none known

### 2. Cartesia Bridge — ✅ STABLE SINCE 2026-05-31
- **Tests:** 16/16 intake, 0 loops on edge cases
- **Branch:** main
- **Deployed:** GitHub push auto-deploy (`truevow_test_cartesia_voice_agent_usa`)
- **Last session:** 2026-05-31 — architecture separation, 852-line standalone routing
- **Known issue:** B1 (three-criteria PI reasoning) missing from routing prompt — low priority
- **Known issue:** Ngrok URL changes on restart; need to update `TENANT_API_URL`

### 3. AssemblyAI Bridge — ⚠️ MOST ACTIVE, EXPERIMENT OPEN
- **Tests:** 50/50 main (22 routes + 25 bridge + 3 persistence)
- **Branch:** main (Phases 1-3) + `experiment/assemblyai-toolcall-engine` (Phase 4, untested)
- **Deployed:** local (port 3022, voice_agent_demo.html)
- **Last session:** 2026-06-02 — 4 phases in one session
- **Experiment:** Phase 4 tool-call engine proxy — creative backdoor to route Voice Agent through 108-node WorkflowEngine. Untested.
- **Risks:** Phase 4 relies on LLM reliably calling `process_input` tool — unverified
- **Known issue:** Windows + OneDrive pytest imports hang (pre-existing)

### 4. Dograh Bridge — ✅ DEPLOYED, FLY.IO LIVE
- **Tests:** 39/39 passing
- **Branch:** `experiment/dograh-twilio-consolidate` (3 commits ahead of main) — **NOT yet squash-merged to main**
- **Deployed:** Fly.io (`truevow-dograh`, machine `78494d3c994998`), Call #92 verified (3.7s latency)
- **Last session:** 2026-06-02 — P0 webhook fix + Twilio TURN + voice-stuck fix
- **Risks:** Production code is on experiment branch, not main — release-readiness gap
- **Pending:** C15 `strip("._-@")` → `strip("._-")` (trivial)

### 5. Pipecat Bridge — ✅ DEPLOYED, FLY.IO LIVE
- **Tests:** 17/17 engine + 15/15 workflow + 11/11 router = 100% by BRIDGE_DIFFERENCE_REPORT
- **Branch:** main (C4+C10) + `experiment/dograh-twilio-consolidate` (ICE fix)
- **Deployed:** Fly.io (`truevow-pipecat` + `truevow-pipecat-v2`), 5 ICE servers live (2 STUN + 3 TURN)
- **Last session:** 2026-06-02 — Track A+B cleanup + Pipecat 1.3.0 ICE fix
- **Risks:** P2 Spanish routing issues ("inmigración" error, car accident misroute)
- **Security:** TURN script creds verified NOT leaked (.env.local + Fly secrets clean)

### 6. LiveKit Bridge — ✅ ACTIVE (2026-06-03 SESSION TODAY)
- **Tests:** 26/26 (per 2026-06-01 session)
- **Repo:** lives in `app/services/voice/livekit_agent/` inside Tenant App (NOT separate repo — my earlier claim was wrong)
- **Agent version:** `fZpe9rdUSu8v` (deployed 2026-06-03T02:45Z)
- **Deployed:** LiveKit Cloud (`truevow-legal-intake`, project `p_3lg6wdz6npb`) + ngrok tunnel to `:3022`
- **Last session:** 2026-06-03 — 3 tasks: stable ngrok URL, `gemini_v2.py` pre-warming fix, SIP trunk wired
- **Known issue:** ngrok URL changes on restart; Fly.io deploy attempted but blocked by Depot builder permissions
- **Known issue:** Twilio `<Gather>` times out through loopback
- **SIP trunk:** `ST_C4pr2q8b6Hnb`, dispatch `SDR_QCFE8ro6pUzS`, URI `sip:3lg6wdz6npb.sip.livekit.cloud`
- **Security alert:** `lk agent update-secrets` CLI bug dumps `.env.local` content on invalid character — avoid command

### Bridge-By-Session Matrix (last week)

| Date | xAI/Groq | Cartesia | AssemblyAI | Dograh | Pipecat | LiveKit | SaaS Admin |
|------|----------|----------|------------|--------|---------|---------|------------|
| 2026-05-28 | — | — | — | ✅ adapter | — | — | ✅ TASK 17 Dograh integration + 4 tenants |
| 2026-05-29 | — | — | ✅ bridge built | ✅ sync fix | ✅ bridge built (3 modes) | — | ✅ VOICE BRIDGE EXPANSION: 6 types, 7 tenants |
| 2026-05-31 | — | ✅ sep'n + harden | — | — | — | — | — |
| 2026-06-01 | ✅ demo stable | — | ✅ demo + call log | — | — | ✅ full session (10 layers, B1, 26 tests) | — |
| 2026-06-02 | ✅ P0/P1 fix | — | ✅ 4 phases | ✅ deploy + fix | ✅ cleanup + ICE | — | ✅ TASK 19 Cartesia deployed |
| 2026-06-03 | — | — | — | — | — | ✅ 3 tasks (ngrok, pre-warm, SIP) | — |

### SaaS Admin — Bridge Configuration Side

SaaS Admin is the admin dashboard where each law firm's bridge type is configured. Key work:

| Date | What | Details |
|------|------|---------|
| 2026-05-28 | TASK 17: Dograh Bridge Integration | Adapter fixes (list URL, sourceHandle/targetHandle, add_global_prompt). 4 test tenants created with per-tenant bridge assignments. Added `voice_bridge_type` to tenant config endpoint. |
| 2026-05-29 | TASK 18: Voice Bridge Expansion | 6 bridge types configured (dograh, gemini, deepgram, assemblyai, groq, pipecat). 7 test tenants with per-tenant assignments. Dograh sync() fix — now sends full workflow_configurations. |
| 2026-06-02 | TASK 19: Cartesia Bridge Deployed | Added `cartesia` to supported types. Seeded `oakwood-law-firm-cartesia` tenant. Created standalone bridge service (`deploy/cartesia/`) deployed to `truevow-cartesia.fly.dev` (2 machines HA). Cloud E2E passed: 3-turn conversation. |

Test tenants seeded in SaaS Admin:
- `oakwood-law-firm-cartesia` (Cartesia Sonic 3.5 + Benjamin voice)
- `oakwood-law-firm-assemblyai` (U3 Pro streaming STT)
- `oakwood-law-firm-groq-voice` (xAI/Groq inference)
- `oakwood-law-firm-pipecat` (dual transport: Twilio + Daily)
- `oakwood-law-firm-livekit` (LiveKit Cloud agent)
- Plus earlier: gemini, dograh, deepgram tenants

## Shared Engine Changes (affect all bridges)

| Date | Rule | What | Benefits |
|------|------|------|----------|
| 2026-06-02 | C4 | No-injury regex matches contractions | `didn't...injur`, `wasn't...hurt`, `never...injur`, `I'm fine...my car...damaged` |
| 2026-06-02 | C10 | Terminal guard in `process_input()` | Saves 1-5s by detecting terminal nodes before LLM call |

Both applied to `intake_engine/workflow/workflow_engine.py` — commit `b99eff9`. Engine now 17/17.

## Cross-Cutting Patterns (Updated 2026-06-03)

1. **Branch-per-experiment → squash-merge** — `experiment/<name>` → work + test → squash-merge to main → delete branch.
2. **Twilio TURN consolidation** — Dograh, Pipecat both pivoted from coturn → Twilio NTS.
3. **BRIDGE_CHANGES_FOR_OTHER_AGENTS.md** — Cross-bridge learning sync pattern.
4. **B1 three-criteria PI reasoning** — LiveKit + Pipecat + AssemblyAI have it. Cartesia missing.
5. **Groq single-provider consolidation** (NEW 2026-06-03) — Pipecat bridge switching from Deepgram STT + Cartesia TTS to Groq for everything (Whisper STT, TTS, LLM routing). Deepgram/Cartesia kept as fallback only.
6. **Greeting system overhaul** (NEW 2026-06-03) — Emergency 911, firm name substitution, returning client flow, branch routing. Affects ALL bridges.
7. **Shared engine #1/#3/#4/#5 fixes** (NEW 2026-06-03) — Consulting pre-check, noise gate hardening, email retry, context aggregation. 5 commits.

## Unverified Claims (from audit — 1 verified, 4 still open)

| # | Claim | Source | Risk | Status |
|---|-------|--------|------|--------|
| 1 | Dograh experiment branch is deployed to Fly.io, not main | DOGRAH_PROGRESS_LOG.md | Medium | ✅ **VERIFIED** — 4 dograh-specific commits on experiment not on main: P0 webhook fix (032f4fd), voice-stuck fix (8871bff), 2 docs (fb76e3f, 808c66f). Merge-base is 314cdf6. |
| 2 | Pipecat 1.3.0 API changes fully absorbed | PROGRESS_LOG.md | Low | Open |
| 3 | AssemblyAI Phase 4 tool-call engine proxy works | PROGRESS_LOG.md | Medium | Open |
| 4 | Cartesia B1 missing is low-priority | Cartesia diff report | Low | Open |
| 5 | LiveKit 26 tests all pass | PROGRESS_LOG.md (2026-06-01) | Low-ish | Open (but PROGRESS_LOG now confirmed, LiveKit actively worked on today) |

## Tracking Workflow (Git Hook — SET UP 2026-06-03)

- **Post-commit hook:** `.git/hooks/post-commit` → calls `post-commit-log.ps1`
- **Output:** `Projects/tenant-app-bridges/git-commits.jsonl` — one JSON line per commit: `{sha, branch, message, files, timestamp, author}`
- **Reconciliation:** `Skills/daily-checkin.md` reads `.jsonl` and cross-references with user's daily message
- **Graceful degradation:** If vault is missing, hook writes to `$TEMP/truevow-git-hook-errors.log` — never blocks a commit

## Sub-Agents
| Tool | Role | Tasks |
|---|---|---|
| opencode (me) | Orchestrator | Vault tracking, git hook monitor, daily check-in processing, blocker surfacing |
| VSCode | Code editor (user's main surface) | All coding, file edits, test runs |
| Chrome browser | Test surface | End-to-end bridge testing, call flow verification |

## Workstreams
| Stream | Owner | Status | Last updated |
|---|---|---|---|
| Integration — TrueVow ↔ bridges | you | in progress (1 week) | 2026-06-02 |
| Test suites — local pytest | you | in progress (all 6 bridges have passing suites) | 2026-06-02 |
| Stabilization — error handling | you | in progress | 2026-06-02 |
| Feature work | you | in progress | 2026-06-02 |
| Cleanup / refactor | you + orchestrator | in progress | 2026-06-02 |
| Vault tracking + session logs | orchestrator (me) | active | 2026-06-02 |

## Recent Decisions
- 2026-06-02 — Decision — created `Projects/` directory + tracking workflow — Profit: + (faster onboarding)
- 2026-06-02 — Decision — Q9 — defer Tenant App cleanup until bridges all-green — Profit: neutral
- 2026-06-02 — Decision — Q10 — restart Platform Analytics (port 3071 live) — Profit: + (unblocks Financial Mgmt)
- 2026-06-02 — Decision — Q11 — no git init on Agent/ folder — Profit: neutral
- 2026-06-02 — Decision — Q12 — build voice-friendly skills — Profit: + (faster capture)
- 2026-06-02 — Decision — Q7 — build 6 new skills — Profit: + (reusable procedures)

## Test Results
- 2026-06-02 — xAI battery — 24/24 pass — commit 314cdf6
- 2026-06-02 — Dograh full suite — 39/39 pass — experiment branch
- 2026-06-02 — Pipecat diff report — 17/17 engine, 15/15 workflow, 11/11 router
- 2026-06-02 — AssemblyAI routes + bridge + persistence — 50/50 pass (main)
- 2026-05-31 — Cartesia intake — 16/16 pass, 0 loops
- 2026-06-01 — LiveKit agent — 26/26 pass (unverified by orchestrator)

## Blockers
- (no current blockers — all 6 bridges testable)
- Phase 4 AssemblyAI tool-call engine proxy is an experiment, not blocking main work

## Recent Completions
- 2026-06-03 — Cross-bridge propagation: greeting overhaul instructions sent to Cartesia, LiveKit, Gemini Live (commit `7e1fe09`)
- 2026-06-03 — LiveKit: ngrok URL, pre-warming fix, SIP trunk — agent fZpe9rdUSu8v
- 2026-06-02 — SaaS Admin: TASK 19 Cartesia bridge deployed to truevow-cartesia.fly.dev (2 machines HA)
- 2026-06-02 — xAI P0/P1 fixes (tool name, sample rate, VAD, AGC, dead code) — pass (24/24) — commit 314cdf6
- 2026-06-02 — Dograh deploy to Fly.io (webhook fix + TURN + voice-stuck) — pass (39/39) — Call #92 verified
- 2026-06-02 — Pipecat cleanup + Pipecat 1.3.0 ICE fix — pass (100% rules) — 5 TURN servers live
- 2026-06-02 — AssemblyAI 4-phase session (routes → tests → persistence → toolcall-engine) — 50/50 main
- 2026-06-02 — Shared engine C4 + C10 fixes — 17/17 engine rules — benefits all bridges

## Propagation In Flight
| Propagation | Source | Sent | Cartesia | LiveKit | Gemini Live | Verified |
|-------------|--------|------|----------|---------|-------------|----------|
| Greeting overhaul | `f6a755d` | 2026-06-03 | 🔄 pending | 🔄 pending | 🔄 pending | ⏳ check on reconnect |

## Completed Propagations
- (first one in flight)

## Next Milestones
- [ ] Read LiveKit repo for full status
- [ ] Read SaaS Admin repo further for bridge config docs
- [ ] Verify Dograh experiment branch vs main (git log)
- [ ] Test AssemblyAI Phase 4 tool-call engine proxy with live call
- [ ] Add B1 to Cartesia routing prompt (low-priority gap)
- [ ] Squash-merge Dograh consolidation branch to main when ready
- [ ] Set up git hook for hybrid tracking workflow
- [ ] When all bridges green-lighted → Tenant App cleanup

## Sales Ops — Open-Source Roadmap (Next Pipeline)

| Priority | Task | Effort | Status |
|----------|------|--------|--------|
| P0 | Verify external scrapers (ports 3002-3005) are running — if not, build Playwright Google Maps scraper | 300-500 lines | ⏳ Pending |
| P0 | Wire domain→email discovery: extend `email-pattern-service.ts` + wire to contact-enricher | 200-300 lines | ⏳ Pending |
| P1 | Add multi-turn conversation memory (new Supabase table + Claude context injection) | 300-500 lines + 1 migration | ⏳ Pending |
| P1 | Build client-facing chat widget (embeddable React, routable through WorkflowEngine) | 400-600 lines | ⏳ Pending |
| P1 | Unified cross-channel inbox (merge email/SMS/WhatsApp timelines per lead) | 200-400 lines | ⏳ Pending |

Ref: `docs/OPEN_SOURCE_ROADMAP.md` in Sales Ops repo

## Related
- [[Session-Log/2026-06-02-bridges-audit]] — comprehensive audit of 15 sessions
- [[Session-Log/2026-06-02-bridges-intake]] — session that created this page
- [[Session-Log/2026-06-02-skills-extraction-audit]] — skills work from today
- [[Code-Maps/truevow-tenant-application-service]] — current structure map (stale, 2026-05-29)
- [[REPO-MAP]] — service inventory
- [[Skills/]] — 16 procedures used in this work
- [[.triage.yaml]] — pipeline contract

## Gate Record
- Proposed: 2026-06-02 (create `Projects/tenant-app-bridges.md` + intake last week's work)
- Path: structural change (new `Projects/` directory)
- Score: severity=15/25, frequency=20/20, agent_solvable=18/20, profit_impact=18/20, strategic_fit=15/15 = 86/100
- Verdict: APPROVED
- Fulfilled: project page created, 5 session logs written, 6 skills built, 1 comprehensive audit, 2 background tasks done
