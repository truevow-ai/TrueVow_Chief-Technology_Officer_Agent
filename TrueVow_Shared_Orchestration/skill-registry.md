# TrueVow Agent Skill Registry

> Auto-generated catalog of all available skills, personas, and tools in the ecosystem.

## Osmani Agent Skills (24 skills)

### META
| Skill | Path | Description |
|-------|------|-------------|
| using-agent-skills | `skills/using-agent-skills/` | Maps work to the right skill via flowchart |

### DEFINE
| Skill | Path | Description |
|-------|------|-------------|
| interview-me | `skills/interview-me/` | One-question-at-a-time stakeholder interview |
| idea-refine | `skills/idea-refine/` | Divergent/convergent thinking with frameworks |
| spec-driven-development | `skills/spec-driven-development/` | PRD before code - structured specification |

### PLAN
| Skill | Path | Description |
|-------|------|-------------|
| planning-and-task-breakdown | `skills/planning-and-task-breakdown/` | Decompose specs into verifiable tasks |

### BUILD
| Skill | Path | Description |
|-------|------|-------------|
| incremental-implementation | `skills/incremental-implementation/` | Thin vertical slices, one at a time |
| test-driven-development | `skills/test-driven-development/` | Red-Green-Refactor cycle |
| context-engineering | `skills/context-engineering/` | Feed agents the right context |
| source-driven-development | `skills/source-driven-development/` | Cite official documentation |
| doubt-driven-development | `skills/doubt-driven-development/` | Adversarial fresh-context review |
| frontend-ui-engineering | `skills/frontend-ui-engineering/` | Components, accessibility, state |
| api-and-interface-design | `skills/api-and-interface-design/` | Contract-first, Hyrum's Law |

### VERIFY
| Skill | Path | Description |
|-------|------|-------------|
| browser-testing-with-devtools | `skills/browser-testing-with-devtools/` | Chrome DevTools MCP for runtime testing |
| debugging-and-error-recovery | `skills/debugging-and-error-recovery/` | Five-step triage process |

### REVIEW
| Skill | Path | Description |
|-------|------|-------------|
| code-review-and-quality | `skills/code-review-and-quality/` | Five-axis review (correctness, readability, architecture, security, performance) |
| code-simplification | `skills/code-simplification/` | Reduce complexity, preserve behavior |
| security-and-hardening | `skills/security-and-hardening/` | OWASP Top 10 hardening |
| performance-optimization | `skills/performance-optimization/` | Measure-first optimization |

### SHIP
| Skill | Path | Description |
|-------|------|-------------|
| git-workflow-and-versioning | `skills/git-workflow-and-versioning/` | Trunk-based dev, atomic commits |
| ci-cd-and-automation | `skills/ci-cd-and-automation/` | Shift Left, feature flags |
| deprecation-and-migration | `skills/deprecation-and-migration/` | Code-as-liability |
| documentation-and-adrs | `skills/documentation-and-adrs/` | Architecture Decision Records |
| observability-and-instrumentation | `skills/observability-and-instrumentation/` | Logging, tracing, alerting |
| shipping-and-launch | `skills/shipping-and-launch/` | Pre-launch checklist, rollback plans |

## Agent Personas (4)

| Persona | File | Role |
|---------|------|------|
| code-reviewer | `agents/code-reviewer.md` | Senior Staff Engineer - five-axis review |
| test-engineer | `agents/test-engineer.md` | QA Specialist - Prove-It pattern |
| security-auditor | `agents/security-auditor.md` | Security Engineer - OWASP + vulnerability detection |
| web-performance-auditor | `agents/web-performance-auditor.md` | Web Perf Engineer - Core Web Vitals |

## Slash Commands (8)

| Command | Phase | What it does |
|---------|-------|--------------|
| `/spec` | DEFINE | Write structured PRD |
| `/plan` | PLAN | Break into tasks with acceptance criteria |
| `/build` | BUILD | Implement one task at a time (TDD) |
| `/test` | VERIFY | Prove-It: reproduce, fix, verify |
| `/review` | REVIEW | Five-axis code review |
| `/webperf` | REVIEW | Lighthouse/CrUX performance audit |
| `/code-simplify` | REVIEW | Reduce complexity |
| `/ship` | SHIP | Fan-out pre-launch review (GO/NO-GO) |

## Tool Capabilities

### Codebase Memory (5 tools)
- `remember` - Store architecture, patterns, bugs, decisions
- `recall` - Full-text search with category/tag/file filters
- `update_memory` - Update existing memories
- `forget` - Delete outdated memories
- `project_summary` - Overview at session start

### Agent Reach (13 platforms)
- Web, YouTube, RSS, Exa Search, GitHub, V2EX - zero config
- Twitter/X, Reddit, XiaoHongShu, Bilibili, LinkedIn, Xueqiu, Xiaoyuzhou - optional config

### SkillSpector (68 vulnerability patterns)
- 17 categories: prompt injection, data exfiltration, supply chain, MCP poisoning, and more
- Static + LLM two-stage analysis
- Risk scoring 0-100 with SAFE/CAUTION/DO_NOT_INSTALL verdicts
