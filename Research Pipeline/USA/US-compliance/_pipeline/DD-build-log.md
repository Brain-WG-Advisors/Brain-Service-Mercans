# DD - build log
Artifact: DD | Country: US | Round: 1 | Built: 2026-11-03
Manifest: _pipeline/build-manifest.json (USD, currency_minor_units 2, rounding payment 0.01, tier T4, package 1.0, year 2026)
Pack: _research/DD-research-pack.md | Facts: _research/DD-8_sheets-facts.json (108 facts, 5 unresolved[] + 1 precheck entry)
Generator: 05-data-dictionary/_build/build_dd.py (dd_common.py, dd_defs.py, dd_rules.py, dd_recon.py); deliverable 05-data-dictionary/US-DD-001-v1.0.xlsx
Contract of the generator: re-runnable, the only source of the workbook (C71 PASS: rebuilt workbook identical cell by cell). Scratch: 05-data-dictionary/_build/_scratch/.

## Precedent inspection (L1)
CZ_Data_Dictionary_V2_0.xlsx opened with openpyxl and inspect_workbook.py. 8 sheets in order: Version Control, Introduction, Instructions, ID Information, Country Fields, Country Option Mappers, Currency Codes - ISO 4217, Country Codes - ISO 3166-1.
- ID Information: header row 4, 22 columns A-V, data from row 5, freeze E1; blue (4472C4) A, C, E-K, V; orange (FF9900) B, D, L-U. A second block "Country-Specific Legal Entity Fields" starts at row 12 with the header repeated at row 13 (template quirk: not data).
- Country Fields: header row 4, col A empty spacer, labels B-W (23), blue B, D, F-L, W, orange C, E, M-V. Header repeated at row 42 in the template.
- Country Option Mappers: header row 4, columns B-F; the header repeats at the start of each block (9 repeats in the template, none counted as data).
- Excel table objects in the template: Table_1 (Instructions), Table_2 (ID Information A13:V17), Table_3 (Country Fields B42:X292), Table_4-11 (option mapper blocks), Table_12-13 (ISO sheets). Review comments of the precedent country (threaded, 6) sit on its data cells.
NOTE: the monolith and the April-2026 team guide say 24 columns A-X; the template file says 22 (A-V). Built to the file.
NOTE: team-guide text says populate "blue" only; the template's own precedent rows populate orange cells too. Built to the contract: orange columns (Ordinal, Internal Code, Validations, parent / sub-group block, Default Value, MSS / ESS permissions) are empty on every row (dd_lint C12 checks this).

## Deviations from the template (all deliberate, all in the generator)
| Item | What was done | Why |
|---|---|---|
| Excel tables Table_2, Table_3, Table_4-11 | removed (autofilter on ID Information A4:V14); Table_1, Table_12, Table_13 kept | stale table ranges over rewritten content made Excel refuse the file (open_check FAILED); plain ranges with the template's cell fills open clean (open_check OK) |
| Review comments on data cells (ID Information, Country Fields, Version Control A1) | removed; Version Control guidance comments B12:E12 kept | precedent-country content must not survive (C42); the comments are history (C47) |
| Introduction B11:B16 | numbering formulas replaced by their values 1-6 | no cached values after a save without Excel; same result |
| Version Control status list (E13:E23) | "Issued" added to the list | the one Version Control row carries package version, issue date and status "Issued" |
| Version Control title | B9 = "United States of America | US-DD-001 v1.0" | package version on the title block (C43) |
| Instructions, ISO 4217, ISO 3166-1 | unchanged (compared cell by cell with the template) | contract: change the country name only / preserve as-is; the Instructions sheet carries no country name |
| Mid-sheet repeated header | kept once in ID Information (entity block, as the template) and once per option mapper block; none in Country Fields | template structure; counted out of the data rows |
| Version Control date | 2027-03-31 is the manifest planning placeholder (package.issue_date; owner has not set a date) | taken from the manifest, not invented |

## Result
- Elements: 144 data fields: ID Information 7 (1 employee block, 6 legal entity block), Country Fields 137.
- Option mappers: 34 mappers, 275 rows (US State or District (USPS code) 51; Treasury Tipped Occupation Code 72; State withholding certificate 41; the rest are small lists; 10 external code lists are pointer rows, see RQ-02 and RQ-03).
- [[FACT]] tags: 205 in the workbook, 126 distinct keys (108 of the 108 DD facts bound; 17 borrowed keys from approved CCG / RSPEC / SIR facts, listed below). Bindings: _pipeline/DD-bindings.csv (203 rows: location, key, register_id, effective_from).
- Marker cells (in-place research gaps): 13 cells, ids DD-RQ-01 to DD-RQ-04; documented limitations use the neutral wording "not named in the cited sources".

## Fact bindings (section -> key -> register_id), sample; full table in _pipeline/DD-bindings.csv
| Location | Claim | key | register_id |
|---|---|---|---|
| Country Fields / Alaska geographic code / Additional Notes | tagged value of the key | `dd.ak.ui.geographic_code` | US-AKS5-014 |
| Country Option Mappers / Alaska geographic code (authority list) | tagged value of the key | `dd.ak.ui.geographic_code` | US-AKS5-014 |
| Country Fields / Alaska occupational code / Additional Notes | tagged value of the key | `dd.ak.ui.occupation_code` | US-AKS5-014 |
| Country Option Mappers / Alaska occupational code (authority list) | tagged value of the key | `dd.ak.ui.occupation_code` | US-AKS5-014 |
| Country Fields / Denver occupational privilege tax work location / Additional Notes | tagged value of the key | `dd.co.denver_opt` | US-COP52-001 |
| Country Fields / Employee primary language / Additional Notes | tagged value of the key | `dd.co.workforce_first_language_5pct` | US-COL-001 |
| ID Information / State employer account numbers / Additional Notes | tagged value of the key | `dd.ct.pfml.employee_level_data` | US-CTB5-001 |
| Country Fields / Hours worked (time-data input) / Additional Notes | tagged value of the key | `dd.ct.ui.occupation_hours_zip` | US-CTS5-018 |
| Country Fields / Occupation / Additional Notes | tagged value of the key | `dd.ct.ui.occupation_hours_zip` | US-CTS5-018 |
| Country Fields / Worksite ZIP code / Additional Notes | tagged value of the key | `dd.ct.ui.occupation_hours_zip` | US-CTS5-018 |
| Country Fields / Hours worked (time-data input) / Additional Notes | tagged value of the key | `dd.de.paid_leave.hours` | US-DES5-013 |
| Country Fields / New York MCTMT zone / Additional Notes | tagged value of the key | `dd.employer.ny_mctmt_zone` | US-NY-003 |
| ID Information / State employer account numbers / Additional Notes | tagged value of the key | `dd.employer.state_account_ids` | US-UTR3-001 |
| Country Fields / ACA monthly employee status / Additional Notes | tagged value of the key | `dd.fed.aca.fte_tracking` | US-FEDS5-012 |
| Country Fields / Hours worked (time-data input) / Additional Notes | tagged value of the key | `dd.fed.aca.fte_tracking` | US-FEDS5-012 |
| Country Option Mappers / ACA monthly employee status | tagged value of the key | `dd.fed.aca.fte_tracking` | US-FEDS5-012 |
| Country Fields / Date services first performed (hire date) / Additional Notes | tagged value of the key | `dd.fed.new_hire.date_first_services` | US-FEDS5-024 |
| Country Fields / Form 8233 treaty exemption claimed / Additional Notes | tagged value of the key | `dd.fed.nra.flag` | US-FEDS5-016 |
| Country Fields / Nonresident alien Form W-4 completed per Notice 1392 / Additional Notes | tagged value of the key | `dd.fed.nra.flag` | US-FEDS5-016 |
| Country Fields / Nonresident alien country of residence / Additional Notes | tagged value of the key | `dd.fed.nra.flag` | US-FEDS5-016 |
| Country Fields / Nonresident alien flag / Additional Notes | tagged value of the key | `dd.fed.nra.flag` | US-FEDS5-016 |
| Country Fields / Nonresident alien visa class / Additional Notes | tagged value of the key | `dd.fed.nra.visa_class` | US-FEDR2-001 |

Borrowed keys (not in DD-8_sheets-facts.json; the value is carried by an approved facts file and cited with its own tag): `fed.ein.format`, `fed.fica.totalization.exemption_rule`, `fed.household.fit.withholding`, `fed.w4.exempt.validity`, `fed.w4.input_fields`, `rspec.fed.aca.form1095c.line14_codes`, `rspec.fed.aca.form1095c.line16_codes`, `rspec.fed.efw2.re.agent_indicator.codes`, `rspec.fed.efw2.re.employment_code.codes`, `rspec.fed.efw2.re.kind_of_employer.codes`, `rspec.fed.efw2.re.tax_jurisdiction.codes`, `rspec.fed.efw2.re.third_party_sick_pay.codes`, `rspec.fed.form944.rule`, `rspec.fed.new_hire.multistate_designation`, `rspec.fed.w2.box14b.ttoc_codes`, `rspec.fed.w2.ssn_truncation`, `sir.fed.efw2.employer_signature_pin`.
Reason: the DD facts carry no enumeration for these lists (W-4 filing status, W-2 code lists, ACA line 14 / 16, Treasury Tipped Occupation Codes, EIN format, Form 944 rule, household withholding, SSN truncation, Signature PIN, totalization rule, new-hire multistate designation). Agent 2 may copy them into the DD facts.

## Scope decisions (INCLUDE / EXCLUDE tree)
| Candidate | Verdict | Test that decided it |
|---|---|---|
| Employee legal name (first, middle, last, suffix) | INCLUDE | master data; present and confirmed (no global master-data file exists to inherit) |
| Employee home address (9 components) | INCLUDE | master data; present and confirmed |
| Employer legal name, address, contact | INCLUDE | master data |
| SSN, EIN, other EIN, agent for EIN, establishment number, State account numbers, Signature PIN | INCLUDE | identifiers = master data / user input |
| Starting compensation, salary, hourly wage (IN, MS, MD new hire; VT wage report) | EXCLUDE | wage amount -> WTC base pay; the DD keeps rate-of-pay basis and pay frequency (codes) only |
| Weeks paid (OH), base weeks (NJ), credit weeks (PA) | EXCLUDE | count / sum of other fields, derived per quarter (F26); facts tagged as "derived values not stored" on the hire / termination date rows |
| Employment on the 12th of the month (counts) | EXCLUDE | derived from hire date, termination date and the payroll calendar (F26) |
| Wages reported to other States in the year | EXCLUDE | wage amount; enters through the YTD load (WTC mechanism) |
| Louisiana workday counter | EXCLUDE | accumulator; YTD load |
| Denver OPT monthly earnings test | EXCLUDE | comparison computed by the payroll calculation; only the work location is held |
| Missouri probationary flag with dates | EXCLUDE | derived flag; the separation date is held |
| Tax withheld, taxable wages, contributions, W-2 box 12 amounts, MBT wage match, AZ sick-time balances | EXCLUDE | calculated amounts (WTC / report computations); none was in the facts |
| MCTMT rate table per zone | EXCLUDE | system constant; the zone is held |
| Hours worked (WA, MN, MA, CT, NE, DE paid leave, OR Form 132, ACA) | INCLUDE as period input from time data | pack class "period input (time data)", not derived; flagged for QA (see below) |
| NY and PA working days | INCLUDE as period input | pack class "period input (working days)"; flagged for QA |
| ACA monthly full-time / FTE status | INCLUDE as an employer-determined status input | specs 'Per Data Dictionary'; pack class "period input (hours) + derived monthly status"; flagged for QA |
| Contractors / Form 1099-NEC | no element | owner scope 2026-10-29 (out of scope) |
| CT Paid Leave employee-level data | no element | fact dd.ct.pfml.employee_level_data: employer totals only |

## RSPEC x DD reconciliation (05-data-dictionary/_build/checks/rspec_dd_recon.csv, dd_element_usage.csv)
Direction 1: 949 field rows of the 20 Report Specs. 192 rows cite the Data Dictionary and map to a DD element; 2 rows cite it and are exceptions; 755 rows do not cite it (payroll results, calculated values, generator configuration: not DD fields by the tree); UNMAPPED = 0.
Name: {'identical name': 9, 'same concept (mapping rule)': 133, 'identical authority label': 50} (a spec row is one record position of a DD concept, so the DD name equals the spec name in 9 rows and the authority label of the spec in 50). Type: {'match': 96, 'n/a': 96} (match = spec column R class compatible with the DD field type; the 27 'n/a' are the State electronic filing threshold rows, where the spec row describes the threshold amount, a jurisdiction constant, and the DD holds the employer flag). Format: Pre-Defined Format is taken from column J where the spec gives a pattern (16 rows identical); 2 rows differ by design and are listed in the CSV: US-DOR-002 row 15, US-SSA-001 row 52 (file layout without the hyphen / State format).
Exceptions (cite the DD, no DD element, by the tree; both for the Report Spec owner to re-point at the next propagation, the specs were not touched):
- US-UI-001 row 10 'Monthly employment counts (pay period including the 12th)': derived: count of employees on the payroll in the pay period including the 12th of each month; computed by the report from hire date, termination date and the payroll calendar (INCLUDE/EXCLUDE tree: count of other fields)
- US-UI-001 row 13 'Weeks counted per employee': derived: weeks paid, base weeks and credit weeks are computed per quarter from wages and pay dates by the report (INCLUDE/EXCLUDE tree: count/sum of other fields; transactional per-payrun value)
Direction 2: 144 of 144 elements have a consumer. 130 elements are cited by a Report Spec row or a spec cell that tags their fact; 14 are named only as inputs of a payroll calculation or notice by their facts (Vacation forfeiture policy acknowledged in writing; Form W-4 filing status (Step 1(c)); Form W-4 multiple jobs or spouse works (Step 2); Form W-4 dependents and other credits (Step 3); Form W-4 other income (Step 4(a)); Form W-4 deductions (Step 4(b)); Form W-4 extra withholding (Step 4(c)); Form W-4 exempt from withholding; State withholding allowances or exemptions claimed; Interstate transport worker type; Military spouse residence election; Working days in the taxing State (nonresident allocation); Total working days in the period; Employee primary language): the WTC and SIR are not built yet, so the consumer is the facts' consumers entry (QA to confirm at the WTC close).

## Lessons from earlier rounds (applied)
1. Every factual cell carries [[FACT:key=value]] with the exact value; dd_lint checks tag = fact (period-aware): 205 tags, 0 mismatches, 0 keys missing.
2. New gaps: marker plus request (DD-RQ-01..04 in _research/DD-research-request.json); documented limitations (TX start quarter, CT Q3 2026 positions, PA PSD code layout, OH municipal code identity, visa class examples) use "not named in the cited sources" and also appear in the request file as RQ-06..RQ-10.
3. No tier-B number: C30 = 0. Register tiers of the 108 facts: {'A.2/active': 70, 'A.1/active': 24, 'A.2/partial': 2, 'A.3/active': 12}.
4. Period awareness: every source cell prints the effective period of its fact ("effective from ...", "effective ... to ..."). dd.oh.school_district_code is the 2025 list (effective 2025-01-01 to 2025-12-31): the cell says the 2026 changes are not named in the cited sources. dd.multi.sui_state has effective_to 2027-06-30. The WTC-side keys ga.sui.new_employer.rate.contribution (2026-01-01) and ma.pfml.* (2027-01-01) are not used by any DD cell.
5. Units from the fact: dd.state.new_hire.rehire_gap_days is written "[[FACT:...=60]] days" (unit_of_measure of the fact); no percentage is written in the workbook (PCT 0, FRAC 0, UNIT 0).
6. Portal and authority names: none is written in the DD (no portal appears). US-LAP52-005 LAWATS is not used.
7. RSPEC x DD: above.
8. Re-pointed elements (precheck-next, tokens only) used by DD cells, each opened in the local copy and read in context: dd.state.w4.ar (AR4ECSP: "You should have a Form AR4EC or AR4ECSP", withholding exemption certificate, US-ARP51-002 p7), dd.state.w4.hi (HW-6 nonresident certificate and HW-7 exemption, US-HIP51-001), dd.state.w4.oh (IT 4 "or the employer must withhold tax based on the employee claiming zero exemptions", US-OHP51-002; the primary row US-OH-002 has no local copy), dd.state.w4.ut (W-4E rule R865-9I and Pub. 14, US-UTPIT-002 / US-UTS5-013), dd.ct.ui.occupation_hours_zip (primary row CGS 31-225a(j)(1)(B) holds the clause "Commencing with the third calendar quarter of 2026 ... may include ... occupation ... hours worked ... zip code of primary worksite"; the re-pointed IP 2026-1 hit is a due-date table and is not relied on), dd.employer.state_account_ids (UT 14-digit "ending in WTH", KS "(036#######F##)", MD CRN positions 338-345, IA 9-digit permit number: each read in its copy). All hold; no cell uses a gap for them. The rows that agent 2 hand-read (OH, PA, FL) were taken as given.
9. _precheck_unmatched facts (7), bound to the fact and not restated as verified: dd.ms.new_hire.extra (DOB), dd.ga.new_hire.extra (DOB), dd.ia.new_hire.health (IWO), dd.ct.ui.occupation_hours_zip (ZIP), dd.state.w4.az (2026), dd.state.w4.mt (DOR), dd.oh.municipal_rate_table (5-digit). Builder read-through of the copies: IWO holds (Iowa Code 252G.3: "address to which income withholding orders ... should be sent"), ZIP holds (CGS 31-225a), DOB is plain wording, DOR is plain wording, 5-digit was hand-read by agent 2; "(2026)" of the Arizona A-4 is not in the page text (the file name of the held copy says 2026).

## Open items (gap markers and limitations)
| id | Location | Marker | Request | Blocking |
|---|---|---|---|---|
| DD-RQ-01 | Country Fields!W83 | in-place marker | dd.state.w4.line_structure | no |
| DD-RQ-02 | Country Option Mappers!F318 | in-place marker | dd.codelists.external | no |
| DD-RQ-03 | Country Option Mappers!F345 | in-place marker | dd.ui.adjustment_reason.codes | no |
| DD-RQ-04 | Country Option Mappers!F114 | in-place marker | dd.fed.depositor_status.codes | no |
| DD-RQ-05 | Country Option Mappers!B67 | in-place marker | dd.fed.special_population.category | no |
| DD-RQ-06 | Country Fields!D41 | neutral wording | dd.tx.ui.enhanced_mandatory_from | no |
| DD-RQ-07 | Country Fields!D48 | neutral wording | dd.ct.ui.q3_2026_positions | no |
| DD-RQ-08 | Country Option Mappers!B336 | neutral wording | dd.pa.psd_code.format | no |
| DD-RQ-09 | Country Option Mappers!B333 | neutral wording | dd.oh.municipal_rate_table.code_identity | no |
| DD-RQ-10 | Country Option Mappers!B76 | neutral wording | dd.fed.nra.visa_class.examples | no |

## For QA to look at (builder findings; none was edited in facts, register or specs)
1. Facts not supported by the local copy of their own register row (word check of the 108 values against the copies, builder side): dd.ms.new_hire.extra (US-MSS5-006 copy is the 15-day law page; it names none of gender, salary, pay frequency, medical insurance, date of birth); dd.ky.locality ("Lexington-Fayette" is not in the Louisville page copy US-KYP9W-001); dd.state.w4.ny ("IT-2104.1" is not in the copy US-NY-001); dd.state.w4.nm ("optional" is not in the copy US-NMP52-001). The cells bind to the facts (the facts file is the contract) and say nothing beyond the tag; agent 2 to confirm or reword.
2. Report Spec forward references to be re-pointed at the next propagation: US-UI-001 row 10 (monthly employment counts) and row 13 (weeks counted per employee) cite "US-DD-001" but are derived values (F26): they belong to the report generator. Specs and DD tag the facts dd.state.ui.month12_count, dd.oh.ui.weeks_paid, dd.nj.ui.base_weeks, dd.pa.ui.credit_weeks.
3. Judgement calls under F26 (Canada precedent): hours worked, NY / PA working days and the ACA monthly status are held as period inputs / employer determinations, not calculated values. If QA reads the Canada precedent more strictly, the fix is to delete 4 elements and re-point the spec rows to the WTC unit-of-measure elements.
4. Special population category: the seven values come from the owner scope statement (_owner_scope, not facts[]), cited as [US-OWN-005] without a tag (RQ-05).
5. Shared C46 on the whole package reports 6 unbound hits in the DD: 5 numeric ISO 4217 codes of the preserved currency sheet (116, 214, 434, 512, 604) and the Treasury Tipped Occupation Code 604 (equal to the numeric fact me.garn.creditor.weekly_protected). Same class as the layout positions and TTOC codes recorded for the Report Specs (checker limitation); the period-aware check counts the TTOC code as DERIVED (row cites US-FEDS6-011, whose tagged value contains it).
6. Excel table objects were removed from the three content sheets (see Deviations).

## Checks run (all on the delivered workbook; outputs in _build/checks/)
| Check | Result |
|---|---|
| C12 structure per template (validate_workbook.py --artifact DD; dd_lint C12) | PASS: 8 sheets in order, header rows 4, ID Information 22 columns A-V, Country Fields 23 labelled columns B-W, mappers B-F; orange columns empty; 7 + 137 data rows counted out of the repeated headers; no duplicate Field Name; every mapper referenced and defined |
| C29 residual markers | 0 |
| WORD pipeline wording | 0 |
| C30 tier-B number | 0 |
| C46 period-aware | 205 tags, 0 mismatches, 0 missing keys, unbound 0, DERIVED 1 |
| FRAC / PCT / UNIT | 0 / 0 / 0 |
| C71 regenerate = issued | PASS (regen_check_dd.py: rebuilt workbook identical) |
| RSPEC x DD reconciliation | UNMAPPED 0; 2 exceptions |
| Excel open (open_check.ps1, COM) | OK |
| validate_contract (research-request) | PASS |
| Report Specs unchanged | md5 of the 20 workbooks equals 04-reports-spec/_build/checks/md5_final.txt (checked before and after the build) |

## Accuracy
About 80%. Every field has an official-source-backed fact or a Report Specification row; the gaps: the line structure of the State withholding certificates (RQ-01), nine external code lists (RQ-02), the UI adjustment reason codes (RQ-03), items bound to facts that the local copies do not support (list above), and the three F26 judgement calls. Closing it needs agent 2 (facts for RQ-01 to RQ-05 and the four copy discrepancies) and the Report Spec owner (two forward references).


## Round 1 fix batch (2026-11-03, builder; QA r1 `_qa/DD-review-r1.json` -> `_batch_fix_list`)
Backup before the batch: `_pipeline/_backup/dd-r1fix-2026-11-03/` (dd/ and rspec/). Facts: `_research/dd-fix/R1-FACTS-READY.md` read; no facts edited. Generator changes only (dd_defs.py, dd_rules.py, dd_common.py, dd_recon.py, dd_lint.py, build_dd.py, write_requests.py).

| QA finding | Action | Where |
|---|---|---|
| 1 F26 hours | element "Hours worked (time-data input)" deleted; W80 reworded ("the supporting hours come from time data, not from this dictionary") | dd_defs.py |
| 2 F26 day counts | "Working days in the taxing State" and "Total working days in the period" deleted; the derived Louisiana workday count (dd.la.workday_counter) is tagged on Residence State with a note that day counts are time data | dd_defs.py |
| 3 C29 | 13 RESEARCH-GAP cells now "Not configured in this release [[GAP:DD-RQ-0n]]: <what is missing>" (W83, W85 RQ-01; mappers RQ-02 x9, RQ-03, RQ-04). The v2.12 C29 HARD list is in dd_common.hard_hits, used by clean() and dd_lint | dd_defs.py, dd_rules.py, dd_common.py, dd_lint.py |
| 10 | ID Information row 13 split into 3 rows: State employer account State (mapper US State or District), programme (new mapper Withholding / Unemployment insurance / Paid leave), number (Text, "Per State format", V tags kept, text: repeat the three fields per State and programme) | dd_defs.py, dd_rules.py |
| 11 | W-2 agent indicator and kind of employer mappers: code "(other)" -> "blank" | dd_rules.py |
| 12 | 9 return-level elements end with "Entered for the return period it applies to (effective-dated per return); not a standing master value." | dd_defs.py (RETURN_LEVEL) |
| facts | E299 regenerated (dd.state.w4.mt, US-MTS5-005). W96: the "2025 list" sentence replaced by a limitation sentence (the full-year nonresident value rests on the 2025 school district list [US-OHS5-019], effective to 2025-12-31; no 2026 restatement is named), so the 9999 rule is not presented as a 2026 rule. dd.ky.locality.lexington bound on the LEX row of the Kentucky locality mapper | build |

Mechanism (C27 / F25): the DD build writes `04-reports-spec/_build/dd_l_overlay.json` (spec id | field position -> column L text) from the reconciliation; `us_book.write` applies it. dd_rules.match_rule resolves a row whose L already lists exact DD Field Names, so the loop is stable (overlay identical on the second pass; DD rebuilt after the specs).

### EXCLUDE table additions (tree: time data / WTC unit of measure, F26)
| Fact | Verdict |
|---|---|
| dd.wa.ui.hours_quarter, dd.mn.ui.paid_hours, dd.de.paid_leave.hours, dd.or.form132.hours | EXCLUDE: hours = WTC unit of measure / time data, accumulated per quarter by the report |
| dd.ma.ui.hours_work_location, dd.ct.ui.occupation_hours_zip, dd.ne.ui.hours_job_title, dd.wa.pfml_ltc.employee_fields, dd.fed.aca.fte_tracking | EXCLUDE for the hours part, same reason (a fact stays bound where its non-hours part is a DD field) |
| dd.multi.ny_convenience_days, dd.multi.pa_working_days | EXCLUDE: day counts = time data / WTC unit of measure feeding NY and PA SIT allocation; an employee-declared estimate would arrive with the dd.state.w4.ny (IT-2104.1) fix, no field added in this batch |

Judgement call 3 of the first build (hours and NY / PA days as period inputs) is withdrawn. Deviation from the QA wording: spec rows that map other DD fields besides hours (UI-001 r14, r49, r97, r107, r185, PFML-001 r33, IRS-007 r6) keep those DD names and add "; payroll result: hours accumulated from time data (WTC unit of measure)"; only the hours-only rows (UI-001 r11, PFML-001 r5) read "Payroll result: ...".

### Open items after the batch
- Facts added by the source hunter and not bound in the DD (outside this batch, for QA r2): dd.fed.depositor_status.codes (closes RQ-04; the depositor status note still cites DD-RQ-04), dd.in.county_code.list, dd.md.county_code.list, dd.oh.municipal.code_list, dd.md.ui.adjustment_reason.codes (RQ-02 / RQ-03 partly closed). The mapper cells keep "Not configured in this release [[GAP:DD-RQ-0n]]".
- `_research/gaps.json` carries no DD-RQ entries (owner: source hunter); needed for C70 on the DD.
- Shared C29 X-run tier: 1 DD cell (ID Information V16, value of sir.fed.efw2.employer_signature_pin, mask S-XXXXXX-Y) and 7 RSPEC cells (SSA-001 x5, same mask; DOR-002 x2, Vermont account mask) hit the X-run rule. Pre-existing (same hits in the backup); the mask sits inside a fact value or authority format text, so it needs a facts reword or a wording change decided by the owner.

### Checks (this batch)
| Check | Result |
|---|---|
| dd_lint C29 (v2.12 HARD list) / WORD / FRAC / PCT / UNIT / C30 / C12 | 0 / 0 / 0 / 0 / 0 / 0 / 0 |
| C46 period-aware | 193 tags, 0 mismatches, 0 missing keys, 0 unbound |
| C71 regenerate = issued (DD) | PASS, 0 differences |
| RSPEC x DD recon | MAPPED 190, NOT-DD 759, UNMAPPED 0, EXCEPTION 0, "(forward reference)" 0 |
| validate_contract --all | PASS 88 files |
| open_check.ps1 (Excel COM) | 21 files, 0 not clean |
| Cell diff vs backup | ID Information: 1 row replaced by 3. Country Fields: 3 rows deleted; Additional Notes changed on 10 rows (facts rewording, W80, W96, residence note); Description changed on 9 rows (return-level sentence). Mappers: 2 codes (other) -> blank, new programme mapper, 11 gap-cell rows, MT / NM / NY / OH / LOU rows (facts). Version Control, Introduction, Instructions unchanged |

### Follow-up before QA r2 (2026-11-03, builder)
- Code-list facts bound (gap cells removed where the RQ is closed): dd.fed.depositor_status.codes (Federal depositor status mapper; RQ-04 closed), dd.in.county_code.list (Indiana county), dd.md.county_code.list (Maryland county), dd.oh.municipal.code_list (Ohio municipal code; RQ-02 closed for these three), dd.md.ui.adjustment_reason.codes (UI adjustment reason mapper; RQ-03 closed for Maryland). Gap cells remaining: 9 (RQ-01 x2, RQ-02 x6: SOC, NAICS, Alaska occupational, Alaska geographic, Ohio school district, Pennsylvania PSD; RQ-03 Massachusetts). Tags 198, mismatches 0, missing 0.
- `_research/gaps.json`: 8 limitation entries DD-RQ-01, 02, 03, 05, 06, 07, 08, 10 (searched, date, what would close it, reason). C70 PASS. Backup `_pipeline/_backup/dd-r1fix-2026-11-03/gaps.json.bak`. RQ-04 and RQ-09 are closed upstream.
- Authority format masks, not placeholders: the 8 shared-C29 X-run hits (`S-XXXXXX-Y` Employer Signature PIN in DD V16 and SSA-001 x5; `WHTXXXXXXXX` Vermont account in DOR-002 x2) are the authority's own character masks, left as written. QA: treat as sanctioned masks (the C29 rule sanctions an X-run only for payslip sheets, code ranges and digit-adjacent masks; these are letter/hyphen-adjacent, so the strict check still lists them).
- DD facts still not bound, all documented EXCLUDE (hours / day counts): dd.wa.ui.hours_quarter, dd.mn.ui.paid_hours, dd.de.paid_leave.hours, dd.or.form132.hours, dd.multi.ny_convenience_days, dd.multi.pa_working_days.
- Overlay `dd_l_overlay.json` unchanged, so the specs were not rebuilt. Checks: dd_lint C29/WORD/FRAC/PCT/UNIT/C30/C12 0; C46 period-aware 0 mismatches; C71 DD PASS; recon MAPPED 190, UNMAPPED 0, forward references 0; validate_contract --all PASS 88; C70 PASS. Diff vs the previous build: only the 5 mapper cells above (depositor status, Indiana county, Maryland county, Ohio municipal code, UI adjustment reason).

### QA r2 builder items (2026-11-03)
- Internal paths: `_research/dd-fix/R2-FACTS-READY.md` read; F338, F344, F347 regenerated from the reworded facts (path clause removed; paths sit in the non-printing `_local_table`). WORD check now also scans the full cell text, tag values included, for internal paths (00-official-sources, _research/, _pipeline/, .json, .py, drive paths): dd_lint and spec_lint (`us_common.PATH_RX`); 0 hits in the DD and the 20 specs.
- F107 (Kentucky locality of work) cites `dd.ky.locality.lexington_name` (no rate); the rate key `dd.ky.locality.lexington` stays unbound in the DD for the WTC.
- Reconciliation direction 2: the State and programme qualifiers of the account number carry the consumers of "State employer account number" (group rule in dd_recon.py); element usage shows every element used (0 with used = NO). V13 and V14 "Used by" text changed accordingly.
- Diff vs the previous build: ID Information V13, V14; Country Option Mappers F107, F338, F344, F347 only. dd_lint all 0 (tags 198), C71 PASS, C70 PASS, validate_contract --all PASS 89 files; overlay unchanged, specs not rebuilt.

### DESIGN QA r1 fields (2026-11-04, builder)
Backup before: `_pipeline/_backup/dd-design-2026-11-04/` (DD, 20 specs, gaps.json, DD-research-request.json). Facts: `_research/design-fix/FACTS-READY.md` (STATUS: COMPLETE). Two legal-entity fields added in ID Information (FR 52560 pattern), consumer = the regulation design:
| Element (id) | Type | Facts bound | Note |
|---|---|---|---|
| Supplemental wage withholding method election (`er.supplemental_wage_method`) | CM, Text, mapper "Supplemental wage withholding method": 1 Flat rate, 2 Aggregate | fed.fit.supplemental.aggregate_method, .flat_rate (mapper), .mandatory_rate, .mandatory_threshold | the mandatory rate above the annual threshold is not an option (stated in the field description) |
| State-assigned unemployment insurance rate (`er.state_sui_rate`) | CM, Decimal, percentage, per State account, effective-dated | none (no per-State notice fact exists) | DD-RQ-11 (request + gaps.json limitation): how each State notifies the rate |
Generator: dd_defs.py (el consumers=), dd_rules.py (mapper), dd_recon.py (element consumers credited in direction 2). dd_common.src writes the unit of a percent fact as "%" right after the tag (UNIT check). Elements 145 (ID 11 + CF 134), mappers 36, tags 202. Recon: overlay unchanged, specs not rebuilt; usage 145/145. Checks: dd_lint all 0, C46 period-aware 0 mismatches, C70 PASS, C71 PASS, validate_contract --all PASS 108, open check 0 not clean, tag_sync: no DD or RSPEC line stale (stale lines are in the design file only). Diff vs backup: 2 ID Information rows and 2 mapper rows added; nothing else changed.
