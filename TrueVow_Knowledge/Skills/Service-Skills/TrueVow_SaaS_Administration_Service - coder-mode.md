---
source: TrueVow_SaaS_Administration_Service/.opencode/skills/coder-mode/SKILL.md
service: TrueVow_SaaS_Administration_Service
type: admin-dashboard
stack: ["nextjs", "typescript", "postgresql", "supabase"]
imported: 2026-06-30T22:32:04.806013+00:00
skill_name: coder-mode
---
---
name: coder-mode
description: Use when implementing planned tasks, writing code, fixing bugs, creating features. Use ONLY after Architect Mode has created a plan or when making small focused changes.
---

# Coder Mode

## Role
You are the **Expert Coding Agent** for TrueVow SaaS Administration. You complete each planned task following established patterns, conventions, and security best practices.

## Code Conventions
- **Framework:** Next.js 14.2 (App Router)
- **Language:** TypeScript (strict mode)
- **Package Manager:** pnpm
- **Database:** Supabase PostgreSQL
- **Auth:** Clerk
- **Testing:** Jest

## Patterns to Follow

### API Route Pattern
```typescript
import { NextRequest } from 'next/server'
import { withErrorHandler, withAuth } from '@/lib/api/middleware'
import { ApiErrors, createSuccessResponse } from '@/lib/api/errors'
import { logger } from '@/lib/api/logger'

export const GET = withErrorHandler(
  withAuth(async (request: NextRequest) => {
    try {
      const user = await getCurrentUser()
      if (!user) return ApiErrors.UNAUTHORIZED()
      // Implementation
      return createSuccessResponse(data)
    } catch (error: any) {
      logger.error('Error:', error)
      throw ApiErrors.DATABASE_ERROR('Database error', error)
    }
  })
)
```

### Service Client Pattern
- Singleton pattern with `getInstance()`
- JWT authentication for Tenant App
- API Key authentication for other services
- Retry logic with exponential backoff (3 attempts)
- 30-second timeout

### Error Handling
- Use `withErrorHandler` middleware wrapper
- Use `ApiErrors` for consistent error responses
- Log all errors with `logger`
- Never expose internal errors to clients

### Database Access
- Use `adminSupabase` for admin database
- Use `billingSupabase` for billing database (separate project)
- Always use service role key for admin operations
- Handle RLS appropriately

## Security Rules
- **NEVER** commit secrets or API keys
- **NEVER** expose internal error details to clients
- **ALWAYS** validate UUIDs before database queries
- **ALWAYS** use parameterized queries (Supabase handles this)
- **NEVER** add LLM access to Platform Service (MDM pattern)

## Pattern: Companion Table for New Config Domain
When adding new configuration fields for an external service that relate 1:1 to an existing table:
- Create a **companion table** (not columns on the existing table) — decouples different change cadences
- Use `workflow_row_id UUID NOT NULL UNIQUE REFERENCES workflows(workflow_row_id) ON DELETE CASCADE`
- Add trigger for `updated_at` auto-update
- Example: `workflow_llm_configs` for Tenant App LLM configs (migration 142)

## Pattern: Extending Sync Payload
When adding fields to the Tenant App sync pipeline:
1. Extend `SyncCommitRequest` interface with optional `llmConfig` field
2. Add fields to the payload object inside `commitWorkflowToTenantApp()`
3. Fetch LLM config in the route handler BEFORE calling sync, pass alongside
4. Key files: `lib/workflows/sync-client.ts`, `approve/route.ts`, `commit/route.ts`

## Pattern: Supabase DB Migration Run
- Use `scripts/_migrate_*.js` pattern with pg client
- Connection string: session pooler on **port 6543** (`aws-1-us-west-1.pooler.supabase.com:6543`)
- Port 5432 consistently gives ECONNRESET; port 6543 works
- User format: `postgres.<project_ref>` (not `postgres` alone for pooler)

## File Locations
- API routes: `app/api/v1/` and `app/api/workflows/` (workflow builder routes)
- UI pages: `app/(dashboard)/`
- Components: `components/`
- Libraries: `lib/`
- Tests: `tests/`
- Migrations: `supabase/migrations/`
- Workflow builder docs: `docs/01-main/`
- Agent briefing: `docs/01-main/WF_LLM_CONFIGS_BRIDGE_BRIEF.md`

## Process Management
- If any command runs longer than 120 seconds, kill it and report
- If stuck on a problem, document the issue and move to the next task
- Never let a process run indefinitely

## Branching Strategy (CRITICAL)
- Always branch from main for new work: `git checkout -b feat/<description>`
- If it works → merge back to main. If it breaks → discard, return to main, restart fresh.
- Never commit broken code to main.

## Supabase Pooler Gotcha
- Session pooler port 6543 works, port 5432 gives ECONNRESET
- Host: `aws-1-us-west-1.pooler.supabase.com:6543`
- User: `postgres.jahhqcypxjkxwrfzpyxd`

## Pattern: Bridge Adapter Integration (CRITICAL — Do Not Skip)
When integrating a new voice/audio bridge adapter:
- **STEP 0 (MANDATORY):** Get the vendor's working workflow JSON from their system BEFORE writing any adapter code
- **STEP 1:** Diff your adapter's `compile()` output against their reference workflow FIELD-BY-FIELD
- **STEP 2:** Every node field in their reference (`add_global_prompt`, `allow_interrupt`, etc.) must exist in your output
- **STEP 3:** Every edge field in their reference (`sourceHandle`, `targetHandle`, `data.condition`, etc.) must exist in your output
- **STEP 4:** Verify API key, health check, list endpoint, create endpoint
- **STEP 5:** Push ONE test workflow, verify in their UI renders clean
- **DO NOT iterate 5 times (like Dograh)** — catch all schema mismatches at step 1 via diff
- Reference: `docs/01-main/BRIDGE_ADAPTER_CHECKLIST.md`

## After Coding
1. Run truth commands: typecheck, lint
2. If both pass, hand off to QA Mode
3. If failures, fix and re-run
