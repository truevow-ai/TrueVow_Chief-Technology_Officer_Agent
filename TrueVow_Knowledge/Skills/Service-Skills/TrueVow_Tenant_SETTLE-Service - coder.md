---
source: TrueVow_Tenant_SETTLE-Service/.opencode/skills/coder/SKILL.md
service: TrueVow_Tenant_SETTLE-Service
type: settlement-engine
stack: ["python", "nextjs", "postgresql", "alembic", "docker"]
imported: 2026-06-30T22:32:05.040749+00:00
skill_name: coder
---
# Coder Skill — Implementation Patterns & Conventions

**Last Updated:** 2026-06-23
**When to use:** Implementing features, writing code, creating tests.
**Note:** Hard constraints and truth commands are in `settle-rules.md` (always loaded).

---

## Role

Implement tasks specified by the Architect. Write code, tests, and documentation. Run truth commands after every change.

## Code Conventions

**Python Style:**
- Follow existing patterns in `app/` directory
- Use Pydantic v2 for all models
- Use `async/await` for all database operations
- Use `logging.getLogger(__name__)` for logging
- Type hints on all function signatures
- Docstrings on all public functions and classes
- No comments unless explicitly requested

**Database:**
- Use `get_db()` from `app.core.database` for async database access
- All table names use `settle_` prefix
- Soft-delete pattern: `deleted_at`, `deleted_by` columns
- Optimistic locking: `row_version` column
- UUIDs for all primary keys

**API Endpoints:**
- Use FastAPI router pattern in `app/api/v1/endpoints/`
- Register routers in `app/api/v1/router.py`
- Use dependency injection for auth (`require_admin`, `require_any_auth`)
- Return Pydantic models as response types
- Use `HTTPException` for error responses

**Testing:**
- Use pytest with pytest-asyncio
- Test files in `tests/` directory
- Mock `get_db()` for unit tests
- Follow existing test patterns in `tests/test_estimator.py`

## Implementation Workflow

**Step 1: Receive Plan** — Read the Architect's plan, understand objective and compliance requirements.

**Step 2: Context Gathering** — Read ONLY files you will modify (max 10). Use grep first.

**Step 3: Implement** — Write code following conventions. Write tests alongside code.

**Step 4: Verify** — Run truth commands. Fix first failure only, re-run, repeat.

**Step 5: Document** — Update IMPLEMENTATION_PROGRESS.md, create checkpoint, update WORKING_CACHE.md.

## Common Code Patterns

**New Service:**
```python
"""
Service Name -- Brief description.
"""
import logging
from typing import List, Optional
from pydantic import BaseModel, Field

from app.core.database import get_db

logger = logging.getLogger(__name__)

class ServiceResponse(BaseModel):
    """Response model."""
    field: str = Field(..., description="Description")

async def service_function(param: str) -> ServiceResponse:
    """Function description."""
    db = await get_db()
    return ServiceResponse(field="value")
```

**New API Endpoint:**
```python
"""
Endpoint Name -- Brief description.
"""
import logging
from fastapi import APIRouter, Depends, HTTPException

from app.core.auth import require_any_auth
from app.services import service_module

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/prefix", tags=["tag"])

@router.get("/endpoint", response_model=ResponseModel)
async def get_endpoint(
    param: str = Query(None),
    auth=Depends(require_any_auth),
):
    """Endpoint description."""
    try:
        result = await service_module.function(param)
        return result
    except Exception as e:
        logger.error(f"Error: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))
```

**New Test:**
```python
"""
Tests for Feature Name.
"""
import pytest
from unittest.mock import AsyncMock, MagicMock, patch

from app.services import service_module

class TestFeatureName:
    @pytest.mark.asyncio
    async def test_happy_path(self):
        with patch("app.services.service_module.get_db") as mock_get_db:
            mock_get_db.return_value = MagicMock()
            result = await service_module.function("param")
            assert result is not None
```

## Anti-Patterns

- **Never use `supabase` directly** — use `get_db()` from `app.core.database`
- **Never mix sync and async** database calls
- **Never use `print()`** — use `logging.getLogger(__name__)`
- **Never hardcode credentials** — use `app.core.config.settings`
- **Never skip tests** — every new feature needs tests
- **Never claim DONE without truth commands** — status stays UNVERIFIED
- **Never fix multiple failures at once** — fix first failure, re-run, repeat
- **Never delete files without asking** — follow restructure safety protocol
