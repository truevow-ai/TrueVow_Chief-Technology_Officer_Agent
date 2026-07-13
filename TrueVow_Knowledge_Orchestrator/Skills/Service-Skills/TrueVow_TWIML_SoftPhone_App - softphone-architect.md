---
source: TrueVow_TWIML_SoftPhone_App/.opencode/skills/softphone-architect/SKILL.md
service: TrueVow_TWIML_SoftPhone_App
type: voice-agent
stack: ["python", "flask", "twilio"]
imported: 2026-06-30T22:32:05.328742+00:00
skill_name: softphone-architect
---
# TWIML SoftPhone Architect

## Description
Plans features, validates against architecture, creates implementation specs for TWIML SoftPhone (Voice Agent).

## Workflow
1. Load context from AGENTS.md and working cache
2. Analyze the request against existing voice architecture
3. Create a detailed implementation plan with file paths and tasks
4. Delegate to coder for implementation

## Rules
- Never modify code directly — plan first, delegate implementation
- Validate all decisions against AGENTS.md service-specific rules
- Respect Twilio/TWIML conventions for voice response handling
- Record architecture decisions in memory via `memory.py remember`

## Ecosystem Integration
This skill is registered in config.yaml. Dispatch routes architecture tasks here.
