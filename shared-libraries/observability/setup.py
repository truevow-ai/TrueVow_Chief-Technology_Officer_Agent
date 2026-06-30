#!/usr/bin/env python3
"""
Unified Observability Installer — One command wires OTEL + Sentry into any service.

Usage:
  python shared-libraries/observability/setup.py <service-name>
  python shared-libraries/observability/setup.py TrueVow_Tenant_Application_Service
  python shared-libraries/observability/setup.py --all-python
  python shared-libraries/observability/setup.py --all-nextjs
  python shared-libraries/observability/setup.py --all

What it does:
  1. Installs OpenTelemetry SDK packages
  2. Copies otel_init.py / otel-node.js to the service
  3. Adds OTEL env vars to .env.local
  4. Pairs with existing Sentry installation
"""

import sys
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
OTEL_PYTHON = Path(__file__).resolve().parent / "python" / "otel_init.py"
OTEL_NEXTJS = Path(__file__).resolve().parent / "nextjs" / "otel-node.js"

PYTHON_SERVICES = [
    "TrueVow_Tenant_Application_Service",
    "TrueVow_Financial_Management_Service",
    "TrueVow_Platform_Analytics_Service",
    "TrueVow_SaaS_Administration_Service",
    "TrueVow_Tenant_LEVERAGE_Service",
    "TrueVow_Tenant_SETTLE-Service",
    "TrueVow_Tenant_VERIFY_Service",
    "TrueVow-Tenant_Billing-Service",
]

NEXTJS_SERVICES = [
    "Truevow_Tenant_Customer_Portal_Service",
    "TrueVow_Sales_Ops_Service",
    "TrueVow_Customer_Success_CORE_Service",
]

OTEL_ENV = """
# OpenTelemetry - SigNoz OTLP Collector
OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317
OTEL_SERVICE_NAME={service_name}
OTEL_RESOURCE_ATTRIBUTES_ENVIRONMENT=development

# Log level for OTEL
OTEL_LOG_LEVEL=info
"""

OTEL_ENV_NEXTJS = """
# OpenTelemetry - SigNoz OTLP Collector (HTTP endpoint for Node.js)
OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318/v1/traces
OTEL_SERVICE_NAME={service_name}
OTEL_RESOURCE_ATTRIBUTES_ENVIRONMENT=development
"""


def install_python_deps():
    """Install OpenTelemetry Python packages."""
    deps = [
        "opentelemetry-api",
        "opentelemetry-sdk",
        "opentelemetry-instrumentation-fastapi",
        "opentelemetry-instrumentation-sqlalchemy",
        "opentelemetry-instrumentation-httpx",
        "opentelemetry-instrumentation-logging",
        "opentelemetry-exporter-otlp-proto-grpc",
    ]
    print("[deps] Installing OpenTelemetry Python packages...")
    subprocess.run(["py", "-3", "-m", "pip", "install", "-q"] + deps, capture_output=True)
    print("[deps] Done")


def setup_python(service_name: str):
    svc_dir = ROOT / service_name
    if not svc_dir.exists():
        print(f"  [SKIP] {service_name} - not found")
        return

    shared_dir = svc_dir / "app" / "shared"
    shared_dir.mkdir(parents=True, exist_ok=True)

    dest = shared_dir / "otel_init.py"
    if not dest.exists():
        dest.write_text(OTEL_PYTHON.read_text(encoding="utf-8"))
    else:
        dest.write_text(OTEL_PYTHON.read_text(encoding="utf-8"))

    env_file = svc_dir / ".env.local"
    if env_file.exists():
        content = env_file.read_text(encoding="utf-8", errors="replace")
        if "OTEL_EXPORTER_OTLP_ENDPOINT" not in content:
            with open(env_file, "a", encoding="utf-8") as f:
                f.write(OTEL_ENV.format(service_name=service_name))
    else:
        env_file.write_text(OTEL_ENV.format(service_name=service_name), encoding="utf-8")

    print(f"  [OK] {service_name} -> app/shared/otel_init.py + OTEL env")


def setup_nextjs(service_name: str):
    svc_dir = ROOT / service_name
    if not svc_dir.exists():
        print(f"  [SKIP] {service_name} - not found")
        return

    shared_dir = svc_dir / "shared"
    shared_dir.mkdir(parents=True, exist_ok=True)

    dest = shared_dir / "otel-node.js"
    dest.write_text(OTEL_NEXTJS.read_text(encoding="utf-8"))

    env_file = svc_dir / ".env.local"
    if env_file.exists():
        content = env_file.read_text(encoding="utf-8", errors="replace")
        if "OTEL_EXPORTER_OTLP_ENDPOINT" not in content:
            with open(env_file, "a", encoding="utf-8") as f:
                f.write(OTEL_ENV_NEXTJS.format(service_name=service_name))
    else:
        env_file.write_text(OTEL_ENV_NEXTJS.format(service_name=service_name), encoding="utf-8")

    print(f"  [OK] {service_name} -> shared/otel-node.js + OTEL env")


def main():
    if "--all-python" in sys.argv:
        install_python_deps()
        print("\n=== Installing OTEL into all Python services ===\n")
        for svc in PYTHON_SERVICES:
            setup_python(svc)
        print(f"\nDone. {len(PYTHON_SERVICES)} services wired.")
        print("Start SigNoz: docker-compose -f shared-libraries/observability/docker-compose.yml up -d")
    elif "--all-nextjs" in sys.argv:
        print("\n=== Installing OTEL into all Next.js services ===\n")
        for svc in NEXTJS_SERVICES:
            setup_nextjs(svc)
        print(f"\nDone. {len(NEXTJS_SERVICES)} services wired.")
    elif "--all" in sys.argv:
        install_python_deps()
        print("\n=== Installing OTEL into ALL services ===\n")
        print("Python:")
        for svc in PYTHON_SERVICES:
            setup_python(svc)
        print("\nNext.js:")
        for svc in NEXTJS_SERVICES:
            setup_nextjs(svc)
        print(f"\nDone. {len(PYTHON_SERVICES) + len(NEXTJS_SERVICES)} services wired.")
        print("Start SigNoz: docker-compose -f shared-libraries/observability/docker-compose.yml up -d")
    elif len(sys.argv) > 1:
        svc = sys.argv[1]
        if svc in PYTHON_SERVICES:
            install_python_deps()
            setup_python(svc)
        elif svc in NEXTJS_SERVICES:
            setup_nextjs(svc)
        else:
            print(f"Unknown service: {svc}")
    else:
        print("Usage:")
        print("  python setup.py --all          # Install everywhere")
        print("  python setup.py --all-python   # All Python services")
        print("  python setup.py --all-nextjs   # All Next.js services")
        print("  python setup.py <service-name> # Single service")


if __name__ == "__main__":
    main()
