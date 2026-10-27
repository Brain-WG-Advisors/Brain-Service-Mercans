# Belgium — Compliance Payslip Generator

*Source workbook: `06-payslip/BE_Compliance_Payslip_Generator.xlsx` — 8 sheets, in workbook order: `How to set up Payslip`, `Compliance Payslip`, `Belgium (EN)`, `Belgium (NL)`, `Payslip Spec`, `Field Option`, `Population Range`, `Unit Rate Details`*

<!-- nav-index -->
## Navigation — line numbers in this file

*Read this file with `offset`/`limit` rather than whole; it is large.*

- L21: Sheet: `How to set up Payslip`
- L85: Sheet: `Compliance Payslip`
- L147: Sheet: `Belgium (EN)`
- L271: Sheet: `Belgium (NL)`
- L395: Sheet: `Payslip Spec`
- L570: Sheet: `Field Option`
- L576: Sheet: `Population Range`
- L597: Sheet: `Unit Rate Details`

---

## Sheet: `How to set up Payslip`

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Create new sheet for your country, copy the payslip from  "Compliance Payslip" sheet and then make changes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | Example Payslip |  |  |  | \| |
|  | When creating report make sure to use the Normal margins <br> Page Layout -> Margins -> Normal   this will show if the content will fit on your page or not |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | Net Pay: |  |  |  |  |
|  | This section contains employer-related information. To add an extra row, simply select Row 10, right-click, and choose ‘Insert Row’ from the menu. |  |  | Employer  <br> Details |  | Employer Name |  | Mercans Estonia |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  | Employer Address |  | Väike-Tähe 20, Tartu, Tartumaa, 51010 |  |  |  | EUR |  | 1,350.00 |  |  | 1. Finalize Your Worksheet: |
|  |  |  |  |  |  | Country |  | Estonia |  |  |  |  |  |  |  |  | • Ensure all desired changes are made to your worksheet. |
|  |  |  |  |  |  | Period |  | 01/10/2023 - 31/10/2023 |  |  |  |  |  |  |  |  | 2. Access the ‘Save As’ Function: |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | • Click on the File tab in the top-left corner. |
|  | This section contains employee-related information. If a field is not applicable, you can either remove it or replace it with one relevant to the country. Additionally, you have the option to delete or add extra rows as needed. |  |  | Employee <br> Details |  | Employee name |  | John Doe |  | Email |  | jdoe@mercan.com |  |  |  |  | • Select Save As from the menu. |
|  |  |  |  |  |  | Employee ID |  | EID-1337 |  | Hire date |  | 01/10/2019 |  |  |  |  | 3. Choose PDF as the File Format: |
|  |  |  |  |  |  | Employee Position |  | Operational Support |  | Payment Method |  | Bank |  |  |  |  | • In the ‘Save As’ dialog box, click the dropdown menu labeled File format. |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | • Select PDF (*.pdf) from the list of file formats. |
|  | This section is for countries that require additional details on the payslip. If not needed, you can simply delete it.” |  |  | Extra Information |  | Basic Salary (EUR) |  | 2,000.00 |  | Custom Field |  | XXXXX |  |  |  |  | 4. Specify the Content to Export: |
|  |  |  |  |  |  | Daily (EUR) |  | 100.00 |  | Custom Field |  | XXXXX |  |  |  |  | • Click on the Sheet option |
|  |  |  |  |  |  | Hourly (EUR) |  | 12.50 |  | Custom Field |  | XXXXX |  |  |  |  | • Ensure the Option is set to Best for Printing |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 5. Save the PDF: |
|  | Here, you can add or remove wage types by inserting or deleting rows. If the provided columns are not applicable to the country, rename or merge them with other fields. <br> Don't delete the columns otherwise it messes up the design. |  |  | Details |  | Details |  |  |  |  |  |  |  |  |  |  | • Choose your desired file location and name. |
|  |  |  |  |  |  | Earnings |  |  |  | Unit | Amount |  |  | Year-to-date |  |  | • Click Save to generate the PDF. |
|  |  |  |  |  |  | XXXXX - Earning Pay Element |  |  |  |  | 2,000.00 |  |  | 20,000.00 |  |  |  |
|  |  |  |  |  |  | XXXXX - Earning Pay Element |  |  |  | 5 (Hrs) | 200.00 |  |  | 2,000.00 |  |  |  |
|  |  |  |  |  |  | XXXXX - Earning Pay Element |  |  |  |  | 10.00 |  |  | 100.00 |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  | Total Gross |  |  |  |  | 2,250.00 |  |  | EUR |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Here, you can add or remove wage types by inserting or deleting rows. If the provided columns are not applicable to the country, rename or merge them with other fields. <br> Don't delete the columns otherwise it messes up the design. |  |  | Details |  | Deductions |  |  |  | Unit | Amount |  |  | Year-to-date |  |  |  |
|  |  |  |  |  |  | XXXXX - Deduction Pay Element |  |  |  |  | 800.00 |  |  | 8,000.00 |  |  |  |
|  |  |  |  |  |  | XXXXX - Deduction Pay Element |  |  |  |  | 100.00 |  |  | 1,000.00 |  |  |  |
|  |  |  |  |  |  | Total Deductions |  |  |  |  | 900.00 |  |  | EUR |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | Net Pay: |  |  | 1,350.00 |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Here, you can add Bank info by inserting row if there is also Secoundary bank account. If the provided columns are not applicable to the country, rename or merge them with other fields. <br> Don't delete the columns otherwise it messes up the design. |  |  | Details |  | Employer Contributions |  |  |  |  | Amount |  |  | Year-to-date |  |  |  |
|  |  |  |  |  |  | XXXXX - Employer Contribution Pay Element |  |  |  |  | 400.00 |  |  | 4,000.00 |  |  |  |
|  |  |  |  |  |  | Total Employer Contributions |  |  |  |  | 400.00 |  |  | EUR |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Here, you can add Bank info by inserting row if there is also Secoundary bank account. If the provided columns are not applicable to the country, rename or merge them with other fields. <br> Don't delete the columns otherwise it messes up the design. |  |  | Bank Info |  | Banking details |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  | Bank name | SWIFT |  | Beneficiary name |  | Acc. Number |  | Account currency |  | Type |  |  |
|  |  |  |  |  |  | Swed Bank AS | SW121212 |  | Jhon Doe |  | EE121212121212 |  | EUR |  | Primary |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | This is a filler section designed to ensure the template fills the entire page and the footer remains in the correct position. If you add or delete rows in other sections, make sure to adjust this filler section by adding or removing the same number of rows. For example, if you add two rows in the ‘Earnings’ section, you should delete two rows from the ‘Filler’ section. |  |  | Filler |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  | This document has been generated by Mercans |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  | REF-P26-663 |  |  | © All rights reserved |  |  |  |  |  |  |  |  |

## Sheet: `Compliance Payslip`

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  | Example Payslip |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  | Net Pay: |  |  |
| Employer Name |  | Mercans Estonia |  |  |  |  |  |  |  |
| Employer Address |  | Väike-Tähe 20, Tartu, Tartumaa, 51010 |  |  |  | EUR |  | =SUM(I22:J24)-SUM(I28:J29) |  |
| Country |  | Belgium |  |  |  |  |  |  |  |
| Period |  | 01/10/2023 - 31/10/2023 |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
| Employee name |  | John Doe |  | Email |  | jdoe@mercan.com |  |  |  |
| Employee ID |  | EID-1337 |  | Hire date |  | 01/10/2019 |  |  |  |
| Employee Position |  | Operational Support |  | Payment Method |  | Bank |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
| Basic Salary (EUR) |  | 2000 |  | Custom Field |  | XXXXX |  |  |  |
| Daily (EUR) |  | 100 |  | Custom Field |  | XXXXX |  |  |  |
| Hourly (EUR) |  | 12.5 |  | Custom Field |  | XXXXX |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
| Details |  |  |  |  |  |  |  |  |  |
| Earnings |  |  |  |  |  | Rate | Unit | Amount |  |
| XXXXX - Earning Pay Element |  |  |  |  |  |  |  | 3210 |  |
| XXXXX - Earning Pay Element |  |  |  |  |  |  |  | 200 |  |
| XXXXX - Earning Pay Element |  |  |  |  |  |  |  | 10 |  |
| Total Gross |  |  |  |  |  |  |  | =CONCATENATE(TEXT(SUM(I22:J24), "# ###.00"), " ",G8) |  |
|  |  |  |  |  |  |  |  |  |  |
| Deductions |  |  |  |  |  | Rate | Unit | Amount |  |
| XXXXX - Deduction Pay Element |  |  |  |  |  |  |  | 800 |  |
| XXXXX - Deduction Pay Element |  |  |  |  |  |  |  | 100 |  |
| Total Deductions |  |  |  |  |  |  |  | =CONCATENATE(TEXT(SUM(I28:J29), "# ###.00"), " ",G8) |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  | Net Pay: |  |  | =CONCATENATE(TEXT(SUM(I8), "# ###.00"), " ",G8) |  |
|  |  |  |  |  |  |  |  |  |  |
| Employer Contributions |  |  |  |  |  |  |  | Amount |  |
| XXXXX - Employer Contribution Pay Element |  |  |  |  |  |  |  | 400 |  |
| Total Employer Contributions |  |  |  |  |  |  |  | =CONCATENATE(TEXT(SUM(I35), "# ###.00"), " ",G8) |  |
|  |  |  |  |  |  |  |  |  |  |
| Banking details |  |  |  |  |  |  |  |  |  |
| Bank name | SWIFT |  | Beneficiary name |  | Acc. Number |  | Account currency |  | Type |
| Swed Bank AS | SW121212 |  | Jhon Doe |  | EE121212121212 |  | EUR |  | Primary |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
| This document has been generated by Mercans |  |  |  |  |  |  |  |  |  |
| REF-P26-663 |  |  | © All rights reserved |  |  |  |  |  |  |

## Sheet: `Belgium (EN)`

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | PAYSLIP - BELGIUM |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Mercans Belgium NV |  |  |  |  | NET PAY (EUR) |  |  |  |  |  |  |  |
|  | Statutory payslip (loonbrief) - Wage Protection Act of 12 April 1965, Article 15; Royal Decree of 20 September 2009 |  |  |  |  | =H46 |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Pay period |  | 01/07/2026 - 31/07/2026 |  | Pay date |  | 31/07/2026 |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| EMPLOYER DETAILS |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Employer Name |  | Mercans Belgium NV |  | Enterprise Number (KBO / BCE) |  | 0412.345.614 |  |  |  |  |  |  |  |
| Establishment Unit Address |  | Uitbreidingstraat 84, 2600 Berchem (Antwerpen), Belgium |  | Establishment Unit Number |  | 2.123.456.791 |  |  |  |  |  |  |  |
| NSSO Employer Registration Number |  | 012-3456-25 |  | NSSO Employer Category |  | 017 |  |  |  |  |  |  |  |
| VAT Number |  | BE 0412.345.614 |  | NACE Activity Code |  | 62020 |  |  |  |  |  |  |  |
| Joint Committee |  | 200 - Aanvullend Paritair Comité voor de Bedienden |  | Withholding Tax Registration |  | 0412.345.614 (Finprof) |  |  |  |  |  |  |  |
| Work Accident Policy |  | AO-2026-004512 / Insurer enterprise number 0850.123.440 |  | Payslip Language Regime |  | Dutch - Dutch-language region (Decree of 19 July 1973) |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| EMPLOYEE DETAILS |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Employee Name |  | Jan Peeters |  | National Register Number (INSZ) |  | 88.03.14-245.40 |  |  |  |  |  |  |  |
| Employee Code |  | BE-00123 |  | Date of Birth |  | 14/03/1988 |  |  |  |  |  |  |  |
| Job Title |  | Senior Business Analyst |  | Department |  | IT Services |  |  |  |  |  |  |  |
| Worker Status |  | White-collar (bediende) |  | DmfA Worker Code |  | 495 |  |  |  |  |  |  |  |
| Hire Date |  | 01/09/2019 |  | Seniority |  | 6 years 10 months |  |  |  |  |  |  |  |
| Contract Duration Type |  | Indefinite duration (onbepaalde duur) |  | Working Time Regime |  | Full-time, 38h/week, 5-day week |  |  |  |  |  |  |  |
| Withholding Scale / Family Situation |  | Scale I - single, no dependants |  | Bank Account (IBAN) |  | BE68 5390 0754 7034 |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| WORKING TIME |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Calendar days | Working days in month | Days worked | Public holiday days | Paid leave days | Unpaid absence days | Contractual hours per week | Hours worked |  |  |  |  |  |  |
| 31 | 22 | 21 | 1 | 0 | 0 | 38 | 159.6 |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| EARNINGS |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Code | Description |  |  |  |  |  | Rate | Unit | Amount (EUR) |  |  |  |  |
| 62100 | Basic salary - monthly (white-collar) |  |  |  |  |  | =3500.0/22 | 21 | =ROUND(H33*I33,2) |  |  |  |  |
| 62964 | Public holiday pay - 21 July 2026 (National Day) |  |  |  |  |  | =H33 | 1 | =ROUND(H34*I34,2) |  |  |  |  |
|  | GROSS REMUNERATION (NSSO AND TAXABLE BASE) |  |  |  |  |  |  |  | =SUM(J33:J34) |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| DEDUCTIONS |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Code | Description |  |  |  |  |  | Rate | Unit | Amount (EUR) |  |  |  |  |
| 21900 | Employee social security contribution (NSSO) - 13.07% of the gross |  |  |  |  |  | 0.1307 |  | =ROUND(J35*H39,2) |  |  |  |  |
| BE-002 | Social work bonus - reduction of the employee contribution (two components, P = R_B + R_A, each degressive above its own full-amount limit - see the calculation basis in columns L to N) |  |  |  |  |  |  |  | =-M82 |  |  |  |  |
| BE-004 | Wage withholding tax (bedrijfsvoorheffing) - ordinary remuneration |  |  |  |  |  |  |  | =I80 |  |  |  |  |
| BE-001 | Special social security contribution (employee) |  |  |  |  |  |  |  | =I83 |  |  |  |  |
| BE-011 | Meal voucher - employee part (one voucher per day actually worked) |  |  |  |  |  | 1.09 | 21 | =ROUND(H43*I43,2) |  |  |  |  |
|  | TOTAL DEDUCTIONS |  |  |  |  |  |  |  | =SUM(J39:J43) |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| NET AMOUNT DUE AND PAID |  |  |  |  |  |  | =J35-J44 |  |  |  |  |  |  |
| Paid by SEPA credit transfer to BE68 5390 0754 7034 on 31/07/2026 - the amount due and the amount actually paid are identical. |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| NON-CASH ENTITLEMENTS |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Code | Description |  |  |  |  | Number | Face value | Total value | Employer part |  |  |  |  |
| 62660 | Meal vouchers - electronic |  |  |  |  | 21 | 10 | =ROUND(G51*H51,2) | =ROUND(G51*8.91,2) |  |  |  |  |
| 62870 | Eco vouchers - none granted in this period; the sectoral eco voucher of joint committee 200 is issued once a year |  |  |  |  | 0 | 0 | =ROUND(G52*H52,2) | =ROUND(G52*0.0,2) |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| EMPLOYER CONTRIBUTIONS AND TOTAL COST |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Code | Description |  |  |  |  |  | Rate | Unit | Amount (EUR) |  |  |  |  |
|  | Gross salary |  |  |  |  |  |  |  | =J35 |  |  |  |  |
| 23671 | Employer global social security contribution (facial rate, approximately 25%) |  |  |  |  |  | 0.25 |  | =ROUND(J35*H57,2) |  |  |  |  |
| BE-012 | Meal voucher - employer part |  |  |  |  |  | 8.91 |  | =ROUND(H58*21,2) |  |  |  |  |
| 62160 | Provision - double holiday pay (92% of the monthly gross / 12) |  |  |  |  |  | 0.92 |  | =ROUND(J35*H59/12,2) |  |  |  |  |
| 62901 | Provision - end-of-year premium (thirteenth month, 1/12) |  |  |  |  |  |  |  | =ROUND(J35/12,2) |  |  |  |  |
| 23671 | Employer contributions on the end-of-year premium provision |  |  |  |  |  | 0.25 |  | =ROUND(J60*H61,2) |  |  |  |  |
|  | TOTAL MONTHLY EMPLOYER COST |  |  |  |  |  |  |  | =SUM(J56:J61) |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| WITHHOLDING TAX CALCULATION BASIS (2026 PARAMETERS) |  |  |  |  |  |  |  |  |  |  | SOCIAL WORK BONUS CALCULATION BASIS (2026 PARAMETERS) |  |  |
| Step | Calculation |  |  |  |  |  |  | Amount (EUR) |  |  | Item | Value | Note |
| 1 | Gross remuneration |  |  |  |  |  |  | =J35 |  |  | Parameter row in force | 1 July 2026 | Pay period 01/07/2026 - 31/07/2026. The parameter set steps five times inside 2026 (1 January, 1 March, 1 April, 1 July, 1 September). Select the row by the PAY MONTH, not by the year. |
| 2 | Employee social security, 13.07% |  |  |  |  |  |  | =-J39 |  |  | Worker category | White-collar | The blue-collar maxima are the white-collar maxima x 1.08 (EUR 185.75 component B, EUR 137.74 component A) because the contribution runs on the 108% base. The wage limits are identical for both. |
| 3 | Social work bonus - nil: the reference wage of 3,500.00 exceeds both zero points in force from 1 July 2026, being 2,937.93 for component B and 3,336.98 for component A |  |  |  |  |  |  | =-J40 |  |  | Performance fraction, capped at 1.00 | =IFERROR(MIN(1,(C29+D29+E29)/B29),0) | Days worked plus public holidays plus paid leave, over the working days in the month (J/D). |
| 4 | Taxable base |  |  |  |  |  |  | =I66+I67+I68 |  |  | Reference wage S at 100%, full-time equivalent | =IF(M68=0,0,ROUND(J35/M68,2)) | S is the full-time-equivalent reference wage at 100%. For a blue-collar worker this is the 100% wage, NOT the 108% contribution base. |
| 5 | Annualised, x 12 |  |  |  |  |  |  | =I69*12 |  |  | Component B - full amount up to S_B | 2300.62 |  |
| 6 | Lump-sum professional expenses, 30% capped at 6,070.00 |  |  |  |  |  |  | =-MIN(ROUND(I70*0.3,2),6070.0) |  |  | Component B - maximum | 171.99 |  |
| 7 | Annual net taxable |  |  |  |  |  |  | =I70+I71 |  |  | Component B - degressive coefficient | 0.2699 |  |
| 8 | Tax, slice 1 - 16,710.00 x 26.75% |  |  |  |  |  |  | =ROUND(MIN(I72,16710.0)*0.2675,2) |  |  | Component B - reaches zero at S_A | 2937.93 |  |
| 9 | Tax, slice 2 - 12,790.00 x 42.80% |  |  |  |  |  |  | =ROUND(MAX(0,MIN(I72,29500.0)-16710.0)*0.428,2) |  |  | Component A - full amount up to S_A | 2937.93 |  |
| 10 | Tax, slice 3 - 940.60 x 48.15% |  |  |  |  |  |  | =ROUND(MAX(0,MIN(I72,51050.0)-29500.0)*0.4815,2) |  |  | Component A - maximum | 127.54 |  |
| 11 | Tax, slice 4 - nil above 51,050.00 |  |  |  |  |  |  | =ROUND(MAX(0,I72-51050.0)*0.535,2) |  |  | Component A - degressive coefficient | 0.3196 |  |
| 12 | Annual tax before reductions |  |  |  |  |  |  | =SUM(I73:I76) |  |  | Component A - reaches zero at S_zero | 3336.98 |  |
| 13 | Reduction for the tax-free allowance - 11,170.00 x 26.75% |  |  |  |  |  |  | =-ROUND(11170.0*0.2675,2) |  |  | R_B - component B granted | =IF(M69>M73,0,MAX(0,ROUND(M71-M72*MAX(0,M69-M70),2))) | Maximum at or below S_B; degressive between S_B and S_A; nil above S_A. |
| 14 | Annual withholding |  |  |  |  |  |  | =I77+I78 |  |  | R_A - component A granted | =IF(M69>M77,0,MAX(0,ROUND(M75-M76*MAX(0,M69-M74),2))) | Maximum at or below S_A; degressive between S_A and S_zero; nil above S_zero. |
| 15 | Monthly withholding tax, / 12 |  |  |  |  |  |  | =ROUND(I79/12,2) |  |  | P = R_B + R_A, full-time equivalent | =ROUND(M78+M79,2) | The two components are computed separately and added. |
| 16 | Quarterly wage for the special social security contribution, 3 x 3,500.00 |  |  |  |  |  |  | =J35*3 |  |  | P prorated by the performance fraction | =ROUND(M80*M68,2) |  |
| 17 | Special social security contribution per quarter - six-band table on the quarterly wage; this quarter falls in the band EUR 6,570.55 to EUR 11,211.00: 30.99 + 1.10% x (10,500.00 - 6,570.54) |  |  |  |  |  |  | =ROUND(30.99+0.011*(I81-6570.54),2) |  |  | P capped at the employee contribution due | =MIN(M81,J39) | The bonus can never exceed the 13.07% contribution itself and can never make it negative. |
| 18 | Special social security contribution per month, / 3 |  |  |  |  |  |  | =ROUND(I82/3,2) |  |  | Annual cap | see note | EUR 3,466.44 per calendar year from 1 January 2026 and EUR 3,523.92 from 1 April 2026. NOT FOUND - the cap applicable after the 1 July 2026 indexation; it must not be extrapolated. Not binding on a single-month specimen. |
|  |  |  |  |  |  |  |  |  |  |  | Legal basis: Law of 20 December 1999, Article 2, implemented by the Royal Decree of 17 January 2000 (BS 28 January 2000) as amended by the Royal Decrees of 27 March 2023 and 5 March 2024; NSSO administrative instructions 2026/1 and 2026/2, the work bonus annex. Since 1 April 2024 the bonus has TWO components. Each pays its maximum only at or below its own full-amount (lower) limit and is degressive between that limit and its own zero point - granting the full maximum anywhere below the upper limit overstates the bonus and is wrong. |  |  |
| YEAR-TO-DATE CUMULATIVE FIGURES (JANUARY - JULY 2026) |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Description |  |  |  |  |  |  |  | Amount (EUR) |  |  |  |  |  |
| Year-to-date ordinary gross remuneration, 7 x 3,500.00 |  |  |  |  |  |  |  | =3500.0*7 |  |  |  |  |  |
| Year-to-date double holiday pay, paid in May 2026 (92%) |  |  |  |  |  |  |  | =ROUND(3500.0*0.92,2) |  |  |  |  |  |
| Year-to-date total gross |  |  |  |  |  |  |  | =SUM(I87:I88) |  |  |  |  |  |
| Year-to-date employee social security, 13.07% |  |  |  |  |  |  |  | =ROUND(J39,2)*7+ROUND(I88*0.1307,2) |  |  |  |  |  |
| Year-to-date wage withholding tax, ordinary remuneration and double holiday pay at 47.44% |  |  |  |  |  |  |  | =J41*7+ROUND((I88-ROUND(I88*0.1307,2))*0.4744,2) |  |  |  |  |  |
| Year-to-date special social security contribution, quarters 1 and 2 plus the July instalment |  |  |  |  |  |  |  | =74.21+134.45+24.74 |  |  |  |  |  |
| Year-to-date meal voucher employee part, 139 vouchers x 1.09 |  |  |  |  |  |  |  | =ROUND(139*1.09,2) |  |  |  |  |  |
| Year-to-date net pay |  |  |  |  |  |  |  | =I89-I90-I91-I92-I93 |  |  |  |  |  |
| Year-to-date employer social security, ordinary remuneration only (double holiday pay carries no employer contribution) |  |  |  |  |  |  |  | =ROUND(3500.0*0.25,2)*7 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| LEAVE BALANCES |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Leave type |  |  |  | Entitlement | Taken | Balance | Legal basis |  |  |  |  |  |  |
| Statutory annual leave - 2025 service year, five-day week |  |  |  | 20 | 6 | =E99-F99 | Royal Decree of 30 March 1967 - four weeks |  |  |  |  |  |  |
| Public holidays, including replacement days |  |  |  | 10 | 6 | =E100-F100 | Law of 4 January 1974 - ten paid days per year |  |  |  |  |  |  |
| European leave (Europese vakantie) |  |  |  | 0 | 0 | =E101-F101 | Not applicable - the employee has a full 2025 service year |  |  |  |  |  |  |
| Care leave (unpaid) |  |  |  | 10 | 0 | =E102-F102 | Ten days per calendar year, unpaid |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| PAYMENT DETAILS |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Bank name |  | IBAN |  | BIC | Beneficiary | Payment method |  | Currency |  |  |  |  |  |
| ING Belgium NV |  | BE68 5390 0754 7034 |  | BBRUBEBB | Jan Peeters | SEPA credit transfer |  | EUR |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| STATUTORY NOTES - INCOME YEAR 2026 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| - Language. This payslip is issued in Dutch because the employer's seat of operation is in the Dutch-language region (Decree of 19 July 1973); the sanction for the wrong language is nullity of the document. Belgium does not permit bilingual personnel documents, so this English sheet is a courtesy translation only and has no legal effect. Belgium has three language regions and two of them are not yet delivered: a French version is a mandatory second deliverable for employers seated in the French-language region, and a German version is an explicit unbuilt seam for employers seated in the German-language region. Both are documented as known limitations of this build. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| - Employee social security. Single global contribution of 13.07% on the gross remuneration (Law of 27 June 1969, Articles 14 and 23; Royal Decree of 28 November 1969). Since 1 April 2024 the social work bonus has two components, computed separately and added (Law of 20 December 1999, Article 2; Royal Decree of 17 January 2000, as amended by the Royal Decree of 5 March 2024). On the parameters in force from 1 July 2026 for a white-collar worker, component B pays a maximum of EUR 171.99 at or below a reference wage of EUR 2,300.62 and falls degressively to nil at EUR 2,937.93; component A pays a maximum of EUR 127.54 at or below EUR 2,937.93 and falls degressively to nil at EUR 3,336.98. Each maximum is granted only at or below its own lower limit, never anywhere below the upper limit. The bonus is nil here because the reference wage of EUR 3,500.00 exceeds both zero points. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| - Wage withholding tax. Annualised non-cumulative calculation on the Annex III nr. 31 scale as amended by the Royal Decree of 11 December 2025: 26.75% to EUR 16,710.00, 42.80% to EUR 29,500.00, 48.15% to EUR 51,050.00 and 53.50% above. Lump-sum professional expenses of 30% capped at EUR 6,070.00. Basic tax-free allowance of EUR 11,170.00 delivered as a reduction of EUR 2,987.98 (11,170.00 x 26.75%). |  |  |  |  |  |  |  |  |  |  |  |  |  |
| - Special social security contribution. Banded on the QUARTERLY wage W under a table of six bands, and not on the monthly wage: up to EUR 5,836.14 nil; EUR 5,836.15 to EUR 6,570.54 = 4.22% x (W - 5,836.14); EUR 6,570.55 to EUR 11,211.00 = EUR 30.99 + 1.10% x (W - 6,570.54); EUR 11,211.01 to EUR 12,300.00 = EUR 82.05 + 3.38% x (W - 11,211.00); EUR 12,300.01 to EUR 18,116.46 = EUR 118.83 + 1.10% x (W - 12,300.00); above EUR 18,116.46 = EUR 182.82, the quarterly maximum for an individually assessed employee. The band is selected on the wage of the quarter actually paid, so a quarter that carries double holiday pay or the end-of-year premium normally falls in a higher band than an ordinary quarter - which is why the quarterly amounts in the cumulative block differ from one another. Withheld in monthly instalments and trued up at the last payment of the quarter (NSSO administrative instructions 2026/2). |  |  |  |  |  |  |  |  |  |  |  |  |  |
| - Meal vouchers. Employee share of EUR 1.09 per voucher and employer share of EUR 8.91 per voucher, at one voucher per day actually worked. Within these limits the voucher is exempt from social security contributions and from income tax. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| - Annual leave. Four weeks - 20 days on a five-day week - earned in the preceding holiday service year (Royal Decree of 30 March 1967). Double holiday pay of 92% of the monthly gross is paid separately in May and uses its own withholding table. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| - Employer cost. The employer facial rate of approximately 25% and the provisions for double holiday pay and the end-of-year premium are shown for information; they are not deducted from the employee. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| - Cumulative data are not mandatory on the Belgian payslip and are provided through the individual account; they are shown here for transparency. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| - Retention and format. The employer retains the payslip and the individual account for five years. An electronic payslip requires the employee's consent under the Law of 3 June 2007 on electronic social documents. |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| This document has been generated by Mercans Payroll System |  |  |  |  |  |  |  |  |  |  |  |  |  |
| BE-PSL-001 v1.0 - income year 2026 - all rights reserved |  |  |  |  |  |  |  |  |  |  |  |  |  |

## Sheet: `Belgium (NL)`

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | LOONBRIEF - BELGIË |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Mercans Belgium NV |  |  |  |  | NETTO TE BETALEN (EUR) |  |  |  |  |  |  |  |
|  | Wettelijke loonbrief - Loonbeschermingswet van 12 april 1965, artikel 15; Koninklijk besluit van 20 september 2009 |  |  |  |  | =H46 |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Loonperiode |  | 01/07/2026 - 31/07/2026 |  | Betaaldatum |  | 31/07/2026 |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| GEGEVENS VAN DE WERKGEVER |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Naam van de werkgever |  | Mercans Belgium NV |  | Ondernemingsnummer (KBO / BCE) |  | 0412.345.614 |  |  |  |  |  |  |  |
| Adres van de vestigingseenheid |  | Uitbreidingstraat 84, 2600 Berchem (Antwerpen), België |  | Vestigingseenheidsnummer |  | 2.123.456.791 |  |  |  |  |  |  |  |
| RSZ-werkgeversnummer |  | 012-3456-25 |  | RSZ-werkgeverscategorie |  | 017 |  |  |  |  |  |  |  |
| BTW-nummer |  | BE 0412.345.614 |  | NACE-activiteitscode |  | 62020 |  |  |  |  |  |  |  |
| Paritair comité |  | 200 - Aanvullend Paritair Comité voor de Bedienden |  | Registratienummer bedrijfsvoorheffing |  | 0412.345.614 (Finprof) |  |  |  |  |  |  |  |
| Polis arbeidsongevallen |  | AO-2026-004512 / Ondernemingsnummer verzekeraar 0850.123.440 |  | Taalregeling loonbrief |  | Nederlands - Nederlands taalgebied (Decreet van 19 juli 1973) |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| GEGEVENS VAN DE WERKNEMER |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Naam van de werknemer |  | Jan Peeters |  | Rijksregisternummer (INSZ) |  | 88.03.14-245.40 |  |  |  |  |  |  |  |
| Werknemersnummer |  | BE-00123 |  | Geboortedatum |  | 14/03/1988 |  |  |  |  |  |  |  |
| Functie |  | Senior Business Analist |  | Afdeling |  | IT Services |  |  |  |  |  |  |  |
| Statuut |  | Bediende |  | DmfA-werknemerskengetal |  | 495 |  |  |  |  |  |  |  |
| Datum indiensttreding |  | 01/09/2019 |  | Anciënniteit |  | 6 jaar 10 maanden |  |  |  |  |  |  |  |
| Type overeenkomst (duur) |  | Onbepaalde duur |  | Arbeidsregeling |  | Voltijds, 38u/week, vijfdagenweek |  |  |  |  |  |  |  |
| Schaal bedrijfsvoorheffing / gezinstoestand |  | Schaal I - alleenstaande, geen personen ten laste |  | Bankrekening (IBAN) |  | BE68 5390 0754 7034 |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ARBEIDSTIJD |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Kalenderdagen | Arbeidsdagen in de maand | Gewerkte dagen | Feestdagen | Betaalde verlofdagen | Onbezoldigde afwezigheidsdagen | Contractuele uren per week | Gewerkte uren |  |  |  |  |  |  |
| 31 | 22 | 21 | 1 | 0 | 0 | 38 | 159.6 |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| LOONBESTANDDELEN |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Code | Omschrijving |  |  |  |  |  | Tarief | Eenheid | Bedrag (EUR) |  |  |  |  |
| 62100 | Basisloon - maandwedde (bediende) |  |  |  |  |  | =3500.0/22 | 21 | =ROUND(H33*I33,2) |  |  |  |  |
| 62964 | Feestdagloon - 21 juli 2026 (Nationale Feestdag) |  |  |  |  |  | =H33 | 1 | =ROUND(H34*I34,2) |  |  |  |  |
|  | BRUTOLOON (RSZ- EN BELASTBARE BASIS) |  |  |  |  |  |  |  | =SUM(J33:J34) |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| INHOUDINGEN |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Code | Omschrijving |  |  |  |  |  | Tarief | Eenheid | Bedrag (EUR) |  |  |  |  |
| 21900 | Persoonlijke socialezekerheidsbijdrage (RSZ) - 13,07% van het bruto |  |  |  |  |  | 0.1307 |  | =ROUND(J35*H39,2) |  |  |  |  |
| BE-002 | Sociale werkbonus - vermindering van de persoonlijke bijdrage (twee componenten, P = R_B + R_A, elk degressief boven haar eigen ondergrens - zie de berekeningsbasis in de kolommen L tot N) |  |  |  |  |  |  |  | =-M82 |  |  |  |  |
| BE-004 | Bedrijfsvoorheffing - gewone bezoldigingen |  |  |  |  |  |  |  | =I80 |  |  |  |  |
| BE-001 | Bijzondere bijdrage voor de sociale zekerheid (werknemer) |  |  |  |  |  |  |  | =I83 |  |  |  |  |
| BE-011 | Maaltijdcheque - werknemersaandeel (een cheque per werkelijk gewerkte dag) |  |  |  |  |  | 1.09 | 21 | =ROUND(H43*I43,2) |  |  |  |  |
|  | TOTAAL INHOUDINGEN |  |  |  |  |  |  |  | =SUM(J39:J43) |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| NETTOBEDRAG VERSCHULDIGD EN UITBETAALD |  |  |  |  |  |  | =J35-J44 |  |  |  |  |  |  |
| Betaald via SEPA-overschrijving op BE68 5390 0754 7034 op 31/07/2026 - het verschuldigde bedrag en het werkelijk uitbetaalde bedrag zijn identiek. |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| VOORDELEN IN NATURA EN CHEQUES |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Code | Omschrijving |  |  |  |  | Aantal | Nominale waarde | Totale waarde | Werkgeversaandeel |  |  |  |  |
| 62660 | Maaltijdcheques - elektronisch |  |  |  |  | 21 | 10 | =ROUND(G51*H51,2) | =ROUND(G51*8.91,2) |  |  |  |  |
| 62870 | Ecocheques - geen toekenning in deze periode; de sectorale ecocheque van paritair comité 200 wordt eenmaal per jaar uitgereikt |  |  |  |  | 0 | 0 | =ROUND(G52*H52,2) | =ROUND(G52*0.0,2) |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| WERKGEVERSBIJDRAGEN EN TOTALE LOONKOST |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Code | Omschrijving |  |  |  |  |  | Tarief | Eenheid | Bedrag (EUR) |  |  |  |  |
|  | Brutoloon |  |  |  |  |  |  |  | =J35 |  |  |  |  |
| 23671 | Globale werkgeversbijdrage sociale zekerheid (faciaal percentage, ongeveer 25%) |  |  |  |  |  | 0.25 |  | =ROUND(J35*H57,2) |  |  |  |  |
| BE-012 | Maaltijdcheque - werkgeversaandeel |  |  |  |  |  | 8.91 |  | =ROUND(H58*21,2) |  |  |  |  |
| 62160 | Provisie - dubbel vakantiegeld (92% van het maandbruto / 12) |  |  |  |  |  | 0.92 |  | =ROUND(J35*H59/12,2) |  |  |  |  |
| 62901 | Provisie - eindejaarspremie (dertiende maand, 1/12) |  |  |  |  |  |  |  | =ROUND(J35/12,2) |  |  |  |  |
| 23671 | Werkgeversbijdragen op de provisie eindejaarspremie |  |  |  |  |  | 0.25 |  | =ROUND(J60*H61,2) |  |  |  |  |
|  | TOTALE MAANDELIJKSE LOONKOST WERKGEVER |  |  |  |  |  |  |  | =SUM(J56:J61) |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| BEREKENINGSBASIS BEDRIJFSVOORHEFFING (PARAMETERS 2026) |  |  |  |  |  |  |  |  |  |  | BEREKENINGSBASIS SOCIALE WERKBONUS (PARAMETERS 2026) |  |  |
| Stap | Berekening |  |  |  |  |  |  | Bedrag (EUR) |  |  | Item | Waarde | Toelichting |
| 1 | Brutobezoldiging |  |  |  |  |  |  | =J35 |  |  | Toepasselijke parameterrij | 1 juli 2026 | Loonperiode 01/07/2026 - 31/07/2026. De parameters wijzigen vijfmaal in 2026 (1 januari, 1 maart, 1 april, 1 juli, 1 september). Kies de rij op basis van de LOONMAAND, niet op basis van het jaar. |
| 2 | Persoonlijke RSZ-bijdrage, 13,07% |  |  |  |  |  |  | =-J39 |  |  | Werknemerscategorie | Bediende | De maxima voor arbeiders zijn de maxima voor bedienden x 1,08 (EUR 185,75 component B, EUR 137,74 component A), omdat de bijdrage op de 108%-basis wordt berekend. De loongrenzen zijn voor beide gelijk. |
| 3 | Sociale werkbonus - nul: het referteloon van 3.500,00 overschrijdt beide nulpunten die gelden vanaf 1 juli 2026, namelijk 2.937,93 voor component B en 3.336,98 voor component A |  |  |  |  |  |  | =-J40 |  |  | Prestatiebreuk, begrensd tot 1,00 | =IFERROR(MIN(1,(C29+D29+E29)/B29),0) | Gewerkte dagen plus feestdagen plus betaalde verlofdagen, gedeeld door de arbeidsdagen in de maand (J/D). |
| 4 | Belastbare basis |  |  |  |  |  |  | =I66+I67+I68 |  |  | Referteloon S aan 100%, voltijds equivalent | =IF(M68=0,0,ROUND(J35/M68,2)) | S is het voltijds equivalente referteloon aan 100%. Voor een arbeider is dit het loon aan 100%, NIET de bijdragebasis aan 108%. |
| 5 | Geannualiseerd, x 12 |  |  |  |  |  |  | =I69*12 |  |  | Component B - volledig bedrag tot S_B | 2300.62 |  |
| 6 | Forfaitaire beroepskosten, 30% begrensd op 6.070,00 |  |  |  |  |  |  | =-MIN(ROUND(I70*0.3,2),6070.0) |  |  | Component B - maximum | 171.99 |  |
| 7 | Jaarlijks netto belastbaar |  |  |  |  |  |  | =I70+I71 |  |  | Component B - degressieve coefficient | 0.2699 |  |
| 8 | Belasting, schijf 1 - 16.710,00 x 26,75% |  |  |  |  |  |  | =ROUND(MIN(I72,16710.0)*0.2675,2) |  |  | Component B - nul vanaf S_A | 2937.93 |  |
| 9 | Belasting, schijf 2 - 12.790,00 x 42,80% |  |  |  |  |  |  | =ROUND(MAX(0,MIN(I72,29500.0)-16710.0)*0.428,2) |  |  | Component A - volledig bedrag tot S_A | 2937.93 |  |
| 10 | Belasting, schijf 3 - 940,60 x 48,15% |  |  |  |  |  |  | =ROUND(MAX(0,MIN(I72,51050.0)-29500.0)*0.4815,2) |  |  | Component A - maximum | 127.54 |  |
| 11 | Belasting, schijf 4 - nihil boven 51.050,00 |  |  |  |  |  |  | =ROUND(MAX(0,I72-51050.0)*0.535,2) |  |  | Component A - degressieve coefficient | 0.3196 |  |
| 12 | Jaarbelasting voor verminderingen |  |  |  |  |  |  | =SUM(I73:I76) |  |  | Component A - nul vanaf S_zero | 3336.98 |  |
| 13 | Vermindering belastingvrije som - 11.170,00 x 26,75% |  |  |  |  |  |  | =-ROUND(11170.0*0.2675,2) |  |  | R_B - toegekende component B | =IF(M69>M73,0,MAX(0,ROUND(M71-M72*MAX(0,M69-M70),2))) | Maximum tot en met S_B; degressief tussen S_B en S_A; nul boven S_A. |
| 14 | Jaarlijkse bedrijfsvoorheffing |  |  |  |  |  |  | =I77+I78 |  |  | R_A - toegekende component A | =IF(M69>M77,0,MAX(0,ROUND(M75-M76*MAX(0,M69-M74),2))) | Maximum tot en met S_A; degressief tussen S_A en S_zero; nul boven S_zero. |
| 15 | Maandelijkse bedrijfsvoorheffing, / 12 |  |  |  |  |  |  | =ROUND(I79/12,2) |  |  | P = R_B + R_A, voltijds equivalent | =ROUND(M78+M79,2) | De twee componenten worden afzonderlijk berekend en opgeteld. |
| 16 | Kwartaalloon voor de bijzondere bijdrage, 3 x 3.500,00 |  |  |  |  |  |  | =J35*3 |  |  | P geproratiseerd met de prestatiebreuk | =ROUND(M80*M68,2) |  |
| 17 | Bijzondere bijdrage per kwartaal - tabel met zes schijven op het kwartaalloon; dit kwartaal valt in de schijf EUR 6.570,55 tot EUR 11.211,00: 30,99 + 1,10% x (10.500,00 - 6.570,54) |  |  |  |  |  |  | =ROUND(30.99+0.011*(I81-6570.54),2) |  |  | P begrensd tot de verschuldigde persoonlijke bijdrage | =MIN(M81,J39) | De werkbonus kan nooit hoger zijn dan de bijdrage van 13,07% zelf en kan die nooit negatief maken. |
| 18 | Bijzondere bijdrage per maand, / 3 |  |  |  |  |  |  | =ROUND(I82/3,2) |  |  | Jaarlijks plafond | zie toelichting | EUR 3.466,44 per kalenderjaar vanaf 1 januari 2026 en EUR 3.523,92 vanaf 1 april 2026. NIET GEVONDEN - het plafond na de indexering van 1 juli 2026; het mag niet worden geextrapoleerd. Niet bindend voor een specimen van een enkele maand. |
|  |  |  |  |  |  |  |  |  |  |  | Rechtsgrond: Wet van 20 december 1999, artikel 2, uitgevoerd bij het koninklijk besluit van 17 januari 2000 (BS 28 januari 2000), gewijzigd bij de koninklijke besluiten van 27 maart 2023 en 5 maart 2024; RSZ-administratieve instructies 2026/1 en 2026/2, bijlage werkbonus. Sinds 1 april 2024 bestaat de werkbonus uit TWEE componenten. Elke component kent haar maximum enkel toe tot en met haar eigen ondergrens en is degressief tussen die grens en haar eigen nulpunt - het volledige maximum toekennen overal onder de bovengrens overschat de werkbonus en is onjuist. |  |  |
| CUMULATIEVE BEDRAGEN SINDS 1 JANUARI (JANUARI - JULI 2026) |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Omschrijving |  |  |  |  |  |  |  | Bedrag (EUR) |  |  |  |  |  |
| Cumulatief gewoon brutoloon, 7 x 3.500,00 |  |  |  |  |  |  |  | =3500.0*7 |  |  |  |  |  |
| Cumulatief dubbel vakantiegeld, betaald in mei 2026 (92%) |  |  |  |  |  |  |  | =ROUND(3500.0*0.92,2) |  |  |  |  |  |
| Cumulatief totaal bruto |  |  |  |  |  |  |  | =SUM(I87:I88) |  |  |  |  |  |
| Cumulatieve persoonlijke RSZ-bijdrage, 13,07% |  |  |  |  |  |  |  | =ROUND(J39,2)*7+ROUND(I88*0.1307,2) |  |  |  |  |  |
| Cumulatieve bedrijfsvoorheffing, gewone bezoldigingen en dubbel vakantiegeld aan 47,44% |  |  |  |  |  |  |  | =J41*7+ROUND((I88-ROUND(I88*0.1307,2))*0.4744,2) |  |  |  |  |  |
| Cumulatieve bijzondere bijdrage, kwartalen 1 en 2 plus de julischijf |  |  |  |  |  |  |  | =74.21+134.45+24.74 |  |  |  |  |  |
| Cumulatief werknemersaandeel maaltijdcheques, 139 cheques x 1,09 |  |  |  |  |  |  |  | =ROUND(139*1.09,2) |  |  |  |  |  |
| Cumulatief nettoloon |  |  |  |  |  |  |  | =I89-I90-I91-I92-I93 |  |  |  |  |  |
| Cumulatieve werkgeversbijdrage, enkel op de gewone bezoldigingen (dubbel vakantiegeld draagt geen werkgeversbijdrage) |  |  |  |  |  |  |  | =ROUND(3500.0*0.25,2)*7 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| VERLOFSALDI |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Verlofsoort |  |  |  | Recht | Opgenomen | Saldo | Wettelijke basis |  |  |  |  |  |  |
| Wettelijke jaarlijkse vakantie - dienstjaar 2025, vijfdagenweek |  |  |  | 20 | 6 | =E99-F99 | Koninklijk besluit van 30 maart 1967 - vier weken |  |  |  |  |  |  |
| Feestdagen, inclusief vervangingsdagen |  |  |  | 10 | 6 | =E100-F100 | Wet van 4 januari 1974 - tien betaalde dagen per jaar |  |  |  |  |  |  |
| Europese vakantie |  |  |  | 0 | 0 | =E101-F101 | Niet van toepassing - de werknemer heeft een volledig dienstjaar 2025 |  |  |  |  |  |  |
| Zorgverlof (onbezoldigd) |  |  |  | 10 | 0 | =E102-F102 | Tien dagen per kalenderjaar, onbezoldigd |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| BETALINGSGEGEVENS |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Naam van de bank |  | IBAN |  | BIC | Begunstigde | Betaalwijze |  | Munteenheid |  |  |  |  |  |
| ING Belgium NV |  | BE68 5390 0754 7034 |  | BBRUBEBB | Jan Peeters | SEPA-overschrijving |  | EUR |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| WETTELIJKE VERMELDINGEN - INKOMSTENJAAR 2026 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| - Taal. Deze loonbrief wordt in het Nederlands opgesteld omdat de exploitatiezetel van de werkgever in het Nederlandse taalgebied ligt (Decreet van 19 juli 1973); de sanctie bij een verkeerde taal is nietigheid van het document. Belgie laat geen tweetalige personeelsdocumenten toe: het Engelstalige blad is enkel een hoffelijkheidsvertaling zonder rechtsgevolg. Belgie telt drie taalgebieden en twee daarvan zijn nog niet opgeleverd: een Franstalige versie is een verplichte tweede deliverable voor werkgevers met een exploitatiezetel in het Franse taalgebied, en een Duitstalige versie is een uitdrukkelijk niet-gebouwd onderdeel voor werkgevers met een exploitatiezetel in het Duitse taalgebied. Beide zijn gedocumenteerd als bekende beperkingen van deze build. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| - Persoonlijke RSZ-bijdrage. Enige globale bijdrage van 13,07% op het brutoloon (Wet van 27 juni 1969, artikelen 14 en 23; Koninklijk besluit van 28 november 1969). Sinds 1 april 2024 bestaat de sociale werkbonus uit twee componenten, die afzonderlijk worden berekend en opgeteld (Wet van 20 december 1999, artikel 2; koninklijk besluit van 17 januari 2000, gewijzigd bij het koninklijk besluit van 5 maart 2024). Op de parameters die gelden vanaf 1 juli 2026 voor een bediende kent component B een maximum van EUR 171,99 toe tot en met een referteloon van EUR 2.300,62 en daalt zij degressief tot nul bij EUR 2.937,93; component A kent een maximum van EUR 127,54 toe tot en met EUR 2.937,93 en daalt degressief tot nul bij EUR 3.336,98. Elk maximum wordt enkel toegekend tot en met de eigen ondergrens, nooit overal onder de bovengrens. De werkbonus bedraagt hier nul omdat het referteloon van EUR 3.500,00 beide nulpunten overschrijdt. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| - Bedrijfsvoorheffing. Geannualiseerde niet-cumulatieve berekening volgens schaal nr. 31 van bijlage III, zoals gewijzigd bij het Koninklijk besluit van 11 december 2025: 26,75% tot EUR 16.710,00, 42,80% tot EUR 29.500,00, 48,15% tot EUR 51.050,00 en 53,50% daarboven. Forfaitaire beroepskosten van 30%, begrensd op EUR 6.070,00. De belastingvrije som van EUR 11.170,00 wordt toegekend als een vermindering van EUR 2.987,98 (11.170,00 x 26,75%). |  |  |  |  |  |  |  |  |  |  |  |  |  |
| - Bijzondere bijdrage voor de sociale zekerheid. Berekend op het KWARTAALLOON W volgens een tabel met zes schijven, en niet op het maandloon: tot EUR 5.836,14 nihil; EUR 5.836,15 tot EUR 6.570,54 = 4,22% x (W - 5.836,14); EUR 6.570,55 tot EUR 11.211,00 = EUR 30,99 + 1,10% x (W - 6.570,54); EUR 11.211,01 tot EUR 12.300,00 = EUR 82,05 + 3,38% x (W - 11.211,00); EUR 12.300,01 tot EUR 18.116,46 = EUR 118,83 + 1,10% x (W - 12.300,00); boven EUR 18.116,46 = EUR 182,82, het kwartaalmaximum voor een afzonderlijk belaste werknemer. De schijf wordt bepaald op het werkelijk betaalde kwartaalloon, zodat een kwartaal met dubbel vakantiegeld of een eindejaarspremie doorgaans in een hogere schijf valt dan een gewoon kwartaal - vandaar dat de kwartaalbedragen in het cumulatieve blok van elkaar verschillen. Ingehouden in maandelijkse schijven en definitief afgerekend bij de laatste betaling van het kwartaal (administratieve instructies RSZ 2026/2). |  |  |  |  |  |  |  |  |  |  |  |  |  |
| - Maaltijdcheques. Werknemersaandeel van EUR 1,09 en werkgeversaandeel van EUR 8,91 per cheque, aan een cheque per werkelijk gewerkte dag. Binnen deze grenzen is de cheque vrijgesteld van socialezekerheidsbijdragen en van belasting. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| - Jaarlijkse vakantie. Vier weken - 20 dagen bij een vijfdagenweek - opgebouwd in het voorafgaande vakantiedienstjaar (Koninklijk besluit van 30 maart 1967). Het dubbel vakantiegeld van 92% van het maandelijks brutoloon wordt afzonderlijk in mei uitbetaald en volgt een eigen voorheffingsschaal. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| - Loonkost werkgever. Het faciale werkgeversbijdragepercentage van ongeveer 25% en de provisies voor dubbel vakantiegeld en eindejaarspremie worden ter informatie vermeld; zij worden niet op de werknemer ingehouden. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| - Cumulatieve gegevens zijn niet verplicht op de Belgische loonbrief en worden via de individuele rekening verstrekt; zij worden hier ter transparantie opgenomen. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| - Bewaring en vorm. De werkgever bewaart de loonbrief en de individuele rekening gedurende vijf jaar. Een elektronische loonbrief vereist de toestemming van de werknemer op grond van de Wet van 3 juni 2007 betreffende de elektronische sociale documenten. |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Dit document is gegenereerd door het Mercans Payroll System |  |  |  |  |  |  |  |  |  |  |  |  |  |
| BE-PSL-001 v1.0 - inkomstenjaar 2026 - alle rechten voorbehouden |  |  |  |  |  |  |  |  |  |  |  |  |  |

## Sheet: `Payslip Spec`

|  | BELGIUM PAYSLIP SPECIFICATION - field-by-field mapping for the Mercans HR Payroll engine (BE-PSL-001 v1.0, income year 2026) |  |  |  |
| --- | --- | --- | --- | --- |
|  | Header Details  /  Kopgegevens |  |  |  |
|  | Field Name (EN) | Field Name (NL) | HRP Mapping (TA & BA) | Field Explanation |
|  | Payslip Title | Titel loonbrief | Report Title in English: Payslip <br> Report Title in Dutch: Loonbrief | Document title displayed in the navy title bar. Identifies the country and the document type. |
|  | Statutory Basis Subtitle | Wettelijke grondslag (ondertitel) | static text below the employer name: 'Statutory payslip (loonbrief) - Wage Protection Act of 12 April 1965, Article 15; Royal Decree of 20 September 2009' | Names the instruments that make the document mandatory. Belgian law prescribes the CONTENT of the payslip and not its layout, so this line, and not a prescribed form number, is the compliance anchor of the document. |
|  | Company Logo | Bedrijfslogo | static image asset | Mercans corporate logo anchored at cell A1 of both language sheets. |
|  | Pay Period | Loonperiode | CONCAT(DATE_FORMAT($period.begin_date;'dd/MM/yyyy');' - ';DATE_FORMAT($period.end_date;'dd/MM/yyyy')) | Period covered by the payment. Mandatory content under the Royal Decree of 20 September 2009. |
|  | Pay Date | Betaaldatum | DATE_FORMAT($payroll.payment_date;'dd/MM/yyyy') | Date on which the net amount is credited. Mandatory content under the Royal Decree of 20 September 2009. |
|  | Net Pay Summary | Samenvatting nettoloon | column calculated value 'Net Pay' | Prominent net pay box in the top right corner, repeating the net amount due and paid. |
|  | Currency | Munteenheid | $legal_entity.currency | EUR with two decimal places. All Belgian statutory outputs are denominated in euro. |
|  |  |  |  |  |
|  | Employer Fields  /  Gegevens van de werkgever |  |  |  |
|  | Field Name (EN) | Field Name (NL) | HRP Mapping (TA & BA) | Field Explanation |
|  | Employer Legal Name | Naam van de werkgever | $legal_entity.name | Legal name of the employer. Mandatory identification content. |
|  | Establishment Unit Address | Adres van de vestigingseenheid | CONCAT($legal_entity_address.1.address_line_1;' ';$legal_entity_address.1.postal_code;' ';$legal_entity_address.1.city) | Address of the place of activity. It determines the language regime that applies to the payslip. |
|  | Enterprise Number (KBO / BCE) | Ondernemingsnummer (KBO / BCE) | $legal_entity.registration_number | Ten digits, first digit 0 or 1, last two a modulo-97 check on the preceding eight. Source: BE-DD-001 legal entity fields. |
|  | Establishment Unit Number | Vestigingseenheidsnummer | $legal_entity.custom.establishment_unit_number | Ten digits beginning with 2, granted per physical place of activity. |
|  | NSSO Employer Registration Number | RSZ-werkgeversnummer | $legal_entity.social_security_number | Employer identification number of the National Social Security Office. Mandatory identification content on the payslip. |
|  | NSSO Employer Category | RSZ-werkgeverscategorie | $legal_entity.custom.nsso_employer_category | Three-digit category that selects the employer contribution obligations and the DmfA codes available. |
|  | VAT Number | BTW-nummer | $legal_entity.tax_registration_number | The letters 'BE' followed by the ten-digit enterprise number. Source: BE-DD-001 ID Information, country-specific legal entity field 'VAT Number'. |
|  | NACE Activity Code | NACE-activiteitscode | $legal_entity.custom.nace_activity_code | Five-digit NACE-BEL code of the main activity of the establishment unit. Drives the work accident tariff and the sectoral obligations. Source: BE-DD-001 ID Information, 'NACE Activity Code'. |
|  | Joint Committee | Paritair comité | $legal_entity.custom.joint_committee | Mandatory payslip content. Drives the sectoral scales, the end-of-year premium and the sectoral funds. |
|  | Withholding Tax Registration Number | Registratienummer bedrijfsvoorheffing | $legal_entity.custom.wage_withholding_tax_registration_number | Registration under which the wage withholding tax is declared and paid through Finprof. Source: BE-DD-001 ID Information, 'Wage Withholding Tax Registration Number'. |
|  | Work Accident Policy | Polis arbeidsongevallen | CONCAT($legal_entity.custom.work_accident_policy_number;' / ';$legal_entity.custom.work_accident_insurer_identification) | Policy number and the identification of the accident insurer. Every employer must be insured from the first day of employment (Law of 10 April 1971). Source: BE-DD-001 ID Information, 'Work Accident Policy Number' and 'Work Accident Insurer Identification'. |
|  | Payslip Language Regime | Taalregeling loonbrief | $legal_entity.custom.language_regime_of_personnel_documents | Language in which personnel documents must be drawn up, fixed by the region of the establishment unit and not by the parties (Decree of 19 July 1973 for the Dutch-language region). The sanction for the wrong language is nullity of the document. Source: BE-DD-001 Country Fields, 'Language Regime of Personnel Documents'. |
|  |  |  |  |  |
|  | Employee Fields  /  Gegevens van de werknemer |  |  |  |
|  | Field Name (EN) | Field Name (NL) | HRP Mapping (TA & BA) | Field Explanation |
|  | Employee Full Name | Naam van de werknemer | CONCAT($person.first_name;' ';$person.last_name) | Name of the employee. Mandatory identification content. |
|  | National Register Number (INSZ) | Rijksregisternummer (INSZ) | $person.national_id | Eleven digits: date of birth, sequence number odd for men and even for women, and a modulo-97 check. Key of the whole social security chain. |
|  | Employee Code | Werknemersnummer | $employee.reference_code | Employer's own payroll reference, carried through the declarations as a correlation key. |
|  | Date of Birth | Geboortedatum | DATE_FORMAT($person.birth_date;'dd/MM/yyyy') | Date of birth. It is also encoded in the first six positions of the INSZ and is reported in zone 2.009 of the 281.10. Source: BE-DD-001 Country Fields, 'Date of Birth'. |
|  | Job Title | Functie | $job.job_description | Function performed, used with the joint committee to determine the applicable minimum scale. |
|  | Department | Afdeling | $employee.department | Department or cost centre to which the occupation is attached. Carries the analytical allocation of the payroll result; not itself mandatory payslip content. |
|  | Worker Status | Statuut | $employee.custom.worker_status | Blue-collar or white-collar. Drives the 108% contribution base, the holiday pay route and the guaranteed salary scale. |
|  | DmfA Worker Code | DmfA-werknemerskengetal | $employee.custom.nsso_worker_code | Three-digit NSSO worker code - 495 for an ordinary white-collar employee - which selects the contribution set applied in the DmfA. Source: BE-DD-001 Country Fields, 'NSSO Worker Code'. |
|  | Working Time Regime | Arbeidsregeling | CONCAT($employee.custom.contract_type;', ';$employee.custom.mean_weekly_working_hours;'h/week, ';$employee.custom.working_days_system;'-day week') | Contractual working time regime. Mandatory payslip content under the Royal Decree of 20 September 2009. It renders as 'Full-time, 38h/week, 5-day week' (NL 'Voltijds, 38u/week, vijfdagenweek'), which is a COMPOSITE of three DD fields and not a single one. BE-X10-013, fixed 2026-08-17: the mapping previously read '$employee.custom.working_time_regime', which resolves to no BE-DD-001 field. It is now bound to the three fields that actually source the three limbs of the rendered value: 'Contract Type' (option mapper Contract Type, 0 = Full time / 1 = Part time, NSSO zone 00050) for the full-time / part-time limb - this is the DD field of that name and NOT 'Contract Duration Type', which is the separate field mapped at row 40; 'Mean Weekly Working Hours' (BE-NSSO-002 Mean Working Hours, BE-NSSO-004 block 90068) for the hours limb, the same field already mapped alone at row 52; and 'Working Days System' (local label 'Arbeidsregeling - dagen per week', BE-NSSO-002 Working Days System, BE-NSSO-004 block 90068) for the days-per-week limb. 'Working Time Cycle' is NOT the source, although it is the field the Stage 10 report named: it is the length of the cycle where a schedule repeats over more than one week, declared in the BE-FEDRIS-001 and BE-NSSO-004 calculation-basis blocks 90032 and 90013, which is a different concept from the regime. The DD states the composition itself - 'Working Days System' is described as the number of days per week of the working-time regime which, TOGETHER WITH THE AVERAGE WEEKLY HOURS, defines the regime - and its Dutch label is the same word, Arbeidsregeling, that this row carries. Source: BE-DD-001 Country Fields, 'Contract Type', 'Mean Weekly Working Hours' and 'Working Days System'. |
|  | Hire Date | Datum indiensttreding | DATE_FORMAT($employee.hire_date;'dd/MM/yyyy') | Start of the employment relationship, used for seniority and for the notice periods. |
|  | Seniority | Anciënniteit | $employee.custom.seniority_date_for_notice | Length of service, derived from the seniority reference date. Drives the notice periods of the Unified Status Act and the sectoral seniority scales of joint committee 200. Source: BE-DD-001 Country Fields, 'Seniority Date for Notice'. |
|  | Contract Duration Type | Type overeenkomst (duur) | $employee.custom.contract_duration_type | Indefinite duration, fixed term, clearly defined work, replacement, student or flexi-job contract - the six values of the Contract Duration Type mapper. Mandatory payslip content under the Royal Decree of 20 September 2009 and a Dimona input. Source: BE-DD-001 Country Fields, 'Contract Duration Type' (mapper block B52:F57). NOT to be confused with BE-DD-001 'Contract Type', which is the FULL-TIME / PART-TIME field (mapper block B48:F49, NSSO DmfA zone 00050) and is a different domain. |
|  | Withholding Scale and Family Situation | Schaal bedrijfsvoorheffing en gezinstoestand | $employee.custom.withholding_scale | Scale I, II or III with the dependants counter. Drives the reduction of the basisbelasting under Annex III nr. 38. |
|  | Bank Account (IBAN) | Bankrekening (IBAN) | $primary_employee_bank_account.iban | Sixteen-character Belgian IBAN credited with the net amount. Payment in cash requires the written agreement of the employee (Wage Protection Act of 12 April 1965, Article 5). Source: BE-DD-001 Country Fields, 'Employee Bank Account IBAN'. |
|  |  |  |  |  |
|  | Working Time Fields  /  Arbeidstijd |  |  |  |
|  | Field Name (EN) | Field Name (NL) | HRP Mapping (TA & BA) | Field Explanation |
|  | Calendar Days | Kalenderdagen | $period.calendar_days | Calendar days in the pay period. Denominator of the calendar-day proration method and the basis of the guaranteed salary count in a period of incapacity. |
|  | Working Days in the Month | Arbeidsdagen in de maand | $actual_prorata_days | Working days of the month under the employee's working days system. Denominator of the working-day proration method, which is the market-standard method used for the basic salary line 62100. Source: BE-DD-001 Country Fields, 'Working Days System'. |
|  | Days Worked | Gewerkte dagen | $employee_time.days_worked | Days actually worked in the period. Drives the meal voucher count, which is granted at one voucher per day actually worked, and is declared in the DmfA occupation block. |
|  | Public Holiday Days | Feestdagen | $employee_time.public_holiday_days | Paid public holidays and replacement days falling in the period. Ten paid days per calendar year (Law of 4 January 1974); paid at the daily value of the monthly salary through pay element 62964. |
|  | Paid Leave Days | Betaalde verlofdagen | $employee_time.paid_leave_days | Statutory annual leave days taken in the period, earned in the preceding holiday service year (Royal Decree of 30 March 1967). Shown separately because they must be distinguishable from days worked. |
|  | Unpaid Absence Days | Onbezoldigde afwezigheidsdagen | $employee_time.unpaid_absence_days | Days not covered by salary. Valued through pay element 21100 with the same proration method as the basic salary and declared in the DmfA with the applicable absence code, which also decides whether the day is an equivalent day for holiday accrual. |
|  | Contractual Hours per Week | Contractuele uren per week | $employee.custom.mean_weekly_working_hours | Contractual weekly working time - 38 hours for a full-time employee in joint committee 200. Source: BE-DD-001 Country Fields, 'Mean Weekly Working Hours'. |
|  | Hours Worked | Gewerkte uren | $employee_time.hours_worked | Number of hours to which the pay relates - mandatory payslip content under the Royal Decree of 20 September 2009. Equal to days worked multiplied by the daily hours of the work schedule. Source: BE-DD-001 Country Fields, 'Work Schedule Hours per Day'. |
|  |  |  |  |  |
|  | Earnings Fields  /  Loonbestanddelen |  |  |  |
|  | Field Name (EN) | Field Name (NL) | HRP Mapping (TA & BA) | Field Explanation |
|  | Earning Code | Looncode | $pay_element.code | Mercans pay element code from BE-WTC-001. Global codes are 62xxx; Belgium-specific additions carry a BE-0xx reference. |
|  | Earning Description | Omschrijving looncomponent | $pay_element.description_local | Each premium, allowance and supplement must appear separately - aggregation is not permitted. |
|  | Rate | Tarief | $pay_element.rate | Unit rate applied. For the basic salary this is the daily value of the monthly salary under the working-day proration method. |
|  | Unit | Eenheid | $pay_element.units | Number of units. Days for prorated salary, hours for overtime, vouchers for meal vouchers. |
|  | Earning Amount | Bedrag | $pay_element.amount | Rate multiplied by units, rounded to the eurocent at each presented line. |
|  | Gross Remuneration | Brutoloon | SUM of all earnings pay elements | Gross salary that forms both the NSSO contribution base and the starting point of the taxable base. Mandatory payslip content. |
|  | Overtime Hours and Supplement | Overuren en toeslag | $pay_element.62111.units / $pay_element.62111.amount | Overtime hours and the overtime supplement must be shown separately from ordinary pay. |
|  | Meal Vouchers Granted | Toegekende maaltijdcheques | $pay_element.62660.units | Number and value of the vouchers granted. Mandatory non-cash entitlement content. |
|  |  |  |  |  |
|  | Deductions Fields  /  Inhoudingen |  |  |  |
|  | Field Name (EN) | Field Name (NL) | HRP Mapping (TA & BA) | Field Explanation |
|  | Employee Social Security Contribution | Persoonlijke socialezekerheidsbijdrage | $pay_element.21900.amount | Single global contribution of 13.07% of the gross. Must be shown separately on the payslip. |
|  | Social Work Bonus | Sociale werkbonus | $pay_element.BE-002.amount | Reduction of the employee contribution for low wages. Must be shown as a separate reduction, not netted into the contribution. |
|  | Wage Withholding Tax | Bedrijfsvoorheffing | $pay_element.BE-004.amount | Annualised non-cumulative withholding on the Annex III nr. 31 scale. Mandatory payslip content. |
|  | Special Social Security Contribution | Bijzondere bijdrage voor de sociale zekerheid | $pay_element.BE-001.amount | Quarterly banded employee levy, withheld in monthly instalments. Must be shown separately. |
|  | Meal Voucher Employee Part | Werknemersaandeel maaltijdcheque | $pay_element.BE-011.amount | Statutory minimum employee share of EUR 1.09 per voucher, withheld from net pay. |
|  | Garnishment or Wage Assignment | Loonbeslag of loonoverdracht | $pay_element.BE-013.amount | Any attachment must be shown with the amount withheld, computed on the Article 1409 protected bands. |
|  | Total Deductions | Totaal inhoudingen | SUM of all deduction pay elements | Sum of every deduction line. Each other deduction must be itemised individually with its reason. |
|  | Net Amount Due and Paid | Nettobedrag verschuldigd en uitbetaald | Gross Remuneration - Total Deductions | The net amount due and the amount actually paid, with the payment method. Mandatory payslip content. |
|  |  |  |  |  |
|  | Net Pay  /  Nettoloon |  |  |  |
|  | Field Name (EN) | Field Name (NL) | HRP Mapping (TA & BA) | Field Explanation |
|  | Net Pay Band | Nettobedrag (uitgelicht) | column calculated value 'Net Pay' | Highlighted band restating the net amount due and actually paid. Mandatory payslip content under the Royal Decree of 20 September 2009; the same value is repeated in the summary box of the header. |
|  | Payment Confirmation Statement | Bevestiging van de betaling | CONCAT('Paid by ';$employee.custom.wage_payment_method;' to ';$primary_employee_bank_account.iban;' on ';DATE_FORMAT($payroll.payment_date;'dd/MM/yyyy')) | Sentence naming the payment method, the account credited and the payment date, and confirming that the amount due and the amount actually paid are identical. The payslip must show the amount actually paid and not only the amount due (Wage Protection Act of 12 April 1965). |
|  |  |  |  |  |
|  | Non-Cash Entitlements  /  Voordelen in natura en cheques |  |  |  |
|  | Field Name (EN) | Field Name (NL) | HRP Mapping (TA & BA) | Field Explanation |
|  | Entitlement Code | Code voordeel | $pay_element.code | Mercans pay element code of the non-cash entitlement from BE-WTC-001: 62660 meal vouchers, 62870 eco vouchers. |
|  | Entitlement Description | Omschrijving voordeel | $pay_element.description_local | Each entitlement appears on its own line. A period in which no entitlement is granted is shown with a nil count rather than suppressed, so the reader can see that the entitlement exists. |
|  | Number Granted | Aantal | $pay_element.units | Number of vouchers granted. A meal voucher is granted at one voucher per day actually worked; the sectoral eco voucher of joint committee 200 is issued once a year. |
|  | Face Value | Nominale waarde | $pay_element.rate | Face value of one voucher. The meal voucher face value may not exceed EUR 10.00, of which the employer bears at most EUR 8.91 and the employee at least EUR 1.09. |
|  | Total Value | Totale waarde | $pay_element.amount | Number granted multiplied by the face value. Mandatory non-cash entitlement content - the benefit must be identified and valued on the payslip. |
|  | Employer Part | Werkgeversaandeel | $pay_element.BE-012.amount | Employer share of the voucher. Within the statutory limits the voucher is exempt from social security contributions and from income tax, and the employer share is not deducted from the employee. |
|  |  |  |  |  |
|  | Employer Contributions and Total Cost  /  Werkgeversbijdragen en totale loonkost |  |  |  |
|  | Field Name (EN) | Field Name (NL) | HRP Mapping (TA & BA) | Field Explanation |
|  | Employer Contribution Code | Code werkgeversbijdrage | $pay_element.code | Mercans pay element code from BE-WTC-001, category Employer Contribution: 23671 global employer contribution, BE-012 meal voucher employer part, 62160 and 62901 the deferred-pay provisions. |
|  | Employer Contribution Description | Omschrijving werkgeversbijdrage | $pay_element.description_local | Description of each employer-borne line. Shown for information only; no line in this block is withheld from the employee. |
|  | Rate | Tarief | $pay_element.rate | Rate applied to the contribution base - approximately 25% facial rate for the global employer contribution, 92% for the double holiday pay provision, 1/12 for the end-of-year premium provision. |
|  | Employer Contribution Amount | Bedrag werkgeversbijdrage | $pay_element.amount | Monetary amount of each employer line, rounded to the eurocent at each presented line. |
|  | Employer Global Social Security Contribution | Globale werkgeversbijdrage sociale zekerheid | $pay_element.23671.amount | Single global employer contribution to the National Social Security Office, facial rate of approximately 25% of the gross for a category 017 white-collar employer (Law of 27 June 1969). The effective rate differs from the facial rate wherever a structural or target-group reduction applies. |
|  | Provisions for Deferred Pay | Provisies voor uitgesteld loon | $pay_element.62160.amount / $pay_element.62901.amount | Monthly accrual of the double holiday pay (92% of the monthly gross, divided by twelve) and of the end-of-year premium (one twelfth). Both are paid later in the year and are provisioned monthly so that the employer cost line is complete. |
|  | Total Monthly Employer Cost | Totale maandelijkse loonkost werkgever | Gross Remuneration + SUM of all employer contribution pay elements | Total cost of the employee to the employer for the period. Informational content: it is not part of the mandatory payslip content and is never deducted from the employee. |
|  |  |  |  |  |
|  | Withholding Tax Calculation Basis  /  Berekeningsbasis bedrijfsvoorheffing |  |  |  |
|  | Field Name (EN) | Field Name (NL) | HRP Mapping (TA & BA) | Field Explanation |
|  | Step 1 - Gross Remuneration | Stap 1 - Brutobezoldiging | SUM of all earnings pay elements | Starting point of the calculation: the same gross that forms the NSSO contribution base. |
|  | Step 2 - Employee Social Security | Stap 2 - Persoonlijke RSZ-bijdrage | $pay_element.21900.amount | The 13.07% employee contribution is deductible from the taxable base and is subtracted here as a negative amount. |
|  | Step 3 - Social Work Bonus | Stap 3 - Sociale werkbonus | $pay_element.BE-002.amount | Where the work bonus reduces the employee contribution, the reduction increases the taxable base by the same amount. Since 1 April 2024 the bonus has TWO components, computed separately and added (P = R_B + R_A). Each component pays its maximum only at or below its own full-amount (lower) limit, falls degressively between that limit and its own zero point, and is nil above it - the full maximum is never granted merely because the wage is below the upper limit. On the parameters in force from 1 July 2026 for a white-collar worker: component B, maximum EUR 171.99 up to EUR 2,300.62, coefficient 0.2699, nil from EUR 2,937.93; component A, maximum EUR 127.54 up to EUR 2,937.93, coefficient 0.3196, nil from EUR 3,336.98. The bonus is therefore nil above EUR 3,336.98. Blue-collar maxima are these x 1.08; the wage limits are identical. Prorated by the performance fraction and capped at the contribution actually due. |
|  | Step 4 - Taxable Base | Stap 4 - Belastbare basis | Step 1 + Step 2 + Step 3 | Monthly taxable base of the ordinary remuneration. |
|  | Step 5 - Annualised Income | Stap 5 - Geannualiseerd inkomen | Step 4 x 12 | Belgium uses a non-cumulative annualised method: the monthly taxable base is multiplied by twelve, the annual withholding is computed, and the result is divided back by twelve. Each month stands alone; no year-to-date cumulation enters the calculation. |
|  | Step 6 - Lump-Sum Professional Expenses | Stap 6 - Forfaitaire beroepskosten | MIN(Step 5 x 30%; 6,070.00), as a negative amount | Statutory flat-rate professional expenses of 30% of the annualised income, capped at EUR 6,070.00 for income year 2026. The employee may claim real expenses in the annual tax return instead; that election does not change the withholding. |
|  | Step 7 - Annual Net Taxable | Stap 7 - Jaarlijks netto belastbaar | Step 5 + Step 6 | Annual income to which the scale of Annex III is applied. |
|  | Step 8 - Tax Slice 1 at 26.75% | Stap 8 - Belasting schijf 1 aan 26,75% | MIN(Step 7; 16,710.00) x 26.75% | First bracket of the Annex III nr. 31 scale as amended by the Royal Decree of 11 December 2025. The rate is the ordinary bracket rate plus the 6% municipal surcharge already embedded in the withholding scale. |
|  | Step 9 - Tax Slice 2 at 42.80% | Stap 9 - Belasting schijf 2 aan 42,80% | MAX(0; MIN(Step 7; 29,500.00) - 16,710.00) x 42.80% | Second bracket, from EUR 16,710.00 to EUR 29,500.00. |
|  | Step 10 - Tax Slice 3 at 48.15% | Stap 10 - Belasting schijf 3 aan 48,15% | MAX(0; MIN(Step 7; 51,050.00) - 29,500.00) x 48.15% | Third bracket, from EUR 29,500.00 to EUR 51,050.00. |
|  | Step 11 - Tax Slice 4 at 53.50% | Stap 11 - Belasting schijf 4 aan 53,50% | MAX(0; Step 7 - 51,050.00) x 53.50% | Top bracket above EUR 51,050.00. The slice is rendered even when it is nil, so that the reader can see the whole scale that was applied. |
|  | Step 12 - Annual Tax Before Reductions | Stap 12 - Jaarbelasting voor verminderingen | SUM(Step 8 : Step 11) | Basisbelasting before any reduction. |
|  | Step 13 - Reduction for the Tax-Free Allowance | Stap 13 - Vermindering belastingvrije som | 11,170.00 x 26.75%, as a negative amount | The basic tax-free allowance of EUR 11,170.00 is not deducted from the income; it is delivered as a reduction of the tax, valued at the first bracket rate - EUR 2,987.98. Further reductions for dependants, disability and the fiscal work bonus attach at this same step under Annex III nr. 38 and are nil for a Scale I employee with no dependants. |
|  | Step 14 - Annual Withholding | Stap 14 - Jaarlijkse bedrijfsvoorheffing | Step 12 + Step 13 | Annual wage withholding tax after reductions. |
|  | Step 15 - Monthly Withholding Tax | Stap 15 - Maandelijkse bedrijfsvoorheffing | Step 14 / 12 | The withholding actually deducted, carried to the deduction line BE-004. Mandatory payslip content. |
|  | Step 16 - Quarterly Wage for the Special Contribution | Stap 16 - Kwartaalloon voor de bijzondere bijdrage | SUM of the taxable remuneration of the three months of the quarter | The special social security contribution is banded on the QUARTERLY wage, not on the monthly wage. The quarterly wage includes exceptional remuneration paid in the quarter - double holiday pay, the end-of-year premium, a CBA no. 90 bonus - which can move the quarter into a higher band. |
|  | Step 17 - Special Contribution per Quarter | Stap 17 - Bijzondere bijdrage per kwartaal | six-band table on the quarterly wage W: up to 5,836.14 nil; 5,836.15-6,570.54 = 4.22% x (W - 5,836.14); 6,570.55-11,211.00 = 30.99 + 1.10% x (W - 6,570.54); 11,211.01-12,300.00 = 82.05 + 3.38% x (W - 11,211.00); 12,300.01-18,116.46 = 118.83 + 1.10% x (W - 12,300.00); above 18,116.46 = 182.82 (maximum) | Employee levy of the Law of 30 March 1994, banded on the quarterly wage. The band must be selected on the wage of the quarter actually paid: a quarter carrying double holiday pay or the end-of-year premium commonly falls one or two bands higher than an ordinary quarter, so an implementation that hardcodes a single band returns the wrong figure for most white-collar employees in the second and fourth quarters. Trued up at the last payment of each quarter, once the quarterly wage is final. |
|  | Step 18 - Special Contribution per Month | Stap 18 - Bijzondere bijdrage per maand | Step 17 / 3 | The quarterly contribution is withheld in three monthly instalments and carried to the deduction line BE-001 (NSSO administrative instructions 2026/2). |
|  |  |  |  |  |
|  | Year-to-Date Cumulative Figures  /  Cumulatieve bedragen |  |  |  |
|  | Field Name (EN) | Field Name (NL) | HRP Mapping (TA & BA) | Field Explanation |
|  | Year-to-Date Ordinary Gross Remuneration | Cumulatief gewoon brutoloon | SUM of all earnings pay elements from the first period of the calendar year | Cumulative ordinary gross since 1 January, excluding the exceptional remuneration shown on the following line. |
|  | Year-to-Date Double Holiday Pay | Cumulatief dubbel vakantiegeld | $pay_element.62160.amount, cumulative | Double holiday pay of 92% of the monthly gross, paid separately in May and taxed on its own exceptional-remuneration table. Shown apart because it enters the quarterly base of the special social security contribution and moves the quarter into a higher band. |
|  | Year-to-Date Total Gross | Cumulatief totaal bruto | Year-to-date ordinary gross + year-to-date exceptional gross | Total gross since 1 January. Reconciles with the sum of the four DmfA declarations and with box 250 of the 281.10 certificate. |
|  | Year-to-Date Employee Social Security | Cumulatieve persoonlijke RSZ-bijdrage | $pay_element.21900.amount, cumulative | Cumulative 13.07% employee contribution, including the contribution due on the double holiday pay. |
|  | Year-to-Date Wage Withholding Tax | Cumulatieve bedrijfsvoorheffing | $pay_element.BE-004.amount + $pay_element.BE-006.amount, cumulative | Cumulative withholding on the ordinary remuneration (BE-004) plus the withholding taken on the double holiday pay at its own table rate (BE-006). Reported in box 286 of the 281.10. |
|  | Year-to-Date Special Social Security Contribution | Cumulatieve bijzondere bijdrage | $pay_element.BE-001.amount, cumulative | Cumulative special contribution. Because the levy is banded per quarter, the cumulative figure is the sum of the completed quarterly amounts plus the instalments of the quarter in progress - it is not the monthly figure multiplied by the number of months. |
|  | Year-to-Date Meal Voucher Employee Part | Cumulatief werknemersaandeel maaltijdcheques | $pay_element.BE-011.amount, cumulative | Cumulative employee share of the vouchers granted, at EUR 1.09 per voucher. |
|  | Year-to-Date Net Pay | Cumulatief nettoloon | Year-to-date total gross - year-to-date deductions | Cumulative net paid since 1 January. |
|  | Year-to-Date Employer Social Security | Cumulatieve werkgeversbijdrage | $pay_element.23671.amount, cumulative | Cumulative employer contribution, on the ordinary remuneration only where the double holiday pay carries no employer contribution. Informational; not deducted from the employee. Cumulative data are not mandatory payslip content in Belgium - they are provided through the individual account - and are rendered here for transparency. |
|  |  |  |  |  |
|  | Leave Balances  /  Verlofsaldi |  |  |  |
|  | Field Name (EN) | Field Name (NL) | HRP Mapping (TA & BA) | Field Explanation |
|  | Leave Type | Verlofsoort | $absence_type.description_local | One row per leave type carried for the employee. The balance table is not mandatory payslip content; it is rendered here because the entitlement it reports is statutory. |
|  | Entitlement | Recht | $employee.custom.holiday_entitlement_in_days | Days of entitlement for the leave type in the current year. Source: BE-DD-001 Country Fields, 'Holiday Entitlement in Days'. |
|  | Taken | Opgenomen | $absence.days_taken | Days of that type already taken in the current year, including any days settled by a previous employer and reported on the holiday certificate. |
|  | Balance | Saldo | Entitlement - Taken | Remaining days. Statutory annual leave must be taken within the calendar year and may not be carried forward or paid out in place of being taken. |
|  | Legal Basis | Wettelijke basis | static text per leave type | Instrument that creates the entitlement, rendered on the row so that the reader can verify the entitlement without leaving the document. |
|  | Statutory Annual Leave | Wettelijke jaarlijkse vakantie | $absence_type.'statutory_annual_leave' | Four weeks - 20 days on a five-day week - earned in the preceding holiday service year (Royal Decree of 30 March 1967). For a white-collar employee the holiday pay is paid by the employer; for a blue-collar employee it is paid by the holiday fund on the 108% base. |
|  | Public Holidays | Feestdagen | $absence_type.'public_holiday' | Ten paid public holidays per calendar year, including replacement days for a holiday falling on a day of habitual inactivity (Law of 4 January 1974). |
|  | European Leave | Europese vakantie | $absence_type.'european_leave' | Supplementary leave for an employee starting or resuming activity in Belgium who has no full holiday service year. Nil where the service year is complete. Financed as an advance on the following year double holiday pay. |
|  | Care Leave | Zorgverlof | $absence_type.'care_leave' | Ten unpaid days per calendar year for compelling reasons. Unpaid days are shown in the working-time block as unpaid absence days and are valued through pay element 21100. |
|  |  |  |  |  |
|  | Payment Details  /  Betalingsgegevens |  |  |  |
|  | Field Name (EN) | Field Name (NL) | HRP Mapping (TA & BA) | Field Explanation |
|  | Bank Name | Naam van de bank | $primary_employee_bank_account.bank_name | Institution holding the account credited with the net amount. |
|  | IBAN | IBAN | $primary_employee_bank_account.iban | Sixteen-character Belgian IBAN, structure BE plus two check digits plus twelve digits. Source: BE-DD-001 Country Fields, 'Employee Bank Account IBAN'. |
|  | BIC | BIC | $primary_employee_bank_account.bic | Business identifier code of the beneficiary institution, eight or eleven characters. Required for the SEPA credit transfer instruction. Source: BE-DD-001 Country Fields, 'Employee Bank BIC'. |
|  | Beneficiary | Begunstigde | $primary_employee_bank_account.beneficiary_name | Beneficiary name, which must match the legal name of the employee. A payment to a third-party account requires a wage assignment or an attachment order. |
|  | Payment Method | Betaalwijze | $employee.custom.wage_payment_method | SEPA credit transfer in the ordinary case. Payment in cash is possible only with the written agreement of the employee, or where a collective agreement or custom allows it (Wage Protection Act of 12 April 1965, Article 5). Source: BE-DD-001 Country Fields, 'Wage Payment Method'. |
|  | Currency | Munteenheid | $primary_employee_bank_account.account_currency | EUR with two decimal places. Wages must be paid in euro (Wage Protection Act of 12 April 1965, Article 4). |
|  |  |  |  |  |
|  | Statutory Notes  /  Wettelijke vermeldingen |  |  |  |
|  | Field Name (EN) | Field Name (NL) | HRP Mapping (TA & BA) | Field Explanation |
|  | Language Regime Note | Vermelding taalregeling | static text, driven by the language regime of the establishment unit | States the language in which the payslip is issued and why, that Belgium does not permit bilingual personnel documents, and that the sanction for the wrong language is nullity. It also carries the disclosure of the language versions that are not yet delivered. |
|  | Employee Social Security Note | Vermelding persoonlijke RSZ-bijdrage | static text | Single global contribution of 13.07% of the gross (Law of 27 June 1969, Articles 14 and 23; Royal Decree of 28 November 1969) and the position of the social work bonus for this employee. |
|  | Wage Withholding Tax Note | Vermelding bedrijfsvoorheffing | static text | Annualised non-cumulative method, the four bracket rates of the Annex III nr. 31 scale as amended by the Royal Decree of 11 December 2025, the professional expenses cap and the tax-free allowance delivered as a reduction. |
|  | Special Social Security Contribution Note | Vermelding bijzondere bijdrage | static text | The six-band quarterly table applied to the special contribution, and the rule that the band is selected on the wage of the quarter actually paid (NSSO administrative instructions 2026/2). |
|  | Meal Voucher Note | Vermelding maaltijdcheques | static text | Employee and employer shares per voucher, one voucher per day actually worked, and the exemption from social security contributions and income tax within those limits. |
|  | Annual Leave Note | Vermelding jaarlijkse vakantie | static text | Four weeks earned in the preceding holiday service year (Royal Decree of 30 March 1967) and the separate May payment of the double holiday pay on its own withholding table. |
|  | Employer Cost Note | Vermelding loonkost werkgever | static text | States that the employer contribution block and the provisions are shown for information and are not deducted from the employee. Required so that the employer-cost block cannot be read as a deduction. |
|  | Cumulative Data Note | Vermelding cumulatieve gegevens | static text | States that cumulative data are not mandatory on the Belgian payslip, are provided through the individual account, and are shown here for transparency. |
|  | Retention and Format Note | Vermelding bewaring en vorm | static text | Five-year retention of the payslip and the individual account, and the requirement that an electronic payslip has the consent of the employee (Law of 3 June 2007 on electronic social documents). |
|  |  |  |  |  |
|  | Footer Details  /  Voetgegevens |  |  |  |
|  | Field Name (EN) | Field Name (NL) | HRP Mapping (TA & BA) | Field Explanation |
|  | Generated By Note | Vermelding van de generatie | This document has been generated by Mercans Payroll System (same as in standard payslip) | System note in the footer of the document. |
|  | Document Reference and Income Year | Documentreferentie en inkomstenjaar | CONCAT('BE-PSL-001 v1.0';' - ';$period.income_year) | Reference code of the payslip specification and the income year to which the document relates. Rendered on the same footer line as the copyright note. |
|  | Copyright Note | Vermelding auteursrechten | All rights reserved (same as in standard payslip) | Closing rights notice of the document. |

## Sheet: `Field Option`

| Field Name | Option Value | Option Description | Usage Context |
| --- | --- | --- | --- |
| CURRENCY | EUR | Euro | Displayed sample currency in payslip summary and banking currency fields |

## Sheet: `Population Range`

| Worker Situation | Include? (YES/NO) | Notes |
| --- | --- | --- |
| Active employees - white-collar (bediende), full-time | YES | Standard population. Gross to net on the 13.07% employee contribution and the annualised Annex III nr. 31 withholding. |
| Active employees - white-collar, part-time | YES | Same layout with the actual hours and the performance fraction. The social work bonus is computed on the full-time equivalent reference wage and then prorated by that fraction. |
| Active employees - blue-collar (arbeider) | YES | Contribution base is the gross x 108%, which raises the employee's own 13.07% as well. Holiday pay comes from the holiday fund, not from the employer, so no double holiday pay line appears in May. |
| New hires during the period | YES | Pay period, hire date and days worked reflect the actual start date. Proration follows the method declared under WTC flag BE-055; the market standard is the working-day method. |
| Terminations during the period | YES | Final settlement with the notice indemnity, the pro rata end-of-year premium and departure holiday pay at 15.34%. The holiday certificate is issued for the following employer. |
| Sickness within the guaranteed salary period | YES | Employer pays the guaranteed salary - 30 calendar days for white-collar staff. Days are equivalent days for holiday accrual. |
| Sickness beyond the guaranteed salary period | YES | Salary is suppressed and the health insurance fund takes over at 60% of the capped gross. The payslip still issues where any remuneration or deduction arises. |
| Maternity, birth, parental and thematic leave | YES | Income replacement is paid by a public authority; the payslip carries any employer supplement and the correct DmfA absence code. |
| Unpaid leave and time credit | YES | Salary is suppressed for the day with the applicable absence code. Ordinary unpaid leave is not an equivalent day and reduces the following year's holiday entitlement. |
| Employees under a wage garnishment or assignment | YES | The attachment is shown with the amount withheld, computed on the Article 1409 protected bands. Maintenance debts are attachable without limit. |
| Students within the 650-hour quota | YES | Solidarity contribution of 2.71% employee and 5.42% employer replaces the ordinary contributions; no wage withholding tax within the quota. |
| Flexi-job workers | YES | Flexi-salary is exempt from the employee contribution and from withholding; the employer pays a special contribution of 28%. |
| Inbound taxpayers and inbound researchers | YES | Up to 35% of the remuneration may be reimbursed as exempt employer own costs; the exempt part is shown separately and is outside the taxable base. |
| Posted workers covered by an A1 certificate of another member state | CONDITIONAL | Include only where Belgian payroll produces the payment. Social security remains in the sending state under Regulation (EC) 883/2004, while Belgian wage withholding tax may still be due. |
| Company directors (bedrijfsleiders) not under an employment contract | CONDITIONAL | Include only where the mandate is processed through payroll as an employee. Self-employed directors fall under the social insurance fund regime and are out of scope. |
| Self-employed contractors | NO | Not employees. No payslip, no DmfA line and no wage withholding tax; remuneration is invoiced and reported outside payroll. |

## Sheet: `Unit Rate Details`

|  | BELGIUM - UNIT RATE DETAILS - earning codes from BE-WTC-001 v1.0 (global Mercans pay element codes) |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Earning Description | Earning Code | Rate Account | Unit Account | Notes |
|  | Basic salary - monthly (white-collar) | 62100 |  | 63100 | Monthly salary prorated by the working-day method: monthly salary x working days covered / total working days in the month. Unit = days. |
|  | Arrears - basic salary (previous calendar year) | 62101 |  | 63101 | Arrears of a previous year are taxed at the exceptional-remuneration percentage keyed on the monthly gross x 13.92. Unit = days. |
|  | Adjustment - basic salary (current calendar year) | 62102 |  | 63102 | Added to the current period's ordinary remuneration and taxed once at the Annex III scale. Unit = days. |
|  | Advance on basic salary (blue-collar mid-month payment) | 62103 |  | 63103 | Mid-month advance to a blue-collar worker; recovered at the definitive pay. Unit = days. |
|  | Historic pay - year-to-date take-on from the previous provider | 62108 |  | 63108 | Take-on of year-to-date balances at a mid-year go-live. Unit = periods taken on. |
|  | Unpaid leave of absence - basic salary line | 62109 |  | 63109 | Carrier for the salary attributable to unpaid days before the reduction is applied. Unit = days. |
|  | Overtime - base pay for the overtime hour (100%) | 62110 |  | 63110 | Ordinary hourly pay for the overtime hour. Hourly rate = monthly salary x 3 / 13 / weekly hours. Unit = hours. |
|  | Overtime supplement 50% - weekday and Saturday | 62111 |  | 63111 | Statutory 50% supplement. Qualifies for the 66.81% employee withholding reduction within the 180-hour ceiling. Unit = hours. |
|  | Overtime supplement 100% - Sunday and public holiday | 62112 |  | 63112 | Statutory 100% supplement on Sundays and public holidays. Unit = hours. |
|  | Overtime supplement 20% (sectoral) | 62113 |  | 63113 | Sectoral 20% supplement; the reduced 57.75% employee withholding reduction applies. Unit = hours. |
|  | Voluntary overtime - first 240 net hours (from 1 April 2026) | 62114 |  | 63114 | Net overtime tranche: exempt from the supplement and from withholding within the quota. Unit = hours. |
|  | Voluntary overtime - 120 hours with supplement, favourable regime | 62115 |  | 63115 | Voluntary overtime carrying the supplement under the favourable regime. Unit = hours. |
|  | Voluntary overtime - base pay for the hour | 62116 |  | 63116 | Ordinary hourly pay for a voluntary overtime hour. Unit = hours. |
|  | Overtime - hotel and catering, employer without registered cash register | 62119 |  | 63119 | Sectoral horeca overtime quota. Unit = hours. |
|  | Overtime - hotel and catering, employer with registered cash register | 62120 |  | 63120 | Higher horeca quota where a registered cash register is in use. Unit = hours. |
|  | Overtime - construction with electronic attendance registration | 62121 |  | 63121 | Sectoral construction quota conditional on electronic attendance registration. Unit = hours. |
|  | Overtime - extraordinary increase of work | 62122 |  | 63122 | Overtime authorised for an extraordinary increase of work. Unit = hours. |
|  | Overtime - unforeseen necessity | 62123 |  | 63123 | Overtime authorised for an unforeseen necessity. Unit = hours. |
|  | Overtime above the 180-hour relief ceiling - taxed normally | 62124 |  | 63124 | Hours beyond the 180-hour relief ceiling; no withholding reduction. Unit = hours. |
|  | Night work supplement | 62125 |  | 63125 | Sectoral night premium, generally an hourly amount. Unit = hours. |
|  | Sunday work supplement | 62126 |  | 63126 | Sectoral Sunday premium. Unit = hours. |
|  | Public holiday work supplement | 62127 |  | 63127 | Sectoral premium for work performed on a public holiday. Unit = hours. |
|  | Saturday work supplement | 62128 |  | 63128 | Sectoral Saturday premium. Unit = hours. |
|  | Shift work supplement - two-shift system | 62129 |  | 63129 | Sectoral shift premium, generally a percentage of the hourly rate. Unit = hours. |
|  | Shift work supplement - three-shift or continuous system | 62130 |  | 63130 | Higher sectoral shift premium for three-shift or continuous systems. Unit = hours. |
|  | Double holiday pay - white-collar (92%) | 62160 |  | 63160 | 92% of the monthly gross for a full service year, paid in May and taxed on its own withholding table. Unit = months of service accrued. |
|  | Single holiday pay - white-collar (salary continued during leave) | 62300 |  | 63300 | Salary continued during the leave day; no separate cash line for a monthly-paid employee. Unit = days. |
|  | Commuting allowance - public transport | 62520 |  | 63520 | Employer intervention in the season ticket. Exempt within the statutory limits. Unit = months. |
|  | Bicycle allowance (CBA no. 164) | 62530 |  | 63530 | Per-kilometre allowance; requalified above EUR 0.37 per kilometre. Unit = kilometres. |
|  | Homeworking (office) allowance | 62630 |  | 63630 | Lump-sum office allowance; requalified above EUR 160.99 per month. Unit = months. |
|  | Meal vouchers - face value | 62660 |  | 63660 | One voucher per day actually worked. Employer share maximum EUR 8.91, employee share minimum EUR 1.09. Unit = vouchers. |
|  | Eco vouchers | 62870 |  | 63870 | Annual sectoral entitlement issued once a year; exempt within the sectoral ceiling. Unit = vouchers. |
|  | End-of-year premium (thirteenth month) | 62901 |  | 63901 | Sectoral end-of-year premium taxed at the exceptional-remuneration percentage. Unit = months of service accrued. |
|  | Public holiday pay | 62964 |  | 63964 | Value of the paid public holiday for a monthly-paid employee, at the daily value of the monthly salary. Unit = days. |
|  |  |  |  |  |  |
|  | Rate Account is left empty in line with REFERENCE_Payslip_Tunisia.xlsx, where the rate carrier is not accounted separately; the rate basis for each code is stated in the Notes column. Unit Account follows the Mercans convention of the 62xxx earning code re-prefixed to 63xxx. |  |  |  |  |
