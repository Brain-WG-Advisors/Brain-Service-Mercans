# SR-109: rascunho de comentário (EN). NÃO POSTADO. (rodada 2)

@mjain Spec review done; changes highlighted in light blue in the spec (v1.2).

1. Overtime by day type is covered: WTC V2.3 split 62110/62111, 62120–62122 and 62130–62132, and the rates match LSA art. 24 and the MOL reference payslip. I added optional rate and hours lines. The overtime PEs have no hours input, so please confirm whether hours can be shown.
2. I added the "agreed total wage" line, which is LSA Enforcement Rules art. 14-1 item 1 and the only mandatory item that was missing. Its variable is TO BE CONFIRMED.
3. I filled Employer Address, Payment Date and Account currency with the variables used in the Mercans reference payslips. Please confirm the names; for the payment date the references use `$payroll.payment_date` or `$entry.payroll_payment_date`.
4. I added rows for Total Gross, Total Deductions and Total ER. The 65500:65859 range includes notional benefits (65508/65509, 65609, 65659): should they be left out of Total Gross or shown separately?
5. National ID now points to `$hr.id_card_number` (TW DD), as an optional field. Bank fields: the TW DD also has `$hr.bank_name` and `$hr.bank_account_name`. Which record is filled?
6. Chinese version: the law does not set a language, so I proposed one bilingual zh-TW/EN layout, with the labels in column U. This is a product decision for you.
7. I added a Report Matrix tab, RA field descriptions (column T) and the version history.

The test was run on an India entity, so the TW wage type names were not checked. Please retest on the Taiwan entity.
