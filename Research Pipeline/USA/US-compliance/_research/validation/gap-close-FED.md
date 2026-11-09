# Gap close: worker FED (per-state validation pilot, step 1)

Run date 2026-11-06. Channel: curl and Opera (US exit). Register shard: 00-official-sources/_register-shards/S6V-FED.csv (ids US-FEDV6-001 to -043). Source texts: 00-official-sources/ccg-sources/FED/. Several gaps share one answer, so they are grouped.

## RQ-402 fed.futa.credit_reduction.ca
- result: **still_blocked**
- answer: Not final until after 2026-11-10 (today 2026-11-06). Potential 2026 total for California is 0.053 (xlsx cells 0.015 + 0.038 BCR add-on; sum checked). Re-read the DOL page and xlsx after 2026-11-10.
- source: https://oui.doleta.gov/unemploy/futa_credit.asp
- quote: "the final credit reduction for any given year is not determined until Nov. 10 of that year" (local: FED_dol-futa-credit-reductions.txt)
- register ids: US-FEDV6-001, US-FEDV6-002

## RQ-403 fed.futa.credit_reduction.vi
- result: **still_blocked**
- answer: Same determination date. Potential 2026 total for the Virgin Islands is 0.048 (xlsx cell 4.8000000000000001E-2). Final value after 2026-11-10.
- source: https://oui.doleta.gov/unemploy/futa_credit.asp
- quote: "the final credit reduction for any given year is not determined until Nov. 10 of that year" (local: FED_dol-futa-credit-reductions.txt)
- register ids: US-FEDV6-001, US-FEDV6-002

## RQ-404 fed.fica.oasdi.wage_base.next_year_reverification
- result: **closed**
- answer: SSA's own page, read from the US exit, confirms the 2027 OASDI contribution and benefit base of 192,300 (US-FED-022 re-verified); 6.2% rate; 11,922.60 maximum per party.
- source: https://www.ssa.gov/oact/cola/cbb.html
- quote: "For earnings in 2027, this base is $192,300." (local: FED_ssa-cbb.txt)
- register ids: US-FEDV6-003

## RQ-530 fed.indexation.publication_2027
- result: **closed**
- answer: IRS issued Rev. Proc. 2026-35 on 2026-11-05 (IR-2026-133). Payroll-relevant 2027 figures stated: qualified transportation fringe and parking 350 per month; health FSA salary-reduction limit 3,500; standard deduction single 16,600, MFJ 33,200. OASDI base 192,300 (RQ-404). Not yet published on 2026-11-06: 2027 Pub. 15-T tables (newest p15t draft is the Dec 2025 one for 2026) and the 2027 retirement-plan limits notice (not in the IRS newsroom list). Rev. Proc. text saved, not transcribed.
- source: https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2027-taxpayers-continue-to-benefit-from-the-working-families-tax-cuts
- quote: "the monthly limitation for the qualified transportation fringe benefit and the monthly limitation for qualified parking increases to $350" (local: FED_irs-IR-2026-133-ty2027-adjustments.txt)
- register ids: US-FEDV6-003, US-FEDV6-004, US-FEDV6-005

## RQ-405 fed.indexation.next_year
- result: **still_blocked**
- answer: Partly closed: the TY2027 Rev. Proc. is out (Rev. Proc. 2026-35, 2026-11-05). Still unpublished on 2026-11-06: the 2027 Pub. 15-T and the 2027 retirement-plan limits notice. Re-check irs.gov/pub/irs-pdf/p15t.pdf and the newsroom in Nov-Dec 2026.
- source: https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2027-taxpayers-continue-to-benefit-from-the-working-families-tax-cuts
- quote: "Revenue Procedure 2026-35 PDF provides details about these annual adjustments." (local: FED_irs-IR-2026-133-ty2027-adjustments.txt)
- register ids: US-FEDV6-004, US-FEDV6-005

## RQ-406 fed.form940.instructions_edition / RQ-526 fed.form940.instructions_current (Form 940 part)
- result: **documented_limitation**
- answer: Final TY2026 Instructions for Form 940 are not issued (irs-pdf/i940.pdf is still the 2025 edition, last modified 2025-11-25). An early-release draft posted 2026-09-22 shows: due date Feb 1, 2027 (Feb 10, 2027 if all FUTA deposited); FUTA wage base 7,000 unchanged; dependent care exclusion limit raised to 7,500. Treat as draft until final.
- source: https://www.irs.gov/pub/irs-dft/i940--dft.pdf
- quote: "The due date for filing Form 940 for 2026 is February 1, 2027." (local: FED_irs-i940-draft-2026-09-22.txt)
- register ids: US-FEDV6-006

## RQ-407 fed.aca.instructions_edition / SIR-RQ-02 fed.aca.efile_threshold.ty2026 / RQ-526 fed.form940.instructions_current (1094-C/1095-C part)
- result: **documented_limitation**
- answer: Final 2026 Instructions for Forms 1094-C/1095-C are not issued (i109495c.pdf is still the 2025 edition, last modified 2025-11-05). The early-release draft of 2026-10-16 states the electronic-filing threshold as 10 or more information returns in the aggregate. Draft value only.
- source: https://www.irs.gov/pub/irs-dft/i109495c--dft.pdf
- quote: "If you are required to file 10 or more information returns during the year, you must file the forms electronically." (local: FED_irs-i109495c-draft-2026-10-16.txt)
- register ids: US-FEDV6-007

## RQ-408 fed.leave.eo13706.accrual / RQ-518 fed.eo13706.sick_leave.accrual
- result: **closed**
- answer: Accrual: 1 hour of paid sick leave per 30 hours worked on or in connection with a covered contract; a contractor may cap accrual at not less than 56 hours per accrual year. Caveat: the DOL WHD EO 13706 page returned 404 and the current status of EO 13706 itself was not established from an official source; eCFR still carries 29 CFR 13.5 as of 2026-11-01.
- source: https://www.ecfr.gov/current/title-29/subtitle-A/part-13/section-13.5
- quote: "A contractor shall permit an employee to accrue not less than 1 hour of paid sick leave for every 30 hours worked" (local: FED_ecfr-29cfr13.5.txt)
- register ids: US-FEDV6-008

## RQ-409 fed.bik.mileage_rate / RQ-536 fed.bik.business_mileage.rate
- result: **closed**
- answer: 2026 business standard mileage rate is split: 72.5 cents per mile for 2026-01-01 to 2026-06-30 (Notice 2026-10) and 76 cents per mile from 2026-07-01 (Announcement 2026-11, IRB 2026-29, IR-2026-29). Medical and moving 20.5 then 23.5; charity 14. The current-rate instrument is Announcement 2026-11, not a Notice; a search-engine summary calling it Notice 2026-29 was wrong (29 is the bulletin number).
- source: https://www.irs.gov/irb/2026-29_irb
- quote: "(1) Business 76 cents per mile" (local: FED_irs-irb-2026-29-announcement-2026-11.txt)
- register ids: US-FEDV6-009, US-FEDV6-010, US-FEDV6-011

## RQ-410 fed.iwo.revised_form_go_live / RQ-528 fed.iwo.revised_form.state_golive
- result: **documented_limitation**
- answer: No OCSE Action Transmittal with state go-live dates for the gig-worker revision (ICR 202607-0970-002) was found. The OIRA record gives states an extension to reprogram and then requires the revised form, without a date. The posted IWO instructions (OMB 0970-0154) show expiry 08/31/2029. Closing document: an OCSE Action Transmittal; two guessed acf.gov/css paths returned 404.
- source: https://www.reginfo.gov/public/do/PRAViewICR?ref_nbr=202607-0970-002
- quote: "Once the system is programmed, states will then be required to use the revised version of the IWO and e-IWO." (local: FED_OIRA-ICR-202607-0970-002_2026-11-02.html)
- register ids: US-FEDV6-012, US-FEDV6-013

## RQ-517 fed.fmla.eligibility
- result: **closed**
- answer: Employer coverage: 50 or more employees for 20 or more workweeks in the current or preceding calendar year (825.104). Employee eligibility: 12 months of employment, 1,250 hours in the prior 12 months, worksite with 50 or more employees within 75 miles (825.110).
- source: https://www.ecfr.gov/current/title-29/subtitle-B/chapter-V/part-825/subpart-A/section-825.110
- quote: "worksite where 50 or more employees are employed by the employer within 75 miles of that worksite" (local: FED_ecfr-29cfr825.110.txt)
- register ids: US-FEDV6-014, US-FEDV6-015, US-FEDV6-016

## RQ-521 fed.pfml.employer_top_up.treatment
- result: **closed**
- answer: An employer-paid supplement is employer sick pay: employee and employer FICA and FUTA apply, and income tax withholding is mandatory. Caveat: Pub. 15-A does not mention State PFML/TDI explicitly; the answer rests on the general sick-pay rule. The State-paid benefit is not employer wages (not addressed in the publication read). W-2 box reporting not separately quoted.
- source: https://www.irs.gov/pub/irs-pdf/p15a.pdf
- quote: "Sick pay paid by you or your agent is subject to mandatory federal income tax withholding." (local: FED_irs-p15a-2026-text.txt)
- register ids: US-FEDV6-017

## RQ-522 fed.userra.leave_rules
- result: **documented_limitation**
- answer: Tax side closed: differential wage payments (active duty over 30 days) are wages for income tax withholding but not FICA or FUTA, reported in W-2 box 1. USERRA statute texts 4312, 4316, 4317 are saved but the cumulative service limit and pension rule (38 U.S.C. 4318, not fetched) were not extracted; read the saved files to close the rest.
- source: https://www.irs.gov/pub/irs-pdf/p15.pdf
- quote: "Differential wage payments are wages for income tax withholding, but aren't subject to social security, Medicare, or FUTA tax." (local: FED_irs-p15-2026-text.txt)
- register ids: US-FEDV6-018, US-FEDV6-019, US-FEDV6-020, US-FEDV6-021

## RQ-525 fed.backpay.treatment
- result: **closed**
- answer: Back pay and retroactive increases are ordinary wages taxed in the year paid (FICA); for income tax withholding Pub. 15 lists back pay and retroactive pay increases among supplemental wages. SSA credits back pay as wages in the year paid.
- source: https://www.irs.gov/pub/irs-pdf/p15.pdf
- quote: "Back pay, including retroactive wage increases (but not amounts paid as liquidated damages), is taxed as ordinary wages in the year paid." (local: FED_irs-p15-2026-text.txt)
- register ids: US-FEDV6-018, US-FEDV6-022

## RQ-532 fed.fit.pay_frequency_change
- result: **documented_limitation**
- answer: No federal rule specific to a mid-year change of payroll frequency was found in Pub. 15 or Pub. 15-T 2026. The published rule: with a regular payroll period, withhold for that period; with no regular period use the daily/miscellaneous method counting the days in the period.
- source: https://www.irs.gov/pub/irs-pdf/p15.pdf
- quote: "When you have a regular payroll period, withhold income tax for that time period even if your employee doesn't work the full period." (local: FED_irs-p15-2026-text.txt)
- register ids: US-FEDV6-018

## RQ-533 fed.common_paymaster.rule
- result: **documented_limitation**
- answer: Common paymaster closed: each related corporation is treated as paying only what it disburses, taxes are figured as if one employer, and the common paymaster files returns and W-2s. The successor-employer wage-base rule (26 U.S.C. 3121(a)(1), 3306(b)(1)) was not extracted; closing documents are the already-saved 26 U.S.C. 3121 and 3306 files.
- source: https://www.ecfr.gov/current/title-26/chapter-I/subchapter-C/part-31/subpart-B/section-31.3121(s)-1
- quote: "is determined as though the individual has only one employer" (local: FED_ecfr-26cfr31.3121s-1.txt)
- register ids: US-FEDV6-023

## RQ-535 fed.nra.residency_change
- result: **documented_limitation**
- answer: Partly closed. FICA: the F/J exception covers a nonresident alien and does not apply where inconsistent with section 7701(b), so a resident alien is not exempt. Withholding: Pub. 15 states the nonresident add-on and W-4 conditions (single status, no exemption) apply to nonresident aliens. A dual-status-year W-4 replacement procedure was not found in the publications read (Pub. 515 not read).
- source: https://www.ecfr.gov/current/title-26/chapter-I/subchapter-C/part-31/subpart-B/section-31.3121(b)(19)-1
- quote: "The preceding sentence does not apply to the extent it is inconsistent with section 7701(b) and the regulations under that section." (local: FED_ecfr-26cfr31.3121b19-1.txt)
- register ids: US-FEDV6-024, US-FEDV6-018

## RQ-546 fed.student_loan.payroll_obligation
- result: **closed**
- answer: Federal administrative wage garnishment of student loans: maximum 15 percent of disposable pay (more only with written consent), 30 days' written notice, no deduction until 12 months of continuous reemployment after involuntary separation, no retaliation. Disposable pay = after amounts required by law to be withheld.
- source: https://www.govinfo.gov/link/uscode/20/1095a
- quote: "the amount deducted for any pay period may not exceed 15 percent of disposable pay" (local: FED_govinfo-20USC1095a.txt)
- register ids: US-FEDV6-025, US-FEDV6-026

## RQ-556 fed.registration.number_formats
- result: **documented_limitation**
- answer: Federal EIN closed: nine digits, XX-XXXXXXX. State withholding and unemployment account number formats sit on per-State registration pages, outside this worker's scope; parallel fan-out over 51 jurisdictions.
- source: https://www.irs.gov/pub/irs-pdf/p1635.pdf
- quote: "An Employer Identification Number (EIN) is a nine-digit number that IRS assigns in the following format: XX-XXXXXXX." (local: FED_irs-p1635-understanding-ein.txt)
- register ids: US-FEDV6-027

## RQ-557 fed.ssn.format
- result: **documented_limitation**
- answer: SSN: nine digits (Pub. 15 display 000-00-0000); SSA excludes area numbers 000, 666 and 900-999 from assignment; the W-2 electronic file takes digits only and rejects a leading 666 or 9. ITIN: nine-digit number issued by IRS (W-7). Not found in the IRS text read: the ITIN 4th and 5th digit ranges.
- source: https://www.ssa.gov/employer/randomization.html
- quote: "excluding area numbers 000, 666 and 900-999" (local: FED_ssa-ssn-randomization.txt)
- register ids: US-FEDV6-028, US-FEDV6-029, US-FEDV6-030, US-FEDV6-018

## RQ-558 fed.payroll_data_protection.framework
- result: **documented_limitation**
- answer: Federal items located: FTC Disposal Rule 16 CFR 682.3 (reasonable measures when disposing of consumer information) and employment-tax record retention of at least four years (26 CFR 31.6001-1). State SSN-protection and breach-notification statutes were not researched (51-jurisdiction fan-out). Applicability of the Disposal Rule to employer-held payroll data was not established.
- source: https://www.ecfr.gov/current/title-16/chapter-I/subchapter-F/part-682/section-682.3
- quote: "must properly dispose of such information by taking reasonable measures to protect against unauthorized access to or use of the information" (local: FED_ecfr-16cfr682.3.txt)
- register ids: US-FEDV6-031, US-FEDV6-032

## RQ-561 fed.flsa.deductions_below_minimum_wage
- result: **documented_limitation**
- answer: 29 CFR 531.35 states the free-and-clear principle: tools or kickbacks that cut into minimum or overtime wages violate the Act. Rules for uniforms, cash shortages, loans and board/lodging were not extracted (the eCFR responses for 531.36 and 531.37 were empty section headers; 531.32 not read).
- source: https://www.ecfr.gov/current/title-29/subtitle-B/chapter-V/subchapter-B/part-531/subpart-C/section-531.35
- quote: "the cost of such tools purchased by the employee cuts into the minimum or overtime wages required to be paid him" (local: FED_ecfr-29cfr531.35.txt)
- register ids: US-FEDV6-033

## RQ-564 fed.bonus.statutory_obligation
- result: **documented_limitation**
- answer: Negative finding, not proven by a single source: no federal statute requiring a bonus or 13th-month pay was found in the FLSA regulation read (29 CFR 778.211 treats only discretionary bonuses as outside the regular rate). State wage-payment timing rules are a per-State fan-out and were not researched.
- source: https://www.ecfr.gov/current/title-29/subtitle-B/chapter-V/subchapter-B/part-778/subpart-C/section-778.211
- quote: "both the fact that payment is to be made and the amount of the payment are determined at the sole discretion of the employer" (local: FED_ecfr-29cfr778.211.txt)
- register ids: US-FEDV6-034

## RQ-569 fed.employment_tax.adjustment_procedure
- result: **closed**
- answer: Over-collected employee FICA and over-withheld income tax: if found before the return is filed, repay or reimburse the employee before filing and keep the employee's written receipt, and do not report the overcollection; for income tax paragraph (b)(1) adds a calendar-year condition. After filing, 31.6413(a)-1(a)(2) and (b)(2) apply, with Form 941-X procedures in its instructions.
- source: https://www.ecfr.gov/current/title-26/chapter-I/subchapter-C/part-31/subpart-F/section-31.6413(a)-1
- quote: "repays or reimburses the amount of the overcollection to the employee before filing the return for such return period" (local: FED_ecfr-26cfr31.6413a-1.txt)
- register ids: US-FEDV6-035, US-FEDV6-036

## RQ-571 fed.ccpa.disposable_earnings.definition
- result: **documented_limitation**
- answer: Definition closed: disposable earnings are earnings after deduction of amounts required by law to be withheld; CCPA cap 25 per centum, or the amount over 30 times the FLSA minimum wage. Whether voluntary deductions such as retirement contributions reduce disposable earnings is not stated in the text read; the statutory wording (only amounts required by law) implies they do not.
- source: https://www.govinfo.gov/link/uscode/15/1672
- quote: "remaining after the deduction from those earnings of any amounts required by law to be withheld" (local: FED_govinfo-15USC1672.txt)
- register ids: US-FEDV6-037, US-FEDV6-038

## RQ-573 fed.equity.nra.sourcing_period
- result: **closed**
- answer: For stock options the time-basis period is generally grant to vesting (the date all employment-related conditions for exercise are satisfied); U.S.-source share = U.S. days over total days in that period (regulation Example 6: 5-year period, 7/10 U.S.). RSUs are not named in (F); treatment by analogy is not stated in the regulation.
- source: https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/section-1.861-4
- quote: "the period between the grant of an option and the date on which all employment-related conditions for its exercise have been satisfied" (local: FED_ecfr-26cfr1.861-4.txt)
- register ids: US-FEDV6-039

## RQ-581 fed.fica.totalization.agreements_in_force
- result: **closed**
- answer: SSA lists 31 totalization agreements in force (Italy 1978 through Romania, entry into force 2026-09-01); the status page gives signing and effective dates with legal citations. Certificate-of-coverage procedure: the overview page's Certificates of Coverage section is collapsed in the browser text and was not captured; coc.html returned 404.
- source: https://www.ssa.gov/international/agreements_overview.html
- quote: "Romania September 1, 2026" (local: FED_ssa-international-agreements.txt)
- register ids: US-FEDV6-040, US-FEDV6-041

## RQ-591 fed.bik.trump_account.employment_tax_treatment
- result: **closed**
- answer: Per the preamble to the section 128 proposed regulations (IRB 2026-37, 2026-09-08): employer contributions excludable from income remain wages for FICA and FUTA; income tax withholding is not required on excludable contributions. G-RULING status: PROPOSED regulation, not final; operates at employer withholding and reporting level.
- source: https://www.irs.gov/irb/2026-37_irb
- quote: "have no corresponding exclusion from the definitions of wages under section 3121 (FICA) and section 3306 (FUTA)" (local: FED_irs-irb-2026-37.txt)
- register ids: US-FEDV6-042

## RQ-593 fed.minister.futa
- result: **closed**
- answer: FUTA excludes service in the employ of a 501(c)(3) religious organization (26 U.S.C. 3306(c)(8)); the exemption cannot be waived. A minister's pay is outside FUTA when the employer is a 501(c)(3) church or organization; if the employer is not 501(c)(3) this exclusion does not apply. Pub. 15-A states no separate minister FUTA rule.
- source: https://www.irs.gov/pub/irs-pdf/p15a.pdf
- quote: "An organization that is exempt from federal income tax under section 501(c)(3) of the Internal Revenue Code is also exempt from FUTA tax." (local: FED_irs-p15a-2026-text.txt)
- register ids: US-FEDV6-017, US-FEDV6-043
