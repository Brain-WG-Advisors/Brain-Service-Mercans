# Module 3: The Gross-to-Net Calculation Framework
*Purpose: To establish the high-level, sequential logic of the payroll calculation.*

## 3.1 Gross-to-Net Flow

### Deliverable: Provide a definitive, step-by-step description or text-based flowchart illustrating the standard Gross-to-Net (G2N) calculation framework.

A US payroll run computes one federal stack and, for each employee, the State and local stacks selected by the routing keys (`work_location_jurisdiction`, `residence_jurisdiction`, `sui_state`; Module 2). Each stack has its own taxable base. The order below is binding where a later step consumes an earlier result (flagged **ORDER**).

Coverage: this flow is the treatment of the ordinary employee, coverage row `resident_employee` [US-FEDS5-001, US-FEDS5-005, US-FEDS5-007, US-MULTIS5-017]: federal withholding per Form W-4 and Pub. 15-T; FICA employee and employer; FUTA and SUI employer-paid (SUI to the localization State); State income tax of the work State and, for residents working elsewhere, the residence State per its own rule.

#### Step 1: Summation of Gross Earnings

Sum every earning paid in the period, by its payment date: regular pay, overtime, commissions, supplemental pay (bonuses, severance), reported tips and the taxable value of non-cash benefits. Classification of each earning into regular or supplemental decides the income-tax method in Step 5.

| Earning | Rule that matters at this step | Fact |
|---|---|---|
| Tips | Tips of USD 20 or more in a month are subject to income tax withholding and FICA | [US-FEDS5-003] |
| Severance | `fed.severance.is_wages` [US-FEDS5-029]: wages for FIT, FICA and FUTA | [US-FEDS5-029] |
| Group-term life insurance above USD 50,000 of coverage | Imputed cost is FICA wages; income tax withholding not required | [US-FEDS5-008] |
| Paid-leave (PFML) employee contribution | `fed.pfml.employee_contribution.is_w2_wages` [US-FEDS5-007]: remains W-2 wages | [US-FEDS5-007] |

#### Step 2: Application of Pre-Tax Deductions

Subtract salary-reduction amounts that the law excludes from a base. Each base has its own exclusion list, so one deduction can reduce the federal income-tax base and leave a State or unemployment base untouched.

| Deduction | Annual limit 2026 | Fact |
|---|---|---|
| Elective deferral, 401(k)-type plan | USD 24,500; catch-up USD 8,000 (age 50+), USD 11,250 (ages 60 to 63) | [US-FED-023] |
| Health FSA salary reduction | USD 3,400 | [US-FEDS5-010] |
| HSA contribution | USD 4,400 self-only / USD 8,750 family | [US-FED-024] |

State conformity differs, so the State base is built separately (examples):

| State | Treatment | Fact |
|---|---|---|
| CA | UI/SDI subject; PIT not subject | `ca.wages.401k_deferrals` [US-CAS5-019] |
| PA | employee deferrals are taxable for Pennsylvania personal income tax | `pa.bik.pa.401k_403b_457.taxable` [US-PAS5-011] |
| CA | California does not conform to the federal HSA exclusion (HSA contributions subject to PIT, UI and SDI as stated in the annex) | `ca.hsa.conforms` [US-CAS5-019] |
| NJ | 401(k) deferrals are New Jersey unemployment and disability wages | `nj.sui.wages.401k_included` [US-NJS5-017] |
| NJ | cafeteria-plan (IRC sec.125) reductions are New Jersey unemployment wages where cash is electable | `nj.sui.wages.section125_included` [US-NJS5-017] |
| AK | deferrals are excluded from Alaska unemployment wages, unlike FUTA | `ak.sui.wages.excludes_401k_deferrals` [US-AKS5-005] |

Federal base reduced by each pre-tax deduction (Pub. 15 (2026) section 15 and Pub. 15-B (2026) Table 2-1):

| Deduction | Federal income-tax wages | FICA wages | FUTA wages | Source |
|---|---|---|---|---|
| 401(k) elective deferral | excluded (up to the section 402(g) limit) | included | included | [US-FEDS5-029] |
| 403(b) salary reduction | excluded (up to the section 402(g) limit) | included | included | [US-FEDS5-029] |
| 457(b) salary reduction | excluded (up to the section 457(b) limit) | included | included | [US-FEDS5-029] |
| SIMPLE salary reduction | excluded | included | included | [US-FEDS5-029] |
| Section 125 cafeteria plan: accident and health premiums | excluded | excluded | excluded | [US-FEDS5-008] |
| Dependent-care assistance (Section 125 or employer program) | excluded up to 7,500 a year (3,750 married filing separately) | excluded up to 7,500 a year (3,750 married filing separately) | excluded up to 7,500 a year (3,750 married filing separately) | [US-FEDS5-008] |
| HSA contribution (employer or Section 125 salary reduction) | excluded for a qualified individual up to the HSA contribution limit (employer or section 125 salary-reduction contributions) | excluded for a qualified individual up to the HSA contribution limit (employer or section 125 salary-reduction contributions) | excluded for a qualified individual up to the HSA contribution limit (employer or section 125 salary-reduction contributions) | [US-FEDS5-008] |

Rule: 401(k), 403(b) and 457(b) elective deferrals and SIMPLE salary-reduction contributions reduce federal income-tax withholding wages only (within the 402(g) / 457(b) limits); they remain FICA and FUTA wages. Section 125 cafeteria-plan salary reductions for a qualified benefit (accident and health premiums, health FSA, dependent care, HSA) take the treatment of that benefit outside the plan, so they reduce income-tax, FICA and FUTA wages within the benefit limits. [US-FEDS5-029]

Cafeteria-plan election: Benefit chosen under a section 125 cafeteria plan: if the employee chooses cash or another taxable benefit, it is subject to all employment taxes; if the employee chooses a nontaxable (qualified) benefit, the treatment is the same as if the benefit were provided outside the plan. [US-FEDS5-029]

#### Step 3: Determination of Taxable Income

Build one taxable base per tax, from the same gross:

| Base | Built from | Fact |
|---|---|---|
| Federal income-tax wages | Gross less federally excluded pre-tax deductions; then annualised in Worksheet 1A (Module 6) | `fed.fit.method` |
| OASDI wages | FICA wages, capped at USD 184,500 paid by this employer in 2026 | [US-FEDS5-005] |
| Medicare wages | FICA wages, no cap; Additional Medicare above USD 200,000 per employer | [US-FEDS5-005] |
| FUTA wages | First USD 7,000 per employee per employer per year, across all States | `multi.futa.wage_base.scope` [US-MULTIS5-009] |
| State income-tax wages | State definition (conformity table in Step 2; annexes) | annexes |
| Local wages | Local definition; example: Ohio municipal income tax base = Medicare wages less 125 deductions; 401(k) deferrals taxable (medium confidence) | [US-OHS5-001] |
| SUI / SDI / PFML wages | Each programme's definition and cap (Module 5) | annexes |

#### Step 4: Calculation of Employee Social Security Contributions (FICA)

```
oasdi_ee   = round( 6.2% x min( oasdi_wages_period , max(0, 184,500 - oasdi_wages_ytd) ) )
medicare_ee = round( 1.45% x medicare_wages_period )
addl_medicare = round( 0.9% x max(0, medicare_wages_ytd_after - max(200,000, medicare_wages_ytd_before)) )
```

Rates and thresholds: `fed.fica.oasdi.rate.employee` [US-FEDS5-005]; `fed.fica.medicare.rate.employee` [US-FEDS5-005]; `fed.fica.addl_medicare.rate` [US-FEDS5-005]; `fed.fica.addl_medicare.withholding_threshold` [US-FEDS5-005]. Additional Medicare is employee-only and is triggered per employer regardless of filing status. The remaining-base form (lesser of the remaining annual maximum or rate x period base) is mandatory; never annualise and divide.

#### Step 5: Calculation of Income Tax Withholding

Federal: IRS Pub. 15-T (2026) Worksheet 1A with the Annual Percentage Method tables (STANDARD schedule; Step-2-checked schedule when W-4 Step 2 box checked) [US-FEDS5-001]. When the W-4 Step 2 box is **not** checked, Worksheet 1A line 1g subtracts USD 12,900 (married filing jointly) or USD 8,600 (all other statuses) [US-FEDS5-001]. Supplemental pay may instead be withheld at the flat 22% and must be withheld at 37% above USD 1,000,000 in the year [US-FEDS5-003]. Full method and examples: Module 6.

Then State income tax, then local tax. **ORDER** where a State base consumes the federal result:

| State | Dependency | Fact |
|---|---|---|
| AL | Alabama deducts federal income tax withheld from the state base: compute FIT before AL SIT | [US-ALS5-001] |
| OR | Federal tax withheld is subtracted from the Oregon base, capped at USD 8,750 (phase-out by income); the Department's 2026 publication also prints a lower figure in places: use the cap above (formula pages) | [US-ORS5-009]; `practice.or.federal_cap` [US-ORS5-009] |

Resident and nonresident State routing (reciprocity, day thresholds, convenience rules, difference withholding) is applied before the State computation: Module 6 §6.2.

#### Step 6: Application of Post-Tax Deductions

Employee shares of State programmes (unemployment in the States that levy one, disability, paid leave, long-term care), then voluntary after-tax deductions, then garnishments and levies computed on disposable earnings with their protected amounts and priority (Module 7). Withholding for support has priority over any other legal process under state law against the same income (section 466(b)(7) of the Social Security Act); if a federal tax levy is in effect, notify the sender [US-FEDP6-002].

Note: the facts classify some State programme shares as after-tax (for example `me.pfml.employee_deduction.after_tax` [US-MES5-025]); the State annex decides per programme.

#### Step 7: Finalization of Net Pay

```
net_pay = gross
        - pre_tax_deductions
        - (oasdi_ee + medicare_ee + addl_medicare)
        - fit - state_income_tax(es) - local_tax(es)
        - state_programme_employee_shares
        - after_tax_deductions - garnishments
```

Rounding: Optional: wages may be rounded to the nearest dollar and the period tax rounded to the nearest dollar (drop under 50 cents, 50-99 cents up) [US-FED-001]; the quarterly return is always in cents (`fed.form941.amounts_in_cents` [US-FED-005]); Iowa computes its 2026 withholding to the cent, half-up (no whole-dollar rounding in 2026) [US-IAS5-005]. State rounding table: Module 1 §1.5.

### Explain where employer on-costs are calculated in parallel.

Employer amounts are computed from the same bases in Step 3, in parallel with Steps 4 to 6, and never reduce net pay:

| Employer on-cost | Rate / base | Fact |
|---|---|---|
| OASDI employer share | 6.2% up to the OASDI base | [US-FEDS5-005] |
| Medicare employer share | 1.45%, no cap; no employer match of Additional Medicare | [US-FEDS5-005] |
| FUTA | 6% less a credit of up to 5.4% = 0.6% net on USD 7,000, plus any credit reduction of the wages' State | [US-FED-007] |
| SUI employer contribution | Experience rate of the `sui_state` on that State's base | annexes |
| Employer paid-leave shares | Example: District of Columbia paid leave 0.75%, employer only, no cap | [US-DCS5-020] |
| Employer payroll levies | Examples: Nevada Modified Business Tax 1.17% on quarterly wages above USD 50,000; Oregon TriMet transit 0.8237% | [US-NVP51-002]; [US-ORS5-010] |
| Per-employee fees | Example: New Mexico workers' compensation fee, employer USD 2.55 and employee USD 2.25 per quarter | [US-NMR3-001] |

### G2N flow summary and cross-cutting rules

```
for each employee, pay period:
  route  -> federal stack + State stack(s) from work/residence/sui_state
  gross  -> sum earnings by payment date (Step 1)
  bases  -> FIT wages, OASDI wages, Medicare wages, FUTA wages, State wages, local wages, SUI/SDI/PFML wages (Steps 2-3)
  ee     -> FICA (remaining-base form) -> FIT -> State tax [AL, OR after FIT] -> local tax -> programme shares (Steps 4-6)
  net    -> gross - all employee deductions (Step 7)
  er     -> OASDI/Medicare ER, FUTA, SUI ER, ER programme shares and levies (parallel)
```

| Case | Rule | Source |
|---|---|---|
| Mid-period joiner or leaver | No proration rule in federal law: withholding is computed on the wages paid in the pay period with the Pub. 15-T period of the payroll frequency; wage bases start at the first payment by this employer in the year | coverage row `mid_month_joiner_and_leaver` [US-FEDS5-001, US-FEDS5-024, US-MULTIS5-009] |
| Employee with more than one employer | Each employer withholds and applies wage bases independently; Additional Medicare per employer at USD 200,000; with W-4 Step 2 checked, line 1g is not subtracted and the Step-2 schedule applies | coverage row `multiple_employers` [US-FEDS5-006, US-MULTIS5-009, US-FEDS5-005] |
| Supplemental and special pay cycles | Pub. 15-T supports daily to annual periods (annualise, then divide); supplemental pay flat 22% or aggregate, 37% mandatory above USD 1,000,000 | coverage row `special_pay_cycles` [US-FEDS5-003, US-FEDS5-001, US-CAS5-004] |
| Accrual vs payment | Federal taxes follow the **payment** date: a December-earned, January-paid wage takes the new year's rates and bases. Exception: Massachusetts paid-leave rates apply to wages earned on or after 1 January | coverage row `accrual_vs_payment` [US-FED-003, US-FED-006, US-MULTIS5-009, US-MAS5-012] |


## Fact index

Every value above with its key, effective period and register id.

| Key | Value | Effective | Register id |
|---|---|---|---|
| `al.wh.fit_before_sit` | Alabama deducts federal income tax withheld from the state base: compute FIT before AL SIT | from 2026-01-01 | US-ALS5-001 |
| `ca.wages.401k_deferrals` | UI/SDI subject; PIT not subject | from 2026-01-01 | US-CAS5-019 |
| `dc.pfml.employer.rate` | 0.75 | from 2026-01-01 | US-DCS5-020 |
| `fed.base.401k_deferral.fica` | included | from 2026-01-01 | US-FEDS5-029 |
| `fed.base.401k_deferral.fit` | excluded (up to the section 402(g) limit) | from 2026-01-01 | US-FEDS5-029 |
| `fed.base.401k_deferral.futa` | included | from 2026-01-01 | US-FEDS5-029 |
| `fed.base.403b_salary_reduction.fica` | included | from 2026-01-01 | US-FEDS5-029 |
| `fed.base.403b_salary_reduction.fit` | excluded (up to the section 402(g) limit) | from 2026-01-01 | US-FEDS5-029 |
| `fed.base.403b_salary_reduction.futa` | included | from 2026-01-01 | US-FEDS5-029 |
| `fed.base.457b_salary_reduction.fica` | included | from 2026-01-01 | US-FEDS5-029 |
| `fed.base.457b_salary_reduction.fit` | excluded (up to the section 457(b) limit) | from 2026-01-01 | US-FEDS5-029 |
| `fed.base.457b_salary_reduction.futa` | included | from 2026-01-01 | US-FEDS5-029 |
| `fed.base.dependent_care.fica` | excluded up to 7,500 a year (3,750 married filing separately) | from 2026-01-01 | US-FEDS5-008 |
| `fed.base.dependent_care.fit` | excluded up to 7,500 a year (3,750 married filing separately) | from 2026-01-01 | US-FEDS5-008 |
| `fed.base.dependent_care.futa` | excluded up to 7,500 a year (3,750 married filing separately) | from 2026-01-01 | US-FEDS5-008 |
| `fed.base.hsa_contribution.fica` | excluded for a qualified individual up to the HSA contribution limit (employer or section 125 salary-reduction contributions) | from 2026-01-01 | US-FEDS5-008 |
| `fed.base.hsa_contribution.fit` | excluded for a qualified individual up to the HSA contribution limit (employer or section 125 salary-reduction contributions) | from 2026-01-01 | US-FEDS5-008 |
| `fed.base.hsa_contribution.futa` | excluded for a qualified individual up to the HSA contribution limit (employer or section 125 salary-reduction contributions) | from 2026-01-01 | US-FEDS5-008 |
| `fed.base.section125.rule` | Benefit chosen under a section 125 cafeteria plan: if the employee chooses cash or another taxable benefit, it is subject to all employment taxes; if the employee chooses a nontaxable (qualified) benefit, the treatment is the same as if the benefit were provided outside the plan. | from 2026-01-01 | US-FEDS5-029 |
| `fed.base.section125_health.fica` | excluded | from 2026-01-01 | US-FEDS5-008 |
| `fed.base.section125_health.fit` | excluded | from 2026-01-01 | US-FEDS5-008 |
| `fed.base.section125_health.futa` | excluded | from 2026-01-01 | US-FEDS5-008 |
| `fed.base.simple_salary_reduction.fica` | included | from 2026-01-01 | US-FEDS5-029 |
| `fed.base.simple_salary_reduction.fit` | excluded | from 2026-01-01 | US-FEDS5-029 |
| `fed.base.simple_salary_reduction.futa` | included | from 2026-01-01 | US-FEDS5-029 |
| `fed.bik.group_term_life.excluded_coverage` | 50,000 | from 2026-01-01 | US-FEDS5-008 |
| `fed.bik.health_fsa.salary_reduction_cap` | 3,400 | from 2026-01-01 to 2026-12-31 | US-FEDS5-010 |
| `fed.fica.addl_medicare.rate` | 0.9 | from 2026-01-01 to 2026-12-31 | US-FEDS5-005 |
| `fed.fica.addl_medicare.withholding_threshold` | 200,000 | from 2026-01-01 to 2026-12-31 | US-FEDS5-005 |
| `fed.fica.medicare.rate.employee` | 1.45 | from 2026-01-01 to 2026-12-31 | US-FEDS5-005 |
| `fed.fica.medicare.rate.employer` | 1.45 | from 2026-01-01 to 2026-12-31 | US-FEDS5-005 |
| `fed.fica.oasdi.rate.employee` | 6.2 | from 2026-01-01 to 2026-12-31 | US-FEDS5-005 |
| `fed.fica.oasdi.rate.employer` | 6.2 | from 2026-01-01 to 2026-12-31 | US-FEDS5-005 |
| `fed.fica.oasdi.wage_base` | 184,500 | from 2026-01-01 to 2026-12-31 | US-FEDS5-005 |
| `fed.fit.method` | IRS Pub. 15-T (2026) Worksheet 1A with the Annual Percentage Method tables (STANDARD schedule; Step-2-checked schedule when W-4 Step 2 box checked) | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.rounding` | Optional: wages may be rounded to the nearest dollar and the period tax rounded to the nearest dollar (drop under 50 cents, 50-99 cents up) | from 2026-01-01 | US-FED-001 |
| `fed.fit.supplemental.flat_rate` | 22 | from 2026-01-01 | US-FEDS5-003 |
| `fed.fit.supplemental.mandatory_rate` | 37 | from 2026-01-01 | US-FEDS5-003 |
| `fed.fit.supplemental.mandatory_threshold` | 1,000,000 | from 2026-01-01 | US-FEDS5-003 |
| `fed.fit.worksheet1a.line1g.mfj` | 12,900 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.worksheet1a.line1g.other` | 8,600 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.futa.credit.max` | 5.4 | from 2025-01-01 | US-FED-007 |
| `fed.futa.rate.gross` | 6 | from 2025-01-01 | US-FED-007 |
| `fed.futa.rate.net` | 0.6 | from 2025-01-01 | US-FED-007 |
| `fed.futa.wage_base` | 7,000 | from 2025-01-01 | US-FED-007 |
| `fed.hsa.limit.family` | 8,750 | from 2026-01-01 to 2026-12-31 | US-FED-024 |
| `fed.hsa.limit.self_only` | 4,400 | from 2026-01-01 to 2026-12-31 | US-FED-024 |
| `fed.iwo.priority` | Withholding for support has priority over any other legal process under state law against the same income (section 466(b)(7) of the Social Security Act); if a federal tax levy is in effect, notify the sender | from 2026-01-01 to 2026-12-31 | US-FEDP6-002 |
| `fed.retirement.401k.catch_up_50` | 8,000 | from 2026-01-01 to 2026-12-31 | US-FED-023 |
| `fed.retirement.401k.catch_up_60_63` | 11,250 | from 2026-01-01 to 2026-12-31 | US-FED-023 |
| `fed.retirement.401k.elective_deferral_limit` | 24,500 | from 2026-01-01 to 2026-12-31 | US-FED-023 |
| `fed.retirement.pretax.tax_treatment` | 401(k), 403(b) and 457(b) elective deferrals and SIMPLE salary-reduction contributions reduce federal income-tax withholding wages only (within the 402(g) / 457(b) limits); they remain FICA and FUTA wages. Section 125 cafeteria-plan salary reductions for a qualified benefit (accident and health premiums, health FSA, dependent care, HSA) take the treatment of that benefit outside the plan, so they reduce income-tax, FICA and FUTA wages within the benefit limits. | from 2026-01-01 | US-FEDS5-029 |
| `fed.tips.reporting_threshold_monthly` | 20 | from 2026-01-01 | US-FEDS5-003 |
| `ia.wh.rounding` | to the cent, half-up (no whole-dollar rounding in 2026) | from 2026-01-01 to 2026-12-31 | US-IAS5-005 |
| `nm.wc.admin_fee.employee.quarterly` | 2.25 | from 2025-07-01 to 2028-06-30 | US-NMR3-001 |
| `nm.wc.admin_fee.employer.quarterly` | 2.55 | from 2025-07-01 to 2028-06-30 | US-NMR3-001 |
| `nv.mbt.general.quarterly_threshold` | 50,000 | from 2026-01-01 | US-NVS5-011 |
| `nv.mbt.general.rate` | 1.17 | from 2026-01-01 | US-NVP51-002 |
| `oh.local.municipal_base` | Ohio municipal income tax base = Medicare wages less 125 deductions; 401(k) deferrals taxable | from 2026-08-01 | US-OHS5-001 |
| `or.pit.federal_tax_subtraction.cap` | 8,750 | from 2026-01-01 to 2026-12-31 | US-ORS5-009 |
| `or.transit.trimet.employer.rate` | 0.8237 | from 2026-01-01 to 2026-12-31 | US-ORS5-010 |
