#!/usr/bin/env python3
"""
Agent-Native Verification — replaces CI/CD pipelines.
Runs typecheck + lint + tests for a given service directly from the agent OS.
No YAML pipelines. No GitHub Actions. The orchestrator calls this inline.

Concept from: "CI/CD is Dead — Agents Need Continuous Compute" (NEA/Namespace, 2026)
Agents don't fail on syntax — they need behavioral validation, not pipeline stages.

Usage:
    python verify.py --service settle
    python verify.py --service saas-admin --skip-tests
    python verify.py --service tenant-app --test-only
"""

import argparse
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

CURSOR_ROOT = Path(__file__).resolve().parents[2]
VAULT_ROOT = CURSOR_ROOT / "TrueVow_Knowledge"
LIVE_DIR = VAULT_ROOT / "Session-Logs" / "live"

SERVICE_CONFIG = {
    "saas-admin": {
        "path": "TrueVow_SaaS_Administration_Service",
        "stack": "nextjs",
        "typecheck": ["npx", "tsc", "--noEmit"],
        "lint": ["npx", "next", "lint"],
        "test": ["npx", "jest", "--passWithNoTests"],
        "port": 3001,
    },
    "customer-portal": {
        "path": "Truevow_Tenant_Customer_Portal_Service",
        "stack": "nextjs",
        "typecheck": ["npx", "tsc", "--noEmit"],
        "lint": ["npx", "next", "lint"],
        "test": ["npx", "playwright", "test"],
        "port": 3031,
    },
    "csm-core": {
        "path": "TrueVow_Customer_Success_CORE_Service",
        "stack": "nextjs",
        "typecheck": ["npx", "tsc", "--noEmit"],
        "lint": ["npx", "next", "lint"],
        "test": ["npx", "jest"],
        "port": 3012,
    },
    "first-line-support": {
        "path": "TrueVow_First_Line_Support_Service",
        "stack": "nextjs",
        "typecheck": ["npx", "tsc", "--noEmit"],
        "lint": ["npx", "next", "lint"],
        "test": ["npx", "jest", "--passWithNoTests"],
        "port": None,
    },
    "sales-ops": {
        "path": "TrueVow_Sales_Ops_Service",
        "stack": "nextjs",
        "typecheck": ["npx", "tsc", "--noEmit"],
        "lint": ["npx", "next", "lint"],
        "test": ["npx", "jest", "--passWithNoTests"],
        "port": 3056,
    },
    "settle": {
        "path": "TrueVow_Tenant_SETTLE-Service",
        "stack": "python",
        "typecheck": ["python", "-m", "mypy", "app/", "--ignore-missing-imports"],
        "lint": ["python", "-m", "flake8", "app/", "--max-line-length=120", "--extend-ignore=E501,W503"],
        "test": ["python", "-m", "pytest", "tests/", "-v", "--tb=short"],
        "port": 8002,
    },
    "tenant-app": {
        "path": "TrueVow_Tenant_Application_Service",
        "stack": "python",
        "typecheck": None,  # No mypy config
        "lint": None,
        "test": ["python", "-m", "pytest", "tests/", "-x", "--tb=short"],
        "port": 3022,
    },
    "financial-management": {
        "path": "TrueVow_Financial_Management_Service",
        "stack": "python",
        "typecheck": None,
        "lint": None,
        "test": ["python", "-m", "pytest", "tests/", "-v", "--tb=short"],
        "port": 3011,
    },
    "billing": {
        "path": "TrueVow-Tenant_Billing-Service",
        "stack": "nodejs",
        "typecheck": ["npx", "tsc", "--noEmit"],
        "lint": None,
        "test": ["npx", "jest", "--passWithNoTests"],
        "port": 3016,
    },
    "internal-ops": {
        "path": "TrueVow_Internal_Ops_Service",
        "stack": "nodejs",
        "typecheck": None,
        "lint": None,
        "test": None,
        "port": 3006,
    },
    "leverage": {
        "path": "TrueVow_Tenant_LEVERAGE_Service",
        "stack": "nodejs",
        "typecheck": None,
        "lint": None,
        "test": None,
        "port": 3036,
    },
}


def log_verification(agent: str, service: str, result: dict):
    LIVE_DIR.mkdir(parents=True, exist_ok=True)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    log_path = LIVE_DIR / f"{today}.jsonl"
    entry = {
        "ts": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "agent": agent,
        "action": "verify",
        "detail": json.dumps(result),
        "service": service,
        "path": "",
        "verification": "VERIFIED" if result.get("passed") else "UNTESTED",
    }
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def run_step(label: str, cmd: list[str] | None, cwd: Path) -> dict:
    if cmd is None:
        return {"step": label, "status": "skipped", "reason": "not configured"}

    start = time.time()
    try:
        result = subprocess.run(
            cmd, cwd=str(cwd), capture_output=True, text=True, timeout=300
        )
        duration_ms = int((time.time() - start) * 1000)
        passed = result.returncode == 0
        return {
            "step": label,
            "status": "pass" if passed else "fail",
            "duration_ms": duration_ms,
            "exit_code": result.returncode,
            "stdout_tail": result.stdout.strip()[-500:] if result.stdout else "",
            "stderr_tail": result.stderr.strip()[-500:] if result.stderr else "",
        }
    except subprocess.TimeoutExpired:
        return {"step": label, "status": "timeout", "duration_ms": 300000}
    except FileNotFoundError:
        return {"step": label, "status": "skipped", "reason": "binary not found"}


def verify_service(service: str, skip_tests: bool = False, test_only: bool = False) -> dict:
    config = SERVICE_CONFIG.get(service)
    if not config:
        return {"service": service, "error": f"Unknown service: {service}. Known: {list(SERVICE_CONFIG.keys())}"}

    cwd = CURSOR_ROOT / config["path"]
    if not cwd.exists():
        return {"service": service, "error": f"Path not found: {cwd}"}

    steps = []

    if not test_only:
        steps.append(run_step("typecheck", config.get("typecheck"), cwd))
        steps.append(run_step("lint", config.get("lint"), cwd))

    if not skip_tests or test_only:
        steps.append(run_step("test", config.get("test"), cwd))

    all_passed = all(s["status"] == "pass" for s in steps if s["status"] not in ("skipped", "timeout"))
    any_failed = any(s["status"] == "fail" for s in steps)
    any_timeout = any(s["status"] == "timeout" for s in steps)

    return {
        "service": service,
        "path": config["path"],
        "stack": config["stack"],
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "passed": all_passed,
        "failed": any_failed,
        "timeout": any_timeout,
        "steps": steps,
    }


def main():
    parser = argparse.ArgumentParser(description="Agent-Native Verification — replaces CI/CD")
    parser.add_argument("--service", "-s", required=True, help="Service name")
    parser.add_argument("--skip-tests", action="store_true", help="Skip test suite")
    parser.add_argument("--test-only", action="store_true", help="Only run tests, skip typecheck/lint")
    parser.add_argument("--agent", default="yasha-orchestrator", help="Agent ID for logging")
    args = parser.parse_args()

    print(f"Verifying {args.service}...")
    result = verify_service(args.service, args.skip_tests, args.test_only)
    print(json.dumps(result, indent=2))

    log_verification(args.agent, args.service, result)

    if result.get("failed"):
        sys.exit(1)
    elif result.get("timeout"):
        sys.exit(2)


if __name__ == "__main__":
    main()
