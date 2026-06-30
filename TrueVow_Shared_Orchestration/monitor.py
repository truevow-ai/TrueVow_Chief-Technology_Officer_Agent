#!/usr/bin/env python3
"""
Real-Time Monitor - Health checks and status dashboard for the entire agent ecosystem.

Checks:
1. Codebase Memory DB health
2. Agent Skills validation
3. Agent Reach channel status
4. SkillSpector baseline status
5. Obsidian vault integrity

Run: python TrueVow_Shared_Orchestration/monitor.py [--watch] [--json]
"""

import subprocess
import sqlite3
import json
import sys
import time
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent.parent


def check_memory_db():
    """Verify the SQLite memory database is healthy (Python client, no MCP)."""
    db_path = ROOT / "TrueVow_Shared_Codebase_Memory" / "memory.db"
    if not db_path.exists():
        return {"status": "EMPTY", "message": "No memory database yet - created on first remember()", "entries": 0}

    try:
        import sqlite3
        conn = sqlite3.connect(str(db_path))
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM memories")
        count = cursor.fetchone()[0]
        cursor.execute("SELECT category, COUNT(*) FROM memories GROUP BY category ORDER BY COUNT(*) DESC")
        categories = dict(cursor.fetchall())
        conn.close()
        return {"status": "OK", "entries": count, "categories": categories}
    except Exception as e:
        return {"status": "CORRUPT", "message": str(e), "entries": 0}


def check_skills_validation():
    """Check that SKILL.md files exist and are valid."""
    skills_dir = ROOT / "TrueVow_Shared_Agent_Tools" / "agent-skills" / "skills"
    if not skills_dir.exists():
        return {"status": "MISSING", "message": "Skills directory not found"}

    skill_count = 0
    missing = []
    for d in sorted(skills_dir.iterdir()):
        if d.is_dir():
            if (d / "SKILL.md").exists():
                skill_count += 1
            else:
                missing.append(d.name)

    return {
        "status": "OK" if skill_count > 0 else "MISSING",
        "total": skill_count,
        "missing_skills": missing
    }


def check_agent_reach():
    """Check Agent Reach availability (fast - checks file existence only)."""
    exe = Path.home() / "AppData" / "Roaming" / "Python" / "Python313" / "Scripts" / "agent-reach.exe"
    if exe.exists():
        return {"status": "OK", "installed": True}
    return {"status": "NOT_INSTALLED", "message": "agent-reach CLI not found"}


def check_skillspector():
    """Check SkillSpector availability (fast - checks file existence only)."""
    baseline = ROOT / ".skillspector-baseline.yaml"
    has_baseline = baseline.exists()
    exe = Path.home() / "AppData" / "Roaming" / "Python" / "Python313" / "Scripts" / "skillspector.exe"
    installed = exe.exists()

    if installed:
        return {"status": "READY", "version": "installed", "baseline": has_baseline}
    else:
        return {"status": "NOT_INSTALLED", "message": "skillspector not installed"}


def check_obsidian_vault():
    """Check Obsidian vault integrity."""
    vault = ROOT / "TrueVow_Knowledge"
    if not vault.exists():
        return {"status": "MISSING", "message": "Vault directory not found"}

    obsidian_cfg = vault / ".obsidian"
    has_obsidian = obsidian_cfg.exists()

    expected_dirs = ["Skills", "Agent", "Decisions", "Code-Maps", "Session-Logs", "Incidents", "Projects", "Templates"]
    present = [d for d in expected_dirs if (vault / d).is_dir()]
    missing = [d for d in expected_dirs if not (vault / d).is_dir()]

    return {
        "status": "OK" if has_obsidian else "NO_CONFIG",
        "path": str(vault),
        "has_obsidian_config": has_obsidian,
        "directories_present": present,
        "directories_missing": missing
    }


def run_all_checks():
    """Run all health checks and return results."""
    checks = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "codebase_memory": check_memory_db(),
        "agent_skills": check_skills_validation(),
        "agent_reach": check_agent_reach(),
        "skillspector": check_skillspector(),
        "obsidian_vault": check_obsidian_vault(),
    }

    all_ok = all(
        v.get("status") in ("OK", "READY", "EMPTY", "NO_CONFIG")
        for v in checks.values()
        if isinstance(v, dict)
    )
    checks["overall"] = "HEALTHY" if all_ok else "DEGRADED"
    return checks


def print_summary(checks: dict):
    """Print a color-coded summary to the terminal."""
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    status_colors = {
        "OK": GREEN, "READY": GREEN, "HEALTHY": GREEN,
        "EMPTY": YELLOW, "NO_CONFIG": YELLOW, "DEGRADED": YELLOW,
        "FAILED": RED, "CORRUPT": RED, "ERROR": RED, "MISSING": RED, "NOT_INSTALLED": YELLOW,
    }

    print(f"\n{BOLD}=== TrueVow Agent Ecosystem Monitor ==={RESET}")
    print(f"Time: {checks['timestamp']}")
    print(f"Overall: {status_colors.get(checks['overall'], RED)}{checks['overall']}{RESET}\n")

    for name, result in checks.items():
        if name in ("timestamp", "overall"):
            continue
        status = result.get("status", "UNKNOWN")
        color = status_colors.get(status, RED)
        label = name.replace("_", " ").title()

        if name == "codebase_memory":
            entries = result.get("entries", 0)
            cats = result.get("categories", {})
            print(f"  {color}[{status}]{RESET} {label}: {entries} memories" + (f" across {len(cats)} categories" if cats else ""))
        elif name == "agent_skills":
            total = result.get("total", 0)
            missing_list = result.get("missing_skills", [])
            missing_str = f" (missing: {', '.join(missing_list[:3])})" if missing_list else ""
            print(f"  {color}[{status}]{RESET} {label}: {total} SKILL.md files{missing_str}")
        elif name == "agent_reach":
            print(f"  {color}[{status}]{RESET} {label}: {'Installed' if result.get('installed') else result.get('message', '')}")
        elif name == "skillspector":
            bl = " + baseline" if result.get("baseline") else ""
            print(f"  {color}[{status}]{RESET} {label}: {result.get('version', result.get('message', ''))}{bl}")
        elif name == "obsidian_vault":
            present = len(result.get("directories_present", []))
            missing = len(result.get("directories_missing", []))
            print(f"  {color}[{status}]{RESET} {label}: {present} dirs present" + (f", {missing} missing" if missing else ""))

    print()


def watch_mode(interval: int = 300):
    """Continuously monitor every `interval` seconds."""
    print(f"[monitor] Watch mode: checking every {interval}s. Ctrl+C to stop.")
    try:
        while True:
            checks = run_all_checks()
            print_summary(checks)
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\n[monitor] Stopped.")


if __name__ == "__main__":
    if "--json" in sys.argv:
        checks = run_all_checks()
        print(json.dumps(checks, indent=2, ensure_ascii=False))
    elif "--watch" in sys.argv:
        watch_mode()
    else:
        checks = run_all_checks()
        print_summary(checks)
