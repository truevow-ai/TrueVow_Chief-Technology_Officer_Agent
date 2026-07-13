# Service Dependency Map

> High-level data flow and integration points between services.

```mermaid
graph TD
    Portal[Customer Portal] --> Analytics[Platform Analytics]
    Portal --> InternalOps[Internal Ops]
    Portal --> Application[Tenant Application]
    Application --> SaaSAdmin[SaaS Administration]
    Application --> Billing[Tenant Billing]
    LEVERAGE[Tenant LEVERAGE] --> Application
    SETTLE[Tenant SETTLE] --> Financial[Financial Management]
    VERIFY[Tenant VERIFY] --> Application
    CONNECT[Tenant CONNECT] --> Application
    Dialogflow[Dialogflow Intake] --> FirstLine[First Line Support]
    FirstLine --> CustomerSuccess[Customer Success CORE]
    Sales[Sales Ops] --> SaaSAdmin
    Sales --> Application
```

## Known Broken Links
- **Platform Analytics → Supabase DB** — DNS fails (see [[Incident-001]])
- **Internal Ops → Supabase REST** — port 443 unreachable (same root cause)

## Data Flow Notes
- All services use Supabase as backing store (with direct or REST access)
- Registry pattern exists in Internal Ops but is nascent
- No event bus / message queue exists yet — services call each other via HTTP
