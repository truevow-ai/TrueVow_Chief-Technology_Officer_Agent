# write-session-log
## Function: Infrastructure
## Trigger: End of every session
## Who: All agents

Write structured session summary to `Session-Logs/{date}.md`. Include: what was done, decisions made, blocks hit, what's next. Link to ADRs, Incidents, and sub-agent handoffs.

## Learned (2026-06-18)
- Session log is the audit trail. If a sub-agent does work and it's not in the session log, it didn't happen.
- Daily reports supplement session logs — one summary per day for the human.
