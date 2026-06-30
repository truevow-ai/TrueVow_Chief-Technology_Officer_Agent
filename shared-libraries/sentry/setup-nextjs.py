#!/usr/bin/env python3
"""
Sentry SDK Installer for Next.js services.
Drops Sentry config files into any Next.js service.

Usage:
  python shared-libraries/sentry/setup-nextjs.py TrueVow_Sales_Ops_Service
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
CLIENT_CONFIG = Path(__file__).resolve().parent / "nextjs" / "sentry.client.config.ts"
SERVER_CONFIG = Path(__file__).resolve().parent / "nextjs" / "sentry.server.config.ts"


def setup_service(service_name: str):
    svc_dir = ROOT / service_name
    if not svc_dir.exists():
        print(f"[ERROR] Service not found: {service_name}")
        return

    # 1. Copy config files
    sentry_dir = svc_dir / "sentry"
    sentry_dir.mkdir(parents=True, exist_ok=True)
    dest_client = sentry_dir / "sentry.client.config.ts"
    dest_server = sentry_dir / "sentry.server.config.ts"
    if not dest_client.exists():
        dest_client.write_text(CLIENT_CONFIG.read_text(encoding="utf-8"))
        print(f"[1/2] Created sentry.client.config.ts")
    if not dest_server.exists():
        dest_server.write_text(SERVER_CONFIG.read_text(encoding="utf-8"))
        print(f"[1/2] Created sentry.server.config.ts")

    # 2. Add DSN to .env.local
    env_file = svc_dir / ".env.local"
    if env_file.exists():
        content = env_file.read_text(encoding="utf-8", errors="replace")
        if "SENTRY_DSN" not in content:
            with open(env_file, "a", encoding="utf-8") as f:
                f.write("\n# Sentry Error Tracking\n# SENTRY_DSN=<add-your-dsn>\n# NEXT_PUBLIC_SENTRY_DSN=<same-dsn>\nSENTRY_ENVIRONMENT=development\n")
            print(f"[2/2] Added SENTRY_DSN to .env.local")
        else:
            print(f"[2/2] SENTRY_DSN already present")
    print(f"  Run: npm install @sentry/nextjs")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python shared-libraries/sentry/setup-nextjs.py <service-name>")
        sys.exit(1)
    setup_service(sys.argv[1])
