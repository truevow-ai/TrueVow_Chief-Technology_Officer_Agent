# Code Structure Map — Sales Ops Service

> Auto-generated: 2026-05-29
> Repository: `TrueVow_Sales_Ops_Service`

## File Breakdown

| Extension | Count |
|-----------|-------|
| .ts | 639 |
| .md | 220 |
| .tsx | 218 |
| .sql | 104 |
| .js | 38 |
| .ps1 | 5 |
| .json | 4 |
| .txt | 3 |
| .old | 2 |
| .toml | 2 |
| .css | 1 |
| .bak | 1 |
| .rtf | 1 |
| .local | 1 |
| (none) | 1 |
| .tsbuildinfo | 1 |

## Directory Tree

```
```

## Component Graph

```mermaid
graph TD
```

## Issues Found (186)

### MEDIUM

- **"route.test.ts" appears in 2 locations**
  > Found at: ..\..\TrueVow_Sales_Ops_Service\__tests__\api\v1\gtm\playbooks\route.test.ts, ..\..\TrueVow_Sales_Ops_Service\__tests__\api\v1\leads\route.test.ts
  > _..\..\TrueVow_Sales_Ops_Service\__tests__\api\v1\gtm\playbooks\route.test.ts_

- **"page.tsx" appears in 70 locations**
  > Found at: ..\..\TrueVow_Sales_Ops_Service\app\(auth)\sign-in\[[...sign-in]]\page.tsx, ..\..\TrueVow_Sales_Ops_Service\app\(auth)\sign-up\[[...sign-up]]\page.tsx, ..\..\TrueVow_Sales_Ops_Service\app\(dashboard)\email\analytics\page.tsx...
  > _..\..\TrueVow_Sales_Ops_Service\app\(auth)\sign-in\[[...sign-in]]\page.tsx_

- **"layout.tsx" appears in 2 locations**
  > Found at: ..\..\TrueVow_Sales_Ops_Service\app\(dashboard)\layout.tsx, ..\..\TrueVow_Sales_Ops_Service\app\layout.tsx
  > _..\..\TrueVow_Sales_Ops_Service\app\(dashboard)\layout.tsx_

- **"route.ts" appears in 317 locations**
  > Found at: ..\..\TrueVow_Sales_Ops_Service\app\api\analytics\events\route.ts, ..\..\TrueVow_Sales_Ops_Service\app\api\analytics\link\route.ts, ..\..\TrueVow_Sales_Ops_Service\app\api\cron\check-domain-health\route.ts...
  > _..\..\TrueVow_Sales_Ops_Service\app\api\analytics\events\route.ts_

- **"RevenueMetricsCard.tsx" appears in 2 locations**
  > Found at: ..\..\TrueVow_Sales_Ops_Service\components\sales\analytics\RevenueMetricsCard.tsx, ..\..\TrueVow_Sales_Ops_Service\components\sales\revops\RevenueMetricsCard.tsx
  > _..\..\TrueVow_Sales_Ops_Service\components\sales\analytics\RevenueMetricsCard.tsx_

- **"IMPLEMENTATION_COMPLETE.md" appears in 2 locations**
  > Found at: ..\..\TrueVow_Sales_Ops_Service\docs\Brief\GTM-Playbook-First-10-Weeks\IMPLEMENTATION_COMPLETE.md, ..\..\TrueVow_Sales_Ops_Service\docs\sales-ops\IMPLEMENTATION_COMPLETE.md
  > _..\..\TrueVow_Sales_Ops_Service\docs\Brief\GTM-Playbook-First-10-Weeks\IMPLEMENTATION_COMPLETE.md_

- **"INTEGRATION_COMPLETE.md" appears in 2 locations**
  > Found at: ..\..\TrueVow_Sales_Ops_Service\docs\Brief\GTM-Playbook-First-10-Weeks\INTEGRATION_COMPLETE.md, ..\..\TrueVow_Sales_Ops_Service\docs\integrations\INTEGRATION_COMPLETE.md
  > _..\..\TrueVow_Sales_Ops_Service\docs\Brief\GTM-Playbook-First-10-Weeks\INTEGRATION_COMPLETE.md_

- **"README.md" appears in 6 locations**
  > Found at: ..\..\TrueVow_Sales_Ops_Service\docs\Brief\GTM-Playbook-First-10-Weeks\README.md, ..\..\TrueVow_Sales_Ops_Service\docs\integrations\README.md, ..\..\TrueVow_Sales_Ops_Service\docs\lead-research\README.md...
  > _..\..\TrueVow_Sales_Ops_Service\docs\Brief\GTM-Playbook-First-10-Weeks\README.md_

- **"icp_messaging_v1.md" appears in 2 locations**
  > Found at: ..\..\TrueVow_Sales_Ops_Service\docs\Brief\icp_messaging_v1.md, ..\..\TrueVow_Sales_Ops_Service\rules\icp_messaging_v1.md
  > _..\..\TrueVow_Sales_Ops_Service\docs\Brief\icp_messaging_v1.md_

- **"types.ts" appears in 4 locations**
  > Found at: ..\..\TrueVow_Sales_Ops_Service\lib\agent-framework\types.ts, ..\..\TrueVow_Sales_Ops_Service\lib\chief-of-staff\types.ts, ..\..\TrueVow_Sales_Ops_Service\lib\lead-factory\types.ts...
  > _..\..\TrueVow_Sales_Ops_Service\lib\agent-framework\types.ts_

- **"email-drafting-agent.ts" appears in 2 locations**
  > Found at: ..\..\TrueVow_Sales_Ops_Service\lib\agents\email-drafting-agent.ts, ..\..\TrueVow_Sales_Ops_Service\lib\ai-agents\email-drafting\email-drafting-agent.ts
  > _..\..\TrueVow_Sales_Ops_Service\lib\agents\email-drafting-agent.ts_

- **"index.ts" appears in 15 locations**
  > Found at: ..\..\TrueVow_Sales_Ops_Service\lib\agents\index.ts, ..\..\TrueVow_Sales_Ops_Service\lib\chief-of-staff\index.ts, ..\..\TrueVow_Sales_Ops_Service\lib\db\repositories\index.ts...
  > _..\..\TrueVow_Sales_Ops_Service\lib\agents\index.ts_

- **"revops-tracker.ts" appears in 2 locations**
  > Found at: ..\..\TrueVow_Sales_Ops_Service\lib\agents\revops-tracker.ts, ..\..\TrueVow_Sales_Ops_Service\lib\services\revops-tracker.ts
  > _..\..\TrueVow_Sales_Ops_Service\lib\agents\revops-tracker.ts_

- **"rate-limiter.ts" appears in 2 locations**
  > Found at: ..\..\TrueVow_Sales_Ops_Service\lib\ai-agents\rate-limiter.ts, ..\..\TrueVow_Sales_Ops_Service\lib\middleware\rate-limiter.ts
  > _..\..\TrueVow_Sales_Ops_Service\lib\ai-agents\rate-limiter.ts_

- **"errors.ts" appears in 2 locations**
  > Found at: ..\..\TrueVow_Sales_Ops_Service\lib\api\errors.ts, ..\..\TrueVow_Sales_Ops_Service\lib\utils\errors.ts
  > _..\..\TrueVow_Sales_Ops_Service\lib\api\errors.ts_

- **"validation.ts" appears in 3 locations**
  > Found at: ..\..\TrueVow_Sales_Ops_Service\lib\api\validation.ts, ..\..\TrueVow_Sales_Ops_Service\lib\middleware\validation.ts, ..\..\TrueVow_Sales_Ops_Service\lib\utils\validation.ts
  > _..\..\TrueVow_Sales_Ops_Service\lib\api\validation.ts_

- **"manager.ts" appears in 4 locations**
  > Found at: ..\..\TrueVow_Sales_Ops_Service\lib\factories\ad-outreach\manager.ts, ..\..\TrueVow_Sales_Ops_Service\lib\factories\cold-outreach\manager.ts, ..\..\TrueVow_Sales_Ops_Service\lib\factories\lead-engagement\manager.ts...
  > _..\..\TrueVow_Sales_Ops_Service\lib\factories\ad-outreach\manager.ts_

- **"client.ts" appears in 2 locations**
  > Found at: ..\..\TrueVow_Sales_Ops_Service\lib\integrations\internal-ops\client.ts, ..\..\TrueVow_Sales_Ops_Service\lib\llm\client.ts
  > _..\..\TrueVow_Sales_Ops_Service\lib\integrations\internal-ops\client.ts_

- **"auth.ts" appears in 2 locations**
  > Found at: ..\..\TrueVow_Sales_Ops_Service\lib\middleware\auth.ts, ..\..\TrueVow_Sales_Ops_Service\lib\auth.ts
  > _..\..\TrueVow_Sales_Ops_Service\lib\middleware\auth.ts_

- **"email-template-service.ts" appears in 2 locations**
  > Found at: ..\..\TrueVow_Sales_Ops_Service\lib\services\playbooks\email-template-service.ts, ..\..\TrueVow_Sales_Ops_Service\lib\services\email-template-service.ts
  > _..\..\TrueVow_Sales_Ops_Service\lib\services\playbooks\email-template-service.ts_

### LOW

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\(dashboard)\sales\campaigns\[id]\cadences**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\(dashboard)\sales\campaigns\[id]\cadences_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\(dashboard)\sales\campaigns\[id]\enrollments**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\(dashboard)\sales\campaigns\[id]\enrollments_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\(dashboard)\sales\campaigns\[id]\send-log**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\(dashboard)\sales\campaigns\[id]\send-log_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\(dashboard)\sales\gtm\auto-reply\queue**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\(dashboard)\sales\gtm\auto-reply\queue_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\(dashboard)\sales\gtm\auto-reply\settings**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\(dashboard)\sales\gtm\auto-reply\settings_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\(dashboard)\sales\marketing\campaigns\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\(dashboard)\sales\marketing\campaigns\[id]_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\activities\[activity_id]\complete**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\activities\[activity_id]\complete_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\agents\bdr\execute**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\agents\bdr\execute_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\agents\dlq\[dlq_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\agents\dlq\[dlq_id]_

- **Deep nesting (depth 7): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\agents\dlq\[dlq_id]\resolve**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\agents\dlq\[dlq_id]\resolve_

- **Deep nesting (depth 7): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\agents\dlq\[dlq_id]\retry**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\agents\dlq\[dlq_id]\retry_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\agents\email-drafting\execute**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\agents\email-drafting\execute_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\agents\email-sending\execute**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\agents\email-sending\execute_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\agents\feedback\[feedback_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\agents\feedback\[feedback_id]_

- **Deep nesting (depth 7): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\agents\feedback\[feedback_id]\apply**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\agents\feedback\[feedback_id]\apply_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\agents\interactions\[interaction_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\agents\interactions\[interaction_id]_

- **Deep nesting (depth 7): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\agents\interactions\[interaction_id]\review**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\agents\interactions\[interaction_id]\review_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\agents\interactions\pending-review**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\agents\interactions\pending-review_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\agents\knowledge-base\[kb_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\agents\knowledge-base\[kb_id]_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\agents\performance\[agent_name]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\agents\performance\[agent_name]_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\agents\rate-limits\alerts**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\agents\rate-limits\alerts_

- **Deep nesting (depth 7): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\agents\rate-limits\alerts\[alert_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\agents\rate-limits\alerts\[alert_id]_

- **Deep nesting (depth 8): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\agents\rate-limits\alerts\[alert_id]\acknowledge**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\agents\rate-limits\alerts\[alert_id]\acknowledge_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\agents\sdr\execute**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\agents\sdr\execute_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\agents\state\conversation**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\agents\state\conversation_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\agents\state\workflow**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\agents\state\workflow_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\analytics\dashboard\stats**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\analytics\dashboard\stats_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\analytics\pipeline\advanced**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\analytics\pipeline\advanced_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\analytics\pipeline\distribution**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\analytics\pipeline\distribution_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\analytics\pipeline\stuck-deals**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\analytics\pipeline\stuck-deals_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\applications\[id]\status**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\applications\[id]\status_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\applications\[id]\submit-kyc**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\applications\[id]\submit-kyc_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\calls\[call_id]\assistant**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\calls\[call_id]\assistant_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\calls\[call_id]\auto-update**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\calls\[call_id]\auto-update_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\calls\[call_id]\objections**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\calls\[call_id]\objections_

- **Deep nesting (depth 7): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\calls\[call_id]\objections\[objection_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\calls\[call_id]\objections\[objection_id]_

- **Deep nesting (depth 8): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\calls\[call_id]\objections\[objection_id]\handle**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\calls\[call_id]\objections\[objection_id]\handle_

- **Deep nesting (depth 7): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\calls\[call_id]\objections\realtime**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\calls\[call_id]\objections\realtime_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\calls\[call_id]\room**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\calls\[call_id]\room_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\calls\[call_id]\transcribe**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\calls\[call_id]\transcribe_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\calls\objections\metrics**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\calls\objections\metrics_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\calls\objections\reframe**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\calls\objections\reframe_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\calls\objections\suggestions**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\calls\objections\suggestions_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\coaching\scorecards\[rep_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\coaching\scorecards\[rep_id]_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\coaching\scorecards\team**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\coaching\scorecards\team_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\cohorts\[id]\evaluate**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\cohorts\[id]\evaluate_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\communications\calls\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\communications\calls\[id]_

- **Deep nesting (depth 7): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\communications\calls\[id]\analyze**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\communications\calls\[id]\analyze_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\communications\link\call-to-conversation**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\communications\link\call-to-conversation_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\communications\link\conversation-to-call**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\communications\link\conversation-to-call_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\communications\twilio\inbound-call**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\communications\twilio\inbound-call_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\contacts\[contact_id]\relationships**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\contacts\[contact_id]\relationships_

- **Deep nesting (depth 7): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\contacts\[contact_id]\relationships\[relationship_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\contacts\[contact_id]\relationships\[relationship_id]_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\contacts\[contact_id]\send-email**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\contacts\[contact_id]\send-email_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\contacts\segments\[segment_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\contacts\segments\[segment_id]_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\dashboard\layouts\[layout_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\dashboard\layouts\[layout_id]_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\demos\[demo_id]\complete**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\demos\[demo_id]\complete_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\dialer\parallel\[session_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\dialer\parallel\[session_id]_

- **Deep nesting (depth 7): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\dialer\parallel\[session_id]\connect**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\dialer\parallel\[session_id]\connect_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\dialer\permissions\toggle**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\dialer\permissions\toggle_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\dialer\webrtc\token**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\dialer\webrtc\token_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\discoveries\[id]\action-items**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\discoveries\[id]\action-items_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\discoveries\[id]\analyze**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\discoveries\[id]\analyze_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\discoveries\[id]\complete**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\discoveries\[id]\complete_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\discoveries\[id]\follow-ups**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\discoveries\[id]\follow-ups_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\discoveries\[id]\start**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\discoveries\[id]\start_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\domains\[domain]\pattern**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\domains\[domain]\pattern_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\email\ab-test\[test_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\email\ab-test\[test_id]_

- **Deep nesting (depth 7): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\email\ab-test\[test_id]\analyze**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\email\ab-test\[test_id]\analyze_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\email\campaigns\[campaign_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\email\campaigns\[campaign_id]_

- **Deep nesting (depth 7): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\email\campaigns\[campaign_id]\draft**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\email\campaigns\[campaign_id]\draft_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\email\domain-rotation\select**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\email\domain-rotation\select_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\email\domain-warming\[domain]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\email\domain-warming\[domain]_

- **Deep nesting (depth 7): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\email\domain-warming\[domain]\record-email**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\email\domain-warming\[domain]\record-email_

- **Deep nesting (depth 7): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\email\domain-warming\[domain]\record-engagement**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\email\domain-warming\[domain]\record-engagement_

- **Deep nesting (depth 7): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\email\domain-warming\[domain]\record-spam-complaint**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\email\domain-warming\[domain]\record-spam-complaint_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\email\import\api**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\email\import\api_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\email\import\csv**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\email\import\csv_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\email\ip-mappings\[mapping_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\email\ip-mappings\[mapping_id]_

- **Deep nesting (depth 7): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\email\ip-mappings\[mapping_id]\swap-ip**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\email\ip-mappings\[mapping_id]\swap-ip_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\email\playbooks\[playbook_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\email\playbooks\[playbook_id]_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\email\replies\webhook**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\email\replies\webhook_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\email\sequences\[sequence_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\email\sequences\[sequence_id]_

- **Deep nesting (depth 7): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\email\sequences\[sequence_id]\conditional**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\email\sequences\[sequence_id]\conditional_

- **Deep nesting (depth 7): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\email\sequences\[sequence_id]\sms-fallback**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\email\sequences\[sequence_id]\sms-fallback_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\email\templates\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\email\templates\[id]_

- **Deep nesting (depth 7): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\email\templates\[id]\validate**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\email\templates\[id]\validate_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\email\templates\generate**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\email\templates\generate_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\email\track\open**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\email\track\open_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\email\unsubscribe\[token]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\email\unsubscribe\[token]_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\emails\[message_id]\bounce**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\emails\[message_id]\bounce_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\emails\[message_id]\engagement**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\emails\[message_id]\engagement_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\emails\[message_id]\spam-complaint**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\emails\[message_id]\spam-complaint_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\emails\verify-bulk\leads**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\emails\verify-bulk\leads_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\emails\verify-bulk\sanitize**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\emails\verify-bulk\sanitize_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\emails\verify-bulk\threshold**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\emails\verify-bulk\threshold_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\factories\[factory]\execute**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\factories\[factory]\execute_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\factories\leads-management\batch**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\factories\leads-management\batch_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\gtm\playbooks\[playbook_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\gtm\playbooks\[playbook_id]_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\gtm\playbooks\start**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\gtm\playbooks\start_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\gtm\templates\[template_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\gtm\templates\[template_id]_

- **Deep nesting (depth 7): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\gtm\templates\[template_id]\activate**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\gtm\templates\[template_id]\activate_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\gtm\templates\[template_key]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\gtm\templates\[template_key]_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\hitl\approvals\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\hitl\approvals\[id]_

- **Deep nesting (depth 7): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\hitl\approvals\[id]\review**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\hitl\approvals\[id]\review_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\inbox\conversations\[conversation_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\inbox\conversations\[conversation_id]_

- **Deep nesting (depth 7): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\inbox\conversations\[conversation_id]\assign**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\inbox\conversations\[conversation_id]\assign_

- **Deep nesting (depth 7): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\inbox\conversations\[conversation_id]\link**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\inbox\conversations\[conversation_id]\link_

- **Deep nesting (depth 8): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\inbox\conversations\[conversation_id]\link\auto**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\inbox\conversations\[conversation_id]\link\auto_

- **Deep nesting (depth 8): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\inbox\conversations\[conversation_id]\link\contact**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\inbox\conversations\[conversation_id]\link\contact_

- **Deep nesting (depth 8): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\inbox\conversations\[conversation_id]\link\lead**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\inbox\conversations\[conversation_id]\link\lead_

- **Deep nesting (depth 7): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\inbox\conversations\[conversation_id]\reply**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\inbox\conversations\[conversation_id]\reply_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\integrations\internal-ops\health**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\integrations\internal-ops\health_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\leads\[id]\activities**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\leads\[id]\activities_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\leads\[id]\churn-risk**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\leads\[id]\churn-risk_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\leads\[id]\convert**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\leads\[id]\convert_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\leads\[id]\enrich**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\leads\[id]\enrich_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\leads\[id]\enrich-waterfall**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\leads\[id]\enrich-waterfall_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\leads\[id]\generate-email**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\leads\[id]\generate-email_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\leads\[id]\health-score**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\leads\[id]\health-score_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\leads\[id]\intent**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\leads\[id]\intent_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\leads\[id]\lead-score**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\leads\[id]\lead-score_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\leads\[id]\make-call**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\leads\[id]\make-call_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\leads\[id]\marketing-intelligence**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\leads\[id]\marketing-intelligence_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\leads\[id]\qualification**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\leads\[id]\qualification_

- **Deep nesting (depth 7): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\leads\[id]\qualification\disqualify**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\leads\[id]\qualification\disqualify_

- **Deep nesting (depth 7): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\leads\[id]\qualification\qualify**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\leads\[id]\qualification\qualify_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\leads\[id]\qualify**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\leads\[id]\qualify_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\leads\[id]\send-email**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\leads\[id]\send-email_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\leads\[id]\send-sms**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\leads\[id]\send-sms_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\leads\[id]\sla-status**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\leads\[id]\sla-status_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\leads\[id]\verify-email**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\leads\[id]\verify-email_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\leads\webhooks\enrich**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\leads\webhooks\enrich_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\llm-agents\[agent_id]\execute**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\llm-agents\[agent_id]\execute_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\llm-agents\[agent_id]\toggle**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\llm-agents\[agent_id]\toggle_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\llm-agents\ai-sdr\qualify**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\llm-agents\ai-sdr\qualify_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\llm-agents\by-lead\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\llm-agents\by-lead\[id]_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\llm-agents\email-sending\sequence**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\llm-agents\email-sending\sequence_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\llm-agents\email-writing\complete-workflow**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\llm-agents\email-writing\complete-workflow_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\llm-agents\email-writing\write**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\llm-agents\email-writing\write_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\messages\webhook\sms**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\messages\webhook\sms_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\messages\webhook\whatsapp**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\messages\webhook\whatsapp_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\notifications\[notification_id]\read**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\notifications\[notification_id]\read_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\objections\[objection_id]\responses**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\objections\[objection_id]\responses_

- **Deep nesting (depth 7): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\objections\[objection_id]\responses\[response_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\objections\[objection_id]\responses\[response_id]_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\objections\[response_id]\record-usage**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\objections\[response_id]\record-usage_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\onboarding\[onboarding_id]\steps**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\onboarding\[onboarding_id]\steps_

- **Deep nesting (depth 7): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\onboarding\[onboarding_id]\steps\[step_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\onboarding\[onboarding_id]\steps\[step_id]_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\pipeline\automation\[automation_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\pipeline\automation\[automation_id]_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\pipeline\cycle\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\pipeline\cycle\[id]_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\pipeline\stages\[stage_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\pipeline\stages\[stage_id]_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\playbooks\[id]\execute**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\playbooks\[id]\execute_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\pods\[pod_id]\members**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\pods\[pod_id]\members_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\providers\[id]\pause**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\providers\[id]\pause_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\providers\[id]\resume**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\providers\[id]\resume_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\providers\[id]\test**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\providers\[id]\test_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\qualification\by-lead\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\qualification\by-lead\[id]_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\scripts\[script_id]\usage**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\scripts\[script_id]\usage_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\security\events\[event_id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\security\events\[event_id]_

- **Deep nesting (depth 7): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\security\events\[event_id]\resolve**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\security\events\[event_id]\resolve_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\services\[serviceId]\health**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\services\[serviceId]\health_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\services\[serviceId]\toggle**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\services\[serviceId]\toggle_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\tasks\[task_id]\complete**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\tasks\[task_id]\complete_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\users\[user_id]\phone-number**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\users\[user_id]\phone-number_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\webhooks\twilio\call-status**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\webhooks\twilio\call-status_

- **Deep nesting (depth 6): ..\..\TrueVow_Sales_Ops_Service\app\api\v1\webhooks\twilio\sms**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_Sales_Ops_Service\app\api\v1\webhooks\twilio\sms_



## Related Service
- [[Cross-Service/truevow-sales-ops-service|Service Page]]
