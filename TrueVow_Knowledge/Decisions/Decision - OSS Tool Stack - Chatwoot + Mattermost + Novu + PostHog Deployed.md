---
category: decision
title: "OSS Tool Stack - Chatwoot + Mattermost + Novu + PostHog Deployed"
importance: 10
tags: ["oss-tools", "chatwoot", "mattermost", "novu", "posthog", "replacement", "archive"]
file_paths: []
created: 2026-06-25T03:47:07.347281+00:00
updated: 2026-06-25T03:47:07.347281+00:00
memory_id: d139273e-8e40-4143-b3fc-140e4ef3e2f4
---

# OSS Tool Stack - Chatwoot + Mattermost + Novu + PostHog Deployed

Four open-source tools deployed to replace/augment custom services: 1) CHATWOOT (21.5k stars) replaces First-Line Support Service at port 3007 - multi-channel inbox, ticketing, knowledge base, AI co-pilot, CSAT. First-Line Support repo archived. 2) MATTERMOST (30k+ stars) replaces Internal Ops Team Chat at port 8065 - Slack alternative. 3) NOVU (35k+ stars) replaces custom notifications across all services at ports 3009/4200 - unified email/SMS/push/in-app. 4) POSTHOG (29k+ stars) augments Platform Analytics at port 8010 - product analytics, session recording. All managed via shared-libraries/oss-tools/docker-compose.yml. Docker Hub connectivity issues may require retry on docker-compose up.

---
**Category:** `decision` | **Importance:** 10/10
**Files:** N/A
