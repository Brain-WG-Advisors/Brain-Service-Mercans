Each example is computed from the statutory parameters listed in this annex and checked against the result published by the authority. Amounts round half-up to the cent unless the line states another rule.

**Example LA-1: L-4 status 1, weekly wages 700.00 (R-1306 formula).**

| Line | Calculation | Result |
|---|---|---|
| Period deduction | [[FACT:la.wh.std_deduction.single=12,875]] / 52 | 247.5962 |
| Withholding | (700.00 - 247.5962) x [[FACT:la.pit.rate.flat=3.09]] % = 13.9793, half-up to the cent | [[FACT:la.oracle.r1306.example1.withholding=13.98]] |

Computed result = published [[FACT:la.oracle.r1306.example1.withholding=13.98]] (match).

**Example LA-2: L-4 status 2, biweekly wages 4,600.00 (R-1306 formula).**

| Line | Calculation | Result |
|---|---|---|
| Period deduction | [[FACT:la.wh.std_deduction.joint=25,750]] / 26 | 990.3846 |
| Withholding | (4,600.00 - 990.3846) x [[FACT:la.pit.rate.flat=3.09]] % = 111.5371, half-up to the cent | [[FACT:la.oracle.r1306.example2.withholding=111.54]] |

Computed result = published [[FACT:la.oracle.r1306.example2.withholding=111.54]] (match).
