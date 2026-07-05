#!/usr/bin/env python3
"""
Real-Time Agent Reporting System.
Every agent checks in/out through this. The CTO (orchestrator) tracks all activity.

Agent check-in protocol:
  python TrueVow_Shared_Orchestration/orchestrator.py agent-checkin start "ServiceName: what I'm doing"
  python TrueVow_Shared_Orchestration/orchestrator.py agent-checkin progress "what I've completed so far"
  python TrueVow_Shared_Orchestration/orchestrator.py agent-checkin done "result" --status DONE
  python TrueVow_Shared_Orchestration/orchestrator.py agent-checkin blocked "reason"
  python TrueVow_Shared_Orchestration/orchestrator.py agent-checkin status    ← show current status

All activity logged to memory.db and visible on the dashboard.
"""

import json
import sys
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "TrueVow_Shared_Codebase_Memory" / "memory.db"


def get_agent_id():
    """Derive a stable agent ID from the working directory."""
    cwd = Path.cwd().resolve()
    try:
        relative = cwd.relative_to(ROOT)
        return str(relative.parts[0]) if relative.parts else "orchestrator"
    except ValueError:
        return cwd.name


def checkin(action: str, message: str = "", status: str = "ACTIVE"):
    """
    Agent check-in protocol. Called by any agent in any service.

    Actions:
      start    - Agent begins a session. Registers in dashboard.
      progress - Agent reports intermediate progress.
      done     - Agent completed a task. Provide result.
      blocked  - Agent is blocked. Provide reason.
      status   - Show current agent status.
    """
    from memory import MemoryDatabase

    agent_id = get_agent_id()
    db = MemoryDatabase(str(DB_PATH))
    timestamp = datetime.now(timezone.utc).isoformat()

    if action == "status":
        results = db.query(
            query=agent_id,
            category="context",
            sort_by="recent",
            limit=5,
        )
        results = [r for r in results if "agent-checkin" in r.get("tags", [])]
        if results:
            print(f"\n=== Agent: {agent_id} ===\n")
            for r in results:
                print(f"  [{r['updatedAt'][:19]}] {r['title']}")
                print(f"    {r['content'][:200]}")
        else:
            print(f"\n=== Agent: {agent_id} ===\n  No activity logged yet.")
        db.close()
        return

    title = f"[{status}] {action.upper()}: {message[:100]}"
    content = json.dumps({
        "agent_id": agent_id,
        "action": action,
        "status": status,
        "message": message,
        "timestamp": timestamp,
        "working_dir": str(Path.cwd()),
    })

    entry = db.create(
        category="context",
        title=title,
        content=content,
        tags=["agent-checkin", action, status, agent_id],
        importance=7 if action in ("start", "done") else 5,
    )

    print(f"[{status}] Agent '{agent_id}' checked in: {action}")
    print(f"  {message[:120]}")
    print(f"  Memory ID: {entry['id']}")

    db.close()


def get_dashboard() -> dict:
    """Build the live agent dashboard from all agent-checkin memories."""
    from memory import MemoryDatabase
    db = MemoryDatabase(str(DB_PATH))

    # Get all recent checkins (don't use FTS query - it sorts by rank not date)
    all_checkins = db.query(
        category="context",
        sort_by="recent",
        limit=200,
    )

    # Filter to only agent-checkin tagged entries
    checkins = [c for c in all_checkins if "agent-checkin" in c.get("tags", [])]

    # Group by agent
    agents = {}
    for entry in checkins:
        try:
            data = json.loads(entry["content"])
        except (json.JSONDecodeError, TypeError):
            continue
        agent_id = data.get("agent_id", "unknown")
        if agent_id not in agents:
            agents[agent_id] = []
        agents[agent_id].append(data)

    # Get latest status per agent (most recent timestamp)
    dashboard = {}
    for agent_id, entries in agents.items():
        entries.sort(key=lambda e: e.get("timestamp", ""), reverse=True)
        latest = entries[0]
        dashboard[agent_id] = {
            "status": latest.get("status", "UNKNOWN"),
            "last_action": latest.get("action", ""),
            "last_message": latest.get("message", ""),
            "last_seen": latest.get("timestamp", ""),
            "total_checkins": len(entries),
        }

    db.close()
    return dashboard


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python reporting.py <action> [message] [--status STATUS]")
        print("Actions: start | progress | done | blocked | status | dashboard")
        sys.exit(0)

    action = sys.argv[1]
    message = sys.argv[2] if len(sys.argv) > 2 else ""
    status = "ACTIVE"

    # Parse --status flag
    args = sys.argv[3:]
    for i, arg in enumerate(args):
        if arg == "--status" and i + 1 < len(args):
            status = args[i + 1]

    if action == "dashboard":
        dash = get_dashboard()
        print(json.dumps(dash, indent=2))
    else:
        checkin(action, message, status)
