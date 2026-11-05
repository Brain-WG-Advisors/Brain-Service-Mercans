# US — United States Payroll — Regulation Design v1.0

**Country:** United States (US) · ISO 3166-1 numeric **840** · Currency **USD**  
**Tax year:** 2026; every value that changes with the year carries its own period (2027 values are labelled)  
**Regulation ID prefix:** `9840` (9 + ISO 840) · **Flag accounts:** `58401`–`58449` · **Calculation accounts:** `58501`–`58549`  
**Design basis:** `US-CCG-001 v1.0` (13 modules and the jurisdiction annexes), `US-WTC-001 v1.0`, `US-DD-001 v1.0`  
**Status:** For QA · **Package version:** 1.0

| Version | Issue date | Issued by | Status |
|---|---|---|---|
| 1.0 | 2027-03-31 | Wallisson Gomes | For QA |

**Scope.** Private-sector employers and common-law employees. Independent contractors paid on Form 1099-NEC are out of scope [US-OWN-008]. The layer covers federal employment taxes (income tax withholding, FICA, FUTA), State income tax withholding, State unemployment insurance and State-mandated payroll programmes for the 50 States and the District of Columbia, and refers local taxes to the jurisdiction annexes of the Configuration Guide. Every special population accepted by the owner is in [US-OWN-005]; State-level rules for special populations are a scope statement deferred to a later release, not a gap.

**How to read the design.** Part 1 declares every flag with its values. Part 2 lists the accounts and the wage types they read or write. Part 3 gives the order of the regulations. Part 4 gives each regulation. Part 5 gives the taxability matrix of the wage-type catalogue. Part 6 lists the open items, each with both readings where the design and the research differ; the research wins. Every rate, ceiling and threshold is written once as a bound value; a value valid for a different period is written with that period.

---

## PART 0 — Special-category sweep

Two sweeps ran against the Configuration Guide: one on every row of the coverage matrix, one on every population the owner accepted. A category is *in core* when a flag and a regulation of this design implement it; *no branch* when the research shows no differential treatment; *by reference* when the rule lives in a jurisdiction annex.

| Category | Configuration Guide location | Disposition | Flags | Regulations |
|---|---|---|---|---|
| Resident employee | Module 3; Module 5; Module 6 | In core | 58404, 58415, 58416, 58420 | 9840021, 9840031, 9840032, 9840041, 9840051, 9840052 |
| Non-resident employee | Module 6 (NRA, reciprocity, thresholds); Module 11 | In core: two meanings kept apart (nonresident alien of the United States; employee working in or living in another State) | 58404, 58418, 58419 | 9840024, 9840051 |
| Fixed-term contract | Module 9 | No branch: no federal or general State fixed-term payroll regime | none | none |
| Part-time | Module 4; Module 10 | No branch: no federal part-time payroll regime | none | none |
| Officers without employment contract | Module 11 | In core: corporate officers are employees for payroll; State coverage exclusions are reporting inputs | 58423 | 9840021, 9840052 |
| Apprentices and trainees | Module 4; Module 11 | No branch; student employees are a separate flag | 58411 | 9840031, 9840041 |
| Maternity, paternity and parental leave | Module 8; Module 5 | By reference: no federal paid leave; State programmes are in 9840053 | 58415 | 9840053 |
| Work accident and occupational disease | Module 5; Module 7 | By reference: State workers' compensation rows | 58415 | 9840053 |
| Termination and final pay | Module 9 | In core: final wages are paid wages; supplemental identification applies | 58413 | 9840022, 9840023 |
| Mid-month joiner and leaver | Module 2; Module 3 | No branch: no proration rule; withholding follows the wages paid | none | none |
| Annual regularisation | Module 10; Module 5 | No branch: no employer year-end regularisation; accumulators follow the payment year | 58420 | 9840031, 9840041 |
| Overtime | Module 4; Module 10 | In core as earnings; the qualified overtime premium is reported only | none | 9840011 |
| Multiple employers | Module 3; Module 5 | In core: every wage base and accumulator is kept per employer entity | 58420 | 9840031, 9840032, 9840041 |
| Local regimes | Module 6 (local); annexes PA, OH, MI, IN, MD, KY, NY, OR | By reference: local rows and annexes | 58415, 58416 | 9840061 |
| Employer type and size | Module 10; Module 11 | By reference: coverage thresholds sit in the programme parameters; health-coverage reporting is outside the calculation | 58415 | 9840053 |
| Mid-year rate change | Module 4; Module 6; Module 13 | In core: dated values selected by the payment date | 58420, 58421 | 9840031, 9840051, 9840053 |
| Special pay cycles | Module 3; Module 6 | In core: pay periods per year from the pay frequency | 58422 | 9840021 |
| Accrual versus payment | Module 3; Module 5 | In core: federal taxes follow the payment date | 58420 | 9840021, 9840031 |

**Populations accepted by the owner** [US-OWN-005].

| Population | Flag | Regulations | Wage types | Rule carried by the research |
|---|---|---|---|---|
| Ordinary common-law employee | 58405 = 1 | 9840021, 9840031, 9840032, 9840041, 9840051 | `US-001`, `US-006` | Default path of the design. |
| Nonresident alien | 58404 = 1 | 9840024, 9840021 | `US-004`, `US-033`, `US-029` | Single schedule whatever the marital status; cannot claim exempt; wage add-on added before the table. [US-FEDS5-015] |
| Statutory employee | 58406 = 1 | 9840021, 9840031, 9840032 | `US-035` | FICA withheld, no income tax withholding. [US-FEDR3-005] |
| Household employee | 58407 = 1 | 9840021, 9840031 | `US-028` | Income tax withholding only by agreement. [US-FEDS5-029] |
| Agricultural employee | 58408 = 1 | 9840031, 9840041 | `US-036` | Own return and thresholds. [US-FEDR3-006] |
| Clergy | 58409 = 1 | 9840021, 9840031, 9840032 | `US-034` | No withholding for income tax, social security or Medicare. [US-FED-030] |
| Employee abroad | 58410 = 1 | 9840021 | `US-001` | Citizen abroad: income tax withholding can stop on a statement. [US-FEDR3-007] |
| Student employee | 58411 = 1 | 9840031, 9840041 | `US-038` | Private school or college student: income tax withheld, FICA and FUTA exempt. [US-FEDS5-029] |

Populations in detail (values as carried by the research):

- **Statutory employee:** [[FACT:fed.statutory_employee.treatment=FICA withheld, no FIT withholding; W-2 box 13 checked; FUTA for drivers and traveling salespersons only]] [US-FEDR3-005]
- **Household employee, federal income tax:** [[FACT:fed.household.fit.withholding=only by agreement]] [US-FEDS5-029]
- **Clergy:** [[FACT:fed.minister.withholding=No FIT, social security or Medicare withholding (SE tax; voluntary FIT withholding agreement allowed); parsonage allowance excluded from W-2 box 1]] [US-FED-030]
- **Student employee:** [[FACT:fed.students.treatment=Private school/college students: FIT withheld, FICA and FUTA exempt; public school: FICA exempt unless sec. 218 agreement; work-experience full-time student: FICA taxable]] [US-FEDS5-029]
- **Employee abroad (citizen):** [[FACT:fed.citizen_abroad.form673=Employer may stop FIT withholding on Form 673 statement (FEIE/housing); citizens only]] [US-FEDR3-007]
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

---

## PART 1 — Flags and HR fields

> The engine reads numbers only; string interpretation lives in flags only, never inside a regulation. Each flag lists its values; every gate in Part 4 compares a flag against one of its declared values. A definition written `DD:` names a field of the Data Dictionary; a wage-type code is written in backticks.

| Account | Flag name | Definition | Values |
|---|---|---|---|
| 58401 | Filing status | DD:`Form W-4 filing status (Step 1(c))` (option code J, S or H) **[DERIVED]** | 1 = married filing jointly or qualifying surviving spouse, 2 = single or married filing separately, 3 = head of household |
| 58402 | Multiple jobs box (Step 2) | DD:`Form W-4 multiple jobs or spouse works (Step 2)` **[DERIVED]** | 1 = box checked (Step-2 schedule), 2 = not checked (standard schedule) |
| 58403 | Exempt from withholding | DD:`Form W-4 exempt from withholding` **[DERIVED]** | 1 = exempt certificate in force, 2 = not exempt |
| 58404 | Nonresident alien | `US-033`; DD:`Nonresident alien flag` **[DERIVED]** | 1 = nonresident alien, 2 = not |
| 58405 | Employee category | DD:`Employee special population category` (option code ORD, NRA, STAT, HH, AG, CLG, ABR) **[DERIVED]** | 1 = ordinary, 2 = nonresident alien, 3 = statutory employee, 4 = household, 5 = agricultural, 6 = clergy, 7 = employee abroad |
| 58406 | Statutory employee | `US-035`; from 58405 **[DERIVED]** | 1 = statutory employee, 2 = not |
| 58407 | Household employee | `US-028`; from 58405 **[DERIVED]** | 1 = household employee, 2 = not |
| 58408 | Agricultural employee | `US-036`; from 58405 **[DERIVED]** | 1 = agricultural employee, 2 = not |
| 58409 | Clergy | `US-034`; from 58405 **[DERIVED]** | 1 = minister of religion, 2 = not |
| 58410 | Employee abroad | from 58405 **[DERIVED]** | 1 = employee abroad, 2 = not |
| 58411 | Student employee (exempt case) | `US-038` **[DERIVED]** | 1 = student employee whose wages are exempt from FICA and FUTA, 2 = not |
| 58412 | Third-party sick pay | `US-037`; DD:`W-2 third-party sick pay indicator` **[DERIVED]** | 1 = third-party sick pay, 2 = not |
| 58413 | Supplemental wage payment | earning wage type with Special Tax = Yes, or Yes-No resolved as separately identified **[DERIVED]** | 1 = supplemental wages, 2 = regular wages |
| 58414 | Supplemental withholding method | entity parameter Not configured in this release [[GAP:DESIGN-RQ-03]] | 1 = flat rate, 2 = aggregate method |
| 58415 | Work State | DD:`Work State` **[DERIVED]** | USPS code of the jurisdiction list in Part 4.4 |
| 58416 | Residence State | DD:`Residence State` **[DERIVED]** | USPS code of the jurisdiction list in Part 4.4 |
| 58417 | Unemployment insurance State | `US-041`; DD:`Unemployment insurance State` **[DERIVED]** | USPS code of the jurisdiction list in Part 4.4 |
| 58418 | State withholding mode | from 58415, 58416 and 58419 **[DERIVED]** | 1 = work State only, 2 = work State and residence State, 3 = reciprocity: work State does not withhold |
| 58419 | Reciprocity certificate on file | DD:`State withholding certificate on file` **[DERIVED]** | 1 = certificate on file, 2 = none |
| 58420 | Payment-year rule set | `IF(LESS(DATE_FORMAT($period.payment_date;'yyyyMMdd');'20270101');1;2)` **[DERIVED]** | 1 = 2026 rule set, 2 = 2027 rule set |
| 58421 | Utah table period | `IF(LESS(DATE_FORMAT($period.payment_date;'yyyyMMdd');'20260401');1;2)` **[DERIVED]** | 1 = payment date before 2026-04-01, 2 = from 2026-04-01 |
| 58422 | Pay periods per year | DD:`Pay frequency` **[DERIVED]** | numeric: the count of pay periods of the pay frequency, see 9840021 |
| 58423 | Corporate officer without voluntary UI coverage | DD:`Corporate officer without voluntary unemployment insurance coverage` **[DERIVED]** | 1 = officer without voluntary coverage, 2 = otherwise |

**Note on 58420 and 58421.** Federal taxes follow the payment date, so the rule set is chosen by the payment date and not by the period worked. 58421 selects the Utah withholding table; the Utah table of the earlier period is Not configured in this release [[GAP:DESIGN-RQ-01]].

**Note on 58413 and 58414.** A payment identified separately from regular wages takes the supplemental path of 9840022 and 9840023. The choice between the flat rate and the aggregate method belongs to the payer [US-FEDQ1-002].

**Note on 58422.** The pay periods per year are [[FACT:fed.fit.pay_periods_per_year=2 / 4 / 12 / 24 / 26 / 52 / 260 (semiannual, quarterly, monthly, semimonthly, biweekly, weekly, daily)]] [US-FEDS5-001].

**Note on 58423.** The flag is an input of the State unemployment return; the exclusion rules of each State are in its annex of the Configuration Guide.

---

## PART 2 — Account register

Accounts `58501` onwards hold bases, intermediates and results. The wage-type code is the row of `US-WTC-001` that carries the account in the pay run; an account with no catalogue row is an engine intermediate.

| Account | Type | Regulation | Wage type | Meaning |
|---|---|---|---|---|
| 58501 | Base | 9840011 | `US-011` | Federal income tax wages (accumulator) |
| 58502 | Base | 9840011 | `US-012` | Social security wages, capped accumulator |
| 58503 | Base | 9840011 | `US-014` | Medicare wages and tips, uncapped accumulator |
| 58504 | Base | 9840011 | `US-015` | Wages subject to Additional Medicare Tax withholding |
| 58505 | Base | 9840011 | `US-019` | FUTA taxable wages |
| 58506 | Intermediate | 9840024 | `US-004` | Nonresident alien wage add-on |
| 58507 | Result | 9840021 | `US-001` | Federal income tax withheld, regular wages |
| 58508 | Result | 9840022 | `US-002` | Federal income tax, supplemental wages at the optional flat rate |
| 58509 | Result | 9840023 | `US-003` | Federal income tax, supplemental wages above the mandatory threshold |
| 58510 | Result | 9840031 | WTC `21900` | Social security tax, employee |
| 58511 | Result | 9840031 | `US-005` | Social security tax, employer |
| 58512 | Result | 9840032 | `US-006` | Medicare tax, employee |
| 58513 | Result | 9840032 | `US-007` | Medicare tax, employer |
| 58514 | Result | 9840032 | `US-008` | Additional Medicare Tax, employee |
| 58515 | Result | 9840041 | `US-009` | FUTA, employer |
| 58516 | Result | 9840041 | `US-010` | FUTA credit reduction, employer |
| 58517 | Result | 9840051 | `US-074` to `US-115` | State income tax withholding (one row per State) |
| 58518 | Result | 9840052 | `US-116` to `US-166` | State unemployment insurance, employer (one row per State) |
| 58519 | Result | 9840052 | `US-167` to `US-169` | State unemployment insurance, employee |
| 58520 | Result | 9840053 | `US-170` to `US-204` | State programmes, employee and employer |
| 58521 | Result | 9840061 | `US-211` to `US-233` | Local taxes |

---

## PART 3 — Regulation sequence

Regulations run in this order for each payment. A regulation reads only accounts written by an earlier one.

| Order | Regulation | Name | Reads | Writes |
|---|---|---|---|---|
| 1 | 9840011 | Federal wage bases | earning lines and their wage-type flags | 58501–58505 |
| 2 | 9840024 | Nonresident alien add-on | 58501, 58404, 58422 | 58506 |
| 3 | 9840021 | Federal income tax, regular wages | 58501, 58506 | 58507 |
| 4 | 9840022 | Federal income tax, supplemental flat rate | 58501, 58413, 58414 | 58508 |
| 5 | 9840023 | Federal income tax, supplemental above the mandatory threshold | 58501, 58413 | 58509 |
| 6 | 9840031 | Social security tax | 58502, 58420 | 58510, 58511 |
| 7 | 9840032 | Medicare and Additional Medicare tax | 58503, 58504 | 58512–58514 |
| 8 | 9840041 | FUTA and credit reduction | 58505, 58417 | 58515, 58516 |
| 9 | 9840051 | State income tax withholding | 58501, 58415–58419 | 58517 |
| 10 | 9840052 | State unemployment insurance | 58417, 58423 | 58518, 58519 |
| 11 | 9840053 | State programmes | 58415 | 58520 |
| 12 | 9840061 | Local taxes | 58415, 58416 | 58521 |

---

## PART 4 — Regulation detail

Amounts are rounded half-up to the cent between lines unless a State annex of the Configuration Guide sets another rule; full precision is carried between lines. A contribution or tax with an annual maximum is always the lesser of the remaining annual maximum and the rate times the period base; no annualise-then-divide shortcut is used.

### 9840011 — Federal wage bases

Reads the earning lines. Each earning wage type carries the flags Subject to Tax, Q1 (OASDI), Q2 (Medicare) and Q3 (FUTA) in `US-WTC-001`; where a flag is Yes-No the explanation of the row decides, and Part 5 lists every row. Accumulators: `US-011` (58501), `US-012` (58502), `US-014` (58503), `US-015` (58504), `US-019` (58505).

```
58501 = SUM(earnings with Subject to Tax = Yes) - pre-tax deductions that reduce income tax wages
58502 = SUM(earnings with Q1 = Yes) - pre-tax deductions that reduce FICA wages
58503 = SUM(earnings with Q2 = Yes) - pre-tax deductions that reduce FICA wages
58504 = 58503 year to date, above the Additional Medicare threshold
58505 = SUM(earnings with Q3 = Yes) - payments exempt from FUTA
```

Debit `58501`, `58502`, `58503`, `58504`, `58505`.

### 9840024 — Nonresident alien add-on

Reads `$58501` and the flags 58404 and 58422. The add-on is added to the period wages before the schedule is read [US-FEDS5-002]. It does not apply to flat-rate supplemental wages (a flat-rate supplemental payment is withheld at the flat rate alone).

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

Table 1 applies to an employee whose Form W-4 predates the 2020 revision. The design reads the 2020 revision only: Not configured in this release [[GAP:DESIGN-RQ-02]]. The nonresident alien Form W-4 rule: [[FACT:fed.fit.nra.w4_rule=Single/MFS, write NRA below 4(c), cannot claim exempt]] [US-FEDS5-015].

Debit `58506`.

### 9840021 — Federal income tax, regular wages

Method: [[FACT:fed.fit.method=IRS Pub. 15-T (2026) Worksheet 1A with the Annual Percentage Method tables (STANDARD schedule; Step-2-checked schedule when W-4 Step 2 box checked)]] [US-FEDS5-001]. Reads `$58501` and `$58506`; flags 58401, 58402, 58403, 58404, 58406, 58407, 58409, 58410, 58422.

```
pay_periods   = 58422
annual_wages  = (58501 + 58506) x pay_periods + W-4 Step 4(a)
line_1g       = IF(EQUALS($58402;1); 0; IF(EQUALS($58401;1); [[FACT:fed.fit.worksheet1a.line1g.mfj=12,900]]; [[FACT:fed.fit.worksheet1a.line1g.other=8,600]]))
adjusted      = MAX(0; annual_wages - W-4 Step 4(b) - line_1g)
row          = last row of the schedule with floor <= adjusted
tentative    = cumulative_tax(row) + (adjusted - floor(row)) x rate(row)
credit       = W-4 Step 3 / pay_periods
58507        = IF(EQUALS($58403;1); 0;
                IF(EQUALS($58406;1); 0;
                IF(EQUALS($58409;1); 0;
                MAX(0; tentative / pay_periods - credit) + W-4 Step 4(c))))
```

Schedule: the standard schedule when 58402 = 2, the Step-2 schedule when 58402 = 1. A household employee is withheld only under an agreement [US-FEDS5-029]: `IF(EQUALS($58407;1); agreement_amount; ...)` uses DD:`Household employee: federal income tax withholding agreement`. An employee without a certificate: [[FACT:fed.w4.default_no_certificate=Single or Married filing separately in Step 1(c), no entries in Step 2, Step 3 or Step 4 of the 2026 Form W-4]] [US-FEDQ3-004]. The exempt certificate: [[FACT:fed.w4.exempt.validity=2026 only: the exemption checkbox certification lapses; a new W-4 is required for 2027]] [US-FEDS5-006].

Debit `58507`.

Employees abroad (58410 = 1): the withholding can stop on a statement; Not configured in this release [[GAP:DESIGN-RQ-05]].

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

Reads `$58501` and the flags 58413 and 58414. [[FACT:fed.fit.supplemental.aggregate_method=Supplemental wages identified separately, income tax withheld from regular wages in the current or preceding year: either flat 22% or aggregate - add the supplemental wages to the concurrently paid regular wages (or, if none, to the regular wages of the current or preceding payroll period), figure the tax as if one regular-period payment, subtract the tax withheld or to be withheld from the regular wages, withhold the remainder; earlier supplemental payments of the same period are aggregated too. No income tax withheld from regular wages in the current or preceding year: aggregate method only. Supplemental wages paid with regular wages without specifying each amount: withhold on the total as one regular payment.]] [US-FEDQ1-002].

```
58508 = IF(EQUALS($58413;1); IF(EQUALS($58414;1); ROUND([[FACT:fed.fit.supplemental.flat_rate=22]]% x supplemental_wages); aggregate_method); 0)
58509 = IF(EQUALS($58413;1); [[FACT:fed.fit.supplemental.mandatory_rate=37]]% x MAX(0; supplemental_ytd - [[FACT:fed.fit.supplemental.mandatory_threshold=1,000,000]]); 0)
```

The optional flat rate is [[FACT:fed.fit.supplemental.flat_rate=22]]%; the mandatory rate is [[FACT:fed.fit.supplemental.mandatory_rate=37]]% on the part of the year's supplemental wages above USD [[FACT:fed.fit.supplemental.mandatory_threshold=1,000,000]] [US-FEDS5-003]. The nonresident alien add-on does not apply to flat-rate supplemental wages. The aggregate method uses the schedule of 9840021 on the sum of the supplemental and regular wages. Backup withholding is separate at [[FACT:fed.fit.backup_withholding.rate=24]]% [US-FEDS5-003]. The decision between the flat rate and the aggregate method is Not configured in this release [[GAP:DESIGN-RQ-03]].

Debit `58508`, `58509`.

### 9840031 — Social security tax (OASDI)

Reads `$58502` and the flag 58420. Employee row WTC `21900`; employer row `US-005`. The wage base applies per employer.

```
limit_2026 = [[FACT:fed.fica.oasdi.wage_base=184,500]]   (payment dates in 2026)
limit_2027 = [[FACT:fed.fica.oasdi.wage_base=192,300]]   (payment dates from 2027-01-01)
limit  = IF(EQUALS($58420;1); limit_2026; limit_2027)
58510 = IF(EQUALS($58411;1); 0; IF(EQUALS($58409;1); 0; ROUND([[FACT:fed.fica.oasdi.rate.employee=6.2]]% x MIN(58502; MAX(0; limit - 58502_ytd)))))
58511 = IF(EQUALS($58411;1); 0; IF(EQUALS($58409;1); 0; ROUND([[FACT:fed.fica.oasdi.rate.employer=6.2]]% x MIN(58502; MAX(0; limit - 58502_ytd)))))
```

Social security base: USD [[FACT:fed.fica.oasdi.wage_base=184,500]] for 2026 (period 2026-01-01 to 2026-12-31) and USD [[FACT:fed.fica.oasdi.wage_base=192,300]] from 2027-01-01; employee and employer each at [[FACT:fed.fica.oasdi.rate.employee=6.2]]% [US-FEDS5-005]. A student employee (58411 = 1) is exempt from FICA [US-FEDS5-029]; an employee under a totalization agreement is exempt to the extent the agreement says so: [[FACT:fed.fica.totalization.exemption_rule=Wages are exempt from employee FICA (IRC 3101(c)) and employer FICA (IRC 3111(c)) while a section 233 Social Security Act agreement is in effect, to the extent the agreement makes them subject exclusively to the foreign social security system.]] [US-FEDR2-003], using DD:`Totalization agreement FICA exemption`.

Debit `58510`, `58511`.

### 9840032 — Medicare tax and Additional Medicare Tax

Reads `$58503` and `$58504`. The Medicare base has no annual cap. Employee row `US-006`; employer row `US-007`; Additional Medicare row `US-008`.

```
58512 = IF(EQUALS($58409;1); 0; ROUND([[FACT:fed.fica.medicare.rate.employee=1.45]]% x 58503))
58513 = IF(EQUALS($58409;1); 0; ROUND([[FACT:fed.fica.medicare.rate.employer=1.45]]% x 58503))
58514 = ROUND([[FACT:fed.fica.addl_medicare.rate=0.9]]% x MAX(0; 58503_ytd_after - MAX([[FACT:fed.fica.addl_medicare.withholding_threshold=200,000]]; 58503_ytd_before)))
```

Rates: employee [[FACT:fed.fica.medicare.rate.employee=1.45]]%, employer [[FACT:fed.fica.medicare.rate.employer=1.45]]%; Additional Medicare [[FACT:fed.fica.addl_medicare.rate=0.9]]% on wages above USD [[FACT:fed.fica.addl_medicare.withholding_threshold=200,000]] in the year, employee only [US-FEDS5-005].

Debit `58512`, `58513`, `58514`.

### 9840041 — FUTA and credit reduction

Reads `$58505` and the flag 58417. Rows `US-009` and `US-010`.

```
net_rate = [[FACT:fed.futa.rate.net=0.6]]%
58515 = IF(EQUALS($58411;1); 0; ROUND(net_rate x MIN(58505; MAX(0; [[FACT:fed.futa.wage_base=7,000]] - 58505_ytd))))
58516 = IF(EQUALS($58411;1); 0; ROUND(credit_reduction_rate(58417) x MIN(58505; MAX(0; [[FACT:fed.futa.wage_base=7,000]] - 58505_ytd))))
```

Gross rate [[FACT:fed.futa.rate.gross=6]]%, maximum credit [[FACT:fed.futa.credit.max=5.4]]%, net rate [[FACT:fed.futa.rate.net=0.6]]% on the first USD [[FACT:fed.futa.wage_base=7,000]] of each employee's wages [US-FED-007]. The quarterly deposit applies when the liability exceeds USD [[FACT:fed.futa.deposit_threshold=500]] [US-FEDS5-031]. Credit reduction for California ([[FACT:fed.futa.credit_reduction.ca.potential.rate=5.3]]%) and the Virgin Islands ([[FACT:fed.futa.credit_reduction.vi.potential.rate=4.8]]%) is a potential rate for 2026: Not configured in this release [[GAP:RQ-402]] and Not configured in this release [[GAP:RQ-403]].

Debit `58515`, `58516`.

### 9840051 — State income tax withholding

Reads `$58501` and the flags 58415 to 58419. Rows `US-074` to `US-115`; the State of work and the State of residence decide the mode.

```
state_wh(S)  = withholding of State S by its method class (Part 4.4 table)
58517 = IF(EQUALS($58418;3); 0;
        IF(EQUALS($58418;2); MAX(state_wh(58415); state_wh(58416));
        state_wh(58415)))
```

The mode 58418 = 3 needs the certificate 58419 = 1; the State pairs are carried by the reciprocity text of each State. The default for a missing State certificate is set in Module 2 of the Configuration Guide.

Debit `58517`.

#### Part 4.4 — Jurisdiction register

One row per State and the District of Columbia. *No wage tax* and *flat rate* come from the research; *Table or formula* means the State publishes tables or a formula, set out in its annex of the Configuration Guide. Wage-base cells carry their own period.

| State | USPS | Withholding row | State income tax | UI employer row | UI wage base (USD) | New-employer rate | UI employee | Programme rows |
|---|---|---|---|---|---|---|---|---|
| Alaska | AK | none | No wage tax | US-116 | 2026-01-01 to 2026-12-31: [[FACT:ak.sui.wage_base=54,200]] | 2026-01-01 to 2026-12-31: [[FACT:ak.sui.new_employer.rate=1]]% | US-167 2026-01-01 to 2026-12-31: [[FACT:ak.sui.employee.rate=0.5]]% | none |
| Alabama | AL | US-074 | Table or formula | US-117 | from 2026-01-01: [[FACT:al.sui.wage_base=8,000]] | from 2026-01-01: [[FACT:al.sui.new_employer.rate=2.7]]% | none | none |
| Arkansas | AR | US-075 | Table or formula | US-118 | from 2026-01-01: [[FACT:ar.sui.wage_base=7,000]] | 2026-01-01 to 2026-12-31: [[FACT:ar.sui.new_employer.rate=2]]% | none | none |
| Arizona | AZ | US-076 | Table or formula | US-119 | from 2026-01-01: [[FACT:az.sui.wage_base=8,000]] | 2026-01-01 to 2026-12-31: [[FACT:az.sui.new_employer.rate=2]]% | none | none |
| California | CA | US-077 | Table or formula | US-120 | from 2026-01-01: [[FACT:ca.sui.wage_base=7,000]] | from 2026-01-01: [[FACT:ca.sui.new_employer.rate=3.4]]% | none | US-170 |
| Colorado | CO | US-078 | Flat rate 2026-01-01 to 2026-12-31: [[FACT:co.pit.rate.flat=4.4]]% | US-121 | 2026-01-01 to 2026-12-31: [[FACT:co.sui.wage_base=30,600]]; from 2027-01-01: [[FACT:co.sui.wage_base=32,100]] | Not configured in this release [[GAP:DESIGN-RQ-06]] | none | US-171, US-172 |
| Connecticut | CT | US-079 | Table or formula | US-122 | 2026-01-01 to 2026-12-31: [[FACT:ct.sui.wage_base=27,000]] | 2026-01-01 to 2026-12-31: [[FACT:ct.sui.new_employer.rate=1.9]]% | none | US-173 |
| District of Columbia | DC | US-080 | Table or formula | US-123 | from 2026-01-01: [[FACT:dc.sui.wage_base=9,000]] | from 2026-01-01: [[FACT:dc.sui.new_employer.rate=2.7]]% | none | US-174 |
| Delaware | DE | US-081 | Table or formula | US-124 | 2026-01-01 to 2026-12-31: [[FACT:de.sui.wage_base=14,500]]; from 2027-01-01: [[FACT:de.sui.wage_base=16,500]] | 2026-01-01 to 2026-12-31: [[FACT:de.sui.new_employer.rate=1]]% | none | US-175, US-176 |
| Florida | FL | none | No wage tax | US-125 | from 2015-01-01: [[FACT:fl.sui.wage_base=7,000]] | from 2026-01-01: [[FACT:fl.sui.new_employer.rate=2.7]]% | none | none |
| Georgia | GA | US-082 | Flat rate from 2026-01-01: [[FACT:ga.pit.rate.flat=4.99]]% | US-126 | from 2013-01-01: [[FACT:ga.sui.wage_base=9,500]] | Not configured in this release [[GAP:DESIGN-RQ-06]] | none | none |
| Hawaii | HI | US-083 | Table or formula | US-127 | 2026-01-01 to 2026-12-31: [[FACT:hi.sui.wage_base=64,500]] | 2026-01-01 to 2026-12-31: [[FACT:hi.sui.new_employer.rate=2.4]]% | none | US-177, US-178 |
| Iowa | IA | US-084 | Flat rate from 2025-01-01: [[FACT:ia.pit.rate.flat=3.8]]% | US-128 | 2026-01-01 to 2026-12-31: [[FACT:ia.sui.wage_base=20,400]]; from 2027-01-01: [[FACT:ia.sui.wage_base=21,100]] | 2026-01-01 to 2026-12-31: [[FACT:ia.sui.new_employer.rate=1]]% | none | none |
| Idaho | ID | US-085 | Flat rate from 2025-01-01: [[FACT:id.pit.rate.flat=5.3]]% | US-129 | 2026-01-01 to 2026-12-31: [[FACT:id.sui.wage_base=58,300]] | 2026-01-01 to 2026-12-31: [[FACT:id.sui.new_employer.rate=1]]% | none | none |
| Illinois | IL | US-086 | Flat rate from 2026-01-01: [[FACT:il.pit.rate.flat=4.95]]% | US-130 | 2026-01-01 to 2026-12-31: [[FACT:il.sui.wage_base=14,250]] | 2026-01-01 to 2026-12-31: [[FACT:il.sui.new_employer.rate=3.35]]% | none | US-204 |
| Indiana | IN | US-087 | Flat rate 2026-01-01 to 2026-12-31: [[FACT:in.pit.rate=2.95]]%; from 2027-01-01: [[FACT:in.pit.rate=2.9]]% | US-131 | from 2011-01-01: [[FACT:in.sui.wage_base=9,500]] | from 2026-01-01: [[FACT:in.sui.new_employer.rate=2.5]]% | none | none |
| Kansas | KS | US-088 | Table or formula | US-132 | 2026-01-01 to 2026-12-31: [[FACT:ks.sui.wage_base=15,100]] | from 2026-01-01: [[FACT:ks.sui.new_employer.rate=1.75]]% | none | none |
| Kentucky | KY | US-089 | Flat rate from 2026-01-01: [[FACT:ky.pit.rate.flat=3.5]]% | US-133 | 2026-01-01 to 2026-12-31: [[FACT:ky.sui.wage_base=12,000]] | 2026-01-01 to 2026-12-31: [[FACT:ky.sui.new_employer.rate=2.7]]% | none | none |
| Louisiana | LA | US-090 | Flat rate from 2026-01-01: [[FACT:la.pit.rate.flat=3.09]]% | US-134 | 2026-01-01 to 2026-12-31: [[FACT:la.sui.wage_base=7,000]] | Not configured in this release [[GAP:DESIGN-RQ-06]] | none | none |
| Massachusetts | MA | US-091 | Flat rate from 2026-01-01: [[FACT:ma.pit.rate=5]]% | US-135 | 2015-01-01 to 2026-12-31: [[FACT:ma.sui.wage_base=15,000]] | 2026-01-01 to 2026-12-31: [[FACT:ma.sui.new_employer.rate=2.42]]% | none | US-179, US-180 |
| Maryland | MD | US-092 | Table or formula | US-136 | from 2026-01-01: [[FACT:md.sui.wage_base=8,500]] | Not configured in this release [[GAP:DESIGN-RQ-06]] | none | US-181, US-182 |
| Maine | ME | US-093 | Table or formula | US-137 | from 2026-01-01: [[FACT:me.sui.wage_base=12,000]] | Not configured in this release [[GAP:DESIGN-RQ-06]] | none | US-183, US-184 |
| Michigan | MI | US-094 | Flat rate from 2026-01-01: [[FACT:mi.pit.rate.flat=4.25]]% | US-138 | 2026-01-01 to 2026-12-31: [[FACT:mi.sui.wage_base=9,000]] | from 2026-01-01: [[FACT:mi.sui.new_employer.rate=2.7]]% | none | none |
| Minnesota | MN | US-095 | Table or formula | US-139 | 2026-01-01 to 2026-12-31: [[FACT:mn.sui.wage_base=44,000]] | Not configured in this release [[GAP:DESIGN-RQ-06]] | none | US-185, US-186 |
| Missouri | MO | US-096 | Table or formula | US-140 | 2026-01-01 to 2026-12-31: [[FACT:mo.sui.wage_base=9,000]] | 2026-01-01 to 2026-12-31: [[FACT:mo.sui.new_employer.rate=2.376]]% | none | none |
| Mississippi | MS | US-097 | Flat rate 2026-01-01 to 2026-12-31: [[FACT:ms.pit.rate.flat=4]]%; from 2027-01-01: [[FACT:ms.pit.rate.flat=3.75]]% | US-141 | from 2011-01-01: [[FACT:ms.sui.wage_base=14,000]] | Not configured in this release [[GAP:DESIGN-RQ-06]] | none | none |
| Montana | MT | US-098 | Table or formula | US-142 | 2026-01-01 to 2026-12-31: [[FACT:mt.sui.wage_base=47,300]] | Not configured in this release [[GAP:DESIGN-RQ-06]] | none | none |
| North Carolina | NC | US-099 | Flat rate from 2026-01-01: [[FACT:nc.pit.rate.flat=3.99]]% | US-143 | 2026-01-01 to 2026-12-31: [[FACT:nc.sui.wage_base=34,200]] | 2026-01-01 to 2026-12-31: [[FACT:nc.sui.new_employer.rate=1]]% | none | none |
| North Dakota | ND | US-100 | Table or formula | US-144 | 2026-01-01 to 2026-12-31: [[FACT:nd.sui.wage_base=46,600]] | from 2026-01-01: [[FACT:nd.sui.new_employer.rate=1]]% | none | none |
| Nebraska | NE | US-101 | Table or formula | US-145 | 2026-01-01 to 2026-12-31: [[FACT:ne.sui.wage_base=9,000]] | 2026-01-01 to 2026-12-31: [[FACT:ne.sui.new_employer.rate=1.25]]% | none | none |
| New Hampshire | NH | none | No wage tax | US-146 | from 2026-01-01: [[FACT:nh.sui.wage_base=14,000]] | 2026-01-01 to 2026-12-31: [[FACT:nh.sui.new_employer.rate=1.7]]% | none | none |
| New Jersey | NJ | US-102 | Table or formula | US-147 | 2026-01-01 to 2026-12-31: [[FACT:nj.sui.wage_base=44,800]]; from 2027-01-01: [[FACT:nj.sui.wage_base=46,400]] | from 2025-07-01: [[FACT:nj.sui.new_employer.rate=2.6825]]% | US-168 from 2026-01-01: [[FACT:nj.sui.employee.rate=0.3825]]% | US-187, US-188 |
| New Mexico | NM | US-103 | Table or formula | US-148 | 2026-01-01 to 2026-12-31: [[FACT:nm.sui.wage_base=34,800]] | Not configured in this release [[GAP:DESIGN-RQ-06]] | none | US-202, US-203 |
| Nevada | NV | none | No wage tax | US-149 | 2026-01-01 to 2026-12-31: [[FACT:nv.sui.wage_base=43,700]]; 2027-01-01 to 2027-12-31: [[FACT:nv.sui.wage_base=45,400]] | from 2026-01-01: [[FACT:nv.sui.new_employer.rate=2.95]]% | none | US-206 |
| New York | NY | US-104 | Table or formula | US-150 | 2026-01-01 to 2026-12-31: [[FACT:ny.sui.wage_base=17,600]] | 2026-01-01 to 2026-12-31: [[FACT:ny.sui.new_employer.rate=4.025]]% | none | US-189, US-190, US-207 |
| Ohio | OH | US-105 | Table or formula | US-151 | 2026-01-01 to 2026-12-31: [[FACT:oh.sui.wage_base=9,000]] | 2026-01-01 to 2026-12-31: [[FACT:oh.sui.new_employer.rate=2.85]]% | none | none |
| Oklahoma | OK | US-106 | Table or formula | US-152 | 2026-01-01 to 2026-12-31: [[FACT:ok.sui.wage_base=25,000]]; 2027-01-01 to 2027-12-31: [[FACT:ok.sui.wage_base=24,400]] | 2026-01-01 to 2027-12-31: [[FACT:ok.sui.new_employer.rate=1.5]]% | none | none |
| Oregon | OR | US-107 | Table or formula | US-153 | 2026-01-01 to 2026-12-31: [[FACT:or.sui.wage_base=56,700]] | 2026-01-01 to 2026-12-31: [[FACT:or.sui.new_employer.rate=2.4]]% | none | US-191, US-192, US-193, US-194, US-208, US-209, US-210 |
| Pennsylvania | PA | US-108 | Flat rate from 2026-01-01: [[FACT:pa.pit.rate.flat=3.07]]% | US-154 | from 2018-01-01: [[FACT:pa.sui.wage_base=10,000]] | 2026-01-01 to 2026-12-31: [[FACT:pa.sui.new_employer.rate=3.822]]% | US-169 from 2023-01-01: [[FACT:pa.sui.employee.rate=0.07]]% | none |
| Rhode Island | RI | US-109 | Table or formula | US-155 | 2026-01-01 to 2026-12-31: [[FACT:ri.sui.wage_base=30,800]] | 2026-01-01 to 2026-12-31: [[FACT:ri.sui.new_employer.rate=1.21]]% | none | US-195 |
| South Carolina | SC | US-110 | Table or formula | US-156 | from 2015-01-01: [[FACT:sc.sui.wage_base=14,000]] | 2026-01-01 to 2026-12-31: [[FACT:sc.sui.new_employer.rate=1.06]]% | none | none |
| South Dakota | SD | none | No wage tax | US-157 | from 2015-01-01: [[FACT:sd.sui.wage_base=15,000]] | Not configured in this release [[GAP:DESIGN-RQ-06]] | none | none |
| Tennessee | TN | none | No wage tax | US-158 | 2018-01-01 to 2026-12-31: [[FACT:tn.sui.wage_base=7,000]] | from 2026-01-01: [[FACT:tn.sui.new_employer.rate=2.7]]% | none | none |
| Texas | TX | none | No wage tax | US-159 | from 2026-01-01: [[FACT:tx.sui.wage_base=9,000]] | 2026-01-01 to 2026-12-31: [[FACT:tx.sui.new_employer.rate=2.7]]% | none | none |
| Utah | UT | US-111 | Flat rate from 2026-01-01: [[FACT:ut.pit.rate.flat=4.45]]% | US-160 | 2026-01-01 to 2026-12-31: [[FACT:ut.sui.wage_base=50,700]] | Not configured in this release [[GAP:DESIGN-RQ-06]] | none | none |
| Virginia | VA | US-112 | Table or formula | US-161 | from 2026-01-01: [[FACT:va.sui.wage_base=8,000]] | from 2026-01-01: [[FACT:va.sui.new_employer.rate=2.5]]% | none | none |
| Vermont | VT | US-113 | Table or formula | US-162 | 2026-01-01 to 2026-12-31: [[FACT:vt.sui.wage_base=15,400]] | from 2004-07-01: [[FACT:vt.sui.new_employer.rate=1]]% | none | US-196, US-197 |
| Washington | WA | none | No wage tax | US-163 | 2026-01-01 to 2026-12-31: [[FACT:wa.sui.wage_base=78,200]] | Not configured in this release [[GAP:DESIGN-RQ-06]] | none | US-198, US-199, US-200, US-201 |
| Wisconsin | WI | US-114 | Table or formula | US-164 | from 2013-01-01: [[FACT:wi.sui.wage_base=14,000]] | Not configured in this release [[GAP:DESIGN-RQ-06]] | none | none |
| West Virginia | WV | US-115 | Table or formula | US-165 | from 2024-07-01: [[FACT:wv.sui.wage_base=9,500]] | 2026-01-01 to 2031-07-01: [[FACT:wv.sui.new_employer.rate=2.7]]% | none | none |
| Wyoming | WY | none | No wage tax | US-166 | 2026-01-01 to 2026-12-31: [[FACT:wy.sui.wage_base=33,800]]; from 2027-01-01: [[FACT:wy.sui.wage_base=34,900]] | Not configured in this release [[GAP:DESIGN-RQ-06]] | none | US-205 |

The wage base, the rate range and the new-employer rate of each State are the values of its annex; a State whose single new-employer rate is not carried as one number is marked [[GAP:DESIGN-RQ-06]].

### 9840052 — State unemployment insurance

Reads the flags 58417 and 58423. The State of coverage is the State of localization [US-MULTIS5-017].

```
base     = MIN(sui_wages_period; MAX(0; state_wage_base(58417) - sui_wages_ytd_state))
58518 = ROUND(employer_rate(58417) x base)
58519 = ROUND(employee_rate(58417) x base)
```

The employer rate is the rate assigned by the State, held per legal entity and State; Not configured in this release [[GAP:DESIGN-RQ-04]]. A new employer uses the new-employer rate of Part 4.4. An employee contribution exists only in the States whose row carries one in Part 4.4. An officer without voluntary coverage (58423 = 1) is reported on the State return as the annex of the State requires.

Debit `58518`, `58519`.

### 9840053 — State programmes

Reads the flag 58415. One result row per programme and side (Part 4.4 lists the rows of each State). A programme with a wage cap is the lesser of the remaining annual cap and the rate times the period base.

```
58520 = ROUND(programme_rate(58415; period) x MIN(programme_wages_period; MAX(0; programme_cap(58415) - programme_wages_ytd)))
```

**Programme parameters.** Every dated value of the research for these programmes:

| State | Parameter | Period | Value |
|---|---|---|---|
| California | sdi employee rate | 2026-01-01 to 2026-12-31 | [[FACT:ca.sdi.employee.rate=1.3]]% |
| California | sdi employee rate | from 2027-01-01 | [[FACT:ca.sdi.employee.rate=1.4]]% |
| Colorado | famli employee rate | 2026-01-01 to 2026-12-31 | [[FACT:co.famli.employee.rate=0.44]]% |
| Colorado | famli employee rate | from 2027-01-01 | [[FACT:co.famli.employee.rate=0.43]]% |
| Colorado | famli employer rate | 2026-01-01 to 2026-12-31 | [[FACT:co.famli.employer.rate=0.44]]% |
| Colorado | famli employer rate | from 2027-01-01 | [[FACT:co.famli.employer.rate=0.43]]% |
| Colorado | famli small employer max employees | from 2026-01-01 | [[FACT:co.famli.small_employer.max_employees=9]] |
| Colorado | famli total rate | 2026-01-01 to 2026-12-31 | [[FACT:co.famli.total.rate=0.88]]% |
| Colorado | famli total rate | from 2027-01-01 | [[FACT:co.famli.total.rate=0.86]]% |
| Connecticut | pfml benefit weekly max | 2026-01-01 to 2026-12-31 | [[FACT:ct.pfml.benefit.weekly_max=1,016.40]] |
| Connecticut | pfml employee rate | 2026-01-01 to 2026-12-31 | [[FACT:ct.pfml.employee.rate=0.5]]% |
| Connecticut | pfml wage cap | 2026-01-01 to 2026-12-31 | [[FACT:ct.pfml.wage_cap=184,500]] |
| District of Columbia | pfl benefit weekly max | from 2026-10-01 | [[FACT:dc.pfl.benefit.weekly_max=1,100]] |
| District of Columbia | pfl employer rate | from 2024-07-01 | [[FACT:dc.pfl.employer.rate=0.75]]% |
| District of Columbia | pfml employer rate | from 2026-01-01 | [[FACT:dc.pfml.employer.rate=0.75]]% |
| Delaware | pfml benefit weekly max | 2026-01-01 to 2027-12-31 | [[FACT:de.pfml.benefit.weekly_max=900]] |
| Delaware | pfml employee share max | from 2026-01-01 | [[FACT:de.pfml.employee_share.max=50]]% |
| Delaware | pfml employee share max percent | from 2025-01-01 | [[FACT:de.pfml.employee_share.max_percent=50]]% |
| Delaware | pfml leave parental weeks | from 2026-01-01 | [[FACT:de.pfml.leave.parental_weeks=12]] weeks |
| Delaware | pfml rate cap | from 2027-01-01 | [[FACT:de.pfml.rate.cap=1]]% |
| Delaware | pfml rate family caregiving | 2025-01-01 to 2026-12-31 | [[FACT:de.pfml.rate.family_caregiving=0.08]]% |
| Delaware | pfml rate medical | 2025-01-01 to 2026-12-31 | [[FACT:de.pfml.rate.medical=0.4]]% |
| Delaware | pfml rate parental | 2025-01-01 to 2026-12-31 | [[FACT:de.pfml.rate.parental=0.32]]% |
| Delaware | pfml rate total | 2025-01-01 to 2026-12-31 | [[FACT:de.pfml.rate.total=0.8]]% |
| Hawaii | phc employee share max percent of wages | from 2026-01-01 | [[FACT:hi.phc.employee_share.max_percent_of_wages=1.5]]% |
| Hawaii | phc min monthly wage | 2026-01-01 to 2027-12-31 | [[FACT:hi.phc.min_monthly_wage=1,387]] |
| Hawaii | phc monthly wage threshold | from 2026-01-01 | [[FACT:hi.phc.monthly_wage_threshold=1,387]] |
| Hawaii | tdi benefit weekly max | 2026-01-01 to 2026-12-31 | [[FACT:hi.tdi.benefit.weekly_max=871]] |
| Hawaii | tdi employee max rate | from 2026-01-01 | [[FACT:hi.tdi.employee.max_rate=0.5]]% |
| Hawaii | tdi employee max weekly deduction | 2026-01-01 to 2026-12-31 | [[FACT:hi.tdi.employee.max_weekly_deduction=7.50]] |
| Hawaii | tdi max weekly wage base | 2026-01-01 to 2026-12-31 | [[FACT:hi.tdi.max_weekly_wage_base=1,500.21]] |
| Massachusetts | pfml benefit weekly max | 2026-01-01 to 2026-12-31 | [[FACT:ma.pfml.benefit.weekly_max=1,230.39]] |
| Massachusetts | pfml benefit weekly max | from 2027-01-01 | [[FACT:ma.pfml.benefit.weekly_max=1,284.61]] |
| Massachusetts | pfml employee max total 25 plus | from 2026-01-01 | [[FACT:ma.pfml.employee.max_total.25_plus=0.46]]% |
| Massachusetts | pfml family rate | 2026-01-01 to 2026-12-31 | [[FACT:ma.pfml.family.rate=0.18]]% |
| Massachusetts | pfml family rate | from 2027-01-01 | [[FACT:ma.pfml.family.rate=0.7]]% |
| Massachusetts | pfml medical rate | 2026-01-01 to 2026-12-31 | [[FACT:ma.pfml.medical.rate=0.7]]% |
| Massachusetts | pfml medical rate | from 2027-01-01 | [[FACT:ma.pfml.medical.rate=0.18]]% |
| Massachusetts | pfml rate total under 25 | from 2026-01-01 | [[FACT:ma.pfml.rate.total.under_25=0.46]]% |
| Massachusetts | pfml rate total under 25 | from 2027-01-01 | [[FACT:ma.pfml.rate.total.under_25=0.46]]% |
| Massachusetts | pfml total rate | from 2026-01-01 | [[FACT:ma.pfml.total.rate=0.88]]% |
| Massachusetts | pfml total rate | from 2027-01-01 | [[FACT:ma.pfml.total.rate=0.88]]% |
| Maryland | pfml employee share max percent | from 2027-01-01 | [[FACT:md.pfml.employee_share.max_percent=50]]% |
| Maryland | pfml rate total | from 2027-01-01 | [[FACT:md.pfml.rate.total=0.9]]% |
| Maryland | pfml small employer threshold | from 2027-01-01 | [[FACT:md.pfml.small_employer.threshold=15]] employees |
| Maine | pfml employee max rate | 2025-01-01 to 2027-12-31 | [[FACT:me.pfml.employee.max_rate=0.5]]% |
| Maine | pfml rate total 15 plus | 2025-01-01 to 2027-12-31 | [[FACT:me.pfml.rate.total.15_plus=1]]% |
| Maine | pfml rate total under 15 | 2025-01-01 to 2027-12-31 | [[FACT:me.pfml.rate.total.under_15=0.5]]% |
| Maine | pfml total rate 15plus | 2025-01-01 to 2027-12-31 | [[FACT:me.pfml.total.rate.15plus=1]]% |
| Maine | pfml total rate under15 | 2025-01-01 to 2027-12-31 | [[FACT:me.pfml.total.rate.under15=0.5]]% |
| Minnesota | pfml employee max share rate | 2026-01-01 to 2027-12-31 | [[FACT:mn.pfml.employee.max_share.rate=0.44]]% |
| Minnesota | pfml employer share min | from 2026-01-01 | [[FACT:mn.pfml.employer_share.min=50]]% |
| Minnesota | pfml rate family | 2026-01-01 to 2027-12-31 | [[FACT:mn.pfml.rate.family=0.27]]% |
| Minnesota | pfml rate medical | 2026-01-01 to 2027-12-31 | [[FACT:mn.pfml.rate.medical=0.61]]% |
| Minnesota | pfml rate total | 2026-01-01 to 2027-12-31 | [[FACT:mn.pfml.rate.total=0.88]]% |
| Minnesota | pfml small employer rate | 2026-01-01 to 2027-12-31 | [[FACT:mn.pfml.small_employer.rate=0.66]]% |
| Minnesota | pfml wage cap annual | 2026-01-01 to 2026-12-31 | [[FACT:mn.pfml.wage_cap.annual=185,000]] |
| New Jersey | fli employee max annual | 2026-01-01 to 2026-12-31 | [[FACT:nj.fli.employee.max_annual=393.53]] |
| New Jersey | fli employee rate | 2026-01-01 to 2026-12-31 | [[FACT:nj.fli.employee.rate=0.23]]% |
| New Jersey | fli employee rate | from 2027-01-01 | [[FACT:nj.fli.employee.rate=0.24]]% |
| New Jersey | tdi employee max annual | 2026-01-01 to 2026-12-31 | [[FACT:nj.tdi.employee.max_annual=325.09]] |
| New Jersey | tdi employee rate | 2026-01-01 to 2026-12-31 | [[FACT:nj.tdi.employee.rate=0.19]]% |
| New Jersey | tdi employee rate | from 2027-01-01 | [[FACT:nj.tdi.employee.rate=0.24]]% |
| New Jersey | tdi employer new employer rate | from 2025-07-01 | [[FACT:nj.tdi.employer.new_employer.rate=0.5]]% |
| New Jersey | tdi max weekly benefit | 2026-01-01 to 2026-12-31 | [[FACT:nj.tdi.max_weekly_benefit=1,119]] |
| New Jersey | tdi fli employee wage base annual | 2026-01-01 to 2026-12-31 | [[FACT:nj.tdi_fli.employee.wage_base.annual=171,100]] |
| New Jersey | tdi fli employee wage base annual | from 2027-01-01 | [[FACT:nj.tdi_fli.employee.wage_base.annual=177,100]] |
| New Mexico | wc admin fee employee quarterly | 2025-07-01 to 2028-06-30 | [[FACT:nm.wc.admin_fee.employee.quarterly=2.25]] |
| New Mexico | wc admin fee employee quarterly | 2028-07-01 to 2033-06-30 | [[FACT:nm.wc.admin_fee.employee.quarterly=2.38]] |
| New Mexico | wc admin fee employer quarterly | 2025-07-01 to 2028-06-30 | [[FACT:nm.wc.admin_fee.employer.quarterly=2.55]] |
| New Mexico | wc admin fee employer quarterly | 2028-07-01 to 2033-06-30 | [[FACT:nm.wc.admin_fee.employer.quarterly=2.68]] |
| Nevada | mbt financial mining rate | from 2026-01-01 | [[FACT:nv.mbt.financial_mining.rate=1.554]]% |
| Nevada | mbt general quarterly threshold | from 2026-01-01 | [[FACT:nv.mbt.general.quarterly_threshold=50,000]] |
| Nevada | mbt general rate | from 2026-01-01 | [[FACT:nv.mbt.general.rate=1.17]]% |
| New York | dbl employee max weekly | from 2026-01-01 | [[FACT:ny.dbl.employee.max_weekly=0.60]] |
| New York | dbl employee rate | from 2026-01-01 | [[FACT:ny.dbl.employee.rate=0.5]]% |
| New York | dbl employee weekly max | from 2026-01-01 | [[FACT:ny.dbl.employee.weekly_max=0.60]] |
| New York | pfl benefit max weekly | 2026-01-01 to 2026-12-31 | [[FACT:ny.pfl.benefit.max_weekly=1,228.53]] |
| New York | pfl benefit rate of aww | from 2026-01-01 | [[FACT:ny.pfl.benefit.rate_of_aww=67]]% |
| New York | pfl employee max annual | 2026-01-01 to 2026-12-31 | [[FACT:ny.pfl.employee.max_annual=411.91]] |
| New York | pfl employee max annual | from 2027-01-01 | [[FACT:ny.pfl.employee.max_annual=451.81]] |
| New York | pfl employee rate | 2026-01-01 to 2026-12-31 | [[FACT:ny.pfl.employee.rate=0.432]]% |
| New York | pfl employee rate | from 2027-01-01 | [[FACT:ny.pfl.employee.rate=0.452]]% |
| New York | pfl nysaww | 2026-01-01 to 2026-12-31 | [[FACT:ny.pfl.nysaww=1,833.63]] |
| Oregon | pfml employee share | from 2023-01-01 | [[FACT:or.pfml.employee.share=60]]% |
| Oregon | pfml employer share | from 2026-01-01 | [[FACT:or.pfml.employer_share=40]]% |
| Oregon | pfml rate total | 2026-01-01 to 2026-12-31 | [[FACT:or.pfml.rate.total=1]]% |
| Oregon | pfml small employer threshold | from 2023-01-01 | [[FACT:or.pfml.small_employer.threshold=25]] |
| Oregon | pfml total rate | from 2026-01-01 | [[FACT:or.pfml.total.rate=1]]% |
| Oregon | pfml wage cap annual | 2026-01-01 to 2026-12-31 | [[FACT:or.pfml.wage_cap.annual=184,500]] |
| Oregon | transit lane employer rate | 2026-01-01 to 2026-12-31 | [[FACT:or.transit.lane.employer.rate=0.8]]% |
| Oregon | transit trimet employer rate | 2026-01-01 to 2026-12-31 | [[FACT:or.transit.trimet.employer.rate=0.8237]]% |
| Oregon | wbf rate per hour | 2026-01-01 to 2026-12-31 | [[FACT:or.wbf.rate.per_hour=0.018]] USD per hour |
| Rhode Island | tdi employee annual max | from 2026-01-01 | [[FACT:ri.tdi.employee.annual_max=1,100]] |
| Rhode Island | tdi employee max annual | 2026-01-01 to 2026-12-31 | [[FACT:ri.tdi.employee.max_annual=1,100]] |
| Rhode Island | tdi employee rate | 2026-01-01 to 2026-12-31 | [[FACT:ri.tdi.employee.rate=1.1]]% |
| Rhode Island | tdi wage base annual | 2026-01-01 to 2026-12-31 | [[FACT:ri.tdi.wage_base.annual=100,000]] |
| Tennessee | wc benefit ppd weekly max | 2026-07-01 to 2027-06-30 | [[FACT:tn.wc.benefit.ppd.weekly_max=1,353]] |
| Tennessee | wc benefit ttd weekly max | 2026-07-01 to 2027-06-30 | [[FACT:tn.wc.benefit.ttd.weekly_max=1,488.30]] |
| Tennessee | wc benefit weekly min | 2026-07-01 to 2027-06-30 | [[FACT:tn.wc.benefit.weekly_min=202.95]] |
| Vermont | ccc employee max rate | from 2024-07-01 | [[FACT:vt.ccc.employee.max_rate=0.11]]% |
| Vermont | ccc total rate | from 2024-07-01 | [[FACT:vt.ccc.total.rate=0.44]]% |
| Washington | cares employee rate | from 2026-01-01 | [[FACT:wa.cares.employee.rate=0.58]]% |
| Washington | pfml employee share | 2026-01-01 to 2026-12-31 | [[FACT:wa.pfml.employee.share=71.43]]% |
| Washington | pfml employee share | from 2027-01-01 | [[FACT:wa.pfml.employee.share=70.7]]% |
| Washington | pfml small employer threshold | from 2026-01-01 | [[FACT:wa.pfml.small_employer.threshold=50]] |
| Washington | pfml total rate | 2026-01-01 to 2026-12-31 | [[FACT:wa.pfml.total.rate=1.13]]% |
| Washington | pfml total rate | from 2027-01-01 | [[FACT:wa.pfml.total.rate=1.2]]% |
| Washington | pfml wage cap | 2026-01-01 to 2026-12-31 | [[FACT:wa.pfml.wage_cap=184,500]] |
| Washington | pfml wage cap annual | 2026-01-01 to 2026-12-31 | [[FACT:wa.pfml.wage_cap.annual=184,500]] |
| Washington | wc class101 employee hourly | from 2026-01-01 | [[FACT:wa.wc.class101.employee_hourly=0.3532]] |
| Washington | wc supplemental pension rate | 2026-01-01 to 2026-12-31 | [[FACT:wa.wc.supplemental_pension.rate=0.1912]] USD per hour |

Massachusetts paid family and medical leave: the 2026 and 2027 splits are the dated entries above; the rate in force is chosen by 58420. The disagreement between the statute and the published guidance is recorded in Part 6.

Debit `58520`.

### 9840061 — Local taxes

Reads the flags 58415 and 58416. Local rows: `US-211`, `US-212`, `US-213`, `US-214`, `US-215`, `US-216`, `US-217`, `US-218`, `US-219`, `US-220`, `US-221`, `US-222`, `US-223`, `US-224`, `US-225`, `US-226`, `US-227`, `US-228`, `US-229`, `US-230`, `US-231`, `US-232`, `US-233`. Each locality, rate, base and filing rule is set out in the jurisdiction annexes of `US-CCG-001 v1.0`; this design routes the wages and does not repeat the rates.

```
58521 = SUM(local_tax(locality) for each locality of 58415 and 58416)
```

Debit `58521`.

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
| 2 | Form W-4 before the 2020 revision (allowance method, nonresident alien Table 1) | 2020 revision only | Allowance method and Table 1 exist in the research; the Data Dictionary has no field for the revision or the allowance count | Not configured in this release [[GAP:DESIGN-RQ-02]] |
| 3 | Supplemental withholding method | Entity parameter 58414 | Payer chooses flat rate or aggregate method; the Data Dictionary has no field | Not configured in this release [[GAP:DESIGN-RQ-03]] |
| 4 | State unemployment insurance assigned rate | Held per legal entity and State | The State assigns the rate by notice; the Data Dictionary has no field | Not configured in this release [[GAP:DESIGN-RQ-04]] |
| 5 | Employee abroad: statement that stops withholding | Flag 58410 routes the employee | The statement stops withholding; the Data Dictionary has no field | Not configured in this release [[GAP:DESIGN-RQ-05]] |
| 6 | New-employer unemployment rate for some States | Single rate per State | Some States carry a rate by industry or by class and no single number | Not configured in this release [[GAP:DESIGN-RQ-06]] |
| 7 | FUTA credit reduction | Potential rate recorded | Final only after the year-end determination | Not configured in this release [[GAP:RQ-402]]; Not configured in this release [[GAP:RQ-403]] |
| 8 | 2027 federal income tax schedules | Schedules of the build year only | Indexation for the next year is not published in the research | Not configured in this release [[GAP:RQ-530]] |
| 9 | Hawaii withholding for 2027 | Not modelled | The State changes the brackets for 2027 and has not published the tables | Not configured in this release [[GAP:RQ-170]] |
| 10 | Virginia withholding for 2027 | Not modelled | The statute changes the standard deduction for 2027; the formula is not published | Not configured in this release [[GAP:RQ-351]] |
| 11 | District of Columbia withholding method | Method as recorded for the build year | A change revoked personal exemptions and no method is published | Not configured in this release [[GAP:RQ-138]] |

**Statute against published method.** Where a State's published withholding method differs from the statute, the research directs which one the configuration follows. Both readings:

- [[FACT:practice.al.fit_before_sit=AL state base deducts federal withholding: order FIT before AL SIT]] [US-ALS5-001]
- [[FACT:practice.ct.tables_vs_rules=DRS permits tables or TPG-211 rules; results differ up to 0.48/period; configured: DRS per-period tables up to each table maximum, TPG-211 rules above (CT.2, configuration decision of 2026-11-02)]] [US-CTS5-010]
- [[FACT:practice.dc.2026_method_unpublished=D.C. Act 26-416 (emergency, from 2026-08-13) revoked personal exemptions; no 2026 withholding method published (D-4 under review)]] [US-DCS5-021]
- [[FACT:practice.fed.estimator_not_oracle=IRS Tax Withholding Estimator is not an employer engine or oracle]] [US-FED-021]
- [[FACT:practice.fed.pl119_21_withholding=Do not reduce FIT withholding for tips/overtime deductions except through W-4 Step 4(b)]] [US-FEDS5-030]
- [[FACT:practice.ga.rate_change_2026=4.99% for TY2026 (5.19% before); 2027 0.125-point step conditional on OPB report of 2026-12-01]] [US-GAS5-009]
- [[FACT:practice.hi.2027_tables_pending=Act 24 SLH 2026 changes TY2027 brackets (new 13% top); 2027 withholding indeterminate until DOTAX issues 2027 Booklet A]] [US-HIS5-029]
- [[FACT:practice.ks.kw100_header_stale=KW-100 header prints "wages paid on and after January 1, 2021" but figures are the 2024 values in force for 2026 (5.20/5.58%)]] [US-KSS5-001]
- [[FACT:practice.ma.pfml_split=Follow DFML: 2026 split unchanged, swap from 2027-01-01 (Ch. 101/2026 s.45 conflict recorded)]] [US-MAS5-012]
- [[FACT:practice.mi.tips_ot_deduction_level=MI 2025 PA 24 tips/overtime deduction (TY2026-2028) is ASSESSMENT only; no change to withholding]] [US-MIS5-017]
- [[FACT:practice.ne.use_circular_en_tables=Withholding uses DOR Circular EN tables (2026 2.26-4.60%), not the statutory 4.55% rate]] [US-NES5-018]
- [[FACT:practice.oh.flat_rate_vs_tables=TY2026 statute flat 2.75% but withholding tables graduated to 3.4% (5747.06 rule vs 5747.02 rate) - use the tables]] [US-OHS5-007]
- [[FACT:practice.or.federal_cap=Use 8,750 federal-tax subtraction cap (pp.6-7 formula); DOR publication also prints 8,500 and its example 1 is mis-computed]] [US-ORS5-009]
- [[FACT:practice.sc.withholding_rates_2026=Use WH-1603 tables 0/3/6% for 2026 withholding; Act 110 rates (1.99%/5.21%) apply at the 2026 annual return only]] [US-SCS5-004]
- [[FACT:practice.va.std_deduction_2027_not_modelled=Statute: 2027 standard deduction 9,200/18,400; do not model 2027 withholding until Virginia Tax publishes the 2027 formula (guide Rev. 10/26 says the deduction sunsets - wrong)]] [US-VAS5-018]
- [[FACT:practice.wi.use_w166_tables=Withholding uses W-166 schedule (3.54/4.65/5.30/7.65%), not the assessment brackets (3.50/4.40/5.30/7.65%)]] [US-WIS5-010]

---

## PART 7 — Self-review

- Flags declared with their values: 23. Gates on a flag: 21; each compares a flag against a value of its declared list.
- Every wage-type code and Data Dictionary field named in this design exists in the approved catalogue and dictionary.
- Every rate, ceiling and threshold is a bound value; values of another period are written with their period.
- Every limitation is written *Not configured in this release* with its identifier; none carries a value.
- No State-level rule for a special population is configured: a scope statement under the owner decision.

