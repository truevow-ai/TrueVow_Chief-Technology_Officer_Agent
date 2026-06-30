# TrueVow Agent OS — Build Recap

**Built:** 2026-05-28 to 2026-05-29 (2 sessions)  
**Status:** 7-layer OS is operational. Production services running. Customer Portal unblocked.  
**Restart from:** Open Obsidian → `DASHBOARD.md` or `Ctrl+O` → "dashboard"

---

## The OS Architecture

```
TrueVow_Knowledge/           ← The brain (63 files, 568 chunks indexed)
    ↕  read/write plain markdown
Any agent (opencode, Claude, Hermes, PI, future)

shared-libraries/             ← 3 internal tools
├── knowledge-sync/           ← Git ingestion pipeline
├── knowledge-indexer/        ← Local vector search (all-MiniLM-L6-v2)
└── code-mapper/              ← Repo structure analysis

sync-and-index.bat            ← One-click refresh
```

---

## Built Infrastructure

### 1. TrueVow_Knowledge Vault (The Memory Layer)

```
TrueVow_Knowledge/
├── .obsidian/              ← Graph settings + Dataview + Kanban plugins
├── ADRs/ (1)               ← Architecture Decisions
├── Incidents/ (1)          ← Bugs & outages
├── Session-Logs/ (5)       ← Every session logged
├── Cross-Service/ (19)     ← Per-service metadata + status
├── Code-Maps/ (16)         ← Repo structure maps + cleanup plans
├── Templates/ (9)          ← ADR, Incident, Session-Log, Agent Harnesses
├── .vector-index.json      ← 568 chunks, semantic search
├── DASHBOARD.md            ← Mission Control — Dataview tables
├── KANBAN-BOARD.md         ← Drag-drop task board
├── REPO-MAP.md             ← All 16 services with status
├── Structure-Audit.md      ← All services ranked by hygiene
├── FIDUCIARY-MANDATE.md    ← Profit-first constitution
├── AGENT-OS-PLAN.md        ← Original 7-layer blueprint
├── AGENT-OS-PLAN-REVISED.md← Revised after video analysis
└── GRAPH-GUIDE.md          ← How to navigate the knowledge graph
```

### 2. 3 Shared Library Tools

| Tool | Package | Command | What it does |
|------|---------|---------|-------------|
| **knowledge-sync** | `@truevow/knowledge-sync` | `npm run sync` | Pulls git logs from 13 repos → writes to vault |
| **knowledge-indexer** | `@truevow/knowledge-indexer` | `npm run index` | Chunks/embeds all .md → local vector store |
| **knowledge-indexer** | `@truevow/knowledge-indexer` | `npm run query -- "ask"` | Semantic search across all knowledge |
| **code-mapper** | `@truevow/code-mapper` | `npm run map` | Walks any repo → finds issues → writes map |

All use local models (no API cost, no subscriptions).

### 3. Agent Harness Templates (Framework-Agnostic)

| Template | Use |
|----------|-----|
| `Agent-Harness-Service.md` | For any agent working on a specific service |
| `Agent-Harness-Feedback.md` | For the feedback/review agent |
| `Agent-Harness-Orchestrator.md` | My own constitution |

All plain markdown. Paste into any agent framework.

---

## Services Fixed

### Running Services (Ports Confirmed)

| Service | Port | Status | DB | Fix Applied |
|---------|------|--------|----|-------------|
| Platform Analytics | 3071 | ✅ Healthy | Pooler URL in `.env.local` | `DATABASE_URL` → pooler |
| Internal Ops | 3006 | ✅ Healthy | REST API (no Postgres) | `SKIP_REGISTRY=true` |
| LEVERAGE | 3036 | ✅ Healthy | Connected via pooler | Was not running. Created `start_leverage.bat`. |

### Start Scripts Created

- `start_analytics.bat` — Platform Analytics (port 3071)
- `start_internal_ops.bat` — Internal Ops (port 3006)
- `start_leverage.bat` — LEVERAGE (port 3036)

### Customer Portal
- **Unblocked.** `UNBLOCK_NOTICE.md` written in portal repo with live endpoints.
- Agent reads it → resumes Phase 2-4 development.

---

## Key Discoveries

### DNS Pattern
4 of 5 Supabase project subdomains (`db.*.supabase.co`) don't resolve. Pooler domains (`aws-*.pooler.supabase.com`) always work.

| Domain | Resolves? |
|--------|-----------|
| `db.yhxtjqczyvjceooyjskc.supabase.co` | ✅ (Internal Ops) |
| `db.nxvbqxzyafujymuxuccl.supabase.co` | ❌ (Platform Analytics) |
| `db.cnbzuiuyppzrygxllgxj.supabase.co` | ❌ (LEVERAGE) |
| `db.flhnyyreaxkmwmexchla.supabase.co` | ❌ (Tenant App) |
| `db.jahhqcypxjkxwrfzpyxd.supabase.co` | ❌ (SaaS Admin) |
| `aws-1-us-east-1.pooler.supabase.com` | ✅ (All poolers) |

**Fix:** Use pooler URLs everywhere. Direct connection DNS is Supabase-side issue.

### Code Hygiene (Structure Audit)

| Service | Files | Issues | Priority |
|---------|-------|--------|----------|
| Financial Management | 5,378 | 557 | 🔴 Worst |
| SaaS Administration | 2,204 | 471 | 🔴 |
| Tenant Application | 2,964 | 234 | 🔴 |
| Sales Ops | 1,241 | 186 | 🔴 |
| Internal Ops | 18,955 | 41 | ⚠️ Anomaly |
| SETTLE | 415 | 15 | 🟢 Clean |
| VERIFY | 43 | 1 | 🟢 Clean |

---

## How To Restart

### 1. Open Obsidian
Launch Obsidian → `TrueVow_Knowledge` vault

### 2. Check the Dashboard
`Ctrl+O` → type `dashboard` → enter
See all services, incidents, sessions in live tables.

### 3. Update the Vault
Double-click `sync-and-index.bat` (in `C:\Users\yasha\OneDrive\Documents\TrueVow\Cursor\`)

### 4. Start a Service (if needed)
Double-click the `start_*.bat` in the service's directory.

### 5. Query Anything
```bash
cd shared-libraries/knowledge-indexer
npm run query -- "your question"
```

---

## What's Blocked / Waiting

| Task | Status |
|------|--------|
| Tenant App cleanup | Awaiting tenant agent's audit response |
| Financial Management cleanup | Pending |
| SaaS Admin cleanup | Pending |
| Internal Ops 18K file anomaly | Needs recheck (nested `app/(auth)/...` folders) |

---

## Orchestrator Agent Role

- **Route tasks** to service agents using Agent Harness templates
- **Fiduciary duty** — challenge unprofitable decisions, keep it simple
- **Feedback loop** — every session writes to vault, reindexes, compounds
- **Agent-agnostic** — any framework can read/write the vault
