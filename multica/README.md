# Multica Self-Hosted — Agent Execution Layer

Location: `multica/` in the CTO agent repo (platform infra).
Runs as a platform service: Next.js UI + Go backend + PostgreSQL + pgvector.

**Start (self-host quickstart):**
```bash
cd multica
curl -fsSL https://raw.githubusercontent.com/multica-ai/multica/main/scripts/install.sh | bash -s -- --with-server
multica setup self-host
# → http://localhost:3000
```

## What Multica does vs. what the orchestrator does

| Layer | Tool | Job |
|---|---|---|
| **Discovery + Routing** | TrueVow Orchestrator | `scan-services`, `dispatch`, `agent-checkin`, `truth-loop`, stickiness/perception |
| **Execution + Tracking** | Multica | Agents pick up tasks, write code, report blockers, compound skills, post PRs |
| **Agent skills/personas** | agency-agents (selective) | Pre-built engineer personalities loaded into Multica agents |

The orchestrator says "TRACE-ocr migration: swap deepdoctection → PaddleOCR". Multica's agent picks it up, opens the repo, writes code, posts a PR, and marks the issue done. The orchestrator then `truth-loop`s the result.

## TrueVow integration
- **Shared memory is the handoff:** the orchestrator writes tasks via `memory.py`; Multica agents read the board.
- **Per-repo agent mapping:** TRACE gets a TRACE-agent, Billing gets a Billing-agent, etc.
- **Skills compound across repos:** a bug found in TRACE becomes a reusable skill for SETTLE's pipeline.

## Per-repo agent assignment
| Repo | Multica agent | Loaded agency-agent |
|---|---|---|
| TRACE | `trace-coder` | Backend Architect, Code Reviewer, Security Auditor |
| INTAKE | `intake-coder` | AI Engineer, Voice AI Integration Engineer, Code Reviewer |
| SETTLE | `settle-coder` | Database Optimizer, Backend Architect |
| Billing | `billing-coder` | Backend Architect, Security Auditor, Database Optimizer |
| SaaS Admin | `saas-admin-coder` | Backend Architect, Frontend Developer |
| Sales Ops | `sales-ops-coder` | Data Engineer, AI Engineer |
