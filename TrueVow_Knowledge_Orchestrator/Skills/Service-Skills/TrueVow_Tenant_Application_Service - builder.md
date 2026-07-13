---
source: TrueVow_Tenant_Application_Service/.opencode/skills/builder/SKILL.md
service: TrueVow_Tenant_Application_Service
type: core-platform
stack: ["python-fastapi", "cloudflare-workers", "postgresql", "docker"]
imported: 2026-06-30T22:32:04.884077+00:00
skill_name: builder
---
# Tenant Application Builder

## Description
Implements planned tasks for the core Tenant Application platform, following established patterns.

## Workflow
1. Receive implementation plan from architect
2. Search codebase for existing patterns
3. Implement changes following established conventions
4. Report progress back to architect

## Rules
- Follow directory structure conventions in AGENTS.md and DEVELOPMENT_METHODOLOGY.md
- Never bypass security rules or invent new top-level directories
- Run truth commands before marking work DONE
- Record decisions in memory via `memory.py remember`

## Ecosystem Integration
This skill is registered in config.yaml. Dispatch routes implementation tasks here.
