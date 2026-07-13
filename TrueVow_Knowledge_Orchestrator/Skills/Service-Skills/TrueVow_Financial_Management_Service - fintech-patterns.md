---
source: TrueVow_Financial_Management_Service/.opencode/skills/fintech-patterns/SKILL.md
service: TrueVow_Financial_Management_Service
type: financial-backend
stack: ["python-fastapi", "nextjs", "postgresql", "alembic"]
imported: 2026-06-30T22:32:04.624283+00:00
skill_name: fintech-patterns
---
---
name: fintech-patterns
description: TrueVow Financial Management domain patterns — multi-tenancy via legal_entity_id + Row Level Security, double-entry accounting, GL/AR/AP/Payroll/Treasury/Intercompany/Reporting module relationships, Benjamin INTAKE usage-based cost accruals, the Billing Service adapter, API/error envelopes, and common pitfalls. Use when implementing or reviewing any TrueVow FM backend feature, accounting flow, tenant/RLS scoping, or Benjamin vendor cost.
---

# TrueVow Financial Management — Domain Patterns

---

## Architecture Overview

TrueVow Financial Management is the back-office accounting and financial operations system for TrueVow, an enterprise company building and deploying legal AI services (INTAKE, DRAFT, VERIFY, SETTLE) to solo and small law firms in the USA.

### System Role
- Manages TrueVow's own finances (internal accounting)
- Tracks operational costs including Benjamin INTAKE infrastructure
- Handles billing to law firm clients via the AR module
- Multi-tenant capable (legal entities)

---

## Core Data Patterns

### Multi-Tenancy via legal_entity_id
Every financial record belongs to a legal entity. This is enforced at both:
- **Application level:** all queries scoped by `legal_entity_id`
- **Database level:** PostgreSQL Row Level Security (RLS) on every table

```sql
-- Every table follows this pattern
CREATE TABLE module_resource (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    legal_entity_id UUID NOT NULL REFERENCES legal_entity(id),
    ...
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now()
);
ALTER TABLE module_resource ENABLE ROW LEVEL SECURITY;
CREATE POLICY module_resource_tenant_isolation ON module_resource
    USING (legal_entity_id::text = current_setting('app.current_tenant', true));
```

### Audit Trail
All financial records require:
- `created_at` / `updated_at` timestamps
- `created_by` / `updated_by` user references (where applicable)
- Immutable audit logs for sensitive operations

### Double-Entry Accounting (GL)
Every financial event produces balanced journal entries:
```
Debit  Account_A   Amount
Credit Account_B   Amount
Sum(debits) == Sum(credits)  — always
```

---

## Module Relationships

```
GL (General Ledger) ← Master ledger, receives entries from all modules
         ↑
   ┌─────┼─────┬──────────┬──────────┐
  AR    AP   Payroll  Treasury  Intercompany
         ↓
     Reporting (reads from GL + all modules)
```

- **AR** posts revenue/receivable entries to GL on invoice + payment
- **AP** posts expense/payable entries to GL on bill + payment
- **Payroll** posts payroll expense entries to GL on run approval
- **Treasury** posts bank transaction entries to GL on reconciliation
- **Intercompany** posts elimination and transfer entries to GL

> Posting seam: subledgers post into the GL through the `LedgerPoster` protocol
> (`app/modules/general_ledger/services/ledger_poster.py`) via `get_ledger_poster(session)`,
> not by importing `JournalEntryService` directly.

---

## Benjamin INTAKE Cost Patterns

### What Benjamin Is
Benjamin is TrueVow's voice AI engine that powers the INTAKE service — handling inbound calls for law firm clients. TrueVow pays all infrastructure and vendor costs.

### Cost Categories
| Category | Vendor Examples | Billing Type | AP Treatment |
|----------|----------------|--------------|--------------|
| Compute | Hetzner, DigitalOcean, AWS | Monthly fixed | Standard AP invoice |
| Telephony | Twilio, Telnyx | Per-minute usage | Accrual then invoice |
| STT | Deepgram, AssemblyAI | Per-minute usage | Accrual then invoice |
| TTS | ElevenLabs, Azure TTS | Per-character | Accrual then invoice |
| Monitoring | Grafana Cloud | Monthly fixed | Standard AP invoice |

### Accrual Pattern for Usage-Based Vendors
Because telephony/STT/TTS bill in arrears:
1. End of month: estimate usage → post accrual entry to GL
2. Invoice received: reverse accrual, post actual AP bill
3. Payment: standard AP payment workflow

### Cost Center
Benjamin/INTAKE operational costs should be tracked under a dedicated cost center for:
- P&L visibility per service line
- Future per-client allocation if needed
- Investor/board reporting on INTAKE service economics

---

## External Integration Patterns

### Billing Service Adapter (AR Module)
AR integrates with the external Billing Service for pricing and feature access:
```
app/modules/ar/integrations/
├── billing_adapter.py          # Abstract base (ABC)
└── http_billing_adapter.py     # Real HTTP implementation
```

**Key capabilities provided by Billing Service:**
- Tenant tier (`solo` | `growth`) with subscription status
- Feature access with per-use pricing (INTAKE, SETTLE, DRAFT)
- Add-on purchases
- Founding Intelligence pricing lock (until 2029-01-01)

**Founding Intelligence Rule:** Founding members have contractually locked pricing. The `check_founding_intelligence_benefits()` method in `pricing_service.py` must be called before any cost calculation. NEVER apply a price override to a founding member account.

### General Adapter Rule
All external service integrations follow this pattern:
```
{module}/integrations/
├── {service}_adapter.py        # ABC — defines the interface contract
└── http_{service}_adapter.py   # HTTP implementation for production
```
Tests use a `Mock{Service}Adapter`. Never hardcode HTTP adapter in service layer.

---

## Module File Structure

All backend modules use **directory-based** structure:
```
app/modules/{module}/
├── api/
│   └── routes/              # FastAPI route files
├── models/               # ORM model files
├── repositories/         # DB query layer files
├── schemas/              # Pydantic schema files
├── services/             # Business logic files
└── integrations/         # External service adapters (if applicable)
```

> CRITICAL: Do NOT assume `models.py`, `service.py`. Always use the directory structure above.

---

## API Patterns

### Standard Response Envelope
```json
{
  "data": { ... },
  "meta": { "total": 100, "page": 1 }
}
```

### Error Response
```json
{
  "detail": "Human-readable message",
  "code": "MACHINE_READABLE_CODE"
}
```

### Pagination
All list endpoints support:
- `?page=1&page_size=50`
- Default page_size: 50
- Max page_size: 200

---

## Security Patterns

### Auth Flow
1. Login → JWT issued
2. JWT included in `Authorization: Bearer {token}` header
3. `get_current_user` dependency validates token
4. `legal_entity_id` extracted from token or request path

### Forbidden Patterns
- Never bypass auth globally
- Never expose raw SQL errors to API consumers
- Never skip RLS on new tables
- Never log PII (names, SSNs, account numbers) in plain text

---

## Testing Patterns

### Backend Test Structure
```
tests/
├── unit/           # Isolated service/repository tests
├── integration/    # DB + API tests with real DB session
└── conftest.py     # Shared fixtures (db session, auth tokens)
```

> Offline unit tests default to in-memory SQLite when `TEST_DATABASE_URL` is unset
> (see `tests/conftest.py`). Live integration/compliance tests require Postgres/HTTP.

### Frontend Test Structure
```
frontend/__tests__/
├── components/     # React component tests
├── hooks/          # Custom hook tests
└── pages/          # Page integration tests
```

---

## Common Pitfalls

| Pitfall | Symptom | Fix |
|---------|---------|-----|
| Missing RLS context | Empty query results, no error | Set `app.current_tenant` before query |
| Assuming flat module files | Can't find `models.py`, `service.py` | Look for `models/`, `services/` directories instead |
| Hardcoding HTTP adapter | Tests make real HTTP calls, fail | Inject adapter interface, use Mock in tests |
| Unbalanced journal entries | GL trial balance fails | Always post debit+credit pairs |
| Usage-based vendor not accrued | Understated expenses mid-month | Post monthly accruals for Twilio/Deepgram/ElevenLabs |
| pnpm vs npm mix | Frontend install errors | Use pnpm only (pnpm-lock.yaml present) |
| Missing `legal_entity_id` on new table | RLS blocks all rows | Always add RLS policy on migration |
| Ignoring Founding Intelligence lock | Wrong pricing applied to founding members | Always call `check_founding_intelligence_benefits()` before cost calculation |
| Milestone "Complete (90%)" | Edge cases never finished | Ask: "What are the remaining 10%?" |
| Direct psql on Windows | DNS resolution failure | Use connection pooler (aws-1-us-east-1.pooler.supabase.com) |
| Treasury tables missing | Queries fail, code references non-existent tables | Check `WORKING_CACHE.md` for schema gaps before querying |

---

## Debugging Checklist

- [ ] Check RLS context is set (`app.current_tenant`)
- [ ] Verify double-entry accounting holds (debits = credits)
- [ ] Confirm external adapters are injected correctly (not hardcoded)
- [ ] Run `alembic upgrade head` to reproduce
- [ ] Check logs: `logs/alembic.log`, `logs/pytest.log`
- [ ] **Verify table exists** before querying (check `WORKING_CACHE.md` for known gaps)
- [ ] **Use connection pooler** on Windows (not direct psql)

---

_Migrated from `.qoder/skills/fintech-patterns.md` (Updated 2026-03-06)._
