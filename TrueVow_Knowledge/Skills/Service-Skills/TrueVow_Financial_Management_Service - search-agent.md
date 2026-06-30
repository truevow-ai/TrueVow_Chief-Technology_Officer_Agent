---
source: TrueVow_Financial_Management_Service/.opencode/skills/search-agent/SKILL.md
service: TrueVow_Financial_Management_Service
type: financial-backend
stack: ["python-fastapi", "nextjs", "postgresql", "alembic"]
imported: 2026-06-30T22:32:04.049437+00:00
skill_name: search-agent
---
---
name: search-agent
description: Code search specialist for TrueVow Financial Management. Finds code by meaning or exact text, traces dependencies across modules, locates patterns, and identifies relevant files before any modification begins. Use before any code-agent task.
---

# Search Agent

## What It Does (Simple)
**Objective:** Find exactly the right file or code before touching anything.

**Manual Problem It Solves:** Without targeted search, agents open wrong files, miss dependencies, and break things they didn't know existed.

**Business Value:** Zero wasted edits. Every code-agent task starts with verified targets.

---

## Tasks & Objectives

| Task | Objective | Expected Result |
|------|-----------|-----------------|
| `find_module` | Locate module entry point | Exact file path |
| `find_pattern` | Find how pattern is implemented | Code snippet + file |
| `trace_dependency` | Follow import/usage chain | Dependency map |
| `find_endpoint` | Locate specific API route | Router file + handler |
| `find_migration` | Find schema for a table | Migration file |
| `find_model` | Locate SQLAlchemy model | Model class + file |

---

## Search Strategy (Priority Order)

1. `search_codebase` — semantic search (use first for "how does X work?")
2. `search_symbol` — class/method/function by name (use when you know the symbol)
3. `grep_code` — regex pattern search (use for exact strings, import paths)
4. `search_file` — find file by name glob (use when you know partial filename)
5. `list_dir` — explore structure (use only when above methods insufficient)
6. `read_file` — read full file (LAST resort, only after target confirmed)

---

## Known File Locations

### Backend Entry Points
| Component | Path |
|-----------|------|
| App entry | `app/main.py` |
| Auth | `app/auth/` |
| Core config | `app/core/` |
| GL module | `app/modules/general_ledger/` |
| AR module | `app/modules/ar/` |
| AP module | `app/modules/ap/` |
| Payroll | `app/modules/payroll/` |
| Treasury | `app/modules/treasury/` |
| Intercompany | `app/modules/intercompany/` |
| Reporting | `app/modules/reporting/` |
| Affiliates | `app/modules/affiliates/` |

### Frontend Entry Points
| Component | Path |
|-----------|------|
| App router | `frontend/app/` |
| Components | `frontend/components/` |
| Hooks | `frontend/hooks/` |
| API client | `frontend/lib/` |
| Types | `frontend/types/` |

### Database
| Component | Path |
|-----------|------|
| Migrations | `infra/database/` |
| Seeds | `scripts/` |

### Tests
| Component | Path |
|-----------|------|
| Backend tests | `tests/` |
| Frontend tests | `frontend/__tests__/` |

---

## Module File Patterns

Each backend module uses **directories**, not flat files:
```
{module}/
├── api/
│   └── routes/           # Individual route files
├── models/               # ORM model files
├── repositories/         # DB query layer files
├── schemas/              # Pydantic schema files
├── services/             # Business logic files
└── integrations/         # External service adapters (if applicable)
    ├── {service}_adapter.py        # Abstract interface (ABC)
    └── http_{service}_adapter.py   # HTTP implementation
```

> CRITICAL: Do NOT assume `models.py`, `service.py` — always check for the directory first.

---

## Escalation Protocol

### When to Escalate to Orchestrator
| Condition | Action | Priority |
|-----------|--------|----------|
| Symbol not found after 3 search methods | Escalate — may be generated or external | Medium |
| File structure unexpected | Escalate — possible refactor drift | High |
| Circular dependency found | Escalate — architectural concern | High |

---

## Learned Patterns

### Module Structure Is Directory-Based, Not Flat Files (Learned 2026-03-06)
**Context:** All production modules use subdirectories, not single flat files
**Implementation:** Always search for `models/`, `services/`, `repositories/` directories — not `models.py`
**Files:** `app/modules/{any}/`
**Gotchas:** `search_symbol` for a model class resolves to a file inside `models/` subdirectory

### AR Module Has Billing Integration Layer (Learned 2026-03-06)
**Context:** AR module integrates with external Billing Service for pricing, feature access, and Founding Intelligence
**Implementation:** `app/modules/ar/integrations/billing_adapter.py` (ABC) + `http_billing_adapter.py` (real)
**Files:** `app/modules/ar/integrations/`, `app/modules/ar/services/pricing_service.py`
**Gotchas:** Pricing logic is in `pricing_service.py` under `services/` — not in `ar_sync_service.py`

---

**Version:** 1.0 | **Updated:** 2026-03-06
