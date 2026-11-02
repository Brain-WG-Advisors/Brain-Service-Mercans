# Annex ME: Maine

United States Country Configuration Guide, jurisdiction annex ME. Tax year 2026; currency USD (two decimal places).

## ME.0 Scope of this annex

This annex holds the Maine layer only. The federal layer (federal income tax withholding, Social Security and Medicare, federal unemployment tax, Forms W-4, W-2, 941 and 940) is in Annex FED, and the rules for employees who live and work in different jurisdictions (sourcing, resident credits, reciprocity mechanics) are in Annex MULTI. Neither is repeated here. Independent contractors and Form 1099-NEC are out of scope. The pay statement is issued in English.

In every table, *Valid from* and *Valid to* give the period in which the value applies (*open* means no end date has been published), and *Source* is the identifier of the row in the legal-basis register (00-official-sources/legal-basis-register.csv), with the authority and address listed in section ME.20 (the source address is held in the register row). Items marked as a research gap are not yet confirmed and must not be configured from this annex.

## ME.1 Jurisdiction layer

| Item | Value |
|---|---|
| Annex tier | T3 (verified) |
| Basis | Percentage method, 2026 booklet [US-MEP52-001, US-MEP52-009]; Title 36 contents: income taxes at State level only [US-MER3-001] |

Tier key: T1 = no state wage tax (unemployment insurance and levies only); T3 = state withholding with no local layer remitted separately; T4 = a local layer remitted to a separate local authority on its own return.

## ME.2 Configuration decisions

- Withholding uses the withholding standard deduction of the 2026 withholding method ([[FACT:me.wh.std_deduction.single=12450]] single, [[FACT:me.wh.std_deduction.married=27750]] married, with phase-out), not the standard deduction used on the individual return.
- The new-employer combined unemployment rate [[FACT:me.sui.new_employer.rate.total=2.54]] percent includes the Unemployment Program Administrative Fund component, whose 2026 rate differs between two authority sources. Treat the combined rate and its split as unconfirmed until the blocking gap in section ME.7 closes.
- A pay statement is required each payday: [[FACT:me.payslip.required=True]].
- There is no local wage tax ([[FACT:me.local_wage_tax.exists=False]]) and no reciprocity agreement.
- Paid family and medical leave contributions are deducted from the employee after tax: [[FACT:me.pfml.employee_deduction.after_tax=True]]; the employee share is reported on Form W-2 under the label [[FACT:me.pfml.w2_box14_label=MEPFML]].

## ME.3 Employment and labour code

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `me.minwage.hourly` | [[FACT:me.minwage.hourly=15.1]] USD | 2026-01-01 | 2026-12-31 | US-MES5-002 (A.2, Maine Department of Labor, Bureau of Labor Standards) | Agricultural and non-agricultural; CPI-W Northeast Aug-Aug rounded to 0.05 each Jan 1 [US-MES5-001]; step [[FACT:me.minwage.hourly=15.10]] -> [[FACT:me.minwage.hourly=15.70]] not reproduced (CPI not fetched). |
| `me.minwage.hourly` | [[FACT:me.minwage.hourly=15.7]] USD | 2027-01-01 | open | US-MES5-003 (A.2, Maine Department of Labor, Bureau of Labor Standards) | 2027 poster (rev. 9/26). |
| `me.minwage.tip_credit.max_percent` | [[FACT:me.minwage.tip_credit.max_percent=50]] percent | 2026-01-01 | open | US-MES5-001 (A.1, Maine Legislature, Office of the Revisor of Statutes) | Cash wage >= [[FACT:me.minwage.tipped.cash_wage=7.55]] in 2026 (derived); notice items A-F; weekly shortfall test; card tips by next payday without fee. |
| `me.minwage.tipped.cash_wage` | [[FACT:me.minwage.tipped.cash_wage=7.55]] USD | 2026-01-01 | 2026-12-31 | US-MES5-001 (A.1, Maine Legislature, Office of the Revisor of Statutes) | [[FACT:me.minwage.hourly=15.10]] x 0.5. |
| `me.local_minwage.portland.hourly` | [[FACT:me.local_minwage.portland.hourly=16.75]] USD | 2026-01-01 | 2026-12-31 | US-MES5-012 (A.1, City of Portland, Maine) | Hours within city limits; City employees from 2026-07-01; tip credit max half city rate; emergency work 1.5x; CPI-U Northeast from 2029. State does not pre-empt local MW (paid leave is pre-empted). |
| `me.local_minwage.portland.hourly` | [[FACT:me.local_minwage.portland.hourly=17.75]] USD | 2027-01-01 | 2027-12-31 | US-MES5-012 (A.1, City of Portland, Maine) |  |
| `me.local_minwage.portland.hourly` | [[FACT:me.local_minwage.portland.hourly=19.0]] USD | 2028-01-01 | open | US-MES5-012 (A.1, City of Portland, Maine) |  |
| `me.overtime.weekly_threshold_hours` | [[FACT:me.overtime.weekly_threshold_hours=40]] hours | 2026-01-01 | open | US-MES5-001 (A.1, Maine Legislature, Office of the Revisor of Statutes) | 1.5x; no daily OT; regular rate includes bonuses/commissions; exemptions auto sales/service, mariners, most public employees, listed ag/fish processing [US-MES5-005]. |
| `me.exempt.salary.weekly_min` | [[FACT:me.exempt.salary.weekly_min=871.16]] USD | 2026-01-01 | 2026-12-31 | US-MES5-002 (A.2, Maine Department of Labor, Bureau of Labor Standards) | Annualised pay must exceed 3,000 x the state minimum wage (or the FLSA level): 3,000 x [[FACT:me.minwage.hourly=15.10]] / 52 = 871.1538, published as [[FACT:me.exempt.salary.weekly_min=871.16]] (first cent above). Safe rule: the salary must exceed 3,000 x the minimum wage. |
| `me.pay_frequency.rule` | [[FACT:me.pay_frequency.rule=intervals not exceeding 16 days; each payment covers wages to within 8 days of payday; closed-day payday moves to next business day; lengthening interval needs 30 days written notice; rate decrease needs prior notice]] | 2026-01-01 | open | US-MES5-004 (A.1, Maine Legislature, Office of the Revisor of Statutes) |  |
| `me.direct_deposit.fee_prohibited` | [[FACT:me.direct_deposit.fee_prohibited=True]] | 2026-01-01 | open | US-MES5-004 (A.1, Maine Legislature, Office of the Revisor of Statutes) | 621-A(7); no consent/paycard rule in text read. |

- ⚠️ RESEARCH-GAP (non-blocking, `me.exempt.salary.next_year`): The 2027 salary threshold for exempt employees differs by a few cents between the state poster and the statutory formula; the 2027 threshold is not written. To close: MDOL overtime guidance page; safe rule: salary must exceed 3,000 x MW.
- ⚠️ RESEARCH-GAP (non-blocking, `me.minwage.derivation`): The Northeast CPI-W series used for the annual adjustment was not obtained, so the 2027 step was not checked against the index. To close: BLS series CWUR0100SA0 values.
- ⚠️ RESEARCH-GAP (non-blocking, `me.local_minwage.other`): Other municipal minimum wages (e.g. Rockland) not checked. To close: Municipal ordinance check or MDOL minimum-wage FAQ.
- ⚠️ RESEARCH-GAP (non-blocking, `me.payment.paycard_consent`): No paycard/direct-deposit consent rule beyond no-fee. To close: MDOL rule or Bureau of Consumer Credit Protection guidance.
- ⚠️ RESEARCH-GAP (non-blocking, `me.minwage.agricultural_basis`): The state poster applies the state minimum wage to agriculture, while 26 MRSA 663(3)(A) excludes agricultural workers from the subchapter. To close: 26 MRSA 664 as amended or the MDOL basis for the agricultural rate.

## ME.4 State income tax withholding

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `me.wh.method` | [[FACT:me.wh.method=annualise (52/26/24/12/260); - 5,300 per W-4ME allowance; - withholding standard deduction; apply schedule; divide by periods; round to nearest dollar]] | 2026-01-01 | 2026-12-31 | US-MES5-011 (A.2, Maine Revenue Services) | 2026 booklet (rev. Dec 2025). Do not reduce for federal W-4 Step 4(b) deductions. |
| `me.wh.allowance.annual` | [[FACT:me.wh.allowance.annual=5300]] USD | 2026-01-01 | 2026-12-31 | US-MES5-011 (A.2, Maine Revenue Services) |  |
| `me.wh.std_deduction.single` | [[FACT:me.wh.std_deduction.single=12450]] USD | 2026-01-01 | 2026-12-31 | US-MES5-011 (A.2, Maine Revenue Services) | Full amount if annual wages are at or below [[FACT:me.wh.std_deduction.single.phaseout_start=102,250]]; otherwise [[FACT:me.wh.std_deduction.single=12,450]] x ([[FACT:me.wh.std_deduction.single.phaseout_end=177,250]] - W) / 75,000; zero from [[FACT:me.wh.std_deduction.single.phaseout_end=177,250]]. This is the withholding figure, not the return-level standard deduction. |
| `me.wh.std_deduction.married` | [[FACT:me.wh.std_deduction.married=27750]] USD | 2026-01-01 | 2026-12-31 | US-MES5-011 (A.2, Maine Revenue Services) | If wages <= 204,550; else [[FACT:me.wh.std_deduction.married=27,750]] x (354,550 - W) / 150,000; zero from 354,550. |
| `me.wh.std_deduction.single.phaseout_start` | [[FACT:me.wh.std_deduction.single.phaseout_start=102250]] USD | 2026-01-01 | 2026-12-31 | US-MES5-011 (A.2, Maine Revenue Services) |  |
| `me.wh.std_deduction.single.phaseout_end` | [[FACT:me.wh.std_deduction.single.phaseout_end=177250]] USD | 2026-01-01 | 2026-12-31 | US-MES5-011 (A.2, Maine Revenue Services) |  |
| `me.wh.bracket.married.1.ceiling` | [[FACT:me.wh.bracket.married.1.ceiling=54850]] USD | 2026-01-01 | 2026-12-31 | US-MES5-011 (A.2, Maine Revenue Services) | 5.80% below [[FACT:me.wh.bracket.married.1.ceiling=54,850]]; 3,181 + 6.75% to [[FACT:me.wh.bracket.married.2.ceiling=129,750]]; 8,237 + 7.15% above. |
| `me.wh.bracket.married.2.ceiling` | [[FACT:me.wh.bracket.married.2.ceiling=129750]] USD | 2026-01-01 | 2026-12-31 | US-MES5-011 (A.2, Maine Revenue Services) |  |
| `me.wh.bracket.1.rate` | [[FACT:me.wh.bracket.1.rate=5.8]] percent | 2026-01-01 | 2026-12-31 | US-MES5-011 (A.2, Maine Revenue Services) |  |
| `me.wh.bracket.2.rate` | [[FACT:me.wh.bracket.2.rate=6.75]] percent | 2026-01-01 | 2026-12-31 | US-MES5-011 (A.2, Maine Revenue Services) |  |
| `me.wh.bracket.3.rate` | [[FACT:me.wh.bracket.3.rate=7.15]] percent | 2026-01-01 | 2026-12-31 | US-MES5-011 (A.2, Maine Revenue Services) |  |
| `me.wh.supplemental.rate` | [[FACT:me.wh.supplemental.rate=5]] percent | 2026-01-01 | open | US-MES5-011 (A.2, Maine Revenue Services) | Aggregated or flat 5% when paid separately; backup withholding 5%. |
| `me.wh.certificate` | [[FACT:me.wh.certificate=W-4ME required; none valid = single, zero allowances; more allowances need MRS Allowance Variance Certificate; copy to MRS when IRS demands W-4 or non-Maine-address exempt claimant expects >= 5,000 Maine-source pay]] | 2026-01-01 | open | US-MES5-011 (A.2, Maine Revenue Services) |  |
| `me.oracle.booklet.examples_weekly` | [[FACT:me.oracle.booklet.examples_weekly=0 / 33 / 257]] | 2026-01-01 | 2026-12-31 | US-MES5-011 (A.2, Maine Revenue Services) | Booklet Examples 1-3 reproduced (weekly, rounded to dollar). No official calculator [US-MEP52-009]. |
| `me.wh.bracket.single.1.ceiling` | [[FACT:me.wh.bracket.single.1.ceiling=27400]] USD | 2026-01-01 | 2026-12-31 | US-MEP52-001 (A.2, Maine Revenue Services) | Single: 5.80% below [[FACT:me.wh.bracket.single.1.ceiling=27,400]]; 1,589 + 6.75% to [[FACT:me.wh.bracket.single.2.ceiling=64,850]]; 4,117 + 7.15% above. Use the withholding standard deduction ([[FACT:me.wh.std_deduction.single=12,450]] single / [[FACT:me.wh.std_deduction.married=27,750]] married), not the return-level amounts. |
| `me.wh.bracket.single.2.ceiling` | [[FACT:me.wh.bracket.single.2.ceiling=64850]] USD | 2026-01-01 | 2026-12-31 | US-MEP52-001 (A.2, Maine Revenue Services) |  |

- ⚠️ RESEARCH-GAP (non-blocking, `me.pit.obbba_decoupling`): Decoupling from federal tips/overtime deductions for 2026 not checked (assessment). To close: 2026 MRS individual instructions or the conformity act.
- ⚠️ RESEARCH-GAP (non-blocking, `me.wh.tables.next_year`): 2027 withholding tables not published. To close: MRS 27_wh_tab_instr.pdf (December 2026).

## ME.5 Non-residents, residents working elsewhere and reciprocity

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `me.nonres.threshold` | [[FACT:me.nonres.threshold=taxable only if present in Maine more than 12 days AND more than 3,000 Maine-source pay in the year (training, inspection, R&D, project-team days excluded)]] | 2026-01-01 | open | US-MES5-011 (A.2, Maine Revenue Services) | Rule on US-MEP52-003; resident credit [US-MEP52-004]; no reciprocity in force [US-MEP52-005]. |

## ME.6 Local wage taxes

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `me.local_wage_tax.exists` | [[FACT:me.local_wage_tax.exists=False]] | 2026-01-01 | open | US-MER3-001 (A.1, Maine Legislature, Office of the Revisor of Statutes) | [US-MER3-002]. |

## ME.7 Unemployment insurance, disability and paid-leave contributions, other payroll levies

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `me.sui.wage_base` | [[FACT:me.sui.wage_base=12000]] USD | 2026-01-01 | open | US-MES5-020 (A.1, Maine Legislature, Office of the Revisor of Statutes) | Fixed, not indexed; other-state wages by same legal entity and predecessor wages count (26 MRSA 1043(19)); non-cash remuneration at cash value. |
| `me.pfml.rate.total.15_plus` | [[FACT:me.pfml.rate.total.15_plus=1.0]] percent | 2025-01-01 | 2027-12-31 | US-MEP6-001 (A.3, Maine Department of Labor, Paid Family and Medical Leave) | Authority FAQ plus the statutory ceiling [US-MES5-024]: employers with 15 or more employees remit the total rate, of which the employee bears at most [[FACT:me.pfml.employee.max_rate=0.5]] percent; employers with fewer than 15 remit [[FACT:me.pfml.rate.total.under_15=0.5]] percent, all deductible from the employee. From 2028 the department sets the rate by October 1. Wages capped at the Social Security wage base; the employee share is deducted after tax; an employee share paid by the employer is taxable wages; Form W-2 box 14 label 'MEPFML'; late payment 1% of quarterly payroll; coverage follows unemployment-insurance localization. |
| `me.pfml.rate.total.under_15` | [[FACT:me.pfml.rate.total.under_15=0.5]] percent | 2025-01-01 | 2027-12-31 | US-MEP6-001 (A.3, Maine Department of Labor, Paid Family and Medical Leave) |  |
| `me.pfml.employee.max_rate` | [[FACT:me.pfml.employee.max_rate=0.5]] percent | 2025-01-01 | 2027-12-31 | US-MEP6-001 (A.3, Maine Department of Labor, Paid Family and Medical Leave) |  |
| `me.pfml.employee_deduction.after_tax` | [[FACT:me.pfml.employee_deduction.after_tax=True]] | 2025-01-01 | open | US-MES5-025 (A.3, Maine Department of Labor, Paid Family and Medical Leave) |  |
| `me.pfml.w2_box14_label` | [[FACT:me.pfml.w2_box14_label=MEPFML]] | 2025-01-01 | open | US-MES5-025 (A.3, Maine Department of Labor, Paid Family and Medical Leave) |  |
| `me.sui.new_employer.rate.total` | [[FACT:me.sui.new_employer.rate.total=2.54]] percent | 2026-01-01 | 2026-12-31 | US-MEP51-001 (A.2, Maine Department of Labor, Bureau of Unemployment Compensation) | 2.23% UI + 0.14% CSSF + 0.17% UPAF (UPAF conflict vs UC-1 0.16%, Q1). |
| `me.sui.employer.rate.combined.range` | [[FACT:me.sui.employer.rate.combined.range=0.31% - 6.60% (categories 01-20; adjusted UI 0.00%-6.29%)]] | 2026-01-01 | 2026-12-31 | US-MEP51-001 (A.2, Maine Department of Labor, Bureau of Unemployment Compensation) |  |

- ⚠️ RESEARCH-GAP (blocking, `me.sui.upaf.rate.conflict`): The 2026 rate-year table and the 2026 Form UC-1 instructions give different rates for the Unemployment Program Administrative Fund component. The component rate is not written, and the combined new-employer rate that includes it is unconfirmed. To close: An employer 2026 MDOL rate notice or MDOL BUC confirmation of the 2026 UPAF predetermined yield.
- ⚠️ RESEARCH-GAP (non-blocking, `me.pfml.rate.a2_source`): The split of the total rate by employer size rests on the authority FAQ and the statutory ceiling; no authority rate table was found. To close: 12-702 CMR ch. 1 contributions section or an MDOL 2026 rate notice.

## ME.8 Pay statement

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `me.payslip.required` | [[FACT:me.payslip.required=True]] | 2026-01-01 | open | US-MES5-006 (A.1, Maine Legislature, Office of the Revisor of Statutes) | 26 MRSA 665(1): with each payment: pay-period date, hours, total earnings, itemized deductions; same record at time of electronic transfer; electronic only with ready access and free printing. CORRECTS US-MEP51-004 / US-MEP52-006 (superseded). |
| `me.payslip.items` | [[FACT:me.payslip.items=date of the pay period, hours, total earnings, itemized deductions]] | 2026-01-01 | open | US-MES5-006 (A.1, Maine Legislature, Office of the Revisor of Statutes) |  |

## ME.9 Statutory reporting

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `me.report.wh.941me` | [[FACT:me.report.wh.941me=quarterly, due last day of month after quarter; electronic mandatory (Rule 104) even if nothing to report; deposits semiweekly if look-back >= 18,000 else quarterly; 900ME voucher; no W-3ME after TY2023]] | 2026-01-01 | open | US-MES5-011 (A.2, Maine Revenue Services) |  |
| `me.report.w2` | [[FACT:me.report.w2=electronic with MRS by 31 January, paper not accepted; Maine Tax Portal Bulk File Upload Specifications (EFW2 acceptance open); 50 per missing statement]] | 2026-01-01 | open | US-MES5-011 (A.2, Maine Revenue Services) |  |
| `me.report.sui.uc1` | [[FACT:me.report.sui.uc1=ME UC-1 quarterly, last day of month after quarter, via ReEmployME (file spec published) or paper, filed with MRS; monthly employment (12th), gross/excess/taxable wages, UC rate, CSSF, UPAF; interest 10% from 2026-01-01]] | 2026-01-01 | open | US-MES5-021 (A.2, Maine Department of Labor, Bureau of Unemployment Compensation) |  |
| `me.newhire.report_days` | [[FACT:me.newhire.report_days=7]] days | 2026-01-01 | open | US-MES5-016 (A.1, Maine Legislature, Office of the Revisor of Statutes) | To DHHS within 7 days of first services (stricter than federal 20); rehires after 60+ days; DOB; employer UI/UBI number; independent contractors expected >= 2,500 also within 7 days. |
| `me.newhire.contractor_threshold` | [[FACT:me.newhire.contractor_threshold=2500]] USD | 2026-01-01 | open | US-MES5-016 (A.1, Maine Legislature, Office of the Revisor of Statutes) |  |
| `me.report.wh.semiweekly_threshold` | [[FACT:me.report.wh.semiweekly_threshold=18000]] USD | 2026-01-01 | open | US-MEP52-002 (A.2, Maine Revenue Services) | Look-back 12 months to prior 30 June; semiweekly Wed-Fri -> Wednesday, Sat-Tue -> Friday; electronic payment if combined Maine tax >= 10,000. |

- ⚠️ RESEARCH-GAP (non-blocking, `me.report.w2.bulk_spec`): Maine Tax Portal Bulk File Upload Specifications not fetched (EFW2 acceptance open). To close: MRS bulk file specifications.

## ME.10 Leave

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `me.leave.earned_paid.employer_threshold` | [[FACT:me.leave.earned_paid.employer_threshold=10]] employees | 2026-01-01 | open | US-MES5-008 (A.1, Maine Legislature, Office of the Revisor of Statutes) | 26 MRSA 637: MORE than 10 employees for > 120 days; 1 h per 40 h up to 40 h/yr, any purpose; use after 120 days; carryover (PL 2025 c.438 does not reduce next year accrual); base rate; seasonal excluded; local ordinances pre-empted. |
| `me.leave.earned_paid.accrual.hours_worked_per_hour` | [[FACT:me.leave.earned_paid.accrual.hours_worked_per_hour=40]] hours | 2026-01-01 | open | US-MES5-008 (A.1, Maine Legislature, Office of the Revisor of Statutes) |  |
| `me.leave.earned_paid.cap_hours` | [[FACT:me.leave.earned_paid.cap_hours=40]] hours | 2026-01-01 | open | US-MES5-008 (A.1, Maine Legislature, Office of the Revisor of Statutes) |  |

- ⚠️ RESEARCH-GAP (non-blocking, `me.leave.earned_paid.payout`): Payout of earned paid leave at separation is an interpretation via 626. To close: MDOL rule 12-170 CMR ch. 18 or FAQ.

## ME.11 Termination and final pay

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `me.final_pay.rule` | [[FACT:me.final_pay.rule=no later than next established payday (discharge or resignation); on demand earlier of next payday or 2 weeks; accrued vacation from 2023-01-01 payable (not employers with <= 10 employees or public; CBA overrides); liquidated damages 2x]] | 2026-01-01 | open | US-MES5-007 (A.1, Maine Legislature, Office of the Revisor of Statutes) |  |
| `me.severance.mass_layoff` | [[FACT:me.severance.mass_layoff=establishments with 100+ employees: one week pay per year of service, within one pay period after last day; 90 days notice]] | 2026-01-01 | open | US-MES5-010 (A.1, Maine Legislature, Office of the Revisor of Statutes) |  |

Rules:

- Separating employees receive the Employment Security Law notice (poster copy). Deductions from final pay: overcompensation and signed loans/advances. (US-MES5-021, US-MES5-007)

## ME.12 Taxable wages and benefits in kind

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `me.pit.conformity_date` | [[FACT:me.pit.conformity_date=2025-12-31 (fixed); no additions for HSA, 125, transit, 401(k) (36 MRSA 5122) - federal exclusions followed]] | 2026-01-01 | open | US-MES5-018 (A.1, Maine Legislature, Office of the Revisor of Statutes) | [US-MES5-027]. |

## ME.13 Deductions and garnishments

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `me.garn.creditor.rule` | [[FACT:me.garn.creditor.rule=least of 25% of disposable, excess over 40 x higher of federal/State MW, or the total]] | 2026-01-01 | open | US-MES5-013 (A.1, Maine Legislature, Office of the Revisor of Statutes) |  |
| `me.garn.creditor.weekly_protected` | [[FACT:me.garn.creditor.weekly_protected=604.0]] USD | 2026-01-01 | 2026-12-31 | US-MES5-013 (A.1, Maine Legislature, Office of the Revisor of Statutes) | 40 x [[FACT:me.minwage.hourly=15.10]]. |
| `me.garn.employer_fee_per_check` | [[FACT:me.garn.employer_fee_per_check=1]] USD | 2026-01-01 | open | US-MES5-014 (A.1, Maine Legislature, Office of the Revisor of Statutes) | Answer within 20 days; no discharge. |
| `me.garn.child_support.remit_business_days` | [[FACT:me.garn.child_support.remit_business_days=7]] business days | 2026-01-01 | open | US-MES5-015 (A.1, Maine Legislature, Office of the Revisor of Statutes) | Order adds 2/week; priority over non-support; processing fee only by DHHS rule. |

- ⚠️ RESEARCH-GAP (non-blocking, `me.deductions.authorisation`): 26 MRSA 629/635 not read. To close: Statute read.

## ME.14 Prevailing wage and collective agreements

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `me.prevailing_wage.threshold` | [[FACT:me.prevailing_wage.threshold=50000]] USD | 2026-01-01 | open | US-MES5-017 (A.1, Maine Legislature, Office of the Revisor of Statutes) | State-funded public works >= 50,000 (< 10,000 never construction); energy projects >= 2 MW; certified payroll filed monthly; records 3 years; fine >= 250/employee/day. |

## ME.15 Indexation

Indexation of each value is stated in the note of the value concerned.

## ME.16 Payroll data protection and records

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `me.records.retention_years` | [[FACT:me.records.retention_years=3]] years | 2026-01-01 | open | US-MES5-006 (A.1, Maine Legislature, Office of the Revisor of Statutes) | 665(1); 622 date/amount and daily time records except salaried exempt [US-MES5-026]. SSN not requestable on applications [US-MES5-009]. |

- ⚠️ RESEARCH-GAP (non-blocking, `me.data_protection.breach_ssn`): SSN on pay statements and breach law not read. To close: 10 MRSA 1346-1350-B and 1272-B.

## ME.17 Legal change in force or enacted

No Maine rule is configured in this domain; the federal treatment in Annex FED applies.

## ME.18 Special populations

- Domestic: no MW exclusion found. (US-MES5-020, US-MES5-005)
- Minors: full MW. (US-MES5-028, US-MES5-020)
- Clergy: UI-excluded; no withholding rule beyond federal. (US-MES5-020)
- Students: co-op/OJT, student nurses/interns UI-excluded; camp counselors MW-subchapter excluded. (US-MES5-020, US-MES5-005)
- Government: most public employees OT-exempt; public employers exempt from vacation payout. (US-MES5-005, US-MES5-007, US-MES5-024)
- Family members dependent on employer: own child/spouse UI-excluded. (US-MES5-005, US-MES5-020)
- ⚠️ RESEARCH-GAP (non-blocking, `me.special_populations.thresholds`): thresholds, amounts or conditions for these populations are stated in the research without a confirmed value record and are not configured from this annex: Domestic; Agricultural; Minors; Tipped; NRAs; Government; Family members dependent on employer; Small employers. To close: one confirmed value per threshold, with its source row.

## ME.19 Language

- The pay statement and all filings are in English (owner decision US-OWN-006).

## ME.20 Sources

| Source | Authority |
|---|---|
| US-MEP51-001 | Maine Department of Labor, Bureau of Unemployment Compensation |
| US-MEP52-001 | Maine Revenue Services |
| US-MEP52-002 | Maine Revenue Services |
| US-MEP6-001 | Maine Department of Labor, Paid Family and Medical Leave |
| US-MER3-001 | Maine Legislature, Office of the Revisor of Statutes |
| US-MES5-001 | Maine Legislature, Office of the Revisor of Statutes |
| US-MES5-002 | Maine Department of Labor, Bureau of Labor Standards |
| US-MES5-003 | Maine Department of Labor, Bureau of Labor Standards |
| US-MES5-004 | Maine Legislature, Office of the Revisor of Statutes |
| US-MES5-006 | Maine Legislature, Office of the Revisor of Statutes |
| US-MES5-007 | Maine Legislature, Office of the Revisor of Statutes |
| US-MES5-008 | Maine Legislature, Office of the Revisor of Statutes |
| US-MES5-010 | Maine Legislature, Office of the Revisor of Statutes |
| US-MES5-011 | Maine Revenue Services |
| US-MES5-012 | City of Portland, Maine |
| US-MES5-013 | Maine Legislature, Office of the Revisor of Statutes |
| US-MES5-014 | Maine Legislature, Office of the Revisor of Statutes |
| US-MES5-015 | Maine Legislature, Office of the Revisor of Statutes |
| US-MES5-016 | Maine Legislature, Office of the Revisor of Statutes |
| US-MES5-017 | Maine Legislature, Office of the Revisor of Statutes |
| US-MES5-018 | Maine Legislature, Office of the Revisor of Statutes |
| US-MES5-020 | Maine Legislature, Office of the Revisor of Statutes |
| US-MES5-021 | Maine Department of Labor, Bureau of Unemployment Compensation |
| US-MES5-025 | Maine Department of Labor, Paid Family and Medical Leave |
