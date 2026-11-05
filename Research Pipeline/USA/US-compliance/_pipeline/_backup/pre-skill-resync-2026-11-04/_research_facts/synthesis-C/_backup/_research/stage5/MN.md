# Stage 5 - MN (Minnesota) - 13-domain findings

Worker: compliance-source-hunter, 2026-11-02. Scope: `_prompts/stage5-brief.md`, JUR = MN. The mandate block US-MQ-43 (answered at seal attempt 5) was reused, not re-researched.

Budget:
- Declared 60 fetches / 2 h; working ceiling 45 fetches.
- Used about 34 fetches and 1 search, roughly 20 min of wall clock.

New files:
- Register shard `00-official-sources/_register-shards/S5-MN.csv`: rows US-MNS5-001..022 (21 active, 1 partial).
- 25 source files in `00-official-sources/ccg-sources/MN/`, 2.7 MB total. Every file is under 0.9 MB; the largest is the Laws 2026 c 106 page.

Reused active rows (not re-fetched):
- US-MN-PIT-001, US-MN-P5-1-001, US-MN-P5-1-004.
- US-MN-P5-2-001..005, US-MNR3-001, US-MNR3-002.
- US-MNP6-001..003, US-MNP7-001, US-MNP7-002, US-MNP9L-001, US-MULTI-013.

The DOR booklet wh-inst-26 was already on disk (`00-official-sources/pdfs/MN/`). It was read locally again with pdftotext and **not re-downloaded or copied**, so each file sits in only one folder (F23). Its formula lines are now registered as US-MNS5-010.

Supersessions proposed for the synthesis (both earlier rows were MANUAL, from a summarizer reading):
- US-MNS5-017 supersedes US-MN-P5-1-003: 268.035 read literally.
- US-MNS5-018 supersedes US-MN-P5-1-002: 268B.14 read literally.

Access: Revisor, DLI, Minneapolis and St. Paul all answered plain curl with HTTP 200. uimn.org returned HTTP 000 (no connection); the active Wayback rows were kept.

## 1. labour_code
- **State minimum wage** [US-MNS5-002, A.2 (DLI); mechanism US-MNS5-001, A.1]:

  | From | All employers | 90-day training wage (under 20) |
  |---|---|---|
  | 2026-01-01 | **11.41** | **9.31** |
  | 2027-01-01 (published) | **11.87** | **9.68** |

  - The statute does not print the yearly rate. The rate comes from indexation under 177.24 subd. 1(c) (see §11).
  - The employer may not cut existing employees' hours or wages to hire at the training wage.
- **No tip credit** [US-MNS5-001 subd. 2; US-MNS5-002]:
  - Tips belong to the employee; pooling is voluntary only.
  - Card tips go to the employee no later than the next scheduled pay period (subd. 3a).
- **Local minimum wages:**
  - **Minneapolis** [US-MNS5-008, A.2]: 16.37 for 2026 and 17.02 from 2027-01-01, whatever the employer size or employee age. Indexed each 1 January, capped at 5%.
  - **Saint Paul** [US-MNS5-009, A.2], by business size:

    | Business size | Earlier rate | 2026 rate | Later |
    |---|---|---|---|
    | Macro (10,001+) and the City | | 16.37 from 2026-01-01 | |
    | Large (101-10,000) | | 16.37 from 2026-01-01 | |
    | Small (6-100) | 15.00 from 2025-07-01 | 16.37 from 2026-07-01 | |
    | Micro (5 or fewer) | | 14.25 from 2026-07-01 | 15.00 from 2027-07-01; indexed city rate from 2028-07-01 |
    | Youth / training | | 13.95 from 2026-07-01 | |

    - The 2027 indexed "City Rate" for macro/large/small is not on the page (open question).
    - The city minimum applies from the employee's 18th birthday.
  - No other city minimum wage is named on the DLI page.
- **Overtime** (Minn. Stat. 177.25) [US-MNS5-003, A.1]:
  - 1.5x the regular rate **over 48 hours** a week. The FLSA 40-hour rule still binds FLSA-covered employers.
  - Health care facilities may use an 8/80 schedule by prior agreement.
  - Public employers may give comp time at 1.5 hours per hour.
  - Exemptions: commissioned vehicle sales and mechanics, silo piece-rate work, air-carrier shift trades. Exempt categories under 177.23 subd. 7 are in US-MNS5-004.
- **Pay frequency** (181.101) [US-MNS5-005, A.1]:
  - Wages at least every 31 days, commissions at least every 3 months, on a regular payday set in advance.
  - The first half of the first period is due on the first regular payday after the start date.
  - Wages are earned on the day worked.
  - DLI demand penalty: average daily earnings for each day after 10 days.
- **Method of payment (direct deposit / paycard consent): not read this pass.** Open question.
- Confidence: high on minimum wage, overtime and frequency; payment method open.

## 2. income_tax
- **Method** (DOR booklet 2026, computer formula p. 34) [US-MNS5-010, A.2; statute US-MN-P5-1-001]:
  - Annualise the wages: x 360 / 52 / 26 / 24 / 12 / 1.
  - Subtract **allowances x 5,300**.
  - Apply the chart below, then divide by the number of pay periods.

  | Status | Taxable band (annual) | Rate | Add |
  |---|---|---|---|
  | Single | 4,700 - 38,010 | 5.35% of excess over 4,700 | 0 |
  | Single | 38,010 - 114,130 | 6.80% | 1,782.09 |
  | Single | 114,130 - 207,850 | 7.85% | 6,958.25 |
  | Single | over 207,850 | 9.85% | 14,315.27 |
  | Married | 14,700 - 63,400 | 5.35% of excess over 14,700 | 0 |
  | Married | 63,400 - 208,180 | 6.80% | 2,605.45 |
  | Married | 208,180 - 352,630 | 7.85% | 12,450.49 |
  | Married | over 352,630 | 9.85% | 23,789.82 |

  - Derivation check, done in Python: the cumulative "add" amounts reproduce exactly (33,310 x 5.35% = 1,782.09; then 6,958.25; 14,315.27; married 2,605.45; 12,450.49; 23,789.82).
  - **Oracle seed:** biweekly 2,000.00, single, 1 allowance:
    - 52,000 - 5,300 = 46,700;
    - 1,782.09 + (46,700 - 38,010) x 6.80% = 2,373.01;
    - 2,373.01 / 26 = **91.27**, or 91 if rounded.
    - The official oracle is the DOR Withholding Tax Calculator [US-MNR3-002].
- **Rounding:** "You may round the amount to the nearest dollar" (formula step 6). The table rows say "round total to the nearest whole dollar". 290.92 subd. 2a allows rounding to the nearest dollar [US-MN-P5-1-001].
- **Certificate:** W-4MN is required alongside the federal W-4. With no W-4MN, withhold as single with 0 allowances.
  - Copies go to DOR when more than 10 allowances are claimed, or when an exempt box is checked and wages exceed 200/week.
  - An exempt claim must be renewed each year.
  - Penalties: 500 USD on the employee, 50 USD on the employer per form not sent [US-MNS5-010].
- **Supplemental wages:** 6.25% flat (Method 2) or aggregate (Method 1). Method 1 is mandatory when supplemental pay is not listed separately [US-MNS5-010; US-MN-P5-1-001].
- **Nonresidents** [US-MNS5-010; US-MULTI-013]:
  - No MN withholding when the expected pay is under **15,300**, or when MI/ND residents give Form MWR (reciprocity).
  - Wages earned while a MN resident but paid after the person leaves stay MN-source (e.g. severance, equity).
  - MN residents working in another state: withhold the difference using the worksheet (MN tax minus the other state's tax).
- **Backup withholding:** 9.85% on personal-service payments with no TIN or a wrong TIN [US-MNS5-010].
- **Local income taxes:** none. A general law prohibits them [US-MNR3-001, A.2].
- **Conformity:** withholding definitions follow the IRC as amended through **2023-05-01**. MN has **not adopted the H.R. 1 (2025)** withholding changes [US-MNS5-010].
- Confidence: high.

## 3. social_security
- **State UI** (all on active rows US-MN-P5-2-001/-002, Wayback copies of uimn.org):
  - 2026 wage base **44,000**.
  - Base tax rate 0.40%; experience maximum 8.90%.
  - Additional assessment 14%; special assessment 0%.
  - New employers get the industry-average rate.
  - No employee contribution.
- **UI statute read literally** (268.035 subd. 24) [US-MNS5-017, A.1]:
  - The wage base = 60% of the state's average annual wage, rounded to the nearest 1,000.
  - Noncovered employment is listed under special populations below.
- **Workforce development fee:** 0.10% of taxable wages [US-MNP7-001].
- **Minnesota Paid Leave (DEED)**, in force from 2026-01-01:
  - Statute 268B.14 [US-MNS5-018, A.1]:
    - The employer pays at least 50% of the premium; the employee share is a payroll deduction that may not push pay below the minimum wage.
    - The wage cap is the OASDI maximum.
    - Payment must be electronic.
    - Statutory base rates: 0.7% (family + medical), 0.4% (medical only), 0.3% (family only).
    - The commissioner adjusts the rate by July 31 each year.
  - DEED page [US-MN-P5-2-003, A.2, Wayback 2026-07-31]:
    - Adjusted rate for **2026 and 2027: 0.88%** (family 0.27 + medical 0.61) on wages up to **185,000**.
    - Employee share up to 0.44%.
    - Small employers 0.66%.
    - First quarterly premiums due 2026-04-30 [US-MN-P5-2-004].
  - The 2027 cap follows the 2027 OASDI base (FED unit).
- **No SDI/TDI.**
- Confidence: high on statute and rates. The live pl.mn.gov and uimn.org pages could not be re-read (ACCESS).

## 4. payslip_statute
- **Earnings statement** (181.032) [US-MNP6-001, A.1, reused]:
  - Given each pay period, in writing or electronically.
  - Electronic delivery requires access to an employer computer during work hours and keeping statements available for 3 years.
  - 12 content items.
  - Hire notice in English, with the right to ask for another language.
- **ESST balance** [US-MNS5-011]: each pay period, the hours available and the hours used must be given (on or attached to the statement, or through an electronic system).
- **Record retention** [US-MNS5-020, A.1]: payroll records kept 3 years (177.30). For state-funded public works, 3 years after the project.
- Confidence: high.

## 5. reporting_instruments
- **Withholding** [US-MNS5-010]:
  - Registration: needed when tax will be withheld within the next 30 days.
  - Deposits follow the federal semiweekly/monthly schedule; monthly deposits are due by the 15th. There is no MN one-day rule.
  - Electronic payment is required above the thresholds; non-electronic payment then carries a 5% penalty.
  - Quarterly returns are due Apr 30 / Jul 31 / Oct 31 / Jan 31, filed electronically in e-Services.
  - Annual filers (500 USD or less in the prior year) file by Jan 31.
  - W-2s go to employees by Jan 31, and the W-2 information goes to DOR by Jan 31.
  - **e-Services is mandatory above 10 W-2 + 1099 forms.**
  - The W-2/1099 e-file method changed (DOR Fact Sheets 2 and 2a, not fetched; open).
  - Box 16 allocation: all wages of MN residents, plus MN-sourced wages of nonresidents.
  - Third-party bulk filers must file electronically [US-MN-PIT-001].
- **UI quarterly wage detail report** (268.044) [US-MNS5-015, A.1]:
  - Filed electronically in the commissioner's format.
  - Per employee: name, SSN, wages and **paid hours worked**. Hours are a MN-specific field: exempt full-time employees are reported at 40 h per week.
  - Wages may be truncated to the dollar.
  - A report is due every quarter, even with no wages.
  - Fees: 10 USD per employee (minimum 250), doubled after 30 days; 25 USD per bad record; 2% of wages for an omitted employee.
  - The quarterly due date is not in this section (open).
- **New hire** (142A.29) [US-MNS5-016, A.1]:
  - Due within 20 calendar days of hire.
  - Rehires count after 60 days or more of separation.
  - Exempt: employed less than 2 months and earning under 250/month.
  - Domestic workers in a private home are excluded.
  - Federal fields; a copy of the W-4 is acceptable.
  - Public employers must also report contractors.
- **Paid Leave:** quarterly wage detail and premium payment to DEED, electronic [US-MNS5-018; US-MN-P5-2-004].
- **POA / agents:** REV184b (DOR) [US-MN-P5-2-005]; UI Agent Self-Service ID [US-MNP6-003].
- Confidence: high on statute; UI due dates and file formats are open.

## 6. leave
- **ESST** (181.9445-.9448) [US-MNS5-011, A.1]:
  - Coverage: employers with 1 or more employees; employees expected to work 80+ hours a year in MN.
  - Accrual: 1 hour per 30 hours worked, up to 48 hours a year.
  - Carryover: the balance is capped at 80 hours. Alternatively the employer front-loads 48 hours (paying out unused hours at year end) or 80 hours (no payout).
  - Exempt employees are deemed to work 40 hours a week.
  - Use: increments of 15 minutes to 4 hours.
  - Pay: at the same rate, with benefits maintained.
  - **No payout at separation.**
- **Local ESST ordinances** (Minneapolis, St. Paul, Duluth, Bloomington): not read (open). St. Paul's ESST page link was found but not fetched.
- **Paid Leave benefits:** DEED pays the benefits; the employer collects premiums (see §3).
- Confidence: high on state ESST.

## 7. termination
- **Discharge** (181.13) [US-MNS5-006]:
  - Pay is due within **24 hours after the employee's written demand**.
  - Penalty: average daily earnings for up to 15 days.
- **Resignation** (181.14) [US-MNS5-007]:
  - Pay by the next regular payday.
  - If that payday is less than 5 days after the last day, pay by the second payday, and never later than 20 calendar days after the last day.
  - Migrant workers: within 3 days.
  - Employees who handled money get a 10-day audit window.
- **Accrued vacation payout:** no state statute requires payout. 181.13 and 181.14 count wages owed under "contract ... policy", so payout follows the employer's policy. Confidence medium; no DLI page read.
- **Unused ESST:** no payout [US-MNS5-011].
- **UI separation notice:** the statute imposes **posting only** (268.068) [US-MNS5-021]. No individual separation notice.
- Confidence: high.

## 8. benefits_in_kind
- MN withholding follows the IRC as amended through 2023-05-01 and **does not follow H.R. 1 (2025)** [US-MNS5-010].
- Payroll impact: H.R. 1 provisions affecting federal withholding or exclusions (e.g. changes to fringe exclusions or deductions after 2023-05-01) do not flow to MN withholding.
- No MN departure on 401(k), 125, HSA, transit or group-term life was found in the booklet. A full MN-vs-federal departure list was **not** inventoried (open).
- Confidence: medium.

## 9. deductions_garnishments
- **Wage deductions** (181.79, 181.06) [US-MNS5-012]:
  - Loss or debt deductions need written authorisation given after the loss arises, or a court judgment, and never above the garnishment-exempt limit. Penalty: twice the amount.
  - Wage assignments are void beyond 60 days, except above 1,500/month.
  - A list of deductions is allowed by written contract.
  - Uniform/equipment deductions are capped at 50 USD and may not cut pay below the minimum wage [US-MNS5-001].
- **Garnishment** (571.922) [US-MNS5-013] is **stricter than the CCPA**:
  - Tiers of 25% / 15% / 10% of disposable earnings by weekly income (more than 80x / 60x / 40x the hourly minimum), or the excess over 40x the minimum wage, whichever is less.
  - Child-support judgments: 50/55/60/65%.
- **IWO** (518A.53) [US-MNS5-014, partial]:
  - Remit within 7 business days of payday.
  - Report termination within 10 days.
  - Support withholding has priority over all other attachments.
  - The employer processing fee amount was not located (open).
- **State tax levies:** not read (open).
- Confidence: high on 571.922 and 181.79; IWO fee open.

## 10. collective_agreements
- **State prevailing wage** (177.41-177.44) applies to projects financed in whole or part by state funds [US-MNP6-002, US-MN-P5-1-004, reused].
- Records must be kept 3 years after the project [US-MNS5-020].
- Certified payroll and threshold mechanics were not re-read (left to the existing P5/P6 rows).
- Confidence: medium-high.

## 11. indexation

| Item | Mechanism | Publication | register_id |
|---|---|---|---|
| State minimum and training wage | 12-month PCE implicit price deflator, capped at 5%, nearest cent, set by Aug 31, effective Jan 1 | DLI page (2027: 11.87 / 9.68) | US-MNS5-001, -002 |
| Minneapolis minimum wage | Inflation, capped at 5%, each Jan 1 | City site (2027: 17.02) | US-MNS5-008 |
| St. Paul minimum wage | Percentage increase (city rate) | City HREEO page (2027 figure not shown) | US-MNS5-009 |
| UI wage base | 60% of the state average annual wage, nearest 1,000 | uimn.org tax rates (2026: 44,000) | US-MNS5-017, US-MN-P5-2-001 |
| Paid Leave rate / cap | Commissioner adjusts by July 31; cap = OASDI base | pl.mn.gov (2026-27: 0.88%) | US-MNS5-018, US-MN-P5-2-003 |
| Withholding brackets / allowance | DOR yearly formula | wh-inst-{yy} booklet | US-MNS5-010 |

- Derivation status: the 2027 minimum-wage step (11.41 to 11.87 = +4.03%; 9.31 to 9.68 = +3.97%) is consistent with the cap. The exact PCE percentage was not read, so this is a consistency check, not a reproduction. Reproducing it needs the DLI minimum-wage report or the BEA series.

## 12. data_protection
- **SSN use** (325E.59) [US-MNS5-019]:
  - No public display.
  - No requirement to send an SSN over the internet unless the connection is secure.
  - No printing on mailed materials unless the law requires it.
- **No SSN-truncation rule for pay statements;** 181.032 does not require the SSN on the statement.
- **ESST medical records** are kept confidential and separate, and destroyed or returned on request after 3 years [US-MNS5-011, 181.9447].
- Confidence: high.

## 13. live_legal_change
- **Laws 2026 c 106 art 15 s 5** amended 181.101, but only the firefighter wording [US-MNS5-022]. None of the other payroll statutes read carries a 2026 chapter in its history (the latest is 1Sp2025).
- **Paid Leave** started 2026-01-01, and the 0.88% rate is confirmed for 2027 [US-MN-P5-2-003].
- **2027 minimum wages are published:** state 11.87 / 9.68; Minneapolis 17.02.
- **H.R. 1 nonconformity:** a pending MN conformity bill was not searched (open).
- Not checked: the DEED/DOR news feeds from 2026-01-01 to today. The DOR booklet "What's New" was read.

## Special populations (state rules)

| Population | Rule | register_id |
|---|---|---|
| Domestic / household | UI not covered if quarterly domestic wages are under 1,000 in the current and prior year; excluded from new-hire reporting; sole-practitioner babysitters outside the MFLSA | US-MNS5-017, -016, -004 |
| Agricultural | MFLSA excludes small salaried farm groups and some farm minors; UI covers only "covered agricultural employment" (subd. 11 not read); H-2A not covered; agricultural labor included in the 31-day pay rule | US-MNS5-004, -017, -005 |
| Minors | Training wage under 20 for the first 90 days (9.31 in 2026); St. Paul youth rate until age 18; minors in municipal recreation under 20 h/week excluded; child under 18 employed by a parent not UI-covered | US-MNS5-001, -002, -009, -004, -017 |
| Tipped | No tip credit at state level | US-MNS5-001, -002 |
| Clergy / religious | Excluded from the MFLSA; church and minister employment not UI-covered | US-MNS5-004, -017 |
| Students | Students employed by their school, full-time credit students, J-1 summer work travel and student nurses not UI-covered | US-MNS5-017 |
| Nonresident aliens | No state rule beyond federal found in the booklet; the nonresident 15,300 threshold and MI/ND reciprocity apply by residence | US-MNS5-010 |
| Statutory employees | No state rule found beyond federal (booklet read) | US-MNS5-010 |
| Government employees | MFLSA excludes elected officials, police/fire and some PERA-ineligible staff; public-employer comp time; 24 h discharge clock starts at the board meeting; public employers report contractors as new hires | US-MNS5-004, -003, -006, -016 |
| Family employment | Spouse, child or parent employment not UI-covered | US-MNS5-017 |

## ACCESS gaps
- https://www.uimn.org/employers/wages-taxes/tax-rates/index.jsp: HTTP 000 (no connection) today. The 2026 values rest on the Wayback copy (US-MN-P5-2-001).
- https://pl.mn.gov/resources/calculators/premium-rate-and-contributions: the human-verification wall noted in earlier passes; not retried, Wayback row reused.
- https://www.minneapolismn.gov/business-services/labor-standards/minimum-wage/: HTTP 404. The working route is https://minimumwage.minneapolismn.gov/.

## Open questions
- **mn.labour.payment_method:** direct deposit / paycard consent rule. Would close it: Minn. Stat. 181.08 / 177.30 or the DLI "Paying employees" page.
- **mn.stpaul.minwage.2027:** St. Paul 2027 indexed city rate. Would close it: the city's 2027 rate notice (HREEO).
- **mn.ui.wage_report.due_dates / format:** UI quarterly due dates and file format. Would close it: the UIMN employer handbook "Wage Detail Reports" page (uimn.org; currently unreachable) or Minn. Stat. 268.051 subd. 1.
- **mn.ui.wage_base.2027:** 2027 UI base. Would close it: the DEED 2027 tax rate notice (usually published in December).
- **mn.w2.efile_spec:** W-2 e-file format. Would close it: DOR Withholding Fact Sheets 2 and 2a.
- **mn.iwo.employer_fee:** employer fee for processing an IWO. Would close it: the 518A.53 subdivision on the fee, or the DCYF employer guide.
- **mn.esst.local:** Minneapolis / St. Paul / Duluth / Bloomington ESST ordinances. Would close it: the city ordinance pages.
- **mn.conformity.departures:** full MN-vs-federal departures for fringe exclusions after 2023-05-01. Would close it: the DOR "Federal Update" page.
- **mn.tax_levy:** state tax levy on wages. Would close it: Minn. Stat. 270C.67-.69.
- **mn.vacation.payout:** a DLI statement confirming that vacation payout follows the employer's policy.

## Parallel shape
The open items are independent lookups (city pages, DEED, DOR fact sheets). Any one worker can close them in about 10 fetches. The UIMN items need a browser pass because uimn.org cannot be reached by curl.
