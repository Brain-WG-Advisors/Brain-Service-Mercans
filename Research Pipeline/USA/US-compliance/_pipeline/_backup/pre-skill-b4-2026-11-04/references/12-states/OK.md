# Annex OK: Oklahoma


Jurisdiction annex of the United States Country Configuration Guide (US-CCG-001). Layer classification: **T3 - state withholding; local layer absent or piggybacked on the state return**.

The federal layer (federal income tax withholding, FICA, FUTA, Forms W-2, 941 and 940) and the multistate rules (residence and work-location sourcing, reciprocity mechanics) are in the federal reference and the multistate reference and are not repeated here. Independent contractors and Form 1099-NEC reporting are out of scope (owner instruction of 2026-10-29) [US-OWN-008]. Payslip language: English; second-language duties attach to notices and posters only (US-OWN-006).

Every value in this annex is bound to a verified fact and carries its legal-basis register id. A value that changes during the year is shown with its effective dates. A point marked as a research gap has not been closed by the research; it is not filled with an estimate.

## OK.1 Employment and labour code

- **Minimum wage (40 O.S. 197.2) [US-OKS5-001].** The state rate equals the current federal minimum wage (follows federal: True); the figure is in the federal reference. No state increase is possible in 2027 without a federal change. Coverage and exclusions of the state Act are in Section 14.
- **Local minimum wage and local leave mandates:** preempted (40 O.S. 160): True [US-OKS5-002].
- **Overtime:** none (FLSA only); the FLSA rule applies (the federal reference) [US-OKS5-017, US-OKS5-022].
- **Pay frequency (40 O.S. 165.2) [US-OKS5-003, US-OK-003]:** at least twice each calendar month; payday max 11 days after period end (+3 grace). Exempt staff and public employees may be paid at least monthly.
- **Method of payment (165.2) [US-OKS5-003]:** lawful money incl. electronic; deposit at employee-chosen institution; paycard if employee does not designate. ODOL guidance reads the paycard rule differently (open point below).
- **Dishonoured paycheck:** the employer reimburses the employee's bank fees within 14 days [US-OKS5-003]. Rest breaks apply only to minors under 16 (40 O.S. 75) [US-OKS5-017].

**Parameters (labour code and pay rules)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ok.labour.minwage.state.follows_federal` | True |  | from 1983-11-01 | US-OKS5-001 |  |
| `ok.local_mandates.preempted` | True |  | from 2014-07-01 | US-OKS5-002 | 40 O.S. 160 also preempts local vacation/sick leave |
| `ok.labour.overtime.state_rule` | none (FLSA only) |  | from 1997-07-01 | US-OKS5-017 |  |
| `ok.pay_frequency.rule` | at least twice each calendar month; payday max 11 days after period end (+3 grace) |  | from 2022-11-01 | US-OKS5-003 | exempt/public employees at least monthly |
| `ok.payment.method` | lawful money incl. electronic; deposit at employee-chosen institution; paycard if employee does not designate |  | from 2022-11-01 | US-OKS5-003 |  |
| `ok.labour.dishonoured_check.reimburse_days` | 14 | days | from 2022-11-01 | US-OKS5-003 |  |

**Open research points**

- Not configured in this release (open gap RQ-286): Statute vs ODOL FAQ differ on paycards.

## OK.2 Income tax withholding

- **Statutory rates from tax year 2026 (68 O.S. 2355(D), HB 2764) [US-OKS5-009].** Single bands: zero rate on the first 3750 USD; 2.5 % on the next 1150 USD; 3.5 % on the next 2300 USD; 4.5 % on the remainder. Joint filers use double-width bands (statute; widths not carried as facts).
- **Standard deduction (68 O.S. 2358, not indexed) [US-OKS5-011]:** single 6350 USD; married filing jointly 12,700 USD; head of household 9350 USD. Allowance 1000 USD per year [US-OK-001].
- **Withholding method [US-OK-001]:** OW-2 (Rev. 11-2025) percentage formula or wage-bracket tables, effective 2026-01-01. The annual percentage-method thresholds are the standard deduction plus the statutory band edges: single 10100;11250;13550; married 20200;22500;27100 (USD, at which the zero, first, second and top bands begin). "Married, but withhold at the higher Single rate" uses the Single table. Per-period tables are published in OW-2.
- **Rounding (68 O.S. 2385.2(B)) [US-OKS5-010]:** nearest whole dollar (49c down, 50c up); nothing if quarterly tax < 0.25.
- **Oracle:** OW-2 percentage-method example (semimonthly, married, two allowances): 37.00 USD, reproduced exactly [US-OK-001]. Recomputation in Module 12.
- **Certificate [US-OKS5-014, US-OKS5-021]:** OK-W-4 (Rev. 3-2021); none on file = Single, 0 allowances. A federal W-4 signed before the 2018 changeover still governs for older hires.
- **Supplemental wages [US-OK-005, US-OKS5-014]:** if paid separately or identified, the highest statutory rate (4.5 % for 2026) or the aggregate method; if paid together with regular wages and not separated, treat as one regular payment. The rule still cross-references the pre-2026 subsection; the rates sit in 2355(D).
- **Exclusions from withholding wages (68 O.S. 2385.1(e)) [US-OKS5-010]:** farm work up to 900 USD a month; domestic service in a private home; casual work outside the trade or business; nonresidents with no more than 300 USD of Oklahoma income in a quarter; ministers and members of religious orders.
- **Nonresident aliens:** 8 % under 68 O.S. 2355(G) and OAC 710:90-1-8 [US-OKS5-009]; whether it replaces table withholding on wages is open (below).
- **Local wage tax:** none (exists: False) [US-OKP9V-001]. **Reciprocity:** none [US-OKP51-002]. Residents get a credit for tax paid to another state on Form 511-TX [US-OKP52-002].
- **Resident and nonresident matrix.**

| Income type | Resident | Nonresident (US) |
|---|---|---|
| Regular salary | Withheld on services inside or outside Oklahoma (2385.1(c)), OW-2 | Withheld only on services performed in Oklahoma, above the quarterly de minimis |
| Bonus / supplemental | Top statutory rate or aggregate | Same, Oklahoma-source share |
| Nonresident alien | - | Flat NRA rate per 2355(G) (interaction with tables open) |
| Severance, equity, benefits in kind | Follow the IRC wage definition (2385.1) | Oklahoma-source share |

- **Rate-cut trigger:** the earliest possible statutory cut takes effect 2028-01-01 (62 O.S. 34.103(D)); none in 2027 [US-OKS5-025].

**Parameters (income tax withholding (state and local))**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ok.pit.statutory.bracket.single.1.width` | 3750 | USD | from 2026-01-01 | US-OKS5-009 | 0%; MFJ/HoH 7,500 |
| `ok.pit.statutory.bracket.single.2.width` | 1150 | USD | from 2026-01-01 | US-OKS5-009 | 2.5%; MFJ 2,300 |
| `ok.pit.statutory.bracket.single.3.width` | 2300 | USD | from 2026-01-01 | US-OKS5-009 | 3.5%; MFJ 4,600 |
| `ok.pit.statutory.rate.2` | 2.5 | % | from 2026-01-01 | US-OKS5-009 |  |
| `ok.pit.statutory.rate.3` | 3.5 | % | from 2026-01-01 | US-OKS5-009 |  |
| `ok.pit.statutory.rate.top` | 4.5 | % | from 2026-01-01 | US-OKS5-009 | earliest cut 2028-01-01 (US-OKS5-025); none in 2027 |
| `ok.pit.std_deduction.single` | 6350 | USD | from 2017-01-01 | US-OKS5-011 | not indexed |
| `ok.pit.std_deduction.mfj` | 12,700 | USD | from 2017-01-01 | US-OKS5-011 |  |
| `ok.pit.std_deduction.hoh` | 9350 | USD | from 2017-01-01 | US-OKS5-011 |  |
| `ok.pit.allowance.annual` | 1000 | USD | from 2026-01-01 | US-OK-001 | OW-2 Rev. 11-2025; weekly 19.23, biweekly 38.46, semimonthly 41.67, monthly 83.33 |
| `ok.wh.method` | OW-2 (Rev. 11-2025) percentage formula or wage-bracket tables |  | from 2026-01-01 | US-OK-001 |  |
| `ok.pit.wh.single.annual.thresholds` | 10100;11250;13550 |  | from 2026-01-01 | US-OK-001 |  |
| `ok.pit.wh.married.annual.thresholds` | 20200;22500;27100 |  | from 2026-01-01 | US-OK-001 | 57.50 at 22,500; 218.50+4.5% above 27,100 |
| `ok.pit.rounding` | nearest whole dollar (49c down, 50c up); nothing if quarterly tax < 0.25 |  | from 2026-01-01 | US-OKS5-010 | 68 O.S. 2385.2(B) |
| `ok.pit.oracle.example_1.withholding` | 37.00 | USD | from 2026-01-01 | US-OK-001 | OW-2 p.7 semimonthly married 2 allowances 1,825.00: 1,825-83.34=1,741.66; 9.10+(1,741.66-1,129)x4.5% = 36.67 -> 37.00 |
| `ok.wh.certificate` | OK-W-4 (Rev. 3-2021); none on file = Single, 0 allowances |  | from 2019-08-11 | US-OKS5-014 | federal W-4 signed before 2018-03-01 still governs |
| `ok.wh.supplemental.rate` | 4.5 | % | from 2026-01-01 | US-OK-001 | highest 2355 rate; or aggregate; aggregate only if nothing withheld from regular |
| `ok.pit.nonresident.quarterly_threshold` | 300 | USD | from 2023-07-01 | US-OKS5-010 | nonresidents with <=300 OK income in a quarter excluded |
| `ok.pit.agricultural.monthly_threshold` | 900 | USD | from 2023-07-01 | US-OKS5-010 | farm work <=900/month excluded |
| `ok.pit.nra.rate` | 8 | % | from 2026-01-01 | US-OKS5-009 | 68 O.S. 2355(G) |
| `ok.local_wage_tax.exists` | False |  | from 2026-01-01 | US-OKP9V-001 |  |
| `ok.reciprocity.states` | none |  | from 2026-01-01 | US-OKP51-002 | no convenience rule found |

**Open research points**

- Not configured in this release (open gap RQ-284): Whether the flat NRA rate of 2355(G) replaces table withholding on nonresident-alien wages is open.

## OK.2b Non-resident regime and reciprocity

The non-resident and reciprocity rules of this jurisdiction are written in OK.2.

## OK.2c Local wage taxes

The local wage taxes of this jurisdiction, where any exist, are written in OK.2.

## OK.3 Social insurance: unemployment, disability, paid leave and payroll levies

- **Unemployment insurance (OESC) [US-OK-002, US-OKS5-018].** Employer-only; the law forbids deducting contributions from wages (employee rate 0 %) [US-OKS5-005].

| Year | Taxable wage base | Experienced rate range | New employer | Register id |
|---|---|---|---|---|
| 2026 | 25,000 USD | 0.2 % to 5.8 % | 1.5 % | US-OK-002 |
| 2027 | 24,400 USD | 0.1 % to 5.5 % | same rate, 2026-2027 | US-OKS5-018 |

- **Wage-base mechanism (40 O.S. 1-201(48), 1-223) [US-OKS5-005]:** a percentage of the state average annual wage of the second preceding year, rounded to the nearest hundred dollars; the 2027 caliber is 60,993.99 USD [US-OKS5-018]. The 2026 and 2025 bases reproduce only with the percentages in force before 2025-11-01 (open point below).
- **Wages reported to another state count toward the base:** True [US-OKS5-005].
- **UI wages (40 O.S. 1-218) [US-OKS5-006]:** elective retirement deferrals included; cafeteria-plan payments included: False. UI therefore departs from income tax for deferrals.
- **No SDI, TDI, PFML, LTC, transit or workforce levy** [US-OKP9V-001, US-OKP9V-002, US-OKS5-026].

**Parameters (social insurance and payroll levies)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ok.sui.wage_base` | 25,000 | USD | 2026-01-01 to 2026-12-31 | US-OK-002 | 42.5% x 58,765.95 = 24,975.53 -> 25,000 (pre-c.140 percentage, inference) |
| `ok.sui.wage_base` | 24,400 | USD | 2027-01-01 to 2027-12-31 | US-OKS5-018 |  |
| `ok.sui.employer.rate.min` | 0.2 | % | 2026-01-01 to 2026-12-31 | US-OK-002 | range 0.2-5.8 |
| `ok.sui.employer.rate.max` | 5.8 | % | 2026-01-01 to 2026-12-31 | US-OK-002 |  |
| `ok.sui.employer.rate.min` | 0.1 | % | 2027-01-01 to 2027-12-31 | US-OKS5-018 | published 2027 range 0.1-5.5 |
| `ok.sui.employer.rate.max` | 5.5 | % | 2027-01-01 to 2027-12-31 | US-OKS5-018 |  |
| `ok.sui.new_employer.rate` | 1.5 | % | 2026-01-01 to 2027-12-31 | US-OKS5-018 | 2026 and 2027 |
| `ok.ui.average_annual_wage.caliber` | 60,993.99 | USD | 2027-01-01 to 2027-12-31 | US-OKS5-018 | second-preceding-year AAW drives the 2027 base |
| `ok.sui.employee.rate` | 0 | % | from 2025-11-01 | US-OKS5-005 | deduction forbidden (3-102(A)) |
| `ok.sui.wages.401k_included` | True |  | from 2019-07-01 | US-OKS5-006 |  |
| `ok.sui.wages.section125_included` | False |  | from 2019-07-01 | US-OKS5-006 |  |
| `ok.sui.wage_base.other_state_credit` | True |  | from 2025-11-01 | US-OKS5-005 | 40 O.S. 1-201(48) |

**Open research points**

- Not configured in this release (open gap RQ-285): The 2025 and 2026 wage bases reproduce only with the percentages in force before Laws 2025 c. 140 (an inference from arithmetic; the old text was not read).

## OK.4 Pay statement

- **Content (40 O.S. 165.2) [US-OKS5-003, US-OK-003]:** brief itemized statement of all deductions with each payment. No other content is mandated by state law; gross, hours and rates follow from FLSA records (the federal reference). Paper or electronic delivery per ODOL guidance [US-OKS5-022]. The rule follows work in Oklahoma (165.1(1)).
- **Retention:** payroll-tax records 4 years after the due or payment date, whichever is later (OAC 710:90-1-11) [US-OKS5-014].

**Parameters (payslip statute and payroll records)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ok.payslip.items` | brief itemized statement of all deductions with each payment |  | from 2022-11-01 | US-OKS5-003 | 165.2; paper or electronic (ODOL FAQ) |
| `ok.records.payroll_tax.retention_years` | 4 | years | from 2019-08-11 | US-OKS5-014 | OAC 710:90-1-11 |

## OK.5 Statutory reporting

- **Withholding return (68 O.S. 2385.3; OAC 710:90-3-4) [US-OKS5-010, US-OKS5-014, US-OK-001]:** quarterly, due 20th of month after quarter; zero return required. Remittance monthly once quarterly withholding reaches 500 USD; federal semiweekly depositors follow the federal dates. Channel: OkTAP.
- **W-2 and annual reconciliation:** 31 January via OkTAP (EFW2 or manual) [US-OKS5-010]; to a departing employee within the statutory period after the last wage payment.
- **UI quarterly wage report (OES-3) [US-OKS5-020]:** filed in EZ Tax Express by manual entry or upload; upload format ICESA 275-character fixed records (E, S, T); required on every active account. Statutory due date: open point below.
- **New hire (40 O.S. 2-802) [US-OKS5-007, US-OKS5-029]:** every hire who resides or works in Oklahoma, within 20 days of start, to OESC.
- **Registration:** OTC withholding account at tax.ok.gov; OESC account via EZ Tax Express; powers of attorney BT-129 (OTC) and OES-190T (OESC) [US-OKP51-004, US-OKP51-005].

**Parameters (statutory reporting)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ok.report.wh.return_due` | 20th of month after quarter |  | from 2023-07-01 | US-OKS5-010 | zero return required |
| `ok.report.wh.monthly_threshold.quarterly` | 500 | USD | from 2023-07-01 | US-OKS5-010 | >=500/quarter monthly by 20th; semiweekly if federal semiweekly; electronic at >=5,000/month |
| `ok.report.w2.due` | 31 January via OkTAP (EFW2 or manual) |  | from 2023-07-01 | US-OKS5-010 | paper/magnetic not accepted; employee W-2 within 30 days of last payment if terminated |
| `ok.report.ui.format` | ICESA 275-character fixed records (E, S, T) |  | from 2024-10-01 | US-OKS5-020 | EZ Tax Express; due date not confirmed from A source |
| `ok.newhire.report_days` | 20 | days | from 2015-11-01 | US-OKS5-007 | to OESC |

**Open research points**

- Not configured in this release (open gap RQ-283): Not established from an official source.

## OK.6 Leave

- **Paid sick leave:** no state statute (exists: False); local mandates preempted (40 O.S. 160) [US-OKS5-002]. No PFML or SDI [US-OKS5-026].
- **Voting leave (26 O.S. 7-101):** 2 hours paid on proof of voting, with advance notice; not due where the shift leaves enough time before or after the polls [US-OKS5-023].
- **Jury duty:** no duty to pay non-exempt employees; the employer may not require use of paid leave; exempt employees keep their salary with an offset for jury fees [US-OKS5-024, US-OKS5-022]. Military leave: open point below.

**Parameters (leave)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ok.leave.sick.state_statute.exists` | False |  | from 2014-07-01 | US-OKS5-002 | local preempted |
| `ok.leave.voting.paid_hours` | 2 | hours | from 2019-05-06 | US-OKS5-023 | on proof of voting, 3 days notice |

**Open research points**

- Not configured in this release (open gap RQ-288): State military-leave rights (Title 44) not established from an official source.

## OK.7 Termination and final pay

- **Final pay (40 O.S. 165.3) [US-OKS5-004]:** next regular designated payday (discharge and resignation), or by certified mail on request; amounts in bona fide dispute excluded; liquidated damages for wilful failure.
- **Accrued vacation:** per agreement or established policy (165.1(7)) [US-OKS5-003]; no statute forces payout.
- **Separation notice:** no general UI separation-notice duty in Title 40. W-2 to a departing employee within the statutory period [US-OKS5-010]; IWO termination notice to the support agency [US-OKS5-015].

**Parameters (termination)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ok.final_pay.rule` | next regular designated payday (discharge and resignation) |  | from 2005-11-01 | US-OKS5-004 | liquidated damages 2%/day capped at unpaid amount |
| `ok.term.vacation.payout` | per agreement or established policy |  | from 2022-11-01 | US-OKS5-003 | 165.1(7) |

## OK.8 Benefits in kind and taxable wages

- **Income tax:** withholding wages carry the IRC meaning apart from the 2385.1(e) exclusions, so the federal exclusions carry over [US-OKS5-010]; Oklahoma adjustments (68 O.S. 2358) not reviewed item by item (open point below).
- **UI departs:** elective deferrals are UI wages; cafeteria-plan, educational-assistance and dependent-care payments are excluded [US-OKS5-006].

**Open research points**

- Not configured in this release (open gap RQ-287): 68 O.S. 2358 adjustments not reviewed item by item.

## OK.9 Deductions and garnishments

- **Wage deductions:** beyond statutory deductions and court orders, a written agreement signed by both parties is required (ODOL guidance) [US-OKS5-022]; the underlying rule is open (below).
- **Creditor garnishment (31 O.S. 1(A)(18)) [US-OKS5-013]:** maximum 25 % of disposable earnings, subject to the federal CCPA floor (the federal reference).
- **Continuing earnings garnishment (12 O.S. 1173.4) [US-OKS5-012]:** lien of 180 days; the earlier lien has priority.
- **Child support (12 O.S. 1171.2, 1171.3) [US-OKS5-012, US-OKS5-015]:** CCPA support percentages; priority current support, health premiums, arrears, then other; remit to the Centralized Support Registry within 7 days of payday; employer fee 5 USD per pay period, with a monthly cap.

**Parameters (deductions and garnishments)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ok.garn.creditor.max_percent` | 25 | % | from 2026-01-01 | US-OKS5-013 | 75% of last 90 days earnings exempt; CCPA floor |
| `ok.garn.continuing.lien_days` | 180 | days | from 2023-11-01 | US-OKS5-012 | 12 O.S. 1173.4 |
| `ok.garn.iwo.employer_fee.per_period` | 5 | USD | from 2026-01-01 | US-OKS5-015 | max 10/month; remit within 7 days |
| `ok.garn.iwo.remit_days` | 7 | days | from 2026-01-01 | US-OKS5-015 |  |

**Open research points**

- Not configured in this release (open gap RQ-289): ODOL deduction rule (OAC 380:30-1-3) behind the FAQ not read.

## OK.10 Collective agreements and prevailing wage

Prevailing wage (public works) is an optional informational flag [US-OWN-009]: this guide documents prevailing-wage laws, thresholds and certified-payroll duties as an overlay, and the payroll build does not produce certified payroll reports.

- **No state prevailing wage** (exists: False): the Minimum Wages on Public Works Act was held unconstitutional and repealed by Laws 2015 c. 71, effective 2015-11-01 [US-OKS5-016]. Federal Davis-Bacon applies on federally funded work.

**Parameters (collective agreements and prevailing wage)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ok.prevailing_wage.exists` | False |  | from 2015-11-01 | US-OKS5-016 | repealed Laws 2015 c.71 |

## OK.11 Indexation

- **Minimum wage:** follows the federal rate only [US-OKS5-001].
- **SUI wage base and rate range:** yearly, published by OESC (Section 3) [US-OKS5-005, US-OKS5-018].
- **PIT brackets, standard deduction, allowance:** not indexed; rates fall only through the revenue trigger (earliest 2028-01-01) [US-OKS5-009, US-OKS5-011, US-OKS5-025].
- **Withholding tables:** republished when the law changes (OW-2) [US-OK-001].

## OK.12 Payroll data protection and records

- **40 O.S. 173.1 (private employers) [US-OKS5-008]:** no public display of SSNs; no SSN on access cards; no unsecured transmission; no SSN as sole login; no SSN on materials mailed to the employee unless law requires it. A mailed paper payslip falls under this rule: mask the SSN.
- **Annual withholding statement:** may show only the last digits of the SSN (OAC 710:90-1-10) [US-OKS5-014].

**Parameters (payroll data protection)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ok.data.w2.ssn_last4_allowed` | True |  | from 2019-08-11 | US-OKS5-014 | OAC 710:90-1-10 |
| `ok.data.ssn.mailed_materials_prohibited` | True |  | from 2004-11-01 | US-OKS5-008 | 40 O.S. 173.1 unless required by law |

## OK.13 Live legal change

- **2026-01-01:** new statutory rates in force; OW-2 (Rev. 11-2025) implements them [US-OKS5-009, US-OK-001].
- **2025-11-01:** UI percentage amendments (Laws 2025 c. 140) and tip-credit link to the federal cash wage (Laws 2025 c. 401) [US-OKS5-005, US-OKS5-001].
- **2027-01-01:** published SUI numbers (Section 3) [US-OKS5-018]. Paid-leave and tips/overtime bills (SB 277, SB 470, SB 1986) not enacted [US-OKS5-026]; OTC announced no withholding change [US-OKS5-028]. The 2026 session laws were not swept as a whole (open point below).

**Open research points**

- Not configured in this release (open gap RQ-290): 2026 session laws effective 2026-11-01 not reviewed; OW-2 2027 expected Nov 2026.

## OK.14 Authority worked examples (oracle values)

No authority worked example is reproduced in this annex; recomputed withholding examples are in Module 12.

## OK.15 Special populations

| Population | Oklahoma rule | Register id |
|---|---|---|
| Domestic / household | Exempt from withholding (2385.1(e)(2)); UI covered above a quarterly cash test; excluded from the state minimum-wage Act (FLSA may apply) | US-OKS5-010, US-OKS5-006, US-OKS5-001 |
| Agricultural | Withholding exempt up to 900 USD a month; UI coverage tests; H-2A excluded; excluded from the state minimum-wage Act | US-OKS5-010, US-OKS5-006, US-OKS5-027, US-OKS5-001 |
| Minors | Under 16: hours and rest-break limits; state Act excludes minor non-graduates; minor newspaper carriers excluded from UI | US-OKS5-017, US-OKS5-001, US-OKS5-027 |
| Tipped | Tip credit if the cash wage is at least the federal 29 CFR 531.50 amount; UI wages include tips | US-OKS5-001, US-OKS5-006 |
| Clergy / religious | Exempt from withholding and excluded from UI | US-OKS5-010, US-OKS5-027 |
| Students | UI excludes own-school employment, work-study and student nurses; state Act excludes students below the statutory age | US-OKS5-027, US-OKS5-001 |
| Nonresident aliens | NRA rate 8 % (interaction with tables open) | US-OKS5-009, US-OKS5-014 |
| Nonresidents (US) | Withheld on Oklahoma services above the quarterly de minimis; no reciprocity; no convenience rule found | US-OKS5-010, US-OKP51-002, US-OKP52-001 |
| Military / spouses | OK-W-4 exemption lines for MSRRA (with OW-9-MSE) and active-duty pay | US-OKS5-021 |
| Statutory employees / officers | Corporate officers are employees for withholding (2385.1(c)) | US-OKS5-010 |
| Government employees | Paid at least monthly; elected officials excluded from UI; the SSN rule does not bind the state | US-OKS5-003, US-OKS5-001, US-OKS5-027, US-OKS5-008 |
| Family employment | UI excludes service for a child or spouse, and a minor child working for a parent | US-OKS5-027 |
| Commission insurance / real-estate agents | Excluded from UI | US-OKS5-027 |

## OK.16 Language

No language rule for employee documents is written for this jurisdiction in this annex.

## OK.S Sources

Authorities:

- Decided under the owner's delegation: US-OWN-006
- Oklahoma Department of Labor: US-OKS5-022
- Oklahoma Employment Security Commission: US-OK-002, US-OKP51-005, US-OKP9V-002, US-OKS5-018, US-OKS5-020, US-OKS5-029
- Oklahoma Legislature: US-OKS5-026
- Oklahoma Legislature (Oklahoma Statutes, Title 12): US-OKS5-012, US-OKS5-015
- Oklahoma Legislature (Oklahoma Statutes, Title 26): US-OKS5-023
- Oklahoma Legislature (Oklahoma Statutes, Title 31): US-OKS5-013
- Oklahoma Legislature (Oklahoma Statutes, Title 38): US-OKS5-024
- Oklahoma Legislature (Oklahoma Statutes, Title 40): US-OKS5-001, US-OKS5-002, US-OKS5-003, US-OKS5-004, US-OKS5-005, US-OKS5-006, US-OKS5-007, US-OKS5-008, US-OKS5-016, US-OKS5-017, US-OKS5-027
- Oklahoma Legislature (Oklahoma Statutes, Title 62): US-OKS5-025
- Oklahoma Legislature (Oklahoma Statutes, Title 68): US-OKS5-009, US-OKS5-010, US-OKS5-011
- Oklahoma Legislature / OSCN: US-OK-003
- Oklahoma Tax Commission: US-OK-001, US-OKP51-002, US-OKP51-004, US-OKP52-001, US-OKP52-002, US-OKP9V-001, US-OKS5-021, US-OKS5-028
- Oklahoma Tax Commission (OAC 710:90): US-OK-005, US-OKS5-014
- Owner (Wallisson Gomes): US-OWN-008


## Fact index

Every value above with its key, effective period and register id.

| Key | Value | Effective | Register id |
|---|---|---|---|
| `ok.data.ssn.mailed_materials_prohibited` | True | from 2004-11-01 | US-OKS5-008 |
| `ok.data.w2.ssn_last4_allowed` | True | from 2019-08-11 | US-OKS5-014 |
| `ok.final_pay.rule` | next regular designated payday (discharge and resignation) | from 2005-11-01 | US-OKS5-004 |
| `ok.garn.continuing.lien_days` | 180 | from 2023-11-01 | US-OKS5-012 |
| `ok.garn.creditor.max_percent` | 25 | from 2026-01-01 | US-OKS5-013 |
| `ok.garn.iwo.employer_fee.per_period` | 5 | from 2026-01-01 | US-OKS5-015 |
| `ok.garn.iwo.remit_days` | 7 | from 2026-01-01 | US-OKS5-015 |
| `ok.labour.dishonoured_check.reimburse_days` | 14 | from 2022-11-01 | US-OKS5-003 |
| `ok.labour.minwage.state.follows_federal` | True | from 1983-11-01 | US-OKS5-001 |
| `ok.labour.overtime.state_rule` | none (FLSA only) | from 1997-07-01 | US-OKS5-017 |
| `ok.leave.sick.state_statute.exists` | False | from 2014-07-01 | US-OKS5-002 |
| `ok.leave.voting.paid_hours` | 2 | from 2019-05-06 | US-OKS5-023 |
| `ok.local_mandates.preempted` | True | from 2014-07-01 | US-OKS5-002 |
| `ok.local_wage_tax.exists` | False | from 2026-01-01 | US-OKP9V-001 |
| `ok.newhire.report_days` | 20 | from 2015-11-01 | US-OKS5-007 |
| `ok.pay_frequency.rule` | at least twice each calendar month; payday max 11 days after period end (+3 grace) | from 2022-11-01 | US-OKS5-003 |
| `ok.payment.method` | lawful money incl. electronic; deposit at employee-chosen institution; paycard if employee does not designate | from 2022-11-01 | US-OKS5-003 |
| `ok.payslip.items` | brief itemized statement of all deductions with each payment | from 2022-11-01 | US-OKS5-003 |
| `ok.pit.agricultural.monthly_threshold` | 900 | from 2023-07-01 | US-OKS5-010 |
| `ok.pit.allowance.annual` | 1000 | from 2026-01-01 | US-OK-001 |
| `ok.pit.nonresident.quarterly_threshold` | 300 | from 2023-07-01 | US-OKS5-010 |
| `ok.pit.nra.rate` | 8 | from 2026-01-01 | US-OKS5-009 |
| `ok.pit.oracle.example_1.withholding` | 37.00 | from 2026-01-01 | US-OK-001 |
| `ok.pit.rounding` | nearest whole dollar (49c down, 50c up); nothing if quarterly tax < 0.25 | from 2026-01-01 | US-OKS5-010 |
| `ok.pit.statutory.bracket.single.1.width` | 3750 | from 2026-01-01 | US-OKS5-009 |
| `ok.pit.statutory.bracket.single.2.width` | 1150 | from 2026-01-01 | US-OKS5-009 |
| `ok.pit.statutory.bracket.single.3.width` | 2300 | from 2026-01-01 | US-OKS5-009 |
| `ok.pit.statutory.rate.2` | 2.5 | from 2026-01-01 | US-OKS5-009 |
| `ok.pit.statutory.rate.3` | 3.5 | from 2026-01-01 | US-OKS5-009 |
| `ok.pit.statutory.rate.top` | 4.5 | from 2026-01-01 | US-OKS5-009 |
| `ok.pit.std_deduction.hoh` | 9350 | from 2017-01-01 | US-OKS5-011 |
| `ok.pit.std_deduction.mfj` | 12,700 | from 2017-01-01 | US-OKS5-011 |
| `ok.pit.std_deduction.single` | 6350 | from 2017-01-01 | US-OKS5-011 |
| `ok.pit.wh.married.annual.thresholds` | 20200;22500;27100 | from 2026-01-01 | US-OK-001 |
| `ok.pit.wh.single.annual.thresholds` | 10100;11250;13550 | from 2026-01-01 | US-OK-001 |
| `ok.prevailing_wage.exists` | False | from 2015-11-01 | US-OKS5-016 |
| `ok.reciprocity.states` | none | from 2026-01-01 | US-OKP51-002 |
| `ok.records.payroll_tax.retention_years` | 4 | from 2019-08-11 | US-OKS5-014 |
| `ok.report.ui.format` | ICESA 275-character fixed records (E, S, T) | from 2024-10-01 | US-OKS5-020 |
| `ok.report.w2.due` | 31 January via OkTAP (EFW2 or manual) | from 2023-07-01 | US-OKS5-010 |
| `ok.report.wh.monthly_threshold.quarterly` | 500 | from 2023-07-01 | US-OKS5-010 |
| `ok.report.wh.return_due` | 20th of month after quarter | from 2023-07-01 | US-OKS5-010 |
| `ok.sui.employee.rate` | 0 | from 2025-11-01 | US-OKS5-005 |
| `ok.sui.employer.rate.max` | 5.5 | from 2027-01-01 to 2027-12-31 | US-OKS5-018 |
| `ok.sui.employer.rate.max` | 5.8 | from 2026-01-01 to 2026-12-31 | US-OK-002 |
| `ok.sui.employer.rate.min` | 0.1 | from 2027-01-01 to 2027-12-31 | US-OKS5-018 |
| `ok.sui.employer.rate.min` | 0.2 | from 2026-01-01 to 2026-12-31 | US-OK-002 |
| `ok.sui.new_employer.rate` | 1.5 | from 2026-01-01 to 2027-12-31 | US-OKS5-018 |
| `ok.sui.wage_base` | 24,400 | from 2027-01-01 to 2027-12-31 | US-OKS5-018 |
| `ok.sui.wage_base` | 25,000 | from 2026-01-01 to 2026-12-31 | US-OK-002 |
| `ok.sui.wage_base.other_state_credit` | True | from 2025-11-01 | US-OKS5-005 |
| `ok.sui.wages.401k_included` | True | from 2019-07-01 | US-OKS5-006 |
| `ok.sui.wages.section125_included` | False | from 2019-07-01 | US-OKS5-006 |
| `ok.term.vacation.payout` | per agreement or established policy | from 2022-11-01 | US-OKS5-003 |
| `ok.ui.average_annual_wage.caliber` | 60,993.99 | from 2027-01-01 to 2027-12-31 | US-OKS5-018 |
| `ok.wh.certificate` | OK-W-4 (Rev. 3-2021); none on file = Single, 0 allowances | from 2019-08-11 | US-OKS5-014 |
| `ok.wh.method` | OW-2 (Rev. 11-2025) percentage formula or wage-bracket tables | from 2026-01-01 | US-OK-001 |
| `ok.wh.supplemental.rate` | 4.5 | from 2026-01-01 | US-OK-001 |
