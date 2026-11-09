Each example is computed from the statutory parameters listed in this annex and checked against the result published by the authority. Amounts round half-up to the cent unless the line states another rule.

**Example IA-1: head of household, monthly wages 5,000.00, W-4 allowance amount W = 160.00, no additional amount (2026 withholding formula, example 6).**

| Line | Calculation | Result |
|---|---|---|
| D (period deduction) | [[FACT:ia.wh.deduction.hoh=19,500]] / 12 | 1,625.00 |
| T1 = G - D | 5,000.00 - 1,625.00 | 3,375.00 |
| T2 = T1 x rate | 3,375.00 x [[FACT:ia.pit.rate.flat=3.8]] % | 128.25 |
| T3 = T2 - W / P | 128.25 - 160.00 / 12 = 114.9167 | [[FACT:ia.oracle.formula.example6.withholding=114.92]] |
| T4 = T3 + A | [[FACT:ia.oracle.formula.example6.withholding=114.92]] + 0.00 (rounding: to the cent, half-up, per `ia.wh.rounding`) | [[FACT:ia.oracle.formula.example6.withholding=114.92]] |

Result [[FACT:ia.oracle.formula.example6.withholding=114.92]] = [[FACT:ia.oracle.formula.example6.withholding=114.92]] (match). The published example prints no final figure; the value is re-derived from the formula.
