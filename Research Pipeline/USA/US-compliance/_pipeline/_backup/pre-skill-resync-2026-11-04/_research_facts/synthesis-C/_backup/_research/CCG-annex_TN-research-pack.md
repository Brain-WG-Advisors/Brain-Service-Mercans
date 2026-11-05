# CCG research pack - annex_TN (Tennessee)

Synthesis-B worker MN-WY, 2026-11-02. Unit `annex_TN` of the CCG (jurisdiction annex, all 13 domains + special populations).
Facts file: `_research/CCG-annex_TN-facts.json` (24 facts, 3 pending on the register_id pattern defect, 11 unresolved). Every claim below carries its register_id inline; numbers may be cited in the CCG only through a fact key.

## 0. How to use this pack

- Body sections 1-13 and Special populations are the stage-5 findings (`_research/stage5/TN.md`), carried verbatim because they are already organised by the 13 CCG domains with register ids inline.
- Federal layer (FIT, FICA, FUTA, W-2/941/940), the multistate rules (reciprocity, sourcing) and the language seams (US-OWN-006: payslip in English; second-language duties attach to notices and posters only) live in annex_FED / annex_MULTI and are not repeated here.
- Special populations (US-OWN-005): the state-level rules are in the Special populations table below; the country-wide coverage matrix is CCG unit `coverage`.
- Values are 2026 unless the fact says otherwise. 2027 values appear only where the row carries an enacted or published 2027 figure; projections are never facts.

## 0.1 Synthesis decisions and traps (bind the builder)

- TN has NO wage tax (T1). SUI base 7,000; Table 6 (0.01-10.00%); new employer 2.7%.
- Separation Notice LB-0489 within 24 hours of separation - DD needs severance, wages in lieu of notice and vacation pay fields.
- Garnishment departs from CCPA: 2.50/week per dependent child under 16 reduces the amount withheld.

## 0.2 Register status check of the ids cited in the findings

These ids appear in the findings but are not plain `active`; do not cite them for a number:

- US-TNR3-001: superseded
- US-TNS5-015: MANUAL
- US-TNS5-016: MANUAL

## 0.3 Facts emitted

| key | value | from | to | register_id | conf |
|---|---|---|---|---|---|
| `tn.labour.minwage.state.exists` | False | 2026-01-01 |  | US-TNS5-011 | high |
| `tn.labour.overtime.state_rule` | none (FLSA only) | 2026-01-01 |  | US-TNS5-001 | medium |
| `tn.pay_frequency.rule` | employers with 5+ employees: regular paydays at least monthly | 2026-01-01 |  | US-TNS5-001 | high |
| `tn.labour.meal_break.minutes` | 30 minutes | 2026-01-01 |  | US-TNS5-001 | high |
| `tn.pit.exists` | False | 2021-01-01 |  | US-TN-001 | high |
| `tn.sui.wage_base` | 7000 USD | 2018-01-01 | 2026-12-31 | US-TNS5-002 | high |
| `tn.ui.rate_table.in_effect` | Premium Rate Table 6 | 2026-01-01 | 2026-12-31 | US-TNS5-002 | high |
| `tn.sui.employer.rate.min` | 0.01 % | 2026-01-01 | 2026-12-31 | US-TNS5-003 | high |
| `tn.sui.employer.rate.max` | 10.0 % | 2026-01-01 | 2026-12-31 | US-TNS5-003 | high |
| `tn.sui.new_employer.rate` | 2.7 % | 2026-01-01 |  | US-TNS5-004 | high |
| `tn.sui.employee.rate` | 0 % | 2026-01-01 |  | US-TNR3-003 | high |
| `tn.sdi_pfml.exists` | False | 2026-01-01 |  | US-TNR3-003 | high |
| `tn.payslip.statute.exists` | False | 2026-01-01 |  | US-TNS5-001 | medium |
| `tn.report.ui.quarterly_due` | Apr 30; Jul 31; Oct 31; Jan 31 | 2025-05-27 |  | US-TNS5-005 | high |
| `tn.newhire.report_days` | 20 days | 2026-01-01 |  | US-TNS5-008 | high |
| `tn.leave.sick.state_statute.exists` | False | 2026-01-01 |  | US-TNS5-001 | high |
| `tn.leave.jury_duty.paid` | True | 2026-01-01 |  | US-TNS5-012 | high |
| `tn.final_pay.rule` | later of next regular payday or 21 days after separation | 2026-01-01 |  | US-TNS5-001 | high |
| `tn.term.vacation.payout` | only if policy or labour agreement requires | 2026-01-01 |  | US-TNS5-001 | high |
| `tn.term.separation_notice.hours` | 24 hours | 2026-01-01 |  | US-TNS5-007 | high |
| `tn.term.warn.employee_threshold` | 50 | 2026-01-01 |  | US-TNS5-006 | medium |
| `tn.garn.creditor.max_percent` | 25 % | 2026-01-01 |  | US-TNS5-010 | high |
| `tn.garn.consumer.child_reduction.weekly` | 2.5 USD | 2026-01-01 |  | US-TNS5-010 | high |
| `tn.garn.iwo.remit_days` | 7 days | 2026-01-01 |  | US-TNS5-009 | medium |
| `tn.local_wage_tax.exists` | False | 2026-01-01 |  | US-TN-P5-2-001 (PENDING id pattern) | high |
| `tn.prevailing_wage.scope` | state-funded highway construction only | 2026-01-01 |  | US-TN-P5-1-002 (PENDING id pattern) | high |
| `tn.prevailing_wage.unskilled_laborer.hourly` | 23.52 USD | 2026-01-01 |  | US-TN-P5-1-002 (PENDING id pattern) | high |

# Findings by domain (stage 5)

## 1 — labour_code
- **Minimum wage:** Tennessee has no state minimum wage law. FLSA-covered employers pay the federal USD 7.25/hour (DOL WHD state table, updated 2026-07-01). [US-TNS5-011, A.2, high]
  - No 2027 state rate exists.
  - Local minimum wages are preempted (T.C.A. 7-51-1802). This comes from tier-B/CTAS leads only, so no number is registered. [lead, medium]
- **Overtime:** no state overtime rule beyond the FLSA. The DLWD wage-regulations index lists no overtime topic. [US-TNS5-001, US-TNR3-001, medium-high]
- **Pay frequency and pay-day timing** (T.C.A. 50-2-103(a)): [US-TNS5-001, A.2, high]
  - Private employers with 5 or more employees must keep regular paydays and pay at least once a month.
  - Monthly payers: wages earned before the 1st are due by the 5th of the next month.
  - Payers with 2 or more periods a month: wages earned before the 1st are due by the 20th of the following month; wages earned before the 16th are due by the 5th of the next month.
- **Live change, piece-work and commission timing:** PC 617 (2026, HB 1958) is said to replace 50-2-103(a)(2) from 2026-07-01. Piece-work and commission pay earned on or after that date would be due by the last day of the following month. [US-TNS5-015, MANUAL, tier-B lead]
- **Meal break:** 30 minutes unpaid if the employee is scheduled 6 consecutive hours, except where the nature of the business gives ample chance to rest (50-2-103(h)). [US-TNS5-001]
- **Method of payment (direct deposit / paycard consent):** no A-tier source was read. The DLWD wage page is silent on it. → Open question Q1.

## 2 — income_tax
- No state tax on wage income and no withholding. The Hall tax (interest and dividends) was repealed from 2021-01-01. There is no state W-4, no state supplemental rate and no state W-2 filing. [US-TN-001, US-TN-P5-1-001, A.2, high]
- No local income or wage tax. [US-TN-P5-2-001, A.2, high]
- Reciprocity and resident/nonresident rules do not apply.
- **Payroll consequence:** a TN resident who works in a wage-taxing state is withheld for that state (MULTI unit). A TN worker gets no state withholding at all.

## 3 — social_security
- **SUI taxable wage base 2026:** USD 7,000 (unchanged since 2018). Earlier bases: 8,000 in 2016-2017 and 9,000 in 2014-2015. The base varies with the Trust Fund balance. [US-TNS5-002, A.2, high]
- **Rate table:** Premium Rate Table 6 applies from 2026-01-01 and 2026-07-01 (in force continuously since 2015-07-01). The Trust Fund balance on June 30 and December 31 decides the table for the next six months (T.C.A. 50-7-403). [US-TNS5-002]
- **Rate range:** Table 6 runs from 0.01% (reserve ratio 20.0 and over) to 10.00% (most negative reserve ratios). Rates for negative reserve ratios run 5.00–10.00% and are shared across all tables. The PDF layout is column-shifted, so read each cell before mapping a reserve-ratio row. [US-TNS5-003, A.2, high on range, medium on row mapping]
- **New-employer rate:** 2.7% for all other industries. Manufacturing NAICS sectors 31, 32 and 33 get a sector-based rate from the sector's combined reserve experience. A new employer becomes experience-rated after 36 consecutive months ending December 31, starting the next July 1. [US-TNS5-004, A.3, high]
- **Employee contribution:** none. [US-TNR3-003]
- **Liability thresholds:** [US-TNS5-013, A.2, high]
  - FUTA-liable employer with 1 or more TN employee;
  - USD 1,500 in a quarter, or 1 employee in 20 weeks;
  - 501(c)(3) employer with 4 or more employees in 20 weeks;
  - domestic service: USD 1,000 cash wages in a quarter;
  - agricultural: 10 or more employees in 20 weeks, or USD 20,000 in a quarter;
  - every government unit.
- **PEO rules:** separate quarterly reports per client (UIT-P account), at the PEO aggregate rate. [US-TNS5-013]
- **No other payroll levy:** no SDI/TDI, PFML, LTC, transit or workforce levy. [US-TNR3-003, US-TN-P5-2-001]

## 4 — payslip_statute
- No Tennessee statute requires an itemised pay statement. The DLWD Wage Regulations Act index and poster show none. Federal recordkeeping (FLSA) applies. [US-TNR3-001, US-TN-P5-1-003, US-TNS5-001, medium-high; T.C.A. text not read]
- Retention: no state rule located beyond UI records. → Q4.

## 5 — reporting_instruments
- **No state withholding returns and no state W-2 filing:** TN has no wage tax.
- **Quarterly UI report:** Wage Report LB-0851 plus Premium Report LB-0456 (form numbers as cited on LB-0489). [US-TNS5-005, US-TNS5-007, US-TNS5-014]
  - Due by the last day of the month after the quarter: Apr 30, Jul 31, Oct 31, Jan 31. Late filing starts the delinquent cycle (notice about 3 weeks after the due date, then a pending assessment).
  - Filed in **Employer e-Services** (TNPAWS closed; tax functions live since 2025-05-27). Formats: manual entry, abbreviated ICESA, 58-character text file, or full ICESA (single employer or TPA/PEO bulk).
  - Amendments that decrease wages need documentation and staff approval.
- **Registration:** online in Employer e-Services; the 8-digit account number and the rate are issued immediately. [US-TNS5-005, US-TNS5-013]
- **New hires:** report new or rehired employees within 20 days of hire. The programme belongs to TN DHS (tnnewhire.com), not to the UI system. [US-TNS5-008, A.2; US-TNS5-009]
- **TPA access:** no POA is needed since 2025-05-27. [US-TNR3-002]

## 6 — leave
- **No mandatory paid sick leave, vacation or PTO, and no PFML.** Fringe benefits follow company policy. [US-TNS5-001, A.2, high]
- **Jury duty:** the employer pays wages during jury service less the court's pay (T.C.A. 22-4-108). [US-TNS5-012, A.3, high]
- **Voting:** voting absence is protected (2-1-106). [US-TNS5-012]
  - Pay rule, from leads only: up to 3 hours, no pay reduction, request by noon the day before. [US-TNS5-016, MANUAL]
- **Military leave:** protected (8-33-101 to -109). [US-TNS5-012]
- **Parental leave (4-21-408):** up to 4 months **unpaid**, at 100 or more full-time employees per site, after 12 months of service. Leads only. [US-TNS5-016, MANUAL]

## 7 — termination
- **Final pay:** due by the next regular payday or 21 days after separation, whichever is later. This applies to discharge and resignation alike, with no exemption (50-2-103(g)). [US-TNS5-001, A.2, high]
- **Accrued vacation/PTO:** paid out only if the policy or a labour agreement requires it (50-2-103(a)(3)). [US-TNS5-001]
- **Separation Notice (form LB-0489):** [US-TNS5-007, A.2, high]
  - Hand or mail it to the employee within 24 hours of separation (Rule 0800-09-01-.02).
  - Not required if the employee worked less than a week or will be recalled within 7 days.
  - The form reports severance pay, wages in lieu of notice and vacation pay on temporary layoff. → Payroll data needed (DD).
- **TN WARN:** applies at 50 or more full-time employees (or 50+ working 2,000 hours a week in total). It is a notice duty only. [US-TNS5-006, A.3]
- **Child-support IWO:** report terminations to the child-support office named on the IWO. [US-TNS5-009]

## 8 — benefits_in_kind
Not applicable at state level: there is no state income tax, so there is no state conformity question (401(k), 125, HSA and the rest follow federal treatment only). SUI wage definition: the state Employment Security Law excludes certain items, but its text was not read (Lexis). → Q5. [US-TN-P5-1-001]

## 9 — deductions_garnishments
- **Wage deductions:** an offset for amounts the employee owes needs a prior signed written agreement held by the employer (50-2-110(a)(2)). A pay cut is allowed if notified before the work is done. [US-TNS5-001, A.2]
- **Ordinary garnishment** (T.C.A. 26-2-404(b) worksheet on the Davidson County court form): [US-TNS5-010, A.3, high]
  - Disposable earnings = gross pay less social security and federal income tax.
  - Withhold the lesser of 25% of disposable earnings, or disposable earnings minus 30 × federal minimum wage per week (×2 biweekly, ×2.166667 semimonthly, ×4.333334 monthly).
  - Then subtract USD 2.50/week for each dependent child under 16 living in TN (5.00 biweekly, 5.42 semimonthly, 10.83 monthly).
  - TN therefore departs from the CCPA through the child add-on.
- **Child support / alimony (ex-spouse not remarried):** [US-TNS5-010]
  - 50% or 55% of disposable earnings if supporting another spouse or child (arrears under or over 12 weeks);
  - 60% or 65% if not;
  - or the ordered amount, if lower.
- **IWO:** remit to the TN SDU within 7 days of payday; tell the employer line about lump sums (bonus, profit sharing); e-IWO and ACH available. Fees and priority were not located on an A-tier source. → Q3. [US-TNS5-009, A.3]
- **State tax levies on wages:** not applicable (no income tax). A DOR levy for other taxes was not researched.

## 10 — collective_agreements
- **Prevailing Wage Act** (T.C.A. 12-4-401 et seq.): state-funded highway construction only. Rates (25 crafts) apply from 2026-01-01, for example Unskilled Laborer USD 23.52. [US-TN-P5-1-002, A.2]
- No state certified-payroll format was read. → Q6.

## 11 — indexation
- The SUI wage base is set by the Trust Fund level (USD 7,000 since 2018), not by an index. The rate table is reset every six months from the Trust Fund balance. [US-TNS5-002]
- There is no minimum wage to index. Prevailing highway rates are re-surveyed each year. [US-TN-P5-1-002]
- **G-DERIVE:** no indexed amount exists, so there is nothing to derive. The wage base is a published level, not a formula output.

## 12 — data_protection
No SSN-truncation rule for pay statements was located on an A-tier source.
- Leads: T.C.A. 47-18-2110 (limits on displaying SSNs) and the Tennessee Information Protection Act, effective 2025-07-01. Reports say TIPA excludes employee data, but this was not verified. → Q7. [no row]

## 13 — live_legal_change
- **PC 617 (2026), pay timing for piece-work and commission:** effective 2026-07-01. [US-TNS5-015, MANUAL]
- **UI tax system moved to Employer e-Services** on 2025-05-27; POA numbers dropped. [US-TNS5-005, US-TNR3-002]
- **2026 SUI changes:** none (base 7,000, Table 6 in both halves). [US-TNS5-002]
- **Workers' compensation:** the BWC "2026 Workers' Compensation Legislative Changes" page (2026-07-10) could not be read (HTTP 403). Its payroll relevance is unknown. → Q2.
- No 2027 enactment located (bulletin sweep not completed: capitol.tn.gov unreachable).

## Special populations (state rules beyond federal)
| Population | TN rule | register_id |
|---|---|---|
| Domestic/household | UI coverage at USD 1,000 cash wages in a quarter; household employers must register | US-TNS5-013, US-TNS5-005 |
| Agricultural | UI coverage at 10 or more workers in 20 weeks, or USD 20,000 in a quarter | US-TNS5-013 |
| Minors | Child Labor Act (break/hours rules). DLWD child-labor page HTTP 403 today; no state minor wage rate (no state minimum wage) | US-TN-P5-1-003 (poster), Q8 |
| Tipped | No state rule; FLSA 3(m) only (no state minimum wage) | US-TNS5-011 |
| Clergy/religious | No state rule beyond federal (no state income tax). UI exclusion not read | Q5 |
| Students | No state rule beyond federal located. UI exclusions not read | Q5 |
| Nonresident aliens | No state withholding, so no state effect | US-TN-P5-1-001 |
| Statutory employees | No state rule beyond federal (no state income tax) | US-TN-P5-1-001 |
| Government employees | UI liability covers all state and local government units | US-TNS5-013 |
| Seasonal employers | LB-3304 election (Sept 1 – Oct 31); seasonal wages may be excluded from benefit determination; written notice to workers | US-TNS5-013 |
| PEO clients | Separate reports per client, aggregate rate, joint liability unless a USD 100,000 bond is posted | US-TNS5-013 |

## ACCESS gaps (exact URLs, 2026-11-02)
- https://wapp.capitol.tn.gov/apps/BillInfo/Default.aspx?BillNumber=HB1958&GA=114: curl timeout (000), WebFetch ECONNREFUSED 170.142.7.21:443.
- https://www.capitol.tn.gov/Bills/114/Bill/HB1958.pdf: curl timeout (000).
- https://publications.tnsosfiles.com/acts/114/pub/pc0617.pdf: HTTP 403.
- https://www.tn.gov/humanrights/laws-and-regu1/maternity-leave1.html: HTTP 404 (page moved). The Wayback attempt was blocked by the session permission classifier and was not retried.
- https://sos.tn.gov/elections/voter-information: HTTP 403. Wayback not attempted (same classifier block).
- https://www.tn.gov/workforce/injuries-at-work/bwc-newsroom/2026/7/10/2026-workers-compensation-legislative-changes-tennessee.html: HTTP 403 (tn.gov began rate-limiting curl at about 08:10).
- https://www.tn.gov/workforce/employees/labor-laws/labor-laws-redirect/child-labor.html: HTTP 403 (same).
- https://www.tn.gov/content/dam/tn/workforce/documents/employers/HandbookforEmployers6-13-19.pdf: HTTP 404 (retired).
- T.C.A. (Lexis Advance public site): not readable by curl, so no A.1 statute row.

## Open questions

Mirrors `unresolved[]` of the facts file (same keys, same wording).

- **tn.meta.register_id_pattern** (blocking): 3 facts rest on active register rows whose ids (US-TN-P5-1-002, US-TN-P5-2-001) do not match the facts-schema register_id pattern ^[A-Z]{2}-[A-Z0-9]{2,12}-[0-9]{3,4}$ (multi-hyphen legacy ids). They are carried in full in _facts_pending_register_id_pattern and are NOT yet consumable facts. What would close it: Orchestrator decision: a PATCH of facts.schema.json loosening the register_id pattern (e.g. ^[A-Z]{2}-[A-Z0-9-]{2,16}-[0-9]{3,4}$), or register alias ids; then run _research/synthesis-B/_work-MN-WY/promote.py to move the pending facts into facts[].
- **tn.payment.method** (non-blocking): Direct deposit / paycard consent rule not read (Lexis-only T.C.A.). What would close it: T.C.A. 50-2-103 text (Chrome pass) or a DLWD page.
- **tn.live.pc617_pay_timing** (non-blocking): PC 617 (2026, HB 1958) piece-work/commission timing from 2026-07-01 rests on MANUAL US-TNS5-015. What would close it: Read the act text (publications.tnsosfiles.com pc0617.pdf) via browser.
- **tn.live.bwc_2026** (non-blocking): BWC 2026 workers' compensation legislative changes not read (403). What would close it: Chrome read of the BWC newsroom page.
- **tn.garn.iwo.fee_priority** (non-blocking): IWO employer fee and priority not located on A source. What would close it: TN DHS Child Support Employer Services page.
- **tn.records.retention** (non-blocking): State payroll record retention not located. What would close it: T.C.A. 50-7-701 / Rule 0800-09-01 text.
- **tn.ui.wage_definition** (non-blocking): SUI wage exclusions (125, 401(k), tips, students, clergy, officers) not read. What would close it: T.C.A. 50-7-207, 50-7-213 or the DLWD employer handbook.
- **tn.prevailing_wage.certified_payroll** (non-blocking): State highway certified payroll format not read. What would close it: TDOT/DLWD prevailing-wage contract special provisions.
- **tn.data.ssn_tipa** (non-blocking): SSN display (47-18-2110) and TIPA employee-data exclusion not verified. What would close it: T.C.A. 47-18 text or TN AG page.
- **tn.labour.child_labour** (non-blocking): Child Labor Act hours/break rules not read (403). What would close it: DLWD child-labor page (Chrome).
- **tn.leave.voting_parental** (non-blocking): Voting pay (3 h) and parental leave (4 months unpaid) rest on MANUAL US-TNS5-016. What would close it: THRC/SOS pages or T.C.A. 2-1-106 / 4-21-408.
