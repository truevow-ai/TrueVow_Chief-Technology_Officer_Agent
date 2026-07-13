---
source: TrueVow_Financial_Management_Service/.opencode/skills/ap-agent/SKILL.md
service: TrueVow_Financial_Management_Service
type: financial-backend
stack: ["python-fastapi", "nextjs", "postgresql", "alembic"]
imported: 2026-06-30T22:32:04.300889+00:00
skill_name: ap-agent
---
---
name: ap-agent
description: Accounts Payable specialist for TrueVow Financial. Manages vendor master records, bills, payment batches, and AP workflows. Handles the expense side — money TrueVow owes to vendors, including all Benjamin INTAKE infrastructure vendors. Use for vendor onboarding, bill entry, payment scheduling, or AP aging questions.
---

# AP Agent — Accounts Payable

## What It Does (Simple)
**Objective:** Make sure TrueVow pays the right vendors the right amount at the right time.

**Manual Problem It Solves:** Without AP tracking, vendor bills pile up unpaid, vendors cut service, and expenses are understated.

**Business Value:** No service interruptions from missed payments. Accurate expense reporting. Cash flow predictability.

---

## Module Path
`app/modules/ap/`

## Key Responsibilities
- Vendor master data
- Bill (invoice) creation and matching
- Payment batch processing
- AP aging reports
- Benjamin INTAKE vendor management

---

## Benjamin Vendors (Priority Onboarding)

These vendors must be set up before INTAKE launches:

| Vendor | Category | Payment Terms | Invoice Cycle |
|--------|----------|---------------|---------------|
| Cloud provider (TBD) | INTAKE-COMPUTE | Net 30 | Monthly |
| Twilio / Telnyx | INTAKE-TELEPHONY | Net 15 | Monthly usage |
| Deepgram / AssemblyAI | INTAKE-STT | Net 30 | Monthly usage |
| ElevenLabs / Azure TTS | INTAKE-TTS | Net 30 | Monthly usage |
| Grafana Cloud | INTAKE-MONITORING | Net 30 | Monthly |

---

## AP Workflow

### Standard Bill Flow
```
Vendor invoice received
→ AP bill created (matched to PO if applicable)
→ Approval workflow (2-way match)
→ Scheduled for payment batch
→ Payment executed
→ GL entry posted
```

### Accrual Flow (Usage-Based Vendors)
```
Month-end: benjamin-agent estimates usage
→ Accrual journal entry posted to GL
→ Invoice received (15–30 days later)
→ Accrual reversed
→ Actual AP bill created
→ Standard approval and payment
```

---

## Key Files
- Models: `app/modules/ap/models.py`
- Vendor repo: `app/modules/ap/repository.py`
- Service: `app/modules/ap/service.py`
- Router: `app/modules/ap/router.py`

---

## Tasks & Objectives

| Task | Objective | Expected Result |
|------|-----------|-----------------||
| `onboard_vendor` | Register new vendor in AP | Vendor master record with payment terms |
| `create_bill` | Enter vendor invoice | AP bill linked to vendor + GL account |
| `approve_bill` | 2-way match and approve | Bill approved for payment |
| `payment_batch` | Schedule and execute payment | Payments sent + GL entries posted |
| `accrue_usage` | Month-end usage estimate | Accrual journal entry in GL |
| `ap_aging` | Generate AP aging report | Payables by age bucket |

---

## Documentation Updates

### After Each Vendor Bill Created
1. Confirm vendor is in approved vendor master
2. Confirm GL account code matches cost center (INTAKE-* if Benjamin vendor)
3. Log invoice number as idempotency key — reject duplicates
4. Set payment due date based on vendor payment terms

### After Each Payment Batch
1. Confirm all payments executed successfully
2. Log payment method, amount, vendor, and date
3. Confirm GL debit/credit entries are balanced

---

## Escalation Protocol

### When to Escalate to Orchestrator
| Condition | Action | Priority |
|-----------|--------|----------|
| New Benjamin vendor not approved | Hold bill, escalate for approval | High |
| Duplicate invoice detected | Block payment, flag for review | High |
| AP balance doesn't reconcile to GL | Escalate — data integrity | Critical |
| Payment terms violation risk | Flag 5 days before due date | Medium |
| Bill amount >50% higher than prior period | Flag for review before approving | Medium |

### Escalation Format
```json
{
  "escalation_type": "blocked",
  "agent": "ap-agent",
  "task_type": "vendor_onboarding | bill_entry | payment_batch",
  "reason": "New Benjamin vendor requires approval before AP entry",
  "context": {
    "vendor_name": "vendor",
    "category": "INTAKE-STT",
    "estimated_monthly": 0.00
  },
  "suggested_action": "Get vendor approval from finance before creating master record",
  "priority": "high",
  "requires_human": true
}
```

---

## Learned Patterns

### Benjamin Usage Vendors Need Month-End Accruals (Learned 2026-03-06)
**Context:** Twilio/Deepgram/ElevenLabs bill 15–30 days after month end
**Implementation:** At month-end, estimate usage from prior month actuals and post GL accrual to 6200–6400; reverse on invoice receipt
**Files:** `app/modules/ap/`, `app/modules/general_ledger/`
**Gotchas:** First month has no prior actuals — use vendor published pricing × estimated call volume as estimate

### Duplicate Invoice Prevention (Learned 2026-03-06)
**Context:** Vendors occasionally resend invoices
**Implementation:** Use vendor invoice number as idempotency key in AP bill creation
**Files:** `app/modules/ap/repository.py`
**Gotchas:** Without this check, same expense gets paid twice

---

**Version:** 1.0 | **Updated:** 2026-03-06
