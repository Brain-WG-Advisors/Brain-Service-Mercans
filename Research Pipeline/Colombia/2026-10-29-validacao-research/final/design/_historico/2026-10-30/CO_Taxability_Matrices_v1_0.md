# CO — Taxability Matrices (companion to `CO_Regulation_Design_v1_0.md`)

Mechanically derived from **CO-WTC-001 v1.7**, sheet *Wage Type Catalogue*, columns N–X (405 wage-type rows; raw extraction: `CO_Taxability_Perimeters_Extract_v1_0.csv`). Nothing here is hand-transcribed. Convention, as for the dev team's matrices: **specific overrides first** (`No` and `Yes-No` rows), then the default; rows that are `NA` in a perimeter are not in that matrix.

**Row identifiers.** WTC v1.7 carries no Mercans codes in column A (codes are assigned at configuration). Every row is therefore identified here by its **WTC row number** (`R123`) and English name; the CSV carries the same key. When codes are assigned, the matrices are re-keyed one to one; no wildcard (`621%%`-style) condensation is possible until then.

**Perimeters (WTC column → matrix → consuming regulation):**

| WTC column | Matrix | Feeds | Consumed by |
|---|---|---|---|
| N | A — Subject to withholding | `58150` taxable labour payments | `9170051`, `9170061`–`9170065` |
| O | B — Art. 383 table | routing: `Yes` = ordinary monthly table read; `No` = withheld by another method | `9170061`, `9170064`, `9170065` |
| P | C — Non-resident flat 20% | `58163` base | `9170063` |
| Q | D — Health | `58101`/`58102` → `58106` IBC (health) | `9170016`–`9170021`, `9170031`, `9170041` |
| R | E — Solidarity pension fund | `58113` IBC (FSP) | `9170033`, `9170034` |
| S | F — Occupational risk | `58114` IBC (ARL) | `9170043` |
| T | G — Payroll levies (CCF / SENA / ICBF) | `58108` levy base | `9170023`, `9170044`–`9170046` |
| U | H — Pension | `58112` IBC (pension) | `9170032`, `9170042` |
| W | I — Statutory-benefit base (prima / cesantías / interest) | `58171` | `9170081`–`9170084` |
| X | J — Vacation base | `58175` | `9170085`, `9170086` |
| V | K — Salary class (CST arts. 127 / 128) | `58101` (Salary), `58102` (Non-Salary – pacted) | `9170016`, `9170017` |

---

## 🔴 Structural finding — the engine matrix cannot express `Yes-No`

The WTC marks rows **`Yes/No`** (subject only in part or only under a condition). A taxability matrix holds `Yes` or `No` per row; there is no third state. Count per perimeter: N 22, O 13, P 2, Q 57, R 58, S 55, T 4, U 57, W 3, X 3.

**Social-security perimeters (Q, R, S, U): two families, two different treatments.**

1. **Pacted non-salary (53 rows, column V = `Non-Salary - pacted`).** The payment is outside the contribution base only up to 40% of total remuneration (Law 1393 of 2010 art. 30; Consejo de Estado SU exp. 25185 of 9 December 2021, rule 3). Built: these rows are **`No`** in matrices D, E, F and H and **`Yes`** in matrix K-pacted (`58102`); regulation `9170019` computes the excess over 40% (`58104`), which is added to every IBC (health, pension, FSP, occupational risk) and **never** to the levy base (Law 21 of 1982 art. 17; Decree-Law 1295 of 1994 art. 17 for occupational risk).
2. **Conditional rows (5 rows, other classes: R6 Unpaid LOA - Basic salary deduction, R37 Long Term Disability deduction, R227 Per diem allowance, R338 Apprentice maintenance support, R358 Payroll advance (accrued)).** The condition is a statutory test on the payment itself, stated in the WTC explanation (e.g. the per diem allowance, the apprentice support by phase, the payroll advance). These must be **split into two wage types at configuration** — the exempt portion (`No`) and the subject portion (`Yes`) — with the split decided upstream of the regulation. They are set to `No` in the matrices below and listed with ⚠split.

**Withholding perimeter (N): 22 rows `Yes/No`.** Severance savings and interest (exempt in full when the average monthly labour income of the last six months is ≤ 350 UVT, tapered above, Tax Code art. 206 num. 4), pensions, gratuities and end-of-service payments, third-party meals (≤ 41 UVT when salary ≤ 310 UVT, art. 387-1), employer voluntary pension contributions (Tax Code art. 55: up to 25% of income and 2,500 UVT a year), occasional per diem (Decree 1625 of 2016 art. 1.2.4.7) and the payroll advance. Same split rule: `No` in matrix A and listed ⚠split; the subject portion is configured as its own wage type.

---

## Rows excluded from all ten matrices (`NA` in every perimeter)

107 rows are `NA` in every column N–X: deductions and recoveries, employer-contribution and accrual lines, bases, flags, percentages and the withholding lines themselves. They are produced by regulations, not summed by matrices:

```
R2, R3, R4, R5, R7, R8, R9, R10, R11, R12, R13, R14
R15, R16, R17, R18, R19, R20, R21, R22, R23, R24, R25, R26
R27, R28, R29, R30, R31, R32, R33, R34, R35, R36, R38, R39
R40, R41, R42, R43, R44, R45, R46, R47, R48, R49, R50, R51
R52, R53, R54, R55, R56, R57, R58, R59, R60, R65, R336, R337
R360, R361, R362, R363, R364, R365, R366, R367, R368, R369, R370, R371
R372, R373, R374, R375, R376, R377, R378, R379, R380, R381, R382, R383
R384, R385, R386, R387, R388, R389, R390, R391, R392, R393, R394, R395
R396, R397, R398, R399, R400, R401, R402, R403, R404, R405, R406
```

## Matrix A — Subject to withholding (WTC column N)

**Consumed by:** `9170051`, `9170061`–`9170065` · **Feeds:** `58150` taxable labour payments

Counts: `Yes` 263 · `No` 13 · `Yes/No` 22 (→ `No`: pacted rows via the Law 1393 excess, others ⚠split) · `NA` 107 (not in the matrix).

**Section 1 — overrides (35 rows):**

| WTC row | Value | Wage type | Salary class |
|---|---|---|---|
| R120 | No ⚠split | Severance & Seniority | Non-Salary - non-remunerative |
| R121 | No ⚠split | Severance & Seniority | Non-Salary - non-remunerative |
| R122 | No ⚠split | Severance & Seniority | Non-Salary - non-remunerative |
| R218 | No | Arrears - Relocation allowance | Non-Salary - non-remunerative |
| R219 | No | Adjustment - Relocation allowance | Non-Salary - non-remunerative |
| R220 | No | Travel ticket allowance | Non-Salary - non-remunerative |
| R221 | No | Arrears - Travel ticket allowance | Non-Salary - non-remunerative |
| R222 | No | Adjustment - Travel ticket allowance | Non-Salary - non-remunerative |
| R223 | No | Relocation allowance | Non-Salary - non-remunerative |
| R224 | No | Arrears - Relocation allowance | Non-Salary - non-remunerative |
| R225 | No | Adjustment - Relocation allowance | Non-Salary - non-remunerative |
| R241 | No ⚠split | Pensions & Pension Refunds | Non-Salary - non-remunerative |
| R242 | No ⚠split | Pensions & Pension Refunds | Non-Salary - non-remunerative |
| R243 | No ⚠split | Pensions & Pension Refunds | Non-Salary - non-remunerative |
| R244 | No ⚠split | Pensions & Pension Refunds | Non-Salary - non-remunerative |
| R245 | No ⚠split | Pensions & Pension Refunds | Non-Salary - non-remunerative |
| R246 | No ⚠split | Pensions & Pension Refunds | Non-Salary - non-remunerative |
| R247 | No ⚠split | Pensions & Pension Refunds | Non-Salary - non-remunerative |
| R248 | No ⚠split | Pensions & Pension Refunds | Non-Salary - non-remunerative |
| R265 | No | Family allowance (MLA, Children) | Non-Salary - non-remunerative |
| R266 | No | Adjustment - Family allowance (MLA, Children) | Non-Salary - non-remunerative |
| R282 | No ⚠split | Statutory Gratuity, EOS | Non-Salary - non-remunerative |
| R284 | No ⚠split | Gratuity, EOS, Post-termination, etc. | Non-Salary - non-remunerative |
| R285 | No ⚠split | Gratuity, EOS, Post-termination, etc. | Non-Salary - non-remunerative |
| R286 | No ⚠split | Gratuity, EOS, Post-termination, etc. | Non-Salary - non-remunerative |
| R321 | No ⚠split | Severance savings | Non-Salary - non-remunerative |
| R322 | No ⚠split | Interest on severance savings | Non-Salary - non-remunerative |
| R325 | No | Work clothing and footwear | Non-Salary - non-remunerative |
| R346 | No ⚠split | Third-party meal payments | Non-Salary - non-remunerative |
| R349 | No ⚠split | Employer contribution to a voluntary pension fund | Non-Salary - pacted |
| R350 | No ⚠split | Employer voluntary contribution to the individual pension account | Non-Salary - pacted |
| R353 | No ⚠split | Occasional per diem, and the transport / representation portion | Non-Salary - non-remunerative |
| R355 | No | Tips | Non-Salary - non-remunerative |
| R358 | No ⚠split | Payroll advance (accrued) | Conditional |
| R359 | No | Reimbursement to the employee (accrued) | Non-Salary - non-remunerative |

**Section 2 — default `Yes` (263 rows):** every row not `NA` and not listed in Section 1. Row list (for configuration check):

```
R6, R37, R61, R62, R63, R64, R66, R67, R68, R69, R70, R71, R72, R73, R74
R75, R76, R77, R78, R79, R80, R81, R82, R83, R84, R85, R86, R87, R88, R89
R90, R91, R92, R93, R94, R95, R96, R97, R98, R99, R100, R101, R102, R103, R104
R105, R106, R107, R108, R109, R110, R111, R112, R113, R114, R115, R116, R117, R118, R119
R123, R124, R125, R126, R127, R128, R129, R130, R131, R132, R133, R134, R135, R136, R137
R138, R139, R140, R141, R142, R143, R144, R145, R146, R147, R148, R149, R150, R151, R152
R153, R154, R155, R156, R157, R158, R159, R160, R161, R162, R163, R164, R165, R166, R167
R168, R169, R170, R171, R172, R173, R174, R175, R176, R177, R178, R179, R180, R181, R182
R183, R184, R185, R186, R187, R188, R189, R190, R191, R192, R193, R194, R195, R196, R197
R198, R199, R200, R201, R202, R203, R204, R205, R206, R207, R208, R209, R210, R211, R212
R213, R214, R215, R216, R217, R226, R227, R228, R229, R230, R231, R232, R233, R234, R235
R236, R237, R238, R239, R240, R249, R250, R251, R252, R253, R254, R255, R256, R257, R258
R259, R260, R261, R262, R263, R264, R267, R268, R269, R270, R271, R272, R273, R274, R275
R276, R277, R278, R279, R280, R281, R283, R287, R288, R289, R290, R291, R292, R293, R294
R295, R296, R297, R298, R299, R300, R301, R302, R303, R304, R305, R306, R307, R308, R309
R310, R311, R312, R313, R314, R315, R316, R317, R318, R319, R320, R323, R324, R326, R327
R328, R329, R330, R331, R332, R333, R334, R335, R338, R339, R340, R341, R342, R343, R344
R345, R347, R348, R351, R352, R354, R356, R357
```

## Matrix B — Art. 383 table (WTC column O)

**Consumed by:** `9170061`, `9170064`, `9170065` · **Feeds:** routing: `Yes` = ordinary monthly table read; `No` = withheld by another method

Counts: `Yes` 263 · `No` 22 · `Yes/No` 13 (→ `No`: pacted rows via the Law 1393 excess, others ⚠split) · `NA` 107 (not in the matrix).

**Section 1 — overrides (35 rows):**

| WTC row | Value | Wage type | Salary class |
|---|---|---|---|
| R120 | No | Severance & Seniority | Non-Salary - non-remunerative |
| R121 | No | Severance & Seniority | Non-Salary - non-remunerative |
| R122 | No | Severance & Seniority | Non-Salary - non-remunerative |
| R218 | No | Arrears - Relocation allowance | Non-Salary - non-remunerative |
| R219 | No | Adjustment - Relocation allowance | Non-Salary - non-remunerative |
| R220 | No | Travel ticket allowance | Non-Salary - non-remunerative |
| R221 | No | Arrears - Travel ticket allowance | Non-Salary - non-remunerative |
| R222 | No | Adjustment - Travel ticket allowance | Non-Salary - non-remunerative |
| R223 | No | Relocation allowance | Non-Salary - non-remunerative |
| R224 | No | Arrears - Relocation allowance | Non-Salary - non-remunerative |
| R225 | No | Adjustment - Relocation allowance | Non-Salary - non-remunerative |
| R241 | No ⚠split | Pensions & Pension Refunds | Non-Salary - non-remunerative |
| R242 | No ⚠split | Pensions & Pension Refunds | Non-Salary - non-remunerative |
| R243 | No ⚠split | Pensions & Pension Refunds | Non-Salary - non-remunerative |
| R244 | No ⚠split | Pensions & Pension Refunds | Non-Salary - non-remunerative |
| R245 | No ⚠split | Pensions & Pension Refunds | Non-Salary - non-remunerative |
| R246 | No ⚠split | Pensions & Pension Refunds | Non-Salary - non-remunerative |
| R247 | No ⚠split | Pensions & Pension Refunds | Non-Salary - non-remunerative |
| R248 | No ⚠split | Pensions & Pension Refunds | Non-Salary - non-remunerative |
| R265 | No | Family allowance (MLA, Children) | Non-Salary - non-remunerative |
| R266 | No | Adjustment - Family allowance (MLA, Children) | Non-Salary - non-remunerative |
| R282 | No | Statutory Gratuity, EOS | Non-Salary - non-remunerative |
| R284 | No | Gratuity, EOS, Post-termination, etc. | Non-Salary - non-remunerative |
| R285 | No | Gratuity, EOS, Post-termination, etc. | Non-Salary - non-remunerative |
| R286 | No | Gratuity, EOS, Post-termination, etc. | Non-Salary - non-remunerative |
| R321 | No | Severance savings | Non-Salary - non-remunerative |
| R322 | No | Interest on severance savings | Non-Salary - non-remunerative |
| R325 | No | Work clothing and footwear | Non-Salary - non-remunerative |
| R346 | No ⚠split | Third-party meal payments | Non-Salary - non-remunerative |
| R349 | No ⚠split | Employer contribution to a voluntary pension fund | Non-Salary - pacted |
| R350 | No ⚠split | Employer voluntary contribution to the individual pension account | Non-Salary - pacted |
| R353 | No ⚠split | Occasional per diem, and the transport / representation portion | Non-Salary - non-remunerative |
| R355 | No | Tips | Non-Salary - non-remunerative |
| R358 | No ⚠split | Payroll advance (accrued) | Conditional |
| R359 | No | Reimbursement to the employee (accrued) | Non-Salary - non-remunerative |

**Section 2 — default `Yes` (263 rows):** every row not `NA` and not listed in Section 1. Row list (for configuration check):

```
R6, R37, R61, R62, R63, R64, R66, R67, R68, R69, R70, R71, R72, R73, R74
R75, R76, R77, R78, R79, R80, R81, R82, R83, R84, R85, R86, R87, R88, R89
R90, R91, R92, R93, R94, R95, R96, R97, R98, R99, R100, R101, R102, R103, R104
R105, R106, R107, R108, R109, R110, R111, R112, R113, R114, R115, R116, R117, R118, R119
R123, R124, R125, R126, R127, R128, R129, R130, R131, R132, R133, R134, R135, R136, R137
R138, R139, R140, R141, R142, R143, R144, R145, R146, R147, R148, R149, R150, R151, R152
R153, R154, R155, R156, R157, R158, R159, R160, R161, R162, R163, R164, R165, R166, R167
R168, R169, R170, R171, R172, R173, R174, R175, R176, R177, R178, R179, R180, R181, R182
R183, R184, R185, R186, R187, R188, R189, R190, R191, R192, R193, R194, R195, R196, R197
R198, R199, R200, R201, R202, R203, R204, R205, R206, R207, R208, R209, R210, R211, R212
R213, R214, R215, R216, R217, R226, R227, R228, R229, R230, R231, R232, R233, R234, R235
R236, R237, R238, R239, R240, R249, R250, R251, R252, R253, R254, R255, R256, R257, R258
R259, R260, R261, R262, R263, R264, R267, R268, R269, R270, R271, R272, R273, R274, R275
R276, R277, R278, R279, R280, R281, R283, R287, R288, R289, R290, R291, R292, R293, R294
R295, R296, R297, R298, R299, R300, R301, R302, R303, R304, R305, R306, R307, R308, R309
R310, R311, R312, R313, R314, R315, R316, R317, R318, R319, R320, R323, R324, R326, R327
R328, R329, R330, R331, R332, R333, R334, R335, R338, R339, R340, R341, R342, R343, R344
R345, R347, R348, R351, R352, R354, R356, R357
```

## Matrix C — Non-resident flat 20% (WTC column P)

**Consumed by:** `9170063` · **Feeds:** `58163` base

Counts: `Yes` 280 · `No` 16 · `Yes/No` 2 (→ `No`: pacted rows via the Law 1393 excess, others ⚠split) · `NA` 107 (not in the matrix).

**Section 1 — overrides (18 rows):**

| WTC row | Value | Wage type | Salary class |
|---|---|---|---|
| R218 | No | Arrears - Relocation allowance | Non-Salary - non-remunerative |
| R219 | No | Adjustment - Relocation allowance | Non-Salary - non-remunerative |
| R220 | No | Travel ticket allowance | Non-Salary - non-remunerative |
| R221 | No | Arrears - Travel ticket allowance | Non-Salary - non-remunerative |
| R222 | No | Adjustment - Travel ticket allowance | Non-Salary - non-remunerative |
| R223 | No | Relocation allowance | Non-Salary - non-remunerative |
| R224 | No | Arrears - Relocation allowance | Non-Salary - non-remunerative |
| R225 | No | Adjustment - Relocation allowance | Non-Salary - non-remunerative |
| R265 | No | Family allowance (MLA, Children) | Non-Salary - non-remunerative |
| R266 | No | Adjustment - Family allowance (MLA, Children) | Non-Salary - non-remunerative |
| R325 | No | Work clothing and footwear | Non-Salary - non-remunerative |
| R346 | No ⚠split | Third-party meal payments | Non-Salary - non-remunerative |
| R349 | No | Employer contribution to a voluntary pension fund | Non-Salary - pacted |
| R350 | No | Employer voluntary contribution to the individual pension account | Non-Salary - pacted |
| R353 | No | Occasional per diem, and the transport / representation portion | Non-Salary - non-remunerative |
| R355 | No | Tips | Non-Salary - non-remunerative |
| R358 | No ⚠split | Payroll advance (accrued) | Conditional |
| R359 | No | Reimbursement to the employee (accrued) | Non-Salary - non-remunerative |

**Section 2 — default `Yes` (280 rows):** every row not `NA` and not listed in Section 1. Row list (for configuration check):

```
R6, R37, R61, R62, R63, R64, R66, R67, R68, R69, R70, R71, R72, R73, R74
R75, R76, R77, R78, R79, R80, R81, R82, R83, R84, R85, R86, R87, R88, R89
R90, R91, R92, R93, R94, R95, R96, R97, R98, R99, R100, R101, R102, R103, R104
R105, R106, R107, R108, R109, R110, R111, R112, R113, R114, R115, R116, R117, R118, R119
R120, R121, R122, R123, R124, R125, R126, R127, R128, R129, R130, R131, R132, R133, R134
R135, R136, R137, R138, R139, R140, R141, R142, R143, R144, R145, R146, R147, R148, R149
R150, R151, R152, R153, R154, R155, R156, R157, R158, R159, R160, R161, R162, R163, R164
R165, R166, R167, R168, R169, R170, R171, R172, R173, R174, R175, R176, R177, R178, R179
R180, R181, R182, R183, R184, R185, R186, R187, R188, R189, R190, R191, R192, R193, R194
R195, R196, R197, R198, R199, R200, R201, R202, R203, R204, R205, R206, R207, R208, R209
R210, R211, R212, R213, R214, R215, R216, R217, R226, R227, R228, R229, R230, R231, R232
R233, R234, R235, R236, R237, R238, R239, R240, R241, R242, R243, R244, R245, R246, R247
R248, R249, R250, R251, R252, R253, R254, R255, R256, R257, R258, R259, R260, R261, R262
R263, R264, R267, R268, R269, R270, R271, R272, R273, R274, R275, R276, R277, R278, R279
R280, R281, R282, R283, R284, R285, R286, R287, R288, R289, R290, R291, R292, R293, R294
R295, R296, R297, R298, R299, R300, R301, R302, R303, R304, R305, R306, R307, R308, R309
R310, R311, R312, R313, R314, R315, R316, R317, R318, R319, R320, R321, R322, R323, R324
R326, R327, R328, R329, R330, R331, R332, R333, R334, R335, R338, R339, R340, R341, R342
R343, R344, R345, R347, R348, R351, R352, R354, R356, R357
```

## Matrix D — Health (WTC column Q)

**Consumed by:** `9170016`–`9170021`, `9170031`, `9170041` · **Feeds:** `58101`/`58102` → `58106` IBC (health)

Counts: `Yes` 168 · `No` 65 · `Yes/No` 57 (→ `No`: pacted rows via the Law 1393 excess, others ⚠split) · `NA` 115 (not in the matrix).

**Section 1 — overrides (122 rows):**

| WTC row | Value | Wage type | Salary class |
|---|---|---|---|
| R6 | No ⚠split | Unpaid LOA - Basic salary deduction | Salary |
| R37 | No ⚠split | Long Term Disability deduction | Salary |
| R120 | No | Severance & Seniority | Non-Salary - non-remunerative |
| R121 | No | Severance & Seniority | Non-Salary - non-remunerative |
| R122 | No | Severance & Seniority | Non-Salary - non-remunerative |
| R134 | No (via Law 1393 excess `58104`) | Bonus - profit sharing | Non-Salary - pacted |
| R135 | No (via Law 1393 excess `58104`) | Bonus - profit sharing | Non-Salary - pacted |
| R136 | No (via Law 1393 excess `58104`) | Bonus - profit sharing | Non-Salary - pacted |
| R137 | No (via Law 1393 excess `58104`) | Bonus - profit sharing | Non-Salary - pacted |
| R138 | No (via Law 1393 excess `58104`) | Bonus - profit sharing | Non-Salary - pacted |
| R139 | No (via Law 1393 excess `58104`) | Bonus - profit sharing | Non-Salary - pacted |
| R140 | No (via Law 1393 excess `58104`) | Bonus - profit sharing | Non-Salary - pacted |
| R141 | No (via Law 1393 excess `58104`) | Bonus - profit sharing | Non-Salary - pacted |
| R142 | No (via Law 1393 excess `58104`) | Bonus - profit sharing | Non-Salary - pacted |
| R143 | No (via Law 1393 excess `58104`) | Bonus - profit sharing | Non-Salary - pacted |
| R144 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R145 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R146 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R147 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R148 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R149 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R150 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R151 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R152 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R153 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R156 | No | Annual leave payout | Paid Rest |
| R201 | No (via Law 1393 excess `58104`) | Car allowance | Non-Salary - pacted |
| R202 | No (via Law 1393 excess `58104`) | Arrears - Car allowance | Non-Salary - pacted |
| R203 | No (via Law 1393 excess `58104`) | Adjustment - Car allowance | Non-Salary - pacted |
| R204 | No (via Law 1393 excess `58104`) | Advance - Car allowance | Non-Salary - pacted |
| R205 | No (via Law 1393 excess `58104`) | Car maintenance | Non-Salary - pacted |
| R206 | No (via Law 1393 excess `58104`) | Car fuel | Non-Salary - pacted |
| R207 | No | Car & Transportation allowance | Non-Salary - non-remunerative |
| R208 | No | Arrears - Car & Transportation allowance | Non-Salary - non-remunerative |
| R209 | No | Adjustment - Car & Transportation allowance | Non-Salary - non-remunerative |
| R210 | No | Transportation allowance | Non-Salary - non-remunerative |
| R211 | No | Arrears - Transportation allowance | Non-Salary - non-remunerative |
| R212 | No | Adjustment - Transportation allowance | Non-Salary - non-remunerative |
| R213 | No | Advance - Transportation allowance | Non-Salary - non-remunerative |
| R214 | No (via Law 1393 excess `58104`) | Car Maintenance Allowance 2 | Non-Salary - pacted |
| R215 | No (via Law 1393 excess `58104`) | Arrears - Car Maintenance Allowance 2 | Non-Salary - pacted |
| R216 | No (via Law 1393 excess `58104`) | Adjustment - Car Maintenance Allowance 2 | Non-Salary - pacted |
| R217 | No | Relocation allowance | Non-Salary - non-remunerative |
| R218 | No | Arrears - Relocation allowance | Non-Salary - non-remunerative |
| R219 | No | Adjustment - Relocation allowance | Non-Salary - non-remunerative |
| R220 | No | Travel ticket allowance | Non-Salary - non-remunerative |
| R221 | No | Arrears - Travel ticket allowance | Non-Salary - non-remunerative |
| R222 | No | Adjustment - Travel ticket allowance | Non-Salary - non-remunerative |
| R223 | No | Relocation allowance | Non-Salary - non-remunerative |
| R224 | No | Arrears - Relocation allowance | Non-Salary - non-remunerative |
| R225 | No | Adjustment - Relocation allowance | Non-Salary - non-remunerative |
| R226 | No | Advance - Relocation allowance | Non-Salary - non-remunerative |
| R227 | No ⚠split | Per diem allowance | Conditional |
| R228 | No | Birth and Marriage Allowance | Non-Salary - non-remunerative |
| R229 | No | Birth and Marriage Allowance | Non-Salary - non-remunerative |
| R230 | No (via Law 1393 excess `58104`) | COVID-19 Allowance | Non-Salary - pacted |
| R231 | No (via Law 1393 excess `58104`) | Medical insurance / Medical Care | Non-Salary - pacted |
| R232 | No (via Law 1393 excess `58104`) | Arrears - Medical insurance / Medical Care | Non-Salary - pacted |
| R233 | No (via Law 1393 excess `58104`) | Adjustment - Medical insurance / Medical Care | Non-Salary - pacted |
| R234 | No (via Law 1393 excess `58104`) | Medical insurance / Medical Care | Non-Salary - pacted |
| R235 | No (via Law 1393 excess `58104`) | Medical insurance / Medical Care | Non-Salary - pacted |
| R236 | No (via Law 1393 excess `58104`) | Medical insurance / Medical Care | Non-Salary - pacted |
| R237 | No (via Law 1393 excess `58104`) | Medical insurance / Medical Care | Non-Salary - pacted |
| R253 | No (via Law 1393 excess `58104`) | Benefits plan 1 | Non-Salary - pacted |
| R254 | No (via Law 1393 excess `58104`) | Benefits plan 2 | Non-Salary - pacted |
| R255 | No (via Law 1393 excess `58104`) | Education allowance | Non-Salary - pacted |
| R256 | No (via Law 1393 excess `58104`) | Schooling allowance | Non-Salary - pacted |
| R257 | No (via Law 1393 excess `58104`) | Arrears - Schooling allowance | Non-Salary - pacted |
| R258 | No (via Law 1393 excess `58104`) | Education & Schooling allowance 2 | Non-Salary - pacted |
| R259 | No (via Law 1393 excess `58104`) | Arrears - Education & Schooling allowance 2 | Non-Salary - pacted |
| R260 | No (via Law 1393 excess `58104`) | Education & Schooling allowance 3 | Non-Salary - pacted |
| R261 | No (via Law 1393 excess `58104`) | Education & Schooling allowance 4 | Non-Salary - pacted |
| R262 | No (via Law 1393 excess `58104`) | Arrears - Education & Schooling allowance 4 | Non-Salary - pacted |
| R263 | No (via Law 1393 excess `58104`) | Education & Schooling allowance 5 | Non-Salary - pacted |
| R264 | No (via Law 1393 excess `58104`) | Arrears - Education & Schooling allowance 5 | Non-Salary - pacted |
| R265 | No | Family allowance (MLA, Children) | Non-Salary - non-remunerative |
| R266 | No | Adjustment - Family allowance (MLA, Children) | Non-Salary - non-remunerative |
| R267 | No (via Law 1393 excess `58104`) | Recognition Award | Non-Salary - pacted |
| R277 | No | Post-termination payment | Non-Salary - non-remunerative |
| R278 | No | Post-termination payment | Non-Salary - non-remunerative |
| R279 | No | Post-termination payment | Non-Salary - non-remunerative |
| R280 | No | Post-termination payment | Non-Salary - non-remunerative |
| R281 | No (via Law 1393 excess `58104`) | Stock options and grants | Non-Salary - pacted |
| R282 | No | Statutory Gratuity, EOS | Non-Salary - non-remunerative |
| R283 | No | Supplemental basic (i.e. 13th or 14th months salary) | Non-Salary - non-remunerative |
| R284 | No | Gratuity, EOS, Post-termination, etc. | Non-Salary - non-remunerative |
| R285 | No | Gratuity, EOS, Post-termination, etc. | Non-Salary - non-remunerative |
| R286 | No | Gratuity, EOS, Post-termination, etc. | Non-Salary - non-remunerative |
| R298 | No (via Law 1393 excess `58104`) | Stock options and grants | Non-Salary - pacted |
| R299 | No (via Law 1393 excess `58104`) | Stock options and grants | Non-Salary - pacted |
| R300 | No (via Law 1393 excess `58104`) | Stock options and grants | Non-Salary - pacted |
| R301 | No (via Law 1393 excess `58104`) | Stock options and grants | Non-Salary - pacted |
| R304 | No | Statutory transport allowance | Non-Salary - non-remunerative |
| R305 | No | Connectivity allowance (teleworkers) | Non-Salary - non-remunerative |
| R316 | No (via Law 1393 excess `58104`) | Extra-statutory bonus under a written non-salary pact | Non-Salary - pacted |
| R317 | No (via Law 1393 excess `58104`) | Extra-statutory vacation bonus | Non-Salary - pacted |
| R318 | No | Occasional gratuity (mera liberalidad) | Non-Salary - non-remunerative |
| R320 | No | Statutory service bonus | Non-Salary - non-remunerative |
| R321 | No | Severance savings | Non-Salary - non-remunerative |
| R322 | No | Interest on severance savings | Non-Salary - non-remunerative |
| R324 | No | Vacation compensated in cash | Paid Rest |
| R325 | No | Work clothing and footwear | Non-Salary - non-remunerative |
| R339 | No | Indemnity for dismissal without just cause | Non-Salary - non-remunerative |
| R340 | No | Late-payment penalty | Non-Salary - non-remunerative |
| R341 | No | Penalty for non-deposit of severance savings | Non-Salary - non-remunerative |
| R342 | No | Penalty for unpaid severance interest | Non-Salary - non-remunerative |
| R343 | No | Indemnity for early termination of a fixed-term or work-or-task contract | Non-Salary - non-remunerative |
| R344 | No | Indemnity for dismissal during protected status | Non-Salary - non-remunerative |
| R345 | No | Retirement or mutual-termination settlement bonus | Non-Salary - non-remunerative |
| R346 | No | Third-party meal payments | Non-Salary - non-remunerative |
| R347 | No (via Law 1393 excess `58104`) | Voucher, card or non-cash instrument payment | Non-Salary - pacted |
| R348 | No (via Law 1393 excess `58104`) | Employer-paid prepaid health / supplementary health plan | Non-Salary - pacted |
| R349 | No (via Law 1393 excess `58104`) | Employer contribution to a voluntary pension fund | Non-Salary - pacted |
| R350 | No (via Law 1393 excess `58104`) | Employer voluntary contribution to the individual pension account | Non-Salary - pacted |
| R351 | No (via Law 1393 excess `58104`) | Equity and share-incentive awards | Non-Salary - pacted |
| R353 | No | Occasional per diem, and the transport / representation portion | Non-Salary - non-remunerative |
| R354 | No | Telework allowance | Non-Salary - non-remunerative |
| R355 | No | Tips | Non-Salary - non-remunerative |
| R356 | No | Cooperative associated-work compensation | Non-Salary - non-remunerative |
| R357 | No (via Law 1393 excess `58104`) | Third-party payment (accrued) | Non-Salary - pacted |
| R358 | No ⚠split | Payroll advance (accrued) | Conditional |
| R359 | No | Reimbursement to the employee (accrued) | Non-Salary - non-remunerative |

**Section 2 — default `Yes` (168 rows):** every row not `NA` and not listed in Section 1. Row list (for configuration check):

```
R61, R62, R63, R64, R66, R67, R68, R69, R70, R71, R72, R73, R74, R75, R76
R77, R78, R79, R80, R81, R82, R83, R84, R85, R86, R87, R88, R89, R90, R91
R92, R93, R94, R95, R96, R97, R98, R99, R100, R101, R102, R103, R104, R105, R106
R107, R108, R109, R110, R111, R112, R113, R114, R115, R116, R117, R118, R119, R123, R124
R125, R126, R127, R128, R129, R130, R131, R132, R133, R154, R155, R157, R158, R159, R160
R161, R162, R163, R164, R165, R166, R167, R168, R169, R170, R171, R172, R173, R174, R175
R176, R177, R178, R179, R180, R181, R182, R183, R184, R185, R186, R187, R188, R189, R190
R191, R192, R193, R194, R195, R196, R197, R198, R199, R200, R238, R239, R240, R249, R250
R251, R252, R268, R269, R270, R271, R272, R273, R274, R275, R276, R287, R288, R289, R290
R291, R292, R293, R294, R295, R296, R297, R302, R303, R306, R307, R308, R309, R310, R311
R312, R313, R314, R315, R319, R323, R326, R327, R328, R329, R330, R331, R332, R333, R334
R335, R338, R352
```

## Matrix E — Solidarity pension fund (WTC column R)

**Consumed by:** `9170033`, `9170034` · **Feeds:** `58113` IBC (FSP)

Counts: `Yes` 167 · `No` 65 · `Yes/No` 58 (→ `No`: pacted rows via the Law 1393 excess, others ⚠split) · `NA` 115 (not in the matrix).

**Section 1 — overrides (123 rows):**

| WTC row | Value | Wage type | Salary class |
|---|---|---|---|
| R6 | No ⚠split | Unpaid LOA - Basic salary deduction | Salary |
| R37 | No ⚠split | Long Term Disability deduction | Salary |
| R120 | No | Severance & Seniority | Non-Salary - non-remunerative |
| R121 | No | Severance & Seniority | Non-Salary - non-remunerative |
| R122 | No | Severance & Seniority | Non-Salary - non-remunerative |
| R134 | No (via Law 1393 excess `58104`) | Bonus - profit sharing | Non-Salary - pacted |
| R135 | No (via Law 1393 excess `58104`) | Bonus - profit sharing | Non-Salary - pacted |
| R136 | No (via Law 1393 excess `58104`) | Bonus - profit sharing | Non-Salary - pacted |
| R137 | No (via Law 1393 excess `58104`) | Bonus - profit sharing | Non-Salary - pacted |
| R138 | No (via Law 1393 excess `58104`) | Bonus - profit sharing | Non-Salary - pacted |
| R139 | No (via Law 1393 excess `58104`) | Bonus - profit sharing | Non-Salary - pacted |
| R140 | No (via Law 1393 excess `58104`) | Bonus - profit sharing | Non-Salary - pacted |
| R141 | No (via Law 1393 excess `58104`) | Bonus - profit sharing | Non-Salary - pacted |
| R142 | No (via Law 1393 excess `58104`) | Bonus - profit sharing | Non-Salary - pacted |
| R143 | No (via Law 1393 excess `58104`) | Bonus - profit sharing | Non-Salary - pacted |
| R144 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R145 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R146 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R147 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R148 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R149 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R150 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R151 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R152 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R153 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R156 | No | Annual leave payout | Paid Rest |
| R201 | No (via Law 1393 excess `58104`) | Car allowance | Non-Salary - pacted |
| R202 | No (via Law 1393 excess `58104`) | Arrears - Car allowance | Non-Salary - pacted |
| R203 | No (via Law 1393 excess `58104`) | Adjustment - Car allowance | Non-Salary - pacted |
| R204 | No (via Law 1393 excess `58104`) | Advance - Car allowance | Non-Salary - pacted |
| R205 | No (via Law 1393 excess `58104`) | Car maintenance | Non-Salary - pacted |
| R206 | No (via Law 1393 excess `58104`) | Car fuel | Non-Salary - pacted |
| R207 | No | Car & Transportation allowance | Non-Salary - non-remunerative |
| R208 | No | Arrears - Car & Transportation allowance | Non-Salary - non-remunerative |
| R209 | No | Adjustment - Car & Transportation allowance | Non-Salary - non-remunerative |
| R210 | No | Transportation allowance | Non-Salary - non-remunerative |
| R211 | No | Arrears - Transportation allowance | Non-Salary - non-remunerative |
| R212 | No | Adjustment - Transportation allowance | Non-Salary - non-remunerative |
| R213 | No | Advance - Transportation allowance | Non-Salary - non-remunerative |
| R214 | No (via Law 1393 excess `58104`) | Car Maintenance Allowance 2 | Non-Salary - pacted |
| R215 | No (via Law 1393 excess `58104`) | Arrears - Car Maintenance Allowance 2 | Non-Salary - pacted |
| R216 | No (via Law 1393 excess `58104`) | Adjustment - Car Maintenance Allowance 2 | Non-Salary - pacted |
| R217 | No | Relocation allowance | Non-Salary - non-remunerative |
| R218 | No | Arrears - Relocation allowance | Non-Salary - non-remunerative |
| R219 | No | Adjustment - Relocation allowance | Non-Salary - non-remunerative |
| R220 | No | Travel ticket allowance | Non-Salary - non-remunerative |
| R221 | No | Arrears - Travel ticket allowance | Non-Salary - non-remunerative |
| R222 | No | Adjustment - Travel ticket allowance | Non-Salary - non-remunerative |
| R223 | No | Relocation allowance | Non-Salary - non-remunerative |
| R224 | No | Arrears - Relocation allowance | Non-Salary - non-remunerative |
| R225 | No | Adjustment - Relocation allowance | Non-Salary - non-remunerative |
| R226 | No | Advance - Relocation allowance | Non-Salary - non-remunerative |
| R227 | No ⚠split | Per diem allowance | Conditional |
| R228 | No | Birth and Marriage Allowance | Non-Salary - non-remunerative |
| R229 | No | Birth and Marriage Allowance | Non-Salary - non-remunerative |
| R230 | No (via Law 1393 excess `58104`) | COVID-19 Allowance | Non-Salary - pacted |
| R231 | No (via Law 1393 excess `58104`) | Medical insurance / Medical Care | Non-Salary - pacted |
| R232 | No (via Law 1393 excess `58104`) | Arrears - Medical insurance / Medical Care | Non-Salary - pacted |
| R233 | No (via Law 1393 excess `58104`) | Adjustment - Medical insurance / Medical Care | Non-Salary - pacted |
| R234 | No (via Law 1393 excess `58104`) | Medical insurance / Medical Care | Non-Salary - pacted |
| R235 | No (via Law 1393 excess `58104`) | Medical insurance / Medical Care | Non-Salary - pacted |
| R236 | No (via Law 1393 excess `58104`) | Medical insurance / Medical Care | Non-Salary - pacted |
| R237 | No (via Law 1393 excess `58104`) | Medical insurance / Medical Care | Non-Salary - pacted |
| R253 | No (via Law 1393 excess `58104`) | Benefits plan 1 | Non-Salary - pacted |
| R254 | No (via Law 1393 excess `58104`) | Benefits plan 2 | Non-Salary - pacted |
| R255 | No (via Law 1393 excess `58104`) | Education allowance | Non-Salary - pacted |
| R256 | No (via Law 1393 excess `58104`) | Schooling allowance | Non-Salary - pacted |
| R257 | No (via Law 1393 excess `58104`) | Arrears - Schooling allowance | Non-Salary - pacted |
| R258 | No (via Law 1393 excess `58104`) | Education & Schooling allowance 2 | Non-Salary - pacted |
| R259 | No (via Law 1393 excess `58104`) | Arrears - Education & Schooling allowance 2 | Non-Salary - pacted |
| R260 | No (via Law 1393 excess `58104`) | Education & Schooling allowance 3 | Non-Salary - pacted |
| R261 | No (via Law 1393 excess `58104`) | Education & Schooling allowance 4 | Non-Salary - pacted |
| R262 | No (via Law 1393 excess `58104`) | Arrears - Education & Schooling allowance 4 | Non-Salary - pacted |
| R263 | No (via Law 1393 excess `58104`) | Education & Schooling allowance 5 | Non-Salary - pacted |
| R264 | No (via Law 1393 excess `58104`) | Arrears - Education & Schooling allowance 5 | Non-Salary - pacted |
| R265 | No | Family allowance (MLA, Children) | Non-Salary - non-remunerative |
| R266 | No | Adjustment - Family allowance (MLA, Children) | Non-Salary - non-remunerative |
| R267 | No (via Law 1393 excess `58104`) | Recognition Award | Non-Salary - pacted |
| R277 | No | Post-termination payment | Non-Salary - non-remunerative |
| R278 | No | Post-termination payment | Non-Salary - non-remunerative |
| R279 | No | Post-termination payment | Non-Salary - non-remunerative |
| R280 | No | Post-termination payment | Non-Salary - non-remunerative |
| R281 | No (via Law 1393 excess `58104`) | Stock options and grants | Non-Salary - pacted |
| R282 | No | Statutory Gratuity, EOS | Non-Salary - non-remunerative |
| R283 | No | Supplemental basic (i.e. 13th or 14th months salary) | Non-Salary - non-remunerative |
| R284 | No | Gratuity, EOS, Post-termination, etc. | Non-Salary - non-remunerative |
| R285 | No | Gratuity, EOS, Post-termination, etc. | Non-Salary - non-remunerative |
| R286 | No | Gratuity, EOS, Post-termination, etc. | Non-Salary - non-remunerative |
| R298 | No (via Law 1393 excess `58104`) | Stock options and grants | Non-Salary - pacted |
| R299 | No (via Law 1393 excess `58104`) | Stock options and grants | Non-Salary - pacted |
| R300 | No (via Law 1393 excess `58104`) | Stock options and grants | Non-Salary - pacted |
| R301 | No (via Law 1393 excess `58104`) | Stock options and grants | Non-Salary - pacted |
| R304 | No | Statutory transport allowance | Non-Salary - non-remunerative |
| R305 | No | Connectivity allowance (teleworkers) | Non-Salary - non-remunerative |
| R316 | No (via Law 1393 excess `58104`) | Extra-statutory bonus under a written non-salary pact | Non-Salary - pacted |
| R317 | No (via Law 1393 excess `58104`) | Extra-statutory vacation bonus | Non-Salary - pacted |
| R318 | No | Occasional gratuity (mera liberalidad) | Non-Salary - non-remunerative |
| R320 | No | Statutory service bonus | Non-Salary - non-remunerative |
| R321 | No | Severance savings | Non-Salary - non-remunerative |
| R322 | No | Interest on severance savings | Non-Salary - non-remunerative |
| R324 | No | Vacation compensated in cash | Paid Rest |
| R325 | No | Work clothing and footwear | Non-Salary - non-remunerative |
| R338 | No ⚠split | Apprentice maintenance support | Conditional |
| R339 | No | Indemnity for dismissal without just cause | Non-Salary - non-remunerative |
| R340 | No | Late-payment penalty | Non-Salary - non-remunerative |
| R341 | No | Penalty for non-deposit of severance savings | Non-Salary - non-remunerative |
| R342 | No | Penalty for unpaid severance interest | Non-Salary - non-remunerative |
| R343 | No | Indemnity for early termination of a fixed-term or work-or-task contract | Non-Salary - non-remunerative |
| R344 | No | Indemnity for dismissal during protected status | Non-Salary - non-remunerative |
| R345 | No | Retirement or mutual-termination settlement bonus | Non-Salary - non-remunerative |
| R346 | No | Third-party meal payments | Non-Salary - non-remunerative |
| R347 | No (via Law 1393 excess `58104`) | Voucher, card or non-cash instrument payment | Non-Salary - pacted |
| R348 | No (via Law 1393 excess `58104`) | Employer-paid prepaid health / supplementary health plan | Non-Salary - pacted |
| R349 | No (via Law 1393 excess `58104`) | Employer contribution to a voluntary pension fund | Non-Salary - pacted |
| R350 | No (via Law 1393 excess `58104`) | Employer voluntary contribution to the individual pension account | Non-Salary - pacted |
| R351 | No (via Law 1393 excess `58104`) | Equity and share-incentive awards | Non-Salary - pacted |
| R353 | No | Occasional per diem, and the transport / representation portion | Non-Salary - non-remunerative |
| R354 | No | Telework allowance | Non-Salary - non-remunerative |
| R355 | No | Tips | Non-Salary - non-remunerative |
| R356 | No | Cooperative associated-work compensation | Non-Salary - non-remunerative |
| R357 | No (via Law 1393 excess `58104`) | Third-party payment (accrued) | Non-Salary - pacted |
| R358 | No ⚠split | Payroll advance (accrued) | Conditional |
| R359 | No | Reimbursement to the employee (accrued) | Non-Salary - non-remunerative |

**Section 2 — default `Yes` (167 rows):** every row not `NA` and not listed in Section 1. Row list (for configuration check):

```
R61, R62, R63, R64, R66, R67, R68, R69, R70, R71, R72, R73, R74, R75, R76
R77, R78, R79, R80, R81, R82, R83, R84, R85, R86, R87, R88, R89, R90, R91
R92, R93, R94, R95, R96, R97, R98, R99, R100, R101, R102, R103, R104, R105, R106
R107, R108, R109, R110, R111, R112, R113, R114, R115, R116, R117, R118, R119, R123, R124
R125, R126, R127, R128, R129, R130, R131, R132, R133, R154, R155, R157, R158, R159, R160
R161, R162, R163, R164, R165, R166, R167, R168, R169, R170, R171, R172, R173, R174, R175
R176, R177, R178, R179, R180, R181, R182, R183, R184, R185, R186, R187, R188, R189, R190
R191, R192, R193, R194, R195, R196, R197, R198, R199, R200, R238, R239, R240, R249, R250
R251, R252, R268, R269, R270, R271, R272, R273, R274, R275, R276, R287, R288, R289, R290
R291, R292, R293, R294, R295, R296, R297, R302, R303, R306, R307, R308, R309, R310, R311
R312, R313, R314, R315, R319, R323, R326, R327, R328, R329, R330, R331, R332, R333, R334
R335, R352
```

## Matrix F — Occupational risk (WTC column S)

**Consumed by:** `9170043` · **Feeds:** `58114` IBC (ARL)

Counts: `Yes` 156 · `No` 79 · `Yes/No` 55 (→ `No`: pacted rows via the Law 1393 excess, others ⚠split) · `NA` 115 (not in the matrix).

**Section 1 — overrides (134 rows):**

| WTC row | Value | Wage type | Salary class |
|---|---|---|---|
| R6 | No | Unpaid LOA - Basic salary deduction | Salary |
| R37 | No | Long Term Disability deduction | Salary |
| R120 | No | Severance & Seniority | Non-Salary - non-remunerative |
| R121 | No | Severance & Seniority | Non-Salary - non-remunerative |
| R122 | No | Severance & Seniority | Non-Salary - non-remunerative |
| R123 | No | Long Term Disability | Non-Salary - non-remunerative |
| R134 | No (via Law 1393 excess `58104`) | Bonus - profit sharing | Non-Salary - pacted |
| R135 | No (via Law 1393 excess `58104`) | Bonus - profit sharing | Non-Salary - pacted |
| R136 | No (via Law 1393 excess `58104`) | Bonus - profit sharing | Non-Salary - pacted |
| R137 | No (via Law 1393 excess `58104`) | Bonus - profit sharing | Non-Salary - pacted |
| R138 | No (via Law 1393 excess `58104`) | Bonus - profit sharing | Non-Salary - pacted |
| R139 | No (via Law 1393 excess `58104`) | Bonus - profit sharing | Non-Salary - pacted |
| R140 | No (via Law 1393 excess `58104`) | Bonus - profit sharing | Non-Salary - pacted |
| R141 | No (via Law 1393 excess `58104`) | Bonus - profit sharing | Non-Salary - pacted |
| R142 | No (via Law 1393 excess `58104`) | Bonus - profit sharing | Non-Salary - pacted |
| R143 | No (via Law 1393 excess `58104`) | Bonus - profit sharing | Non-Salary - pacted |
| R144 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R145 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R146 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R147 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R148 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R149 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R150 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R151 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R152 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R153 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R154 | No | Annual leave pay | Salary |
| R155 | No | Adjustment - Annual leave pay | Salary |
| R156 | No | Annual leave payout | Paid Rest |
| R201 | No (via Law 1393 excess `58104`) | Car allowance | Non-Salary - pacted |
| R202 | No (via Law 1393 excess `58104`) | Arrears - Car allowance | Non-Salary - pacted |
| R203 | No (via Law 1393 excess `58104`) | Adjustment - Car allowance | Non-Salary - pacted |
| R204 | No (via Law 1393 excess `58104`) | Advance - Car allowance | Non-Salary - pacted |
| R205 | No (via Law 1393 excess `58104`) | Car maintenance | Non-Salary - pacted |
| R206 | No (via Law 1393 excess `58104`) | Car fuel | Non-Salary - pacted |
| R207 | No | Car & Transportation allowance | Non-Salary - non-remunerative |
| R208 | No | Arrears - Car & Transportation allowance | Non-Salary - non-remunerative |
| R209 | No | Adjustment - Car & Transportation allowance | Non-Salary - non-remunerative |
| R210 | No | Transportation allowance | Non-Salary - non-remunerative |
| R211 | No | Arrears - Transportation allowance | Non-Salary - non-remunerative |
| R212 | No | Adjustment - Transportation allowance | Non-Salary - non-remunerative |
| R213 | No | Advance - Transportation allowance | Non-Salary - non-remunerative |
| R214 | No (via Law 1393 excess `58104`) | Car Maintenance Allowance 2 | Non-Salary - pacted |
| R215 | No (via Law 1393 excess `58104`) | Arrears - Car Maintenance Allowance 2 | Non-Salary - pacted |
| R216 | No (via Law 1393 excess `58104`) | Adjustment - Car Maintenance Allowance 2 | Non-Salary - pacted |
| R217 | No | Relocation allowance | Non-Salary - non-remunerative |
| R218 | No | Arrears - Relocation allowance | Non-Salary - non-remunerative |
| R219 | No | Adjustment - Relocation allowance | Non-Salary - non-remunerative |
| R220 | No | Travel ticket allowance | Non-Salary - non-remunerative |
| R221 | No | Arrears - Travel ticket allowance | Non-Salary - non-remunerative |
| R222 | No | Adjustment - Travel ticket allowance | Non-Salary - non-remunerative |
| R223 | No | Relocation allowance | Non-Salary - non-remunerative |
| R224 | No | Arrears - Relocation allowance | Non-Salary - non-remunerative |
| R225 | No | Adjustment - Relocation allowance | Non-Salary - non-remunerative |
| R226 | No | Advance - Relocation allowance | Non-Salary - non-remunerative |
| R227 | No ⚠split | Per diem allowance | Conditional |
| R228 | No | Birth and Marriage Allowance | Non-Salary - non-remunerative |
| R229 | No | Birth and Marriage Allowance | Non-Salary - non-remunerative |
| R230 | No (via Law 1393 excess `58104`) | COVID-19 Allowance | Non-Salary - pacted |
| R231 | No (via Law 1393 excess `58104`) | Medical insurance / Medical Care | Non-Salary - pacted |
| R232 | No (via Law 1393 excess `58104`) | Arrears - Medical insurance / Medical Care | Non-Salary - pacted |
| R233 | No (via Law 1393 excess `58104`) | Adjustment - Medical insurance / Medical Care | Non-Salary - pacted |
| R234 | No (via Law 1393 excess `58104`) | Medical insurance / Medical Care | Non-Salary - pacted |
| R235 | No (via Law 1393 excess `58104`) | Medical insurance / Medical Care | Non-Salary - pacted |
| R236 | No (via Law 1393 excess `58104`) | Medical insurance / Medical Care | Non-Salary - pacted |
| R237 | No (via Law 1393 excess `58104`) | Medical insurance / Medical Care | Non-Salary - pacted |
| R253 | No (via Law 1393 excess `58104`) | Benefits plan 1 | Non-Salary - pacted |
| R254 | No (via Law 1393 excess `58104`) | Benefits plan 2 | Non-Salary - pacted |
| R255 | No (via Law 1393 excess `58104`) | Education allowance | Non-Salary - pacted |
| R256 | No (via Law 1393 excess `58104`) | Schooling allowance | Non-Salary - pacted |
| R257 | No (via Law 1393 excess `58104`) | Arrears - Schooling allowance | Non-Salary - pacted |
| R258 | No (via Law 1393 excess `58104`) | Education & Schooling allowance 2 | Non-Salary - pacted |
| R259 | No (via Law 1393 excess `58104`) | Arrears - Education & Schooling allowance 2 | Non-Salary - pacted |
| R260 | No (via Law 1393 excess `58104`) | Education & Schooling allowance 3 | Non-Salary - pacted |
| R261 | No (via Law 1393 excess `58104`) | Education & Schooling allowance 4 | Non-Salary - pacted |
| R262 | No (via Law 1393 excess `58104`) | Arrears - Education & Schooling allowance 4 | Non-Salary - pacted |
| R263 | No (via Law 1393 excess `58104`) | Education & Schooling allowance 5 | Non-Salary - pacted |
| R264 | No (via Law 1393 excess `58104`) | Arrears - Education & Schooling allowance 5 | Non-Salary - pacted |
| R265 | No | Family allowance (MLA, Children) | Non-Salary - non-remunerative |
| R266 | No | Adjustment - Family allowance (MLA, Children) | Non-Salary - non-remunerative |
| R267 | No (via Law 1393 excess `58104`) | Recognition Award | Non-Salary - pacted |
| R277 | No | Post-termination payment | Non-Salary - non-remunerative |
| R278 | No | Post-termination payment | Non-Salary - non-remunerative |
| R279 | No | Post-termination payment | Non-Salary - non-remunerative |
| R280 | No | Post-termination payment | Non-Salary - non-remunerative |
| R281 | No (via Law 1393 excess `58104`) | Stock options and grants | Non-Salary - pacted |
| R282 | No | Statutory Gratuity, EOS | Non-Salary - non-remunerative |
| R283 | No | Supplemental basic (i.e. 13th or 14th months salary) | Non-Salary - non-remunerative |
| R284 | No | Gratuity, EOS, Post-termination, etc. | Non-Salary - non-remunerative |
| R285 | No | Gratuity, EOS, Post-termination, etc. | Non-Salary - non-remunerative |
| R286 | No | Gratuity, EOS, Post-termination, etc. | Non-Salary - non-remunerative |
| R298 | No (via Law 1393 excess `58104`) | Stock options and grants | Non-Salary - pacted |
| R299 | No (via Law 1393 excess `58104`) | Stock options and grants | Non-Salary - pacted |
| R300 | No (via Law 1393 excess `58104`) | Stock options and grants | Non-Salary - pacted |
| R301 | No (via Law 1393 excess `58104`) | Stock options and grants | Non-Salary - pacted |
| R304 | No | Statutory transport allowance | Non-Salary - non-remunerative |
| R305 | No | Connectivity allowance (teleworkers) | Non-Salary - non-remunerative |
| R316 | No (via Law 1393 excess `58104`) | Extra-statutory bonus under a written non-salary pact | Non-Salary - pacted |
| R317 | No (via Law 1393 excess `58104`) | Extra-statutory vacation bonus | Non-Salary - pacted |
| R318 | No | Occasional gratuity (mera liberalidad) | Non-Salary - non-remunerative |
| R320 | No | Statutory service bonus | Non-Salary - non-remunerative |
| R321 | No | Severance savings | Non-Salary - non-remunerative |
| R322 | No | Interest on severance savings | Non-Salary - non-remunerative |
| R323 | No | Annual leave taken | Salary |
| R324 | No | Vacation compensated in cash | Paid Rest |
| R325 | No | Work clothing and footwear | Non-Salary - non-remunerative |
| R326 | No | Sickness incapacity, days 1-2 (employer) | Non-Salary - non-remunerative |
| R327 | No | Sickness incapacity from day 3 (EPS) | Non-Salary - non-remunerative |
| R328 | No | Occupational accident or disease incapacity (ARL) | Non-Salary - non-remunerative |
| R329 | No | Sickness incapacity beyond day 180 (AFP / EPS) | Non-Salary - non-remunerative |
| R330 | No | Maternity leave (18 weeks) | Non-Salary - non-remunerative |
| R331 | No | Paternity leave (2 weeks) | Non-Salary - non-remunerative |
| R332 | No | Shared and flexible parental leave | Non-Salary - non-remunerative |
| R333 | No | Childcare leave (10 working days per year, EPS) | Non-Salary - non-remunerative |
| R339 | No | Indemnity for dismissal without just cause | Non-Salary - non-remunerative |
| R340 | No | Late-payment penalty | Non-Salary - non-remunerative |
| R341 | No | Penalty for non-deposit of severance savings | Non-Salary - non-remunerative |
| R342 | No | Penalty for unpaid severance interest | Non-Salary - non-remunerative |
| R343 | No | Indemnity for early termination of a fixed-term or work-or-task contract | Non-Salary - non-remunerative |
| R344 | No | Indemnity for dismissal during protected status | Non-Salary - non-remunerative |
| R345 | No | Retirement or mutual-termination settlement bonus | Non-Salary - non-remunerative |
| R346 | No | Third-party meal payments | Non-Salary - non-remunerative |
| R347 | No (via Law 1393 excess `58104`) | Voucher, card or non-cash instrument payment | Non-Salary - pacted |
| R348 | No (via Law 1393 excess `58104`) | Employer-paid prepaid health / supplementary health plan | Non-Salary - pacted |
| R349 | No (via Law 1393 excess `58104`) | Employer contribution to a voluntary pension fund | Non-Salary - pacted |
| R350 | No (via Law 1393 excess `58104`) | Employer voluntary contribution to the individual pension account | Non-Salary - pacted |
| R351 | No (via Law 1393 excess `58104`) | Equity and share-incentive awards | Non-Salary - pacted |
| R353 | No | Occasional per diem, and the transport / representation portion | Non-Salary - non-remunerative |
| R354 | No | Telework allowance | Non-Salary - non-remunerative |
| R355 | No | Tips | Non-Salary - non-remunerative |
| R356 | No | Cooperative associated-work compensation | Non-Salary - non-remunerative |
| R357 | No (via Law 1393 excess `58104`) | Third-party payment (accrued) | Non-Salary - pacted |
| R358 | No ⚠split | Payroll advance (accrued) | Conditional |
| R359 | No | Reimbursement to the employee (accrued) | Non-Salary - non-remunerative |

**Section 2 — default `Yes` (156 rows):** every row not `NA` and not listed in Section 1. Row list (for configuration check):

```
R61, R62, R63, R64, R66, R67, R68, R69, R70, R71, R72, R73, R74, R75, R76
R77, R78, R79, R80, R81, R82, R83, R84, R85, R86, R87, R88, R89, R90, R91
R92, R93, R94, R95, R96, R97, R98, R99, R100, R101, R102, R103, R104, R105, R106
R107, R108, R109, R110, R111, R112, R113, R114, R115, R116, R117, R118, R119, R124, R125
R126, R127, R128, R129, R130, R131, R132, R133, R157, R158, R159, R160, R161, R162, R163
R164, R165, R166, R167, R168, R169, R170, R171, R172, R173, R174, R175, R176, R177, R178
R179, R180, R181, R182, R183, R184, R185, R186, R187, R188, R189, R190, R191, R192, R193
R194, R195, R196, R197, R198, R199, R200, R238, R239, R240, R249, R250, R251, R252, R268
R269, R270, R271, R272, R273, R274, R275, R276, R287, R288, R289, R290, R291, R292, R293
R294, R295, R296, R297, R302, R303, R306, R307, R308, R309, R310, R311, R312, R313, R314
R315, R319, R334, R335, R338, R352
```

## Matrix G — Payroll levies (CCF / SENA / ICBF) (WTC column T)

**Consumed by:** `9170023`, `9170044`–`9170046` · **Feeds:** `58108` levy base

Counts: `Yes` 160 · `No` 126 · `Yes/No` 4 (→ `No`: pacted rows via the Law 1393 excess, others ⚠split) · `NA` 115 (not in the matrix).

**Section 1 — overrides (130 rows):**

| WTC row | Value | Wage type | Salary class |
|---|---|---|---|
| R6 | No ⚠split | Unpaid LOA - Basic salary deduction | Salary |
| R37 | No | Long Term Disability deduction | Salary |
| R120 | No | Severance & Seniority | Non-Salary - non-remunerative |
| R121 | No | Severance & Seniority | Non-Salary - non-remunerative |
| R122 | No | Severance & Seniority | Non-Salary - non-remunerative |
| R123 | No | Long Term Disability | Non-Salary - non-remunerative |
| R134 | No | Bonus - profit sharing | Non-Salary - pacted |
| R135 | No | Bonus - profit sharing | Non-Salary - pacted |
| R136 | No | Bonus - profit sharing | Non-Salary - pacted |
| R137 | No | Bonus - profit sharing | Non-Salary - pacted |
| R138 | No | Bonus - profit sharing | Non-Salary - pacted |
| R139 | No | Bonus - profit sharing | Non-Salary - pacted |
| R140 | No | Bonus - profit sharing | Non-Salary - pacted |
| R141 | No | Bonus - profit sharing | Non-Salary - pacted |
| R142 | No | Bonus - profit sharing | Non-Salary - pacted |
| R143 | No | Bonus - profit sharing | Non-Salary - pacted |
| R144 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R145 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R146 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R147 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R148 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R149 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R150 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R151 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R152 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R153 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R201 | No | Car allowance | Non-Salary - pacted |
| R202 | No | Arrears - Car allowance | Non-Salary - pacted |
| R203 | No | Adjustment - Car allowance | Non-Salary - pacted |
| R204 | No | Advance - Car allowance | Non-Salary - pacted |
| R205 | No | Car maintenance | Non-Salary - pacted |
| R206 | No | Car fuel | Non-Salary - pacted |
| R207 | No | Car & Transportation allowance | Non-Salary - non-remunerative |
| R208 | No | Arrears - Car & Transportation allowance | Non-Salary - non-remunerative |
| R209 | No | Adjustment - Car & Transportation allowance | Non-Salary - non-remunerative |
| R210 | No | Transportation allowance | Non-Salary - non-remunerative |
| R211 | No | Arrears - Transportation allowance | Non-Salary - non-remunerative |
| R212 | No | Adjustment - Transportation allowance | Non-Salary - non-remunerative |
| R213 | No | Advance - Transportation allowance | Non-Salary - non-remunerative |
| R214 | No | Car Maintenance Allowance 2 | Non-Salary - pacted |
| R215 | No | Arrears - Car Maintenance Allowance 2 | Non-Salary - pacted |
| R216 | No | Adjustment - Car Maintenance Allowance 2 | Non-Salary - pacted |
| R217 | No | Relocation allowance | Non-Salary - non-remunerative |
| R218 | No | Arrears - Relocation allowance | Non-Salary - non-remunerative |
| R219 | No | Adjustment - Relocation allowance | Non-Salary - non-remunerative |
| R220 | No | Travel ticket allowance | Non-Salary - non-remunerative |
| R221 | No | Arrears - Travel ticket allowance | Non-Salary - non-remunerative |
| R222 | No | Adjustment - Travel ticket allowance | Non-Salary - non-remunerative |
| R223 | No | Relocation allowance | Non-Salary - non-remunerative |
| R224 | No | Arrears - Relocation allowance | Non-Salary - non-remunerative |
| R225 | No | Adjustment - Relocation allowance | Non-Salary - non-remunerative |
| R226 | No | Advance - Relocation allowance | Non-Salary - non-remunerative |
| R227 | No ⚠split | Per diem allowance | Conditional |
| R228 | No | Birth and Marriage Allowance | Non-Salary - non-remunerative |
| R229 | No | Birth and Marriage Allowance | Non-Salary - non-remunerative |
| R230 | No | COVID-19 Allowance | Non-Salary - pacted |
| R231 | No | Medical insurance / Medical Care | Non-Salary - pacted |
| R232 | No | Arrears - Medical insurance / Medical Care | Non-Salary - pacted |
| R233 | No | Adjustment - Medical insurance / Medical Care | Non-Salary - pacted |
| R234 | No | Medical insurance / Medical Care | Non-Salary - pacted |
| R235 | No | Medical insurance / Medical Care | Non-Salary - pacted |
| R236 | No | Medical insurance / Medical Care | Non-Salary - pacted |
| R237 | No | Medical insurance / Medical Care | Non-Salary - pacted |
| R253 | No | Benefits plan 1 | Non-Salary - pacted |
| R254 | No | Benefits plan 2 | Non-Salary - pacted |
| R255 | No | Education allowance | Non-Salary - pacted |
| R256 | No | Schooling allowance | Non-Salary - pacted |
| R257 | No | Arrears - Schooling allowance | Non-Salary - pacted |
| R258 | No | Education & Schooling allowance 2 | Non-Salary - pacted |
| R259 | No | Arrears - Education & Schooling allowance 2 | Non-Salary - pacted |
| R260 | No | Education & Schooling allowance 3 | Non-Salary - pacted |
| R261 | No | Education & Schooling allowance 4 | Non-Salary - pacted |
| R262 | No | Arrears - Education & Schooling allowance 4 | Non-Salary - pacted |
| R263 | No | Education & Schooling allowance 5 | Non-Salary - pacted |
| R264 | No | Arrears - Education & Schooling allowance 5 | Non-Salary - pacted |
| R265 | No | Family allowance (MLA, Children) | Non-Salary - non-remunerative |
| R266 | No | Adjustment - Family allowance (MLA, Children) | Non-Salary - non-remunerative |
| R267 | No | Recognition Award | Non-Salary - pacted |
| R277 | No | Post-termination payment | Non-Salary - non-remunerative |
| R278 | No | Post-termination payment | Non-Salary - non-remunerative |
| R279 | No | Post-termination payment | Non-Salary - non-remunerative |
| R280 | No | Post-termination payment | Non-Salary - non-remunerative |
| R281 | No | Stock options and grants | Non-Salary - pacted |
| R282 | No | Statutory Gratuity, EOS | Non-Salary - non-remunerative |
| R283 | No | Supplemental basic (i.e. 13th or 14th months salary) | Non-Salary - non-remunerative |
| R284 | No | Gratuity, EOS, Post-termination, etc. | Non-Salary - non-remunerative |
| R285 | No | Gratuity, EOS, Post-termination, etc. | Non-Salary - non-remunerative |
| R286 | No | Gratuity, EOS, Post-termination, etc. | Non-Salary - non-remunerative |
| R298 | No | Stock options and grants | Non-Salary - pacted |
| R299 | No | Stock options and grants | Non-Salary - pacted |
| R300 | No | Stock options and grants | Non-Salary - pacted |
| R301 | No | Stock options and grants | Non-Salary - pacted |
| R304 | No | Statutory transport allowance | Non-Salary - non-remunerative |
| R305 | No | Connectivity allowance (teleworkers) | Non-Salary - non-remunerative |
| R316 | No | Extra-statutory bonus under a written non-salary pact | Non-Salary - pacted |
| R317 | No | Extra-statutory vacation bonus | Non-Salary - pacted |
| R318 | No | Occasional gratuity (mera liberalidad) | Non-Salary - non-remunerative |
| R320 | No | Statutory service bonus | Non-Salary - non-remunerative |
| R321 | No | Severance savings | Non-Salary - non-remunerative |
| R322 | No | Interest on severance savings | Non-Salary - non-remunerative |
| R325 | No | Work clothing and footwear | Non-Salary - non-remunerative |
| R326 | No | Sickness incapacity, days 1-2 (employer) | Non-Salary - non-remunerative |
| R327 | No | Sickness incapacity from day 3 (EPS) | Non-Salary - non-remunerative |
| R328 | No | Occupational accident or disease incapacity (ARL) | Non-Salary - non-remunerative |
| R329 | No | Sickness incapacity beyond day 180 (AFP / EPS) | Non-Salary - non-remunerative |
| R330 | No | Maternity leave (18 weeks) | Non-Salary - non-remunerative |
| R331 | No | Paternity leave (2 weeks) | Non-Salary - non-remunerative |
| R332 | No | Shared and flexible parental leave | Non-Salary - non-remunerative |
| R333 | No | Childcare leave (10 working days per year, EPS) | Non-Salary - non-remunerative |
| R338 | No ⚠split | Apprentice maintenance support | Conditional |
| R339 | No | Indemnity for dismissal without just cause | Non-Salary - non-remunerative |
| R340 | No | Late-payment penalty | Non-Salary - non-remunerative |
| R341 | No | Penalty for non-deposit of severance savings | Non-Salary - non-remunerative |
| R342 | No | Penalty for unpaid severance interest | Non-Salary - non-remunerative |
| R343 | No | Indemnity for early termination of a fixed-term or work-or-task contract | Non-Salary - non-remunerative |
| R344 | No | Indemnity for dismissal during protected status | Non-Salary - non-remunerative |
| R345 | No | Retirement or mutual-termination settlement bonus | Non-Salary - non-remunerative |
| R346 | No | Third-party meal payments | Non-Salary - non-remunerative |
| R347 | No | Voucher, card or non-cash instrument payment | Non-Salary - pacted |
| R348 | No | Employer-paid prepaid health / supplementary health plan | Non-Salary - pacted |
| R349 | No | Employer contribution to a voluntary pension fund | Non-Salary - pacted |
| R350 | No | Employer voluntary contribution to the individual pension account | Non-Salary - pacted |
| R351 | No | Equity and share-incentive awards | Non-Salary - pacted |
| R353 | No | Occasional per diem, and the transport / representation portion | Non-Salary - non-remunerative |
| R354 | No | Telework allowance | Non-Salary - non-remunerative |
| R355 | No | Tips | Non-Salary - non-remunerative |
| R356 | No | Cooperative associated-work compensation | Non-Salary - non-remunerative |
| R357 | No | Third-party payment (accrued) | Non-Salary - pacted |
| R358 | No ⚠split | Payroll advance (accrued) | Conditional |
| R359 | No | Reimbursement to the employee (accrued) | Non-Salary - non-remunerative |

**Section 2 — default `Yes` (160 rows):** every row not `NA` and not listed in Section 1. Row list (for configuration check):

```
R61, R62, R63, R64, R66, R67, R68, R69, R70, R71, R72, R73, R74, R75, R76
R77, R78, R79, R80, R81, R82, R83, R84, R85, R86, R87, R88, R89, R90, R91
R92, R93, R94, R95, R96, R97, R98, R99, R100, R101, R102, R103, R104, R105, R106
R107, R108, R109, R110, R111, R112, R113, R114, R115, R116, R117, R118, R119, R124, R125
R126, R127, R128, R129, R130, R131, R132, R133, R154, R155, R156, R157, R158, R159, R160
R161, R162, R163, R164, R165, R166, R167, R168, R169, R170, R171, R172, R173, R174, R175
R176, R177, R178, R179, R180, R181, R182, R183, R184, R185, R186, R187, R188, R189, R190
R191, R192, R193, R194, R195, R196, R197, R198, R199, R200, R238, R239, R240, R249, R250
R251, R252, R268, R269, R270, R271, R272, R273, R274, R275, R276, R287, R288, R289, R290
R291, R292, R293, R294, R295, R296, R297, R302, R303, R306, R307, R308, R309, R310, R311
R312, R313, R314, R315, R319, R323, R324, R334, R335, R352
```

## Matrix H — Pension (WTC column U)

**Consumed by:** `9170032`, `9170042` · **Feeds:** `58112` IBC (pension)

Counts: `Yes` 167 · `No` 66 · `Yes/No` 57 (→ `No`: pacted rows via the Law 1393 excess, others ⚠split) · `NA` 115 (not in the matrix).

**Section 1 — overrides (123 rows):**

| WTC row | Value | Wage type | Salary class |
|---|---|---|---|
| R6 | No ⚠split | Unpaid LOA - Basic salary deduction | Salary |
| R37 | No | Long Term Disability deduction | Salary |
| R120 | No | Severance & Seniority | Non-Salary - non-remunerative |
| R121 | No | Severance & Seniority | Non-Salary - non-remunerative |
| R122 | No | Severance & Seniority | Non-Salary - non-remunerative |
| R134 | No (via Law 1393 excess `58104`) | Bonus - profit sharing | Non-Salary - pacted |
| R135 | No (via Law 1393 excess `58104`) | Bonus - profit sharing | Non-Salary - pacted |
| R136 | No (via Law 1393 excess `58104`) | Bonus - profit sharing | Non-Salary - pacted |
| R137 | No (via Law 1393 excess `58104`) | Bonus - profit sharing | Non-Salary - pacted |
| R138 | No (via Law 1393 excess `58104`) | Bonus - profit sharing | Non-Salary - pacted |
| R139 | No (via Law 1393 excess `58104`) | Bonus - profit sharing | Non-Salary - pacted |
| R140 | No (via Law 1393 excess `58104`) | Bonus - profit sharing | Non-Salary - pacted |
| R141 | No (via Law 1393 excess `58104`) | Bonus - profit sharing | Non-Salary - pacted |
| R142 | No (via Law 1393 excess `58104`) | Bonus - profit sharing | Non-Salary - pacted |
| R143 | No (via Law 1393 excess `58104`) | Bonus - profit sharing | Non-Salary - pacted |
| R144 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R145 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R146 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R147 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R148 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R149 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R150 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R151 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R152 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R153 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R156 | No | Annual leave payout | Paid Rest |
| R201 | No (via Law 1393 excess `58104`) | Car allowance | Non-Salary - pacted |
| R202 | No (via Law 1393 excess `58104`) | Arrears - Car allowance | Non-Salary - pacted |
| R203 | No (via Law 1393 excess `58104`) | Adjustment - Car allowance | Non-Salary - pacted |
| R204 | No (via Law 1393 excess `58104`) | Advance - Car allowance | Non-Salary - pacted |
| R205 | No (via Law 1393 excess `58104`) | Car maintenance | Non-Salary - pacted |
| R206 | No (via Law 1393 excess `58104`) | Car fuel | Non-Salary - pacted |
| R207 | No | Car & Transportation allowance | Non-Salary - non-remunerative |
| R208 | No | Arrears - Car & Transportation allowance | Non-Salary - non-remunerative |
| R209 | No | Adjustment - Car & Transportation allowance | Non-Salary - non-remunerative |
| R210 | No | Transportation allowance | Non-Salary - non-remunerative |
| R211 | No | Arrears - Transportation allowance | Non-Salary - non-remunerative |
| R212 | No | Adjustment - Transportation allowance | Non-Salary - non-remunerative |
| R213 | No | Advance - Transportation allowance | Non-Salary - non-remunerative |
| R214 | No (via Law 1393 excess `58104`) | Car Maintenance Allowance 2 | Non-Salary - pacted |
| R215 | No (via Law 1393 excess `58104`) | Arrears - Car Maintenance Allowance 2 | Non-Salary - pacted |
| R216 | No (via Law 1393 excess `58104`) | Adjustment - Car Maintenance Allowance 2 | Non-Salary - pacted |
| R217 | No | Relocation allowance | Non-Salary - non-remunerative |
| R218 | No | Arrears - Relocation allowance | Non-Salary - non-remunerative |
| R219 | No | Adjustment - Relocation allowance | Non-Salary - non-remunerative |
| R220 | No | Travel ticket allowance | Non-Salary - non-remunerative |
| R221 | No | Arrears - Travel ticket allowance | Non-Salary - non-remunerative |
| R222 | No | Adjustment - Travel ticket allowance | Non-Salary - non-remunerative |
| R223 | No | Relocation allowance | Non-Salary - non-remunerative |
| R224 | No | Arrears - Relocation allowance | Non-Salary - non-remunerative |
| R225 | No | Adjustment - Relocation allowance | Non-Salary - non-remunerative |
| R226 | No | Advance - Relocation allowance | Non-Salary - non-remunerative |
| R227 | No ⚠split | Per diem allowance | Conditional |
| R228 | No | Birth and Marriage Allowance | Non-Salary - non-remunerative |
| R229 | No | Birth and Marriage Allowance | Non-Salary - non-remunerative |
| R230 | No (via Law 1393 excess `58104`) | COVID-19 Allowance | Non-Salary - pacted |
| R231 | No (via Law 1393 excess `58104`) | Medical insurance / Medical Care | Non-Salary - pacted |
| R232 | No (via Law 1393 excess `58104`) | Arrears - Medical insurance / Medical Care | Non-Salary - pacted |
| R233 | No (via Law 1393 excess `58104`) | Adjustment - Medical insurance / Medical Care | Non-Salary - pacted |
| R234 | No (via Law 1393 excess `58104`) | Medical insurance / Medical Care | Non-Salary - pacted |
| R235 | No (via Law 1393 excess `58104`) | Medical insurance / Medical Care | Non-Salary - pacted |
| R236 | No (via Law 1393 excess `58104`) | Medical insurance / Medical Care | Non-Salary - pacted |
| R237 | No (via Law 1393 excess `58104`) | Medical insurance / Medical Care | Non-Salary - pacted |
| R253 | No (via Law 1393 excess `58104`) | Benefits plan 1 | Non-Salary - pacted |
| R254 | No (via Law 1393 excess `58104`) | Benefits plan 2 | Non-Salary - pacted |
| R255 | No (via Law 1393 excess `58104`) | Education allowance | Non-Salary - pacted |
| R256 | No (via Law 1393 excess `58104`) | Schooling allowance | Non-Salary - pacted |
| R257 | No (via Law 1393 excess `58104`) | Arrears - Schooling allowance | Non-Salary - pacted |
| R258 | No (via Law 1393 excess `58104`) | Education & Schooling allowance 2 | Non-Salary - pacted |
| R259 | No (via Law 1393 excess `58104`) | Arrears - Education & Schooling allowance 2 | Non-Salary - pacted |
| R260 | No (via Law 1393 excess `58104`) | Education & Schooling allowance 3 | Non-Salary - pacted |
| R261 | No (via Law 1393 excess `58104`) | Education & Schooling allowance 4 | Non-Salary - pacted |
| R262 | No (via Law 1393 excess `58104`) | Arrears - Education & Schooling allowance 4 | Non-Salary - pacted |
| R263 | No (via Law 1393 excess `58104`) | Education & Schooling allowance 5 | Non-Salary - pacted |
| R264 | No (via Law 1393 excess `58104`) | Arrears - Education & Schooling allowance 5 | Non-Salary - pacted |
| R265 | No | Family allowance (MLA, Children) | Non-Salary - non-remunerative |
| R266 | No | Adjustment - Family allowance (MLA, Children) | Non-Salary - non-remunerative |
| R267 | No (via Law 1393 excess `58104`) | Recognition Award | Non-Salary - pacted |
| R277 | No | Post-termination payment | Non-Salary - non-remunerative |
| R278 | No | Post-termination payment | Non-Salary - non-remunerative |
| R279 | No | Post-termination payment | Non-Salary - non-remunerative |
| R280 | No | Post-termination payment | Non-Salary - non-remunerative |
| R281 | No (via Law 1393 excess `58104`) | Stock options and grants | Non-Salary - pacted |
| R282 | No | Statutory Gratuity, EOS | Non-Salary - non-remunerative |
| R283 | No | Supplemental basic (i.e. 13th or 14th months salary) | Non-Salary - non-remunerative |
| R284 | No | Gratuity, EOS, Post-termination, etc. | Non-Salary - non-remunerative |
| R285 | No | Gratuity, EOS, Post-termination, etc. | Non-Salary - non-remunerative |
| R286 | No | Gratuity, EOS, Post-termination, etc. | Non-Salary - non-remunerative |
| R298 | No (via Law 1393 excess `58104`) | Stock options and grants | Non-Salary - pacted |
| R299 | No (via Law 1393 excess `58104`) | Stock options and grants | Non-Salary - pacted |
| R300 | No (via Law 1393 excess `58104`) | Stock options and grants | Non-Salary - pacted |
| R301 | No (via Law 1393 excess `58104`) | Stock options and grants | Non-Salary - pacted |
| R304 | No | Statutory transport allowance | Non-Salary - non-remunerative |
| R305 | No | Connectivity allowance (teleworkers) | Non-Salary - non-remunerative |
| R316 | No (via Law 1393 excess `58104`) | Extra-statutory bonus under a written non-salary pact | Non-Salary - pacted |
| R317 | No (via Law 1393 excess `58104`) | Extra-statutory vacation bonus | Non-Salary - pacted |
| R318 | No | Occasional gratuity (mera liberalidad) | Non-Salary - non-remunerative |
| R320 | No | Statutory service bonus | Non-Salary - non-remunerative |
| R321 | No | Severance savings | Non-Salary - non-remunerative |
| R322 | No | Interest on severance savings | Non-Salary - non-remunerative |
| R324 | No | Vacation compensated in cash | Paid Rest |
| R325 | No | Work clothing and footwear | Non-Salary - non-remunerative |
| R338 | No ⚠split | Apprentice maintenance support | Conditional |
| R339 | No | Indemnity for dismissal without just cause | Non-Salary - non-remunerative |
| R340 | No | Late-payment penalty | Non-Salary - non-remunerative |
| R341 | No | Penalty for non-deposit of severance savings | Non-Salary - non-remunerative |
| R342 | No | Penalty for unpaid severance interest | Non-Salary - non-remunerative |
| R343 | No | Indemnity for early termination of a fixed-term or work-or-task contract | Non-Salary - non-remunerative |
| R344 | No | Indemnity for dismissal during protected status | Non-Salary - non-remunerative |
| R345 | No | Retirement or mutual-termination settlement bonus | Non-Salary - non-remunerative |
| R346 | No | Third-party meal payments | Non-Salary - non-remunerative |
| R347 | No (via Law 1393 excess `58104`) | Voucher, card or non-cash instrument payment | Non-Salary - pacted |
| R348 | No (via Law 1393 excess `58104`) | Employer-paid prepaid health / supplementary health plan | Non-Salary - pacted |
| R349 | No (via Law 1393 excess `58104`) | Employer contribution to a voluntary pension fund | Non-Salary - pacted |
| R350 | No (via Law 1393 excess `58104`) | Employer voluntary contribution to the individual pension account | Non-Salary - pacted |
| R351 | No (via Law 1393 excess `58104`) | Equity and share-incentive awards | Non-Salary - pacted |
| R353 | No | Occasional per diem, and the transport / representation portion | Non-Salary - non-remunerative |
| R354 | No | Telework allowance | Non-Salary - non-remunerative |
| R355 | No | Tips | Non-Salary - non-remunerative |
| R356 | No | Cooperative associated-work compensation | Non-Salary - non-remunerative |
| R357 | No (via Law 1393 excess `58104`) | Third-party payment (accrued) | Non-Salary - pacted |
| R358 | No ⚠split | Payroll advance (accrued) | Conditional |
| R359 | No | Reimbursement to the employee (accrued) | Non-Salary - non-remunerative |

**Section 2 — default `Yes` (167 rows):** every row not `NA` and not listed in Section 1. Row list (for configuration check):

```
R61, R62, R63, R64, R66, R67, R68, R69, R70, R71, R72, R73, R74, R75, R76
R77, R78, R79, R80, R81, R82, R83, R84, R85, R86, R87, R88, R89, R90, R91
R92, R93, R94, R95, R96, R97, R98, R99, R100, R101, R102, R103, R104, R105, R106
R107, R108, R109, R110, R111, R112, R113, R114, R115, R116, R117, R118, R119, R123, R124
R125, R126, R127, R128, R129, R130, R131, R132, R133, R154, R155, R157, R158, R159, R160
R161, R162, R163, R164, R165, R166, R167, R168, R169, R170, R171, R172, R173, R174, R175
R176, R177, R178, R179, R180, R181, R182, R183, R184, R185, R186, R187, R188, R189, R190
R191, R192, R193, R194, R195, R196, R197, R198, R199, R200, R238, R239, R240, R249, R250
R251, R252, R268, R269, R270, R271, R272, R273, R274, R275, R276, R287, R288, R289, R290
R291, R292, R293, R294, R295, R296, R297, R302, R303, R306, R307, R308, R309, R310, R311
R312, R313, R314, R315, R319, R323, R326, R327, R328, R329, R330, R331, R332, R333, R334
R335, R352
```

## Matrix I — Statutory-benefit base (prima / cesantías / interest) (WTC column W)

**Consumed by:** `9170081`–`9170084` · **Feeds:** `58171`

Counts: `Yes` 168 · `No` 108 · `Yes/No` 3 (→ `No`: pacted rows via the Law 1393 excess, others ⚠split) · `NA` 126 (not in the matrix).

**Section 1 — overrides (111 rows):**

| WTC row | Value | Wage type | Salary class |
|---|---|---|---|
| R123 | No | Long Term Disability | Non-Salary - non-remunerative |
| R134 | No | Bonus - profit sharing | Non-Salary - pacted |
| R135 | No | Bonus - profit sharing | Non-Salary - pacted |
| R136 | No | Bonus - profit sharing | Non-Salary - pacted |
| R137 | No | Bonus - profit sharing | Non-Salary - pacted |
| R138 | No | Bonus - profit sharing | Non-Salary - pacted |
| R139 | No | Bonus - profit sharing | Non-Salary - pacted |
| R140 | No | Bonus - profit sharing | Non-Salary - pacted |
| R141 | No | Bonus - profit sharing | Non-Salary - pacted |
| R142 | No | Bonus - profit sharing | Non-Salary - pacted |
| R143 | No | Bonus - profit sharing | Non-Salary - pacted |
| R144 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R145 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R146 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R147 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R148 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R149 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R150 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R151 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R152 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R153 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R156 | No | Annual leave payout | Paid Rest |
| R201 | No | Car allowance | Non-Salary - pacted |
| R202 | No | Arrears - Car allowance | Non-Salary - pacted |
| R203 | No | Adjustment - Car allowance | Non-Salary - pacted |
| R204 | No | Advance - Car allowance | Non-Salary - pacted |
| R205 | No | Car maintenance | Non-Salary - pacted |
| R206 | No | Car fuel | Non-Salary - pacted |
| R214 | No | Car Maintenance Allowance 2 | Non-Salary - pacted |
| R215 | No | Arrears - Car Maintenance Allowance 2 | Non-Salary - pacted |
| R216 | No | Adjustment - Car Maintenance Allowance 2 | Non-Salary - pacted |
| R217 | No | Relocation allowance | Non-Salary - non-remunerative |
| R218 | No | Arrears - Relocation allowance | Non-Salary - non-remunerative |
| R219 | No | Adjustment - Relocation allowance | Non-Salary - non-remunerative |
| R220 | No | Travel ticket allowance | Non-Salary - non-remunerative |
| R221 | No | Arrears - Travel ticket allowance | Non-Salary - non-remunerative |
| R222 | No | Adjustment - Travel ticket allowance | Non-Salary - non-remunerative |
| R223 | No | Relocation allowance | Non-Salary - non-remunerative |
| R224 | No | Arrears - Relocation allowance | Non-Salary - non-remunerative |
| R225 | No | Adjustment - Relocation allowance | Non-Salary - non-remunerative |
| R226 | No | Advance - Relocation allowance | Non-Salary - non-remunerative |
| R227 | No ⚠split | Per diem allowance | Conditional |
| R228 | No | Birth and Marriage Allowance | Non-Salary - non-remunerative |
| R229 | No | Birth and Marriage Allowance | Non-Salary - non-remunerative |
| R230 | No | COVID-19 Allowance | Non-Salary - pacted |
| R231 | No | Medical insurance / Medical Care | Non-Salary - pacted |
| R232 | No | Arrears - Medical insurance / Medical Care | Non-Salary - pacted |
| R233 | No | Adjustment - Medical insurance / Medical Care | Non-Salary - pacted |
| R234 | No | Medical insurance / Medical Care | Non-Salary - pacted |
| R235 | No | Medical insurance / Medical Care | Non-Salary - pacted |
| R236 | No | Medical insurance / Medical Care | Non-Salary - pacted |
| R237 | No | Medical insurance / Medical Care | Non-Salary - pacted |
| R253 | No | Benefits plan 1 | Non-Salary - pacted |
| R254 | No | Benefits plan 2 | Non-Salary - pacted |
| R255 | No | Education allowance | Non-Salary - pacted |
| R256 | No | Schooling allowance | Non-Salary - pacted |
| R257 | No | Arrears - Schooling allowance | Non-Salary - pacted |
| R258 | No | Education & Schooling allowance 2 | Non-Salary - pacted |
| R259 | No | Arrears - Education & Schooling allowance 2 | Non-Salary - pacted |
| R260 | No | Education & Schooling allowance 3 | Non-Salary - pacted |
| R261 | No | Education & Schooling allowance 4 | Non-Salary - pacted |
| R262 | No | Arrears - Education & Schooling allowance 4 | Non-Salary - pacted |
| R263 | No | Education & Schooling allowance 5 | Non-Salary - pacted |
| R264 | No | Arrears - Education & Schooling allowance 5 | Non-Salary - pacted |
| R265 | No | Family allowance (MLA, Children) | Non-Salary - non-remunerative |
| R266 | No | Adjustment - Family allowance (MLA, Children) | Non-Salary - non-remunerative |
| R267 | No | Recognition Award | Non-Salary - pacted |
| R277 | No | Post-termination payment | Non-Salary - non-remunerative |
| R278 | No | Post-termination payment | Non-Salary - non-remunerative |
| R279 | No | Post-termination payment | Non-Salary - non-remunerative |
| R280 | No | Post-termination payment | Non-Salary - non-remunerative |
| R281 | No | Stock options and grants | Non-Salary - pacted |
| R298 | No | Stock options and grants | Non-Salary - pacted |
| R299 | No | Stock options and grants | Non-Salary - pacted |
| R300 | No | Stock options and grants | Non-Salary - pacted |
| R301 | No | Stock options and grants | Non-Salary - pacted |
| R303 | No | All-inclusive salary | Salary |
| R316 | No | Extra-statutory bonus under a written non-salary pact | Non-Salary - pacted |
| R317 | No | Extra-statutory vacation bonus | Non-Salary - pacted |
| R318 | No | Occasional gratuity (mera liberalidad) | Non-Salary - non-remunerative |
| R324 | No | Vacation compensated in cash | Paid Rest |
| R325 | No | Work clothing and footwear | Non-Salary - non-remunerative |
| R326 | No | Sickness incapacity, days 1-2 (employer) | Non-Salary - non-remunerative |
| R327 | No | Sickness incapacity from day 3 (EPS) | Non-Salary - non-remunerative |
| R328 | No | Occupational accident or disease incapacity (ARL) | Non-Salary - non-remunerative |
| R329 | No | Sickness incapacity beyond day 180 (AFP / EPS) | Non-Salary - non-remunerative |
| R330 | No | Maternity leave (18 weeks) | Non-Salary - non-remunerative |
| R331 | No | Paternity leave (2 weeks) | Non-Salary - non-remunerative |
| R332 | No | Shared and flexible parental leave | Non-Salary - non-remunerative |
| R333 | No | Childcare leave (10 working days per year, EPS) | Non-Salary - non-remunerative |
| R338 | No ⚠split | Apprentice maintenance support | Conditional |
| R339 | No | Indemnity for dismissal without just cause | Non-Salary - non-remunerative |
| R340 | No | Late-payment penalty | Non-Salary - non-remunerative |
| R341 | No | Penalty for non-deposit of severance savings | Non-Salary - non-remunerative |
| R342 | No | Penalty for unpaid severance interest | Non-Salary - non-remunerative |
| R343 | No | Indemnity for early termination of a fixed-term or work-or-task contract | Non-Salary - non-remunerative |
| R344 | No | Indemnity for dismissal during protected status | Non-Salary - non-remunerative |
| R345 | No | Retirement or mutual-termination settlement bonus | Non-Salary - non-remunerative |
| R346 | No | Third-party meal payments | Non-Salary - non-remunerative |
| R347 | No | Voucher, card or non-cash instrument payment | Non-Salary - pacted |
| R348 | No | Employer-paid prepaid health / supplementary health plan | Non-Salary - pacted |
| R349 | No | Employer contribution to a voluntary pension fund | Non-Salary - pacted |
| R350 | No | Employer voluntary contribution to the individual pension account | Non-Salary - pacted |
| R351 | No | Equity and share-incentive awards | Non-Salary - pacted |
| R353 | No | Occasional per diem, and the transport / representation portion | Non-Salary - non-remunerative |
| R354 | No | Telework allowance | Non-Salary - non-remunerative |
| R355 | No | Tips | Non-Salary - non-remunerative |
| R356 | No | Cooperative associated-work compensation | Non-Salary - non-remunerative |
| R357 | No | Third-party payment (accrued) | Non-Salary - pacted |
| R358 | No ⚠split | Payroll advance (accrued) | Conditional |
| R359 | No | Reimbursement to the employee (accrued) | Non-Salary - non-remunerative |

**Section 2 — default `Yes` (168 rows):** every row not `NA` and not listed in Section 1. Row list (for configuration check):

```
R6, R37, R61, R62, R63, R64, R66, R67, R68, R69, R70, R71, R72, R73, R74
R75, R76, R77, R78, R79, R80, R81, R82, R83, R84, R85, R86, R87, R88, R89
R90, R91, R92, R93, R94, R95, R96, R97, R98, R99, R100, R101, R102, R103, R104
R105, R106, R107, R108, R109, R110, R111, R112, R113, R114, R115, R116, R117, R118, R119
R124, R125, R126, R127, R128, R129, R130, R131, R132, R133, R154, R155, R157, R158, R159
R160, R161, R162, R163, R164, R165, R166, R167, R168, R169, R170, R171, R172, R173, R174
R175, R176, R177, R178, R179, R180, R181, R182, R183, R184, R185, R186, R187, R188, R189
R190, R191, R192, R193, R194, R195, R196, R197, R198, R199, R200, R207, R208, R209, R210
R211, R212, R213, R238, R239, R240, R249, R250, R251, R252, R268, R269, R270, R271, R272
R273, R274, R275, R276, R287, R288, R289, R290, R291, R292, R293, R294, R295, R296, R297
R302, R304, R305, R306, R307, R308, R309, R310, R311, R312, R313, R314, R315, R319, R323
R334, R335, R352
```

## Matrix J — Vacation base (WTC column X)

**Consumed by:** `9170085`, `9170086` · **Feeds:** `58175`

Counts: `Yes` 119 · `No` 152 · `Yes/No` 3 (→ `No`: pacted rows via the Law 1393 excess, others ⚠split) · `NA` 131 (not in the matrix).

**Section 1 — overrides (155 rows):**

| WTC row | Value | Wage type | Salary class |
|---|---|---|---|
| R6 | No | Unpaid LOA - Basic salary deduction | Salary |
| R37 | No | Long Term Disability deduction | Salary |
| R68 | No | Overtime | Salary |
| R69 | No | Overtime | Salary |
| R70 | No | Overtime | Salary |
| R71 | No | Overtime | Salary |
| R72 | No | Overtime | Salary |
| R73 | No | Overtime | Salary |
| R74 | No | Overtime | Salary |
| R75 | No | Overtime | Salary |
| R76 | No | Overtime | Salary |
| R77 | No | Overtime | Salary |
| R78 | No | Overtime | Salary |
| R79 | No | Overtime | Salary |
| R80 | No | Overtime | Salary |
| R81 | No | Overtime | Salary |
| R82 | No | Overtime | Salary |
| R83 | No | Overtime | Salary |
| R84 | No | Overtime | Salary |
| R85 | No | Overtime | Salary |
| R86 | No | Overtime | Salary |
| R87 | No | Overtime | Salary |
| R88 | No | Overtime | Salary |
| R89 | No | Overtime | Salary |
| R90 | No | Overtime | Salary |
| R91 | No | Overtime | Salary |
| R92 | No | Overtime | Salary |
| R93 | No | Overtime | Salary |
| R94 | No | Overtime | Salary |
| R95 | No | Overtime | Salary |
| R96 | No | Overtime | Salary |
| R97 | No | Overtime | Salary |
| R123 | No | Long Term Disability | Non-Salary - non-remunerative |
| R134 | No | Bonus - profit sharing | Non-Salary - pacted |
| R135 | No | Bonus - profit sharing | Non-Salary - pacted |
| R136 | No | Bonus - profit sharing | Non-Salary - pacted |
| R137 | No | Bonus - profit sharing | Non-Salary - pacted |
| R138 | No | Bonus - profit sharing | Non-Salary - pacted |
| R139 | No | Bonus - profit sharing | Non-Salary - pacted |
| R140 | No | Bonus - profit sharing | Non-Salary - pacted |
| R141 | No | Bonus - profit sharing | Non-Salary - pacted |
| R142 | No | Bonus - profit sharing | Non-Salary - pacted |
| R143 | No | Bonus - profit sharing | Non-Salary - pacted |
| R144 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R145 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R146 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R147 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R148 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R149 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R150 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R151 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R152 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R153 | No | Bonuses - discretionary or one-time | Non-Salary - non-remunerative |
| R201 | No | Car allowance | Non-Salary - pacted |
| R202 | No | Arrears - Car allowance | Non-Salary - pacted |
| R203 | No | Adjustment - Car allowance | Non-Salary - pacted |
| R204 | No | Advance - Car allowance | Non-Salary - pacted |
| R205 | No | Car maintenance | Non-Salary - pacted |
| R206 | No | Car fuel | Non-Salary - pacted |
| R207 | No | Car & Transportation allowance | Non-Salary - non-remunerative |
| R208 | No | Arrears - Car & Transportation allowance | Non-Salary - non-remunerative |
| R209 | No | Adjustment - Car & Transportation allowance | Non-Salary - non-remunerative |
| R210 | No | Transportation allowance | Non-Salary - non-remunerative |
| R211 | No | Arrears - Transportation allowance | Non-Salary - non-remunerative |
| R212 | No | Adjustment - Transportation allowance | Non-Salary - non-remunerative |
| R213 | No | Advance - Transportation allowance | Non-Salary - non-remunerative |
| R214 | No | Car Maintenance Allowance 2 | Non-Salary - pacted |
| R215 | No | Arrears - Car Maintenance Allowance 2 | Non-Salary - pacted |
| R216 | No | Adjustment - Car Maintenance Allowance 2 | Non-Salary - pacted |
| R217 | No | Relocation allowance | Non-Salary - non-remunerative |
| R218 | No | Arrears - Relocation allowance | Non-Salary - non-remunerative |
| R219 | No | Adjustment - Relocation allowance | Non-Salary - non-remunerative |
| R220 | No | Travel ticket allowance | Non-Salary - non-remunerative |
| R221 | No | Arrears - Travel ticket allowance | Non-Salary - non-remunerative |
| R222 | No | Adjustment - Travel ticket allowance | Non-Salary - non-remunerative |
| R223 | No | Relocation allowance | Non-Salary - non-remunerative |
| R224 | No | Arrears - Relocation allowance | Non-Salary - non-remunerative |
| R225 | No | Adjustment - Relocation allowance | Non-Salary - non-remunerative |
| R226 | No | Advance - Relocation allowance | Non-Salary - non-remunerative |
| R227 | No ⚠split | Per diem allowance | Conditional |
| R228 | No | Birth and Marriage Allowance | Non-Salary - non-remunerative |
| R229 | No | Birth and Marriage Allowance | Non-Salary - non-remunerative |
| R230 | No | COVID-19 Allowance | Non-Salary - pacted |
| R231 | No | Medical insurance / Medical Care | Non-Salary - pacted |
| R232 | No | Arrears - Medical insurance / Medical Care | Non-Salary - pacted |
| R233 | No | Adjustment - Medical insurance / Medical Care | Non-Salary - pacted |
| R234 | No | Medical insurance / Medical Care | Non-Salary - pacted |
| R235 | No | Medical insurance / Medical Care | Non-Salary - pacted |
| R236 | No | Medical insurance / Medical Care | Non-Salary - pacted |
| R237 | No | Medical insurance / Medical Care | Non-Salary - pacted |
| R253 | No | Benefits plan 1 | Non-Salary - pacted |
| R254 | No | Benefits plan 2 | Non-Salary - pacted |
| R255 | No | Education allowance | Non-Salary - pacted |
| R256 | No | Schooling allowance | Non-Salary - pacted |
| R257 | No | Arrears - Schooling allowance | Non-Salary - pacted |
| R258 | No | Education & Schooling allowance 2 | Non-Salary - pacted |
| R259 | No | Arrears - Education & Schooling allowance 2 | Non-Salary - pacted |
| R260 | No | Education & Schooling allowance 3 | Non-Salary - pacted |
| R261 | No | Education & Schooling allowance 4 | Non-Salary - pacted |
| R262 | No | Arrears - Education & Schooling allowance 4 | Non-Salary - pacted |
| R263 | No | Education & Schooling allowance 5 | Non-Salary - pacted |
| R264 | No | Arrears - Education & Schooling allowance 5 | Non-Salary - pacted |
| R265 | No | Family allowance (MLA, Children) | Non-Salary - non-remunerative |
| R266 | No | Adjustment - Family allowance (MLA, Children) | Non-Salary - non-remunerative |
| R267 | No | Recognition Award | Non-Salary - pacted |
| R277 | No | Post-termination payment | Non-Salary - non-remunerative |
| R278 | No | Post-termination payment | Non-Salary - non-remunerative |
| R279 | No | Post-termination payment | Non-Salary - non-remunerative |
| R280 | No | Post-termination payment | Non-Salary - non-remunerative |
| R281 | No | Stock options and grants | Non-Salary - pacted |
| R298 | No | Stock options and grants | Non-Salary - pacted |
| R299 | No | Stock options and grants | Non-Salary - pacted |
| R300 | No | Stock options and grants | Non-Salary - pacted |
| R301 | No | Stock options and grants | Non-Salary - pacted |
| R304 | No | Statutory transport allowance | Non-Salary - non-remunerative |
| R305 | No | Connectivity allowance (teleworkers) | Non-Salary - non-remunerative |
| R306 | No | Day overtime (+25%) | Salary |
| R307 | No | Night overtime (+75%) | Salary |
| R309 | No | Obligatory rest-day / holiday premium (80% / 90%) | Salary |
| R310 | No | Day overtime on a rest day / holiday (+105% / +115%) | Salary |
| R311 | No | Night overtime on a rest day / holiday (+155% / +165%) | Salary |
| R312 | No | Night premium on a rest day / holiday (+115% / +125%) | Salary |
| R316 | No | Extra-statutory bonus under a written non-salary pact | Non-Salary - pacted |
| R317 | No | Extra-statutory vacation bonus | Non-Salary - pacted |
| R318 | No | Occasional gratuity (mera liberalidad) | Non-Salary - non-remunerative |
| R325 | No | Work clothing and footwear | Non-Salary - non-remunerative |
| R326 | No | Sickness incapacity, days 1-2 (employer) | Non-Salary - non-remunerative |
| R327 | No | Sickness incapacity from day 3 (EPS) | Non-Salary - non-remunerative |
| R328 | No | Occupational accident or disease incapacity (ARL) | Non-Salary - non-remunerative |
| R329 | No | Sickness incapacity beyond day 180 (AFP / EPS) | Non-Salary - non-remunerative |
| R330 | No | Maternity leave (18 weeks) | Non-Salary - non-remunerative |
| R331 | No | Paternity leave (2 weeks) | Non-Salary - non-remunerative |
| R332 | No | Shared and flexible parental leave | Non-Salary - non-remunerative |
| R333 | No | Childcare leave (10 working days per year, EPS) | Non-Salary - non-remunerative |
| R338 | No ⚠split | Apprentice maintenance support | Conditional |
| R339 | No | Indemnity for dismissal without just cause | Non-Salary - non-remunerative |
| R340 | No | Late-payment penalty | Non-Salary - non-remunerative |
| R341 | No | Penalty for non-deposit of severance savings | Non-Salary - non-remunerative |
| R342 | No | Penalty for unpaid severance interest | Non-Salary - non-remunerative |
| R343 | No | Indemnity for early termination of a fixed-term or work-or-task contract | Non-Salary - non-remunerative |
| R344 | No | Indemnity for dismissal during protected status | Non-Salary - non-remunerative |
| R345 | No | Retirement or mutual-termination settlement bonus | Non-Salary - non-remunerative |
| R346 | No | Third-party meal payments | Non-Salary - non-remunerative |
| R347 | No | Voucher, card or non-cash instrument payment | Non-Salary - pacted |
| R348 | No | Employer-paid prepaid health / supplementary health plan | Non-Salary - pacted |
| R349 | No | Employer contribution to a voluntary pension fund | Non-Salary - pacted |
| R350 | No | Employer voluntary contribution to the individual pension account | Non-Salary - pacted |
| R351 | No | Equity and share-incentive awards | Non-Salary - pacted |
| R353 | No | Occasional per diem, and the transport / representation portion | Non-Salary - non-remunerative |
| R354 | No | Telework allowance | Non-Salary - non-remunerative |
| R355 | No | Tips | Non-Salary - non-remunerative |
| R356 | No | Cooperative associated-work compensation | Non-Salary - non-remunerative |
| R357 | No | Third-party payment (accrued) | Non-Salary - pacted |
| R358 | No ⚠split | Payroll advance (accrued) | Conditional |
| R359 | No | Reimbursement to the employee (accrued) | Non-Salary - non-remunerative |

**Section 2 — default `Yes` (119 rows):** every row not `NA` and not listed in Section 1. Row list (for configuration check):

```
R61, R62, R63, R64, R66, R67, R98, R99, R100, R101, R102, R103, R104, R105, R106
R107, R108, R109, R110, R111, R112, R113, R114, R115, R116, R117, R118, R119, R124, R125
R126, R127, R128, R129, R130, R131, R132, R133, R157, R158, R159, R160, R161, R162, R163
R164, R165, R166, R167, R168, R169, R170, R171, R172, R173, R174, R175, R176, R177, R178
R179, R180, R181, R182, R183, R184, R185, R186, R187, R188, R189, R190, R191, R192, R193
R194, R195, R196, R197, R198, R199, R200, R238, R239, R240, R249, R250, R251, R252, R268
R269, R270, R271, R272, R273, R274, R275, R276, R287, R288, R289, R290, R291, R292, R293
R294, R295, R296, R297, R302, R303, R308, R313, R314, R315, R319, R334, R335, R352
```

## Matrix K — Salary class (WTC column V; CST arts. 127 / 128)

Counts: `Salary` 160 · `NA` 107 · `Non-Salary - non-remunerative` 80 · `Non-Salary - pacted` 53 · `Conditional` 3 · `Paid Rest` 2.

- **`Salary`** → `58101` salary payments of the month (the art. 114-1 test and the IBC start here).
- **`Non-Salary - pacted`** → `58102`, the numerator of the Law 1393 40% test.
- **`Non-Salary - non-remunerative`** → outside the IBC, the 40% numerator and the total (CE SU 25185/2021, rule 1).
- **`Paid Rest`** (vacation paid in cash) → outside the IBC (CE S4 exp. 26941 of 2024) but inside the levy base (Law 21 of 1982 art. 17).
- **`Conditional`** → configuration decides per client (⚠split).

| WTC row | Class | Wage type |
|---|---|---|
| R156 | Paid Rest | Annual leave payout |
| R227 | Conditional | Per diem allowance |
| R324 | Paid Rest | Vacation compensated in cash |
| R338 | Conditional | Apprentice maintenance support |
| R358 | Conditional | Payroll advance (accrued) |

---

## Consolidated register (all 298 active rows, all perimeters)

| WTC row | Wage type | Cat. | V class | N | O | P | Q | R | S | T | U | W | X |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R6 | Unpaid LOA - Basic salary deduction | Dedu | S | Y | Y | Y | Y/N | Y/N | N | Y/N | Y/N | Y | N |
| R37 | Long Term Disability deduction | Dedu | S | Y | Y | Y | Y/N | Y/N | N | N | N | Y | N |
| R61 | Basic salary | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R62 | Arrears - Basic salary | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R63 | Adjustment - Basic salary | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R64 | Advance - Basic salary | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R66 | Historic Pay | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R67 | Unpaid LOA - Basic salary | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R68 | Overtime | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | N |
| R69 | Overtime | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | N |
| R70 | Overtime | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | N |
| R71 | Overtime | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | N |
| R72 | Overtime | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | N |
| R73 | Overtime | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | N |
| R74 | Overtime | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | N |
| R75 | Overtime | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | N |
| R76 | Overtime | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | N |
| R77 | Overtime | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | N |
| R78 | Overtime | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | N |
| R79 | Overtime | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | N |
| R80 | Overtime | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | N |
| R81 | Overtime | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | N |
| R82 | Overtime | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | N |
| R83 | Overtime | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | N |
| R84 | Overtime | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | N |
| R85 | Overtime | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | N |
| R86 | Overtime | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | N |
| R87 | Overtime | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | N |
| R88 | Overtime | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | N |
| R89 | Overtime | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | N |
| R90 | Overtime | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | N |
| R91 | Overtime | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | N |
| R92 | Overtime | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | N |
| R93 | Overtime | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | N |
| R94 | Overtime | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | N |
| R95 | Overtime | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | N |
| R96 | Overtime | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | N |
| R97 | Overtime | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | N |
| R98 | Salary addition | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R99 | Arrears - Salary addition | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R100 | Adjustment - Salary addition | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R101 | Salary addition | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R102 | Salary addition | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R103 | Salary addition | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R104 | Salary addition | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R105 | Salary addition | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R106 | Salary addition | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R107 | Salary addition | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R108 | Premium pay (i.e. Shift premium) | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R109 | Premium pay (i.e. Shift premium) | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R110 | Premium pay (i.e. Shift premium) | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R111 | Premium pay (i.e. Shift premium) | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R112 | Premium pay (i.e. Shift premium) | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R113 | Premium pay (i.e. Shift premium) | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R114 | Holiday Allowance | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R115 | Arrears - Holiday Allowance | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R116 | Adjustment - Holiday Allowance | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R117 | On-call duty | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R118 | Arrears - On-call duty | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R119 | Adjustment - On-call duty | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R120 | Severance & Seniority | Earn | NS-n | Y/N | N | Y | N | N | N | N | N | NA | NA |
| R121 | Severance & Seniority | Earn | NS-n | Y/N | N | Y | N | N | N | N | N | NA | NA |
| R122 | Severance & Seniority | Earn | NS-n | Y/N | N | Y | N | N | N | N | N | NA | NA |
| R123 | Long Term Disability | Earn | NS-n | Y | Y | Y | Y | Y | N | N | Y | N | N |
| R124 | Bonus (annual, referral, etc) | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R125 | Bonus (annual, referral, etc) | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R126 | Bonus (annual, referral, etc) | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R127 | Bonus (annual, referral, etc) | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R128 | Bonus (annual, referral, etc) | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R129 | Bonus (annual, referral, etc) | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R130 | Bonus (annual, referral, etc) | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R131 | Bonus (annual, referral, etc) | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R132 | Bonus (annual, referral, etc) | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R133 | Bonus (annual, referral, etc) | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R134 | Bonus - profit sharing | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R135 | Bonus - profit sharing | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R136 | Bonus - profit sharing | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R137 | Bonus - profit sharing | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R138 | Bonus - profit sharing | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R139 | Bonus - profit sharing | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R140 | Bonus - profit sharing | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R141 | Bonus - profit sharing | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R142 | Bonus - profit sharing | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R143 | Bonus - profit sharing | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R144 | Bonuses - discretionary or one-time | Earn | NS-n | Y | Y | Y | N | N | N | N | N | N | N |
| R145 | Bonuses - discretionary or one-time | Earn | NS-n | Y | Y | Y | N | N | N | N | N | N | N |
| R146 | Bonuses - discretionary or one-time | Earn | NS-n | Y | Y | Y | N | N | N | N | N | N | N |
| R147 | Bonuses - discretionary or one-time | Earn | NS-n | Y | Y | Y | N | N | N | N | N | N | N |
| R148 | Bonuses - discretionary or one-time | Earn | NS-n | Y | Y | Y | N | N | N | N | N | N | N |
| R149 | Bonuses - discretionary or one-time | Earn | NS-n | Y | Y | Y | N | N | N | N | N | N | N |
| R150 | Bonuses - discretionary or one-time | Earn | NS-n | Y | Y | Y | N | N | N | N | N | N | N |
| R151 | Bonuses - discretionary or one-time | Earn | NS-n | Y | Y | Y | N | N | N | N | N | N | N |
| R152 | Bonuses - discretionary or one-time | Earn | NS-n | Y | Y | Y | N | N | N | N | N | N | N |
| R153 | Bonuses - discretionary or one-time | Earn | NS-n | Y | Y | Y | N | N | N | N | N | N | N |
| R154 | Annual leave pay | Earn | S | Y | Y | Y | Y | Y | N | Y | Y | Y | NA |
| R155 | Adjustment - Annual leave pay | Earn | S | Y | Y | Y | Y | Y | N | Y | Y | Y | NA |
| R156 | Annual leave payout | Earn | PR | Y | Y | Y | N | N | N | Y | N | N | NA |
| R157 | Expat allowance | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R158 | Arrears - Expat allowance | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R159 | Adjustment - Expat allowance | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R160 | Expat allowance | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R161 | Arrears - Expat allowance | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R162 | Adjustment - Expat allowance | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R163 | Expat allowance | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R164 | Arrears - Expat allowance | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R165 | Adjustment - Expat allowance | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R166 | Expat allowance | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R167 | Expat allowance | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R168 | Expat allowance | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R169 | Arrears - Expat allowance | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R170 | Adjustment - Expat allowance | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R171 | Expat allowance | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R172 | Arrears - Expat allowance | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R173 | Adjustment - Expat allowance | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R174 | Expat allowance | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R175 | Arrears - Expat allowance | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R176 | Adjustment - Expat allowance | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R177 | Housing allowance | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R178 | Arrears - Housing allowance | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R179 | Adjustment - Housing allowance | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R180 | Advance - Housing allowance | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R181 | Housing allowance 2 | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R182 | Arrears - Housing allowance 2 | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R183 | Adjustment - Housing allowance 2 | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R184 | Housing allowance 3 | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R185 | Arrears - Housing allowance 3 | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R186 | Adjustment - Housing allowance 3 | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R187 | Housing & Rent allowance 1 | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R188 | Arrears - Housing & Rent allowance 1 | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R189 | Adjustment - Housing & Rent allowance 1 | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R190 | Housing & Rent allowance 2 | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R191 | Arrears - Housing & Rent allowance 2 | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R192 | Housing & Rent allowance 3 | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R193 | Arrears - Housing & Rent allowance 3 | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R194 | Housing & Rent allowance 4 | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R195 | Housing & Rent allowance 5 | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R196 | Arrears - Housing & Rent allowance 5 | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R197 | Adjustment - Housing & Rent allowance 5 | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R198 | Housing & Rent allowance 6 | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R199 | Arrears - Housing & Rent allowance 6 | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R200 | Adjustment - Housing & Rent allowance 6 | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R201 | Car allowance | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R202 | Arrears - Car allowance | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R203 | Adjustment - Car allowance | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R204 | Advance - Car allowance | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R205 | Car maintenance | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R206 | Car fuel | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R207 | Car & Transportation allowance | Earn | NS-n | Y | Y | Y | N | N | N | N | N | Y | N |
| R208 | Arrears - Car & Transportation allowance | Earn | NS-n | Y | Y | Y | N | N | N | N | N | Y | N |
| R209 | Adjustment - Car & Transportation allowance | Earn | NS-n | Y | Y | Y | N | N | N | N | N | Y | N |
| R210 | Transportation allowance | Earn | NS-n | Y | Y | Y | N | N | N | N | N | Y | N |
| R211 | Arrears - Transportation allowance | Earn | NS-n | Y | Y | Y | N | N | N | N | N | Y | N |
| R212 | Adjustment - Transportation allowance | Earn | NS-n | Y | Y | Y | N | N | N | N | N | Y | N |
| R213 | Advance - Transportation allowance | Earn | NS-n | Y | Y | Y | N | N | N | N | N | Y | N |
| R214 | Car Maintenance Allowance 2 | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R215 | Arrears - Car Maintenance Allowance 2 | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R216 | Adjustment - Car Maintenance Allowance 2 | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R217 | Relocation allowance | Earn | NS-n | Y | Y | Y | N | N | N | N | N | N | N |
| R218 | Arrears - Relocation allowance | Earn | NS-n | N | N | N | N | N | N | N | N | N | N |
| R219 | Adjustment - Relocation allowance | Earn | NS-n | N | N | N | N | N | N | N | N | N | N |
| R220 | Travel ticket allowance | Earn | NS-n | N | N | N | N | N | N | N | N | N | N |
| R221 | Arrears - Travel ticket allowance | Earn | NS-n | N | N | N | N | N | N | N | N | N | N |
| R222 | Adjustment - Travel ticket allowance | Earn | NS-n | N | N | N | N | N | N | N | N | N | N |
| R223 | Relocation allowance | Earn | NS-n | N | N | N | N | N | N | N | N | N | N |
| R224 | Arrears - Relocation allowance | Earn | NS-n | N | N | N | N | N | N | N | N | N | N |
| R225 | Adjustment - Relocation allowance | Earn | NS-n | N | N | N | N | N | N | N | N | N | N |
| R226 | Advance - Relocation allowance | Earn | NS-n | Y | Y | Y | N | N | N | N | N | N | N |
| R227 | Per diem allowance | Earn | C | Y | Y | Y | Y/N | Y/N | Y/N | Y/N | Y/N | Y/N | Y/N |
| R228 | Birth and Marriage Allowance | Earn | NS-n | Y | Y | Y | N | N | N | N | N | N | N |
| R229 | Birth and Marriage Allowance | Earn | NS-n | Y | Y | Y | N | N | N | N | N | N | N |
| R230 | COVID-19 Allowance | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R231 | Medical insurance / Medical Care | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R232 | Arrears - Medical insurance / Medical Care | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R233 | Adjustment - Medical insurance / Medical Care | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R234 | Medical insurance / Medical Care | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R235 | Medical insurance / Medical Care | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R236 | Medical insurance / Medical Care | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R237 | Medical insurance / Medical Care | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R238 | Personal Allowance 2 | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R239 | Arrears - Personal Allowance 2 | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R240 | Adjustment - Personal Allowance 2 | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R241 | Pensions & Pension Refunds | Earn | NS-n | Y/N | Y/N | Y | NA | NA | NA | NA | NA | NA | NA |
| R242 | Pensions & Pension Refunds | Earn | NS-n | Y/N | Y/N | Y | NA | NA | NA | NA | NA | NA | NA |
| R243 | Pensions & Pension Refunds | Earn | NS-n | Y/N | Y/N | Y | NA | NA | NA | NA | NA | NA | NA |
| R244 | Pensions & Pension Refunds | Earn | NS-n | Y/N | Y/N | Y | NA | NA | NA | NA | NA | NA | NA |
| R245 | Pensions & Pension Refunds | Earn | NS-n | Y/N | Y/N | Y | NA | NA | NA | NA | NA | NA | NA |
| R246 | Pensions & Pension Refunds | Earn | NS-n | Y/N | Y/N | Y | NA | NA | NA | NA | NA | NA | NA |
| R247 | Pensions & Pension Refunds | Earn | NS-n | Y/N | Y/N | Y | NA | NA | NA | NA | NA | NA | NA |
| R248 | Pensions & Pension Refunds | Earn | NS-n | Y/N | Y/N | Y | NA | NA | NA | NA | NA | NA | NA |
| R249 | Social raise / Social allowance | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R250 | Personal Allowance 1 | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R251 | Arrears - Personal Allowance 1 | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R252 | Adjustment - Personal Allowance 1 | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R253 | Benefits plan 1 | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R254 | Benefits plan 2 | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R255 | Education allowance | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R256 | Schooling allowance | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R257 | Arrears - Schooling allowance | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R258 | Education & Schooling allowance 2 | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R259 | Arrears - Education & Schooling allowance 2 | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R260 | Education & Schooling allowance 3 | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R261 | Education & Schooling allowance 4 | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R262 | Arrears - Education & Schooling allowance 4 | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R263 | Education & Schooling allowance 5 | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R264 | Arrears - Education & Schooling allowance 5 | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R265 | Family allowance (MLA, Children) | Earn | NS-n | N | N | N | N | N | N | N | N | N | N |
| R266 | Adjustment - Family allowance (MLA, Children) | Earn | NS-n | N | N | N | N | N | N | N | N | N | N |
| R267 | Recognition Award | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R268 | Special allowance | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R269 | Special allowance | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R270 | Special allowance | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R271 | Special allowance | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R272 | Special allowance | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R273 | Special allowance | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R274 | Special allowance | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R275 | Special allowance | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R276 | Special allowance | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R277 | Post-termination payment | Earn | NS-n | Y | Y | Y | N | N | N | N | N | N | N |
| R278 | Post-termination payment | Earn | NS-n | Y | Y | Y | N | N | N | N | N | N | N |
| R279 | Post-termination payment | Earn | NS-n | Y | Y | Y | N | N | N | N | N | N | N |
| R280 | Post-termination payment | Earn | NS-n | Y | Y | Y | N | N | N | N | N | N | N |
| R281 | Stock options and grants | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R282 | Statutory Gratuity, EOS | Earn | NS-n | Y/N | N | Y | N | N | N | N | N | NA | NA |
| R283 | Supplemental basic (i.e. 13th or 14th months salary) | Earn | NS-n | Y | Y | Y | N | N | N | N | N | NA | NA |
| R284 | Gratuity, EOS, Post-termination, etc. | Earn | NS-n | Y/N | N | Y | N | N | N | N | N | NA | NA |
| R285 | Gratuity, EOS, Post-termination, etc. | Earn | NS-n | Y/N | N | Y | N | N | N | N | N | NA | NA |
| R286 | Gratuity, EOS, Post-termination, etc. | Earn | NS-n | Y/N | N | Y | N | N | N | N | N | NA | NA |
| R287 | Salary addition | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R288 | Salary addition | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R289 | Salary addition | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R290 | Salary addition | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R291 | Salary addition | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R292 | Salary addition | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R293 | Salary addition | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R294 | Salary addition | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R295 | Salary addition | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R296 | Salary addition | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R297 | Salary addition | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R298 | Stock options and grants | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R299 | Stock options and grants | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R300 | Stock options and grants | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R301 | Stock options and grants | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R302 | Basic salary | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R303 | All-inclusive salary | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | N | Y |
| R304 | Statutory transport allowance | Earn | NS-n | Y | Y | Y | N | N | N | N | N | Y | N |
| R305 | Connectivity allowance (teleworkers) | Earn | NS-n | Y | Y | Y | N | N | N | N | N | Y | N |
| R306 | Day overtime (+25%) | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | N |
| R307 | Night overtime (+75%) | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | N |
| R308 | Night premium (35%) | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R309 | Obligatory rest-day / holiday premium (80% / 90%) | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | N |
| R310 | Day overtime on a rest day / holiday (+105% / +115%) | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | N |
| R311 | Night overtime on a rest day / holiday (+155% / +165%) | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | N |
| R312 | Night premium on a rest day / holiday (+115% / +125%) | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | N |
| R313 | Paid weekly rest day and paid public holidays | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R314 | Commissions and sales percentages | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R315 | Habitual bonus (salary) | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R316 | Extra-statutory bonus under a written non-salary pact | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R317 | Extra-statutory vacation bonus | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R318 | Occasional gratuity (mera liberalidad) | Earn | NS-n | Y | Y | Y | N | N | N | N | N | N | N |
| R319 | Salary in kind | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R320 | Statutory service bonus | Earn | NS-n | Y | Y | Y | N | N | N | N | N | NA | NA |
| R321 | Severance savings | Earn | NS-n | Y/N | N | Y | N | N | N | N | N | NA | NA |
| R322 | Interest on severance savings | Earn | NS-n | Y/N | N | Y | N | N | N | N | N | NA | NA |
| R323 | Annual leave taken | Earn | S | Y | Y | Y | Y | Y | N | Y | Y | Y | NA |
| R324 | Vacation compensated in cash | Earn | PR | Y | Y | Y | N | N | N | Y | N | N | NA |
| R325 | Work clothing and footwear | Earn | NS-n | N | N | N | N | N | N | N | N | N | N |
| R326 | Sickness incapacity, days 1-2 (employer) | Earn | NS-n | Y | Y | Y | Y | Y | N | N | Y | N | N |
| R327 | Sickness incapacity from day 3 (EPS) | Earn | NS-n | Y | Y | Y | Y | Y | N | N | Y | N | N |
| R328 | Occupational accident or disease incapacity (ARL) | Earn | NS-n | Y | Y | Y | Y | Y | N | N | Y | N | N |
| R329 | Sickness incapacity beyond day 180 (AFP / EPS) | Earn | NS-n | Y | Y | Y | Y | Y | N | N | Y | N | N |
| R330 | Maternity leave (18 weeks) | Earn | NS-n | Y | Y | Y | Y | Y | N | N | Y | N | N |
| R331 | Paternity leave (2 weeks) | Earn | NS-n | Y | Y | Y | Y | Y | N | N | Y | N | N |
| R332 | Shared and flexible parental leave | Earn | NS-n | Y | Y | Y | Y | Y | N | N | Y | N | N |
| R333 | Childcare leave (10 working days per year, EPS) | Earn | NS-n | Y | Y | Y | Y | Y | N | N | Y | N | N |
| R334 | Statutory paid leave (CST art. 57 num. 6) | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R335 | Bereavement leave (5 working days) | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R338 | Apprentice maintenance support | Earn | C | Y | Y | Y | Y | Y/N | Y | Y/N | Y/N | Y/N | Y/N |
| R339 | Indemnity for dismissal without just cause | Earn | NS-n | Y | Y | Y | N | N | N | N | N | N | N |
| R340 | Late-payment penalty | Earn | NS-n | Y | Y | Y | N | N | N | N | N | N | N |
| R341 | Penalty for non-deposit of severance savings | Earn | NS-n | Y | Y | Y | N | N | N | N | N | N | N |
| R342 | Penalty for unpaid severance interest | Earn | NS-n | Y | Y | Y | N | N | N | N | N | N | N |
| R343 | Indemnity for early termination of a fixed-term or work-or-task contract | Earn | NS-n | Y | Y | Y | N | N | N | N | N | N | N |
| R344 | Indemnity for dismissal during protected status | Earn | NS-n | Y | Y | Y | N | N | N | N | N | N | N |
| R345 | Retirement or mutual-termination settlement bonus | Earn | NS-n | Y | Y | Y | N | N | N | N | N | N | N |
| R346 | Third-party meal payments | Earn | NS-n | Y/N | Y/N | Y/N | N | N | N | N | N | N | N |
| R347 | Voucher, card or non-cash instrument payment | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R348 | Employer-paid prepaid health / supplementary health plan | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R349 | Employer contribution to a voluntary pension fund | Earn | NS-p | Y/N | Y/N | N | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R350 | Employer voluntary contribution to the individual pension account | Earn | NS-p | Y/N | Y/N | N | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R351 | Equity and share-incentive awards | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R352 | Permanent per diem - board and lodging portion (salary) | Earn | S | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| R353 | Occasional per diem, and the transport / representation portion | Earn | NS-n | Y/N | Y/N | N | N | N | N | N | N | N | N |
| R354 | Telework allowance | Earn | NS-n | Y | Y | Y | N | N | N | N | N | N | N |
| R355 | Tips | Earn | NS-n | N | N | N | N | N | N | N | N | N | N |
| R356 | Cooperative associated-work compensation | Earn | NS-n | Y | Y | Y | N | N | N | N | N | N | N |
| R357 | Third-party payment (accrued) | Earn | NS-p | Y | Y | Y | Y/N | Y/N | Y/N | N | Y/N | N | N |
| R358 | Payroll advance (accrued) | Earn | C | Y/N | Y/N | Y/N | Y/N | Y/N | Y/N | Y/N | Y/N | Y/N | Y/N |
| R359 | Reimbursement to the employee (accrued) | Earn | NS-n | N | N | N | N | N | N | N | N | N | N |

Legend: Y = Yes, N = No, Y/N = Yes/No (→ `No` ⚠split in the matrix), NA = not applicable. V class: S Salary, NS-p Non-Salary pacted, NS-n Non-Salary non-remunerative, PR Paid Rest, C Conditional.

**Source file:** CO-WTC-001 v1.7, md5 `d83d0e3c75b908f3e9d2e710b2c3eec2`.
