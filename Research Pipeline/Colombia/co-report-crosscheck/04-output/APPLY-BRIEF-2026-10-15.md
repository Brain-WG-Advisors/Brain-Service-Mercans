# Brief: build the APPROVED change map for one Colombia spec (15 Oct 2026)

You produce `04-output/<SPEC>-changemap-APPROVED.json`. You do NOT edit any spec. A separate script applies the file cell by cell to a DRAFT copy in `02-specs-out/` and runs the diff. Everything in English. Never open `02-client-reports-raw/` or `99-local-only/`.

## Inputs to read
1. `CLAUDE.md`
2. `04-output/<SPEC>-changemap-PROPOSED.json` (the proposed edits, status keep / change / review)
3. `04-output/<SPEC>-crosscheck.json` (verdicts, findings, evidence)
4. `04-output/<SPEC>-verification.json` (independent second pass: confirmed / overturned / needs Wallisson, with factual corrections)
5. The spec workbook in `01-specs/` (read-only with openpyxl; read the exact current text of every cell you will change, in every sheet)
6. Wallisson's decisions (section "Decisions" below)

## Rules
- **Apply only what is approved**: (a) PROPOSED edits with status `change` whose verification result is `confirmed`, with every factual correction the verifier made folded into the text; (b) edits required by Wallisson's decisions; (c) for every item still open (status `review`, verifier `needs Wallisson`, decisions 6-8), NO change to the Field Explanation: put a short query in column T "Query to RA" only.
- Edits the verifier **overturned** are not applied as proposed. If the verifier said "verdict stays but the text must be corrected", apply the corrected text. If the verifier changed the verdict to Not evidenced or to "Explanation to improve with RA query", drop the M edit and add the query in T.
- Column T "Query to RA": if the cell already has text, keep it and append the new query after a line break (`\n`). Each query is one or two sentences and names what RA or the client must confirm.
- Column M "Field Explanation": give the full replacement text (the whole cell, not a fragment). Keep the existing substance, correct only what the evidence and decisions require, and never present an inference as a confirmed client instruction (mark inferences as inferences).
- Column U "RA Comments": do NOT write it in the edits; list the changed field rows in `mark_corrected_rows` and the applier writes "Corrected" there.
- `current` must be the exact current cell text (copy it from openpyxl; for cells stored as formulas openpyxl returns a string starting with "=", copy that). The applier refuses an edit whose `current` does not match the cell, so be exact. Use `null` for an empty cell.
- Edits in other sheets (Example Analysis, Population Rules, Report Matrix, Payroll Scope Summary, Field Options, Sample File) are allowed ONLY where a decision below requires them; give sheet name and cell reference.
- One Version Control sentence per alteration (a field, or one coherent group of cells changed for one reason). Short, factual, states only what is confirmed, names the field id(s) and the legal source where the decision cites one. No speculation.
- Never invent a column, code, wage type, or rule. If something cannot be evidenced, say so in the query instead.
- Do not add or delete rows. Do not touch merged cells or section-header rows.

## Output schema
```json
{
  "spec": "CO-XXX-NNN",
  "spec_file": "01-specs/<file>.xlsx",
  "spec_sheet": "<main spec sheet name>",
  "header_row": 2,
  "edits": [
    {"sheet": "<sheet name>", "cell": "M58", "row": 58, "column_letter": "M",
     "field_id": "T2R1-020", "field_name": "Total payroll value",
     "current": "<exact current text or null>", "proposed": "<full new text>",
     "reason": "<one sentence>", "basis": "decision 1 | changemap+verifier confirmed | verifier correction",
     "vc_sentence": "<one short Version Control sentence for this alteration>"}
  ],
  "mark_corrected_rows": [58, 111],
  "version_control": ["<deduplicated list of the vc_sentence values, in order>"],
  "not_applied": [{"row": 22, "field_id": "...", "why": "open: query only (decision 8)"}],
  "summary": {"edits_M": 0, "edits_T": 0, "edits_other_columns": 0, "edits_other_sheets": 0, "fields_marked_corrected": 0, "vc_sentences": 0}
}
```

## Decisions by Wallisson (15 Oct 2026)
1. **PILA T2R1-020 (row 58)**: the total payroll value is the SUM of campo 45 (IBC CCF), per AT2 v30 §2.1.1.1 campo 20. Correct every place that says campo 95 / parafiscal base: PILA Spec L58 System Mapping (`SUM(Payroll.Parafiscal_Base)`), Example Analysis C18 and D18, Population Rules C9 (the assertion) and any other Population Rules cell that ties T2R1-020 to campo 95, Sample File A76, and the cross-reference inside M112 (T2R2-095) so that it agrees. M58 already says campo 45: keep it, correct only if it contradicts itself.
2. **PILA T2R2-045 (row 111) and T2R2-065 (row 138)**: the IBC CCF has NO 25 SMMLV ceiling; the base is the monthly salary payroll (Ley 21 de 1982 art. 17), with 70% for integral salary (Ley 789 de 2002 art. 49). Remove the ceiling from M111, from M138 if it repeats it, from Payroll Scope Summary C28 ("Applies to pension, health, occupational risk and the CCF") and from any Population Rules cell that caps the CCF base. Keep the floor rules as they are unless they repeat the cap.
3. **PILA T2R2-076 (row 150), T2R2-043 (health IBC row) and Population Rules**: the ET art. 114-1 exoneration uses the total earnings of the month (total devengado) < 10 SMMLV (Decreto 1828 de 2013 art. 7); in addition campo 76 must be N whenever campo 43 >= 10 SMMLV (AT2 v30 campo 76). Write both rules.
4. **Nómina Electrónica transport allowance (row 87)**: AuxilioTransporte only up to 2 SMMLV (Ley 15 de 1959); the collective-agreement transport allowance paid above 2 SMMLV goes to Auxilios (AuxilioS or AuxilioNS according to the salary character agreed in the convention). Put a query in column T about the salary character of WT 62523 in the convention.
5. **Cesantías**: an employee who leaves is excluded from the deposit and is paid directly (Ley 50 de 1990 art. 99 num. 4). Correct the explanation of field E08 (row 11) and the Report Matrix sentence (A32, "...is owed a pro rata deposit..."). Direct payments in January to employees who left before the deposit are lawful: write T14 and E92 accordingly (deposit net of direct payments already made; a leaver paid directly is excluded).
6. **Formulario 350 pensions (rows 24/25, casillas 78/94)**: the spec rule stays (ET art. 206 num. 5). Query in column T about the nature of WT 62151 "Retirement Payment - PRV-6795". No change to M.
7. **Pensioners (PILA T2R2-006 row 68; Nómina Electrónica pension rate row 185 and worker sub-type row 54)**: the spec stays; query in column T about the "Pensioner Effective Date" of the 2 employees (equal to their hire date). No change to M.
8. **Open, text unchanged, query in T only**: the position of non-residents in Form 350 (row 22 and rows 31-34) and of vacation pay in Form 220 (row 33).
9. Items the verifier left as "needs Wallisson" and that are not covered above (e.g. contingent withholding treatment, recipient country code format, tax year of the February severance deposit, meal benefit above 310 UVT, beneficiary columns on pension rows, T14 January practice beyond decision 5): query in T only, no M change. For Form 350 row 39 apply the explanation WITHOUT the "upper-case ISO 3166-1 alpha-2" clause and add the query.

## Spec-specific pointers
- CO-PILA-003: also fold in the verifier's corrections (row 65 no employee lacks a document column; row 86 46 employees; row 116 list the voluntary-pension codes explicitly, excluding 25817; rows 71-72 add that 4 employees have a blank work location; the "21 amount fields" count is 19; row 112 sentence must agree with decision 1). Row 68 and the related row 150 counter-example corrections as the verifier states.
- CO-DIAN-001: rows 85, 130, 133, 171, 172, 202, 214 must use the verifier's corrected texts; row 68 becomes an Explanation to improve (4 integral employees differ between G2N and Master Data); rows 54 and 185 per decision 7; row 87 per decision 4; smaller corrections (rows 16, 195, 196, 191, 187-190, 145-146, 149-150) folded in; the Bank Payments reclassification is a report-map matter, not a spec edit.
- CO-DIAN-002: rows 23 and 39 as corrected by the verifier (neutral wording for the 6 employees on WT 21330; G2N example -49100 is WT 21117, not 2552; 9 procedure-3 employees in Master Data, 7 in the run; Payroll id differs between reports); rows 22, 24, 25 per decisions 6 and 8 (query only); rounding column P edits only if confirmed.
- CO-DIAN-004: rows 24, 25 are Not evidenced (no edit); row 33 per decision 8 (query only); rows 14, 29, 41, 27, 45 with the verifier's corrections (248 of 261 match; 13 foreigner-card holders blank; 777 payees without Master Data row; UVT from the tax-year parameter, not WT 58001; "substitute pension" as unconfirmed; leave payouts 79405-79419 added to the RA list; counts "of 261").
- CO-DIAN-005: ids 12 and 24 are open (query only); corrections: 261 people, 14 rows with more than one document column, 0 with none, 8 people without identity in any report, 6 foreign countries, minimum meal amount 20,951, 5 of 6 exceptions with integral salary, counts "of 261", wage types 65803/65804 added to the classification list; the Payroll Scope Summary pensioner row is NOT added (structural change, pending).
- CO-CESANTIAS-006: decision 5 for E08 (M11), Report Matrix A32, T14 (row 30) and E92 (row 51); verifier corrections (T20: 21 and 40; T10: 204 of 284 and hedge the partial-payment phrase; IN01 count 3,715; 62110/62117 110 employees); employee 92256020 case goes into a query, not into the explanation.

## Final reply
Counts per column and sheet, the list of VC sentences, and the list of items left as query only.
