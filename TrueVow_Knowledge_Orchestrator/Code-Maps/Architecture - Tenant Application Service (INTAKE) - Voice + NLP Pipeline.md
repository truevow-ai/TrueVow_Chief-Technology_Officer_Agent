---
category: architecture
title: "Tenant Application Service (INTAKE) - Voice + NLP Pipeline"
importance: 8
tags: ["intake", "nlp", "fsm", "voice", "fastapi", "python", "tenant-application"]
file_paths: []
created: 2026-06-25T02:09:36.138004+00:00
updated: 2026-06-25T02:09:36.138004+00:00
memory_id: cf20b875-ffc7-4dfb-ae0f-acbef2008a13
---

# Tenant Application Service (INTAKE) - Voice + NLP Pipeline

Phase I intake services. Stack: Python/FastAPI backend, FSM-based deterministic NLP engine, voice pipeline. Purpose: Legal AI intake for personal injury attorneys - captures client information via voice/NLP. Separated from website code (Nov 2025). Technology: Finite State Machine, deterministic NLP (not LLM-based for compliance). Voice pipeline components integrated. Ports: API backend. Depends on: SaaS Admin (tenant management, auth). Related: Benjamin voice agent (STT/TTS), Dialogflow Intake (alternative intake path).

---
**Category:** `architecture` | **Importance:** 8/10
**Files:** N/A
