---
source: TrueVow_Tenant_Application_Service/.opencode/skills/qa/SKILL.md
service: TrueVow_Tenant_Application_Service
type: core-platform
stack: ["python-fastapi", "cloudflare-workers", "postgresql", "docker"]
imported: 2026-06-30T22:32:04.887917+00:00
skill_name: qa
---
# Tenant Application QA

## Description
Runs truth commands, verifies tests and builds, commits when all checks pass for the Tenant Application platform.

## Workflow
1. Receive completed work from builder
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
