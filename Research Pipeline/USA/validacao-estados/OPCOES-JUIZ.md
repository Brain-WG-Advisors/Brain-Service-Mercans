# Options for the independent "oracle" (judge) - US state validation pilot

Date: 2026-11-06. Pilot: Federal + CA, TX, NY, FL, IL, PA, OH, NC, MI, GA. Survey only; nothing built.
Existing oracle (C37): `_validation/oracle/oracle.py` re-implements the federal method (Pub 15-T) from our facts files, 49 cases, mostly federal; `build_suite.py` labels each reference as official_example / ccg_worked_example / parameter. No state formulas yet.

## 1. Option (a): oracle written from each state's official formula + official worked examples

| State | Publication (2026) | Worked examples? (verified = I read the file) |
|---|---|---|
| CA | EDD "2026 Withholding Schedules - Method B" (DE 44 family) https://edd.ca.gov/siteassets/files/pdf_pub_ctr/26methb.pdf | Verified: Examples A-F (low-income exemption, estimated deductions, weekly to annual) with step results |
| NY | NYS-50-T-NYS (1/26), Method II exact calculation https://www.tax.ny.gov/pdf/publications/withholding/nys50_t_nys.pdf ; Yonkers: https://nystax.gov/pdf/publications/withholding/nys50_t_y.pdf | Verified: 4 examples single + 4 married (NYS); Yonkers/NYC: not read |
| IL | IL-700-T (R-12/25) formula https://tax.illinois.gov/forms/withholding/currentyear/il-700-t-withholding-guide-tables.html | Page shows an "Example" and the formula; PDF not read |
| PA | REV-415 Employer Withholding Guide https://www.pa.gov/agencies/revenue/resources/tax-types-and-information/employer-withholding.html | Not verified (PDF blocked from here). Flat 3.07%; local EIT/LST come from Act 32 collectors, not REV-415 |
| OH | ODT percentage method 2026 https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/employer_withholding/2026%20Withholding%20Tables/WHT_PercentageMethod_2026.pdf | Verified: tables only, no examples; tables effective Aug 1, 2026 (two regimes in the year) https://ohiocpa.com/advocacy/advocacy-news/2026/07/24/effective-august-1--odt-updates-employer-withholding-tables |
| NC | NC-30 https://www.ncdor.gov/income-tax-withholding-tables-and-instructions-employers/open | Verified: percentage method and annualized method, each with a $450 weekly example (result $4) |
| MI | Form 446 Withholding Guide https://www.michigan.gov/taxes/biz-forms/withholding/2026-withholding-tax-forms | Not verified (guide PDF not opened); page lists a "Withholding Tax Calculator" |
| GA | Employer's Tax Guide, rev. June 2026 https://dor.georgia.gov/document/document/2026-employers-tax-guide-updated-june-2026/download | Verified: formula (std deduction, 4.99%, $4,000 per dependent) and tables; examples only in table notes, no full cases. Rate changed retroactively (HB 463), see https://taxnews.ey.com/news/2026-1294-georgia-department-of-revenue-releases-revised-withholding-formula-reflecting-lower-income-tax-rate-for-2026 |
| TX, FL | No state income tax; nothing to compute | n/a |

Employee-side SDI/PFML (CA SDI, NY PFL/DBL), SUI wage bases and rates: each agency's own page (EDD, NYS DFS/WCB, GA DOL, etc.); formula is a rate x wage base, with few or no worked examples. Local: NY Yonkers (NYS-50-T-Y), PA/OH/MI cities: rates in each collector's table; not verified.
Note: CA Method B example arithmetic (e.g. Example B result $2.38) can be replayed by hand, so the official examples work as hard anchors.

## 2. Option (b): open-source engines

| Engine | What it does | Licence / maintenance | Verdict |
|---|---|---|---|
| PolicyEngine-US | Annual household microsimulation; payroll taxes exist only as annual variables (employee_payroll_tax); I found no withholding-per-period variables in the repo tree; state income tax variables for ~50 state folders. https://github.com/PolicyEngine/policyengine-us | AGPL-3.0; pushed 2026-11-06; PyPI 2.104.0 https://pypi.org/project/policyengine-us/ | Annual liability != Pub 15-T/state withholding. Not a withholding oracle |
| OpenFisca-US | Superseded by PolicyEngine-US (fork). Only stale or data repos: 18F prototype last push 2025-03 (archived); PolicyEngine/openfisca-us-data 2026-04 https://github.com/PolicyEngine/openfisca-us-data | AGPL-3.0 | Not usable |
| Tax-Calculator (PSL) | Federal income and payroll taxes, annual, no state tax. https://github.com/PSLmodels/Tax-Calculator | Public-domain style licence (GitHub API says NOASSERTION; check file); pushed 2026-11-05 | Federal annual only |
| taxsim-py | Python port of NBER TAXSIM: federal tax, FICA, state income tax, annual liability for all 50 states + DC to 2025 https://pypi.org/project/taxsim-py/ | MIT; v0.4.1 on 2026-10-21; years to 2025, not 2026 | Annual, no 2026: not a withholding oracle |
| python-taxes | SS, Medicare, federal income tax, 2023-2025 only https://pypi.org/project/python-taxes/ | MIT; v0.7.0 | No state, no 2026 |
| Withhold Right (web) | Pub 15-T + official formulas for 11 states, 2026 tables, in-browser https://withhold-right.pages.dev/about | Closed source as far as found; unknown author | Spot-check only, unaudited |
| Symmetry Tax Engine (commercial) | Real payroll tax engine, all jurisdictions incl. local https://docs.symmetry.com/ste/overview/what-is-the-ste.md | Paid licence | Strongest independence and coverage; cost and approval needed |

I found no maintained open-source library giving per-period withholding for states with 2026 tables.

## 3. Option (c): official calculators as spot-check

| Tool | Scope | Use |
|---|---|---|
| IRS Tax Withholding Estimator https://www.irs.gov/node/70261 | Employee-side, annual estimate, recommends W-4 entries; not a per-period Pub 15-T calculator | Not an oracle (different question) |
| Michigan "Withholding Tax Calculator" (listed on https://www.michigan.gov/taxes/biz-forms/withholding/2026-withholding-tax-forms; blocked from non-US IP) | Employer calculator, behaviour not tested | Possible MI spot-check, to be tested through Opera |
| IL-700-T page formula/tables https://tax.illinois.gov/forms/withholding/currentyear/il-700-t-withholding-guide-tables.html | Tables, not a calculator | Table lookup = cross-check of formula |
| GA, NC, CA, NY, OH, PA | No official employer calculator found in searches (NC/GA/NY searches returned only PDFs). Not exhaustively confirmed | n/a |

## 4. Comparison

| Option | Coverage of pilot | Independence from our research | Effort | Risk | Recommendation |
|---|---|---|---|---|---|
| (a1) Official worked examples as fixed reference cases | Strong CA, NY (state), NC; thin IL, GA; none OH; PA, MI unverified | High (authority-published numbers) | Low: transcribe cases | Few cases; no YTD or cap cases | Yes, first layer |
| (a2) Own oracle coded from each state's formula/tables (like the federal one) | All income-tax states; SUI/SDI/PFML by rate x base; locals partial | Medium: same sources as our research, so a shared misreading would pass | Medium-high: ~8 formulas + tables, mid-year changes (OH Aug 1, GA retro) | Correlated errors with the artifacts | Yes, second layer, written by a different session than the research, using only the publication |
| (b) PolicyEngine / Tax-Calculator / taxsim-py | Annual liability only; no per-period withholding, no 2026 for taxsim | Good, but wrong question | Medium for little gain | False mismatches (annual vs per-period) | No for withholding; at most a sanity check on annual federal tax |
| (b2) Commercial engine (Symmetry STE) | Full incl. locals | Very high | Cost, procurement, data-egress approval | Licence/time | Option if the team funds it; park |
| (c) Official / web calculators | IRS TWE n/a; MI calculator maybe; Withhold Right 11 states | High for MI, medium for web tool | Low, manual per case | Manual, few cases, tool may drift | Use only as sparse spot-check |

## 5. Recommended combination

1. Reference cases from official examples: CA Method B A-F, NY NYS-50-T-NYS (8), NC-30 (2), IL-700-T example, GA table example; label them `official_example` in build_suite.py.
2. State oracle coded from the publication only (no reading of our CCG), same pattern as C37, plus cases for wage-base caps with YTD (SUI, OASDI) and mid-year rate changes (GA before/after 11 May, OH before/after 1 Aug).
3. Spot-check 2-3 cases per state on the MI calculator and Withhold Right (CA, NY, IL, MI, GA, NC, OH are in the 11-state list to be confirmed); disagreements are investigated, not auto-failed.
4. Locals (Yonkers, NYC, PA EIT/LST, OH, MI cities) and employee-side SDI/PFML: keep as parameter checks (rate and base from the collector/agency page); mark confidence below 100% until a second source exists.
5. Do not use PolicyEngine/Tax-Calculator for withholding.

Open items: PA REV-415 and MI 446 examples not verified; Yonkers/NYC and local publications not read; Withhold Right state list not confirmed.
