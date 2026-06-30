# Agent Onboarding Preamble
# Drop this into any service's AGENTS.md to wire it into the ecosystem.
# The agent reads this on startup and becomes ecosystem-aware.

## Ecosystem Integration

**You are not alone.** You report to the **TrueVow Agent Ecosystem Orchestrator** (CTO).
The orchestrator is at `../TrueVow_Shared_Orchestration/orchestrator.py` (relative to this service).

### On Every Session Start
```
python ../TrueVow_Shared_Orchestration/orchestrator.py agent-checkin start "Working on <service>: <task>"
```
This registers you in the ecosystem dashboard. The CTO now knows you're active.

### Before Any Work
```
python ../TrueVow_Shared_Orchestration/orchestrator.py dispatch "<user's request>"
```
This auto-routes the task to the right skill. You MUST follow the SKILL.md it returns.

### After Every Important Decision
```
python ../TrueVow_Shared_Orchestration/memory.py remember <category> "<title>" "<content>" --importance N
```
Categories: architecture, pattern, decision, dependency, convention, bug, context, todo, relationship

### On Task Completion
```
python ../TrueVow_Shared_Orchestration/orchestrator.py agent-checkin done "<what was accomplished>" --status DONE|UNVERIFIED|BLOCKED
```
This reports your status to the CTO and updates the dashboard.

### On Error or Block
```
python ../TrueVow_Shared_Orchestration/orchestrator.py agent-checkin blocked "<what's blocking you>"
```

### Security
- Scan any new skill before installing: `skillspector scan <path> --no-llm`
- Never bypass the orchestrator — it tracks everything for the CTO

### Web Research
- Use `agent-reach` for internet lookups: `agent-reach doctor` for status

### Knowledge Sync
- All memory syncs to Obsidian: `python ../TrueVow_Shared_Orchestration/obsidian-bridge.py`

**Remember:** You have 24 lifecycle skills, 4 specialist personas, persistent memory,
web eyes, and a security guardrail. Use them. Report everything.
