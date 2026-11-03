# Annex KS: Kansas


**Layer classification (T3).** T3: separate state withholding calculation and state return; no local layer, or a local layer piggybacked on the state return. Source: build manifest tier census, local income tax domain.

**Summary.** Minimum wage [[FACT:ks.minwage.hourly=7.25]] (state law only for non-FLSA employers; OT after 46 h for them); local mandates pre-empted. Withholding: KW-100 tables in force since 2024-07-01, two rates [[FACT:ks.pit.bracket.1.rate=5.2]]% / [[FACT:ks.pit.bracket.2.rate=5.58]]%; SB 269 rate-cut trigger NOT met for 2026 or 2027; K-4 allowances [[FACT:ks.pit.exemption.single=9,160]] / [[FACT:ks.pit.exemption.mfj=18,320]] / [[FACT:ks.pit.exemption.dependent=2,320]]; supplemental 5%; no reciprocity, no local tax. UI employer-only, base [[FACT:ks.sui.wage_base=15,100]] (25% of SAAW, indexed from 2026), Schedule C 0%-[[FACT:ks.sui.employer.rate.max=6.95]]%, new [[FACT:ks.sui.new_employer.rate=1.75]]% (construction [[FACT:ks.sui.new_employer.construction.rate=5.55]]%). No routine pay statement (deductions statement on request). New hire within 20 business days.

Each parameter row gives its key, the period in force and its legal basis: the legal-basis register row, the authority, the source tier and how the value was verified.

## KS.1 Employment and labour code

State MW/OT exclusions (44-1202(e)) [US-KSS5-009]: agriculture; private-home domestic; EAP and outside commission sales; federal employees; nonprofit volunteers; 18 or under occasional/part-time; USD EAP staff.

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ks.local_mandates.preempted` | [[FACT:ks.local_mandates.preempted=True]] | 2026-01-01 to open | US-KSS5-012 (Kansas Office of the Revisor of Statutes; A.1, direct artifact inspection, confidence high) | K.S.A. 12-16,130: wages, leave, benefits, scheduling. |
| `ks.minwage.hourly` | [[FACT:ks.minwage.hourly=7.25]] USD | 2010-01-01 to open | US-KSS5-008 (Kansas Office of the Revisor of Statutes; A.1, direct artifact inspection, confidence high) | K.S.A. 44-1203; not for FLSA-covered employers/employees; not indexed; SB 471 (16/h) died [US-KSS5-027]. |
| `ks.minwage.tipped.cash_wage` | [[FACT:ks.minwage.tipped.cash_wage=2.13]] USD | 2010-01-01 to open | US-KSS5-008 (Kansas Office of the Revisor of Statutes; A.1, direct artifact inspection, confidence high) |  |
| `ks.overtime.non_flsa.weekly_threshold_hours` | [[FACT:ks.overtime.non_flsa.weekly_threshold_hours=46]] hours | 2026-01-01 to open | US-KSS5-010 (Kansas Office of the Revisor of Statutes; A.1, direct artifact inspection, confidence high) | 44-1204: only employees not covered by FLSA s.7; EMS/fire/police 258 h per 28 days. FLSA 40 h governs most employers. |
| `ks.pay_frequency.rule` | [[FACT:ks.pay_frequency.rule=at least once per calendar month on designated paydays; period ends no more than 15 days before payday (44-314)]] | 2026-01-01 to open | US-KSS5-013 (Kansas Office of the Revisor of Statutes; A.1, direct artifact inspection, confidence high) |  |
| `ks.payment.method` | [[FACT:ks.payment.method=cash, check, EFT to designated account, or payroll card (one free withdrawal up to net pay per period, no fees); EFT-only employers offer default alternative; forum/education 30 days before EFT-only or card-only programme]] | 2026-01-01 to open | US-KSS5-013 (Kansas Office of the Revisor of Statutes; A.1, direct artifact inspection, confidence high) |  |

## KS.2 Income tax withholding

Configuration rule: withholding is computed with the KW-100 table parameters (`ks.wh.allowance.*`, `ks.wh.table.*`), whose bands already contain the standard deduction as a zero band. The statutory brackets, exemptions and standard deductions (`ks.pit.*`) are assessment parameters and must not be applied directly to wages in the withholding calculation.

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ks.pit.bracket.1.rate` | [[FACT:ks.pit.bracket.1.rate=5.2]] % | 2024-01-01 to open | US-KSS5-004 (Kansas Office of the Revisor of Statutes; A.1, direct artifact inspection, confidence high) |  |
| `ks.pit.bracket.2.rate` | [[FACT:ks.pit.bracket.2.rate=5.58]] % | 2024-01-01 to open | US-KSS5-004 (Kansas Office of the Revisor of Statutes; A.1, direct artifact inspection, confidence high) |  |
| `ks.pit.bracket.mfj.1.ceiling` | [[FACT:ks.pit.bracket.mfj.1.ceiling=46,000]] USD | 2024-01-01 to open | US-KSS5-004 (Kansas Office of the Revisor of Statutes; A.1, direct artifact inspection, confidence high) |  |
| `ks.pit.bracket.single.1.ceiling` | [[FACT:ks.pit.bracket.single.1.ceiling=23,000]] USD | 2024-01-01 to open | US-KSS5-004 (Kansas Office of the Revisor of Statutes; A.1, direct artifact inspection, confidence high) | K.S.A. 79-32,110: single/HoH/MFS [[FACT:ks.pit.bracket.1.rate=5.2]]% to [[FACT:ks.pit.bracket.single.1.ceiling=23,000]] then 1,196 + [[FACT:ks.pit.bracket.2.rate=5.58]]%; MFJ [[FACT:ks.pit.bracket.1.rate=5.2]]% to [[FACT:ks.pit.bracket.mfj.1.ceiling=46,000]] then 2,392 + [[FACT:ks.pit.bracket.2.rate=5.58]]%. |
| `ks.pit.exemption.dependent` | [[FACT:ks.pit.exemption.dependent=2,320]] USD | 2025-01-01 to open | US-KSS5-006 (Kansas Office of the Revisor of Statutes; A.1, direct artifact inspection, confidence high) |  |
| `ks.pit.exemption.mfj` | [[FACT:ks.pit.exemption.mfj=18,320]] USD | 2025-01-01 to open | US-KSS5-006 (Kansas Office of the Revisor of Statutes; A.1, direct artifact inspection, confidence high) |  |
| `ks.pit.exemption.single` | [[FACT:ks.pit.exemption.single=9,160]] USD | 2025-01-01 to open | US-KSS5-006 (Kansas Office of the Revisor of Statutes; A.1, direct artifact inspection, confidence high) | 79-32,121: [[FACT:ks.pit.exemption.mfj=18,320]] MFJ; [[FACT:ks.pit.exemption.dependent=2,320]] per dependent. |
| `ks.pit.rate_cut_trigger.2026` | [[FACT:ks.pit.rate_cut_trigger.2026=not triggered: FY2025 collections 88,481,523 below inflation-adjusted base (Notice 25-06)]] | 2026-01-01 to 2026-12-31 | US-KSS5-002 (Kansas Department of Revenue, Policy and Research; A.2, quoted from authority page, confidence high) |  |
| `ks.pit.rate_cut_trigger.2027` | [[FACT:ks.pit.rate_cut_trigger.2027=not triggered: FY2026 collections 214,339,364 below base (Notice 26-11, 2026-10-15)]] | 2027-01-01 to 2027-12-31 | US-KSS5-003 (Kansas Department of Revenue, Policy and Research; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-KSS5-003. |
| `ks.pit.std_deduction.married` | [[FACT:ks.pit.std_deduction.married=8,240]] USD | 2024-01-01 to open | US-KSS5-005 (Kansas Office of the Revisor of Statutes; A.1, direct artifact inspection, confidence high) |  |
| `ks.pit.std_deduction.single` | [[FACT:ks.pit.std_deduction.single=3,605]] USD | 2024-01-01 to open | US-KSS5-005 (Kansas Office of the Revisor of Statutes; A.1, direct artifact inspection, confidence high) | Married [[FACT:ks.pit.std_deduction.married=8,240]], HoH 6,180; fixed, not indexed. |
| `ks.wh.allowance.weekly.single` | [[FACT:ks.wh.allowance.weekly.single=176.15]] USD | 2024-07-01 to open | US-KSS5-001 (Kansas Department of Revenue; A.2, derived arithmetically, confidence high) | [[FACT:ks.pit.exemption.single=9,160]]/52; the joint and per-dependent weekly allowances are the annual amounts / 52. |
| `ks.wh.certificate` | [[FACT:ks.wh.certificate=K-4 (Rev. 7-24): Single or Joint allowance rate (married with earning spouse marks Single); no K-4 = Single, no allowance; exempt needs KDOR verification; federal W-4 not accepted]] | 2024-07-01 to open | US-KSS5-025 (Kansas Department of Revenue; A.2, direct artifact inspection, confidence high) |  |
| `ks.wh.method` | [[FACT:ks.wh.method=KW-100 (wages paid on and after 2024-07-01): gross - allowance for period (annual 9,160 Single / 18,320 Joint / 2,320 per dependent; HoH + one extra 2,320) then period table; annual Single 0% to 3,605, 5.2% to 26,605, then 1,196 + 5.58%; Married 0% to 8,240, 5.2% to 54,240, then 2,392 + 5.58%]] | 2024-07-01 to open | US-KSS5-001 (Kansas Department of Revenue; A.2, derived arithmetically, confidence high) | TRAP: table thresholds ([[FACT:ks.wh.table.single.band1_ceiling.annual=26,605]] / [[FACT:ks.wh.table.married.band1_ceiling.annual=54,240]]) = standard deduction + statutory band, not the statutory brackets ([[FACT:ks.pit.bracket.single.1.ceiling=23,000]] / [[FACT:ks.pit.bracket.mfj.1.ceiling=46,000]]). Period thresholds = the annual thresholds above divided by the number of pay periods in the year. KW-100 header still says "January 1, 2021" - figures are 2024 (never-do 6). |
| `ks.wh.rounding` | [[FACT:ks.wh.rounding=percentage-method result may be rounded to nearest dollar (under 50c down, 50c+ up)]] | 2024-07-01 to open | US-KSS5-001 (Kansas Department of Revenue; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-KSS5-001. |
| `ks.wh.supplemental.rate` | [[FACT:ks.wh.supplemental.rate=5]] % | 2024-07-01 to open | US-KSS5-001 (Kansas Department of Revenue; A.2, derived arithmetically, confidence high) | When stated separately with federal flat %, or other percentage-withheld payments; aggregated: tables. |
| `ks.wh.table.married.band1_ceiling.annual` | [[FACT:ks.wh.table.married.band1_ceiling.annual=54,240]] USD | 2024-07-01 to open | US-KSS5-001 (Kansas Department of Revenue; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-KSS5-001. |
| `ks.wh.table.married.zero_bracket.annual` | [[FACT:ks.wh.table.married.zero_bracket.annual=8,240]] USD | 2024-07-01 to open | US-KSS5-001 (Kansas Department of Revenue; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-KSS5-001. |
| `ks.wh.table.single.band1_ceiling.annual` | [[FACT:ks.wh.table.single.band1_ceiling.annual=26,605]] USD | 2024-07-01 to open | US-KSS5-001 (Kansas Department of Revenue; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-KSS5-001. |
| `ks.wh.table.single.zero_bracket.annual` | [[FACT:ks.wh.table.single.zero_bracket.annual=3,605]] USD | 2024-07-01 to open | US-KSS5-001 (Kansas Department of Revenue; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-KSS5-001. |

Not configured in this release [[GAP:RQ-217]]: 79-32,117(b)(vi) adds KPERS picked-up contributions to KS income; whether KS withholding applies to them on public-employer payroll is not stated.

## KS.2b Non-resident regime and reciprocity

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ks.nonres.rules` | [[FACT:ks.nonres.rules=full-time in KS: as resident; partly in KS: KS tax on total wages x KS share (hours/days/commissions), K-4C allocation; interstate carriers P.L. 91-569; residents working elsewhere: KS tax less other-state required withholding; NRAs withheld when federal applies; no reciprocity]] | 2024-07-01 to open | US-KSS5-001 (Kansas Department of Revenue; A.2, derived arithmetically, confidence high) | Level withholding; nonresident ratio at assessment (79-32,110(b)). |

## KS.2c Local wage taxes

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ks.local_wage_tax.exists` | [[FACT:ks.local_wage_tax.exists=False]] | 2026-01-01 to open | US-KSP9V-002 (Kansas Department of Revenue; A.2, direct artifact inspection, confidence medium) | KDOR tax list only wage item is withholding; 12-16,130 does not itself bar a local income tax. |

## KS.3 Social insurance: unemployment, disability, paid leave and payroll levies

No SDI/TDI/PFML [US-LAP52-002]; no levy beyond UI [US-KSP9V-001].

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ks.sui.employee.rate` | [[FACT:ks.sui.employee.rate=0]] % | 2026-01-01 to open | US-KSS5-023 (Kansas Department of Labor; A.2, derived arithmetically, confidence medium) | Derivation recorded in register row US-KSS5-023. |
| `ks.sui.employer.rate.max` | [[FACT:ks.sui.employer.rate.max=6.95]] % | 2026-01-01 to 2026-12-31 | US-KSS5-023 (Kansas Department of Labor; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-KSS5-023. |
| `ks.sui.employer.rate.min` | [[FACT:ks.sui.employer.rate.min=0]] % | 2026-01-01 to 2026-12-31 | US-KSS5-023 (Kansas Department of Labor; A.2, derived arithmetically, confidence high) | Schedule C (HB 2570): 0%-[[FACT:ks.sui.employer.rate.max=6.95]]%; not re-traced into 44-710a tables. |
| `ks.sui.government_rated.rate` | [[FACT:ks.sui.government_rated.rate=0.1]] % | 2025-01-01 to 2027-12-31 | US-KSS5-023 (Kansas Department of Labor; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-KSS5-023. |
| `ks.sui.new_employer.construction.rate` | [[FACT:ks.sui.new_employer.construction.rate=5.55]] % | 2026-01-01 to open | US-KSS5-029 (Kansas Office of the Revisor of Statutes; A.1, second independent authority, confidence high) |  |
| `ks.sui.new_employer.rate` | [[FACT:ks.sui.new_employer.rate=1.75]] % | 2026-01-01 to open | US-KSS5-029 (Kansas Office of the Revisor of Statutes; A.1, second independent authority, confidence high) | 44-710a(a)(1) until 24 months chargeability; KDOL table [US-KSS5-023]. |
| `ks.sui.wage_base` | [[FACT:ks.sui.wage_base=15,100]] USD | 2026-01-01 to 2026-12-31 | US-KSS5-023 (Kansas Department of Labor; A.2, derived arithmetically, confidence high) | 44-703(o)(2): 25% of prior-year SAAW rounded to 100 for 2026-27 (30% 2028, 35% 2029, 40% 2030-31) [US-KSS5-020]. Derivation: max WBA 637 = 55% SAWW -> SAAW 60,225-60,320 -> 25% = 15,056-15,080 -> [[FACT:ks.sui.wage_base=15,100]]. No 2027 value is modelled. |
| `ks.sui.wage_base.other_state_credit` | [[FACT:ks.sui.wage_base.other_state_credit=True]] | 2026-01-01 to open | US-KSS5-020 (Kansas Office of the Revisor of Statutes; A.1, derived arithmetically, confidence high) | 44-703(o)(2)(C)(i). Coverage: agricultural 20,000/quarter or 10 in 20 weeks; domestic 1,000/quarter; tips >= 20/month are UI wages. |

Not configured in this release [[GAP:RQ-218]]: 2027 base unpublished; ~15,700 is a projection only.

Not configured in this release [[GAP:RQ-219]]: 44-710a Schedule C table not traced row by row against KDOL 0%-[[FACT:ks.sui.employer.rate.max=6.95]]%.

## KS.4 Pay statement

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ks.payslip.required` | [[FACT:ks.payslip.required=itemized statement of deductions on request for each pay period with deductions (44-320(d)); no routine pay statement; payroll card net shown on earnings statement (44-314(d))]] | 2026-01-01 to open | US-KSS5-013 (Kansas Office of the Revisor of Statutes; A.1, direct artifact inspection, confidence medium) | 44-320(d) on row US-KSP52-001. |

## KS.5 Statutory reporting

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ks.newhire.report_business_days` | [[FACT:ks.newhire.report_business_days=20]] business days | 2026-01-01 to open | US-KSS5-019 (Kansas Office of the Revisor of Statutes; A.1, direct artifact inspection, confidence high) | K.S.A. 75-5743 (statute governs over KDOL "20 days"); rehire after 60+ days. |
| `ks.report.annual.kw3` | [[FACT:ks.report.annual.kw3=KW-3 electronic by January 31 with state W-2s and 1099s with KS withholding; closure within 30 days after month of closure]] | 2024-07-01 to open | US-KSS5-001 (Kansas Department of Revenue; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-KSS5-001. |
| `ks.report.sui.quarterly` | [[FACT:ks.report.sui.quarterly=wage report + contribution return due Apr 30 / Jul 31 / Oct 31 / Jan 31; MMREF / NASWA upload; paper K-CNS-100 for small employers]] | 2026-01-01 to open | US-KSS5-022 (Kansas Department of Labor; A.2, quoted from authority page, confidence high) | E-file threshold 25+ (EDI, from 2024-07-01) vs 26+ (FAQ) conflict open. |
| `ks.report.w2.efile_threshold_forms` | [[FACT:ks.report.w2.efile_threshold_forms=51]] forms | 2025-10-01 to open | US-KSS5-026 (Kansas Department of Revenue; A.2, direct artifact inspection, confidence high) | EFW2 with KS RS (K-2MT Rev. 10-25; RA/RE/RW/RS/RT/RF) or KW-2CSV; box 15 carries the Kansas withholding account number in its published layout (prefix 036, account body, suffix F-01); no CF/SF. TY2026 K-2MT not located. |
| `ks.report.wh.deposit_frequency` | [[FACT:ks.report.wh.deposit_frequency=quad-monthly > 100,000/yr (7th/15th/21st/last, 3 banking days); semi-monthly 8,000-100,000 (25th / 10th); monthly 1,200-8,000 (15th); quarterly 200-1,200 (25th after quarter); annual <= 200 (Jan 25); KW-5 every period even if zero]] | 2026-01-01 to open | US-KSS5-007 (Kansas Office of the Revisor of Statutes; A.1, second independent authority, confidence high) |  |

Not configured in this release [[GAP:RQ-220]]: KDOL FAQ says 26+ employees, the EDI section says 25+ (from 2024-07-01).

Not configured in this release [[GAP:RQ-221]]: TY2026 K-2MT edition (RS layout for files due 2027-01-31) not posted.

## KS.6 Leave

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ks.leave.sick.state_mandate.exists` | [[FACT:ks.leave.sick.state_mandate.exists=False]] | 2026-01-01 to open | US-KSS5-012 (Kansas Office of the Revisor of Statutes; A.1, direct artifact inspection, confidence high) |  |

Not configured in this release [[GAP:RQ-222]]: Jury duty (K.S.A. 43-173) and state military leave not read.

## KS.7 Termination and final pay

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ks.final_pay.rule` | [[FACT:ks.final_pay.rule=next regular payday for discharge and resignation, by mail on request; willful non-payment 1%/day after 8th day, max 100% (44-315)]] | 2026-01-01 to open | US-KSS5-014 (Kansas Office of the Revisor of Statutes; A.1, direct artifact inspection, confidence high) | Vacation payout only by policy/contract (Mid America Aerospace, 1985). |
| `ks.final_wage.deductions` | [[FACT:ks.final_wage.deductions=with written notice for unreturned property, loans, overpayment, merchandise; never below MW (44-319(c),(e))]] | 2026-01-01 to open | US-KSS5-016 (Kansas Office of the Revisor of Statutes; A.1, direct artifact inspection, confidence high) |  |

Not configured in this release [[GAP:RQ-223]]: No Kansas separation notice requirement located.

## KS.8 Benefits in kind and taxable wages

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ks.pit.conformity` | [[FACT:ks.pit.conformity=KS AGI = federal AGI + modifications (79-32,117(a)); federal exclusions flow through; departure: KPERS employer-picked-up contributions are a KS addition (79-32,117(b)(vi))]] | 2026-01-01 to open | US-KSS5-028 (Kansas Office of the Revisor of Statutes; A.1, direct artifact inspection, confidence high) |  |

## KS.9 Deductions and garnishments

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ks.deductions.authorised` | [[FACT:ks.deductions.authorised=required by law; medical without employer benefit; signed authorisation for employee benefit; retirement auto-enrolment; written agreement for loans/overpayment/merchandise; charity and union dues; never below MW (44-319)]] | 2026-01-01 to open | US-KSS5-016 (Kansas Office of the Revisor of Statutes; A.1, direct artifact inspection, confidence high) |  |
| `ks.garn.child_support.cap_percent` | [[FACT:ks.garn.child_support.cap_percent=50]] % | 2026-01-01 to open | US-KSS5-018 (Kansas Office of the Revisor of Statutes; A.1, direct artifact inspection, confidence high) | 23-3104/3105: total cap 50% of disposable incl. fee and medical premiums; start next pay after 14 days; remit within 7 business days; fee lesser of 5/period or 10/month on top; IV-D contact 14 days before lump sum with arrears. |
| `ks.garn.child_support.fee_monthly_max` | [[FACT:ks.garn.child_support.fee_monthly_max=10]] USD | 2026-01-01 to open | US-KSS5-018 (Kansas Office of the Revisor of Statutes; A.1, direct artifact inspection, confidence high) |  |
| `ks.garn.child_support.fee_per_period` | [[FACT:ks.garn.child_support.fee_per_period=5]] USD | 2026-01-01 to open | US-KSS5-018 (Kansas Office of the Revisor of Statutes; A.1, direct artifact inspection, confidence high) |  |
| `ks.garn.creditor.rule` | [[FACT:ks.garn.creditor.rule=lesser of 25% of disposable, excess over 30 x federal MW (217.50/week), or the claim; one garnishment per creditor per 30 days (60-2310)]] | 2026-01-01 to open | US-KSS5-017 (Kansas Office of the Revisor of Statutes; A.1, direct artifact inspection, confidence high) |  |

## KS.10 Collective agreements and prevailing wage

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ks.prevailing_wage.state_law.exists` | [[FACT:ks.prevailing_wage.state_law.exists=False]] | 1987-01-01 to open | US-KSP52-002 (Kansas Office of the Revisor of Statutes; US Department of Labor Wage and Hour Division; A.1, quoted from authority page, confidence high) | Repealed 1987 (K.S.A. 44-201); Davis-Bacon only. |

## KS.11 Indexation

MW, std deduction, exemptions fixed; PIT revenue-contingent cut certified each Aug 15 (not triggered 2026/2027); UI base % of SAAW yearly; WBA 55% SAWW July 1; schedule yearly (KDOL by Dec 1).

## KS.12 Payroll data protection and records

SSN commercial use limited, internal administrative use exempt, penalty up to 1,000 (K.S.A. 75-3520) [US-KSS5-024]; no truncation rule; breach law 50-7a01 not read.

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ks.records.retention_years` | [[FACT:ks.records.retention_years=3]] years | 1978-01-01 to open | US-KSS5-011 (Kansas Office of the Revisor of Statutes; A.1, direct artifact inspection, confidence high) | 44-1209: name, occupation, rate, amount paid, daily/weekly hours; FLSA records acceptable. |

## KS.13 Live legal change

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ks.live.sb471.status` | [[FACT:ks.live.sb471.status=died at end of 2025-2026 biennium (minimum wage 16/h) - do not model]] | 2026-01-01 to open | US-KSS5-027 (Kansas State Legislature; A.1, direct artifact inspection, confidence high) |  |

## KS.14 Authority worked examples (oracle values)

No published state worked example is recorded for this jurisdiction.

## KS.15 Special populations

- Domestic: withholding follows federal (voluntary); UI 1,000 cash/quarter; excluded from state MW [US-KSS5-001, US-KSS5-020, US-KSS5-009].
- Agricultural: withholding follows federal; UI 20,000/quarter or 10 in 20 weeks (non-cash not UI wages); state MW excluded [US-KSS5-001, US-KSS5-020].
- Minors: 18 or under occasional/part-time excluded from state MW; UI excludes newspaper delivery under 18 and child under 21 for parent [US-KSS5-009, US-KSS5-020].
- Tipped: [[FACT:ks.minwage.tipped.cash_wage=2.13]] (non-FLSA employers); tips >= 20/month UI wages [US-KSS5-008, US-KSS5-020].
- Clergy: UI excludes church employment and ministers; withholding follows federal [US-KSS5-020, US-KSS5-001].
- Students: own-school and work-study UI-excluded [US-KSS5-020, US-KSS5-009].
- NRAs / statutory employees: follow federal; PEO = employer [US-KSS5-001].
- Government: withholding required; rated governmental UI [[FACT:ks.sui.government_rated.rate=0.10]]%; KPERS pick-up addition (open) [US-KSS5-001, US-KSS5-023, US-KSS5-028].
- Motion-picture extras under 14 days/yr: exempt from KS withholding [US-KSS5-001].

## KS.16 Language

Bilingual agency documents expressly permitted; official-language designation government-only [US-KSP9L-002]; payslip English (US-OWN-006).

## KS.S Sources

The legal basis of each value (legal-basis register id, authority, source tier and verification method) is given in the row that carries it.
