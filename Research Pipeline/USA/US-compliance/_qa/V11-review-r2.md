# US v1.1 QA review, round 2 of 3 (2026-11-06)

**Verdict: FAIL.** The review found 1 blocker, 4 majors and 8 minors. The full record is `V11-review-r2.json` (schema review 1.4.0, validated).

Files reviewed: all 26 entries in `_pipeline/V11-md5.txt`, md5 OK. Each was compared with its `_v1.0/` copy line by line (docx) and cell by cell (xlsx). C43 was not counted, as instructed.

## r1 findings
Of the 20 round-1 findings, 16 are closed, 3 are partly closed and 1 is open.
- **Partly closed:**
  - #1 (US-FLV6-002 is still dated at retrieval).
  - #3 (4 Ohio Revised Code rows still use other authority spellings).
  - #12 (the change-log row does not log the W-4 rewording).
- **Open:** #7 (GA minimum-wage exemptions, F18).

## Focus items
| # | Item | Result |
|---|---|---|
| 2 | Register dates | Sampled 15 of the 55 re-dated rows: **15/15 match** the saved copy. Sampled 5 of the 19 rows kept at 2026-01-01 (17 limitations plus 2 dated by an edition): **5/5 print no date in the copy**. |
| 3 | Provisional/historical | No provisional item is shown as in-force law. **OH:** the label "implementing rule proposed only, not in force" was put on an in-force no-PFML fact (major). **WTC DC D381:** the rule is **not wrong as law**. D.C. Code 47-1812.08(b)(1) (US-DCS5-025, read in full) gives one method for all wages and no flat supplemental rate. The defect is the historical source and its label. The WTC should cite US-DCS5-025, be shown as in force, and retire US-DCP52-002 (major, source-hunter). |
| 4 | `deliverable_wording.py` | 15 rewrites sampled: 13 keep the meaning and all 15 keep their numbers. **BLOCKER:** "not checked" became "not verified" in 13 Form W-4 *checkbox* lines (m02, m06, m12: "Step 2 not verified", "Checked / not verified"). The federal method now reads wrong, and the CCG contradicts itself. Also: "not transcribed" became "not configured" (HI), one doubled phrase (WTC D462), and the SIR provider-choice line. |
| 5 | Change logs | RSPEC x20, WTC, DD and SIR are accurate against the diff. The v1.0 row's date was changed from 2027-03-31 to 2026-11-05 in every workbook and in the SIR, and no row logs it. |
| 6 | Regression | 13 modules and 53 annexes kept. The 61 v1.0 lines with no v1.1 counterpart are all gap closures or re-pointed sources. No other silent loss. |
| 7 | C29 | Accepted as the exception: 9 lines, identical to v1.0. 7 are the SSA "S-XXXXXX-Y" mask; **2 are the VT "WHTXXXXXXXX" account mask** (the build log is inaccurate). |

## Owners
- **artifact-builder:** finding 1 (blocker), 3, 6, 7, 8, 9 and 13 ("refused access").
- **compliance-source-hunter:** findings 2 (FL date), 4 (GA F18, or a documented limitation), 5 (DC rebind and the wages definition), 10 (Ohio spellings), 11 (register under-filled; TXB5-301 stale note), 12 (MI note), and 13 (CA/FL wording).

Round 3 is the last; a FAIL there escalates to a human.
