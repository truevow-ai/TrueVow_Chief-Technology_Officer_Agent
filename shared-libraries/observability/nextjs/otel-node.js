// TrueVow Shared Observability SDK — OpenTelemetry for Next.js
// Auto-instruments all Next.js services. Traces -> SigNoz, Errors -> Sentry.

// next.config.ts snippet:
//   const { withOpenTelemetry } = require('./shared/otel-config');
//   module.exports = withOpenTelemetry({ ...yourNextConfig });

const opentelemetry = require('@opentelemetry/sdk-node');
const { getNodeAutoInstrumentations } = require('@opentelemetry/auto-instrumentations-node');
const { OTLPTraceExporter } = require('@opentelemetry/exporter-trace-otlp-http');
const { Resource } = require('@opentelemetry/resources');
const { SemanticResourceAttributes } = require('@opentelemetry/semantic-conventions');

const sdk = new opentelemetry.NodeSDK({
  resource: new Resource({
    [SemanticResourceAttributes.SERVICE_NAME]:
      process.env.OTEL_SERVICE_NAME || process.env.NEXT_PUBLIC_APP_NAME || 'unknown-nextjs',
    [SemanticResourceAttributes.DEPLOYMENT_ENVIRONMENT]:
      process.env.OTEL_RESOURCE_ATTRIBUTES_ENVIRONMENT || process.env.NODE_ENV || 'development',
  }),
  traceExporter: new OTLPTraceExporter({
    url: process.env.OTEL_EXPORTER_OTLP_ENDPOINT || 'http://localhost:4318/v1/traces',
  }),
  instrumentations: [getNodeAutoInstrumentations()],
});

sdk.start();
console.log('[OTEL] Next.js instrumentation started');

process.on('SIGTERM', () => {
  sdk.shutdown().then(() => console.log('[OTEL] Shutdown complete'));
});
