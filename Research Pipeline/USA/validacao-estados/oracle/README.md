# Independent withholding oracle: US pilot, tax year 2026

Per-pay-period calculator for Federal (FIT, OASDI, Medicare, Additional Medicare, FUTA) and the pilot states CA, NY (+NYC, Yonkers resident), IL, PA, OH, NC, MI, GA, TX, FL: state income tax withholding, employee programs (CA SDI, NY DBL and PFL, PA UC employee) and employer SUI at the new-employer rate. Built 2026-11-06 for option A of `../OPCOES-JUIZ.md`.

## Independence statement
Every parameter was taken from the government's own publication (IRS, EDD, NYS DTF, NYS DFS/WCL, IDOR, IDES, PA DOR/DLI, ODT, ORC, NCDOR, NC DES, MI Treasury/UIA, GA DOR/GDOL, TWC, FL DOR, US DOL). Inputs used:
- `US-compliance/00-official-sources/` (saved official documents, read as raw text or tables);
- `US-compliance/_pipeline/opera_read.py` (only to read live pages: ORC 4141.25, the MI calculator page);
- direct downloads in `_src_live/` (ODT 2025 percentage method and weekly tables, GA guide Dec 2025 and Jun 2026 revisions from the Wayback Machine).

A grep over `00-official-sources/` once printed three lines of `SOURCE-REGISTER.md` (the research team's register); nothing from it was used.

Not opened: any CCG, WTC, DD, payslip, design, release, skill, `_research` (facts, packs, gaps) or `_validation` file, and no payroll-compliance skill. The only file read under `validacao-estados/` before building was `OPCOES-JUIZ.md` (it names the publications). A shared misreading of the same publication is still possible; the official worked examples are the guard against that.

## Files
| File | What |
|---|---|
| `oracle.py` | Pure functions; `calc(case) -> {line: amount, ..., "flags": [...]}` |
| `params_2026.json` | All numbers (no number is hard-coded in `oracle.py`) |
| `params_sources.md` | Source URL/file and page for every key, plus the decisions no publication states |
| `reference_tests.py` | Official worked examples + official-table consistency rows; writes `reference_results.json` |
| `build_cases.py` | Generates `cases.json` (150 cases, 15 per state) and `results.json` (oracle output) |
| `_src_text/`, `_src_live/` | Text extracted from the saved PDFs; files downloaded in this session |

## How to run
```
python reference_tests.py     # pass/fail per publication, writes reference_results.json
python build_cases.py         # writes cases.json and results.json
python oracle.py '{"state":"NY","frequency":"weekly","gross":400,"pay_date":"2026-03-13","state_inputs":{"filing_status":"single","allowances":3}}'
```
Python 3.10+, standard library only (Decimal arithmetic).

## Case format
`state`, `frequency` (daily, weekly, biweekly, semimonthly, monthly, quarterly, semiannual, annual), `gross` (taxable wages of the period, used for every tax), `ytd_gross_before`, `pay_date` (selects GA/OH regime), `federal` (`w4_version` "2020" with `filing_status` single/mfj/hoh, `step2`, `step3`, `step4a`, `step4b`, `step4c`; or "pre2020" with `marital` single/married, `allowances`, `additional`; optional `nra`), `state_inputs` (CA: filing_status single/married/hoh, allowances, est_ded_allowances, method period/annual; NY: filing_status single/married, allowances, locality nyc/yonkers; IL: line1, line2; OH/MI: exemptions; NC: filing_status, allowances, method; GA: filing_status mfj_one_income/single/hoh/mfs/mfj_both_working, dependents; all: additional), optional `employer.sui_rate`, optional `ytd_pfl_contrib_before`.

## Reference tests (2026-11-06)
| Publication | Official examples | Table consistency |
|---|---|---|
| IRS Pub 15-T | 1/1 (NRA example) | 30/30 (wage-bracket rows at midpoint) |
| EDD DE 44 Method B | 6/6 (A-F) | |
| NYS-50-T-NYS | 6/8 | |
| NYS-50-T-NYC | 8/8 | |
| NYS-50-T-Y | 7/8 | |
| IL-700-T | 1/1 | 1/1 |
| NC-30 | 2/2 | |
| GA guide Dec 2025 / Jun-Sep 2026 | 2/2 and 2/2 | |
| ODT weekly tables (2025-10, 2026-08) | none published | 6/6 and 6/6 |

The three NY misses are arithmetic in the publication, reported without tuning: NYS single Ex.2 prints 165 x 0.0753 = 12.43 (product 12.4245, oracle 258.50 vs printed 258.51); NYS married Ex.2 prints 58.80 x 0.070[7] = 4.15 (product 4.15716, oracle 248.12 vs 248.11); Yonkers single Ex.3 prints 3,576.63 x 0.1675 = 599.08 (product 599.085525, oracle 599.09). No single rounding rule reproduces all 24 NY examples.

## Known limits
- No worked example exists for PA (REV-415 01-23 gives only 3.07%), MI (446 gives rate and exemption, the calculator is an online form), OH (tables only), or for SDI/DBL/PFL/SUI. These lines rest on the formula alone; their rounding is not stated, so they are returned unrounded and flagged.
- FUTA credit reduction for CA (5.3%) is the DOL estimate; final only after 2026-11-10. Returned as a separate `futa_credit_reduction_er_pending` line.
- GA: the guide says employers "can begin" the 4.99% regime on 2026-05-11; the oracle switches on pay date 2026-05-11. Annual true-up of the retroactive cut is not modelled.
- OH: regime chosen by pay date (tables "effective August 1, 2026"); school-district and municipal tax out of scope; the 2026 optional computer formula PDF has a broken text layer and was not used (percentage-method tables used instead).
- NY: Yonkers resident only (nonresident 0.50% earnings tax not modelled); NYC/Yonkers have no quarterly tables; DBL weekly cap converted as 0.60 x 52/periods (assumption).
- CA: Method B rate tables loaded for daily, weekly, biweekly, semimonthly, monthly and annual (quarterly/semiannual only through `method: "annual"`).
- SUI is the new-employer rate only (experience rates, construction rates, TX replenishment/obligation components, OH mutualized add-ons and voluntary contributions are not modelled); `employer.sui_rate` overrides it.
- One wage base per case: pre-tax deductions, supplemental-wage flat rates, tips, fringe benefits and multi-state allocation are out of scope. NC has no daily percentage table, so daily NC uses the annualized method.
- FIT is returned unrounded (`fit`) and whole-dollar (`fit_whole_dollar`) because Pub 15-T makes rounding optional.
