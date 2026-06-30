#!/usr/bin/env python3
"""
OSS Tools Setup — One command to start all open-source replacements.
Run: python shared-libraries/oss-tools/setup.py

Services:
  Chatwoot (port 3007)   → replaces First-Line Support
  Mattermost (port 8065) → replaces Internal Ops Team Chat
  Novu (port 3009/4200)  → replaces custom notifications
  PostHog (port 8010)    → augments Platform Analytics
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
COMPOSE_FILE = Path(__file__).resolve().parent / "docker-compose.yml"


def cmd(c, **kw):
    return subprocess.run(c, shell=True, capture_output=True, text=True, cwd=str(ROOT), **kw)


def status():
    """Show status of all OSS tools."""
    print("\n=== OSS TOOLS STATUS ===\n")
    r = cmd("docker ps --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}' --filter name=truevow-chatwoot --filter name=truevow-mattermost --filter name=truevow-novu --filter name=truevow-posthog")
    if r.stdout.strip():
        print(r.stdout)
    else:
        print("  No OSS tool containers running.")
        print("  Run: python shared-libraries/oss-tools/setup.py start")


def start():
    """Start all OSS tools."""
    print("\n=== Starting OSS Tools Stack ===\n")
    r = subprocess.run(
        ["docker-compose", "-f", str(COMPOSE_FILE), "up", "-d"],
        cwd=str(ROOT),
    )
    if r.returncode == 0:
        print("\nServices starting. URLs:")
        print("  Chatwoot:    http://localhost:3007")
        print("  Mattermost:  http://localhost:8065")
        print("  Novu:        http://localhost:4200")
        print("  PostHog:     http://localhost:8010")
    else:
        print("\nSome services may have failed. Check: docker ps -a")
        print("Retry: python shared-libraries/oss-tools/setup.py start")


def stop():
    """Stop all OSS tools."""
    r = cmd(f"docker-compose -f {COMPOSE_FILE} down")
    print("OSS tools stopped.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python setup.py start          Start all OSS tools")
        print("  python setup.py stop           Stop all tools")
        print("  python setup.py status         Show status")
        sys.exit(0)

    action = sys.argv[1]
    if action == "start":
        start()
    elif action == "stop":
        stop()
    elif action == "status":
        status()
    else:
        print(f"Unknown: {action}")
