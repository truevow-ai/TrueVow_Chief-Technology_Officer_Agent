---
category: architecture
title: "Observability Stack LIVE - Jaeger + OTEL + Sentry"
importance: 10
tags: ["observability", "jaeger", "otel", "visualization", "live", "tracing", "dashboard"]
file_paths: []
created: 2026-06-25T03:29:32.605981+00:00
updated: 2026-06-25T03:29:32.605981+00:00
memory_id: 25608f4b-9668-443b-b362-8ce12e3c63ed
---

# Observability Stack LIVE - Jaeger + OTEL + Sentry

Visualization stack operational: JAEGER All-in-One at http://localhost:16686 (trace visualization UI, in-memory storage). OpenTelemetry Collector at localhost:4317-4318 (receives traces from all 11 services, forwards to Jaeger). SENTRY for error tracking (DSN pending per-service). ARCHITECTURE: Services -> OTEL SDK -> OTLP gRPC/HTTP -> OTEL Collector -> Jaeger. Docker compose at shared-libraries/observability/docker-compose.yml. Two containers: truevow-jaeger + truevow-otel-collector.

---
**Category:** `architecture` | **Importance:** 10/10
**Files:** N/A
