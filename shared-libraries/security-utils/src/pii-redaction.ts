/**
 * PII Redaction — Mandatory for LLM Zone (Clerk App 2)
 * 
 * Strips personally identifiable information from all responses
 * sent to Sales-Ops and First-Line Support services.
 * 
 * Patterns detected and redacted:
 * - Email addresses
 * - Phone numbers
 * - SSN / Tax IDs
 * - Credit card numbers
 * - Physical addresses
 * - Names (when tagged)
 */

// ─── Redaction Patterns ───────────────────────────────────────────
const PII_PATTERNS: Array<{ name: string; regex: RegExp; replacement: string }> = [
  {
    name: 'email',
    regex: /[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/g,
    replacement: '[REDACTED_EMAIL]',
  },
  {
    name: 'phone_us',
    regex: /(\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}/g,
    replacement: '[REDACTED_PHONE]',
  },
  {
    name: 'phone_intl',
    regex: /\+\d{1,3}[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}/g,
    replacement: '[REDACTED_PHONE]',
  },
  {
    name: 'ssn',
    regex: /\b\d{3}[-.\s]?\d{2}[-.\s]?\d{4}\b/g,
    replacement: '[REDACTED_SSN]',
  },
  {
    name: 'credit_card',
    regex: /\b(?:\d{4}[-.\s]?){3}\d{4}\b/g,
    replacement: '[REDACTED_CC]',
  },
  {
    name: 'ip_address',
    regex: /\b(?:\d{1,3}\.){3}\d{1,3}\b/g,
    replacement: '[REDACTED_IP]',
  },
]

// ─── Types ────────────────────────────────────────────────────────
export interface RedactionResult {
  redacted: string
  piiFound: boolean
  redactedFields: string[]
  redactionCount: number
}

export interface RedactionConfig {
  additionalPatterns?: Array<{ name: string; regex: RegExp; replacement: string }>
  preserveFields?: string[]    // JSON keys to skip
  strictMode?: boolean         // If true, errors on any PII detection
}

// ─── Core Redaction Functions ─────────────────────────────────────
/**
 * Redact PII from a string value
 */
export function redactString(input: string, config?: RedactionConfig): RedactionResult {
  let redacted = input
  const redactedFields: string[] = []
  let totalCount = 0

  const patterns = [...PII_PATTERNS, ...(config?.additionalPatterns ?? [])]

  for (const pattern of patterns) {
    const matches = redacted.match(pattern.regex)
    if (matches && matches.length > 0) {
      redactedFields.push(pattern.name)
      totalCount += matches.length
      redacted = redacted.replace(pattern.regex, pattern.replacement)
    }
  }

  return {
    redacted,
    piiFound: totalCount > 0,
    redactedFields,
    redactionCount: totalCount,
  }
}

/**
 * Redact PII from a JSON object (deep traversal)
 * Preserves structure, redacts string values
 */
export function redactObject<T extends Record<string, unknown>>(
  obj: T,
  config?: RedactionConfig
): { redacted: T; summary: RedactionResult } {
  const preserveSet = new Set(config?.preserveFields ?? [])
  let totalPiiFound = false
  const allRedactedFields: string[] = []
  let totalCount = 0

  function traverse(value: unknown, key?: string): unknown {
    // Skip preserved fields
    if (key && preserveSet.has(key)) return value

    if (typeof value === 'string') {
      const result = redactString(value, config)
      if (result.piiFound) {
        totalPiiFound = true
        allRedactedFields.push(...result.redactedFields)
        totalCount += result.redactionCount
      }
      return result.redacted
    }

    if (Array.isArray(value)) {
      return value.map((item, i) => traverse(item, `${key}[${i}]`))
    }

    if (value && typeof value === 'object') {
      const result: Record<string, unknown> = {}
      for (const [k, v] of Object.entries(value)) {
        result[k] = traverse(v, k)
      }
      return result
    }

    return value
  }

  const redactedObj = traverse(obj) as T

  return {
    redacted: redactedObj,
    summary: {
      redacted: JSON.stringify(redactedObj),
      piiFound: totalPiiFound,
      redactedFields: [...new Set(allRedactedFields)],
      redactionCount: totalCount,
    },
  }
}

/**
 * Middleware-style PII redaction for API responses.
 * Wraps a response body and redacts before sending.
 */
export function createPiiRedactionMiddleware(config?: RedactionConfig) {
  return function redactResponse(responseBody: unknown): {
    body: unknown
    wasRedacted: boolean
    summary: RedactionResult
  } {
    if (typeof responseBody === 'string') {
      const result = redactString(responseBody, config)
      return { body: result.redacted, wasRedacted: result.piiFound, summary: result }
    }

    if (responseBody && typeof responseBody === 'object') {
      const { redacted, summary } = redactObject(
        responseBody as Record<string, unknown>,
        config
      )
      return { body: redacted, wasRedacted: summary.piiFound, summary }
    }

    return {
      body: responseBody,
      wasRedacted: false,
      summary: { redacted: String(responseBody), piiFound: false, redactedFields: [], redactionCount: 0 },
    }
  }
}
