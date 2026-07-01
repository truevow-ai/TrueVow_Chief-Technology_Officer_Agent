# ADR-004: Multi-Developer Shared Memory via Git-Tracked SQLite

**Status:** Accepted  
**Date:** 2026-07-01  
**Deciders:** Yasha (CTO)

## Context

TrueVow has 4 developers (Yasha, Ms. Sania, Ghulam Ghaus, Ghulam Ghous) working on different services simultaneously. Each developer's coding agent needs access to the shared decisions, architecture patterns, bugs, and context that other developers have discovered. Previously, the `memory.db` SQLite database was local to Yasha's laptop with no mechanism for sharing.

The CTO orchestrator and knowledge vault (`truevow-cto-agent`) needed to be deployable to any machine — not tied to Yasha's laptop — for production deployment.

## Decision

`memory.db` is tracked in the `truevow-cto-agent` git repository. Two new orchestrator commands enable the multi-developer workflow:

1. **`sync-memory`** — Runs `git pull` on the CTO repo at session start, pulling the latest `memory.db` from all developers.
2. **`push-memory`** — Commits and pushes `memory.db` after important decisions, sharing with all developers.

`memory.py remember` now auto-stages `memory.db` for git after every write. Each entry is tagged with the developer's identity (`TRUEVOW_DEV` environment variable, falling back to `git config user.name`). The `source` column in the schema stores this attribution.

## Consequences

- **Positive:** All 4 developers share one CTO brain. Decisions compound across the team.
- **Positive:** The CTO agent is no longer tied to Yasha's laptop — it's deployable anywhere via `git clone --recursive`.
- **Positive:** No conflicts — memory entries are UUID-keyed INSERT operations. Multiple developers writing simultaneously won't conflict on merge.
- **Positive:** Developer attribution on every entry enables accountability and context.
- **Risk:** Requires the `truevow-cto-agent` repo to be accessible (GitHub) from all developer machines.
- **Risk:** Developers must remember to run `sync-memory` before work and `push-memory` after decisions. Forgetting means working with stale knowledge.

## Session Workflow

```
sync-memory → dispatch "<task>" → work → remember → push-memory → sync-obsidian
```

## Affected Components

- `TrueVow_Shared_Orchestration/orchestrator.py` — sync-memory, push-memory commands
- `TrueVow_Shared_Orchestration/memory.py` — auto-stage, developer attribution
- `TrueVow_Shared_Orchestration/config.yaml` — session startup updated
- `TrueVow_Shared_Codebase_Memory/memory.db` — git-tracked SQLite
- `AGENTS.md` — multi-developer workflow documentation
- `README.md` — full ecosystem documentation
