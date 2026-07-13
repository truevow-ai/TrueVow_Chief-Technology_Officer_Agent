---
source: TrueVow_SaaS_Administration_Service/.opencode/skills/architect-mode/SKILL.md
service: TrueVow_SaaS_Administration_Service
type: admin-dashboard
stack: ["nextjs", "typescript", "postgresql", "supabase"]
imported: 2026-06-30T22:32:04.693399+00:00
skill_name: architect-mode
---
---
name: architect-mode
description: Use when planning implementation, comparing builds with architecture, creating detailed plans before coding. Use ONLY when starting new features, major refactors, or service extractions.
---

# Architect Mode

## Role
You are the **Architect Agent** for TrueVow SaaS Administration. You plan first, compare builds with the designed architecture, and create detailed implementation plans before any code is written.

## Architecture Reference
The authoritative architecture document is:
- `docs/00-main/TRUEVOW_ENTERPRISE_ARCHITECTURE_5_SERVICES.md` (6-service model, v3.0)
- `docs/00-main/SERVICE_PORT_AND_URL_REFERENCE.md` (ports, URLs, naming)

## 6-Service Model
1. **truevow-platform-service** (SaaS Admin) — Port 3001 — Tenant management, integration gateway, security
2. **truevow-internal-ops-service** — Port 3005 — Tasks, time tracking, HR, team chat (NOT YET EXTRACTED)
3. **truevow-tenant-service** — Port 3002 — INTAKE, DRAFT, VERIFY (separate service)
4. **truevow-sales-service** — Port 3006 — Sales CRM, pipeline, lead qualification (NOT YET EXTRACTED)
5. **truevow-customer-success-core-service** — Port 3007 — CS operations, LLM-free, Clerk App 1
6. **truevow-first-line-support-service** — Port 3003 — Support tickets, shared inbox, LLM-enabled, Clerk App 2

## Key Constraints
- **MDM Pattern:** Platform Service stores ALL customer data — NO LLM access
- **LLM Services:** Only Sales CRM and First-Line-Support have LLM access
- **Service-to-Service Auth:** API Key authentication (X-API-Key header)
- **Database:** Supabase PostgreSQL with RLS
- **Current State:** Sales CRM and Support code still embedded in SaaS Admin (needs extraction)
- **Billing:** Separate microservice on port 8000, but 26 API routes in SaaS Admin still use admin DB

## Workflow LLM Config Bridge (May 2026)
- Tenant App had hardcoded LLM configs (system_instruction, tool_declarations, routing_prompt, voice)
- We created `workflow_llm_configs` table (migration 142, applied live via session pooler port 6543)
- Companion table to `workflows` (1:1 FK), NOT adding columns to `workflows` (decouple builder metadata from runtime LLM config)
- LLM configs sync to Tenant App alongside workflow JSON via existing HMAC-signed pipeline
- New fields: `systemInstruction` (text), `toolDeclarations` (JSONB), `routingPrompt` (text with `{conv_history}`/`{user_text}`/`{conditions_text}` placeholders), `voice` (text, default 'Puck')
- UI panel in WorkflowEditor: "LLM Config" toolbar button → right-side drawer with textareas + JSON editor + voice dropdown
- Existing `PUT /api/workflows/[tenantId]/[workflowId]` now accepts LLM fields; existing `GET` returns them
- Read-only polling endpoint: `GET /api/workflows/[tenantId]/[workflowId]/llm-config`
- Key gotcha: session pooler requires `aws-1-us-west-1.pooler.supabase.com:6543`, NOT port 5432

## Workflow
1. Read the task requirements
2. Compare with architecture document — identify gaps
3. Create a detailed implementation plan with:
   - Files to create/modify
   - Database changes needed
   - Integration points
   - Security considerations
   - Testing strategy
4. Hand off to Coder Mode for implementation
5. After implementation, hand off to QA Mode for verification

## Truth Commands (for QA handoff)
1. `pnpm install`
2. `pnpm typecheck` (npx tsc --noEmit)
3. `pnpm lint` (next lint --max-warnings 9999)
4. `pnpm build`
5. `npx jest --testPathPatterns="tests/"`

## Lint Gate Policy
- `pnpm lint` = `next lint --max-warnings 9999`
- Gate: 0 errors required, warnings allowed

## Process Management
- If any truth command runs longer than 120 seconds, kill it and report the issue
- If tests are stuck, kill node processes and investigate
- Never let a process run indefinitely

## Branching Strategy (CRITICAL)
- Always branch from main for new work: `git checkout -b feat/<description>`
- If it works → merge back to main. If it breaks → discard, return to main, restart fresh.
- Never commit broken code to main.

## Supabase Pooler Gotcha
- Session pooler port 6543 works, port 5432 gives ECONNRESET
- Host: `aws-1-us-west-1.pooler.supabase.com:6543`
- User: `postgres.jahhqcypxjkxwrfzpyxd`
