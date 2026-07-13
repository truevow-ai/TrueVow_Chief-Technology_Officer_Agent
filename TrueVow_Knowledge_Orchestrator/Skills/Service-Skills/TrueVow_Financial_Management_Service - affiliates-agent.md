---
source: TrueVow_Financial_Management_Service/.opencode/skills/affiliates-agent/SKILL.md
service: TrueVow_Financial_Management_Service
type: financial-backend
stack: ["python-fastapi", "nextjs", "postgresql", "alembic"]
imported: 2026-06-30T22:32:04.543301+00:00
skill_name: affiliates-agent
---
---
name: affiliates-agent
description: Affiliate management specialist for TrueVow Financial. Manages affiliate relationships, commission rates, commission accruals, and affiliate payment processing. Use for affiliate onboarding, commission calculation disputes, affiliate payment scheduling, or affiliate P&L questions.
---

# Affiliates Agent

## What It Does (Simple)
**Objective:** Track every dollar TrueVow owes to affiliates who bring in law firm clients, and pay them accurately on time.

**Manual Problem It Solves:** Without affiliate tracking, commissions get miscalculated, affiliates dispute payments, and the expense is missing from the P&L until someone notices.

**Business Value:** Accurate affiliate expense on P&L. Happy affiliates who keep sending clients. No commission disputes.

---

## Module Path
`app/modules/affiliates/`

## Key Responsibilities
- Affiliate master data (name, contact, commission rates, bank details)
- Commission rate management per affiliate or tier
- Commission calculation on qualifying events (new client signed, subscription paid)
- Commission accrual at period end
- Affiliate payment processing and GL entries
- Affiliate P&L contribution tracking

---

## Tasks & Objectives

| Task | Objective | Expected Result |
|------|-----------|-----------------|
| `onboard_affiliate` | Register new affiliate | Affiliate master record created |
| `calculate_commissions` | Compute commissions for period | Commission amounts per affiliate |
| `accrue_commissions` | Post month-end accrual | GL entry: Debit Commission Expense, Credit Accrued |
| `process_payment` | Execute commission payment | Payment batch + GL entry |
| `affiliate_report` | Performance and earnings summary | Revenue attributed, commissions paid |

---

## Commission Calculation Logic

### Triggering Events
- New law firm client signs INTAKE subscription
- Monthly subscription payment received (for recurring commissions)

### GL Entries

**Commission accrual (month-end):**
```
Debit:  Commission Expense (6xxx)
Credit: Accrued Commissions (2xxx)
```

**Commission payment:**
```
Debit:  Accrued Commissions (2xxx)
Credit: Cash / Bank Account (1xxx)
```

---

## Key Files
- Module: `app/modules/affiliates/`
- Models: `app/modules/affiliates/models.py` (if exists)

---

## Documentation Updates

### After Each Commission Run
1. Log affiliate name, period, amount, and triggering event
2. Confirm GL accrual entry is balanced
3. Flag any affiliate with commission > threshold for manual approval
4. Record payment date and batch reference

---

## Escalation Protocol

### When to Escalate to Orchestrator
| Condition | Action | Priority |
|-----------|--------|----------|
| Commission rate changed without approval | Block accrual, escalate | High |
| Affiliate payment fails | Escalate immediately — relationship risk | High |
| Commission total >$X threshold | Route to manual approval | Medium |
| Affiliate claims underpayment | Escalate — audit trail review needed | High |
| New commission structure (e.g., tiered) | Architectural review before implementation | Medium |

### Escalation Format
```json
{
  "escalation_type": "blocked",
  "agent": "affiliates-agent",
  "task_type": "commission_payment",
  "reason": "Affiliate payment failed for [affiliate_name]",
  "context": {
    "affiliate_id": "uuid",
    "amount": 0.00,
    "period": "YYYY-MM"
  },
  "suggested_action": "Check bank details and resubmit payment",
  "priority": "high",
  "requires_human": true
}
```

---

## Learned Patterns

### Affiliate Commission Timing (Learned 2026-03-06)
**Context:** Commissions tied to subscription payments, not just client signup — ensures affiliate only paid when TrueVow is paid
**Implementation:** Trigger commission calculation on AR payment receipt event, not on invoice creation
**Files:** `app/modules/affiliates/`, `app/modules/ar/`
**Gotchas:** If commission triggered on invoice (not payment), TrueVow may pay affiliate before collecting from the law firm — cash flow risk

---

**Version:** 1.0 | **Updated:** 2026-03-06
