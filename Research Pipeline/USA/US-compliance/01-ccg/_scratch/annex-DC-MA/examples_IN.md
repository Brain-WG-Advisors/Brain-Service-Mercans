Each example is computed from the statutory parameters listed in this annex and checked against the result published by the authority. Amounts round half-up to the cent unless the line states another rule.

**Example IN-1: weekly wages 800.00 with deduction constants A5, B3, B1 and C2, county rate 1.00% as used in the Departmental Notice 1 example (payroll from 2026-10-01).**

| Line | Calculation | Result |
|---|---|---|
| Constant A5 | 5 x [[FACT:in.wh.exemption.personal=1,000]] / 52, two decimals | 96.15 |
| Constant B3 | 3 x [[FACT:in.wh.exemption.dependent=1,500]] / 52, two decimals | 86.54 |
| Constant B1 | 1 x [[FACT:in.wh.exemption.dependent=1,500]] / 52, two decimals | 28.85 |
| Constant C2 | 2 x [[FACT:in.wh.exemption.adopted_child=3,000]] / 52, two decimals | 115.38 |
| Total constants | 96.15 + 86.54 + 28.85 + 115.38 | 326.92 |
| Taxable wages | 800.00 - 326.92 | 473.08 |
| State withholding | 473.08 x [[FACT:in.pit.rate=2.95]] % = 13.9559, half-up to the cent | [[FACT:in.oracle.dn1.example.state=13.96]] |
| County withholding | 473.08 x 1.00 % (example county rate) = 4.7308 | [[FACT:in.oracle.dn1.example.county=4.73]] |

Computed result = published [[FACT:in.oracle.dn1.example.state=13.96]] (match); [[FACT:in.oracle.dn1.example.county=4.73]] = published [[FACT:in.oracle.dn1.example.county=4.73]] (match). The county rate in production is the employee's county rate from the county chart (IN.2c).
