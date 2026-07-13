---
category: bug
title: "Fixed obsidian-bridge.py Windows-filename crash (orchestration tooling)"
importance: 7
tags: ["orchestration", "obsidian", "windows", "bugfix"]
file_paths: []
created: 2026-06-25T03:12:30.766632+00:00
updated: 2026-06-25T03:12:30.766632+00:00
memory_id: 371d09f7-d397-4c19-8ec2-9974e6a7465d
---

# Fixed obsidian-bridge.py Windows-filename crash (orchestration tooling)

obsidian-bridge.py built Obsidian filenames from memory/session titles but only stripped / and \ — any title containing a Windows-illegal char (: ? * " < > |) threw OSError [Errno 22] and crashed the ENTIRE ecosystem knowledge-sync on Windows (e.g. a title ending "active: me"). Fix: added safe_filename() that strips all illegal chars + control chars, trims trailing dots/spaces, caps length; applied at the memory-filename site; also hardened the YAML title: line via json.dumps to survive titles containing quotes. Verified: sync now completes (35 memories / 24 skills / 4 agents, exit 0). NOTE: ../orchestration is NOT version-controlled (on-disk only) — if there is a canonical source for the orchestration tooling, apply the same sanitizer there.

---
**Category:** `bug` | **Importance:** 7/10
**Files:** N/A
