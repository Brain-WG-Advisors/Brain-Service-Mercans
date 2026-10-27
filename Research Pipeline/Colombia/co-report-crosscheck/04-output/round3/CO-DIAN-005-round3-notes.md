# CO-DIAN-005 (Formato 2276 v4) - round-3 cross-check notes (17 Oct 2026)

Companion files: `CO-DIAN-005-crosscheck-r3.json` (48 spec rows, one verdict each) and `CO-DIAN-005-changemap-r3-PROPOSED.json` (46 proposed cell edits, 11 items deliberately not applied). No spec and no masked file was edited.

## 1. What the file is and how it was analysed

**File:** [[Research Pipeline/Colombia/co-report-crosscheck/03-client-reports-masked/round3/Formato 2276 - Preliminar - Envio - 16oct.xlsx|Formato 2276 - Preliminar - Envio - 16oct.xlsx]], sheet `2276`, header row 1, 1035 beneficiary records (rows 2-1036) plus a totals row (row 1037), 45 columns A-AS. Identity columns C-H are masked (digit-substituted IDs, NAME_/ADDRESS_ tokens); codes I-K and amounts are real. No residual PII was found (profile + spot checks on shape only).

**Column set:** A-AS are exactly the 45 attributes of the DIAN technical specification (Anexo T3.45: entinfo, tdocb, nitb, pap, sap, pno, ono, dir, dpto, mun, pais, pasa, paec, pabop, vaex, paho, pase, paco, papre, pavia, paga, patra, vapo, potro, cein, ceco, auce, peju, tingbtp, apos, apof, aprais, apov, apafc, apavc, vare, ivav, rfiva, pagahuvt, vilap, tdocde, nitde, identfc, tdocpcc, nitpcc) in annex order; the resolution's 36 numerals map onto them with numerals 2, 3, 4, 34 and 36 split, as the spec describes. Only the column labels differ in wording; one label is wrong (column AM, see section 3).

**Official sources reached.** `dian.gov.co` / normograma could not be read in full and the Res. 162/2023 annex on sisjur.bogotajuridica.gov.co failed (certificate error; the file obtained was another annex). Two reliable mirrors were used instead: (a) the PDF of Res. 000227/2025 Título 3 (cijuf.org.co) - art. 1.3.7.1.1 numerals 1-36, parágrafos 1-7 (the article is the compiled Res. 162/2023 art. 51 as amended by Res. 188/2024 art. 8) and the formats table (T3.45 = Formato 2276 versión 4); (b) the Diario Oficial 53.254 (25 Sep 2025) text of Anexo T3.45 (enlegislacion.com), with the full attribute table (type, length, criteria) and the XSD. Every verdict cites these; nothing is marked 'annex not verified online'.

**Method.** pandas/openpyxl on the masked workbook: value shapes and distinct values of every column; per-column statistics (rows > 0, sums, min/max, negatives, decimals, share of values ending in 000); arithmetic check of AC against L..AB; population classes (salary / pension / neither); cross-field tests (Y vs Z, AN vs Y/Z, AJ/AC ratio, doc type vs population); a person-level join to the Accumulated Report (masked IDs are consistent across files: 908 of 1038 Accumulated persons matched, pensioners mostly through the 'Beneficiary National Id' column) to test the wage-type routing and the period; a comparison with the client's Form 220 working file (round 2). Only counts, ratios and amounts are quoted; no identity value is printed anywhere.

**What the file turns out to be: the FULL tax year 2025, not a 2026 year-to-date extract.** Evidence: (i) on 448 matched pensioners column AB = exactly 14 x the December-2025 monthly pension (WT 62154) = 12 mesadas + 2 additional mesadas (WT 62153); a rolling Oct-25..Sep-26 window would give about 14.45 because of the 2026 increase; (ii) the pensioner 'otros pagos' (column X) = exactly 12 x the December-2025 EPS-offset compensation (WT 62155); (iii) column N (numeral 7) ~ 11.7 x the December-2025 meal allowance (WT 65818); (iv) every amount is >= the Oct-Dec 2025 months of the matching wage types (e.g. health 833 of 835 persons, salary 376 of 376); (v) the records sit in the same identity order as the client's Form 220 working file for 2025-01-01..2025-12-31. Consequence: the brief's expected reconciliation of column AJ to the Jan-Sep 2026 Accumulated Report (WT 2552 = 14,928,096,127; WT 21140 = 48,229,727; WT 21155 does not exist in the catalogue; total 14,976,325,854) against AJ = 13,926,475,000 compares different years and proves nothing; per person the 2025 figures are >= the Oct-Dec 2025 months for 366 of 371 matched persons (5 exceptions for the client to explain). The 2026 return must be built from 1 Jan-31 Dec 2026 payment-date accumulators, as the spec already says.

**Population:** 460 records with salary (numeral 5 > 0, active employees and 2025 leavers), 512 employer-paid pensioner records (numeral 21 > 0), 63 records with neither (leavers/others paid only settlements or benefits: 61 with 'otros pagos', 24 with a meal allowance, 25 with withholding, 3 with severance paid). No record has both salary and pension; no record has a zero total. Document types: 13 CC x 1015, 22 CE x 18, 12 TI x 2 (both TI records are pensioners - survivor beneficiaries who are minors, which the spec's identity rule covers).

## 2. Findings that change the spec (annex basis) - all in the change map

1. **Field Length of every amount attribute = 18** (annex: long 18, XSD `[0-9]{1,18}`); the spec says 14 on 29 rows (9-21, 23-25, 27-28, 30-35, 37-39, 41-42).
2. **Identification numbers are string 20** (nitb, nitde, nitpcc); the spec says 2 + 16 on rows 5, 43, 45. **Fideicomiso identfc = string 14, digits only** (row 44: 'Var' / 'AN'). **entinfo = int 2** (row 4: '1').
3. **Country sub-field is a numeric code** (annex pais int 4, 'de acuerdo con los definidos por resolución'); the client's file carries 169 (Colombia) on every record. Row 7: Field Length 'Var (country)' -> '4 (country code)', Example 'Colombia' -> '169', address length 200, DANE codes with leading zeros ('debe incluir los ceros a la izquierda'); one sentence appended to the Field Explanation; Sample File A46 and Example Analysis A10 aligned.
4. **XML header (element Cab):** the annex carries `Ano` = year of SENDING and the tax year as `FecInicial` / `FecFinal`; the spec's ENV-03 maps the tax year to a single AAAA value. Sentence appended to M49; the mandatory header attributes (Ano, CodCpt, Formato, Version, NumEnvio, FecEnvio, FecInicial, FecFinal, ValorTotal, CantReg) added to File Structure B9. Note the annex's own definition of ValorTotal ('sumatoria del atributo tdocb') is quoted as published.
5. **Numeral 33 'blank' -> 'zero'** (Population Rules C29): attribute vilap is 'Siempre debe diligenciarse' and par. 2 requires 0; the client's file correctly writes 0 on 684 records.
6. **Payroll Scope Summary: new YES row for the employer-paid pensioner** (A50:C50, appended). The sheet has only a NO row for fund-paid pensioners, while 49% of the client's records are employer-paid pensioners; the row restates the N17/N21/N23/N24/N29 rules already in the spec sheet (pension incl. additional mesadas in 21, EPS offset in 17, health on pension in 23, solidarity in 24, nil withholding below 1,000 UVT/month).

Confirmations (no change): numeral 1 = 1 and numerals 35/36 blank (par. 4); 4 name columns, blank second surname / other names allowed; numeral 22 = sum of numerals 5-21 on 1035 of 1035 records; numerals 19 and 20 mutually exclusive (20 is zero everywhere); every Z > 0 record also has Y > 0 (January interest), 69 leaver records have Y without Z; health on 511 of 512 pensioners (apos), solidarity on 2 (apof); zero withholding on every pensioner (ET art. 206 num. 5); 14 records with AJ/AC ~ 20% (4 with a foreign document) - the spec's non-resident control fires on real data; format/version 2276 / 4 fixed in the XSD; unique key (entinfo + tdocb + nitb + ...) satisfied (no duplicate identification).

## 3. Client errors / preliminary-file issues NOT replicated into the spec

| # | Issue | Evidence | Official rule the spec keeps |
|---|---|---|---|
| C1 | Every amount is rounded to thousands | 100% of non-zero values in all 15 populated amount columns end in 000 (e.g. L: 460 of 460) | Annex: 'valor positivo, entero, sin puntos ni comas', values 'según lo reportado por el informante'; no rounding prescribed. Apparently inherited from Form 220 figures. |
| C2 | Meal allowance reported entirely in numeral 7 (column N, 447 persons = the WT 65818 recipients); numerals 8 and 32 zero on every record | N ~ 11.7 x the monthly WT 65818; O and AM = 0 | Res. 227 numerals 8 and 32, par. 1 and 6; ET art. 387-1: monthly fork at 310 UVT, split at 41 UVT (spec rows 11, 12, 41). |
| C3 | Numeral 33 populated on 52 records without severance paid/deposited; zero on 5 records with severance | AN > 0 on 351 salary records, 299 with Y or Z > 0 | Res. 227 numeral 33 'Únicamente para trabajadores que aplique el numeral 4 art. 206 E.T.'. |
| C4 | 50 pensioner records with no first name (47 also without other names) | column F blank on 50 rows, all with numeral 21 > 0 | Annex: pno 'Siempre debe diligenciarse', XSD required / minLength 1 - the records would be rejected. |
| C5 | Column AM header reads 'mayor a 41 UVT' | header text | Annex attribute pagahuvt / numeral 32 = 'Pagos por alimentación mensuales hasta 41 UVT'. Probably why the column is empty (see C2). |
| C6 | 31 records with department 25, municipality 001 (DIVIPOLA 25001 = Agua de Dios), 29 of them active employees | columns I/J | Looks like a default municipality where only Cundinamarca is known; the spec requires DIVIPOLA-validated codes. |
| C7 | Numeric 0 written in the optional attributes AO-AS | 0 on all rows | Annex: optional ('si se conoce'); omit/empty in the XML; '0' is not a document-type code. |
| C8 | All voluntary pension contributions in numeral 26, none in numeral 25 | AF = 0, AG > 0 on 43 records | Shows the client's current classification only; the art. 55 / 126-1 attribute stays an open point (N25, 16 Oct). |
| C9 | 5 persons whose 2025 withholding (AJ) is below their Oct-Dec 2025 withholding in the Accumulated Report | person-level join | Reversal/correction to be explained; no spec impact. |
| C10 | Totals row at the bottom of the sheet | row 1037 | Working artefact; the XML uses CantReg / ValorTotal. |

## 4. Questions for the client

1. Confirm that the file is the Formato 2276 of tax year 2025 (filed in 2026) and whether it was accepted by DIAN as sent (thousand-rounded amounts, 50 records without first name).
2. Meal allowance (WT 65818 'Meal Allowance Inf.', deduction 21115): is it paid through vouchers/cards (bonos de servicio) or to a food supplier? Why are numerals 8 and 32 nil for every employee, including the 10 person-months above 41 UVT and the employees above 310 UVT found in 2026? (open since round 1)
3. Numeral 33: on what basis is the six-month average populated for 52 employees without severance paid or deposited, and omitted for 5 with severance?
4. How is the six-month average computed (which wage types, last six months of employment on termination)? The file shows about 1.1 x average monthly salary.
5. Municipality for the 31 Cundinamarca records coded 25/001: real location or default?
6. First name missing on 50 pensioner records: is the pensioner master data incomplete, or are these records keyed to an entity/estate?
7. The 5 persons whose 2025 withholding is below their Oct-Dec 2025 withholding: reversal, correction or a different beneficiary record?
8. Which February deposit feeds numeral 19 in the 2025 file (February 2025, i.e. year of deposit, as the spec assumes)?
9. Numeral 25 vs 26: confirm that every '(FVOL)' and institutional-plan wage type is an ET art. 126-1 contribution (the file reports all of it in numeral 26).

## 5. Verdict counts (48 spec rows)

| Verdict | Rows | Notes |
|---|---|---|
| Aligned | 9 | 8 section headers + ENV-04 (format/version) |
| Format mismatch | 18 | annex lengths/types (14 -> 18, 16 -> 20, identfc 14, entinfo 2, country code) on rows whose data is zero or whose only issue is the declared shape |
| Conflict | 18 | populated amount rows (thousand rounding C1 on all of them) plus the specific client deviations C2 (rows 11, 12, 41), C3 (row 42), C4 (row 6) |
| Explanation to improve | 1 | ENV-03 (header Ano vs FecInicial/FecFinal) |
| Not evidenced | 2 | ENV-01 NIT, ENV-02 taxpayer category |

Every Conflict is a client-side deviation from the official text; no Conflict required a change to a spec rule. Change map: 46 cell edits (29 of them the Field Length 14 -> 18), 11 items not applied.

## 6. Verification outcome (independent verifier, 17 Oct 2026) and application

`CO-DIAN-005-verification-r3.json`: 90 items checked, agreement 0.967; 45 of the 46 proposed edits confirmed against the Anexo T3.45 attribute table and XSD (Diario Oficial 53.254), 0 overturned, 1 for Wallisson.
- WITHDRAWN: finding C9 and client question 7 (5 persons with 2025 withholding below Oct-Dec 2025): not reproducible - the differences are at most 473 pesos, i.e. the thousand rounding.
- ADDED: row 50 (ENV-04 Format and version) is a Format mismatch, not Aligned: the annex header carries Formato int 5 and Version int 2, the spec said 'Var' -> Field Length '5 + 2' (I50).
- CORRECTED EVIDENCE: row 12 (numeral 8) must be read on 2025 data - two employees at or below 310 UVT have a month above 41 UVT with numeral 8 = 0; rows 11 / 41: 96 meal recipients earn above 310 UVT, so the Conflict covers about 327 records, not 447.
- HELD FOR WALLISSON (not applied): Payroll Scope Summary A50:C50 (new YES row for the employer-paid pensioner). The proposed C50 text puts every non-pension payment to a pensioner (incl. the monthly EPS-offset WT 62155) in numeral 17, while N17 (M21) and N21 (M27) limit numeral 17 to one-off payments; decide whether N17/N21 are broadened or C50 says 'one-off'.
- APPLIED onto [[Research Pipeline/Colombia/co-report-crosscheck/05-final/CO-DIAN-005-Formato2276-Spec.xlsx|CO-DIAN-005-Formato2276-Spec.xlsx]] (previous copy in `05-final/_previous/`): the 43 remaining cell edits plus I50, via `04-output/final-prep/CO-DIAN-005-round3-map.json` and `make_final.py --on-final`. The M7 sentence was applied without the clause referring to the client's file (delivery standard: no client observations in the spec).
