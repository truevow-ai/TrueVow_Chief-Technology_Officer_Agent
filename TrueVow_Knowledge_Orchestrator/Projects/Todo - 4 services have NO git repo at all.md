---
category: todo
title: "4 services have NO git repo at all"
importance: 8
tags: ["git", "nogit", "risk"]
file_paths: []
created: 2026-06-25T04:04:57.762279+00:00
updated: 2026-06-25T04:04:57.762279+00:00
memory_id: efb8c900-03b4-451c-914f-91804fd2189e
---

# 4 services have NO git repo at all

Dialogflow_Intake_Service, Platform_Analytics_Service, Tenant_VERIFY_Service, TWIML_SoftPhone_App are NOT git repositories — entire source unversioned/unbacked. Separate from (and worse than) the gitignore leak. Needs a CTO decision: git-init + initial commit (secrets-scan first).

---
**Category:** `todo` | **Importance:** 8/10
**Files:** N/A
