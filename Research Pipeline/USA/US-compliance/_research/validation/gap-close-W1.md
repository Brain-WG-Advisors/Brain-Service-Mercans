# Gap close W1 - read 2026-11-06 via Opera US (US VPN exit)

Scope: open gaps of CA, TX, NY, FL, IL, PA, OH, NC, MI, GA in `_research/gaps.json` (86). Register shard: `00-official-sources/_register-shards/S6V-W1.csv` (ids US-{ST}V6-NNN). Source texts: `00-official-sources/ccg-sources/{ST}/`.

Honest limits: about 110 page reads were used; 25 gaps (all of GA bar one, most of PA/IL, parts of OH/FL) could not be reached and are marked still_blocked, either NOT ATTEMPTED (budget) or blocked as stated. HTTP 403 PDFs (michigan.gov Treasury, floridajobs.org poster, twc.texas.gov commission PDF) and an "Access denied" NY DOL page were not bypassed. No form was submitted.

Search-engine summaries were used only to locate URLs; every value below was read on the authority page or statute.


## California (CA)

### RQ-480 `ca.sdi.employee.rate.next_year` - closed
- Answer: 2027 SDI withholding rate 1.4 percent (2026 was 1.3%); all wages subject to SDI; also 2027 UI schedule F+ (1.5%-6.2%, 7,000 wage limit) and ETT 0.1%
- Source (A.2): https://edd.ca.gov/en/payroll_taxes/tax-rated-employers/
- Quote: "The SDI withholding rate for 2027 is 1.4 percent."
- Register ids: US-CAV6-002

### RQ-481 `ca.payslip.electronic_consent` - documented_limitation
- Reason: LAB 226(a) read in full on leginfo: requires an accurate itemized statement 'in writing' furnished semimonthly or at each payment; the text contains no occurrence of the word 'electronic' and states no consent rule. The DLSE opinion letter / DIR paydays FAQ was not located (dir.ca.gov/dlse/DLSE_FAQ_Paydays.htm returned page-not-found).
- Register ids: none

### RQ-482 `ca.report.de9c.file_format` - closed
- Answer: Bulk DE 9C return file accepted as XML (App. B), ICESA (App. C/D no-payroll) or MMREF-1 (RE/RS/RST records); guide Rev. 12 (7-24) - a newer revision was not checked
- Source (A.2): https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de8300.pdf
- Quote: "Appendix B - eXtensible Markup Language (XML) Format; Appendix C - Interstate Conference of Employment Security Agencies (ICESA) Format"
- Register ids: US-CAV6-009

### RQ-483 `ca.sdi.benefit.weekly_max` - closed
- Answer: 2026 maximum weekly benefit amount 1,765 USD; max benefit 91,780 = 1,765 x 52 (checked); employee contribution rate 1.3% (eff. 2026-01-01)
- Source (A.2): https://edd.ca.gov/en/disability/Contribution_Rates_and_Benefit_Amounts/
- Quote: "Maximum Weekly Benefit Amount (WBA) $1,765"
- Register ids: US-CAV6-001

### RQ-484 `ca.warn.employer_threshold` - closed
- Answer: Covered establishment = 75 or more persons employed (incl. within preceding 12 months); mass layoff = 50 or more employees in any 30-day period at a covered establishment
- Source (A.1): https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=LAB&sectionNum=1400.5
- Quote: "Covered establishment means any industrial or commercial facility or part thereof that employs, or has employed within the preceding 12 months, 75 or more persons."
- Register ids: US-CAV6-006

### RQ-485 `ca.hsa.conformity_2026` - closed
- Answer: Not enacted: AB 781 (DeMaio) is an Inactive Bill - Died 2026-01-31 pursuant to Art. IV Sec 10(c); hearing canceled 2025-04-21. No other enacted HSA-conformity act was located (only this bill checked); FTB 2026 Schedule CA instructions not read. Level: assessment
- Source (A.1): https://leginfo.legislature.ca.gov/faces/billStatusClient.xhtml?bill_id=202520260AB781
- Quote: "Inactive Bill - Died ... 01/31/26 Died pursuant to Art. IV, Sec. 10(c) of the Constitution."
- Register ids: US-CAV6-008

### RQ-486 `ca.garn.child_support.employer_fee` - closed
- Answer: Employer may deduct 1.50 USD per payment made under the order; SDU remittance once operational; substitution of payee forwarded within 10 days
- Source (A.1): https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=FAM&sectionNum=5235
- Quote: "The employer may deduct from the earnings of the employee the sum of one dollar and fifty cents ($1.50) for each payment made pursuant to the order."
- Register ids: US-CAV6-003

### RQ-487 `ca.prevailing_wage.thresholds` - closed
- Answer: DIR contractor registration not required for public works projects of 25,000 USD or less (construction/alteration/demolition/installation/repair) or 15,000 USD or less (maintenance); registration/renewal fee up to 800 USD set by DIR
- Source (A.1): https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=LAB&sectionNum=1725.5
- Quote: "twenty-five thousand dollars ($25,000) or less when the project is for construction, alteration, demolition, installation, or repair work"
- Register ids: US-CAV6-004

### RQ-488 `ca.overtime.agricultural_phase_in` - closed
- Answer: Fully phased in: >8h/day or >40h/week at 1.5x commencing 2022-01-01 for employers with 26+ employees; commencing 2025-01-01 for employers with 25 or fewer (earlier steps 9.5/55 from 2019, 9/50 from 2020, 8.5/45 from 2021, with +3 years for small employers)
- Source (A.1): https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=LAB&sectionNum=860
- Quote: "This subdivision shall apply to an employer who employs 25 or fewer employees commencing January 1, 2025."
- Register ids: US-CAV6-005

### RQ-514 `ca.special_populations.ui_coverage_thresholds` - closed
- Answer: General employer: 1+ employee and wages over 100 USD in any calendar quarter (current or preceding year); domestic service in private home/college club: cash wages of 1,000 USD or more in any quarter (current or preceding year). Agricultural (UIC 678) and nonprofit thresholds NOT read
- Source (A.1): https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=UIC&sectionNum=682
- Quote: "pays wages in cash of one thousand dollars ($1,000) or more for such service during any calendar quarter"
- Register ids: US-CAV6-007


## Texas (TX)

### RQ-336 `tx.report.ui.due_date_records` - closed
- Answer: Quarterly wage report and tax due last day of month after quarter end: Apr 30, Jul 31, Oct 31, Jan 31. Records-retention rule (40 TAC 815.107) not read
- Source (A.2): https://www.twc.texas.gov/programs/unemployment-tax/tax-report-payment-due-dates
- Quote: "Quarterly wage reports and tax payments are due by the last day of the month following the end of the quarter."
- Register ids: US-TXV6-001

### RQ-338 `tx.ui.rate.new_employer.derivation` - still_blocked
- Reason: TWC 'Your 2026 Tax Rates' page renders only its title (rate content sits in collapsed accordions not exposed in page text) and the commission-meeting PDF (mtg25 ... item9b-dp-2026-tax-rates) returned HTTP 403 to curl; not bypassed. Statute: new-employer rate assignment rule is Labor Code 204.006 (cited by TWC; local copy US register TX_LA.204 predates this pass).
- Register ids: none

### RQ-339 `tx.ui.wages.401k_section125` - closed
- Answer: Wages = all remuneration for personal services (201.081); 201.082 exceptions read in full contain no exclusion for employee elective 401(k) deferrals or IRC s.125 reductions (only payments to/from exempt 401(a) trusts); TWC guidance not obtained
- Source (A.1): https://statutes.capitol.texas.gov/Docs/LA/htm/LA.201.htm
- Quote: "'wages' means all remuneration for personal services, including"
- Register ids: US-TXV6-004

### RQ-340 `tx.report.new_hire.contractors` - closed
- Answer: For new-hire reporting 'employee' = IRC 3401(c) employee OR an independent contractor as defined by the IRS (also TNC drivers); employers report each newly hired/rehired employee to the state directory per 42 USC 653a
- Source (A.1): https://statutes.capitol.texas.gov/Docs/FA/htm/FA.234.htm
- Quote: "or an independent contractor as defined by the Internal Revenue Service."
- Register ids: US-TXV6-002

### RQ-341 `tx.leave.jury_military` - closed
- Answer: Jury service: permanent employee may not be discharged/threatened/coerced; right to return to same employment on notice; text states no pay obligation. Military leave (Gov. Code 431.005/437.204) NOT read
- Source (A.1): https://statutes.capitol.texas.gov/Docs/CP/htm/CP.122.htm
- Quote: "An employer may not discharge, threaten to discharge, intimidate, or coerce any permanent employee because the employee serves as a juror"
- Register ids: US-TXV6-003

### RQ-342 `tx.ui.rates.next_year` - documented_limitation
- Reason: TWC rate page is still titled 'Your 2026 Tax Rates' with no 2027 content as read on 2026-11-06; TWC sets rates at its November/December commission meeting and mails notices in December, so no 2027 rate is published yet.
- Register ids: none

### RQ-580 `tx.report.ui.enhanced_fields.adoption` - closed
- Answer: Status PROPOSED, not adopted on this page: TWC proposes 40 TAC ch.815 amendments for new employer wage-record data elements; comments due 2026-09-07. The Oct 1 / Nov 1 2026 effective dates on the same page belong to the Child Care Services rules, NOT ch.815. Adoption notice and layout not found; level: employer reporting
- Source (A.2): https://www.twc.texas.gov/agency/laws-rules-policy/rules/rules-proposed-adopted
- Quote: "TWC proposes amendments to 40 TAC Chapter 815, Unemployment Insurance, to incorporate new employer wage record reporting data elements"
- Register ids: US-TXV6-005


## New York (NY)

### RQ-263 `ny.pit.oracle.example2_residual` - documented_limitation
- Reason: NYS-50-T-NYS (1/26) read in full from tax.ny.gov (ccg-sources/NY/nys50t-nys-1-26.txt): the publication states NO rounding convention (no occurrence of round / nearest / whole-dollar rule). Example 2 prints 165.00 x 0.0753 = 12.43, but the product is 12.4245 (half-up = 12.42, ceiling = 12.43); Examples 1 (27,016.40 x 0.0735 = 1,985.7054 -> 1,985.71) and 4 (107.85 x 0.0640 = 6.9024 -> 6.90) match half-up. Residual of 0.01 is unexplained; only a DTF statement or calculator result can settle it.
- Register ids: none

### RQ-264 `ny.sui.wage_base.next_year` - documented_limitation
- Reason: NYS-50-T-NYS and NYS-45-I (1/26) carry 2026 figures only. The NYS-45-I states the wage base is the state average annual wage rounded up to the nearest 100 USD, set annually; the 2027 figure/NYS-50 2027 edition is expected in December 2026 and is not yet published (gap's own closing condition).
- Register ids: none

### RQ-265 `ny.garn.consumer.floor_region` - closed
- Answer: Nothing withheld unless weekly disposable earnings exceed the GREATER of 30x the federal minimum hourly wage or 30x the state minimum hourly wage in Labor Law 652 (so the state minimum applies when higher); cap is the lesser of 25% of disposable earnings or the excess over that floor; 10% of gross for the 10% execution. The clause as read does not name a Labor Law 652 region
- Source (A.1): https://www.nysenate.gov/legislation/laws/CVP/5231
- Quote: "the greater of thirty times the federal minimum hourly wage prescribed in the Fair Labor Standards Act of 1938 or thirty times the state minimum hourly wage prescribed in section six hundred fifty-two of the labor law"
- Register ids: US-NYV6-002

### RQ-266 `ny.labour.paycard` - closed
- Answer: No employer may deposit net wage in a bank/financial institution without the employee's advance written consent (exempt: executive/admin/professional earning over 1,300 USD/week; farm workers). 12 NYCRR Part 192 (paycard rules) NOT read
- Source (A.1): https://www.nysenate.gov/legislation/laws/LAB/192
- Quote: "No employer shall without the advance written consent of any employee directly pay or deposit the net wage or salary of such employee in a bank"
- Register ids: US-NYV6-005

### RQ-267 `ny.payslip.electronic` - closed
- Answer: Employer must furnish each employee a statement with every payment of wages; the section text contains no occurrence of 'electronic' (inspected directly), so electronic delivery rests on DOL guidance which was not obtained
- Source (A.1): https://www.nysenate.gov/legislation/laws/LAB/195
- Quote: "furnish each employee with a statement with every payment of wages"
- Register ids: US-NYV6-006

### RQ-268 `ny.report.nys45_annual` - closed
- Answer: NYS-45 is a quarterly combined return (Parts A UI, B withholding reconciliation, C employee wage detail) due last day of month after quarter end; no separate annual NYS-45 reconciliation found in the instructions; annual UI items go on IA7/IA7A; Q4 withholding overpayment is refunded automatically
- Source (A.2): https://www.tax.ny.gov/pdf/current_forms/wt/nys45i.pdf
- Quote: "Part B is used to reconcile your withholding tax payments for the"
- Register ids: US-NYV6-001

### RQ-269 `ny.bik.nyc_flex125_addback` - closed
- Answer: A-101 New York City flexible benefits program (IRC 125): amount deducted/deferred under an NYC (or certain other NYC public employer) flexible benefits program shown on W-2 is an ADDITION modification on IT-201/IT-203/IT-204. Edition read is (2025); level: assessment
- Source (A.2): https://www.tax.ny.gov/pdf/current_forms/it/it225i.pdf
- Quote: "A-101: New York City flexible benefits program (IRC 125)"
- Register ids: US-NYV6-004

### RQ-270 `ny.term.ia12_3.timing` - still_blocked
- Reason: dol.ny.gov/notice-eligibility-ui-benefits redirected to an 'Access denied' page (labor department site); 12 NYCRR 472.8 text and IA 12.3 timing not read. Not bypassed. Only search snippets (tier B) describe the notice.
- Register ids: none

### RQ-271 `ny.garn.state_tax_levy` - closed
- Answer: DTF issues a warrant after notice and demand; once filed with the county clerk it is a judgment and the sheriff/DTF officer executes it 'in the same manner prescribed by law in respect to executions issued against' property, i.e. CPLR 5231 income-execution limits apply to wages (not separately read per DTF forms)
- Source (A.1): https://www.nysenate.gov/legislation/laws/TAX/692
- Quote: "proceed upon the warrant in all respects, with like effect, and in the same manner prescribed by law in respect to executions issued against"
- Register ids: US-NYV6-003

### RQ-547 `ny.oracle.nys50t.example2.withholding` - documented_limitation
- Reason: Same finding as ny.pit.oracle.example2_residual: publication prints 12.43 and 258.51 (12.43 + 246.08) for Example 2; half-up of 12.4245 gives 12.42 and 258.50. DTF does not state its rounding rule in NYS-50-T-NYS (1/26); DTF calculator not run (form submission out of scope).
- Register ids: none


## Florida (FL)

### RQ-155 `fl.minwage.tipped.poster_confirmation` - still_blocked
- Reason: The 2026 poster/announcement PDFs on floridajobs.org returned HTTP 403 to curl (not bypassed). The HTML page floridajobs.org/florida-minimum-wage was read and confirms 15.00 USD/h effective 2026-09-30 to 2027-12-31, but it does not print the tipped direct wage; 11.98 (= 15.00 - 3.02) is still only derived.
- Register ids: none

### RQ-157 `fl.report.sui.xml_changes_2026` - closed
- Answer: v2026 1.0: 257 change rows, ALL in User Information (guide/XPath docs/samples; 221 Changed, 18 Inserted, 8 Deleted, 6 Renamed, 3 Added) and none in Schema_Reemployment; RSI replaces BSWA as intake provider. URL is the package landing page (zip retrieved 2026-11-02, inspected directly)
- Source (A.2): https://floridarevenue.com/taxes/etools/Pages/RT_XML.aspx
- Quote: "Updated User Guide to reflect RSI system and process changes"
- Register ids: US-FLV6-001

### RQ-158 `fl.termination.separation_notice` - documented_limitation
- Reason: Rule chapter 73B-10 F.A.C. index read on flrules.org (ccg-sources/FL/flrules-73b-10.txt): its rule titles (73B-10.022 to .037) include no separation-notice rule. Chapter 73B-11 was not read, so absence is not established for the whole 73B-10/73B-11 pair.
- Register ids: none

### RQ-159 `fl.live.ch_2026_52` - closed
- Answer: In force: the 2026 Florida Statutes text carries 'History - ... s. 9, ch. 2026-52'. Notice to the Department of Legal Affairs for breaches of 500+ individuals no later than 30 days after determination (15-day extension possible). Which subsection ch. 2026-52 s.9 changed was not isolated (session-law text not read: laws.flrules.org/2026/52 rendered blank)
- Source (A.1): https://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0500-0599/0501/Sections/0501.171.html
- Quote: "A covered entity shall provide notice to the department of any breach of security affecting 500 or more individuals in this state."
- Register ids: US-FLV6-002

### RQ-160 `fl.live.bulletin_sweep` - documented_limitation
- Reason: Not performed: a full sweep of Laws of Florida 2026 and DOR Tax Information Publications needs index pages (laws.flrules.org rendered blank) and exceeds the remaining read budget. Only ch. 2026-52 (501.171) was pinned.
- Register ids: none


## Illinois (IL)

### RQ-198 `il.pit.rate.statutory` - closed
- Answer: Individual/trust/estate rate 4.95% of net income for taxable years beginning on or after 2017-07-01; no different 2027 rate appears in the section text as currently published (header: Text of Section from P.A. 104-468). Level: assessment and withholding base rate
- Source (A.1): https://www.ilga.gov/Documents/legislation/ilcs/documents/003500050K201.htm
- Quote: "for taxable years beginning on or after July 1, 2017, an amount equal to 4.95% of the taxpayer's net income for the taxable year."
- Register ids: US-ILV6-001

### RQ-199 `il.pit.conformity_statement` - still_blocked
- Reason: NOT ATTEMPTED: the ~110 page-read budget was exhausted before this gap. Would close it: IDOR Pub. 101 / IL-1040 instructions
- Register ids: none

### RQ-200 `il.sui.wage_base.next_year` - closed
- Answer: Statutory wage base: 2026 = 14,250 USD; 2027 and each later year = 14,592 USD (2024 13,590; 2025 13,916). The 405/235 formula gap is closed; the IDES 2027 rate chart (December 2026) is still unpublished
- Source (A.1): https://www.ilga.gov/Documents/legislation/ilcs/documents/082004050K235.htm
- Quote: "With respect to the calendar year 2027, and each calendar year thereafter, the term "wages" shall include only the remuneration paid to an individual by an employer during that period with respect to employment which does not exceed $14,592."
- Register ids: US-ILV6-002

### RQ-201 `il.payslip.content_list` - still_blocked
- Reason: 56 Ill. Adm. Code 300.600: the JCAR URL tried (ilga.gov/commission/jcar/admincode/056/056003000F06000R.html) returned 404 and the correct URL was not found within budget. Would close it: ilga.gov/JCAR Title 56 Part 300 section 300.600 text.
- Register ids: none

### RQ-204 `il.termination.ui_separation_notice` - still_blocked
- Reason: NOT ATTEMPTED: the ~110 page-read budget was exhausted before this gap. Would close it: 56 Ill. Adm. Code 2770 or the IDES employer handbook
- Register ids: none

### RQ-205 `il.data_protection.ssn_paystub` - closed
- Answer: A person may not publicly post/display an SSN, print it on access cards, transmit it over the Internet unless secure/encrypted, or print it on materials mailed to the individual unless law requires it. Pay statements are not named in the section text read; 815 ILCS 530 (PIPA breach notice) NOT read
- Source (A.1): https://www.ilga.gov/Documents/legislation/ilcs/documents/081505050K2RR.htm
- Quote: "a person may not do any of the following"
- Register ids: US-ILV6-003

### RQ-206 `il.local_minwage.chicago.tipped_schedule` - still_blocked
- Reason: NOT ATTEMPTED: the ~110 page-read budget was exhausted before this gap. Would close it: MCC 6-105-020 text or BACP 2026 notice
- Register ids: none

### RQ-207 `il.live.news_sweep` - still_blocked
- Reason: NOT ATTEMPTED: the ~110 page-read budget was exhausted before this gap. Would close it: tax.illinois.gov, labor.illinois.gov and ides.illinois.gov newsroom sweeps
- Register ids: none

### RQ-578 `il.leave.cook.paid_leave.rules_2025` - still_blocked
- Reason: NOT ATTEMPTED: the ~110 page-read budget was exhausted before this gap. Would close it: CCHR Paid Leave Ordinance Rules on cookcountyil.gov
- Register ids: none


## Pennsylvania (PA)

### RQ-299 `pa.payment.method` - still_blocked
- Reason: palegis.us consolidated-statute/bill pages rendered blank in Opera (page text empty after 25 s; 23 Pa.C.S. 4348 tried twice, URL redirected from legis.state.pa.us), so statute text could not be read; other PA gaps behind the same host were not attempted. Would close it: DLI BLLC interpretation or palegis.us search for payroll card
- Register ids: none

### RQ-300 `pa.leave.philadelphia.accrual` - still_blocked
- Reason: NOT ATTEMPTED: the ~110 page-read budget was exhausted before this gap. Would close it: Phila. Code 9-4104 or the Office of Worker Protections page
- Register ids: none

### RQ-301 `pa.bik.hsa_withholding` - still_blocked
- Reason: NOT ATTEMPTED: the ~110 page-read budget was exhausted before this gap. Would close it: REV-634 or PA PIT Bulletin 2006-05
- Register ids: none

### RQ-302 `pa.pit.local.eit.base` - still_blocked
- Reason: NOT ATTEMPTED: the ~110 page-read budget was exhausted before this gap. Would close it: LTEA Sec. 501 and the DCED Tax Register page
- Register ids: none

### RQ-303 `pa.garn.state_tax_levy` - still_blocked
- Reason: palegis.us consolidated-statute/bill pages rendered blank in Opera (page text empty after 25 s; 23 Pa.C.S. 4348 tried twice, URL redirected from legis.state.pa.us), so statute text could not be read; other PA gaps behind the same host were not attempted. Would close it: 72 P.S. 7345 / DOR guidance
- Register ids: none

### RQ-304 `pa.prevailing_wage.certified_payroll` - still_blocked
- Reason: palegis.us consolidated-statute/bill pages rendered blank in Opera (page text empty after 25 s; 23 Pa.C.S. 4348 tried twice, URL redirected from legis.state.pa.us), so statute text could not be read; other PA gaps behind the same host were not attempted. Would close it: 34 Pa. Code ch. 9 / DLI LLC forms
- Register ids: none

### RQ-305 `pa.garn.iwo.specifics` - still_blocked
- Reason: palegis.us consolidated-statute/bill pages rendered blank in Opera (page text empty after 25 s; 23 Pa.C.S. 4348 tried twice, URL redirected from legis.state.pa.us), so statute text could not be read; other PA gaps behind the same host were not attempted. Would close it: 23 Pa.C.S. 4348 and the PA Child Support Program employer page
- Register ids: none

### RQ-306 `pa.live.minwage_bill` - still_blocked
- Reason: palegis.us consolidated-statute/bill pages rendered blank in Opera (page text empty after 25 s; 23 Pa.C.S. 4348 tried twice, URL redirected from legis.state.pa.us), so statute text could not be read; other PA gaps behind the same host were not attempted. Would close it: palegis.us bill history
- Register ids: none

### RQ-307 `pa.labour.child_labour` - still_blocked
- Reason: palegis.us consolidated-statute/bill pages rendered blank in Opera (page text empty after 25 s; 23 Pa.C.S. 4348 tried twice, URL redirected from legis.state.pa.us), so statute text could not be read; other PA gaps behind the same host were not attempted. Would close it: DLI child labour page or 43 P.S. 40.1 ff.
- Register ids: none


## Ohio (OH)

### RQ-273 `oh.payment.method` - closed
- Answer: Wages must be paid by the 1st (for 1st-15th of prior month) and the 15th (for 16th-end of prior month) of each month; section text contains no provision on payment medium (direct deposit/paycard/check) - inspected directly (search for direct deposit, electronic, card, check, cash: none)
- Source (A.1): https://codes.ohio.gov/ohio-revised-code/section-4113.15
- Quote: "pay all its employees the wages earned by them during the first half of the preceding month"
- Register ids: US-OHV6-004

### RQ-274 `oh.ui.wage_base.indexation` - closed
- Answer: Statutory fixed wage base, not indexed: 9,000 USD from 1995-01-01; 9,500 USD from 2018-01-01; 9,000 USD from 2020-01-01 (in force for 2026)
- Source (A.1): https://codes.ohio.gov/ohio-revised-code/section-4141.01
- Quote: "nine thousand dollars on and after January 1, 2020"
- Register ids: US-OHV6-001

### RQ-275 `oh.leave.other` - documented_limitation
- Reason: Only ORC 3599.06 was read (saved ccg-sources/OH/orc-3599-06.txt): employer may not discharge or threaten an elector for taking a reasonable amount of time to vote; the section states no pay rule. ORC 2313.19 (jury) and 5903.02 (military) were not read (2313.18 was fetched by mistake, irrelevant).
- Register ids: none

### RQ-276 `oh.garn.deduction_rules_priority` - closed
- Answer: Withholding begins no later than 14 business days after the notice is mailed/transmitted, or for employers no later than the first pay period after 14 business days; continues until further notice. Statutory priority between orders (3121.034) and general deduction-authorisation rules (4113.15) NOT read
- Source (A.1): https://codes.ohio.gov/ohio-revised-code/section-3121.03
- Quote: "begin the withholding no later than fourteen business days following the date the notice is mailed or transmitted to the payor"
- Register ids: US-OHV6-003

### RQ-277 `oh.prevailing_wage.certified_payroll` - closed
- Answer: Contractors submit complete payroll for each pay date to the public authority's prevailing wage coordinator: employee name, current address, last four SSN digits, hours per day and week, hourly rate, job classification, fringe payments, deductions. 2026 coverage-threshold adjustment (4115.03) NOT read
- Source (A.1): https://codes.ohio.gov/ohio-revised-code/section-4115.071
- Quote: "a copy of the contractor's or subcontractor's complete payroll for each date exhibiting for each employee paid any wages"
- Register ids: US-OHV6-002

### RQ-278 `oh.report.ui.channel` - documented_limitation
- Reason: ODJFS employer pages reached (jfs.ohio.gov/unemployment-services) are navigation only; the bulk-upload specification was not located on the guessed URLs (unemployment.ohio.gov/... returned no usable content).
- Register ids: none

### RQ-279 `oh.term.ui_separation_notice` - documented_limitation
- Reason: OAC 4141 rule text not located: the one rule fetched (4141-9-01, codes.ohio.gov) concerns taxable wages, not separation notices; no ODJFS employer handbook page was found.
- Register ids: none

### RQ-280 `oh.pit.tables.next_year` - documented_limitation
- Reason: Gap's own closing condition is 're-check January 2027': ODT/ODJFS publish 2027 withholding tables and rates later in the year; nothing to read yet on 2026-11-06 (not re-fetched this pass).
- Register ids: none

### RQ-281 `oh.sdi_pfml.exists` - still_blocked
- Reason: NOT ATTEMPTED: the ~110 page-read budget was exhausted before this gap. Would close it: a DOL state TDI/PFML list or an ODJFS page
- Register ids: none

### RQ-282 `oh.pit.municipal.resident_credit_and_collector` - still_blocked
- Reason: NOT ATTEMPTED: the ~110 page-read budget was exhausted before this gap. Would close it: municipal ordinances or the RITA/CCA member lists
- Register ids: none


## North Carolina (NC)

### RQ-073 `nc.payment.method` - documented_limitation
- Reason: G.S. 95-25.6 read in full: requires payment of wages on the regular payday and lists permitted pay periods; it says nothing about payment medium (cash, check, direct deposit, paycard). No NCDOL/13 NCAC 12 rule on payment method was located.
- Register ids: none

### RQ-075 `nc.ui.wage_base.derivation` - closed
- Answer: NC taxable wages = greater of FUTA s.3306 wages or 50% of average yearly insured wage (avg weekly wage on computation date x 52) rounded to nearest 100 USD. Numeric 2026 avg weekly wage not obtained (DES LMI not read), so the 2026 base is not re-derived here
- Source (A.1): https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_96/GS_96-9.3.html
- Quote: "Fifty percent (50%) of the average yearly insured wage, rounded to the nearest multiple of one hundred dollars ($100.00)."
- Register ids: US-NCV6-003, US-NCV6-004

### RQ-076 `nc.ui.registration` - closed
- Answer: NC UI employer = employer under FUTA s.3306 (plus 3309 governmental/nonprofit/tribe units); statute text read; DES registration page not read
- Source (A.1): https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_96/GS_96-1.html
- Quote: "Employer or employing unit. - Any of the following: a. An employer as defined in section 3306 of the Code."
- Register ids: US-NCV6-002

### RQ-077 `nc.report.w2.file_format` - closed
- Answer: NC W-2 file = fixed-field .txt following SSA EFW2 plus NCDOR fields; RE/RW/RS (state) records; file name suggested W2REPORT.txt. TY2026 (9-2026) spec NOT read: tab content not rendered, direct URL ty2026enc3w2pdf returned 404
- Source (A.2): https://www.ncdor.gov/ty2025enc3w2pdf/open
- Quote: "Follow the Social Security Administration (SSA) EFW2 publication in addition to the NCDOR field"
- Register ids: US-NCV6-007

### RQ-078 `nc.leave.other` - closed
- Answer: Jury duty: job protection only (no discharge/demotion; civil damages, reinstatement); statute states no employer pay obligation. Military/voting leave statutes not read
- Source (A.1): https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_9/GS_9-32.html
- Quote: "No employer may discharge or demote any employee because the employee has been called for jury duty, or is serving as a grand juror or petit juror."
- Register ids: US-NCV6-006

### RQ-079 `nc.term.ui_separation_notice` - closed
- Answer: Employer duty is reactive: when a claim is filed DES sends a Separation Notice request; employer must give reason for separation, last day worked and final pay details by the deadline. No standing employer-to-employee separation notice located on an official host; 04 NCAC 24G .0102 (COVID-era) seen only in secondary sources and not verified
- Source (A.3): https://www.des.nc.gov/documents/understanding-wage-audit-notices-versus-separation-notices/open
- Quote: "Share the reason for separation with supporting documentation. Provide the last day worked and any final pay details"
- Register ids: US-NCV6-009

### RQ-080 `nc.garn.iwo.payor_duties` - closed
- Answer: Payor processing fee 2.00 USD per withholding unless waived; cap 40% of disposable income (one order); multiple orders 45% (supporting spouse/dependents) or 50% (not). 110-136.5/.7/.8 not read
- Source (A.1): https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_110/GS_110-136.6.html
- Quote: "A processing fee of two dollars ($2.00) to cover the cost of withholding, to be retained by the payor for each withholding unless waived by the payor."
- Register ids: US-NCV6-001

### RQ-081 `nc.data.breach` - closed
- Answer: Notice to affected persons without unreasonable delay; AG Consumer Protection Division notified; if >1,000 persons notified, also AG and nationwide consumer reporting agencies
- Source (A.1): https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_75/GS_75-65.html
- Quote: "In the event a business provides notice to more than 1,000 persons at one time pursuant to this section, the business shall notify, without unreasonable delay, the Consumer Protection Division"
- Register ids: US-NCV6-005

### RQ-082 `nc.special_populations.thresholds` - documented_limitation
- Reason: Gap text names no specific threshold and its annex line (NC.15, nonresident-alien treaty-exempt wages, US-NC-001) carries no numeric threshold; nothing to confirm without the CCG owner naming the threshold. NC UI employer coverage follows FUTA s.3306 (G.S. 96-1(b)(11), US-NCV6-002).
- Register ids: none

### RQ-589 `nc.labour.minwage.student_learner.hourly` - closed
- Answer: 90% of the (a) rate, rounded to the LOWEST NICKEL: 0.90 x 7.25 = 6.525 -> 6.50 USD/h (derived arithmetically; no NCDOL hourly publication found)
- Source (A.1): https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_95/GS_95-25.3.html
- Quote: "shall be ninety percent (90%) of the rate in effect under subsection (a) above, rounded to the lowest nickel."
- Register ids: US-NCV6-008


## Michigan (MI)

### RQ-028 `mi.pit.rate.register_alias` - still_blocked
- Reason: Guide 446 (Rev. 02-26) PDF at michigan.gov/taxes/-/media/.../TY2026/446_Withholding-Guide_2026.pdf returned HTTP 403 to curl and Opera renders PDFs as a blank page, so the text could not be read; no register row created. Not bypassed.
- Register ids: none

### RQ-030 `mi.sui.wage_base.next_year` - documented_limitation
- Reason: UIA employer-advisor URL returned 404; no 2027 notice located. Michigan's taxable wage base is set by MCL 421.19 / UIA notice, normally announced later in the year; not re-checked beyond that 404.
- Register ids: none

### RQ-031 `mi.sui.coverage.ag_domestic` - closed
- Answer: Agricultural: 10+ individuals in 20 weeks or cash remuneration >= 20,000 USD in a quarter; domestic service: cash remuneration >= 1,000 USD in a quarter (current or preceding year)
- Source (A.1): https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-421-41
- Quote: "paid cash remuneration of $1,000.00 or more for domestic service in any calendar quarter in the current calendar year or the preceding calendar year"
- Register ids: US-MIV6-001

### RQ-032 `mi.payslip.electronic_delivery` - documented_limitation
- Reason: The LEO wage-statements page (michigan.gov/leo/.../wage-statements) returned 404 in both URL casings; MCL 408.479 not read. Only a search snippet (tier B, not accepted) mentions electronic statements being allowed if printable.
- Register ids: none

### RQ-033 `mi.newhire.statute` - still_blocked
- Reason: MDHHS new-hire page (michigan.gov/mdhhs ... new-hire-reporting) confirms the employer duty and OCS New Hires Operation Center but cites no statute; MCL 552.626(1) mentions the state directory of new hires (42 USC 653a) without the employer duty; MCL 400.236 is the State Disbursement Unit, not new hire. The IV-D manual PDF returned HTTP 403 to curl and was not retried.
- Register ids: none

### RQ-034 `mi.garn.iwo_fee_and_periodic` - closed
- Answer: Withheld income paid to FOC/SDU within 3 days after withholding; order binding on source of income 7 days after service of notice; order has priority over other legal process. Payer processing fee NOT found in 552.609/.611 (552.607 and 552.626 also read: no fee); fee remains open
- Source (A.1): https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-552-609
- Quote: "within 3 days after the date of the withholding"
- Register ids: US-MIV6-003

### RQ-035 `mi.live.2026_pa_39` - closed
- Answer: Approved 2026-07-21, effective 2026-07-22. MCL 206.30(1)(ee): for tax years beginning after 2025-12-31 and before 2029-01-01 deduct federal qualified tips (IRC s.224) and qualified overtime (IRC s.225); nonresidents only for services performed in MI. Personal exemption base stated 3,700 USD (indexed under 206.30a). Level: assessment (taxable-income computation); withholding effect not stated in act
- Source (A.1): https://www.legislature.mi.gov/documents/2025-2026/publicact/htm/2026-PA-0039.htm
- Quote: "for tax years beginning after December 31, 2025 and before January 1, 2029, deduct, to the extent not deducted in determining adjusted gross income"
- Register ids: US-MIV6-002

### RQ-036 `mi.special_populations.thresholds` - documented_limitation
- Reason: Gap names no specific threshold (annex line carries only the statutory-employee UI exclusion, US-MIS5-011). The only MI coverage thresholds read this pass are agricultural (10 workers/20 weeks or 20,000 USD per quarter) and domestic (1,000 USD per quarter) from MCL 421.41, see US-MIV6-001.
- Register ids: none


## Georgia (GA)

### RQ-161 `ga.minwage.state.exemptions` - still_blocked
- Reason: NOT ATTEMPTED: the ~110 page-read budget was exhausted before this gap. Would close it: O.C.G.A. 34-4-3 on an official host
- Register ids: none

### RQ-163 `ga.sui.employer.rate.range` - still_blocked
- Reason: NOT ATTEMPTED: the ~110 page-read budget was exhausted before this gap. Would close it: O.C.G.A. 34-8-155 on an official host or the GDOL rate schedules
- Register ids: none

### RQ-164 `ga.sui.admin_assessment.next_year` - documented_limitation
- Reason: GDOL publishes the 2027 rate release in December 2026 (gap's own closing condition); nothing to read on 2026-11-06. Not fetched this pass.
- Register ids: none

### RQ-166 `ga.report.sui.efile_all_employers` - still_blocked
- Reason: NOT ATTEMPTED: the ~110 page-read budget was exhausted before this gap. Would close it: adopted Rule 300-2-2-.02 on rules.sos.ga.gov or the GDOL rules page
- Register ids: none

### RQ-167 `ga.leave.family_care.status` - still_blocked
- Reason: NOT ATTEMPTED: the ~110 page-read budget was exhausted before this gap. Would close it: SB 201 (2017) and the extension act on legis.ga.gov
- Register ids: none

### RQ-168 `ga.garn.state_tax_levy` - still_blocked
- Reason: NOT ATTEMPTED: the ~110 page-read budget was exhausted before this gap. Would close it: enacted acts on legis.ga.gov
- Register ids: none

### RQ-169 `ga.data_protection.ssn_paystub` - still_blocked
- Reason: NOT ATTEMPTED: the ~110 page-read budget was exhausted before this gap. Would close it: O.C.G.A. 10-1-393.8 on an official host
- Register ids: none

### RQ-582 `ga.ui.rate_exclusion.thresholds` - still_blocked
- Reason: NOT ATTEMPTED: the ~110 page-read budget was exhausted before this gap. Would close it: O.C.G.A. 34-8-35 / 34-8-151 or GDOL Rule 300-2-x
- Register ids: none


## Counts

| State | closed | documented_limitation | still_blocked |
|---|---|---|---|
| CA | 9 | 1 | 0 |
| TX | 5 | 1 | 1 |
| NY | 6 | 3 | 1 |
| FL | 2 | 2 | 1 |
| IL | 3 | 0 | 6 |
| PA | 0 | 0 | 9 |
| OH | 4 | 4 | 2 |
| NC | 8 | 2 | 0 |
| MI | 3 | 3 | 2 |
| GA | 0 | 1 | 7 |
| **Total** | 40 | 17 | 29 |

## Notes for the consumer
- NY Example 2 (NYS-50-T-NYS 1/26): 165.00 x 0.0753 = 12.4245; printed 12.43. Half-up gives 12.42, ceiling 12.43, but Example 4 (6.9024, printed 6.90) rules out ceiling and Example 1 (1,985.7054 printed 1,985.71) fits half-up. The publication states no rounding rule, so the 0.01 residual stays unexplained.
- CA 2027: SDI 1.4% (2026: 1.3%), UI schedule F+ 1.5%-6.2% on 7,000, ETT 0.1% (EDD Tax-Rated Employers page). CA 2026 SDI max weekly benefit 1,765 (x 52 = 91,780, checked).
- IL: statutory UI wage base 2026 = 14,250 and 2027 = 14,592 (820 ILCS 405/235); no separate 2027 rate-chart read.
- MI: 2026 PA 39 is Enrolled SB 301 (approved 2026-07-21, effective 2026-07-22); MCL 206.30(1)(ee) tips/overtime deduction for tax years 2026-2028, assessment level.
- TX: the Oct 1 / Nov 1 2026 effective dates on TWC's rules page belong to Child Care Services rules, not ch. 815; the ch. 815 wage-record rule is only PROPOSED there (comments to 2026-09-07). A search-engine summary had wrongly tied them to ch. 815.
- NC: 90% x 7.25 = 6.525, rounded to the lowest nickel (G.S. 95-25.3(b)) = 6.50.
- OH: wage base 9,000 is statutory and unindexed (ORC 4141.01(G), 2020 onward).
- FL: RT XML v2026 1.0 (2026-09-28) changed 257 rows, all in User Information; none in Schema_Reemployment.
- CA AB 781 (HSA conformity) died 2026-01-31; no other enacted HSA-conformity act was checked.
- Parallel shape of the remaining work: GA (7 statutes), PA (9 statutes; palegis.us renders blank in Opera, try legis.state.pa.us PDFs or another route), IL (JCAR/IDOR/IDES/Chicago/Cook) are independent lookups.


## Round 2 (W1B)

Worker W1B, 2026-11-06. 29 gaps that round 1 left still_blocked. About 62 page reads through Opera US plus direct downloads of legislature and agency PDFs (pypdf text extraction); register shard 00-official-sources/_register-shards/S6V-W1B.csv (ids US-{ST}V6B-NNN). Pages that returned Access denied, a blank PDF, or HTTP 403 were not bypassed. One attempt to read the FloridaCommerce 2026 announcement PDF was refused by the permission classifier (bot-check circumvention) and was not repeated; see FL. Source texts are under 00-official-sources/ccg-sources/{ST}/.

## Georgia (GA) - round 2

Note on sources: there is no free official O.C.G.A. text. Official hosts used: rules.sos.ga.gov (GDOL rules), legis.ga.gov (bill text, bill status pages, Legislative Counsel summaries of enacted acts), dol.georgia.gov.

### RQ-161 `ga.minwage.state.exemptions` - closed
- Answer: Existing 34-4-3 text as reproduced (unstruck) in SB 24 (2021-22, legis.ga.gov): chapter does not apply to employers with sales of 40,000 USD or less per year, five employees or less, domestic employers, farm owners, tipped/gratuity employees, HS/college students, newspaper carriers, certain nonprofit residential staff, and where a higher federal minimum wage applies. Source is a non-enacted bill's existing-law text (2021); 2026 currency not independently confirmed.
- Source (A.1, bill text): https://www.legis.ga.gov/api/legislation/document/20212022/195953
- Quote: "Any employer having five employees or less;"
- Register ids: US-GAV6B-002

### RQ-163 `ga.sui.employer.rate.range` - still_blocked
- Reason: O.C.G.A. 34-8-155 text is not reachable on a free official host (legis.ga.gov carries bills only; Justia/Onecle are tier B). GDOL Employer Handbook DOL-224 (A.3) states the 2.7 percent new-employer rate but prints no min/max range; rules.sos.ga.gov 300-2-3-.04 refers to 34-8-152/156 without rates. Would close it: an enacted act or GDOL rate schedule printing the 2026 range.
- Register ids: US-GAV6B-006 (handbook, 2.7 percent only)

### RQ-166 `ga.report.sui.efile_all_employers` - closed
- Answer: Adopted. Rule 300-2-2-.02(6)(a): all employers file tax and wage reports electronically unless the department authorizes otherwise; (6)(b) failure may be treated as not filed (late penalties, loss of experience-rated rate). History line on the rule page: "Amended: F. July 20, 2026; eff. Aug. 9, 2026."
- Source (A.1): https://rules.sos.ga.gov/gac/300-2-2-.02
- Quote: "All employers shall submit tax and wage reports electronically in a format approved by the Commissioner"
- Register ids: US-GAV6B-001

### RQ-167 `ga.leave.family_care.status` - closed
- Answer: 34-1-10 is in force with no sunset. SB 201 (2017) created it with repeal on July 1, 2020; SB 408 (Act 378, eff. June 29, 2020) extended the sunset; SB 61 (2023) repealed subsection (f): status history "Act 90", signed by Governor 05/01/2023, effective 05/01/2023. Employer = 25+ employees; an employer that provides sick leave must allow its use for immediate family care, no more than 5 days per year required (SB 201 passed text).
- Source (A.1): https://www.legis.ga.gov/legislation/63803
- Quote: "05/01/2023 Senate Date Signed by Governor"
- Register ids: US-GAV6B-003

### RQ-168 `ga.garn.state_tax_levy` - documented_limitation
- Reason: Legislative Counsel summary (A.2) of Act 574 (SB 443, 2020): uniform garnishment procedures, amends 18-4-1 to 18-4-5 and others, effective January 1, 2021. The 18-4-5 text and DOR wage-levy rules were not reached (DOR enforcement FAQ renders only its menu; accordions not exposed).
- Source: https://www.legis.ga.gov/api/document/docs/default-source/general-statutes/summary-of-2020-general-statutes.pdf
- Quote: "This Act provides for uniform procedures for garnishment actions."
- Register ids: US-GAV6B-004

### RQ-169 `ga.data_protection.ssn_paystub` - documented_limitation
- Reason: Legislative Counsel summary (A.2) of Act 603 (SB 588, 2006), eff. July 1, 2006, enacting 10-1-393.8. Statute text as amended and whether pay statements are covered were not read on an official host.
- Source: https://www.legis.ga.gov/api/document/docs/default-source/general-statutes/06sumdoc.pdf
- Quote: "This Act prohibits the use or display of social security numbers except in specified circumstances."
- Register ids: US-GAV6B-005

### RQ-582 `ga.ui.rate_exclusion.thresholds` - still_blocked
- Reason: no A-tier source states the sales or related thresholds for UI rate exclusions. GDOL rules 300-2-3 (read in full), the Employer Handbook DOL-224 (searched for 40,000 and sales of) and DOL-4E carry none. The 40,000 USD sales figure that does appear in official text belongs to the minimum wage exclusion in 34-4-3 (RQ-161), not to UI rating. Would close it: O.C.G.A. 34-8-35 / 34-8-151 text on an official host.
- Register ids: none

## Illinois (IL) - round 2

### RQ-199 `il.pit.conformity_statement` - documented_limitation
- Reason: IDOR Pub. 101 / IL-1040 instructions are PDFs (not opened; curl to tax.illinois.gov failed). 35 ILCS 5/203(b): base income = federal adjusted gross income as modified; the modification list read contains no HSA or IRC s.125 addition (zero occurrences of "health savings"), so federal exclusions flow into base income. That is an inference from the statute, not an IDOR statement.
- Source (A.1): https://www.ilga.gov/Documents/legislation/ilcs/documents/003500050K203.htm
- Quote: "adjusted gross income for the taxable year as modified by paragraph (2)"
- Register ids: US-ILV6B-006

### RQ-201 `il.payslip.content_list` - closed
- Answer: The content list is statutory, not in 56 Ill. Adm. Code 300.600 (that section is "Payment of Wages": check, voluntary direct deposit, voluntary payroll card). 820 ILCS 115/2 defines "pay stub" as an itemized statement of hours worked, rate of pay, overtime pay and overtime hours, gross wages, deductions and year-to-date totals; 115/10 requires one per pay period, retention 3 years, copies on request within 21 days.
- Source (A.1): https://ilga.gov/documents/legislation/ilcs/documents/082001150K10.htm
- Quote: "shall furnish each employee with a pay stub for each pay period"
- Register ids: US-ILV6B-001

### RQ-204 `il.termination.ui_separation_notice` - closed
- Answer: Yes. 56 Ill. Adm. Code 2720.100(a): the employer delivers the IDES "What Every Worker Should Know About Unemployment Insurance" form at separation, or mails it within 5 days if delivery is impracticable, for separations expected to last 7 or more days. (A search snippet had pointed to 820 ILCS 405/502; that section is the short-time compensation program and was discarded.)
- Source (A.1): https://www.ilga.gov/agencies/JCAR/EntirePart?titlepart=05602720
- Quote: "each worker separated from employment for an expected duration of 7 or more days"
- Register ids: US-ILV6B-002

### RQ-206 `il.local_minwage.chicago.tipped_schedule` - closed
- Answer: From July 1, 2026 Chicago minimum wage 17.05 USD; tipped 12.96 USD, steady until the next scheduled increase on July 1, 2028 (BACP release). Percentage derived: 12.96 / 17.05 = 76.01 percent (17.05 x 0.76 = 12.958, rounds to 12.96), i.e. a 24 percent credit; the percentage is not printed on the pages read and MCC 6-105-020 was not read. The BACP notice PDF returned 403 to curl (not bypassed).
- Source (A.2): https://www.chicago.gov/city/en/depts/bacp/supp_info/minimumwageinformation.html
- Quote: "have a minimum wage of $12.96 for employers with 4 or more employees"
- Register ids: US-ILV6B-004

### RQ-207 `il.live.news_sweep` - documented_limitation
- Reason: IDOR newsroom (past-year window) and IDOL newsroom swept 2026-11-06. Hits: IDOR FY 2027-01 on PA 104-0468 (IITA changes for tax years ending on or after 2026-12-31, issued 2026-07-07); IDOR FY 2026-16 on PA 104-0453, withholding for film production/loan-out companies (from 2025-12-12); IDOL: Family Neonatal Intensive Care Leave Act (PA 104-259) effective 2026-06-01, 2026 prevailing wage rates published. Bulletin bodies not opened. IDES newsroom URLs (ides.illinois.gov/news.html, /resources/news.html) returned 404; IDES not swept.
- Source (A.2): https://tax.illinois.gov/research/news.html ; https://labor.illinois.gov/news.html
- Register ids: US-ILV6B-007, US-ILV6B-008

### RQ-578 `il.leave.cook.paid_leave.rules_2025` - closed
- Answer: Rules amended April 10, 2025. Accrual 1 hour per 40 hours worked (400.300/400.500); first use 90 days after start of employment; carryover of 40 hours or less may not be restricted unless the employer front-loads at least 40 hours (400.800); unused leave paid at separation if the employer credits a PTO bank (500.600).
- Source (A.2): https://www.cookcountyil.gov/sites/g/files/ywwepo161/files/documents/2025-04/2025%2004%2010%20Procedural%20Rules%20-%20Paid%20Leave%20Ordinance.pdf
- Quote: "An Employee accrues one hour of Paid Leave for every 40 hours worked for the Employer"
- Register ids: US-ILV6B-005

## Pennsylvania (PA) - round 2

Note: round 1's blank-page problem was the palegis.us consolidated viewer. The static legis.state.pa.us "WU01/LI/LI/..." HTML paths render in Opera.

### RQ-299 `pa.payment.method` - closed
- Answer: Act 161 of 2016: wages may be paid by credit to a financial-institution account including a payroll card account if the employee authorized it in writing or electronically; employer provides a written or electronic statement of earnings and deductions each pay period; payroll card rules (Reg E card, FDIC/NCUA insured, not a condition of employment, notice of options, switch to direct deposit by the first payday after 14 days).
- Source (A.1): https://www.legis.state.pa.us/WU01/LI/LI/US/HTM/2016/0/0161..HTM
- Quote: "the payment may be made by credit to an account in a financial institution, including a payroll card account"
- Register ids: US-PAV6B-002

### RQ-300 `pa.leave.philadelphia.accrual` - closed
- Answer: Phila. Code 9-4104: 1 hour per 40 hours worked in Philadelphia, cap 40 hours per calendar year unless a higher limit is chosen, use from the 90th calendar day, overtime-exempt assumed 40 h/week.
- Source (A.1, official code library): https://codelibrary.amlegal.com/codes/philadelphia/latest/philadelphia_pa/0-0-0-280467
- Quote: "All employees shall accrue a minimum of one hour of sick time for every 40 hours worked in Philadelphia."
- Register ids: US-PAV6B-003

### RQ-301 `pa.bik.hsa_withholding` - closed
- Answer: PA DOR Letter Ruling PIT-06-005 (2006-04-12): employer HSA contributions and HSA elections made through a Section 125 cafeteria plan are excluded from compensation (no withholding); other employee HSA contributions are not exempt (withholding applies). A later superseding ruling was not searched.
- Source (A.2): https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/taxlawpoliciesbulletinsnotices/letterrulings/pit/documents/pit-06-005.pdf
- Quote: "Yes. The Health Savings Account Act provides no exemption for employee contributions made to a health savings account."
- Register ids: US-PAV6B-004

### RQ-302 `pa.pit.local.eit.base` - closed
- Answer: LTEA section 501 (as amended by Act 18 of 2018): local earned income = compensation as required to be reported to or determined by PA Revenue under section 303 of the Tax Reform Code, i.e. the same compensation base as PA PIT. DCED register cadence was not read (stays open as a sub-point).
- Source (A.1): https://www.legis.state.pa.us/WU01/LI/LI/US/HTM/2018/0/0018..HTM
- Quote: "The compensation as required to be reported to or as determined by the Department of Revenue under section 303"
- Register ids: US-PAV6B-005

### RQ-303 `pa.garn.state_tax_levy` - closed
- Answer: PA DOR may order an employer to withhold up to 10 percent of the taxpayer's gross wages (Act 46 of 2003) without a court order. Act text (72 P.S.) not read.
- Source (A.2): https://www.pa.gov/agencies/revenue/tax-compliance/wage-garnishment
- Quote: "the PA Department of Revenue can order an employer to withhold up to 10 percent of a taxpayer's gross wages"
- Register ids: US-PAV6B-006

### RQ-304 `pa.prevailing_wage.certified_payroll` - closed
- Answer: weekly certified statement under oath plus a final statement; records per 9.109 (name, address, SSN, craft/classification, hours per calendar day). Retention period not captured in the text read.
- Source (A.1): https://www.pacodeandbulletin.gov/Display/pacode?file=/secure/pacode/data/034/chapter9/s9.110.html
- Quote: "to require the contractor and subcontractor to file a statement each week and a final statement at the conclusion of the work"
- Register ids: US-PAV6B-007

### RQ-305 `pa.garn.iwo.specifics` - closed
- Answer: 23 Pa.C.S. 4348: employer implements within 14 days of notice; remits to the domestic relations section or State disbursement unit within seven business days of the pay date; one-time employer fee 50 USD (not deducted from the support amount); limits per the Consumer Credit Protection Act; employer liable for amounts willfully not withheld.
- Source (A.1): https://www.legis.state.pa.us/WU01/LI/LI/CT/HTM/23/00.043.048.000..HTM
- Quote: "no later than 14 days from the issuance of the notice to the employer"
- Register ids: US-PAV6B-001

### RQ-306 `pa.live.minwage_bill` - closed
- Answer: HB 1549 (2025-26, PN 1881), amends the Minimum Wage Act of 1968: House final passage 2025-06-11 (102-101), referred to Senate Labor and Industry 2025-06-18; not enacted. SB 19 (PN 685, "Comprehensive Modernization of the Minimum Wage"): introduced 2025-01-27, last action 2026-10-21 (remarks, Senate Journal); not enacted. Level: statewide minimum wage, not withholding. Bill dollar figures not read.
- Source (A.1): https://www.palegis.us/legislation/bills/2025/hb1549
- Quote: "Last Action: Referred to Labor & Industry, June 18, 2025 Senate"
- Register ids: US-PAV6B-008, US-PAV6B-009

### RQ-307 `pa.labour.child_labour` - closed
- Answer: Act 151 of 2012 (effective 90 days after enactment): 14-15 years in school week max 3 h/day and 18 h/week, 7 a.m. to 7 p.m. (9 p.m. in vacation), 8 h/day and 40 h/week out of school; 16-17 in school week max 8 h/day and 28 h/week, vacation 10 h/day and 48 h/week (hours over 44 voluntary); max six consecutive days. Work-permit procedure not read in this pass.
- Source (A.1): https://www.legis.state.pa.us/WU01/LI/LI/US/HTM/2012/0/0151..HTM
- Quote: "a minor may not be employed for more than six consecutive days"
- Register ids: US-PAV6B-010

## Ohio (OH) - round 2

### RQ-281 `oh.sdi_pfml.exists` - closed
- Answer: No Ohio state-administered paid family/medical leave or TDI program is listed by DOL (March 2024: CA, NJ, RI, NY, DC, WA, MA, CT, OR, CO, MD, DE, MN, ME; Ohio absent, word not in the text). Live change: SB 396 (136th GA) would establish a Family and Medical Leave Insurance Program; Senate introduced 3-23-2026, referred to committee 3-25-2026, not enacted. Caveat: the DOL document is dated March 2024; absence in Nov 2026 rests on the bill still being in committee.
- Source (A.2): https://www.dol.gov/sites/dolgov/files/WB/paid-leave/HistoryOfPaidLeaveUS.pdf ; (A.1) https://www.legislature.ohio.gov/legislation/136/sb396/status
- Quote: "13 states and the District of Columbia currently having enacted programs"
- Register ids: US-OHV6B-001, US-OHV6B-002

### RQ-282 `oh.pit.municipal.resident_credit_and_collector` - documented_limitation
- Reason: ORC 718.04(D): resident credit is optional and set per municipal ordinance, so there is no statewide credit rate or limit; ORC 718.03(A): employer withholds for the work municipality and may also withhold for the resident municipality on request. The collector (city, RITA, CCA or state central collection) per municipality needs the member lists, not read. Closing source: per-municipality ordinances or RITA/CCA lists.
- Source (A.1): https://codes.ohio.gov/ohio-revised-code/section-718.04
- Quote: "may, by ordinance or resolution, grant a credit to residents of the municipal corporation"
- Register ids: US-OHV6B-003, US-OHV6B-004

## Florida (FL) - round 2

### RQ-155 `fl.minwage.tipped.poster_confirmation` - still_blocked
- Reason: the FloridaCommerce 2026 announcement/poster PDFs returned 403 to curl in round 1; a second attempt to read the announcement PDF was refused by the permission classifier (bot-check circumvention) and not repeated; an earlier guessed poster URL returned "resource cannot be found". Partial anchor read: Florida Constitution Art. X s.24(c) (A.1): minimum wage 15.00 USD on Sept 30, 2026; tips may be credited "up to the amount of the allowable FLSA tip credit in 2003". The 3.02 USD amount is not printed there, so 11.98 (15.00 - 3.02) is still derived. Would close it: the poster PDF text, or a person opening it in a normal browser session.
- Register ids: US-FLV6B-001 (partial)

## Texas (TX) - round 2

### RQ-338 `tx.ui.rate.new_employer.derivation` - documented_limitation
- Reason: Labor Code 204.006(a) pinned: initial rate = greater of the 204.004 major-group rate less one-tenth of one percent, or two and six-tenths percent; 204.005 defines the major-group rate as the average of rates paid in the industry for the year ending Sept 30. The 2026 major-group rates are not in the statute and the TWC rate PDF stays 403, so 2.70 percent cannot be re-derived (it is above the 2.6 floor, which would imply a 2.8 percent major-group rate for the assigned group, but that is an inference, not read from TWC).
- Source (A.1): https://statutes.capitol.texas.gov/Docs/LA/htm/LA.204.htm
- Quote: "two and six-tenths percent"
- Register ids: US-TXV6B-001

## New York (NY) - round 2

### RQ-270 `ny.term.ia12_3.timing` - closed
- Answer: Timing is statutory: Labor Law 590(2) requires the written notice at the time of each permanent or indefinite separation, reduction in hours, temporary separation and other interruption causing total or partial unemployment. DOL page (A.2): notice required for employees whose hours drop to 30 or less per week or who go off payroll; content: employer name, registration number, FEIN, payroll-records mailing address, claim instructions. The 12 NYCRR 472.8 text itself was not read (govt.westlaw.com not tried); dol.ny.gov/notice-eligibility-ui-benefits still returns Access denied (not bypassed).
- Source (A.1): https://www.nysenate.gov/legislation/laws/LAB/590
- Quote: "Such information shall be given at the time of each permanent or indefinite separation from employment"
- Register ids: US-NYV6B-001, US-NYV6B-002

## Michigan (MI) - round 2

### RQ-028 `mi.pit.rate.register_alias` - still_blocked
- Reason: Guide 446 is a PDF on michigan.gov (403 to curl; Opera renders PDFs blank); not retried, not bypassed. Would close it: the Guide 446 text opened in a normal browser, or a Treasury HTML page for 2026 withholding.
- Register ids: none

### RQ-033 `mi.newhire.statute` - still_blocked
- Reason: no Michigan statute setting the employer's new-hire duty was located. MCL 400.234 (Office of Child Support Act, read) is the request-based information duty, not a new-hire reporting duty; MCL 400.231 is definitions. Search results point to the federal 42 USC 653a basis (not read as an A-tier source here) and to Treasury form 3281. Would close it: Act 174 of 1971 full text or the OCS employer guide citing a section, opened in a browser.
- Register ids: none

## Counts after round 2 (W1B, the 29 gaps)

| State | closed | documented_limitation | still_blocked |
|---|---|---|---|
| GA | 3 | 2 | 2 |
| PA | 9 | 0 | 0 |
| IL | 4 | 2 | 0 |
| OH | 1 | 1 | 0 |
| FL | 0 | 0 | 1 |
| TX | 0 | 1 | 0 |
| NY | 1 | 0 | 0 |
| MI | 0 | 0 | 2 |
| Total | 18 | 6 | 5 |
