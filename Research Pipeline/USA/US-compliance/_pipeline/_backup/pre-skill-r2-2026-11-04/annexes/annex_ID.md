# Annex ID: Idaho


**Layer classification (T3).** T3: separate state withholding calculation and state return; no local layer, or a local layer piggybacked on the state return. Source: build manifest tier census, local income tax domain.

**Summary.** Minimum wage [[FACT:id.minwage.hourly=7.25]] tracking federal; tipped cash [[FACT:id.minwage.tipped.cash_wage=3.35]]; opportunity wage [[FACT:id.minwage.opportunity_wage=4.25]]; local minimum wages barred; FLSA overtime. Flat 5.3% PIT; withholding tables changed MID-YEAR: zero bracket 15,000/30,000 to 2026-07-22, [[FACT:id.wh.zero_bracket.single.annual=16,100]]/[[FACT:id.wh.zero_bracket.married.annual=32,200]] from 2026-07-23 (prospective, no catch-up); allowance value 0; percentage method rounds to whole dollar; supplemental flat 5.3%; nonresident threshold 1,000; no reciprocity, no local tax. SUI base [[FACT:id.sui.wage_base=58,300]], new [[FACT:id.sui.new_employer.rate=1.000]]%. Only a deductions statement is mandated. Final pay earlier of next payday or 10 days. Oracle: STC examples 31 / 20.

Each parameter row gives its key, the period in force and its legal basis: the legal-basis register row, the authority, the source tier and how the value was verified.

## ID.1 Employment and labour code

Exclusions (44-1504) [US-IDS5-003]: EAP/outside sales; domestic; nonprofit camp seasonal; under-16 part-time <= 4 h/day; under-18 family; agricultural cases. Government employers outside state MW law (FLSA only). Overtime: no state rule (ch. 44-15 index; IDOL guide) [US-IDS5-025]. Hire notice of rate/payday on request; reduction notice before work (45-610) [US-IDS5-006].

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `id.local_minwage.preempted` | [[FACT:id.local_minwage.preempted=True]] | 2026-01-01 to open | US-IDS5-001 (Idaho Legislature (Wayback id_ 20261010193220); A.1, direct artifact inspection, confidence high) | 44-1502(4); H0812 (2026) not enacted. |
| `id.minwage.hourly` | [[FACT:id.minwage.hourly=7.25]] USD | 2009-07-24 to open | US-IDS5-001 (Idaho Legislature (Wayback id_ 20261010193220); A.1, direct artifact inspection, confidence high) | 44-1502(1): conforms to and tracks the federal minimum; not indexed; H0813 (2026) filed only [US-IDS5-024]. |
| `id.minwage.opportunity_wage` | [[FACT:id.minwage.opportunity_wage=4.25]] USD | 2026-01-01 to open | US-IDS5-001 (Idaho Legislature (Wayback id_ 20261010193220); A.1, direct artifact inspection, confidence high) | Under 20, first 90 consecutive calendar days (44-1502(3)). |
| `id.minwage.tipped.cash_wage` | [[FACT:id.minwage.tipped.cash_wage=3.35]] USD | 2026-01-01 to open | US-IDS5-001 (Idaho Legislature (Wayback id_ 20261010193220); A.1, direct artifact inspection, confidence high) | Tip credit up to 3.90; employer makes up shortfall; tipped = > 30/month tips [US-IDS5-002]. |
| `id.pay_frequency.rule` | [[FACT:id.pay_frequency.rule=at least once per calendar month on designated paydays; period ends <= 15 days before payday; nonworkday payday moves earlier; pattern of late pay up to 500 per period (45-608)]] | 2026-01-01 to open | US-IDS5-004 (Idaho Legislature (Wayback id_ 20260516075513); A.1, direct artifact inspection, confidence high) |  |
| `id.payment.method` | [[FACT:id.payment.method=lawful money or checks cashable without charge; direct deposit only with voluntary authorisation to account of choice, revocable (45-608); paycards not addressed]] | 2026-01-01 to open | US-IDS5-004 (Idaho Legislature (Wayback id_ 20260516075513); A.1, direct artifact inspection, confidence high) |  |

Not configured in this release [[GAP:RQ-188]]: 45-608 does not address paycards.

## ID.2 Income tax withholding

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `id.pit.rate.flat` | [[FACT:id.pit.rate.flat=5.3]] % | 2025-01-01 to open | US-IDS5-007 (Idaho Legislature (Wayback id_ 20261025225240); A.1, direct artifact inspection, confidence high) | 63-3024 (2025 ch. 13, H 40); applies above CPI-indexed 2,500/5,000; no 2026 amendment; H0589/H0782/H0605 not enacted. |
| `id.wh.allowance.value` | [[FACT:id.wh.allowance.value=0]] USD | 2026-01-01 to open | US-IDS5-008 (Idaho State Tax Commission (Wayback id_ 20261010115435); A.2, direct artifact inspection, confidence medium) | Child Tax Credit sunset (63-3029L); S1450 (2026) not enacted. |
| `id.wh.certificate` | [[FACT:id.wh.certificate=federal W-4 required; Form ID W-4 (EFO00307) strongly encouraged: A Single/HoH, B Married, C Married at single rate; allowances = children 16 or under (+2 HoH)]] | 2025-04-28 to open | US-IDS5-013 (Idaho State Tax Commission (Wayback id_ 20250602053713); A.2, direct artifact inspection, confidence medium) | [partial row] Partial row: 2025 edition; 2026 edition not captured. |
| `id.wh.method` | [[FACT:id.wh.method=percentage computation (rounded to nearest whole dollar), annualized wage, or wage bracket (EPB00745); allowance value 0 (Idaho CTC sunset)]] | 2026-01-01 to open | US-IDS5-008 (Idaho State Tax Commission (Wayback id_ 20261010115435); A.2, direct artifact inspection, confidence high) | Tables apply prospectively, no retro catch-up. |
| `id.wh.rounding` | [[FACT:id.wh.rounding=nearest whole dollar]] | 2026-01-01 to open | US-IDS5-008 (Idaho State Tax Commission (Wayback id_ 20261010115435); A.2, direct artifact inspection, confidence high) |  |
| `id.wh.supplemental.rate` | [[FACT:id.wh.supplemental.rate=5.3]] % | 2026-01-01 to open | US-IDS5-008 (Idaho State Tax Commission (Wayback id_ 20261010115435); A.2, direct artifact inspection, confidence high) | Aggregate or flat [[FACT:id.wh.supplemental.rate=5.3]]% on separately issued payment. |
| `id.wh.zero_bracket.married.annual` | [[FACT:id.wh.zero_bracket.married.annual=30,000]] USD | 2025-04-28 to 2026-07-22 | US-IDS5-012 (Idaho State Tax Commission (Wayback id_ 20260120032653); A.2, derived arithmetically, confidence high) | EPB00744 edition 04-28-2025: governs 2026 payrolls through 2026-07-22 (closed period; replaced prospectively by the 07-23-2026 edition, US-IDS5-011). |
| `id.wh.zero_bracket.married.annual` | [[FACT:id.wh.zero_bracket.married.annual=32,200]] USD | 2026-07-23 to open | US-IDS5-011 (Idaho State Tax Commission (Wayback id_ 20261007091254); A.2, derived arithmetically, confidence high) | Per-period married 2,683 / 1,342 / 1,238 / [[FACT:id.wh.zero_bracket.single.biweekly=619]] / 124. |
| `id.wh.zero_bracket.single.annual` | [[FACT:id.wh.zero_bracket.single.annual=15,000]] USD | 2025-04-28 to 2026-07-22 | US-IDS5-012 (Idaho State Tax Commission (Wayback id_ 20260120032653); A.2, derived arithmetically, confidence high) | EPB00744 edition 04-28-2025: governs 2026 payrolls through 2026-07-22 (closed period; replaced prospectively by the 07-23-2026 edition, US-IDS5-011). |
| `id.wh.zero_bracket.single.annual` | [[FACT:id.wh.zero_bracket.single.annual=16,100]] USD | 2026-07-23 to open | US-IDS5-011 (Idaho State Tax Commission (Wayback id_ 20261007091254); A.2, derived arithmetically, confidence high) | EPB00744 ed. 07-23-2026; per-period = annual / 12/24/26/52/260 rounded to dollar: monthly 1,342, semimonthly 671, biweekly [[FACT:id.wh.zero_bracket.single.biweekly=619]], weekly 310, daily 62. Equals 2026 federal standard deduction (observation) [US-FEDS5-010]. |
| `id.wh.zero_bracket.single.biweekly` | [[FACT:id.wh.zero_bracket.single.biweekly=577]] USD | 2025-04-28 to 2026-07-22 | US-IDS5-012 (Idaho State Tax Commission (Wayback id_ 20260120032653); A.2, derived arithmetically, confidence high) | EPB00744 edition 04-28-2025: governs 2026 payrolls through 2026-07-22 (closed period; replaced prospectively by the 07-23-2026 edition, US-IDS5-011). |
| `id.wh.zero_bracket.single.biweekly` | [[FACT:id.wh.zero_bracket.single.biweekly=619]] USD | 2026-07-23 to open | US-IDS5-011 (Idaho State Tax Commission (Wayback id_ 20261007091254); A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-IDS5-011. |

Not yet published [[GAP:RQ-189]]: Form ID W-4 2026 edition not captured (CDX lists to 04-28-2025); NRA add-ons and multiple-jobs factor (2025: [[FACT:id.wh.zero_bracket.single.annual=15,000]] and 3,868) may have changed.

Not configured in this release [[GAP:RQ-190]]: STC computing page married example uses "over 32,000", matching neither EPB00744 edition.

## ID.2b Non-resident regime and reciprocity

No reciprocity [US-IDB5-401]; no local wage tax [US-IDP52-003]. Interstate carrier staff withheld for state of residence; enrolled tribal members on reservation not withheld.

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `id.nonres.withholding_threshold` | [[FACT:id.nonres.withholding_threshold=1,000]] USD | 2026-01-01 to open | US-IDS5-020 (Idaho State Tax Commission (Wayback id_ 20260514201525; page last updated 2022-08-30); A.2, direct artifact inspection, confidence high) | Withhold once nonresident earns > [[FACT:id.nonres.withholding_threshold=1,000]] in Idaho in the calendar year; all Idaho wages on W-2; residents working elsewhere: Idaho withholding optional; out-of-state employers withhold for employees physically in Idaho. |

## ID.2c Local wage taxes

No jurisdiction-specific item was recorded in the research for this domain.

## ID.3 Social insurance: unemployment, disability, paid leave and payroll levies

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `id.pfml.exists` | [[FACT:id.pfml.exists=False]] | 2026-01-01 to open | US-IDS5-018 (Idaho Legislature (Wayback id_ 20260216102311); A.1, direct artifact inspection, confidence high) | 2022 H0447 died in committee [US-KYR3-003]. |
| `id.sui.coverage` | [[FACT:id.sui.coverage=general 1,500/quarter or 20 weeks; agricultural 20,000 cash/quarter or 10 workers on 20 days (H-2A counted, not taxed); domestic 1,000 cash/quarter; government and nonprofits covered; LLC-as-corporation members = officers; officer opt-out before March 31]] | 2026-01-01 to open | US-IDS5-022 (Idaho Legislature (Wayback id_ 20260419115712); A.1, direct artifact inspection, confidence high) |  |
| `id.sui.employer.rate.range` | [[FACT:id.sui.employer.rate.range=positive classes 0.208%-0.694%; deficit classes 1.250%-5.400%]] | 2026-01-01 to 2026-12-31 | US-IDP52-004 (Idaho Department of Labor; A.2, quoted from authority page, confidence high) |  |
| `id.sui.new_employer.admin_component.rate` | [[FACT:id.sui.new_employer.admin_component.rate=0.0]] % | 2026-01-01 to 2026-12-31 | US-IDB5-402 (Idaho Department of Labor; A.2, quoted from authority page, confidence high) | Standard (new employer) rate [[FACT:id.sui.new_employer.rate=1.000]]%: administrative rate component 0.00000% (IDOL Rate Class Array effective 01/01/2026, row "Standard"). |
| `id.sui.new_employer.rate` | [[FACT:id.sui.new_employer.rate=1.0]] % | 2026-01-01 to 2026-12-31 | US-IDP52-004 (Idaho Department of Labor; A.2, quoted from authority page, confidence high) | Standard: [[FACT:id.sui.new_employer.rate=1.000]]% = [[FACT:id.sui.new_employer.ui_component.rate=0.97000]]% UI + [[FACT:id.sui.new_employer.admin_component.rate=0.00000]]% admin + [[FACT:id.sui.workforce_development.rate=0.03000]]% workforce development; standard rate for at least the first six calendar quarters [US-IDS5-021]. IDOL Tax Handbook p.21: "All new employers except cost-reimbursement employers begin with the same standard unemployment insurance tax rate for at least the first six calendar quarters." |
| `id.sui.new_employer.ui_component.rate` | [[FACT:id.sui.new_employer.ui_component.rate=0.97]] % | 2026-01-01 to 2026-12-31 | US-IDB5-402 (Idaho Department of Labor; A.2, quoted from authority page, confidence high) | Standard (new employer) rate [[FACT:id.sui.new_employer.rate=1.000]]%: UI contribution rate component [[FACT:id.sui.new_employer.ui_component.rate=0.97000]]% (IDOL Rate Class Array effective 01/01/2026, row "Standard"). |
| `id.sui.wage_base` | [[FACT:id.sui.wage_base=58,300]] USD | 2026-01-01 to 2026-12-31 | US-IDB5-402 (ID official authority; A.2, quoted from authority page, confidence medium) | 72-1350: AAW of penultimate year rounded to 100 or FUTA if higher [US-IDS5-014]; not re-derived from the average annual wage; figure rests on the 2026 rate array (US-IDP52-004). |
| `id.sui.workforce_development.rate` | [[FACT:id.sui.workforce_development.rate=0.03]] % | 2026-01-01 to 2026-12-31 | US-IDB5-402 (ID official authority; A.2, quoted from authority page, confidence high) | Inside the UI rate; no other levy. |

Not configured in this release [[GAP:RQ-191]]: 2027 SUI base/rate array unpublished; 2024 AAW needed to derive [[FACT:id.sui.wage_base=58,300]] not obtained.

## ID.4 Pay statement

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `id.payslip.required_content` | [[FACT:id.payslip.required_content=written statement of deductions for each pay period in which deductions are made (45-609(2)); no full itemised statute]] | 2026-01-01 to open | US-IDS5-025 (Idaho Department of Labor (Wayback id_ 20260406155804); A.3, direct artifact inspection, confidence medium) |  |

## ID.5 Statutory reporting

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `id.newhire.report_days` | [[FACT:id.newhire.report_days=20]] days | 2026-01-01 to open | US-IDS5-015 (Idaho Legislature (Wayback id_ 20260222181234); A.1, direct artifact inspection, confidence high) | 72-1604: employee name/address/SSN; employer name/address/FEIN; Idaho UI account; hire date; multistate flag. |
| `id.report.annual.form967` | [[FACT:id.report.annual.form967=Form 967 + W-2s due last day of January (1099s with ID withholding last day of February); EFW2 + Idaho state records via TAP (valid EFW2 generates 967); penalty 2/month per missing W-2 min 10 max 2,000; amounts to nearest dollar]] | 2026-01-01 to open | US-IDS5-010 (Idaho State Tax Commission (Wayback id_ 20260214041722 and 20260514224310); A.2, direct artifact inspection, confidence high) |  |
| `id.report.sui.tx20` | [[FACT:id.report.sui.tx20=TX20 + TX26 (TX20C amendments) due last day of month after quarter (72-1311), no grace; online Employer Portal mandatory; zero reports required]] | 2026-01-01 to open | US-IDS5-021 (Idaho Department of Labor (Wayback id_ 20260113182918); A.3, direct artifact inspection, confidence high) |  |
| `id.report.wh.form910` | [[FACT:id.report.wh.form910=Form 910 in TAP: semimonthly if >= 25,000/month or >= 300,000/12 months (20th / 5th); monthly < 25,000 and > 750/quarter (20th); quarterly <= 750/quarter; annual < 750/yr (last day of Jan); zero return required; cycle fixed for the year (changes by Nov 15)]] | 2026-01-01 to open | US-IDS5-009 (Idaho State Tax Commission (Wayback id_ 20260618173701 and 20260412130751); A.2, direct artifact inspection, confidence high) |  |

Not configured in this release [[GAP:RQ-192]]: Idaho EFW2 RS/RV state-record spec not read.

## ID.6 Leave

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `id.leave.paid_mandate.exists` | [[FACT:id.leave.paid_mandate.exists=False]] | 2026-01-01 to open | US-IDS5-025 (Idaho Department of Labor (Wayback id_ 20260406155804); A.3, direct artifact inspection, confidence high) | H0641 (2026) sick leave FAILED [US-IDS5-024]; no PFML. |

Not configured in this release [[GAP:RQ-193]]: Search lead 44-2701 was the non-compete chapter (secondary-source error); no pre-emption statute or city leave ordinance located.

Not configured in this release [[GAP:RQ-194]]: H0544 (2026) text not read; reach to private employers unknown.

## ID.7 Termination and final pay

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `id.final_pay.max_days` | [[FACT:id.final_pay.max_days=10]] days | 2026-01-01 to open | US-IDS5-005 (Idaho Legislature (Wayback id_ 20260831052422); A.1, direct artifact inspection, confidence high) |  |
| `id.final_pay.rule` | [[FACT:id.final_pay.rule=earlier of next regular payday or 10 days excluding weekends/holidays; within 48 hours on written request; piece/commission: MW for last period then balance next payday (45-606)]] | 2026-01-01 to open | US-IDS5-005 (Idaho Legislature (Wayback id_ 20260831052422); A.1, direct artifact inspection, confidence high) | No vacation-payout statute (agreement); no discharge notice or separation notice required. |

Not configured in this release [[GAP:RQ-195]]: Whether accrued vacation is "wages" under 45-601(7) when policy is silent.

## ID.8 Benefits in kind and taxable wages

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `id.pit.conformity_date` | [[FACT:id.pit.conformity_date=2026-01-01]] | 2026-01-01 to open | US-IDS5-019 (Idaho Legislature (Wayback id_ 20260906190743); A.1, direct artifact inspection, confidence high) | Static conformity (2026 ch. 1, H0559); federal wage exclusions carry over; UI wages include board/lodging; domestic UI on noncash too. |

## ID.9 Deductions and garnishments

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `id.garn.child_support.cap_percent` | [[FACT:id.garn.child_support.cap_percent=50]] % | 2025-02-06 to open | US-IDS5-017 (Idaho Legislature (Wayback id_ 20250206071607); A.1, direct artifact inspection, confidence high) | 32-1210: total cap 50% of disposable incl. arrears and fee (stricter than CCPA); remit within 7 business days; answer court order within 10 days; current first then pro rata. |
| `id.garn.child_support.employer_fee` | [[FACT:id.garn.child_support.employer_fee=5]] USD | 2025-02-06 to open | US-IDS5-017 (Idaho Legislature (Wayback id_ 20250206071607); A.1, direct artifact inspection, confidence high) |  |
| `id.garn.creditor.max_percent` | [[FACT:id.garn.creditor.max_percent=25]] % | 2026-01-01 to open | US-IDS5-016 (Idaho Legislature (Wayback id_ 20260311064454); A.1, direct artifact inspection, confidence high) | 11-207 mirrors CCPA: lesser of [[FACT:id.garn.creditor.max_percent=25]]% or excess over 30 x federal MW; support 50/60% (55/65% arrears > 12 weeks). |

Not configured in this release [[GAP:RQ-196]]: STC wage levy (63-3061ff) and priority vs IWOs not established from an official source.

## ID.10 Collective agreements and prevailing wage

Prevailing wage (public works) is an optional informational flag [US-OWN-009]: this guide documents prevailing-wage laws, thresholds and certified-payroll duties as an overlay, and the payroll build does not produce certified payroll reports.

No state prevailing wage (repealed 1985) [US-IDR3-003]; 44-1001 95% Idaho residents on public works, no wage rate.

## ID.11 Indexation

MW tracks federal; SUI base AAW penultimate year (2027 unpublished, newest snapshot 2026-08-03); PIT 2,500/5,000 thresholds CPI-U; tables reissued as needed.

## ID.12 Payroll data protection and records

No SSN truncation rule located (ch. 28-51 not read). Full SSN on ID W-4 and new-hire report.

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `id.records.retention_years` | [[FACT:id.records.retention_years=3]] years | 2026-01-01 to open | US-IDS5-006 (Idaho Legislature (Wayback id_ 20260516081013); A.1, direct artifact inspection, confidence high) | 45-610(1): from last date of service. |

Not configured in this release [[GAP:RQ-197]]: Idaho Code 28-51 and any SSN display rule not read.

## ID.13 Live legal change

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `id.live.epb00744_2026_07_23` | [[FACT:id.live.epb00744_2026_07_23=new withholding table in force prospectively from 2026-07-23 (mid_year_rate_change); level withholding]] | 2026-07-23 to open | US-IDS5-011 (Idaho State Tax Commission (Wayback id_ 20261007091254); A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-IDS5-011. |
| `id.live.h0544_military_leave` | [[FACT:id.live.h0544_military_leave=enacted (ch. 57), text not read; private-employer impact open]] | 2026-01-01 to open | US-IDS5-024 (Idaho Legislature (Wayback id_ copy, fetched 2026-11-02); A.1, direct artifact inspection, confidence low) |  |

## ID.14 Authority worked examples (oracle values)

Each example is computed from the statutory parameters listed in this annex and checked against the result published by the authority. Amounts round half-up to the cent unless the line states another rule.

**Example ID-1: single, biweekly wages 1,212.00, payroll on or after 2026-07-23 (percentage computation).**

| Line | Calculation | Result |
|---|---|---|
| Taxable wages | 1,212.00 - [[FACT:id.wh.zero_bracket.single.biweekly=619]] | 593.00 |
| Tax | 593.00 x [[FACT:id.pit.rate.flat=5.3]] % | 31.4290 |
| Withholding | rounded to the nearest whole dollar (`id.wh.rounding`) | 31 |

Computed result = published [[FACT:id.oracle.stc.single_biweekly.withholding=31]] (match).

Example ID-2 (married, weekly 1,000.00, published result [[FACT:id.oracle.stc.married_weekly.withholding=20]]) is not reproduced: the published example uses a zero bracket that matches neither the table in force before 2026-07-23 nor the table in force from that date. Use the wage-bracket table for numbers.

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `id.oracle.stc.married_weekly.withholding` | [[FACT:id.oracle.stc.married_weekly.withholding=20]] USD | 2026-01-01 to open | US-IDS5-008 (Idaho State Tax Commission (Wayback id_ 20261010115435); A.2, derived arithmetically, confidence medium) | Married weekly 1,000: (52,000 - 32,000) x 5.3% / 52 = 20.38 -> 20 as published; the example uses 32,000, matching neither table ([[FACT:id.wh.zero_bracket.married.annual=32,200]] / 30,000) - use EPB00744 for numbers. |
| `id.oracle.stc.single_biweekly.withholding` | [[FACT:id.oracle.stc.single_biweekly.withholding=31]] USD | 2026-07-23 to open | US-IDS5-008 (Idaho State Tax Commission (Wayback id_ 20261010115435); A.2, derived arithmetically, confidence high) | Single, biweekly 1,212: 5.3% x (1,212 - [[FACT:id.wh.zero_bracket.single.biweekly=619]]) = 31.43 -> 31; matches 07-23-2026 table. |

## ID.15 Special populations

- Domestic: MW-excluded; withholding not required (account + W-2/967); UI at 1,000 cash/quarter on cash and noncash [US-IDS5-003, US-IDS5-020, US-IDS5-022].
- Agricultural: MW exclusions; withhold where federal applies and >= 1,000/yr; UI 20,000/quarter or 10 on 20 days; H-2A not taxed [US-IDS5-003, US-IDS5-020].
- Minors: opportunity wage [[FACT:id.minwage.opportunity_wage=4.25]] (under 20, 90 days); under-16 odd jobs and under-18 family MW-excluded; under-21 for parent and under-18 newspaper carriers UI-exempt [US-IDS5-001, US-IDS5-003, US-IDS5-023].
- Tipped: cash [[FACT:id.minwage.tipped.cash_wage=3.35]]; > 30/month [US-IDS5-001, US-IDS5-002].
- Clergy: churches/seminaries/ministers UI-exempt; PIT follows federal [US-IDS5-023, US-IDS5-019].
- Students: own-school, under-22 work-study, student nurses/interns UI-exempt [US-IDS5-023].
- NRAs: ID W-4 status A, 0 allowances, add-on 15/31/33/66 weekly/biweekly/semimonthly/monthly (India students 0) - 2025 edition [US-IDS5-013].
- US nonresidents: 1,000 threshold [US-IDS5-020]. Statutory employees: no Idaho withholding required [US-IDS5-020].
- Corporate officers: withholding employees; UI opt-out before March 31 [US-IDS5-020, US-IDS5-021].
- Government: outside state MW law; UI covered except elected officials, legislators, guard, emergency temps, election workers < 1,000 [US-IDS5-002, US-IDS5-022, US-IDS5-023].

## ID.16 Language

No language requirement; English and Spanish posters offered [US-IDP9M-001]; payslip English (US-OWN-006).

## ID.S Sources

The legal basis of each value (legal-basis register id, authority, source tier and verification method) is given in the row that carries it.
