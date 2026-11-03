# Annex MD: Maryland


United States Country Configuration Guide, jurisdiction annex MD. Tax year 2026; currency USD (two decimal places).

**Scope of this annex.**

This annex holds the Maryland layer only. The federal layer (federal income tax withholding, Social Security and Medicare, federal unemployment tax, Forms W-4, W-2, 941 and 940) is in Annex FED, and the rules for employees who live and work in different jurisdictions (sourcing, resident credits, reciprocity mechanics) are in Annex MULTI. Neither is repeated here. Independent contractors and Form 1099-NEC reporting are out of scope (owner instruction of 2026-10-29) [US-OWN-008]. The pay statement is issued in English.

In every table, *Valid from* and *Valid to* give the period in which the value applies (*open* means no end date has been published), and *Source* is the identifier of the row in the legal-basis register, with the authority and address listed in section MD.S (the source address is held in the register row). Items marked as a research gap are not yet confirmed and must not be configured from this annex.

**Jurisdiction layer.**

| Item | Value |
|---|---|
| Annex tier | T3 (county tax piggybacked, verified) |
| Basis | State + county-of-residence tax withheld together, one return MW506 [US-MDP51-001] |

Tier key: T1 = no state wage tax (unemployment insurance and levies only); T3 = state withholding with no local layer remitted separately; T4 = a local layer remitted to a separate local authority on its own return.

**Configuration decisions.**

- County tax is piggybacked: withhold the state tax and the county-of-residence local tax together and report both on the state return; apply the local table that equals or next exceeds the county rate (`md.wh.method`). Where the county is unknown, use [[FACT:md.local.county_rate.default_unknown=3.3]] percent.
- Nonresidents of reciprocal jurisdictions ([[FACT:md.reciprocity.states=DC, PA, VA, WV]]) are exempt on a valid certificate; other nonresidents pay the state rate plus the special nonresident rate of [[FACT:md.nonres.special_rate=2.25]] percent and no county tax.
- Paid family and medical leave (FAMLI) contributions are not collected in 2026: [[FACT:md.pfml.contributions.start=2027-01-01 (no contribution in 2026)]]. Configure the [[FACT:md.pfml.rate.total=0.9]] percent rate with a 2027-01-01 start only.
- The Social Security number may not appear on the pay statement or any pay notice: [[FACT:md.payslip.ssn.prohibited=True]]. Do not print a truncated number either.
- The pay statement shows the earned sick and safe leave balance each time wages are paid: [[FACT:md.payslip.essl_balance.required=True]].

## MD.1 Employment and labour code

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `md.minwage.hourly` | [[FACT:md.minwage.hourly=15.0]] USD | 2024-01-01 | open | US-MDS5-005 (A.1, Maryland General Assembly) | All sizes; not indexed; no 2027 step. |
| `md.minwage.under18.percent` | [[FACT:md.minwage.under18.percent=85]] percent | 2024-01-01 | open | US-MDS5-005 (A.1, Maryland General Assembly) | = 12.75 [US-MDS5-015]. |
| `md.minwage.tipped.cash_wage` | [[FACT:md.minwage.tipped.cash_wage=3.63]] USD | 2026-01-01 | open | US-MDS5-007 (A.1, Maryland General Assembly) | Max tip credit 11.37; restaurant Tip Credit Wage Statement each pay period. |
| `md.local_minwage.montgomery.51_plus` | [[FACT:md.local_minwage.montgomery.51_plus=18.0]] USD | 2026-07-01 | open | US-MDS5-015 (A.2, Maryland Department of Labor, Division of Labor and Industry) | DOL page only (ordinance unread). 11-50 employees (and 501(c)(3)/Medicaid home care 11+) [[FACT:md.local_minwage.montgomery.11_50=16.50]]; <= 10 [[FACT:md.local_minwage.montgomery.10_or_fewer=15.95]]; CPI-W Washington-Baltimore July 1; under 19 <= 20 h/week excluded; under 20 at 85% first 6 months; tipped cash 4.00. |
| `md.local_minwage.montgomery.11_50` | [[FACT:md.local_minwage.montgomery.11_50=16.5]] USD | 2026-07-01 | open | US-MDS5-015 (A.2, Maryland Department of Labor, Division of Labor and Industry) |  |
| `md.local_minwage.montgomery.10_or_fewer` | [[FACT:md.local_minwage.montgomery.10_or_fewer=15.95]] USD | 2026-07-01 | open | US-MDS5-015 (A.2, Maryland Department of Labor, Division of Labor and Industry) |  |
| `md.local_minwage.howard` | [[FACT:md.local_minwage.howard=16.0]] USD | 2026-07-01 | open | US-MDS5-015 (A.2, Maryland Department of Labor, Division of Labor and Industry) |  |
| `md.local_minwage.prince_georges` | [[FACT:md.local_minwage.prince_georges=15.3]] USD | 2026-07-01 | open | US-MDS5-015 (A.2, Maryland Department of Labor, Division of Labor and Industry) |  |
| `md.overtime.weekly_threshold_hours` | [[FACT:md.overtime.weekly_threshold_hours=40]] hours | 2026-01-01 | open | US-MDS5-006 (A.1, Maryland General Assembly) | No daily OT; 48 h bowling and non-hospital residential care; 60 h FLSA-exempt agriculture. |
| `md.pay_frequency.rule` | [[FACT:md.pay_frequency.rule=at least every 2 weeks or twice a month (EAP less often); nonworkday payday moves to preceding workday]] | 2026-01-01 | open | US-MDS5-008 (A.1, Maryland General Assembly) |  |
| `md.payment.method` | [[FACT:md.payment.method=cash or check at face value; direct deposit only with authorisation; pay card only with authorisation and fees disclosed in writing in >= 12-point type]] | 2026-01-01 | open | US-MDS5-008 (A.1, Maryland General Assembly) |  |

- Not configured in this release [[GAP:RQ-001]]: The county ordinances were not read (the Montgomery County site returned an error); the county minimum wages above come from the state Department of Labor page only.

## MD.2 Income tax withholding

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `md.pit.rates` | [[FACT:md.pit.rates=2 / 3 / 4 / 4.75 / 5 / 5.25 / 5.5 / 5.75 / 6.25 / 6.50 percent (TG 10-105); single 6.25% > 500,000 and 6.50% > 1,000,000; joint 6.25% > 600,000 and 6.50% > 1,200,000]] | 2025-01-01 | open | US-MDS5-001 (A.1, Maryland General Assembly) | The two top bands are new from the 2025 Budget Reconciliation and Financing Act and apply to 2026 withholding [US-MDS5-003]. The 2% capital-gain surcharge applies at assessment only. |
| `md.pit.top_rate` | [[FACT:md.pit.top_rate=6.5]] percent | 2025-01-01 | open | US-MDS5-001 (A.1, Maryland General Assembly) |  |
| `md.wh.method` | [[FACT:md.wh.method=wages - standard deduction - exemptions x per-period exemption; apply the local table that equals or slightly exceeds the county rate (tables start at 4.75%, ignoring 2/3/4% bands); ten tables 2.25, 2.40, 2.65, 2.75, 2.85, 3.00, 3.05, 3.10, 3.20, 3.30]] | 2026-01-01 | 2026-12-31 | US-MDS5-021 (A.2, Comptroller of Maryland) | The single bases of the 3.30 table reproduce from the state bands plus the county rate; the joint bases reproduce exactly. Per-period exemption / standard deduction: weekly 61.54/65.38, monthly 266.67/283.33; the biweekly (130.76) and semimonthly (141.66) standard deductions are truncated; daily amounts divide the annual amounts by 365. |
| `md.wh.exemption.annual` | [[FACT:md.wh.exemption.annual=3200]] USD | 2026-01-01 | 2026-12-31 | US-MDS5-021 (A.2, Comptroller of Maryland) |  |
| `md.wh.std_deduction` | [[FACT:md.wh.std_deduction=3400]] USD | 2026-01-01 | 2026-12-31 | US-MDS5-021 (A.2, Comptroller of Maryland) | TG 10-217: indexed from 2026 and rounded down to a multiple of 50 [US-MDS5-002]; the Comptroller's published adjustment figure was not read. |
| `md.wh.floor.annual` | [[FACT:md.wh.floor.annual=5000]] USD | 2026-01-01 | 2026-12-31 | US-MDS5-021 (A.2, Comptroller of Maryland) | No withholding below weekly 96, biweekly 192, semimonthly 208, monthly 417, daily 13.70, annual 5,000. |
| `md.wh.certificate` | [[FACT:md.wh.certificate=MW507 (MW507M military spouse, MW507P annuity/sick pay); none filed = one exemption; unknown county default 3.30% (state payroll memo)]] | 2026-01-01 | open | US-MDS5-021 (A.2, Comptroller of Maryland) |  |
| `md.wh.supplemental.lump_sum_bonus` | [[FACT:md.wh.supplemental.lump_sum_bonus=top state rate 6.50% + county top local rate (e.g. 9.80% in 3.30 table; 9.70% in 3.20 table); no flat rate for other supplemental pay; computed in cents (retirement whole dollars)]] | 2026-01-01 | 2026-12-31 | US-MDS5-021 (A.2, Comptroller of Maryland) |  |

## MD.2b Non-resident regime and reciprocity

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `md.nonres.special_rate` | [[FACT:md.nonres.special_rate=2.25]] percent | 2026-01-01 | 2026-12-31 | US-MDS5-021 (A.2, Comptroller of Maryland) | Residents of non-reciprocal states: state rate plus the special nonresident rate, no county tax; the flat nonresident rate is the lowest table rate plus the special rate. Residents of reciprocal DC/PA/VA/WV are exempt with Form MW507 [US-MULTI-008]; the exemption is lost if the employee keeps a Maryland abode for more than six months and is present 183 days or more (not WV). Maryland residents working in Delaware or another non-reciprocal state: Delaware table with county tax and credit. |
| `md.reciprocity.states` | [[FACT:md.reciprocity.states=DC, PA, VA, WV]] | 2026-01-01 | open | US-MDS5-021 (A.2, Comptroller of Maryland) |  |

## MD.2c Local wage taxes

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `md.local.county_rate.default_unknown` | [[FACT:md.local.county_rate.default_unknown=3.3]] percent | 2026-01-01 | 2026-12-31 | US-MDS5-003 (A.2, Comptroller of Maryland (Central Payroll Bureau)) | New county maximum from TY2026. |
| `md.local.county_rates` | [[FACT:md.local.county_rates=2.25 Worcester (24), out-of-state (25-76); 2.40 Talbot (21); 2.65 Garrett (12); 2.74 Cecil (08); 2.95 Washington (22); 3.03 Carroll (07), Charles (09); 3.06 Harford (13); 3.20 Allegany, Baltimore Co, Baltimore City, Calvert, Caroline, Howard, Montgomery, Prince George's, Queen Anne's, St. Mary's, Somerset, Wicomico; 3.30 Dorchester (10), Kent (15); graduated Anne Arundel (02) and Frederick (11)]] | 2026-01-01 | 2026-12-31 | US-MDS5-003 (A.2, Comptroller of Maryland (Central Payroll Bureau)) | Cross-checked with DLS [US-MDS5-004]; Allegany [[FACT:md.local.county.carroll.rate=3.03]] -> 3.20, Kent 3.20 -> 3.30 vs 2025. |
| `md.local.anne_arundel.single` | [[FACT:md.local.anne_arundel.single=2.70 to 50,000 / 2.94 to 400,000 / 3.20 over (joint 2.70 to 75,000 / 2.94 to 480,000 / 3.20 over)]] | 2026-01-01 | 2026-12-31 | US-MDS5-003 (A.2, Comptroller of Maryland (Central Payroll Bureau)) |  |

## MD.3 Social insurance: unemployment, disability, paid leave and payroll levies

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `md.sui.employer.rate.min` | [[FACT:md.sui.employer.rate.min=0.3]] percent | 2026-01-01 | 2026-12-31 | US-MDP9V-001 (A.2, Maryland Department of Labor, Division of Unemployment Insurance) | Experience rates run from the minimum to the maximum ([[FACT:md.sui.employer.rate.max=7.5]] percent), which is also the standard rate; foreign construction contractors pay the industry average. |
| `md.sui.employer.rate.max` | [[FACT:md.sui.employer.rate.max=7.5]] percent | 2026-01-01 | 2026-12-31 | US-MDP9V-001 (A.2, Maryland Department of Labor, Division of Unemployment Insurance) |  |
| `md.sui.new_employer.rate.range` | [[FACT:md.sui.new_employer.rate.range=1.0% - 2.6%]] | 2026-01-01 | 2026-12-31 | US-MDP9V-001 (A.2, Maryland Department of Labor, Division of Unemployment Insurance) |  |
| `md.pfml.contributions.start` | [[FACT:md.pfml.contributions.start=2027-01-01 (no contribution in 2026)]] | 2027-01-01 | open | US-MDS5-014 (A.2, Maryland Department of Labor (FAMLI Division)) |  |
| `md.pfml.rate.total` | [[FACT:md.pfml.rate.total=0.9]] percent | 2027-01-01 | open | US-MDS5-014 (A.2, Maryland Department of Labor (FAMLI Division)) | 0.45 employer + 0.45 employee (employer may withhold up to 50%); wages to SS base; < 15 employees (all locations, one EIN) remit employee share only; statutory rate cap; quarterly with wage-and-hour report, first due 2027-04-30; coverage follows UI localization (LE 8-202) [US-MDS5-019]; benefits from 2028-01-01 up to 1,000/week, 12 weeks. |
| `md.pfml.employee_share.max_percent` | [[FACT:md.pfml.employee_share.max_percent=50]] percent | 2027-01-01 | open | US-MDS5-014 (A.2, Maryland Department of Labor (FAMLI Division)) |  |
| `md.pfml.small_employer.threshold` | [[FACT:md.pfml.small_employer.threshold=15]] employees | 2027-01-01 | open | US-MDS5-014 (A.2, Maryland Department of Labor (FAMLI Division)) |  |
| `md.sui.wage_base` | [[FACT:md.sui.wage_base=8500]] USD | 2026-01-01 | open | US-MDP51-002 (A.2, Maryland Department of Labor, Division of Unemployment Insurance) | Not indexed; employer-only; other-state credit implied by BEACON field. |

Rules:

- No SDI/TDI; no other levy beyond withholding. (US-MDP9V-002)

- Not configured in this release [[GAP:RQ-002]]: Implied by the BEACON "Out of State taxable wages" field only; taxable-wages statute not located (LE 8-101, 8-606 read).
- Not configured in this release [[GAP:RQ-003]]: The domestic-service coverage threshold of Labor and Employment Article Title 8 is not verified.

## MD.4 Pay statement

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `md.payslip.essl_balance.required` | [[FACT:md.payslip.essl_balance.required=True]] | 2026-01-01 | open | US-MDS5-013 (A.1, Maryland General Assembly) | LE 3-1305(f): available ESSL balance each time wages are paid (online system satisfies). Core LE 3-504 content on row US-MDP51-005. |
| `md.payslip.items` | [[FACT:md.payslip.items=employer name, address, phone; pay date and period; hours (unless exempt); rates; gross and net; each deduction by name and amount; other bases of pay; written or online (LE 3-504); notice at hire and change one pay period ahead]] | 2026-01-01 | open | US-MDP51-005 (A.1, Maryland General Assembly) |  |

## MD.5 Statutory reporting

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `md.report.wh.mw506` | [[FACT:md.report.wh.mw506=MW506 on Maryland Tax Connect: accelerated (15,000+ prior year and 700+ accumulated, within 3 business days); monthly (> 700 in any quarter, 15th); quarterly (< 700/quarter); seasonal (approval); annual (< 250/yr, Jan 31); amendments MW506A/AM; final MW506FR; CRA registration (8-digit CRN)]] | 2026-01-01 | open | US-MDS5-021 (A.2, Comptroller of Maryland) |  |
| `md.report.annual.mw508` | [[FACT:md.report.annual.mw508=MW508 + W-2s due 31 January; electronic mandatory at 25+ W-2s (TG 13-706.1; 100 penalty); SSA EFW2 modified MD format by bulk upload; RS FEIN 328-336, CRN 338-345; RV = MW508 with NAICS 333-338; date-time stamp 497-512; zero MW508 required for open accounts]] | 2025-01-01 | open | US-MDS5-016 (A.2, Comptroller of Maryland) | TY2025 spec ("layouts unchanged"); TY2026 not posted. |
| `md.report.w2.efile_threshold` | [[FACT:md.report.w2.efile_threshold=25]] forms | 2025-01-01 | open | US-MDS5-016 (A.2, Comptroller of Maryland) |  |
| `md.report.sui.quarterly` | [[FACT:md.report.sui.quarterly=BEACON within 1 month after quarter end; online, CSV, XML, ICESA or EFW2 (spec 2026-04-20); cents without decimal point; adjustment codes 00-10; 35 per late report; 1.5%/month interest; optional out-of-state taxable wages field]] | 2026-04-20 | open | US-MDS5-017 (A.2, Maryland Department of Labor, Division of Unemployment Insurance) |  |
| `md.newhire.report_days` | [[FACT:md.newhire.report_days=20]] days | 2026-01-01 | open | US-MDS5-018 (A.1, Maryland General Assembly) | LE 8-626.1: SSN, name, address, hire date, employer name/address, starting wage, employer health insurance offered, FEIN, MD UI account; penalty warning then 20/month (500 conspiracy). |

- Not configured in this release [[GAP:RQ-004]]: TY2026 Maryland W-2/MW508 EFW2 spec not posted.

## MD.6 Leave

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `md.leave.essl.paid_employer_threshold` | [[FACT:md.leave.essl.paid_employer_threshold=15]] employees | 2026-01-01 | open | US-MDS5-013 (A.1, Maryland General Assembly) | HWFA LE 3-1301..1311: 15+ paid, <= 14 unpaid; 1 h per 30 h; caps earn 40 / use 64 / balance 64; use after 106 days; no accrual in periods < 24 h (biweekly) / 26 h (semimonthly); carryover 40 or front-load; rehire within 37 weeks reinstated; no payout; advanced leave recoverable with signed agreement; excluded < 12 h/week, under 18, agricultural, certain temps; post-2017 local laws pre-empted (Montgomery survives). |
| `md.leave.essl.accrual.hours_worked_per_hour` | [[FACT:md.leave.essl.accrual.hours_worked_per_hour=30]] hours | 2026-01-01 | open | US-MDS5-013 (A.1, Maryland General Assembly) |  |
| `md.leave.essl.annual_earn_cap_hours` | [[FACT:md.leave.essl.annual_earn_cap_hours=40]] hours | 2026-01-01 | open | US-MDS5-013 (A.1, Maryland General Assembly) |  |
| `md.leave.essl.use_cap_hours` | [[FACT:md.leave.essl.use_cap_hours=64]] hours | 2026-01-01 | open | US-MDS5-013 (A.1, Maryland General Assembly) |  |

- Not configured in this release [[GAP:RQ-005]]: Whether the 12 h/week threshold and accrual count MD hours only.
- Not configured in this release [[GAP:RQ-006]]: Montgomery County Code ch. 27 Art. XIII (pre-2017 ESSL) not read.

## MD.7 Termination and final pay

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `md.final_pay.rule` | [[FACT:md.final_pay.rule=on or before next regular payday, discharge or resignation; accrued vacation payable unless written policy limits payout, employee notified at hire and policy denies it; ESSL not payable]] | 2026-01-01 | open | US-MDS5-010 (A.1, Maryland General Assembly) |  |

- Not configured in this release [[GAP:RQ-007]]: COMAR 09.32.01 separation notice and Economic Stabilization Act (LE 11-301) not read.

## MD.8 Benefits in kind and taxable wages

No Maryland rule is configured in this domain; the federal treatment in Annex FED applies.

- Not configured in this release [[GAP:RQ-008]]: TG 10-203/204/205 and annual IRC conformity act not read.

## MD.9 Deductions and garnishments

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `md.deductions.rule` | [[FACT:md.deductions.rule=only if court-ordered, authorised in writing, allowed by the Commissioner or required by law (LE 3-503)]] | 2026-01-01 | open | US-MDS5-009 (A.1, Maryland General Assembly) |  |
| `md.garn.creditor.weekly_exempt_floor` | [[FACT:md.garn.creditor.weekly_exempt_floor=450.0]] USD | 2024-01-01 | open | US-MDS5-011 (A.1, Maryland General Assembly) | CL 15-601.1: greater of 75% of disposable or 30 x State MW x weeks = 30 x 15.00; medical insurance deductions also exempt; per pay period. |

- Not configured in this release [[GAP:RQ-009]]: IWO employer fee/remittance (FL 10-123/10-128) and Comptroller salary lien (TG 13-811) not read.

## MD.10 Collective agreements and prevailing wage

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `md.prevailing_wage.threshold` | [[FACT:md.prevailing_wage.threshold=250000]] USD | 2026-01-01 | open | US-MDS5-012 (A.1, Maryland General Assembly) | Not for Davis-Bacon-funded parts; extends to TIF-bond construction and mechanical systems service contracts above SCA threshold. |

- Not configured in this release [[GAP:RQ-010]]: SFP 17-220 certified payroll duty not read.

## MD.11 Indexation

Indexation of each value is stated in the note of the value concerned.

## MD.12 Payroll data protection and records

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `md.payslip.ssn.prohibited` | [[FACT:md.payslip.ssn.prohibited=True]] | 2026-01-01 | open | US-MDS5-008 (A.1, Maryland General Assembly) | LE 3-502(d): SSN may not be printed on the wage check, any attachment, direct-deposit notice or card-credit notice; covers governmental units; no truncation safe harbour - treat truncated SSN as barred. |
| `md.records.withholding.retention_years` | [[FACT:md.records.withholding.retention_years=3]] years | 2026-01-01 | open | US-MDS5-021 (A.2, Comptroller of Maryland) |  |

- Not configured in this release [[GAP:RQ-011]]: LE 3-424 record period and e-delivery consent not read.

## MD.13 Live legal change

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `md.live.county_rates_2026` | [[FACT:md.live.county_rates_2026=county maximum 3.30% from TY2026 (Dorchester, Kent 3.30; Allegany 3.20); level withholding]] | 2026-01-01 | open | US-MDS5-004 (A.3, Maryland Department of Legislative Services) |  |

- Not configured in this release [[GAP:RQ-012]]: The effect of the 2026 Budget Reconciliation and Financing Act on taxable income and withholding from tax year 2027 rests on a secondary summary only.

## MD.14 Authority worked examples (oracle values)

No authority worked example is reproduced in this annex; recomputed withholding examples are in Module 12.

## MD.15 Special populations

- Domestic: MD withholding not required (private home, college club, fraternity). (US-MDS5-021)
- Agricultural: withheld when subject to FICA; ESSL excluded. (US-MDS5-021, US-MDS5-020, US-MDS5-006, US-MDS5-013)
- Tipped: Tip Credit Wage Statement; ESSL paid at not more than MW. (US-MDS5-007, US-MDS5-015, US-MDS5-013)
- Clergy: withholding not required; churches/ministers outside UI. (US-MDS5-021, US-MDS5-020)
- NRAs: general nonresident treatment; Nonresident seamen: not withheld in MD port. (US-MDS5-021)
- Commission workers: insurance producers, real estate, yacht salespersons, direct sellers etc; UI-excluded. (US-MDS5-020)
- Government: withholding applies; elected officials/legislators/judges/Guard etc; UI-excluded. (US-MDS5-020)
- Not configured in this release [[GAP:RQ-013]]: Thresholds, amounts or conditions for these populations are stated in the sources read without a confirmed value record and are not configured from this annex: Domestic; Agricultural; Minors; Tipped; Students; Military spouses.

## MD.16 Language

- The pay statement and all filings are in English (owner decision US-OWN-006).

## MD.S Sources

| Source | Authority |
|---|---|
| US-MDP51-002 | Maryland Department of Labor, Division of Unemployment Insurance |
| US-MDP51-005 | Maryland General Assembly |
| US-MDP9V-001 | Maryland Department of Labor, Division of Unemployment Insurance |
| US-MDS5-001 | Maryland General Assembly |
| US-MDS5-003 | Comptroller of Maryland (Central Payroll Bureau) |
| US-MDS5-004 | Maryland Department of Legislative Services |
| US-MDS5-005 | Maryland General Assembly |
| US-MDS5-006 | Maryland General Assembly |
| US-MDS5-007 | Maryland General Assembly |
| US-MDS5-008 | Maryland General Assembly |
| US-MDS5-009 | Maryland General Assembly |
| US-MDS5-010 | Maryland General Assembly |
| US-MDS5-011 | Maryland General Assembly |
| US-MDS5-012 | Maryland General Assembly |
| US-MDS5-013 | Maryland General Assembly |
| US-MDS5-014 | Maryland Department of Labor (FAMLI Division) |
| US-MDS5-015 | Maryland Department of Labor, Division of Labor and Industry |
| US-MDS5-016 | Comptroller of Maryland |
| US-MDS5-017 | Maryland Department of Labor, Division of Unemployment Insurance |
| US-MDS5-018 | Maryland General Assembly |
| US-MDS5-021 | Comptroller of Maryland |
