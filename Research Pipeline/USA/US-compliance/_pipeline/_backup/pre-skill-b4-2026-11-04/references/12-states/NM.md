# Annex NM: New Mexico


United States Country Configuration Guide, jurisdiction annex NM. Tax year 2026; currency USD (two decimal places).

**Scope of this annex.**

This annex holds the New Mexico layer only. The federal layer (federal income tax withholding, Social Security and Medicare, federal unemployment tax, Forms W-4, W-2, 941 and 940) is in the federal reference, and the rules for employees who live and work in different jurisdictions (sourcing, resident credits, reciprocity mechanics) are in the multistate reference. Neither is repeated here. Independent contractors and Form 1099-NEC reporting are out of scope (owner instruction of 2026-10-29) [US-OWN-008]. The pay statement is issued in English.

In every table, *Valid from* and *Valid to* give the period in which the value applies (*open* means no end date has been published), and *Source* is the identifier of the row in the legal-basis register, with the authority and address listed in section NM.S (the source address is held in the legal-basis entry). Items marked as a research gap are not yet confirmed and must not be configured from this annex.

**Jurisdiction layer.**

| Item | Value |
|---|---|
| Annex tier | T3 (verified) |
| Basis | FYI-104 Rev. 11/2025 eff. 2026-01-01, graduated rates, top 5.9% [US-NMP52-001]; TRD list of all taxes has no local wage tax [US-NMP52-003] |

Tier key: T1 = no state wage tax (unemployment insurance and levies only); T3 = state withholding with no local layer remitted separately; T4 = a local layer remitted to a separate local authority on its own return.

**Configuration decisions.**

- The workers' compensation administration fee has an employee share of 2.25 USD a quarter, deducted from pay and reported on Form TRD-41431, next to the employer share of 2.55 USD.
- The garnishment floor follows the highest minimum wage that applies at the place of work, times 40.
- City and county minimum wages (Albuquerque, Santa Fe city, Las Cruces, Bernalillo County) are configured as dated rows; the Santa Fe County rate is a blocking gap (section NM.1).
- The reference withholding result of the 2026 method is 41.8 USD.

## NM.1 Employment and labour code

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nm.minwage.hourly` | 12.0 USD | 2023-01-01 | open | US-NMS5-004 (A.1, New Mexico Legislature (nmlegis.gov, via Wayback 2026id_)) | 50-4-22(A); not indexed; no 2026-session change found |
| `nm.labour.minwage.student.hourly` | 8.5 USD | 2020-01-01 | open | US-NMS5-004 (A.1, New Mexico Legislature (nmlegis.gov, via Wayback 2026id_)) | secondary-school students after school/out of session |
| `nm.minwage.tipped.cash_wage` | 3.0 USD | 2020-01-01 | open | US-NMS5-004 (A.1, New Mexico Legislature (nmlegis.gov, via Wayback 2026id_)) | >30 USD/month in tips; tips + cash reach minimum |
| `nm.overtime.weekly_threshold_hours` | 40 hours | 2020-01-01 | open | US-NMS5-004 (A.1, New Mexico Legislature (nmlegis.gov, via Wayback 2026id_)) | no daily OT |
| `nm.overtime.premium.multiplier` | 1.5 ratio | 2020-01-01 | open | US-NMS5-004 (A.1, New Mexico Legislature (nmlegis.gov, via Wayback 2026id_)) | - |
| `nm.labour.minwage.local.albuquerque.hourly` | 12.0 USD | 2026-01-01 | 2026-12-31 | US-NMS5-006 (A.2, City of Albuquerque, Legal Department) | - |
| `nm.labour.minwage.local.albuquerque.hourly` | 13.0 USD | 2027-01-01 | open | US-NMS5-006 (A.2, City of Albuquerque, Legal Department) | stays 12.00 with >=2,500/yr healthcare or childcare benefit |
| `nm.labour.minwage.local.albuquerque.tipped.hourly` | 7.2 USD | 2026-01-01 | open | US-NMS5-006 (A.2, City of Albuquerque, Legal Department) | 2026 and 2027 |
| `nm.labour.minwage.local.santa_fe_city.hourly` | 15.0 USD | 2025-03-01 | 2026-02-28 | US-NMS5-007 (A.2, City of Santa Fe, Office of Economic Development) | - |
| `nm.labour.minwage.local.santa_fe_city.hourly` | 15.4 USD | 2026-03-01 | 2026-12-31 | US-NMS5-007 (A.2, City of Santa Fe, Office of Economic Development) | 15.00 x 1.0268 = 15.402 -> 15.40 (reproduces) |
| `nm.labour.minwage.local.santa_fe_city.hourly` | 17.5 USD | 2027-01-01 | open | US-NMS5-007 (A.2, City of Santa Fe, Office of Economic Development) | from 2028-03-01: 50% Western CPI + 50% HUD FMR, cap 5% |
| `nm.labour.minwage.local.santa_fe_city.tipped_base.hourly` | 3.0 USD | 2026-03-01 | open | US-NMS5-007 (A.2, City of Santa Fe, Office of Economic Development) | tipped/commissioned >=100 USD/month |
| `nm.pay_frequency.rule` | paydays max 16 days apart; days 1-15 by 25th; 16-end by 10th of next month | 2026-01-01 | open | US-NMP8-001 (A.1, New Mexico Legislature (nmlegis.gov)) | exempt staff may be paid monthly |
| `nm.labour.direct_deposit.consent_required` | True | 2026-01-01 | open | US-NMP8-001 (A.1, New Mexico Legislature (nmlegis.gov)) | employer, employee and institution |
| `nm.labour.minwage.local.las_cruces.hourly` | 13.01 USD | 2026-01-01 | 2026-12-31 | US-NMB5-001 (A.2, City of Las Cruces) |  |
| `nm.labour.minwage.local.las_cruces.hourly` | 13.47 USD | 2027-01-01 | open | US-NMB5-001 (A.2, City of Las Cruces) | 2027 figure as published by the City (Ordinance 2726 CPI computation; higher of City or State). |
| `nm.labour.minwage.local.las_cruces.tipped.hourly` | 5.2 USD | 2026-01-01 | 2026-12-31 | US-NMB5-001 (A.2, City of Las Cruces) |  |
| `nm.labour.minwage.local.las_cruces.tipped.hourly` | 5.39 USD | 2027-01-01 | open | US-NMB5-001 (A.2, City of Las Cruces) |  |
| `nm.labour.minwage.local.bernalillo_county.hourly` | 10.95 USD | 2026-01-01 | 2026-12-31 | US-NMB5-002 (A.2, Bernalillo County, Planning & Development Services) | Unincorporated Bernalillo County ordinance rate; the State minimum 12.00 is higher and prevails, so no county figure above the State rate applies in 2026. |
| `nm.labour.minwage.local.santa_fe_county.hourly` | 15.0 USD | 2025-03-01 | 2026-02-28 | US-NMB5-301 (A.2, Santa Fe County, New Mexico) | Unincorporated Santa Fe County living wage (Ord. 2014-1 as amended), previous-rates table. |
| `nm.labour.minwage.local.santa_fe_county.hourly` | 15.4 USD | 2026-03-01 | open | US-NMB5-301 (A.2, Santa Fe County, New Mexico) | From 2026-03-01 (County news release 2026-02-12); adjusted each March 1 by CPI-W West. 15.40/15.00 = 1.0267. |
| `nm.labour.minwage.local.santa_fe_county.tipped_base.hourly` | 4.5 USD | 2025-03-01 | 2026-02-28 | US-NMB5-301 (A.2, Santa Fe County, New Mexico) |  |
| `nm.labour.minwage.local.santa_fe_county.tipped_base.hourly` | 4.62 USD | 2026-03-01 | open | US-NMB5-301 (A.2, Santa Fe County, New Mexico) | Tipped base = 30% of the living wage: 15.40 x 0.30 = 4.62; 15.00 x 0.30 = 4.50 (arithmetic check only, ratio not stated on the page). |

Rules:

- Local minimum wages. DWS lists five ordinances: Albuquerque, Bernalillo County, Las Cruces, City of Santa Fe and Santa Fe County. (US-NMS5-005)

- Not configured in this release (open gap RQ-119): No change to the state minimum wage for 2027 from the 2026 legislative session is confirmed.
- Not configured in this release (open gap RQ-579): The Santa Fe County rate from 2027-03-01 is set by CPI-W West and published in early 2027.

## NM.2 Income tax withholding

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nm.pit.tribal.exempt` | income wholly earned on own-tribe lands while living there | 2026-01-01 | open | US-NMS5-013 (A.2, New Mexico Taxation and Revenue Department) | - |
| `nm.wh.certificate` | no state form; optional federal W-4 copy marked For New Mexico State Withholding Only | 2026-01-01 | open | US-NMP52-001 (A.2, New Mexico Taxation and Revenue Department) | - |
| `nm.wh.method` | FYI-104 Rev. 11/2025 percentage tables; standard deduction built in; no allowances | 2026-01-01 | 2026-12-31 | US-NMP52-001 (A.2, New Mexico Taxation and Revenue Department) | no withholding if under 1 USD in a month |
| `nm.pit.wh.single.zero_bracket` | 8050 USD | 2026-01-01 | 2026-12-31 | US-NMP52-001 (A.2, New Mexico Taxation and Revenue Department) | annual |
| `nm.pit.wh.single.band_starts` | 0;5500;16500;33500;66500;210000 | 2026-01-01 | 2026-12-31 | US-NMP52-001 (A.2, New Mexico Taxation and Revenue Department) | taxable income above zero bracket; cumulative 82.50/434.50/1,165.50/2,716.50/9,748.00 reproduced |
| `nm.pit.wh.rates` | 1.5;3.2;4.3;4.7;4.9;5.9 | 2026-01-01 | 2026-12-31 | US-NMP52-001 (A.2, New Mexico Taxation and Revenue Department) | percent |
| `nm.pit.wh.rate.top` | 5.9 percent | 2026-01-01 | 2026-12-31 | US-NMP52-001 (A.2, New Mexico Taxation and Revenue Department) | - |
| `nm.wh.supplemental.rate` | 5.9 percent | 2026-01-01 | 2026-12-31 | US-NMP52-001 (A.2, New Mexico Taxation and Revenue Department) | when federal uses flat percentage; Table 8 for separate bonus/overtime |
| `nm.pit.oracle.example_1.withholding` | 41.8 USD | 2026-01-01 | 2026-12-31 | US-NMP52-001 (A.2, New Mexico Taxation and Revenue Department) | FYI-104 weekly, married, wages 1,000: the bracket base tax plus 4.3% of the 210 excess gives 21.80; adding the 20.00 extra withholding requested by the employee gives 41.80. |

- Not configured in this release (open gap RQ-120): 2027 FYI-104 not yet visible.

## NM.2b Non-resident regime and reciprocity

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nm.pit.nonresident.days_threshold` | 15 days | 2026-01-01 | open | US-NMP52-002 (A.2, New Mexico Taxation and Revenue Department) | no withholding for nonresidents working <=15 days in NM per year |
| `nm.reciprocity.states` | none | 2026-01-01 | open | US-NMP52-002 (A.2, New Mexico Taxation and Revenue Department) | resident credit at assessment |

## NM.2c Local wage taxes

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nm.local_wage_tax.exists` | False | 2026-10-29 | open | US-NMP52-003 (A.2, New Mexico Taxation and Revenue Department) | - |

## NM.3 Social insurance: unemployment, disability, paid leave and payroll levies

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nm.sui.employer.rate.min` | 0.33 percent | 2026-01-01 | 2026-12-31 | US-NMS5-008 (A.2, New Mexico Department of Workforce Solutions, UI Tax) | - |
| `nm.sui.employer.rate.max` | 5.4 percent | 2026-01-01 | 2026-12-31 | US-NMS5-008 (A.2, New Mexico Department of Workforce Solutions, UI Tax) | + excess-claims premium (rate-5.4)x10%, max 1% |
| `nm.ui.reserve_factor` | 3.6361 ratio | 2026-01-01 | 2026-12-31 | US-NMS5-008 (A.2, New Mexico Department of Workforce Solutions, UI Tax) | - |
| `nm.sui.employee.rate` | 0 percent | 2026-01-01 | open | US-NMS5-016 (A.3, New Mexico Department of Workforce Solutions) | deduction prohibited |
| `nm.wc.admin_fee.employer.quarterly` | 2.55 USD | 2025-07-01 | 2028-06-30 | US-NMR3-001 (A.2, NM Taxation and Revenue Department) | per employee per quarter on TRD-41431; then 2.68 to 2033-06-30 |
| `nm.wc.admin_fee.employer.quarterly` | 2.68 USD | 2028-07-01 | 2033-06-30 | US-NMR3-001 (A.2, NM Taxation and Revenue Department) | scheduled step |
| `nm.wc.admin_fee.employee.quarterly` | 2.25 USD | 2025-07-01 | 2028-06-30 | US-NMR3-001 (A.2, NM Taxation and Revenue Department) | payroll deduction; then 2.38 |
| `nm.wc.admin_fee.employee.quarterly` | 2.38 USD | 2028-07-01 | 2033-06-30 | US-NMR3-001 (A.2, NM Taxation and Revenue Department) | - |
| `nm.sdi_pfml.exists` | False | 2026-01-01 | open | US-NMR3-002 (A.2, NM Department of Workforce Solutions) | no PFML Act enacted |
| `nm.sui.wage_base` | 34800 USD | 2026-01-01 | 2026-12-31 | US-NMP51-001 (A.2, NM Department of Workforce Solutions) | 60% of state average earnings rounded up to 100 (not derivable) |
| `nm.ui.rate.new_employer.min` | 1.0 percent | 2026-01-01 | 2026-12-31 | US-NMP51-002 (A.2, NM Department of Workforce Solutions) | greater of NAICS average or 1%; 2026 range 1.00-1.28 |

- Not configured in this release (open gap RQ-121): SUI other-state wage credit and 51-1-42(F) exclusions not read.

## NM.4 Pay statement

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nm.payslip.items` | employer identity, gross pay, hours worked, total wages and benefits, itemized deductions | 2026-01-01 | open | US-NMP8-001 (A.1, New Mexico Legislature (nmlegis.gov)) | 50-4-2(B) each payday |
| `nm.payslip.sick_leave_summary` | YTD earned sick leave accrued and used at least quarterly | 2022-07-01 | open | US-NMS5-002 (A.1, NM State Records Center and Archives (NMAC) / NM DWS Labor Relations Division) | - |

## NM.5 Statutory reporting

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nm.report.trd41414.due` | 25th of month after period (monthly/quarterly/semiannual per certificate) | 2026-01-01 | open | US-NMS5-011 (A.2, New Mexico Taxation and Revenue Department) | zero return required |
| `nm.report.trd41431.due` | 25th after quarter end | 2026-01-01 | open | US-NMS5-012 (A.2, New Mexico Taxation and Revenue Department) | new 2026: WC fee + quarterly wage and withholding report; e-file/e-pay mandatory |
| `nm.report.ui.quarterly_due` | last day of month after quarter, electronic only | 2026-01-01 | open | US-NMS5-016 (A.3, New Mexico Department of Workforce Solutions) | - |
| `nm.newhire.report_days` | 20 days | 1997-10-01 | open | US-NMS5-010 (A.3, New Mexico New Hire Directory (state directory operated for NM; HCA Child Support Services)) | rehire after 60+ days |
| `nm.report.w2.due` | 31 January, electronic only | 2026-01-01 | open | US-NMP52-005 (A.2, New Mexico Taxation and Revenue Department) | FYI-330; TRD page still says last day of February - build on FYI-330 |

Rules:

- Registration: TRD (ACD-31015, NMBTIN) and the DWS UI Tax & Claims System.
- POA: ACD-31102; ES-905 or a third-party administrator login. (US-NMP51-004, US-NMP6-001)

- Not configured in this release (open gap RQ-122): FYI-330 (31 Jan) vs TRD page (last day of Feb).
- Not configured in this release (open gap RQ-123): TRD-41431/TAP bulk schema and TAP W-2 TXT layout not obtained.
- Not configured in this release (open gap RQ-124): Filing-frequency thresholds not stated.

## NM.6 Leave

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nm.leave.paid_sick.accrual_ratio_hours_worked` | 30 hours | 2022-07-01 | open | US-NMS5-002 (A.1, NM State Records Center and Archives (NMAC) / NM DWS Labor Relations Division) | all employers 1+; or frontload 64 h |
| `nm.leave.paid_sick.annual_cap_hours` | 64 hours | 2022-07-01 | open | US-NMS5-001 (A.1, New Mexico Legislature (nmlegis.gov, via Wayback 2026id_)) | use cap per 12 months; carryover |
| `nm.leave.sick.payout_on_separation` | False | 2022-07-01 | open | US-NMS5-001 (A.1, New Mexico Legislature (nmlegis.gov, via Wayback 2026id_)) | reinstated on rehire within 12 months |

## NM.7 Termination and final pay

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nm.final_pay.discharge` | fixed wages within 5 days; task/piece/commission within 10 days | 2026-01-01 | open | US-NMS5-014 (A.3, New Mexico Legislature (nmlegis.gov, via Wayback 2026id_)) | 2017 bill reprint (A.3); penalty up to 60 days |
| `nm.term.final_pay.quit` | next regular payday | 2026-01-01 | open | US-NMS5-014 (A.3, New Mexico Legislature (nmlegis.gov, via Wayback 2026id_)) | - |
| `nm.term.vacation.payout` | owed if written policy grants it (vacation pay is wages) | 2017-11-14 | open | US-NMS5-003 (A.1, NM State Records Center and Archives (NMAC) / NM DWS Labor Relations Division) | 11.1.4.7(O) NMAC |

- Not configured in this release (open gap RQ-125): The current text of NMSA 50-4-4 and 50-4-5 was not read; only an older reprint was available.

## NM.8 Benefits in kind and taxable wages

No New Mexico rule is configured in this domain; the federal treatment in the federal reference applies.

## NM.9 Deductions and garnishments

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nm.garn.consumer.exempt_multiple_minwage` | 40 | 2023-07-01 | open | US-NMS5-015 (A.1, New Mexico Legislature (nmlegis.gov, via Wayback 2026id_)) | greater of 75% disposable or 40x highest applicable minimum wage at place of work |
| `nm.garn.consumer.exempt.weekly.state` | 480 USD | 2023-07-01 | open | US-NMS5-015 (A.1, New Mexico Legislature (nmlegis.gov, via Wayback 2026id_)) | 40 x 12.00 state minimum (US-NMS5-004) |
| `nm.garn.support.max_rate` | 50 percent | 2023-07-01 | open | US-NMS5-015 (A.1, New Mexico Legislature (nmlegis.gov, via Wayback 2026id_)) | - |

- Not configured in this release (open gap RQ-126): The employer fee for child-support income withholding was not located (the agency site refused access).

## NM.10 Collective agreements and prevailing wage

Prevailing wage (public works) is an optional informational flag [US-OWN-009]: this guide documents prevailing-wage laws, thresholds and certified-payroll duties as an overlay, and the payroll build does not produce certified payroll reports.

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nm.prevailing_wage.threshold` | 60000 USD | 2026-01-01 | open | US-NMR3-003 (A.2, US DOL Wage and Hour Division) | public works contracts |
| `nm.prevailing_wage.certified_payroll` | weekly payrolls submitted every two weeks within 5 working days; kept 4 years | 1972-05-31 | open | US-NMS5-009 (A.1, New Mexico Department of Workforce Solutions, Labor Relations Division) | - |

## NM.11 Indexation

Indexation of each value is stated in the note of the value concerned.

## NM.12 Payroll data protection and records

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nm.records.sick_leave.retention_months` | 48 months | 2022-07-01 | open | US-NMS5-002 (A.1, NM State Records Center and Archives (NMAC) / NM DWS Labor Relations Division) | - |

- Not configured in this release (open gap RQ-127): The Social Security number truncation rule (NMSA 57-12B), consent for electronic pay statements and the paycard rule were not read (the legislature site refused access).

## NM.13 Live legal change

No New Mexico rule is configured in this domain; the federal treatment in the federal reference applies.

## NM.14 Authority worked examples (oracle values)

No authority worked example is reproduced in this annex; recomputed withholding examples are in Module 12.

## NM.15 Special populations

- Domestic/household workers: PIT withholding follows federal (none required where federal withholding is not required). (US-NMS5-004, US-NMS5-016, US-NMP52-001)
- Agricultural: Board and lodging deductible. (US-NMS5-004, US-NMS5-016, US-NMS5-013)
- Clergy/religious: PIT follows federal (no state rule beyond federal in FYI-104). (US-NMS5-004, US-NMS5-016)
- Nonresident aliens: No state rule beyond federal (FYI-104 follows the federal W-4 and method). (US-NMP52-001)
- Native Americans (NM-specific): Income wholly earned on own-tribe lands while living there is exempt; no withholding. (US-NMS5-013, US-NMP52-001)
- Military / military spouses: Active-duty pay is exempt; spouses keeping out-of-state residence are exempt. (US-NMP52-001)
- Statutory employees: No state rule beyond federal (FYI-104 ties withholding to federal withholding). (US-NMP52-001)
- Government employees: Excluded from the Healthy Workplaces Act (the state and political subdivisions are not "employers"). (US-NMS5-004, US-NMS5-001)
- Not configured in this release (open gap RQ-128): Thresholds, amounts or conditions for these populations are stated in the sources read without a confirmed value record and are not configured from this annex: Domestic/household workers; Agricultural; Minors; Tipped; Clergy/religious; Students; Government employees; Commission/piecework salespersons.

## NM.16 Language

- The pay statement and all filings are in English (owner decision US-OWN-006).

## NM.S Sources

| Source | Authority |
|---|---|
| US-NMB5-001 | City of Las Cruces |
| US-NMB5-002 | Bernalillo County, Planning & Development Services |
| US-NMB5-301 | Santa Fe County, New Mexico |
| US-NMP51-001 | NM Department of Workforce Solutions |
| US-NMP51-002 | NM Department of Workforce Solutions |
| US-NMP52-001 | New Mexico Taxation and Revenue Department |
| US-NMP52-002 | New Mexico Taxation and Revenue Department |
| US-NMP52-003 | New Mexico Taxation and Revenue Department |
| US-NMP52-005 | New Mexico Taxation and Revenue Department |
| US-NMP8-001 | New Mexico Legislature (nmlegis.gov) |
| US-NMR3-001 | NM Taxation and Revenue Department |
| US-NMR3-002 | NM Department of Workforce Solutions |
| US-NMR3-003 | US DOL Wage and Hour Division |
| US-NMS5-001 | New Mexico Legislature (nmlegis.gov, via Wayback 2026id_) |
| US-NMS5-002 | NM State Records Center and Archives (NMAC) / NM DWS Labor Relations Division |
| US-NMS5-003 | NM State Records Center and Archives (NMAC) / NM DWS Labor Relations Division |
| US-NMS5-004 | New Mexico Legislature (nmlegis.gov, via Wayback 2026id_) |
| US-NMS5-006 | City of Albuquerque, Legal Department |
| US-NMS5-007 | City of Santa Fe, Office of Economic Development |
| US-NMS5-008 | New Mexico Department of Workforce Solutions, UI Tax |
| US-NMS5-009 | New Mexico Department of Workforce Solutions, Labor Relations Division |
| US-NMS5-010 | New Mexico New Hire Directory (state directory operated for NM; HCA Child Support Services) |
| US-NMS5-011 | New Mexico Taxation and Revenue Department |
| US-NMS5-012 | New Mexico Taxation and Revenue Department |
| US-NMS5-013 | New Mexico Taxation and Revenue Department |
| US-NMS5-014 | New Mexico Legislature (nmlegis.gov, via Wayback 2026id_) |
| US-NMS5-015 | New Mexico Legislature (nmlegis.gov, via Wayback 2026id_) |
| US-NMS5-016 | New Mexico Department of Workforce Solutions |


## Fact index

Every value above with its key, effective period and register id.

| Key | Value | Effective | Register id |
|---|---|---|---|
| `nm.final_pay.discharge` | fixed wages within 5 days; task/piece/commission within 10 days | from 2026-01-01 | US-NMS5-014 |
| `nm.garn.consumer.exempt.weekly.state` | 480 | from 2023-07-01 | US-NMS5-015 |
| `nm.garn.consumer.exempt_multiple_minwage` | 40 | from 2023-07-01 | US-NMS5-015 |
| `nm.garn.support.max_rate` | 50 | from 2023-07-01 | US-NMS5-015 |
| `nm.labour.direct_deposit.consent_required` | True | from 2026-01-01 | US-NMP8-001 |
| `nm.labour.minwage.local.albuquerque.hourly` | 12.0 | from 2026-01-01 to 2026-12-31 | US-NMS5-006 |
| `nm.labour.minwage.local.albuquerque.hourly` | 13.0 | from 2027-01-01 | US-NMS5-006 |
| `nm.labour.minwage.local.albuquerque.tipped.hourly` | 7.2 | from 2026-01-01 | US-NMS5-006 |
| `nm.labour.minwage.local.bernalillo_county.hourly` | 10.95 | from 2026-01-01 to 2026-12-31 | US-NMB5-002 |
| `nm.labour.minwage.local.las_cruces.hourly` | 13.01 | from 2026-01-01 to 2026-12-31 | US-NMB5-001 |
| `nm.labour.minwage.local.las_cruces.hourly` | 13.47 | from 2027-01-01 | US-NMB5-001 |
| `nm.labour.minwage.local.las_cruces.tipped.hourly` | 5.2 | from 2026-01-01 to 2026-12-31 | US-NMB5-001 |
| `nm.labour.minwage.local.las_cruces.tipped.hourly` | 5.39 | from 2027-01-01 | US-NMB5-001 |
| `nm.labour.minwage.local.santa_fe_city.hourly` | 15.0 | from 2025-03-01 to 2026-02-28 | US-NMS5-007 |
| `nm.labour.minwage.local.santa_fe_city.hourly` | 15.4 | from 2026-03-01 to 2026-12-31 | US-NMS5-007 |
| `nm.labour.minwage.local.santa_fe_city.hourly` | 15.40 | from 2026-03-01 to 2026-12-31 | US-NMS5-007 |
| `nm.labour.minwage.local.santa_fe_city.hourly` | 17.5 | from 2027-01-01 | US-NMS5-007 |
| `nm.labour.minwage.local.santa_fe_city.tipped_base.hourly` | 3.0 | from 2026-03-01 | US-NMS5-007 |
| `nm.labour.minwage.local.santa_fe_county.hourly` | 15.0 | from 2025-03-01 to 2026-02-28 | US-NMB5-301 |
| `nm.labour.minwage.local.santa_fe_county.hourly` | 15.4 | from 2026-03-01 | US-NMB5-301 |
| `nm.labour.minwage.local.santa_fe_county.hourly` | 15.40 | from 2026-03-01 | US-NMB5-301 |
| `nm.labour.minwage.local.santa_fe_county.tipped_base.hourly` | 4.5 | from 2025-03-01 to 2026-02-28 | US-NMB5-301 |
| `nm.labour.minwage.local.santa_fe_county.tipped_base.hourly` | 4.62 | from 2026-03-01 | US-NMB5-301 |
| `nm.labour.minwage.student.hourly` | 8.5 | from 2020-01-01 | US-NMS5-004 |
| `nm.leave.paid_sick.accrual_ratio_hours_worked` | 30 | from 2022-07-01 | US-NMS5-002 |
| `nm.leave.paid_sick.annual_cap_hours` | 64 | from 2022-07-01 | US-NMS5-001 |
| `nm.leave.sick.payout_on_separation` | False | from 2022-07-01 | US-NMS5-001 |
| `nm.local_wage_tax.exists` | False | from 2026-10-29 | US-NMP52-003 |
| `nm.minwage.hourly` | 12.0 | from 2023-01-01 | US-NMS5-004 |
| `nm.minwage.tipped.cash_wage` | 3.0 | from 2020-01-01 | US-NMS5-004 |
| `nm.newhire.report_days` | 20 | from 1997-10-01 | US-NMS5-010 |
| `nm.overtime.premium.multiplier` | 1.5 | from 2020-01-01 | US-NMS5-004 |
| `nm.overtime.weekly_threshold_hours` | 40 | from 2020-01-01 | US-NMS5-004 |
| `nm.pay_frequency.rule` | paydays max 16 days apart; days 1-15 by 25th; 16-end by 10th of next month | from 2026-01-01 | US-NMP8-001 |
| `nm.payslip.items` | employer identity, gross pay, hours worked, total wages and benefits, itemized deductions | from 2026-01-01 | US-NMP8-001 |
| `nm.payslip.sick_leave_summary` | YTD earned sick leave accrued and used at least quarterly | from 2022-07-01 | US-NMS5-002 |
| `nm.pit.nonresident.days_threshold` | 15 | from 2026-01-01 | US-NMP52-002 |
| `nm.pit.oracle.example_1.withholding` | 41.8 | from 2026-01-01 to 2026-12-31 | US-NMP52-001 |
| `nm.pit.oracle.example_1.withholding` | 41.80 | from 2026-01-01 to 2026-12-31 | US-NMP52-001 |
| `nm.pit.tribal.exempt` | income wholly earned on own-tribe lands while living there | from 2026-01-01 | US-NMS5-013 |
| `nm.pit.wh.rate.top` | 5.9 | from 2026-01-01 to 2026-12-31 | US-NMP52-001 |
| `nm.pit.wh.rates` | 1.5;3.2;4.3;4.7;4.9;5.9 | from 2026-01-01 to 2026-12-31 | US-NMP52-001 |
| `nm.pit.wh.single.band_starts` | 0;5500;16500;33500;66500;210000 | from 2026-01-01 to 2026-12-31 | US-NMP52-001 |
| `nm.pit.wh.single.zero_bracket` | 8050 | from 2026-01-01 to 2026-12-31 | US-NMP52-001 |
| `nm.prevailing_wage.certified_payroll` | weekly payrolls submitted every two weeks within 5 working days; kept 4 years | from 1972-05-31 | US-NMS5-009 |
| `nm.prevailing_wage.threshold` | 60000 | from 2026-01-01 | US-NMR3-003 |
| `nm.reciprocity.states` | none | from 2026-01-01 | US-NMP52-002 |
| `nm.records.sick_leave.retention_months` | 48 | from 2022-07-01 | US-NMS5-002 |
| `nm.report.trd41414.due` | 25th of month after period (monthly/quarterly/semiannual per certificate) | from 2026-01-01 | US-NMS5-011 |
| `nm.report.trd41431.due` | 25th after quarter end | from 2026-01-01 | US-NMS5-012 |
| `nm.report.ui.quarterly_due` | last day of month after quarter, electronic only | from 2026-01-01 | US-NMS5-016 |
| `nm.report.w2.due` | 31 January, electronic only | from 2026-01-01 | US-NMP52-005 |
| `nm.sdi_pfml.exists` | False | from 2026-01-01 | US-NMR3-002 |
| `nm.sui.employee.rate` | 0 | from 2026-01-01 | US-NMS5-016 |
| `nm.sui.employer.rate.max` | 5.4 | from 2026-01-01 to 2026-12-31 | US-NMS5-008 |
| `nm.sui.employer.rate.min` | 0.33 | from 2026-01-01 to 2026-12-31 | US-NMS5-008 |
| `nm.sui.wage_base` | 34800 | from 2026-01-01 to 2026-12-31 | US-NMP51-001 |
| `nm.term.final_pay.quit` | next regular payday | from 2026-01-01 | US-NMS5-014 |
| `nm.term.vacation.payout` | owed if written policy grants it (vacation pay is wages) | from 2017-11-14 | US-NMS5-003 |
| `nm.ui.rate.new_employer.min` | 1.0 | from 2026-01-01 to 2026-12-31 | US-NMP51-002 |
| `nm.ui.reserve_factor` | 3.6361 | from 2026-01-01 to 2026-12-31 | US-NMS5-008 |
| `nm.wc.admin_fee.employee.quarterly` | 2.25 | from 2025-07-01 to 2028-06-30 | US-NMR3-001 |
| `nm.wc.admin_fee.employee.quarterly` | 2.38 | from 2028-07-01 to 2033-06-30 | US-NMR3-001 |
| `nm.wc.admin_fee.employer.quarterly` | 2.55 | from 2025-07-01 to 2028-06-30 | US-NMR3-001 |
| `nm.wc.admin_fee.employer.quarterly` | 2.68 | from 2028-07-01 to 2033-06-30 | US-NMR3-001 |
| `nm.wh.certificate` | no state form; optional federal W-4 copy marked For New Mexico State Withholding Only | from 2026-01-01 | US-NMP52-001 |
| `nm.wh.method` | FYI-104 Rev. 11/2025 percentage tables; standard deduction built in; no allowances | from 2026-01-01 to 2026-12-31 | US-NMP52-001 |
| `nm.wh.supplemental.rate` | 5.9 | from 2026-01-01 to 2026-12-31 | US-NMP52-001 |
