# Annex TX: Texas


Jurisdiction annex of the United States Country Configuration Guide (US-CCG-001). Layer classification: **T1 - no state wage tax; SUI and levies only** (build manifest, tier rationale).

The federal layer (federal income tax withholding, FICA, FUTA, Forms W-2, 941 and 940) and the multistate rules (residence and work-location sourcing, reciprocity mechanics) are in Annex FED and Annex MULTI and are not repeated here. Independent contractors and Form 1099-NEC reporting are out of scope (owner instruction of 2026-10-29) [US-OWN-008]. Payslip language: English; second-language duties attach to notices and posters only (US-OWN-006).

Every value in this annex is bound to a verified fact and carries its legal-basis register id. A value that changes during the year is shown with its effective dates. A point marked as a research gap has not been closed by the research; it is not filled with an estimate.

## TX.1 Employment and labour code

- **Minimum wage (Labor Code 62.051) [US-TXS5-002]:** the state rate is the federal FLSA rate (follows federal: [[FACT:tx.labour.minwage.state.follows_federal=True]]); the figure is in Annex FED. No 2027 change enacted. The state rule overrides local wage ordinances for private employment (62.0515): [[FACT:tx.local_mandates.preempted=True]].
- **Scope trap:** chapter 62 does not apply to persons covered by the FLSA (62.151); in practice it covers employees outside FLSA coverage. Exemptions in 62.152-62.160.
- **Overtime:** [[FACT:tx.labour.overtime.state_rule=none (FLSA only)]] [US-TXS5-002, US-TXS5-004].
- **Tipped:** "tipped" means more than [[FACT:tx.labour.tip_credit.monthly_tip_threshold=20]] USD a month in tips (62.052); cash wage per FLSA 3(m) [US-TXS5-002].
- **Pay frequency (61.011-61.012) [US-TXS5-004]:** [[FACT:tx.pay_frequency.rule=FLSA-exempt at least monthly; others at least twice a month (default 1st and 15th)]]; paydays must be posted.
- **Method of payment (61.016-61.017) [US-TXS5-004]:** cash, negotiable instrument, EFT to an employee-designated account, or payroll card. The employer may elect direct deposit with [[FACT:tx.labour.direct_deposit.notice_days=60]] days' written notice; payroll cards need the same notice period (or notice by the first day of work for new hires), a fee list and an opt-out. Wages in kind need written agreement.
- **Child labour:** minimum age [[FACT:tx.labour.child_labour.min_age=14]]; daily and weekly hour limits and night bans for the youngest workers (51.011, 51.013) [US-TXS5-006].

**Parameters (labour code and pay rules)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `tx.labour.minwage.state.follows_federal` | [[FACT:tx.labour.minwage.state.follows_federal=True]] |  | from 2003-09-01 | US-TXS5-002 |  |
| `tx.local_mandates.preempted` | [[FACT:tx.local_mandates.preempted=True]] |  | from 2003-09-01 | US-TXS5-002 | 62.0515 except public contracts |
| `tx.labour.overtime.state_rule` | [[FACT:tx.labour.overtime.state_rule=none (FLSA only)]] |  | from 2003-09-01 | US-TXS5-002 |  |
| `tx.pay_frequency.rule` | [[FACT:tx.pay_frequency.rule=FLSA-exempt at least monthly; others at least twice a month (default 1st and 15th)]] |  | from 2026-01-01 | US-TXS5-004 | 61.011-61.012 |
| `tx.labour.direct_deposit.notice_days` | [[FACT:tx.labour.direct_deposit.notice_days=60]] | days | from 2026-01-01 | US-TXS5-004 | employer may elect EFT with 60 days notice; payroll card with fee list and opt-out (61.017) |
| `tx.labour.tip_credit.monthly_tip_threshold` | [[FACT:tx.labour.tip_credit.monthly_tip_threshold=20]] | USD | from 2003-09-01 | US-TXS5-002 | tipped = >20/month (62.052); cash wage per FLSA 3(m) |
| `tx.labour.child_labour.min_age` | [[FACT:tx.labour.child_labour.min_age=14]] | years | from 2026-01-01 | US-TXS5-006 | 14-15: 8 h/day, 48 h/week |

## TX.2 Income tax withholding

- **No state income tax** (exists: [[FACT:tx.pit.exists=False]]): Const. Art. VIII s.24-a bars a tax on individuals' net incomes; s.24-b (2025) also bars a capital gains tax. No state withholding, W-4, supplemental rate, rounding rule, state W-2 or reciprocity [US-TXS5-001].
- **No local wage tax** (exists: [[FACT:tx.local_wage_tax.exists=False]]) [US-TXP52-001].
- **Resident and nonresident matrix.** Nothing is withheld for Texas for any income type; a Texas resident working in another state is withheld under that state's rules, and a Texas employer with out-of-state workers follows the work state (Annex MULTI).

**Parameters (income tax withholding (state and local))**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `tx.pit.exists` | [[FACT:tx.pit.exists=False]] |  | from 2019-11-05 | US-TXS5-001 | Const. Art. VIII s.24-a. |
| `tx.local_wage_tax.exists` | [[FACT:tx.local_wage_tax.exists=False]] |  | from 2026-01-01 | US-TXP52-001 |  |

## TX.2b Non-resident regime and reciprocity

The non-resident and reciprocity rules of this jurisdiction are written in TX.2.

## TX.2c Local wage taxes

The local wage taxes of this jurisdiction, where any exist, are written in TX.2.

## TX.3 Social insurance: unemployment, disability, paid leave and payroll levies

- **Unemployment insurance (TWC) [US-TXS5-007, US-TXSUI-001].** Taxable wage base [[FACT:tx.sui.wage_base=9000]] USD per employee per calendar year, fixed by statute (201.082(1)), not indexed. 2026 rates [[FACT:tx.sui.employer.rate.min=0.32]] % to [[FACT:tx.sui.employer.rate.max=6.32]] %, including the obligation assessment of [[FACT:tx.ui.obligation_assessment.rate=0.01]] % [US-TXS5-019]. New employer [[FACT:tx.sui.new_employer.rate=2.7]] % for the first six calendar quarters (statute: the greater of the major-group rate less a fixed step, or a statutory floor, 204.006); the published rate cannot be re-derived without the major-group rates (open point below) [US-TXS5-008, US-TXS5-019].
- **Employee contribution:** [[FACT:tx.sui.employee.rate=0]] %; deduction from wages prohibited (204.003) [US-TXS5-008].
- **Employment and Training Investment Assessment:** [[FACT:tx.ui.etia.rate=0.1]] % of taxable wages, employer-paid, offset by an equal cut in the replenishment rate (204.121, 204.0625) [US-TXS5-008].
- **UI wages (201.081-201.082):** include non-cash pay and FUTA-taxable tips; exclude employer plan payments for retirement, sickness, medical or death benefits and employer-paid FICA. [US-TXS5-007]. Employee deferrals and cafeteria-plan reductions: [[FACT:tx.ui.wages.401k_section125=Wages = all remuneration for personal services (201.081); 201.082 exceptions read in full contain no exclusion for employee elective 401(k) deferrals or IRC s.125 reductions (only payments to/from exempt 401(a) trusts); TWC guidance not obtained]] [[GAP:RQ-339]] [US-TXV6-004].
- **Coverage:** quarterly wage or 20-week tests; domestic employers above a quarterly cash test with an annual-reporting option (201.027); farm and ranch labour per 201.028 / 201.047 [US-TXS5-007].
- **No SDI, TDI, PFML or LTC** (exists: [[FACT:tx.sdi_pfml.exists=False]]) [US-TXR3-003].

**Parameters (social insurance and payroll levies)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `tx.sui.wage_base` | [[FACT:tx.sui.wage_base=9000]] | USD | from 2026-01-01 | US-TXS5-007 | 201.082(1), not indexed; second document family US-TXSUI-001 |
| `tx.ui.obligation_assessment.rate` | [[FACT:tx.ui.obligation_assessment.rate=0.01]] | % | 2026-01-01 to 2026-12-31 | US-TXS5-019 | deficit 0.00 |
| `tx.sui.new_employer.rate` | [[FACT:tx.sui.new_employer.rate=2.7]] | % | 2026-01-01 to 2026-12-31 | US-TXS5-019 | TWC "generally [[FACT:tx.sui.new_employer.rate=2.70]]%" first six quarters; statute floor 2.6% (US-TXS5-008); not derivable |
| `tx.ui.etia.rate` | [[FACT:tx.ui.etia.rate=0.1]] | % | from 2026-01-01 | US-TXS5-008 | offset by 0.1-pt replenishment cut; no net increase |
| `tx.sui.employee.rate` | [[FACT:tx.sui.employee.rate=0]] | % | from 2026-01-01 | US-TXS5-008 | 204.003 |
| `tx.sdi_pfml.exists` | [[FACT:tx.sdi_pfml.exists=False]] |  | from 2026-01-01 | US-TXR3-003 |  |
| `tx.sui.employer.rate.min` | [[FACT:tx.sui.employer.rate.min=0.32]] | % | 2026-01-01 to 2026-12-31 | US-TXSUI-001 |  |
| `tx.sui.employer.rate.max` | [[FACT:tx.sui.employer.rate.max=6.32]] | % | 2026-01-01 to 2026-12-31 | US-TXSUI-001 |  |
| `tx.ui.wages.401k_section125` | [[FACT:tx.ui.wages.401k_section125=Wages = all remuneration for personal services (201.081); 201.082 exceptions read in full contain no exclusion for employee elective 401(k) deferrals or IRC s.125 reductions (only payments to/from exempt 401(a) trusts); TWC guidance not obtained]] [[GAP:RQ-339]] |  | from 2026-01-01 | US-TXV6-004 | Register: US-TXV6-004 |

**Open research points**

- Not configured in this release [[GAP:RQ-338]]: The published new-employer rate cannot be re-derived without the 2026 major-group rates.
- Not yet published [[GAP:RQ-342]]: The 2027 Texas Workforce Commission tax rates are set in November or December and are not yet published.

## TX.4 Pay statement

- **Labor Code 62.003 (earnings statement) exists, for employees outside FLSA coverage only [US-TXS5-003].** At the end of each pay period: [[FACT:tx.payslip.content.non_flsa=signed statement: name, rate, gross, each deduction and purpose, net, hours or units]]; any form, including the check voucher; meals or lodging credited toward the wage stated separately (62.053). For FLSA-covered employees Texas has no statutory content rule (federal records rules apply). Never write "Texas has no pay-statement law".
- **Electronic delivery and retention:** no Texas rule in chapters 61 or 62; retention follows FLSA and UI record rules (the TWC records-retention rule was not read).

**Parameters (payslip statute and payroll records)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `tx.payslip.content.non_flsa` | [[FACT:tx.payslip.content.non_flsa=signed statement: name, rate, gross, each deduction and purpose, net, hours or units]] |  | from 1993-09-01 | US-TXS5-003 | Labor Code 62.003 - ONLY employees outside FLSA coverage (62.151); best practice for others |

## TX.5 Statutory reporting

- **No withholding return or state W-2.**
- **Quarterly UI wage report and payment [US-TXSUI-006]:** [[FACT:tx.report.ui.channel=electronic only (Unemployment Tax Services / QuickFile: ICESA, MMREF-1, delimited)]]. Due dates: [[FACT:tx.report.ui.due_date_records=Quarterly wage report and tax due last day of month after quarter end: Apr 30, Jul 31, Oct 31, Jan 31. Records-retention rule (40 TAC 815.107) not verified]] [US-TXV6-001].
- **Enhanced wage-report content (Labor Code 204.0025, 2025 amendments) [US-TXS5-008]:** [[FACT:tx.report.ui.enhanced_fields=wage, industry, occupation, FT/PT, county of primary employment, remote-work status]]. Status: [[FACT:tx.report.ui.enhanced_fields.status=PROPOSED ONLY: TWC proposed amendment to 40 TAC 815.107 (51 TexReg 5161, 2026-08-07; approved for proposal 2026-07-21, comments to 2026-09-07) would add to the quarterly wage report: wages, industry, occupation field, full/part-time status, county of primary employment, remote-work status (Labor Code 204.0025) and data for the 302.0205 Regional Labor Demand Assessment. Not adopted in the Texas Register adopted-rules issues of 2026-09-25 to 2026-10-30: on 2026-11-02 no field is mandatory and no start quarter is set.]] [US-TXV6-005]. Proposed only: these fields are not configured as mandatory (open point below).
- **New hire [US-TXS5-012, US-TXS5-016, US-TXS5-017]:** to the OAG Child Support Division state directory within [[FACT:tx.newhire.report_days=20]] calendar days of the first day of work, or twice monthly for electronic reporters. Who is reported: [[FACT:tx.report.new_hire.contractors=For new-hire reporting 'employee' = IRC 3401(c) employee OR an independent contractor as defined by the IRS (also TNC drivers); employers report each newly hired/rehired employee to the state directory per 42 USC 653a]] [US-TXV6-002]; independent contractors are out of scope for this guide (US-OWN-008).
- **Registration:** TWC UI account once the coverage thresholds are met; agent authorisation Form C-42 [US-TXSUI-005, US-TXP52-008].

**Parameters (statutory reporting)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `tx.report.ui.enhanced_fields` | [[FACT:tx.report.ui.enhanced_fields=wage, industry, occupation, FT/PT, county of primary employment, remote-work status]] |  | from 2025-06-01 | US-TXS5-008 | Labor Code 204.0025 (2025) lists the data; TWC implementation is a PROPOSED rule only (tx.report.ui.enhanced_fields.status, US-TXB5-301) - not mandatory on 2026-11-02. |
| `tx.newhire.report_days` | [[FACT:tx.newhire.report_days=20]] | days | from 2026-01-01 | US-TXS5-017 | OAG; second authority US-TXS5-016 form |
| `tx.report.ui.channel` | [[FACT:tx.report.ui.channel=electronic only (Unemployment Tax Services / QuickFile: ICESA, MMREF-1, delimited)]] |  | from 2026-01-01 | US-TXSUI-006 | due date not verified from primary source |
| `tx.report.ui.enhanced_fields.status` | [[FACT:tx.report.ui.enhanced_fields.status=PROPOSED ONLY: TWC proposed amendment to 40 TAC 815.107 (51 TexReg 5161, 2026-08-07; approved for proposal 2026-07-21, comments to 2026-09-07) would add to the quarterly wage report: wages, industry, occupation field, full/part-time status, county of primary employment, remote-work status (Labor Code 204.0025) and data for the 302.0205 Regional Labor Demand Assessment. Not adopted in the Texas Register adopted-rules issues of 2026-09-25 to 2026-10-30: on 2026-11-02 no field is mandatory and no start quarter is set.]] |  | from 2026-08-07 | US-TXB5-301 | identity 40 TAC 815.107 (proposed), 51 TexReg 5161; status proposal, not adopted; level employer reporting. Configure nothing as mandatory; re-check adopted-rules issues from November 2026. Status as of 2026-11-06 [US-TXV6-005]: TWC 40 TAC ch. 815 amendments are PROPOSED only, not adopted; do not configure as mandatory. |
| `tx.report.ui.due_date_records` | [[FACT:tx.report.ui.due_date_records=Quarterly wage report and tax due last day of month after quarter end: Apr 30, Jul 31, Oct 31, Jan 31. Records-retention rule (40 TAC 815.107) not verified]] |  | from 2026-01-01 | US-TXV6-001 | Register: US-TXV6-001 |
| `tx.report.new_hire.contractors` | [[FACT:tx.report.new_hire.contractors=For new-hire reporting 'employee' = IRC 3401(c) employee OR an independent contractor as defined by the IRS (also TNC drivers); employers report each newly hired/rehired employee to the state directory per 42 USC 653a]] |  | from 2026-01-01 | US-TXV6-002 | Register: US-TXV6-002 |

**Open research points**

- Not yet published [[GAP:RQ-580]]: The Texas Workforce Commission amendment to 40 TAC ch. 815 (new wage-record data elements) is proposed only and not adopted; the adoption date, the first mandatory quarter and the file layout are not published. The fields are not configured as mandatory.

## TX.6 Leave

- **Paid sick leave:** no state statute (exists: [[FACT:tx.leave.sick.state_statute.exists=False]]); Labor Code 1.005 (H.B. 2127, 2023) preempts city and county leave, benefit and scheduling ordinances for private employers [US-TXS5-005]. No PFML.
- **Leave pay is wages only if promised in writing** (61.001(7)(B)) [US-TXS5-004].
- **Voting time (Election Code 276.004):** paid ([[FACT:tx.leave.voting.paid=True]]): no penalty, including lost wages, for time off to vote, unless the polls are open long enough outside working hours [US-TXS5-014]. Jury and military leave: [[FACT:tx.leave.jury_military=Jury service: permanent employee may not be discharged/threatened/coerced; right to return to same employment on notice; text states no pay obligation. Military leave (Gov. Code 431.005/437.204) not verified]] [US-TXV6-003].

**Parameters (leave)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `tx.leave.sick.state_statute.exists` | [[FACT:tx.leave.sick.state_statute.exists=False]] |  | from 2023-09-01 | US-TXS5-005 | Labor Code 1.005 preempts local ordinances |
| `tx.leave.voting.paid` | [[FACT:tx.leave.voting.paid=True]] |  | from 2026-01-01 | US-TXS5-014 | unless polls open 2 consecutive hours outside working hours |
| `tx.leave.jury_military` | [[FACT:tx.leave.jury_military=Jury service: permanent employee may not be discharged/threatened/coerced; right to return to same employment on notice; text states no pay obligation. Military leave (Gov. Code 431.005/437.204) not verified]] |  | from 2026-01-01 | US-TXV6-003 | Register: US-TXV6-003 |

## TX.7 Termination and final pay

- **Final pay (61.014) [US-TXS5-004]:** a discharged employee is paid within [[FACT:tx.term.final_pay.discharge.days=6]] calendar days of discharge; any other separation: [[FACT:tx.term.final_pay.other=next regularly scheduled payday]]. Commissions and bonuses follow the agreement (61.015).
- **Accrued vacation:** [[FACT:tx.term.vacation.payout=only if written policy or agreement promises it]] [US-TXS5-004, US-TXS5-018].
- **Child-support interaction (FC 158.215, 158.214) [US-TXS5-011]:** with a IV-D administrative writ, notify the OAG before any lump-sum payment of [[FACT:tx.garn.iwo.lump_sum.threshold=500]] USD or more and hold it for the statutory period; severance is withheld as usual earnings within the cap.
- No state separation notice or mini-WARN found.

**Parameters (termination)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `tx.term.final_pay.discharge.days` | [[FACT:tx.term.final_pay.discharge.days=6]] | days | from 2026-01-01 | US-TXS5-004 | calendar days after discharge; other separations next regular payday (61.014) |
| `tx.term.final_pay.other` | [[FACT:tx.term.final_pay.other=next regularly scheduled payday]] |  | from 2026-01-01 | US-TXS5-004 |  |
| `tx.term.vacation.payout` | [[FACT:tx.term.vacation.payout=only if written policy or agreement promises it]] |  | from 2026-01-01 | US-TXS5-004 | 61.001(7)(B) |

## TX.8 Benefits in kind and taxable wages

- **No income tax;** conformity matters only for the UI wage definition (Section 3) [US-TXS5-007].

## TX.9 Deductions and garnishments

- **Wage deductions (61.018):** only by court order, by law, or with written authorisation for a lawful purpose [US-TXS5-004].
- **Garnishment (Const. Art. XVI s.28; CPRC 63.004) [US-TXS5-009, US-TXS5-010]:** current wages are exempt except for child support and spousal maintenance; creditor wage garnishment available: [[FACT:tx.garn.consumer.available=False]]. Federal tax levies and federal administrative garnishments apply by federal law.
- **Child-support IWO [US-TXS5-011]:** cap [[FACT:tx.garn.iwo.max_rate=50]] % of disposable earnings (158.009); start by the first pay period after delivery; remit to the SDU on each pay date (larger employers electronically); employer fee up to [[FACT:tx.garn.iwo.employer_fee.monthly=10]] USD per month (158.204); multiple orders split equally, current support first; notify termination within [[FACT:tx.garn.iwo.termination_notice_days=7]] days (158.211).

**Parameters (deductions and garnishments)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `tx.garn.consumer.available` | [[FACT:tx.garn.consumer.available=False]] |  | from 1999-11-02 | US-TXS5-009 | current wages exempt except support/spousal maintenance (Const. XVI s.28) |
| `tx.garn.iwo.max_rate` | [[FACT:tx.garn.iwo.max_rate=50]] | % | from 2026-01-01 | US-TXS5-011 | of disposable earnings |
| `tx.garn.iwo.employer_fee.monthly` | [[FACT:tx.garn.iwo.employer_fee.monthly=10]] | USD | from 2026-01-01 | US-TXS5-011 | 158.204 |
| `tx.garn.iwo.lump_sum.threshold` | [[FACT:tx.garn.iwo.lump_sum.threshold=500]] | USD | from 2026-01-01 | US-TXS5-011 | notify OAG; hold 10 days |
| `tx.garn.iwo.termination_notice_days` | [[FACT:tx.garn.iwo.termination_notice_days=7]] | days | from 2026-01-01 | US-TXS5-011 |  |

## TX.10 Collective agreements and prevailing wage

Prevailing wage (public works) is an optional informational flag [US-OWN-009]: this guide documents prevailing-wage laws, thresholds and certified-payroll duties as an overlay, and the payroll build does not produce certified payroll reports.

- **Prevailing wage (Gov. Code ch. 2258) [US-TXR3-002, US-TXS5-015]:** public works; the public body sets the rate (survey or Davis-Bacon); penalty [[FACT:tx.prevailing_wage.penalty.per_worker_day=60]] USD per worker per day; records of name, occupation and per diem wage; no state certified-payroll form.

**Parameters (collective agreements and prevailing wage)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `tx.prevailing_wage.penalty.per_worker_day` | [[FACT:tx.prevailing_wage.penalty.per_worker_day=60]] | USD | from 2026-01-01 | US-TXS5-015 | Gov. Code ch. 2258; public body sets rate |

## TX.11 Indexation

- **Nothing is indexed by state law:** minimum wage follows the FLSA; the UI wage base is statutory; UI rates are recomputed by TWC each year and mailed in December; 2027 rates not yet published (open point below).

## TX.12 Payroll data protection and records

- **Business and Commerce Code 501.001 [US-TXS5-013]:** no public display of SSNs, no SSN on access cards, no unsecured transmission, no SSN on mailed material unless law requires it ([[FACT:tx.data.ssn.mailed_prohibited=True]]). No pay-statement truncation rule: a mailed paper payslip should not show the full SSN.

**Parameters (payroll data protection)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `tx.data.ssn.mailed_prohibited` | [[FACT:tx.data.ssn.mailed_prohibited=True]] |  | from 2026-01-01 | US-TXS5-013 | B&C 501.001; mask on paper payslips (our reading) |

## TX.13 Live legal change

- **Const. Art. VIII s.24-b (approved 2025-11-04):** capital gains tax ban; no payroll effect [US-TXS5-001].
- **Labor Code 204.0025:** enhanced wage-filing data; payroll and DD impact depends on TWC implementation (open point below) [US-TXS5-008].
- **2027 TWC rates** due December 2026; not swept (TWC site blocked).

## TX.14 Authority worked examples (oracle values)

No authority worked example is reproduced in this annex; recomputed withholding examples are in Module 12.

## TX.15 Special populations

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

## TX.16 Language

No language rule for employee documents is written for this jurisdiction in this annex.

## TX.S Sources

Register ids cited in this annex resolve to the build record; the URL of each value is in the facts file. Authorities:

- Build lead (Claude) under owner delegation (Wallisson Gomes): US-OWN-006
- Office of the Attorney General of Texas - Child Support Division: US-TXS5-016
- Owner (Wallisson Gomes): US-OWN-008
- Texas Comptroller of Public Accounts: US-TXP52-001
- Texas Legislative Council: US-TXS5-015
- Texas Legislative Council (tcss.legis.texas.gov official statutes file server): US-TXS5-001
- Texas Legislative Council (tcss.legis.texas.gov): US-TXS5-002, US-TXS5-003, US-TXS5-004, US-TXS5-005, US-TXS5-006, US-TXS5-007, US-TXS5-008, US-TXS5-009, US-TXS5-010, US-TXS5-011, US-TXS5-012, US-TXS5-013, US-TXS5-014
- Texas Legislature (statutes.capitol.texas.gov): US-TXR3-002, US-TXV6-002, US-TXV6-003, US-TXV6-004
- Texas Secretary of State (Texas Register) / Texas Workforce Commission: US-TXB5-301
- Texas Workforce Commission: US-TXP52-008, US-TXR3-003, US-TXS5-017, US-TXS5-019, US-TXSUI-001, US-TXSUI-005, US-TXSUI-006, US-TXV6-001, US-TXV6-005
- Texas Workforce Commission (Office of the Commissioner Representing Employers): US-TXS5-018
