# Developer Quickstart — One Page

## Start Your Service

1. Clone your repo
2. Copy `.env.local` from Yasha (secure channel)
3. Double-click `start_*.bat`
4. If it fails, see below.

## Fast Fixes (in order)

### DB connection fails
Your `.env.local` has multiple DB URL formats. If direct DNS fails:
- Open `.env.local` → find `*_SESSION_POOLER_URL` or `*_TRANSACTION_POOLER_URL`
- Open `app/core/config.py` → make `DATABASE_URL` property prefer pooler over direct
- Pattern: pooler URLs with `aws-*-*.pooler.supabase.com` always work

### Port in use
Check `app/core/config.py` for `PORT` or `service_port`. Change if needed.

### Import errors (Python)
Missing packages: run `pip install -r requirements.txt` in the venv.

### Import errors (Next.js)
Missing packages: run `npm install` (or `pnpm install` for SaaS Admin).

### Emoji crash on Windows
Some Python services use emoji in print statements. Remove them from `app/main.py` lifespan function. Replace with plain text.

## Log Your Work

From the Cursor root directory:
```
log "file-write" "Changed billing route" "ghaus-fsd-agent" "billing"
log "blocker" "DB not connecting" "ghaus-fsd-agent" "billing"
log "task-complete" "Invoice generation done" "ghaus-fsd-agent" "billing"
```

Actions: task-start, task-complete, task-fail, file-write, file-read, blocker, decision, question

## Don't

- Delete files without Yasha's approval
- Commit `.env` or `.env.local`
- Push directly to main without PR if working on a shared branch
- Skip logging — Yasha needs audit trail for investor due diligence

## Service Owners

| Service | Port | Owner |
|---------|------|-------|
| SaaS Admin | 3001 | Ghulam Ghous (ISB) |
| CSM CORE | 3012 | Ghulam Ghous (ISB) |
| First Line Support | 3007 | Ghulam Ghous (ISB) |
| Tenant App | 3022 | Ghulam Ghaus (FSD) |
| Billing | 3016 | Ghulam Ghaus (FSD) |
| Sales Ops | 3056 | Ms. Sania |
