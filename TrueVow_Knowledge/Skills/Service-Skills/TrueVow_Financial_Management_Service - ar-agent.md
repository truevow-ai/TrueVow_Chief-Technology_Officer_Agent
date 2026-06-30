---
source: TrueVow_Financial_Management_Service/.opencode/skills/ar-agent/SKILL.md
service: TrueVow_Financial_Management_Service
type: financial-backend
stack: ["python-fastapi", "nextjs", "postgresql", "alembic"]
imported: 2026-06-30T22:32:04.284215+00:00
skill_name: ar-agent
---
---
name: ar-agent
description: Accounts Receivable specialist for TrueVow Financial. Manages customer records, invoices, payments, deferred revenue recognition, and billing system integration. Handles the revenue side — money owed TO TrueVow from law firm clients. Use for invoice creation, payment allocation, aging reports, or deferred revenue questions.
---

# AR Agent — Accounts Receivable

## What It Does (Simple)
**Objective:** Track every dollar law firms owe TrueVow and ensure it gets collected and recorded correctly.

**Manual Problem It Solves:** Without AR management, invoices get sent but nobody tracks whether they were paid — revenue goes missing.

**Business Value:** Accurate revenue recognition, faster collections, clean aging reports for cash flow management.

---

## Module Path
`app/modules/ar/`

## Key Responsibilities
- Customer (law firm) master data
- Invoice creation and management
- Payment receipt and allocation
- Deferred revenue recognition (subscription billing)
- Billing system sync (external billing platform integration)
- AR aging reports

---

## Module Structure (Actual)
```
app/modules/ar/
├── api/routes/          # Route files
├── models/              # ORM models
├── repositories/        # DB query layer
├── schemas/             # Pydantic schemas (incl. pricing_schemas.py)
├── services/            # Business logic
│   ├── ar_posting_service.py
│   ├── ar_sync_service.py
│   ├── dashboard_stats_service.py
│   ├── deferred_revenue_service.py
│   └── pricing_service.py
└── integrations/        # External service adapters
    ├── billing_adapter.py          # Abstract base (ABC)
    └── http_billing_adapter.py     # Real HTTP implementation
```

---

## Billing Service Integration

AR integrates with an external **Billing Service** via adapter pattern:

### What the Billing Service Provides
- Tenant tier info (`solo` | `growth`)
- Feature access with pricing per use
- Add-on purchases
- **Founding Intelligence** pricing locks

### Pricing Endpoints
```
GET /api/v1/fm/pricing/tenants/{tenant_id}/feature-access
GET /api/v1/fm/pricing/tenants/{tenant_id}/feature-cost
GET /api/v1/fm/pricing/tenants/{tenant_id}/addons
GET /api/v1/fm/pricing/tenants/{tenant_id}/founding-intelligence
```

### Founding Intelligence Pricing Lock
Founding members have pricing locked until 2029-01-01:
```json
{
  "has_founding_benefits": true,
  "pricing_locked_until": "2029-01-01T00:00:00Z",
  "locked_unlock_price_cents": 9900,
  "is_still_locked": true
}
```
**Rule:** Never override founding member pricing without explicit unlock.

### Feature Cost Calculation
- INTAKE: $89/use (growth tier), $99/use (solo tier)
- SETTLE: $0 for founding members, otherwise $99/use
- Usage over monthly quota = billable overage

---

## Revenue Model Context

TrueVow bills law firms for:
- INTAKE service subscriptions (monthly recurring)
- Possibly usage-based components per call/lead

### Deferred Revenue Rule
For subscription payments received in advance:
```
On payment receipt:
  Debit:  Cash
  Credit: Deferred Revenue (liability)

Monthly recognition:
  Debit:  Deferred Revenue
  Credit: Revenue
```

---

## Key Files
- Models: `app/modules/ar/models.py`
- Customer repo: `app/modules/ar/repository.py`
- Invoice service: `app/modules/ar/service.py`
- Router: `app/modules/ar/router.py`

---

## Tasks & Objectives

| Task | Objective | Expected Result |
|------|-----------|-----------------||
| `create_customer` | Register new law firm client | Customer master record |
| `create_invoice` | Issue invoice to law firm | Invoice posted to AR ledger |
| `allocate_payment` | Match payment to invoice | Invoice marked paid, GL entry posted |
| `recognize_revenue` | Run deferred revenue schedule | Monthly revenue recognition entries |
| `ar_aging` | Generate aging report | Receivables by age bucket |
| `sync_billing` | Sync from external billing platform | Invoices/payments imported |

---

## Documentation Updates

### After Each Invoice Created
1. Confirm invoice is linked to correct law firm customer
2. Log invoice number, amount, due date, and GL account
3. Flag if invoice amount > prior period average (unusual spike)

### After Each Payment Received
1. Confirm full allocation against invoice(s)
2. Log payment method, amount, and AR aging impact
3. Trigger deferred revenue schedule if subscription prepayment

---

## Escalation Protocol

### When to Escalate to Orchestrator
| Condition | Action | Priority |
|-----------|--------|----------|
| Invoice > 60 days overdue | Flag for collections review | High |
| Deferred revenue schedule mismatch | Escalate — revenue recognition error | Critical |
| Billing sync failure | Escalate — revenue will be missed | High |
| New pricing model for INTAKE | Confirm recognition treatment | Medium |
| Partial payment with no allocation instruction | Hold, escalate | Medium |

### Escalation Format
```json
{
  "escalation_type": "blocked",
  "agent": "ar-agent",
  "task_type": "payment_allocation | billing_sync | revenue_recognition",
  "reason": "Invoice overdue >60 days with no payment",
  "context": {
    "invoice_id": "uuid",
    "customer": "law firm name",
    "amount_outstanding": 0.00,
    "days_overdue": 0
  },
  "suggested_action": "Initiate collections outreach",
  "priority": "high",
  "requires_human": true
}
```

---

## Learned Patterns

### Billing Integration Uses Adapter Pattern — Always Inject, Never Hardcode (Learned 2026-03-06)
**Context:** AR module uses `billing_adapter.py` (ABC) + `http_billing_adapter.py` to decouple from billing service
**Implementation:** Inject adapter via dependency injection; use `MockBillingAdapter` in tests
**Files:** `app/modules/ar/integrations/`
**Gotchas:** If you hardcode `HTTPBillingAdapter` in service layer, tests will make real HTTP calls and fail

### Founding Intelligence Pricing Is Immutable (Learned 2026-03-06)
**Context:** Founding members have pricing locked contractually until 2029-01-01
**Implementation:** `pricing_service.check_founding_intelligence_benefits()` returns lock status; never apply price overrides to locked accounts
**Files:** `app/modules/ar/services/pricing_service.py`
**Gotchas:** Calculating feature cost for founding members without checking lock status will apply wrong price

### Subscription Billing Creates Deferred Revenue (Learned 2026-03-06)
**Context:** Law firms pay monthly subscriptions for INTAKE service; payments received in advance must be deferred
**Implementation:** On payment receipt: Credit Deferred Revenue (liability). On month recognition: Debit Deferred Revenue, Credit Revenue
**Files:** `app/modules/ar/services/deferred_revenue_service.py`, `app/modules/general_ledger/`
**Gotchas:** Never book full subscription payment directly to revenue in one shot — violates ASC 606 revenue recognition

### Billing Sync Idempotency (Learned 2026-03-06)
**Context:** External billing platform may resend same invoice/payment events
**Implementation:** Use `external_invoice_id` as idempotency key — reject duplicates silently
**Files:** `app/modules/ar/repositories/`
**Gotchas:** Without this check, duplicate invoices inflate AR and revenue

---

**Version:** 1.0 | **Updated:** 2026-03-06
