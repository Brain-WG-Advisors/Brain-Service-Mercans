# CCG research pack - annex_OH (Ohio)

Synthesis-B worker MN-WY, 2026-11-02. Unit `annex_OH` of the CCG (jurisdiction annex, all 13 domains + special populations).
Facts file: `_research/CCG-annex_OH-facts.json` (50 facts, 2 pending on the register_id pattern defect, 13 unresolved). Every claim below carries its register_id inline; numbers may be cited in the CCG only through a fact key.

## 0. How to use this pack

- Body sections 1-13 and Special populations are the stage-5 findings (`_research/stage5/OH.md`), carried verbatim because they are already organised by the 13 CCG domains with register ids inline.
- Federal layer (FIT, FICA, FUTA, W-2/941/940), the multistate rules (reciprocity, sourcing) and the language seams (US-OWN-006: payslip in English; second-language duties attach to notices and posters only) live in annex_FED / annex_MULTI and are not repeated here.
- Special populations (US-OWN-005): the state-level rules are in the Special populations table below; the country-wide coverage matrix is CCG unit `coverage`.
- Values are 2026 unless the fact says otherwise. 2027 values appear only where the row carries an enacted or published 2027 figure; projections are never facts.

## 0.1 Synthesis decisions and traps (bind the builder)

- MID-YEAR CHANGE: two withholding editions in 2026 - pay dates 2025-10-01..2026-07-31 (1.775/2.990/3.640%) and from 2026-08-01 (1.6/2.99/3.4%). Withholding schedule (to 3.4%) != statutory flat 2.75% - both are correct for their level.
- Oracle: OH biweekly 2,000 / 1 exemption = 45.13 from 2026-08-01 (46.88 under the earlier formula).
- Municipal base = Medicare wages less 125: 401(k) deferrals TAXABLE locally; school district tax follows residence; municipal follows work location.

## 0.2 Register status check of the ids cited in the findings

These ids appear in the findings but are not plain `active`; do not cite them for a number:

- US-OH-014: gated
- US-OH-P5-1-002: superseded
- US-OH-P5-1-004: MANUAL
- US-OH-P5-2-001: superseded
- US-OHS5-023: partial

## 0.3 Facts emitted

| key | value | from | to | register_id | conf |
|---|---|---|---|---|---|
| `oh.minwage.hourly` | 11.0 USD | 2026-01-01 | 2026-12-31 | US-OHS5-005 | high |
| `oh.minwage.hourly` | 11.4 USD | 2027-01-01 | 2027-12-31 | US-OHS5-004 | high |
| `oh.minwage.tipped.cash_wage` | 5.5 USD | 2026-01-01 | 2026-12-31 | US-OHS5-005 | high |
| `oh.minwage.tipped.cash_wage` | 5.7 USD | 2027-01-01 | 2027-12-31 | US-OHS5-004 | high |
| `oh.labour.minwage.small_employer.gross_threshold` | 405000 USD | 2026-01-01 | 2026-12-31 | US-OHS5-005 | high |
| `oh.labour.minwage.small_employer.gross_threshold` | 419000 USD | 2027-01-01 | 2027-12-31 | US-OHS5-004 | high |
| `oh.minwage.indexation` | CPI-W 12 months to September, each 1 January, rounded to 0.05 | 2007-01-01 |  | US-OHS5-006 | high |
| `oh.local_mandates.preempted` | True | 2017-03-21 |  | US-OHS5-012 | medium |
| `oh.overtime.weekly_threshold_hours` | 40 hours | 2022-07-06 |  | US-OHS5-003 | high |
| `oh.overtime.premium.multiplier` | 1.5 ratio | 2022-07-06 |  | US-OHS5-003 | high |
| `oh.pay_frequency.rule` | at least semimonthly (1-15 by 1st of next month; 16-end by 15th) | 2019-03-20 |  | US-OHS5-015 | high |
| `oh.records.wage_hour.retention_years` | 3 years | 2027-01-01 | 2027-12-31 | US-OHS5-004 | high |
| `oh.pit.statutory.rate` | 2.75 % | 2026-01-01 |  | US-OHS5-007 | high |
| `oh.pit.statutory.zero_bracket` | 26050 USD | 2026-01-01 |  | US-OHS5-007 | high |
| `oh.pit.wh.method.period_b` | formula: TW=pay x PP-650 x exemptions; 1.6% to 26,050; 416.80+2.99% to 100,000; 2,627.91+3.4% above; / PP | 2026-08-01 |  | US-OHS5-001 | high |
| `oh.pit.wh.exemption.annual` | 650 USD | 2025-10-01 |  | US-OHS5-001 | high |
| `oh.pit.wh.rate.1` | 1.6 % | 2026-08-01 |  | US-OHS5-001 | high |
| `oh.pit.wh.rate.2` | 2.99 % | 2026-08-01 |  | US-OHS5-001 | high |
| `oh.pit.wh.rate.3` | 3.4 % | 2026-08-01 |  | US-OHS5-001 | high |
| `oh.pit.wh.break.1` | 26050 USD | 2026-08-01 |  | US-OHS5-001 | high |
| `oh.pit.wh.break.2` | 100000 USD | 2026-08-01 |  | US-OHS5-001 | high |
| `oh.pit.wh.base_tax.2` | 416.8 USD | 2026-08-01 |  | US-OHS5-001 | high |
| `oh.pit.wh.base_tax.3` | 2627.91 USD | 2026-08-01 |  | US-OHS5-001 | high |
| `oh.pit.oracle.example_1.withholding` | 45.13 USD | 2026-08-01 |  | US-OHS5-001 | high |
| `oh.wh.supplemental.rate` | 2.75 % | 2026-01-01 | 2026-12-31 | US-OHS5-017 | high |
| `oh.reciprocity.states` | IN;KY;MI;PA;WV | 2026-01-01 |  | US-MULTI-005 | high |
| `oh.pit.exempt.quarterly_cash_threshold` | 300 USD | 2019-10-17 |  | US-OHS5-008 | high |
| `oh.pit.school_district.basis` | withheld for employees residing in a taxing district | 2026-08-01 |  | US-OH-002 | high |
| `oh.pit.municipal.basis` | work-location; qualifying wages = Medicare wages less section 125 (401(k) deferrals taxable) | 2025-09-30 |  | US-OHS5-013 | high |
| `oh.pit.municipal.occasional_entrant_days` | 20 days | 2015-03-23 |  | US-OH-008 | high |
| `oh.pit.municipal.rate_cap_without_vote` | 1 % | 2026-01-01 |  | US-OHP7-001 | high |
| `oh.sui.wage_base` | 9000 USD | 2026-01-01 | 2026-12-31 | US-OHS5-002 | high |
| `oh.sui.new_employer.rate` | 2.85 % | 2026-01-01 | 2026-12-31 | US-OHS5-002 | high |
| `oh.ui.rate.new_employer.construction` | 5.85 % | 2026-01-01 | 2026-12-31 | US-OHS5-002 | high |
| `oh.ui.rate.min_total` | 0.55 % | 2026-01-01 | 2026-12-31 | US-OHS5-002 | high |
| `oh.ui.rate.max_total` | 10.25 % | 2026-01-01 | 2026-12-31 | US-OHS5-002 | high |
| `oh.ui.tcsf.rate` | 0.15 % | 2026-01-01 | 2026-12-31 | US-OHS5-002 | high |
| `oh.sui.employee.rate` | 0 % | 2026-01-01 | 2026-12-31 | US-OHS5-002 | high |
| `oh.report.it501.quarterly_threshold` | 2000 USD | 2026-01-01 |  | US-OH-009 | high |
| `oh.report.it501.partial_weekly_threshold` | 84000 USD | 2026-01-01 |  | US-OH-009 | high |
| `oh.report.it941.due` | January 31 | 2026-01-01 |  | US-OH-009 | high |
| `oh.report.ui.quarterly_due` | last day of month after quarter | 2014-09-15 |  | US-OHS5-020 | high |
| `oh.newhire.report_days` | 20 days | 2013-09-29 |  | US-OHS5-009 | high |
| `oh.leave.sick.state_statute.exists` | False | 2017-03-21 |  | US-OHS5-012 | high |
| `oh.final_pay.rule` | next regular payday under 4113.15 schedule | 2019-03-20 |  | US-OHS5-015 | medium |
| `oh.term.mass_layoff.notice_working_days` | 3 days | 2023-10-03 |  | US-OHS5-016 | high |
| `oh.garn.consumer.exempt_multiple_fmw.weekly` | 30 | 2025-09-30 |  | US-OHS5-011 | high |
| `oh.garn.iwo.employer_fee.min` | 2 USD | 2001-03-22 |  | US-OHS5-010 | high |
| `oh.prevailing_wage.threshold.new_construction` | 250000 USD | 2026-01-01 |  | US-OHR3-002 | medium |
| `oh.data.breach_notice.days` | 45 days | 2007-03-30 |  | US-OHS5-021 | high |
| `oh.wh.certificate` | IT 4; none on file = zero exemptions | 2026-10-29 |  | US-OH-P5-2-006 (PENDING id pattern) | high |
| `oh.payslip.items` | name and address; employer name; gross and net; each addition and deduction; pay date and period; hours and rate (hourly) | 2025-04-09 |  | US-OH-P5-1-001 (PENDING id pattern) | high |

# Findings by domain (stage 5)

## 1 labour_code
- **Minimum wage, 2026:** 11.00 USD/h non-tipped and 5.50 USD/h tipped (tipped = more than 30 USD/month in tips). Employers grossing under 405,000 USD and employees under 16 pay the federal 7.25 USD. Vigência 2026-01-01..2026-12-31 [US-OHS5-005].
- **Minimum wage, 2027 (published):** 11.40 / 5.70 USD/h, small-employer threshold 419,000 USD, from 2027-01-01 [US-OHS5-004]. The G-DERIVE proof is in domain 11.
- **No local minimum wages.** Ohio law preempts local regulation of hours, scheduling and benefits for private employers (ORC 4113.85) [US-OHS5-012]. No city minimum wage was located; the 4113.85 text covers benefits and scheduling, and minimum-wage preemption itself (ORC 4111.02) was not read. Confidence 80%.
- **Overtime:** 1.5x over 40 hours per workweek, following FLSA s.7/s.13 exemptions; no daily overtime (ORC 4111.03) [US-OHS5-003]. The poster excludes employers grossing under 150,000 USD/year [US-OHS5-004/005].
- **Pay frequency and pay day:** at least semimonthly. Wages for the 1st–15th are due by the 1st of the next month; wages for the 16th–month end by the 15th of the next month. Daily or weekly pay is allowed, as is a longer lapse that is customary or set by contract. Liquidated damages apply after 30 days unpaid (ORC 4113.15) [US-OHS5-015, US-OH-004].
- **Method of payment** (direct deposit or paycard consent): no Ohio statute was read this pass. This is an open question.
- **Records:** kept 3 years — name, address, occupation, rate, pay per period, hours per day and per week [US-OHS5-004].
- **Confidence:** High for the minimum wage and overtime; Medium for the method of payment.

## 2 income_tax
- **Statutory rate (HB 96):**
  - TY2026 and later: flat 332.00 + 2.75% of Ohio taxable income over 26,050 USD; no tax up to 26,050.
  - TY2025: 2.75% / 3.125%. TY2024: 2.75% / 3.5%.
  - Source: ORC 5747.02(A)(3), effective 2025-09-30 [US-OHS5-007].
- **Withholding duty:** ORC 5747.06 [US-OHS5-008]. The commissioner's tables define the method. They apply to residents and nonresidents, and also to the state and its political subdivisions as employers.
- **Withholding method, two editions in 2026 (mid-year change):**
  - Pay dates 2025-10-01 to 2026-07-31:
    - optional computer formula with 650 USD per exemption and rates 1.775% / 2.990% / 3.640% (breaks at 26,050 and 100,000) [US-OH-P5-2-001];
    - percentage tables of the same period [US-OH-002].
  - Pay dates from 2026-08-01:
    - percentage tables: weekly 12.50 per exemption, then 1.600% up to 500.96, 8.02 + 2.990% up to 1,923.08, 50.54 + 3.400% above. Biweekly, semimonthly, monthly and daily tables also exist [US-OH-006];
    - computer formula: TW = pay x PP − 650 x exemptions; WD = TW x 0.016 / PP up to 26,050; ((TW − 26,050) x 0.0299 + 416.80) / PP up to 100,000; ((TW − 100,000) x 0.034 + 2,627.91) / PP above [US-OHS5-001].
  - The withholding schedule still graduates up to 3.4%, although the TY2026 statutory rate is flat 2.75%. These are two different instruments: the 5747.06 rule versus the 5747.02 rate. The tables do not mis-transcribe the rate.
- **Derivation (G-DERIVE):**
  - The constants reconcile: 26,050 x 0.016 = 416.80, and 416.80 + 73,950 x 0.0299 = 2,627.91.
  - Oracle seed: biweekly 2,000 USD with 1 exemption, paid on or after 2026-08-01.
    - Table: TW 1,975.00 gives 16.03 + 973.08 x 0.0299 = 45.13.
    - Formula: TW 51,350 gives (25,300 x 0.0299 + 416.80) / 26 = 45.13.
    - The 2025 formula gives 46.88.
- **No rounding instruction** appears in the tables or the formula. ORC 718.25 optional whole-dollar rounding applies to municipal returns only [US-OH-P5-2-002].
- **Supplemental rate:** OAC 5703-7-10, effective 2026-01-01, withholds supplemental pay (bonuses, commissions, nonrecurring pay) at the highest 5747.02(A)(3) rate for the year. That is **2.75% for TY2026** [US-OHS5-017], which confirms US-OH-002.
- **Certificate:** IT 4 (rev. 12/2020), a combined form that replaces IT 4NR, IT 4 MIL and IT MIL-SP. If no IT 4 is on file, withhold at zero exemptions. Keep the form 4 years [US-OH-P5-2-006; 2026 Filing Guidelines Rev. 11/25 on disk under pdfs/OH, row US-OH-P5-1-002 superseded].
- **Reciprocity:** no Ohio withholding for residents of IN, KY, MI, PA or WV working in Ohio [US-MULTI-005, US-OH-P5-2-006]. The resident credit is IT RC; no credit for wages from the reciprocity states [US-OH-P5-2-004].
- **Exemptions from withholding (5747.06):** agricultural labour, domestic service, service in a quarter with cash pay under 300 USD, foreign government service, newspaper carriers under 18 [US-OHS5-008].
- **School district income tax (ch. 5748):**
  - Withheld for employees who *reside* in a taxing district, even if the employer has no operations there [US-OH-002, US-OHS5-017].
  - 2026 changes: 6 new districts (e.g. Westerville CSD 0.75%, Findlay CSD 1.00%), 2 expired, 3 rate changes and 21 renewals [US-OHS5-018]. The 2025 full list is US-OHS5-019; no consolidated 2026 full list was located.
  - Lookup tool: The Finder [US-OHS5-023, partial].
- **Municipal income tax (ch. 718):**
  - Work-location based. The employer withholds qualifying wages x the municipal rate and remits to the municipality or its collector (RITA, CCA) [US-OH-P5-2-003, US-OH-010].
  - 20-day occasional-entrant rule [US-OH-008].
  - The base is Medicare wages less section 125, so 401(k) deferrals are taxable [US-OHS5-013].
  - Rates may not exceed 1% without voter approval [US-OHP7-001].
  - **No consolidated municipal rate table was obtained** (ACCESS gap).
- **Confidence:** High for state withholding; Medium for the local layer (no rate table).

## 3 social_security (SUI, SDI/PFML, levies)
- **ODJFS rate year 2026** [US-OHS5-002 (rate-detail PDF), US-OH-005 (ODJFS page); second document family, consistent]:
  - taxable wage base 9,000 USD;
  - new employer 2.85% (2.7% + 0.15% Technology & Customer Service Fee, ORC 4141.251); construction 5.85%;
  - experienced rates 0.4%–10.1% before the fee, 0.55%–10.25% total; mutualized 0.0%;
  - delinquency 12.75%; SUTA dumping 12.75%; tax-avoidance penalty 14.75%;
  - employer-only, no employee contribution.
- **TCSF levy (0.15%):** see US-OHP7-003.
- **No SDI/TDI/PFML** [US-OH-P5-1-004].
- **No transit or workforce levy on wages** [US-OHL-002].
- **Not covered:** how the wage base is indexed (ORC 4141.01) was not read. The base has been fixed at 9,000 in recent years, but that is unverified this pass. Open question.
- **Confidence:** High.

## 4 payslip_statute
- **Content (ORC 4113.14, Pay Stub Protection Act, HB 106, effective 2025-04-09):** a written or electronic statement every pay period showing:
  - employee name and address, employer name;
  - gross and net pay;
  - amount and purpose of each addition and deduction;
  - pay date and pay period;
  - for hourly employees, hours worked and rate.

  Sources: [US-OH-P5-1-001, US-OHL-001]. The statute has no language clause.
- **SSN on the stub:** not required.
- **Retention:** 3 years for wage and hour records [US-OHS5-004]; 4 years for withholding records [2026 Filing Guidelines].
- **Confidence:** High.

## 5 reporting_instruments
- **State withholding** [US-OH-009; Filing Guidelines]:
  - IT 501 return, filed electronically through OH|TAX eServices or the Treasurer.
  - Frequency by look-back (12 months ending June 30):
    - up to 2,000 USD: quarterly, due the last day of the month after the quarter;
    - more than 2,000 and less than 84,000 USD: monthly, due within 15 days;
    - 84,000 USD or more: partial-weekly EFT within 3 banking days;
    - 100,000 USD or more in one pay period: next banking day.
  - IT 941 annual reconciliation by January 31.
  - W-2/1099 upload through OH|TAX "Upload Income Statement" by January 31; the CD option has been eliminated; a simplified format is available up to 500 statements. W-2s carry the four-digit school district code [US-OHS5-018].
  - Registration within 15 days of liability.
- **School district:** SD 101 (periodic) and SD 141 (annual, January 31). Bulk filing uses FSET XML 4.4 [US-FIL-012]. Agent authorisation is WT 8655 [US-FIL-011].
- **Municipal:** returns go to each municipality or collector. Under 718.03: monthly (15 days after month-end) if prior-year withholding exceeded 2,399 USD or any month of the preceding quarter exceeded 200 USD; otherwise quarterly. A municipality may require semimonthly remittance [US-OH-P5-2-003]. CCA uses Form CCA-102 [US-OH-010]. RITA Form 11/17 is gated [US-OH-014].
- **UI quarterly report (ORC 4141.20):** contribution and wage report by the last day of the month after the quarter. Fields: total and taxable remuneration, each employee's name and SSN, wages per employee, number of weeks paid. Late-filing forfeiture is 0.25% of remuneration, 50–1,000 USD [US-OHS5-020]. The channel or format for the employer filing portal was not read.
- **New hire (ORC 3121.891–.893):** to ODJFS within 20 days of hire. Fields: name, address, date of birth, SSN, hire date, plus employer name, address and ID. Contractors are also reported. A copy of the W-4 is allowed; multistate employers may designate one state [US-OHS5-009, US-OHS5-014].
- **Representatives:** TBOR 1 [US-OH-P5-2-005]; JFS-20106 (UI taxes) [US-OHR3-001].
- **Confidence:** High for the state; Medium for municipal (per collector).

## 6 leave
- **No state paid sick leave law.** ORC 4113.85 makes leave and fringe benefits matters of employer policy or agreement and preempts local mandates for private employers [US-OHS5-012].
- **No PFML,** so there is no benefit-side payroll interaction [US-OH-P5-1-004].
- **Other leave** (jury duty 2313.19, military 5903.02, voting): not read this pass. Open question.
- **Confidence:** Medium-High.

## 7 termination
- **No dedicated final-pay statute.** Final wages fall on the next regular payday under the 4113.15 schedule [US-OHS5-015].
- **Accrued vacation payout:** follows employer policy (4113.85 lists vacation and separation pay as policy matters) [US-OHS5-012].
- **UI separation:**
  - ODJFS asks the separating employer for the reason when a claim is filed.
  - Mass layoff of 50 or more people in 7 days for lack of work: notify the director 3 working days ahead and give each worker the eligibility information (ORC 4141.28(C)) [US-OHS5-016].
  - No individual separation-notice duty was found in 4141.28 (the OAC 4141 rules were not read).
- **No state WARN law located;** federal WARN applies.
- **Confidence:** Medium-High.

## 8 benefits_in_kind
- **State tax:** Ohio AGI starts from federal AGI (ORC 5747.01(A), latest amendment SB 9 effective 2026-03-05). None of the add-backs read touch 401(k), section 125, HSA, transit or group-term life, so the state follows federal exclusions [US-OHS5-022].
- **Municipal tax departs from federal.** The base is IRC 3121(a) wages: 401(k)/403(b) elective deferrals are **taxable**, section 125 is excluded, and NQDC and stock options depend on a municipal ordinance adopted before 2016 [US-OHS5-013].
- **School district tax:** follows the district base ("T" traditional or "E" earned income) [US-OHS5-019].
- **Confidence:** High for state and municipal; Medium for the SD earned-income base detail.

## 9 deductions_garnishments
- **Creditor garnishment (ORC 2329.66(A)(13)):** exempt amount is the greater of 75% of disposable earnings or 30x / 60x / 65x / 130x the federal minimum wage (weekly / biweekly / semimonthly / monthly) [US-OHS5-011]. This matches the CCPA.
- **Child support IWO fee (ORC 3121.18):** the employer may deduct the greater of 2 USD or up to 1% of the amount withheld [US-OHS5-010].
- **Not covered:** wage-deduction authorisation rules and the support priority order were not read. Open question.
- **Confidence:** Medium.

## 10 collective_agreements / prevailing wage
- **State prevailing wage (ORC ch. 4115):** the Director of Commerce determines rates (4115.04). Thresholds: 250,000 USD new construction and 75,000 USD remodeling; road, sewer and bridge work 78,258 / 23,447 USD; adjusted biennially under 4115.034 [US-OHR3-002, US-OHR3-003, US-OH-P5-1-003].
- **Not covered:** the certified-payroll obligation (4115.071) was not read. The 2026 adjusted threshold figures come from the DOL table, with the date of adjustment unconfirmed.
- **Confidence:** Medium.

## 11 indexation
- **Minimum wage (Ohio Const. art. II s.34a):** indexed each 1 January by CPI-W for the 12 months to the preceding September (rounded to 5 cents). The small-employer gross-receipts threshold uses the same index, rounded to 1,000. The tipped wage is 50% of the minimum [US-OHS5-006].
  - **2026 derivation:** 10.70 x 317.306 / 308.640 = 11.0004, which gives 11.00 ✓.
  - **2027 derivation:** 11.00 x 328.481 / 317.306 = 11.387, which gives 11.40 ✓. Threshold: 405,000 x 1.03522 = 419,263, which gives 419,000 ✓. Tipped: 5.70 ✓.
  - CPI-W August values come from the BLS API (series CWUR0000SA0, file on disk).
- **SUI wage base:** 9,000 USD, statutory (4141.01) and not indexed. That reading of the statute is not confirmed this pass.
- **Withholding tables:** the commissioner re-issues them within 45 days of a rate change (OAC 5703-7-10) [US-OHS5-017]. Hence the 2026-08-01 edition.
- **Prevailing-wage thresholds:** biennial (4115.034).
- **School district rates:** an annual change list each January [US-OHS5-018].

## 12 data_protection
- **Breach notice (ORC 1349.19):** goes to affected Ohio residents within 45 days of discovery. Personal information includes a name combined with an SSN or an account number [US-OHS5-021].
- **SSN on pay statements:** no SSN-truncation rule for pay statements was located. 4113.14 does not require the SSN [US-OH-P5-1-001].
- **Confidence:** Medium.

## 13 live_legal_change (2026-01-01 to today)
- **HB 96 (136th GA):**
  - flat 2.75% PIT from TY2026 [US-OHS5-007];
  - municipal 718.01 amendments effective 2025-09-30 [US-OH-P5-2-003];
  - 2329.66 amended effective 2025-09-30 [US-OHS5-011].
- **Mid-year withholding tables and formula,** effective 2026-08-01 [US-OH-006, US-OHS5-001].
- **OAC 5703-7-10:** new supplemental rule effective 2026-01-01 [US-OHS5-017].
- **ORC 5747.01:** amended by SB 9, effective 2026-03-05 [US-OHS5-022]. The substance of SB 9 was not analysed.
- **School district changes,** effective 2026-01-01 [US-OHS5-018].
- **Already enacted for 2027:** minimum wage 11.40 / 5.70 [US-OHS5-004].
- **Not yet published:** 2027 withholding tables, 2027 ODJFS rates, 2027 school district changes.
- **Tier-B lead only (not a source):** news from EY and the Ohio CPA society (July 2026) about the 2026-08-01 tables and the 3.4% top withholding rate versus the 2.75% statutory rate. It is consistent with the A.2 files.

## Special populations (US-OWN-005, state round)

| Population | Ohio rule | register_id |
|---|---|---|
| Domestic / household | No Ohio withholding on domestic service in a private home (5747.06(A)(2)); babysitters in the employer's home and live-in companions are exempt from the minimum wage | US-OHS5-008, US-OHS5-004 |
| Agricultural | No Ohio withholding on agricultural labour (IRC 3121(g)) | US-OHS5-008 |
| Minors | Under 16: federal minimum wage 7.25; newspaper carriers under 18: no withholding; Minor Labor Law ORC 4109 (work permits) not read | US-OHS5-005, US-OHS5-008 |
| Tipped | 5.50 (2026) / 5.70 (2027) cash wage, tip credit to the full minimum; threshold more than 30 USD/month in tips | US-OHS5-005, US-OHS5-004 |
| Clergy / religious | No state rule beyond federal located (Ohio AGI follows federal; 5747.06 read) | US-OHS5-008, US-OHS5-022 |
| Students | No state withholding rule located; UI exclusions in 4141.01(B)(3) not read | open |
| Nonresident aliens | No state rule beyond federal located; Ohio withholds on nonresidents generally | US-OHS5-008 |
| Statutory employees | No state rule beyond federal located | US-OHS5-022 |
| Government employees | State and political subdivisions must withhold (5747.06(A)); public employers are outside the 4113.85 employer definition; federal employees are exempt from the Ohio minimum wage | US-OHS5-008, US-OHS5-012, US-OHS5-004 |
| Reciprocity-state residents | IN/KY/MI/PA/WV residents: no Ohio withholding; nonresident military spouse: no withholding | US-MULTI-005, US-OH-P5-2-006 |
| Small employers | Gross under 405,000 (2026) / 419,000 (2027): federal minimum wage; under 150,000: no state overtime duty | US-OHS5-005, US-OHS5-004 |

## ACCESS gaps
- https://tax.ohio.gov/business/employer-withholding: 404/403 shell to scripts. The Wayback copy https://web.archive.org/web/2026id_/https://tax.ohio.gov/business/employer-withholding resolves to 20260923233444 and also gives 404. Tried once.
- https://tax.ohio.gov/employer and https://tax.ohio.gov/business/ohio-business-taxes/employer-withholding: 404 shell. The municipal rate table on tax.ohio.gov could therefore not be read.
- https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/ohio_individual/2026_All_School_Districts.pdf: 404 (no 2026 full list at that path).
- https://jfs.ohio.gov/unemployment-services/for-employers/file-unemployment-taxes/tax-resources/contribution-rates: 404 to curl. The contents are held by US-OH-005 (earlier read) and US-OHS5-002.
- https://thefinder.tax.ohio.gov/: application shell only (lookup per address, no table).
- RITA https://www.ritaohio.com/Businesses/Faqs: HTTP 200 at the root this pass, but the employer FAQ was not re-read (US-OH-014 stays gated).

## Open questions

Mirrors `unresolved[]` of the facts file (same keys, same wording).

- **oh.meta.register_id_pattern** (blocking): 2 facts rest on active register rows whose ids (US-OH-P5-1-001, US-OH-P5-2-006) do not match the facts-schema register_id pattern ^[A-Z]{2}-[A-Z0-9]{2,12}-[0-9]{3,4}$ (multi-hyphen legacy ids). They are carried in full in _facts_pending_register_id_pattern and are NOT yet consumable facts. What would close it: Orchestrator decision: a PATCH of facts.schema.json loosening the register_id pattern (e.g. ^[A-Z]{2}-[A-Z0-9-]{2,16}-[0-9]{3,4}$), or register alias ids; then run _research/synthesis-B/_work-MN-WY/promote.py to move the pending facts into facts[].
- **oh.pit.municipal.rate_table** (blocking): No consolidated official municipal income tax rate table obtained. What would close it: Ohio Department of Taxation municipal rate table (browser pass) or per-municipality ordinances via The Finder.
- **oh.pit.school_district.full_list** (non-blocking): No consolidated 2026 school-district list; 2025 list (US-OHS5-019) + 2026 delta is the basis. What would close it: 2026 IT 1040 booklet SD list (January 2027) or The Finder.
- **oh.payment.method** (non-blocking): Direct deposit / paycard consent: no statute read. What would close it: ORC 4113.15/4113.16 neighbourhood (browser pass).
- **oh.ui.wage_base.indexation** (non-blocking): 9,000 base assumed statutory and fixed (4141.01(G)), not read. What would close it: ORC 4141.01(G)(1) text.
- **oh.leave.other** (non-blocking): Jury duty, military and voting leave with pay impact not read. What would close it: ORC 2313.19, 5903.02, 3599.06.
- **oh.garn.deduction_rules_priority** (non-blocking): Deduction authorisation rules and IWO priority not read. What would close it: ORC 3121.03/3121.034.
- **oh.prevailing_wage.certified_payroll** (non-blocking): 4115.071 certified payroll and 2026 threshold adjustment date not read. What would close it: ORC 4115.071 and Commerce threshold notice.
- **oh.report.ui.channel** (non-blocking): UI quarterly report channel/format not read. What would close it: ODJFS employer portal bulk upload spec.
- **oh.term.ui_separation_notice** (non-blocking): Individual UI separation notice under OAC 4141 not read. What would close it: OAC 4141 rules.
- **oh.pit.tables.next_year** (non-blocking): 2027 withholding tables, ODJFS rates and SD changes not published. What would close it: Re-check January 2027.
- **oh.pit.wh.method.period_a** (non-blocking): The withholding formula for pay dates 2025-10-01..2026-07-31 (1.775/2.990/3.640%, 462.39/2,673.50) sits on US-OH-P5-2-001, status superseded (effective_to 2026-08-01). It remains the correct rule for that window (retro corrections) but cannot be cited as an active fact. What would close it: Merge worker: re-status US-OH-P5-2-001 as historical (in force 2025-10-01..2026-07-31) or register the 2025-10 percentage tables as an active row with effective_to 2026-07-31.
- **oh.sdi_pfml.exists** (non-blocking): "No SDI/TDI/PFML in Ohio" rests on US-OH-P5-1-004 (MANUAL). What would close it: An A.1/A.2 source (DOL TDI/PFML list or ODJFS) registered active.
