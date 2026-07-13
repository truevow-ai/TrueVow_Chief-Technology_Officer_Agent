---
source: TrueVow_Tenant_SETTLE-Service/.opencode/skills/lead-dev-playbook/SKILL.md
service: TrueVow_Tenant_SETTLE-Service
type: settlement-engine
stack: ["python", "nextjs", "postgresql", "alembic", "docker"]
imported: 2026-06-30T22:32:05.064787+00:00
skill_name: lead-dev-playbook
---
# Lead Developer Playbook & Staged Wiring Workflow

**Last Updated:** 2026-06-19
**When to use:** Playing the lead-developer / architect role and handing well-scoped, staged work to a cheaper coder agent, OR wiring code paths from mock/stub to live.

---

## Part 1: Lead Developer Playbook

### The Three-Step Discipline

#### SURVEY (read-only, ~10-15 min)

Before designing any change, look at the actual state:

- **List folders** with exact names (don't infer from naming patterns -- verify)
- **Read key config files** (`.env.local`, `package.json`, `requirements.txt`, schema files)
- **Query the database** for current schema and row counts
- **Read existing code** that will be touched (function signatures, return types, imports)
- **Confirm which folder/project is canonical** when multiple similar names exist

Output: a factual inventory in a structured format. Never a "trust me, I looked."

#### PLAN

After the survey, design based on what you actually saw:

- **List explicit assumptions** ("survey shows X, so doing Y because Z")
- **Identify dependencies, side effects, blockers** up front
- **Propose multiple options** when there's a real tradeoff (typically A/B/C with cost/risk for each)
- **Get user OK before implementing** if scope is significant
- **Pick a recommendation and explain the reasoning**

#### BUILD

Execute with discipline:

- **One file or one logical change at a time** -- never bundle independent edits
- **Pause at natural gate-points** -- between independent files, between fix-and-verify, between code and tests
- **Test/verify after each change** -- don't assume "patch applied = patch correct"
- **Report what you actually did** with diffs, not summaries -- summaries hide bugs

### Prompt Anatomy for Coder Agents

Every prompt to a coder agent should have six parts:

1. **Mission line** -- One sentence stating what this prompt accomplishes.
2. **Current state (the survey)** -- What does the agent need to know before making the change?
3. **The exact change** -- Be specific. "Find this string, replace with this string" beats "update the function."
4. **Guardrails (the "don't" list)** -- "Don't touch X," "Don't run pytest," "Don't flip flags."
5. **Verification step** -- How will the agent know the change worked?
6. **Pause-point** -- Explicit instruction to stop and report.

### Decision Frameworks

**A/B/C tradeoff tables:**

| Option | Time | Risk | Reach |
|---|---|---|---|
| **A. Full rebuild** | 4 hours | High | Covers everything |
| **B. Patch-and-extend** | 1 hour | Low | Covers 80% |
| **C. Defer entirely** | 0 | Zero | Covers nothing |

Then recommend one with reasoning.

**The "highest-ROI single change" framing:**
When there are 5 things broken, identify the single change that fixes the most and start there.

### Guardrail Patterns

**The "don't touch" list (every prompt):**
- Don't touch `tests/`, `database/`, specific folders
- Don't run `pytest`
- Don't modify "pre-existing files"
- Don't flip global flags mid-task

**The "stage gate" pattern:**
```
STAGE 1 -- Survey -> PAUSE
STAGE 2 -- Plan -> PAUSE FOR APPROVAL
STAGE 3a -- Build patch #1 -> PAUSE
STAGE 3b -- Build patch #2 -> PAUSE
STAGE 3c -- Smoke test -> PAUSE
```

**The "if X then STOP" pattern:**
> "If pre-conditions check fails, STOP and report -- don't try to fix."
> "If any test goes RED, STOP -- copy the exact error message back to me."

### Common Recipes

**Schema audit before any DB change:**
```
STAGE 1 (read-only): List ALL tables, columns with types, confirm extensions, check row counts.
Output as markdown table. PAUSE AND REPORT. DO NOT run any DDL.
```

**Endpoint inventory before API changes:**
```
STAGE 1 (read-only): Walk app/api/v1/endpoints/ and produce a table:
| File | Route | Function | State (MOCK/DEAD/ORM/READY/SKIP) | Auth |
PAUSE AND REPORT. No code changes.
```

**Diagnostic before any "this is broken" patch:**
```
Before fixing, diagnose: group failures, identify dominant mode, report findings.
PROPOSE one patch. DO NOT apply yet.
```

### Anti-Patterns

- **The "do everything" prompt** -- Stage it
- **Substitution without asking** -- Agent MUST stop and ask
- **Letting the coder agent fix architecture** -- Coder never fixes schema or security
- **Bundling fixes with features** -- Each goes in its own stage
- **Confidently wrong on resource location** -- 30-second clarification beats 3-hour wrong-folder excursion

### Recovery Playbook

**When a test goes RED:**
1. Don't panic. Read the full error.
2. Categorize: Schema mismatch / Env-config / Network-transient / Code bug / Security failure
3. Apply rollback if data was written. Patch upstream of the failure. Re-run.

**When the coder agent goes off-script:**
1. Note what it actually did. 2. Decide: keep or revert. 3. Re-issue with stricter guardrails.

### Cost Model

| Agent | Use for | Cost per work-hour |
|---|---|---|
| Claude Opus 4 / GPT-5 | Architecture, design, debugging | $5-15 |
| Claude Sonnet 4 | Mid-complexity, budget fallback | $1-5 |
| Qoder / Cursor / Aider with Sonnet | Execution of well-defined patches | $0.50-2 |
| Qwen 3 / DeepSeek / local Llama | High-volume mechanical work | $0.05-0.50 |

**Spec-once / execute-cheap pattern:**
1 Opus session writing a focused spec ($5-10) + 5 Qoder executions ($1.50) = ~$7 vs 5 Opus sessions at $50+

---

## Part 2: Staged Wiring Workflow

**When to use:** Wiring code paths from mock/stub to live, refactoring across multiple endpoints, or any change that touches >1 file with regression risk.

**Core principle:** Survey -> Plan -> Build (one substep) -> Sanity-check -> Pause -> Next substep. Never skip the pause.

### The 5-Stage Outer Loop

**Stage 0 -- Classify:** Mechanical fix (one symbol) -> small patch. Wiring task -> use Stages 1-4.

**Stage 1 -- Inventory survey (READ-ONLY):**
Produce a table: `| File | Symbol/Route | Function | State (M/D/O/R/S) | Auth/Deps |`
Also catalog: DB client patterns, Pydantic models, env vars, auth injection.
**PAUSE AND REPORT.**

**Stage 2 -- Per-substep mini-survey:**
For each substep: Input contract, Output contract, Caller/dependency structure, Available primitives.
**PAUSE AND REPORT.**

**Stage 3 -- Plan with risk table:**
Option A vs Option B. Recommend based on dominant codebase pattern.

**Stage 4 -- Build ONE substep, sanity-check, report:**
Apply one patch. Run isolated sanity check. Report. **PAUSE.**

### Sanity-Check Rules

1. **Probe scripts, NOT `python -c`** on PowerShell (mangles escaped quotes)
2. **Decode opaque output** before reporting
3. **One sanity check per substep**, not per session
4. **Hung terminal recovery:** write output to `logs/<probe_name>.log`

### Latent-Crasher Catalog Protocol

Grep for these during every survey:

| Pattern | Risk | Fix |
|---|---|---|
| `datetime.now(UTC)` without `from datetime import UTC` | `NameError` | Add `UTC` import |
| `UUID()` with no args | `TypeError` | Replace with `uuid4()` |
| `.range(from, to)` on custom REST client | `AttributeError` | Add `range()` method |
| `await pool.fetch(...)` against non-asyncpg client | `AttributeError` | Rewrite to project's client API |

**Defensive-fix order:** Fix crashers FIRST, before any flag flip.

### Mock-Mode Flip Policy

1. Land all defensive fixes from latent-crasher catalog
2. Wire the live path while flag is still `True`
3. Add unit/probe coverage for the new live code
4. Smoke-test the live path with a script that bypasses the flag
5. Only then flip the flag in `.env.local`
6. Re-run smoke test through the API surface
7. Keep the flag toggle reversible -- do not delete the mock path in the same patch

### Reporting Template (Every Pause)

```
### Substep N.M -- <short title>

**Changed:** - path/to/file.py -- <one-line diff summary>
**Sanity command:** - `python scripts/_phaseNX_thing_probe.py`
**Result:** PASS | FAIL | BLOCKED
**Deviations from spec:** <none | list>
**Side-findings (out of scope):** <list>
**Next:** Substep N.(M+1) -- <title>, awaiting go.
```

### Quick Checklist

```
[ ] Stage 0: Classified as mechanical | wiring
[ ] Stage 1: Inventory table produced, paused
[ ] Stage 2.1: Mini-survey for substep 1, paused
[ ] Stage 3.1: Plan + risk table, option chosen
[ ] Stage 4.1: One patch + probe + report, paused
[ ] (repeat 2.N -> 4.N per substep)
[ ] Defensive crashers fixed before flag flip
[ ] Mock-mode flip is its own commit
[ ] WORKING_CACHE.md updated
```
