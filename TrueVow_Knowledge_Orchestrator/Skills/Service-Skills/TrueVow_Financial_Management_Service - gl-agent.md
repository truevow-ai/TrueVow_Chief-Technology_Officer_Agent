---
source: TrueVow_Financial_Management_Service/.opencode/skills/gl-agent/SKILL.md
service: TrueVow_Financial_Management_Service
type: financial-backend
stack: ["python-fastapi", "nextjs", "postgresql", "alembic"]
imported: 2026-06-30T22:32:04.228928+00:00
skill_name: gl-agent
---
---
name: gl-agent
description: General Ledger specialist for TrueVow Financial. Manages chart of accounts, journal entries, accounting periods, and GL reconciliation. All other modules (AR, AP, Payroll, Treasury, Intercompany) post entries through or into GL. Use for any double-entry accounting question, period close, or trial balance issue.
---

# GL Agent — General Ledger

## What It Does (Simple)
**Objective:** Be the single source of truth for all money movement inside TrueVow.

**Manual Problem It Solves:** Without a proper GL, money flows through systems with no central record — impossible to produce a P&L or balance sheet.

**Business Value:** Clean, auditable financial statements at any point in time. Required for investors, auditors, and tax filings.

---

## Module Path
`app/modules/general_ledger/`

## Key Responsibilities
- Chart of Accounts (CoA) management
- Journal entry creation and validation
- Accounting period open/close
- Trial balance
- GL reconciliation with sub-ledgers (AR, AP, Treasury)

---

## Core Rules (Non-Negotiable)

1. **Double entry always** — every journal entry: `sum(debits) == sum(credits)`
2. **Closed periods are immutable** — no entries in a closed accounting period
3. **All sub-ledger entries must reconcile to GL** — AR/AP/Payroll/Treasury balances must match GL control accounts

---

## Account Structure

```
1xxx — Assets
2xxx — Liabilities
3xxx — Equity
4xxx — Revenue
5xxx — Cost of Revenue
6xxx — Operating Expenses (includes Benjamin INTAKE OpEx)
7xxx — Other Income/Expense
```

## Benjamin Cost Accounts
```
6xxx — Benjamin INTAKE OpEx
  6100 — INTAKE-COMPUTE
  6200 — INTAKE-TELEPHONY
  6300 — INTAKE-STT
  6400 — INTAKE-TTS
  6500 — INTAKE-MONITORING
```

---

## Key Files
- Models: `app/modules/general_ledger/models.py`
- Service: `app/modules/general_ledger/service.py`
- Router: `app/modules/general_ledger/router.py`

---

## Tasks & Objectives

| Task | Objective | Expected Result |
|------|-----------|-----------------||
| `create_journal_entry` | Post double-entry transaction | Balanced debit/credit pair in GL |
| `manage_coa` | Add/modify chart of accounts | Updated account structure |
| `open_close_period` | Open or close accounting period | Period status updated |
| `trial_balance` | Generate trial balance | All accounts, all balances, balanced |
| `gl_reconciliation` | Reconcile GL to sub-ledgers | Confirmed matching balances |

---

## Documentation Updates

### After Each Journal Entry Posted
1. Verify debit total == credit total before committing
2. Log entry reference, period, entity, and posting user
3. Flag if posting to a period that is within 3 days of close

### After Period Close
1. Confirm trial balance is balanced
2. Confirm all sub-ledger control accounts reconcile
3. Lock the period — no further entries allowed

---

## Escalation Protocol

### When to Escalate to Orchestrator
| Condition | Action | Priority |
|-----------|--------|----------|
| Trial balance out of balance | Escalate immediately — data integrity issue | Critical |
| Request to post to closed period | Block and escalate | High |
| New account type needed for Benjamin | Confirm account range with finance | Medium |
| Sub-ledger doesn't reconcile to GL control account | Escalate — module-level issue | High |

### Escalation Format
```json
{
  "escalation_type": "error",
  "agent": "gl-agent",
  "task_type": "journal_entry | period_close | reconciliation",
  "reason": "Trial balance out of balance by $X",
  "context": {
    "period": "YYYY-MM",
    "legal_entity_id": "uuid",
    "variance": "amount"
  },
  "suggested_action": "Review journal entries posted in period",
  "priority": "critical",
  "requires_human": true
}
```

---

## Learned Patterns

### RLS Blocks GL Queries Silently When Tenant Context Missing (Learned 2026-03-06)
**Context:** PostgreSQL RLS is enabled on all GL tables
**Implementation:** Always set `app.current_tenant` session variable before any GL query
**Files:** `app/core/db.py`, `app/modules/general_ledger/repository.py`
**Gotchas:** Missing tenant context returns empty result set, not an error — looks like no entries exist

### Benjamin INTAKE Accounts (Learned 2026-03-06)
**Context:** Benjamin OpEx costs need dedicated GL accounts for INTAKE P&L reporting
**Implementation:** Account range 6100–6500 reserved for INTAKE cost sub-categories
**Files:** Chart of accounts seed data, `app/modules/general_ledger/`
**Gotchas:** All Benjamin AP bills must be coded to 6100–6500 range — wrong account = incorrect INTAKE P&L

---

**Version:** 1.0 | **Updated:** 2026-03-06
