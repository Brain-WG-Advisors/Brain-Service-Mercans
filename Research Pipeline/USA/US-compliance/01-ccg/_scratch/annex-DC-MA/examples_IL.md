Each example is computed from the statutory parameters listed in this annex and checked against the result published by the authority. Amounts round half-up to the cent unless the line states another rule.

**Example IL-2: weekly wages 800.00, IL-W-4 Line 1 = 2, Line 2 = 2 (IL-700-T example).**

| Line | Calculation | Result |
|---|---|---|
| Annual exemptions | 2 x [[FACT:il.wh.exemption.line1=2,925]] + 2 x [[FACT:il.wh.exemption.line2=1,000]] | 7,850.00 |
| Weekly exemption | 7,850.00 / 52, rounded to the cent | 150.96 |
| Taxable wages | 800.00 - 150.96 | 649.04 |
| Withholding | 649.04 x [[FACT:il.pit.rate.flat=4.95]] % = 32.1275, half-up to the cent | [[FACT:il.oracle.il700t.example2.withholding=32.13]] |

Computed result = published [[FACT:il.oracle.il700t.example2.withholding=32.13]] (match).

**Example IL-1: weekly wages 300.00, IL-W-4 Line 1 = 2, Line 2 = 1 (IL-700-T example).**

| Line | Calculation | Result |
|---|---|---|
| Annual exemptions | 2 x [[FACT:il.wh.exemption.line1=2,925]] + 1 x [[FACT:il.wh.exemption.line2=1,000]] | 6,850.00 |
| Weekly exemption | 6,850.00 / 52, rounded to the cent | 131.73 |
| Taxable wages | 300.00 - 131.73 | 168.27 |
| Withholding | 168.27 x [[FACT:il.pit.rate.flat=4.95]] % = 8.3294, half-up to the cent | 8.33 |

The formula with the 2026 exemption amounts gives 8.33; the IL-700-T prints [[FACT:il.oracle.il700t.example1.withholding=8.38]]. ⚠️ RESEARCH-GAP: the inputs of IL-700-T example 1 do not reproduce its printed result with the 2026 exemption amounts; the example's allowance counts or wage must be re-read before it is used as a test case (open item `il.oracle.il700t.example1.inputs`, non-blocking).
