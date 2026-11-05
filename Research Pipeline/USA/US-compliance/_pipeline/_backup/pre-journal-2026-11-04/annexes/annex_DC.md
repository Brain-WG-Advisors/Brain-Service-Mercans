# Annex DC: District of Columbia


**Layer classification (T3).** T3: separate state withholding calculation and state return; no local layer, or a local layer piggybacked on the state return. Source: build manifest tier census, local income tax domain.

**Summary.** Minimum wage [[FACT:dc.minwage.hourly=17.95]] -> [[FACT:dc.minwage.hourly=18.40]] (2026-07-01, CPI Washington MSA); tipped wage [[FACT:dc.minwage.tipped.cash_wage=10.30]] = 56% of the minimum, rising to 75% by 2034; non-hotel tipped employers must use a third-party payroll business. Income tax withheld by a percentage method/tables with no standard deduction in withholding; the 2026 method after D.C. Act 26-416 (personal exemptions repealed) is UNPUBLISHED and the D-4/D-4A are "under review" (blocking open question). Nonresidents not taxed (Home Rule Act, D-4A). SUI base 9,000, new [[FACT:dc.sui.new_employer.rate=2.7]]%, +[[FACT:dc.sui.admin_assessment.rate=0.2]]% admin assessment; PFL 0.75% employer-only, no cap. Itemised pay statement with tip lines and, from 2026, compensation sources.

Each parameter row gives its key, the period in force and its legal basis: the legal-basis register row, the authority, the source tier and how the value was verified.

## DC.1 Employment and labour code

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `dc.minwage.coverage` | [[FACT:dc.minwage.coverage=> 50% of working time in DC, or DC-based with substantial DC time and <= 50% in any one state; any employee with >= 2 h in DC in a workweek gets DC MW for DC hours (32-1003(b),(b-1))]] | 2026-01-01 to open | US-DCS5-001 (Council of the District of Columbia; A.1, direct artifact inspection, confidence high) |  |
| `dc.minwage.hourly` | [[FACT:dc.minwage.hourly=17.95]] USD | 2025-07-01 to 2026-06-30 | US-DCS5-011 (DC Department of Employment Services, Office of Wage and Hour; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-DCS5-011. |
| `dc.minwage.hourly` | [[FACT:dc.minwage.hourly=18.40]] USD | 2026-07-01 to open | US-DCS5-011 (DC Department of Employment Services, Office of Wage and Hour; A.2, derived arithmetically, confidence high) | Derivation: [[FACT:dc.minwage.hourly=17.95]] x 1.024 (CPI-U Washington MSA) = 18.3808 -> [[FACT:dc.minwage.hourly=18.40]] (nearest 0.05) [US-DCS5-001, 32-1003(a)(6)]. 2027 due by ~June 2027. |
| `dc.minwage.tipped.cash_wage` | [[FACT:dc.minwage.tipped.cash_wage=10]] USD | 2024-07-01 to 2026-06-30 | US-DCS5-011 (DC Department of Employment Services, Office of Wage and Hour; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-DCS5-011. |
| `dc.minwage.tipped.cash_wage` | [[FACT:dc.minwage.tipped.cash_wage=10.30]] USD | 2026-07-01 to open | US-DCS5-011 (DC Department of Employment Services, Office of Wage and Hour; A.2, derived arithmetically, confidence high) | = [[FACT:dc.minwage.tipped.percent_of_minimum=56]]% x [[FACT:dc.minwage.hourly=18.40]] = 10.304 -> [[FACT:dc.minwage.tipped.cash_wage=10.30]]; employer tops up weekly shortfall. |
| `dc.minwage.tipped.percent_of_minimum` | [[FACT:dc.minwage.tipped.percent_of_minimum=56]] % | 2026-07-01 to 2028-06-30 | US-DCS5-001 (Council of the District of Columbia; A.1, direct artifact inspection, confidence high) | D.C. Law 26-55 s.2222(a): [[FACT:dc.minwage.tipped.percent_of_minimum=56]]% from 2026-07-01, 60% 2028, [[FACT:dc.minwage.tipped.percent_of_minimum=65]]% 2030, 70% 2032, [[FACT:dc.minwage.tipped.percent_of_minimum=75]]% 2034. |
| `dc.minwage.tipped.percent_of_minimum` | [[FACT:dc.minwage.tipped.percent_of_minimum=60]] % | 2028-07-01 to 2030-06-30 | US-DCS5-001 (Council of the District of Columbia; A.1, direct artifact inspection, confidence high) |  |
| `dc.minwage.tipped.percent_of_minimum` | [[FACT:dc.minwage.tipped.percent_of_minimum=65]] % | 2030-07-01 to 2032-06-30 | US-DCS5-001 (Council of the District of Columbia; A.1, direct artifact inspection, confidence high) |  |
| `dc.minwage.tipped.percent_of_minimum` | [[FACT:dc.minwage.tipped.percent_of_minimum=70]] % | 2032-07-01 to 2034-06-30 | US-DCS5-001 (Council of the District of Columbia; A.1, direct artifact inspection, confidence high) |  |
| `dc.minwage.tipped.percent_of_minimum` | [[FACT:dc.minwage.tipped.percent_of_minimum=75]] % | 2034-07-01 to open | US-DCS5-001 (Council of the District of Columbia; A.1, direct artifact inspection, confidence high) |  |
| `dc.overtime.weekly_threshold_hours` | [[FACT:dc.overtime.weekly_threshold_hours=40]] hours | 2026-01-01 to open | US-DCS5-001 (Council of the District of Columbia; A.1, direct artifact inspection, confidence high) | 1.5x over 40; no daily OT; retail/service commission exemption. |
| `dc.pay_frequency.rule` | [[FACT:dc.pay_frequency.rule=at least twice per calendar month on paydays designated in advance; EAP or contract/custom monthly; at most 10 working days from period end to payday]] | 2026-01-01 to open | US-DCS5-002 (Council of the District of Columbia; A.1, direct artifact inspection, confidence high) |  |
| `dc.payment.method` | [[FACT:dc.payment.method=lawful US money or checks payable on demand (32-1302); no DC direct-deposit/paycard statute found]] | 2026-01-01 to open | US-DCS5-002 (Council of the District of Columbia; A.1, direct artifact inspection, confidence medium) |  |
| `dc.tipped.third_party_payroll.required` | [[FACT:dc.tipped.third_party_payroll.required=True]] | 2025-12-06 to open | US-DCS5-010 (Council of the District of Columbia; A.1, direct artifact inspection, confidence high) | 32-1008(a-1): employers paying the tipped wage, other than hotels. |

## DC.2 Income tax withholding

Configuration rule: the federal tips and overtime deductions are allowed as DC deductions from tax year 2026 at assessment only (`dc.pit.obbba_deductions`). Withholding is not changed for them.
Configuration warning: DC 2026 withholding method is unpublished. 47-1812.08 is unchanged, but D.C. Act 26-416 repealed personal exemptions (the old D-4 allowance basis) and the D-4/D-4A are under review. Until OTR publishes, the only published instruction is Notice 2022-08 (rate schedule with federal allowance amount) - an inference for 2026; the the payroll calculation must flag this. No flat supplemental rate: bonuses withheld as regular wages [US-DCR3-001, US-DCR3-002].

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `dc.pit.obbba_deductions` | [[FACT:dc.pit.obbba_deductions=disallowed TY2025; allowed as DC deductions from TY2026; operating level assessment only (no withholding change)]] | 2026-01-01 to open | US-DCS5-021 (Council of the District of Columbia; A.1, direct artifact inspection, confidence high) |  |
| `dc.pit.personal_exemption.repealed` | [[FACT:dc.pit.personal_exemption.repealed=True]] | 2025-01-01 to open | US-DCS5-021 (Council of the District of Columbia; A.1, direct artifact inspection, confidence high) | D.C. Act 26-416 (emergency, in force 2026-08-13 for <= 90 days, ~to 2026-11-11); tax subtitle as of 2025-01-01; DC standard deduction 15,000 / 22,500 / 30,000 for 2025, COLA from 2026 rounded down to 50. Operating level ASSESSMENT; no change to 47-1812.08. |
| `dc.pit.rate_schedule` | [[FACT:dc.pit.rate_schedule=<=10,000 4%; 10,000-40,000 400+6%; 40,000-60,000 2,200+6.5%; 60,000-250,000 3,500+8.5%; 250,000-500,000 19,650+9.25%; 500,000-1,000,000 42,775+9.75%; >1,000,000 91,525+10.75%]] | 2022-01-01 to open | US-DCP52-001 (DC Office of Tax and Revenue; A.2, quoted from authority page, confidence high) | Base amounts re-derived (match). Not indexed. |
| `dc.wh.certificate.status` | [[FACT:dc.wh.certificate.status=D-4 and D-4A marked "currently under review" on the OTR forms page, no fill-in link]] | 2026-11-02 to open | US-DCS5-013 (DC Office of Tax and Revenue; A.2, direct artifact inspection, confidence high) |  |
| `dc.wh.lump_sum_retirement.rate` | [[FACT:dc.wh.lump_sum_retirement.rate=10.75]] % | 2026-01-01 to open | US-DCP51-002 (DC Office of Tax and Revenue; A.2, direct artifact inspection, confidence high) | Resident lump-sum retirement distributions at highest rate (47-1812.08(m), amended by D.C. Law 26-89 / Act 26-214). |
| `dc.wh.notice_2022_08` | [[FACT:dc.wh.notice_2022_08=apply current rate schedule with the federal allowance amount (no FR-230 after 2018); applying to 2026 is an inference]] | 2022-01-01 to open | US-DCP51-002 (DC Office of Tax and Revenue; A.2, quoted from authority page, confidence high) |  |
| `dc.wh.statutory_method` | [[FACT:dc.wh.statutory_method=percentage method or tables similar to IRC 3402; no standard-deduction allowance in withholding; wages may be computed to nearest dollar (47-1812.08(b))]] | 2026-01-01 to open | US-DCS5-025 (Council of the District of Columbia; A.1, direct artifact inspection, confidence high) |  |

Not yet published [[GAP:RQ-138]]: 2026 DC withholding method after D.C. Act 26-416 repealed personal exemptions is unpublished; D-4/D-4A "under review"; OTR withholding-instructions page 403.

Not configured in this release [[GAP:RQ-139]]: No flat supplemental rate in statute or any FR-230 edition; bonuses modelled as regular wages.

Not configured in this release [[GAP:RQ-140]]: 2026 COLA amount of the DC standard deduction (assessment level) not read.

## DC.2b Non-resident regime and reciprocity

DC exempts all nonresidents (Home Rule Act); MD and VA appear in the MULTI matrix because they exempt DC residents [US-MULTI-016].

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `dc.nonres.taxable` | [[FACT:dc.nonres.taxable=False]] | 2026-01-01 to open | US-DCP51-006 (Council of the District of Columbia; A.1, quoted from authority page, confidence high) | Home Rule Act bars taxing nonresidents; D-4A stops DC withholding; resident credit for other-state tax at assessment. |

## DC.2c Local wage taxes

None: DC is itself the local layer.

## DC.3 Social insurance: unemployment, disability, paid leave and payroll levies

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `dc.pfl.benefit.weekly_max` | [[FACT:dc.pfl.benefit.weekly_max=1,100]] USD | 2026-10-01 to open | US-DCS5-021 (Council of the District of Columbia; A.1, direct artifact inspection, confidence high) | D.C. Act 26-416 (emergency); CPI-indexed thereafter; durations parental 12 / family 6 / medical 10 / pre-natal 2 weeks for claims 2026-10-01..2030-09-30. Benefit side, not payroll. |
| `dc.pfl.coverage` | [[FACT:dc.pfl.coverage=> 50% of work time in DC, or DC-based with substantial DC time and <= 50% elsewhere (32-541.01(3)); not by residence]] | 2026-01-01 to open | US-DCS5-007 (Council of the District of Columbia; A.1, direct artifact inspection, confidence high) |  |
| `dc.pfl.employer.rate` | [[FACT:dc.pfl.employer.rate=0.75]] % | 2024-07-01 to open | US-DCS5-019 (DC DOES Office of Paid Family Leave; A.2, second independent authority, confidence high) | 100% employer-funded, not deductible from pay, no wage cap (US-DCS5-020). History: 0.62% to 2022-Q2, 0.26% to 2024-Q2. |
| `dc.pfl.wage_cap.exists` | [[FACT:dc.pfl.wage_cap.exists=False]] | 2026-01-01 to open | US-DCS5-020 (Council of the District of Columbia; A.1, direct artifact inspection, confidence high) |  |
| `dc.sui.admin_assessment.rate` | [[FACT:dc.sui.admin_assessment.rate=0.2]] % | 2026-01-01 to open | US-DCS5-017 (Council of the District of Columbia; A.1, direct artifact inspection, confidence high) | (m)(1) administrative funding assessment on taxable wages [US-DCB5-401]. Interest surcharge (l)(1) billing in 2026 unconfirmed [US-DCP7-003]. |
| `dc.sui.employee.rate` | [[FACT:dc.sui.employee.rate=0]] % | 2026-01-01 to open | US-DCS5-017 (Council of the District of Columbia; A.1, direct artifact inspection, confidence high) | Contributions may not be deducted from wages (d). |
| `dc.sui.employer.rate.max` | [[FACT:dc.sui.employer.rate.max=7.4]] % | 2026-01-01 to open | US-DCS5-017 (Council of the District of Columbia; A.1, direct artifact inspection, confidence high) |  |
| `dc.sui.employer.rate.min` | [[FACT:dc.sui.employer.rate.min=1.9]] % | 2026-01-01 to open | US-DCS5-017 (Council of the District of Columbia; A.1, direct artifact inspection, confidence high) | Tax Table VI [[FACT:dc.sui.employer.rate.min=1.9]]%-[[FACT:dc.sui.employer.rate.max=7.4]]% (51-103(c)(8)(A)). |
| `dc.sui.new_employer.rate` | [[FACT:dc.sui.new_employer.rate=2.7]] % | 2026-01-01 to open | US-DCS5-016 (DC Department of Employment Services; A.2, second independent authority, confidence high) |  |
| `dc.sui.wage_base` | [[FACT:dc.sui.wage_base=9,000]] USD | 2026-01-01 to open | US-DCS5-017 (Council of the District of Columbia; A.1, direct artifact inspection, confidence high) | 51-103(e)(6); fixed. No explicit other-state credit found (open). |

Not configured in this release [[GAP:RQ-141]]: 51-103(e)(6) as read states no explicit credit for wages subject to another state UI.

## DC.4 Pay statement

Electronic delivery: no DC rule found. Reach follows 32-1003(b)/(b-1) coverage (inference).

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `dc.hire_notice.language` | [[FACT:dc.hire_notice.language=English and also the employee primary language where a Mayor template exists (32-1008(c))]] | 2026-01-01 to open | US-DCS5-010 (Council of the District of Columbia; A.1, direct artifact inspection, confidence high) |  |
| `dc.payslip.items` | [[FACT:dc.payslip.items=date of payment; gross wages; deductions and additions with separate gratuities line; net wages; hours worked; tip-declaration form split cash/card; from 2026-01-01 list of compensation sources beyond base wages and tips]] | 2026-01-01 to open | US-DCS5-010 (Council of the District of Columbia; A.1, direct artifact inspection, confidence high) | 32-1008(b), (b)(6A). |

Not configured in this release [[GAP:RQ-142]]: No DC rule found for electronic payslips, direct deposit, deduction authorisation or SSN truncation.

## DC.5 Statutory reporting

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `dc.newhire.report_days` | [[FACT:dc.newhire.report_days=20]] days | 2026-01-01 to open | US-DCS5-022 (Council of the District of Columbia; A.1, direct artifact inspection, confidence high) | dc-newhire.com online/mail/fax; employee name/address/SSN, employer name/address/FEIN, hire date; penalty 25/employee. |
| `dc.report.pfl.quarterly` | [[FACT:dc.report.pfl.quarterly=same ESSP channel and due dates (Apr 30, Jul 31, Oct 31, Jan 31)]] | 2026-01-01 to open | US-DCS5-019 (DC DOES Office of Paid Family Leave; A.2, second independent authority, confidence high) |  |
| `dc.report.sui.quarterly` | [[FACT:dc.report.sui.quarterly=UC-30 via DOES ESSP, due last day of month after quarter; household annual April 15; 250+ employees machine-readable; penalty 10% (min 100), interest 1.5%/month]] | 2026-01-01 to open | US-DCS5-018 (Council of the District of Columbia; A.1, direct artifact inspection, confidence high) |  |
| `dc.report.w2` | [[FACT:dc.report.w2=EFW2/EFW2C with required RS record via MyTax.DC.gov; mandatory electronic at 25+ forms (else paper with WT or manual entry); due January 31]] | 2025-01-01 to open | US-DCS5-015 (DC Office of Tax and Revenue; A.2, direct artifact inspection, confidence medium) | TY2025 edition read; TY2026 not yet published. |
| `dc.report.w2.efile_threshold` | [[FACT:dc.report.w2.efile_threshold=25]] forms | 2025-01-01 to open | US-DCS5-015 (DC Office of Tax and Revenue; A.2, direct artifact inspection, confidence high) |  |
| `dc.report.wh.fr900q` | [[FACT:dc.report.wh.fr900q=FR-900Q electronic on MyTax.DC.gov (mandatory since TY2023); deposits weekly/semi-weekly/monthly/quarterly as assigned by 20th of following month; returns due Apr 30, Jul 31, Oct 31, Jan 31; zero return required; payments over 5,000 electronic (ACH code 00300); FR-900A annual if under 200/yr]] | 2026-01-01 to open | US-DCS5-014 (DC Office of Tax and Revenue; A.2, direct artifact inspection, confidence high) |  |

Not configured in this release [[GAP:RQ-143]]: UC-30 / ESSP bulk-upload field layout is behind the employer login (behind the employer login).

## DC.6 Leave

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `dc.leave.sick.accrual.100_plus` | [[FACT:dc.leave.sick.accrual.100_plus=1 h per 37 h worked, up to 7 days/yr]] | 2026-01-01 to open | US-DCS5-004 (Council of the District of Columbia; A.1, direct artifact inspection, confidence high) | 25-99: 1/43 up to 5 days; <=24: 1/87 up to 3 days; tipped restaurant/bar 1/43 up to 5 days at full MW; use after 90 days; reinstated on rehire within 1 year. |
| `dc.leave.sick.accrual.25_99` | [[FACT:dc.leave.sick.accrual.25_99=1 h per 43 h worked, up to 5 days/yr]] | 2026-01-01 to open | US-DCS5-004 (Council of the District of Columbia; A.1, direct artifact inspection, confidence high) |  |
| `dc.leave.sick.accrual.under_25` | [[FACT:dc.leave.sick.accrual.under_25=1 h per 87 h worked, up to 3 days/yr]] | 2026-01-01 to open | US-DCS5-004 (Council of the District of Columbia; A.1, direct artifact inspection, confidence high) |  |
| `dc.leave.sick.payout_on_separation` | [[FACT:dc.leave.sick.payout_on_separation=False]] | 2026-01-01 to open | US-DCS5-024 (DC Department of Employment Services, Office of Wage-Hour; A.3, second independent authority, confidence medium) |  |

Not configured in this release [[GAP:RQ-144]]: DOES fact sheet says at least 50% of time in DC while 32-1003(b) and 32-541.01 say more than 50%.

## DC.7 Termination and final pay

Accrued vacation payout: no statutory rule (policy). UI separation notice: no DC form found.

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `dc.final_pay.rule` | [[FACT:dc.final_pay.rule=discharge: working day after (4 days if employee handled employer money); resignation: next regular payday or 7 days, whichever first; liquidated damages lesser of 10%/working day or treble; CBA may override]] | 2026-01-01 to open | US-DCS5-003 (Council of the District of Columbia; A.1, direct artifact inspection, confidence high) |  |

Not configured in this release [[GAP:RQ-145]]: No DC statutory rule found for vacation payout or a UI separation notice.

## DC.8 Benefits in kind and taxable wages

DC income tax starts from federal gross income: federal exclusions (401(k), s.125, HSA, transit, GTL) flow through (47-1803.02 not read). UI wages include non-cash and customary tips, exclude employer retirement/sickness/medical/death plans [US-DCS5-008].

## DC.9 Deductions and garnishments

Child support: OAG CSSD sends IWO within 2 business days of the new-hire entry [US-DCS5-022]; DC fees/priority not read. No DC wage-deduction authorisation rule read.

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `dc.garn.creditor.rule` | [[FACT:dc.garn.creditor.rule=max 25% of weekly disposable wages exceeding 40 x DC minimum wage; one attachment at a time (16-572)]] | 2026-01-01 to open | US-DCS5-006 (Council of the District of Columbia; A.1, direct artifact inspection, confidence high) |  |
| `dc.garn.creditor.weekly_threshold` | [[FACT:dc.garn.creditor.weekly_threshold=736]] USD | 2026-07-01 to open | US-DCS5-006 (Council of the District of Columbia; A.1, derived arithmetically, confidence high) | 40 x [[FACT:dc.minwage.hourly=18.40]]. |

## DC.10 Collective agreements and prevailing wage

Prevailing wage (public works) is an optional informational flag [US-OWN-009]: this guide documents prevailing-wage laws, thresholds and certified-payroll duties as an overlay, and the payroll build does not produce certified payroll reports.

Sector prevailing wage for underground electrical and gas utility work at Davis-Bacon rates [US-DCP52-005].

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `dc.living_wage.contract_threshold` | [[FACT:dc.living_wage.contract_threshold=100,000]] USD | 2026-01-01 to open | US-DCS5-009 (Council of the District of Columbia; A.1, direct artifact inspection, confidence high) |  |
| `dc.living_wage.hourly` | [[FACT:dc.living_wage.hourly=17.95]] USD | 2026-01-01 to 2026-06-30 | US-DCS5-012 (DC Department of Employment Services, Office of Wage-Hour; A.2, second independent authority, confidence high) | DC contractors/assistance >= [[FACT:dc.living_wage.contract_threshold=100,000]] (subs 15,000/50,000) [US-DCS5-009]; CPI-U capped 3% each 1 Jan; floor = minimum wage. |
| `dc.living_wage.hourly` | [[FACT:dc.living_wage.hourly=18.40]] USD | 2026-07-01 to open | US-DCS5-012 (DC Department of Employment Services, Office of Wage-Hour; A.2, second independent authority, confidence high) |  |

## DC.11 Indexation

MW July 1 CPI-U Washington MSA (0.05); tipped % of MW; living wage Jan 1 CPI-U capped 3%; SUI base fixed; PFL rate statutory; PFL max benefit CPI from 2026-10-01; DC standard deduction COLA (assessment); brackets not indexed.

## DC.12 Payroll data protection and records

New-hire reports carry the SSN; no truncation rule found; D.C. Code 28-3851 not read.

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `dc.records.retention_years` | [[FACT:dc.records.retention_years=3]] years | 2026-01-01 to open | US-DCS5-010 (Council of the District of Columbia; A.1, direct artifact inspection, confidence high) | Or federal standard if longer; DOB for employees under 19. |

## DC.13 Live legal change

D.C. Act 26-416 (emergency, 2026-08-13 to ~2026-11-11; status of the permanent FY2027 BSA unconfirmed); D.C. Law 26-55 (in force 2025-12-06: tipped %, compensation-sources payslip line); MW [[FACT:dc.minwage.hourly=18.40]] / tipped [[FACT:dc.minwage.tipped.cash_wage=10.30]] from 2026-07-01; D.C. Law 26-89 and Act 26-214 amend lump-sum retirement withholding only.

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `dc.live.fy2027_bsa_permanent` | [[FACT:dc.live.fy2027_bsa_permanent=B26-0661 Fiscal Year 2027 Budget Support Act of 2026: enacted without the Mayor's signature 2026-08-14 as D.C. Act 26-418 (73 DCR 11735); transmitted to Congress 2026-08-20; D.C. Law 26-189 effective 2026-10-02 (73 DCR 13120). Status: IN FORCE (congressional review complete), before the emergency Act 26-416 lapses.]] Not yet published [[GAP:RQ-146]]: Value not final. | 2026-10-02 to open | US-DCB5-301 (Council of the District of Columbia; A.1, quoted from authority page, confidence high) | Status confirmed on Council LIMS (verbatim excerpt). NOT checked: that Law 26-189 carries the same tax (7112) and PFL (4051-4053) text as Act 26-416 - see unresolved dc.live.fy2027_bsa_permanent. |

Not yet published [[GAP:RQ-146]]: The permanent FY2027 BSA is D.C. Law 26-189, in force from 2026-10-02 (fact dc.live.fy2027_bsa_permanent). Whether its tax (secs. 7111-7113) and PFL (secs. 4051-4053) text is identical to the emergency Act 26-416 the annex models was not compared (214-page text not read).

## DC.14 Authority worked examples (oracle values)

No published state worked example is recorded for this jurisdiction.

## DC.15 Special populations

- Domestic: covered by MW; household withholding on FR-900Q; UI annual April 15; casual babysitters excluded from ASSLA [US-DCS5-013, US-DCS5-018, US-DCS5-005].
- Agricultural: no DC rule (federal).
- Minors: no youth subminimum; DOB on records under 19 [US-DCS5-001, US-DCS5-010].
- Tipped: [[FACT:dc.minwage.tipped.cash_wage=10.30]] with top-up; mandatory third-party payroll (non-hotel); tip lines on payslip; ASSLA 1/43 at full MW [US-DCS5-001, US-DCS5-010, US-DCS5-011, US-DCS5-004].
- Clergy and students: excluded from ASSLA [US-DCS5-005].
- Nonresidents incl. NRAs living outside DC: no DC withholding with D-4A [US-DCP51-006, US-MULTI-016].
- Government: DC government excluded from tipped schedule, covered by ASSLA; District reimburses UI [US-DCS5-001, US-DCS5-005, US-DCS5-017].
- Security officers in office buildings: SCA Guard 1 wage + fringe; workers with disabilities: MW unless 14(c) certificate [US-DCS5-001].

## DC.16 Language

Hire notice in English and the primary language where a Mayor template exists (32-1008(c)) [US-DCS5-010]; payslip English (US-OWN-006). DC postings page unreadable.

## DC.S Sources

The legal basis of each value (legal-basis register id, authority, source tier and verification method) is given in the row that carries it.
