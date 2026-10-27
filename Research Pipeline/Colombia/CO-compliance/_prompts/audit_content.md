# Colombia PRE-SUBMISSION AUDIT — CONTENT REVIEW + HANDOVER STATUS

You are the Pre-Submission Audit Gate for Colombia v2.4 build.

## INPUTS

1. Mechanical audit results: ~/mercans-pipeline/CO-compliance/logs/audit_v24_mechanical.json
2. Audit reference: ~/mercans-pipeline/shared/PRESUBMISSION_AUDIT.md (C1-C22)
3. Failure log: ~/mercans-pipeline/shared/country_failure_log.md (F1-F15)
4. All artifacts in ~/mercans-pipeline/CO-compliance/
5. Country failure log to check against

## YOUR TASK

1. Read the mechanical audit results.
2. For each FAIL or MANUAL, investigate the actual artifact:
   - Open the file
   - Find the flagged issue in context
   - Determine if it's a real problem or a false positive

3. **FALSE POSITIVE HANDLING** (proven on Chile v2.4):
   If a mechanical check FAILS but manual inspection reveals the failure is
   a false positive (e.g., audit matched a substring inside non-English terms,
   or flagged a structurally valid pattern as invalid), you may OVERRIDE the
   verdict with written justification.
   
   Examples of valid overrides:
   - "C8 flagged 'TODO' but the 4 hits are all inside Spanish legal phrase
     'a todo evento' (Art. 164 CdT severance fund), not English open-item markers"
   - "C12 reports thin schema but Colombia's tax authority publishes only
     12 column requirements; thin schema is justified per the official spec"

4. **REAL FAILURE HANDLING:**
   If a FAIL is genuine, attempt to fix the artifact:
   - For C8 real markers: search for TBD/TODO/FIXME and resolve from sources
   - For C11 thin coverage: add missing H3 headings + answers from CCG content
   - For C12 thin schema: extract columns from source PDFs and add to spec
   - For C20 missing specs: generate the missing spec
   - For C21 wrong sheets: rename/add sheets in payslip
   - For C22 thin spec: expand sections with WTC/DD content
   - For C33 CCG local-language leakage (MANUAL): open the CCG and TRANSLATE every
     flagged local-language passage into English. Rules:
       * The CCG PROSE must end up English-only (headings, sentences, table cells,
         worked examples, notes).
       * Preserve a genuine statutory/legal term of art by putting the English wording
         first and the original term in parentheses on FIRST use only, e.g.
         "professional expenses (frais professionnels)". After first use, English alone.
       * Keep official proper names of authorities/forms/statutes as-is (e.g.
         "Direction Générale des Impôts (DGI)") — those are proper nouns, not prose.
       * Verify each C33 hit in context first: a hit that is ONLY an official proper
         name or an already-parenthesised citation is a false positive — record it as an
         override, do not "translate" a proper noun.
       * This applies to the CCG ONLY. Do NOT touch the DD/WTC/Payslip local-language
         fields — the "Name Local (Spanish)" columns and the
         "Colombia (ES)" payslip sheet are correct by design.
       * After translating, add a Version Control entry in the CCG for the language pass
         (same session), consistent with how every other edit is logged.

5. After all fixes attempted, re-run the mechanical audit:
   python3 ~/mercans-pipeline/CO-compliance/_audit_v24_mechanical.py > /tmp/audit_recheck.json
   Compare to original results.

## OUTPUT

Save handover_status.md to:
~/mercans-pipeline/CO-compliance/07-qa-crosscheck/handover_status.md

Structure:

```markdown
# Pre-Submission Audit — Colombia v2.4

**Overall verdict:** READY_FOR_HANDOVER | BLOCKED (with reason)

**Mechanical audit raw result:** [PASS/MANUAL/FAIL summary]

## Artifacts produced
| Artifact | File | Size |
|---|---|---|
| CCG | 01-ccg/CO-CCG-001-v1.0.docx | XX KB |
| Report Specs | 04-reports-spec/ | N files |
| DD | 05-data-dictionary/CO-DD-001-v1.0.xlsx | XX KB |
| WTC | 02-wtc/CO-WTC-001-v1.0.xlsx | XX KB |
| SIR index | 03-statutory-integrations/CO-SIR-INDEX-001-v1.0.docx | XX KB |
| Integration runbooks | 03-statutory-integrations/<AUTH>/ (per-authority, via si-runbook) | — |
| Payslip | 06-payslip/CO_Compliance_Payslip_Generator.xlsx | XX KB |

## Audit results (C1-C22)
[Render the JSON as a readable table]

## False positives identified
[For each override, explain WHY the FAIL is not a real issue + cite specific
paragraphs/cells. Tag with check ID, e.g., "C8 override: ..."]

## Real fixes applied
[For each genuine FAIL fixed: what was wrong, what you changed]

## Remaining issues (if any)
[FAILs that couldn't be fixed — escalate to manual review]

## Sign-off recommendation
[Either READY_FOR_HANDOVER or BLOCKED with required actions]

## Next steps
1. Open the artifacts and review
2. Apply any manual fixes flagged above
3. If READY: share with dev team
4. Append any new failure patterns to ~/mercans-pipeline/shared/country_failure_log.md
```
