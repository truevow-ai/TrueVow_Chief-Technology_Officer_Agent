---
category: architecture
title: "INTAKE \u2014 Multi-Bridge Voice Orchestration Platform"
importance: 10
tags: ["intake", "voice-bridge", "gemini", "dograh", "assemblyai", "pipecat", "xai", "fsm", "workflow", "orchestration"]
file_paths: []
created: 2026-06-25T02:45:31.370891+00:00
updated: 2026-06-25T02:45:31.370891+00:00
memory_id: 4f23972d-b0a1-489c-8055-4ceb3ecb6211
---

# INTAKE — Multi-Bridge Voice Orchestration Platform

INTAKE uses a Common Voice Bridge Interface that decouples voice technology from intake logic. All bridges implement: start conversation, receive/return audio, barge-in handling, tool calls to intake engine, receive instructions, end call cleanly. ACTIVE BRIDGES: 1) Gemini Live Bridge (WebSocket to Gemini 3.1 Flash Live API, V2 Direct Demo, 36 tests), 2) Dograh Bridge (separate bridge, 25 tests), 3) AssemblyAI Bridge, 4) Pipecat Bridge, 5) xAI Bridge (handoff ready). Shared intake engine: FSM workflow (~108 nodes for PI intake) handles questions, branching, lead scoring, guardrails. Workflow pushed from SaaS Admin per tenant. Bridge adapter pattern: SaaS Admin assigns different voice tech to different law firm tenants. 61 total bridge tests passing. Frontend: gemini_direct_demo.js browser WebSocket capture.

---
**Category:** `architecture` | **Importance:** 10/10
**Files:** N/A
