# US Compliance Mandate (United States of America)

**Date:** 2026-10-29  
**Author:** compliance-scaffolder  
**Status:** `mandate_status: pending_research`. No artifact may leave `scaffolded` until this mandate is sealed.  
**BASE:** `C:/Users/instituto/Documents/brain-service/Research Pipeline/USA/US-compliance`  
**Contract:** `_pipeline/build-manifest.json` (schema 1.4.0)

## Parameters

| Parameter | Value | Basis |
|---|---|---|
| COUNTRY / CODE | United States of America / `US` | ISO 3166-1 alpha-2 |
| CURRENCY | USD (payroll and reporting) | ISO 4217; statutory confirmation US-MQ-02 |
| CURRENCY_MINOR_UNITS | 2 | ISO 4217 exponent |
| ROUNDING | payment 0.01, accounting 0.01 (working values); whole-dollar rules pending | US-MQ-02, US-MQ-20..70 |
| YEAR | 2026; next_year 2027 | calendar-year basis pending US-MQ-01 |
| LANGUAGE | en first build (working assumption); es documented seam | G-LANG pending US-MQ-03 |

## Scope facts (owner decisions, not legal findings)

- **Employers:** private sector. **Workers:** common-law employees; independent contractors / Form 1099-NEC **OUT OF SCOPE** (owner instruction, 2026-10-29). Special populations: US-MQ-12.
- **Filing channel:** statutory filings (federal and state) go through a **third-party filing provider; no ADP integration** (owner, biweekly 2026-10-21). The SIR covers the provider handoff, not direct authority submission. Authorisation instruments: US-MQ-09.
- **Structure:** a common FEDERAL layer + a MULTISTATE routing domain + 51 jurisdictions (50 states + DC). Jurisdiction ordering: US-MQ-13. Package shape: US-MQ-14.

## Tier verdict (repeat verbatim in CCG m01, scope_manifest.json and the QA report)

> Overall T4 (provisional: citations pending US-MQ-04, US-MQ-10 and US-MQ-20..70). Employer-operation test: T4 requires a second independent calculation AND a separate remittance/return to a second authority. The employer computes federal income-tax withholding, FICA and FUTA for the IRS (Forms 941/940, W-2), and in every state that taxes wages computes a SEPARATE state withholding under that state's own tables/certificate and remits it to the state revenue department on a state return; state unemployment insurance is likewise a separate calculation on a separate quarterly report to a state agency. Nothing is absorbed into the federal deduction (contrast Switzerland, StHG Art. 36a Abs. 1, where one deduction discharges all levels). This is the Quebec pattern repeated for up to 51 jurisdictions, plus a local layer (city/county/school district) that is T4 where remitted separately and T3 where piggybacked on the state return. Consequence: the federal core and each jurisdiction are declared and scoped as parallel layers, and the multistate domain routes each employee to one or more of them. No US instrument is on disk yet; the candidate instruments to confirm are IRC chapter 24 (federal withholding), chapters 21/23 (FICA/FUTA) and each state's withholding and UI statutes.

| Domain | Tier | Why |
|---|---|---|
| federal_income_tax | **T2** | One authority (IRS), progressive tables, one certificate (W-4); NRA and supplemental regimes sit inside one calculation. |
| fica_social_security_medicare | **T2** | Federal, uniform rates, one authority; wage base indexed (US-MQ-06). |
| futa | **T3** | Federal return, but the effective rate depends on the state UI credit and credit-reduction states: a cross-layer dependency (US-MQ-04). |
| state_income_tax | **T4** | Second independent calculation plus a separate return to a second authority (state DoR) in every wage-taxing state; T1 ('none') in states without wage tax, which states pending per jurisdiction. |
| local_income_tax | **T4** | T4 where a locality/collector receives a separate return; T3 where piggybacked on the state return. Mixed per state, pending US-MQ-20..70. |
| state_unemployment_insurance | **T4** | Separate state agency, separate quarterly wage report and remittance; employer experience rate is per-employer master data. |
| sdi_tdi_pfml | **T4-shaped** | T4 where a separate agency/return exists, T3 where filed with UI, data-problem where funded through a private insurer. Does not uniformly meet the discriminator. |
| workers_compensation | **data-problem** | Mostly insurer premiums outside payroll; payroll-deducted only in some state-fund states. Variability axis is the insurer/state fund, not a statutory rate table (US-MQ-05). |
| multistate | **T4** | Routing layer that selects which T4 jurisdictions apply per employee (work state, residence state, reciprocity, convenience rule, SUI localization), US-MQ-10. |
| labour_code | **T3** | Federal floor (FLSA) plus state wage-payment rules; one calculation, state-keyed fields. |
| payslip_statute | **T3** | No federal pay-statement mandate assumed; state-by-state content rules (US-MQ-03). |
| statutory_reporting | **T4** | Federal 941/940/W-2 plus per-state withholding, reconciliation, UI and local returns; submitted via third-party provider (US-MQ-09). |
| leave | **T3** | State and local paid-sick-leave rules, state/locality-keyed. |
| termination | **T3** | State final-pay deadlines, state-keyed. |
| benefits_in_kind | **T2** | Federal fringe rules; state conformity is data. |
| deductions_garnishments | **T3** | Federal CCPA limits plus state variations. |
| collective_agreements | **T1** | Provisional: no sector extension mechanism assumed, pending US-MQ-07. |
| indexation | **T3** | Annual federal Revenue Procedure + SSA wage base + state wage-base indexation (US-MQ-06 and per state). |
| payroll_data_protection | **T2** | SSN handling rules, mostly uniform. |
| live_legal_change | **T3** | 53 parameter sets (federal + multistate + 51) change every year. |

**Sub-national key:** work_location_jurisdiction (state + locality down to school district / PSD); residence_jurisdiction (state + locality down to school district); sui_state (result of the localization test, US-MQ-10). Checked below the state tier: several local wage taxes are residence-based or school-district-based, so a state-only key cannot express them. Work and residence are separate keys because the multistate rules diverge on them.

## Federal and cross-cutting questions (the seven mandate questions + oracle, scope, owner)

Every answer needs a citation; none is on disk, so all are `pending_research`. Owner questions (US-MQ-11, 13, 14) are answered by the owner and recorded the same way.

### Q1 — Tax year
**Status:** `pending_research`  
**Question id:** `US-MQ-01`  
**Asked:** 2026-10-29  
**Question:** Which instruments fix the period of federal employment-tax reporting (Form W-2 / 941 / 940) and of state wage-withholding reconciliation, and may an employer with a non-calendar fiscal year report employment taxes on that fiscal year instead of the calendar year?  
**What would answer it:** Federal: the IRC withholding/reporting provisions and the Treasury regulation on the W-2 period, plus the Form 941/940 instructions (IRS). One state DoR annual-reconciliation instruction as a check that states follow the calendar year.  
**Blocks:** CCG, SCOPE, RSPEC, DD, WTC, SIR, PSL, SKILL; Sets YEAR=2026 (next_year 2027) for every artifact and every jurisdiction annex.  
**Answer:** _pending_  
**register_id:** _pending_

### Q2 — Currency, minor units and rounding
**Status:** `pending_research`  
**Question id:** `US-MQ-02`  
**Asked:** 2026-10-29  
**Question:** Which instrument requires federal employment-tax returns and W-2s to be stated in USD, and what rounding rules apply (a) inside the federal withholding computation (Pub. 15-T methods: rounding of wages or withholding to whole dollars?) and (b) on returns (optional whole-dollar rounding on Forms 941/940/W-2)? Is there any rule fixing a payment unit coarser than USD 0.01?  
**What would answer it:** IRS Pub. 15-T (computation rounding), Form 941/940 instructions (whole-dollar option), General Instructions for Forms W-2 and W-3. State-specific rounding is asked in each jurisdiction question (US-MQ-20..70).  
**Blocks:** CCG, WTC, PSL, RSPEC, DD; rounding.payment / rounding.accounting / rounding.rule; WTC and payslip number formats.  
**Answer:** _pending_  
**register_id:** _pending_

### Q3 — Official languages and what fixes document language (G-LANG)
**Status:** `pending_research`  
**Question id:** `US-MQ-03`  
**Asked:** 2026-10-29  
**Question:** Is there a federal or state instrument designating an official language that binds employer documents, and which instrument (if any) fixes the language of (a) the employee pay statement / wage statement and (b) authority-facing filings (IRS, SSA, state DoR, state UI agency)? Which states require wage or pay-rate notices in the employee's primary language, and are bilingual documents permitted? If no statute fixes payslip language, state the non-statutory constraint that governs instead.  
**What would answer it:** Federal: any official-language instrument and the FLSA recordkeeping rule (29 CFR Part 516) for whether a pay statement is federally required at all; per state: the pay-statement content provision and any primary-language notice provision (collected under US-MQ-20..70, summarised here).  
**Blocks:** CCG, PSL, DD; languages.payslip_rule / authority_facing_rule / seams (es candidate); PSL language tabs.  
**Answer:** _pending_  
**register_id:** _pending_

### Q4 — Sub-national wrinkle: confirm the T4 discriminator
**Status:** `pending_research`  
**Question id:** `US-MQ-04`  
**Asked:** 2026-10-29  
**Question:** Confirm with citations that (a) federal income-tax withholding, FICA and FUTA are computed and remitted to the IRS on federal returns (941/944, 940), and (b) state income-tax withholding and state unemployment insurance are separate calculations remitted to separate state authorities on separate returns, i.e. no state tax is absorbed into the federal deduction. Does the FUTA credit for state UI contributions (and credit-reduction states) create a calculation dependency between the federal and state layers?  
**What would answer it:** IRC chapter 24 (wage withholding) and chapters 21/23 (FICA/FUTA) including the FUTA credit provision; one representative state withholding statute and one state UI statute.  
**Blocks:** CCG, SCOPE, RSPEC, DD, WTC, SIR, PSL, SKILL; tier.overall=T4 (provisional until answered); fan-out design of the whole build.  
**Answer:** _pending_  
**register_id:** _pending_

### Q5 — Devolved payroll-adjacent domains (federal list)
**Status:** `pending_research`  
**Question id:** `US-MQ-05`  
**Asked:** 2026-10-29  
**Question:** Which payroll-adjacent obligations sit outside federal income tax/FICA/FUTA and must be flagged in or out of scope: state disability (SDI/TDI), paid family and medical leave (PFML) contributions, long-term-care payroll premiums, transit / workforce-training / job-development levies, workers' compensation employee deductions where a state fund collects through payroll, new-hire reporting, child-support income-withholding orders (federal IWO form, CCPA limits)? Give the federal anchor for each and the list of states where each exists.  
**What would answer it:** CCPA (15 U.S.C. 1671-1677) and the federal IWO form; the federal new-hire reporting provision; per-state instruments collected under US-MQ-20..70.  
**Blocks:** CCG, SCOPE, WTC, DD; Every OUT-OF-SCOPE tag agent 3 writes reconciles against this list.  
**Answer:** _pending_  
**register_id:** _pending_

### Q6 — Indexation (federal)
**Status:** `pending_research`  
**Question id:** `US-MQ-06`  
**Asked:** 2026-10-29  
**Question:** Name each federal indexation mechanism that moves 2026/2027 payroll parameters, with the index, its caliber, the trigger and the step: (a) income-tax brackets / standard deduction (which CPI variant, which annual Revenue Procedure); (b) the Social Security contribution and benefit base (which wage index, which SSA announcement); (c) other indexed federal payroll limits (retirement deferrals, HSA, fringe exclusions).  
**What would answer it:** The IRC inflation-adjustment provision plus the IRS Revenue Procedure for 2026 (and 2027 when published); the Social Security Act provision on the contribution base plus the SSA announcement.  
**Blocks:** CCG, WTC, DD; Agent 2 G-DERIVE proofs; 2027 next_year refresh.  
**Answer:** _pending_  
**register_id:** _pending_

### Q7 — Collective agreements
**Status:** `pending_research`  
**Question id:** `US-MQ-07`  
**Asked:** 2026-10-29  
**Question:** Does any US instrument extend a collective agreement's pay terms to non-signatory employers in a sector, or do CBAs bind only the certified bargaining unit? Are federal/state prevailing-wage regimes (public-works contracts) in scope for a private-sector payroll build? Which sectors, if any, are in scope?  
**What would answer it:** NLRA (29 U.S.C. 151 ff.) on exclusive representation; Davis-Bacon Act; per-state prevailing-wage statutes under US-MQ-20..70.  
**Blocks:** CCG, SCOPE; collective_agreements tier and CCG m11 scope.  
**Answer:** _pending_  
**register_id:** _pending_

### Oracle — Oracle for Stage 9b
**Status:** `pending_research`  
**Question id:** `US-MQ-08`  
**Asked:** 2026-10-29  
**Question:** Which official engine or official worked examples will serve as the oracle for federal withholding (worked examples in IRS Pub. 15-T, or an IRS calculator), and is there an official per-state equivalent (state DoR withholding calculator or worked examples) for each jurisdiction?  
**What would answer it:** IRS Pub. 15-T 2026 (and whether the IRS Tax Withholding Estimator qualifies as an engine); per-state DoR calculators listed under US-MQ-20..70.  
**Blocks:** CCG, SCOPE; oracle block (Stage 2 check 7, Stage 9b).  
**Answer:** _pending_  
**register_id:** _pending_

### Scope fact — Third-party filing provider (SIR)
**Status:** `pending_research`  
**Question id:** `US-MQ-09`  
**Asked:** 2026-10-29  
**Question:** Scope fact (owner, biweekly 2026-10-21): statutory filings go through a THIRD-PARTY filing provider; no ADP integration. Research: which instruments authorise a third party to file and deposit federal employment taxes for the employer (reporting-agent authorisation, Form 8655 and its Revenue Procedure), what liability stays with the employer, and what is each state's equivalent authorisation (POA / agent form) for withholding and UI filings? Owner: which provider, and what input format does it accept?  
**What would answer it:** IRS reporting-agent Revenue Procedure and Form 8655 instructions; per-state POA/agent forms under US-MQ-20..70; owner answer for the provider.  
**Blocks:** SIR, RSPEC, SCOPE; SIR scope: Mercans produces provider input files, not authority submissions.  
**Answer:** _pending_  
**register_id:** _pending_

### Q4 — Multi-state domain
**Status:** `pending_research`  
**Question id:** `US-MQ-10`  
**Asked:** 2026-10-29  
**Question:** For employees who live in one state and work in another (or in several): what decides (a) which state's income tax is withheld (work-state sourcing vs residence), (b) reciprocity agreements (which state pairs), (c) resident credit for tax paid to the work state and whether the employer must withhold the difference, (d) convenience-of-the-employer rules (which states), (e) day/dollar thresholds before nonresident withholding starts (which states, what threshold), (f) the SUI localization tests (localized / base of operations / direction and control / residence) and the reciprocal coverage election? Is there any federal statute limiting state taxation of mobile employees?  
**What would answer it:** The uniform UI localization provision as enacted in a state UI law; each state's nonresident-withholding provision and reciprocity agreement text (collected under US-MQ-20..70); any limiting federal statute in Title 4 U.S.C.  
**Blocks:** CCG, DD, WTC, SCOPE; multistate design and DD master-data keys (work_location_jurisdiction, residence_jurisdiction, sui_state).  
**Answer:** _pending_  
**register_id:** _pending_

### F68 — Validation exemptions (owner)
**Status:** `pending_research`  
**Question id:** `US-MQ-11`  
**Asked:** 2026-10-29  
**Question:** Owner question: for checks C34-C36, C48, C50, C57 and C71, is there a machine-readable norm (eCFR / state codes), an authority validator (SSA AccuWage for EFW2, IRS MeF schemas for 94x), an identifier plugin (SSN/ITIN/EIN/state account numbers) and a code table (W-2 Box 12/14, state codes) for each jurisdiction? For each missing item, will the owner provide the support or record a validation_exemptions entry (reason, official URL, decided_on)?  
**What would answer it:** Owner decision, informed by the IRS/SSA technical specifications located by agent 2.  
**Blocks:** RSPEC, DD, SIR; Without it C34-C36, C48, C50, C57, C71 fail at Stage 9.  
**Answer:** _pending_  
**register_id:** _pending_

### Scope — Employee population in scope
**Status:** `pending_research`  
**Question id:** `US-MQ-12`  
**Asked:** 2026-10-29  
**Question:** Owner scope decision recorded 2026-10-29: private-sector employers, common-law employees; independent contractors / Form 1099-NEC out of scope. Research: which special populations must the federal layer still treat distinctly (nonresident aliens, household employees, agricultural employees on Form 943, clergy, statutory employees, student FICA exemption, employees abroad), and which are in or out for this build?  
**What would answer it:** IRS Pub. 15, 15-A, 15-T and 51; owner confirmation per population (L10 coverage matrix).  
**Blocks:** SCOPE, CCG, WTC; SCOPE employment_types and the L10 special-population matrix.  
**Answer:** _pending_  
**register_id:** _pending_

### Scope — Jurisdiction priority (owner)
**Status:** `pending_research`  
**Question id:** `US-MQ-13`  
**Asked:** 2026-10-29  
**Question:** Owner question: which states have active or committed clients (Yoyo / BAU master list), so the 51 jurisdiction fan-outs can be ordered? Unanswered as of the 2026-09-29 weekly and the 2026-10-21 biweekly.  
**What would answer it:** Owner answer.  
**Blocks:** CCG; Build order of the 51 jurisdiction annexes.  
**Answer:** _pending_  
**register_id:** _pending_

### Scope — Package shape (owner)
**Status:** `pending_research`  
**Question id:** `US-MQ-14`  
**Asked:** 2026-10-29  
**Question:** Owner question: one US package (federal core + multistate module + one annex per jurisdiction, Canada precedent) or one package per state? The T4 verdict requires every parallel layer to be declared and staffed; it does not by itself fix the packaging.  
**What would answer it:** Owner answer (PROPOSTA-ESTRUTURA.md section 6).  
**Blocks:** CCG, SCOPE, RSPEC, DD, WTC, SIR, PSL, SKILL; artifacts[].units and package layout.  
**Answer:** _pending_  
**register_id:** _pending_

## Per-jurisdiction questions (Q4-Q7 per state; one source-hunter each)

Ids are stable, assigned in alphabetical order of the USPS code (US-MQ-20 = AK ... US-MQ-70 = WY), never renumbered or reused. US-MQ-15..19 are unassigned and reserved. Sources land in `00-official-sources/ccg-sources/{JUR}/`.

### AK — Alaska
**Status:** `pending_research`  
**Question id:** `US-MQ-20`  
**Asked:** 2026-10-29  
**Question:** For Alaska (AK), with citations and effective dates for 2026 (and 2027 if published): (1) does Alaska tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the Alaska revenue department withholding statute/guide and 2026 employer tables; the Alaska unemployment-insurance agency's wage-base and rate notice; the Alaska pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### AL — Alabama
**Status:** `pending_research`  
**Question id:** `US-MQ-21`  
**Asked:** 2026-10-29  
**Question:** For Alabama (AL), with citations and effective dates for 2026 (and 2027 if published): (1) does Alabama tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the Alabama revenue department withholding statute/guide and 2026 employer tables; the Alabama unemployment-insurance agency's wage-base and rate notice; the Alabama pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### AR — Arkansas
**Status:** `pending_research`  
**Question id:** `US-MQ-22`  
**Asked:** 2026-10-29  
**Question:** For Arkansas (AR), with citations and effective dates for 2026 (and 2027 if published): (1) does Arkansas tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the Arkansas revenue department withholding statute/guide and 2026 employer tables; the Arkansas unemployment-insurance agency's wage-base and rate notice; the Arkansas pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### AZ — Arizona
**Status:** `pending_research`  
**Question id:** `US-MQ-23`  
**Asked:** 2026-10-29  
**Question:** For Arizona (AZ), with citations and effective dates for 2026 (and 2027 if published): (1) does Arizona tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the Arizona revenue department withholding statute/guide and 2026 employer tables; the Arizona unemployment-insurance agency's wage-base and rate notice; the Arizona pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### CA — California
**Status:** `pending_research`  
**Question id:** `US-MQ-24`  
**Asked:** 2026-10-29  
**Question:** For California (CA), with citations and effective dates for 2026 (and 2027 if published): (1) does California tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the California revenue department withholding statute/guide and 2026 employer tables; the California unemployment-insurance agency's wage-base and rate notice; the California pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### CO — Colorado
**Status:** `pending_research`  
**Question id:** `US-MQ-25`  
**Asked:** 2026-10-29  
**Question:** For Colorado (CO), with citations and effective dates for 2026 (and 2027 if published): (1) does Colorado tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the Colorado revenue department withholding statute/guide and 2026 employer tables; the Colorado unemployment-insurance agency's wage-base and rate notice; the Colorado pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### CT — Connecticut
**Status:** `pending_research`  
**Question id:** `US-MQ-26`  
**Asked:** 2026-10-29  
**Question:** For Connecticut (CT), with citations and effective dates for 2026 (and 2027 if published): (1) does Connecticut tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the Connecticut revenue department withholding statute/guide and 2026 employer tables; the Connecticut unemployment-insurance agency's wage-base and rate notice; the Connecticut pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### DC — District of Columbia
**Status:** `pending_research`  
**Question id:** `US-MQ-27`  
**Asked:** 2026-10-29  
**Question:** For District of Columbia (DC), with citations and effective dates for 2026 (and 2027 if published): (1) does District of Columbia tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the District of Columbia revenue department withholding statute/guide and 2026 employer tables; the District of Columbia unemployment-insurance agency's wage-base and rate notice; the District of Columbia pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### DE — Delaware
**Status:** `pending_research`  
**Question id:** `US-MQ-28`  
**Asked:** 2026-10-29  
**Question:** For Delaware (DE), with citations and effective dates for 2026 (and 2027 if published): (1) does Delaware tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the Delaware revenue department withholding statute/guide and 2026 employer tables; the Delaware unemployment-insurance agency's wage-base and rate notice; the Delaware pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### FL — Florida
**Status:** `pending_research`  
**Question id:** `US-MQ-29`  
**Asked:** 2026-10-29  
**Question:** For Florida (FL), with citations and effective dates for 2026 (and 2027 if published): (1) does Florida tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the Florida revenue department withholding statute/guide and 2026 employer tables; the Florida unemployment-insurance agency's wage-base and rate notice; the Florida pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### GA — Georgia
**Status:** `pending_research`  
**Question id:** `US-MQ-30`  
**Asked:** 2026-10-29  
**Question:** For Georgia (GA), with citations and effective dates for 2026 (and 2027 if published): (1) does Georgia tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the Georgia revenue department withholding statute/guide and 2026 employer tables; the Georgia unemployment-insurance agency's wage-base and rate notice; the Georgia pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### HI — Hawaii
**Status:** `pending_research`  
**Question id:** `US-MQ-31`  
**Asked:** 2026-10-29  
**Question:** For Hawaii (HI), with citations and effective dates for 2026 (and 2027 if published): (1) does Hawaii tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the Hawaii revenue department withholding statute/guide and 2026 employer tables; the Hawaii unemployment-insurance agency's wage-base and rate notice; the Hawaii pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### IA — Iowa
**Status:** `pending_research`  
**Question id:** `US-MQ-32`  
**Asked:** 2026-10-29  
**Question:** For Iowa (IA), with citations and effective dates for 2026 (and 2027 if published): (1) does Iowa tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the Iowa revenue department withholding statute/guide and 2026 employer tables; the Iowa unemployment-insurance agency's wage-base and rate notice; the Iowa pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### ID — Idaho
**Status:** `pending_research`  
**Question id:** `US-MQ-33`  
**Asked:** 2026-10-29  
**Question:** For Idaho (ID), with citations and effective dates for 2026 (and 2027 if published): (1) does Idaho tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the Idaho revenue department withholding statute/guide and 2026 employer tables; the Idaho unemployment-insurance agency's wage-base and rate notice; the Idaho pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### IL — Illinois
**Status:** `pending_research`  
**Question id:** `US-MQ-34`  
**Asked:** 2026-10-29  
**Question:** For Illinois (IL), with citations and effective dates for 2026 (and 2027 if published): (1) does Illinois tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the Illinois revenue department withholding statute/guide and 2026 employer tables; the Illinois unemployment-insurance agency's wage-base and rate notice; the Illinois pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### IN — Indiana
**Status:** `pending_research`  
**Question id:** `US-MQ-35`  
**Asked:** 2026-10-29  
**Question:** For Indiana (IN), with citations and effective dates for 2026 (and 2027 if published): (1) does Indiana tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the Indiana revenue department withholding statute/guide and 2026 employer tables; the Indiana unemployment-insurance agency's wage-base and rate notice; the Indiana pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### KS — Kansas
**Status:** `pending_research`  
**Question id:** `US-MQ-36`  
**Asked:** 2026-10-29  
**Question:** For Kansas (KS), with citations and effective dates for 2026 (and 2027 if published): (1) does Kansas tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the Kansas revenue department withholding statute/guide and 2026 employer tables; the Kansas unemployment-insurance agency's wage-base and rate notice; the Kansas pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### KY — Kentucky
**Status:** `pending_research`  
**Question id:** `US-MQ-37`  
**Asked:** 2026-10-29  
**Question:** For Kentucky (KY), with citations and effective dates for 2026 (and 2027 if published): (1) does Kentucky tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the Kentucky revenue department withholding statute/guide and 2026 employer tables; the Kentucky unemployment-insurance agency's wage-base and rate notice; the Kentucky pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### LA — Louisiana
**Status:** `pending_research`  
**Question id:** `US-MQ-38`  
**Asked:** 2026-10-29  
**Question:** For Louisiana (LA), with citations and effective dates for 2026 (and 2027 if published): (1) does Louisiana tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the Louisiana revenue department withholding statute/guide and 2026 employer tables; the Louisiana unemployment-insurance agency's wage-base and rate notice; the Louisiana pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### MA — Massachusetts
**Status:** `pending_research`  
**Question id:** `US-MQ-39`  
**Asked:** 2026-10-29  
**Question:** For Massachusetts (MA), with citations and effective dates for 2026 (and 2027 if published): (1) does Massachusetts tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the Massachusetts revenue department withholding statute/guide and 2026 employer tables; the Massachusetts unemployment-insurance agency's wage-base and rate notice; the Massachusetts pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### MD — Maryland
**Status:** `pending_research`  
**Question id:** `US-MQ-40`  
**Asked:** 2026-10-29  
**Question:** For Maryland (MD), with citations and effective dates for 2026 (and 2027 if published): (1) does Maryland tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the Maryland revenue department withholding statute/guide and 2026 employer tables; the Maryland unemployment-insurance agency's wage-base and rate notice; the Maryland pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### ME — Maine
**Status:** `pending_research`  
**Question id:** `US-MQ-41`  
**Asked:** 2026-10-29  
**Question:** For Maine (ME), with citations and effective dates for 2026 (and 2027 if published): (1) does Maine tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the Maine revenue department withholding statute/guide and 2026 employer tables; the Maine unemployment-insurance agency's wage-base and rate notice; the Maine pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### MI — Michigan
**Status:** `pending_research`  
**Question id:** `US-MQ-42`  
**Asked:** 2026-10-29  
**Question:** For Michigan (MI), with citations and effective dates for 2026 (and 2027 if published): (1) does Michigan tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the Michigan revenue department withholding statute/guide and 2026 employer tables; the Michigan unemployment-insurance agency's wage-base and rate notice; the Michigan pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### MN — Minnesota
**Status:** `pending_research`  
**Question id:** `US-MQ-43`  
**Asked:** 2026-10-29  
**Question:** For Minnesota (MN), with citations and effective dates for 2026 (and 2027 if published): (1) does Minnesota tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the Minnesota revenue department withholding statute/guide and 2026 employer tables; the Minnesota unemployment-insurance agency's wage-base and rate notice; the Minnesota pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### MO — Missouri
**Status:** `pending_research`  
**Question id:** `US-MQ-44`  
**Asked:** 2026-10-29  
**Question:** For Missouri (MO), with citations and effective dates for 2026 (and 2027 if published): (1) does Missouri tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the Missouri revenue department withholding statute/guide and 2026 employer tables; the Missouri unemployment-insurance agency's wage-base and rate notice; the Missouri pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### MS — Mississippi
**Status:** `pending_research`  
**Question id:** `US-MQ-45`  
**Asked:** 2026-10-29  
**Question:** For Mississippi (MS), with citations and effective dates for 2026 (and 2027 if published): (1) does Mississippi tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the Mississippi revenue department withholding statute/guide and 2026 employer tables; the Mississippi unemployment-insurance agency's wage-base and rate notice; the Mississippi pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### MT — Montana
**Status:** `pending_research`  
**Question id:** `US-MQ-46`  
**Asked:** 2026-10-29  
**Question:** For Montana (MT), with citations and effective dates for 2026 (and 2027 if published): (1) does Montana tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the Montana revenue department withholding statute/guide and 2026 employer tables; the Montana unemployment-insurance agency's wage-base and rate notice; the Montana pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### NC — North Carolina
**Status:** `pending_research`  
**Question id:** `US-MQ-47`  
**Asked:** 2026-10-29  
**Question:** For North Carolina (NC), with citations and effective dates for 2026 (and 2027 if published): (1) does North Carolina tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the North Carolina revenue department withholding statute/guide and 2026 employer tables; the North Carolina unemployment-insurance agency's wage-base and rate notice; the North Carolina pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### ND — North Dakota
**Status:** `pending_research`  
**Question id:** `US-MQ-48`  
**Asked:** 2026-10-29  
**Question:** For North Dakota (ND), with citations and effective dates for 2026 (and 2027 if published): (1) does North Dakota tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the North Dakota revenue department withholding statute/guide and 2026 employer tables; the North Dakota unemployment-insurance agency's wage-base and rate notice; the North Dakota pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### NE — Nebraska
**Status:** `pending_research`  
**Question id:** `US-MQ-49`  
**Asked:** 2026-10-29  
**Question:** For Nebraska (NE), with citations and effective dates for 2026 (and 2027 if published): (1) does Nebraska tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the Nebraska revenue department withholding statute/guide and 2026 employer tables; the Nebraska unemployment-insurance agency's wage-base and rate notice; the Nebraska pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### NH — New Hampshire
**Status:** `pending_research`  
**Question id:** `US-MQ-50`  
**Asked:** 2026-10-29  
**Question:** For New Hampshire (NH), with citations and effective dates for 2026 (and 2027 if published): (1) does New Hampshire tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the New Hampshire revenue department withholding statute/guide and 2026 employer tables; the New Hampshire unemployment-insurance agency's wage-base and rate notice; the New Hampshire pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### NJ — New Jersey
**Status:** `pending_research`  
**Question id:** `US-MQ-51`  
**Asked:** 2026-10-29  
**Question:** For New Jersey (NJ), with citations and effective dates for 2026 (and 2027 if published): (1) does New Jersey tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the New Jersey revenue department withholding statute/guide and 2026 employer tables; the New Jersey unemployment-insurance agency's wage-base and rate notice; the New Jersey pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### NM — New Mexico
**Status:** `pending_research`  
**Question id:** `US-MQ-52`  
**Asked:** 2026-10-29  
**Question:** For New Mexico (NM), with citations and effective dates for 2026 (and 2027 if published): (1) does New Mexico tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the New Mexico revenue department withholding statute/guide and 2026 employer tables; the New Mexico unemployment-insurance agency's wage-base and rate notice; the New Mexico pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### NV — Nevada
**Status:** `pending_research`  
**Question id:** `US-MQ-53`  
**Asked:** 2026-10-29  
**Question:** For Nevada (NV), with citations and effective dates for 2026 (and 2027 if published): (1) does Nevada tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the Nevada revenue department withholding statute/guide and 2026 employer tables; the Nevada unemployment-insurance agency's wage-base and rate notice; the Nevada pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### NY — New York
**Status:** `pending_research`  
**Question id:** `US-MQ-54`  
**Asked:** 2026-10-29  
**Question:** For New York (NY), with citations and effective dates for 2026 (and 2027 if published): (1) does New York tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the New York revenue department withholding statute/guide and 2026 employer tables; the New York unemployment-insurance agency's wage-base and rate notice; the New York pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### OH — Ohio
**Status:** `pending_research`  
**Question id:** `US-MQ-55`  
**Asked:** 2026-10-29  
**Question:** For Ohio (OH), with citations and effective dates for 2026 (and 2027 if published): (1) does Ohio tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the Ohio revenue department withholding statute/guide and 2026 employer tables; the Ohio unemployment-insurance agency's wage-base and rate notice; the Ohio pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### OK — Oklahoma
**Status:** `pending_research`  
**Question id:** `US-MQ-56`  
**Asked:** 2026-10-29  
**Question:** For Oklahoma (OK), with citations and effective dates for 2026 (and 2027 if published): (1) does Oklahoma tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the Oklahoma revenue department withholding statute/guide and 2026 employer tables; the Oklahoma unemployment-insurance agency's wage-base and rate notice; the Oklahoma pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### OR — Oregon
**Status:** `pending_research`  
**Question id:** `US-MQ-57`  
**Asked:** 2026-10-29  
**Question:** For Oregon (OR), with citations and effective dates for 2026 (and 2027 if published): (1) does Oregon tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the Oregon revenue department withholding statute/guide and 2026 employer tables; the Oregon unemployment-insurance agency's wage-base and rate notice; the Oregon pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### PA — Pennsylvania
**Status:** `pending_research`  
**Question id:** `US-MQ-58`  
**Asked:** 2026-10-29  
**Question:** For Pennsylvania (PA), with citations and effective dates for 2026 (and 2027 if published): (1) does Pennsylvania tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the Pennsylvania revenue department withholding statute/guide and 2026 employer tables; the Pennsylvania unemployment-insurance agency's wage-base and rate notice; the Pennsylvania pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### RI — Rhode Island
**Status:** `pending_research`  
**Question id:** `US-MQ-59`  
**Asked:** 2026-10-29  
**Question:** For Rhode Island (RI), with citations and effective dates for 2026 (and 2027 if published): (1) does Rhode Island tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the Rhode Island revenue department withholding statute/guide and 2026 employer tables; the Rhode Island unemployment-insurance agency's wage-base and rate notice; the Rhode Island pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### SC — South Carolina
**Status:** `pending_research`  
**Question id:** `US-MQ-60`  
**Asked:** 2026-10-29  
**Question:** For South Carolina (SC), with citations and effective dates for 2026 (and 2027 if published): (1) does South Carolina tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the South Carolina revenue department withholding statute/guide and 2026 employer tables; the South Carolina unemployment-insurance agency's wage-base and rate notice; the South Carolina pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### SD — South Dakota
**Status:** `pending_research`  
**Question id:** `US-MQ-61`  
**Asked:** 2026-10-29  
**Question:** For South Dakota (SD), with citations and effective dates for 2026 (and 2027 if published): (1) does South Dakota tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the South Dakota revenue department withholding statute/guide and 2026 employer tables; the South Dakota unemployment-insurance agency's wage-base and rate notice; the South Dakota pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### TN — Tennessee
**Status:** `pending_research`  
**Question id:** `US-MQ-62`  
**Asked:** 2026-10-29  
**Question:** For Tennessee (TN), with citations and effective dates for 2026 (and 2027 if published): (1) does Tennessee tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the Tennessee revenue department withholding statute/guide and 2026 employer tables; the Tennessee unemployment-insurance agency's wage-base and rate notice; the Tennessee pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### TX — Texas
**Status:** `pending_research`  
**Question id:** `US-MQ-63`  
**Asked:** 2026-10-29  
**Question:** For Texas (TX), with citations and effective dates for 2026 (and 2027 if published): (1) does Texas tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the Texas revenue department withholding statute/guide and 2026 employer tables; the Texas unemployment-insurance agency's wage-base and rate notice; the Texas pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### UT — Utah
**Status:** `pending_research`  
**Question id:** `US-MQ-64`  
**Asked:** 2026-10-29  
**Question:** For Utah (UT), with citations and effective dates for 2026 (and 2027 if published): (1) does Utah tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the Utah revenue department withholding statute/guide and 2026 employer tables; the Utah unemployment-insurance agency's wage-base and rate notice; the Utah pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### VA — Virginia
**Status:** `pending_research`  
**Question id:** `US-MQ-65`  
**Asked:** 2026-10-29  
**Question:** For Virginia (VA), with citations and effective dates for 2026 (and 2027 if published): (1) does Virginia tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the Virginia revenue department withholding statute/guide and 2026 employer tables; the Virginia unemployment-insurance agency's wage-base and rate notice; the Virginia pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### VT — Vermont
**Status:** `pending_research`  
**Question id:** `US-MQ-66`  
**Asked:** 2026-10-29  
**Question:** For Vermont (VT), with citations and effective dates for 2026 (and 2027 if published): (1) does Vermont tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the Vermont revenue department withholding statute/guide and 2026 employer tables; the Vermont unemployment-insurance agency's wage-base and rate notice; the Vermont pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### WA — Washington
**Status:** `pending_research`  
**Question id:** `US-MQ-67`  
**Asked:** 2026-10-29  
**Question:** For Washington (WA), with citations and effective dates for 2026 (and 2027 if published): (1) does Washington tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the Washington revenue department withholding statute/guide and 2026 employer tables; the Washington unemployment-insurance agency's wage-base and rate notice; the Washington pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### WI — Wisconsin
**Status:** `pending_research`  
**Question id:** `US-MQ-68`  
**Asked:** 2026-10-29  
**Question:** For Wisconsin (WI), with citations and effective dates for 2026 (and 2027 if published): (1) does Wisconsin tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the Wisconsin revenue department withholding statute/guide and 2026 employer tables; the Wisconsin unemployment-insurance agency's wage-base and rate notice; the Wisconsin pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### WV — West Virginia
**Status:** `pending_research`  
**Question id:** `US-MQ-69`  
**Asked:** 2026-10-29  
**Question:** For West Virginia (WV), with citations and effective dates for 2026 (and 2027 if published): (1) does West Virginia tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the West Virginia revenue department withholding statute/guide and 2026 employer tables; the West Virginia unemployment-insurance agency's wage-base and rate notice; the West Virginia pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

### WY — Wyoming
**Status:** `pending_research`  
**Question id:** `US-MQ-70`  
**Asked:** 2026-10-29  
**Question:** For Wyoming (WY), with citations and effective dates for 2026 (and 2027 if published): (1) does Wyoming tax wage income and require employer withholding: method (tables/formula/flat/percent-of-federal), own withholding certificate or federal W-4, supplemental rate, rounding rule, authority, withholding return and deposit/reconciliation schedule? (2) local wage taxes (city/county/school district/PSD): which exist, residence- or work-based, who administers, piggybacked on the state return or remitted separately? (3) state unemployment insurance: agency, taxable wage base and how it is indexed, new-employer rate, any employee contribution, quarterly wage report? (4) SDI/TDI, PFML, long-term-care, transit, workforce or other payroll levies: employee/employer split, ceiling, return? (5) multistate: reciprocity agreements, resident credit, convenience-of-employer rule, nonresident day/dollar threshold? (6) pay-statement content and any primary-language notice rule; state prevailing-wage regime; third-party/POA filing authorisation; official withholding calculator or worked examples (oracle)?  
**What would answer it:** the Wyoming revenue department withholding statute/guide and 2026 employer tables; the Wyoming unemployment-insurance agency's wage-base and rate notice; the Wyoming pay-statement provision; the text of any reciprocity agreement.  
**Answer:** _pending_  
**register_id:** _pending_

## Changelog

- 2026-10-29 — compliance-scaffolder: mandate created. Tier T4 provisional. Open: US-MQ-01..14 and US-MQ-20..70 (65 questions). mandate_status pending_research.
