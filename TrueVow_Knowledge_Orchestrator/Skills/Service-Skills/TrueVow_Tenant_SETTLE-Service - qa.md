---
source: TrueVow_Tenant_SETTLE-Service/.opencode/skills/qa/SKILL.md
service: TrueVow_Tenant_SETTLE-Service
type: settlement-engine
stack: ["python", "nextjs", "postgresql", "alembic", "docker"]
imported: 2026-06-30T22:32:05.068805+00:00
skill_name: qa
---
# QA Skill — Testing, Verification & Documentation

**Last Updated:** 2026-06-23
**When to use:** Verifying implementations, running tests, fixing failures, committing, updating docs.
**Note:** Hard constraints and truth commands are in `settle-rules.md` (always loaded).

---

## Role

Verify implementations, run truth commands, fix test failures, commit to git, and update documentation.

## QA Workflow

**Step 1: Verify Implementation**
- Read the Architect's plan
- Read the Coder's checkpoint file
- Verify the implementation matches the plan
- Check that all files were created/modified correctly

**Step 2: Run Truth Commands**
- Run full test suite (see settle-rules.md)
- If any failures, fix FIRST failure only, re-run, repeat

**Step 3: Fix Test Failures**
1. Paste FULL output (or log path + failing section)
2. Fix ONLY the first failure
3. Re-run the same command
4. Repeat until green
5. Commit each fix with message: `fix: <first failure summary>`

**Step 4: Git Commit**
```bash
git add -A
git commit -m "feat: <feature description>

- Summary of changes
- Files modified
- Tests added/updated"
```

**Step 5: Update Documentation**
- Update `docs/01-main/IMPLEMENTATION_PROGRESS.md`
- Create/update `docs/01-main/MILESTONE_*_CHECKPOINT.md`
- Update `docs/01-main/WORKING_CACHE.md`
- Create ADR if non-trivial architectural decision was made

**Step 6: Architecture Validation**
- Verify the change respects all hard constraints (see settle-rules.md)
- Check for PHI/PII risks, predictive language, bar-compliance
- Document validation result in checkpoint

## Architecture Validation Checklist

Before marking DONE:

- [ ] No PHI/PII collection in new code
- [ ] No free-text narrative fields added
- [ ] No predictive AI language
- [ ] No liability assessment language
- [ ] No legal advice language
- [ ] IntelligenceGate n>=50 floor not lowered
- [ ] No tenant isolation added to SETTLE
- [ ] All new endpoints use proper auth dependencies
- [ ] All new models use Pydantic v2
- [ ] All new database operations use `get_db()` (async)
- [ ] All new code has tests
- [ ] All tests pass
- [ ] Documentation updated

## Test Coverage (Current: 186/186 passing)

| Test File | Module(s) Covered |
|---|---|
| `test_estimator.py` | Estimator engine |
| `test_intelligence_gate.py` | Intelligence gate, hierarchical fallback, pilot mode |
| `test_anonymizer.py` | PHI/PII anonymizer |
| `test_validator.py` | Input validation |
| `test_phase1_phase2.py` | Confidence score, carrier patterns, verdict search models |
| `test_phase2_5.py` | Advanced search filters, trend report models |
| `test_phase3_1.py` | Multiplier model layer |
| `test_phase3_2.py` | Overdemand cliff detection |
| `test_phase3_3.py` | Override tracking |
| `test_phase3_4_5_6.py` | Weekly digest, recency weighting, firm-wide yield |
| `test_phase4.py` | Outcome distribution |
| `test_e2e_integration.py` | End-to-end integration (14 tests, requires live backend) |

## Git Commit Convention

Types: `feat` (new feature), `fix` (bug fix), `test` (test changes), `docs` (documentation), `refactor` (no behavior change), `chore` (maintenance)

## Anti-Patterns

- **Never skip truth commands** — status stays UNVERIFIED
- **Never fix multiple failures at once** — fix first, re-run, repeat
- **Never commit without tests passing** — red tests = no commit
- **Never update docs without verifying code** — docs must match reality
- **Never use forced pushes** — always normal commits
- **Never commit secrets** — check for API keys, passwords, tokens
