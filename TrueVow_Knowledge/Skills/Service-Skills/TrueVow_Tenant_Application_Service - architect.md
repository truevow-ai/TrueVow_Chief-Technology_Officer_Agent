---
source: TrueVow_Tenant_Application_Service/.opencode/skills/architect/SKILL.md
service: TrueVow_Tenant_Application_Service
type: core-platform
stack: ["python-fastapi", "cloudflare-workers", "postgresql", "docker"]
imported: 2026-06-30T22:32:04.880623+00:00
skill_name: architect
---
# Tenant Application Architect

## Description
Plans features, validates against architecture, creates implementation plans for the core Tenant Application platform.

## Workflow
1. Load context from AGENTS.md and working cache
2. Analyze the request against existing architecture
3. Create a detailed implementation plan with file paths and tasks
4. Delegate to builder for implementation

## Rules
- Never modify code directly — plan first, delegate implementation
- Validate all decisions against AGENTS.md, DEVELOPMENT_METHODOLOGY.md, and architecture docs
- Record architecture decisions in memory via `memory.py remember`

## Ecosystem Integration
This skill is registered in config.yaml. Dispatch routes architecture tasks here.
