# Skills Directory
## 21 skills across 9 functions

| Directory | Function | Skills |
|-----------|----------|--------|
| infrastructure | Logging, syncing, indexing | vault-log, write-session-log, sync-and-index |
| context | Service knowledge, vector search | load-service-context, run-vector-search |
| governance | Fiduciary rules, sub-agent protocol | check-sub-agent-work, score-proposal, run-gate, fiduciary-challenge |
| pipeline | Lead processing, community affinity | pipeline-e2e, community-affinity-gate |
| decisions | ADRs, incidents | propose-adr, write-incident |
| feedback | Pattern detection, audits | detect-recurring-blocker, audit-week-of-sessions |
| communication | Daily checkins, blockers, completions | daily-checkin, log-blocker, log-task-completion |
| qa | Test results | log-test-result |
| maintenance | Repo handoff, bridge changes | clean-repo-for-handoff, propagate-cross-bridge-changes |

## Tool scripts
- `vault-log.py` — Live JSONL logger (in Skills/ root)

## Rule
Every skill file must have a "Learned" section that gets appended with new lessons. Skills are living documents, not static references.
