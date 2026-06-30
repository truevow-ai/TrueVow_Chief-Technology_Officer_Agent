# TrueVow Agent Ecosystem

> **Skills are the new apps.** Five GitHub tools, one orchestrator, infinite leverage.
> Harness-agnostic: works with OpenCode, Cursor, Claude Code, or any agent.
> No MCP servers. Pure file-based skills + CLI tools.

## Architecture

```
TrueVow_Shared_Orchestration/              ← Control plane
├── config.yaml             Master config (all 5 pillars)
├── orchestrator.py         Single entry point
├── monitor.py              Health checks + dashboard
├── memory.py               SQLite memory client (no MCP needed)
├── obsidian-bridge.py      Syncs agent memory → Obsidian vault
└── skill-registry.md       Full catalog (24 skills, 4 personas)

TrueVow_Shared_Agent_Tools/               ← GitHub repos (cloned)
├── agent-skills/           Osmani's 24 skills + 4 personas
├── codebase-memory/        SQLite schema (used directly by memory.py)
├── agent-reach/            Live web eyes (13 platforms)
└── skillspector/           NVIDIA security guardrail (68 patterns)

TrueVow_Shared_Codebase_Memory/           ← SQLite DB
└── memory.db               Agent memories (auto-created)

TrueVow_Knowledge/          ← Obsidian vault (sync target)
├── Skills/                 Synced skill files
├── Agent/                  Persona definitions
├── Decisions/              Architecture decisions
├── Code-Maps/              Patterns, conventions
├── Session-Logs/           Per-session context
└── DASHBOARD.md            Auto-generated dashboard
```

## The Five Pillars

### 1. Osmani Agent Skills
24 production-grade SKILL.md files encoding senior-engineer workflows.
**DEFINE → PLAN → BUILD → VERIFY → REVIEW → SHIP**
- 8 slash commands (Claude Code / Gemini CLI)
- 4 specialist personas (code-reviewer, test-engineer, security-auditor, web-perf-auditor)

### 2. Codebase Memory
SQLite database with FTS5 full-text search. Agents remember architecture decisions,
code patterns, conventions, bugs, and project context across sessions.
- 5 operations: create, query, update, delete, summarize
- 9 categories, importance scoring 1-10
- No MCP server required — Python client in `TrueVow_Shared_Orchestration/memory.py`

### 3. Agent Reach
Live web access across 13 platforms — zero API fees.
- Zero config: Web, YouTube, RSS, Exa Search, GitHub, V2EX
- Optional: Twitter/X, Reddit, XiaoHongShu, Bilibili, LinkedIn, and more

### 4. NVIDIA SkillSpector
Security guardrail: 68 vulnerability patterns across 17 categories.
Scans every skill before installation. Risk scoring 0-100.

### 5. Obsidian Bridge
Syncs agent memory, decisions, and skills into the Obsidian vault.

## Quick Start

```powershell
# Clone repos
git clone https://github.com/addyosmani/agent-skills.git TrueVow_Shared_Agent_Tools/agent-skills
git clone https://github.com/yuga-hashimoto/codebase-memory.git TrueVow_Shared_Agent_Tools/codebase-memory
git clone https://github.com/Panniantong/Agent-Reach.git TrueVow_Shared_Agent_Tools/agent-reach
git clone https://github.com/NVIDIA/SkillSpector.git TrueVow_Shared_Agent_Tools/skillspector

# Verify
python TrueVow_Shared_Orchestration/orchestrator.py doctor

# List available skills
python TrueVow_Shared_Orchestration/orchestrator.py list

# Store a memory
python TrueVow_Shared_Orchestration/memory.py remember architecture "Event-driven" "Services communicate via RabbitMQ" --importance 8

# Search memories
python TrueVow_Shared_Orchestration/memory.py recall "event driven"

# Sync to Obsidian
python TrueVow_Shared_Orchestration/obsidian-bridge.py
```

## Commands

| Command | Purpose |
|---------|---------|
| `python TrueVow_Shared_Orchestration/orchestrator.py doctor` | Full diagnostic |
| `python TrueVow_Shared_Orchestration/orchestrator.py list` | List all skills + personas |
| `python TrueVow_Shared_Orchestration/orchestrator.py skill <name>` | Print a skill's SKILL.md |
| `python TrueVow_Shared_Orchestration/orchestrator.py skill-scan` | Security scan all skills |
| `python TrueVow_Shared_Orchestration/orchestrator.py memory-summary` | Memory stats |
| `python TrueVow_Shared_Orchestration/orchestrator.py sync-obsidian` | Sync to vault |
| `python TrueVow_Shared_Orchestration/orchestrator.py monitor` | Health check |
| `python TrueVow_Shared_Orchestration/memory.py summarize` | Memory DB overview |
| `python TrueVow_Shared_Orchestration/memory.py remember <cat> <title> <content>` | Store memory |
| `python TrueVow_Shared_Orchestration/memory.py recall <query>` | Search memories |
| `python TrueVow_Shared_Orchestration/obsidian-bridge.py --watch` | Live sync to Obsidian |
| `agent-reach doctor` | Web channel health |
| `skillspector scan <path>` | Security scan a skill |

## GitHub Sources

| Tool | Stars | URL |
|------|-------|-----|
| Agent Skills | 66.4k | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) |
| Agent Reach | 39.6k | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) |
| SkillSpector | 10.3k | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) |
| Codebase Memory | - | [yuga-hashimoto/codebase-memory](https://github.com/yuga-hashimoto/codebase-memory) |
