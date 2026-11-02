# Annex FL: Florida

**Layer classification (T1).** T1: no state wage tax; the annex carries unemployment insurance, levies and labour rules only. Source: build manifest tier census, local income tax domain.

**Summary.** T1: no state or local wage tax. Payroll obligations: constitutional minimum wage ([[FACT:fl.minwage.hourly=14.00]] to 2026-09-29, [[FACT:fl.minwage.hourly=15.00]] from 2026-09-30, first CPI-W indexation effective 2028-01-01), tipped cash wage (credit capped at [[FACT:fl.minwage.tip_credit.max=3.02]]), employer-only reemployment tax (base [[FACT:fl.sui.wage_base=7,000]]; [[FACT:fl.sui.employer.rate.min=0.1]]%-[[FACT:fl.sui.employer.rate.max=5.4]]%; new [[FACT:fl.sui.new_employer.rate=2.7]]%; RT-6 with fixed-length or XML upload), new-hire reporting including non-employees paid [[FACT:fl.newhire.nonemployee_threshold=600]]+, E-Verify certification, and garnishment/child-support rules. No general pay-statement statute (labor pools only); local wage/leave mandates pre-empted.

Each parameter row gives its key, the period in force and its legal basis: the legal-basis register row, the authority, the source tier and how the value was verified.

## FL.1 Employment and labour code

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `fl.everify.employer_threshold` | [[FACT:fl.everify.employer_threshold=25]] employees | 2023-07-01 to open | US-FLS5-010 (Florida Senate (2026 Florida Statutes); A.1, quoted from authority page, confidence high) | 448.095: private employers 25+ and all public agencies must use E-Verify within 3 business days; certify on first RT return each year or RT-E Verify [US-FLS5-019]. |
| `fl.local_mandates.preempted` | [[FACT:fl.local_mandates.preempted=True]] | 2024-07-01 to open | US-FLS5-009 (Florida Senate (2026 Florida Statutes); A.1, quoted from authority page, confidence high) | 218.077(2) (ch. 2024-80): no local minimum wage or employment-benefit mandates (sick leave, vacation, holidays) or contractor-wage control; exceptions own employees and direct subsidy recipients. |
| `fl.manual_labor.legal_day_hours` | [[FACT:fl.manual_labor.legal_day_hours=10]] hours | 2026-01-01 to open | US-FLS5-027 (Florida Senate (2026 Florida Statutes); A.1, quoted from authority page, confidence high) | 448.01: extra pay beyond 10 h/day absent written contract; no premium rate fixed. Otherwise FLSA only. |
| `fl.minwage.hourly` | [[FACT:fl.minwage.hourly=14]] USD | 2025-09-30 to 2026-09-29 | US-FLS5-001 (Florida Senate (Florida Constitution); A.1, quoted from authority page, confidence high) | Fla. Const. Art. X s.24(c). Fla. Stat. 448.110 still prints a stale pre-amendment amount (overridden), but controls coverage (FLSA-covered only). |
| `fl.minwage.hourly` | [[FACT:fl.minwage.hourly=15]] USD | 2026-09-30 to 2027-12-31 | US-FLS5-001 (Florida Senate (Florida Constitution); A.1, quoted from authority page, confidence high) | Steps 10.00 (2021) -> [[FACT:fl.minwage.hourly=15.00]]; first CPI-W adjustment calculated 2027-09-30, effective 2028-01-01: no change in 2027. |
| `fl.minwage.pre_suit_notice_days` | [[FACT:fl.minwage.pre_suit_notice_days=15]] days | 2026-01-01 to open | US-FLS5-002 (Florida Senate (2026 Florida Statutes); A.1, quoted from authority page, confidence high) | 448.110; DOR/FloridaCommerce post new rate by 15 Oct, mailed notice by 15 Nov. |
| `fl.minwage.tip_credit.max` | [[FACT:fl.minwage.tip_credit.max=3.02]] USD | 2021-09-30 to open | US-FLS5-001 (Florida Senate (Florida Constitution); A.1, derived arithmetically, confidence high) | Capped at the 2003 FLSA tip credit (2003 federal minimum wage less the federal tipped cash wage [[FACT:fed.tipped.cash_wage.hourly=2.13]]) = [[FACT:fl.minwage.tip_credit.max=3.02]] (federal inputs, FED unit). |
| `fl.minwage.tipped.cash_wage` | [[FACT:fl.minwage.tipped.cash_wage=10.98]] USD | 2025-09-30 to 2026-09-29 | US-FLS5-001 (Florida Senate (Florida Constitution); A.1, derived arithmetically, confidence high) | [[FACT:fl.minwage.hourly=14.00]] - [[FACT:fl.minwage.tip_credit.max=3.02]]. |
| `fl.minwage.tipped.cash_wage` | [[FACT:fl.minwage.tipped.cash_wage=11.98]] USD | 2026-09-30 to 2027-12-31 | US-FLS5-001 (Florida Senate (Florida Constitution); A.1, derived arithmetically, confidence high) | [[FACT:fl.minwage.hourly=15.00]] - [[FACT:fl.minwage.tip_credit.max=3.02]]; poster confirmation open (low risk). |

⚠️ RESEARCH-GAP: [[FACT:fl.minwage.tipped.cash_wage=11.98]] is derived from A.1 but not confirmed on the FloridaCommerce 2026 poster (access gap). (open item `fl.minwage.tipped.poster_confirmation`, non-blocking; would close it: FloridaCommerce 2026 minimum wage poster.)

## FL.2 State income tax withholding

No state income tax on natural persons (Fla. Const. Art. VII s.5(a)) [US-FL-001]; DOR tax list has no personal income or withholding tax [US-FL-002, US-FLL-003]. Not applicable: state withholding method, W-4, supplemental, rounding, state W-2, reciprocity, resident/nonresident. Florida residents working elsewhere follow the work state (MULTI).

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `fl.pit.exists` | [[FACT:fl.pit.exists=False]] | 2026-01-01 to open | US-FL-001 (Florida Senate; A.1, quoted from authority page, confidence high) |  |

## FL.2b Non-resident regime and reciprocity

No jurisdiction-specific item was recorded in the research for this domain.

## FL.2c Local wage taxes

None [US-FLL-003].

## FL.3 Social insurance (unemployment, disability, paid leave, levies)

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `fl.sdi_pfml.exists` | [[FACT:fl.sdi_pfml.exists=False]] | 2026-01-01 to open | US-FLP52-001 (Florida Senate (2025 Florida Statutes); A.1, quoted from authority page, confidence high) | Title XXXI has no SDI/TDI/PFML chapter; no state WARN. Workers comp employer-funded, employee contribution void (440.21) [US-FLP52-002]. |
| `fl.sui.employee.rate` | [[FACT:fl.sui.employee.rate=0]] % | 2026-01-01 to open | US-FLS5-004 (Florida Senate (2026 Florida Statutes); A.1, quoted from authority page, confidence high) | 443.131(1): may not be deducted from wages. |
| `fl.sui.employer.rate.max` | [[FACT:fl.sui.employer.rate.max=5.4]] % | 2026-01-01 to 2026-12-31 | US-FLS5-018 (Florida Department of Revenue; A.2, quoted from authority page, confidence high) | = 378 per employee; +1 point for short-time-compensation employers. |
| `fl.sui.employer.rate.min` | [[FACT:fl.sui.employer.rate.min=0.1]] % | 2026-01-01 to 2026-12-31 | US-FLS5-018 (Florida Department of Revenue; A.2, quoted from authority page, confidence high) | = 7 per employee. |
| `fl.sui.liability_threshold.quarterly_wages` | [[FACT:fl.sui.liability_threshold.quarterly_wages=1,500]] USD | 2026-01-01 to open | US-FLS5-020 (Florida Department of Revenue; A.3, direct artifact inspection, confidence medium) | Or 1 employee in 20 weeks or FUTA liability; domestic 1,000 in a quarter. |
| `fl.sui.new_employer.rate` | [[FACT:fl.sui.new_employer.rate=2.7]] % | 2026-01-01 to open | US-FLS5-004 (Florida Senate (2026 Florida Statutes); A.1, quoted from authority page, confidence high) | While chargeable < 8 quarters (statute); DOR: until reported 10 quarters. |
| `fl.sui.rounding` | [[FACT:fl.sui.rounding=contribution fraction under half a cent dropped; half a cent or more rounds up to 1 cent]] | 2026-01-01 to open | US-FLS5-004 (Florida Senate (2026 Florida Statutes); A.1, quoted from authority page, confidence high) |  |
| `fl.sui.wage_base` | [[FACT:fl.sui.wage_base=7,000]] USD | 2015-01-01 to open | US-FLS5-003 (Florida Senate (2026 Florida Statutes); A.1, second independent authority, confidence high) | Fixed in statute; successor may count predecessor wages; out-of-state wages credited via RT-6NF [US-FLS5-020, US-FLS5-018]. |

⚠️ RESEARCH-GAP: 443.1217(2)(f) excludes payments to a 401(a) trust and carves out salary reduction only for 403(b); ambiguous against FUTA 3306(r); DOR guide silent. (open item `fl.sui.wages.401k_deferral`, blocking; would close it: A DOR TIP or an answer from DOR e-vendor / Reemployment Tax FAQ.)

## FL.4 Pay statement

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `fl.payslip.general_statute.exists` | [[FACT:fl.payslip.general_statute.exists=False]] | 2026-01-01 to open | US-FLL-002 (Florida Senate (Online Sunshine); A.1, quoted from authority page, confidence high) | Only labor pools: itemised deductions at each payment (electronic on request) and annual earnings summary by 1 February (448.24(2)(g),(h)). |

## FL.5 Statutory reporting

Other: BLS-3020 multiple worksite; RT-6EW; RT-6NF; RT-7 annual for domestic-only employers (due 1 Jan, late after 31 Jan). Registration DR-1 online. DR-835 POA / RTS-9 agent [US-FL-005].

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `fl.newhire.nonemployee_threshold` | [[FACT:fl.newhire.nonemployee_threshold=600]] USD | 2026-01-01 to open | US-FLS5-008 (Florida Senate (2026 Florida Statutes); A.1, quoted from authority page, confidence high) |  |
| `fl.newhire.report_days` | [[FACT:fl.newhire.report_days=20]] days | 2026-01-01 to open | US-FLS5-008 (Florida Senate (2026 Florida Statutes); A.1, quoted from authority page, confidence high) | 409.2576; DOB optional; also NON-EMPLOYEES paid [[FACT:fl.newhire.nonemployee_threshold=600]]+ in a year within 20 days. |
| `fl.report.sui.efile_threshold_employees` | [[FACT:fl.report.sui.efile_threshold_employees=10]] employees | 2026-01-01 to open | US-FLS5-006 (Florida Senate (2026 Florida Statutes); A.1, quoted from authority page, confidence high) | 10+ employees in any quarter of prior state fiscal year must e-file/e-pay; non-electronic report 25 + 1/employee max 300; erroneous report greater of 50 or 10% max 300 [US-FLS5-024]; ITIN not accepted. |
| `fl.report.sui.flat_file` | [[FACT:fl.report.sui.flat_file=Flat File Web Import v7 (Dec 2023): fixed-length records 00 Header, 01 Employer, 02 Employee, 03 Totals, 99 Trailer; 2 implied decimals; zip refused]] | 2023-12-01 to open | US-FLS5-022 (Florida Department of Revenue; A.2, direct artifact inspection, confidence high) |  |
| `fl.report.sui.rt6` | [[FACT:fl.report.sui.rt6=RT-6 (R. 07/23) due 30 Apr, 31 Jul, 31 Oct, 31 Jan (next business day); zero report required; e-payment by 5 pm ET business day before; lines 1 covered employees (12th), 2 gross, 3 excess over 7,000, 4 taxable, 5 tax; wage detail name/SSN/gross/taxable; corrections RT-8A]] | 2023-07-01 to open | US-FLS5-021 (Florida Department of Revenue; A.2, direct artifact inspection, confidence high) |  |
| `fl.report.sui.xml` | [[FACT:fl.report.sui.xml=FL_RT_XML_Schemas_v2026 1.0: 9 XSD in IRS efile envelope; required above 20,000 employee records; RT-6 sample validates (lxml)]] | 2026-01-01 to open | US-FLS5-023 (Florida Department of Revenue (Software Developer Information and Specifications); A.2, direct artifact inspection, confidence high) |  |
| `fl.report.sui.xml_required_records` | [[FACT:fl.report.sui.xml_required_records=20,000]] records | 2026-01-01 to open | US-FLS5-023 (Florida Department of Revenue (Software Developer Information and Specifications); A.2, direct artifact inspection, confidence high) |  |

⚠️ RESEARCH-GAP: RT_changes.xlsx inside the RT XML package not read. (open item `fl.report.sui.xml_changes_2026`, non-blocking; would close it: Read RT_changes.xlsx in FL_DOR_flRtXmlPkg_2026-11-02.zip.)

## FL.6 Leave

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `fl.leave.domestic_violence.days` | [[FACT:fl.leave.domestic_violence.days=3]] working days | 2026-01-01 to open | US-FLS5-014 (Florida Senate (2026 Florida Statutes); A.1, quoted from authority page, confidence high) | Employers 50+, employees 3+ months; up to 3 working days per 12 months, paid or unpaid at employer choice. |
| `fl.leave.sick.state_statute.exists` | [[FACT:fl.leave.sick.state_statute.exists=False]] | 2024-07-01 to open | US-FLS5-009 (Florida Senate (2026 Florida Statutes); A.1, quoted from authority page, confidence high) | None at state level; local mandates pre-empted. |

## FL.7 Termination and final pay

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `fl.final_pay.state_statute.exists` | [[FACT:fl.final_pay.state_statute.exists=False]] | 2026-01-01 to open | US-FLS5-016 (Florida Senate (2026 Florida Statutes); A.1, quoted from authority page, confidence medium) | No final-pay timing or vacation payout statute; prevailing party fees in wage action (448.08). |

⚠️ RESEARCH-GAP: 443.151(1) defers to rules; whether a FloridaCommerce rule requires a separation form was not read. (open item `fl.termination.separation_notice`, non-blocking; would close it: Rule chapters 73B-10/73B-11 F.A.C. on flrules.org.)

## FL.8 Benefits in kind and taxable wages

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `fl.sui.wages.taxable_items` | [[FACT:fl.sui.wages.taxable_items=personal-use cars, non-convenience meals and lodging, group legal, golden parachutes, excess discounts, below-market loan interest, reported tips]] | 2026-01-01 to open | US-FLS5-003 (Florida Senate (2026 Florida Statutes); A.1, second independent authority, confidence high) | 443.1217(2)(b)-(g); excluded: sickness/accident/medical/death plan payments, employer-paid employee FICA, convenience meals/lodging, 401(a)/403(a)/SEP/403(b) non-salary-reduction/3121(v)(3). 401(k) deferral treatment open. |

## FL.9 Deductions and garnishments

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `fl.garn.child_support.employer_fee.first` | [[FACT:fl.garn.child_support.employer_fee.first=5]] USD | 2026-01-01 to open | US-FLS5-013 (Florida Senate (2026 Florida Statutes); A.1, quoted from authority page, confidence high) | 61.1301: 5 first deduction, 2 each after; start first pay date > 14 days after service; remit within 2 days after pay date; arrears +20%; termination notice penalty 250/500. |
| `fl.garn.child_support.employer_fee.subsequent` | [[FACT:fl.garn.child_support.employer_fee.subsequent=2]] USD | 2026-01-01 to open | US-FLS5-013 (Florida Senate (2026 Florida Statutes); A.1, quoted from authority page, confidence high) |  |
| `fl.garn.child_support.remit_days` | [[FACT:fl.garn.child_support.remit_days=2]] days | 2026-01-01 to open | US-FLS5-013 (Florida Senate (2026 Florida Statutes); A.1, quoted from authority page, confidence high) |  |
| `fl.garn.head_of_family.weekly_exempt` | [[FACT:fl.garn.head_of_family.weekly_exempt=750]] USD | 2026-01-01 to open | US-FLS5-012 (Florida Senate (2026 Florida Statutes); A.1, quoted from authority page, confidence high) | 222.11: head of family disposable earnings up to [[FACT:fl.garn.head_of_family.weekly_exempt=750]]/week fully exempt; above only with separate written waiver up to CCPA; others CCPA. Not indexed. |

## FL.10 Collective agreements and prevailing wage

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `fl.prevailing_wage.state_law.exists` | [[FACT:fl.prevailing_wage.state_law.exists=False]] | 2026-01-01 to open | US-FLP52-003 (Florida Senate; A.1, quoted from authority page, confidence high) | Ch. 255 scanned in full; local procurement wage control barred (218.077(2)(b)-(c)). |

## FL.11 Indexation

MW fixed steps to [[FACT:fl.minwage.hourly=15.00]] (2026-09-30); CPI-W from 2028-01-01; UI base not indexed; UI rates yearly (RT-20); garnishment [[FACT:fl.garn.head_of_family.weekly_exempt=750]] not indexed.

## FL.12 Payroll data protection and records

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `fl.breach.notice_days` | [[FACT:fl.breach.notice_days=30]] days | 2026-01-01 to open | US-FLS5-017 (Florida Senate (2026 Florida Statutes); A.1, quoted from authority page, confidence high) | 501.171: notice to Dept. of Legal Affairs for 500+ Floridians within 30 days (+15 for good cause). Amended by ch. 2026-52 s.9 (substance not read). |

## FL.13 Live legal change

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `fl.live.minwage_2026_09_30` | [[FACT:fl.live.minwage_2026_09_30=minimum wage 15.00 and tipped 11.98 from 2026-09-30, in force]] | 2026-09-30 to open | US-FLS5-001 (Florida Senate (Florida Constitution); A.1, quoted from authority page, confidence high) |  |

⚠️ RESEARCH-GAP: 501.171 was amended by ch. 2026-52 s.9; substance not read. (open item `fl.live.ch_2026_52`, non-blocking; would close it: Laws of Florida ch. 2026-52 on laws.flrules.org.)

⚠️ RESEARCH-GAP: Full sweep of Laws of Florida 2026 and DOR TIPs 2026 not run within budget. (open item `fl.live.bulletin_sweep`, non-blocking; would close it: Laws of Florida 2026 index and DOR Tax Information Publications 2026.)

## FL.14 Worked examples

No withholding oracle (no wage tax). UI: Line 4 x rate with half-cent rounding; RT-800002 p.9 worked examples (successor wages; NY to FL transfer) and the 4 RT XML test cases [US-FLS5-020, US-FLS5-023].

## FL.15 Special populations

- Domestic: UI at 1,000 cash/quarter; RT-7 annual option; minor hours limits not applicable; casual private-residence labor not "employee" for E-Verify [US-FLS5-005, US-FLS5-004].
- Agricultural: UI at 10,000 cash/quarter or 5+ workers in 20 weeks; crew-leader rules [US-FLS5-005].
- Minors: 450.081 hours (15 and under 3 h school days/15 h week; 16-17 8 h/30 h in session); no subminimum; newspaper delivery under 18 UI-exempt [US-FLS5-011, US-FLS5-005].
- Tipped: credit [[FACT:fl.minwage.tip_credit.max=3.02]]; [[FACT:fl.minwage.tipped.cash_wage=11.98]] from 2026-09-30; reported tips are UI wages [US-FLS5-001, US-FLS5-020, US-FLS5-021].
- Clergy: churches/ministers UI-exempt; other 501(c)(3) covered at 4+ in 20 weeks [US-FLS5-005, US-FLS5-020].
- Students: own-school, co-op, student nurses/interns, F/J purpose-related work UI-exempt [US-FLS5-005, US-FLS5-020, US-FLS5-025].
- NRAs: no PIT; UI taxable except F/J; ITIN invalid on RT-6 [US-FLS5-025, US-FLS5-024].
- Statutory employees: agent/commission drivers and traveling salespersons UI-covered; commission insurance/real-estate (and barbers) exempt [US-FLS5-005, US-FLS5-020].
- Government: UI covers public employers with exceptions; E-Verify mandatory; own-employee wage autonomy [US-FLS5-005, US-FLS5-010, US-FLS5-009].
- Corporate officers covered; family employment exempt except in corporations [US-FLS5-005, US-FLS5-020].
- Labor pools: 448.24 itemised statement and annual summary [US-FLL-002].

## FL.16 Language of employee documents

Minimum-wage poster in English and Spanish (448.109(3)(a)) [US-FLL-001]; RT-83 poster with Spanish version RT-83SP [US-FLS5-026]; payslip English (US-OWN-006). FL postings page unreadable.
