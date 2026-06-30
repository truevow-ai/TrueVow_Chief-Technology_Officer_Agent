# Operational State

**Last updated:** 2026-06-18
**Orchestrator:** Odysseus

---

## Vault stats
| Metric | Value |
|---|---|
| Skills | 22 (merged into single SKILLS.md) |
| Session logs | 16+ |
| Active services | 12 |

---

## Pipeline — Sales Ops

| Stage | Count | Status |
|-------|-------|--------|
| won (campaign-ready) | 1,504 | Standard leads, icebreakers done |
| qualified | ~291 | Need icebreakers |
| new | ~372 | Need enrichment |
| lost | | Score < 30 |

## Community Affinity Layer
- `special_cohort_leads` table: 632 leads (sub-agent implementation, authoritative)
- Ownership: GTM engineer
- Tier: confirmed_match / probable_match / potential_match

## Active Services
| Service | Port | Owner |
|---------|------|-------|
| SaaS Admin | 3001 | Ghous (ISB) |
| Tenant App | 3021 | Ghaus (FSD) - Fly.io |
| Customer Portal | 3031 | Yasha |
| SETTLE | 3041 | Yasha |
| Sales Ops | 3056 | Sania - Fly.io |
| CSM CORE | 3061 | Ghous (ISB) |
| First Line Support | 3066 | Ghous (ISB) |
| Billing | 3016 | Ghaus (FSD) |
| Financial Mgmt | 3011 | Yasha |
| LEVERAGE | 3036 | Yasha |
| VERIFY | 8004 | Yasha |
| Platform Analytics | 3071 | Yasha |
| Internal Ops | 3006 | Yasha |

## Key Learnings (Today)
1. Sub-agent output trumps orchestrator's — adopt theirs, discard mine
2. Pipeline stages must run with real gates, never SQL batch bypass
3. Skills system must be updated daily with new learnings
4. Single SKILLS.md file over individual files
5. Check sub-agent work before building anything new

## Active Sub-Agents
| Agent | Service | Last Activity |
|-------|---------|---------------|
| Sales Ops Lead Factory | Sales Ops | Built special_cohort_leads, community_tag |
