---
category: architecture
title: "Sales Ops \u2014 5 Factory Multi-Agent CRM System"
importance: 10
tags: ["sales-ops", "factory", "multi-agent", "crm", "leads", "outreach", "sub-agents", "manager-agents"]
file_paths: []
created: 2026-06-25T02:45:34.923195+00:00
updated: 2026-06-25T02:45:34.923195+00:00
memory_id: 22aa21ea-5a49-4c61-b2c3-d8a00b63a7ba
---

# Sales Ops — 5 Factory Multi-Agent CRM System

Sales CRM is built around 5 FACTORIES (sub-modules), each with a manager agent orchestrating sub-agents: 1) LEADS MANAGEMENT (Manager: Razi) — 12-stage lead pipeline: Market Planner → Scout → Identity Normalizer → Website Profiler → Contact Enricher → Deep Enricher (DeepSeek LLM) → Validation Agent → Signal Scorer → Quality Gates → QA Auditor → Outreach Writer → Ingestor. 2) COLD OUTREACH (Manager: Siraj). 3) AD OUTREACH (Manager: Tariq). 4) LEAD ENGAGEMENT (Manager: Omar). 5) MARKETING INTELLIGENCE (Manager: Imran). Central orchestrator: SaniaOrchestrator (factory-dispatcher.ts). 4 seeded playbooks. Multi-agent production features: circuit breakers, retry with exponential backoff, LLM failover (Claude→Kimi), human trainable feedback loops. Stack: Next.js/TypeScript, Supabase, port 3056, 400+ Jest tests, 28 integration tests.

---
**Category:** `architecture` | **Importance:** 10/10
**Files:** N/A
