## @labour
- **Minimum wage (Labor Code 62.051) [US-TXS5-002]:** the state rate is the federal FLSA rate (follows federal: {{tx.labour.minwage.state.follows_federal}}); the figure is in Annex FED. No 2027 change enacted. The state rule overrides local wage ordinances for private employment (62.0515): {{tx.local_mandates.preempted}}.
- **Scope trap:** chapter 62 does not apply to persons covered by the FLSA (62.151); in practice it covers employees outside FLSA coverage. Exemptions in 62.152-62.160.
- **Overtime:** {{tx.labour.overtime.state_rule}} [US-TXS5-002, US-TXS5-004].
- **Tipped:** "tipped" means more than {{tx.labour.tip_credit.monthly_tip_threshold}} USD a month in tips (62.052); cash wage per FLSA 3(m) [US-TXS5-002].
- **Pay frequency (61.011-61.012) [US-TXS5-004]:** {{tx.pay_frequency.rule}}; paydays must be posted.
- **Method of payment (61.016-61.017) [US-TXS5-004]:** cash, negotiable instrument, EFT to an employee-designated account, or payroll card. The employer may elect direct deposit with {{tx.labour.direct_deposit.notice_days}} days' written notice; payroll cards need the same notice period (or notice by the first day of work for new hires), a fee list and an opt-out. Wages in kind need written agreement.
- **Child labour:** minimum age {{tx.labour.child_labour.min_age}}; daily and weekly hour limits and night bans for the youngest workers (51.011, 51.013) [US-TXS5-006].

## @income_tax
- **No state income tax** (exists: {{tx.pit.exists}}): Const. Art. VIII s.24-a bars a tax on individuals' net incomes; s.24-b (2025) also bars a capital gains tax. No state withholding, W-4, supplemental rate, rounding rule, state W-2 or reciprocity [US-TXS5-001].
- **No local wage tax** (exists: {{tx.local_wage_tax.exists}}) [US-TXP52-001].
- **Resident and nonresident matrix.** Nothing is withheld for Texas for any income type; a Texas resident working in another state is withheld under that state's rules, and a Texas employer with out-of-state workers follows the work state (Annex MULTI).

## @social
- **Unemployment insurance (TWC) [US-TXS5-007, US-TXSUI-001].** Taxable wage base {{tx.sui.wage_base}} USD per employee per calendar year, fixed by statute (201.082(1)), not indexed. 2026 rates {{tx.sui.employer.rate.min}} % to {{tx.sui.employer.rate.max}} %, including the obligation assessment of {{tx.ui.obligation_assessment.rate}} % [US-TXS5-019]. New employer {{tx.sui.new_employer.rate}} % for the first six calendar quarters (statute: the greater of the major-group rate less a fixed step, or a statutory floor, 204.006); the published rate cannot be re-derived without the major-group rates (open point below) [US-TXS5-008, US-TXS5-019].
- **Employee contribution:** {{tx.sui.employee.rate}} %; deduction from wages prohibited (204.003) [US-TXS5-008].
- **Employment and Training Investment Assessment:** {{tx.ui.etia.rate}} % of taxable wages, employer-paid, offset by an equal cut in the replenishment rate (204.121, 204.0625) [US-TXS5-008].
- **UI wages (201.081-201.082):** include non-cash pay and FUTA-taxable tips; exclude employer plan payments for retirement, sickness, medical or death benefits and employer-paid FICA. [US-TXS5-007]. Employee deferrals and cafeteria-plan reductions: {{tx.ui.wages.401k_section125}} [US-TXV6-004].
- **Coverage:** quarterly wage or 20-week tests; domestic employers above a quarterly cash test with an annual-reporting option (201.027); farm and ranch labour per 201.028 / 201.047 [US-TXS5-007].
- **No SDI, TDI, PFML or LTC** (exists: {{tx.sdi_pfml.exists}}) [US-TXR3-003].

## @payslip
- **Labor Code 62.003 (earnings statement) exists, for employees outside FLSA coverage only [US-TXS5-003].** At the end of each pay period: {{tx.payslip.content.non_flsa}}; any form, including the check voucher; meals or lodging credited toward the wage stated separately (62.053). For FLSA-covered employees Texas has no statutory content rule (federal records rules apply). Never write "Texas has no pay-statement law".
- **Electronic delivery and retention:** no Texas rule in chapters 61 or 62; retention follows FLSA and UI record rules (the TWC records-retention rule was not read).

## @reporting
- **No withholding return or state W-2.**
- **Quarterly UI wage report and payment [US-TXSUI-006]:** {{tx.report.ui.channel}}. Due dates: {{tx.report.ui.due_date_records}} [US-TXV6-001].
- **Enhanced wage-report content (Labor Code 204.0025, 2025 amendments) [US-TXS5-008]:** {{tx.report.ui.enhanced_fields}}. Status: {{tx.report.ui.enhanced_fields.status}} [US-TXV6-005]. Proposed only: these fields are not configured as mandatory (open point below).
- **New hire [US-TXS5-012, US-TXS5-016, US-TXS5-017]:** to the OAG Child Support Division state directory within {{tx.newhire.report_days}} calendar days of the first day of work, or twice monthly for electronic reporters. Who is reported: {{tx.report.new_hire.contractors}} [US-TXV6-002]; independent contractors are out of scope for this guide (US-OWN-008).
- **Registration:** TWC UI account once the coverage thresholds are met; agent authorisation Form C-42 [US-TXSUI-005, US-TXP52-008].

## @leave
- **Paid sick leave:** no state statute (exists: {{tx.leave.sick.state_statute.exists}}); Labor Code 1.005 (H.B. 2127, 2023) preempts city and county leave, benefit and scheduling ordinances for private employers [US-TXS5-005]. No PFML.
- **Leave pay is wages only if promised in writing** (61.001(7)(B)) [US-TXS5-004].
- **Voting time (Election Code 276.004):** paid ({{tx.leave.voting.paid}}): no penalty, including lost wages, for time off to vote, unless the polls are open long enough outside working hours [US-TXS5-014]. Jury and military leave: {{tx.leave.jury_military}} [US-TXV6-003].

## @termination
- **Final pay (61.014) [US-TXS5-004]:** a discharged employee is paid within {{tx.term.final_pay.discharge.days}} calendar days of discharge; any other separation: {{tx.term.final_pay.other}}. Commissions and bonuses follow the agreement (61.015).
- **Accrued vacation:** {{tx.term.vacation.payout}} [US-TXS5-004, US-TXS5-018].
- **Child-support interaction (FC 158.215, 158.214) [US-TXS5-011]:** with a IV-D administrative writ, notify the OAG before any lump-sum payment of {{tx.garn.iwo.lump_sum.threshold}} USD or more and hold it for the statutory period; severance is withheld as usual earnings within the cap.
- No state separation notice or mini-WARN found.

## @bik
- **No income tax;** conformity matters only for the UI wage definition (Section 3) [US-TXS5-007].

## @deductions
- **Wage deductions (61.018):** only by court order, by law, or with written authorisation for a lawful purpose [US-TXS5-004].
- **Garnishment (Const. Art. XVI s.28; CPRC 63.004) [US-TXS5-009, US-TXS5-010]:** current wages are exempt except for child support and spousal maintenance; creditor wage garnishment available: {{tx.garn.consumer.available}}. Federal tax levies and federal administrative garnishments apply by federal law.
- **Child-support IWO [US-TXS5-011]:** cap {{tx.garn.iwo.max_rate}} % of disposable earnings (158.009); start by the first pay period after delivery; remit to the SDU on each pay date (larger employers electronically); employer fee up to {{tx.garn.iwo.employer_fee.monthly}} USD per month (158.204); multiple orders split equally, current support first; notify termination within {{tx.garn.iwo.termination_notice_days}} days (158.211).

## @cba
- **Prevailing wage (Gov. Code ch. 2258) [US-TXR3-002, US-TXS5-015]:** public works; the public body sets the rate (survey or Davis-Bacon); penalty {{tx.prevailing_wage.penalty.per_worker_day}} USD per worker per day; records of name, occupation and per diem wage; no state certified-payroll form.

## @indexation
- **Nothing is indexed by state law:** minimum wage follows the FLSA; the UI wage base is statutory; UI rates are recomputed by TWC each year and mailed in December; 2027 rates not yet published (open point below).

## @data
- **Business and Commerce Code 501.001 [US-TXS5-013]:** no public display of SSNs, no SSN on access cards, no unsecured transmission, no SSN on mailed material unless law requires it ({{tx.data.ssn.mailed_prohibited}}). No pay-statement truncation rule: a mailed paper payslip should not show the full SSN.

## @live
- **Const. Art. VIII s.24-b (approved 2025-11-04):** capital gains tax ban; no payroll effect [US-TXS5-001].
- **Labor Code 204.0025:** enhanced wage-filing data; payroll and DD impact depends on TWC implementation (open point below) [US-TXS5-008].
- **2027 TWC rates** due December 2026; not swept (TWC site blocked).

## @special
| Population | Texas rule | Register id |
|---|---|---|
| Domestic / household | UI above a quarterly cash test with annual-reporting option (201.027); exempt from the state minimum wage (62.154), FLSA may apply | US-TXS5-007, US-TXS5-002 |
| Agricultural | UI for farm and ranch labour (201.028 / 201.047); H-2A excluded unless FUTA covers them (201.078); chapter 62 dairy and livestock exemptions | US-TXS5-007, US-TXS5-002 |
| Minors | Minimum age and hour limits (Section 1); minor non-graduates exempt from the state minimum wage (62.155) | US-TXS5-006, US-TXS5-002 |
| Tipped | Tip threshold per Section 1; UI wages include FUTA-taxable tips | US-TXS5-002, US-TXS5-007 |
| Clergy / religious | Excluded from UI (201.066) and from chapter 62 (62.152) | US-TXS5-007, US-TXS5-002 |
| Students | Excluded from UI for own-school, credit co-op and some camp work (201.069); student minimum-wage exemption (62.155) | US-TXS5-007, US-TXS5-002 |
| Nonresident aliens | No state income tax; only the UI H-2A exclusion | US-TXS5-001, US-TXS5-007 |
| Statutory employees | UI employment includes certain drivers and salespersons (201.042) | US-TXS5-007 |
| Government employees | State and political subdivisions are UI employers (201.026); elected officials exempt from chapter 62 | US-TXS5-007, US-TXS5-002 |

## @gaps
- tx.ui.rate.new_employer.derivation :: The published new-employer rate cannot be re-derived without the 2026 major-group rates. :: TWC rate notice or "how your 2026 tax rate was calculated" page.
- tx.ui.wages.401k_section125 :: TWC treatment of employee retirement deferrals and cafeteria-plan reductions was not read (201.082 is silent). :: 40 TAC ch. 815 wage definition or TWC guidance.
- tx.report.ui.enhanced_fields_layout :: Which Labor Code 204.0025 fields are mandatory on the quarterly wage report, and from which quarter, is unknown. :: TWC wage-report file specification or the adopted TWC rule.
