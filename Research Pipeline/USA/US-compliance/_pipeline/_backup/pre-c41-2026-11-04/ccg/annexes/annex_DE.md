# Annex DE: Delaware


**Layer classification (T4).** T4: separate state withholding calculation and state return, plus a local layer remitted to the locality on its own return. Source: build manifest tier census, local income tax domain.

**Summary.** Minimum wage 15.00 (fixed since 2025-01-01, not indexed); FLSA overtime. PIT 0-[[FACT:de.pit.bracket.7.rate=6.6]]% (30 Del. C. 1102, not indexed); withholding per Employer Guide (standard deduction [[FACT:de.wh.std_deduction.single=3,250]]/6,500, 110 credit per exemption); statutory convenience rule; no reciprocity; Wilmington [[FACT:de.local.wilmington.eit.rate=1.25]]% EIT. SUI employer-only, base [[FACT:de.sui.wage_base=14,500]] (2026) / [[FACT:de.sui.wage_base=16,500]] (2027), new [[FACT:de.sui.new_employer.rate=1.0]]%; Operations & Technology [[FACT:de.sui.op_tech_assessment.rate=0.2]]% billed separately by letter from 2026. Delaware Paid Leave [[FACT:de.pfml.rate.total=0.80]]% (2025-2026), employee share up to 50%. Pay statement for employers with more than 3 employees. Oracle: Employer Guide examples ([[FACT:de.oracle.weekly_25000.withholding=13.88]] weekly; [[FACT:de.oracle.supplemental.withholding=269.63]] supplemental).

Each parameter row gives its key, the period in force and its legal basis: the legal-basis register row, the authority, the source tier and how the value was verified.

## DE.1 Employment and labour code

Overtime: no state premium rule (ch. 9 read in full); FLSA 1.5x over 40. No local minimum wages (absence, 85%). No youth subminimum.

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `de.minor.work_permit.required` | [[FACT:de.minor.work_permit.required=True]] | 2026-01-01 to open | US-DES5-017 (Delaware General Assembly (Delaware Code Online); A.1, quoted from authority page, confidence high) | 19 Del. C. 504, under 18. |
| `de.minwage.exclusions` | [[FACT:de.minwage.exclusions=agriculture; private-home domestic service; EAP and outside sales; US government; fishing; under-18 camp counselors; DOC inmates; CBA minor-league baseball (901(3))]] | 2026-01-01 to open | US-DES5-001 (Delaware General Assembly (Delaware Code Online); A.1, quoted from authority page, confidence high) |  |
| `de.minwage.hourly` | [[FACT:de.minwage.hourly=15]] USD | 2025-01-01 to open | US-DES5-001 (Delaware General Assembly (Delaware Code Online); A.1, quoted from authority page, confidence high) | 19 Del. C. 902(a)(5): last statutory step, not indexed, no 2027 step; equals federal if federal exceeds. |
| `de.minwage.tipped.cash_wage` | [[FACT:de.minwage.tipped.cash_wage=2.23]] USD | 2026-01-01 to open | US-DES5-001 (Delaware General Assembly (Delaware Code Online); A.1, quoted from authority page, confidence high) | Make-up to [[FACT:de.minwage.hourly=15.00]]; mandatory tip pool capped at 15%; tips withheld as supplemental [US-DES5-021, US-DES5-006]. |
| `de.pay_frequency.rule` | [[FACT:de.pay_frequency.rule=at least once per calendar month on paydays designated in advance; due within 7 days of period close; nonwork-day payday moves earlier (1102)]] | 2026-01-01 to open | US-DES5-002 (Delaware General Assembly (Delaware Code Online); A.1, quoted from authority page, confidence high) |  |
| `de.payment.method` | [[FACT:de.payment.method=cash or check cashable at full value nearby; direct deposit only on employee written request; no paycard rule]] | 2026-01-01 to open | US-DES5-002 (Delaware General Assembly (Delaware Code Online); A.1, quoted from authority page, confidence high) |  |
| `de.wage_theft.penalty.max` | [[FACT:de.wage_theft.penalty.max=20,000]] USD | 2026-01-01 to open | US-DES5-002 (Delaware General Assembly (Delaware Code Online); A.1, quoted from authority page, confidence high) | 1102A: 2,000-[[FACT:de.wage_theft.penalty.max=20,000]] per violation per employee for failing to withhold, failing to forward within 7 days, misclassification. |

## DE.2 Income tax withholding

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `de.pit.bracket.1.ceiling` | [[FACT:de.pit.bracket.1.ceiling=2,000]] USD | 2014-01-01 to open | US-DES5-003 (Delaware General Assembly (Delaware Code Online); A.1, quoted from authority page, confidence high) | 0%. |
| `de.pit.bracket.2.ceiling` | [[FACT:de.pit.bracket.2.ceiling=5,000]] USD | 2014-01-01 to open | US-DES5-003 (Delaware General Assembly (Delaware Code Online); A.1, quoted from authority page, confidence high) |  |
| `de.pit.bracket.2.rate` | [[FACT:de.pit.bracket.2.rate=2.2]] % | 2014-01-01 to open | US-DES5-003 (Delaware General Assembly (Delaware Code Online); A.1, quoted from authority page, confidence high) |  |
| `de.pit.bracket.3.ceiling` | [[FACT:de.pit.bracket.3.ceiling=10,000]] USD | 2014-01-01 to open | US-DES5-003 (Delaware General Assembly (Delaware Code Online); A.1, quoted from authority page, confidence high) |  |
| `de.pit.bracket.3.rate` | [[FACT:de.pit.bracket.3.rate=3.9]] % | 2014-01-01 to open | US-DES5-003 (Delaware General Assembly (Delaware Code Online); A.1, quoted from authority page, confidence high) |  |
| `de.pit.bracket.4.ceiling` | [[FACT:de.pit.bracket.4.ceiling=20,000]] USD | 2014-01-01 to open | US-DES5-003 (Delaware General Assembly (Delaware Code Online); A.1, quoted from authority page, confidence high) |  |
| `de.pit.bracket.4.rate` | [[FACT:de.pit.bracket.4.rate=4.8]] % | 2014-01-01 to open | US-DES5-003 (Delaware General Assembly (Delaware Code Online); A.1, quoted from authority page, confidence high) |  |
| `de.pit.bracket.5.ceiling` | [[FACT:de.pit.bracket.5.ceiling=25,000]] USD | 2014-01-01 to open | US-DES5-003 (Delaware General Assembly (Delaware Code Online); A.1, quoted from authority page, confidence high) |  |
| `de.pit.bracket.5.rate` | [[FACT:de.pit.bracket.5.rate=5.2]] % | 2014-01-01 to open | US-DES5-003 (Delaware General Assembly (Delaware Code Online); A.1, quoted from authority page, confidence high) |  |
| `de.pit.bracket.6.ceiling` | [[FACT:de.pit.bracket.6.ceiling=60,000]] USD | 2014-01-01 to open | US-DES5-003 (Delaware General Assembly (Delaware Code Online); A.1, quoted from authority page, confidence high) |  |
| `de.pit.bracket.6.rate` | [[FACT:de.pit.bracket.6.rate=5.55]] % | 2014-01-01 to open | US-DES5-003 (Delaware General Assembly (Delaware Code Online); A.1, quoted from authority page, confidence high) |  |
| `de.pit.bracket.7.rate` | [[FACT:de.pit.bracket.7.rate=6.6]] % | 2014-01-01 to open | US-DES5-003 (Delaware General Assembly (Delaware Code Online); A.1, quoted from authority page, confidence high) | Over [[FACT:de.pit.bracket.6.ceiling=60,000]]. |
| `de.wh.certificate` | [[FACT:de.wh.certificate=Delaware W-4 (Employee's Withholding Allowance Certificate, Division of Revenue). A federal W-4 of 2020 or later may NOT be accepted for Delaware withholding; a federal W-4 completed before 2020 may still be relied on.]] | 2020-01-01 to open | US-DEB5-301 (Delaware Division of Revenue; A.3, quoted from authority page, confidence high) | The Division of Revenue FAQ answers "No" to accepting a 2020-version federal W-4 for Delaware withholding. The Employer's Guide (US-DES5-006) still uses pre-2020 W-4/allowance wording. Default without a certificate and the copy-to-Division rule: de.wh.certificate.default_and_copies. |
| `de.wh.deferred_comp.recommended_rate` | [[FACT:de.wh.deferred_comp.recommended_rate=5]] % | 2026-01-01 to open | US-DES5-006 (Delaware Division of Revenue; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-DES5-006. |
| `de.wh.duty` | [[FACT:de.wh.duty=withhold whenever wages are subject to federal withholding ("If you withhold Federal tax, then you must withhold State tax"); residents and nonresidents]] | 2026-01-01 to open | US-DES5-005 (Delaware General Assembly (Delaware Code Online); A.1, quoted from authority page, confidence high) |  |
| `de.wh.method` | [[FACT:de.wh.method=annualise (daily x300, weekly x52, biweekly x26, semi-monthly x24, monthly x12); less standard deduction; table 0/66/261/741/1,001/2,943.50 + marginal rate; less 110 x exemptions; divide by periods]] | 2025-01-01 to open | US-DES5-006 (Delaware Division of Revenue; A.2, derived arithmetically, confidence high) | Guide table "Effective January 1, 2025", live page. Base amounts re-derived from statute rates. Rounding: none stated; examples round half-up to the cent. |
| `de.wh.personal_credit.per_exemption` | [[FACT:de.wh.personal_credit.per_exemption=110]] USD | 2025-01-01 to open | US-DES5-006 (Delaware Division of Revenue; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-DES5-006. |
| `de.wh.std_deduction.mfj` | [[FACT:de.wh.std_deduction.mfj=6,500]] USD | 2025-01-01 to open | US-DES5-006 (Delaware Division of Revenue; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-DES5-006. |
| `de.wh.std_deduction.single` | [[FACT:de.wh.std_deduction.single=3,250]] USD | 2025-01-01 to open | US-DES5-006 (Delaware Division of Revenue; A.2, derived arithmetically, confidence high) | MFJ [[FACT:de.wh.std_deduction.mfj=6,500]]; MFS [[FACT:de.wh.std_deduction.single=3,250]]. |
| `de.wh.supplemental.method` | [[FACT:de.wh.supplemental.method=with regular wages: one payment; separately: annualized-with minus annualized-without; tips same; deferred compensation recommended 5%]] | 2026-01-01 to open | US-DES5-006 (Delaware Division of Revenue; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-DES5-006. |

## DE.2b Non-resident regime and reciprocity

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `de.nonres.convenience_rule` | [[FACT:de.nonres.convenience_rule=True]] | 2026-01-01 to open | US-DES5-004 (Delaware General Assembly (Delaware Code Online); A.1, quoted from authority page, confidence high) | 30 Del. C. 1124(b)(1)b statutory. Nonresident tax = resident-basis tax less 110 credits x DE-source / DE AGI (1121). Resident credit for other-state tax at assessment only (1111) [US-DES5-003]. No reciprocity [US-DES5-008]. |
| `de.reciprocity.exists` | [[FACT:de.reciprocity.exists=False]] | 2026-01-01 to open | US-DES5-008 (Delaware Division of Revenue; A.3, quoted from authority page, confidence high) |  |

## DE.2c Local wage taxes

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `de.local.wilmington.eit.rate` | [[FACT:de.local.wilmington.eit.rate=1.25]] % | 2023-01-01 to open | US-DEP52-001 (City of Wilmington Department of Finance; A.2, quoted from authority page, confidence high) | Wilmington EIT: residents wherever they earn, nonresidents for work in the City; separate return and reconciliation to City Finance. Regulations rev. 2023 not re-verified; 2026 rate assumed at the 22 Del. C. 901-902 cap. |

Not configured in this release [[GAP:RQ-148]]: Wilmington EIT regulations (rev. 2023) not re-verified; 2026 rate assumed at the statutory [[FACT:de.local.wilmington.eit.rate=1.25]]% cap.

## DE.3 Social insurance: unemployment, disability, paid leave and payroll levies

Industry and employer-size assessments (3350E/F) first payable 2027 [US-DEP9V-001]. The employer training tax of the Blue Collar Jobs Program is not configured in this release [[GAP:RQ-594]]; its rate and wage base are not established from an official source. No SDI/TDI.

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `de.pfml.benefit.weekly_max` | [[FACT:de.pfml.benefit.weekly_max=900]] USD | 2026-01-01 to 2027-12-31 | US-DES5-012 (Delaware General Assembly (Delaware Code Online); A.1, quoted from authority page, confidence high) | 80% of AWW, min 100; CPI-U Philadelphia-Camden-Wilmington after 2027. |
| `de.pfml.employee_share.max_percent` | [[FACT:de.pfml.employee_share.max_percent=50]] % | 2025-01-01 to open | US-DES5-012 (Delaware General Assembly (Delaware Code Online); A.1, quoted from authority page, confidence high) |  |
| `de.pfml.multistate` | [[FACT:de.pfml.multistate=coverage by primary worksite: employees primarily reporting to a DE worksite (3701(6)a), not UI localization]] | 2026-01-01 to open | US-DES5-012 (Delaware General Assembly (Delaware Code Online); A.1, quoted from authority page, confidence high) |  |
| `de.pfml.rate.cap` | [[FACT:de.pfml.rate.cap=1.0]] % | 2027-01-01 to open | US-DES5-012 (Delaware General Assembly (Delaware Code Online); A.1, quoted from authority page, confidence high) |  |
| `de.pfml.rate.family_caregiving` | [[FACT:de.pfml.rate.family_caregiving=0.08]] % | 2025-01-01 to 2026-12-31 | US-DES5-012 (Delaware General Assembly (Delaware Code Online); A.1, quoted from authority page, confidence high) |  |
| `de.pfml.rate.medical` | [[FACT:de.pfml.rate.medical=0.4]] % | 2025-01-01 to 2026-12-31 | US-DES5-012 (Delaware General Assembly (Delaware Code Online); A.1, quoted from authority page, confidence high) |  |
| `de.pfml.rate.parental` | [[FACT:de.pfml.rate.parental=0.32]] % | 2025-01-01 to 2026-12-31 | US-DES5-012 (Delaware General Assembly (Delaware Code Online); A.1, quoted from authority page, confidence high) |  |
| `de.pfml.rate.total` | [[FACT:de.pfml.rate.total=0.8]] % | 2025-01-01 to 2026-12-31 | US-DES5-012 (Delaware General Assembly (Delaware Code Online); A.1, quoted from authority page, confidence high) | 19 Del. C. 3705: medical 0.40 + caregiving 0.08 + parental 0.32; employer may deduct up to 50% of each; FICA wage base; 10-24 employees parental only ([[FACT:de.pfml.rate.parental=0.32]]%); 25+ all three; <=9 exempt. From 2027 DOL-set, cap [[FACT:de.pfml.rate.cap=1.00]]% (unpublished). |
| `de.sui.employee.rate` | [[FACT:de.sui.employee.rate=0]] % | 2026-01-01 to open | US-DER3C-001 (Delaware Code Online; A.1, quoted from authority page, confidence high) | 19 Del. C. 3346: UI assessments payable by the employer shall not be deducted, in whole or in part, from employees' wages. |
| `de.sui.employer.rate.max` | [[FACT:de.sui.employer.rate.max=5.4]] % | 2026-01-01 to 2026-12-31 | US-DES5-022 (Delaware Department of Labor; A.2, second independent authority, confidence high) |  |
| `de.sui.employer.rate.min` | [[FACT:de.sui.employer.rate.min=0.3]] % | 2026-01-01 to 2026-12-31 | US-DES5-022 (Delaware Department of Labor; A.2, second independent authority, confidence high) | Range [[FACT:de.sui.employer.rate.min=0.3]]%-[[FACT:de.sui.employer.rate.max=5.4]]%; whether it excludes the separately billed Op & Tech [[FACT:de.sui.op_tech_assessment.rate=0.2]]% is open. |
| `de.sui.new_employer.rate` | [[FACT:de.sui.new_employer.rate=1.0]] % | 2026-01-01 to 2026-12-31 | US-DES5-022 (Delaware Department of Labor; A.2, second independent authority, confidence high) | Construction new employers and delinquent employers are assigned their own rates by the Department. |
| `de.sui.op_tech_assessment.rate` | [[FACT:de.sui.op_tech_assessment.rate=0.2]] % | 2026-01-01 to 2026-12-31 | US-DEL-003 (Delaware General Assembly; A.1, quoted from authority page, confidence high) | Billed separately by letter from 2026 (Q1 due 2026-08-31, Q2 2026-09-30; Op & Tech Lockbox) [US-DES5-011]; [[FACT:de.sui.op_tech_assessment.rate=0.175]]% from 2027. Separate payable line. |
| `de.sui.op_tech_assessment.rate` | [[FACT:de.sui.op_tech_assessment.rate=0.175]] % | 2027-01-01 to open | US-DEL-003 (Delaware General Assembly; A.1, quoted from authority page, confidence high) |  |
| `de.sui.wage_base` | [[FACT:de.sui.wage_base=14,500]] USD | 2026-01-01 to 2026-12-31 | US-DES5-010 (Delaware General Assembly (Delaware Code Online); A.1, second independent authority, confidence high) | 3302(28)(A)(viii); confirmed by DOL Merit Rate Table [US-DES5-022]. DOL FAQ still printing 18,500/10,500 is stale [US-DES5-011]. Other-state employment counts (3302(28)(A)(x)). |
| `de.sui.wage_base` | [[FACT:de.sui.wage_base=16,500]] USD | 2027-01-01 to open | US-DES5-010 (Delaware General Assembly (Delaware Code Online); A.1, quoted from authority page, confidence high) | Enacted (or FUTA base if higher). |

Not configured in this release [[GAP:RQ-149]]: 2027 Paid Leave contribution rate is DOL-set (cap [[FACT:de.pfml.rate.cap=1.00]]%) and unpublished on 2026-11-02.

Not configured in this release [[GAP:RQ-150]]: Unclear whether the 2026 [[FACT:de.sui.employer.rate.min=0.3]]%-[[FACT:de.sui.employer.rate.max=5.4]]% range excludes the separately billed [[FACT:de.sui.op_tech_assessment.rate=0.2]]% Op & Tech.

## DE.4 Pay statement

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `de.payslip.employer_threshold` | [[FACT:de.payslip.employer_threshold=3]] employees | 2026-01-01 to open | US-DES5-002 (Delaware General Assembly (Delaware Code Online); A.1, quoted from authority page, confidence high) | 1108: employers with MORE than 3 employees: at each payment (check, slip, or electronic if retainable; paper on request): wages due, pay period, each deduction, total hours for hourly. Hire notice of rate and payday. |
| `de.payslip.items` | [[FACT:de.payslip.items=wages due; pay period; total deductions each separately specified; total hours for hourly employees]] | 2026-01-01 to open | US-DES5-002 (Delaware General Assembly (Delaware Code Online); A.1, quoted from authority page, confidence high) |  |

## DE.5 Statutory reporting

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `de.newhire.report_days` | [[FACT:de.newhire.report_days=20]] days | 2026-01-01 to open | US-DES5-005 (Delaware General Assembly (Delaware Code Online); A.1, quoted from authority page, confidence high) | 30 Del. C. 1156A; rehire after 60+ days; fine 25 per failure. |
| `de.report.annual.wth_rec` | [[FACT:de.report.annual.wth_rec=WTH-REC (rev. 02/03/26) replaces W-3, due last day of January with W-2s; e-file if federal e-file; paper only for 10 or fewer forms; EFW2 with DE RS records; no SSN truncation]] | 2026-02-03 to open | US-DES5-009 (Delaware Division of Revenue; A.2, direct artifact inspection, confidence high) |  |
| `de.report.pfml.quarterly` | [[FACT:de.report.pfml.quarterly=Hours & Wage Report and contributions in Delaware LaborFirst]] | 2026-01-01 to open | US-DES5-013 (Delaware Department of Labor; A.2, quoted from authority page, confidence high) |  |
| `de.report.sui.quarterly` | [[FACT:de.report.sui.quarterly=UC-8 tax report + UC-8A wage report, due end of month after quarter; late 1.5%/month interest and 17.50 per late report; Online Employer Services Portal]] | 2026-01-01 to open | US-DES5-011 (Delaware Department of Labor; A.3, quoted from authority page, confidence high) |  |
| `de.report.w2.employee_on_termination_days` | [[FACT:de.report.w2.employee_on_termination_days=30]] days | 2026-01-01 to open | US-DES5-005 (Delaware General Assembly (Delaware Code Online); A.1, quoted from authority page, confidence high) | By Jan 31 or within 30 days of last wage payment on termination (1152). |
| `de.report.w2.paper_max_forms` | [[FACT:de.report.w2.paper_max_forms=10]] forms | 2026-02-03 to open | US-DES5-008 (Delaware Division of Revenue; A.3, quoted from authority page, confidence high) |  |
| `de.report.wh.calendar` | [[FACT:de.report.wh.calendar=quarterly: last day of month after quarter; monthly: 15th; eighth-monthly: 3 working days after periods ending 3rd/7th/11th/15th/19th/22nd/25th/last; tax type 01106]] | 2026-01-01 to open | US-DES5-007 (Delaware Division of Revenue; A.2, direct artifact inspection, confidence high) |  |
| `de.report.wh.frequency` | [[FACT:de.report.wh.frequency=July-June lookback: quarterly up to 4,500; monthly 4,500-25,000; eighth-monthly over 25,000 (statutory, indexed under 30 Del. C. 515; 2026 values not read)]] | 2026-01-01 to open | US-DES5-005 (Delaware General Assembly (Delaware Code Online); A.1, quoted from authority page, confidence medium) |  |

Not configured in this release [[GAP:RQ-151]]: 2026 indexed withholding filing thresholds not read (Guide prints 6,020 / 33,460 undated).

Not configured in this release [[GAP:RQ-152]]: UI separation-notice duty and UC-8A electronic wage-file format not read.

## DE.6 Leave

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `de.leave.sick.state_statute.exists` | [[FACT:de.leave.sick.state_statute.exists=False]] | 2026-01-01 to open | US-DES5-021 (Delaware Department of Labor, Division of Industrial Affairs; A.3, second independent authority, confidence high) | DOL KB: no private-sector paid sick leave or required days off; policies must be made available (1108(3)). |
| `de.pfml.leave.parental_weeks` | [[FACT:de.pfml.leave.parental_weeks=12]] weeks | 2026-01-01 to open | US-DES5-012 (Delaware General Assembly (Delaware Code Online); A.1, quoted from authority page, confidence high) | Medical/caregiving 6 weeks per 24 months; eligibility 12 months and 1,250 hours; employer decides within 5 business days and notifies DOL within 3. |

## DE.7 Termination and final pay

Not configured in this release [[GAP:RQ-592]]: The Delaware UI separation notice and any State plant-closing notice duty are not established from an official source; federal WARN applies (Annex FED.7).

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `de.final_pay.rule` | [[FACT:de.final_pay.rule=later of next regular payday or 3 business days after last day worked (quit, discharge, suspension, layoff); liquidated damages lower of 10%/day or unpaid wages]] | 2026-01-01 to open | US-DES5-002 (Delaware General Assembly (Delaware Code Online); A.1, quoted from authority page, confidence high) | Vacation payout per written policy (1109, within 30 days); death: up to 300 to family without probate (1106). |

## DE.8 Benefits in kind and taxable wages

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `de.pit.conformity` | [[FACT:de.pit.conformity=rolling: DE taxable income = federal AGI as in effect with ch. 11 modifications (1105); federal exclusions flow through; no HSA/125 add-back found]] | 2026-01-01 to open | US-DES5-019 (Delaware General Assembly (Delaware Code Online); A.1, quoted from authority page, confidence medium) |  |

## DE.9 Deductions and garnishments

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `de.deductions.rule` | [[FACT:de.deductions.rule=only if required by law, medical care without employer benefit, or signed authorization for a lawful purpose benefiting the employee (1107)]] | 2026-01-01 to open | US-DES5-002 (Delaware General Assembly (Delaware Code Online); A.1, quoted from authority page, confidence high) |  |
| `de.garn.child_support.arrears_addon_percent` | [[FACT:de.garn.child_support.arrears_addon_percent=20]] % | 2026-01-01 to open | US-DES5-016 (Delaware General Assembly (Delaware Code Online); A.1, quoted from authority page, confidence high) | 13 Del. C. 513: CCPA cap; priority except federal tax liens; arrears up to 20% of current or 20/month; start within 7 days after first payday; EFT/EDI for 50+ employees; fee amount not in statute. |
| `de.garn.creditor.exempt_percent` | [[FACT:de.garn.creditor.exempt_percent=85]] % | 2026-01-01 to open | US-DES5-014 (Delaware General Assembly (Delaware Code Online); A.1, quoted from authority page, confidence high) | 10 Del. C. 4913: max 15% of wages; apply lower of DE 15% of wages and CCPA 25% of disposable; one attachment at a time; not for State fines/taxes. |

Not configured in this release [[GAP:RQ-153]]: 13 Del. C. 513(b)(8)a refers to a State-set fee without stating it.

## DE.10 Collective agreements and prevailing wage

Prevailing wage (public works) is an optional informational flag [US-OWN-009]: this guide documents prevailing-wage laws, thresholds and certified-payroll duties as an overlay, and the payroll build does not produce certified payroll reports.

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `de.prevailing_wage.threshold.alteration` | [[FACT:de.prevailing_wage.threshold.alteration=45,000]] USD | 2026-01-01 to open | US-DES5-015 (Delaware General Assembly (Delaware Code Online); A.1, quoted from authority page, confidence high) |  |
| `de.prevailing_wage.threshold.new_construction` | [[FACT:de.prevailing_wage.threshold.new_construction=500,000]] USD | 2026-01-01 to open | US-DES5-015 (Delaware General Assembly (Delaware Code Online); A.1, quoted from authority page, confidence high) | 29 Del. C. 6960; alteration/repair/renovation/demolition [[FACT:de.prevailing_wage.threshold.alteration=45,000]]; weekly pay and weekly certified payroll to DOL; penalties 1,000-5,000 + treble. |

## DE.11 Indexation

MW, PIT brackets, standard deduction and 110 credit not indexed; SUI base statutory steps; withholding filing thresholds indexed under 30 Del. C. 515 (2026 values not read; Guide prints 6,020/33,460 undated); Paid Leave rate statutory to 2026 then DOL-set; max benefit CPI after 2027.

## DE.12 Payroll data protection and records

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `de.breach.notice_days` | [[FACT:de.breach.notice_days=60]] days | 2026-01-01 to open | US-DES5-020 (Delaware General Assembly (Delaware Code Online); A.1, quoted from authority page, confidence high) | 6 Del. C. ch. 12B: AG notice > 500 residents; 1 year credit monitoring if SSN breached. Full SSN required on W-2 RS and IWO remittances. |
| `de.records.retention_years` | [[FACT:de.records.retention_years=3]] years | 2026-01-01 to open | US-DES5-002 (Delaware General Assembly (Delaware Code Online); A.1, quoted from authority page, confidence high) | 1108(6); 907 adds hours each day and week [US-DES5-001]. |

## DE.13 Live legal change

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `de.live.hb13_hs2.status` | [[FACT:de.live.hb13_hs2.status=draft in House Revenue & Finance Committee since 2025-06-17, NOT enacted; would act at assessment and withholding]] | 2025-06-17 to open | US-DES5-018 (Delaware General Assembly (legis.delaware.gov); A.1, quoted from authority page, confidence high) |  |
| `de.wh.certificate.default_and_copies` | [[FACT:de.wh.certificate.default_and_copies=No certificate: withhold as single with no allowances. Send copies to the Division within 5 working days when an employee claims 14+ allowances, or claims exempt with wages expected above 168.50 a week. Nonresidents: worksheet W-4NR.]] | 2025-01-01 to open | US-DES5-006 (Delaware Division of Revenue; A.2, quoted from authority page, confidence high) | Employer's Guide (live page, sections 13-17). |

Not configured in this release [[GAP:RQ-154]]: Content of 85 Del. Laws c. 301 (amending 1154) and enactment date of the 1103 three-business-day wording not identified.

## DE.14 Authority worked examples (oracle values)

Each example is computed from the statutory parameters listed in this annex and checked against the result published by the authority. Amounts round half-up to the cent unless the line states another rule.

**Example DE-1: single, 1 exemption, annual wages 25,000.00, weekly payroll (Withholding Tax Guide example 1).**

| Line | Calculation | Result |
|---|---|---|
| Annual wages | example input | 25,000.00 |
| Standard deduction (single) | 25,000.00 - [[FACT:de.wh.std_deduction.single=3,250]] | 21,750.00 |
| Bracket 1: 0 to [[FACT:de.pit.bracket.1.ceiling=2,000]] | 0 % (no tax) | 0.00 |
| Bracket 2: 3,000.00 above [[FACT:de.pit.bracket.1.ceiling=2,000]] | 3,000.00 x [[FACT:de.pit.bracket.2.rate=2.2]] % | 66.00 |
| Bracket 3: 5,000.00 above [[FACT:de.pit.bracket.2.ceiling=5,000]] | 5,000.00 x [[FACT:de.pit.bracket.3.rate=3.9]] % | 195.00 |
| Bracket 4: 10,000.00 above [[FACT:de.pit.bracket.3.ceiling=10,000]] | 10,000.00 x [[FACT:de.pit.bracket.4.rate=4.8]] % | 480.00 |
| Bracket 5: 1,750.00 above [[FACT:de.pit.bracket.4.ceiling=20,000]] | 1,750.00 x [[FACT:de.pit.bracket.5.rate=5.2]] % | 91.00 |
| Annual tax before credit | sum of bracket amounts | 832.00 |
| Personal credit | 832.00 - 1 x [[FACT:de.wh.personal_credit.per_exemption=110]] | 722.00 |
| Weekly withholding | 722.00 / 52, half-up to the cent | [[FACT:de.oracle.weekly_25000.withholding=13.88]] |

Computed result = published [[FACT:de.oracle.weekly_25000.withholding=13.88]] (match).

**Example DE-2: supplemental payment 5,000.00 paid separately to an employee earning 500.00 weekly, single, 1 exemption (annualised-with minus annualised-without, per `de.wh.supplemental.method`).**

| Line | Calculation | Result |
|---|---|---|
| Annual regular wages | 500.00 x 52 | 26,000.00 |
| Tax without the bonus | tax on (26,000.00 - [[FACT:de.wh.std_deduction.single=3,250]]) - [[FACT:de.wh.personal_credit.per_exemption=110]] | 774.00 |
| Tax with the bonus | tax on (26,000.00 + 5,000.00 - [[FACT:de.wh.std_deduction.single=3,250]]) - [[FACT:de.wh.personal_credit.per_exemption=110]] | 1,043.625 |
| Withholding on the bonus | 1,043.625 - 774.00 = 269.625, half-up to the cent | [[FACT:de.oracle.supplemental.withholding=269.63]] |

Computed result = published [[FACT:de.oracle.supplemental.withholding=269.63]] (match).

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `de.oracle.supplemental.withholding` | [[FACT:de.oracle.supplemental.withholding=269.63]] USD | 2025-01-01 to open | US-DES5-006 (Delaware Division of Revenue; A.2, derived arithmetically, confidence high) | Guide example 2: 500/week + 5,000 bonus, single, 1 allowance -> 269.625, shown [[FACT:de.oracle.supplemental.withholding=269.63]] (half-up to cent). |
| `de.oracle.weekly_25000.withholding` | [[FACT:de.oracle.weekly_25000.withholding=13.88]] USD | 2025-01-01 to open | US-DES5-006 (Delaware Division of Revenue; A.2, derived arithmetically, confidence high) | Guide example 1: single, 1 allowance, 25,000 annual -> tax 832.00; weekly [[FACT:de.oracle.weekly_25000.withholding=13.88]]. |

## DE.15 Special populations

- Domestic: excluded from state MW (FLSA applies); UI at 1,000 cash/quarter; PIT follows federal (none required) [US-DES5-001, US-DES5-010, US-DES5-005].
- Agricultural: excluded from MW; UI at 20,000/quarter or 10+ workers in 20 weeks [US-DES5-001, US-DES5-010].
- Minors: work permit; no youth subminimum; under-18 camp counselors excluded; child working for parent UI-excluded [US-DES5-017, US-DES5-001, US-DES5-010].
- Tipped: cash wage [[FACT:de.minwage.tipped.cash_wage=2.23]] with make-up; tips employee property; pool cap 15%; supplemental withholding [US-DES5-001, US-DES5-021, US-DES5-006].
- Clergy/religious organisations: UI exclusion per 3302(15)(E); volunteers MW-excluded [US-DES5-010, US-DES5-001].
- Students: own-school and work-study UI-excluded [US-DES5-010].
- NRAs: no DE rule beyond federal [US-DES5-005]. Other-state employees: DE-source wages, convenience rule [US-DES5-004, US-DES5-008].
- Commission agents/direct sellers: UI-excluded [US-DES5-010].
- Government: excluded from ch. 11 and UI (except 3302(14)(B)); US employees MW-excluded; State-plan employees excluded from Paid Leave [US-DES5-002, US-DES5-010, US-DES5-012].
- Family employment: UI-excluded [US-DES5-010, US-DES5-011].
- Small employers: payslip duty only above 3 employees; Paid Leave <10 exempt, 10-24 parental only [US-DES5-002, US-DES5-012].

## DE.16 Language

Paid-leave poster in English, Spanish and any first language of 5%+ of the workforce (19 Del. C. 3710(c)) [US-DEL-001]; bilingual expressly permitted [US-DEP9L-001]; payslip English (US-OWN-006).

## DE.S Sources

The legal basis of each value (legal-basis register id, authority, source tier and verification method) is given in the row that carries it.
