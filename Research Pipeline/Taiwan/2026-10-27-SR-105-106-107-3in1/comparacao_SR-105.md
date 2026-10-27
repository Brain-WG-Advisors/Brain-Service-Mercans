# Comparação célula a célula

- Base: `C:/Users/instituto/Documents/brain-service/raw/docs/drive-exports/2026-10-27/TW - SI electronic filing Salary Adjustment specification.xlsx`
- Nova: [[Research Pipeline/Taiwan/2026-10-27-SR-105-106-107-3in1/TW - SI electronic filing Salary Adjustment specification v1.1.xlsx|TW - SI electronic filing Salary Adjustment specification v1.1.xlsx]]

- Células com diferença: **88** (declaradas: 88; sem efeito: 0)
- Abas removidas: nenhuma
- Partes do zip idênticas (bytes descomprimidos): 20; alteradas (declaradas): xl/worksheets/sheet1.xml, xl/worksheets/sheet2.xml, xl/worksheets/sheet3.xml, xl/styles.xml; removidas: nenhuma
- Problemas: **0**


| # | Aba | Célula | Antes | Depois | Preenchimento |
|---|---|---|---|---|---|
| 1 | Report Matrix | B6 | Quarterly | Period | FFDDEBF7 |
| 2 | Report Matrix | B9 | Usually unspecified; may follow CompanyCode_Adjustment_YYYYQX.xlsx /  | Not prescribed by the official format guide (03_Adj3Of1, rev. 114.12.12). | FFDDEBF7 |
| 3 | Report Matrix | B11 | Manual: Submit hardcopies offline | Electronic: Upload online  | FFDDEBF7 |
| 4 | Report Matrix | B14 | Regular employees enrolled in Labor Insurance (勞保), Health Insurance (健保), or Pension (勞退) | Employees of a unit filing LI(+EI)/OAI, LP and NHI together (the guide applies to 勞(就)保/災保/勞退/健保 and 就保/災保/勞退/健保 units) whose monthly wage total (月薪資總額) or NHI insured amount changes. | FFDDEBF7 |
| 5 | Report Matrix | B20 | Used to notify the Bureau of salary changes that affect insurance premium contributions under the Labor Insurance and National Health Insurance Acts. Submitted quarterly unless there’s an urgent change. | Used to notify BLI and NHIA, in one Excel batch, of changes in the LI/EI/OAI insured salary, the LP monthly contribution wage and the NHI insured amount. Wage changes Feb-Jul must be filed by the end of August; Aug-Jan by the end of February; the new amounts apply from the 1st of the month after filing (BLI form 承表S rev. 115.05, instr. 7; NHIA insured-amount guide). | FFDDEBF7 |
| 6 | Report Matrix | B22 | The salary adjustment is required if there’s a change in insured salary tier. Employer must print the form and submit with company seal. /  | Electronic batch: Excel file uploaded in the NHIA multi-certificate online system (申報批次勞健合一 EXCEL: enrolment, withdrawal, salary adjustment). The official guide (03_Adj3Of1, rev. 114.12.12) defines only column order, values and notes: no start/end positions and no official TXT layout. Salary reductions require supporting documents uploaded in the NHIA system (NHIA East Division flyer). BLI may ask for the last 3 months' payroll records (承表S instr. 8). | FFDDEBF7 |
| 7 | Specification | A1 | Format Explanation for Salary Adjustment in Labor Insurance, Health Insurance, and Labor Retirement (3-in-1) Batches (October 5, 2014) | Format Explanation for 3-in-1 Batch Salary Adjustment (三合一批次薪資調整格式說明) - NHIA/BLI, revised 2025-12-12 (ROC 114.12.12). Applies to 勞(就)保/災保/勞退/健保 and 就保/災保/勞退/健保 units. | FFDDEBF7 |
| 8 | Specification | D3 | (vazio) | M | FFDDEBF7 |
| 9 | Specification | E3 | (vazio) | Text | FFDDEBF7 |
| 10 | Specification | G3 | 3.0 | 3 | FFDDEBF7 |
| 11 | Specification | J3 | (vazio) | 3 | FFDDEBF7 |
| 12 | Specification | L3 | (vazio) | Always "3" | FFDDEBF7 |
| 13 | Specification | C5 | 勞工保險證號 (8位數字) | 保險證號 (8位數字) | FFDDEBF7 |
| 14 | Specification | D5 | (vazio) | M | FFDDEBF7 |
| 15 | Specification | E5 | (vazio) | Text | FFDDEBF7 |
| 16 | Specification | J5 | (vazio) | 01999999 | FFDDEBF7 |
| 17 | Specification | L5 | (vazio) | $legal_entity_hr.labor_insure_id - first 8 characters, as text (keep leading zeros). DD V3.3 types this field as Number although the 9th character is a letter: TO BE CONFIRMED BY MOHIT/BA (DD also has insurance_certification_number, '8 digits + 1 text'). | FFDDEBF7 |
| 18 | Specification | C7 | 勞工保險證號檢查碼 (1位英文字母) | 保險證號檢查碼 (1位英文字母) | FFDDEBF7 |
| 19 | Specification | D7 | (vazio) | M | FFDDEBF7 |
| 20 | Specification | E7 | (vazio) | Text | FFDDEBF7 |
| 21 | Specification | J7 | (vazio) | B | FFDDEBF7 |
| 22 | Specification | L7 | (vazio) | UPPERCASE of the 9th character of $legal_entity_hr.labor_insure_id | FFDDEBF7 |
| 23 | Specification | D9 | (vazio) | M | FFDDEBF7 |
| 24 | Specification | E9 | (vazio) | Text | FFDDEBF7 |
| 25 | Specification | J9 | (vazio) | 000000000 | FFDDEBF7 |
| 26 | Specification | L9 | (vazio) | PREPAD($legal_entity_hr.health_insure_id; 9; '0') - 9 digits as text | FFDDEBF7 |
| 27 | Specification | D11 | (vazio) | M | FFDDEBF7 |
| 28 | Specification | E11 | (vazio) | Text | FFDDEBF7 |
| 29 | Specification | J11 | (vazio) | 1 | FFDDEBF7 |
| 30 | Specification | L11 | (vazio) | $legal_entity_hr.nhi_authority::key (DD V3.3, option mapper 'NHI Authority', keys 1-6) | FFDDEBF7 |
| 31 | Specification | C18 | 被保險人外籍 | <外籍專用> 被保險人外籍 | FFDDEBF7 |
| 32 | Specification | D18 | (vazio) | C | FFDDEBF7 |
| 33 | Specification | E18 | (vazio) | Text | FFDDEBF7 |
| 34 | Specification | G18 | Y, 1, 2, Blank | Y, 1, 2, L, Blank | FFDDEBF7 |
| 35 | Specification | J18 | (vazio) | Y | FFDDEBF7 |
| 36 | Specification | L18 | (vazio) | Employee nationality: no field in DD V3.3 -> NEW DD FIELD (proposed): Employee Nationality (+ permanent-resident foreign professional flag for 'L'); TO BE CONFIRMED BY MOHIT/BA. Logic: nationality = TW -> blank; permanent-resident foreign professional (永居外專) -> 'L'; $hr.spouse_nationality = TW and nationality = CN -> '2'; $hr.spouse_nationality = TW and other nationality (incl. Hong Kong/Macau) -> '1'; otherwise 'Y'. Do not use $hr.residential_status (tax residency). | FFDDEBF7 |
| 37 | Specification | M22 | (vazio) | For "Permanent-resident foreign professional" (永居外專), enter "L". "Foreign spouse" ("1") includes Hong Kong/Macau spouses. | FFDDEBF7 |
| 38 | Specification | C23 | 被保險人姓名 (外籍含全名) | 被保險人姓名 | FFDDEBF7 |
| 39 | Specification | D23 | (vazio) | M | FFDDEBF7 |
| 40 | Specification | E23 | (vazio) | Text | FFDDEBF7 |
| 41 | Specification | J23 | (vazio) | ＤＡＶＩＤ | FFDDEBF7 |
| 42 | Specification | L23 | (vazio) | IF(EQUALS(field 6; ''); $hr.name; FULLWIDTH(UPPERCASE($hr.name))) - nationals: Chinese name ($hr.name, DD V3.3 ID Information 'name' 名字); foreigners with English names: full name in full-width uppercase (e.g. ＤＡＶＩＤ), max. 200 characters. FULLWIDTH: TO BE CONFIRMED BY MOHIT/BA (no such function known in the formula engine; also confirm that $hr.name holds the English full name of foreigners). | FFDDEBF7 |
| 43 | Specification | M23 | Please enter your name, up to 25 characters. Chinese names must be no less than 2 characters. For foreigners with English names, please enter the full name in uppercase English letters. | Chinese names: nationals at least 2 characters, foreigners at least 1. English names: full name in full-width uppercase letters. Maximum 200 characters. | FFDDEBF7 |
| 44 | Specification | C25 | 被保險人身份證號 (居留證或護照號碼) (勞保專用) | 被保險人身分證號 (居留證統一證號或護照號碼) (勞保專用) | FFDDEBF7 |
| 45 | Specification | D25 | (vazio) | M | FFDDEBF7 |
| 46 | Specification | E25 | (vazio) | Text | FFDDEBF7 |
| 47 | Specification | J25 | (vazio) | W987654 | FFDDEBF7 |
| 48 | Specification | L25 | (vazio) | IF(EQUALS($hr.id_type::key; '3'); $hr.passport_number; $hr.id_card_number) - nationals: national ID; foreigners: ARC unified ID number (id_type 2) or passport (id_type 3), the same ID used at enrolment. Replaces $hr.residential_status (tax residency). | FFDDEBF7 |
| 49 | Specification | C30 | 被保險人居留證號碼 (健保專用) | 被保險人居留證統一證號 (健保專用) | FFDDEBF7 |
| 50 | Specification | D30 | (vazio) | C | FFDDEBF7 |
| 51 | Specification | E30 | (vazio) | Text | FFDDEBF7 |
| 52 | Specification | J30 | (vazio) | AB12345678 | FFDDEBF7 |
| 53 | Specification | L30 | (vazio) | IF(EQUALS($hr.id_type::key; '2'); $hr.id_card_number; '') - ARC unified ID number; blank for nationals. | FFDDEBF7 |
| 54 | Specification | D34 | (vazio) | M | FFDDEBF7 |
| 55 | Specification | E34 | (vazio) | Text | FFDDEBF7 |
| 56 | Specification | G34 | (vazio) | YYYMMDD (ROC year) | FFDDEBF7 |
| 57 | Specification | J34 | (vazio) | 0731215 | FFDDEBF7 |
| 58 | Specification | L34 | (vazio) | CONCAT(PREPAD(SUBTRACT(DATE_FORMAT($person.birth_date; 'yyyy'); 1911); 3; '0'); DATE_FORMAT($person.birth_date; 'MMdd')) | FFDDEBF7 |
| 59 | Specification | B36 | Adjusted actual monthly salary (For labor insurance and labor retirement purposes only) | Monthly wage total after adjustment [LI(EI)/OAI/LP] | FFDDEBF7 |
| 60 | Specification | C36 | 調後月實際工資 (勞保、勞退專用) | 調後月薪資總額 [勞(就)保/災保/勞退] | FFDDEBF7 |
| 61 | Specification | D36 | (vazio) | M | FFDDEBF7 |
| 62 | Specification | E36 | (vazio) | Text (official sample: 6 digits with leading zero, e.g. 040000; padding/width TO BE CONFIRMED BY MOHIT/BA) | FFDDEBF7 |
| 63 | Specification | J36 | (vazio) | 040000 | FFDDEBF7 |
| 64 | Specification | L36 | (vazio) | TO BE CONFIRMED BY MOHIT/BA: new interim pay element = average monthly wage total (月薪資總額) of the 3 months before the adjustment (BLI page 0022929, item 2(1)). Include all pay received for work: base salary, monthly allowances, meal allowance, overtime, attendance/performance/production bonuses. Exclude year-end and assessment bonuses, festival bonuses and profit sharing (NHIA insured-amount guide; LSA Enforcement Rules art. 10). Do not use 58008/58009/6220%: 58009 is additional pay, 6220x are annual/referral bonuses, 58008 covers taxable recurring pay only. | FFDDEBF7 |
| 65 | Specification | M36 | Please enter the adjusted monthly actual salary | Enter the monthly wage total after adjustment. BLI classifies it into the LI, OAI and LP band tables after receiving the file. | FFDDEBF7 |
| 66 | Specification | B38 | Pre-Adjustment Health Insurance Salary /  | Pre-adjustment NHI insured amount | FFDDEBF7 |
| 67 | Specification | C38 | 健保調前投保薪資 | 健保調前投保金額 | FFDDEBF7 |
| 68 | Specification | D38 | (vazio) | M | FFDDEBF7 |
| 69 | Specification | E38 | (vazio) | Text (official sample: 6 digits with leading zero, e.g. 040000; padding/width TO BE CONFIRMED BY MOHIT/BA) | FFDDEBF7 |
| 70 | Specification | J38 | (vazio) | 031800 | FFDDEBF7 |
| 71 | Specification | L38 | (vazio) | TO BE CONFIRMED BY MOHIT/BA: $hr.nhi_grade::orLabel in force before the change (requires the previous value / history of the HR field). Amount per the NHI insured-amount table. | FFDDEBF7 |
| 72 | Specification | B40 | Post-Adjustment Health Insurance Salary /  | Post-adjustment NHI insured amount | FFDDEBF7 |
| 73 | Specification | C40 | 健保調後投保薪資 | 健保調後投保金額 | FFDDEBF7 |
| 74 | Specification | D40 | (vazio) | M | FFDDEBF7 |
| 75 | Specification | E40 | (vazio) | Text (official sample: 6 digits with leading zero, e.g. 040000; padding/width TO BE CONFIRMED BY MOHIT/BA) | FFDDEBF7 |
| 76 | Specification | J40 | (vazio) | 043900 | FFDDEBF7 |
| 77 | Specification | L40 | (vazio) | $hr.nhi_grade::orLabel (current value; same base as WTC 64550). Validation: not lower than the LI/EI/OAI insured salary and the LP monthly contribution wage (BLI form 承表S instr. 6(3)). | FFDDEBF7 |
| 78 | Specification | D42 | (vazio) | C | FFDDEBF7 |
| 79 | Specification | E42 | (vazio) | Text | FFDDEBF7 |
| 80 | Specification | G42 | 1. 8. Blank | 1, 2, 6, 7, 8, Blank | FFDDEBF7 |
| 81 | Specification | L42 | (vazio) | $hr.special_identity_code::key when it is 1, 2, 6, 7 or 8; otherwise blank (the batch accepts only these values, guide rev. 114.12.12). TO BE CONFIRMED BY MOHIT/BA: DD V3.3 defines special_identity_code twice - ID Information ord. 36 (mapper 'Special Identity Code', keys 1-8, A, B, S, T; used here) and Country Fields ord. 46 (mapper 'Received Social Insurance Benefits Type (Occupational Accident)', keys 1, 2 only). Confirm the field read by the report. | FFDDEBF7 |
| 82 | Specification | M44 | (vazio) | For "Low-income occupational union member", enter "2"; "Awaiting ship onshore", "6"; "Sheltered workers with disabilities", "7". If the pay is below the minimum wage (e.g. part-time), the special identity must be filled. | FFDDEBF7 |
| 83 | Specification | A45 | NOTE : The "actual monthly salary after adjustment" entered will be processed by the Bureau of Labor Insurance after receiving the file, and then classified as "monthly insured salary after adjustment for Labor Insurance" and "monthly contribution salary after adjustment for labor retirement" respectively according to the labor insurance and labor retirement classification tables. / In addition, the Bureau of Labor Insurance will independently compare whether the workers have contributed to the labor pension. If the workers are not eligible for labor pension contributions, they will not contribute to the labor pension or the monthly contribution wage for the labor pension will be adjusted. / When you wish to declare the salary adjustment for the National Health Insurance separately, please leave the three fields of the labor insurance certificate number, the labor insurance certificate number check code, and the actual monthly salary after adjustment (for labor insurance and labor retirement purposes only) blank. | NOTE (guide rev. 114.12.12, field 11): BLI classifies the monthly wage total into the band tables after receiving the file. BLI checks whether the worker is an LP contributor; if not, no LP contribution or LP wage adjustment is made. If the pay is below the minimum wage (e.g. part-time), fill the special identity (field 14). / The 104.10.05 rule 'leave fields 2, 3 and 11 blank for an NHI-only adjustment' is no longer in the guide: NHI-only adjustments TO BE CONFIRMED BY MOHIT/BA. | FFDDEBF7 |
| 84 | Version Control | B14 | (vazio) | 1.1 | FFDDEBF7 |
| 85 | Version Control | C14 | (vazio) | 2026-10-27 00:00:00 | FFDDEBF7 |
| 86 | Version Control | D14 | (vazio) | Spec review against NHIA/BLI 3-in-1 batch salary adjustment format (03_Adj3Of1, rev. 114.12.12): field mappings, C/M/O, data types and Report Matrix updated. | FFDDEBF7 |
| 87 | Version Control | E14 | (vazio) | Under Review | FFDDEBF7 |
| 88 | Version Control | F14 | (vazio) | Wallisson Gomes | FFDDEBF7 |
