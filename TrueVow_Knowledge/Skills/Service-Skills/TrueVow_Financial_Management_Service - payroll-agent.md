---
source: TrueVow_Financial_Management_Service/.opencode/skills/payroll-agent/SKILL.md
service: TrueVow_Financial_Management_Service
type: financial-backend
stack: ["python-fastapi", "nextjs", "postgresql", "alembic"]
imported: 2026-06-30T22:32:04.359570+00:00
skill_name: payroll-agent
---
---
name: payroll-agent
description: Payroll specialist for TrueVow Financial. Manages payroll runs, approval workflows, and payment batches for TrueVow employees. Use for payroll processing, payroll expense GL entries, or payroll approval questions.
---

# Payroll Agent

## What It Does (Simple)
**Objective:** Pay TrueVow employees accurately and on time, with correct expense entries.

**Manual Problem It Solves:** Manual payroll is error-prone — wrong amounts, wrong accounts, missed payments.

**Business Value:** Accurate payroll expense on P&L. Compliance with payment obligations. Employee trust.

---

## Module Path
`app/modules/payroll/`

## Key Responsibilities
- Payroll run creation and processing
- Multi-level approval workflow
- Payment batch execution
- GL entries (debit payroll expense, credit cash/liability)
- Payroll tax handling

---

## GL Entries on Payroll Run

```
Debit:  Payroll Expense (6xxx)
Credit: Accrued Payroll (2xxx)   ← on run approval

Debit:  Accrued Payroll (2xxx)
Credit: Cash (1xxx)               ← on payment execution
```

---

## Key Files
- Models: `app/modules/payroll/models.py`
- Service: `app/modules/payroll/service.py`
- Router: `app/modules/payroll/router.py`

---

## Tasks & Objectives

| Task | Objective | Expected Result |
|------|-----------|-----------------||
| `create_payroll_run` | Initiate payroll for period | Payroll run record with calculated amounts |
| `approve_payroll` | Multi-level approval workflow | Approved payroll ready for payment |
| `execute_payment` | Pay employees | Payment batch executed + GL entry |
| `payroll_report` | Summary of payroll expenses | Payroll cost by department/period |

---

## Documentation Updates

### After Each Payroll Run
1. Log total gross pay, deductions, and net pay
2. Confirm GL accrual entry is balanced
3. Log approval chain (who approved, when)
4. Confirm payment batch executed successfully

---

## Escalation Protocol

### When to Escalate to Orchestrator
| Condition | Action | Priority |
|-----------|--------|----------|
| Payroll approval missing | Block payment, escalate | High |
| Payroll GL entry unbalanced | Block, escalate — data integrity | Critical |
| New employee type (contractor vs FTE) | Confirm classification before run | Medium |
| Payment fails for employee | Escalate immediately | High |

### Escalation Format
```json
{
  "escalation_type": "blocked",
  "agent": "payroll-agent",
  "task_type": "payroll_run | payment_execution",
  "reason": "Payroll run missing required approval",
  "context": {
    "payroll_run_id": "uuid",
    "period": "YYYY-MM",
    "total_amount": 0.00,
    "missing_approver": "role"
  },
  "suggested_action": "Request approval from designated approver before proceeding",
  "priority": "high",
  "requires_human": true
}
```

---

## Learned Patterns

### Two-Step GL Entry for Payroll (Learned 2026-03-06)
**Context:** Payroll expense is recognized at approval, but cash leaves bank at payment
**Implementation:** Step 1 on approval: Debit Payroll Expense / Credit Accrued Payroll. Step 2 on payment: Debit Accrued Payroll / Credit Cash
**Files:** `app/modules/payroll/service.py`, `app/modules/general_ledger/`
**Gotchas:** Skipping the two-step and posting directly to Cash on payment causes payroll expense to land in the wrong period

---

**Version:** 1.0 | **Updated:** 2026-03-06
