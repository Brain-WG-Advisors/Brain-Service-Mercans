# Module 6: Income Tax Withholding System
*Purpose: To define the entire income tax withholding system.*

## 6.0 Resident vs non-resident matrix (federal income tax)

Resident = US citizen or resident alien; non-resident = nonresident alien (NRA). State residence is treated in §6.2. Source rows: coverage row `non_resident_employee` [US-FEDS5-002, US-FEDS5-016, US-MULTIS5-017, US-MULTI-021, US-MULTIS5-013]; coverage row `resident_employee` [US-FEDS5-001, US-FEDS5-005, US-FEDS5-007, US-MULTIS5-017].

| Income type | Resident: rate, method, base | Non-resident alien: rate, method, base |
|---|---|---|
| Regular salary | Pub. 15-T Worksheet 1A, STANDARD or Step-2 schedule by filing status; base = income-tax wages annualised, less line 1g (USD 8,600 / USD 12,900 married filing jointly) when Step 2 is not checked [US-FEDS5-001] | Same worksheet; Form W-4 per Check Single or MFS regardless of marital status; write NRA below Step 4(c); exempt not allowed; Step 3 only for residents of Canada, Mexico, South Korea or India (students/apprentices) [US-FEDS5-015]; base = wages **plus** the NRA add-on (Table 2: USD 16,100 a year; Table 1: USD 11,800), for the computation only: not on the W-2, no FICA/FUTA effect [US-FEDS5-002] |
| Annual / 13th-month bonus | Supplemental: flat 22% (optional) or aggregate; 37% mandatory above USD 1,000,000 in the year [US-FEDS5-003] | Supplemental, same rates; the NRA add-on is **not** applied to the flat 22% / 37% methods [US-FEDS5-002] |
| Severance | Wages for income tax, FICA and FUTA `fed.severance.is_wages` [US-FEDS5-029]; supplemental methods as for a bonus (coverage row `termination_and_final_pay` [US-FEDS5-025, US-FEDS5-029, US-FED-016]) | Wages; supplemental methods as for a bonus, NRA add-on not applied to the flat methods [US-FEDS5-002] |
| Equity (stock options, RSUs) | Resident employee, 2026: (1) Nonstatutory option (NSO): the spread at exercise (FMV - price) is wages - a taxable fringe benefit subject to the supplemental-wage rules (22% optional flat or aggregate; 37% on supplemental wages above 1,000,000), FICA and FUTA wages, timed at the actual exercise (transfer) date; W-2 boxes 1, 3 (to the SS base), 5 and box 12 code V. (2) ISO and ESPP options: no FICA or FUTA at grant, exercise or disposition; no FIT withholding required on a disqualifying disposition or on the ESPP discount at a qualifying disposition, but the ordinary income is W-2 box 1 wages. (3) Restricted stock (actual shares subject to forfeiture): FMV minus amount paid is wages when substantially vested (or at transfer with an 83(b) election). (4) RSU (legally binding right to receive shares in a future year): FICA and FUTA wages at the later of service performance and vesting (special timing rule, 26 CFR 31.3121(v)(2)-1 / 31.3306(r)(2)-1); FIT withholding when the shares are delivered (settlement) as supplemental wages. (5) 83(i) election (private company): FIT deferred up to 5 years and withheld at 37% when included; FICA/FUTA not deferred; W-2 codes GG/HH. [US-FEDQ1-001]; RSU FICA/FUTA timing: Later of the performance of the services and the date the right is no longer subject to a substantial risk of forfeiture (vesting); FUTA follows the same rule [US-FEDQ1-004]; 83(i) deferred income withheld at 37% [US-FEDQ1-001] | Nonresident alien employee, 2026: equity income is wages subject to graduated withholding as for residents, with the Pub. 15-T NRA add-on, except that no add-on applies when the payment is withheld at the 22% optional or 37% mandatory flat supplemental rate. Only the U.S.-source part is wages for U.S. withholding: compensation attributable to several years is sourced on a time basis (U.S. workdays / total workdays over the period to which it is attributable, facts and circumstances). FICA/FUTA follow the resident rules (NSO spread and RSU at vesting are FICA wages) unless the employee is exempt as an F-1/J-1/M-1/Q nonimmigrant. Reporting on Form W-2; Form 1042-S only for wages exempt under a treaty claimed on Form 8233. [US-FEDQ1-006] |
| Labour-service pay | Independent contractors and Form 1099-NEC reporting are out of scope (owner instruction of 2026-10-29) [US-OWN-008]. | Treaty-exempt personal-service wages: Treaty-exempt wages claimed on Form 8233 are reported on Form 1042-S (not W-2 box 1); 2026 Forms 1042-S due 2027-03-15 and must be e-filed via IRIS [US-FEDS5-016]; commercial-traveler exception: present at most 90 days and paid at most USD 3,000 by a foreign employer [US-FEDS5-016] |
| Social security (FICA) and FUTA on wages | FICA (OASDI up to the annual wage base, Medicare) and FUTA on wages, as in Module 5 (5.1) [US-FEDS5-005] [US-FED-007] | As for residents, unless an exemption applies: pay of an F-1, J-1, M-1 or Q nonimmigrant exempt from FICA: yes [US-FEDR2-001]; Exempt: pay of a nonresident alien in F-1, J-1, M-1 or Q status for services that carry out the purpose of admission, on or off campus, including authorized Curricular and Optional Practical Training. Not exempt: other employment of the same person (e.g. an unrelated part-time job), and any pay once the person is a resident alien. [US-FEDS5-016]; the same pay exempt from FUTA: yes [US-FEDR2-002]; nonresident aliens in other visa classes liable to FICA: yes [US-FEDS5-016]; Wages are exempt from employee FICA (IRC 3101(c)) and employer FICA (IRC 3111(c)) while a section 233 Social Security Act agreement is in effect, to the extent the agreement makes them subject exclusively to the foreign social security system. [US-FEDR2-003] (Module 5, 5.1) |
| Benefits in kind | Taxable fringe benefits are wages unless excluded (Module 7 §7.2); group-term life cost above USD 50,000 is FICA wages and income-tax withholding is not required [US-FEDS5-008] | Nonresident alien employee, 2026: taxable fringe benefits are wages subject to graduated FIT withholding. Added to regular wages for the payroll period, they are withheld with the Pub. 15-T NRA add-on; withheld separately at the 22% optional flat supplemental rate (37% above 1,000,000), no add-on applies. Noncash fringes may be treated as paid per pay period, quarter, half-year or year (at least annually). FICA and FUTA apply as for residents unless the employee is an F-1/J-1/M-1/Q nonimmigrant. Group-term life cost over 50,000: FICA wages, no FIT withholding and no FUTA required, W-2 boxes 1, 3, 5 and box 12 code C. Only U.S.-source fringes are wages for withholding: housing, education, local transportation (main job location), tax reimbursement (taxing jurisdiction), hazardous duty and moving (new main job location) are sourced geographically, other fringes on a time basis. Reported on Form W-2 (Form 1042-S only for treaty-exempt wages on Form 8233). [US-FEDQ1-008] |

## 6.1 System Overview and Methodology

### Describe the country's income tax withholding system.

Pay-as-you-earn withholding per pay period, in parallel layers. Federal: 26 U.S.C. 3402: employer withholds federal income tax per tables/procedures prescribed by the Secretary (federal tax only) [US-FED-012]; method IRS Pub. 15-T (2026) Worksheet 1A with the Annual Percentage Method tables (STANDARD schedule; Step-2-checked schedule when W-4 Step 2 box checked) [US-FEDS5-001]. There is no employer year-end income-tax regularisation: the employee settles at assessment (coverage row `annual_regularisation` [US-FEDS5-007, US-FEDS5-005, US-FEDS5-006]). Each wage-taxing State runs its own withholding on its own base and return; some localities add a local layer. Routing (which State, which locality) is decided before any computation (§6.2).

### What types of taxes are withheld by the employer?

| Tax withheld | Layer | Fact |
|---|---|---|
| Federal income tax | Federal | [US-FED-012] |
| Employee OASDI, Medicare, Additional Medicare | Federal (Module 5) | [US-FEDS5-005] |
| State income tax | State, where the State taxes wages (Module 1 lists the States without one) | annexes |
| Local income / wage / occupational taxes | Locality (coverage row `local_regimes` [US-PAS5-022, US-MIR3-002, US-INS5-009, US-MULTIS5-011]) | annexes |
| Employee shares of State programmes (UI in AK/NJ/PA, SDI/TDI, PFML, WA Cares) | State (Module 5) | annexes |

The facts also carry the federal backup-withholding rate, 24% [US-FEDS5-003].

### At what level are tax rates published (central or state)?

Each layer publishes its own. Federal: IRS Pub. 15-T tables (§6.1.1). States publish their withholding formulas or tables; the withholding instrument does not always reproduce the statutory rates:

| Pattern | State examples | Fact |
|---|---|---|
| Flat rate | Indiana 2.95% in 2026 (2.9% from 2027) plus county tax; Utah 4.45%; Georgia 4.99% statutory for 2026 (withholding 5.19% to 2026-05-10, 4.99% from 2026-05-11 [US-GA-001]); Michigan 4.25% plus city taxes | [US-INS5-009]; [US-UTS5-001]; [US-GAS5-009]; [US-MIPIT-001] |
| Graduated | Maryland top rate 6.5% plus county tax (default county rate 3.3%); California graduated tables (annex CA) | [US-MDS5-001]; [US-MDS5-003] |
| Statute differs from the withholding instrument | Ohio, Wisconsin, Nebraska, Kansas, South Carolina (trap table §6.2) | `practice.*` |
| No wage income tax | Module 1 §1.0 | `*.no_wage_tax` |

## 6.1.1 Taxable Income Definition

### Provide the statutory definition of 'Taxable Income'.

| Element | Rule | Source |
|---|---|---|
| Definition (26 U.S.C. 3401(a)) | Wages for income-tax withholding (IRC 3401(a)): all remuneration (other than fees paid to a public official) for services performed by an employee for his employer, including the cash value of all remuneration (including benefits) paid in any medium other than cash, except the exclusions in 3401(a)(1)-(23). Amounts includible in gross income under section 409A are wages. | [US-FEDQ3-001] |
| Exclusions | Exclusions relevant to private-sector employees: (a)(2) agricultural labor unless FICA wages; (a)(3) domestic service in a private home; (a)(4) non-business service under 50 a quarter; (a)(8) certain pay abroad / in possessions; (a)(12) payments to or from qualified plans (401(a) trust incl. 401(k) deferrals, 403(a), SEP 402(h), SIMPLE 408(p), governmental 457(b)); (a)(14) group-term life insurance; (a)(15) moving-expense reimbursements deductible under 217; (a)(16) non-cash tips and cash tips under 20 a month; (a)(18) 127 educational assistance, 129 dependent care, 134(b)(4)-(5); (a)(19) 74(c), 108(f)(4), 117 and 132 benefits; (a)(20) self-insured medical reimbursements; (a)(21) 106(b) Archer MSA; (a)(22) 106(d) HSA. | [US-FEDQ3-001] |

Operationally, the withholding base is the employee's income-tax wages for the period after the pre-tax deductions that reduce income-tax wages (Module 3, Step 2).

### Explain how this base is derived from total gross earnings.

```
1a  wages_period      = gross - federally excluded pre-tax deductions   (+ NRA add-on for a nonresident alien)
1c  annual_wages      = wages_period x pay_periods_per_year
1e  = 1c + W-4 Step 4(a)
1g  = 12,900 (MFJ) or 8,600 (other) if W-4 Step 2 NOT checked, else 0
1h  = W-4 Step 4(b) + 1g
1i  adjusted_annual   = max(0, 1e - 1h)
    (pre-2020 W-4: adjusted_annual = annual_wages - allowances x 4,300)
```

Facts: `fed.fit.worksheet1a.line1g.mfj` [US-FEDS5-001]; `fed.fit.worksheet1a.line1g.other` [US-FEDS5-001]; `fed.fit.allowance.pre2020_value` [US-FEDS5-001]; pay periods 2 / 4 / 12 / 24 / 26 / 52 / 260 (semiannual, quarterly, monthly, semimonthly, biweekly, weekly, daily).

### Deliverable: Provide a step-by-step decision guide to determine the correct tax schedule for an employee.

| Step | Question | Outcome | Fact |
|---|---|---|---|
| 1 | Which States and localities apply? | Work State, residence State and locality from the routing keys, then reciprocity, thresholds, convenience and federal transport limits (§6.2) | [US-MULTIS5-023] |
| 2 | Exempt checkbox on a 2026 W-4? | No federal income tax withheld for 2026 only | [US-FEDS5-006] |
| 3 | Nonresident alien? | Single schedule regardless of marital status, no exempt, add NRA add-on (Table 2 if 2020+ W-4 or first paid 2020+, else Table 1) | [US-FEDS5-015]; [US-FEDS5-002] |
| 4 | Form W-4 from 2019 or earlier? | Allowances method, each worth USD 4,300 | [US-FEDS5-001] |
| 5 | W-4 Step 2 checked? | Yes: Step-2 schedule, no line 1g. No: STANDARD schedule, line 1g subtracted | `fed.fit.step2.*`; `fed.fit.standard.*` |
| 6 | Filing status? | Married filing jointly / Single or married filing separately / Head of household column | `fed.w4.input_fields` |
| 7 | Supplemental payment? | Flat 22% or aggregate; 37% above USD 1,000,000 | [US-FEDS5-003] |
| 8 | State schedule | The State's own certificate and method (annex); defaults for a missing certificate (Module 2) | annexes |

### Deliverable: Explain the official tax calculation method with formulas and examples.

```
find row r of the schedule with floor_r <= adjusted_annual < floor_(r+1)
2e excess    = adjusted_annual - floor_r
2f           = excess x rate_r
2g tentative = cumulative_tax_r + 2f
2h period    = 2g / pay_periods_per_year
3  credits   = W-4 Step 3 / pay_periods_per_year ;  4  extra = W-4 Step 4(c)
FIT_period   = max(0, 2h - credits) + extra
```

**2026 Annual Percentage Method, STANDARD schedule (W-4 Step 2 not checked).** Floor and cumulative tax in USD; rate in %.

| Row | MFJ floor | MFJ rate | MFJ cumulative | Single/MFS floor | Single rate | Single cumulative | HoH floor | HoH rate | HoH cumulative |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 0 | 0 | 0.00 | 0 | 0 | 0.00 | 0 | 0 | 0.00 |
| 2 | 19,300 | 10 | 0.00 | 7,500 | 10 | 0.00 | 15,550 | 10 | 0.00 |
| 3 | 44,100 | 12 | 2,480.00 | 19,900 | 12 | 1,240.00 | 33,250 | 12 | 1,770.00 |
| 4 | 120,100 | 22 | 11,600.00 | 57,900 | 22 | 5,800.00 | 83,000 | 22 | 7,740.00 |
| 5 | 230,700 | 24 | 35,932.00 | 113,200 | 24 | 17,966.00 | 121,250 | 24 | 16,155.00 |
| 6 | 422,850 | 32 | 82,048.00 | 209,275 | 32 | 41,024.00 | 217,300 | 32 | 39,207.00 |
| 7 | 531,750 | 35 | 116,896.00 | 263,725 | 35 | 58,448.00 | 271,750 | 35 | 56,631.00 |
| 8 | 788,000 | 37 | 206,583.50 | 648,100 | 37 | 192,979.25 | 656,150 | 37 | 191,171.00 |

Source [US-FEDS5-001]; the standard deduction behind the zero bracket is USD 16,100 single, USD 32,200 married filing jointly, USD 24,150 head of household [US-FEDS5-010].

**Step-2-checked schedule (floors and rates; cumulative tax per the formula above).**

| Row | MFJ floor | MFJ rate | Single/MFS floor | Single rate | HoH floor | HoH rate |
|---|---|---|---|---|---|---|
| 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2 | 16,100 | 10 | 8,050 | 10 | 12,075 | 10 |
| 3 | 28,500 | 12 | 14,250 | 12 | 20,925 | 12 |
| 4 | 66,500 | 22 | 33,250 | 22 | 45,800 | 22 |
| 5 | 121,800 | 24 | 60,900 | 24 | 64,925 | 24 |
| 6 | 217,875 | 32 | 108,938 | 32 | 112,950 | 32 |
| 7 | 272,325 | 35 | 136,163 | 35 | 140,175 | 35 |
| 8 | 400,450 | 37 | 328,350 | 37 | 332,375 | 37 |

Source [US-FEDS5-001]. Worked examples: §6.3. Oracle: `fed.oracle.source` [US-FED-027].

## 6.2 Tax Rates and Logic

### What are the latest tax rates by tax type, residential status, and payment frequency?

Federal rates are the annual schedules of §6.1.1, identical for every frequency (applied after annualising). The NRA add-on is published per frequency:

| Pay frequency | Table 2 add-on (USD) | Table 1 add-on (USD) |
|---|---|---|
| weekly | 309.60 | 226.90 |
| biweekly | 619.20 | 453.80 |
| semimonthly | 670.80 | 491.70 |
| monthly | 1,341.70 | 983.30 |
| quarterly | 4,025.00 | 2,950.00 |
| semiannual | 8,050.00 | 5,900.00 |
| annual | 16,100.00 | 11,800.00 |
| daily | 61.90 | 45.40 |

Source [US-FEDS5-002]. Supplemental rates: §6.0. State rates: §6.1 and annexes.

Special pay cycles and supplemental pay (coverage row `special_pay_cycles` [US-FEDS5-003, US-FEDS5-001, US-CAS5-004]): Pub. 15-T supports daily to annual periods (annualise, then divide); supplemental pay is withheld at the flat 22% or by the aggregate method, 37% mandatory above USD 1,000,000; State supplemental rates are annex detail (examples in Module 4 §4.5: California 10.23% bonus / 6.6% other).

**Local layer (examples)**

| Locality | Rate | Fact |
|---|---|---|
| Philadelphia, PA | Resident 3.74% / nonresident 3.43% to 2026-06-30; resident 3.735% / nonresident 3.425% from 2026-07-01 | [US-PAS5-022] |
| Detroit, MI | Resident 2.4% / nonresident 1.2%; annual exemption USD 600 | [US-MIR3-002] |
| Louisville Metro, KY | 1.45% on all wages earned in Louisville Metro; residents 2.2% in total | [US-KYP9W-001] |
| Maryland counties | Collected with the State return; default county rate 3.3% | [US-MDS5-003] |
| Indiana counties | County rates may change in January and October (DN#1 R47/10-26 from 2026-10-01) | [US-INS5-009] |
| Ohio municipalities | Base: Ohio municipal income tax base = Medicare wages less 125 deductions; 401(k) deferrals taxable | [US-OHS5-001] |

Local taxes are outside State reciprocity (annex MULTI notes); W-2 boxes carry up to 2 States and localities per form [US-MULTIS5-011].

### How are rates applied for different frequencies?

Annualise, apply the annual schedule, divide back: line 1c multiplies by the pay periods of the frequency (2 / 4 / 12 / 24 / 26 / 52 / 260 (semiannual, quarterly, monthly, semimonthly, biweekly, weekly, daily)), line 2h divides by the same number [US-FEDS5-001]. The NRA add-on is added per period from the table above. Several States round the per-period result (Module 1 §1.5).

### How does tax applicability and calculation logic differ by residential status?

Federal: §6.0. State: a resident is taxed on all wages; a nonresident on wages for services performed in the State (No general federal rule: each State taxes residents on all wages (credit at assessment for tax paid to the work State) and nonresidents on wages for services performed in the State; federal limits only for transport workers and military spouses. 4 U.S.C. 114 is retirement income only, not wages. [US-MULTIQ1-001]). Each State decides how it withholds for a resident working elsewhere:

| State | Resident working in another State | Fact |
|---|---|---|
| CT | All wages subject; where the employer must withhold for the other jurisdiction, CT tax is prorated and only the excess remitted | [US-CTP10-001] |
| KS | KS tax on total wages less the other State's required withholding (example 250 - 130 = 120); zero if the other State's withholding is higher | [US-KSP51-003] |
| VT | Compute on the full payment, then reduce by tax withheld for the State where services were performed | [US-VTP51-003] |
| MA | MA amount minus the other jurisdiction's amount (credit method, 830 CMR 62B.2.1(9)(b)); employer without MA office may withhold for MA residents as a convenience | [US-MAS5-023] |
| GA | No GA withholding if the other State requires withholding; otherwise withhold GA | [US-GAS5-004] |
| NC | Withhold on all wages wherever earned, except no NC withholding on wages for services in a State that requires the employer to withhold | [US-NCP51-002] |
| CO | Withhold CO on all wages except wages for services in another State that itself requires withholding | [US-COP51-002] |
| IL | IL resident working entirely in another State whose compensation is subject to that State's withholding: no IL withholding (credit on the return) | [US-ILS5-014] |
| NY | Withhold NYS tax for NY residents even if wages are earned outside NY | [US-NY-013] |
| OK | Residents are withheld on services within or without Oklahoma (68 O.S. 2385.1 employee definition) | [US-OKS5-010] |
| OH | Every employer with an office or transacting business in Ohio withholds on residents (resident credit IT RC at assessment) | [US-OHP52-006] |
| LA | LA residents working in another State may be subject to LA withholding if those wages are not subject to withholding there | [US-LAP51-001] |
| WI | Residents working outside WI: withholding on all wages; Minnesota special arrangement - no WI withholding if MN withholds | [US-WIS5-011] |
| MS | Withhold MS on total wages except to the extent withheld for another State; commuter to a no-income-tax State is withheld MS on total wages (credit at assessment). MS is not a credit-only State. | [US-MSS5-004] |
| SC | Withhold for the other State; if that State has no income tax, withhold 100% SC (12-8-520(C)(1)) | [US-SCR3-003] |

The credit for tax paid to another State is never a payroll deduction where it operates at assessment: SC [US-SCR3-004], AR [US-ARS5-006], MS [US-MSS5-019], DC [US-DCP51-007], ME [US-MEP52-004], RI [US-RIP52-002], OH [US-OHP52-004], OK [US-OKP52-002], AZ [US-AZWH-003].

**Nonresident thresholds (work State withholds only above them)**

| State | Threshold | Fact |
|---|---|---|
| SAFE_HARBOR | 30 days | [US-ALS5-003] |
| AZ | 60 days | [US-MULTIB5-401] |
| CT | 15 days | [US-CTP10-001] |
| EXEMPT_DAYS | 60 days | [US-HIP51-002] |
| IL | 30 days | [US-MULTIS5-023] |
| LA | 30 days | [US-MULTIS5-021] |
| ME | 12 days | [US-MEP52-003] |
| NONRESIDENT | 30 days | [US-MTP51-003] |
| NONRESIDENT | 7 days | [US-NEP51-002] |
| NONRESIDENT | 15 days | [US-NMP52-002] |
| UT | 20 days | [US-UTP51-002] |
| VT | 30 days | [US-VTP52-003] |
| WV | 30 days | [US-MULTI-015] |
| THRESHOLD_AMOUNT | USD 5,000 | [US-GAS5-004] |
| ID | USD 1,000 | [US-IDB5-401] |
| MN | USD 15,300 | [US-MNS5-010] |
| NONRESIDENT | USD 300 per quarter | [US-OKS5-010] |
| NONRESIDENT | USD 1,500 | [US-WIS5-011] |
| CA | No threshold: working-day ratio from day 1 (commission pay: volume ratio) | [US-MULTIS5-010] |
| NY | No threshold: NY working days / total working days with the convenience test | [US-MULTIS5-013] |
| CO | No threshold: apportioned by days worked in CO (a day counts if majority of working time is in CO) | [US-COP51-002] |
| AR | No threshold: apportioned by AR working days (HB1116 of 2025, 15 days / 2,500, died) | [US-ARP51-002] |
| MS | Day 1 by earnings ratio, except no withholding when annual MS earnings will be below the standard deduction for the filing status | [US-MSS5-019] |
| ND | Mobile workforce exclusion (57-38-59.3): present 20 days or fewer, no other ND income, home State reciprocal exclusion or no income tax; not athletes, entertainers, persons of prominence, construction workers, key employees | [US-NDS5-004] |
| LA | Begin withholding and report on Form L-1 beginning in the period in which the 31st day fell | [US-LAS5-002] |

Not configured in this release (open gap RQ-411): Act 382 says from day 31 every LA day incl. the first 30 is taxable, but LAC 61:I.1923 only says begin withholding in the period of the 31st day; how days 1-30 are caught up is not stated (LA-OQ-1).

**Reciprocity** (work-State withholding stops on a certificate): partner table in Module 2 §2.2. AZ exempts residents of CA, IN, OR, VA on Form WEC (they can claim the AZ credit); one-way - an AZ resident working in CA is withheld by CA [US-MULTIB5-401]. D.C. Code 1-206.02(a)(5): DC may not tax any nonresident's personal income; DC withholding stops for ANY nonresident (D-4A: domicile outside DC and under 183 days) [US-DCP51-006].

**Convenience-of-the-employer rules**

| State | Rule | Fact |
|---|---|---|
| NY | 20 NYCRR 132.18(a): nonresident allocates by NY working days / total working days; days outside NY count only if worked of NECESSITY; home-office days are NY days unless the home is a bona fide employer office | [US-MULTIS5-013] |
| PA | 61 Pa. Code 109.8: same necessity test as NY; PA reciprocal agreements prevail | [US-MULTIS5-014] |
| DE | 30 Del. C. 1124(b)(1): compensation is DE-source if attributable to employment in DE and not required to be performed elsewhere; working from home does not qualify for the PIT-SCW exclusion | [US-DES5-004] |
| NE | From 2025: services performed outside NE for the nonresident's convenience are NE-sourced (77-2733(8)(c)) | [US-NEP51-002] |
| NJ | From 2023 NJ applies the convenience rule against residents of States that apply one (DE, NE, NY; CT by reciprocal law); PA residents excluded by the reciprocal agreement | [US-MULTI-012] |
| CT | From tax years beginning 2019-01-01 CT applies the resident State's convenience test to nonresidents working for a CT employer | [US-MULTI-020] |
| AR | Not a convenience State: Act 1019 of 2021 (SB 484), in force from TY2021 - a nonresident works in AR only when physically located in AR | [US-ARS5-006] |
| All other States | Everywhere else wages follow the place of physical performance | [US-MULTIQ1-001] |

**Federal limits on State taxation**

| Worker | Rule | Fact |
|---|---|---|
| Motor carrier | Employee with regularly assigned duties in 2+ States: taxable ONLY by the residence State/subdivision (49 U.S.C. 14503) | [US-MULTIS5-001] |
| Rail | Residence State/subdivision only (49 U.S.C. 11502) | [US-MULTIS5-002] |
| Air carrier | Residence State plus the State where more than 50% of carrier pay is earned (scheduled flight time) (49 U.S.C. 40116(f)) | [US-MULTIS5-003] |
| Seamen | Seamen's wages may not be withheld for State/local tax; multi-State vessel crew and pilots taxable only by the residence State (46 U.S.C. 11108) | [US-MULTIS5-004] |
| Military spouse | A military spouse present in a State solely to be with the servicemember under military orders neither loses nor acquires residence or domicile; the spouse's income for services performed in that State is not income for services performed or from sources within that State if the spouse is not a resident of it; for any taxable year the spouse may elect the residence of the servicemember, the spouse's own residence or the permanent duty station (50 U.S.C. 4001(a)(2), (c)). Payroll effect: on the employee's State certificate of nonresidence, stop work-State withholding. | [US-MULTIS5-005] |

### Provide the tax calculation logic covering eligibility, joining month, termination month, mid-month joining, mid-month terminations, and mid-month salary revisions.

Per pay period on the wages paid, with the period's frequency; no proration and no catch-up (coverage row `mid_month_joiner_and_leaver` [US-FEDS5-001, US-FEDS5-024, US-MULTIS5-009]). A salary revision changes the wages of the period in which it is paid. A terminated employee's final pay is withheld with the regular or supplemental method by its nature (Module 9).

Mid-year changes are applied by **payment date** (coverage row `mid_year_rate_change` [US-DCS5-011, US-ORS5-002, US-OHS5-001, US-PAS5-022, US-FEDS5-030]):

| Change | Effective | Fact |
|---|---|---|
| Ohio withholding tables | 2026-08-01 | [US-OHS5-001] |
| Philadelphia wage tax rates | 2026-07-01 | [US-PAS5-022] |
| Indiana county rates | County rates may change in January and October (DN#1 R47/10-26 from 2026-10-01) | [US-INS5-009] |
| Idaho withholding tables (zero bracket single USD 16,100 from 2026-07-23; USD 15,000 before) | 2026-07-23 | [US-IDS5-011] |
| Georgia | 4.99% for taxable years beginning on/after 2026-01-01 (5.19% before); from 2027-01-01 reduced by 0.125 point annually to 3.99%, each step delayed one year if an OPB trigger holds at 1 December | [US-GAS5-009] |

### Do tax rates vary by gender or age?

No. The federal schedules carried in the facts are keyed only by filing status and the W-4 Step 2 box (`fed.fit.standard.*`, `fed.fit.step2.*`); no gender or age dimension exists. States may add age-linked allowances: tips, overtime, car-loan interest conformed at ASSESSMENT only (no withholding allowance); senior deduction (up to 6,000) may be claimed as an IA W-4 allowance [US-IAS5-019].

### What is the minimum tax rate applicable?

0% on the first row of every schedule: no federal income tax is withheld until the adjusted annual wage reaches USD 7,500 (single), USD 19,300 (married filing jointly) or USD 15,550 (head of household); the first positive rate is 10% [US-FEDS5-001].

**Build traps (statute vs withholding instrument, assessment-only items)**

| Jurisdiction | Rule for the engine | Fact |
|---|---|---|
| SC | Withholding tables in force: SCDOR WH-1603 (Rev. 10/30/25) 2026 tables, 0/3/6%; SCDOR Information Letter #26-20 gives the Act 110 2026 schedule 1.99% (0-29,999) / 5.21% minus 966 (30,000+) and says withholding is unchanged until DOR republishes the tables | [US-SCS5-004; US-SCS5-005] |
| WI | Withholding uses W-166 schedule (3.54/4.65/5.30/7.65%), not the assessment brackets (3.50/4.40/5.30/7.65%) | [US-WIS5-010; US-WIS5-011] |
| NE | Withholding uses the DOR Circular EN 2026 percentage-method tables (2.26% to 4.60% rates); the statute (77-2715.03) sets 4.55% for rate three in tax year 2026 | [US-NES5-010; US-NES5-018] |
| KS | KW-100 header prints "wages paid on and after January 1, 2021" but figures are the 2024 values in force for 2026 (5.20/5.58%) | [US-KSS5-001] |
| OH | Ohio withholding follows the tax commissioner's tables under ORC 5747.06, graduated 1.6% / 2.99% / 3.4% from 2026-08-01 (US-OH-006, US-OHS5-001); the ORC 5747.02 statute rate for TY2026 and thereafter is a flat 2.75% over 26,050 (US-OHS5-007) - use the tables for withholding | [US-OHS5-007; US-OHS5-008; US-OH-006; US-OHS5-001] |
| MI | MI 2025 PA 24 tips/overtime deduction (TY2026-2028) is ASSESSMENT only; no change to withholding | [US-MIS5-017] |
| VA | Statute: 2027 standard deduction 9,200/18,400; do not model 2027 withholding until Virginia Tax publishes the 2027 formula (guide Rev. 10/26 says the deduction sunsets - wrong) | [US-VAS5-018] |
| CT | DRS: 'Use either the withholding calculation rules or the withholding tables' (TPG-211); the two methods can give different amounts; configured: DRS per-period tables up to each table maximum, TPG-211 rules above (CT.2, configuration decision of 2026-11-02) | [US-CTS5-010; US-CTWH-001] |
| HI | Act 24 SLH 2026 changes TY2027 brackets (new 13% top); 2027 withholding indeterminate until DOTAX issues 2027 Booklet A | [US-HIS5-029] |
| AL | AL state base deducts federal withholding: order FIT before AL SIT | [US-ALS5-001] |
| OR | Use 8,750 federal-tax subtraction cap (pp.6-7 formula); DOR publication also prints 8,500 and its example 1 is mis-computed | [US-ORS5-009] |
| FED | Do not reduce FIT withholding for tips/overtime deductions except through W-4 Step 4(b) | [US-FEDS5-030] |
| FED | IRS Tax Withholding Estimator is not an employer engine or oracle | [US-FED-021] |
| DC | D.C. Act 26-416 (emergency, from 2026-08-13) revoked personal exemptions; no 2026 withholding method published (D-4 under review) | [US-DCS5-021] |
| OH (statute) | TY2026 flat 2.75% above 26,050 (ORC 5747.02 as amended by HB 96); withholding tables still graduated to 3.4% - two instruments | [US-OHS5-007] |
| AL, GA, IA, DC (tips / overtime) | Assessment only, no withholding change: Module 4 §4.4 | [US-ALS5-004]; [US-GAS5-009]; [US-IAS5-019]; [US-DCS5-021] |
| HI (tips / overtime) | Not configured in this release (open gap RQ-563): Level not established from an official source. | |
| ND | Method: annual percentage method on federal W-4 (tables route under 57-38-59(3)); the booklet's worked example is a recorded defect, use the method/table (`nd.oracle.section2_booklet.withholding` [US-NDS5-001]) | [US-NDS5-001] |

Not configured in this release (open gap RQ-543): DC has no published 2026 withholding method: D.C. Act 26-416 (emergency, effective 2026-08-13, max 90 days) revoked personal exemptions; D-4 under review (US-DCS5-021).

Not configured in this release (open gap RQ-542): Utah: the effective date of Pub 14 (Rev. 04/26) is not established, so its examples are not dated results.

## 6.3 Adjustments and Special Cases

### For annualized tax systems, which salary components must be projected?

None beyond the current period. Worksheet 1A annualises the current period's wages by multiplying by the pay periods; it does not project other components or year-to-date earnings. Supplemental pay withheld at the flat rate is not annualised [US-FEDS5-003].

### Are year-end tax adjustments required?

No employer year-end income-tax adjustment: the employee reconciles at assessment (coverage row `annual_regularisation` [US-FEDS5-007, US-FEDS5-005, US-FEDS5-006]). The exempt status is renewed yearly (2026 only: the exemption checkbox certification lapses; a new W-4 is required for 2027). 2027 parameters: Not configured in this release (open gap RQ-530): TY2027 Rev. Proc., 401(k)/IRA notice and 2027 Pub. 15-T not published as of 2026-11-02 (IR-2026-117..129 checked).

### Are there minimum or higher tax requirements if employees fail to submit a tax ID or social security number?

| Situation | Federal rule | Source |
|---|---|---|
| New employee gives no Form W-4 in 2026 | Withhold as if the employee had entered: Single or Married filing separately in Step 1(c), no entries in Step 2, Step 3 or Step 4 of the 2026 Form W-4 | [US-FEDQ3-004] |
| Employee paid before 2020 with no Form W-4 on file | Employee paid wages before 2020 who never furnished a Form W-4: single with zero allowances on a 2019 Form W-4 | [US-FEDQ3-004] |
| Exempt status not renewed | Exempt Form W-4 not renewed by February 15: withhold as Single or Married filing separately in Step 1(c) with no entries in Steps 2-4; a later exempt Form W-4 applies to future wages only, without refund | [US-FEDQ3-004] |
| No SSN yet | Employee applied for an SSN but has none when Form W-2 is due: enter 'Applied For' on a paper W-2, all zeros in an electronic file; when the SSN is received file Form W-2c (Copy A) with SSA and furnish copies to the employee | [US-FEDQ3-004] |

State defaults for a missing State certificate are in Module 2 (for example `ct.cert.default_no_certificate` [US-CTS5-011]: flat withholding; `ca.cert.default_no_certificate` [US-CAS5-004]).

### What is the income tax and social security refund procedure?

Employee side: income tax and excess OASDI from several employers are refunded at assessment (coverage row `multiple_employers` [US-FEDS5-006, US-MULTIS5-009, US-FEDS5-005]). Employer side: corrections run through the federal correction returns.

Not configured in this release (open gap RQ-569): The employer procedure to repay or reimburse over-withheld income tax or over-collected FICA in the same year and after year-end (26 CFR 31.6413, Forms 941-X / W-2c) is not established from an official source.

### Deliverable: Provide detailed worked examples for a standard resident employee, a non-resident employee, and an irregular payment.

Computed by the computation from the facts; each amount rounded half-up to the cent (Module 1 §1.5); full precision carried between lines.

**Example 1: standard resident employee.** Resident employee, Form W-4 (2026): Single, Step 2 not checked, no Step 3 or Step 4 entries; weekly wages USD 1,640.00; no pre-tax deductions; year-to-date wages below every cap.

| Line | Calculation | Result |
|---|---|---|
| 1c. Annualised wages | 1,640.00 × 52 | 85,280.00 |
| 1i. Adjusted annual wage (line 1g subtracted, Step 2 not checked) | 85,280.00 − 8,600 | 76,680.00 |
| 2e. Excess over the bracket floor (STANDARD SINGLE row 4) | 76,680.00 − 57,900 | 18,780.00 |
| 2f. Excess × bracket rate | 18,780.00 × 22% | 4,131.60 |
| 2g. Tentative annual withholding | 5,800 + 4,131.60 | 9,931.60 |
| 2h. Withholding for the period | 9,931.60 ÷ 52 | 190.99 |

| Line | Base | Rate | Amount |
|---|---|---|---|
| OASDI employee | 1,640.00 | 6.2% | 101.68 |
| Medicare employee | 1,640.00 | 1.45% | 23.78 |

| Line | Calculation | Result |
|---|---|---|
| Net pay | 1,640.00 − 190.99 − 101.68 − 23.78 | 1,323.55 |

**Example 2: nonresident alien employee.** Nonresident alien employee, Form W-4 (2026) completed per Notice 1392 (Single, NRA, Step 2 not checked); weekly wages USD 1,640.00; first paid in 2026 (Table 2 add-on); no treaty exemption.

| Line | Calculation | Result |
|---|---|---|
| 1a. Wages for the computation, including the NRA add-on (Table 2, weekly) | 1,640.00 + 309.60 | 1,949.60 |
| 1c. Annualised wages | 1,949.60 × 52 | 101,379.20 |
| 1i. Adjusted annual wage (line 1g subtracted, Step 2 not checked) | 101,379.20 − 8,600 | 92,779.20 |
| 2e. Excess over the bracket floor (STANDARD SINGLE row 4) | 92,779.20 − 57,900 | 34,879.20 |
| 2f. Excess × bracket rate | 34,879.20 × 22% | 7,673.42 |
| 2g. Tentative annual withholding | 5,800 + 7,673.42 | 13,473.42 |
| 2h. Withholding for the period | 13,473.42 ÷ 52 | 259.10 |

| Line | Base | Rate | Amount |
|---|---|---|---|
| OASDI employee | 1,640.00 | 6.2% | 101.68 |
| Medicare employee | 1,640.00 | 1.45% | 23.78 |

| Line | Calculation | Result |
|---|---|---|
| Net pay (the add-on is not paid and not reported) | 1,640.00 − 259.10 − 101.68 − 23.78 | 1,255.44 |

**Example 3: irregular payment (bonus).** Irregular payment: annual bonus USD 12,400.00 paid separately from regular wages to a resident employee whose 2026 supplemental wages stay below the mandatory-rate threshold and whose year-to-date wages are below the OASDI base and the Additional Medicare threshold; the employer uses the optional flat rate.

| Line | Base | Rate | Amount |
|---|---|---|---|
| Federal income tax (flat supplemental rate) | 12,400.00 | 22% | 2,728.00 |
| OASDI employee | 12,400.00 | 6.2% | 768.80 |
| Medicare employee | 12,400.00 | 1.45% | 179.80 |

| Line | Calculation | Result |
|---|---|---|
| Net bonus | 12,400.00 − 2,728.00 − 768.80 − 179.80 | 8,723.40 |

State and local withholding for these employees depends on the work and residence State (annex worked examples, Module 12).


## Fact index

Every value above with its key, effective period and register id.

| Key | Value | Effective | Register id |
|---|---|---|---|
| `al.nonres.safe_harbor.days` | 30 | from 2026-01-01 | US-ALS5-003 |
| `ca.wh.supplemental.rate.bonus_stock_options` | 10.23 | from 2026-01-01 | US-CAS5-004 |
| `ca.wh.supplemental.rate.other` | 6.6 | from 2026-01-01 | US-CAS5-004 |
| `fed.bik.group_term_life.excluded_coverage` | 50,000 | from 2026-01-01 | US-FEDS5-008 |
| `fed.equity.83i.withholding_rate` | 37 | from 2026-01-01 | US-FEDQ1-001 |
| `fed.equity.rsu.fica_timing` | Later of the performance of the services and the date the right is no longer subject to a substantial risk of forfeiture (vesting); FUTA follows the same rule | from 2026-01-01 | US-FEDQ1-004 |
| `fed.equity.withholding_treatment.nonresident` | Nonresident alien employee, 2026: equity income is wages subject to graduated withholding as for residents, with the Pub. 15-T NRA add-on, except that no add-on applies when the payment is withheld at the 22% optional or 37% mandatory flat supplemental rate. Only the U.S.-source part is wages for U.S. withholding: compensation attributable to several years is sourced on a time basis (U.S. workdays / total workdays over the period to which it is attributable, facts and circumstances). FICA/FUTA follow the resident rules (NSO spread and RSU at vesting are FICA wages) unless the employee is exempt as an F-1/J-1/M-1/Q nonimmigrant. Reporting on Form W-2; Form 1042-S only for wages exempt under a treaty claimed on Form 8233. | from 2026-01-01 | US-FEDQ1-006 |
| `fed.equity.withholding_treatment.resident` | Resident employee, 2026: (1) Nonstatutory option (NSO): the spread at exercise (FMV - price) is wages - a taxable fringe benefit subject to the supplemental-wage rules (22% optional flat or aggregate; 37% on supplemental wages above 1,000,000), FICA and FUTA wages, timed at the actual exercise (transfer) date; W-2 boxes 1, 3 (to the SS base), 5 and box 12 code V. (2) ISO and ESPP options: no FICA or FUTA at grant, exercise or disposition; no FIT withholding required on a disqualifying disposition or on the ESPP discount at a qualifying disposition, but the ordinary income is W-2 box 1 wages. (3) Restricted stock (actual shares subject to forfeiture): FMV minus amount paid is wages when substantially vested (or at transfer with an 83(b) election). (4) RSU (legally binding right to receive shares in a future year): FICA and FUTA wages at the later of service performance and vesting (special timing rule, 26 CFR 31.3121(v)(2)-1 / 31.3306(r)(2)-1); FIT withholding when the shares are delivered (settlement) as supplemental wages. (5) 83(i) election (private company): FIT deferred up to 5 years and withheld at 37% when included; FICA/FUTA not deferred; W-2 codes GG/HH. | from 2026-01-01 | US-FEDQ1-001 |
| `fed.fica.medicare.rate.employee` | 1.45 | from 2026-01-01 to 2026-12-31 | US-FEDS5-005 |
| `fed.fica.nra.fjmq_exempt.scope` | Exempt: pay of a nonresident alien in F-1, J-1, M-1 or Q status for services that carry out the purpose of admission, on or off campus, including authorized Curricular and Optional Practical Training. Not exempt: other employment of the same person (e.g. an unrelated part-time job), and any pay once the person is a resident alien. | from 2026-01-01 | US-FEDS5-016 |
| `fed.fica.oasdi.rate.employee` | 6.2 | from 2026-01-01 to 2026-12-31 | US-FEDS5-005 |
| `fed.fica.totalization.exemption_rule` | Wages are exempt from employee FICA (IRC 3101(c)) and employer FICA (IRC 3111(c)) while a section 233 Social Security Act agreement is in effect, to the extent the agreement makes them subject exclusively to the foreign social security system. | from 2026-01-01 | US-FEDR2-003 |
| `fed.fit.allowance.pre2020_value` | 4,300 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.backup_withholding.rate` | 24 | from 2026-01-01 | US-FEDS5-003 |
| `fed.fit.legal_basis.withholding_statute` | 26 U.S.C. 3402: employer withholds federal income tax per tables/procedures prescribed by the Secretary (federal tax only) | from 2026-01-01 | US-FED-012 |
| `fed.fit.method` | IRS Pub. 15-T (2026) Worksheet 1A with the Annual Percentage Method tables (STANDARD schedule; Step-2-checked schedule when W-4 Step 2 box checked) | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.nra.addon.table1.annual` | 11,800 | from 2026-01-01 to 2026-12-31 | US-FEDS5-002 |
| `fed.fit.nra.addon.table1.annual` | 11,800.00 | from 2026-01-01 to 2026-12-31 | US-FEDS5-002 |
| `fed.fit.nra.addon.table1.biweekly` | 453.80 | from 2026-01-01 to 2026-12-31 | US-FEDS5-002 |
| `fed.fit.nra.addon.table1.daily` | 45.40 | from 2026-01-01 to 2026-12-31 | US-FEDS5-002 |
| `fed.fit.nra.addon.table1.monthly` | 983.30 | from 2026-01-01 to 2026-12-31 | US-FEDS5-002 |
| `fed.fit.nra.addon.table1.quarterly` | 2,950.00 | from 2026-01-01 to 2026-12-31 | US-FEDS5-002 |
| `fed.fit.nra.addon.table1.semiannual` | 5,900.00 | from 2026-01-01 to 2026-12-31 | US-FEDS5-002 |
| `fed.fit.nra.addon.table1.semimonthly` | 491.70 | from 2026-01-01 to 2026-12-31 | US-FEDS5-002 |
| `fed.fit.nra.addon.table1.weekly` | 226.90 | from 2026-01-01 to 2026-12-31 | US-FEDS5-002 |
| `fed.fit.nra.addon.table2.annual` | 16,100 | from 2026-01-01 to 2026-12-31 | US-FEDS5-002 |
| `fed.fit.nra.addon.table2.annual` | 16,100.00 | from 2026-01-01 to 2026-12-31 | US-FEDS5-002 |
| `fed.fit.nra.addon.table2.biweekly` | 619.20 | from 2026-01-01 to 2026-12-31 | US-FEDS5-002 |
| `fed.fit.nra.addon.table2.daily` | 61.90 | from 2026-01-01 to 2026-12-31 | US-FEDS5-002 |
| `fed.fit.nra.addon.table2.monthly` | 1,341.70 | from 2026-01-01 to 2026-12-31 | US-FEDS5-002 |
| `fed.fit.nra.addon.table2.quarterly` | 4,025.00 | from 2026-01-01 to 2026-12-31 | US-FEDS5-002 |
| `fed.fit.nra.addon.table2.semiannual` | 8,050.00 | from 2026-01-01 to 2026-12-31 | US-FEDS5-002 |
| `fed.fit.nra.addon.table2.semimonthly` | 670.80 | from 2026-01-01 to 2026-12-31 | US-FEDS5-002 |
| `fed.fit.nra.addon.table2.weekly` | 309.60 | from 2026-01-01 to 2026-12-31 | US-FEDS5-002 |
| `fed.fit.nra.bik.treatment` | Nonresident alien employee, 2026: taxable fringe benefits are wages subject to graduated FIT withholding. Added to regular wages for the payroll period, they are withheld with the Pub. 15-T NRA add-on; withheld separately at the 22% optional flat supplemental rate (37% above 1,000,000), no add-on applies. Noncash fringes may be treated as paid per pay period, quarter, half-year or year (at least annually). FICA and FUTA apply as for residents unless the employee is an F-1/J-1/M-1/Q nonimmigrant. Group-term life cost over 50,000: FICA wages, no FIT withholding and no FUTA required, W-2 boxes 1, 3, 5 and box 12 code C. Only U.S.-source fringes are wages for withholding: housing, education, local transportation (main job location), tax reimbursement (taxing jurisdiction), hazardous duty and moving (new main job location) are sourced geographically, other fringes on a time basis. Reported on Form W-2 (Form 1042-S only for treaty-exempt wages on Form 8233). | from 2026-01-01 | US-FEDQ1-008 |
| `fed.fit.nra.commercial_traveler.max_days` | 90 | from 2026-01-01 | US-FEDS5-016 |
| `fed.fit.nra.commercial_traveler.max_pay` | 3,000 | from 2026-01-01 | US-FEDS5-016 |
| `fed.fit.nra.treaty_exempt.reporting` | Treaty-exempt wages claimed on Form 8233 are reported on Form 1042-S (not W-2 box 1); 2026 Forms 1042-S due 2027-03-15 and must be e-filed via IRIS | from 2026-01-01 | US-FEDS5-016 |
| `fed.fit.nra.w4.rule` | Check Single or MFS regardless of marital status; write NRA below Step 4(c); exempt not allowed; Step 3 only for residents of Canada, Mexico, South Korea or India (students/apprentices) | from 2020-01-01 | US-FEDS5-015 |
| `fed.fit.pay_periods_per_year` | 2 / 4 / 12 / 24 / 26 / 52 / 260 (semiannual, quarterly, monthly, semimonthly, biweekly, weekly, daily) | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.hoh.bracket.1.cumulative_tax` | 0.00 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.hoh.bracket.1.floor` | 0 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.hoh.bracket.1.rate` | 0 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.hoh.bracket.2.cumulative_tax` | 0.00 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.hoh.bracket.2.floor` | 15,550 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.hoh.bracket.2.rate` | 10 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.hoh.bracket.3.cumulative_tax` | 1,770.00 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.hoh.bracket.3.floor` | 33,250 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.hoh.bracket.3.rate` | 12 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.hoh.bracket.4.cumulative_tax` | 7,740.00 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.hoh.bracket.4.floor` | 83,000 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.hoh.bracket.4.rate` | 22 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.hoh.bracket.5.cumulative_tax` | 16,155.00 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.hoh.bracket.5.floor` | 121,250 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.hoh.bracket.5.rate` | 24 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.hoh.bracket.6.cumulative_tax` | 39,207.00 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.hoh.bracket.6.floor` | 217,300 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.hoh.bracket.6.rate` | 32 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.hoh.bracket.7.cumulative_tax` | 56,631.00 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.hoh.bracket.7.floor` | 271,750 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.hoh.bracket.7.rate` | 35 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.hoh.bracket.8.cumulative_tax` | 191,171.00 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.hoh.bracket.8.floor` | 656,150 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.hoh.bracket.8.rate` | 37 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.mfj.bracket.1.cumulative_tax` | 0.00 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.mfj.bracket.1.floor` | 0 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.mfj.bracket.1.rate` | 0 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.mfj.bracket.2.cumulative_tax` | 0.00 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.mfj.bracket.2.floor` | 19,300 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.mfj.bracket.2.rate` | 10 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.mfj.bracket.3.cumulative_tax` | 2,480.00 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.mfj.bracket.3.floor` | 44,100 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.mfj.bracket.3.rate` | 12 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.mfj.bracket.4.cumulative_tax` | 11,600.00 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.mfj.bracket.4.floor` | 120,100 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.mfj.bracket.4.rate` | 22 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.mfj.bracket.5.cumulative_tax` | 35,932.00 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.mfj.bracket.5.floor` | 230,700 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.mfj.bracket.5.rate` | 24 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.mfj.bracket.6.cumulative_tax` | 82,048.00 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.mfj.bracket.6.floor` | 422,850 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.mfj.bracket.6.rate` | 32 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.mfj.bracket.7.cumulative_tax` | 116,896.00 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.mfj.bracket.7.floor` | 531,750 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.mfj.bracket.7.rate` | 35 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.mfj.bracket.8.cumulative_tax` | 206,583.50 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.mfj.bracket.8.floor` | 788,000 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.mfj.bracket.8.rate` | 37 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.single.bracket.1.cumulative_tax` | 0.00 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.single.bracket.1.floor` | 0 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.single.bracket.1.rate` | 0 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.single.bracket.2.cumulative_tax` | 0.00 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.single.bracket.2.floor` | 7,500 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.single.bracket.2.rate` | 10 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.single.bracket.3.cumulative_tax` | 1,240.00 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.single.bracket.3.floor` | 19,900 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.single.bracket.3.rate` | 12 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.single.bracket.4.cumulative_tax` | 5,800 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.single.bracket.4.cumulative_tax` | 5,800.00 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.single.bracket.4.floor` | 57,900 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.single.bracket.4.rate` | 22 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.single.bracket.5.cumulative_tax` | 17,966.00 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.single.bracket.5.floor` | 113,200 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.single.bracket.5.rate` | 24 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.single.bracket.6.cumulative_tax` | 41,024.00 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.single.bracket.6.floor` | 209,275 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.single.bracket.6.rate` | 32 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.single.bracket.7.cumulative_tax` | 58,448.00 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.single.bracket.7.floor` | 263,725 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.single.bracket.7.rate` | 35 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.single.bracket.8.cumulative_tax` | 192,979.25 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.single.bracket.8.floor` | 648,100 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.standard.single.bracket.8.rate` | 37 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.std_deduction.hoh` | 24,150 | from 2026-01-01 to 2026-12-31 | US-FEDS5-010 |
| `fed.fit.std_deduction.mfj` | 32,200 | from 2026-01-01 to 2026-12-31 | US-FEDS5-010 |
| `fed.fit.std_deduction.single` | 16,100 | from 2026-01-01 to 2026-12-31 | US-FEDS5-010 |
| `fed.fit.step2.hoh.bracket.1.floor` | 0 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.hoh.bracket.1.rate` | 0 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.hoh.bracket.2.floor` | 12,075 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.hoh.bracket.2.rate` | 10 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.hoh.bracket.3.floor` | 20,925 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.hoh.bracket.3.rate` | 12 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.hoh.bracket.4.floor` | 45,800 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.hoh.bracket.4.rate` | 22 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.hoh.bracket.5.floor` | 64,925 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.hoh.bracket.5.rate` | 24 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.hoh.bracket.6.floor` | 112,950 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.hoh.bracket.6.rate` | 32 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.hoh.bracket.7.floor` | 140,175 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.hoh.bracket.7.rate` | 35 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.hoh.bracket.8.floor` | 332,375 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.hoh.bracket.8.rate` | 37 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.mfj.bracket.1.floor` | 0 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.mfj.bracket.1.rate` | 0 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.mfj.bracket.2.floor` | 16,100 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.mfj.bracket.2.rate` | 10 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.mfj.bracket.3.floor` | 28,500 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.mfj.bracket.3.rate` | 12 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.mfj.bracket.4.floor` | 66,500 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.mfj.bracket.4.rate` | 22 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.mfj.bracket.5.floor` | 121,800 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.mfj.bracket.5.rate` | 24 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.mfj.bracket.6.floor` | 217,875 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.mfj.bracket.6.rate` | 32 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.mfj.bracket.7.floor` | 272,325 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.mfj.bracket.7.rate` | 35 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.mfj.bracket.8.floor` | 400,450 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.mfj.bracket.8.rate` | 37 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.single.bracket.1.floor` | 0 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.single.bracket.1.rate` | 0 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.single.bracket.2.floor` | 8,050 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.single.bracket.2.rate` | 10 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.single.bracket.3.floor` | 14,250 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.single.bracket.3.rate` | 12 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.single.bracket.4.floor` | 33,250 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.single.bracket.4.rate` | 22 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.single.bracket.5.floor` | 60,900 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.single.bracket.5.rate` | 24 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.single.bracket.6.floor` | 108,938 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.single.bracket.6.rate` | 32 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.single.bracket.7.floor` | 136,163 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.single.bracket.7.rate` | 35 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.single.bracket.8.floor` | 328,350 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.step2.single.bracket.8.rate` | 37 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.supplemental.flat_rate` | 22 | from 2026-01-01 | US-FEDS5-003 |
| `fed.fit.supplemental.mandatory_rate` | 37 | from 2026-01-01 | US-FEDS5-003 |
| `fed.fit.supplemental.mandatory_threshold` | 1,000,000 | from 2026-01-01 | US-FEDS5-003 |
| `fed.fit.wage_definition` | Wages for income-tax withholding (IRC 3401(a)): all remuneration (other than fees paid to a public official) for services performed by an employee for his employer, including the cash value of all remuneration (including benefits) paid in any medium other than cash, except the exclusions in 3401(a)(1)-(23). Amounts includible in gross income under section 409A are wages. | from 2026-01-01 | US-FEDQ3-001 |
| `fed.fit.wage_definition.exclusions` | Exclusions relevant to private-sector employees: (a)(2) agricultural labor unless FICA wages; (a)(3) domestic service in a private home; (a)(4) non-business service under 50 a quarter; (a)(8) certain pay abroad / in possessions; (a)(12) payments to or from qualified plans (401(a) trust incl. 401(k) deferrals, 403(a), SEP 402(h), SIMPLE 408(p), governmental 457(b)); (a)(14) group-term life insurance; (a)(15) moving-expense reimbursements deductible under 217; (a)(16) non-cash tips and cash tips under 20 a month; (a)(18) 127 educational assistance, 129 dependent care, 134(b)(4)-(5); (a)(19) 74(c), 108(f)(4), 117 and 132 benefits; (a)(20) self-insured medical reimbursements; (a)(21) 106(b) Archer MSA; (a)(22) 106(d) HSA. | from 2026-01-01 | US-FEDQ3-001 |
| `fed.fit.worksheet1a.line1g.mfj` | 12,900 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.worksheet1a.line1g.other` | 8,600 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.ssn.not_issued.w2_rule` | Employee applied for an SSN but has none when Form W-2 is due: enter 'Applied For' on a paper W-2, all zeros in an electronic file; when the SSN is received file Form W-2c (Copy A) with SSA and furnish copies to the employee | from 2026-01-01 | US-FEDQ3-004 |
| `fed.w4.default_no_certificate` | Single or Married filing separately in Step 1(c), no entries in Step 2, Step 3 or Step 4 of the 2026 Form W-4 | from 2026-01-01 to 2026-12-31 | US-FEDQ3-004 |
| `fed.w4.default_no_certificate.pre2020_employee` | Employee paid wages before 2020 who never furnished a Form W-4: single with zero allowances on a 2019 Form W-4 | from 2026-01-01 to 2026-12-31 | US-FEDQ3-004 |
| `fed.w4.exempt.validity` | 2026 only: the exemption checkbox certification lapses; a new W-4 is required for 2027 | from 2026-01-01 to 2026-12-31 | US-FEDS5-006 |
| `fed.w4.exempt_not_renewed.default` | Exempt Form W-4 not renewed by February 15: withhold as Single or Married filing separately in Step 1(c) with no entries in Steps 2-4; a later exempt Form W-4 applies to future wages only, without refund | from 2026-01-01 to 2026-12-31 | US-FEDQ3-004 |
| `ga.nonres.threshold_amount` | 5,000 | from 2026-01-01 | US-GAS5-004 |
| `ga.pit.rate.flat` | 4.99 | from 2026-01-01 | US-GAS5-009 |
| `ga.wh.rate` | 4.99 | from 2026-05-11 | US-GAS5-009 |
| `ga.wh.rate` | 5.19 | from 2026-01-01 to 2026-05-10 | US-GA-001 |
| `hi.nonres.exempt_days` | 60 | from 2026-01-01 | US-HIP51-002 |
| `ia.pit.obbba` | tips, overtime, car-loan interest conformed at ASSESSMENT only (no withholding allowance); senior deduction (up to 6,000) may be claimed as an IA W-4 allowance | from 2026-01-01 | US-IAS5-019 |
| `id.wh.zero_bracket.single.annual` | 15,000 | from 2025-04-28 to 2026-07-22 | US-IDS5-012 |
| `id.wh.zero_bracket.single.annual` | 16,100 | from 2026-07-23 | US-IDS5-011 |
| `in.county.change_dates` | County rates may change in January and October (DN#1 R47/10-26 from 2026-10-01) | from 2026-01-01 | US-INS5-009 |
| `in.pit.rate` | 2.9 | from 2027-01-01 | US-INS5-009 |
| `in.pit.rate` | 2.95 | from 2026-01-01 to 2026-12-31 | US-INS5-009 |
| `ky.local.louisville.rate.all_wages` | 1.45 | from 2026-01-01 | US-KYP9W-001 |
| `ky.local.louisville.rate.resident_total` | 2.2 | from 2026-01-01 | US-KYP9W-001 |
| `md.local.county_rate.default_unknown` | 3.3 | from 2026-01-01 to 2026-12-31 | US-MDS5-003 |
| `md.pit.top_rate` | 6.5 | from 2025-01-01 | US-MDS5-001 |
| `mi.local.detroit.exemption.annual` | 600 | from 2026-01-01 | US-MIR3-002 |
| `mi.local.detroit.rate.nonresident` | 1.2 | from 2026-01-01 | US-MIR3-002 |
| `mi.local.detroit.rate.resident` | 2.4 | from 2026-01-01 | US-MIR3-002 |
| `mi.pit.rate.flat` | 4.25 | from 2026-01-01 | US-MIPIT-001 |
| `mt.pit.nonresident.days_exemption` | 30 | from 2026-01-01 | US-MTP51-003 |
| `multi.convenience.ar.rule` | Not a convenience State: Act 1019 of 2021 (SB 484), in force from TY2021 - a nonresident works in AR only when physically located in AR | from 2021-01-01 | US-ARS5-006 |
| `multi.convenience.ct.rule` | From tax years beginning 2019-01-01 CT applies the resident State's convenience test to nonresidents working for a CT employer | from 2019-01-01 | US-MULTI-020 |
| `multi.convenience.de.rule` | 30 Del. C. 1124(b)(1): compensation is DE-source if attributable to employment in DE and not required to be performed elsewhere; working from home does not qualify for the PIT-SCW exclusion | from 2026-01-01 | US-DES5-004 |
| `multi.convenience.default` | Everywhere else wages follow the place of physical performance | from 2026-01-01 | US-MULTIQ1-001 |
| `multi.convenience.ne.rule` | From 2025: services performed outside NE for the nonresident's convenience are NE-sourced (77-2733(8)(c)) | from 2025-01-01 | US-NEP51-002 |
| `multi.convenience.nj.rule` | From 2023 NJ applies the convenience rule against residents of States that apply one (DE, NE, NY; CT by reciprocal law); PA residents excluded by the reciprocal agreement | from 2023-01-01 | US-MULTI-012 |
| `multi.convenience.ny.rule` | 20 NYCRR 132.18(a): nonresident allocates by NY working days / total working days; days outside NY count only if worked of NECESSITY; home-office days are NY days unless the home is a bona fide employer office | from 2006-05-15 | US-MULTIS5-013 |
| `multi.convenience.pa.rule` | 61 Pa. Code 109.8: same necessity test as NY; PA reciprocal agreements prevail | from 1999-12-11 | US-MULTIS5-014 |
| `multi.military_spouse.rule` | A military spouse present in a State solely to be with the servicemember under military orders neither loses nor acquires residence or domicile; the spouse's income for services performed in that State is not income for services performed or from sources within that State if the spouse is not a resident of it; for any taxable year the spouse may elect the residence of the servicemember, the spouse's own residence or the permanent duty station (50 U.S.C. 4001(a)(2), (c)). Payroll effect: on the employee's State certificate of nonresidence, stop work-State withholding. | from 2018-12-31 | US-MULTIS5-005 |
| `multi.nonresident.ar.allocation_rule` | No threshold: apportioned by AR working days (HB1116 of 2025, 15 days / 2,500, died) | from 2026-01-01 | US-ARP51-002 |
| `multi.nonresident.az.threshold_days` | 60 | from 2026-01-01 | US-MULTIB5-401 |
| `multi.nonresident.ca.allocation_rule` | No threshold: working-day ratio from day 1 (commission pay: volume ratio) | from 2026-01-01 | US-MULTIS5-010 |
| `multi.nonresident.co.allocation_rule` | No threshold: apportioned by days worked in CO (a day counts if majority of working time is in CO) | from 2026-01-01 | US-COP51-002 |
| `multi.nonresident.ct.threshold_days` | 15 | from 2026-01-01 | US-CTP10-001 |
| `multi.nonresident.id.threshold_amount` | 1,000 | from 2026-04-12 | US-IDB5-401 |
| `multi.nonresident.il.threshold_days` | 30 | from 2026-01-01 | US-MULTIS5-023 |
| `multi.nonresident.la.employer_start_rule` | Begin withholding and report on Form L-1 beginning in the period in which the 31st day fell | from 2026-03-20 | US-LAS5-002 |
| `multi.nonresident.la.threshold_days` | 30 | from 2026-01-01 | US-MULTIS5-021 |
| `multi.nonresident.me.threshold_days` | 12 | from 2026-01-01 | US-MEP52-003 |
| `multi.nonresident.mn.threshold_amount` | 15,300 | from 2026-01-01 to 2026-12-31 | US-MNS5-010 |
| `multi.nonresident.ms.threshold_rule` | Day 1 by earnings ratio, except no withholding when annual MS earnings will be below the standard deduction for the filing status | from 2026-01-01 | US-MSS5-019 |
| `multi.nonresident.nd.threshold_rule` | Mobile workforce exclusion (57-38-59.3): present 20 days or fewer, no other ND income, home State reciprocal exclusion or no income tax; not athletes, entertainers, persons of prominence, construction workers, key employees | from 2026-01-01 | US-NDS5-004 |
| `multi.nonresident.ny.allocation_rule` | No threshold: NY working days / total working days with the convenience test | from 2006-05-15 | US-MULTIS5-013 |
| `multi.nonresident.ut.threshold_days` | 20 | from 2026-01-01 | US-UTP51-002 |
| `multi.nonresident.vt.threshold_days` | 30 | from 2026-01-01 | US-VTP52-003 |
| `multi.nonresident.wv.threshold_days` | 30 | from 2026-01-01 | US-MULTI-015 |
| `multi.pit.sourcing.general` | No general federal rule: each State taxes residents on all wages (credit at assessment for tax paid to the work State) and nonresidents on wages for services performed in the State; federal limits only for transport workers and military spouses. 4 U.S.C. 114 is retirement income only, not wages. | from 2026-01-01 | US-MULTIQ1-001 |
| `multi.reciprocity.az.unilateral` | AZ exempts residents of CA, IN, OR, VA on Form WEC (they can claim the AZ credit); one-way - an AZ resident working in CA is withheld by CA | from 2026-01-01 | US-MULTIB5-401 |
| `multi.reciprocity.dc.nonresident_exempt` | D.C. Code 1-206.02(a)(5): DC may not tax any nonresident's personal income; DC withholding stops for ANY nonresident (D-4A: domicile outside DC and under 183 days) | from 2026-01-01 | US-DCP51-006 |
| `multi.resident_out_of_state.co.withholding_rule` | Withhold CO on all wages except wages for services in another State that itself requires withholding | from 2026-01-01 | US-COP51-002 |
| `multi.resident_out_of_state.ct.withholding_rule` | All wages subject; where the employer must withhold for the other jurisdiction, CT tax is prorated and only the excess remitted | from 2026-01-01 | US-CTP10-001 |
| `multi.resident_out_of_state.ga.withholding_rule` | No GA withholding if the other State requires withholding; otherwise withhold GA | from 2026-01-01 | US-GAS5-004 |
| `multi.resident_out_of_state.il.withholding_rule` | IL resident working entirely in another State whose compensation is subject to that State's withholding: no IL withholding (credit on the return) | from 2026-02-01 | US-ILS5-014 |
| `multi.resident_out_of_state.ks.withholding_rule` | KS tax on total wages less the other State's required withholding (example 250 - 130 = 120); zero if the other State's withholding is higher | from 2024-07-01 | US-KSP51-003 |
| `multi.resident_out_of_state.la.withholding_rule` | LA residents working in another State may be subject to LA withholding if those wages are not subject to withholding there | from 2026-01-01 | US-LAP51-001 |
| `multi.resident_out_of_state.ma.withholding_rule` | MA amount minus the other jurisdiction's amount (credit method, 830 CMR 62B.2.1(9)(b)); employer without MA office may withhold for MA residents as a convenience | from 2026-01-01 | US-MAS5-023 |
| `multi.resident_out_of_state.ms.withholding_rule` | Withhold MS on total wages except to the extent withheld for another State; commuter to a no-income-tax State is withheld MS on total wages (credit at assessment). MS is not a credit-only State. | from 2026-01-01 | US-MSS5-004 |
| `multi.resident_out_of_state.nc.withholding_rule` | Withhold on all wages wherever earned, except no NC withholding on wages for services in a State that requires the employer to withhold | from 2026-01-01 | US-NCP51-002 |
| `multi.resident_out_of_state.ny.withholding_rule` | Withhold NYS tax for NY residents even if wages are earned outside NY | from 2026-01-01 | US-NY-013 |
| `multi.resident_out_of_state.oh.withholding_rule` | Every employer with an office or transacting business in Ohio withholds on residents (resident credit IT RC at assessment) | from 2026-10-29 | US-OHP52-006 |
| `multi.resident_out_of_state.ok.withholding_rule` | Residents are withheld on services within or without Oklahoma (68 O.S. 2385.1 employee definition) | from 2023-07-01 | US-OKS5-010 |
| `multi.resident_out_of_state.sc.withholding_rule` | Withhold for the other State; if that State has no income tax, withhold 100% SC (12-8-520(C)(1)) | from 2026-01-01 | US-SCR3-003 |
| `multi.resident_out_of_state.vt.withholding_rule` | Compute on the full payment, then reduce by tax withheld for the State where services were performed | from 2026-01-01 | US-VTP51-003 |
| `multi.resident_out_of_state.wi.withholding_rule` | Residents working outside WI: withholding on all wages; Minnesota special arrangement - no WI withholding if MN withholds | from 2026-01-01 | US-WIS5-011 |
| `multi.transport.air_carrier` | Residence State plus the State where more than 50% of carrier pay is earned (scheduled flight time) (49 U.S.C. 40116(f)) | from 2018-10-05 | US-MULTIS5-003 |
| `multi.transport.motor_carrier` | Employee with regularly assigned duties in 2+ States: taxable ONLY by the residence State/subdivision (49 U.S.C. 14503) | from 1996-01-01 | US-MULTIS5-001 |
| `multi.transport.rail` | Residence State/subdivision only (49 U.S.C. 11502) | from 2026-01-01 | US-MULTIS5-002 |
| `multi.transport.seamen` | Seamen's wages may not be withheld for State/local tax; multi-State vessel crew and pilots taxable only by the residence State (46 U.S.C. 11108) | from 2010-10-15 | US-MULTIS5-004 |
| `multi.w2.states_per_form` | 2 | from 2026-01-01 | US-MULTIS5-011 |
| `nd.wh.method` | annual percentage method on federal W-4 (tables route under 57-38-59(3)) | from 2026-01-01 to 2026-12-31 | US-NDS5-001 |
| `ne.pit.nonresident.duty_days` | 7 | from 2025-01-01 | US-NEP51-002 |
| `nm.pit.nonresident.days_threshold` | 15 | from 2026-01-01 | US-NMP52-002 |
| `oh.local.municipal_base` | Ohio municipal income tax base = Medicare wages less 125 deductions; 401(k) deferrals taxable | from 2026-08-01 | US-OHS5-001 |
| `oh.sit.statutory` | TY2026 flat 2.75% above 26,050 (ORC 5747.02 as amended by HB 96); withholding tables still graduated to 3.4% - two instruments | from 2025-09-30 | US-OHS5-007 |
| `oh.wh.tables.effective_from` | 2026-08-01 | from 2026-08-01 | US-OHS5-001 |
| `ok.pit.nonresident.quarterly_threshold` | 300 | from 2023-07-01 | US-OKS5-010 |
| `pa.local.philadelphia.nonresident.rate` | 3.425 | from 2026-07-01 | US-PAS5-022 |
| `pa.local.philadelphia.nonresident.rate` | 3.43 | from 2025-07-01 to 2026-06-30 | US-PAS5-022 |
| `pa.local.philadelphia.resident.rate` | 3.735 | from 2026-07-01 | US-PAS5-022 |
| `pa.local.philadelphia.resident.rate` | 3.74 | from 2025-07-01 to 2026-06-30 | US-PAS5-022 |
| `practice.al.fit_before_sit` | AL state base deducts federal withholding: order FIT before AL SIT | from 2026-01-01 | US-ALS5-001 |
| `practice.ct.tables_vs_rules` | DRS: 'Use either the withholding calculation rules or the withholding tables' (TPG-211); the two methods can give different amounts; configured: DRS per-period tables up to each table maximum, TPG-211 rules above (CT.2, configuration decision of 2026-11-02) | from 2026-01-01 | US-CTS5-010 |
| `practice.dc.2026_method_unpublished` | D.C. Act 26-416 (emergency, from 2026-08-13) revoked personal exemptions; no 2026 withholding method published (D-4 under review) | from 2026-08-13 | US-DCS5-021 |
| `practice.fed.estimator_not_oracle` | IRS Tax Withholding Estimator is not an employer engine or oracle | from 2026-01-01 | US-FED-021 |
| `practice.fed.pl119_21_withholding` | Do not reduce FIT withholding for tips/overtime deductions except through W-4 Step 4(b) | from 2026-01-01 | US-FEDS5-030 |
| `practice.ga.rate_change_2026` | 4.99% for taxable years beginning on/after 2026-01-01 (5.19% before); from 2027-01-01 reduced by 0.125 point annually to 3.99%, each step delayed one year if an OPB trigger holds at 1 December | from 2026-01-01 | US-GAS5-009 |
| `practice.hi.2027_tables_pending` | Act 24 SLH 2026 changes TY2027 brackets (new 13% top); 2027 withholding indeterminate until DOTAX issues 2027 Booklet A | from 2026-01-01 | US-HIS5-029 |
| `practice.ks.kw100_header_stale` | KW-100 header prints "wages paid on and after January 1, 2021" but figures are the 2024 values in force for 2026 (5.20/5.58%) | from 2024-07-01 | US-KSS5-001 |
| `practice.mi.tips_ot_deduction_level` | MI 2025 PA 24 tips/overtime deduction (TY2026-2028) is ASSESSMENT only; no change to withholding | from 2026-01-01 to 2028-12-31 | US-MIS5-017 |
| `practice.ne.use_circular_en_tables` | Withholding uses the DOR Circular EN 2026 percentage-method tables (2.26% to 4.60% rates); the statute (77-2715.03) sets 4.55% for rate three in tax year 2026 | from 2026-01-01 | US-NES5-010 |
| `practice.oh.flat_rate_vs_tables` | Ohio withholding follows the tax commissioner's tables under ORC 5747.06, graduated 1.6% / 2.99% / 3.4% from 2026-08-01 (US-OH-006, US-OHS5-001); the ORC 5747.02 statute rate for TY2026 and thereafter is a flat 2.75% over 26,050 (US-OHS5-007) - use the tables for withholding | from 2025-09-30 | US-OHS5-007 |
| `practice.or.federal_cap` | Use 8,750 federal-tax subtraction cap (pp.6-7 formula); DOR publication also prints 8,500 and its example 1 is mis-computed | from 2026-01-01 | US-ORS5-009 |
| `practice.sc.withholding_rates_2026` | Withholding tables in force: SCDOR WH-1603 (Rev. 10/30/25) 2026 tables, 0/3/6%; SCDOR Information Letter #26-20 gives the Act 110 2026 schedule 1.99% (0-29,999) / 5.21% minus 966 (30,000+) and says withholding is unchanged until DOR republishes the tables | from 2026-01-01 | US-SCS5-004 |
| `practice.va.std_deduction_2027_not_modelled` | Statute: 2027 standard deduction 9,200/18,400; do not model 2027 withholding until Virginia Tax publishes the 2027 formula (guide Rev. 10/26 says the deduction sunsets - wrong) | from 2025-01-01 | US-VAS5-018 |
| `practice.wi.use_w166_tables` | Withholding uses W-166 schedule (3.54/4.65/5.30/7.65%), not the assessment brackets (3.50/4.40/5.30/7.65%) | from 2025-01-01 | US-WIS5-010 |
| `ut.pit.rate.flat` | 4.45 | from 2026-01-01 | US-UTS5-001 |
| `wi.pit.nonresident.de_minimis` | 1,500 | from 2026-01-01 | US-WIS5-011 |
