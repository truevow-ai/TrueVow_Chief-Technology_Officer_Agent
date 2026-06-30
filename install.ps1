# TrueVow Agent Ecosystem - One-Command Install
# Skills are the new apps. This installs the full stack.
# Run: powershell -ExecutionPolicy Bypass -File install.ps1

param(
    [switch]$SkillsOnly,
    [switch]$MemoryOnly,
    [switch]$ReachOnly,
    [switch]$SecurityOnly,
    [switch]$SkipClone,
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"
$ROOT = $PSScriptRoot
$AGENT_TOOLS = Join-Path $ROOT "TrueVow_Shared_Agent_Tools"

Write-Host "`n=== TrueVow Agent Ecosystem Installer ===`n" -ForegroundColor Cyan
Write-Host "Skills are the new apps. This installs all 5 pillars:`n" -ForegroundColor White
Write-Host "  1. Osmani Agent Skills    - 24 skills + 4 personas + 8 slash commands"
Write-Host "  2. Codebase Memory         - Persistent repo memory (MCP server)"
Write-Host "  3. Agent Reach             - Live web eyes (13 platforms)"
Write-Host "  4. NVIDIA SkillSpector     - Security guardrail (68 patterns)"
Write-Host "  5. Obsidian Bridge         - Knowledge management sync`n"

if ($DryRun) {
    Write-Host "[DRY RUN] No changes will be made.`n" -ForegroundColor Yellow
}

# ── Clone Stage ──
if (-not $SkipClone) {
    Write-Host "--- Cloning Repositories ---" -ForegroundColor Green
    $repos = @(
        @{Name="agent-skills";     Url="https://github.com/addyosmani/agent-skills.git"},
        @{Name="codebase-memory";  Url="https://github.com/yuga-hashimoto/codebase-memory.git"},
        @{Name="agent-reach";      Url="https://github.com/Panniantong/Agent-Reach.git"},
        @{Name="skillspector";     Url="https://github.com/NVIDIA/SkillSpector.git"}
    )

    if (-not (Test-Path $AGENT_TOOLS)) {
        New-Item -ItemType Directory -Path $AGENT_TOOLS -Force | Out-Null
    }

    foreach ($repo in $repos) {
        $dest = Join-Path $AGENT_TOOLS $repo.Name
        if (Test-Path $dest) {
            Write-Host "  [SKIP] $($repo.Name) already exists" -ForegroundColor DarkGray
        } else {
            Write-Host "  [CLONE] $($repo.Name)..." -ForegroundColor Gray
            if (-not $DryRun) {
                git clone $repo.Url $dest 2>&1 | Out-Null
                Write-Host "  [OK] $($repo.Name)" -ForegroundColor Green
            }
        }
    }
}

# ── Pillar 1: Osmani Agent Skills ──
if ($SkillsOnly -or (-not ($MemoryOnly -or $ReachOnly -or $SecurityOnly))) {
    Write-Host "`n--- Pillar 1: Osmani Agent Skills ---" -ForegroundColor Green
    $skillsDir = Join-Path $AGENT_TOOLS "agent-skills\skills"
    if (Test-Path $skillsDir) {
        $skillCount = (Get-ChildItem -Path $skillsDir -Directory).Count
        Write-Host "  [OK] $skillCount skills available in TrueVow_Shared_Agent_Tools/agent-skills/skills/"
        Write-Host "  [INFO] Slash commands at TrueVow_Shared_Agent_Tools/agent-skills/.claude/commands/"
        Write-Host "  [INFO] Agent personas at TrueVow_Shared_Agent_Tools/agent-skills/agents/"
        Write-Host "  [INFO] Reference checklists at TrueVow_Shared_Agent_Tools/agent-skills/references/"
    } else {
        Write-Host "  [WARN] Skills not found - run without --skipClone" -ForegroundColor Yellow
    }
}

# ── Pillar 2: Codebase Memory ──
if ($MemoryOnly -or (-not ($SkillsOnly -or $ReachOnly -or $SecurityOnly))) {
    Write-Host "`n--- Pillar 2: Codebase Memory ---" -ForegroundColor Green
    $memDir = Join-Path $AGENT_TOOLS "codebase-memory"
    if (-not $DryRun -and (Test-Path $memDir)) {
        Push-Location $memDir
        try {
            npm install 2>&1 | Out-Null
            npm run build 2>&1 | Out-Null
            Write-Host "  [OK] Codebase Memory MCP server built"
        } catch {
            Write-Host "  [WARN] Build failed - check Node.js version (>=18 required)" -ForegroundColor Yellow
        } finally {
            Pop-Location
        }
    }

    # Create .codebase-memory directory for the DB
    $memDbDir = Join-Path $ROOT "TrueVow_Shared_Codebase_Memory"
    if (-not (Test-Path $memDbDir)) {
        New-Item -ItemType Directory -Path $memDbDir -Force | Out-Null
        Write-Host "  [OK] TrueVow_Shared_Codebase_Memory/ directory created"
    }

    Write-Host "  [INFO] MCP Config: TrueVow_Shared_Orchestration/mcp-config.json"
    Write-Host "  [INFO] 5 tools: remember, recall, update_memory, forget, project_summary"
}

# ── Pillar 3: Agent Reach ──
if ($ReachOnly -or (-not ($SkillsOnly -or $MemoryOnly -or $SecurityOnly))) {
    Write-Host "`n--- Pillar 3: Agent Reach ---" -ForegroundColor Green
    $reachDir = Join-Path $AGENT_TOOLS "agent-reach"
    if (-not $DryRun -and (Test-Path $reachDir)) {
        try {
            & py -3 -m pip install $reachDir 2>&1 | Out-Null
            Write-Host "  [OK] Agent Reach Python package installed"
            try {
                agent-reach install --env=auto --safe 2>&1 | Out-Null
                Write-Host "  [OK] Agent Reach channels configured"
            } catch {
                Write-Host "  [INFO] Run 'agent-reach install --env=auto' to configure channels"
            }
        } catch {
            Write-Host "  [WARN] pip install failed - check Python 3.10+" -ForegroundColor Yellow
        }
    }
}

# ── Pillar 4: NVIDIA SkillSpector ──
if ($SecurityOnly -or (-not ($SkillsOnly -or $MemoryOnly -or $ReachOnly))) {
    Write-Host "`n--- Pillar 4: NVIDIA SkillSpector ---" -ForegroundColor Green
    if (-not $DryRun) {
        try {
            & py -3 -m pip install "skillspector[mcp]" 2>&1 | Out-Null
            Write-Host "  [OK] SkillSpector installed with MCP support"
            Write-Host "  [INFO] 68 vulnerability patterns across 17 categories"
            Write-Host "  [INFO] Run: skillspector scan TrueVow_Shared_Agent_Tools/agent-skills/skills/ --recursive"
        } catch {
            Write-Host "  [WARN] SkillSpector install failed - try: pip install skillspector[mcp]" -ForegroundColor Yellow
        }
    }
}

# ── Pillar 5: Obsidian Bridge ──
Write-Host "`n--- Pillar 5: Obsidian Bridge ---" -ForegroundColor Green
$vaultDir = Join-Path $ROOT "TrueVow_Knowledge"
if (Test-Path $vaultDir) {
    Write-Host "  [OK] Obsidian vault: TrueVow_Knowledge/"
    Write-Host "  [INFO] Run: python TrueVow_Shared_Orchestration/obsidian-bridge.py to sync"
    Write-Host "  [INFO] Run: python TrueVow_Shared_Orchestration/obsidian-bridge.py --watch for live sync"
} else {
    Write-Host "  [WARN] Obsidian vault not found at TrueVow_Knowledge/" -ForegroundColor Yellow
}

# ── Orchestration Layer ──
Write-Host "`n--- Orchestration Layer ---" -ForegroundColor Green
$orchDir = Join-Path $ROOT "TrueVow_Shared_Orchestration"
if (Test-Path $orchDir) {
    $files = Get-ChildItem $orchDir -File | Measure-Object | Select-Object -ExpandProperty Count
    Write-Host "  [OK] $files orchestration files ready"
    Write-Host "  [INFO] Config: TrueVow_Shared_Orchestration/config.yaml"
    Write-Host "  [INFO] MCP: TrueVow_Shared_Orchestration/mcp-config.json"
    Write-Host "  [INFO] Monitor: python TrueVow_Shared_Orchestration/monitor.py"
    Write-Host "  [INFO] Orchestrator: python TrueVow_Shared_Orchestration/orchestrator.py doctor"
}

# ── Summary ──
Write-Host "`n=== Installation Complete ===`n" -ForegroundColor Cyan
Write-Host "Quick Start:" -ForegroundColor White
Write-Host "  python TrueVow_Shared_Orchestration/orchestrator.py doctor        Full diagnostic"
Write-Host "  python TrueVow_Shared_Orchestration/monitor.py                    Health check"
Write-Host "  python TrueVow_Shared_Orchestration/obsidian-bridge.py            Sync to Obsidian"
Write-Host "  skillspector scan TrueVow_Shared_Agent_Tools/agent-skills/skills/ --recursive   Security audit"
Write-Host "  agent-reach doctor                                 Check web channels"

Write-Host "`nMCP Configuration (add to .cursor/mcp.json):" -ForegroundColor White
Write-Host "  Copy from: TrueVow_Shared_Orchestration/mcp-config.json"

Write-Host "`nSkills are the new apps. The ecosystem is ready.`n" -ForegroundColor Cyan
