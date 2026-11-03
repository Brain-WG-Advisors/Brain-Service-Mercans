# RSPEC — build log
Artifact: RSPEC (stage 3) | Country: US | Round: 1 | Built: 2026-11-03 | Package v1.0 (issue date 2027-03-31, from build-manifest.package)
Manifest: _pipeline/build-manifest.json (USD, minor units 2, tier T4, languages: authority-facing English [US-OWN-006])
Scope: scope_manifest.json md5 8c1b7e8a191021db67d3edd8de5fb1ef (20 in-scope filings; related_obligations_no_return treated as rules)
Pack: _research/RSPEC-research-pack.md (md5 ca8906e0f755d14eb9e16c1487fac793) | Facts: _research/RSPEC-facts.json (md5 663758c84a7a5aba6dda0a4120b1e772; 425 facts / 423 keys, 0 blocking, 43 unresolved of which 18 documented limitations)
Consistency source: 01-ccg/US-CCG-001-v1.0.docx (qa_pass) and its module / annex facts.

## Rebuild
`cd 04-reports-spec && python _build/build_specs.py --bindings ../_pipeline/RSPEC-bindings.csv` then `python _build/write_requests.py` (from BASE).
The generator is the only source of the 20 workbooks (`spec_checks.json` → `build_command`; C71 PASS, 0 differences).
Generator files: `_build/us_common.py` (facts, tags, guards), `us_rows.py`, `us_book.py` (shared `mercans_spec.workbook` writer), `us_federal.py`, `us_fed_annual.py`, `us_fed_info.py`, `us_state_core.py`, `us_state.py`, `us_alloc.py` (fact → workbook allocation by key pattern), `us_gaps.py` (neutral wording of every open point), `spec_lint.py`, `c44_mapped.py`, `write_requests.py`. Check outputs: `04-reports-spec/_build/checks/`.

## Precedent inspection (L1)
`ES-M296-001_ResumenAnual_Spec.xlsx` opened with the toolkit `inspect_workbook.py` (openpyxl): 9 sheets — Version Control · Report Matrix · Payroll Scope Summary · M296 Spec · File Structure · Field Options · Population Rules · Example Analysis · TXT Sample File. Core sheet: header row 1, 21 columns A–U (`FF4472C4`, white bold, Google Sans 11), freeze B2, column M width 55. Version Control header row 12 (`FF4BACC6`); Payroll Scope Summary header row 5 (`FF1F4E78`), freeze A6.
Built through the shared library `~/mercans-pipeline/shared/spec-builder/mercans_spec` (no country-specific writer). Differences between the library and the precedent, taken from the library (the approved FR route) and recorded here:
- Sheet 9 is named `Sample File` (precedent `TXT Sample File`); the toolkit contract accepts the suffix.
- Library column widths (M = 62, not 55 or the 70 of the agent doc); Population Rules has 5 columns (library) vs 3 in the precedent.
- Field Options column D header written by the library as "Description (FR)" is overwritten after the call to "Description (Authority wording, EN)"; core-sheet column B is "Field Name (Authority label, EN)" (English is the filing language, US-OWN-006).
- Freeze panes of Field Options / Population Rules are A2 (library), A4 in the precedent.

## Structure decisions (reversible)
| Decision | Class | Reason / inbound contract |
|---|---|---|
| One workbook per in-scope filing of scope_manifest (20) | in scope | "One Report Specification per authority return" with per-State filings grouped as the manifest groups them. Each State / locality return is one Report Matrix row (`<doc>-<USPS>`) and one `═══ <USPS>: <STATE> ═══` section of the core sheet. Reversal = split a workbook by section; no field definition changes. |
| File name `{CODE}-{AUTH}-{NNN}-{ReportName}-Spec.xlsx` without `-v1.0` | in scope | Every shared spec tool (spec_checks, regen_check, C44, C56) globs `*-Spec.xlsx`; the version is internal (Report Matrix "Version", Version Control) and C43 PASS. Deviation from agent §4.1 (version in file name); the Release stage renames if required. |
| Common FIELD MODEL + jurisdiction parameter rows | in scope | The filing channel is the third-party provider hand-off (owner, 2026-10-21; scope integrations): the payroll supplies a logical data set, the provider maps it to each authority wire format. Sheet 5 states "FIELD MODEL: logical model - not the wire/submission format" wherever no layout was read (C23). |
| related_obligations_no_return (registrations, employee notices, WARN, UI agency answers) | owned upstream (CCG rules) | No spec built; notices with a fact (CO DR 0995, NJ BC-10) are listed as NO rows in Payroll Scope Summary. |
| Out-of-scope filings (1099-NEC / CA DE 542, NH BET, territories, certified payroll, Schedule H filing itself, State household / agricultural annual returns) | out of scope | Listed as NO rows with the owner decision (US-OWN-005 / 008 / 009). |
| Shared PFML / levy items carried on combined returns (OR Form OQ, NY NYS-45, NJ NJ-927 / WR-30, NM TRD-41431, VT WHT-436, RI TX-17, CA DE 9C) | inbound contract | Specified on the carrying return (DOR-001 / UI-001) and cross-referenced from PFML-001, DOR-004 and WC-001; never duplicated. |

## Filing → spec crosswalk (C44 / C18)
`04-reports-spec/_build/filing_crosswalk.json`. 20/20 filings have exactly one spec; no spec without a filing.
| # | Filing (scope_manifest) | Spec |
|---|---|---|
| 1 | IRS Form 941 | US-IRS-001-Form941 |
| 2 | IRS Form 944 | US-IRS-002-Form944 |
| 3 | IRS Form 943 | US-IRS-003-Form943 |
| 4 | IRS Form 940 | US-IRS-004-Form940 |
| 5 | Schedule H routing | US-IRS-005-ScheduleHRouting |
| 6 | SSA Forms W-2 / W-3 (W-2c) | US-SSA-001-FormW2W3 |
| 7 | IRS Form 1042-S | US-IRS-006-Form1042S |
| 8 | IRS Forms 1094-C / 1095-C | US-IRS-007-Forms1094C1095C |
| 9 | IRS Form 941-X | US-IRS-008-Form941X |
| 10 | State withholding returns and deposits | US-DOR-001 (51 rows: 42 returns, 9 "no return") |
| 11 | State annual reconciliation and State W-2 | US-DOR-002 (42 States) |
| 12 | State UI quarterly contribution and wage report | US-UI-001 (51) |
| 13 | State PFML / SDI / LTC programme reports | US-PFML-001 (11) |
| 14 | Local income / wage tax returns | US-LOC-001 (10 jurisdictions) |
| 15 | City employer payroll taxes (Jersey City, Newark, St. Louis, Pittsburgh) | US-LOC-002 (3) |
| 16 | Seattle PET and Social Housing Tax | US-LOC-003 (1) |
| 17 | Nevada MBT (TAX-F003) | US-DOR-003 (1) |
| 18 | Employer payroll transit levies (OR, NY) | US-DOR-004 (2) |
| 19 | State-fund workers' compensation (WA, NM, OR, WY) | US-WC-001 (4) |
| 20 | New-hire report | US-SDNH-001 (51) |

## STEP 3.5 — submission format (C23 / C24 / C25)
- Every Report Matrix row carries `Channel: <classes> | Portal: <names + URL> | Source: <url> | CONFIRMED|TO CONFIRM` plus an accuracy %. Channel classes come from the channel / format / form fact values (`us_common.channel_types`).
- `xml` is recorded only where the fact value names a schema or file specification (FL RT XSD package, MI MiUI XML spec v1, CT Paid Leave toolkit XSD, MD BEACON spec, CA DE 8300, OH SD FSET 4.4). Indiana XML is open (RSPEC-GAP-014: schema package not held).
- Portals are per institution: revenue portals only in DOR-001/002, UI portals only in UI-001, programme portals only in PFML-001.
- Sample File sheets: no sample pasted and none constructed in any workbook; each states the verified channel. The official FL RT-6 XML sample package is named in the UI-001 FL row only.
- Filing consolidation is taken from the facts (combined returns above); nothing assumed.
- "FORMAT TO CONFIRM vs a real filing" is written in every File Structure sheet: no real filed sample exists for any return.

## Fact bindings
Full binding table: `_pipeline/RSPEC-bindings.csv` (location → key → register_id → effective_from → facts file; 1,123 rows, 521 keys).
- 423/423 RSPEC fact keys are bound at least once (spec_lint "UNUSED RSPEC FACTS" = []).
- 98 keys come from other facts files already used by the CCG for the same register rows (CCG FED / NV / OR / NM / NJ / PA / WA / CO / MO / DE / KY annexes, m01, m10; DD; SIR; WTC). Reason: the RSPEC facts carry no rates or thresholds for FICA, FUTA, household, agricultural, NV MBT, transit, WC fees or city taxes, and the DD facts carry the field definitions the System Mapping refers to. Every such key is a validated fact with a tier-A register row.
- 1,338 `[[FACT:key=value]]` tags; 0 key missing; 0 value mismatch on a period-aware comparison; multi-period keys (`fed.fica.oasdi.wage_base` 2026 / 2027, NM WC fee 2025-2028 / 2028-2033) are written with the 2026 value.
- Rates are stored in percent in the facts and written as "<value>%"; computations divide by 100.
- Positions in column H come from the layout facts (EFW2 RE / RW / RO / RU / RS / RF) and are re-derived by `positions()` from the fact text; field lengths are computed (end − start + 1).

| Location (sample) | Claim | key | register_id |
|---|---|---|---|
| US-SSA-001 W-2 EFW2 Spec!H/M row W2-011 | Signature PIN 319-328, Luhn check | `rspec.fed.efw2.re.layout_ty2026` | US-FEDS5-032 |
| US-SSA-001 W-2 EFW2 Spec!M row W2-016 | social security wage base 184,500 (2026) | `fed.fica.oasdi.wage_base` | US-FEDS5-005 |
| US-DOR-002 State Annual Recon W-2 Spec rows RS-001..RS-024 | generic RS positions | `rspec.fed.efw2.rs.layout` | US-FEDS5-032 |
| US-UI-001 UI-C-011 | NJ base week 310; PA credit week 116 | `rspec.nj.ui_qtr.base_week_amount`; `pa.report.ui.credit_week.amount` | US-NJS5-010; US-PAS5-013 |
| US-DOR-003 MBT-C-003 | 1.17% above 50,000 a quarter | `nv.mbt.general.rate`; `nv.mbt.general.quarterly_threshold` | US-NVP51-002; US-NVS5-011 |

## Checks
| Check | Result | Note |
|---|---|---|
| Toolkit pre-flight `validate_workbook.py --artifact RSPEC` ×20 | PASS 20/20 | 9 sheets, core sheet 21 columns A–U, 0 blocker / 0 major / 0 minor |
| C12 columns populated (core sheet) | PASS | 20 of 21 on every workbook; column U (RA Comments) left for the Regional Advisor |
| Column M blank on a field row | PASS 0 | 646 field rows (all workbooks) |
| Row width ≤ header columns, every sheet | PASS 0 cells beyond the header |  |
| C29 residual markers (toolkit regex, every cell) | PASS 0 | gap texts curated in `us_gaps.py`; "xxx" in a statute lead removed |
| Pipeline wording outside tags | PASS 0 | guard `us_common.clean()` raises at build time |
| C30 (tagged number whose register rows are all tier B/C or MANUAL) | PASS 0 |  |
| C42 (foreign series / precedent markers; specs) | PASS 0 hits | series IRS, SSA, DOR, UI, PFML, LOC, WC, SDNH: none used by BE/CO/FR |
| C43 package version | PASS | file names carry no version; Report Matrix / Version Control = 1.0 |
| C44 shared | SKIP | shared check pairs a spec to a filing only when filing_id is a document id; US filing ids are descriptions |
| C44 crosswalk (`c44_mapped.py`, same FAMILIES rule) | PASS 20/20 | 5 manifest formats name a family (W-2 text; Seattle, transit, new-hire portal; NV pdf/paper) and the spec supports each |
| C46 shared, restricted to the specs | FAIL (checker limitation) | 19 "mismatches" = the shared checker keeps one value per key: `fed.fica.oasdi.wage_base` (2027 value loaded last) and the NM WC fee keys (2028 value); 9 "unbound": 5 file positions in column H equal to unrelated facts (214, 225, 276, 319 ×2) and 4 hits of "129.2" inside the NC new-hire URL (G.S. 110-129.2). Binding 99.3%. |
| C46 period-aware (`spec_lint.py`) | PASS | 1,338 tags, 0 mismatches, 0 keys missing; unbound 4 (the NC URL only) |
| C56 (mandatory field without mapping or source) | PASS | 640 mandatory / conditional fields |
| C70 (citations, gap phrases) | PASS | 0 unregistered citations, 0 gap phrases |
| C34 / C35 / C36 | FAIL (gated) | no machine-readable norm, no authority validator, no US identifier plugin; the gate turns SKIP into FAIL without `validation_exemptions.<check>` in the build manifest. Not written by the builder (owner decision). Candidate country support: EFW2 Employer Signature PIN Luhn check (C36), FL RT XSD and MI MiUI validator (C35). |
| C71 regenerate = issued (`regen_check.py`) | PASS | 20 files, 0 differences |
| Excel open check (`open_check.ps1`, COM) | PASS | 20 files, 0 failed / repaired |
| validate_contract --all | PASS | 83 files incl. `_research/RSPEC-research-request.json` |
| C49 / C53 (content checks) | not applicable yet | FAIL only because 02-wtc and 03-statutory-integrations are not built; the specs cite no WTC code |

## Open items — gaps by return
Recorded limitations (gaps.json → RSPEC) are cited as `[[GAP:RSPEC-GAP-nnn]]`; builder requests as `[[GAP:RSPEC-RQ-nn]]` (to be added to gaps.json by agent 2). All non-blocking.
| Spec | Open points |
|---|---|
| US-IRS-001 / 002 | RQ-01 (941 / 944 line map) |
| US-IRS-003 | RQ-04 (943 lines and due date) |
| US-IRS-004 | GAP-001 (2026 i940), RQ-08 (940 line map, credit-reduction States) |
| US-IRS-005 | RQ-09 (statement for the household employer) |
| US-SSA-001 | RQ-02 (RA / RW / RT positions and RE code lists from the held Pub. 42-007), RQ-03 (W-2 box map, tipped occupation code list) |
| US-IRS-006 | RQ-05 (1042-S codes) |
| US-IRS-007 | GAP-002 (2026 i1094/1095-C), RQ-06 (1095-C line codes) |
| US-IRS-008 | RQ-07 (941-X lines) |
| US-DOR-001 | GAP-006 (DE), GAP-014 (IN XML), GAP-027 (NM) |
| US-DOR-002 | GAP-008 (GA), 010 (HI), 012 (ID), 013 (IL), 015 (KS), 016 (KY), 017 (LA), 018 (MA), 020 (MD), 021 (ME), 027 (NM), 029 (NY), 035 (SC), 039 (WV) |
| US-UI-001 | GAP-003 (CO), 005 (CT), 007 (DE), 009 (GA), 011 (IA), 023 (MN), 024 (MT), 025 (NE), 026 (NH), 027 (NM), 028 (NV), 030 (OH), 031 (OK), 036 (SD), 037 (TX), 038 (UT), 040 (WY), 041 (AR), 043 (AZ) |
| US-PFML-001 | GAP-019 (MA) |
| US-LOC-001 | GAP-032 (Portland), RQ-11 (WV municipal service fees) |
| US-LOC-002 | RQ-12 (Pittsburgh return) |
| US-LOC-003 | RQ-13 (Seattle base, thresholds, due dates) |
| US-DOR-004 | RQ-14 (MCTMT rates, MTA-305 lines) |
| US-WC-001 | GAP-042 (WA L&I quarterly report) |
| US-SDNH-001 | GAP-004 (CO), 022 (MI), 033 (PA), 034 (RI) |
Totals: 43 recorded limitations cited (all 43 open RSPEC gaps), 13 builder requests (`_research/RSPEC-research-request.json`, RQ-01..RQ-09, RQ-11..RQ-14; severity major except RQ-09 minor).

## Findings for other agents (not fixed here)
- Agent 2: `rspec.nj.ui_qtr.base_week_amount` = 310 cites US-NJS5-010, while the CCG key `nj.ui.base_week.amount` cites US-NJS5-011 for 2026 (310) and US-NJS5-010 for 2027 (319). Same value for 2026; the register id of the RSPEC fact looks like the 2027 row.
- Agent 2: unresolved notes of the RSPEC facts carry research wording ("Stage-5", "tier-B leads", "registered", "not obtained"); the deliverable uses curated wording (`_build/us_gaps.py`) instead. Please add RSPEC-RQ-01..14 to `_research/gaps.json`.
- Owner / orchestrator: decide `validation_exemptions.C34/C35/C36` (reason, official URL, decided_on) or commission a `countries/us.py` plugin; the builder must not write exemptions.
- Shared-tool owner: C46 one-value-per-key (multi-period keys), C46 position / URL false positives, C44 filing-id pairing, file-name version vs `*-Spec.xlsx` glob.

## Accuracy
Mean of the 227 return rows: **78%**. By workbook: SSA-001 85%, IRS-005 85%, DOR-002 84%, UI-001 80%, DOR-001 77%, PFML-001 76%, IRS-001/002/004, LOC, DOR-003/004, WC, SDNH 75%, IRS-003 70%, IRS-006 70%, IRS-007 65%, IRS-008 60%.
Basis: official authority pages and, where read, the authority file specification (EFW2 TY2026, FL RT XML, AK CSV, CT 276-character layout, MI MiUI, MD BEACON, NC TY2026, SC SUITS); no real filed sample for any return. What closes the gap: the 13 requests above (several read from files already held, e.g. Pub. 42-007), the 18 documented limitations (US network exit, employer / TPA portal logins, unpublished 2026 editions), and the provider's import layout plus one accepted real filing per authority.

## Delivered files (md5)
```
397e3a7dd5ef90bc6019dba4d03095ed *04-reports-spec/US-DOR-001-StateWithholdingReturns-Spec.xlsx
c6ddcda6c3420d259a70b5c8dc54ea1e *04-reports-spec/US-DOR-002-StateAnnualReconciliationW2-Spec.xlsx
8a3f57ff6563e3215a8865c2eada1cc1 *04-reports-spec/US-DOR-003-NevadaMBT-Spec.xlsx
35656ed086a9cf28b3123b111ccce1b3 *04-reports-spec/US-DOR-004-PayrollTransitLevies-Spec.xlsx
9e5e71e5bc230c5ecd161902a35c52b0 *04-reports-spec/US-IRS-001-Form941-Spec.xlsx
e4cde313e6e32435b2ec759a907ebc45 *04-reports-spec/US-IRS-002-Form944-Spec.xlsx
3f5543b2bef6207f360eb0327e4fd8fc *04-reports-spec/US-IRS-003-Form943-Spec.xlsx
1d79377bd247bb7bc7f2485cc00192ba *04-reports-spec/US-IRS-004-Form940-Spec.xlsx
1f4b054ac49dbb34187ee024dcefd15d *04-reports-spec/US-IRS-005-ScheduleHRouting-Spec.xlsx
ce00c6fe3787d6b541da9cad67c85ff2 *04-reports-spec/US-IRS-006-Form1042S-Spec.xlsx
cede6b9cd7b4890ddb50358dd202b4fd *04-reports-spec/US-IRS-007-Forms1094C1095C-Spec.xlsx
6c11cf47e466f9b16ef4b13ff6fa7d70 *04-reports-spec/US-IRS-008-Form941X-Spec.xlsx
b42a6ce2c9ca173d24490d1ff9095e81 *04-reports-spec/US-LOC-001-LocalIncomeWageTaxReturns-Spec.xlsx
29810af50eb8e8b8d24ba3fc06ef538c *04-reports-spec/US-LOC-002-CityEmployerPayrollTaxes-Spec.xlsx
9951441655f69658bc3b1e076b2b633a *04-reports-spec/US-LOC-003-SeattlePETSocialHousing-Spec.xlsx
f254cbd573fce911fccac25084152be7 *04-reports-spec/US-PFML-001-PFMLProgrammeReports-Spec.xlsx
3aacb37a5c291f2256229cd2b91921a2 *04-reports-spec/US-SDNH-001-NewHireReport-Spec.xlsx
3916a9373f85cc572cfbc87e2364707b *04-reports-spec/US-SSA-001-FormW2W3-Spec.xlsx
57b9e4b4bf6833bdc3aa84daeaa79dbe *04-reports-spec/US-UI-001-StateUIWageReports-Spec.xlsx
a1d834dde4aad9b3e78bbab39a43249f *04-reports-spec/US-WC-001-StateFundWorkersComp-Spec.xlsx
```
