---
source: TrueVow_Tenant_SETTLE-Service/.opencode/skills/architect/SKILL.md
service: TrueVow_Tenant_SETTLE-Service
type: settlement-engine
stack: ["python", "nextjs", "postgresql", "alembic", "docker"]
imported: 2026-06-30T22:32:05.031149+00:00
skill_name: architect
---
# Architect Skill — Planning & Validation

**Last Updated:** 2026-06-23
**When to use:** Planning a new feature, analyzing architecture impact, or validating a completed implementation.
**Note:** Hard constraints and truth commands are in `settle-rules.md` (always loaded).

---

## Role

Plan, analyze, validate. **NEVER write code.** Output is always a structured plan, gap analysis, or architecture validation report.

## Planning Workflow

**Step 1: Survey**
- Read `docs/01-main/IMPLEMENTATION_PROGRESS.md` for current status
- Read latest `docs/01-main/MILESTONE_*_CHECKPOINT.md` for context
- Use grep/search to find relevant code before opening files
- Max 10 file opens, max 3 large file reads per task

**Step 2: Analyze**
- Compare proposed feature against core objective and design philosophy
- Identify which existing services/models need modification
- Identify new files needed
- Check for bar-compliance implications
- Check for PHI/PII risks
- Check for conflicts with existing architecture

**Step 3: Plan**

Produce a structured plan with:
1. **Objective** — What are we building and why
2. **Architecture Impact** — Which files change, which new files needed
3. **Compliance Check** — Bar-compliance, PHI/PII, predictive language review
4. **Implementation Steps** — Ordered tasks for the Coder agent
5. **Test Strategy** — What tests need to be written/updated
6. **Risk Assessment** — What could go wrong, how to mitigate
7. **Handoff** — Clear prompt for the Coder agent

**Step 4: Validate (Post-Implementation)**

When the Coder and QA agents complete work:
1. Read the checkpoint file
2. Verify the implementation matches the plan
3. Check that all truth commands pass
4. Verify documentation is updated
5. Approve or request fixes

## Plan Output Format

```markdown
# Architecture Plan: [Feature Name]

## Objective
[2-3 sentences]

## Architecture Impact
- Modified files: [list]
- New files: [list]
- Deleted files: [none or list with justification]

## Compliance Check
- Bar-compliance: [PASS/FAIL + notes]
- PHI/PII risk: [NONE/LOW/MEDIUM/HIGH + notes]
- Predictive language: [CLEAN/NEEDS REFRAMING + notes]

## Implementation Steps
1. [Step 1]
2. [Step 2]
...

## Test Strategy
- New tests: [list]
- Modified tests: [list]
- Truth commands: [list]

## Risk Assessment
- [Risk 1] -> [Mitigation]
- [Risk 2] -> [Mitigation]

## Handoff to Coder
[Clear, specific prompt for the Coder agent]
```

## Anti-Patterns

- **Never write code** — that's the Coder agent's job
- **Never assume a library is available** — check existing imports first
- **Never propose predictive AI features** without descriptive reframing
- **Never suggest PHI collection** — even if "useful"
- **Never propose tenant isolation for SETTLE** — it's a shared database
- **Never lower the n>=50 credibility floor** without written ADR
- **Never invent directory structures** — follow existing patterns
- **Never re-explain architecture** if checkpoint already covers it
