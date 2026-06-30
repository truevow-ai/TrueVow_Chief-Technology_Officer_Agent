"""
TrueVow Shared Observability SDK — OpenTelemetry
Drop-in instrumentation for ALL Python services.
Sends traces + metrics to SigNoz, errors to Sentry.
One interface. All services.

Install: pip install opentelemetry-api opentelemetry-sdk opentelemetry-instrumentation-fastapi opentelemetry-instrumentation-sqlalchemy opentelemetry-instrumentation-httpx opentelemetry-exporter-otlp
Setup:   from app.shared.otel_init import init_observability; init_observability(app, "service-name")
"""

import os
import logging
from opentelemetry import trace, metrics
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.sdk.resources import SERVICE_NAME, DEPLOYMENT_ENVIRONMENT, Resource
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor
from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor
from opentelemetry.instrumentation.logging import LoggingInstrumentor

logger = logging.getLogger(__name__)


def init_observability(
    app=None,
    service_name: str = None,
    otlp_endpoint: str = None,
    environment: str = None,
    enable_logs: bool = True,
    enable_metrics: bool = True,
    enable_traces: bool = True,
):
    """
    Initialize OpenTelemetry for a service.
    Traces + metrics -> SigNoz OTLP collector.
    Errors -> Sentry (via sentry_init.py, installed separately).

    Args:
        app: FastAPI app instance (optional but recommended)
        service_name: e.g. 'intake-service', 'fm-service'
        otlp_endpoint: SigNoz OTLP collector (default: localhost:4317)
        environment: production/staging/development
    """
    otlp = otlp_endpoint or os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT", "http://localhost:4317")
    svc = service_name or os.getenv("OTEL_SERVICE_NAME", os.getenv("SERVICE_NAME", "unknown"))
    env = environment or os.getenv("OTEL_RESOURCE_ATTRIBUTES_ENVIRONMENT", os.getenv("ENV", "development"))

    resource = Resource(attributes={
        SERVICE_NAME: svc,
        DEPLOYMENT_ENVIRONMENT: env,
    })

    # --- Traces ---
    if enable_traces:
        provider = TracerProvider(resource=resource)
        try:
            otlp_exporter = OTLPSpanExporter(endpoint=otlp, insecure=True)
            provider.add_span_processor(BatchSpanProcessor(otlp_exporter))
        except Exception as e:
            logger.warning(f"[OTEL] Trace exporter unavailable ({e}) — traces disabled")
        trace.set_tracer_provider(provider)

    # --- Metrics ---
    if enable_metrics:
        try:
            metric_reader = PeriodicExportingMetricReader(
                OTLPMetricExporter(endpoint=otlp, insecure=True),
                export_interval_millis=30000
            )
            meter_provider = MeterProvider(resource=resource, metric_readers=[metric_reader])
            metrics.set_meter_provider(meter_provider)
        except Exception as e:
            logger.warning(f"[OTEL] Metric exporter unavailable ({e}) — metrics disabled")

    # --- Auto-instrumentation ---
    if app and enable_traces:
        FastAPIInstrumentor.instrument_app(app, excluded_urls="/health,/metrics,/")

    try:
        SQLAlchemyInstrumentor().instrument(enable_commenter=True)
    except Exception:
        pass

    try:
        HTTPXClientInstrumentor().instrument()
    except Exception:
        pass

    # --- Log correlation ---
    if enable_logs:
        LoggingInstrumentor().instrument(set_logging_format=True)

    logger.info(f"[OTEL] Service='{svc}' env='{env}' otlp='{otlp}'")
    return True
