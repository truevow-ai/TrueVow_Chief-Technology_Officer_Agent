---
source: TrueVow_Tenant_SETTLE-Service/.opencode/skills/govdata/SKILL.md
service: TrueVow_Tenant_SETTLE-Service
type: settlement-engine
stack: ["python", "nextjs", "postgresql", "alembic", "docker"]
imported: 2026-06-30T22:32:05.049077+00:00
skill_name: govdata
---
# Government Economic & Medical Data APIs (govdata)

**Last Updated:** 2026-06-19
**When to use:** Agent needs public economic, actuarial, medical, demographic, or price-parity data from BLS, SSA, CMS, Census, or BEA to compute damages, benchmark medical costs, or localize settlements.

**Location:** `scripts/scraping-factory/govdata/`

**Output contract:** every helper returns `(settle_rows, raw)`
- `settle_rows: list[SettleRow]` -- SETTLE-ready, one row per (region, metric, code, year)
- `raw: dict` -- provenance and debugging payload (URLs, counts, errors)

---

## Unified schema -- `SettleRow` (15 columns)

```
metric_type        discriminator -- one of 14 valid values (see below)
region             US / state / county / metro / locality name
region_fips        2-digit state | 5-digit county | 5-digit CBSA
occupation_code    SOC (BLS), HCPCS/CPT (CMS), or null
occupation_title   human-readable
age, sex           for SSA life tables
value, unit        numeric + {usd, years, count, index, percent}
source_year
source_agency      BLS | SSA | CMS | CMS-MRF | Census-ACS5 | BEA-SARPP
source_url         exact API or file URL queried
scraped_date       UTC ISO-8601
notes, raw_ref     provenance
```

## `metric_type` -- 14 valid values

| Bucket | Values |
|--------|--------|
| Wage (BLS) | `wage_median`, `wage_mean`, `wage_percentile`, `wage_employment_count` |
| Life (SSA) | `life_expectancy`, `death_probability` |
| Medical (CMS) | `medical_allowed`, `medical_charge`, `medical_negotiated` |
| Demographic (Census ACS) | `demographic_income`, `demographic_age`, `demographic_population`, `demographic_education` |
| Economic (BEA) | `economic_rpp` |

Validated at `SettleRow.__post_init__` -- invalid values raise `ValueError`.

---

## Scripts (7)

| File | Purpose |
|------|---------|
| `govdata_common.py` | `SettleRow`, HTTP layer (requests / urllib auto-detect), FIPS lookups, CSV/JSONL writers |
| `govdata_bls.py` | `get_median_wage`, `bulk_oews_state`, `query_series` -- BLS OEWS wages with national-median fallback |
| `govdata_ssa.py` | `get_life_expectancy`, `get_full_life_table` -- embedded 2023 SSA Period Life Table (SSA blocks scrapers) |
| `govdata_cms_pfs.py` | `get_medicare_allowed`, `bulk_pfs_locality` -- CMS PFS via RVU x GPCI x CF |
| `govdata_cms_chargemaster.py` | `parse_mrf_csv`, `parse_mrf_json`, `discover_mrf_url`, `KNOWN_FL_HOSPITAL_MRF` |
| `govdata_census.py` | `get_state_acs`, `get_county_acs`, `bulk_states_acs`, `bulk_counties_acs` |
| `govdata_bea.py` | `get_rpp`, `bulk_state_rpp` with SARPP zip fallback when no BEA key |

---

## Credentials (all optional)

Set in `.env.local` -- every module falls back to a public path when missing.

```
BLS_API_KEY=         # bumps 25/day -> 500/day (BLS v2 timeseries)
CENSUS_API_KEY=      # higher rate limits (500/IP/day anon -> unlimited)
BEA_API_KEY=         # GUEST deprecated 2023; fallback = SARPP bulk zip
```

Register keys:
- BLS: https://data.bls.gov/registrationEngine/
- Census: https://api.census.gov/data/key_signup.html
- BEA: https://apps.bea.gov/API/signup/

---

## Quickstart -- Python

```python
from scripts.scraping_factory.govdata import SettleRow, write_csv
from scripts.scraping_factory.govdata.govdata_bls import get_median_wage
from scripts.scraping_factory.govdata.govdata_ssa import get_life_expectancy
from scripts.scraping_factory.govdata.govdata_cms_pfs import get_medicare_allowed
from scripts.scraping_factory.govdata.govdata_census import get_county_acs
from scripts.scraping_factory.govdata.govdata_bea import get_rpp

rows = []

# 1) BLS -- RN median wage in Florida
r, _ = get_median_wage(soc="29-1141", state="FL", year=2023)
rows.extend(r)

# 2) SSA -- life expectancy for a 35-year-old male
r, _ = get_life_expectancy(age=35, sex="M")
rows.extend(r)

# 3) CMS PFS -- cervical fusion 22551, FL-Locality-03, facility setting
r, _ = get_medicare_allowed(code="22551", locality="FL-03", setting="facility")
rows.extend(r)  # smoke-test target: value ~ $1,926.61

# 4) Census -- all FL counties demographics
r, _ = get_county_acs(state="FL", year=2023)
rows.extend(r)

# 5) BEA -- FL Regional Price Parity (falls back to SARPP.zip if no key)
r, _ = get_rpp(state="FL", year=2023)
rows.extend(r)  # smoke-test target: value ~ 103.6

write_csv(rows, "logs/govdata_unified.csv")
```

---

## Quickstart -- CLI

```bash
cd scripts/scraping-factory/govdata

# BLS
python govdata_bls.py median --soc 29-1141 --state FL --year 2023

# SSA
python govdata_ssa.py expectancy --age 35 --sex M
python govdata_ssa.py table --sex F

# CMS PFS
python govdata_cms_pfs.py allowed --code 22551 --locality FL-03 --setting facility

# CMS chargemaster
python govdata_cms_chargemaster.py known
python govdata_cms_chargemaster.py discover --domain https://www.tgh.org
python govdata_cms_chargemaster.py csv --path ./tgh_standardcharges.csv --hospital "Tampa General" --fips 12057

# Census ACS
python govdata_census.py state --state FL
python govdata_census.py county --state FL
python govdata_census.py bulk-states --states FL,GA,TX,NY,CA

# BEA
python govdata_bea.py state --state FL --year 2023
python govdata_bea.py bulk --year 2023
python govdata_bea.py zip --year 2023
```

---

## Verified smoke tests

| Source | Call | Expected value |
|--------|------|----------------|
| SSA | 35M life expectancy | ~ 42.26 years (linear interp of 2023 Period Life Table) |
| CMS PFS | CPT 22551, FL-03 (Fort Lauderdale), facility, CY2025 | **$1,876.39** |
| CMS PFS | CPT 22551, FL-99 (Rest of Florida), facility, CY2025 | **$1,761.32** |
| BEA | FL RPP 2023 all-items | **103.636** |
| Census | FL counties 2023 ACS5 | **268 rows** (67 counties x 4 metrics) |

RVU/GPCI/CF values are pulled from the CMS CY2025 Q1 release:
`PPRRVU25_JAN.csv` + `GPCI2025.csv` (inside `rvu25a.zip`). CF=32.3465.

**Locality naming note:** CMS locality 03 is FORT LAUDERDALE, not "Rest of Florida". Rest of Florida is locality 99.

---

## SETTLE alignment

- **Source tagging** -- every row carries `source_url` + `scraped_date` (UTC ISO-8601)
- **No PII** -- all data is aggregate (state/county/metro level)
- **Staleness** -- `source_year` and `scraped_date` let downstream code flag stale rows
- **Raw evidence** -- every helper also returns the unmodified API/file payload in `raw`
- **Discriminator schema** -- drops straight into `external_data` Supabase table with `metric_type` as the primary filter

---

## Fallback behavior

| Module | When API / credential fails | Fallback |
|--------|----------------------------|---------|
| BLS | network error | `OEWS_FALLBACK_NATIONAL_MEDIAN` dict (7 damages-relevant SOCs) |
| SSA | always | Embedded 2023 Period Life Table (SSA blocks scrapers) |
| CMS PFS | always offline | Embedded RVU_2025 + GPCI_2025 tables (authoritative CY2025 values) |
| CMS MRF | link 404 | `discover_mrf_url(domain)` scans common paths + HTML hrefs |
| Census | 429 / network | raises -- surface to caller |
| BEA | no BEA_API_KEY | Bulk `SARPP.zip` download + CSV parse (no key needed) |

---

## Common workflows

**Build a damages-ready row bundle for a single case:**
```python
def build_case_bundle(state: str, soc: str, cpt: str, age: int, sex: str):
    rows = []
    rows.extend(get_median_wage(soc, state)[0])
    rows.extend(get_life_expectancy(age, sex)[0])
    rows.extend(get_medicare_allowed(cpt, locality=f"{state}-03")[0])
    rows.extend(get_state_acs(state)[0])
    rows.extend(get_rpp(state)[0])
    return rows
```

**Nightly national refresh:**
```python
from govdata_bea import bulk_state_rpp
from govdata_census import bulk_states_acs

rpp_rows, _   = bulk_state_rpp(year=2023)
acs_rows, _   = bulk_states_acs(list(STATE_FIPS.keys()), year=2023)
write_csv(rpp_rows + acs_rows, "logs/govdata_nightly.csv")
```
