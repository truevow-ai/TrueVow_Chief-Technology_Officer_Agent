# OpenCodeReview (ocr) — Working Setup

**Status: WORKING.** CLI installed, DeepSeek configured, verified with a real scan
that produced 17 review comments (incl. a critical FTS5 trigger bug + SQL-injection flags).

## Install (per machine)
```
npm install -g @alibaba-group/open-code-review    # provides `ocr`
```

## Configure LLM — DeepSeek (OpenAI-compatible)
```
ocr config set provider deepseek
ocr config set custom_providers.deepseek.url https://api.deepseek.com/v1
ocr config set custom_providers.deepseek.protocol openai
ocr config set providers.deepseek.model deepseek-chat
ocr config set providers.deepseek.api_key <DEEPSEEK_API_KEY>   # from Infisical, NOT committed
ocr config set providers.deepseek.auth_header authorization
ocr llm test        # -> ✓ Connection test successful
```
Config lives at `~/.opencodereview/config.json` (contains the key — never commit it).

## Usage
```
ocr review --from main --to <branch>          # diff review
ocr scan --path <dir-or-file>                 # full-file audit
ocr scan --path app/ --max-tokens-budget 200000   # CAP TOKENS — a 558-line file used ~626K tokens
```

## Cost warning
deepseek-v4-flash with tool-use is thorough but token-heavy (~626K tokens for one 558-line
file, 2m39s). ALWAYS set `--max-tokens-budget` in CI. Consider `--no-plan --no-summary` for speed.

## CI (GitHub Actions) — per repo
Workflow at `.github/workflows/code-review.yml` (added to TRACE + Billing).
Keys are prefixed `OPENCODEREVIEW_` (NOT `OCR_`) to avoid confusion with TRACE's OCR tooling.

### Where the CI key comes from
Only ONE value is secret — the LLM API key. It already exists in your repos:
`DEEPSEEK_API_KEY` in `TrueVow_Sales_Ops_Service/.env.local` (starts `sk-fc78…`),
or regenerate at **platform.deepseek.com → API Keys**. Once Infisical is live, pull it from there.
The other three are not secret.

### The four GitHub keys
| GitHub key | Kind | Value |
|---|---|---|
| `OPENCODEREVIEW_LLM_URL` | secret | `https://api.deepseek.com/v1/chat/completions` |
| `OPENCODEREVIEW_LLM_AUTH_TOKEN` | secret | the DeepSeek API key |
| `OPENCODEREVIEW_LLM_MODEL` | variable | `deepseek-chat` (or the Azure GPT-5.4-mini deployment later) |
| `OPENCODEREVIEW_LLM_USE_ANTHROPIC` | variable | `false` |

### Wire into GitHub — UI
Repo → **Settings → Secrets and variables → Actions**:
- **Secrets** tab → *New repository secret*: add `OPENCODEREVIEW_LLM_URL` and `OPENCODEREVIEW_LLM_AUTH_TOKEN`
- **Variables** tab → *New repository variable*: add `OPENCODEREVIEW_LLM_MODEL` and `OPENCODEREVIEW_LLM_USE_ANTHROPIC`

### Wire into GitHub — gh CLI (faster; org-wide once)
```
# Whole org at once (applies to all 13 repos):
gh secret   set OPENCODEREVIEW_LLM_URL          --org truevow-ai --visibility all --body "https://api.deepseek.com/v1/chat/completions"
gh secret   set OPENCODEREVIEW_LLM_AUTH_TOKEN   --org truevow-ai --visibility all --body "<paste-deepseek-key>"
gh variable set OPENCODEREVIEW_LLM_MODEL        --org truevow-ai --body "deepseek-chat"
gh variable set OPENCODEREVIEW_LLM_USE_ANTHROPIC --org truevow-ai --body "false"
```
Never paste the key into chat or a commit — enter it directly in the GitHub UI or the `gh` command.

When moving `ocr` to Azure GPT-5.4-mini: set `OPENCODEREVIEW_LLM_URL` to the Azure
deployment endpoint, keep `OPENCODEREVIEW_LLM_USE_ANTHROPIC=false` (Azure uses the OpenAI protocol).
