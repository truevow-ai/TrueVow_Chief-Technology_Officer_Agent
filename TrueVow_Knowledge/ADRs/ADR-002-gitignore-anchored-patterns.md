# ADR-002: Anchored .gitignore Directory Patterns

**Status:** Accepted  
**Date:** 2026-07-01  
**Deciders:** Yasha (CTO)

## Context

Six service repositories had unanchored `.gitignore` directory patterns (e.g., `lib/` instead of `/lib/`) that silently match at any depth in the repository tree. These patterns were intended to ignore Python virtual environment or build artifact directories, but because they lacked a leading `/`, they also matched legitimate source directories named `lib/`, `env/`, `build/`, `dist/`, `data/`, `var/`, etc. anywhere in the tree.

Three services (Financial Management, Tenant Billing, LEVERAGE) also contained a leaked PowerShell command (`"@ | Out-File -Encoding utf8 .gitignore`) that was inadvertently appended to their `.gitignore` files.

## Decision

All dangerous unanchored patterns in all 6 affected services are replaced with root-anchored equivalents (`/lib/`, `/env/`, `/venv/`, `/build/`, `/dist/`, `/data/`). Leaked PowerShell commands are removed. Duplicate patterns and redundant sections are consolidated.

Additionally, `_check_pii.py` and `test_db_conn.py` / `recover_pyc.py` patterns in Tenant Application and SETTLE are scoped to root-level only (`/_check_pii.py`, `/test_db_conn.py`) since the unanchored forms would hide these filenames anywhere in the tree.

## Consequences

- **Positive:** All legitimate source directories are now visible to git. No source code can be accidentally hidden.
- **Positive:** The `.gitignore` files are cleaner and free of corruption artifacts.
- **Neutral:** Existing venv/build/dist directories at root will still be ignored as intended.
- **Risk:** If a service has a nested `lib/` or `build/` directory that should be ignored, it needs an explicit anchored path like `app/lib/`. This is by design — explicit paths are safer than blanket rules.

## Affected Services

1. `TrueVow_Financial_Management_Service` (P0 — revenue-critical)
2. `TrueVow_Tenant_Application_Service` (P0 — production on Fly.io)
3. `TrueVow-Tenant_Billing-Service` (P0)
4. `TrueVow_Internal_Ops_Service` (P1 — latent, no active leak)
5. `TrueVow_Tenant_SETTLE-Service` (P1 — latent)
6. `TrueVow_Tenant_LEVERAGE_Service` (P1 — latent)
