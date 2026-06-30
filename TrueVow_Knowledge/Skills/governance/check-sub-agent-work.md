# check-sub-agent-work
## Function: Governance
## Trigger: BEFORE starting any new feature or fix
## Who: Orchestrator

1. Check git log for related sub-agent commits in last 48 hours
2. Check live log for sub-agent activity on same service
3. If sub-agent has work → integrate with theirs, never compete
4. If sub-agent data contradicts mine → their data wins, discard mine

## Learned (2026-06-18)
- Built competing cohort table while sub-agent built better one. Cost: hours of wasted work + confusing 'discovery' stage artifacts.
- Sub-agent's whole-word matching (632) found 71 more leads than my lookup table (561).
- This skill is #1 priority. Run it before any new code.
