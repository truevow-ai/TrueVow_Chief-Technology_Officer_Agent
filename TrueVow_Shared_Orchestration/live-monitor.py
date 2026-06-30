#!/usr/bin/env python3
"""
Real-Time Agent Activity Monitor — Live central logging aggregator.
Polls memory.db every 2 seconds and streams new agent activities to the console.
This is the CTO's live view of all sub-coding agents working across the platform.

Usage:
  python TrueVow_Shared_Orchestration/live-monitor.py           # Continuous live stream
  python TrueVow_Shared_Orchestration/live-monitor.py --once    # Single snapshot
  python TrueVow_Shared_Orchestration/live-monitor.py --json    # JSON output for integrations
"""

import sys
import time
import json
from pathlib import Path
from datetime import datetime, timezone

# Windows: force UTF-8
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "TrueVow_Shared_Codebase_Memory" / "memory.db"

# Status colors
STATUS_COLOR = {
    "DONE": "\033[92m",      # Green
    "ACTIVE": "\033[94m",    # Blue
    "BLOCKED": "\033[93m",   # Yellow
    "UNVERIFIED": "\033[91m",# Red
    "ERROR": "\033[91m",     # Red
    "RESET": "\033[0m",
}

PHASE_ICON = {
    "start": "[+]",
    "done": "[OK]",
    "blocked": "[!!]",
    "progress": "[..]",
    "status": "[?]",
}

def get_db():
    import sqlite3
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn


def get_latest_activities(limit: int = 50):
    """Pull latest agent-checkin activities from memory."""
    conn = get_db()
    rows = conn.execute("""
        SELECT * FROM memories
        WHERE tags LIKE '%agent-checkin%'
        ORDER BY updated_at DESC
        LIMIT ?
    """, (limit,)).fetchall()
    conn.close()

    activities = []
    for row in rows:
        try:
            data = json.loads(row["tags"])
            if isinstance(data, list) and "agent-checkin" in data:
                content = json.loads(row["content"])
                activities.append({
                    "agent": content.get("agent_id", "unknown"),
                    "action": content.get("action", ""),
                    "status": content.get("status", ""),
                    "message": content.get("message", ""),
                    "timestamp": content.get("timestamp", ""),
                    "memory_id": row["id"],
                })
        except (json.JSONDecodeError, TypeError):
            continue

    return activities


def print_activity(activity: dict):
    """Print a single activity line with color."""
    agent = activity["agent"]
    action = activity["action"]
    status = activity["status"]
    msg = activity["message"][:120]
    msg = msg.encode("ascii", errors="replace").decode("ascii")
    ts = activity["timestamp"][:19] if activity["timestamp"] else ""

    color = STATUS_COLOR.get(status, "")
    reset = STATUS_COLOR["RESET"]
    icon = PHASE_ICON.get(action, "   ")

    print(f"{color}{icon} [{status:10s}] {agent:40s} | {msg}{reset}")
    sys.stdout.flush()


def show_once():
    """Single snapshot of current state."""
    activities = get_latest_activities(30)
    # Deduplicate by agent: show latest per agent
    seen = set()
    unique = []
    for a in activities:
        if a["agent"] not in seen:
            seen.add(a["agent"])
            unique.append(a)

    print(f"\n=== REAL-TIME AGENT ACTIVITY (snapshot) ===\n")
    for a in unique:
        print_activity(a)
    print(f"\n  {len(unique)} agents tracked | {len(activities)} total activities")


def show_json():
    """JSON output for integrations."""
    activities = get_latest_activities(30)
    seen = set()
    unique = []
    for a in activities:
        if a["agent"] not in seen:
            seen.add(a["agent"])
            unique.append(a)
    print(json.dumps(unique, indent=2, ensure_ascii=False))


def watch(interval: float = 2.0):
    """Continuous live stream — polls for new activities."""
    print("\n=== LIVE AGENT MONITOR — CTO Central Logging ===")
    print("  Polling every {:.0f}s. Ctrl+C to stop.\n".format(interval))

    last_id = None

    # Get initial state
    conn = get_db()
    try:
        while True:
            rows = conn.execute("""
                SELECT * FROM memories
                WHERE tags LIKE '%agent-checkin%'
                ORDER BY updated_at DESC
                LIMIT 20
            """).fetchall()

            if rows and rows[0]["id"] != last_id:
                last_id = rows[0]["id"]
                for row in rows[:5]:  # Show 5 most recent
                    try:
                        content_data = json.loads(row["content"])
                        activity = {
                            "agent": content_data.get("agent_id", "unknown"),
                            "action": content_data.get("action", ""),
                            "status": content_data.get("status", ""),
                            "message": content_data.get("message", ""),
                            "timestamp": content_data.get("timestamp", ""),
                        }
                        print_activity(activity)
                    except (json.JSONDecodeError, TypeError):
                        continue

            sys.stdout.flush()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\n[CTO] Monitoring stopped.")
    finally:
        conn.close()


if __name__ == "__main__":
    if "--once" in sys.argv:
        show_once()
    elif "--json" in sys.argv:
        show_json()
    else:
        watch()
