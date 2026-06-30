---
status: mitigated
severity: high
date: 2026-05-28
resolved:
---
# Incident-001: Platform Analytics DB DNS Resolution Failure

## Summary
Platform Analytics Service fails to connect to Supabase PostgreSQL because DNS cannot resolve `db.nxvbqxzyafujymuxuccl.supabase.co`. Service starts but has no database.

## Root Cause
Unknown DNS issue — possibly transient DNS, or the Supabase project was paused/rotated. `getaddrinfo failed` error.

## Timeline
- 2026-05-28 — discovered during service startup verification

## Fix Applied
- Changed DB init from `raise` (hard crash) to `logger.warning` in `app/main.py`
- Added `extra = "allow"` to Pydantic `Settings` class to tolerate unexpected config fields

## Related
- [[Platform Analytics Service]]
- [[Internal Ops Service]] — similar DB issue (Supabase REST API unreachable on port 443)
