# How to Read the Graph

Close Obsidian and reopen the vault. The graph will now be color-coded:

| Color | Label | What it is | Click to see |
|-------|-------|------------|-------------|
| 🔴 Red | **ADRs** | Architecture decisions | Why we built things a certain way |
| 🟠 Orange | **Incidents** | Bugs / outages | What broke and how we fixed it |
| 🔵 Blue | **Session-Logs** | Work sessions | What was done, when, by whom |
| 🟢 Green | **Cross-Service** | Service metadata + dependency maps | How services connect |
| 🟣 Purple | **Code-Maps** | Repo structure analysis | Which files are where, hygiene issues |
| ⚪ Gray | **Templates** | Agent harnesses + doc templates | Instructions for agents |
| ⚪ White | **Root files** | Core docs (plans, mandate, repo map) | The big picture |

---

## 3 Ways to Explore

### 1. Local Graph (best for focus)
Click any node → click the 3-dot menu → **"Open local graph"**  
Shows only THAT node and its direct connections. Perfect for understanding one service at a time.

### 2. Filter by type
In the graph panel, type a path query:
- `path:Incidents` → only incidents
- `path:Cross-Service` → only services
- `path:Code-Maps` → only code structure

### 3. Follow the links
Open any document (Ctrl+O) and click the `[[wiki-links]]` inside to jump between related documents.

---

## Start Here

| If you want to... | Open this |
|-------------------|-----------|
| Understand the whole system | [[AGENT-OS-PLAN-REVISED]] |
| See what's running | [[Cross-Service/status-update-2026-05-29]] |
| Check repo health | [[Structure-Audit]] |
| Find all services | [[REPO-MAP]] |
| Know the rules | [[FIDUCIARY-MANDATE]] |
| Assign an agent | [[Templates/README]] |

---

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `Ctrl+O` | Open any file by name |
| `Ctrl+G` | Open graph view |
| `Ctrl+H` | Toggle backlinks |
| `Ctrl+E` | Toggle file explorer |
