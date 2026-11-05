# Module 5: Social Security & Pension Systems
*Purpose: To detail the rules for all mandatory social security and pension schemes.*

## 5.1 Contribution Types and Rates

### List all mandatory social security and pension contributions for both employer and employee.

**Federal layer (every employee)**

| Contribution | Employee | Employer | Base / cap 2026 | Fact |
|---|---|---|---|---|
| Old-age, survivors and disability insurance (OASDI, social security) | 6.2% | 6.2% | USD 184,500 per employer | [US-FEDS5-005]; [US-FEDS5-005] |
| Medicare (hospital insurance) | 1.45% | 1.45% | No cap | [US-FEDS5-005] |
| Additional Medicare | 0.9% | none | Wages above USD 200,000 paid by this employer in the year | [US-FEDS5-005] |
| Federal unemployment (FUTA) | none | 6% gross, credit up to 5.4% = 0.6% net | USD 7,000 per employer | [US-FED-007]; [US-FED-007] |

There is no federal pension contribution beyond OASDI; occupational pensions are voluntary plans (§5.3).

**State layer: unemployment insurance (SUI).** Every State levies an employer contribution on its own base, at an experience rate assigned to the employer (rates in the annexes). Employee contributions exist only in three States: AK, NJ, PA (only three States levy employee UI contributions; take 2026 rates from the State annexes) [US-FEDP52-006].

| State | Employee UI rate 2026 | Fact |
|---|---|---|
| AK | 0.5% | [US-AKS5-003] |
| NJ | 0.3825% | [US-NJS5-010] |
| PA | 0.07% on all gross wages, no cap | [US-PAS5-019] |

**State layer: disability (SDI/TDI), paid family and medical leave (PFML) and long-term care.**

| State | Programme | Rate 2026 and split | Fact |
|---|---|---|---|
| CA | State Disability Insurance incl. paid family leave | Employee 1.3%, no wage cap, no employer share | [US-CAP7-002]; `ca.sdi.wage_cap.exists` [US-CAP7-002] |
| NJ | Temporary disability / family leave insurance | Employee TDI 0.19% (annual maximum USD 325.09); employee FLI 0.23% (annual maximum USD 393.53) | [US-NJS5-010]; [US-NJP51-004] |
| NY | Disability benefits (DBL) and paid family leave (PFL), insurer-funded | DBL employee 0.5%, maximum USD 0.60 a week; PFL employee 0.432% (annual maximum USD 411.91) | [US-NYB5-401]; [US-NYP8-001] |
| HI | Temporary disability insurance, insurer-funded | Employer may withhold up to 0.5% of weekly wages, maximum USD 7.50 a week | [US-HIS5-014]; [US-HIS5-015] |
| RI | Temporary disability / caregiver insurance | Employee 1.1% (annual maximum USD 1,100) | [US-RIP9V-001] |
| WA | Paid Family and Medical Leave | Total 1.13% in 2026, employee up to 71.43% of the premium; 1.2% in 2027, employee 70.7%; wage cap USD 184,500; fewer than 50 WA employees: no employer share | [US-WAS5-015]; [US-WAB5-002] |
| WA | WA Cares long-term care | Employee 0.58%, no cap | [US-WAS5-016] |
| MA | Paid Family and Medical Leave | Total 0.88% (25+ covered individuals); split below | [US-MAS5-012] |
| DC | Universal Paid Leave | Employer only 0.75%, no cap | [US-DCS5-020] |
| OR | Paid Leave Oregon | Total 1%; employee 60% of the contribution | [US-ORS5-003]; [US-ORS5-013] |
| CO | FAMLI | 0.88% = employee 0.44% + employer 0.44% (2027 total 0.86%) | [US-COB5-401] |
| CT | Paid Leave | Employee 0.5%, no employer share | [US-CTP7-001] |
| DE | Paid Leave | Total 0.8% (medical 0.4% + caregiving 0.08% + parental 0.32%); employee up to 50% | [US-DES5-012] |
| ME | Paid Family and Medical Leave | 1% with 15+ employees, 0.5% below; employee at most 0.5%; deducted after tax | [US-MEP6-001]; `me.pfml.employee_deduction.after_tax` [US-MES5-025] |
| MN | Paid Leave | Total 0.88% (family 0.27% + medical 0.61%); employee at most 0.44%; small employers 0.66% | [US-MNP52-003] |
| MD | FAMLI (contributions from 2027-01-01) | Total 0.9%; employee up to 50% | [US-MDS5-014] |

Maternity, paternity and parental leave (coverage row `maternity_paternity_parental` [US-FEDS5-026, US-FEDS5-007, US-WAS5-015, US-MAS5-012]): there is no federal paid parental leave for private employers; paid leave comes from the State PFML/TDI programmes above, whose premiums are withheld or paid through payroll while the benefits are paid by the State. `fed.pfml.employee_contribution.is_w2_wages` [US-FEDS5-007]: the employee contribution remains W-2 wages.

**Workers' compensation and levies.** Workers' compensation is State law and generally an insured employer cost outside payroll (coverage row `work_accident_occupational_disease` [US-NMR3-001, US-FEDS5-029]). Payroll touches it where a State levies a per-employee fee or allows an employee deduction: New Mexico fee employer USD 2.55 and employee USD 2.25 per quarter [US-NMR3-001]; Washington employer (not self-insured) deducts from each worker one-half of the medical aid premium per hour per risk class [US-WAS7-001].

Not configured in this release (open gap RQ-544): Only NM fee and WA employee deduction are known; other States allowing employee workers-comp deductions not reviewed.

Employer transit levies (Oregon): TriMet 0.8237%, Lane 0.8% [US-ORS5-010]. Other employer payroll levies are in the annexes (scope decision US-OWN-007).

### Are contributions managed at a national or sub-national level?

Both. FICA and FUTA are federal (IRS, quarterly and annual federal returns). Unemployment insurance, disability, paid-leave and long-term-care programmes are State programmes with their own agency, base and return. FUTA links the two levels: State UI contributions credited against FUTA, capped at 90% of the tax; credit reduced for states with outstanding Title XII advances [US-FED-014].

| Element | Rule | Fact |
|---|---|---|
| Which State's SUI applies | One State covers the entire service with one employer, in order: (1) localized (entirely in the State, or out-of-state service incidental: temporary, transitory, isolated); (2) else some service in the base-of-operations State; (3) else some service in the State of direction or control; (4) else some service in the State of residence | [US-MULTIS5-017] |
| Telecommuting | UIPL 20-04 (2004, continuing) reissues the UIPL 291 interpretation with telecommuting examples | [US-MULTIS5-016] |
| Unresolved cases | Where no test resolves the case, employer, employee and States may elect coverage of all service in one State (performance, residence or place of business); CA CUIC 602/603 | [US-MULTIS5-010] |
| Which State's PFML/SDI applies | Key the PFML/SDI premium State to sui_state unless the State annex proves otherwise (WA, CT, ME, OR, MD, RI proven; DC and DE differ) | [US-MULTIS5-024] |

The PFML/SDI/TDI coverage test of the remaining programmes (California, New Jersey, New York, Massachusetts, Colorado, Minnesota, Vermont, Hawaii) is open State by State in the multistate reference (MULTI.3), where each carries its own research marker.

## 5.1.1 Contribution Basis Definition

### For each mandatory contribution, provide the statutory definition of the earnings base.

FICA and FUTA are levied on wages **paid** in the calendar year by the employer (coverage row `accrual_vs_payment` [US-FED-003, US-FED-006, US-MULTIS5-009, US-MAS5-012]). FUTA counts one base per employer, not per State: FUTA 7,000 counts remuneration paid by the employer in the calendar year across all States: one base per employer, not per State; successor carry-over [US-MULTIS5-009]. The inclusion/exclusion lists of FICA and FUTA wages are in Module 4 §4.2 [US-FEDQ3-002]. Each State defines its own UI wages; the 2026 taxable wage bases are:

| State | SUI taxable wage base 2026 (USD) | Fact |
|---|---|---|
| AK | 54,200 | [US-AKS5-003] |
| AL | 8,000 | [US-ALS5-009] |
| AR | 7,000 | [US-ARP9V-001] |
| AZ | 8,000 | [US-AZP9V-001] |
| CA | 7,000 | [US-CAS5-016] |
| CO | 30,600 | [US-COP51-003] |
| CT | 27,000 | [US-CTP9V-001] |
| DC | 9,000 | [US-DCS5-017] |
| DE | 14,500 | [US-DES5-010] |
| FL | 7,000 | [US-FLS5-003] |
| GA | 9,500 | [US-GAW1B-001] |
| HI | 64,500 | [US-HIP9V-001] |
| IA | 20,400 | [US-IAS5-009] |
| ID | 58,300 | [US-IDB5-402] |
| IL | 14,250 | [US-ILS5-015] |
| IN | 9,500 | [US-INS5-014] |
| KS | 15,100 | [US-KSS5-023] |
| KY | 12,000 | [US-KY-003] |
| LA | 7,000 | [US-LAP9V-001] |
| MA | 15,000 | [US-MAP51-005] |
| MD | 8,500 | [US-MDB5-401] |
| ME | 12,000 | [US-MES5-020] |
| MI | 9,000 | [US-MIS5-025] |
| MN | 44,000 | [US-MNP52-001] |
| MO | 9,000 | [US-MOP9W-002] |
| MS | 14,000 | [US-MSS5-011] |
| MT | 47,300 | [US-MTP51-005] |
| NC | 34,200 | [US-NCB5-401] |
| ND | 46,600 | [US-NDS5-012] |
| NE | 9,000 | [US-NEP51-003] |
| NH | 14,000 | [US-NHS5-007] |
| NJ | 44,800 | [US-NJS5-010] |
| NM | 34,800 | [US-NMP51-001] |
| NV | 43,700 | [US-NVP51-001] |
| NY | 17,600 | [US-NYS5-010] |
| OH | 9,000 | [US-OHS5-002] |
| OK | 25,000 | [US-OK-002] |
| OR | 56,700 | [US-ORS5-003] |
| PA | 10,000 | [US-PAS5-019] |
| RI | 30,800 | [US-RIP9V-001] |
| SC | 14,000 | [US-SCS5-014] |
| SD | 15,000 | [US-SDS5-002] |
| TN | 7,000 | [US-TNS5-002] |
| TX | 9,000 | [US-TXS5-007] |
| UT | 50,700 | [US-UTS5-005] |
| VA | 8,000 | [US-VAB5-401] |
| VT | 15,400 | [US-VTS5-004] |
| WA | 78,200 | [US-WAS5-012] |
| WI | 14,000 | [US-WIS5-014] |
| WV | 9,500 | [US-WVS5-001] |
| WY | 33,800 | [US-WYS5-008] |

Many States count wages already reported by the same employer to another State's UI in the same year toward their own base (for example `multi.sui.other_state_wage_credit.ca` [US-MULTIS5-010], `multi.sui.other_state_wage_credit.fl` [US-FLS5-020]); some do not (`multi.sui.other_state_wage_credit.ia` [US-IAS5-024]; `mt.sui.wage_base.other_state_credit` [US-MTS5-025]). the multistate reference keys each State.

The States whose other-State wage credit is not yet established are listed in the multistate reference (MULTI.3), each with its own research marker.

State UI wage definitions also differ from FICA wages for deferrals and cafeteria-plan reductions (examples: `nj.sui.wages.401k_included` [US-NJS5-017]; `va.sui.wages.401k_included` [US-VAS5-014]; `ak.sui.wages.excludes_401k_deferrals` [US-AKS5-005]; `ri.ui_tdi.wages.401k_section125_excluded` [US-RIS5-017]).

### Clarify the legal definitions of any specific terms used.

| Term | Meaning in this guide | Fact |
|---|---|---|
| FICA wages | Remuneration for employment subject to OASDI and Medicare, before the OASDI cap | `fed.fica.*` |
| Wage base | Annual cap per employer and calendar year on the wages subject to a contribution | [US-FEDS5-005] |
| Localization | First step of the UI coverage test: service entirely within the State, or out-of-State service incidental | [US-MULTIS5-017] |
| `sui_state` | Result of the localization test, a routing key on the employee master data | [US-MULTIS5-017] |
| Credit reduction | Reduction of the FUTA credit for a State with an outstanding Title XII advance | [US-FED-014] |

### Deliverable: Provide a comprehensive summary of current contribution rates. Describe rates across various regions and residential statuses, including tiers, ceilings, floors, variations by age or gender.

Federal rates are uniform across States and residence statuses; the tables of §5.1 are the rate summary. Variations:

| Variation | Rule | Fact |
|---|---|---|
| Ceiling | OASDI USD 184,500 (2026); USD 192,300 published for 2027 (medium confidence) | [US-FEDS5-005]; [US-FEDB5-401] |
| Tier above a threshold | Additional Medicare above USD 200,000 | [US-FEDS5-005] |
| Region (FUTA) | Credit reduction for the State of the wages when the State carries an outstanding Title XII advance; the 2026 credit-reduction States are stated in the limitation below this table (open gap RQ-402) | [US-FED-014] |
| Region (State programmes) | SUI, SDI, PFML per State (§5.1) | annexes |
| Nonresident alien | The NRA withholding add-on has no FICA or FUTA effect; FICA and FUTA apply to actual wages unless one of these exemptions applies: pay of an F-1, J-1, M-1 or Q nonimmigrant exempt from FICA: yes [US-FEDR2-001]; Exempt: pay of a nonresident alien in F-1, J-1, M-1 or Q status for services that carry out the purpose of admission, on or off campus, including authorized Curricular and Optional Practical Training. Not exempt: other employment of the same person (e.g. an unrelated part-time job), and any pay once the person is a resident alien. [US-FEDS5-016]; the same pay exempt from FUTA: yes [US-FEDR2-002]; nonresident aliens in other visa classes liable to FICA: yes [US-FEDS5-016]; Wages are exempt from employee FICA (IRC 3101(c)) and employer FICA (IRC 3111(c)) while a section 233 Social Security Act agreement is in effect, to the extent the agreement makes them subject exclusively to the foreign social security system. [US-FEDR2-003] | coverage row `non_resident_employee` [US-FEDS5-002, US-FEDS5-016, US-MULTIS5-017, US-MULTI-021, US-MULTIS5-013] |
| Age | No age-based rates; age-based exemptions only: household workers under 18 (unless principal occupation), family employment, students (§5.2) | [US-FEDS5-029]; `fed.family_employment.treatment` [US-FEDS5-029] |
| Gender | No gender-based rate or exemption in the federal or State sources read | |

Not configured in this release (open gap RQ-402): The 2026 FUTA credit reductions for California and the U.S. Virgin Islands become final only if the Title XII advances remain unpaid on 2026-11-10; the potential rates and the related items are in the federal reference (FED.3).

**Massachusetts PFML split (decision recorded).** The employee may bear part of each component; the split changes on 2027-01-01:

| Period | Split | Fact |
|---|---|---|
| 2026 | family 0.18% (up to 100% from employee) + medical 0.70% (employee up to 40% = 0.28%, employer 0.42%) | [US-MAS5-012] |
| From 2027 | family 0.70% (employee up to 40% = 0.28%, employer 0.42%) + medical 0.18% (up to 100% from employee); total 0.88% | [US-MAS5-012] |

Decision: Follow DFML: 2026 split unchanged, swap from 2027-01-01 (Ch. 101/2026 s.45 conflict recorded) [US-MAS5-012; US-MAS5-026]. The Act's section 45 makes the swap apply for taxable years beginning on or after 1 January 2026 [US-MAS5-026], while the Department of Family and Medical Leave implements it from 2027 [US-MAS5-012]; contributions are set per calendar year by the Department, and the Act gives no mechanism to re-split amounts already withheld. Massachusetts rates apply to wages **earned** on or after 1 January (coverage row `accrual_vs_payment` [US-FED-003, US-FED-006, US-MULTIS5-009, US-MAS5-012]).

Not configured in this release (open gap RQ-540): Ch. 101/2026 s.45 says ss.25-26 apply for taxable years beginning on or after 2026-01-01; DFML implements the swap from 2027-01-01. Decision taken: follow DFML (rows US-MAS5-026, US-MAS5-012).

## 5.2 Calculation Logic and Edge Cases

### What is the step-by-step calculation logic for all types of social security contributions?

```
for each contribution c with rate r_c and annual cap cap_c (None = no cap):
  base_ytd_before = taxable wages of c already paid by this employer this calendar year
  room            = cap_c - base_ytd_before            (infinite when no cap)
  taxable_period  = min(period_wages_c, max(0, room))
  amount          = round_half_up(taxable_period x r_c, 0.01)
# never annualise and divide; weekly-capped programmes (NY DBL, HI TDI) cap per week
```

Federal application (coverage row `resident_employee` [US-FEDS5-001, US-FEDS5-005, US-FEDS5-007, US-MULTIS5-017]): OASDI 6.2% + 6.2% to USD 184,500; Medicare 1.45% + 1.45%; Additional Medicare 0.9% above USD 200,000; FUTA 0.6% net on USD 7,000; SUI per `sui_state`.

### Are contributions based on actual or standard salary?

Actual wages paid. No notional or standard salary appears in the federal or State bases of the facts; every base is wages paid in the period by payment date (coverage row `accrual_vs_payment` [US-FED-003, US-FED-006, US-MULTIS5-009, US-MAS5-012]).

### Describe rules for eligibility, joining month, termination month, mid-period hires, mid-period terminations, and mid-period salary changes.

No proration and no minimum period: contributions apply to the wages paid in the period from the first payment (coverage row `mid_month_joiner_and_leaver` [US-FEDS5-001, US-FEDS5-024, US-MULTIS5-009]). Each base runs per employer per calendar year from the first payment; a salary change takes effect through the wages of the period in which it is paid. Successor employers may carry FUTA wages over ([US-MULTIS5-009]).

### Do different payment frequencies affect contribution rates or parameters?

Rates and annual caps do not change with frequency. Weekly-defined parameters do: New York DBL is capped at USD 0.60 a week [US-NYB5-401] and Hawaii TDI at USD 7.50 a week [US-HIS5-015]; convert these per pay period.

### Detail variations based on employee age or gender.

| Group | Treatment | Fact |
|---|---|---|
| Household employees | FICA when cash wages reach USD 3,000 in 2026 (exempt under 18 unless principal occupation); FUTA when USD 1,000 cash wages in any quarter | [US-FEDS5-029] |
| Family employment | Child under 18 of a sole proprietor/parents-only partnership: FICA exempt, FUTA exempt under 21; spouse: FUTA exempt; parent employed by child: FUTA exempt | [US-FEDS5-029] |
| Students | Private school/college students: FIT withheld, FICA and FUTA exempt; public school: FICA exempt unless sec. 218 agreement; work-experience full-time student: FICA taxable | [US-FEDS5-029] |
| Gender | No variation in the facts | |

### Is there a minimum number of working days required for contributions?

No. The thresholds are monetary, not day counts:

| Group | Threshold | Fact |
|---|---|---|
| Agricultural workers | USD 150 cash wages to a worker in the year, or USD 2,500 total farm pay; FUTA at USD 20,000 in a quarter | [US-FEDR3-006] |
| Election workers | FICA from USD 2,500 | [US-FEDS5-003] |
| Household employees | See above (USD 3,000) | [US-FEDS5-029] |

### How are contributions calculated for Board of Directors who are also employees?

Corporate officers are employees: officer wages bear FICA and FUTA and State UI covers them; directors' fees without employment are not wages and stay outside payroll (coverage row `officers_without_employment_contract` [US-OKS5-010, US-FLS5-005, US-FEDR3-005]). Statutory employees: FICA withheld, no FIT withholding; W-2 box 13 checked; FUTA for drivers and traveling salespersons only [US-FEDR3-005]. Full treatment: Module 11.

### Are year-end adjustments required?

No employer regularisation (coverage row `annual_regularisation` [US-FEDS5-007, US-FEDS5-005, US-FEDS5-006]): the employer stops OASDI at the cap and starts Additional Medicare above the threshold per employer; it reconciles four quarterly returns to the annual W-2/W-3 and corrects through the federal correction forms. Excess OASDI caused by several employers is refunded to the employee at assessment (coverage row `multiple_employers` [US-FEDS5-006, US-MULTIS5-009, US-FEDS5-005]). The FUTA credit reduction of the year is settled on the annual return.

Not configured in this release (open gap RQ-533): Common-paymaster relief for related employers (multiple_employers row) is not established from an official source.

## 5.3 Voluntary Contributions & Private Schemes

### Can employees and employers make additional voluntary contributions?

Yes, to employer retirement and health-savings plans, within annual limits:

| Plan | 2026 limit | Fact |
|---|---|---|
| 401(k)-type elective deferral | USD 24,500; catch-up USD 8,000 (50+), USD 11,250 (60 to 63) | [US-FED-023] |
| SIMPLE plan deferral | USD 17,000 | [US-FED-023] |
| HSA | USD 4,400 self-only / USD 8,750 family | [US-FED-024] |
| Health FSA | USD 3,400; carry-over up to USD 680 | [US-FEDS5-010] |

An employer's voluntary payment of the employee's State PFML share is W-2 wages [US-FEDS5-007].

### Which employee contributions are allowed as pre-tax deductions?

Elective deferrals, health FSA and HSA salary reductions are salary-reduction arrangements (limits above). Which federal base each one reduces is in Module 3, Step 2 [US-FEDS5-029]; State treatment differs (`ca.wages.401k_deferrals` [US-CAS5-019]; `pa.bik.pa.401k_403b_457.taxable` [US-PAS5-011]).

### Are there private insurance schemes with employer and employee contributions?

| Scheme | Rule | Fact |
|---|---|---|
| New York DBL / PFL | Insured with a private carrier or the State fund; employee share withheld by payroll (§5.1) | [US-NYB5-401] |
| Hawaii TDI | Insurer-funded, no State return; employee share up to the cap (§5.1) | [US-HIS5-014] |
| California voluntary disability plan | Employer plan in place of State SDI; W-2 box 14 label VPDI | [US-CAS5-018] |

### What documents or declarations are required from an employee?

None for FICA or FUTA. Retirement and HSA salary reductions require the employee's plan election; the Washington paid-leave/WA Cares report carries the employee's WA Cares exemption status [US-WAB5-003].


## Fact index

Every value above with its key, effective period and register id.

| Key | Value | Effective | Register id |
|---|---|---|---|
| `ak.sui.employee.rate` | 0.5 | from 2026-01-01 to 2026-12-31 | US-AKS5-003 |
| `ak.sui.wage_base` | 54,200 | from 2026-01-01 to 2026-12-31 | US-AKS5-003 |
| `al.sui.wage_base` | 8,000 | from 2026-01-01 | US-ALS5-009 |
| `ar.sui.wage_base` | 7,000 | from 2026-01-01 | US-ARP9V-001 |
| `az.sui.wage_base` | 8,000 | from 2026-01-01 | US-AZP9V-001 |
| `ca.sdi.employee.rate` | 1.3 | from 2026-01-01 to 2026-12-31 | US-CAP7-002 |
| `ca.sdi.voluntary_plan.w2_box14_label` | VPDI | from 2026-01-01 | US-CAS5-018 |
| `ca.sui.wage_base` | 7,000 | from 2026-01-01 | US-CAS5-016 |
| `co.famli.employee.rate` | 0.44 | from 2026-01-01 to 2026-12-31 | US-COB5-003 |
| `co.famli.employer.rate` | 0.44 | from 2026-01-01 to 2026-12-31 | US-COB5-003 |
| `co.famli.total.rate` | 0.86 | from 2027-01-01 | US-COB5-301 |
| `co.famli.total.rate` | 0.88 | from 2026-01-01 to 2026-12-31 | US-COB5-401 |
| `co.sui.wage_base` | 30,600 | from 2026-01-01 to 2026-12-31 | US-COP51-003 |
| `ct.pfml.employee.rate` | 0.5 | from 2026-01-01 to 2026-12-31 | US-CTP7-001 |
| `ct.sui.wage_base` | 27,000 | from 2026-01-01 to 2026-12-31 | US-CTP9V-001 |
| `dc.pfml.employer.rate` | 0.75 | from 2026-01-01 | US-DCS5-020 |
| `dc.sui.wage_base` | 9,000 | from 2026-01-01 | US-DCS5-017 |
| `de.pfml.employee_share.max_percent` | 50 | from 2025-01-01 | US-DES5-012 |
| `de.pfml.rate.family_caregiving` | 0.08 | from 2025-01-01 to 2026-12-31 | US-DES5-012 |
| `de.pfml.rate.medical` | 0.4 | from 2025-01-01 to 2026-12-31 | US-DES5-012 |
| `de.pfml.rate.parental` | 0.32 | from 2025-01-01 to 2026-12-31 | US-DES5-012 |
| `de.pfml.rate.total` | 0.8 | from 2025-01-01 to 2026-12-31 | US-DES5-012 |
| `de.sui.wage_base` | 14,500 | from 2026-01-01 to 2026-12-31 | US-DES5-010 |
| `fed.agricultural.futa_quarter_threshold` | 20,000 | from 2026-01-01 | US-FEDR3-006 |
| `fed.agricultural.per_worker_threshold` | 150 | from 2026-01-01 | US-FEDR3-006 |
| `fed.agricultural.total_threshold` | 2,500 | from 2026-01-01 | US-FEDR3-006 |
| `fed.bik.health_fsa.carryover_max` | 680 | from 2026-01-01 to 2026-12-31 | US-FEDS5-010 |
| `fed.bik.health_fsa.salary_reduction_cap` | 3,400 | from 2026-01-01 to 2026-12-31 | US-FEDS5-010 |
| `fed.election_worker.fica_threshold` | 2,500 | from 2026-01-01 to 2026-12-31 | US-FEDS5-003 |
| `fed.family_employment.treatment` | Child under 18 of a sole proprietor/parents-only partnership: FICA exempt, FUTA exempt under 21; spouse: FUTA exempt; parent employed by child: FUTA exempt | from 2026-01-01 | US-FEDS5-029 |
| `fed.fica.addl_medicare.rate` | 0.9 | from 2026-01-01 to 2026-12-31 | US-FEDS5-005 |
| `fed.fica.addl_medicare.withholding_threshold` | 200,000 | from 2026-01-01 to 2026-12-31 | US-FEDS5-005 |
| `fed.fica.medicare.rate.employee` | 1.45 | from 2026-01-01 to 2026-12-31 | US-FEDS5-005 |
| `fed.fica.medicare.rate.employer` | 1.45 | from 2026-01-01 to 2026-12-31 | US-FEDS5-005 |
| `fed.fica.nra.fjmq_exempt.scope` | Exempt: pay of a nonresident alien in F-1, J-1, M-1 or Q status for services that carry out the purpose of admission, on or off campus, including authorized Curricular and Optional Practical Training. Not exempt: other employment of the same person (e.g. an unrelated part-time job), and any pay once the person is a resident alien. | from 2026-01-01 | US-FEDS5-016 |
| `fed.fica.oasdi.rate.employee` | 6.2 | from 2026-01-01 to 2026-12-31 | US-FEDS5-005 |
| `fed.fica.oasdi.rate.employer` | 6.2 | from 2026-01-01 to 2026-12-31 | US-FEDS5-005 |
| `fed.fica.oasdi.wage_base` | 184,500 | from 2026-01-01 to 2026-12-31 | US-FEDS5-005 |
| `fed.fica.oasdi.wage_base` | 192,300 | from 2027-01-01 to 2027-12-31 | US-FEDB5-401 |
| `fed.fica.totalization.exemption_rule` | Wages are exempt from employee FICA (IRC 3101(c)) and employer FICA (IRC 3111(c)) while a section 233 Social Security Act agreement is in effect, to the extent the agreement makes them subject exclusively to the foreign social security system. | from 2026-01-01 | US-FEDR2-003 |
| `fed.futa.credit.max` | 5.4 | from 2025-01-01 | US-FED-007 |
| `fed.futa.legal_basis.state_credit` | State UI contributions credited against FUTA, capped at 90% of the tax; credit reduced for states with outstanding Title XII advances | from 2026-01-01 | US-FED-014 |
| `fed.futa.rate.gross` | 6 | from 2025-01-01 | US-FED-007 |
| `fed.futa.rate.net` | 0.6 | from 2025-01-01 | US-FED-007 |
| `fed.futa.wage_base` | 7,000 | from 2025-01-01 | US-FED-007 |
| `fed.household.fica_cash_threshold` | 3,000 | from 2026-01-01 to 2026-12-31 | US-FEDS5-029 |
| `fed.household.futa_quarter_threshold` | 1,000 | from 2026-01-01 | US-FEDS5-029 |
| `fed.hsa.limit.family` | 8,750 | from 2026-01-01 to 2026-12-31 | US-FED-024 |
| `fed.hsa.limit.self_only` | 4,400 | from 2026-01-01 to 2026-12-31 | US-FED-024 |
| `fed.retirement.401k.catch_up_50` | 8,000 | from 2026-01-01 to 2026-12-31 | US-FED-023 |
| `fed.retirement.401k.catch_up_60_63` | 11,250 | from 2026-01-01 to 2026-12-31 | US-FED-023 |
| `fed.retirement.401k.elective_deferral_limit` | 24,500 | from 2026-01-01 to 2026-12-31 | US-FED-023 |
| `fed.retirement.simple.deferral_limit` | 17,000 | from 2026-01-01 to 2026-12-31 | US-FED-023 |
| `fed.statutory_employee.treatment` | FICA withheld, no FIT withholding; W-2 box 13 checked; FUTA for drivers and traveling salespersons only | from 2026-01-01 | US-FEDR3-005 |
| `fed.students.treatment` | Private school/college students: FIT withheld, FICA and FUTA exempt; public school: FICA exempt unless sec. 218 agreement; work-experience full-time student: FICA taxable | from 2026-01-01 | US-FEDS5-029 |
| `fl.sui.wage_base` | 7,000 | from 2015-01-01 | US-FLS5-003 |
| `ga.sui.wage_base` | 9,500 | from 2013-01-01 | US-GAW1B-001 |
| `hi.sui.wage_base` | 64,500 | from 2026-01-01 to 2026-12-31 | US-HIP9V-001 |
| `hi.tdi.employee.max_rate` | 0.5 | from 2026-01-01 | US-HIS5-014 |
| `hi.tdi.employee.max_weekly_deduction` | 7.50 | from 2026-01-01 to 2026-12-31 | US-HIS5-015 |
| `ia.sui.wage_base` | 20,400 | from 2026-01-01 to 2026-12-31 | US-IAS5-009 |
| `id.sui.wage_base` | 58,300 | from 2026-01-01 to 2026-12-31 | US-IDB5-402 |
| `il.sui.wage_base` | 14,250 | from 2026-01-01 to 2026-12-31 | US-ILS5-015 |
| `in.sui.wage_base` | 9,500 | from 2011-01-01 | US-INS5-014 |
| `ks.sui.wage_base` | 15,100 | from 2026-01-01 to 2026-12-31 | US-KSS5-023 |
| `ky.sui.wage_base` | 12,000 | from 2026-01-01 to 2026-12-31 | US-KY-003 |
| `la.sui.wage_base` | 7,000 | from 2026-01-01 to 2026-12-31 | US-LAP9V-001 |
| `ma.pfml.split` | family 0.18% (up to 100% from employee) + medical 0.70% (employee up to 40% = 0.28%, employer 0.42%) | from 2026-01-01 to 2026-12-31 | US-MAS5-012 |
| `ma.pfml.split` | family 0.70% (employee up to 40% = 0.28%, employer 0.42%) + medical 0.18% (up to 100% from employee); total 0.88% | from 2027-01-01 | US-MAS5-012 |
| `ma.pfml.total.rate` | 0.88 | from 2026-01-01 | US-MAS5-012 |
| `ma.sui.wage_base` | 15,000 | from 2015-01-01 to 2026-12-31 | US-MAP51-005 |
| `md.pfml.employee_share.max_percent` | 50 | from 2027-01-01 | US-MDS5-014 |
| `md.pfml.rate.total` | 0.9 | from 2027-01-01 | US-MDS5-014 |
| `md.sui.wage_base` | 8,500 | from 2026-01-01 | US-MDB5-401 |
| `me.pfml.employee.max_rate` | 0.5 | from 2025-01-01 to 2027-12-31 | US-MEP6-001 |
| `me.pfml.rate.total.15_plus` | 1 | from 2025-01-01 to 2027-12-31 | US-MEP6-001 |
| `me.pfml.rate.total.under_15` | 0.5 | from 2025-01-01 to 2027-12-31 | US-MEP6-001 |
| `me.sui.wage_base` | 12,000 | from 2026-01-01 | US-MES5-020 |
| `mi.sui.wage_base` | 9,000 | from 2026-01-01 to 2026-12-31 | US-MIS5-025 |
| `mn.pfml.employee.max_share.rate` | 0.44 | from 2026-01-01 to 2027-12-31 | US-MNP52-003 |
| `mn.pfml.rate.family` | 0.27 | from 2026-01-01 to 2027-12-31 | US-MNP52-003 |
| `mn.pfml.rate.medical` | 0.61 | from 2026-01-01 to 2027-12-31 | US-MNP52-003 |
| `mn.pfml.rate.total` | 0.88 | from 2026-01-01 to 2027-12-31 | US-MNP52-003 |
| `mn.pfml.small_employer.rate` | 0.66 | from 2026-01-01 to 2027-12-31 | US-MNP52-003 |
| `mn.sui.wage_base` | 44,000 | from 2026-01-01 to 2026-12-31 | US-MNP52-001 |
| `mo.sui.wage_base` | 9,000 | from 2026-01-01 to 2026-12-31 | US-MOP9W-002 |
| `ms.sui.wage_base` | 14,000 | from 2011-01-01 | US-MSS5-011 |
| `mt.sui.wage_base` | 47,300 | from 2026-01-01 to 2026-12-31 | US-MTP51-005 |
| `multi.futa.wage_base.scope` | FUTA 7,000 counts remuneration paid by the employer in the calendar year across all States: one base per employer, not per State; successor carry-over | from 2026-01-01 | US-MULTIS5-009 |
| `multi.pfml.coverage_test.default` | Key the PFML/SDI premium State to sui_state unless the State annex proves otherwise (WA, CT, ME, OR, MD, RI proven; DC and DE differ) | from 2026-01-01 to 2027-06-30 | US-MULTIS5-024 |
| `multi.sui.employee_contribution_states` | AK, NJ, PA (only three States levy employee UI contributions; take 2026 rates from the State annexes) | from 2023-01-01 | US-FEDP52-006 |
| `multi.sui.localization.telecommuting` | UIPL 20-04 (2004, continuing) reissues the UIPL 291 interpretation with telecommuting examples | from 2004-05-10 | US-MULTIS5-016 |
| `multi.sui.localization_test` | One State covers the entire service with one employer, in order: (1) localized (entirely in the State, or out-of-state service incidental: temporary, transitory, isolated); (2) else some service in the base-of-operations State; (3) else some service in the State of direction or control; (4) else some service in the State of residence | from 2026-01-01 | US-MULTIS5-017 |
| `multi.sui.reciprocal_coverage_election` | Where no test resolves the case, employer, employee and States may elect coverage of all service in one State (performance, residence or place of business); CA CUIC 602/603 | from 2026-01-01 | US-MULTIS5-010 |
| `nc.sui.wage_base` | 34,200 | from 2026-01-01 to 2026-12-31 | US-NCB5-401 |
| `nd.sui.wage_base` | 46,600 | from 2026-01-01 to 2026-12-31 | US-NDS5-012 |
| `ne.sui.wage_base` | 9,000 | from 2026-01-01 to 2026-12-31 | US-NEP51-003 |
| `nh.sui.wage_base` | 14,000 | from 2026-01-01 | US-NHS5-007 |
| `nj.fli.employee.max_annual` | 393.53 | from 2026-01-01 to 2026-12-31 | US-NJP51-004 |
| `nj.fli.employee.rate` | 0.23 | from 2026-01-01 to 2026-12-31 | US-NJS5-010 |
| `nj.sui.employee.rate` | 0.3825 | from 2026-01-01 | US-NJS5-010 |
| `nj.sui.wage_base` | 44,800 | from 2026-01-01 to 2026-12-31 | US-NJS5-010 |
| `nj.tdi.employee.max_annual` | 325.09 | from 2026-01-01 to 2026-12-31 | US-NJP51-004 |
| `nj.tdi.employee.rate` | 0.19 | from 2026-01-01 to 2026-12-31 | US-NJS5-010 |
| `nm.sui.wage_base` | 34,800 | from 2026-01-01 to 2026-12-31 | US-NMP51-001 |
| `nm.wc.admin_fee.employee.quarterly` | 2.25 | from 2025-07-01 to 2028-06-30 | US-NMR3-001 |
| `nm.wc.admin_fee.employer.quarterly` | 2.55 | from 2025-07-01 to 2028-06-30 | US-NMR3-001 |
| `nv.sui.wage_base` | 43,700 | from 2026-01-01 to 2026-12-31 | US-NVP51-001 |
| `ny.dbl.employee.max_weekly` | 0.60 | from 2026-01-01 | US-NYB5-401 |
| `ny.dbl.employee.rate` | 0.5 | from 2026-01-01 | US-NYB5-401 |
| `ny.pfl.employee.max_annual` | 411.91 | from 2026-01-01 to 2026-12-31 | US-NYP8-001 |
| `ny.pfl.employee.rate` | 0.432 | from 2026-01-01 to 2026-12-31 | US-NYP8-001 |
| `ny.sui.wage_base` | 17,600 | from 2026-01-01 to 2026-12-31 | US-NYS5-010 |
| `oh.sui.wage_base` | 9,000 | from 2026-01-01 to 2026-12-31 | US-OHS5-002 |
| `ok.sui.wage_base` | 25,000 | from 2026-01-01 to 2026-12-31 | US-OK-002 |
| `or.pfml.employee.share` | 60 | from 2023-01-01 | US-ORS5-013 |
| `or.pfml.rate.total` | 1 | from 2026-01-01 to 2026-12-31 | US-ORS5-003 |
| `or.sui.wage_base` | 56,700 | from 2026-01-01 to 2026-12-31 | US-ORS5-003 |
| `or.transit.lane.employer.rate` | 0.8 | from 2026-01-01 to 2026-12-31 | US-ORS5-010 |
| `or.transit.trimet.employer.rate` | 0.8237 | from 2026-01-01 to 2026-12-31 | US-ORS5-010 |
| `pa.sui.employee.rate` | 0.07 | from 2023-01-01 | US-PAS5-019 |
| `pa.sui.wage_base` | 10,000 | from 2018-01-01 | US-PAS5-019 |
| `practice.ma.pfml_split` | Follow DFML: 2026 split unchanged, swap from 2027-01-01 (Ch. 101/2026 s.45 conflict recorded) | from 2026-01-01 | US-MAS5-012 |
| `ri.sui.wage_base` | 30,800 | from 2026-01-01 to 2026-12-31 | US-RIP9V-001 |
| `ri.tdi.employee.max_annual` | 1,100 | from 2026-01-01 to 2026-12-31 | US-RIP9V-001 |
| `ri.tdi.employee.rate` | 1.1 | from 2026-01-01 to 2026-12-31 | US-RIP9V-001 |
| `sc.sui.wage_base` | 14,000 | from 2015-01-01 | US-SCS5-014 |
| `sd.sui.wage_base` | 15,000 | from 2015-01-01 | US-SDS5-002 |
| `tn.sui.wage_base` | 7,000 | from 2018-01-01 to 2026-12-31 | US-TNS5-002 |
| `tx.sui.wage_base` | 9,000 | from 2026-01-01 | US-TXS5-007 |
| `ut.sui.wage_base` | 50,700 | from 2026-01-01 to 2026-12-31 | US-UTS5-005 |
| `va.sui.wage_base` | 8,000 | from 2026-01-01 | US-VAB5-401 |
| `vt.sui.wage_base` | 15,400 | from 2026-01-01 to 2026-12-31 | US-VTS5-004 |
| `wa.ltc.wa_cares.employee.rate` | 0.58 | from 2023-07-01 | US-WAS5-016 |
| `wa.pfml.employee.share` | 70.7 | from 2027-01-01 | US-WAS5-015 |
| `wa.pfml.employee.share` | 71.43 | from 2026-01-01 to 2026-12-31 | US-WAB5-002 |
| `wa.pfml.small_employer.threshold` | 50 | from 2026-01-01 | US-WAS5-011 |
| `wa.pfml.total.rate` | 1.13 | from 2026-01-01 to 2026-12-31 | US-WAS5-015 |
| `wa.pfml.total.rate` | 1.2 | from 2027-01-01 | US-WAS5-015 |
| `wa.pfml.wage_cap.annual` | 184,500 | from 2026-01-01 to 2026-12-31 | US-WAB5-002 |
| `wa.sui.wage_base` | 78,200 | from 2026-01-01 to 2026-12-31 | US-WAS5-012 |
| `wa.wc.employee_deduction.rule` | employer (not self-insured) deducts from each worker one-half of the medical aid premium per hour per risk class | from 2026-01-01 to 2026-12-31 | US-WAS7-001 |
| `wi.sui.wage_base` | 14,000 | from 2013-01-01 | US-WIS5-014 |
| `wv.sui.wage_base` | 9,500 | from 2024-07-01 | US-WVS5-001 |
| `wy.sui.wage_base` | 33,800 | from 2026-01-01 to 2026-12-31 | US-WYS5-008 |
