Reply in the 'PMI Review' thread (Reply all). Replaces CLIENT-FOLLOWUP-2026-10-21.md (14 questions) after the critical review in section B below.

## A. E-mail text

Hi Heidy, Hi Cinthya,

Thank you for the answers and for the Conceptos CIR 2025 file. Three points remain open. Codes and counts only, please - no employee data.

1. WT 21330 'Personal Income Tax Withholding (Theoretical)': in the September monthly run it is part of 'Total Deductions' for 6 employees, and the Base of Withholding adds it to WT 2552 in the 'WITHOLDING TAX WITH CONTRIBUTION' column. The Conceptos map gives it no Form 220 line but maps it to the Formato 2276 withholding column. Is the WT 21330 amount remitted to DIAN as withholding (Formulario 350 casilla 93), or is it a hypothetical tax kept by the employer under a tax-equalisation arrangement? Same question for WT 25834 'Hypothetical Witholding Tax - IC Foreign Country'.
2. WT 62830 'Pensioner Allowance-6794' is paid to 2 of the 454 pensioners on top of WT 62154 'Monthly Retired Pension-6798'. What does it pay, and is it paid as part of the pension or as a separate benefit?
3. Institutional plans: the Conceptos map notes for WT 65803 that the fund makes the deductions. Do WT 21210, 21211, 21212, 25820 and 25821 reduce the employee's net pay, or are they recorded for information only?

Electronic payroll: for the 871 files of September, please put them in one zip file in a Google Drive folder shared with me.
Folder access: the folder 'September 2026 Payroll Validation Files' linked in your 21 Oct e-mail shows 'You need access' for my account. Could you share it?

**Scope (Manju, Andy)**
Still open from 19 Oct: are the PILA and cesantías specs (new system functionality) in scope for the December go-live? And the PILA of the pension payer (454 pensioners, 21 retirees), which has a different layout from the employees' PILA: in or out of scope?

Thanks a lot,
Wallisson

## B. Critical review of the 14 questions of v1 (21 Oct 2026) - internal
Sources (masked / no PII, counts and totals only): client WT nature table 'Naturaleza conceptos' (sheet in round3 `Liquidacion termination 1 - 16oct.xlsx`, columns SS / Retención / Prima / Cesantías / Indemnización / Renglon CIR, older form numbering: 36 salary, 45 other payments, 50 pension contributions, 53 voluntary pension, 56 withholding); client map `00-reference/Conceptos_cir_2025.xlsx`; `Accumulated Report.xlsx` (2026 year to date); September G2N (monthly round2, pensioners round3); BAU answers of 21 Oct.

| v1 | Verdict | Evidence |
|---|---|---|
| 1 21330 / 25834 | KEEP, sharpened (v2 #1) | Monthly G2N: Total Deductions = other 2xxxx deductions + 21330 for all 6 employees (gross - deductions = net) -> deducted from net pay. That does not prove remittance to DIAN (a hypothetical tax under tax equalisation is also deducted). Map: Renglon CIR 'Ninguno' but Columna medios = 2276 withholding column (inconsistent). The filed 350 stays with the client. |
| 2 23552 | DROP | Not in the Accumulated Report 2026 nor any September file: not used. |
| 3 62150 | DROP - our decision | Client is consistent: nature table 'Salarial', base for prima / cesantías / indemnización, line 36; 2025 map line 36. Classification (36 vs 42) is a legal decision from the instruction guide, not a client fact -> Phase 2 spec item. |
| 4 62830 | KEEP, sharpened (v2 #2) | Pensioners' G2N: 62830 on 2 of 454, on top of 62154 -> it is in addition to the pension (known). What it pays is not in any file; nature table N/A everywhere; 2025 map: pension line 50; our spec: 46. |
| 5 62118 / 62224 | DROP - answered | Nature table: 62118 'Salarial', base, line 36 (salary -> 36, as the spec says; the 2025 map's 46 is the client's filing). 62224: SS '1393' (Ley 1393/2010 art. 30 non-salary payment), not a base for prima / cesantías, line 45 'other payments' -> non-salary -> 46; our spec says 36 -> Phase 2 spec item. |
| 6 65820 | DROP | Not in the Accumulated Report 2026: not used. Spec rule by WTC attribute stands. |
| 7 62837 / CLA 65831-65839 | DROP - answered / our decision | 62837: nature table 'Salarial', base, line 36, note 'additional payment where the salary varied in the last 3 months'. CLA in-kind WTs: same benefits as 65801 / 65809 (nature table '1393', line 45 -> 46) and 65817 (map 46) -> 46 by analogy; legal routing is ours -> Phase 2 spec item. |
| 8 21644 | DROP | Not in the Accumulated Report 2026: not used; nature table line 50 (pension contributions) = 21643 -> 54 by analogy. |
| 9 62839 | DROP | Answered on 21 Oct (Q20: refund of an unauthorised AFC deduction); netting is a legal rule already in the spec (ET art. 126-4). |
| 10 overtime 62841 / 62842 / 62845, 79419, 62137 | DROP - answered by data | Overtime: Accumulated Report rows 1 / 12 / 13 -> used in 2026 (spec names them in 36). 79419: 9 rows, nature table 'Ausentismo', line 36. 62137 'Vacation Bonus-Termination Pay': nature table 'Salarial', line 36; not in the Accumulated Report 2026. |
| 11 institutional plans | KEEP, sharpened (v2 #3) | 2025 map: 21210-21212, 25820, 25821 'Voluntarios', no line; note on 65803 'aporte voluntario especial, los descuentos los hace el fondo'; nature table: 21210-21212 line 53 (voluntary pension), 65804 'Ingreso', base, line 36. They are deduction-series WTs present in the Accumulated Report 2026 (25820: 31 rows, 25821: 15) but not in the September G2N -> whether they reduce net pay is not evidenced. |
| 12 871 NE files | KEEP (answer to BAU's own question) | BAU asked how to share them (Q21). |
| 13 2276 accepted by DIAN | DROP | Asked twice without answer; does not change any spec (the spec follows Res. 000227/2025). |
| 14 folder access | KEEP | Access still pending. |
| Scope (Manju, Andy) | KEEP | No answer since 19 Oct. |

Phase 2 spec items found by this review (our decision, official source + independent verifier, independent of BAU): 62150 line 36 vs 42; 62224 to line 46 (non-salary, Ley 1393/2010 art. 30); name 62837 / 79419 / 62137 in 36, CLA in-kind 65831 / 65837 / 65839 in 46 and 21644 in 54 in the WT-to-casilla lists.
