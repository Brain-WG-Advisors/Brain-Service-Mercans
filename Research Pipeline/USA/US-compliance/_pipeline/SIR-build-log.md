# SIR - build log
Artifact: SIR | Country: US | Round: 1 | Built: 2026-11-04
Manifest: _pipeline/build-manifest.json (USD, currency_minor_units 2, rounding payment 0.01 / accounting 0.01, tier T4, package 1.0, year 2026; validation_exemptions C34 and C35 read: they concern the RSPEC norm and validator gates and do not apply to this document)
Pack: _research/SIR-research-pack.md | Facts: _research/SIR-facts.json (299 facts, 23 open questions in unresolved[] plus 1 pre-build text-check entry that is internal)
Generator: 03-statutory-integrations/_build/build_sir.py (sir_common.py, sir_defs.py, sir_specs.py, sir_docx.py); deliverable 03-statutory-integrations/US-SIR-INDEX-001-v1.0.docx
Contract of the generator: re-runnable and the only source of the document (C71: rebuilt package identical, 0 differences). Previous builds are copied to _build/_backup/ before each rebuild; md5 of the final set in _build/checks/md5_final.txt (written last).

## Precedent inspection (L1)
Opened with python-docx (not read from prose): FR-SIR-INDEX-001-v1.0.docx (79 paragraphs, 13 tables, 1 section) and CO-SIR-INDEX-001-v1.0.docx (68 paragraphs, 12 tables). Both: Letter portrait with 1008-twip side margins, Arial, Heading 1 14 pt and Heading 2 12 pt, bordered tables (top row bold, repeated), footer "<ID> v1.0 | Mercans Compliance Regulations Team | 2026", sections Table of Contents, Document Control (Document ID table + one version row), 0 Purpose / Scope / Audit Compliance (inventory, direction rule, confidence), 1 Inbound, 2 Outbound, 3 Authentication, 4 Technical Specifications, 5 Error Handling, 6 SLA and Deadlines, Appendix A Sources.
Built to that skeleton. Deviations, all deliberate: (1) the precedents print "FR-SIR-001" / "CO-SIR-001" in the Document ID row and footer although the file is "...-SIR-INDEX-001"; this document uses the file id everywhere (C53 compares them). (2) The precedents carry no per-report register; section 7 is landscape because the C53 and reconciliation contract needs one hand-off row per Report Matrix row (236 rows). (3) Section 3 is "Authorisation Requirements" (the instrument per jurisdiction), because no authority credential or certificate model exists for a provider hand-off. (4) Sections 8 (provider input data set) and Appendix B (not configured) are added. (5) The TOC is a field with the precedent's placeholder text (updated when opened in Word).
Template governing: SHARED_TEMPLATES_GUIDE_v2_1.md (SIR row) and shared/si-runbook/README.md (discover first, scale to reality).

## Scope decisions
| Item | Verdict | Basis |
|---|---|---|
| Discovery verdict | HAS_INTEGRATIONS (integration-landscape.json, si-discovery schema) | SIR-QA1-01: the single integrable party for Mercans is the third-party filing provider (scope manifest integrations.outbound, owner decision US-MQ-09); authority groups with a machine-channel fact (SFTP, web service, XML or bulk file) are integration=true, operated by the provider; the provider runbook set is deferred (gap request of the provider choice). |
| Shape of the index | Extended index (one row per authority group in section 0.4, plus the hand-off register) | Template for HAS_INTEGRATIONS: index with integration yes/no, channel, direction, developer portal and runbook location per party; per-authority runbooks are not issued because the provider operates every channel. |
| Integrations in the inventory | 5 (2 outbound, 3 inbound) | scope_manifest.json integrations; ids US-OUT-001/002 and US-INB-001/002/003 assigned here. Direction from the scope manifest and the Report Type of each spec (all 20 specs outbound). |
| Local layers, programme returns, MBT, transit levies, workers' compensation | In scope, sections 7.6 to 7.8 | One hand-off row per Report Matrix row of US-LOC-001..003, US-PFML-001, US-DOR-003/004, US-WC-001. |
| Special populations (household, agricultural) | In scope as far as the specs carry them (US-IRS-003, US-IRS-005) | Filing consequences only; State rules beyond these deferred by the owner. |
| 1099 contractors | Out of payroll scope; not asserted | The new-hire duty for contractors is not written without a fact. |

## Lessons applied
1. Binding: every factual cell is a [[FACT:key=value]] tag (480 tags, 409 distinct keys); priority when a key is in several files: SIR, RSPEC, DD, WTC, CCG last (sir_common.fact). Citations are the fact's register_id plus _also_register_ids. Keys used: SIR-facts 274, RSPEC-facts 72, DD facts 52, CCG facts 11. Binding log: _pipeline/SIR-bindings.csv (478 rows: location, key, register_id, also ids, effective_from, file).
2. F44: _build/f44_self.py reads the saved copy of every register row bound to a tag and checks every number, form name, date, quarter, channel word and acronym of the value. Result: 409 distinct tags, 0 misses, 0 tags without a local copy. The generator applies the same test before it writes a value (sir_common.usable): a fact with a missing element, or whose cited source has no saved copy, is not written; the cell becomes "Not configured in this release [[GAP:SIR-RQ-nn]]" with a request. A fallback fact of the same row (for example the RSPEC fact for the same return) is used first when it passes.
3. Period-aware: no fact key used here has more than one period or value; facts with an effective_to carry "(effective from to)" in the cell. No key is collapsed.
4. Gaps: 39 requests (SIR-RQ-01..39): 8 F44, 23 open questions recorded with the facts, 8 grouped "no source recorded". _research/SIR-research-request.json (validated), _research/gaps.json (SIR-RQ entries appended; other entries untouched; C70 PASS), Appendix B.
5. Text rules: no tier-B figure (C30 0; no fact used rests on a tier B/C or MANUAL row), no internal path or pipeline wording, no percentage or 3-decimal fraction outside a tag, units written from the fact ("business days" when the key says so).
6. Portals: portal and authority names are those of the Report Matrix rows of the approved specs (written by the RSPEC generator under the same rule) or sit inside a tagged fact that passed F44. US-LAP52-005 "LAWATS" is used only for the Louisiana UI power of attorney (the online power of attorney, which that row's copy names); the Louisiana wage-report channel is written from rspec.la.ui_qtr.due ("LWC online services", US-LAS5-007), and sir.la.ui.wage_report (its value names LAWATS) is not written anywhere. rspec.mn.pfml_qtr.form is taken from SIR-facts first (same value as the RSPEC fact; the cell is identical to the Report Matrix wording).
7. Reconciliation: _build/checks/sir_recon.csv, 401 rows: report rows 229 mapped + 7 mapped with a documented limitation, specs 20 of 20 in the outbound register with direction OUTBOUND, UNMAPPED 0 (checked both ways: every Report Matrix row has a hand-off row; every hand-off row names a Report Matrix row).
8. Not edited: facts, register, manifest, approved RSPEC, DD, WTC. Written: 03-statutory-integrations/, _pipeline/SIR-*, _research/SIR-research-request.json and the SIR entries of _research/gaps.json.

## DD elements without a Report Spec or WTC consumer (checked here)
| DD element | Verdict | Where / why |
|---|---|---|
| Supplemental wage withholding method election | NOT_A_FILING_INPUT | Input of the federal income tax calculation on supplemental wages (regulation design); no authority filing or integration carries it; DD fact fed.fit.supplemental.aggregate_method |
| State-assigned unemployment insurance rate | CONSUMED_BY_SIR | Loaded as configuration data from the annual State UI rate notice (US-INB-003, section 1.2) |
| Alaska occupational code | CONSUMED_BY_SIR | Alaska UI wage report; DD fact dd.ak.ui.occupation_code |
| Employer health insurance offered | CONSUMED_BY_SIR | Maryland new-hire report; DD fact dd.md.new_hire.wage_health |
| Oregon transit district of work | CONSUMED_BY_SIR | Form OQ; DD fact dd.or.transit_district |
| Iowa school district of residence | NOT_A_FILING_INPUT | Individual assessment (school district surtax at filing), not an employer filing carried by a provider; DD fact dd.ia.school_district_residence |
| Employee primary language | NOT_A_FILING_INPUT | Employee notice template input; no authority filing or integration carries it; DD fact dd.ny.employee_primary_language |
| NAICS industry code (Maryland wage file) | CONSUMED_BY_SIR | Maryland MW508 record; DD fact dd.md.naics |
Direction DD -> SIR: of 145 elements: 112 cited by Report Spec rows, 25 consumed in the WTC, 5 consumed in this SIR (section 8, the DD fact tagged there), 3 not a filing input (section 8.7 gives the reason); 0 with no consumer. "Employee primary language" is an employee-notice template input: no authority filing carries it, so it is not consumed in the SIR (reason in the document); the language rule itself belongs to the PSL stage.

## Fact bindings (section -> key -> register_id), sample; full table in _pipeline/SIR-bindings.csv
| Location | Claim | key | register_id |
|---|---|---|---|
| 8.3 Geographic code, Alaska | tagged value of the key | `dd.ak.ui.geographic_code` | US-AKS5-014 |
| 8.3 Occupational code, Alaska | tagged value of the key | `dd.ak.ui.occupation_code` | US-AKS5-014 |
| 8.4 Denver occupational privilege tax location | tagged value of the key | `dd.co.denver_opt` | US-COP52-001 |
| 8.6 Connecticut Paid Leave employee-level data | tagged value of the key | `dd.ct.pfml.employee_level_data` | US-CTB5-001 |
| 8.6 Delaware Paid Leave hours and wages | tagged value of the key | `dd.de.paid_leave.hours` | US-DES5-013 |
| 8.1 New York MCTMT payroll zone | tagged value of the key | `dd.employer.ny_mctmt_zone` | US-NY-003 |
| 8.1 State withholding, UI and paid-leave account identifiers per State | tagged value of the key | `dd.employer.state_account_ids` | US-UTR3-001 |
| 8.1 Federal depositor status | tagged value of the key | `dd.fed.depositor_status.codes` | US-FEDS5-004 |
| 8.2 Date services first performed | tagged value of the key | `dd.fed.new_hire.date_first_services` | US-FEDS5-024 |
| 8.3 Treasury Tipped Occupation Code | tagged value of the key | `dd.fed.w2.tipped_occupation_code` | US-FEDS5-007 |
| 8.1 E-Verify certification, Florida | tagged value of the key | `dd.fl.everify_certified` | US-FLS5-010 |
| 8.2 SSN, not an ITIN, Florida | tagged value of the key | `dd.fl.ssn_not_itin` | US-FLS5-024 |
| 8.5 Employee fields, Georgia | tagged value of the key | `dd.ga.new_hire.extra` | US-GAS5-012 |
| 8.5 Dependent health coverage, Iowa | tagged value of the key | `dd.ia.new_hire.health` | US-IAS5-012 |

## Deviations from this agent's stated constants
- Verdict HAS_INTEGRATIONS with the provider as the single integrable party (QA SIR r1, SIR-QA1-01); the 'one-page form' deviation of round 0 is withdrawn. No per-authority P1-P7 runbook folder is issued (provider deferred).
- Employer signature PIN (sir.fed.efw2.employer_signature_pin) is written in section 8.1; sir_lint no longer treats an X-run inside a FACT tag as a C29 hit (QA DD r2 ruling C29_X_run_masks; SIR-QA1-06).
- Report Spec accuracy and closing evidence are mirrored per row from each Report Matrix (F27); a later change to either must be mirrored the same day.

## Open items (non-blocking)
| Request | Key | Reason | Jurisdictions | What would close it |
|---|---|---|---|---|
| SIR-RQ-01 | `dd.ct.ui.occupation_hours_zip` | f44 | - | The authority page or form that carries the wording, saved and read |
| SIR-RQ-02 | `fed.aca.efile_threshold.ty2026` | open | - | IRS publication of the final 2026 Instructions for Forms 1094-C and 1095-C |
| SIR-RQ-03 | `rspec.fed.form940.due.ty2026` | open | - | IRS publication of the final 2026 Instructions for Form 940 (expected December 2026) |
| SIR-RQ-04 | `sir.ca.de9c.file_spec` | open | - | EDD DE 8300 annexes / FSET schema download |
| SIR-RQ-05 | `sir.fl.agent_authorization` | f44 | FL | The authority page or form that carries the wording, saved and read |
| SIR-RQ-06 | `sir.fl.agent_authorization.rts9` | open | - | the Florida Department of Revenue page or form that names the reemployment-tax agent registration (RTS-9) - floridarevenue.com Forms library |
| SIR-RQ-07 | `sir.fl.ui.xml` | f44 | - | The authority page or form that carries the wording, saved and read |
| SIR-RQ-08 | `sir.in.w2.xml_schema` | open | - | Indiana DOR XML schema archive, extracted and inspected |
| SIR-RQ-09 | `sir.ks.live_kw100_page` | open | - | a live copy of kw100.html and KW-2CSV from a network that reaches ksrevenue.gov |
| SIR-RQ-10 | `sir.ky.agent_authorization` | open | KY | Kentucky DOR Form 20A100 and the KUIP TPA/agent authorization page |
| SIR-RQ-11 | `sir.la.withholding.agent_authorization` | open | LA | Louisiana LDR Form R-7006 current edition read on revenue.louisiana.gov |
| SIR-RQ-12 | `sir.ma.agent_authorization` | f44 | MA | The authority page or form that carries the wording, saved and read |
| SIR-RQ-13 | `sir.ma.agent_authorization.m2848` | open | - | a saved copy of the mass.gov POA / third-party authorization page (browser save by an owner with access) or Form M-2848 PDF |
| SIR-RQ-14 | `sir.me.withholding.agent_authorization` | open | ME | Current Maine Revenue Services Form 2848-ME and Maine DOL UC-28 read on maine.gov |
| SIR-RQ-15 | `sir.mi.new_hire.statute` | open | - | MCL 400.231 et seq. text on legislature.mi.gov |
| SIR-RQ-16 | `sir.ms.ui.agent_authorization` | f44 | MS | The authority page or form that carries the wording, saved and read |
| SIR-RQ-17 | `sir.ms.ui.agent_authorization.j9` | open | - | an OCR text of the J-9 PDF or the MDES downloadable-forms page text naming Form J-9 (mdes.ms.gov downloadable forms) |
| SIR-RQ-18 | `sir.ms.withholding.agent_authorization` | open | MS | Mississippi DOR Form 21-002 PDF read on dor.ms.gov |
| SIR-RQ-19 | `sir.ne.agent_authorization` | f44 | NE | The authority page or form that carries the wording, saved and read |
| SIR-RQ-20 | `sir.ne.agent_authorization.form33` | open | - | the Nebraska Department of Revenue Form 33 (power of attorney) PDF and the NDOL UI representative form page |
| SIR-RQ-21 | `sir.nh.ui.tpa_registration` | open | - | the current NHES page or form naming how a third-party administrator registers for NHUIS (nhes.nh.gov employer pages) |
| SIR-RQ-22 | `sir.ny.withholding.agent_authorization` | open | NY | Form POA-1 from tax.ny.gov/poa read on the official host |
| SIR-RQ-23 | `sir.oh.local.municipal` | f44 | OH | The authority page or form that carries the wording, saved and read |
| SIR-RQ-24 | `sir.oh.local.municipal.thresholds` | open | - | the Ohio Revised Code 718.04 / Ohio Department of Taxation municipal withholding page stating the thresholds |
| SIR-RQ-25 | `sir.oh.ui.agent_authorization` | f44 | OH | The authority page or form that carries the wording, saved and read |
| SIR-RQ-26 | `sir.oh.ui.agent_authorization.jfs20106` | open | - | the JFS-20106 PDF itself or a browser-rendered copy of the ODJFS tax forms page |
| SIR-RQ-27 | `sir.provider.selection` | no_fact | - | Owner/BAU RFP to candidate providers (6 questions: external file/API, IRS reporting agent, state POAs 50+DC, deposit account, local returns, SLA/penalty liability); provider-specific input spec the... |
| SIR-RQ-28 | `sir.state.ui.agent_authorization.missing` | missing | AR, MD, ME, MT, ND, RI | The authority's own page or form for each jurisdiction named, read on the official host |
| SIR-RQ-29 | `sir.state.us_pfml_001.programme.missing` | missing | DC, MA, MD | The authority's own page or form for each jurisdiction named, read on the official host |
| SIR-RQ-30 | `sir.state.us_sdnh_001.new_hire.missing` | missing | CO | The authority's own page or form for each jurisdiction named, read on the official host |
| SIR-RQ-31 | `sir.state.us_ui_001.quarterly.missing` | missing | CO, OH | The authority's own page or form for each jurisdiction named, read on the official host |
| SIR-RQ-32 | `sir.state.us_wc_001.report.missing` | missing | WA | The authority's own page or form for each jurisdiction named, read on the official host |
| SIR-RQ-33 | `sir.state.wh.agent_authorization.missing` | missing | AL, DE, MO, NC | The authority's own page or form for each jurisdiction named, read on the official host |
| SIR-RQ-34 | `sir.tx.ui.due_date` | open | - | TWC rule 815.107 text (40 TAC 815) read on the official host |
| SIR-RQ-35 | `sir.ui.file_specs_missing` | open | - | One official spec per state, downloaded and inspected; parallel lookups |
| SIR-RQ-36 | `sir.w2.state_specs_ty2026` | open | - | Re-check each state W-2 spec page in January 2027 before the first TY2026 file |
| SIR-RQ-37 | `sir.wy.ui.agent_authorization_form_text` | open | WY | WY DWS POA PDF downloaded by the user |
| SIR-RQ-38 | `sir.error_handling.catalogue.missing` | missing | - | The authority reject / business-rule lists per channel class, or an owner decision that error handling belongs to the provider contract (US-MQ-09) |
| SIR-RQ-39 | `sir.state.ack_response_times.missing` | missing | - | The State authority pages that state acknowledgement and response times, saved and read |

## Checks (latest run; full output in _build/checks/run_summary.txt)
```
## build (identical rebuild below) (exit 0)
written C:\Users\instituto\Documents\brain-service\Research Pipeline\USA\US-compliance\03-statutory-integrations\US-SIR-INDEX-001-v1.0.docx

## C12 / C29 / WORD+PATH / FRAC+PCT+UNIT / C30 / C46 period-aware / GAP (sir_lint) (exit 0)
{
 "C29": 0,
 "WORD": 0,
 "mismatch": 0,
 "missing_key": 0,
 "unbound": 0,
 "C30": 0,
 "FRAC": 0,
 "PCT": 0,
 "UNIT": 0,
 "tags": 480,
 "C12": 0,
 "GAP": 0,
 "info": {
  "tables": 31,
  "paragraphs": 126,
  "handoff_rows": 236,
  "spec_rows": 236,
  "sections": 3,
  "tags": 480,
  "gap_ids": 39
 }
}

## F44 self-check (exit 0)
F44 self-check: 409 distinct tags, 0 misses, 0 tags without a local copy

## SIR x RSPEC x DD reconciliation (exit 0)
recon rows 401 {('REPORT_ROW', 'MAPPED'): 229, ('REPORT_ROW', 'MAPPED_LIMITATION'): 7, ('SPEC', 'MAPPED'): 20, ('DD_ELEMENT', 'CONSUMED_BY_SPEC'): 112, ('DD_ELEMENT', 'NOT_A_FILING_INPUT'): 3, ('DD_ELEMENT', 'CONSUMED_BY_SIR'): 5, ('DD_ELEMENT', 'CONSUMED_BY_WTC'): 25}
UNMAPPED 0; DD elements with no consumer 0

## C71 identical rebuild (exit 0)
C71: 0 differences

## shared consistency C42 / C43 / C46 (whole package; rows naming 03-statutory-integrations below) (exit 1)
C42: PASS  {'hits': 0}
C43: PASS  {'package_version': '1.0', 'problems': 0}
C46: FAIL  {'facts': 5305, 'tags': 12224, 'mismatches': 537, 'unbound': 235, 'binding': 0.9811, 'problems': ['537 tag(s) disagree with the facts', '235 fact value(s) written without a tag (binding 98.1%, minimum 100%)']}
      {'file': '01-ccg\\US-CCG-001-v1.0.docx', 'where': 'para 70', 'key': 'fed.fit.extra_pay_period.rule', 'why': "artifact 'No IRS rule adjusts withholding for a 27th biweekly or 53rd weekly payday: Pub. 15-T Worksheet 1A annualises e"}
      {'file': '01-ccg\\US-CCG-001-v1.0.docx', 'where': 'para 73', 'key': 'fed.fica.oasdi.wage_base', 'why': "artifact '184,500' vs facts 192300"}
      {'file': '01-ccg\\US-CCG-001-v1.0.docx', 'where': 'para 163', 'key': 'fed.fica.oasdi.wage_base', 'why': "artifact '184,500' vs facts 192300"}
      {'file': '01-ccg\\US-CCG-001-v1.0.docx', 'where': 'para 288', 'key': 'nm.wc.admin_fee.employer.quarterly', 'why': "artifact '2.55' vs facts 2.68"}
      {'file': '01-ccg\\US-CCG-001-v1.0.docx', 'where': 'para 288', 'key': 'nm.wc.admin_fee.employee.quarterly', 'why': "artifact '2.25' vs facts 2.38"}
      {'file': '01-ccg\\US-CCG-001-v1.0.docx', 'where': 'para 320', 'key': 'fed.fica.oasdi.wage_base', 'why': "artifact '184,500' vs facts 192300"}
      {'file': '01-ccg\\US-CCG-001-v1.0.docx', 'where': 'para 603', 'key': 'fed.fica.oasdi.wage_base', 'why': "artifact '184,500' vs facts 192300"}
      {'file': '01-ccg\\US-CCG-001-v1.0.docx', 'where': 'para 687', 'key': 'fed.fica.oasdi.wage_base', 'why': "artifact '184,500' vs facts 192300"}
      {'file': '01-ccg\\US-CCG-001-v1.0.docx', 'where': 'para 763', 'key': 'wa.pfml.total.rate', 'why': "artifact '1.13' vs facts 1.2"}
      {'file': '01-ccg\\US-CCG-001-v1.0.docx', 'where': 'para 798', 'key': 'pa.local.philadelphia.resident.rate', 'why': "artifact '3.735' vs facts 3.74"}

## shared C46, SIR document only (exit 0)
C46 (SIR only): PASS {'facts': 5305, 'tags': 480, 'mismatches': 0, 'unbound': 0, 'binding': 1.0}

## shared content C53 / C70 (exit 0)
C53: PASS  {'sir': '03-statutory-integrations\\US-SIR-INDEX-001-v1.0.docx', 'specs': 20, 'problems': 0}
C70: PASS  {'citations_checked': 7, 'not_in_register': 0, 'repealed_cited': 0, 'gap_problems': 0}

## validate_contract --all (exit 0)
ok    C:\Users\instituto\Documents\brain-service\Research Pipeline\USA\US-compliance\_qa\WTC-review-r2.json   [review.schema.json]
ok    C:\Users\instituto\Documents\brain-service\Research Pipeline\USA\US-compliance\_qa\WTC-review-r3.json   [review.schema.json]
PASS  (115 files)

## Word open check (exit 0)


OPEN CHECK: 1 file(s), 0 not clean

```

## Items for QA
1. Verdict and shape: HAS_INTEGRATIONS (QA SIR r1 ruling applied). Provider runbook deferred: request id printed in section 0.4.
2. 8 of the 39 gap cells come from the F44 text-element rule; most are acronym or channel-word misses (POA, TPA, DOR, csv, xml, paper) on otherwise sourced rows. If QA accepts those as the research's own wording the rows can be restored by agent 2 (same facts); the generator needs no change.
3. Section 5 error-code catalogue and section 6.2 acknowledgement rules are named gaps with request numbers (SIR-QA1-07), not negative claims.
4. Shared consistency C46 reports mismatches in other deliverables (CCG, WTC, specs; for example OASDI wage base 184,500 vs 192300); none is in this document (the rows naming 03-statutory-integrations: 0).
5. Hours, weeks and wage totals in section 8 are payroll results, not DD fields; the section says so (F26).

## Round 2 (QA SIR r2 batch, one pass; copies in _pipeline/_backup/pre-sir-r2-2026-11-04/)
| Item | Change | Result |
|---|---|---|
| SIR-QA2-01 | f44_textcache.refresh() runs before every F44 use (register or local file newer than the cache, or a bound row missing, is re-read; assertion on missing entries). f44_lib: a State code is proven by a cited row of that State (id prefix), the State name, or the code in a list of codes; "<word> ID" is an identifier, not Idaho; NOT/ONLY/MUST/ALL/ANY/NEW/MAY are not acronyms; an acronym expansion by initials counts only inside one page of at most 40,000 characters | F44 gaps 16 before the page-bounded initials rule, 8 after (each is a real miss: form id or word not in the copy); the MD row is sourced again; recon exit 0 |
| SIR-QA2-02 | CCG rebuilt (rebuild_all.py, copy kept; every changed line is fact-bound text or a Sources renumbering) and WTC rebuilt (D370) | package C46: only multi-period hits remain |
| SIR-QA2-03 | DD generator prints _also_register_ids after the tag (dd_common.src) | W33, W37, W57 and 19 other cells that carry facts with _also ids |
| SIR-QA2-04 | RSPEC IRS-004 M10: rspec.fed.form940.due tag removed | M5, B11, F27, C10 keep it |
| SIR-QA2-05 | TY2025 label and request number on every cell of fed.aca.efile_threshold / rspec.fed.form940.due (sir_common.render); RSPEC IRS-007 M8, H27, File Structure A4 carry the label and the RSPEC gap id | done |
| SIR-QA2-06 | plain-language subjects for the 10 new open questions (OPEN_LABEL) | P36-P45 and Appendix B readable |
| Status | Version Control / Version history status "For QA" while the manifest issue date is a placeholder (SIR, RSPEC, DD, WTC, CCG); release sets "Issued" | done |

## Known limitation of the shared checker (not fixed here; shared/ is read-only for the SIR build)
shared consistency_checks.py c46() builds its facts lookup as one value per key (last entry wins), so every tag of a key that has two period entries is compared with the last one. Example: fed.fica.oasdi.wage_base is 184,500 (2026-01-01..2026-12-31, US-FEDS5-005) and 192,300 (2027-01-01..2027-12-31, US-FEDB5-401); tags in 2026 contexts are reported as mismatches against 192300. QA evidence: SIR-QA1-19 in _qa/SIR-review-r1.json (147 of the 150 package-wide mismatches equal another period entry of the same key). This document uses c46_sir.py / sir_lint (period-aware) for its own verdict; the package-wide C46 stays FAIL until the owner of shared/ makes c46() period-aware.

## Accuracy
Provider hand-off content: 75 to 85 percent (official pages and file layouts read for most rows; no provider layout, no real filing, 39 cells not configured). Per-row figures are those of the Report Matrix (lowest 50 where the specs themselves leave the row open, highest 90). What closes the gap: the chosen provider's import layout and one accepted real filing per channel; the closing sources listed in Appendix B. Document words: about 23948.
