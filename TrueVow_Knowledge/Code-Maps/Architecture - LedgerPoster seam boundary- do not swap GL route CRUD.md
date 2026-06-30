---
category: architecture
title: "LedgerPoster seam boundary: do not swap GL route CRUD"
importance: 6
tags: []
file_paths: []
created: 2026-06-25T02:13:36.635916+00:00
updated: 2026-06-25T02:13:36.635916+00:00
memory_id: 50d16c96-2732-4835-95eb-bfd2363129c7
---

# LedgerPoster seam boundary: do not swap GL route CRUD

journal_entry_routes.py posting/reversal/draft paths already use get_ledger_poster() (lines 59/185/259). The 6 remaining JournalEntryService(db) sites only use entry_repo/line_repo, bulk_upsert_lines, and _validate_required_dimensions, which the LedgerPoster Protocol intentionally excludes. Do NOT route these through the seam: it would break mypy and runtime under an alternate backend. Current state is correct by design. Offline seam suite green: 12 passed (logs/ledger_seam_verify.log).

---
**Category:** `architecture` | **Importance:** 6/10
**Files:** N/A
