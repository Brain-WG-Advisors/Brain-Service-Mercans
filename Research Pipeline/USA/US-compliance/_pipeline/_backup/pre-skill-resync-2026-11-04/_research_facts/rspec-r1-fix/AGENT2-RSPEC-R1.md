# Agent 2 - RSPEC r1 fix (key -> action -> evidence)

Date: 2026-11-03. Inbound: `_qa/RSPEC-review-r1.json` findings 1-4, 7, 8, 13-15. Scope: only the 37 unverified keys, the 25 consumed_by rows, the 12 + 5 rows without a local copy, RQ-15, the two bracketed values and owner row US-OWN-010. `04-reports-spec/` was not touched.

Backups and pre-change md5: `_research/rspec-r1-fix/_backup/` (`MD5-BEFORE.txt`).

## Files changed (md5 after)

- `00-official-sources/legal-basis-register.csv` de5fc2dd131c151724c38e07af4c738f
- `_research/RSPEC-facts.json` dbd99f8f19a2245074084cc32b69789e
- `_research/SIR-facts.json` 348c5517d1dd4147e32e25d772571fcf
- `_research/DD-8_sheets-facts.json` e4ec05284fa6e9354dcd74885ab9cefc
- `_research/CCG-m01_foundational-facts.json` 4f11ad31102708ab99d83e84999938a1
- `_research/CCG-annex_WA-facts.json` fa064eb874ada5b9e3849eead9ec7d65
- `_research/gaps.json` 1da44aab264aa00018a5957ebdf82090

All five facts files validate against `shared/schemas/facts.schema.json` with 0 errors. The register now has 2,697 rows: 2,694 plus 3 new rows (US-WAS7-001, US-HIS7-001, US-OWN-010).

Mechanical self-check: for every changed key, each number token in the new value was searched in the text of the cited row's local copy (PDF page by page, HTML, XLSX, CSV, JSON). 0 tokens were missing. Each fact carries `_figure_located` (page plus verbatim quote). The same note is appended to the register row's `verification_method`.

## The 37 keys (findings 1-4)

| # | key | action | register_id | evidence (page + quote) |
|---|---|---|---|---|
| 1 | `dd.multi.residence_state` | DD-8_sheets (kept US-MULTIS5-001), value changed | US-MULTIS5-001 | 49 U.S.C. 14503(a): pay is not subject to the income tax laws of a State "other than the State or subdivision thereof of the employee's residence" |
| 2 | `dd.multi.work_state` | DD-8_sheets (kept US-MULTIS5-017), value changed | US-MULTIS5-017 | DOL memo p1: "the Employment and Training Administration's localization of work guidance for reporting wages determines the state ... See Unemployment Insurance Program Letter (UIPL) No. 20-04" |
| 3 | `fed.efw2c.publication` | RSPEC (kept US-FIL-002), value unchanged | US-FIL-002 | SSA EFW2/EFW2C page (Wayback 20261026205542): "EFW2C Publication 42-014 provides the electronic format for submitting annual Form W-2C" |
| 4 | `fed.fica.return_period` | CCG-m01_foundational (kept US-FED-015), value unchanged | US-FED-015 | 26 CFR 31.6011(a)-1(a)(1): "every employer is required to make a return for the first calendar quarter in which the employer pays wages, other than wages for agricultural labor"; Form 943 (agricultural, annual) and Form 944 (annual option) in the same section |
| 5 | `rspec.ak.ui_qtr.channel` | RSPEC (kept US-AKS5-014), value changed | US-AKS5-014 | AK ES Tax CSV guidelines p1 (single and multiple filer): "No column headings or descriptors" |
| 6 | `rspec.az.ui_qtr.form` | RSPEC (kept US-AZB5-005), value changed | US-AZB5-005 | AZ DES Completing the Reports: "quarterly Unemployment Tax and Wage Report (UC-018)"; "Section A ... during the payroll period that includes the twelfth of the month". The 2027 paper UIT-0018F clause was removed (it sits on US-AZB5-006) |
| 7 | `rspec.co.w2_state.format` | RSPEC (kept US-COS5-013), value changed | US-COS5-013 | CDOR XLSX template (cited row). Clause "paper with DR 1093" removed from this key: DR 1093 is quoted in US-COS5-006 p14 "file paper copies of W-2s along with an Annual Transmittal of State W-2 Forms (DR 1093)". The 10-100 employee band is on the CDOR instructions web page, not in the held XLSX, and was removed |
| 8 | `rspec.dc.wh_return.annual` | RSPEC (US-DCS5-014 -> US-DCS5-013), value unchanged | US-DCS5-013 | OTR Withholding Tax Forms page (live 2026-11-02): "File the FR-900A if you are an annual wage filer whose threshold is less than $200 per year. Note: The 2026 FR-900A is due January 31, 2027." |
| 9 | `rspec.de.annual_recon.form` | RSPEC (kept US-DES5-009), value changed | US-DES5-009 | DE WTH-REC instructions (Rev. 02/03/26) p1: "must be filed on or before the last day of January and must be accompanied by a duplicate of each ... (Federal Form W-2)"; "All employers who are required to file W-2s and 1099s electronically for Federal purposes are now required to file those returns electronically for Delaware". The former "paper only for 10 or fewer forms" was removed: not in the source |
| 10 | `rspec.fl.ui_qtr.xml` | RSPEC (US-FLS5-023 -> US-FLS5-022), value changed | US-FLS5-022 | FL RT import specs p5: "Files with greater than 20,000 employee records require upload of an XML file." (the XSD package itself remains on US-FLS5-023) |
| 11 | `rspec.hi.tdi.state_return` | RSPEC (US-HI-003 -> US-HIS7-001), value unchanged | US-HIS7-001 | DLIR DCD About TDI: coverage through an "insured" plan "from an authorized insurance carrier" or an approved "self-insured" plan; also HRS 392-43(c) [US-HIS5-014]: "contributions of the employees ... shall be held in a separate fund or be paid to insurance carriers as premiums" |
| 12 | `rspec.hi.w2_state.format` | RSPEC (US-HIS5-006 -> US-HIS5-005), value changed | US-HIS5-005 | DOTAX withholding page: "Maximum of 1,000 employee records per submission"; "(4) using the Hawaii Bulk Filing System (HBFS)" |
| 13 | `rspec.ia.permit.format` | RSPEC (US-IAS5-018 -> US-IAS5-017), value changed | US-IAS5-017 | IDR File a W-2 or 1099 page: "permits are assigned a 9-digit permit number"; "12-digit numbers were previously assigned to permits issued before November 15, 2021. The Department accepts both" |
| 14 | `rspec.in.w2_state.format` | RSPEC (US-INS5-013 -> US-INS5-011), value changed | US-INS5-011 | IN EFW2 guide p11: "306-307 County Code 2"; "309-319 Local Taxable Wages 11"; "320-330 Local Income Tax Withheld 11"; "331-340* Employer TID 10"; "341-343* Employer TID Location 3" |
| 15 | `rspec.in.wh_return.form` | RSPEC (kept US-INS5-010), value changed | US-INS5-010 | IN DOR withholding page: "Filing Schedule Monthly, early-monthly, or annual"; "you must still file Forms WH-1 and WH-3 for each period even if no tax is due". Thresholds 83.33 / 1,000 and 30 / 20 days moved to unresolved rspec.in.wh_return.thresholds |
| 16 | `rspec.ks.annual_recon.form` | RSPEC (US-KSS5-007 -> US-KSS5-001), value unchanged | US-KSS5-001 | KW-100: "The annual return, W-2s and 1099s are due by January 31 of the following year. Form KW-3 must be filed electronically" |
| 17 | `rspec.la.wh_payment.frequency` | RSPEC (US-LAS5-008 -> US-LAS5-003), value unchanged | US-LAS5-003 | LDR withholding page: "Quarterly Less than $500 Monthly $500 to less than $5,000 Semi-monthly $5,000 or more" |
| 18 | `rspec.mi.annual_recon.form` | RSPEC (US-MIS5-021 -> US-MIS5-018), value changed | US-MIS5-018 | Form 5081 TY2026 p1: "File this return by February 28, 2027. Do not use this form to replace a monthly/quarterly return." |
| 19 | `rspec.mo.local.kansas_city` | RSPEC (kept US-MOP52-007), value unchanged | US-MOP52-007 | KCMO nonresident business tax guide (Wayback 20260609143109): "the employer must withhold the one percent earnings tax on all salaries and wages"; "submit a Registration Application (Form RD-100)" |
| 20 | `rspec.multi.ui_qtr.recipient` | RSPEC (kept US-MULTIS5-017), value changed | US-MULTIS5-017 | DOL memo p1 "localization of work guidance for reporting wages determines the state"; p2 "(1) Is the individual's service localized in this state or some other state?" |
| 21 | `rspec.nd.w2_state.format` | RSPEC (US-NDS5-003 -> US-NDS5-002), value changed | US-NDS5-002 | ND guideline p13: "Form W-2 files must be formatted according to the specifications in SSA Publication 42-007 (EFW2). Forms W-2c files must be formatted according to the specifications in SSA Publication 42-014 (EFW2C)" |
| 22 | `rspec.nh.wh_return.applicable` | RSPEC (kept US-NH-006), value unchanged | US-NH-006 | NH DRA "Taxes at a Glance" list (16 tax types, Business Enterprise Tax ... Utility Property & Railroad Taxes): no wage income tax and no withholding tax listed (absence evidence) |
| 23 | `rspec.ny.nys45.efile` | RSPEC (US-FIL-007 -> US-NYS5-010), value unchanged | US-NYS5-010 | NYS-50 page: "All quarterly combined withholding, wage reporting, and UI returns must be electronically filed, and any balance due with the return must be paid via ACH debit"; "a $50 penalty for each tax document not electronically filed"; "see Publication 72.5, Electronic Reporting of Form NYS-45 Information" |
| 24 | `rspec.oh.municipal.rate_table` | RSPEC (kept US-OHB5-002), value unchanged | US-OHB5-002 | inspected directly: OHMuniRateTable.csv (no header row; columns begin, end, FIPS, name, rate) has 1,083 rows; rows with begin <= 20261101 <= end = 678, 678 distinct FIPS (counted by script 2026-11-03) |
| 25 | `rspec.ok.wh_remit.schedule` | RSPEC (US-OKS5-014 -> US-OK-001), value changed | US-OK-001 | OW-2 2026 p3: "except where the amount withheld is more than $500.00 per quarter ... monthly basis on or before the 20th"; "$5,000.00 or more per month in the previous fiscal year, every employer must remit the tax withheld electronically"; "$10,000.00 or more ... same dates as required under the federal semi-weekly deposit" |
| 26 | `rspec.pa.annual_recon.form` | RSPEC (US-PAS5-010 -> US-PAS5-009), value changed | US-PAS5-009 | PA DOR employer withholding page: "Employers filing 10 or more income statements must file electronically through myPATH. Employers filing less than 10 income statements can remit electronically through myPATH or mail" |
| 27 | `rspec.ri.wh_deposit.schedule` | RSPEC (US-RIS5-018 -> US-RIS5-019), value changed | US-RIS5-019 | 2026 RI booklet p5: "WEEKLY - If the employer withholds $600 or more for a calendar month from employees' wages, the employer must remit such withheld taxes on a weekly basis ... next banking day"; p6 "MONTHLY - If the employer withholds $50 or more but less than $600 ... if the employer withholds $200 or more but less than $600 ... via electronic means"; p7 "QUARTERLY - If the employer withholds less than $50 for any calendar month". Form name RI-941M dropped from this key |
| 28 | `rspec.sc.w2_state.format` | RSPEC (kept US-SCS5-016), value changed | US-SCS5-016 | SCDOR W-2 upload page: "SSA Publication No. 42-007"; "SCDOR state record format ... (RS-1)"; "employers that have up to 30 employees"; "Full SSN". FIPS state code 45 removed (not on the page) |
| 29 | `rspec.sc.wh_payment.efile` | RSPEC (US-SCS5-018 -> US-SCP51-003), value changed | US-SCP51-003 | WH-105: "If your South Carolina Withholding Tax is $15,000 or more, or you make 24 or more payments in a year, you are required to file and pay electronically." Paper form number WH-1601 removed (not in this source) |
| 30 | `rspec.sd.wh_return.applicable` | RSPEC (US-SDS5-013 -> US-SD-001), value unchanged | US-SD-001 | SD DOR individual taxes page: "South Dakota is one of seven states that does not impose a state income tax." (no State income tax, hence no State withholding return) |
| 31 | `rspec.tn.ui_qtr.channel` | RSPEC (kept US-TNS5-005), value changed | US-TNS5-005 | TN DLWD article 41492672876947: "(Manual Entry, Abbreviated ICESA, or 58-Character Text File)"; "In e-Services go to the Summary tab". Start date 2025-05-27 and "full ICESA" removed (not in the local copy) |
| 32 | `rspec.tn.wh_return.applicable` | RSPEC (US-TNS5-005 -> US-TNP51-001), value unchanged | US-TNP51-001 | GEN-34: "Tennessee has no state income tax on earned income and therefore has no withholding requirements." |
| 33 | `rspec.va.annual_recon.form` | RSPEC (US-VAS5-009 -> US-VAS5-013), value changed | US-VAS5-013 | VA employer guide p5: "Form VA-6 ... along with required wage statements (Forms W-2 and 1099) is January 31. If a business closes, these forms must be filed within 30 days after the last month in which wages were paid." |
| 34 | `rspec.wa.local.seattle.base_thresholds_due` | RSPEC (kept US-WAS6-001), value changed | US-WAS6-001 | OCF page: "2026 $9,074,409 or more in 2025 $194,452 or more in 2026"; "Q4 2026 Payroll Expense Tax Packet - for Q4-2026, due Jan. 31, 2027". Social Housing Tax clause removed from this key: carried by rspec.wa.local.seattle.sht.* on US-WAS6-002 |
| 35 | `rspec.wa.wh_return.applicable` | RSPEC (US-WAS5-013 -> US-WAS5-017), value unchanged | US-WAS5-017 | WA DOR income tax page: "Washington does not currently have an individual income tax." (the tax from 2028-01-01 is assessment-level, not withholding) |
| 36 | `sir.mo.new_hire.days` | RSPEC (US-MOS5-008 -> US-MOS5-001), value unchanged; SIR (US-MOS5-008 -> US-MOS5-001), value unchanged | US-MOS5-001 | pdfs/MO/4282_2026_wayback-20260808194643.pdf p6 "Within 20 days of hiring a new employee, please mail a copy of the completed Form MO W-4"; p15 "Notice to Employer: Within 20 days of hiring a new employee, a copy of the Employee's Withholding Certificate (Form MO W-4) must be submitted" |
| 37 | `wa.wc.employee_deduction.rule` | CCG-annex_WA (US-WAS5-019 -> US-WAS7-001), value changed | US-WAS7-001 | RCW 51.16.140(1): "shall deduct from the pay of each of his or her workers one-half of the amount he or she is required to pay, for medical benefits within each risk classification". Stay-at-Work and Supplemental Pension worker shares moved to unresolved wa.wc.employee_deduction.saw_supplemental_pension |

The value changes remove only clauses that the cited source does not carry, and each removal is named in the evidence column. Numbers that could not be proven were moved to `unresolved[]` (non-blocking), so the builder removes them:

- `rspec.in.wh_return.thresholds` (RSPEC-facts): IN WH-1 thresholds 83.33 / 1,000 and 30 / 20 days. Closes with IC 6-3-4-8.1 or the IN DOR withholding FAQ.
- `wa.wc.employee_deduction.saw_supplemental_pension` (CCG-annex_WA-facts): worker share of the Stay-at-Work and Supplemental Pension premiums. Closes with RCW 51.32.073 plus the L&I Stay-at-Work rule or notice. The proven part, one-half of medical aid (RCW 51.16.140), stays on the key.

Clauses removed because the cited copy does not carry them. The builder must drop them from the cells, or cite the named row in prose:
- CO: "paper with DR 1093" (it is in US-COS5-006 p14) and the "10-100 employees" band (on the CDOR web page, not in the held XLSX).
- AZ: "2027 paper UIT-0018F" (it is on US-AZB5-006).
- DE: "paper only for 10 or fewer forms". It is in no source, and the federal threshold is 10 or more returns.
- FL: the XSD package detail (still on US-FLS5-023).
- IN: the W-2 xml/IRIS channels (still on US-INS5-013).
- MI: "every filer files".
- ND: the TAP/web-service channels and "mandatory since 2022".
- PA: the due date and EFW2/CSV (on US-PAS5-010).
- RI: the form name RI-941M.
- SC: FIPS state code 45, "filing with SSA does not satisfy SC" and the paper form WH-1601.
- TN: the start date 2025-05-27 and "full ICESA".
- VA: "filed separately from W-2 upload".
- Seattle: the SHT clause (carried by `rspec.wa.local.seattle.sht.*` on US-WAS6-002).

Propagation:
- `sir.mo.new_hire.days` is re-pointed in SIR-facts too.
- `dd.multi.*` changed in DD-8_sheets.
- `fed.fica.return_period` in CCG m01: only its row gained a local copy.
- `wa.wc.employee_deduction.rule` in CCG annex_WA: the value is narrowed.
- CCG/annex_WA and DD/8_sheets need a re-sync when those stages next run. The `consumed_by` of each new target row now lists the consuming unit.

## Findings 3 and 8: local copies saved (md5 in the register verification_method)

- US-FIL-002: `SSA_EFW2-EFW2C-page_wb_2026-11-03.html`
- US-FED-015: `eCFR_26CFR31.6011a-1_api_2026-11-03.xml`
- US-NH-006: `DRA-taxes-at-a-glance-and-BET_2026-11-01.txt`
- US-MOP52-007: `KCMO_tax-guide-nonresident-businesses_wb-20260609_2026-11-03.html`
- US-FIL-007: `NY_DTF-Pub72.5_2026-11-03.pdf`
- US-FED-014: `USC_26-3302_govinfo-2024ed_2026-11-03.html`
- US-FED-008: `IRS_RevProc-2012-32_2026-11-03.pdf`
- US-NY-003: `NY_DTF-MTA-305-I_2026-11-03.html`
- US-AKWT-001: `AK_DOR-withholding-tax-page_2026-11-03.html`
- US-FIL-006: `CA_EDD-DE8300_2026-11-03.pdf`
- US-FL-001: `FL_Constitution-ArtVII_2026-11-03.html`
- US-COP51-006: `CO_CDOR-withholding-forms_wb_2026-11-03.html`
- US-WAP51-001: `WA_Seattle-OCF-payroll-expense-tax_2026-11-03.html`
- US-WAPFML-001: `WA_PaidLeave-employer-roles_2026-11-03.html`
- US-WVUI-001: `WV_WorkForce-tax-filing-reporting_2026-11-03.html`
- US-FIL-008: `PA_DLI-UC-2010_2026-11-03.pdf`
- US-FIL-012: `OH_ODT-BulkFilingImplementationGuide_02242026_2026-11-03.pdf`
- US-SD-001: `SD_DOR-individual-taxes_2026-11-03.html`
- US-TNP51-001: `TN_DOR-GEN-34_2026-11-03.json`

US-FIL-007 (Pub. 72.5) does not contain "e-file and ACH mandatory" or "50 USD per paper document". `rspec.ny.nys45.efile` is therefore re-pointed to US-NYS5-010 (the NYS-50 page), which carries all three parts: the mandate with ACH debit, "a $50 penalty for each tax document not electronically filed", and the Pub. 72.5 reference.
- Seattle: US-WAP51-001 now holds the same OCF page as US-WAS6-001.
- MTA-305: US-NY-003 now has its own local copy of MTA-305-I, so no re-point was needed.
- NH: US-NH-006 now points to the DRA Taxes-at-a-Glance capture already held under US-NHP9W-003, because the direct fetch returns 403.

## Finding 7: consumed_by

`RSPEC` was appended to the 25 rows listed in the review (US-COB5-403 ... US-WVR3-001).

## Findings 13-15

- 13: `RSPEC-RQ-15` added to `gaps.json` -> `RSPEC.gaps` (minor, non-blocking). It closes with the Pub. 42-007 RO/RU tables, checked against US-FEDS5-032.
- 14: `rspec.fed.form1042s.wage_codes` now reads "(also 19 teaching, 20 studying/training, 42/43 artist/athlete)". `rspec.wv.local.service_fee_returns` uses "(register US-...)" instead of "[US-...]". Neither value contains a square bracket.
- 15: owner row **US-OWN-010** added (consumed_by RSPEC;SCOPE). Reason: there is no single national norm, validator or plugin for US payroll filings. Some State specifications are held (FL RT XML XSD, US-FLS5-023; MI MiUI) but cover only their own State and are not wired as a validator. Owner default (asked, no objection), reversible, decided 2026-11-03. **Not done (outside agent 2's write scope):** the C35 `reason` text in `_pipeline/build-manifest.json` still needs the same narrowing. That edit belongs to the scaffolder.

## Remaining for the builder

- Rebuild with the new values and register_ids.
- Remove the numbers now in `unresolved[]` and drop the clauses listed above.
- Then do findings 5, 6 and 9-12 (routed to the builder).

By the self-check above, 0 of the 37 keys remain unverified. The fresh auditor confirms this in r2.
