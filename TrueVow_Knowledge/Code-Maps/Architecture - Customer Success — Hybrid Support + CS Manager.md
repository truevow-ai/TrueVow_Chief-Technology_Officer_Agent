---
category: architecture
title: "Customer Success \u2014 Hybrid Support + CS Manager"
importance: 9
tags: ["customer-success", "support", "hybrid-agent", "faq", "llm", "compliance", "cs-manager"]
file_paths: []
created: 2026-06-25T02:45:38.775335+00:00
updated: 2026-06-25T02:45:38.775335+00:00
memory_id: fdfa4951-1172-476c-a51c-de65966ff520
---

# Customer Success — Hybrid Support + CS Manager

Customer Success CORE service has two major components: 1) HYBRID SUPPORT AGENT: 3-tier architecture — Tier 1: Rule-Based FAQ Agent (deterministic matching from knowledge base, FIRST CHOICE). Tier 2: LLM Enhancement Agent (augments Tier 1 with multi-provider LLM, adds structure/personalization). Tier 3: Compliance Validator (checks blocked phrases, validates zero-knowledge reminders, triggers escalation). Structured Response Formatter for final output. 2) CUSTOMER SUCCESS MANAGER MODULE: manages law firm relationships, onboarding, and account health. Stack: Next.js 14+ App Router, TypeScript, Tailwind, Clerk Auth, Supabase PostgreSQL, Claude + Kimi LLMs, Deepgram STT + Cartesia TTS. Port 3003. Also has AI Agent Prompts design system with context management.

---
**Category:** `architecture` | **Importance:** 9/10
**Files:** N/A
