#!/usr/bin/env python3
"""
Sentry SDK Installer â€” Drops Sentry into any Python (FastAPI) service.

Usage:
  python shared-libraries/sentry/setup-python.py <service-path>
  python shared-libraries/sentry/setup-python.py TrueVow_Tenant_Application_Service

What it does:
  1. Installs sentry-sdk via pip
  2. Copies sentry_init.py to the service's shared/ directory
  3. Adds SENTRY_DSN to .env.local (if not present)
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
SENTRY_INIT = Path(__file__).resolve().parent / "python" / "sentry_init.py"


def setup_service(service_name: str):
    svc_dir = ROOT / service_name
    if not svc_dir.exists():
        print(f"[ERROR] Service not found: {service_name}")
        return

    app_dir = svc_dir / "app"
    env_file = svc_dir / ".env.local"

    # 1. Install sentry-sdk
    print(f"[1/4] Installing sentry-sdk for {service_name}...")
    import subprocess
    subprocess.run(["py", "-3", "-m", "pip", "install", "sentry-sdk"], capture_output=True)

    # 2. Copy sentry_init.py to service
    shared_dir = app_dir / "shared"
    shared_dir.mkdir(parents=True, exist_ok=True)
    dest = shared_dir / "sentry_init.py"
    if not dest.exists():
        dest.write_text(SENTRY_INIT.read_text(encoding="utf-8"))
        print(f"[2/4] Copied sentry_init.py -> {dest}")
    else:
        print(f"[2/4] sentry_init.py already exists, skipping")

    # 3. Add SENTRY_DSN to .env.local
    if env_file.exists():
        content = env_file.read_text(encoding="utf-8", errors="replace")
        if "SENTRY_DSN" not in content:
            with open(env_file, "a", encoding="utf-8") as f:
                f.write("\n# Sentry Error Tracking\n# SENTRY_DSN=<add-your-dsn>\nSENTRY_ENVIRONMENT=development\n")
            print(f"[3/4] Added SENTRY_DSN placeholder to .env.local")
        else:
            print(f"[3/4] SENTRY_DSN already in .env.local, skipping")
    else:
        print(f"[3/4] No .env.local found â€” create one with SENTRY_DSN=<your-dsn>")

    # 4. Print integration instructions
    print(f"[4/4] Integration instructions:")
    print(f"  In {service_name}/app/main.py, add:")
    print(f"    from app.shared.sentry_init import init_sentry")
    print(f"    init_sentry(app)")
    print()
    print(f"  In {service_name}/.env.local, set:")
    print(f"    SENTRY_DSN=<your-sentry-project-dsn>")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python shared-libraries/sentry/setup-python.py <service-name>")
        sys.exit(1)
    setup_service(sys.argv[1])

