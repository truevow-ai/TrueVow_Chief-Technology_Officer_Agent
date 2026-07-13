# Agent Folder — Orchestrator's Home

**Owner:** Orchestrator (me, opencode agent)
**Created:** 2026-06-02
**Purpose:** The orchestrator's own working folder. Where I document my work, log my decisions, track my own state, and surface open questions for the human.

---

## What's in this folder

| File | Purpose |
|---|---|
| `agent-log.md` | Complete chronological log of everything I've done this session (and going forward) |
| `open-questions.md` | Things waiting for the user's decision or input |
| `operational-state.md` | Current state of the system (vault stats, what's running, what's pending) |
| `changelog.md` | Per-file log of every vault modification I've made |
| `self-assessment.md` | Honest evaluation of what I did well and badly this session |

---

## Why this exists

On 2026-06-02 the user pointed out a real gap: I had built infrastructure (skills, policies, YAML, harnesses) but wasn't using it to capture the user's actual work-in-progress (the Tenant App bridges work spanning a week). The user expected me to be the central coordinator of their work, not a passive bystander.

This folder is part of the fix:
- **`agent-log.md`** = the "what did I do" record. The user shouldn't have to ask "what did you actually do today?"
- **`open-questions.md`** = the "what do I need from you" record. Surfaces decisions waiting on the human.
- **`operational-state.md`** = the "what's the current state" record. Quick read of the system.
- **`changelog.md`** = the "what files did I touch" record. Full audit trail.

---

## How I'll use it going forward

- **Every session start:** read `operational-state.md` and `open-questions.md`
- **During work:** log inline decisions to `changelog.md` (not at end)
- **End of session:** flush `agent-log.md` entry for the session + update `operational-state.md`
- **When I have a question for the user:** add to `open-questions.md`, then ASK in chat
- **When the user asks "what did you do":** point them at `agent-log.md` or this folder

---

## Related

- `Session-Logs/` — per-session time-stamped records (complement, not replacement)
- `Projects/` — active multi-session work tracking
- `Skills/` — procedures I follow
- `Templates/Agent-Harness-Orchestrator.md` — my constitution
