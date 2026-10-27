# BELGIUM PAYSLIP — REFORMAT TO COLOMBIA'S VISUAL MODEL

Run this locally on F5A4T8E, via Claude Code. Goal: `06-payslip/
BE_Compliance_Payslip_Generator.xlsx`'s two visual sheets (`Belgium (EN)`,
`Belgium (NL)`) get Colombia's exact visual structure — colors, fonts,
row heights, merge scheme — while every real Belgian data point, formula,
and statutory note is preserved. This is a reformat, not a rewrite of
content. The reference target (Colombia's real row-by-row structure) is
given below in full — extracted directly from `CO_Compliance_Payslip_
Generator.xlsx`, so it doesn't need re-deriving.

## TWO THINGS THAT WENT WRONG THE LAST TIME THIS WAS DONE FOR FRANCE — AVOID THEM FROM THE START

**1. Resetting value/color/font alone is not enough.** The first France
attempt cleared those three but left the OLD column widths, row heights,
and borders in place — text ended up squeezed into a narrow column with
no room, illegible. Column A's width alone isn't the culprit; the fix
is that note rows need `merge A:J + wrap_text + height 30`, and every
other row type needs its own merge pattern (below). Reset and reapply
ALL FIVE properties together — value, font, fill, dimensions, border —
row by row, not fill-then-hope-the-old-geometry-still-fits.

**2. Don't guess which PDF page is the real content.** Page-number
guessing repeatedly landed on "How to set up Payslip" or "Compliance
Payslip" (the two generic front sheets) instead of the actual rebuilt
sheet. After rendering to PDF, extract text and search programmatically
for a real, distinctive Belgian data point (the sample employee's name,
or the NSSO number, or "Mercans Belgium NV") to find the right page —
don't assume a page index.

## COLOMBIA'S EXACT STRUCTURE (extracted from the real file — use this directly)

Row heights 1–6: **12.75, 12.75, 12.75, 12.75, 7.5, 21.75** — matches the
documented Mercans standard exactly, so this is confirmed, not disputed.

| Row(s) | Fill | Font | Merge pattern | Content |
|---|---|---|---|---|
| 1 | — | — | `A1:A6` | Logo anchor spans the whole banner height |
| 3 | — | 10pt bold | `H3:J3` | Title ("Colombia Payslip") |
| 5 | — | — | `J5:J6` | **Net Pay value** cell (large, next to label) |
| 6 | — | 6pt bold | `H6:I6` | "Net Pay:" label |
| 7–10 | `FFDCDCDC` | 6pt (row 8 bold) | 2-cell label+value pairs (`A:B` label, `C:D` value; `G:H`/`I` for a second pair on the same row) | Employer block: Name, Address, Tax ID, Risk Class |
| 12–17 | `FFDCDCDC` | 6pt (row 15 bold) | 4-way split: `A:B` label / `C:D` value / `E:F` label / `G:J` value | Employee block: Name, Code, Years in Service, Tax Month, Days in Month, scheme identifiers |
| 18 | — | — | `A18:J18` | Spacer, **zero border** |
| 19, 36, 46, 54, 58, 65, 71 | `FFA9A9A9` | **7pt bold** | `A:J` full width | Section title rows (Salary Detail, Employer Contributions, Social Benefit Provisions, Banking Details, Contribution & Provision Summary, Year-to-Date, Statutory Notes) |
| 20, 27, 37, 47, 55 | `FFDCDCDC` | 6pt bold | `A:E` + `H:J` | Column-header row within a section ("Payment Item", "Deduction Item", "Contribution Item", "Beneficiary Name") |
| 21–24, 28–31, 38–43, 48–51 | none | 6pt regular | `A:E` + `H:J` | Line-item rows, label left / value right |
| 25, 32, 44, 52 | `FFDCDCDC` | 6pt **bold** | `A:E` + `H:J` | Total rows (Total Earnings, Total Deductions, Total Employer Contributions, Total Provisions) |
| 34 | `FFDCDCDC` | 6pt bold | `A:G` + `H:J` **(wider left merge than other totals)** | Net Pay summary row |
| 26, 33, 35, 45, 53, 57, 64, 70 | none | — | full width, **zero border** | Spacer rows between sections |
| 56 | none | 10pt regular | 4-way split matching row 55 | Beneficiary name value |
| 59–63, 66–69 | none | 6pt regular | `A:E` + `H:J`, height 9.75 | Summary/YTD label+value rows |
| 72–79 | `FFF5F5F5` | **5pt**, height **30** | `A:J`, **wrap_text on** | Statutory notes, one per row |
| 81–83 | none | 6pt / 10pt | partial merges | Footer + reference code |

Two structural facts worth carrying over exactly: (a) the "Total" row merge
is the SAME width as its section's line-item rows (`A:E`+`H:J`) EXCEPT the
final Net Pay row, which widens to `A:G`+`H:J` — don't apply the wider
merge to the other totals by mistake; (b) every note row is individually
merged and heighted — don't merge the whole notes block as one range.

## STEP 1 — READ BELGIUM'S CURRENT CONTENT FIRST, DON'T ASSUME

Before touching anything, read `Belgium (EN)` and `Belgium (NL)` in full
and catalogue every real content item currently present: employer block
fields, employee block fields, every earning/deduction/employer-
contribution line (note which ones combine employee AND employer rates in
one row — those need splitting into two, same as France's approach),
every statutory note's full text, YTD lines, banking details, footer. Do
not lose or shorten any of this — this pass changes layout, not content.

## STEP 2 — MAP BELGIUM'S CONTENT INTO COLOMBIA'S ROW STRUCTURE

Belgium likely has more distinct line items than Colombia's 4 earnings /
4 deductions / 6 employer-contribution rows — that's fine, extend each
section's row count as needed while keeping every row within that
section styled identically to its Colombia counterpart (same fill/font/
merge pattern), not just the first few rows. Any Belgian contribution
row that states employee AND employer rates together splits into two:
one row under Deductions (employee side), one under Employer
Contributions (employer side) — real values preserved on each side, not
duplicated or dropped.

## STEP 3 — RESET AND REAPPLY, ALL FIVE PROPERTIES TOGETHER

For every row: clear and reset value, font, fill, row height AND column
widths (match Colombia's column widths, not Belgium's old ones), and
border, then apply Colombia's scheme for that row type from the table
above. Do this per-row, not as a global find-and-replace that might miss
one property.

## STEP 4 — LOGO AND NET PAY BOX

Confirm the Mercans logo is anchored the same way as Colombia's (`A1:A6`
merge, correct display size — verify via the raw drawing XML `ext`
values, not `openpyxl`'s `.width`/`.height`, which reports native
resolution unreliably). Populate the `J5:J6` Net Pay value cell with a
real formula referencing Belgium's actual net-pay calculation — don't
leave it as a static number or, worse, empty.

## STEP 5 — FIX THE TWO SHEET-LEVEL NAMING ISSUES FOUND EARLIER

While in this file: rename `Payslip Spec` → `Payslip Spec 1`, and
`Unit Rate Details` → `UnitRate Account Details`. On `Payslip Spec 1`,
add the two missing columns after the current last one: **F "Query to
RA"** and **G "RA Comments"** (teal `FF4BACC6` header fill, matching the
sheet's existing header row style) — currently the sheet stops at column
E. Leave rows/existing columns B–E exactly as they are; this is an
addition, not a rewrite of that sheet's content.

## STEP 6 — VERIFY, THE SAME RIGOR AS EVERY OTHER STAGE THIS SESSION

1. Both embedded logo images byte-identical (MD5) before/after.
2. Zero differences on the other 6 sheets (`How to set up Payslip`,
   `Compliance Payslip`, `Field Option`, `Population Range`,
   `UnitRate Account Details`, and the renamed `Payslip Spec 1`'s
   original B–E content).
3. `recalc.py` on the file, zero formula errors.
4. Merge-overlap check across both visual sheets.
5. Render to PDF, extract text, search for a real Belgian data point
   (not a guessed page number) to locate `Belgium (EN)` and
   `Belgium (NL)`'s actual pages, then look at both rendered images —
   confirm legible, no squeezed text, Net Pay box shows a real number,
   section colors match the table above.

Don't declare this done until all five checks pass on the actual saved
file — this exact checklist is what caught the France session's bugs
(oversized/misaligned elements, blank borders) only at the visual-render
step, not at the cell-value-check step.

## OUTPUT

Report back: Step 1's content catalogue (brief), which rows needed
splitting (employee/employer combined → two rows) and how many, Step 6's
five verification results including the two rendered page images'
descriptions, and confirm the Net Pay box shows a real computed value in
both languages.
