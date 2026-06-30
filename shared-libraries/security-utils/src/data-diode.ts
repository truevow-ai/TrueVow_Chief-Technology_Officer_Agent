/**
 * Data Diode Primitives (Shared Library)
 * Reusable one-way data flow enforcement for all TrueVow services.
 */

/** Maximum response sizes per trust level */
export const TRUST_LEVEL_SIZE_LIMITS = {
  high: 10 * 1024 * 1024,    // 10 MB
  medium: 256 * 1024,         // 256 KB
  low: 64 * 1024,             // 64 KB
  external: 1 * 1024 * 1024,  // 1 MB
} as const;

export type TrustLevel = keyof typeof TRUST_LEVEL_SIZE_LIMITS;

/** Sensitive field names that should be stripped from responses */
const SENSITIVE_FIELDS = new Set([
  'ssn', 'social_security', 'tax_id', 'ein',
  'bank_account', 'routing_number', 'credit_card',
  'date_of_birth', 'dob', 'drivers_license',
  'passport_number', 'home_address', 'personal_email',
  'personal_phone', 'salary', 'compensation',
  'api_keys', 'webhook_secrets', 'encryption_keys',
]);

export interface DiodeCheckResult {
  allowed: boolean;
  violations: string[];
}

/**
 * Check if a response size is within limits for the given trust level.
 */
export function checkResponseSize(
  bodyBytes: number,
  trustLevel: TrustLevel,
): DiodeCheckResult {
  const limit = TRUST_LEVEL_SIZE_LIMITS[trustLevel];
  if (bodyBytes > limit) {
    return {
      allowed: false,
      violations: [`Response size ${bodyBytes} exceeds limit ${limit} for trust level ${trustLevel}`],
    };
  }
  return { allowed: true, violations: [] };
}

/**
 * Strip sensitive fields from an object based on trust level.
 */
export function stripFields<T>(data: T, trustLevel: TrustLevel): T {
  if (trustLevel === 'high') return data; // Full trust = no stripping
  if (data === null || data === undefined || typeof data !== 'object') return data;

  if (Array.isArray(data)) {
    return data.map(item => stripFields(item, trustLevel)) as unknown as T;
  }

  const result: Record<string, unknown> = {};
  for (const [key, value] of Object.entries(data as Record<string, unknown>)) {
    if (SENSITIVE_FIELDS.has(key.toLowerCase())) {
      result[key] = '[REDACTED]';
      continue;
    }
    result[key] = typeof value === 'object' && value !== null
      ? stripFields(value, trustLevel)
      : value;
  }
  return result as T;
}

/**
 * Simple sliding-window rate limiter.
 */
export class RateLimiter {
  private buckets = new Map<string, { count: number; windowStart: number }>();

  constructor(private windowMs: number = 60_000) {}

  check(key: string, limit: number): { allowed: boolean; remaining: number } {
    const now = Date.now();
    let bucket = this.buckets.get(key);

    if (!bucket || now - bucket.windowStart >= this.windowMs) {
      bucket = { count: 0, windowStart: now };
      this.buckets.set(key, bucket);
    }

    bucket.count++;
    const remaining = Math.max(0, limit - bucket.count);
    return { allowed: bucket.count <= limit, remaining };
  }

  reset(key: string): void {
    this.buckets.delete(key);
  }
}
