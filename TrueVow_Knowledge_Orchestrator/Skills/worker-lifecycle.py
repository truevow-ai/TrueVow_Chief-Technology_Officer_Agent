#!/usr/bin/env python3
"""
Worker Lifecycle Manager — tool-agnostic agent state machine.
Manages worker state across sessions using the filesystem + Supabase.
Inspired by HiClaw's controller reconciler pattern.

States: pending → active → sleeping → stopped
                                    ↘ failed

Usage:
    python worker-lifecycle.py --action heartbeat --agent settle-agent
    python worker-lifecycle.py --action status --agent settle-agent
    python worker-lifecycle.py --action start --agent settle-agent
    python worker-lifecycle.py --action stop --agent settle-agent
    python worker-lifecycle.py --action gc  # auto-stop idle workers
    python worker-lifecycle.py --action list
"""

import argparse
import json
import os
import sys
import yaml
from datetime import datetime, timezone, timedelta
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parents[1]
WORKERS_DIR = VAULT_ROOT / "Agent" / "workers"
STATE_FILE = VAULT_ROOT / "Agent" / "worker-state.json"
LIVE_DIR = VAULT_ROOT / "Session-Logs" / "live"

VALID_STATES = ["pending", "active", "sleeping", "stopped", "failed"]
VALID_TRANSITIONS = {
    "pending": ["active", "stopped"],
    "active": ["sleeping", "stopped", "failed"],
    "sleeping": ["active", "stopped"],
    "stopped": ["active"],
    "failed": ["active", "stopped"],
}

DEFAULT_IDLE_MINUTES = 30
DEFAULT_HEARTBEAT_SEC = 300
DEFAULT_MAX_RETRIES = 3
DEFAULT_TIMEOUT_MINUTES = 120


def load_state() -> dict:
    if STATE_FILE.exists():
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    return {"workers": {}, "updated": None}


def save_state(state: dict):
    state["updated"] = datetime.now(timezone.utc).isoformat()
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2, default=str)


def load_spec(agent_name: str) -> dict | None:
    spec_path = WORKERS_DIR / f"{agent_name}.yaml"
    if not spec_path.exists():
        return None
    with open(spec_path, "r") as f:
        return yaml.safe_load(f)


def resolve_agent_id(agent_name: str) -> str:
    spec = load_spec(agent_name)
    if not spec:
        return agent_name
    return f"{spec.get('developer', 'unknown')}-{agent_name}"


def log_lifecycle_event(agent: str, action: str, detail: str):
    LIVE_DIR.mkdir(parents=True, exist_ok=True)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    log_path = LIVE_DIR / f"{today}.jsonl"
    entry = {
        "ts": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "agent": resolve_agent_id(agent),
        "action": f"lifecycle-{action}",
        "detail": detail,
        "service": agent,
        "path": "",
        "verification": "VERIFIED",
    }
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def heartbeat(agent_name: str) -> dict:
    spec = load_spec(agent_name)
    if not spec:
        return {"error": f"No spec found for {agent_name}"}

    state = load_state()
    worker_state = state["workers"].get(agent_name, {
        "state": "pending",
        "last_heartbeat": None,
        "task_count": 0,
        "retry_count": 0,
        "started_at": None,
    })

    now = datetime.now(timezone.utc)

    if worker_state["state"] == "pending":
        worker_state["state"] = "active"
        worker_state["started_at"] = now.isoformat()

    if worker_state["state"] == "sleeping":
        worker_state["state"] = "active"

    worker_state["last_heartbeat"] = now.isoformat()
    worker_state["task_count"] = worker_state.get("task_count", 0)

    state["workers"][agent_name] = worker_state
    save_state(state)

    return {
        "agent": agent_name,
        "state": worker_state["state"],
        "last_heartbeat": worker_state["last_heartbeat"],
        "task_count": worker_state["task_count"],
    }


def set_state(agent_name: str, new_state: str) -> dict:
    spec = load_spec(agent_name)
    if not spec:
        return {"error": f"No spec found for {agent_name}"}

    state = load_state()
    worker_state = state["workers"].get(agent_name, {"state": "pending"})
    current = worker_state["state"]

    if new_state not in VALID_TRANSITIONS.get(current, []):
        return {"error": f"Invalid transition: {current} → {new_state}. Allowed: {VALID_TRANSITIONS.get(current, [])}"}

    worker_state["state"] = new_state
    state["workers"][agent_name] = worker_state
    save_state(state)

    log_lifecycle_event(agent_name, "state-change", f"{current} → {new_state}")
    return {"agent": agent_name, "state": new_state}


def garbage_collect() -> list:
    """Auto-stop idle workers that have exceeded their max_idle_minutes."""
    state = load_state()
    now = datetime.now(timezone.utc)
    stopped = []

    for agent_name, worker_state in state["workers"].items():
        if worker_state["state"] not in ("active", "sleeping"):
            continue

        spec = load_spec(agent_name)
        idle_minutes = spec.get("lifecycle", {}).get("max_idle_minutes", DEFAULT_IDLE_MINUTES) if spec else DEFAULT_IDLE_MINUTES

        last_hb = worker_state.get("last_heartbeat")
        if last_hb:
            last = datetime.fromisoformat(last_hb)
            idle_time = (now - last).total_seconds() / 60
            if idle_time > idle_minutes:
                worker_state["state"] = "sleeping"
                state["workers"][agent_name] = worker_state
                stopped.append(agent_name)
                log_lifecycle_event(agent_name, "auto-sleep", f"Idle for {idle_time:.0f}min (limit: {idle_minutes}min)")

    if stopped:
        save_state(state)

    return stopped


def list_workers() -> list:
    state = load_state()
    results = []
    for spec_file in sorted(WORKERS_DIR.glob("*.yaml")):
        if spec_file.name.startswith("_"):
            continue
        agent_name = spec_file.stem
        worker_state = state["workers"].get(agent_name, {"state": "pending", "last_heartbeat": None})
        spec = load_spec(agent_name) or {}
        results.append({
            "agent": agent_name,
            "developer": spec.get("developer", "unknown"),
            "state": worker_state.get("state", "pending"),
            "last_heartbeat": worker_state.get("last_heartbeat"),
            "task_count": worker_state.get("task_count", 0),
        })
    return results


def main():
    parser = argparse.ArgumentParser(description="Worker Lifecycle Manager")
    parser.add_argument("--action", required=True,
                        choices=["heartbeat", "start", "stop", "sleep", "status", "list", "gc"])
    parser.add_argument("--agent", help="Agent name (e.g. settle-agent)")
    args = parser.parse_args()

    if args.action == "heartbeat":
        if not args.agent:
            print(json.dumps({"error": "--agent required for heartbeat"}))
            sys.exit(1)
        result = heartbeat(args.agent)
        log_lifecycle_event(args.agent, "heartbeat", "OK")
        print(json.dumps(result))

    elif args.action == "start":
        if not args.agent:
            print(json.dumps({"error": "--agent required"}))
            sys.exit(1)
        print(json.dumps(set_state(args.agent, "active")))

    elif args.action == "stop":
        if not args.agent:
            print(json.dumps({"error": "--agent required"}))
            sys.exit(1)
        print(json.dumps(set_state(args.agent, "stopped")))

    elif args.action == "sleep":
        if not args.agent:
            print(json.dumps({"error": "--agent required"}))
            sys.exit(1)
        print(json.dumps(set_state(args.agent, "sleeping")))

    elif args.action == "status":
        if not args.agent:
            print(json.dumps({"error": "--agent required"}))
            sys.exit(1)
        state = load_state()
        print(json.dumps(state["workers"].get(args.agent, {"state": "pending"})))

    elif args.action == "list":
        print(json.dumps(list_workers(), indent=2))

    elif args.action == "gc":
        stopped = garbage_collect()
        print(json.dumps({"stopped": stopped, "count": len(stopped)}))


if __name__ == "__main__":
    main()
