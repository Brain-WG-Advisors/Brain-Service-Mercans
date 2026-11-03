# Agent 2 (source hunter): CCG F44 closure, 2026-11-02

Scope: merge shard S5B-P4, then close the "not verified / partial" items in `_research/stage5/browser-pass-P4.md`. No web fetch was made. Nothing was written under `01-ccg/` or `~/mercans-pipeline`, and `rebuild_all.py` was not run. Backups are in `_research/qa-r3b-fix/_backup2/` (the register, all 73 facts files and all packs, taken before any write). Scripts: `scripts/apply_f44_p4.py` and `scripts/apply_f44_p4_b.py`. Logs: `apply-f44-p4-log.json` and `apply-f44-p4-b-log.json`.

## 1. Shard merge
- `legal-basis-register.csv` went from 2,616 to 2,657 rows: the 41 S5B-P4 rows were appended. The file still has 20 columns, CRLF line endings and unique ids. 84 lines differ from the backup: 41 new rows, the 41 superseded rows, US-PA-009 and US-IDS5-021.
- Each of the 41 cited rows now has `effective_to` = 2026-11-02 and `status` = superseded. Its `consumed_by` was carried into the successor row (union of the old and shard tokens) and also kept on the old row as the re-sync list. US-CTQ1B-001 previously had `effective_to` 2026-12-31; it is now 2026-11-02, as instructed.
- Re-pointing covered all 73 `_research/*-facts.json` files: `facts[]`, notes, `_history`, `unresolved[]` and the key-to-source maps in m05/m06. 32 files changed. 645 `register_id` values were re-pointed, 566 of them in the CT tables (US-CTQ1B-001 to US-CTB5-401). `url` and `tier` were synced from the successor row.
- US-NY-005 is split by key. `ny.dbl.*` goes to US-NYB5-401 (WCL 209), and the tier and authority were updated to match. Anything else goes to US-NYB5-402 (the DFS PFL page).
- In 27 packs the ids were replaced line by line. Older notes in `mandate-answers/`, `synthesis-*` and `qa-r*` were not touched; they are history.
- Checks after the merge: 0 superseded P4 ids remain in any facts file; every `register_id` resolves; there is no fact/row tier mismatch; and every successor row's `consumed_by` contains every artifact/unit that cites it.

## 2. key → row → local file → quote

| key | row (was) | local file | quote / basis | result |
|---|---|---|---|---|
| co.famli.total.rate 0.86 (2027) | US-COB5-301 (US-COS5-008), tier A.3 | ccg-sources/CO/CO_CDLE_FAMLI-business-brief-2026-09-30_2026-11-02.html | "The 2027 premium rate will be 0.86% of wages, down from 0.88% in 2026." | verified (CCG annex_CO + WTC) |
| co.famli.total.rate 0.88 (2026) | US-COB5-401 (US-COFAMLI-001) | CO/CO_FAMLI_employers_2026-11-02.txt | "The premiums are set to 0.88% of the employee's wage, with 0.44% paid by the employer and 0.44% paid by the employee." | verified |
| ny.dbl.employee.rate 0.5 / weekly max 0.60 | US-NYB5-401 (CCG: US-NY-010; WTC: US-NY-005), tier A.1 | NY/NY_WCL-209_nysenate_browser_2026-11-02.txt | "one-half of one per centum of the employee's wages ... but not in excess of sixty cents per week" | verified; WTC no longer cites the DFS PFL page |
| mn.pit.oracle.example_1.withholding 91.27 | US-MNS5-010 (unchanged) | pdfs/MN/wh-inst-26_webfetch-20261030.pdf p.34 | `verification_method` is now "derived arithmetically" in all 3 files (CCG annex_MN, m12, WTC). Inputs in the note: 26 periods; 5,300 per allowance; single row 38,010–114,130 with base 1,782.09 and 6.80%. 2,000×26 = 52,000; minus 5,300 = 46,700; 1,782.09 + 8,690×0.068 = 2,373.01; ÷26 = 91.27 (recomputed in Python) | derived |
| pa.sui.employer.rate.min / .max, pa.sui.new_employer.rate, pa.ui.rate.new_employer.construction | US-PA-009 (unchanged) | PA/PA_US-PA-009_r2-curl_2026-11-02.html | ".014190" / ".103734" / ".038220" / ".105924" ("this includes the 9.2 percent Surcharge") | verified. The decimal quotes were added to the **register row's** `verification_method`, and `verified_on` was set to 2026-11-02. The facts' `verification_method` is a schema enum, so each fact's note carries its decimal instead. |
| ma.wh.supplemental.rate 5 | US-MAP51-003 (US-MAR3-002, then US-MAB5-402) | pdfs/MA/circularM-2026_wayback-20261018080456.pdf p.13 §G | "5. If the result of step 4 is $1,107,750 or less, withhold 5% of the amount determined in step 3." | verified (partial closed) |
| id.sui.new_employer.rate 1.0 | CCG: US-IDP52-004 (unchanged); WTC: US-IDB5-402 (US-IDP7-001) | ID transcription + ID/IDOL_Handbook_Tax-information_Nov-2025 p.21 [US-IDS5-021] | "Standard \| 1.000% \| 0.97000% \| 0.00000% \| 0.03000%" + "All new employers except cost-reimbursement employers begin with the same standard unemployment insurance tax rate for at least the first six calendar quarters." | verified (Standard = new employer, by the handbook) |
| tn.sui.employee.rate 0 | US-TNB5-401 (US-TNR3-003) | TN/TN_DLWD_unemployment-insurance-tax_2026-11-02.txt (+ US-TNS5-002/003) | Absence: the page frames premiums only as employer liability ("Employers who are liable to pay unemployment taxes include the following"); rates are set by the employer's reserve ratio; no employee rate appears. | **still partial.** Confidence lowered to medium and the reasoning is in the note. Would close: the T.C.A. 50-7-403 text (premiums payable by employers). No local TN file states it. |
| fed.fica.oasdi.wage_base 192,300 (2027) | US-FEDB5-401 (US-FED-022) | FED/FED_SSA_cbb_browser_2026-11-02.txt l.4, l.73 | "For earnings in 2027, this base is $192,300." | verified. Confidence raised to high. The 2 unresolved re-verification items were closed and moved to `_history` (annex_FED, WTC global): `fed.fica.oasdi.wage_base.next_year_reverification` and `.2027_reverify`. |

The other 36 re-pointed keys are the "yes" rows of browser-pass-P4.md. Each now cites its B5-4xx row, and that row's local file carries the quoted figure.

## 3. Validation
- All 73 facts files validate against facts.schema.json with 0 errors (jsonschema). The 32 touched files PASS `validate_contract.py facts`.
- Line endings and indentation were preserved per file. After the first pass the CRLF line endings were restored on the register and 24 facts files.

## Still open
- tn.sui.employee.rate: absence fact with no positive statement (see above).
- Not in this scope, carried from P4: the Denver OPT figures rest on the 2025-07 Tax Guide edition; the Pittsburgh payroll-expense FAQ is undated; the ma.wtf 0.056 statutory rate has no confirmed 2026 adjustment.
- Not touched: superseded rows from other agents still cited in facts (for example US-AZS5-028, US-DEP51-003, US-MEP51-004, US-RI-006, US-WVLAB-001, US-TXPIT-001, US-CAEDD-004, US-MIS5-026, US-NYS5-023). They are outside the P4 shard.
- SOURCE-REGISTER.md has not been regenerated for the 41 new rows.
