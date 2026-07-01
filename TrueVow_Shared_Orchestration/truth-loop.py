#!/usr/bin/env python3
"""
Self-Healing Truth Loop — Automated RED→GREEN→REFACTOR cycle.

Runs truth commands for a service. On failure:
1. Captures error output
2. Auto-dispatches to debugging-and-error-recovery skill
3. Applies fix
4. Re-runs truth commands
5. Repeats until GREEN or max attempts exhausted

Usage:
  python truth-loop.py <service-name>
  python truth-loop.py TrueVow_Financial_Management_Service --max-attempts 3
"""

import subprocess
import sys
import yaml
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "TrueVow_Shared_Orchestration" / "config.yaml"


def load_config():
    return yaml.safe_load(CONFIG.read_text(encoding="utf-8"))


def run_truth_commands(service_name: str, service_cfg: dict) -> list[dict]:
    """Run truth commands for a service. Returns list of {command, exit_code, output, passed}."""
    svc_path = ROOT / service_cfg["path"]
    truth = service_cfg.get("truth_commands", {})

    if not truth:
        return []

    results = []
    cwd = str(svc_path)

    # Run backend commands
    for cmd in truth.get("backend", []):
        r = subprocess.run(
            cmd, shell=True, cwd=cwd,
            capture_output=True, text=True, timeout=120
        )
        results.append({
            "command": cmd,
            "exit_code": r.returncode,
            "output": (r.stdout + r.stderr)[-2000:],
            "passed": r.returncode == 0,
        })

    # Run frontend commands
    for cmd in truth.get("frontend", []):
        r = subprocess.run(
            cmd, shell=True, cwd=cwd,
            capture_output=True, text=True, timeout=120
        )
        results.append({
            "command": cmd,
            "exit_code": r.returncode,
            "output": (r.stdout + r.stderr)[-2000:],
            "passed": r.returncode == 0,
        })

    return results


def truth_loop(service_name: str, max_attempts: int = 3):
    """Run truth-loop for a service until all commands pass or max attempts reached."""
    cfg = load_config()
    services = cfg.get("services", {})

    if service_name not in services:
        print(f"Service '{service_name}' not found in config.yaml")
        return

    svc = services[service_name]
    if svc.get("status") in ("archived", "replaced"):
        print(f"Service '{service_name}' is {svc.get('status')} — skipping.")
        return

    print(f"\n=== SELF-HEALING TRUTH LOOP: {service_name} ===")
    print(f"Max attempts: {max_attempts}")
    print(f"Started: {datetime.now().isoformat()}\n")

    for attempt in range(1, max_attempts + 1):
        print(f"--- Attempt {attempt}/{max_attempts} ---")
        results = run_truth_commands(service_name, svc)

        passed = [r for r in results if r["passed"]]
        failed = [r for r in results if not r["passed"]]

        print(f"  Passed: {len(passed)}/{len(results)}")

        if not failed:
            print(f"\n=== ALL GREEN ({attempt} attempt(s)) ===")
            print(f"Finished: {datetime.now().isoformat()}")
            return {"result": "GREEN", "attempts": attempt, "total_commands": len(results)}

        # Show failures
        for f in failed:
            print(f"\n  FAILED: {f['command']}")
            print(f"  Exit code: {f['exit_code']}")
            # Show last 20 lines of output
            lines = f["output"].strip().split("\n")
            for line in lines[-20:]:
                print(f"    {line[:200]}")

        if attempt < max_attempts:
            print(f"\n  [AUTO-FIX] Dispatching to debugging-and-error-recovery...")
            # Build dispatch request with the error details
            error_summary = "\n".join([
                f"{f['command']}: exit={f['exit_code']}\n{f['output'][:500]}"
                for f in failed
            ])
            dispatch_request = f"debug and fix these failing truth commands in {service_name}: {error_summary[:300]}"

            r = subprocess.run(
                [sys.executable, str(ROOT / "TrueVow_Shared_Orchestration" / "orchestrator.py"),
                 "dispatch", dispatch_request],
                capture_output=True, text=True, timeout=60, cwd=str(ROOT)
            )
            print(f"  Dispatched. Running truth commands again...")

    print(f"\n=== STILL FAILING after {max_attempts} attempts ===")
    print(f"Finished: {datetime.now().isoformat()}")
    return {"result": "FAILED", "attempts": max_attempts, "remaining_failures": len(failed)}


def truth_loop_all(max_attempts: int = 2):
    """Run truth-loop on all active services."""
    cfg = load_config()
    services = cfg.get("services", {})
    active = {k: v for k, v in services.items() if v.get("status") not in ("archived", "replaced")}

    results = {}
    for name, svc in active.items():
        if not svc.get("truth_commands"):
            continue
        print(f"\n{'='*60}")
        result = truth_loop(name, max_attempts=max_attempts)
        results[name] = result

    print(f"\n{'='*60}")
    print("=== LOOP SUMMARY ===")
    green = sum(1 for r in results.values() if r and r.get("result") == "GREEN")
    failed = sum(1 for r in results.values() if r and r.get("result") == "FAILED")
    print(f"GREEN: {green}  |  FAILED: {failed}  |  TOTAL: {len(results)}")
    return results


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        print("Usage: python truth-loop.py <service-name> [--max-attempts N] [--all]")
        sys.exit(0)

    max_attempts = 3
    args = sys.argv[1:]
    service_name = args[0]
    i = 1
    while i < len(args):
        if args[i] == "--max-attempts" and i + 1 < len(args):
            max_attempts = int(args[i + 1]); i += 2
        else:
            i += 1

    if service_name == "--all":
        truth_loop_all(max_attempts=max_attempts)
    else:
        truth_loop(service_name, max_attempts=max_attempts)
