# Agent Harness Templates

Pick the right harness, paste it into any agent, and go.

| Template | Use When | Agent Type |
|----------|----------|------------|
| [[Agent-Harness-Service]] | Working on a specific service (code, cleanup, debugging) | Service Agent |
| [[Agent-Harness-Feedback]] | Reviewing sessions, detecting patterns, proposing ADRs | Feedback Agent |
| [[Agent-Harness-Orchestrator]] | Coordinating all work, routing tasks, fiduciary oversight | Orchestrator |

## How to Use

1. Copy the harness content
2. Replace `{{PLACEHOLDERS}}` with actual values
3. Paste into any agent's system prompt (opencode, Claude, Hermes, PI, etc.)
4. The agent will know to read from and write to `TrueVow_Knowledge/`

## Framework-Agnostic

These templates are plain markdown. No proprietary format. No lock-in. Any agent framework that can read files can use them. The only requirement: access to the `TrueVow_Knowledge/` directory.

## Companion Templates

- [[ADR]] — Architecture Decision Record
- [[Incident]] — Bug/outage record
- [[Session-Log]] — Session summary
- [[Service-Map]] — Per-service metadata
- [[Decision]] — Non-ADR decision log
