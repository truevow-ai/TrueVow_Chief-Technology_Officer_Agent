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
"""

import subprocess
import sys
import yaml
import os
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
