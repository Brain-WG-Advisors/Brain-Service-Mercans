# -*- coding: utf-8 -*-
# exec'd by build_skill.py: writes SKILL.md, 13-gotchas.md and 07-qa-report.md. Statutory values are [[FACT:key=value]] tags.

GOTCHAS = r"""# Gotchas and traps

Each rule below is a point where a published source, a statute and the withholding instrument diverge, or where a dated value changes. The value, key, effective period and register id of every number are in the fact index at the end of this file.

## 1. Values that change over time (select by the date the rule keys on)

- **OASDI wage base:** USD [[FACT:fed.fica.oasdi.wage_base=184,500]] for wages paid 2026-01-01 to 2026-12-31 [US-FEDS5-005]; USD [[FACT:fed.fica.oasdi.wage_base=192,300]] from 2027-01-01 [US-FEDB5-401] (medium confidence). Never carry the 2026 figure into 2027.
- **Utah withholding allowance and phase-out:** base allowance USD [[FACT:ut.pit.base_allowance.single.annual=485]] single and USD [[FACT:ut.pit.base_allowance.married.annual=970]] married, phase-out rate [[FACT:ut.pit.phaseout.rate=1.3]] %, all with a period start of 2026-04-01 (Pub. 14, revision dated April 2026; the publication states no effective date) [US-UTPIT-003]. The flat rate is [[FACT:ut.pit.rate.flat=4.45]] % from 2026-01-01 [US-UTS5-001]. The 2026-01-01 to 2026-03-31 allowance values are an open gap (RQ-596); do not back-date the April figures.
- **Massachusetts PFML:** total [[FACT:ma.pfml.total.rate=0.88]] % in both years, but the split swaps. 2026: family [[FACT:ma.pfml.family.rate=0.18]] % and medical [[FACT:ma.pfml.medical.rate=0.7]] %. From 2027-01-01: family [[FACT:ma.pfml.family.rate=0.7]] % and medical [[FACT:ma.pfml.medical.rate=0.18]] % [US-MAS5-012]. PFML follows the earning date, not the payment date. Statute (Chapter 101 of 2026, s.45) and the Department differ on the transition. Configuration rule: [[FACT:practice.ma.pfml_split=Follow DFML: 2026 split unchanged, swap from 2027-01-01 (Ch. 101/2026 s.45 conflict recorded)]] [US-MAS5-012].
- **Ohio withholding tables** apply from [[FACT:oh.wh.tables.effective_from=2026-08-01]] [US-OHS5-001].
- **District of Columbia minimum wage:** USD [[FACT:dc.minwage.hourly=17.95]] per hour for hours worked to 2026-06-30, USD [[FACT:dc.minwage.hourly=18.40]] for hours worked from 2026-07-01 [US-DCS5-011]. Minimum wage follows hours worked, not the payment date: June hours paid in July stay at the June rate.
- **Selection rule:** tax and contribution values are selected by the payment date of the run; minimum-wage rates by hours worked on or after the effective date; Massachusetts PFML by earning date.

## 2. Statute is not the withholding instrument

| Jurisdiction | Rule for the engine | Register |
|---|---|---|
| SC | [[FACT:practice.sc.withholding_rates_2026=Use WH-1603 tables 0/3/6% for 2026 withholding; Act 110 rates (1.99%/5.21%) apply at the 2026 annual return only]]. Act 110 of 2026 must not be loaded into 2026 withholding. | US-SCS5-004 |
| WI | [[FACT:practice.wi.use_w166_tables=Withholding uses W-166 schedule (3.54/4.65/5.30/7.65%), not the assessment brackets (3.50/4.40/5.30/7.65%)]] | US-WIS5-010 |
| NE | [[FACT:practice.ne.use_circular_en_tables=Withholding uses DOR Circular EN tables (2026 2.26-4.60%), not the statutory 4.55% rate]] | US-NES5-018 |
| KS | [[FACT:practice.ks.kw100_header_stale=KW-100 header prints "wages paid on and after January 1, 2021" but figures are the 2024 values in force for 2026 (5.20/5.58%)]] | US-KSS5-001 |
| OH | [[FACT:practice.oh.flat_rate_vs_tables=TY2026 statute flat 2.75% but withholding tables graduated to 3.4% (5747.06 rule vs 5747.02 rate) - use the tables]] | US-OHS5-007 |
| CT | [[FACT:practice.ct.tables_vs_rules=DRS permits tables or TPG-211 rules; results differ up to 0.48/period; configured: DRS per-period tables up to each table maximum, TPG-211 rules above (CT.2, configuration decision of 2026-11-02)]] | US-CTS5-010 |
| OR | [[FACT:practice.or.federal_cap=Use 8,750 federal-tax subtraction cap (pp.6-7 formula); DOR publication also prints 8,500 and its example 1 is mis-computed]] | US-ORS5-009 |
| VA | [[FACT:practice.va.std_deduction_2027_not_modelled=Statute: 2027 standard deduction 9,200/18,400; do not model 2027 withholding until Virginia Tax publishes the 2027 formula (guide Rev. 10/26 says the deduction sunsets - wrong)]] | US-VAS5-018 |
| HI | [[FACT:practice.hi.2027_tables_pending=Act 24 SLH 2026 changes TY2027 brackets (new 13% top); 2027 withholding indeterminate until DOTAX issues 2027 Booklet A]] | US-HIS5-029 |
| AL | [[FACT:practice.al.fit_before_sit=AL state base deducts federal withholding: order FIT before AL SIT]] | US-ALS5-001 |
| GA | [[FACT:practice.ga.rate_change_2026=4.99% for TY2026 (5.19% before); 2027 0.125-point step conditional on OPB report of 2026-12-01]] | US-GAS5-009 |
| DC | [[FACT:practice.dc.2026_method_unpublished=D.C. Act 26-416 (emergency, from 2026-08-13) revoked personal exemptions; no 2026 withholding method published (D-4 under review)]]. The last published instruction is Notice 2022-08: [[FACT:dc.wh.notice_2022_08=apply current rate schedule with the federal allowance amount (no FR-230 after 2018); applying to 2026 is an inference]]; the payroll calculation must flag that result as an inference (open gap RQ-138). | US-DCS5-021, US-DCP51-002 |

The Wisconsin, Nebraska, Kansas and Ohio withholding tables are therefore not the statutory brackets: use the withholding instrument, and keep the statutory rate for the annual return.

## 3. Tips and overtime deductions (Public Law 119-21) are assessment items

- Federal: [[FACT:practice.fed.pl119_21_withholding=Do not reduce FIT withholding for tips/overtime deductions except through W-4 Step 4(b)]] [US-FEDS5-030]. Level: [[FACT:fed.plaw119_21.tips_overtime.level=assessment; withholding only via W-4 Step 4(b); employer reporting W-2 TP/TT/14b; FICA unchanged]].
- MI: [[FACT:practice.mi.tips_ot_deduction_level=MI 2025 PA 24 tips/overtime deduction (TY2026-2028) is ASSESSMENT only; no change to withholding]] [US-MIS5-017].
- IA: [[FACT:ia.pit.obbba=tips, overtime, car-loan interest conformed at ASSESSMENT only (no withholding allowance); senior deduction (up to 6,000) may be claimed as an IA W-4 allowance]] [US-IAS5-019].
- DC: [[FACT:dc.pit.obbba_deductions=disallowed TY2025; allowed as DC deductions from TY2026; operating level assessment only (no withholding change)]] [US-DCS5-021].
- AL and GA: assessment only [US-ALS5-004], [US-GAS5-009]. HI: tips deduction conformed at assessment, overtime deduction not conformed [US-HIS5-029]; the withholding level in Hawaii is not established from an official source.

## 4. Channels and identifiers that are easy to mix up

- **Louisiana: LAWATS is not the wage-report channel.** The quarterly UI wage report is filed through the Louisiana Workforce Commission online services: [[FACT:la.report.sui.quarterly=@@LA@@]] [US-LAS5-007]. LAWATS appears only as the online power-of-attorney portal: [[FACT:sir.la.ui.agent_authorization=Online Power of Attorney in LAWATS]] [US-LAP52-005]. Withholding L-1: [[FACT:la.report.wh.l1=L-1 quarterly, electronic (LaTAP/software), zero returns required, due Apr 30 / Jul 31 / Oct 31 / Jan 31; payment quarterly < 500/month average, monthly 500 to < 5,000, semi-monthly >= 5,000]] [US-LAS5-003]. Annual: [[FACT:la.report.annual.l3=L-3 + W-2s due first business day after January 31 (30 days on closure); electronic mandatory at 50+ W-2s via LaWage; no magnetic media/CD; state boxes 16-18]] [US-LAS5-009].
- **Hawaii HRS 487J:** [[FACT:psl.hi.ssn.rule=Not required on the statement; section 487J-2 bars making an entire SSN available to the general public and printing an entire SSN on mailed materials, except employer-to-employee communications or where the individual requests it]] [US-HIS5-028]. The employer-to-employee mailing exemption applies; a full number must not appear in public or third-party material.
- **IRS Tax Withholding Estimator** is not an employer engine or oracle: [[FACT:practice.fed.estimator_not_oracle=IRS Tax Withholding Estimator is not an employer engine or oracle]] [US-FED-021].
- **North Dakota booklet:** the Section 2 worked example is a recorded defect; configure from the method and table [US-NDS5-001].

## 5. Federal FICA

- **Additional Medicare Tax uses its own year-to-date base.** Rate [[FACT:fed.fica.addl_medicare.rate=0.9]] % on wages paid above USD [[FACT:fed.fica.addl_medicare.withholding_threshold=200,000]] in the calendar year, regardless of filing status; employee only, no employer match [US-FEDS5-005]. It is computed on the employee's cumulative calendar-year Medicare wages from the employer, separate from the OASDI base: Medicare wages are not capped (key `fed.fica.medicare.wage_base.capped`) while OASDI stops at its annual base. Do not reuse the OASDI year-to-date accumulator, and do not reset it on a filing-status basis.
- OASDI is capped by its annual base (section 1); Medicare is not.

## 6. Scope

- Independent contractors and Form 1099-NEC reporting are out of scope [US-OWN-008]. Employers in scope are private-sector employers; workers are common-law employees.
- Prevailing-wage and certified payroll reports are an informational overlay only [US-OWN-009].
- Territories are not covered; the jurisdiction set is the 50 States and the District of Columbia [US-OWN-002].
"""

QA = r"""# QA report

The United States package (v1.0) reached QA pass in every artifact. Review verdicts come from independent audits of each artifact.

| Artifact | Final review round | Verdict | Reviewed on | Stated accuracy |
|---|---|---|---|---|
{rows}

## Validation exemptions recorded by the owner

- US-OWN-010: checks on validation of filing files against an official norm, validator or plugin are exempted for the Report Specifications; no machine-callable national validator exists (SSA AccuWage validates EFW2 only inside an authenticated session; State validators are State-specific).
- US-OWN-011: three narrowly scoped content-check findings are exempted (WTC row for W-2 box 12 code TA valid only from 2026-07-04; a Kansas guide id that matches a wage-type code pattern; the Georgia SUI wage-type wording).

## Limitations that carry into this skill

- Open research gaps and documented limitations are listed in `14-known-gaps.md`; each is printed in the references as 'Not configured in this release (open gap id)'.
- No real filed sample exists for any Report Specification; every return layout is derived from official authority pages and file specifications.
- The payslip has no tested US sample; State pay-statement rules are statute readings.

## Source-change log

- 2026-11-04: skill re-synced after the CCG and SIR citation rebuild (practice rows cite their additional rows, two social-security citations, SIR Form 940 and Ohio school-district cells).
- 2026-11-04: skill re-synced after the run-close rebuilds (practice notes GA/SC/NE/OH/CT, data dictionary fields er.supplemental_wage_method and er.state_sui_rate, ma.pfml.rate.selection_basis, superseded legal-basis rows re-pointed to their successors); 13 reference files changed.
- 2026-11-04: skill re-synced after the CCG rebuild (m10 payslip wording, annex_LA channel wording, annex_DC wording, annex_MS payslip gap PSL-RQ-14, m04 Hawaii row), the WTC wording fix and the UT/MS/LA fact fixes; references regenerated.
- 2026-11-04: skill references flattened from the approved CCG (13 modules, federal, multistate and 51 jurisdiction references), WTC, DD, SIR, 20 Report Specifications and the payslip generator at package version 1.0. Append one line here whenever any source document changes, even when a full re-sync is deferred.
"""

SKILL = r"""---
name: payroll-compliance-united-states
description: United States private-sector payroll compliance for 2026 (with dated 2027 values) across the federal layer and all 50 States plus the District of Columbia - IRS federal income tax withholding (Pub. 15-T), FICA (OASDI, Medicare, Additional Medicare), FUTA, Forms W-2, 941, 940 and State withholding, State unemployment insurance, paid family and medical leave programmes, State minimum wage and pay-statement rules, multistate residence and reciprocity rules, wage type catalogue, data dictionary, Report Specifications, third-party filing hand-off and payslip. Currency USD. Contractors and Form 1099-NEC are out of scope. Use for any question about US payroll rates, thresholds, filings, wage types, master data or payslip content, federal or by State.
---

# United States payroll compliance - router

**ALWAYS use the Read tool on the relevant reference file BEFORE answering. Do NOT answer US-specific rates, wage bases, brackets or deadlines from general knowledge.** The United States has no single payroll regime: a federal layer (IRS, SSA, DOL) sits under 51 State layers, and many values change mid-year or between 2026 and 2027.

The reference files are long. Read with `offset`/`limit` or Grep for the heading or the fact key (for example `fed.fica.oasdi.wage_base`) instead of loading a whole file.

## Routing

| Topic | Read |
|---|---|
| Federal income tax withholding, FICA, FUTA, W-2/W-4/941/940, special populations | `references/10-federal.md` |
| Residence vs work-location sourcing, reciprocity, multistate employees | `references/11-multistate.md` |
| One State (income tax withholding, SUI, PFML, minimum wage, pay statement, new hire, filings, local taxes) | `references/12-states/<XX>.md` (index: `references/12-states.md`) |
| Cross-cutting configuration guide, modules 1-13, worked examples, practices | `references/01-ccg.md` then `references/01-ccg/<module>.md` |
| Wage types (global baseline plus US additions), tax and contribution flags | `references/02-wtc.md` |
| Statutory integrations and the third-party provider hand-off | `references/03-sir.md` |
| Report Specifications (IRS, SSA, State DOR, UI, PFML, local, new hire) | `references/04-reports-spec.md` then `references/04-reports-spec/<report>.md` |
| Data dictionary, master data, option mappers | `references/05-data-dictionary.md` |
| Payslip generator and pay-statement content | `references/06-payslip.md` |
| QA results, exemptions, limitations, source-change log | `references/07-qa-report.md` |
| Traps: statute vs withholding table, assessment-only items, channels | `references/13-gotchas.md` |
| Open gaps and the US-OWN-001..011 owner decisions | `references/14-known-gaps.md` |
| Legal basis rows (authority, article, URL, effective dates) | `references/15-sources.md` |

## How to answer

1. Read the reference first; quote the value verbatim with its unit.
2. Cite the register id in brackets (for example `[US-FEDS5-005]`) and give the effective period. Every content reference file (CCG modules, federal, multistate, State, WTC, SIR, Report Specification, data dictionary and payslip files) ends with a fact index listing key, value, effective period and register id; the index files, QA report, gaps and sources files have none.
3. A value that changes in time is multi-period: give the period asked for. Tax and contribution values are selected by the payment date of the run; minimum-wage rates by hours worked on or after the effective date; Massachusetts PFML by earning date. Example: OASDI wage base USD [[FACT:fed.fica.oasdi.wage_base=184,500]] (2026) and USD [[FACT:fed.fica.oasdi.wage_base=192,300]] (2027); Utah allowance schedule applies from 2026-04-01; Massachusetts PFML split changes from 2027-01-01.
4. If the reference prints 'Not configured in this release (open gap id)', say the point is not established and name the gap; never estimate. Re-verify time-varying values against the authority before relying on them in a live run.

## Scope and limits

- In scope: private-sector employers, common-law employees, the federal layer, the 50 States and the District of Columbia, State and local payroll levies listed in the references.
- Out of scope: independent contractors and Form 1099-NEC reporting [US-OWN-008]; territories; public-sector employers; certified payroll production (informational flag only [US-OWN-009]).
- Filings to States are made through a third-party provider hand-off, not by system-to-system integration with each agency (`references/03-sir.md`).
- Open gaps, TY2025-labelled federal items and owner decisions: `references/14-known-gaps.md`.

## Design clarifications

1. **Withholding follows the withholding instrument, not the statute.** South Carolina Act 110 rates apply to the 2026 annual return only; Wisconsin, Nebraska, Kansas and Ohio withholding tables are not the statutory brackets. See `references/13-gotchas.md` section 2.
2. **Tips and overtime deductions (Public Law 119-21) reduce assessment, not withholding,** except through federal Form W-4 Step 4(b) (section 3 of the gotchas).
3. **District of Columbia has no published 2026 withholding method.** The last published instruction is Notice 2022-08; applying it to 2026 is an inference the payroll calculation must flag (`references/12-states/DC.md`, gap RQ-138).
4. **Louisiana LAWATS is the power-of-attorney portal, not the wage-report channel;** the UI wage report goes through the Louisiana Workforce Commission online services [US-LAS5-007].
5. **Hawaii HRS 487J** bars public display and mailing of a full SSN, except employer-to-employee communications.
6. **Additional Medicare Tax runs on its own calendar-year base** with its own threshold, employee-only.
7. **Every dated value is multi-period.** Do not carry 2026 values into 2027 or the reverse. The District of Columbia minimum wage follows hours worked, not the payment date.
8. **Contractors and Form 1099-NEC are out of scope.**
"""
