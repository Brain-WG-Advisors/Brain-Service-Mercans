# Annex GA: Georgia


**Layer classification (T3).** T3: separate state withholding calculation and state return; no local layer, or a local layer piggybacked on the state return. Source: tier census, local income tax domain.

**Summary.** Federal minimum wage applies (state 5.15 nominal); local mandates pre-empted (34-4-3.1). Flat PIT 4.99% for 2026 (HB 463, signed 2026-05-11, retroactive; withholding at 4.99% from 2026-05-11); standard deduction 30,000/15,000, dependent 5,000; G-4 certificate; no local tax, no reciprocity; HB 463 OT/tip subtractions at assessment only. SUI base 9,500, new employer 2.70% (2.64% + 0.06% admin assessment to 2026-12-31). No pay-statement statute. New-hire within 10 days. Oracle: DOR guide percentage-method example 27.03.

Each parameter row gives its key, the period in force and its legal basis: the legal-basis entry, the authority, the source tier and how the value was verified.

## GA.1 Employment and labour code

Overtime: FLSA only (1.5x over 40); no daily OT, no break law [US-GAS5-016, US-GAS5-008]. State-rate exclusion thresholds: not configured in this release (open gap RQ-582).

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ga.local_mandates.preempted` | True | 2026-01-01 to open | US-GAS5-017 (Georgia General Assembly; A.1, direct artifact inspection, confidence high) | 34-4-3.1 pre-empts local wage/benefit/scheduling mandates; HB 1157 (2026) repeal introduced, NOT enacted. |
| `ga.minwage.state.hourly` | 5.15 USD | 2026-01-01 to open | US-GAS5-022 (Georgia Department of Labor; A.2, direct artifact inspection, confidence medium) | O.C.G.A. 34-4-3; GDOL: the federal 7.25 applies with limited exceptions [US-GAS5-008]. Not indexed; no 2027 increase. |
| `ga.pay_frequency.rule` | at least semi-monthly in two equal periods per month; officers/superintendents/department heads monthly (34-7-2) | 2026-01-01 to open | US-GAP9L-001 (Georgia General Assembly (legis.ga.gov); A.1, direct artifact inspection, confidence high) |  |
| `ga.payment.method` | money, check, direct deposit with consent, or payroll card (written fee explanation at hire or 30 days before; opt-out; one free access) - full net amount | 2026-01-01 to open | US-GAP9L-001 (Georgia General Assembly (legis.ga.gov); A.1, direct artifact inspection, confidence high) |  |

Not configured in this release (open gap RQ-161): 34-4-3 state-rate scope not read on an official host (low impact; federal rate applies).

## GA.2 Income tax withholding

Configuration rule: the HB 463 overtime and tip subtractions (`ga.pit.overtime_subtraction.max`, `ga.pit.tip_subtraction.max`) operate at assessment only. They do not reduce withholding; payroll reports them on the W-2 only.

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ga.pit.overtime_subtraction.max` | 1,750 USD | 2026-01-01 to 2028-12-31 | US-GAS5-009 (Georgia General Assembly; A.1, second independent authority, confidence high) | HB 463: full-time hourly OT 2026-2028; operating level ASSESSMENT only, do not reduce withholding; W-2 box 12 TT, box 14b TTOC; RLA "GA OT" 14a; G-7 quarterly totals from 2027 [US-GAS5-003]. |
| `ga.pit.rate.flat` | 4.99 % | 2026-01-01 to open | US-GAS5-009 (Georgia General Assembly; A.1, second independent authority, confidence high) | Statutory rate for taxable year 2026, retroactive to 2026-01-01 (HB 463); the year-end assessment applies 4.99% to all 2026 wages. Withholding level: ga.wh.rate. LEVEL: assessment. |
| `ga.pit.tip_subtraction.max` | 1,750 USD | 2026-01-01 to open | US-GAS5-009 (Georgia General Assembly; A.1, second independent authority, confidence high) | Assessment only; W-2 box 12 TP. |
| `ga.wh.certificate.form` | G-4 Rev. 06/03/26: letters A Single, B MFS or MFJ both working, C MFJ one working, D HoH; line 4 dependents; line 5 adjustment allowances (/5,000, remainder >2,500 rounds up); line 6 additional; 8a exempt; 8b MSRRA | 2026-06-03 to open | US-GAS5-010 (Georgia Department of Revenue; A.2, direct artifact inspection, confidence high) | Mail to DOR only if >14 allowances or exempt; no G-4: use W-4 if sufficient else Single 0; exempt valid to 15 Feb next year [US-GAS5-004]. |
| `ga.wh.dependent_allowance` | 5,000 USD | 2026-01-01 to open | US-GAS5-001 (Georgia Department of Revenue; A.2, derived arithmetically, confidence high) | Derivation recorded in legal-basis entry US-GAS5-001. |
| `ga.wh.method` | tax tables (pp. 31-50) or percentage method (Tables E/F): (wages - period standard deduction - dependent allowance x n) x 4.99%; tables use top of band | 2026-01-01 to open | US-GAS5-001 (Georgia Department of Revenue; A.2, derived arithmetically, confidence high) | Per-period values = annual / periods rounded to cent (21 values re-derived); daily = annual/365. Tables and formula "differ slightly". |
| `ga.wh.rate` | 5.19 % | 2026-01-01 to 2026-05-10 | US-GA-001 (Georgia Department of Revenue; A.2, quoted from authority page, confidence high) | Employers kept withholding 5.19% until HB 463 was signed (2026-05-11). LEVEL: withholding. |
| `ga.wh.rate` | 4.99 % | 2026-05-11 to open | US-GAS5-009 (Georgia General Assembly; A.1, second independent authority, confidence high) | Withholding at 4.99% from 2026-05-11 (DOR Employer Guide US-GA-001 states the start date; HB 463 the rate). LEVEL: withholding. |
| `ga.wh.std_deduction.mfj` | 30,000 USD | 2026-01-01 to open | US-GAS5-001 (Georgia Department of Revenue; A.2, derived arithmetically, confidence high) | Single/HoH 15,000; MFS 15,000; married both working use MFS column. |
| `ga.wh.std_deduction.single` | 15,000 USD | 2026-01-01 to open | US-GAS5-001 (Georgia Department of Revenue; A.2, derived arithmetically, confidence high) | Derivation recorded in legal-basis entry US-GAS5-001. |
| `ga.wh.supplemental.rate` | applicable income tax rate in effect when paid (4.99% from 2026-05-11); no separate table | 2026-01-01 to open | US-GAS5-004 (Georgia Department of Revenue; A.2, direct artifact inspection, confidence high) |  |

Not yet published (expected OPB determination 2026-12-01; guide after that) (open gap RQ-162): 2027 rate/standard deduction/dependent depend on OPB trigger determination due 2026-12-01; no 2027 value is modelled until it is published.

## GA.2b Non-resident regime and reciprocity

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ga.nonres.threshold` | withhold for nonresidents when more than 5% of wages or more than 5,000 is attributable to Georgia | 2026-01-01 to open | US-GAS5-004 (Georgia Department of Revenue; A.2, direct artifact inspection, confidence high) | Resident: legal resident, living in GA regularly, or 183+ days in 365 ending 31 Dec. Residents working elsewhere: no GA withholding if that state requires it. No reciprocity, no 23-day rule [US-GAP52-003]. NRAs: withhold unless 8233 filed and copy sent to DOR. |
| `ga.nonres.threshold_amount` | 5,000 USD | 2026-01-01 to open | US-GAS5-004 (Georgia Department of Revenue; A.2, direct artifact inspection, confidence high) |  |
| `ga.nonres.threshold_percent` | 5 % | 2026-01-01 to open | US-GAS5-004 (Georgia Department of Revenue; A.2, direct artifact inspection, confidence high) |  |

## GA.2c Local wage taxes

No jurisdiction-specific item was recorded in the research for this domain.

## GA.3 Social insurance: unemployment, disability, paid leave and payroll levies

Experience rate by reserve ratio; DOL-626 notices on the Employer Portal by 31 Dec. The 2026 rate range is not on a primary source and is not modelled. No SDI or PFML programme is configured for Georgia [US-OWN-007; US-GAP9W-001; US-GAP9W-003].

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ga.sui.admin_assessment.rate` | 0.06 % | 2024-01-01 to 2026-12-31 | US-GAS5-013 (Georgia General Assembly; A.1, second independent authority, confidence high) | May not be deducted from wages; only employer levy [US-GAP9W-001, US-GAP9W-003]. |
| `ga.sui.coverage` | 1 worker in 20 weeks or 1,500 quarter; agricultural 10 in 20 weeks or 20,000; domestic 1,000 quarter; 501(c)(3) 4 in 20 weeks; officers are employees; UI wages include 401(k) deferrals, tips (FUTA extent), board and lodging; exclude 125 premiums and employer 401(k) | 2026-01-01 to open | US-GAS5-006 (Georgia Department of Labor; A.3, direct artifact inspection, confidence high) |  |
| `ga.sui.new_employer.rate.contribution` | 2.7 % | 2027-01-01 to open | US-GAS5-013 (Georgia General Assembly; A.1, second independent authority, confidence high) | 34-8-151(a), absent new legislation (none located). |
| `ga.sui.new_employer.rate.total` | 2.7 % | 2026-01-01 to 2026-12-31 | US-GAS5-013 (Georgia General Assembly; A.1, derived arithmetically, confidence high) | 2.64% contribution (34-8-151(d)) + 0.06% admin assessment (34-8-181) = 2.70%. From 2027 2.7% contribution only (Art. 6 repealed 2027-01-01). |
| `ga.sui.wage_base` | 9,500 USD | 2013-01-01 to open | US-GAW1B-001 (Georgia Department of Labor; A.2, quoted from authority page, confidence high) | HB 347 (2012), not indexed; employer-only (no employee contribution). |

Not configured in this release (open gap RQ-163): 2026 and 2027 experience rate min/max not on a primary source.

Not configured in this release (open gap RQ-164): No 2026 act extending Article 6 beyond 2026-12-31 located.

Not configured in this release (open gap RQ-582): The thresholds for the State UI rate exclusions are not established from an official source.

## GA.4 Pay statement

No Georgia pay-statement content statute: 34-7-2 and the 164-page GDOL handbook read (full-text search); federal layer only; electronic delivery unrestricted; no language clause.

## GA.5 Statutory reporting

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ga.newhire.report_days` | 10 days | 2026-01-01 to open | US-GAS5-012 (Georgia Department of Human Services, Georgia State Directory of New Hires; A.2, second independent authority, confidence high) | O.C.G.A. 19-11-9.2: FEIN (same as UI), employee name/address/SSN/DOB/start date, medical insurance availability, state of hire. |
| `ga.report.annual.g1003` | W-2s and 1099-NEC with GA withholding due 31 Jan (TY2026: 2027-02-01), other 1099s 28 Feb; e-file if federal e-file or EFT; GTC entry, G-1003 Excel/CSV or EFW2 + GA RS (Rev 01/18); 1099s via IRIS XML only; no CF/SF | 2026-01-01 to open | US-GAS5-003 (Georgia Department of Revenue; A.2, direct artifact inspection, confidence high) |  |
| `ga.report.sui.dol4n` | DOL-4N due 30 Apr, 31 Jul, 31 Oct, 31 Jan; electronic for 25+ employees (portal <=100, CSV/Excel 100-15,000, SFTP >15,000); domestic-only annual DOL-4 by 31 Jan; corrections DOL-3C; temporary substitute SSN 000-00-000n allowed (correct within 30 days) | 2026-01-01 to open | US-GAS5-005 (Georgia Department of Labor; A.3, direct artifact inspection, confidence high) |  |
| `ga.report.sui.efile_threshold_employees` | 25 employees | 2026-01-01 to open | US-GAS5-005 (Georgia Department of Labor; A.3, direct artifact inspection, confidence medium) | Proposed all-employer mandate (300-2-2-.02(6)) adoption unconfirmed. |
| `ga.report.w2.rs_layout` | Rev 01/18: 248-267 state employer account; 274-275 state code; 276-286 state wages; 287-297 state tax; 298-307 period end; 331-339 withholding number | 2018-01-01 to open | US-GAS5-011 (Georgia Department of Revenue; A.2, direct artifact inspection, confidence medium) | [partial row] TY2026 layout with GA OT field not yet posted. |
| `ga.report.wh.payer_status` | lookback 12 months to prior 30 June: semi-weekly > 50,000 (EFT; G-7 Schedule B); monthly > 200/month (GA-V by 15th; G-7 quarterly); quarterly <= 200/month and > 800/yr; annual <= 800/yr by 31 Jan | 2026-01-01 to open | US-GAS5-002 (Georgia Department of Revenue; A.2, direct artifact inspection, confidence high) | One-day rule > 100,000 per payday; G-7 > 500 makes EFT/e-file mandatory (10% penalty); zero G-7 required; Q3 2026 due 2026-11-02, Q4 2027-02-01. |
| `ga.report.wh.semiweekly_threshold` | 50,000 USD | 2026-01-01 to open | US-GAS5-002 (Georgia Department of Revenue; A.2, direct artifact inspection, confidence high) |  |

Not yet published (open gap RQ-165): TY2026 RS record (GA OT field) and G-1003 2026 template not posted on 2026-11-02 (announced late October 2026).

Not configured in this release (open gap RQ-166): Adoption and effective date of proposed Rule 300-2-2-.02(6) (all-employer electronic DOL-4N) unconfirmed.

## GA.6 Leave

Family Care Act 34-1-10 (25+ employees offering sick leave; 5 days for family) read only in committee-substitute text [US-GAS5-015 partial]; enacted version and sunset unconfirmed, not modelled.

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ga.leave.paid.mandate.exists` | False | 2026-01-01 to open | US-GAS5-016 (Georgia Department of Labor; A.3, direct artifact inspection, confidence high) |  |

Not configured in this release (open gap RQ-167): 34-1-10 read only in committee-substitute text; a secondary source says repealed in 2023.

## GA.7 Termination and final pay

No final-pay statute; vacation contractual. Severance withheld if resident at payment. Final G-7 within 30 days of ceasing employees.

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ga.mass_separation.threshold_workers` | 25 workers | 2026-01-01 to open | US-GAS5-020 (Georgia Department of Labor; A.1, direct artifact inspection, confidence medium) | [partial row] DOL-402/402A within 48 hours when 25+ separated same day same reason for 7+ days; replaces individual DOL-800s. |
| `ga.sales_rep.commission_due_days` | 30 days | 2026-01-01 to open | US-GAS5-007 (Georgia Department of Labor; A.3, direct artifact inspection, confidence high) |  |
| `ga.separation_notice.delivery_days` | 3 days | 2026-01-01 to open | US-GAS5-007 (Georgia Department of Labor; A.3, direct artifact inspection, confidence high) |  |
| `ga.separation_notice.dol800` | DOL-800 (R-02-24) to every separated worker stating reason, on last day or within 3 days; electronic with e-signature allowed (Oct 2026 rules) | 2026-01-01 to open | US-GAS5-007 (Georgia Department of Labor; A.3, direct artifact inspection, confidence high) |  |

## GA.8 Benefits in kind and taxable wages

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ga.pit.conformity` | federal AGI start; IRC conformity as of 2026-01-01 (HB 1199); 401(k)/125/HSA/transit/GTL follow federal; no GA departure located | 2026-01-01 to open | US-GAS5-023 (Georgia Department of Revenue; A.2, second independent authority, confidence medium) |  |

## GA.9 Deductions and garnishments

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ga.garn.child_support.per_deduction_fee` | 3 USD | 2026-01-01 to open | US-GAS5-019 (Georgia Department of Human Services, Division of Child Support Services; A.2, direct artifact inspection, confidence high) |  |
| `ga.garn.child_support.setup_fee` | 25 USD | 2026-01-01 to open | US-GAS5-019 (Georgia Department of Human Services, Division of Child Support Services; A.2, direct artifact inspection, confidence high) | 3 per deduction; Family Support Registry. |
| `ga.garn.creditor.max_percent` | 25 % | 2016-01-01 to open | US-GAS5-014 (Georgia General Assembly; A.1, direct artifact inspection, confidence medium) | [partial row] [partial] 18-4-5: lesser of 25% of disposable earnings or excess over 217.00 (as printed); CCPA floor 30 x 7.25 = 217.50 binds [US-FED-011]: use 217.50. Support continuing garnishment max 50%. Garnishee expense greater of 50 or 10% capped 100. |

Not configured in this release (open gap RQ-168): DOR wage-levy rules and enacted 18-4-5 (2016 Act, 2020 SB 443) not read.

## GA.10 Collective agreements and prevailing wage

Prevailing wage (public works) is an optional informational flag [US-OWN-009]: this guide documents prevailing-wage laws, thresholds and certified-payroll duties as an overlay, and the payroll build does not produce certified payroll reports.

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ga.prevailing_wage.state_law.exists` | False | 2026-01-01 to open | US-GAP51-002 (US Department of Labor Wage and Hour Division; A.2, quoted from authority page, confidence high) | Davis-Bacon only; right-to-work state [US-GAS5-022]. |

## GA.11 Indexation

Nothing CPI-indexed. HB 463 sets a conditional step schedule for the rate, standard deduction and dependent allowance from 2027; no 2027 value is modelled until the OPB determination of 2026-12-01 and the 2027 DOR guide are published.

## GA.12 Payroll data protection and records

Full SSN required on GDOL records. 10-1-393.8 (no public SSN display) only on a secondary-source row [US-GAS5-018].

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ga.records.dor.retention_years` | 4 years | 2026-01-01 to open | US-GAS5-004 (Georgia Department of Revenue; A.2, direct artifact inspection, confidence high) |  |
| `ga.records.gdol.retention_years` | 7 years | 2026-01-01 to open | US-GAS5-005 (Georgia Department of Labor; A.3, direct artifact inspection, confidence high) | 34-8-121: full name, full SSN, hire/separation dates, separation reason, quarterly wages incl. non-cash and tips. |

Not configured in this release (open gap RQ-169): 10-1-393.8 read only via mirror (secondary source).

## GA.13 Live legal change

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ga.live.gdol_rules_2026` | proposed 2026-06-15, announced 2026-10-07: temporary substitute SSN, electronic separation notices, electronic posters, proposed all-employer DOL-4N e-file; adopted text/effective date not read | 2026-10-07 to open | US-GAS5-021 (Georgia Department of Labor; A.2, direct artifact inspection, confidence medium) |  |
| `ga.live.hb1157.status` | introduced, NOT enacted (would repeal local-mandate pre-emption) | 2026-01-01 to open | US-GAS5-017 (Georgia General Assembly; A.1, direct artifact inspection, confidence high) |  |
| `ga.live.hb463.status` | in force (signed 2026-05-11, retroactive 2026-01-01); levels withholding + assessment (rate), assessment + reporting (subtractions) | 2026-01-01 to open | US-GAS5-009 (Georgia General Assembly; A.1, second independent authority, confidence high) |  |

## GA.14 Authority worked examples (oracle values)

Each example is computed from the statutory parameters listed in this annex and checked against the result published by the authority. Amounts round half-up to the cent unless the line states another rule.

**Example GA-1: married filing jointly, semimonthly wages 2,000.00, 1 dependent (Employer's Tax Guide percentage method).**

| Line | Calculation | Result |
|---|---|---|
| Period standard deduction | 30,000 / 24, rounded to the cent | 1,250.00 |
| Period dependent allowance | 5,000 / 24, rounded to the cent | 208.33 |
| Taxable wages | 2,000.00 - 1,250.00 - 1 x 208.33 | 541.67 |
| Withholding | 541.67 x 4.99 % = 27.0293, half-up to the cent | 27.03 |

Computed result = published 27.03 (match). The withholding rate used applies to payments from 2026-05-11; payments to 2026-05-10 were withheld at the earlier withholding rate (GA.2).

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `ga.oracle.guide.example1.withholding` | 27.03 USD | 2026-01-01 to open | US-GAS5-001 (Georgia Department of Revenue; A.2, derived arithmetically, confidence high) | MFJ, semimonthly 2,000, 1 dependent: (2,000 - 1,250 - 208.33) x 0.0499 = 27.029 -> 27.03. Table check: Single weekly band 276-294: (294 - 288.46) x 0.0499 = 0.28 as printed. |

## GA.15 Special populations

- Domestic: GA withholding voluntary; UI at 1,000 cash/quarter, annual DOL-4 [US-GAS5-004, US-GAS5-006, US-GAS5-005].
- Agricultural: withholding not required; UI 10 in 20 weeks or 20,000/quarter [US-GAS5-004, US-GAS5-006].
- Minors: DOL-4103 work certificate under 18; DOL-4101 entertainment; newspaper carriers under 18 outside UI [US-GAS5-008, US-GAS5-006].
- Tipped: federal 2.13; tip subtraction at assessment; W-2 TP/TTOC; tips UI wages to FUTA extent [US-GAS5-016, US-GAS5-009, US-GAS5-003, US-GAS5-006].
- Clergy: ministers no GA withholding; church/religious order employees outside UI [US-GAS5-004, US-GAS5-006].
- Students: work-study and student nurses outside UI [US-GAS5-006].
- NRAs: withhold unless 8233 filed + copy to DOR [US-GAS5-004].
- Statutory employees: no state rule; SS-8 determinations accepted for UI [US-GAS5-006].
- Government: mostly reimbursing; elected officials/legislators/judiciary/National Guard outside UI [US-GAS5-006, US-GAS5-004].
- Military spouses: G-4 line 8b [US-GAS5-010]. Sole-proprietor family outside UI [US-GAS5-006]. RLA rail: GA OT field [US-GAS5-003].

## GA.16 Language

No language clause in 34-7-2 [US-GAP9L-001, US-GAP9L-003]; payslip English (US-OWN-006).

## GA.S Sources

The legal basis of each value (legal-basis register id, authority, source tier and verification method) is given in the row that carries it.


## Fact index

Every value above with its key, effective period and register id.

| Key | Value | Effective | Register id |
|---|---|---|---|
| `fed.ccpa.protected_weekly` | 217.50 | from 1970-07-01 | US-FEDS5-023 |
| `fed.minwage.hourly` | 7.25 | from 2009-07-24 | US-FEDS5-017 |
| `fed.tipped.cash_wage.hourly` | 2.13 | from 1996-08-20 | US-FEDS5-019 |
| `ga.garn.child_support.per_deduction_fee` | 3 | from 2026-01-01 | US-GAS5-019 |
| `ga.garn.child_support.setup_fee` | 25 | from 2026-01-01 | US-GAS5-019 |
| `ga.garn.creditor.max_percent` | 25 | from 2016-01-01 | US-GAS5-014 |
| `ga.leave.paid.mandate.exists` | False | from 2026-01-01 | US-GAS5-016 |
| `ga.live.gdol_rules_2026` | proposed 2026-06-15, announced 2026-10-07: temporary substitute SSN, electronic separation notices, electronic posters, proposed all-employer DOL-4N e-file; adopted text/effective date not read | from 2026-10-07 | US-GAS5-021 |
| `ga.live.hb1157.status` | introduced, NOT enacted (would repeal local-mandate pre-emption) | from 2026-01-01 | US-GAS5-017 |
| `ga.live.hb463.status` | in force (signed 2026-05-11, retroactive 2026-01-01); levels withholding + assessment (rate), assessment + reporting (subtractions) | from 2026-01-01 | US-GAS5-009 |
| `ga.local_mandates.preempted` | True | from 2026-01-01 | US-GAS5-017 |
| `ga.mass_separation.threshold_workers` | 25 | from 2026-01-01 | US-GAS5-020 |
| `ga.minwage.state.hourly` | 5.15 | from 2026-01-01 | US-GAS5-022 |
| `ga.newhire.report_days` | 10 | from 2026-01-01 | US-GAS5-012 |
| `ga.nonres.threshold` | withhold for nonresidents when more than 5% of wages or more than 5,000 is attributable to Georgia | from 2026-01-01 | US-GAS5-004 |
| `ga.nonres.threshold_amount` | 5,000 | from 2026-01-01 | US-GAS5-004 |
| `ga.nonres.threshold_percent` | 5 | from 2026-01-01 | US-GAS5-004 |
| `ga.oracle.guide.example1.withholding` | 27.03 | from 2026-01-01 | US-GAS5-001 |
| `ga.pay_frequency.rule` | at least semi-monthly in two equal periods per month; officers/superintendents/department heads monthly (34-7-2) | from 2026-01-01 | US-GAP9L-001 |
| `ga.payment.method` | money, check, direct deposit with consent, or payroll card (written fee explanation at hire or 30 days before; opt-out; one free access) - full net amount | from 2026-01-01 | US-GAP9L-001 |
| `ga.pit.conformity` | federal AGI start; IRC conformity as of 2026-01-01 (HB 1199); 401(k)/125/HSA/transit/GTL follow federal; no GA departure located | from 2026-01-01 | US-GAS5-023 |
| `ga.pit.overtime_subtraction.max` | 1,750 | from 2026-01-01 to 2028-12-31 | US-GAS5-009 |
| `ga.pit.rate.flat` | 4.99 | from 2026-01-01 | US-GAS5-009 |
| `ga.pit.tip_subtraction.max` | 1,750 | from 2026-01-01 | US-GAS5-009 |
| `ga.prevailing_wage.state_law.exists` | False | from 2026-01-01 | US-GAP51-002 |
| `ga.records.dor.retention_years` | 4 | from 2026-01-01 | US-GAS5-004 |
| `ga.records.gdol.retention_years` | 7 | from 2026-01-01 | US-GAS5-005 |
| `ga.report.annual.g1003` | W-2s and 1099-NEC with GA withholding due 31 Jan (TY2026: 2027-02-01), other 1099s 28 Feb; e-file if federal e-file or EFT; GTC entry, G-1003 Excel/CSV or EFW2 + GA RS (Rev 01/18); 1099s via IRIS XML only; no CF/SF | from 2026-01-01 | US-GAS5-003 |
| `ga.report.sui.dol4n` | DOL-4N due 30 Apr, 31 Jul, 31 Oct, 31 Jan; electronic for 25+ employees (portal <=100, CSV/Excel 100-15,000, SFTP >15,000); domestic-only annual DOL-4 by 31 Jan; corrections DOL-3C; temporary substitute SSN 000-00-000n allowed (correct within 30 days) | from 2026-01-01 | US-GAS5-005 |
| `ga.report.sui.efile_threshold_employees` | 25 | from 2026-01-01 | US-GAS5-005 |
| `ga.report.w2.rs_layout` | Rev 01/18: 248-267 state employer account; 274-275 state code; 276-286 state wages; 287-297 state tax; 298-307 period end; 331-339 withholding number | from 2018-01-01 | US-GAS5-011 |
| `ga.report.wh.payer_status` | lookback 12 months to prior 30 June: semi-weekly > 50,000 (EFT; G-7 Schedule B); monthly > 200/month (GA-V by 15th; G-7 quarterly); quarterly <= 200/month and > 800/yr; annual <= 800/yr by 31 Jan | from 2026-01-01 | US-GAS5-002 |
| `ga.report.wh.semiweekly_threshold` | 50,000 | from 2026-01-01 | US-GAS5-002 |
| `ga.sales_rep.commission_due_days` | 30 | from 2026-01-01 | US-GAS5-007 |
| `ga.separation_notice.delivery_days` | 3 | from 2026-01-01 | US-GAS5-007 |
| `ga.separation_notice.dol800` | DOL-800 (R-02-24) to every separated worker stating reason, on last day or within 3 days; electronic with e-signature allowed (Oct 2026 rules) | from 2026-01-01 | US-GAS5-007 |
| `ga.sui.admin_assessment.rate` | 0.06 | from 2024-01-01 to 2026-12-31 | US-GAS5-013 |
| `ga.sui.coverage` | 1 worker in 20 weeks or 1,500 quarter; agricultural 10 in 20 weeks or 20,000; domestic 1,000 quarter; 501(c)(3) 4 in 20 weeks; officers are employees; UI wages include 401(k) deferrals, tips (FUTA extent), board and lodging; exclude 125 premiums and employer 401(k) | from 2026-01-01 | US-GAS5-006 |
| `ga.sui.new_employer.rate.contribution` | 2.64 | from 2026-01-01 to 2026-12-31 | US-GAS5-013 |
| `ga.sui.new_employer.rate.contribution` | 2.7 | from 2027-01-01 | US-GAS5-013 |
| `ga.sui.new_employer.rate.total` | 2.7 | from 2026-01-01 to 2026-12-31 | US-GAS5-013 |
| `ga.sui.new_employer.rate.total` | 2.70 | from 2026-01-01 to 2026-12-31 | US-GAS5-013 |
| `ga.sui.wage_base` | 9,500 | from 2013-01-01 | US-GAW1B-001 |
| `ga.wh.certificate.form` | G-4 Rev. 06/03/26: letters A Single, B MFS or MFJ both working, C MFJ one working, D HoH; line 4 dependents; line 5 adjustment allowances (/5,000, remainder >2,500 rounds up); line 6 additional; 8a exempt; 8b MSRRA | from 2026-06-03 | US-GAS5-010 |
| `ga.wh.dependent_allowance` | 5,000 | from 2026-01-01 | US-GAS5-001 |
| `ga.wh.method` | tax tables (pp. 31-50) or percentage method (Tables E/F): (wages - period standard deduction - dependent allowance x n) x 4.99%; tables use top of band | from 2026-01-01 | US-GAS5-001 |
| `ga.wh.rate` | 4.99 | from 2026-05-11 | US-GAS5-009 |
| `ga.wh.rate` | 5.19 | from 2026-01-01 to 2026-05-10 | US-GA-001 |
| `ga.wh.std_deduction.mfj` | 30,000 | from 2026-01-01 | US-GAS5-001 |
| `ga.wh.std_deduction.single` | 15,000 | from 2026-01-01 | US-GAS5-001 |
| `ga.wh.supplemental.rate` | applicable income tax rate in effect when paid (4.99% from 2026-05-11); no separate table | from 2026-01-01 | US-GAS5-004 |
