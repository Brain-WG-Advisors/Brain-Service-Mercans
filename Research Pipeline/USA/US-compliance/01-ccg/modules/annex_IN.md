# Annex IN: Indiana

**Layer classification (T3).** T3: separate state withholding calculation and state return; no local layer, or a local layer piggybacked on the state return. Source: build manifest tier census, local income tax domain.

**Summary.** Minimum wage tracks the FLSA ([[FACT:in.minwage.hourly=7.25]]; state law covers only non-FLSA employers with 2+ employees); local mandates pre-empted; weekly overtime. State PIT [[FACT:in.pit.rate=2.95]]% ([[FACT:in.pit.rate=2.90]]% from 2027 per DOR) plus county LIT in all 92 counties (rate by Jan-1 county, chart R47/10-26 from 2026-10-01: Boone [[FACT:in.local.lit.rate.boone=0.0171]]); WH-4 exemptions [[FACT:in.wh.exemption.personal=1,000]]/[[FACT:in.wh.exemption.dependent=1,500]]/[[FACT:in.wh.exemption.adopted_child=3,000]]; supplemental flat [[FACT:in.pit.rate=2.95]]% + county; 30-day nonresident safe harbor; reciprocity KY/MI/OH/PA/WI (county still withheld). UI employer-only, base [[FACT:in.sui.wage_base=9,500]], new [[FACT:in.sui.new_employer.rate=2.5]]%. Pay-statement duty literally limited to non-FLSA employers. Oracle: DN#1 example [[FACT:in.oracle.dn1.example.state=13.96]] + [[FACT:in.oracle.dn1.example.county=4.73]].

Each parameter row gives its key, the period in force and its legal basis: the legal-basis register row, the authority, the source tier and how the value was verified.

## IN.1 Employment and labour code

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `in.late_wages.liquidated_damages_multiple` | [[FACT:in.late_wages.liquidated_damages_multiple=2]] ratio | 2026-01-01 to open | US-INS5-003 (Indiana General Assembly (iga.in.gov); A.1, direct artifact inspection, confidence high) | 22-2-5-2 if not in good faith, plus attorney fees. |
| `in.local_mandates.preempted` | [[FACT:in.local_mandates.preempted=True]] | 2026-01-01 to open | US-INS5-002 (Indiana General Assembly (iga.in.gov); A.1, direct artifact inspection, confidence high) | IC 22-2-2-10.5 (MW) and 22-2-16-3 (benefits/leave); not for a unit's own employees. |
| `in.minwage.hourly` | [[FACT:in.minwage.hourly=7.25]] USD | 2009-07-24 to open | US-INS5-001 (Indiana General Assembly (iga.in.gov); A.1, direct artifact inspection, confidence high) | IC 22-2-2-4(c): state minimum = FLSA minimum; state law covers employers with 2+ employees NOT subject to FLSA MW (22-2-2-3). |
| `in.minwage.tipped.cash_wage` | [[FACT:in.minwage.tipped.cash_wage=2.13]] USD | 2026-01-01 to open | US-INS5-001 (Indiana General Assembly (iga.in.gov); A.1, direct artifact inspection, confidence high) |  |
| `in.overtime.weekly_threshold_hours` | [[FACT:in.overtime.weekly_threshold_hours=40]] hours | 2026-01-01 to open | US-INS5-001 (Indiana General Assembly (iga.in.gov); A.1, direct artifact inspection, confidence high) | 1.5x; no daily OT; hospitals 14-day/80 h with 8 h daily trigger; domestic covered. |
| `in.pay_frequency.rule` | [[FACT:in.pay_frequency.rule=at least semimonthly, or biweekly on request; pay covers wages up to no more than 10 business days before payday (IC 22-2-5-1)]] | 2026-01-01 to open | US-INS5-003 (Indiana General Assembly (iga.in.gov); A.1, direct artifact inspection, confidence high) |  |
| `in.payment.method` | [[FACT:in.payment.method=US money, negotiable check, draft, money order, or electronic transfer to institution designated by employee; paycards not named; DD cannot be forced (75%)]] | 2026-01-01 to open | US-INS5-003 (Indiana General Assembly (iga.in.gov); A.1, direct artifact inspection, confidence high) |  |

## IN.2 State income tax withholding

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `in.pit.rate` | [[FACT:in.pit.rate=2.95]] % | 2026-01-01 to 2026-12-31 | US-INS5-009 (Indiana Department of Revenue; A.2, quoted from authority page, confidence high) | IC 6-3-2-1 not read (SPA); DOR rates page. |
| `in.pit.rate` | [[FACT:in.pit.rate=2.9]] % | 2027-01-01 to open | US-INS5-009 (Indiana Department of Revenue; A.2, quoted from authority page, confidence medium) | DOR: "will adjust in 2027 to [[FACT:in.pit.rate=2.90]]%"; statute not read. |
| `in.wh.certificate` | [[FACT:in.wh.certificate=WH-4 (State Form 48845, R10/8-23): counties of residence and principal employment as of Jan 1; additional state/county lines 9-10; new WH-4 within 10 days when exemptions decrease]] | 2023-08-01 to open | US-INS5-021 (Indiana Department of Revenue; A.3, direct artifact inspection, confidence high) |  |
| `in.wh.exemption.adopted_child` | [[FACT:in.wh.exemption.adopted_child=3,000]] USD | 2026-01-01 to open | US-INS5-007 (Indiana Department of Revenue; A.2, derived arithmetically, confidence high) | Line 8. |
| `in.wh.exemption.dependent` | [[FACT:in.wh.exemption.dependent=1,500]] USD | 2026-01-01 to open | US-INS5-007 (Indiana Department of Revenue; A.2, derived arithmetically, confidence high) | Lines 6 and 7 (first-time dependent one year only). |
| `in.wh.exemption.personal` | [[FACT:in.wh.exemption.personal=1,000]] USD | 2026-01-01 to open | US-INS5-007 (Indiana Department of Revenue; A.2, derived arithmetically, confidence high) | WH-4 line 5; not indexed. |
| `in.wh.method` | [[FACT:in.wh.method=taxable wages = gross per period - deduction constants (annual / 52, 26, 24, 12, 365); x 2.95% state and x county rate; 2-decimal constants and results]] | 2026-10-01 to open | US-INS5-007 (Indiana Department of Revenue; A.2, derived arithmetically, confidence high) | DN#1 R47/10-26 effective 2026-10-01 supersedes R46/01-26 (US-IN-001, effective_to 2026-09-30). |
| `in.wh.supplemental.rate` | [[FACT:in.wh.supplemental.rate=2.95]] % | 2026-01-01 to 2026-12-31 | US-INS5-007 (Indiana Department of Revenue; A.2, derived arithmetically, confidence high) | Flat state rate plus county rate, no exemptions; Indiana does not follow IRC 3402(n). |

⚠️ RESEARCH-GAP: [[FACT:in.pit.rate=2.90]]% for 2027 rests on the DOR page alone; IC 6-3-2-1 unread (iga.in.gov SPA). (open item `in.pit.rate.next_year.statute`, non-blocking; would close it: IC 6-3-2-1 from the 2026 IC Title 6 Article 3 PDF.)

⚠️ RESEARCH-GAP: IRC conformity date and HSA/s.125/transit departures not read. (open item `in.pit.conformity`, non-blocking; would close it: IC 6-3-1-11 (2026) or DOR IT-40 2025 instructions, Add-backs.)

## IN.2b Non-resident regime and reciprocity

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `in.nonres.safe_harbor_days` | [[FACT:in.nonres.safe_harbor_days=30]] days | 2024-01-01 to open | US-INS5-007 (Indiana Department of Revenue; A.2, derived arithmetically, confidence high) | IC 6-3-2-27.5: no state/county withholding when expected <= 30 days in Indiana; time-and-attendance system or WH-4AFF; catch-up once exceeded. |
| `in.reciprocity.states` | [[FACT:in.reciprocity.states=KY, MI, OH, PA, WI]] | 2026-01-01 to open | US-INS5-012 (Indiana Department of Revenue; A.3, quoted from authority page, confidence high) | WH-47; no state tax, but county tax withheld if principal work county on Jan 1 is in Indiana [US-IN-002, US-INS5-008]. NRAs: one exemption only on WH-4. |

## IN.2c Local wage taxes

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `in.local.lit.change_calendar` | [[FACT:in.local.lit.change_calendar=ordinance Jan 1-Aug 31 -> effective Oct 1 same year; Sep 1-Oct 31 -> Jan 1 next year; Nov 1-Dec 31 -> Oct 1 next year]] | 2026-01-01 to open | US-INS5-008 (Indiana Department of Revenue; A.2, direct artifact inspection, confidence high) |  |
| `in.local.lit.county_basis` | [[FACT:in.local.lit.county_basis=county of residence on Jan 1 (out-of-state residents: county of principal work on Jan 1), fixed for the year; withheld and reported with state tax on WH-1/WH-3/W-2 RS (T3 piggyback); no separate nonresident rate]] | 2026-01-01 to open | US-INS5-008 (Indiana Department of Revenue; A.2, direct artifact inspection, confidence high) |  |
| `in.local.lit.rate.boone` | [[FACT:in.local.lit.rate.boone=0.017]] ratio | 2026-01-01 to 2026-09-30 | US-IN-001 (Indiana Department of Revenue; A.2, direct artifact inspection, confidence high) | DN#1 R46/01-26 county chart (local copy inspected: Boone [[FACT:in.local.lit.rate.boone=0.017]], Marion [[FACT:in.local.lit.rate.marion=0.0202]], Porter [[FACT:in.local.lit.rate.min=0.005]], Randolph [[FACT:in.local.lit.rate.max=0.03]]); periods 2026-01-01..2026-09-30; replaced by R47 (US-INS5-007) from 2026-10-01. |
| `in.local.lit.rate.boone` | [[FACT:in.local.lit.rate.boone=0.0171]] ratio | 2026-10-01 to open | US-INS5-007 (Indiana Department of Revenue; A.2, derived arithmetically, confidence high) | Was [[FACT:in.local.lit.rate.boone=0.017]] to 2026-09-30 (R46). |
| `in.local.lit.rate.marion` | [[FACT:in.local.lit.rate.marion=0.0202]] ratio | 2026-01-01 to 2026-09-30 | US-IN-001 (Indiana Department of Revenue; A.2, direct artifact inspection, confidence high) | DN#1 R46/01-26 county chart (local copy inspected: Boone [[FACT:in.local.lit.rate.boone=0.017]], Marion [[FACT:in.local.lit.rate.marion=0.0202]], Porter [[FACT:in.local.lit.rate.min=0.005]], Randolph [[FACT:in.local.lit.rate.max=0.03]]); periods 2026-01-01..2026-09-30; replaced by R47 (US-INS5-007) from 2026-10-01. |
| `in.local.lit.rate.marion` | [[FACT:in.local.lit.rate.marion=0.0202]] ratio | 2026-10-01 to open | US-INS5-007 (Indiana Department of Revenue; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-INS5-007. |
| `in.local.lit.rate.max` | [[FACT:in.local.lit.rate.max=0.03]] ratio | 2026-01-01 to 2026-09-30 | US-IN-001 (Indiana Department of Revenue; A.2, direct artifact inspection, confidence high) | DN#1 R46/01-26 county chart (local copy inspected: Boone [[FACT:in.local.lit.rate.boone=0.017]], Marion [[FACT:in.local.lit.rate.marion=0.0202]], Porter [[FACT:in.local.lit.rate.min=0.005]], Randolph [[FACT:in.local.lit.rate.max=0.03]]); periods 2026-01-01..2026-09-30; replaced by R47 (US-INS5-007) from 2026-10-01. |
| `in.local.lit.rate.max` | [[FACT:in.local.lit.rate.max=0.03]] ratio | 2026-10-01 to open | US-INS5-007 (Indiana Department of Revenue; A.2, derived arithmetically, confidence high) | Randolph. Full 92-county chart in DN#1 R47/10-26 (the full county chart is the configuration source). |
| `in.local.lit.rate.min` | [[FACT:in.local.lit.rate.min=0.005]] ratio | 2026-01-01 to 2026-09-30 | US-IN-001 (Indiana Department of Revenue; A.2, direct artifact inspection, confidence high) | DN#1 R46/01-26 county chart (local copy inspected: Boone [[FACT:in.local.lit.rate.boone=0.017]], Marion [[FACT:in.local.lit.rate.marion=0.0202]], Porter [[FACT:in.local.lit.rate.min=0.005]], Randolph [[FACT:in.local.lit.rate.max=0.03]]); periods 2026-01-01..2026-09-30; replaced by R47 (US-INS5-007) from 2026-10-01. |
| `in.local.lit.rate.min` | [[FACT:in.local.lit.rate.min=0.005]] ratio | 2026-10-01 to open | US-INS5-007 (Indiana Department of Revenue; A.2, derived arithmetically, confidence high) | Porter. |

## IN.3 Social insurance (unemployment, disability, paid leave, levies)

No SDI/TDI/PFML/LTC/transit/workforce levy [US-INR3-002, US-KYR3-003, US-OWN-007]. Coverage: domestic [[FACT:in.wh.exemption.personal=1,000]] cash/quarter; agricultural 20,000/quarter or 10 in 20 weeks; clergy excluded.

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `in.sui.employee.rate` | [[FACT:in.sui.employee.rate=0]] % | 2026-01-01 to open | US-INS5-014 (Indiana Department of Workforce Development; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-INS5-014. |
| `in.sui.employer.rate.max` | [[FACT:in.sui.employer.rate.max=7.4]] % | 2026-01-01 to open | US-INS5-014 (Indiana Department of Workforce Development; A.2, derived arithmetically, confidence medium) | Good standing; delinquent max 9.40%; penalty rate computed + 2% [US-INS5-015 partial]. 2026 solvency surcharge/schedule not obtained. |
| `in.sui.employer.rate.min` | [[FACT:in.sui.employer.rate.min=0.5]] % | 2026-01-01 to open | US-INS5-014 (Indiana Department of Workforce Development; A.2, derived arithmetically, confidence medium) | [[FACT:in.sui.wage_base=9,500]] x [[FACT:in.sui.employer.rate.min=0.50]]% = 47.50 (table check). |
| `in.sui.new_employer.rate` | [[FACT:in.sui.new_employer.rate=2.5]] % | 2026-01-01 to open | US-INS5-014 (Indiana Department of Workforce Development; A.2, derived arithmetically, confidence medium) | First 4 calendar years; construction lesser of 4.0% or construction average ([[FACT:in.sui.new_employer.rate=2.50]]% for 2025); government 1.6% [US-IN-003]. |
| `in.sui.wage_base` | [[FACT:in.sui.wage_base=9,500]] USD | 2011-01-01 to open | US-INS5-014 (Indiana Department of Workforce Development; A.2, derived arithmetically, confidence medium) | Not indexed; no 2026-labelled DWD page; IC 22-4-4-2 not read. |

⚠️ RESEARCH-GAP: 2026 solvency surcharge, applied-rate schedule and a 2026-labelled wage base not obtained (partial row). (open item `in.sui.rate_year.current`, non-blocking; would close it: DWD state-premium-rate page as currently published, or IC 22-4-4-2 / 22-4-11-3.3 from the 2026 IC PDF.)

## IN.4 Pay statement

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `in.payslip.items` | [[FACT:in.payslip.items=hours worked, wages paid, deductions made, each pay period (IC 22-2-2-8(a))]] | 2026-01-01 to open | US-INS5-001 (Indiana General Assembly (iga.in.gov); A.1, direct artifact inspection, confidence medium) | Scope: binds employers subject to the chapter = 2+ employees NOT subject to FLSA MW (literal reading 70%); build emits the three items anyway. No e-delivery/retention clause; federal 3-year fallback. |

⚠️ RESEARCH-GAP: IC 22-2-2-8 binds only employers "subject to this chapter" = non-FLSA employers (22-2-2-3); literal reading excludes most employers. (open item `in.payslip.scope`, non-blocking; would close it: Owner decision; or IDOL guidance on 22-2-2-8 scope. Recommendation: emit hours, wages, deductions anyway.)

## IN.5 Statutory reporting

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `in.newhire.report_days` | [[FACT:in.newhire.report_days=20]] days | 2024-07-01 to open | US-INS5-016 (Indiana New Hire Reporting Center (State of Indiana; operated by contractor Stellarware); A.3, second independent authority, confidence high) | in-newhire.com, electronic only since 2024-07-01 (SB 148-2024, 4 extra fields); rehire after 60+ days; penalty 25 / 500. |
| `in.report.annual.wh3` | [[FACT:in.report.annual.wh3=WH-3 + state W-2 due Jan 31; electronic mandatory above 25 statements (IC 6-3-4-16.5); XML (schema IDORWTH2016V1.0 not downloaded) / IRIS XML / EFW2 for existing filers; DOR FAQ "Feb 28" conflicts - use Jan 31]] | 2026-01-01 to open | US-INS5-011 (Indiana Department of Revenue; A.2, direct artifact inspection, confidence high) | 1220 flat file retired 2027-09 [US-INS5-010]. |
| `in.report.sui.quarterly` | [[FACT:in.report.sui.quarterly=DWD E S S/UPLINK due Apr 30, Jul 31, Oct 31, Jan 31; electronic filing (646 IAC 5-2-2) and payment (5-2-17) mandatory; penalty 25 per missing report]] | 2019-01-01 to open | US-INS5-014 (Indiana Department of Workforce Development; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-INS5-014. |
| `in.report.w2.efile_threshold` | [[FACT:in.report.w2.efile_threshold=25]] statements | 2026-01-01 to open | US-INS5-011 (Indiana Department of Revenue; A.2, direct artifact inspection, confidence high) |  |
| `in.report.wh.wh1` | [[FACT:in.report.wh.wh1=WH-1 via INTIME (online or upload < 10 MB) or SFTP; annual if monthly average <= 83.33, monthly if <= 1,000 (30 days after month end), early filer above]] | 2026-01-01 to open | US-INS5-010 (Indiana Department of Revenue; A.2, quoted from authority page, confidence medium) |  |

⚠️ RESEARCH-GAP: WH-1/WH-3 XML schema IDORWTH2016V1.0 and business rules not downloaded; EFW2 guide labelled 2025 and prior. (open item `in.report.wh.xml_schema`, non-blocking; would close it: Schema files and TY2026 EFW2 guide fetched from a US exit.)

## IN.6 Leave

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `in.leave.military_family.days` | [[FACT:in.leave.military_family.days=10]] working days | 2026-01-01 to open | US-INS5-006 (Indiana General Assembly (iga.in.gov); A.1, direct artifact inspection, confidence high) | IC 22-2-13: unpaid, 12 months and [[FACT:in.wh.exemption.dependent=1,500]] hours. |
| `in.leave.sick.state_mandate.exists` | [[FACT:in.leave.sick.state_mandate.exists=False]] | 2026-01-01 to open | US-INS5-002 (Indiana General Assembly (iga.in.gov); A.1, direct artifact inspection, confidence high) |  |

⚠️ RESEARCH-GAP: Jury duty (IC 34-28-4), voting, volunteer firefighter leave not researched. (open item `in.leave.other_mandated`, non-blocking; would close it: Those IC sections.)

## IN.7 Termination and final pay

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `in.final_pay.rule` | [[FACT:in.final_pay.rule=discharge: regular payday for the period of separation (22-2-9-2); resignation: next usual payday; employer pays conceded part of disputed amount (22-2-9-3)]] | 2026-01-01 to open | US-INS5-005 (Indiana General Assembly (iga.in.gov); A.1, direct artifact inspection, confidence high) | No vacation payout statute (open). No mandatory separation notice; answer DWD SF52984. |

⚠️ RESEARCH-GAP: No payout statute; case law (secondary source) treats promised vacation as wages. (open item `in.final_pay.accrued_vacation`, non-blocking; would close it: IDOL knowledge-base article or Indiana Supreme Court decision on courts.in.gov.)

## IN.8 Benefits in kind and taxable wages

Federal AGI start; withholding duty follows federal duty [US-INS5-012]. IRC conformity date and HSA/s.125/transit departures not read (low confidence).

## IN.9 Deductions and garnishments

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `in.deductions.overpayment_recovery` | [[FACT:in.deductions.overpayment_recovery=2 weeks notice; lesser of 25% of weekly disposable or excess over 30 x federal MW (IC 22-2-6-4)]] | 2026-01-01 to open | US-INS5-004 (Indiana General Assembly (iga.in.gov); A.1, direct artifact inspection, confidence high) |  |
| `in.deductions.wage_assignment` | [[FACT:in.deductions.wage_assignment=written, signed, revocable, employer-agreed, copy within 10 days, listed purpose (IC 22-2-6-2(b)); uniforms/tools lesser of 2,500/yr or 5% weekly disposable; no PPE charge; loan interest max prime + 4%]] | 2026-01-01 to open | US-INS5-004 (Indiana General Assembly (iga.in.gov); A.1, direct artifact inspection, confidence high) |  |
| `in.garn.child_support.employer_fee` | [[FACT:in.garn.child_support.employer_fee=2]] USD | 2026-01-01 to open | US-INS5-017 (Indiana Department of Child Services, Child Support Bureau; A.3, quoted from authority page, confidence high) | IC 31-16-15: start first period within 14 days after service; remit INSCCU each payday; 50+ employees with >1 order electronic; priority except current taxes; lump sums subject to arrears. |
| `in.garn.creditor.max_percent` | [[FACT:in.garn.creditor.max_percent=25]] % | 2026-01-01 to open | US-INS5-017 (Indiana Department of Child Services, Child Support Bureau; A.3, quoted from authority page, confidence high) | Statute moved to IC 37-2-6-4 (P.L.115-2026; effective date per a secondary source 2026-07-01) [US-INS5-020]. |

⚠️ RESEARCH-GAP: IC 37-2-6-4 text, effective date and any employer fee not read. (open item `in.garn.creditor.statute_text`, non-blocking; would close it: IC Title 37 Article 2 (2026).)

## IN.10 Collective agreements and prevailing wage

No state prevailing wage since 2015-07-01 (HEA 1019-2015) [US-INR3-005, US-INR3-006].

## IN.11 Indexation

MW tracks FLSA; SUI base fixed since 2011; PIT statutory step [[FACT:in.pit.rate=2.95]]% -> [[FACT:in.pit.rate=2.9]]%; LIT by county ordinance (Jan 1 / Oct 1); WH-4 amounts not indexed.

## IN.12 Payroll data protection and records

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `in.breach.ag_penalty_max` | [[FACT:in.breach.ag_penalty_max=150,000]] USD | 2026-01-01 to open | US-INS5-018 (Indiana Office of the Attorney General, Consumer Protection Division; A.3, quoted from authority page, confidence medium) | [partial row] [partial] IC 24-4.9. |

## IN.13 Live legal change

P.L.104-2026 political-subdivision deferred-retirement assignment; P.L.115-2026 UCCC recodified (garnishment cite IC 37-2-6-4); SEA 1-2025 municipal LIT from 2028 (secondary-source detail only, US-INS5-019); 1220 flat file retired 2027-09.

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `in.live.dn1_r47` | [[FACT:in.live.dn1_r47=DN#1 R47/10-26 in force 2026-10-01 (Boone LIT 0.017 -> 0.0171); level withholding]] | 2026-10-01 to open | US-INS5-007 (Indiana Department of Revenue; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-INS5-007. |

## IN.14 Worked examples

Each example is computed from the statutory parameters listed in this annex and checked against the result published by the authority. Amounts round half-up to the cent unless the line states another rule.

**Example IN-1: weekly wages 800.00 with deduction constants A5, B3, B1 and C2, county rate 1.00% as used in the Departmental Notice 1 example (payroll from 2026-10-01).**

| Line | Calculation | Result |
|---|---|---|
| Constant A5 | 5 x [[FACT:in.wh.exemption.personal=1,000]] / 52, two decimals | 96.15 |
| Constant B3 | 3 x [[FACT:in.wh.exemption.dependent=1,500]] / 52, two decimals | 86.54 |
| Constant B1 | 1 x [[FACT:in.wh.exemption.dependent=1,500]] / 52, two decimals | 28.85 |
| Constant C2 | 2 x [[FACT:in.wh.exemption.adopted_child=3,000]] / 52, two decimals | 115.38 |
| Total constants | 96.15 + 86.54 + 28.85 + 115.38 | 326.92 |
| Taxable wages | 800.00 - 326.92 | 473.08 |
| State withholding | 473.08 x [[FACT:in.pit.rate=2.95]] % = 13.9559, half-up to the cent | [[FACT:in.oracle.dn1.example.state=13.96]] |
| County withholding | 473.08 x 1.00 % (example county rate) = 4.7308 | [[FACT:in.oracle.dn1.example.county=4.73]] |

Computed result = published [[FACT:in.oracle.dn1.example.state=13.96]] (match); [[FACT:in.oracle.dn1.example.county=4.73]] = published [[FACT:in.oracle.dn1.example.county=4.73]] (match). The county rate in production is the employee's county rate from the county chart (IN.2c).

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `in.oracle.dn1.example.county` | [[FACT:in.oracle.dn1.example.county=4.73]] USD | 2026-10-01 to open | US-INS5-007 (Indiana Department of Revenue; A.2, derived arithmetically, confidence high) | 473.08 x 0.01 = [[FACT:in.oracle.dn1.example.county=4.73]]. |
| `in.oracle.dn1.example.state` | [[FACT:in.oracle.dn1.example.state=13.96]] USD | 2026-10-01 to open | US-INS5-007 (Indiana Department of Revenue; A.2, derived arithmetically, confidence high) | Weekly 800; constants A5 96.15 + B3 86.54 + B1 28.85 + C2 115.38 = 326.92; taxable 473.08 x 0.0295 = [[FACT:in.oracle.dn1.example.state=13.96]]. |

## IN.15 Special populations

- Domestic: state MW law only via FLSA coverage; 40 h OT applies; agency companionship excluded; UI [[FACT:in.wh.exemption.personal=1,000]] cash/quarter; may opt out of withholding [US-INS5-001, US-INS5-014, US-INS5-012].
- Agricultural: excluded from state MW and pay-frequency chapter; UI 20,000/quarter or 10 in 20 weeks [US-INS5-001, US-INS5-003, US-INS5-014].
- Minors: under 16 excluded from state MW; hours limits only [US-INS5-001].
- Tipped: [[FACT:in.minwage.tipped.cash_wage=2.13]] + tip credit [US-INS5-001].
- Clergy: excluded from state MW; ministers may choose no withholding; UI-excluded [US-INS5-001, US-INS5-012, US-INS5-014].
- Students: own-school and student nurses excluded from MW [US-INS5-001, US-INS5-021].
- NRAs: one exemption [US-INS5-021]. Nonresidents: 30-day safe harbor; reciprocity with county still withheld [US-INS5-007].
- Commission-only/outside sales: excluded from MW [US-INS5-001].
- Government: wage-assignment chapter applies; UI 1.6% or reimbursable [US-INS5-004, US-INS5-014].
- Casual laborers / pensioners: may choose no withholding [US-INS5-012].

## IN.16 Language of employee documents

IC 22-2-2-8 has no language clause; bilingual expressly permitted [US-INP6-001, US-INP9L-001]; payslip English (US-OWN-006).
