# Annex NC: North Carolina


United States Country Configuration Guide, jurisdiction annex NC. Tax year 2026; currency USD (two decimal places).

**Scope of this annex.**

This annex holds the North Carolina layer only. The federal layer (federal income tax withholding, Social Security and Medicare, federal unemployment tax, Forms W-4, W-2, 941 and 940) is in the federal reference, and the rules for employees who live and work in different jurisdictions (sourcing, resident credits, reciprocity mechanics) are in the multistate reference. Neither is repeated here. Independent contractors and Form 1099-NEC reporting are out of scope (owner instruction of 2026-10-29) [US-OWN-008]. The pay statement is issued in English.

In every table, *Valid from* and *Valid to* give the period in which the value applies (*open* means no end date has been published), and *Source* is the identifier of the row in the legal-basis register, with the authority and address listed in section NC.S (the source address is held in the legal-basis entry). Items marked as a research gap are not yet confirmed and must not be configured from this annex.

**Jurisdiction layer.**

| Item | Value |
|---|---|
| Annex tier | T3 |
| Basis | State withholding verified [US-NC-001] |

Tier key: T1 = no state wage tax (unemployment insurance and levies only); T3 = state withholding with no local layer remitted separately; T4 = a local layer remitted to a separate local authority on its own return.

**Configuration decisions.**

- Withholding uses 4.09 percent, not the statutory rate of 3.99 percent.
- The 2027 rate is not modelled until the Department of Revenue publishes the 2027 withholding method (blocking gap in section NC.2).
- Withholding is rounded to the nearest whole dollar, while the nonresident-alien add-on is rounded up (`nc.pit.rounding`).
- There is no local wage tax and no reciprocity agreement (none).

## NC.1 Employment and labour code

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nc.labour.minwage.state.follows_federal` | True | 2006-08-23 | open | US-NCS5-002 (A.1, NC General Assembly (General Statutes, official host ncleg.gov)) | Higher of the state statutory floor or the FLSA rate (7.25 in 2026, the federal reference); no state indexation. |
| `nc.local_mandates.preempted` | True | 2023-10-03 | open | US-NCS5-001 (A.1, NC General Assembly (General Statutes, official host ncleg.gov)) | 95-25.1(d) |
| `nc.overtime.weekly_threshold_hours` | 40 hours | 1991-06-19 | open | US-NCS5-003 (A.1, NC General Assembly (General Statutes, official host ncleg.gov)) | no daily OT; FLSA-covered enterprises governed by FLSA |
| `nc.overtime.premium.multiplier` | 1.5 ratio | 1991-06-19 | open | US-NCS5-003 (A.1, NC General Assembly (General Statutes, official host ncleg.gov)) | - |
| `nc.labour.pay_frequency.allowed` | daily; weekly; biweekly; semimonthly; monthly | 2026-01-01 | open | US-NCS5-005 (A.1, NC General Assembly (General Statutes, official host ncleg.gov)) | bonuses/commissions as rarely as annually if scheduled |

- Not configured in this release (open gap RQ-073): NC direct deposit / paycard consent rule not located.
- Not configured in this release (open gap RQ-589): The full-time student, learner, apprentice and messenger rate of G.S. 95-25.3(b) (ninety percent of the minimum wage) is not configured: no official NCDOL page states the rounded hourly figure.

## NC.2 Income tax withholding

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nc.pit.rate.flat` | 3.99 percent | 2026-01-01 | open | US-NCS5-011 (A.1, NC General Assembly (General Statutes, official host ncleg.gov)) | G.S. 105-153.7(a) tax years after 2025 |
| `nc.pit.wh.rate` | 4.09 percent | 2026-01-01 | 2026-12-31 | US-NC-001 (A.2, NC Department of Revenue) | 3.99% plus the statutory add-on gives the 4.09% withholding rate; nearest whole dollar |
| `nc.pit.std_deduction.single` | 12750 USD | 2026-01-01 | open | US-NCS5-010 (A.1, NC General Assembly (General Statutes, official host ncleg.gov)) | also MFS; married withholding tables use single deduction (US-NC-001) |
| `nc.pit.std_deduction.head_of_household` | 19125 USD | 2026-01-01 | open | US-NCS5-010 (A.1, NC General Assembly (General Statutes, official host ncleg.gov)) | - |
| `nc.pit.std_deduction.mfj` | 25500 USD | 2026-01-01 | open | US-NCS5-010 (A.1, NC General Assembly (General Statutes, official host ncleg.gov)) | - |
| `nc.pit.allowance.amount` | 2500 USD | 2026-01-01 | 2026-12-31 | US-NC-001 (A.2, NC Department of Revenue) | per year |
| `nc.pit.rounding` | nearest whole dollar (NRA add-on rounded up) | 2026-01-01 | 2026-12-31 | US-NC-001 (A.2, NC Department of Revenue) | - |
| `nc.pit.oracle.example_1.withholding` | 4 USD | 2026-01-01 | 2026-12-31 | US-NC-001 (A.2, NC Department of Revenue) | percentage method 450 weekly single 2 allowances: (450-245.19-96.16) x 0.0409 = 4.44 -> 4; annualized (23,400-17,750) x 0.0409/52 = 4.44 -> 4 |
| `nc.pit.oracle.example_2.nra_withholding` | 21 USD | 2026-01-01 | 2026-12-31 | US-NC-001 (A.2, NC Department of Revenue) | NC-30 NRA example 500 x 4.09% = 20.45 -> 21 (rounded up) |
| `nc.wh.certificate` | no NC-4: single, zero allowances; federal W-4 not acceptable | 2026-01-01 | open | US-NC-001 (A.2, NC Department of Revenue) | exempt certificate expires; withhold from Feb 16 without new NC-4 EZ |
| `nc.wh.supplemental.rate` | 4.09 percent | 2026-01-01 | 2026-12-31 | US-NC-001 (A.2, NC Department of Revenue) | or aggregate; aggregate mandatory if nothing withheld from regular wages |

- Not yet published (expected NC-30 for 2027, before 2027-01-01 (trigger data August 2026)) (open gap RQ-074): The 2027 rate depends on a revenue trigger and is not confirmed. It is not written and must not be modelled until the Department of Revenue publishes the 2027 Form NC-30.

## NC.2b Non-resident regime and reciprocity

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nc.pit.nra.addon.weekly` | 11 USD | 2026-01-01 | 2026-12-31 | US-NC-001 (A.2, NC Department of Revenue) | 12,750 x 4.09% / 52 = 10.03 rounded up; capped at 4.09% of wages when annualized <= 12,750 |
| `nc.pit.nra.addon.biweekly` | 21 USD | 2026-01-01 | 2026-12-31 | US-NC-001 (A.2, NC Department of Revenue) | - |
| `nc.pit.nra.addon.semimonthly` | 22 USD | 2026-01-01 | 2026-12-31 | US-NC-001 (A.2, NC Department of Revenue) | - |
| `nc.pit.nra.addon.monthly` | 44 USD | 2026-01-01 | 2026-12-31 | US-NCP51-002 (A.2, North Carolina Department of Revenue) | - |
| `nc.reciprocity.states` | none | 2026-01-01 | open | US-NC-001 (A.2, NC Department of Revenue) | - |

## NC.2c Local wage taxes

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nc.local_wage_tax.exists` | False | 2026-01-01 | open | US-NCP51-001 (A.1, North Carolina General Assembly) | G.S. 105-247 prohibits |

## NC.3 Social insurance: unemployment, disability, paid leave and payroll levies

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nc.sui.wage_base` | 34200 USD | 2026-01-01 | 2026-12-31 | US-NCB5-401 (A.2, NC Division of Employment Security) | other-state and predecessor wages count (US-NCS5-015) |
| `nc.sui.wage_base.other_state_credit` | True | 2026-01-01 | open | US-NCS5-015 (A.1, NC General Assembly (General Statutes, official host ncleg.gov)) | - |
| `nc.sui.new_employer.rate` | 1.0 percent | 2026-01-01 | 2026-12-31 | US-NCS5-014 (A.1, NC General Assembly (General Statutes, official host ncleg.gov)) | - |
| `nc.ui.rate.base` | 1.9 percent | 2026-01-01 | 2026-12-31 | US-NCP9V-001 (A.2, North Carolina Division of Employment Security) | experience rate = base - reserve ratio x 0.68 |
| `nc.sui.employer.rate.min` | 0.06 percent | 2026-01-01 | 2026-12-31 | US-NCP9V-001 (A.2, North Carolina Division of Employment Security) | - |
| `nc.sui.employer.rate.max` | 5.76 percent | 2026-01-01 | 2026-12-31 | US-NCP9V-001 (A.2, North Carolina Division of Employment Security) | 20% surtax only if trust fund < 1 bn |
| `nc.sui.employee.rate` | 0 percent | 2026-01-01 | open | US-NCS5-014 (A.1, NC General Assembly (General Statutes, official host ncleg.gov)) | may not be deducted |

- Not configured in this release (open gap RQ-075): Reproducing the wage base of 34200 USD needs the agency's average weekly insured wage at the 2025 computation date.
- Not configured in this release (open gap RQ-076): NCSUITS registration steps and liability thresholds (incl. domestic/agricultural) not read.

## NC.4 Pay statement

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nc.payslip.items` | itemized statement of deductions each pay period with deductions; wage notice at hire | 2026-01-01 | open | US-NCW1B-003 (A.2, North Carolina General Assembly) | 95-25.13; writing, printable e-mail or any keepable form (US-NCS5-024) |

## NC.5 Statutory reporting

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nc.report.wh.quarterly_threshold.monthly_avg` | 250 USD | 2026-01-01 | open | US-NC-001 (A.2, NC Department of Revenue) | <250 quarterly NC-5; 250-<2,000 monthly by 15th; >=2,000 semiweekly NC-5P + NC-5Q |
| `nc.report.wh.semiweekly_threshold.monthly_avg` | 2000 USD | 2026-01-01 | open | US-NC-001 (A.2, NC Department of Revenue) | - |
| `nc.report.nc3.due` | January 31, electronic (eNC3) | 2026-01-01 | open | US-NC-001 (A.2, NC Department of Revenue) | late 50/day max 1,000; wrong format 200 |
| `nc.report.efile_spec.version` | 9-2026 (TY2026, use beginning January 2027) | 2027-01-01 | open | US-NCS5-028 (A.2, NC Department of Revenue) | NC-3/W-2 fixed-field text file. |
| `nc.report.ui.quarterly_due` | Apr 30; Jul 31; Oct 31; Jan 31 | 2026-01-01 | open | US-NCS5-025 (A.2, NC Division of Employment Security (NC Department of Commerce)) | NCUI 101 via NCSUITS; electronic mandatory at 10+ wage items |
| `nc.newhire.report_days` | 20 days | 2026-01-01 | open | US-NCS5-020 (A.1, NC General Assembly (General Statutes, official host ncleg.gov)) | or twice monthly 12-16 days apart electronically |

Rules:

- Third-party and POA: NCDOR GEN-58 (withholding) and the DES Power of Attorney (UI). (US-NCP51-003, US-FIL-013)

- Not configured in this release (open gap RQ-077): Whether the North Carolina W-2 file in eNC3 uses the federal EFW2 layout or a state layout is not confirmed; the current state specification was not obtained.

## NC.6 Leave

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nc.leave.sick.state_statute.exists` | False | 2023-10-03 | open | US-NCS5-001 (A.1, NC General Assembly (General Statutes, official host ncleg.gov)) | local mandates preempted |

- Not configured in this release (open gap RQ-078): Jury-duty, voting and other leave with pay impact not searched.

## NC.7 Termination and final pay

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nc.final_pay.rule` | next regular payday (discharge and resignation) | 2026-01-01 | open | US-NCS5-006 (A.1, NC General Assembly (General Statutes, official host ncleg.gov)) | bonuses/commissions first payday after calculable |
| `nc.term.vacation.payout` | per employer policy; forfeiture only with advance written notice | 2026-01-01 | open | US-NCS5-008 (A.1, NC General Assembly (General Statutes, official host ncleg.gov)) | - |
| `nc.term.final_w2.days` | 30 days | 2026-01-01 | open | US-NC-001 (A.2, NC Department of Revenue) | after final wage payment |

- Not configured in this release (open gap RQ-079): Whether NC employers must hand separating employees a UI-availability notice is not confirmed.

## NC.8 Benefits in kind and taxable wages

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nc.bik.conformity.irc_date` | 2025-07-05 | 2026-01-01 | open | US-NCS5-029 (A.2, NC Department of Revenue) | S.L. 2026-31; withholding follows IRC 3401 (US-NCS5-012) |

## NC.9 Deductions and garnishments

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nc.garn.support.max_rate` | 40 percent | 2026-01-01 | open | US-NCS5-018 (A.1, NC General Assembly (General Statutes, official host ncleg.gov)) | of monthly disposable earnings; 1 USD fee per pay period |
| `nc.garn.support.employer_fee.per_period` | 1 USD | 2026-01-01 | open | US-NCS5-018 (A.1, NC General Assembly (General Statutes, official host ncleg.gov)) | - |
| `nc.garn.tax_levy.max_rate` | 10 percent | 2026-01-01 | open | US-NCS5-021 (A.1, NC General Assembly (General Statutes, official host ncleg.gov)) | G.S. 105-242(b) |

- Not configured in this release (open gap RQ-080): IV-D remittance timing and payor fee (110-136.5 to.8) not extracted.

## NC.10 Collective agreements and prevailing wage

Prevailing wage (public works) is an optional informational flag [US-OWN-009]: this guide documents prevailing-wage laws, thresholds and certified-payroll duties as an overlay, and the payroll build does not produce certified payroll reports.

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nc.prevailing_wage.exists` | False | 2026-01-01 | open | US-NCP51-004 (A.2, US Department of Labor Wage and Hour Division) | DOL WHD state table |

Rules:

- NC has no state prevailing-wage law (DOL WHD state table). So there is no state certified-payroll duty; federal Davis-Bacon applies on federal projects (the federal reference). (US-NCP51-004)

## NC.11 Indexation

Indexation of each value is stated in the note of the value concerned.

## NC.12 Payroll data protection and records

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nc.records.wage_hour.retention_years` | 3 years | 1980-11-01 | open | US-NCS5-022 (A.1, NC Office of Administrative Hearings - NC Administrative Code (13 NCAC 12, NC Department of Labor rules)) | 13 NCAC 12.0802 |
| `nc.records.withholding.retention_years` | 10 years | 2026-01-01 | open | US-NC-001 (A.2, NC Department of Revenue) | NC-30 s.26 |
| `nc.data.ssn.mailing_restricted` | True | 2026-01-01 | open | US-NCS5-016 (A.1, NC General Assembly (General Statutes, official host ncleg.gov)) | 75-62; safe build truncates SSN on mailed stubs |

- Not configured in this release (open gap RQ-081): G.S. 75-65 breach notice not read.

## NC.13 Live legal change

No North Carolina rule is configured in this domain; the federal treatment in the federal reference applies.

## NC.14 Authority worked examples (oracle values)

No authority worked example is reproduced in this annex; recomputed withholding examples are in Module 12.

## NC.15 Special populations

- Domestic / household: No NC withholding required (voluntary agreement possible); Exempt from state minimum wage, overtime and youth rules (FLSA applies). (US-NC-001, US-NCS5-009)
- Minors: Youth employment certificate; school-night hours limit. (US-NCS5-004)
- Tipped: tips withheld as supplemental. (US-NCS5-002, US-NC-001)
- Nonresident aliens: treaty-exempt wages exempt. (US-NC-001)
- Government employees: Only minimum wage and a few Wage and Hour Act provisions apply to public employers. (US-NC-001, US-NCS5-009)
- Not configured in this release (open gap RQ-082): Thresholds, amounts or conditions for these populations are stated in the sources read without a confirmed value record and are not configured from this annex: Domestic / household; Agricultural; Tipped; Clergy / religious; Students; Nonresident aliens; Statutory employees; Government employees; Military spouses (SCRA); Interstate rail, motor carrier, airline; Tribal members on reservation; Seamen.

## NC.16 Language

- The pay statement and all filings are in English (owner decision US-OWN-006).

## NC.S Sources

| Source | Authority |
|---|---|
| US-NC-001 | NC Department of Revenue |
| US-NCB5-401 | NC Division of Employment Security |
| US-NCP51-001 | North Carolina General Assembly |
| US-NCP51-002 | North Carolina Department of Revenue |
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


## Fact index

Every value above with its key, effective period and register id.

| Key | Value | Effective | Register id |
|---|---|---|---|
| `fed.minwage.hourly` | 7.25 | from 2009-07-24 | US-FEDS5-017 |
| `nc.bik.conformity.irc_date` | 2025-07-05 | from 2026-01-01 | US-NCS5-029 |
| `nc.data.ssn.mailing_restricted` | True | from 2026-01-01 | US-NCS5-016 |
| `nc.final_pay.rule` | next regular payday (discharge and resignation) | from 2026-01-01 | US-NCS5-006 |
| `nc.garn.support.employer_fee.per_period` | 1 | from 2026-01-01 | US-NCS5-018 |
| `nc.garn.support.max_rate` | 40 | from 2026-01-01 | US-NCS5-018 |
| `nc.garn.tax_levy.max_rate` | 10 | from 2026-01-01 | US-NCS5-021 |
| `nc.labour.minwage.state.follows_federal` | True | from 2006-08-23 | US-NCS5-002 |
| `nc.labour.pay_frequency.allowed` | daily; weekly; biweekly; semimonthly; monthly | from 2026-01-01 | US-NCS5-005 |
| `nc.leave.sick.state_statute.exists` | False | from 2023-10-03 | US-NCS5-001 |
| `nc.local_mandates.preempted` | True | from 2023-10-03 | US-NCS5-001 |
| `nc.local_wage_tax.exists` | False | from 2026-01-01 | US-NCP51-001 |
| `nc.newhire.report_days` | 20 | from 2026-01-01 | US-NCS5-020 |
| `nc.oracle.weekly_450_s2.withholding` | 4.44 | from 2026-01-01 | US-NC-001 |
| `nc.overtime.premium.multiplier` | 1.5 | from 1991-06-19 | US-NCS5-003 |
| `nc.overtime.weekly_threshold_hours` | 40 | from 1991-06-19 | US-NCS5-003 |
| `nc.payslip.items` | itemized statement of deductions each pay period with deductions; wage notice at hire | from 2026-01-01 | US-NCW1B-003 |
| `nc.pit.allowance.amount` | 2500 | from 2026-01-01 to 2026-12-31 | US-NC-001 |
| `nc.pit.nra.addon.biweekly` | 21 | from 2026-01-01 to 2026-12-31 | US-NC-001 |
| `nc.pit.nra.addon.monthly` | 44 | from 2026-01-01 to 2026-12-31 | US-NCP51-002 |
| `nc.pit.nra.addon.semimonthly` | 22 | from 2026-01-01 to 2026-12-31 | US-NC-001 |
| `nc.pit.nra.addon.weekly` | 11 | from 2026-01-01 to 2026-12-31 | US-NC-001 |
| `nc.pit.oracle.example_1.withholding` | 4 | from 2026-01-01 to 2026-12-31 | US-NC-001 |
| `nc.pit.oracle.example_2.nra_withholding` | 21 | from 2026-01-01 to 2026-12-31 | US-NC-001 |
| `nc.pit.rate.flat` | 3.99 | from 2026-01-01 | US-NCS5-011 |
| `nc.pit.rounding` | nearest whole dollar (NRA add-on rounded up) | from 2026-01-01 to 2026-12-31 | US-NC-001 |
| `nc.pit.std_deduction.head_of_household` | 19125 | from 2026-01-01 | US-NCS5-010 |
| `nc.pit.std_deduction.mfj` | 25500 | from 2026-01-01 | US-NCS5-010 |
| `nc.pit.std_deduction.single` | 12,750 | from 2026-01-01 | US-NCS5-010 |
| `nc.pit.std_deduction.single` | 12750 | from 2026-01-01 | US-NCS5-010 |
| `nc.pit.wh.rate` | 4.09 | from 2026-01-01 to 2026-12-31 | US-NC-001 |
| `nc.prevailing_wage.exists` | False | from 2026-01-01 | US-NCP51-004 |
| `nc.reciprocity.states` | none | from 2026-01-01 | US-NC-001 |
| `nc.records.wage_hour.retention_years` | 3 | from 1980-11-01 | US-NCS5-022 |
| `nc.records.withholding.retention_years` | 10 | from 2026-01-01 | US-NC-001 |
| `nc.report.efile_spec.version` | 9-2026 (TY2026, use beginning January 2027) | from 2027-01-01 | US-NCS5-028 |
| `nc.report.nc3.due` | January 31, electronic (eNC3) | from 2026-01-01 | US-NC-001 |
| `nc.report.ui.quarterly_due` | Apr 30; Jul 31; Oct 31; Jan 31 | from 2026-01-01 | US-NCS5-025 |
| `nc.report.wh.quarterly_threshold.monthly_avg` | 250 | from 2026-01-01 | US-NC-001 |
| `nc.report.wh.semiweekly_threshold.monthly_avg` | 2000 | from 2026-01-01 | US-NC-001 |
| `nc.sui.employee.rate` | 0 | from 2026-01-01 | US-NCS5-014 |
| `nc.sui.employer.rate.max` | 5.76 | from 2026-01-01 to 2026-12-31 | US-NCP9V-001 |
| `nc.sui.employer.rate.min` | 0.06 | from 2026-01-01 to 2026-12-31 | US-NCP9V-001 |
| `nc.sui.new_employer.rate` | 1.0 | from 2026-01-01 to 2026-12-31 | US-NCS5-014 |
| `nc.sui.wage_base` | 34200 | from 2026-01-01 to 2026-12-31 | US-NCB5-401 |
| `nc.sui.wage_base.other_state_credit` | True | from 2026-01-01 | US-NCS5-015 |
| `nc.term.final_w2.days` | 30 | from 2026-01-01 | US-NC-001 |
| `nc.term.vacation.payout` | per employer policy; forfeiture only with advance written notice | from 2026-01-01 | US-NCS5-008 |
| `nc.ui.rate.base` | 1.9 | from 2026-01-01 to 2026-12-31 | US-NCP9V-001 |
| `nc.wh.certificate` | no NC-4: single, zero allowances; federal W-4 not acceptable | from 2026-01-01 | US-NC-001 |
| `nc.wh.supplemental.rate` | 4.09 | from 2026-01-01 to 2026-12-31 | US-NC-001 |
