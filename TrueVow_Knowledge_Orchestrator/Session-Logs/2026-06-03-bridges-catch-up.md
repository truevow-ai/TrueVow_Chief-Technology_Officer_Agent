# Audit Catch-Up — 2026-06-03: Tenant App Bridges Activity (Since Last Audit)

**Sub-agent:** Orchestrator
**Date:** 2026-06-03
**Status:** ✅ Caught up on 10 commits + 20 uncommitted files across 7 bridges
**Trigger:** User asked "are you following all the work being done at the tenant app repo" — I was NOT. This corrects that.

---

## Focus
Catch up on all bridge work in Tenant App since my last audit (~15 hrs ago). 10 commits applied, 20 files with uncommitted changes across 7 bridges.

## What I Missed

### Committed (last 10 commits on main)

| Commit | What | Impact |
|--------|------|--------|
| `16936d1` (2 min ago) | BRIDGE_GREETING_UPDATE — new greeting + emergency + firm name | All bridges |
| `3710c55` (16 min ago) | greeting update — branch routing, emergency 911, returning client flow + bridge instructions | All bridges |
| `9e088fd` (5 hrs ago) | fix(#4): stronger noise gate — legal-keyword filter for short inputs | Shared engine |
| `9154566` (6 hrs ago) | fix(#3,#5): email retry count fixed + per-field context aggregation | Shared engine |
| `0984c8f` (7 hrs ago) | fix(#4): stricter noise gate — reject STT artifacts + background chatter | Shared engine |
| `77ecc80` (7 hrs ago) | fix(#3,#5): email retry limit + contact context aggregation | Shared engine |
| `9faf4b2` (7 hrs ago) | fix(#1): consulting pre-check — 'speaking to' no longer misroutes to transferring | Shared engine |
| `cb934e1` (7 hrs ago) | feat: show per-turn latency in demo transcript | Demos |
| `186b857` (15 hrs ago) | fix: Bug #1 — sequence node stale user_text (from handoff) | Simple bridge |
| `e9b65a9` (before that) | experiment: use LLM response for ALL nodes in simple bridge | Simple bridge |

### Uncommitted (20 files, 941 insertions, 12610 deletions)

| File | Lines | What Changed |
|------|-------|-------------|
| `pipecat_voice/server/main.py` | +146 | **Major: switched from Deepgram/Cartesia to Groq** (single-provider STT+TTS+LLM). Added FIRM_NAME for greeting. Deepgram/Cartesia keys kept as fallback only. |
| `pipecat_voice/server/Dockerfile_v3` | +6 | Updated for Groq provider |
| `pipecat_voice_demo.html` | +143 | Updated demo for Groq provider |
| `livekit_agent/agent_cloud.py` | +26 | New ngrok URL (`7252-...`), removed google plugin import, added TurnHandlingOptions |
| `gemini_live/gemini_live_bridge.py` | +75 | Bridge updates |
| `intake_engine/normalizer/response_normalizer.py` | +66 | Normalizer improvements |
| `intake_engine/workflow/workflow_engine.py` | +18 | Workflow engine updates |
| `grok_demo.html` | +34 | Grok demo improvements |
| `cartesia/softphone/index.html` | +310 | Cartesia softphone overhaul |
| `cartesia/softphone/softphone_server.py` | +243 | Cartesia softphone server overhaul |
| `dograh/server/fly.toml` | +2 | Dograh deploy config tweak |
| `dograh/server/ui/next.config.ts` | +35 | Dograh UI config |
| `dograh/server/ui/package.json` | +12 | Dograh UI deps |
| `dograh/server/ui/pnpm-lock.yaml` | -11009 | **Deleted pnpm-lock** |
| `dograh/server/ui/src/app/layout.tsx` | +6 | Dograh UI layout |
| `dograh/server/ui/src/instrumentation.ts` | +15 | Dograh UI instrumentation |
| `gemini_v2.py` | +32 | V2 endpoint updates |
| `app/main.py` | +8 | Route/config updates |
| `.dockerignore` | +31 | Expanded Docker ignore |

## Key Patterns

1. **Groq consolidation** — Pipecat bridge is pivoting from Deepgram STT + Cartesia TTS to Groq for everything (Whisper STT, TTS, LLM routing). This is a significant architecture simplification.

2. **Greeting overhaul** — Two commits rewriting the greeting system across all bridges: emergency 911 detection, firm name substitution, returning client flow, branch routing. Affects every bridge's first interaction with callers.

3. **Shared engine hardening** — 5 commits fixing bugs #1, #3, #4, #5 across consulting pre-check, noise gate, email retry, and context aggregation. These benefit ALL bridges using the WorkflowEngine.

4. **Cartesia softphone** — Heavy work on the standalone softphone prototype (310+243 lines changed).

## Gap Analysis

- **I had zero awareness** of these 10 commits + 20 uncommitted files until the user asked
- **My last audit** (Session-Logs/2026-06-02-bridges-audit.md) is now ~15 hours stale
- **The git hook** I installed has no commits to capture yet — it'll fire on the NEXT commit, not retroactively
- **Root cause**: I rely on explicit "tell me what happened" from the user. Sub-agents commit independently and I'm not polling.

## Decisions Made
- 2026-06-03 — Need a proactive check-in cadence. Going forward: check `git log --since="2 hours ago"` at least twice per session.

## Next Steps
- Wait for the 20-file uncommitted work to be committed, then update per-bridge status
- Add Groq consolidation to project page as a cross-cutting pattern
- Add greeting overhaul to project page
- Reindex vault after this log

## Related
- [[Projects/tenant-app-bridges]] — stale, needs update with Groq pivot + greeting overhaul
- [[Session-Logs/2026-06-02-bridges-audit]] — now ~15 hrs stale
- [[Session-Logs/2026-06-03-repo-reading-livekit-saas-admin]] — LiveKit update from earlier today
