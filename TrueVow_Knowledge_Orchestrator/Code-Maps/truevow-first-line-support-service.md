# Code Structure Map — First Line Support Service

> Auto-generated: 2026-05-29
> Repository: `TrueVow_First_Line_Support_Service`

## File Breakdown

| Extension | Count |
|-----------|-------|
| .ts | 190 |
| .tsx | 75 |
| .md | 12 |
| .json | 5 |
| .ps1 | 4 |
| .js | 4 |
| .py | 4 |
| .sql | 2 |
| .css | 1 |
| .ico | 1 |
| .local | 1 |
| .tsbuildinfo | 1 |

## Directory Tree

```
```

## Component Graph

```mermaid
graph TD
```

## Issues Found (49)

### MEDIUM

- **9 .md files at repository root**
  > Move to a subfolder (docs/)
  > _C:\Users\yasha\OneDrive\Documents\TrueVow\Cursor\TrueVow_First_Line_Support_Service_

- **"page.tsx" appears in 18 locations**
  > Found at: ..\..\TrueVow_First_Line_Support_Service\app\(dashboard)\demo\page.tsx, ..\..\TrueVow_First_Line_Support_Service\app\(dashboard)\dialer\page.tsx, ..\..\TrueVow_First_Line_Support_Service\app\(dashboard)\enterprise-dashboard\page.tsx...
  > _..\..\TrueVow_First_Line_Support_Service\app\(dashboard)\demo\page.tsx_

- **"layout.tsx" appears in 2 locations**
  > Found at: ..\..\TrueVow_First_Line_Support_Service\app\(dashboard)\layout.tsx, ..\..\TrueVow_First_Line_Support_Service\app\layout.tsx
  > _..\..\TrueVow_First_Line_Support_Service\app\(dashboard)\layout.tsx_

- **"route.ts" appears in 91 locations**
  > Found at: ..\..\TrueVow_First_Line_Support_Service\app\api\admin\users\route.ts, ..\..\TrueVow_First_Line_Support_Service\app\api\health\route.ts, ..\..\TrueVow_First_Line_Support_Service\app\api\support\case\[id]\route.ts...
  > _..\..\TrueVow_First_Line_Support_Service\app\api\admin\users\route.ts_

- **"index.ts" appears in 3 locations**
  > Found at: ..\..\TrueVow_First_Line_Support_Service\components\shared\index.ts, ..\..\TrueVow_First_Line_Support_Service\lib\config\index.ts, ..\..\TrueVow_First_Line_Support_Service\lib\repositories\index.ts
  > _..\..\TrueVow_First_Line_Support_Service\components\shared\index.ts_

- **"api-key.ts" appears in 2 locations**
  > Found at: ..\..\TrueVow_First_Line_Support_Service\lib\auth\api-key.ts, ..\..\TrueVow_First_Line_Support_Service\lib\middleware\api-key.ts
  > _..\..\TrueVow_First_Line_Support_Service\lib\auth\api-key.ts_

- **"README.md" appears in 2 locations**
  > Found at: ..\..\TrueVow_First_Line_Support_Service\scripts\README.md, ..\..\TrueVow_First_Line_Support_Service\README.md
  > _..\..\TrueVow_First_Line_Support_Service\scripts\README.md_

### LOW

- **Deep nesting (depth 6): ..\..\TrueVow_First_Line_Support_Service\app\api\v1\ai\support\analyze**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_First_Line_Support_Service\app\api\v1\ai\support\analyze_

- **Deep nesting (depth 6): ..\..\TrueVow_First_Line_Support_Service\app\api\v1\ai\support\respond**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_First_Line_Support_Service\app\api\v1\ai\support\respond_

- **Deep nesting (depth 6): ..\..\TrueVow_First_Line_Support_Service\app\api\v1\beacon\session\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_First_Line_Support_Service\app\api\v1\beacon\session\[id]_

- **Deep nesting (depth 6): ..\..\TrueVow_First_Line_Support_Service\app\api\v1\collision\[id]\active**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_First_Line_Support_Service\app\api\v1\collision\[id]\active_

- **Deep nesting (depth 6): ..\..\TrueVow_First_Line_Support_Service\app\api\v1\collision\[id]\typing**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_First_Line_Support_Service\app\api\v1\collision\[id]\typing_

- **Deep nesting (depth 6): ..\..\TrueVow_First_Line_Support_Service\app\api\v1\collision\[id]\viewing**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_First_Line_Support_Service\app\api\v1\collision\[id]\viewing_

- **Deep nesting (depth 6): ..\..\TrueVow_First_Line_Support_Service\app\api\v1\communication-templates\[templateKey]\render**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_First_Line_Support_Service\app\api\v1\communication-templates\[templateKey]\render_

- **Deep nesting (depth 6): ..\..\TrueVow_First_Line_Support_Service\app\api\v1\communication-templates\[templateKey]\send**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_First_Line_Support_Service\app\api\v1\communication-templates\[templateKey]\send_

- **Deep nesting (depth 6): ..\..\TrueVow_First_Line_Support_Service\app\api\v1\csms\[csmId]\phone-number**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_First_Line_Support_Service\app\api\v1\csms\[csmId]\phone-number_

- **Deep nesting (depth 6): ..\..\TrueVow_First_Line_Support_Service\app\api\v1\customer-portal\ai\chat**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_First_Line_Support_Service\app\api\v1\customer-portal\ai\chat_

- **Deep nesting (depth 6): ..\..\TrueVow_First_Line_Support_Service\app\api\v1\customer-portal\kb\search**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_First_Line_Support_Service\app\api\v1\customer-portal\kb\search_

- **Deep nesting (depth 6): ..\..\TrueVow_First_Line_Support_Service\app\api\v1\customer-portal\tickets\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_First_Line_Support_Service\app\api\v1\customer-portal\tickets\[id]_

- **Deep nesting (depth 7): ..\..\TrueVow_First_Line_Support_Service\app\api\v1\customer-portal\tickets\[id]\messages**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_First_Line_Support_Service\app\api\v1\customer-portal\tickets\[id]\messages_

- **Deep nesting (depth 7): ..\..\TrueVow_First_Line_Support_Service\app\api\v1\customer-portal\tickets\[id]\reply**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_First_Line_Support_Service\app\api\v1\customer-portal\tickets\[id]\reply_

- **Deep nesting (depth 6): ..\..\TrueVow_First_Line_Support_Service\app\api\v1\dialer\permissions\toggle**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_First_Line_Support_Service\app\api\v1\dialer\permissions\toggle_

- **Deep nesting (depth 6): ..\..\TrueVow_First_Line_Support_Service\app\api\v1\email\unsubscribe\[token]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_First_Line_Support_Service\app\api\v1\email\unsubscribe\[token]_

- **Deep nesting (depth 6): ..\..\TrueVow_First_Line_Support_Service\app\api\v1\inbox\[id]\call**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_First_Line_Support_Service\app\api\v1\inbox\[id]\call_

- **Deep nesting (depth 6): ..\..\TrueVow_First_Line_Support_Service\app\api\v1\inbox\[id]\copilot**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_First_Line_Support_Service\app\api\v1\inbox\[id]\copilot_

- **Deep nesting (depth 6): ..\..\TrueVow_First_Line_Support_Service\app\api\v1\inbox\[id]\draft**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_First_Line_Support_Service\app\api\v1\inbox\[id]\draft_

- **Deep nesting (depth 6): ..\..\TrueVow_First_Line_Support_Service\app\api\v1\inbox\[id]\mentions**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_First_Line_Support_Service\app\api\v1\inbox\[id]\mentions_

- **Deep nesting (depth 6): ..\..\TrueVow_First_Line_Support_Service\app\api\v1\inbox\[id]\reply**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_First_Line_Support_Service\app\api\v1\inbox\[id]\reply_

- **Deep nesting (depth 6): ..\..\TrueVow_First_Line_Support_Service\app\api\v1\inbox\[id]\send-email**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_First_Line_Support_Service\app\api\v1\inbox\[id]\send-email_

- **Deep nesting (depth 6): ..\..\TrueVow_First_Line_Support_Service\app\api\v1\inbox\[id]\send-sms**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_First_Line_Support_Service\app\api\v1\inbox\[id]\send-sms_

- **Deep nesting (depth 6): ..\..\TrueVow_First_Line_Support_Service\app\api\v1\inbox\[id]\shared-draft**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_First_Line_Support_Service\app\api\v1\inbox\[id]\shared-draft_

- **Deep nesting (depth 6): ..\..\TrueVow_First_Line_Support_Service\app\api\v1\inbox\[id]\summarize**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_First_Line_Support_Service\app\api\v1\inbox\[id]\summarize_

- **Deep nesting (depth 6): ..\..\TrueVow_First_Line_Support_Service\app\api\v1\kb\articles\[id]**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_First_Line_Support_Service\app\api\v1\kb\articles\[id]_

- **Deep nesting (depth 7): ..\..\TrueVow_First_Line_Support_Service\app\api\v1\kb\articles\[id]\helpful**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_First_Line_Support_Service\app\api\v1\kb\articles\[id]\helpful_

- **Deep nesting (depth 6): ..\..\TrueVow_First_Line_Support_Service\app\api\v1\messages\webhook\sms**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_First_Line_Support_Service\app\api\v1\messages\webhook\sms_

- **Deep nesting (depth 6): ..\..\TrueVow_First_Line_Support_Service\app\api\v1\messages\webhook\whatsapp**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_First_Line_Support_Service\app\api\v1\messages\webhook\whatsapp_

- **Deep nesting (depth 6): ..\..\TrueVow_First_Line_Support_Service\app\api\v1\sales-webchat\[id]\messages**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_First_Line_Support_Service\app\api\v1\sales-webchat\[id]\messages_

- **Deep nesting (depth 6): ..\..\TrueVow_First_Line_Support_Service\app\api\v1\sales-webchat\[id]\voice**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_First_Line_Support_Service\app\api\v1\sales-webchat\[id]\voice_

- **Deep nesting (depth 6): ..\..\TrueVow_First_Line_Support_Service\app\api\v1\support\phone-numbers\pool**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_First_Line_Support_Service\app\api\v1\support\phone-numbers\pool_

- **Deep nesting (depth 6): ..\..\TrueVow_First_Line_Support_Service\app\api\v1\unified-inbox\[id]\assign-context**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_First_Line_Support_Service\app\api\v1\unified-inbox\[id]\assign-context_

- **Deep nesting (depth 6): ..\..\TrueVow_First_Line_Support_Service\app\api\v1\webchat\[id]\end**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_First_Line_Support_Service\app\api\v1\webchat\[id]\end_

- **Deep nesting (depth 6): ..\..\TrueVow_First_Line_Support_Service\app\api\v1\webchat\[id]\read**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_First_Line_Support_Service\app\api\v1\webchat\[id]\read_

- **Deep nesting (depth 6): ..\..\TrueVow_First_Line_Support_Service\app\api\v1\webchat\[id]\voice**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_First_Line_Support_Service\app\api\v1\webchat\[id]\voice_

- **Deep nesting (depth 6): ..\..\TrueVow_First_Line_Support_Service\app\api\v1\webhooks\platform\milestone**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_First_Line_Support_Service\app\api\v1\webhooks\platform\milestone_

- **Deep nesting (depth 6): ..\..\TrueVow_First_Line_Support_Service\app\api\v1\webhooks\twilio\call**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_First_Line_Support_Service\app\api\v1\webhooks\twilio\call_

- **Deep nesting (depth 7): ..\..\TrueVow_First_Line_Support_Service\app\api\v1\webhooks\twilio\call\handle**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_First_Line_Support_Service\app\api\v1\webhooks\twilio\call\handle_

- **Deep nesting (depth 7): ..\..\TrueVow_First_Line_Support_Service\app\api\v1\webhooks\twilio\call\recording**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_First_Line_Support_Service\app\api\v1\webhooks\twilio\call\recording_

- **Deep nesting (depth 7): ..\..\TrueVow_First_Line_Support_Service\app\api\v1\webhooks\twilio\call\transcribe**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_First_Line_Support_Service\app\api\v1\webhooks\twilio\call\transcribe_

- **Deep nesting (depth 6): ..\..\TrueVow_First_Line_Support_Service\app\api\v1\webhooks\twilio\sms**
  > Deeply nested folders are hard to discover. Consider flattening.
  > _..\..\TrueVow_First_Line_Support_Service\app\api\v1\webhooks\twilio\sms_



## Related Service
- [[Cross-Service/truevow-first-line-support-service|Service Page]]
