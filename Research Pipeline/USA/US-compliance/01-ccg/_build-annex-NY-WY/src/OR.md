## @labour
- **Minimum wage (ORS 653.025) [US-ORS5-001, US-ORS5-002].** Three geographic tiers; the rate changes on **July 1**, not January 1.

| Period | Standard | Portland metro (inside the urban growth boundary) | Nonurban counties (ORS 653.026) |
|---|---|---|---|
| 2025-07-01 to 2026-06-30 | {{or.labour.minwage.standard.hourly@2025-07-01}} USD | {{or.labour.minwage.portland_metro.hourly@2025-07-01}} USD | {{or.labour.minwage.nonurban.hourly@2025-07-01}} USD |
| 2026-07-01 to 2027-06-30 | {{or.labour.minwage.standard.hourly@2026-07-01}} USD | {{or.labour.minwage.portland_metro.hourly@2026-07-01}} USD | {{or.labour.minwage.nonurban.hourly@2026-07-01}} USD |

The applicable tier is that of the county where the employee works the majority of weekly hours; a shift straddling June 30 / July 1 is paid at two rates. Tip credit allowed: {{or.minwage.tip_credit.allowed}} (tips never count toward the minimum wage). Minors receive the same rate. There is no city ordinance layer.
- **Overtime [US-ORS5-008].** {{or.overtime.premium.multiplier}} times the regular rate after {{or.overtime.weekly_threshold_hours}} hours per workweek (ORS 653.261). Daily overtime and hour caps apply in manufacturing, mills and factories (ORS 652.020) and in canneries, driers and packing plants (ORS 653.265). Agricultural workers: overtime above {{or.labour.overtime.agricultural.threshold_hours@2025-01-01}} hours per week in 2025-2026 and above {{or.labour.overtime.agricultural.threshold_hours@2027-01-01}} hours from 2027-01-01 (ORS 653.272). Domestic workers: ORS 653.547 (higher threshold if living in, weekly rest period).
- **Pay frequency (ORS 652.120) [US-ORS5-006]:** regular paydays no more than {{or.labour.pay_frequency.max_days}} days apart; undisputed shortfalls corrected by the next payday or within the statutory period after notice.
- **Method of payment (ORS 652.110) [US-ORS5-006]:** negotiable checks; direct deposit allowed; a check on request. Paycard: {{or.labour.paycard.consent}} (shorter revocation period for seasonal farm and packing workers).

## @income_tax
- **Instruments [US-ORS5-020, US-ORS5-009, US-OR-001, US-ORS5-012]:** ORS 316.037, 316.048, 316.162, 316.167; DOR 150-206-436 Withholding Tax Formulas (effective 2026-01-01); Form OR-W-4 (2026).
- **Method [US-ORS5-009]:** {{or.wh.method}}.
  - Standard deduction: single {{or.pit.std_deduction.single}} USD; married (and single with three or more allowances) {{or.pit.std_deduction.married}} USD.
  - Federal tax subtraction capped at {{or.pit.federal_tax_subtraction.cap}} USD, phasing out at higher wages (DOR formula pages); the publication also prints a different cap on another page (open point below). Build on the formula pages.
  - Withholding rates by band: {{or.pit.wh.rates}} (%); top rate {{or.pit.wh.rate.top}} %. The band constants are cumulative and published in 150-206-436; the base-tax constants are not carried as separate facts.
  - Subtract {{or.pit.allowance.credit}} USD per allowance (no allowances above the statutory high-income levels); a negative result is zero; divide by the number of pay periods.
- **Oracle:** DOR Example 1 recomputed gives annual withholding of {{or.pit.oracle.example_1.annual_withholding}} USD; the publication prints a higher figure that its own lines do not support. Record the defect; do not "fix" the publication. Recomputation in Module 12.
- **Supplemental wages:** optional flat {{or.wh.supplemental.rate}} % when paid apart from the regular payday; the same rate is the default when no OR-W-4 is on file (HB 2119) [US-ORS5-009].
- **Rounding:** {{or.pit.rounding}} [US-ORS5-009].
- **Withholding wages exclude (ORS 316.162(2)) [US-ORS5-020]:** armed forces pay with no federal withholding; interstate carrier employees protected by 49 U.S.C. 14503 / 40116; domestic service in a private home; casual labour outside the trade; small seasonal crop payments; ministers and religious orders; independent contractors; governmental 457(b). For seasonal crop workers the employer may elect a flat {{or.pit.seasonal_crop.flat_rate}} % (316.167(1)).
- **Residents and nonresidents [US-ORS5-025]:** nonresident working in Oregon: {{or.pit.nonresident.threshold}}. An out-of-state employer of Oregon residents working in Oregon (including teleworking) must withhold. An employer with no employees working in Oregon cannot be required to withhold for residents working elsewhere. Reciprocity: {{or.reciprocity.states}}. Residents get a credit for tax paid to another state at assessment (ORS 316.082), not at withholding. No convenience-of-employer rule found.
- **Local income taxes (T4 layer; City of Portland Revenue Division, separate returns) [US-ORS5-004, US-ORS5-005, US-ORS5-024].**
  - Metro Supportive Housing Services (SHS): {{or.pit.local.metro_shs.rate}} %; assessment threshold for single filers {{or.pit.local.metro_shs.threshold.single@2026-01-01}} USD in 2026 and {{or.pit.local.metro_shs.threshold.single@2027-01-01}} USD in 2027 (indexed from 2026).
  - Multnomah County Preschool for All (PFA): {{or.pit.local.multnomah_pfa.rate.1}} % above the first statutory threshold and {{or.pit.local.multnomah_pfa.rate.2}} % in total above the second (not indexed). An announced rate step has a conflicting start year (blocking open point below).
  - Withholding is mandatory for employees who **work** in Metro or Multnomah and earn {{or.pit.local.withholding_trigger}} USD or more in the calendar year; employees may opt in or out on the jurisdictions' forms. Telework from outside the district is not taxable; work physically performed inside is. W-2 local names "METRO" and "MULT".
- **Statewide transit tax** (employee, all residents' wages wherever earned and nonresidents' Oregon wages): Section 3.
- **Resident and nonresident matrix.**

| Income type | Oregon resident | Nonresident |
|---|---|---|
| Regular salary | Withheld under 150-206-436 (by an employer with Oregon employees) | Withheld on Oregon-service wages unless annual Oregon earnings stay below the standard deduction |
| Bonus / supplemental | Flat {{or.wh.supplemental.rate}} % option or aggregate | Same, on Oregon-service wages |
| Metro SHS / Multnomah PFA | By work location in the district, at or above the trigger | Same (work physically performed in the district) |
| Statewide transit tax | All wages, wherever earned | Oregon-service wages |
| Severance, equity, benefits in kind | Federal taxable income with Oregon modifications (ORS 316.048) | Oregon-source share |

## @social
- **Unemployment insurance (OED) [US-ORS5-003, US-ORS5-015].** 2026 taxable wage base {{or.sui.wage_base@2026-01-01}} USD (2025: {{or.sui.wage_base@2025-01-01}} USD); statutory mechanism: a share of the average annual wage of the second preceding year, rounded, never lower than the prior year (ORS 657.095(1)). 2026 is Tax Schedule III: new employer {{or.sui.new_employer.rate}} %, experience range {{or.sui.employer.rate.min}} % to {{or.sui.employer.rate.max}} % (the special payroll tax is embedded in the rate) [US-ORP7-006]. Employee contribution {{or.sui.employee.rate}} %. Wages paid for covered work in another state count toward the base: {{or.sui.wage_base.other_state_credit}} (ORS 657.095(2)).
- **Paid Leave Oregon (PFML) [US-ORS5-003, US-ORS5-013, US-ORS5-014].** Total rate {{or.pfml.rate.total}} % of wages up to {{or.pfml.wage_cap.annual}} USD (equal to the Social Security wage base). Employee share {{or.pfml.employee.share}} % of the contribution; employers with fewer than {{or.pfml.small_employer.threshold}} employees (counting out-of-state employees) pay no employer share but still withhold the employee share. A sole corporate officer cannot elect out of Paid Leave. The employer may pay the employee share as a benefit.
- **Other levies on the combined return [US-ORS5-010, US-ORS5-011].** Statewide transit tax (employee) {{or.stt.employee.rate}} %. TriMet employer tax {{or.transit.trimet.employer.rate}} %; Lane Transit District employer tax {{or.transit.lane.employer.rate}} %. Workers' Benefit Fund {{or.wbf.rate.per_hour}} USD per hour worked, split between employer and employee.

## @payslip
- **Content (ORS 652.610(1)(b)) [US-ORS5-026]:** {{or.payslip.items}}. Electronic delivery only with the employee's express agreement and the ability to print or store.
- **New-hire explanation (SB 906, from 2026-01-01) [US-ORS5-022]:** {{or.payslip.new_hire_explanation}}; BOLI template in English and Spanish [US-ORL-001].
- **Deductions** only as required by law or authorised in writing for the employee's benefit (652.610(3)).
- **Retention:** at least {{or.records.retention_years}} years (ORS 653.045) [US-ORS5-019].

## @reporting
- **Combined quarterly Form OQ [US-ORS5-010]:** withholding, UI, Paid Leave, WBF, TriMet, Lane Transit and STT, with Schedule B and Form 132; filed in Frances Online, paid through Revenue Online. Due dates: {{or.report.oq.due}}. Deposits follow the federal schedule; registered employers file even with no payroll. Annual filers: Form OA (household), Form WA and OR-STT-A (agricultural).
- **W-2 and reconciliation:** Form OR-WR; W-2 {{or.report.w2.due}} (ORS 316.202) [US-ORS5-010].
- **Portland, Metro and Multnomah [US-ORS5-004, US-ORS5-024]:** quarterly returns and annual reconciliation to Portland Revenue Online on the state's due dates (XML bulk upload available); local W-2 {{or.report.local.w2.due}}.
- **New hire [US-ORS5-016]:** to the Oregon DOJ Child Support Program within {{or.newhire.report_days}} days, including rehires and, since 2024-01-01, qualifying independent contractors.
- **Representatives:** OR-AUTH-REP and OR-AUTH-INFO [US-ORP51-005].

## @leave
- **Oregon sick time (ORS 653.601-653.661) [US-ORS5-007, US-ORS5-027]:** paid at {{or.leave.sick.paid_employer_threshold}} or more employees in Oregon, unpaid below. Accrual one hour per {{or.leave.sick.accrual_ratio_hours_worked}} hours worked from day one; annual accrual, carry-over, balance and use may be capped per statute; front-loading allowed. Payout at separation: {{or.leave.sick.payout_at_separation}}. Local sick-leave rules are preempted (653.661). New permitted uses from 2026: blood donation (SB 1108), Paid Leave events [US-ORS5-022].
- **Paid Leave Oregon benefits** are paid by the state; the employer may limit top-up from accrued leave to full wage replacement (ORS 657B.030(2)) [US-ORS5-013].

## @termination
- **Final pay (ORS 652.140) [US-ORS5-006]:** discharge or mutual agreement: {{or.final_pay.discharge}}; resignation with notice: {{or.term.final_pay.resignation_with_notice}}; resignation without notice: within the statutory business-day period or the next payday, whichever is first. Penalty wage (652.150): {{or.term.penalty_wage}}.
- **Accrued vacation:** {{or.term.vacation.payout}} [US-ORS5-021]. Sick time: no payout [US-ORS5-007].

## @bik
- **Base:** federal taxable income with Oregon modifications (ORS 316.048), so federal exclusions flow through; withholding wages include non-cash remuneration (316.162(2)) [US-ORS5-020]. Oregon add-backs not reviewed item by item (open point below).

## @deductions
- **Wage exemption (ORS 18.385) [US-ORS5-017]:** {{or.garn.consumer.exempt_rate}} % of disposable earnings is exempt, and a protected weekly net floor applies: {{or.garn.consumer.floor.weekly@2025-07-01}} USD for wages payable 2025-07-01 to 2026-06-30 and {{or.garn.consumer.floor.weekly@2026-07-01}} USD from 2026-07-01 to 2027-06-30 (other pay periods per the State Court Administrator table); from 2027-07-01 the floor becomes a multiple of the standard minimum wage. Support or restitution writs: weekly floor {{or.garn.support.floor.weekly}} USD. Support withholdings are deducted before a garnishment.
- **Deduction authorisation:** ORS 652.610(3) [US-ORS5-026]; public-employer overpayment recoupment (SB 968, from 2026-01-01) [US-ORS5-022]. IWO fee and priority: open point below.

## @cba
- **BOLI prevailing wage [US-ORP51-004]:** covered public works at or above {{or.prevailing_wage.threshold}} USD with public funds; base plus fringe; certified payroll on WH-38. HB 2688 extends coverage to off-site bespoke fabrication from 2026-07-01; SB 426 (from 2026-01-01) makes owners and direct contractors liable for unpaid wages on construction projects [US-ORS5-022].

## @indexation
- **Minimum wage:** {{or.minwage.indexation}} [US-ORS5-001, US-ORS5-023].
- **UI wage base:** share of the average annual wage of the second preceding year, never lower than the prior year (open point on the derivation below).
- **Paid Leave cap:** equals the Social Security wage base.
- **Withholding brackets, standard deduction, allowance credit:** indexed by DOR each year (150-206-436).
- **Metro SHS thresholds:** indexed from 2026; PFA thresholds not indexed. **Garnishment floor:** minimum-wage multiple from 2027-07-01.

## @data
- **ORS 646A.620 [US-ORS5-018]:** no SSN on unrequested mail (prohibited: {{or.data.ssn.mail_prohibited}}), on access cards or in public display; disposal must render it unreadable. ORS 652.610 does not list the SSN on the pay statement: omit or truncate.

## @live
- **Statewide transit tax increase (HB 3991, Measure 120): not in force.** Measure 120 failed at the 2026-05-19 primary; DOR instructs employers to continue at the current rate (Section 3) [US-ORS5-011].
- **2026 enactments with employer effect [US-ORS5-022]:** SB 906 (new-hire explanation), SB 968 (public-employer recoupment), HB 3550 (minor-league baseball players), SB 1108 (blood donation sick time), SB 69 (sick time and Paid Leave), HB 2688 (prevailing wage from 2026-07-01).
- **2026-07-01:** minimum-wage step; garnishment floor step.
- **2027:** agricultural overtime threshold from 2027-01-01; HB 4013 minors' hours from 2027-01-01; Metro SHS thresholds; predictive-scheduling amendments operative 2027-07-01; 2027 UI, Paid Leave and DOR formulas not yet published (open point below).

## @special
| Population | Oregon rule | Register id |
|---|---|---|
| Domestic / household | Excluded from withholding wages (316.162(2)(c)); UI only above a quarterly cash test (657.050); overtime per 653.547; annual Form OA | US-ORS5-020, US-ORS5-028, US-ORS5-008, US-ORS5-010 |
| Agricultural | Small seasonal crop payments excluded; elective flat {{or.pit.seasonal_crop.flat_rate}} %; UI coverage tests; overtime per Section 1; annual WA / OR-STT-A | US-ORS5-020, US-ORS5-028, US-ORS5-008 |
| Minors | Same minimum wage as adults; HB 4013 hours rule from 2027 | US-ORS5-002, US-ORS5-022 |
| Tipped | No tip credit | US-ORS5-002 |
| Clergy / religious | Excluded from withholding wages (316.162(2)(i)); UI not checked | US-ORS5-020 |
| Students | UI excludes own-school and for-credit work-experience students; sick time excludes work-study | US-ORS5-028, US-ORS5-027 |
| Nonresident aliens | No state rule beyond federal; nonresident threshold applies | US-ORS5-025 |
| Statutory employees | No state rule; independent contractors excluded from withholding wages but reportable as new hires | US-ORS5-020, US-ORS5-016 |
| Government employees | Federal employees excluded from UI and Paid Leave benefits; public-employer overtime exceptions (653.269) and SB 968 recoupment | US-ORS5-028, US-ORS5-013, US-ORS5-022, US-ORS5-026 |
| Corporate officers | May elect out of UI (657.044), not out of Paid Leave | US-ORS5-010, US-ORS5-028 |
| Interstate carrier and airline employees | Withholding barred by federal law (316.162(2)(b)) | US-ORS5-020 |

## @gaps
- or.pit.local.multnomah_pfa.step_year :: The announced Multnomah PFA rate step has conflicting start years on the county's withholding page and personal-tax page; no step rate is modelled until the year is established. :: Multnomah County Code ch. 11 or the county PFA tax page.
- or.pit.federal_tax_subtraction.cap_conflict :: DOR 150-206-436 (2026) prints a different federal-tax subtraction cap on one page and FAQ than the {{or.pit.federal_tax_subtraction.cap}} USD of its formula pages; Example 1 is misprinted. :: DOR written answer (payroll.help.dor@dor.oregon.gov) or DOR calculator run on Example 1.
- or.ui.wage_base.derivation :: The average annual wage behind the 2026 base of {{or.sui.wage_base@2026-01-01}} USD was not fetched, so the base was not re-derived. :: OED annual average wage publication.
- or.bik.addbacks :: Oregon add-backs for HSA, cafeteria-plan and transit benefits were not reviewed. :: DOR Publication OR-17 (2025/2026).
