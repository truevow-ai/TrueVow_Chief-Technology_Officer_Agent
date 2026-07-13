---
source: TrueVow_Financial_Management_Service/.opencode/skills/orchestrator/SKILL.md
service: TrueVow_Financial_Management_Service
type: financial-backend
stack: ["python-fastapi", "nextjs", "postgresql", "alembic"]
imported: 2026-06-30T22:32:03.987733+00:00
skill_name: orchestrator
---
---
name: orchestrator
description: Master orchestrator for TrueVow Financial Management. Understands full architecture across GL, AR, AP, Payroll, Treasury, Intercompany, Reporting, and Affiliates modules. Manages specialized agents, detects gaps between checkpoints, routes tasks, and maintains all skill files. Also tracks Benjamin INTAKE operational costs.
---

# Orchestrator Agent

## What It Does (Simple)
**Objective:** Be the master brain that knows everything about TrueVow Financial and delegates work to the right specialist.

**Manual Problem It Solves:** Without an orchestrator, every AI session restarts with zero knowledge — same questions asked, same mistakes made, same patterns discovered from scratch.

**Business Value:** Institutional memory that compounds. Faster delivery, fewer repeated bugs, consistent patterns across all 9 financial modules.

---

## References
- **Rules:** `AGENTS.md`
- **Domain:** `.opencode/skills/fintech-patterns/SKILL.md`
- **Repo Type:** Python (FastAPI) + Node (Next.js) — Monorepo

---

## AGENT REGISTRY

### Tool Agents (Development)
| Agent | Skill File | Purpose |
|-------|------------|---------|
| search-agent | `.opencode/skills/search-agent/SKILL.md` | Find code, trace dependencies, locate patterns |
| code-agent | `.opencode/skills/code-agent/SKILL.md` | Write/modify code, follow repo patterns |

### Application Agents (Financial Modules)
| Agent | Skill File | Purpose |
|-------|------------|---------|
| gl-agent | `.opencode/skills/gl-agent/SKILL.md` | General Ledger, journal entries, chart of accounts |
| ar-agent | `.opencode/skills/ar-agent/SKILL.md` | Accounts Receivable, invoices, payments, deferred revenue |
| ap-agent | `.opencode/skills/ap-agent/SKILL.md` | Accounts Payable, vendor bills, AP workflows |
| payroll-agent | `.opencode/skills/payroll-agent/SKILL.md` | Payroll runs, approvals, payment batches |
| treasury-agent | `.opencode/skills/treasury-agent/SKILL.md` | Bank accounts, transactions, FX, settlements |
| intercompany-agent | `.opencode/skills/intercompany-agent/SKILL.md` | Intercompany transfers, royalties, reconciliation |
| reporting-agent | `.opencode/skills/reporting-agent/SKILL.md` | Financial statements, trial balance, aging, cash flow |
| affiliates-agent | `.opencode/skills/affiliates-agent/SKILL.md` | Affiliate management |
| benjamin-agent | `.opencode/skills/benjamin-agent/SKILL.md` | Benjamin INTAKE voice AI — vendor cost tracking, OpEx budgeting |

---

## DELEGATION PROTOCOL

### Task Routing
| User Request | Primary Agent | Supporting |
|--------------|---------------|------------|
| "Where is X?" | search-agent | — |
| "Add feature to GL" | code-agent | search-agent, gl-agent |
| "Fix AR bug" | code-agent | search-agent, ar-agent |
| "Add payroll endpoint" | code-agent | search-agent, payroll-agent |
| "Benjamin vendor cost" | benjamin-agent | ar-agent (AP side) |
| "New migration" | code-agent | search-agent |
| "Report on cash flow" | reporting-agent | treasury-agent |
| "Intercompany reconciliation" | intercompany-agent | gl-agent |

---

## ARCHITECTURE OVERVIEW

### Backend (Python / FastAPI)
```
app/
├── main.py                  # Entry point, router registration
├── api/                     # API layer
├── auth/                    # Auth & authorization
├── core/                    # Shared infrastructure (DB, config, security)
└── modules/
    ├── general_ledger/      # GL module
    ├── ar/                  # Accounts Receivable
    ├── ap/                  # Accounts Payable
    ├── payroll/             # Payroll
    ├── treasury/            # Treasury & banking
    ├── intercompany/        # Intercompany
    ├── reporting/           # Financial reporting
    └── affiliates/          # Affiliate management
```

### Frontend (Next.js / TypeScript)
```
frontend/
├── app/                     # Next.js app router
├── components/              # UI components
├── hooks/                   # Custom hooks
├── contexts/                # React contexts
├── lib/                     # API clients, utilities
└── types/                   # TypeScript types
```

### Infrastructure
```
infra/
└── database/                # Migrations, schema
```

### Tech Stack
- Backend: Python + FastAPI + SQLAlchemy + Alembic + PostgreSQL
- Frontend: Next.js + TypeScript + Tailwind CSS
- Auth: JWT
- Database: Supabase (PostgreSQL)
- Package manager (frontend): pnpm

---

## TRUTH COMMANDS

### Backend
```bash
alembic upgrade head
python -m pytest tests/ -v
```

### Frontend
```bash
pnpm install
pnpm lint
pnpm build
```

---

## CHECKPOINT MANAGEMENT

### Gap Detection — Analyze On Each Session
1. Schema/migration changes since last checkpoint
2. New API endpoints added
3. Module integration changes
4. Frontend component changes
5. New patterns discovered

### Skill Update Protocol
| Change Type | Update File |
|-------------|-------------|
| Architecture change | orchestrator/SKILL.md |
| New financial pattern | fintech-patterns.md |
| New search pattern | search-agent/SKILL.md |
| New code pattern | code-agent/SKILL.md |
| Module-specific | {module}-agent/SKILL.md |
| Benjamin cost data | benjamin-agent/SKILL.md |

---

## SELF-IMPROVEMENT CYCLE

### Every Agent Must
1. **Log interactions** — track what was done and outcome
2. **Track patterns** — note recurring situations and their solutions
3. **Flag improvements** — suggest skill updates when better approaches found
4. **Update learned patterns** — document new knowledge in relevant SKILL.md

### After Each Session
1. Review what was accomplished vs planned
2. Identify new patterns learned (RLS gotchas, accounting rules, vendor behaviours)
3. Update relevant SKILL.md files with new patterns
4. Flag any technical debt discovered
5. Update `docs/01-main/IMPLEMENTATION_PROGRESS.md`

### Continuous Improvement Loop
```
Task → Execute → Result → Analyze → Update Skill → Next Task
                              ↓
                    If pattern new:
                    Append to relevant agent's "Learned Patterns"
                    If architectural decision:
                    Create ADR in docs/01-main/adr/
```

### Skill Update Trigger Events
| Event | Action | Target File |
|-------|--------|-------------|
| New Benjamin vendor onboarded | Update vendor registry | `benjamin-agent/SKILL.md` |
| New GL account range needed | Document account structure | `gl-agent/SKILL.md` |
| New billing model for law firms | Document recognition treatment | `ar-agent/SKILL.md` |
| RLS bug discovered | Document gotcha | `search-agent/SKILL.md` + `fintech-patterns.md` |
| New module added | Add agent to registry | `orchestrator/SKILL.md` |
| New code pattern discovered | Document pattern | `code-agent/SKILL.md` |

---

## DOCUMENTATION UPDATES

### After Each Milestone
1. Update `docs/01-main/IMPLEMENTATION_PROGRESS.md`
2. Create `docs/01-main/MILESTONE_{N}_CHECKPOINT.md`
3. Update relevant SKILL.md files with new patterns
4. Create ADR if architectural decision was made

### After Each Benjamin Vendor Decision
1. Update `benjamin-agent/SKILL.md` vendor registry
2. Update `ap-agent/SKILL.md` Benjamin vendors table
3. Update `fintech-patterns.md` cost categories if new category

---

## ESCALATION PROTOCOL

### Standard Escalation Format (All Agents)
```json
{
  "escalation_type": "error | blocked | uncertain | resource_limit | security",
  "agent": "agent_name",
  "task_type": "what_was_attempted",
  "reason": "why escalating",
  "context": {
    "relevant": "data"
  },
  "suggested_action": "what to try next",
  "priority": "critical | high | medium | low",
  "requires_human": true
}
```

### Escalation Types
| Type | When | Priority |
|------|------|----------|
| `error` | Task failed after retries | High |
| `blocked` | Missing dependency or approval | High |
| `uncertain` | Low confidence in result | Medium |
| `resource_limit` | Rate or cost limit hit | Medium |
| `security` | Potential threat detected | Critical |

---

## LEARNED PATTERNS

### Multi-Tenant RLS Enforcement (Learned 2026-03-06)
**Context:** All financial data is tenant-isolated via PostgreSQL Row Level Security
**Implementation:** Every table has `legal_entity_id` + RLS policies; queries must always include tenant context
**Files:** `infra/database/`, `app/core/`, all module models
**Gotchas:** Missing tenant context causes RLS to block all rows silently — not an error, just empty results

### Benjamin Cost Tracking (Learned 2026-03-06)
**Context:** TrueVow pays all Benjamin INTAKE infrastructure vendors from company accounts
**Implementation:** Benjamin costs tracked as operational AP entries under a Benjamin/INTAKE cost center
**Files:** `app/modules/ap/` (vendor master), future: benjamin cost center config
**Gotchas:** Usage-based vendors (telephony, STT, TTS) need accrual entries monthly — invoices lag actual usage

### Milestone "Complete (90%)" Pattern Indicates Deferred Edge Cases (Learned 2026-03-06)
**Context:** Historical milestones marked 85-95% complete but never reached 100% — accessibility, mobile testing, cross-browser testing always deferred
**Implementation:** When seeing "Complete (90%)", immediately ask: "What are the remaining 10% edge cases?"
**Files:** `docs/00-main/IMPLEMENTATION_PROGRESS.md`, all milestone checkpoints
**Gotchas:** Status "Complete" without qualification may hide significant unfinished work; always verify scope

### Pre-Existing Schema Gaps Block Full Audit Coverage (Learned 2026-03-06)
**Context:** Migration 006 deployed row audit triggers but only covered 47/53 tables — 6 treasury tables don't exist in DB
**Implementation:** Document missing tables in WORKING_CACHE; make audit trigger SQL idempotent so it can be re-run when tables created
**Files:** `database/row_audit_triggers.sql`, `docs/00-main/WORKING_CACHE.md`
**Gotchas:** "DONE" status on migrations can be misleading if target tables are missing; always verify table existence before claiming audit coverage complete

### Windows + Supabase Requires Connection Pooler Workaround (Learned 2026-03-06)
**Context:** Direct psql connection fails with DNS resolution error on Windows; connection pooler (aws-1-us-east-1.pooler.supabase.com) works
**Implementation:** Always use pooler URL for database operations on Windows environments
**Files:** `.env.local`, `app/core/db.py`
**Gotchas:** DNS/firewall issues only apply to direct connections, not HTTPS/443 — pooler uses different routing

---

**Version:** 1.0 | **Updated:** 2026-03-06
