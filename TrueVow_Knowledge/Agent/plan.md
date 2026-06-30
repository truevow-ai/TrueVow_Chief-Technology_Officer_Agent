# Orchestrator Plan — Next Steps

## Blocked (External Dependency)
| Task | Blocker | Owner |
|------|---------|-------|
| Deploy pipeline on Fly.io | Sub-agent needs to add DEEPSEEK_API_KEY secret + `fly deploy` | Sales Ops sub-agent |
| Email verification | Bouncer credits (credit card unblock) | Yasha |
| Trigger pipeline run | Sub-agent runs via Fly.io endpoint | Sales Ops sub-agent |

## Ready Now
| Task | Effort | Priority |
|------|--------|----------|
| Monitor sub-agent activity via live log | Ongoing | P0 |
| Create campaign execution plan for 1,512 won leads | 30 min | P0 |
| Document GTM engineer handoff for special_cohort_leads (632 leads) | 30 min | P1 |
| Clean up failed Python scripts in Sales Ops | 15 min | P2 |
| Resume vault reindex (embedding model download) | Background | P2 |
| Seed remaining 7 communities in name_ethnicity_lookup | 2 hr | P3 |

## Pipeline State
- 1,504 standard leads at 'won' (campaign-ready)
- 632 in special_cohort_leads (GTM engineer)
- ~797 need outreach angles + icebreakers
- ~372 need enrichment
- 2,941 total
