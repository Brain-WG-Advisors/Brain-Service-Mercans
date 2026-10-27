# Log de comparação célula a célula: SR-108 SNHI v1.1 → v1.2

Base: `C:/Users/instituto/Documents/brain-service/raw/docs/drive-exports/2026-10-27/TW - SNHI report specification.xlsx`
Nova: `TW - SNHI report specification_v1.2.xlsx`
Gerado: 2026-10-27 10:57

## 1. Partes do pacote
- `xl/worksheets/sheet1.xml`: alterada (esperado)
- `xl/worksheets/sheet2.xml`: alterada (esperado)
- `xl/worksheets/sheet3.xml`: alterada (esperado)
- `xl/styles.xml`: alterada (esperado)
- 29 partes; 25 idênticas byte a byte; 4 alteradas (só as 4 esperadas)

## 2. XML das folhas sem as células editadas
- `xl/worksheets/sheet1.xml`: idêntico fora das 5 células editadas
- `xl/worksheets/sheet2.xml`: idêntico fora das 11 células editadas
- `xl/worksheets/sheet3.xml`: idêntico fora das 41 células editadas
- `xl/styles.xml`: só acrescentou 1 fill (FFDDEBF7) e os xf clonados no fim; resto idêntico

## 3. XML bem formado
- todas as partes .xml/.rels da v1.2 passam no parser

## 4. Célula a célula (valor, preenchimento, fonte, borda, alinhamento, formato)
- `Version Control`: 26104 células comparadas
- `Report Matrix`: 96 células comparadas
- `Spec(TXT)`: 24024 células comparadas
- `Testing`: 14 células comparadas
- `Options`: 18 células comparadas
- Report Matrix!B23: itens 1, 2 e 4 preservados; item 3 
- aba Testing intocada: sim

## 5. Diferenças encontradas (todas devem estar na lista)
| Aba | Célula | Antes | Depois |
|---|---|---|---|
| Version Control | B15 |  | 1.2 |
| Version Control | C15 |  | 2026-10-27 00:00:00 |
| Version Control | D15 |  | Spec review against the NHIA TXT layout for income type 62 and the Supplementary Premium Regulations: section C totals = sum of the detail lines (not YTD); U... |
| Version Control | E15 |  | Draft |
| Version Control | F15 |  | Wallisson Gomes |
| Report Matrix | B5 |  | Period, Tax Year |
| Report Matrix | B6 | Quarterly | Period |
| Report Matrix | B8 | ASCII | BIG5 (NHIA: data code ASCII and BIG5; numeric/code fields single-byte, name fields in full-width characters) |
| Report Matrix | B11 |  | Section A (withholding unit): 1 line per file. Section B (detail): 1 line per bonus payment with SNHI withheld. Section C (totals): 1 line per file = totals ... |
| Report Matrix | B12 | Manual: Submit hardcopies offline | Electronic: Upload online  |
| Report Matrix | B13 |  | Not applicable (TXT data file; name fields in Traditional Chinese, full-width) |
| Report Matrix | B15 |  | Category 1 insured employees of the entity (active and terminated) who received a bonus in the period. A bonus paid after termination is included (4x the ins... |
| Report Matrix | B16 |  | Proposed (inference from Regulations art. 10, which requires the detail of the premium withheld): bonus payments with SNHI employee premium withheld (2558 > ... |
| Report Matrix | B17 |  | TWD (whole NT$, no decimals) |
| Report Matrix | B21 |  | Detail declaration (扣費明細) of the supplementary NHI premium withheld on bonuses, income type 62: the part of the bonus paid by the employee's own insured unit... |
| Report Matrix | B23 |         1.        Type N fields = numbers, right-aligned, pad left with zeros /         2.        Type C fields = characters, left-aligned, pad right with sp... |         1.        Type N fields = numbers, right-aligned, pad left with zeros /         2.        Type C fields = characters, left-aligned, pad right with sp... |
| Spec(TXT) | B24 | Social Security Integrate Number | Insured Unit Code (投保單位代號) |
| Spec(TXT) | E14 | 8628407.0 | 08628407 |
| Spec(TXT) | E36 | 0000000000002869420 | 00000000000000286942 |
| Spec(TXT) | E37 | 000000000000210127 | 0000000000002101 |
| Spec(TXT) | E38 | 065866#1111 | 27065866#1111 |
| Spec(TXT) | F6 | Format: yyyymm, cannot span across years | Format: yyymm (ROC year = Gregorian year - 1911, e.g. 11406 = June 2025); earliest payment month of the detail lines in the file; cannot span across years |
| Spec(TXT) | F7 | Format: yyyymm, cannot span across years | Format: yyymm (ROC year); latest payment month of the detail lines in the file; same year as the start month |
| Spec(TXT) | F8 | Format: yyyymmdd | Format: yyymmdd (ROC year, 7 characters) |
| Spec(TXT) | F18 | Format: yyyymmdd | Format: yyymmdd (ROC year, 7 characters) |
| Spec(TXT) | F20 | Alphanumeric, no duplicates | Alphanumeric (C), left-aligned, padded with spaces on the right; no duplicates |
| Spec(TXT) | F24 |  | NHI insured unit code, C, 9 characters (NHIA sample 123456789). Not the UBN. |
| Spec(TXT) | G4 | Social Security Integrate Number | Withholding agent's Unified Business Number (扣費單位統一編號), 8 characters. Same value in sections A, B and C. |
| Spec(TXT) | G14 | Social Security Integrate Number | Withholding agent's Unified Business Number (扣費單位統一編號), 8 characters. Same value in sections A, B and C. |
| Spec(TXT) | G23 | Mandatory column. / Input 62 or 66 | Block of 4 sub-fields (rows 24-27). Mandatory for income types 62 and 66. |
| Spec(TXT) | I4 | $legal_entity_hr.social_security_integrate_number | PREPAD($legal_entity_hr.company_registration_number; 8; '0') (公司統一編號, DD V3.3: Number, maximum 8 digits; output 8 characters with leading zeros); same field ... |
| Spec(TXT) | I6 | Take period in which first bonus is paid from pay element 58009 date within the tax year. | Take period in which first bonus is paid from pay element 58009 date within the tax year. Output in ROC yyymm: CONCAT(PREPAD(SUBTRACT(DATE_FORMAT(that paymen... |
| Spec(TXT) | I7 | Take period in which latest bonus is paid from pay element 58009 date within the tax year. | Take period in which latest bonus is paid from pay element 58009 date within the tax year. Output in ROC yyymm: CONCAT(PREPAD(SUBTRACT(DATE_FORMAT(that payme... |
| Spec(TXT) | I8 |  | CONCAT(PREPAD(SUBTRACT(DATE_FORMAT($report.generation_time; 'yyyy'); 1911); 3; '0'); DATE_FORMAT($report.generation_time; 'MMdd')) |
| Spec(TXT) | I9 |  | Blank (8 spaces) for a single unit. Filled with the head office UBN only when the entity has a head office (總機構); no such field in DD V3.3. |
| Spec(TXT) | I11 | $legal_entity.name | $legal_entity.name, converted to full-width characters and padded with full-width spaces (U+3000) to 25 characters (50 bytes BIG5); truncate after 25 characters |
| Spec(TXT) | I14 | $legal_entity_hr.social_security_integrate_number | PREPAD($legal_entity_hr.company_registration_number; 8; '0') (公司統一編號, DD V3.3: Number, maximum 8 digits; output 8 characters with leading zeros); same field ... |
| Spec(TXT) | I16 |  | Sequential per detail line in the file: 000000001, 000000002, ... (N, 9, left-padded with zeros) |
| Spec(TXT) | I17 |  | I (new). R (replace) is not supported by the product (Mohit, L17); corrections are made outside this report. |
| Spec(TXT) | I18 |  | Proposed: actual payment date of the payroll run in which the bonus (58009) is paid (Regulations art. 2), in ROC yyymmdd with the same formula as I8 (ROC yea... |
| Spec(TXT) | I20 | Unique ID; no duplicates allowed / You may use combination of CONCAT(DOB in YYYYMMDD, Employee ID) left padded with 0. | CONCAT(PREPAD($legal_entity_hr.company_registration_number; 8; '0'); '62'; Income Payment Date (positions 22-28, ROC yyymmdd); Serial Number (positions 12-20... |
| Spec(TXT) | I21 | Current period value of 58009. | Current period value of 58009. Full amount of this payment, N 14, never negative. Bonus base: question in K21. |
| Spec(TXT) | I23 | Input 62 | No value of its own: filled by rows 24-27 (positions 93-101, 102-107, 108-117, 118-132). |
| Spec(TXT) | I24 | $legal_entity_hr.social_security_integrate_number | PREPAD($legal_entity_hr.health_insure_id; 9; '0') (proposed: DD V3.3 'Health Insurance ID' 健保證號, 9 digits; same field as the NHI unit code in the TW SI specs... |
| Spec(TXT) | I25 | SUM(58139) | Proposed: 64550 (SNHI Interim Base = $hr.nhi_grade::orLabel) of the month of payment; for a bonus paid after termination, the insured amount at withdrawal (R... |
| Spec(TXT) | I26 | YTD of 58009 including current month 58009 value. | YTD of 58009 including current month 58009 value (1 January to this payment date, Regulations art. 6). Same bonus base as I21 (question in K21). N 10, never ... |
| Spec(TXT) | I29 |  | $employee_name, converted to full-width characters and padded with full-width spaces (U+3000) to 25 characters (50 bytes BIG5); truncate after 25 characters |
| Spec(TXT) | I33 | $legal_entity_hr.company_registration_number | PREPAD($legal_entity_hr.company_registration_number; 8; '0') |
| Spec(TXT) | I35 |  | COUNT of section B (detail) lines in this file. N 9, left-padded with zeros. |
| Spec(TXT) | I36 | Total of YTD 58009 Amount for all employees in this report. | SUM of positions 69-82 (Bonus Payment Amount) of all section B lines in this file; not YTD. N 20, left-padded with zeros. |
| Spec(TXT) | I37 | Total of YTD 2558 Amount for all employees in this report. Kindly confirm with RA if YTD amount need to show for 2558 here for only current period amount. | SUM of positions 83-92 (Supplementary Insurance Fee) of all section B lines in this file; not YTD. N 16, left-padded with zeros. |
| Spec(TXT) | I39 | $legal_entity_hr.representative | Contact person (聯絡人姓名), converted to full-width characters and padded with full-width spaces (U+3000) to 25 characters (50 bytes BIG5); truncate after 25 cha... |
| Spec(TXT) | K18 |  | Which engine variable holds the actual payment date of the payroll run? I18 needs it in ROC yyymmdd. |
| Spec(TXT) | K21 |  | Is 58009 the same bonus base that drives 2558? 58009 sums 6221x and 6222x only; should 6220x Bonus (Annual/Referral) be included (year-end bonus, Regulations... |
| Spec(TXT) | K24 |  | Is $legal_entity_hr.health_insure_id the NHI insured unit code (投保單位代號, 9 characters)? |
| Spec(TXT) | K25 |  | PE 58139 is not in WTC V2.8. Is 64550 the insured amount of the month of payment? |
| Spec(TXT) | K39 |  | DD V3.3 has no contact-person field. Use $legal_entity_hr.representative or create a contact field? |

Por aba: Version Control = 5, Report Matrix = 11, Spec(TXT) = 41, Testing = 0, Options = 0
Total de células diferentes: 57 | esperadas: 57 | fora da lista: 0 | não aplicadas: 0

**Resultado: PASS (nenhuma diferença fora do escopo)**
