/**
 * Credential Scoping Registry
 *
 * Tool-agnostic credential manager. No dependency on opencode, Cursor, or any harness.
 * Each agent receives ONLY the env vars it needs — never the full .env.local.
 *
 * Protocol: JSON file at TrueVow_Knowledge/Agent/credential-scope.json
 * Any agent runtime reads this file to determine what credentials to inject.
 */

// --- Types (language-agnostic, mirrored in credential-scope.json) ---

interface CredentialScope {
  agent_id: string;           // e.g. "sania-sales-agent"
  services: string[];         // e.g. ["sales-ops"]
  allowed_env: string[];      // e.g. ["SALES_OPS_DATABASE_URL", "SALES_OPS_SERVICE_API_KEY"]
  blocked_env: string[];      // Never expose these (e.g. Stripe keys for non-billing agents)
  max_lifetime_minutes: number; // Credential TTL
}

interface CredentialRegistry {
  version: "1.0";
  updated: string;            // ISO timestamp
  scopes: CredentialScope[];
  master_key_env: string[];   // Only orchestrator sees these
}

// --- Hardcoded scope definitions (sync with DEVELOPERS.md) ---

const DEFAULT_REGISTRY: CredentialRegistry = {
  version: "1.0",
  updated: new Date().toISOString(),
  master_key_env: [
    "STRIPE_SECRET_KEY",
    "CLERK_SECRET_KEY",
    "JWT_SECRET_KEY",
    "SENDGRID_API_KEY",
    "TWILIO_AUTH_TOKEN",
    "DEEPGRAM_API_KEY",
    "CARTESIA_API_KEY",
    "EXA_API_KEY",
    "COURTLISTENER_API_KEY",
  ],
  scopes: [
    // --- Ghulam Ghaus (Faisalabad) — Tenant App + Billing ---
    {
      agent_id: "ghaus-fsd-*",
      services: ["tenant-app", "billing"],
      allowed_env: [
        "TENANT_APP_DATABASE_URL", "TENANT_APP_SERVICE_API_KEY",
        "TENANT_BILLING_DATABASE_URL", "TENANT_BILLING_SERVICE_API_KEY",
        "TWILIO_ACCOUNT_SID", "TWILIO_API_KEY",
        "DEEPGRAM_API_KEY", "CARTESIA_API_KEY",
        "LIVEKIT_API_KEY", "LIVEKIT_API_SECRET",
        "GEMINI_API_KEY", "XAI_API_KEY",
      ],
      blocked_env: ["STRIPE_SECRET_KEY", "CLERK_SECRET_KEY", "JWT_SECRET_KEY"],
      max_lifetime_minutes: 480,
    },
    // --- Ghulam Ghous (Islamabad) — SaaS Admin + CSM + First Line Support ---
    {
      agent_id: "ghous-isb-*",
      services: ["saas-admin", "csm-core", "first-line-support"],
      allowed_env: [
        "SAAS_ADMIN_DATABASE_URL", "SAAS_ADMIN_SERVICE_API_KEY",
        "CSM_CORE_DATABASE_URL", "CSM_CORE_SERVICE_API_KEY",
        "FIRST_LINE_SUPPORT_DATABASE_URL",
        "PLATFORM_SERVICE_API_KEY",
        "SENDGRID_API_KEY", "RESEND_CS_SUPPORT_API_KEY",
      ],
      blocked_env: ["STRIPE_SECRET_KEY", "TWILIO_AUTH_TOKEN", "CARTESIA_API_KEY"],
      max_lifetime_minutes: 480,
    },
    // --- Ms. Sania — Sales Ops ---
    {
      agent_id: "sania-*",
      services: ["sales-ops"],
      allowed_env: [
        "SALES_OPS_DATABASE_URL", "SALES_OPS_SERVICE_API_KEY",
        "SAAS_ADMIN_SERVICE_API_KEY",
      ],
      blocked_env: ["STRIPE_SECRET_KEY", "CLERK_SECRET_KEY", "TWILIO_AUTH_TOKEN"],
      max_lifetime_minutes: 480,
    },
    // --- Yasha (Orchestrator) — everything ---
    {
      agent_id: "yasha-orchestrator",
      services: ["all"],
      allowed_env: ["*"],   // Orchestrator gets full access
      blocked_env: [],
      max_lifetime_minutes: 1440,
    },
    // --- Default fallback (any unknown agent) ---
    {
      agent_id: "default",
      services: [],
      allowed_env: [
        "DATABASE_URL",
        "SUPABASE_URL", "SUPABASE_ANON_KEY",
      ],
      blocked_env: ["STRIPE_SECRET_KEY", "CLERK_SECRET_KEY", "JWT_SECRET_KEY",
                    "TWILIO_AUTH_TOKEN", "SENDGRID_API_KEY", "DEEPGRAM_API_KEY",
                    "CARTESIA_API_KEY", "EXA_API_KEY", "COURTLISTENER_API_KEY"],
      max_lifetime_minutes: 60,
    },
  ],
};

// --- Utility: resolve scope for an agent ---

function resolveScope(agentId: string): CredentialScope {
  // Exact match first
  const exact = DEFAULT_REGISTRY.scopes.find(s => s.agent_id === agentId);
  if (exact) return exact;

  // Wildcard match
  const wildcard = DEFAULT_REGISTRY.scopes.find(s => {
    const pattern = s.agent_id.replace("*", ".*");
    return new RegExp("^" + pattern + "$").test(agentId);
  });

  return wildcard || DEFAULT_REGISTRY.scopes.find(s => s.agent_id === "default")!;
}

// --- Utility: filter env vars based on scope ---

function filterEnvForAgent(agentId: string, fullEnv: Record<string, string>): Record<string, string> {
  const scope = resolveScope(agentId);

  if (scope.allowed_env.includes("*")) {
    return fullEnv;  // Orchestrator gets everything
  }

  const filtered: Record<string, string> = {};

  for (const [key, value] of Object.entries(fullEnv)) {
    // Explicitly blocked
    if (scope.blocked_env.some(blocked => key.toUpperCase().includes(blocked.toUpperCase()))) {
      continue;
    }
    // Explicitly allowed
    if (scope.allowed_env.some(allowed => {
      if (allowed === "*") return true;
      return key.toUpperCase().includes(allowed.toUpperCase());
    })) {
      filtered[key] = value;
    }
  }

  return filtered;
}

export { DEFAULT_REGISTRY, resolveScope, filterEnvForAgent };
export type { CredentialScope, CredentialRegistry };
