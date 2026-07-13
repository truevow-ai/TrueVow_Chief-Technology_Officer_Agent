---
status: accepted
date: 2026-05-28
---
# ADR-001: Skip Registry Self-Registration on Startup

## Context
Internal Ops Service was calling `registry.register()` inside its own startup handler (`app/main.py`) before the uvicorn server began listening. The registration call hit `http://localhost:3006/api/v1/registry/register` — i.e., itself — which failed because the server wasn't accepting connections yet, creating a startup deadlock.

## Decision
Add a `SKIP_REGISTRY` environment variable check. When set to `true`, the service skips the registration call on startup. This is a temporary safeguard.

## Consequences
- Service starts reliably in dev without a running registry
- Registration must happen manually or via a separate init step until a proper health-dependent startup sequence is built

## Affected Services
- [[Internal Ops Service]] — `app/main.py`: added `import os` + `SKIP_REGISTRY` guard
- [[Platform Analytics Service]] — similar pattern considered but not needed (no self-registration)

## Related
- [[Incident-001|Incident 001]]
