# CO-DIAN-002 (Formulario 350) - round-3 reconciliation of the September 2026 withholding (17 Oct 2026)

Question: do the gross-to-net files of all payroll runs, the monthly Base of Withholding and the weekly Base of Withholding cover the whole withholding of September 2026, and does the rule "casilla 93 sums every run of the month" hold against the Accumulated Report?

## Files used (masked)
| Run | File | Pay group | Employees |
|---|---|---|---|
| REF-P201-090 (monthly) | round3 [[Research Pipeline/Colombia/co-report-crosscheck/03-client-reports-masked/round3/Gross to net PMI 2026-09-01-2026-09-30 - Monthly (1) - 16oct.xlsx\|Gross to net PMI 2026-09-01-2026-09-30 - Monthly (1) - 16oct.xlsx]] (content-identical to the round-2 Monthly file except 6 stray cells below the table in column U, absent in the new copy) | CO - Monthly | 261 |
| REF-P201-065 (monthly withholding working report) | round3 `...Base of Withholding ... (1) - 16oct.xlsx` (cell-identical to the round-1 file) | monthly | 261 |
| REF-P201-216 (weekly) | round3 `...Base of Withholding ... - Weekly (1) - 16oct.xlsx` | weekly | 132 (93 with withholding > 0) |
| REF-P201-184 (pensioners) | round3 [[Research Pipeline/Colombia/co-report-crosscheck/03-client-reports-masked/round3/Gross to net PMI 2026-09-01-2026-09-30 - 16oct.xlsx\|Gross to net PMI 2026-09-01-2026-09-30 - 16oct.xlsx]] | CO - Pensionaries | 454 |
| REF-P203-119 (October termination run) | round3 [[Research Pipeline/Colombia/co-report-crosscheck/03-client-reports-masked/round3/Gross to net PMI 2026-10-01-2026-10-31 - 16oct.xlsx\|Gross to net PMI 2026-10-01-2026-10-31 - 16oct.xlsx]] | CO - Monthly | 2 |
| Year-to-date accumulations | round1 [[Research Pipeline/Colombia/co-report-crosscheck/03-client-reports-masked/Accumulated Report.xlsx\|Accumulated Report.xlsx]], column 01/09/2026 | all | 1,038 ids |

The three populations (monthly 261, weekly 132, pensioners 454) do not overlap.

## Totals, September 2026 (COP)
| Source | Amount |
|---|---|
| Accumulated Report, WT 2552 'Income Tax (employee)', Sep-2026, 418 employees | 1,543,834,892 |
| = monthly run WT 2552 (G2N REF-P201-090, 261 employees) | 1,399,199,389 |
| + weekly run withholding (Base of Withholding REF-P201-216, column 'WITHOLDING TAX WITH CONTRIBUTION') | 42,067,461 |
| + residual: 4 employees in NO run file received (two of them carry WT 62116 Vacation Terminations and WT 62110 in September = settlement runs) | 102,568,042 |
| Accumulated Report, WT 21330 'Personal Income Tax Withholding (Theoretical)', Sep-2026, all in the monthly run | 69,301,209 |
| **Casilla 93 candidate (2552 + 21330)**, before the nearest-1,000 rounding | **1,613,136,101** |
| Accumulated Report, WT 21140 'Personal Income Tax Withholding-Retirees', Sep-2026, 17 pensioners (casilla 94 per the spec) | 5,145,376 |
| **Casillas 93 + 94** | **1,618,281,477** |

Per-employee check: for 414 of the 418 employees with a September WT 2552 value, Accumulated = monthly G2N 2552 + weekly withholding, to the peso; the weekly file's column 'WITHOLDING TAX WITH CONTRIBUTION' equals the Accumulated WT 2552 of the same 132 employees to the peso (42,067,461). The 4 residual employees belong to none of the files received: their September withholding (102,568,042) was deducted in runs the client has not sent (settlement / off-cycle runs).

Monthly Base of Withholding column 'WITHOLDING TAX WITH CONTRIBUTION' = 1,468,500,598 = G2N WT 2552 (1,399,199,389) + WT 21330 (69,301,209) exactly: the client's withholding working report counts WT 21330 as withholding practised, which is the spec rule for casilla 93 (21330 where it carries the withholding actually deducted).

Other withholding wage types in September: 21129 (terminations), 25832 (stock awards), 25833 (IC local) = 0; 21114, 21619, 25834 (theoretical / hypothetical, out of scope) not present in September.

## Verdicts on the final spec (CO-DIAN-002, sheet 'Formulario 350 Spec')
| Row | Casilla | Verdict | Evidence |
|---|---|---|---|
| 22 | 77 base, work income | Aligned (confirmed) | monthly Base of Withholding column 'WITHOLDING TAX BASIS' 6,263,719,152 + weekly 804,582,972: the base exists per run and is only complete when every run is summed |
| 23 | 93 withholding, work income | Aligned (confirmed) | 2552 of all runs + 21330 = 1,613,136,101 reconciles to the Accumulated Report; no single run or pay group gives the month: monthly 1,399.2 M + weekly 42.1 M + settlement runs 102.6 M + 21330 69.3 M |
| 24 | 78 base, pension income | Not evidenced | the pensioners' G2N (REF-P201-184) has no withholding or taxable-base column; the 17 pensioners with WT 21140 in September are NOT among its 454 ids |
| 25 | 94 withholding, pension income | Aligned (rule) / Not evidenced (run) | WT 21140 = 5,145,376 in the Accumulated Report for 17 pensioners; the run that deducted it was not received |

## Findings
1. The rule "casilla 93 sums every pay group and every run of the month" is CONFIRMED by the data: 1,543,834,892 of WT 2552 is spread over the monthly run (261), the weekly run (132) and at least one settlement/off-cycle run (4 employees, 102,568,042). No spec change.
2. WT 21330 treatment CONFIRMED: the client's own withholding report adds 21330 (69,301,209, 6 employees with a non-zero value, 9 ids with a line) to the withholding practised. No spec change.
3. Pensioners: the 'CO - Pensionaries' run received (454 ids) carries pensions (62154), pensioner allowance (62830) and association / health deductions, but no withholding column, while the Accumulated Report shows WT 21140 for 17 other pensioner ids in September (5,145,376). Either a second pensioners' run exists or the 17 are paid in another group. Client question (new, round 3).
4. Settlement runs of September: 4 employees with withholding in September (102,568,042) are in none of the files; two of them have WT 62116 / 62110 in September (final settlements). The client has still not sent the list of all September runs nor the settlement runs (open since round 2). Client question (kept).
5. October: the termination run REF-P203-119 (2 leavers) carries WT 2552 of 85,717,464 on vacation paid in cash (62116, 141,345,386) and indemnity (62181, 200,453,880): it enters casilla 93 of OCTOBER, the month it is practised, as the spec states. One of the two leavers was in the September monthly run (September 2552 8,808,879, October 2552 48,095,372); the other was not in any September run file.
6. The files 'Base of Withholding - 16oct' and 'Gross to net ... Monthly - 16oct' are the same content as the earlier copies (hash-identical, or cell-identical); 'Base of Withholding (1) - 16oct' is cell-identical to the round-1 file although its bytes differ.

No change to CO-DIAN-002 is proposed from this reconciliation.

## Update 18 Oct 2026 - reconciliation against the full list of September runs (Heidy)

Runs of September 2026 (id | group | date | headcount): REF-P199-263 Weekly+Monthly 08-31 (3); REF-P199-250 Monthly+Weekly 08-31 (16); REF-P199-307 Weekly 08-31 (124); REF-P199-483 Weekly 09-01 (1); REF-P199-776 Monthly 09-03 (1); REF-P199-836 Weekly+Monthly 09-03 (17); REF-P199-846 Weekly 09-03 (126); REF-P199-994 Retirees 09-04 (21); REF-P200-272 Weekly 09-08 (1); REF-P200-438 Weekly 09-09 (126); REF-P200-455 Monthly+Weekly 09-09 (19); REF-P201-090 Monthly 09-16 (261); REF-P201-184 Pensionaries 09-18 (454); REF-P201-209 Monthly 09-17 (5); REF-P201-332 Weekly 09-18 (132).

Correction on the weekly id: the Base of Withholding files carry their own report id, not the payroll run id (monthly: Base of Withholding REF-P201-065 = run REF-P201-090). The weekly Base of Withholding REF-P201-216 (132 employees, generated 2026-09-18) is the withholding working report of the weekly group whose last run of the month is REF-P201-332 (132). Its withholding equals the whole September WT 2552 of those 132 employees in the Accumulated Report (42,067,461, 93 employees with a value), so it covers the month's weekly withholding; whether WT 2552 is deducted only in the last weekly run or in each of the four weekly runs (124 / 126 / 126 / 132 employees) cannot be told without the four gross-to-net files (client question).

| Run(s) | Files received | Withholding of the Accumulated Report explained (Sep-2026) |
|---|---|---|
| REF-P201-090 Monthly (261) | G2N + Base of Withholding (REF-P201-065) | WT 2552 1,399,199,389 (casilla 93) + WT 21330 69,301,209 (casilla 93) |
| Weekly group: REF-P199-307, REF-P199-846, REF-P200-438, REF-P201-332 | Base of Withholding of the group (REF-P201-216) only | WT 2552 42,067,461 (casilla 93), not split by run |
| REF-P201-184 Pensionaries (454) | G2N | 0 - no withholding wage type in the run |
| REF-P199-994 Retirees (21) | none | WT 21140 5,145,376 on 13 pensioners (casilla 94) - the only run that can carry it (all 13 also carry 21140 in August; none is in REF-P201-184); to be confirmed with the file |
| Mixed and small runs: REF-P199-263 (3), REF-P199-250 (16), REF-P199-836 (17), REF-P200-455 (19), REF-P201-209 (5), REF-P199-776 (1), REF-P200-272 (1), REF-P199-483 (1) | none | WT 2552 102,568,042 on 4 employees: three final settlements (62110 / 62116 / 62117, one with 62115 and 62203) and one off-cycle payment (62203 'Reconciliations PMI additional payment'); run not identifiable without the files |
| **Total** | | **2552 1,543,834,892 + 21330 69,301,209 = casilla 93 1,613,136,101; 21140 5,145,376 = casilla 94; 1,618,281,477** |

Timing: the runs dated 2026-08-31 (REF-P199-263, REF-P199-250, REF-P199-307) belong to August if they were paid on 31 August (withholding is declared in the month of payment or credit to account, whichever first); whether the Accumulated Report's September column is by period or by payment date is not evidenced (client question). The spec now states the payment-date rule explicitly (CO-DIAN-002 M22, M23, Population Rules C5 - map `final-prep/CO-DIAN-002-timing-map.json`).

Contingent withholding: the Base of Withholding column 'CONTINGENT WITHHOLDING' = 'WITHOLDING TAX WITHOUT CONTRIBUTION' - 'WITHOLDING TAX WITH CONTRIBUTION' (ET arts. 126-1 / 126-4), 20 employees of the monthly group (14,300,634) and 1 of the weekly group (14,800) in September; the WT 2552 totals exclude it, so it is outside Formulario 350 as the spec (M23, Population Rules C5) states. Whether this column is the 'contingent withholding report' the client mentioned is a client question.
