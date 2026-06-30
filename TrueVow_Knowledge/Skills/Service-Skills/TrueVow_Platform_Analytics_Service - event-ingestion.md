---
source: TrueVow_Platform_Analytics_Service/.opencode/skills/event-ingestion/SKILL.md
service: TrueVow_Platform_Analytics_Service
type: analytics
stack: ["python", "fastapi"]
imported: 2026-06-30T22:32:05.242282+00:00
skill_name: event-ingestion
---
---
name: event-ingestion
description: How to ingest and process analytics events from platform services.
---

# Event Ingestion

## Overview
This skill covers the event ingestion pipeline for the Platform Analytics Service.
Events from all platform microservices flow through this pipeline.

## When to Use
- Adding new event types to the platform
- Modifying event ingestion endpoints
- Debugging event processing issues
- Implementing new event validators

## Implementation Steps
1. Define event type in `app/warehouse/event_store/envelope.py` (EventTypes class)
2. Add event to the appropriate domain category
3. If new service, add to ServiceNames class
4. Update EventAuthorityRules if event has restricted authority
5. Test ingestion via POST /api/v1/events/ingest
6. Verify event appears in event_store table

## Validation Checklist
- [ ] Event type follows naming convention (lowercase, underscores)
- [ ] Event is added to correct domain in EventTypes
- [ ] Service name is in ServiceNames
- [ ] Authority rules are set if event is restricted
- [ ] Ingestion endpoint accepts the event
- [ ] Event is stored correctly in event_store table

## Files to Modify
- `app/warehouse/event_store/envelope.py` — Event types and authority rules
- `app/api/v1/endpoints/events.py` — Ingestion endpoint
- `app/api/v1/endpoints/portal_integration.py` — Portal event endpoint
