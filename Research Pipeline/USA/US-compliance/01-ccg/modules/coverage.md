## 11.3 Population Coverage Matrix

One row per population. All special employee populations are in scope at the federal layer (owner decision US-OWN-005); State-level rules for special populations are deferred to a later round (US-OWN-005). Each row gives the federal and multistate treatment, its effect on income tax, social security and reporting, the module that carries the rule, and the sources. State-specific treatments are in the annexes named in the row.

### Resident employee

*Status: answered. Rule carried in: Module 3; Module 5; Module 6.*

Ordinary employee. FIT per Form W-4 and the Pub. 15-T method. FICA employee and employer. FUTA and SUI employer-paid, SUI to the State of UI coverage. State income tax of the work State and, for residents working elsewhere, of the residence State under its own rule (credit, difference withholding or reciprocity).

| Effect on | Treatment |
|---|---|
| Income tax | FIT Pub. 15-T 2026 Worksheet 1A (line 1g [[FACT:fed.fit.worksheet1a.line1g.mfj=12,900]] MFJ); State withholding per annex |
| Social security | OASDI [[FACT:fed.fica.oasdi.rate.employee=6.2]]% + [[FACT:fed.fica.oasdi.rate.employer=6.2]]% up to [[FACT:fed.fica.oasdi.wage_base=184,500]]; Medicare [[FACT:fed.fica.medicare.rate.employee=1.45]]% + [[FACT:fed.fica.medicare.rate.employer=1.45]]%; Additional Medicare [[FACT:fed.fica.addl_medicare.rate=0.9]]% above [[FACT:fed.fica.addl_medicare.withholding_threshold=200,000]]; FUTA [[FACT:fed.futa.rate.net=0.6]]% on [[FACT:fed.futa.wage_base=7,000]]; SUI per the State of coverage ([[FACT:multi.sui.localization_test=One State covers the entire service with one employer, in order: (1) localized (entirely in the State, or out-of-state service incidental: temporary, transitory, isolated); (2) else some service in the base-of-operations State; (3) else some service in the State of direction or control; (4) else some service in the State of residence]]) |
| Reporting | Form 941 quarterly, 940 annual, W-2 by [[FACT:fed.w2.due_date=2027-02-01]]; State withholding and UI returns |

Sources: US-FEDS5-001 (Worksheet 1A); US-FEDS5-005 (941 lines 5a-5d); US-FEDS5-007 (W-2 2026); US-MULTIS5-017 (localization test).

### Non-resident employee

*Status: answered. Rule carried in: Module 6 (NRA, reciprocity, thresholds); Module 11.*

Two meanings. (a) **Nonresident alien of the US:** regular withholding with the Pub. 15-T add-on ([[FACT:fed.fit.nra.addon.table2.annual=16,100]] per year, Table 2); W-4 per Notice 1392; treaty-exempt wages via Form 8233 on Form 1042-S; commercial-traveler exception (at most [[FACT:fed.fit.nra.commercial_traveler.max_days=90]] days and [[FACT:fed.fit.nra.commercial_traveler.max_pay=3,000]]). (b) **Nonresident of a State:** work-State withholding subject to reciprocity certificates, day or dollar thresholds (e.g. Alabama [[FACT:al.nonres.safe_harbor.days=30]] days, Louisiana [[FACT:multi.nonresident.la.threshold_days=30]], West Virginia [[FACT:multi.nonresident.wv.threshold_days=30]], Arizona [[FACT:multi.nonresident.az.threshold_days=60]], Illinois [[FACT:multi.nonresident.il.threshold_days=30]] working days), convenience rules (New York: [[FACT:multi.convenience.ny.rule=20 NYCRR 132.18(a): nonresident allocates by NY working days / total working days; days outside NY count only if worked of NECESSITY; home-office days are NY days unless the home is a bona fide employer office]]), and the federal limits for transport workers and military spouses.

| Effect on | Treatment |
|---|---|
| Income tax | Add-on for withholding only; 1042-S for treaty-exempt wages; State nonresident sourcing per Module 6 |
| Social security | The add-on has no FICA or FUTA effect: FICA is computed on actual wages, as for residents. For State nonresidents SUI follows the localization test, not residence |
| Reporting | W-2 (or 1042-S for treaty-exempt wages: [[FACT:fed.form1042s.channel=IRIS (FIRE retired for TY2026); due 2027-03-15]]); State nonresident withholding on the work-State return; W-2 boxes 15-20 for up to [[FACT:multi.w2.states_per_form=2]] States |

Sources: US-FEDS5-002 (NRA adjustment tables 1-2); US-FEDS5-016 (Pub. 515 pay for personal services); US-MULTIS5-017 (localization test); US-MULTI-021 (AL 30-day); US-MULTIS5-013 (NY convenience).

### Fixed term contract

*Status: answered. Rule carried in: Module 9.*

No federal or general State fixed-term regime: employment is at will, and a fixed term is a matter of contract. Payroll treats a fixed-term worker as any employee. Expiry of the term is a separation and triggers the work State's final-pay rule ([[FACT:fed.final_pay.rule=No federal immediate final-pay rule; wages due by the regular payday; timing and vacation payout are state law]]).

| Effect on | Treatment |
|---|---|
| Income tax | None: same withholding as any employee |
| Social security | None: FICA, FUTA and SUI unchanged; UI benefit eligibility on separation is State law |
| Reporting | Separation: State final pay (Module 9, Table 9.1.1) and any State separation notice (e.g. Tennessee within [[FACT:tn.term.separation_notice.hours=24]] hours); W-2 as usual |

Sources: US-SDS5-010 (at-will; final wages); US-TNS5-012 (employment at will); US-FEDS5-025 (federal final pay).

### Part time

*Status: answered. Rule carried in: Module 4; Module 10.*

No federal part-time regime: the FLSA minimum wage ([[FACT:fed.minwage.hourly=7.25]]) and the 40-hour overtime rule apply per hour and per workweek whatever the schedule. Part-time hours count toward the ACA full-time-equivalent test (applicable large employer at [[FACT:fed.aca.ale.fte_threshold=50]] (partial source)). State paid-sick-leave accrual is per hour worked (Module 8).

| Effect on | Treatment |
|---|---|
| Income tax | None: same withholding method, by pay period |
| Social security | None: FICA from the first dollar; SUI and PFML per State (some States have hours-based coverage) |
| Reporting | ACA: FTE count for ALE status (1094-C/1095-C); State UI reports with hours where required (e.g. Washington) |

Sources: US-FEDS5-017 (FLSA 206); US-FEDS5-018 (FLSA 207); US-FEDS5-012 (ALE 50 incl. FTE).

### Officers without employment contract

*Status: answered. Rule carried in: Module 11.*

Corporate officers are employees for payroll: wages take FIT withholding, FICA and FUTA. State law includes corporate officers as employees for withholding (Oklahoma) and UI coverage (Florida). Directors' fees and partner or sole-proprietor draws are not wages (self-employment, outside payroll). Statutory employees: [[FACT:fed.statutory_employee.treatment=FICA withheld, no FIT withholding; W-2 box 13 checked; FUTA for drivers and traveling salespersons only]].

| Effect on | Treatment |
|---|---|
| Income tax | Officer wages: FIT withholding as any employee |
| Social security | FICA and FUTA on officer wages; SUI covers corporate officers (e.g. Florida); some States allow officer exclusions (annexes) |
| Reporting | W-2 as any employee; statutory employees W-2 box 13 |

Sources: US-OKS5-010 (2385.1 employee incl. corporate officers); US-FLS5-005 (443.1216(1)(a)); US-FEDR3-005 (statutory employees).

### Apprentices and trainees

*Status: answered. Rule carried in: Module 4; Module 11.*

No federal apprentice payroll regime: the FLSA minimum wage applies (a sub-minimum only under DOL certificates). Students: [[FACT:fed.students.treatment=Private school/college students: FIT withheld, FICA and FUTA exempt; public school: FICA exempt unless sec. 218 agreement; work-experience full-time student: FICA taxable]]. States set learner rates (California, Washington: annexes).

| Effect on | Treatment |
|---|---|
| Income tax | FIT withheld as any employee |
| Social security | Student exemptions from FICA and FUTA as listed; State UI student exclusions (annexes) |
| Reporting | W-2 as usual |

Sources: US-FEDS5-029 (sec. 15 special classes (students)); US-CAS5-006 (learners 85%); US-WAS5-006 (youth 85%).

### Maternity, paternity and parental leave

*Status: answered. Rule carried in: Module 8; Module 5.*

No federal paid parental leave for private employers. FMLA gives up to [[FACT:fed.fmla.weeks=12]] workweeks of job-protected leave (may be unpaid). Paid leave comes from the State PFML/TDI programmes. Premiums are withheld or paid through payroll (e.g. Washington [[FACT:wa.pfml.total.rate=1.13]]% in 2026, Massachusetts [[FACT:ma.pfml.total.rate=0.88]]%, District of Columbia [[FACT:dc.pfml.employer.rate=0.75]]% employer-only). Benefits are paid by the State or insurer (Module 8, Table 8.1.5).

| Effect on | Treatment |
|---|---|
| Income tax | State PFML benefits are not employer payroll; employee PFML contributions are W-2 wages |
| Social security | Employee and employer PFML contributions per State programme, capped as the State sets (Module 5) |
| Reporting | State PFML quarterly returns; W-2 box 14 per State practice |

Sources: US-FEDS5-026 (29 U.S.C. 2612); US-FEDS5-007 (PFML W-2 treatment); US-WAS5-015 (WA PFML rate); US-MAS5-012 (MA PFML rates).

### Work accident and occupational disease

*Status: answered. Rule carried in: Module 5; Module 7.*

Workers' compensation is State law and generally an insured employer cost outside payroll. Payroll touches it where a State levies a per-employee fee or allows an employee deduction (New Mexico fee on TRD-41431; Washington employee share of workers' compensation premiums). No federal payroll rule. Not configured in this release [[GAP:RQ-544]]: Only the New Mexico fee and the Washington employee deduction are established from official sources; other States that allow an employee workers' compensation deduction are not established.

| Effect on | Treatment |
|---|---|
| Income tax | None at payroll: workers' compensation benefits are not employer wages |
| Social security | New Mexico fee per covered employee per quarter (employer and employee parts); Washington employee deduction; no federal levy |
| Reporting | New Mexico TRD-41431 quarterly (fee + wage report); State annexes |

Sources: US-NMR3-001 (52-5-19 NMSA); US-FEDS5-029 (Pub. 15 sec. 15 (no federal WC rule listed)).

### Termination and final pay

*Status: answered. Rule carried in: Module 9.*

[[FACT:fed.final_pay.rule=No federal immediate final-pay rule; wages due by the regular payday; timing and vacation payout are state law]] (Module 9, Table 9.1.1; vacation payout Module 8, Table 8.1.3). Severance is wages for FIT, FICA and FUTA. WARN: [[FACT:fed.warn.notice_days=60]] days' notice for a plant closing or mass layoff; pay in lieu is wages. W-2 for a terminated employee: [[FACT:fed.w2.terminated_employee.furnishing=Terminated employee: W-2 no later than January 31 of following year (earlier on request)]].

| Effect on | Treatment |
|---|---|
| Income tax | Severance and pay in lieu are supplemental wages ([[FACT:fed.fit.supplemental.flat_rate=22]]% optional flat rate or aggregate) |
| Social security | Severance subject to FICA and FUTA |
| Reporting | W-2; State separation notices where required |

Sources: US-FEDS5-025 (DOL last paycheck; WARN 2102); US-FEDS5-029 (severance = wages); US-FED-016 (31.6051-1(a)(1)).

### Mid-month joiner and leaver

*Status: answered. Rule carried in: Module 2; Module 3.*

No federal proration rule: withholding is computed on the wages paid in the pay period with the period frequency of Pub. 15-T. A joiner files a W-4 (and the State certificate) at hire and is reported to the State Directory of New Hires within [[FACT:fed.newhire.deadline_days=20]] days (shorter in many States). A leaver receives final pay under State law. Wage bases run per employer per calendar year from the first payment.

| Effect on | Treatment |
|---|---|
| Income tax | Pub. 15-T per-period method on wages actually paid; no catch-up or proration |
| Social security | Wage bases start at the first payment by this employer in the calendar year (FUTA [[FACT:fed.futa.wage_base=7,000]]); successor-employer carry-over for FUTA |
| Reporting | New-hire report; W-2 for any part-year employee |

Sources: US-FEDS5-001 (pay-period tables); US-FEDS5-024 (653a(b)); US-MULTIS5-009 (3306(b)(1)).

### Annual regularisation

*Status: answered. Rule carried in: Module 10; Module 5.*

No employer year-end income-tax regularisation: the employee settles at assessment. The employer reconciles the quarterly 941s to the annual W-2/W-3, corrects with 941-X and W-2c, stops OASDI at the wage base and starts Additional Medicare above the threshold per employer. Excess OASDI from multiple employers is refunded at assessment, not by the employer.

| Effect on | Treatment |
|---|---|
| Income tax | None at payroll; W-4 exempt status renewed yearly ([[FACT:fed.w4.exempt.validity=2026 only: the exemption checkbox certification lapses; a new W-4 is required for 2027]]) |
| Social security | Per-employer annual bases (OASDI [[FACT:fed.fica.oasdi.wage_base=184,500]]; FUTA [[FACT:fed.futa.wage_base=7,000]]; SUI per State); Additional Medicare above [[FACT:fed.fica.addl_medicare.withholding_threshold=200,000]] |
| Reporting | W-2/W-3 by [[FACT:fed.w2.due_date=2027-02-01]] reconciled to four 941s; 940 annual; State annual reconciliations |

Sources: US-FEDS5-007 (W-2/W-3 2026); US-FEDS5-005 (Additional Medicare); US-FEDS5-006 (W-4 exempt expiry).

### Overtime

*Status: answered. Rule carried in: Module 4; Module 10.*

FLSA: [[FACT:fed.overtime.premium.multiplier=1.5]] × the regular rate above [[FACT:fed.overtime.weekly_threshold_hours=40]] hours in a workweek; no federal daily overtime. States add daily overtime (California: [[FACT:ca.overtime.rule=1.5x over 8 h/day, over 40 h/week and first 8 h of 7th consecutive day; 2x over 12 h/day and over 8 h on 7th day (Lab. Code 510); alternative workweek exceptions]]; Nevada for employees paid under [[FACT:nv.overtime.daily_threshold_wage=18]] per hour; others in the annexes). The P.L. 119-21 qualified-overtime deduction operates at assessment ([[FACT:fed.plaw119_21.qualified_overtime.level=assessment (employee return); withholding only via W-4 Step 4(b); employer reports W-2 Box 12 TT; overtime remains fully subject to FICA]]).

| Effect on | Treatment |
|---|---|
| Income tax | Overtime is regular wages for withholding; the deduction reaches withholding only via W-4 Step 4(b) |
| Social security | Fully subject to FICA, FUTA and SUI |
| Reporting | W-2 box 12 code TT ([[FACT:fed.w2.box12.new_codes=TP (cash tips reported to employer); TT (qualified overtime compensation); TA (employer Trump-account contributions)]]) |

Sources: US-FEDS5-018 (29 U.S.C. 207(a)(1)); US-FEDS5-030 (P.L. 119-21); US-CAS5-008 (Lab. Code 510).

### Multiple employers

*Status: answered. Rule carried in: Module 3; Module 5.*

Each employer withholds and applies the wage bases independently. The OASDI and FUTA bases are per employer (successor carry-over only on acquisition). Additional Medicare is triggered per employer. The employee coordinates FIT across jobs on W-4 Step 2: the line 1g amount ([[FACT:fed.fit.worksheet1a.line1g.mfj=12,900]] MFJ) is not subtracted when Step 2 is checked. Not configured in this release [[GAP:RQ-533]]: Common-paymaster relief for related employers (IRC 3121(s)) is not established from an official source.

| Effect on | Treatment |
|---|---|
| Income tax | W-4 Step 2 checkbox changes the schedule and line 1g |
| Social security | Per-employer OASDI, FUTA ([[FACT:fed.futa.wage_base=7,000]]) and SUI bases; excess OASDI refunded at assessment |
| Reporting | Separate W-2 per employer |

Sources: US-FEDS5-006 (Step 2); US-MULTIS5-009 (FUTA per employer); US-FEDS5-005 (Additional Medicare per employer).

### Local regimes

*Status: answered. Rule carried in: Module 6 (local); annexes PA, OH, MI, IN, MD, KY, NY, OR.*

Local income and payroll taxes exist in a minority of States and sit outside State reciprocity: Pennsylvania EIT and LST; Philadelphia wage tax ([[FACT:pa.local.philadelphia.resident.rate=3.74]] (2025-07-01 to 2026-06-30); [[FACT:pa.local.philadelphia.resident.rate=3.735]] (from 2026-07-01) resident); Ohio municipal and school-district taxes ([[FACT:oh.local.municipal_base=Ohio municipal income tax base = Medicare wages less 125 deductions; 401(k) deferrals taxable]]); Michigan city taxes (Detroit resident [[FACT:mi.local.detroit.rate.resident=2.4]]%); Indiana county tax ([[FACT:in.county.change_dates=County rates may change in January and October (DN#1 R47/10-26 from 2026-10-01)]]); Maryland county tax; Kentucky occupational taxes; NYC and Yonkers; Oregon transit and local levies. Per-locality detail is in the annexes.

| Effect on | Treatment |
|---|---|
| Income tax | Local withholding by residence and/or work locality per local rule; W-2 boxes 18-20 |
| Social security | Local transit and payroll levies (Oregon, New York MCTMT) per the levy scope |
| Reporting | Local returns per locality; W-2 boxes 18-20 for up to [[FACT:multi.w2.states_per_form=2]] localities |

Sources: US-PAS5-022 (Philadelphia wage tax); US-MIR3-002 (Detroit 5469); US-INS5-009 (county rate changes); US-MULTIS5-011 (W-2 boxes 15-20).

### Employer type and size

*Status: answered. Rule carried in: Module 10; Module 11.*

Size and type thresholds change obligations: ACA applicable large employer at [[FACT:fed.aca.ale.fte_threshold=50]] (partial source) full-time incl. equivalents (1094-C/1095-C, e-file at [[FACT:fed.aca.efile_threshold=10]]+); deposit schedule by lookback liability ([[FACT:fed.deposit.monthly_max_lookback_liability=50,000]] monthly/semiweekly; [[FACT:fed.deposit.next_day_threshold=100,000]] next day); household employers (FICA at [[FACT:fed.household.fica_cash_threshold=3,000]], FUTA at [[FACT:fed.household.futa_quarter_threshold=1,000]] per quarter); agricultural ([[FACT:fed.agricultural.per_worker_threshold=150]] / [[FACT:fed.agricultural.total_threshold=2,500]] tests); government employers ([[FACT:fed.government_employee.treatment=FIT withheld; no FUTA; FICA with sec. 218 / Medicare-only exceptions]]); State size tests (Massachusetts PFML employer share, Nebraska sick leave, Virginia paid sick leave: annexes and Module 8).

| Effect on | Treatment |
|---|---|
| Income tax | Household FIT only by agreement; agricultural FIT and FICA from the thresholds |
| Social security | Household and agricultural thresholds; Massachusetts PFML employer share depends on size |
| Reporting | ALE 1094-C/1095-C; Form 943/944/Schedule H routes |

Sources: US-FEDS5-012 (ALE); US-FEDS5-004 (deposit schedule); US-FEDS5-029 (household/government); US-MAS5-012 (MA PFML <25).

### Mid year rate change

*Status: answered. Rule carried in: Module 4; Module 6; Module 13.*

Several 2026 values change during the year and are applied by payment date (Module 11, Table 11.1.1): District of Columbia minimum wage ([[FACT:dc.minwage.hourly=17.95]] (2025-07-01 to 2026-06-30); [[FACT:dc.minwage.hourly=18.40]] (from 2026-07-01)); Oregon ([[FACT:or.labour.minwage.standard.hourly=15.05]] (2025-07-01 to 2026-06-30); [[FACT:or.labour.minwage.standard.hourly=15.55]] (2026-07-01 to 2027-06-30)); Ohio withholding tables from [[FACT:oh.wh.tables.effective_from=2026-08-01]]; Georgia withholding rate ([[FACT:ga.wh.rate=5.19]]% to 2026-05-10, [[FACT:ga.wh.rate=4.99]]% from 2026-05-11; assessment rate [[FACT:ga.pit.rate.flat=4.99]]% for tax year 2026, [[FACT:ga.live.hb463.status=in force (signed 2026-05-11, retroactive 2026-01-01); levels withholding + assessment (rate), assessment + reporting (subtractions)]]); Indiana county rates; Idaho tables; Philadelphia wage tax; Trump-account exclusion (from 2026-07-04).

| Effect on | Treatment |
|---|---|
| Income tax | Withholding tables effective by payment date |
| Social security | Rate changes on the effective date (no federal mid-year change in 2026) |
| Reporting | Quarterly returns split by period; W-2 annual totals |

Sources: US-DCS5-011 (32-1003); US-ORS5-002 (BOLI 2026-07-01); US-OHS5-001 (tables 2026-08-01); US-PAS5-022 (Philadelphia 2026-07-01); US-FEDS5-030 (Trump account 2026-07-04).

### Special pay cycles

*Status: answered. Rule carried in: Module 3; Module 6.*

Pub. 15-T supports these periods: [[FACT:fed.fit.pay_periods_per_year=2 / 4 / 12 / 24 / 26 / 52 / 260 (semiannual, quarterly, monthly, semimonthly, biweekly, weekly, daily)]]. Supplemental pay (bonus, commissions, severance): [[FACT:fed.fit.supplemental.flat_rate=22]]% optional flat rate or aggregate; [[FACT:fed.fit.supplemental.mandatory_rate=37]]% mandatory above [[FACT:fed.fit.supplemental.mandatory_threshold=1,000,000]] per year. State pay-frequency rules and State supplemental rates (California [[FACT:ca.wh.supplemental.rate.bonus_stock_options=10.23]]% bonus / [[FACT:ca.wh.supplemental.rate.other=6.6]]% other) are annex detail (Module 9, Table 9.2.1).

| Effect on | Treatment |
|---|---|
| Income tax | Supplemental methods; State supplemental rates |
| Social security | None: FICA on all wages including supplemental |
| Reporting | None specific |

Sources: US-FEDS5-003 (sec. 7 supplemental); US-FEDS5-001 (periods); US-CAS5-004 (DE 44 supplemental).

### Accrual versus payment

*Status: answered. Rule carried in: Module 3; Module 5.*

Federal payroll taxes follow the payment date ([[FACT:fed.tax_year.basis=calendar year (W-2 on calendar-year basis)]]): FIT, FICA and FUTA apply to wages paid in the calendar year (OASDI base for remuneration paid in 2026; FUTA [[FACT:fed.futa.wage_base=7,000]] per employer). Exception: Massachusetts PFML rates apply to wages earned on or after 1 January. A December-earned, January-paid wage takes the new year's rates and bases federally.

| Effect on | Treatment |
|---|---|
| Income tax | Withholding at payment; table year = payment date |
| Social security | Wage bases by payment date; Massachusetts PFML by earning date |
| Reporting | W-2 and 941 by payment date |

Sources: US-FED-003 (base for remuneration paid in 2026); US-FED-006 (calendar-year basis); US-MULTIS5-009 (paid in the calendar year); US-MAS5-012 (wages earned on/after Jan 1).
