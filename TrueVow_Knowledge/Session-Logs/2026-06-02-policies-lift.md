# Session Log — 2026-06-02 (part 2)

## Focus
Added `policies:` section to `.triage.yaml` and annotated agent harnesses with the Worker/Service/Support taxonomy from the arXiv paper.

## Business Impact
- [x] Risk: Declarative policy rules replace implicit "orchestrator remembers the rules" — fewer silent policy violations possible.
- [x] Learning: Agent type annotations make the multi-agent architecture explicit (2 Support hats, 1 Worker hat, 3 Service utilities).
- [ ] Revenue: No direct revenue impact.
- [ ] Efficiency: Negligible at current scale; pays off if/when we add more agents or services.

## Work Done
- [x] Read 3 sources: Redwerk framework survey, Kore.ai orchestration article, arXiv 2601.13671 (Adimulam et al.)
- [x] Honest evaluation: ~80% of the patterns in those docs already exist in our 7-layer system under different vocabulary
- [x] Identified 2 genuine lifts: (1) policy/planning separation, (2) agent type taxonomy
- [x] Added `policies:` section to `.triage.yaml` (8 categories, 70 lines) — persistence, git, secrets, destructive ops, production, cross-service, audit, agent behavior
- [x] Annotated 3 agent harnesses with type — Orchestrator:Support, Service-Agent:Worker, Feedback-Agent:Support
- [x] Updated roles section in `.triage.yaml` to include type tags
- [x] Force-reindexed vault: 577 → 587 chunks, 64 → 65 files (new file is the Hermes-lift session log)
- [x] User approved via gate → fulfilled

## Decisions Made
- Lifted policy/planning separation from arXiv §V-A — Decision — paper's strongest insight, fills a real gap. Profit impact: neutral.
- Adopted Worker/Service/Support taxonomy — Decision — gives clean vocabulary for future agent additions. Profit impact: neutral.
- Declined QA / Healing / Compliance agent types — Decision — we don't have the volume to justify dedicated agents. Orchestrator + rubric + gate is sufficient at current scale. Revisit if incident volume grows. Profit impact: + (avoid premature infra).
- Declined all framework recommendations (OpenAI Agents SDK, AutoGen, Google ADK, etc.) — Decision — we ARE the framework; adding one would create a dependency for no capability gain. Profit impact: + (avoids vendor lock-in).
- Declined MCP / A2A protocol adoption — Decision — relevant for multi-agent networks, not single-orchestrator-multi-hats. Profit impact: neutral.
- `.triage.yaml` + Templates in `auto_writable_paths` — Decision — pipeline config, not persistent KB. Updates flow through orchestrator proposals, not the gate. Profit impact: neutral.

## Blockers
- None.

## Services Touched
- None. Vault config only.

## Next Steps
- [ ] Next session: do a sample triage end-to-end to verify the policies + 3-verb gate work in practice
- [ ] Optional: add a `policy_violation` field to session log template so we can track if/when policies get challenged
- [ ] Optional: indexer incremental update (skip if `.vector-index.json` mtime > newest .md mtime) — file as ADR if scope grows

## Related
- [[AGENT-OS-PLAN|Agent OS Plan]] — original 7-layer blueprint
- [[AGENT-OS-PLAN-REVISED|Agent OS Plan (Revised)]] — feedback loop moved to Phase 2.5
- [[.triage.yaml]] — now includes `policies:` section
- [[Templates/Agent-Harness-Orchestrator|Orchestrator Harness]] — Support type
- [[Templates/Agent-Harness-Service|Service Harness]] — Worker type
- [[Templates/Agent-Harness-Feedback|Feedback Harness]] — Support type
- Session-Logs/2026-06-02-hermes-lift.md — first part of today's session

## Gate Record
- Proposed: 2026-06-02 (add `policies:` section + agent type annotations)
- Path: config update (auto-writable per `.triage.yaml` → `policies.persistence.auto_writable_paths`)
- Score: N/A (utility config update)
- Target: `.triage.yaml` + 3 Templates/*.md files
- Verdict: APPROVED by user
- Fulfilled: 70 lines added to `.triage.yaml`, 3 harnesses annotated, vault reindexed
