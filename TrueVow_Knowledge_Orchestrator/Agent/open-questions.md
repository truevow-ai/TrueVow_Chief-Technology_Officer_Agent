# Open Questions for the User

**Last updated:** 2026-06-02 (ALL ANSWERED — Q1-Q12 closed)

These are decisions, inputs, or clarifications I'm waiting on from the human. The orchestrator should not proceed unilaterally on any of these.

---

## Bridges work tracking

### Q1. Which tracking workflow? ✅ ANSWERED 2026-06-02
- **Answer:** "best of both daily checkin" → **Option C: Hybrid** (git hook + 60-sec daily check-in)
- Built: `Skills/daily-checkin.md`

### Q2. Approve the 3 new user-facing skills? ✅ ANSWERED 2026-06-02
- **Answer:** "skills approved" → all 3 approved
- Built: `Skills/log-test-result.md`, `Skills/log-blocker.md`, `Skills/log-task-completion.md`

### Q3. Catalog your other AI tools ✅ ANSWERED 2026-06-02
- Tools: VSCode (code editor), opencode (orchestrator CLI), Chrome browser (testing)

### Q4. What's the bridges "done" state? ✅ ANSWERED 2026-06-02
- Real bridge list: LiveKit, Cartesia, AssemblyAI, xAI/Groq, Dograh, Gemini Live
- "Done" = bridges are testable end-to-end

### Q5. Backfill last week's work? ✅ COMPLETE 2026-06-02
- Read 5 per-bridge PROGRESS_LOG.md files, 2 BRIDGE_DIFFERENCE_REPORT.md, 1 BRIDGE_CHANGES_FOR_OTHER_AGENTS.md, 1 SESSION_SUMMARY, root PROGRESS_LOG (913 lines)
- Synthesized into `Session-Logs/2026-06-02-bridges-audit.md` + `Projects/tenant-app-bridges.md`
- SaaS Admin repo pending (separate task)

---

## Skills system

### Q6. First weekly Feedback Agent run / audit? ✅ ANSWERED 2026-06-02
- **Answer:** "you can do a audit of last one week sessions"
- Built: `Skills/audit-week-of-sessions.md` + ran the audit (`Session-Logs/2026-06-02-bridges-audit.md`) — 15 sessions, 6 bridges, 5 cross-cutting patterns, 5 unverified claims

### Q7. Extract more skills? ✅ ANSWERED 2026-06-02
- **Answer:** "yes extract all the skills you can and build whats pending"
- Built 6 new skills: log-test-result, log-blocker, log-task-completion, daily-checkin, backfill-project-from-repos, audit-week-of-sessions
- Total skills now: 16

---

## Indexer

### Q8. Fix the indexer? ✅ ANSWERED 2026-06-02
- **Answer:** "yes reindex all"
- Deleted `.vector-index.json`, ran reindex (now 843 chunks, 85 files). Reindex takes ~5 min with model download.
- Indexer fixes (.yaml support, skip-if-fresh) still on the idea list but not urgent

---

## Open Incidents / Items (from `.triage.yaml` perspective)

### Q9. The "Tenant App cleanup — awaiting agent's audit response" kanban entry ✅ ANSWERED 2026-06-02
- **Answer:** "wait on the tenant app cleanup once when we are done with the testings of all the bridges and give you the green signal because that is just maintenance, it can wait"
- Moved to 🟡 Deferred in KANBAN — awaiting bridges all-green signal

### Q10. The "Financial Management cleanup — waiting on Platform Analytics restart" kanban entry ✅ ANSWERED 2026-06-02
- **Answer:** "i dont know, you restart it you have my approval"
- Started Platform Analytics (port 3071, process 29076). Financial Management cleanup now unblocked.

---

## Lower priority

### Q11. Should `.triage.yaml` and the agent harnesses live in git? ✅ ANSWERED 2026-06-02
- **Answer:** "you decide i think no need to git it yet"
- Skipped — vault stays local-first unversioned. Agent/ folder not git inited.

### Q12. Voice for the orchestrator? ✅ ANSWERED 2026-06-02
- **Answer:** "yes voice will be good"
- All 3 user-facing skills (log-test-result, log-blocker, log-task-completion) designed for voice input: trigger phrases, max 2 clarifying questions, structured output
- `Skills/daily-checkin.md` also voice-friendly

---

## What I will NOT do without explicit approval

- Write to `Incidents/`, `ADRs/`, `Decisions/` (gate_required)
- Commit, push, deploy anything
- Modify production env vars
- Delete vault files
- Run destructive operations (drop tables, force push, rm -rf)
- Start new infrastructure work without an ADR

All of these are in `.triage.yaml` → `policies:` and the gate is the enforcement.
