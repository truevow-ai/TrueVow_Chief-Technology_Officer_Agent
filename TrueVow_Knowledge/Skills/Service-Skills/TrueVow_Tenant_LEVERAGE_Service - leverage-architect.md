---
source: TrueVow_Tenant_LEVERAGE_Service/.opencode/skills/leverage-architect/SKILL.md
service: TrueVow_Tenant_LEVERAGE_Service
type: rules-engine
stack: ["python-fastapi", "nextjs", "postgresql", "alembic"]
imported: 2026-06-30T22:32:05.074973+00:00
skill_name: leverage-architect
---
# LEVERAGE Architect

## Description
Plans features, validates against architecture, creates implementation specs for LEVERAGE (3-Tier Rules Engine).

## Workflow
1. Load context from AGENTS.md and working cache
2. Analyze the request against existing architecture
3. Create a detailed implementation plan with file paths and tasks
4. Delegate to coder for implementation

## Rules
- Never modify code directly — plan first, delegate implementation
- Validate all decisions against AGENTS.md service-specific rules
- LEVERAGE is a 3-tier rules engine — NO AI component
- Record architecture decisions in memory via `memory.py remember`

## Ecosystem Integration
This skill is registered in config.yaml. Dispatch routes architecture tasks here.
