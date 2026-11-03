# Annex MT: Montana


United States Country Configuration Guide, jurisdiction annex MT. Tax year 2026; currency USD (two decimal places).

**Scope of this annex.**

This annex holds the Montana layer only. The federal layer (federal income tax withholding, Social Security and Medicare, federal unemployment tax, Forms W-4, W-2, 941 and 940) is in Annex FED, and the rules for employees who live and work in different jurisdictions (sourcing, resident credits, reciprocity mechanics) are in Annex MULTI. Neither is repeated here. Independent contractors and Form 1099-NEC reporting are out of scope (owner instruction of 2026-10-29) [US-OWN-008]. The pay statement is issued in English.

In every table, *Valid from* and *Valid to* give the period in which the value applies (*open* means no end date has been published), and *Source* is the identifier of the row in the legal-basis register, with the authority and address listed in section MT.S (the source address is held in the register row). Items marked as a research gap are not yet confirmed and must not be configured from this annex.

**Jurisdiction layer.**

| Item | Value |
|---|---|
| Annex tier | T3 (verified) |
| Basis | 2026 formula (HB 337) [US-MTP51-001/-002]; local governments may not tax income, MCA 7-1-112 [US-MTP52-001] |

Tier key: T1 = no state wage tax (unemployment insurance and levies only); T3 = state withholding with no local layer remitted separately; T4 = a local layer remitted to a separate local authority on its own return.

**Configuration decisions.**

- Unemployment wages include cafeteria-plan salary reductions ([[FACT:mt.sui.wages.section125_included=True]]) and 401(k) deferrals ([[FACT:mt.sui.wages.401k_included=True]]), unlike the income-tax base.
- Accrued vacation must be paid at separation: [[FACT:mt.leave.vacation.payout_at_separation=True]].
- Withholding is rounded up to the next whole dollar, not to the nearest dollar (`mt.wh.method`).
- The 2027 minimum wage is not confirmed and is not configured (blocking gap in section MT.1).

## MT.1 Employment and labour code

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mt.minwage.hourly` | [[FACT:mt.minwage.hourly=10.85]] USD | 2026-01-01 | 2026-12-31 | US-MTS5-014 (A.2, Montana Department of Labor and Industry, Employment Relations Division) | Indexed: 10.55 x 1.0292 = 10.86, rounded to the nearest 0.05 = [[FACT:mt.minwage.hourly=10.85]] (US-MTS5-016). |
| `mt.labour.minwage.small_business.hourly` | [[FACT:mt.labour.minwage.small_business.hourly=4.0]] USD | 2026-01-01 | open | US-MTS5-004 (A.1, Montana Legislature (MCA 2025)) | non-FLSA business with annual gross sales <= 110,000; FLSA-covered individual gets the higher rate |
| `mt.minwage.indexation` | [[FACT:mt.minwage.indexation=CPI-U US city average Aug/Aug; set by 30 Sep; effective 1 Jan; nearest 0.05]] | 2026-01-01 | open | US-MTS5-004 (A.1, Montana Legislature (MCA 2025)) | 39-3-409 |
| `mt.minwage.tip_credit.allowed` | [[FACT:mt.minwage.tip_credit.allowed=False]] | 2026-01-01 | 2026-12-31 | US-MTS5-014 (A.2, Montana Department of Labor and Industry, Employment Relations Division) | no tip credit, training wage or meal credit |
| `mt.overtime.weekly_threshold_hours` | [[FACT:mt.overtime.weekly_threshold_hours=40]] hours | 2026-01-01 | open | US-MTS5-003 (A.1, Montana Legislature (MCA 2025)) | 1.5x; no daily OT; not for farm workers |
| `mt.overtime.premium.multiplier` | [[FACT:mt.overtime.premium.multiplier=1.5]] ratio | 2026-01-01 | open | US-MTS5-003 (A.1, Montana Legislature (MCA 2025)) | - |
| `mt.labour.overtime.computer_employee_threshold.hourly` | [[FACT:mt.labour.overtime.computer_employee_threshold.hourly=27.63]] USD | 2026-01-01 | open | US-MTS5-006 (A.1, Montana Legislature (MCA 2025)) | fixed in statute |
| `mt.labour.pay_timing.max_business_days_after_due` | [[FACT:mt.labour.pay_timing.max_business_days_after_due=10]] days | 2009-10-01 | open | US-MTS5-001 (A.1, Montana Legislature (MCA 2025)) | semimonthly presumed if no period established |
| `mt.labour.direct_deposit.consent_required` | [[FACT:mt.labour.direct_deposit.consent_required=True]] | 2009-10-01 | open | US-MTS5-001 (A.1, Montana Legislature (MCA 2025)) | cannot be required |
| `mt.labour.late_wage_penalty.max` | [[FACT:mt.labour.late_wage_penalty.max=110]] percent | 2026-01-01 | open | US-MTS5-019 (A.1, Montana Legislature (MCA 2025)) | 39-3-206; DLI applies 55% under ARM 24.16.7566 (rule not read) |

- Not yet published (expected autumn 2026, before the 2027-01-01 effective date) [[GAP:RQ-065]]: The 2027 Montana minimum wage is derived only; the Department of Labor and Industry's 2027 notice could not be read. The 2027 rate is not written and must not be configured.
- Not configured in this release [[GAP:RQ-066]]: The paycard rules, the written-authorisation rule for deductions and the wage-and-hour record retention period were not read (the state rules site was unreachable).

## MT.2 Income tax withholding

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mt.pit.bracket.1.ceiling.single` | [[FACT:mt.pit.bracket.1.ceiling.single=47500]] USD | 2026-01-01 | 2026-12-31 | US-MTS5-022 (A.1, Montana Legislature (MCA 2025)) | statutory: [[FACT:mt.pit.bracket.1.ceiling.hoh=71,250]] HoH, 95,000 joint |
| `mt.pit.bracket.1.ceiling.single` | [[FACT:mt.pit.bracket.1.ceiling.single=65000]] USD | 2027-01-01 | open | US-MTS5-022 (A.1, Montana Legislature (MCA 2025)) | enacted; [[FACT:mt.pit.bracket.1.ceiling.hoh=97,500]] HoH; 130,000 joint |
| `mt.pit.bracket.1.ceiling.hoh` | [[FACT:mt.pit.bracket.1.ceiling.hoh=71250]] USD | 2026-01-01 | 2026-12-31 | US-MTS5-022 (A.1, Montana Legislature (MCA 2025)) | - |
| `mt.pit.bracket.1.ceiling.hoh` | [[FACT:mt.pit.bracket.1.ceiling.hoh=97500]] USD | 2027-01-01 | open | US-MTS5-022 (A.1, Montana Legislature (MCA 2025)) | - |
| `mt.pit.bracket.1.ceiling.joint` | [[FACT:mt.pit.bracket.1.ceiling.joint=95000]] USD | 2026-01-01 | 2026-12-31 | US-MTS5-022 (A.1, Montana Legislature (MCA 2025)) | - |
| `mt.pit.bracket.1.ceiling.joint` | [[FACT:mt.pit.bracket.1.ceiling.joint=130000]] USD | 2027-01-01 | open | US-MTS5-022 (A.1, Montana Legislature (MCA 2025)) | - |
| `mt.pit.bracket.1.rate` | [[FACT:mt.pit.bracket.1.rate=4.7]] percent | 2026-01-01 | open | US-MTS5-022 (A.1, Montana Legislature (MCA 2025)) | - |
| `mt.pit.bracket.2.rate` | [[FACT:mt.pit.bracket.2.rate=5.65]] percent | 2026-01-01 | 2026-12-31 | US-MTS5-022 (A.1, Montana Legislature (MCA 2025)) | HB 337 |
| `mt.pit.bracket.2.rate` | [[FACT:mt.pit.bracket.2.rate=5.4]] percent | 2027-01-01 | open | US-MTS5-022 (A.1, Montana Legislature (MCA 2025)) | enacted; 2027 withholding tables not published |
| `mt.pit.agricultural.withholding_required` | [[FACT:mt.pit.agricultural.withholding_required=False]] | 2026-01-01 | open | US-MTS5-005 (A.2, Montana Department of Revenue) | cannabis workers are not agricultural |
| `mt.wh.method` | [[FACT:mt.wh.method=annual formula W = A + B(G - C); federal standard deduction; no MT allowances; round UP to next dollar]] | 2026-01-01 | 2026-12-31 | US-MTP51-001 (A.2, Montana Department of Revenue) | Form MW-4 |
| `mt.pit.wh.single.1.ceiling` | [[FACT:mt.pit.wh.single.1.ceiling=16100]] USD | 2026-01-01 | 2026-12-31 | US-MTP51-001 (A.2, Montana Department of Revenue) | 0% up to [[FACT:mt.pit.wh.single.1.ceiling=16,100]] (= federal std deduction single) |
| `mt.pit.wh.single.2.rate` | [[FACT:mt.pit.wh.single.2.rate=4.7]] percent | 2026-01-01 | 2026-12-31 | US-MTP51-001 (A.2, Montana Department of Revenue) | [[FACT:mt.pit.wh.single.1.ceiling=16,100]]-[[FACT:mt.pit.wh.single.2.ceiling=63,600]] |
| `mt.pit.wh.single.2.ceiling` | [[FACT:mt.pit.wh.single.2.ceiling=63600]] USD | 2026-01-01 | 2026-12-31 | US-MTP51-001 (A.2, Montana Department of Revenue) | [[FACT:mt.pit.wh.single.1.ceiling=16,100]] + [[FACT:mt.pit.bracket.1.ceiling.single=47,500]] (US-MTS5-022) |
| `mt.pit.wh.single.3.rate` | [[FACT:mt.pit.wh.single.3.rate=5.65]] percent | 2026-01-01 | 2026-12-31 | US-MTP51-001 (A.2, Montana Department of Revenue) | - |
| `mt.pit.wh.single.3.base_tax` | [[FACT:mt.pit.wh.single.3.base_tax=2233]] USD | 2026-01-01 | 2026-12-31 | US-MTP51-001 (A.2, Montana Department of Revenue) | [[FACT:mt.pit.bracket.1.rate=4.7]]% x [[FACT:mt.pit.bracket.1.ceiling.single=47,500]] = 2,232.5 rounded up |
| `mt.wh.supplemental.rate` | [[FACT:mt.wh.supplemental.rate=5]] percent | 2026-01-01 | open | US-MTP51-001 (A.2, Montana Department of Revenue) | when paid separately, or aggregate |

- Not configured in this release [[GAP:RQ-067]]: The 2027 withholding formula and tables are not yet published.

## MT.2b Non-resident regime and reciprocity

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mt.pit.nra.treaty_at_withholding` | [[FACT:mt.pit.nra.treaty_at_withholding=False]] | 2026-01-01 | open | US-MTS5-005 (A.2, Montana Department of Revenue) | treaty exclusions decided at assessment; H-2A exempt from withholding |
| `mt.pit.nonresident.days_exemption` | [[FACT:mt.pit.nonresident.days_exemption=30]] days | 2026-01-01 | open | US-MTP51-003 (A.2, Montana Department of Revenue) | fewer than 30 days in MT and works in more than one state; excludes athletes, entertainers, construction, key employees (>500,000) |
| `mt.reciprocity.states` | [[FACT:mt.reciprocity.states=ND]] | 2026-01-01 | open | US-MTP51-004 (A.2, Montana Department of Revenue) | MW-4 line 5 via TAP, renewed each year by 31 Jan |

## MT.2c Local wage taxes

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mt.local_wage_tax.exists` | [[FACT:mt.local_wage_tax.exists=False]] | 2026-01-01 | open | US-MTP52-001 (A.1, Montana Legislature (MCA)) | MCA 7-1-112 |

## MT.3 Social insurance: unemployment, disability, paid leave and payroll levies

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mt.ui.admin_fund_tax.rate` | [[FACT:mt.ui.admin_fund_tax.rate=0.18]] percent | 2026-01-01 | 2026-12-31 | US-MTP7-001 (A.2, MT official authority) | 0.13 for eligible classes 1-2 |
| `mt.ui.admin_fund_tax.rate_class_1_2` | [[FACT:mt.ui.admin_fund_tax.rate_class_1_2=0.13]] percent | 2026-01-01 | 2026-12-31 | US-MTP7-001 (A.2, MT official authority) | - |
| `mt.sui.employee.rate` | [[FACT:mt.sui.employee.rate=0]] percent | 2026-01-01 | open | US-MTS5-023 (A.1, Montana Legislature (MCA 2025)) | no deduction from wages |
| `mt.sui.wages.section125_included` | [[FACT:mt.sui.wages.section125_included=True]] | 2026-01-01 | open | US-MTS5-023 (A.1, Montana Legislature (MCA 2025)) | also 401(k) deferrals, 129, officer pay, company vehicle personal use, room and board |
| `mt.sui.wages.401k_included` | [[FACT:mt.sui.wages.401k_included=True]] | 2026-01-01 | open | US-MTS5-023 (A.1, Montana Legislature (MCA 2025)) | - |
| `mt.sui.wage_base.other_state_credit` | [[FACT:mt.sui.wage_base.other_state_credit=False]] | 2025-07-01 | open | US-MTS5-025 (A.3, Montana Department of Labor and Industry, Unemployment Insurance Division) | MT does not use other-state wages for excess wages |
| `mt.sui.wage_base` | [[FACT:mt.sui.wage_base=47300]] USD | 2026-01-01 | 2026-12-31 | US-MTP51-005 (A.2, Montana Department of Labor and Industry, UI Division) | 0.8 x 59,106.64 = 47,285.31 -> [[FACT:mt.sui.wage_base=47,300]] (US-MTS5-024) |
| `mt.sui.employer.rate.min` | [[FACT:mt.sui.employer.rate.min=0.0]] percent | 2026-01-01 | 2026-12-31 | US-MTP51-005 (A.2, Montana Department of Labor and Industry, UI Division) | schedule 1 |
| `mt.sui.employer.rate.max` | [[FACT:mt.sui.employer.rate.max=6.12]] percent | 2026-01-01 | 2026-12-31 | US-MTP51-005 (A.2, Montana Department of Labor and Industry, UI Division) | penalty rate 50% higher |
| `mt.ui.rate.new_employer.min` | [[FACT:mt.ui.rate.new_employer.min=1.0]] percent | 2026-01-01 | 2026-12-31 | US-MTP51-005 (A.2, Montana Department of Labor and Industry, UI Division) | 1.00-2.00 by industry |
| `mt.ui.rate.new_employer.construction` | [[FACT:mt.ui.rate.new_employer.construction=2.0]] percent | 2026-01-01 | 2026-12-31 | US-MTP51-005 (A.2, Montana Department of Labor and Industry, UI Division) | services 1.10, agriculture/mining 1.30 |
| `mt.sdi_pfml.exists` | [[FACT:mt.sdi_pfml.exists=False]] | 2026-01-01 | open | US-MTP52-002 (A.1, Montana Legislature (MCA)) | no SDI/TDI/PFML |

Rules:

- No employee UI contribution. Employers may not deduct UI from wages. (US-MTP52-003, US-MTS5-023)

## MT.4 Pay statement

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mt.payslip.items` | [[FACT:mt.payslip.items=itemized statement of state and federal income tax, social security and other deductions each payment]] | 2026-01-01 | open | US-MTP51-006 (A.1, Montana Legislature (MCA)) | 39-3-101; narrow statute (no gross/hours/rate requirement) |

Rules:

- No Montana provision on electronic delivery or consent for pay statements was located.
- No gross/hours/rate content requirement exists beyond deductions. This is a narrow statute.
- Multistate reach: "all employers in this state" when paying employees. No out-of-state reach rule located.

## MT.5 Statutory reporting

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mt.report.wh.accelerated_threshold` | [[FACT:mt.report.wh.accelerated_threshold=12000]] USD | 2026-01-01 | open | US-MTS5-005 (A.2, Montana Department of Revenue) | lookback 1 Jul-30 Jun; 1,200-11,999 monthly by 15th; <=1,199 annual by 31 Jan |
| `mt.report.wh.monthly_threshold` | [[FACT:mt.report.wh.monthly_threshold=1200]] USD | 2026-01-01 | open | US-MTS5-005 (A.2, Montana Department of Revenue) | - |
| `mt.report.mw3.due` | [[FACT:mt.report.mw3.due=31 January (MW-3 + all W-2s)]] | 2026-01-01 | open | US-MTS5-005 (A.2, Montana Department of Revenue) | federal W-3 and truncated SSNs not accepted; EFW2 via TAP |
| `mt.report.ui.quarterly_due` | [[FACT:mt.report.ui.quarterly_due=Apr 30; Jul 31; Oct 31; Jan 31]] | 2025-07-01 | open | US-MTS5-025 (A.3, Montana Department of Labor and Industry, Unemployment Insurance Division) | electronic mandatory from 2025-07-01 |
| `mt.newhire.report_days` | [[FACT:mt.newhire.report_days=20]] days | 2026-01-01 | open | US-MTS5-012 (A.1, Montana Legislature (MCA 2025)) | DPHHS; electronic twice a month 12-16 days apart |

- Not configured in this release [[GAP:RQ-068]]: UI quarterly report file format not obtained.

## MT.6 Leave

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mt.leave.vacation.payout_at_separation` | [[FACT:mt.leave.vacation.payout_at_separation=True]] | 2026-01-01 | open | US-MTS5-018 (A.3, Montana Department of Labor and Industry, Office of Administrative Hearings) | accrued vacation is wages, cannot be forfeited (Langager v. Crazy Creek, 1998 MT 44) - read via DLI decision only (A.3) |
| `mt.leave.sick.state_statute.exists` | [[FACT:mt.leave.sick.state_statute.exists=False]] | 2026-01-01 | open | US-MTP52-002 (A.1, Montana Legislature (MCA)) | no private-sector statute |

- Not configured in this release [[GAP:RQ-069]]: Public-employee sick leave (2-18-618) and child-labour hours not read.
- Not configured in this release [[GAP:RQ-070]]: The Langager v. Crazy Creek decision was read only through the Department of Labor and Industry's decision, not in the court's own text.

## MT.7 Termination and final pay

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mt.term.final_pay.quit` | [[FACT:mt.term.final_pay.quit=next regular payday or 15 days, whichever first]] | 2026-01-01 | open | US-MTS5-002 (A.1, Montana Legislature (MCA 2025)) | 39-3-205 |
| `mt.final_pay.discharge` | [[FACT:mt.final_pay.discharge=immediately (policy may extend to next payday or 15 days)]] | 2026-01-01 | open | US-MTS5-002 (A.1, Montana Legislature (MCA 2025)) | DLI reads immediately as 4 hours or end of business day (US-MTS5-014) |

## MT.8 Benefits in kind and taxable wages

Rules:

- Income-tax withholding follows federal: "if a class of employment or service is subject to wage withholding for federal purposes, it is also subject to Montana wage withholding". (US-MTS5-005)

- Not configured in this release [[GAP:RQ-071]]: Income-tax departures from the federal exclusions (HSA, cafeteria plans, transit) were not checked in the statute.

## MT.9 Deductions and garnishments

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mt.garn.creditor.max_percent` | [[FACT:mt.garn.creditor.max_percent=25]] percent | 2026-01-01 | open | US-MTS5-009 (A.1, Montana Legislature (MCA 2025)) | or excess over 30x FMW; mirrors CCPA |
| `mt.garn.iwo.employer_fee.monthly` | [[FACT:mt.garn.iwo.employer_fee.monthly=5]] USD | 2026-01-01 | open | US-MTS5-013 (A.1, Montana Legislature (MCA 2025)) | if department allows; remit same month |

## MT.10 Collective agreements and prevailing wage

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mt.prevailing_wage.threshold` | [[FACT:mt.prevailing_wage.threshold=25000]] USD | 2026-01-01 | open | US-MTS5-010 (A.1, Montana Legislature (MCA 2025)) | public works incl. nonconstruction services; weekly pay required (US-MTS5-011) |
| `mt.prevailing_wage.pay_frequency` | [[FACT:mt.prevailing_wage.pay_frequency=weekly]] | 2026-01-01 | open | US-MTS5-011 (A.1, Montana Legislature (MCA 2025)) | - |

## MT.11 Indexation

Indexation of each value is stated in the note of the value concerned.

## MT.12 Payroll data protection and records

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mt.records.payroll_tax.retention_years` | [[FACT:mt.records.payroll_tax.retention_years=5]] years | 2026-01-01 | open | US-MTS5-005 (A.2, Montana Department of Revenue) | ARM 42.17.203 via DOR guide |
| `mt.data.w2.truncated_ssn_rejected` | [[FACT:mt.data.w2.truncated_ssn_rejected=True]] | 2026-01-01 | open | US-MTS5-005 (A.2, Montana Department of Revenue) | - |

Rules:

- No Montana rule requiring SSN truncation on pay statements was located.
- DOR rejects truncated SSNs on W-2s filed with the MW-3. (US-MTS5-005)
- Montana's identity-theft law requires destruction of records that are no longer needed, and breach notice to residents and to the AG (data elements include SSN and TIN). (US-MTS5-020)

## MT.13 Live legal change

No Montana rule is configured in this domain; the federal treatment in Annex FED applies.

## MT.14 Authority worked examples (oracle values)

No authority worked example is reproduced in this annex; recomputed withholding examples are in Module 12.

## MT.15 Special populations

- Domestic/household: excluded if employed by family or guardian. (US-MTS5-006, US-MTS5-021, US-MTS5-025)
- Tipped: No tip credit; UI taxes reported tips. (US-MTS5-014, US-MTS5-019, US-MTS5-025)
- Clergy/religious: Withholding follows federal (minister exempt from federal withholding, no state rule beyond that); UI excludes ministers and religious-order members. (US-MTS5-005, US-MTS5-021, US-MTS5-025)
- Nonresident aliens: Withheld like other employees; Treaty exclusion applied at assessment only; H-2A exempt from withholding; UI excludes F/H-2A/J/M/Q. (US-MTS5-005, US-MTS5-021)
- Statutory employees / officers: Direct sellers excluded (min wage and UI); Corporate officers are UI employees (including S corp). (US-MTS5-006, US-MTS5-021, US-MTS5-025)
- Government: US federal employees excluded from Montana minimum wage/OT. State/local work-period overtime rules; UI: reimbursable option for government and tribes. (US-MTS5-006, US-MTS5-023)
- Military / Guard / spouses: Active duty exempt. (US-MTS5-005)
- Not configured in this release [[GAP:RQ-072]]: Thresholds, amounts or conditions for these populations are stated in the sources read without a confirmed value record and are not configured from this annex: Domestic/household; Agricultural; Minors; Tipped; Students; Tribal members; Military / Guard / spouses; Small non-FLSA business.

## MT.16 Language

- The pay statement and all filings are in English (owner decision US-OWN-006).

## MT.S Sources

| Source | Authority |
|---|---|
| US-MTP51-001 | Montana Department of Revenue |
| US-MTP51-003 | Montana Department of Revenue |
| US-MTP51-004 | Montana Department of Revenue |
| US-MTP51-005 | Montana Department of Labor and Industry, UI Division |
| US-MTP51-006 | Montana Legislature (MCA) |
| US-MTP52-001 | Montana Legislature (MCA) |
| US-MTP52-002 | Montana Legislature (MCA) |
| US-MTP7-001 | MT official authority |
| US-MTS5-001 | Montana Legislature (MCA 2025) |
| US-MTS5-002 | Montana Legislature (MCA 2025) |
| US-MTS5-003 | Montana Legislature (MCA 2025) |
| US-MTS5-004 | Montana Legislature (MCA 2025) |
| US-MTS5-005 | Montana Department of Revenue |
| US-MTS5-006 | Montana Legislature (MCA 2025) |
| US-MTS5-009 | Montana Legislature (MCA 2025) |
| US-MTS5-010 | Montana Legislature (MCA 2025) |
| US-MTS5-011 | Montana Legislature (MCA 2025) |
| US-MTS5-012 | Montana Legislature (MCA 2025) |
| US-MTS5-013 | Montana Legislature (MCA 2025) |
| US-MTS5-014 | Montana Department of Labor and Industry, Employment Relations Division |
| US-MTS5-018 | Montana Department of Labor and Industry, Office of Administrative Hearings |
| US-MTS5-019 | Montana Legislature (MCA 2025) |
| US-MTS5-022 | Montana Legislature (MCA 2025) |
| US-MTS5-023 | Montana Legislature (MCA 2025) |
| US-MTS5-025 | Montana Department of Labor and Industry, Unemployment Insurance Division |
