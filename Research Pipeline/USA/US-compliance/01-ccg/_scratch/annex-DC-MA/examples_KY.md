Each example is computed from the statutory parameters listed in this annex and checked against the result published by the authority. Amounts round half-up to the cent unless the line states another rule.

**Example KY-1: monthly wages 3,270.00 (2026 formula sheet).**

| Line | Calculation | Result |
|---|---|---|
| Annual wages | 3,270.00 x 12 | 39,240.00 |
| Annual tax | (39,240.00 - [[FACT:ky.wh.std_deduction=3,360]]) x [[FACT:ky.pit.rate.flat=3.5]] % | 1,255.80 |
| Monthly withholding | 1,255.80 / 12, half-up to the cent | [[FACT:ky.oracle.formula.monthly_3270=104.65]] |

Computed result = published [[FACT:ky.oracle.formula.monthly_3270=104.65]] (match).

**Example KY-2: biweekly wages 1,500.00 (2026 formula sheet).**

| Line | Calculation | Result |
|---|---|---|
| Annual wages | 1,500.00 x 26 | 39,000.00 |
| Annual tax | (39,000.00 - [[FACT:ky.wh.std_deduction=3,360]]) x [[FACT:ky.pit.rate.flat=3.5]] % | [[FACT:ky.oracle.formula.biweekly_1500.annual=1,247.40]] |
| Biweekly withholding | [[FACT:ky.oracle.formula.biweekly_1500.annual=1,247.40]] / 26, half-up to the cent | [[FACT:ky.oracle.biweekly_1500.result=47.98]] |

The annual tax matches the published figure (match). The formula sheet shows a whole-dollar per-period figure without stating a rounding rule; see the open item `ky.wh.rounding.tax` in KY.2.
