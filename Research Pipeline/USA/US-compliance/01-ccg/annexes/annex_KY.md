# Annex KY: Kentucky


**Layer classification (T4).** T4: separate state withholding calculation and state return, plus a local layer remitted to the locality on its own return. Source: build manifest tier census, local income tax domain.

**Summary.** Minimum wage [[FACT:ky.minwage.hourly=7.25]] following federal; tipped-employee definition changed 2026-04-10 (HB 185); OT over 40 plus a KY 7th-day rule; paid rest breaks. Flat [[FACT:ky.pit.rate.flat=3.5]]% PIT (2027 [[FACT:ky.pit.rate.flat=3.5]]% on the statute); formula (annual wage - [[FACT:ky.wh.std_deduction=3,360]]) x [[FACT:ky.pit.rate.flat=3.5]]%; K-4 exemption-only; no supplemental rate; reciprocity IL/IN/MI/WV/WI/VA(commuters)/OH; local occupational license taxes (Louisville [[FACT:ky.local.louisville.rate.all_wages=1.45]]%/2.2%, Lexington [[FACT:ky.local.lexington.rate=2.25]]%, others uncatalogued). UI employer-only, base 12,000 (cap reached), new [[FACT:ky.sui.new_employer.rate=2.70]]%, Schedule A [[FACT:ky.sui.employer.rate.min=0.30]]%-[[FACT:ky.sui.employer.rate.max=9.00]]%. Deductions statement for 10+ employers. Final pay later of next payday or 14 days. Oracle: 42A003 formula examples.

Each parameter row gives its key, the period in force and its legal basis: the legal-basis register row, the authority, the source tier and how the value was verified.

## KY.1 Employment and labour code

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ky.minwage.hourly` | [[FACT:ky.minwage.hourly=7.25]] USD | 2009-07-01 to open | US-KYS5-001 (Kentucky Legislative Research Commission; A.1, direct artifact inspection, confidence high) | KRS 337.275(1); rises automatically with federal 29 USC 206(a)(1). Tipped: federal cash wage with records. |
| `ky.overtime.seventh_day_rule` | [[FACT:ky.overtime.seventh_day_rule=1.5x for time worked on the 7th day of a workweek unless not allowed to work over 40 h that week; OT already paid for same hours credited (KRS 337.050)]] | 2026-01-01 to open | US-KYS5-003 (Kentucky Legislative Research Commission; A.1, direct artifact inspection, confidence high) |  |
| `ky.overtime.weekly_threshold_hours` | [[FACT:ky.overtime.weekly_threshold_hours=40]] hours | 2026-01-01 to open | US-KYS5-002 (Kentucky Legislative Research Commission; A.1, direct artifact inspection, confidence high) | KRS 337.285(1); exemptions incl. retail selling, restaurant/hotel/motel, companionship; public comp time. |
| `ky.pay_frequency.rule` | [[FACT:ky.pay_frequency.rule=at least semimonthly; pay covers wages to a day not more than 18 days before payday; absent employee within 6 days of demand; EAP excluded]] | 2026-01-01 to open | US-KYS5-004 (Kentucky Legislative Research Commission; A.1, direct artifact inspection, confidence medium) |  |
| `ky.payment.method` | [[FACT:ky.payment.method=legal tender, check, direct deposit or payroll card (no activation fee, one free withdrawal per period up to full balance) (KRS 337.010(1)(c)1)]] | 2026-01-01 to open | US-KYS5-006 (Kentucky Legislative Research Commission; A.1, direct artifact inspection, confidence medium) |  |
| `ky.rest_break.paid_minutes_per_4h` | [[FACT:ky.rest_break.paid_minutes_per_4h=10]] minutes | 2026-01-01 to open | US-KYS5-015 (Kentucky Legislative Research Commission; A.1, direct artifact inspection, confidence high) | KRS 337.365; lunch between 3rd and 5th hour (337.355). |
| `ky.tip_pool.rule` | [[FACT:ky.tip_pool.rule=employer may not keep tips except required withholding; pools may include tipped employees, not salaried staff/managers/supervisors (KRS 337.065)]] | 2026-04-10 to open | US-KYS5-008 (Kentucky Legislative Research Commission; A.1, direct artifact inspection, confidence high) |  |
| `ky.tipped.definition` | [[FACT:ky.tipped.definition=more than 30/month in tips AND work directly supporting the tipped service function (2026 Ky. Acts ch. 72)]] | 2026-04-10 to open | US-KYS5-021 (Kentucky Legislative Research Commission; A.1, direct artifact inspection, confidence high) |  |

Not configured in this release [[GAP:RQ-224]]: 2016 KY Supreme Court Louisville MW decision known only from a secondary source; PSL pre-emption unread.

## KY.2 Income tax withholding

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ky.pit.rate.flat` | [[FACT:ky.pit.rate.flat=3.5]] % | 2026-01-01 to open | US-KYS5-009 (Kentucky Legislative Research Commission; A.1, direct artifact inspection, confidence high) | KRS 141.020(2)(f); 2027 stays [[FACT:ky.pit.rate.flat=3.5]]% on the statute unless Budget Director report + General Assembly act (HB 152 stalled, per a secondary source). |
| `ky.wh.certificate` | [[FACT:ky.wh.certificate=K-4 (42A804): no allowances; exemption claims only (no liability; Fort Campbell nonresident; SCRA/MSRRA; reciprocal-state residents)]] | 2026-01-01 to open | US-KYS5-013 (Kentucky Department of Revenue; A.2, direct artifact inspection, confidence high) |  |
| `ky.wh.method` | [[FACT:ky.wh.method=(period wage x periods - 3,360) x 3.5% / periods (2026 formula sheet 42A003 TCF)]] | 2026-01-01 to 2026-12-31 | US-KY-002 (Kentucky Department of Revenue; A.2, derived arithmetically, confidence high) | Bi-weekly example prints 35,730 where 35,640 is correct (35,640 x [[FACT:ky.pit.rate.flat=3.5]]% = [[FACT:ky.oracle.formula.biweekly_1500.annual=1,247.40]] as printed): typo. Per-period rounding unstated (sheet shows 47 for [[FACT:ky.oracle.biweekly_1500.result=47.98]]). |
| `ky.wh.rounding` | [[FACT:ky.wh.rounding=employer may compute WAGES to nearest dollar (KRS 141.310(4)); no rounding rule for the tax]] | 2026-01-01 to open | US-KYS5-010 (Kentucky Legislative Research Commission; A.1, direct artifact inspection, confidence high) |  |
| `ky.wh.std_deduction` | [[FACT:ky.wh.std_deduction=3,360]] USD | 2026-01-01 to 2026-12-31 | US-KY-002 (Kentucky Department of Revenue; A.2, direct artifact inspection, confidence high) | Indexed annually (KRS 141.081(2)(a)). Extra 117.60 for multiple W-2 = [[FACT:ky.wh.std_deduction=3,360]] x [[FACT:ky.pit.rate.flat=3.5]]%. |
| `ky.wh.supplemental.method` | [[FACT:ky.wh.supplemental.method=no separate rate; bonuses and severance through the same formula; film-incentive companies at max 141.020 rate]] | 2026-01-01 to open | US-KY-001 (Kentucky Department of Revenue; A.2, direct artifact inspection, confidence medium) |  |

Not configured in this release [[GAP:RQ-225]]: TY2027 rate is [[FACT:ky.pit.rate.flat=3.5]]% on the statute; the Budget Director report of 2026-09-05 was not verified against the official source.

Not configured in this release [[GAP:RQ-226]]: Formula sheet shows 47 for [[FACT:ky.oracle.biweekly_1500.result=47.98]] bi-weekly; KRS 141.310(4) rounds only wages.

## KY.2b Non-resident regime and reciprocity

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ky.reciprocity.states` | [[FACT:ky.reciprocity.states=IL, IN, MI, WV, WI; VA daily commuters only; OH unless 20%+ S-corp shareholder]] | 2026-01-01 to open | US-KY-001 (Kentucky Department of Revenue; A.2, direct artifact inspection, confidence high) | Certificate 42A809 [US-MULTI-009]. Nonresidents taxed on KY labour only; out-of-state employers withhold on KY-earned wages (103 KAR 18:010(2)) [US-KYS5-023]. Other-state credit at assessment (KRS 141.070). |

## KY.2c Local wage taxes

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ky.local.basis` | [[FACT:ky.local.basis=work-location occupational license taxes on separate returns per locality; DOR does not administer]] | 2026-01-01 to open | US-KYS5-024 (Lexington-Fayette Urban County Government Division of Revenue; A.2, direct artifact inspection, confidence medium) |  |
| `ky.local.lexington.rate` | [[FACT:ky.local.lexington.rate=2.25]] % | 2026-01-01 to open | US-KYS5-024 (Lexington-Fayette Urban County Government Division of Revenue; A.2, direct artifact inspection, confidence high) | LFUCG: withheld by employer; 220-221 quarterly (preprinted, mailed Jan), monthly if quarterly > 300; 222 annual reconciliation; base (s.125/deferred comp) unread. |
| `ky.local.louisville.rate.all_wages` | [[FACT:ky.local.louisville.rate.all_wages=1.45]] % | 2026-01-01 to open | US-KYP9W-001 (Louisville Metro Revenue Commission; A.2, quoted from authority page, confidence high) | Metro and TARC rates together on all wages earned in Louisville Metro; residents add the school-board rate, total [[FACT:ky.local.louisville.rate.resident_total=2.2]]%; W-1 quarterly, W-1D monthly if > 3,000/quarter, W-3 by Feb 28 [US-KYP9W-002]. |
| `ky.local.louisville.rate.resident_total` | [[FACT:ky.local.louisville.rate.resident_total=2.2]] % | 2026-01-01 to open | US-KYP9W-001 (Louisville Metro Revenue Commission; A.2, quoted from authority page, confidence high) |  |

Not configured in this release [[GAP:RQ-227]]: Only Louisville and Lexington verified; other cities, counties and school districts uncatalogued.

Not configured in this release [[GAP:RQ-228]]: LFUCG withholding base (s.125/deferred comp) and Fayette County Board of Education tax not verified against the official source; a secondary source says included.

## KY.3 Social insurance: unemployment, disability, paid leave and payroll levies

No SDI/TDI/PFML; KRS 304.53 only voluntary group PFL insurance [US-KYR3-001..003]. Workers compensation premiums may not be deducted.

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ky.sui.coverage` | [[FACT:ky.sui.coverage=non-ag 1,500/quarter or 1 in 20 weeks; ag 20,000/quarter or 10 in 20 weeks; domestic 1,000/quarter; 501(c)(3) 4 in 20 weeks; officers covered; proprietor spouse/parent/child < 21 not]] | 2026-01-01 to open | US-KYS5-019 (Kentucky Office of Unemployment Insurance; A.2, direct artifact inspection, confidence high) |  |
| `ky.sui.employer.rate.max` | [[FACT:ky.sui.employer.rate.max=9.0]] % | 2026-01-01 to 2026-12-31 | US-KY-003 (Kentucky Office of Unemployment Insurance; A.2, quoted from authority page, confidence medium) |  |
| `ky.sui.employer.rate.min` | [[FACT:ky.sui.employer.rate.min=0.3]] % | 2026-01-01 to 2026-12-31 | US-KY-003 (Kentucky Office of Unemployment Insurance; A.2, quoted from authority page, confidence medium) | Schedule A [[FACT:ky.sui.employer.rate.min=0.30]]%-[[FACT:ky.sui.employer.rate.max=9.00]]%. |
| `ky.sui.new_employer.rate` | [[FACT:ky.sui.new_employer.rate=2.7]] % | 2026-01-01 to 2026-12-31 | US-KY-003 (Kentucky Office of Unemployment Insurance; A.2, quoted from authority page, confidence medium) | [[FACT:ky.sui.wage_base=12,000]] x [[FACT:ky.sui.new_employer.rate=2.7]]% = 324 max per employee [US-KYS5-019]. |
| `ky.sui.scuf.rate` | [[FACT:ky.sui.scuf.rate=0.0115]] % | 2027-01-01 to open | US-KYB5-401 (KY official authority; A.2, quoted from authority page, confidence high) | Inside the rate (diverted), no extra cost; 0% in 2026 (SB 129). |
| `ky.sui.wage_base` | [[FACT:ky.sui.wage_base=12,000]] USD | 2026-01-01 to 2026-12-31 | US-KY-003 (Kentucky Office of Unemployment Insurance; A.2, derived arithmetically, confidence high) | KRS 341.030(7): 9,000 from 2012 + 300 each Jan 1 to [[FACT:ky.sui.wage_base=12,000]] cap (suspended if fund < 200M on Sept 30): 11,400 + 300 + 300 = [[FACT:ky.sui.wage_base=12,000]]; 2027 = [[FACT:ky.sui.wage_base=12,000]] unless amended [US-KYS5-012]. |
| `ky.sui.wage_base.other_state_credit` | [[FACT:ky.sui.wage_base.other_state_credit=True]] | 2026-01-01 to open | US-KYS5-018 (Kentucky Legislative Research Commission; A.1, direct artifact inspection, confidence high) | KRS 341.030(7)(a). |

## KY.4 Pay statement

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ky.payslip.deduction_statement.employer_threshold` | [[FACT:ky.payslip.deduction_statement.employer_threshold=10]] employees | 2026-01-01 to open | US-KYP8-001 (Kentucky General Assembly (apps.legislature.ky.gov); A.1, direct artifact inspection, confidence high) | Employers with 10+ employees making deductions: paper or electronic statement of each deduction and purpose at payment (electronic requires computer/printer access); no other content mandated. |

## KY.5 Statutory reporting

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ky.newhire.report_days` | [[FACT:ky.newhire.report_days=20]] days | 2025-07-01 to open | US-KYS5-020 (Kentucky Legislative Research Commission; A.1, direct artifact inspection, confidence high) | Recipient Office of the Attorney General since 2025-07-01; residents or workers in KY; includes state EIN. |
| `ky.report.sui.quarterly` | [[FACT:ky.report.sui.quarterly=KUIP (replaced KEWES 2026), due last day of month after quarter, zero reports required; late 25/75 first, 125/175 later; interest 1.5%/month]] | 2026-01-01 to open | US-KYS5-019 (Kentucky Office of Unemployment Insurance; A.2, direct artifact inspection, confidence high) |  |
| `ky.report.w2` | [[FACT:ky.report.w2=due Jan 31 via MyTaxes or CD; SSA EFW2 with DOR RS record or K-5; electronic mandatory at 26+ statements (103 KAR 18:050(4)); paper W-2 not processed]] | 2026-01-01 to open | US-KYS5-013 (Kentucky Department of Revenue; A.2, direct artifact inspection, confidence high) |  |
| `ky.report.w2.efile_threshold` | [[FACT:ky.report.w2.efile_threshold=26]] statements | 2026-01-01 to open | US-KYS5-013 (Kentucky Department of Revenue; A.2, direct artifact inspection, confidence high) |  |
| `ky.report.wh.frequency` | [[FACT:ky.report.wh.frequency=annual < 400 (K-3 Jan 31); quarterly 400-1,999 (K-1 last day of month after quarter); monthly 2,000-49,999 (K-1 15th); twice-monthly >= 50,000 (25th / 10th); >= 100,000 in a period by EFT next banking day; zero returns required; MyTaxes electronic]] | 2026-01-01 to open | US-KYS5-013 (Kentucky Department of Revenue; A.2, direct artifact inspection, confidence high) |  |

Not configured in this release [[GAP:RQ-229]]: KY EFW2 RS-record spec and KUIP wage-file layout not verified against the official source.

## KY.6 Leave

No paid sick leave statute; local PSL pre-emption not verified against the official source. Court appearance protected (337.415) [US-KYS5-017]; jury/military not verified against the official source.

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ky.leave.adoption.weeks` | [[FACT:ky.leave.adoption.weeks=6]] weeks | 2026-01-01 to open | US-KYS5-016 (Kentucky Legislative Research Commission; A.1, direct artifact inspection, confidence high) | KRS 337.015: child under 10; match benefits given to birth parents. |
| `ky.leave.voting.hours` | [[FACT:ky.leave.voting.hours=4]] hours | 2026-01-01 to open | US-KYS5-025 (Kentucky Legislative Research Commission; A.1, direct artifact inspection, confidence high) | KRS 118.035; no pay rule. |

Not configured in this release [[GAP:RQ-230]]: KRS 29A.160, 38.238/38.460 and KRS 339 / 803 KAR 1:100 not verified against the official source.

## KY.7 Termination and final pay

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ky.final_pay.max_days` | [[FACT:ky.final_pay.max_days=14]] days | 2026-01-01 to open | US-KYS5-005 (Kentucky Legislative Research Commission; A.1, direct artifact inspection, confidence high) |  |
| `ky.final_pay.rule` | [[FACT:ky.final_pay.rule=later of next normal payday or 14 days after separation, discharge or resignation (KRS 337.055); vested vacation and earned bonuses are wages]] | 2026-01-01 to open | US-KYS5-005 (Kentucky Legislative Research Commission; A.1, direct artifact inspection, confidence high) | [US-KYS5-006] vacation; public comp time paid at higher of 3-year average or final rate. |

Not configured in this release [[GAP:RQ-231]]: Only claim-driven UI-412A/UI-412 found.

## KY.8 Benefits in kind and taxable wages

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ky.pit.conformity_date` | [[FACT:ky.pit.conformity_date=2025-12-31 (KRS 141.010(21), effective 2026-07-15, TY2026)]] | 2026-07-15 to open | US-KYS5-022 (Kentucky Legislative Research Commission; A.1, direct artifact inspection, confidence high) |  |
| `ky.wh.chart_42a003` | [[FACT:ky.wh.chart_42a003=not required: 125/flex, DCAP, health, GTL*, 401(k)*, SEP*, TSP*, IRA, fringe*, meals/lodging*, travel*; required: company cars, moving, severance, bonuses, vacation/sick pay*, tips > 20/month]] | 2026-01-01 to open | US-KYS5-023 (Kentucky Department of Revenue; A.2, direct artifact inspection, confidence high) |  |

## KY.9 Deductions and garnishments

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ky.deductions.rule` | [[FACT:ky.deductions.rule=only if required by law or expressly authorised in writing (insurance, medical dues); union dues written consent; fines, shared-till shortages etc. prohibited]] | 2026-01-01 to open | US-KYS5-007 (Kentucky Legislative Research Commission; A.1, direct artifact inspection, confidence high) |  |
| `ky.garn.creditor.rule` | [[FACT:ky.garn.creditor.rule=lesser of 25% of disposable or excess over 30 x federal MW (217.50/week) (KRS 427.010); support/Ch. 13/tax outside]] | 2026-01-01 to open | US-KYS5-014 (Kentucky Legislative Research Commission; A.1, direct artifact inspection, confidence high) |  |

Not configured in this release [[GAP:RQ-232]]: DOR wage levy / priority not established from an official source.

Not configured in this release [[GAP:RQ-233]]: The per-payment employer fee and the lump-sum reporting threshold rest on a secondary source and are not configured.

Not configured in this release [[GAP:RQ-586]]: The employer fee per income-withholding payment is not established from an official source.

Not configured in this release [[GAP:RQ-587]]: The lump-sum reporting threshold for child-support obligors is not established from an official source.

## KY.10 Collective agreements and prevailing wage

Prevailing wage (public works) is an optional informational flag [US-OWN-009]: this guide documents prevailing-wage laws, thresholds and certified-payroll duties as an overlay, and the payroll build does not produce certified payroll reports.

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ky.prevailing_wage.state_law.exists` | [[FACT:ky.prevailing_wage.state_law.exists=False]] | 2017-01-01 to open | US-KYP52-004 (Kentucky Legislative Research Commission; A.1, quoted from authority page, confidence high) | Repealed 2017 (KRS 337.505-.550); Davis-Bacon only. |

## KY.11 Indexation

Std deduction indexed yearly (141.081(2)(a)); PIT rate trigger review; SUI base +300 to 12,000 cap (reached); schedule by fund balance Sept 30; MW follows federal; garnishment floor 30 x federal MW.

## KY.12 Payroll data protection and records

No SSN truncation rule read; KRS 141.335 lists SSN on the annual statement; W-2 by Jan 31 or last wage payment day [US-KYS5-011].

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ky.records.retention_years` | [[FACT:ky.records.retention_years=1]] years | 2026-01-01 to open | US-KYP8-002 (Kentucky General Assembly (apps.legislature.ky.gov); A.1, direct artifact inspection, confidence high) | KRS 337.320: pay and hours records at least 1 year. |

Not configured in this release [[GAP:RQ-234]]: SSN truncation statutes not verified against the official source.

## KY.13 Live legal change

No jurisdiction-specific item was recorded in the research for this domain.

## KY.14 Authority worked examples (oracle values)

Each example is computed from the statutory parameters listed in this annex and checked against the result published by the authority. Amounts round half-up to the cent unless the line states another rule.

**Example KY-1: monthly wages 3,270.00 (2026 formula sheet).**

| Line | Calculation | Result |
|---|---|---|
| Annual wages | 3,270.00 x 12 | 39,240.00 |
| Annual tax | (39,240.00 - [[FACT:ky.wh.std_deduction=3,360]]) x [[FACT:ky.pit.rate.flat=3.5]] % | 1,255.80 |
| Monthly withholding | 1,255.80 / 12, half-up to the cent | [[FACT:ky.oracle.formula.monthly_3270=104.65]] |

Computed result = published [[FACT:ky.oracle.formula.monthly_3270=104.65]] (match).

**Example KY-2: biweekly wages 1,500.00 (2026 formula sheet).**

| Line | Calculation | Result |
|---|---|---|
| Annual wages | 1,500.00 x 26 | 39,000.00 |
| Annual tax | (39,000.00 - [[FACT:ky.wh.std_deduction=3,360]]) x [[FACT:ky.pit.rate.flat=3.5]] % | [[FACT:ky.oracle.formula.biweekly_1500.annual=1,247.40]] |
| Biweekly withholding | [[FACT:ky.oracle.formula.biweekly_1500.annual=1,247.40]] / 26, half-up to the cent | [[FACT:ky.oracle.biweekly_1500.result=47.98]] |

The annual tax matches the published figure (match). The formula sheet shows a whole-dollar per-period figure without stating a rounding rule; see the rounding limitation in KY.2.

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ky.oracle.formula.biweekly_1500.annual` | [[FACT:ky.oracle.formula.biweekly_1500.annual=1,247.40]] USD | 2026-01-01 to 2026-12-31 | US-KY-002 (Kentucky Department of Revenue; A.2, derived arithmetically, confidence medium) | Bi-weekly 1,500: (39,000 - [[FACT:ky.wh.std_deduction=3,360]]) = 35,640 x [[FACT:ky.pit.rate.flat=3.5]]% = [[FACT:ky.oracle.formula.biweekly_1500.annual=1,247.40]] (sheet prints 35,730 - typo); /26 = [[FACT:ky.oracle.biweekly_1500.result=47.98]], sheet shows 47 (rounding unexplained). |
| `ky.oracle.formula.monthly_3270` | [[FACT:ky.oracle.formula.monthly_3270=104.65]] USD | 2026-01-01 to 2026-12-31 | US-KY-002 (Kentucky Department of Revenue; A.2, derived arithmetically, confidence high) | Monthly 3,270: (39,240 - [[FACT:ky.wh.std_deduction=3,360]]) x [[FACT:ky.pit.rate.flat=3.5]]% = 1,255.80 / 12 = [[FACT:ky.oracle.formula.monthly_3270=104.65]]. |

## KY.15 Special populations

- Domestic: excluded from state MW/OT unless more than one domestic regularly employed; withholding not required; UI 1,000/quarter [US-KYS5-006, US-KYS5-023, US-KYS5-019].
- Agricultural: excluded from state MW/OT; withholding per IRC 3121(a) test; UI 20,000/quarter or 10 in 20 weeks [US-KYS5-006, US-KYS5-023, US-KYS5-019].
- Minors: no subminimum; KRS 339 not verified against the official source.
- Tipped: federal cash wage; new definition 2026-04-10; tip pools; tips > 20/month withheld [US-KYS5-001, US-KYS5-021, US-KYS5-008, US-KYS5-023].
- Clergy: withholding not required; religious camps <= 210 days excluded from MW chapter [US-KYS5-023, US-KYS5-006].
- Students/learners/apprentices: subminimum only with commissioner certificate [US-KYS5-006].
- NRAs: withholding required [US-KYS5-023]. Statutory employees: direct sellers excluded from MW; withholding per IRC 3401 [US-KYS5-006, US-KYS5-013].
- Government: federal and certain state employees excluded from MW chapter; county/city comp-time regime [US-KYS5-006, US-KYS5-002].
- Small retail/service (< 95,000 gross) and family: excluded from MW chapter [US-KYS5-006].
- Military / Fort Campbell nonresidents and SCRA/MSRRA spouses exempt [US-KYS5-013].

## KY.16 Language

No language clause in KRS 337.070/.320/.325 [US-KYP8-001..003]; payslip English (US-OWN-006).

## KY.S Sources

The legal basis of each value (legal-basis register id, authority, source tier and verification method) is given in the row that carries it.
