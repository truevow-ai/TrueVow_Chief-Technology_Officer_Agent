# community-affinity-gate
## Function: Pipeline
## Trigger: After enrichment, before campaign
## Who: Orchestrator

1. Load name ethnicity lookup table
2. Extract last names from firm_name + managing_partner + firm_attorneys
3. Cross-reference against lookup (whole-word match preferred over substring)
4. Weight: firm+attorney both match = 1.0, one match = 0.5
5. Move matched leads to `special_cohort_leads` table
6. Remove from standard pipeline

## Learned (2026-06-18)
- Sub-agent's implementation is authoritative. Adopt theirs, discard mine.
- Whole-word matching (632 leads) more thorough than lookup table alone (561).
- Don't name things that raise eyebrows. "Community Affinity Layer" with "confirmed_match" tiers.
