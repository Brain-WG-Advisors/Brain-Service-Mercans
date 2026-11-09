Each example is computed from the statutory parameters listed in this annex and checked against the result published by the authority. Amounts round half-up to the cent unless the line states another rule.

**Example ID-1: single, biweekly wages 1,212.00, payroll on or after 2026-07-23 (percentage computation).**

| Line | Calculation | Result |
|---|---|---|
| Taxable wages | 1,212.00 - [[FACT:id.wh.zero_bracket.single.biweekly=619]] | 593.00 |
| Tax | 593.00 x [[FACT:id.pit.rate.flat=5.3]] % | 31.4290 |
| Withholding | rounded to the nearest whole dollar (`id.wh.rounding`) | 31 |

Computed result = published [[FACT:id.oracle.stc.single_biweekly.withholding=31]] (match).

Example ID-2 (married, weekly 1,000.00, published result [[FACT:id.oracle.stc.married_weekly.withholding=20]]) is not reproduced: the published example uses a zero bracket that matches neither the table in force before 2026-07-23 nor the table in force from that date. See the open item `id.wh.example_threshold_discrepancy` in ID.2; use the wage-bracket table for numbers.
