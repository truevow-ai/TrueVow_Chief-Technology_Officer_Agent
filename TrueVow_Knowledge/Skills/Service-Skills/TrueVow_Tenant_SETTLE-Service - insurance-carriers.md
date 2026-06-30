---
source: TrueVow_Tenant_SETTLE-Service/.opencode/skills/insurance-carriers/SKILL.md
service: TrueVow_Tenant_SETTLE-Service
type: settlement-engine
stack: ["python", "nextjs", "postgresql", "alembic", "docker"]
imported: 2026-06-30T22:32:05.053063+00:00
skill_name: insurance-carriers
---
# Insurance Carrier Data Sources -- Free Public Channels

**Last Updated:** 2026-06-19
**When to use:** A SETTLE thread needs carrier intelligence, building a carrier profile for a settlement intelligence dashboard, plaintiff-side negotiation prep, compiling industry-wide reserves benchmarks, or cross-referencing complaint indices with carrier financial strength.

**Do NOT use for:** Live policy lookups (private), individual claim status, NAIC Schedule P at insurer-line granularity (paid via NAIC FDR), or proprietary verdict databases (Westlaw JVR, Lex Machina, VerdictSearch -- all paid).

**Four free public ecosystems:**
- **NAIC complaint indices** (via Texas TDI Socrata proxy)
- **SEC EDGAR filings** + XBRL loss reserves
- **Florida OIR** public records and industry reports
- **CourtListener** bad-faith verdicts

Returns raw native data per source (per SETTLE flexible-schema posture). Every row source-tagged with `_source_url` and `_scraped_at`.

---

## Why Texas TDI for NAIC complaint data

NAIC's Consumer Information Source (`content.naic.org`) is a Tableau-backed UI with no public API. But Texas TDI republishes the same NAIC-derived complaint index data via a Socrata Open Data API. Because every major U.S. carrier operating nationally also operates in Texas, this gives you a free programmatic proxy for NAIC complaint indices for the entire industry.

The complaint index is calculated as: `(carrier's share of complaints) / (carrier's share of policies in force)` for a given line. Average = 1.00. Index > 1.0 = more complaints than peers. Index < 1.0 = fewer.

---

## Scripts location

All scripts live in `scripts/scraping-factory/insurance-carrier/`:

| Script | Purpose |
|--------|---------|
| `naic_complaints.py` | Texas TDI / NAIC complaint index + raw complaints |
| `sec_edgar_filings.py` | SEC EDGAR company resolution, filing lists, full-text search |
| `sec_edgar_reserves.py` | SEC EDGAR XBRL loss reserves extraction |
| `fl_oir_filings.py` | Florida OIR IRFS search + industry reports |
| `courtlistener_bad_faith.py` | CourtListener bad-faith opinion search |
| `carrier_profile.py` | Composite profile builder (calls all above) |

---

## Operations

**NAIC complaint indices:**
```bash
python naic_complaints.py index --carrier "STATE FARM" --line Automobile --limit 50
python naic_complaints.py raw --coverage Automobile --finding Confirmed --after 2024-01-01
```

```python
from naic_complaints import get_complaint_index
rows = get_complaint_index(carrier="GEICO", line_of_coverage="Automobile", limit=20)
```

**SEC EDGAR filings + full-text search:**
```bash
python sec_edgar_filings.py company --ticker PGR
python sec_edgar_filings.py filings --cik 0000080661 --form 10-K --limit 5
python sec_edgar_filings.py search --query "loss development triangle" --form 10-K --start 2024-01-01 --end 2024-12-31
python sec_edgar_filings.py download --accession 0000080661-26-000086
```

**Common carrier CIKs:**
- Allstate (ALL): `0000899051`
- Progressive (PGR): `0000080661`
- Travelers (TRV): `0000086312`
- Hartford (HIG): `0000874766`
- MetLife (MET): `0001099219`
- Berkshire (BRK.A) [GEICO parent]: `0001067983`
- USAA: `0000200245`
- State Farm: NOT publicly traded (mutual)

**SEC EDGAR loss reserves (XBRL):**
```bash
python sec_edgar_reserves.py reserves --cik 0000080661
python sec_edgar_reserves.py concept --cik 0000080661 --concept LiabilityForUnpaidClaimsAndClaimsAdjustmentExpenseNet
python sec_edgar_reserves.py frame --concept LiabilityForUnpaidClaimsAndClaimsAdjustmentExpenseNet --period CY2023Q4I
```

The `reserves` command tries these concepts in order until one resolves:
`LiabilityForUnpaidClaimsAndClaimsAdjustmentExpense`, `...Net`, `LiabilityForClaimsAndClaimsAdjustmentExpense`, `LiabilityForUnpaidPolicyClaimsAndClaimsAdjustmentExpense`.

**Florida OIR:**
```bash
python fl_oir_filings.py categories
python fl_oir_filings.py reports
python fl_oir_filings.py irfs --company "STATE FARM"
```

When the IRFS portal is needed, route to a Browser tool (Playwright/Selenium) -- the ASP.NET viewstate flow is brittle to scrape with raw HTTP.

**CourtListener bad-faith verdicts:**
```bash
python courtlistener_bad_faith.py search --carrier "State Farm" --jurisdiction Florida --limit 20
python courtlistener_bad_faith.py search --carrier "State Farm" --jurisdiction Florida --after 2020-01-01
python courtlistener_bad_faith.py punitive --carrier "Progressive" --jurisdiction Florida
python courtlistener_bad_faith.py opinion --id 5297875
```

**Composite carrier profile:**
```bash
python carrier_profile.py --carrier "Progressive" --ticker PGR
python carrier_profile.py --carrier "State Farm" --naic 25178
```

Returns a dict with keys: `meta`, `naic_complaint_index`, `sec_company`, `sec_filings_10k`, `sec_loss_reserves`, `fl_oir_categories`, `bad_faith_opinions`, `errors`.

---

## Auth & credentials

| Variable | Required | Purpose |
|----------|----------|---------|
| `SEC_EDGAR_USER_AGENT` | Yes (production) | Format: `Your Name your.email@example.com` |
| `COURTLISTENER_API_TOKEN` | Optional (recommended) | Free token from courtlistener.com |
| `TX_SOCRATA_APP_TOKEN` | Optional | ~100x rate limit lift on TDI datasets |

---

## SETTLE alignment notes

1. **Source tagging is mandatory.** Every row includes `_source_url` and `_scraped_at`. Don't strip these.
2. **No PII.** None of these sources expose individual claimant data.
3. **Sample-size disclosure.** Surface `n` / `count` to the consumer.
4. **Confidence bands, not predictions.** This skill returns raw data; downstream code outputs ranges with sample sizes.
5. **Staleness flags.** Tag consuming dashboards with `source_year` or `period_end` for every datum.

---

## Mutual carriers (no SEC filings)

State Farm, USAA, Liberty Mutual, Nationwide, Farmers -- these are mutual/private. The skill handles this gracefully: `sec_company` returns null with an error note, while `naic_complaint_index` and `bad_faith_opinions` remain populated.

---

## Common workflows

**Compare bad-faith exposure:**
```python
import courtlistener_bad_faith as cl
sf = cl.search_bad_faith("State Farm", jurisdiction="Florida", page_size=1)
pg = cl.search_bad_faith("Progressive", jurisdiction="Florida", page_size=1)
print(f"State Farm FL bad-faith opinions: {sf['count']}")
print(f"Progressive FL bad-faith opinions: {pg['count']}")
```

**Loss reserves growth:**
```python
import sec_edgar_reserves as r
data = r.get_loss_reserves("0000080661")
fy_data = [s for s in data["series"] if s["fiscal_period"] == "FY"][:5]
for row in fy_data:
    print(f"{row['fiscal_year']}: ${row['value_usd']:,}")
```

**Worst complaint indices:**
```python
import naic_complaints as n
rows = n.get_complaint_index(line_of_coverage="Automobile", limit=1000)
worst = [r for r in rows if r["year"] == "2023" and float(r.get("col3") or 0) > 1.0]
worst.sort(key=lambda r: float(r["col3"]), reverse=True)
for r in worst[:10]:
    print(r["company_name"], r["col3"])
```

**Full carrier profile:**
```python
from carrier_profile import build_carrier_profile
profile = build_carrier_profile("Progressive", ticker="PGR")
```

---

## Dependencies

- Python 3.9+
- `requests` (`pip install requests`)
