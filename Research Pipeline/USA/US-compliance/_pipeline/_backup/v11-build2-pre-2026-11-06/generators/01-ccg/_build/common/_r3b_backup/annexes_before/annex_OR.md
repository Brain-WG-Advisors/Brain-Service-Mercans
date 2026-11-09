# Annex OR: Oregon


Jurisdiction annex of the United States Country Configuration Guide (US-CCG-001). Layer classification: **T4 - local layer remitted to the locality on its own return** (build manifest, tier rationale). City of Portland Metro SHS / Multnomah PFA [US-ORS5-004].

The federal layer (federal income tax withholding, FICA, FUTA, Forms W-2, 941 and 940) and the multistate rules (residence and work-location sourcing, reciprocity mechanics) are in Annex FED and Annex MULTI and are not repeated here. Independent contractors and Form 1099-NEC reporting are out of scope (owner instruction of 2026-10-29) [US-OWN-008]. Payslip language: English; second-language duties attach to notices and posters only (US-OWN-006).

Every value in this annex is bound to a verified fact and carries its legal-basis register id. A value that changes during the year is shown with its effective dates. A point marked as a research gap has not been closed by the research; it is not filled with an estimate.

## OR.1 Employment and labour code

- **Minimum wage (ORS 653.025) [US-ORS5-001, US-ORS5-002].** Three geographic tiers; the rate changes on **July 1**, not January 1.

| Period | Standard | Portland metro (inside the urban growth boundary) | Nonurban counties (ORS 653.026) |
|---|---|---|---|
| 2025-07-01 to 2026-06-30 | [[FACT:or.labour.minwage.standard.hourly=15.05]] USD | [[FACT:or.labour.minwage.portland_metro.hourly=16.30]] USD | [[FACT:or.labour.minwage.nonurban.hourly=14.05]] USD |
| 2026-07-01 to 2027-06-30 | [[FACT:or.labour.minwage.standard.hourly=15.55]] USD | [[FACT:or.labour.minwage.portland_metro.hourly=16.80]] USD | [[FACT:or.labour.minwage.nonurban.hourly=14.55]] USD |

The applicable tier is that of the county where the employee works the majority of weekly hours; a shift straddling June 30 / July 1 is paid at two rates. Tip credit allowed: [[FACT:or.minwage.tip_credit.allowed=False]] (tips never count toward the minimum wage). Minors receive the same rate. There is no city ordinance layer.
- **Overtime [US-ORS5-008].** [[FACT:or.overtime.premium.multiplier=1.5]] times the regular rate after [[FACT:or.overtime.weekly_threshold_hours=40]] hours per workweek (ORS 653.261). Daily overtime and hour caps apply in manufacturing, mills and factories (ORS 652.020) and in canneries, driers and packing plants (ORS 653.265). Agricultural workers: overtime above [[FACT:or.labour.overtime.agricultural.threshold_hours=48]] hours per week in 2025-2026 and above [[FACT:or.labour.overtime.agricultural.threshold_hours=40]] hours from 2027-01-01 (ORS 653.272). Domestic workers: ORS 653.547 (higher threshold if living in, weekly rest period).
- **Pay frequency (ORS 652.120) [US-ORS5-006]:** regular paydays no more than [[FACT:or.labour.pay_frequency.max_days=35]] days apart; undisputed shortfalls corrected by the next payday or within the statutory period after notice.
- **Method of payment (ORS 652.110) [US-ORS5-006]:** negotiable checks; direct deposit allowed; a check on request. Paycard: [[FACT:or.labour.paycard.consent=written agreement in employer's principal language; free full withdrawal; revocation 30 days]] (shorter revocation period for seasonal farm and packing workers).

**Parameters (labour code and pay rules)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `or.labour.minwage.standard.hourly` | [[FACT:or.labour.minwage.standard.hourly=15.05]] | USD | 2025-07-01 to 2026-06-30 | US-ORS5-002 |  |
| `or.labour.minwage.standard.hourly` | [[FACT:or.labour.minwage.standard.hourly=15.55]] | USD | 2026-07-01 to 2027-06-30 | US-ORS5-002 |  |
| `or.labour.minwage.portland_metro.hourly` | [[FACT:or.labour.minwage.portland_metro.hourly=16.30]] | USD | 2025-07-01 to 2026-06-30 | US-ORS5-002 |  |
| `or.labour.minwage.portland_metro.hourly` | [[FACT:or.labour.minwage.portland_metro.hourly=16.80]] | USD | 2026-07-01 to 2027-06-30 | US-ORS5-002 |  |
| `or.labour.minwage.nonurban.hourly` | [[FACT:or.labour.minwage.nonurban.hourly=14.05]] | USD | 2025-07-01 to 2026-06-30 | US-ORS5-002 | standard - 1.00; 18 counties in ORS 653.026 |
| `or.labour.minwage.nonurban.hourly` | [[FACT:or.labour.minwage.nonurban.hourly=14.55]] | USD | 2026-07-01 to 2027-06-30 | US-ORS5-002 |  |
| `or.minwage.indexation` | [[FACT:or.minwage.indexation=CPI-U March/March, nearest 0.05, effective July 1; metro +1.25, nonurban -1.00]] |  | from 2023-07-01 | US-ORS5-001 | ORS 653.025; rate of county where 50%+ of weekly hours worked |
| `or.minwage.tip_credit.allowed` | [[FACT:or.minwage.tip_credit.allowed=False]] |  | from 2025-07-01 | US-ORS5-002 |  |
| `or.overtime.weekly_threshold_hours` | [[FACT:or.overtime.weekly_threshold_hours=40]] | hours | from 2026-01-01 | US-ORS5-008 | ORS 653.261; manufacturing daily limits (652.020) |
| `or.overtime.premium.multiplier` | [[FACT:or.overtime.premium.multiplier=1.5]] | ratio | from 2026-01-01 | US-ORS5-008 |  |
| `or.labour.overtime.agricultural.threshold_hours` | [[FACT:or.labour.overtime.agricultural.threshold_hours=48]] | hours | 2025-01-01 to 2026-12-31 | US-ORS5-008 | ORS 653.272 |
| `or.labour.overtime.agricultural.threshold_hours` | [[FACT:or.labour.overtime.agricultural.threshold_hours=40]] | hours | from 2027-01-01 | US-ORS5-008 | enacted (Or Laws 2022 c.115) |
| `or.labour.pay_frequency.max_days` | [[FACT:or.labour.pay_frequency.max_days=35]] | days | from 2026-01-01 | US-ORS5-006 | ORS 652.120 |
| `or.labour.paycard.consent` | [[FACT:or.labour.paycard.consent=written agreement in employer's principal language; free full withdrawal; revocation 30 days]] |  | from 2026-01-01 | US-ORS5-006 | ORS 652.110 |

## OR.2 Income tax withholding

- **Instruments [US-ORS5-020, US-ORS5-009, US-OR-001, US-ORS5-012]:** ORS 316.037, 316.048, 316.162, 316.167; DOR 150-206-436 Withholding Tax Formulas (effective 2026-01-01); Form OR-W-4 (2026).
- **Method [US-ORS5-009]:** [[FACT:or.wh.method=DOR 150-206-436 annual formula: BASE = wages - federal tax (capped) - std deduction; bands; minus 263 per allowance; / periods]].
  - Standard deduction: single [[FACT:or.pit.std_deduction.single=2910]] USD; married (and single with three or more allowances) [[FACT:or.pit.std_deduction.married=5820]] USD.
  - Federal tax subtraction capped at [[FACT:or.pit.federal_tax_subtraction.cap=8750]] USD, phasing out at higher wages (DOR formula pages); the publication also prints a different cap on another page (open point below). Build on the formula pages.
  - Withholding rates by band: [[FACT:or.pit.wh.rates=4.75;6.75;8.75;9.9]] (%); top rate [[FACT:or.pit.wh.rate.top=9.9]] %. The band constants are cumulative and published in 150-206-436; the base-tax constants are not carried as separate facts.
  - Subtract [[FACT:or.pit.allowance.credit=263]] USD per allowance (no allowances above the statutory high-income levels); a negative result is zero; divide by the number of pay periods.
- **Oracle:** DOR Example 1 recomputed gives annual withholding of [[FACT:or.oracle.annual_25000.withholding=1789]] USD; the publication prints a higher figure that its own lines do not support. Record the defect; do not "fix" the publication. Recomputation in Module 12.
- **Supplemental wages:** optional flat [[FACT:or.wh.supplemental.rate=8]] % when paid apart from the regular payday; the same rate is the default when no OR-W-4 is on file (HB 2119) [US-ORS5-009].
- **Rounding:** [[FACT:or.pit.rounding=nearest dollar permitted, not required]] [US-ORS5-009].
- **Withholding wages exclude (ORS 316.162(2)) [US-ORS5-020]:** armed forces pay with no federal withholding; interstate carrier employees protected by 49 U.S.C. 14503 / 40116; domestic service in a private home; casual labour outside the trade; small seasonal crop payments; ministers and religious orders; independent contractors; governmental 457(b). For seasonal crop workers the employer may elect a flat [[FACT:or.pit.seasonal_crop.flat_rate=2]] % (316.167(1)).
- **Residents and nonresidents [US-ORS5-025]:** nonresident working in Oregon: [[FACT:or.pit.nonresident.threshold=withhold unless Oregon earnings for the year below the standard deduction]]. An out-of-state employer of Oregon residents working in Oregon (including teleworking) must withhold. An employer with no employees working in Oregon cannot be required to withhold for residents working elsewhere. Reciprocity: [[FACT:or.reciprocity.states=none]]. Residents get a credit for tax paid to another state at assessment (ORS 316.082), not at withholding. No convenience-of-employer rule found.
- **Local income taxes (T4 layer; City of Portland Revenue Division, separate returns) [US-ORS5-004, US-ORS5-005, US-ORS5-024].**
  - Metro Supportive Housing Services (SHS): [[FACT:or.pit.local.metro_shs.rate=1]] %; assessment threshold for single filers [[FACT:or.pit.local.metro_shs.threshold.single=128,000]] USD in 2026 and [[FACT:or.pit.local.metro_shs.threshold.single=132,000]] USD in 2027 (indexed from 2026).
  - Multnomah County Preschool for All (PFA): [[FACT:or.pit.local.multnomah_pfa.rate.1=1.5]] % above the first statutory threshold and [[FACT:or.pit.local.multnomah_pfa.rate.2=3]] % in total above the second (not indexed). An announced rate step has a conflicting start year (blocking open point below).
  - Withholding is mandatory for employees who **work** in Metro or Multnomah and earn [[FACT:or.pit.local.withholding_trigger=200,000]] USD or more in the calendar year; employees may opt in or out on the jurisdictions' forms. Telework from outside the district is not taxable; work physically performed inside is. W-2 local names "METRO" and "MULT".
- **Statewide transit tax** (employee, all residents' wages wherever earned and nonresidents' Oregon wages): Section 3.
- **Resident and nonresident matrix.**

| Income type | Oregon resident | Nonresident |
|---|---|---|
| Regular salary | Withheld under 150-206-436 (by an employer with Oregon employees) | Withheld on Oregon-service wages unless annual Oregon earnings stay below the standard deduction |
| Bonus / supplemental | Flat [[FACT:or.wh.supplemental.rate=8]] % option or aggregate | Same, on Oregon-service wages |
| Metro SHS / Multnomah PFA | By work location in the district, at or above the trigger | Same (work physically performed in the district) |
| Statewide transit tax | All wages, wherever earned | Oregon-service wages |
| Severance, equity, benefits in kind | Federal taxable income with Oregon modifications (ORS 316.048) | Oregon-source share |

**Parameters (income tax withholding (state and local))**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `or.wh.method` | [[FACT:or.wh.method=DOR 150-206-436 annual formula: BASE = wages - federal tax (capped) - std deduction; bands; minus 263 per allowance; / periods]] |  | 2026-01-01 to 2026-12-31 | US-ORS5-009 | Rev. 12-31-25 |
| `or.pit.std_deduction.single` | [[FACT:or.pit.std_deduction.single=2910]] | USD | 2026-01-01 to 2026-12-31 | US-ORS5-009 | single with <3 allowances |
| `or.pit.std_deduction.married` | [[FACT:or.pit.std_deduction.married=5820]] | USD | 2026-01-01 to 2026-12-31 | US-ORS5-009 | also single with 3+ allowances |
| `or.pit.federal_tax_subtraction.cap` | [[FACT:or.pit.federal_tax_subtraction.cap=8750]] | USD | 2026-01-01 to 2026-12-31 | US-ORS5-009 | phases out 125k-145k single / 250k-290k married |
| `or.pit.allowance.credit` | [[FACT:or.pit.allowance.credit=263]] | USD | 2026-01-01 to 2026-12-31 | US-ORS5-009 | 0 allowances for single >100,000 / married >200,000 |
| `or.pit.wh.rates` | [[FACT:or.pit.wh.rates=4.75;6.75;8.75;9.9]] |  | 2026-01-01 to 2026-12-31 | US-ORS5-009 |  |
| `or.pit.wh.rate.top` | [[FACT:or.pit.wh.rate.top=9.9]] | % | 2026-01-01 to 2026-12-31 | US-ORS5-009 |  |
| `or.wh.supplemental.rate` | [[FACT:or.wh.supplemental.rate=8]] | % | from 2026-01-01 | US-ORS5-009 | optional when paid at a different time; also default when no OR-W-4 |
| `or.pit.rounding` | [[FACT:or.pit.rounding=nearest dollar permitted, not required]] |  | from 2026-01-01 | US-ORS5-009 |  |
| `or.pit.seasonal_crop.flat_rate` | [[FACT:or.pit.seasonal_crop.flat_rate=2]] | % | from 2026-01-01 | US-ORS5-020 | elective (316.167) |
| `or.pit.nonresident.threshold` | [[FACT:or.pit.nonresident.threshold=withhold unless Oregon earnings for the year below the standard deduction]] |  | 2026-01-01 to 2026-12-31 | US-ORS5-025 |  |
| `or.reciprocity.states` | [[FACT:or.reciprocity.states=none]] |  | 2026-01-01 to 2026-12-31 | US-ORS5-025 | resident credit at assessment (316.082) |
| `or.pit.local.metro_shs.rate` | [[FACT:or.pit.local.metro_shs.rate=1]] | % | from 2023-11-27 | US-ORS5-024 | withholding mandatory for workers in Metro earning 200,000+; Portland Revenue Division |
| `or.pit.local.multnomah_pfa.rate.1` | [[FACT:or.pit.local.multnomah_pfa.rate.1=1.5]] | % | from 2023-11-27 | US-ORS5-005 |  |
| `or.pit.local.multnomah_pfa.rate.2` | [[FACT:or.pit.local.multnomah_pfa.rate.2=3]] | % | from 2023-11-27 | US-ORS5-024 | [[FACT:or.pit.local.multnomah_pfa.rate.1=1.5]]% tier plus a second tier over 250,000/400,000; a further rate step has a conflicting start year (2027 vs 2028) |
| `or.pit.local.withholding_trigger` | [[FACT:or.pit.local.withholding_trigger=200,000]] | USD | from 2023-11-27 | US-ORS5-005 | employees working in Metro/Multnomah earning 200,000+ in the year |
| `or.pit.local.metro_shs.threshold.single` | [[FACT:or.pit.local.metro_shs.threshold.single=128,000]] | USD | 2026-01-01 to 2026-12-31 | US-ORS5-005 | assessment; joint 205,000 |
| `or.pit.local.metro_shs.threshold.single` | [[FACT:or.pit.local.metro_shs.threshold.single=132,000]] | USD | from 2027-01-01 | US-ORS5-005 | joint 211,000 |

**Open research points**

- Not yet published (expected before 2027-01-01 (county withholding notice)) [[GAP:RQ-291]]: The announced Multnomah PFA rate step has conflicting start years on the county's withholding page and personal-tax page; no step rate is modelled until the year is established.
- Not configured in this release [[GAP:RQ-292]]: DOR 150-206-436 (2026) prints a different federal-tax subtraction cap on one page and FAQ than the [[FACT:or.pit.federal_tax_subtraction.cap=8750]] USD of its formula pages; Example 1 is misprinted.

## OR.2b Non-resident regime and reciprocity

The non-resident and reciprocity rules of this jurisdiction are written in OR.2.

## OR.2c Local wage taxes

The local wage taxes of this jurisdiction, where any exist, are written in OR.2.

## OR.3 Social insurance: unemployment, disability, paid leave and payroll levies

- **Unemployment insurance (OED) [US-ORS5-003, US-ORS5-015].** 2026 taxable wage base [[FACT:or.sui.wage_base=56,700]] USD; statutory mechanism: a share of the average annual wage of the second preceding year, rounded, never lower than the prior year (ORS 657.095(1)). 2026 is Tax Schedule III: new employer [[FACT:or.sui.new_employer.rate=2.4]] %, experience range [[FACT:or.sui.employer.rate.min=0.9]] % to [[FACT:or.sui.employer.rate.max=5.4]] % (the special payroll tax is embedded in the rate) [US-ORP7-006]. Employee contribution [[FACT:or.sui.employee.rate=0]] %. Wages paid for covered work in another state count toward the base: [[FACT:or.sui.wage_base.other_state_credit=True]] (ORS 657.095(2)).
- **Paid Leave Oregon (PFML) [US-ORS5-003, US-ORS5-013, US-ORS5-014].** Total rate [[FACT:or.pfml.rate.total=1]] % of wages up to [[FACT:or.pfml.wage_cap.annual=184,500]] USD (equal to the Social Security wage base). Employee share [[FACT:or.pfml.employee.share=60]] % of the contribution; employers with fewer than [[FACT:or.pfml.small_employer.threshold=25]] employees (counting out-of-state employees) pay no employer share but still withhold the employee share. A sole corporate officer cannot elect out of Paid Leave. The employer may pay the employee share as a benefit.
- **Other levies on the combined return [US-ORS5-010, US-ORS5-011].** Statewide transit tax (employee) [[FACT:or.stt.employee.rate=0.1]] %. TriMet employer tax [[FACT:or.transit.trimet.employer.rate=0.8237]] %; Lane Transit District employer tax [[FACT:or.transit.lane.employer.rate=0.8]] %. Workers' Benefit Fund [[FACT:or.wbf.rate.per_hour=0.018]] USD per hour worked, split between employer and employee.

**Parameters (social insurance and payroll levies)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `or.sui.wage_base` | [[FACT:or.sui.wage_base=56,700]] | USD | 2026-01-01 to 2026-12-31 | US-ORS5-003 | 0.80 x AAW(t-2), rounded to 100, never lower (AAW not fetched) |
| `or.sui.new_employer.rate` | [[FACT:or.sui.new_employer.rate=2.4]] | % | 2026-01-01 to 2026-12-31 | US-ORS5-003 | Tax Schedule 3; second authority statute 657.435 |
| `or.sui.employer.rate.min` | [[FACT:or.sui.employer.rate.min=0.9]] | % | 2026-01-01 to 2026-12-31 | US-ORS5-015 | Schedule III 0.9-5.4 |
| `or.sui.employer.rate.max` | [[FACT:or.sui.employer.rate.max=5.4]] | % | 2026-01-01 to 2026-12-31 | US-ORS5-015 |  |
| `or.sui.employee.rate` | [[FACT:or.sui.employee.rate=0]] | % | 2026-01-01 to 2026-12-31 | US-ORS5-003 |  |
| `or.sui.wage_base.other_state_credit` | [[FACT:or.sui.wage_base.other_state_credit=True]] |  | from 2026-01-01 | US-ORS5-015 | 657.095(2); OED proof rule not read |
| `or.pfml.rate.total` | [[FACT:or.pfml.rate.total=1]] | % | 2026-01-01 to 2026-12-31 | US-ORS5-003 | statutory cap 1% |
| `or.pfml.employee.share` | [[FACT:or.pfml.employee.share=60]] | % | from 2023-01-01 | US-ORS5-013 | employer 40%; <25 employees pay no employer share |
| `or.pfml.wage_cap.annual` | [[FACT:or.pfml.wage_cap.annual=184,500]] | USD | 2026-01-01 to 2026-12-31 | US-ORS5-003 | = SS wage base |
| `or.pfml.small_employer.threshold` | [[FACT:or.pfml.small_employer.threshold=25]] |  | from 2023-01-01 | US-ORS5-013 | size counts out-of-state employees |
| `or.stt.employee.rate` | [[FACT:or.stt.employee.rate=0.1]] | % | from 2018-07-01 | US-ORS5-011 | statewide transit tax 0.001; Measure 120 (0.002) did not pass 2026-05-19 |
| `or.transit.trimet.employer.rate` | [[FACT:or.transit.trimet.employer.rate=0.8237]] | % | 2026-01-01 to 2026-12-31 | US-ORS5-010 | 0.008237 |
| `or.transit.lane.employer.rate` | [[FACT:or.transit.lane.employer.rate=0.8]] | % | 2026-01-01 to 2026-12-31 | US-ORS5-010 | 0.0080 |
| `or.wbf.rate.per_hour` | [[FACT:or.wbf.rate.per_hour=0.018]] | USD (USD per hour) | 2026-01-01 to 2026-12-31 | US-ORS5-010 | Workers' Benefit Fund, split half employee / half employer |

**Open research points**

- Not configured in this release [[GAP:RQ-293]]: The average annual wage behind the 2026 base of [[FACT:or.sui.wage_base=56,700]] USD was not read, so the base was not re-derived.
- Not configured in this release [[GAP:RQ-297]]: 2027 OED UI schedule/base, PFML rate and DOR 2027 formulas not published.

## OR.4 Pay statement

- **Content (ORS 652.610(1)(b)) [US-ORS5-026]:** [[FACT:or.payslip.items=payment date; work dates; employee name; employer name, registry no., address, phone; rates; basis; gross; net; each deduction; allowances; regular/OT rates and hours; piece rates]]. Electronic delivery only with the employee's express agreement and the ability to print or store.
- **New-hire explanation (SB 906, from 2026-01-01) [US-ORS5-022]:** [[FACT:or.payslip.new_hire_explanation=written explanation of earnings, deductions and all payroll codes; updated each January 1]]; BOLI template in English and Spanish [US-ORL-001].
- **Deductions** only as required by law or authorised in writing for the employee's benefit (652.610(3)).
- **Retention:** at least [[FACT:or.records.retention_years=2]] years (ORS 653.045) [US-ORS5-019].

**Parameters (payslip statute and payroll records)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `or.payslip.items` | [[FACT:or.payslip.items=payment date; work dates; employee name; employer name, registry no., address, phone; rates; basis; gross; net; each deduction; allowances; regular/OT rates and hours; piece rates]] |  | from 2026-01-01 | US-ORS5-026 | ORS 652.610(1)(b); electronic only with express agreement |
| `or.payslip.new_hire_explanation` | [[FACT:or.payslip.new_hire_explanation=written explanation of earnings, deductions and all payroll codes; updated each January 1]] |  | from 2026-01-01 | US-ORS5-022 | SB 906 |
| `or.records.retention_years` | [[FACT:or.records.retention_years=2]] | years | from 2026-01-01 | US-ORS5-019 | ORS 653.045 |

## OR.5 Statutory reporting

- **Combined quarterly Form OQ [US-ORS5-010]:** withholding, UI, Paid Leave, WBF, TriMet, Lane Transit and STT, with Schedule B and Form 132; filed in Frances Online, paid through Revenue Online. Due dates: [[FACT:or.report.oq.due=Apr 30; Jul 31; Nov 2 (2026); Feb 1 (2027)]]. Deposits follow the federal schedule; registered employers file even with no payroll. Annual filers: Form OA (household), Form WA and OR-STT-A (agricultural).
- **W-2 and reconciliation:** Form OR-WR; W-2 [[FACT:or.report.w2.due=January 31 via iWire (EFW2 or template)]] (ORS 316.202) [US-ORS5-010].
- **Portland, Metro and Multnomah [US-ORS5-004, US-ORS5-024]:** quarterly returns and annual reconciliation to Portland Revenue Online on the state's due dates (XML bulk upload available); local W-2 [[FACT:or.report.local.w2.due=January 31 via Portland Revenue Online, no extension]].
- **New hire [US-ORS5-016]:** to the Oregon DOJ Child Support Program within [[FACT:or.newhire.report_days=20]] days, including rehires and, since 2024-01-01, qualifying independent contractors.
- **Representatives:** OR-AUTH-REP and OR-AUTH-INFO [US-ORP51-005].

**Parameters (statutory reporting)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `or.report.oq.due` | [[FACT:or.report.oq.due=Apr 30; Jul 31; Nov 2 (2026); Feb 1 (2027)]] |  | 2026-01-01 to 2027-02-01 | US-ORS5-010 | combined Form OQ (withholding, UI, PFML, WBF, transit, STT) + Form 132 via Frances Online |
| `or.report.w2.due` | [[FACT:or.report.w2.due=January 31 via iWire (EFW2 or template)]] |  | 2026-01-01 to 2026-12-31 | US-ORS5-010 | ORS 316.202; OR-WR reconciliation |
| `or.report.local.w2.due` | [[FACT:or.report.local.w2.due=January 31 via Portland Revenue Online, no extension]] |  | from 2023-11-27 | US-ORS5-024 | XML ReturnBatch 1.0; 50 per W-2 penalty |
| `or.newhire.report_days` | [[FACT:or.newhire.report_days=20]] | days | from 2024-01-01 | US-ORS5-016 | DOJ Child Support; contractors since 2024-01-01 |

## OR.6 Leave

- **Oregon sick time (ORS 653.601-653.661) [US-ORS5-007, US-ORS5-027]:** paid at [[FACT:or.leave.sick.paid_employer_threshold=10]] or more employees in Oregon, unpaid below. Accrual one hour per [[FACT:or.leave.sick.accrual_ratio_hours_worked=30]] hours worked from day one; annual accrual, carry-over, balance and use may be capped per statute; front-loading allowed. Payout at separation: [[FACT:or.leave.sick.payout_at_separation=False]]. Local sick-leave rules are preempted (653.661). New permitted uses from 2026: blood donation (SB 1108), Paid Leave events [US-ORS5-022].
- **Paid Leave Oregon benefits** are paid by the state; the employer may limit top-up from accrued leave to full wage replacement (ORS 657B.030(2)) [US-ORS5-013].

**Parameters (leave)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `or.leave.sick.paid_employer_threshold` | [[FACT:or.leave.sick.paid_employer_threshold=10]] |  | from 2026-01-01 | US-ORS5-007 | unpaid below 10 Oregon employees |
| `or.leave.sick.accrual_ratio_hours_worked` | [[FACT:or.leave.sick.accrual_ratio_hours_worked=30]] | hours | from 2026-01-01 | US-ORS5-007 | from day 1; cap accrual 40/yr; balance 80 |
| `or.leave.sick.payout_at_separation` | [[FACT:or.leave.sick.payout_at_separation=False]] |  | from 2026-01-01 | US-ORS5-007 | state preempts local (653.661) |

**Open research points**

- Not configured in this release [[GAP:RQ-298]]: Sick-time accrual for hours worked outside Oregon not read.

## OR.7 Termination and final pay

- **Final pay (ORS 652.140) [US-ORS5-006]:** discharge or mutual agreement: [[FACT:or.final_pay.discharge=end of first business day]]; resignation with notice: [[FACT:or.term.final_pay.resignation_with_notice=immediately (48 h notice)]]; resignation without notice: within the statutory business-day period or the next payday, whichever is first. Penalty wage (652.150): [[FACT:or.term.penalty_wage=8 hours per day up to 30 days]].
- **Accrued vacation:** [[FACT:or.term.vacation.payout=per established policy or agreement]] [US-ORS5-021]. Sick time: no payout [US-ORS5-007].

**Parameters (termination)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `or.final_pay.discharge` | [[FACT:or.final_pay.discharge=end of first business day]] |  | from 2026-01-01 | US-ORS5-006 | ORS 652.140 |
| `or.term.final_pay.resignation_with_notice` | [[FACT:or.term.final_pay.resignation_with_notice=immediately (48 h notice)]] |  | from 2026-01-01 | US-ORS5-006 | without notice: 5 business days or next payday whichever first |
| `or.term.penalty_wage` | [[FACT:or.term.penalty_wage=8 hours per day up to 30 days]] |  | from 2026-01-01 | US-ORS5-006 | 652.150 |
| `or.term.vacation.payout` | [[FACT:or.term.vacation.payout=per established policy or agreement]] |  | from 2026-01-01 | US-ORS5-021 |  |

**Open research points**

- Not configured in this release [[GAP:RQ-295]]: UI separation notice and state WARN not established from an official source.

## OR.8 Benefits in kind and taxable wages

- **Base:** federal taxable income with Oregon modifications (ORS 316.048), so federal exclusions flow through; withholding wages include non-cash remuneration (316.162(2)) [US-ORS5-020]. Oregon add-backs not reviewed item by item (open point below).

**Open research points**

- Not configured in this release [[GAP:RQ-294]]: Oregon add-backs for HSA, cafeteria-plan and transit benefits were not reviewed.

## OR.9 Deductions and garnishments

- **Wage exemption (ORS 18.385) [US-ORS5-017]:** [[FACT:or.garn.consumer.exempt_rate=75]] % of disposable earnings is exempt, and a protected weekly net floor applies: [[FACT:or.garn.consumer.floor.weekly=338]] USD for wages payable 2025-07-01 to 2026-06-30 and [[FACT:or.garn.consumer.floor.weekly=400]] USD from 2026-07-01 to 2027-06-30 (other pay periods per the State Court Administrator table); from 2027-07-01 the floor becomes a multiple of the standard minimum wage. Support or restitution writs: weekly floor [[FACT:or.garn.support.floor.weekly=254]] USD. Support withholdings are deducted before a garnishment.
- **Deduction authorisation:** ORS 652.610(3) [US-ORS5-026]; public-employer overpayment recoupment (SB 968, from 2026-01-01) [US-ORS5-022]. IWO fee and priority: open point below.

**Parameters (deductions and garnishments)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `or.garn.consumer.floor.weekly` | [[FACT:or.garn.consumer.floor.weekly=338]] | USD | 2025-07-01 to 2026-06-30 | US-ORS5-017 |  |
| `or.garn.consumer.floor.weekly` | [[FACT:or.garn.consumer.floor.weekly=400]] | USD | 2026-07-01 to 2027-06-30 | US-ORS5-017 | biweekly 832; semimonthly 912; monthly 1,792; from 2027-07-01: 30x standard minimum wage |
| `or.garn.consumer.exempt_rate` | [[FACT:or.garn.consumer.exempt_rate=75]] | % | from 2025-01-01 | US-ORS5-017 | of disposable earnings, plus floor |
| `or.garn.support.floor.weekly` | [[FACT:or.garn.support.floor.weekly=254]] | USD | from 2025-01-01 | US-ORS5-017 | support/restitution writs |

**Open research points**

- Not configured in this release [[GAP:RQ-296]]: Child-support IWO employer fee and priority not established from an official source.

## OR.10 Collective agreements and prevailing wage

- **BOLI prevailing wage [US-ORP51-004]:** covered public works at or above [[FACT:or.prevailing_wage.threshold=50,000]] USD with public funds; base plus fringe; certified payroll on WH-38. HB 2688 extends coverage to off-site bespoke fabrication from 2026-07-01; SB 426 (from 2026-01-01) makes owners and direct contractors liable for unpaid wages on construction projects [US-ORS5-022].

**Parameters (collective agreements and prevailing wage)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `or.prevailing_wage.threshold` | [[FACT:or.prevailing_wage.threshold=50,000]] | USD | from 2026-01-01 | US-ORP51-004 | BOLI; certified payroll WH-38 |

## OR.11 Indexation

- **Minimum wage:** [[FACT:or.minwage.indexation=CPI-U March/March, nearest 0.05, effective July 1; metro +1.25, nonurban -1.00]] [US-ORS5-001, US-ORS5-023].
- **UI wage base:** share of the average annual wage of the second preceding year, never lower than the prior year (open point on the derivation below).
- **Paid Leave cap:** equals the Social Security wage base.
- **Withholding brackets, standard deduction, allowance credit:** indexed by DOR each year (150-206-436).
- **Metro SHS thresholds:** indexed from 2026; PFA thresholds not indexed. **Garnishment floor:** minimum-wage multiple from 2027-07-01.

## OR.12 Payroll data protection and records

- **ORS 646A.620 [US-ORS5-018]:** no SSN on unrequested mail (prohibited: [[FACT:or.data.ssn.mail_prohibited=True]]), on access cards or in public display; disposal must render it unreadable. ORS 652.610 does not list the SSN on the pay statement: omit or truncate.

**Parameters (payroll data protection)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `or.data.ssn.mail_prohibited` | [[FACT:or.data.ssn.mail_prohibited=True]] |  | from 2026-01-01 | US-ORS5-018 | ORS 646A.620 |

## OR.13 Live legal change

- **Statewide transit tax increase (HB 3991, Measure 120): not in force.** Measure 120 failed at the 2026-05-19 primary; DOR instructs employers to continue at the current rate (Section 3) [US-ORS5-011].
- **2026 enactments with employer effect [US-ORS5-022]:** SB 906 (new-hire explanation), SB 968 (public-employer recoupment), HB 3550 (minor-league baseball players), SB 1108 (blood donation sick time), SB 69 (sick time and Paid Leave), HB 2688 (prevailing wage from 2026-07-01).
- **2026-07-01:** minimum-wage step; garnishment floor step.
- **2027:** agricultural overtime threshold from 2027-01-01; HB 4013 minors' hours from 2027-01-01; Metro SHS thresholds; predictive-scheduling amendments operative 2027-07-01; 2027 UI, Paid Leave and DOR formulas not yet published (open point below).

**Parameters (live legal change)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `or.oracle.annual_25000.withholding` | [[FACT:or.oracle.annual_25000.withholding=1789]] | USD | 2026-01-01 to 2026-12-31 | US-ORS5-009 |  |

## OR.14 Authority worked examples (oracle values)

No authority worked example is reproduced in this annex; recomputed withholding examples are in Module 12.

## OR.15 Special populations

| Population | Oregon rule | Register id |
|---|---|---|
| Domestic / household | Excluded from withholding wages (316.162(2)(c)); UI only above a quarterly cash test (657.050); overtime per 653.547; annual Form OA | US-ORS5-020, US-ORS5-028, US-ORS5-008, US-ORS5-010 |
| Agricultural | Small seasonal crop payments excluded; elective flat [[FACT:or.pit.seasonal_crop.flat_rate=2]] %; UI coverage tests; overtime per Section 1; annual WA / OR-STT-A | US-ORS5-020, US-ORS5-028, US-ORS5-008 |
| Minors | Same minimum wage as adults; HB 4013 hours rule from 2027 | US-ORS5-002, US-ORS5-022 |
| Tipped | No tip credit | US-ORS5-002 |
| Clergy / religious | Excluded from withholding wages (316.162(2)(i)); UI not checked | US-ORS5-020 |
| Students | UI excludes own-school and for-credit work-experience students; sick time excludes work-study | US-ORS5-028, US-ORS5-027 |
| Nonresident aliens | No state rule beyond federal; nonresident threshold applies | US-ORS5-025 |
| Statutory employees | No state rule; independent contractors excluded from withholding wages but reportable as new hires | US-ORS5-020, US-ORS5-016 |
| Government employees | Federal employees excluded from UI and Paid Leave benefits; public-employer overtime exceptions (653.269) and SB 968 recoupment | US-ORS5-028, US-ORS5-013, US-ORS5-022, US-ORS5-026 |
| Corporate officers | May elect out of UI (657.044), not out of Paid Leave | US-ORS5-010, US-ORS5-028 |
| Interstate carrier and airline employees | Withholding barred by federal law (316.162(2)(b)) | US-ORS5-020 |

## OR.16 Language

No language rule for employee documents is written for this jurisdiction in this annex.

## OR.S Sources

Register ids cited in this annex resolve to the build record; the URL of each value is in the facts file. Authorities:

- City of Portland Revenue Division: US-ORS5-005, US-ORS5-024
- Oregon Bureau of Labor and Industries: US-ORP51-004
- Oregon Bureau of Labor and Industries (BOLI): US-ORS5-002, US-ORS5-021, US-ORS5-022
- Oregon Department of Justice, Division of Child Support: US-ORS5-016
- Oregon Department of Revenue (DOR): US-ORS5-009, US-ORS5-011
- Oregon Department of Revenue (DOR); Oregon Legislature: US-ORS5-025
- Oregon Department of Revenue with OED and DCBS: US-ORS5-010
- Oregon Employment Department (OED): US-ORS5-003
- Oregon Employment Department, Paid Leave Oregon: US-ORS5-013
- Oregon Legislature (ORS): US-ORS5-001, US-ORS5-006, US-ORS5-007, US-ORS5-008, US-ORS5-015, US-ORS5-017, US-ORS5-018, US-ORS5-019, US-ORS5-020, US-ORS5-026
