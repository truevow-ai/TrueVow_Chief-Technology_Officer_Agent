# TrueVow Developer Onboarding

## Quick Start — Your Service

| Developer | Service | Start Command | Status |
|-----------|---------|---------------|--------|
| **Ghulam Ghous (ISB)** | SaaS Admin | `start_saas.bat` → :3001 | Ready |
| **Ghulam Ghous (ISB)** | CSM CORE | `start_csm.bat` → :3061 | Verified |
| **Ghulam Ghous (ISB)** | First Line Support | `start_fls.bat` → :3066 | Ready |
| **Ghulam Ghaus (FSD)** | Tenant App | Deployed on Fly.io | Prod |
| **Ghulam Ghaus (FSD)** | Billing | `start_billing.bat` → :3016 | DB fix needed |
| **Ms. Sania** | Sales Ops | `start_sales.bat` → :3056 | Ready |

## Known Issues (Read Before Starting)

1. **DB DNS**: `db.*.supabase.co` domains fail. Use pooler URLs instead (`aws-*-*.pooler.supabase.com`). Every `.env.local` has them.
2. **Emoji crashes**: Some Python services have emoji in `print()` statements. Remove them from `app/main.py` if your console crashes on startup.
3. **Python 3.13**: Some pinned deps need loosening. If `pip install` fails, try `>=` instead of `==`.

## Before You Start Work

1. **Read the live log** — check `TrueVow_Knowledge\Session-Logs\live\{today}.jsonl` to see what other developers did today
2. **Check your credential scope** — `TrueVow_Knowledge\Agent\credential-scope.json` lists which env vars your agent gets
3. **Log everything** — every action must be logged:
   ```bash
   python TrueVow_Knowledge\Skills\vault-log.py --agent {your-agent-id} --action file-write --detail "Changed billing route" --service billing
   ```

## Rules

- **No file deletions** without Yasha's explicit approval
- **Commit source files** — .pyc bytecode is not enough
- **Log before you act** — write to the live log, then do the work
- **Never commit .env files** — credentials stay local
- **If blocked** — write to `Session-Logs/live/{date}.jsonl` with action `blocker`

## Database Note

All services use Supabase. If direct DB DNS fails (`db.*.supabase.co`), use pooler URLs instead (`aws-*-*.pooler.supabase.com`). Pooler URLs are in each service's `.env.local`.
