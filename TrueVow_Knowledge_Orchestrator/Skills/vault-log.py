#!/usr/bin/env python3
"""
Live Session Logger — tool-agnostic JSONL stream to TrueVow_Knowledge vault.
Every agent (opencode, Cursor, Pi, CLI) writes structured log entries here.
No dependency on any specific agent harness. Plain JSONL on filesystem.

Usage:
    python vault-log.py --agent yasha-orchestrator --action "task-start" --detail "Building credential scoping"
    python vault-log.py --agent sania-sales-agent --action "file-write" --detail "Updated pipeline.ts" --path "app/api/pipeline/route.ts"

Stream format (JSONL — one JSON object per line):
    {"ts":"2026-06-16T18:00:00Z","agent":"yasha-orchestrator","action":"task-start","detail":"...","service":"settle","path":null,"verification":"UNVERIFIED"}

Verification tags: VERIFIED | COMPILED | SCAFFOLDED | UNTESTED | ASSUMED
"""

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parents[2] / "TrueVow_Knowledge"
LIVE_DIR = VAULT_ROOT / "Session-Logs" / "live"
LIVE_DIR.mkdir(parents=True, exist_ok=True)


def log_entry(
    agent: str,
    action: str,
    detail: str = "",
    service: str = "",
    path: str = "",
    verification: str = "UNVERIFIED",
) -> str:
    now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    entry = {
        "ts": now,
        "agent": agent,
        "action": action,
        "detail": detail[:500],
        "service": service,
        "path": path,
        "verification": verification,
    }

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    log_path = LIVE_DIR / f"{today}.jsonl"

    with open(log_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    return json.dumps(entry)


ACTIONS = [
    "task-start", "task-complete", "task-fail",
    "file-read", "file-write", "file-delete",
    "subagent-launch", "subagent-result",
    "decision", "blocker", "question",
    "commit", "deploy",
    "session-start", "session-end", "heartbeat",
]


def main():
    parser = argparse.ArgumentParser(description="Vault Live Logger (tool-agnostic)")
    parser.add_argument("--agent", required=True, help="Agent ID (e.g. yasha-orchestrator)")
    parser.add_argument("--action", required=True, choices=ACTIONS, help="Action type")
    parser.add_argument("--detail", default="", help="Description of the action")
    parser.add_argument("--service", default="", help="Service name")
    parser.add_argument("--path", default="", help="File path if relevant")
    parser.add_argument("--verification", default="UNVERIFIED",
                        choices=["VERIFIED", "COMPILED", "SCAFFOLDED", "UNTESTED", "ASSUMED"])
    args = parser.parse_args()

    result = log_entry(
        agent=args.agent,
        action=args.action,
        detail=args.detail,
        service=args.service,
        path=args.path,
        verification=args.verification,
    )
    print(result)


if __name__ == "__main__":
    main()
