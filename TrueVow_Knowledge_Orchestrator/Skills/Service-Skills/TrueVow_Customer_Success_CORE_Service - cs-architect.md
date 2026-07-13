---
source: TrueVow_Customer_Success_CORE_Service/.opencode/skills/cs-architect/SKILL.md
service: TrueVow_Customer_Success_CORE_Service
type: customer-success
stack: ["nextjs", "typescript", "postgresql", "supabase"]
imported: 2026-06-30T22:32:05.104288+00:00
skill_name: cs-architect
---
# Customer Success Architect

## Description
Plans features, validates against architecture, creates implementation specs for Customer Success Core.

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
