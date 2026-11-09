# Annex SC: South Carolina


Jurisdiction annex of the United States Country Configuration Guide (US-CCG-001). Layer classification: **T3 - state withholding; local layer absent or piggybacked on the state return** (build manifest, tier rationale).

The federal layer (federal income tax withholding, FICA, FUTA, Forms W-2, 941 and 940) and the multistate rules (residence and work-location sourcing, reciprocity mechanics) are in Annex FED and Annex MULTI and are not repeated here. Independent contractors and Form 1099-NEC reporting are out of scope (owner instruction of 2026-10-29) [US-OWN-008]. Payslip language: English; second-language duties attach to notices and posters only (US-OWN-006).

Every value in this annex is bound to a verified fact and carries its legal-basis register id. A value that changes during the year is shown with its effective dates. A point marked as a research gap has not been closed by the research; it is not filled with an estimate.

## SC.1 Employment and labour code

- **Minimum wage:** no state minimum-wage statute (state rate exists: [[FACT:sc.labour.minwage.state.exists=False]]); the federal FLSA rate applies (Annex FED). Local minimum wages are preempted (6-1-130): [[FACT:sc.local_mandates.preempted=True]] [US-SCS5-012, US-SCR3-006]. No 2027 change enacted.
- **Overtime:** [[FACT:sc.labour.overtime.state_rule=none (FLSA only)]] [US-SCR3-006].
- **Pay frequency and timing:** no statutory frequency; pay at the time and place set in the hire notice (41-10-30(A)); changes need [[FACT:sc.labour.pay_change_notice.days=7]] calendar days' written notice (wage increases excepted) [US-SCP52-006].
- **Method of payment (41-10-40(A)-(B)) [US-SCP52-006]:** lawful money, or a negotiable warrant or check dated the payday; deposit to an insured institution allowed; with direct deposit, a statement of earnings and withholdings and at least one free withdrawal per deposit ([[FACT:sc.labour.direct_deposit.free_withdrawal=True]]). Paycards are not mentioned.
- **Deductions:** none without state or federal authority or the written hire notice (41-10-40(C)); unpaid wages carry treble damages (41-10-80(C)).
- **Lactation:** reasonable unpaid break time (41-1-130) [US-SCS5-013].

**Parameters (labour code and pay rules)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `sc.labour.minwage.state.exists` | [[FACT:sc.labour.minwage.state.exists=False]] |  | from 2014-06-09 | US-SCS5-012 |  |
| `sc.local_mandates.preempted` | [[FACT:sc.local_mandates.preempted=True]] |  | from 2014-06-09 | US-SCS5-012 | 6-1-130 |
| `sc.labour.overtime.state_rule` | [[FACT:sc.labour.overtime.state_rule=none (FLSA only)]] |  | from 2026-01-01 | US-SCR3-006 | absence at chapter-index level |
| `sc.labour.pay_change_notice.days` | [[FACT:sc.labour.pay_change_notice.days=7]] | days | from 2026-01-01 | US-SCP52-006 | Written notice before changing time/place of payment (41-10-30(A)). |
| `sc.labour.direct_deposit.free_withdrawal` | [[FACT:sc.labour.direct_deposit.free_withdrawal=True]] |  | from 2026-01-01 | US-SCP52-006 | 41-10-40(A)-(B). |

**Open research points**

- Not configured in this release [[GAP:RQ-319]]: LLR child-labour regulations not read.

## SC.2 Income tax withholding

- **Act 110 trap (binding).** The two-rate schedule of 2026 Act No. 110 ([[FACT:sc.pit.statutory.rate.1=1.99]] % up to [[FACT:sc.pit.statutory.bracket.1.ceiling=30,000]] USD of taxable income and [[FACT:sc.pit.statutory.rate.2=5.21]] % above, with the SC income adjustment deduction of [[FACT:sc.pit.sciad.single=15,000]] USD for single filers) applies **at assessment** for tax year 2026 [US-SCS5-001, US-SCS5-005]. **2026 withholding stays on WH-1603F** until SCDOR reissues the tables; the Act 110 rates are never put in the 2026 withholding engine. Revised tables: blocking open point below.
- **Withholding method 2026 (operative) [US-SCS5-004]:** [[FACT:sc.wh.method=WH-1603F: annualize; minus 5,000 per allowance; minus std deduction 10% of gross capped 7,500 (only with 1+ allowances); bands]].
  - Allowance [[FACT:sc.pit.allowance.annual=5000]] USD per year; standard deduction [[FACT:sc.pit.wh.std_deduction.rate=10]] % of gross, capped at [[FACT:sc.pit.wh.std_deduction.cap=7500]] USD, only with one or more allowances.

| Annual wages after deductions | Annual withholding | Register id |
|---|---|---|
| below [[FACT:sc.pit.wh.band.1.ceiling=3640]] USD | zero | US-SCS5-004 |
| from the first ceiling to [[FACT:sc.pit.wh.band.3.floor=18,230]] USD | [[FACT:sc.pit.wh.band.2.rate=3]] % minus [[FACT:sc.pit.wh.band.2.subtract=109.20]] USD | US-SCS5-004 |
| from the second floor | [[FACT:sc.pit.wh.band.3.rate=6]] % minus [[FACT:sc.pit.wh.band.3.subtract=656.10]] USD | US-SCS5-004 |

- **Oracle:** WH-1603F worked example (weekly, three allowances): [[FACT:sc.pit.oracle.example_1.withholding=10.58]] USD, reproduced exactly. Recomputation in Module 12.
- **Certificate [US-SCS5-003, US-SCP51-003]:** [[FACT:sc.wh.certificate=SC W-4 (2026); none = zero allowances; no flat amount on regular wages]]; exempt status expires at year end; military-spouse domicile election (RR #24-5).
- **Threshold and rounding (12-8-520) [US-SCS5-018, US-SCR3-001]:** withhold if wages are expected to reach [[FACT:sc.pit.withholding_threshold.annual=1000]] USD in the year; wages may be computed to the nearest dollar.
- **Supplemental wages:** no flat supplemental rate (exists: [[FACT:sc.pit.supplemental.flat_rate.exists=False]]); bonuses run through the tables [US-SCR3-002, US-SCS5-002].
- **Residents and nonresidents [US-SCS5-002, US-SCS5-018, US-SCR3-003, US-SCR3-004]:** wages are taxed where earned; a nonresident is withheld on South Carolina wages; a resident working in a state with no income tax is withheld for South Carolina; a resident's wages earned in another state are not withheld where that state's withholding applies (12-8-520(C)(1)), with a credit at assessment (12-6-3400). Reciprocity: [[FACT:sc.reciprocity.states=none]].
- **Local income taxes:** none (exists: [[FACT:sc.local_wage_tax.exists=False]]) [US-SCP52-003].
- **Conformity:** IRC as of [[FACT:sc.pit.conformity.irc_date=2024-12-31]] (12-6-40(A)(1)(a)) [US-SCS5-001].
- **Resident and nonresident matrix.**

| Income type | South Carolina resident | Nonresident |
|---|---|---|
| Regular salary | WH-1603F on all wages, except wages earned in another state that withholds | WH-1603F on South Carolina wages |
| Bonus / supplemental | Through the tables (no flat rate) | Same, South Carolina share |
| Assessment (not payroll) | Act 110 two-rate schedule | Same, with the adjustment deduction prorated |
| Temporary personal services (non-wage) | - | Separate nonresident withholding under 12-8-550 (not payroll wages) |

**Parameters (income tax withholding (state and local))**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `sc.wh.method` | [[FACT:sc.wh.method=WH-1603F: annualize; minus 5,000 per allowance; minus std deduction 10% of gross capped 7,500 (only with 1+ allowances); bands]] |  | 2026-01-01 to 2026-12-31 | US-SCS5-004 | operative 2026 withholding (Act 110 not yet in tables) |
| `sc.pit.allowance.annual` | [[FACT:sc.pit.allowance.annual=5000]] | USD | 2026-01-01 to 2026-12-31 | US-SCS5-004 |  |
| `sc.pit.wh.std_deduction.rate` | [[FACT:sc.pit.wh.std_deduction.rate=10]] | % | 2026-01-01 to 2026-12-31 | US-SCS5-004 | cap 7,500 |
| `sc.pit.wh.std_deduction.cap` | [[FACT:sc.pit.wh.std_deduction.cap=7500]] | USD | 2026-01-01 to 2026-12-31 | US-SCS5-004 |  |
| `sc.pit.wh.band.1.ceiling` | [[FACT:sc.pit.wh.band.1.ceiling=3640]] | USD | 2026-01-01 to 2026-12-31 | US-SCP51-002 | 0% below |
| `sc.pit.wh.band.2.rate` | [[FACT:sc.pit.wh.band.2.rate=3]] | % | 2026-01-01 to 2026-12-31 | US-SCP51-002 |  |
| `sc.pit.wh.band.2.subtract` | [[FACT:sc.pit.wh.band.2.subtract=109.20]] | USD | 2026-01-01 to 2026-12-31 | US-SCP51-002 |  |
| `sc.pit.wh.band.3.floor` | [[FACT:sc.pit.wh.band.3.floor=18,230]] | USD | 2026-01-01 to 2026-12-31 | US-SCP51-002 |  |
| `sc.pit.wh.band.3.rate` | [[FACT:sc.pit.wh.band.3.rate=6]] | % | 2026-01-01 to 2026-12-31 | US-SCP51-002 |  |
| `sc.pit.wh.band.3.subtract` | [[FACT:sc.pit.wh.band.3.subtract=656.10]] | USD | 2026-01-01 to 2026-12-31 | US-SCP51-002 |  |
| `sc.pit.oracle.example_1.withholding` | [[FACT:sc.pit.oracle.example_1.withholding=10.58]] | USD | 2026-01-01 to 2026-12-31 | US-SCP51-002 |  |
| `sc.wh.certificate` | [[FACT:sc.wh.certificate=SC W-4 (2026); none = zero allowances; no flat amount on regular wages]] |  | from 2026-01-01 | US-SCS5-003 | exempt expires 2026-12-31 |
| `sc.pit.withholding_threshold.annual` | [[FACT:sc.pit.withholding_threshold.annual=1000]] | USD | from 2026-01-01 | US-SCS5-018 | withhold if wages expected to reach 1,000; may compute wages to nearest dollar |
| `sc.pit.supplemental.flat_rate.exists` | [[FACT:sc.pit.supplemental.flat_rate.exists=False]] |  | from 2026-01-01 | US-SCS5-002 | bonuses through the tables |
| `sc.pit.statutory.rate.1` | [[FACT:sc.pit.statutory.rate.1=1.99]] | % | from 2026-01-01 | US-SCS5-001 | Act 110 ASSESSMENT level only (TY2026 return); not in 2026 withholding |
| `sc.pit.statutory.rate.2` | [[FACT:sc.pit.statutory.rate.2=5.21]] | % | from 2026-01-01 | US-SCS5-001 | assessment level only; minus 966 above 30,000 bracket |
| `sc.pit.statutory.bracket.1.ceiling` | [[FACT:sc.pit.statutory.bracket.1.ceiling=30,000]] | USD | from 2026-01-01 | US-SCS5-001 | indexed by chained CPI (cap 4%) |
| `sc.pit.sciad.single` | [[FACT:sc.pit.sciad.single=15,000]] | USD | from 2026-01-01 | US-SCS5-005 | assessment; HoH 22,500; MFJ 30,000; phase-out |
| `sc.reciprocity.states` | [[FACT:sc.reciprocity.states=none]] |  | from 2026-01-01 | US-SCS5-018 | resident credit at assessment (12-6-3400) |
| `sc.pit.conformity.irc_date` | [[FACT:sc.pit.conformity.irc_date=2024-12-31]] |  | from 2026-01-01 | US-SCS5-001 | OBBBA 2025 not adopted unless later conformity act |
| `sc.local_wage_tax.exists` | [[FACT:sc.local_wage_tax.exists=False]] |  | from 2026-01-01 | US-SCP52-003 |  |

**Open research points**

- Not yet published [[GAP:RQ-315]]: SCDOR has not republished WH-1603 / WH-1603F after Act 110 (Information Letter #26-20: SCDOR "will consult"); the 2027 files are not yet published. Withholding stays on the current WH-1603F; no Act 110 rate enters the withholding engine.

## SC.2b Non-resident regime and reciprocity

The non-resident and reciprocity rules of this jurisdiction are written in SC.2.

## SC.2c Local wage taxes

The local wage taxes of this jurisdiction, where any exist, are written in SC.2.

## SC.3 Social insurance: unemployment, disability, paid leave and payroll levies

- **Unemployment insurance (DEW) [US-SCS5-014, US-SC-003].** Employer-only; deduction from wages prohibited (41-31-310); employee rate [[FACT:sc.sui.employee.rate=0]] % [US-SCP52-005]. Taxable wage base [[FACT:sc.sui.wage_base=14,000]] USD per employee, fixed by statute and not indexed; wages reported under other states' laws count toward it: [[FACT:sc.sui.wage_base.other_state_credit=True]] (41-27-380(B)).
- **2026 rates [US-SC-003]:** total rates from [[FACT:sc.ui.rate.min_total=0.06]] % (class 1) to [[FACT:sc.ui.rate.max_total=5.46]] % (class 20), including the Departmental Administrative Contingency Assessment of [[FACT:sc.ui.daca.rate=0.06]] % (41-27-410) [US-SCS5-014]; no solvency surcharge in 2026; new employer [[FACT:sc.sui.new_employer.rate=1.06]] %.
- **2026 Act No. 243 (in force 2026-07-01) [US-SCS5-015]:** benefit-ratio look-back of [[FACT:sc.ui.benefit_ratio.lookback_quarters=16]] quarters for tax year 2027 (longer from 2028); solvency surcharge rewritten; higher rate on unpaid-tax executions from 2027; late-report penalty caps removed. The 2027 rate table is open (below).
- **Coverage of agricultural labour and domestic service (41-27-230) [US-SCS5-014]:** agricultural labour is covered employment where the employer, in any calendar quarter of the current or the preceding calendar year, paid cash wages of [[FACT:sc.ui.coverage.agricultural.cash_per_quarter=20,000]] USD or more for agricultural labour, or employed in agricultural labour [[FACT:sc.ui.coverage.agricultural.workers_in_20_weeks=10]] or more individuals for some portion of a day in each of twenty different calendar weeks of the current or the preceding calendar year. Domestic service in a private home, a local college club or a local chapter of a college fraternity or sorority is covered where the employer paid cash wages of [[FACT:sc.ui.coverage.domestic.cash_per_quarter=1000]] USD or more for such service in any calendar quarter of the current or the preceding calendar year.
- **SDI, TDI, PFML, LTC:** none (exists: [[FACT:sc.sdi_pfml.exists=False]]) [US-SCR3-006]. Corporate officers are covered unless the corporation elects out (41-27-265) [US-SCS5-014].

**Parameters (social insurance and payroll levies)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `sc.sui.wage_base` | [[FACT:sc.sui.wage_base=14,000]] | USD | from 2015-01-01 | US-SCS5-014 | statutory, not indexed; other-state wages count (41-27-380(B)) |
| `sc.sui.wage_base.other_state_credit` | [[FACT:sc.sui.wage_base.other_state_credit=True]] |  | from 2015-01-01 | US-SCS5-014 |  |
| `sc.ui.rate.min_total` | [[FACT:sc.ui.rate.min_total=0.06]] | % | 2026-01-01 to 2026-12-31 | US-SC-003 |  |
| `sc.ui.rate.max_total` | [[FACT:sc.ui.rate.max_total=5.46]] | % | 2026-01-01 to 2026-12-31 | US-SC-003 |  |
| `sc.sui.new_employer.rate` | [[FACT:sc.sui.new_employer.rate=1.06]] | % | 2026-01-01 to 2026-12-31 | US-SC-003 | higher of class 12 or 1%, plus DACA |
| `sc.ui.daca.rate` | [[FACT:sc.ui.daca.rate=0.06]] | % | from 2015-01-01 | US-SCS5-014 | 41-27-410; second authority DEW page US-SCR3-007; not reimbursing/governmental |
| `sc.ui.benefit_ratio.lookback_quarters` | [[FACT:sc.ui.benefit_ratio.lookback_quarters=16]] |  | 2027-01-01 to 2027-12-31 | US-SCS5-015 | Act 243: 12 through 2026; 20 from 2028 |
| `sc.sdi_pfml.exists` | [[FACT:sc.sdi_pfml.exists=False]] |  | from 2026-01-01 | US-SCR3-006 |  |
| `sc.sui.employee.rate` | [[FACT:sc.sui.employee.rate=0]] | % | from 2026-01-01 | US-SCP52-005 | May not be deducted from wages. |
| `sc.ui.coverage.agricultural.cash_per_quarter` | [[FACT:sc.ui.coverage.agricultural.cash_per_quarter=20,000]] | USD | from 1978-01-01 | US-SCS5-014 | 41-27-230(5)(a)(i): agricultural labor is employment where the person 'during any calendar quarter in either the current or preceding calendar year paid remuneration in cash of twenty thousand dollars or more to individuals employed in agricultural labor'. In force as at retrieval; the subsection applies to service 'performed after December 31, 1977'. |
| `sc.ui.coverage.agricultural.workers_in_20_weeks` | [[FACT:sc.ui.coverage.agricultural.workers_in_20_weeks=10]] | persons | from 1978-01-01 | US-SCS5-014 | 41-27-230(5)(a)(ii): or 'for some portion of a day in each of twenty different calendar weeks ... in either the current or the preceding calendar year, employed in agricultural labor ... ten or more individuals'. In force as at retrieval; the subsection applies to service 'performed after December 31, 1977'. |
| `sc.ui.coverage.domestic.cash_per_quarter` | [[FACT:sc.ui.coverage.domestic.cash_per_quarter=1000]] | USD | from 1978-01-01 | US-SCS5-014 | 41-27-230: domestic service in a private home, local college club or fraternity/sorority chapter is employment where the person 'paid cash remuneration of one thousand dollars or more ... in the current calendar year or the preceding calendar year to individuals employed in such domestic service in any calendar quarter'. In force as at retrieval; applies to remuneration paid 'after December 31, 1977'. |

**Open research points**

- Not configured in this release [[GAP:RQ-316]]: Not established from an official source.

## SC.4 Pay statement

- **Content (41-10-30(C), 41-10-40(B)) [US-SCP52-006]:** [[FACT:sc.payslip.items=itemized gross pay and deductions each pay period]]; with direct deposit, a statement of earnings and withholdings. No other field is required. Employers of domestic labour in private homes and very small employers are exempt from 41-10-30 (41-10-20).
- **Hire notice:** normal hours, wages, time and place of payment, and deductions, in writing or posted.
- **Electronic delivery:** no statute addresses it ("furnish" only).
- **Retention:** wage-payment records [[FACT:sc.records.wage.retention_years=3]] years (41-10-30(B)); UI payroll records per Reg. 47-14 [US-SCS5-007].

**Parameters (payslip statute and payroll records)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `sc.payslip.items` | [[FACT:sc.payslip.items=itemized gross pay and deductions each pay period]] |  | from 2026-01-01 | US-SCP52-006 | 41-10-30(C); domestic and <5 employers exempt. |
| `sc.records.wage.retention_years` | [[FACT:sc.records.wage.retention_years=3]] | years | from 2026-01-01 | US-SCP52-006 | UI payroll records 5 years (Reg. 47-14, US-SCS5-007). |

## SC.5 Statutory reporting

- **Withholding deposits (SCDOR, MyDORWAY) [US-SCS5-002, US-SCS5-018]:** resident agents on the federal deposit dates; others monthly by the 15th if withholding reaches [[FACT:sc.report.wh.deposit_threshold.monthly=500]] USD, otherwise quarterly.
- **WH-1605 (first three quarters):** due [[FACT:sc.report.wh1605.due=Apr 30; Jul 31; Oct 31]]; zero returns required while the account is open. **WH-1606** (fourth quarter and annual reconciliation) due January 31 [US-SCS5-002].
- **W-2 to SCDOR [US-SCS5-016, US-SCS5-017]:** [[FACT:sc.report.w2.due=Jan 31; EFW2 with SC RS record (state code 45, full SSN); electronic at 10+ forms]]. Filing with SSA does not satisfy South Carolina.
- **Quarterly UI contribution and wage report (DEW, SUITS) [US-SCS5-006, US-SCS5-007]:** due [[FACT:sc.report.ui.quarterly_due=last day of month after quarter]]; ICESA, EFW2, XML or CSV.
- **New hire [US-SCS5-011]:** to the DSS State Directory of New Hires within [[FACT:sc.newhire.report_days=20]] calendar days.
- **Mass separation:** form UCB-113 per worker to DEW [US-SCS5-007].
- **Scope note:** the TY2026 RS-1 edition is not yet published (open point below) [US-SCS5-017].

**Parameters (statutory reporting)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `sc.report.wh.deposit_threshold.monthly` | [[FACT:sc.report.wh.deposit_threshold.monthly=500]] | USD | from 2026-01-01 | US-SCS5-002 | nonresident agents: by 15th if >=500 else quarterly; resident agents follow federal dates |
| `sc.report.wh1605.due` | [[FACT:sc.report.wh1605.due=Apr 30; Jul 31; Oct 31]] |  | from 2026-01-01 | US-SCS5-002 |  |
| `sc.report.w2.due` | [[FACT:sc.report.w2.due=Jan 31; EFW2 with SC RS record (state code 45, full SSN); electronic at 10+ forms]] |  | from 2026-01-01 | US-SCS5-016 | SSA filing does not satisfy SC |
| `sc.report.ui.quarterly_due` | [[FACT:sc.report.ui.quarterly_due=last day of month after quarter]] |  | from 2023-10-25 | US-SCS5-006 | SUITS ICESA/EFW2/XML/CSV |
| `sc.newhire.report_days` | [[FACT:sc.newhire.report_days=20]] | days | from 1998-10-01 | US-SCS5-011 |  |

**Open research points**

- Not configured in this release [[GAP:RQ-317]]: TY2026 RS-1 not yet published.

## SC.6 Leave

- **Paid sick leave:** no state statute (exists: [[FACT:sc.leave.sick.state_statute.exists=False]]); local benefit mandates are preempted (41-1-25) [US-SCS5-013]. No PFML. Jury duty is protected without a paid-leave mandate (41-1-70). Vacation and sick pay follow policy and become wages once due.

**Parameters (leave)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `sc.leave.sick.state_statute.exists` | [[FACT:sc.leave.sick.state_statute.exists=False]] |  | from 2017-04-05 | US-SCS5-013 | local benefit mandates preempted (41-1-25) |

## SC.7 Termination and final pay

- **Final pay (41-10-50) [US-SCP52-006]:** [[FACT:sc.final_pay.rule=within 48 hours or next regular payday (max 30 days)]], for any separation; treble damages for failure.
- **Accrued vacation:** [[FACT:sc.term.vacation.payout=only if due under policy or contract]] (41-10-10(2)).
- **Separation notice:** no employer-issued UI notice at termination; the employer answers DEW's claim notice; mass separations use UCB-113 [US-SCS5-007]. Child support: notify the clerk of the termination date and final paycheck (63-17-1460(G)) [US-SCS5-010]. No state WARN law found.

**Parameters (termination)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `sc.final_pay.rule` | [[FACT:sc.final_pay.rule=within 48 hours or next regular payday (max 30 days)]] |  | from 2026-01-01 | US-SCP52-006 | 41-10-50; treble damages. |
| `sc.term.vacation.payout` | [[FACT:sc.term.vacation.payout=only if due under policy or contract]] |  | from 2026-01-01 | US-SCP52-006 |  |

## SC.8 Benefits in kind and taxable wages

- **Conformity:** IRC as of the conformity date above; Act 110 decouples only the federal standard and itemised deductions. Federal exclusions for retirement deferrals, cafeteria plans, HSA, transit and group-term life follow the conformed IRC; later federal changes are not adopted until a conformity act passes. Item-by-item SC additions and subtractions: open point below [US-SCS5-001].
- **UI:** in-kind pay valued at DEW rates; in-kind pay to agricultural and domestic workers and employer plan payments are excluded from UI wages (41-27-380(A)) [US-SCS5-007, US-SCS5-014].

**Open research points**

- Not configured in this release [[GAP:RQ-321]]: 12-6-1130/1140 item-by-item fringe treatment after Act 110 not read.

## SC.9 Deductions and garnishments

- **Consumer debt:** no wage garnishment for consumer credit (37-5-104) (available: [[FACT:sc.garn.consumer.available=False]]); no discharge over such a garnishment [US-SCS5-008].
- **Child support [US-SCS5-010]:** start by the next regular pay period after service; CCPA cap (Annex FED); employer fee up to [[FACT:sc.garn.iwo.employer_fee.per_withholding=3]] USD per withholding, deducted from the obligor; current support first; remit to the State Disbursement Unit within [[FACT:sc.garn.iwo.remit_working_days=7]] working days. Out-of-state orders follow the law of the principal place of employment.

**Parameters (deductions and garnishments)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `sc.garn.consumer.available` | [[FACT:sc.garn.consumer.available=False]] |  | from 2026-01-01 | US-SCS5-008 | 37-5-104 no garnishment for consumer debt |
| `sc.garn.iwo.employer_fee.per_withholding` | [[FACT:sc.garn.iwo.employer_fee.per_withholding=3]] | USD | from 2026-01-01 | US-SCS5-010 | remit within 7 working days |
| `sc.garn.iwo.remit_working_days` | [[FACT:sc.garn.iwo.remit_working_days=7]] | days | from 2026-01-01 | US-SCS5-010 |  |

**Open research points**

- Not configured in this release [[GAP:RQ-320]]: SCDOR wage levy not read.

## SC.10 Collective agreements and prevailing wage

- **No state prevailing-wage law** (exists: [[FACT:sc.prevailing_wage.exists=False]]); federal Davis-Bacon applies on federal projects only [US-SCR3-009].

**Parameters (collective agreements and prevailing wage)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `sc.prevailing_wage.exists` | [[FACT:sc.prevailing_wage.exists=False]] |  | from 2026-01-01 | US-SCR3-009 |  |

## SC.11 Indexation

- **Income tax brackets:** indexed each 15 December by chained CPI, capped, for the next tax year (12-6-520); the Act 110 bracket ceiling is indexed the same way. From tax year 2027 the top rate falls under a revenue trigger (12-6-510(C)(2)) [US-SCS5-001, US-SCS5-005].
- **Withholding constants** (allowance, standard deduction rate and cap): set by SCDOR in WH-1603F each year, not statutory; 2027 files not yet published [US-SCS5-002].
- **Not indexed:** the UI wage base (statutory) and the minimum wage (federal).

## SC.12 Payroll data protection and records

- **SSN (37-20-180) [US-SCS5-009, US-SCS5-017]:** no public display; mailed material may carry at most [[FACT:sc.data.ssn.max_digits_mailed=5]] digits of the SSN unless law requires more, never visible through the envelope; secure transmission only. Mailed pay statements therefore show no more than that; the W-2 and the RS record (full SSN) are exempt as legally required.

**Parameters (payroll data protection)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `sc.data.ssn.max_digits_mailed` | [[FACT:sc.data.ssn.max_digits_mailed=5]] |  | from 2026-01-01 | US-SCS5-009 | no 6+ digits on mailed materials; W-2/RS exempt |

## SC.13 Live legal change

- **2026 Act No. 110 (signed 2026-03-30):** new two-rate schedule for tax year 2026 at assessment; Section 6 orders SCDOR to adjust withholding tables, not yet implemented (SCDOR Information Letter #26-20) [US-SCS5-001, US-SCS5-005].
- **2026 Act No. 243 (in force 2026-07-01):** UI benefit ratio and penalties, effective for tax year 2027 [US-SCS5-015].
- **Tax year 2027 rate cut:** contingent on the revenue forecast; not determined [US-SCS5-001].

## SC.14 Authority worked examples (oracle values)

No authority worked example is reproduced in this annex; recomputed withholding examples are in Module 12.

## SC.15 Special populations

| Population | South Carolina rule | Register id |
|---|---|---|
| Domestic / household | Exempt from the 41-10-30 notice and pay-statement duties; in-kind pay excluded from UI wages; UI coverage threshold not extracted | US-SCS5-014 |
| Agricultural | Agricultural labour by students or qualifying part-timers excluded from UI (41-27-260(16)); in-kind pay excluded; minimum wage federal | US-SCS5-014 |
| Minors | Child-labour rules delegated to LLR regulations (not read); minor newspaper carriers and a minor child employed by a parent excluded from UI | US-SCS5-014 |
| Tipped | Federal tipped rules apply; reported tips are UI wages | US-SCS5-014, US-SCS5-012 |
| Clergy / religious | Churches and ministers excluded from UI (41-27-260(10)); withholding follows the federal wage definition | US-SCS5-014 |
| Students | Own-school students, student nurses and interns excluded from UI | US-SCS5-014 |
| Nonresident aliens | General rule: South Carolina wages withheld regardless of residence | US-SCS5-018 |
| Statutory employees | No state rule beyond federal | US-SCS5-018 |
| Government employees | Elected and policymaking posts excluded from UI; governmental employers exempt from the administrative assessment | US-SCS5-014, US-SCS5-018 |
| Corporate officers | UI-covered unless the corporation elects out | US-SCS5-014 |
| Military spouses | Exemption election on the SC W-4 | US-SCS5-003 |
| Commission-only insurance and real-estate agents, direct sellers, owner-operator drivers | Excluded from UI | US-SCS5-014 |

## SC.16 Language

No language rule for employee documents is written for this jurisdiction in this annex.

## SC.S Sources

Register ids cited in this annex resolve to the build record; the URL of each value is in the facts file. Authorities:

- Build lead (Claude) under owner delegation (Wallisson Gomes): US-OWN-006
- Owner (Wallisson Gomes): US-OWN-008
- SC Dept of Employment and Workforce: US-SC-003
- SC Legislative Services Agency: US-SCR3-001, US-SCR3-004, US-SCR3-006
- SC Legislative Services Agency (Code of Regulations): US-SCR3-002, US-SCS5-007
- South Carolina Department of Employment and Workforce: US-SCR3-007, US-SCS5-006
- South Carolina Department of Revenue: US-SCP51-002, US-SCP51-003, US-SCP52-003, US-SCR3-003, US-SCS5-002, US-SCS5-003, US-SCS5-004, US-SCS5-005, US-SCS5-016, US-SCS5-017
- South Carolina General Assembly: US-SCS5-001
- South Carolina Legislature: US-SCP52-005, US-SCP52-006, US-SCS5-008, US-SCS5-009, US-SCS5-010, US-SCS5-011, US-SCS5-012, US-SCS5-013, US-SCS5-014, US-SCS5-015, US-SCS5-018
- South Carolina Legislature (S.C. Code Title 41 ch. 27): US-SCS5-014
- US DOL Wage and Hour Division: US-SCR3-009
