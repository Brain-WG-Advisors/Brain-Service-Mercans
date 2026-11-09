# params_2026.json: source of every number

Built 2026-11-06 from official publications only. "SRC/" = `US-compliance/00-official-sources/` (government documents saved earlier, read here as raw documents). "LIVE/" = `validacao-estados/oracle/_src_live/` (downloaded in this session). Page numbers are the page printed on the document; "PDF p." is the page index of the file when it differs.

## Federal

| Key | Value | Source | Where |
|---|---|---|---|
| `federal.fit.annual_tables.standard.*`, `.checkbox.*` | Annual Percentage Method tables (MFJ, Single/MFS, HOH; STANDARD and Step-2 Checkbox) | IRS Pub 15-T (2026), https://www.irs.gov/pub/irs-pdf/p15t.pdf; SRC/ccg-sources/FED/FED_IRS-p15t-2026_2026-11-02.pdf | p.12, "2026 Percentage Method Tables for Automated Payroll Systems" |
| `federal.fit.w4_2020_step1g_std_deduction` | 12,900 MFJ / 8,600 other | same | p.10, Worksheet 1A line 1g |
| `federal.fit.pre2020_allowance_value` | 4,300 | same | p.10, Worksheet 1A line 1k |
| `federal.fit.nra_addition_pre2020_w4` | weekly 226.90 ... annual 11,800 | same | PDF p.6, Table 1 |
| `federal.fit.nra_addition_2020_w4` | weekly 309.60 ... annual 16,100 | same | PDF p.7, Table 2 |
| FIT rounding (optional whole dollar) | "may ... round the tax for the pay period to the nearest dollar ... used consistently" | same | p.9, "Rounding" |
| `federal.oasdi.rate_*`, `wage_base` | 6.2% / 184,500 | IRS Pub 15 (2026), https://www.irs.gov/pub/irs-pdf/p15.pdf; SRC/ccg-sources/FED/FED_IRS-p15-2026_2026-11-02.pdf | PDF p.2 (What's New) and PDF p.29 (section 9, "Tax rates and the social security wage base limit") |
| `federal.medicare.rate_*` | 1.45% | same | PDF p.29 |
| `federal.addl_medicare` | 0.9% on wages over 200,000 in the calendar year, employee only | same | PDF p.30, "Additional Medicare Tax withholding" |
| FICA to the cent | rounding to the nearest cent each time payroll is figured (fractions-of-cents adjustment) | same | PDF p.40 |
| `federal.futa.gross_rate`, `max_credit`, `net_rate`, `wage_base` | 6.0%, 5.4%, 0.6%, 7,000 | same | PDF p.44, section 14 "Figuring FUTA tax"; wage base also PDF p.29 |
| `federal.futa.credit_reduction_pending_2026_11_10.CA` | 0.053 (1.5% advance + 0% 2.7 add-on + 3.8% estimated BCR add-on); PENDING | DOL/ETA, "Potential 2026 FUTA Credit Reductions" (dated 2026-01-15), https://oui.doleta.gov/unemploy/docs/potential_credit_states_2026.xlsx; SRC/ccg-sources/FED/FED_DOL-potential_credit_states_2026_2026-11-02.xlsx | sheet 1, row "California". Only CA and Virgin Islands listed: no other pilot state. Final only if the advance is not repaid by 2026-11-10 |

## California (EDD DE 44 Rev. 52 (4-26), "California Employer's Guide 2026" (EDD publication DE 44; saved copy SRC/pdfs/CA/de44_wb.pdf, URL of the saved copy not recorded in the file))

| Key | Value | Where |
|---|---|---|
| `CA.pit.low_income_exemption` | Table 1 | p.46 (PDF p.54) Method B Table 1 |
| `CA.pit.estimated_deduction_per_allowance_table` | Table 2 (>10: one-allowance amount x number) | p.46 Table 2 and footnote 2 |
| `CA.pit.standard_deduction` | Table 3 | p.47 (PDF p.55) Table 3 |
| `CA.pit.exemption_allowance_credit_table` | Table 4 (>10: one-allowance amount x number) | p.47 Table 4 and footnote 1 |
| `CA.pit.rate_tables.annual/daily` | Tables 5-10 | p.48 (PDF p.56) |
| `CA.pit.rate_tables.semimonthly/monthly` | Tables 17-22 | p.50 (PDF p.58) |
| `CA.pit.rate_tables.weekly/biweekly` | Tables 23-28 | p.51 (PDF p.59) |
| Method B steps, Examples A-F | | pp.43-45 (PDF pp.51-53) |
| `CA.sdi.rate_ee` 1.3%, no wage limit | | inside cover p.ii (PDF p.2) and p.8 (PDF p.16) |
| `CA.sui.wage_base` 7,000; `new_employer_rate` 3.4% | | p.ii and p.8 |
| `CA.ett` 0.1% on 7,000 | | p.ii and p.8 |

Tables 1-4 were read with pdfplumber cell extraction (the text layer interleaves columns); every value was cross-checked against Examples A-F.

## New York

| Key | Value | Source | Where |
|---|---|---|---|
| `NY.pit_state.deduction_table_B`, `exemption_table_C` | | NYS-50-T-NYS (1/26), https://www.tax.ny.gov/pdf/publications/withholding/nys50_t_nys.pdf; SRC/pdfs/NY/nys50tnys_wb.pdf | p.14, Tables B and C (Table A = B + n x C, checked for all 11 columns) |
| `NY.pit_state.method2.single.*` | Tables II-A to II-E and annual schedule | same | p.17 |
| `NY.pit_state.method2.married.*` | | same | p.19 |
| `NY.pit_state.method3` | 10.45% / 11.10% / 11.70% | same | p.22 |
| Examples (8) | | same | pp.16 and 18 |
| `NY.pit_nyc.*` | Tables A-C, II-A to II-E, annual (single = married) | NYS-50-T-NYC (1/26) (NYS DTF); SRC/ccg-sources/NY/NY_DTF_NYS-50-T-NYC_1-26_2026-11-02.pdf | pp.24-26; examples p.27 |
| `NY.pit_yonkers_resident.factor_of_nys_withholding` | 16.75% of NYS Method II/III result | NYS-50-T-Y (1/26), https://www.tax.ny.gov/pdf/publications/withholding/nys50_t_y.pdf; SRC/ccg-sources/NY/NY_DTF_NYS-50-T-Y_1-26_2026-11-02.pdf | pp.16-19 (Step 5) and p.22; examples pp.16, 18 |
| `NY.dbl` | 0.5% of wages, not over $0.60 per week | NY Workers' Compensation Law s.209(3)(a), https://www.nysenate.gov/legislation/laws/WKC/209; SRC/ccg-sources/NY/NY_WCL-209_nysenate_browser_2026-11-02.txt | s.209(3)(a) |
| `NY.pfl` | 0.432% per pay period; annual max employee contribution 411.91 | NY DFS, "Decision on Premium Rate for Paid Family Leave ... Beginning January 1, 2026" (2025-08-29), https://www.dfs.ny.gov/apps-and-licensing/health-insurers/pfl-rate-decision-2026-page; SRC/ccg-sources/NY/NY_DFS_PFL-rate-decision-2026_browser_2026-11-02.txt | decision paragraph |
| `NY.sui.wage_base` 17,600 | | NYS-45-I (1/26) instructions, https://www.tax.ny.gov/pdf/current_forms/wt/nys45i.pdf; SRC/ccg-sources/NY/nys45i-instructions.txt | "UI wage base" chart: "The wage base for 2026 is $17,600" |
| `NY.sui.new_employer_rate_total` 4.1% (4.025% UI + 0.075% RSF) | | NYS DOL "Unemployment Insurance Rate Information", https://dol.ny.gov/unemployment-insurance-rate-information; SRC/pdfs/NY/DOL-UI-rate-information_2026-11-01.html | 2026 rate table, row "New Employer rate" |

## Illinois

| Key | Value | Source | Where |
|---|---|---|---|
| `IL.pit.rate` 4.95%, `line1_allowance` 2,925, `line2_allowance` 1,000 | | Booklet IL-700-T (R-12/25), IDOR page https://tax.illinois.gov/forms/withholding/currentyear/il-700-t-withholding-guide-tables.html; SRC/pdfs/IL/il-700-t_2026_webfetch-20261029.pdf | p.3 and p.4 "Automated payroll method" (formula + Alice example); Mary table example p.3 |
| `IL.sui.wage_base` 14,250; `new_employer_rate` 3.35% ("Standard (Ineligible) rate", non-construction) | | IDES "Historical Rate Chart", SRC/ccg-sources/IL/IDES_UI-tax-rates-2026_2026-11-02.pdf (same file as SRC/pdfs/IL/UI_tax_rates_2026_wayback-20260402163104.pdf) | column 2026, rows "WAGE BASE" and "STANDARD (Ineligible) RATE" |

## Pennsylvania

| Key | Value | Source | Where |
|---|---|---|---|
| `PA.pit.rate` 3.07% | | REV-415 (SU) 01-23 Employer Withholding Information Guide, SRC/pdfs/PA/REV-415_wayback-2026-10-29.pdf | p.11 (PDF p.13) "Calculation of withholding" |
| `PA.uc_ee.rate_ee` 0.07%, no cap | | PA DLI "Yearly Tax Highlights", https://www.pa.gov/agencies/dli/resources/for-employers-and-educators/how-to-file/uc-tax/yearly-tax-highlights; SRC/ccg-sources/PA/PA_US-PA-009_r2-curl_2026-11-02.html | 2026 section, "Employee contributions (UC withholding)" |
| `PA.sui.wage_base` 10,000; `new_employer_rate` 3.8220% (newly liable non-construction) | | same | 2026 section, "Taxable Wage Base for Calendar Year 2026" and "newly liable non-construction employer contribution rate is .038220" |

## Ohio

| Key | Value | Source | Where |
|---|---|---|---|
| `OH.pit_regimes[0]` (2025-10-01 to 2026-07-31) | exemption per period; 1.775% / 2.99% / 3.64% brackets | ODT "Employer Withholding Taxes - Percentage Method (Effective October 1, 2025)", https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/employer_withholding/2025%20Withholding%20Tables/WHT_PercentageMethod_2025.pdf; LIVE/OH_WHT_PercentageMethod_2025.pdf | Tables 1-5 |
| `OH.pit_regimes[1]` (from 2026-08-01) | 1.6% / 2.99% / 3.4% | ODT "... Percentage Method (Effective August 1, 2026)", https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/employer_withholding/2026%20Withholding%20Tables/WHT_PercentageMethod_2026.pdf; SRC/pdfs/OH/WHT_PercentageMethod_2026_wayback-20261018074050.pdf | Tables 1-5 |
| Regime dates | "Current Withholding Tables Effective October 1, 2025 through July 31, 2026"; "New Withholding Tables Effective August 1, 2026" | https://tax.ohio.gov/business/employer-withholding; SRC/ccg-sources/OH/OH_Tax_employer-withholding_2026-11-02.html | "Tax Rates" block |
| Table consistency rows | | ODT Weekly tables 2025 and 2026, LIVE/OH_WHT_WeeklyRate_2025.pdf, LIVE/OH_WHT_WeeklyRate_2026.pdf | page 1 rows |
| `OH.sui.wage_base` 9,000 | | ORC 4141.01(G)(1), SRC/ccg-sources/OH/orc-4141-01.txt | "nine thousand dollars on and after January 1, 2020" |
| `OH.sui.new_employer_rate` 2.7% | | ORC 4141.25(A)(1), https://codes.ohio.gov/ohio-revised-code/section-4141.25; LIVE/OH_ORC-4141.25_opera.txt | (A)(1) "standard rate ... two and seven-tenths per cent" (construction: industry average if higher) |

## North Carolina (NC-30 "2026 Income Tax Withholding Tables and Instructions for Employers", Web 11-25, https://www.ncdor.gov/income-tax-withholding-tables-and-instructions-employers/open; SRC/pdfs/NC/NC-30_2026_ncdor-2026-10-29.pdf)

| Key | Value | Where |
|---|---|---|
| `NC.pit.rate` 4.09% (3.99% + 0.1%), whole-dollar rounding | | p.17-19 headers "Round off the final amount to the nearest whole dollar" |
| `NC.pit.percentage_method` | per-period standard deduction and allowance amounts | pp.17-18 |
| `NC.pit.annualized_method` | 12,750 / 19,125; 2,500 per allowance | p.19 |
| Examples ($450 weekly, result $4) | | p.18 and p.19 (PDF pp.19-20) |
| `NC.sui.wage_base` 34,200; `new_employer_rate` 1% | NC DES "Tax Rate Information", https://www.des.nc.gov/employers/tax-rate-information; SRC/pdfs/NC/DES-tax-rate-information_2026-11-01.html | "New Employer Tax Rate Table", row 2026 |

## Michigan

| Key | Value | Source | Where |
|---|---|---|---|
| `MI.pit.rate` 4.25%, `exemption_annual` 5,900 | "4.25 percent of compensation after deducting the personal and dependency exemption allowance" | Form 446 (Rev. 02-26) 2026 Michigan Income Tax Withholding Guide, https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/SUW/TY2026/446_Withholding-Guide_2026.pdf; SRC/pdfs/MI/446_Withholding-Guide_2026_wayback-20261018080321.pdf | p.1 header; p.2 "How Much to Withhold"; p.4 exemption amount |
| `MI.sui.wage_base` 9,000 | | UIA FAQ "Taxable Wage Base", https://www.michigan.gov/leo/bureaus-agencies/uia/employers/frequently-asked-questions-for-employers/for-employers/taxable-wage-base; SRC/ccg-sources/MI/MI_UIA-FAQ-taxable-wage-base_2026-11-02.html | answer "How much is the taxable wage base?" |
| `MI.sui.new_employer_rate` 2.7% | | UIA "Tax Rate Summary for 2026" (unemployment-insurance-taxes page); SRC/pdfs/MI/UIA-tax-rate-pages_2026-11-01.txt | "New Employer Rate 2.7%" |

## Georgia

| Key | Value | Source | Where |
|---|---|---|---|
| `GA.pit_regimes[0]` (2026-01-01 to 2026-05-10): 5.19%, Table E | 461.54/230.77/230.77/76.92 weekly ... | GA DOR "Employer's Withholding Tax Guide 2026", revised December 2025, https://dor.georgia.gov/document/document/2026-employers-tax-guide/download (Wayback 2026-01-16); LIVE/GA_2026-employers-tax-guide_wayback-20260116.pdf | p.3 What's New; p.46 Table E and example; p.47 Table F example |
| `GA.pit_regimes[1]` (from 2026-05-11): 4.99%, Table E | 576.92/288.46/288.46/96.15 weekly ... | GA DOR guide revised September 2026, SRC/pdfs/GA/GA-DOR-2026-Employers-Withholding-Guide_rev-Sept2026_download-2026-10-29.pdf (identical text to the June 2026 revision, LIVE/GA_2026-employers-tax-guide-june_wayback-20260913.pdf) | p.3 "HB 463 ... continue to withhold at 5.19% before the effective date ... can begin withholding at the new rate of 4.99%, starting May 11, 2026"; p.51 Table E and example; p.52 Table F example |
| `GA.sui.wage_base` 9,500; `new_employer_rate` 2.70% | | GA DOL Employers FAQ, https://dol.georgia.gov/faqs-employers/employers-faqs-unemployment-insurance (Wayback 2026-06-13); SRC/pdfs/GA/employers-faqs-unemployment-insurance_wayback-20260613135345.html | "taxable wage base ... $9,500"; "New or newly covered employers are assigned a total tax rate of 2.70 percent" |

## Texas and Florida

| Key | Value | Source | Where |
|---|---|---|---|
| `TX.pit`, `FL.pit` = null | no state personal income tax | (no withholding publication exists) | |
| `TX.sui.wage_base` 9,000 | | TWC "Your Tax Rates", https://www.twc.texas.gov/programs/unemployment-tax/your-tax-rates; SRC/ccg-sources/TX/twc-your-tax-rates.txt | "taxable wages are the sum of the wages you pay up to $9,000 per employee per year" |
| `TX.sui.new_employer_rate` 2.70% | "generally" (industry-average rule not modelled) | TWC eFTE "Estimate chargebacks and tax rates", SRC/ccg-sources/TX/TX_TWC-efte_estimate_cbs_and_tax_rates_2026-11-02.htm | note "first six calendar quarters ... 'new employer' tax rate of 2.70%" |
| `FL.sui.wage_base` 7,000; `new_employer_rate` 2.7% | | FL DOR "Reemployment Tax", https://floridarevenue.com/taxes/taxesfees/Pages/reemployment.aspx; SRC/ccg-sources/FL/FL_DOR_reemployment_2026-11-02.html | "initial tax rate for new employers is .0270 (2.7%), ... first $7,000" |

## Decisions not stated by any publication (flagged in every result)

| Topic | Oracle choice | Flag |
|---|---|---|
| Rounding where only examples show it (CA, NY, NYC, Yonkers, IL, GA) | cents, half-up, at the step the example rounds | `ROUNDING_FROM_EXAMPLES:<line>` |
| Rounding with no rule (PA, OH, MI, CA SDI, NY DBL/PFL, PA UC, SUI, ETT, FUTA) | unrounded, 6 dp | `UNROUNDED:<line>` |
| NY Method III rounding | cents | `ASSUMED_CENTS:sit_NY_method3` |
| CA "Married 0 or 1 / 2 or more allowances" column | counts regular allowances (DE 4 line 1) | `CA_MARRIED_COLUMN_BY_REGULAR_ALLOWANCES` |
| NY DBL $0.60 weekly cap on non-weekly payrolls | 0.60 x 52 / periods | `NY_DBL_WEEKLY_CAP_CONVERTED_52_OVER_PERIODS` |
| MI per-period exemption | 5,900 x exemptions / periods | `MI_PER_PERIOD_EXEMPTION_PRORATION_NOT_STATED` |
| GA and OH regime switch | by pay date (GA: "can begin" on 2026-05-11, so the switch date is an employer option) | `GA_REGIME_FROM_*`, `OH_REGIME_FROM_*` |

- 2026-11-06 (V-05, ORACLE-DEFECT): OH new-employer rate 2.7% + 0.15% flat surcharge (ORC 4141.251) = 2.85%. Source: ODJFS 2026 Rate Details line 41 "Rate 2.7% ... 0.15% 2.85%".
