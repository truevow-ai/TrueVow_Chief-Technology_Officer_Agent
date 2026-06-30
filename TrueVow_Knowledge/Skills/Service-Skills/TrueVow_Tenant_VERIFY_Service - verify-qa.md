---
source: TrueVow_Tenant_VERIFY_Service/.opencode/skills/verify-qa/SKILL.md
service: TrueVow_Tenant_VERIFY_Service
type: verification-service
stack: ["python", "fastapi"]
imported: 2026-06-30T22:32:05.098416+00:00
skill_name: verify-qa
---
# VERIFY QA

## Description
Runs truth commands, verifies tests and builds, commits when all checks pass for VERIFY.

## Workflow
1. Receive completed work from coder
2. Run truth commands in order (see AGENTS.md)
3. Fix first failure, re-run, repeat until green
4. Commit when all checks pass

## Rules
- Never commit with failing truth commands
- First-failure fix loop: fix only the first failure before re-running
- Capture raw command output for verification
- Run `skillspector scan` before installing new skills

## Ecosystem Integration
This skill is registered in config.yaml. Dispatch routes QA tasks here.
