# Lituânia: specs GPM313 v1.2 e GPM312 v1.2 (correções da validação de 28/10)

> Hub [[Lituania]] · Validação: [[Research Pipeline/Lithuania/2026-10-28-validacao/VAL-GPM313-GPM312|VAL-GPM313-GPM312]] · Passe de bastão: [[Research Pipeline/Lithuania/2026-10-28-validacao/PASSE-DE-BASTAO|PASSE-DE-BASTAO]] · Base: [[Research Pipeline/Lithuania/2026-10-27-reports/CONFERENCIA|CONFERENCIA 27/10]]

- **Data:** 2026-10-29. **Escopo:** só arquivos locais. Drive, tickets e e-mail não foram tocados; nada em `raw/` nem nos arquivos v1.1 foi alterado.
- **Bases:** `2026-10-27-reports/LT-VMI-001-GPM313-Spec_v1.1.xlsx` (md5 `3ee4f2db5f34c23f7bef083d231017e6`) e `LT-VMI-002-GPM312-Spec_v1.1.xlsx` (md5 `4a13365c74371cdb5f0580beddb21195`), idênticas ao Drive (CONFERENCIA 28/10).
- **Fontes primárias:** `raw/docs/oficiais/LT/2026-10-27-VMI-reports/x_GPM313_mxfd/GPM313.mxfd` (script VBScript de 342 linhas) e `x_GPM312_mxfd/GPM312.mxfd` (3 981 linhas); `x_IN_GPM312_DOC/IN_GPM312.docx`; `x_IN_GPM313_DOC/IN_GPM313_nuo_2026.docx`. As linhas citadas ("l. N") são do ScriptModule de cada MXFD, numeração a partir de 1 (a mesma do relatório de validação).
- **Método de edição:** `inspect_workbook.py` mostrou 9 desenhos (vazios) e `xl/persons/person.xml` no GPM313. Por isso as duas specs foram editadas por XML+zip (lxml), sem `openpyxl.save`. Desenhos, persons, larguras, congelamento, fontes e bordas ficaram iguais (diff de estilo v1.1 × v1.2 = 0).
- **Destaque:** o azul `FFDDEBF7` que marcava a v1.1 foi retirado (55 células no GPM313, 105 no GPM312). Cada célula voltou ao preenchimento que tinha na v1.0 (`specs-drive/`), na mesma coordenada; isso inclui as Field Options B11-B13 do GPM313 (achado m8). Agora o azul marca só a v1.2: 35 células no GPM313 e 90 no GPM312, incluindo os 3 títulos de seção (Spec A2/A10/A27), que trocaram o cinza `FFD6DCE4` pelo azul (R2 da revalidação). Conferido: azul = alterado, sem sobra dos dois lados.
- **Version Control:** nova linha 4, v1.2, `2026-10-29` (ISO, como as linhas acima; texto curto, R3). Na linha 3 (v1.1), o texto "No change to the content rules" foi trocado pela lista do que a v1.1 de fato mudou (achado m7).

## Alterações célula a célula

Nos textos longos aparece só o trecho que mudou; `[…]` indica o texto que não mudou.

| Arquivo!Aba!Célula | Antes (v1.1) | Depois (v1.2) | Fonte (arquivo + linha/regra) | Achado |
|---|---|---|---|---|
| GPM313!GPM313 Spec!J3 | `Numeric, 9 or 11 digits` | Numeric, 9, 10 or 11 digits (MXFD script l. 20: 9 = legal-entity code, 10 = code assigned by VMI, 11 = personal code) | GPM313.mxfd l. 20 | m1 |
| GPM313!GPM313 Spec!K3 | `302123456` | `302123442` | GPM313.mxfd l. 197-213 (ID_formatas_simple_f); GPM312.mxfd l. 1209-1210, 3843-3866 (JAR_tikrinimas) | B1 |
| GPM313!GPM313 Spec!K9 | `184250.00` | `184250,00` | GPM313.mxfd/GPM312.mxfd FieldDataDef DecimalSeparator ','; script l. 6 SetDefaultDecimalSeparator "," | M3 |
| GPM313!GPM313 Spec!K10 | `31322.50` | `31322,50` | GPM313.mxfd/GPM312.mxfd FieldDataDef DecimalSeparator ','; script l. 6 SetDefaultDecimalSeparator "," | M3 |
| GPM313!GPM313 Spec!K11 | `0.00` | `0,00` | GPM313.mxfd/GPM312.mxfd FieldDataDef DecimalSeparator ','; script l. 6 SetDefaultDecimalSeparator "," | M3 |
| GPM313!GPM313 Spec!K13 | `12000.00` | `12000,00` | GPM313.mxfd/GPM312.mxfd FieldDataDef DecimalSeparator ','; script l. 6 SetDefaultDecimalSeparator "," | M3 |
| GPM313!GPM313 Spec!K14 | `2400.00` | `2400,00` | GPM313.mxfd/GPM312.mxfd FieldDataDef DecimalSeparator ','; script l. 6 SetDefaultDecimalSeparator "," | M3 |
| GPM313!GPM313 Spec!K15 | `0.00` | `0,00` | GPM313.mxfd/GPM312.mxfd FieldDataDef DecimalSeparator ','; script l. 6 SetDefaultDecimalSeparator "," | M3 |
| GPM313!Example Analysis!A2 | `302123456` | `302123442` | GPM313.mxfd l. 197-213 (ID_formatas_simple_f); GPM312.mxfd l. 1209-1210, 3843-3866 (JAR_tikrinimas) | B1 |
| GPM313!Example Analysis!A6 | `184250.00` | `184250,00` | GPM313.mxfd/GPM312.mxfd FieldDataDef DecimalSeparator ','; script l. 6 SetDefaultDecimalSeparator "," | M3 |
| GPM313!Example Analysis!A7 | `31322.50` | `31322,50` | GPM313.mxfd/GPM312.mxfd FieldDataDef DecimalSeparator ','; script l. 6 SetDefaultDecimalSeparator "," | M3 |
| GPM313!Example Analysis!A8 | `0.00` | `0,00` | GPM313.mxfd/GPM312.mxfd FieldDataDef DecimalSeparator ','; script l. 6 SetDefaultDecimalSeparator "," | M3 |
| GPM313!Example Analysis!A9 | `12000.00` | `12000,00` | GPM313.mxfd/GPM312.mxfd FieldDataDef DecimalSeparator ','; script l. 6 SetDefaultDecimalSeparator "," | M3 |
| GPM313!Example Analysis!A10 | `2400.00` | `2400,00` | GPM313.mxfd/GPM312.mxfd FieldDataDef DecimalSeparator ','; script l. 6 SetDefaultDecimalSeparator "," | M3 |
| GPM313!Example Analysis!A11 | `0.00` | `0,00` | GPM313.mxfd/GPM312.mxfd FieldDataDef DecimalSeparator ','; script l. 6 SetDefaultDecimalSeparator "," | M3 |
| GPM313!Example Analysis!D2 | Illustrative - see the note on Sample File. Rule 7.1 states no length; Lithuanian legal-entity codes are 9 digits and resident individual TINs are 11 digits, so both lengths are valid in this box. | Illustrative - see the note on Sample File. Rule 7.1 states no length; the MXFD accepts 9, 10 or 11 digits (script l. 20) and checks the check digit (ID_formatas_simple_f, l. 197-325). 302123442 is a fictitious 9-digit code that passes that check. | GPM313.mxfd l. 197-213 (ID_formatas_simple_f); GPM312.mxfd l. 1209-1210, 3843-3866 (JAR_tikrinimas) | B1 |
| GPM313!Example Analysis!D5 | `[…] This return would be due by 15 August 2026 under rule 12 […]` | […] Under rule 12 this return is due by the 15th of the following month: 15 August 2026, which is a Saturday. No primary source held for this build states whether the deadline moves to the next working day (the Law on Tax Administration is not in the source folder), so the date is kept as written and the point stays open […] | IN_GPM313_nuo_2026.docx regra 12; calendário (2026-08-15 = sábado) | m3 (marcado, não corrigido) |
| GPM313!Sample File!B6 | `  1  Mokesčio mokėtojo identifikacinis numeris ...... 302123456` | `  1  Mokesčio mokėtojo identifikacinis numeris ...... 302123442` | GPM313.mxfd l. 197-213 (ID_formatas_simple_f); GPM312.mxfd l. 1209-1210, 3843-3866 (JAR_tikrinimas) | B1 |
| GPM313!GPM313 Spec!J9 | `Decimal, 2 dp` | `Decimal, 2 dp; decimal separator ',' (MXFD DecimalSeparator; FFData value e.g. 1234,56)` | GPM313.mxfd/GPM312.mxfd FieldDataDef DecimalSeparator ','; script l. 6 SetDefaultDecimalSeparator "," | M3 |
| GPM313!GPM313 Spec!J10 | `Decimal, 2 dp` | `Decimal, 2 dp; decimal separator ',' (MXFD DecimalSeparator; FFData value e.g. 1234,56)` | GPM313.mxfd/GPM312.mxfd FieldDataDef DecimalSeparator ','; script l. 6 SetDefaultDecimalSeparator "," | M3 |
| GPM313!GPM313 Spec!J11 | `Decimal, 2 dp` | `Decimal, 2 dp; decimal separator ',' (MXFD DecimalSeparator; FFData value e.g. 1234,56)` | GPM313.mxfd/GPM312.mxfd FieldDataDef DecimalSeparator ','; script l. 6 SetDefaultDecimalSeparator "," | M3 |
| GPM313!GPM313 Spec!J13 | `Decimal, 2 dp` | `Decimal, 2 dp; decimal separator ',' (MXFD DecimalSeparator; FFData value e.g. 1234,56)` | GPM313.mxfd/GPM312.mxfd FieldDataDef DecimalSeparator ','; script l. 6 SetDefaultDecimalSeparator "," | M3 |
| GPM313!GPM313 Spec!J14 | `Decimal, 2 dp` | `Decimal, 2 dp; decimal separator ',' (MXFD DecimalSeparator; FFData value e.g. 1234,56)` | GPM313.mxfd/GPM312.mxfd FieldDataDef DecimalSeparator ','; script l. 6 SetDefaultDecimalSeparator "," | M3 |
| GPM313!GPM313 Spec!J15 | `Decimal, 2 dp` | `Decimal, 2 dp; decimal separator ',' (MXFD DecimalSeparator; FFData value e.g. 1234,56)` | GPM313.mxfd/GPM312.mxfd FieldDataDef DecimalSeparator ','; script l. 6 SetDefaultDecimalSeparator "," | M3 |
| GPM313!GPM313 Spec!J17 | `Decimal, 2 dp` | `Decimal, 2 dp; decimal separator ',' (MXFD DecimalSeparator; FFData value e.g. 1234,56)` | GPM313.mxfd/GPM312.mxfd FieldDataDef DecimalSeparator ','; script l. 6 SetDefaultDecimalSeparator "," | M3 |
| GPM313!GPM313 Spec!J18 | `Decimal, 2 dp` | `Decimal, 2 dp; decimal separator ',' (MXFD DecimalSeparator; FFData value e.g. 1234,56)` | GPM313.mxfd/GPM312.mxfd FieldDataDef DecimalSeparator ','; script l. 6 SetDefaultDecimalSeparator "," | M3 |
| GPM313!Version Control!E3 | `[…] No change to the content rules […]` | […] Also changed in v1.1 (log completed in v1.2): boxes 5-7 Mandatory Y -> C with Conditional Reason (F9-F11, G9-G11); month without a leading zero (7, not 07) in J7, K7, O7, Field Options B2-B10, Example Analysis A5 and Sample File B9 […] | diff v1.0 × v1.1 do relatório de validação | m7 |
| GPM313!File Structure!C8 | `(texto da v1.1)` | […] + « Each page also carries the form's system fields B_FormNr (6 cells) and B_FormVerNr (2 cells), IsRequired = false; they identify the form and its version and are not populated from payroll.» | GPM313.mxfd/GPM312.mxfd FieldDataDefs B_FormNr (6/7 células) e B_FormVerNr (2), IsRequired=false | m2 |
| GPM313!Population Rules!C5 | `(texto da v1.1)` | […] + « Rule 21: where the foreign tax on such treaty-state employment income is paid in a LATER month of the same tax period than the month the income was paid (so the income was first declared here with GPM withheld), the payer may remove the double taxation by filing an amended return for the month of payment; those payments then count as non-taxable employment payments and are no longer declared in that return.» | IN_GPM313_nuo_2026.docx regra 21 | M6 |
| GPM313!Population Rules!C11 | `(texto da v1.1)` | […] + « Rule 21 adds a further amendment case: employment income paid to a resident employee for work in a treaty state, taxed here in the month of payment, on which foreign tax was paid in a later month of the same tax period - the payer may file an amended return for the month of payment, from which those payments are removed as non-taxable.» | IN_GPM313_nuo_2026.docx regra 21 | M6 |
| GPM313!Version Control!A4 | (vazio) | `LT-VMI-001` | — | linha v1.2 (R3: data ISO, texto curto) |
| GPM313!Version Control!B4 | (vazio) | `1.2` | — | linha v1.2 (R3: data ISO, texto curto) |
| GPM313!Version Control!C4 | (vazio) | `2026-10-29` | — | linha v1.2 (R3: data ISO, texto curto) |
| GPM313!Version Control!D4 | (vazio) | `Mercans Global Compliance` | — | linha v1.2 (R3: data ISO, texto curto) |
| GPM313!Version Control!E4 | (vazio) | Validation fixes 2026-10-28: payer code passes MXFD check; decimal comma; box 1 accepts 9-11 digits; rule 21 added; 15 Aug 2026 deadline (Saturday) flagged open. | — | linha v1.2 (R3: data ISO, texto curto) |
| GPM312!GPM312 Spec!J3 | `Numeric, 9 or 11 digits` | Numeric, 9, 10 or 11 digits (MXFD script l. 1204: 9 = legal-entity code, 10 = code assigned by VMI, 11 = personal code) | GPM312.mxfd l. 1204-1205 | m1 |
| GPM312!GPM312 Spec!J12 | `Numeric, 9 or 11 digits` | Numeric, 9, 10 or 11 digits (MXFD script l. 1204: 9 = legal-entity code, 10 = code assigned by VMI, 11 = personal code) | GPM312.mxfd l. 1204-1205 | m1 |
| GPM312!GPM312 Spec!J29 | `Numeric, 9 or 11 digits` | Numeric, 9, 10 or 11 digits (MXFD script l. 1204: 9 = legal-entity code, 10 = code assigned by VMI, 11 = personal code) | GPM312.mxfd l. 1204-1205 | m1 |
| GPM312!GPM312 Spec!K3 | `302123456` | `302123442` | GPM313.mxfd l. 197-213 (ID_formatas_simple_f); GPM312.mxfd l. 1209-1210, 3843-3866 (JAR_tikrinimas) | B1 |
| GPM312!GPM312 Spec!K12 | `302123456` | `302123442` | GPM313.mxfd l. 197-213 (ID_formatas_simple_f); GPM312.mxfd l. 1209-1210, 3843-3866 (JAR_tikrinimas) | B1 |
| GPM312!GPM312 Spec!K29 | `302123456` | `302123442` | GPM313.mxfd l. 197-213 (ID_formatas_simple_f); GPM312.mxfd l. 1209-1210, 3843-3866 (JAR_tikrinimas) | B1 |
| GPM312!GPM312 Spec!K6 | `2211000.00` | `200600,00` | GPM312.mxfd l. 1265-1311 (setcheckvalue G4/G5); IN_GPM312.docx regras 14-15 | M2 |
| GPM312!GPM312 Spec!K7 | `392000.00` | `16660,00` | GPMI IX-1007 suvestinė 2026-06-11 art. 2(16)(4) e art. 5(4)(5); IN_GPM312 regras 49 (último §) e 50.2.1; GPM312.mxfd l. 2946 (0 aceito p/ U5 01); GPM312.mxfd l. 1265-1311 | R1 + M2 |
| GPM312!GPM312 Spec!K8 | `0.00` | `0,00` | GPM313.mxfd/GPM312.mxfd FieldDataDef DecimalSeparator ','; script l. 6 SetDefaultDecimalSeparator "," | M3 |
| GPM312!GPM312 Spec!K9 | `0.00` | `0,00` | GPM313.mxfd/GPM312.mxfd FieldDataDef DecimalSeparator ','; script l. 6 SetDefaultDecimalSeparator "," | M3 |
| GPM312!GPM312 Spec!J14 | `Numeric 11, or alphanumeric for the fallbacks` | Numeric, 10 or 11 digits when L2 = 1 (MXFD script l. 1465-1480: 11 = personal code checked by AK_tikrinimas, 10 = code assigned by VMI); alphanumeric for the fallbacks | GPM312.mxfd l. 1465-1480 | m1 |
| GPM312!GPM312 Spec!K14 | `39001010101` | `39001010109` | GPM312.mxfd l. 3751-3841 (AK_tikrinimas), l. 1474-1483 | M4 |
| GPM312!GPM312 Spec!K21 | `42000.00` | `42000,00` | GPM313.mxfd/GPM312.mxfd FieldDataDef DecimalSeparator ','; script l. 6 SetDefaultDecimalSeparator "," | M3 |
| GPM312!GPM312 Spec!K22 | `20.00` | `20,00` | GPM313.mxfd/GPM312.mxfd FieldDataDef DecimalSeparator ','; script l. 6 SetDefaultDecimalSeparator "," | M3 |
| GPM312!GPM312 Spec!K23 | `8400.00` | `8400,00` | GPM313.mxfd/GPM312.mxfd FieldDataDef DecimalSeparator ','; script l. 6 SetDefaultDecimalSeparator "," | M3 |
| GPM312!GPM312 Spec!K24 | `0.00` | `0,00` | GPM313.mxfd/GPM312.mxfd FieldDataDef DecimalSeparator ','; script l. 6 SetDefaultDecimalSeparator "," | M3 |
| GPM312!GPM312 Spec!K25 | `DE` | (vazio) | padrão da coluna K (K19, K20, K36 em branco) | R7 |
| GPM312!GPM312 Spec!K26 | `0.00` | `0,00` | GPM313.mxfd/GPM312.mxfd FieldDataDef DecimalSeparator ','; script l. 6 SetDefaultDecimalSeparator "," | M3 |
| GPM312!GPM312 Spec!K31 | `LT100001234567` | (vazio) | IN_GPM312 regra 42, último §, e 43 (U1/U2 vazios); GPM312.mxfd l. 2538-2540 | R4 (alinhado à amostra) |
| GPM312!GPM312 Spec!K32 | `3` | (vazio) | GPM313.mxfd/GPM312.mxfd FieldDataDef DecimalSeparator ','; script l. 6 SetDefaultDecimalSeparator "," | M3 |
| GPM312!GPM312 Spec!K38 | `96000.00` | `96000,00` | GPM313.mxfd/GPM312.mxfd FieldDataDef DecimalSeparator ','; script l. 6 SetDefaultDecimalSeparator "," | M3 |
| GPM312!GPM312 Spec!K39 | `20.00` | `0,00` | GPMI IX-1007 suvestinė 2026-06-11 art. 2(16)(4) e art. 5(4)(5); IN_GPM312 regras 49 (último §) e 50.2.1; GPM312.mxfd l. 2946 (0 aceito p/ U5 01) | R1 |
| GPM312!GPM312 Spec!K40 | `19200.00` | `0,00` | GPMI IX-1007 suvestinė 2026-06-11 art. 2(16)(4) e art. 5(4)(5); IN_GPM312 regras 49 (último §) e 50.2.1; GPM312.mxfd l. 2946 (0 aceito p/ U5 01) | R1 |
| GPM312!GPM312 Spec!K41 | `0.00` | `0,00` | GPM313.mxfd/GPM312.mxfd FieldDataDef DecimalSeparator ','; script l. 6 SetDefaultDecimalSeparator "," | M3 |
| GPM312!GPM312 Spec!J21 | `Decimal, 2 dp (whole euro for stakes)` | `Decimal, 2 dp; decimal separator ',' (MXFD DecimalSeparator); whole euro for stakes` | GPM313.mxfd/GPM312.mxfd FieldDataDef DecimalSeparator ','; script l. 6 SetDefaultDecimalSeparator "," | M3 |
| GPM312!GPM312 Spec!J38 | `Decimal, 2 dp (whole euro for stakes)` | `Decimal, 2 dp; decimal separator ',' (MXFD DecimalSeparator); whole euro for stakes` | GPM313.mxfd/GPM312.mxfd FieldDataDef DecimalSeparator ','; script l. 6 SetDefaultDecimalSeparator "," | M3 |
| GPM312!GPM312 Spec!T6 | Confirm that EDS itself excludes 'C'-marked stake rows from box 4, or whether the filer must compute the reduced total. | Answered by the MXFD script (l. 1273-1276 and 1290-1293): EDS recomputes box 4 as the sum of L8/U8 on lines whose L7/U7 is not 'C', so stake rows are excluded automatically, and the declared box 4 must equal that sum. | GPM312.mxfd l. 1273-1276, 1290-1293 | m6 |
| GPM312!GPM312 Spec!T31 | Confirm whether EDS accepts a U annex line with U1 and U2 both empty, and what matching key it then uses. | Answered by the MXFD script (l. 2538-2540): U1 and U2 may both be left empty; an error arises only when one of them is filled and the other is not. | GPM312.mxfd l. 2538-2540 | m6 |
| GPM312!GPM312 Spec!T37 | Confirm the first tax period for which the 'U' marker is expected. Order VA-24 was published 2026-03-27 and the consolidated redaction runs from 2026-03-28, i.e. after the 2025 return deadline of 2026-02-16, which suggests first use on the 2026 annual return filed in 2027. | Answered by the MXFD script (l. 2863-2864): 'U' is accepted only for tax periods from 2026 (an earlier period gives an error), so it is first used on the 2026 return. | GPM312.mxfd l. 2863-2864 | m6 |
| GPM312!GPM312 Spec!F42 | `Y` | `C` | GPM312.mxfd FieldDataDef U12-n/U15-n IsRequired=false; l. 2555-2558, 3237-3243, 3334-3348; IN_GPM312.docx regras 53, 56 | M1 |
| GPM312!GPM312 Spec!G42 | (vazio) | Required when U14 is a foreign state, U13 is empty and U2 is not 6: the MXFD script then gives the error 'turi būti užpildyti U12 ir / ar U13' (l. 3237-3243). Must be left EMPTY when U2 = 6 (error, l. 2555-2558). MXFD IsRequired = false. Send it whenever the date of birth is held (rule 53). | GPM312.mxfd FieldDataDef U12-n/U15-n IsRequired=false; l. 2555-2558, 3237-3243, 3334-3348; IN_GPM312.docx regras 53, 56 | M1 |
| GPM312!GPM312 Spec!F45 | `Y` | `C` | GPM312.mxfd FieldDataDef U12-n/U15-n IsRequired=false; l. 2555-2558, 3237-3243, 3334-3348; IN_GPM312.docx regras 53, 56 | M1 |
| GPM312!GPM312 Spec!G45 | (vazio) | Filled with the foreign residential address of an individual resident abroad (rule 56). Must be left EMPTY when U2 = 6 (error, MXFD l. 2555-2558). Where U14 is a foreign state and U15 is empty the script gives only a warning (l. 3334-3348, 3426). MXFD IsRequired = false. | GPM312.mxfd FieldDataDef U12-n/U15-n IsRequired=false; l. 2555-2558, 3237-3243, 3334-3348; IN_GPM312.docx regras 53, 56 | M1 |
| GPM312!Field Options!E70 | […] . U ANNEX ONLY (rule 43.6) - used for the rules 37-38 cases where interest, dividends or royalties were paid to an entity that distributed them without disclosing the owner list. U2 = 6; there is no L2 = 6 […] | […]  (rule 43.6). U ANNEX ONLY - there is no L2 = 6. For tax periods from 2026 the MXFD accepts U2 = 6 only with U5 = 62, 67, 51 or 52 (script l. 2566-2570): royalties paid to a foreign collective rights management association (rule 38, code 62), interest paid to an entity that did not disclose its owner list (rule 37, code 67), and performer or sportsperson income paid to a third party acting for the performer or sportsperson (new rule 36-1, codes 52/51). Dividends (26) paid to an intermediary are accepted only on the 2025 return (rule 37 second paragraph: payments 2025-01-01 to 2025-06-30). With U2 = 6, U12, U13 and U15 are left empty (l. 2555-2558) […] | GPM312.mxfd l. 2555-2575; IN_GPM312.docx regras 36-1, 37 (2º §), 38, 43.6 | M5 |
| GPM312!Example Analysis!A2 | `302123456` | `302123442` | GPM313.mxfd l. 197-213 (ID_formatas_simple_f); GPM312.mxfd l. 1209-1210, 3843-3866 (JAR_tikrinimas) | B1 |
| GPM312!Example Analysis!A4 | `39001010101` | `39001010109` | GPM312.mxfd l. 3751-3841 (AK_tikrinimas), l. 1474-1483 | M4 |
| GPM312!Example Analysis!C4 | Eleven-digit Lithuanian personal code used as the resident's taxpayer identification number. | Eleven-digit Lithuanian personal code used as the resident's taxpayer identification number. Fictitious: first digit 3 = male born 1900-1999, birth date 1990-01-01, check digit valid under AK_tikrinimas (MXFD l. 3751-3841). | GPM312.mxfd l. 3751-3841 (AK_tikrinimas), l. 1474-1483 | M4 |
| GPM312!Example Analysis!A12 | `42000.00` | `42000,00` | GPM313.mxfd/GPM312.mxfd FieldDataDef DecimalSeparator ','; script l. 6 SetDefaultDecimalSeparator "," | M3 |
| GPM312!Example Analysis!A13 | `20.00` | `20,00` | GPM313.mxfd/GPM312.mxfd FieldDataDef DecimalSeparator ','; script l. 6 SetDefaultDecimalSeparator "," | M3 |
| GPM312!Example Analysis!A14 | `8400.00` | `8400,00` | GPM313.mxfd/GPM312.mxfd FieldDataDef DecimalSeparator ','; script l. 6 SetDefaultDecimalSeparator "," | M3 |
| GPM312!Example Analysis!A15 | `0.00` | `0,00` | GPM313.mxfd/GPM312.mxfd FieldDataDef DecimalSeparator ','; script l. 6 SetDefaultDecimalSeparator "," | M3 |
| GPM312!Example Analysis!D17 | […] , used for the rules 37-38 cases where interest or dividends were paid to an entity that did not disclose its owner list […] | […] . For tax periods from 2026 the MXFD accepts it only with U5 = 62, 67, 51 or 52 (script l. 2566-2570): royalties to a foreign collective rights association (rule 38), interest to an entity that did not disclose its owner list (rule 37) and performer or sportsperson income paid to a third party (new rule 36-1). Dividends (26) only on the 2025 return (rule 37 second paragraph). On such a line U12, U13 and U15 stay empty (l. 2555-2558) […] | GPM312.mxfd l. 2555-2575; IN_GPM312.docx regras 36-1, 37 (2º §), 38, 43.6 | M5 |
| GPM312!File Structure!C9 | `[…] four […]` | `[…] three […]` | IN_GPM312.docx 2 priedas (seções 1, 2 e 3) | m9 |
| GPM312!Sample File!B2 | […] using the decimal comma that Lithuanian forms display. It illustrates the line-splitting grain (person x class x type x rate x in-kind), the L7 'M' and U7 'U' markers, the L1 passport composite key, and the U2 = 6 entity case […] | […] with the decimal comma of the MXFD (DecimalSeparator ','), each annex value under its label. It illustrates the line-splitting grain (person x class x type x rate x in-kind), the L7 'M' and U7 'U' markers and the L1 business-certificate identifier (L2 = 2). The payer code and the personal codes are fictitious and pass the MXFD check-digit functions; boxes 4-7 equal the sums of the annex lines (MXFD l. 1265-1311) […] | coerência com as linhas da amostra | B3/M3/M4/m4 |
| GPM312!Sample File!B6 | `  1  Mokesčių mokėtojo identifikacinis numeris ....... 302123456` | `  1  Mokesčių mokėtojo identifikacinis numeris ....... 302123442` | GPM313.mxfd l. 197-213 (ID_formatas_simple_f); GPM312.mxfd l. 1209-1210, 3843-3866 (JAR_tikrinimas) | B1 |
| GPM312!Sample File!B9 | `  4  Bendra išmokų suma (L8 + U8 sumos) ........... 2211000,00` | `  4  Bendra išmokų suma (L8 + U8 sumos) ........... 200600,00` | GPM312.mxfd l. 1265-1311 (setcheckvalue G4/G5); IN_GPM312.docx regras 14-15 | M2 |
| GPM312!Sample File!B10 | `  5  Bendra išskaičiuota GPM suma (L10 + U10) ....... 392000,00` | `  5  Bendra išskaičiuota GPM suma (L10 + U10) ....... 16660,00` | GPMI IX-1007 suvestinė 2026-06-11 art. 2(16)(4) e art. 5(4)(5); IN_GPM312 regras 49 (último §) e 50.2.1; GPM312.mxfd l. 2946 (0 aceito p/ U5 01); GPM312.mxfd l. 1265-1311 | R1 + M2 |
| GPM312!Sample File!B14 | `=============================================================================` | ————————————————————————————————————————————————————————————————————————————— | regra do Drive: texto começando com '=' vira #ERROR! na importação (CONFERENCIA 28/10) | Drive #ERROR! |
| GPM312!Sample File!B16 | `  1  302123456          3  2026` | `  1  302123442          3  2026` | GPM313.mxfd l. 197-213 (ID_formatas_simple_f); GPM312.mxfd l. 1209-1210, 3843-3866 (JAR_tikrinimas) | B1 |
| GPM312!Sample File!B18 | `  L1           L2 L3               L4 L5 L6 L7        L8    L9      L10   L11` | `  L1            L2 L3                L4 L5 L6 L7 L8         L9    L10       L11` | necessário para leitura mecânica pelo check_gpm (valor sob o rótulo); valores iguais | M3 (L9/U9 com vírgula) |
| GPM312!Sample File!B28 | `=============================================================================` | ————————————————————————————————————————————————————————————————————————————— | regra do Drive: texto começando com '=' vira #ERROR! na importação (CONFERENCIA 28/10) | Drive #ERROR! |
| GPM312!Sample File!B30 | `  1  302123456          3  2026` | `  1  302123442          3  2026` | GPM313.mxfd l. 197-213 (ID_formatas_simple_f); GPM312.mxfd l. 1209-1210, 3843-3866 (JAR_tikrinimas) | B1 |
| GPM312!Sample File!B32 | `  U1              U2 U3          U4 U5 U6 U7        U8   U9     U10   U11` | `  U1              U2 U3            U4 U5 U6 U7 U8         U9    U10       U11` | necessário para leitura mecânica pelo check_gpm (valor sob o rótulo); valores iguais | M3 (L9/U9 com vírgula) |
| GPM312!Sample File!B33 | `  U12        U13            U14  U15` | `  U12         U13             U14  U15` | necessário para leitura mecânica pelo check_gpm (valor sob o rótulo); valores iguais | M3 (L9/U9 com vírgula) |
| GPM312!Sample File!B35 | `                                 John Smith  A 01     U    96000,00  20  19200,00  0,00` | `                     John Smith    A  01    U  96000,00   0,00  0,00      0,00` | GPMI IX-1007 suvestinė 2026-06-11 art. 2(16)(4) e art. 5(4)(5); IN_GPM312 regras 49 (último §) e 50.2.1; GPM312.mxfd l. 2946 (0 aceito p/ U5 01) | R1 |
| GPM312!Sample File!B36 | `  1985-03-12   DE12345678901  DE   Musterstrasse 1, 10115 Berlin, Germany` | `  1985-03-12  DE12345678901   DE   Musterstrasse 1, 10115 Berlin, Germany` | necessário para leitura mecânica pelo check_gpm (valor sob o rótulo); valores iguais | M3 (L9/U9 com vírgula) |
| GPM312!Sample File!B38 | `  LT100001234567   6 AB Brokeris  A 26        250000,00  15  37500,00  0,00` | (vazio) | GPM312.mxfd l. 2555-2570, 2512-2534 (3 erros na linha U2=6/U5=26 em 2026) | B3 |
| GPM312!Sample File!B39 | `  --         --             LT   Konstitucijos pr. 1, Vilnius, Lietuva` | (vazio) | GPM312.mxfd l. 2555-2570, 2512-2534 (3 erros na linha U2=6/U5=26 em 2026) | B3 |
| GPM312!Sample File!B20 | `  39001010101   1 Jonas Jonaitis    A 01           42000,00  20  8400,00  0,00` | `  39001010109   1  Jonas Jonaitis    A  01       42000,00   20,00 8400,00   0,00` | GPM312.mxfd l. 3751-3841 (AK) + DecimalSeparator ',' | M4 + M3 |
| GPM312!Sample File!B21 | `  39001010101   1 Jonas Jonaitis    A 03            1200,00  15   180,00  0,00` | `  39001010109   1  Jonas Jonaitis    A  03       1200,00    15,00 180,00    0,00` | GPM312.mxfd l. 3751-3841 (AK) + DecimalSeparator ',' | M4 + M3 |
| GPM312!Sample File!B22 | `  38505054321   1 Rita Ritaite      A 01  N        38000,00  20  7600,00  0,00` | `  48505054322   1  Rita Ritaite      A  01       38000,00   20,00 7600,00   0,00` | IN_GPM312 regra 28 (L6 só para pagamento em espécie) | R5 |
| GPM312!Sample File!B23 | `  38505054321   1 Rita Ritaite      A 01  A         2400,00  20   480,00  0,00` | `  48505054322   1  Rita Ritaite      A  01 A     2400,00    20,00 480,00    0,00` | GPM312.mxfd l. 3751-3841 (AK) + DecimalSeparator ',' | M4 + M3 |
| GPM312!Sample File!B24 | `  47712120987   1 Petras Petraitis  A 44        M  15000,00  20  3000,00  0,00` | `  37712120987   1  Petras Petraitis  B  77    M  15000,00   0,00  0,00      0,00` | IN_GPM312.docx regra 29.2 e 2 priedas item 2.8.17 (código 77, classe B quando a MB paga o próprio membro); regra 31.2.2 (L9 = 0); GPM312.mxfd l. 3751-3841 | m5 + M4 |
| GPM312!Sample File!B25 | `  AB 1234567    5 Ona Onaite        B 92            6000,00   0      0,00  0,00` | `  VL123456      2  Ona Onaite        B  92       6000,00    0,00  0,00      0,00` | IN_GPM312.docx regra 23, 2º §; GPM312.mxfd l. 1485-1495 (verslo_nr) | m4 |
| GPM312!GPM312 Spec!J6 | `Decimal, 2 dp` | `Decimal, 2 dp; decimal separator ',' (MXFD DecimalSeparator; FFData value e.g. 1234,56)` | GPM313.mxfd/GPM312.mxfd FieldDataDef DecimalSeparator ','; script l. 6 SetDefaultDecimalSeparator "," | M3 |
| GPM312!GPM312 Spec!J7 | `Decimal, 2 dp` | `Decimal, 2 dp; decimal separator ',' (MXFD DecimalSeparator; FFData value e.g. 1234,56)` | GPM313.mxfd/GPM312.mxfd FieldDataDef DecimalSeparator ','; script l. 6 SetDefaultDecimalSeparator "," | M3 |
| GPM312!GPM312 Spec!J8 | `Decimal, 2 dp` | `Decimal, 2 dp; decimal separator ',' (MXFD DecimalSeparator; FFData value e.g. 1234,56)` | GPM313.mxfd/GPM312.mxfd FieldDataDef DecimalSeparator ','; script l. 6 SetDefaultDecimalSeparator "," | M3 |
| GPM312!GPM312 Spec!J9 | `Decimal, 2 dp` | `Decimal, 2 dp; decimal separator ',' (MXFD DecimalSeparator; FFData value e.g. 1234,56)` | GPM313.mxfd/GPM312.mxfd FieldDataDef DecimalSeparator ','; script l. 6 SetDefaultDecimalSeparator "," | M3 |
| GPM312!GPM312 Spec!J23 | `Decimal, 2 dp` | `Decimal, 2 dp; decimal separator ',' (MXFD DecimalSeparator; FFData value e.g. 1234,56)` | GPM313.mxfd/GPM312.mxfd FieldDataDef DecimalSeparator ','; script l. 6 SetDefaultDecimalSeparator "," | M3 |
| GPM312!GPM312 Spec!J24 | `Decimal, 2 dp` | `Decimal, 2 dp; decimal separator ',' (MXFD DecimalSeparator; FFData value e.g. 1234,56)` | GPM313.mxfd/GPM312.mxfd FieldDataDef DecimalSeparator ','; script l. 6 SetDefaultDecimalSeparator "," | M3 |
| GPM312!GPM312 Spec!J26 | `Decimal, 2 dp` | `Decimal, 2 dp; decimal separator ',' (MXFD DecimalSeparator; FFData value e.g. 1234,56)` | GPM313.mxfd/GPM312.mxfd FieldDataDef DecimalSeparator ','; script l. 6 SetDefaultDecimalSeparator "," | M3 |
| GPM312!GPM312 Spec!J40 | `Decimal, 2 dp` | `Decimal, 2 dp; decimal separator ',' (MXFD DecimalSeparator; FFData value e.g. 1234,56)` | GPM313.mxfd/GPM312.mxfd FieldDataDef DecimalSeparator ','; script l. 6 SetDefaultDecimalSeparator "," | M3 |
| GPM312!GPM312 Spec!J41 | `Decimal, 2 dp` | `Decimal, 2 dp; decimal separator ',' (MXFD DecimalSeparator; FFData value e.g. 1234,56)` | GPM313.mxfd/GPM312.mxfd FieldDataDef DecimalSeparator ','; script l. 6 SetDefaultDecimalSeparator "," | M3 |
| GPM312!Population Rules!C15 | […]  is stated unconditionally by rule 53, with none of the 'may be left empty' escapes that rules 42, 43 and 54 give the other non-resident fields, so it must be treated as a hard requirement in the interface. U13 takes the foreign TIN, falling back to a foreign identity document number or another identification code from a document issued abroad, and may be left empty where the individual has none; rule 54 points to the European Commission TIN portals for structural checks of EU codes. U14 takes the country of residence, but rule 55 overrides it for the rules 37-38 entity cases, where it carries the residence of the DIVIDEND- or INTEREST-RECEIVING ENTITY rather than an individual. U15 takes the foreign residential address as free text […] | […] : rule 53 states it without a 'may be left empty' clause, but the MXFD (IsRequired = false) only requires U12 and/or U13 on a line where U14 is a foreign state and U2 is not 6 (error, script l. 3237-3243); the interface should send U12 whenever the date of birth is held. U13 takes the foreign TIN, falling back to a foreign identity document number or another identification code from a document issued abroad, and may be left empty where the individual has none (rule 54); rule 54 points to the European Commission TIN portals for structural checks of EU codes. U14 takes the country of residence; for the entity cases of rule 37 (interest; dividends only on the 2025 return) it carries the state of the receiving entity (rule 55), and LT is accepted only with U2 = 6 and U5 = 26, 62 or 67 (l. 3272-3279); since U2 = 6 with U5 = 26 is rejected for tax periods from 2026 (l. 2566-2570), only 62 or 67 remain in 2026. U15 takes the foreign residential address as free text; a missing U15 on a foreign-resident line gives only a warning (l. 3334-3348). With U2 = 6 (entity lines under rules 36-1, 37, 38) U12, U13 and U15 must be left empty (error, l. 2555-2558) […] | GPM312.mxfd FieldDataDef U12-n/U15-n IsRequired=false; l. 2555-2558, 3237-3243, 3334-3348; IN_GPM312.docx regras 53, 56 | M1 |
| GPM312!GPM312 Spec!A2 | `=== DEKLARACIJA GPM312 - PAGRINDINE FORMA / MAIN RETURN (boxes 1-7, rules 12-17) ===` | — DEKLARACIJA GPM312 - PAGRINDINE FORMA / MAIN RETURN (boxes 1-7, rules 12-17) — | regra do Drive: texto começando com '=' vira #ERROR! na importação (CONFERENCIA 28/10) | Drive #ERROR! |
| GPM312!GPM312 Spec!A10 | === GPM312L PRIEDAS - NUOLATINIAI LIETUVOS GYVENTOJAI / L ANNEX - RESIDENTS (rules 18-35; one line per class/type/rate combination) === | — GPM312L PRIEDAS - NUOLATINIAI LIETUVOS GYVENTOJAI / L ANNEX - RESIDENTS (rules 18-35; one line per class/type/rate combination) — | regra do Drive: texto começando com '=' vira #ERROR! na importação (CONFERENCIA 28/10) | Drive #ERROR! |
| GPM312!GPM312 Spec!A27 | === GPM312U PRIEDAS - NENUOLATINIAI LIETUVOS GYVENTOJAI / U ANNEX - NON-RESIDENTS (rules 36-56; note new rule 36-1 and new marker 'U' added by order VA-24 of 2026-03-26) === | — GPM312U PRIEDAS - NENUOLATINIAI LIETUVOS GYVENTOJAI / U ANNEX - NON-RESIDENTS (rules 36-56; note new rule 36-1 and new marker 'U' added by order VA-24 of 2026-03-26) — | regra do Drive: texto começando com '=' vira #ERROR! na importação (CONFERENCIA 28/10) | Drive #ERROR! |
| GPM312!GPM312 Spec!M42 | […] It is stated unconditionally by the order, with none of the 'may be left empty' escapes that rules 42, 43 and 54 attach to the other non-resident identification fields […] | […] Rule 53 states it without a 'may be left empty' clause, but the MXFD script treats it as conditional: required (with or instead of U13) on a foreign-resident line with U2 other than 6 (l. 3237-3243) and forbidden when U2 = 6 (l. 2555-2558) […] | GPM312.mxfd FieldDataDef U12-n/U15-n IsRequired=false; l. 2555-2558, 3237-3243, 3334-3348; IN_GPM312.docx regras 53, 56 | M1 |
| GPM312!GPM312 Spec!M45 | […] ; where rules 37 and 38 route an entity through the U annex this field carries that entity's address […] | […] . Where an entity is reported with U2 = 6 (rules 36-1, 37, 38) the MXFD forbids this field (l. 2555-2558), so no address is entered […] | GPM312.mxfd FieldDataDef U12-n/U15-n IsRequired=false; l. 2555-2558, 3237-3243, 3334-3348; IN_GPM312.docx regras 53, 56 | M1 |
| GPM312!Population Rules!C4 | `[…] 7 and 38 additionally place ENTITY identification numbers in U1 with U2 = 6 […]` | […] 6-1, 37 and 38 additionally place ENTITY identification numbers in U1 with U2 = 6; for tax periods from 2026 the MXFD accepts U2 = 6 only with U5 = 62, 67, 51 or 52 (script l. 2566-2570) and then forbids U12, U13 and U15 (l. 2555-2558) […] | GPM312.mxfd l. 2555-2575; IN_GPM312.docx regras 36-1, 37 (2º §), 38, 43.6 | M5 |
| GPM312!Population Rules!D4 | `[…] 7-38 taking U2 = 6 […]` | `[…] 6-1, 37 or 38 taking U2 = 6 (2026 domain: U5 62, 67, 51, 52) […]` | GPM312.mxfd l. 2555-2575; IN_GPM312.docx regras 36-1, 37 (2º §), 38, 43.6 | M5 |
| GPM312!Version Control!E3 | `[…] No change to the content rules […]` | […] Also changed in v1.1 (log completed in v1.2): boxes 4-6 Mandatory Y -> C with Conditional Reason (F6-F8, G6-G8); 2026 L9/U9 rate lists (J22, K22, J39, K39); Field Options E90 and E91; Population Rules C5 and D15; Example Analysis A13, A18 and D18; Sample File B2, B35 and B36 […] | diff v1.0 × v1.1 do relatório de validação | m7 |
| GPM312!Example Analysis!D16 | `(texto da v1.1)` | […] + « Such income is not Lithuanian-source for a non-resident (GPMI art. 2(16)(4) excludes income non-residents receive from activity in foreign states) and only Lithuanian-source employment income is taxed (GPMI art. 5(4)(5)); it is still declared (rule 49, last paragraph) with U9 = 0 and U10 = 0 (rule 50.2.1), so it adds to box 4 but not to box 5.» | GPMI IX-1007 suvestinė 2026-06-11 art. 2(16)(4) e art. 5(4)(5); IN_GPM312 regras 49 (último §) e 50.2.1; GPM312.mxfd l. 2946 (0 aceito p/ U5 01) | R1 |
| GPM312!File Structure!C10 | `(texto da v1.1)` | […] + « Each page also carries the form's system fields B_FormNr (6 or 7 cells) and B_FormVerNr (2 cells), IsRequired = false; they identify the form and its version and are not populated from payroll.» | GPM313.mxfd/GPM312.mxfd FieldDataDefs B_FormNr (6/7 células) e B_FormVerNr (2), IsRequired=false | m2 |
| GPM312!Example Analysis!D2 | Illustrative - see the note on Sample File. Rules 22 and 41 make the annex values a strict copy of the declaration value. | Illustrative - see the note on Sample File. Rules 22 and 41 make the annex values a strict copy of the declaration value. 302123442 is fictitious and passes the MXFD check (JAR_tikrinimas, l. 3843-3916). | GPM313.mxfd l. 197-213 (ID_formatas_simple_f); GPM312.mxfd l. 1209-1210, 3843-3866 (JAR_tikrinimas) | B1 |
| GPM312!Version Control!A4 | (vazio) | `LT-VMI-002` | — | linha v1.2 (R3: data ISO, texto curto) |
| GPM312!Version Control!B4 | (vazio) | `1.2` | — | linha v1.2 (R3: data ISO, texto curto) |
| GPM312!Version Control!C4 | (vazio) | `2026-10-29` | — | linha v1.2 (R3: data ISO, texto curto) |
| GPM312!Version Control!D4 | (vazio) | `Mercans Global Compliance` | — | linha v1.2 (R3: data ISO, texto curto) |
| GPM312!Version Control!E4 | (vazio) | Validation fixes 2026-10-28: valid payer/personal codes; 2026 U2 = 6 domain; U12/U15 conditional; U-marker abroad income untaxed; boxes 4-5 = line sums; decimal comma. | — | linha v1.2 (R3: data ISO, texto curto) |

## Achados: o que foi corrigido

| Achado | Situação |
|---|---|
| B1 código do pagador | Corrigido: `302123442` em todas as células listadas (GPM313 K3/A2/B6; GPM312 K3/K12/K29/A2/B6/B16/B30). Passa no `ID_formatas_simple_f` e no `JAR_tikrinimas` (soma 101, mod 11 = 2, dígito 2). |
| B2 PVM | Corrigido: o PVM inválido saiu. Na rodada R4, K31/K32 ficaram vazios, alinhados à amostra (John Smith sem U1/U2, regra 42, último §; l. 2538-2540). O `LT100000000014` passava no PVM_kodas, mas deixava os dois exemplos incoerentes. |
| B3 linha U de dividendos | Corrigido: linha removida da amostra (B38/B39 vazias). O U2 = 6 de 2026 está descrito em Example Analysis D17 e Field Options E70. |
| M1 U12/U15 | Corrigido: F42 e F45 = C, com G42/G45; M42/M45 e Population Rules C15 reescritos. |
| M2 caixas 4/5 | Corrigido: 200 600,00 e 16 660,00 (após R1), iguais às somas das linhas (K6/K7 e B9/B10). As somas mudaram também por B3 (linha U removida) e m5 (linha MB passou a classe B, L10 = 0). |
| M3 vírgula decimal | Corrigido: todos os exemplos Decimal com vírgula (coluna K, Example Analysis, Sample) e coluna J declarando o separador. |
| M4 códigos pessoais | Corrigido: `39001010109`, `48505054322` (Rita, 4 = feminino) e `37712120987` (Petras, 3 = masculino). Todos passam no `AK_tikrinimas` e estão marcados como fictícios (Example Analysis C4, Sample B2). |
| M5 U2 = 6 | Corrigido: domínio de 2026 (62/67/51/52) com a regra 36-1 em E70, C4, D4 e D17. |
| M6 regra 21 IN GPM313 | Corrigido: Population Rules C5 e C11. |
| m1 9/10/11 dígitos | Corrigido: J3/J12/J29 (e J3 do GPM313) e J14. |
| m2 B_FormNr/B_FormVerNr | Corrigido: File Structure C8 (GPM313) e C10 (GPM312). |
| m4 código 92 | Corrigido: L1 = 8 primeiros caracteres do verslo liudijimas (`VL123456`, fictício), L2 = 2 (regra 23, 2º §). Passa no `verslo_nr`. O exemplo de passaporte continua em Example Analysis A6. |
| m5 código 44 com M | Corrigido: linha passa a 77 / classe B / M, com L9 = 0 e L10 = 0 (regra 29.2; 2 priedas item 2.8.17: classe B quando a MB paga o próprio membro; regra 31.2.2). |
| m6 T6/T31/T37 | Corrigido: respondidas pelo script, com as linhas. O T37 não cita mais o "2026-02-16", e com isso some a incoerência apontada em m3. |
| m7 log da v1.1 | Corrigido: E3 das duas specs. |
| m8 azul sem alteração | Corrigido pela retirada geral do azul da v1.1. |
| m9 "four groups" | Corrigido: "three groups". |
| Drive `#ERROR!` | Corrigido: GPM312 Spec A2/A10/A27 agora começam com "— " e terminam com " —"; o fill cinza `FFD6DCE4` foi mantido. Sample B14/B28 viraram linha de "—". Nas duas specs, nenhuma célula começa com "=" (conferido pelo check). |
| R1 (revalidação) | Corrigido: a linha U7 = U (trabalho no exterior) passou a U9 = U10 = 0,00 (K39, K40, Sample B35). Caixa 5 = 16 660,00 (K7, B10), igual à ΣL10 (16 660) + ΣU10 (0); a caixa 4 continua 200 600,00. Explicação em Example Analysis D16: GPMI art. 2(16)(4) e art. 5(4)(5); regras 49 (último §) e 50.2.1. |
| R5 | Corrigido: a linha da Rita de 38 000,00 passou a pagamento em dinheiro (L6 vazio). A linha A (carro) ficou. |
| R6 | Corrigido: C15 agora diz que, em 2026, só 62/67 permitem U14 = LT (l. 2566-2570). |
| R7 | Corrigido: K25 vazio, como K19/K20/K36. |
| N1 (novo) | Achado pelo `check_gpm.py`: o exemplo K25 = `DE` (L12), na mesma linha de K22 = 20 % e K23 = 8 400, é rejeitado pelo script (l. 2121-2127/2287: L12 preenchido exige L9/L10/L11 = 0). K25 ficou vazio (R7); a regra continua descrita em G25. |

## O que ficou sem corrigir e por quê

1. **m3: prazo de 2026-08-15 (sábado) no GPM313** (Example Analysis D5, Sample B4).
   - A regra de passar para o dia útil seguinte está na Lei de Administração Tributária, que não está entre as fontes locais.
   - Por isso a data ficou como está e foi marcada como ponto aberto em D5.
   - Vai para o source-hunter.
2. **Tributação do salário de não residente por trabalho no exterior:** resolvida na rodada R1 (ver tabela acima). Conferida no GPMI local, art. 2(16)(4) e 5(4)(5), e não depende mais do source-hunter.
3. **Formato real do FFData.**
   - A vírgula vem do MXFD (DecimalSeparator e SetDefaultDecimalSeparator).
   - Ainda não há um FFData real exportado do EDS para confirmar a serialização. Resíduo de M3.
4. **Validações do servidor EDS** além do script do MXFD: não verificáveis localmente.
5. **Linha da Rita:** resolvida na rodada R5 (L6 vazio).
6. **Propagação** (encaminhamento da validação), não tocada nesta entrega:
   - o pagador `302123456` pode estar também na SAM e no LT-SIR-001;
   - a mudança de U12/U15 para C deve ser conferida no SIR e no DD.
7. **Drive e tickets:** nada foi importado.
   - O país está ativo (regra 9), então a alteração em produção pede ticket ao Development.
   - O import nos `.gsheet` (Replace) espera o ok do usuário.

## Limites do `check_gpm.py`

- Portadas literalmente:
  - funções de dígito verificador: `ID_formatas_simple_f`, `JAR_tikrinimas`, `TIN_tikrinimas`, `AK_tikrinimas`, `PVM_kodas`, `verslo_nr`, `IVPN`;
  - Sub GPM313 completa;
  - Sub GPM312: somas e `setcheckvalue`;
  - regras de linha L e U no ramo de período ≥ 2025/2026.
- As listas de códigos e taxas são lidas do próprio script pela linha citada. As 24 âncoras conferem que cada linha citada tem o trecho esperado.
- Não portados:
  - ramos de anos < 2025;
  - checagens de duplicidade (comentadas no próprio script);
  - o aviso fixo da l. 2376 (portal TIN da UE, emitido sempre que há página U).
- A regra de "sexo do código × nome" é heurística nossa (terminação do prenome lituano), não do MXFD.
- Teste negativo: rodado sobre as v1.1, o check dá `RESULTADO: FAIL - 90 erro(s), 33 aviso(s)`. Reproduz B1, B2, B3, M2, M3, M4, os "=" do Drive e o N1.

## Saída do `validate_workbook.py --artifact RSPEC`

```
FILE      LT-VMI-001-GPM313-Spec_v1.2.xlsx
ARTIFACT  RSPEC
CONTRACT  Report Spec (Spain 9-sheet standard)  [measured from report-spec-template/ES-M296-001_ResumenAnual_Spec.xlsx]
SHEETS    (9) ['Version Control', 'Report Matrix', 'Payroll Scope Summary', 'GPM313 Spec', 'File Structure', 'Field Options', 'Population Rules', 'Example Analysis', 'Sample File']
VERDICT   PASS  (blocker=0 major=0 minor=0)
exit=0
FILE      LT-VMI-002-GPM312-Spec_v1.2.xlsx
ARTIFACT  RSPEC
CONTRACT  Report Spec (Spain 9-sheet standard)  [measured from report-spec-template/ES-M296-001_ResumenAnual_Spec.xlsx]
SHEETS    (9) ['Version Control', 'Report Matrix', 'Payroll Scope Summary', 'GPM312 Spec', 'File Structure', 'Field Options', 'Population Rules', 'Example Analysis', 'Sample File']
VERDICT   PASS  (blocker=0 major=0 minor=0)
exit=0
```

## Saída do `check_gpm.py` (v1.2)

```
Ancoras do script conferidas: 24 (GPM313.mxfd 342 linhas, GPM312.mxfd 3981 linhas)
GPM313: 12 campos na coluna K, 12 no Example Analysis, 12 no Sample File; 747 celulas lidas
        valores: {'B_MM_ID': '302123442', 'B_MM_Pavadinimas': 'UAB Pavyzdys', 'B_ML_Metai': '2026', 'B_ML_Menuo': '7', 'G5': '184250,00', 'G6': '31322,50', 'G7': '0,00', 'G8': '12000,00', 'G9': '2400,00', 'G10': '0,00', 'G11': '', 'G12': ''}
GPM312: declaracao {'B_MM_ID': '302123442', 'B_ML_Metai': '2026', 'G4': '200600,00', 'G5': '16660,00', 'G6': '0,00', 'G7': '0,00'}; 6 linhas L e 1 linhas U na amostra; 1761 celulas lidas
         {'L1': '39001010109', 'L2': '1', 'L3': 'Jonas Jonaitis', 'L4': 'A', 'L5': '01', 'L8': '42000,00', 'L9': '20,00', 'L10': '8400,00', 'L11': '0,00', '_cell': 'B20'}
         {'L1': '39001010109', 'L2': '1', 'L3': 'Jonas Jonaitis', 'L4': 'A', 'L5': '03', 'L8': '1200,00', 'L9': '15,00', 'L10': '180,00', 'L11': '0,00', '_cell': 'B21'}
         {'L1': '48505054322', 'L2': '1', 'L3': 'Rita Ritaite', 'L4': 'A', 'L5': '01', 'L8': '38000,00', 'L9': '20,00', 'L10': '7600,00', 'L11': '0,00', '_cell': 'B22'}
         {'L1': '48505054322', 'L2': '1', 'L3': 'Rita Ritaite', 'L4': 'A', 'L5': '01', 'L6': 'A', 'L8': '2400,00', 'L9': '20,00', 'L10': '480,00', 'L11': '0,00', '_cell': 'B23'}
         {'L1': '37712120987', 'L2': '1', 'L3': 'Petras Petraitis', 'L4': 'B', 'L5': '77', 'L7': 'M', 'L8': '15000,00', 'L9': '0,00', 'L10': '0,00', 'L11': '0,00', '_cell': 'B24'}
         {'L1': 'VL123456', 'L2': '2', 'L3': 'Ona Onaite', 'L4': 'B', 'L5': '92', 'L8': '6000,00', 'L9': '0,00', 'L10': '0,00', 'L11': '0,00', '_cell': 'B25'}
         {'U3': 'John Smith', 'U4': 'A', 'U5': '01', 'U7': 'U', 'U8': '96000,00', 'U9': '0,00', 'U10': '0,00', 'U11': '0,00', '_cell': 'B35/B36', 'U12': '1985-03-12', 'U13': 'DE12345678901', 'U14': 'DE', 'U15': 'Musterstrasse 1, 10115 Berlin, Germany'}

== INFO ==
  [GPM312 Sample File] G4: declarado '200600,00' / soma das linhas 200600,00 -> ok   (GPM312 l.1308-1311 setcheckvalue)
  [GPM312 Sample File] G5: declarado '16660,00' / soma das linhas 16660,00 -> ok   (GPM312 l.1308-1311 setcheckvalue)
  [GPM312 Sample File] G6: declarado '0,00' / soma das linhas 0,00 -> ok   (GPM312 l.1308-1311 setcheckvalue)
  [GPM312 Sample File] G7: declarado '0,00' / soma das linhas 0 -> ok   (GPM312 l.1308-1311 setcheckvalue)

== AVISOS (el_warning: nao impedem a entrega no EDS) ==
  [GPM313 Spec col. K] campos 5-12 vazios = declarar que nada foi pago: G11,G12   (GPM313 l.86)
  [GPM313 Example Analysis] campos 5-12 vazios = declarar que nada foi pago: G11,G12   (GPM313 l.86)
  [GPM313 Sample File] campos 5-12 vazios = declarar que nada foi pago: G11,G12   (GPM313 l.86)
  [GPM312 Spec col. K linha U] Pasitikrinkite U1/U13/U12/U15 (algum vazio)   (GPM312 l.3426)
  [GPM312 Spec col. K] periodo corrente: aviso de ano (versao do MXFD de 2026-06-12)   (GPM312 l.1244-1247)
  [GPM312 Example Analysis (ID)] periodo corrente: aviso de ano (versao do MXFD de 2026-06-12)   (GPM312 l.1244-1247)
  [GPM312 Sample File!B25] individual-activity code: se pago pelo empregador, L7 = D   (GPM312 l.1659/2276)
  [GPM312 Sample File!B35/B36] Pasitikrinkite U1/U13/U12/U15 (algum vazio)   (GPM312 l.3426)
  [GPM312 Sample File] periodo corrente: aviso de ano (versao do MXFD de 2026-06-12)   (GPM312 l.1244-1247)

== ERROS ==

RESULTADO: PASS - 0 erro(s), 9 aviso(s)
```

Sobre os avisos (todos `el_warning`, que não bloqueiam o envio):
- **G11/G12 vazios (GPM313 l. 86):** a regra 4 permite caixa vazia ou zero. A classe B está fora do escopo do payroll.
- **"Período corrente" (GPM312 l. 1244-1247):** esta versão do MXFD (2026-06-12) avisa em qualquer declaração do ano em curso. Some na versão usada em 2027.
- **Código 92 sem L7 (l. 1659/2276):** lembrete de marcar D quando quem paga é o empregador. Não se aplica à amostra.
- **U1/U2 vazios na linha U (l. 3426), na amostra e na coluna K:** a regra 42, último parágrafo, permite.

## md5 dos arquivos entregues

| Arquivo | md5 |
|---|---|
| LT-VMI-001-GPM313-Spec_v1.2.xlsx | `61285401c648581bdcf48df88b6edfcc` |
| LT-VMI-002-GPM312-Spec_v1.2.xlsx | `243500940fe0a3469e0ea7abc0b22075` |
| check_gpm.py | `11b6622bbeaa239fd74be936dcc4701e` |

## Frentes

| Data | Frente | O quê |
|---|---|---|
| 2026-10-29 | pipeline (subagente) | Geração das specs v1.2 em local, `check_gpm.py` e este changelog. Sem Drive e sem ticket. |
| 2026-10-29 | pipeline (subagente) | Rodada 2: R1–R7 do [[Research Pipeline/Lithuania/2026-10-29-correcoes/REVAL-GPM-v1.2\|REVAL-GPM-v1.2]], nas mesmas v1.2, a partir da v1.1 (azul = alterado em relação à v1.1). |
