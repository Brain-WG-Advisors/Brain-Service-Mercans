# Module 4: Gross Compensation
*Purpose: To define all components of gross pay and their calculation rules.*

## 4.1 Minimum Wage

### Is there a minimum wage? Who is eligible?

Yes. The federal minimum wage is USD [[FACT:fed.minwage.hourly=7.25]] an hour [US-FEDS5-017] and applies to employment covered by the Fair Labor Standards Act (FLSA). Special federal rules:

| Group | Rule | Fact |
|---|---|---|
| Tipped employees (more than USD [[FACT:fed.tipped.monthly_tips_threshold=30]] a month in tips) | Cash wage USD [[FACT:fed.tipped.cash_wage.hourly=2.13]]; maximum tip credit USD [[FACT:fed.tipped.tip_credit.max_hourly=5.12]] | [US-FEDS5-019] |
| Executive, administrative and professional (EAP) exemption | Salary floor USD [[FACT:fed.exempt.salary_floor.weekly=684]] a week (USD [[FACT:fed.exempt.salary_floor.biweekly=1,368]] biweekly, USD [[FACT:fed.exempt.salary_floor.semimonthly=1,482]] semimonthly, USD [[FACT:fed.exempt.salary_floor.monthly=2,964]] monthly) | [US-FEDS5-020] |
| Apprentices, trainees, learners | No federal apprentice payroll regime; the FLSA minimum applies (sub-minimum only under DOL certificates). States set learner rates, e.g. California [[FACT:ca.minwage.learner.percent=85]]% for the first 160 hours, Washington 14-15 year olds USD [[FACT:wa.labour.minwage.youth_14_15.hourly=14.56]] in 2026 | coverage row `apprentices_and_trainees` [US-FEDS5-029, US-CAS5-006, US-WAS5-006]; [US-CAS5-006]; [US-WAS5-007] |
| Part-time employees | No part-time regime: the minimum wage and the weekly overtime threshold apply per hour and per workweek regardless of schedule | coverage row `part_time` [US-FEDS5-017, US-FEDS5-018, US-FEDS5-012] |

Several State tipped-wage rules differ from the federal one (for example `ak.minwage.tip_credit.allowed` [US-AKS5-001]: no tip credit; `wa.minwage.tip_credit.allowed` [US-WAS5-001]: no tip credit); see annexes.

### Is the minimum wage applicable at a national level or does it vary by province/state?

Both. The federal rate is a floor and the most protective applicable rate wins: [[FACT:multi.wage_hour.overlay_rule=FLSA does not excuse a higher State/municipal minimum wage, a lower maximum workweek or a stricter child-labour standard: apply the more protective standard of the place where the work is performed]] [US-MULTIS5-008]. The employer pays the highest of the federal, State and local minimum of the place where the work is performed [US-FEDS5-017]. Several cities and counties set their own rates (examples below; California municipal rates are in Annex CA).

### Provide all applicable minimum wage rates.

All dates are effective dates; a rate change applies to hours worked from the date shown.

| Jurisdiction | Hourly minimum wage | Fact |
|---|---|---|
| Federal (FLSA) | USD [[FACT:fed.minwage.hourly=7.25]] (from 2009-07-24) | [US-FEDS5-017] |
| AK | USD [[FACT:ak.minwage.hourly=13.00]] (from 2025-07-01 to 2026-06-30); USD [[FACT:ak.minwage.hourly=14.00]] (from 2026-07-01 to 2027-06-30); USD [[FACT:ak.minwage.hourly=15.00]] (from 2027-07-01) | [US-AKS5-001] |
| AR | USD [[FACT:ar.minwage.hourly=11.00]] (from 2021-01-01) | [US-ARS5-002] |
| AZ | USD [[FACT:az.minwage.hourly=15.15]] (from 2026-01-01 to 2026-12-31); USD [[FACT:az.minwage.hourly=15.65]] (from 2027-01-01) | [US-AZB5-001] |
| CA | USD [[FACT:ca.minwage.hourly=16.90]] (from 2026-01-01 to 2026-12-31); USD [[FACT:ca.minwage.hourly=17.40]] (from 2027-01-01) | [US-CAS5-006] |
| CO | USD [[FACT:co.minwage.hourly=15.16]] (from 2026-01-01 to 2026-12-31) | [US-COB5-001] |
| CT | USD [[FACT:ct.minwage.hourly=16.94]] (from 2026-01-01 to 2026-12-31); USD [[FACT:ct.minwage.hourly=17.48]] (from 2027-01-01) | [US-CTS5-008] |
| DC | USD [[FACT:dc.minwage.hourly=17.95]] (from 2025-07-01 to 2026-06-30); USD [[FACT:dc.minwage.hourly=18.40]] (from 2026-07-01) | [US-DCS5-011] |
| DE | USD [[FACT:de.minwage.hourly=15.00]] (from 2025-01-01) | [US-DES5-001] |
| FL | USD [[FACT:fl.minwage.hourly=14.00]] (from 2025-09-30 to 2026-09-29); USD [[FACT:fl.minwage.hourly=15.00]] (from 2026-09-30 to 2027-12-31) | [US-FLS5-001] |
| HI | USD [[FACT:hi.minwage.hourly=16.00]] (from 2026-01-01 to 2027-12-31); USD [[FACT:hi.minwage.hourly=18.00]] (from 2028-01-01) | [US-HIS5-001] |
| IA | USD [[FACT:ia.minwage.hourly=7.25]] (from 2008-01-01) | [US-IAS5-001] |
| ID | USD [[FACT:id.minwage.hourly=7.25]] (from 2009-07-24) | [US-IDS5-001] |
| IL | USD [[FACT:il.minwage.hourly=15.00]] (from 2025-01-01) | [US-ILS5-001] |
| IN | USD [[FACT:in.minwage.hourly=7.25]] (from 2009-07-24) | [US-FEDS5-017] |
| KS | USD [[FACT:ks.minwage.hourly=7.25]] (from 2010-01-01) | [US-KSS5-008] |
| KY | USD [[FACT:ky.minwage.hourly=7.25]] (from 2009-07-01) | [US-KYS5-001] |
| MA | USD [[FACT:ma.minwage.hourly=15.00]] (from 2023-01-01) | [US-MAS5-001] |
| MD | USD [[FACT:md.minwage.hourly=15.00]] (from 2024-01-01) | [US-MDS5-005] |
| ME | USD [[FACT:me.minwage.hourly=15.10]] (from 2026-01-01 to 2026-12-31); USD [[FACT:me.minwage.hourly=15.70]] (from 2027-01-01) | [US-MES5-002] |
| MI | USD [[FACT:mi.minwage.hourly=13.73]] (from 2026-01-01 to 2026-12-31); USD [[FACT:mi.minwage.hourly=15.00]] (from 2027-01-01) | [US-MIS5-001] |
| MN | USD [[FACT:mn.minwage.hourly=11.41]] (from 2026-01-01 to 2026-12-31); USD [[FACT:mn.minwage.hourly=11.87]] (from 2027-01-01) | [US-MNS5-002] |
| MO | USD [[FACT:mo.minwage.hourly=15.00]] (from 2026-01-01) | [US-MOS5-002] |
| MT | USD [[FACT:mt.minwage.hourly=10.85]] (from 2026-01-01 to 2026-12-31) | [US-MTS5-014] |
| ND | USD [[FACT:nd.minwage.hourly=7.25]] (from 2009-07-24) | [US-NDS5-006] |
| NE | USD [[FACT:ne.minwage.hourly=15.00]] (from 2026-01-01 to 2026-12-31) | [US-NES5-001] |
| NJ | USD [[FACT:nj.minwage.hourly=15.92]] (from 2026-01-01 to 2026-12-31); USD [[FACT:nj.minwage.hourly=16.48]] (from 2027-01-01 to 2027-12-31) | [US-NJS5-009] |
| NM | USD [[FACT:nm.minwage.hourly=12.00]] (from 2023-01-01) | [US-NMS5-004] |
| NV | USD [[FACT:nv.minwage.hourly=12.00]] (from 2024-07-01) | [US-NVS5-013] |
| NY | New York City, Long Island, Westchester: USD [[FACT:ny.minwage.nyc_li_westchester.hourly=17.00]] (from 2026-01-01); rest of State: USD [[FACT:ny.minwage.rest.hourly=16.00]] (from 2026-01-01) | [US-NYS5-001] |
| OH | USD [[FACT:oh.minwage.hourly=11.00]] (from 2026-01-01 to 2026-12-31); USD [[FACT:oh.minwage.hourly=11.40]] (from 2027-01-01 to 2027-12-31) | [US-OHS5-005] |
| OR | standard (Portland metro and nonurban rates in annex OR): USD [[FACT:or.labour.minwage.standard.hourly=15.05]] (from 2025-07-01 to 2026-06-30); USD [[FACT:or.labour.minwage.standard.hourly=15.55]] (from 2026-07-01 to 2027-06-30) | [US-ORS5-002] |
| PA | USD [[FACT:pa.minwage.hourly=7.25]] (from 2009-07-24) | [US-PAS5-002] |
| RI | USD [[FACT:ri.minwage.hourly=16.00]] (from 2026-01-01 to 2026-12-31); USD [[FACT:ri.minwage.hourly=17.00]] (from 2027-01-01) | [US-RIS5-001] |
| SD | USD [[FACT:sd.minwage.hourly=11.85]] (from 2026-01-01 to 2026-12-31); USD [[FACT:sd.minwage.hourly=12.30]] (from 2027-01-01) | [US-SDS5-003] |
| TX | State rate: USD [[FACT:tx.minwage.hourly=7.25]] (from 2003-09-01) | [US-FEDS5-017] |
| UT | USD [[FACT:ut.minwage.hourly=7.25]] (from 2009-07-24) | [US-UTS5-011] |
| VA | USD [[FACT:va.minwage.hourly=12.77]] (from 2026-01-01 to 2026-12-31); USD [[FACT:va.minwage.hourly=13.75]] (from 2027-01-01 to 2027-12-31); USD [[FACT:va.minwage.hourly=15.00]] (from 2028-01-01) | [US-VAS5-001] |
| VT | USD [[FACT:vt.minwage.hourly=14.42]] (from 2026-01-01 to 2026-12-31) | [US-VTS5-003] |
| WA | USD [[FACT:wa.minwage.hourly=17.13]] (from 2026-01-01 to 2026-12-31); USD [[FACT:wa.minwage.hourly=17.73]] (from 2027-01-01) | [US-WAS5-006] |
| WI | USD [[FACT:wi.minwage.hourly=7.25]] (from 2009-07-24) | [US-WIS5-001] |
| WV | USD [[FACT:wv.minwage.hourly=8.75]] (from 2016-01-01) | [US-WVS5-007] |
| WY | USD [[FACT:wy.minwage.hourly=5.15]] (from 2026-05-08) | [US-WYS5-001] |
| AL, GA, LA, MS, NC, NH, OK, SC, TN | No State minimum-wage fact in the pack; the federal floor applies to FLSA-covered employment | see request below |

Local minimum wages (examples; full lists in the annexes):

| Locality | Rate | Fact |
|---|---|---|
| Seattle, WA | USD [[FACT:wa.labour.minwage.local.seattle.hourly=21.30]] (from 2026-01-01 to 2026-12-31) | [US-WAS5-008] |
| Tukwila, WA | USD [[FACT:wa.labour.minwage.local.tukwila.hourly=21.65]] (from 2026-01-01 to 2026-12-31) | [US-WAS5-008] |
| SeaTac, WA (hospitality and transportation) | USD [[FACT:wa.labour.minwage.local.seatac.hourly=20.74]] (from 2026-01-01 to 2026-12-31) | [US-WAS5-008] |
| Montgomery County, MD (51+ employees) | USD [[FACT:md.local_minwage.montgomery.51_plus=18]] (from 2026-07-01) | [US-MDS5-015] |
| Howard County, MD | USD [[FACT:md.local_minwage.howard=16]] (from 2026-07-01) | [US-MDS5-015] |
| Prince George's County, MD | USD [[FACT:md.local_minwage.prince_georges=15.30]] (from 2026-07-01) | [US-MDS5-015] |

Not configured in this release [[GAP:RQ-560]]: No State minimum-wage fact for AL, GA, LA, MS, NC, NH, OK, SC, TN; whether each has a State rate (relevant to employment outside FLSA coverage) is not established.

Coverage of mid-year changes (coverage row `mid_year_rate_change` [US-DCS5-011, US-ORS5-002, US-OHS5-001, US-PAS5-022, US-FEDS5-030]): the District of Columbia, Oregon and Alaska change on 2026-07-01, Florida on 2026-09-30, and the Nevada daily overtime rule on 2026-07-01; each rate is applied by the date the hours were worked.

### Does the minimum wage impact any tax or social security calculations?

Not the tax or contribution rates. It feeds three payroll calculations:

| Calculation | How the minimum wage enters | Fact |
|---|---|---|
| Federal garnishment protection | Protected amount USD [[FACT:fed.ccpa.protected_weekly=217.50]] a week = 30 x the federal minimum wage | [US-FEDS5-023] |
| State garnishment protection | Multiples of the higher State or federal minimum, e.g. California [[FACT:ca.garn.creditor.minwage_multiple.weekly=48]] x (weekly), Arizona [[FACT:az.garn.creditor.minwage_multiple=60]] x, Colorado weekly floor USD [[FACT:co.garn.creditor.weekly_floor=606.40]], Connecticut weekly protected USD [[FACT:ct.garn.creditor.weekly_protected=677.60]] | [US-CAS5-013]; [US-AZS5-016]; [US-COS5-009]; [US-CTS5-024] |
| Tip credit | Cash wage plus tip credit must reach the minimum: USD [[FACT:fed.tipped.cash_wage.hourly=2.13]] + USD [[FACT:fed.tipped.tip_credit.max_hourly=5.12]] = USD [[FACT:fed.minwage.hourly=7.25]] | [US-FEDS5-019] |

### How are deductions handled if they cannot be made due to minimum wage constraints?

Not configured in this release [[GAP:RQ-561]]: The FLSA rule on deductions that would reduce pay below the minimum wage (and the State variants) is not established from an official source.
Statutory deductions (taxes, garnishments within their limits) are not limited by the minimum wage; the garnishment protected amounts in Module 7 apply instead.

## 4.2 Salary Components

### What are the mandatory and common salary components?

Federal law mandates no salary component other than the minimum wage and the overtime premium. The components that the law classifies, and that the WTC must carry, are:

| Component | Classification that matters | Fact |
|---|---|---|
| Regular wages (salary or hourly) | Regular wages: Worksheet 1A method | `fed.fit.method` |
| Overtime premium | Regular wages for withholding; qualified overtime reported on the W-2 | `fed.plaw119_21.qualified_overtime.level` [US-FEDS5-030] |
| Tips | Subject to withholding and FICA when USD [[FACT:fed.tips.reporting_threshold_monthly=20]] or more in a month | [US-FEDS5-003] |
| Bonuses, commissions, severance | Supplemental wages: flat [[FACT:fed.fit.supplemental.flat_rate=22]]% optional or aggregate | [US-FEDS5-003] |
| Non-cash fringe benefits | Taxable unless an exclusion applies (Module 7) | `fed.bik.parking.monthly_exclusion` [US-FEDS5-008] and related keys |

### What is the general definition and pay cycle for each component?

Regular wages are paid on the employer's regular payday under the work State's pay-frequency rule (Module 1 §1.2). Overtime is due with the wages of the period, or by the next regular payday where a State says so (for example `ca.pay_frequency.rule` [US-CAS5-009]). Supplemental wages may be paid with or separately from regular wages; the withholding method depends on that choice (Module 6 §6.2).

### Which components are taxable vs non-taxable and sociable vs non-sociable?

| Component | Federal income tax | FICA (social security and Medicare) | FUTA | Fact |
|---|---|---|---|---|
| Regular wages, overtime, bonuses, commissions | Taxable | Subject | Subject (wages) | [US-FEDS5-030]; [US-FED-013]; coverage row `overtime` [US-FEDS5-018, US-FEDS5-030, US-CAS5-008] |
| Severance and pay in lieu of notice | Taxable | Subject | Subject | `fed.severance.is_wages` [US-FEDS5-029] |
| Tips | [[FACT:fed.base.tips.fit=withhold on cash tips of 20 or more in a month (tips under 20 a month and non-cash tips: exempt)]] | [[FACT:fed.base.tips.fica=included for cash tips of 20 or more in a month; excluded under 20 a month]] | [[FACT:fed.base.tips.futa=included for all tips of 20 or more in a month reported in writing to the employer; excluded under 20 a month]] | [US-FEDS5-029]; [US-FEDS5-003] |
| Group-term life insurance | [[FACT:fed.base.group_term_life.fit=excluded (employer may at its option withhold on the cost of coverage over 50,000)]] | [[FACT:fed.base.group_term_life.fica=excluded up to the cost of 50,000 of coverage; the cost of coverage over 50,000 less employee payments is included (W-2 boxes 1, 3, 5 and box 12 code C)]] | [[FACT:fed.base.group_term_life.futa=excluded]] | [US-FEDS5-008] |
| PFML employee contribution | W-2 wages | W-2 wages | No FUTA exclusion is configured for the contribution: it is withheld from wages, which stay wages under the general definition | [US-FEDS5-007]; [US-FEDQ1-002] |
| Transit passes, commuter vehicle and qualified parking | [[FACT:fed.base.transportation.fit=excluded up to 340 a month for commuter highway vehicle and transit passes and 340 a month for qualified parking]] | [[FACT:fed.base.transportation.fica=excluded up to 340 a month for commuter highway vehicle and transit passes and 340 a month for qualified parking]] | [[FACT:fed.base.transportation.futa=excluded up to 340 a month for commuter highway vehicle and transit passes and 340 a month for qualified parking]] | [US-FEDS5-008] |
| Educational assistance | [[FACT:fed.base.educational_assistance.fit=excluded up to 5,250 a year under a qualifying educational assistance program]] | [[FACT:fed.base.educational_assistance.fica=excluded up to 5,250 a year under a qualifying educational assistance program]] | [[FACT:fed.base.educational_assistance.futa=excluded up to 5,250 a year under a qualifying educational assistance program]] | [US-FEDS5-008] |
| Dependent-care assistance | [[FACT:fed.base.dependent_care.fit=excluded up to 7,500 a year (3,750 married filing separately)]] | [[FACT:fed.base.dependent_care.fica=excluded up to 7,500 a year (3,750 married filing separately)]] | [[FACT:fed.base.dependent_care.futa=excluded up to 7,500 a year (3,750 married filing separately)]] | [US-FEDS5-008] |
| Retirement deferrals and Section 125 reductions | See Module 3, Step 2 | See Module 3, Step 2 | See Module 3, Step 2 | [US-FEDS5-029] |
| Moving expenses, bicycle commuting | No exclusion (eliminated, except moving for Armed Forces / intelligence community) | No exclusion | No exclusion | `fed.bik.moving_and_bicycle.excluded` [US-FEDS5-008] |
| Ministers' pay | No withholding (self-employment tax); parsonage allowance excluded from W-2 box 1 | Not withheld | [[FACT:fed.minister.futa=FUTA excludes service in the employ of a 501(c)(3) religious organization (26 U.S.C. 3306(c)(8)); the exemption cannot be waived. A minister's pay is outside FUTA when the employer is a 501(c)(3) church or organization; if the employer is not 501(c)(3) this exclusion does not apply. Pub. 15-A states no separate minister FUTA rule.]] [US-FEDV6-017] | `fed.minister.withholding` [US-FED-030] |

Statutory wage definitions behind the table:

| Base | Definition and exclusions | Source |
|---|---|---|
| All federal employment taxes (general) | [[FACT:fed.wages.general_definition=Wages subject to federal employment taxes generally include all pay given to an employee for services, in cash or other forms (salaries, vacation allowances, bonuses, commissions, taxable fringe benefits), however measured or paid; signing bonuses and payments for cancellation of an employment contract are wages for social security, Medicare, FUTA and income-tax withholding; pay to a former employee for services performed while employed is wages.]] | [US-FEDQ1-002] |
| FICA wages | [[FACT:fed.fica.wage_definition.exclusions=FICA wages (IRC 3121(a)) are all remuneration for employment, including non-cash remuneration, except among others: (a)(1) pay above the OASDI wage base (OASDI only); (a)(2) sickness, accident, medical and hospitalization plan payments; (a)(5) payments to or from qualified plans (401(a), 403(a), SEP, 403(b) other than salary reduction, governmental 457, SIMPLE other than elective contributions) and (5)(G) section 125 cafeteria-plan benefits that would not be wages outside the plan; (a)(12) non-cash tips and cash tips under 20 a month; (a)(18) 127/129/134 benefits; (a)(19) meals and lodging excludable under 119; (a)(20) 74(c), 108(f)(4), 117 and 132 fringes. 3121(v)(1): 401(k) elective deferrals and 414(h) salary-reduction pickups remain FICA wages.]] | [US-FEDQ3-002] |
| FUTA wages | [[FACT:fed.futa.wage_definition.exclusions=FUTA wages (IRC 3306(b)) are all remuneration for employment, including non-cash remuneration, except among others: (b)(1) pay above the 7,000 FUTA wage base; (b)(2) sickness, accident, medical plan payments; (b)(5) qualified-plan payments as in 3121(a)(5), incl. (5)(G) section 125 cafeteria-plan benefits; (b)(13) 127/129/134 benefits; (b)(14) meals and lodging under 119; (b)(16) 74(c), 117, 132 fringes; (b)(17) 106(b); (b)(18) 106(d) HSA. 3306(r)(1): 401(k) elective deferrals remain FUTA wages. Tips: only cash tips of 20 or more a month reported in writing are FUTA wages (Pub. 15 p.52).]] | [US-FEDQ3-003] |
| Income-tax withholding wages | Module 6 §6.1.1 (26 U.S.C. 3401(a)) | Module 6 |

### Are components uniform across the country or do they differ by state/province?

Federal classification is uniform. State classification differs, because each State decides its own conformity (examples: `ca.obbba.conforms` [US-CAS5-020] no State tips or overtime deduction; `pa.bik.pa.401k_403b_457.taxable` [US-PAS5-011]; `nj.sui.wages.401k_included` [US-NJS5-017]; `ms.bik.section125.excluded` [US-MSS5-004]). Each State annex carries its own inclusion and exclusion rules.

### What is the calculation logic for each salary component?

| Component | Logic |
|---|---|
| Salaried | Periodic salary for the pay period; proration only where the employer's policy applies it (§4.3) |
| Hourly | Hours worked x hourly rate, at least the applicable minimum wage (§4.1) |
| Overtime | Overtime hours x regular rate x [[FACT:fed.overtime.premium.multiplier=1.5]] (§4.4) |
| Tipped | Cash wage + tips; employer tops up to the minimum when the tip credit does not reach it ([US-FEDS5-019]) |
| Supplemental | Amount as granted; withholding method per Module 6 |

### Which components require employee-declared values and submissions?

| Declaration | Content | Fact |
|---|---|---|
| Form W-4 | [[FACT:fed.w4.input_fields=filing status (Single/MFS, MFJ/QSS, HoH); Step 2 flag; Step 3 amount; Step 4(a); Step 4(b); Step 4(c); exempt checkbox]] | [US-FEDS5-006] |
| State withholding certificate | Per State (Module 2) | annexes |
| Tip report | Tips of USD [[FACT:fed.tips.reporting_threshold_monthly=20]] or more in a month reported to the employer | [US-FEDS5-003] |
| Treaty exemption (nonresident alien) | Form 8233; treaty-exempt wages reported on Form 1042-S | `fed.fit.nra.treaty_exempt.reporting` [US-FEDS5-016] |
| Reciprocity / nonresidence certificate | Per work State (Module 2) | `multi.reciprocity.*` |

### Deliverable: Define the primary earnings base for social security contributions. Produce a comprehensive Inclusion/Exclusion analysis.

The primary base is FICA wages: all remuneration for employment unless excluded. It feeds three different caps:

| Base | Cap 2026 | Fact |
|---|---|---|
| OASDI | USD [[FACT:fed.fica.oasdi.wage_base=184,500]] per employer | [US-FEDS5-005] |
| Medicare | No cap; Additional Medicare above USD [[FACT:fed.fica.addl_medicare.withholding_threshold=200,000]] | [US-FEDS5-005] |
| FUTA | USD [[FACT:fed.futa.wage_base=7,000]] per employer | [US-FED-007] |

Inclusion/exclusion analysis: the rows supported by the facts are in the table of the previous question; the complete statutory list is research gap `fed.fica.wage_definition.exclusions`. State unemployment bases follow their own definitions (Module 5 §5.1.1).

## 4.3 Proration

### Are fixed wages prorated for the number of working days?

No statutory rule. Federal law sets no proration method (coverage row `mid_month_joiner_and_leaver` [US-FEDS5-001, US-FEDS5-024, US-MULTIS5-009]); withholding is computed on the wages actually paid in the period. Whether a fixed salary is prorated, and on which day count, is the employer's policy, subject to the minimum wage for the hours worked and, for EAP-exempt staff, the salary-basis floor (USD [[FACT:fed.exempt.salary_floor.weekly=684]] a week, [US-FEDS5-020]).

### Describe the statutory or standard business practice for prorating fixed salary components for mid-period hires and terminations.

Configuration choice (non-statutory): the engine offers a working-day or a calendar-day factor per pay group. The chosen factor is applied to every fixed component of the period; variable components are paid as earned.

### Provide the proration formula and a worked example.

```
prorated_salary = round( period_salary x days_in_service / days_in_period , 2 )   # half-up to the cent
```

Worked example (configuration choice, working-day factor; computed by the build record):

| Calculation | Result |
|---|---|
| Scenario: monthly salary 6,300.00; 22 working days in the month; hired on working day 13 (10 working days in service) |  |
| 6,300.00 × 10 ÷ 22 | 2,863.64 |

## 4.4 Overtime

### Detail the statutory rules for overtime, including eligibility criteria and mandatory rates.

Federal (coverage row `overtime` [US-FEDS5-018, US-FEDS5-030, US-CAS5-008]): [[FACT:fed.overtime.premium.multiplier=1.5]] x the regular rate for hours over [[FACT:fed.overtime.weekly_threshold_hours=40]] in a workweek [US-FEDS5-018]; there is no federal daily overtime. EAP-exempt employees paid at least the salary floor are excluded. States add daily or seventh-day overtime:

| Jurisdiction | Rule | Fact |
|---|---|---|
| CA | [[FACT:ca.overtime.rule=1.5x over 8 h/day, over 40 h/week and first 8 h of 7th consecutive day; 2x over 12 h/day and over 8 h on 7th day (Lab. Code 510); alternative workweek exceptions]] | [US-CAS5-008] |
| AK | [[FACT:ak.overtime.premium.multiplier=1.5]] x over [[FACT:ak.overtime.daily_threshold_hours=8]] hours a day and over [[FACT:ak.overtime.weekly_threshold_hours=40]] a week; employers with fewer than 4 employees exempt | [US-AKS5-001] |
| NV | From 2026-07-01: employees earning under USD [[FACT:nv.overtime.daily_threshold_wage=18]] an hour get 1.5 x over 8 hours in 24 hours | [US-NVS5-003] |
| WA | [[FACT:wa.overtime.premium.multiplier=1.5]] x over [[FACT:wa.overtime.weekly_threshold_hours=40]] hours a week; no daily overtime | [US-WAS5-001] |
| DC | Over [[FACT:dc.overtime.weekly_threshold_hours=40]] hours a week; no daily overtime | [US-DCS5-001] |

Worked example (computed by the examples script from the federal facts):

| Calculation | Result |
|---|---|
| Scenario: non-exempt employee, USD 26.50 an hour, 46 hours in the workweek, no State daily overtime |  |
| [[FACT:fed.overtime.weekly_threshold_hours=40]] × 26.50 | 1,060.00 |
| 46 − [[FACT:fed.overtime.weekly_threshold_hours=40]] | 6 |
| 6 × 26.50 × [[FACT:fed.overtime.premium.multiplier=1.5]] | 238.50 |
| 1,060.00 + 238.50 | 1,298.50 |

### Explain how overtime is treated for income tax and social security calculations.

Overtime is regular wages for withholding and fully subject to FICA, FUTA and SUI. The federal qualified-overtime deduction operates only at assessment: [[FACT:fed.plaw119_21.qualified_overtime.level=assessment (employee return); withholding only via W-4 Step 4(b); employer reports W-2 Box 12 TT; overtime remains fully subject to FICA]] [US-FEDS5-030]; the employee's annual deduction is capped at USD [[FACT:fed.plaw119_21.qualified_overtime.deduction_cap=12,500]] (USD [[FACT:fed.plaw119_21.qualified_overtime.deduction_cap_mfj=25,000]] married filing jointly) [US-FEDS5-030]. Build rule: [[FACT:practice.fed.pl119_21_withholding=Do not reduce FIT withholding for tips/overtime deductions except through W-4 Step 4(b)]] [US-FEDS5-030].

State overtime deductions also operate at assessment only (never reduce State withholding):

| State | Rule | Fact |
|---|---|---|
| AL | Overtime premium deduction up to USD [[FACT:al.pit.overtime_premium_deduction.max=1,000]], assessment only | [US-ALS5-004] |
| GA | Overtime subtraction up to USD [[FACT:ga.pit.overtime_subtraction.max=1,750]], assessment only | [US-GAS5-009] |
| MI | [[FACT:mi.pit.tips_overtime_deduction=2025 PA 24 (MCL 206.30(1)(ee)): tax years 2026-2028 deduct federally allowed qualified tips (IRC 224) and overtime (IRC 225); level ASSESSMENT (MI-1040) only - no withholding change]] | [US-MIV6-002] |
| IA | [[FACT:ia.pit.obbba=tips, overtime, car-loan interest conformed at ASSESSMENT only (no withholding allowance); senior deduction (up to 6,000) may be claimed as an IA W-4 allowance]] | [US-IAS5-019] |
| DC | [[FACT:dc.pit.obbba_deductions=disallowed TY2025; allowed as DC deductions from TY2026; operating level assessment only (no withholding change)]] | [US-DCS5-021] |
| CO | Colorado's worksheet removes the federal qualified-overtime deduction from W-4 Step 4(b) for State withholding | `co.wh.obbba_overtime_deduction.allowed` [US-COS5-012] |
| CA | `ca.obbba.conforms` [US-CAS5-020]: no State tips or overtime deduction | [US-CAS5-020] |
| HI | Not configured in this release [[GAP:RQ-563]]: The Hawaii treatment of tips and overtime deductions is not established from an official source. | |

W-2 reporting of overtime and tips: [[FACT:fed.w2.box12.new_codes=TP (cash tips reported to employer); TT (qualified overtime compensation); TA (employer Trump-account contributions)]] [US-FEDS5-007].

## 4.5 Bonuses

### Is there a statutory requirement to pay bonuses? If so, how are they calculated?

Not configured in this release [[GAP:RQ-564]]: No official source read for this release states whether any federal or State statute requires a private employer to pay a bonus (13th-month or similar)

### Is there a specific tax treatment for bonuses?

Yes. Bonuses are supplemental wages. Federal: flat [[FACT:fed.fit.supplemental.flat_rate=22]]% (optional) or the aggregate method; [[FACT:fed.fit.supplemental.mandatory_rate=37]]% mandatory on supplemental wages above USD [[FACT:fed.fit.supplemental.mandatory_threshold=1,000,000]] paid to one employee in the calendar year [US-FEDS5-003]. FICA applies as to regular wages (coverage row `special_pay_cycles` [US-FEDS5-003, US-FEDS5-001, US-CAS5-004]). States set their own supplemental methods:

| State | Supplemental method | Fact |
|---|---|---|
| CA | Bonuses and stock options [[FACT:ca.wh.supplemental.rate.bonus_stock_options=10.23]]%; other supplemental [[FACT:ca.wh.supplemental.rate.other=6.6]]% (when paid separately) | [US-CAS5-004] |
| ID | Flat [[FACT:id.wh.supplemental.rate=5.3]]% on a separately issued payment, or aggregate | [US-IDS5-008] |
| ND | Flat [[FACT:nd.wh.supplemental.rate=1.5]]% or aggregate | [US-NDS5-001] |
| KY | [[FACT:ky.wh.supplemental.method=no separate rate; bonuses and severance through the same formula; film-incentive companies at max 141.020 rate]] | [US-KY-001] |
| SC | No flat supplemental rate: bonuses through the tables | `sc.pit.supplemental.flat_rate.exists` [US-SCS5-002] |

A worked bonus example is in Module 6 §6.3.

## 4.6 Wage Classification (Country-Specific)

### Are there country-specific classifications for wages critical for social security or tax calculations?

Yes. US payroll classifies each payment along four independent axes; one payment can fall in different classes for different bases.

### Provide a detailed definition for each classification.

| Classification | Definition | Fact |
|---|---|---|
| Regular vs supplemental wages | Supplemental = bonuses, commissions, severance and similar; may be withheld at a flat rate | [US-FEDS5-003] |
| Withholding wages vs FICA wages | A payment can be FICA wages without income-tax withholding being required (group-term life cost above USD [[FACT:fed.bik.group_term_life.excluded_coverage=50,000]] of coverage); a statutory employee's pay is FICA-withheld with no income-tax withholding | [US-FEDS5-008]; `fed.statutory_employee.treatment` [US-FEDR3-005] |
| Taxable wage base vs total wages | OASDI, FUTA and each SUI/PFML base stop at a cap; Medicare does not | [US-FED-007] |
| Qualified tips and qualified overtime | Reported separately on the W-2 from tax year 2026, Box 12 codes: [[FACT:fed.w2.box12.new_codes=TP (cash tips reported to employer); TT (qualified overtime compensation); TA (employer Trump-account contributions)]] | [US-FEDS5-007] |
| State and local wages | Wages allocated to each State and locality; the W-2 carries up to [[FACT:multi.w2.states_per_form=2]] States and localities per form | [US-MULTIS5-011] |

### Create a reference table classifying common pay components.

| Pay component | Regular / supplemental | Federal income tax | FICA | W-2 reporting |
|---|---|---|---|---|
| Salary, hourly wages | Regular | Worksheet 1A | Yes | W-2 wages |
| Overtime premium | Regular | Worksheet 1A | Yes | Box 12 code TT for qualified overtime ([US-FEDS5-007]) |
| Cash tips reported | Regular | Worksheet 1A | Yes | Box 12 code TP; box 14b occupation code ([US-FEDS5-007]) |
| Bonus, commission | Supplemental | Flat or aggregate | Yes | W-2 wages ([US-FEDS5-003]) |
| Severance | Supplemental | Flat or aggregate | Yes | W-2 wages ([US-FEDS5-029]) |
| Group-term life cost above the excluded coverage | Imputed | Not required | Yes | ([US-FEDS5-008]) |
| Employer Trump-account contribution | Employer contribution | Excluded up to USD [[FACT:fed.bik.trump_account.employer_contribution_max=2,500]] from 2026-07-04 | Not configured in this release [[GAP:RQ-591]]: FICA and FUTA treatment of the employer contribution is not established from an official source. | Box 12 code TA ([US-FEDS5-030]) |

Prevailing wage (public works) is an optional informational flag [US-OWN-009]: this guide documents prevailing-wage laws, thresholds and certified-payroll duties as an overlay, and the payroll build does not produce certified payroll reports.

Prevailing-wage overlay: federal construction contracts over USD [[FACT:fed.davis_bacon.contract_threshold=2,000]] carry Davis-Bacon wage rates and weekly certified payroll ([[FACT:fed.davis_bacon.certified_payroll.frequency=weekly, to the contracting agency; prime responsible for subcontractors; optional form WH-347; records 3 years]]; [US-FEDS5-027]). State prevailing-wage laws are in the annexes; never use the federal DOL State list for Michigan.

Not configured in this release [[GAP:RQ-541]]: the DOL Women's Bureau paid-leave page could not be read; the DOL prevailing-wage list still says MI has no law (MI restored 2023).
