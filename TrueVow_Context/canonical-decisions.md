# Canonical Decisions (Binding)

> Binding across all services. Each item links to its source of truth. Violating one is a defect. Recall live detail with `python TrueVow_Shared_Orchestration/memory.py recall "<topic>"`.

### 1. Platform Identity & ID Contract — ADR-005 (APPROVED; migration pending)
The canonical identifiers, binding on every service:

| Entity | Canonical ID | Type | Source of truth |
|---|---|---|---|
| Firm | `clerk_org_id` | TEXT (`org_*`) | Clerk |
| User | `clerk_user_id` | TEXT (`user_*`) | Clerk |
| Case | `mdm_cases.case_id` | UUID | **SaaS Admin MDM — the only minter** |
| Client | `contact_id` | UUID | SaaS Admin MDM (`mdm_contacts`) |
| CRM matter | `crm_matter_id` | TEXT | SaaS Admin CRM sync |

Rules: no service mints `case_id` except MDM; firm id is **TEXT, never UUID-cast**; `contact_id` travels alongside TRACE's opaque `client_token` (the non-PHI cross-service client key); `mdm_events_outbox` fans INTAKE → MDM → downstream. **Source:** `TrueVow_Tenant_TRACE_Service/docs/00-Planning/ADR-005-Platform-Identity-and-ID-Contract.md`. TRACE migration + sibling SETTLE/Billing/INTAKE ADRs are pending.

### 2. Auth = Clerk (3-domain). No Supabase Auth migration.
Frontends consume the shared `@truevow/auth-client` (`ClerkWrapper`); backends verify the Clerk JWT and normalize to a `AuthContext(user_id, firm_id, role, permissions)`. Services consume `AuthContext`, **never raw Clerk objects**. **Source:** ADR-003, `shared-libraries/auth-client`.

### 3. RULE 0 — No fabrication (platform-wide)
Never report a build, a test count, or a metric you did not actually produce. If a command did not run green in front of you, it is not green. A stub result is not a real result. **Source:** SETTLE decision memory (RULE 0).

### 4. Mandatory orchestrator check-in protocol
Every session: `sync-memory` → `scan-services` → `agent-checkin start` → work → `remember` → `agent-checkin done` → `push-memory`. A task is not done until the check-in is posted. Without it a service shows `NEGLECTED` and the CTO is blind. **Source:** per-service coding-instructions ("Report to the Orchestrator") + root `AGENTS.md`.

### 5. TRACE stack locks (ADR-003 / ADR-004)
Fax = **Documo**; clinical NER = **OpenMed**; OCR = **PaddleOCR-VL 1.5** (Tier 1B) + **Docling** (Tier 1A) — **deepdoctection ELIMINATED**; **Mistral OCR** = Tier 2 escalation; billing LLM = **Azure GPT-4o-mini**; e-signing = **DocuSeal**. `OCR_CLOUD_BACKEND` locks after the handwriting-spike WER result.

### 6. Product renames / retirements
DRAFT → **LEVERAGE** (same service, renamed). **CONNECT** archived. **First-Line Support** replaced by Chatwoot. **Dialogflow Intake** dead. **Source:** decision memory (importance 10).

### 7. Observability = SigNoz + Sentry + OpenTelemetry
Unified across services. **Source:** architecture memory (importance 10).

### 8. Domain safety invariants
- **LEVERAGE:** zero-knowledge — document content never leaves the attorney's device (not even in logs/telemetry).
- **SETTLE:** bar-compliant anonymization — no client identifiers, ever.
- **INTAKE:** zero-PHI hot path + prohibited-phrase filter — the voice agent may never say a dollar amount, a case-strength evaluation, legal advice, or urgency tactics (UPL risk).
- **TRACE / all tenant health data:** PHI never in logs or URLs; tenant isolation at three layers.
**Source:** per-service `docs/00-Planning/*-Agent-Coding-Instructions.md`.

_Curated 2026-07-10._
