# TrueVow Agent Ecosystem

> **Skills are the new apps.** Harness-agnostic. Pure files + CLI. Works with any coding agent.

When an agent begins work on this codebase, it should:

## 1. Load Context
- Run `python TrueVow_Shared_Orchestration/orchestrator.py memory-summary` to see what the project remembers
- Run `python TrueVow_Shared_Orchestration/orchestrator.py list` to see available skills

## 2. Auto-Dispatch: Map Intent → Skill → Persona
**Before doing any work**, the agent must run:
```
python TrueVow_Shared_Orchestration/orchestrator.py dispatch "<user's request>"
```
This auto-maps the user's intent to the right skill + persona and prints the full SKILL.md.
The agent must then **follow the SKILL.md instructions exactly** — never partially.

## 3. Dispatch Table (for quick reference)
| User says... | Skill loaded | Persona activated |
|-------------|-------------|-------------------|
| "review this code" / "PR review" | code-review-and-quality | code-reviewer |
| "write tests" / "test coverage" | test-driven-development | test-engineer |
| "security audit" / "vulnerability" | security-and-hardening | security-auditor |
| "performance / slow / optimize" | performance-optimization | web-performance-auditor |
| "ship / launch / deploy" | shipping-and-launch | code-reviewer + security-auditor + test-engineer (parallel fan-out) |
| "new feature / spec / define" | spec-driven-development | — |
| "plan / breakdown / tasks" | planning-and-task-breakdown | — |
| "implement / build / develop" | incremental-implementation | — |
| "bug / broken / debug / fix" | debugging-and-error-recovery | — |
| "simplify / refactor / messy" | code-simplification | — |
| "api / endpoint / contract" | api-and-interface-design | — |
| "ui / frontend / component" | frontend-ui-engineering | — |
| "search web / research / twitter" | agent-reach | — |

## 4. Remember Everything
After important decisions, architecture changes, bug discoveries:
```
python TrueVow_Shared_Orchestration/memory.py remember <category> "<title>" "<content>" --importance 8
```
Categories: architecture, pattern, decision, dependency, convention, bug, context, todo, relationship

## 5. Work Incrementally
- One thin vertical slice at a time
- RED → GREEN → REFACTOR → COMMIT
- Never skip the test

## 6. Review Before Shipping
- Five-axis review: correctness, readability, architecture, security, performance
- Scan skills before installing: `skillspector scan TrueVow_Shared_Agent_Tools/agent-skills/skills/ --recursive`

## Available Commands
| Command | Purpose |
|---------|---------|
| `python TrueVow_Shared_Orchestration/orchestrator.py doctor` | Full ecosystem diagnostic |
| `python TrueVow_Shared_Orchestration/orchestrator.py list` | List all skills + personas |
| `python TrueVow_Shared_Orchestration/orchestrator.py dispatch "<request>"` | Auto-map intent → skill + load SKILL.md |
| `python TrueVow_Shared_Orchestration/memory.py summarize` | Memory database summary |
| `python TrueVow_Shared_Orchestration/memory.py remember <cat> <title> <content>` | Store a memory |
| `python TrueVow_Shared_Orchestration/memory.py recall <query>` | Search memories |
| `python TrueVow_Shared_Orchestration/obsidian-bridge.py` | Sync to Obsidian vault |
| `agent-reach doctor` | Check web channel status |
| `skillspector scan <path>` | Security scan a skill |

## All Registered Agents
- **4 Personas:** code-reviewer, test-engineer, security-auditor, web-performance-auditor
- **24 Lifecycle Skills:** DEFINE → PLAN → BUILD → VERIFY → REVIEW → SHIP
- **2 Tool Skills:** agent-reach (web), skillspector-guardrail (security)
- **Sub-repo agents:** agent-skills AGENTS.md, Agent-Reach CLAUDE.md, SkillSpector README

## Obsidian Vault
All knowledge syncs to `TrueVow_Knowledge/`. Run `python TrueVow_Shared_Orchestration/obsidian-bridge.py` to update.
