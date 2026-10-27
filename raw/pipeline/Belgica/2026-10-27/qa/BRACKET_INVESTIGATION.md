# Belgian Annex III withholding bracket ceilings, income year 2026 — investigation

**Status:** INVESTIGATION ONLY. No file in `01-ccg/` or `02-wtc/` was modified.
**Date of investigation:** 14 August 2026
**Question:** every tax calculation in the CCG and WTC uses the ceilings 16,720 / 29,510 / 51,070 inside the *bedrijfsvoorheffing* formula. Does Annex III use its own, separately set ceilings, and if so what changes?
**Predecessors:** `ALLOWANCE_INVESTIGATION.md` (the 11,170 / 11,550 split) and `CHILDREN_SUPPLEMENT_INVESTIGATION.md`, whose §6(a) first flagged this defect and instructed that it be given its own pass.

---

## 1. Bottom line

**Confirmed from the primary text, and independently corroborated.** Annex III nr. 31 sets its own base scale. The ceilings are **16,710 / 29,500 / 51,050**, not the assessment ceilings 16,720 / 29,510 / 51,070 that the CCG and WTC use everywhere.

The **rates are genuinely the Annex III rates** — 26.75% / 42.80% / 48.15% / 53.50% appear verbatim in nr. 31. They are *not* the assessment rates: the assessment rates are 25 / 40 / 45 / 50%, and the withholding rates are those uplifted by exactly 7%. So the CCG has the rates right and the ceilings wrong, in both directions at once (§3).

**Scope of the defect is wider than "the tax examples".** Because Annex III **nr. 108** computes the scale III basisbelasting from the same nr. 31 scale, the non-resident example is affected too. Nine worked examples across Modules 6, 9 and 12 change; one (m12 E2) is insulated.

**The effect is small but systematic.** Taken alone, the bracket correction moves the monthly withholding by **+EUR 0.13 to +EUR 0.18** for an employee reaching the third slice. Combined with the two already-scoped fixes (allowance 11,170 and the nr. 38 child table) the net movement is **+EUR 0.36 to +EUR 0.40 per month** for childless employees and **−EUR 6.39 to −EUR 21.01** where children are involved.

**Task 3 answers, both negative — and that is the useful result:**

| Instrument | Shares the ceiling-mismatch defect? | Why |
|---|---|---|
| **Module 8 holiday-pay table** | **No.** Correct, verbatim | Its thresholds *are* Annex III nr. 53 thresholds. There is no assessment-side counterpart to carry across. The CCG even reads the correct *column* of a two-column table |
| **Module 5 special social security contribution** | **No.** Correct, verbatim | Not in Annex III at all. An NSSO levy under art. 106 of the Law of 30 March 1994, with its own fixed quarterly EUR bands. Matches the NSSO 2026/2 instructions to the cent |

**One major adjacent defect was surfaced.** Module 9 withholds the notice indemnity from the *wrong Annex III table* — nr. 53 (53.50%) instead of nr. 58 (38.96%), a EUR 5,766.20 overstatement on a single worked example. Annex III nr. 53 expressly excludes severance. See §6(a). This is bigger than the bracket issue itself.

Confidence: see §7.

---

## 2. Task 1 — the Annex III base scale, all four bands

### 2.1 Source

Same machine-readable source as `CHILDREN_SUPPLEMENT_INVESTIGATION.md`: the coordinated Annex III as replaced by the **Royal Decree of 11 December 2025** (BS 29.12.2025, p. 97613), retrieved as `Bijlage-III-KB-WIB-2026.pdf` from Securex. 44 pages, first line *"Bijlage bij het Koninklijk besluit van 11 december 2025"*, text layer extracted with `pdfplumber` — 131,195 characters, fully clean.

The scale sits in **Deel 2, Hoofdstuk 1, nr. 31**, one page before the nr. 32 allowance provision that the predecessor investigations already relied on.

### 2.2 The scale, verbatim

> **DEEL 2. DE JAARLIJKSE BASISBELASTING**
> **HOOFDSTUK 1. DE BASISSCHAAL**
> **31.** De belasting wordt berekend met behulp van onderstaande basisschaal.
>
> | JAARLIJKS NETTOBEDRAG VAN DE BELASTBARE GRONDSLAG | BASISBELASTING |
> |---|---|
> | van 0,01 EUR tot 16.710 EUR | 26,75 pct. |
> | van 16.710,01 EUR tot 29.500 EUR | 4.469,93 EUR + 42,80 pct. op de schijf boven 16.710 EUR |
> | van 29.500,01 EUR tot 51.050 EUR | 9.944,05 EUR + 48,15 pct. " " 29.500 EUR |
> | boven 51.050 EUR | 20.320,38 EUR + 53,50 pct. " " 51.050 EUR |

All four bands, as requested. The fourth band — **above EUR 51,050, EUR 20,320.38 + 53.50%** — is not stated anywhere in the CCG in its Annex III form; the CCG gives only "53.50% on the slice above 51,070", which omits the cumulative constant a payroll engine needs.

### 2.3 Internal proof that the ceilings are read correctly

The three published cumulative constants reproduce **exactly** from these ceilings, and only from these ceilings:

| Constant | Derivation | Result |
|---|---|---|
| 4,469.93 | 16,710 × 26.75% = 4,469.925 | → **4,469.93** ✅ |
| 9,944.05 | 4,469.93 + 42.80% × (29,500 − 16,710) = 4,469.93 + 5,474.12 | → **9,944.05** ✅ |
| 20,320.38 | 9,944.05 + 48.15% × (51,050 − 29,500) = 9,944.05 + 10,376.325 | → **20,320.375 → 20,320.38** ✅ |

A transcription error in any ceiling would break this chain. The two half-cent cases (4,469.925 and 20,320.375) both round **up**, which is exactly what Annex III **nr. 12** requires — see §2.5.

Recomputing the same three constants from the CCG's ceilings gives 4,472.60 / 9,946.72 / 20,331.02 — none of which appears in the annex.

### 2.4 Independent corroboration — the residual gap from CHILDREN §7 is now closed

`CHILDREN_SUPPLEMENT_INVESTIGATION.md` §7 left open that the annex had been read from Securex's reproduction rather than the Staatsblad. Two independent houses confirm the scale:

- **SYNOVA**, *Bedrijfsvoorheffing* reference page, income year 2026: brackets **0.01–16,710.00 at 26.75%; 16,710–29,500 at 4,469.9x + 42.80%; 29,500–51,050 at 9,944.05 + 48.15%; above 51,050 at 20,320.38 + 53.50%**, and *belastingvrije som* **11,170.00**. Every ceiling and two of three constants match the annex exactly. (SYNOVA renders the first constant as 4,469.96; the arithmetic 16,710 × 26.75% = 4,469.925 and the annex text both give **4,469.93**, so this is a typo on SYNOVA's side and the annex governs.)
- **Securex**, *Bedrijfsvoorheffing achterstallen en opzegvergoedingen* reference page: reproduces the nr. 58 table (§6(a)) across all 18 bands with figures identical to the PDF, confirming the PDF is a faithful reproduction of the annex generally.

Two houses, one primary text, and an internal arithmetic proof. The scale is settled.

### 2.5 The rounding rule — also found, and it matters

Annex III **nr. 12** (Deel 1, Hoofdstuk 1, Afdeling 5. *Afronding*), verbatim:

> **12.** Voor de toepassing van deze volledige bijlage, met inbegrip van nrs. 4 en 11 hierboven, worden alle bedragen, in voorkomend geval **in elke stap**, afgerond tot de hogere of lagere cent, naargelang het cijfer van de duizendsten al dan niet 5 bereikt.

Round to the cent **at every step**, half-up. This is a primary-source basis for the CCG's stated convention ("rounding is to the eurocent at each presented line", `m12_examples.md:5`) — that convention is correct and should be kept. All recomputations in §5 apply it.

### 2.6 ⚠️ No rounding rule derives these ceilings — do not pattern-match

`ALLOWANCE_INVESTIGATION.md` §4.1 established that the withholding allowance is the assessment allowance rounded *down* to the lower 10. **That convention does not generalise to the brackets, and anyone applying it here would get two of three ceilings wrong.**

Art. 130 WIB 92 bases indexed at coefficient 2.0592 (BS 12 Aug 2026, Table III A):

| Base | Unrounded | Assessment (nearest 10) | Round *down* to lower 10 | **Annex III actual** | Rule works? |
|---|---|---|---|---|---|
| 8,120 | 16,720.704 | 16,720 ✅ | 16,720 | **16,710** | ❌ |
| 14,330 | 29,508.336 | 29,510 ✅ | 29,500 | **29,500** | ✅ |
| 24,800 | 51,068.160 | 51,070 ✅ | 51,060 | **51,050** | ❌ |

The convention reproduces one ceiling out of three. Nor does any single coefficient fit: 16,710/8,120 = 2.05788, 29,500/14,330 = 2.05862, 51,050/24,800 = 2.05847 — three different values.

**Conclusion: the Annex III ceilings are set in the annex and are not derivable.** They must be read from nr. 31 each year. This is the strongest form of the predecessor investigations' central thesis, and it is precisely why the instruction not to estimate by pattern was the right one — a pattern estimate would have produced 16,720 / 29,500 / 51,060, wrong in two places.

---

## 3. Task 2 — are the rates the Annex III rates?

**Yes. Explicitly and unambiguously.** 26,75 / 42,80 / 48,15 / 53,50 pct. appear in the nr. 31 table quoted at §2.2. They are Annex III's own withholding rates.

**They are not the assessment rates.** The two instruments differ on the rates as well as the ceilings, but in a way that is easy to miss because the relationship is exact:

| Slice | Art. 130 WIB 92 — assessment rate | Annex III nr. 31 — withholding rate | Relationship |
|---|---|---|---|
| 1 | 25% | **26.75%** | 25 × 1.07 |
| 2 | 40% | **42.80%** | 40 × 1.07 |
| 3 | 45% | **48.15%** | 45 × 1.07 |
| 4 | 50% | **53.50%** | 50 × 1.07 |

The 7% uplift is the notional stand-in for the regional and municipal surcharges. `m06_tax.md:25` states this correctly and needs no change.

**The precise answer to the question as posed:** the rates do **not** "match between the two instruments" in the sense of being the same numbers — 26.75% is not an assessment rate anywhere. They match in the sense of being *derived* from the assessment rates by a fixed, exact multiplier. So the situation is the mirror image of what the ceilings do:

- **Rates** — different raw numbers, deterministic relationship (× 1.07), and the CCG has them right.
- **Ceilings** — nearly identical numbers, *no* deterministic relationship, and the CCG has them wrong.

That asymmetry is the trap. The rates look like they were carried across from the assessment side and were not; the ceilings look independently sourced and were not.

**What is correct and must not be touched:** `m06_tax.md:172–177` presents "Personal income tax scale — income year 2026, assessment year 2027" at 25 / 40 / 45 / 50% on 16,720 / 29,510 / 51,070. That is the **assessment** scale, it is right, and `ALLOWANCE_INVESTIGATION.md` §2.2 verified it against BS 12 August 2026.

**What is wrong is the sentence immediately after it.** `m06_tax.md:181`:

> **Withholding scale actually used in payroll** — the same slices at 26.75%, 42.80%, 48.15% and 53.50%.

"**The same slices**" is the defect, stated in four words. The rates in that sentence are right; the claim that the slices are shared is false.

---

## 4. Task 3 — Module 8 and Module 5

### 4.1 Module 8, the holiday-pay table — CORRECT, and better than expected

The double-holiday-pay table is Annex III **nr. 53** (Deel 3, Hoofdstuk 6, Afdeling 1, Onderafdeling 1). It is a **two-column** table: one column for *vakantiegeld*, one for *andere vergoedingen en toelagen*. Both share one set of ten thresholds.

Column order was established positionally from the PDF (word x-coordinates), not from the flattened text, because the flattened header interleaves the two column captions and reads misleadingly. The header `VAKANTIEGELD` sits at x≈317 and `ANDERE VERGOEDINGEN EN TOELAGEN` at x≈404–444; the two data columns sit at x≈338 and x≈447 respectively. So the **left** percentage column is holiday pay and the **right** is other allowances.

| Annual normal gross remuneration | nr. 53 — **VAKANTIEGELD** | nr. 53 — **ANDERE VERG. EN TOELAGEN** | `m08:96–106` | `m04:324–334` |
|---|---|---|---|---|
| tot 10.675 EUR | 0 | 0 | 0.00% ✅ | 0.00% ✅ |
| 10.675,01 – 13.660 | 19,17 | 23,22 | 19.17% ✅ | 23.22% ✅ |
| 13.660,01 – 17.375 | 21,20 | 25,23 | 21.20% ✅ | 25.23% ✅ |
| 17.375,01 – 20.840 | 26,25 | 30,28 | 26.25% ✅ | 30.28% ✅ |
| 20.840,01 – 23.580 | 31,30 | 35,33 | 31.30% ✅ | 35.33% ✅ |
| 23.580,01 – 26.340 | 34,33 | 38,36 | 34.33% ✅ | 38.36% ✅ |
| 26.340,01 – 31.830 | 36,34 | 40,38 | 36.34% ✅ | 40.38% ✅ |
| 31.830,01 – 34.640 | 39,37 | 43,41 | 39.37% ✅ | 43.41% ✅ |
| 34.640,01 – 45.860 | 42,39 | 46,44 | 42.39% ✅ | 46.44% ✅ |
| 45.860,01 – 59.900 | 47,44 | 51,48 | 47.44% ✅ | 51.48% ✅ |
| boven 59.900 | 53,50 | 53,50 | 53.50% ✅ | 53.50% ✅ |

**Every threshold and every percentage is correct in both modules, and each module reads the correct column.** Module 8 takes the holiday-pay column, Module 4 takes the other-allowances column. `m12:197`'s observation that the holiday-pay table is "materially more favourable than the exceptional-payment table at the same reference wage — 42.39% against 46.44%" is a correct reading of the two columns.

**Why no mismatch is possible here.** These thresholds have no assessment-side counterpart to be confused with. At assessment, exceptional remuneration is taxed under art. 171 WIB 92 at an average rate, not from a percentage table. There is only one instrument, so there is nothing to carry across. `m06_tax.md:245` ("the tables themselves begin at 0.00% for an annual gross reference remuneration up to EUR 10,675.00") is also correct.

### 4.2 Module 5, the special social security contribution — CORRECT

The *bijzondere bijdrage voor de sociale zekerheid* is not in Annex III. It is an NSSO levy under **art. 106 of the Law of 30 March 1994**, banded on the **quarterly wage**, with fixed euro thresholds published in the NSSO administrative instructions.

`m05_social_security.md:116–125` against the NSSO 2026/2 instructions:

| Quarterly wage W | CCG `m05:118–123` | NSSO 2026/2 | |
|---|---|---|---|
| Up to 5,836.14 | nil (+ fixed withholding) | 5,836.14 band start | ✅ |
| 5,836.15 – 6,570.54 | 4.22% × (W − 5,836.14) | 4.22% | ✅ |
| 6,570.55 – 11,211.00 | 30.99 + 1.10% × (W − 6,570.54) | 30.99 + 1.10% | ✅ |
| 11,211.01 – 12,300.00 | 82.05 + 3.38% × (W − 11,211.00) | 82.05 + 3.38% | ✅ |
| 12,300.01 – 18,116.46 | 118.83 + 1.10% × (W − 12,300.00) | 118.83 + 1.10% | ✅ |
| Above 18,116.46 | 182.82 (maximum) | 182.82 | ✅ |
| Jointly assessed, spouse with income | 15.45 fixed from 3,285.29; 43.32 + 1.10% above 6,570.54; max 154.92 (`m05:125`) | 3,285.29 / 15.45 / 43.32 / 154.92 | ✅ |

Every threshold, every percentage, every fixed amount and both maxima match. The four applications of the table in the worked examples are also arithmetically correct — spot-checked: `m06:322` W = 12,000 → 82.05 + 3.38% × 789.00 = 108.72 ✅; `m12:27` W = 10,500 → 30.99 + 1.10% × 3,929.46 = 74.21 ✅; `m12:181` W = 14,896 → 118.83 + 1.10% × 2,596 = 147.39 ✅.

**A provisional/definitive split does exist for this levy** — it is withheld provisionally each quarter and finally settled through the tax assessment, which the CCG itself states at `m06:308` and `m05:227`. So the *structure* that produced the Annex III defect is present. But payroll needs the quarterly withholding table, and that is the table the CCG uses. **The CCG is on the correct side of the split.**

⚠️ Two things not established in this pass, neither of which affects the answer: (i) whether these amounts are indexed annually or are fixed converted-BEF figures — the NSSO page fetch asserted annual indexation, which sits oddly with amounts that have been stable for years; (ii) the definitive annual scale used at assessment. Neither is needed for payroll. `m05:127` already carries a live warning that the announced reform of this contribution is unconfirmed; that warning stands and is outside this investigation.

---

## 5. Downstream impact inventory — scoping only, not applied

### 5.1 Statements of the ceilings (text edits, no arithmetic)

| Location | Current text | Change |
|---|---|---|
| `m06_tax.md:128–131` | formula step 6 — "26.75% on the slice 0 – 16,720 / 42.80% … 16,720 – 29,510 / 48.15% … 29,510 – 51,070 / 53.50% … above 51,070" | → 16,710 / 29,500 / 51,050. Consider adding the cumulative constants 4,469.93 / 9,944.05 / 20,320.38, which the annex publishes and payroll needs |
| `m06_tax.md:181` | "**Withholding scale actually used in payroll** — **the same slices** at 26.75%, 42.80%, 48.15% and 53.50%." | **Cannot be repaired by substitution.** The claim of shared slices must go; replace with the Annex III scale stated in full, alongside the assessment scale at 172–177 |
| `m12_examples.md:5` | preamble — "withholding scale slices of 26.75% to EUR 16,720, 42.80% to EUR 29,510, 48.15% to EUR 51,070 and 53.50% above" | → 16,710 / 29,500 / 51,050 |
| `02-wtc/be_wtc_data_part7.py:59` | "26.75% on 0-16,720; 42.80% on 16,720-29,510; 48.15% on 29,510-51,070; 53.50% above 51,070" | → same; rebuild WTC after edit |

**Not to be changed:** `m06_tax.md:172–177` (the art. 130 assessment scale, correct) and `m06_tax.md:25` (the 7% uplift explanation, correct).

The WTC carries the ceilings **only as descriptive text** in one file. No computed withholding amounts exist in `02-wtc/`. Unlike the child-supplement ticket, `_prompts/wtc.md` does **not** carry the bracket ceilings, so no upstream prompt fix is required for this defect.

### 5.2 Recomputed worked examples

All figures computed directly from Annex III nrs. 31 → 32 → 38 → 42, applying nr. 12 cent-rounding at each step, holding every non-tax input at the CCG's own values.

Three columns are given deliberately:
- **CCG now** — as written.
- **Brackets only** — this ticket in isolation, allowance and child mechanism left as the CCG has them. Use this to price the bracket fix on its own.
- **FULL fix** — brackets + allowance (2,987.98, `ALLOWANCE_INVESTIGATION.md`) + child table (nr. 38, `CHILDREN_SUPPLEMENT_INVESTIGATION.md`). **This is the figure that should actually land in the artifact**, because all three fixes touch the same lines (§5.4).

| Example | Line | Annual net taxable E | F now | **F correct** | Monthly now | Brackets only | **FULL fix** | Δ full |
|---|---|---|---|---|---|---|---|---|
| m06 §6.1 single, 4,000 | 146–158 | 35,656.40 | 12,906.21 | **12,908.36** | 826.30 | 826.48 | **826.70** | +0.40 |
| m06 §6.1 two children | 162 | 35,656.40 | 12,906.21 | **12,908.36** | 709.71 | 709.89 | **688.70** | −21.01 |
| m06 Ex. 2, scale III, 4,000 | 342–345 | 35,656.40 | 12,906.21 | **12,908.36** | 1,075.52 | 1,075.70 | **1,075.70** | +0.18 |
| m12 E1, 3,500 | 17–26 | 30,440.60 | 10,394.81 ⚠ | **10,396.95** | 617.01 | 617.19 | **617.41** | +0.40 |
| m12 E2, 1,300 | 56–62 | 10,135.52 | 2,711.25 | **2,711.25** | 0.00 | 0.00 | **0.00** | — |
| m12 E3, 4,200 + pension | 80–90 | 37,742.72 | 13,910.77 | **13,912.92** | 874.01 | 874.19 | **874.41** | +0.40 |
| m12 E4, 2,800 + 1 child | 111–120 | 24,668.96 | 7,874.76 ⚠ | **7,876.36** | 298.01 | 298.14 | **291.62** | −6.39 |
| m12 E5A, 3,800 + car | 157–163 | 36,784.88 | 13,449.57 | **13,451.72** | 871.58 | 871.76 | **871.98** | +0.40 |
| m12 E6, blue-collar | 211–220 | 22,997.24 | 7,159.26 ⚠ | **7,160.87** | 283.63 | 283.77 | **283.99** | +0.36 |
| m09 April salary, 4,500 + car 250 | 213 | 43,872.20 | 16,862.12 | **16,864.26** | 1,155.96 | 1,156.13 | **1,156.36** | +0.40 |

⚠ = the CCG's own F total is one cent adrift of its own slice figures, independently of this defect. See §6(c).

**Slice-level detail for the four F-steps the CCG prints in full** (the correct values under nr. 31):

| Example | Slice 1 | Slice 2 | Slice 3 |
|---|---|---|---|
| m06 §6.1 / m06 Ex. 2 | 16,710.00 × 26.75% = **4,469.93** | 12,790.00 × 42.80% = **5,474.12** | 6,156.40 × 48.15% = **2,964.31** |
| m12 E1 | 4,469.93 | 5,474.12 | 940.60 × 48.15% = **452.90** |
| m12 E3 | 4,469.93 | 5,474.12 | 8,242.72 × 48.15% = **3,968.87** |
| m12 E4 | 4,469.93 | 7,958.96 × 42.80% = **3,406.43** | — |
| m12 E5A | 4,469.93 | 5,474.12 | 7,284.88 × 48.15% = **3,507.67** |
| m12 E6 | 4,469.93 | 6,287.24 × 42.80% = **2,690.94** | — |

Note that **slice 2 is EUR 12,790.00 wide on both scales** (29,510 − 16,720 = 29,500 − 16,710), so the line "12,790.00 x 42.80% | 5,474.12" is correct as written in every example and does not change. Only slices 1 and 3 move.

**m06 §6.1 two-children narrative (line 162)** must be rewritten, not renumbered: the mechanism changes per `CHILDREN_SUPPLEMENT_INVESTIGATION.md` §2.2. On the fully corrected basis the childless comparator is 826.70 and the two-child figure is 688.70, so the stated *"monthly saving of EUR 116.59"* becomes **exactly EUR 138.00** = 1,656 ÷ 12.

**m06 Example 2 (scale III) — a case the previous inventories did not reach.** Annex III **nr. 108**: *"De basisbelasting wordt berekend met behulp van de basisschaal opgenomen in nr. 31"*, and **nr. 109** divides by 12 with no reduction. So the non-resident figure moves purely on the brackets: **1,075.52 → 1,075.70**. Two consequential lines:

| Line | Current | Corrected |
|---|---|---|
| 342 Tax on the scale | 12,906.21 | **12,908.36** |
| 344 Annual withholding | 12,906.21 | **12,908.36** |
| 345 Monthly withholding | 1,075.52 | **1,075.70** |
| 347 Net paid | 2,365.44 | **2,365.26** |
| 349 "difference against the resident case is exactly the tax-free allowance reduction — EUR 249.22 per month, or EUR 2,990.65 per year" | 249.22 / 2,990.65 | **249.00 / 2,987.98** |

Line 349 is a genuine identity and stays true after the fix: 1,075.70 − 826.70 = **249.00**, and 249.00 × 12 = **2,987.98** (2,988.00 less the cent-rounding). Worth keeping — it is a good self-check on the corrected figures.

**m12 E2 is fully insulated**, as it was for the allowance fix. Its annual net taxable of 10,135.52 sits below both first-slice ceilings, so F is 2,711.25 on either scale, and the withholding floors at zero under every candidate figure. No line in E2 changes.

**m06 Example 3 (bonus) and Module 8's holiday-pay example are unaffected** by this ticket — they use nr. 53, which §4.1 confirms is correct. (Both are however touched by a separate reference-remuneration inconsistency, §6(b).)

### 5.3 Second-order lines that must follow

| Example | Line | Current | Brackets only | **FULL fix** |
|---|---|---|---|---|
| m06 Ex. 1 net paid | 324 | 2,591.77 | 2,591.59 | **2,591.37** |
| m06 Ex. 2 net paid | 347 | 2,365.44 | 2,365.26 | **2,365.26** |
| m12 E1 net pay | 29 | 2,377.91 | 2,377.73 | **2,377.51** |
| m12 E1 employer-cost ratio sentence | 43 | "EUR 2,377.91 in cash … ratio of about 2.0" | — | **2,377.51** (ratio unchanged at ≈2.0) |
| m12 E3 net pay | 94 | 2,593.45 | 2,593.27 | **2,593.05** |
| m12 E4 net for art. 1409 | 122 | 2,246.53 | 2,246.40 | **2,252.92** |
| m12 E5 net of ordinary remuneration | 189 | 2,431.76 | 2,431.58 | **2,431.36** |
| m12 E5 net paid in quarter-end month | 192 | 4,035.18 | 4,035.00 | **4,034.78** |
| m12 E6 net pay | 222 | 2,120.80 | 2,120.66 | **2,120.44** |
| m09 April salary net | 221 | 2,755.89 | 2,755.73 | **2,755.49** |

**m12 E4 garnishment cascade** — the self-cancelling property holds under every variant, as it did in both predecessor investigations:

| Line | Current | Brackets only | **FULL fix** |
|---|---|---|---|
| 122 Net for art. 1409 | 2,246.53 | 2,246.40 | **2,252.92** |
| 132 Fourth band, 100% | 319.53 | 319.40 | **325.92** |
| 133 Total attachable | 450.73 | 450.60 | **457.12** |
| 137 Net before attachment | 2,246.53 | 2,246.40 | **2,252.92** |
| 140 **Net paid to the employee** | 1,772.91 | 1,772.91 | **1,772.91 — unchanged** ✅ |
| 142 maintenance-debt sentence | 2,246.53 | 2,246.40 | **2,252.92** |

The whole delta lands in the 100%-attachable band in every case. Flag this in the fix ticket so a reviewer does not "correct" line 140.

**m09 Step 8 payout summary** — if only this ticket is applied (severance left at 53.50%, see §6(a) for the larger correction):

| Line | Gross | Employee SS | Withholding now → corrected | Net now → corrected |
|---|---|---|---|---|
| April salary | 4,500.00 | 588.15 | 1,155.96 → **1,156.36** | 2,755.89 → **2,755.49** |
| **Total** (line 225) | 54,381.28 | 7,107.63 | 24,354.33 → **24,354.73** | 22,919.32 → **22,918.92** |

### 5.4 Interaction with the two predecessor tickets — apply as one edit

This fix **collides in the same lines** with both predecessors and must not be applied sequentially:

| Line | Allowance ticket | Child ticket | This ticket |
|---|---|---|---|
| `m06_tax.md:133` (step 7) | ✔ | ✔ mechanism rewrite | — |
| `m06_tax.md:128–131` (step 6) | — | — | ✔ |
| `m06_tax.md:152–158` | ✔ | — | ✔ |
| `m06_tax.md:162` | ✔ | ✔ | ✔ |
| `m12` E1/E3/E5/E6 F-steps and monthly | ✔ | — | ✔ |
| `m12` E4 lines 111–142 | ✔ | ✔ | ✔ |
| `m12_examples.md:5` | ✔ | — | ✔ |

**The FULL-fix column in §5.2 and §5.3 is the authoritative target and supersedes both predecessors' recomputations**, in the same way that `CHILDREN_SUPPLEMENT_INVESTIGATION.md` §5.2 superseded the ⚠-marked rows of `ALLOWANCE_INVESTIGATION.md` §5.2. Specifically:

- `ALLOWANCE_INVESTIGATION.md` §5.2's monthly figures at 11,170 (826.52, 617.24, 874.23, 871.80, 283.86, …) were computed on the **assessment** brackets and are all superseded — each is EUR 0.18 low, except m12 E6 which is EUR 0.13 low.
- `CHILDREN_SUPPLEMENT_INVESTIGATION.md` §5.2's two figures — **688.70** and **291.62** — were already computed on the correct nr. 31 scale and **are confirmed unchanged** by this investigation. They reproduce exactly here.
- `ALLOWANCE_INVESTIGATION.md` §5.2's closing statement that the brackets "are confirmed correct and must **not** be touched" applies only to the art. 130 assessment scale at `m06_tax.md:172–177`. It is wrong as applied to the withholding formula, and `CHILDREN_SUPPLEMENT_INVESTIGATION.md` §6(a) already recorded that correction.

### 5.5 Legal-basis citations

`m06_tax.md:164`, `m06_tax.md:249`, `m12_examples.md:226` and `m09_termination.md:229` cite Annex III generically. When the scale is restated they should cite **Annex III nr. 31** specifically, alongside the existing art. 130 citation for the assessment scale, so that a reviewer can see at a glance that two instruments are in play. The extension to the Royal Decree of 24 July 2026 requested by `ALLOWANCE_INVESTIGATION.md` §5.3 still applies and is unaffected by this ticket (that decree did not touch nr. 31).

---

## 6. Adjacent findings — flagged, NOT resolved

### (a) ⚠️ HIGH — Module 9 withholds the notice indemnity from the wrong Annex III table

This is larger in money terms than the bracket defect and was found by the same read.

`m09_termination.md:203–206` computes the notice indemnity withholding from the **exceptional-payment table** (nr. 53) at the top rate:

> The annual gross reference remuneration is 4,500.00 x 13.92 = EUR 62,640.00, which is above EUR 59,900.00, so the top rate applies:
> `Withholding = 39,657.54 x 53.50% = EUR 21,216.78`

**Annex III nr. 53 expressly excludes severance from its own scope**, in its opening words:

> **53.** Voor **andere** exceptionele vergoedingen en toelagen **dan opzeggingsvergoedingen** die een werkgever […] betaalt […]

and **nr. 62** routes severance to the arrears table instead:

> *Afdeling 3. Opzeggingsvergoedingen.*
> **62.** De bedrijfsvoorheffing wordt vastgesteld volgens de regels van **nrs. 58 tot 60**, met dien verstande dat voor het bepalen van het tarief […] de in aanmerking te nemen referentiebezoldiging die is welke tot grondslag diende voor het vaststellen van de vergoeding […]

The nr. 58 table is an **18-band** schedule topping out at 48.00%, entirely different from nr. 53:

| Referentiebezoldiging | % | | Referentiebezoldiging | % |
|---|---|---|---|---|
| tot 11.860 | 0,00 | | 42.695,01 – 55.355 | 31,30 |
| 11.860,01 – 14.235 | 2,68 | | 55.355,01 – 62.465 | 36,90 |
| 14.235,01 – 15.810 | 6,57 | | **62.465,01 – 71.160** | **38,96** |
| 15.810,01 – 18.980 | 10,77 | | 71.160,01 – 83.020 | 40,93 |
| 18.980,01 – 20.565 | 13,55 | | 83.020,01 – 99.630 | 42,92 |
| 20.565,01 – 22.935 | 16,55 | | 99.630,01 – 124.925 | 44,99 |
| 22.935,01 – 26.885 | 19,17 | | 124.925,01 – 143.905 | 46,47 |
| 26.885,01 – 34.790 | 24,92 | | 143.905,01 – 169.205 | 47,48 |
| 34.790,01 – 42.695 | 29,93 | | boven 169.205 | 48,00 |

Independently confirmed band-for-band by Securex's *Bedrijfsvoorheffing achterstallen en opzegvergoedingen* page.

**Effect on the m09 worked example.** Both candidate reference remunerations land in the same band — the CCG's own 4,500 × 13.92 = 62,640, and the reference nr. 62 actually prescribes (the remuneration that served as the basis for the indemnity, i.e. the CCG's own Step 2 figure of 67,778.40). Band 62,465.01 – 71,160 → **38.96%**.

| Line | Current | Correct under nr. 58/62 |
|---|---|---|
| 206 Withholding on the indemnity | 39,657.54 × 53.50% = **21,216.78** | 39,657.54 × 38.96% = **15,450.58** |
| 222 Notice indemnity net | 18,440.76 | **24,206.96** |
| 225 Total withholding | 24,354.33 | **18,588.53** |
| 225 Total net | 22,919.32 | **28,685.12** |
| 227 Definitive tax at 38.5% | 15,268.15 | 15,268.15 (unchanged) |
| 227 Excess refunded on assessment | 5,948.63 | **182.43** |

A **EUR 5,766.20 over-withholding on one settlement**, and Step 9's narrative — *"This gap between withholding and final taxation is normal and must be explained to employees"* — largely dissolves: the annex is designed so that the nr. 58 rate approximates the art. 171 average rate, which is exactly what 38.96% vs 38.5% shows. The current text presents a 27% over-withholding as normal Belgian practice. It is not.

Also to check in the same pass: `m09_termination.md:9`, `:140` and `:244`, and `m11_advanced.md`/`m04_compensation.md:295` all route severance or arrears to "the exceptional-payment table (Module 4.5)". Arrears (*achterstallen*) are governed by nr. 58 too, not nr. 53. **This needs its own ticket and its own verification pass; nothing beyond the m09 example was recomputed here.**

### (b) The 13.92 reference-remuneration factor is applied inconsistently

`m06_tax.md:205` and `:264`, and `m09_termination.md:239`, all define the exceptional-payment reference as **monthly gross × 13.92**. But two worked examples key the table on **× 12**:

| Location | Reference used | At × 13.92 | Band under 13.92 | Rate would become |
|---|---|---|---|---|
| `m08_leave.md:147` | 3,600 × 12 = 43,200 → 42.39% | 3,600 × 13.92 = **50,112** | 45,860.01 – 59,900 | **47.44%** |
| `m12_examples.md:172` | 3,800 × 12 = 45,600 → 42.39% | 3,800 × 13.92 = **52,896** | 45,860.01 – 59,900 | **47.44%** |

`m06_tax.md:360` and `m09_termination.md:297` correctly use × 13.92. Annex III nr. 53 says only *"het jaarbedrag van de normale brutobezoldigingen"* and does not itself prescribe a factor — 13.92 is administrative practice (12 months + double holiday pay + end-of-year premium). **Whichever convention is adopted, the CCG must use one.** This is not a bracket defect and is not resolved here; it needs its own pass, and it would change the withholding in both examples by roughly EUR 150.

### (c) Three one-cent arithmetic errors in the CCG's own F totals

Independent of every ticket. Each is a slice rounded up where nr. 12 rounds down:

| Location | CCG | Correct on the CCG's own basis |
|---|---|---|
| `m12:22` E1 slice 3 | 930.60 × 48.15% = 448.09 | **448.08** (448.0839) |
| `m12:23` E1 total | 10,394.81 | **10,394.80** |
| `m12:115` E4 slice 2 | 7,948.96 × 42.80% = 3,402.16 | **3,402.15** (3,402.15488) |
| `m12:116` E4 total | 7,874.76 | **7,874.75** |
| `m12:216` E6 total | 7,159.26 | **7,159.26** — correct; listed for completeness as its recomputed value differs only through the bracket change |

These disappear once §5.2's corrected figures are applied, so they need no separate ticket — but they should be called out in the fix so that a reviewer reconciling old against new does not chase a phantom.

### (d) The fourth band's cumulative constant is missing throughout

No module states EUR **20,320.38**, the cumulative amount at the top of the third slice. Any employee with annual net taxable income above EUR 51,050 cannot be computed from what the CCG publishes. None of the worked examples reaches that level, so no figure changes — but the formula at `m06_tax.md:127–131` is not implementable at the top of the scale as written. Worth folding into the same edit.

---

## 7. Confidence

| Claim | Confidence | Basis |
|---|---|---|
| Annex III nr. 31 base scale is 16,710 / 29,500 / 51,050 | **Certain** | nr. 31 verbatim from the machine-readable annex; all three published constants recompute exactly; independently confirmed by SYNOVA |
| Fourth band: above 51,050, 20,320.38 + 53.50% | **Certain** | nr. 31 verbatim; 9,944.05 + 48.15% × 21,550 = 20,320.375 → 20,320.38 under nr. 12 |
| Rates 26.75 / 42.80 / 48.15 / 53.50 are the Annex III withholding rates | **Certain** | nr. 31 verbatim |
| Assessment rates are 25 / 40 / 45 / 50, and withholding = assessment × 1.07 | **Certain** | art. 130 WIB 92; exact arithmetic on all four |
| Ceilings are not derivable from the assessment figures by any rounding rule | **Certain** | Round-down convention reproduces 1 of 3; no single coefficient fits (§2.6) |
| Annex III mandates cent-rounding at every step | **Certain** | nr. 12 verbatim |
| Scale III (non-residents) uses the same nr. 31 scale | **Certain** | nr. 108 verbatim: *"met behulp van de basisschaal opgenomen in nr. 31"*; nr. 109 divides by 12 |
| Module 8 holiday-pay table is correct, including column choice | **Certain** | nr. 53 read positionally from the PDF (x-coordinates), all 11 rows × 2 columns matched against `m08` and `m04` |
| Module 5 special SS contribution bands are correct | **High** | Every threshold, rate, fixed amount and both maxima match the NSSO 2026/2 instructions; four in-example applications recompute exactly. Near-primary (NSSO instructions), not the Law of 30 March 1994 text itself |
| Recomputed monthly figures in §5.2 | **High** | Computed from primary text under nr. 12 rounding; the model reproduces every current CCG figure exactly (including m09's 1,155.96 from an undocumented base), which validates it; two independent cross-checks pass — 688.70/291.62 reproduce `CHILDREN_SUPPLEMENT_INVESTIGATION.md`, and m06 line 349's 249.00 × 12 = 2,987.98 identity holds |
| Severance uses nr. 58, not nr. 53 (§6(a)) | **High** | nr. 53 excludes *opzeggingsvergoedingen* in terms; nr. 62 cross-refers to nrs. 58–60; the nr. 58 table independently confirmed band-for-band by Securex, whose page is titled for arrears **and** severance. Not verified against a Belgian payroll engine's output |
| Arrears also use nr. 58 | **Probable** | nr. 58 is headed *Achterstallen* and nr. 53 does not exclude them by name, but nr. 53's subject matter is exceptional allowances. Needs its own pass |

**Residual gap — unchanged from the predecessor, and now smaller.** The annex was again read from Securex's coordinated reproduction rather than the Staatsblad, because the BS text is not machine-readable. This pass adds two things the predecessors did not have: an internal arithmetic proof that the ceilings are self-consistent with the three published constants (§2.3), and confirmation of the same scale from a second house (§2.4). The risk of a transcription error in the reproduction is now very low. If certification against the BS is required before the fix ships, the target remains the Royal Decree of 11 December 2025, BS 29 December 2025, p. 97613.

---

## 8. Recommendation

1. **Correct the withholding scale to 16,710 / 29,500 / 51,050** at `m06_tax.md:128–131`, `m12_examples.md:5` and `02-wtc/be_wtc_data_part7.py:59`, and publish the cumulative constants 4,469.93 / 9,944.05 / 20,320.38 with it (§6(d)).
2. **Rewrite `m06_tax.md:181`, do not renumber it.** "The same slices" is the sentence that caused this defect; it must be replaced with an explicit statement that the withholding scale has its own ceilings. Leave `m06_tax.md:172–177` alone.
3. **Apply this fix together with the allowance and child-supplement fixes as a single edit** (§5.4). The FULL-fix column of §5.2/§5.3 is the target; it supersedes `ALLOWANCE_INVESTIGATION.md` §5.2 in full and confirms `CHILDREN_SUPPLEMENT_INVESTIGATION.md` §5.2.
4. **Add m06 Example 2 (scale III) to the fix scope.** Neither predecessor reached it, and Annex III nr. 108 puts it squarely inside this one. Line 349's 249.00 / 2,987.98 identity is a good post-fix self-check.
5. **Open a high-priority ticket for §6(a), the severance table.** It is worth EUR 5,766.20 on a single worked example, it changes a client-facing narrative in `m09_termination.md:227` that is currently misleading, and it may extend to arrears across Modules 4, 9 and 11.
6. **Open a ticket for §6(b), the 13.92 factor**, applied inconsistently between `m06`/`m09` and `m08`/`m12`.
7. **Record in the fix that m12 E2 is insulated and that m12 E4's net paid stays at EUR 1,772.91**, so a reviewer does not "correct" either.
8. **Do not carry the round-down convention forward as a derivation rule** (§2.6). It works for the allowance and fails for the brackets. Every Annex III constant must be read from the annex. Recording this in the shared playbook would be worth more than the fix itself.
9. **Modules 5 and 8 need no change.** Both were checked in full and both are correct; record the checks so the question is not reopened.

---

## 9. Sources

**Primary — Annex III, income year 2026**

- *Bijlage III van het Koninklijk besluit tot uitvoering van het WIB 1992*, as annexed to the **Koninklijk besluit van 11 december 2025** (BS 29.12.2025, p. 97613). Coordinated text, 44 pp., retrieved as [`Bijlage-III-KB-WIB-2026.pdf`](https://www.securex.be/getattachment/ceca9705-6370-4e55-9fee-3500a442a156/Bijlage-III-KB-WIB-2026.pdf) from the [Securex Annex III overview page](https://www.securex.be/nl/lex4you/werkgever/themas/verlonen/fiscale-loonlasten-bedrijfsvoorheffing/bijlage-iii-in-het-kort); text extracted with `pdfplumber`, tables resolved positionally where column order was ambiguous. Provisions relied on: **nrs. 12, 28, 31, 32, 37, 38, 42, 53, 54, 55, 58, 62, 66, 108, 109, 111, 117, 118**.

**Primary — assessment side, via the predecessor investigations**

- *Bericht in verband met de automatische indexering inzake inkomstenbelastingen — Aanslagjaar 2027*, BS 12.08.2026, p. 43734, NUMAC 2026006085 — Table III A, coefficient 2.0592 and the art. 130 bracket ceilings 16.720 / 29.510 / 51.070, used at §2.6 to demonstrate that no rounding rule derives the Annex III ceilings
- *Koninklijk besluit van 24 juli 2026 tot wijziging van de toepassingsregels voor de bedrijfsvoorheffing*, BS 30.07.2026 Ed. 2, NUMAC 2026005690 — operative list confirms nr. 31 was not amended

**Near-primary — social security**

- NSSO / RSZ, [*Bijzondere bijdrage sociale zekerheid*, administrative instructions 2026/2](https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/special_contributions/other_specialcontributions/specialsocialsecuritycontribution.html) — quarterly bands, percentages and maxima, §4.2

**Secondary — independent corroboration**

- [SYNOVA — *Bedrijfsvoorheffing*](https://www.synova.be/nl/fiscaliteit-personenbelasting/bedrijfsvoorheffing) — confirms the nr. 31 ceilings 16,710 / 29,500 / 51,050, the constants and the 11,170 allowance, from a house independent of Securex
- [Securex — *Bedrijfsvoorheffing achterstallen en opzegvergoedingen*](https://www.securex.be/nl/lex4you/werkgever/actuele-bedragen/fiscale-bedragen/bedrijfsvoorheffing-achterstallen-en-opzegvergoedingen) — confirms the nr. 58 table band-for-band, §6(a)
- [FPS Finance — *Bedrijfsvoorheffing: berekening*](https://financien.belgium.be/nl/ondernemingen/personeel_en_loon/bedrijfsvoorheffing/berekening) — now publishes the 2026 rules and *sleutelformule* on Fisconetplus. **Not usable as a source here:** the Fisconetplus viewer is a JavaScript application and returns no document text to a fetch. It remains the best route to a fully official confirmation if one is required, but it needs a browser or the Fisconet API.
- [CLB Group](https://www.clbgroup.be/nieuws/berekeningsregels-bedrijfsvoorheffing-vanaf-2026-bekend/) and [Wf-fe](https://www.wf-fe.be/bibliotheek/2025/7614-bijlage-iii-regels-bedrijfsvoorheffing-2026-gepubliceerd/) — publication of the 2026 Annex III rules, used only to date the instrument

**Sources found to be unreliable on this point**

- [calculateur-de-salaire.be](https://calculateur-de-salaire.be/guide/precompte-professionnel-belgique) — presents **16,310 / 28,790 / 49,820** as the 2026 withholding brackets. Those are income-year-2025 figures. A third, wrong candidate set, and a reminder that aggregator sites carry the previous year's scale for months after the new annex lands.

**Internal**

- `BE-compliance/07-qa-crosscheck/ALLOWANCE_INVESTIGATION.md` — §2.2 the art. 130 assessment ceilings, §4.1 the round-down convention (which §2.6 here bounds), §5.2 the recomputation now superseded
- `BE-compliance/07-qa-crosscheck/CHILDREN_SUPPLEMENT_INVESTIGATION.md` — §6(a) the original flag that opened this ticket, §2.2 the nr. 38 mechanism, §5.2 the two figures confirmed here
