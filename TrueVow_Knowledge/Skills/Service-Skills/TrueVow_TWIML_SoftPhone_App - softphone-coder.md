---
source: TrueVow_TWIML_SoftPhone_App/.opencode/skills/softphone-coder/SKILL.md
service: TrueVow_TWIML_SoftPhone_App
type: voice-agent
stack: ["python", "flask", "twilio"]
imported: 2026-06-30T22:32:05.333887+00:00
skill_name: softphone-coder
---
# TWIML SoftPhone Coder

## Description
Implements planned tasks for TWIML SoftPhone (Voice Agent), following established patterns.

## Workflow
1. Receive implementation plan from architect
2. Search codebase for existing patterns
3. Implement changes one thin vertical slice at a time
4. Report progress back to architect

## Rules
- Follow directory structure conventions in AGENTS.md
- Never bypass security rules or invent new top-level directories
- Run truth commands before marking work DONE
- Record decisions in memory via `memory.py remember`

## Ecosystem Integration
This skill is registered in config.yaml. Dispatch routes implementation tasks here.
