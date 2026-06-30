#!/usr/bin/env python3
"""
Agent Onboarding Tool — Wires any service into the ecosystem.
Creates/updates AGENTS.md and .opencode/skills/ for a target service.

Usage:
  python TrueVow_Shared_Orchestration/setup-agent.py <service-path>
  python TrueVow_Shared_Orchestration/setup-agent.py TrueVow_Customer_Success_CORE_Service
  python TrueVow_Shared_Orchestration/setup-agent.py --all   ← wire ALL services
  python TrueVow_Shared_Orchestration/setup-agent.py --dry-run   ← show what would happen
  python TrueVow_Shared_Orchestration/setup-agent.py --status   ← show wiring status of all services
"""

import sys
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent.parent
ONBOARDING_PREAMBLE = (Path(__file__).parent / "agent-onboarding.md").read_text(encoding="utf-8")

SERVICES = [
    "TrueVow_Customer_Success_CORE_Service",
    "TrueVow_Dialogflow_Intake_Service",
    "TrueVow_Documentation",
    "TrueVow_Financial_Management_Service",
    "TrueVow_First_Line_Support_Service",
    "TrueVow_Internal_Ops_Service",
    "TrueVow_Platform_Analytics_Service",
    "TrueVow_SaaS_Administration_Service",
    "TrueVow_Sales_Ops_Service",
    "TrueVow_Tenant_Application_Service",
    "Truevow_Tenant_Customer_Portal_Service",
    "TrueVow_Tenant_LEVERAGE_Service",
    "TrueVow_Tenant_SETTLE-Service",
    "TrueVow_Tenant_VERIFY_Service",
    "TrueVow_TWIML_SoftPhone_App",
    "TrueVow-Tenant_Billing-Service",
    "TrueVow-Documentation",
    "truevow_test_cartesia_voice_agent_usa",
]

ARCHIVED = [
    "TrueVow_Tenant_CONNECT_Service",  # Decommissioned June 2026
]


def wire_service(service_path: str, dry_run: bool = False):
    """Wire a single service into the ecosystem."""
    svc_dir = ROOT / service_path
    if not svc_dir.exists():
        print(f"  [MISSING] {service_path} — directory not found")
        return False

    agents_md = svc_dir / "AGENTS.md"
    existing = agents_md.exists()

    if dry_run:
        action = "UPDATE" if existing else "CREATE"
        print(f"  [{action:6s}] {service_path}/AGENTS.md")
        return True

    # If AGENTS.md exists, prepend ecosystem preamble
    if existing:
        current = agents_md.read_text(encoding="utf-8", errors="replace")
        if "Ecosystem Integration" in current:
            print(f"  [WIRED  ] {service_path} — already connected")
            return True
        # Prepend onboarding
        new_content = ONBOARDING_PREAMBLE + "\n\n---\n\n" + current
        agents_md.write_text(new_content, encoding="utf-8")
        print(f"  [WIRED  ] {service_path} — AGENTS.md updated with ecosystem preamble")
    else:
        # Create fresh AGENTS.md
        content = f"""# {service_path} — Agent Rules

{ONBOARDING_PREAMBLE}

---

## Service-Specific Rules

> Add service-specific rules below. The ecosystem preamble above is auto-generated
> and wires this agent into the TrueVow Agent Ecosystem.
"""
        agents_md.write_text(content, encoding="utf-8")
        print(f"  [WIRED  ] {service_path} — AGENTS.md created")

    return True


def show_status():
    """Show wiring status of all services."""
    print("\n=== Service Wiring Status ===\n")
    wired = 0
    aware = 0
    blind = 0
    for svc in SERVICES:
        svc_dir = ROOT / svc
        if not svc_dir.exists():
            continue
        agents_md = svc_dir / "AGENTS.md"
        has_opencode = (svc_dir / ".opencode").exists()
        has_cursor = (svc_dir / ".cursor").exists()
        has_cursor_rules = (svc_dir / ".cursorrules").exists()
        has_ocjson = (svc_dir / "opencode.json").exists()
        has_any_config = any([has_opencode, has_cursor, has_cursor_rules, has_ocjson])

        if agents_md.exists():
            content = agents_md.read_text(encoding="utf-8", errors="replace")
            is_wired = "Ecosystem Integration" in content
            if is_wired:
                icons = "[W]"
                wired += 1
            else:
                icons = "[A]"
                aware += 1
        else:
            icons = "[ ]" if has_any_config else "   "
            blind += 1

        configs = []
        if has_opencode: configs.append("opencode")
        if has_cursor_rules: configs.append("cursorrules")
        if has_cursor: configs.append("cursor/")
        if has_ocjson: configs.append("oc.json")
        cfg_str = f" [{', '.join(configs)}]" if configs else ""

        print(f"  {icons} {svc}{cfg_str}")

    print(f"\n  [W] = Wired  |  [A] = Has AGENTS.md (not wired)  |  [ ] = Has agent configs only")
    print(f"  Wired: {wired}  |  Aware: {aware}  |  Blind: {blind}  |  Total: {wired + aware + blind}")


def main():
    if "--status" in sys.argv:
        show_status()
        return

    if "--dry-run" in sys.argv:
        print("\n=== DRY RUN — no changes will be made ===\n")
        for svc in SERVICES:
            wire_service(svc, dry_run=True)
        print("\nRun without --dry-run to apply.")
        return

    if "--all" in sys.argv:
        print("\n=== Wiring ALL services to ecosystem ===\n")
        for svc in SERVICES:
            wire_service(svc)
        print("\nDone. Run 'python TrueVow_Shared_Orchestration/orchestrator.py list' to verify.")
        return

    if len(sys.argv) > 1 and sys.argv[1] not in ("--all", "--status", "--dry-run"):
        wire_service(sys.argv[1])
        return

    print("Usage:")
    print("  python TrueVow_Shared_Orchestration/setup-agent.py <service-path>")
    print("  python TrueVow_Shared_Orchestration/setup-agent.py --all")
    print("  python TrueVow_Shared_Orchestration/setup-agent.py --dry-run")
    print("  python TrueVow_Shared_Orchestration/setup-agent.py --status")


if __name__ == "__main__":
    main()
