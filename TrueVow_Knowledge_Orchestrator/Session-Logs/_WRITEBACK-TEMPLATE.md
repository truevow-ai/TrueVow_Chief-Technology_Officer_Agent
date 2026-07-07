# Agent Writeback Template

Every sub-coding agent writes back to this vault at session start and end.
The CTO orchestrator scans all services and flags any without recent activity as STALE.

## Start of Session

```bash
python ../TrueVow_Shared_Orchestration/orchestrator.py sync-memory
python ../TrueVow_Shared_Orchestration/orchestrator.py scan-services
python ../TrueVow_Shared_Orchestration/orchestrator.py agent-checkin start "<ServiceName>: <task> | from: <previous state> | goal: <success criteria>"
```

## During Session

```bash
python ../TrueVow_Shared_Orchestration/memory.py remember <category> "<title>" "<content>" --importance <1-10>
```

## End of Session

```bash
python ../TrueVow_Shared_Orchestration/orchestrator.py agent-checkin done "<ServiceName>: <accomplished> | result: <outcome> | learned: <insight> | next: <todo>" --status DONE
python ../TrueVow_Shared_Orchestration/orchestrator.py push-memory
```

## Blocked

```bash
python ../TrueVow_Shared_Orchestration/orchestrator.py agent-checkin blocked "<ServiceName>: <blocker> | tried: <attempts> | need: <unblock requirement>"
```

## Writeback Format (pipe-delimited)

Every writeback MUST follow this format:

```
<service>: <specific action> | result: <outcome> | learned: <insight> | next: <next step or blocker>
```

Example:
```
SETTLE: CA crawler Phase 2 completed — 1,880 websites crawled | result: 99% success rate, 14 throttle recoveries | learned: CourtListener needs 3s min-delay for reliability | next: load into Supabase once DNS restored
```

---

**Why this matters:** The orchestrator can only help you if it knows what you're doing.
Without writeback, your service appears DEAD on the dashboard. Don't let your service go stale.
