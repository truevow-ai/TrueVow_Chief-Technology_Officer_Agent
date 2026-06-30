---
source: TrueVow-Tenant_Billing-Service/.opencode/skills/billing-architect/SKILL.md
service: TrueVow-Tenant_Billing-Service
type: billing
stack: ["python", "nextjs", "postgresql", "alembic"]
imported: 2026-06-30T22:32:05.315718+00:00
skill_name: billing-architect
---
# Billing Architect

## Description
Plans features, validates against architecture, creates implementation specs for Billing.

## Workflow
1. Load context from AGENTS.md and working cache
2. Analyze the request against existing architecture
3. Create a detailed implementation plan with file paths and tasks
4. Delegate to coder for implementation

## Rules
- Never modify code directly — plan first, delegate implementation
- Validate all decisions against AGENTS.md service-specific rules
- Respect billing invariants: idempotency, immutable invoices, audit trail
- Record architecture decisions in memory via `memory.py remember`

## Ecosystem Integration
This skill is registered in config.yaml. Dispatch routes architecture tasks here.
