# Comparação célula a célula

- Base: `C:/Users/instituto/Documents/brain-service/raw/docs/drive-exports/2026-10-27/TW - SI electronic filing Joiner Specification.xlsx`
- Nova: `TW - SI electronic filing Joiner Specification v1.1.xlsx`

- Células com diferença: **119** (declaradas: 119; sem efeito: 0)
- Abas removidas: New Specification
- Partes do zip idênticas (bytes descomprimidos): 21; alteradas (declaradas): xl/worksheets/sheet1.xml, xl/worksheets/sheet2.xml, xl/worksheets/sheet3.xml, xl/styles.xml, xl/workbook.xml, xl/_rels/workbook.xml.rels, [Content_Types].xml; removidas: xl/drawings/drawing4.xml, xl/worksheets/_rels/sheet4.xml.rels, xl/worksheets/sheet4.xml
- Problemas: **0**


| # | Aba | Célula | Antes | Depois | Preenchimento |
|---|---|---|---|---|---|
| 1 | New Specification | * | aba existente | ABA REMOVIDA |  |
| 2 | Report Matrix | B10 | Employee Level /  | Employee level: one row per new hire (投保者 = 1) plus one row per NHI dependant (投保者 = 2). | FFDDEBF7 |
| 3 | Report Matrix | B11 | Manual: Submit hardcopies offline | Electronic: Upload online  | FFDDEBF7 |
| 4 | Report Matrix | B14 | All employees joining and requiring SI/HI/retirement enrollment | New hires enrolled by the same unit in LI(+EI)/OAI, LP and NHI (投保別 2) or in OAI, LP and NHI (投保別 4). Excluded (guide 01_Apply3Of1, rev. 115.03.11, note to field 6): NHI-only enrolments and enrolment of foreign (外籍) employees, for whom LI and NHI are filed separately (NHI with NHIA). Whether codes 1/2/L of field 7 are also excluded: TO BE CONFIRMED BY MOHIT/BA. | FFDDEBF7 |
| 5 | Report Matrix | B22 | Must be submitted within 3 days of employment. Failure to report may result in fines. For foreign nationals, additional identification fields are required. | File on the hire date (到職當日). LI/EI coverage starts at 00:00 on the filing date; if not filed on the hire date, from the next day (BLI form 承表D rev. 115.01, note 2). NHI starts on the day the enrolment conditions are met. Electronic batch: Excel upload in the NHIA multi-certificate system; the official guide defines column order, values and notes only (no start/end positions, no official TXT layout). | FFDDEBF7 |
| 6 | Spec | K2 | (vazio) | C = Conditional, M = Mandatory, O = Optional | FFDDEBF7 |
| 7 | Spec | L2 | (vazio) | Data Type | FFDDEBF7 |
| 8 | Spec | D3 | 4.0 | 4 | FFDDEBF7 |
| 9 | Spec | F3 | (vazio) | Always "4" | FFDDEBF7 |
| 10 | Spec | K3 | (vazio) | M | FFDDEBF7 |
| 11 | Spec | L3 | (vazio) | Text | FFDDEBF7 |
| 12 | Spec | C4 | 勞工保險證號 / (8位數字) | 保險證號 / (8位數字) | FFDDEBF7 |
| 13 | Spec | F4 | (vazio) | $legal_entity_hr.labor_insure_id - first 8 characters, as text (keep leading zeros). DD V3.3 types this field as Number although the 9th character is a letter: TO BE CONFIRMED BY MOHIT/BA (DD also has insurance_certification_number, '8 digits + 1 text'). | FFDDEBF7 |
| 14 | Spec | K4 | (vazio) | M | FFDDEBF7 |
| 15 | Spec | L4 | (vazio) | Text | FFDDEBF7 |
| 16 | Spec | C5 | 勞工保險證號檢查碼 | 保險證號檢查碼 | FFDDEBF7 |
| 17 | Spec | F5 | (vazio) | UPPERCASE of the 9th character of $legal_entity_hr.labor_insure_id | FFDDEBF7 |
| 18 | Spec | K5 | (vazio) | M | FFDDEBF7 |
| 19 | Spec | L5 | (vazio) | Text | FFDDEBF7 |
| 20 | Spec | F6 | (vazio) | PREPAD($legal_entity_hr.health_insure_id; 9; '0') - 9 digits as text | FFDDEBF7 |
| 21 | Spec | K6 | (vazio) | M | FFDDEBF7 |
| 22 | Spec | L6 | (vazio) | Text | FFDDEBF7 |
| 23 | Spec | F7 | (vazio) | Employee row: $hr.si_enrollment_code::key (2 or 4). Dependant row: "3" (as in the official sample) - TO BE CONFIRMED BY MOHIT/BA. Pay elements 58140/58120/2517/2560 are not used. | FFDDEBF7 |
| 24 | Spec | G7 | “2”: Labor Ins., Health Ins., Labor Pension;  / “3”: Health Ins. only;  / “4”: Occupational Accident Ins., Health Ins., Labor Pension | "2": LI(EI), OAI, LP and NHI (勞(就)保/災保/勞退/健保); / "3": NHI (健保); / "4": OAI, LP and NHI (災保/勞退/健保) - field 27 is then mandatory. | FFDDEBF7 |
| 25 | Spec | K7 | (vazio) | M | FFDDEBF7 |
| 26 | Spec | L7 | (vazio) | Text | FFDDEBF7 |
| 27 | Spec | F8 | (vazio) | Employee row: "1"; dependant row: "2". $hr.number_of_nhi_dependents = number of dependant rows to generate for the employee. 58212 (tax dependants) is not used. | FFDDEBF7 |
| 28 | Spec | K8 | (vazio) | M | FFDDEBF7 |
| 29 | Spec | L8 | (vazio) | Text | FFDDEBF7 |
| 30 | Spec | G9 | ※If only declaring health insurance for self or dependent, use NHI e-system; enter “3” in "Type of Enrollment" / ※Use e-service system for labor insurance or pension only / ※Foreign employees in non-category 1 units must upload supporting docs via e-system | ※ If field 5 = "4" (OAI/LP/NHI), field 27 must be filled. / ※ NHI-only changes, or enrolment of foreign (外籍) employees (LI and NHI filed separately): file with NHIA. / ※ Pay below the minimum wage (e.g. part-time): fill the special identity (field 13). | FFDDEBF7 |
| 31 | Spec | D10 | Y, 1, 2, blank | Y, 1, 2, L, blank | FFDDEBF7 |
| 32 | Spec | F10 | (vazio) | Employee nationality: no field in DD V3.3 -> NEW DD FIELD (proposed): Employee Nationality (+ permanent-resident foreign professional flag for 'L'); TO BE CONFIRMED BY MOHIT/BA. Logic: nationality = TW -> blank; permanent-resident foreign professional (永居外專) -> 'L'; $hr.spouse_nationality = TW and nationality = CN -> '2'; $hr.spouse_nationality = TW and other nationality (incl. Hong Kong/Macau) -> '1'; otherwise 'Y'. Do not use $hr.residential_status (tax residency). | FFDDEBF7 |
| 33 | Spec | G10 | Partial Foreigners require supporting documents via online system: / “Y”: Foreigner / “1”: Foreign spouse / “2”: Mainland Chinese spouse / Blank: Taiwanese nationality | "Y": Foreigner / "1": Foreign spouse (incl. Hong Kong/Macau spouse) / "2": Mainland Chinese spouse / "L": Permanent-resident foreign professional (永居外專) / Blank: Taiwanese nationality | FFDDEBF7 |
| 34 | Spec | K10 | (vazio) | C | FFDDEBF7 |
| 35 | Spec | L10 | (vazio) | Text | FFDDEBF7 |
| 36 | Spec | C11 | 被保險人身份證號 / (居留證或護照號碼) | 被保險人身分證號 / (居留證統一證號/護照號碼) | FFDDEBF7 |
| 37 | Spec | F11 | (vazio) | IF(EQUALS($hr.id_type::key; '3'); $hr.passport_number; $hr.id_card_number) - nationals: national ID; foreigners: ARC unified ID number (id_type 2) or passport (id_type 3), the same ID used at enrolment. Replaces $hr.residential_status (tax residency). | FFDDEBF7 |
| 38 | Spec | G11 | For Taiwanese, enter ID no. / For foreigners, enter ARC or passport no. | For Taiwanese, enter the national ID no. / For foreigners, enter the ARC unified ID no. or passport no. | FFDDEBF7 |
| 39 | Spec | K11 | (vazio) | M | FFDDEBF7 |
| 40 | Spec | L11 | (vazio) | Text | FFDDEBF7 |
| 41 | Spec | C12 | 被保險人姓名 / （外籍含全名） | 被保險人姓名 | FFDDEBF7 |
| 42 | Spec | F12 | (vazio) | Nationals: Chinese name (ID Information field 'name' 名字). Foreigners with English names: UPPERCASE full name converted to full-width characters (e.g. ＤＡＶＩＤ), max. 200 characters. Full-width conversion function: TO BE CONFIRMED BY MOHIT/BA. | FFDDEBF7 |
| 43 | Spec | G12 | Up to 25 characters. Chinese names: min. 2 characters.  / Foreign names: uppercase full-width English | Chinese names: nationals at least 2 characters, foreigners at least 1. English names: full name in full-width uppercase letters. Maximum 200 characters. | FFDDEBF7 |
| 44 | Spec | K12 | (vazio) | M | FFDDEBF7 |
| 45 | Spec | L12 | (vazio) | Text | FFDDEBF7 |
| 46 | Spec | F13 | (vazio) | CONCAT(PREPAD(SUBTRACT(DATE_FORMAT($person.birth_date; 'yyyy'); 1911); 3; '0'); DATE_FORMAT($person.birth_date; 'MMdd')) | FFDDEBF7 |
| 47 | Spec | K13 | (vazio) | M | FFDDEBF7 |
| 48 | Spec | L13 | (vazio) | Text | FFDDEBF7 |
| 49 | Spec | B14 | Actual Monthly Wage / (for Labor Ins. & Pension only) | Monthly wage total / [LI(EI)/OAI/LP] | FFDDEBF7 |
| 50 | Spec | C14 | 月實際工資 / (勞保、勞退專用) | 月薪資總額 / [勞(就)保/災保/勞退] | FFDDEBF7 |
| 51 | Spec | F14 | (vazio) | TO BE CONFIRMED BY MOHIT/BA: HR field holding the agreed monthly wage at hire (no payroll result exists at the hire event); if none exists -> NEW DD FIELD (proposed): Monthly wage total at hire. Must include all regular pay for work (base salary, monthly allowances incl. meal allowance, attendance/performance bonuses) and exclude year-end/assessment bonuses, festival bonuses and profit sharing (BLI page 0022929; NHIA insured-amount guide; LSA Enforcement Rules art. 10). 58008/58009/6220% are not used. | FFDDEBF7 |
| 52 | Spec | G14 | Enter actual monthly wage | Enter the monthly wage total | FFDDEBF7 |
| 53 | Spec | K14 | (vazio) | M | FFDDEBF7 |
| 54 | Spec | L14 | (vazio) | Numeric (integer) | FFDDEBF7 |
| 55 | Spec | G15 | ※Will be classified into insured salary/pension wage after submission | ※ BLI classifies it into the LI, OAI and LP band tables after receiving the file | FFDDEBF7 |
| 56 | Spec | B16 | Health Insurance Insured Salary | Health Insurance Insured Amount | FFDDEBF7 |
| 57 | Spec | C16 | 健保投保薪資 | 健保投保金額 | FFDDEBF7 |
| 58 | Spec | F16 | (vazio) | $hr.nhi_grade::orLabel (same base as WTC 64550; pay element 58139 does not exist in WTC V2.8). Validation: not lower than the LI/EI/OAI insured salary and the LP contribution wage (BLI form 承表D instr. 9(3)). | FFDDEBF7 |
| 59 | Spec | K16 | (vazio) | M | FFDDEBF7 |
| 60 | Spec | L16 | (vazio) | Numeric (integer) | FFDDEBF7 |
| 61 | Spec | F17 | (vazio) | $hr.special_identity_code::key; blank if empty | FFDDEBF7 |
| 62 | Spec | K17 | (vazio) | C | FFDDEBF7 |
| 63 | Spec | L17 | (vazio) | Text | FFDDEBF7 |
| 64 | Spec | F18 | (vazio) | $hr.labor_standards_act_special_identity::key; blank if empty | FFDDEBF7 |
| 65 | Spec | K18 | (vazio) | C | FFDDEBF7 |
| 66 | Spec | L18 | (vazio) | Text | FFDDEBF7 |
| 67 | Spec | F19 | (vazio) | Dependant row: $hr.id_card_number_dependent_N (national dependants only); employee row: blank. NEW DD FIELD (proposed): id_card_number_dependent_4..6 (DD V3.3 has ID/name/birthday for dependants 1-3 but relationship for 1-6). Non-national dependants: TO BE CONFIRMED BY MOHIT/BA. | FFDDEBF7 |
| 68 | Spec | K19 | (vazio) | C | FFDDEBF7 |
| 69 | Spec | L19 | (vazio) | Text | FFDDEBF7 |
| 70 | Spec | F20 | (vazio) | Dependant row: $hr.name_dependent_N; employee row: blank. NEW DD FIELD (proposed): name_dependent_4..6. | FFDDEBF7 |
| 71 | Spec | K20 | (vazio) | C | FFDDEBF7 |
| 72 | Spec | L20 | (vazio) | Text | FFDDEBF7 |
| 73 | Spec | F21 | (vazio) | Dependant row: CONCAT(PREPAD(SUBTRACT(DATE_FORMAT($hr.birthday_dependent_N; 'yyyy'); 1911); 3; '0'); DATE_FORMAT($hr.birthday_dependent_N; 'MMdd')); employee row: blank. NEW DD FIELD (proposed): birthday_dependent_4..6. | FFDDEBF7 |
| 74 | Spec | K21 | (vazio) | C | FFDDEBF7 |
| 75 | Spec | L21 | (vazio) | Text | FFDDEBF7 |
| 76 | Spec | C22 | 稱謂代碼 | 稱謂代號 | FFDDEBF7 |
| 77 | Spec | F22 | (vazio) | Dependant row: $hr.dependent_N_relationship::key (1-9); employee row: blank. The batch does not accept 'P' (ward, present in the DD mapper): such dependants TO BE CONFIRMED BY MOHIT/BA. | FFDDEBF7 |
| 78 | Spec | K22 | (vazio) | C | FFDDEBF7 |
| 79 | Spec | L22 | (vazio) | Text | FFDDEBF7 |
| 80 | Spec | F23 | (vazio) | $legal_entity_hr.nhi_authority::key (DD V3.3, option mapper 'NHI Authority', keys 1-6) | FFDDEBF7 |
| 81 | Spec | K23 | (vazio) | M | FFDDEBF7 |
| 82 | Spec | L23 | (vazio) | Text | FFDDEBF7 |
| 83 | Spec | F24 | (vazio) | Employee row: "1" (到職起薪). Dependant row: $hr.adult_2_lineal_relatives_code_N::key (S, P, A, H, G) when filled; otherwise NEW DD FIELD (proposed): NHI enrolment reason per dependant (4-8) - TO BE CONFIRMED BY MOHIT/BA (proposal: "4"). | FFDDEBF7 |
| 84 | Spec | G24 | Self: / “1”: Employment start / “2”: Union membership / Dependent: / “4”: Affiliated coverage / “5”: Change in status / “6”: Marriage / “7”: Adoption / “8”: Newborn / Special cases (dependent age ≥ 20, relationship = 3,5,7): / “S”: Student without job / “P”: Under guardianship / “A”: Disabled & unable to work / “H”: Seriously ill without job / “G”: Recent graduate or discharged soldier without job (within 1 year) /  | Self: / "1": Employment start / "2": Union membership / Dependent: / "4": Affiliated coverage / "5": Change in status / "6": Marriage / "7": Adoption / "8": Newborn / Special cases (dependant transferred in, aged 18 or over, relationship = 3, 5, 7): / "S": Student without job / "P": Under guardianship / "A": Disabled & unable to work / "H": Seriously ill without job / "G": Recent graduate or discharged soldier without job (within 1 year) | FFDDEBF7 |
| 85 | Spec | K24 | (vazio) | M | FFDDEBF7 |
| 86 | Spec | L24 | (vazio) | Text | FFDDEBF7 |
| 87 | Spec | F25 | (vazio) | Employee row: CONCAT(PREPAD(SUBTRACT(DATE_FORMAT($hr.health_insurance_enrollment_start_date; 'yyyy'); 1911); 3; '0'); DATE_FORMAT($hr.health_insurance_enrollment_start_date; 'MMdd')) - DD V3.3 types the field as Text: TO BE CONFIRMED BY MOHIT/BA. Dependant row: NEW DD FIELD (proposed): date of the dependant's enrolment reason. | FFDDEBF7 |
| 88 | Spec | K25 | (vazio) | M | FFDDEBF7 |
| 89 | Spec | L25 | (vazio) | Text | FFDDEBF7 |
| 90 | Spec | F26 | (vazio) | IF field 7 is not blank: IF(EQUALS($person.gender; 'male'); 'M'; 'F'); otherwise blank (foreigners only). Replaces $hr.residential_status (tax residency). | FFDDEBF7 |
| 91 | Spec | K26 | (vazio) | C | FFDDEBF7 |
| 92 | Spec | L26 | (vazio) | Text | FFDDEBF7 |
| 93 | Spec | F27 | (vazio) | $hr.pension_contribution_identity::key (employee row only) | FFDDEBF7 |
| 94 | Spec | K27 | (vazio) | C | FFDDEBF7 |
| 95 | Spec | L27 | (vazio) | Text | FFDDEBF7 |
| 96 | Spec | B28 | Employer Contribution Rate | Employer Contribution Rate (%) | FFDDEBF7 |
| 97 | Spec | C28 | 雇主提繳率 | 雇主提繳率(%) | FFDDEBF7 |
| 98 | Spec | F28 | (vazio) | Rate as an integer % (e.g. 6). Object holding it: TO BE CONFIRMED BY MOHIT/BA (WTC 52537 = DIVIDE($52537.amount;100), i.e. 0.06). | FFDDEBF7 |
| 99 | Spec | K28 | (vazio) | C | FFDDEBF7 |
| 100 | Spec | L28 | (vazio) | Numeric | FFDDEBF7 |
| 101 | Spec | B29 | Personal Voluntary Contribution Rate | Personal Voluntary Contribution Rate (%) | FFDDEBF7 |
| 102 | Spec | C29 | 個人自願提繳率 | 個人自願提繳率(%) | FFDDEBF7 |
| 103 | Spec | F29 | (vazio) | Rate as an integer %; blank if 0. Object holding it: TO BE CONFIRMED BY MOHIT/BA (WTC 52517 = DIVIDE($52517.amount;100)). | FFDDEBF7 |
| 104 | Spec | K29 | (vazio) | C | FFDDEBF7 |
| 105 | Spec | L29 | (vazio) | Numeric | FFDDEBF7 |
| 106 | Spec | F30 | (vazio) | Only if the LP contribution date differs from the LI enrolment date and is 1 to 6 days before the filing date: CONCAT(PREPAD(SUBTRACT(DATE_FORMAT($hr.labor_pension_contribution_date; 'yyyy'); 1911); 3; '0'); DATE_FORMAT($hr.labor_pension_contribution_date; 'MMdd')); otherwise blank. DD V3.3 types the field as Text: TO BE CONFIRMED BY MOHIT/BA. | FFDDEBF7 |
| 107 | Spec | K30 | (vazio) | C | FFDDEBF7 |
| 108 | Spec | L30 | (vazio) | Text | FFDDEBF7 |
| 109 | Spec | B31 | Received Social Insurance Benefits Type (Occupational Accident) | OAI-only enrolment condition (Occupational Accident Insurance; insurance type 4 only) | FFDDEBF7 |
| 110 | Spec | C31 | 已領取社會保險 / 給付種類 / (勞保職災專用) | <勞工職業災害保險> / 僅參加「災保」條件 / (投保別-4專用欄位) | FFDDEBF7 |
| 111 | Spec | F31 | (vazio) | IF field 5 = "4": $hr.received_social_insurance_benefits_type_occupational_accident::key; otherwise blank. TO BE CONFIRMED BY MOHIT/BA: DD mapper key 2 reads "received other social insurance benefits and over 65"; guide rev. 115.03.11 defines 2 as "not received the LI old-age benefit and over 65". | FFDDEBF7 |
| 112 | Spec | G31 | “1”: Received labor insurance old-age benefit / “2”: Received other social insurance benefit & over 65 years old / Leave blank if not applicable | "1": Already received the LI old-age benefit / "2": Not received the LI old-age benefit and over 65 / Blank: other cases. Mandatory when field 5 = "4". | FFDDEBF7 |
| 113 | Spec | K31 | (vazio) | C | FFDDEBF7 |
| 114 | Spec | L31 | (vazio) | Text | FFDDEBF7 |
| 115 | Version Control | B9 | <Country name> | Taiwan | FFDDEBF7 |
| 116 | Version Control | B14 | (vazio) | 1.1 | FFDDEBF7 |
| 117 | Version Control | C14 | (vazio) | 2026-10-27 00:00:00 | FFDDEBF7 |
| 118 | Version Control | D14 | (vazio) | Spec review against NHIA/BLI 3-in-1 batch enrolment format (01_Apply3Of1, rev. 115.03.11): field mappings, C/M/O, data types and Report Matrix updated; 'New Specification' tab (withholding tax) removed. | FFDDEBF7 |
| 119 | Version Control | E14 | (vazio) | Draft | FFDDEBF7 |
| 120 | Version Control | F14 | (vazio) | Wallisson Gomes | FFDDEBF7 |
