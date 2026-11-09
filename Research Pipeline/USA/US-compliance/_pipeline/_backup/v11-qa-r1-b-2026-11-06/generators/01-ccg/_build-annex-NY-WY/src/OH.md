## @labour
- **Minimum wage (Ohio Const. art. II s.34a) [US-OHS5-005, US-OHS5-004].** 2026: {{oh.minwage.hourly@2026-01-01}} USD per hour non-tipped; tipped cash wage {{oh.minwage.tipped.cash_wage@2026-01-01}} USD. Employers grossing under {{oh.labour.minwage.small_employer.gross_threshold@2026-01-01}} USD a year, and employees under 16, are paid the federal minimum wage (Annex FED). 2027 (published): {{oh.minwage.hourly@2027-01-01}} USD and {{oh.minwage.tipped.cash_wage@2027-01-01}} USD; small-employer threshold {{oh.labour.minwage.small_employer.gross_threshold@2027-01-01}} USD.
- **No local minimum wages.** Local regulation of hours, scheduling and benefits for private employers is preempted (ORC 4113.85): {{oh.local_mandates.preempted}} [US-OHS5-012]. No city minimum wage was located; the minimum-wage preemption text itself (ORC 4111.02) was not read.
- **Overtime (ORC 4111.03) [US-OHS5-003].** {{oh.overtime.premium.multiplier}} times the regular rate over {{oh.overtime.weekly_threshold_hours}} hours per workweek, following FLSA exemptions; no daily overtime. Small employers below the poster's gross-receipts test are outside the state overtime duty [US-OHS5-004, US-OHS5-005].
- **Pay frequency and pay day (ORC 4113.15) [US-OHS5-015, US-OH-004]:** {{oh.pay_frequency.rule}}. Daily or weekly pay is allowed, as is a longer customary or contractual lapse; liquidated damages accrue on wages left unpaid beyond the statutory period.
- **Payment timing and method (ORC 4113.15) [US-OHV6-004]:** {{oh.payment.method}}.
- **Records:** name, address, occupation, rate, pay per period, hours per day and week, kept {{oh.records.wage_hour.retention_years}} years [US-OHS5-005].

## @income_tax
- **Statutory rate (HB 96, ORC 5747.02(A)(3), effective 2025-09-30) [US-OHS5-007].** From tax year 2026 a flat {{oh.pit.statutory.rate}} % on Ohio taxable income above a zero bracket of {{oh.pit.statutory.zero_bracket}} USD.
- **Withholding schedule is not the statutory rate.** The commissioner's withholding tables and formula (ORC 5747.06) still graduate above the statutory flat rate. The two instruments are both correct for their level: the payroll engine withholds under the tables (5747.06); the flat rate (5747.02) applies at assessment. Never replace the withholding schedule with the statutory rate.
- **Mid-year change: two withholding editions in 2026.**

| Pay dates | Rate band 1 | Band 2 | Band 3 | Breakpoints | Base tax at band 2 / band 3 | Register id |
|---|---|---|---|---|---|---|
| 2025-10-01 to 2026-07-31 | {{oh.pit.wh.rate.1@2025-10-01}} % | {{oh.pit.wh.rate.2@2025-10-01}} % | {{oh.pit.wh.rate.3@2025-10-01}} % | {{oh.pit.wh.break.1@2025-10-01}} / {{oh.pit.wh.break.2@2025-10-01}} USD | {{oh.pit.wh.base_tax.2@2025-10-01}} / {{oh.pit.wh.base_tax.3@2025-10-01}} USD | US-OHP52-001 |
| from 2026-08-01 | {{oh.pit.wh.rate.1@2026-08-01}} % | {{oh.pit.wh.rate.2@2026-08-01}} % | {{oh.pit.wh.rate.3@2026-08-01}} % | {{oh.pit.wh.break.1@2026-08-01}} / {{oh.pit.wh.break.2@2026-08-01}} USD | {{oh.pit.wh.base_tax.2@2026-08-01}} / {{oh.pit.wh.base_tax.3@2026-08-01}} USD | US-OHS5-001 |

- **Formula (annualised).** Taxable wages TW = pay x pay periods - {{oh.pit.wh.exemption.annual}} USD x exemptions; tax = base tax of the band + band rate x (TW - lower breakpoint); withholding = tax / pay periods. Edition text: earlier period {{oh.pit.wh.method.period_a}}; from 2026-08-01 {{oh.pit.wh.method.period_b}}. Percentage tables per pay frequency are published with each edition [US-OH-006, US-OH-002].
- **Oracle:** biweekly pay, one exemption, paid on or after 2026-08-01: withholding {{oh.pit.oracle.example_1.withholding}} USD (table and formula agree) [US-OHS5-001]. Recomputation is in Module 12 and the validation suite.
- **Rounding:** no rounding instruction in the tables or the formula; whole-dollar rounding (ORC 718.25) is optional on municipal returns only [US-OHP52-002].
- **Supplemental wages (OAC 5703-7-10, from 2026-01-01):** withheld at the highest statutory rate of the year, OAC 5703-7-10 [US-OHS5-017]; that rate is {{oh.wh.supplemental.rate}} %, ORC 5747.02(A)(3)(c) [US-OHS5-007].
- **Certificate:** {{oh.wh.certificate}} [US-OHP52-006].
- **Exemptions from withholding (5747.06) [US-OHS5-008]:** agricultural labour, domestic service, service in a quarter with cash pay under {{oh.pit.exempt.quarterly_cash_threshold}} USD, foreign government service, newspaper carriers who are minors.
- **Reciprocity:** no Ohio withholding for residents of {{oh.reciprocity.states}} working in Ohio [US-MULTI-005, US-OHP52-006]; resident credit via IT RC, none for wages from reciprocity states [US-OHP52-004].
- **School district income tax (ORC ch. 5748):** {{oh.pit.school_district.basis}}, even where the employer has no operations in the district [US-OH-002, US-OHS5-017]. Districts with the tax in 2026: {{oh.pit.school_district.count}}, of which {{oh.pit.school_district.earned_income_base.count}} on the earned-income-only base. Source list: {{oh.pit.school_district.full_list}} [US-OHB5-001].
- **Municipal income tax (ORC ch. 718), T4 layer.** Basis: {{oh.pit.municipal.basis}} [US-OHS5-013]. The employer withholds qualifying wages times the municipal rate and remits to the municipality or its collector [US-OHP52-003, US-OH-010]. Occasional-entrant rule: {{oh.pit.municipal.occasional_entrant_days}} days [US-OH-008]. Rates above {{oh.pit.municipal.rate_cap_without_vote}} % need voter approval [US-OHP7-001]. Rate source: {{oh.pit.municipal.rate_table}} [US-OHB5-002]; municipalities with a rate in force on 2026-11-01: {{oh.pit.municipal.count_in_force}}.

| Municipality | Rate | Register id |
|---|---|---|
| Columbus | {{oh.pit.municipal.columbus.rate}} % | US-OHB5-002 |
| Cleveland | {{oh.pit.municipal.cleveland.rate}} % | US-OHB5-002 |
| Cincinnati | {{oh.pit.municipal.cincinnati.rate}} % | US-OHB5-002 |
| Dayton | {{oh.pit.municipal.dayton.rate}} % | US-OHB5-002 |
| Toledo | {{oh.pit.municipal.toledo.rate}} % | US-OHB5-002 |
| Akron | {{oh.pit.municipal.akron.rate}} % | US-OHB5-002 |
| Youngstown | {{oh.pit.municipal.youngstown.rate}} % | US-OHB5-002 |

- **Resident and nonresident matrix.**

| Income type | Ohio resident | Nonresident |
|---|---|---|
| Regular salary | State withholding under the tables; school district tax if resident in a taxing district; municipal tax of the work location | State withholding under the same tables (5747.06 covers nonresidents), unless resident of a reciprocity state; municipal tax of the work location; no school district tax |
| Bonus / supplemental | Supplemental rate {{oh.wh.supplemental.rate}} % | Same, unless reciprocity applies |
| 401(k) deferrals | Excluded at state level (follows federal) | Same |
| Municipal base | Medicare wages less cafeteria-plan contributions: elective deferrals taxable | Same, at the work location |
| Severance, equity, benefits in kind | Follow federal wages at state level; municipal treatment of NQDC and stock options depends on the ordinance | Same, work-location sourcing |

## @social
- **Unemployment insurance (ODJFS rate year 2026) [US-OHS5-002, US-OH-005].** Taxable wage base {{oh.sui.wage_base}} USD. New employer {{oh.sui.new_employer.rate}} % (including the Technology and Customer Service Fee); construction new employer {{oh.ui.rate.new_employer.construction}} %. Experienced range, fee included: {{oh.ui.rate.min_total}} % to {{oh.ui.rate.max_total}} %. Technology and Customer Service Fee {{oh.ui.tcsf.rate}} % (ORC 4141.251) [US-OHP7-003]. Employee contribution {{oh.sui.employee.rate}} %.
- **No SDI, TDI or PFML** ({{oh.sdi_pfml.exists}} [US-OHV6B-001]) and no transit or workforce levy on wages [US-OHL-002].

## @payslip
- **Content (ORC 4113.14, Pay Stub Protection Act, effective 2025-04-09) [US-OHP51-001, US-OHL-001]:** a written or electronic statement every pay period: {{oh.payslip.items}}. No language clause; the SSN is not required.
- **Retention:** wage and hour records {{oh.records.wage_hour.retention_years}} years [US-OHS5-005]; withholding records per the ODT Filing Guidelines.

## @reporting
- **State withholding [US-OH-009].** IT 501 payments filed electronically. Frequency by look-back: quarterly up to {{oh.report.it501.quarterly_threshold}} USD; monthly above it; partial-weekly EFT at {{oh.report.it501.partial_weekly_threshold}} USD or more. Annual reconciliation IT 941 due {{oh.report.it941.due}}; W-2 upload through OH|TAX by the same date, with the school district code [US-OHS5-018].
- **School district:** SD 101 (periodic) and SD 141 (annual); bulk filing in FSET XML [US-FIL-012]; agent authorisation WT 8655 [US-FIL-011].
- **Municipal:** returns to each municipality or its collector under 718.03 thresholds; a municipality may require semimonthly remittance [US-OHP52-003, US-OH-010].
- **UI quarterly report (ORC 4141.20):** due {{oh.report.ui.quarterly_due}}; total and taxable remuneration, per-employee name, SSN, wages and weeks paid [US-OHS5-020]. Portal channel: open point below.
- **New hire (ORC 3121.891-.893):** to ODJFS within {{oh.newhire.report_days}} days; contractors are also reported; multistate employers may designate one state [US-OHS5-009, US-OHS5-014].
- **Representatives:** TBOR 1 [US-OHP52-005]; JFS-20106 for UI [US-OHR3-001].

## @leave
- **No state paid sick leave statute** (exists: {{oh.leave.sick.state_statute.exists}}); leave and fringe benefits are employer policy or agreement, and local mandates are preempted (ORC 4113.85) [US-OHS5-012]. No PFML. Other statutory leave with pay impact: open point below.

## @termination
- **Final pay:** {{oh.final_pay.rule}} [US-OHS5-015]. Accrued vacation and separation pay follow employer policy (4113.85) [US-OHS5-012].
- **Mass layoff (ORC 4141.28(C)):** for a mass layoff for lack of work, notify the director {{oh.term.mass_layoff.notice_working_days}} working days ahead and give each worker the eligibility information [US-OHS5-016]. No state WARN law; federal WARN applies. Individual separation notice: open point below.

## @bik
- **State tax** starts from federal AGI (ORC 5747.01(A), amended by SB 9 effective 2026-03-05); the add-backs read do not touch retirement deferrals, cafeteria plans, HSA, transit or group-term life, so the state follows the federal exclusions [US-OHS5-022].
- **Municipal tax departs from federal:** IRC 3121(a) wage base; elective deferrals taxable, cafeteria plans excluded; NQDC and stock options per pre-2016 ordinance [US-OHS5-013].
- **School district tax** follows the district base: traditional or earned income [US-OHS5-019].

## @deductions
- **Creditor garnishment (ORC 2329.66(A)(13)) [US-OHS5-011]:** the exempt amount is the greater of the CCPA percentage of disposable earnings or {{oh.garn.consumer.exempt_multiple_fmw.weekly}} times the federal minimum wage per week (with the corresponding multiples for longer pay periods). This matches the CCPA (Annex FED).
- **Child support IWO fee (ORC 3121.18):** the employer may deduct a fee of at least {{oh.garn.iwo.employer_fee.min}} USD per withholding, within the statutory percentage of the amount withheld [US-OHS5-010]. Start of withholding: {{oh.garn.deduction_rules_priority}} [US-OHV6-003].

## @cba
- **Prevailing wage (ORC ch. 4115):** rates set by the Director of Commerce (4115.04); new-construction threshold {{oh.prevailing_wage.threshold.new_construction}} USD, with other thresholds for remodelling and road work, adjusted biennially (4115.034) [US-OHR3-002, US-OHR3-003, US-OHP51-003]. Certified payroll: {{oh.prevailing_wage.certified_payroll}} [US-OHV6-002].

## @indexation
- **Minimum wage:** {{oh.minwage.indexation}} [US-OHS5-006]. The small-employer threshold uses the same index; the tipped wage is half the minimum wage. The 2026 and 2027 published values follow from the index (derivation in the research pack; values in Section 1).
- **SUI wage base:** {{oh.ui.wage_base.indexation}} [US-OHV6-001].
- **Withholding tables:** republished after a rate change (OAC 5703-7-10) [US-OHS5-017], hence the 2026-08-01 edition.
- **Prevailing-wage thresholds:** biennial (4115.034). **School district rates:** annual change list each January [US-OHS5-018].

## @data
- **Breach notice (ORC 1349.19):** to affected Ohio residents within {{oh.data.breach_notice.days}} days of discovery; personal information includes a name combined with an SSN or account number [US-OHS5-021]. No SSN-truncation rule for pay statements; 4113.14 does not require the SSN [US-OHP51-001].

## @live
- **HB 96:** flat statutory rate from tax year 2026 [US-OHS5-007]; municipal 718.01 amendments and 2329.66 amendments effective 2025-09-30 [US-OHP52-003, US-OHS5-011].
- **2026-01-01:** supplemental rule OAC 5703-7-10 [US-OHS5-017]; school district changes [US-OHS5-018].
- **2026-03-05:** ORC 5747.01 amended by SB 9 (substance not analysed) [US-OHS5-022].
- **2026-08-01:** new withholding tables and formula [US-OH-006, US-OHS5-001].
- **2027-01-01 (enacted):** minimum wage and tipped wage per Section 1 [US-OHS5-004]. Not yet published: 2027 withholding tables, ODJFS rates and school district changes (open point in Section 2).

## @special
| Population | Ohio rule | Register id |
|---|---|---|
| Domestic / household | No Ohio withholding on domestic service in a private home (5747.06(A)(2)); babysitters in the employer's home and live-in companions are exempt from the minimum wage | US-OHS5-008, US-OHS5-005 |
| Agricultural | No Ohio withholding on agricultural labour | US-OHS5-008 |
| Minors | Under 16: federal minimum wage; newspaper carriers who are minors: no withholding; Minor Labor Law (ORC 4109) not read | US-OHS5-005, US-OHS5-008 |
| Tipped | Cash wage per Section 1; tip credit up to the full minimum | US-OHS5-005, US-OHS5-004 |
| Clergy / religious | No state rule beyond federal located | US-OHS5-008, US-OHS5-022 |
| Students | No state withholding rule located; UI exclusions in 4141.01(B)(3) not read | - |
| Nonresident aliens | No state rule beyond federal; Ohio withholds on nonresidents generally | US-OHS5-008 |
| Statutory employees | No state rule beyond federal located | US-OHS5-022 |
| Government employees | State and political subdivisions must withhold (5747.06(A)); public employers are outside the 4113.85 definition | US-OHS5-008, US-OHS5-012, US-OHS5-005 |
| Reciprocity-state residents | No Ohio withholding (Section 2); nonresident military spouse: no withholding | US-MULTI-005, US-OHP52-006 |
| Small employers | Below the gross-receipts threshold: federal minimum wage | US-OHS5-005 |

## @gaps
- oh.ui.wage_base.indexation :: The SUI wage base is read as statutory and fixed (ORC 4141.01(G)); the text was not read. :: ORC 4141.01(G)(1) text.
