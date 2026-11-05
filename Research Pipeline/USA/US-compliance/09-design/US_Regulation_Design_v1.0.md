# US — United States Payroll — Regulation Design v1.0

**Country:** United States (US) · ISO 3166-1 numeric **840** · Currency **USD**  
**Tax year:** 2026; every value that changes with the year carries its own period (2027 values are labelled)  
**Regulation ID prefix:** `9840` (9 + ISO 840) · **Flag accounts:** `58401`–`58449` · **Calculation accounts:** `58501`–`58549`  
**Design basis:** `US-CCG-001 v1.0` (13 modules and the jurisdiction annexes), `US-WTC-001 v1.0`, `US-DD-001 v1.0`  
**Status:** For QA · **Package version:** 1.0

| Version | Issue date | Issued by | Status |
|---|---|---|---|
| 1.0 | 2027-03-31 | Wallisson Gomes | For QA |

**Scope.** Private-sector employers and common-law employees. Independent contractors paid on Form 1099-NEC are out of scope [US-OWN-008]. The layer covers federal employment taxes (income tax withholding, FICA, FUTA), State income tax withholding, State unemployment insurance, State-mandated payroll programmes, local taxes by flag and the minimum wage rate for the 50 States and the District of Columbia. Every special population accepted by the owner is in [US-OWN-005]; State-level rules for special populations are a scope statement deferred to a later release, not a gap.

**How to read the design.** Part 1 declares every flag with its values. Part 2 lists the accounts and the wage types they read or write. Part 3 gives the order of the regulations. Part 4 gives each regulation and the jurisdiction register they share. Part 5 gives the taxability matrix of the wage-type catalogue. Part 6 lists the open items, each with both readings where the design and the research differ; the research wins. Every rate, ceiling and threshold is written as a bound value; a value valid for a different period is written with that period. Annex section ids (for example `FED.2`, `UT.2`) name the section of `US-CCG-001 v1.0` that holds the table or rule.

---

## PART 0 — Special-category sweep

Two sweeps ran against the Configuration Guide: one on every row of the coverage matrix, one on every population the owner accepted. A category is *in core* when a flag and a regulation of this design implement it; *no branch* when the research shows no differential treatment; *by reference* when the rule lives in a jurisdiction annex.

| Category | Configuration Guide location | Disposition | Flags | Regulations |
|---|---|---|---|---|
| Resident employee | Module 3; Module 5; Module 6 | In core | 58404, 58415, 58416, 58420 | 9840021, 9840031, 9840032, 9840041, 9840051, 9840052 |
| Non-resident employee | Module 6 (NRA, reciprocity, thresholds); Module 11 | In core: two meanings kept apart (nonresident alien of the United States; employee working in or living in another State) | 58404, 58418, 58419, 58424 | 9840024, 9840031, 9840051 |
| Fixed-term contract | Module 9 | No branch: no federal or general State fixed-term payroll regime | none | none |
| Part-time | Module 4; Module 10 | No branch: no federal part-time payroll regime | none | none |
| Officers without employment contract | Module 11 | In core as ordinary employees: corporate officers are employees for payroll; State coverage exclusions are annex rules reported on the State return | 58405 | 9840021, 9840052 |
| Apprentices and trainees | Module 4; Module 11 | No branch; student employees are a separate flag | 58411 | 9840031, 9840032, 9840041 |
| Maternity, paternity and parental leave | Module 8; Module 5 | By reference: no federal paid leave; State programmes are in 9840053 | 58415, 58420 | 9840053 |
| Work accident and occupational disease | Module 5; Module 7 | By reference: State workers' compensation rows | 58415, 58420 | 9840053 |
| Termination and final pay | Module 9 | In core: final wages are paid wages; supplemental identification applies | 58413, 58414 | 9840022, 9840023 |
| Mid-month joiner and leaver | Module 2; Module 3 | No branch: no proration rule; withholding follows the wages paid | none | none |
| Annual regularisation | Module 10; Module 5 | No branch: no employer year-end regularisation; accumulators follow the payment year | 58420 | 9840031, 9840041 |
| Overtime | Module 4; Module 10 | In core as earnings; the qualified overtime premium is reported only; the minimum wage regulation reads the hours | none | 9840011, 9840071 |
| Multiple employers | Module 3; Module 5 | In core: every wage base and accumulator is kept per employer entity | 58420 | 9840031, 9840032, 9840041 |
| Local regimes | Module 6 (local); annexes PA, OH, MI, IN, MD, KY, NY, OR | In core by flag: locality fields of the Data Dictionary select the local rows | 58431, 58432, 58433, 58434, 58435, 58436, 58437, 58438, 58439, 58440 | 9840061 |
| Employer type and size | Module 10; Module 11 | By reference: coverage thresholds sit in the programme parameters; health-coverage reporting is outside the calculation | 58415, 58420 | 9840053 |
| Mid-year rate change | Module 4; Module 6; Module 13 | In core: dated values selected by the payment date, the date earned (Massachusetts paid family and medical leave only) or the date the hours were worked | 58420, 58421, 58428 | 9840031, 9840051, 9840053, 9840071 |
| Special pay cycles | Module 3; Module 6 | In core: pay periods per year from the pay frequency | 58422 | 9840021 |
| Accrual versus payment | Module 3; Module 5 | In core: federal taxes and State programmes follow the payment date; Massachusetts paid family and medical leave follows the date earned | 58420, 58428 | 9840021, 9840031, 9840053 |

**Populations accepted by the owner** [US-OWN-005].

| Population | Flag | Regulations | Wage types | Rule carried by the research |
|---|---|---|---|---|
| Ordinary common-law employee | 58405 = 1 | 9840021, 9840031, 9840032, 9840041, 9840051 | `US-001`, `US-006` | Default path of the design. |
| Nonresident alien | 58404 = 1, 58424 | 9840024, 9840021, 9840031 | `US-004`, `US-033`, `US-029` | Single schedule whatever the marital status; cannot claim exempt; wage add-on added before the table; F-1, J-1, M-1 and Q-1 pay for the purpose of admission is exempt from FICA. [US-FEDS5-015] [US-FEDR2-001] |
| Statutory employee | 58406 = 1, 58427 | 9840021, 9840031, 9840041 | `US-035` | FICA withheld, no income tax withholding, FUTA for drivers and traveling salespersons only. [US-FEDR3-005] |
| Household employee | 58407 = 1 | 9840021, 9840031, 9840041 | `US-028` | Income tax withholding only by agreement; FICA and FUTA from the cash-wage thresholds. [US-FEDS5-029] |
| Agricultural employee | 58408 = 1 | 9840031, 9840041 | `US-036` | Own thresholds. [US-FEDR3-006] |
| Clergy | 58409 = 1 | 9840021, 9840031, 9840032 | `US-034` | No withholding for income tax, social security or Medicare. [US-FED-030] |
| Employee abroad | 58405 = 7 | 9840021 | `US-001` | Withheld normally in package 1.0; the statement that stops withholding is a named limitation. [US-FEDR3-007] |
| Student employee | 58411 = 1 | 9840031, 9840032, 9840041 | `US-038` | Private school or college student: income tax withheld, FICA and FUTA exempt. [US-FEDS5-029] |
| Election worker | 58430 = 1 | 9840031, 9840032 | `US-001` | FICA applies from the annual threshold. [US-FEDS5-003] |

Populations in detail (values as carried by the research):

- **Statutory employee:** [[FACT:fed.statutory_employee.treatment=FICA withheld, no FIT withholding; W-2 box 13 checked; FUTA for drivers and traveling salespersons only]] [US-FEDR3-005]
- **Household employee, federal income tax:** [[FACT:fed.household.fit.withholding=only by agreement]] [US-FEDS5-029]
- **Clergy:** [[FACT:fed.minister.withholding=No FIT, social security or Medicare withholding (SE tax; voluntary FIT withholding agreement allowed); parsonage allowance excluded from W-2 box 1]] [US-FED-030]
- **Student employee:** [[FACT:fed.students.treatment=Private school/college students: FIT withheld, FICA and FUTA exempt; public school: FICA exempt unless sec. 218 agreement; work-experience full-time student: FICA taxable]] [US-FEDS5-029]
- **Employee abroad (citizen):** [[FACT:fed.citizen_abroad.form673=Employer may stop FIT withholding on Form 673 statement (FEIE/housing); citizens only]] [US-FEDR3-007]
- **Nonresident alien visa exemption:** [[FACT:fed.fica.nra.fjmq_exempt.scope=Exempt: pay of a nonresident alien in F-1, J-1, M-1 or Q status for services that carry out the purpose of admission, on or off campus, including authorized Curricular and Optional Practical Training. Not exempt: other employment of the same person (e.g. an unrelated part-time job), and any pay once the person is a resident alien.]] [US-FEDS5-016]
- **Household employee thresholds:** cash wages USD [[FACT:fed.household.fica_cash_threshold=3,000]] a year for FICA; FUTA from USD [[FACT:fed.household.futa_quarter_threshold=1,000]] in a quarter [US-FEDS5-029]
- **Agricultural employee thresholds:** USD [[FACT:fed.agricultural.per_worker_threshold=150]] per worker or USD [[FACT:fed.agricultural.total_threshold=2,500]] in total; FUTA from USD [[FACT:fed.agricultural.futa_quarter_threshold=20,000]] in a quarter [US-FEDR3-006]
- **Employee abroad:** foreign earned income exclusion USD [[FACT:fed.feie.amount=132,900]] for 2026 [US-FED-025]
- **Nonresident alien commercial traveler:** up to [[FACT:fed.fit.nra.commercial_traveler.max_days=90]] days and USD [[FACT:fed.fit.nra.commercial_traveler.max_pay=3,000]] of pay [US-FEDS5-016]
- **Election workers:** FICA applies from USD [[FACT:fed.election_worker.fica_threshold=2,500]] a year [US-FEDS5-003]

**Population rules at State level.**

- [[FACT:special_population.agricultural.al=AL does not follow federal withholding on agricultural cash wages]] [US-ALS5-001]
- [[FACT:special_population.household.state_withholding=not required in MO, MA (by agreement); HI requires on domestic/agricultural]] [US-MOS5-001]
- [[FACT:special_population.minister.ms_or=ministers excluded from MS and OR withholding]] [US-MSS5-004]
- [[FACT:special_population.wa_cares.niv_exempt=non-immigrant work visa holders auto-exempt from WA Cares from 2026-01-01 unless they opt in in writing]] [US-WAS5-024]

State-level rules for the remaining populations are deferred by owner decision [US-OWN-005]. They are a scope statement of this release.

**Fallback for the two populations not configured in package 1.0.** An employee first paid before 2020 who has no 2020 or later Form W-4 is handled manually: the payroll operator enters the withholding, and the engine does not run the employee silently on the 2020 method (Not configured in this release [[GAP:DESIGN-RQ-02]]). A citizen abroad who holds a Form 673 statement is withheld normally, as an ordinary employee (Not configured in this release [[GAP:DESIGN-RQ-05]]). Both are carried to version 1.1 of the Data Dictionary as a change request.

---

## PART 1 — Flags and HR fields

> The engine reads numbers only; string interpretation lives in flags only, never inside a regulation. Each flag lists its values; every gate in Part 4 compares a flag against one of its declared values, and every flag with values is used by at least one gate (a **[SOURCE]** flag is the origin of other flags; a USPS-code flag is a lookup key). A definition written `DD:` names a field of the Data Dictionary; a wage-type code is written in backticks.

| Account | Flag name | Definition | Values |
|---|---|---|---|
| 58401 | Filing status | DD:`Form W-4 filing status (Step 1(c))` (option code J, S or H) **[DERIVED]** | 1 = married filing jointly or qualifying surviving spouse, 2 = single or married filing separately, 3 = head of household |
| 58402 | Multiple jobs box (Step 2) | DD:`Form W-4 multiple jobs or spouse works (Step 2)` **[DERIVED]** | 1 = box checked (Step-2 schedule), 2 = not checked (standard schedule) |
| 58403 | Exempt from withholding | DD:`Form W-4 exempt from withholding` **[DERIVED]** | 1 = exempt certificate in force, 2 = not exempt |
| 58404 | Nonresident alien | `US-033`; DD:`Nonresident alien flag` **[DERIVED]** | 1 = nonresident alien, 2 = not |
| 58405 | Employee category | DD:`Employee special population category` (option code ORD, NRA, STAT, HH, AG, CLG, ABR) **[SOURCE]** | 1 = ordinary, 2 = nonresident alien, 3 = statutory employee, 4 = household, 5 = agricultural, 6 = clergy, 7 = employee abroad |
| 58406 | Statutory employee | `US-035`; from 58405 **[DERIVED]** | 1 = statutory employee, 2 = not |
| 58407 | Household employee | `US-028`; from 58405 **[DERIVED]** | 1 = household employee, 2 = not |
| 58408 | Agricultural employee | `US-036`; from 58405 **[DERIVED]** | 1 = agricultural employee, 2 = not |
| 58409 | Clergy | `US-034`; from 58405 **[DERIVED]** | 1 = minister of religion, 2 = not |
| 58411 | Student employee (exempt case) | `US-038` **[DERIVED]** | 1 = student employee whose wages are exempt from FICA and FUTA, 2 = not |
| 58413 | Supplemental wage payment | earning wage type with Special Tax = Yes, or Yes-No resolved as separately identified **[DERIVED]** | 1 = supplemental wages, 2 = regular wages |
| 58414 | Supplemental withholding method | `IF(EQUALS($58403;1);2;DD:`Supplemental wage withholding method election`)`, with the default of the note below **[DERIVED]** | 1 = optional flat rate, 2 = aggregate method |
| 58415 | Work State | DD:`Work State` **[DERIVED]** | USPS code of the jurisdiction register in Part 4 |
| 58416 | Residence State | DD:`Residence State` **[DERIVED]** | USPS code of the jurisdiction register in Part 4 |
| 58417 | Unemployment insurance State | `US-041`; DD:`Unemployment insurance State` **[DERIVED]** | USPS code of the jurisdiction register in Part 4 |
| 58418 | State withholding mode | from 58415, 58416 and 58419 **[DERIVED]** | 1 = work State only, 2 = work State and residence State, 3 = reciprocity: work State does not withhold, residence State does |
| 58419 | Reciprocity certificate on file | DD:`State withholding certificate on file` **[DERIVED]** | 1 = certificate on file, 2 = none |
| 58420 | Payment-year rule set | `IF(LESS(DATE_FORMAT($period.payment_date;'yyyyMMdd');'20270101');1;2)` **[DERIVED]** | 1 = 2026 rule set, 2 = 2027 rule set |
| 58421 | Utah table period | `IF(LESS(DATE_FORMAT($period.payment_date;'yyyyMMdd');'20260401');1;2)` **[DERIVED]** | 1 = payment date before 2026-04-01, 2 = from 2026-04-01 |
| 58422 | Pay periods per year | DD:`Pay frequency` **[DERIVED]** | numeric: the count of pay periods of the pay frequency, see 9840021 |
| 58424 | Nonresident alien visa exemption | DD:`Nonresident alien visa class` and DD:`Work carries out the purpose of admission` **[DERIVED]** | 1 = F-1, J-1, M-1 or Q-1 pay for the purpose of admission, 2 = not |
| 58425 | Totalization FICA exemption | DD:`Totalization agreement FICA exemption` **[DERIVED]** | 1 = exempt under an agreement, 2 = not |
| 58426 | Washington Cares exemption | DD:`Washington Cares exemption status` **[DERIVED]** | 1 = exempt, 2 = not |
| 58427 | Statutory employee liable to FUTA | DD:`Occupation` (driver or traveling salesperson) **[DERIVED]** | 1 = driver or traveling salesperson, 2 = other |
| 58428 | Earned-year rule set (Massachusetts paid family and medical leave) | `IF(LESS(DATE_FORMAT($period.earned_date;'yyyyMMdd');'20270101');1;2)` **[DERIVED]** | 1 = wages earned in 2026, 2 = wages earned from 2027 |
| 58429 | State-assigned UI rate on file | `IF(IS_NULL(DD:`State-assigned unemployment insurance rate`);2;1)` **[DERIVED]** | 1 = assigned rate on file, 2 = none: the new-employer rate applies |
| 58430 | Election worker | DD:`Occupation` (election official or election worker) **[DERIVED]** | 1 = election worker, 2 = not |
| 58431 | New York City or Yonkers resident | DD:`New York City or Yonkers residence status` **[DERIVED]** | 1 = New York City resident, 2 = Yonkers resident, 3 = neither |
| 58432 | Ohio municipality | DD:`Ohio municipality of work` **[DERIVED]** | 1 = municipality of work or residence given, 2 = none |
| 58433 | Pennsylvania political subdivision | DD:`Pennsylvania PSD code of the work location` **[DERIVED]** | 1 = PSD code given, 2 = none |
| 58434 | Indiana county | DD:`Indiana county of residence on January 1` **[DERIVED]** | 1 = county given, 2 = none |
| 58435 | Maryland county | DD:`Maryland county of residence` **[DERIVED]** | 1 = county given, 2 = none |
| 58436 | Kentucky locality | DD:`Kentucky locality of work` **[DERIVED]** | 1 = locality given, 2 = none |
| 58437 | Oregon Metro or Multnomah | DD:`Oregon Metro SHS or Multnomah PFA work location` **[DERIVED]** | 1 = location given, 2 = none |
| 58438 | Michigan city | DD:`Michigan city of residence or predominant place of employment` **[DERIVED]** | 1 = city given, 2 = none |
| 58439 | Denver occupational privilege tax | DD:`Denver occupational privilege tax work location` **[DERIVED]** | 1 = Denver work location, 2 = none |
| 58440 | Iowa school district | DD:`Iowa school district of residence` **[DERIVED]** | 1 = district given, 2 = none |

**Note on 58420, 58421 and 58428.** Federal taxes and State programmes follow the payment date, so the rule set is chosen by the payment date and not by the period worked. 58421 selects the Utah withholding table; the Utah table of the earlier period is Not configured in this release [[GAP:DESIGN-RQ-01]]. Only the Massachusetts paid family and medical leave rates follow the date the wages were earned (58428): [[FACT:ma.pfml.rate.selection_basis=The new contribution rate applies to wages earned on or after January 1 of each year; rates are set annually for January 1-December 31]] [US-MAS5-012] For the other programmes with a 2027 change the paid or earned basis is not established: Not configured in this release [[GAP:DESIGN-RQ-09]]; they use the payment date (58420).

**Note on 58413 and 58414.** A payment identified separately from regular wages takes the supplemental path of 9840022 and 9840023. The payer elects the method in the legal-entity field above; the default when the field is blank is the aggregate method when no income tax was withheld from regular wages in the current or the preceding year, and the flat rate otherwise: [[FACT:fed.fit.supplemental.aggregate_method=Supplemental wages identified separately, income tax withheld from regular wages in the current or preceding year: either flat 22% or aggregate - add the supplemental wages to the concurrently paid regular wages (or, if none, to the regular wages of the current or preceding payroll period), figure the tax as if one regular-period payment, subtract the tax withheld or to be withheld from the regular wages, withhold the remainder; earlier supplemental payments of the same period are aggregated too. No income tax withheld from regular wages in the current or preceding year: aggregate method only. Supplemental wages paid with regular wages without specifying each amount: withhold on the total as one regular payment.]] [US-FEDQ1-002].

**Note on 58422.** The pay periods per year are [[FACT:fed.fit.pay_periods_per_year=2 / 4 / 12 / 24 / 26 / 52 / 260 (semiannual, quarterly, monthly, semimonthly, biweekly, weekly, daily)]] [US-FEDS5-001].

**Note on 58429.** The assigned rate is entered per State account and year in DD:`State-assigned unemployment insurance rate`; the way each State notifies the rate is a named limitation [[GAP:DD-RQ-11]].

---

## PART 2 — Account register

Accounts `58501` onwards hold bases, intermediates and results. The wage-type code is the row of `US-WTC-001` that carries the account in the pay run; an account with no catalogue row is an engine intermediate.

| Account | Type | Regulation | Wage type | Meaning |
|---|---|---|---|---|
| 58501 | Base | 9840011 | `US-011` | Federal income tax wages of regular wages (accumulator) |
| 58502 | Base | 9840011 | `US-012` | Social security wages, capped accumulator |
| 58503 | Base | 9840011 | `US-014` | Medicare wages and tips, uncapped accumulator |
| 58504 | Base | 9840011 | `US-015` | Wages subject to Additional Medicare Tax withholding |
| 58505 | Base | 9840011 | `US-019` | FUTA taxable wages |
| 58522 | Intermediate | 9840011 | none | Supplemental wages of the payment (earning lines with 58413 = 1) |
| 58523 | Intermediate | 9840011 | none | Supplemental wages of the year, accumulator |
| 58525 | Intermediate | 9840011 | none | State income tax wages (Part 5 State column) |
| 58506 | Intermediate | 9840024 | `US-004` | Nonresident alien wage add-on |
| 58507 | Result | 9840021 | `US-001` | Federal income tax withheld, regular wages |
| 58508 | Result | 9840022 | `US-002` | Federal income tax, supplemental wages at the optional flat rate |
| 58524 | Result | 9840022 | `US-001` | Federal income tax, supplemental wages by the aggregate method |
| 58509 | Result | 9840023 | `US-003` | Federal income tax, supplemental wages above the mandatory threshold |
| 58510 | Result | 9840031 | WTC `21900` | Social security tax, employee |
| 58511 | Result | 9840031 | `US-005` | Social security tax, employer |
| 58512 | Result | 9840032 | `US-006` | Medicare tax, employee |
| 58513 | Result | 9840032 | `US-007` | Medicare tax, employer |
| 58514 | Result | 9840032 | `US-008` | Additional Medicare Tax, employee |
| 58515 | Result | 9840041 | `US-009` | FUTA, employer |
| 58516 | Result | 9840041 | `US-010` | FUTA credit reduction, employer |
| 58517 | Result | 9840051 | `US-074` to `US-115` | State income tax withheld, row of the work State |
| 58527 | Result | 9840051 | `US-074` to `US-115` | State income tax withheld, row of the residence State |
| 58518 | Result | 9840052 | `US-116` to `US-166` | State unemployment insurance, employer (one row per State) |
| 58519 | Result | 9840052 | `US-167` to `US-169` | State unemployment insurance, employee |
| 58520 | Result | 9840053 | `US-170` to `US-203`, `US-205` to `US-210` | State programmes, employee and employer |
| 58521 | Result | 9840061 | `US-211` to `US-233` | Local taxes |
| 58526 | Result | 9840071 | none | Applicable minimum hourly rate |

`US-204` (Illinois Secure Choice) is an elective employee deduction, not a State programme tax; it is outside 9840053.

---

## PART 3 — Regulation sequence

Regulations run in this order for each payment. A regulation reads only accounts written by an earlier one.

| Order | Regulation | Name | Reads | Writes |
|---|---|---|---|---|
| 1 | 9840011 | Federal and State wage bases | earning lines and their wage-type flags, 58413 | 58501–58505, 58522, 58523, 58525 |
| 2 | 9840024 | Nonresident alien add-on | 58501, 58404, 58422 | 58506 |
| 3 | 9840021 | Federal income tax, regular wages | 58501, 58506 | 58507 |
| 4 | 9840022 | Federal income tax, supplemental wages (flat rate and aggregate method) | 58501, 58507, 58522, 58523, 58414 | 58508, 58524 |
| 5 | 9840023 | Federal income tax, supplemental wages above the mandatory threshold | 58522, 58523 | 58509 |
| 6 | 9840031 | Social security tax | 58502, 58420 | 58510, 58511 |
| 7 | 9840032 | Medicare and Additional Medicare tax | 58503, 58504 | 58512–58514 |
| 8 | 9840041 | FUTA and credit reduction | 58505, 58417 | 58515, 58516 |
| 9 | 9840051 | State income tax withholding | 58525, 58507–58509, 58524, 58415–58419, 58421 | 58517, 58527 |
| 10 | 9840052 | State unemployment insurance | 58417, 58420, 58429 | 58518, 58519 |
| 11 | 9840053 | State programmes | 58415, 58420, 58426, 58428 | 58520 |
| 12 | 9840061 | Local taxes | 58431–58440 | 58521 |
| 13 | 9840071 | Minimum wage rate | 58415, hours with their work date | 58526 |

---

## PART 4 — Regulation detail

Amounts are rounded half-up to the cent between lines unless a State annex of the Configuration Guide sets another rule; full precision is carried between lines. A contribution or tax with an annual maximum is always the lesser of the remaining annual maximum and the rate times the period base; no annualise-then-divide shortcut is used.

### 9840011 — Federal and State wage bases

Reads the earning lines. Each earning wage type carries the flags Subject to Tax, Q1 (OASDI), Q2 (Medicare), Q3 (FUTA) and State income tax in `US-WTC-001`; where a flag is Yes-No the explanation of the row decides, and Part 5 lists every row. Accumulators: `US-011` (58501), `US-012` (58502), `US-014` (58503), `US-015` (58504), `US-019` (58505). Separately identified supplemental wages (58413 = 1) are kept out of 58501 and held in 58522, so the same wages are never withheld on twice. Configuration Guide section `FED.2`.

```
58501 = SUM(IF(EQUALS($58413;2); wages of earnings with Subject to Tax = Yes; 0)) - pre-tax deductions that reduce income tax wages
58522 = SUM(IF(EQUALS($58413;1); wages of earnings with Subject to Tax = Yes; 0))
58523 = 58523_ytd_before + 58522
58502 = SUM(earnings with Q1 = Yes) - pre-tax deductions that reduce FICA wages
58503 = SUM(earnings with Q2 = Yes) - pre-tax deductions that reduce FICA wages
58504 = 58503 year to date, above the Additional Medicare threshold
58505 = SUM(earnings with Q3 = Yes) - payments exempt from FUTA
58525 = SUM(earnings with State income tax = Yes) - deductions the State allows
```

Debit `58501`, `58502`, `58503`, `58504`, `58505`, `58522`, `58523`, `58525`.

### 9840024 — Nonresident alien add-on

Reads `$58501` and the flags 58404 and 58422. The add-on is added to the period wages before the schedule is read [US-FEDS5-002]. A flat-rate supplemental payment is withheld at the flat rate alone. Configuration Guide section `FED.2b`.

```
58506 = IF(EQUALS($58404;1); NRA_ADDON_TABLE2(58422); 0)
```

Add-on amounts per pay period for Table 1 and Table 2, in USD:

| Pay period | Table 1 | Table 2 |
|---|---|---|
| Weekly | [[FACT:fed.fit.nra.addon.table1.weekly=226.90]] | [[FACT:fed.fit.nra.addon.table2.weekly=309.60]] |
| Biweekly | [[FACT:fed.fit.nra.addon.table1.biweekly=453.80]] | [[FACT:fed.fit.nra.addon.table2.biweekly=619.20]] |
| Semimonthly | [[FACT:fed.fit.nra.addon.table1.semimonthly=491.70]] | [[FACT:fed.fit.nra.addon.table2.semimonthly=670.80]] |
| Monthly | [[FACT:fed.fit.nra.addon.table1.monthly=983.30]] | [[FACT:fed.fit.nra.addon.table2.monthly=1,341.70]] |
| Quarterly | [[FACT:fed.fit.nra.addon.table1.quarterly=2,950]] | [[FACT:fed.fit.nra.addon.table2.quarterly=4,025]] |
| Semiannual | [[FACT:fed.fit.nra.addon.table1.semiannual=5,900]] | [[FACT:fed.fit.nra.addon.table2.semiannual=8,050]] |
| Annual | [[FACT:fed.fit.nra.addon.table1.annual=11,800]] | [[FACT:fed.fit.nra.addon.table2.annual=16,100]] |
| Daily | [[FACT:fed.fit.nra.addon.table1.daily=45.40]] | [[FACT:fed.fit.nra.addon.table2.daily=61.90]] |

Table 1 applies to an employee whose Form W-4 predates the 2020 revision: Not configured in this release [[GAP:DESIGN-RQ-02]]; the fallback is manual handling (Part 0). The nonresident alien Form W-4 rule: [[FACT:fed.fit.nra.w4_rule=Single/MFS, write NRA below 4(c), cannot claim exempt]] [US-FEDS5-015].

Debit `58506`.

### 9840021 — Federal income tax, regular wages

Method: [[FACT:fed.fit.method=IRS Pub. 15-T (2026) Worksheet 1A with the Annual Percentage Method tables (STANDARD schedule; Step-2-checked schedule when W-4 Step 2 box checked)]] [US-FEDS5-001]. Configuration Guide section `FED.2`. Reads `$58501` and `$58506`; flags 58401, 58402, 58403, 58406, 58407, 58409, 58422.

```
pay_periods   = 58422
annual_wages  = (58501 + 58506) x pay_periods + DD:`Form W-4 other income (Step 4(a))`
line_1g       = IF(EQUALS($58402;1); 0; IF(EQUALS($58401;1); [[FACT:fed.fit.worksheet1a.line1g.mfj=12,900]]; [[FACT:fed.fit.worksheet1a.line1g.other=8,600]]))
adjusted      = MAX(0; annual_wages - DD:`Form W-4 deductions (Step 4(b))` - line_1g)
row           = last row of the schedule with floor <= adjusted
tentative     = cumulative_tax(row) + (adjusted - floor(row)) x rate(row)
credit        = DD:`Form W-4 dependents and other credits (Step 3)` / pay_periods
extra         = DD:`Form W-4 extra withholding (Step 4(c))`
58507         = IF(EQUALS($58403;1); 0;
                IF(EQUALS($58406;1); 0;
                IF(EQUALS($58409;1); 0;
                IF(EQUALS($58407;1); household_agreement_amount;
                MAX(0; tentative / pay_periods - credit) + extra))))
```

Schedule: the standard schedule when 58402 = 2, the Step-2 schedule when 58402 = 1. A household employee is withheld only under an agreement [US-FEDS5-029], using DD:`Household employee: federal income tax withholding agreement`. An employee without a certificate: [[FACT:fed.w4.default_no_certificate=Single or Married filing separately in Step 1(c), no entries in Step 2, Step 3 or Step 4 of the 2026 Form W-4]] [US-FEDQ3-004]. The exempt certificate: [[FACT:fed.w4.exempt.validity=2026 only: the exemption checkbox certification lapses; a new W-4 is required for 2027]] [US-FEDS5-006].

Debit `58507`.

**Standard schedule** (58402 = 2), annual percentage method, 2026. Floor and cumulative tax in USD; rate in percent [US-FEDS5-001].

| Row | MFJ floor | MFJ rate | MFJ cumulative | Single/MFS floor | Single/MFS rate | Single/MFS cumulative | HoH floor | HoH rate | HoH cumulative |
|---|---|---|---|---|---|---|---|---|---|
| 1 | [[FACT:fed.fit.standard.mfj.bracket.1.floor=0]] | [[FACT:fed.fit.standard.mfj.bracket.1.rate=0]]% | [[FACT:fed.fit.standard.mfj.bracket.1.cumulative_tax=0]] | [[FACT:fed.fit.standard.single.bracket.1.floor=0]] | [[FACT:fed.fit.standard.single.bracket.1.rate=0]]% | [[FACT:fed.fit.standard.single.bracket.1.cumulative_tax=0]] | [[FACT:fed.fit.standard.hoh.bracket.1.floor=0]] | [[FACT:fed.fit.standard.hoh.bracket.1.rate=0]]% | [[FACT:fed.fit.standard.hoh.bracket.1.cumulative_tax=0]] |
| 2 | [[FACT:fed.fit.standard.mfj.bracket.2.floor=19,300]] | [[FACT:fed.fit.standard.mfj.bracket.2.rate=10]]% | [[FACT:fed.fit.standard.mfj.bracket.2.cumulative_tax=0]] | [[FACT:fed.fit.standard.single.bracket.2.floor=7,500]] | [[FACT:fed.fit.standard.single.bracket.2.rate=10]]% | [[FACT:fed.fit.standard.single.bracket.2.cumulative_tax=0]] | [[FACT:fed.fit.standard.hoh.bracket.2.floor=15,550]] | [[FACT:fed.fit.standard.hoh.bracket.2.rate=10]]% | [[FACT:fed.fit.standard.hoh.bracket.2.cumulative_tax=0]] |
| 3 | [[FACT:fed.fit.standard.mfj.bracket.3.floor=44,100]] | [[FACT:fed.fit.standard.mfj.bracket.3.rate=12]]% | [[FACT:fed.fit.standard.mfj.bracket.3.cumulative_tax=2,480]] | [[FACT:fed.fit.standard.single.bracket.3.floor=19,900]] | [[FACT:fed.fit.standard.single.bracket.3.rate=12]]% | [[FACT:fed.fit.standard.single.bracket.3.cumulative_tax=1,240]] | [[FACT:fed.fit.standard.hoh.bracket.3.floor=33,250]] | [[FACT:fed.fit.standard.hoh.bracket.3.rate=12]]% | [[FACT:fed.fit.standard.hoh.bracket.3.cumulative_tax=1,770]] |
| 4 | [[FACT:fed.fit.standard.mfj.bracket.4.floor=120,100]] | [[FACT:fed.fit.standard.mfj.bracket.4.rate=22]]% | [[FACT:fed.fit.standard.mfj.bracket.4.cumulative_tax=11,600]] | [[FACT:fed.fit.standard.single.bracket.4.floor=57,900]] | [[FACT:fed.fit.standard.single.bracket.4.rate=22]]% | [[FACT:fed.fit.standard.single.bracket.4.cumulative_tax=5,800]] | [[FACT:fed.fit.standard.hoh.bracket.4.floor=83,000]] | [[FACT:fed.fit.standard.hoh.bracket.4.rate=22]]% | [[FACT:fed.fit.standard.hoh.bracket.4.cumulative_tax=7,740]] |
| 5 | [[FACT:fed.fit.standard.mfj.bracket.5.floor=230,700]] | [[FACT:fed.fit.standard.mfj.bracket.5.rate=24]]% | [[FACT:fed.fit.standard.mfj.bracket.5.cumulative_tax=35,932]] | [[FACT:fed.fit.standard.single.bracket.5.floor=113,200]] | [[FACT:fed.fit.standard.single.bracket.5.rate=24]]% | [[FACT:fed.fit.standard.single.bracket.5.cumulative_tax=17,966]] | [[FACT:fed.fit.standard.hoh.bracket.5.floor=121,250]] | [[FACT:fed.fit.standard.hoh.bracket.5.rate=24]]% | [[FACT:fed.fit.standard.hoh.bracket.5.cumulative_tax=16,155]] |
| 6 | [[FACT:fed.fit.standard.mfj.bracket.6.floor=422,850]] | [[FACT:fed.fit.standard.mfj.bracket.6.rate=32]]% | [[FACT:fed.fit.standard.mfj.bracket.6.cumulative_tax=82,048]] | [[FACT:fed.fit.standard.single.bracket.6.floor=209,275]] | [[FACT:fed.fit.standard.single.bracket.6.rate=32]]% | [[FACT:fed.fit.standard.single.bracket.6.cumulative_tax=41,024]] | [[FACT:fed.fit.standard.hoh.bracket.6.floor=217,300]] | [[FACT:fed.fit.standard.hoh.bracket.6.rate=32]]% | [[FACT:fed.fit.standard.hoh.bracket.6.cumulative_tax=39,207]] |
| 7 | [[FACT:fed.fit.standard.mfj.bracket.7.floor=531,750]] | [[FACT:fed.fit.standard.mfj.bracket.7.rate=35]]% | [[FACT:fed.fit.standard.mfj.bracket.7.cumulative_tax=116,896]] | [[FACT:fed.fit.standard.single.bracket.7.floor=263,725]] | [[FACT:fed.fit.standard.single.bracket.7.rate=35]]% | [[FACT:fed.fit.standard.single.bracket.7.cumulative_tax=58,448]] | [[FACT:fed.fit.standard.hoh.bracket.7.floor=271,750]] | [[FACT:fed.fit.standard.hoh.bracket.7.rate=35]]% | [[FACT:fed.fit.standard.hoh.bracket.7.cumulative_tax=56,631]] |
| 8 | [[FACT:fed.fit.standard.mfj.bracket.8.floor=788,000]] | [[FACT:fed.fit.standard.mfj.bracket.8.rate=37]]% | [[FACT:fed.fit.standard.mfj.bracket.8.cumulative_tax=206,583.50]] | [[FACT:fed.fit.standard.single.bracket.8.floor=648,100]] | [[FACT:fed.fit.standard.single.bracket.8.rate=37]]% | [[FACT:fed.fit.standard.single.bracket.8.cumulative_tax=192,979.25]] | [[FACT:fed.fit.standard.hoh.bracket.8.floor=656,150]] | [[FACT:fed.fit.standard.hoh.bracket.8.rate=37]]% | [[FACT:fed.fit.standard.hoh.bracket.8.cumulative_tax=191,171]] |

**Step-2 schedule** (58402 = 1). The cumulative tax of a row is the standard formula applied to the rows above it [US-FEDS5-001].

| Row | MFJ floor | MFJ rate | Single/MFS floor | Single/MFS rate | HoH floor | HoH rate |
|---|---|---|---|---|---|---|
| 1 | [[FACT:fed.fit.step2.mfj.bracket.1.floor=0]] | [[FACT:fed.fit.step2.mfj.bracket.1.rate=0]]% | [[FACT:fed.fit.step2.single.bracket.1.floor=0]] | [[FACT:fed.fit.step2.single.bracket.1.rate=0]]% | [[FACT:fed.fit.step2.hoh.bracket.1.floor=0]] | [[FACT:fed.fit.step2.hoh.bracket.1.rate=0]]% |
| 2 | [[FACT:fed.fit.step2.mfj.bracket.2.floor=16,100]] | [[FACT:fed.fit.step2.mfj.bracket.2.rate=10]]% | [[FACT:fed.fit.step2.single.bracket.2.floor=8,050]] | [[FACT:fed.fit.step2.single.bracket.2.rate=10]]% | [[FACT:fed.fit.step2.hoh.bracket.2.floor=12,075]] | [[FACT:fed.fit.step2.hoh.bracket.2.rate=10]]% |
| 3 | [[FACT:fed.fit.step2.mfj.bracket.3.floor=28,500]] | [[FACT:fed.fit.step2.mfj.bracket.3.rate=12]]% | [[FACT:fed.fit.step2.single.bracket.3.floor=14,250]] | [[FACT:fed.fit.step2.single.bracket.3.rate=12]]% | [[FACT:fed.fit.step2.hoh.bracket.3.floor=20,925]] | [[FACT:fed.fit.step2.hoh.bracket.3.rate=12]]% |
| 4 | [[FACT:fed.fit.step2.mfj.bracket.4.floor=66,500]] | [[FACT:fed.fit.step2.mfj.bracket.4.rate=22]]% | [[FACT:fed.fit.step2.single.bracket.4.floor=33,250]] | [[FACT:fed.fit.step2.single.bracket.4.rate=22]]% | [[FACT:fed.fit.step2.hoh.bracket.4.floor=45,800]] | [[FACT:fed.fit.step2.hoh.bracket.4.rate=22]]% |
| 5 | [[FACT:fed.fit.step2.mfj.bracket.5.floor=121,800]] | [[FACT:fed.fit.step2.mfj.bracket.5.rate=24]]% | [[FACT:fed.fit.step2.single.bracket.5.floor=60,900]] | [[FACT:fed.fit.step2.single.bracket.5.rate=24]]% | [[FACT:fed.fit.step2.hoh.bracket.5.floor=64,925]] | [[FACT:fed.fit.step2.hoh.bracket.5.rate=24]]% |
| 6 | [[FACT:fed.fit.step2.mfj.bracket.6.floor=217,875]] | [[FACT:fed.fit.step2.mfj.bracket.6.rate=32]]% | [[FACT:fed.fit.step2.single.bracket.6.floor=108,938]] | [[FACT:fed.fit.step2.single.bracket.6.rate=32]]% | [[FACT:fed.fit.step2.hoh.bracket.6.floor=112,950]] | [[FACT:fed.fit.step2.hoh.bracket.6.rate=32]]% |
| 7 | [[FACT:fed.fit.step2.mfj.bracket.7.floor=272,325]] | [[FACT:fed.fit.step2.mfj.bracket.7.rate=35]]% | [[FACT:fed.fit.step2.single.bracket.7.floor=136,163]] | [[FACT:fed.fit.step2.single.bracket.7.rate=35]]% | [[FACT:fed.fit.step2.hoh.bracket.7.floor=140,175]] | [[FACT:fed.fit.step2.hoh.bracket.7.rate=35]]% |
| 8 | [[FACT:fed.fit.step2.mfj.bracket.8.floor=400,450]] | [[FACT:fed.fit.step2.mfj.bracket.8.rate=37]]% | [[FACT:fed.fit.step2.single.bracket.8.floor=328,350]] | [[FACT:fed.fit.step2.single.bracket.8.rate=37]]% | [[FACT:fed.fit.step2.hoh.bracket.8.floor=332,375]] | [[FACT:fed.fit.step2.hoh.bracket.8.rate=37]]% |

Before the 2026 revision the allowance method gave each allowance a value of USD [[FACT:fed.fit.allowance.pre2020_value=4,300]] [US-FEDS5-001]; the allowance method is Not configured in this release [[GAP:DESIGN-RQ-02]].

The 2026 schedule is held for payment dates in 2026; the 2027 schedule is Not configured in this release [[GAP:RQ-530]].

### 9840022 / 9840023 — Federal income tax, supplemental wages

Reads `$58501`, `$58507`, `$58522`, `$58523` and the flags 58403, 58406, 58409, 58414. [[FACT:fed.fit.supplemental.aggregate_method=Supplemental wages identified separately, income tax withheld from regular wages in the current or preceding year: either flat 22% or aggregate - add the supplemental wages to the concurrently paid regular wages (or, if none, to the regular wages of the current or preceding payroll period), figure the tax as if one regular-period payment, subtract the tax withheld or to be withheld from the regular wages, withhold the remainder; earlier supplemental payments of the same period are aggregated too. No income tax withheld from regular wages in the current or preceding year: aggregate method only. Supplemental wages paid with regular wages without specifying each amount: withhold on the total as one regular payment.]] [US-FEDQ1-002]. Configuration Guide section `FED.2`. The first USD [[FACT:fed.fit.supplemental.mandatory_threshold=1,000,000]] of supplemental wages in the year is withheld by the chosen method; only the part above it takes the mandatory rate, incrementally.

```
below   = MAX(0; MIN(58523; [[FACT:fed.fit.supplemental.mandatory_threshold=1,000,000]]) - MIN(58523_ytd_before; [[FACT:fed.fit.supplemental.mandatory_threshold=1,000,000]]))
excess  = MAX(0; 58523 - MAX([[FACT:fed.fit.supplemental.mandatory_threshold=1,000,000]]; 58523_ytd_before))
58508 = IF(EQUALS($58406;1); 0; IF(EQUALS($58409;1); 0; IF(EQUALS($58403;1); 0; IF(EQUALS($58414;1); ROUND([[FACT:fed.fit.supplemental.flat_rate=22]]% x below); 0))))
58524 = IF(EQUALS($58403;1); 0; IF(EQUALS($58406;1); 0; IF(EQUALS($58409;1); 0; IF(EQUALS($58414;2); MAX(0; FIT_SCHEDULE(58501 + below) - 58507); 0))))
58509 = IF(EQUALS($58406;1); 0; IF(EQUALS($58409;1); 0; ROUND([[FACT:fed.fit.supplemental.mandatory_rate=37]]% x excess)))
```

The optional flat rate is [[FACT:fed.fit.supplemental.flat_rate=22]]%; the mandatory rate is [[FACT:fed.fit.supplemental.mandatory_rate=37]]% on the part of the year's supplemental wages above USD [[FACT:fed.fit.supplemental.mandatory_threshold=1,000,000]] [US-FEDS5-003]. The aggregate method uses the schedule of 9840021 on the sum of the regular wages and the supplemental wages under the threshold, less the regular withholding already computed. An employee with an exempt certificate (58403 = 1) takes the aggregate method, which gives no withholding, but is still withheld at the mandatory rate on the excess. Backup withholding is separate at [[FACT:fed.fit.backup_withholding.rate=24]]% [US-FEDS5-003].

Debit `58508`, `58524`, `58509`.

### 9840031 — Social security tax (OASDI)

Reads `$58502` and the flags 58420, 58409, 58411, 58424, 58425, 58407, 58408, 58430. Employee row WTC `21900`; employer row `US-005`. The wage base applies per employer. When a threshold is crossed, every cash wage of the year becomes FICA wages: the period in which it is crossed carries the earlier year-to-date wages (catch_up), capped by the wage base. Configuration Guide section `FED.3`.

```
limit_2026 = [[FACT:fed.fica.oasdi.wage_base=184,500]]   (payment dates in 2026)
limit_2027 = [[FACT:fed.fica.oasdi.wage_base=192,300]]   (payment dates from 2027-01-01)
limit  = IF(EQUALS($58420;1); limit_2026; limit_2027)
fica_exempt = IF(EQUALS($58411;1); 1; IF(EQUALS($58424;1); 1; IF(EQUALS($58425;1); 1; IF(EQUALS($58409;1); 1; 0))))
below_threshold = IF(EQUALS($58407;1); household_cash_wages_ytd_after < household_threshold;
                  IF(EQUALS($58408;1); agricultural_wages_ytd_after < agricultural_thresholds;
                  IF(EQUALS($58430;1); election_wages_ytd_after < election_threshold; 0)))
catch_up = IF(below_threshold; 0; IF(threshold_crossed_in_this_period; wages_ytd_before_this_period; 0))
58510 = IF(fica_exempt = 1; 0; IF(below_threshold; 0; ROUND([[FACT:fed.fica.oasdi.rate.employee=6.2]]% x MIN(58502 + catch_up; MAX(0; limit - 58502_ytd)))))
58511 = IF(fica_exempt = 1; 0; IF(below_threshold; 0; ROUND([[FACT:fed.fica.oasdi.rate.employer=6.2]]% x MIN(58502 + catch_up; MAX(0; limit - 58502_ytd)))))
```

Social security base: USD [[FACT:fed.fica.oasdi.wage_base=184,500]] for 2026 (period 2026-01-01 to 2026-12-31) and USD [[FACT:fed.fica.oasdi.wage_base=192,300]] from 2027-01-01; employee and employer each at [[FACT:fed.fica.oasdi.rate.employee=6.2]]% [US-FEDS5-005]. A student employee (58411 = 1) is exempt from FICA [US-FEDS5-029]; an employee under a totalization agreement is exempt to the extent the agreement says so: [[FACT:fed.fica.totalization.exemption_rule=Wages are exempt from employee FICA (IRC 3101(c)) and employer FICA (IRC 3111(c)) while a section 233 Social Security Act agreement is in effect, to the extent the agreement makes them subject exclusively to the foreign social security system.]] [US-FEDR2-003]; a nonresident alien in F-1, J-1, M-1 or Q-1 status working for the purpose of admission is exempt [US-FEDR2-001]. Thresholds: household cash wages USD [[FACT:fed.household.fica_cash_threshold=3,000]] a year; agricultural wages USD [[FACT:fed.agricultural.per_worker_threshold=150]] per worker or USD [[FACT:fed.agricultural.total_threshold=2,500]] in total; election workers USD [[FACT:fed.election_worker.fica_threshold=2,500]] a year.

Debit `58510`, `58511`.

### 9840032 — Medicare tax and Additional Medicare Tax

Reads `$58503` and `$58504`, and the flags 58409, 58411, 58424, 58425, 58407, 58408, 58430 through `fica_exempt` and `below_threshold` of 9840031. The Medicare base has no annual cap. Employee row `US-006`; employer row `US-007`; Additional Medicare row `US-008`. Configuration Guide section `FED.3`.

```
58512 = IF(fica_exempt = 1; 0; IF(below_threshold; 0; ROUND([[FACT:fed.fica.medicare.rate.employee=1.45]]% x (58503 + catch_up))))
58513 = IF(fica_exempt = 1; 0; IF(below_threshold; 0; ROUND([[FACT:fed.fica.medicare.rate.employer=1.45]]% x (58503 + catch_up))))
58514 = IF(fica_exempt = 1; 0; IF(below_threshold; 0; ROUND([[FACT:fed.fica.addl_medicare.rate=0.9]]% x MAX(0; 58503_ytd_after - MAX([[FACT:fed.fica.addl_medicare.withholding_threshold=200,000]]; 58503_ytd_before)))))
```

Rates: employee [[FACT:fed.fica.medicare.rate.employee=1.45]]%, employer [[FACT:fed.fica.medicare.rate.employer=1.45]]%; Additional Medicare [[FACT:fed.fica.addl_medicare.rate=0.9]]% on wages above USD [[FACT:fed.fica.addl_medicare.withholding_threshold=200,000]] in the year, employee only [US-FEDS5-005]. Clergy (58409 = 1) are not withheld for Medicare or Additional Medicare.

Debit `58512`, `58513`, `58514`.

### 9840041 — FUTA and credit reduction

Reads `$58505` and the flags 58417, 58411, 58406, 58427, 58407, 58408. Rows `US-009` and `US-010`. Configuration Guide section `FED.3`.

```
net_rate = [[FACT:fed.futa.rate.net=0.6]]%
futa_exempt = IF(EQUALS($58411;1); 1; IF(EQUALS($58406;1); IF(EQUALS($58427;1); 0; 1); 0))
below_futa_threshold = IF(EQUALS($58407;1); NOT(any_quarter_of_current_or_preceding_year >= household_futa_threshold);
                       IF(EQUALS($58408;1); NOT(any_quarter_of_current_or_preceding_year >= agricultural_futa_threshold); 0))
futa_catch_up = IF(below_futa_threshold; 0; IF(liability_starts_in_this_period; futa_wages_ytd_before_this_period; 0))
58515 = IF(futa_exempt = 1; 0; IF(below_futa_threshold; 0; ROUND(net_rate x MIN(58505 + futa_catch_up; MAX(0; [[FACT:fed.futa.wage_base=7,000]] - 58505_ytd)))))
58516 = IF(futa_exempt = 1; 0; IF(below_futa_threshold; 0; ROUND(credit_reduction_rate(58417) x MIN(58505 + futa_catch_up; MAX(0; [[FACT:fed.futa.wage_base=7,000]] - 58505_ytd)))))
```

Gross rate [[FACT:fed.futa.rate.gross=6]]%, maximum credit [[FACT:fed.futa.credit.max=5.4]]%, net rate [[FACT:fed.futa.rate.net=0.6]]% on the first USD [[FACT:fed.futa.wage_base=7,000]] of each employee's wages [US-FED-007]. The quarterly deposit applies when the liability exceeds USD [[FACT:fed.futa.deposit_threshold=500]] [US-FEDS5-031]. Household FUTA liability starts when cash wages reach USD [[FACT:fed.household.futa_quarter_threshold=1,000]] in any calendar quarter of the current or the preceding year, and agricultural FUTA at USD [[FACT:fed.agricultural.futa_quarter_threshold=20,000]] in any such quarter; the wages of the year before the period of crossing are then caught up, up to the wage base. A statutory employee is liable only as a driver or traveling salesperson [US-FEDR3-005]. Credit reduction for California ([[FACT:fed.futa.credit_reduction.ca.potential.rate=5.3]]%) and the Virgin Islands ([[FACT:fed.futa.credit_reduction.vi.potential.rate=4.8]]%) is a potential rate for 2026: Not configured in this release [[GAP:RQ-402]] and Not configured in this release [[GAP:RQ-403]].

Debit `58515`, `58516`.

### Jurisdiction register (read by 9840051, 9840052, 9840053 and 9840071)

One row per State and the District of Columbia. *No wage tax* and *flat rate* come from the research; a flat rate is applied after the allowances, deductions or bands of the State annex, and the Massachusetts surtax is carried in its row. *Table or formula* means the State publishes tables or a formula. The *Annex* column names the section of the Configuration Guide that holds the rule (`.2` income tax withholding, `.3` unemployment insurance and payroll levies). Wage-base cells carry their own period.

| State | USPS | Annex | Withholding row | State income tax | UI employer row | UI wage base (USD) | New-employer rate | UI employee | Programme rows |
|---|---|---|---|---|---|---|---|---|---|
| Alaska | AK | AK.2 / AK.3 | none | No wage tax | US-116 | 2026-01-01 to 2026-12-31: [[FACT:ak.sui.wage_base=54,200]] | 2026-01-01 to 2026-12-31: [[FACT:ak.sui.new_employer.rate=1]]% | US-167 2026-01-01 to 2026-12-31: [[FACT:ak.sui.employee.rate=0.5]]% | none |
| Alabama | AL | AL.2 / AL.3 | US-074 | Table or formula | US-117 | from 2026-01-01: [[FACT:al.sui.wage_base=8,000]] | from 2026-01-01: [[FACT:al.sui.new_employer.rate=2.7]]% | none | none |
| Arkansas | AR | AR.2 / AR.3 | US-075 | Table or formula | US-118 | from 2026-01-01: [[FACT:ar.sui.wage_base=7,000]] | 2026-01-01 to 2026-12-31: [[FACT:ar.sui.new_employer.rate=2]]% | none | none |
| Arizona | AZ | AZ.2 / AZ.3 | US-076 | Table or formula | US-119 | from 2026-01-01: [[FACT:az.sui.wage_base=8,000]] | 2026-01-01 to 2026-12-31: [[FACT:az.sui.new_employer.rate=2]]% | none | none |
| California | CA | CA.2 / CA.3 | US-077 | Table or formula | US-120 | from 2026-01-01: [[FACT:ca.sui.wage_base=7,000]] | from 2026-01-01: [[FACT:ca.sui.new_employer.rate=3.4]]% | none | US-170 |
| Colorado | CO | CO.2 / CO.3 | US-078 | Flat rate 2026-01-01 to 2026-12-31: [[FACT:co.pit.rate.flat=4.4]]%, after the State's allowances, deductions or bands | US-121 | 2026-01-01 to 2026-12-31: [[FACT:co.sui.wage_base=30,600]]; from 2027-01-01: [[FACT:co.sui.wage_base=32,100]] | Not configured in this release [[GAP:DESIGN-RQ-06]] | none | US-171, US-172 |
| Connecticut | CT | CT.2 / CT.3 | US-079 | Table or formula | US-122 | 2026-01-01 to 2026-12-31: [[FACT:ct.sui.wage_base=27,000]] | 2026-01-01 to 2026-12-31: [[FACT:ct.sui.new_employer.rate=1.9]]% | none | US-173 |
| District of Columbia | DC | DC.2 / DC.3 | US-080 | Table or formula | US-123 | from 2026-01-01: [[FACT:dc.sui.wage_base=9,000]] | from 2026-01-01: [[FACT:dc.sui.new_employer.rate=2.7]]% | none | US-174 |
| Delaware | DE | DE.2 / DE.3 | US-081 | Table or formula | US-124 | 2026-01-01 to 2026-12-31: [[FACT:de.sui.wage_base=14,500]]; from 2027-01-01: [[FACT:de.sui.wage_base=16,500]] | 2026-01-01 to 2026-12-31: [[FACT:de.sui.new_employer.rate=1]]% | none | US-175, US-176 |
| Florida | FL | FL.2 / FL.3 | none | No wage tax | US-125 | from 2015-01-01: [[FACT:fl.sui.wage_base=7,000]] | from 2026-01-01: [[FACT:fl.sui.new_employer.rate=2.7]]% | none | none |
| Georgia | GA | GA.2 / GA.3 | US-082 | Flat rate from 2026-01-01: [[FACT:ga.pit.rate.flat=4.99]]%, after the State's allowances, deductions or bands | US-126 | from 2013-01-01: [[FACT:ga.sui.wage_base=9,500]] | Not configured in this release [[GAP:DESIGN-RQ-06]] | none | none |
| Hawaii | HI | HI.2 / HI.3 | US-083 | Table or formula | US-127 | 2026-01-01 to 2026-12-31: [[FACT:hi.sui.wage_base=64,500]] | 2026-01-01 to 2026-12-31: [[FACT:hi.sui.new_employer.rate=2.4]]% | none | US-177, US-178 |
| Iowa | IA | IA.2 / IA.3 | US-084 | Flat rate from 2025-01-01: [[FACT:ia.pit.rate.flat=3.8]]%, after the State's allowances, deductions or bands | US-128 | 2026-01-01 to 2026-12-31: [[FACT:ia.sui.wage_base=20,400]]; from 2027-01-01: [[FACT:ia.sui.wage_base=21,100]] | 2026-01-01 to 2026-12-31: [[FACT:ia.sui.new_employer.rate=1]]% | none | none |
| Idaho | ID | ID.2 / ID.3 | US-085 | Flat rate from 2025-01-01: [[FACT:id.pit.rate.flat=5.3]]%, after the State's allowances, deductions or bands | US-129 | 2026-01-01 to 2026-12-31: [[FACT:id.sui.wage_base=58,300]] | 2026-01-01 to 2026-12-31: [[FACT:id.sui.new_employer.rate=1]]% | none | none |
| Illinois | IL | IL.2 / IL.3 | US-086 | Flat rate from 2026-01-01: [[FACT:il.pit.rate.flat=4.95]]%, after the State's allowances, deductions or bands | US-130 | 2026-01-01 to 2026-12-31: [[FACT:il.sui.wage_base=14,250]] | 2026-01-01 to 2026-12-31: [[FACT:il.sui.new_employer.rate=3.35]]% | none | none |
| Indiana | IN | IN.2 / IN.3 | US-087 | Flat rate 2026-01-01 to 2026-12-31: [[FACT:in.pit.rate=2.95]]%; from 2027-01-01: [[FACT:in.pit.rate=2.9]]%, after the State's allowances, deductions or bands | US-131 | from 2011-01-01: [[FACT:in.sui.wage_base=9,500]] | from 2026-01-01: [[FACT:in.sui.new_employer.rate=2.5]]% | none | none |
| Kansas | KS | KS.2 / KS.3 | US-088 | Table or formula | US-132 | 2026-01-01 to 2026-12-31: [[FACT:ks.sui.wage_base=15,100]] | from 2026-01-01: [[FACT:ks.sui.new_employer.rate=1.75]]% | none | none |
| Kentucky | KY | KY.2 / KY.3 | US-089 | Flat rate from 2026-01-01: [[FACT:ky.pit.rate.flat=3.5]]%, after the State's allowances, deductions or bands | US-133 | 2026-01-01 to 2026-12-31: [[FACT:ky.sui.wage_base=12,000]] | 2026-01-01 to 2026-12-31: [[FACT:ky.sui.new_employer.rate=2.7]]% | none | none |
| Louisiana | LA | LA.2 / LA.3 | US-090 | Flat rate from 2026-01-01: [[FACT:la.pit.rate.flat=3.09]]%, after the State's allowances, deductions or bands | US-134 | 2026-01-01 to 2026-12-31: [[FACT:la.sui.wage_base=7,000]] | Not configured in this release [[GAP:DESIGN-RQ-06]] | none | none |
| Massachusetts | MA | MA.2 / MA.3 | US-091 | Flat rate from 2026-01-01: [[FACT:ma.pit.rate=5]]%, after the State's allowances, deductions or bands; surtax [[FACT:ma.pit.surtax.rate=4]]% above USD [[FACT:ma.pit.surtax.threshold=1,107,750]] | US-135 | 2015-01-01 to 2026-12-31: [[FACT:ma.sui.wage_base=15,000]] | 2026-01-01 to 2026-12-31: [[FACT:ma.sui.new_employer.rate=2.42]]% | none | US-179, US-180 |
| Maryland | MD | MD.2 / MD.3 | US-092 | Table or formula | US-136 | from 2026-01-01: [[FACT:md.sui.wage_base=8,500]] | Not configured in this release [[GAP:DESIGN-RQ-06]] | none | US-181, US-182 |
| Maine | ME | ME.2 / ME.3 | US-093 | Table or formula | US-137 | from 2026-01-01: [[FACT:me.sui.wage_base=12,000]] | Not configured in this release [[GAP:DESIGN-RQ-06]] | none | US-183, US-184 |
| Michigan | MI | MI.2 / MI.3 | US-094 | Flat rate from 2026-01-01: [[FACT:mi.pit.rate.flat=4.25]]%, after the State's allowances, deductions or bands | US-138 | 2026-01-01 to 2026-12-31: [[FACT:mi.sui.wage_base=9,000]] | from 2026-01-01: [[FACT:mi.sui.new_employer.rate=2.7]]% | none | none |
| Minnesota | MN | MN.2 / MN.3 | US-095 | Table or formula | US-139 | 2026-01-01 to 2026-12-31: [[FACT:mn.sui.wage_base=44,000]] | Not configured in this release [[GAP:DESIGN-RQ-06]] | none | US-185, US-186 |
| Missouri | MO | MO.2 / MO.3 | US-096 | Table or formula | US-140 | 2026-01-01 to 2026-12-31: [[FACT:mo.sui.wage_base=9,000]] | 2026-01-01 to 2026-12-31: [[FACT:mo.sui.new_employer.rate=2.376]]% | none | none |
| Mississippi | MS | MS.2 / MS.3 | US-097 | Flat rate 2026-01-01 to 2026-12-31: [[FACT:ms.pit.rate.flat=4]]%; from 2027-01-01: [[FACT:ms.pit.rate.flat=3.75]]%, after the State's allowances, deductions or bands | US-141 | from 2011-01-01: [[FACT:ms.sui.wage_base=14,000]] | Not configured in this release [[GAP:DESIGN-RQ-06]] | none | none |
| Montana | MT | MT.2 / MT.3 | US-098 | Table or formula | US-142 | 2026-01-01 to 2026-12-31: [[FACT:mt.sui.wage_base=47,300]] | Not configured in this release [[GAP:DESIGN-RQ-06]] | none | none |
| North Carolina | NC | NC.2 / NC.3 | US-099 | Flat rate from 2026-01-01: [[FACT:nc.pit.rate.flat=3.99]]%, after the State's allowances, deductions or bands | US-143 | 2026-01-01 to 2026-12-31: [[FACT:nc.sui.wage_base=34,200]] | 2026-01-01 to 2026-12-31: [[FACT:nc.sui.new_employer.rate=1]]% | none | none |
| North Dakota | ND | ND.2 / ND.3 | US-100 | Table or formula | US-144 | 2026-01-01 to 2026-12-31: [[FACT:nd.sui.wage_base=46,600]] | from 2026-01-01: [[FACT:nd.sui.new_employer.rate=1]]% | none | none |
| Nebraska | NE | NE.2 / NE.3 | US-101 | Table or formula | US-145 | 2026-01-01 to 2026-12-31: [[FACT:ne.sui.wage_base=9,000]] | 2026-01-01 to 2026-12-31: [[FACT:ne.sui.new_employer.rate=1.25]]% | none | none |
| New Hampshire | NH | NH.2 / NH.3 | none | No wage tax | US-146 | from 2026-01-01: [[FACT:nh.sui.wage_base=14,000]] | 2026-01-01 to 2026-12-31: [[FACT:nh.sui.new_employer.rate=1.7]]% | none | none |
| New Jersey | NJ | NJ.2 / NJ.3 | US-102 | Table or formula | US-147 | 2026-01-01 to 2026-12-31: [[FACT:nj.sui.wage_base=44,800]]; from 2027-01-01: [[FACT:nj.sui.wage_base=46,400]] | from 2025-07-01: [[FACT:nj.sui.new_employer.rate=2.6825]]% | US-168 from 2026-01-01: [[FACT:nj.sui.employee.rate=0.3825]]%; workforce and supplemental workforce fund from 2026-01-01: [[FACT:nj.ui.employee.wf_swf.rate=0.0425]]% | US-187, US-188 |
| New Mexico | NM | NM.2 / NM.3 | US-103 | Table or formula | US-148 | 2026-01-01 to 2026-12-31: [[FACT:nm.sui.wage_base=34,800]] | Not configured in this release [[GAP:DESIGN-RQ-06]] | none | US-202, US-203 |
| Nevada | NV | NV.2 / NV.3 | none | No wage tax | US-149 | 2026-01-01 to 2026-12-31: [[FACT:nv.sui.wage_base=43,700]]; 2027-01-01 to 2027-12-31: [[FACT:nv.sui.wage_base=45,400]] | from 2026-01-01: [[FACT:nv.sui.new_employer.rate=2.95]]% | none | US-206 |
| New York | NY | NY.2 / NY.3 | US-104 | Table or formula | US-150 | 2026-01-01 to 2026-12-31: [[FACT:ny.sui.wage_base=17,600]] | 2026-01-01 to 2026-12-31: [[FACT:ny.sui.new_employer.rate=4.025]]% | none | US-189, US-190, US-207 |
| Ohio | OH | OH.2 / OH.3 | US-105 | Table or formula | US-151 | 2026-01-01 to 2026-12-31: [[FACT:oh.sui.wage_base=9,000]] | 2026-01-01 to 2026-12-31: [[FACT:oh.sui.new_employer.rate=2.85]]% | none | none |
| Oklahoma | OK | OK.2 / OK.3 | US-106 | Table or formula | US-152 | 2026-01-01 to 2026-12-31: [[FACT:ok.sui.wage_base=25,000]]; 2027-01-01 to 2027-12-31: [[FACT:ok.sui.wage_base=24,400]] | 2026-01-01 to 2027-12-31: [[FACT:ok.sui.new_employer.rate=1.5]]% | none | none |
| Oregon | OR | OR.2 / OR.3 | US-107 | Table or formula | US-153 | 2026-01-01 to 2026-12-31: [[FACT:or.sui.wage_base=56,700]] | 2026-01-01 to 2026-12-31: [[FACT:or.sui.new_employer.rate=2.4]]% | none | US-191, US-192, US-193, US-194, US-208, US-209, US-210 |
| Pennsylvania | PA | PA.2 / PA.3 | US-108 | Flat rate from 2026-01-01: [[FACT:pa.pit.rate.flat=3.07]]%, after the State's allowances, deductions or bands | US-154 | from 2018-01-01: [[FACT:pa.sui.wage_base=10,000]] | 2026-01-01 to 2026-12-31: [[FACT:pa.sui.new_employer.rate=3.822]]% | US-169 from 2023-01-01: [[FACT:pa.sui.employee.rate=0.07]]% | none |
| Rhode Island | RI | RI.2 / RI.3 | US-109 | Table or formula | US-155 | 2026-01-01 to 2026-12-31: [[FACT:ri.sui.wage_base=30,800]] | 2026-01-01 to 2026-12-31: [[FACT:ri.sui.new_employer.rate=1.21]]% | none | US-195 |
| South Carolina | SC | SC.2 / SC.3 | US-110 | Table or formula | US-156 | from 2015-01-01: [[FACT:sc.sui.wage_base=14,000]] | 2026-01-01 to 2026-12-31: [[FACT:sc.sui.new_employer.rate=1.06]]% | none | none |
| South Dakota | SD | SD.2 / SD.3 | none | No wage tax | US-157 | from 2015-01-01: [[FACT:sd.sui.wage_base=15,000]] | Not configured in this release [[GAP:DESIGN-RQ-06]] | none | none |
| Tennessee | TN | TN.2 / TN.3 | none | No wage tax | US-158 | 2018-01-01 to 2026-12-31: [[FACT:tn.sui.wage_base=7,000]] | from 2026-01-01: [[FACT:tn.sui.new_employer.rate=2.7]]% | none | none |
| Texas | TX | TX.2 / TX.3 | none | No wage tax | US-159 | from 2026-01-01: [[FACT:tx.sui.wage_base=9,000]] | 2026-01-01 to 2026-12-31: [[FACT:tx.sui.new_employer.rate=2.7]]% | none | none |
| Utah | UT | UT.2 / UT.3 | US-111 | Flat rate from 2026-01-01: [[FACT:ut.pit.rate.flat=4.45]]%, after the State's allowances, deductions or bands | US-160 | 2026-01-01 to 2026-12-31: [[FACT:ut.sui.wage_base=50,700]] | Not configured in this release [[GAP:DESIGN-RQ-06]] | none | none |
| Virginia | VA | VA.2 / VA.3 | US-112 | Table or formula | US-161 | from 2026-01-01: [[FACT:va.sui.wage_base=8,000]] | from 2026-01-01: [[FACT:va.sui.new_employer.rate=2.5]]% | none | none |
| Vermont | VT | VT.2 / VT.3 | US-113 | Table or formula | US-162 | 2026-01-01 to 2026-12-31: [[FACT:vt.sui.wage_base=15,400]] | from 2004-07-01: [[FACT:vt.sui.new_employer.rate=1]]% | none | US-196, US-197 |
| Washington | WA | WA.2 / WA.3 | none | No wage tax | US-163 | 2026-01-01 to 2026-12-31: [[FACT:wa.sui.wage_base=78,200]] | Not configured in this release [[GAP:DESIGN-RQ-06]] | none | US-198, US-199, US-200, US-201 |
| Wisconsin | WI | WI.2 / WI.3 | US-114 | Table or formula | US-164 | from 2013-01-01: [[FACT:wi.sui.wage_base=14,000]] | Not configured in this release [[GAP:DESIGN-RQ-06]] | none | none |
| West Virginia | WV | WV.2 / WV.3 | US-115 | Table or formula | US-165 | from 2024-07-01: [[FACT:wv.sui.wage_base=9,500]] | 2026-01-01 to 2031-07-01: [[FACT:wv.sui.new_employer.rate=2.7]]% | none | none |
| Wyoming | WY | WY.2 / WY.3 | none | No wage tax | US-166 | 2026-01-01 to 2026-12-31: [[FACT:wy.sui.wage_base=33,800]]; from 2027-01-01: [[FACT:wy.sui.wage_base=34,900]] | Not configured in this release [[GAP:DESIGN-RQ-06]] | none | US-205 |

A State whose single new-employer rate is not carried as one number is marked [[GAP:DESIGN-RQ-06]].

### 9840051 — State income tax withholding

Reads `$58525`, the federal withholding `$58507`, `$58508`, `$58509`, `$58524`, and the flags 58415, 58416, 58417, 58418, 58419 and 58421. Rows `US-074` to `US-115`. The State of work and the State of residence decide the mode; the State wages are the State income tax wages of 9840011 (Part 5, State column), not the federal wages. Alabama and Oregon deduct federal withholding from the State base: [[FACT:practice.al.fit_before_sit=AL state base deducts federal withholding: order FIT before AL SIT]] [US-ALS5-001]; [[FACT:practice.or.federal_cap=Use 8,750 federal-tax subtraction cap (pp.6-7 formula); DOR publication also prints 8,500 and its example 1 is mis-computed]] [US-ORS5-009].

```
fed_wh      = 58507 + 58508 + 58524 + 58509
base(S)     = 58525 - IF(S is AL or OR; fed_wh limited as above; 0)
state_wh(S) = IF(EQUALS($58421;2); STATE_METHOD(S; base(S)); STATE_METHOD_BEFORE_2026_04_01(S; base(S)))   -- the 58421 gate applies to Utah only
work_tax    = state_wh(58415)
res_tax     = state_wh(58416)
credit      = residence-State credit for the work-State tax per the residence annex
58517 = IF(EQUALS($58418;3); IF(EQUALS($58419;1); 0; work_tax); work_tax)
58527 = IF(EQUALS($58418;3); IF(EQUALS($58419;1); res_tax; 0); IF(EQUALS($58418;2); MAX(0; res_tax - credit); 0))
```

Mode 3 needs the certificate 58419 = 1; the work State stops withholding and the employer withholds for the residence State, for example a Pennsylvania resident working in New Jersey with the NJ-165 certificate [US-MULTI-011]. Residence-State rules for residents working elsewhere are in the annex of the residence State; for example [[FACT:multi.resident_out_of_state.ma.withholding_rule=MA amount minus the other jurisdiction's amount (credit method, 830 CMR 62B.2.1(9)(b)); employer without MA office may withhold for MA residents as a convenience]] [US-MAS5-023]. Utah: the table in force from 2026-04-01 applies when 58421 = 2; before that date Not configured in this release [[GAP:DESIGN-RQ-01]]. The default for a missing State certificate is set in Module 2 of the Configuration Guide.

Debit `58517`, `58527`.

### 9840052 — State unemployment insurance

Reads the flags 58417, 58420 and 58429. The State of coverage is the State of localization [US-MULTIS5-017]. Configuration Guide section `X.3` of the State.

```
base_limit = state_wage_base(58417; 58420)
base       = MIN(sui_wages_period; MAX(0; base_limit - sui_wages_ytd_state))
rate_er    = IF(EQUALS($58429;1); DD:`State-assigned unemployment insurance rate`; new_employer_rate(58417; 58420))
58518 = ROUND(rate_er x base)
58519 = ROUND(employee_rate(58417; 58420) x base)
```

The assigned rate is entered per State account and year. A new employer, or an employer with no assigned rate on file, uses the new-employer rate of the jurisdiction register. An employee contribution exists only in the States whose row carries one. State UI wages follow the payment year. How each State notifies the assigned rate is a named limitation [[GAP:DD-RQ-11]].

Debit `58518`, `58519`.

### 9840053 — State programmes

Reads the flags 58415, 58420, 58426 and 58428. One result row per programme and side (the jurisdiction register lists the rows of each State). Parameters are selected by the payment date (58420); the Massachusetts paid family and medical leave parameters by the date the wages were earned (58428). Washington Cares is not withheld when 58426 = 1. The method of each parameter is in the *Method* column.

```
params       = IF(MA paid family and medical leave; IF(EQUALS($58428;1); parameters earned in 2026; parameters earned from 2027); IF(EQUALS($58420;1); parameters of payment dates in 2026; parameters of payment dates from 2027))
by rate:       58520 = ROUND(rate x MIN(programme_wages; MAX(0; cap - programme_wages_ytd)))
by hour:       58520 = rate_per_hour x hours worked
by week:       58520 = MIN(rate x MIN(weekly_wages; weekly_base); weekly_maximum)
by quarter:    58520 = flat fee per quarter
by threshold:  58520 = rate x wages above the quarterly threshold
by share:      employee part = rate x employee_share; employer part = rate x (1 - employee_share)
WA Cares:      58520 = IF(EQUALS($58426;1); 0; ROUND(rate x wages))
```

**Programme parameters.** Every dated value of the research for these programmes:

| State | Parameter | Method | Period | Value |
|---|---|---|---|---|
| California | sdi employee rate | rate on wages | 2026-01-01 to 2026-12-31 | [[FACT:ca.sdi.employee.rate=1.3]]% |
| California | sdi employee rate | rate on wages | from 2027-01-01 | [[FACT:ca.sdi.employee.rate=1.4]]% |
| Colorado | famli employee rate | rate on wages | 2026-01-01 to 2026-12-31 | [[FACT:co.famli.employee.rate=0.44]]% |
| Colorado | famli employee rate | rate on wages | from 2027-01-01 | [[FACT:co.famli.employee.rate=0.43]]% |
| Colorado | famli employer rate | rate on wages | 2026-01-01 to 2026-12-31 | [[FACT:co.famli.employer.rate=0.44]]% |
| Colorado | famli employer rate | rate on wages | from 2027-01-01 | [[FACT:co.famli.employer.rate=0.43]]% |
| Colorado | famli small employer max employees | parameter | from 2026-01-01 | [[FACT:co.famli.small_employer.max_employees=9]] |
| Colorado | famli total rate | rate on wages | 2026-01-01 to 2026-12-31 | [[FACT:co.famli.total.rate=0.88]]% |
| Colorado | famli total rate | rate on wages | from 2027-01-01 | [[FACT:co.famli.total.rate=0.86]]% |
| Connecticut | pfml benefit weekly max | weekly amount or cap | 2026-01-01 to 2026-12-31 | [[FACT:ct.pfml.benefit.weekly_max=1,016.40]] |
| Connecticut | pfml employee rate | rate on wages | 2026-01-01 to 2026-12-31 | [[FACT:ct.pfml.employee.rate=0.5]]% |
| Connecticut | pfml wage cap | annual cap | 2026-01-01 to 2026-12-31 | [[FACT:ct.pfml.wage_cap=184,500]] |
| District of Columbia | pfl benefit weekly max | weekly amount or cap | from 2026-10-01 | [[FACT:dc.pfl.benefit.weekly_max=1,100]] |
| District of Columbia | pfl employer rate | rate on wages | from 2024-07-01 | [[FACT:dc.pfl.employer.rate=0.75]]% |
| District of Columbia | pfml employer rate | rate on wages | from 2026-01-01 | [[FACT:dc.pfml.employer.rate=0.75]]% |
| Delaware | pfml benefit weekly max | weekly amount or cap | 2026-01-01 to 2027-12-31 | [[FACT:de.pfml.benefit.weekly_max=900]] |
| Delaware | pfml employee share max | side share | from 2026-01-01 | [[FACT:de.pfml.employee_share.max=50]]% |
| Delaware | pfml employee share max percent | side share | from 2025-01-01 | [[FACT:de.pfml.employee_share.max_percent=50]]% |
| Delaware | pfml leave parental weeks | weekly amount or cap | from 2026-01-01 | [[FACT:de.pfml.leave.parental_weeks=12]] weeks |
| Delaware | pfml rate cap | annual cap | from 2027-01-01 | [[FACT:de.pfml.rate.cap=1]]% |
| Delaware | pfml rate family caregiving | rate on wages | 2025-01-01 to 2026-12-31 | [[FACT:de.pfml.rate.family_caregiving=0.08]]% |
| Delaware | pfml rate medical | rate on wages | 2025-01-01 to 2026-12-31 | [[FACT:de.pfml.rate.medical=0.4]]% |
| Delaware | pfml rate parental | rate on wages | 2025-01-01 to 2026-12-31 | [[FACT:de.pfml.rate.parental=0.32]]% |
| Delaware | pfml rate total | rate on wages | 2025-01-01 to 2026-12-31 | [[FACT:de.pfml.rate.total=0.8]]% |
| Hawaii | phc employee share max percent of wages | side share | from 2026-01-01 | [[FACT:hi.phc.employee_share.max_percent_of_wages=1.5]]% |
| Hawaii | phc min monthly wage | parameter | 2026-01-01 to 2027-12-31 | [[FACT:hi.phc.min_monthly_wage=1,387]] |
| Hawaii | phc monthly wage threshold | threshold test | from 2026-01-01 | [[FACT:hi.phc.monthly_wage_threshold=1,387]] |
| Hawaii | tdi benefit weekly max | weekly amount or cap | 2026-01-01 to 2026-12-31 | [[FACT:hi.tdi.benefit.weekly_max=871]] |
| Hawaii | tdi employee max rate | rate on wages | from 2026-01-01 | [[FACT:hi.tdi.employee.max_rate=0.5]]% |
| Hawaii | tdi employee max weekly deduction | weekly amount or cap | 2026-01-01 to 2026-12-31 | [[FACT:hi.tdi.employee.max_weekly_deduction=7.50]] |
| Hawaii | tdi max weekly wage base | weekly amount or cap | 2026-01-01 to 2026-12-31 | [[FACT:hi.tdi.max_weekly_wage_base=1,500.21]] |
| Massachusetts | pfml benefit weekly max | weekly amount or cap | 2026-01-01 to 2026-12-31 | [[FACT:ma.pfml.benefit.weekly_max=1,230.39]] |
| Massachusetts | pfml benefit weekly max | weekly amount or cap | from 2027-01-01 | [[FACT:ma.pfml.benefit.weekly_max=1,284.61]] |
| Massachusetts | pfml employee max total 25 plus | parameter | from 2026-01-01 | [[FACT:ma.pfml.employee.max_total.25_plus=0.46]]% |
| Massachusetts | pfml family rate | rate on wages | 2026-01-01 to 2026-12-31 | [[FACT:ma.pfml.family.rate=0.18]]% |
| Massachusetts | pfml family rate | rate on wages | from 2027-01-01 | [[FACT:ma.pfml.family.rate=0.7]]% |
| Massachusetts | pfml medical rate | rate on wages | 2026-01-01 to 2026-12-31 | [[FACT:ma.pfml.medical.rate=0.7]]% |
| Massachusetts | pfml medical rate | rate on wages | from 2027-01-01 | [[FACT:ma.pfml.medical.rate=0.18]]% |
| Massachusetts | pfml rate total under 25 | rate on wages | from 2026-01-01 | [[FACT:ma.pfml.rate.total.under_25=0.46]]% |
| Massachusetts | pfml rate total under 25 | rate on wages | from 2027-01-01 | [[FACT:ma.pfml.rate.total.under_25=0.46]]% |
| Massachusetts | pfml total rate | rate on wages | from 2026-01-01 | [[FACT:ma.pfml.total.rate=0.88]]% |
| Massachusetts | pfml total rate | rate on wages | from 2027-01-01 | [[FACT:ma.pfml.total.rate=0.88]]% |
| Maryland | pfml employee share max percent | side share | from 2027-01-01 | [[FACT:md.pfml.employee_share.max_percent=50]]% |
| Maryland | pfml rate total | rate on wages | from 2027-01-01 | [[FACT:md.pfml.rate.total=0.9]]% |
| Maryland | pfml small employer threshold | threshold test | from 2027-01-01 | [[FACT:md.pfml.small_employer.threshold=15]] employees |
| Maine | pfml employee max rate | rate on wages | 2025-01-01 to 2027-12-31 | [[FACT:me.pfml.employee.max_rate=0.5]]% |
| Maine | pfml rate total 15 plus | rate on wages | 2025-01-01 to 2027-12-31 | [[FACT:me.pfml.rate.total.15_plus=1]]% |
| Maine | pfml rate total under 15 | rate on wages | 2025-01-01 to 2027-12-31 | [[FACT:me.pfml.rate.total.under_15=0.5]]% |
| Maine | pfml total rate 15plus | rate on wages | 2025-01-01 to 2027-12-31 | [[FACT:me.pfml.total.rate.15plus=1]]% |
| Maine | pfml total rate under15 | rate on wages | 2025-01-01 to 2027-12-31 | [[FACT:me.pfml.total.rate.under15=0.5]]% |
| Minnesota | pfml employee max share rate | side share | 2026-01-01 to 2027-12-31 | [[FACT:mn.pfml.employee.max_share.rate=0.44]]% |
| Minnesota | pfml employer share min | side share | from 2026-01-01 | [[FACT:mn.pfml.employer_share.min=50]]% |
| Minnesota | pfml rate family | rate on wages | 2026-01-01 to 2027-12-31 | [[FACT:mn.pfml.rate.family=0.27]]% |
| Minnesota | pfml rate medical | rate on wages | 2026-01-01 to 2027-12-31 | [[FACT:mn.pfml.rate.medical=0.61]]% |
| Minnesota | pfml rate total | rate on wages | 2026-01-01 to 2027-12-31 | [[FACT:mn.pfml.rate.total=0.88]]% |
| Minnesota | pfml small employer rate | rate on wages | 2026-01-01 to 2027-12-31 | [[FACT:mn.pfml.small_employer.rate=0.66]]% |
| Minnesota | pfml wage cap annual | annual cap | 2026-01-01 to 2026-12-31 | [[FACT:mn.pfml.wage_cap.annual=185,000]] |
| New Jersey | fli employee max annual | annual cap | 2026-01-01 to 2026-12-31 | [[FACT:nj.fli.employee.max_annual=393.53]] |
| New Jersey | fli employee rate | rate on wages | 2026-01-01 to 2026-12-31 | [[FACT:nj.fli.employee.rate=0.23]]% |
| New Jersey | fli employee rate | rate on wages | from 2027-01-01 | [[FACT:nj.fli.employee.rate=0.24]]% |
| New Jersey | tdi employee max annual | annual cap | 2026-01-01 to 2026-12-31 | [[FACT:nj.tdi.employee.max_annual=325.09]] |
| New Jersey | tdi employee rate | rate on wages | 2026-01-01 to 2026-12-31 | [[FACT:nj.tdi.employee.rate=0.19]]% |
| New Jersey | tdi employee rate | rate on wages | from 2027-01-01 | [[FACT:nj.tdi.employee.rate=0.24]]% |
| New Jersey | tdi employer new employer rate | rate on wages | from 2025-07-01 | [[FACT:nj.tdi.employer.new_employer.rate=0.5]]% |
| New Jersey | tdi max weekly benefit | weekly amount or cap | 2026-01-01 to 2026-12-31 | [[FACT:nj.tdi.max_weekly_benefit=1,119]] |
| New Jersey | tdi fli employee wage base annual | annual cap | 2026-01-01 to 2026-12-31 | [[FACT:nj.tdi_fli.employee.wage_base.annual=171,100]] |
| New Jersey | tdi fli employee wage base annual | annual cap | from 2027-01-01 | [[FACT:nj.tdi_fli.employee.wage_base.annual=177,100]] |
| New Jersey | ui employee governmental reimbursable rate | rate on wages | from 2026-01-01 | [[FACT:nj.ui.employee.governmental_reimbursable.rate=0.0825]]% |
| New Jersey | ui employee max annual | annual cap | 2026-01-01 to 2026-12-31 | [[FACT:nj.ui.employee.max_annual=190.40]] |
| New Jersey | ui employee wf swf rate | rate on wages | from 2026-01-01 | [[FACT:nj.ui.employee.wf_swf.rate=0.0425]]% |
| New Mexico | wc admin fee employee quarterly | flat fee per quarter | 2025-07-01 to 2028-06-30 | [[FACT:nm.wc.admin_fee.employee.quarterly=2.25]] |
| New Mexico | wc admin fee employee quarterly | flat fee per quarter | 2028-07-01 to 2033-06-30 | [[FACT:nm.wc.admin_fee.employee.quarterly=2.38]] |
| New Mexico | wc admin fee employer quarterly | flat fee per quarter | 2025-07-01 to 2028-06-30 | [[FACT:nm.wc.admin_fee.employer.quarterly=2.55]] |
| New Mexico | wc admin fee employer quarterly | flat fee per quarter | 2028-07-01 to 2033-06-30 | [[FACT:nm.wc.admin_fee.employer.quarterly=2.68]] |
| Nevada | mbt financial mining rate | rate on wages | from 2026-01-01 | [[FACT:nv.mbt.financial_mining.rate=1.554]]% |
| Nevada | mbt general quarterly threshold | flat fee or threshold per quarter | from 2026-01-01 | [[FACT:nv.mbt.general.quarterly_threshold=50,000]] |
| Nevada | mbt general rate | rate on wages | from 2026-01-01 | [[FACT:nv.mbt.general.rate=1.17]]% |
| New York | dbl employee max weekly | weekly amount or cap | from 2026-01-01 | [[FACT:ny.dbl.employee.max_weekly=0.60]] |
| New York | dbl employee rate | rate on wages | from 2026-01-01 | [[FACT:ny.dbl.employee.rate=0.5]]% |
| New York | dbl employee weekly max | weekly amount or cap | from 2026-01-01 | [[FACT:ny.dbl.employee.weekly_max=0.60]] |
| New York | pfl benefit max weekly | weekly amount or cap | 2026-01-01 to 2026-12-31 | [[FACT:ny.pfl.benefit.max_weekly=1,228.53]] |
| New York | pfl benefit rate of aww | benefit parameter, not withheld | from 2026-01-01 | [[FACT:ny.pfl.benefit.rate_of_aww=67]]% |
| New York | pfl employee max annual | annual cap | 2026-01-01 to 2026-12-31 | [[FACT:ny.pfl.employee.max_annual=411.91]] |
| New York | pfl employee max annual | annual cap | from 2027-01-01 | [[FACT:ny.pfl.employee.max_annual=451.81]] |
| New York | pfl employee rate | rate on wages | 2026-01-01 to 2026-12-31 | [[FACT:ny.pfl.employee.rate=0.432]]% |
| New York | pfl employee rate | rate on wages | from 2027-01-01 | [[FACT:ny.pfl.employee.rate=0.452]]% |
| New York | pfl nysaww | benefit parameter, not withheld | 2026-01-01 to 2026-12-31 | [[FACT:ny.pfl.nysaww=1,833.63]] |
| Oregon | pfml employee share | side share | from 2023-01-01 | [[FACT:or.pfml.employee.share=60]]% |
| Oregon | pfml employer share | side share | from 2026-01-01 | [[FACT:or.pfml.employer_share=40]]% |
| Oregon | pfml rate total | rate on wages | 2026-01-01 to 2026-12-31 | [[FACT:or.pfml.rate.total=1]]% |
| Oregon | pfml small employer threshold | threshold test | from 2023-01-01 | [[FACT:or.pfml.small_employer.threshold=25]] |
| Oregon | pfml total rate | rate on wages | from 2026-01-01 | [[FACT:or.pfml.total.rate=1]]% |
| Oregon | pfml wage cap annual | annual cap | 2026-01-01 to 2026-12-31 | [[FACT:or.pfml.wage_cap.annual=184,500]] |
| Oregon | stt employee rate | rate on wages | from 2018-07-01 | [[FACT:or.stt.employee.rate=0.1]]% |
| Oregon | transit lane employer rate | rate on wages | 2026-01-01 to 2026-12-31 | [[FACT:or.transit.lane.employer.rate=0.8]]% |
| Oregon | transit trimet employer rate | rate on wages | 2026-01-01 to 2026-12-31 | [[FACT:or.transit.trimet.employer.rate=0.8237]]% |
| Oregon | wbf rate per hour | per hour | 2026-01-01 to 2026-12-31 | [[FACT:or.wbf.rate.per_hour=0.018]] USD per hour |
| Rhode Island | tdi employee annual max | annual cap | from 2026-01-01 | [[FACT:ri.tdi.employee.annual_max=1,100]] |
| Rhode Island | tdi employee max annual | annual cap | 2026-01-01 to 2026-12-31 | [[FACT:ri.tdi.employee.max_annual=1,100]] |
| Rhode Island | tdi employee rate | rate on wages | 2026-01-01 to 2026-12-31 | [[FACT:ri.tdi.employee.rate=1.1]]% |
| Rhode Island | tdi wage base annual | annual cap | 2026-01-01 to 2026-12-31 | [[FACT:ri.tdi.wage_base.annual=100,000]] |
| Tennessee | wc benefit ppd weekly max | weekly amount or cap | 2026-07-01 to 2027-06-30 | [[FACT:tn.wc.benefit.ppd.weekly_max=1,353]] |
| Tennessee | wc benefit ttd weekly max | weekly amount or cap | 2026-07-01 to 2027-06-30 | [[FACT:tn.wc.benefit.ttd.weekly_max=1,488.30]] |
| Tennessee | wc benefit weekly min | weekly amount or cap | 2026-07-01 to 2027-06-30 | [[FACT:tn.wc.benefit.weekly_min=202.95]] |
| Vermont | ccc employee max rate | rate on wages | from 2024-07-01 | [[FACT:vt.ccc.employee.max_rate=0.11]]% |
| Vermont | ccc total rate | rate on wages | from 2024-07-01 | [[FACT:vt.ccc.total.rate=0.44]]% |
| Washington | cares employee rate | rate on wages | from 2026-01-01 | [[FACT:wa.cares.employee.rate=0.58]]% |
| Washington | pfml employee share | side share | 2026-01-01 to 2026-12-31 | [[FACT:wa.pfml.employee.share=71.43]]% |
| Washington | pfml employee share | side share | from 2027-01-01 | [[FACT:wa.pfml.employee.share=70.7]]% |
| Washington | pfml small employer threshold | threshold test | from 2026-01-01 | [[FACT:wa.pfml.small_employer.threshold=50]] |
| Washington | pfml total rate | rate on wages | 2026-01-01 to 2026-12-31 | [[FACT:wa.pfml.total.rate=1.13]]% |
| Washington | pfml total rate | rate on wages | from 2027-01-01 | [[FACT:wa.pfml.total.rate=1.2]]% |
| Washington | pfml wage cap | annual cap | 2026-01-01 to 2026-12-31 | [[FACT:wa.pfml.wage_cap=184,500]] |
| Washington | pfml wage cap annual | annual cap | 2026-01-01 to 2026-12-31 | [[FACT:wa.pfml.wage_cap.annual=184,500]] |
| Washington | wc class101 employee hourly | per hour | from 2026-01-01 | [[FACT:wa.wc.class101.employee_hourly=0.3532]] |
| Washington | wc supplemental pension rate | per hour | 2026-01-01 to 2026-12-31 | [[FACT:wa.wc.supplemental_pension.rate=0.1912]] USD per hour |

Massachusetts paid family and medical leave: the 2026 and 2027 splits are the dated entries above, selected by 58428; for the other programmes with a 2027 entry the basis is Not configured in this release [[GAP:DESIGN-RQ-09]]. The disagreement between the statute and the published guidance is recorded in Part 6. `US-205` (Wyoming workers' compensation, employer-specific rate) and `US-207` (New York MCTMT) carry no parameter in the research: Not configured in this release [[GAP:DESIGN-RQ-07]].

Debit `58520`.

### 9840061 — Local taxes

Reads the locality flags 58431, 58432, 58433, 58434, 58435, 58436, 58437, 58438, 58439 and 58440, set from the locality fields of the Data Dictionary. Local rows: `US-211`, `US-212`, `US-213`, `US-214`, `US-215`, `US-216`, `US-217`, `US-218`, `US-219`, `US-220`, `US-221`, `US-222`, `US-223`, `US-224`, `US-225`, `US-226`, `US-227`, `US-228`, `US-229`, `US-230`, `US-231`, `US-232`, `US-233`. Each locality, rate, base and filing rule is set out in the jurisdiction annexes (section `X.2c`) of `US-CCG-001 v1.0`; this design routes the wages and does not repeat the rates.

```
58521 = IF(EQUALS($58431;1); `US-223` on DD:`New York City or Yonkers residence status`; IF(EQUALS($58431;2); `US-223`; 0))
      + IF(EQUALS($58432;1); `US-224` on DD:`Ohio municipality of work` and DD:`Ohio municipality of residence`; 0)
      + IF(EQUALS($58433;1); `US-228` and `US-229` on DD:`Pennsylvania PSD code of the work location` and DD:`Pennsylvania PSD code of the residence`; 0)
      + IF(EQUALS($58434;1); `US-215` on DD:`Indiana county of principal employment on January 1`; 0)
      + IF(EQUALS($58435;1); `US-217`; 0)
      + IF(EQUALS($58436;1); `US-216` on DD:`Kentucky locality of residence (school board component)`; 0)
      + IF(EQUALS($58437;1); `US-226` and `US-227`; 0)
      + IF(EQUALS($58438;1); `US-218` and `US-219`; 0)
      + IF(EQUALS($58439;1); `US-212` and `US-213`; 0)
      + IF(EQUALS($58440;1); Iowa school district surtax; 0)
```

The Ohio school district tax `US-225` reads DD:`Ohio school district of residence`. The Iowa school district has no catalogue row: Not configured in this release [[GAP:DESIGN-RQ-07]]. Other local rows of the catalogue are selected by the work location of the Data Dictionary and the annex of the State.

Debit `58521`.

### 9840071 — Minimum wage rate

Reads the work State 58415 and the hours of the time data with their work date. The rate is selected by the date the hours were worked, not by the payment date; hours of a period that spans a change date are split at that date. [[FACT:multi.wage_hour.overlay_rule=FLSA does not excuse a higher State/municipal minimum wage, a lower maximum workweek or a stricter child-labour standard: apply the more protective standard of the place where the work is performed]] [US-MULTIS5-008].

```
rate(S; d)  = dated rate of the State table below at the work date d (the federal rate when the State has no entry)
58526 = MAX(federal_rate(d); rate(58415; d); local_rate(d))
```

Federal rate: USD [[FACT:fed.minwage.hourly=7.25]] [US-FEDS5-017]. Local minimum wages are set out in section `X.1` of the State annex. State rates reaching 2026 or later:

| State | Annex | Period | Hourly rate (USD) |
|---|---|---|---|
| Alaska | AK.1 | 2025-07-01 to 2026-06-30 | [[FACT:ak.minwage.hourly=13]] |
| Alaska | AK.1 | 2026-07-01 to 2027-06-30 | [[FACT:ak.minwage.hourly=14]] |
| Alaska | AK.1 | from 2027-07-01 | [[FACT:ak.minwage.hourly=15]] |
| Arkansas | AR.1 | from 2021-01-01 | [[FACT:ar.minwage.hourly=11]] |
| Arizona | AZ.1 | 2026-01-01 to 2026-12-31 | [[FACT:az.minwage.hourly=15.15]] |
| Arizona | AZ.1 | from 2027-01-01 | [[FACT:az.minwage.hourly=15.65]] |
| California | CA.1 | 2026-01-01 to 2026-12-31 | [[FACT:ca.minwage.hourly=16.90]] |
| California | CA.1 | from 2027-01-01 | [[FACT:ca.minwage.hourly=17.40]] |
| Colorado | CO.1 | 2026-01-01 to 2026-12-31 | [[FACT:co.minwage.hourly=15.16]] |
| Connecticut | CT.1 | 2026-01-01 to 2026-12-31 | [[FACT:ct.minwage.hourly=16.94]] |
| Connecticut | CT.1 | from 2027-01-01 | [[FACT:ct.minwage.hourly=17.48]] |
| District of Columbia | DC.1 | 2025-07-01 to 2026-06-30 | [[FACT:dc.minwage.hourly=17.95]] |
| District of Columbia | DC.1 | from 2026-07-01 | [[FACT:dc.minwage.hourly=18.40]] |
| Delaware | DE.1 | from 2025-01-01 | [[FACT:de.minwage.hourly=15]] |
| Florida | FL.1 | 2025-09-30 to 2026-09-29 | [[FACT:fl.minwage.hourly=14]] |
| Florida | FL.1 | 2026-09-30 to 2027-12-31 | [[FACT:fl.minwage.hourly=15]] |
| Hawaii | HI.1 | 2026-01-01 to 2027-12-31 | [[FACT:hi.minwage.hourly=16]] |
| Hawaii | HI.1 | from 2028-01-01 | [[FACT:hi.minwage.hourly=18]] |
| Iowa | IA.1 | from 2008-01-01 | [[FACT:ia.minwage.hourly=7.25]] |
| Idaho | ID.1 | from 2009-07-24 | [[FACT:id.minwage.hourly=7.25]] |
| Illinois | IL.1 | from 2025-01-01 | [[FACT:il.minwage.hourly=15]] |
| Indiana | IN.1 | from 2009-07-24 | [[FACT:in.minwage.hourly=7.25]] |
| Kansas | KS.1 | from 2010-01-01 | [[FACT:ks.minwage.hourly=7.25]] |
| Kentucky | KY.1 | from 2009-07-01 | [[FACT:ky.minwage.hourly=7.25]] |
| Massachusetts | MA.1 | from 2023-01-01 | [[FACT:ma.minwage.hourly=15]] |
| Maryland | MD.1 | from 2024-01-01 | [[FACT:md.minwage.hourly=15]] |
| Maine | ME.1 | 2026-01-01 to 2026-12-31 | [[FACT:me.minwage.hourly=15.10]] |
| Maine | ME.1 | from 2027-01-01 | [[FACT:me.minwage.hourly=15.70]] |
| Michigan | MI.1 | 2026-01-01 to 2026-12-31 | [[FACT:mi.minwage.hourly=13.73]] |
| Michigan | MI.1 | from 2027-01-01 | [[FACT:mi.minwage.hourly=15]] |
| Minnesota | MN.1 | 2026-01-01 to 2026-12-31 | [[FACT:mn.minwage.hourly=11.41]] |
| Minnesota | MN.1 | from 2027-01-01 | [[FACT:mn.minwage.hourly=11.87]] |
| Missouri | MO.1 | from 2026-01-01 | [[FACT:mo.minwage.hourly=15]] |
| Montana | MT.1 | 2026-01-01 to 2026-12-31 | [[FACT:mt.minwage.hourly=10.85]] |
| North Dakota | ND.1 | from 2009-07-24 | [[FACT:nd.minwage.hourly=7.25]] |
| Nebraska | NE.1 | 2026-01-01 to 2026-12-31 | [[FACT:ne.minwage.hourly=15]] |
| New Jersey | NJ.1 | 2026-01-01 to 2026-12-31 | [[FACT:nj.minwage.hourly=15.92]] |
| New Jersey | NJ.1 | 2027-01-01 to 2027-12-31 | [[FACT:nj.minwage.hourly=16.48]] |
| New Mexico | NM.1 | from 2023-01-01 | [[FACT:nm.minwage.hourly=12]] |
| Nevada | NV.1 | from 2024-07-01 | [[FACT:nv.minwage.hourly=12]] |
| Ohio | OH.1 | 2026-01-01 to 2026-12-31 | [[FACT:oh.minwage.hourly=11]] |
| Ohio | OH.1 | 2027-01-01 to 2027-12-31 | [[FACT:oh.minwage.hourly=11.40]] |
| Pennsylvania | PA.1 | from 2009-07-24 | [[FACT:pa.minwage.hourly=7.25]] |
| Rhode Island | RI.1 | 2026-01-01 to 2026-12-31 | [[FACT:ri.minwage.hourly=16]] |
| Rhode Island | RI.1 | from 2027-01-01 | [[FACT:ri.minwage.hourly=17]] |
| South Dakota | SD.1 | 2026-01-01 to 2026-12-31 | [[FACT:sd.minwage.hourly=11.85]] |
| South Dakota | SD.1 | from 2027-01-01 | [[FACT:sd.minwage.hourly=12.30]] |
| Texas | TX.1 | from 2003-09-01 | [[FACT:tx.minwage.hourly=7.25]] |
| Utah | UT.1 | from 2009-07-24 | [[FACT:ut.minwage.hourly=7.25]] |
| Virginia | VA.1 | 2026-01-01 to 2026-12-31 | [[FACT:va.minwage.hourly=12.77]] |
| Virginia | VA.1 | 2027-01-01 to 2027-12-31 | [[FACT:va.minwage.hourly=13.75]] |
| Virginia | VA.1 | from 2028-01-01 | [[FACT:va.minwage.hourly=15]] |
| Vermont | VT.1 | 2026-01-01 to 2026-12-31 | [[FACT:vt.minwage.hourly=14.42]] |
| Washington | WA.1 | 2026-01-01 to 2026-12-31 | [[FACT:wa.minwage.hourly=17.13]] |
| Washington | WA.1 | from 2027-01-01 | [[FACT:wa.minwage.hourly=17.73]] |
| Wisconsin | WI.1 | from 2009-07-24 | [[FACT:wi.minwage.hourly=7.25]] |
| West Virginia | WV.1 | from 2016-01-01 | [[FACT:wv.minwage.hourly=8.75]] |
| Wyoming | WY.1 | from 2026-05-08 | [[FACT:wy.minwage.hourly=5.15]] |
| Georgia | GA.1 | from 2026-01-01 | [[FACT:ga.minwage.state.hourly=5.15]] |

**Regional and local rates.** Within a State the rate also depends on the region or locality of the work. The region is read from DD:`County of primary employment`, DD:`Work location` and DD:`Worksite ZIP code` at the work date.

| State | Region or locality | Annex | Period | Hourly rate (USD) |
|---|---|---|---|---|
| Minnesota | minneapolis | MN.1 | 2026-01-01 to 2026-12-31 | [[FACT:mn.labour.minwage.local.minneapolis.hourly=16.37]] |
| Minnesota | minneapolis | MN.1 | from 2027-01-01 | [[FACT:mn.labour.minwage.local.minneapolis.hourly=17.02]] |
| Minnesota | st paul macro large | MN.1 | from 2026-01-01 | [[FACT:mn.labour.minwage.local.st_paul.macro_large.hourly=16.37]] |
| Minnesota | st paul micro | MN.1 | 2026-07-01 to 2027-06-30 | [[FACT:mn.labour.minwage.local.st_paul.micro.hourly=14.25]] |
| Minnesota | st paul micro | MN.1 | from 2027-07-01 | [[FACT:mn.labour.minwage.local.st_paul.micro.hourly=15]] |
| Minnesota | st paul small | MN.1 | 2025-07-01 to 2026-06-30 | [[FACT:mn.labour.minwage.local.st_paul.small.hourly=15]] |
| Minnesota | st paul small | MN.1 | from 2026-07-01 | [[FACT:mn.labour.minwage.local.st_paul.small.hourly=16.37]] |
| Minnesota | st paul youth | MN.1 | from 2026-07-01 | [[FACT:mn.labour.minwage.local.st_paul.youth.hourly=13.95]] |
| New Mexico | albuquerque | NM.1 | 2026-01-01 to 2026-12-31 | [[FACT:nm.labour.minwage.local.albuquerque.hourly=12]] |
| New Mexico | albuquerque | NM.1 | from 2027-01-01 | [[FACT:nm.labour.minwage.local.albuquerque.hourly=13]] |
| New Mexico | bernalillo county | NM.1 | 2026-01-01 to 2026-12-31 | [[FACT:nm.labour.minwage.local.bernalillo_county.hourly=10.95]] |
| New Mexico | las cruces | NM.1 | 2026-01-01 to 2026-12-31 | [[FACT:nm.labour.minwage.local.las_cruces.hourly=13.01]] |
| New Mexico | las cruces | NM.1 | from 2027-01-01 | [[FACT:nm.labour.minwage.local.las_cruces.hourly=13.47]] |
| New Mexico | santa fe city | NM.1 | 2025-03-01 to 2026-02-28 | [[FACT:nm.labour.minwage.local.santa_fe_city.hourly=15]] |
| New Mexico | santa fe city | NM.1 | 2026-03-01 to 2026-12-31 | [[FACT:nm.labour.minwage.local.santa_fe_city.hourly=15.40]] |
| New Mexico | santa fe city | NM.1 | from 2027-01-01 | [[FACT:nm.labour.minwage.local.santa_fe_city.hourly=17.50]] |
| New Mexico | santa fe county | NM.1 | 2025-03-01 to 2026-02-28 | [[FACT:nm.labour.minwage.local.santa_fe_county.hourly=15]] |
| New Mexico | santa fe county | NM.1 | from 2026-03-01 | [[FACT:nm.labour.minwage.local.santa_fe_county.hourly=15.40]] |
| New York | nyc li westchester | NY.1 | from 2026-01-01 | [[FACT:ny.labour.minwage.nyc_li_westchester.hourly=17]] |
| New York | rest of state | NY.1 | from 2026-01-01 | [[FACT:ny.labour.minwage.rest_of_state.hourly=16]] |
| Oregon | nonurban | OR.1 | 2025-07-01 to 2026-06-30 | [[FACT:or.labour.minwage.nonurban.hourly=14.05]] |
| Oregon | nonurban | OR.1 | 2026-07-01 to 2027-06-30 | [[FACT:or.labour.minwage.nonurban.hourly=14.55]] |
| Oregon | portland metro | OR.1 | 2025-07-01 to 2026-06-30 | [[FACT:or.labour.minwage.portland_metro.hourly=16.30]] |
| Oregon | portland metro | OR.1 | 2026-07-01 to 2027-06-30 | [[FACT:or.labour.minwage.portland_metro.hourly=16.80]] |
| Oregon | standard | OR.1 | 2025-07-01 to 2026-06-30 | [[FACT:or.labour.minwage.standard.hourly=15.05]] |
| Oregon | standard | OR.1 | 2026-07-01 to 2027-06-30 | [[FACT:or.labour.minwage.standard.hourly=15.55]] |
| Washington | bellingham | WA.1 | 2026-01-01 to 2026-12-31 | [[FACT:wa.labour.minwage.local.bellingham.hourly=19.13]] |
| Washington | burien large | WA.1 | 2026-01-01 to 2026-12-31 | [[FACT:wa.labour.minwage.local.burien.large.hourly=21.78]] |
| Washington | burien mid | WA.1 | 2026-01-01 to 2026-12-31 | [[FACT:wa.labour.minwage.local.burien.mid.hourly=20.78]] |
| Washington | burien small | WA.1 | 2026-01-01 to 2026-12-31 | [[FACT:wa.labour.minwage.local.burien.small.hourly=19.28]] |
| Washington | everett large | WA.1 | 2026-01-01 to 2026-12-31 | [[FACT:wa.labour.minwage.local.everett.large.hourly=20.77]] |
| Washington | everett mid | WA.1 | 2026-01-01 to 2026-06-30 | [[FACT:wa.labour.minwage.local.everett.mid.hourly=18.77]] |
| Washington | everett mid | WA.1 | 2026-07-01 to 2026-12-31 | [[FACT:wa.labour.minwage.local.everett.mid.hourly=19.77]] |
| Washington | king county uninc large | WA.1 | 2026-01-01 to 2026-12-31 | [[FACT:wa.labour.minwage.local.king_county_uninc.large.hourly=20.82]] |
| Washington | renton large | WA.1 | 2026-01-01 to 2026-12-31 | [[FACT:wa.labour.minwage.local.renton.large.hourly=21.57]] |
| Washington | renton mid | WA.1 | 2026-01-01 to 2026-06-30 | [[FACT:wa.labour.minwage.local.renton.mid.hourly=20.57]] |
| Washington | renton mid | WA.1 | 2026-07-01 to 2026-12-31 | [[FACT:wa.labour.minwage.local.renton.mid.hourly=21.57]] |
| Washington | seatac | WA.1 | 2026-01-01 to 2026-12-31 | [[FACT:wa.labour.minwage.local.seatac.hourly=20.74]] |
| Washington | seattle | WA.1 | 2026-01-01 to 2026-12-31 | [[FACT:wa.labour.minwage.local.seattle.hourly=21.30]] |
| Washington | tukwila | WA.1 | 2026-01-01 to 2026-12-31 | [[FACT:wa.labour.minwage.local.tukwila.hourly=21.65]] |

Alabama, Louisiana, Mississippi, North Carolina, New Hampshire, Oklahoma, South Carolina and Tennessee have no State rate above the federal rate and follow the federal rate; the Georgia State rate is below the federal rate, so the maximum of the two is the federal rate. Local rates of California and of the localities of other States are set out in section `X.1` of the State annex. Not configured in this release [[GAP:DESIGN-RQ-10]]
---

## PART 5 — Taxability matrices

Every earning and deduction row of the wage-type catalogue grouped by name and flag pattern. Columns follow the catalogue: Subject to Tax, Table Tax, Special Tax, Q1 OASDI, Q2 Medicare, Q3 FUTA, SUI, State programmes, State income tax, Local income tax. Yes-No means the row's explanation in the catalogue decides.

| Wage type group | Category | Codes | FIT | Table | Special | Q1 | Q2 | Q3 | SUI | Prog. | State | Local | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Basic salary deduction | Deduction | `21100` | Yes | Yes | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Adjustment - Basic salary deduction | Deduction | `21102` | Yes | Yes | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Sick leave - Basic salary deduction | Deduction | `21108` | Yes | Yes | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Unpaid LOA - Basic salary deduction | Deduction | `21109` | Yes | Yes | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Overtime deduction | Deduction | `21110` to `21213` (19) | Yes | Yes | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Adjustment - Overtime deduction | Deduction | `21112` | Yes | Yes | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Salary addition deduction | Deduction | `21140` to `21149` (10) | Yes | Yes | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Premium pay (i.e. Shift premium) deduction | Deduction | `21150` to `21152` (3) | Yes | Yes | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Housing allowance deduction | Deduction | `21400` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Transportation allowance deduction | Deduction | `21520` | Yes-No | Yes | No | Yes-No | Yes-No | Yes-No | Yes-No | Yes-No | Yes | Yes | US-FEDP52-005, US-FEDS5-001, US-FEDS5-003 |
| Health insurance & Life insurance contributions | Deduction | `21610` to `21611` (2) | Yes-No | Yes | No | Yes-No | Yes-No | Yes-No | Yes-No | Yes-No | Yes-No | Yes | US-FEDP52-005, US-FEDS5-001, US-FEDS5-003 |
| Pre-tax 401(k) elective deferral - employee deduction | Deduction | `21640` | No | No | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes-No | Yes-No | US-FEDP52-005, US-FEDS5-029, US-MULTIS5-017 |
| Pre-tax 403(b) salary reduction - employee deduction | Deduction | `21641` | No | No | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes-No | Yes-No | US-FEDP52-005, US-FEDS5-029, US-MULTIS5-017 |
| Pre-tax 457(b) salary reduction - employee deduction | Deduction | `21642` | No | No | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes-No | Yes-No | US-FEDP52-005, US-FEDS5-029, US-MULTIS5-017 |
| Pre-tax SIMPLE plan salary reduction - employee deduction | Deduction | `21645` | No | No | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes-No | Yes-No | US-FEDP52-005, US-FEDS5-029, US-MULTIS5-017 |
| Parking deduction | Deduction | `21810` | Yes-No | Yes | No | Yes-No | Yes-No | Yes-No | Yes-No | Yes-No | Yes | Yes | US-FEDP52-005, US-FEDS5-001, US-FEDS5-003 |
| Basic salary | Earning | `62100` | Yes | Yes | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Arrears - Basic salary | Earning | `62101` | Yes | Yes | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Adjustment - Basic salary | Earning | `62102` | Yes | Yes | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Historic Pay | Earning | `62108` | Yes | Yes | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Unpaid LOA - Basic salary | Earning | `62109` | Yes | Yes | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Overtime | Earning | `62110` to `62139` (30) | Yes | Yes | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Salary addition | Earning | `62140` to `62980` (19) | Yes | Yes | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Arrears - Salary addition | Earning | `62141` | Yes | Yes | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Adjustment - Salary addition | Earning | `62142` | Yes | Yes | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Premium pay (i.e. Shift premium) | Earning | `62150` to `62155` (6) | Yes | Yes | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Holiday Allowance | Earning | `62160` | Yes | Yes | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Arrears - Holiday Allowance | Earning | `62161` | Yes | Yes | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Adjustment - Holiday Allowance | Earning | `62162` | Yes | Yes | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| On-call duty | Earning | `62170` | Yes | Yes | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Arrears - On-call duty | Earning | `62171` | Yes | Yes | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Adjustment - On-call duty | Earning | `62172` | Yes | Yes | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Severance & Seniority | Earning | `62180` to `62182` (3) | Yes | Yes-No | Yes-No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FEDP52-005, US-FEDS5-003, US-FEDS5-029 |
| Bonus (annual, referral, etc) | Earning | `62200` to `62209` (10) | Yes | Yes-No | Yes-No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Bonus - profit sharing | Earning | `62210` to `62219` (10) | Yes | Yes-No | Yes-No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Bonuses - discretionary or one-time | Earning | `62220` to `62229` (10) | Yes | Yes-No | Yes-No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Annual leave pay | Earning | `62300` | Yes | Yes | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Adjustment - Annual leave pay | Earning | `62302` | Yes | Yes | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Annual leave payout | Earning | `62305` | Yes | Yes | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Expat allowance | Earning | `62310` to `62360` (8) | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Arrears - Expat allowance | Earning | `62311` to `62361` (6) | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Adjustment - Expat allowance | Earning | `62312` to `62362` (6) | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Housing allowance | Earning | `62400` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Arrears - Housing allowance | Earning | `62401` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Adjustment - Housing allowance | Earning | `62402` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Housing allowance 2 | Earning | `62410` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Arrears - Housing allowance 2 | Earning | `62411` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Adjustment - Housing allowance 2 | Earning | `62412` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Housing allowance 3 | Earning | `62420` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Arrears - Housing allowance 3 | Earning | `62421` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Adjustment - Housing allowance 3 | Earning | `62422` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Housing & Rent allowance 1 | Earning | `62430` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Arrears - Housing & Rent allowance 1 | Earning | `62431` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Adjustment - Housing & Rent allowance 1 | Earning | `62432` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Housing & Rent allowance 2 | Earning | `62440` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Arrears - Housing & Rent allowance 2 | Earning | `62441` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Housing & Rent allowance 3 | Earning | `62450` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Arrears - Housing & Rent allowance 3 | Earning | `62451` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Housing & Rent allowance 4 | Earning | `62460` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Housing & Rent allowance 5 | Earning | `62470` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Arrears - Housing & Rent allowance 5 | Earning | `62471` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Adjustment - Housing & Rent allowance 5 | Earning | `62472` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Housing & Rent allowance 6 | Earning | `62480` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Arrears - Housing & Rent allowance 6 | Earning | `62481` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Adjustment - Housing & Rent allowance 6 | Earning | `62482` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Car allowance | Earning | `62500` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Arrears - Car allowance | Earning | `62501` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Adjustment - Car allowance | Earning | `62502` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Car maintenance | Earning | `62504` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Car fuel | Earning | `62505` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Car & Transportation allowance | Earning | `62510` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Arrears - Car & Transportation allowance | Earning | `62511` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Adjustment - Car & Transportation allowance | Earning | `62512` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Transportation allowance | Earning | `62520` | Yes-No | Yes | No | Yes-No | Yes-No | Yes-No | Yes-No | Yes-No | Yes | Yes | US-FEDP52-005, US-FEDS5-001, US-FEDS5-003 |
| Arrears - Transportation allowance | Earning | `62521` | Yes-No | Yes | No | Yes-No | Yes-No | Yes-No | Yes-No | Yes-No | Yes | Yes | US-FEDP52-005, US-FEDS5-001, US-FEDS5-003 |
| Adjustment - Transportation allowance | Earning | `62522` | Yes-No | Yes | No | Yes-No | Yes-No | Yes-No | Yes-No | Yes-No | Yes | Yes | US-FEDP52-005, US-FEDS5-001, US-FEDS5-003 |
| Car Maintenance Allowance 2 | Earning | `62530` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Arrears - Car Maintenance Allowance 2 | Earning | `62531` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Adjustment - Car Maintenance Allowance 2 | Earning | `62532` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Relocation allowance | Earning | `62540` to `62560` (2) | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FEDP52-005, US-FEDS5-003, US-FEDS5-008 |
| Arrears - Relocation allowance | Earning | `62541` to `62561` (2) | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FEDP52-005, US-FEDS5-003, US-FEDS5-008 |
| Adjustment - Relocation allowance | Earning | `62542` to `62562` (2) | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FEDP52-005, US-FEDS5-003, US-FEDS5-008 |
| Travel ticket allowance | Earning | `62550` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Arrears - Travel ticket allowance | Earning | `62551` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Adjustment - Travel ticket allowance | Earning | `62552` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Per diem allowance | Earning | `62570` | Yes-No | Yes | No | Yes-No | Yes-No | Yes-No | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Birth and Marriage Allowance | Earning | `62590` to `62591` (2) | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| COVID-19 Allowance | Earning | `62599` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Medical insurance / Medical Care | Earning | `62610` to `62619` (5) | Yes-No | Yes | No | Yes-No | Yes-No | Yes-No | Yes-No | Yes-No | Yes-No | Yes | US-FEDP52-005, US-FEDS5-001, US-FEDS5-003 |
| Arrears - Medical insurance / Medical Care | Earning | `62611` | Yes-No | Yes | No | Yes-No | Yes-No | Yes-No | Yes-No | Yes-No | Yes-No | Yes | US-FEDP52-005, US-FEDS5-001, US-FEDS5-003 |
| Adjustment - Medical insurance / Medical Care | Earning | `62612` | Yes-No | Yes | No | Yes-No | Yes-No | Yes-No | Yes-No | Yes-No | Yes-No | Yes | US-FEDP52-005, US-FEDS5-001, US-FEDS5-003 |
| Personal Allowance 2 | Earning | `62630` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Arrears - Personal Allowance 2 | Earning | `62631` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Adjustment - Personal Allowance 2 | Earning | `62632` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Social raise / Social allowance | Earning | `62650` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Personal Allowance 1 | Earning | `62660` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Arrears - Personal Allowance 1 | Earning | `62661` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Adjustment - Personal Allowance 1 | Earning | `62662` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Education allowance | Earning | `62700` | Yes-No | Yes | No | Yes-No | Yes-No | Yes-No | Yes-No | Yes-No | Yes | Yes | US-FEDP52-005, US-FEDS5-001, US-FEDS5-003 |
| Schooling allowance | Earning | `62710` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Arrears - Schooling allowance | Earning | `62711` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Education & Schooling allowance 2 | Earning | `62720` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Arrears - Education & Schooling allowance 2 | Earning | `62721` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Education & Schooling allowance 3 | Earning | `62730` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Education & Schooling allowance 4 | Earning | `62740` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Arrears - Education & Schooling allowance 4 | Earning | `62741` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Education & Schooling allowance 5 | Earning | `62750` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Arrears - Education & Schooling allowance 5 | Earning | `62751` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Family allowance (MLA, Children) | Earning | `62760` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Adjustment - Family allowance (MLA, Children) | Earning | `62762` | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Recognition Award | Earning | `62770` | Yes | Yes | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Special allowance | Earning | `62870` to `62879` (9) | Yes | Yes | No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Post-termination payment | Earning | `62880` to `62883` (4) | Yes | Yes-No | Yes-No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FEDP52-005, US-FEDS5-003, US-FEDS5-029 |
| Stock options and grants - nonstatutory option spread and restricted stock | Earning | `62890` | Yes | Yes-No | Yes-No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FEDQ1-001 |
| Statutory Gratuity, EOS | Earning | `62900` | Yes | Yes-No | Yes-No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FEDP52-005, US-FEDS5-003, US-FEDS5-029 |
| Supplemental basic (i.e. 13th or 14th months salary) | Earning | `62901` | Yes | Yes-No | Yes-No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Gratuity, EOS, Post-termination, etc. | Earning | `62910` to `62930` (3) | Yes | Yes-No | Yes-No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FEDP52-005, US-FEDS5-003, US-FEDS5-029 |
| Stock options and grants - restricted stock unit settlement | Earning | `62990` | Yes | Yes-No | Yes-No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FEDQ1-001 |
| Stock options and grants - restricted stock vesting | Earning | `62991` | Yes | Yes-No | Yes-No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FEDQ1-001 |
| Stock options and grants - incentive stock option and employee stock purchase plan income | Earning | `62993` | Yes-No | No | No | No | No | No | Yes-No | Yes-No | Yes | Yes | US-FEDQ1-001 |
| Stock options and grants - section 83(i) inclusion | Earning | `62994` | Yes | Yes-No | Yes-No | Yes | Yes | Yes | Yes-No | Yes-No | Yes | Yes | US-FEDQ1-001 |
| Commission | Earning | `US-042` | Yes | Yes-No | Yes-No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-001 |
| Cash tips reported by the employee | Earning | `US-043` | Yes-No | Yes | No | Yes-No | Yes-No | Yes-No | Yes-No | Yes-No | Yes | Yes | US-FEDP52-005, US-FEDS5-001, US-FEDS5-003 |
| Minister parsonage allowance | Earning | `US-046` | No | No | No | No | No | - | - | - | - | - | US-FED-030 |
| Imputed income - group-term life insurance above the excluded coverage | Notional | `US-047` | No | No | No | Yes | Yes | No | Yes-No | Yes-No | Yes-No | Yes-No | US-FEDP52-005, US-FEDS5-001, US-FEDS5-003 |
| Personal use of an employer vehicle (imputed income) | Notional | `US-048` | Yes | Yes-No | Yes-No | Yes | Yes | Yes-No | Yes-No | Yes-No | Yes | Yes | US-FED-007, US-FEDP52-005, US-FEDS5-008 |
| Dependent care assistance (employer-provided or salary reduction) | Deduction | `US-049` | Yes-No | No | No | Yes-No | Yes-No | Yes-No | Yes-No | Yes-No | Yes-No | Yes-No | US-FEDP52-005, US-FEDS5-001, US-FEDS5-003 |
| Employer contribution to a health savings account | Employer Contribution | `US-050` | Yes-No | No | No | Yes-No | Yes-No | Yes-No | Yes-No | Yes-No | Yes-No | Yes-No | US-FEDP52-005, US-FEDS5-008, US-MULTIS5-017 |
| Employer Trump-account contribution | Employer Contribution | `US-051` | Yes-No | - | - | - | - | - | - | - | - | - | US-FEDS5-030 |

---

## PART 6 — Open items

Each item gives the design reading and the research reading. Where they differ the research wins. A limitation is written *Not configured in this release* with its identifier.

| # | Item | Design reading | Research reading | Disposition |
|---|---|---|---|---|
| 1 | Utah withholding before the new table | One table selected by 58421 | The table in force from 2026-04-01 is carried; the earlier table is not | Not configured in this release [[GAP:DESIGN-RQ-01]] |
| 2 | Form W-4 before the 2020 revision (allowance method, nonresident alien Table 1) | 2020 revision only; pre-2020 employees handled manually | Allowance method and Table 1 exist in the research; the Data Dictionary has no field for the revision or the allowance count; change request for Data Dictionary 1.1 | Not configured in this release [[GAP:DESIGN-RQ-02]] |
| 3 | Supplemental withholding method | Flag 58414 from the legal-entity field; default rule in Part 1 | Payer chooses flat rate or aggregate method; the Data Dictionary carries the field | Closed: no limitation |
| 4 | State unemployment insurance assigned rate | Legal-entity rate per State and year (58429) | The State assigns the rate by notice; the Data Dictionary carries the field | [[GAP:DD-RQ-11]] (how each State notifies the rate) |
| 5 | Employee abroad: statement that stops withholding | Withheld normally | The statement stops withholding; the Data Dictionary has no field; change request for Data Dictionary 1.1 | Not configured in this release [[GAP:DESIGN-RQ-05]] |
| 6 | New-employer unemployment rate for some States | Single rate per State | Some States carry a rate by industry or by class and no single number | Not configured in this release [[GAP:DESIGN-RQ-06]] |
| 7 | FUTA credit reduction | Potential rate recorded | Final only after the year-end determination | Not configured in this release [[GAP:RQ-402]]; Not configured in this release [[GAP:RQ-403]] |
| 8 | 2027 federal income tax schedules | Schedules of the build year only | Indexation for the next year is not published in the research | Not configured in this release [[GAP:RQ-530]] |
| 9 | Hawaii withholding for 2027 | Not modelled | The State changes the brackets for 2027 and has not published the tables | Not configured in this release [[GAP:RQ-170]] |
| 10 | Virginia withholding for 2027 | Not modelled | The statute changes the standard deduction for 2027; the formula is not published | Not configured in this release [[GAP:RQ-351]] |
| 11 | District of Columbia withholding method | Method as recorded for the build year | A change revoked personal exemptions and no method is published | Not configured in this release [[GAP:RQ-138]] |
| 12 | Programme rows without a parameter | Row listed, no value written | Wyoming workers' compensation, New York MCTMT and the Iowa school district have no value or row | Not configured in this release [[GAP:DESIGN-RQ-07]] |
| 13 | Programme parameters with no 2027 value | 2027 payment or earned dates use the last carried value only where the research says it continues | Parameters listed in the limitation have no entry for 2027 | Not configured in this release [[GAP:DESIGN-RQ-08]] |
| 14 | Paid or earned basis of programmes with a 2027 change | Selected by the payment date (58420); Massachusetts paid family and medical leave by the date earned (58428) | The research proves the earned-date rule for Massachusetts only; the basis of CA SDI, CO FAMLI, NJ TDI and FLI, NY PFL and WA PFML is not established | Not configured in this release [[GAP:DESIGN-RQ-09]] |
| 15 | Sector-specific and age-specific minimum wages | State and local rows only | Rates for fast food, health care, school bus drivers, farm work, youth and training wages exist in the research; no field selects them | Not configured in this release [[GAP:DESIGN-RQ-10]] |

**Statute against published method.** Where a State's published withholding method differs from the statute, the research directs which one the configuration follows. Both readings:

- [[FACT:practice.al.fit_before_sit=AL state base deducts federal withholding: order FIT before AL SIT]] [US-ALS5-001]
- [[FACT:practice.ct.tables_vs_rules=DRS: 'Use either the withholding calculation rules or the withholding tables' (TPG-211); the two methods can give different amounts; configured: DRS per-period tables up to each table maximum, TPG-211 rules above (CT.2, configuration decision of 2026-11-02)]] [US-CTS5-010]
- [[FACT:practice.dc.2026_method_unpublished=D.C. Act 26-416 (emergency, from 2026-08-13) revoked personal exemptions; no 2026 withholding method published (D-4 under review)]] [US-DCS5-021]
- [[FACT:practice.fed.estimator_not_oracle=IRS Tax Withholding Estimator is not an employer engine or oracle]] [US-FED-021]
- [[FACT:practice.fed.pl119_21_withholding=Do not reduce FIT withholding for tips/overtime deductions except through W-4 Step 4(b)]] [US-FEDS5-030]
- [[FACT:practice.ga.rate_change_2026=4.99% for taxable years beginning on/after 2026-01-01 (5.19% before); from 2027-01-01 reduced by 0.125 point annually to 3.99%, each step delayed one year if an OPB trigger holds at 1 December]] [US-GAS5-009]
- [[FACT:practice.hi.2027_tables_pending=Act 24 SLH 2026 changes TY2027 brackets (new 13% top); 2027 withholding indeterminate until DOTAX issues 2027 Booklet A]] [US-HIS5-029]
- [[FACT:practice.ks.kw100_header_stale=KW-100 header prints "wages paid on and after January 1, 2021" but figures are the 2024 values in force for 2026 (5.20/5.58%)]] [US-KSS5-001]
- [[FACT:practice.ma.pfml_split=Follow DFML: 2026 split unchanged, swap from 2027-01-01 (Ch. 101/2026 s.45 conflict recorded)]] [US-MAS5-012]
- [[FACT:practice.mi.tips_ot_deduction_level=MI 2025 PA 24 tips/overtime deduction (TY2026-2028) is ASSESSMENT only; no change to withholding]] [US-MIS5-017]
- [[FACT:practice.ne.use_circular_en_tables=Withholding uses the DOR Circular EN 2026 percentage-method tables (2.26% to 4.60% rates); the statute (77-2715.03) sets 4.55% for rate three in tax year 2026]] [US-NES5-010]
- [[FACT:practice.oh.flat_rate_vs_tables=Ohio withholding follows the tax commissioner's tables under ORC 5747.06, graduated 1.6% / 2.99% / 3.4% from 2026-08-01 (US-OH-006, US-OHS5-001); the ORC 5747.02 statute rate for TY2026 and thereafter is a flat 2.75% over 26,050 (US-OHS5-007) - use the tables for withholding]] [US-OHS5-007]
- [[FACT:practice.or.federal_cap=Use 8,750 federal-tax subtraction cap (pp.6-7 formula); DOR publication also prints 8,500 and its example 1 is mis-computed]] [US-ORS5-009]
- [[FACT:practice.sc.withholding_rates_2026=Withholding tables in force: SCDOR WH-1603 (Rev. 10/30/25) 2026 tables, 0/3/6%; SCDOR Information Letter #26-20 gives the Act 110 2026 schedule 1.99% (0-29,999) / 5.21% minus 966 (30,000+) and says withholding is unchanged until DOR republishes the tables]] [US-SCS5-004]
- [[FACT:practice.va.std_deduction_2027_not_modelled=Statute: 2027 standard deduction 9,200/18,400; do not model 2027 withholding until Virginia Tax publishes the 2027 formula (guide Rev. 10/26 says the deduction sunsets - wrong)]] [US-VAS5-018]
- [[FACT:practice.wi.use_w166_tables=Withholding uses W-166 schedule (3.54/4.65/5.30/7.65%), not the assessment brackets (3.50/4.40/5.30/7.65%)]] [US-WIS5-010]

---

## PART 7 — Self-review

- Flags declared with their values: 37. Gates on a flag: 54; each compares a flag against a value of its declared list.
- Every wage-type code and Data Dictionary field named in this design exists in the approved catalogue and dictionary.
- Every rate, ceiling and threshold is a bound value; values of another period are written with their period.
- Every limitation is written *Not configured in this release* with its identifier; none carries a value.
- No State-level rule for a special population is configured: a scope statement under the owner decision.

