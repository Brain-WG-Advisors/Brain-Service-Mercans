# Annex HI: Hawaii


**Layer classification (T3).** T3: separate state withholding calculation and state return; no local layer, or a local layer piggybacked on the state return. Source: build manifest tier census, local income tax domain.

**Summary.** Minimum wage 16.00 (2026-2027), 18.00 from 2028; tip credit [[FACT:hi.minwage.tip_credit=1.25]]. Withholding per Booklet A (Rev. 2025): allowance [[FACT:hi.wh.allowance.annual=1,144]] + lump-sum [[FACT:hi.wh.lump_sum_allowance.annual=4,350]], brackets 1.40%-7.90%, HW-4 (no exempt status), no flat supplemental, no reciprocity, no local tax; 2027 tables will change under Act 24 SLH 2026 - unpublished. UI employer-only, base [[FACT:hi.sui.wage_base=64,500]] (AAW-indexed), new [[FACT:hi.sui.new_employer.rate=2.40]]%, E&T 0.01%; TDI employee max [[FACT:hi.tdi.employee.max_rate=0.5]]% capped 7.50/week; Prepaid Health Care threshold [[FACT:hi.phc.min_monthly_wage=1,387]]/month. 14-item pay statement (HRS 387-6(c)). Oracle: Booklet A Part 1 example [[FACT:hi.oracle.weekly_500_s3.withholding=9.58]].

Each parameter row gives its key, the period in force and its legal basis: the legal-basis register row, the authority, the source tier and how the value was verified.

## HI.1 Employment and labour code

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `hi.minwage.exempt.guaranteed_monthly` | [[FACT:hi.minwage.exempt.guaranteed_monthly=4,000]] USD | 2024-07-01 to open | US-HIS5-003 (Hawaii State Legislature; A.1, direct artifact inspection, confidence high) | HRS 387-1 carve-out (L 2024 c 73); also agriculture < 20 employees, coffee harvesting, casual domestic/companionship. |
| `hi.minwage.hourly` | [[FACT:hi.minwage.hourly=16]] USD | 2026-01-01 to 2027-12-31 | US-HIS5-001 (Hawaii State Legislature; A.1, second independent authority, confidence high) | HRS 387-2 and DLIR agree [US-HIS5-002]; no 2027 step; no indexation; no county rates. |
| `hi.minwage.hourly` | [[FACT:hi.minwage.hourly=18]] USD | 2028-01-01 to open | US-HIS5-001 (Hawaii State Legislature; A.1, second independent authority, confidence high) | Enacted (L 2022 c 114). |
| `hi.minwage.tip_credit` | [[FACT:hi.minwage.tip_credit=1.25]] USD | 2024-01-01 to 2027-12-31 | US-HIS5-001 (Hawaii State Legislature; A.1, second independent authority, confidence high) | Only if wage + tips >= MW + [[FACT:hi.minwage.tip_credit.min_total_over_minwage=7.00]]; tipped = > 20/month tips [US-HIS5-003]; cash wage 14.75. [[FACT:hi.minwage.tip_credit=1.50]] from 2028. |
| `hi.minwage.tip_credit` | [[FACT:hi.minwage.tip_credit=1.50]] USD | 2028-01-01 to open | US-HIS5-001 (Hawaii State Legislature; A.1, second independent authority, confidence high) |  |
| `hi.minwage.tip_credit.min_total_over_minwage` | [[FACT:hi.minwage.tip_credit.min_total_over_minwage=7]] USD | 2024-01-01 to open | US-HIS5-001 (Hawaii State Legislature; A.1, second independent authority, confidence high) |  |
| `hi.overtime.weekly_threshold_hours` | [[FACT:hi.overtime.weekly_threshold_hours=40]] hours | 2026-01-01 to open | US-HIS5-002 (Hawaii DLIR Wage Standards Division; A.2, direct artifact inspection, confidence high) | 1.5x; regular-rate divisors weekly /40, biweekly /2/40, semimonthly x24/52/40, monthly x12/52/40; seasonal ag 20 weeks OT after 48; public works OT after 8/day and weekends/holidays. |
| `hi.pay_frequency.rule` | [[FACT:hi.pay_frequency.rule=at least twice each calendar month on designated paydays; monthly only by secret-ballot majority (2 years) or director permission; due within 7 days after period end (15 with permission)]] | 2026-01-01 to open | US-HIS5-007 (Hawaii State Legislature; A.1, direct artifact inspection, confidence high) |  |
| `hi.paycard.rules` | [[FACT:hi.paycard.rules=employee chooses DD/check/card, never condition of hire; 10-pt disclosure; free 3 withdrawals per period, 24/7 balance, 60-day history, 1 replacement/yr; no overdraft/balance fees; switch within two pay periods (HRS 388-5.7)]] | 2026-01-01 to open | US-HIS5-017 (Hawaii State Legislature; A.1, direct artifact inspection, confidence high) |  |

## HI.2 Income tax withholding

Configuration rule: Hawaii conforms to the federal tips deduction at assessment only and does not conform to the overtime deduction (`hi.pit.ot_deduction.conformed`). Neither changes withholding.
Withholding stops at [[FACT:hi.wh.bracket.single.8.rate=7.90]]%; the assessment schedule (HRS 235-51) continues to higher rates above 175,000 single [US-HIS5-027, partial]. Withholding required on agricultural and domestic wages even where federal is not. Exclusions: MSRRA spouses; ministers; tips < 20/month; casual domestic; newspaper carriers < 18; interstate crew; convenience meals/lodging.

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `hi.pit.ot_deduction.conformed` | [[FACT:hi.pit.ot_deduction.conformed=False]] | 2026-01-01 to open | US-HIS5-029 (Hawaii Department of Taxation; A.2, quoted from authority page, confidence high) | Act 35 SLH 2026 (in force 2026-05-26, TY2026): IRC conformity 2025-12-31; IRC 224 tips deduction conformed (assessment); IRC s.225 overtime NOT conformed; 132(f) bicycle suspended; IRC 128 Trump Account exclusion conformed. |
| `hi.wh.allowance.annual` | [[FACT:hi.wh.allowance.annual=1,144]] USD | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Weekly 22.00. |
| `hi.wh.bracket.married.1.ceiling` | [[FACT:hi.wh.bracket.married.1.ceiling=19,200]] USD | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-HIS5-004. |
| `hi.wh.bracket.married.1.rate` | [[FACT:hi.wh.bracket.married.1.rate=1.4]] % | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-HIS5-004. |
| `hi.wh.bracket.married.2.base_tax` | [[FACT:hi.wh.bracket.married.2.base_tax=269]] USD | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Cumulative bracket sum rounded to whole dollars. |
| `hi.wh.bracket.married.2.ceiling` | [[FACT:hi.wh.bracket.married.2.ceiling=28,800]] USD | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-HIS5-004. |
| `hi.wh.bracket.married.2.rate` | [[FACT:hi.wh.bracket.married.2.rate=3.2]] % | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-HIS5-004. |
| `hi.wh.bracket.married.3.base_tax` | [[FACT:hi.wh.bracket.married.3.base_tax=576]] USD | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Cumulative bracket sum rounded to whole dollars. |
| `hi.wh.bracket.married.3.ceiling` | [[FACT:hi.wh.bracket.married.3.ceiling=38,400]] USD | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-HIS5-004. |
| `hi.wh.bracket.married.3.rate` | [[FACT:hi.wh.bracket.married.3.rate=5.5]] % | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-HIS5-004. |
| `hi.wh.bracket.married.4.base_tax` | [[FACT:hi.wh.bracket.married.4.base_tax=1,104]] USD | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Cumulative bracket sum rounded to whole dollars. |
| `hi.wh.bracket.married.4.ceiling` | [[FACT:hi.wh.bracket.married.4.ceiling=48,000]] USD | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-HIS5-004. |
| `hi.wh.bracket.married.4.rate` | [[FACT:hi.wh.bracket.married.4.rate=6.4]] % | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-HIS5-004. |
| `hi.wh.bracket.married.5.base_tax` | [[FACT:hi.wh.bracket.married.5.base_tax=1,718]] USD | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Cumulative bracket sum rounded to whole dollars. |
| `hi.wh.bracket.married.5.ceiling` | [[FACT:hi.wh.bracket.married.5.ceiling=72,000]] USD | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-HIS5-004. |
| `hi.wh.bracket.married.5.rate` | [[FACT:hi.wh.bracket.married.5.rate=6.8]] % | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-HIS5-004. |
| `hi.wh.bracket.married.6.base_tax` | [[FACT:hi.wh.bracket.married.6.base_tax=3,350]] USD | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Cumulative bracket sum rounded to whole dollars. |
| `hi.wh.bracket.married.6.ceiling` | [[FACT:hi.wh.bracket.married.6.ceiling=96,000]] USD | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-HIS5-004. |
| `hi.wh.bracket.married.6.rate` | [[FACT:hi.wh.bracket.married.6.rate=7.2]] % | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-HIS5-004. |
| `hi.wh.bracket.married.7.base_tax` | [[FACT:hi.wh.bracket.married.7.base_tax=5,078]] USD | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Cumulative bracket sum rounded to whole dollars. |
| `hi.wh.bracket.married.7.ceiling` | [[FACT:hi.wh.bracket.married.7.ceiling=250,000]] USD | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-HIS5-004. |
| `hi.wh.bracket.married.7.rate` | [[FACT:hi.wh.bracket.married.7.rate=7.6]] % | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-HIS5-004. |
| `hi.wh.bracket.married.8.base_tax` | [[FACT:hi.wh.bracket.married.8.base_tax=16,782]] USD | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Cumulative bracket sum rounded to whole dollars. |
| `hi.wh.bracket.married.8.rate` | [[FACT:hi.wh.bracket.married.8.rate=7.9]] % | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-HIS5-004. |
| `hi.wh.bracket.single.1.ceiling` | [[FACT:hi.wh.bracket.single.1.ceiling=9,600]] USD | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-HIS5-004. |
| `hi.wh.bracket.single.1.rate` | [[FACT:hi.wh.bracket.single.1.rate=1.4]] % | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-HIS5-004. |
| `hi.wh.bracket.single.2.base_tax` | [[FACT:hi.wh.bracket.single.2.base_tax=134]] USD | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Cumulative bracket sum rounded to whole dollars. |
| `hi.wh.bracket.single.2.ceiling` | [[FACT:hi.wh.bracket.single.2.ceiling=14,400]] USD | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-HIS5-004. |
| `hi.wh.bracket.single.2.rate` | [[FACT:hi.wh.bracket.single.2.rate=3.2]] % | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-HIS5-004. |
| `hi.wh.bracket.single.3.base_tax` | [[FACT:hi.wh.bracket.single.3.base_tax=288]] USD | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Cumulative bracket sum rounded to whole dollars. |
| `hi.wh.bracket.single.3.ceiling` | [[FACT:hi.wh.bracket.single.3.ceiling=19,200]] USD | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-HIS5-004. |
| `hi.wh.bracket.single.3.rate` | [[FACT:hi.wh.bracket.single.3.rate=5.5]] % | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-HIS5-004. |
| `hi.wh.bracket.single.4.base_tax` | [[FACT:hi.wh.bracket.single.4.base_tax=552]] USD | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Cumulative bracket sum rounded to whole dollars. |
| `hi.wh.bracket.single.4.ceiling` | [[FACT:hi.wh.bracket.single.4.ceiling=24,000]] USD | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-HIS5-004. |
| `hi.wh.bracket.single.4.rate` | [[FACT:hi.wh.bracket.single.4.rate=6.4]] % | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-HIS5-004. |
| `hi.wh.bracket.single.5.base_tax` | [[FACT:hi.wh.bracket.single.5.base_tax=859]] USD | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Cumulative bracket sum rounded to whole dollars. |
| `hi.wh.bracket.single.5.ceiling` | [[FACT:hi.wh.bracket.single.5.ceiling=36,000]] USD | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-HIS5-004. |
| `hi.wh.bracket.single.5.rate` | [[FACT:hi.wh.bracket.single.5.rate=6.8]] % | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-HIS5-004. |
| `hi.wh.bracket.single.6.base_tax` | [[FACT:hi.wh.bracket.single.6.base_tax=1,675]] USD | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Cumulative bracket sum rounded to whole dollars. |
| `hi.wh.bracket.single.6.ceiling` | [[FACT:hi.wh.bracket.single.6.ceiling=48,000]] USD | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-HIS5-004. |
| `hi.wh.bracket.single.6.rate` | [[FACT:hi.wh.bracket.single.6.rate=7.2]] % | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-HIS5-004. |
| `hi.wh.bracket.single.7.base_tax` | [[FACT:hi.wh.bracket.single.7.base_tax=2,539]] USD | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Cumulative bracket sum rounded to whole dollars. |
| `hi.wh.bracket.single.7.ceiling` | [[FACT:hi.wh.bracket.single.7.ceiling=125,000]] USD | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-HIS5-004. |
| `hi.wh.bracket.single.7.rate` | [[FACT:hi.wh.bracket.single.7.rate=7.6]] % | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-HIS5-004. |
| `hi.wh.bracket.single.8.base_tax` | [[FACT:hi.wh.bracket.single.8.base_tax=8,391]] USD | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Cumulative bracket sum rounded to whole dollars. |
| `hi.wh.bracket.single.8.rate` | [[FACT:hi.wh.bracket.single.8.rate=7.9]] % | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-HIS5-004. |
| `hi.wh.certificate.form` | [[FACT:hi.wh.certificate.form=HW-4 (Rev. 2022): Single / Married / Married-withhold-Single / Certified Disabled / Nonresident Military Spouse; no exempt status; federal W-4 not accepted; no HW-4 = Single 0; HoH withheld as Single + extra allowance; copy to Tax Assessor for excessive (>10) allowances]] | 2022-01-01 to open | US-HIS5-026 (Hawaii Department of Taxation; A.2, direct artifact inspection, confidence high) |  |
| `hi.wh.lump_sum_allowance.annual` | [[FACT:hi.wh.lump_sum_allowance.annual=4,350]] USD | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Every employee; weekly 83.65 ([[FACT:hi.wh.lump_sum_allowance.annual=4,350]]/52, re-derived). |
| `hi.wh.method` | [[FACT:hi.wh.method=wage-bracket tables (Part 3), annualized formula (Part 1) or per-period formula (Part 2), Booklet A Rev. 2025, effective 2026-01-01]] | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Still current 2026-11-02 [US-HIS5-005]. Supplemental: no flat rate; aggregate with current/preceding period or average over periods covered. No withholding below 0.10 per payment. |

Not yet published (expected December 2026) [[GAP:RQ-170]]: TY2027 thresholds/cumulative amounts after Act 24 SLH 2026 and the 2027 withholding tables are unpublished; Act text not accessible (HTTP 403).

Not configured in this release [[GAP:RQ-171]]: Full HRS 235-2.3(b) non-operative IRC list after Act 35 not read (HSA etc.).

## HI.2b Non-resident regime and reciprocity

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `hi.nonres.exempt_days` | [[FACT:hi.nonres.exempt_days=60]] days | 2026-01-01 to open | US-HIP51-002 (Hawaii Department of Taxation; A.2, quoted from authority page, confidence high) | Booklet A s.13: nonresident <= 60 days exempt with HW-6, paid from outside HI, regular workplace outside HI; HW-7 with original HW-6; never construction contractor employees. Resident = domicile or > 200 days. No reciprocity, no local tax [US-HIP9V-002]. |

## HI.2c Local wage taxes

No jurisdiction-specific item was recorded in the research for this domain.

## HI.3 Social insurance: unemployment, disability, paid leave and payroll levies

No PFML (TDI only). Only employer levy is E&T. Schedule C minimum rate not transcribed.

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `hi.phc.employee_share.max_percent_of_wages` | [[FACT:hi.phc.employee_share.max_percent_of_wages=1.5]] % | 2026-01-01 to open | US-HIS5-015 (Hawaii DLIR Disability Compensation Division; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-HIS5-015. |
| `hi.phc.min_monthly_wage` | [[FACT:hi.phc.min_monthly_wage=1,387]] USD | 2026-01-01 to 2027-12-31 | US-HIS5-015 (Hawaii DLIR Disability Compensation Division; A.2, derived arithmetically, confidence high) | Prepaid Health Care: regular employees 20+ h/week earning >= 86.67 x MW (1,386.72 rounded up by DCD); employee share max half premium and max [[FACT:hi.phc.employee_share.max_percent_of_wages=1.5]]% of wages [US-HIS5-016]. 2028 derived 1,560.06 not published. |
| `hi.sui.employee.rate` | [[FACT:hi.sui.employee.rate=0]] % | 2026-01-01 to open | US-HIS5-010 (Hawaii State Legislature; A.1, derived arithmetically, confidence high) | HRS 383-61(a) forbids deduction. |
| `hi.sui.employer.rate.max` | [[FACT:hi.sui.employer.rate.max=5.6]] % | 2026-01-01 to 2026-12-31 | US-HIP9V-001 (Hawaii Department of Labor and Industrial Relations; A.2, quoted from authority page, confidence high) |  |
| `hi.sui.et_assessment.rate` | [[FACT:hi.sui.et_assessment.rate=0.01]] % | 2026-01-01 to 2026-12-31 | US-HIP9V-001 (Hawaii Department of Labor and Industrial Relations; A.2, quoted from authority page, confidence high) | Employers above 0% and below schedule max; not FUTA-creditable. |
| `hi.sui.new_employer.rate` | [[FACT:hi.sui.new_employer.rate=2.4]] % | 2026-01-01 to 2026-12-31 | US-HIS5-011 (Hawaii DLIR Unemployment Insurance Division; A.2, second independent authority, confidence high) | Schedule C; rate at reserve ratio .0000. |
| `hi.sui.wage_base` | [[FACT:hi.sui.wage_base=64,500]] USD | 2026-01-01 to 2026-12-31 | US-HIP9V-001 (Hawaii Department of Labor and Industrial Relations; A.2, derived arithmetically, confidence high) | HRS 383-61(b): AAW 4 quarters to 30 June rounded to 100; DCD AAW 64,471.82 -> [[FACT:hi.sui.wage_base=64,500]] (G-CALIBER: both DLIR state averages, assumed same caliber). Other-state wages combine toward base [US-HIS5-012]. |
| `hi.tdi.benefit.weekly_max` | [[FACT:hi.tdi.benefit.weekly_max=871]] USD | 2026-01-01 to 2026-12-31 | US-HIS5-015 (Hawaii DLIR Disability Compensation Division; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-HIS5-015. |
| `hi.tdi.employee.max_rate` | [[FACT:hi.tdi.employee.max_rate=0.5]] % | 2026-01-01 to open | US-HIS5-014 (Hawaii State Legislature; A.1, derived arithmetically, confidence high) | Employer may withhold half the cost, max [[FACT:hi.tdi.employee.max_rate=0.5]]% of weekly wages; eligibility 400 + 14 weeks of 20+ h in prior 52 weeks; insurer-funded, no state return. |
| `hi.tdi.employee.max_weekly_deduction` | [[FACT:hi.tdi.employee.max_weekly_deduction=7.50]] USD | 2026-01-01 to 2026-12-31 | US-HIS5-015 (Hawaii DLIR Disability Compensation Division; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-HIS5-015. |
| `hi.tdi.max_weekly_wage_base` | [[FACT:hi.tdi.max_weekly_wage_base=1,500.21]] USD | 2026-01-01 to 2026-12-31 | US-HIS5-015 (Hawaii DLIR Disability Compensation Division; A.2, derived arithmetically, confidence high) | 64,471.82 / 52 x 1.21 [US-HI-003]. |

Not configured in this release [[GAP:RQ-172]]: Minimum rate and full Schedule C table not in the page text (image Table 2).

Not configured in this release [[GAP:RQ-173]]: HRS 392-4/392-5 localization not read; recommendation: key TDI to sui_state = HI meanwhile.

Not configured in this release [[GAP:RQ-174]]: December 2026 DLIR (UI base/schedule) and DCD (TDI) notices not yet published.

## HI.4 Pay statement

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `hi.payslip.items` | [[FACT:hi.payslip.items=employee name; employer name, address, phone; total hours; regular and OT hours; straight-time pay; OT pay; other compensation incl. MW allowances; gross; amount and purpose of each deduction; net; pay date; pay period; rates and basis incl. OT and piece rates/counts]] | 2026-01-01 to open | US-HIS5-007 (Hawaii State Legislature; A.1, direct artifact inspection, confidence medium) | HRS 387-6(c) 14 items [US-HIP52-001]; electronic with written authorization; direct deposit still requires statement. |

Not configured in this release [[GAP:RQ-175]]: The 14-item list of HRS 387-6(c) is carried by row US-HIP52-001; the fact cites US-HIS5-007 at medium confidence.

## HI.5 Statutory reporting

Registration BB-1 / Hawaii Tax Online. TDI and PHC via insurers, no state wage return. BLS 3020 for 10+ at secondary sites.

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `hi.newhire.report_days` | [[FACT:hi.newhire.report_days=20]] days | 2026-01-01 to open | US-HIS5-021 (Hawaii Department of the Attorney General, Child Support Enforcement Agency; A.2, quoted from authority page, confidence high) | CSEA: copy of W-4 by fax/mail or SFTP FLO101 fixed-width; rehire after 60+ days; penalty 25 / 500. |
| `hi.report.sui.ucb6` | [[FACT:hi.report.sui.ucb6=UC-B6 quarterly wage/contribution/E&T report due last day of month after quarter, even with no wages; name, SSN, total wages; late report 30, late contributions 10% (min 100) + 2/3%/month; registration within 20 days after first hire]] | 2026-01-01 to open | US-HIS5-012 (Hawaii DLIR Unemployment Insurance Division; A.3, quoted from authority page, confidence medium) |  |
| `hi.report.w2.efile_threshold_forms` | [[FACT:hi.report.w2.efile_threshold_forms=10]] forms | 2026-01-01 to open | US-HIS5-006 (Hawaii Department of Taxation; A.2, quoted from authority page, confidence high) | TA 2025-05; also if liability > [[FACT:hi.report.wh.semiweekly_threshold=40,000]]; penalty 25/form up to 50/employee; W-2/HW-2 to DOTAX by 31 Jan; EFW2 upload (EF-10), Simple File Import <= 1,000 records (EF-12), Bulk SFTP (EF-9); HW-30 paper transmittal only. |
| `hi.report.wh.hw14` | [[FACT:hi.report.wh.hw14=HW-14 quarterly due Apr 15/Jul 15/Oct 15/Jan 15, filed even with no wages; VP-1 deposits quarterly <= 5,000, monthly 5,000-40,000 (15th), semi-weekly > 40,000 or federal semi-weekly (no lookback)]] | 2026-01-01 to open | US-HIS5-005 (Hawaii Department of Taxation; A.2, quoted from authority page, confidence high) |  |
| `hi.report.wh.semiweekly_threshold` | [[FACT:hi.report.wh.semiweekly_threshold=40,000]] USD | 2026-01-01 to open | US-HIS5-005 (Hawaii Department of Taxation; A.2, quoted from authority page, confidence high) |  |

Not configured in this release [[GAP:RQ-176]]: Hawaii-specific EFW2 RS requirements (Tax ID position) not read.

Not configured in this release [[GAP:RQ-177]]: Bulk/file format for UC-B6 beyond online entry not located (behind the employer login).

## HI.6 Leave

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `hi.leave.family.employer_threshold` | [[FACT:hi.leave.family.employer_threshold=100]] employees | 2026-01-01 to open | US-HIS5-023 (Hawaii DLIR Wage Standards Division; A.3, quoted from authority page, confidence medium) | HRS ch. 398 (HRS 398-1 not read): 4 weeks unpaid per year after 6 months; up to 10 days accrued sick leave usable [US-HIS5-018]. |
| `hi.leave.sick.state_mandate.exists` | [[FACT:hi.leave.sick.state_mandate.exists=False]] | 2026-01-01 to open | US-HIS5-024 (Hawaii DLIR Wage Standards Division; A.2, direct artifact inspection, confidence medium) |  |

## HI.7 Termination and final pay

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `hi.final_pay.rule` | [[FACT:hi.final_pay.rule=discharge: at discharge or next working day; resignation: next regular payday (at quitting if one pay period notice); layoff: next regular payday (HRS 388-3)]] | 2026-01-01 to open | US-HIS5-008 (Hawaii State Legislature; A.1, direct artifact inspection, confidence high) | Accrued vacation not wages (108 H. 411, 2005): policy governs. No employer UI separation notice. |

## HI.8 Benefits in kind and taxable wages

No jurisdiction-specific item was recorded in the research for this domain.

## HI.9 Deductions and garnishments

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `hi.deductions.rule` | [[FACT:hi.deductions.rule=only if required by statute/court or authorised in writing; never fines, till shortages, breakage, dishonored checks, non-wilful losses, required medical exams (HRS 388-6)]] | 2026-01-01 to open | US-HIS5-009 (Hawaii State Legislature; A.1, direct artifact inspection, confidence high) |  |
| `hi.garn.child_support.employer_fee` | [[FACT:hi.garn.child_support.employer_fee=2]] USD | 2003-01-01 to open | US-HIS5-022 (Hawaii Department of the Attorney General, Child Support Enforcement Agency; A.3, quoted from authority page, confidence medium) | FEN125 remittance and start timing: not configured in this release; CCPA 50/60% + 5%. |
| `hi.garn.child_support.remit_working_days` | [[FACT:hi.garn.child_support.remit_working_days=5]] working days | 2003-01-01 to open | US-HIS5-022 (Hawaii Department of the Attorney General, Child Support Enforcement Agency; A.3, quoted from authority page, confidence medium) |  |
| `hi.garn.creditor.schedule` | [[FACT:hi.garn.creditor.schedule=5% of first 100/month, 10% of next 100, 20% above 200 (weekly equivalent) on wages after required deductions; apply lower of this and CCPA]] | 2026-01-01 to open | US-HIS5-019 (Hawaii State Legislature; A.1, direct artifact inspection, confidence high) |  |

Not configured in this release [[GAP:RQ-178]]: DOTAX wage levy not established from an official source.

Not configured in this release [[GAP:RQ-583]]: The remittance and start timing of income withholding orders (form FEN125) are not established from an official source.

## HI.10 Collective agreements and prevailing wage

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `hi.prevailing_wage.certified_payroll` | [[FACT:hi.prevailing_wage.certified_payroll=weekly certified payroll + fringe-benefit form to contracting agency (GC for subs); records 3 years, produced within 10 days]] | 2026-01-01 to open | US-HIS5-020 (Hawaii State Legislature; A.1, direct artifact inspection, confidence high) |  |
| `hi.prevailing_wage.threshold` | [[FACT:hi.prevailing_wage.threshold=2,000]] USD | 2026-01-01 to open | US-HIP52-002 (Hawaii Legislature; A.1, quoted from authority page, confidence high) | HRS ch. 104 public-works construction over 2,000. |

## HI.11 Indexation

UI base AAW (nearest 100); TDI max weekly AAW/52 x 1.21; PHC 86.67 x MW; MW statutory steps; PIT statutory (Act 24 changes 2027).

## HI.12 Payroll data protection and records

HRS 487J-2: no public display/mailing of full SSN (employer-employee mail allowed if not visible) [US-HIS5-028]. Full SSN on UC-B6, new hire, W-2/HW-2. Pay statement retention 6 years (388-7) [US-HIP51-003].

## HI.13 Live legal change

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `hi.live.act24_2026` | [[FACT:hi.live.act24_2026=in force (TA 2026-06, 2026-07-31): TY2027 2nd bracket 3.2 -> 2.5%, 3rd 5.5 -> 5%, new 13% top bracket; level assessment from TY2027 and withholding from 2027-01-01 once the 2027 Booklet A issues]] | 2026-07-31 to open | US-HIS5-029 (Hawaii Department of Taxation; A.2, quoted from authority page, confidence medium) | Act text not accessible (HTTP 403) [US-HIS5-030]; HRS 235-51 snapshot superseded in part [US-HIS5-027 partial]. |

## HI.14 Authority worked examples (oracle values)

Each example is computed from the statutory parameters listed in this annex and checked against the result published by the authority. Amounts round half-up to the cent unless the line states another rule.

**Example HI-1: single, 3 allowances, weekly wages 500.00 (Booklet A, Part 1 annualised method).**

| Line | Calculation | Result |
|---|---|---|
| Annual wages | 500.00 x 52 | 26,000.00 |
| Allowances | 3 x [[FACT:hi.wh.allowance.annual=1,144]] | 3,432.00 |
| Taxable wages | 26,000.00 - 3,432.00 - [[FACT:hi.wh.lump_sum_allowance.annual=4,350]] | 18,218.00 |
| Bracket | above [[FACT:hi.wh.bracket.single.2.ceiling=14,400]] up to [[FACT:hi.wh.bracket.single.3.ceiling=19,200]] | bracket 3 |
| Annual tax | [[FACT:hi.wh.bracket.single.3.base_tax=288]] + (18,218.00 - [[FACT:hi.wh.bracket.single.2.ceiling=14,400]]) x [[FACT:hi.wh.bracket.single.3.rate=5.5]] % | 497.99 |
| Weekly withholding | 497.99 / 52, half-up to the cent | [[FACT:hi.oracle.weekly_500_s3.withholding=9.58]] |

Computed result = published [[FACT:hi.oracle.weekly_500_s3.withholding=9.58]] (match).

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `hi.oracle.weekly_500_s3.withholding` | [[FACT:hi.oracle.weekly_500_s3.withholding=9.58]] USD | 2026-01-01 to 2026-12-31 | US-HIS5-004 (Hawaii Department of Taxation; A.2, derived arithmetically, confidence high) | Single, 3 allowances, 500/week: 26,000 - 3,432 - [[FACT:hi.wh.lump_sum_allowance.annual=4,350]] = 18,218; [[FACT:hi.wh.bracket.single.3.base_tax=288]] + 3,818 x 5.5% = 497.99; /52 = [[FACT:hi.oracle.weekly_500_s3.withholding=9.58]]. Re-derived exactly. |

## HI.15 Special populations

- Domestic: withholding required unless casual (< 50 cash/quarter or not regular); UI at 1,000/quarter; casual domestic/companionship outside wage-hour law [US-HIS5-013].
- Agricultural: withholding required; UI excluded < 20,000/quarter and <= 9 workers/19 weeks; H-2A excluded; MW excludes farms < 20 and coffee harvesting [US-HIS5-013, US-HIS5-003].
- Minors: CL-1 (14-15) / eCL-3 (16-17); newspaper carriers < 18 outside withholding and UI [US-HIS5-025, US-HIS5-013].
- Tipped: tip credit [[FACT:hi.minwage.tip_credit=1.25]] with MW + 7.00 test; withholding on reported tips >= 20/month; IRC 224 deduction at assessment [US-HIS5-001, US-HIS5-029].
- Clergy: no withholding; ordained church members outside UI [US-HIS5-013].
- Students: own-school, school-to-work, student nurses/interns outside UI [US-HIS5-013].
- NRAs: general nonresident rules (HW-6/60 days) and treaty exclusion.
- Statutory employees: commission insurance/real-estate/travel agents and direct sellers outside UI [US-HIS5-013].
- Government: federal/other-state service outside UI; State and counties outside PHC [US-HIS5-013, US-HIS5-016].
- Certified blind/deaf/disabled and MSRRA spouses: no withholding [US-HIS5-026].
- Construction contractor employees: no 60-day exemption. Crew: no withholding. Family employment outside UI.

## HI.16 Language

No rule requires a non-English pay statement [US-HIL-001, US-HIL-002, US-HIP9L-001, US-HIP9L-002]; payslip English (US-OWN-006).

## HI.S Sources

The legal basis of each value (legal-basis register id, authority, source tier and verification method) is given in the row that carries it.
