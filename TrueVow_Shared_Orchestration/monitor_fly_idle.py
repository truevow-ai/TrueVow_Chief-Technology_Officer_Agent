#!/usr/bin/env python3
"""
Fly.io idle-machine monitor — stops machines idle > 30 min.
Run via the orchestrator or standalone: python monitor_fly_idle.py
Depends on: flyctl CLI installed and authenticated.
"""

import subprocess, sys, json, time
from datetime import datetime, timezone, timedelta
from pathlib import Path

IDLE_MINUTES = 30
CHECK_INTERVAL_S = 1260  # every 21 minutes
FLY_ORG = "truevow"

def run(*args):
    return subprocess.run(args, capture_output=True, text=True, timeout=30)

def list_apps(org):
    r = run("flyctl", "apps", "list", "--org", org)
    apps = []
    for line in r.stdout.strip().split("\n"):
        parts = line.split()
        if len(parts) >= 3 and parts[0] not in ("NAME", ""):
            apps.append(parts[0])
    return apps

def list_machines(app):
    r = run("flyctl", "machines", "list", "--app", app, "--json")
    if not r.stdout.strip():
        return []
    try:
        return json.loads(r.stdout)
    except Exception:
        return []

def machine_events(app, machine_id):
    r = run("flyctl", "machine", "status", machine_id, "--app", app)
    events = []
    in_log = False
    for line in r.stdout.split("\n"):
        line = line.strip()
        if "Event Logs" in line:
            in_log = True
            continue
        if in_log and line and not line.startswith("STATE"):
            parts = line.split("|")
            if len(parts) >= 4:
                ts_str = parts[3].strip()
                parts2 = ts_str.split("+")
                ts_clean = parts2[0].strip()
                try:
                    events.append(datetime.fromisoformat(ts_clean))
                except Exception:
                    pass
    return events

def should_stop(machine, app):
    if machine.get("state") != "started":
        return False, None
    events = machine_events(app, machine["id"])
    if not events:
        return True, "no events"
    latest = max(events)
    idle = (datetime.now(timezone.utc) - latest.replace(tzinfo=timezone.utc)).total_seconds() / 60
    if idle > IDLE_MINUTES:
        return True, f"idle {idle:.0f} min"
    return False, None

def stop_machine(app, machine_id, name):
    print(f"  STOP {app}/{name} ({machine_id})")
    r = run("flyctl", "machines", "stop", machine_id, "--app", app)
    if "successfully stopped" in r.stdout:
        print(f"    -> stopped")
        return True
    print(f"    -> {r.stdout.strip() or r.stderr.strip()}")
    return False

def monitor(org, once=False):
    stopped = 0
    while True:
        print(f"\n--- check {datetime.now(timezone.utc).isoformat()} ---")
        apps = list_apps(org)
        total = 0
        for app in apps:
            for m in list_machines(app):
                total += 1
                stop, reason = should_stop(m, app)
                if stop:
                    print(f"  IDLE: {app}/{m['name']} ({reason})")
                    if stop_machine(app, m["id"], m["name"]):
                        stopped += 1
        print(f"  checked {total} machines across {len(apps)} apps, stopped {stopped} total this session")
        if once:
            break
        print(f"  sleeping {CHECK_INTERVAL_S}s...")
        time.sleep(CHECK_INTERVAL_S)
    return stopped

if __name__ == "__main__":
    once = "--once" in sys.argv
    monitor(FLY_ORG, once=once)
