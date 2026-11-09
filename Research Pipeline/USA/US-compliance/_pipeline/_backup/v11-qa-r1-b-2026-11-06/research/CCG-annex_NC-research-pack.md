# CCG research pack - annex_NC (North Carolina)

> **Synthesis C (2026-11-02).** Register ids were normalized to the facts-schema pattern (map: `_research/stage5/ID-RENAME-MAP.csv`, ids in this pack already rewritten). Every fact that was held for the register_id pattern defect (marked here as "legacy id, NOT a fact", "PENDING", "(P)", "parked" or "carried in unresolved") is now a validated fact in `facts[]`; promotion log `_research/synthesis-C/_work/step2-promotion-log.csv`. Counts of held facts quoted below are historical. The Open questions block below mirrors the current `unresolved[]`.

Synthesis-B worker MN-WY, 2026-11-02. Unit `annex_NC` of the CCG (jurisdiction annex, all 13 domains + special populations).
Facts file: `_research/CCG-annex_NC-facts.json` (46 facts, 3 pending on the register_id pattern defect, 10 unresolved). Every claim below carries its register_id inline; numbers may be cited in the CCG only through a fact key.

## 0. How to use this pack

- Body sections 1-13 and Special populations are the stage-5 findings (`_research/stage5/NC.md`), carried verbatim because they are already organised by the 13 CCG domains with register ids inline.
- Federal layer (FIT, FICA, FUTA, W-2/941/940), the multistate rules (reciprocity, sourcing) and the language seams (US-OWN-006: payslip in English; second-language duties attach to notices and posters only) live in annex_FED / annex_MULTI and are not repeated here.
- Special populations (US-OWN-005): the state-level rules are in the Special populations table below; the country-wide coverage matrix is CCG unit `coverage`.
- Values are 2026 unless the fact says otherwise. 2027 values appear only where the row carries an enacted or published 2027 figure; projections are never facts.

## 0.1 Synthesis decisions and traps (bind the builder)

- Withholding rate 4.09% (= 3.99% statutory + 0.1%) - do not use 3.99% in the WTC.
- 2027 3.49% is a projection on a revenue trigger - do NOT model until NCDOR publishes the 2027 NC-30.
- NRA add-on rounded UP (11/21/22/44) while general rounding is to nearest dollar.
- Oracle: NC-30 examples 4 (percentage and annualized, 450 weekly single 2 allowances) and NRA 21 reproduced.

## 0.2 Register status check of the ids cited in the findings

These ids appear in the findings but are not plain `active`; do not cite them for a number:

- US-NCP51-005: MANUAL
- US-NCW1B-002: superseded
- US-NCS5-019: partial
- US-NCS5-027: partial
- US-NCS5-030: partial

## 0.3 Facts emitted

| key | value | from | to | register_id | conf |
|---|---|---|---|---|---|
| `nc.labour.minwage.state.follows_federal` | True | 2006-08-23 |  | US-NCS5-002 | high |
| `nc.labour.minwage.student_learner.hourly` | 6.5 USD | 2026-01-01 |  | US-NCS5-002 | high |
| `nc.local_mandates.preempted` | True | 2023-10-03 |  | US-NCS5-001 | high |
| `nc.overtime.weekly_threshold_hours` | 40 hours | 1991-06-19 |  | US-NCS5-003 | high |
| `nc.overtime.premium.multiplier` | 1.5 ratio | 1991-06-19 |  | US-NCS5-003 | high |
| `nc.labour.pay_frequency.allowed` | daily; weekly; biweekly; semimonthly; monthly | 2026-01-01 |  | US-NCS5-005 | high |
| `nc.pit.rate.flat` | 3.99 % | 2026-01-01 |  | US-NCS5-011 | high |
| `nc.pit.wh.rate` | 4.09 % | 2026-01-01 | 2026-12-31 | US-NC-001 | high |
| `nc.pit.std_deduction.single` | 12750 USD | 2026-01-01 |  | US-NCS5-010 | high |
| `nc.pit.std_deduction.head_of_household` | 19125 USD | 2026-01-01 |  | US-NCS5-010 | high |
| `nc.pit.std_deduction.mfj` | 25500 USD | 2026-01-01 |  | US-NCS5-010 | high |
| `nc.pit.allowance.amount` | 2500 USD | 2026-01-01 | 2026-12-31 | US-NC-001 | high |
| `nc.pit.rounding` | nearest whole dollar (NRA add-on rounded up) | 2026-01-01 | 2026-12-31 | US-NC-001 | high |
| `nc.pit.nra.addon.weekly` | 11 USD | 2026-01-01 | 2026-12-31 | US-NC-001 | high |
| `nc.pit.nra.addon.biweekly` | 21 USD | 2026-01-01 | 2026-12-31 | US-NC-001 | high |
| `nc.pit.nra.addon.semimonthly` | 22 USD | 2026-01-01 | 2026-12-31 | US-NC-001 | high |
| `nc.pit.nra.addon.monthly` | 44 USD | 2026-01-01 | 2026-12-31 | US-NC-001 | high |
| `nc.pit.oracle.example_1.withholding` | 4 USD | 2026-01-01 | 2026-12-31 | US-NC-001 | high |
| `nc.pit.oracle.example_2.nra_withholding` | 21 USD | 2026-01-01 | 2026-12-31 | US-NC-001 | high |
| `nc.wh.certificate` | no NC-4: single, zero allowances; federal W-4 not acceptable | 2026-01-01 |  | US-NC-001 | high |
| `nc.wh.supplemental.rate` | 4.09 % | 2026-01-01 | 2026-12-31 | US-NC-001 | high |
| `nc.reciprocity.states` | none | 2026-01-01 |  | US-NC-001 | high |
| `nc.sui.wage_base` | 34200 USD | 2026-01-01 | 2026-12-31 | US-NCB5-401 | high |
| `nc.sui.wage_base.other_state_credit` | True | 2026-01-01 |  | US-NCS5-015 | high |
| `nc.sui.new_employer.rate` | 1.0 % | 2026-01-01 | 2026-12-31 | US-NCS5-014 | high |
| `nc.ui.rate.base` | 1.9 % | 2026-01-01 | 2026-12-31 | US-NCP9V-001 | high |
| `nc.sui.employer.rate.min` | 0.06 % | 2026-01-01 | 2026-12-31 | US-NCP9V-001 | high |
| `nc.sui.employer.rate.max` | 5.76 % | 2026-01-01 | 2026-12-31 | US-NCP9V-001 | high |
| `nc.sui.employee.rate` | 0 % | 2026-01-01 |  | US-NCS5-014 | high |
| `nc.records.wage_hour.retention_years` | 3 years | 1980-11-01 |  | US-NCS5-022 | high |
| `nc.records.withholding.retention_years` | 10 years | 2026-01-01 |  | US-NC-001 | high |
| `nc.report.wh.quarterly_threshold.monthly_avg` | 250 USD | 2026-01-01 |  | US-NC-001 | high |
| `nc.report.wh.semiweekly_threshold.monthly_avg` | 2000 USD | 2026-01-01 |  | US-NC-001 | high |
| `nc.report.nc3.due` | January 31, electronic (eNC3) | 2026-01-01 |  | US-NC-001 | high |
| `nc.report.efile_spec.version` | 9-2026 (TY2026, use beginning January 2027) | 2027-01-01 |  | US-NCS5-028 | high |
| `nc.report.ui.quarterly_due` | Apr 30; Jul 31; Oct 31; Jan 31 | 2026-01-01 |  | US-NCS5-025 | high |
| `nc.newhire.report_days` | 20 days | 2026-01-01 |  | US-NCS5-020 | high |
| `nc.leave.sick.state_statute.exists` | False | 2023-10-03 |  | US-NCS5-001 | high |
| `nc.final_pay.rule` | next regular payday (discharge and resignation) | 2026-01-01 |  | US-NCS5-006 | high |
| `nc.term.vacation.payout` | per employer policy; forfeiture only with advance written notice | 2026-01-01 |  | US-NCS5-008 | high |
| `nc.term.final_w2.days` | 30 days | 2026-01-01 |  | US-NC-001 | high |
| `nc.bik.conformity.irc_date` | 2025-07-05 | 2026-01-01 |  | US-NCS5-029 | high |
| `nc.garn.support.max_rate` | 40 % | 2026-01-01 |  | US-NCS5-018 | high |
| `nc.garn.support.employer_fee.per_period` | 1 USD | 2026-01-01 |  | US-NCS5-018 | high |
| `nc.garn.tax_levy.max_rate` | 10 % | 2026-01-01 |  | US-NCS5-021 | high |
| `nc.data.ssn.mailing_restricted` | True | 2026-01-01 |  | US-NCS5-016 | high |
| `nc.local_wage_tax.exists` | False | 2026-01-01 |  | US-NCP51-001 (promoted, Synthesis C) | high |
| `nc.payslip.items` | itemized statement of deductions each pay period with deductions; wage notice at hire | 2026-01-01 |  | US-NCW1B-003 (promoted, Synthesis C) | high |
| `nc.prevailing_wage.exists` | False | 2026-01-01 |  | US-NCP51-004 (promoted, Synthesis C) | medium |

# Findings by domain (stage 5)

## 1. labour_code
- **Minimum wage:** 7.25 USD/h in 2026. G.S. 95-25.3(a) sets the higher of 6.15 USD/h or the FLSA 206(a)(1) rate "as that wage may change", so it follows the federal rate (federal figure: FED unit). There is no state indexation and no enacted 2027 increase (none found in the statute; the live-change sweep was limited, see §13) [US-NCS5-002]. Full-time students, learners, apprentices and messengers get 90% of the rate, rounded to the lowest nickel: 7.25 × 0.9 = 6.525, so **6.50 USD/h**. The arithmetic was run in Python [US-NCS5-002].
- **Local minimum wages:** none. G.S. 95-25.1(d) preempts any local ordinance on wage levels, hours, payment of earned wages, benefits or leave for private employers. The only exceptions are a locality's own employees, economic-development incentives, CDBG and 160D-1311 programs [US-NCS5-001].
- **Overtime:** 1.5× the regular rate above 40 hours per workweek. No daily overtime [US-NCS5-003]. Under the 95-25.14(a)(1) carve-out, employees of FLSA-covered enterprises are governed by the FLSA rather than by the state minimum-wage and overtime rules. The exemption lists are in [US-NCS5-009].
- **Pay frequency:** daily, weekly, biweekly, semimonthly or monthly, with wages paid on the regular payday. Bonuses and commissions may be paid as rarely as annually if the schedule is set in advance [US-NCS5-005].
- **Method of payment (direct deposit / paycard):** 95-25.6 says nothing on this. The NC rule was not located in this pass (open question Q1).
- **Youth:** a youth employment certificate is needed under 18. School-night limit: 11 p.m.–5 a.m. [US-NCS5-004].
- Confidence: 90% (the payment-method rule is missing).

## 2. income_tax
- **Method:** NC-30 (web 11-25), "2026 Income Tax Withholding Tables and Instructions for Employers" [US-NC-001]. The flat tax rate is **3.99%** for tax years after 2025 (G.S. 105-153.7(a)) [US-NCS5-011]. The withholding rate is **4.09%** (3.99% + 0.1%). The final amount is rounded to the nearest whole dollar. Three methods are allowed: wage-bracket tables, the percentage method and the annualized method. Any other method may be used if it is "substantially the same" as the tables [US-NC-001].
- **Standard deduction** (G.S. 105-153.5(a)(1)): single / MFS 12,750; head of household 19,125; MFJ / surviving spouse 25,500 [US-NCS5-010]. The married withholding tables use the single deduction (NC-30 groups "Single Person, Married Person, or Surviving Spouse") [US-NC-001].
- **Allowance:** 2,500 USD per year. An employee may claim one extra allowance per 2,500 of itemized deductions above the standard deduction, or per 2,500 of adjustments, and one per 103 USD of tax credit [US-NC-001].
- **G-DERIVE: every per-period figure in NC-30 was reproduced from the statutory amounts** (Python, 2026-11-02):

  | Period | 12,750/n | 19,125/n (HoH) | 2,500/n | NRA extra = 12,750×4.09%/n |
  |---|---|---|---|---|
  | weekly 52 | 245.19 | 367.79 | 48.08 | 10.03 → **11** |
  | biweekly 26 | 490.38 | 735.58 | 96.15 | 20.06 → **21** |
  | semimonthly 24 | 531.25 | 796.88 | 104.17 | 21.73 → **22** |
  | monthly 12 | 1,062.50 | 1,593.75 | 208.33 | 43.46 → **44** |

  All match NC-30. Note that the NRA additional amounts are **rounded up**, not to the nearest dollar. NC-30's own NRA example also gives 500 × 4.09% = 20.45 → **$21**. So the build must treat the NRA add-on and its "4.09% limitation" as a ceiling, while the general rule is nearest dollar. Oracle checks: the percentage-method example 450 weekly, single, 2 allowances: (450 − 245.19 − 96.16) × 0.0409 = 4.44 → **$4**. The annualized example (23,400 − 17,750) × 0.0409 / 52 = 4.44 → **$4**. Both reproduced [US-NC-001].
- **Certificate:** NC-4, NC-4 EZ, or NC-4 NRA for nonresident aliens (always single, plus the per-period add-on above). With no certificate, withhold as single with zero allowances. Federal W-4s are not acceptable. Copies of certificates claiming more than 10 allowances, or claiming exemption when weekly wages normally exceed 245 USD, must be sent to NCDOR with the quarterly return (or the monthly return for the third month of the quarter). An exempt certificate expires: from **February 16** the employer withholds unless a new NC-4 EZ was filed [US-NC-001].
- **Supplemental:** a flat 4.09%, or the aggregate method. The aggregate method is mandatory if nothing was withheld from regular wages. Vacation pay paid in addition to regular wages counts as supplemental. Tips follow the same rule [US-NC-001].
- **Residence and work location:** residents are withheld on all wages wherever earned. The exception is wages for services in another state that requires the employer to withhold. Nonresidents are withheld on wages for services in NC. Location means the physical place where the services are performed. There is **no reciprocity**: relief for a nonresident comes from the employee's home state [US-NC-001, US-NCP51-002].
- **Local income tax:** prohibited (G.S. 105-247) [US-NCP51-001].
- **Withholding definitions:** wages follow IRC 3401. Clergy who elect employee treatment, corporate officers and elected officials are employees [US-NCS5-012].
- Confidence: 97%.

## 3. social_security (state layer: SUI, SDI/PFML, levies)
- **SUI:** employer-paid only. "An employer may not deduct the contributions … from the remuneration" (G.S. 96-9.2(a)) [US-NCS5-014]. The **2026 taxable wage base is 34,200** (2025: 32,600) [US-NCB5-401, US-NCP9V-001]. The **new-employer rate is 1.000%** [US-NCS5-014, US-NCP9V-001]. Experience rate = base rate − ERRP (reserve ratio × 0.68). The 2026 base rate is 1.9%, applied because the trust fund exceeds 1.25% of insured wages. Range: **0.06%–5.76%** [US-NCS5-014, US-NCP9V-001]. A 20% surtax applies only when the trust fund is below 1 billion USD (G.S. 96-9.7(b)). It is not FUTA-certified [US-NCP9V-001].
- **Wage-base indexation:** the base is the greater of the FUTA base or 50% of the average yearly insured wage, rounded to the nearest 100 USD. Wages paid in another state and predecessor wages count toward it [US-NCS5-015]. G-DERIVE could not be closed: DES's published average weekly insured wage was not obtained (Q4).
- **SDI/TDI/PFML:** none located in NC. Agency level: the only NCDOR wage-based tax is withholding [US-NCP9V-002]; the programme-level absence rests only on tier-B MANUAL US-NCP51-005, so it is not a fact.
- **Employer levies:** P7/P9 result reused: none besides SUI [US-NCP9V-001, US-NCP9V-002].
- Confidence: 92%.

## 4. payslip_statute
- **Content:** G.S. 95-25.13 requires a wage notice at hire, posted or written wage policies, advance written notice of wage changes, and an itemized statement of deductions for each pay period in which deductions are made [US-NCW1B-003, US-NCL-001]. NC has no general pay-stub content list beyond the deductions statement.
- **Delivery:** the itemized statement may be given in writing, by printable e-mail, or by any means the employee can keep in written form. No separate consent rule applies [US-NCS5-024]. Check stubs can satisfy the 95-25.13(2) notice duty [US-NCS5-023].
- **Retention:** 3 years for Wage and Hour Act records (13 NCAC 12 .0802) [US-NCS5-022]. Withholding records: **10 years** after the last filing or payment for the year (NC-30 §26) [US-NC-001].
- **Language:** English (US-OWN-006) [US-NCP9L-001].
- Confidence: 90%.

## 5. reporting_instruments
- **Registration:** Form NC-BR with NCDOR (withholding ID) [US-NC-001]. UI registration with DES/NCSUITS (no row captured; Q5).
- **Withholding return and deposit:** the filing frequency is set by NCDOR from average monthly withholding and changes only with written authorization [US-NC-001].
  - Under 250 USD a month: **quarterly** NC-5, due the last day of the month after the quarter.
  - 250 to under 2,000 USD a month: **monthly** NC-5, due the 15th of the following month. The December return is due January 31.
  - 2,000 USD or more: **semiweekly**, on the federal deposit dates, with voucher NC-5P. The federal next-day rule for 100,000 USD does not apply.
  - Semiweekly filers also file **NC-5Q** by the last day of the month after each quarter (10 more days if all deposits were made).
  - NC has no depository system. Amendments use NC-5X, NC-5PX and NC-3X. Penalties: 5% a month up to 25% for late filing, and 5% for failure to pay [US-NC-001].
- **Annual reconciliation and state W-2:** NC-3 plus the state copies of W-2/1099 are **due January 31**, and electronic filing is mandatory through **eNC3**. A business that closes files by the end of the month after the quarter of closure. Late NC-3: 50 USD a day, capped at 1,000 USD. Wrong format: 200 USD [US-NC-001]. File formats: NC-3 and W-2 are fixed-field .txt; 1099/W-2G/1042-S are .xml. **The TY2026 specs are version 9-2026** ("use beginning January 2027") [US-NCS5-028]. The NC-3 layout PDF on disk is the **10-2020** edition (512-byte records, monthly amounts). It is a structural lead only, not the TY2026 edition [US-NCS5-027, partial]. EFW2 conformity of the NC W-2 file was not confirmed because the spec was not downloaded (Q2).
- **Quarterly UI wage report:** NCUI 101 through NCSUITS. Due **Apr 30 / Jul 31 / Oct 31 / Jan 31**. Wages are reported by employee name and SSN. Electronic filing is mandatory for **10 or more employee wage items**, with a 25 USD penalty otherwise. A zero report is required while the business is active. Late filing: 5% a month up to 25%. Late payment: 10% [US-NCS5-025].
- **New hire:** within **20 days** of hire, or twice a month 12–16 days apart if filed electronically. Fields: employee name, address, SSN, first date of services; employer name, address and FEIN (G.S. 110-129.2) [US-NCS5-020].
- **Third-party and POA:** NCDOR GEN-58 (withholding) and the DES Power of Attorney (UI) [US-NCP51-003, US-FIL-013].
- Confidence: 88% (TY2026 file specs not downloaded).

## 6. leave
- **Paid sick leave:** there is no state statute, and local mandates on private employers are preempted [US-NCS5-001]. No sick-leave statute was found among the Wage and Hour Act sections read.
- **Vacation:** optional. If offered, the employer follows its policy. Forfeiture requires prior written notice of the policy [US-NCS5-008, US-NCS5-023].
- **PFML:** none located [US-NCP9V-002, agency level; programme-level absence rests only on tier-B MANUAL US-NCP51-005, not a fact].
- **Other paid-leave mandates with payroll impact:** none located (jury duty, voting and similar leave were not searched; Q6).
- Confidence: 80%.

## 7. termination
- **Final pay:** on or before the **next regular payday**, the same for discharge and resignation. Bonuses and commissions are due on the first payday after they become calculable. On written request, payment goes by trackable mail [US-NCS5-006].
- **Accrued vacation payout:** follows the employer's policy. It may be forfeited only if the forfeiture policy was notified in advance [US-NCS5-008].
- **Final-pay deductions:** shortage and damage deductions need no 7-day notice at separation [US-NCS5-007].
- **Final W-2:** the wage and tax statement must be given within 30 days of the final wage payment when an employee leaves (NC-30 §22) [US-NC-001].
- **UI separation notice:** DES sends a request to the employer after a claim is filed, and the employer answers by the deadline on the notice [US-NCS5-026]. A proactive employer notice duty was not confirmed (Q3).
- **WARN:** no state law located (not searched specifically).
- Confidence: 85%.

## 8. benefits_in_kind
- NC conforms to the **IRC as enacted on July 5, 2025** (G.S. 105-228.90, updated by S.L. 2026-31) [US-NCS5-013, US-NCS5-029]. Wages for withholding follow IRC 3401 [US-NCS5-012]. State W-2 wages are reported "to the same extent reported for federal tax purposes" [US-NC-001]. So the 401(k), section 125, HSA, transit and group-term-life exclusions follow federal treatment for withholding. The decoupling items in S.L. 2026-31 (R&E, timber, gambling) apply on the return, not to payroll [US-NCS5-029].
- Confidence: 85%. The list of state decouplings in G.S. 105-153.5/.6 was not reviewed item by item for payroll-relevant ones.

## 9. deductions_garnishments
- **Wage deductions:** require a signed written authorization (electronic allowed). Deductions for the employer's benefit cannot take pay below minimum wage or touch overtime. Shortages and damage need 7 days' notice. Overpayments, advances and loan principal count as prepaid wages [US-NCS5-007].
- **Creditor garnishment:** effectively unavailable. Earnings from the 60 days before the order are exempt when needed for family support (G.S. 1-362) [US-NCS5-017].
- **Child support:** a garnishment order is capped at **40% of monthly disposable earnings**, plus a **1 USD processing fee per pay period** kept by the employer (G.S. 110-136) [US-NCS5-018]. IV-D income withholding may be served by OCSE e-IWO [US-NCS5-019, partial]. The federal CCPA caps apply too (FED unit).
- **State tax levy:** at most **10% of wages** (G.S. 105-242(b)) [US-NCS5-021].
- Confidence: 85% (payor remittance timing and the IV-D fee in 110-136.4ff are not extracted).

## 10. collective_agreements (prevailing wage)
- NC has no state prevailing-wage law (DOL WHD state table) [US-NCP51-004]. So there is no state certified-payroll duty; federal Davis-Bacon applies on federal projects (FED unit).
- Confidence: 85%.

## 11. indexation
| Item | Indexed? | Mechanism / publication | register_id |
|---|---|---|---|
| Minimum wage | follows the federal rate, no state index | G.S. 95-25.3(a) | US-NCS5-002 |
| SUI wage base | yes, yearly | 50% of average yearly insured wage, nearest 100 (G.S. 96-9.3); DES tax-rate page | US-NCS5-015, US-NCP9V-001 |
| SUI rates | yearly experience rating | G.S. 96-9.2; DES notices rates in November | US-NCS5-014 |
| PIT rate | statutory trigger, not CPI | G.S. 105-153.7(a1); NC-30 each year | US-NCS5-011 |
| Standard deduction | not indexed (statutory amounts) | G.S. 105-153.5 | US-NCS5-010 |

## 12. data_protection
- **G.S. 75-62:** no public display of SSNs; no SSN on mailed materials unless the law requires it; never visible through the envelope; no unsecured transmission. Redacted SSNs are exempt [US-NCS5-016]. No NC rule requiring SSN truncation on the pay statement was located. A pay stub mailed with a full SSN falls under 75-62(a)(5), so the safe build is a truncated SSN.
- **Payroll-record privacy:** NC's breach statute (G.S. 75-65) was not read (Q7).
- Confidence: 75%.

## 13. live_legal_change (2026-01-01 → 2026-11-02)
- **2027 PIT rate: 3.49% is likely but not confirmed.** Under G.S. 105-153.7(a1) the rate drops to 3.49% for 2027 if FY2025-26 General Fund revenue exceeds **33.042 bn USD**. The test is the Office of State Controller's final accounting published in August 2026 [US-NCS5-011]. The May 2026 consensus forecast "continues to anticipate exceeding the triggers" in FY2025-26 and FY2026-27, giving 3.99% → 3.49% (2027) → 2.99% (2028+) [US-NCS5-030, A.3, partial]. The OSC final accounting and the 2027 NC-30 (normally out in late November/December) were **not located**, so I have recorded it as an open question. Do not model 3.49% until NCDOR publishes it. **Level: withholding and assessment.**
- **S.L. 2026-31 and S.L. 2026-41 (enacted, signed July 2026):** IRC conformity date moves to 2025-07-05, plus return-level deductions. NCDOR notice of 2026-07-23 (updated 2026-07-29 and 2026-10-09). **Level: assessment.** No change to withholding was announced [US-NCS5-029].
- **TY2026 eNC3 specs version 9-2026** were published for filing from January 2027 [US-NCS5-028]. **Level: employer reporting.**
- **SUI 2027 wage base:** not yet published on the DES page read on 2026-11-01 (it shows 2021–2026 only) [US-NCP9V-001].
- The sweep was limited to these NCDOR and DES pages. A full sweep of 2026 NCGA session laws was not run (Q8).

## Special populations (US-OWN-005, state level)
| Population | NC rule | register_id |
|---|---|---|
| Domestic / household | No NC withholding required (voluntary agreement possible). Exempt from state minimum wage, overtime and youth rules (FLSA applies). UI coverage threshold not read | US-NC-001, US-NCS5-009 |
| Agricultural | Exempt from state MW/OT/youth (95-25.14(a)(2)). Withholding follows IRC 3401 wages. UI coverage not read | US-NCS5-009, US-NCS5-012 |
| Minors | Youth employment certificate; school-night hours limit | US-NCS5-004 |
| Tipped | Tip credit up to FLSA 3(m) with notice and tip certification; tip pool max 15%; tips withheld as supplemental | US-NCS5-002, US-NC-001 |
| Clergy / religious | Clergy are employees for NC withholding only if they elect under 105-163.1A | US-NCS5-012 |
| Students | 90% minimum wage (6.50 USD/h); Indian students/business apprentices put $0 on NC-4 NRA line 2 | US-NCS5-002, US-NC-001 |
| Nonresident aliens | NC-4 NRA: single, plus add-on 11/21/22/44 per period (rounded up), capped at 4.09% of wages when annualized wages are 12,750 or less; treaty-exempt wages exempt; Canada/Mexico transport and border workers exempt | US-NC-001 |
| Statutory employees | No state rule beyond federal (wages = IRC 3401) | US-NCS5-012 |
| Government employees | Must withhold (NC-30 §2). Only minimum wage and a few Wage and Hour Act provisions apply to public employers | US-NC-001, US-NCS5-009 |
| Military spouses (SCRA) | Exempt on NC-4 EZ line 4, renewed each year | US-NC-001 |
| Interstate rail, motor carrier, airline | Taxed only by the state of residence (Amtrak Act, 49 USC 14503); airline: NC tax only if more than 50% of scheduled flight time is in NC | US-NC-001 |
| Tribal members on reservation | Exempt on NC-4 EZ line 5 | US-NC-001 |
| Seamen | No withholding (46 USC 11108), except voluntary coastwide trade within NC | US-NC-001 |

## ACCESS gaps (exact URLs)
- `https://des.nc.gov/documents/files/employers-quarterly-tax-and-wage-report-english/open`: HTTP 404 (NCUI 101 form PDF).
- `https://des.nc.gov/documents/downloads/ncdes-524e/download`: HTTP 404.
- `https://des.nc.gov/employers/workplace-posters`: HTTP 404.
- `http://reports.oah.state.nc.us/ncac/title%2013%20-%20labor/chapter%2012%20-%20wage%20and%20hour/subchapter%2008/subchapter%2008%20rules.pdf`: HTTP 404 (single rules .0802/.0805/.0807 fetched instead; .0801/.0806 not fetched).
- These are 404s, not bot blocks, so Wayback was not tried.

## Open questions

Mirrors `unresolved[]` of the facts file (same keys, same wording).

- **nc.payment.method** (non-blocking): NC direct deposit / paycard consent rule not located. What would close it: NCDOL wage-payment FAQ or a 13 NCAC 12 rule on payment method.
- **nc.report.w2.file_format** (non-blocking): Whether the NC W-2 file in eNC3 is EFW2 or an NC layout; the 9-2026 spec was not downloaded (US-NCS5-027 is a 10-2020 partial lead). What would close it: TY2026 "eNC3 W2" spec version 9-2026 from the NCDOR eNC3 file-format page.
- **nc.term.ui_separation_notice** (non-blocking): Whether NC employers must hand separating employees a UI-availability notice is not confirmed. What would close it: 04 NCAC 24A/24B text on the OAH host, or the DES employer handbook.
- **nc.ui.wage_base.derivation** (non-blocking): G-DERIVE of 34,200 needs the DES average weekly insured wage at the 2025 computation date. What would close it: DES Labor Market Information average-wage publication.
- **nc.ui.registration** (non-blocking): NCSUITS registration steps and liability thresholds (incl. domestic/agricultural) not read. What would close it: G.S. 96-1(b) text plus the DES registration page.
- **nc.leave.other** (non-blocking): Jury-duty, voting and other leave with pay impact not searched. What would close it: G.S. 9-32 and related statutes on ncleg.gov.
- **nc.data.breach** (non-blocking): G.S. 75-65 breach notice not read. What would close it: The statute text.
- **nc.pit.rate.next_year** (blocking): 3.49% for 2027 is projected (revenue trigger), not confirmed; US-NCS5-030 is partial. Not written as a fact. What would close it: OSC FY2025-26 final General Fund accounting (August 2026) or the 2027 NC-30 / NCDOR rate notice.
- **nc.garn.iwo.payor_duties** (non-blocking): IV-D remittance timing and payor fee (110-136.5 to .8) not extracted. What would close it: G.S. 110-136.5 to 110-136.8.
