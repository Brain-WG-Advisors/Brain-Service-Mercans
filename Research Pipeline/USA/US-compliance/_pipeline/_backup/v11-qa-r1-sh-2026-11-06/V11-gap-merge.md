# V11 gap merge (validation pilot gap closures -> research)

Run 2026-11-06, compliance-source-hunter. Inputs: `gap-close-FED.md` (shard S6V-FED, 43 rows) and `gap-close-W1.md` rounds 1-2 (shards S6V-W1, 41 rows, and S6V-W1B, 31 rows). US-ILV6B-003 is absent from the shards and from every facts file (checked), so it stays unused. Facts were edited under `_research/facts.lock`; backups are in `_pipeline/_backup/v11-gapmerge-2026-11-06/`. For the same RQ, round 2 supersedes round 1.

## Register merge

- legal-basis-register.csv: 2,712 -> 2,827 rows (+115), with no id collisions and no duplicate ids. Tiers: 73 A.1, 38 A.2, 4 A.3; no tier B.
- consumed_by is filled on all 115 rows, from the gap location unit and every facts file that cites the row.
- supersedes: US-FEDV6-010 (Announcement 2026-11, 76 cents) supersedes US-FEDV6-011 (Notice 2026-10, 72.5 cents; effective_to 2026-06-30, status superseded). US-MIV6-002 (2026 PA 39, eff. 2026-07-22) supersedes US-MIS5-017 (2025 PA 24; effective_to 2026-07-21, superseded), and the facts were re-pointed. US-GAV6B-001 partly supersedes US-GAS5-005: only the 25-employee e-file threshold, and that row stays active. US-FEDV6-003 re-verifies US-FEDB5-401: verified_on stamped 2026-11-06, no supersession, same SSA figure.
- effective_from: 75 shard rows had none. They are set to 2026-01-01 with the note "in force for the whole build year as read 2026-11-06; enactment date not transcribed". Exceptions: US-MIV6-002 is 2026-07-22, and US-TXV6-005 is 2026-08-07 (the 51 TexReg proposal date already used by US-TXB5-301). 44 facts follow the row date.
- authority: 57 rows were renamed to the spelling the register and bulletin-sweep.json already use for the same institution (e.g. "Illinois General Assembly (ILGA)" -> "Illinois General Assembly"). Two were not renamed because no swept equivalent exists: "FTC / eCFR" (US-FEDV6-031) and "City of Philadelphia (Philadelphia Code ...)" (US-PAV6B-003).

## Quote spot-check (10 random, seed 20261106, plus the mileage quote)

All 11 quotes are in the saved source texts. 10 match verbatim. The other matches only after whitespace normalisation: RQ-169 / US-GAV6B-005 ("This Act prohibits the use or display of social security numbers ..."), where pypdf split words ("social se curity", "spec ified"). The words are the same, so this is a PDF spacing artefact. The row is kept and flagged here. No row was excluded.
Mileage was read in `FED/FED_irs-irb-2026-29-announcement-2026-11.txt`: "Announcement 2026-11 ... modifying Notice 2026-10 ... The revised standard mileage rates are: (1) Business 76 cents per mile (2) Medical and moving 23.5 cents per mile", for costs paid or incurred on or after July 1, 2026. The instrument is Announcement 2026-11 in IRB 2026-29. "Notice 2026-29" is a mis-citation.

## Gap counts (this merge, per jurisdiction)

| jurisdiction | closed | documented_limitation | open (still_blocked) |
|---|---|---|---|
| FED | 15 | 17 | 3 |
| CA | 9 | 1 | 0 |
| TX | 4 | 3 | 0 |
| NY | 7 | 3 | 0 |
| FL | 2 | 2 | 1 |
| IL | 7 | 2 | 0 |
| PA | 9 | 0 | 0 |
| OH | 5 | 5 | 0 |
| NC | 8 | 2 | 0 |
| MI | 3 | 3 | 2 |
| GA | 3 | 3 | 2 |
| **total** | **72** | **41** | **8** |

FED includes WTC-RQ-89 (`fed.bik.mileage.rate`), which was documented_limitation and is now closed by the mileage facts. Two results the workers marked "closed" were reclassified as documented_limitation, as instructed. RQ-591: the Trump-account FICA/FUTA treatment rests only on proposed section 128 regulations, so it is kept as a note. RQ-580: the TX 40 TAC ch. 815 amendments are still only proposed. Still_blocked items keep status open and have the round note appended to `note`. gaps.json totals after the merge: {"open": 474, "documented_limitation": 174, "closed": 104, "check_existing_fact": 1, "total": 753}.

## Facts keys changed

| file | key | old | new | contradiction | register |
|---|---|---|---|---|---|
| CCG-annex_FED-facts.json | `fed.leave.eo13706.accrual` | (none) | Accrual: 1 hour of paid sick leave per 30 hours worked on or in connection with a covered  [2017-01-01..] | no | US-FEDV6-008 |
| CCG-m08_leave-facts.json | `fed.eo13706.sick_leave.accrual` | (none) | Accrual: 1 hour of paid sick leave per 30 hours worked on or in connection with a covered  [2017-01-01..] | no | US-FEDV6-008 |
| CCG-m08_leave-facts.json | `fed.fmla.eligibility` | (none) | Employer coverage: 50 or more employees for 20 or more workweeks in the current or precedi [2026-11-06..] | no | US-FEDV6-014 |
| CCG-m08_leave-facts.json | `fed.pfml.employer_top_up.treatment` | (none) | An employer-paid supplement is employer sick pay: employee and employer FICA and FUTA appl [2026-01-01..] | no | US-FEDV6-017 |
| CCG-m09_termination-facts.json | `fed.backpay.treatment` | (none) | Back pay and retroactive increases are ordinary wages taxed in the year paid (FICA); for i [2026-01-01..] | no | US-FEDV6-018 |
| CCG-m12_worked_examples-facts.json | `fed.student_loan.payroll_obligation` | (none) | Federal administrative wage garnishment of student loans: maximum 15 percent of disposable [2026-11-06..] | no | US-FEDV6-025 |
| CCG-m06_tax-facts.json | `fed.employment_tax.adjustment_procedure` | (none) | Over-collected employee FICA and over-withheld income tax: if found before the return is f [2026-11-06..] | no | US-FEDV6-035 |
| CCG-annex_FED-facts.json | `fed.equity.nra.sourcing_period` | (none) | For stock options the time-basis period is generally grant to vesting (the date all employ [2005-07-14..] | no | US-FEDV6-039 |
| CCG-m06_tax-facts.json | `fed.equity.nra.sourcing_period` | (none) | For stock options the time-basis period is generally grant to vesting (the date all employ [2005-07-14..] | no | US-FEDV6-039 |
| CCG-annex_FED-facts.json | `fed.fica.totalization.agreements_in_force` | (none) | SSA lists 31 totalization agreements in force (Italy 1978 through Romania, entry into forc [2026-09-01..] | no | US-FEDV6-040 |
| CCG-m05_social_security-facts.json | `fed.fica.totalization.agreements_in_force` | (none) | SSA lists 31 totalization agreements in force (Italy 1978 through Romania, entry into forc [2026-09-01..] | no | US-FEDV6-040 |
| CCG-m04_compensation-facts.json | `fed.minister.futa` | (none) | FUTA excludes service in the employ of a 501(c)(3) religious organization (26 U.S.C. 3306( [2026-01-01..] | no | US-FEDV6-017 |
| CCG-annex_CA-facts.json | `ca.report.de9c.file_format` | (none) | Bulk DE 9C return file accepted as XML (App. B), ICESA (App. C/D no-payroll) or MMREF-1 (R [2026-11-06..] | no | US-CAV6-009 |
| CCG-annex_CA-facts.json | `ca.warn.employer_threshold` | (none) | Covered establishment = 75 or more persons employed (incl. within preceding 12 months); ma [2026-11-06..] | no | US-CAV6-006 |
| CCG-annex_CA-facts.json | `ca.hsa.conformity_2026` | (none) | Not enacted: AB 781 (DeMaio) is an Inactive Bill - Died 2026-01-31 pursuant to Art. IV Sec [2026-11-06..] | no | US-CAV6-008 |
| CCG-annex_CA-facts.json | `ca.garn.child_support.employer_fee` | (none) | Employer may deduct 1.50 USD per payment made under the order; SDU remittance once operati [2026-11-06..] | no | US-CAV6-003 |
| CCG-annex_CA-facts.json | `ca.prevailing_wage.thresholds` | (none) | DIR contractor registration not required for public works projects of 25,000 USD or less ( [2026-11-06..] | no | US-CAV6-004 |
| CCG-annex_CA-facts.json | `ca.overtime.agricultural_phase_in` | (none) | Fully phased in: >8h/day or >40h/week at 1.5x commencing 2022-01-01 for employers with 26+ [2026-11-06..] | no | US-CAV6-005 |
| CCG-annex_CA-facts.json | `ca.special_populations.ui_coverage_thresholds` | (none) | General employer: 1+ employee and wages over 100 USD in any calendar quarter (current or p [2026-11-06..] | no | US-CAV6-007 |
| CCG-annex_TX-facts.json | `tx.report.ui.due_date_records` | (none) | Quarterly wage report and tax due last day of month after quarter end: Apr 30, Jul 31, Oct [2026-11-06..] | no | US-TXV6-001 |
| CCG-annex_TX-facts.json | `tx.ui.wages.401k_section125` | (none) | Wages = all remuneration for personal services (201.081); 201.082 exceptions read in full  [2026-11-06..] | no | US-TXV6-004 |
| CCG-annex_TX-facts.json | `tx.report.new_hire.contractors` | (none) | For new-hire reporting 'employee' = IRC 3401(c) employee OR an independent contractor as d [2026-11-06..] | no | US-TXV6-002 |
| CCG-annex_TX-facts.json | `tx.leave.jury_military` | (none) | Jury service: permanent employee may not be discharged/threatened/coerced; right to return [2026-11-06..] | no | US-TXV6-003 |
| CCG-annex_NY-facts.json | `ny.garn.consumer.floor_region` | (none) | Nothing withheld unless weekly disposable earnings exceed the GREATER of 30x the federal m [2026-11-06..] | no | US-NYV6-002 |
| CCG-annex_NY-facts.json | `ny.labour.paycard` | (none) | No employer may deposit net wage in a bank/financial institution without the employee's ad [2026-11-06..] | no | US-NYV6-005 |
| CCG-annex_NY-facts.json | `ny.payslip.electronic` | (none) | Employer must furnish each employee a statement with every payment of wages; the section t [2026-11-06..] | no | US-NYV6-006 |
| CCG-annex_NY-facts.json | `ny.report.nys45_annual` | (none) | NYS-45 is a quarterly combined return (Parts A UI, B withholding reconciliation, C employe [2026-11-06..] | no | US-NYV6-001 |
| CCG-annex_NY-facts.json | `ny.bik.nyc_flex125_addback` | (none) | A-101 New York City flexible benefits program (IRC 125): amount deducted/deferred under an [2026-11-06..] | no | US-NYV6-004 |
| CCG-annex_NY-facts.json | `ny.term.ia12_3.timing` | (none) | Timing is statutory: Labor Law 590(2) requires the written notice at the time of each perm [2026-11-06..] | no | US-NYV6B-001 |
| CCG-annex_NY-facts.json | `ny.garn.state_tax_levy` | (none) | DTF issues a warrant after notice and demand; once filed with the county clerk it is a jud [2026-11-06..] | no | US-NYV6-003 |
| CCG-annex_FL-facts.json | `fl.report.sui.xml_changes_2026` | (none) | v2026 1.0: 257 change rows, ALL in User Information (guide/XPath docs/samples; 221 Changed [2026-11-06..] | no | US-FLV6-001 |
| CCG-annex_FL-facts.json | `fl.live.ch_2026_52` | (none) | In force: the 2026 Florida Statutes text carries 'History - ... s. 9, ch. 2026-52'. Notice [2026-11-06..] | no | US-FLV6-002 |
| CCG-annex_IL-facts.json | `il.pit.rate.statutory` | (none) | Individual/trust/estate rate 4.95% of net income for taxable years beginning on or after 2 [2026-11-06..] | no | US-ILV6-001 |
| CCG-annex_IL-facts.json | `il.payslip.content_list` | (none) | The content list is statutory, not in 56 Ill. Adm. Code 300.600 (that section is "Payment  [2026-11-06..] | no | US-ILV6B-001 |
| CCG-annex_IL-facts.json | `il.termination.ui_separation_notice` | (none) | Yes. 56 Ill. Adm. Code 2720.100(a): the employer delivers the IDES "What Every Worker Shou [2026-11-06..] | no | US-ILV6B-002 |
| CCG-annex_IL-facts.json | `il.data_protection.ssn_paystub` | (none) | A person may not publicly post/display an SSN, print it on access cards, transmit it over  [2026-11-06..] | no | US-ILV6-003 |
| CCG-annex_IL-facts.json | `il.local_minwage.chicago.tipped_schedule` | (none) | From July 1, 2026 Chicago minimum wage 17.05 USD; tipped 12.96 USD, steady until the next  [2026-07-01..] | no | US-ILV6B-004 |
| CCG-annex_IL-facts.json | `il.leave.cook.paid_leave.rules_2025` | (none) | Rules amended April 10, 2025. Accrual 1 hour per 40 hours worked (400.300/400.500); first  [2025-04-10..] | no | US-ILV6B-005 |
| CCG-annex_PA-facts.json | `pa.payment.method` | (none) | Act 161 of 2016: wages may be paid by credit to a financial-institution account including  [2016-11-04..] | no | US-PAV6B-002 |
| CCG-annex_PA-facts.json | `pa.leave.philadelphia.accrual` | (none) | Phila. Code 9-4104: 1 hour per 40 hours worked in Philadelphia, cap 40 hours per calendar  [2026-11-06..] | no | US-PAV6B-003 |
| CCG-annex_PA-facts.json | `pa.bik.hsa_withholding` | (none) | PA DOR Letter Ruling PIT-06-005 (2006-04-12): employer HSA contributions and HSA elections [2006-04-12..] | no | US-PAV6B-004 |
| CCG-annex_PA-facts.json | `pa.pit.local.eit.base` | (none) | LTEA section 501 (as amended by Act 18 of 2018): local earned income = compensation as req [2018-05-04..] | no | US-PAV6B-005 |
| CCG-annex_PA-facts.json | `pa.garn.state_tax_levy` | (none) | PA DOR may order an employer to withhold up to 10 percent of the taxpayer's gross wages (A [2003-01-01..] | no | US-PAV6B-006 |
| CCG-annex_PA-facts.json | `pa.prevailing_wage.certified_payroll` | (none) | weekly certified statement under oath plus a final statement; records per 9.109 (name, add [2026-11-06..] | no | US-PAV6B-007 |
| CCG-annex_PA-facts.json | `pa.garn.iwo.specifics` | (none) | 23 Pa.C.S. 4348: employer implements within 14 days of notice; remits to the domestic rela [2026-11-06..] | no | US-PAV6B-001 |
| CCG-annex_PA-facts.json | `pa.live.minwage_bill` | (none) | HB 1549 (2025-26, PN 1881), amends the Minimum Wage Act of 1968: House final passage 2025- [2025-06-11..] | no | US-PAV6B-008 |
| CCG-annex_PA-facts.json | `pa.labour.child_labour` | (none) | Act 151 of 2012 (effective 90 days after enactment): 14-15 years in school week max 3 h/da [2012-10-24..] | no | US-PAV6B-010 |
| CCG-annex_OH-facts.json | `oh.payment.method` | (none) | Wages must be paid by the 1st (for 1st-15th of prior month) and the 15th (for 16th-end of  [2026-11-06..] | no | US-OHV6-004 |
| CCG-annex_OH-facts.json | `oh.ui.wage_base.indexation` | (none) | Statutory fixed wage base, not indexed: 9,000 USD from 1995-01-01; 9,500 USD from 2018-01- [2026-11-06..] | no | US-OHV6-001 |
| CCG-annex_OH-facts.json | `oh.garn.deduction_rules_priority` | (none) | Withholding begins no later than 14 business days after the notice is mailed/transmitted,  [2026-11-06..] | no | US-OHV6-003 |
| CCG-annex_OH-facts.json | `oh.prevailing_wage.certified_payroll` | (none) | Contractors submit complete payroll for each pay date to the public authority's prevailing [2026-11-06..] | no | US-OHV6-002 |
| CCG-annex_OH-facts.json | `oh.sdi_pfml.exists` | (none) | No Ohio state-administered paid family/medical leave or TDI program is listed by DOL (Marc [2024-03-01..] | no | US-OHV6B-001 |
| CCG-annex_NC-facts.json | `nc.ui.wage_base.derivation` | (none) | NC taxable wages = greater of FUTA s.3306 wages or 50% of average yearly insured wage (avg [2026-11-06..] | no | US-NCV6-003 |
| CCG-annex_NC-facts.json | `nc.ui.registration` | (none) | NC UI employer = employer under FUTA s.3306 (plus 3309 governmental/nonprofit/tribe units) [2026-11-06..] | no | US-NCV6-002 |
| CCG-annex_NC-facts.json | `nc.report.w2.file_format` | (none) | NC W-2 file = fixed-field .txt following SSA EFW2 plus NCDOR fields; RE/RW/RS (state) reco [2026-11-06..] | no | US-NCV6-007 |
| CCG-annex_NC-facts.json | `nc.leave.other` | (none) | Jury duty: job protection only (no discharge/demotion; civil damages, reinstatement); stat [2026-11-06..] | no | US-NCV6-006 |
| CCG-annex_NC-facts.json | `nc.term.ui_separation_notice` | (none) | Employer duty is reactive: when a claim is filed DES sends a Separation Notice request; em [2026-11-06..] | no | US-NCV6-009 |
| CCG-annex_NC-facts.json | `nc.garn.iwo.payor_duties` | (none) | Payor processing fee 2.00 USD per withholding unless waived; cap 40% of disposable income  [2026-11-06..] | no | US-NCV6-001 |
| CCG-annex_NC-facts.json | `nc.data.breach` | (none) | Notice to affected persons without unreasonable delay; AG Consumer Protection Division not [2026-11-06..] | no | US-NCV6-005 |
| CCG-annex_NC-facts.json | `nc.labour.minwage.student_learner.hourly` | (none) | 6.5 [2026-11-06..] | no | US-NCV6-008 |
| CCG-annex_MI-facts.json | `mi.sui.coverage.ag_domestic` | (none) | Agricultural: 10+ individuals in 20 weeks or cash remuneration >= 20,000 USD in a quarter; [2026-11-06..] | no | US-MIV6-001 |
| CCG-annex_MI-facts.json | `mi.garn.iwo_fee_and_periodic` | (none) | Withheld income paid to FOC/SDU within 3 days after withholding; order binding on source o [2026-11-06..] | no | US-MIV6-003 |
| CCG-annex_MI-facts.json | `mi.live.2026_pa_39` | (none) | Approved 2026-07-21, effective 2026-07-22. MCL 206.30(1)(ee): for tax years beginning afte [2026-07-22..] | no | US-MIV6-002 |
| CCG-annex_GA-facts.json | `ga.minwage.state.exemptions` | (none) | Existing 34-4-3 text as reproduced (unstruck) in SB 24 (2021-22, legis.ga.gov): chapter do [2022-01-01..] | no | US-GAV6B-002 |
| CCG-annex_GA-facts.json | `ga.leave.family_care.status` | (none) | 34-1-10 is in force with no sunset. SB 201 (2017) created it with repeal on July 1, 2020;  [2023-05-01..] | no | US-GAV6B-003 |
| CCG-annex_FED-facts.json | `fed.bik.business_mileage.rate` | (none) | 0.725 [2026-01-01..2026-06-30] | no | US-FEDV6-011 |
| CCG-annex_FED-facts.json | `fed.bik.business_mileage.rate` | (none) | 0.76 [2026-07-01..] | no | US-FEDV6-010 |
| CCG-m11_advanced-facts.json | `fed.bik.business_mileage.rate` | (none) | 0.725 [2026-01-01..2026-06-30] | no | US-FEDV6-011 |
| CCG-m11_advanced-facts.json | `fed.bik.business_mileage.rate` | (none) | 0.76 [2026-07-01..] | no | US-FEDV6-010 |
| WTC-global_baseline-facts.json | `fed.bik.business_mileage.rate` | (none) | 0.725 [2026-01-01..2026-06-30] | no | US-FEDV6-011 |
| WTC-global_baseline-facts.json | `fed.bik.business_mileage.rate` | (none) | 0.76 [2026-07-01..] | no | US-FEDV6-010 |
| CCG-annex_FED-facts.json | `fed.fit.std_deduction.single` | (none) | 16600 [2027-01-01..2027-12-31] | no | US-FEDV6-004 |
| CCG-annex_FED-facts.json | `fed.fit.std_deduction.mfj` | (none) | 33200 [2027-01-01..2027-12-31] | no | US-FEDV6-004 |
| CCG-annex_FED-facts.json | `fed.fit.std_deduction.hoh` | (none) | 24925 [2027-01-01..2027-12-31] | no | US-FEDV6-004 |
| CCG-annex_FED-facts.json | `fed.bik.health_fsa.salary_reduction_cap` | (none) | 3500 [2027-01-01..2027-12-31] | no | US-FEDV6-004 |
| CCG-annex_FED-facts.json | `fed.bik.parking.monthly_exclusion` | effective_to open | effective_to 2026-12-31 | no | US-FEDS5-008 |
| CCG-annex_FED-facts.json | `fed.bik.parking.monthly_exclusion` | (none) | 350 [2027-01-01..2027-12-31] | no | US-FEDV6-004 |
| WTC-global_baseline-facts.json | `fed.fit.std_deduction.single` | (none) | 16600 [2027-01-01..2027-12-31] | no | US-FEDV6-004 |
| WTC-global_baseline-facts.json | `fed.fit.std_deduction.mfj` | (none) | 33200 [2027-01-01..2027-12-31] | no | US-FEDV6-004 |
| WTC-global_baseline-facts.json | `fed.fit.std_deduction.hoh` | (none) | 24925 [2027-01-01..2027-12-31] | no | US-FEDV6-004 |
| WTC-global_baseline-facts.json | `fed.bik.health_fsa.salary_reduction_cap` | (none) | 3500 [2027-01-01..2027-12-31] | no | US-FEDV6-004 |
| WTC-global_baseline-facts.json | `fed.bik.parking.monthly_exclusion` | effective_to open | effective_to 2026-12-31 | no | US-FEDS5-008 |
| WTC-global_baseline-facts.json | `fed.bik.parking.monthly_exclusion` | (none) | 350 [2027-01-01..2027-12-31] | no | US-FEDV6-004 |
| CCG-m04_compensation-facts.json | `fed.base.transportation.fit` | excluded up to 340 a month for commuter .. [2026-01-01..open] -> closed 2026-12-31 | excluded up to 350 a month for commuter highway vehicle and transit passes and 350 a month [2027-01-01..2027-1 | no | US-FEDV6-004 |
| CCG-m04_compensation-facts.json | `fed.base.transportation.fica` | excluded up to 340 a month for commuter .. [2026-01-01..open] -> closed 2026-12-31 | excluded up to 350 a month for commuter highway vehicle and transit passes and 350 a month [2027-01-01..2027-1 | no | US-FEDV6-004 |
| CCG-m04_compensation-facts.json | `fed.base.transportation.futa` | excluded up to 340 a month for commuter .. [2026-01-01..open] -> closed 2026-12-31 | excluded up to 350 a month for commuter highway vehicle and transit passes and 350 a month [2027-01-01..2027-1 | no | US-FEDV6-004 |
| WTC-global_baseline-facts.json | `fed.base.transportation.fit` | excluded up to 340 a month for commuter .. [2026-01-01..open] -> closed 2026-12-31 | excluded up to 350 a month for commuter highway vehicle and transit passes and 350 a month [2027-01-01..2027-1 | no | US-FEDV6-004 |
| WTC-global_baseline-facts.json | `fed.base.transportation.fica` | excluded up to 340 a month for commuter .. [2026-01-01..open] -> closed 2026-12-31 | excluded up to 350 a month for commuter highway vehicle and transit passes and 350 a month [2027-01-01..2027-1 | no | US-FEDV6-004 |
| WTC-global_baseline-facts.json | `fed.base.transportation.futa` | excluded up to 340 a month for commuter .. [2026-01-01..open] -> closed 2026-12-31 | excluded up to 350 a month for commuter highway vehicle and transit passes and 350 a month [2027-01-01..2027-1 | no | US-FEDV6-004 |
| CCG-m07_deductions-facts.json | `fed.bik.transportation.conditions` | Commuter highway vehicle and transit pas.. [2026-01-01..open] -> closed 2026-12-31 | Commuter highway vehicle and transit passes up to 350 a month and qualified parking up to  [2027-01-01..2027-1 | no | US-FEDV6-004 |
| CCG-annex_FED-facts.json | `fed.indexation.publication_2027` | (none) | Rev. Proc. 2026-35 (IR-2026-133, issued 2026-11-05) publishes the TY2027 inflation adjustm [2026-11-05..] | no | US-FEDV6-005 |
| CCG-m07_deductions-facts.json | `fed.bik.trump_account.conditions` | note | note += section 128 proposed-rule treatment | no | US-FEDV6-042 |
| WTC-country_specific-facts.json | `ca.sdi.employee.rate` | (none) | 1.4 [2027-01-01..] | no | US-CAV6-002 |
| CCG-annex_CA-facts.json | `ca.sdi.benefit.weekly_max` | (none) | 1765 [2026-01-01..2026-12-31] | no | US-CAV6-001 |
| CCG-annex_IL-facts.json | `il.sui.wage_base` | (none) | 14592 [2027-01-01..] | no | US-ILV6-002 |
| WTC-country_specific-facts.json | `il.sui.wage_base` | (none) | 14592 [2027-01-01..] | no | US-ILV6-002 |
| CCG-annex_GA-facts.json | `ga.report.sui.efile_threshold_employees` | 25 [2026-01-01..open] | 25 [2026-01-01..2026-08-08] | YES | US-GAS5-005 |
| CCG-annex_GA-facts.json | `ga.report.sui.efile_all_employers` | threshold 25 employees (open-ended) | True [2026-08-09..] | YES | US-GAV6B-001 |
| RSPEC-facts.json | `ga.report.sui.efile_threshold_employees` | 25 [2026-01-01..open] | 25 [2026-01-01..2026-08-08] | YES | US-GAS5-005 |
| RSPEC-facts.json | `ga.report.sui.efile_all_employers` | threshold 25 employees (open-ended) | True [2026-08-09..] | YES | US-GAV6B-001 |
| CCG-annex_GA-facts.json | `ga.report.sui.dol4n` | "electronic for 25+ employees" [2026-01-01..open] | DOL-4N due 30 Apr, 31 Jul, 31 Oct, 31 Jan; electronic for all employers (Rule 300-2-2-.02( [2026-08-09..] | YES | US-GAV6B-001 |
| CCG-annex_MI-facts.json | `mi.pit.tips_overtime_deduction` | register US-MIS5-017 (2025 PA 24) | register US-MIV6-002 (2026 PA 39); rule unchanged, assessment only | no | US-MIV6-002 |
| CCG-m13_practices-facts.json | `practice.mi.tips_ot_deduction_level` | register US-MIS5-017 (2025 PA 24) | register US-MIV6-002 (2026 PA 39); rule unchanged, assessment only | no | US-MIV6-002 |
| CCG-annex_TX-facts.json | `tx.report.ui.enhanced_fields.status` | PROPOSED ONLY (unchanged) | note: ch. 815 PROPOSED only (re-confirmed) | no | US-TXV6-005 |
| DD-8_sheets-facts.json | `dd.tx.ui.enhanced` | effective 2026-01-01 without an adopted implementing rule | note: ch. 815 PROPOSED only (re-confirmed) | YES | US-TXV6-005 |
| RSPEC-facts.json | `rspec.tx.ui_qtr.enhanced_content` | effective 2026-01-01 without an adopted implementing rule | note: ch. 815 PROPOSED only (re-confirmed) | YES | US-TXV6-005 |
| SIR-facts.json | `sir.tx.wage_report.enhanced_content` | effective 2026-01-01 without an adopted implementing rule | note: ch. 815 PROPOSED only (re-confirmed) | YES | US-TXV6-005 |

Also changed: 44 rule facts from this run moved from effective_from 2026-11-06 to the row date above. The unresolved[] entries for closed keys were removed from the facts files that owned them. For documented limitations, `why` was replaced and `attempted` appended. For still_blocked items, `attempted` was appended.

## Contradictions (research defects)

1. **GA SUI e-filing (YES).** CCG-annex_GA and RSPEC carried `ga.report.sui.efile_threshold_employees` = 25, open-ended (US-GAS5-005, DOL-224 R-11/24), and `ga.report.sui.dol4n` said "electronic for 25+ employees". GDOL Rule 300-2-2-.02(6)(a), amended F. 2026-07-20 and eff. 2026-08-09, requires all employers to file electronically [US-GAV6B-001]. The old facts now end on 2026-08-08, and successor facts start on 2026-08-09.
2. **TX enhanced UI wage-report content (YES, framing).** DD (`dd.tx.ui.enhanced`), RSPEC (`rspec.tx.ui_qtr.enhanced_content`) and SIR (`sir.tx.wage_report.enhanced_content`) present the Labor Code 204.0025 data elements as effective 2026-01-01; SIR has no caveat. The TWC amendment to 40 TAC ch. 815 that would implement them is still PROPOSED [US-TXV6-005]. The values are unchanged; a note was added: "proposed only, do not configure as mandatory". The CCG annex already said PROPOSED ONLY.
No contradiction in the other findings. CA SDI 2027 1.4% was already in CCG and RSPEC; it is now added to WTC. IL UI wage base 14,250 (2026) matches, and 14,592 (2027) is added. SSA 2027 base 192,300 matches. MI 2026 PA 39 keeps the rule (assessment level only, TY2026-2028); only the cited act changes. Mileage, the Rev. Proc. 2026-35 TY2027 figures and the Trump-account note are additions. OH UI 9,000 (not indexed) matches. Chicago tipped 12.96 matches.

## Key aliases (for agent 3 / agent 4 re-binding)

- `fed.bik.mileage_rate` (RQ-409, annex_FED), `fed.bik.business_mileage.rate` (RQ-536, m11) and `fed.bik.mileage.rate` (WTC-RQ-89) are one fact. It is emitted only as **`fed.bik.business_mileage.rate`**: 0.725 USD/mile for 2026-01-01..06-30 and 0.76 from 2026-07-01, in CCG-annex_FED, CCG-m11_advanced and WTC-global_baseline.
- Closed gaps answered under existing canonical keys: `il.sui.wage_base.next_year` -> `il.sui.wage_base` (2027 object); `ca.sdi.employee.rate.next_year` -> `ca.sdi.employee.rate` (2027); `fed.fica.oasdi.wage_base.next_year_reverification` -> `fed.fica.oasdi.wage_base` (2027, note); `fed.indexation.publication_2027` is emitted in annex_FED; `ga.report.sui.efile_all_employers` is new.
- Open question, not changed here: `fed.leave.eo13706.accrual` (annex_FED) and `fed.eo13706.sick_leave.accrual` (m08) now carry the same rule. They should be merged into one key in a later cycle.

## Artifacts whose text must be rebuilt

- **CCG**: annexes FED, CA, TX, NY, FL, IL, PA, OH, NC, MI, GA; modules m02_master_data, m04_compensation, m06_tax, m07_deductions, m08_leave, m09_termination, m10_reporting, m11_advanced, m12_worked_examples, m13_practices. The CCG must write the mid-year dates **2026-08-09** (GA e-file for all employers) and **2026-09-01** (US-Romania totalization in force); C41 fails until it does. Every [[GAP:RQ-...]] marker for a closed RQ must become a fact citation.
- **WTC**: global_baseline (mileage; TY2027 standard deduction, FSA, parking and transportation) and country_specific (CA SDI 2027, IL wage base 2027, MI note).
- **RSPEC** (GA e-file scope from 2026-08-09; TX ch. 815 proposed caveat), **DD** (TX caveat), **SIR** (TX caveat).
- PSL: no facts changed. DESIGN: re-read only if it cites the GA e-file threshold or the TX enhanced fields.
- Research packs: the Open-questions blocks of the packs above were NOT regenerated in this run. The facts files and gaps.json are authoritative; regenerate the packs before or with the rebuild.

## Validation

- validate_contract --all: PASS (118 files).
- research_checks C40: PASS (18/18 rows answered).
- research_checks C41: FAIL on 4 items; it passed before the merge. (a) Two authorities have no bulletin sweep: FTC (US-FEDV6-031) and City of Philadelphia / Philadelphia Code (US-PAV6B-003). To clear them, run a real 2026 sweep of each (Federal Register for the FTC; Philadelphia City Council legislation for ch. 9-4100). (b) Two mid-year change dates are not yet written in the CCG (2026-08-09, 2026-09-01); the CCG rebuild clears them. No register row is stale or undated, and no fact is dangling.
- F44 on the 28 changed facts files: 3,300 facts checked. Every fact cites an existing register row that is A-tier, not MANUAL, has an effective_from and has a verified_on within 120 days. 0 issues.
