---
category: pattern
title: "Voice Bridge Latency Budget"
importance: 8
tags: ["voice", "bridge", "latency", "tts", "stt", "fsm", "pattern"]
file_paths: []
created: 2026-06-25T02:17:11.642886+00:00
updated: 2026-06-25T02:17:11.642886+00:00
memory_id: cbd11196-c76e-4c76-b856-0dad03c07afa
---

# Voice Bridge Latency Budget

All voice bridges (Cartesia, Deepgram, telephony) must complete FSM state transitions within 500ms. Cartesia TTS streaming should begin within 150ms of chunk receipt. Bridge adapter pattern: each bridge implements a common Adapter interface (connect, stream, disconnect). FSM orchestrator routes to active bridge based on availability and cost.

---
**Category:** `pattern` | **Importance:** 8/10
**Files:** N/A
