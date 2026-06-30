// sentry.server.config.ts
// Server-side Sentry for Next.js API routes and SSR

import * as Sentry from "@sentry/nextjs";

Sentry.init({
  dsn: process.env.SENTRY_DSN,
  environment: process.env.SENTRY_ENVIRONMENT || process.env.NODE_ENV || "development",
  tracesSampleRate: 0.1,
  sendDefaultPii: false,
  maxBreadcrumbs: 100,
  beforeSend(event) {
    if (event.request?.cookies) delete event.request.cookies;
    return event;
  },
});
