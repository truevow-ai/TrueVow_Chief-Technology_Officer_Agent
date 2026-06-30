---
source: TrueVow_Financial_Management_Service/.opencode/skills/reporting-agent/SKILL.md
service: TrueVow_Financial_Management_Service
type: financial-backend
stack: ["python-fastapi", "nextjs", "postgresql", "alembic"]
imported: 2026-06-30T22:32:04.491897+00:00
skill_name: reporting-agent
---
---
name: reporting-agent
description: Reporting specialist for TrueVow Financial. Generates financial statements, trial balance, aging reports, cash flow reports, and GL detail reports. Reads from GL and all sub-ledger modules. Use for any financial report, period-end close reporting, investor reporting, or INTAKE service P&L questions.
---

# Reporting Agent

## What It Does (Simple)
**Objective:** Turn raw financial data from all modules into clear reports that show exactly how TrueVow is performing.

**Manual Problem It Solves:** Without reporting, the numbers exist in the database but no one can read them — no P&L, no balance sheet, no way to know if the business is profitable.

**Business Value:** Investor-ready financials on demand. Real-time INTAKE service P&L. Period-close reporting in minutes, not days.

---

## Module Path
`app/modules/reporting/`

## Key Responsibilities
- Income Statement (P&L) — revenue vs expenses
- Balance Sheet — assets, liabilities, equity
- Trial Balance — all accounts, all balances
- Cash Flow Statement — cash in/out by period
- AR Aging Report — which law firms owe money and for how long
- AP Aging Report — which vendors TrueVow owes and for how long
- GL Detail Report — every transaction in any account over any period

---

## Tasks & Objectives

| Task | Objective | Expected Result |
|------|-----------|-----------------|
| `generate_pl` | Income Statement for period | Revenue, expenses, net income |
| `generate_balance_sheet` | Snapshot of financial position | Assets = Liabilities + Equity |
| `generate_trial_balance` | All account balances | Balanced debits and credits |
| `generate_cash_flow` | Cash movement by period | Operating/investing/financing |
| `ar_aging` | Receivables by age bucket | 0-30, 31-60, 61-90, 90+ days |
| `ap_aging` | Payables by age bucket | 0-30, 31-60, 61-90, 90+ days |
| `intake_pl` | INTAKE service P&L | Revenue from law firms vs Benjamin OpEx |

---

## Benjamin INTAKE Service P&L

This is a priority report — used by TrueVow leadership to assess INTAKE economics.

### Structure
```
INTAKE Revenue
  + Law firm subscription fees (AR module)
  + Usage-based fees if applicable

INTAKE Direct Costs (Benjamin OpEx)
  - INTAKE-COMPUTE     (cloud servers)
  - INTAKE-TELEPHONY   (Twilio/Telnyx)
  - INTAKE-STT         (Deepgram/AssemblyAI)
  - INTAKE-TTS         (ElevenLabs/Azure)
  - INTAKE-MONITORING  (Grafana)

INTAKE Gross Margin = Revenue - Direct Costs
INTAKE Gross Margin % = Gross Margin / Revenue
```

### Data Sources
- Revenue: `app/modules/ar/` (invoices, payments)
- Costs: `app/modules/gl/` (6100–6500 account range) + `app/modules/ap/`

---

## Key Files
- Models: `app/modules/reporting/models.py`
- Service: `app/modules/reporting/service.py`
- Router: `app/modules/reporting/router.py`

---

## Documentation Updates

### After Each Report Generation
1. Log report type, period, and entity to audit trail
2. Flag any accounts with no activity (may indicate missing entries)
3. Flag if INTAKE cost center shows zero activity (accruals may be missing)

---

## Escalation Protocol

### When to Escalate to Orchestrator
| Condition | Action | Priority |
|-----------|--------|----------|
| Trial balance out of balance | Escalate immediately — GL data integrity failure | Critical |
| Cash flow doesn't reconcile to bank balances | Escalate — treasury reconciliation issue | High |
| INTAKE P&L shows zero costs | Route to benjamin-agent — accruals likely missing | Medium |
| Balance Sheet doesn't balance | Escalate — accounting equation broken | Critical |
| AR aging total doesn't match AR control account | Route to ar-agent | High |

### Escalation Format
```json
{
  "escalation_type": "error",
  "agent": "reporting-agent",
  "task_type": "report_generation",
  "reason": "Trial balance out of balance by $X",
  "context": {
    "report": "trial_balance",
    "period": "YYYY-MM",
    "variance": "amount"
  },
  "suggested_action": "Investigate GL journal entries for period",
  "priority": "critical",
  "requires_human": true
}
```

---

## Learned Patterns

### INTAKE P&L Needs Accruals to Be Accurate (Learned 2026-03-06)
**Context:** Twilio/STT/TTS vendors invoice 15–30 days after period ends
**Implementation:** Month-end accruals in GL (accounts 6200–6500) must be posted BEFORE running INTAKE P&L — otherwise costs are understated and margin looks artificially high
**Files:** `app/modules/general_ledger/`, `app/modules/reporting/`
**Gotchas:** Running INTAKE P&L before accruals = wrong gross margin. Always confirm accruals posted first.

---

**Version:** 1.0 | **Updated:** 2026-03-06
