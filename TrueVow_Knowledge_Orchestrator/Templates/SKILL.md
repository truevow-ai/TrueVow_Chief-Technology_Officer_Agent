# Skill: {{SKILL_NAME}}

**Version:** 1.0
**Last reviewed:** {{date}}
**Owner(s):** {{harness or role that uses this — e.g., Orchestrator, Service-Agent, Feedback-Agent}}
**Used by:** {{which paths in .triage.yaml — e.g., incident, adr, decision}}

---

## What
One-sentence description of what this skill produces.

## When to use
Trigger conditions — what situation/pattern means "use this skill." Be specific. The sharper the trigger, the less the agent has to guess.

## Inputs
What context or data you need before executing. List the things that must already be true (e.g., "vault is indexed", "session has been logged").

## Procedure
1. Step 1
2. Step 2
3. Step 3

If the procedure has decision points, list them inline as `if X → Y, else Z`.

## Output
What you produce, in what format, and where it lands (file path, message shape, etc.).

## Example
A worked instance from a past session. If the skill is new, fabricate a realistic one and label it `(hypothetical)`.

## Improvement signals
What tells you this skill needs an update. Be specific. Examples:
- "Human frequently uses `MODIFY` on the score breakdown — the rubric dimensions are wrong."
- "Vector search returns nothing relevant 3+ times in a row — query templates are stale."
- "Session logs are missing the Focus field — template needs to enforce it."

## Related
- [[skill-name]] — related skill
- [[ADR-XXX]] — decision that shaped this skill
- [[Templates/Template-Name]] — form this skill fills in
