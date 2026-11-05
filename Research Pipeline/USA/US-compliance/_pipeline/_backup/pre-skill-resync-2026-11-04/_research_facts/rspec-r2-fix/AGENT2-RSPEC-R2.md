# Agent 2 - RSPEC r2 fix (key -> action -> evidence)

Date: 2026-11-03. Inbound: `_qa/RSPEC-review-r2.json` blockers 1 and 2 (the C30 findings routed to agent 2), plus the orchestrator's US-OWN-010 alignment. Scope was limited to those keys. `04-reports-spec/` was not touched, and nothing was written under `~/mercans-pipeline`.

Backups and pre-change md5 are in `_research/rspec-r2-fix/_backup/` (`MD5-BEFORE.txt`).

## Files changed (md5 after)
- `00-official-sources/legal-basis-register.csv` e7ca111aa32e29e4b33c7bcb379898bb: 2,700 rows. The 3 new rows are US-DCS5-026, US-DCS5-027 and US-OKS5-030. Edited rows: US-FED-028, which now has a local copy, the 21 target rows below and US-OWN-010.
- `_research/RSPEC-facts.json` 2e59c83c822a0cf850b4fdad0f23654e: 17 keys changed and 3 `unresolved[]` entries added.
- `_research/DD-8_sheets-facts.json` 575530df1fc6ddae44da046cb67e157f: 1 key changed (`dd.employer.state_account_ids`).
- `_research/CCG-annex_FED-facts.json` 51b8bf60fef918d84629c2df883d6444: 1 key changed (`fed.reporting_agent.authorization`).
- New local copies, each in exactly one folder:
  - `00-official-sources/spec-sources/DC/DC_DOES_reporting-questions_2026-11-03.html` (md5 6d65033a949ac7c8eef9c94f6c471d18)
  - `00-official-sources/spec-sources/DC/DC_DOES_UI-tax-division-forms_2026-11-03.html` (md5 bd05534776db91d598aaf33fa3da2793)
  - `00-official-sources/spec-sources/OK/OK_OESC_EZTaxExpress_UserGuide_Full_2026-11-03.pdf` (md5 8a2b3a48d7aa950e32dbf2ea9de07fd5, 7,008,066 bytes). It is over 5 MB and was kept because it is the only official OESC copy that names OES-3 together with EZ Tax Express. The justification is in the row.
  - `00-official-sources/spec-sources/FED/FED_IRS-f8655-rev2024-01_2026-11-03.pdf` (md5 ae69c6d9c6017bf7b1d4edb4cd67a004)

All three facts files validate against `shared/schemas/facts.schema.json` with 0 errors.

How the second source is recorded: a fact has one schema `register_id`. Where a value needs a second row, the fact carries `_also_register_ids`; the schema allows `^_` keys. This is the review's "add that row as a second register_id" option. The builder should render both citations.

Every key carries `_figure_located` with one entry per text element of the value: element, row, file, page and the verbatim snippet. Each target row carries the matching quote in `verification_method`, with `verified_on` set to 2026-11-03. Every target row now lists `RSPEC` in `consumed_by`, and the DD account-id rows also list `DD/8_sheets`. US-UTB5-002 was empty before.

## The 19 keys
| key | register_id (+ _also) | value change | evidence |
|---|---|---|---|
| rspec.ut.wh_return.form | US-UTB5-002 (+US-UTS5-013) | unchanged | UTB5-002: "Employers use form TC-941E for their quarterly returns"; "All returns must be filed electronically". R865-9I: $1,000/month; Schedule H / Form 944 annual |
| rspec.ut.w2_state.content | US-UTR3-001 (+US-UTS5-013) | unchanged | Pub. 14: "the 14-digit number ending in WTH". R865-9I: the word "Utah"; SSN |
| dd.employer.state_account_ids | US-UTR3-001 (+US-KSS5-026, US-MDS5-016, US-IAS5-017) | rewritten: KS `036#######F##` replaces "036-...-01"; MD stated as "Central Registration Number in RS positions 338-345" | K-2MT p3 "(036#######F##)"; MD p8 "CRN in positions 338-345"; IA "9-digit permit number" |
| rspec.co.w2_state.format | US-COS5-006 (+US-COS5-013) | rewritten to the guide's manual-file / .txt upload route; "uploaded in Revenue Online" for the XLSX template was removed because that page is not held | Guide p14 "upload an electronic file in a .txt format" |
| rspec.al.annual_recon.form | US-ALS5-001 | unchanged | Booklet p2 "On or before the last day of January each year ... must file Form A-3" |
| rspec.az.annual_recon.form | US-AZP52-005 (+US-AZS5-025, US-AZS5-022) | rewritten, see finding 2 | below |
| rspec.hi.wh_deposit.schedule | US-HIS5-004 (+US-HIS5-005) | unchanged | Booklet A p4 "Remit taxes quarterly with Form VP-1"; thresholds re-confirmed on the 2026 page |
| rspec.hi.w2_state.due | US-HIS5-005 | unchanged; note added | "no later than January 31st". The same page's FAQ also says "by February 28 using Form HW-3", now recorded in the note |
| rspec.ks.w2_state.format | US-KSS5-026 (+US-KSS5-001) | "no CF/SF" removed (an inference, not text); the record list is now the K-2MT list | K-2MT "RA, RE, RW, RO (optional), RS, RT, RU (optional), RV (optional) and RF"; KW-100 "formatted as outlined in the KW-2CSV" |
| rspec.ks.wh_deposit.report | US-KSS5-001 (+US-KSS5-007) | unchanged | KW-100 "file a KW-5 ... for EACH reporting period even when no Kansas tax was withheld" |
| rspec.ms.ui_qtr.form | US-MSS5-012 (+US-MSS5-014) | "zero report required" removed (in no held copy) and moved to unresolved | MSS5-014 "Detail Wage information (Form UI-3) ... submitted separately" |
| rspec.nc.ui_qtr.form | US-NCS5-025 | rewritten without "NCUI 101", which is in no official copy obtainable today; added to unresolved | "Sign in to your NCSUITS account to file the report online"; "ten or more employee wage items"; "Zero report" |
| rspec.oh.school_district.returns | US-OHB5-401 (+US-FIL-012) | "WT 8655" changed to "WT-8655" | "Ohio form WT-8655 is a reporting agent authorization"; SD 141 "by January 31st"; FSET 4.4 in FIL-012 |
| rspec.ok.ui_qtr.form | US-OKS5-020 (+US-OKS5-030 new) | wording | Guide "3.1.3 Print Copy of OES-3"; EZ Tax Express; OES-047 "required each quarter on all active tax accounts"; "zero wage" |
| rspec.pa.local.eit_lst | US-PAS5-018 (+US-PAS5-017) | rewritten to the DCED wording (Feb 28 becomes "last day of February"; "to the collector" removed) | "due within 30 days after the end of each calendar quarter"; "W2-R ... On or before the last day of February" |
| rspec.wv.wh_return.form | US-WVS5-014 (+US-WVS5-010) | unchanged | TSD-381 "will file the WV/IT-101A annual return" |
| rspec.in.wh_return.format | US-INS5-010 | wording (the 10 MB split is quoted) | "IDORWTH2016V1.0"; "under 10 MB, manually enter or upload via INTIME"; "exceeds 10 MB ... SFTP" |
| rspec.dc.ui_qtr.form | US-DCS5-026 new (+US-DCS5-027 new, US-DCS5-018) | "via DOES ESSP" removed and moved to unresolved; "UC-30-H" changed to "UC30-H" | DOES "Form UC-30 each quarter ... due on April 30, July 31, October 31 and January 31"; forms page "Form UC30-H"; D.C. Code 51-104 April 15 |
| fed.reporting_agent.authorization | US-FED-008 (+US-FED-028, local copy now saved) | unchanged | f8655 p1 "(Rev. January 2024)"; lines 15/16; "does not relieve me, as the taxpayer" |

## Finding 2 (AZ): the source does not support the expected wording
The ADOR page (US-AZP52-005, local copy `pdfs/AZ/employer-withholding-filing-obligations_wayback.html`) states the 30-day extension for both forms:
- "Employers may apply for a 30-day extension of time to file Arizona Form A1-APR. Employers must show good cause ..."
- In the A1-R section: "Employers may apply for a 30-day extension of time to file Arizona Form A1-R. Employers must show good cause when requesting an extension."

A.R.S. 43-412 (US-AZS5-022) says only "The department may extend the filing deadline on a showing of good cause by the employer", with no day count. Pub. 701 (US-AZS5-025) carries A1-R and the W-2s.

The new value cites both and does not restrict the 30 days to A1-APR: "A1-R with W-2s, due Jan 31; the department may extend the deadline on a showing of good cause (A.R.S. 43-412); ADOR: 30-day extension on a good-cause request, stated for A1-APR and for A1-R". The auditor should re-read the A1-R section of the held copy.

## US-OWN-010
`figure_or_rule_carried` now carries the corrected reason from build-manifest `validation_exemptions`, word for word (AccuWage Online inside an authenticated BSO session, Pub. 42-007 §6.0; State-specific validators FL RT XSD and MI MiUI; revisit condition). It keeps "Owner default, asked, no objection, reversible; owner re-informed 2026-11-03". `verified_on` is 2026-11-03.

## Unresolved (added to RSPEC-facts `unresolved[]`)
- `rspec.nc.ui_qtr.form_number`: NCUI 101.
  - Tried: des.nc.gov `documents/downloads/ncui101-0/download` (404); `documents/files/employers-quarterly-tax-and-wage-report-english/open` (404); `about/forms-and-documents`, which names only NCUI 101A; the archive.org API (429).
  - Would close it: the blank NCUI 101 PDF from NC DES.
- `rspec.dc.ui_qtr.channel`: ESSP as the UC-30 channel.
  - Would close it: the DOES UI Employer Handbook (attachment on the forms page) or the ESSP help page.
- `rspec.ms.ui_qtr.zero_report`.
  - Would close it: an MDES page or regulation stating that a report is due when no wages were paid.

## Self-check over all RSPEC-bound facts (task 3)
Script: `selfcheck/selfcheck.py`, which builds a text cache with `selfcheck/textcache.py` (PDF via pdftotext, gzip-aware, HTML stripped, XLSX cells).

What it checks: for every fact in `_research/*-facts.json` bound in `_pipeline/RSPEC-bindings.csv`, each text element of the value must be found in the local copy of `register_id` plus `_also_register_ids`. Elements are dates (Mon D, ISO, "last day of"), quarter tokens, form ids (with OCR I/l->1, O->0), numbers, channel words and acronyms (literal or expanded by initials).

Result:
- The 19 keys: 91 elements, **0 misses**.
- Whole RSPEC-bound set: 2,691 elements over 536 keys. 151 elements across 81 other keys are still unmatched (`selfcheck/selfcheck-misses.json`). They were not adjudicated or fixed in this pass because they are outside the key-limited scope and over budget.
- Most look like matcher limits, not clause failures. Examples:
  - label acronyms the source never spells out (FUTA, PFML, FIT, ICHRA);
  - EFW2 positions printed across table columns (RW 188-198);
  - rates printed in an image table (OR-DOR 211-155-2 p2 has no text layer);
  - "20 days" rules phrased differently.
- Some deserve a human read, for example:
  - `rspec.tx.ui_qtr.due` (the four dates are not in the held 40 TAC 815.109 text);
  - `rspec.la.wh_return.form` (dates);
  - `rspec.wv.local.charleston.service_fee_return` (dates and paper);
  - `rspec.or.local.portland_metro_multnomah` (Jan 31, EFW2).
- The residual is independent per State and can be split across workers.

### Residual list (key [rows]: unmatched elements)
- fed.futa.rate.net [US-FED-007]: numv:0.6
- nv.mbt.base [US-NVS5-011]: word:ESD
- or.stt.employee.rate [US-ORS5-011]: numv:0.1
- or.transit.trimet.employer.rate [US-ORS5-010]: numv:0.8237
- or.transit.lane.employer.rate [US-ORS5-010]: numv:0.8
- pa.pit.local.pittsburgh.payroll_expense.rate [US-PAB5-401]: numv:0.55
- dd.fed.aca.fte_tracking [US-FEDS5-012]: word:FTE
- dd.multi.sui_state [US-MULTIS5-024]: word:PFML
- dd.oh.school_district_code [US-OHS5-019]: form:W-2; form:SD 101; num:141
- dd.pa.psd_code [US-PAS5-017]: word:PSD
- dd.fl.everify_certified [US-FLS5-010]: form:RT-6
- dd.oh.municipality_work [US-OHP52-003]: word:CCA; word:RITA
- dd.oh.municipal_rate_table [US-OHB5-002]: num:5; word:FIPS
- dd.fed.nra.visa_class [US-FEDR2-001]: form:F-1; form:J-1; form:M-1; form:Q-1; form:Q-2; form:H-1B; form:L-1; word:CPT; word:OPT; word:FUTA
- rspec.multi.pfml.state_key [US-MULTIS5-024]: word:PFML
- rspec.ak.ui_qtr.online_mandate [US-AKS5-005]: form:1M
- az.newhire.report_days [US-AZS5-012]: numv:20
- rspec.co.w2_state.due [US-COS5-006]: word:CDOR
- rspec.ct.ui_qtr.layout [US-CTS5-032]: form:EAN 147-156; num:30; num:42; num:45; num:51; num:146
- rspec.ct.ui_qtr.new_optional_fields [US-CTS5-018]: qtr:3; word:ZIP
- rspec.ct.pfml_qtr.channel [US-CTS5-022]: chan:xml; chan:csv
- rspec.fl.ui_qtr.everify_block [US-FLS5-010]: form:RT-6
- rspec.ga.wh_return.form [US-GAS5-002]: qtr:3
- rspec.ia.w2_state.due [US-IAS5-017]: chan:paper
- rspec.id.registration.form [US-IDS5-021]: word:IDOL
- rspec.il.wh_return.form [US-ILS5-012]: num:04; num:07; num:02
- rspec.il.ui_monthly.rule [US-ILS5-017]: num:1; num:2
- rspec.in.annual_recon.form [US-INS5-011]: date:february/28
- rspec.ks.ui_qtr.format [US-KSS5-022]: chan:paper
- rspec.ky.local.louisville [US-KYP9W-002]: word:OLT
- rspec.la.wh_return.form [US-LAS5-003]: date:april/30; date:july/31; date:october/31
- rspec.la.annual_recon.form [US-LAS5-003]: form:W-2
- rspec.la.ui_qtr.due [US-LAS5-007]: word:LAWATS
- la.newhire.report_days [US-LAS5-010]: numv:20
- rspec.me.ui_qtr.form [US-MES5-021]: word:MRS
- rspec.mn.w2_state.due [US-MNS5-010]: word:DOR
- rspec.mn.pfml_qtr.form [US-MNS5-018]: word:DEED
- rspec.ms.ui_qtr.format [US-MSS5-013]: form:EFW2
- rspec.mt.w2_state.format [US-MTS5-005]: word:PDF
- ne.newhire.report_days [US-NES5-014]: numv:20
- rspec.nm.ui_qtr.formats [US-NMS5-008]: chan:electronic
- rspec.ny.nys1.deposit [US-NYS5-010]: word:QTD
- rspec.oh.w2_state.school_district_code [US-OHS5-018]: form:W-2
- oh.newhire.report_days [US-OHS5-014]: numv:20
- rspec.ok.ui_qtr.format [US-OKS5-020]: word:TPA
- rspec.or.oq.due [US-ORS5-010]: num:04; num:02
- rspec.or.local.portland_metro_multnomah [US-ORS5-024]: date:january/31; form:W-2; form:EFW2
- rspec.ri.w2_state.format [US-RIS5-019]: form:EFW2; chan:txt; word:ASCII
- rspec.ri.ui_qtr.form [US-RIS5-017]: word:JDA
- rspec.sc.wh_return.form [US-SCS5-002]: qtr:1; qtr:3
- rspec.sd.ui_qtr.layout [US-SDS5-014]: chan:ssn
- rspec.va.wh_return.form [US-VAS5-013]: num:999
- rspec.wi.w2_state.format [US-WIS5-012]: chan:upload; chan:sftp
- rspec.nm.w2_state.due [US-NMP52-005]: chan:txt
- rspec.oh.municipal.frequency [US-OHP52-003]: num:2,399; num:200
- rspec.oh.municipal.rate_table [US-OHB5-002]: iso:2026/november/1; num:678; word:FIPS
- rspec.oh.school_district.list [US-OHB5-001]: form:SD 101; form:SD 141; form:W-2
- rspec.wa.ui_qtr.penalties [US-WAB5-004]: word:ESD
- rspec.fed.efw2.rs.layout [US-FEDS5-032]: word:SQUI
- rspec.nc.w2_state.ty2026_rs_layout [US-NCS6-001]: word:ZIP
- rspec.tx.ui_qtr.due [US-TXS6-002]: date:april/30; date:july/31; date:october/31; date:january/31; num:1; num:3
- rspec.fed.form941.line_map [US-FEDS6-001]: date:september/12; word:FIT
- rspec.fed.form944.line_map [US-FEDS6-003]: word:FIT
- rspec.fed.form944.due [US-FEDS6-003]: iso:2027/february/10
- rspec.fed.efw2.rw.layout [US-FEDS5-032]: word:NQDC
- rspec.fed.w2.box_map [US-FEDS5-007]: form:RW 188-198; form:RW 199-209; form:RW 221-231; form:RW 232-242; form:RW 243-253; form:RW 254-264; form:RO 12-22; form:RW 276-286; form:RW 353-363; form:RW 486; form:RW 490; num:375; num:385; num:488; num:489; num:492; num:493; num:495
- rspec.fed.w2.box14b.ttoc_codes [US-FEDS6-011]: num:000
- rspec.fed.w2.box14b.ttoc_count [US-FEDS6-011]: numv:71
- rspec.fed.form943.due [US-FEDS6-004]: iso:2027/february/10
- rspec.fed.form1042s.wage_codes [US-FEDS6-005]: word:NRA
- rspec.fed.aca.form1095c.line14_codes [US-FEDS6-006]: word:FPL; word:ICHRA
- rspec.fed.aca.form1095c.line17_rule [US-FEDS6-006]: word:ICHRA
- rspec.fed.aca.ty2026_due [US-FEDS6-006]: iso:2027/march/1
- rspec.fed.form940.line_map [US-FEDS6-008]: word:SUTA
- rspec.wv.local.charleston.service_fee_return [US-WVS6-001]: date:april/30; date:july/31; date:october/31; chan:paper
- rspec.wv.local.morgantown.service_fee_return [US-WVS6-002]: num:7
- rspec.wv.local.service_fee_returns [US-WVS6-001]: form:WVS6-001; form:WVS6-002; form:WVP52-005
- rspec.pa.local.pittsburgh_payroll_expense.return [US-PAS6-001]: chan:paper; word:USPS
- rspec.wa.local.seattle.sht.due [US-WAS6-002]: date:april/30; date:july/31; date:october/31; word:PET
- fed.futa.credit_reduction.ca.potential.rate [US-FEDS5-009]: numv:5.3
- fed.futa.credit_reduction.vi.potential.rate [US-FEDS5-009]: numv:4.8