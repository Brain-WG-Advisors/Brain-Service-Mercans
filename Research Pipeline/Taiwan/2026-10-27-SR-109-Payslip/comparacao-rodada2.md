# Rodada 2: diff célula a célula (v1.2 rodada 1 × v1.2 rodada 2)

- r1 md5 d198bd28f8c0910e47572e42c47b0c1a · r2 md5 ba8c27add3ee9680738db2008f3985a1

| Aba | Célula | Antes (r1) | Depois (r2) | Fill r2 | Status |
|---|---|---|---|---|---|
| Version Control | B13 | 1.2 | 1.0 | FFDDEBF7 | ok |
| Version Control | C13 | 2026-10-27 | 2025-12-02 | FFDDEBF7 | ok |
| Version Control | D13 | Spec review (LSA art. 23-24, Enforcement Rules art. 14-1): added Agreed Total Wage, Payment Date, Employer Address, total rows, overtime rate/hours, ID field, R | Payslip mapping done (ticket SR-109). | FFDDEBF7 | ok |
| Version Control | E13 | Draft |  | Values must be of type <class 'str'> | ok |
| Version Control | F13 | Wallisson Gomes | Lily Li | FFDDEBF7 | ok |
| Version Control | B14 |  | 1.1 | FFDDEBF7 | ok |
| Version Control | C14 |  | 2026-01-29 | FFDDEBF7 | ok |
| Version Control | D14 |  | Payslip configuration completed at country level; report code taiwan-payslip. | FFDDEBF7 | ok |
| Version Control | F14 |  | Shaik Jani Sharif | FFDDEBF7 | ok |
| Version Control | B15 |  | 1.2 | FFDDEBF7 | ok |
| Version Control | C15 |  | 2026-10-27 | FFDDEBF7 | ok |
| Version Control | D15 |  | Spec review (LSA art. 23-24, Enforcement Rules art. 14-1): added Agreed Total Wage, Payment Date, Employer Address, total rows, overtime rate/hours, ID field, R | FFDDEBF7 | ok |
| Version Control | E15 |  | Draft | FFDDEBF7 | ok |
| Version Control | F15 |  | Wallisson Gomes | FFDDEBF7 | ok |
| Report Matrix | B17 | TWD (NT$) - TO BE CONFIRMED BY MOHIT/BA | TWD (NT$) | FFDDEBF7 | ok |
| Report Matrix | A22 | Legal basis |  | None | ok |
| Report Matrix | B22 | Labor Standards Act arts. 23, 24, 39, 79; LSA Enforcement Rules art. 14-1; MOL reference payslip examples (參考例, attached to ticket SR-109). Texts read on laws.m |  | None | ok |
| Report Matrix | A23 |  | Comments | FFDDEBF7 | ok |
| Report Matrix | B23 |  | Legal basis: Labor Standards Act arts. 23, 24, 39, 79; LSA Enforcement Rules art. 14-1; MOL reference payslip examples (參考例, attached to ticket SR-109). Texts r | FFDDEBF7 | ok |
| Spec | Q6 | TO BE CONFIRMED BY MOHIT/BA - legal entity address variable (TW DD V3.3 has only $legal_entity_hr.post_code) | CONCAT($legal_entity_address.1.address_line_1;' ';$legal_entity_address.1.address_line_2;' ';$legal_entity_address.1.city;' ';$legal_entity_address.1.postal_cod | FFDDEBF7 | ok |
| Spec | U14 | 到職日期 | 到（離）職日期 | FFDDEBF7 | ok |
| Spec | Q15 | TO BE CONFIRMED BY MOHIT/BA - payment date of the payroll run (no variable found in TW DD V3.3) | $payroll.payment_date (as in REFERENCE_Payslip_Tunisia) or $entry.payroll_payment_date (as in REFERENCE_Payslip_Mozambique) — proposed (as in Mercans reference  | FFDDEBF7 | ok |
| Spec | H16 | TO BE CONFIRMED BY MOHIT/BA | 3210.0 | FFDDEBF7 | ok |
| Spec | Q20 | Static rate from the WTC V2.8 PE name: 62110=1.33, 62111=1.67, 62120=1.33, 62121=1.67, 62122=2.67, 62130=1, 62131=1.33, 62132=1.67. Display on payslip: TO BE CO | Static rate from the WTC V2.8 PE name (names round 1⅓/1⅔/2⅔ to 1.33/1.67/2.67): 62110 = 1⅓, 62111 = 1⅔ (LSA art. 24 para. 1); 62120 = 1⅓, 62121 = 1⅔ (LSA art. 2 | FFDDEBF7 | ok |
| Spec | T22 | Sum of all earning lines shown (same accounts as Earnings). MOL reference payslips show this subtotal. | Sum of all earning lines shown (same accounts as Earnings). MOL reference payslips show this subtotal. Note: 65500:65859 includes notional benefits not paid in  | FFDDEBF7 | ok |
| Spec | T37 | Amount actually paid. Covers LSA Enforcement Rules art. 14-1 item 4. Expected to equal Total Gross - Total Deductions; BA to confirm for the system accounts use | Amount actually paid. Covers LSA Enforcement Rules art. 14-1 item 4. Total Gross (row 22) includes notional benefits (65508/65509, 65609, 65659), so while they  | FFDDEBF7 | ok |
| Spec | T47 | Employee bank name. | Employee bank name. Question to BA: TW DD V3.3 Country Fields also holds $hr.bank_name, $hr.bank_account_name and $hr.bank_branch_code (CM, bank transfer). Whic | FFDDEBF7 | ok |
| Spec | T49 | Account holder name. | Account holder name. Question to BA: TW DD V3.3 Country Fields also holds $hr.bank_name, $hr.bank_account_name and $hr.bank_branch_code (CM, bank transfer). Whi | FFDDEBF7 | ok |
| Spec | Q51 | TO BE CONFIRMED BY MOHIT/BA (shown in the example, cell I63; no mapping) | $primary_employee_bank_account.account_currency — proposed (as in Mercans reference payslips) — confirm variable name with Mohit/BA | FFDDEBF7 | ok |

- Células por aba: {'Version Control': 14, 'Report Matrix': 5, 'Spec': 10}; total 29
- **Nenhuma diferença fora do escopo da rodada 2.**
