# Module 12: Gross-to-Net Worked Examples

*Purpose: To provide a final, comprehensive validation of all researched rules.*

## 12.1 Comprehensive Gross-to-Net Examples

### Deliverable: Complete, end-to-end Gross-to-Net calculation examples for common scenarios

**Common parameters for every example below (Colombia, 2026).**

| Parameter | Value |
|---|---|
| Minimum monthly wage | **COP 1,750,905** |
| Transport allowance (employees up to 2 minimum wages = COP 3,501,810) | **COP 249,095** |
| Tax unit | **COP 52,374** |
| Contribution-base floor / ceiling | 1,750,905 / **43,772,625** (25 minimum wages) |
| Solidarity pension fund trigger | 4 minimum wages = **7,003,620** |
| Payroll-levy exemption cut-off | **less than** 10 minimum wages = 17,509,050 |
| Employee contributions | Health 4%, pension 4%, solidarity fund 1% / 0.2–1.0% |
| Employer contributions | Pension 12%, health 8.5%, occupational risk by class, family compensation fund 4%, apprenticeship levy 2%, family welfare levy 3% |
| Occupational risk (all examples) | **Class I, initial rate 0.522%** |
| Employer status | Legal person, income-tax filer — **exemption-eligible** |
| Withholding procedure | **Procedure 1** |
| Monthly cap on the 25% exempt income (790 units ÷ 12) | **COP 3,447,955** |
| Monthly combined cap (1,340 units ÷ 12) | **COP 5,848,430** |
| Rounding | Contribution base **up** to the peso; each contribution **up** to the next multiple of 100 |
| Statutory benefit accruals | Service bonus 8.3333%, severance savings 8.3333%, interest 1.0000%, vacation 4.1667% |

---

### Example 1 — Full-time resident employee on a standard salary (the minimum wage)

**Facts.** Indefinite-term contract, full 30-day month, salary at the statutory minimum, transport
allowance due, no overtime, no declared deductions.

**Step 1 — Gross earnings**

| Line | COP |
|---|---|
| Basic salary | 1,750,905.00 |
| Transport allowance | 249,095.00 |
| **Total gross earnings** | **2,000,000.00** |

**Step 2 — Contribution base**

| Line | Computation | COP |
|---|---|---|
| Salary-constituting payments | Transport allowance **excluded** — it is non-salary | 1,750,905 |
| 40% clamp | No non-salary payments beyond the allowance — not engaged | n/a |
| Floor | Equal to 1 minimum wage | ok |
| Ceiling | Far below 25 minimum wages | ok |
| **Contribution base** | Already a whole peso | **1,750,905** |

**Step 3 — Employee social security** (each rounded **up** to the next multiple of 100)

| Concept | Rate | Raw | Rounded |
|---|---|---|---|
| Health | 4.00% | 70,036.20 | **70,100** |
| Pension | 4.00% | 70,036.20 | **70,100** |
| Solidarity fund | Base 1,750,905 < 4 minimum wages (7,003,620) | — | **0** |
| **Total** | | | **140,200** |

**Step 4 — Withholding tax, Procedure 1**

| Line | Computation | COP |
|---|---|---|
| (A) Taxable payments | | 2,000,000.00 |
| (B) Non-taxable — pension and health contributions | | (140,200.00) |
| **(C) Subtotal** | | **1,859,800.00** |
| (D) Deductions | None | 0.00 |
| (E) 25% exempt income | 25% × 1,859,800 = 464,950; monthly cap 3,447,955 → within | (464,950.00) |
| (F) 40% cap | 40% × 1,859,800 = 743,920 → within | ok |
| **(G) Taxable base** | | **1,394,850.00** |
| (H) In tax units | 1,394,850 ÷ 52,374 | **26.6325** |
| (I) Band | ≤ 95 tax units → **0%** | |
| **Withholding** | | **0.00** |

**Step 5 — Net pay**

| Line | COP |
|---|---|
| Total gross earnings | 2,000,000.00 |
| Less health 4% | (70,100.00) |
| Less pension 4% | (70,100.00) |
| Less withholding tax | (0.00) |
| **NET PAY** | **1,859,800.00** |

**Step 6 — Employer cost**

| Concept | Rate | Base | COP |
|---|---|---|---|
| Pension | 12.0% | 1,750,905 | 210,108.60 → **210,200** |
| Health | 8.5% | 1,750,905 | **0** — exempt, salary < 10 minimum wages |
| Occupational risk, class I | 0.522% | 1,750,905 | 9,139.72 → **9,200** |
| Family compensation fund | 4.0% | 1,750,905 (payroll-levy base) | 70,036.20 → **70,100** |
| Apprenticeship training levy | 2.0% | 1,750,905 | **0** — exempt |
| Family welfare levy | 3.0% | 1,750,905 | **0** — exempt |
| **Contributions subtotal** | | | **289,500** |
| Service bonus accrual | 8.3333% | 2,000,000 (salary + allowance) | 166,666.67 |
| Severance-savings accrual | 8.3333% | 2,000,000 | 166,666.67 |
| Interest accrual | 1.0000% | 2,000,000 | 20,000.00 |
| Vacation accrual | 4.1667% | 1,750,905 (allowance **excluded**) | 72,954.38 |
| **Accruals subtotal** | **21.8333%** | | **426,287.72** |
| **TOTAL EMPLOYER COST** | | | **2,715,787.72** |
| **Employer cost factor** | | | **1.3579** |

---

### Example 2 — Part-time employee

**Facts.** Part-time employee working **20 hours per week** over the full month, salary **COP 900,000**,
indefinite-term contract. Salary is below 2 minimum wages, so the transport allowance is due in full.

**Minimum-wage compliance check.** The minimum wage applies proportionally: 1,750,905 × 20 ÷ 42 =
**COP 833,764.29**. The agreed COP 900,000 is above it. Compliant.

**Step 1 — Gross earnings**

| Line | COP |
|---|---|
| Basic salary | 900,000.00 |
| Transport allowance | 249,095.00 |
| **Total gross earnings** | **1,149,095.00** |

**Step 2 — Contribution base: the part-time floor effect**

| Line | Computation | COP |
|---|---|---|
| Salary-constituting payments | | 900,000 |
| **Floor test** | The employee worked a **full month**, so the floor is a **full** minimum wage — not prorated. 900,000 < 1,750,905 → **the floor applies** | |
| **Contribution base** | **Raised to 1 minimum wage** | **1,750,905** |

**Step 3 — Employee social security**

| Concept | Rate | Base | Rounded |
|---|---|---|---|
| Health | 4.00% | 1,750,905 | **70,100** |
| Pension | 4.00% | 1,750,905 | **70,100** |
| Solidarity fund | — | Below 4 minimum wages | **0** |
| **Total** | | | **140,200** |

The employee contributes **COP 140,200 on earnings of COP 900,000** — an effective 15.6% of salary rather
than 8%, because the base is floored. This is the defining part-time effect in Colombia.

**Step 4 — Withholding tax**

Taxable payments 1,149,095 less contributions 140,200 = 1,008,895; less the 25% exemption of 252,223.75 =
a base of **COP 756,671.25** = **14.4475 tax units** → **0% band** → **withholding COP 0.00**.

**Step 5 — Net pay**

| Line | COP |
|---|---|
| Total gross earnings | 1,149,095.00 |
| Less health 4% | (70,100.00) |
| Less pension 4% | (70,100.00) |
| **NET PAY** | **1,008,895.00** |

**Step 6 — Employer cost**

| Concept | Rate | Base | COP |
|---|---|---|---|
| Pension | 12.0% | **1,750,905** (floored contribution base) | **210,200** |
| Health | 8.5% | — | **0** — exempt |
| Occupational risk, class I | 0.522% | 1,750,905 | **9,200** |
| Family compensation fund | 4.0% | **900,000** — the payroll-levy base is the actual salary roll (Law 21 of 1982 art. 17), **not** the floored contribution base | **36,000** |
| Apprenticeship levy / family welfare levy | 2% / 3% | — | **0** — exempt |
| **Contributions subtotal** | | | **255,400** |
| Service bonus accrual | 8.3333% | 1,149,095 | 95,757.92 |
| Severance-savings accrual | 8.3333% | 1,149,095 | 95,757.92 |
| Interest accrual | 1.0000% | 1,149,095 | 11,490.95 |
| Vacation accrual | 4.1667% | 900,000 | 37,500.00 |
| **Accruals subtotal** | | | **240,506.79** |
| **TOTAL EMPLOYER COST** | | | **1,645,001.79** |
| **Employer cost factor** | | | **1.4316** |

**The lesson.** The part-time employer cost factor is **1.4316** against 1.3579 for the full-time
minimum-wage employee, purely because of the contribution-base floor. Note also the deliberate divergence
in Step 6: the **contribution base is floored at 1,750,905** while the **payroll-levy base is the actual
900,000**. Reusing one base for the other would misstate the family compensation fund contribution by
almost 100%.

---

### Example 3 — Employee with a pre-tax deduction (voluntary pension and long-term savings)

**Facts.** Salary **COP 12,000,000**, indefinite-term contract, full month. The employee contributes
**COP 1,500,000** per month to a voluntary pension fund and **COP 500,000** per month to a long-term
savings account. No dependants, no housing-loan interest, no prepaid health.

**Step 1 — Gross earnings.** COP 12,000,000. No transport allowance — salary exceeds 2 minimum wages.

**Step 2 — Contribution base.** COP 12,000,000. Above the floor, below the 25-minimum-wage ceiling.

**Step 3 — Employee social security**

| Concept | Rate | Base | COP |
|---|---|---|---|
| Health | 4.00% | 12,000,000 | 480,000 |
| Pension | 4.00% | 12,000,000 | 480,000 |
| Solidarity fund — solidarity account | 1.00% | 12,000,000 ≥ 4 minimum wages | 120,000 |
| Solidarity fund — subsistence account | — | 12,000,000 < 16 minimum wages (28,014,480) | 0 |
| **Total** | | | **1,080,000** |

**Step 4 — Withholding tax, Procedure 1**

| Line | Computation | COP |
|---|---|---|
| (A) Taxable payments | | 12,000,000.00 |
| (B) Non-taxable — pension 4% + solidarity 1% + health 4% | | (1,080,000.00) |
| **(C) Subtotal** | | **10,920,000.00** |
| (D) Art. 387 deductions | None declared | 0.00 |
| (E1) Exempt income — voluntary pension + long-term savings | 2,000,000. Cap: 30% of labour income = 3,600,000; annual 3,800 units ÷ 12 = COP 16,585,100 → **within both** | (2,000,000.00) |
| (E2) Exempt income — the 25% deduction, computed **LAST** | 25% × (10,920,000 − 2,000,000) = 25% × 8,920,000 = 2,230,000. Monthly 790-unit cap 3,447,955 → within | (2,230,000.00) |
| **(D + E)** | 0 + 2,000,000 + 2,230,000 | **4,230,000.00** |
| (F) 40% cap | 40% × 10,920,000 = 4,368,000 → 4,230,000 is **just within** | ok |
| — 1,340-unit monthly cap | 5,848,430 → within | ok |
| **(G) Taxable base** | 10,920,000 − 4,230,000 | **6,690,000.00** |
| (H) In tax units | 6,690,000 ÷ 52,374 | **127.7351** |
| (I) Band | > 95 and ≤ 150 → marginal **19%** | |
| (I) Withholding, in tax units | (127.7351 − 95) × 19% = **6.2197** | |
| **Withholding** | 6.2197 × 52,374 | **325,749.30** |

**The ordering effect made visible.** Had the 25% exemption been computed on the pre-deduction figure —
25% × 10,920,000 = 2,730,000 — the total deductions would have been 4,730,000, capped at 4,368,000, giving
a base of 6,552,000 = 125.1002 tax units and a withholding of COP 299,529.30. The **correct** ordering
produces **COP 325,749.30**. The difference of COP 26,220.00 per month is the cost of the ordering error,
and it compounds across a workforce.

**Step 5 — Net pay**

| Line | COP |
|---|---|
| Basic salary | 12,000,000.00 |
| Less health 4% | (480,000.00) |
| Less pension 4% | (480,000.00) |
| Less solidarity pension fund 1% | (120,000.00) |
| Less withholding tax | (325,749.30) |
| Less voluntary pension fund contribution | (1,500,000.00) |
| Less long-term savings contribution | (500,000.00) |
| **NET PAY** | **8,594,250.70** |

**Note on the class of relief.** The voluntary pension and long-term savings contributions are **exempt
income** (Tax Code arts. 126-1 and 126-4), deducted **inside** the 40% and 1,340-unit caps. Had the same
COP 2,000,000 been paid instead as a **voluntary contribution to the individual pension account** under
art. 55, it would have been **non-taxable income**, deducted **before** the cap reference figure was
struck — a structurally more valuable relief. The engine must carry the two vehicles as distinct wage
types.

---

### Example 4 — Employee with a student loan and a special statutory deduction

**Facts.** Salary **COP 3,500,000** — just below the 2-minimum-wage transport-allowance ceiling of
COP 3,501,810, so the allowance **is** due. The employee repays a national student loan through payroll
under a written payroll-lending authorisation at **COP 350,000** per month, and is subject to the **Higher
Education Solidarity Contribution** (*Contribución Solidaria a la Educación Superior — Contribución
Sabes*) notified at **COP 120,000** per month.

> **Scope note.** Colombia has **no statutory student-loan repayment tax** and no income-contingent
> repayment scheme deducted at source as a tax. The two Colombian analogues are (a) repayment of a national
> student loan through a **payroll-lending authorisation** under Law 1527 of 2012 — a voluntary,
> employee-authorised deduction, and (b) the **Higher Education Solidarity Contribution**, which **Labour
> Code art. 150, as substituted by Law 1911 of 2018 art. 22, expressly makes a permitted deduction
> requiring no individual written order**. Neither is a tax and neither reduces the withholding base.

**Step 1 — Gross earnings**

| Line | COP |
|---|---|
| Basic salary | 3,500,000.00 |
| Transport allowance (3,500,000 ≤ 3,501,810) | 249,095.00 |
| **Total gross earnings** | **3,749,095.00** |

**Step 2 — Contribution base.** COP 3,500,000 — the transport allowance is excluded.

**Step 3 — Employee social security**

| Concept | Rate | COP |
|---|---|---|
| Health | 4.00% | **140,000** |
| Pension | 4.00% | **140,000** |
| Solidarity fund | 3,500,000 < 7,003,620 | **0** |
| **Total** | | **280,000** |

**Step 4 — Withholding tax, Procedure 1**

| Line | Computation | COP |
|---|---|---|
| (A) Taxable payments | Salary + transport allowance — the allowance **is** income | 3,749,095.00 |
| (B) Non-taxable — pension + health | | (280,000.00) |
| **(C) Subtotal** | | **3,469,095.00** |
| (D) Deductions | The student-loan repayment and the solidarity contribution are **not** deductible against the withholding base | 0.00 |
| (E) 25% exempt income | 25% × 3,469,095 = 867,273.75; within the monthly cap | (867,273.75) |
| (F) 40% cap | 40% × 3,469,095 = 1,387,638 → within | ok |
| **(G) Taxable base** | | **2,601,821.25** |
| (H) In tax units | 2,601,821.25 ÷ 52,374 | **49.6777** |
| (I) Band | ≤ 95 tax units → **0%** | |
| **Withholding** | | **0.00** |

**Step 5 — Post-tax deductions and the protected-earnings check**

| Check | Computation | Result |
|---|---|---|
| Net before voluntary deductions | 3,749,095 − 280,000 | 3,469,095.00 |
| **Payroll-lending 50% rule** (Law 1527 of 2012) | Deductions of 350,000 + 120,000 = 470,000 must leave at least 50% of net = **1,734,547.50** | **Passes** — 2,999,095 remains |
| **Minimum-wage floor** (Labour Code art. 149 num. 2) | Net after deductions 2,999,095 vs the minimum wage 1,750,905 | **Passes** |
| Higher Education Solidarity Contribution | Permitted under art. 150 **without an individual written order** | Applied |
| Student-loan repayment | Requires a **written authorisation for the case** under arts. 149 and 151 | Applied |

**Step 6 — Net pay**

| Line | COP |
|---|---|
| Total gross earnings | 3,749,095.00 |
| Less health 4% | (140,000.00) |
| Less pension 4% | (140,000.00) |
| Less withholding tax | (0.00) |
| Less student-loan repayment (payroll lending) | (350,000.00) |
| Less Higher Education Solidarity Contribution | (120,000.00) |
| **NET PAY** | **2,999,095.00** |

**Step 7 — Employer cost**

| Concept | Rate | Base | COP |
|---|---|---|---|
| Pension | 12.0% | 3,500,000 | **420,000** |
| Health | 8.5% | — | **0** — exempt |
| Occupational risk, class I | 0.522% | 3,500,000 | 18,270 → **18,300** |
| Family compensation fund | 4.0% | 3,500,000 | **140,000** |
| Apprenticeship levy / family welfare levy | 2% / 3% | — | **0** — exempt |
| **Contributions subtotal** | | | **578,300** |
| Service bonus accrual | 8.3333% | 3,749,095 | 312,424.58 |
| Severance-savings accrual | 8.3333% | 3,749,095 | 312,424.58 |
| Interest accrual | 1.0000% | 3,749,095 | 37,490.95 |
| Vacation accrual | 4.1667% | 3,500,000 | 145,833.33 |
| **Accruals subtotal** | | | **808,173.44** |
| **TOTAL EMPLOYER COST** | | | **5,135,568.44** |
| **Employer cost factor** | | | **1.3698** |

**The lesson.** Neither the student-loan repayment nor the Higher Education Solidarity Contribution
touches the withholding base or the contribution base. Both are **post-tax deductions**, and both are
bounded by the minimum-wage floor and the payroll-lending 50% rule. Note also how close this salary sits
to the transport-allowance cliff: at COP 3,501,811 the allowance would be lost entirely, reducing gross by
COP 249,095 and the statutory-benefit base with it.

---

### Example 5 — Complex scenario: all-inclusive salary above the exemption threshold

**Facts.** Senior executive on an **all-inclusive salary** (*salario integral*) of **COP 25,000,000** per
month under a written agreement, indefinite-term contract, occupational risk class I. This is the most
structurally distinctive Colombian remuneration form, and it engages four separate rules at once.

**Step 0 — Validity check**

| Test | Requirement | Result |
|---|---|---|
| Written agreement | Labour Code art. 132 num. 2 | Present |
| Ordinary salary component above 10 minimum wages | 17,509,050 | Satisfied |
| Total not less than 13 minimum wages | **22,761,765** | 25,000,000 ≥ 22,761,765 — **valid** |

**Step 1 — Gross earnings.** COP 25,000,000. No transport allowance.

**Step 2 — Contribution base at 70%**

| Line | Computation | COP |
|---|---|---|
| All-inclusive salary | | 25,000,000 |
| **Contribution base = 70%** | Law 100 of 1993 art. 18 final paragraph; Decree 1072 of 2015 art. 2.2.4.3.3 for occupational risk | **17,500,000** |
| Ceiling check | 17,500,000 < 43,772,625 | ok |
| **Payroll-levy base = 70%** | Labour Code art. 132 num. 3: *"the contributions shall be reduced by thirty percent (30%)"* | **17,500,000** |

**Step 3 — Employee social security**

| Concept | Rate | Base | COP |
|---|---|---|---|
| Health | 4.00% | 17,500,000 | **700,000** |
| Pension | 4.00% | 17,500,000 | **700,000** |
| Solidarity fund — solidarity account | 1.00% | 17,500,000 ≥ 4 minimum wages | **175,000** |
| Solidarity fund — subsistence account | — | 17,500,000 < 16 minimum wages (28,014,480) | **0** |
| **Total** | | | **1,575,000** |

**Step 4 — The exemption test**

The employee **earns** COP 25,000,000, which is **at or above 10 minimum wages** (COP 17,509,050). The
Tax Code art. 114-1 exemption is therefore **LOST**. Note carefully that the test is applied to what the
employee *earns* — the full COP 25,000,000 — **not** to the 70% contribution base of COP 17,500,000, which
would (barely) have fallen below the threshold. Testing on the contribution base would wrongly exonerate
this employee and understate employer cost by roughly COP 2.36 million a month.

**Step 5 — Withholding tax, Procedure 1**

| Line | Computation | COP |
|---|---|---|
| (A) Taxable payments | The **whole** salary is taxable; the 70% rule is a social-security rule only | 25,000,000.00 |
| (B) Non-taxable — the contributions actually deducted | | (1,575,000.00) |
| **(C) Subtotal** | | **23,425,000.00** |
| (D) Deductions | None declared | 0.00 |
| (E) 25% exempt income | 25% × 23,425,000 = 5,856,250; monthly 790-unit cap **3,447,955** → **capped** | (3,447,955.00) |
| (F) 40% cap | 40% × 23,425,000 = 9,370,000 → within | ok |
| — 1,340-unit monthly cap | 5,848,430 → within | ok |
| **(G) Taxable base** | 23,425,000 − 3,447,955 | **19,977,045.00** |
| (H) In tax units | 19,977,045 ÷ 52,374 | **381.4306** |
| (I) Band | > 360 and ≤ 640 → marginal **33%** | |
| (I) Withholding, in tax units | (381.4306 − 360) × 33% + 69 = 7.0721 + 69 = **76.0721** | |
| **Withholding** | 76.0721 × 52,374 | **3,984,199.65** |

**Step 6 — Net pay**

| Line | COP |
|---|---|
| All-inclusive salary | 25,000,000.00 |
| Less health 4% | (700,000.00) |
| Less pension 4% | (700,000.00) |
| Less solidarity pension fund 1% | (175,000.00) |
| Less withholding tax | (3,984,199.65) |
| **NET PAY** | **19,440,800.35** |

**Step 7 — Employer cost**

| Concept | Rate | Base | COP |
|---|---|---|---|
| Pension | 12.0% | 17,500,000 | **2,100,000** |
| **Health** | 8.5% | 17,500,000 | **1,487,500** — exemption **lost** |
| Occupational risk, class I | 0.522% | 17,500,000 | 91,350 → **91,400** |
| Family compensation fund | 4.0% | 17,500,000 (70% levy base) | **700,000** |
| **Apprenticeship training levy** | 2.0% | 17,500,000 | **350,000** — exemption lost |
| **Family welfare levy** | 3.0% | 17,500,000 | **525,000** — exemption lost |
| **Contributions subtotal** | | | **5,253,900** |
| Service bonus accrual | — | **Absorbed** by the all-inclusive salary | 0 |
| Severance-savings accrual | — | **Absorbed** | 0 |
| Interest accrual | — | **Absorbed** | 0 |
| **Vacation accrual** | 4.1667% | **25,000,000 — the FULL salary**, because Labour Code art. 132 num. 2 expressly excepts vacation from what the all-inclusive salary absorbs | **1,041,666.67** |
| **TOTAL EMPLOYER COST** | | | **31,295,566.67** |
| **Employer cost factor** | | | **1.2518** |

**The four lessons this example carries.**

1. **The 70% rule applies to the contribution base and the payroll-levy base, not to tax.** The whole
   COP 25,000,000 is taxable.
2. **The exemption test is on what the employee earns, not on the contribution base.** Testing on the 70%
   figure would have wrongly exonerated the employee.
3. **Vacation is not absorbed** and is owed on the **full** COP 25,000,000, while contributions run on 70%.
   Three different bases in one employee: 25,000,000 for tax and vacation, 17,500,000 for contributions and
   levies.
4. **The employer cost factor is lower — 1.2518 against 1.3579 for a minimum-wage employee** — because the
   70% rule and the absorption of three of the four statutory benefits outweigh the loss of the exemption.
   This is why the all-inclusive salary is the standard senior-executive structure in Colombia.

---

### Summary comparison of the five examples

| # | Scenario | Gross | Employee deductions | Withholding | Net pay | Employer cost | Factor |
|---|---|---|---|---|---|---|---|
| 1 | Minimum wage, full time | 2,000,000 | 140,200 | 0 | **1,859,800** | 2,715,787.72 | **1.3579** |
| 2 | Part time, 20 h/week | 1,149,095 | 140,200 | 0 | **1,008,895** | 1,645,001.79 | **1.4316** |
| 3 | Pre-tax deduction (voluntary savings) | 12,000,000 | 1,080,000 | 325,749.30 | **8,594,250.70** | — | — |
| 4 | Student loan + solidarity contribution | 3,749,095 | 280,000 | 0 | **2,999,095** | 5,135,568.44 | **1.3698** |
| 5 | All-inclusive salary, exemption lost | 25,000,000 | 1,575,000 | 3,984,199.65 | **19,440,800.35** | 31,295,566.67 | **1.2518** |

*Note on example 3: net pay is after the employee's own COP 2,000,000 of voluntary savings contributions,
which are a transfer to the employee's own accounts, not a cost. Employer cost is not shown because the
example is constructed to isolate the depuration ordering rule.*

**The Colombian employer cost factor is not monotonic in salary.** It **rises** at the low end because the
contribution-base floor bites on part-time and low-paid work; it **falls** at the top end because of the
all-inclusive salary's 70% rule; and it **spikes** at exactly 10 minimum wages where the exemption is lost.
The cliff is quantified in Module 5 and demonstrated by the bonus example in Module 9.2.

*Legal basis: Substantive Labour Code arts. 127, 128, 129, 132, 149, 150, 151, 192, 230, 249, 306 (art. 150
as substituted by Law 1911 of 2018 art. 22); Law 100 of 1993 arts. 18, 20, 204; Law 21 of 1982 art. 17;
Law 89 of 1988 art. 1; Law 1393 of 2010 art. 30; Law 1527 of 2012; Tax Code (Decree-Law 624 of 1989)
arts. 55, 56, 114-1, 126-1, 126-4, 206 num. 10, 336 num. 3, 383, 385, 387, 388; Decree 1072 of 2015
arts. 2.2.4.3.3 and 2.2.4.3.5; Decree 1772 of 1994 art. 13; Decree 780 of 2016 art. 3.2.1.5 (substituted by
Decree 1990 of 2016 art. 1); Decree 1469 of 2025; Decree 1470 of 2025; Resolution DIAN 000238 of 2025.*
