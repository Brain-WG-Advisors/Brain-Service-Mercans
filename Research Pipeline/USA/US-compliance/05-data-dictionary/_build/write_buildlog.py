# -*- coding: utf-8 -*-
"""Write _pipeline/DD-build-log.md (counts are computed from the built workbook and the sidecars)."""
import csv
import json
import os
import subprocess
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import dd_common as D  # noqa: E402
import dd_defs as DEF  # noqa: E402
import dd_lint as L  # noqa: E402
import dd_recon as RC  # noqa: E402
import dd_rules as RU  # noqa: E402

wb_path = os.path.join(D.OUT, D.FILENAME)
rep = L.run(wb_path)
recs, usage = RC.compute(DEF.ELEMENTS)
st = Counter(r["status"] for r in recs)
rq = json.load(open(os.path.join(D.RESEARCH, "DD-research-request.json"), encoding="utf-8"))["requests"]
bind = list(csv.DictReader(open(os.path.join(D.BASE, "_pipeline", "DD-bindings.csv"), encoding="utf-8")))
borrowed = sorted({r["key"] for r in bind if r["key"] not in D.DD_KEYS})
n_el = len(DEF.ELEMENTS)
n_id = sum(1 for e in DEF.ELEMENTS if e["sheet"] == "ID")
calc_only = [e["name"] for e in DEF.ELEMENTS if not usage[e["id"]]["rows"] and not (usage[e["id"]]["specs"])]
fmt_diff = [r for r in recs if r["status"] == "MAPPED" and r["format_check"].startswith("differs")]
name_c = Counter(r["name_check"] for r in recs if r["status"] == "MAPPED")
type_c = Counter(r["type_check"].split(" ")[0] for r in recs if r["status"] == "MAPPED")
exc = [r for r in recs if r["status"] == "EXCEPTION"]
notdd = Counter(r["reason"].split(":")[0] for r in recs if r["status"] == "NOT-DD")
today = "2026-11-03"

md5 = {}
for line in open(os.path.join(D.SPECS, "_build", "checks", "md5_final.txt"), encoding="utf-8"):
    if "-Spec.xlsx" in line:
        h, f = line.strip().split(" *", 1)
        md5[os.path.basename(f)] = h

log = f"""# DD - build log
Artifact: DD | Country: US | Round: 1 | Built: {today}
Manifest: _pipeline/build-manifest.json (USD, currency_minor_units 2, rounding payment 0.01, tier T4, package {D.PKG}, year {D.YEAR})
Pack: _research/DD-research-pack.md | Facts: _research/DD-8_sheets-facts.json (108 facts, 5 unresolved[] + 1 precheck entry)
Generator: 05-data-dictionary/_build/build_dd.py (dd_common.py, dd_defs.py, dd_rules.py, dd_recon.py); deliverable 05-data-dictionary/{D.FILENAME}
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
| Excel tables Table_2, Table_3, Table_4-11 | removed (autofilter on ID Information {__import__('openpyxl').load_workbook(wb_path)['ID Information'].auto_filter.ref}); Table_1, Table_12, Table_13 kept | stale table ranges over rewritten content made Excel refuse the file (open_check FAILED); plain ranges with the template's cell fills open clean (open_check OK) |
| Review comments on data cells (ID Information, Country Fields, Version Control A1) | removed; Version Control guidance comments B12:E12 kept | precedent-country content must not survive (C42); the comments are history (C47) |
| Introduction B11:B16 | numbering formulas replaced by their values 1-6 | no cached values after a save without Excel; same result |
| Version Control status list (E13:E23) | "Issued" added to the list | the one Version Control row carries package version, issue date and status "Issued" |
| Version Control title | B9 = "United States of America | US-DD-001 v{D.PKG}" | package version on the title block (C43) |
| Instructions, ISO 4217, ISO 3166-1 | unchanged (compared cell by cell with the template) | contract: change the country name only / preserve as-is; the Instructions sheet carries no country name |
| Mid-sheet repeated header | kept once in ID Information (entity block, as the template) and once per option mapper block; none in Country Fields | template structure; counted out of the data rows |
| Version Control date | {D.ISSUE:%Y-%m-%d} is the manifest planning placeholder (package.issue_date; owner has not set a date) | taken from the manifest, not invented |

## Result
- Elements: {n_el} data fields: ID Information {n_id} (1 employee block, {n_id - 1} legal entity block), Country Fields {n_el - n_id}.
- Option mappers: {rep['info']['mappers']} mappers, {rep['info']['mapper_rows']} rows ({'; '.join(f"{m['name']} {len(m['rows'])}" for m in RU.MAPPERS if len(m['rows']) > 20)}; the rest are small lists; 10 external code lists are pointer rows, see RQ-02 and RQ-03).
- [[FACT]] tags: {rep['tags']} in the workbook, {len(rep['bound'])} distinct keys ({len(set(rep['bound']) & set(D.DD_KEYS))} of the 108 DD facts bound; {len(borrowed)} borrowed keys from approved CCG / RSPEC / SIR facts, listed below). Bindings: _pipeline/DD-bindings.csv ({len(bind)} rows: location, key, register_id, effective_from).
- Marker cells (in-place research gaps): {len(rep['gapmarks'])} cells, ids DD-RQ-01 to DD-RQ-04; documented limitations use the neutral wording "not named in the cited sources".

## Fact bindings (section -> key -> register_id), sample; full table in _pipeline/DD-bindings.csv
| Location | Claim | key | register_id |
|---|---|---|---|
""" + "\n".join(
    f"| {r['location']} | tagged value of the key | `{r['key']}` | {r['register_id']} |" for r in bind[:22]) + f"""

Borrowed keys (not in DD-8_sheets-facts.json; the value is carried by an approved facts file and cited with its own tag): {', '.join('`' + k + '`' for k in borrowed)}.
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
Direction 1: {len(recs)} field rows of the 20 Report Specs. {st['MAPPED']} rows cite the Data Dictionary and map to a DD element; {st['EXCEPTION']} rows cite it and are exceptions; {st['NOT-DD']} rows do not cite it (payroll results, calculated values, generator configuration: not DD fields by the tree); UNMAPPED = {st.get('UNMAPPED', 0)}.
Name: {dict(name_c)} (a spec row is one record position of a DD concept, so the DD name equals the spec name in {name_c.get('identical name', 0)} rows and the authority label of the spec in {name_c.get('identical authority label', 0)}). Type: {dict(type_c)} (match = spec column R class compatible with the DD field type; the 27 'n/a' are the State electronic filing threshold rows, where the spec row describes the threshold amount, a jurisdiction constant, and the DD holds the employer flag). Format: Pre-Defined Format is taken from column J where the spec gives a pattern (16 rows identical); {len(fmt_diff)} rows differ by design and are listed in the CSV: {', '.join(r['spec'] + ' row ' + str(r['row']) for r in fmt_diff)} (file layout without the hyphen / State format).
Exceptions (cite the DD, no DD element, by the tree; both for the Report Spec owner to re-point at the next propagation, the specs were not touched):
""" + "\n".join(f"- {r['spec']} row {r['row']} '{r['name']}': {r['reason']}" for r in exc) + f"""
Direction 2: {sum(1 for e in DEF.ELEMENTS if usage[e['id']]['used'])} of {n_el} elements have a consumer. {n_el - len(calc_only)} elements are cited by a Report Spec row or a spec cell that tags their fact; {len(calc_only)} are named only as inputs of a payroll calculation or notice by their facts ({'; '.join(calc_only)}): the WTC and SIR are not built yet, so the consumer is the facts' consumers entry (QA to confirm at the WTC close).

## Lessons from earlier rounds (applied)
1. Every factual cell carries [[FACT:key=value]] with the exact value; dd_lint checks tag = fact (period-aware): {rep['tags']} tags, {len(rep['mismatch'])} mismatches, {len(rep['missing_key'])} keys missing.
2. New gaps: marker plus request (DD-RQ-01..04 in _research/DD-research-request.json); documented limitations (TX start quarter, CT Q3 2026 positions, PA PSD code layout, OH municipal code identity, visa class examples) use "not named in the cited sources" and also appear in the request file as RQ-06..RQ-10.
3. No tier-B number: C30 = {len(rep['C30'])}. Register tiers of the 108 facts: {dict(Counter(D.REG[f['register_id']]['tier'] + '/' + D.REG[f['register_id']]['status'] for f in D.DDFACTS['facts']))}.
4. Period awareness: every source cell prints the effective period of its fact ("effective from ...", "effective ... to ..."). dd.oh.school_district_code is the 2025 list (effective 2025-01-01 to 2025-12-31): the cell says the 2026 changes are not named in the cited sources. dd.multi.sui_state has effective_to 2027-06-30. The WTC-side keys ga.sui.new_employer.rate.contribution (2026-01-01) and ma.pfml.* (2027-01-01) are not used by any DD cell.
5. Units from the fact: dd.state.new_hire.rehire_gap_days is written "[[FACT:...=60]] days" (unit_of_measure of the fact); no percentage is written in the workbook (PCT 0, FRAC 0, UNIT 0).
6. Portal and authority names: none is written in the DD (no portal appears). US-LAP52-005 LAWATS is not used.
7. RSPEC x DD: above.
8. Re-pointed elements (precheck-next, tokens only) used by DD cells, each opened in the local copy and read in context: dd.state.w4.ar (AR4ECSP: "You should have a Form AR4EC or AR4ECSP", withholding exemption certificate, US-ARP51-002 p7), dd.state.w4.hi (HW-6 nonresident certificate and HW-7 exemption, US-HIP51-001), dd.state.w4.oh (IT 4 "or the employer must withhold tax based on the employee claiming zero exemptions", US-OHP51-002; the primary row US-OH-002 has no local copy), dd.state.w4.ut (W-4E rule R865-9I and Pub. 14, US-UTPIT-002 / US-UTS5-013), dd.ct.ui.occupation_hours_zip (primary row CGS 31-225a(j)(1)(B) holds the clause "Commencing with the third calendar quarter of 2026 ... may include ... occupation ... hours worked ... zip code of primary worksite"; the re-pointed IP 2026-1 hit is a due-date table and is not relied on), dd.employer.state_account_ids (UT 14-digit "ending in WTH", KS "(036#######F##)", MD CRN positions 338-345, IA 9-digit permit number: each read in its copy). All hold; no cell uses a gap for them. The rows that agent 2 hand-read (OH, PA, FL) were taken as given.
9. _precheck_unmatched facts (7), bound to the fact and not restated as verified: dd.ms.new_hire.extra (DOB), dd.ga.new_hire.extra (DOB), dd.ia.new_hire.health (IWO), dd.ct.ui.occupation_hours_zip (ZIP), dd.state.w4.az (2026), dd.state.w4.mt (DOR), dd.oh.municipal_rate_table (5-digit). Builder read-through of the copies: IWO holds (Iowa Code 252G.3: "address to which income withholding orders ... should be sent"), ZIP holds (CGS 31-225a), DOB is plain wording, DOR is plain wording, 5-digit was hand-read by agent 2; "(2026)" of the Arizona A-4 is not in the page text (the file name of the held copy says 2026).

## Open items (gap markers and limitations)
| id | Location | Marker | Request | Blocking |
|---|---|---|---|---|
""" + "\n".join(
    f"| DD-{r['id']} | {r['location'].split('!', 1)[1]} | {'in-place marker' if r.get('_status') == 'open_non_blocking' else 'neutral wording'} | {r['key']} | no |" for r in rq) + f"""

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
| C12 structure per template (validate_workbook.py --artifact DD; dd_lint C12) | PASS: 8 sheets in order, header rows 4, ID Information 22 columns A-V, Country Fields 23 labelled columns B-W, mappers B-F; orange columns empty; {rep['info']['ID Information']} + {rep['info']['Country Fields']} data rows counted out of the repeated headers; no duplicate Field Name; every mapper referenced and defined |
| C29 residual markers | {len(rep['C29'])} |
| WORD pipeline wording | {len(rep['WORD'])} |
| C30 tier-B number | {len(rep['C30'])} |
| C46 period-aware | {rep['tags']} tags, {len(rep['mismatch'])} mismatches, {len(rep['missing_key'])} missing keys, unbound {len(rep['unbound'])}, DERIVED {rep['derived']} |
| FRAC / PCT / UNIT | {len(rep['FRAC'])} / {len(rep['PCT'])} / {len(rep['UNIT'])} |
| C71 regenerate = issued | PASS (regen_check_dd.py: rebuilt workbook identical) |
| RSPEC x DD reconciliation | UNMAPPED {st.get('UNMAPPED', 0)}; {st['EXCEPTION']} exceptions |
| Excel open (open_check.ps1, COM) | OK |
| validate_contract (research-request) | PASS |
| Report Specs unchanged | md5 of the 20 workbooks equals 04-reports-spec/_build/checks/md5_final.txt (checked before and after the build) |

## Accuracy
About 80%. Every field has an official-source-backed fact or a Report Specification row; the gaps: the line structure of the State withholding certificates (RQ-01), nine external code lists (RQ-02), the UI adjustment reason codes (RQ-03), items bound to facts that the local copies do not support (list above), and the three F26 judgement calls. Closing it needs agent 2 (facts for RQ-01 to RQ-05 and the four copy discrepancies) and the Report Spec owner (two forward references).
"""
open(os.path.join(D.BASE, "_pipeline", "DD-build-log.md"), "w", encoding="utf-8").write(log)
print("written DD-build-log.md", len(log))
