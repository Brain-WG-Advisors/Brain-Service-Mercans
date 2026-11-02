# Annex AZ: Arizona

This annex sets out the Arizona payroll rules for the 2026 build year. Read with Annex FED (the federal layer every employee carries) and Annex MULTI (which routes an employee to this State by work location, residence or UI localization). Every value is shown with its effective dates and its source (list at the end of the annex). Federal values are not repeated here.

Classification: T3. Separate State withholding and UI; no local wage tax; local minimum wages in Tucson and Flagstaff.

## AZ.1 Employment and labour code

State minimum wage USD [[FACT:az.minwage.hourly=15.15]] for 2026 and USD [[FACT:az.minwage.hourly=15.65]] for 2027, indexed [[FACT:az.minwage.indexation=each 1 January by Aug-over-Aug CPI-U (US city average), increase rounded to nearest 0.05 (A.R.S. 23-363(B))]]. Cities may set higher rates ([[FACT:az.local_minwage.allowed=True]]); Tucson and Flagstaff do. No State overtime statute: federal overtime applies.

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Minimum wage indexation | [[FACT:az.minwage.indexation=each 1 January by Aug-over-Aug CPI-U (US city average), increase rounded to nearest 0.05 (A.R.S. 23-363(B))]] | from 2021-01-01 |  | S1 |  |
| Minimum wage tip credit max | USD [[FACT:az.minwage.tip_credit.max=3]] | from 2021-01-01 |  | S1 | Employer may pay up to [[FACT:az.minwage.tip_credit.max=3]]/h below the minimum if tips + wages reach it each week. |
| Local minimum wage allowed | [[FACT:az.local_minwage.allowed=True]] | from 2026-01-01 |  | S2 | 23-364(I) (voter-protected) permits county/city ordinances above the state rate; the azleg copy of 23-362 says otherwise. Build rule: local rates apply; flag for counsel. |
| Local minimum wage tucson hourly | USD [[FACT:az.local_minwage.tucson.hourly=15.45]] | 2026-01-01 to 2026-12-31 |  | S3 | Employees with 5+ hours per pay cycle in the city; tip credit max 3.00; State/federal/tribal employers excluded. Derivation: 15.00 x 1.029162 = 15.437 -> [[FACT:az.local_minwage.tucson.hourly=15.45]]. |
| Local minimum wage tucson hourly | USD [[FACT:az.local_minwage.tucson.hourly=16]] | from 2027-01-01 |  | S3 | Published 2027 rate; Derivation [[FACT:az.local_minwage.tucson.hourly=15.45]] x 1.033965 = 15.975 -> [[FACT:az.local_minwage.tucson.hourly=16]]. |
| Cpi u aug2025 over aug2024 percent | [[FACT:az.cpi_u.aug2025_over_aug2024.percent=2.9162]] % | from 2025-08-01 |  | S4 | BLS CPI-U Aug 2024 314.796, Aug 2025 323.976: 323.976/314.796 - 1. |
| Cpi u aug2026 over aug2025 percent | [[FACT:az.cpi_u.aug2026_over_aug2025.percent=3.3965]] % | from 2026-08-01 |  | S4 | BLS CPI-U Aug 2026 334.980 / Aug 2025 323.976 - 1. |
| Pay frequency rule | [[FACT:az.pay_frequency.rule=two or more fixed paydays a month, no more than 16 days apart; monthly allowed for FLSA-exempt staff of out-of-state employers with centralized payroll; up to 5 days held back; OT due within 16 days after period]] | from 2026-01-01 |  | S5 |  |
| Payment method | [[FACT:az.payment.method=cash or negotiable check; direct deposit with written consent; payroll card if DD offered and employee neither consents nor names an institution; one free withdrawal per deposit]] | from 2026-01-01 |  | S5 |  |
| Minor under16 school week max hours | [[FACT:az.minor.under16.school_week_max_hours=18]] hours | from 2026-01-01 |  | S6 | 23-233: in session [[FACT:az.minor.under16.school_week_max_hours=18]] h/week, 3 h/day; outside session 40 h/week, 8 h/day; no night work. |
| Minimum wage hourly | USD [[FACT:az.minwage.hourly=15.15]] | 2026-01-01 to 2026-12-31 |  | S7 | ICA 2026 poster. Agrees with the CPI-U chain 14.70 + [[FACT:az.cpi_u.aug2025_over_aug2024.percent=2.9162]] % = 15.1287, rounded to the nearest 0.05 = [[FACT:az.minwage.hourly=15.15]]. |
| Minimum wage hourly | USD [[FACT:az.minwage.hourly=15.65]] | from 2027-01-01 |  | S8 | ICA 2027 poster read in the PDF viewer (PDF title metadata says 2024; printed text 2027 / [[FACT:az.minwage.hourly=15.65]]). Agrees with [[FACT:az.minwage.hourly=15.15]] + [[FACT:az.cpi_u.aug2026_over_aug2025.percent=3.3965]] % = 15.6646 -> [[FACT:az.minwage.hourly=15.65]]. Not yet linked from the ICA main page on 2026-11-02. |
| Minimum wage tipped cash wage | USD [[FACT:az.minwage.tipped.cash_wage=12.15]] | 2026-01-01 to 2026-12-31 |  | S7 | [[FACT:az.minwage.hourly=15.15]] - 3.00 maximum tip credit (poster: tipped employees may be paid at most 3.00/h less than the minimum wage). |
| Minimum wage tipped cash wage | USD [[FACT:az.minwage.tipped.cash_wage=12.65]] | from 2027-01-01 |  | S8 | [[FACT:az.minwage.hourly=15.65]] - 3.00 maximum tip credit (A.R.S. 23-363(C), az.minwage.tip_credit.max). |
| Local minimum wage flagstaff hourly | USD [[FACT:az.local_minwage.flagstaff.hourly=18.35]] | 2026-01-01 to 2026-12-31 |  | S9 |  |
| Local minimum wage flagstaff hourly | USD [[FACT:az.local_minwage.flagstaff.hourly=18.95]] | from 2027-01-01 |  | S9 |  |
| Local minimum wage flagstaff tip credit applies | [[FACT:az.local_minwage.flagstaff.tip_credit.applies=False]] | from 2026-01-01 |  | S9 | No tip credit in Flagstaff: tipped employees get the full city minimum wage. |
| Local minimum wage flagstaff coverage min hours per year | [[FACT:az.local_minwage.flagstaff.coverage_min_hours_per_year=25]] hours | from 2026-01-01 |  | S9 | Individuals who work or are expected to work [[FACT:az.local_minwage.flagstaff.coverage_min_hours_per_year=25]]+ hours in a calendar year within city limits (City Code Title 15, Prop 414). |

⚠️ RESEARCH-GAP (non-blocking): Minimum wage statute 23 362 current: not established by the research. Source that would close it: Current 23-362 text (Prop. 202) via azleg or Westlaw public.

## AZ.2 Income tax withholding

**Method.** [[FACT:az.wh.method=flat percentage of gross taxable wages (federal IRC 3401 wages, W-2 box 1) elected on Form A-4]]. The employee elects one of [[FACT:az.wh.rate_options=0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5 percent]] on Form A-4; without an election the default is [[FACT:az.wh.default_rate=2]] %. Supplemental pay: [[FACT:az.wh.supplemental.rate=same elected percentage (no separate supplemental rate)]]. Excluded from withholding: [[FACT:az.wh.exclusions=nonresident common-carrier employees; domestic service in private home; casual labour; seasonal hand farm labour; nonresidents present < 60 days (not athletes/entertainers); disaster-recovery workers]].

```
period_tax = period_federal_FIT_wages x elected_percentage      # W-2 box 1 wages
```

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Withholding method | [[FACT:az.wh.method=flat percentage of gross taxable wages (federal IRC 3401 wages, W-2 box 1) elected on Form A-4]] | from 2026-01-01 |  | S10 | A.R.S. 43-401(A),(E). Same percentage applies to bonus and other emolument: no separate supplemental rate (medium-high). |
| Withholding rate options | [[FACT:az.wh.rate_options=0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5 percent]] | from 2026-01-01 |  | S10 |  |
| Withholding default rate | [[FACT:az.wh.default_rate=2]] % | from 2026-01-01 |  | S10 | Until the employee elects; A-4 due within 5 days of hire. Zero-percent election renewed yearly. |
| Withholding supplemental rate | [[FACT:az.wh.supplemental.rate=same elected percentage (no separate supplemental rate)]] | from 2026-01-01 |  | S11 |  |
| Withholding december OPT out | [[FACT:az.wh.december_opt_out=True]] | from 2026-01-01 |  | S11 | 43-401(B),(F): employer may elect not to withhold in December; tell ADOR and employees before 1 July. |
| Withholding a4c remit days after quarter | [[FACT:az.wh.a4c.remit_days_after_quarter=15]] days | from 2026-01-01 |  | S11 | A-4C credit-contribution reduction; employee statement within 30 days after year end or [[FACT:az.wh.a4c.remit_days_after_quarter=15]] days after termination. |
| Withholding exclusions | [[FACT:az.wh.exclusions=nonresident common-carrier employees; domestic service in private home; casual labour; seasonal hand farm labour; nonresidents present < 60 days (not athletes/entertainers); disaster-recovery workers]] | from 2026-01-01 |  | S12 | A.R.S. 43-403. |

⚠️ RESEARCH-GAP (non-blocking): Withholding rounding: not established by the research. Source that would close it: A.A.C. R15-2B-101 on azsos.gov.

## AZ.2b Non-resident regime and reciprocity

Non-residents are withheld after [[FACT:az.nonres.withholding_days_threshold=60]] days in Arizona in the year. Residents of [[FACT:az.nonres.wec_states=CA, IN, OR, VA]] may claim exemption on Form WEC (one-way: the credit is claimed at assessment).

**Resident / non-resident matrix (Arizona income tax)**

| Income type | Resident | Non-resident |
|---|---|---|
| Regular salary | Elected percentage of federal FIT wages | Elected percentage on Arizona wages after the [[FACT:az.nonres.withholding_days_threshold=60]]-day threshold; WEC exemption for residents of the listed States |
| Annual bonus / supplemental pay | Same elected percentage | Same, on the Arizona portion |
| Severance | Same elected percentage (federal wage definition) | Same, on the Arizona portion |
| Equity | Same elected percentage; classification of equity income open at federal level (Annex FED, FED.2b) | Same, on the Arizona portion |
| Benefits in kind | Included where in federal FIT wages | Same, on the Arizona portion |
| Contractor pay | Out of scope | Out of scope |

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Non-resident withholding days threshold | [[FACT:az.nonres.withholding_days_threshold=60]] days | from 2026-01-01 |  | S12 | Nonresident withheld after [[FACT:az.nonres.withholding_days_threshold=60]] days (or earlier by agreement). Form WEC exemptions: residents of CA, IN, OR, VA claiming the credit (unilateral; assessment-level credit 43-1096), MSRRA spouses, Native Americans on own reservation. Resident working outside AZ may opt in with A-4V. |
| Non-resident wec states | [[FACT:az.nonres.wec_states=CA, IN, OR, VA]] | from 2026-01-01 |  | S10 |  |

## AZ.2c Local wage taxes

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Local wage tax exists | [[FACT:az.local_wage_tax.exists=False]] | from 2026-01-01 |  | S13 |  |

## AZ.3 Social insurance: unemployment, disability, paid leave and payroll levies

Employer-only UI ([[FACT:az.sui.employee.rate=0]] % employee) on wages up to the base. From 2027 experience-rated employers pay [[FACT:az.ui_operating_fund.rate_of_ui_liability=3.15]] % of their UI liability into the UI Operating Fund, with UI liability reduced by the same amount. No SDI, TDI or PFML ([[FACT:az.sdi_pfml.exists=False]]).

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| SUI wage base | USD [[FACT:az.sui.wage_base=8,000]] | from 2026-01-01 |  | S14 | Fixed (7,000 before 2023); not indexed. |
| SUI new employer rate | [[FACT:az.sui.new_employer.rate=2]] % | 2026-01-01 to 2026-12-31 |  | S14 |  |
| SUI employer rate min | [[FACT:az.sui.employer.rate.min=0.03]] % | 2026-01-01 to 2026-12-31 |  | S15 | 2026 adjusted rates 0.03%-8.36% (UIT-0603A, A.R.S. 23-730). |
| SUI employer rate max | [[FACT:az.sui.employer.rate.max=8.36]] % | 2026-01-01 to 2026-12-31 |  | S14 |  |
| SUI employee rate | [[FACT:az.sui.employee.rate=0]] % | from 2026-01-01 |  | S16 | "You cannot take these taxes out of employee pay." |
| UI operating fund rate of UI liability | [[FACT:az.ui_operating_fund.rate_of_ui_liability=3.15]] % | from 2027-01-01 |  | S17 | Each quarter of 2027 experience-rated employers pay [[FACT:az.ui_operating_fund.rate_of_ui_liability=3.15]] % of UI liability to the UI Operating Fund (NOT 2026). |
| SDI PFML exists | [[FACT:az.sdi_pfml.exists=False]] | from 2026-01-01 |  | S18 | No SDI/PFML or other levy. |

⚠️ RESEARCH-GAP (non-blocking): UI separation notice and domestic threshold: not established by the research. Source that would close it: A.R.S. 23-613.01 / 23-615 text on azleg.gov or the DES employer handbook section on separation notices.

## AZ.4 Pay statement

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Payslip required when | [[FACT:az.payslip.required_when=only for direct deposit or payroll card: written or electronic statement of earnings and withholdings, no content list (23-351(E),(F))]] | from 2026-01-01 |  | S5 |  |
| Payslip sick time fields | [[FACT:az.payslip.sick_time_fields=sick time available; sick time used year to date; pay received as sick time (on paycheck or attachment, every regular paycheck)]] | from 2017-07-01 |  | S19 | A.R.S. 23-375(C); hard PSL/DD field set. |

## AZ.5 Statutory reporting

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Report withholding annual due | [[FACT:az.report.wh.annual.due=A1-R with W-2s due 31 January (43-412(B)); 30-day extension for good cause]] | from 2026-01-01 |  | S20 |  |
| Report W-2 format | [[FACT:az.report.w2.format=EFW2 (Pub 701 rev. Jan 2025): mandatory electronic .txt via AZTaxes/AZFSET/transmitter; RS required, RV optional, state code 04; no SSN/EIN truncation; 1099s with AZ withholding direct to ADOR (Pub 1220)]] | from 2025-01-01 |  | S21 | Edition: Jan 2025 text speaks of calendar 2024; 2026 edition not located. |
| Newhire report days | [[FACT:az.newhire.report_days=20]] days | from 2026-01-01 |  | S22 | 23-722.01: DES; electronic two transmissions a month <=16 days apart; includes first day of paid work; no employer penalty. |
| Report withholding deposit schedule | [[FACT:az.report.wh.deposit_schedule=under 200 average: annual A1-APR due 31 Jan; 200-1,500: quarterly; over 1,500: federal schedule; EFT mandatory at 500+; A1-QRT quarterly even if zero (+10 days for timely payers)]] | from 2026-01-01 |  | S23 |  |
| Report SUI quarterly | [[FACT:az.report.sui.quarterly=UC-018 Unemployment Tax and Wage Report (continuation UC-020; 2027 paper version named UIT-0018F); employees listed alphabetically or by SSN with total wages for the quarter in which PAID; Section A monthly count of employees in the pay period including the 12th; every page carries employer name, account number, quarter/year; online via the Tax and Wage System (TWS)]] | from 2026-01-01 |  | S24 |  |
| Report SUI due dates | [[FACT:az.report.sui.due_dates=Apr 30 / Jul 31 / Oct 31 / Jan 31 (next business day if weekend or state holiday); file every quarter even with no wages]] | from 2026-01-01 |  | S25 |  |
| Report SUI late penalty | [[FACT:az.report.sui.late_penalty=late report: 0.1% of total quarterly wages, minimum 35 USD, maximum 200 USD; interest 1% per month or part month on unpaid tax]] | from 2026-01-01 |  | S25 |  |
| Report SUI uiof line | [[FACT:az.report.sui.uiof_line=From CY2027 experience-rated employers pay 3.15% of UI liability into the UI Operating Fund; UI liability reduced by the same amount; a new UIOF line on UIT-0018F Section B, TWS and bulk files; only the UI contribution is reportable for FUTA credit on Form 940]] | from 2027-01-01 |  | S26 |  |

⚠️ RESEARCH-GAP (non-blocking): Report W-2 Pub. 701 edition: not established by the research. Source that would close it: the ADOR Pub 701 2026 edition

## AZ.6 Leave

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Leave sick accrual hours worked per hour | [[FACT:az.leave.sick.accrual.hours_worked_per_hour=30]] hours | from 2017-07-01 |  | S27 |  |
| Leave sick cap hours 15 plus | [[FACT:az.leave.sick.cap_hours.15_plus=40]] hours | from 2017-07-01 |  | S27 | Yearly cap [[FACT:az.leave.sick.cap_hours.15_plus=40]] h (15+ employees) / 24 h (fewer than 15) unless higher. |
| Leave sick cap hours under 15 | [[FACT:az.leave.sick.cap_hours.under_15=24]] hours | from 2017-07-01 |  | S27 |  |
| Leave sick waiting days | [[FACT:az.leave.sick.waiting_days=90]] days | from 2017-07-01 |  | S27 |  |
| Leave sick rehire reinstatement months | [[FACT:az.leave.sick.rehire_reinstatement_months=9]] months | from 2017-07-01 |  | S27 |  |
| Leave sick payout on separation | [[FACT:az.leave.sick.payout_on_separation=False]] | from 2017-07-01 |  | S27 | 23-372(F). Paid at normal hourly rate, never below minimum wage; State of AZ and federal employers excluded. |

## AZ.7 Termination and final pay

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Final pay discharge | [[FACT:az.final_pay.discharge=within 7 working days or end of next regular pay period, whichever sooner; resignation: regular payday of the period]] | from 2026-01-01 |  | S28 | 23-353. No vacation-payout rule. |

## AZ.8 Benefits in kind and taxable wages

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Irc conformity date | [[FACT:az.irc_conformity_date=2026-01-01]] | from 2026-01-01 |  | S29 | 43-105(A); withholding base = federal wages, so federal exclusions flow through. |

⚠️ RESEARCH-GAP (non-blocking): PIT departures from federal: not established by the research. Source that would close it: ADOR Form 140 instructions 2026.

## AZ.9 Deductions and garnishments

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Deductions rule | [[FACT:az.deductions.rule=only when required by law, with prior revocable written authorization, or during a good-faith wage dispute (23-352)]] | from 2026-01-01 |  | S30 |  |
| Garnishment creditor max percent | [[FACT:az.garn.creditor.max_percent=10]] % | from 2026-01-01 |  | S31 |  |
| Garnishment creditor minimum wage multiple | [[FACT:az.garn.creditor.minwage_multiple=60]] ratio | from 2026-01-01 |  | S31 |  |
| Garnishment child support remit business days | [[FACT:az.garn.child_support.remit_business_days=2]] business days | from 2026-01-01 |  | S32 | 25-504: start within 14 days; employer fee 1 per payment, max 4/month; report termination within 10 days; support priority. |
| Garnishment child support employer fee per payment | USD [[FACT:az.garn.child_support.employer_fee_per_payment=1]] | from 2026-01-01 |  | S32 |  |
| Garnishment child support employer fee monthly max | USD [[FACT:az.garn.child_support.employer_fee_monthly_max=4]] | from 2026-01-01 |  | S32 |  |

⚠️ RESEARCH-GAP (non-blocking): Garnishment creditor statute conflict: not established by the research. Source that would close it: Effective date of the Prop. 209 10% amendment and A.R.S. 25-510 text on azleg.

## AZ.10 Collective agreements and prevailing wage

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Prevailing wage state mandate exists | [[FACT:az.prevailing_wage.state_mandate.exists=False]] | from 2026-01-01 |  | S33 | 34-321(B) bars agencies from requiring prevailing wage. |

## AZ.12 Payroll data protection and records

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Records payroll retention years | [[FACT:az.records.payroll.retention_years=4]] years | from 2026-01-01 |  | S2 | 23-364(D): hours each day, wages, sick time paid; employee may inspect and copy. |

## AZ.13 Live legal change

From 2027: State minimum wage USD [[FACT:az.minwage.hourly=15.65]], Tucson USD [[FACT:az.local_minwage.tucson.hourly=16]], Flagstaff USD [[FACT:az.local_minwage.flagstaff.hourly=18.95]]; UI Operating Fund [[FACT:az.ui_operating_fund.rate_of_ui_liability=3.15]] % of UI liability. Arizona conforms to the Internal Revenue Code as of [[FACT:az.irc_conformity_date=2026-01-01]]. The 2026 agency bulletins are not swept (gap below).

⚠️ RESEARCH-GAP (non-blocking): Live bulletin sweep: not established by the research. Source that would close it: the ADOR news archive and DES employer bulletins for 2026

## AZ.15 Special populations

- Domestic workers: no Arizona withholding (43-403(A)(2)); Tucson minimum wage excludes casual babysitting; UI threshold open (AZ.3).
- Agricultural workers: no withholding for seasonal hand field labour except machine operators (who may elect).
- Minors: hour limits for under-16s (table in AZ.1); under-18 newspaper carriers excluded from UI.
- Tipped employees: tip credit up to USD [[FACT:az.minwage.tip_credit.max=3]] (State and Tucson); no tip credit in Flagstaff.
- Clergy: churches and ministers excluded from UI; no withholding exception.
- Students: own-school students, student nurses and interns, co-op students excluded from UI.
- Non-resident aliens and statutory employees: no Arizona rule beyond the federal one; non-resident day threshold (AZ.2b).
- Government: the sick-time law and the Tucson minimum wage exclude State and federal employers.
- Native Americans working on their own reservation and military spouses: WEC exemption.
- Non-resident common-carrier, motion-picture and disaster-recovery workers: excluded.

⚠️ RESEARCH-GAP (non-blocking): the coverage thresholds that apply to these populations (quarterly cash-wage and headcount thresholds for UI coverage of domestic, agricultural and non-profit employment) are cited by statute only and carry no facts key; the engine must not hard-code them until they are keyed.

## AZ.16 Language

The sick-time notice must be in English and Spanish (23-375(B)); minimum-wage and sick-time posters in both languages. The pay statement itself is in English.

## AZ.S Sources

| Ref | Instrument | Article / section | Authority |
|---|---|---|---|
| S1 | A.R.S. 23-363 Minimum wage (Fair Wages and Healthy Families Act, Prop. 206 of 2016) | 23-363(A)-(C) | Arizona State Legislature (azleg.gov, A.R.S.) |
| S2 | A.R.S. 23-364 Enforcement (records, posting, hire notice, local minimum wages) | 23-364(D),(F),(G),(I) | Arizona State Legislature (azleg.gov, A.R.S.) |
| S3 | City of Tucson - Tucson Minimum Wage Act page (Prop. 206 of 2021) | page | City of Tucson, Business Services Department (Labor Standards Unit) |
| S4 | BLS CPI-U US city average, all items (CUUR0000SA0), August values | August 2024, 2025, 2026 | US Bureau of Labor Statistics |
| S5 | A.R.S. 23-351 Designation of paydays; payment methods; earnings statement | 23-351(A)-(K) | Arizona State Legislature (azleg.gov, A.R.S.) |
| S6 | A.R.S. 23-233 Hours of labor for persons under 16 | 23-233(A)-(D) | Arizona State Legislature (azleg.gov, A.R.S.) |
| S7 | ICA poster 'The Fair Wages and Healthy Families Act' 2026 (English) | Poster header; Tips and Gratuities | Industrial Commission of Arizona |
| S8 | ICA poster 'The Fair Wages and Healthy Families Act' 2027 (English) | Poster header | Industrial Commission of Arizona |
| S9 | City of Flagstaff - Minimum Wage page (Office of Labor Standards) | 2026 Minimum Wage; 2027 Minimum Wage; Background | City of Flagstaff |
| S10 | ADOR Withholding Tax page (live copy 2026-11-02) | page | Arizona Department of Revenue |
| S11 | A.R.S. 43-401 Withholding tax; rates; election by employee (local copy) | 43-401(A),(B),(E)-(H) | Arizona State Legislature (azleg.gov, A.R.S.) |
| S12 | A.R.S. 43-403 Employment excluded from withholding | 43-403(A)-(D) | Arizona State Legislature (azleg.gov, A.R.S.) |
| S13 | ADOR Pub 10 Summary of Arizona Taxes (Feb 2022) | whole publication (2 pp.) | Arizona Dept of Revenue |
| S14 | Arizona DES UIT-0603A Unemployment Insurance Tax Rate Chart 2026 | ARS 23-730 adjusted rates | Arizona Department of Economic Security |
| S15 | UIT-0603A Unemployment Insurance Tax Rate Chart (calendar year 2026) | whole chart (form rev. 12/25) | Arizona Dept of Economic Security (DES) |
| S16 | DES Payment Taxes - Overview (Arizona UI employer) | sections Calculating Taxable Wages; Wage Limits | Arizona Dept of Economic Security (DES) |
| S17 | DES Unemployment Insurance Operating Fund (UIOF) | Key Provisions | Arizona Dept of Economic Security (DES) |
| S18 | Arizona Senate Research Staff brief: Unemployment Insurance (2024) | Introduction; Discontinued Surcharges | Arizona State Senate Research Staff |
| S19 | A.R.S. 23-375(C) Earned paid sick time balances on the paycheck | 23-375(C) | Arizona State Legislature (azleg.gov, A.R.S.) |
| S20 | A.R.S. 43-412 Returns of withholding (annual return due 31 January) | 43-412(A),(B) | Arizona State Legislature (azleg.gov, A.R.S.) |
| S21 | ADOR Pub 701 Submitting Forms A1-R/A1-APR and W-2, W-2c, W-2G, 1099 (rev. Jan 2025) | Pub 701 (3 pp.) | Arizona Department of Revenue |
| S22 | A.R.S. 23-722.01 New hire reporting | 23-722.01(A)-(E),(K),(M) | Arizona State Legislature (azleg.gov, A.R.S.) |
| S23 | ADOR Employer Withholding Filing Obligations (Wayback 2026-10-09) | Employer Withholding Filing Obligations | Arizona Department of Revenue |
| S24 | DES - Reporting Wages - Completing the Reports (UC-018 / UC-020) | Form Availability; How to Prepare; Section A; Multiple Pages; Avoid Penalties; Online Filing | Arizona Department of Economic Security |
| S25 | DES - Reporting Wages and Paying Taxes - Schedule (UI quarterly wage report) | Unemployment Insurance Tax Wage Report Schedule; Late Penalties and Interest | Arizona Department of Economic Security |
| S26 | DES - Unemployment Insurance Operating Fund (UIOF) page + Unemployment-Employer announcements | Key Provisions; calculation example; Filing; FUTA Reporting Notes | Arizona Department of Economic Security |
| S27 | A.R.S. 23-372 Accrual of earned paid sick time | 23-372(A)-(F) | Arizona State Legislature (azleg.gov, A.R.S.) |
| S28 | A.R.S. 23-353 Payment of wages of discharged employee | 23-353(A)-(D) | Arizona State Legislature (azleg.gov, A.R.S.) |
| S29 | A.R.S. 43-105 Internal Revenue Code conformity date | 43-105(A) | Arizona State Legislature (azleg.gov, A.R.S.) |
| S30 | A.R.S. 23-352 Withholding of wages (deduction authorization) | 23-352(1)-(3) | Arizona State Legislature (azleg.gov, A.R.S.) |
| S31 | A.R.S. 33-1131 Exempt earnings (creditor garnishment and support limits) | 33-1131(A)-(D) | Arizona State Legislature (azleg.gov, A.R.S.) |
| S32 | A.R.S. 25-504 Order of assignment for support (Arizona income withholding) | 25-504(E),(F),(H),(P) | Arizona State Legislature (azleg.gov, A.R.S.) |
| S33 | A.R.S. 34-321 (public works wage rates) | 34-321(B) | Arizona Legislature |
