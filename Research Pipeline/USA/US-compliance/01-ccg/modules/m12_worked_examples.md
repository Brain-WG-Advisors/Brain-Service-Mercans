# Module 12: Gross-to-Net Worked Examples

*Purpose: To provide a final, comprehensive validation of all researched rules.*

## 12.1 Comprehensive Gross-to-Net Examples

### Provide complete, end-to-end Gross-to-Net calculation examples for common scenarios:

**How these examples are produced.** Every figure below is computed from the verified rates, bases and constants; no number is typed by hand. Amounts are rounded half-up to the cent at each line. The optional whole-dollar rounding that Pub. 15-T allows ([[FACT:fed.fit.rounding=Optional: wages may be rounded to the nearest dollar and the period tax rounded to the nearest dollar (drop under 50 cents, 50-99 cents up)]]) [US-FED-001] is not applied, so the examples show the exact percentage-method result. Employees are on a 2020-or-later Form W-4 with Step 2 not verified and Steps 3 and 4 blank unless stated. The federal layer is shown in full. State and local withholding is shown where the example's work State levies it; per-State figures live in the jurisdiction annexes.

### A full-time resident employee on a standard salary

#### Worked example 1: Scenario A, full-time resident employee (biweekly)

**Scenario A: Full-time resident employee on a standard salary (Texas, biweekly).** Single filer, biweekly salary 3,000.00, first pay of 2026. Work and residence State Texas, which levies no wage income tax (no state income tax withholding, [US-TXS5-001]). Employer State unemployment insurance is paid at the employer's assigned Texas rate on the Texas wage base (Annex TX). It is employer-specific, so it is not computed here.

**Federal income tax: Pub. 15-T 2026 Worksheet 1A, Annual Percentage Method** ([[FACT:fed.fit.method=IRS Pub. 15-T (2026) Worksheet 1A with the Annual Percentage Method tables (STANDARD schedule; Step-2-checked schedule when W-4 Step 2 box checked)]]) [US-FEDS5-001]

| Line | Calculation | Result (USD) |
|---|---|---|
| Annualised wages | 3,000.00 × 26 (biweekly) | 78,000.00 |
| Adjusted annual wage (W-4 Step 2 not verified: less the line 1g amount) | 78,000.00 − [[FACT:fed.fit.worksheet1a.line1g.other=8,600]] | 69,400.00 |
| Annual tentative withholding (STANDARD SINGLE schedule, row 4) | [[FACT:fed.fit.standard.single.bracket.4.cumulative_tax=5,800]] + (69,400.00 − [[FACT:fed.fit.standard.single.bracket.4.floor=57,900]]) × [[FACT:fed.fit.standard.single.bracket.4.rate=22]]% | 8,330.00 |
| Per-period FIT | 8,330.00 ÷ 26 | 320.38 |

**FICA (employee)** [US-FEDS5-005]

| Line | Calculation | Result (USD) |
|---|---|---|
| OASDI employee | 3,000.00 × [[FACT:fed.fica.oasdi.rate.employee=6.2]]% | 186.00 |
| Medicare employee | 3,000.00 × [[FACT:fed.fica.medicare.rate.employee=1.45]]% | 43.50 |

**Net pay**

| Line | Calculation | Result (USD) |
|---|---|---|
| Gross pay | — | 3,000.00 |
| Total employee deductions | 320.38 + 186.00 + 43.50 | 549.88 |
| Net pay | 3,000.00 − 320.38 − 186.00 − 43.50 | 2,450.12 |

**Employer federal contributions** [US-FED-007]

| Line | Calculation | Result (USD) |
|---|---|---|
| OASDI employer | 3,000.00 × [[FACT:fed.fica.oasdi.rate.employer=6.2]]% | 186.00 |
| Medicare employer (no employer share of Additional Medicare) | 3,000.00 × [[FACT:fed.fica.medicare.rate.employer=1.45]]% | 43.50 |
| FUTA base in this pay (first [[FACT:fed.futa.wage_base=7,000]] per employee per year) | min(3,000.00, [[FACT:fed.futa.wage_base=7,000]] − 0.00) | 3,000.00 |
| FUTA (net rate after the full state credit) | 3,000.00 × [[FACT:fed.futa.rate.net=0.6]]% | 18.00 |
| Total employer federal cost | 186.00 + 43.50 + 18.00 | 247.50 |

### A casual or part-time employee

#### Worked example 2: Scenario B, part-time employee at the federal minimum wage

**Scenario B: Part-time hourly employee at the federal minimum wage (weekly).** Single filer, 24 hours in the workweek at the federal minimum wage of [[FACT:fed.minwage.hourly=7.25]] per hour [US-FEDS5-017]. No overtime: the hours are below the [[FACT:fed.overtime.weekly_threshold_hours=40]]-hour weekly threshold [US-FEDS5-018]. Work State without a wage income tax. A higher State or local minimum wage displaces the federal one ([[FACT:multi.wage_hour.overlay_rule=FLSA does not excuse a higher State/municipal minimum wage, a lower maximum workweek or a stricter child-labour standard: apply the more protective standard of the place where the work is performed]]) [US-MULTIS5-008].

| Line | Calculation | Result (USD) |
|---|---|---|
| Gross weekly pay | 24 × [[FACT:fed.minwage.hourly=7.25]] | 174.00 |

**Federal income tax: Pub. 15-T 2026 Worksheet 1A, Annual Percentage Method** ([[FACT:fed.fit.method=IRS Pub. 15-T (2026) Worksheet 1A with the Annual Percentage Method tables (STANDARD schedule; Step-2-checked schedule when W-4 Step 2 box checked)]]) [US-FEDS5-001]

| Line | Calculation | Result (USD) |
|---|---|---|
| Annualised wages | 174.00 × 52 (weekly) | 9,048.00 |
| Adjusted annual wage (W-4 Step 2 not verified: less the line 1g amount) | 9,048.00 − [[FACT:fed.fit.worksheet1a.line1g.other=8,600]] | 448.00 |
| Annual tentative withholding (STANDARD SINGLE schedule, row 1) | [[FACT:fed.fit.standard.single.bracket.1.cumulative_tax=0]] + (448.00 − [[FACT:fed.fit.standard.single.bracket.1.floor=0]]) × [[FACT:fed.fit.standard.single.bracket.1.rate=0]]% | 0.00 |
| Per-period FIT | 0.00 ÷ 52 | 0.00 |

**FICA (employee)** [US-FEDS5-005]

| Line | Calculation | Result (USD) |
|---|---|---|
| OASDI employee | 174.00 × [[FACT:fed.fica.oasdi.rate.employee=6.2]]% | 10.79 |
| Medicare employee | 174.00 × [[FACT:fed.fica.medicare.rate.employee=1.45]]% | 2.52 |

**Net pay**

| Line | Calculation | Result (USD) |
|---|---|---|
| Gross pay | — | 174.00 |
| Total employee deductions | 0.00 + 10.79 + 2.52 | 13.31 |
| Net pay | 174.00 − 0.00 − 10.79 − 2.52 | 160.69 |

**Employer federal contributions** [US-FED-007]

| Line | Calculation | Result (USD) |
|---|---|---|
| OASDI employer | 174.00 × [[FACT:fed.fica.oasdi.rate.employer=6.2]]% | 10.79 |
| Medicare employer (no employer share of Additional Medicare) | 174.00 × [[FACT:fed.fica.medicare.rate.employer=1.45]]% | 2.52 |
| FUTA base in this pay (first [[FACT:fed.futa.wage_base=7,000]] per employee per year) | min(174.00, [[FACT:fed.futa.wage_base=7,000]] − 0.00) | 174.00 |
| FUTA (net rate after the full state credit) | 174.00 × [[FACT:fed.futa.rate.net=0.6]]% | 1.04 |
| Total employer federal cost | 10.79 + 2.52 + 1.04 | 14.35 |

The adjusted annual wage falls in the 0 % row of the STANDARD Single schedule, so no federal income tax is withheld. FICA is still due from the first dollar.

### An employee with a pre-tax deduction

The 2026 limits for the main pre-tax plans are: 401(k) elective deferral [[FACT:fed.retirement.401k.elective_deferral_limit=24,500]], catch-up at age 50 [[FACT:fed.retirement.401k.catch_up_50=8,000]], catch-up at ages 60 to 63 [[FACT:fed.retirement.401k.catch_up_60_63=11,250]] [US-FED-023]; HSA [[FACT:fed.hsa.limit.self_only=4,400]] self-only and [[FACT:fed.hsa.limit.family=8,750]] family [US-FED-024]; health FSA salary reduction [[FACT:fed.bik.health_fsa.salary_reduction_cap=3,400]] [US-FEDS5-010]. California taxes 401(k) deferrals for UI and SDI but not for personal income tax ([[FACT:ca.wages.401k_deferrals=UI/SDI subject; PIT not subject]]) [US-CAS5-019].

#### Worked example 3: Scenario E, 401(k) elective deferral (biweekly)

**Scenario E: Full-time employee with a 401(k) elective deferral (Texas, biweekly).** Scenario A (single filer, biweekly salary 3,000.00, first pay of 2026, Texas) with a 401(k) elective deferral of 300.00 per pay. Treatment of the deferral by base: federal income tax withholding wages [[FACT:fed.base.401k_deferral.fit=excluded (up to the section 402(g) limit)]]; FICA wages [[FACT:fed.base.401k_deferral.fica=included]]; FUTA wages [[FACT:fed.base.401k_deferral.futa=included]] [US-FEDS5-029]. Rule: [[FACT:fed.retirement.pretax.tax_treatment=401(k), 403(b) and 457(b) elective deferrals and SIMPLE salary-reduction contributions reduce federal income-tax withholding wages only (within the 402(g) / 457(b) limits); they remain FICA and FUTA wages. Section 125 cafeteria-plan salary reductions for a qualified benefit (accident and health premiums, health FSA, dependent care, HSA) take the treatment of that benefit outside the plan, so they reduce income-tax, FICA and FUTA wages within the benefit limits.]] [US-FEDS5-029].

| Line | Calculation | Result (USD) |
|---|---|---|
| Deferrals in the year at this rate | 300.00 × 26 | 7,800.00 |
| Within the 402(g) elective deferral limit | 7,800.00 ≤ [[FACT:fed.retirement.401k.elective_deferral_limit=24,500]] | yes |
| Federal income tax withholding wages | 3,000.00 − 300.00 | 2,700.00 |
| FICA wages (deferral not excluded) | 3,000.00 | 3,000.00 |
| FUTA wages (deferral not excluded) | 3,000.00 | 3,000.00 |

**Federal income tax on the reduced wages: Pub. 15-T 2026 Worksheet 1A** [US-FEDS5-001]

| Line | Calculation | Result (USD) |
|---|---|---|
| Annualised wages | 2,700.00 × 26 (biweekly) | 70,200.00 |
| Adjusted annual wage (W-4 Step 2 not verified: less the line 1g amount) | 70,200.00 − [[FACT:fed.fit.worksheet1a.line1g.other=8,600]] | 61,600.00 |
| Annual tentative withholding (STANDARD SINGLE schedule, row 4) | [[FACT:fed.fit.standard.single.bracket.4.cumulative_tax=5,800]] + (61,600.00 − [[FACT:fed.fit.standard.single.bracket.4.floor=57,900]]) × [[FACT:fed.fit.standard.single.bracket.4.rate=22]]% | 6,614.00 |
| Per-period FIT | 6,614.00 ÷ 26 | 254.38 |

**FICA (employee) on the full wages** [US-FEDS5-005]

| Line | Calculation | Result (USD) |
|---|---|---|
| OASDI employee | 3,000.00 × [[FACT:fed.fica.oasdi.rate.employee=6.2]]% | 186.00 |
| Medicare employee | 3,000.00 × [[FACT:fed.fica.medicare.rate.employee=1.45]]% | 43.50 |

**Net pay and employer federal cost**

| Line | Calculation | Result (USD) |
|---|---|---|
| Gross pay | — | 3,000.00 |
| Total employee deductions | 300.00 + 254.38 + 186.00 + 43.50 | 783.88 |
| Net pay | 3,000.00 − 300.00 − 254.38 − 186.00 − 43.50 | 2,216.12 |
| OASDI employer | 3,000.00 × [[FACT:fed.fica.oasdi.rate.employer=6.2]]% | 186.00 |
| Medicare employer | 3,000.00 × [[FACT:fed.fica.medicare.rate.employer=1.45]]% | 43.50 |
| FUTA base in this pay | min(3,000.00, [[FACT:fed.futa.wage_base=7,000]] − 0.00) | 3,000.00 |
| FUTA (net rate after the full state credit) | 3,000.00 × [[FACT:fed.futa.rate.net=0.6]]% | 18.00 |

Compared with Scenario A, only the federal income tax changes; OASDI, Medicare and FUTA are computed on the same 3,000.00.

### An employee with a student loan or other special tax obligation

Student loans: [[FACT:fed.student_loan.payroll_obligation=Federal administrative wage garnishment of student loans: maximum 15 percent of disposable pay (more only with written consent), 30 days' written notice, no deduction until 12 months of continuous reemployment after involuntary separation, no retaliation. Disposable pay = after amounts required by law to be withheld.]] [US-FEDV6-025]. The garnishment mechanics follow Module 7; no student-loan case is computed here.

#### Worked example 4: Supplemental payment above the mandatory threshold

**Special tax obligation computed instead: a supplemental payment above the mandatory threshold.** Supplemental wages paid to one employee in excess of [[FACT:fed.fit.supplemental.mandatory_threshold=1,000,000]] in the calendar year are withheld at the mandatory rate of [[FACT:fed.fit.supplemental.mandatory_rate=37]]% [US-FEDS5-003]. Scenario: the employee has already received 1,000,000.00 of supplemental wages in 2026 and OASDI wages above the base. A further bonus of 50,000.00 is paid.

| Line | Calculation | Result (USD) |
|---|---|---|
| Bonus (all above the mandatory threshold) | — | 50,000.00 |
| FIT at the mandatory rate | 50,000.00 × [[FACT:fed.fit.supplemental.mandatory_rate=37]]% | 18,500.00 |
| OASDI (annual wage base already reached) | — | 0.00 |
| Medicare employee | 50,000.00 × [[FACT:fed.fica.medicare.rate.employee=1.45]]% | 725.00 |
| Additional Medicare (wages already above the threshold) | 50,000.00 × [[FACT:fed.fica.addl_medicare.rate=0.9]]% | 450.00 |
| Net payment | 50,000.00 − 18,500.00 − 725.00 − 450.00 | 30,325.00 |

### Other complex scenarios that are common in the country

#### Worked example 5: Scenario C, OASDI wage base and Additional Medicare threshold (semimonthly)

**Scenario C: High earner crossing the OASDI wage base and the Additional Medicare threshold (semimonthly).** Single filer, semimonthly salary 20,000.00, wages already paid in 2026 by this employer 182,000.00. The OASDI contribution is the rate × the lesser of the remaining annual wage base and the pay (base [[FACT:fed.fica.oasdi.wage_base=184,500]] for 2026, [US-FEDS5-005]). The Additional Medicare tax applies only to the part of the cumulative wages above the threshold. The figures are never annualised and then divided.

**Federal income tax: Pub. 15-T 2026 Worksheet 1A, Annual Percentage Method** ([[FACT:fed.fit.method=IRS Pub. 15-T (2026) Worksheet 1A with the Annual Percentage Method tables (STANDARD schedule; Step-2-checked schedule when W-4 Step 2 box checked)]]) [US-FEDS5-001]

| Line | Calculation | Result (USD) |
|---|---|---|
| Annualised wages | 20,000.00 × 24 (semimonthly) | 480,000.00 |
| Adjusted annual wage (W-4 Step 2 not verified: less the line 1g amount) | 480,000.00 − [[FACT:fed.fit.worksheet1a.line1g.other=8,600]] | 471,400.00 |
| Annual tentative withholding (STANDARD SINGLE schedule, row 7) | [[FACT:fed.fit.standard.single.bracket.7.cumulative_tax=58,448]] + (471,400.00 − [[FACT:fed.fit.standard.single.bracket.7.floor=263,725]]) × [[FACT:fed.fit.standard.single.bracket.7.rate=35]]% | 131,134.25 |
| Per-period FIT | 131,134.25 ÷ 24 | 5,463.93 |

**FICA (employee)** [US-FEDS5-005]

| Line | Calculation | Result (USD) |
|---|---|---|
| OASDI base remaining before this pay | [[FACT:fed.fica.oasdi.wage_base=184,500]] − 182,000.00 | 2,500.00 |
| OASDI base for this pay (lesser of remaining base and pay) | min(2,500.00, 20,000.00) | 2,500.00 |
| OASDI employee | 2,500.00 × [[FACT:fed.fica.oasdi.rate.employee=6.2]]% | 155.00 |
| Medicare employee | 20,000.00 × [[FACT:fed.fica.medicare.rate.employee=1.45]]% | 290.00 |
| Wages above the Additional Medicare threshold in this pay | 202,000.00 − [[FACT:fed.fica.addl_medicare.withholding_threshold=200,000]] | 2,000.00 |
| Additional Medicare (employee only) | 2,000.00 × [[FACT:fed.fica.addl_medicare.rate=0.9]]% | 18.00 |

**Net pay**

| Line | Calculation | Result (USD) |
|---|---|---|
| Gross pay | — | 20,000.00 |
| Total employee deductions | 5,463.93 + 155.00 + 290.00 + 18.00 | 5,926.93 |
| Net pay | 20,000.00 − 5,463.93 − 155.00 − 290.00 − 18.00 | 14,073.07 |

**Employer federal contributions** [US-FED-007]

| Line | Calculation | Result (USD) |
|---|---|---|
| OASDI employer | 2,500.00 × [[FACT:fed.fica.oasdi.rate.employer=6.2]]% | 155.00 |
| Medicare employer (no employer share of Additional Medicare) | 20,000.00 × [[FACT:fed.fica.medicare.rate.employer=1.45]]% | 290.00 |
| FUTA base in this pay (first [[FACT:fed.futa.wage_base=7,000]] per employee per year) | min(20,000.00, [[FACT:fed.futa.wage_base=7,000]] − 182,000.00) | 0.00 |
| FUTA (net rate after the full state credit) | 0.00 × [[FACT:fed.futa.rate.net=0.6]]% | 0.00 |
| Total employer federal cost | 155.00 + 290.00 + 0.00 | 445.00 |

## 12.2 Oracle Collection: Published and Re-derived Withholding Examples

The build manifest names the oracle: IRS Pub. 15-T (2026) for the federal layer, and the worked examples published by each State [US-FED-027]. The IRS Tax Withholding Estimator is not an oracle ([[FACT:fed.oracle.estimator_not_oracle=IRS Tax Withholding Estimator is an employee tool, not an employer withholding engine - not an oracle]]) [US-FED-021]. Table 12.2.1 lists every verified example. Each row gives its register id, how the result was obtained and any residual. Table 12.2.2 recomputes from verified figures each example whose inputs are all verified.

### 12.2.1 Oracle register

| Jurisdiction | Case | Result (USD) | Register | How obtained | Status / residual |
|---|---|---|---|---|---|
| FED | nra_example | [[FACT:fed.oracle.pub15t.nra_example.withholding=31]] | US-FED-027 | quoted | Pub. 15-T wage-bracket result for weekly wages [[FACT:fed.oracle.pub15t.nra_example.wages=526.90]] (300.00 plus the Table 1 add-on [[FACT:fed.fit.nra.addon.table1.weekly=226.90]]). Not re-derived here: the example's filing status and allowance count are not established from an official source. |
| FED | tribal_example | [[FACT:fed.oracle.pub15t.tribal_example.withholding=584.09]] | US-FED-027 | quoted | Tribal gaming monthly payment [[FACT:fed.oracle.pub15t.tribal_example.payment=6,000]]. Tribal gaming tables are not established from an official source, so it is not re-derived here. |
| CA | de44_f.monthly | [[FACT:ca.oracle.de44_f.monthly.withholding=7.17]] | US-CAS5-001 | quoted | Recomputed in 12.2.2: agrees |
| GA | mfj_semimonthly | [[FACT:ga.oracle.mfj_semimonthly.withholding=27.03]] (from 2026-05-11) | US-GAS5-001 | quoted | Recomputed in 12.2.2: agrees |
| IL | weekly_800 | [[FACT:il.oracle.weekly_800.withholding=32.13]] | US-ILR3-001 | quoted | Not recomputed here: scenario inputs not all verified (see the annex). |
| IN | dn1.example.state | [[FACT:in.oracle.dn1.example.state=13.96]] (from 2026-10-01) | US-INS5-007 | quoted | Not recomputed here: scenario inputs not all verified (see the annex). |
| IN | dn1.example.county | [[FACT:in.oracle.dn1.example.county=4.73]] (from 2026-10-01) | US-INS5-007 | quoted | Not recomputed here: scenario inputs not all verified (see the annex). |
| WI | weekly_350_s1 | [[FACT:wi.oracle.weekly_350_s1.withholding=7.59]] | US-WIS5-011 | quoted | Not recomputed here: scenario inputs not all verified (see the annex). |
| WI | biweekly_1000_m3 | [[FACT:wi.oracle.biweekly_1000_m3.withholding=22.08]] | US-WIS5-011 | quoted | Not recomputed here: scenario inputs not all verified (see the annex). |
| DE | weekly_25000 | [[FACT:de.oracle.weekly_25000.withholding=13.88]] | US-DES5-006 | quoted | Not recomputed here: scenario inputs not all verified (see the annex). |
| DE | supplemental | [[FACT:de.oracle.supplemental.withholding=269.63]] | US-DES5-006 | quoted | Not recomputed here: scenario inputs not all verified (see the annex). |
| HI | weekly_500_s3 | [[FACT:hi.oracle.weekly_500_s3.withholding=9.58]] | US-HIS5-004 | quoted | Recomputed in 12.2.2: agrees |
| LA | weekly_700 | [[FACT:la.oracle.weekly_700.withholding=13.98]] | US-LAS5-001 | quoted | Recomputed in 12.2.2: agrees |
| LA | biweekly_4600 | [[FACT:la.oracle.biweekly_4600.withholding=111.54]] | US-LAS5-001 | quoted | Recomputed in 12.2.2: agrees |
| MA | weekly_155_0ex | [[FACT:ma.oracle.weekly_155_0ex.withholding=7.16]] | US-MAS5-024 | quoted | Not recomputed here: scenario inputs not all verified (see the annex). |
| ME | example3.weekly | [[FACT:me.oracle.example3.weekly.withholding=257]] | US-MES5-011 | quoted | Not recomputed here: scenario inputs not all verified (see the annex). |
| MO | oracle.example_1.annual_tax | [[FACT:mo.pit.oracle.example_1.annual_tax=707.81]] | US-MOS5-001 | quoted | Not recomputed here: scenario inputs not all verified (see the annex). |
| MS | weekly_460_0ex | [[FACT:ms.oracle.weekly_460_0ex.withholding=8.94]] | US-MSS5-003 | re-derived from the published method | Recomputed in 12.2.2: agrees |
| RI | weekly_2195 | [[FACT:ri.oracle.weekly_2195.withholding=87.57]] | US-RIS5-019 | quoted | Recomputed in 12.2.2: agrees |
| VT | oracle.example_1 | [[FACT:vt.pit.oracle.example_1.withholding=45.77]] | US-VTS5-016 | quoted | Not recomputed here: scenario inputs not all verified (see the annex). |
| AL | example.1 | [[FACT:al.oracle.example.1.withholding=29.59]] | US-ALS5-001 | quoted | Not recomputed here: scenario inputs not all verified (see the annex). |
| AR | example.1 | [[FACT:ar.oracle.example.1.withholding=36.50]] | US-ARS5-001 | quoted | Recomputed in 12.2.2: agrees |
| ND | section2_booklet | [[FACT:nd.oracle.section2_booklet.withholding=734]] | US-NDS5-001 | quoted | Booklet defect: the booklet prints this figure while its own table gives a lower amount; the oracle uses the table, not the printed example. Never use this row as an expected result. |
| CT | ex8_f_weekly700 | [[FACT:ct.oracle.ex8_f_weekly700.withholding=17.65]] | US-CTP10-001 | re-derived from the published method | Table route. The DRS rules route (TPG-211) gives a different figure for the same case; the engine must choose one method (Module 13, 13.1) [US-CTS5-010]. |
| CT | ex9_a_weekly1000 | [[FACT:ct.oracle.ex9_a_weekly1000.withholding=39.97]] | US-CTP10-001 | re-derived from the published method | Table route. The DRS rules route (TPG-211) gives a different figure for the same case; the engine must choose one method (Module 13, 13.1) [US-CTS5-010]. |
| CT | ex10_b_biweekly2300 | [[FACT:ct.oracle.ex10_b_biweekly2300.withholding=78.82]] | US-CTP10-001 | re-derived from the published method | Table route. The DRS rules route (TPG-211) gives a different figure for the same case; the engine must choose one method (Module 13, 13.1) [US-CTS5-010]. |
| MI | detroit.resident_biweekly_2000 | [[FACT:mi.oracle.detroit.resident_biweekly_2000=47.45]] | US-MIR3-002 | re-derived from the published method | Recomputed in 12.2.2: agrees |
| MN | oracle.example_1 | [[FACT:mn.pit.oracle.example_1.withholding=91.27]] | US-MNS5-010 | re-derived from the published method | Recomputed in 12.2.2: agrees |
| OH | oracle.example_1 | [[FACT:oh.pit.oracle.example_1.withholding=45.13]] (from 2026-08-01) | US-OHS5-001 | re-derived from the published method | Recomputed in 12.2.2: agrees |
| NC | weekly_450_s2 | [[FACT:nc.oracle.weekly_450_s2.withholding=4.44]] | US-NC-001 | re-derived from the published method | Recomputed in 12.2.2: agrees |
| ND | oracle.example_2 | [[FACT:nd.pit.oracle.example_2.withholding=10]] | US-NDS5-001 | re-derived from the published method | Not recomputed here: scenario inputs not all verified (see the annex). |
| NM | oracle.example_1 | [[FACT:nm.pit.oracle.example_1.withholding=41.80]] | US-NMP52-001 | re-derived from the published method | Not recomputed here: scenario inputs not all verified (see the annex). |
| MI | biweekly_2000_1ex | [[FACT:mi.oracle.biweekly_2000_1ex.withholding=75.36]] | US-MIPIT-001 | re-derived from the published method | Recomputed in 12.2.2: agrees The Treasury withholding calculator (official oracle) was not run. |
| OK | oracle.example_1 | [[FACT:ok.pit.oracle.example_1.withholding=37]] | US-OK-001 | re-derived from the published method | Not recomputed here: scenario inputs not all verified (see the annex). |
| OR | annual_25000 | [[FACT:or.oracle.annual_25000.withholding=1,789]] | US-ORS5-009 | re-derived from the published method | Re-derivation from the published method; the published example is mis-computed ([[FACT:practice.or.federal_cap=Use 8,750 federal-tax subtraction cap (pp.6-7 formula); DOR publication also prints 8,500 and its example 1 is mis-computed]]). |
| IA | formula.example6 | [[FACT:ia.oracle.formula.example6.withholding=114.92]] | US-IAS5-005 | re-derived from the published method | The published example has no final figure; re-derivation. Dependent count not established from an official source. |
| ID | biweekly_1212_single | [[FACT:id.oracle.biweekly_1212_single.withholding=31]] | US-IDS5-008 | re-derived from the published method | Recomputed in 12.2.2: agrees |
| SC | oracle.example_1 | [[FACT:sc.pit.oracle.example_1.withholding=10.58]] | US-SCP51-002 | re-derived from the published method | Recomputed in 12.2.2: agrees 2026 withholding tables, not the Act 110 return rates ([[FACT:practice.sc.withholding_rates_2026=Withholding tables in force: SCDOR WH-1603 (Rev. 10/30/25) 2026 tables, 0/3/6%; SCDOR Information Letter #26-20 gives the Act 110 2026 schedule 1.99% (0-29,999) / 5.21% minus 966 (30,000+) and says withholding is unchanged until DOR republishes the tables]]). |
| KS | weekly_threshold_single | [[FACT:ks.oracle.weekly_threshold_single.withholding=69]] | US-KSS5-001 | re-derived from the published method | Recomputed in 12.2.2: agrees |
| FED | payroll_obligation | [[FACT:fed.student_loan.payroll_obligation=Federal administrative wage garnishment of student loans: maximum 15 percent of disposable pay (more only with written consent), 30 days' written notice, no deduction until 12 months of continuous reemployment after involuntary separation, no retaliation. Disposable pay = after amounts required by law to be withheld.]] | US-FEDV6-025 | quoted | Not recomputed here: scenario inputs not all verified (see the annex). |

**Residuals (published examples not reproduced; not expected results):**

- **NY**: Not configured in this release [[GAP:RQ-547]]: NYS-50-T-NYS Method II example 2: the booklet's printed figures differ by one cent from half-up arithmetic, and the booklet states no rounding rule. Examples 1, 3 and 4 reproduce. Needs the DTF rounding convention or a DTF calculator result.
- **KY**: Not configured in this release [[GAP:RQ-548]]: Kentucky 2026 formula sheet: the per-period result is printed without a stated rounding rule, and one intermediate figure is misprinted. Needs DOR KY confirmation of the per-period rounding.
- **UT**: Not configured in this release [[GAP:RQ-542]]: Utah Pub. 14 (Rev. 04/26): six examples reproduce, but the publication's effective date is not established, so they are not dated results. Needs the Tax Commission's statement of the effective date.
- **DC**: Not configured in this release [[GAP:RQ-543]]: District of Columbia: no 2026 withholding method is published. An emergency act revoked personal exemptions and the D-4 is under review. Needs the OTR 2026 withholding instructions or the permanent act.
- **MD**: Not configured in this release [[GAP:RQ-549]]: Maryland: the official oracle is the Comptroller's withholding calculator, which was not run. Needs one calculator run for a fixed case.

### 12.2.2 Re-derivation from verified figures

Each table recomputes one oracle from the verified rates, deductions and brackets. The scenario inputs (wages, frequency, filing status, allowances) are those of the published example. Results are shown to four decimals before rounding. The last column of 12.2.1 records agreement with the oracle fact at the cent (at the dollar where the State rounds withholding to whole dollars).

#### Worked example 6: GA published example re-derived

**GA: MFJ, one dependent, semimonthly 2,000.00 (from 2026-05-11)** [US-GAS5-001]. Published result [[FACT:ga.oracle.mfj_semimonthly.withholding=27.03]].

| Line | Calculation | Result (USD) |
|---|---|---|
| Period standard deduction | [[FACT:ga.wh.std_deduction.mfj=30,000]] ÷ 24 | 1,250.00 |
| Period dependent allowance (1) | [[FACT:ga.wh.dependent_allowance=5,000]] ÷ 24 | 208.33 |
| Withholding | (2,000.00 − 1,250.00 − 208.33) × [[FACT:ga.wh.rate=4.99]]% | 27.0293 |

#### Worked example 7: LA published example re-derived

**LA: L-4 "1", weekly 700.00** [US-LAS5-001]. Published result [[FACT:la.oracle.weekly_700.withholding=13.98]].

| Line | Calculation | Result (USD) |
|---|---|---|
| Withholding | (700.00 − [[FACT:la.wh.std_deduction.single=12,875]] ÷ 52) × [[FACT:la.pit.rate.flat=3.09]]% | 13.9793 |

#### Worked example 8: LA published example re-derived

**LA: L-4 "2", biweekly 4,600.00** [US-LAS5-001]. Published result [[FACT:la.oracle.biweekly_4600.withholding=111.54]].

| Line | Calculation | Result (USD) |
|---|---|---|
| Withholding | (4,600.00 − [[FACT:la.wh.std_deduction.joint=25,750]] ÷ 26) × [[FACT:la.pit.rate.flat=3.09]]% | 111.5371 |

#### Worked example 9: MI published example re-derived

**MI: MI-W4 one exemption, biweekly 2,000.00** [US-MIPIT-001]. Published result [[FACT:mi.oracle.biweekly_2000_1ex.withholding=75.36]].

| Line | Calculation | Result (USD) |
|---|---|---|
| Withholding | (2,000.00 − [[FACT:mi.wh.exemption.biweekly=226.92]]) × [[FACT:mi.pit.rate.flat=4.25]]% | 75.3559 |

#### Worked example 10: MI (Detroit) published example re-derived

**MI (Detroit): Detroit resident, one exemption, biweekly 2,000.00** [US-MIR3-002]. Published result [[FACT:mi.oracle.detroit.resident_biweekly_2000=47.45]].

| Line | Calculation | Result (USD) |
|---|---|---|
| Withholding | (2,000.00 − [[FACT:mi.local.detroit.exemption.annual=600]] ÷ 26) × [[FACT:mi.local.detroit.rate.resident=2.4]]% | 47.4462 |

#### Worked example 11: MN published example re-derived

**MN: Single, one allowance, biweekly 2,000.00** [US-MNS5-010]. Published result [[FACT:mn.pit.oracle.example_1.withholding=91.27]].

| Line | Calculation | Result (USD) |
|---|---|---|
| Annual taxable wages | 2,000.00 × 26 − [[FACT:mn.pit.allowance.amount=5,300]] | 46,700.00 |
| Annual tax | [[FACT:mn.pit.wh.single.2.base_tax=1,782.09]] + (46,700.00 − [[FACT:mn.pit.wh.single.2.floor=38,010]]) × [[FACT:mn.pit.wh.single.2.rate=6.8]]% | 2,373.01 |
| Withholding | 2,373.01 ÷ 26 | 91.2696 |

#### Worked example 12: OH published example re-derived

**OH: One exemption, biweekly 2,000.00 (tables from 2026-08-01)** [US-OHS5-001]. Published result [[FACT:oh.pit.oracle.example_1.withholding=45.13]].

| Line | Calculation | Result (USD) |
|---|---|---|
| Annual taxable wages | 2,000.00 × 26 − [[FACT:oh.pit.wh.exemption.annual=650]] | 51,350.00 |
| Annual tax | [[FACT:oh.pit.wh.base_tax.2=416.80]] + (51,350.00 − [[FACT:oh.pit.wh.break.1=26,050]]) × [[FACT:oh.pit.wh.rate.2=2.99]]% | 1,173.27 |
| Withholding | 1,173.27 ÷ 26 | 45.1258 |

#### Worked example 13: NC published example re-derived

**NC: Single, two allowances, weekly 450.00 (before whole-dollar rounding)** [US-NC-001]. Published result [[FACT:nc.oracle.weekly_450_s2.withholding=4.44]].

| Line | Calculation | Result (USD) |
|---|---|---|
| Weekly standard deduction | [[FACT:nc.pit.std_deduction.single=12,750]] ÷ 52 | 245.1923 |
| Weekly allowances (2) | 2 × [[FACT:nc.pit.allowance.amount=2,500]] ÷ 52 | 96.1538 |
| Withholding | (450.00 − 245.1923 − 96.1538) × [[FACT:nc.pit.wh.rate=4.09]]% | 4.4439 |

#### Worked example 14: SC published example re-derived

**SC: Three allowances, weekly 750.00 (2026 tables, not Act 110)** [US-SCP51-002]. Published result [[FACT:sc.pit.oracle.example_1.withholding=10.58]].

| Line | Calculation | Result (USD) |
|---|---|---|
| Annual wages | 750.00 × 52 | 39,000.00 |
| Standard deduction (rate × wages, capped) | min(39,000.00 × [[FACT:sc.pit.wh.std_deduction.rate=10]]%, [[FACT:sc.pit.wh.std_deduction.cap=7,500]]) | 3,900.00 |
| Annual taxable wages | 39,000.00 − 3 × [[FACT:sc.pit.allowance.annual=5,000]] − 3,900.00 | 20,100.00 |
| Annual tax | 20,100.00 × [[FACT:sc.pit.wh.band.3.rate=6]]% − [[FACT:sc.pit.wh.band.3.subtract=656.10]] | 549.90 |
| Withholding | 549.90 ÷ 52 | 10.5750 |

#### Worked example 15: ID published example re-derived

**ID: Single, biweekly 1,212.00 (table from 2026-07-23); whole dollar** [US-IDS5-008]. Published result [[FACT:id.oracle.biweekly_1212_single.withholding=31]].

| Line | Calculation | Result (USD) |
|---|---|---|
| Withholding before rounding | (1,212.00 − [[FACT:id.wh.zero_bracket.single.biweekly=619]]) × [[FACT:id.pit.rate.flat=5.3]]% | 31.4290 |
| Rounded to the nearest dollar ([[FACT:id.wh.rounding=nearest whole dollar]]) | 31.4290 | 31 |

#### Worked example 16: KS published example re-derived

**KS: Single, weekly per-period zero-bracket threshold; whole dollar** [US-KSS5-001]. Published result [[FACT:ks.oracle.weekly_threshold_single.withholding=69]].

| Line | Calculation | Result (USD) |
|---|---|---|
| Weekly threshold | [[FACT:ks.pit.std_deduction.single=3,605]] ÷ 52 | 69.3269 |
| Rounded to the nearest dollar | 69.3269 | 69 |

#### Worked example 17: HI published example re-derived

**HI: Single, three allowances, weekly 500.00** [US-HIS5-004]. Published result [[FACT:hi.oracle.weekly_500_s3.withholding=9.58]].

| Line | Calculation | Result (USD) |
|---|---|---|
| Annual taxable wages | 500.00 × 52 − 3 × [[FACT:hi.wh.allowance.annual=1,144]] − [[FACT:hi.wh.lump_sum_allowance.annual=4,350]] | 18,218.00 |
| Annual tax | [[FACT:hi.wh.bracket.single.3.base_tax=288]] + (18,218.00 − [[FACT:hi.wh.bracket.single.2.ceiling=14,400]]) × [[FACT:hi.wh.bracket.single.3.rate=5.5]]% | 497.99 |
| Withholding | 497.99 ÷ 52 | 9.5767 |

#### Worked example 18: MS published example re-derived

**MS: Single, zero exemptions, weekly 460.00 (formula, before the table's whole-dollar rounding)** [US-MSS5-003]. Published result [[FACT:ms.oracle.weekly_460_0ex.withholding=8.94]].

| Line | Calculation | Result (USD) |
|---|---|---|
| Annual taxable income | 460.00 × 52 − [[FACT:ms.pit.std_deduction.single=2,300]] | 21,620.00 |
| Annual tax | (21,620.00 − [[FACT:ms.pit.rate.zero_band.ceiling=10,000]]) × [[FACT:ms.pit.rate.flat=4]]% | 464.80 |
| Withholding | 464.80 ÷ 52 | 8.9385 |

#### Worked example 19: RI published example re-derived

**RI: One exemption, weekly 2,195.00** [US-RIS5-019]. Published result [[FACT:ri.oracle.weekly_2195.withholding=87.57]].

| Line | Calculation | Result (USD) |
|---|---|---|
| Weekly taxable wages | 2,195.00 − [[FACT:ri.pit.exemption.annual=1,000]] ÷ 52 | 2,175.7692 |
| Annual tax | [[FACT:ri.pit.bracket.2.base_tax=3,076.88]] + (2,175.7692 × 52 − [[FACT:ri.pit.bracket.1.ceiling=82,050]]) × [[FACT:ri.pit.bracket.2.rate=4.75]]% | 4,553.6550 |
| Withholding | 4,553.6550 ÷ 52 | 87.5703 |

#### Worked example 20: CA published example re-derived

**CA: DE 44 Method B example F: married, annual wages 57,000.00, four allowances, monthly** [US-CAS5-001]. Published result [[FACT:ca.oracle.de44_f.monthly.withholding=7.17]].

| Line | Calculation | Result (USD) |
|---|---|---|
| Married bracket ceilings (DE 44 Rev. 52) | [[FACT:ca.pit.brackets.married.ceilings=22,158 / 52,528 / 82,904 / 115,084 / 145,448 / 742,958 / 891,542 / 1,000,000 / 1,485,906; 14.63% over; base 164,228.58]] | — |
| Taxable income | 57,000.00 − [[FACT:ca.wh.std_deduction.married_2plus_hoh=11,412]] | 45,588.00 |
| Tax on the first married bracket | 22,158.00 × [[FACT:ca.pit.bracket.single.1.rate=1.1]]% | 243.74 |
| Computed annual tax | 243.74 + (45,588.00 − 22,158.00) × [[FACT:ca.pit.bracket.single.2.rate=2.2]]% | 759.20 |
| Exemption allowance credit (4) | 4 × [[FACT:ca.wh.allowance_credit.per_allowance=168.30]] | 673.20 |
| Annual withholding | 759.20 − 673.20 | 86.00 |
| Monthly withholding | 86.00 ÷ 12 | 7.1667 |

#### Worked example 21: AR published example re-derived

**AR: Two exemptions, monthly 2,127.00** [US-ARS5-001]. Published result [[FACT:ar.oracle.example.1.withholding=36.50]].

| Line | Calculation | Result (USD) |
|---|---|---|
| Annual net taxable income | 2,127.00 × 12 − [[FACT:ar.wh.std_deduction=2,470]] | 23,054.00 |
| Band midpoint (USD 50, per [[FACT:ar.wh.method=DFA Formula Method 2026: annualise; less standard deduction; band midpoint (USD 50) below 100,001; bracket formula; round annual tax to dollar; less 29 per exemption; divide by periods]]) | 23,054.00 | 23,050.00 |
| Annual tax before credits | 23,050.00 × [[FACT:ar.pit.bracket.4.rate=3.4]]% − [[FACT:ar.pit.bracket.4.subtract=287.97]] | 495.73 |
| Annual tax rounded to the dollar, less credits (2) | 496 − 2 × [[FACT:ar.wh.personal_credit.per_exemption=29]] | 438.00 |
| Monthly withholding | 438.00 ÷ 12 | [[FACT:ar.oracle.example.1.withholding=36.50]] |

