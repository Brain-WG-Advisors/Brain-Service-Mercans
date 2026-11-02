Each example is computed from the statutory parameters listed in this annex and checked against the result published by the authority. Amounts round half-up to the cent unless the line states another rule.

**Example DE-1: single, 1 exemption, annual wages 25,000.00, weekly payroll (Withholding Tax Guide example 1).**

| Line | Calculation | Result |
|---|---|---|
| Annual wages | example input | 25,000.00 |
| Standard deduction (single) | 25,000.00 - [[FACT:de.wh.std_deduction.single=3,250]] | 21,750.00 |
| Bracket 1: 0 to [[FACT:de.pit.bracket.1.ceiling=2,000]] | 0 % (no tax) | 0.00 |
| Bracket 2: 3,000.00 above [[FACT:de.pit.bracket.1.ceiling=2,000]] | 3,000.00 x [[FACT:de.pit.bracket.2.rate=2.2]] % | 66.00 |
| Bracket 3: 5,000.00 above [[FACT:de.pit.bracket.2.ceiling=5,000]] | 5,000.00 x [[FACT:de.pit.bracket.3.rate=3.9]] % | 195.00 |
| Bracket 4: 10,000.00 above [[FACT:de.pit.bracket.3.ceiling=10,000]] | 10,000.00 x [[FACT:de.pit.bracket.4.rate=4.8]] % | 480.00 |
| Bracket 5: 1,750.00 above [[FACT:de.pit.bracket.4.ceiling=20,000]] | 1,750.00 x [[FACT:de.pit.bracket.5.rate=5.2]] % | 91.00 |
| Annual tax before credit | sum of bracket amounts | 832.00 |
| Personal credit | 832.00 - 1 x [[FACT:de.wh.personal_credit.per_exemption=110]] | 722.00 |
| Weekly withholding | 722.00 / 52, half-up to the cent | [[FACT:de.oracle.guide.example1.withholding_weekly=13.88]] |

Computed result = published [[FACT:de.oracle.guide.example1.withholding_weekly=13.88]] (match).

**Example DE-2: supplemental payment 5,000.00 paid separately to an employee earning 500.00 weekly, single, 1 exemption (annualised-with minus annualised-without, per `de.wh.supplemental.method`).**

| Line | Calculation | Result |
|---|---|---|
| Annual regular wages | 500.00 x 52 | 26,000.00 |
| Tax without the bonus | tax on (26,000.00 - [[FACT:de.wh.std_deduction.single=3,250]]) - [[FACT:de.wh.personal_credit.per_exemption=110]] | 774.00 |
| Tax with the bonus | tax on (26,000.00 + 5,000.00 - [[FACT:de.wh.std_deduction.single=3,250]]) - [[FACT:de.wh.personal_credit.per_exemption=110]] | 1,043.625 |
| Withholding on the bonus | 1,043.625 - 774.00 = 269.625, half-up to the cent | [[FACT:de.oracle.guide.example2.supplemental=269.63]] |

Computed result = published [[FACT:de.oracle.guide.example2.supplemental=269.63]] (match).
