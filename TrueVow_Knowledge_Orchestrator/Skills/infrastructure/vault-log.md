# vault-log
## Function: Infrastructure
## Trigger: Any action — file write, decision, blocker, subagent launch, task start/end
## Who: All agents

Write structured JSONL entries to `Session-Logs/live/{date}.jsonl`.

```
python TrueVow_Knowledge/Skills/vault-log.py --agent <id> --action <type> --detail "<desc>" --service <name>
```

**Actions**: task-start, task-complete, task-fail, file-read, file-write, decision, blocker, question, subagent-launch, subagent-result, commit, deploy, session-start, session-end, heartbeat

**Tags**: VERIFIED, COMPILED, SCAFFOLDED, UNTESTED, ASSUMED

## Learned (2026-06-18)
- 2 entries in 11 hours is unacceptable. Minimum: 1 entry per sub-agent interaction.
- Every sub-agent launch AND result must be logged.
- Monitoring system is worthless if not used.
