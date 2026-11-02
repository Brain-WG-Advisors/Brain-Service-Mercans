## @labour
- **Minimum wage:** no state minimum-wage statute (state rate exists: {{sc.labour.minwage.state.exists}}); the federal FLSA rate applies (Annex FED). Local minimum wages are preempted (6-1-130): {{sc.local_mandates.preempted}} [US-SCS5-012, US-SCR3-006]. No 2027 change enacted.
- **Overtime:** {{sc.labour.overtime.state_rule}} [US-SCR3-006].
- **Pay frequency and timing:** no statutory frequency; pay at the time and place set in the hire notice (41-10-30(A)); changes need {{sc.labour.pay_change_notice.days}} calendar days' written notice (wage increases excepted) [US-SCP52-006].
- **Method of payment (41-10-40(A)-(B)) [US-SCP52-006]:** lawful money, or a negotiable warrant or check dated the payday; deposit to an insured institution allowed; with direct deposit, a statement of earnings and withholdings and at least one free withdrawal per deposit ({{sc.labour.direct_deposit.free_withdrawal}}). Paycards are not mentioned.
- **Deductions:** none without state or federal authority or the written hire notice (41-10-40(C)); unpaid wages carry treble damages (41-10-80(C)).
- **Lactation:** reasonable unpaid break time (41-1-130) [US-SCS5-013].

## @income_tax
- **Act 110 trap (binding).** The two-rate schedule of 2026 Act No. 110 ({{sc.pit.statutory.rate.1}} % up to {{sc.pit.statutory.bracket.1.ceiling}} USD of taxable income and {{sc.pit.statutory.rate.2}} % above, with the SC income adjustment deduction of {{sc.pit.sciad.single}} USD for single filers) applies **at assessment** for tax year 2026 [US-SCS5-001, US-SCS5-005]. **2026 withholding stays on WH-1603F** until SCDOR reissues the tables; the Act 110 rates are never put in the 2026 withholding engine. Revised tables: blocking open point below.
- **Withholding method 2026 (operative) [US-SCS5-004]:** {{sc.wh.method}}.
  - Allowance {{sc.pit.allowance.annual}} USD per year; standard deduction {{sc.pit.wh.std_deduction.rate}} % of gross, capped at {{sc.pit.wh.std_deduction.cap}} USD, only with one or more allowances.

| Annual wages after deductions | Annual withholding | Register id |
|---|---|---|
| below {{sc.pit.wh.band.1.ceiling}} USD | zero | US-SCS5-004 |
| from the first ceiling to {{sc.pit.wh.band.3.floor}} USD | {{sc.pit.wh.band.2.rate}} % minus {{sc.pit.wh.band.2.subtract}} USD | US-SCS5-004 |
| from the second floor | {{sc.pit.wh.band.3.rate}} % minus {{sc.pit.wh.band.3.subtract}} USD | US-SCS5-004 |

- **Oracle:** WH-1603F worked example (weekly, three allowances): {{sc.pit.oracle.example_1.withholding}} USD, reproduced exactly. Recomputation in Module 12.
- **Certificate [US-SCS5-003, US-SCP51-003]:** {{sc.wh.certificate}}; exempt status expires at year end; military-spouse domicile election (RR #24-5).
- **Threshold and rounding (12-8-520) [US-SCS5-018, US-SCR3-001]:** withhold if wages are expected to reach {{sc.pit.withholding_threshold.annual}} USD in the year; wages may be computed to the nearest dollar.
- **Supplemental wages:** no flat supplemental rate (exists: {{sc.pit.supplemental.flat_rate.exists}}); bonuses run through the tables [US-SCR3-002, US-SCS5-002].
- **Residents and nonresidents [US-SCS5-002, US-SCS5-018, US-SCR3-003, US-SCR3-004]:** wages are taxed where earned; a nonresident is withheld on South Carolina wages; a resident working in a state with no income tax is withheld for South Carolina; a resident's wages earned in another state are not withheld where that state's withholding applies (12-8-520(C)(1)), with a credit at assessment (12-6-3400). Reciprocity: {{sc.reciprocity.states}}.
- **Local income taxes:** none (exists: {{sc.local_wage_tax.exists}}) [US-SCP52-003].
- **Conformity:** IRC as of {{sc.pit.conformity.irc_date}} (12-6-40(A)(1)(a)) [US-SCS5-001].
- **Resident and nonresident matrix.**

| Income type | South Carolina resident | Nonresident |
|---|---|---|
| Regular salary | WH-1603F on all wages, except wages earned in another state that withholds | WH-1603F on South Carolina wages |
| Bonus / supplemental | Through the tables (no flat rate) | Same, South Carolina share |
| Assessment (not payroll) | Act 110 two-rate schedule | Same, with the adjustment deduction prorated |
| Temporary personal services (non-wage) | - | Separate nonresident withholding under 12-8-550 (not payroll wages) |

## @social
- **Unemployment insurance (DEW) [US-SCS5-014, US-SC-003].** Employer-only; deduction from wages prohibited (41-31-310); employee rate {{sc.sui.employee.rate}} % [US-SCP52-005]. Taxable wage base {{sc.sui.wage_base}} USD per employee, fixed by statute and not indexed; wages reported under other states' laws count toward it: {{sc.sui.wage_base.other_state_credit}} (41-27-380(B)).
- **2026 rates [US-SC-003]:** total rates from {{sc.ui.rate.min_total}} % (class 1) to {{sc.ui.rate.max_total}} % (class 20), including the Departmental Administrative Contingency Assessment of {{sc.ui.daca.rate}} % (41-27-410) [US-SCS5-014]; no solvency surcharge in 2026; new employer {{sc.sui.new_employer.rate}} %.
- **2026 Act No. 243 (in force 2026-07-01) [US-SCS5-015]:** benefit-ratio look-back of {{sc.ui.benefit_ratio.lookback_quarters}} quarters for tax year 2027 (longer from 2028); solvency surcharge rewritten; higher rate on unpaid-tax executions from 2027; late-report penalty caps removed. The 2027 rate table is open (below).
- **SDI, TDI, PFML, LTC:** none (exists: {{sc.sdi_pfml.exists}}) [US-SCR3-006]. Corporate officers are covered unless the corporation elects out (41-27-265) [US-SCS5-014].

## @payslip
- **Content (41-10-30(C), 41-10-40(B)) [US-SCP52-006]:** {{sc.payslip.items}}; with direct deposit, a statement of earnings and withholdings. No other field is required. Employers of domestic labour in private homes and very small employers are exempt from 41-10-30 (41-10-20).
- **Hire notice:** normal hours, wages, time and place of payment, and deductions, in writing or posted.
- **Electronic delivery:** no statute addresses it ("furnish" only).
- **Retention:** wage-payment records {{sc.records.wage.retention_years}} years (41-10-30(B)); UI payroll records per Reg. 47-14 [US-SCS5-007].

## @reporting
- **Withholding deposits (SCDOR, MyDORWAY) [US-SCS5-002, US-SCS5-018]:** resident agents on the federal deposit dates; others monthly by the 15th if withholding reaches {{sc.report.wh.deposit_threshold.monthly}} USD, otherwise quarterly.
- **WH-1605 (first three quarters):** due {{sc.report.wh1605.due}}; zero returns required while the account is open. **WH-1606** (fourth quarter and annual reconciliation) due January 31 [US-SCS5-002].
- **W-2 to SCDOR [US-SCS5-016, US-SCS5-017]:** {{sc.report.w2.due}}. Filing with SSA does not satisfy South Carolina.
- **Quarterly UI contribution and wage report (DEW, SUITS) [US-SCS5-006, US-SCS5-007]:** due {{sc.report.ui.quarterly_due}}; ICESA, EFW2, XML or CSV.
- **New hire [US-SCS5-011]:** to the DSS State Directory of New Hires within {{sc.newhire.report_days}} calendar days.
- **Mass separation:** form UCB-113 per worker to DEW [US-SCS5-007].
- **Scope note:** the TY2026 RS-1 edition is not yet published (open point below) [US-SCS5-017].

## @leave
- **Paid sick leave:** no state statute (exists: {{sc.leave.sick.state_statute.exists}}); local benefit mandates are preempted (41-1-25) [US-SCS5-013]. No PFML. Jury duty is protected without a paid-leave mandate (41-1-70). Vacation and sick pay follow policy and become wages once due.

## @termination
- **Final pay (41-10-50) [US-SCP52-006]:** {{sc.final_pay.rule}}, for any separation; treble damages for failure.
- **Accrued vacation:** {{sc.term.vacation.payout}} (41-10-10(2)).
- **Separation notice:** no employer-issued UI notice at termination; the employer answers DEW's claim notice; mass separations use UCB-113 [US-SCS5-007]. Child support: notify the clerk of the termination date and final paycheck (63-17-1460(G)) [US-SCS5-010]. No state WARN law found.

## @bik
- **Conformity:** IRC as of the conformity date above; Act 110 decouples only the federal standard and itemised deductions. Federal exclusions for retirement deferrals, cafeteria plans, HSA, transit and group-term life follow the conformed IRC; later federal changes are not adopted until a conformity act passes. Item-by-item SC additions and subtractions: open point below [US-SCS5-001].
- **UI:** in-kind pay valued at DEW rates; in-kind pay to agricultural and domestic workers and employer plan payments are excluded from UI wages (41-27-380(A)) [US-SCS5-007, US-SCS5-014].

## @deductions
- **Consumer debt:** no wage garnishment for consumer credit (37-5-104) (available: {{sc.garn.consumer.available}}); no discharge over such a garnishment [US-SCS5-008].
- **Child support [US-SCS5-010]:** start by the next regular pay period after service; CCPA cap (Annex FED); employer fee up to {{sc.garn.iwo.employer_fee.per_withholding}} USD per withholding, deducted from the obligor; current support first; remit to the State Disbursement Unit within {{sc.garn.iwo.remit_working_days}} working days. Out-of-state orders follow the law of the principal place of employment.

## @cba
- **No state prevailing-wage law** (exists: {{sc.prevailing_wage.exists}}); federal Davis-Bacon applies on federal projects only [US-SCR3-009].

## @indexation
- **Income tax brackets:** indexed each 15 December by chained CPI, capped, for the next tax year (12-6-520); the Act 110 bracket ceiling is indexed the same way. From tax year 2027 the top rate falls under a revenue trigger (12-6-510(C)(2)) [US-SCS5-001, US-SCS5-005].
- **Withholding constants** (allowance, standard deduction rate and cap): set by SCDOR in WH-1603F each year, not statutory; 2027 files not yet published [US-SCS5-002].
- **Not indexed:** the UI wage base (statutory) and the minimum wage (federal).

## @data
- **SSN (37-20-180) [US-SCS5-009, US-SCS5-017]:** no public display; mailed material may carry at most {{sc.data.ssn.max_digits_mailed}} digits of the SSN unless law requires more, never visible through the envelope; secure transmission only. Mailed pay statements therefore show no more than that; the W-2 and the RS record (full SSN) are exempt as legally required.

## @live
- **2026 Act No. 110 (signed 2026-03-30):** new two-rate schedule for tax year 2026 at assessment; Section 6 orders SCDOR to adjust withholding tables, not yet implemented (SCDOR Information Letter #26-20) [US-SCS5-001, US-SCS5-005].
- **2026 Act No. 243 (in force 2026-07-01):** UI benefit ratio and penalties, effective for tax year 2027 [US-SCS5-015].
- **Tax year 2027 rate cut:** contingent on the revenue forecast; not determined [US-SCS5-001].

## @special
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

## @gaps
- sc.pit.tables.post_act110 :: SCDOR has not reissued WH-1603 / WH-1603F after Act 110 (Information Letter #26-20: SCDOR "will consult"); the 2027 files are not yet published. Withholding stays on the current WH-1603F; no Act 110 rate enters the withholding engine. :: SCDOR 2027 (or revised 2026) WH-1603F on dor.sc.gov/withholding (expected November 2026).
