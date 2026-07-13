---
source: TrueVow_Customer_Success_CORE_Service/.opencode/skills/cs-qa/SKILL.md
service: TrueVow_Customer_Success_CORE_Service
type: customer-success
stack: ["nextjs", "typescript", "postgresql", "supabase"]
imported: 2026-06-30T22:32:05.113587+00:00
skill_name: cs-qa
---
# Customer Success QA

## Description
Runs truth commands, verifies tests and builds, commits when all checks pass for Customer Success Core.

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
