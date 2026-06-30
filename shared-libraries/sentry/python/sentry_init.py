"""
TrueVow Shared Sentry SDK — Python (FastAPI)
Drop-in error tracking and performance monitoring for all Python services.

Usage:
  from shared_libraries.sentry import init_sentry
  init_sentry(app, dsn=os.getenv("SENTRY_DSN"))

Install:
  pip install sentry-sdk
  cp shared-libraries/sentry/python/sentry_init.py <service>/shared/
"""

import os
import sentry_sdk
from sentry_sdk.integrations.fastapi import FastApiIntegration
from sentry_sdk.integrations.starlette import StarletteIntegration
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration


def init_sentry(app=None, dsn: str = None, environment: str = None, traces_sample_rate: float = 0.1):
    """
    Initialize Sentry for a FastAPI service.
    Call this once at app startup, before any routes.

    Args:
        app: FastAPI app instance (optional, for performance tracing)
        dsn: Sentry DSN (defaults to SENTRY_DSN env var)
        environment: production/staging/development (defaults to ENV or SENTRY_ENVIRONMENT)
        traces_sample_rate: 0.0 to 1.0 (default 0.1 = 10% of transactions)
    """
    sentry_dsn = dsn or os.getenv("SENTRY_DSN")
    if not sentry_dsn:
        print("[Sentry] WARNING: SENTRY_DSN not set — error tracking disabled")
        return False

    sentry_env = environment or os.getenv("SENTRY_ENVIRONMENT", os.getenv("ENV", "development"))

    integrations = [
        StarletteIntegration(transaction_style="endpoint"),
        FastApiIntegration(transaction_style="endpoint"),
        SqlalchemyIntegration(),
    ]

    sentry_sdk.init(
        dsn=sentry_dsn,
        environment=sentry_env,
        traces_sample_rate=traces_sample_rate,
        integrations=integrations,
        send_default_pii=False,
        max_breadcrumbs=100,
    )

    if app:
        @app.middleware("http")
        async def sentry_transaction_middleware(request, call_next):
            with sentry_sdk.start_transaction(name=f"{request.method} {request.url.path}"):
                response = await call_next(request)
                return response

    print(f"[Sentry] Initialized — env={sentry_env}, traces={traces_sample_rate}")
    return True


def capture_exception(exception, extras: dict = None):
    """Manual error capture with context."""
    with sentry_sdk.push_scope() as scope:
        if extras:
            for key, value in extras.items():
                scope.set_extra(key, value)
        sentry_sdk.capture_exception(exception)


def set_user(user_id: str, tenant_id: str = None, email: str = None):
    """Tag Sentry events with the current user context."""
    sentry_sdk.set_user({
        "id": user_id,
        "tenant_id": tenant_id,
        "email": email,
    })


def capture_message(message: str, level: str = "info"):
    """Log a message to Sentry."""
    sentry_sdk.capture_message(message, level=level)
