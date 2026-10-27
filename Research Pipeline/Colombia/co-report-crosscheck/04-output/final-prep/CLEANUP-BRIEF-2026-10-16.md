# Cleanup brief: from v1.1 DRAFT to the initial version (16 Oct 2026)

The 6 specs have not been submitted to the development team yet. They go out as an initial version: no DRAFT, no review trail, no correction history. You rewrite the text of ONE spec and write `04-output/final-prep/<SPEC>-cleanup-map.json`. You do NOT edit any workbook; a script applies your map by cell and runs the checks.

## Inputs
- The DRAFT workbook: `02-specs-out/<SPEC>-...-DRAFT-2026-10-15.xlsx` (read with openpyxl, every sheet).
- The flagged-cell list: `04-output/final-prep/<SPEC>-flagged-cells.json` (sheet, cell, field id, patterns, current text). It is a starting point found by regex; you must also read every other text cell of the spec sheet (columns A-S, rows 3+) and of the other sheets (Report Matrix, Payroll Scope Summary, File Structure, Field Options, Population Rules, Example Analysis, Sample File) and add any cell that breaks the rules below. Column T and U of the spec sheet and the Version Control sheet are handled by the script: ignore them.

## What the final text must look like
Every explanation states the rule as it is, with its legal source. The reader is a developer who has never seen a client file or a review.

Remove, by rewriting the cell:
1. Review or process language: corrected, revised, review(ed/er), verified, verifier, verification, cross-check, round 1 / round 2, proposed status, DRAFT, previously, no longer, "added after the original build", "15 Oct 2026", "decision of ...", "DECISION PENDING", "OPEN", "pending RA", "see Query to RA", "query", "RA to confirm", "client to confirm/provide/explain", "to be confirmed", "(inference)", "not evidenced", "evidence", "observed", "CLIENT DATA" / "CLIENT NE FILE" / "CLIENT EVIDENCE" / "CLIENT PRACTICE" labels.
2. Comparisons with a previous version: "not 686", "corrected from campo 95", "was I to V", "instead of the 12-position example", "replacing the earlier ...".
3. Observations about client files or client data: "the client's file ...", "the client's certificates show ...", "the client's current electronic payroll file reports ...", "in the Sep-2026 run 255 of 261 employees ...", "Payroll id REF-P201-090", "Base of Withholding column V", "G2N 'Salary Assigned' (239 of 261)", "the client holds ...", "PMI pays ...", "at PMI ...", counts of employees, totals in pesos taken from client reports, report names used as evidence (Vertical G2N Dynamic, Base of Withholding, Accumulated Report, Leave Absence Report, Master Data report, Detail IBC, Bank Payments, Monthly_fixed, ConsolidadoCCT, Form 220 working file).

Keep, rephrased as rules:
- Legal citations (Ley, Decreto, Resolución, Anexo Técnico, ET articles, CST, XSD, DIAN instruction guides) exactly as cited.
- Wage-type mappings: "Source: wage types 62100 'Ordinary Salary' and 62140 'Integral Salary'" is a rule and stays; "the client's file confirms WT 62100 + 62140 for 261 of 261" is an observation and goes. Keep wage-type codes and their descriptions.
- Source fields in the HR / payroll system, stated as mappings: "Source: Master Data field 'Hire Date' (DD-MM-YYYY, converted to AAAA-MM-DD)" stays; "the client's Master Data holds three start dates differing for 40 employees" goes. Use the field names as system field names, not as "the client's report column".
- Configuration points: where the text said "client to confirm X" or "pending the client's answer", write it as a configuration parameter: "X is a configuration parameter supplied at implementation (e.g. the Employee Group to contributor-type mapping table)". Where the text said "RA to confirm whether A or B", state the rule the spec currently applies (the Field Explanation's own rule) and drop the question; if the spec gives no rule at all for that point, write "Rule to be set at implementation: ..." in one neutral sentence and list the item in `unrewritable` so Wallisson sees it.
- Data-quality rules stay as rules: "Blank values are rejected as data errors" stays; "4 employees have a blank work location" goes.
- Numbers that are part of the rule (thresholds, UVT, SMMLV, percentages, lengths, positions, rates, rounding) stay. Numbers that are client measurements (employee counts, run totals, match rates) go.
- Formatting rules, record positions, option values, examples stay.

Also:
- Field Options, Example Analysis, Population Rules, Report Matrix, Payroll Scope Summary, File Structure, Sample File: same rules. In File Structure, headers such as "═══ SUBMISSION FORMAT - VERIFIED (V2.7 STEP 3.5) ═══" lose the process part ("═══ SUBMISSION FORMAT ═══"); "FORMAT TO CONFIRM" rows are rewritten as statements of the format. In the Sample File, "PLACEHOLDER" is replaced by the script (do not list those cells unless the sentence needs more than that word changed).
- Keep every cell's substance and length reasonable: a cleaned explanation keeps all rules of the original, loses only the review and client-observation sentences. Do not add new rules. Do not shorten a rule to a fragment.
- Section-header cells ("═══ ... ═══" in column A) and the header row stay unless they contain a listed word.
- No masked tokens (NAME_nnnn, ID digits, MASKED_TEXT, POSTAL_nnnn, SHORTID_nnnn, ENTID_nnnn) and no employee identifiers anywhere.
- English. Spanish field names and labels stay as they are.

## Output
```json
{"spec":"CO-XXX-NNN","draft":"02-specs-out/<file>.xlsx","final_name":"<name given>",
 "edits":[{"sheet":"<sheet>","cell":"M23","field_id":"...","current":"<exact current text>","proposed":"<full new text>","why":"<which rule: review language | version comparison | client observation | process header>"}],
 "unrewritable":["<sheet>!<cell> (<field id>): <the sentence and why it cannot be rewritten without losing content>"],
 "summary":{"cells_rewritten":0,"by_sheet":{},"unrewritable":0}}
```
`current` must be the exact current cell text (the script refuses a mismatch). A `proposed` of "" clears the cell (use only for cells whose whole content is review language, e.g. a note "Verified vs XSD" in a column other than T/U).

## Final names
CO-PILA-003-AportesSeguridadSocial-Spec.xlsx, CO-DIAN-001-NominaElectronica-Spec.xlsx, CO-DIAN-002-Formulario350-Spec.xlsx, CO-DIAN-004-Formulario220-Spec.xlsx, CO-DIAN-005-Formato2276-Spec.xlsx, CO-CESANTIAS-006-ConsignacionAnual-Spec.xlsx

## Final reply
Cells rewritten per sheet, the list of unrewritable sentences, and anything you deliberately kept although it matched a pattern (with the reason).
