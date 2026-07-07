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


def check_observability():
    """Check if observability stack is configured and running."""
    docker_compose = ROOT / "shared-libraries" / "observability" / "docker-compose.yml"
    if not docker_compose.exists():
        return {"status": "NO_CONFIG", "message": "No observability docker-compose found"}

    try:
        r = subprocess.run(
            ["docker", "compose", "-f", str(docker_compose), "ps", "--format", "json"],
            capture_output=True, text=True, timeout=15
        )
        if r.returncode == 0 and r.stdout.strip():
            running = 0
            total = 0
            for line in r.stdout.strip().split("\n"):
                try:
                    data = json.loads(line)
                    total += 1
                    if data.get("State") == "running":
                        running += 1
                except json.JSONDecodeError:
                    continue
            if running == total and total > 0:
                return {"status": "RUNNING", "containers": total, "running": running}
            elif running > 0:
                return {"status": "PARTIAL", "containers": total, "running": running}
            else:
                return {"status": "STOPPED", "containers": total, "running": 0}
        else:
            return {"status": "NOT_DEPLOYED", "message": "docker-compose ps returned no containers"}
    except (FileNotFoundError, Exception) as e:
        return {"status": "DOCKER_NOT_AVAILABLE", "message": str(e)[:80]}


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


def check_services_git():
    """Check git state of all registered services (fast — one log + status per repo)."""
    import yaml
    config_path = Path(__file__).parent / "config.yaml"
    if not config_path.exists():
        return {"status": "NO_CONFIG", "message": "config.yaml not found"}

    with open(config_path, encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    services = cfg.get("services", {})
    clean, dirty, missing, errors = 0, 0, 0, 0
    dirty_details = []

    for svc_name, svc in services.items():
        if svc.get("status") in ("archived", "replaced"):
            continue

        svc_path = ROOT / svc["path"]
        if not svc_path.exists():
            missing += 1
            continue

        git_dir = svc_path / ".git"
        has_git = False
        if git_dir.exists():
            has_git = True
        else:
            git_check = subprocess.run(
                ["git", "rev-parse", "--git-dir"],
                cwd=str(svc_path), capture_output=True, text=True, timeout=5
            )
            has_git = git_check.returncode == 0

        if not has_git:
            missing += 1
            continue

        try:
            status_r = subprocess.run(
                ["git", "status", "--porcelain"],
                cwd=str(svc_path), capture_output=True, text=True, timeout=10, encoding="utf-8", errors="replace"
            )
            if status_r.stdout.strip():
                dirty += 1
                dirty_details.append({
                    "service": svc_name,
                    "type": svc.get("type", ""),
                    "files": min(status_r.stdout.strip().count("\n") + 1, 50),
                })
            else:
                clean += 1
        except Exception:
            errors += 1

    return {
        "status": "CLEAN" if (dirty == 0 and errors == 0) else "DEGRADED",
        "clean": clean,
        "dirty": dirty,
        "missing": missing,
        "errors": errors,
        "dirty_details": dirty_details,
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
        "services_git": check_services_git(),
        "observability": check_observability(),
    }

    all_ok = all(
        v.get("status") in ("OK", "READY", "EMPTY", "NO_CONFIG", "CLEAN", "RUNNING", "NOT_DEPLOYED", "DOCKER_NOT_AVAILABLE")
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
        elif name == "services_git":
            clean = result.get("clean", 0)
            dirty = result.get("dirty", 0)
            missing = result.get("missing", 0)
            errors = result.get("errors", 0)
            parts = [f"{clean} clean"]
            if dirty: parts.append(f"{YELLOW}{dirty} dirty{RESET}")
            if missing: parts.append(f"{RED}{missing} missing{RESET}")
            if errors: parts.append(f"{RED}{errors} errors{RESET}")
            print(f"  {color}[{status}]{RESET} {label}: {', '.join(parts)}")
            if result.get("dirty_details"):
                for dd in result["dirty_details"][:3]:
                    print(f"    - {dd['service']} ({dd['files']} uncommitted)")
        elif name == "observability":
            containers = result.get("containers", 0)
            running = result.get("running", 0)
            if containers:
                print(f"  {color}[{status}]{RESET} {label}: {running}/{containers} containers running")
            else:
                print(f"  {color}[{status}]{RESET} {label}: {result.get('message', 'unknown')}")

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
