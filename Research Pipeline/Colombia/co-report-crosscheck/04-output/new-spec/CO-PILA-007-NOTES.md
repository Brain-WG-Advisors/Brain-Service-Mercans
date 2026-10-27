# CO-PILA-007 - PILA of the pension payer (Anexo Técnico 3) - build notes, 2026-10-21

Internal file (not for development). Companion to `CO-PILA-007-AportesPensionados-Spec.xlsx` (same folder). Built by `build_co_pila_007.py`; the sample records are also in `sample-records.txt` (482 / 285 / 519 / 519 characters).

## 1. Sources per section

| Section of the workbook | Source (read on 2026-10-21) |
|---|---|
| Field table (all 108 rows), positions, lengths, types, validations, code lists | Res. MSPS 2388/2016 **Anexo Técnico 3 v15, 24-07-2026** - `raw/docs/oficiais/CO/2026-10-21-MinSalud-Anexo-Tecnico-3-PILA-pensionados.pdf` (md5 cf0bf837e8027e85cbfe4276b0d676ba per the RA) |
| Health rate bands (T2R2-048, Field Options, Population Rules) | Ley 100/1993 art. 204 par. 5 incl. inciso of Ley 2294/2023 art. 78 - `raw/docs/oficiais/CO/2026-10-21-Ley-100-1993-FuncionPublica.html`; Res. MSPS 1271/2023 art. 1 (AT1 table "A partir del año 2024") - `raw/docs/oficiais/CO/2026-10-21-Res-MSPS-1271-2023-colpensiones.htm` |
| Rounding (Rounding column, File Structure, Population Rules) | Decreto 780/2016 art. 3.2.1.5 (text of Decreto 1990/2016 art. 1) - `raw/docs/oficiais/CO/2026-10-13-Decreto-780-2016-FuncionPublica.html` |
| IBC = mesada (T2R2-039) | Decreto 780/2016 art. 2.2.1.1.2.1 (same local file) |
| Electronic modality, 20+ pensioners (Report Matrix, File Structure) | Decreto 780/2016 art. 3.2.3.9 (same local file) |
| Deadline (Report Matrix) | Decreto 780/2016 art. 3.2.2.1 (same local file) - see open item 8 |
| Scope (pensioners vs employees vs retirees), WT codes | `04-output/RA-PENSIONERS-PILA-2026-10-21.md`; `HANDOFF-2026-10-21.md` (BAU answers Q1, Q19); WT names from `04-output/*` (62154 'Monthly Retired Pension-6798'; 21645-21647 'Medical Plan - Healthcare Insurance (EPS) - Pensioner'; 21643 / 21648 / 21644 'Solidarity Pension Fund-Pensioner') |
| FSP 1% / 2% above 10 / 20 SMLMV (T2R2-036, 047; Field Options; Population Rules) | Ley 797/2003 art. 8 (new Ley 100 art. 27 num. 2 lit. d) - `raw/docs/oficiais/CO/2026-10-21-Ley-797-2003-SecretariaSenado.html` (Secretaría del Senado, md5 6083dab7a899235d457dba46fa50eef7), saved and read in round 2 |
| Electronic payroll cross-reference (Report Matrix) | Res. DIAN 000227/2025 art. 1.5.3.2.3, as quoted in the RA (not reopened here) |
| Layout and styles | Structural precedent `05-final/CO-PILA-003-AportesSeguridadSocial-Spec.xlsx` (styles copied cell by cell, no content) |
| SMLMV 2026 = 1,750,905 (worked example only) | Decreto 0159 de 2026 (transitional), as recorded in `paises/Colombia.md`; decree not reopened here |

## 2. AT3 v15 pages used

pp. 1-2 (incorporating acts up to Res. 1529/2026); pp. 3-6 (table of contents); p. 7 (ch. 1 s.0 files and justification rules; archivo tipo 1 campos 1-3); pp. 8-11 (archivo tipo 1 campos 4-27, total 482, July/January update); pp. 12-13 (§1.2.1-1.2.4: clase, naturaleza, tipo persona, tipo de pagador; §2 archivo tipo 2); pp. 14-16 (registro tipo 1, 18 campos, total 285); pp. 16-20 (§2.1.2.1-2.1.2.2: periods, planilla types P/R/L/C/V, 'INFORMACIÓN PAGADORES DE PENSIONES'); pp. 21-39 (registro tipo 2, 63 campos, total 519; payer ID differs from pensioner ID); pp. 39-40 (§2.2.2.1 BDUA names); pp. 40-47 (§2.2.2.2 pension types, IBC floors, FSP 1%/2%); p. 47 (§2.2.2.3 causante); pp. 48-49 (§2.2.2.4 pensioner types, type 9 record); pp. 49-51 (§2.2.2.5-2.2.2.9 abroad, ING, RET, VSP, SUS); pp. 51-52 (§2.2.2.10-2.2.2.13 days, IBC); pp. 52-59 (§2.2.2.14-2.2.2.17 pension, Ley 2381 distribution); pp. 59-62 (§2.2.2.18-2.2.2.21 FSP); pp. 62-64 (§2.2.2.22-2.2.2.28 health, UPC, CCF, mesada, total mesada); pp. 65-72 (ch. 2 operator totals records 3-7, headings only); pp. 99-108 (ch. 4 §1-§6: R01, R02, R03, R04, table 8, R6 - read on the rendered pages); pp. 108-109 (§7 IBC floors, §8 health to FOSYGA/MIN001); pp. 109-113 (§9 health rates of pensioners); pp. 126-133 (ch. 5, items 5.22-5.32).

## 3. Open items - NOT LOCATED or conflicting (kept out of the spec as rules)

1. **Health band 2-3 SMLMV - open only on the Government 'reglamentación'.** The spec gives the rate by contribution period: 2020-2021 8% / 10% (>1-2) / 12% (>2); 2022-2023 4% / 10% (>1-2) / 12% (>2); from 2024 4% / 10% (>1-3) / 12% (>3) (Ley 100 art. 204 par. 5 with Ley 2294/2023 art. 78; Res. MSPS 1271/2023 art. 1 nums. 3-5, AT1). AT3 v15 ch. 4 §9 (p. 113) prints '2022 en adelante 4% 10% 12%' with no band limits, so it does not contradict the 2024 bands, and Res. 1271/2023 is listed among the acts incorporated in AT3 v15 (p. 2). The only point still open: Ley 2294 art. 78 makes the 2-3 SMLMV reduction apply 'previa reglamentación del Gobierno nacional'; that reglamentación was NOT LOCATED. Res. 1271/2023 already sets the 2024 bands for PILA reporting, and BAU applies the same bands (HANDOFF-2026-10-21 Q1).
2. **Health period (T2R1-011).** AT3 says only "Obligatorio. Formato año y mes (aaaa-mm). Lo suministra el pagador de pensiones." It does not state whether the pensioners' health period runs one month ahead of campo 10, as it does for employees under AT2. NOT LOCATED. The sample uses the same month in both fields.
3. **Campo 15 (tipo de identificación del causante).** The field table says "Obligatorio", while §2.2.2.3 limits the causante block to pension types 2-7. The spec marks it C. Confirm with the operator's validation for type 10 / 13 records (blank expected).
4. **Campo 62 Correcciones.** The field table says blank "para planillas diferentes a L - Reliquidaciones", while §2.1.2.2 (p. 19) requires A and C records in planilla **V**. The spec states both.
5. **Archivo tipo 1 campo 23.** Printed positions 422-440 (19 positions) for a 20-position field; campo 24 starts at 442 and the total is 482, so the spec uses 422-441.
6. **Rate layout.** AT3 prints the decimal layout only for campo 51 (2.0% = 0.02000, p. 63). The layout of campos 40 and 48 is not printed; the spec sends it to the operator's file-format configuration, and the sample uses the campo 51 pattern.
7. **Rounding wording.** AT3 §2.2.2.23 (p. 63) says contributions on an IBC below 1 SMLMV are approximated "al múltiplo de cien más cercano" under art. 3.2.1.5, whose text says "múltiplo de 100 superior más cercano". The spec follows the decree (round UP).
8. **Deadline day numbers.** The local copy of Decreto 780 art. 3.2.2.1 shows the 15 NIT bands (00-07 ... 94-99) but not the business-day column. The spec states the rule without the day numbers. NOT LOCATED in the local file.
9. **Campo 7 vs campo 8 document types.** Campo 8 (and 16, 54) lists a length rule for PC (PEP-TUTOR, up to 16), but PC is not in the campo 7 / 15 / 53 value lists. The spec keeps the lists as printed.
10. **Table 8 vs field table.** Table 8 (p. 106) marks TAE and TDE as permitted for pension types 10 and 13, while the field table says campos 24-27 "Debe reportarse en blanco". The spec follows the field table (blank).
11. **Campo 47 subaccount wording.** Title "Subcuenta de Subsistencia", but §2.2.2.21 (p. 62) first says "el aporte se debe efectuar a la Subcuenta de Solidaridad ... FSP001" and then, for shared pensions, "Subcuenta de Subsistencia". The spec states the field and the FSP001 code only.
12. **Pension type 10 IBC floor.** Campo 9 (p. 24) says the mesada of types 10, 14 and 16 may be below 1 SMMLV; ch. 4 §7 (p. 109) and §2.2.2.2 (p. 43) give "Mayor o igual 1 SMLMV" for type 10. The spec states the ch. 4 §7 table.
13. **Client facts still needed:** which pension types the 454 pensioners hold (10 Jubilación, 13 Convencional, 11/14 para compartir, survivors 2-4); whether any pension is shared with Colpensiones (campo 10, pension fields); pensioner type 5 vs 6 (25 SMMLV cap); whether any pensioner contributes to a CCF; pensioners resident abroad; additional UPC beneficiaries; whether the payer is listed in 'INFORMACIÓN PAGADORES DE PENSIONES'; which of WT 21645 / 21646 / 21647 carries which health band and how 21643 / 21648 / 21644 split (attributes per WT belong in the WTC); nature of WT 62830 'Pensioner Allowance-6794' (2 pensioners, on top of 62154) - not mapped to any field; confirmation that the 21 retirees' WT 62151 is not a periodic pension.
14. **Not read locally:** Ley 1643/2013; Decreto 780 art. 2.1.3.17 (abroad, cited by AT3); Ley 2381/2024 arts. (cited by AT3 for campos 41, 46).
15. **Precedent finding (outside this spec).** The worked example of CO-PILA-003 (and its Sample File) uses NIT 900123456-**7**; the DIAN check digit of 900123456 is **8** (weights 3,7,13,17,19,23,29,37,41: sum 586, mod 11 = 3, DV = 11 - 3 = 8). This spec uses 900123456-8.

## 4. Checks run (2026-10-21)

- `validate_workbook.py --artifact RSPEC`: FAIL blocker=1 major=6, all C12/columns on the spec sheet row 1 (title row above the header row 2) - the same pattern as CO-PILA-003; no C29 residual markers.
- WORDS of `scripts/make_final.py` over all cells: 0 hits. Formula cells: 0. Columns T / U: empty.
- Position integrity asserted in the builder: 27 / 18 / 63 fields, contiguous positions, totals 482 / 285 / 519; sample record lengths 482 / 285 / 519 / 519; example arithmetic (10% and 12% health, 1% FSP, header total) asserted.

## 5. Round 2 (2026-10-21) - fixes from `CO-PILA-007-verification.json`

| # | Cell | Before | After |
|---|---|---|---|
| 1 (major) | PILA Pensioners Spec!M107 (T2R2-048) | "From January 2020 ... 1 SMLMV 4%; more than 1 and up to 3 SMLMV 10%; more than 3 SMLMV 12% (... Res. 1271/2023 art. 1 ...)" | Rate by contribution period: 2020-2021 8% / 10% (>1-2) / 12% (>2); 2022-2023 4% / 10% (>1-2) / 12% (>2); from 2024 4% / 10% (>1-3) / 12% (>3) (Res. 1271/2023 art. 1 nums. 3-5); R, L and V planillas use the rate in force for the period reported; source adds AT3 §2.1.2.2 p. 20 |
| 2 | Field Options D65:D67 | "4% (...)", "10% (... from 2024)", "12% (same sources)" | "4% for periods from January 2022 (8% in 2020-2021)", "10% for periods from January 2024 ... For periods 2020-2023 the 10% band is more than 1 and up to 2 SMLMV", "12% for periods from January 2024 ... For periods 2020-2023 the 12% band starts above 2 SMLMV" |
| 3 | Population Rules C9 | "Select the rate on campo 63: a mesada of 1 SMLMV 4%; ... 3 SMLMV 12% (...)" | "Select the rate on campo 63 for the contribution period: from January 2024 ... ; periods 2020-2023 as in T2R2-048" |
| 4 | Payroll Scope Summary C16 | "Rate on the total mesada: 1 SMLMV 4%; ..." | "Rate on the total mesada, for contribution periods from January 2024: ...; earlier periods as in T2R2-048" |
| 5 | PILA Pensioners Spec!M108 (T2R2-049) | "Where the IBC is below 1 SMLMV the value is approximated to a multiple of 100 under Decreto 780 de 2016 art. 3.2.1.5." | "Campo 48 x campo 39, rounded UP to the next multiple of 100 (Decreto 780 de 2016 art. 3.2.1.5 num. 2), also where the IBC is below 1 SMLMV." (now consistent with column P) |
| 6 | Payroll Scope Summary C9 | "... The FSP contribution above 10 SMLMV still applies." | "... The exemption covers the health contribution only; the FSP contribution above 10 SMLMV still applies (AT3 v15 §2.2.2.21, pp. 61-62)." |
| 7 | Payroll Scope Summary A12; Population Rules D4 | "...retirement bonus in instalments (WT 62151)"; "Instalments of a retirement bonus (WT 62151) are not a pension..." | WT 62151 removed from both cells (it feeds no field) |
| 8 (consistency, same rule as #1) | Report Matrix, "CONTRIBUTIONS SETTLED" health bullet | "rate by total mesada 4% / 10% / 12%" | "rate by total mesada and contribution period, from January 2024 4% / 10% / 12% ..., earlier periods as in T2R2-048" |
| 9 | This file, item 1 | Stated a conflict AT3 v15 vs Res. 1271/2023 | Rewritten: AT3 p. 113 prints no band limits; open point is only the Ley 2294 art. 78 reglamentación |
| 10 | raw/docs/oficiais/CO | Ley 797/2003 not saved locally | `2026-10-21-Ley-797-2003-SecretariaSenado.html` saved; art. 8 (new Ley 100 art. 27 num. 2 lit. d) read: >10 to 20 SMLMV 1%, >20 SMLMV 2% to the subsistence subaccount - matches the spec |

Checks after round 2: 108 fields, positions contiguous, totals 482 / 285 / 519; sample 482 / 285 / 519 / 519; WORDS 0; formulas 0; T/U empty; no '62151' in any cell; `validate_workbook --artifact RSPEC` FAIL blocker=1 major=6, all C12 title-row (same pattern as CO-PILA-003); C29 0.
