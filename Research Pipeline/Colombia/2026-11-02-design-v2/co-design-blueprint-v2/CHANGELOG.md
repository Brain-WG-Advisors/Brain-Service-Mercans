# CHANGELOG — Colombia design v1.2 → v2.0 (2 November 2026)

Basis: v1.2 of 2 November 2026 (57 regulations, prose and formulas) → v2.0 (machine-readable `co_design_v2.json`, executed). Basis documents: CCG v1.7, WTC v1.9, DD v1.6, SIR v1.4.

## Defects of v1.2 found by executing it (v1.2-faithful variant, same engine)

1. **Order** — 47 reads of an account before the regulation that posts it (e.g. the IBC `9170021` read vacation, illness and maternity amounts posted at ordinals 85–94; gross `9170015` read the service bonus posted at 82; the indemnity withholding `9170064` read the indemnity posted at 91; total contributions read the type-51 amounts posted at 97). Fixed: every earning / payment runs before the bases.
2. **Transport allowance counted twice in the statutory-benefit base** — v1.2 `58171` = matrix I (which contains the transport-allowance row, WTC W304 = Yes) + 52503 by formula. Service bonus and severance savings 12% too high for salaries ≤ 2 SMMLV (P01: 1,749,095 instead of 1,624,548). Fixed: the allowance enters only through its WTC row.
3. **Non-resident base** — v1.2 used the column-N base `58150`; the WTC has its own column P, which differs on 15 rows (pensions R241–R248, end-of-service gratuities R282, R284–R286 are P = Yes; employer voluntary pension R349–R350 and occasional per diem R353 are P = No). Fixed: `9170132` reads column P.
4. **Service bonus and indemnities in the monthly table read** — v1.2 matrix A (column N) included R320 and R339 although the design reads them separately (Decree 1625 art. 1.2.4.1.3 Procedure 1; Tax Code art. 401-3). Fixed: false in `9170072` (with R340 and the retirement bonus R345), read by `9170089`–`9170093`; under Procedure 2 the service bonus enters the monthly base through `9170073`.
5. **Indemnity withholding base** — only the art. 64 indemnity; Tax Code art. 401-3 covers "las indemnizaciones derivadas de una relación laboral". Fixed: R339, R343, R344.
6. **Illness floor** — v1.2 stated "no validation case triggers it"; the floor of C-543 of 2007 binds on days 91–180 for salaries below 2 SMMLV (half the daily salary < SMMLV / 30). The v1.2 formula already had the floor; its check text (I03 days 91–100 = 500,000) was wrong: 583,635.
7. **Rule groups** — the 17 income-tax regulations of v1.2 were `retro_simple_tax*`; v2.0 uses `simple_tax*` (no retro_), as the development team's draft 9170132, because Procedure 1 applies the table to the payments made in the month (Decree 1625 art. 1.2.4.1.3).

## Changes after the independent review

- Procedure 2: the service bonus is folded into the monthly base (`9170073`; Decree 1625 art. 1.2.4.1.3, Procedure 2: "la totalidad de tales pagos gravables"; CCG v1.7 Module 6). Check X12: 1,057,500.
- Retirement bonus R345: out of the monthly read, withheld by Decree 1625 art. 1.2.4.1.8 (`9170090`; "bonificaciones por retiro definitivo del trabajador"; the 20% of Tax Code art. 401-3 is for indemnities). Check X13.
- Termination average: divided by the months of service when fewer than 12 (`9170088`, input `58259`; Decree 1625 art. 1.2.4.1.8 lit. a). Check X14: 194,649.
- Contributions: one regulation per fund with an employee band (`employeeRate`) and an employer band (`employerRate` / `employerRateAccount`), as the development team codes them; the employer band is written from the base and reads no other band. Check that a band coded on the wrong side is caught.
- Projection for periods shorter than 30 days: Procedure 1 only (`9170074`). Check X15: 341,250.
- Late-payment indemnity R340 (Labour Code art. 65, "como indemnización") withheld with the indemnities of Tax Code art. 401-3; 204-UVT test on the monthly salary, as the CCG v1.7 worked example (Module 9). Check X16.
- Non-resident flat tax reads `$64552`, the account of the development team's draft; JSON keys `regulationId` and `systemTaxYearIds`.
- Rounding: each contributor and fund rounded once, up to the next COP 100 (Decree 780 art. 3.2.1.5 num. 2; AT2 v30 field 47); employee share = statutory rate to the peso, employer share = rounded fund total - employee share; non-taxable income = contributions withheld (Tax Code arts. 55, 56). Check X17.
- Gross and net in cash: severance savings deposited to the fund out of the gross (added when paid on termination), deduction wage types negative; net pay less salary in kind and voluntary pension / AFC / RAIS deductions. Checks X18–X20.
- Column-O (table read) check added; memo and matrices texts aligned; apprentice practical phase listed in the research gaps.

## Regulation by regulation

| v1.2 | v2.0 ID (ordinal) | Name | Change |
|---|---|---|---|
| 9170010 (10) | 9170009 (9) | CO All-inclusive Salary for the Period | split out of v1.2 9170010: the all-inclusive salary is posted to its own WTC row R303 (column W = No) |
| 9170010 (10) | 9170010 (10) | CO Basic Salary for the Period | same rule |
| 9170096 (96) | 9170011 (11) | CO Apprentice Maintenance Support | moved before the bases (defect 1) |
| 9170012 (12) | 9170012 (12) | CO Overtime and Premium Hours | same rule |
| 9170013 (13) | 9170013 (13) | CO Transport Allowance | same rule |
| 9170085 (85) | 9170014 (14) | CO Vacation Base | moved before the bases (defect 1) |
| 9170085 (85) | 9170015 (15) | CO Vacation Daily Value | moved before the bases (defect 1); information |
| 9170085 (85) | 9170016 (16) | CO Vacation Taken | moved before the bases (defect 1) |
| 9170085 (85) | 9170017 (17) | CO Vacation Compensated in Cash | moved before the bases (defect 1) |
| 9170085 (85) | 9170018 (18) | CO Vacation Compensation Above Half (block flag) | moved before the bases (defect 1); block written as a flag (v1.2: "must be blocked") |
| 9170086 (86) | 9170019 (19) | CO Vacation Paid on Termination | moved before the bases (defect 1) |
| 9170081 (81) | 9170020 (20) | CO Statutory-Benefit Base | moved before the bases (defect 1); transport allowance only through its WTC row (defect 2) |
| 9170082 (82) | 9170021 (21) | CO Service Bonus | moved before the bases (defect 1) |
| 9170083 (83) | 9170022 (22) | CO Severance Savings | moved before the bases (defect 1) |
| 9170084 (84) | 9170023 (23) | CO Interest on Severance Savings | moved before the bases (defect 1) |
| 9170093 (93) | 9170024 (24) | CO Illness Benefit Days 1-2 (employer) | moved before the bases (defect 1) |
| 9170093 (93) | 9170025 (25) | CO Illness Benefit Days 3-90 (health insurer) | moved before the bases (defect 1) |
| 9170093 (93) | 9170026 (26) | CO Illness Benefit Days 91-180 (health insurer) | moved before the bases (defect 1); split into segments; floor binds (defect 6) |
| 9170093 (93) | 9170027 (27) | CO Illness Benefit Total | moved before the bases (defect 1); information |
| 9170093 (93) | 9170028 (28) | CO Contribution Base of the Illness Days | moved before the bases (defect 1); information |
| 9170094 (94) | 9170029 (29) | CO Maternity Leave Pay | moved before the bases (defect 1) |
| 9170094 (94) | 9170030 (30) | CO Contribution Base of the Maternity Leave | moved before the bases (defect 1); information |
| 9170091 (91) | 9170031 (31) | CO Art. 64 Indemnity Days | moved before the bases (defect 1) |
| 9170091 (91) | 9170032 (32) | CO Art. 64 Indemnity | moved before the bases (defect 1) |
| 9170015 (15) | 9170039 (39) | CO Severance Savings Paid on Termination | new: severance savings paid on termination in the gross |
| 9170015 (15) | 9170040 (40) | CO Gross Earnings | deposited severance savings out; deductions negative |
| 9170016 (16) | 9170041 (41) | CO Salary Payments of the Month | same rule; renumbered (order rule; ID = 9170000 + ordinal) |
| 9170017 (17) | 9170042 (42) | CO Pacted Non-Salary Payments | same rule; renumbered (order rule; ID = 9170000 + ordinal) |
| 9170018 (18) | 9170043 (43) | CO Total Remuneration (Law 1393 test) | same rule; renumbered (order rule; ID = 9170000 + ordinal) |
| 9170019 (19) | 9170044 (44) | CO Law 1393 Excess | same rule; renumbered (order rule; ID = 9170000 + ordinal) |
| 9170021 (21) | 9170045 (45) | CO Contribution Base (IBC) - Health | same rule; renumbered (order rule; ID = 9170000 + ordinal) |
| 9170022 (22) | 9170046 (46) | CO IBC in Minimum Wages | same rule; renumbered (order rule; ID = 9170000 + ordinal) |
| 9170023 (23) | 9170047 (47) | CO Payroll-Levy Base | same rule; renumbered (order rule; ID = 9170000 + ordinal) |
| 9170025 (25) | 9170048 (48) | CO Art. 114-1 Exoneration Test | same rule; renumbered (order rule; ID = 9170000 + ordinal) |
| 9170026 (26) | 9170049 (49) | CO IBC - Pension | same rule; renumbered (order rule; ID = 9170000 + ordinal) |
| 9170027 (27) | 9170050 (50) | CO IBC - Solidarity Fund | same rule; renumbered (order rule; ID = 9170000 + ordinal) |
| 9170028 (28) | 9170051 (51) | CO IBC - Occupational Risk | same rule; renumbered (order rule; ID = 9170000 + ordinal) |
| 9170097 (97) | 9170052 (52) | CO Contributor Type 51 Bases | same rule; renumbered (order rule; ID = 9170000 + ordinal) |
| 9170034 (34) | 9170053 (53) | CO Solidarity Fund Subsistence Rate | rate as an account (band rate), so the contribution keeps its raw value |
| 9170032 (32) | 9170054 (54) | CO Employer Pension Rate | rate as an account |
| 9170043 (43) | 9170055 (55) | CO Occupational-Risk Rate | rate as an account |
| 9170031 (31) | 9170056 (56) | CO Health Contribution (EE and ER) | employee and employer bands in one regulation; one rounding per contributor and fund |
| 9170032 (32) | 9170057 (57) | CO Pension Contribution (EE and ER) | employee and employer bands in one regulation; one rounding per contributor and fund |
| 9170033 (33) | 9170058 (58) | CO Solidarity Fund - Solidarity (EE) | same rule; renumbered (order rule; ID = 9170000 + ordinal) |
| 9170034 (34) | 9170059 (59) | CO Solidarity Fund - Subsistence (EE) | same rule; renumbered (order rule; ID = 9170000 + ordinal) |
| 9170043 (43) | 9170060 (60) | CO Occupational Risk (ER) | same rule; renumbered (order rule; ID = 9170000 + ordinal) |
| 9170044 (44) | 9170061 (61) | CO Family Compensation Fund (ER) 4% | same rule; renumbered (order rule; ID = 9170000 + ordinal) |
| 9170045 (45) | 9170062 (62) | CO SENA (ER) 2% | same rule; renumbered (order rule; ID = 9170000 + ordinal) |
| 9170046 (46) | 9170063 (63) | CO ICBF (ER) 3% | same rule; renumbered (order rule; ID = 9170000 + ordinal) |
| 9170097 (97) | 9170064 (64) | CO Contributor Type 51 Pension (EE and ER) | employee and employer bands; total rounded once |
| 9170097 (97) | 9170065 (65) | CO Contributor Type 51 Occupational Risk (ER) | same rule; renumbered (order rule; ID = 9170000 + ordinal) |
| 9170097 (97) | 9170066 (66) | CO Contributor Type 51 Family Compensation Fund (ER) | same rule; renumbered (order rule; ID = 9170000 + ordinal) |
| 9170039 (39) | 9170067 (67) | CO Total Employee Contributions | same rule; renumbered (order rule; ID = 9170000 + ordinal) |
| 9170049 (49) | 9170068 (68) | CO Total Employer Contributions and Levies | same rule; renumbered (order rule; ID = 9170000 + ordinal) |
| 9170051 (51) | 9170072 (72) | CO Taxable Labour Payments (monthly read) | R320, R339, R340, R343, R344, R345 false (defect 4); rule group retro_ -> simple_tax (item 7) |
| — | 9170073 (73) | CO Service Bonus in the Procedure 2 Base | new: service bonus in the Procedure 2 base |
| — | 9170074 (74) | CO Projection Factor for Periods Shorter than 30 Days | new: Decree 1625 art. 1.2.4.1.3 lits. a-b option, off by default; Procedure 1 only |
| 9170052 (52) | 9170075 (75) | CO Non-taxable Income (contributions and voluntary RAIS) | contributions withheld, not before rounding; rule group retro_ -> simple_tax (item 7) |
| 9170053 (53) | 9170076 (76) | CO Net Income | same rule; renumbered (order rule; ID = 9170000 + ordinal); rule group retro_ -> simple_tax (item 7) |
| 9170054 (54) | 9170077 (77) | CO Dependants Deduction | same rule; renumbered (order rule; ID = 9170000 + ordinal); rule group retro_ -> simple_tax (item 7) |
| 9170055 (55) | 9170078 (78) | CO Prepaid Health Deduction | same rule; renumbered (order rule; ID = 9170000 + ordinal); rule group retro_ -> simple_tax (item 7) |
| 9170056 (56) | 9170079 (79) | CO Mortgage Interest Deduction | same rule; renumbered (order rule; ID = 9170000 + ordinal); rule group retro_ -> simple_tax (item 7) |
| 9170057 (57) | 9170080 (80) | CO Voluntary Pension / AFC Exempt | same rule; renumbered (order rule; ID = 9170000 + ordinal); rule group retro_ -> simple_tax (item 7) |
| 9170058 (58) | 9170081 (81) | CO 25% Exempt Labour Income (computed last) | same rule; renumbered (order rule; ID = 9170000 + ordinal); rule group retro_ -> simple_tax (item 7) |
| 9170059 (59) | 9170082 (82) | CO 40% / 1,340 UVT Cap | same rule; renumbered (order rule; ID = 9170000 + ordinal); rule group retro_ -> simple_tax (item 7) |
| 9170059 (59) | 9170083 (83) | CO Reliefs Applied within the Cap | same rule; renumbered (order rule; ID = 9170000 + ordinal); rule group retro_ -> simple_tax (item 7) |
| 9170060 (60) | 9170084 (84) | CO Taxable Base | same rule; renumbered (order rule; ID = 9170000 + ordinal); rule group retro_ -> simple_tax (item 7) |
| 9170061 (61) | 9170085 (85) | CO Procedure 1 Tax before Rounding | raw tax kept (÷ projection factor); rounding in the next regulation; rule group retro_ -> simple_tax (item 7) |
| 9170061 (61) | 9170086 (86) | CO Withholding - Procedure 1 | same rule; renumbered (order rule; ID = 9170000 + ordinal); rule group retro_ -> simple_tax (item 7) |
| 9170062 (62) | 9170087 (87) | CO Withholding - Procedure 2 | service bonus in the base; no projection; rule group retro_ -> simple_tax (item 7) |
| 9170064 (64) | 9170088 (88) | CO Termination Withholding Percentage (12-month average) | average by the months of service when fewer than 12; rule group retro_ -> simple_tax (item 7) |
| 9170064 (64) | 9170089 (89) | CO Withholding - Indemnities | base R339 + R340 + R343 + R344 (defect 5); 204-UVT test on the monthly salary; rule group retro_ -> simple_tax (item 7) |
| — | 9170090 (90) | CO Withholding - Retirement Bonus | new: retirement bonus by Decree 1625 art. 1.2.4.1.8 |
| 9170065 (65) | 9170091 (91) | CO Service Bonus Exempt 25% | new split of the separate read: 25% within the annual 790 UVT left after the salary read; rule group retro_ -> simple_tax (item 7) |
| 9170065 (65) | 9170092 (92) | CO Service Bonus Reliefs within the Cap | new split of the separate read; rule group retro_ -> simple_tax (item 7) |
| 9170065 (65) | 9170093 (93) | CO Withholding - Service Bonus (Procedure 1) | same rule; renumbered (order rule; ID = 9170000 + ordinal); rule group retro_ -> simple_tax (item 7) |
| 9170063 (63) | 9170132 (132) | CO Income Tax Flat | ID, name, ordinal, rule group and assertion `EQUALS($64552;2)` of the development team's draft; base column P (defect 3); rule group retro_ -> simple_tax (item 7) |
| 9170069 (69) | 9170139 (139) | CO Total Withholding | same rule; renumbered (order rule; ID = 9170000 + ordinal); rule group retro_ -> simple_tax (item 7) |
| 9170071 (71) | 9170141 (141) | CO Net Pay | less salary in kind and voluntary pension / AFC / RAIS deductions; rule group retro_ -> simple_tax (item 7) |

Basis texts of the 2 November 2026 issue reflected: Constitutional Court C-397 of 1994 and DIAN Concepto 577 of 2020 (severance savings of non-residents); Decree 1469 of 2025 with Decree 0159 of 2026 left without effect (SMMLV); C-543 of 2007 (illness floor); incapacity and leave outside SENA / ICBF / CCF (WTC column T; Consejo de Estado exp. 23856 of 2021; Superintendencia del Subsidio Familiar Concepto 2-2018-083606); payment method 46 (report side).
