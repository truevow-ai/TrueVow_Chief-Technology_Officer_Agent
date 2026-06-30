#!/usr/bin/env python3
"""
Obsidian Bridge - Syncs codebase-memory entries and agent decisions
into the TrueVow Knowledge Obsidian vault.

Run: python TrueVow_Shared_Orchestration/obsidian-bridge.py [--watch]
"""

import sqlite3
import json
import os
import re
import sys
import time
from pathlib import Path
from datetime import datetime, timezone

VAULT_ROOT = Path(__file__).resolve().parent.parent / "TrueVow_Knowledge"
MEMORY_DB = Path(__file__).resolve().parent.parent / "TrueVow_Shared_Codebase_Memory" / "memory.db"
SKILLS_DIR = Path(__file__).resolve().parent.parent / "TrueVow_Shared_Agent_Tools" / "agent-skills" / "skills"
ROOT = Path(__file__).resolve().parent.parent
CONFIG_YAML = ROOT / "TrueVow_Shared_Orchestration" / "config.yaml"

_ILLEGAL_FILENAME_CHARS = re.compile(r'[<>:"/\\|?*\x00-\x1f]')


def safe_filename(name: str, max_len: int = 80) -> str:
    """Sanitize an arbitrary string into a safe cross-platform filename stem.

    Strips characters illegal in Windows filenames (<>:"/\\|?*) and control
    chars, trims trailing dots/spaces, and caps length. Prevents the sync from
    crashing on titles like 'Context: foo'.
    """
    cleaned = _ILLEGAL_FILENAME_CHARS.sub("-", name or "")
    cleaned = cleaned.strip()[:max_len].strip(" .-")
    return cleaned or "untitled"


def ensure_dirs():
    for d in ["Decisions", "Code-Maps", "Session-Logs", "Skills", "Agent", "Incidents"]:
        (VAULT_ROOT / d).mkdir(parents=True, exist_ok=True)


def sync_memory_to_obsidian():
    """Export codebase-memory entries to Obsidian markdown files."""
    if not MEMORY_DB.exists():
        print(f"[obsidian-bridge] Memory DB not found at {MEMORY_DB} - skipping")
        return {}

    conn = sqlite3.connect(str(MEMORY_DB))
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    stats = {}
    category_map = {
        "decision": ("Decisions", "Decision"),
        "architecture": ("Code-Maps", "Architecture"),
        "pattern": ("Code-Maps", "Pattern"),
        "convention": ("Code-Maps", "Convention"),
        "bug": ("Incidents", "Bug"),
        "context": ("Session-Logs", "Context"),
        "todo": ("Projects", "Todo"),
        "dependency": ("Code-Maps", "Dependency"),
        "relationship": ("Code-Maps", "Relationship"),
    }

    for category, (folder, label) in category_map.items():
        rows = cursor.execute(
            "SELECT * FROM memories WHERE category = ? ORDER BY updated_at DESC",
            (category,)
        ).fetchall()

        if not rows:
            continue

        out_dir = VAULT_ROOT / folder
        out_dir.mkdir(parents=True, exist_ok=True)
        count = 0

        for row in rows:
            filename = f"{label} - {safe_filename(row['title'])}.md"
            filepath = out_dir / filename

            tags = json.loads(row["tags"] or "[]")
            file_paths = json.loads(row["file_paths"] or "[]")

            content = f"""---
category: {category}
title: {json.dumps(row['title'])}
importance: {row['importance']}
tags: {json.dumps(tags)}
file_paths: {json.dumps(file_paths)}
created: {row['created_at']}
updated: {row['updated_at']}
memory_id: {row['id']}
---

# {row['title']}

{row['content']}

---
**Category:** `{category}` | **Importance:** {row['importance']}/10
**Files:** {', '.join(file_paths) if file_paths else 'N/A'}
"""

            filepath.write_text(content, encoding="utf-8")
            count += 1

        stats[category] = count

    conn.close()
    return stats


def sync_skills_to_obsidian():
    """Export agent skills to Obsidian Skills directory."""
    if not SKILLS_DIR.exists():
        print(f"[obsidian-bridge] Skills dir not found at {SKILLS_DIR} - skipping")
        return 0

    out_dir = VAULT_ROOT / "Skills"
    out_dir.mkdir(parents=True, exist_ok=True)
    count = 0

    for skill_dir in sorted(SKILLS_DIR.iterdir()):
        if not skill_dir.is_dir():
            continue
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            continue

        skill_name = skill_dir.name.replace("-", " ").title()
        dest = out_dir / f"{skill_name}.md"

        content = skill_md.read_text(encoding="utf-8", errors="replace")
        frontmatter = f"""---
source: TrueVow_Shared_Agent_Tools/agent-skills/skills/{skill_dir.name}/SKILL.md
imported: {datetime.now(timezone.utc).isoformat()}
skill_name: {skill_dir.name}
---

"""
        dest.write_text(frontmatter + content, encoding="utf-8")
        count += 1

    return count


def sync_agent_personas():
    """Export agent personas to Obsidian Agent directory."""
    agents_dir = Path(__file__).resolve().parent.parent / "TrueVow_Shared_Agent_Tools" / "agent-skills" / "agents"
    if not agents_dir.exists():
        return 0

    out_dir = VAULT_ROOT / "Agent"
    out_dir.mkdir(parents=True, exist_ok=True)
    count = 0

    for agent_file in agents_dir.glob("*.md"):
        dest = out_dir / agent_file.name
        content = agent_file.read_text(encoding="utf-8", errors="replace")
        frontmatter = f"""---
source: TrueVow_Shared_Agent_Tools/agent-skills/agents/{agent_file.name}
imported: {datetime.now(timezone.utc).isoformat()}
---

"""
        dest.write_text(frontmatter + content, encoding="utf-8")
        count += 1

    return count


def sync_service_skills():
    """Export service-specific .opencode/skills to Obsidian."""
    out_dir = VAULT_ROOT / "Skills" / "Service-Skills"
    out_dir.mkdir(parents=True, exist_ok=True)
    total = 0

    try:
        import yaml
    except ImportError:
        return total

    if not CONFIG_YAML.exists():
        return total

    config = yaml.safe_load(CONFIG_YAML.read_text(encoding="utf-8"))
    services = config.get("services", {})

    for svc_name, svc in services.items():
        if svc.get("status") in ("archived", "replaced"):
            continue
        skills_dir_s = svc.get("skills_dir", ".opencode/skills")
        skills_dir = ROOT / svc["path"] / skills_dir_s
        if not skills_dir.exists():
            continue

        for skill in svc.get("skills", []):
            skill_name = skill["name"]
            skill_md = skills_dir / skill_name / "SKILL.md"
            if not skill_md.exists():
                continue

            safe_svc = safe_filename(svc_name, 60)
            dest = out_dir / f"{safe_svc} - {safe_filename(skill_name, 60)}.md"
            content = skill_md.read_text(encoding="utf-8", errors="replace")
            frontmatter = f"""---
source: {svc['path']}/{skills_dir_s}/{skill_name}/SKILL.md
service: {svc_name}
type: {svc.get('type', '')}
stack: {json.dumps(svc.get('stack', []))}
imported: {datetime.now(timezone.utc).isoformat()}
skill_name: {skill_name}
---
"""
            dest.write_text(frontmatter + content, encoding="utf-8")
            total += 1

    return total


def sync_services_registry():
    """Export registered services list to Obsidian."""
    out_dir = VAULT_ROOT / "Agent"
    out_dir.mkdir(parents=True, exist_ok=True)

    try:
        import yaml
    except ImportError:
        return 0

    if not CONFIG_YAML.exists():
        return 0

    config = yaml.safe_load(CONFIG_YAML.read_text(encoding="utf-8"))
    services = config.get("services", {})

    lines = [
        "---",
        f"imported: {datetime.now(timezone.utc).isoformat()}",
        "---",
        "",
        "# Registered Services",
        "",
    ]

    active_services = {k: v for k, v in services.items() if v.get("status") not in ("archived", "replaced")}
    archived_services = {k: v for k, v in services.items() if v.get("status") in ("archived", "replaced")}

    lines.append(f"**{len(active_services)} active** | **{len(archived_services)} archived/replaced**")
    lines.append("")

    lines.append("## Active Services")
    lines.append("")
    lines.append("| Service | Type | Stack | Skills |")
    lines.append("|---------|------|-------|--------|")
    for name, svc in active_services.items():
        skills_n = len(svc.get("skills", []))
        lines.append(f"| {name} | {svc.get('type', '')} | {', '.join(svc.get('stack', []))} | {skills_n} |")
    lines.append("")

    if archived_services:
        lines.append("## Archived / Replaced")
        lines.append("")
        lines.append("| Service | Status | Replaced By |")
        lines.append("|---------|--------|-------------|")
        for name, svc in archived_services.items():
            replaced = svc.get("replaced_by", svc.get("note", "N/A"))
            lines.append(f"| {name} | {svc.get('status', '').upper()} | {replaced} |")
        lines.append("")

    dest = out_dir / "Registered Services.md"
    dest.write_text("\n".join(lines), encoding="utf-8")
    return len(active_services)


def generate_dashboard(stats: dict):
    total_memories = sum(stats.get("memory", {}).values()) if isinstance(stats.get("memory"), dict) else stats.get("memory", 0)
    total_skills = stats.get("skills", 0)
    total_agents = stats.get("agents", 0)
    total_services = stats.get("services", 0)
    total_service_skills = stats.get("service_skills", 0)

    dashboard = f"""# TrueVow Agent Ecosystem Dashboard

> Auto-generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}

## Health

| Component | Status | Details |
|-----------|--------|---------|
| Codebase Memory | {'ONLINE' if total_memories > 0 else 'EMPTY'} | {total_memories} memories stored |
| Lifecycle Skills | ONLINE | {total_skills} skills synced |
| Service Skills | ONLINE | {total_service_skills} skills across {total_services} services |
| Agent Personas | ONLINE | {total_agents} personas available |
| SkillSpector Guardrail | READY | Scan on install: enabled |
| Agent Reach | READY | 13 channels available |
| Obsidian Bridge | ACTIVE | Syncing to `TrueVow_Knowledge/` |
| Registered Services | {'ONLINE' if total_services > 0 else 'EMPTY'} | {total_services} active services |

## Quick Commands

- `python TrueVow_Shared_Orchestration/obsidian-bridge.py` - Sync all data to Obsidian
- `python TrueVow_Shared_Orchestration/monitor.py` - Run health checks
- `python TrueVow_Shared_Orchestration/orchestrator.py skill-scan` - Scan all skills with SkillSpector
- `python TrueVow_Shared_Orchestration/orchestrator.py install --all` - Full ecosystem install

## Memory Categories

| Category | Entries |
|----------|---------|
"""
    if isinstance(stats.get("memory"), dict):
        for cat, count in stats["memory"].items():
            dashboard += f"| {cat} | {count} |\n"
    else:
        dashboard += f"| all | {total_memories} |\n"

    dashboard += f"""
## Installed Skills ({total_skills} lifecycle + {total_service_skills} service-specific)

See [[Skills/]] for full catalog.
See [[Skills/Service-Skills/]] for service-specific skills.

## Agent Personas ({total_agents})

See [[Agent/]] for all personas.

## Registered Services ({total_services} active)

See [[Agent/Registered Services]] for the full registry.

## Recent Sessions

See [[Session-Logs/]] for session history.
"""

    (VAULT_ROOT / "DASHBOARD.md").write_text(dashboard, encoding="utf-8")
    print(f"[obsidian-bridge] Dashboard written to DASHBOARD.md")


def watch_mode(interval: int = 300):
    """Continuously sync every `interval` seconds."""
    print(f"[obsidian-bridge] Watch mode: syncing every {interval}s. Ctrl+C to stop.")
    try:
        while True:
            run_sync()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\n[obsidian-bridge] Stopped.")


def run_sync():
    print(f"[obsidian-bridge] Syncing at {datetime.now().isoformat()}...")
    ensure_dirs()

    memory_stats = sync_memory_to_obsidian()
    skills_count = sync_skills_to_obsidian()
    agents_count = sync_agent_personas()
    service_skills_count = sync_service_skills()
    services_count = sync_services_registry()

    stats = {
        "memory": memory_stats,
        "skills": skills_count,
        "agents": agents_count,
        "service_skills": service_skills_count,
        "services": services_count,
    }
    generate_dashboard(stats)

    total_memories = sum(memory_stats.values())
    print(f"[obsidian-bridge] Done: {total_memories} memories, {skills_count} lifecycle skills, {service_skills_count} service skills, {agents_count} agents, {services_count} services")


if __name__ == "__main__":
    if "--watch" in sys.argv:
        watch_mode()
    else:
        run_sync()
