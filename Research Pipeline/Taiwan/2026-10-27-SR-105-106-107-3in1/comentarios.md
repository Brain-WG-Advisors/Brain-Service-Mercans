# Rascunhos de comentário (EN): SR-105 / SR-106 / SR-107 (rodada 2)

> Rascunho. Não postar sem o ok do usuário. Pressupõe as specs v1.1 aprovadas e anexadas/importadas.
> Há uma pergunta para cada marcador TO BE CONFIRMED da spec; a célula vai entre colchetes, só para conferência interna (tirar antes de postar, se preferir).

## SR-105 (Salary Adjustment)
@mjain I reviewed the spec against the current NHIA/BLI 3-in-1 batch salary adjustment format (03_Adj3Of1, rev. 114.12.12). The changes in v1.1 are in light blue.
- The batch is an Excel file uploaded online (NHIA system or BLI e-service). The guide gives no positions, so there is no official TXT layout.
- All 14 fields are now mapped, with C/M/O, data type and a sample taken from the official sample.
- Field 11 is the monthly wage total: the 3-month average, without year-end/festival bonuses. 58009/6220% are no longer used.
- Field 14 accepts only 1, 2, 6, 7 and 8. Field 6 now includes "L".
- Periodicity is no longer quarterly. Changes from Feb–Jul are filed by the end of August, and changes from Aug–Jan by the end of February. Filing method: electronic upload.

Questions:
1. Field 11: may we create an interim pay element for the 3-month average? Which WTs should go into it? [L36]
2. Field 12: does HR keep the previous `$hr.nhi_grade` value? [L38]
3. Fields 11–13: the official sample uses 6-digit text with a leading zero (040000). Should we pad? [E36/E38/E40]
4. Employee nationality is not in the DD. Can we add it, plus a flag for "L"? [L18]
5. Name: is there a full-width function, and does `$hr.name` hold the English full name? [L23]
6. Field 14: `special_identity_code` exists twice in the DD (ID Information and Country Fields, with different mappers). Which one should the report read? [L42]
7. `labor_insure_id` is typed as Number in the DD, but it has a letter and a leading zero. Can it become Text? [L5]
8. The current guide no longer covers NHI-only adjustments. Should we keep them out of this batch? [A45]

## SR-106 (Termination)
@mjain I reviewed the spec against the current NHIA/BLI 3-in-1 batch withdrawal format (02_Stop3Of1, rev. 114.12.12). The changes in v1.1 are in light blue.
- The batch is an Excel file uploaded online. There is no official TXT layout.
- Fields 8, 10 and 11 used `$hr.residential_status`, which is tax residency. They now use nationality and `$hr.id_type`.
- Fields 13 and 14 now use the DD names `$hr.health_insurance_withdraw_reason_code` and `$hr.health_insurance_withdraw_reason_explanation` (::key). Field 15 is part of the official format and is mapped from field 14.
- Field 6 is always "2". The guide no longer accepts "3", so NHI-only employees are not in this batch.
- Filing is due on the separation date, not within 3 days. Filing method: electronic upload.

Questions:
1. Employee nationality is not in the DD. Can we add it? [F24]
2. Name: is there a full-width function, and does `$hr.name` hold the English full name? [F29]
3. Fields 13/14: what default should we use when HR is empty? We propose 2 / 1 (resignation). [F44/F47]
4. Field 16: for death, missing person or loss of eligibility, the date is not the last working day. Can we add a field for the reason date? [F60]
5. `labor_insure_id` is typed as Number in the DD. Can it become Text? [F5]

## SR-107 (Joiner)
@mjain I reviewed the spec against the current NHIA/BLI 3-in-1 batch enrolment format (01_Apply3Of1, rev. 115.03.11). The changes in v1.1 are in light blue.
- The batch is an Excel file uploaded online. There is no official TXT layout.
- Field 6 is set per row: 1 = employee, 2 = dependant. `$hr.number_of_nhi_dependents` gives the number of dependant rows, so 58212 is no longer used.
- Field 12 used 58139, which does not exist in WTC V2.8. It now uses `$hr.nhi_grade::orLabel`.
- Fields 7 and 22 no longer use `$hr.residential_status`.
- In the current guide, type "4" means OAI/LP/NHI and makes field 27 mandatory. Foreign ("Y") employees are not filed in this batch.
- Filing is due on the hire date, not within 3 days. Filing method: electronic upload. The "New Specification" tab (withholding tax) has been removed.

Questions:
1. Field 11: which HR field holds the agreed monthly wage at hire? [F14]
2. Fields 11/12: the sample uses unpadded text (36000). Is that OK? [L14/L16]
3. Employee nationality is not in the DD. Can we add it? Are codes 1/2/L also out of the batch, or only "Y"? [F10, B14]
4. Name: is there a full-width function, and does `$hr.name` hold the English full name? [F12]
5. Field 5: for dependant rows, should we use "3" as in the official sample? [F7]
6. Field 13: `special_identity_code` exists twice in the DD. Which one should the report read? [F17]
7. Dependants: the DD has ID, name and birthday for dependants 1–3 only. Can we add 4–6? How should non-national dependants be handled? [F19]
8. Relationship "P" (ward) is in the DD but not in the batch. How should we handle these dependants? [F22]
9. Field 20: can we add an NHI enrolment reason per dependant? We propose "4" as the default. [F24]
10. Fields 21/26: `health_insurance_enrollment_start_date` and `labor_pension_contribution_date` are typed as Text in the DD. Can they become Date? Can we also add the date of the dependant's enrolment reason? [F25, F30]
11. Fields 24/25: which object holds the integer rate? 52537/52517 divide by 100. [F28/F29]
12. Field 27: the DD mapper label for "2" differs from the guide ("not received the LI old-age benefit and over 65"). Can it be updated? [F31]
13. `labor_insure_id` is typed as Number in the DD. Can it become Text? [F4]
