# Annex MA: Massachusetts


**Layer classification (T3).** T3: separate state withholding calculation and state return; no local layer, or a local layer piggybacked on the state return. Source: build manifest tier census, local income tax domain.

**Summary.** Minimum wage 15.00 (not indexed; service rate [[FACT:ma.minwage.service_rate=6.75]]; agricultural 8.00); weekly overtime. PIT [[FACT:ma.pit.rate=5.0]]% + 4% surtax above [[FACT:ma.pit.surtax.threshold=1,107,750]] (2026); M-4 exemptions; Circular M tables or percentage method (they differ by up to 0.02); supplemental 5% (9% above threshold); no reciprocity (credit method), no local tax. UI base 15,000, new [[FACT:ma.sui.new_employer.rate=2.42]]%, Schedule E [[FACT:ma.sui.employer.rate.min=0.94]]%-[[FACT:ma.sui.employer.rate.max=14.37]]% + COVID Recovery Assessment [[FACT:ma.sui.covid_recovery.rate.min=0.178]]%-[[FACT:ma.sui.covid_recovery.rate.max=2.716]]%; EMAC 0.12/0.24/0.34%; WTF [[FACT:ma.wtf.rate=0.056]]%; PFML [[FACT:ma.pfml.total.rate=0.88]]% (25+) / 0.46% (<25) with the Chapter 101 family/medical swap applied from 2027-01-01 (decision recorded). Pay slip c.149 s.148. Discharge: pay same day.

Each parameter row gives its key, the period in force and its legal basis: the legal-basis register row, the authority, the source tier and how the value was verified.

## MA.1 Employment and labour code

Pay weekly or biweekly within 6 days of period end (7 if 7-day week); casual within 7 days [US-MAP51-008]. Payment method/e-stub consent not established from an official source. No local MW located (commissioner power under c.151 s.7 unused).

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ma.minwage.agricultural` | [[FACT:ma.minwage.agricultural=8]] USD | 2026-01-01 to open | US-MAS5-004 (Massachusetts General Court (malegislature.gov); A.1, direct artifact inspection, confidence high) | Not children 17 or under or immediate family; agriculture exempt from state OT [US-MAS5-002]. |
| `ma.minwage.hourly` | [[FACT:ma.minwage.hourly=15]] USD | 2023-01-01 to open | US-MAS5-001 (Massachusetts General Court (malegislature.gov); A.1, direct artifact inspection, confidence high) | Never less than federal + 0.50; not indexed; no 2027 rate enacted [US-MAS5-017]. |
| `ma.minwage.service_rate` | [[FACT:ma.minwage.service_rate=6.75]] USD | 2023-01-01 to open | US-MAS5-003 (Massachusetts General Court (malegislature.gov); A.1, direct artifact inspection, confidence high) | Tipped cash wage; max tip credit [[FACT:ma.minwage.hourly=15.00]] - [[FACT:ma.minwage.service_rate=6.75]] = [[FACT:ma.minwage.tip_credit.max=8.25]] (derived); top-up per shift. |
| `ma.minwage.tip_credit.max` | [[FACT:ma.minwage.tip_credit.max=8.25]] USD | 2023-01-01 to open | US-MAS5-003 (Massachusetts General Court (malegislature.gov); A.1, derived arithmetically, confidence high) | [[FACT:ma.minwage.hourly=15.00]] - [[FACT:ma.minwage.service_rate=6.75]]. |
| `ma.overtime.weekly_threshold_hours` | [[FACT:ma.overtime.weekly_threshold_hours=40]] hours | 2026-01-01 to open | US-MAS5-002 (Massachusetts General Court (malegislature.gov); A.1, direct artifact inspection, confidence high) | 1.5x; no daily OT; commissions/bonuses/incentives excluded from regular rate. |

Not configured in this release [[GAP:RQ-248]]: Direct deposit, paycard and electronic pay-stub consent rules not established from an official source.

## MA.2 Income tax withholding

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ma.pit.rate` | [[FACT:ma.pit.rate=5.0]] % | 2026-01-01 to open | US-MAB5-402 (Massachusetts Department of Revenue; A.2, quoted from authority page, confidence high) | Plus 4% surtax above [[FACT:ma.pit.surtax.threshold=1,107,750]] (2026); withholding at combined 9% above threshold. IP 25-18 is not modelled. |
| `ma.pit.surtax.rate` | [[FACT:ma.pit.surtax.rate=4.0]] % | 2026-01-01 to open | US-MAP51-003 (Massachusetts Department of Revenue; A.2, quoted from authority page, confidence high) |  |
| `ma.pit.surtax.threshold` | [[FACT:ma.pit.surtax.threshold=1,107,750]] USD | 2026-01-01 to 2026-12-31 | US-MAB5-402 (Massachusetts Department of Revenue; A.2, quoted from authority page, confidence high) | Indexed (CPI mechanism not confirmed); published in Circular M. |
| `ma.wh.blind_reduction.weekly` | [[FACT:ma.wh.blind_reduction.weekly=2.12]] USD | 2026-01-01 to open | US-MAS5-013 (Massachusetts Department of Revenue; A.2, quoted from authority page, confidence high) | Per person; DOR publishes the biweekly, semimonthly, monthly and daily amounts in the same table. |
| `ma.wh.certificate` | [[FACT:ma.wh.certificate=M-4: line 1 personal (1, or 2 if 65+), line 2 spouse (4, or 5 if 65+), line 3 dependents, line 5 additional; boxes A HoH, B blind, C spouse blind, D full-time student <= 8,000 (no withholding); none filed = zero exemptions; new M-4 within 10 days on decrease; exemptions only with principal employer]] | 2026-01-01 to open | US-MAS5-014 (Massachusetts Department of Revenue; A.2, direct artifact inspection, confidence high) | Edition date not printed in extracted text. |
| `ma.wh.exemption.annual` | [[FACT:ma.wh.exemption.annual=1,000n + 3,400]] | 2026-01-01 to open | US-MAS5-013 (Massachusetts Department of Revenue; A.2, quoted from authority page, confidence high) |  |
| `ma.wh.exemption.weekly` | [[FACT:ma.wh.exemption.weekly=19n + 66]] | 2026-01-01 to open | US-MAS5-013 (Massachusetts Department of Revenue; A.2, quoted from authority page, confidence high) | Daily 3n+9; biweekly 38n+131; semimonthly 42n+141; monthly 83n+284; annual 1,000n+3,400 (n = exemptions). |
| `ma.wh.fica_retirement_deduction.annual_max` | [[FACT:ma.wh.fica_retirement_deduction.annual_max=2,000]] USD | 2026-01-01 to open | US-MAS5-013 (Massachusetts Department of Revenue; A.2, quoted from authority page, confidence high) |  |
| `ma.wh.hoh_reduction.weekly` | [[FACT:ma.wh.hoh_reduction.weekly=2.31]] USD | 2026-01-01 to open | US-MAS5-013 (Massachusetts Department of Revenue; A.2, quoted from authority page, confidence high) | DOR publishes the biweekly, semimonthly, monthly and daily amounts in the same table. |
| `ma.wh.method` | [[FACT:ma.wh.method=Circular M wage-bracket tables or percentage method: wages - FICA/Medicare/retirement (max 2,000/yr) - exemption amount for period; x 5%; - HoH / blind reduction]] | 2026-01-01 to open | US-MAS5-013 (Massachusetts Department of Revenue; A.2, quoted from authority page, confidence high) | Methods not numerically identical (table vs percentage differ up to 0.02 weekly); the payroll calculation must use one method consistently [US-MAS5-024]. |
| `ma.wh.rounding` | [[FACT:ma.wh.rounding=wages may be computed to nearest dollar (830 CMR 62B.2.1(8))]] | 2026-06-05 to open | US-MAS5-023 (Massachusetts Department of Revenue (Massachusetts Register); A.1, direct artifact inspection, confidence high) |  |
| `ma.wh.student_box_d.income_max` | [[FACT:ma.wh.student_box_d.income_max=8,000]] USD | 2026-01-01 to open | US-MAS5-014 (Massachusetts Department of Revenue; A.2, direct artifact inspection, confidence high) |  |
| `ma.wh.supplemental.rate` | [[FACT:ma.wh.supplemental.rate=5]] % | 2026-01-01 to open | US-MAP51-003 (Massachusetts Department of Revenue; A.2, quoted from authority page, confidence medium) | Circular M 2026, section G: 5% while cumulative supplemental wages are $[[FACT:ma.pit.surtax.threshold=1,107,750]] or less; above, lesser of 9% of payment or 9% of excess + 5% of remainder. "5. If the result of step 4 is $[[FACT:ma.pit.surtax.threshold=1,107,750]] or less, withhold 5% of the amount determined in step 3." |
| `ma.wh.supplemental.rule` | [[FACT:ma.wh.supplemental.rule=5% while annualized regular + supplemental to date + this payment <= 1,107,750; above, lesser of 9% of payment or 9% of excess plus 5% of remainder; percentage method excludes supplemental]] | 2026-01-01 to open | US-MAP51-003 (Massachusetts Department of Revenue; A.2, quoted from authority page, confidence high) | Circular M 2026. |

Not configured in this release [[GAP:RQ-249]]: M-4 revision date not printed in extracted text.

Not configured in this release [[GAP:RQ-250]]: 401(k)/403(b), s.125, HSA, transit, GTL treatment not verified against the official source in a DOR source.

Not configured in this release [[GAP:RQ-251]]: Subject of the P.L. 119-21 s.70302(f) deduction and any withholding effect unchecked.

Not configured in this release [[GAP:RQ-588]]: The rate and ballot status of initiative petition IP 25-18 are not established from an official source.

## MA.2b Non-resident regime and reciprocity

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ma.nonres.rules` | [[FACT:ma.nonres.rules=residents on all wages; nonresidents on MA-performed services; nonresident not working in MA not withheld even if paid from MA office; courtesy withholding for residents by out-of-state employers; no reciprocity - credit method: MA amount minus other jurisdiction amount (830 CMR 62B.2.1(9)(b))]] | 2026-01-01 to open | US-MAS5-013 (Massachusetts Department of Revenue; A.2, quoted from authority page, confidence high) | No MA withholding where no federal duty (household); MSRRA M-4-MS: do not withhold [US-MAS5-024]. |

## MA.2c Local wage taxes

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ma.local_wage_tax.exists` | [[FACT:ma.local_wage_tax.exists=False]] | 2026-01-01 to open | US-MAB5-402 (Massachusetts Department of Revenue; A.2, quoted from authority page, confidence high) | No local wage/payroll/income tax [US-MAR3-001, US-MAR3-003]. |

## MA.3 Social insurance: unemployment, disability, paid leave and payroll levies

Configuration rule: 2026 payroll applies the DFML 2026 contribution table; the Chapter 101 family/medical swap applies from 2027-01-01 (`ma.pfml.split.decision`). The employee and employer totals are the same before and after the swap.
No SDI/TDI; PFML the only employee-funded program [US-MAP9W-004]. PFML benefits paid by DFML (optional 5%/10% withholding), not payroll.

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ma.emac.rate.year4` | [[FACT:ma.emac.rate.year4=0.12]] % | 2026-01-01 to open | US-MAS5-021 (Massachusetts Department of Unemployment Assistance; A.2, quoted from authority page, confidence high) | EMAC on [[FACT:ma.sui.wage_base=15,000]] base: years 1-3 exempt; year 4 [[FACT:ma.emac.rate.year4=0.12]]%; year 5 [[FACT:ma.emac.rate.year5=0.24]]%; year 6+ [[FACT:ma.emac.rate.year6_plus=0.34]]%; fewer than 6 employees in a quarter exempt. |
| `ma.emac.rate.year5` | [[FACT:ma.emac.rate.year5=0.24]] % | 2026-01-01 to open | US-MAS5-021 (Massachusetts Department of Unemployment Assistance; A.2, quoted from authority page, confidence high) |  |
| `ma.emac.rate.year6_plus` | [[FACT:ma.emac.rate.year6_plus=0.34]] % | 2026-01-01 to open | US-MAS5-021 (Massachusetts Department of Unemployment Assistance; A.2, quoted from authority page, confidence high) |  |
| `ma.pfml.benefit.weekly_max` | [[FACT:ma.pfml.benefit.weekly_max=1,230.39]] USD | 2026-01-01 to 2026-12-31 | US-MAS5-025 (Massachusetts Department of Family and Medical Leave; A.2, derived arithmetically, confidence high) | 64% x SAWW 1,922.48; benefit side, paid by DFML (not payroll). |
| `ma.pfml.benefit.weekly_max` | [[FACT:ma.pfml.benefit.weekly_max=1,284.61]] USD | 2027-01-01 to open | US-MAS5-025 (Massachusetts Department of Family and Medical Leave; A.2, derived arithmetically, confidence high) | 64% x 2,007.20. |
| `ma.pfml.employee.max_total.25_plus` | [[FACT:ma.pfml.employee.max_total.25_plus=0.46]] % | 2026-01-01 to open | US-MAS5-012 (Massachusetts Department of Family and Medical Leave; A.2, derived arithmetically, confidence high) | 2026: 0.18 + 0.28; 2027: 0.28 + 0.18 - the employee and employer totals (0.46 / 0.42) are identical either side of the swap; only the family/medical labelling (benefit tax treatment) changes. |
| `ma.pfml.family.rate` | [[FACT:ma.pfml.family.rate=0.18]] % | 2026-01-01 to 2026-12-31 | US-MAS5-012 (Massachusetts Department of Family and Medical Leave; A.2, quoted from authority page, confidence high) | Up to 100% from employee. |
| `ma.pfml.family.rate` | [[FACT:ma.pfml.family.rate=0.7]] % | 2027-01-01 to open | US-MAS5-012 (Massachusetts Department of Family and Medical Leave; A.2, derived arithmetically, confidence high) | Chapter 101 swap: employee up to 40% (0.28%), employer 0.42%. |
| `ma.pfml.medical.rate` | [[FACT:ma.pfml.medical.rate=0.7]] % | 2026-01-01 to 2026-12-31 | US-MAS5-012 (Massachusetts Department of Family and Medical Leave; A.2, derived arithmetically, confidence high) | Employee up to 40% (0.28%), employer 0.42% (25+). |
| `ma.pfml.medical.rate` | [[FACT:ma.pfml.medical.rate=0.18]] % | 2027-01-01 to open | US-MAS5-012 (Massachusetts Department of Family and Medical Leave; A.2, quoted from authority page, confidence high) | Up to 100% from employee. |
| `ma.pfml.rate.total.under_25` | [[FACT:ma.pfml.rate.total.under_25=0.46]] % | 2026-01-01 to open | US-MAS5-012 (Massachusetts Department of Family and Medical Leave; A.2, quoted from authority page, confidence high) | No employer share. |
| `ma.pfml.split.decision` | [[FACT:ma.pfml.split.decision=Chapter 101 ss.25-26 family/medical deduction-cap swap applied from 2027-01-01 per DFML; 2026 payroll uses the DFML 2026 table]] | 2026-01-01 to open | US-MAS5-012 (Massachusetts Department of Family and Medical Leave; A.2, quoted from authority page, confidence medium) | Decision: s.45 of Ch. 101 [US-MAS5-026] says ss.25-26 apply "for taxable years beginning on or after January 1, 2026"; DFML, the administering authority, implements from 2027-01-01 [US-MAS5-012]. Decided for DFML: (1) "taxable years" is income-tax language and the swap was made to address the IRS tax treatment of benefits, an assessment-level matter; (2) the contribution totals withheld ([[FACT:ma.pfml.rate.total.under_25=0.46]]% employee / 0.42% employer) are identical under both readings, so no 2026 payroll amount changes; (3) DFML has issued no 2026 re-split or catch-up instruction. Re-open only if DFML/DOR (458 CMR 2.00) issues a transition notice. |
| `ma.pfml.total.rate` | [[FACT:ma.pfml.total.rate=0.88]] % | 2026-01-01 to open | US-MAS5-012 (Massachusetts Department of Family and Medical Leave; A.2, quoted from authority page, confidence high) | Unchanged total in 2027. Cap: SS wage base (c.175M s.6(f)) [US-MAS5-010]. |
| `ma.sui.coverage` | [[FACT:ma.sui.coverage=1 employee 13 weeks or 1,500/quarter; agricultural 40,000/quarter or 10 for 20 weeks; domestic 1,000 cash/quarter; out-of-state employers 200 MA wages/quarter; notices by Jan 31; review requests before Jun 20; 12% late interest]] | 2026-01-01 to open | US-MAS5-022 (Massachusetts Department of Unemployment Assistance; A.2, quoted from authority page, confidence high) |  |
| `ma.sui.covid_recovery.rate.max` | [[FACT:ma.sui.covid_recovery.rate.max=2.716]] % | 2026-01-01 to 2026-12-31 | US-MAS5-020 (Massachusetts Department of Unemployment Assistance; A.2, direct artifact inspection, confidence high) |  |
| `ma.sui.covid_recovery.rate.min` | [[FACT:ma.sui.covid_recovery.rate.min=0.178]] % | 2026-01-01 to 2026-12-31 | US-MAS5-020 (Massachusetts Department of Unemployment Assistance; A.2, direct artifact inspection, confidence high) |  |
| `ma.sui.employer.rate.max` | [[FACT:ma.sui.employer.rate.max=14.37]] % | 2026-01-01 to 2026-12-31 | US-MAS5-020 (Massachusetts Department of Unemployment Assistance; A.2, direct artifact inspection, confidence high) |  |
| `ma.sui.employer.rate.min` | [[FACT:ma.sui.employer.rate.min=0.94]] % | 2026-01-01 to 2026-12-31 | US-MAS5-020 (Massachusetts Department of Unemployment Assistance; A.2, direct artifact inspection, confidence high) | Schedule E; COVID Recovery Assessment [[FACT:ma.sui.covid_recovery.rate.min=0.178]]%-[[FACT:ma.sui.covid_recovery.rate.max=2.716]]% on same base; effective 1.118%-17.086% (UI + COVID = effective in every band). |
| `ma.sui.new_employer.construction.rate` | [[FACT:ma.sui.new_employer.construction.rate=6.08]] % | 2026-01-01 to 2026-12-31 | US-MAS5-022 (Massachusetts Department of Unemployment Assistance; A.2, quoted from authority page, confidence high) |  |
| `ma.sui.new_employer.rate` | [[FACT:ma.sui.new_employer.rate=2.42]] % | 2026-01-01 to 2026-12-31 | US-MAS5-022 (Massachusetts Department of Unemployment Assistance; A.2, quoted from authority page, confidence high) | Under 3 years; construction [[FACT:ma.sui.new_employer.construction.rate=6.08]]%; base [[FACT:ma.sui.wage_base=15,000]] fixed (c.151A s.14, US-MAP51-005); no employee UI. |
| `ma.sui.rate_schedule.in_force` | [[FACT:ma.sui.rate_schedule.in_force=E]] | 2026-01-01 to 2026-12-31 | US-MAB5-001 (Massachusetts Department of Unemployment Assistance; A.2, derived arithmetically, confidence high) | Derivation: the 2026 published minimum [[FACT:ma.sui.employer.rate.min=0.94]]% and maximum [[FACT:ma.sui.employer.rate.max=14.37]]% (ma.sui.employer.rate.min/max, US-MAS5-020) coincide only with column E of the schedule table (min row: A 0.56, B 0.64, C 0.73, D 0.83, E 0.94, F 1.07, G 1.21; max row: 8.62, 9.79, 11.13, 12.65, [[FACT:ma.sui.employer.rate.max=14.37]], 16.33, 18.55). |
| `ma.sui.rate_schedule.selection` | [[FACT:ma.sui.rate_schedule.selection=Schedule A-G by Unemployment Compensation Fund reserve %: A >= 1.65; B 1.5-<1.65; C 1.2-<1.5; D 0.9-<1.2; E 0.6-<0.9; F 0.3-<0.6; G < 0.3]] | 2015-01-01 to open | US-MAB5-001 (Massachusetts Department of Unemployment Assistance; A.2, direct artifact inspection, confidence high) |  |
| `ma.sui.rate_schedule.table` | [[FACT:ma.sui.rate_schedule.table=45 account-reserve rows x 7 schedules (positive reserve 17.0+ : A 0.56 / B 0.64 / C 0.73 / D 0.83 / E 0.94 / F 1.07 / G 1.21 ... negative reserve 23+ : 8.62 / 9.79 / 11.13 / 12.65 / 14.37 / 16.33 / 18.55)]] | 2015-01-01 to open | US-MAB5-001 (Massachusetts Department of Unemployment Assistance; A.2, direct artifact inspection, confidence high) | The full 45 x 7 rate schedule is in the source document at the cited URL. |
| `ma.sui.wage_base` | [[FACT:ma.sui.wage_base=15,000]] USD | 2015-01-01 to 2026-12-31 | US-MAP51-005 (Massachusetts Legislature; A.1, direct artifact inspection, confidence high) | Fixed by statute, not indexed. |
| `ma.wtf.rate` | [[FACT:ma.wtf.rate=0.056]] % | 2026-01-01 to open | US-MAB5-401 (MA official authority; A.2, quoted from authority page, confidence medium) | c.151A s.14L; 2026 DUA value not confirmed (commissioner may adjust). |

Not configured in this release [[GAP:RQ-252]]: 2026 Workforce Training Fund rate as published by DUA not verified against the official source.

Not configured in this release [[GAP:RQ-253]]: Ch. 101 s.45 vs DFML effective date (decided for DFML 2027-01-01; totals unaffected).

## MA.4 Pay statement

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ma.payslip.items` | [[FACT:ma.payslip.items=employer name, employee name, date (day/month/year), hours worked, hourly rate, deductions or increases for the period (c.149 s.148)]] | 2026-01-01 to open | US-MAS5-005 (Massachusetts General Court (malegislature.gov); A.1, direct artifact inspection, confidence medium) | Statute row US-MAP51-008; electronic-delivery consent is not stated in this source. |

## MA.5 Statutory reporting

Registration MassTaxConnect (DOR, PFML) and DUA portal. PFML quarterly return mechanics unread.

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ma.newhire.report_days` | [[FACT:ma.newhire.report_days=14]] days | 2026-01-01 to open | US-MAS5-016 (Massachusetts Department of Revenue (Child Support Services); A.2, quoted from authority page, confidence high) | Employees and contractors 600+; rehires after 30+ days; SSN only (no ITIN); 25+ employees online. |
| `ma.report.sui.quarterly` | [[FACT:ma.report.sui.quarterly=DUA wage detail by 3 p.m. Apr 30 / Jul 31 / Oct 31 / Jan 31; CSV, EFW2 or ICESA; EAN, SSN, name, hours, gross, wages subject to withholding, state tax withheld, work location, 12th-of-month, adjustment reason; wages when paid]] | 2026-01-01 to open | US-MAS5-018 (Massachusetts Department of Unemployment Assistance (EOLWD); A.2, quoted from authority page, confidence high) |  |
| `ma.report.w2` | [[FACT:ma.report.w2=due Jan 31; 50+ W-2s electronic via MassTaxConnect/Bulk File Portal; <= 49 paper with M-3; corrections paper W-2c; EFW2 RA/RE/RS/RT, RS MA wages 276-286, MA tax 287-297, RT = sum RS]] | 2026-01-30 to open | US-MAS5-015 (Massachusetts Department of Revenue; A.2, quoted from authority page, confidence high) | Format [US-MAS5-019] handbook Rev. 20191219. Guide (Aug 2026) says last day of March / Feb 28 - conflict; use Jan 31. |
| `ma.report.w2.efile_threshold` | [[FACT:ma.report.w2.efile_threshold=50]] forms | 2026-01-30 to open | US-MAS5-015 (Massachusetts Department of Revenue; A.2, quoted from authority page, confidence high) |  |
| `ma.report.wh.frequency` | [[FACT:ma.report.wh.frequency=<= 100/yr annual (Jan 31); 101-1,200 quarterly; 1,201-25,000 monthly by 15th (quarter-end months on last day of following month); > 25,000 quarterly return + payment within 3 business days when >= 500 accumulated by 7th/15th/22nd/last; e-file mandatory for new registrations, payroll providers, combined liability >= 5,000]] | 2026-01-01 to open | US-MAS5-013 (Massachusetts Department of Revenue; A.2, quoted from authority page, confidence high) |  |

Not configured in this release [[GAP:RQ-254]]: W-2 e-file handbook served is Rev. 20191219 though reissued yearly.

Not configured in this release [[GAP:RQ-255]]: The Feb 28 (paper) / Mar 31 (electronic) dates come from DOR Directive 07-2 (2007, US-MAB5-302), which the Aug 2026 Withholding Tax Guide still echoes. The newer DOR W-2 page (updated 2026-01-30, US-MAS5-015) says January 31, and 830 CMR 62B.2.1(d) fixes January 31 for the employee statement (US-MAB5-301). No TIR or Directive formally replacing 07-2 was found. Filing by January 31 meets every candidate deadline, so the build can configure January 31 without risk.

Not configured in this release [[GAP:RQ-256]]: Whether the DUA wage detail report is the only quarterly wage report (DOR guide mentions DOR reports).

Not configured in this release [[GAP:RQ-257]]: PFML quarterly return mechanics not verified against the official source.

## MA.6 Leave

PFML benefit: 7-day wait; 80% of AWW to 50% SAWW + 50% above; caps 20/12/26 weeks. Parental, small necessities, DV, jury leave not verified against the official source.

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ma.leave.sick.cap_hours` | [[FACT:ma.leave.sick.cap_hours=40]] hours | 2026-01-01 to open | US-MAS5-006 (Massachusetts General Court (malegislature.gov); A.1, direct artifact inspection, confidence high) |  |
| `ma.leave.sick.employer_threshold_paid` | [[FACT:ma.leave.sick.employer_threshold_paid=11]] employees | 2026-01-01 to open | US-MAS5-006 (Massachusetts General Court (malegislature.gov); A.1, direct artifact inspection, confidence high) | c.149 s.148C: 1 h per 30 h; use from day 90; 40 h/yr paid (11+) or unpaid; carryover 40; no payout; certification after 24 consecutive scheduled hours. |
| `ma.leave.sick.payout_on_separation` | [[FACT:ma.leave.sick.payout_on_separation=False]] | 2026-01-01 to open | US-MAS5-006 (Massachusetts General Court (malegislature.gov); A.1, direct artifact inspection, confidence high) |  |

Not configured in this release [[GAP:RQ-258]]: C.149 ss.52D, 52E, 105D, jury c.234A s.48 and child labour ss.60-66 not verified against the official source.

## MA.7 Termination and final pay

Sick time no payout. UI separation notice instrument not established from an official source.

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ma.final_pay.rule` | [[FACT:ma.final_pay.rule=discharge: in full on the day of discharge; resignation: next regular payday (or following Saturday); agreed vacation/holiday pay are wages payable at termination (c.149 s.148)]] | 2026-01-01 to open | US-MAP51-008 (Massachusetts Legislature; A.1, quoted from authority page, confidence high) |  |

Not configured in this release [[GAP:RQ-259]]: DUA separation notice form/rule not established from an official source (430 CMR 5.00 index only).

## MA.8 Benefits in kind and taxable wages

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ma.pit.irc_decoupling` | [[FACT:ma.pit.irc_decoupling=c.62C s.90 (Ch. 101 s.13, from TY2026): same-year IRC amendments do not affect MA gross income; accountable-plan reimbursements not wages]] | 2026-01-01 to open | US-MAS5-026 (Massachusetts General Court (malegislature.gov); A.1, direct artifact inspection, confidence high) | Level assessment flowing into withholding definition. |

## MA.9 Deductions and garnishments

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ma.garn.creditor.exempt_rule` | [[FACT:ma.garn.creditor.exempt_rule=greater of 85% of gross wages or 50 x higher of federal/MA MW per week; support orders: CCPA (c.246 s.28)]] | 2026-01-01 to open | US-MAS5-009 (Massachusetts General Court (malegislature.gov); A.1, direct artifact inspection, confidence high) |  |
| `ma.garn.creditor.weekly_exempt_floor` | [[FACT:ma.garn.creditor.weekly_exempt_floor=750]] USD | 2023-01-01 to open | US-MAS5-009 (Massachusetts General Court (malegislature.gov); A.1, derived arithmetically, confidence high) | 50 x 15.00. |

Not configured in this release [[GAP:RQ-260]]: C.149 s.150 deduction authorisation and MA IWO fees/priority not verified against the official source.

## MA.10 Collective agreements and prevailing wage

Prevailing wage (public works) is an optional informational flag [US-OWN-009]: this guide documents prevailing-wage laws, thresholds and certified-payroll duties as an overlay, and the payroll build does not produce certified payroll reports.

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ma.prevailing_wage.certified_payroll` | [[FACT:ma.prevailing_wage.certified_payroll=weekly certified payroll with signed statement to awarding authority; apprentice ID copies; records 3 years after contract; compliance statement within 15 days of completion; no dollar threshold (s.27B)]] | 2026-01-01 to open | US-MAS5-007 (Massachusetts General Court (malegislature.gov); A.1, direct artifact inspection, confidence high) |  |
| `ma.prevailing_wage.rule` | [[FACT:ma.prevailing_wage.rule=wages at least the commissioner rate on public works (c.149 s.26)]] | 2026-01-01 to open | US-MAP51-009 (Massachusetts Legislature; A.1, quoted from authority page, confidence high) |  |

## MA.11 Indexation

MW and UI base not indexed; UI/COVID and PFML rates yearly; PFML cap = SS base; PFML max benefit 64% SAWW; surtax threshold indexed; M-4 factors static.

## MA.12 Payroll data protection and records

No SSN-on-slip rule located; c.93H / 201 CMR 17.00 not verified against the official source.

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ma.records.retention_years` | [[FACT:ma.records.retention_years=3]] years | 2026-01-01 to open | US-MAS5-005 (Massachusetts General Court (malegislature.gov); A.1, direct artifact inspection, confidence high) | c.151 s.15; employees may inspect; DOR withholding records 3 years. |

## MA.13 Live legal change

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ma.live.chapter_101_2026` | [[FACT:ma.live.chapter_101_2026=enacted (emergency, approved 2026-06-12): PFML split swap (applied 2027-01-01, see decision), IRC same-year decoupling, P.L. 119-21 s.70302(f) deduction (subject unchecked)]] | 2026-06-12 to open | US-MAS5-026 (Massachusetts General Court (malegislature.gov); A.1, direct artifact inspection, confidence high) |  |
| `ma.pfml.rate.selection_basis` | [[FACT:ma.pfml.rate.selection_basis=The new contribution rate applies to wages earned on or after January 1 of each year; rates are set annually for January 1-December 31]] | 2026-01-01 to open | US-MAS5-012 (Massachusetts Department of Family and Medical Leave; A.2, quoted from authority page, confidence high) | Select the rate (and the 2027 family/medical split) by the date wages are earned, not paid. Level: withholding/employer contribution. |
| `ma.report.w2.employee_statement.due` | [[FACT:ma.report.w2.employee_statement.due=Furnish the wage statement to each employee on or before January 31 of the following year, or within 30 days of the last payment if employment ends earlier.]] | 2026-01-01 to open | US-MAB5-301 (Massachusetts Department of Revenue; A.1, quoted from authority page, confidence high) | 830 CMR 62B.2.1(d) (mass.gov, verbatim excerpt). The regulation sets no deadline for filing W-2 copies with DOR. |

Not configured in this release [[GAP:RQ-261]]: 2026 DOR TIRs/Directives and DUA/DFML news not reviewed.

Not configured in this release [[GAP:RQ-262]]: IP 25-18 exclusion rests on a secondary source (US-MAS5-027); the SJC opinion is not verified against the official source.

## MA.14 Authority worked examples (oracle values)

No published state worked example is recorded for this jurisdiction.

## MA.15 Special populations

- Domestic: MW/OT apply (incl. au pairs); written agreement for 16+ h/week; meal and lodging deductions may not exceed the amounts set by 454 CMR 27 (apply the regulation's amounts); UI coverage per the domestic-service test of the coverage row in MA.3; paystub records 3 years [US-MAS5-028, US-MAS5-022].
- Agricultural: MW 8.00 (not family/under 18); OT-exempt; UI coverage per the agricultural test of the coverage row in MA.3 [US-MAS5-004, US-MAS5-002, US-MAS5-022].
- Minors: MW applies; UI-exempt working for a parent; permits/hours not verified against the official source [US-MAS5-001, US-MAS5-022].
- Tipped: service rate [[FACT:ma.minwage.service_rate=6.75]]; tips 20+/month reported by 10th are withheld on [US-MAS5-003, US-MAS5-013].
- Clergy: religious order members excluded from MW; some religious work UI-exempt; religious organisations still withhold [US-MAS5-017, US-MAS5-022, US-MAS5-013].
- Students: M-4 box D (<= 8,000) no withholding; nonprofit/public work-training UI-exempt [US-MAS5-014, US-MAS5-024, US-MAS5-022].
- NRAs: follow federal duty [US-MAS5-013]. MSRRA: M-4-MS no withholding [US-MAS5-024]. Statutory employees: no state rule.
- Government: must withhold and report new hires; municipal employees excluded from c.151 MW; earned sick time only on local acceptance [US-MAS5-013].
- Interstate carriers: residents and nonresidents with all duties in MA [US-MAS5-013]. Family employment UI-exempt [US-MAS5-022].

## MA.16 Language

Earned sick time notice languages c.149 s.148C(o) [US-MAL-002]; payslip English (US-OWN-006).

## MA.S Sources

The legal basis of each value (legal-basis register id, authority, source tier and verification method) is given in the row that carries it.
