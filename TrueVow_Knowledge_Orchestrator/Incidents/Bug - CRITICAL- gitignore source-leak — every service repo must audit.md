---
category: bug
title: "CRITICAL: gitignore source-leak \u2014 every service repo must audit"
importance: 9
tags: ["gitignore", "build", "ci", "critical", "cross-service", "audit"]
file_paths: []
created: 2026-06-25T02:54:02.328966+00:00
updated: 2026-06-25T02:54:02.328966+00:00
memory_id: 64bc43bf-5694-450a-8d02-bd2c6c8da821
---

# CRITICAL: gitignore source-leak — every service repo must audit

A stray/unanchored .gitignore directory rule (e.g. lib/ or logs/ WITHOUT a leading slash) silently ignores real source files at ANY depth — they are never committed, local builds/tests pass, but origin/main fails to build from a clean clone, and ripgrep/editor search is BLINDED (it skips ignored files). Found+fixed in SaaS Admin (hid ~55 lib/ files + a real endpoint app/api/v1/security/audit/logs/route.ts). EVERY TrueVow service MUST audit before next feature work. TRIAGE (repo root): run "git ls-files --others --ignored --exclude-standard --directory" and look for any source-looking dir (lib/src/app/core/utils/services/api/logs/components/hooks). FIX: anchor rules to root (lib/ -> /lib/ or delete for TS repos; logs/ -> /logs/), remove embedded garbage lines + stray nul, RE-VERIFY secrets still ignored, then secrets-scan + commit recovered files in reviewed batches by subsystem (NEVER git add . ; stage explicit paths), prove with a clean-clone build. FULL PLAYBOOK: TrueVow_SaaS_Administration_Service/docs/01-main/ECOSYSTEM_ADVISORY_GITIGNORE_SOURCE_LEAK.md. REPORT BACK: agent-checkin done + memory remember with result (CLEAN | FIXED n files | BLOCKED).

---
**Category:** `bug` | **Importance:** 9/10
**Files:** N/A
