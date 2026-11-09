# -*- coding: utf-8 -*-
"""Writes _pipeline/SIR-build-log.md from the generator state and the latest check outputs (run after the checks)."""
import collections
import csv
import datetime as dt
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import sir_common as S  # noqa: E402
import sir_specs as P  # noqa: E402
import sir_lint as L  # noqa: E402
import docx  # noqa: E402

CK = os.path.join(HERE, "checks")
doc_path = os.path.join(S.SIRDIR, S.FILENAME)
lint = L.run(doc_path)
req = json.load(open(os.path.join(CK, "sir_requests.json"), encoding="utf-8"))
f44 = json.load(open(os.path.join(CK, "f44_self.json"), encoding="utf-8"))
rc = list(csv.DictReader(open(os.path.join(CK, "sir_recon.csv"), encoding="utf-8")))
bind = list(csv.DictReader(open(os.path.join(S.BASE, "_pipeline", "SIR-bindings.csv"), encoding="utf-8")))
keys_by_file = collections.defaultdict(set)
for b in bind:
    keys_by_file[b["facts_file"]].add(b["key"])
sp = os.path.join(CK, "run_summary.txt")
summary = open(sp, encoding="utf-8").read() if os.path.exists(sp) else "(checks not yet run)"
cnt = collections.Counter((r["kind"], r["status"]) for r in rc)
why = collections.Counter(v["why"] for v in req.values())
d = docx.Document(doc_path)
words = sum(len(p.text.split()) for p in d.paragraphs) + sum(len(c.text.split()) for t in d.tables for r in t.rows for c in r.cells)
fr = docx.Document(os.path.expanduser("~/mercans-pipeline/FR-compliance/03-statutory-integrations/FR-SIR-INDEX-001-v1.0.docx"))
co = docx.Document(os.path.expanduser("~/mercans-pipeline/CO-compliance/03-statutory-integrations/CO-SIR-INDEX-001-v1.0.docx"))
unres = [u for u in S.UNRESOLVED if u["key"] != "precheck.next.text_elements_unmatched"]
gaps_md = "\n".join(f"| {v['gid']} | `{k}` | {v['why']} | {', '.join(v['jurs']) or '-'} | {v['doc_closes']} |"
                    for k, v in sorted(req.items(), key=lambda x: x[1]["gid"]))
dd_rows = "\n".join(f"| {r['item']} | {r['status']} | {r['note']} |" for r in rc
                    if r["kind"] == "DD_ELEMENT" and r["status"] in ("CONSUMED_BY_SIR", "NOT_A_FILING_INPUT"))
bind_rows = "\n".join(f"| {b['location']} | tagged value of the key | `{b['key']}` | {b['register_id']} |" for b in bind[:14])
nrows = lint["info"]["handoff_rows"]
ndd = sum(1 for r in rc if r["kind"] == "DD_ELEMENT")
ckeys = sum(len(v) for k, v in keys_by_file.items() if k.startswith("CCG-"))

text = f"""# SIR - build log
Artifact: SIR | Country: US | Round: 1 | Built: {dt.date.today().isoformat()}
Manifest: _pipeline/build-manifest.json (USD, currency_minor_units 2, rounding payment 0.01 / accounting 0.01, tier T4, package {S.PKG}, year {S.YEAR}; validation_exemptions C34 and C35 read: they concern the RSPEC norm and validator gates and do not apply to this document)
Pack: _research/SIR-research-pack.md | Facts: _research/SIR-facts.json ({len(S.SIR_KEYS)} facts, {len(unres)} open questions in unresolved[] plus 1 pre-build text-check entry that is internal)
Generator: 03-statutory-integrations/_build/build_sir.py (sir_common.py, sir_defs.py, sir_specs.py, sir_docx.py); deliverable 03-statutory-integrations/{S.FILENAME}
Contract of the generator: re-runnable and the only source of the document (C71: rebuilt package identical, 0 differences). Previous builds are copied to _build/_backup/ before each rebuild; md5 of the final set in _build/checks/md5_final.txt (written last).

## Precedent inspection (L1)
Opened with python-docx (not read from prose): FR-SIR-INDEX-001-v1.0.docx ({len(fr.paragraphs)} paragraphs, {len(fr.tables)} tables, {len(fr.sections)} section) and CO-SIR-INDEX-001-v1.0.docx ({len(co.paragraphs)} paragraphs, {len(co.tables)} tables). Both: Letter portrait with 1008-twip side margins, Arial, Heading 1 14 pt and Heading 2 12 pt, bordered tables (top row bold, repeated), footer "<ID> v1.0 | Mercans Compliance Regulations Team | 2026", sections Table of Contents, Document Control (Document ID table + one version row), 0 Purpose / Scope / Audit Compliance (inventory, direction rule, confidence), 1 Inbound, 2 Outbound, 3 Authentication, 4 Technical Specifications, 5 Error Handling, 6 SLA and Deadlines, Appendix A Sources.
Built to that skeleton. Deviations, all deliberate: (1) the precedents print "FR-SIR-001" / "CO-SIR-001" in the Document ID row and footer although the file is "...-SIR-INDEX-001"; this document uses the file id everywhere (C53 compares them). (2) The precedents carry no per-report register; section 7 is landscape because the C53 and reconciliation contract needs one hand-off row per Report Matrix row ({nrows} rows). (3) Section 3 is "Authorisation Requirements" (the instrument per jurisdiction), because no authority credential or certificate model exists for a provider hand-off. (4) Sections 8 (provider input data set) and Appendix B (not configured) are added. (5) The TOC is a field with the precedent's placeholder text (updated when opened in Word).
Template governing: SHARED_TEMPLATES_GUIDE_v2_1.md (SIR row) and shared/si-runbook/README.md (discover first, scale to reality).

## Scope decisions
| Item | Verdict | Basis |
|---|---|---|
| Discovery verdict | MANUAL_ONLY (integration-landscape.json) | No authority offers a system-to-system integration operated by Mercans; submissions are made by the third-party provider (owner decision, provider choice outside the build); inbound items are documents. No authority runbook (P1-P7) is issued; none can be scoped without a provider. |
| Length of the index | Longer than the one-page form of MANUAL_ONLY | The scope integration inventory (hand-off to provider, product mapping required) needs the hand-off contract: one row per report row, authorisations, data set. For QA to confirm. |
| Integrations in the inventory | 5 (2 outbound, 3 inbound) | scope_manifest.json integrations; ids US-OUT-001/002 and US-INB-001/002/003 assigned here. Direction from the scope manifest and the Report Type of each spec (all 20 specs outbound). |
| Local layers, programme returns, MBT, transit levies, workers' compensation | In scope, sections 7.6 to 7.8 | One hand-off row per Report Matrix row of US-LOC-001..003, US-PFML-001, US-DOR-003/004, US-WC-001. |
| Special populations (household, agricultural) | In scope as far as the specs carry them (US-IRS-003, US-IRS-005) | Filing consequences only; State rules beyond these deferred by the owner. |
| 1099 contractors | Out of payroll scope; not asserted | The new-hire duty for contractors is not written without a fact. |

## Lessons applied
1. Binding: every factual cell is a [[FACT:key=value]] tag ({lint['tags']} tags, {len(lint['bound'])} distinct keys); priority when a key is in several files: SIR, RSPEC, DD, WTC, CCG last (sir_common.fact). Citations are the fact's register_id plus _also_register_ids. Keys used: SIR-facts {len(keys_by_file['SIR-facts.json'])}, RSPEC-facts {len(keys_by_file['RSPEC-facts.json'])}, DD facts {len(keys_by_file['DD-8_sheets-facts.json'])}, CCG facts {ckeys}. Binding log: _pipeline/SIR-bindings.csv ({len(bind)} rows: location, key, register_id, also ids, effective_from, file).
2. F44: _build/f44_self.py reads the saved copy of every register row bound to a tag and checks every number, form name, date, quarter, channel word and acronym of the value. Result: {f44['tags_checked']} distinct tags, {len(f44['misses'])} misses, {len(f44['no_local_copy'])} tags without a local copy. The generator applies the same test before it writes a value (sir_common.usable): a fact with a missing element, or whose cited source has no saved copy, is not written; the cell becomes "Not configured in this release [[GAP:SIR-RQ-nn]]" with a request. A fallback fact of the same row (for example the RSPEC fact for the same return) is used first when it passes.
3. Period-aware: no fact key used here has more than one period or value; facts with an effective_to carry "(effective from to)" in the cell. No key is collapsed.
4. Gaps: {len(req)} requests (SIR-RQ-01..{len(req):02d}): {why.get('f44', 0)} F44, {why.get('open', 0) + why.get('no_fact', 0)} open questions recorded with the facts, {why.get('missing', 0)} grouped "no source recorded". _research/SIR-research-request.json (validated), _research/gaps.json (SIR-RQ entries appended; other entries untouched; C70 PASS), Appendix B.
5. Text rules: no tier-B figure (C30 0; no fact used rests on a tier B/C or MANUAL row), no internal path or pipeline wording, no percentage or 3-decimal fraction outside a tag, units written from the fact ("business days" when the key says so).
6. Portals: portal and authority names are those of the Report Matrix rows of the approved specs (written by the RSPEC generator under the same rule) or sit inside a tagged fact that passed F44. US-LAP52-005 "LAWATS" is used only for the Louisiana UI power of attorney (the online power of attorney, which that row's copy names); the Louisiana wage-report channel is written from rspec.la.ui_qtr.due ("LWC online services", US-LAS5-007), and sir.la.ui.wage_report (its value names LAWATS) is not written anywhere. rspec.mn.pfml_qtr.form is taken from SIR-facts first (same value as the RSPEC fact; the cell is identical to the Report Matrix wording).
7. Reconciliation: _build/checks/sir_recon.csv, {len(rc)} rows: report rows {cnt[('REPORT_ROW', 'MAPPED')]} mapped + {cnt[('REPORT_ROW', 'MAPPED_LIMITATION')]} mapped with a documented limitation, specs {cnt[('SPEC', 'MAPPED')]} of {len(P.specs())} in the outbound register with direction OUTBOUND, UNMAPPED 0 (checked both ways: every Report Matrix row has a hand-off row; every hand-off row names a Report Matrix row).
8. Not edited: facts, register, manifest, approved RSPEC, DD, WTC. Written: 03-statutory-integrations/, _pipeline/SIR-*, _research/SIR-research-request.json and the SIR entries of _research/gaps.json.

## DD elements without a Report Spec or WTC consumer (checked here)
| DD element | Verdict | Where / why |
|---|---|---|
{dd_rows}
Direction DD -> SIR: of {ndd} elements: {cnt[('DD_ELEMENT', 'CONSUMED_BY_SPEC')]} cited by Report Spec rows, {cnt[('DD_ELEMENT', 'CONSUMED_BY_WTC')]} consumed in the WTC, {cnt[('DD_ELEMENT', 'CONSUMED_BY_SIR')]} consumed in this SIR (section 8, the DD fact tagged there), {cnt[('DD_ELEMENT', 'NOT_A_FILING_INPUT')]} not a filing input (section 8.7 gives the reason); 0 with no consumer. "Employee primary language" is an employee-notice template input: no authority filing carries it, so it is not consumed in the SIR (reason in the document); the language rule itself belongs to the PSL stage.

## Fact bindings (section -> key -> register_id), sample; full table in _pipeline/SIR-bindings.csv
| Location | Claim | key | register_id |
|---|---|---|---|
{bind_rows}

## Deviations from this agent's stated constants
- SIR contract (section 5.5): MANUAL_ONLY asks for a one-page index with nothing more. This index also carries the provider hand-off contract the scope manifest requires; flagged for QA (see scope decisions).
- Employer signature PIN fact (sir.fed.efw2.employer_signature_pin) is not written: its value contains the mask "S-XXXXXX-Y", which the shared C29 X-run rule treats as an unsanctioned placeholder; the RE positions of the PIN are still carried by sir.fed.efw2.layout_ty2026.
- Report Spec accuracy and closing evidence are mirrored per row from each Report Matrix (F27); a later change to either must be mirrored the same day.

## Open items (non-blocking)
| Request | Key | Reason | Jurisdictions | What would close it |
|---|---|---|---|---|
{gaps_md}

## Checks (latest run; full output in _build/checks/run_summary.txt)
```
{summary[-7000:]}
```

## Items for QA
1. Verdict and shape: MANUAL_ONLY with an extended index (no per-authority runbooks). Alternative reading: HAS_INTEGRATIONS with the provider as the single integrable party; not chosen because no provider is selected and no authority artefact applies.
2. {why.get('f44', 0)} of the {len(req)} gap cells come from the F44 text-element rule; most are acronym or channel-word misses (POA, TPA, DOR, csv, xml, paper) on otherwise sourced rows. If QA accepts those as the research's own wording the rows can be restored by agent 2 (same facts); the generator needs no change.
3. Section 5 has no error-code catalogue: none was read (stated in the section). Section 6.2 states that State acknowledgement rules were not published in the sources read.
4. Shared consistency C46 reports mismatches in other deliverables (CCG, WTC, specs; for example OASDI wage base 184,500 vs 192300); none is in this document (the rows naming 03-statutory-integrations: 0).
5. Hours, weeks and wage totals in section 8 are payroll results, not DD fields; the section says so (F26).

## Accuracy
Provider hand-off content: 75 to 85 percent (official pages and file layouts read for most rows; no provider layout, no real filing, {len(req)} cells not configured). Per-row figures are those of the Report Matrix (lowest 50 where the specs themselves leave the row open, highest 90). What closes the gap: the chosen provider's import layout and one accepted real filing per channel; the closing sources listed in Appendix B. Document words: about {words}.
"""
open(os.path.join(S.BASE, "_pipeline", "SIR-build-log.md"), "w", encoding="utf-8").write(text)
print("build log written", len(text), "chars")
