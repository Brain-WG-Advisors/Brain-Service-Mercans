# Round 5 - spec changes, 21 Oct 2026 - APPLIED 21 Oct 2026 (Wallisson's approval; maps `final-prep/<SPEC>-round5-map.json`, 38 cells; independent verification `final-prep/ROUND5-verification.json` incl. second_pass; make_final.py --on-final PASS on all six; previous copies in `05-final/_previous/*.20261021-*`)

Applied with the verifier's corrections: CO-DIAN-001 M41 = item 2 of art. 1.5.3.3.1; B2 mapping text without process wording; typo 'payment o credit' fixed in the six Payroll Scope Summary cells; casilla 37 meal test names 65813 / 65826 too. B4 applied in its revised form: rule of the Form 220 instruction for casilla 56 (amount actually deducted from the employee's labour income in the employee's name); institutional-plan WTs classified by the WTC employee/employer-side attribute (client follow-up item 11). Windows fixes to scripts/make_final.py: path normalisation (normpath) and closing the source zip before os.replace.

Scope: HANDOFF-2026-10-21 section 5 task 2, checked one by one against `05-final/` and the primary sources. Sources saved in `brain-service/raw/docs/oficiais/CO/` (prefix `2026-10-21-`) unless stated.

## A. Items of task 2 already covered by the finals - no change
| Item | Where it already stands | Source checked 21 Oct |
|---|---|---|
| WT 62839 nets the AFC deductions | CO-DIAN-004 casilla 57 (M49); CO-DIAN-005 N27 (M34) | BAU answer Q20; ET art. 126-4 (sums deposited) |
| WT 62151 / 62152 = casilla 46 / potro, not pension | CO-DIAN-004 casillas 46 and 50; CO-DIAN-005 N17 / N21 | BAU answer Q19 |
| Numeral 33 / casilla 59 populated only where art. 206 num. 4 applies (severance paid or deposited), zero otherwise | CO-DIAN-005 N33 (row 42), Population Rules C29; CO-DIAN-004 casilla 59 | Res. 000227/2025 art. 1.3.7.1.1 num. 33 ('Unicamente para trabajadores que aplique el numeral 4 articulo 206 E.T.'); DUR 1625/2016 art. 1.2.1.20.7 (severance realised on direct payment or on deposit to the fund). The HANDOFF note 'set to zero in round 3' refers to the blank -> zero format fix, not to the population rule. |
| 2276 amounts in whole pesos | CO-DIAN-005 rounding column (e.g. P16): 'whole pesos - no decimals ... (Anexo T3.45; art. 1.3.7.1.1 par. 2)' | Res. 000227/2025. The half-up method stated by BAU is not in the resolution: not added (no primary source). |
| Pensioners' health 4% / 10% / 12%, zero withholding | Not a report-spec rule: the reports read the deducted WTs (21645-21647, 21649; 21140, 21155) | Rates confirmed: Ley 100/1993 art. 204 par. 5 (2022 table) + inciso added by Ley 2294/2023 art. 78; Res. MSPS 1271/2023 Anexo Técnico 1 from 2024: 1 SMLMV 4%, >1 to 3 SMLMV 10%, >3 SMLMV 12%. Goes to CCG / WTC alignment (HANDOFF-2026-10-16 task 2). |

## B. Proposed changes
### B1. Res. 000013/2021 -> Res. 000227/2025 (20 cells, all six specs)
Mapping read in the DIAN normograma notes 'Articulo compilado como articulo ... en la Resolucion 227 de 2025' (`2026-10-21-Res-DIAN-0013-2021-normograma.htm`) and confirmed in the Res. 000227/2025 text for 1.5.3.2.1, 1.5.3.4.1.1, 1.5.3.8.3, 1.5.3.8.5:
art. 2 -> 1.5.3.2.1 · art. 3 -> 1.5.3.2.2 · art. 5 -> 1.5.3.3.1 · art. 8 -> 1.5.3.4.1.1 · art. 22 -> 1.5.3.8.1 · art. 24 -> 1.5.3.8.3 · art. 26 -> 1.5.3.8.5.
Cells: CO-DIAN-001 Report Matrix B13 (art. 3), B14 (art. 8); Payroll Scope Summary C21 (art. 2), C35 (art. 26), C38 (art. 3), C40 (arts. 2-3); spec M6 (art. 24), M16 (art. 3), M17 (art. 26), M29 (art. 26), M31 (art. 22), M41 (art. 5), M86 (art. 3); File Structure A124; Field Options D90; and Payroll Scope Summary C37/C38/C40 of CO-DIAN-002, -004, -005, PILA-003, CESANTIAS-006 (art. 3). Wording: 'Res. DIAN 000227 de 2025 art. 1.5.3.x' (no 'formerly').

### B2. Termination date source (BAU answer Q13)
- CO-DIAN-001 M79 (NIE003) and CO-PILA-003 M156 System Mapping `Contract.End_Date` -> `Contract.End_Date (termination date of the system 'Termination' record, as confirmed by the employer)`.
- CO-DIAN-004 row 21 (casilla 31) System Mapping `PayPeriod.Year_End` -> `PayPeriod.Year_End, or Contract.End_Date (system 'Termination' record) where the employee left during the year`.

### B3. Six-month average - how it is computed (BAU answer Q8)
Add to CO-DIAN-004 casilla 59 (M51) and CO-DIAN-005 N33 (M42), with source DIAN Concepto 4443 de 2025 (int. 522, 9 Apr 2025; `2026-10-21-DIAN-Concepto-4443-2025.htm`) and ET art. 206 num. 4 ('salario mensual promedio'):
'The average is the monthly average salary of six months: on termination or on a withdrawal of severance, the last six months of employment or the six months before the withdrawal; while the employment continues, the six months of the immediately preceding year at the time of the deposit to the fund; for employees outside the Ley 50 de 1990 regime, the six months before the employer recognises the severance (ET art. 27 num. 3).'

### B4. 2276 numeral 26 / 220 casilla 56 - voluntary pension WTs (BAU answer Q11)
CO-DIAN-005 N26 (M33) lists the institutional-plan WTs (25820, 25821, 21210, 21211, 65803, 65804) as possible art. 126-1 contributions by WTC attribute. BAU: voluntary pension WTs are 25811, 25812, 25813, 25814, 25815, 25823 and 21141 (retirees); institutional plans are not deducted from the employee through payroll. Proposed: N26 = those seven WTs; institutional-plan WTs not reported in N26 / casilla 56 (instruction guide: contributions deducted from the employee's labour income). CO-DIAN-004 casilla 56: add 21141.

### B5. Form 220 WT lists - consistent client mappings the spec does not name (from OPEN-POINTS-2026-10-21 section 2)
Add to the SOURCE lists of CO-DIAN-004 (and the CO-DIAN-005 counterparts): 62182 -> 47; 62211, 79403 -> 42; 65813, 65826 -> 37 / 38 meal test; 25819 -> 55; 21141 -> 56; 21142 -> 57; 21154, 21648 -> 54; 21649 -> 53; 21155 -> 60; salary paid abroad: name 65820 next to 25830 (casilla 36 or 46 by WTC).

## C. Not changed until BAU answers (CLIENT-FOLLOWUP-2026-10-21)
21330 / 25834 (CO-DIAN-002, -001, -004 must then say the same thing); 62150 (36 vs 42 - RA to re-read the instruction guide); 62830 (50 vs 46); 62118 / 62224 (habitual?); 62837; CLA in-kind WTs 65831 / 65837 / 65839; 21644; 23552.
