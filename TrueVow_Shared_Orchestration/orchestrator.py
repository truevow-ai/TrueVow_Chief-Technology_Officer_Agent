#!/usr/bin/env python3
"""
TrueVow Agent Ecosystem Orchestrator v2.1
Harness-agnostic. Auto-dispatches user intent → skill → persona.
Multi-developer sync via shared git-tracked memory.db.

Commands:
  python orchestrator.py doctor              Full diagnostic
  python orchestrator.py list                List all skills + personas + agents
  python orchestrator.py monitor             Health check
  python orchestrator.py dispatch "<task>"   Auto-map intent → skill → persona, load SKILL.md
  python orchestrator.py skill <name>        Print a SKILL.md content
  python orchestrator.py memory-summary      Memory database stats
  python orchestrator.py sync-obsidian       Sync to Obsidian vault
  python orchestrator.py skill-scan          Security scan skills
  python orchestrator.py sync-memory         Pull latest shared memory.db from git
  python orchestrator.py push-memory         Commit + push memory.db to shared repo
  python orchestrator.py scan-services [--watch] [--json]  Scan git state of all registered services
"""

import subprocess
import sys
import json
import yaml
import os
import time
from pathlib import Path
from datetime import datetime, timezone

_ORCH_DIR = str(Path(__file__).resolve().parent)
if _ORCH_DIR not in sys.path:
    sys.path.insert(0, _ORCH_DIR)
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Windows: force UTF-8 for printing SKILL.md files (they contain Unicode)
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
AGENT_TOOLS = ROOT / "TrueVow_Shared_Agent_Tools"
SKILLS_DIR = AGENT_TOOLS / "agent-skills" / "skills"
AGENTS_DIR = AGENT_TOOLS / "agent-skills" / "agents"
VAULT = ROOT / "TrueVow_Knowledge"

def cmd(cmdline, **kwargs):
    return subprocess.run(cmdline, cwd=str(ROOT), capture_output=True, text=True, **kwargs)

def _load_config() -> dict:
    cfg_path = Path(__file__).parent / "config.yaml"
    with open(cfg_path, encoding="utf-8") as f:
        return yaml.safe_load(f)

# ═══════════════════════════════════════════════
#  DISPATCH: Intent → Skill → Persona
# ═══════════════════════════════════════════════

def dispatch(user_request: str):
    """
    Given a user request, find the matching skill(s) and persona(s),
    print the relevant SKILL.md content for the agent to follow.
    Uses word-boundary word-set matching — multi-word keywords score higher.
    """
    cfg = _load_config()
    user_lower = user_request.lower()
    user_words = set(user_lower.split())
    matches = []

    for entry in cfg.get("dispatch", []):
        score = 0
        for kw in entry.get("intent", []):
            kw_words = set(kw.split())
            if kw_words.issubset(user_words):
                score += len(kw_words)  # multi-word keywords weight more

        if score > 0:
            skill = entry.get("skill", "")
            persona = entry.get("persona", "")
            personas = entry.get("personas", [])
            if persona:
                personas = [persona] + personas
            matches.append({
                "skill": skill,
                "personas": list(set(personas)),
                "phase": entry.get("phase", ""),
                "score": score,
                "tool": entry.get("tool", ""),
                "service": entry.get("service", ""),
            })

    if not matches:
        # Fallback: default to using-agent-skills for the agent to figure out
        print("=== DISPATCH: No direct match found — loading meta-skill ===\n")
        print("Recommendation: Load `using-agent-skills` to help the agent discover the right skill.\n")
        print_skill("using-agent-skills")
        return

    # Sort by highest score
    matches.sort(key=lambda m: -m["score"])
    best = matches[0]

    print(f"=== DISPATCH: \"{user_request[:80]}\" ===")
    print(f"  Phase:    {best['phase'].upper() if best['phase'] else 'GENERAL'}")
    print(f"  Skill:    {best['skill']}")
    if best["personas"]:
        print(f"  Personas: {', '.join(best['personas'])}")
    if best["tool"]:
        print(f"  Tool:     {best['tool']}")
    if best.get("service"):
        print(f"  Service:  {best['service']}")
    print()

    # Load and print the matched skill
    skill_path = None
    if best["tool"] == "agent-reach":
        skill_path = AGENT_TOOLS / "agent-reach" / "agent_reach" / "skill" / "SKILL_en.md"
    elif best["tool"] == "skillspector":
        print("  [INFO] SkillSpector is a CLI tool. Commands:")
        print("    skillspector scan <path> --no-llm  # Fast static-only scan")
        print("    skillspector scan <path>             # Full LLM semantic scan")
        print("    skillspector baseline <path>          # Generate suppression baseline")
        return
    elif best.get("service"):
        # Service-specific skills (e.g. FM .opencode/skills/)
        svc = best["service"]
        skill_path = ROOT / svc / ".opencode" / "skills" / best["skill"] / "SKILL.md"
    else:
        skill_path = SKILLS_DIR / best["skill"] / "SKILL.md"

    if skill_path and skill_path.exists():
        content = skill_path.read_text(encoding="utf-8")
        # Print persona first if available
        for pname in best.get("personas", []):
            persona_path = AGENTS_DIR / f"{pname}.md"
            if persona_path.exists():
                print(f"--- PERSONA: {pname} ---")
                print(persona_path.read_text(encoding="utf-8"))
                print()
        print(f"--- SKILL: {best['skill']} ---")
        print(content)
    else:
        print(f"  [WARN] Skill file not found: {skill_path}")

    # Also show any secondary matches
    if len(matches) > 1:
        print("\n--- Alternative skills that also matched ---")
        for m in matches[1:4]:
            print(f"  {m['skill']} (score: {m['score']}, phase: {m.get('phase', '')})")

    # Store the dispatch in session memory (best-effort, non-blocking)
    subprocess.Popen(
        [sys.executable, str(Path(__file__).parent / "memory.py"), "remember",
         "context", f"Dispatch: {user_request[:80]}",
         f"Dispatched to skill='{best['skill']}' phase='{best.get('phase', '')}' personas={best.get('personas', [])} tool={best.get('tool', '')}",
         "--tags", f"dispatch,{best.get('phase', 'general')},{best['skill']}"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )


# ═══════════════════════════════════════════════
#  SCAN-SERVICES: Real-time git state of all services
# ═══════════════════════════════════════════════

def _get_truth_loop_history() -> dict:
    """Query memory.db for truth-loop results. Returns {service_name: latest_result}."""
    import sqlite3
    db_path = ROOT / "TrueVow_Shared_Codebase_Memory" / "memory.db"
    if not db_path.exists():
        return {}
    try:
        conn = sqlite3.connect(str(db_path))
        conn.row_factory = sqlite3.Row
        rows = conn.execute("""
            SELECT content, updated_at FROM memories
            WHERE tags LIKE '%truth-loop%'
            ORDER BY updated_at DESC
            LIMIT 100
        """).fetchall()
        conn.close()

        seen = {}
        for row in rows:
            try:
                data = json.loads(row["content"])
            except (json.JSONDecodeError, TypeError):
                content = row["content"]
                parts = content.split(" | ")
                if len(parts) >= 2:
                    svc_part = parts[0].replace("Service: ", "").strip()
                    result_part = parts[1].replace("Result: ", "").strip()
                    if svc_part not in seen:
                        seen[svc_part] = {
                            "result": result_part,
                            "attempts": 0,
                            "timestamp": row["updated_at"][:19],
                        }
                continue

            svc = data.get("service", data.get("summary", {}).get("total", ""))
            if not svc:
                continue
            if svc not in seen:
                seen[svc] = {
                    "result": "GREEN",
                    "attempts": 0,
                    "timestamp": row["updated_at"][:19],
                }

        return seen
    except Exception:
        return {}


def _parse_kanban_tasks() -> dict:
    """Parse KANBAN-BOARD.md for tasks mapped to services. Returns {service_name: [tasks]}."""
    kanban = ROOT / "TrueVow_Knowledge_Orchestrator" / "KANBAN-BOARD.md"
    if not kanban.exists():
        return {}

    service_words = {
        "Tenant App": "TrueVow_Tenant_Application_Service",
        "tenant app": "TrueVow_Tenant_Application_Service",
        "Customer Portal": "Truevow_Tenant_Customer_Portal_Service",
        "customer portal": "Truevow_Tenant_Customer_Portal_Service",
        "SaaS Admin": "TrueVow_SaaS_Administration_Service",
        "saas admin": "TrueVow_SaaS_Administration_Service",
        "SETTLE": "TrueVow_Tenant_SETTLE-Service",
        "settle": "TrueVow_Tenant_SETTLE-Service",
        "LEVERAGE": "TrueVow_Tenant_LEVERAGE_Service",
        "leverage": "TrueVow_Tenant_LEVERAGE_Service",
        "VERIFY": "TrueVow_Tenant_VERIFY_Service",
        "verify": "TrueVow_Tenant_VERIFY_Service",
        "INTAKE": "TrueVow_Tenant_Application_Service",
        "intake": "TrueVow_Tenant_Application_Service",
        "Billing": "TrueVow-Tenant_Billing-Service",
        "billing": "TrueVow-Tenant_Billing-Service",
        "Financial": "TrueVow_Financial_Management_Service",
        "financial": "TrueVow_Financial_Management_Service",
        "Internal Ops": "TrueVow_Internal_Ops_Service",
        "internal ops": "TrueVow_Internal_Ops_Service",
        "CSM": "TrueVow_Customer_Success_CORE_Service",
        "customer success": "TrueVow_Customer_Success_CORE_Service",
        "Analytics": "TrueVow_Platform_Analytics_Service",
        "analytics": "TrueVow_Platform_Analytics_Service",
        "SoftPhone": "TrueVow_TWIML_SoftPhone_App",
        "TWIML": "TrueVow_TWIML_SoftPhone_App",
        "Sales Ops": "TrueVow_Sales_Ops_Service",
        "sales ops": "TrueVow_Sales_Ops_Service",
    }

    sections = {}
    try:
        content = kanban.read_text(encoding="utf-8")
        current_section = None
        for line in content.split("\n"):
            if line.startswith("## "):
                current_section = line.replace("## ", "").strip()
                sections[current_section] = []
            elif current_section and line.strip().startswith("- ["):
                task = line.strip()
                sections[current_section].append(task)
    except Exception:
        return {}

    tasks_by_service = {}
    for section_name, tasks in sections.items():
        status_short = section_name.split(" ")[-1].lower() if " " in section_name else section_name.lower()
        for task in tasks:
            assigned_svc = None
            for keyword, svc_name in service_words.items():
                if keyword.lower() in task.lower():
                    assigned_svc = svc_name
                    break
            
            is_done = "[x]" in task
            task_text = task[6:] if task.startswith("- [") else task
            
            task_entry = {
                "text": task_text[:100],
                "section": status_short,
                "done": is_done,
            }

            if assigned_svc:
                if assigned_svc not in tasks_by_service:
                    tasks_by_service[assigned_svc] = {"active": [], "done": [], "blocked": [], "pending": []}
                if is_done:
                    tasks_by_service[assigned_svc]["done"].append(task_entry)
                elif "blocked" in status_short:
                    tasks_by_service[assigned_svc]["blocked"].append(task_entry)
                elif "progress" in status_short:
                    tasks_by_service[assigned_svc]["active"].append(task_entry)
                else:
                    tasks_by_service[assigned_svc]["pending"].append(task_entry)

    return tasks_by_service


def _parse_incidents() -> dict:
    """Parse incident files for service references. Returns {service_name: {open: N, resolved: N}}."""
    incidents_dir = ROOT / "TrueVow_Knowledge_Orchestrator" / "Incidents"
    if not incidents_dir.exists():
        return {}

    service_files = {
        "TrueVow_Tenant_Application_Service": ["tenant app", "intake", "application service"],
        "Truevow_Tenant_Customer_Portal_Service": ["customer portal"],
        "TrueVow_SaaS_Administration_Service": ["saas admin", "saaS admin"],
        "TrueVow_Tenant_SETTLE-Service": ["settle", "settlement"],
        "TrueVow_Tenant_LEVERAGE_Service": ["leverage"],
        "TrueVow_Tenant_VERIFY_Service": ["verify"],
        "TrueVow-Tenant_Billing-Service": ["billing"],
        "TrueVow_Financial_Management_Service": ["financial"],
        "TrueVow_Internal_Ops_Service": ["internal ops", "internal operations"],
        "TrueVow_Customer_Success_CORE_Service": ["customer success", "csm"],
        "TrueVow_Platform_Analytics_Service": ["platform analytics", "analytics service"],
        "TrueVow_TWIML_SoftPhone_App": ["softphone", "twiml", "softphone app"],
        "TrueVow_Sales_Ops_Service": ["sales ops"],
    }

    incidents = {}
    try:
        for f_path in incidents_dir.glob("*.md"):
            text = f_path.read_text(encoding="utf-8", errors="replace").lower()
            
            is_cross_service = any(kw in text for kw in ["cross-service", "ecosystem audit", "every service", "all 13"])
            if is_cross_service:
                continue

            resolved = "status: resolved" in text and "status: open" not in text[:200]
            title = f_path.stem[:80]

            for svc_name, keywords in service_files.items():
                if any(kw in text for kw in keywords):
                    if svc_name not in incidents:
                        incidents[svc_name] = {"open": 0, "resolved": 0, "items": []}
                    status = "resolved" if resolved else "open"
                    incidents[svc_name][status] += 1
                    incidents[svc_name]["items"].append({"title": title, "status": status, "bug": "bug" in f_path.name.lower()})
    except Exception:
        pass

    return incidents


def _check_observability() -> dict:
    """Check if observability stack (Docker) is deployed and running."""
    result = {"status": "UNKNOWN", "components": {}}
    
    docker_compose = ROOT / "shared-libraries" / "observability" / "docker-compose.yml"
    if not docker_compose.exists():
        result["status"] = "NO_CONFIG"
        return result

    result["config_exists"] = True
    
    try:
        r = subprocess.run(
            ["docker", "compose", "-f", str(docker_compose), "ps", "--format", "json"],
            capture_output=True, text=True, timeout=15
        )
        if r.returncode == 0 and r.stdout.strip():
            containers = []
            for line in r.stdout.strip().split("\n"):
                try:
                    containers.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
            
            running = [c for c in containers if c.get("State") == "running"]
            result["status"] = "RUNNING" if running else "STOPPED"
            result["components"] = {
                "total": len(containers),
                "running": len(running),
                "containers": [c.get("Name", c.get("Service", "?")) for c in containers],
            }
        else:
            result["status"] = "NOT_DEPLOYED"
    except (FileNotFoundError, Exception):
        result["status"] = "DOCKER_NOT_AVAILABLE"

    return result


def _derive_service_status(svc_name: str, svc_type: str, git_status: str, agent_act: dict,
                           truth_loop: dict, kanban: dict, incidents: dict) -> dict:
    """Derive a combined operational status for a service."""
    status = {
        "overall": "UNKNOWN",
        "git": git_status,
        "agent": "stale",
        "truth_loop": "unknown",
        "tasks": {"active": 0, "blocked": 0, "pending": 0, "done": 0},
        "incidents": {"open": 0, "resolved": 0},
        "badges": [],
    }

    # Agent recency
    if agent_act:
        h = agent_act.get("hours_ago", 999)
        if h < 1:
            status["agent"] = "active"
        elif h < 24:
            status["agent"] = "recent"
        else:
            status["agent"] = "stale"
    
    # Truth-loop
    if svc_name in truth_loop:
        status["truth_loop"] = truth_loop[svc_name]["result"].lower()

    # Kanban tasks
    if svc_name in kanban:
        k = kanban[svc_name]
        status["tasks"]["active"] = len(k.get("active", []))
        status["tasks"]["blocked"] = len(k.get("blocked", []))
        status["tasks"]["pending"] = len(k.get("pending", []))
        status["tasks"]["done"] = len(k.get("done", []))

    # Incidents
    if svc_name in incidents:
        inc = incidents[svc_name]
        status["incidents"]["open"] = inc.get("open", 0)
        status["incidents"]["resolved"] = inc.get("resolved", 0)

    # Derive overall status
    if status["agent"] == "stale" and status["git"] == "DIRTY":
        status["overall"] = "NEGLECTED"
        status["badges"].append("[NEGLECTED]")
    elif status["truth_loop"] == "failed":
        status["overall"] = "FAILING"
        status["badges"].append("[FAILING]")
    elif status["tasks"]["blocked"] > 0:
        status["overall"] = "BLOCKED"
        status["badges"].append("[BLOCKED]")
    elif status["incidents"]["open"] > 0:
        status["overall"] = "INCIDENT"
        status["badges"].append("[INCIDENT]")
    elif status["agent"] == "active" and status["git"] == "CLEAN":
        status["overall"] = "HEALTHY"
    elif status["agent"] == "recent":
        status["overall"] = "ACTIVE"
    elif status["agent"] == "stale":
        status["overall"] = "STALE"
    elif status["git"] == "DIRTY":
        status["overall"] = "DIRTY"
    else:
        status["overall"] = "UNKNOWN"

    if status["tasks"]["active"] > 0:
        status["badges"].append(f"[{status['tasks']['active']} TASKS]")
    if status["tasks"]["pending"] > 0:
        status["badges"].append(f"[{status['tasks']['pending']} PENDING]")

    return status


def _get_agent_activity() -> dict:
    """Query memory.db for recent agent check-ins. Returns {agent_id: details}."""
    import sqlite3
    db_path = ROOT / "TrueVow_Shared_Codebase_Memory" / "memory.db"
    if not db_path.exists():
        return {}
    try:
        conn = sqlite3.connect(str(db_path))
        conn.row_factory = sqlite3.Row
        rows = conn.execute("""
            SELECT content, updated_at FROM memories
            WHERE tags LIKE '%agent-checkin%'
            ORDER BY updated_at DESC
            LIMIT 200
        """).fetchall()
        conn.close()

        agents = {}
        for row in rows:
            try:
                data = json.loads(row["content"])
                agent_id = data.get("agent_id", "")
                ts = data.get("timestamp", "") or row["updated_at"]
                if agent_id and ts and agent_id not in agents:
                    try:
                        last = datetime.fromisoformat(ts)
                        age_h = (datetime.now(timezone.utc) - last).total_seconds() / 3600
                        agents[agent_id] = {
                            "hours_ago": round(age_h, 1),
                            "action": data.get("action", ""),
                            "status": data.get("status", ""),
                            "message": data.get("message", "")[:100],
                        }
                    except (ValueError, TypeError):
                        continue
            except (json.JSONDecodeError, TypeError):
                continue
        return agents
    except Exception:
        return {}


def scan_services(json_output: bool = False, store_memory: bool = True, detail: bool = False) -> dict:
    """
    Scan git state of all registered services.
    Returns structured data. Optionally stores in memory.db.
    """
    cfg = _load_config()
    services = cfg.get("services", {})
    results = {}
    timestamp = datetime.now(timezone.utc).isoformat()

    for svc_name, svc in services.items():
        if svc.get("status") in ("archived", "replaced"):
            continue

        svc_path = ROOT / svc["path"]
        result = {
            "name": svc_name,
            "type": svc.get("type", ""),
            "exists": svc_path.exists(),
            "path": str(svc_path),
        }

        if not svc_path.exists():
            result["status"] = "MISSING"
            results[svc_name] = result
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
            result["status"] = "NO_GIT"
            results[svc_name] = result
            continue

        try:
            commits = subprocess.run(
                ["git", "log", "--oneline", "-10", "--format=%h %s"],
                cwd=str(svc_path), capture_output=True, text=True, timeout=10, encoding="utf-8", errors="replace"
            )
            latest_commit = commits.stdout.strip().split("\n")[0] if commits.stdout.strip() else ""
            
            status_r = subprocess.run(
                ["git", "status", "--porcelain"],
                cwd=str(svc_path), capture_output=True, text=True, timeout=10, encoding="utf-8", errors="replace"
            )
            dirty_files = status_r.stdout.strip().count("\n") + 1 if status_r.stdout.strip() else 0

            branch_r = subprocess.run(
                ["git", "rev-parse", "--abbrev-ref", "HEAD"],
                cwd=str(svc_path), capture_output=True, text=True, timeout=10, encoding="utf-8", errors="replace"
            )
            branch = branch_r.stdout.strip()

            result["status"] = "DIRTY" if dirty_files > 0 else "CLEAN"
            result["branch"] = branch
            result["latest_commit"] = latest_commit
            result["dirty_files"] = dirty_files
            result["dirty_detail"] = status_r.stdout.strip()[:500] if status_r.stdout.strip() else ""
        except Exception as e:
            result["status"] = "ERROR"
            result["error"] = str(e)

        results[svc_name] = result

    total = len(results)
    clean = sum(1 for r in results.values() if r.get("status") == "CLEAN")
    dirty = sum(1 for r in results.values() if r.get("status") == "DIRTY")
    missing = sum(1 for r in results.values() if r.get("status") in ("MISSING", "NO_GIT"))
    errors = sum(1 for r in results.values() if r.get("status") == "ERROR")

    # Agent activity recency check
    agent_activity = _get_agent_activity()
    truth_loop_data = _get_truth_loop_history()
    kanban_tasks = _parse_kanban_tasks()
    incident_data = _parse_incidents()
    observability = _check_observability()

    status_counts = {"HEALTHY": 0, "ACTIVE": 0, "STALE": 0, "NEGLECTED": 0, "BLOCKED": 0, "FAILING": 0, "INCIDENT": 0, "DIRTY": 0, "UNKNOWN": 0}
    stale_services = []

    for svc_name in list(results.keys()):
        r = results[svc_name]
        act = agent_activity.get(svc_name)
        if act:
            r["agent_activity"] = act
            if act["hours_ago"] > 24:
                stale_services.append(svc_name)
        else:
            stale_services.append(svc_name)

        derived = _derive_service_status(
            svc_name, r.get("type", ""), r.get("status", "UNKNOWN"),
            act, truth_loop_data, kanban_tasks, incident_data
        )
        r["derived_status"] = derived["overall"]
        r["badges"] = derived.get("badges", [])
        r["tasks"] = derived.get("tasks", {})
        r["incidents_open"] = derived.get("incidents", {}).get("open", 0)
        r["truth_loop"] = derived.get("truth_loop", "unknown")

        overall = derived.get("overall", "UNKNOWN")
        if overall in status_counts:
            status_counts[overall] += 1

    stale_count = len(stale_services)
    active_count = total - stale_count

    summary = {
        "timestamp": timestamp,
        "total": total,
        "clean": clean,
        "dirty": dirty,
        "missing": missing,
        "errors": errors,
        "stale_services": stale_count,
        "active_services": active_count,
        "status_breakdown": status_counts,
        "observability": observability.get("status", "UNKNOWN"),
        "overall": "DEGRADED" if (dirty or missing or errors or stale_count > 0) else "HEALTHY",
    }

    # Store in memory for historical tracking
    if store_memory:
        content = json.dumps({
            "summary": summary,
            "stale_services": stale_services,
            "services": {k: {
                "latest_commit": v.get("latest_commit", ""),
                "status": v.get("status", ""),
                "dirty_files": v.get("dirty_files", 0),
                "derived_status": v.get("derived_status", ""),
                "badges": v.get("badges", []),
                "agent_activity": v.get("agent_activity"),
                "truth_loop": v.get("truth_loop", "unknown"),
                "incidents_open": v.get("incidents_open", 0),
                "tasks": v.get("tasks", {}),
            } for k, v in results.items()},
        }, indent=2)
        subprocess.Popen(
            [sys.executable, str(Path(__file__).parent / "memory.py"), "remember",
             "context", f"Git Scan: {timestamp[:19]}",
             content,
             "--tags", "git-scan,services,automated",
             "--importance", "8"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )

    if json_output:
        print(json.dumps({"summary": summary, "services": results}, indent=2, ensure_ascii=False))
    else:
        _print_scan_report(summary, results, kanban_tasks, incident_data, detail)

    return {"summary": summary, "services": results}


def _print_scan_report(summary: dict, results: dict, kanban: dict = None, incidents: dict = None, detail: bool = False):
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

    sb = summary.get("status_breakdown", {})

    overall_color = GREEN if summary["overall"] == "HEALTHY" else YELLOW
    print(f"\n{BOLD}{'='*60}{RESET}")
    print(f"{BOLD}  TrueVow CTO Dashboard — Service Health Scan{RESET}")
    print(f"  {summary['timestamp'][:19]}")
    print(f"  Overall: {overall_color}{summary['overall']}{RESET}")
    print(f"{BOLD}{'='*60}{RESET}")

    # Row 1: Git state
    print(f"\n  {BOLD}Git{RESET}: {GREEN}{summary['clean']} clean{RESET} | {YELLOW}{summary['dirty']} dirty{RESET} | {RED}{summary['missing']} missing{RESET} | {RED}{summary['errors']} errors{RESET}")

    # Row 2: Agent activity + stale
    active_count = summary.get("active_services", 0)
    stale_count = summary.get("stale_services", 0)
    print(f"  {BOLD}Agents{RESET}: {GREEN}{active_count} active{RESET} | {RED if stale_count > 0 else GREEN}{stale_count} stale{RESET} (>24h no check-in)")

    # Row 3: Derived status counts
    status_parts = []
    for s, c in sb.items():
        if c == 0:
            continue
        if s in ("HEALTHY", "ACTIVE"):
            status_parts.append(f"{GREEN}{c} {s}{RESET}")
        elif s in ("STALE", "DIRTY"):
            status_parts.append(f"{YELLOW}{c} {s}{RESET}")
        else:
            status_parts.append(f"{RED}{c} {s}{RESET}")
    print(f"  {BOLD}Status{RESET}: {', '.join(status_parts) if status_parts else 'N/A'}")

    # Row 4: Observability
    obs = summary.get("observability", "UNKNOWN")
    obs_color = GREEN if obs == "RUNNING" else YELLOW if obs == "STOPPED" else RED
    print(f"  {BOLD}Observability{RESET}: {obs_color}{obs}{RESET} (Docker Prometheus+Grafana+Jaeger+Sentry)")

    print()

    # Per-service table
    print(f"  {BOLD}{'SERVICE':40s} GIT     STATUS     AGENT       TRUTH   TASKS  INCIDENTS{RESET}")
    print(f"  {'─' * 95}")

    for svc_name, result in results.items():
        git_status = result.get("status", "?")
        if git_status == "CLEAN":
            git_col = f"{GREEN}CLEAN {RESET}"
        elif git_status == "DIRTY":
            git_col = f"{YELLOW}DIRTY{RESET}"
        else:
            git_col = f"{RED}{git_status[:5]:5s}{RESET}"

        derived = result.get("derived_status", "?").upper()
        if derived == "HEALTHY":
            status_col = f"{GREEN}{derived:8s}{RESET}"
        elif derived == "ACTIVE":
            status_col = f"{GREEN}{derived:8s}{RESET}"
        elif derived in ("STALE", "DIRTY"):
            status_col = f"{YELLOW}{derived:8s}{RESET}"
        else:
            status_col = f"{RED}{derived:8s}{RESET}"

        act = result.get("agent_activity")
        if act:
            h = act["hours_ago"]
            if h < 1:
                agent_col = f"{GREEN}active <1h{RESET}"
            elif h < 24:
                agent_col = f"{GREEN}recent {h:.0f}h{RESET}"
            else:
                agent_col = f"{RED}stale {h:.0f}h{RESET}"
        else:
            agent_col = f"{RED}none{RESET}"

        tl = result.get("truth_loop", "?")
        if tl == "green":
            tl_col = f"{GREEN}GREEN{RESET}"
        elif tl == "failed":
            tl_col = f"{RED}FAIL{RESET}"
        else:
            tl_col = "?"

        tasks = result.get("tasks", {})
        task_parts = []
        if tasks.get("active", 0):
            task_parts.append(f"{GREEN}{tasks['active']}a{RESET}")
        if tasks.get("blocked", 0):
            task_parts.append(f"{RED}{tasks['blocked']}b{RESET}")
        if tasks.get("pending", 0):
            task_parts.append(f"{YELLOW}{tasks['pending']}p{RESET}")
        tasks_str = ",".join(task_parts) if task_parts else "-"

        inc_open = result.get("incidents_open", 0)
        inc_col = f"  {RED}{inc_open} open{RESET}" if inc_open else f"{GREEN}0{RESET}"

        # Truncate name
        name = svc_name[:38]

        print(f"  {CYAN}{name:38s}{RESET} {git_col}  {status_col}  {agent_col:12s}  {tl_col:6s}  {tasks_str:10s}  {inc_col}")

        # Show additional detail for non-trivial states
        badges = result.get("badges", [])
        if badges:
            badge_str = "  ".join(b for b in badges)
            print(f"    {MAGENTA}{badge_str}{RESET}")

        act_msg = None
        if act and act.get("message"):
            act_msg = act["message"][:80]
        if act_msg:
            print(f"    {YELLOW}└─ {act_msg}{RESET}")

        dirty_n = result.get("dirty_files", 0)
        if dirty_n > 0 and dirty_n <= 20:
            print(f"    {YELLOW}└─ {dirty_n} uncommitted files{RESET}")
        elif dirty_n > 20:
            print(f"    {RED}└─ {dirty_n} uncommitted files (large){RESET}")

        # Drill-down: show actual task descriptions when --detail flag is set
        if detail:
            svc_kanban = (kanban or {}).get(svc_name, {})
            svc_incidents = (incidents or {}).get(svc_name, {}).get("items", [])

            task_lines = []
            for section, entries in svc_kanban.items():
                for e in entries[:5]:  # limit 5 per section
                    prefix = {"active": "▶", "blocked": "✖", "pending": "○", "done": "✓"}.get(section, "·")
                    task_lines.append(f"     {CYAN}{prefix} [{section}]{RESET} {e['text']}")

            incident_lines = []
            for inc in svc_incidents[:3]:
                icon = "✓" if inc["status"] == "resolved" else "✖"
                incident_lines.append(f"     {RED}{icon} [incident]{RESET} {inc['title'][:70]}")

            if task_lines or incident_lines:
                print(f"    {BOLD}── DETAILS ──{RESET}")
                if task_lines:
                    for l in task_lines:
                        print(l)
                if incident_lines:
                    for l in incident_lines:
                        print(l)

    print()


# ═══════════════════════════════════════════════
#  LIST: All registered agents
# ═══════════════════════════════════════════════

def list_all():
    cfg = _load_config()

    print("\n=== TrueVow Agent Ecosystem — All Registered Agents ===\n")

    # 1. Lifecycle Skills (24)
    print("1. LIFECYCLE SKILLS (24) — DEFINE → PLAN → BUILD → VERIFY → REVIEW → SHIP")
    phases = {
        "META": ["using-agent-skills"],
        "DEFINE": ["interview-me", "idea-refine", "spec-driven-development"],
        "PLAN": ["planning-and-task-breakdown"],
        "BUILD": ["incremental-implementation", "test-driven-development",
                   "context-engineering", "source-driven-development",
                   "doubt-driven-development", "frontend-ui-engineering",
                   "api-and-interface-design"],
        "VERIFY": ["browser-testing-with-devtools", "debugging-and-error-recovery"],
        "REVIEW": ["code-review-and-quality", "code-simplification",
                    "security-and-hardening", "performance-optimization"],
        "SHIP": ["git-workflow-and-versioning", "ci-cd-and-automation",
                  "deprecation-and-migration", "documentation-and-adrs",
                  "observability-and-instrumentation", "shipping-and-launch"],
    }
    for phase, skills in phases.items():
        active = sum(1 for s in skills if (SKILLS_DIR / s / "SKILL.md").exists())
        print(f"  {phase:8s}  {active}/{len(skills)} loaded  |  {', '.join(skills)}")
    print()

    # 2. Agent Personas (4)
    print("2. AGENT PERSONAS (4) — load on matching intent")
    for name, p in cfg.get("personas", {}).items():
        path = ROOT / p["file"]
        exists = path.exists()
        mark = "+" if exists else "-"
        print(f"  {mark} {name:30s} {p['description'][:80]}...")
    print()

    # 3. Tool Skills (2)
    print("3. TOOL SKILLS (2) — internet access + security scanning")
    reach_path = AGENT_TOOLS / "agent-reach" / "agent_reach" / "skill" / "SKILL_en.md"
    print(f"  {'+' if reach_path.exists() else '-'} agent-reach             Live web eyes — 13 platforms, zero API fees")
    print(f"  {'+' if _has_cli('skillspector') else '-'} skillspector-guardrail   NVIDIA security scanner — 68 vulnerability patterns")
    print()

    # 4. Infrastructure
    print("4. INFRASTRUCTURE")
    mem_exists = (ROOT / "TrueVow_Shared_Codebase_Memory" / "memory.db").exists()
    vault_ok = (VAULT / ".obsidian").exists()
    print(f"  {'+' if mem_exists else '-'} Codebase Memory        SQLite DB — remember, recall, summarize")
    print(f"  {'+' if vault_ok else '-'} Obsidian Vault          TrueVow_Knowledge/ — auto-sync")
    print(f"  + Orchestrator           TrueVow_Shared_Orchestration/orchestrator.py — dispatch, doctor, list")
    print()

    # 5. Sub-repo agents (each repo ships its own guidance)
    print("5. SUB-REPO AGENTS (each tool's own internal agents)")
    sub_agents = [
        ("TrueVow_Shared_Agent_Tools/agent-skills/AGENTS.md", "agent-skills internal agent guidance"),
        ("TrueVow_Shared_Agent_Tools/agent-skills/CLAUDE.md", "agent-skills Claude dev guide"),
        ("TrueVow_Shared_Agent_Tools/agent-reach/CLAUDE.md", "Agent-Reach Claude dev guide"),
        ("TrueVow_Shared_Agent_Tools/skillspector/README.md", "SkillSpector README (operation guide)"),
    ]
    for path, desc in sub_agents:
        exists = (ROOT / path).exists()
        print(f"  {'+' if exists else '-'} {desc}")
    print()

    # 6. Registered Services
    services = cfg.get("services", {})
    if services:
        active = [n for n, s in services.items() if s.get("status") not in ("archived", "replaced")]
        archived = [n for n, s in services.items() if s.get("status") in ("archived", "replaced")]
        print(f"6. REGISTERED SERVICES ({len(services)} active, {len(archived)} archived/replaced)")
        for svc_name, svc in services.items():
            if svc.get("status") in ("archived", "replaced"):
                print(f"  - {svc_name} [{svc.get('status').upper()}]")
                print(f"    Replaced by: {svc.get('replaced_by', 'N/A')}  |  {svc.get('note', '')}")
                continue
            skills_count = len(svc.get("skills", []))
            skills_dir = ROOT / svc["path"] / svc.get("skills_dir", ".opencode/skills")
            loaded = 0
            for s in svc.get("skills", []):
                s_path = skills_dir / s["name"] / "SKILL.md"
                if s_path.exists():
                    loaded += 1
            print(f"  + {svc_name}")
            print(f"    Type: {svc.get('type', '')}  |  Stack: {', '.join(svc.get('stack', []))}")
            print(f"    Skills: {loaded}/{skills_count} loaded  |  Rules: {', '.join(svc.get('rules', []))}")
        print()

    # 7. Agent Team (Phase 5)
    agent_file = ROOT / "TrueVow_Knowledge" / "Agent" / "workers" / "phase5-agent-team.yaml"
    if agent_file.exists():
        agent_cfg = yaml.safe_load(agent_file.read_text(encoding="utf-8"))
        agents = agent_cfg.get("agents", [])
        print(f"7. AGENT TEAM ({len(agents)} subagents) — Phase 5")
        for a in agents:
            owner = a.get("owner", "—")
            skills_n = len(a.get("skills", []))
            print(f"  + {a['id']:25s} [{a.get('domain', '')}]  owner={owner}  skills={skills_n}  type={a.get('type', '')}")
        print()


# ═══════════════════════════════════════════════
#  SKILL: Print a skill's content
# ═══════════════════════════════════════════════

def print_skill(name: str):
    # Check main skills
    path = SKILLS_DIR / name / "SKILL.md"
    if path.exists():
        print(path.read_text(encoding="utf-8"))
        return
    # Check agent-reach
    path = AGENT_TOOLS / "agent-reach" / "agent_reach" / "skill" / "SKILL_en.md"
    if name in ("agent-reach",):
        print(path.read_text(encoding="utf-8"))
        return
    # Check personas
    path = AGENTS_DIR / f"{name}.md"
    if path.exists():
        print(path.read_text(encoding="utf-8"))
        return
    print(f"Skill/persona not found: {name}")
    available = [d.name for d in sorted(SKILLS_DIR.iterdir()) if d.is_dir()]
    available += [p.stem for p in AGENTS_DIR.glob("*.md")]
    available += ["agent-reach", "skillspector-guardrail"]
    print(f"Available: {', '.join(sorted(available))}")


# ═══════════════════════════════════════════════
#  DOCTOR
# ═══════════════════════════════════════════════

def run_doctor():
    import monitor
    checks = monitor.run_all_checks()
    monitor.print_summary(checks)


# ═══════════════════════════════════════════════
#  MEMORY SUMMARY
# ═══════════════════════════════════════════════

def memory_summary():
    r = subprocess.run(
        [sys.executable, str(Path(__file__).parent / "memory.py"), "summarize"],
        capture_output=True, text=True, timeout=10
    )
    print(r.stdout)
    if r.stderr:
        print(r.stderr)


# ═══════════════════════════════════════════════
#  MULTI-DEVELOPER SHARED MEMORY SYNC
# ═══════════════════════════════════════════════

def sync_memory():
    """Pull latest shared memory.db from git. Run before starting work."""
    git_dir = ROOT
    if not (git_dir / ".git").exists():
        print("Not a git repo. Run: git clone --recursive <repo-url>")
        return

    print("[sync-memory] Pulling latest shared knowledge...")
    r = subprocess.run(
        ["git", "pull", "origin", "master"],
        cwd=str(git_dir),
        capture_output=True, text=True, timeout=30
    )
    print(r.stdout.strip() or "Already up to date.")
    if r.stderr and "error" in r.stderr.lower():
        print(r.stderr)

    # Also pull submodules
    r2 = subprocess.run(
        ["git", "submodule", "update", "--init", "--recursive"],
        cwd=str(git_dir),
        capture_output=True, text=True, timeout=30
    )
    if r2.stdout.strip():
        print(r2.stdout.strip())


def _try_reindex():
    """Attempt to reindex the knowledge vault. Graceful if Node.js not available."""
    indexer_dir = ROOT / "shared-libraries" / "knowledge-indexer"
    if not (indexer_dir / "node_modules" / ".package-lock.json").exists() and \
       not (indexer_dir / "node_modules" / "@xenova").exists():
        print("[reindex] knowledge-indexer node_modules not found. Run: cd shared-libraries/knowledge-indexer && npm install")
        return

    print("[reindex] Re-indexing knowledge vault...")
    r = subprocess.run(
        ["npx", "tsx", str(indexer_dir / "src" / "index.ts")],
        cwd=str(indexer_dir),
        capture_output=True, text=True, timeout=60
    )
    if r.returncode == 0:
        lines = r.stdout.strip().split("\n")
        summary = lines[-1] if lines else "done"
        print(f"[reindex] {summary}")
    else:
        print(f"[reindex] skipped: {r.stderr.strip()[:100] if r.stderr else 'Node.js or tsx not available'}")


def push_memory():
    """Commit and push memory.db to shared repo after important decisions."""
    git_dir = ROOT
    memory_db = git_dir / "TrueVow_Shared_Codebase_Memory" / "memory.db"

    if not (git_dir / ".git").exists():
        print("Not a git repo. Cannot push shared memory.")
        return

    if not memory_db.exists():
        print("memory.db not found.")
        return

    # Get developer identity
    who = os.environ.get("TRUEVOW_DEV", "unknown")
    r = subprocess.run(
        ["git", "config", "user.name"],
        cwd=str(git_dir), capture_output=True, text=True, timeout=5
    )
    git_user = r.stdout.strip()
    if git_user:
        who = git_user

    # Get last memory title from recent entry
    conn = __import__('sqlite3').connect(str(memory_db))
    conn.row_factory = __import__('sqlite3').Row
    row = conn.execute("SELECT title FROM memories ORDER BY updated_at DESC LIMIT 1").fetchone()
    conn.close()
    title = row["title"] if row else "shared knowledge update"

    # Stage, commit, push
    subprocess.run(
        ["git", "add", "TrueVow_Shared_Codebase_Memory/memory.db"],
        cwd=str(git_dir), capture_output=True, timeout=10
    )
    r = subprocess.run(
        ["git", "commit", "-m", f"memory({who}): {title}"],
        cwd=str(git_dir), capture_output=True, text=True, timeout=10
    )
    if "nothing to commit" in (r.stdout + r.stderr):
        print("[push-memory] No changes to push.")
        return

    print(r.stdout.strip())
    r = subprocess.run(
        ["git", "push", "origin", "master"],
        cwd=str(git_dir), capture_output=True, text=True, timeout=30
    )
    print(r.stdout.strip() or "Pushed.")
    if r.stderr:
        print(r.stderr.strip())


# ═══════════════════════════════════════════════
#  HELPERS
# ═══════════════════════════════════════════════

def _has_cli(name: str) -> bool:
    scripts_dir = Path.home() / "AppData" / "Roaming" / "Python" / "Python313" / "Scripts" / f"{name}.exe"
    return scripts_dir.exists()


def print_help():
    print(__doc__)
    print("Usage:")
    print("  python orchestrator.py doctor              Full diagnostic")
    print("  python orchestrator.py list                All agents + skills")
    print("  python orchestrator.py dispatch \"<task>\"   Auto-map intent → load skill")
    print("  python orchestrator.py skill <name>        Print a SKILL.md")
    print("  python orchestrator.py skill-scan          Security scan")
    print("  python orchestrator.py memory-summary      Memory stats")
    print("  python orchestrator.py sync-obsidian       Sync to vault")
    print("  python orchestrator.py sync-memory         Pull shared memory from git")
    print("  python orchestrator.py push-memory         Commit + push memory to git")
    print("  python orchestrator.py dashboard           Live agent dashboard")
    print("  python orchestrator.py truth-loop <svc>    Self-healing auto-fix loop")
    print("  python orchestrator.py scan-services       Git state of all services [--watch] [--json]")


# ═══════════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════════

def main():
    if len(sys.argv) < 2:
        print_help()
        return

    cmd_name = sys.argv[1]

    if cmd_name == "doctor":
        run_doctor()
    elif cmd_name == "list":
        list_all()
    elif cmd_name == "dispatch":
        if len(sys.argv) < 3:
            print("Usage: python orchestrator.py dispatch \"<task description>\"")
        else:
            dispatch(" ".join(sys.argv[2:]))
    elif cmd_name == "skill":
        if len(sys.argv) < 3:
            print("Usage: python orchestrator.py skill <name>")
        else:
            print_skill(sys.argv[2])
    elif cmd_name == "skill-scan":
        from orchestrator import scan_skills
    elif cmd_name == "memory-summary":
        memory_summary()
    elif cmd_name == "sync-obsidian":
        r = subprocess.run(
            [sys.executable, str(Path(__file__).parent / "obsidian-bridge.py")],
            capture_output=True, text=True, timeout=30
        )
        print(r.stdout)
        if r.stderr:
            print(r.stderr)
        # Auto-reindex after sync (self-improving flywheel)
        _try_reindex()
    elif cmd_name == "reindex":
        _try_reindex()
    elif cmd_name == "agent-checkin":
        import reporting
        action = sys.argv[2] if len(sys.argv) > 2 else "status"
        message = " ".join(sys.argv[3:]) if len(sys.argv) > 3 else ""
        # Remove --status flag from message
        status_val = "ACTIVE"
        args = sys.argv[3:]
        new_msg_parts = []
        skip_next = False
        for i, a in enumerate(args):
            if skip_next:
                skip_next = False
                continue
            if a == "--status" and i + 1 < len(args):
                status_val = args[i + 1]
                skip_next = True
            else:
                new_msg_parts.append(a)
        message = " ".join(new_msg_parts)
        if action == "dashboard":
            dash = reporting.get_dashboard()
            if dash:
                print("\n=== LIVE AGENT DASHBOARD ===\n")
                for agent_id, info in dash.items():
                    icon = {"DONE": "[DONE]", "ACTIVE": "[ACTV]", "BLOCKED": "[BLCK]", "UNVERIFIED": "[UNVF]"}.get(info["status"], "[????]")
                    print(f"  {icon} [{info['status']:10s}] {agent_id}")
                    print(f"    Last: {info['last_action']} — {info['last_message'][:100]}")
                    print(f"    Seen: {info['last_seen'][:19]}")
                    print()
            else:
                print("No agents have checked in yet.")
        else:
            reporting.checkin(action, message, status_val)
    elif cmd_name == "dashboard":
        import reporting
        dash = reporting.get_dashboard()
        if dash:
            print("\n=== LIVE AGENT DASHBOARD ===\n")
            for agent_id, info in dash.items():
                icon = {"DONE": "[DONE]", "ACTIVE": "[ACTV]", "BLOCKED": "[BLCK]", "UNVERIFIED": "[UNVF]"}.get(info["status"], "[????]")
                print(f"  {icon} [{info['status']:10s}] {agent_id}")
                print(f"    Last: {info['last_action']} — {info['last_message'][:100]}")
                print(f"    Seen: {info['last_seen'][:19]}")
                print()
        else:
            print("No agents have checked in yet.")
    elif cmd_name == "monitor":
        run_doctor()
    elif cmd_name == "sync-memory":
        sync_memory()
    elif cmd_name == "push-memory":
        push_memory()
    elif cmd_name == "scan-services":
        json_out = "--json" in sys.argv
        watch = "--watch" in sys.argv
        detail = "--detail" in sys.argv
        if watch:
            interval = 3600
            for i, arg in enumerate(sys.argv):
                if arg == "--interval" and i + 1 < len(sys.argv):
                    interval = int(sys.argv[i + 1]); break
            print(f"[scan-services] Watch mode: scanning every {interval}s. Ctrl+C to stop.")
            try:
                while True:
                    scan_services(json_output=json_out, detail=detail)
                    if json_out:
                        break
                    time.sleep(interval)
            except KeyboardInterrupt:
                print("\n[scan-services] Stopped.")
        else:
            scan_services(json_output=json_out, detail=detail)
    elif cmd_name == "truth-loop":
        svc = sys.argv[2] if len(sys.argv) > 2 else ""
        max_attempts = 3
        args = sys.argv[3:]
        i = 0
        while i < len(args):
            if args[i] == "--max-attempts" and i + 1 < len(args):
                max_attempts = int(args[i + 1]); i += 2
            elif args[i] == "--all":
                svc = "--all"; i += 1
            else:
                i += 1
        if svc:
            loop_args = [sys.executable, str(Path(__file__).parent / "truth-loop.py"), svc, "--max-attempts", str(max_attempts)]
            r = subprocess.run(loop_args, cwd=str(ROOT), timeout=600)
        else:
            print("Usage: python orchestrator.py truth-loop <service-name> [--all] [--max-attempts N]")
    elif cmd_name in ("--help", "-h", "help"):
        print_help()
    else:
        print(f"Unknown command: {cmd_name}")
        print_help()


if __name__ == "__main__":
    main()
