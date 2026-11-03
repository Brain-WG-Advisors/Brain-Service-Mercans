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

## Rebuild with RQ facts (2026-11-03, before QA round 1)
Inputs: `_research/RSPEC-facts.json` (md5 42af6bb3dd37586ac1041ccb23ed8946; 493 facts / 490 keys, 46 unresolved, 0 blocking; +68 facts from agent 2, see `_research/rspec-rq/AGENT2-RSPEC-RQ.md`), `RSPEC-research-pack.md` (md5 dccc5109390336152e534be11faf7d0f), `gaps.json` (md5 243ce41d7db58cb42679a0d4662671a6), register (md5 d47ca144fa0b82105ccc1603da7f02fb, read only).
Backup taken before any change: `_pipeline/_backup/RSPEC-pre-RQ-rebuild-2026-11-03/` (`_build/`, the 20 workbooks, bindings, this log, the request file).
Commands: `cd 04-reports-spec && python _build/build_specs.py --bindings ../_pipeline/RSPEC-bindings.csv`, then `python 04-reports-spec/_build/write_requests.py` (from BASE). Only the generator and its inputs changed; no workbook was edited by hand. Binding table: 1,539 rows, 590 keys.

### Generator changes
| File | Change |
|---|---|
| `us_lines.py` (new) | Line-map parser (`P1: 1 label; 2 label \| P2 ...`), record-layout parser (`a-b Name`), named-position parser (RS / RO / RU), code-list parser, contiguity check 1..512 (G-SPOT), line rows mapped to the field model, File Structure line tables. |
| `us_w2.py` (new; W-2 builder moved out of `us_fed_info.py`) | US-SSA-001 rebuilt as the EFW2 wire format: RA 40, RE 30, RW 51, RT 30 fields (each record checked contiguous to 512 at build time), RO / RU TY2026 money fields plus allocated tips (box 8, position from the box map), RS generic, RF; money-field encoding row; W-2 box map row; code lists (agent indicator, kind of employer, employment code, tax jurisdiction, third-party sick pay) and the 71 + 000 Treasury Tipped Occupation Codes in Field Options (count asserted against `rspec.fed.w2.box14b.ttoc_count`); RE TY2026 summary asserted equal to the full RE layout. Row ids are now `W2-<record>-nnn` and `W2-Rnn` (form rules). |
| `us_federal.py` | Form 941: line rows of Rev. 3-2026 (F941-L00..L25) mapped to F941-005..013; Schedule B row F941-017; F941-013 open-point text replaced. |
| `us_fed_annual.py` | Form 944 / 943: due-date rows and line rows (per 2026 draft); Form 940: Schedule A row, 2025 final credit-reduction list (period 2025) and DOL potential 2026 rates, the 2026 list as limitation, line rows (per 2026 draft); Schedule H: statement rows SCHH-005..012, due date, thresholds. |
| `us_fed_info.py` | 1042-S box-code rows F1042S-006..011 (codes 18 / 04 / 16 tagged); ACA: 1095-C lines 14-17, TY2026 dates, 1094-C line rows (per 2026 draft), line 14 / 16 code lists; 941-X: process rule, time limits, line rows of Rev. 4-2026. |
| `us_state.py`, `us_state_core.py` | `custom` / `skip` / per-jurisdiction `what` / `matrix_fix` hooks. Seattle (thresholds, tiers, SHT, schedule; two computed examples), NY MCTMT (threshold, zone rate tables, computed example), WV (Charleston, Morgantown; other cities as limitation), Pittsburgh ET-1 (2026 edition as limitation), NJ base week 2026 / 2027 (example notes now computed: the previous note omitted 117.00 among the weeks below 310). |
| `us_alloc.py` | Seattle keys to US-LOC-003 (they fell into LOC-001 WA and were not rendered); Pittsburgh to US-LOC-002 (was LOC-001 PA); federal RQ keys allocated to their specs (only orphan `rspec.fl.other_forms`, as before). |
| `us_common.py` | `note_use` (derived locations in the binding log), `per_draft` ("Per 2026 draft" marker read from the fact note), `retag` (a figure inside a rendered label re-tagged with its own fact), `quote` (untaggable facts, below); guard: `tag()` refuses a value containing `]`. |
| `us_gaps.py` | RSPEC-GAP-001 / 002 wording narrowed to "final 2026 edition not issued; 2026 draft applied"; partial-request wording for RQ-08 / 11 / 12 (open part only) mapped to the request ids; RQ-15 added. |
| `spec_lint.py` | C46p DERIVED rule (below); quoted untaggable facts reported separately. |
| `write_requests.py` | Merges with `_research/RSPEC-research-request.json` instead of overwriting it (agent 2's `_status` / `_closed_*` / `_resolution_note` kept); stops if a closed request's tag is still written. |
| `regression_diff.py` (new) | Cell-by-cell diff of two folders of workbooks (regression guard). |

### Requests rendered
| RQ | Result in the workbooks |
|---|---|
| 01 | US-IRS-001 line rows + Schedule B; US-IRS-002 line rows and due date (per 2026 draft). Tags removed. |
| 02 | US-SSA-001 RA / RE / RW / RT layouts with positions; File Structure is the wire format; RE code lists. Tags removed. |
| 03 | W-2 box map (row W2-004, Field Options, box on each RW / RO field), box 14b rule, TTOC list (72 rows). Tags removed. |
| 04 | US-IRS-003 due date + line rows (per 2026 draft). Tag removed. |
| 05 | US-IRS-006 box-code rows. Tag removed. |
| 06 | US-IRS-007 lines 14-17, 1094-C lines, dates, affordability (per 2026 draft). Tag removed; RSPEC-GAP-002 kept for the final 2026 instructions. |
| 07 | US-IRS-008 process rule, time limits, line rows. Tag removed. |
| 08 (partial) | US-IRS-004 lines, Schedule A, 2025 final list rendered; the 2026 list cited `[[GAP:RSPEC-RQ-08]]` (F940-011, Report Matrix); RSPEC-GAP-001 kept for the final 2026 form and instructions. |
| 09 | US-IRS-005 statement rows, due date. Tag removed. |
| 11 (partial) | US-LOC-001 WV: Charleston and Morgantown rows; other cities `[[GAP:RSPEC-RQ-11]]` (LOC-WV-005, Report Matrix). |
| 12 (partial) | US-LOC-002 PA: ET-1 row (2025 structure); 2026 edition `[[GAP:RSPEC-RQ-12]]` (LOC-PA-003, Report Matrix, File Structure). |
| 13 | US-LOC-003 thresholds, tiers, SHT, schedule, examples. Tag removed. |
| 14 | US-DOR-004 NY threshold, zone rate tables, example. Tag removed. |
| NJ | UI-C-011: 310 for 2026 (US-NJS5-011) and 319 from 2027-01-01 (US-NJS5-010), period-aware tags. |
| RQ-15 (new) | RO / RU fields beyond the TY2026 money fields and allocated tips (rows W2-RO-900, W2-RU-900, File Structure); minor, non-blocking; written to the request file. |

### Deviations and decisions
- **Untaggable facts.** `rspec.fed.form1042s.wage_codes` and `rspec.wv.local.service_fee_returns` carry `[` `]` in their value, which the `[[FACT:key=value]]` grammar cannot hold (the tag would end at the first `]`). They are quoted with parentheses and their register id (F1042S-006 and File Structure; LOC-WV-004) and logged as derived locations; their component codes (18, 04, 16) and the two city facts are tagged. Finding for agent 2: rephrase both values without square brackets; the builder then tags them.
- **C46p DERIVED rule.** A number in a row rendered from a layout or line-map fact (position, line number, TTOC code) is not counted as unbound when the same sheet row cites the register id of a fact whose full value is tagged in the same workbook and contains that number. 38 such hits (SSA-001 File Structure / Field Options, DOR-002 RS positions). Spec-sheet columns H / I positions stay excluded as before.
- **Mandatory flag of EFW2 fields.** The layout facts carry positions, not the required / optional flag of each field. Y is set only where the facts support it (record identifier, blanks, money fields zero-filled, SSN, submitter and employer EIN, tax year, names, 1/0 sick-pay indicator); other content fields are C with "FORMAT TO CONFIRM vs a real filing".
- **Seattle PET rates** exist only inside `rspec.wa.local.seattle.base_thresholds_due` (no rate keys): the tier and band selection is computed, the PET amount is not (it would need a typed rate). Social Housing Tax and MCTMT amounts are computed from tagged rates.
- **MCTMT band** read from the zone payroll of the quarter (lines 1a / 1b); column T says "Confirm against a real filing".
- **Report Matrix rows** of Seattle, NY MCTMT, WV and Pittsburgh are set from the facts (`matrix_fix`): paper (WV, Pittsburgh), FileLocal or mail (Seattle), Web File (NY). The generic classifier had read "online_form" and the portal "MTA" from the form name.

### Checks (final build)
| Check | Result | Note |
|---|---|---|
| Toolkit pre-flight `validate_workbook.py --artifact RSPEC` ×20 | PASS 20/20 | 0 findings (`_build/checks/preflight.txt`) |
| C12 | PASS | 20 of 21 columns on every core sheet (U left for the Regional Advisor); 949 field rows, 0 blank M |
| Row width ≤ header, every sheet (column-count lint) | PASS 0 | |
| C29 residual markers | PASS 0 | |
| Pipeline wording outside tags | PASS 0 | build-time guard and lint |
| C30 | PASS 0 | |
| C42 / C43 | PASS / PASS | 0 foreign markers; package 1.0 |
| C44 crosswalk (`c44_mapped.py`) | PASS 20/20 | |
| C46 period-aware (`spec_lint.py`) | PASS | 1,461 tags, 0 mismatch, 0 key missing; unbound 4 (NC URL G.S. 110-129.2, as before); 38 derived; 2 quoted untaggable; 0 RSPEC key unbound |
| C46 shared, specs only | FAIL (checker limitation, as before) | 26 "mismatches" = one value per key (OASDI 2026 / 2027 ×14, NJ base week 2026 / 2027 ×4, NM WC fees ×8); 59 "unbound" = layout positions, TTOC codes and line numbers (SSA-001 51, DOR-002 4) and the NC URL (4) |
| C56 | PASS | 934 mandatory / conditional fields, 0 problems |
| C70 | PASS | 0 unregistered citations, 0 gap phrases |
| C71 regenerate = issued | PASS | 20 files, 0 differences |
| Excel open (`open_check.ps1`) | PASS | 20 files, 0 not clean |
| validate_contract --all | PASS | 83 files, incl. the merged request file |
| C34 / C35 / C36 | FAIL (gated, unchanged) | no norm / validator / US plugin; owner decision on `validation_exemptions` still open |

### Regression guard (cell diff vs `_pipeline/_backup/RSPEC-pre-RQ-rebuild-2026-11-03/specs`)
Output: `04-reports-spec/_build/checks/regression_vs_pre_rq.json`. No fact key removed from any workbook.
| Workbook | Changed cells | Explained by |
|---|---|---|
| DOR-001, DOR-002, DOR-003, PFML-001, SDNH-001, WC-001 | 0 | not touched by the RQ facts |
| IRS-001 / 002 / 003 / 004 / 005 / 006 / 007 / 008 | 658 / 512 / 441 / 611 / 234 / 166 / 742 / 744 | RQ-01, 01, 04, 08, 09, 05, 06, 07 (line maps, codes, dates; inserted rows shift the following cells); tags RQ-01..07, 09 removed, RQ-08 kept for the 2026 list |
| SSA-001 | 4,398 | RQ-02 / RQ-03: full EFW2 layouts (rows renumbered by record), box map, code lists, TTOC list, wire-format File Structure; RQ-15 added |
| LOC-001 / 002 / 003 | 95 / 48 / 187 | RQ-11 / RQ-12 / RQ-13 |
| DOR-004 | 219 | RQ-14 |
| UI-001 | 40 | NJ 2026 / 2027 base week (UI-C-011, NJ register id, Example Analysis rows shifted by the added 2027 line, corrected note) |

### Open items after the rebuild
| Location | Marker | Request | Blocking |
|---|---|---|---|
| US-IRS-004 F940-011, Report Matrix | `[[GAP:RSPEC-RQ-08]]` final 2026 credit-reduction list | RQ-08 (documented limitation; DOL list after 2026-11-10) | no |
| US-LOC-001 LOC-WV-005, Report Matrix | `[[GAP:RSPEC-RQ-11]]` other WV municipal service fees | RQ-11 (documented limitation) | no |
| US-LOC-002 LOC-PA-003, Report Matrix, File Structure | `[[GAP:RSPEC-RQ-12]]` 2026 Form ET-1 | RQ-12 (documented limitation) | no |
| US-SSA-001 W2-RO-900, W2-RU-900, File Structure | `[[GAP:RSPEC-RQ-15]]` other RO / RU positions | RQ-15 (new, minor) | no |
| US-IRS-004 / US-IRS-007 | `[[GAP:RSPEC-GAP-001]]` / `[[GAP:RSPEC-GAP-002]]` final 2026 IRS editions | recorded limitations | no |
| Other specs | 41 further RSPEC-GAP ids, unchanged | recorded limitations | no |
Findings for agent 2: add RSPEC-RQ-15 to `gaps.json`; rephrase the two bracketed fact values.

### Accuracy (Report Matrix)
SSA-001 90% (was 85), IRS-005 90% (85), IRS-001 85% (75), IRS-008 85% (60), DOR-004 NY 85%, LOC-003 85% (75), IRS-002 / 003 / 004 80% (75 / 70 / 75; per 2026 draft), IRS-006 80% (70), IRS-007 75% (65), LOC-001 WV 75%, LOC-002 PA 75%; other workbooks unchanged. What closes the rest: the final IRS 2026 editions (normally December), the DOL 2026 list, the RO / RU tables of Pub. 42-007, the provider import layouts and one accepted real filing per return.

### Delivered files (md5, final build)
```
08c956e2b16eaae0265b04dd79fdd220 *04-reports-spec/US-DOR-001-StateWithholdingReturns-Spec.xlsx
adff5cc6682fc24d0e47418804151998 *04-reports-spec/US-DOR-002-StateAnnualReconciliationW2-Spec.xlsx
9a4a31bd06cc0a90db54d322b43ca529 *04-reports-spec/US-DOR-003-NevadaMBT-Spec.xlsx
c324c6468ab82deaac798139a3d60235 *04-reports-spec/US-DOR-004-PayrollTransitLevies-Spec.xlsx
b690747d2dbbaa826f9b8201b7f2ffd2 *04-reports-spec/US-IRS-001-Form941-Spec.xlsx
b23e1ed06ed53f4a4beb6f999ce6a299 *04-reports-spec/US-IRS-002-Form944-Spec.xlsx
2272c10ac6bb345c9d254bb036d44e32 *04-reports-spec/US-IRS-003-Form943-Spec.xlsx
4c5fadf632a6faf92f84e4b1e2a55f78 *04-reports-spec/US-IRS-004-Form940-Spec.xlsx
266dede591b5b9e601d613b957059493 *04-reports-spec/US-IRS-005-ScheduleHRouting-Spec.xlsx
ae1f34ffbc6c929985f75cd3259af836 *04-reports-spec/US-IRS-006-Form1042S-Spec.xlsx
5c7e90d4a445c24a9cc3324965454eee *04-reports-spec/US-IRS-007-Forms1094C1095C-Spec.xlsx
bbfc43bde3cbfc5e447550314df11364 *04-reports-spec/US-IRS-008-Form941X-Spec.xlsx
57e440c6375677864a3171b6bd4e2138 *04-reports-spec/US-LOC-001-LocalIncomeWageTaxReturns-Spec.xlsx
b7e73274ef38bc1a2d90cae1456a3b9e *04-reports-spec/US-LOC-002-CityEmployerPayrollTaxes-Spec.xlsx
617771a618099e026025fb892ff4bbcf *04-reports-spec/US-LOC-003-SeattlePETSocialHousing-Spec.xlsx
ed7773f9b46f5deec0b9194731b8a29d *04-reports-spec/US-PFML-001-PFMLProgrammeReports-Spec.xlsx
53081e8018ad7f1ad9a6e89391241a51 *04-reports-spec/US-SDNH-001-NewHireReport-Spec.xlsx
3ae10be010338ddc292bcad80ce3be26 *04-reports-spec/US-SSA-001-FormW2W3-Spec.xlsx
50eb45a2bc0ccb122dbe3ed5b2118329 *04-reports-spec/US-UI-001-StateUIWageReports-Spec.xlsx
826bacb52f85d92ad8513d4e8959f20d *04-reports-spec/US-WC-001-StateFundWorkersComp-Spec.xlsx
86f0b18b90736219eaf62e8c429830b4 *_research/RSPEC-research-request.json
3f3177a3922ffbb8c038f566ec47db66 *_pipeline/RSPEC-bindings.csv
```

## Round 2 rebuild (2026-11-03, after `_qa/RSPEC-review-r1.json`)
Inputs: `_research/RSPEC-facts.json` md5 dbd99f8f19a2245074084cc32b69789e (493 facts / 490 keys, 47 unresolved, 0 blocking), `gaps.json` 1da44aab264aa00018a5957ebdf82090, register de5fc2dd131c151724c38e07af4c738f (2,697 rows; read only), agent 2 notes `_research/rspec-r1-fix/AGENT2-RSPEC-R1.md` (READY-FOR-BUILD flag written 10:25).
Backup before any change: `_pipeline/_backup/RSPEC-pre-r2-rebuild-2026-11-03/` (`_build/`, `specs/` = the 20 round-1 workbooks + spec_checks.json, bindings, facts, request file, this log).
Commands: `cd 04-reports-spec && python _build/build_specs.py --bindings ../_pipeline/RSPEC-bindings.csv`; `python 04-reports-spec/_build/write_requests.py` (from BASE). Generator only; no workbook edited by hand. Bindings: 1,557 rows, 590 keys, 327 register rows.

### Findings routed to the builder
| # | Finding | Result | Generator change |
|---|---|---|---|
| 5 | DERIVED rule hid 7 percentages | fixed | `spec_lint.py`: DERIVED applies only to integer tokens (no `%`, no decimal part); the count is still reported (31, all integer layout / code values). IRS-003 line labels and File Structure: 0.9% re-tagged `fed.fica.addl_medicare.rate`; 2.9% and 12.4% (combined rates printed by Form 943; no combined-rate fact exists) are written as the sum of the employee and employer facts (`us_common.retag_sum`, total computed from the facts: `(1.45% employee + 1.45% employer)`). IRS-004 K15: no 2025 CA rate key exists, so the example tags the 2025 list fact with period 2025 (`ca_2025_example()` switches to a dedicated 2025 CA key if one is added). |
| 6 | 33 one-sentence Field Explanations | fixed (33/33) | `us_state.py` (DOR-C-005/007, RS-024, MBT-C-002/003, TRN-C-002, LOC-C-002, CITY-C-001/003, SEA-C-003, PFML-C-001/002/005, NH-C-003/005, UI-C-001/011, WC-C-001/002/003), `us_fed_annual.py` (F944-006..009, F943-005..008, F940-007, SCHH-004), `us_fed_info.py` (F1042S-004, ACA-006, F941X-003): content, origin (accumulator / master data), rule, format, edge cases; only tagged facts or references to existing rows. |
| 9 | IRS-004 M15 DOL 2026 rates cited to the 2025 row | fixed | The 2025 list is followed by its own source [US-FEDS6-009]; the potential 2026 CA / VI rates are followed by [US-FEDS5-009]. |
| 10 | W-2 box map positions cited only to US-FEDS5-007 | fixed | `us_w2.py`: W2-004, the Field Options box-map rows with a record position, every RW / RO "W-2 box" mention and the Report Matrix cite both [US-FEDS5-007] (box text) and [US-FEDS5-032] (EFW2 positions). |
| 11 | MA PFML wording vs SCOPE | fixed | `us_gaps.py` RSPEC-GAP-019 subject: "Massachusetts PFML: contribution to DFML; the return channel and mechanics are not configured in this release" (no channel named). |
| 12 | DOR-002 Population Rules RS-017..RS-025 | fixed | New block "CONDITIONAL FIELD RULES (State-defined RS fields)": RS-017 to RS-023 and RS-025, logic and edge cases (more than 100 characters each). |

### Agent 2 changes rendered
- Re-pointed / narrowed values are rendered from the facts (the 37 keys of findings 1-4). Hardcoded text was adjusted where it repeated a removed clause: SC State numeric code 45 removed from the DOR-002 Field Options list (agent 2: not on US-SCS5-016); WC-C-002 Washington share now reads "the worker share defined in row WC-C-001" (the fact is narrowed to one-half of medical aid; the Stay-at-Work / Supplemental Pension share moved to unresolved).
- Numbers moved to unresolved are not written: `rspec.in.wh_return.thresholds` (IN 83.33 / 1,000, 30 / 20 days) and `wa.wc.employee_deduction.saw_supplemental_pension` (0 hits of 83.33 or Stay-at-Work in the 20 workbooks).
- `rspec.fed.form1042s.wage_codes` and `rspec.wv.local.service_fee_returns` (no brackets now) are tagged with `tagr()`; `quote()` is no longer used (quoted_untaggable 0).
- `sir.mo.new_hire.days` now cites US-MOS5-001; the SD / TN / WA / HI "no return" facts cite their new rows.

### Checks (final build)
| Check | Result |
|---|---|
| Pre-flight `validate_workbook.py --artifact RSPEC` ×20 | PASS 20/20, 0 findings |
| C12 | PASS (20 of 21 columns on every core sheet; 0 blank M; 0 cells beyond the header) |
| C29 / pipeline wording | PASS 0 / 0 |
| C30 | PASS 0 |
| C42 / C43 | PASS 0 hits / PASS package 1.0 |
| C44 shared / crosswalk | SKIP (filing ids are descriptions) / PASS 20/20 |
| C46 period-aware (`spec_lint.py`) | PASS: 1,490 tags, 590 keys, 0 mismatches, 0 missing keys, unbound 4 (NC URL G.S. 110-129.2 only), DERIVED 31 (integers only), quoted 0, unused RSPEC facts 0 |
| C46 shared, specs only | FAIL (checker limitation, unchanged): 26 one-value-per-key (OASDI 2026/2027 ×14, NJ base week ×4, NM WC fees ×8); 59 unbound = integer layout positions / codes and the NC URL |
| C56 / C70 | PASS 934 fields, 0 problems / PASS 0 unregistered |
| C34 / C35 / C36 | SKIP under `validation_exemptions` (narrowing of the C35 reason is still open for the scaffolder, per agent 2) |
| C71 | PASS 20 files, 0 differences |
| Excel open (`open_check.ps1`) | PASS 20, 0 not clean |
| validate_contract --all | PASS 84 files |

### Regression guard (cell diff vs `_backup/RSPEC-pre-r2-rebuild-2026-11-03/specs`; `_build/checks/regression_vs_r1.json`)
No fact key and no gap id was removed from any workbook.
| Workbook | Cells | Explained by |
|---|---|---|
| DOR-001 | 40 | agent 2 re-pointed / narrowed State facts (Report Matrix 26, State rows, scope 1); finding 6 (DOR-C-005, 007) |
| DOR-002 | 166 | finding 12 block inserted (Population Rules rows shift: 103); SC code 45 row removed (Field Options shift: 17); agent 2 values (Report Matrix 31); RS-024 explanation |
| DOR-003 / DOR-004 / IRS-005 / IRS-007 / IRS-008 | 2 / 1 / 1 / 1 / 1 | finding 6 |
| IRS-001 | 0 | |
| IRS-002 | 4 | finding 6 (F944-006..009; +1 key `fed.fica.addl_medicare.withholding_threshold`) |
| IRS-003 | 13 | finding 5 (B/M of lines 3, 5, 7 and File Structure; +5 keys) and finding 6 (F943-005..008) |
| IRS-004 | 3 | findings 5 (K15), 6 (F940-007), 9 (M15) |
| IRS-006 | 3 | wage_codes now tagged; finding 6 (F1042S-004) |
| LOC-001 | 3 | WV service-fee returns now tagged; finding 6 (LOC-C-002) |
| LOC-002 / LOC-003 | 2 / 4 | finding 6; Seattle base / thresholds fact narrowed (SHT clause removed) |
| PFML-001 | 8 | finding 6 (PFML-C-001/002/005); finding 11 (M24, T24); HI TDI re-point |
| SDNH-001 | 6 | finding 6 (NH-C-003/005); MO 20 days re-pointed to US-MOS5-001 |
| SSA-001 | 38 | finding 10 (box citations on RW / RO rows, Field Options, W2-004, Report Matrix); EFW2C fact row |
| UI-001 | 26 | agent 2 values (AK, AZ, FL, TN, multistate recipient: Report Matrix 14, State rows); finding 6 (UI-C-001, 011) |
| WC-001 | 9 | finding 6 (WC-C-001..003); WA L&I fact narrowed and re-pointed to US-WAS7-001 |

### Open items
Unchanged from round 1 (RQ-08, RQ-11, RQ-12, RQ-15 now in gaps.json, GAP-001/002 and the 41 other recorded limitations). New: none. Observation: a rough sentence count still finds 37 core-sheet M cells written as one tagged rule (e.g. ACA line rules, W2-R01..R05, LOC-C-003). They were not in finding 6's list and were left unchanged.

### Delivered files (md5)
```
d279c99d80f5f3378872e1ce0ee85aab *04-reports-spec/US-DOR-001-StateWithholdingReturns-Spec.xlsx
c77a3d8220891cf3f0727b72aa3a7f9a *04-reports-spec/US-DOR-002-StateAnnualReconciliationW2-Spec.xlsx
ab3907a553b6421350c1442e0930e319 *04-reports-spec/US-DOR-003-NevadaMBT-Spec.xlsx
b7e6e158d73e8894a484228d9fc47afa *04-reports-spec/US-DOR-004-PayrollTransitLevies-Spec.xlsx
41498a58e6447e74e83f19bc3bc9944f *04-reports-spec/US-IRS-001-Form941-Spec.xlsx
009284356237d90efc04b860353a27c7 *04-reports-spec/US-IRS-002-Form944-Spec.xlsx
7200047b4dae427dbaf66c5d0e577e7a *04-reports-spec/US-IRS-003-Form943-Spec.xlsx
1c448d5573a8e9a69ea631d238ee76ef *04-reports-spec/US-IRS-004-Form940-Spec.xlsx
21cfd756513c03c638218f51b0e291a8 *04-reports-spec/US-IRS-005-ScheduleHRouting-Spec.xlsx
591314a5db2ad55b4631e8b995956035 *04-reports-spec/US-IRS-006-Form1042S-Spec.xlsx
895c93c6c03bc441b7f52790bca076ce *04-reports-spec/US-IRS-007-Forms1094C1095C-Spec.xlsx
e6543590828855eb09a8fe97efc3269c *04-reports-spec/US-IRS-008-Form941X-Spec.xlsx
790f050ab7f75f90550984410b9e10fd *04-reports-spec/US-LOC-001-LocalIncomeWageTaxReturns-Spec.xlsx
866e599fc0c6b75a181deb163871e00c *04-reports-spec/US-LOC-002-CityEmployerPayrollTaxes-Spec.xlsx
46e874d0532b8a14e03fcee65e517b40 *04-reports-spec/US-LOC-003-SeattlePETSocialHousing-Spec.xlsx
b6558cead6e87f57881af10b132e02c0 *04-reports-spec/US-PFML-001-PFMLProgrammeReports-Spec.xlsx
5b85b29e9e77c27f20dd8275e08a4b4a *04-reports-spec/US-SDNH-001-NewHireReport-Spec.xlsx
1466aed102228f8eeec6a874b977e321 *04-reports-spec/US-SSA-001-FormW2W3-Spec.xlsx
e0c60db36451db922f3e85e22be28e10 *04-reports-spec/US-UI-001-StateUIWageReports-Spec.xlsx
4b8d89529d1ec3b65a4fd04e11404a37 *04-reports-spec/US-WC-001-StateFundWorkersComp-Spec.xlsx
86f0b18b90736219eaf62e8c429830b4 *_research/RSPEC-research-request.json (unchanged)
c7ff4161e2edc30bc8b987f6b5d04fc1 *_pipeline/RSPEC-bindings.csv
```
