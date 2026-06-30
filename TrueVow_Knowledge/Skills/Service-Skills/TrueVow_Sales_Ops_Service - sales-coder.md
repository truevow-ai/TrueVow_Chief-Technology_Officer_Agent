---
source: TrueVow_Sales_Ops_Service/.opencode/skills/sales-coder/SKILL.md
service: TrueVow_Sales_Ops_Service
type: crm
stack: ["nextjs", "typescript", "postgresql", "supabase"]
imported: 2026-06-30T22:32:04.872813+00:00
skill_name: sales-coder
---
# Sales Ops Coder

## Description
Implements planned tasks for Sales Ops (5-Factory Multi-Agent CRM), following established patterns.

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
