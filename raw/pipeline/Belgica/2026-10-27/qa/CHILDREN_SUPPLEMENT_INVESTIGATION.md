# Belgian dependent-child relief in the withholding computation, income year 2026 — investigation

**Status:** INVESTIGATION ONLY. No file in `01-ccg/` or `02-wtc/` was modified.
**Date of investigation:** 14 August 2026
**Question:** CCG and WTC state dependent-child supplements to the basic tax-free allowance of EUR 2,030 (one child), 5,230 (two), 11,720 (three). Are these correct for the *bedrijfsvoorheffing* computation, and if not, what is?
**Predecessor:** `ALLOWANCE_INVESTIGATION.md` §5.4(a), which flagged these figures as suspect and instructed that Annex III be verified before anything is changed.

---

## 1. Bottom line

**A definitive primary source was found.** The full text of Annex III as replaced by the Royal Decree of 11 December 2025 — the instrument governing income year 2026 — was obtained in machine-readable form and read directly. No interim position or judgement call is required.

**The CCG and WTC are wrong about the *mechanism*, not merely about the amounts.**

Annex III does **not** grant dependent-child relief as a supplement to the tax-free allowance. It grants it as a **flat euro reduction of the annual basisbelasting**, taken from a table indexed on the number of dependent children (Annex III, Part 3, Ch. 2, Section 1, **nr. 38**). The reduction is not a percentage of anything, and there is no child-related allowance in the withholding annex at all.

| | CCG / WTC as written | Annex III as in force |
|---|---|---|
| Mechanism | supplement to the allowance, then × 26.75% | flat euro reduction of the basisbelasting |
| 1 child | +EUR 2,030 allowance → EUR 543.03 relief | **EUR 624** relief |
| 2 children | +EUR 5,230 allowance → EUR 1,399.03 relief | **EUR 1,656** relief |
| 3 children | +EUR 11,720 allowance → EUR 3,135.10 relief | **EUR 4,404** relief |

So the three EUR figures are wrong, the arithmetic applied to them is wrong, and the resulting relief is understated in every case. This is a structural defect in the formula, not a stale-parameter defect.

**On EUR 2,030 specifically (task 3):** it is almost certainly a genuine mis-sourcing, not coincidence — but the mix-up theory does not explain the other two figures, which match no official table at all. See §4.

**Confidence: see §7.** This investigation also closes the residual gap left open by `ALLOWANCE_INVESTIGATION.md` §6 — EUR 11,170 / EUR 2,987.98 is now confirmed from the annex text itself.

---

## 2. Task 1 — the Annex III mechanism

### 2.1 The source, and why the earlier attempt failed

`ALLOWANCE_INVESTIGATION.md` §6 recorded that the annex "in the BS of 29 Dec 2025 is embedded with a non-standard font encoding and is not machine-readable", and recommended obtaining a readable copy from Fisconetplus or the Securex overview page. **That recommendation worked.**

Securex publishes the coordinated annex as a PDF from its Annex III overview page:

> `https://www.securex.be/getattachment/ceca9705-6370-4e55-9fee-3500a442a156/Bijlage-III-KB-WIB-2026.pdf`

Its first line reads *"Bijlage bij het Koninklijk besluit van **11 december 2025**"* — the correct instrument for income year 2026. 44 pages, fully extractable.

**Caution on a different URL.** The Securex link that surfaces most readily in search (`.../4f3a2c18-.../Bijlage-III-KB-WIB.pdf`, no year in the filename) is the **2023** edition — headed *"Koninklijk besluit van 19 december 2022"*, carrying an allowance of EUR 9,620 and a one-child reduction of EUR 540. It is superseded and must not be used. Both editions were read here; only the 2026 one is cited for figures.

**Authenticity cross-checks** (six independent, all pass):

| Check | Result |
|---|---|
| nr. 32 allowance and reduction | *"verminderd met **2.987,98 euro** (zijnde de belasting op het basisbedrag van de belastingvrije som ten bedrage van **11.170 euro**)"* — matches Securex NL/FR editorial pages and `ALLOWANCE_INVESTIGATION.md` §4.1 |
| nr. 34.2 two-earner figure | 5.975,96 = 2 × 2,987.98 exactly |
| Base scale internal arithmetic | 16,710 × 26.75% = 4,469.93 ✅; +12,790 × 42.80% = 9,944.05 ✅; +21,550 × 48.15% = 20,320.38 ✅ — all three published constants reproduce exactly |
| nr. 28 expense cap | 30% / EUR 6,070 max — matches BS 12 Aug 2026 Table III A |
| Provision numbering | nrs. 45.2, 46.2.2, 78.3.2 and 131 all exist and carry the subject-matter amended by the KB of 24 July 2026 |
| nr. 46.2.2 work bonus | still 52,54%, matching SSGPI-RIO-2026/9 as the pre-August value |

The document is authentic and is the income-year-2026 text.

**One limitation, and why it does not matter here.** Securex dates this PDF 19 March 2026, so it is the **1 January 2026 text and does not incorporate the KB of 24 July 2026** (confirmed by nr. 46.2.2 still reading 52,54%). That decree amended only nrs. 45.2, 45.3, 46.2.2, 78.3.2, 131 and the young-athlete provision — per the full operative list in `ALLOWANCE_INVESTIGATION.md` §2.3. **None of nrs. 37–41 was touched**, so the child and family reduction tables below are the text in force today.

### 2.2 The mechanism, verbatim

Annex III, **Deel 3** (remuneration), **Hoofdstuk 2. VERMINDERINGEN**:

> **37.** Van de jaarlijkse basisbelasting vastgesteld overeenkomstig deel 2 mogen vervolgens de volgende verminderingen worden afgetrokken.
>
> *Afdeling 1. Vermindering voor kinderen ten laste*
>
> **38.** De vermindering voor kinderen ten laste bedraagt (rekening houdend met nr. 8):

> | AANTAL KINDEREN TEN LASTE | VERMINDERING VAN DE BASISBELASTING |
> |---|---|
> | 1 | 624 EUR |
> | 2 | 1.656 EUR |
> | 3 | 4.404 EUR |
> | 4 | 7.620 EUR |
> | 5 | 11.100 EUR |
> | 6 | 14.592 EUR |
> | 7 | 18.120 EUR |
> | 8 | 21.996 EUR |
>
> meer dan 8: de basisbelasting wordt verminderd met een vast bedrag van 21.996 EUR, verhoogd met **3.864 EUR** per kind ten laste boven het achtste, d.w.z.:
> a) voor 9 kinderen: 21.996 + (1 x 3.864) = 25.860 EUR
> b) voor 10 kinderen: 21.996 + (2 x 3.864) = 29.724 EUR

The column heading is decisive: **"VERMINDERING VAN DE BASISBELASTING"** — reduction *of the tax*, not increase of the allowance. The word *belastingvrije som* appears nowhere in nr. 38.

The allowance appears only once in the whole chain, at **nr. 32**, for the basic amount:

> **32.** [...] wordt de belasting bekomen volgens hoofdstuk 1, verminderd met 2.987,98 euro (zijnde de belasting op het basisbedrag van de belastingvrije som ten bedrage van 11.170 euro). Het bekomen verschil vormt de **basisbelasting**.

So Annex III applies the *basic* allowance as a percentage-derived reduction (which is what the CCG's step G models, correctly in structure), and then applies child relief as a **separate, additive, flat-euro step** on top. The CCG collapses these two distinct steps into one, and that collapse is the error.

### 2.3 The correct order of operations

```
 basisschaal (nr. 31)                    -> tax on annual net taxable base
 less 2,987.98                (nr. 32)   -> BASISBELASTING
 less child table             (nr. 38)   -> flat EUR by number of children
 less other family reductions (nrs. 39-41)
 divide by 12                 (nr. 42)   -> monthly bedrijfsvoorheffing
 less monthly reductions      (nrs. 43+) -> pension 30%, fiscal work bonus, overtime
```

### 2.4 The rounding convention — the analogue of §4.1

`ALLOWANCE_INVESTIGATION.md` §4.1 established that withholding figures follow their own rounding convention (round *down* to the lower 10, against the assessment convention of nearest 10), and asked that the same convention be applied here.

**The child table does not use rounding to 10 at all. It uses a different, stricter convention — and it is verifiable on every single row:**

| Children | Annual reduction | ÷ 12 |
|---|---|---|
| 1 | 624 | 52 |
| 2 | 1,656 | 138 |
| 3 | 4,404 | 367 |
| 4 | 7,620 | 635 |
| 5 | 11,100 | 925 |
| 6 | 14,592 | 1,216 |
| 7 | 18,120 | 1,510 |
| 8 | 21,996 | 1,833 |
| each above 8 | 3,864 | 322 |

**Every amount is an exact multiple of 12**, giving a whole number of euro per month. This is the convention nr. 42 demands: the annual figure is divided by 12 to produce the monthly withholding, and the table is constructed so that step is exact. The 2023 edition satisfies the same property (540, 1,476, 3,912, … all ÷ 12 exact), confirming it is a drafting rule and not an accident of one year.

This is a third distinct convention, alongside the two in §4.1 — and it is further evidence for the predecessor investigation's central thesis: **withholding and assessment are separate instruments with separate arithmetic conventions, and figures must never be carried across.**

### 2.5 Two further mechanisms the CCG does not model

**(a) Exceptional remuneration uses a *percentage* reduction, not the flat table.** The user's hypothesis — that Annex III might implement family relief as a percentage step — is correct, but for a *different* income type. Annex III **nr. 55** (Deel 4, exceptional allowances) grants child relief as a percentage of the withholding otherwise due, subject to a gross-income ceiling above which no relief is given:

| Children | % reduction | Ceiling: annual normal gross above which no relief |
|---|---|---|
| 1 | 7,5 | 28.940 EUR |
| 2 | 20 | 28.940 EUR |
| 3 | 35 | 31.835 EUR |
| 4 | 55 | 37.625 EUR |
| 5 | 75 | 40.520 EUR |

Relief is available only up to five children under this provision. A grep of `m04_compensation.md` and `m08_leave.md` returns **no reference to dependent children at all**, so this mechanism appears to be absent from the CCG's bonus and double-holiday-pay treatment. See §6(c).

**(b) Disabled children count twice.** Annex III **nr. 8**: *"wordt een kind ten laste met een handicap [...] voor twee gerekend"* — a disabled dependent child counts as two for the table lookup. **nr. 10**: on the death of a dependent child, the reduction continues to the end of the year of death. Neither rule is currently stated in the CCG.

**(c) Non-residents on scale III get neither.** Deel 6 nr. 108 computes the basisbelasting straight from the base scale with **no** deduction of the 2,987.98, and nr. 111's reduction list contains no child relief. This *confirms* the CCG's existing "Allowances: None" entry for scale III at `m06_tax.md:189` is correct.

---

## 3. Task 2 — the correct current figures

**For ordinary monthly remuneration, income year 2026** (Annex III nr. 38), the reduction of the annual basisbelasting is:

| Dependent children | Annual reduction (EUR) | Monthly effect (EUR) |
|---|---|---|
| 1 | **624** | 52.00 |
| 2 | **1,656** | 138.00 |
| 3 | **4,404** | 367.00 |
| 4 | 7,620 | 635.00 |
| 5 | 11,100 | 925.00 |
| 6 | 14,592 | 1,216.00 |
| 7 | 18,120 | 1,510.00 |
| 8 | 21,996 | 1,833.00 |
| >8 | 21,996 + 3,864 per additional child | +322.00 per child |

*A disabled dependent child counts as two (nr. 8).*

**The related family reductions**, for completeness, since the CCG mentions them in the same breath (nrs. 39–41, annual amounts, all cumulable unless noted):

| Ground | Annual reduction (EUR) |
|---|---|
| The income recipient is themselves disabled (nr. 39.1) | **624** |
| Dependant aged 66+ and care-dependent, per person (nr. 39.2) | 1,992 |
| Other dependants under art. 136, 2°–4° WIB 92, per person (nr. 39.3) | 624 |
| Single parent — non-remarried widow(er), unmarried/divorced/separated parent with dependent children (nr. 40.1) | 624 |
| Spouse with limited professional income ≤ EUR 290 net/month (nr. 40.2) | 1,740 |
| Spouse with pension income only ≤ EUR 579 net/month (nr. 40.3) | 3,474 |
| Spouse of the income recipient is disabled, scale II only (nr. 41) | 624 |

### 3.1 Why no "correct allowance supplement" figure can be given

The task asked for the correct EUR supplements under the withholding rounding convention. **That question has no answer, because the quantity does not exist in the withholding instrument.** The nearest thing is the allowance that *would* produce each reduction if the CCG's × 26.75% method were retained — but these are not lawful figures and must not be used:

| Children | Reduction | Implied "equivalent allowance" |
|---|---|---|
| 1 | 624 | 2,332.71 |
| 2 | 1,656 | 6,190.65 |
| 3 | 4,404 | 16,463.55 |

These are not round numbers in any convention, which is itself confirmation that the annex was never designed as an allowance supplement. **The fix must change the mechanism, not substitute new numbers into the old one.**

### 3.2 The contrast with art. 132, stated for the record

For assessment purposes the art. 132 WIB 92 supplements *are* allowance increases, and `ALLOWANCE_INVESTIGATION.md` §5.4(a) already recorded them correctly from BS 12 August 2026 Table II: **2,130 / 5,130 / 11,440** for one/two/three children. Those figures are right for the annual assessment and wrong for payroll — exactly the 11,550-vs-11,170 split, one level down.

---

## 4. Task 3 — is EUR 2,030 a mis-applied disabled-taxpayer figure?

**Finding: yes, on the balance of evidence — but it explains only one of the three figures.**

### 4.1 The case that it is a genuine mis-sourcing

EUR 2,030 is an **exact** match, to the euro, for the art. 131, 3rd paragraph AJ2027 supplement for a **disabled taxpayer**, per BS 12 August 2026 Table I:

```
Art. 131, 1ste lid   Belastingvrije som :                          4.945    11.550
           3de lid   Verhoging voor gehandicapte belastingplichtige:  870     2.030
```

Three points make coincidence unlikely:

1. **It sits on the line directly beneath the basic allowance** in Table I — the same table, one row down from where the CCG's sibling figure would have been read.
2. **The CCG pairs it with EUR 11,180**, which `ALLOWANCE_INVESTIGATION.md` §2.2 traced to the same family of published AJ2027 tables. Both figures appear to have been lifted from the assessment-side tables in one pass.
3. **The category the CCG assigns it to is occupied by a different number** — the one-child figure in the corresponding Table II is 2,130, not 2,030.

### 4.2 But the mix-up theory does not explain 5,230 and 11,720

Neither figure matches any published value. More importantly, an internal-ratio test rules out the "stale year" explanation entirely — a table indexed for a different year would preserve its internal proportions:

| Triple | Ratios (normalised to the one-child figure) |
|---|---|
| art. 132 non-indexed base (935 / 2,250 / 5,020) | 1 : 2.406 : 5.369 |
| art. 132 indexed AJ2027 (2,130 / 5,130 / 11,440) | 1 : 2.409 : 5.371 |
| **CCG (2,030 / 5,230 / 11,720)** | **1 : 2.576 : 5.773** |
| Annex III reductions (624 / 1,656 / 4,404) | 1 : 2.654 : 7.058 |

The base and the indexed official triple are the same shape, as they must be. **The CCG triple is a different shape, so it is not any year's art. 132 table.** Nor is it the Annex III schedule. Fitting a single indexation coefficient to it gives three inconsistent values (2.1711, 2.3244, 2.3347), i.e. no coefficient reproduces it.

**Conclusion.** EUR 2,030 is a disabled-taxpayer figure wrongly applied — high confidence. EUR 5,230 and EUR 11,720 have **no identified source**: they are not art. 132 for any year, not Annex III, and not internally consistent with each other. The triple as a whole did not come from a single official table, which means the original sourcing cannot be repaired by re-reading one table — it has to be replaced outright from nr. 38.

This distinction matters for the fix ticket: it is not a year-refresh, it is a rewrite.

---

## 5. Downstream impact inventory — scoping only, not applied

### 5.1 Statements of the figures (text, no arithmetic)

| Location | Current text |
|---|---|
| `m06_tax.md:100–101` | decision tree — "+EUR 2,030 for one child, +EUR 5,230 for two, +EUR 11,720 for three" |
| `m06_tax.md:133` | formula step 7 — "26.75% x (11,180 + dependant supplements)" — **mechanism, not just numbers** |
| `m06_tax.md:179` | "increased by EUR 2,030 for one dependent child, EUR 5,230 for two, EUR 11,720 for three" |
| `m07_deductions.md:29` | basic allowance line, same supplements |
| `02-wtc/be_wtc_data_part7.py:60–61` | "dependant supplements of EUR 2,030 for one child, EUR 5,230 for two, EUR 11,720 for three" |
| `02-wtc/build_be_wtc.py:550–552` | "Supplements: EUR 2,030 for one dependent child, EUR 5,230 for two, EUR 11,720 for three" |
| `_prompts/wtc.md:53` | the same triple, in the build prompt — **must be fixed too or a rebuild reintroduces it** |

`_prompts/wtc.md` is worth calling out: it is upstream of the WTC and would silently regenerate the wrong figures on any rebuild.

The **step 7 line in `m06_tax.md:133` cannot be repaired by substitution.** It needs to become two steps — G (allowance, 2,987.98) and a new step for the nr. 38 table.

### 5.2 Recomputed worked examples

Computed directly from Annex III (base scale nr. 31 → nr. 32 → nr. 38 → nr. 42), holding all non-tax inputs at the CCG's own values.

| Example | Line | Monthly withholding now | **Correct** | Delta |
|---|---|---|---|---|
| m06 §6.1, gross 4,000, **two children** | 162 | 709.71 | **688.70** | −21.01 |
| m12 E4, gross 2,800, **one child** | 120 | 298.01 | **291.62** | −6.39 |

Both are over-withholdings in the CCG as written — it understates child relief.

**m06 §6.1 two-children detail.** E = 35,656.40 → base scale 12,908.36 → less 2,987.98 = basisbelasting 9,920.38 → less 1,656 = 8,264.38 → ÷ 12 = **688.70**. The childless comparator on the same corrected basis is 826.70, so the monthly saving for two children is **exactly EUR 138.00** — which is 1,656 ÷ 12, a clean self-check. The CCG's narrative figure of "a monthly saving of EUR 116.59" must be replaced by EUR 138.00.

**m12 E4 detail.** E = 24,668.96 → base scale 7,876.36 → less 2,987.98 = 4,888.38 → less 624 = 4,264.38 → less fiscal work bonus 765.00 = 3,499.38 → ÷ 12 = **291.62**.
⚠️ The EUR 765.00 work bonus is itself flagged as suspect by `ALLOWANCE_INVESTIGATION.md` §5.4(b) (52,54% → 63% from 1 August 2026). This recomputation holds it constant; if that ticket lands, E4 must be recomputed again.

**m12 E4 garnishment cascade**, following through at 291.62:

| Line | Current | Corrected |
|---|---|---|
| 122 Net for art. 1409 | 2,246.53 | **2,252.92** |
| 132 Fourth band, 100% | 319.53 | **325.92** |
| 133 Total attachable | 450.73 | **457.12** |
| 137 Net before attachment | 2,246.53 | **2,252.92** |
| 140 **Net paid to the employee** | 1,772.91 | **1,772.91 — unchanged** ✅ |
| 142 maintenance-debt sentence | 2,246.53 | **2,252.92** |

The self-cancelling property noted in `ALLOWANCE_INVESTIGATION.md` §5.2 holds again: the entire EUR 6.39 delta lands in the 100%-attachable band, so the final net paid is unchanged. Flag this in the ticket so a reviewer does not "correct" it.

### 5.3 Interaction with the allowance fix

These two fixes **collide in the same lines** and must be applied as one edit, not sequentially. `m06_tax.md:133` and `m06_tax.md:162`, and m12 E4 lines 117–120, are on both inventories. The figures in §5.2 above already incorporate the corrected allowance (2,987.98) and supersede the child-affected rows marked ⚠️ in `ALLOWANCE_INVESTIGATION.md` §5.2.

---

## 6. Adjacent findings — flagged, NOT resolved

**(a) The withholding base scale brackets in the CCG are the assessment brackets. This is a new defect affecting every worked example.**

`ALLOWANCE_INVESTIGATION.md` §2.2 verified 16,720 / 29,510 / 51,070 against BS 12 August 2026 Table III A and concluded they "must **not** be touched". That conclusion is correct **for the art. 130 WIB 92 statement at `m06_tax.md:172–177`**, which describes the assessment scale.

But the CCG also uses those same numbers in the **withholding formula** at `m06_tax.md:127–131` and in the F-steps of every worked example. Annex III **nr. 31** sets its own base scale:

```
van 0,01 EUR tot 16.710 EUR              26,75 pct.
van 16.710,01 EUR tot 29.500 EUR          4.469,93 EUR + 42,80 pct. boven 16.710 EUR
van 29.500,01 EUR tot 51.050 EUR          9.944,05 EUR + 48,15 pct. boven 29.500 EUR
boven 51.050 EUR                         20.320,38 EUR + 53,50 pct. boven 51.050 EUR
```

**16,710 / 29,500 / 51,050** — the same round-down-to-the-lower-10 convention as the allowance, and exactly the pattern §4.1 predicted. The three published constants recompute exactly from these thresholds, so the reading is certain.

Consequence: **every** F-step in m06 and m12 is computed on the wrong scale, including the childless examples that the allowance fix treated as needing only a G-step change. Concretely, m06 §6.1 childless resolves to **826.70**, not the 826.52 projected in `ALLOWANCE_INVESTIGATION.md` §5.2. That projection should be treated as superseded. This needs its own ticket and a full recomputation sweep; it is outside this investigation's scope and no other example was recomputed here.

**(b) Missing rules in the child provision.** Disabled child counts double (nr. 8); relief continues to year-end on the death of a dependant (nr. 10). Neither appears in the CCG.

**(c) Child relief on exceptional remuneration appears to be missing entirely.** The nr. 55 percentage table (§2.5(a)) applies to bonuses, end-of-year premium and double holiday pay. No reference to dependent children was found in `m04_compensation.md` or `m08_leave.md`. If confirmed, the CCG over-withholds on bonuses for employees with children below the income ceilings.

**(d) The scale II / spouse thresholds should be checked.** nrs. 33, 40.2 and 40.3 give net monthly thresholds of EUR 174 / 290 / 579 and reductions of 1,740 / 3,474, computed under nr. 11.2 (gross less social contributions, less 20%). Not verified against the CCG in this pass.

---

## 7. Confidence

| Claim | Confidence | Basis |
|---|---|---|
| Annex III grants child relief as a flat reduction of the basisbelasting, not an allowance supplement | **Certain** | nr. 38 verbatim, column heading *"VERMINDERING VAN DE BASISBELASTING"*; nr. 37 places it after the basisbelasting is fixed |
| Child reduction table 624 / 1,656 / 4,404 / … / 21,996 (+3,864) | **Certain** | Annex III nr. 38, primary text, KB of 11 December 2025 |
| Table is unamended as at 14 Aug 2026 | **High** | KB of 24 July 2026 amends only nrs. 45.2, 45.3, 46.2.2, 78.3.2, 131 and the young-athlete provision (per `ALLOWANCE_INVESTIGATION.md` §2.3, which swept the Staatsblad to today); numbering verified present in this text |
| Every table row divisible by 12 | **Certain** | Arithmetic; holds in the 2023 edition too |
| Basic allowance 11,170 / reduction 2,987.98 | **Certain** — upgraded from "High" | Now confirmed from the annex text (nr. 32), not only Securex. **Closes the residual gap in `ALLOWANCE_INVESTIGATION.md` §6.** |
| Annex III base scale is 16,710 / 29,500 / 51,050 | **Certain** | nr. 31; all three published constants recompute exactly |
| EUR 2,030 is a mis-applied disabled-taxpayer figure | **High** | Exact match to art. 131 3rd para. AJ2027; adjacent row to the allowance in Table I; the one-child slot is occupied by 2,130 |
| EUR 5,230 and 11,720 match no official table | **High** | Internal-ratio test excludes any indexed art. 132 year; no single coefficient fits |
| Recomputed 688.70 and 291.62 | **High** | Computed from primary text; inputs taken from the CCG unchanged; cross-checked by the exact 138.00 = 1,656 ÷ 12 identity |
| Child relief absent from CCG exceptional-pay treatment | **Probable** | Grep of m04/m08 found no child reference; not an exhaustive read of those modules |

**Residual gap.** The annex was read from Securex's coordinated PDF rather than the Staatsblad edition, because the BS text is not machine-readable (the obstacle recorded in `ALLOWANCE_INVESTIGATION.md` §6). Six independent cross-checks pass (§2.1) and the figures reconcile with sources of a different house, so the risk of a transcription error in the reproduction is low. If certification against the BS itself is required before the fix ships, the target is the KB of 11 December 2025, BS 29 December 2025, p. 97613.

---

## 8. Recommendation

1. **Fix the mechanism, not the numbers.** Replace step 7 in `m06_tax.md:133` with two steps: the allowance reduction (EUR 2,987.98, per the allowance ticket) and a separate flat reduction from the nr. 38 table. Substituting corrected supplements into the old × 26.75% formula would keep the artifact structurally wrong.
2. **Publish the table in full** (§3), not just the first three rows — the CCG's "rising further beyond" is not implementable, and payroll needs all nine rows plus the >8 rule.
3. **Do not carry the art. 132 figures across.** 2,130 / 5,130 / 11,440 are correct for the annual assessment and wrong for payroll. Consider stating both explicitly in Module 6, as recommended for the allowance — the same two-instrument split, one level down, and a client will ask.
4. **Apply this fix and the allowance fix as a single edit.** They collide in the same lines (§5.3).
5. **Fix `_prompts/wtc.md:53`** as well as the two WTC source files, or the next rebuild reintroduces the wrong triple.
6. **Open a new, high-priority ticket for the base-scale brackets** (§6(a)). It is broader than either allowance ticket: it changes every worked example in m06 and m12, including the ones previously assessed as unaffected.
7. **Open tickets for §6(b), (c), (d).** Item (c) is a potential systematic over-withholding on bonuses.
8. **Record the Securex coordinated-annex URL** in the source register. It is the machine-readable route to Annex III and resolves the obstacle that blocked the previous investigation; it will be needed again when the expected allowance decree lands.

---

## 9. Sources

**Primary — Annex III, income year 2026**

- *Bijlage III van het Koninklijk besluit tot uitvoering van het WIB 1992*, as annexed to the **Koninklijk besluit van 11 december 2025** (BS 29.12.2025, p. 97613). Coordinated text, 44 pp., retrieved as [`Bijlage-III-KB-WIB-2026.pdf`](https://www.securex.be/getattachment/ceca9705-6370-4e55-9fee-3500a442a156/Bijlage-III-KB-WIB-2026.pdf) from the [Securex Annex III overview page](https://www.securex.be/nl/lex4you/werkgever/themas/verlonen/fiscale-loonlasten-bedrijfsvoorheffing/bijlage-iii-kb-wib-92-wettekst). Provisions relied on: nrs. 8, 10, 11, 28, 31, 32, 34.2, 37, 38, 39, 40, 41, 42, 55, 108, 111.
- Superseded comparator, used only to establish that the drafting convention is stable: [`Bijlage-III-KB-WIB.pdf`](https://www.securex.be/getattachment/4f3a2c18-d725-4781-84d5-ff08350a924c/Bijlage-III-KB-WIB.pdf) — annex to the KB of 19 December 2022, income year 2023 (allowance 9,620; one-child reduction 540). **Do not cite for current figures.**

**Primary — assessment side, via the predecessor investigation**

- *Bericht in verband met de automatische indexering inzake inkomstenbelastingen — Aanslagjaar 2027*, BS 12.08.2026, p. 43734, NUMAC 2026006085 — Table I (art. 131 3rd para., 870 → 2.030) and Table II (art. 132, 935/2.250/5.020 → 2.130/5.130/11.440)
- *Koninklijk besluit van 24 juli 2026 tot wijziging van de toepassingsregels voor de bedrijfsvoorheffing*, BS 30.07.2026 Ed. 2, NUMAC 2026005690 — operative list confirms nrs. 37–41 unamended

**Secondary — corroboration of nr. 32**

- [Securex — Maandelijkse bezoldigingen (bijlage III)](https://www.securex.be/nl/lex4you/werkgever/themas/verlonen/fiscale-loonlasten-bedrijfsvoorheffing/maandelijkse-bezoldigingen-\(en-ermee-gelijkgestelde-inkomsten,-met-uitzondering-van-vervangingsinkom) — confirms 11.170 / 2.987,98, and describes the child reduction as *"een forfaitair bedrag dat per kind ten laste wordt toegekend"* (a flat amount), independently corroborating the mechanism finding
- SSGPI service note SSGPI-RIO-2026/9, 8 January 2026 — 52,54% as the pre-August work bonus value, used to date the PDF edition

**Internal**

- `BE-compliance/07-qa-crosscheck/ALLOWANCE_INVESTIGATION.md` — §4.1 rounding conventions, §2.3 the 24 July 2026 decree's operative list, §5.4(a) the original flag, §6 the residual gap now closed
