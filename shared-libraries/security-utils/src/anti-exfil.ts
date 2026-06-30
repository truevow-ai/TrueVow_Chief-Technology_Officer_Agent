/**
 * Anti-Exfiltration Controls — LLM Zone Defense Layer
 * 
 * Prevents data exfiltration from LLM-enabled services (Clerk App 2):
 * - Prompt injection detection
 * - Response size limits
 * - Sensitive data pattern blocking
 * - Rate limiting for data access
 * - Outbound payload inspection
 */

// ─── Types ────────────────────────────────────────────────────────
export interface ExfilCheckResult {
  blocked: boolean
  reason: string
  riskScore: number       // 0-100
  detectedPatterns: string[]
}

export interface AntiExfilConfig {
  maxResponseSizeBytes: number
  maxFieldCount: number
  blockPatterns: RegExp[]
  riskThreshold: number   // Block if riskScore >= this
}

// ─── Default Config ───────────────────────────────────────────────
const DEFAULT_CONFIG: AntiExfilConfig = {
  maxResponseSizeBytes: 50_000,   // 50KB max per response
  maxFieldCount: 100,
  blockPatterns: [],
  riskThreshold: 70,
}

// ─── Prompt Injection Detection ───────────────────────────────────
const INJECTION_PATTERNS: Array<{ pattern: RegExp; weight: number; name: string }> = [
  { pattern: /ignore\s+(all\s+)?previous\s+instructions/i, weight: 90, name: 'ignore_instructions' },
  { pattern: /you\s+are\s+now\s+(a|an)/i, weight: 80, name: 'role_override' },
  { pattern: /system\s*:\s*/i, weight: 70, name: 'system_prompt_injection' },
  { pattern: /\[INST\]/i, weight: 85, name: 'instruction_tag' },
  { pattern: /<\|im_start\|>/i, weight: 85, name: 'chat_ml_injection' },
  { pattern: /pretend\s+you/i, weight: 60, name: 'pretend_attack' },
  { pattern: /reveal\s+(your|the)\s+(system|instructions|prompt)/i, weight: 95, name: 'prompt_extraction' },
  { pattern: /output\s+(all|every)\s+(data|record|user|customer)/i, weight: 90, name: 'bulk_extraction' },
  { pattern: /base64\s*encode/i, weight: 75, name: 'encoding_attempt' },
  { pattern: /eval\s*\(/i, weight: 80, name: 'code_injection' },
]

/**
 * Detect prompt injection attempts in input text
 */
export function detectPromptInjection(input: string): ExfilCheckResult {
  const detectedPatterns: string[] = []
  let maxWeight = 0

  for (const { pattern, weight, name } of INJECTION_PATTERNS) {
    if (pattern.test(input)) {
      detectedPatterns.push(name)
      maxWeight = Math.max(maxWeight, weight)
    }
  }

  return {
    blocked: maxWeight >= DEFAULT_CONFIG.riskThreshold,
    reason: detectedPatterns.length > 0
      ? `Prompt injection detected: ${detectedPatterns.join(', ')}`
      : 'Clean',
    riskScore: maxWeight,
    detectedPatterns,
  }
}

// ─── Response Size & Structure Checks ─────────────────────────────
/**
 * Check if outbound response exceeds safe limits
 */
export function checkResponseSize(
  responseBody: unknown,
  config: Partial<AntiExfilConfig> = {}
): ExfilCheckResult {
  const cfg = { ...DEFAULT_CONFIG, ...config }
  const detectedPatterns: string[] = []
  let riskScore = 0

  // Size check
  const serialized = JSON.stringify(responseBody)
  const sizeBytes = new TextEncoder().encode(serialized).length

  if (sizeBytes > cfg.maxResponseSizeBytes) {
    detectedPatterns.push('oversized_response')
    riskScore = Math.max(riskScore, 80)
  }

  // Field count check (prevents bulk data dumps)
  if (responseBody && typeof responseBody === 'object') {
    const fieldCount = countFields(responseBody)
    if (fieldCount > cfg.maxFieldCount) {
      detectedPatterns.push('excessive_fields')
      riskScore = Math.max(riskScore, 70)
    }
  }

  // Block pattern check
  for (const pattern of cfg.blockPatterns) {
    if (pattern.test(serialized)) {
      detectedPatterns.push('blocked_pattern')
      riskScore = Math.max(riskScore, 90)
    }
  }

  return {
    blocked: riskScore >= cfg.riskThreshold,
    reason: detectedPatterns.length > 0
      ? `Exfiltration risk: ${detectedPatterns.join(', ')} (size: ${sizeBytes}B)`
      : 'Clean',
    riskScore,
    detectedPatterns,
  }
}

/**
 * Combined anti-exfiltration check for LLM zone responses.
 * Runs both prompt injection and response checks.
 */
export function antiExfilCheck(
  input: string | null,
  output: unknown,
  config?: Partial<AntiExfilConfig>
): ExfilCheckResult {
  const results: ExfilCheckResult[] = []

  // Check input for prompt injection
  if (input) {
    results.push(detectPromptInjection(input))
  }

  // Check output for data exfiltration
  results.push(checkResponseSize(output, config))

  // Combine results — take worst case
  const blocked = results.some(r => r.blocked)
  const allPatterns = results.flatMap(r => r.detectedPatterns)
  const maxRisk = Math.max(...results.map(r => r.riskScore), 0)

  return {
    blocked,
    reason: blocked
      ? `Anti-exfiltration block: ${allPatterns.join(', ')}`
      : 'Clean',
    riskScore: maxRisk,
    detectedPatterns: [...new Set(allPatterns)],
  }
}

// ─── Helpers ──────────────────────────────────────────────────────
function countFields(obj: unknown, depth = 0): number {
  if (depth > 10) return 0 // Prevent infinite recursion
  if (!obj || typeof obj !== 'object') return 0

  let count = 0
  if (Array.isArray(obj)) {
    for (const item of obj) {
      count += countFields(item, depth + 1)
    }
  } else {
    const entries = Object.entries(obj)
    count += entries.length
    for (const [, v] of entries) {
      count += countFields(v, depth + 1)
    }
  }
  return count
}
