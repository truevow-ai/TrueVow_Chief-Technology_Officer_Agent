# Cross-Service Status Update — 2026-05-29

## Platform Analytics — ✅ AVAILABLE
- **Port:** 3071
- **Health:** `{"status":"healthy","service":"saas_admin","version":"0.1.0"}`
- **DB:** Degraded (DNS failure — see [[Incident-001]]). Service runs without DB.
- **Patches:** Config `extra="allow"`, DB init `logger.warning` instead of `raise`

## Internal Ops — ✅ AVAILABLE
- **Port:** 3006
- **Health:** `{"status":"healthy","service":"internal-ops-service","version":"2.0.0","registry":"active"}`
- **DB:** Degraded (REST health check fails, port 443). Service runs without DB.
- **Patches:** `SKIP_REGISTRY=true` env var + `import os` guard
- **ADR:** [[ADR-001]]

## Customer Portal — UNBLOCKED
The two services Portal was waiting for are now running. Portal Phase 2-4 was blocked ~8 days ago. Both dependencies are now healthy and serving.

**Recommended next step for Portal agent:** Resume UI work against live API endpoints at `http://localhost:3071` (Analytics) and `http://localhost:3006` (Internal Ops).

---

*Logged by: Orchestrator Agent, 2026-05-29*
