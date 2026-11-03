# CCG research pack - annex_OK (Oklahoma)

> **Synthesis C (2026-11-02).** Register ids were normalized to the facts-schema pattern (map: `_research/stage5/ID-RENAME-MAP.csv`, ids in this pack already rewritten). Every fact that was held for the register_id pattern defect (marked here as "legacy id, NOT a fact", "PENDING", "(P)", "parked" or "carried in unresolved") is now a validated fact in `facts[]`; promotion log `_research/synthesis-C/_work/step2-promotion-log.csv`. Counts of held facts quoted below are historical. The Open questions block below mirrors the current `unresolved[]`.

Synthesis-B worker MN-WY, 2026-11-02. Unit `annex_OK` of the CCG (jurisdiction annex, all 13 domains + special populations).
Facts file: `_research/CCG-annex_OK-facts.json` (57 facts, 1 pending on the register_id pattern defect, 9 unresolved). Every claim below carries its register_id inline; numbers may be cited in the CCG only through a fact key.

## 0. How to use this pack

- Body sections 1-13 and Special populations are the stage-5 findings (`_research/stage5/OK.md`), carried verbatim because they are already organised by the 13 CCG domains with register ids inline.
- Federal layer (FIT, FICA, FUTA, W-2/941/940), the multistate rules (reciprocity, sourcing) and the language seams (US-OWN-006: payslip in English; second-language duties attach to notices and posters only) live in annex_FED / annex_MULTI and are not repeated here.
- Special populations (US-OWN-005): the state-level rules are in the Special populations table below; the country-wide coverage matrix is CCG unit `coverage`.
- Values are 2026 unless the fact says otherwise. 2027 values appear only where the row carries an enacted or published 2027 figure; projections are never facts.

## 0.1 Synthesis decisions and traps (bind the builder)

- Two published SUI years: 2026 25,000 (0.2-5.8%) and 2027 24,400 (0.1-5.5%); new employer 1.5% both.
- UI wages INCLUDE 401(k) deferrals; EXCLUDE section 125/127/129.
- Rows relabelled B->A.2 by P9-MERGE (e.g. US-OKP52-005, US-OKP51-001) were NOT used for numbers; US-OK-002 and US-OKS5-* used instead.
- Oracle: OW-2 p.7 semimonthly married 2 allowances 1,825 -> 37.00 (36.67 before rounding).

## 0.2 Register status check of the ids cited in the findings

All ids cited in the findings are `active` in the register.

## 0.3 Facts emitted

| key | value | from | to | register_id | conf |
|---|---|---|---|---|---|
| `ok.labour.minwage.state.follows_federal` | True | 1983-11-01 |  | US-OKS5-001 | high |
| `ok.local_mandates.preempted` | True | 2014-07-01 |  | US-OKS5-002 | high |
| `ok.labour.overtime.state_rule` | none (FLSA only) | 1997-07-01 |  | US-OKS5-017 | high |
| `ok.pay_frequency.rule` | at least twice each calendar month; payday max 11 days after period end (+3 grace) | 2022-11-01 |  | US-OKS5-003 | high |
| `ok.payment.method` | lawful money incl. electronic; deposit at employee-chosen institution; paycard if employee does not designate | 2022-11-01 |  | US-OKS5-003 | medium |
| `ok.labour.dishonoured_check.reimburse_days` | 14 days | 2022-11-01 |  | US-OKS5-003 | high |
| `ok.pit.statutory.bracket.single.1.width` | 3750 USD | 2026-01-01 |  | US-OKS5-009 | high |
| `ok.pit.statutory.bracket.single.2.width` | 1150 USD | 2026-01-01 |  | US-OKS5-009 | high |
| `ok.pit.statutory.bracket.single.3.width` | 2300 USD | 2026-01-01 |  | US-OKS5-009 | high |
| `ok.pit.statutory.rate.2` | 2.5 % | 2026-01-01 |  | US-OKS5-009 | high |
| `ok.pit.statutory.rate.3` | 3.5 % | 2026-01-01 |  | US-OKS5-009 | high |
| `ok.pit.statutory.rate.top` | 4.5 % | 2026-01-01 |  | US-OKS5-009 | high |
| `ok.pit.std_deduction.single` | 6350 USD | 2017-01-01 |  | US-OKS5-011 | high |
| `ok.pit.std_deduction.mfj` | 12700 USD | 2017-01-01 |  | US-OKS5-011 | high |
| `ok.pit.std_deduction.hoh` | 9350 USD | 2017-01-01 |  | US-OKS5-011 | high |
| `ok.pit.allowance.annual` | 1000 USD | 2026-01-01 |  | US-OK-001 | high |
| `ok.wh.method` | OW-2 (Rev. 11-2025) percentage formula or wage-bracket tables | 2026-01-01 |  | US-OK-001 | high |
| `ok.pit.wh.single.annual.thresholds` | 10100;11250;13550 | 2026-01-01 |  | US-OK-001 | high |
| `ok.pit.wh.married.annual.thresholds` | 20200;22500;27100 | 2026-01-01 |  | US-OK-001 | high |
| `ok.pit.rounding` | nearest whole dollar (49c down, 50c up); nothing if quarterly tax < 0.25 | 2026-01-01 |  | US-OKS5-010 | high |
| `ok.pit.oracle.example_1.withholding` | 37.0 USD | 2026-01-01 |  | US-OK-001 | high |
| `ok.wh.certificate` | OK-W-4 (Rev. 3-2021); none on file = Single, 0 allowances | 2019-08-11 |  | US-OKS5-014 | high |
| `ok.wh.supplemental.rate` | 4.5 % | 2026-01-01 |  | US-OKS5-014 | high |
| `ok.pit.nonresident.quarterly_threshold` | 300 USD | 2023-07-01 |  | US-OKS5-010 | high |
| `ok.pit.agricultural.monthly_threshold` | 900 USD | 2023-07-01 |  | US-OKS5-010 | high |
| `ok.pit.nra.rate` | 8 % | 2026-01-01 |  | US-OKS5-009 | medium |
| `ok.local_wage_tax.exists` | False | 2026-01-01 |  | US-OKP9V-001 | high |
| `ok.sui.wage_base` | 25000 USD | 2026-01-01 | 2026-12-31 | US-OK-002 | high |
| `ok.sui.wage_base` | 24400 USD | 2027-01-01 | 2027-12-31 | US-OKS5-018 | high |
| `ok.sui.employer.rate.min` | 0.2 % | 2026-01-01 | 2026-12-31 | US-OK-002 | high |
| `ok.sui.employer.rate.max` | 5.8 % | 2026-01-01 | 2026-12-31 | US-OK-002 | high |
| `ok.sui.employer.rate.min` | 0.1 % | 2027-01-01 | 2027-12-31 | US-OKS5-018 | high |
| `ok.sui.employer.rate.max` | 5.5 % | 2027-01-01 | 2027-12-31 | US-OKS5-018 | high |
| `ok.sui.new_employer.rate` | 1.5 % | 2026-01-01 | 2027-12-31 | US-OKS5-018 | high |
| `ok.ui.average_annual_wage.caliber` | 60993.99 USD | 2027-01-01 | 2027-12-31 | US-OKS5-018 | high |
| `ok.sui.employee.rate` | 0 % | 2025-11-01 |  | US-OKS5-005 | high |
| `ok.sui.wages.401k_included` | True | 2019-07-01 |  | US-OKS5-006 | high |
| `ok.sui.wages.section125_included` | False | 2019-07-01 |  | US-OKS5-006 | high |
| `ok.sui.wage_base.other_state_credit` | True | 2025-11-01 |  | US-OKS5-005 | high |
| `ok.payslip.items` | brief itemized statement of all deductions with each payment | 2022-11-01 |  | US-OKS5-003 | high |
| `ok.records.payroll_tax.retention_years` | 4 years | 2019-08-11 |  | US-OKS5-014 | high |
| `ok.report.wh.return_due` | 20th of month after quarter | 2023-07-01 |  | US-OKS5-010 | high |
| `ok.report.wh.monthly_threshold.quarterly` | 500 USD | 2023-07-01 |  | US-OKS5-010 | high |
| `ok.report.w2.due` | 31 January via OkTAP (EFW2 or manual) | 2023-07-01 |  | US-OKS5-010 | high |
| `ok.report.ui.format` | ICESA 275-character fixed records (E, S, T) | 2024-10-01 |  | US-OKS5-020 | high |
| `ok.newhire.report_days` | 20 days | 2015-11-01 |  | US-OKS5-007 | high |
| `ok.leave.sick.state_statute.exists` | False | 2014-07-01 |  | US-OKS5-002 | high |
| `ok.leave.voting.paid_hours` | 2 hours | 2019-05-06 |  | US-OKS5-023 | high |
| `ok.final_pay.rule` | next regular designated payday (discharge and resignation) | 2005-11-01 |  | US-OKS5-004 | high |
| `ok.term.vacation.payout` | per agreement or established policy | 2022-11-01 |  | US-OKS5-003 | high |
| `ok.garn.creditor.max_percent` | 25 % | 2026-01-01 |  | US-OKS5-013 | high |
| `ok.garn.continuing.lien_days` | 180 days | 2023-11-01 |  | US-OKS5-012 | high |
| `ok.garn.iwo.employer_fee.per_period` | 5 USD | 2026-01-01 |  | US-OKS5-015 | high |
| `ok.garn.iwo.remit_days` | 7 days | 2026-01-01 |  | US-OKS5-015 | high |
| `ok.prevailing_wage.exists` | False | 2015-11-01 |  | US-OKS5-016 | high |
| `ok.data.w2.ssn_last4_allowed` | True | 2019-08-11 |  | US-OKS5-014 | high |
| `ok.data.ssn.mailed_materials_prohibited` | True | 2004-11-01 |  | US-OKS5-008 | high |
| `ok.reciprocity.states` | none | 2026-01-01 |  | US-OKP51-002 (promoted, Synthesis C) | high |

# Findings by domain (stage 5)

## 1 — labour_code
- **Minimum wage:** the state rate equals the **current federal minimum wage** (40 O.S. 197.2), so there is no separate state figure [US-OKS5-001, A.1].
  - ODOL states **USD 7.25/h** [US-OKS5-022, A.3]. The number itself is the FLSA rate (FED unit).
  - **2027:** no state increase is possible without a federal change.
  - **Coverage:** employers with more than 10 FT employees at one location **or** gross business above USD 100,000. The Act does not apply to FLSA-covered employers already paying the federal minimum. The 197.4(e) exclusions are listed in the special-populations table.
- **Local minimum wage:** none. **40 O.S. 160** preempts any municipal minimum wage and any mandatory vacation or sick leave, and voids such ordinances [US-OKS5-002, A.1]. Confidence: high.
- **Overtime:** no state overtime statute exists. The Minimum Wage Act (197.1–197.17) has no overtime section, and ODOL says overtime applies only through the FLSA (1.5x above 40 hours a week) [US-OKS5-017, US-OKS5-022].
- **Pay frequency:** at least twice each calendar month on regular paydays designated in advance. Exempt, state, county, municipal and school-district employees: at least monthly. Payday may fall at most **11 days** after the end of the period, with **3 days** of grace (40 O.S. 165.2) [US-OKS5-003, US-OK-003].
- **Method of payment:**
  - Lawful money, including electronic payment. The employer may, at its discretion, pay by deposit at a financial institution the employee chooses. If the employee does not consent or name one, the employer may pay to a **payroll card** (165.2) [US-OKS5-003].
  - ODOL reads the rule differently: direct deposit may be required, but not at one particular bank unless cash or check is offered, and paycards must be voluntary [US-OKS5-022, A.3].
  - These two readings differ. See Open question OK-OQ-4.
- **Breaks:** none for workers aged 16 or over. Under-16s get 1 hour cumulative rest per 8 consecutive hours, and no more than 5 consecutive hours without 30 minutes of rest (40 O.S. 75) [US-OKS5-017].
- **Dishonoured paycheck:** the employer reimburses the employee's bank fees within 14 days (165.2) [US-OKS5-003].

## 2 — income_tax
- **Rates for TY2026 onward** (68 O.S. 2355(D), Laws 2025 c. 307 / HB 2764) [US-OKS5-009, A.1]:

  | Bracket | Single / MFS | MFJ / QSS / HoH |
  |---|---|---|
  | 0% | first 3,750 | first 7,500 |
  | 2.5% | next 1,150 | next 2,300 |
  | 3.5% | next 2,300 | next 4,600 |
  | 4.5% | remainder | remainder |

- **Standard deduction:** 6,350 / 12,700 / 9,350 (HoH), not indexed. It is identical in all three published versions of 68 O.S. 2358 [US-OKS5-011]. **Personal exemption:** 1,000.
- **Withholding method 2026:** Packet **OW-2 (Rev. 11-2025)**, effective 2026-01-01 [US-OK-001, A.2]. The employer may use the percentage formula or the wage-bracket tables.
  - Allowance = 1,000 / pay periods: weekly 19.23, biweekly 38.46, semimonthly 41.67, monthly 83.33, quarterly 250, semiannual 500, annual 1,000, daily 3.85.
  - **Percentage tables:**

    | Table | Single bands | Married bands |
    |---|---|---|
    | Annual | 0 to 10,100 = 0; 2.5% to 11,250; then 28.75 + 3.5% to 13,550; then 109.25 + 4.5% | 0 to 20,200 = 0; 57.50 at 22,500; 218.50 + 4.5% above 27,100 |
    | Semimonthly | 421 / 469 / 565 | 842 / 938 / 1,129 |
    | Monthly | 842 / 938 / 1,129 | 1,683 / 1,875 / 2,258 |
    | Weekly | 194 / 216 / 261 | 388 / 433 / 521 |
    | Biweekly | 388 / 433 / 521 | 777 / 865 / 1,042 |

  - "Married, but withhold at higher Single rate" uses the Single table.
  - **Rounding:** round the percentage-method result to the nearest whole dollar (49 cents down, 50 cents up). If tax for a quarter would be under USD 0.25, nothing is withheld (68 O.S. 2385.2(B)) [US-OKS5-010].
- **G-DERIVE (done in Python):**
  - The annual thresholds equal the standard deduction plus the statutory band edges: 6,350 + 3,750 = 10,100; +1,150 = 11,250; +2,300 = 13,550. For married: 12,700 + 7,500 = 20,200; 22,500; 27,100.
  - Tier amounts: 1,150 x 2.5% = 28.75; 28.75 + 2,300 x 3.5% = 109.25. For married: 57.50 and 218.50.
  - Per-period thresholds = annual / periods (for example 10,100 / 24 = 420.83, published as 421).
  - **Oracle seed reproduced:** semimonthly, married, 2 allowances, USD 1,825.00 gross. 1,825 - 83.34 = 1,741.66; 9.10 + (1,741.66 - 1,129) x 4.5% = 36.67, rounded to **37.00**. This matches OW-2 p. 7.
- **Certificate:** **Form OK-W-4 (Rev. 3-2021)**, the current edition [US-OKS5-021].
  - Fields: Single / Married / Married but withhold at the higher Single rate; allowances for self, spouse (0 if the spouse works), dependents and additional allowances; additional withholding in USD per period; line 7 Exempt (no liability); line 8 Exempt under MSRRA with **OW-9-MSE**; line 9 Exempt for active-duty military income.
  - A federal W-4 signed before 2018-03-01 still governs. Hires after 2018-02-28 use OK-W-4.
  - **No OK-W-4 on file: withhold as Single with 0 allowances** (OAC 710:90-1-5, 1-7(f)) [US-OKS5-014].
- **Supplemental wages:**
  - If paid together with regular wages and not separated: treat the total as one regular payment.
  - If paid separately or identified: either the **highest rate of 68 O.S. 2355** (**4.5%** for TY2026), or the aggregate method. If no tax was withheld from regular wages, only the aggregate method applies.
  - Overtime, vacation and sick pay are treated as regular wages; paid on top of regular wages they are supplemental [US-OK-005, US-OKS5-014].
  - Note: the rule still cites 2355(B)(1). That cross-reference is out of date; the TY2026 rates sit in 2355(D).
- **Exclusions from withholding wages** (68 O.S. 2385.1(e)) [US-OKS5-010]:
  - farm work of USD 900 or less a month;
  - domestic service in a private home, college club or fraternity/sorority;
  - work outside the trade or business under USD 200 cash in a quarter;
  - **nonresidents with USD 300 or less of Oklahoma income in a quarter**;
  - ministers and members of religious orders.
- **Who is an employee for withholding:** a **resident** is withheld on services performed inside or outside Oklahoma; a **nonresident** only on services performed inside Oklahoma (2385.1(c)) [US-OKS5-010, US-OKP52-001].
  - Residents get a credit for tax paid to the other state on Form 511-TX [US-OKP52-002].
  - **No reciprocity agreements and no local income tax** [US-OKP51-002, US-OKP9V-001, US-OKL-002].
- **Nonresident aliens:** 8% under 68 O.S. 2355(G) and OAC 710:90-1-8 [US-OKS5-009, US-OKS5-014].
  - The wording covers "Oklahoma taxable income paid to nonresident aliens".
  - Open question OK-OQ-2: does this 8% replace table withholding on NRA *wages*?
- **Other withholding:** gambling winnings 4%. Production companies paying loan-out companies withhold at the highest rate (OW-21) [US-OK-004].
- **Live rate change:** the earliest possible 0.25-point cut takes effect **2028-01-01** (62 O.S. 34.103(D)) [US-OKS5-025]. Confidence 95% for 2026; 90% for 2027 (subject to the OW-2 2027 release).

## 3 — social_security (SUI only; no SDI/TDI/PFML)
- **Agency:** Oklahoma Employment Security Commission (OESC).
- **Contributions are employer-only.** The law forbids deducting them from wages (40 O.S. 3-102(A)) [US-OKS5-005]. Fractions of a cent: below half a cent are dropped, half a cent or more goes up to 1 cent.

| Year | Taxable wage base | Rate range | New employer | Conditional factor / state factor | AAW | register_id |
|---|---|---|---|---|---|---|
| 2025 | 28,200 | 0.3%–9.2% | 1.5% | D / 50% | 56,341.77 | US-OKS5-019 |
| 2026 | **25,000** | **0.2%–5.8%** | **1.5%** | A / 30% | 58,765.95 | US-OK-002, US-OKP52-004 |
| 2027 | **24,400** | **0.1%–5.5%** | **1.5%** | none / 29% | 60,993.99 | US-OKS5-018 |

- **Wage-base mechanism (G-DERIVE / G-CALIBER).** The caliber is the **state average annual wage of the second preceding year** published by OESC, times the applicable percentage, rounded to the nearest USD 100 (40 O.S. 1-201(48), 1-223) [US-OKS5-005].
  - **2027:** 40% x 60,993.99 = 24,397.60, rounded to **24,400**. Exact match with the current 1-223(1).
  - **2026:** 42.5% x 58,765.95 = 24,975.53, rounded to **25,000**.
  - **2025:** 50% x 56,341.77 = 28,170.89, rounded to **28,200**.
  - The 2026 and 2025 figures reproduce only with the **pre-amendment** percentages (A = 42.5%, D = 50%). Laws 2025 c. 140 (effective 2025-11-01) cut them to A = 41.25% and D = 45%. The old text was not read; this is an inference from arithmetic (OK-OQ-3).
  - The "AAW" printed on each sheet works as the second-preceding-year figure. It also equals the AWW x 52 on the same sheet.
- **New employer rate:** 1.5% until the employer has 4 quarters of experience within a rate cycle. Four consecutive no-wage reports revert the account to the new-employer rate.
  - Rate notice OES-048 is sent at the end of September. A protest (OES-048P) is due within 20 days.
  - A rate of 3.4% or more cannot rise more than 2 points in two years [US-OKS5-018].
- **UI wages** (40 O.S. 1-218) [US-OKS5-006]:
  - Included: all remuneration, including the cash value of in-kind pay and tips. Anything the IRC treats as wages is UI wages. **Employee 401(k)/403(b)/457/SIMPLE/SEP deferrals ARE UI wages.**
  - Excluded: s.125 payments, s.127/s.129 assistance, employer retirement, health and disability plan payments, meals and lodging provided for the employer's convenience, dismissal pay not required by law or contract, and SUB payments.
- **Other levies:** no SDI, TDI, PFML, LTC, transit or workforce levy. Sources: US-OKP9V-001 (OTC Other Taxes) and US-OKP9V-002 (OESC sheet, no add-on line). The legislative check in US-OKS5-026 found no paid-leave programme enacted.
- Confidence: 95% on the numbers; 85% on the history of the wage-base percentages.

## 4 — payslip_statute
- 40 O.S. 165.2 requires, with each payment of wages, "a brief itemized statement of any and all deductions" [US-OKS5-003, US-OK-003].
  - No other content (hours, rates, gross) is mandated by state law. Gross, hours and rates come from FLSA recordkeeping (FED).
- **Delivery:** paper or **electronic**, per the ODOL FAQ [US-OKS5-022, A.3]. No electronic-consent statute was located.
- **Language:** no clause in the statute [US-OKL-001].
- **Retention:** payroll-tax records are kept **4 years** after the due date or the payment date, whichever is later (OAC 710:90-1-11) [US-OKS5-014]. The record list includes name, address, occupation, SSN, periods of employment, date and amount of each payment, withholding, and the W-4 / OK-W-4.
- **Territorial reach:** the definitions in 165.1(1) cover an employer "employing any person in this state". The rule therefore follows work in Oklahoma.
- Confidence: 90%.

## 5 — reporting_instruments
- **Withholding** (68 O.S. 2385.3; OAC 710:90-3-4) [US-OKS5-010, US-OKS5-014, US-OK-001]:
  - **Quarterly return** (wage withholding return) due the **20th of the month after the quarter**, filed on a calendar-year basis. A zero return is required when no wages were paid.
  - **Remittance:**
    - under USD 500 a quarter (prior fiscal-year average): quarterly, by the 20th;
    - USD 500 or more: monthly, by the 20th of the next month, starting after the first quarter over 500;
    - federal **semiweekly** depositors (average of USD 10,000 or more a month): on the federal semiweekly dates, and returns through EDI;
    - USD 5,000 or more a month: payment must be electronic.
  - **Channel:** OkTAP (oktap.tax.ok.gov). Registration is at tax.ok.gov.
- **W-2 / annual reconciliation** [US-OK-001, US-OKS5-010, US-OKS5-014]:
  - The employee gets the W-2 by **31 January**, or **within 30 days of the last wage payment** if employment ends during the year.
  - W-2/W-3 data goes to the OTC by **31 January** through OkTAP, as an **EFW2** upload (SSA Pub. 42-007) or manual entry. Magnetic media and paper are not accepted.
  - The annual reconciliation is due by 31 January. The penalty is up to USD 1,000 if it is more than 30 days late.
  - The employee statement may show **only the last 4 digits of the SSN**.
- **UI quarterly wage report (OES-3 Employer's Quarterly Contribution Report)** [US-OKS5-020]:
  - Filed online in **EZ Tax Express** (eztaxexpress.oesc.ok.gov), by manual entry or upload. Required on every active account, even with no wages.
  - Upload format: **ICESA**, fixed **275-character** ASCII .txt records ending in CR/LF.
    - Records E, S and T are required; P is optional for TPAs.
    - The S record carries the name as on the Social Security card, in upper case, the SSN, total wages and taxable wages.
  - Late filing: USD 200 + 10% of contributions if the report is not filed within 15 days of Notice OES-054. Interest is 1% a month.
  - **Statutory due date not confirmed from an A source.** The OESC page that held it returns 404 (see ACCESS gaps). Tier-B leads say the last day of the month after the quarter (OK-OQ-1).
- **New hire** (40 O.S. 2-802; OESC page) [US-OKS5-007, US-OKS5-029]:
  - Covers every hire who resides or works in Oklahoma. Due **within 20 days** of the start date, or twice a month (12 to 16 days apart) if filed electronically.
  - Filed with OESC through the online Employer New Hire Reporting System. A copy of the W-4 or a fax is also allowed.
  - Required fields: employee name, address, SSN, start date, state of hire; employer name, address (the payroll address, where IWOs are sent) and FEIN.
  - Optional fields: OESC account number, salary, date of birth, dependent health insurance, still employed?, recall date.
- **Registration:**
  - OTC withholding account at tax.ok.gov (payroll or retirement account) [US-OK-001].
  - OESC account through EZ Tax Express.
  - Power of attorney: BT-129 (OTC) [US-OKP51-004]; OES-190T (OESC) [US-OKP51-005].
- Confidence: 90% (85% on the UI due date).

## 6 — leave
- **Paid sick leave:** no state law, and **local paid sick leave is preempted** (40 O.S. 160) [US-OKS5-002].
  - ODOL: "Oklahoma has no mandatory benefits law". Vacation and sick leave follow employer policy [US-OKS5-022].
  - Confidence: high.
- **PFML/SDI:** none. SB 277 (paid leave) was not enacted [US-OKS5-026].
- **Voting leave:** **2 hours, paid on proof of voting**, with 3 days' notice. It does not apply if the shift leaves 3 hours before or after the polls (26 O.S. 7-101) [US-OKS5-023]. Payroll effect: the hours are paid.
- **Jury duty:** no duty to pay non-exempt employees. The employer may not require or request the use of annual, vacation or sick leave; using paid leave is the employee's choice. Exempt employees keep their salary under the FLSA salary basis, with an offset for jury fees (38 O.S. 34–35; ODOL FAQ) [US-OKS5-024, US-OKS5-022].
- **Military leave (private employers):** not researched. Federal USERRA applies (OK-OQ-6).

## 7 — termination
- **Final pay:** for **both discharge and resignation**, wages are due at the **next regular designated payday**, or by certified mail on request. Offsets and amounts in bona fide dispute are excluded. A CBA can provide otherwise.
  - Penalty for willful failure: liquidated damages of 2% a day, capped at the amount unpaid (40 O.S. 165.3) [US-OKS5-004].
  - ODOL confirms the rule [US-OKS5-022].
- **Accrued vacation:** "wages" include holiday and vacation pay and severance that is "agreed upon … or provided … in an established policy" (165.1(7)) [US-OKS5-003]. Payout at termination therefore depends on the policy. No statute forces payout.
- **Separation notice:** no general UI separation-notice duty was found in Title 40. The only service-letter duty is for public-service corporations and their contractors, on request (40 O.S. 171).
- **W-2 on termination:** within 30 days of the last wage payment [US-OKS5-010].
- **IWO on termination:** notify the support agency within 10 days [US-OKS5-015].
- Confidence: 90%.

## 8 — benefits_in_kind
- **Income tax:** withholding "wages" have the **IRC meaning**, apart from the 2385.1(e) exclusions [US-OKS5-010]. Oklahoma starts from federal AGI.
  - So the federal exclusions carry over: pre-tax 401(k)/403(b)/457, s.125, HSA (employer and s.125), qualified transportation, the first USD 50,000 of group-term life, s.127, s.129.
  - **No Oklahoma departure for wage withholding was found.** The 68 O.S. 2358 adjustments were not reviewed item by item (OK-OQ-5).
- **UI:** departs from income tax. **Elective deferrals are UI wages**, while s.125, s.127 and s.129 are excluded [US-OKS5-006].
- Confidence: 80%.

## 9 — deductions_garnishments
- **Wage deductions:** beyond statutory deductions and court orders, deductions need a **written agreement signed by both**. Examples: loans, advances, overpayments, merchandise, uniforms, insurance, retirement, and breakage or shortage where the employee is solely responsible.
  - Source: ODOL FAQ [US-OKS5-022, A.3]. The underlying rule, OAC 380:30-1-3, was not read (OK-OQ-7).
- **Creditor garnishment:** 75% of earnings from the last 90 days is exempt (31 O.S. 1(A)(18)) [US-OKS5-013]. The maximum is 25%, subject to the federal CCPA floor of 30x the minimum wage.
  - **Continuing earnings garnishment:** a 180-day lien. The garnishee answers and pays within 7 days after each pay period. The earlier lien has priority (12 O.S. 1173.4) [US-OKS5-012].
- **Child support:** maximum 50% / 60%, or 55% / 65% for arrears older than 12 weeks.
  - Priority: current support, then health premiums, then arrears, then other (12 O.S. 1171.2).
  - A creditor garnishment on top of a support order is capped at the state maximum minus the support percentage, and at 25% [US-OKS5-012].
  - **IWO:** effective at the next payment. Remit to the **Centralized Support Registry within 7 days** of payday. Notify within 10 days on termination. The **employer fee is USD 5 per pay period, at most USD 10 a month** (12 O.S. 1171.3) [US-OKS5-015].
- **State tax levies:** not researched.
- Confidence: 90%.

## 10 — collective_agreements (prevailing wage)
- **No state prevailing wage.** The Oklahoma Minimum Wages on Public Works Act (40 O.S. 196.1–196.14) was held unconstitutional in *City of Oklahoma City v. State ex rel. Okla. Dept. of Labor*, 918 P.2d 26 (Okla. 1995), and **repealed by Laws 2015 c. 71, effective 2015-11-01** [US-OKS5-016, A.1; confirms US-OKP51-001].
- Only federal Davis-Bacon certified payroll applies, on federally funded work. ODOL confirms [US-OKS5-022].
- Confidence: 95%.

## 11 — indexation
| Item | Indexed? | Mechanism / publication | register_id |
|---|---|---|---|
| Minimum wage | Follows the federal rate only | 40 O.S. 197.2 | US-OKS5-001 |
| SUI taxable wage base | Yes, yearly | % of the second-preceding-year AAW by conditional factor; OESC "Important Numbers" sheet and contribution-rates page (published by December) | US-OKS5-005, US-OKS5-018 |
| SUI rate range / new-employer rate | Yearly (state experience factor, conditional factor) | Same OESC sheet | US-OKS5-018 |
| PIT brackets / standard deduction / exemption | **Not indexed** | Fixed in statute; rates fall only by the 0.25-point revenue trigger (earliest 2028-01-01) | US-OKS5-009, US-OKS5-011, US-OKS5-025 |
| Withholding tables | When the law changes | OTC Packet OW-2 (Rev. 11-2025 for 2026) | US-OK-001 |
| UI maximum weekly benefit | Yearly | OESC sheet (2026: 649; 2027: 703) | US-OK-002, US-OKS5-018 |

## 12 — data_protection
- **40 O.S. 173.1** [US-OKS5-008] applies to private employers; state and local government are exempt. It forbids:
  - publicly posting or displaying an employee's SSN;
  - printing the SSN on access cards;
  - sending the SSN over the Internet unless the connection is secure or the number is encrypted;
  - using the SSN alone as a website login;
  - **printing the SSN on materials mailed to the employee unless law requires it**.

  An employee may consent in writing.
- **No express rule on pay statements.** A mailed paper payslip falls under (e). Mask the SSN unless it is required.
- The annual withholding statement **may show only the last 4 digits** (OAC 710:90-1-10) [US-OKS5-014].
- OESC new-hire and UI data are confidential (40 O.S. 4-508, heading read only).
- Confidence: 85%.

## 13 — live_legal_change (sweep 2026-01-01 to 2026-11-02)
| Item | Status | Operating level | Payroll effect | register_id |
|---|---|---|---|---|
| HB 2764 / Laws 2025 c. 307: rates 0/2.5/3.5/4.5 from TY2026 | **In force** from 2026-01-01; OW-2 Rev. 11-2025 implements it | Withholding and assessment | 2026 tables | US-OKS5-009, US-OK-001 |
| 62 O.S. 34.103(D) rate-cut trigger | In force; first preliminary certification Dec 2026, final Feb 2027 | Withholding and assessment | Earliest cut 2028-01-01; none in 2027 | US-OKS5-025 |
| Laws 2025 c. 140: UI 1-223 percentages | **In force** from 2025-11-01 | Employer UI contributions | Wage base 24,400 for 2027 | US-OKS5-005, US-OKS5-018 |
| OESC 2027 numbers (no conditional factor, 0.1–5.5%, 24,400) | **Published** (page Last Modified 2025-12-16) | Employer UI contributions | 2027 SUI setup | US-OKS5-018 |
| Laws 2025 c. 401: tip credit tied to the 29 CFR 531.50 cash wage | In force from 2025-11-01 | Minimum wage | Tipped cash wage = federal | US-OKS5-001 |
| SB 277 (paid leave) | **Not enacted**; referred to Appropriations 2026-02-24, no later action | n/a | none | US-OKS5-026 |
| SB 470 (paid leave for incentive recipients) | **Not enacted**; in committee since 2025-02-04 | n/a | none | US-OKS5-026 |
| SB 1986 (state tax exemption for tips/overtime) | **Not enacted**; in committee since 2026-02-03 | n/a | none | US-OKS5-026 |
| SB 1132 (2026) | Health appropriation, law 2026-05-04; **not** an overtime exemption (that was the 2008 SB 1132) | n/a | none | US-OKS5-026 |
| OTC newsroom 2026 | No withholding or employer-filing change announced | n/a | none | US-OKS5-028 |

**Not swept:**
- The 2026 session laws as a whole. The Title files predate them; only targeted bills were checked.
- The ODOL and OESC news pages.

See OK-OQ-8.

## Special populations (state level)
| Population | Oklahoma rule | register_id |
|---|---|---|
| Domestic / household | Exempt from withholding (2385.1(e)(2)). UI covered at USD 1,000 cash in a quarter. Excluded from the state minimum-wage Act (FLSA may still apply). | US-OKS5-010, US-OKS5-006, US-OKS5-001 |
| Agricultural | Withholding exempt if USD 900 a month or less. UI covered at USD 20,000 cash in a quarter or 10+ workers in 20 weeks; H-2A workers excluded. Excluded from the state minimum-wage Act. | US-OKS5-010, US-OKS5-006, US-OKS5-027, US-OKS5-001 |
| Minors | Under 16: hours and rest-break limits; FLSA occupations only. State minimum-wage Act excludes under-18 non-graduates. Newspaper carriers under 18 excluded from UI. | US-OKS5-017, US-OKS5-001, US-OKS5-027 |
| Tipped | Tip credit allowed if the cash wage is at least the federal 29 CFR 531.50(a)(1) amount (Laws 2025 c. 401). UI wages include tips. | US-OKS5-001, US-OKS5-006 |
| Clergy / religious | Ministers and religious orders: exempt from withholding and excluded from UI. Churches and church-controlled organisations: UI excluded. | US-OKS5-010, US-OKS5-027 |
| Students | UI excludes students employed by their own school, spouses in aid programmes, work-study and student nurses. State minimum-wage Act excludes students under 22. | US-OKS5-027, US-OKS5-001 |
| Nonresident aliens | 8% under 68 O.S. 2355(G) / OAC 710:90-1-8. Interaction with table withholding on wages is open (OK-OQ-2). | US-OKS5-009, US-OKS5-014 |
| Nonresidents (US) | Withheld on Oklahoma-sourced services; de minimis USD 300 a quarter. No reciprocity; no convenience rule found. | US-OKS5-010, US-OKP51-002, US-OKP52-001 |
| Military / military spouses | OK-W-4 line 8 (MSRRA, with OW-9-MSE) and line 9 (active-duty military income). | US-OKS5-021 |
| Statutory employees / officers | Corporate officers are "employees" for withholding (2385.1(c)). Otherwise no state rule beyond federal. | US-OKS5-010 |
| Government employees | Paid at least monthly. State employees covered by the minimum-wage Act. Elected officials excluded from UI. Covered by withholding (2385.1(c)). SSN rule (173.1) does not bind the state. | US-OKS5-003, US-OKS5-001, US-OKS5-027, US-OKS5-008 |
| Family employment | UI excludes service for a son, daughter or spouse, and a child under 21 working for a parent. | US-OKS5-027 |
| Insurance / real-estate agents on commission | Excluded from UI. | US-OKS5-027 |
| Part-time (< 25 h/week, not permanent) | Excluded from the state minimum-wage Act (FLSA may apply). | US-OKS5-001 |

## MULTI hand-offs (OK answers)
- **SUI wage-base credit for wages reported to another state: YES.** Taxable wages count wages for services covered by "this act **or other state unemployment compensation acts**" (40 O.S. 1-201(48)) [US-OKS5-005]. PEO and client accounts also get credit for wages already reported (40 O.S. 3-121, read in the same Title 40 file) [US-OKS5-005].
- **PFML/SDI coverage of multistate workers:** not applicable; Oklahoma has no programme.
- **Paid sick leave for employees working partly in the state:** not applicable. There is no state law and local laws are preempted.
- **Pay-statement reach:** 165.1(1) covers an employer "employing any person in this state". The 165.2 deduction statement applies to work in Oklahoma.
- **Withholding:** residents are withheld on all services; nonresidents on Oklahoma services above USD 300 a quarter. No reciprocity and no convenience-of-employer rule was found in 68 O.S. 2385.1 or OAC 710:90.

## Oracle
**official_examples:** the OW-2 2026 percentage-method example (semimonthly, married, 2 allowances, 1,825.00, giving 37.00), reproduced exactly. No OTC withholding calculator was located.

## ACCESS gaps (exact URLs)
- `https://www.oscn.net/applications/oscn/DeliverDocument.asp?CiteID=77475`: HTTP 000 (timeout). Replaced by the Legislature's complete-title RTFs.
- `https://oklahoma.gov/oesc/employers/tax/oklahoma-employers-quarterly-contribution-report.html`: 404.
- `https://oklahoma.gov/oesc/employers/employer-resources-and-forms/oklahoma-employers-quarterly-contribution-report.html`: 404. The Wayback `2026id_` copy (20250222) is also 404. This page should hold the OES-3 due date.
- `https://oksenate.gov/press-releases/sen-corn-rep-smithson-announce-tax-cut-working-oklahomans`: JavaScript bot wall. The Wayback copy (20260710) showed it is a 2008 release.
- `https://eztaxexpress.oesc.ok.gov/Help/UserGuides/UserGuide_Full.pdf` (7 MB): read, not kept. It has no due date.

## Confidence by domain
labour_code 95% · income_tax 95% (2026) / 90% (2027) · social_security 95% · payslip 90% · reporting 90% (UI due date 85%) · leave 90% · termination 90% · BIK 80% · garnishment 90% · prevailing wage 95% · indexation 90% · data protection 85% · live change 80% (sweep targeted, not exhaustive).

## Open questions

Mirrors `unresolved[]` of the facts file (same keys, same wording).

- **ok.report.ui.due_date** (non-blocking): OES-3 due date not confirmed from an A source (OESC page 404). What would close it: OAC 240:10 Employer Contributions subchapter or OESC employer handbook (Chrome pass).
- **ok.pit.nra.wages** (non-blocking): Whether 8% (2355(G)) replaces table withholding on NRA wages is open. What would close it: OTC withholding FAQ/ruling or OAC 710:90-1-8 rulemaking history.
- **ok.ui.wage_base.history** (non-blocking): 2025/2026 bases reproduce only with pre-c.140 percentages (inference). What would close it: Laws 2025 c.140 enrolled text.
- **ok.payment.method** (non-blocking): Statute vs ODOL FAQ differ on paycards. What would close it: OAC 380:30 payment-method rule.
- **ok.bik.departures** (non-blocking): 68 O.S. 2358 adjustments not reviewed item by item. What would close it: Full 2358 text (RTF on disk / re-fetch).
- **ok.leave.military** (non-blocking): State military-leave rights (Title 44) not researched. What would close it: Title 44 text.
- **ok.deduction.rule** (non-blocking): ODOL deduction rule (OAC 380:30-1-3) behind the FAQ not read. What would close it: OAC 380:30-1-3.
- **ok.live.bulletin_sweep** (non-blocking): 2026 session laws effective 2026-11-01 not swept; OW-2 2027 expected Nov 2026. What would close it: 2026 session-laws index (Titles 12, 26, 40, 68), ODOL/OESC news, OW-2 2027.
