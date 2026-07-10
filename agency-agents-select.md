# agency-agents — Selective Adoption for TrueVow Engineering

Location: cloned once (reference library). Do NOT install all 232 agents.
Selectively pull 8 agents into the repos that need them as SKILL.md files
or load them into Multica agents per the multica/README.md assignment table.

## Top 7–8 agents for TrueVow's 13 repos

| # | Agent | File | Where it lives | Why it maps to TrueVow |
|---|---|---|---|---|
| 1 | **Backend Architect** | `engineering/engineering-backend-architect.md` | TRACE, INTAKE, Billing, SETTLE (4 repos) | Every FastAPI service needs API design, schema review, scalability |
| 2 | **Code Reviewer** | `engineering/engineering-code-reviewer.md` | ALL repos (13) | Code review before every PR — directly maps to Part 6 of coding-instructions |
| 3 | **Security Auditor** | `security/security-architect.md` | TRACE, Billing, SaaS Admin (3 repos) | PHI/PCI/HIPAA-aware security review — the four-eyes rule |
| 4 | **Database Optimizer** | `engineering/engineering-database-optimizer.md` | TRACE, SETTLE, Billing (3 repos) | Every service has Supabase Postgres — query tuning, index strategy, migration review |
| 5 | **AI Engineer** | `engineering/engineering-ai-engineer.md` | INTAKE, Sales Ops (2 repos) | LLM pipeline design for voice bridges + enrichment |
| 6 | **Voice AI Integration Engineer** | `engineering/engineering-voice-ai-integration-engineer.md` | INTAKE (1 repo) | STT/TTS/transcription/diarization — the core of INTAKE |
| 7 | **Frontend Developer** | `engineering/engineering-frontend-developer.md` | Customer Portal, SaaS Admin (2 repos) | Next.js attorney dashboards + admin UI |
| 8 | **Payments & Billing Engineer** | `engineering/engineering-payments-billing-engineer.md` | Billing (1 repo) | Idempotent payments, Stripe/TELR, PCI compliance |

## How to install per-repo

```bash
git clone https://github.com/msitarzewski/agency-agents.git /tmp/agency-agents

# Per repo (example: TRACE gets Backend Architect + Code Reviewer + Security Auditor)
cp /tmp/agency-agents/engineering/engineering-backend-architect.md \
   /tmp/agency-agents/engineering/engineering-code-reviewer.md \
   /tmp/agency-agents/security/security-architect.md \
   TrueVow_Tenant_TRACE_Service/.opencode/skills/

# Repeat per the table above for each repo.
```

**Do NOT install all agents — only the ones in the table.** The other 220+ are noise for a PI-law platform. Prefer quality over quantity.
