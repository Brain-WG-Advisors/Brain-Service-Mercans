# Dedicated Investigation — Module 9 redundancy worked example, "April salary" withholding of EUR 1,003.36

**Date:** 2026-08-13
**Scope:** Investigation and reporting only. **No artifact was modified.**
**Target artifact (read-only):** `BE-compliance/01-ccg/modules/m09_termination.md`
**Status:** **RESOLVED — the figure is wrong. Confident replacement value identified: EUR 1,035.58.**

---

## 0. Facts reconfirmed directly from the file

All figures below were read fresh from `m09_termination.md` and are quoted, not transcribed from the tasking prompt.

| Location | Line | Content |
|---|---|---|
| Facts paragraph | 166 | White-collar, JC 200, single, no dependants, dismissed with immediate effect 30 April 2026, gross monthly EUR 4,500.00, company car benefit EUR 250.00/month, meal vouchers EUR 10.00/day employer share EUR 8.91 |
| Step 7 table | 213 | `\| April salary \| 4,500.00 \| 588.15 \| Ordinary scale \| 1,003.36 \|` |
| Step 8 table | 221 | `\| April salary \| 4,500.00 \| 588.15 \| 1,003.36 \| 2,908.49 \|` |
| Step 8 total row | 225 | Gross **54,381.28** \| SS **7,107.63** \| WH **24,201.73** \| Net **23,071.92** |

Two things worth stating up front, because they shape the whole investigation:

1. **Employee SS of 588.15 is correct.** 4,500.00 × 13.07% = 588.15 exactly. The company car benefit is correctly excluded from the ordinary employee SS base. No issue on this column.

2. **1,003.36 is not an isolated typo in one cell — it is propagated.** The Step 8 net of 2,908.49 is exactly 4,500.00 − 588.15 − 1,003.36, and the Step 8 totals row is exactly consistent with it (the four withholding rows sum to 24,201.73 to the cent, and 54,381.28 − 7,107.63 − 24,201.73 = 23,071.92). So the wrong number was computed once and then carried arithmetically into three further cells. **Any correction requires four edits, not one.** This is important for whoever applies the fix.

### The reference method (Module 6.1.1, quoted verbatim from `m06_tax.md:120-138`)

```
 Step 1  A = monthly gross taxable remuneration
 Step 2  B = A − employee social security contribution (13.07% of gross)
 Step 3  C = B x 12                            (annualisation)
 Step 4  D = lump-sum professional expenses = 30% of C, capped at EUR 6,070
 Step 5  E = C − D
 Step 6  F = tax on E: 26.75% / 42.80% / 48.15% / 53.50% at 16,720 / 29,510 / 51,070
 Step 7  G = 26.75% x (11,180 + dependant supplements)
 Step 9  Annual withholding = F − G − H, floored at zero
 Step 10 Monthly withholding = annual withholding / 12, rounded to the cent
```

I implemented this in Decimal arithmetic and **validated it against the CCG's own worked example** at `m06_tax.md:142-158` (gross EUR 4,000, single, no dependants): my engine returns **826.30**, matching the document to the cent, with every intermediate line (B 3,477.20 / C 41,726.40 / D 6,070 / E 35,656.40 / F 12,906.21 / G 2,990.65) also matching. The engine is therefore a faithful implementation of this CCG's own documented method, not an independent reimplementation that might differ in convention.

Applying it to gross 4,500.00 gives **EUR 1,035.58** — the H1 figure, which I independently reproduce.

---

## 1. Stale 2025 parameters, properly sourced

**Conclusion: RULED OUT — and ruled out decisively, on a directional argument that does not depend on getting the 2025 figures exactly right.**

I sourced the actual income-year-2025 figures rather than guessing them:

| Parameter | Income year 2026 (used in this CCG) | Income year 2025 (AY 2026) | Source |
|---|---|---|---|
| Withholding scale bands | 16,720 / 29,510 / 51,070 | **16,310 / 28,790 / 49,820** | [Attentia, *De bedrijfsvoorheffing in 2025*](https://www.attentia.be/nl/nieuws/de-bedrijfsvoorheffing-in-2025/) |
| Withholding tax-free allowance | 11,180 | **10,900** | Attentia (quoted: *"Er geldt (in 2025) een belastingvrije som (binnen de laagste tariefschijf) van 10.900,00 euro"*) |
| PIT brackets | — | 16,320 / 28,800 / 49,840 | [Practicali, *Geïndexeerde bedragen AJ 2026*](https://www.practicali.be/blog/geindexeerde-bedragen-aj-2026) |
| PIT basic allowance | — | **10,910** | Practicali |
| Lump-sum professional expenses (employees) | 30%, capped 6,070 | **30%, capped 5,930** | Practicali; corroborated by [Securex](https://www.securex.be/nl/lex4you/werkgever/nieuws/nieuwe-regels-bedrijfsvoorheffing-voor-2025) |

Rates (26.75 / 42.80 / 48.15 / 53.50%) are unchanged between the two years.

**The decisive point is directional.** Every single 2025 parameter moves the calculation the *wrong way*: the bands are **lower** (income reaches higher rates sooner), the allowance is **lower** (smaller reduction at step G), and the expense cap is **lower** (larger taxable base). All three push withholding **up**. The target, 1,003.36, is **below** the 2026 result of 1,035.58. No consistent set of older Belgian parameters can produce it.

Computed, using the full year-set in each case (gross 4,500, single, no dependants):

| Parameter vintage | Full set used | Monthly withholding |
|---|---|---|
| **2026 (this CCG's documented set)** | 16,720/29,510/51,070, cap 6,070, allowance 11,180 | **1,035.58** |
| 2025 | 16,310/28,790/49,820, cap 5,930, allowance 10,900 | 1,056.13 |
| 2025 (allowance variant 10,910) | as above, allowance 10,910 | 1,055.91 |
| 2024 | 15,820/27,920/48,320, cap 5,750, allowance 10,570 | 1,081.14 |
| 2023 | 15,200/26,830/46,440, cap 5,520, allowance 10,160 | 1,112.67 |
| — | **TARGET** | **1,003.36** |

The stale-parameter hypothesis is not merely unsupported; it is **excluded by the direction of the error**. Going further back in time monotonically increases the gap. This also disposes of the earlier single-substitution tests H3/H4/H5 as a family: they only appeared to move toward the target because each substituted a figure *larger* than the real one in the direction that reduces tax, which is the opposite of what a genuine stale-year error does.

---

## 2. Is there a genuine final-pay-period rule?

**Conclusion: NO SUCH RULE EXISTS.** The last ordinary salary before a termination is withheld exactly like any other month.

Basis for this conclusion:

- **The Belgian system is explicitly non-cumulative and per-payment.** This CCG states it itself at `m06_tax.md:24` (*"It is calculated per payment, by annualisation"*) and `m06_tax.md:255` (*"Belgium annualises the current payment only; it does not forecast the year"*). A non-cumulative system has no year-to-date state to true up at exit — which is structurally why no leaver adjustment exists. The CCG reinforces this at `m06_tax.md:228` for the mirror-image case: a joining month is annualised as if it were a full monthly salary and **"No catch-up is performed later."** The same logic applies symmetrically at departure.

- **Searching the CCG itself:** grep for `leaving|departure month|final month|last month|leaver` across `m06_tax.md` returns **no matches**. The CCG documents a joining-month rule and no leaving-month rule — consistent with there being none to document.

- **External check.** I checked Securex's Lex4You reference page on monthly remuneration ([*Maandelijkse bezoldigingen*](https://www.securex.be/nl/lex4you/werkgever/themas/verlonen/fiscale-loonlasten-bedrijfsvoorheffing/maandelijkse-bezoldigingen-(en-ermee-gelijkgestelde-inkomsten,-met-uitzondering-van-vervangingsinkom)), a Belgian social secretariat's authoritative practitioner reference keyed to Annex III points 13–30. It describes a single uniform procedure — gross annual taxable income → less lump-sum expenses → annual tax → **÷ 12** — with **no variant for a final month**. Confirmed explicitly: the page *"does not describe any special or adjusted calculation method for the final monthly salary upon employment termination."*

- **What *is* specific to termination** is the treatment of the severance itself, and this CCG already handles it correctly and separately: the notice indemnity goes down the exceptional-remuneration route (Step 6, `m09_termination.md:203-207`, gross × 13.92 keyed to the exceptional table), and holiday pay and the end-of-year premium likewise. Those are genuinely termination-specific. The **ordinary April salary is not** — it is an ordinary monthly payment that happens to be the last one.

**Limitation, stated honestly:** I attempted to retrieve the primary text of Annex III to KB/WIB92 directly from `financien.belgium.be` to quote the point numbering, but the PDF returned encoded streams that could not be parsed. My conclusion therefore rests on (a) the structural argument from non-cumulativity, (b) this CCG's own explicit statements, and (c) a professional-grade secondary source that maps to Annex III point numbers, rather than on a direct quotation of the Royal Decree. I regard the conclusion as solid, but a reviewer wanting a citation to the primary instrument will need to pull Annex III text separately.

---

## 3. Broader systematic parameter search

I wrote a grid search varying **every** plausible input simultaneously:

- **Gross basis** (3): 4,500.00 · 4,478.20 (less employee meal-voucher share 20 × 1.09) · 4,285.71 (20/21-day proration)
- **Additions to the tax base** (6): none · car +250.00 · car+meals +428.20 · meals +178.20 · car/12 +20.83 · EOY/12 +375.00
- **Expense cap** (12): 6,070 · 5,930 · 5,950 · 5,910 · 5,880 · 5,750 · 5,520 · 4,920 · 6,000 · 6,100 · 5,000 · 13,530
- **Tax-free allowance** (10): 11,180 · 10,910 · 10,900 · 10,570 · 10,160 · 9,270 · 11,570 · 12,000 · 13,500
- **Bracket sets** (5): BV2026 · BV2025 · PIT2025 · BV2024 · BV2023
- **Expense percentage** (3): 30% · 35% · 28.7%
- **Allowance reduction rate** (2): 26.75% · 25%
- **Annual-base rounding** (5): none · down to 15 · 12 · 10 · 1 (the real Annex III rounds the annual base down to a multiple of EUR 15)
- **SS rounding** (2): rounded to cent · unrounded

**648,000 combinations tested.**

### Result: 6 exact hits — all statistically indistinguishable from noise

This is the key finding of Step 3, and it needs the density analysis to interpret correctly. A naive reading ("6 combinations reproduce the figure!") is wrong.

The 648,000 combinations produce 37,745 distinct cent-values spanning 594.56–1,379.49, with **308,844 combinations landing in the 950–1,150 window** — i.e. roughly **15.4 combinations per exact cent** by pure chance in the region where the target sits.

**Expected chance hits at any given cent: ~15. Observed at 1,003.36: 6.**

The target is *under-represented* relative to chance. The grid found **nothing**. A search this wide will always throw off coincidental exact matches; the correct test is whether the target attracts more mass than its neighbours, and it does not.

For completeness, the 6 hits all require the same incoherent 6-way conjunction — 20/21-day prorated gross **and** one-twelfth of the car benefit **and** a 5,910 cap (a figure that exists in no year) **and** a 10,910 allowance (an *income tax* figure, not a *withholding* figure) **and** 2024 brackets **and** a 25% allowance reduction rate instead of 26.75%. Three of the six "distinct" hits are duplicates differing only in the expense percentage, which is inert because the cap binds. No plausible authoring path produces that combination.

### Single-parameter reverse solve

For each parameter individually, the value that *would* be required to land on 1,003.36 (2026 set otherwise):

| Parameter | Required value | Real value | Verdict |
|---|---|---|---|
| Monthly taxable base B | 3,844.93 | 3,911.85 | 66.92 too low, unexplained |
| Implied monthly gross | 4,423.02 | 4,500.00 | not a round figure, appears nowhere in the CCG |
| Tax-free allowance | 12,625.38 | 11,180 (2026) / 10,900 (2025) | exists in no year |
| Expense cap | 6,872.99 | 6,070 (2026) / 5,930 (2025) | exists in no year |
| 3rd-bracket floor | 36,736.92 | 29,510 | exists in no year |
| 2nd-bracket floor | 19,128.97 | 16,720 | exists in no year |
| Employee SS rate | 14.5571% | 13.07% | not a Belgian rate |

**Every** required substitution is a non-round number that corresponds to no Belgian statutory figure in any year. There is no single-parameter story, and the grid shows no multi-parameter story either.

### What the figure is *not*

- Not the car-inclusive base (that is 1,155.96 — I reproduce H2).
- Not any exceptional-payment rate applied to this base: 3,911.85 × 53.50% = 2,092.84; × 26.75% = 1,046.42; none is 1,003.36.
- Not a rounding artefact: the Annex III EUR 15 annual-base rounding is worth at most ~0.60/month, an order of magnitude below the 32.22 gap.

---

## 4. Cross-check against every other worked example in the CCG

**Conclusion: no copy-paste origin. The figure appears nowhere else in the CCG.**

Complete inventory of ordinary-scale monthly withholding results across all modules:

| Module | Location | Gross | Monthly withholding |
|---|---|---|---|
| 6.1.1 | `m06_tax.md:158` | 4,000.00 | 826.30 |
| 6.1.1 (2 children) | `m06_tax.md:162` | 4,000.00 | 709.71 |
| 6 (non-resident scale III) | `m06_tax.md:345` | 4,000.00 | 1,075.52 |
| 12 example 1 | `m12_examples.md:26` | — | 617.01 |
| 12 example 2 | `m12_examples.md:62` | — | 0.00 |
| 12 example 3 | `m12_examples.md:90` | — | 874.01 |
| 12 example 4 | `m12_examples.md:120` | — | 298.01 |
| 12 example 5 | `m12_examples.md:163` | — | 871.58 |
| 12 example 6 | `m12_examples.md:220` | — | 283.63 |
| **9 (this one)** | `m09_termination.md:213` | **4,500.00** | **1,003.36** |

- **No other example uses a monthly gross near EUR 4,500.** Every ordinary-scale example in the CCG uses 4,000.00 or a base not stated as a round monthly gross.
- **No other example produces a withholding near 1,003.** The nearest values are 1,075.52 (the non-resident scale III case, 72.16 away, and structurally different — it grants no allowance at all) and 874.01.
- Module 9's own second example (`m09_termination.md:297-299`) uses gross 3,200.00 and the exceptional route at 46.44% — unrelated.
- Module 7's examples use exceptional-payment percentages, not the ordinary scale.

The figure has no sibling anywhere in the document. It appears to have been generated once, in place, by a method that cannot be reconstructed.

---

## 5. Conclusion and proposed correction

### Finding

**EUR 1,003.36 is incorrect.** It is not reproducible under the method this CCG documents in Module 6.1.1, not reproducible under any historical Belgian parameter vintage (all of which err in the opposite direction), not reproducible under any of 648,000 systematic parameter permutations beyond chance-level coincidence, not attributable to a genuine termination-specific rule (no such rule exists), and not traceable to any other worked example in the CCG.

The correct value under this CCG's own documented and self-validated method is **EUR 1,035.58**, understating withholding by **EUR 32.22**.

I am confident in the *replacement value* because it is not a reverse-engineered guess — it is the direct output of the method the CCG itself specifies, from an engine validated to the cent against the CCG's own Module 6 example. I am **not** able to explain the *origin* of 1,003.36, and I am not going to invent one. The honest characterisation is: unexplained provenance, but demonstrably wrong, with an unambiguous correct replacement.

### A judgement call the reviewer should make consciously

There is a legitimate substantive question, independent of the arithmetic error: **should the company car benefit of EUR 250.00/month be in the April withholding base?**

Under Belgian rules the car benefit **is** taxable and would normally form part of the monthly withholding base, even though it is correctly excluded from the employee SS base (which is why 588.15 is right). Module 6 says so itself at `m06_tax.md:263`: *"Benefits in kind with an annual statutory value | Divided by 12 and added to each month."*

- **Reading A (salary line only, base 3,911.85) → 1,035.58.** Consistent with the table's own "Gross 4,500.00" column, which presents the line as the salary alone.
- **Reading B (salary + car, base 4,161.85) → 1,155.96.** Arguably the technically complete treatment for the month.

**My recommendation is Reading A (1,035.58)**, as the minimal, defensible correction: the row's own Gross column says 4,500.00, the summary table computes net from that same 4,500.00, and adopting Reading B would require also restating the Gross column and the Step 8 totals to include the benefit, which is a scope expansion rather than a correction. But this should be a deliberate decision, not a default — if the reviewer wants the example to model the car benefit in the final month's withholding, the number is 1,155.96 and further edits are needed.

### Exact before/after text (for a human to apply as a separate, deliberate step)

**No file was modified. Four edits are required** — the error is propagated into the net and the totals.

**Edit 1 — `m09_termination.md`, line 213 (Step 7 table)**

```
BEFORE: | April salary | 4,500.00 | 588.15 | Ordinary scale | 1,003.36 |
AFTER:  | April salary | 4,500.00 | 588.15 | Ordinary scale | 1,035.58 |
```

**Edit 2 — `m09_termination.md`, line 221 (Step 8 table, withholding and net)**

```
BEFORE: | April salary | 4,500.00 | 588.15 | 1,003.36 | 2,908.49 |
AFTER:  | April salary | 4,500.00 | 588.15 | 1,035.58 | 2,876.27 |
```
(net = 4,500.00 − 588.15 − 1,035.58 = 2,876.27)

**Edit 3 — `m09_termination.md`, line 225 (Step 8 total row)**

```
BEFORE: | **Total** | **54,381.28** | **7,107.63** | **24,201.73** | **23,071.92** |
AFTER:  | **Total** | **54,381.28** | **7,107.63** | **24,233.95** | **23,039.70** |
```
(gross and SS totals are unchanged; withholding +32.22, net −32.22 — both verified by recomputing all four rows)

**Edit 4 — the DOCX.** `BE-CCG-001-v1.0.docx` contains the rendered version of this module and carries the same three figures. It must be regenerated or edited in step, or the markdown and the deliverable will diverge.

### Side observation, explicitly out of scope and NOT part of the above conclusion

While sourcing the 2025 figures I noticed that two Belgian payroll providers (Securex and Synova) cite the 2026 withholding tax-free allowance as **EUR 11,170**, whereas this CCG uses **EUR 11,180** throughout. The tasking brief states the 2026 figures were confirmed elsewhere in this review, so I did not pursue it, and **it is immaterial to this investigation** — a 10-euro difference in the allowance is worth 0.22/month, nowhere near the 32.22 gap, and it moves in the wrong direction. I record it only so that it is not lost; it would need its own verification against Annex III before anyone acts on it, and search-summary quality on this specific point was poor (results conflated assessment year with income year). **Do not treat this as a finding.**

---

## Sources

- [Attentia — *De bedrijfsvoorheffing in 2025*](https://www.attentia.be/nl/nieuws/de-bedrijfsvoorheffing-in-2025/) — 2025 withholding bands and tax-free allowance
- [Practicali — *De geïndexeerde bedragen aanslagjaar 2026*](https://www.practicali.be/blog/geindexeerde-bedragen-aj-2026) — income year 2025 PIT brackets, allowance, lump-sum expense cap
- [Securex — *Nieuwe regels bedrijfsvoorheffing voor 2025*](https://www.securex.be/nl/lex4you/werkgever/nieuws/nieuwe-regels-bedrijfsvoorheffing-voor-2025) — corroboration of the 2025 expense cap
- [Securex Lex4You — *Maandelijkse bezoldigingen*](https://www.securex.be/nl/lex4you/werkgever/themas/verlonen/fiscale-loonlasten-bedrijfsvoorheffing/maandelijkse-bezoldigingen-(en-ermee-gelijkgestelde-inkomsten,-met-uitzondering-van-vervangingsinkom) — uniform monthly method keyed to Annex III points 13–30; no final-month variant
- [FPS Finance — Annex III to KB/WIB92](https://financien.belgium.be/sites/default/files/downloads/regel151213_NL.pdf) — attempted for primary-text confirmation; PDF not machine-readable (see limitation in §2)
- Internal: `BE-compliance/01-ccg/modules/m06_tax.md` (method and validation example), `m09_termination.md`, `m12_examples.md`
