---
source: TrueVow_SaaS_Administration_Service/.opencode/skills/qa-mode/SKILL.md
service: TrueVow_SaaS_Administration_Service
type: admin-dashboard
stack: ["nextjs", "typescript", "postgresql", "supabase"]
imported: 2026-06-30T22:32:04.864576+00:00
skill_name: qa-mode
---
---
name: qa-mode
description: Use when running tests, verifying builds, quality assurance, and git commits. Use ONLY after Coder Mode completes implementation or when verifying system state.
---

# QA Mode

## Role
You are the **Quality Assurance & Testing Agent** for TrueVow SaaS Administration. You run truth commands, verify builds, and if all ok then git commit and update documentation.

## Truth Commands (Run in Order)
1. `pnpm install` — Ensure dependencies are installed
2. `pnpm typecheck` — TypeScript compilation (npx tsc --noEmit)
3. `pnpm lint` — ESLint (next lint --max-warnings 9999)
4. `pnpm build` — Next.js production build
5. `npx jest --testPathPatterns="tests/"` — Run test suite

## Lint Gate Policy
- `pnpm lint` = `next lint --max-warnings 9999`
- Gate: **0 errors required, warnings allowed**
- If lint fails with errors, return to Coder Mode

## Verification Checklist
For each completed task:
- [ ] `pnpm typecheck` — 0 errors
- [ ] `pnpm lint` — 0 errors (warnings OK)
- [ ] `pnpm build` — Compiled successfully
- [ ] Relevant tests pass
- [ ] No console errors in browser
- [ ] Architecture document updated if needed
- [ ] Implementation progress updated
- [ ] Working cache updated

## Process Management
- **CRITICAL:** If any truth command runs longer than 120 seconds, kill it immediately
- If tests are stuck: kill node processes with `taskkill //F //IM node.exe`
- If build hangs: check for file locks, kill processes, retry
- Never let a process run indefinitely — always enforce timeouts

## Git Commit Protocol
If ALL truth commands pass:
1. `git status` — Review changed files
2. `git diff` — Review changes
3. Stage only intended files: `git add <files>`
4. Commit with descriptive message following repo conventions:
   ```
   git commit -m "type: description

   - Detail 1
   - Detail 2
   
   Verification: typecheck green, lint green, tests passing"
   ```
5. Push if remote exists: `git push`
6. Update documentation:
   - `TODO_TRACKER.md` — Mark task complete
   - `docs/00-main/IMPLEMENTATION_PROGRESS.md` — Update progress
   - `docs/00-main/WORKING_CACHE.md` — Update session log
   - Any other relevant docs

## Common Commit Types
- `feat:` — New feature
- `fix:` — Bug fix
- `docs:` — Documentation only
- `test:` — Test additions/fixes
- `refactor:` — Code refactoring
- `chore:` — Maintenance tasks

## If Tests Fail
1. Identify the failure category:
   - TypeScript errors → Return to Coder Mode
   - Lint errors → Return to Coder Mode
   - Test failures → Document which tests, assess if pre-existing
2. If pre-existing failures (known issues), document and proceed
3. If new failures, return to Coder Mode with specific error details

## Known Pre-existing Issues
- 564 test failures due to FK constraints, schema mismatches, mock issues
- These are NOT blockers — they're pre-existing issues being addressed separately
