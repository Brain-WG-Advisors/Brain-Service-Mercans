# Open points, 21 Oct 2026 - client WT map (Conceptos_cir_2025.xlsx) vs specs - internal control (not for the development team)

Builds on `OPEN-POINTS-2026-10-17.md` (kept unchanged) and `HANDOFF-2026-10-21.md` sections 2-3. Method: every wage type of the client's 'Conceptos' sheet (229 WTs, tax year 2025, column 'Renglon CIR') was compared with the casilla(s) under which `05-final/CO-DIAN-004-Formulario220-Spec.xlsx` names that wage type (column M, casillas 36-60), then each hit was read in context. The client's 'Columna medios' (Formato 2276) carries the same classification as 'Renglon CIR' (the 220 line name), so every 220 difference below carries over to CO-DIAN-005. `Conceptos_cir_2025.xlsx`: PII check by statistics, 21 Oct 2026 - 0 e-mail addresses, 0 numbers of 9+ digits, only WT codes, descriptions and line names.

## 1. Withholding - blocking, owner: BAU (client follow-up item 1)

| Topic | Client map | Our specs | Evidence |
|---|---|---|---|
| WT 21330 'Personal Income Tax Withholding (Theoretical)' | 220: 'Ninguno' (not certified); listed in 'conceptos rete' and 'Conceptos no encontrados' | **Inconsistent between our own specs.** CO-DIAN-004 casilla 60 (M52): 21330 and 25834 are notional and NOT certified. CO-DIAN-002 casilla 93 (M23, Population Rules C5, Report Matrix A40) and CO-DIAN-001 RetencionFuente (M191): 21330 included 'where it carries the withholding actually deducted'. CO-DIAN-004 also requires the year's casilla 60 to reconcile to twelve months of 350 casilla 93. | Round 3 (`round3/CO-DIAN-002-reconciliation-r3.md`): Sep-2026 21330 = 69,301,209 on 6 employees (5 with Employment Status 'D'), all in the monthly run; the client's Base of Withholding 'WITHOLDING TAX WITH CONTRIBUTION' = 2552 + 21330 to the peso; casilla 93 + 94 = 1,618,281,477 = Accumulated Report. |
| WT 25834 'Hypothetical Witholding Tax - IC Foreign Country' | 'Ninguno' | Excluded in 220, 350 and NE | Consistent. Kept in the follow-up only together with 21330. |
| WT 23552 'Income Tax (employee) - Benefit' | only in 'conceptos rete' / 'no encontrados', no line | Not named in any spec | If the employer bears the employee's tax, the tax paid is income of the employee (casilla 36/46) and the withholding is casilla 60. Ask. |

Decision held: no spec changes on 21330 until BAU answers. When answered, CO-DIAN-002, CO-DIAN-001 and CO-DIAN-004 must say the same thing.

## 2. Form 220 / Formato 2276 routing - client map differs from the spec

| WT | Client line | Spec | Owner / note |
|---|---|---|---|
| 62150 Vacation Bonus | 36 (salary) | 42 (vacation pay is a statutory-benefit payment; casilla-36 exclusion rule) | RA: re-read instruction guide Res. 000022/2024 casilla 42 (lists 'vacaciones') before keeping 42. Spec unchanged meanwhile. |
| 62830 Pensioner Allowance-6794 | 50 (pension) | 46 (payment to retirees that is not a pension) | BAU: is 62830 part of the pension (mesada) or a separate allowance? (same question as Q19 for 62151, answered 'not a pension') |
| 62118 Incentive Compensation - IC Local Country | 46 | 36 (salary) | WTC salary attribute decides (spec rule). BAU: habitual? |
| 62224 Quarterly Salary Attendance Bonus | 46 | 36 (habitual bonus) | BAU: habitual? (instruction guide: habitual bonuses = 36) |
| 62229 Years of Service Bonus NON CLA | 46 | 36 where habitual, 46 where not (WTC) | Consistent if non-habitual. No action. |
| 65838 Incentive Compensation - IC Foreign Country | 46 | 36 / 46 by WTC salary attribute | WTC. |
| 65820 Salary paid in Foreign Countries | 46 | Spec names **25830** 'Salary paid in Foreign Countries' (36 or 46 by WTC); 25830 is in the client's 'Conceptos no encontrados', the WT actually used is 65820 | Spec text: replace / add 65820 at the next change. BAU: is 65820 salary (36)? |
| 62837 Leave payout | 'No aplica' / 'Ninguno' | 36 / 42 / 46 by WTC | BAU: what does 62837 pay? (vacation payout = 42) |
| 65831 / 65837 / 65839 (Allianz, Life, Optical - CLA 'Inf.') | 'Ninguno' | 36 / 46 by WTC (in-kind payment) | BAU: why are the CLA variants not certified while the non-CLA ones (65801, 65817, 65809) are in 46? |
| 65832 Withholding Tax on Stock Options (Vesting Infor) | 'Ninguno' | casilla 60 where WTC = deducted | Consistent with 25832 in 60 (deduction side). No action. |
| 62839 Reimbursement AFC | 57 (as a contribution) | 57 netted (refund reduces the AFC deductions) | Q20 answer: refund of an unauthorised AFC deduction. Spec rule already nets it (CO-DIAN-004 M49); check CO-DIAN-005 apafc says the same. Client map adds it: tell BAU. |
| 21644 Solidarity Pension Fund-Pensioner | absent from 'Conceptos' (in 'no encontrados') | not named | 21643 / 21648 are in 54. BAU: should be 54. |
| 62182 Severance-Pay - Social Benefits | 47 | not named | Consistent with the casilla-47 rule (paid to the employee). Add to the spec list at the next change. |
| 62211 Service Legal Bonus | 42 | not named | Consistent (prima de servicios = statutory benefit). Add to the spec list. |
| 79403 Vacations Compensated In cash | 42 | not named | Consistent with 42. Add to the spec list. |
| 65813 / 65826 Meal Allowance Inf. (2005, Apprentice) | 37 | only 65818 named | Same 41 / 310 UVT test applies to every meal WT; spec names only 65818. Add both. |
| 25819 Voluntary Contribution to Mandatory Pension Plan | 55 (RAIS) | casilla 55 has no WT named | Consistent; name it. |
| 21141 (FVOL retirees), 21142 (AFC retirees), 21154 / 21648 / 21649 (pensioner contributions), 21155 (pensioner withholding) | 56 / 57 / 54 / 54 / 53 / 60 | not named | Consistent with the casilla rules; name them in the WT-to-casilla table. |
| Overtime 62841 / 62842 / 62845, leave payout 79419, 25830 | absent from the client map | named in casilla 36 | BAU: are these WTs used? (absent from the 2025 map) |
| 65805 Payment Severance Funds Inf. | 49 | 49 via 25827 (65805 is the mirror; 'take one, not both') | Consistent. |
| 35 earning WTs in line 46 and 12 in line 36 that the spec does not name | - | Spec rule: engine keeps an explicit WT-to-casilla table from WTC attributes | Not a conflict. The client map is the starting point for that configuration table (development). |

## 3. Client answers of 21 Oct still to act on (from HANDOFF-2026-10-21 section 2)
- Numeral 33 (2276) / casilla 59 (220) - re-check against ET art. 206 num. 4 (round 3 set numeral 33 to zero). Owner: Compliance (round 5, task 2).
- Pensioners: health 4% / 10% / 12% and zero withholding; retirees' amounts and 21140 are client inputs. Owner: Compliance (task 2), source Ley 2294/2023 art. 78.
- Termination date source = system 'Termination' record. Owner: Compliance (task 2) + DD mapping.
- 2276 rounding = whole pesos, half up. Owner: Compliance (task 2).
- CO-DIAN-001 citations Res. 000013/2021 -> Res. 000227/2025 (and CO-SIR-001). Owner: Compliance (task 2).
- Q14 PILA correction return type, Q16 NE Cantidad data type, Q17 IBC of vacation compensated in cash: owner RA.

## 4. Scope (Manju / Andy)
- Manual today, so the specs describe new functionality: PILA (Mi Planilla), annual cesantías deposit (Aportes en Línea), Formato 2276, contingent withholding. BAU inventory `PMI REPORTS.xlsx` (14 Oct) also lists as manual: Base of Withholding, Detail IBC per Employee, Leave Absence, Loans Balance, Severance Massive Calculation, CARGA MASIVA AFC, CARGA MASIVA CONSOLIDADA CCT.
- PILA of the pension payer for 454 pensioners / 21 retirees: layout differs from the AT2 cotizantes file of CO-PILA-003. In or out of scope?
- `Variance on Totals.xlsx` and `CARGA_MASIVA_CONSOLIDADA_CCT09.xlsx` were shared on 15 Oct and are client operational reports: record as 'received, out of scope' (`state/report-spec-map.md` still says 'not received').

## 5. Still open from earlier (unchanged)
See `OPEN-POINTS-2026-10-17.md` sections 1-3 and the appendix (RA themes). Folder 'September 2026 Payroll Validation Files' (Heidy, 21 Oct): no access yet; the Google Drive app shows only single-file shares, all already in rounds 1-3.
