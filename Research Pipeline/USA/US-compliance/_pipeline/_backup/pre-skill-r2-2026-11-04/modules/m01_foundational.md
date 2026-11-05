# Module 1: Foundational Jurisdictional Parameters
*Purpose: To establish the core environmental settings that govern all payroll operations.*

## 1.0 How the United States payroll system is organised

The United States is not one payroll jurisdiction but a stack of parallel layers. Every employee is routed to one federal core, one or more State layers and, in some places, a local layer; each layer computes its own amounts on its own base and is remitted to its own authority on its own return.

| Layer | What the employer computes | Legal anchor (fact) |
|---|---|---|
| Federal income tax | Withholding under tables and procedures prescribed by the Secretary; covers federal tax only | `fed.fit.legal_basis.withholding_statute` [US-FED-012] |
| Federal social insurance (FICA) | Employee and employer OASDI and Medicare, reported on the quarterly return | `fed.fica.return_period` [US-FED-015] |
| Federal unemployment (FUTA) | Employer-only tax of [[FACT:fed.futa.rate.gross=6]]% gross on wages paid in the calendar year, credited for State unemployment contributions | `fed.futa.legal_basis.rate_statute` [US-FED-013]; `fed.futa.legal_basis.state_credit` [US-FED-014]; `fed.futa.rate.gross` [US-FED-007] |
| State layer (50 States and the District of Columbia) | State income-tax withholding where the State taxes wages; State unemployment insurance (SUI); in some States disability, paid-leave or other payroll programmes | per-State annexes `annex_XX` |
| Local layer | City, county, school-district or transit taxes in a minority of States | coverage row `local_regimes` [US-PAS5-022, US-MIR3-002, US-INS5-009, US-MULTIS5-011]; Module 6 §6.2 |

**The FLSA is a floor, not a ceiling.** Where a State or municipality sets a more protective standard the employer applies it: [[FACT:multi.wage_hour.overlay_rule=FLSA does not excuse a higher State/municipal minimum wage, a lower maximum workweek or a stricter child-labour standard: apply the more protective standard of the place where the work is performed]] [US-MULTIS5-008].

**States without a wage income tax.** The following States levy no income tax on wages in 2026; payroll in these States carries federal withholding, FICA, FUTA and the State programmes only.

| State | No wage income tax | Effective | Source |
|---|---|---|---|
| Alaska | none levied | from 2026-01-01 | `ak.no_wage_tax` [US-AKWT-002] |
| New Hampshire | none levied | from 2026-01-01 | `nh.no_wage_tax` [US-NHP9W-003] |
| Nevada | none levied | from 2026-01-01 | `nv.no_wage_tax` [US-NV-001] |
| South Dakota | none levied | from 2026-01-01 | `sd.no_wage_tax` [US-SD-001] |
| Tennessee | none levied | from 2021-01-01 | `tn.no_wage_tax` [US-TN-001] |
| Texas | none levied | from 2019-11-05 | `tx.no_wage_tax` [US-TXS5-001] |
| Washington | none levied | from 2026-01-01 to 2027-12-31 | `wa.no_wage_tax` [US-WAS5-017] |
| Florida | none levied | from 2026-01-01 | `fl.pit.exists` [US-FL-001] |
| Wyoming | none levied | from 2026-01-01 | `wy.pit.exists` [US-WYP51-001] |

Washington: no wage income tax to 2027-12-31 [US-WAS5-017]. An enacted tax of [[FACT:wa.pit.high_income_tax.rate=9.9]]% on individuals with adjusted gross income above USD [[FACT:wa.pit.high_income_tax.agi_threshold=1,000,000]] applies from 2028-01-01; it operates at assessment and is not modelled for payroll [US-WAS5-017].

**Live federal change.** Two Mobile Workforce bills are drafts and must not be modelled: [[FACT:multi.mobile_workforce_bill.senate=S. 1443 (introduced 2025-04-10, Senate Finance): DRAFT, NOT ENACTED - do not model]] [US-MULTIS5-020]; [[FACT:multi.mobile_workforce_bill.house=H.R. 10271 (introduced 2026-09-03, House Judiciary): DRAFT, NOT ENACTED - do not model]] [US-MULTIS5-025].

**Calculation oracle.** [[FACT:fed.oracle.source=IRS Pub. 15-T (2026): only two worked examples (NRA weekly 300 -> 31; tribal 6,000 -> 584.09); Stage 9b re-derives from Worksheet 1A + Annual Percentage Method tables]] [US-FED-027]. [[FACT:fed.oracle.estimator_not_oracle=IRS Tax Withholding Estimator is an employee tool, not an employer withholding engine - not an oracle]] [US-FED-021]. State oracles are listed in Module 12.

**Scope of this guide.** Private-sector employers and their common-law employees. Independent contractors and Form 1099-NEC reporting are out of scope (owner instruction of 2026-10-29) [US-OWN-008]. All special employee populations are in scope at the federal layer (owner decision US-OWN-005); State-level rules for special populations are deferred to a later round (US-OWN-005). The federal treatment of each population is in Module 11.

### Tier verdict (build manifest)

Repeated verbatim from the build manifest (tier classification).

**Overall:** T4

| Domain | Tier |
|---|---|
| federal_income_tax | T2 |
| fica_social_security_medicare | T2 |
| futa | T3 |
| state_income_tax | T4 |
| local_income_tax | T4 |
| state_unemployment_insurance | T4 |
| sdi_tdi_pfml | T4-shaped |
| workers_compensation | data-problem |
| multistate | T4 |
| labour_code | T3 |
| payslip_statute | T3 |
| statutory_reporting | T4 |
| leave | T3 |
| termination | T3 |
| benefits_in_kind | T2 |
| deductions_garnishments | T3 |
| collective_agreements | T1 |
| indexation | T3 |
| payroll_data_protection | T2 |
| live_legal_change | T3 |
| employer_payroll_levies | T4-shaped |

> **Rationale (verbatim):** Overall T4 (discriminator confirmed 2026-10-29 on source-read evidence; per-jurisdiction census completed at seal attempt 3 and re-checked at seal attempts 4, 5 and 6, 2026-10-30 to 2026-11-02; mandate sealed 2026-11-02 with all 65 questions answered; the limbs reopened and closed at seal attempt 6 (US-MQ-26 CT, US-MQ-45 MS, US-MQ-57 OR) bear on no tier; Stage-5 re-check 2026-11-02: superseded citations re-pointed to their S5 successors, census unchanged (new local layers found only inside T4 states: Lexington KY, Greenwood Village and Glendale CO OPT), and the five prevailing-wage limbs reopened that day (US-MQ-30 GA, 32 IA, 45 MS, 47 NC, 64 UT) and closed at the reseal the same day bear on no tier). Employer-operation test: T4 requires a second independent calculation AND a separate remittance/return to a second authority. Federal: 26 U.S.C. 3402(a)(1) obliges every employer to withhold federal income tax under IRS tables and covers federal tax only [US-FED-012]; FICA and FUTA go on federal returns 941/944/940 [US-FED-005, US-FED-007, US-FED-015]. State: a wage-taxing state imposes its own withholding computed on its own basis (e.g. Va. Code 58.1-461 [US-VAPIT-002]) remitted to the state revenue authority on its own returns (Virginia Tax VA-5/VA-6 [US-VAPIT-003]); state UI is a separate state tax base and agency (Fla. Stat. 443.1216 [US-MULTI-001]; SC Code ch. 41-31 [US-SCS5-015]). Nothing is absorbed into the federal deduction (contrast Switzerland, StHG Art. 36a Abs. 1, where one deduction discharges all levels). FUTA is federal but its credit depends on state UI paid and on the state's Title XII loan status (26 U.S.C. 3302(c)(2) [US-FED-014]): a cross-layer dependency, so futa is T3. Inside a state, a local layer is T4 where a locality receives a separate return (City of Portland Metro SHS / Multnomah PFA [US-ORS5-004]; Ohio municipal income tax, ORC 718.03 [US-OHP52-003]; Pennsylvania Act 32 EIT/LST to the local collector [US-PA-004]; Jersey City and Newark employer payroll taxes on quarterly city returns [US-NJP6-001, US-NJP6-002]) and T3 where it is piggybacked on the state return (Maryland county tax on MW506 [US-MDP51-001]; NYC and Yonkers on NYS-45/NYS-1 [US-NY-008]). Consequence: the federal core and each jurisdiction are declared and scoped as parallel layers, and the multistate domain routes each employee to one or more of them. Jurisdiction annexes (re-checked 2026-10-30, seal attempt 5): 9 T1 (no state wage tax; SUI and levies only: AK, FL, NH, NV, SD, TN, TX, WA, WY; WA declares the Seattle payroll expense tax, a threshold-conditional employer tax on a city return [US-WAP51-001], as a T4-shaped element), 31 T3 (state withholding, local layer absent or piggybacked on the state return), 11 T4 (local layer remitted to the locality on its own return: AL occupational taxes [US-ALP51-001], CO Denver OPT [US-COP52-001], DE Wilmington [US-DEP52-001], KY occupational taxes [US-KYP52-002], MI 23 self-administering cities [US-MIP52-002], MO St. Louis/Kansas City [US-MOP52-006], NJ Jersey City/Newark employer payroll taxes filed with the city [US-NJP6-001, US-NJP6-002], OH [US-OHP52-003], OR [US-ORS5-004], PA [US-PA-004], WV municipal service fees withheld and remitted to the city, W. Va. Code 8-13-13 [US-WVR3-001], Charleston [US-WVR3-002]); 0 unclassified; no classification rests on MANUAL/gated evidence.

## 1.1 Fiscal, Currency, and Language

### What is the statutory tax year?

The calendar year. Wage statements are prepared on a calendar-year basis: [[FACT:fed.tax_year.basis=calendar year (W-2 on calendar-year basis)]] [US-FED-006]. FUTA is levied on [[FACT:fed.futa.legal_basis.rate_statute=26 U.S.C. 3301: 6 percent of total wages paid during the calendar year]] [US-FED-013], and the FICA and withholding return period is [[FACT:fed.fica.return_period=calendar quarter (Form 941); agricultural labor annual; Form 944 annual option]] [US-FED-015].

| Element | Period | Fact |
|---|---|---|
| Federal withholding, FICA, W-2 | Calendar year (1 January to 31 December) | `fed.tax_year.basis` [US-FED-006] |
| FUTA annual wage base | Calendar year, per employer | `fed.futa.wage_base` [US-FED-007] |
| Quarterly returns | Calendar quarter | `fed.fica.return_period` [US-FED-015] |
| State income-tax and SUI years | Per State annex | `annex_XX` |

### Can employers adopt an alternate tax year? If yes, under what circumstances and what are the implications?

No for payroll purposes. Every payroll-tax period carried in the facts is fixed to the calendar year or the calendar quarter (`fed.tax_year.basis` [US-FED-006]; `fed.fica.return_period` [US-FED-015]; `fed.futa.legal_basis.rate_statute` [US-FED-013]), and no fact provides an employer election of a different payroll tax year. This is the mandate answer US-MQ-01 (build manifest `_year_note`: calendar year, no fiscal-year option). A corporate fiscal year chosen for income-tax accounting does not move any payroll period. Implication for configuration: the payroll year, every annual wage base and every year-to-date accumulator reset on 1 January.

### What is the official currency for payroll processing and reporting? Provide the ISO code.

United States dollar, ISO 4217 code **USD**, 2 minor units (build manifest `currency`, `currency_minor_units`). Payroll and all federal and State filings are in the same currency; no reporting currency differs from the payroll currency.

### What is the official language for statutory reports and employee payslips?

English. [[FACT:fed.language.official=English designated official language (presidential action 2025-03-01); no obligation on private employers]] [US-FED-020].

| Document | Language rule | Basis |
|---|---|---|
| Employee pay statement | English | Owner decision US-OWN-006 (payslip language rule) |
| Authority-facing filings (IRS, SSA, State agencies) | English | Owner decision US-OWN-006 (authority-facing language rule) |
| Notices and posters in certain States | English plus Spanish or the employee's primary language where a State statute requires it | Owner decision US-OWN-006 (State notice seams); not a payroll-calculation item |

No source read in the mandate census requires the pay statement itself in a language other than English; bilingual documents are permitted (`languages._bilingual_documents_permitted`).

## 1.2 Pay Cycles and Dates

### What are the permissible payroll payment frequencies in the country?

Federal law sets no minimum pay frequency in the facts; the federal withholding tables support the following pay periods per year: [[FACT:fed.fit.pay_periods_per_year=2 / 4 / 12 / 24 / 26 / 52 / 260 (semiannual, quarterly, monthly, semimonthly, biweekly, weekly, daily)]] [US-FEDS5-001]. The binding minimum frequency and the maximum lag between period end and payday are State law. The work-location State's rule applies.

| State | Statutory pay-frequency rule | Fact |
|---|---|---|
| AK | [[FACT:ak.pay_frequency.rule=monthly or semi-monthly at the employee's election (AS 23.05.140(a))]] | [US-AKS5-001] |
| AR | [[FACT:ar.pay_frequency.rule=corporations pay semimonthly; corporations with gross income >= 500,000 may pay FLSA-exempt managers earning > 25,000 at least monthly (11-4-401)]] | [US-ARP51-004] |
| AZ | [[FACT:az.pay_frequency.rule=two or more fixed paydays a month, no more than 16 days apart; monthly allowed for FLSA-exempt staff of out-of-state employers with centralized payroll; up to 5 days held back; OT due within 16 days after period]] | [US-AZS5-001] |
| CA | [[FACT:ca.pay_frequency.rule=twice a month: 1st-15th paid 16th-26th; 16th-end paid 1st-10th next month; EAP monthly by 26th; weekly/biweekly/semimonthly within 7 days of period close; OT by next regular payday (Lab. Code 204)]] | [US-CAS5-009] |
| CO | [[FACT:co.pay_frequency.rule=period no longer than one calendar month or 30 days; payday no later than 10 days after period close unless agreed (8-4-103(1)(a)); paydays posted]] | [US-COS5-002] |
| CT | [[FACT:ct.pay_frequency.rule=weekly or biweekly regular payday designated in advance; period ends no more than 8 days before payday; Commissioner waiver never less than monthly]] | [US-CTS5-004] |
| DC | [[FACT:dc.pay_frequency.rule=at least twice per calendar month on paydays designated in advance; EAP or contract/custom monthly; at most 10 working days from period end to payday]] | [US-DCS5-002] |
| DE | [[FACT:de.pay_frequency.rule=at least once per calendar month on paydays designated in advance; due within 7 days of period close; nonwork-day payday moves earlier (1102)]] | [US-DES5-002] |
| GA | [[FACT:ga.pay_frequency.rule=at least semi-monthly in two equal periods per month; officers/superintendents/department heads monthly (34-7-2)]] | [US-GAP9L-001] |
| HI | [[FACT:hi.pay_frequency.rule=at least twice each calendar month on designated paydays; monthly only by secret-ballot majority (2 years) or director permission; due within 7 days after period end (15 with permission)]] | [US-HIS5-007] |
| IA | [[FACT:ia.pay_frequency.rule=at least monthly, semimonthly or biweekly on designated paydays; payday at most 12 days after period end excluding Sundays/holidays; written agreement may vary; commissions true-up at least every 12 months (91A.3(1))]] | [US-IAS5-002] |
| ID | [[FACT:id.pay_frequency.rule=at least once per calendar month on designated paydays; period ends <= 15 days before payday; nonworkday payday moves earlier; pattern of late pay up to 500 per period (45-608)]] | [US-IDS5-004] |
| IL | [[FACT:il.pay_frequency.rule=at least semi-monthly, paid within 13 days after period end; EAP and commissions monthly (115/3)]] | [US-ILS5-003] |
| IN | [[FACT:in.pay_frequency.rule=at least semimonthly, or biweekly on request; pay covers wages up to no more than 10 business days before payday (IC 22-2-5-1)]] | [US-INS5-003] |
| KS | [[FACT:ks.pay_frequency.rule=at least once per calendar month on designated paydays; period ends no more than 15 days before payday (44-314)]] | [US-KSS5-013] |
| KY | [[FACT:ky.pay_frequency.rule=at least semimonthly; pay covers wages to a day not more than 18 days before payday; absent employee within 6 days of demand; EAP excluded]] | [US-KYS5-004] |
| LA | [[FACT:la.pay_frequency.rule=notice at hire of wage, method and frequency; undesignated paydays 1st and 16th; manufacturing/oil-boring/mining 10+ and public-service corporations at least twice monthly; FLSA-exempt outside; fine 25-250/day (23:633)]] | [US-LAS5-004] |
| MD | [[FACT:md.pay_frequency.rule=at least every 2 weeks or twice a month (EAP less often); nonworkday payday moves to preceding workday]] | [US-MDS5-008] |
| ME | [[FACT:me.pay_frequency.rule=intervals not exceeding 16 days; each payment covers wages to within 8 days of payday; closed-day payday moves to next business day; lengthening interval needs 30 days written notice; rate decrease needs prior notice]] | [US-MES5-004] |
| MI | [[FACT:mi.pay_frequency.rule=default semi-monthly (1-15 paid by 1st next month; 16-end by 15th); weekly/biweekly payday <= 14 days after period end; monthly within 15 days; December OT may go to next payday (MCL 408.472)]] | [US-MIS5-005] |
| MN | maximum interval between paydays: [[FACT:mn.labour.pay_frequency.max_days=31]] days | [US-MNS5-005] |
| MO | [[FACT:mo.labour.pay_frequency.corporations=at least semimonthly, within 16 days of period close]] | [US-MOP52-002] |
| MS | [[FACT:ms.labour.pay_frequency.scope=manufacturers 50+ employing public labor: biweekly or semimonthly; public service corporations: semimonthly]] | [US-MSS5-015] |
| NC | [[FACT:nc.labour.pay_frequency.allowed=daily; weekly; biweekly; semimonthly; monthly]] | [US-NCS5-005] |
| ND | [[FACT:nd.pay_frequency.rule=at least once each calendar month on regular paydays]] | [US-NDS5-005] |
| NE | [[FACT:ne.pay_frequency.rule=regular paydays set by employer or agreement; no statutory minimum frequency; 30 days notice to change]] | [US-NES5-006] |
| NJ | [[FACT:nj.pay_frequency.rule=at least twice each calendar month; period ends max 10 working days before payday]] | [US-NJS5-001] |
| NM | [[FACT:nm.pay_frequency.rule=paydays max 16 days apart; days 1-15 by 25th; 16-end by 10th of next month]] | [US-NMP8-001] |
| NV | [[FACT:nv.pay_frequency.rule=at least semimonthly (by 15th / last day of month)]] | [US-NVS5-001] |
| NY | [[FACT:ny.labour.pay_frequency.manual=weekly, max 7 days after week end]] | [US-NYS5-003] |
| OH | [[FACT:oh.pay_frequency.rule=at least semimonthly (1-15 by 1st of next month; 16-end by 15th)]] | [US-OHS5-015] |
| OK | [[FACT:ok.pay_frequency.rule=at least twice each calendar month; payday max 11 days after period end (+3 grace)]] | [US-OKS5-003] |
| OR | maximum interval between paydays: [[FACT:or.labour.pay_frequency.max_days=35]] days | [US-ORS5-006] |
| RI | [[FACT:ri.pay_frequency.rule=weekly (unless fixed at biweekly/semi-monthly/monthly/yearly rate); payday within 9 days of period end]] | [US-RIS5-004] |
| SD | [[FACT:sd.pay_frequency.rule=at least once each calendar month or regular designated paydays]] | [US-SDS5-001] |
| TN | [[FACT:tn.pay_frequency.rule=employers with 5+ employees: regular paydays at least monthly]] | [US-TNS5-001] |
| TX | [[FACT:tx.pay_frequency.rule=FLSA-exempt at least monthly; others at least twice a month (default 1st and 15th)]] | [US-TXS5-004] |
| UT | [[FACT:ut.pay_frequency.rule=at least semimonthly within 10 days after period close; yearly salary monthly by 7th]] | [US-UTP6-001] |
| VA | [[FACT:va.pay_frequency.rule=salaried at least monthly; hourly at least biweekly or twice a month]] | [US-VAS5-003] |
| VT | [[FACT:vt.pay_frequency.rule=weekly by default (wages to max 6 days before payday); biweekly/semimonthly after notice]] | [US-VTS5-002] |
| WA | [[FACT:wa.pay_frequency.rule=at least monthly; pay day max 10 days after period end for shorter periods]] | [US-WAS5-004] |
| WI | [[FACT:wi.pay_frequency.rule=at least monthly, wages to a day max 31 days before payment]] | [US-WIS5-004] |
| WV | [[FACT:wv.pay_frequency.rule=at least twice a month, max 19 days between paydays; wages earned to 12th day before payday]] | [US-WVS5-009] |
| WY | [[FACT:wy.labour.pay_frequency.semimonthly_industries=railroads, mines, refineries, oil and gas, factories, mills, workshops: semimonthly (1-15 by 1st; rest by 15th)]] | [US-WYS5-002] |
| MT | Prevailing-wage work only: [[FACT:mt.prevailing_wage.pay_frequency=weekly]] | [US-MTS5-011] |

Not configured in this release [[GAP:RQ-550]]: No official source read for this release gives a general pay-frequency rule for AL, FL, MA, MT, NH, PA, SC (Montana only for prevailing-wage work), and no federal statement that federal law sets none.

### For each frequency, detail the corresponding statutory reporting and payment deadlines for both income tax withholding and social security contributions.

At the federal layer the deposit deadline does **not** depend on the pay frequency. Federal income tax withheld and both shares of FICA are deposited together on one schedule fixed by the employer's lookback-period liability; the pay frequency only determines the paydays that start each deposit clock.

| Obligation | Rule | Fact |
|---|---|---|
| Lookback period for 2026 | [[FACT:fed.deposit.lookback_period=2024-07-01 to 2025-06-30 (Form 941 filers); CY2024 for 943/944/945 filers]] | [US-FEDS5-004] |
| Monthly depositor | Lookback liability of USD [[FACT:fed.deposit.monthly_max_lookback_liability=50,000]] or less: deposit by the 15th of the following month. Above it: semiweekly (Wednesday, Thursday or Friday paydays deposit by the following Wednesday; Saturday to Tuesday paydays by the following Friday) | [US-FEDS5-004] |
| Next-day rule | USD [[FACT:fed.deposit.next_day_threshold=100,000]] or more accumulated on any day: deposit by the next business day; deposit holidays are District of Columbia legal holidays | [US-FEDS5-004] |
| Quarterly return (FIT + FICA) | [[FACT:fed.form941.frequency=quarterly; due last day of the month after the quarter; amounts in cents]] (register row partial) | [US-FEDS5-031] |
| Annual Form 944 | Only on written IRS notice; liability ceiling USD [[FACT:fed.form944.max_liability=1,000]] (register row partial) | [US-FEDS5-031] |
| FUTA deposit | Deposit for a quarter when accumulated liability exceeds USD [[FACT:fed.futa.deposit_threshold=500]] (register row partial) | [US-FEDS5-031] |
| FUTA annual return | [[FACT:fed.form940.due=January 31 (10 more days if all FUTA deposited on time)]] (register row partial) | [US-FEDS5-031] |
| W-2 to SSA and employees, tax year 2026 | [[FACT:fed.w2.due_date=2027-02-01]] | [US-FEDS5-007] |
| State unemployment | [[FACT:multi.ui_wage_report.routing=UI quarterly wage report to the sui_state only (localization); State income-tax withholding returns to every State where withholding applies]] | [US-MULTIS5-017] |
| State income-tax withholding deposits and returns | Per State annex and Module 10 | `annex_XX` |

### Describe the statutory rule for handling pay dates that fall on a weekend or public holiday.

There is no federal rule in the facts. Where a State statute addresses it, the work-location State's rule applies:

| State | Rule (extract of the State pay-frequency fact) | Fact |
|---|---|---|
| DE | nonwork-day payday moves earlier | `de.pay_frequency.rule` [US-DES5-002] |
| ID | nonworkday payday moves earlier | `id.pay_frequency.rule` [US-IDS5-004] |
| MD | nonworkday payday moves to preceding workday | `md.pay_frequency.rule` [US-MDS5-008] |
| ME | closed-day payday moves to next business day | `me.pay_frequency.rule` [US-MES5-004] |

Federal deposit deadlines that fall on a deposit holiday move as stated in `fed.deposit.next_day_threshold` [US-FEDS5-004] (deposit holidays are District of Columbia legal holidays).

Not configured in this release [[GAP:RQ-551]]: The payday-on-a-non-working-day rule is established for DE, ID, MD and ME only; the other States and the federal position are not established from an official source.

### What are the common payroll pay dates and cut-off dates for payroll processing?

Statutory windows drive the calendar: several States fix the payday window by statute (for example `ca.pay_frequency.rule` [US-CAS5-009], `oh.pay_frequency.rule` [US-OHS5-015], `mi.pay_frequency.rule` [US-MIS5-005], `nm.pay_frequency.rule` [US-NMP8-001], `tx.pay_frequency.rule` [US-TXS5-004]). The cut-off date is the last day of the pay period allowed by the work-location State's maximum lag (table above).

Not configured in this release [[GAP:RQ-552]]: Common (non-statutory) US pay dates and processing cut-offs by frequency are not established from an official source.

## 1.3 Extra Pay Period Handling

### Describe the statutory handling and calculation adjustments required for fiscal years containing extra pay periods (e.g., 53 weekly pays).

The federal method annualises each payment with the number of pay periods of its frequency ([[FACT:fed.fit.pay_periods_per_year=2 / 4 / 12 / 24 / 26 / 52 / 260 (semiannual, quarterly, monthly, semimonthly, biweekly, weekly, daily)]]; [US-FEDS5-001]). A calendar year with 53 weekly paydays (or 27 biweekly paydays) does not change that divisor:

- Rule: [[FACT:fed.fit.extra_pay_period.rule=No IRS rule adjusts withholding for a 27th biweekly or 53rd weekly payday: Pub. 15-T Worksheet 1A annualises each payment with the Table 3 count for the payroll period (weekly 52, biweekly 26), and Pub. 15 sec. 8 requires withholding for the regular payroll period, so the extra payday is withheld as one more ordinary period. FICA and FUTA: wages are counted when paid, against the 2026 annual bases for wages paid in 2026.]] [US-FEDQ1-007].
- Configuration: keep the pay-period count of the frequency (no 53 / 27 divisor); the extra payday is one more ordinary payroll period for income-tax withholding.

### Detail the impact on annualized tax calculations and social security contributions.

Social insurance is unaffected in method: the OASDI, FUTA and SUI bases are annual amounts applied to wages **paid** in the calendar year (coverage row `accrual_vs_payment` [US-FED-003, US-FED-006, US-MULTIS5-009, US-MAS5-012]). An extra payday falls in the year in which it is paid and counts toward that year's bases (OASDI USD [[FACT:fed.fica.oasdi.wage_base=184,500]] for 2026; FUTA USD [[FACT:fed.futa.wage_base=7,000]] per employer). Income tax: each payday, including the extra one, is withheld as a regular payroll period with the normal annualisation [US-FEDQ1-007]; the year-end assessment on the employee's return settles any difference.

### If optional adjustment methods are permitted, provide a step-by-step guide.

No optional federal adjustment method exists: the IRS publications provide none for an extra payday [US-FEDQ1-007]. Steps: (1) keep the frequency's pay-period count in Worksheet 1A; (2) withhold the extra payday as an ordinary period; (3) apply FICA and FUTA to the wages paid, against the annual bases of the year of payment. State methods follow the State annex.

## 1.4 Holiday Calendar

### What are the official public holidays?

Federal legal public holidays: [[FACT:fed.holidays.legal_public=New Year's Day; Birthday of Martin Luther King, Jr.; Washington's Birthday; Memorial Day; Juneteenth National Independence Day; Independence Day; Labor Day; Columbus Day; Veterans Day; Thanksgiving Day; Christmas Day (11 legal public holidays)]] [US-FEDQ1-009]. Federal filing, furnishing and deposit dates roll forward under this rule: [[FACT:fed.deposit.due_date.non_business_day_rule=A filing, furnishing or deposit due date that falls on a Saturday, Sunday or legal holiday moves to the next business day; legal holiday = District of Columbia legal holiday; a statewide holiday never delays a federal deposit; semiweekly depositors get one extra day for each legal holiday in the 3 weekdays after the semiweekly period]] [US-FEDQ1-011].

| Holiday | 2026 observed date | 2027 observed date | Federal deposit / filing holiday |
|---|---|---|---|
| New Year's Day | [[FACT:fed.holiday.new_years_day.observed_date=2026-01-01]] [US-FEDQ1-011] | [[FACT:fed.holiday.new_years_day.observed_date=2027-01-01]] [US-FEDQ1-010] | 2026: yes (Pub. 15 2026 list); 2027: IRS list not yet published |
| Birthday of Martin Luther King, Jr. | [[FACT:fed.holiday.mlk_birthday.observed_date=2026-01-19]] [US-FEDQ1-011] | [[FACT:fed.holiday.mlk_birthday.observed_date=2027-01-18]] [US-FEDQ1-010] | 2026: yes (Pub. 15 2026 list); 2027: IRS list not yet published |
| Washington's Birthday | [[FACT:fed.holiday.washingtons_birthday.observed_date=2026-02-16]] [US-FEDQ1-011] | [[FACT:fed.holiday.washingtons_birthday.observed_date=2027-02-15]] [US-FEDQ1-010] | 2026: yes (Pub. 15 2026 list); 2027: IRS list not yet published |
| Memorial Day | [[FACT:fed.holiday.memorial_day.observed_date=2026-05-25]] [US-FEDQ1-011] | [[FACT:fed.holiday.memorial_day.observed_date=2027-05-31]] [US-FEDQ1-010] | 2026: yes (Pub. 15 2026 list); 2027: IRS list not yet published |
| Juneteenth National Independence Day | [[FACT:fed.holiday.juneteenth.observed_date=2026-06-19]] [US-FEDQ1-011] | [[FACT:fed.holiday.juneteenth.observed_date=2027-06-18]] [US-FEDQ1-010] | 2026: yes (Pub. 15 2026 list); 2027: IRS list not yet published |
| Independence Day | [[FACT:fed.holiday.independence_day.observed_date=2026-07-03]] [US-FEDQ1-011] | [[FACT:fed.holiday.independence_day.observed_date=2027-07-05]] [US-FEDQ1-010] | 2026: yes (Pub. 15 2026 list); 2027: IRS list not yet published |
| Labor Day | [[FACT:fed.holiday.labor_day.observed_date=2026-09-07]] [US-FEDQ1-011] | [[FACT:fed.holiday.labor_day.observed_date=2027-09-06]] [US-FEDQ1-010] | 2026: yes (Pub. 15 2026 list); 2027: IRS list not yet published |
| Columbus Day | [[FACT:fed.holiday.columbus_day.observed_date=2026-10-12]] [US-FEDQ1-011] | [[FACT:fed.holiday.columbus_day.observed_date=2027-10-11]] [US-FEDQ1-010] | 2026: yes (Pub. 15 2026 list); 2027: IRS list not yet published |
| Veterans Day | [[FACT:fed.holiday.veterans_day.observed_date=2026-11-11]] [US-FEDQ1-011] | [[FACT:fed.holiday.veterans_day.observed_date=2027-11-11]] [US-FEDQ1-010] | 2026: yes (Pub. 15 2026 list); 2027: IRS list not yet published |
| Thanksgiving Day | [[FACT:fed.holiday.thanksgiving_day.observed_date=2026-11-26]] [US-FEDQ1-011] | [[FACT:fed.holiday.thanksgiving_day.observed_date=2027-11-25]] [US-FEDQ1-010] | 2026: yes (Pub. 15 2026 list); 2027: IRS list not yet published |
| Christmas Day | [[FACT:fed.holiday.christmas_day.observed_date=2026-12-25]] [US-FEDQ1-011] | [[FACT:fed.holiday.christmas_day.observed_date=2027-12-24]] [US-FEDQ1-010] | 2026: yes (Pub. 15 2026 list); 2027: IRS list not yet published |
| District of Columbia Emancipation Day (not a 5 U.S.C. 6103 holiday) | [[FACT:fed.holiday.dc_emancipation_day.observed_date=2026-04-16]] [US-FEDQ1-011] | not in the research | 2026: yes (District of Columbia legal holiday) |

### Are there any regional, state-specific, or company-specific holidays?

Not configured in this release [[GAP:RQ-555]]: State legal holidays (which affect State deposit due dates and some State payday rules) are not established from an official source.
Company holidays are employer policy; no federal statute requires paid holidays for private employers (`fed.paid_leave.private_employers.exists` [US-FEDS5-026]).

## 1.5 Rounding and Precision Rules

### What are the statutory or common business practice rules for rounding final net pay and individual calculation components?

Federal: [[FACT:fed.fit.rounding=Optional: wages may be rounded to the nearest dollar and the period tax rounded to the nearest dollar (drop under 50 cents, 50-99 cents up)]] [US-FED-001]. No fact requires rounding of net pay; amounts are paid in cents (2 minor units). State withholding rounding is set State by State:

| Jurisdiction | Rounding rule | Fact |
|---|---|---|
| IA (withholding) | [[FACT:ia.wh.rounding=to the cent, half-up (no whole-dollar rounding in 2026)]] | [US-IAS5-005] |
| ID (withholding) | [[FACT:id.wh.rounding=nearest whole dollar]] | [US-IDS5-008] |
| KS (withholding) | [[FACT:ks.wh.rounding=percentage-method result may be rounded to nearest dollar (under 50c down, 50c+ up)]] | [US-KSS5-001] |
| KY (withholding) | [[FACT:ky.wh.rounding=employer may compute WAGES to nearest dollar (KRS 141.310(4)); no rounding rule for the tax]] | [US-KYS5-010] |
| MA (withholding) | [[FACT:ma.wh.rounding=wages may be computed to nearest dollar (830 CMR 62B.2.1(8))]] | [US-MAS5-023] |
| MN (withholding) | [[FACT:mn.pit.rounding=nearest dollar permitted]] | [US-MNP51-001] |
| MO (withholding) | [[FACT:mo.pit.rounding=per-period tax rounded to whole dollar (49c down, 50c up)]] | [US-MOS5-001] |
| NC (withholding) | [[FACT:nc.pit.rounding=nearest whole dollar (NRA add-on rounded up)]] | [US-NC-001] |
| ND (withholding) | [[FACT:nd.pit.rounding=nearest whole dollar; under 1.00 need not be withheld]] | [US-NDS5-001] |
| NY (withholding) | [[FACT:ny.pit.rounding=to the cent per tables or formula]] | [US-NY-001] |
| OK (withholding) | [[FACT:ok.pit.rounding=nearest whole dollar (49c down, 50c up); nothing if quarterly tax < 0.25]] | [US-OKS5-010] |
| OR (withholding) | [[FACT:or.pit.rounding=nearest dollar permitted, not required]] | [US-ORS5-009] |
| PA (withholding) | [[FACT:pa.pit.rounding=none published]] | [US-PAP52-002] |
| UT (withholding) | [[FACT:ut.pit.rounding=all lines to whole dollars, half up]] | [US-UTPIT-003] |
| WI (withholding) | [[FACT:wi.pit.rounding=none stated]] | [US-WIS5-011] |
| FL (unemployment) | [[FACT:fl.sui.rounding=contribution fraction under half a cent dropped; half a cent or more rounds up to 1 cent]] | [US-FLS5-004] |

Build rule: compute every intermediate at full precision and round each statutory amount once, half-up to the cent, unless the jurisdiction's rule above rounds to the dollar; apply the optional federal whole-dollar rounding only if the employer elects it and then consistently.

Not configured in this release [[GAP:RQ-226]]: Kentucky: the 2026 formula sheet shows a bi-weekly result rounded down to whole dollars, while KRS 141.310(4) rounds only wages; the per-period rounding of the tax is not established.

### What level of decimal precision is required for statutory reporting?

Cents on the quarterly federal return: [[FACT:fed.form941.amounts_in_cents=Form 941: do not round to whole dollars, always show cents]] [US-FED-005]. The annual wage statement file is a fixed-length record format ([[FACT:fed.efw2.record_length=512]]-byte records, [US-FEDS5-032]); money-field layout is in the Report Specs. State filings follow each State's specification (Report Specs, annexes).
