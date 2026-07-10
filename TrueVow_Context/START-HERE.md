# TrueVow — START HERE (CTO Second Brain)

> The one file to point any AI, agent, or new developer at first. Read this and the four context files below, and you know TrueVow without anyone re-explaining it.
>
> **Principle:** the AI is disposable; this context is the durable asset. Any model (opencode, Claude, Gemini, ChatGPT) pointed at `TrueVow_Context/` becomes the TrueVow CTO's second brain. This kills the "friction tax" — no re-explaining the platform every session, no re-discovering it from scratch across repos.

## Read in this order
1. **`about-truevow.md`** — what TrueVow is and the product pipeline (2 min).
2. **`platform-map.md`** — the services, trust domains, stack, owners, ports.
3. **`canonical-decisions.md`** — the binding contracts you must not violate.
4. **`voice-and-standards.md`** — who we build for, how we write, how we code.
5. **`memory-digest.md`** — the shared brain, auto-generated from `memory.db`.

## This is an index, not a copy
Each file is a curated summary that points to the **source of truth** (`config.yaml`, the ADRs, `memory.db`, per-service `docs/00-Planning/*-Agent-Coding-Instructions.md`). Follow the source link when in doubt. If a fact here is stale, **fix the source first, then re-derive** — never let this become a 6th drifting copy (that drift is exactly what ADR-005 and the config-note fix were about).

## Session bootstrap (every agent, every session)
```
python TrueVow_Shared_Orchestration/orchestrator.py sync-memory
python TrueVow_Shared_Orchestration/orchestrator.py scan-services
python TrueVow_Shared_Orchestration/orchestrator.py dispatch "<the task>"
python TrueVow_Shared_Orchestration/orchestrator.py agent-checkin start "<service>: <task> | goal: <what success looks like>"
```
End of session:
```
python TrueVow_Shared_Orchestration/orchestrator.py agent-checkin done "<service>: <done> | outcome | learned | next" --status DONE
python TrueVow_Shared_Orchestration/orchestrator.py push-memory
```
**A task is not done until the check-in is posted. Intent is not completion.** (RULE 0 — no fabrication; see `canonical-decisions.md`.)

## Keep the brain fresh
- Regenerate the memory digest: `python TrueVow_Shared_Orchestration/memory.py export`
- Store a decision: `python TrueVow_Shared_Orchestration/memory.py remember <category> "<title>" "<content>" --importance N`
- Recall live detail: `python TrueVow_Shared_Orchestration/memory.py recall "<topic>"`

_Curated 2026-07-10. Maintained by the orchestrator CTO agent._
