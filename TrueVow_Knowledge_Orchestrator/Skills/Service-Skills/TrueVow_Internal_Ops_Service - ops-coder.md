---
source: TrueVow_Internal_Ops_Service/.opencode/skills/ops-coder/SKILL.md
service: TrueVow_Internal_Ops_Service
type: internal-operations
stack: ["python-fastapi", "nextjs", "elk", "docker"]
imported: 2026-06-30T22:32:05.128005+00:00
skill_name: ops-coder
---
# Internal Ops Coder

## Description
Implements planned tasks for Internal Operations, following established patterns and conventions.

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
