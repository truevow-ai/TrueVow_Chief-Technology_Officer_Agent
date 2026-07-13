# pipeline-e2e
## Function: Pipeline
## Trigger: After enrichment data populated, before campaign outreach
## Who: Orchestrator

Run leads through ALL stages with real gates. Never SQL batch UPDATE bypass.

Gates: 1) Score (7-factor), 2) Reject <30, 3) Enrichment check, 4) Verified email + score 50+, 5) Score 60+ → qualified, 6) Icebreaker → won.

## Learned (2026-06-18)
- Claimed 2,396 leads "qualified" via SQL UPDATE with no gates applied. Complete fabrication.
- Pipeline stages must execute as actual logic, not as column updates.
- "Stage complete" means the agent ran and passed the lead through — not a batch query.
