# BE-compliance — Stage 10 QA Cross-Check, FINAL 2

**Date** 25 August 2026
**Supersedes** `BE-QA-REPORT-FINAL-2026-08-24.md`, which was written before the fixes of 24–25
August and was stale within minutes of being saved.
**Scope** Full Stage 10, all 9 checks, re-run after: the items 4/5/6/7/8 task force, the
back-porting of every generator, the Report Matrix version correction, the WTC Form Reference Guide
correction and the BE-X10-009 residual close.

**Method.** Every figure below was measured live against the files on disk in this session with
`openpyxl`, `python-docx` and raw-zip inspection. **Nothing is carried over** from
`BE-QA-REPORT-FINAL-2026-08-24.md`, from `handover_status.md` or from the task brief — including
that brief's own claims about which findings were already closed, all of which were re-tested.
Where a prior figure was reproduced it is marked **confirmed**; where it was not, the measured value
is given.

---

## Executive summary

### **9 of 9 checks pass. The single FAIL carried by the previous report is closed.**

| # | Check | Previous (24 Aug) | **This run** |
|---|---|---|---|
| 1 | CCG ↔ WTC alignment | PASS (1 MINOR) | **PASS** |
| 2 | CCG ↔ DD alignment | PASS | **PASS** |
| 3 | CCG ↔ Report Specs (9) | PASS | **PASS** |
| 4 | DD ↔ Report Specs, 4-bucket (9) | **FAIL — 1 MAJOR, 2 MINOR** | **PASS** |
| 5 | Global WTC coverage audit | PASS | **PASS** |
| 6 | Scope discipline (DD/WTC/CCG) | PASS (1 MINOR) | **PASS** |
| 7 | Report Spec format compliance (9) | PASS 9/9 | **PASS 9/9** |
| 8 | Format / version standards | PASS (3 MINOR) | **PASS** — 5 real mismatches found *and fixed* this run |
| 9 | Composite key / inter-field | PASS | **PASS** |
| — | **NEW: generator reproducibility** | not checked | **PASS 13/13** |

**The headline is the new check.** Stage 10 had never asked whether the *build scripts* still
produce the artefacts being audited. They did not. Eleven artefacts differed from their generator
output by **8,703 cells**; a rebuild would have reverted every correction made since 14 August,
including several this very report was about to certify. That is now 0, with a permanent gate.

**Readiness: not yet closable, and for narrower reasons than before.** No check fails. What blocks
closure is (a) the payslip has no working verifier at all, (b) three small open defects in delivered
files, and (c) `L-15` — nothing has ever been submitted through a live channel.

---

## Artefacts read

| Artefact | Path | State |
|---|---|---|
| CCG | `01-ccg/BE-CCG-001-v1.1.docx` | 313,515 chars of text; zip 19/19 parts, integrity OK |
| Report Specs | `04-reports-spec/` | 9 files, all 9 sheets, correct order |
| DD | `05-data-dictionary/BE-DD-001-v1.3.xlsx` | zip 49/49 parts, integrity OK |
| WTC | `02-wtc/BE-WTC-001-v1.0.xlsx` | zip 23/23 parts, integrity OK |
| SIR | `03-statutory-integrations/BE-SIR-001-v1.0.docx` | present |
| Payslip | `06-payslip/BE_Compliance_Payslip_Generator.xlsx` | zip 34/34 parts, integrity OK |
| scope_manifest | `scope_manifest.json` | valid JSON, `scope_version` 2.3, 14 revision entries |
| Global WTC | `shared/Global_WTC_V1_0.xlsx` | 300 baseline codes |

`*DRAFT*` files outside `Archived/`: **0** — confirmed.

---

## Check 1 — CCG ↔ WTC · **PASS**

- 359 wage types on the catalogue; column A carries a Mercans Code on all 359 (was 0 on rebuild —
  see the generator check).
- Tax Code column: 24 distinct values = **23 Belcotax box codes + NA**. Confirmed.
- CCG version strings anywhere in the WTC: **`v1.1` only**. No stale `v1.0`.
- DD version strings in the WTC: **`v1.3` only**.
- Cross-artifact fact consistency (C32) over 8 load-bearing figures — GMMI 2,233.61, employee rate
  13.07%, CO2 coefficient 1.6291, high-wage cap 86,700, work-bonus cap 3,523.92, departure holiday
  pay 15.34%, CO2 multiplier 4.00, fiscal work-bonus cap 765. Each appears in 2–5 artefacts.
  **Zero contradictions; no near-variant found anywhere.**

## Check 2 — CCG ↔ DD · **PASS**

- CCG version strings in the DD: **`v1.1` only**.
- 13 distinct `CCG Module n.n` references; **none points to a module number above 13**.
- `verify_be_dd.py`: **PASS** — 272 DD fields, 1,191 spec rows classified, **0 unclassified**,
  0 DD-bucket fields missing, 0 orange columns populated, 0 C29 markers, 0 WTC name collisions.

> Fixed during this run: 8 spec fields added by the 24-Aug ISSUE-B pass had never been added to
> `dd_crosscheck_map.py`, so C1 was failing. Six FEDRIS accident-narrative fields, `Subdivision
> Usage`, and the two NSSO-004 benefit-in-kind period dates, all classified `TX` on the map's own
> per-event convention.

## Check 3 — CCG ↔ Report Specs · **PASS**

**50** CCG citations across the nine specs — Dimona 2, DmfA 14, DmfA-Mod 1, DRS 3, FEDRIS 1,
Finprof 1, Belcotax 1, SEPA 1, Limosa 26. **All at `v1.1`. Zero stale `v1.0` citations.**

## Check 4 — DD ↔ Report Specs · **PASS** *(was the sole FAIL)*

| Measure | Value |
|---|---|
| Structured DD citations in column L, all nine specs | **521** — confirmed |
| Version cited | **`v1.3` on all 521.** Zero at any other version |
| Distinct DD field names cited | **163** |
| **Broken citations** (name absent, or on a different sheet than cited) | **0** |

**The MAJOR is closed.** The previous report failed this check because the v1.1→v1.3 promotion
widened the *Days Justification* domain (NSSO zone 00625) to codes 1–7 while three specs still
published a truncated 5-code French domain and a `NOT FOUND`. Measured now: all three specs that
carry the zone — BE-NSSO-002, BE-NSSO-003, BE-NSSO-004 — state the **complete 1–7 domain**,
attributed to the DD option mapper. The verbatim French source quote is retained and explicitly
labelled as cut off inside value 5, which is the right treatment: the source is quoted honestly and
the resolved domain is given beside it rather than in place of it.

> One correction to the previous report's framing, worth recording because it bears on how the
> finding was worded. The claim that "203 field names" were written in the 21-Aug pass is a
> mis-count of category, not of quantity: **203 is the number of rows that gained a citation**
> (226 rewritten − 23 reclassified = 203, which reconciles exactly), written using **75** distinct
> field names. Corrected in the WTC this run.

## Check 5 — Global WTC coverage · **PASS**

- Baseline: **300** Pay Element Codes in `shared/Global_WTC_V1_0.xlsx`.
- Present in WTC catalogue column A: **300 of 300. Zero missing.**
- Present on the `Global WTC Coverage` sheet: **300 of 300. Zero missing.** (373 code rows total —
  300 baseline + 59 Belgium-specific `BE-001`…`BE-059`, plus header/section rows.)

The CRITICAL fix held. Note this check would have started failing on the next rebuild: the WTC
generator emitted column A as empty on all 359 rows, which would have destroyed the join key this
check depends on.

## Check 6 — Scope discipline · **PASS**

- `scope_version` **2.3**; **17** consolidated `known_limitations`.
- `integrations.outbound` **18** entries, crosswalked to the SIR by `sir_flow_id`.
  **OUT-08 is the only SIR outbound flow absent, and the manifest states in terms that this is
  deliberate** — Limosa is descoped by owner ruling; BE-SCOPE-014 closed.
- `integrations.inbound` 18 entries.
- **10** filings in `authority_filings.out_of_scope`, including both Limosa entries
  (`BE-NSSO-LIMOSA-009`, `BE-NSSO-LIMOSA-L1-VERIFY`).
- The Limosa spec carries its DESCOPED banner at `Report Matrix!A2` and is marked descoped in its
  Report Matrix, Payroll Scope Summary and Version Control.

## Check 7 — Report Spec format compliance · **PASS 9/9**

All nine: **9 sheets, in contract order, 21 columns on sheet 4**. `verify_specs.py` — **9/9 PASS**,
zero errors.

> Two gate defects fixed to get an honest result here, both cases of a check asserting a superseded
> state:
> - **C6** required Version Control to still say *"the Data Dictionary does not exist"*. It has
>   existed since 14 August. Eight of nine specs were failing **for being correct**; BE-FEDRIS-001
>   passed only by coincidence, on an unrelated sentence about accident data that "does not exist in
>   a payroll system". C6 now asserts the current contract — the DD is named, with the BE-DD-001
>   version aligned against.
> - **C7** on BE-NSSO-005: rows 15/17/18 answered `NO` in green while row 16 — same answer, same
>   block — was red. Corrected to red per the documented convention.

## Check 8 — Format / version standards · **PASS**

| Spec | Version Control | Report Matrix | |
|---|---|---|---|
| BE-FEBELFIN-001 | 1.2 | 1.2 | OK |
| BE-FEDRIS-001 | 1.3 | 1.3 | OK |
| BE-FIN-001 | 1.2 | 1.2 | OK |
| BE-FIN-002 | 1.2 | 1.2 | OK |
| BE-NSSO-001 | 1.3 | 1.3 | OK |
| BE-NSSO-002 | 1.3 | 1.3 | OK |
| BE-NSSO-003 | 1.3 | 1.3 | OK |
| BE-NSSO-004 | 1.3 | 1.3 | OK |
| BE-NSSO-005 | 1.3 | 1.3 | OK |

**Five real mismatches were found and fixed during this run.** The 24-Aug ISSUE-B pass bumped
Version Control to v1.3 on five specs but left `Report Matrix!B17` at `1.2` in all five. The
previous report recorded this check as PASS with three MINORs and did not catch it.

Consequential downstream: the WTC `Form Reference Guide` still described the set as *"eight at
v1.2"*. Actual: three at v1.2, five at v1.3, one descoped at v1.3. Corrected. The SIR already
carried the correct statement, which is how the discrepancy was isolated.

## Check 9 — Composite key / inter-field · **PASS**

The DmfA worker-record composite key is stated where it belongs — in the DD, at
`Country Fields!G22`: the contribution worker code *"is the primary key of the DmfA worker record
together with the employer category"*. The specs reach it by citation rather than restating it,
which is the correct single-source arrangement. Join-key statements present in all nine specs.

## C29 residual-marker lint · **0 markers**

Across all nine specs, the DD, the WTC, the payslip, the CCG and the SIR: **zero** occurrences of
`TODO`, `TBD`, `FIXME`, `XXX`, `placeholder`, `to be confirmed`, `to be verified`.

## NEW — Generator reproducibility · **PASS 13/13**

| Artefact | Differing cells before | After |
|---|---|---|
| 9 Report Specs | **4,604** | **0** values, **0** fills |
| BE-DD-001 | **3,711** | **0** values (70 cosmetic fills, documented) |
| BE-WTC-001 | **382** | **0** |
| BE-SIR-001 | 6 | **0** |
| BE-CCG-001 | 0 | 0 |
| **Total** | **8,703** | **0** |

Gate: `_pipeline/verify_generators.py`. Runs every generator into a temporary directory, diffs
values *and* fills, exits non-zero on drift, and cannot write to a delivered file.

**One documented tolerance.** BE-DD-001 Country Option Mappers: 14 of the 86 **empty** separator
rows carry a residual background fill that the generator does not reproduce; the other 72 are
unfilled, so the delivered file is internally inconsistent here. No cell content differs. Recorded
in the gate's `TOLERANCES` table with that reason rather than waved through.

---

## Two reported defects that do not exist

Both were on the pending list, both were checked in full, and neither is real. Recording them so
they are not re-raised a third time.

**The "1-cent arithmetic error" in CCG Module 9, Step 7.** There is none.
`1,303.95 × 53.50% = 697.61325`, so **697.61 is correct**; the reported 697.42 is not derivable from
any stated input — no rate or base in the example produces it. The whole worked example was
re-derived independently: notice period, current remuneration, indemnity, outplacement deduction,
social security, withholding at the nr. 58 rate, the other settlement items, both summary tables and
the definitive taxation. **Every figure reconciles**, including all four column totals and the
net-of-gross identity. An arithmetic lint over all 148 CCG tables and every inline equation returned
no genuine hit. **No change made.**

**The unverifiable "nr. 53/58" citation in CCG Modules 4 and 11.** The string `53/58` occurs
**zero** times in the CCG, and **no** `nr. 53` / `nr. 58` citation appears in Module 4 or Module 11.
Where nrs. 53, 58, 60 and 62 do appear — Modules 1, 6 and 9 — they cite **Annex III to the Royal
Decree implementing ITC 92**, the FPS Finance withholding-tax scales annex, which genuinely is
published in numbered points. The research pass that could not confirm them searched NSSO/ONSS
instructions, circulars and annexes: the wrong authority, which is why it found nothing.

Verified against an independent live source this run: Annex III points 58–63 carry the withholding
scale for arrears and notice indemnities, and point 62 determines the notice-indemnity percentage on
*the remuneration that served as the basis for setting the indemnity* — which is precisely what CCG
Module 9 says and what its worked example does. **The citations are correct and were not removed.**

Removing them and substituting the proposed DmfA remuneration codes would have replaced a correct
**tax** authority with an unrelated **social-security** one: nrs. 53/58/62 govern the withholding
*percentage*; codes 3/9, contribution code 812 and the quarter-allocation chapters govern how
severance is *declared and contributed*. They are not substitutes.

### The real gap that sits behind it

The CCG documents severance's **tax** treatment thoroughly and its **social-security declaration**
treatment only generically. Absent from the whole corpus: DmfA remuneration codes **3** and **9**
(both **confirmed** against the live ONSS administrative instructions this run), the closure-fund
worker-contribution code **812** in block **90001** (**not** corroborated — the ONSS end-of-contract
page does not carry it, so it needs its own source before anyone writes it down), and the
severance-specific quarter-allocation and modification rule. **Routed to
`compliance-source-hunter` as new authoring, not as a citation fix.**

---

## Open items — none of which fails a Stage 10 check

| id | Artefact | Item | Owner |
|---|---|---|---|
| T-05 | Payslip | `_verify_payslip.py` aborts with `NameError: IFERROR` — its formula evaluator does not implement `IFERROR` and the workbook uses it in 2 cells. **The payslip is the only artefact with no working gate.** It also resolves paths from the repo root, not `__file__`. | tooling |
| BE-TF-008 | DD | Changelog gaps: v1.2 has no description, status **or** author; v1.3 has no author. Reproduced faithfully rather than papered over. | builder |
| BE-TF-009 | Specs | 7 `Sample File` header lines beginning `===` are stored as **formula** cells; Excel renders `#NAME?`. | builder |
| BE-TF-010 | SIR | §2 preamble and gap G27 say "eleven … are governed"; §2.3 says "ten … by a *live* spec (10 live + 1 descoped + 8 none)". Reconcilable via *live*; both readings sit in one document. | judgment |
| BE-X10-010 | WTC | `YTD Load` (col S) empty on all 359 rows. Column S is orange. Column A is *also* orange and is populated, deliberately and on the record — so "orange" alone does not settle it. **Needs an owner's word, not a builder's.** | owner |
| BE-X10-006 | corpus | Originally "6 cells across 3 artifacts". The corpus holds **478** `NOT FOUND`-bearing cells across 12 workbooks against **17** consolidated `known_limitations` entries. Registration is by consolidated entry, so no cell-level coverage figure is computable and the original 6 cannot be re-identified. **Re-scope before working.** | auditor |
| L-05 … L-10 | various | Sourcing limitations. `L-05`, the work-bonus annual cap after the 1 July 2026 indexation, is marked `NOT FOUND` in the CCG with an explicit *do not extrapolate it*. | source hunter |
| L-15 | — | **No filing has ever been submitted through any channel.** This is what holds every accuracy band below 95%, and no desk verification moves it. | — |

---

## Verdict

**All 9 Stage 10 checks PASS, plus the new generator-reproducibility check at 13/13.**

All 6 blockers and 10 of the 11 majors carried by the 17 August handover are closed, each
re-verified against the live artefacts in this run rather than accepted from the prior report.

**Belgium is not yet ready for final handover** — but for none of the reasons Stage 10 tests. The
gaps are: one artefact with no working verifier (T-05), three small defects in delivered files
(BE-TF-008/009/010), two findings needing an owner or a re-scope (BE-X10-010, BE-X10-006), the
outstanding sourcing limitations, and `L-15`.

**This report is current as at the moment of writing**, which the one it supersedes was not. To keep
it that way, `_pipeline/verify_generators.py` and the four artefact gates should be run together
after every future change — the generator gate in particular, because it is the only one that can
see a fix being silently undone.
