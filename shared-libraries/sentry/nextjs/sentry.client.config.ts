// TrueVow Shared Sentry SDK — Next.js
// Drop-in error tracking for all Next.js services (Portal, Sales Ops, CS CORE, FM frontend)

// sentry.client.config.ts
// Place in your service root. Imported by next.config.ts and instrumentation.ts.

import * as Sentry from "@sentry/nextjs";

Sentry.init({
  dsn: process.env.NEXT_PUBLIC_SENTRY_DSN || process.env.SENTRY_DSN,
  environment: process.env.NEXT_PUBLIC_SENTRY_ENVIRONMENT || process.env.NODE_ENV || "development",
  tracesSampleRate: 0.05,
  replaysSessionSampleRate: process.env.NODE_ENV === "production" ? 0.1 : 0,
  replaysOnErrorSampleRate: 1.0,
  integrations: [
    Sentry.replayIntegration({
      maskAllText: true,
      blockAllMedia: true,
    }),
    Sentry.browserTracingIntegration(),
  ],
  beforeSend(event) {
    // Strip PII — never send names, emails, phone numbers
    if (event.request?.cookies) delete event.request.cookies;
    return event;
  },
});
