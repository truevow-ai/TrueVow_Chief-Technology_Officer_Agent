# Voice & Standards

> How TrueVow writes and builds. Source of truth: each service's `docs/00-Planning/<Service>-Agent-Coding-Instructions.md`, which opens with "The One Thing That Matters Most" and defines "What Constitutes Failure" for that service.

## Who we build for (the north star)
- The **injured caller** on the phone (INTAKE) and the **solo PI attorney** who stakes their reputation on our output in front of adjusters, judges, and their own client.
- For internal tools (App1/App2), the user is a **TrueVow operator** (finance, ops, CSM, sales) — but any tenant data they can see is still sacred and audited.

## Product voice
- **Attorney-facing = plain English.** Never show HTTP codes, stack traces, `null`/`undefined`/`timeout`, JSON, or jargon. Every error states: what happened, whether it's temporary, and what to do next (+ support contact).
- **Loading/empty states are instructions**, not spinners — say what the system is doing and what to do next.
- **INTAKE voice compliance:** never a dollar amount, case-strength evaluation, legal advice, or urgency tactic (unauthorized-practice-of-law risk).
- **SETTLE:** data-backed and bar-compliant — a range, never a guarantee.

## Engineering standards (universal)
- Boring is a feature. Simple is not simplistic. No premature abstractions (write it twice before you abstract).
- Type everything; handle every error path; **write the test before you call it done**.
- **Tenant isolation is absolute** — query firm-scope + API validation + Supabase RLS (three layers).
- Secrets never touch git; `.env.example` with placeholders only.
- **RULE 0 — no fabrication.** Report only what you directly observed.
- **Report to the orchestrator** every session (check-in protocol). A task isn't done until the check-in is posted.
- Migrations are permanent (Alembic, reversible `downgrade()`); never edit an applied migration.

## The failure test (per service)
Every coding-instructions doc defines concrete failure — "If X happens, you have failed." Read your service's doc **before** writing a line of code. Examples:
- INTAKE: the call drops and the caller must re-explain their accident.
- TRACE: a misdirected fax sends PHI to an unauthorized provider.
- Billing: a missing idempotency key double-charges a tenant.
- Financial Management: a posted journal entry edited in place destroys the audit trail.
- LEVERAGE: a wrong SOL year passes a time-barred document → malpractice.

_Curated 2026-07-10._
