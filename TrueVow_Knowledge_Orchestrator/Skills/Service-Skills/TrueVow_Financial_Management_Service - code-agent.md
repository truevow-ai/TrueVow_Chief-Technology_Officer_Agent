---
source: TrueVow_Financial_Management_Service/.opencode/skills/code-agent/SKILL.md
service: TrueVow_Financial_Management_Service
type: financial-backend
stack: ["python-fastapi", "nextjs", "postgresql", "alembic"]
imported: 2026-06-30T22:32:04.115578+00:00
skill_name: code-agent
---
---
name: code-agent
description: Code modification specialist for TrueVow Financial Management. Writes new features, fixes bugs, adds migrations, and updates frontend components following established repo patterns. Always runs search-agent first to confirm targets before editing.
---

# Code Agent

## What It Does (Simple)
**Objective:** Write or modify code that is correct on the first attempt by following proven repo patterns.

**Manual Problem It Solves:** AI agents that modify code without knowing the established patterns create inconsistencies, break tests, and introduce security gaps.

**Business Value:** Consistent code quality across all 9 financial modules. Fewer review cycles. Fewer production bugs.

---

## Tasks & Objectives

| Task | Objective | Expected Result |
|------|-----------|-----------------|
| `add_endpoint` | Add new FastAPI route | Route + schema + service method |
| `add_model` | Add SQLAlchemy model | Model + migration |
| `add_migration` | Create Alembic migration | Versioned migration file |
| `fix_bug` | Fix first-failure only | Passing truth command |
| `add_component` | Add Next.js component | Typed component + hook |
| `add_vendor` | Register new AP vendor | Vendor master entry |

---

## Backend Patterns

### Module Structure (Actual — Directory Based)
```
{module}/
├── api/
│   └── routes/
│       └── {resource}_routes.py    # FastAPI router
├── models/
│   └── {resource}_model.py     # SQLAlchemy model
├── repositories/
│   └── {resource}_repository.py # DB queries
├── schemas/
│   └── {resource}_schemas.py   # Pydantic schemas
├── services/
│   └── {resource}_service.py   # Business logic
└── integrations/               # External adapters (if applicable)
    ├── {service}_adapter.py        # Abstract interface (ABC)
    └── http_{service}_adapter.py   # HTTP implementation
```

> CRITICAL: Do NOT create flat files like `models.py`. Always use the directory structure above.

### Migration Pattern (Alembic)
```python
# Always include legal_entity_id + RLS policy
op.create_table(
    "new_table",
    sa.Column("id", sa.UUID(), primary_key=True),
    sa.Column("legal_entity_id", sa.UUID(), nullable=False),
    ...
)
op.execute("ALTER TABLE new_table ENABLE ROW LEVEL SECURITY")
op.execute("""
    CREATE POLICY new_table_tenant_isolation ON new_table
    USING (legal_entity_id::text = current_setting('app.current_tenant', true))
""")
```

### Endpoint Pattern (FastAPI)
```python
# api/routes/{resource}_routes.py
@router.post("/{entity_id}/resource", response_model=ResourceOut)
async def create_resource(
    entity_id: uuid.UUID,
    payload: ResourceIn,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user),
):
    return await resource_service.create(db, entity_id, payload, current_user)
```

### Repository Pattern
```python
# repositories/{resource}_repository.py
async def create(db: AsyncSession, entity_id: uuid.UUID, data: dict):
    obj = ResourceModel(legal_entity_id=entity_id, **data)
    db.add(obj)
    await db.flush()
    return obj
```

### Integration Adapter Pattern (External Services)
```python
# integrations/{service}_adapter.py  — ABC / interface
from abc import ABC, abstractmethod

class BillingAdapter(ABC):
    @abstractmethod
    async def get_tenant_pricing(self, tenant_id: str) -> dict: ...
    
    @abstractmethod
    async def get_tenant_addons(self, tenant_id: str) -> list: ...

# integrations/http_{service}_adapter.py  — real implementation
class HTTPBillingAdapter(BillingAdapter):
    async def get_tenant_pricing(self, tenant_id: str) -> dict:
        response = await self._client.get(f"{self._base_url}/tenants/{tenant_id}/pricing")
        return response.json()

# tests: use MockBillingAdapter — never use HTTP adapter in tests
```
```

---

## Frontend Patterns

### Hook Pattern
```typescript
// hooks/useResource.ts
export function useResource(entityId: string) {
  const [data, setData] = useState<Resource[]>([]);
  const [loading, setLoading] = useState(true);
  // ...
}
```

### Component Pattern
```typescript
// components/resource/ResourceList.tsx
export default function ResourceList({ entityId }: { entityId: string }) {
  const { data, loading } = useResource(entityId);
  // ...
}
```

---

## Safety Rules

1. **Search first** — never modify without confirming target with search-agent
2. **One file at a time** — sequential edits, never parallel
3. **First failure only** — fix one error per truth command run
4. **No hide-failures** — no `ignoreBuildErrors`, no skipped tests
5. **RLS on every table** — every new table must have `legal_entity_id` + RLS policy
6. **No bulk deletes** — always ask before delete operations

---

## Truth Command Sequence

After any backend change:
```bash
alembic upgrade head
python -m pytest tests/ -v
```

After any frontend change:
```bash
pnpm lint
pnpm build
```

---

## Escalation Protocol

### When to Escalate to Orchestrator
| Condition | Action | Priority |
|-----------|--------|----------|
| Test failure after 2 fix attempts | Escalate with full error | High |
| Migration conflict | Escalate — schema decision needed | High |
| Breaking change to shared module | Escalate — cross-module impact | High |
| New vendor type for Benjamin | Route to benjamin-agent | Medium |

---

## Learned Patterns

### Accrual Entry for Usage-Based Vendors (Learned 2026-03-06)
**Context:** Benjamin INTAKE vendors (Twilio, Deepgram, ElevenLabs) bill in arrears
**Implementation:** Create monthly accrual journal entries estimating usage; reverse on invoice receipt
**Files:** `app/modules/general_ledger/`, `app/modules/ap/`
**Gotchas:** Do not post actuals until invoice received — accruals only

---

**Version:** 1.0 | **Updated:** 2026-03-06
