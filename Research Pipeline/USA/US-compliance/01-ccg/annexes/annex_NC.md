# Annex NC: North Carolina

United States Country Configuration Guide, jurisdiction annex NC. Tax year 2026; currency USD (two decimal places).

## NC.0 Scope of this annex

This annex holds the North Carolina layer only. The federal layer (federal income tax withholding, Social Security and Medicare, federal unemployment tax, Forms W-4, W-2, 941 and 940) is in Annex FED, and the rules for employees who live and work in different jurisdictions (sourcing, resident credits, reciprocity mechanics) are in Annex MULTI. Neither is repeated here. Independent contractors and Form 1099-NEC are out of scope. The pay statement is issued in English.

In every table, *Valid from* and *Valid to* give the period in which the value applies (*open* means no end date has been published), and *Source* is the identifier of the row in the legal-basis register (00-official-sources/legal-basis-register.csv), with the authority and address listed in section NC.20 (the source address is held in the register row). Items marked as a research gap are not yet confirmed and must not be configured from this annex.

## NC.1 Jurisdiction layer

| Item | Value |
|---|---|
| Annex tier | T3 |
| Basis | State withholding verified [US-NC-001] |

Tier key: T1 = no state wage tax (unemployment insurance and levies only); T3 = state withholding with no local layer remitted separately; T4 = a local layer remitted to a separate local authority on its own return.

## NC.2 Configuration decisions

- Withholding uses [[FACT:nc.pit.wh.rate=4.09]] percent, not the statutory rate of [[FACT:nc.pit.rate.flat=3.99]] percent.
- The 2027 rate is not modelled until the Department of Revenue publishes the 2027 withholding method (blocking gap in section NC.4).
- Withholding is rounded to the nearest whole dollar, while the nonresident-alien add-on is rounded up (`nc.pit.rounding`).
- There is no local wage tax ([[FACT:nc.local_wage_tax.exists=False]]) and no reciprocity agreement ([[FACT:nc.reciprocity.states=none]]).

## NC.3 Employment and labour code

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nc.labour.minwage.state.follows_federal` | [[FACT:nc.labour.minwage.state.follows_federal=True]] | 2006-08-23 | open | US-NCS5-002 (A.1, NC General Assembly (General Statutes, official host ncleg.gov)) | Higher of the state statutory floor or the FLSA rate ([[FACT:fed.minwage.hourly=7.25]] in 2026, Annex FED); no state indexation. |
| `nc.labour.minwage.student_learner.hourly` | [[FACT:nc.labour.minwage.student_learner.hourly=6.5]] USD | 2026-01-01 | open | US-NCS5-002 (A.1, NC General Assembly (General Statutes, official host ncleg.gov)) | 90% of [[FACT:fed.minwage.hourly=7.25]] = 6.525 rounded down to the nickel; full-time students, learners, apprentices, messengers |
| `nc.local_mandates.preempted` | [[FACT:nc.local_mandates.preempted=True]] | 2023-10-03 | open | US-NCS5-001 (A.1, NC General Assembly (General Statutes, official host ncleg.gov)) | 95-25.1(d) |
| `nc.overtime.weekly_threshold_hours` | [[FACT:nc.overtime.weekly_threshold_hours=40]] hours | 1991-06-19 | open | US-NCS5-003 (A.1, NC General Assembly (General Statutes, official host ncleg.gov)) | no daily OT; FLSA-covered enterprises governed by FLSA |
| `nc.overtime.premium.multiplier` | [[FACT:nc.overtime.premium.multiplier=1.5]] ratio | 1991-06-19 | open | US-NCS5-003 (A.1, NC General Assembly (General Statutes, official host ncleg.gov)) | - |
| `nc.labour.pay_frequency.allowed` | [[FACT:nc.labour.pay_frequency.allowed=daily; weekly; biweekly; semimonthly; monthly]] | 2026-01-01 | open | US-NCS5-005 (A.1, NC General Assembly (General Statutes, official host ncleg.gov)) | bonuses/commissions as rarely as annually if scheduled |

- ⚠️ RESEARCH-GAP (non-blocking, `nc.payment.method`): NC direct deposit / paycard consent rule not located. To close: NCDOL wage-payment FAQ or a 13 NCAC 12 rule on payment method.

## NC.4 State income tax withholding

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nc.pit.rate.flat` | [[FACT:nc.pit.rate.flat=3.99]] percent | 2026-01-01 | open | US-NCS5-011 (A.1, NC General Assembly (General Statutes, official host ncleg.gov)) | G.S. 105-153.7(a) tax years after 2025 |
| `nc.pit.wh.rate` | [[FACT:nc.pit.wh.rate=4.09]] percent | 2026-01-01 | 2026-12-31 | US-NC-001 (A.2, NC Department of Revenue) | 3.99% + 0.1%; nearest whole dollar |
| `nc.pit.std_deduction.single` | [[FACT:nc.pit.std_deduction.single=12750]] USD | 2026-01-01 | open | US-NCS5-010 (A.1, NC General Assembly (General Statutes, official host ncleg.gov)) | also MFS; married withholding tables use single deduction (US-NC-001) |
| `nc.pit.std_deduction.head_of_household` | [[FACT:nc.pit.std_deduction.head_of_household=19125]] USD | 2026-01-01 | open | US-NCS5-010 (A.1, NC General Assembly (General Statutes, official host ncleg.gov)) | - |
| `nc.pit.std_deduction.mfj` | [[FACT:nc.pit.std_deduction.mfj=25500]] USD | 2026-01-01 | open | US-NCS5-010 (A.1, NC General Assembly (General Statutes, official host ncleg.gov)) | - |
| `nc.pit.allowance.amount` | [[FACT:nc.pit.allowance.amount=2500]] USD | 2026-01-01 | 2026-12-31 | US-NC-001 (A.2, NC Department of Revenue) | per year |
| `nc.pit.rounding` | [[FACT:nc.pit.rounding=nearest whole dollar (NRA add-on rounded up)]] | 2026-01-01 | 2026-12-31 | US-NC-001 (A.2, NC Department of Revenue) | - |
| `nc.pit.oracle.example_1.withholding` | [[FACT:nc.pit.oracle.example_1.withholding=4]] USD | 2026-01-01 | 2026-12-31 | US-NC-001 (A.2, NC Department of Revenue) | percentage method 450 weekly single 2 allowances: (450-245.19-96.16) x 0.0409 = [[FACT:nc.oracle.weekly_450_s2.withholding=4.44]] -> 4; annualized (23,400-17,750) x 0.0409/52 = [[FACT:nc.oracle.weekly_450_s2.withholding=4.44]] -> 4 |
| `nc.pit.oracle.example_2.nra_withholding` | [[FACT:nc.pit.oracle.example_2.nra_withholding=21]] USD | 2026-01-01 | 2026-12-31 | US-NC-001 (A.2, NC Department of Revenue) | NC-30 NRA example 500 x 4.09% = 20.45 -> 21 (rounded up) |
| `nc.wh.certificate` | [[FACT:nc.wh.certificate=no NC-4: single, zero allowances; federal W-4 not acceptable]] | 2026-01-01 | open | US-NC-001 (A.2, NC Department of Revenue) | exempt certificate expires; withhold from Feb 16 without new NC-4 EZ |
| `nc.wh.supplemental.rate` | [[FACT:nc.wh.supplemental.rate=4.09]] percent | 2026-01-01 | 2026-12-31 | US-NC-001 (A.2, NC Department of Revenue) | or aggregate; aggregate mandatory if nothing withheld from regular wages |

- ⚠️ RESEARCH-GAP (blocking, `nc.pit.rate.next_year`): The 2027 rate depends on a revenue trigger and is not confirmed. It is not written and must not be modelled until the Department of Revenue publishes the 2027 Form NC-30. To close: OSC FY2025-26 final General Fund accounting (August 2026) or the 2027 NC-30 / NCDOR rate notice.

## NC.5 Non-residents, residents working elsewhere and reciprocity

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nc.pit.nra.addon.weekly` | [[FACT:nc.pit.nra.addon.weekly=11]] USD | 2026-01-01 | 2026-12-31 | US-NC-001 (A.2, NC Department of Revenue) | [[FACT:nc.pit.std_deduction.single=12,750]] x 4.09% / 52 = 10.03 rounded up; capped at 4.09% of wages when annualized <= [[FACT:nc.pit.std_deduction.single=12,750]] |
| `nc.pit.nra.addon.biweekly` | [[FACT:nc.pit.nra.addon.biweekly=21]] USD | 2026-01-01 | 2026-12-31 | US-NC-001 (A.2, NC Department of Revenue) | - |
| `nc.pit.nra.addon.semimonthly` | [[FACT:nc.pit.nra.addon.semimonthly=22]] USD | 2026-01-01 | 2026-12-31 | US-NC-001 (A.2, NC Department of Revenue) | - |
| `nc.pit.nra.addon.monthly` | [[FACT:nc.pit.nra.addon.monthly=44]] USD | 2026-01-01 | 2026-12-31 | US-NC-001 (A.2, NC Department of Revenue) | - |
| `nc.reciprocity.states` | [[FACT:nc.reciprocity.states=none]] | 2026-01-01 | open | US-NC-001 (A.2, NC Department of Revenue) | - |

## NC.6 Local wage taxes

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nc.local_wage_tax.exists` | [[FACT:nc.local_wage_tax.exists=False]] | 2026-01-01 | open | US-NCP51-001 (A.1, North Carolina General Assembly) | G.S. 105-247 prohibits |

## NC.7 Unemployment insurance, disability and paid-leave contributions, other payroll levies

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nc.sui.wage_base` | [[FACT:nc.sui.wage_base=34200]] USD | 2026-01-01 | 2026-12-31 | US-NC-002 (A.2, NC Division of Employment Security) | 2025: 32,600; other-state and predecessor wages count (US-NCS5-015) |
| `nc.sui.wage_base.other_state_credit` | [[FACT:nc.sui.wage_base.other_state_credit=True]] | 2026-01-01 | open | US-NCS5-015 (A.1, NC General Assembly (General Statutes, official host ncleg.gov)) | - |
| `nc.sui.new_employer.rate` | [[FACT:nc.sui.new_employer.rate=1.0]] percent | 2026-01-01 | 2026-12-31 | US-NCS5-014 (A.1, NC General Assembly (General Statutes, official host ncleg.gov)) | - |
| `nc.ui.rate.base` | [[FACT:nc.ui.rate.base=1.9]] percent | 2026-01-01 | 2026-12-31 | US-NCP9V-001 (A.2, North Carolina Division of Employment Security) | experience rate = base - reserve ratio x 0.68 |
| `nc.sui.employer.rate.min` | [[FACT:nc.sui.employer.rate.min=0.06]] percent | 2026-01-01 | 2026-12-31 | US-NCP9V-001 (A.2, North Carolina Division of Employment Security) | - |
| `nc.sui.employer.rate.max` | [[FACT:nc.sui.employer.rate.max=5.76]] percent | 2026-01-01 | 2026-12-31 | US-NCP9V-001 (A.2, North Carolina Division of Employment Security) | 20% surtax only if trust fund < 1 bn |
| `nc.sui.employee.rate` | [[FACT:nc.sui.employee.rate=0]] percent | 2026-01-01 | open | US-NCS5-014 (A.1, NC General Assembly (General Statutes, official host ncleg.gov)) | may not be deducted |

- ⚠️ RESEARCH-GAP (non-blocking, `nc.ui.wage_base.derivation`): Reproducing the wage base of [[FACT:nc.sui.wage_base=34200]] USD needs the agency's average weekly insured wage at the 2025 computation date. To close: DES Labor Market Information average-wage publication.
- ⚠️ RESEARCH-GAP (non-blocking, `nc.ui.registration`): NCSUITS registration steps and liability thresholds (incl. domestic/agricultural) not read. To close: G.S. 96-1(b) text plus the DES registration page.

## NC.8 Pay statement

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nc.payslip.items` | [[FACT:nc.payslip.items=itemized statement of deductions each pay period with deductions; wage notice at hire]] | 2026-01-01 | open | US-NCW1B-003 (A.2, North Carolina General Assembly) | 95-25.13; writing, printable e-mail or any keepable form (US-NCS5-024) |

## NC.9 Statutory reporting

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nc.report.wh.quarterly_threshold.monthly_avg` | [[FACT:nc.report.wh.quarterly_threshold.monthly_avg=250]] USD | 2026-01-01 | open | US-NC-001 (A.2, NC Department of Revenue) | <250 quarterly NC-5; 250-<2,000 monthly by 15th; >=2,000 semiweekly NC-5P + NC-5Q |
| `nc.report.wh.semiweekly_threshold.monthly_avg` | [[FACT:nc.report.wh.semiweekly_threshold.monthly_avg=2000]] USD | 2026-01-01 | open | US-NC-001 (A.2, NC Department of Revenue) | - |
| `nc.report.nc3.due` | [[FACT:nc.report.nc3.due=January 31, electronic (eNC3)]] | 2026-01-01 | open | US-NC-001 (A.2, NC Department of Revenue) | late 50/day max 1,000; wrong format 200 |
| `nc.report.efile_spec.version` | [[FACT:nc.report.efile_spec.version=9-2026 (TY2026, use beginning January 2027)]] | 2027-01-01 | open | US-NCS5-028 (A.2, NC Department of Revenue) | NC-3/W-2 fixed-field.txt |
| `nc.report.ui.quarterly_due` | [[FACT:nc.report.ui.quarterly_due=Apr 30; Jul 31; Oct 31; Jan 31]] | 2026-01-01 | open | US-NCS5-025 (A.2, NC Division of Employment Security (NC Department of Commerce)) | NCUI 101 via NCSUITS; electronic mandatory at 10+ wage items |
| `nc.newhire.report_days` | [[FACT:nc.newhire.report_days=20]] days | 2026-01-01 | open | US-NCS5-020 (A.1, NC General Assembly (General Statutes, official host ncleg.gov)) | or twice monthly 12-16 days apart electronically |

Rules:

- Third-party and POA: NCDOR GEN-58; DES POA. (US-NCW1B-002, US-NCP51-003, US-FIL-013)

- ⚠️ RESEARCH-GAP (non-blocking, `nc.report.w2.file_format`): Whether the North Carolina W-2 file in eNC3 uses the federal EFW2 layout or a state layout is not confirmed; the current state specification was not obtained. To close: TY2026 "eNC3 W2" spec version 9-2026 from the NCDOR eNC3 file-format page.

## NC.10 Leave

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nc.leave.sick.state_statute.exists` | [[FACT:nc.leave.sick.state_statute.exists=False]] | 2023-10-03 | open | US-NCS5-001 (A.1, NC General Assembly (General Statutes, official host ncleg.gov)) | local mandates preempted |

- ⚠️ RESEARCH-GAP (non-blocking, `nc.leave.other`): Jury-duty, voting and other leave with pay impact not searched. To close: G.S. 9-32 and related statutes on ncleg.gov.

## NC.11 Termination and final pay

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nc.final_pay.rule` | [[FACT:nc.final_pay.rule=next regular payday (discharge and resignation)]] | 2026-01-01 | open | US-NCS5-006 (A.1, NC General Assembly (General Statutes, official host ncleg.gov)) | bonuses/commissions first payday after calculable |
| `nc.term.vacation.payout` | [[FACT:nc.term.vacation.payout=per employer policy; forfeiture only with advance written notice]] | 2026-01-01 | open | US-NCS5-008 (A.1, NC General Assembly (General Statutes, official host ncleg.gov)) | - |
| `nc.term.final_w2.days` | [[FACT:nc.term.final_w2.days=30]] days | 2026-01-01 | open | US-NC-001 (A.2, NC Department of Revenue) | after final wage payment |

- ⚠️ RESEARCH-GAP (non-blocking, `nc.term.ui_separation_notice`): Whether NC employers must hand separating employees a UI-availability notice is not confirmed. To close: 04 NCAC 24A/24B text on the OAH host, or the DES employer handbook.

## NC.12 Taxable wages and benefits in kind

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nc.bik.conformity.irc_date` | [[FACT:nc.bik.conformity.irc_date=2025-07-05]] | 2026-01-01 | open | US-NCS5-029 (A.2, NC Department of Revenue) | S.L. 2026-31; withholding follows IRC 3401 (US-NCS5-012) |

## NC.13 Deductions and garnishments

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nc.garn.support.max_rate` | [[FACT:nc.garn.support.max_rate=40]] percent | 2026-01-01 | open | US-NCS5-018 (A.1, NC General Assembly (General Statutes, official host ncleg.gov)) | of monthly disposable earnings; 1 USD fee per pay period |
| `nc.garn.support.employer_fee.per_period` | [[FACT:nc.garn.support.employer_fee.per_period=1]] USD | 2026-01-01 | open | US-NCS5-018 (A.1, NC General Assembly (General Statutes, official host ncleg.gov)) | - |
| `nc.garn.tax_levy.max_rate` | [[FACT:nc.garn.tax_levy.max_rate=10]] percent | 2026-01-01 | open | US-NCS5-021 (A.1, NC General Assembly (General Statutes, official host ncleg.gov)) | G.S. 105-242(b) |

- ⚠️ RESEARCH-GAP (non-blocking, `nc.garn.iwo.payor_duties`): IV-D remittance timing and payor fee (110-136.5 to.8) not extracted. To close: G.S. 110-136.5 to 110-136.8.

## NC.14 Prevailing wage and collective agreements

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nc.prevailing_wage.exists` | [[FACT:nc.prevailing_wage.exists=False]] | 2026-01-01 | open | US-NCP51-004 (A.2, US Department of Labor Wage and Hour Division) | DOL WHD state table |

Rules:

- NC has no state prevailing-wage law (DOL WHD state table). So there is no state certified-payroll duty; federal Davis-Bacon applies on federal projects (Annex FED). (US-NCP51-004)

## NC.15 Indexation

Indexation of each value is stated in the note of the value concerned.

## NC.16 Payroll data protection and records

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nc.records.wage_hour.retention_years` | [[FACT:nc.records.wage_hour.retention_years=3]] years | 1980-11-01 | open | US-NCS5-022 (A.1, NC Office of Administrative Hearings - NC Administrative Code (13 NCAC 12, NC Department of Labor rules)) | 13 NCAC 12.0802 |
| `nc.records.withholding.retention_years` | [[FACT:nc.records.withholding.retention_years=10]] years | 2026-01-01 | open | US-NC-001 (A.2, NC Department of Revenue) | NC-30 s.26 |
| `nc.data.ssn.mailing_restricted` | [[FACT:nc.data.ssn.mailing_restricted=True]] | 2026-01-01 | open | US-NCS5-016 (A.1, NC General Assembly (General Statutes, official host ncleg.gov)) | 75-62; safe build truncates SSN on mailed stubs |

- ⚠️ RESEARCH-GAP (non-blocking, `nc.data.breach`): G.S. 75-65 breach notice not read. To close: The statute text.

## NC.17 Legal change in force or enacted

No North Carolina rule is configured in this domain; the federal treatment in Annex FED applies.

## NC.18 Special populations

- Domestic / household: No NC withholding required (voluntary agreement possible); Exempt from state minimum wage, overtime and youth rules (FLSA applies). (US-NC-001, US-NCS5-009)
- Minors: Youth employment certificate; school-night hours limit. (US-NCS5-004)
- Tipped: tips withheld as supplemental. (US-NCS5-002, US-NC-001)
- Nonresident aliens: treaty-exempt wages exempt. (US-NC-001)
- Government employees: Only minimum wage and a few Wage and Hour Act provisions apply to public employers. (US-NC-001, US-NCS5-009)
- ⚠️ RESEARCH-GAP (non-blocking, `nc.special_populations.thresholds`): thresholds, amounts or conditions for these populations are stated in the research without a confirmed value record and are not configured from this annex: Domestic / household; Agricultural; Tipped; Clergy / religious; Students; Nonresident aliens; Statutory employees; Government employees; Military spouses (SCRA); Interstate rail, motor carrier, airline; Tribal members on reservation; Seamen. To close: one confirmed value per threshold, with its source row.

## NC.19 Language

- The pay statement and all filings are in English (owner decision US-OWN-006).

## NC.20 Sources

| Source | Authority |
|---|---|
| US-NC-001 | NC Department of Revenue |
| US-NC-002 | NC Division of Employment Security |
| US-NCP51-001 | North Carolina General Assembly |
| US-NCP51-004 | US Department of Labor Wage and Hour Division |
| US-NCP9V-001 | North Carolina Division of Employment Security |
| US-NCS5-001 | NC General Assembly (General Statutes, official host ncleg.gov) |
| US-NCS5-002 | NC General Assembly (General Statutes, official host ncleg.gov) |
| US-NCS5-003 | NC General Assembly (General Statutes, official host ncleg.gov) |
| US-NCS5-005 | NC General Assembly (General Statutes, official host ncleg.gov) |
| US-NCS5-006 | NC General Assembly (General Statutes, official host ncleg.gov) |
| US-NCS5-008 | NC General Assembly (General Statutes, official host ncleg.gov) |
| US-NCS5-010 | NC General Assembly (General Statutes, official host ncleg.gov) |
| US-NCS5-011 | NC General Assembly (General Statutes, official host ncleg.gov) |
| US-NCS5-014 | NC General Assembly (General Statutes, official host ncleg.gov) |
| US-NCS5-015 | NC General Assembly (General Statutes, official host ncleg.gov) |
| US-NCS5-016 | NC General Assembly (General Statutes, official host ncleg.gov) |
| US-NCS5-018 | NC General Assembly (General Statutes, official host ncleg.gov) |
| US-NCS5-020 | NC General Assembly (General Statutes, official host ncleg.gov) |
| US-NCS5-021 | NC General Assembly (General Statutes, official host ncleg.gov) |
| US-NCS5-022 | NC Office of Administrative Hearings - NC Administrative Code (13 NCAC 12, NC Department of Labor rules) |
| US-NCS5-025 | NC Division of Employment Security (NC Department of Commerce) |
| US-NCS5-028 | NC Department of Revenue |
| US-NCS5-029 | NC Department of Revenue |
| US-NCW1B-003 | North Carolina General Assembly |
