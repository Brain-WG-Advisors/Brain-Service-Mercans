# Annex IA: Iowa


**Layer classification (T3).** T3: separate state withholding calculation and state return; no local layer, or a local layer piggybacked on the state return. Source: build manifest tier census, local income tax domain.

**Summary.** Minimum wage [[FACT:ia.minwage.hourly=7.25]] ([[FACT:ia.minwage.first_90_days.hourly=6.35]] first 90 days); local mandates void (364.3(12)); FLSA overtime. Flat 3.8% PIT; 2026 withholding formula T1=G-D, x3.80%, less W/P, + A, computed TO THE CENT (not whole dollar); supplemental 3.8%; reciprocity with IL only; school/EMS surtaxes at assessment. UI employer-only, base [[FACT:ia.sui.wage_base=20,400]] (2026) / [[FACT:ia.sui.wage_base=21,100]] (2027) after SF 607, max 5.4%, new [[FACT:ia.sui.new_employer.rate=1.0]]%; other-state wages do NOT count. Pay statement 91A.6. New hire within 15 days. Oracle: IDR formula PDF examples.

Each parameter row gives its key, the period in force and its legal basis: the legal-basis register row, the authority, the source tier and how the value was verified.

## IA.1 Employment and labour code

No state overtime rule: ch. 91D adopts FLSA (negative on 91D.1 only, 85%). HF 2212 not enacted.

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ia.late_wages.liquidated_damages_percent_per_day` | [[FACT:ia.late_wages.liquidated_damages_percent_per_day=5]] % | 2026-01-01 to open | US-IAS5-027 (Iowa Legislature; A.1, direct artifact inspection, confidence high) | 91A.2(6): excluding Sundays, holidays and first 7 days; capped at unpaid amount. |
| `ia.local_mandates.preempted` | [[FACT:ia.local_mandates.preempted=True]] | 2017-03-30 to open | US-IAS5-021 (Iowa Legislature; A.1, direct artifact inspection, confidence high) | 364.3(12): no city minimum/living wage, leave, benefits or scheduling ordinances. |
| `ia.minor.under16.school_week_max_hours` | [[FACT:ia.minor.under16.school_week_max_hours=28]] hours | 2026-01-01 to open | US-IAS5-014 (Iowa Legislature; A.1, direct artifact inspection, confidence high) | 92.7: 7am-9pm (11pm June-Labor Day); 8 h/day, 40 h/week; 6 h/day and 28 h/week in session; 30-min break for 5+ h. |
| `ia.minwage.first_90_days.hourly` | [[FACT:ia.minwage.first_90_days.hourly=6.35]] USD | 2008-01-01 to open | US-IAS5-001 (Iowa Legislature; A.1, direct artifact inspection, confidence high) |  |
| `ia.minwage.hourly` | [[FACT:ia.minwage.hourly=7.25]] USD | 2008-01-01 to open | US-IAS5-001 (Iowa Legislature; A.1, direct artifact inspection, confidence high) | 91D.1(1)(a),(b): or federal if higher; enterprises under 300,000 gross exempt (not laundries, construction, hospitals, care, schools, public agencies). Not indexed. |
| `ia.pay_frequency.rule` | [[FACT:ia.pay_frequency.rule=at least monthly, semimonthly or biweekly on designated paydays; payday at most 12 days after period end excluding Sundays/holidays; written agreement may vary; commissions true-up at least every 12 months (91A.3(1))]] | 2026-01-01 to open | US-IAS5-002 (Iowa Legislature; A.1, direct artifact inspection, confidence high) |  |
| `ia.payment.method` | [[FACT:ia.payment.method=US currency or negotiable instrument; in kind with written consent; direct deposit may be a condition of employment for hires from 2005-07-01 (3 exceptions); employer pays overdraft charges from late pay; expenses reimbursed within 30 days]] | 2026-01-01 to open | US-IAS5-002 (Iowa Legislature; A.1, direct artifact inspection, confidence high) |  |

Not configured in this release [[GAP:RQ-179]]: Negative rests on 91D.1 only.

## IA.2 Income tax withholding

Configuration rule: the federal tips and overtime deductions are conformed at assessment only (`ia.pit.obbba`). There is no withholding allowance for them; the withholding formula is unchanged.

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ia.pit.obbba` | [[FACT:ia.pit.obbba=tips, overtime, car-loan interest conformed at ASSESSMENT only (no withholding allowance); senior deduction (up to 6,000) may be claimed as an IA W-4 allowance]] | 2026-01-01 to open | US-IAS5-019 (Iowa Department of Revenue; A.2, quoted from authority page, confidence high) |  |
| `ia.pit.rate.flat` | [[FACT:ia.pit.rate.flat=3.8]] % | 2025-01-01 to open | US-IAS5-016 (Iowa Department of Revenue; A.2, direct artifact inspection, confidence high) | 422.5(1)(a); nonresident fraction at assessment; resident credit at assessment. |
| `ia.wh.allowance.per_dependent` | [[FACT:ia.wh.allowance.per_dependent=40]] USD | 2026-01-01 to open | US-IAS5-029 (Iowa Department of Revenue; A.2, direct artifact inspection, confidence high) | 2026 IA W-4 44-019a (11/13/2025); due within 15 days of hire; none on file = zero allowances; keep 4 years; new W-4 within 10 days when allowances decrease. |
| `ia.wh.deduction.hoh` | [[FACT:ia.wh.deduction.hoh=19,500]] USD | 2026-01-01 to 2026-12-31 | US-IAS5-005 (Iowa Department of Revenue; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-IAS5-005. |
| `ia.wh.deduction.mfj_one_earner_qss` | [[FACT:ia.wh.deduction.mfj_one_earner_qss=26,000]] USD | 2026-01-01 to 2026-12-31 | US-IAS5-005 (Iowa Department of Revenue; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-IAS5-005. |
| `ia.wh.deduction.other` | [[FACT:ia.wh.deduction.other=13,000]] USD | 2026-01-01 to 2026-12-31 | US-IAS5-005 (Iowa Department of Revenue; A.2, derived arithmetically, confidence high) | Other / MFJ spouse with income / missing status; weekly 250, biweekly 500, semimonthly 541.67, monthly 1,083.33, daily 50. Pre-2024 W-4: Single [[FACT:ia.wh.deduction.other=13,000]], Married [[FACT:ia.wh.deduction.mfj_one_earner_qss=26,000]], W = allowances x 40. |
| `ia.wh.exempt.threshold.mfj_hoh_under65` | [[FACT:ia.wh.exempt.threshold.mfj_hoh_under65=13,500]] USD | 2026-01-01 to open | US-IAS5-016 (Iowa Department of Revenue; A.2, quoted from authority page, confidence high) |  |
| `ia.wh.exempt.threshold.single_under65` | [[FACT:ia.wh.exempt.threshold.single_under65=9,000]] USD | 2026-01-01 to open | US-IAS5-016 (Iowa Department of Revenue; A.2, quoted from authority page, confidence high) | [[FACT:ia.wh.exempt.threshold.mfj_hoh_under65=13,500]] MFJ/HoH under 65; 32,000 / 24,000 at 65+; nonresidents may not claim EXEMPT. |
| `ia.wh.formula.rate` | [[FACT:ia.wh.formula.rate=3.8]] % | 2026-01-01 to 2026-12-31 | US-IAS5-005 (Iowa Department of Revenue; A.2, quoted from authority page, confidence high) | Rate applied at step T2 of the 2026 withholding formula. LEVEL: withholding. |
| `ia.wh.method` | [[FACT:ia.wh.method=T1 = G - D; T2 = T1 x 3.80%; T3 = T2 - W/P; T4 = T3 + A (2026 formula, released Nov 2025); tables alternative (register US-IAS5-015)]] | 2026-01-01 to 2026-12-31 | US-IAS5-005 (Iowa Department of Revenue; A.2, derived arithmetically, confidence high) | Six 2024+ IA W-4 examples re-derived to the cent. P: daily 260, weekly 52, biweekly 26, semimonthly 24, monthly 12. |
| `ia.wh.rounding` | [[FACT:ia.wh.rounding=to the cent, half-up (no whole-dollar rounding in 2026)]] | 2026-01-01 to 2026-12-31 | US-IAS5-005 (Iowa Department of Revenue; A.2, derived arithmetically, confidence high) | Tables Step 5: "rounded to the nearest cent" [US-IAS5-015]. Supersedes the whole-dollar rounding clause of US-IA-001. |
| `ia.wh.supplemental.rate` | [[FACT:ia.wh.supplemental.rate=3.8]] % | 2026-01-01 to open | US-IAS5-016 (Iowa Department of Revenue; A.2, second independent authority, confidence high) | 422.16(2)(e) and 701 IAC 307.2(1)(c) [US-IAS5-006]: when treated separately and federal withheld at flat rate; otherwise aggregate. |

Not configured in this release [[GAP:RQ-180]]: An older register row (US-IA-001) states whole-dollar rounding; the 2026 formula and tables say nearest cent. The 2025 formula was not read.

## IA.2b Non-resident regime and reciprocity

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ia.reciprocity.states` | [[FACT:ia.reciprocity.states=IL]] | 2026-01-01 to open | US-IAS5-016 (Iowa Department of Revenue; A.2, quoted from authority page, confidence high) | IL resident in IA files 44-016 (employer withholds IL); IA resident in IL files IL-W-5-NR [US-MULTI-018]. Nonresidents otherwise withheld at resident rate from first day (no threshold); exceptions interstate carriers, film/TV (44-017), disaster workers (29C.24). |

## IA.2c Local wage taxes

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ia.local.surtax.withheld` | [[FACT:ia.local.surtax.withheld=False]] | 2026-01-01 to open | US-IAS5-029 (Iowa Department of Revenue; A.2, direct artifact inspection, confidence high) | School-district and EMS surtaxes settled on IA 1040 by residence; employee may adjust allowances/line 8 [US-IAP51-005, US-IAP52-001]. |

## IA.3 Social insurance: unemployment, disability, paid leave and payroll levies

No SDI/TDI/PFML programme is configured for Iowa in this release. 260E/260F training items are credits diverting withholding (NJC, SJC, ACE and TJC programmes), claimed on the quarterly return - not levies [US-IAS5-016]. 2027 rate table unpublished.

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ia.sui.employee.rate` | [[FACT:ia.sui.employee.rate=0]] % | 2026-01-01 to open | US-IAS5-024 (Iowa Workforce Development (published by Iowa Legislature); A.1, direct artifact inspection, confidence high) | 871 IAC 23.6(2). |
| `ia.sui.employer.rate.max` | [[FACT:ia.sui.employer.rate.max=5.4]] % | 2026-01-01 to 2026-12-31 | US-IAP9V-001 (Iowa Workforce Development; A.2, quoted from authority page, confidence high) | Table D, ranks 1-9, 0.000%-[[FACT:ia.sui.employer.rate.max=5.400]]% (max cut from 9%, tables 8 -> 4). |
| `ia.sui.employer.rate.min` | [[FACT:ia.sui.employer.rate.min=0]] % | 2026-01-01 to 2026-12-31 | US-IAP9V-001 (Iowa Workforce Development; A.2, quoted from authority page, confidence high) |  |
| `ia.sui.new_employer.construction.rate` | [[FACT:ia.sui.new_employer.construction.rate=5.4]] % | 2026-01-01 to 2026-12-31 | US-IAS5-011 (Iowa Legislature; A.1, direct artifact inspection, confidence high) |  |
| `ia.sui.new_employer.rate` | [[FACT:ia.sui.new_employer.rate=1.0]] % | 2026-01-01 to 2026-12-31 | US-IAS5-011 (Iowa Legislature; A.1, direct artifact inspection, confidence high) | Non-construction: rank-4 rate but not less than [[FACT:ia.sui.new_employer.rate=1.000]]% until 12 chargeable quarters; construction rank 9 = [[FACT:ia.sui.employer.rate.max=5.400]]%. |
| `ia.sui.wage_base` | [[FACT:ia.sui.wage_base=20,400]] USD | 2026-01-01 to 2026-12-31 | US-IAS5-009 (Iowa Workforce Development; A.2, derived arithmetically, confidence high) | 96.1A(36) as amended by SF 607: 1/3 of AAW rounded up to next 100, not below FUTA: 61,098.90/3 = 20,366.30 -> [[FACT:ia.sui.wage_base=20,400]] [US-IAS5-008]. |
| `ia.sui.wage_base` | [[FACT:ia.sui.wage_base=21,100]] USD | 2027-01-01 to open | US-IAS5-010 (Iowa Workforce Development; A.2, derived arithmetically, confidence high) | Announced 2026-06-30: 63,213.58/3 = 21,071.19 -> [[FACT:ia.sui.wage_base=21,100]]. |
| `ia.sui.wage_base.other_state_credit` | [[FACT:ia.sui.wage_base.other_state_credit=False]] | 2026-01-01 to open | US-IAS5-024 (Iowa Workforce Development (published by Iowa Legislature); A.1, direct artifact inspection, confidence high) | 23.6(3): only wages reported to Iowa UI count; successor with experience transfer may count predecessor wages (23.6(4)). Reported tips are UI wages (23.5). |

Not configured in this release [[GAP:RQ-181]]: CY2027 rate table not yet published.

Not configured in this release [[GAP:RQ-584]]: Whether Iowa has a State SDI/TDI/PFML programme is not established from an official Iowa source; none is configured.

## IA.4 Pay statement

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ia.payslip.items` | [[FACT:ia.payslip.items=hours worked, wages earned, deductions made, each regular payday (91A.6(4)); mail, secure electronic, workplace or view access, no separate consent; itemised computation within 10 working days on request]] | 2026-01-01 to open | US-IAS5-027 (Iowa Legislature; A.1, direct artifact inspection, confidence medium) | Statute row US-IAP51-002; reach follows Iowa work location (91A.2(3),(4)). |

## IA.5 Statutory reporting

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ia.newhire.report_days` | [[FACT:ia.newhire.report_days=15]] days | 2026-01-01 to open | US-IAS5-012 (Iowa Legislature; A.1, direct artifact inspection, confidence high) | 252G.3: employer name/address/FEIN; employee name/address/SSN/DOB; dependent health coverage availability and date; IWO address; independent contractors too. |
| `ia.report.annual_reconciliation.exists` | [[FACT:ia.report.annual_reconciliation.exists=False]] | 2026-01-01 to open | US-IAS5-017 (Iowa Department of Revenue; A.2, quoted from authority page, confidence high) | VSPs no longer required. |
| `ia.report.sui.quarterly` | [[FACT:ia.report.sui.quarterly=Employer Contribution and Payroll Report 65-5300 + wage detail by SSN, electronic, due last day of month after quarter (871 IAC 23.8(1))]] | 2026-01-01 to open | US-IAS5-024 (Iowa Workforce Development (published by Iowa Legislature); A.1, direct artifact inspection, confidence high) |  |
| `ia.report.w2` | [[FACT:ia.report.w2=e-file via GovConnectIowa by February 15 only W-2/1099 with IA withholding; IDR-unique 512-byte EFW2-based format (SSA file rejected); RS state code 19, permit 248-267; IA RV record; Key & Send; employee copy Jan 31, terminated on request within 30 days]] | 2023-01-09 to open | US-IAS5-018 (Iowa Department of Revenue; A.2, direct artifact inspection, confidence medium) | Spec page dated 2023-01-09 (TY2023-2025); TY2026 edition not seen. |
| `ia.report.wh.filer_class` | [[FACT:ia.report.wh.filer_class=quarterly < 6,000/yr and <= 500/month; monthly 6,000-120,000 (15th); semimonthly > 5,000 per semimonthly period (25th / 10th, electronic); annual election <= 2 employees; quarterly return last day of month after quarter via GovConnectIowa, zero returns required]] | 2026-01-01 to open | US-IAS5-016 (Iowa Department of Revenue; A.2, quoted from authority page, confidence high) | 422.16(4) [US-IAS5-007]. |

Not configured in this release [[GAP:RQ-182]]: MyIowaUI quarterly wage-detail upload layout not acquired.

Not configured in this release [[GAP:RQ-183]]: IDR W-2 spec covers TY2023-2025 filed in 2026.

## IA.6 Leave

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ia.leave.sick.state_mandate.exists` | [[FACT:ia.leave.sick.state_mandate.exists=False]] | 2026-01-01 to open | US-IAS5-021 (Iowa Legislature; A.1, direct artifact inspection, confidence medium) |  |

Not configured in this release [[GAP:RQ-184]]: Not established from an official source.

## IA.7 Termination and final pay

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ia.final_pay.rule` | [[FACT:ia.final_pay.rule=next regular payday for the period in which wages were earned (no discharge/resignation distinction); commission true-up within 30 days; vacation only per agreement/pro-rata policy (91A.4)]] | 2026-01-01 to open | US-IAS5-003 (Iowa Legislature; A.1, direct artifact inspection, confidence high) |  |
| `ia.separation.wage_request_response_days` | [[FACT:ia.separation.wage_request_response_days=10]] days | 2026-01-01 to open | US-IAS5-026 (Iowa Workforce Development; A.3, quoted from authority page, confidence medium) | No separation notice statute; IWD Notice of Separation and Wage Request answered within 10 days. |

## IA.8 Benefits in kind and taxable wages

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ia.pit.conformity` | [[FACT:ia.pit.conformity=rolling IRC conformity from TY2023; withholding on same wages as federal; 401(k)/125/HSA/transit/GTL follow federal]] | 2023-01-01 to open | US-IAS5-020 (Iowa Department of Revenue; A.2, quoted from authority page, confidence medium) |  |

## IA.9 Deductions and garnishments

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ia.deductions.rule` | [[FACT:ia.deductions.rule=required by law, court order, or written authorisation for employee benefit; prohibited: shared till shortages, dishonoured checks, non-wilful breakage, lost non-assigned property, gratuities, PPE, relocation over 20 (91A.5)]] | 2026-01-01 to open | US-IAS5-004 (Iowa Legislature; A.1, direct artifact inspection, confidence high) |  |
| `ia.garn.child_support.employer_fee` | [[FACT:ia.garn.child_support.employer_fee=2]] USD | 2026-01-01 to open | US-IAS5-022 (Iowa Legislature; A.1, direct artifact inspection, confidence high) | 252D.17: per payment within CCPA; IWO priority; remit to CSC within 7 business days. |
| `ia.garn.child_support.remit_business_days` | [[FACT:ia.garn.child_support.remit_business_days=7]] business days | 2026-01-01 to open | US-IAS5-022 (Iowa Legislature; A.1, direct artifact inspection, confidence high) |  |
| `ia.garn.creditor.annual_cap_schedule` | [[FACT:ia.garn.creditor.annual_cap_schedule=per judgment creditor by expected annual earnings: < 12,000: 250; 12,000-16,000: 400; 16,000-24,000: 800; 24,000-35,000: 1,500; 35,000-50,000: 2,000; >= 50,000: 10% (plus CCPA)]] | 2026-01-01 to open | US-IAS5-013 (Iowa Legislature; A.1, direct artifact inspection, confidence high) | 642.21; not for support; not indexed. |

Not configured in this release [[GAP:RQ-185]]: IDR wage-levy procedure not read.

## IA.10 Collective agreements and prevailing wage

No state prevailing-wage law (DOL WHD list 2023) [US-IAP51-001].

## IA.11 Indexation

UI base 1/3 AAW yearly (late-June release); rate table by fund formula; PIT flat not indexed (deduction amounts reissued each November); MW and garnishment brackets fixed.

## IA.12 Payroll data protection and records

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ia.breach.notice` | [[FACT:ia.breach.notice=without unreasonable delay; processor notifies owner immediately (715C.2)]] | 2026-01-01 to open | US-IAS5-023 (Iowa Legislature; A.1, direct artifact inspection, confidence high) |  |

Not configured in this release [[GAP:RQ-186]]: Iowa Code 715A not read.

## IA.13 Live legal change

SF 607 in force CY2026 (employer UI level); 2027 base [[FACT:ia.sui.wage_base=21,100]]; 2026 formula/IA W-4 (withholding); OBBBA deductions (assessment); sports wagering 3.8% (non-wage). Full 2026 Acts sweep not done.

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ia.live.hf2212.status` | [[FACT:ia.live.hf2212.status=NOT enacted (introduced 2026-01-29, referred House HHS): direct-care minimum 20.00 - do not model]] | 2026-01-29 to open | US-IAS5-028 (Iowa Legislature; A.1, direct artifact inspection, confidence high) |  |

Not configured in this release [[GAP:RQ-187]]: Full sweep of 2026 enrolled Acts touching chs. 91A, 91D, 92, 96, 252D, 422, 642 not done.

## IA.14 Authority worked examples (oracle values)

Each example is computed from the statutory parameters listed in this annex and checked against the result published by the authority. Amounts round half-up to the cent unless the line states another rule.

**Example IA-1: head of household, monthly wages 5,000.00, W-4 allowance amount W = 160.00, no additional amount (2026 withholding formula, example 6).**

| Line | Calculation | Result |
|---|---|---|
| D (period deduction) | [[FACT:ia.wh.deduction.hoh=19,500]] / 12 | 1,625.00 |
| T1 = G - D | 5,000.00 - 1,625.00 | 3,375.00 |
| T2 = T1 x rate | 3,375.00 x [[FACT:ia.pit.rate.flat=3.8]] % | 128.25 |
| T3 = T2 - W / P | 128.25 - 160.00 / 12 = 114.9167 | [[FACT:ia.oracle.formula.example6.withholding=114.92]] |
| T4 = T3 + A | [[FACT:ia.oracle.formula.example6.withholding=114.92]] + 0.00 (rounding: to the cent, half-up, per `ia.wh.rounding`) | [[FACT:ia.oracle.formula.example6.withholding=114.92]] |

Result [[FACT:ia.oracle.formula.example6.withholding=114.92]] = [[FACT:ia.oracle.formula.example6.withholding=114.92]] (match). The published example prints no final figure; the value is re-derived from the formula.

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ia.oracle.formula.example6.withholding` | [[FACT:ia.oracle.formula.example6.withholding=114.92]] USD | 2026-01-01 to 2026-12-31 | US-IAS5-005 (Iowa Department of Revenue; A.2, derived arithmetically, confidence medium) | Formula PDF example 6 (monthly 5,000, HoH, W = 160) printed WITHOUT its final figure; derived [[FACT:ia.oracle.formula.example6.withholding=114.92]] = (5,000 - 1,625) x 3.8% - 160/12. The other examples (e.g. 59.26, 38.72, 145.50) are printed and reproduced to the cent. |

## IA.15 Special populations

- Domestic: generally excluded from IA withholding; UI at 1,000/quarter [US-IAS5-016, US-IAS5-025].
- Agricultural: withholding follows federal; UI 20,000/quarter or 10+ in 20 weeks [US-IAS5-016, US-IAS5-025, US-IAS5-027].
- Minors: no youth rate beyond 90-day rate; under-16 hours; child under 18 for parent UI-excluded [US-IAS5-001, US-IAS5-014, US-IAS5-025].
- Tipped: tip credit up to 40% of MW (cash wage derived as the minimum wage [[FACT:ia.minwage.hourly=7.25]] less the 40% credit) for restaurants/hotels/motels/inns/cabins with > 30/month tips; tips UI wages; OBBBA tip deduction at assessment [US-IAS5-001, US-IAS5-024].
- Clergy: excluded from IA withholding; church service excluded from UI [US-IAS5-016, US-IAS5-025].
- Students: own-school and curricular work UI-excluded [US-IAS5-025].
- NRAs: IDR additional withholding guidance (15,000 or 29,200 / P x 3.8%) via line 8; no EXEMPT [US-IAS5-016, US-IAS5-029].
- Statutory employees: follow federal [US-IAS5-016].
- Government: withholding agents; reimbursing UI employers; ch. 91D applies [US-IAS5-025].
- Military spouses: MSRRA/VBTA box [US-IAS5-016, US-IAS5-029]. Interstate transport nonresidents: no IA withholding. New employees first 90 days: [[FACT:ia.minwage.first_90_days.hourly=6.35]]. Corporate officers: UI employees.

## IA.16 Language

No language rule; payslip English [US-IAL-001, US-IAP9L-001, US-IAP9L-002] (US-OWN-006).

## IA.S Sources

The legal basis of each value (legal-basis register id, authority, source tier and verification method) is given in the row that carries it.
