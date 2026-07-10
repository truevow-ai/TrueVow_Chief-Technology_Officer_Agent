# Infisical — TrueVow Secret Management

Self-hosted secret manager for all 13 platform services.
Replaces `.env.local` sprawl. One source, no duplication, no leakage.

## Quick Start — Server

```bash
cd infisical
cp server.env.example server.env
# Edit server.env — generate real keys (see comments)
docker compose up -d
```

Visit `http://localhost` → create admin account.
Then: `infisical login` (the CLI opens your browser for OAuth).

## 13-Repo Rollout (in order)

### Phase 1 — One-time infrastructure (human steps)

1. Deploy the server on a shared host (Fly.io recommended for a distributed team — localhost Docker only works for single-dev eval). Spin up `docker-compose.yml` on Fly.io (or use Infisical's `docker-compose.prod.yml`). Set `SITE_URL` to the real domain. TLS terminate with Fly.io's built-in certs.
2. Create your admin account via the web UI.
3. Create an **Infisical organization** for TrueVow.

### Phase 2 — Per-repo setup (human steps, 5 min each)

For each repo:

```bash
cd services/<repo>
infisical login
infisical init --project-name="<Repo-Name>" --env=development
infisical init --env=staging
infisical init --env=production
```

Then run the migration helper to push existing `.env.local` secrets:

```powershell
.\infisical\migrate-secrets.ps1 -RepoPath "TrueVow_Tenant_TRACE_Service"
```

After migration, **delete `.env.local`** and switch to:

```bash
# Instead of: python app/main.py
infisical run -- python app/main.py
# Instead of: npm run dev
infisical run -- npm run dev
```

### Phase 3 — CI / Fly.io

For CI: set `INFISICAL_TOKEN` in GitHub secrets (or equivalent). For Fly.io production: keep `fly secrets set` as the canonical path; Infisical syncs to it optionally.

## Project map (least-privilege by trust domain)

Each service only sees its own secrets. No App2 service has App1 secrets, etc.

| Trust Domain | Services | Secret Scope | Dev Access |
|---|---|---|---|
| PLATFORM_OPERATORS (App1) | SaaS Admin, Internal Ops, CS Core, FM, Billing | Per-service DB+API keys; billing holds TELR/Stripe only | ghous-isb (SaaS Admin/CS Core), ghaus-fsd (Billing), yasha (FM/Internal Ops) |
| SALES_SUPPORT (App2) | Sales Ops | Lead DB + SendGrid/Resend + LLM API keys. NO PHI keys, no Supabase service role. | sania |
| TENANTS (App3) | INTAKE, Customer Portal, TRACE, SETTLE, LEVERAGE, VERIFY | Per-service. TRACE holds Supabase service role + PHI key + fax key + Clerk App3. SETTLE holds STRIPE only. LEVERAGE holds zero secrets. | ghaus-fsd (INTAKE), yasha (rest) |

Each developer gets `member` access in Infisical scoped to their services only. yasha gets `admin` across all.

## Migrate then retire

The PowerShell migration helper (`infisical/migrate-secrets.ps1`) reads a repo's `.env.local`, pushes each variable to the correct Infisical project+environment, and **writes `\n# Migrated to Infisical — not used`** at the top of the former `.env.local` so it's safe to keep as a reference but visibly retired.

After all 13 repos are migrated and verified working with `infisical run`, delete all `.env.local` files permanently.

## Maintenance

```bash
# Regenerate the memory digest after any secret rotation
python TrueVow_Shared_Orchestration/memory.py remember context "Secret rotated: <name>" "Rotated SUPA_KEY in TRACE. Updated in Infisical." --importance 5 --tags secret-rotation

# Pre-commit hook (catches leaks before they reach git)
infisical scan install --pre-commit-hook
```

## Security

- **No `.env.local` on disk in production or CI.** Secrets injected at runtime only.
- **Infisical self-hosted.** Data never leaves the Fly.io private network. No external BAA needed.
- **Least-privilege per developer.** Each dev only sees secrets for their owned services.
- **Audit trail.** Every secret read/write/rotation is logged.

## Infisical Official Secrets Policy

No `.env.local` files anywhere in code or CI. Any `.env.local` found after migration completion is treated as a security incident.
