---
source: TrueVow_Tenant_LEVERAGE_Service/.opencode/skills/leverage-coder/SKILL.md
service: TrueVow_Tenant_LEVERAGE_Service
type: rules-engine
stack: ["python-fastapi", "nextjs", "postgresql", "alembic"]
imported: 2026-06-30T22:32:05.080314+00:00
skill_name: leverage-coder
---
# LEVERAGE Coder

## Description
Implements planned tasks for LEVERAGE (3-Tier Rules Engine), following established patterns.

## Workflow
1. Receive implementation plan from architect
2. Search codebase for existing patterns
3. Implement changes one thin vertical slice at a time
4. Report progress back to architect

## Rules
- Follow directory structure conventions in AGENTS.md
- Never bypass security rules or invent new top-level directories
- Run truth commands before marking work DONE
- Record decisions in memory via `memory.py remember`

## Ecosystem Integration
This skill is registered in config.yaml. Dispatch routes implementation tasks here.
