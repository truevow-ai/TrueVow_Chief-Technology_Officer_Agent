-- Agent State Bucket — Shared cross-session state for all agents
-- Applies to Supabase. Run against the SaaS Admin or Internal Ops project.
-- Tool-agnostic: any agent (opencode, Cursor, Pi) reads/writes via REST API or direct SQL.

CREATE TABLE IF NOT EXISTS agent_state (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    agent_id    TEXT NOT NULL,                          -- e.g. "yasha-orchestrator"
    task_id     TEXT,                                   -- Correlation ID for a task
    state       TEXT NOT NULL DEFAULT 'pending',        -- pending | active | completed | failed
    action      TEXT,                                   -- task-start | file-write | decision | etc.
    detail      TEXT,                                   -- Human-readable description
    service     TEXT,                                   -- Service name
    file_path   TEXT,                                   -- File path if relevant
    verification TEXT DEFAULT 'UNTESTED',               -- VERIFIED | COMPILED | SCAFFOLDED | UNTESTED | ASSUMED
    metadata    JSONB DEFAULT '{}',                     -- Arbitrary extra data
    heartbeat_at TIMESTAMPTZ,                           -- Last alive signal
    started_at  TIMESTAMPTZ DEFAULT now(),
    completed_at TIMESTAMPTZ,
    created_at  TIMESTAMPTZ DEFAULT now(),
    updated_at  TIMESTAMPTZ DEFAULT now()
);

-- Indexes for common queries
CREATE INDEX IF NOT EXISTS idx_agent_state_agent ON agent_state(agent_id);
CREATE INDEX IF NOT EXISTS idx_agent_state_task ON agent_state(task_id);
CREATE INDEX IF NOT EXISTS idx_agent_state_heartbeat ON agent_state(heartbeat_at);
CREATE INDEX IF NOT EXISTS idx_agent_state_service ON agent_state(service);

-- Auto-update updated_at
CREATE OR REPLACE FUNCTION update_agent_state_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = now();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS trg_agent_state_updated ON agent_state;
CREATE TRIGGER trg_agent_state_updated
    BEFORE UPDATE ON agent_state
    FOR EACH ROW
    EXECUTE FUNCTION update_agent_state_timestamp();

-- View: currently active agents
CREATE OR REPLACE VIEW active_agents AS
SELECT agent_id, state, service, heartbeat_at, started_at
FROM agent_state
WHERE state = 'active'
  AND heartbeat_at > now() - INTERVAL '10 minutes'
ORDER BY heartbeat_at DESC;

-- View: agents that have gone silent (no heartbeat in 10 min)
CREATE OR REPLACE VIEW silent_agents AS
SELECT agent_id, state, service, heartbeat_at,
       EXTRACT(EPOCH FROM (now() - heartbeat_at)) / 60 AS minutes_silent
FROM agent_state
WHERE state = 'active'
  AND heartbeat_at < now() - INTERVAL '10 minutes'
ORDER BY heartbeat_at ASC;
