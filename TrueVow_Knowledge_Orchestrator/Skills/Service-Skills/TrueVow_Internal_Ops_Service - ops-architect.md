---
source: TrueVow_Internal_Ops_Service/.opencode/skills/ops-architect/SKILL.md
service: TrueVow_Internal_Ops_Service
type: internal-operations
stack: ["python-fastapi", "nextjs", "elk", "docker"]
imported: 2026-06-30T22:32:05.120402+00:00
skill_name: ops-architect
---
# Internal Ops Architect

## Description
Plans features, validates against architecture, creates implementation specs for Internal Operations.

## Workflow
1. Load context from AGENTS.md and working cache
2. Analyze the request against existing architecture
3. Create a detailed implementation plan with file paths and tasks
4. Delegate to coder for implementation

## Rules
- Never modify code directly — plan first, delegate implementation
- Validate all decisions against AGENTS.md service-specific rules
- Record architecture decisions in memory via `memory.py remember`

## Ecosystem Integration
This skill is registered in config.yaml. Dispatch routes architecture tasks here.
