# Belgium tax-engine fix — APPLIED

**Status:** APPLIED. Files in `01-ccg/` and `02-wtc/` were modified.
**Date:** 14 August 2026
**Basis:** `ALLOWANCE_INVESTIGATION.md`, `CHILDREN_SUPPLEMENT_INVESTIGATION.md`, `BRACKET_INVESTIGATION.md`, applied as a **single combined edit** as all three investigations required (they collide in the same lines), plus a fourth item standardising the reference-remuneration factor on x 13.92.

**Amended 14 August 2026 — second pass.** Item 5 (the nr. 58 / 38.96% severance correction), previously held back for a decision at §2, is now **authorised and applied**. Items 1–4 were held fixed and are confirmed unmoved. Three pre-existing defects were surfaced while mirroring item 5 into the `.docx`; one was closed, two are flagged and left untouched. See §2 and §7.

---

## 1. What was applied

| # | Change | Source |
|---|---|---|
| 1 | Basic tax-free allowance **EUR 11,180 → EUR 11,170**; reduction **2,990.65 → 2,987.98**. Zero-withholding threshold sentence updated. | ALLOWANCE §4 |
| 2 | Dependent-child relief: **structural** change from `26.75% x (allowance + supplement)` to `[26.75% x 11,170 = 2,987.98]` **then a separate flat reduction of the basisbelasting** — 624 / 1,656 / 4,404 (full nr. 38 table published, 1–8 children + the >8 rule + the disabled-child doubling). | CHILDREN §2–3 |
| 3 | Annex III nr. 31 withholding ceilings **16,720/29,510/51,070 → 16,710/29,500/51,050**, with the cumulative constants **4,469.93 / 9,944.05 / 20,320.38** published (band 4's constant was previously absent from the CCG entirely). Rates unchanged. The art. 130 **assessment** scale table was left untouched. | BRACKET §2 |
| 4 | Reference-remuneration factor standardised on **x 13.92** — `m08_leave.md` double-holiday-pay example and `m12` Example 5 Part B moved off x 12. | Mercans convention, per instruction |
| **5** | **Notice indemnities take the Annex III nr. 58 arrears-and-severance scale (nr. 62), not the nr. 53 exceptional-payment table.** m09's worked example moves from 53.50% to **38.96%**; withholding 21,216.78 → **15,450.58**. The 18-band nr. 58 table is now published in Module 9.1. | BRACKET §6(a) |

**Verification method.** Every worked example was recomputed from scratch with an independent Decimal engine applying Annex III nr. 12 cent-rounding at each step, *before* any file was edited. The engine was first validated by reproducing **every pre-fix CCG figure exactly** (826.30, 709.71, 617.01, 874.01, 298.01, 871.58, 283.63, 1,075.52, 1,155.96) from the CCG's own stated inputs on the old parameters. It was then re-run against the edited files as a closing self-check: **59 recomputed figures, 0 missing, 0 discrepancies.**

**Verification method, item 5.** The whole Module 9 example was rebuilt from its stated **facts** only — monthly salary 4,500, car 250, 20 meal-voucher days at 8.91, 39 weeks, 13.07%, 18,000 gross to 30 April, 38.5% average rate — with no figure copied from the edited files, then the nr. 58 band selected from the 18-band table by lookup rather than by hand. Every one of the 25 recomputed lines reproduces, including the four items 1–3 figures that had to stay put. The result was then cross-checked against `BRACKET_INVESTIGATION.md` §6(a)'s pre-computed figures: **6 of 6 match exactly, 0 discrepancies**, so nothing was decided silently. Reproducible: `07-qa-crosscheck/verify_nr58_fix.py`.

**Agreement with the investigations.** My independent arithmetic matched the pre-computed "FULL fix" column of `BRACKET_INVESTIGATION.md` §5.2/§5.3 and the two figures in `CHILDREN_SUPPLEMENT_INVESTIGATION.md` §5.2 **on every single line**. No discrepancy arose, so nothing was decided silently. (`ALLOWANCE_INVESTIGATION.md` §5.2's monthly figures are superseded, exactly as `BRACKET_INVESTIGATION.md` §5.4 states — they were computed on the assessment brackets.)

---

## 2. Item 5 — APPLIED (second pass, 14 August 2026)

Previously held back pending a decision. Now authorised and applied on top of items 1–4, which were held fixed.

**The defect.** `m09_termination.md` withheld the notice indemnity from Annex III **nr. 53** at the top rate of 53.50%. Annex III nr. 53 excludes severance from its own scope in its opening words — *"voor **andere** exceptionele vergoedingen en toelagen **dan opzeggingsvergoedingen**"* — and **nr. 62** routes notice indemnities to the arrears-and-severance scale of **nrs. 58 to 60**, an 18-band table topping out at 48.00%.

**The reference.** Under nr. 62 the percentage is keyed on *the remuneration that served as the basis for determining the indemnity* — the example's own Step 2 annual current remuneration, **EUR 67,778.40**. That falls in the band 62,465.01 – 71,160.00 → **38.96%**. The monthly-gross x 13.92 = EUR 62,640.00 reading lands in the **same band**, so item 4's x 13.92 convention and nr. 62's own reference agree here and the rate is 38.96% on either reading. This was verified arithmetically, not assumed.

**What did not change.** Everything the brief put out of scope held: the 38.96% band itself, the April-salary figure of 1,156.36 (items 1–3), the departure-holiday-pay figure of 1,284.17 (nr. 53 top band, correctly applied — departure holiday pay is *not* severance), and the whole of items 1–4 elsewhere in the CCG.

**Beyond the worked example.** Five other statements in the CCG routed the notice indemnity to the nr. 53 table and were corrected in the same pass, because leaving them would have made the document contradict its own worked example: the m06 treatment matrix, m09's residential-status table, m09's termination-payments reference guide, and two statements in m09 §9.2. The 18-band nr. 58 table is now **published** in Module 9.1 — without it the 38.96% is not derivable from anything the CCG states, the same reasoning that put band 4's missing constant into Module 6 under item 3.

⚠️ **Arrears were deliberately NOT touched.** `BRACKET_INVESTIGATION.md` §6(a)/§7 rates "arrears also use nr. 58" as **Probable, needs its own pass** — unlike severance, which is High confidence. Every arrears statement in m09, m04 and m11 still routes to nr. 53. That remains open (§5, item 1a).

---

## 3. Diff table — every change, grouped by worked example

Line numbers are the **pre-edit** `.md` line numbers. Every `.md` change is mirrored in `BE-CCG-001-v1.0.docx`.

### 3.1 Parameter statements (no arithmetic)

| File | Line | Before | After |
|---|---|---|---|
| m06_tax.md | 7 | full tax-free allowance of EUR **11,180** | EUR **11,170** |
| m06_tax.md | 99–101 | basic allowance EUR **11,180**; dependants +2,030 / +5,230 / +11,720 | allowance EUR **11,170** → reduction **2,987.98**; children = **separate flat** reduction 624 / 1,656 / 4,404 (nr. 38) |
| m06_tax.md | 127–131 (step 6) | 26.75% 0–16,720 / 42.80% 16,720–29,510 / 48.15% 29,510–51,070 / 53.50% >51,070 | **16,710 / 29,500 / 51,050** + constants **4,469.93 / 9,944.05 / 20,320.38** |
| m06_tax.md | 132–137 (steps 7–10) | `G = 26.75% x (11,180 + dependant supplements)`, steps 7–10 | `G = 26.75% x 11,170 = 2,987.98` → **BASISBELASTING**; **new step 8 = nr. 38 flat table** (1–8 children, >8 rule, disabled child ×2); steps renumbered to 11; nr. 12 cent-rounding sentence added |
| m06_tax.md | 174–177 | assessment scale 16,720 / 29,510 / 51,070 at 25/40/45/50% | **UNCHANGED** — correct assessment scale |
| m06_tax.md | 179 | Basic tax-free allowance **11,180**, +2,030 / +5,230 / +11,720 | allowance **11,170** → 2,987.98; children as **separate flat** 624 / 1,656 / 4,404 |
| m06_tax.md | 181 | "Withholding scale actually used in payroll — **the same slices** at 26.75%…" | claim of shared slices removed; explicit nr. 31 **table** added (16,710 / 29,500 / 51,050 + all four cumulative constants) with a note that the ceilings are not derivable from the assessment ones |
| m06_tax.md | 243 | withholding nil at or below EUR **11,180** | EUR **11,170** |
| m07_deductions.md | 25–31 | "…and dependant supplements"; allowance **11,180**; supplements 2,030 / 5,230 / 11,720; "total allowance x 26.75%"; "step 7" | "…and dependent-child relief"; allowance **11,170** → 2,987.98; **full nr. 38 table** 624 … 21,996 (+3,864), disabled child ×2; two-step calculation; "steps 7 and 8" |
| m12_examples.md | 5 | allowance 11,180; slices to 16,720 / 29,510 / 51,070 | allowance **11,170** → **2,987.98**; **Annex III nr. 31** slices **16,710 / 29,500 / 51,050**; child relief flagged as flat nr. 38 reduction |

### 3.2 m06 §6.1 — single resident, EUR 4,000/month

| Line | Before | After |
|---|---|---|
| 152 F1 | 16,720.00 x 26.75% = 4,472.60 | **16,710.00 x 26.75% = 4,469.93** |
| 153 F2 | 12,790.00 x 42.80% = 5,474.12 | **unchanged** (slice 2 is 12,790.00 wide on both scales) |
| 154 F3 | 6,146.40 x 48.15% = 2,959.49 | **6,156.40 x 48.15% = 2,964.31** |
| 155 F | 12,906.21 | **12,908.36** |
| 156 G | 11,180.00 x 26.75% = 2,990.65 | **11,170.00 x 26.75% = 2,987.98** |
| — (new row) | — | **Basisbelasting 12,908.36 − 2,987.98 = 9,920.38** |
| 157 Annual withholding | 9,915.56 | **9,920.38** |
| 158 Monthly withholding | 826.30 | **826.70** |

### 3.3 m06 §6.1 — same employee, two dependent children

| Line | Before | After |
|---|---|---|
| 162 mechanism | "allowance becomes 11,180 + 5,230 = 16,410, reduction 16,410 x 26.75% = 4,389.68" | **allowance unchanged at 11,170; flat EUR 1,656.00 deducted from the basisbelasting (nr. 38)** |
| 162 annual | 8,516.53 | **8,264.38** |
| 162 monthly | 709.71 | **688.70** |
| 162 saving | EUR 116.59 | **exactly EUR 138.00** (= 1,656 / 12; every nr. 38 row is a multiple of 12) |

### 3.4 m06 Example 1 — resident, EUR 4,000

| Line | Before | After |
|---|---|---|
| 321 Wage withholding tax | −826.30 | **−826.70** |
| 324 Net paid | 2,591.77 | **2,591.37** |
| 328 Employer cost | 5,187.11 | **unchanged** |

### 3.5 m06 Example 2 — non-resident, scale III

Annex III nr. 108 computes the scale III basisbelasting from the same nr. 31 scale, so this example moves on the brackets alone.

| Line | Before | After |
|---|---|---|
| 342 Tax on the scale | 4,472.60 + 5,474.12 + 2,959.49 = 12,906.21 | **4,469.93 + 5,474.12 + 2,964.31 = 12,908.36** |
| 344 Annual withholding | 12,906.21 | **12,908.36** |
| 345 Monthly withholding | 1,075.52 | **1,075.70** |
| 347 Net paid | 2,365.44 | **2,365.26** |
| 349 identity sentence | "EUR 249.22 per month, or EUR 2,990.65 per year" | **"EUR 249.00 per month, or EUR 2,987.98 per year"**, prefixed with the nr. 108 basis |

**Self-check on 349:** 1,075.70 − 826.70 = 249.00 and 249.00 x 12 = 2,988.00, against the stated 2,987.98 — the 2-cent gap is nr. 12 cent-rounding, as the investigation predicted. The identity survives the fix.

### 3.6 m08 — double holiday pay, EUR 3,600/month (item 4)

| Line | Before | After |
|---|---|---|
| 147 reference | 3,600.00 x **12** = 43,200.00 | 3,600.00 x **13.92** = **50,112.00** |
| 148 band | 34,640.01 – 45,860.00 → 42.39% | **45,860.01 – 59,900.00 → 47.44%** |
| 149 withholding | 2,879.12 x 42.39% = 1,220.46 | **2,879.12 x 47.44% = 1,365.85** |
| 150 net | 1,658.66 | **1,513.27** |
| after 150 | — | **new sentence** explaining the 13.92 factor |

Module 8's holiday-pay **table** (96–106) is Annex III nr. 53 and is confirmed correct — not touched.

### 3.7 m09 — redundancy termination payout (items 1–3)

| Line | Before | After |
|---|---|---|
| 213 April salary withholding (Step 7) | 1,155.96 | **1,156.36** |
| 221 April salary withholding / net (Step 8) | 1,155.96 / 2,755.89 | **1,156.36 / 2,755.49** |
| 225 Total withholding | 24,354.33 | 24,354.73 → **18,588.53** after item 5 |
| 225 Total net | 22,919.32 | 22,918.92 → **28,685.12** after item 5 |

### 3.7b m09 — item 5, the nr. 58 / 38.96% severance correction

Line numbers are the **pre-item-5** `.md` line numbers (i.e. the file as it stood after items 1–4).

**Parameter and routing statements (no arithmetic)**

| File | Line | Before | After |
|---|---|---|---|
| m06_tax.md | 10 | severance row: "withheld at the **exceptional-payment percentage**" | "withheld at the Annex III **nr. 58** arrears-and-severance percentage (0.00% to 48.00%), to which nr. 62 routes notice indemnities — **not** at the nr. 53 exceptional-payment percentage, which excludes them in terms" |
| m09_termination.md | 27 | "Exceptional-payment percentage, keyed on the annual gross reference" | "Annex III **nr. 58** arrears-and-severance percentage, to which nr. 62 routes notice indemnities, keyed on the remuneration that served as the basis for the indemnity" |
| m09_termination.md | 122 | "but the **exceptional-payment percentage** from the Annex III table, keyed on the employee's normal annual gross remuneration" | rewritten to nr. 58 / nr. 62, with the nr. 53 exclusion quoted in Dutch; **the 18-band nr. 58 table added** plus a note that it tops out at 48.00% and is built to approximate the art. 171 average rate |
| m09_termination.md | 139 | reference guide, notice indemnity: "Exceptional-payment percentage" | "Annex III **nr. 58** percentage (routed there by nr. 62), 0.00% to 48.00%" |
| m09_termination.md | 244 | §9.2 step 2 of the irregular-payment method | 4 code lines added carving notice indemnities out to nr. 58 |
| m09_termination.md | 257 | route list included "notice indemnities" | removed from the nr. 53 list; new paragraph stating they follow the same *structure* but the nr. 58 *table* |
| m09_termination.md | 229 | legal basis | **Annex III nrs. 53, 58 to 60 and 62** added |

**Worked example — Steps 6, 8 and 9**

| Line | Before | After |
|---|---|---|
| 203 Step 6 reference | "4,500.00 x 13.92 = EUR 62,640.00, which is above EUR 59,900.00, so the top rate applies" | nr. 62 reference = Step 2's **EUR 67,778.40**, band 62,465.01 – 71,160.00 → **38.96%**; note added that the x 13.92 reading falls in the same band |
| 206 Withholding on the indemnity | 39,657.54 x 53.50% = **21,216.78** | 39,657.54 x 38.96% = **15,450.58** |
| — (new) | — | note quantifying the correction: nr. 53 would have over-withheld by **EUR 5,766.20** |
| 222 Notice indemnity withholding | 21,216.78 | **15,450.58** |
| 222 Notice indemnity net | 18,440.76 | **24,206.96** |
| 225 Total withholding | 24,354.73 | **18,588.53** |
| 225 Total net | 22,918.92 | **28,685.12** |
| 227 Step 9 withheld | 21,216.78 | **15,450.58** |
| 227 Step 9 excess refunded | 5,948.63 | **182.43** |
| 227 Step 9 narrative | "This gap between withholding and final taxation is normal and must be explained to employees" | replaced: the closeness of 38.96% to 38.5% is the nr. 58 scale working as designed; **a large refund on a notice indemnity should be investigated, not explained away** |

**Rows deliberately unchanged in the same table**

| Line | Figure | Why |
|---|---|---|
| 221 April salary | 1,156.36 / 2,755.49 | items 1–3, held fixed |
| 223 Departure holiday pay | 1,284.17 / 1,116.14 | nr. 53 top band, correctly applied — departure holiday pay is not severance |
| 224 Pro rata end-of-year premium | 697.42 / 606.53 | see §7(c) — carries a pre-existing EUR 0.19 arithmetic error, **not** corrected because it is outside all five authorised changes |
| 225 Total gross / total SS | 54,381.28 / 7,107.63 | unaffected by any withholding change |

Cross-foot: 54,381.28 − 7,107.63 − 18,588.53 = **28,685.12** ✅
Line-by-line nets: 2,755.49 + 24,206.96 + 1,116.14 + 606.53 = **28,685.12** ✅

### 3.8 m12 Example 1 — EUR 3,500

| Line | Before | After |
|---|---|---|
| 20 slice 1 | 16,720.00 x 26.75% = 4,472.60 | **16,710.00 x 26.75% = 4,469.93** |
| 22 slice 3 | 930.60 x 48.15% = 448.09 | **940.60 x 48.15% = 452.90** |
| 23 F | 10,394.81 | **10,396.95** |
| 24 allowance reduction | 11,180.00 x 26.75% = −2,990.65 | **11,170.00 x 26.75% = −2,987.98** |
| 25 annual | 7,404.16 | **7,408.97** |
| 26 monthly | −617.01 | **−617.41** |
| 29 net pay | 2,377.91 | **2,377.51** |
| 43 narrative | EUR 2,377.91 in cash | **EUR 2,377.51** (ratio still ≈ 2.0) |

The pre-existing one-cent slice-3 error (448.09 vs 448.08) noted in BRACKET §6(c) disappears with the corrected slice — no phantom to chase.

### 3.9 m12 Example 2 — part-time, EUR 1,300 (INSULATED)

| Line | Before | After |
|---|---|---|
| 59 tax on first slice | 10,135.52 x 26.75% = 2,711.25 | **unchanged** — base is below both first-slice ceilings |
| 60 allowance reduction | 11,180.00 x 26.75% = −2,990.65 | **11,170.00 x 26.75% = −2,987.98** |
| 61–62 withholding | 0.00 | **0.00 — unchanged** (floored) |
| 65 net pay | 1,192.44 | **unchanged** |

### 3.10 m12 Example 3 — EUR 4,200 + pension contribution

| Line | Before | After |
|---|---|---|
| 83 slice 1 | 16,720.00 x 26.75% = 4,472.60 | **16,710.00 x 26.75% = 4,469.93** |
| 85 slice 3 | 8,232.72 x 48.15% = 3,964.05 | **8,242.72 x 48.15% = 3,968.87** |
| 86 F | 13,910.77 | **13,912.92** |
| 87 allowance reduction | −2,990.65 | **−2,987.98** |
| 89 annual | 10,488.12 | **10,492.94** |
| 90 monthly | −874.01 | **−874.41** |
| 94 net pay | 2,593.45 | **2,593.05** |

### 3.11 m12 Example 4 — EUR 2,800, one child, garnishment

| Line | Before | After |
|---|---|---|
| 114 slice 1 | 16,720.00 x 26.75% = 4,472.60 | **16,710.00 x 26.75% = 4,469.93** |
| 115 slice 2 | 7,948.96 x 42.80% = 3,402.16 | **7,958.96 x 42.80% = 3,406.43** |
| 116 F | 7,874.76 | **7,876.36** |
| 117 allowance step | "(11,180.00 + 2,030.00) x 26.75% = −3,533.68" | **"11,170.00 x 26.75% = −2,987.98"** |
| — (new row) | — | **Basisbelasting 7,876.36 − 2,987.98 = 4,888.38** |
| — (new row) | — | **Reduction for one dependent child, Annex III nr. 38 = −624.00** |
| 118 fiscal work bonus | −765.00 | **unchanged** |
| 119 annual | 3,576.08 | **3,499.38** |
| 120 monthly | −298.01 | **−291.62** |
| 122 net for art. 1409 | 2,246.53 | **2,252.92** |
| 132 fourth band, 100% | 319.53 | **325.92** |
| 133 total attachable | 450.73 | **457.12** |
| 137 net before attachment | 2,246.53 | **2,252.92** |
| 140 **net paid to the employee** | 1,772.91 | **1,772.91 — UNCHANGED** ✅ |
| 142 maintenance-debt sentence | 2,246.53 | **2,252.92** |
| after 142 | — | **new note** explaining that the EUR 6.39 gain is fully absorbed by the 100%-attachable band, so line 140 is correct and must not be "corrected" |

Steps were renumbered 12→19 to accommodate the two new rows.

### 3.12 m12 Example 5 — EUR 3,800 + company car + double holiday pay

**Part A (brackets + allowance):**

| Line | Before | After |
|---|---|---|
| 160 slices 1–3 | 4,472.60 + 5,474.12 + (7,274.88 x 48.15% = 3,502.85) = 13,449.57 | **4,469.93 + 5,474.12 + (7,284.88 x 48.15% = 3,507.67) = 13,451.72** |
| 161 allowance reduction | −2,990.65 | **−2,987.98** |
| 162 annual | 10,458.92 | **10,463.74** |
| 163 monthly | −871.58 | **−871.98** |

**Part B (item 4 — x 12 → x 13.92):**

| Line | Before | After |
|---|---|---|
| 172 reference | 3,800.00 x **12** = 45,600.00 | 3,800.00 x **13.92** = **52,896.00** |
| 173 band | 34,640.01 – 45,860.00 → 42.39% | **45,860.01 – 59,900.00 → 47.44%** |
| 174 withholding | 3,039.07 x 42.39% = 1,288.26 | **3,039.07 x 47.44% = 1,441.73** |
| 175 net double holiday pay | 1,750.81 | **1,597.34** |

**Part C** (special SS contribution, 147.39) — **unchanged**, it is driven by the quarterly wage, not by withholding.

**Part D:**

| Line | Before | After |
|---|---|---|
| 189 net of ordinary remuneration | (3,800.00 − 496.66 − 871.58) = 2,431.76 | **(3,800.00 − 496.66 − 871.98) = 2,431.36** |
| 190 net double holiday pay | 1,750.81 | **1,597.34** |
| 192 net paid in quarter-end month | 4,035.18 | **3,881.31** |
| 197 comparison sentence | "42.39% against 46.44%" | **"47.44% against 51.48%"** + note that both tables key on x 13.92 |

⚠️ **Line 192 deliberately differs from `BRACKET_INVESTIGATION.md` §5.3's figure of 4,034.78.** That figure held the holiday pay at 1,750.81 because item 4 was outside all three investigations' scope. 4,034.78 is the correct value for items 1–3 alone; **3,881.31** is the correct value once item 4 is also applied. This is not a disagreement with the investigation — it is a fourth change layered on top of it. Same for m08 above.

### 3.13 m12 Example 6 — blue-collar, 108% base

| Line | Before | After |
|---|---|---|
| 214 slice 1 | 16,720.00 x 26.75% = 4,472.60 | **16,710.00 x 26.75% = 4,469.93** |
| 215 slice 2 | 6,277.24 x 42.80% = 2,686.66 | **6,287.24 x 42.80% = 2,690.94** |
| 216 F | 7,159.26 | **7,160.87** |
| 217 allowance reduction | −2,990.65 | **−2,987.98** |
| 219 annual | 3,403.61 | **3,407.89** |
| 220 monthly | −283.63 | **−283.99** |
| 222 net pay | 2,120.80 | **2,120.44** |

### 3.14 WTC — `BE-WTC-001-v1.0.xlsx`

| Sheet / cell | Before | After |
|---|---|---|
| Wage Type Catalogue F305 (method narrative) | steps (5)–(8), scale 16,720/29,510/51,070, `26.75% x (11,180 + supplements 2,030/5,230/11,720)` | steps (5)–(9), **Annex III nr. 31** scale 16,710/29,500/51,050 **with all four cumulative constants**, `26.75% x 11,170 = 2,987.98` → basisbelasting, **new step (7) = nr. 38 flat child table** |
| Tax Credit A10 | "Basic tax-free allowance and dependant supplements" | "Basic tax-free allowance and **dependent-child relief**" |
| Tax Credit B10 | "Basic allowance EUR 11,180. Supplements: 2,030 / 5,230 / 11,720…" | "Basic allowance **EUR 11,170** (nr. 32), reduction **EUR 2,987.98**. **Separate flat** nr. 38 reduction 624 … 21,996 (+3,864), disabled child ×2…" |
| Tax Credit D10 | "reduction of the annual tax equal to the total allowance x 26.75% (step 7)" | "**Two distinct steps**: 11,170 x 26.75% = 2,987.98 (step 7), then the flat child amount off the basisbelasting (step 8)" |

The WTC's **x 13.92** references (F62, F124–F133, F229, F284, F306, B344/F344, Global WTC Coverage B58/E58 and others) were already correct and are untouched — item 4 required no WTC change.

**Item 5 in the WTC** (second pass):

| Sheet / cell | Before | After |
|---|---|---|
| Wage Type Catalogue **F120** — the Notice indemnity wage type | "Withheld at the **exceptional-payment percentage**;" | "Withheld at the Annex III **nr. 58** arrears-and-severance percentage, to which nr. 62 routes notice indemnities — NOT at the nr. 53 exceptional-payment percentage, which excludes them in terms…" + **all 18 nr. 58 bands published**, keyed on the remuneration that served as the basis for the indemnity rather than on monthly gross x 13.92 |
| Wage Type Catalogue **F306** — Wage withholding tax, exceptional remuneration | scope list included "…arrears relating to a previous year, **notice indemnities** and the single part of the departure holiday pay" | notice indemnities removed from the scope list; explicit "NOTICE INDEMNITIES DO NOT USE THIS TABLE" pointer to nr. 58 / nr. 62 and to the Notice indemnity wage type |

The nr. 53 **band table** in F306 and the holiday-pay table in F307 are unchanged — both are confirmed correct.

### 3.15 Generator sources fixed so a rebuild cannot reintroduce the defect

Not in the brief's file list, but `CHILDREN_SUPPLEMENT_INVESTIGATION.md` §5.1 / rec. 5 flags these as the upstream cause. Left stale, the next WTC rebuild would silently restore the wrong figures.

| File | Line | Change |
|---|---|---|
| `02-wtc/be_wtc_data_part7.py` | 58–62 | withholding-method narrative → nr. 31 scale + constants, 11,170 / 2,987.98, nr. 38 flat child table |
| `02-wtc/build_be_wtc.py` | 549–558 | Tax Credit row: title, amount and application-point text |
| `_prompts/wtc.md` | 51–53 | "VERIFIED REFERENCE VALUES" block → nr. 31 ceilings with an explicit warning that they are **not** the art. 130 assessment brackets; allowance 11,170; full nr. 38 table |
| `02-wtc/be_wtc_data_part2.py` | 365 | **item 5** — notice-indemnity wage type: exceptional-payment percentage → nr. 58 / nr. 62 with all 18 bands (mirrors F120) |
| `02-wtc/be_wtc_data_part7.py` | 80–81 | **item 5** — exceptional-remuneration wage type: notice indemnities removed from scope, pointer to nr. 58 added (mirrors F306) |

---

## 4. Confirmed NOT moved

Checked by targeted re-scan of all five `.md` files, the `.docx` (whole-document string sweep) and the `.xlsx` (all sheets, all cells):

| Item | Status |
|---|---|
| **art. 130 assessment scale** `m06:174–177` — 16,720 / 29,510 / 51,070 at 25/40/45/50% | ✅ untouched, correct |
| Withholding **rates** 26.75 / 42.80 / 48.15 / 53.50% | ✅ unchanged everywhere |
| **7% uplift** explanation `m06:25` | ✅ unchanged |
| Slice 2 width 12,790.00 and its 5,474.12 | ✅ unchanged in all seven examples — identical on both scales |
| **Module 5** special social security contribution bands, all applications (108.72 / 74.21 / 147.39 / 122.13 / 51.11 / 53.52 / 181.53 / 154.92 / 182.82) | ✅ untouched — quarterly-wage driven |
| **Module 8** holiday-pay table, all 11 bands | ✅ untouched (nr. 53, confirmed correct) |
| **Module 4** exceptional-payment table, all 11 bands | ✅ untouched |
| **m09 bonus example** (3,200 x 13.92 = 44,544 → 46.44%) | ✅ untouched, already on 13.92 |
| **m09 April salary** 1,156.36 / 2,755.49 | ✅ items 1–3 value held through item 5 |
| **m09 departure holiday pay** 1,284.17 / 1,116.14 at 53.50% | ✅ untouched — nr. 53 top band, correctly applied; not severance |
| **m12 E5 net paid in the quarter-end month** | ✅ **3,881.31** — the combined four-fix value, confirmed **not** reverted to the three-fix prediction of 4,034.78 |
| **m12 E5 net double holiday pay** | ✅ **1,597.34** — four-fix value held |
| **m08 double-holiday-pay withholding / net** | ✅ **1,365.85 / 1,513.27** — the m08 equivalents of m12 line 192; four-fix values held, not reverted to 1,220.46 / 1,658.66 |
| **Arrears** routing to nr. 53 in m09 / m04 / m11 | ⚠️ untouched by design — "Probable, needs its own pass" (§5.1a) |
| Lump-sum expense cap EUR 6,070 | ✅ unchanged |
| Employee SS 13.07%, social work bonus, meal vouchers, CO2 contribution, 108% uplift, employer-cost tables | ✅ unchanged |
| m12 E2 (all lines except the allowance-reduction row) | ✅ unchanged — insulated |
| m12 E4 net paid to the employee, EUR 1,772.91 | ✅ unchanged — self-cancelling, now documented in the text |

---

## 5. Not addressed (out of scope, still open)

Recorded so nothing is lost. Each already has a home in the predecessor investigations.

1. ~~**Module 9 severance table nr. 53 → nr. 58**~~ — **CLOSED**, applied as item 5. See §2.
   **1a. Arrears (*achterstallen*) may also belong on nr. 58** — still open, and now the highest-value remaining item. `BRACKET_INVESTIGATION.md` §7 rates it **Probable**, not confirmed: nr. 58 is headed *Achterstallen*, but nr. 53 does not exclude arrears by name. Affects `m09:266`, `m09:281`, `m04_compensation.md:295`, `m11_advanced.md`, and ~14 WTC arrears wage types that all currently say "exceptional-remuneration percentage … x 13.92". Needs its own verification pass against the annex before anything moves.
2. **Fiscal work bonus 52.54% → 63% from 1 August 2026** (ALLOWANCE §5.4(b)) — affects m12 E4 and E6, both of which would need recomputation *again*.
3. **Overtime relief raised ceilings** 360 h hotel / 280 h road-rail (ALLOWANCE §5.4(c)).
4. **Child relief on exceptional remuneration** (nr. 55 percentage table) appears absent from m04/m08 (CHILDREN §6(c)) — potential systematic over-withholding on bonuses.
5. **Scale II / spouse thresholds** nrs. 33, 40.2, 40.3 not verified (CHILDREN §6(d)).
6. **Legal-basis citations** — Annex III citations should be extended with the **Royal Decree of 24 July 2026** and cite **nr. 31 / nr. 32 / nr. 38** specifically; the **Law of 15 July 2026** should be added wherever art. 131 is cited (ALLOWANCE §5.3, BRACKET §5.5). Not applied — citation work, not part of the four confirmed numeric changes.
7. **The 11,170-vs-11,550 two-figure explanation** recommended by ALLOWANCE §7.3 (withholding runs on 11,170, assessment on 11,550, difference refunded) was **not** added; it is new explanatory content rather than one of the four changes.
8. **Watch item:** the Royal Decree amending Annex III for the reformed allowance had not landed as at 14 August 2026. When it does, re-verify against the decree — do **not** use the projected 11,540.

---

## 6. Files changed

| File | Backup taken |
|---|---|
| `01-ccg/modules/m06_tax.md` | (git) |
| `01-ccg/modules/m07_deductions.md` | (git) |
| `01-ccg/modules/m08_leave.md` | (git) |
| `01-ccg/modules/m09_termination.md` | (git) |
| `01-ccg/modules/m12_examples.md` | (git) |
| `01-ccg/BE-CCG-001-v1.0.docx` | `.bak-before-taxengine-fix` — 142 scripted edits, every one assertion-guarded on its expected pre-edit text; the script aborts without writing if any assertion fails |
| `02-wtc/BE-WTC-001-v1.0.xlsx` | `.bak-before-taxengine-fix` — 4 edits, same guard |
| `02-wtc/be_wtc_data_part7.py`, `02-wtc/build_be_wtc.py`, `_prompts/wtc.md` | (git) |

**Post-edit sweeps.** `.md`: 0 stale occurrences of 11,180 / 2,990.65 / 2,030 / 5,230 / 11,720 / 16,720 / 29,510 / 51,070 or any superseded worked-example figure, other than the art. 130 assessment table and the nr. 53 band rows, which are correct. `.docx`: 9 remaining hits, all verified as intentionally-retained content (art. 130 table ×4, m04 exceptional-payment 46.44%, m08 holiday-pay 42.39%, m09 bonus 46.44% ×2, m12 E2's unchanged 2,711.25). `.xlsx`: 0 stale hits.

**Second pass (item 5) — files changed**

| File | Backup |
|---|---|
| `01-ccg/modules/m06_tax.md`, `m09_termination.md` | (git) |
| `01-ccg/BE-CCG-001-v1.0.docx` | `.bak-before-nr58-fix` — 26 scripted edits, each assertion-guarded on its expected pre-edit text; the script aborts without writing if any assertion fails |
| `02-wtc/BE-WTC-001-v1.0.xlsx` | `.bak-before-nr58-fix` — 2 edits, same guard |
| `02-wtc/be_wtc_data_part2.py`, `02-wtc/be_wtc_data_part7.py` | (git) |

**Post-edit sweep for item 5.** `21,216.78` survives exactly once in the `.md` and once in the `.docx`, in both cases inside the new sentence that states explicitly what the nr. 53 rate *would have* produced. `18,440.76`, `24,354.73`, `22,918.92` and `5,948.63` are gone from both. Reproducible verifier: `07-qa-crosscheck/verify_nr58_fix.py`.

---

## 7. Newly surfaced while mirroring item 5 — read this

Mirroring item 5 into the `.docx` was done by rebuilding the document from the `.md` sources **into a scratch file** and diffing it against the live `.docx`, rather than by string-patching blind. That diff isolated item 5's own edits to zero residual difference — and exposed four pre-existing `.md`-vs-`.docx` desyncs that no single-file check could have found. One was closed; three are **left untouched** because they fall outside the five authorised changes.

### (a) CLOSED — item 2 was never mirrored into the .docx

`m07_deductions.md` carried the corrected dependent-child mechanism from the first pass, but the corresponding `.docx` paragraphs still read **"Basic tax-free allowance and dependant supplements"**, *"the **total allowance** multiplied by 26.75%"* and *"**step 7** of the annual withholding calculation"*. §3.1 of this report claimed that change was mirrored; it was not. Four `.docx` paragraphs have now been brought into line with the `.md`. This is a completion of item 2, not a new change.

### (b) ⚠️ NOT TOUCHED — the .docx and the .md disagree on the inbound-taxpayer percentage, and **the .md is the wrong one**

| Artifact | m06 inbound-taxpayer row |
|---|---|
| `BE-CCG-001-v1.0.docx` | "Up to **35%** of gross … minimum gross remuneration of EUR 70,000 per year and no absolute cap…" |
| `m06_tax.md:219` | "Up to **30%** of gross … Note: NSSO/ONSS did not adopt the same reform…" |

`CCG_CONTENT_REVIEW.md` records this under **"RETRACTED — this was MY error, not a document defect"**: the 35% figure is correct, confirmed by Claeys & Engels (April 2026) and Andersen (May 2026) both citing Circulaire 2026/C/51 of 1 April 2026, and the erroneous edit to 30% was supposedly reverted. **The revert reached the `.docx` but not the `.md`.** The `.md` additionally asserts the ONSS non-alignment that the same review log explicitly downgraded to *"genuinely unresolved — DO NOT EDIT until resolved with a primary source"*.

Two consequences, both important:

1. **`m06_tax.md:219` currently carries a known-wrong figure and an unresolved assertion.** It needs its own ticket.
2. **Do not rebuild `BE-CCG-001-v1.0.docx` from the modules until (1) is fixed.** A rebuild would silently reintroduce the retracted 30% into the delivered document. This is why item 5 was applied by guarded patching rather than by regeneration.

### (c) ⚠️ NOT TOUCHED — a EUR 0.19 arithmetic error in m09 Step 7

The pro rata end-of-year premium: gross 1,500.00, employee SS 196.05, taxable **1,303.95**, rate 53.50%.

```
 1,303.95 x 53.50% = EUR 697.61      <- correct
 the CCG states                        EUR 697.42
```

The document is internally consistent with its own 697.42 (net 606.53 = 1,303.95 − 697.42, and the Step 8 total of 18,588.53 foots on it), so the error is confined to that one figure and its net. It appears in none of the three investigations' inventories and is not one of the five authorised changes, so **it was left as written and the item-5 totals were computed on the document's own 697.42.** Correcting it would move 697.42 → 697.61, 606.53 → 606.34, total withholding 18,588.53 → 18,588.72 and total net 28,685.12 → 28,684.93. Needs authorisation.

### (d) ⚠️ NOT TOUCHED — two m09 table cells over-reverted in the .docx

`m09_termination.md` says **"Ordinary scale"** in the income-tax column of the *"Salary for the notice period worked"* and *"Company car returned late"* rows; the `.docx` says just **"Ordinary"**. This is residue from the April-salary fix described in `CCG_CONTENT_REVIEW.md`'s process note, where a bare-string match wrote onto two unrelated rows and the revert trimmed them one word too far. Cosmetic, no numeric effect, and outside the five changes — flagged only so it is not rediscovered as a mystery.

**Sync status after this pass:** the `.docx` now differs from a clean rebuild of the `.md` sources in exactly **four** places — (b), (d) ×2, and one whitespace-only indentation difference in a Module 6 code block. Everything else, including all five changes, is byte-identical in content.
