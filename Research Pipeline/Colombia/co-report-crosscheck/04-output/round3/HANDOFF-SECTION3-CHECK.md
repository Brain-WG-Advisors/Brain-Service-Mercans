# HANDOFF-2026-10-16 section 3 - decisions in force checked against the six finals (18 Oct 2026)

Method: every decision of section 3 was searched (regular expressions, all sheets) in the final workbooks of `05-final/`; the cells found are listed; what was missing was applied through a map and `make_final.py --on-final` (checks PASS).

| Spec | Decision | Status | Where |
|---|---|---|---|
| PILA | T2R1-020 total payroll = sum of campo 45 | present | PILA Spec D58, M112; Population Rules D4, C9 |
| PILA | IBC CCF without 25 SMMLV ceiling; 70% for integral salary | present | PILA Spec M111-M112; Payroll Scope Summary C27-C28; Population Rules C4 |
| PILA | Exoneration ET art. 114-1: total earned < 10 SMMLV (Decreto 1828/2013 art. 7); campo 76 = N when campo 43 >= 10 SMMLV | present | PILA Spec M109, M150; Population Rules C7 |
| PILA | Campos 17-20, 32, 34 blank | present | PILA Spec M81, G96, G98 |
| PILA | Campos 57-60 blank / zero | present | PILA Spec rows 126-129 |
| PILA | Campo 98 closes record type 2 at position 693 | present | PILA Spec A61, M171; File Structure B12, B18 |
| PILA | **Campo 38: ARL days add up to 30; SLN / IGE / LMA / VAC-LR lines report the days of the event; IRL > 0 same value (AT2 §2.1.2.3.13)** | **APPLIED 18 Oct 2026** | PILA Spec M103 (map `final-prep/CO-PILA-003-campo38-map.json`) |
| PILA | Campos 45 and 95 may differ | present | PILA Spec M111-M112 |
| NE | AuxilioTransporte up to 2 SMMLV; collective-agreement allowance above to AuxilioS / AuxilioNS | present | NE Spec M87, M162, M163 |
| NE | DiasTrabajados = 'Days Worked' | present | NE Spec M85 |
| NE | Prepaid medicine / complementary plan / health policy -> PlanComplementarios; other insurance -> OtrasDeducciones | present | NE Spec M206 |
| NE | Document types 22 / 21; PEP / PPT per the NE annex table | present | NE Spec M56; Field Options B19-C19 |
| NE | The client's current NE file is not a template | internal decision, no spec text required | - |
| 350 | Casilla 93 = withholding practised, all pay groups and all runs | present (and confirmed by the round-3 reconciliation) | 350 Spec M23 |
| 350 | Rounding to the nearest 1,000 at casilla level (ET art. 577) | present | 350 Spec P22-P25 |
| 350 | Non-residents: 'Pagos exterior', 20% nominal, no depuration (ET art. 408) | present | 350 Spec M22-M23; Payroll Scope Summary C16, C26-C27 |
| 350 | Contingent withholding excluded | present | 350 Spec M23; Population Rules C5 |
| 350 | Pension withholding in the pensions row; RetencionFuente = 93 + 94; DIAN country table | present | 350 Spec M23, M25, M39 |
| 220 | Pesos rounded to 1,000, zero when no value; casilla 4 by the issuer | present | 220 Spec J27-J32, G11 |
| 220 | Routing 50 / 46 / 42 / 43 / 36 / 46 / 37 / 38 | present | 220 Spec M14, M27-M29, M37, M41 |
| 220 | Casilla 49 = deposits of the tax year (ET art. 27 num. 3); 52 computed; 60 withholding practised | present | 220 Spec M40; Population Rules C7, C9, C12 |
| 220 | Survivor / substitute pension to the recipient, casilla 50; document types 12, 13, 21, 22, 31, 41 | present | 220 Spec M41, M13 |
| 2276 | Calendar-year sums by payment date, employer-paid pensions included | present | 2276 Spec M16-M34; Payroll Scope Summary C40 |
| 2276 | dir / dpto / mun only when the residence country is Colombia; pais always | present | 2276 Spec G7, M7 |
| 2276 | pabop / pagahuvt / vaex; pavia; pasa / potro; peju / potro; apos / apof; ceco; vare | present | 2276 Spec M9-M41 |
| 2276 | XML ISO-8859-1, Dmuisca file name (aaaa = year of sending), max 5,000 records | present | Report Matrix B16-B17; File Structure B4, B9 |
| Cesantías | Leavers excluded from the deposit and paid directly (Ley 50/1990 art. 99 num. 4); deposit net of direct payments | present | Cesantias Spec M11, M30, M45, M50-M51 |
| Cesantías | No direct payment of the consolidated balance to an active employee except CST art. 254 | present | Cesantias Spec M30, M51; Population Rules C7 |

Round-3 applications of 17-18 Oct 2026 on top of these: CO-DIAN-005 (44 cells, Anexo T3.45 lengths / country code / XML header / numeral 33 / I50), CO-DIAN-001 M180, CO-DIAN-004 M38 + L38, CO-PILA-003 G79 + Field Options D139 + M103. Still proposed (not applied): CO-PILA-003 M79 (AT2 v30 wording), CO-DIAN-005 Payroll Scope Summary A50:C50 (numeral 17 one-off rule).
