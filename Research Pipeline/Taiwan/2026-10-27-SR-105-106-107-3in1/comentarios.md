# Rascunhos de comentário (EN) — SR-105 / SR-106 / SR-107

> Rascunho. Não postar sem ok do usuário. Pressupõe as specs v1.1 aprovadas e anexadas/importadas.

## SR-105 — Salary Adjustment
@mjain Spec reviewed against the current NHIA/BLI 3-in-1 batch salary adjustment format (03_Adj3Of1, rev. 114.12.12). Changes in v1.1 are in light blue.
- The batch is an Excel upload in the NHIA online system. The guide has no positions, so there is no official TXT layout.
- All 14 fields are mapped, with C/M/O and data type.
- Field 11 is the monthly wage total: the 3-month average, excluding year-end/festival bonuses. 58009/6220% removed.
- Field 14 accepts only 1, 2, 6, 7, 8. Field 6 adds "L".
- Periodicity: not quarterly. Feb–Jul changes are filed by end of August, Aug–Jan by end of February. Filing method: electronic upload.

Questions:
1. Field 11: OK to create an interim pay element for the 3-month average? Which WTs go in?
2. Field 12: does HR keep the previous `$hr.nhi_grade`?
3. Employee nationality: there is no DD field. Can we add one?
4. Is there a function for full-width characters (English names)?
5. NHI-only adjustments: the current guide no longer covers them. Keep them out of this batch?

## SR-106 — Termination
@mjain Spec reviewed against the current NHIA/BLI 3-in-1 batch withdrawal format (02_Stop3Of1, rev. 114.12.12). Changes in v1.1 are in light blue.
- The batch is an Excel upload in the NHIA online system. There is no official TXT layout.
- Fields 8, 10, 11 used `$hr.residential_status` (tax residency). They now use nationality and `$hr.id_type`.
- Fields 13/14 now use the DD names `$hr.health_insurance_withdraw_reason_code` / `_explanation` (::key).
- Field 15 is in the official format. It is now mapped from field 14.
- Field 6 is always "2": the guide no longer accepts "3", so NHI-only employees are out of this batch.
- Filing is due on the separation date, not within 3 days. Filing method: electronic upload.

Questions:
1. Employee nationality: there is no DD field. Can we add one?
2. Is there a function for full-width characters?
3. Fields 13/14: what default if HR is empty? We propose 2 / 1 (resignation).

## SR-107 — Joiner
@mjain Spec reviewed against the current NHIA/BLI 3-in-1 batch enrolment format (01_Apply3Of1, rev. 115.03.11). Changes in v1.1 are in light blue.
- The batch is an Excel upload in the NHIA online system. There is no official TXT layout.
- Field 6 is per row: 1 = employee, 2 = dependant. `$hr.number_of_nhi_dependents` sets the number of dependant rows. 58212 is no longer used.
- Field 12: 58139 does not exist in WTC V2.8. It now uses `$hr.nhi_grade::orLabel`.
- Fields 7/22 no longer use `$hr.residential_status` (tax residency).
- Current guide: insurance type "4" now means OAI/LP/NHI, and field 27 is mandatory with it. Foreign employees are not filed in this batch.
- Filing is due on the hire date, not within 3 days. Filing method: electronic upload.
- The "New Specification" tab (withholding tax) was removed from this file.

Questions:
1. Field 11: which HR field holds the agreed monthly wage at hire?
2. Employee nationality: there is no DD field. Can we add one?
3. Dependants: the DD has ID/name/birthday for 1–3 only, and no enrolment reason/date per dependant. Can these be added?
4. Fields 24/25: which object holds the integer rate? 52537/52517 divide by 100.
5. Field 27: the DD mapper label for "2" differs from the guide. Can it be updated?
6. Are foreign spouses (1/2) and "L" also excluded from the batch?
