---
source: TrueVow_Tenant_SETTLE-Service/.opencode/skills/cross-workspace-shipping/SKILL.md
service: TrueVow_Tenant_SETTLE-Service
type: settlement-engine
stack: ["python", "nextjs", "postgresql", "alembic", "docker"]
imported: 2026-06-30T22:32:05.044321+00:00
skill_name: cross-workspace-shipping
---
# Cross-Workspace Shipping Patterns

**Last Updated:** 2026-06-19
**When to use:** Operating in combined architect+executor mode, shipping a unit-of-work that touches a repo OUTSIDE the workspace. PowerShell is your shell. Multiple git repos exist.

**Companion skills:** `lead-dev-playbook.md` for two-agent mode. `settle-workflow.md` for general workflow.

---

## 1. Autonomy Calibration (Unit-Scoped Execution)

When the user fires a directive with a verbatim trigger ("go X end to end", "fire X"), execute the **entire unit** before reporting. Do NOT pause after every step. Do NOT ask permission for sub-decisions that fall within the directive.

**Five pre-defined pause triggers:**

1. **Secret leak risk** -- `.env*`, `.backup*`, credential files about to be staged
2. **Fetch returns existing refs** -- git remote is non-empty when directive assumed empty (clobber risk)
3. **CORS block** -- backend rejects required headers; needs CORS rule decision
4. **Gate failure needing arch decision** -- typecheck/test fails on something that's NOT a simple first-failure fix
5. **Scope mismatch** -- recon reveals the unit is materially larger than directive assumed

For all other friction (PowerShell quirks, missing imports, anchor mismatches, log file paths, etc.) -- solve and continue.

---

## 2. Recon Before Architect Calls

Before any cross-workspace edit, run parallel recon:

```
- grep for the symbol in BOTH repos (backend Pydantic + frontend types)
- read the directive's anchor file (the page/route/component named in the directive)
- list the target directory (verify component path exists / doesn't yet exist)
- check git remote ls-remote (clobber risk)
- check existing CORS / auth config (header forwarding constraints)
```

**Scope mismatch triggers (MUST stop and architect-call):**
- The page named in the directive is materially larger than directive language assumed
- The type alignment will break a pre-existing consumer
- The "single change" actually requires a product decision (UI shape vs API shape)
- The "no remote" assumption is wrong (remote has commits)

**Architect call format:** State the mismatch, propose A/B/C narrowed scopes, pick one, document deferral of the rest in end-of-unit report. Do NOT ask the user -- deferred items are surfaced at completion.

---

## 3. Cross-Workspace File Ops

`search_replace` and `create_file` tools error out (code 45405) when the target file is OUTSIDE the open workspace.

**Workaround: PowerShell file ops**

Full file write:
```powershell
$path = 'C:\path\outside\workspace\file.tsx'
$content = @'
// full file content here as a here-string
'@
[System.IO.File]::WriteAllText($path, $content)
```

Surgical edit (read, replace, write):
```powershell
$text = [System.IO.File]::ReadAllText($path)
$anchor = "  created_at: string;`n}"
$replacement = "  created_at: string;`n  newField?: string;`n}"
$newText = $text.Replace($anchor, $replacement)
[System.IO.File]::WriteAllText($path, $newText)
```

**LF vs CRLF detection (matters for anchor matching):**
```powershell
$text = [System.IO.File]::ReadAllText($path)
$hasCRLF = $text.Contains([char]13 + [char]10)
$hasLFOnly = -not $hasCRLF -and $text.Contains([char]10)
```

**Always log every cross-workspace write:**
```powershell
$before = (Get-Item $path).Length
[System.IO.File]::WriteAllText($path, $newText)
$after = (Get-Item $path).Length
Write-Host "Before=$before, After=$after"
```

---

## 4. PowerShell Git Hardening

**`git commit -F` requires `--cleanup=verbatim`:**
Git's default `--cleanup=default` strips lines starting with `#` and trims whitespace. Always:
```powershell
git commit --cleanup=verbatim -F logs\v_front_feature_msg.txt
```

**PowerShell variable expansion in double-quoted strings:**
`"$35k+"` interpolates `$35` as undefined variable -> empty string. Fix:
```powershell
$str = "Typical range increases to `$35k+"   # backtick-escape
$str = 'Typical range increases to $35k+'    # or use single quotes
```

**git push + output redirection = `^C` interrupt:**
Run push WITHOUT redirection:
```powershell
git push origin master:main
git ls-remote origin main   # confirm sha matches local HEAD
git rev-parse HEAD
```

**Push false-positive RemoteException:**
Git writes progress to stderr. PowerShell treats stderr-on-success as error. Trust `git ls-remote origin <branch>` over PowerShell exit codes.

**GitHub PAT `workflow` scope trap:**
Recovery without losing baseline:
```powershell
git rm --cached .github/workflows/<name>.yml
git commit --amend --no-edit --cleanup=verbatim
git push origin master:main
```

---

## 5. Two-Commit Baseline Pattern

When initializing a fresh repo within a feature cohort, split into TWO commits:

```
chore(initial): baseline scaffold + secret protection
feat(<scope>): <cohort-name> infrastructure
```

**Always pre-flight before baseline commit:**
1. `git ls-remote <remote-url>` -- confirm remote is empty
2. Secret scan: `git status` shows NO `.env*`, `.backup*`, credentials
3. If remote is non-empty -> STOP and architect-call

---

## 6. Surface-and-Document for Pre-Existing Damage

When typecheck/lint fails on files you didn't touch, do NOT fix them inline:
1. Capture FULL error output to `logs/<cohort>_<gate>.log`
2. List failing files in feature commit message body
3. Status stays UNVERIFIED with note: "zero new errors introduced by <cohort>"
4. Surface in end-of-unit report as deferred item

---

## 7. Additive Type Updates

When backend Pydantic shape and frontend interface diverge, **prefer additive optional fields** over alignment. The full alignment cohort lands later, after every consumer has migrated.

---

## 8. Anti-Patterns

- **Pausing on every PowerShell quirk** -- solve and continue
- **Letting `npm run lint` open an interactive prompt** -- kill node processes, mark NOT CONFIGURED
- **Inline-fixing TS errors found during typecheck** -- fix only your errors, surface pre-existing as deferred
- **Committing without `--cleanup=verbatim`** -- produces silently empty commits
- **Trusting PowerShell exit codes from git operations** -- verify via `git ls-remote`

---

## 9. End-of-Unit Report Template

```markdown
# Cohort <X> -- End-of-Unit Report

**Status: <DONE | UNVERIFIED | BLOCKED>**
**Push Status: <DONE | DEFERRED>**

## Commit SHAs landed
| Commit | SHA | Scope |
|---|---|---|

## Quality gates
| Gate | Status | Notes |
|---|---|---|
| typecheck | | |
| lint | | |
| build | | |
| tests | | |

## Deferred items (max 3)
1.
2.
3.

## Architect decisions made during execution
-
```
