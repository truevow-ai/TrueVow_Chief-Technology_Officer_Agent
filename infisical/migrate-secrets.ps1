# Infisical migration helper — pushes .env.local secrets to Infisical.
# Usage: .\infisical\migrate-secrets.ps1 -RepoPath "TrueVow_Tenant_TRACE_Service"
# Requires: infisical CLI installed + logged in to the server.
# NEVER commit this file with real INFISICAL_TOKEN.

param(
    [Parameter(Mandatory=$true)]
    [string]$RepoPath,
    [string]$Env = "development",     # development | staging | production
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"
$RepoPath = Resolve-Path $RepoPath
$envFile = Join-Path $RepoPath ".env.local"

if (-not (Test-Path $envFile)) {
    Write-Host "No .env.local found in $RepoPath — nothing to migrate."
    exit 0
}

Write-Host "Migrating secrets from $envFile (env: $Env)..."

$migrated = 0
$skipped = 0

foreach ($line in Get-Content $envFile -ErrorAction SilentlyContinue) {
    $trimmed = $line.Trim()
    if ($trimmed -match '^#|^$') { continue }
    if ($trimmed -match '^(export\s+)?([A-Z_a-z][A-Z0-9_a-z]*)=(.*)$') {
        $key = $Matches[2]
        $value = $Matches[3].Trim('"').Trim("'")
        if ($DryRun) {
            Write-Host "  [dry-run] $key = $($value.Substring(0, [Math]::Min(20,$value.Length)))..."
            $migrated++
        } else {
            # Use `infisical secrets set` — key passed as arg, value piped via stdin
            # so the secret never appears in `ps` output.
            $result = $value | & infisical secrets set $key --env $Env --plain 2>&1
            if ($LASTEXITCODE -eq 0) {
                $migrated++
            } else {
                Write-Warning "  FAILED: $key — $($result -join ' ')"
                $skipped++
            }
        }
    }
}

Write-Host "Done. Migrated: $migrated, Skipped: $skipped"

# Mark the file as retired
if (-not $DryRun) {
    $content = Get-Content $envFile -Raw
    $content = "# Migrated to Infisical — not used. Delete after verifying `infisical run` works.`n$content"
    Set-Content -Path $envFile -Value $content -NoNewline
    Write-Host ".env.local retired (migration marker added at top)."
}
