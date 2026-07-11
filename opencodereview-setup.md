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
Workflow at `.github/workflows/code-review.yml` (already added to TRACE + Billing).
Set these in each repo's GitHub Secrets/Variables (or org-level):

| Key | Type | Value |
|---|---|---|
| `OCR_LLM_URL` | secret | `https://api.deepseek.com/v1/chat/completions` |
| `OCR_LLM_AUTH_TOKEN` | secret | DeepSeek API key |
| `OCR_LLM_MODEL` | variable | `deepseek-chat` (or `gpt-4o-mini` once Azure GPT-5.4-mini is provisioned) |
| `OCR_LLM_USE_ANTHROPIC` | variable | `false` |

When TRACE/others move `ocr` to Azure GPT-5.4-mini: point `OCR_LLM_URL` at the Azure
deployment endpoint, keep `OCR_LLM_USE_ANTHROPIC=false` (Azure uses the OpenAI protocol).
