Each example is computed from the statutory parameters listed in this annex and checked against the result published by the authority. Amounts round half-up to the cent unless the line states another rule.

**Example HI-1: single, 3 allowances, weekly wages 500.00 (Booklet A, Part 1 annualised method).**

| Line | Calculation | Result |
|---|---|---|
| Annual wages | 500.00 x 52 | 26,000.00 |
| Allowances | 3 x [[FACT:hi.wh.allowance.annual=1,144]] | 3,432.00 |
| Taxable wages | 26,000.00 - 3,432.00 - [[FACT:hi.wh.lump_sum_allowance.annual=4,350]] | 18,218.00 |
| Bracket | above [[FACT:hi.wh.bracket.single.2.ceiling=14,400]] up to [[FACT:hi.wh.bracket.single.3.ceiling=19,200]] | bracket 3 |
| Annual tax | [[FACT:hi.wh.bracket.single.3.base_tax=288]] + (18,218.00 - [[FACT:hi.wh.bracket.single.2.ceiling=14,400]]) x [[FACT:hi.wh.bracket.single.3.rate=5.5]] % | 497.99 |
| Weekly withholding | 497.99 / 52, half-up to the cent | [[FACT:hi.oracle.booklet_a.part1.withholding_weekly=9.58]] |

Computed result = published [[FACT:hi.oracle.booklet_a.part1.withholding_weekly=9.58]] (match).
