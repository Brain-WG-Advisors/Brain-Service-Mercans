# Comparação célula a célula

- Base: `C:/Users/instituto/Documents/brain-service/raw/docs/drive-exports/2026-10-27/TW - SI Termination specification.xlsx`
- Nova: `TW - SI Termination specification v1.1.xlsx`

- Células com diferença: **76** (declaradas: 76; sem efeito: 0)
- Abas removidas: nenhuma
- Partes do zip idênticas (bytes descomprimidos): 22; alteradas (declaradas): xl/worksheets/sheet1.xml, xl/worksheets/sheet2.xml, xl/worksheets/sheet3.xml, xl/styles.xml; removidas: nenhuma
- Problemas: **0**


| # | Aba | Célula | Antes | Depois | Preenchimento |
|---|---|---|---|---|---|
| 1 | Report Matrix | B11 | Manual: Submit hardcopies offline | Electronic: Upload online  | FFDDEBF7 |
| 2 | Report Matrix | B14 | Employees who have terminated employment and are enrolled in Labor/Health Insurance or Pension | Employees leaving whose LI(+EI)/OAI, LP and NHI are filed by the same unit (insurance type 2). NHI-only withdrawals ($hr.insurance_coverage = 3) are filed with NHIA, not in this batch (guide 02_Stop3Of1, rev. 114.12.12, field 6 and reminder). | FFDDEBF7 |
| 3 | Report Matrix | B22 | Some employers may use BLI’s e-filing system directly for faster processing. Termination should be reported within 3 days of the last working day. | File on the separation date (離職當日). LI/EI coverage ends at 24:00 on the day the filing reaches BLI; NHI ends at 24:00 on the day the withdrawal reason occurs (BLI form 承表L rev. 113.06, instr. 6). Dependants' NHI is transferred out automatically: no dependant rows. LP: the filing date is taken as the last LP contribution date; if different, file the LP stop form separately with BLI (承表L note 3). Electronic batch: Excel upload in the NHIA multi-certificate system; the official guide defines column order, values and notes only (no start/end positions, no official TXT layout). | FFDDEBF7 |
| 4 | Spec | J2 | (vazio) | C = Conditional, M = Mandatory, O = Optional | FFDDEBF7 |
| 5 | Spec | K2 | (vazio) | Data Type | FFDDEBF7 |
| 6 | Spec | D3 | 2.0 | 2 | FFDDEBF7 |
| 7 | Spec | J3 | (vazio) | M | FFDDEBF7 |
| 8 | Spec | K3 | (vazio) | Text | FFDDEBF7 |
| 9 | Spec | C5 | 勞工保險證號 (8位數子) | 保險證號 (8位數字) | FFDDEBF7 |
| 10 | Spec | F5 | $legal_entity_hr.labor_insure_id first 8 digits | $legal_entity_hr.labor_insure_id - first 8 characters, as text (keep leading zeros). DD V3.3 types this field as Number although the 9th character is a letter: TO BE CONFIRMED BY MOHIT/BA (DD also has insurance_certification_number, '8 digits + 1 text'). | FFDDEBF7 |
| 11 | Spec | J5 | (vazio) | M | FFDDEBF7 |
| 12 | Spec | K5 | (vazio) | Text | FFDDEBF7 |
| 13 | Spec | C7 | 勞工保險證號檢查碼 (1位英文字母) | 保險證號檢查碼 (1位英文字母) | FFDDEBF7 |
| 14 | Spec | F7 | $legal_entity_hr.labor_insure_id 9th digit of the field | UPPERCASE of the 9th character of $legal_entity_hr.labor_insure_id | FFDDEBF7 |
| 15 | Spec | J7 | (vazio) | M | FFDDEBF7 |
| 16 | Spec | K7 | (vazio) | Text | FFDDEBF7 |
| 17 | Spec | F9 | $legal_entity_hr.health_insure_id 9 digits total | PREPAD($legal_entity_hr.health_insure_id; 9; '0') - 9 digits as text | FFDDEBF7 |
| 18 | Spec | J9 | (vazio) | M | FFDDEBF7 |
| 19 | Spec | K9 | (vazio) | Text | FFDDEBF7 |
| 20 | Spec | H11 | Field not configured | $legal_entity_hr.nhi_authority::key (DD V3.3, option mapper 'NHI Authority', keys 1-6) | FFDDEBF7 |
| 21 | Spec | J11 | (vazio) | M | FFDDEBF7 |
| 22 | Spec | K11 | (vazio) | Text | FFDDEBF7 |
| 23 | Spec | D18 | 2,3 | 2 | FFDDEBF7 |
| 24 | Spec | F18 | $hr.insurance_coverage::key | Always "2" (guide rev. 114.12.12 accepts only "2" = 勞(就)保/災保/勞退/健保). Employees with $hr.insurance_coverage = 3 (NHI only) are excluded from this batch. | FFDDEBF7 |
| 25 | Spec | G18 | To apply for "Labor Health Insurance and Labor Retirement", please enter "2 / To apply for Health Insurance only, please enter "3" | To withdraw "勞(就)保/災保/勞退/健保" (LI/EI, OAI, LP and NHI), enter "2". | FFDDEBF7 |
| 26 | Spec | J18 | (vazio) | M | FFDDEBF7 |
| 27 | Spec | K18 | (vazio) | Text | FFDDEBF7 |
| 28 | Spec | G19 | When applying for "National Health Insurance", please enter "3" | Value "3" (NHI only) is no longer in the guide. | FFDDEBF7 |
| 29 | Spec | G20 | Only for the transfer (or cancellation) of one's own or one's dependents' health insurance, please upload the media data file through the Multi-credential online Underwriting operation System of the Central Health Insurance Administration. Fill in 3 in the "Insurance Type" field. | NHI-only changes are filed separately with NHIA (guide reminder). | FFDDEBF7 |
| 30 | Spec | D22 | 1.0 | 1 | FFDDEBF7 |
| 31 | Spec | J22 | (vazio) | M | FFDDEBF7 |
| 32 | Spec | K22 | (vazio) | Text | FFDDEBF7 |
| 33 | Spec | D24 | Y, 1, 2,Blank | Y, 1, 2, L, Blank | FFDDEBF7 |
| 34 | Spec | F24 | IF(EQUALS($hr.residential_status::key; '1'); 'Y'; '') | Employee nationality: no field in DD V3.3 -> NEW DD FIELD (proposed): Employee Nationality (+ permanent-resident foreign professional flag for 'L'); TO BE CONFIRMED BY MOHIT/BA. Logic: nationality = TW -> blank; permanent-resident foreign professional (永居外專) -> 'L'; $hr.spouse_nationality = TW and nationality = CN -> '2'; $hr.spouse_nationality = TW and other nationality (incl. Hong Kong/Macau) -> '1'; otherwise 'Y'. Do not use $hr.residential_status (tax residency). | FFDDEBF7 |
| 35 | Spec | J24 | (vazio) | C | FFDDEBF7 |
| 36 | Spec | K24 | (vazio) | Text | FFDDEBF7 |
| 37 | Spec | G28 | (vazio) | For "Permanent-resident foreign professional" (永居外專), enter "L". "Foreign spouse" ("1") includes Hong Kong/Macau spouses. | FFDDEBF7 |
| 38 | Spec | C29 | 被保險人姓名 (外籍含全名) | 被保險人姓名 | FFDDEBF7 |
| 39 | Spec | F29 | UPPERCASE($employee_name) | Nationals: Chinese name (ID Information field 'name' 名字). Foreigners with English names: UPPERCASE full name converted to full-width characters (e.g. ＤＡＶＩＤ), max. 200 characters. Full-width conversion function: TO BE CONFIRMED BY MOHIT/BA. | FFDDEBF7 |
| 40 | Spec | G29 | Please enter your name, up to 25 characters. Chinese names must be no less than 2 characters. For foreigners with English names, please enter the full name in uppercase English letters. | Chinese names: nationals at least 2 characters, foreigners at least 1. English names: full name in full-width uppercase letters. Maximum 200 characters. | FFDDEBF7 |
| 41 | Spec | J29 | (vazio) | M | FFDDEBF7 |
| 42 | Spec | K29 | (vazio) | Text | FFDDEBF7 |
| 43 | Spec | C31 | 被保險人身份證號 | 被保險人身分證號 | FFDDEBF7 |
| 44 | Spec | F31 | IF(EQUALS($hr.residential_status::key; '1'); $hr.id_card_number; $hr.passport_number) | IF(EQUALS($hr.id_type::key; '3'); $hr.passport_number; $hr.id_card_number) - nationals: national ID; foreigners: ARC unified ID number (id_type 2) or passport (id_type 3), the same ID used at enrolment. Replaces $hr.residential_status (tax residency). | FFDDEBF7 |
| 45 | Spec | J31 | (vazio) | M | FFDDEBF7 |
| 46 | Spec | K31 | (vazio) | Text | FFDDEBF7 |
| 47 | Spec | C32 | (居留證或護照號碼) | (居留證統一證號或護照號碼) | FFDDEBF7 |
| 48 | Spec | C36 | 被保險人居留證號碼 | 被保險人居留證統一證號 | FFDDEBF7 |
| 49 | Spec | F36 | IF(EQUALS($hr.residential_status::key; '0'); $hr.id_card_number; '') | IF(EQUALS($hr.id_type::key; '2'); $hr.id_card_number; '') - ARC unified ID number; blank for nationals. | FFDDEBF7 |
| 50 | Spec | J36 | (vazio) | C | FFDDEBF7 |
| 51 | Spec | K36 | (vazio) | Text | FFDDEBF7 |
| 52 | Spec | J40 | (vazio) | M | FFDDEBF7 |
| 53 | Spec | K40 | (vazio) | Text | FFDDEBF7 |
| 54 | Spec | D44 | 1,2. | 1, 2 | FFDDEBF7 |
| 55 | Spec | F44 | $hr.health_insurance_withdrawal_reason_code | $hr.health_insurance_withdraw_reason_code::key (1 = withdrawal, 2 = transfer out). Default when the HR field is empty: TO BE CONFIRMED BY MOHIT/BA (proposal: 2 for a resignation). | FFDDEBF7 |
| 56 | Spec | J44 | (vazio) | M | FFDDEBF7 |
| 57 | Spec | K44 | (vazio) | Text | FFDDEBF7 |
| 58 | Spec | F47 | $hr.health_insurance_withdrawal_reason_explanation | $hr.health_insurance_withdraw_reason_explanation::key (if field 13 = 1: M, E, U; if 2: 1, 2, 3, 4). Default when empty: TO BE CONFIRMED BY MOHIT/BA (proposal: 1 = resignation). | FFDDEBF7 |
| 59 | Spec | J47 | (vazio) | M | FFDDEBF7 |
| 60 | Spec | K47 | (vazio) | Text | FFDDEBF7 |
| 61 | Spec | G50 | For those who have lost their eligibility for the National Health Insurance, please enter "U". | For those who lost eligibility under NHI Act art. 8 or 9 (loss of nationality or household registration moved out; residence permit expired), enter "U". | FFDDEBF7 |
| 62 | Spec | B56 | Explanation of reasons for cancellation of health insurance coverage | Health insurance withdrawal reason description (text) | FFDDEBF7 |
| 63 | Spec | C56 | 健保退保原因說明別 | 健保退保原因說明 | FFDDEBF7 |
| 64 | Spec | F56 | Not needed field | Text derived from field 14: M -> 死亡; E -> 失蹤; U -> 喪失資格; 1 -> 離職; 2 -> 退休; 3 -> 停、歇業; 4 -> 退會 (short labels of the guide, not the mapper Local Value). | FFDDEBF7 |
| 65 | Spec | J56 | (vazio) | M | FFDDEBF7 |
| 66 | Spec | K56 | (vazio) | Text | FFDDEBF7 |
| 67 | Spec | F60 | CONCAT(SUBTRACT(DATE_FORMAT($employee.last_working_date; 'yyyy'); 1911); DATE_FORMAT($employee.last_working_date; 'MMdd')) | CONCAT(PREPAD(SUBTRACT(DATE_FORMAT($employee.last_working_date; 'yyyy'); 1911); 3; '0'); DATE_FORMAT($employee.last_working_date; 'MMdd')) | FFDDEBF7 |
| 68 | Spec | J60 | (vazio) | M | FFDDEBF7 |
| 69 | Spec | K60 | (vazio) | Text | FFDDEBF7 |
| 70 | Spec | A65 | NOTE: Just a reminder! ※ If the individual cancels their health insurance coverage, all their dependents will be transferred out simultaneously without the need to enter their information. /  / For separate declaration of health insurance, please upload it to the Multi-credential Online Underwriting Operation System of the Central Health Insurance Administration. /  / 以上翻译结果来自有道神经网络翻译（YNMT）· 通用场景 /  | NOTE (guide rev. 114.12.12): ※ When the insured person withdraws from NHI, all dependants are transferred out; no dependant data is entered. ※ NHI Act art. 8: loss of nationality or household registration moved out; art. 9: residence permit expired. ※ NHI-only changes are filed separately with NHIA. | FFDDEBF7 |
| 71 | Version Control | B9 | <Country name> | Taiwan | FFDDEBF7 |
| 72 | Version Control | B14 | (vazio) | 1.1 | FFDDEBF7 |
| 73 | Version Control | C14 | (vazio) | 2026-10-27 | FFDDEBF7 |
| 74 | Version Control | D14 | (vazio) | Spec review against NHIA/BLI 3-in-1 batch withdrawal format (02_Stop3Of1, rev. 114.12.12): field mappings corrected, field 15 added, C/M/O, data types and Report Matrix updated. | FFDDEBF7 |
| 75 | Version Control | E14 | (vazio) | Draft | FFDDEBF7 |
| 76 | Version Control | F14 | (vazio) | Wallisson Gomes | FFDDEBF7 |
