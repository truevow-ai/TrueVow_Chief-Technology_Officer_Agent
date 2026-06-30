# Worker Specifications (Declarative)
# Tool-agnostic YAML specs for agent workers.
# Pattern inspired by HiClaw CRDs but adapted for filesystem-based workflow.
# Lives in Knowledge vault — any harness can read these specs.

# Format:
# workers/
#   {service-name}.yaml    — One spec per service
#   _template.yaml         — Default template for new workers

## Worker lifecycle states
##   pending    → Agent spec created, not yet assigned
##   active     → Agent is running or available
##   sleeping   → Idle, auto-stopped to save resources
##   stopped    → Manually stopped
##   failed     → Crashed or unresponsive

## Agent runtimes (tool-agnostic)
##   opencode    — opencode CLI agent
##   cursor      — Cursor IDE agent
##   pi          — Pi Coding Harness agent
##   custom      — Any other harness, provide command
