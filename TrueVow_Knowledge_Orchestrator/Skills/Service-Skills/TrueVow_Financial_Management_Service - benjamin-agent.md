---
source: TrueVow_Financial_Management_Service/.opencode/skills/benjamin-agent/SKILL.md
service: TrueVow_Financial_Management_Service
type: financial-backend
stack: ["python-fastapi", "nextjs", "postgresql", "alembic"]
imported: 2026-06-30T22:32:04.555364+00:00
skill_name: benjamin-agent
---
---
name: benjamin-agent
description: Tracks all operational costs for Benjamin, TrueVow's INTAKE voice AI engine. Manages vendor master records, monthly AP accruals for usage-based vendors, cost center reporting, and budget vs actuals for the INTAKE service line. Use for any Benjamin infrastructure cost, vendor onboarding, or INTAKE service P&L question.
---

# Benjamin Agent (INTAKE Service — Cost & Vendor Management)

## What It Does (Simple)
**Objective:** Know exactly what TrueVow spends on Benjamin every month, which vendors are paid, and whether spending is on budget.

**Manual Problem It Solves:** Without this agent, Benjamin infrastructure costs get lost in general AP with no visibility into which service line (INTAKE vs DRAFT vs VERIFY vs SETTLE) is spending what.

**Business Value:** Clean P&L per service line from day one. No surprise bills. Investor-ready unit economics for INTAKE.

---

## Benjamin Infrastructure Overview

### Scale Target
- 50 law firm clients
- 100 concurrent calls peak
- 9 servers total

### Monthly Budget Range
```
Low:  $1,200/month
High: $2,500/month
```

---

## Vendor Registry

### Compute (Fixed Monthly)
| Vendor Type | Node Role | Count | Est. Monthly |
|-------------|-----------|-------|--------------|
| Cloud provider | Edge + Audio | 2 nodes × 8vCPU/16GB | $160–400 |
| Cloud provider | STT cluster | 2 nodes × 16vCPU/32GB | $300–600 |
| Cloud provider | App cluster | 2 nodes × 8vCPU/16GB | $160–400 |
| Cloud provider | PostgreSQL | 1 node × 8vCPU/32GB NVMe | $80–200 |
| Cloud provider | Redis | 1 node × 4vCPU/8GB | $40–80 |
| Cloud provider | Monitoring | 1 node × 4vCPU/8GB | $40–80 |

### Usage-Based (Requires Monthly Accrual)
| Vendor Type | Service | Billing Unit | Est. Monthly |
|-------------|---------|--------------|--------------|
| Twilio / Telnyx | Telephony | Per-minute + DID numbers | $200–500 |
| Deepgram / AssemblyAI | STT API (if external) | Per audio minute | $100–300 |
| ElevenLabs / Azure TTS | TTS synthesis | Per 1,000 characters | $50–200 |
| Grafana Cloud | Monitoring (if cloud) | Per seat/metric | $50–100 |

---

## AP Workflow by Vendor Type

### Fixed Monthly Vendors (Compute)
```
Invoice received → AP bill created → Approval → Payment
```
Standard AP workflow. No accrual needed.

### Usage-Based Vendors (Telephony, STT, TTS)
```
Month-end → Estimate usage → Post accrual entry to GL
Invoice received → Reverse accrual → Post actual AP bill → Approval → Payment
```

**Accrual Journal Entry (month-end estimate):**
```
Debit:  6xxx Benjamin INTAKE OpEx   [estimated amount]
Credit: 2xxx Accrued Liabilities     [estimated amount]
```

**Reversal on invoice receipt:**
```
Debit:  2xxx Accrued Liabilities     [estimated amount]
Credit: 6xxx Benjamin INTAKE OpEx   [estimated amount]
```

**Actual AP bill:**
```
Debit:  6xxx Benjamin INTAKE OpEx   [actual invoice amount]
Credit: 2xxx Accounts Payable        [actual invoice amount]
```

---

## Cost Center: INTAKE Service

All Benjamin costs should be tagged to cost center: **`INTAKE`**

Sub-categories:
| Code | Description |
|------|-------------|
| INTAKE-COMPUTE | Server/cloud infrastructure |
| INTAKE-TELEPHONY | Voice/phone vendor costs |
| INTAKE-STT | Speech-to-text vendor costs |
| INTAKE-TTS | Text-to-speech vendor costs |
| INTAKE-MONITORING | Observability tools |

---

## Budget vs Actuals Tracking

### Monthly Budget
| Cost Center | Budget Low | Budget High |
|-------------|------------|-------------|
| INTAKE-COMPUTE | $780 | $1,760 |
| INTAKE-TELEPHONY | $200 | $500 |
| INTAKE-STT | $100 | $300 |
| INTAKE-TTS | $50 | $200 |
| INTAKE-MONITORING | $50 | $100 |
| **TOTAL** | **$1,180** | **$2,860** |

### Variance Alerts
- >10% over budget: flag for review
- >20% over budget: escalate to management
- New vendor line item: always escalate for approval first

---

## Vendor Onboarding Checklist

When a new Benjamin vendor is approved:
1. Create vendor master in AP module
2. Set payment terms (Net 15 or Net 30)
3. Tag with cost center `INTAKE-{subcategory}`
4. Set up accrual schedule if usage-based
5. Document billing cycle (monthly invoice date)
6. Update this SKILL.md with vendor details

---

## Scaling Cost Projections

| Stage | Customers | Concurrent Calls | Est. Monthly |
|-------|-----------|-----------------|--------------|
| Launch | 50 | 100 | $1,200–2,500 |
| Growth | 100 | 200 | +1 STT node ~$2,000–3,500 |
| Scale | 200 | 400 | +STT+App node ~$3,500–5,500 |
| Large | 500 | 1,000 | Split audio plane ~$7,000–12,000 |
| Enterprise | 1,000 | 2,000+ | GPU STT cluster ~$15,000–25,000 |

---

## Documentation Updates

### After Each New Vendor Onboarded
1. Add vendor to Vendor Registry table in this file
2. Create vendor master record in AP module
3. Confirm cost center code assigned (INTAKE-*)
4. Set accrual schedule if usage-based
5. Update Monthly Budget table if new cost line

### After Each Month-End Accrual
1. Log estimated amounts per vendor
2. Log basis for estimate (prior actuals or pricing × volume)
3. Update Budget vs Actuals table with actuals when invoices arrive

---

## Escalation Protocol

### When to Escalate to Orchestrator
| Condition | Action | Priority |
|-----------|--------|----------|
| New vendor not in registry | Escalate for approval before AP entry | High |
| Monthly actuals >20% over budget | Escalate immediately | High |
| New service line cost appears | Confirm it belongs to INTAKE vs other service | Medium |
| GPU node decision | Escalate — capital vs opex classification needed | Medium |
| Vendor service outage | Alert engineering + escalate | High |

### Escalation Format
```json
{
  "escalation_type": "blocked",
  "agent": "benjamin-agent",
  "task_type": "vendor_onboarding | monthly_accrual | budget_variance",
  "reason": "New vendor [name] not in approved registry",
  "context": {
    "vendor": "vendor name",
    "category": "INTAKE-STT",
    "estimated_monthly": 0.00
  },
  "suggested_action": "Get finance approval, add to vendor registry, then create AP master record",
  "priority": "high",
  "requires_human": true
}
```

---

## Key Files (When Implemented)
- Vendor master: `app/modules/ap/` (vendor records)
- Cost center config: TBD
- Accrual templates: TBD
- Budget config: TBD

---

## Learned Patterns

### Usage-Based Vendor Billing Lag (Learned 2026-03-06)
**Context:** Twilio, Deepgram, ElevenLabs all invoice 15–30 days after the billing period ends
**Implementation:** Accrue at month-end using prior month actuals as estimate; true-up on invoice receipt
**Files:** GL accrual entries, AP bills
**Gotchas:** First month has no prior actuals — use vendor published pricing × estimated call volume

---

**Version:** 1.0 | **Updated:** 2026-03-06
