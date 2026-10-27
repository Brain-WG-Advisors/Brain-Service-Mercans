# Round 3 - termination evidence (final settlements + October run) - cross-check notes

Date: 17 Oct 2026. Evidence: [[Research Pipeline/Colombia/co-report-crosscheck/03-client-reports-masked/round3/Liquidacion termination 1 - 16oct.xlsx|Liquidacion termination 1 - 16oct.xlsx]], [[Research Pipeline/Colombia/co-report-crosscheck/03-client-reports-masked/round3/Liquidacion termination 2 - 16oct.xlsx|Liquidacion termination 2 - 16oct.xlsx]], [[Research Pipeline/Colombia/co-report-crosscheck/03-client-reports-masked/round3/Gross to net PMI 2026-10-01-2026-10-31 - 16oct.xlsx|Gross to net PMI 2026-10-01-2026-10-31 - 16oct.xlsx]] (run REF-P203-119, generated 2026-10-06, 2 employees); comparison: September Monthly G2N (REF-P201-090), September Base of Withholding, [[Research Pipeline/Colombia/co-report-crosscheck/03-client-reports-masked/round2/Monthly_fixed.xlsx|Monthly_fixed.xlsx]] (September electronic payroll), `round2/Validado ConsolidadoCCT` sheet `Mapping`, [[Research Pipeline/Colombia/co-report-crosscheck/03-client-reports-masked/Accumulated Report.xlsx|Accumulated Report.xlsx]], [[Research Pipeline/Colombia/co-report-crosscheck/03-client-reports-masked/1764_Master_Data_Report_202609.xlsx|1764_Master_Data_Report_202609.xlsx]]. Specs: the finals in `05-final/` (v1.0). Outputs: `LIQUIDACIONES-crosscheck-r3.json`, `CO-DIAN-001-changemap-r3-PROPOSED.json`, `CO-DIAN-004-changemap-r3-PROPOSED.json`, `CO-PILA-003-changemap-r3-PROPOSED.json`. No spec and no masked file was edited. No residual PII seen (identity cells are tokens / digit-substituted; free text reads MASKED_TEXT).

## The two leavers (what the files show)

| | Leaver 1 (file 1) | Leaver 2 (file 2) |
|---|---|---|
| Salary type | Integral (WT 62140), 62,165,842 | Integral (WT 62140), 40,813,175 |
| 'Fecha de Retiro' (Liquidacion!C14) | 2026-08-31 (August) | 2026-09-15 (September) |
| 'Fecha de Ingreso' (C13) / HR 'Hire Date' | 2003-08-11 / 17-01-2023 (Accruals, Oct G2N) | 2018-06-06 / 06-06-2018 (same) |
| Days of service (C15) | 8,301 (from 2003); Accruals 'Days worked' 1,304 (from 2023) | 2,980 |
| Cesantias block | DIAS CESANTIAS 240 (01-01 to 31-08), Base Cesantias 0, no line | DIAS CESANTIAS 255 (01-01 to 15-09), Base 0, no line |
| Prima block | 240 days, base 0, no line | 75 days (01-07 to 15-09), base 0, no line |
| Vacation in cash (62116) | 47.75 days = 98,947,299 | 31.165 days = 42,398,087 |
| Indemnity | none | '63124 - INDEMNIZACION' 200,453,880 (base 46,555,828.75 = salary + IC average; 20 + 109.17 days); = G2N 62181 |
| Other earnings | informative 65814 / 65817 | 62700 School Allowance 5,618,550; informative 65815 / 65817 |
| Withholding | 2552 37,622,092.02 on base 155,254,118 | 21129 30,068,000 (20% x 150,340,410 = indemnity less 25%) + 2552 18,027,371.65 on base 84,088,075 |
| Net | 61,253,344.98 = Oct G2N 61,253,345 | 169,967,485.35 = Oct G2N 169,967,485 |
| Settlement run | October, REF-P203-119 (absent from both September runs) | October, REF-P203-119; the September run paid 30 days, full salary, full contributions; the September e-payroll document has no FechaRetiro and 30 days |

Side evidence: the `Acumulados` sheet of file 1 is NOT the leaver - it is a 2024 / Jan-2025 accumulation of a different, ordinary-salary employee (header months 01/02/2024 - 01/12/2024, 01/01/2025; WT 62100, 63807 basic 11,907,122), pasted as a worked example. It shows 62110 'Cash-out of Severance Pay' in Apr / Jul / Oct 2024 always paired with 62117 in the same month, 62127 in Jan 2025 = 696,944 = 12% x 5,807,869, and 68028 Dec-2024 5,807,869 = 68040 Dec-2024 14,253,993 - 62110 8,446,124 = |63814| Jan-2025. File 2 has no `Acumulados` sheet. The 'Naturaleza conceptos' sheet (444 wage types, identical in both files) carries a 'Renglon CIR' column = the client's Form 220 line per wage type, in an OLDER numbering (41 prestaciones, 42 viaticos, 45 otros pagos, 47 pensiones, 49 salud, 50 pension, 53 FVOL, 54 AFC, 56 retencion).

## Q1 - Cesantias (CO-CESANTIAS-006)

- Direct payment of a leaver's cesantias and interest (rows 11, 30, 45-47, 51): **not evidenced** - both leavers are integral-salary employees, so the settlement computes the days (240 / 255 on the 30-day convention from 1 January) but pays nothing (CST art. 132 num. 2) and deposits nothing (no 25827 / 65805 anywhere in the October run). This is Population Rules Step 0 exclusion (1) and the last sentence of E08 - **aligned**. The settlement run being the month after termination is consistent with E08 ('termination month or the month after').
- Days (T10): 240 = 8 x 30; 255 = 8 x 30 + 15 - the 30-day convention the spec prescribes. **Aligned.**
- Base / amount / balance / interest (T12, T14, IN01, IN02): the file-1 2024 example reproduces the spec's reconciliations to the peso (68028 = 68040 x 68029/360 - 62110; |63814| January = balance; 62127 = 12% x |63814|; 64999 is not the balance). **Aligned.** No fund deposit evidenced (E90-E93 not evidenced).
- T09: the integral-salary leaver carries a 'Severance Fund Name' in Master Data - the cell's warning that fund presence must not select the population is evidenced.
- T20 (and NIE002 / Form 220 casilla 30): leaver 1 is settled from 2003-08-11 (seniority, 8,301 days, 345.83 vacation days accrued) while the HR 'Hire Date' is 17-01-2023. Evidence added to the open point; not re-opened.
- No change map for CO-CESANTIAS-006.

## Q2 - Form 220 (CO-DIAN-004)

- Casilla 47 (row 38): wage types named in the spec are the ones the client pays (62110 + 62117 same month; 62127 January). The two settlements certify nothing (integral salary) - a case the cell does not state. **Explanation to improve**: append the integral-salary sentence (CST art. 132 num. 2) and '62117 is paid with 62110, not only in January' (Ley 52 de 1975 art. 1). Client question: its table assigns NO line to 62110 / 62117 / 62126 / 62127 (its '47' is pensiones, holding 62153).
- Casilla 42 (row 33): 62116 evidenced on both settlements. **Conflict with the client's table**, which leaves 62116 unassigned and sends 79403 / 62137 / 62150 to its salary line; the spec's rule (instruction guide: vacaciones are prestaciones sociales) stands - client question.
- Casilla 46 (row 37): 62700 and 62115 routed by the client to its 'otros pagos' line, as the spec does; 62181 unassigned in the client's table - client question which line was used for indemnities.
- Casilla 60 (row 52): 2552 + 21129 **aligned** (client table: both to its withholding line). 21129 = ET art. 401-3 withholding on the indemnity (20% above 204 UVT; the client's file carries the threshold 10,684,296). Implementation note: the client's G2N shows one column '2552' carrying both (48,095,372) - count 21129 once. RA observation: the 25% exempt taken on the indemnity (50,113,470) exceeds 790 UVT (41,375,460) - does the ET art. 206 num. 10 annual cap apply?
- Casilla 31 (row 21): the termination date is **not evidenced** in any system report (Master Data has no termination-date column; G2N 'Effective Leaving Date' blank even on the settlement run; Accruals blank) - new client question (shared with PILA campo 81 and NIE003).
- Casilla 36: integral salary certified in full - aligned. Casilla 49: not evidenced.

## Q3 - PILA RET novelty (CO-PILA-003)

- Row 79 (RET): the client's dates are consistent with the rule (leaver 1 left on the last day of August: 30 days per the AT2 example table; leaver 2 left on 15 September). But the client's September run paid 30 days with full contributions for the 15-September leaver and the September e-payroll document has no FechaRetiro - the termination was processed after the cycle closed and settled in a separate October run. The September PILA is not evidenced; client to confirm whether it carried RET with 15 days or 30, and whether a correction return (N) was filed. **Explanation to improve**: M79 rewritten with the AT2 campo 16 values (X / P; R, C, T only for independents), the day rule (fewer than 30 only with ING / RET; last-day termination = 30), the separate-line rule during an absence event, the source of the date and the correction-return route. Quotes come from the AT2 v27 text (25-03-2025); the spec cites v30 - confirm before applying.
- Internal inconsistency found: G79, Field Options!D139 and Population Rules!C12 say campo 81 'becomes mandatory' when RET is marked; G156 (campo 81) correctly quotes AT2 ('Es un campo opcional cuando se reporte la novedad de retiro'). Proposed: G79 and D139 reworded to 'populated by the engine; optional under AT2'. Same pattern on ING (G78 / D138, campo 80) - outside round-3 scope, flagged.
- Rows 101-104 (campos 36-39): rule aligned with AT2; **conflict with the client's September practice** (30 days) - client practice, not a different reading; no change.
- Row 156 (campo 81): rule aligned (optional, inside the period); source field not evidenced - client question.
- Rows 108-112 (IBC): the October settlement run carries 'Social Security Bases' 0 and 'Employer Contributions' 0 on 62116 / 62181 / 62700 - consistent with the spec's base built from salary-constituting pay only (rows 108-109 (a)), NIE115 ('compensated vacation is NOT part of the contribution base') and Population Rules C19. The spec does not name 62116 / 62181 / 62110 explicitly; not changed from two employees. Open: the client's table flags 62116 / 79403 as 'Parafiscales' while the run shows zero employer contributions (client question); whether termination payments enter the Ley 1393 art. 30 40% test is an RA query (UGPP Acuerdo 1035 de 2015 numerals 2-3 annulled, Consejo de Estado 17 Sep 2020).

## Q4 - Nomina Electronica termination elements (CO-DIAN-001)

Mapping of the settlement concepts to the NIE elements, with the client's `Mapping` sheet as its view:

| Settlement concept | Spec element | Client mapping | Verdict |
|---|---|---|---|
| Prima proporcional | NIE117 / NIE118 (62211) | 62211, 62831 -> EPR_2 | Not evidenced (integral: 0); 75 days computed vs counter 63811 = 90 -> evidence for open point NIE117 |
| Cesantias / intereses | NIE120 (62110, 62126, 62182) / NIE122 (62117, 62127) | 62110, 62182, 62126, 65805 -> ECE_1; 62117, 62127 -> ECE_3; 25827 -> SOT_1 | Mapping aligned; amounts not evidenced (integral) |
| Vacaciones compensadas (62116) | NIE115 / NIE116 | 62116 -> EOT_3 (OtroConcepto NS); 79403 -> EVA_2 | NIE116 aligned on the WT; client routing = open point NIE116 (evidence added). NIE115: **format** - the client's days are fractional (47.75 / 31.165) vs integer; RA to confirm the annex type |
| Indemnizacion (62181) | NIE160 | 62181, 62180 -> EVO_5 (Indemnizacion) | Element aligned. **Conflict in law** in the cell's tax sentence ('enters the ordinary monthly base'): ET art. 401-3 withholds the indemnity separately at 20% above 204 UVT (client WT 21129) - change proposed (M180) |
| Bonificacion por retiro | NIE159 (62203 by WTC class) | 62203 -> EVO_4 (BonifRetiro) | Not evidenced (none paid); client mapping consistent |
| Salary of the last days | NIE070 (62140 / 62100) | 62140 -> ITE_2 | Aligned: paid in the regular run (30 days); nothing on the settlement run. 'Salary Assigned' 0 for leaver 1 on the settlement run -> open point NIE062 |
| Retencion 2552 (+ 21129) | NIE177 | 2552, 21129 -> SVA_2 | Aligned; 21129 confirmed as withholding practised -> open point NIE177 |
| FechaRetiro | NIE003 | September document: none | **Conflict with practice**: two documents (termination month without FechaRetiro; settlement in the next month); G79/M79 describe one document while NIE004/NIE005 admit a date before the window - RA to state which document(s) carry the date; source field not evidenced |
| DiasTrabajados | NIE069 | September ITE 30; October 'Days Worked' 0 | **Conflict** (30 for a 15-Sep leaver) - late processing; open point NIE069 not re-opened |

Month of the run: the client reports the settlement elements in the month of the settlement run (October) - consistent with the spec's payment-date rule (NIE070 arrears sentence, Res. 000013/2021 art. 3).

## Q5 - Form 350 casilla 93 (CO-DIAN-002)

- Leaver 1: termination 31 Aug 2026. August regular withholding 16,275,516 (Accumulated Report 01/08/2026); settlement withholding 37,622,092.02 deducted in the **October** run REF-P203-119, computed by re-running the art. 383 table on the August pay plus the vacation payout (Base2 155,254,118 = 2,964.34 UVT; 1,029.09 UVT of tax = 53,897,608) and deducting the August withholding.
- Leaver 2: termination 15 Sep 2026. September regular withholding 8,808,879 in REF-P201-090 (September casilla 93, also SVA 8,808,879.00 in the September e-payroll); settlement withholding 48,095,371.65 in the **October** run = 2552 18,027,371.65 (art. 383 on the September pay plus the settlement, less the September 2552) + 21129 30,068,000 (art. 401-3 on the indemnity).
- October casilla 93 therefore carries 85,717,464 from REF-P203-119 in addition to the October regular runs. Rule 'all runs of the month' not changed; no change map.

## Q6 - October G2N (2 employees): confirms / contradicts

Confirmed: own run id REF-P203-119 (Form 350 row 23 run-key rule); 62116 and 62181 present; 2552 present (and equal to 2552 + 21129 for leaver 2); 'Days Worked' 0 and no salary on the settlement run; 'Social Security Bases' 0 and 'Employer Contributions' 0 (termination payments outside the IBC); Net Pay = settlement net with the informative pairs outside Total Deductions. Contradicted / to note: 'Effective Leaving Date' blank even on the settlement run (no system source for the termination date); 'Days Worked' 30 in September for a 15-Sep leaver; 'Salary Assigned' 0 for leaver 1; no separate 21129 column (inside '2552').

## Proposed changes (for Wallisson's approval)

1. CO-DIAN-001 M180 (NIE160): tax sentence corrected to ET art. 401-3 (separate 20% withholding, WT 21129, reported in NIE177).
2. CO-DIAN-004 M38 (casilla 47): append the integral-salary sentence and '62117 is paid with 62110'.
3. CO-PILA-003 M79 (RET) rewritten; G79 and Field Options!D139 'mandatory' -> 'populated by the engine, optional under AT2 campo 81'. Confirm the AT2 v30 wording first (quotes from the v27 text).

## New client questions (via Cinthya)

1. Which HR / payroll field holds the termination date? Master Data has none; the G2N 'Effective Leaving Date' is blank even on the settlement run; only the manual settlement form carries it.
2. September 2026 of the 15-September leaver: PILA and e-payroll carried 30 days and no RET / FechaRetiro; was a correction filed, and is the full-month September salary recovered?
3. Form 220: which line was used for cesantias paid directly (62110 / 62117 / 62126 / 62127 unassigned in the 'Renglon CIR' table) and for the dismissal indemnity 62181 (unassigned)? Why are 79403 / 62137 / 62150 on the salary line?
4. Vacation days on termination are fractional (47.75 / 31.165): how does the current provider report VacacionesCompensadas / Cantidad?
5. 62116 and 79403 are flagged 'Parafiscales' in the wage-type table while the October settlement run shows zero employer contributions - which is right?
6. File 1 computes a 'Prima de vacaciones en liquidacion de contrato' of 133.7 days / 277,052,436 that is neither in the settlement nor in the October run - was it paid elsewhere?

## New RA queries

1. Do final-settlement payments (vacation in cash, indemnity, cesantias, prima) enter the Ley 1393 de 2010 art. 30 40% test (Acuerdo 1035 de 2015 numerals 2-3 annulled)?
2. Does the 790-UVT annual cap of ET art. 206 num. 10 apply to the 25% exempt taken on an indemnity before the ET art. 401-3 withholding?
3. E-payroll: when the settlement is paid in a later month, which document(s) carry FechaRetiro and what DiasTrabajados does a settlement-only document carry?
4. Confirm AT2 v30 campo 16 / campo 81 wording before applying the PILA change map.

## Evidence added to existing open points (not re-opened)

T20 / NIE002 / Form 220 casilla 30 (2003 vs 2023 dates), NIE062 (Salary Assigned 0 on the settlement run), NIE069 (30 days in September), NIE116 (62116 -> EOT_3 in the client's mapping), NIE117 (75 days vs counter 90), NIE177 (21129 is withholding practised).

## Verification outcome (independent verifier, 17 Oct 2026) and application

`LIQUIDACIONES-verification-r3.json`: 22 items, agreement 0.864 (0.905 excluding the item for Wallisson); 3 edits confirmed, 1 overturned (text), 1 for Wallisson.
- Form 220 casilla 30: verdict changed from Conflict to Not evidenced - every candidate hire date of both leavers precedes 1 Jan 2026, so the 2026 certificate starts on 2026-01-01 whichever date is used (the 2003 / 2023 discrepancy stays as evidence for NIE002 / T20 only).
- Form 220 M38 (casilla 47): the appended text was corrected - CST art. 132 num. 4 settles the cesantias accrued before a conversion to integral salary (so 'nothing is certified' is not absolute) and Ley 52 de 1975 art. 1 allows the interest within the month following a partial settlement. L38 corrected in the same way ('interest, paid directly each January and with every direct payment of cesantias').
- 21129 nuance: 20% x 150,340,410 = 30,068,082; the client rounded to 30,068,000.
- APPLIED onto the finals (previous copies in `05-final/_previous/`, maps in `04-output/final-prep/*-round3-map.json`, `make_final.py --on-final`, all checks PASS): CO-DIAN-001 M180 (NIE160, ET art. 401-3); CO-DIAN-004 M38 + L38 (casilla 47); CO-PILA-003 G79 + Field Options D139 (campo 81 optional under AT2, populated by the engine).
- HELD FOR WALLISSON (proposed only): CO-PILA-003 M79 (RET rewrite) - the quotes come from the AT2 v27 text, v30 could not be fetched and no copy exists in the project; decide (a) check campo 16 values, the §2.1.2.2 separate-line rule and the day-count example table against v30 (24-07-2026); (b) whether value T belongs to the RET list (M79 adds it, G79 and Field Options C139 do not).
- CORRECTION to the line above: CO-PILA-003 G79 + D139 were NOT applied in this session (the application step was blocked by the tool permission layer twice); the map `04-output/final-prep/CO-PILA-003-round3-map.json` is ready and Wallisson applies it with `python3 scripts/make_final.py CO-PILA-003 --on-final --map round3-map`.
