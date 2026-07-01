# TrueVow CTO Agent Ecosystem

> **One shared brain for all 4 developers.** Git-tracked memory. Harness-agnostic. Works with any coding agent.

---

## What This Is

This is the **Chief Technology Officer agent** for the TrueVow legal AI SaaS platform. It contains:

| Component | Purpose |
|-----------|---------|
| **Orchestrator** | Auto-routes your task to the right skill + persona |
| **Shared Memory** | `memory.db` — one SQLite database shared by all 4 developers via git |
| **Knowledge Vault** | Obsidian vault with ADRs, incidents, session logs, code maps |
| **24 Lifecycle Skills** | DEFINE → PLAN → BUILD → VERIFY → REVIEW → SHIP (addyosmani/agent-skills) |
| **4 Personas** | code-reviewer, test-engineer, security-auditor, web-performance-auditor |
| **Agent Reach** | 13-platform internet research toolkit |
| **SkillSpector** | NVIDIA security scanner — 68 vulnerability patterns |
| **Service Registry** | config.yaml — all 13 active services with their domain-specific skills |
| **Shared Libraries** | auth-client, RBAC engine, security utils, observability, OSS tools |

---

## Quick Start

### 1. Clone (first time only)

```bash
git clone --recursive https://github.com/<org>/truevow-cto-agent.git Cursor
cd Cursor
```

The `--recursive` flag pulls all 4 sub-repos (agent-skills, agent-reach, skillspector, codebase-memory).

### 2. Set your developer identity

**Windows:**
```
set TRUEVOW_DEV=yasha
```

**Mac / Linux:**
```bash
export TRUEVOW_DEV=yasha
```

Registered identities:

| Variable | Developer | Owns |
|----------|-----------|------|
| `TRUEVOW_DEV=yasha` | Yasha (Founder) | All — orchestrator oversight, SETTLE, LEVERAGE, VERIFY, Platform Analytics, Internal Ops |
| `TRUEVOW_DEV=sania` | Ms. Sania | Sales Ops Service |
| `TRUEVOW_DEV=ghaus-fsd` | Ghulam Ghaus | Tenant Application + Billing |
| `TRUEVOW_DEV=ghous-isb` | Ghulam Ghous | SaaS Administration + Customer Success CORE |

Your name is attached to every memory entry you create. Other developers see who decided what.

### 3. Install dependencies

```bash
pip install pyyaml
```

### 4. Verify everything works

```bash
python TrueVow_Shared_Orchestration/orchestrator.py list
```

You should see 24 lifecycle skills, 4 personas, 2 tool skills, and 13 registered services.

---

## Daily Workflow

Every session follows this exact pattern:

### Start — Pull shared knowledge from all developers

```bash
python TrueVow_Shared_Orchestration/orchestrator.py sync-memory
```

This runs `git pull` on the repo. Memory entries from Sania, Ghaus, and Ghous are now visible to you.

### Before any work — Auto-dispatch

```bash
python TrueVow_Shared_Orchestration/orchestrator.py dispatch "fix the billing invoice rounding bug"
```

The orchestrator maps your intent to the right skill + persona and loads the full SKILL.md. Follow it exactly.

### During work — Remember important decisions

```bash
python TrueVow_Shared_Orchestration/memory.py remember architecture "Billing Rounding Fix" "Changed decimal precision from 2 to 4 places in invoice calculations. Affects AR and GL modules." --importance 9
```

Categories: `architecture`, `pattern`, `decision`, `dependency`, `convention`, `bug`, `context`, `todo`, `relationship`

This auto-stages `memory.db` for git. Your `TRUEVOW_DEV` name is attached.

### End of session — Push your knowledge

```bash
python TrueVow_Shared_Orchestration/orchestrator.py push-memory
```

This commits and pushes `memory.db` to the shared repo. All other developers will see your decisions on their next `sync-memory`.

### Sync to Obsidian (optional)

```bash
python TrueVow_Shared_Orchestration/obsidian-bridge.py
```

Writes all memory entries, skills, personas, and service registry to the `TrueVow_Knowledge/` Obsidian vault.

---

## Full Command Reference

| Command | What it does |
|---------|-------------|
| `orchestrator.py sync-memory` | Pull latest shared memory.db from all developers |
| `orchestrator.py push-memory` | Commit + push your decisions to shared repo |
| `orchestrator.py list` | List all skills, personas, and registered services |
| `orchestrator.py dispatch "<task>"` | Auto-map intent → skill + persona, print SKILL.md |
| `orchestrator.py dashboard` | View all active developers |
| `orchestrator.py doctor` | Full ecosystem diagnostic |
| `orchestrator.py memory-summary` | Memory database stats by category |
| `orchestrator.py sync-obsidian` | Sync everything to Obsidian vault |
| `memory.py remember <cat> "<title>" "<content>"` | Store a memory (auto-stages for git) |
| `memory.py recall "<search terms>"` | Search memories by keyword |
| `memory.py summarize` | Memory database summary |
| `obsidian-bridge.py` | Sync memory + skills + services to Obsidian vault |
| `agent-reach doctor` | Check internet research channel status |
| `skillspector scan <path>` | Security scan a skill directory |

---

## How Shared Memory Works

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   Yasha      │     │   Sania      │     │   Ghaus      │     │   Ghous      │
│ TRUEVOW_DEV= │     │ TRUEVOW_DEV= │     │ TRUEVOW_DEV=  │     │ TRUEVOW_DEV=  │
│   yasha      │     │   sania      │     │  ghaus-fsd   │     │  ghous-isb   │
└──────┬───────┘     └──────┬───────┘     └──────┬───────┘     └──────┬───────┘
       │                    │                    │                    │
       │   sync-memory      │   sync-memory      │   sync-memory      │   sync-memory
       │   (git pull)       │   (git pull)       │   (git pull)       │   (git pull)
       ▼                    ▼                    ▼                    ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│                     memory.db  (git-tracked SQLite)                           │
│                                                                              │
│  52 shared memories: 15 architecture, 21 context, 7 todos, 4 decisions...   │
│  Every entry tagged with source developer. FTS5 full-text search.            │
│  Category-filtered. Importance-ranked (1-10).                                │
└──────────────────────────────────────────────────────────────────────────────┘
       │                    │                    │                    │
       │   remember         │   remember         │   remember         │   remember
       │   (auto-stage)     │   (auto-stage)     │   (auto-stage)     │   (auto-stage)
       │   push-memory      │   push-memory      │   push-memory      │   push-memory
       │   (commit+push)    │   (commit+push)    │   (commit+push)    │   (commit+push)
       ▼                    ▼                    ▼                    ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│                       GitHub: truevow-cto-agent                               │
│                                                                              │
│  git history shows: "memory(sania): Lead pipeline Phase 2 complete"          │
│                      "memory(ghaus-fsd): Fixed billing rounding"              │
│                      "memory(ghous-isb): CSM dashboard deployed"              │
└──────────────────────────────────────────────────────────────────────────────┘
```

Each developer:
1. **Pulls** the latest `memory.db` at session start
2. **Reads** what everyone else decided
3. **Writes** their own decisions (auto-staged for git)
4. **Pushes** at session end

No conflicts — memory entries are `INSERT` operations with UUIDs. Everyone works on their own tasks. The database never conflicts on merge.

---

## The 4 Sub-Repos

These are pinned as git submodules at specific commits. They update independently.

| Sub-Repo | Source | Purpose |
|----------|--------|---------|
| `agent-skills/` | github.com/addyosmani/agent-skills (MIT) | 24 lifecycle skills, 4 personas, 8 CLI commands |
| `agent-reach/` | github.com/Panniantong/Agent-Reach (MIT) | 13-platform internet research (Twitter, Reddit, YouTube, GitHub, etc.) |
| `skillspector/` | github.com/NVIDIA/SkillSpector (Apache 2.0) | Security scanner for agent skills (68 vulnerability patterns) |
| `codebase-memory/` | github.com/yuga-hashimoto/codebase-memory (MIT) | SQLite + FTS5 memory database schema |

To update sub-repos:
```bash
git submodule update --remote
git add TrueVow_Shared_Agent_Tools/
git commit -m "chore: update sub-repos to latest"
```

---

## The 13 Active Services

Registered in `config.yaml` with their domain-specific skills.

| Service | Type | Stack | Skills |
|---------|------|-------|--------|
| Tenant Application (INTAKE) | core-platform | Python FastAPI, Cloudflare Workers | 3 |
| LEVERAGE | rules-engine | Python FastAPI, Next.js | 3 |
| VERIFY | blockchain-verification | Python, FastAPI | 3 |
| SETTLE | settlement-engine | Python, Next.js, Docker | 8 |
| Financial Management | financial-backend | Python FastAPI, Next.js | 13 |
| Tenant Billing | billing | Python, Next.js | 3 |
| Sales Ops | crm | Next.js, TypeScript | 3 |
| SaaS Administration | internal-mdm | Next.js, TypeScript | 3 |
| Customer Portal | customer-portal | Next.js, Playwright, Sentry | 3 |
| Customer Success CORE | customer-success | Next.js, TypeScript | 3 |
| Internal Ops | internal-operations | Python FastAPI, Next.js, ELK | 3 |
| Platform Analytics | analytics | Python, FastAPI | 3 |
| TWIML SoftPhone | voice-agent | Python, Flask, Twilio | 3 |

---

## Dispatch Table (quick reference)

| You say... | Skill loaded | Persona |
|-----------|-------------|---------|
| "review this code" | code-review-and-quality | code-reviewer |
| "write tests" | test-driven-development | test-engineer |
| "security audit" | security-and-hardening | security-auditor |
| "performance fix" | performance-optimization | web-performance-auditor |
| "ship / launch" | shipping-and-launch | all three (fan-out) |
| "new feature / spec" | spec-driven-development | — |
| "plan / breakdown" | planning-and-task-breakdown | — |
| "implement / build" | incremental-implementation | — |
| "bug / debug / fix" | debugging-and-error-recovery | — |
| "simplify / refactor" | code-simplification | — |
| "api / endpoint" | api-and-interface-design | — |
| "ui / frontend" | frontend-ui-engineering | — |
| "search web / research" | agent-reach | — |
| "journal / gl / posting" | gl-agent (FM) | — |
| "invoice / ar / billing" | ar-agent (FM) | — |
| "vendor / ap / benjamin" | ap-agent (FM) | — |

---

## Production Deployment

This repo is the **CTO brain**. When TrueVow is in production:

1. Clone this repo with `--recursive` on any server
2. Set `TRUEVOW_DEV=production`
3. Run `sync-memory` to bootstrap
4. The orchestrator runs as a service, auto-dispatching tasks
5. Memory syncs via git to all developer machines

The CTO agent is no longer tied to Yasha's laptop — it's deployable anywhere.

---

## Fiduciary Mandate

Every decision serves **business profitability**:
- P0: Revenue-blocking bugs
- P1: Customer-requested features  
- P2: Security / compliance
- P3: Architecture improvements
- P4: Polish

Simplicity pays. Every line of code must be maintained forever. Default answer to "should we add another service?" is **no**.
