---
source: TrueVow_Financial_Management_Service/.opencode/skills/treasury-agent/SKILL.md
service: TrueVow_Financial_Management_Service
type: financial-backend
stack: ["python-fastapi", "nextjs", "postgresql", "alembic"]
imported: 2026-06-30T22:32:04.367908+00:00
skill_name: treasury-agent
---
---
name: treasury-agent
description: Treasury specialist for TrueVow Financial. Manages bank accounts, bank transaction processing, transfers between accounts, foreign exchange, and settlement. Use for bank reconciliation, cash position, FX transactions, or settlement processing questions.
---

# Treasury Agent

## What It Does (Simple)
**Objective:** Know TrueVow's exact cash position at all times and ensure every bank transaction is recorded.

**Manual Problem It Solves:** Without treasury management, bank balances in the system diverge from actual bank balances.

**Business Value:** Accurate cash flow reporting. No overdrafts. Clean reconciliation for audits.

---

## Module Path
`app/modules/treasury/`

## Schema Status (Known Gap)
**CRITICAL:** The following treasury tables do NOT exist in the database yet:
- `bank_account`
- `bank_transaction` 
- `settlement`
- `fx_conversion`
- `transfer`
- `sync_cursor`

This is a **pre-existing gap** documented in `WORKING_CACHE.md`. When these tables are created, re-run `database/row_audit_triggers.sql` to attach audit triggers (idempotent operation).

## Key Responsibilities
- Bank account master data
- Bank transaction ingestion and matching
- Bank reconciliation
- Interbank transfers
- Foreign exchange transactions
- Settlement processing

---

## GL Entries

### Transfer between accounts
```
Debit:  Destination Bank Account (1xxx)
Credit: Source Bank Account (1xxx)
```

### FX transaction
```
Debit:  Foreign Currency Account (1xxx) [at spot rate]
Credit: USD Account (1xxx)
Credit/Debit: FX Gain/Loss (7xxx)      [rate difference]
```

---

## Key Files
- Models: `app/modules/treasury/models.py`
- Service: `app/modules/treasury/service.py`
- Router: `app/modules/treasury/router.py`

---

## Tasks & Objectives

| Task | Objective | Expected Result |
|------|-----------|-----------------||
| `register_bank_account` | Add bank account to system | Bank account master record |
| `ingest_transactions` | Import bank statement transactions | Transactions loaded for matching |
| `reconcile` | Match bank transactions to GL | Reconciliation completed and locked |
| `execute_transfer` | Transfer between bank accounts | Transfer posted + GL entries |
| `fx_transaction` | Record foreign exchange transaction | FX entry with gain/loss calculated |
| `settlement` | Process settlement | Settlement confirmed + GL posted |

---

## Documentation Updates

### After Each Reconciliation
1. Log reconciliation date, period, entity, and account
2. Log unmatched item count and total value
3. Confirm GL cash balance matches bank statement balance
4. Lock the reconciliation — no further changes to matched transactions

### After Each Transfer
1. Confirm debit and credit entries posted to correct accounts
2. Log transfer amount, date, source, and destination

---

## Escalation Protocol

### When to Escalate to Orchestrator
| Condition | Action | Priority |
|-----------|--------|----------|
| Bank balance doesn't reconcile to GL | Escalate immediately | Critical |
| Unmatched transactions >7 days | Flag for manual review | High |
| FX rate outside expected range | Confirm rate source | Medium |
| Large unidentified transaction | Escalate — possible fraud | Critical |

### Escalation Format
```json
{
  "escalation_type": "error",
  "agent": "treasury-agent",
  "task_type": "reconciliation | transfer | fx_transaction",
  "reason": "Bank balance doesn't reconcile to GL by $X",
  "context": {
    "bank_account": "account reference",
    "period": "YYYY-MM",
    "variance": "amount",
    "unmatched_count": 0
  },
  "suggested_action": "Review unmatched transactions and check for missing GL entries",
  "priority": "critical",
  "requires_human": true
}
```

---

## Learned Patterns

### Treasury Tables Missing From Database (Learned 2026-03-06)
**Context:** 6 core treasury tables don't exist in DB — code exists but schema doesn't
**Implementation:** When creating these tables, must also re-run `row_audit_triggers.sql` to attach audit triggers
**Files:** `app/modules/treasury/models/`, `database/row_audit_triggers.sql`
**Gotchas:** Code may reference tables that don't exist — verify table existence before running treasury-related queries

### Benjamin Vendor Payments Flow Through Treasury (Learned 2026-03-06)
**Context:** When AP pays Benjamin vendors (Twilio, etc.), the cash exits a bank account managed by Treasury
**Implementation:** AP payment batch triggers Treasury debit to cash account; Treasury reconciliation must match these AP payment entries
**Files:** `app/modules/treasury/`, `app/modules/ap/`
**Gotchas:** If AP payment is recorded but Treasury transaction not imported, reconciliation will show unmatched debit

---

**Version:** 1.0 | **Updated:** 2026-03-06
