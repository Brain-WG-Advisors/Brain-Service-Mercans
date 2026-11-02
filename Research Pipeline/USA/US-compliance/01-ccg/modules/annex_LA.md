# Annex LA: Louisiana

**Layer classification (T3).** T3: separate state withholding calculation and state return; no local layer, or a local layer piggybacked on the state return. Source: build manifest tier census, local income tax domain.

**Summary.** No state minimum wage (FLSA [[FACT:fed.minwage.hourly=7.25]]); local wage/leave mandates prohibited (23:642). Flat [[FACT:la.pit.rate.flat=3.09]]% withholding (R-1306 1/26): (S - [[FACT:la.wh.std_deduction.single=12,875]]/N) x 0.0309 or (S - [[FACT:la.wh.std_deduction.joint=25,750]]/N) x 0.0309; no supplemental rate; no local tax (constitutional bar), no reciprocity; Act 382 / LAC 61:I.1923 30-day nonresident mobile-workforce exemption (adopted LR 52:358, 2026-03-20). UI base [[FACT:la.sui.wage_base=7,000]], rates [[FACT:la.sui.employer.rate.min=0.09]]%-[[FACT:la.sui.employer.rate.max=6.20]]%, no employee share. No pay-statement statute. Final pay earlier of next payday or 15 days. Child-support max 50%. Oracle: R-1306 examples [[FACT:la.oracle.r1306.example1.withholding=13.98]] / [[FACT:la.oracle.r1306.example2.withholding=111.54]].

Each parameter row gives its key, the period in force and its legal basis: the legal-basis register row, the authority, the source tier and how the value was verified.

## LA.1 Employment and labour code

Overtime: no state statute located (FLSA; medium). Direct deposit/paycard: no consent statute; 23:633 requires only notice of method.

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `la.local_mandates.preempted` | [[FACT:la.local_mandates.preempted=True]] | 2026-01-01 to open | US-LAS5-005 (Louisiana State Legislature; A.1, direct artifact inspection, confidence high) | R.S. 23:642: no local minimum wage or mandatory vacation/sick days. |
| `la.minwage.state_law.exists` | [[FACT:la.minwage.state_law.exists=False]] | 2026-01-01 to open | US-LAS5-006 (U.S. Department of Labor Wage and Hour Division; A.2, direct artifact inspection, confidence high) | FLSA [[FACT:fed.minwage.hourly=7.25]] for covered employers; no 2027 rate. |
| `la.pay_frequency.rule` | [[FACT:la.pay_frequency.rule=notice at hire of wage, method and frequency; undesignated paydays 1st and 16th; manufacturing/oil-boring/mining 10+ and public-service corporations at least twice monthly; FLSA-exempt outside; fine 25-250/day (23:633)]] | 2026-01-01 to open | US-LAS5-004 (Louisiana State Legislature; A.1, direct artifact inspection, confidence high) |  |

⚠️ RESEARCH-GAP: No consent statute located beyond 23:633 notice. (open item `la.payment.direct_deposit_consent`, non-blocking; would close it: Louisiana Works wage-payment FAQ.)

## LA.2 State income tax withholding

Certificate R-1300 (L-4); edition not re-fetched (404). 2027 standard deduction unpublished.

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `la.pit.rate.flat` | [[FACT:la.pit.rate.flat=3.09]] % | 2026-01-01 to open | US-LAS5-001 (Louisiana Department of Revenue; A.2, quoted from authority page, confidence high) |  |
| `la.wh.method` | [[FACT:la.wh.method=no deduction: W = S x 0.0309; L-4 "1" (single/MFS): (S - 12,875/N) x 0.0309; L-4 "2" (MFJ/QSS/HoH): (S - 25,750/N) x 0.0309; N = 365/52/26/24/12/1; negative term = 0; round to cent]] | 2026-01-01 to 2026-12-31 | US-LAS5-001 (Louisiana Department of Revenue; A.2, quoted from authority page, confidence high) |  |
| `la.wh.std_deduction.joint` | [[FACT:la.wh.std_deduction.joint=25,750]] USD | 2026-01-01 to 2026-12-31 | US-LAS5-001 (Louisiana Department of Revenue; A.2, derived arithmetically, confidence high) | = 2 x [[FACT:la.wh.std_deduction.single=12,875]]. |
| `la.wh.std_deduction.single` | [[FACT:la.wh.std_deduction.single=12,875]] USD | 2026-01-01 to 2026-12-31 | US-LAS5-001 (Louisiana Department of Revenue; A.2, quoted from authority page, confidence high) | Indexed by prior-year CPI-U (R.S. 47:294(B)); set by emergency rule LAC 61:I.1501 effective 2026-01-01 (RIB 26-005, 2026-01-12) [US-LAS5-011]; official value may differ slightly once Jan-2026 CPI-U applied. |
| `la.wh.supplemental.method` | [[FACT:la.wh.supplemental.method=withheld like regular wages; no flat supplemental rate (vacation pay likewise)]] | 2026-01-01 to open | US-LAP51-002 (Louisiana Department of Revenue; A.3, quoted from authority page, confidence high) |  |
| `la.wh.who` | [[FACT:la.wh.who=residents; nonresidents performing services in LA (subject to the 30-day rule); residents working outside LA if not withheld in the other state]] | 2026-01-01 to open | US-LAS5-003 (Louisiana Department of Revenue; A.2, quoted from authority page, confidence high) |  |

⚠️ RESEARCH-GAP: State treatment of s.125, 401(k), HSA, transit, GTL not read (LDR FAQ 403/404). (open item `la.pit.conformity`, blocking; would close it: LDR cafeteria-plan FAQ and R.S. 47:293.)

## LA.2b Non-resident regime and reciprocity

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `la.nonres.mobile_workforce.days` | [[FACT:la.nonres.mobile_workforce.days=30]] days | 2026-01-01 to open | US-LAS5-002 (Louisiana Department of Revenue, Tax Policy and Planning Division (published in the Louisiana Register); A.1, direct artifact inspection, confidence high) | Act 382 (2025) R.S. 47:112.2(A), 47:248 [US-MULTIS5-021]; LAC 61:I.1923 adopted LR 52:358 (2026-03-20): <= 30 days exempt (C.1.a says "less than 30" - statute governs); employee notifies within 10 days from day 31; employer begins withholding and reports on L-1 from the period of the 31st day; exemption lost with other LA-source income; home-state condition repealed. Level withholding. Catch-up of days 1-30 open. Build: per-employee LA workday counter (employer + related entities) and other-LA-income flag. |

⚠️ RESEARCH-GAP: From day 31, whether days 1-30 are withheld as a lump catch-up in the period of the 31st day: MULTI row (Act text) says yes; the regulation only says begin withholding in that period. (open item `la.nonres.mobile_workforce.catch_up`, blocking; would close it: Codified R.S. 47:112.2(A) text or an LDR RIB/FAQ on the mobile workforce exemption.)

## LA.2c Local wage taxes

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `la.local_income_tax.exists` | [[FACT:la.local_income_tax.exists=False]] | 2026-01-01 to open | US-LAP52-001 (Louisiana State Senate (constitution text); A.1, quoted from authority page, confidence high) | Constitution bars parish/municipal income tax. |

## LA.3 Social insurance (unemployment, disability, paid leave, levies)

No SDI/TDI/PFML [US-LAP52-002, DOL WB list]. No employee contribution.

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `la.agency.name` | [[FACT:la.agency.name=Louisiana Works (replaces Louisiana Workforce Commission); keep laworks.net]] | 2026-01-01 to open | US-LAS5-004 (Louisiana State Legislature; A.1, direct artifact inspection, confidence high) |  |
| `la.sui.employer.rate.max` | [[FACT:la.sui.employer.rate.max=6.2]] % | 2026-01-01 to 2026-12-31 | US-LAP9V-002 (Louisiana Workforce Commission; A.2, derived arithmetically, confidence medium) | Derivation recorded in register row US-LAP9V-002. |
| `la.sui.employer.rate.min` | [[FACT:la.sui.employer.rate.min=0.09]] % | 2026-01-01 to 2026-12-31 | US-LASUI-001 (Louisiana Workforce Commission; A.2, quoted from authority page, confidence high) | 2026 LWC rate table: [[FACT:la.sui.employer.rate.min=0.09]]% at reserve ratio 9.5+ to [[FACT:la.sui.employer.rate.max=6.20]]%. |
| `la.sui.new_employer.rate` | [[FACT:la.sui.new_employer.rate=average rate of its NAICS industrial classification; experience rating after 24 months]] | 2026-01-01 to open | US-LAP9V-001 (Louisiana Workforce Commission; A.2, quoted from authority page, confidence high) | Social charges (non-charge, IWTP, Integrity) inside the total rate; IWTP and Integrity not FUTA-creditable [US-LAS5-007]. |
| `la.sui.wage_base` | [[FACT:la.sui.wage_base=7,000]] USD | 2026-01-01 to 2026-12-31 | US-LAP9V-001 (Louisiana Workforce Commission; A.2, quoted from authority page, confidence medium) | 23:1536 mechanism not read (secondary source: 7,700 in 2025). |

⚠️ RESEARCH-GAP: R.S. 23:1536 wage-base mechanism and other-state wage credit not read. (open item `la.sui.wage_base.mechanism`, non-blocking; would close it: Wayback read of R.S. 23:1536.)

## LA.4 Pay statement

No itemised pay-statement statute in R.S. 23:631-638 (all read) [US-LAR3-002]; only hire notice of rate/method/frequency [US-LAS5-004]. Retention unread.

## LA.5 Statutory reporting

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `la.newhire.report_days` | [[FACT:la.newhire.report_days=20]] days | 2026-01-01 to open | US-LAS5-010 (Louisiana State Legislature; A.1, direct artifact inspection, confidence high) | DCFS: name, address, SSN, occupation, first day; employer name, address, EIN; rehire incl. return from layoff/furlough/leave (no 60-day threshold in statute); penalty 25 / 500. |
| `la.report.annual.l3` | [[FACT:la.report.annual.l3=L-3 + W-2s due first business day after January 31 (30 days on closure); electronic mandatory at 50+ W-2s via LaWage; no magnetic media/CD; state boxes 16-18]] | 2026-01-01 to open | US-LAS5-009 (Louisiana Department of Revenue; A.3, quoted from authority page, confidence high) |  |
| `la.report.sui.quarterly` | [[FACT:la.report.sui.quarterly=due last day of month after quarter; domestic annual Jan 31; mandatory electronic (LAWATS); DE students earning credit not reported]] | 2025-04-01 to open | US-LAS5-007 (Louisiana Workforce Commission; A.3, quoted from authority page, confidence medium) |  |
| `la.report.w2.efile_threshold` | [[FACT:la.report.w2.efile_threshold=50]] forms | 2026-01-01 to open | US-LAS5-009 (Louisiana Department of Revenue; A.3, quoted from authority page, confidence high) |  |
| `la.report.wh.l1` | [[FACT:la.report.wh.l1=L-1 quarterly, electronic (LaTAP/software), zero returns required, due Apr 30 / Jul 31 / Oct 31 / Jan 31; payment quarterly < 500/month average, monthly 500 to < 5,000, semi-monthly >= 5,000]] | 2026-01-01 to open | US-LAS5-003 (Louisiana Department of Revenue; A.2, quoted from authority page, confidence high) | [US-LAS5-008]. |

⚠️ RESEARCH-GAP: LaWage bulk W-2 file format (EFW2 or LA layout) not read. (open item `la.report.w2.lawage_format`, non-blocking; would close it: LDR LaWage / W-2 electronic filing specification on dam.ldr.la.gov.)

⚠️ RESEARCH-GAP: UI form name and LAWATS upload format (ICESA?) and a 2026 FAQ copy not read. (open item `la.report.sui.format`, non-blocking; would close it: Louisiana Works LAWATS file specification.)

## LA.6 Leave

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `la.leave.jury.paid_days` | [[FACT:la.leave.jury.paid_days=1]] days | 2026-01-01 to open | US-LAS5-013 (Louisiana State Legislature; A.1, direct artifact inspection, confidence high) | R.S. 23:965: one paid day without loss of wages or leave; fines 100-500 / 100-1,000 + reinstatement. |

⚠️ RESEARCH-GAP: Voting, military, school conference, bone marrow/organ donation leave not read. (open item `la.leave.other`, non-blocking; would close it: R.S. 23:961-1015 via Wayback.)

## LA.7 Termination and final pay

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `la.final_pay.max_days` | [[FACT:la.final_pay.max_days=15]] days | 2026-01-01 to open | US-LAR3-002 (Louisiana State Legislature; A.1, quoted from authority page, confidence high) |  |
| `la.final_pay.penalty_wages.max_days` | [[FACT:la.final_pay.penalty_wages.max_days=90]] days | 2026-01-01 to open | US-LAR3-001 (Louisiana State Legislature; A.1, quoted from authority page, confidence high) | 23:632: lesser of 90 days wages or full wages from demand + fees; good-faith dispute: wages + interest. |
| `la.final_pay.rule` | [[FACT:la.final_pay.rule=discharge or resignation: earlier of next regular payday (for the cycle worked) or 15 days; customary place/method or prepaid mail; CBA override; earned eligible vacation is due and cannot be forfeited; commissions/bonuses due if earned (23:631)]] | 2026-01-01 to open | US-LAR3-002 (Louisiana State Legislature; A.1, quoted from authority page, confidence high) |  |
| `la.test_cost_recovery.working_days` | [[FACT:la.test_cost_recovery.working_days=90]] working days | 2026-01-01 to open | US-LAS5-004 (Louisiana State Legislature; A.1, direct artifact inspection, confidence high) | 23:634(B): only if pay >= federal MW + 1 and not part-time/seasonal. |

⚠️ RESEARCH-GAP: LWC Form 1 separation duty not read. (open item `la.termination.ui_separation_notice`, non-blocking; would close it: LAC 40:IV or a Louisiana Works employer page.)

## LA.8 Benefits in kind and taxable wages

No LA source read (LDR cafeteria FAQ 404); LA starts from federal AGI (lead). Confidence 30%.

## LA.9 Deductions and garnishments

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `la.deductions.fines` | [[FACT:la.deductions.fines=prohibited except wilful/negligent damage or theft of employer funds, capped at actual damage (23:635)]] | 2026-01-01 to open | US-LAS5-004 (Louisiana State Legislature; A.1, direct artifact inspection, confidence high) |  |
| `la.garn.child_support.max_percent` | [[FACT:la.garn.child_support.max_percent=50]] % | 2026-01-01 to open | US-LAS5-012 (Louisiana State Legislature; A.1, direct artifact inspection, confidence high) | Exemption 50% child support, 60% spousal (stricter than CCPA); mixed/unclear DCFS order = child support. |
| `la.garn.creditor.exempt_percent` | [[FACT:la.garn.creditor.exempt_percent=75]] % | 2026-01-01 to open | US-LAS5-012 (Louisiana State Legislature; A.1, direct artifact inspection, confidence high) | R.S. 13:3881(A)(1)(a): [[FACT:la.garn.creditor.exempt_percent=75]]% of weekly disposable exempt, never less than 30 x federal MW (CCPA-equivalent); disposable also after retirement/medical/life-insurance deductions and amounts owed to employer. |

⚠️ RESEARCH-GAP: IWO employer fee, priority, SDU remittance not read. (open item `la.garn.iwo_specifics`, non-blocking; would close it: R.S. 46:236.3 / 9:303 and the DCFS employer page.)

## LA.10 Collective agreements and prevailing wage

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `la.cba.fringe_as_wages` | [[FACT:la.cba.fringe_as_wages=True]] | 2026-01-01 to open | US-LAS5-015 (Louisiana State Legislature; A.1, direct artifact inspection, confidence high) | R.S. 23:640: CBA fringe amounts treated as wages for penalty-wage rules. Prevailing wage repealed 1988 [US-LAP6-001]. |

## LA.11 Indexation

Std deduction CPI-U (R.S. 47:294(B)); SUI base mechanism unread; no MW law.

## LA.12 Payroll data protection and records

Not researched.

⚠️ RESEARCH-GAP: No LA payroll-record retention rule read. (open item `la.records.retention`, non-blocking; would close it: R.S. 23:1660 and any LDR withholding-record retention rule.)

⚠️ RESEARCH-GAP: SSN display statutes not researched. (open item `la.data_protection.ssn`, non-blocking; would close it: LA SSN display statutes and R.S. 51:3071 et seq. via Wayback.)

## LA.13 Live legal change

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `la.live.lac_61_i_1923` | [[FACT:la.live.lac_61_i_1923=adopted LR 52:358 (2026-03-20), supersedes the NOI (US-MULTIS5-022); level withholding]] | 2026-03-20 to open | US-LAS5-002 (Louisiana Department of Revenue, Tax Policy and Planning Division (published in the Louisiana Register); A.1, direct artifact inspection, confidence high) |  |
| `la.live.sb133_2025` | [[FACT:la.live.sb133_2025=not codified (technical; adds "laborers")]] | 2025-01-01 to open | US-LAS5-014 (Louisiana State Legislature; A.1, direct artifact inspection, confidence medium) | [partial row] |

⚠️ RESEARCH-GAP: Only page 1 (Acts 1-100) of the 2026 Acts list readable (ASP.NET postback). (open item `la.live.acts_2026_sweep`, non-blocking; would close it: Remaining 2026 Acts pages.)

## LA.14 Worked examples

Each example is computed from the statutory parameters listed in this annex and checked against the result published by the authority. Amounts round half-up to the cent unless the line states another rule.

**Example LA-1: L-4 status 1, weekly wages 700.00 (R-1306 formula).**

| Line | Calculation | Result |
|---|---|---|
| Period deduction | [[FACT:la.wh.std_deduction.single=12,875]] / 52 | 247.5962 |
| Withholding | (700.00 - 247.5962) x [[FACT:la.pit.rate.flat=3.09]] % = 13.9793, half-up to the cent | [[FACT:la.oracle.r1306.example1.withholding=13.98]] |

Computed result = published [[FACT:la.oracle.r1306.example1.withholding=13.98]] (match).

**Example LA-2: L-4 status 2, biweekly wages 4,600.00 (R-1306 formula).**

| Line | Calculation | Result |
|---|---|---|
| Period deduction | [[FACT:la.wh.std_deduction.joint=25,750]] / 26 | 990.3846 |
| Withholding | (4,600.00 - 990.3846) x [[FACT:la.pit.rate.flat=3.09]] % = 111.5371, half-up to the cent | [[FACT:la.oracle.r1306.example2.withholding=111.54]] |

Computed result = published [[FACT:la.oracle.r1306.example2.withholding=111.54]] (match).

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `la.oracle.r1306.example1.withholding` | [[FACT:la.oracle.r1306.example1.withholding=13.98]] USD | 2026-01-01 to 2026-12-31 | US-LAS5-001 (Louisiana Department of Revenue; A.2, derived arithmetically, confidence high) | (700 - [[FACT:la.wh.std_deduction.single=12,875]]/52) x 0.0309 = 13.9793 -> [[FACT:la.oracle.r1306.example1.withholding=13.98]]. |
| `la.oracle.r1306.example2.withholding` | [[FACT:la.oracle.r1306.example2.withholding=111.54]] USD | 2026-01-01 to 2026-12-31 | US-LAS5-001 (Louisiana Department of Revenue; A.2, derived arithmetically, confidence high) | (4,600 - [[FACT:la.wh.std_deduction.joint=25,750]]/26) x 0.0309 = 111.5371 -> [[FACT:la.oracle.r1306.example2.withholding=111.54]]. |

## LA.15 Special populations

- Nonresidents (incl. NRAs working in LA): 30-day mobile-workforce exemption; withhold from period of day 31; lost with other LA-source income [US-MULTIS5-021, US-LAS5-002].
- Domestic: UI annual filers Jan 31; household withholding FAQ unread [US-LAS5-007].
- Students: UI DE students earning credit not reported [US-LAS5-007].
- Minors: Act 61 (2026) employment certificates; no payroll rule [US-LAS5-016].
- Tipped: federal tip credit only [US-LAS5-006].
- FLSA-exempt staff outside 23:633; part-time/seasonal excluded from test-cost recovery [US-LAS5-004].
- Agricultural, clergy, statutory, government: no state rule read (federal assumed,). Military spouses: L-4E exists (title only).

⚠️ RESEARCH-GAP: Household withholding, ag/clergy/statutory/government UI coverage (R.S. 23:1472) and L-4E reporting not read. (open item `la.special_populations.other`, non-blocking; would close it: LDR FAQ pages and R.S. 23:1472.)

## LA.16 Language of employee documents

Posters in Spanish available [US-LAP9M-001]; no language clause in 23:631-638 [US-LAL-001, US-LAL-002]; payslip English (US-OWN-006).
