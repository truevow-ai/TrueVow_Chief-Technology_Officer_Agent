---
category: architecture
title: "Unified Observability Stack - SigNoz + Sentry + OpenTelemetry"
importance: 10
tags: ["observability", "opentelemetry", "signoz", "sentry", "otel", "traces", "metrics", "logs", "unified", "dashboard"]
file_paths: []
created: 2026-06-25T03:06:45.778868+00:00
updated: 2026-06-25T03:06:45.778868+00:00
memory_id: 7aab7334-a709-42d5-8b50-4fa7d59f1d8e
---

# Unified Observability Stack - SigNoz + Sentry + OpenTelemetry

Platform-wide observability implemented: OPEN TELEMETRY SDK installed in ALL 11 application services (8 Python + 3 Next.js). SIGNOZ as the central backend (logs + traces + metrics, OpenTelemetry native, self-hosted, docker-compose based). SENTRY for error tracking (installed separately, complements SigNoz). ARCHITECTURE: Each service runs OTEL SDK auto-instrumentation (FastAPI, SQLAlchemy, HTTPX, logging for Python; Node auto-instrumentation for Next.js). OTEL exporters send data to SigNoz OTLP Collector (gRPC port 4317 for Python, HTTP port 4318 for Next.js). SigNoz stores in ClickHouse and displays via Query Service + Frontend UI (port 3301). ONE INTERFACE: SigNoz dashboard at localhost:3301 shows all traces, metrics, logs across all services. Sentry dashboard shows errors. docker-compose at shared-libraries/observability/docker-compose.yml. All open-source, zero vendor lock-in.

---
**Category:** `architecture` | **Importance:** 10/10
**Files:** N/A
