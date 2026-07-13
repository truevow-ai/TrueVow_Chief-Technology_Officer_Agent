---
source: TrueVow_Sales_Ops_Service/.opencode/skills/sales-architect/SKILL.md
service: TrueVow_Sales_Ops_Service
type: crm
stack: ["nextjs", "typescript", "postgresql", "supabase"]
imported: 2026-06-30T22:32:04.868628+00:00
skill_name: sales-architect
---
# Sales Ops Architect

## Description
Plans CRM features, validates against architecture, creates implementation specs for Sales Ops (5-Factory Multi-Agent CRM).

## Workflow
1. Load context from AGENTS.md and working cache
2. Analyze the request against existing architecture
3. Create a detailed implementation plan with file paths and tasks
4. Delegate to coder for implementation

## Rules
- Never modify code directly — plan first, delegate implementation
- Validate all decisions against AGENTS.md service-specific rules and 8 Immutable Pipeline Phases
- Record architecture decisions in memory via `memory.py remember`

## Ecosystem Integration
This skill is registered in config.yaml. Dispatch routes architecture tasks here.
