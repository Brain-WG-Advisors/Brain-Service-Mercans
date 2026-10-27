# SR-109: rascunho de comentário (EN). NÃO POSTADO.

@mjain Spec review done; changes highlighted in light blue in the spec (v1.2).

1. Overtime by day type is covered: WTC V2.3 split 62110/62111, 62120–62122 and 62130–62132, and the rates match LSA art. 24 and the MOL reference payslip. Added optional rate and hours lines; the overtime PEs have no hours input, please confirm if hours can be shown.
2. Added the "agreed total wage" line (LSA Enforcement Rules art. 14-1 item 1, the only mandatory item missing), plus Payment Date, Employer Address and the three total rows. Their variables are marked TO BE CONFIRMED.
3. National ID now points to `$hr.id_card_number` (TW DD); optional field.
4. Chinese version: the law does not set a language; proposed one bilingual zh-TW/EN layout (labels in column U). Product decision for you.
5. Added a Report Matrix tab and RA field descriptions (column T).

The test was run on an India entity, so TW wage type names were not checked; please retest on the Taiwan entity.
