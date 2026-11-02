# Colombia Payslip - CO_Compliance_Payslip_Generator v1.3 (8-sheet Mercans PSL contract)

Colombia payslip mandatory content and the full line list: the setup sheet, the Compliance Payslip definition, both rendered language variants - Colombia (EN) and Colombia (ES) with the Spanish labels - the Payslip Spec, Field Option, Population Range and Unit Rate Details.


## Provenance

| Source artifact | Bytes | MD5 |
|---|---|---|
| `CO_Compliance_Payslip_Generator.xlsx` | 461,652 | `619c1410c70775c0aa8b09cc0555f99d` |

This file is a complete, verbatim conversion of the artifacts above (python-docx / openpyxl, cached cell values; empty columns dropped; the first column `Row` of each table is the Excel row number, so a citation such as "WTC row 156, column Q" can be checked against the workbook). Figures, dates, codes, Spanish terminology and legal citations are reproduced exactly as delivered; nothing is summarised or rounded. The only change: the name of the client whose wage-type labels appear in a few rows is replaced by `[client]`.


## Reading notes (added at compilation, 2026-11-02)

- **Version:** Payslip Generator **v1.3**, issued 2026-11-02. Rendered variants `Colombia (EN)` and `Colombia (ES)`.
- Colombia has **no Labour Code article prescribing payslip content**. The binding content rules are those of the electronic
  payroll support document: Res. DIAN 000227 de 2025 art. 1.5.3.3.1 (content), art. 1.5.3.8.3 (optional graphical
  representation with the QR code on every page) and art. 1.5.3.8.5 (Spanish and COP mandatory; another language or currency
  may be added, never substituted). Res. DIAN 000013 de 2021 is compiled in Res. 000227 de 2025.
- Amounts in the example columns are cached values of the workbook formulas (e.g. net pay 15,478,848; worked example August
  2026, same pay since January, withholding 1,993,152 with the 790 / 1,340 UVT caps tracked year-to-date).


## Navigation index

Read with `offset` / `limit` rather than opening the whole file.

| Line | Section |
|---|---|
| 44 | Sheet: How to set up Payslip |
| 87 | Sheet: Compliance Payslip |
| 124 | Sheet: Colombia (EN) |
| 204 | Sheet: Colombia (ES) |
| 284 | Sheet: Payslip Spec |
| 365 | Sheet: Field Option |
| 373 | Sheet: Population Range |
| 392 | Sheet: Unit Rate Details |

---


## Sheet: How to set up Payslip

Create new sheet for your country, copy the payslip from "Compliance Payslip" sheet and then make changes  
Example Payslip  
When creating report make sure to use the Normal margins <br> Page Layout -> Margins -> Normal this will show if the content will fit on your page or not  
Net Pay:  

| Row | This section contains employer-related information. To add an extra row, simply select Row 10, right-click, and choose ‘Insert Row’ from the menu. | Employer <br> Details | Employer Name |  | Mercans Estonia |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 8 |  |  | Employer Address |  | Väike-Tähe 20, Tartu, Tartumaa, 51010 |  |  |  | EUR |  | 1,350.00 |  | 1. Finalize Your Worksheet: |
| 9 |  |  | Country |  | Estonia |  |  |  |  |  |  |  | • Ensure all desired changes are made to your worksheet. |
| 10 |  |  | Period |  | 01/10/2023 - 31/10/2023 |  |  |  |  |  |  |  | 2. Access the ‘Save As’ Function: |
| 11 |  |  |  |  |  |  |  |  |  |  |  |  | • Click on the File tab in the top-left corner. |
| 12 | This section contains employee-related information. If a field is not applicable, you can either remove it or replace it with one relevant to the country. Additionally, you have the option to delete or add extra rows as needed. | Employee <br> Details | Employee name |  | John Doe |  | Email |  | jdoe@mercan.com |  |  |  | • Select Save As from the menu. |
| 13 |  |  | Employee ID |  | EID-1337 |  | Hire date |  | 01/10/2019 |  |  |  | 3. Choose PDF as the File Format: |
| 14 |  |  | Employee Position |  | Operational Support |  | Payment Method |  | Bank |  |  |  | • In the ‘Save As’ dialog box, click the dropdown menu labeled File format. |
| 15 |  |  |  |  |  |  |  |  |  |  |  |  | • Select PDF (*.pdf) from the list of file formats. |
| 16 | This section is for countries that require additional details on the payslip. If not needed, you can simply delete it.” | Extra Information | Basic Salary (EUR) |  | 2,000.00 |  | Custom Field |  | XXXXX |  |  |  | 4. Specify the Content to Export: |
| 17 |  |  | Daily (EUR) |  | 100.00 |  | Custom Field |  | XXXXX |  |  |  | • Click on the Sheet option |
| 18 |  |  | Hourly (EUR) |  | 12.50 |  | Custom Field |  | XXXXX |  |  |  | • Ensure the Option is set to Best for Printing |
| 19 |  |  |  |  |  |  |  |  |  |  |  |  | 5. Save the PDF: |
| 20 | Here, you can add or remove wage types by inserting or deleting rows. If the provided columns are not applicable to the country, rename or merge them with other fields. <br> Don't delete the columns otherwise it messes up the design. | Details | Details |  |  |  |  |  |  |  |  |  | • Choose your desired file location and name. |
| 21 |  |  | Earnings |  |  |  | Unit | Amount |  |  | Year-to-date |  | • Click Save to generate the PDF. |
| 22 |  |  | XXXXX - Earning Pay Element |  |  |  |  | 2,000.00 |  |  | 20,000.00 |  |  |
| 23 |  |  | XXXXX - Earning Pay Element |  |  |  | 5 (Hrs) | 200.00 |  |  | 2,000.00 |  |  |
| 24 |  |  | XXXXX - Earning Pay Element |  |  |  |  | 10.00 |  |  | 100.00 |  |  |
| 26 |  |  | Total Gross |  |  |  |  | 2,250.00 |  |  | EUR |  |  |
| 28 | Here, you can add or remove wage types by inserting or deleting rows. If the provided columns are not applicable to the country, rename or merge them with other fields. <br> Don't delete the columns otherwise it messes up the design. | Details | Deductions |  |  |  | Unit | Amount |  |  | Year-to-date |  |  |
| 29 |  |  | XXXXX - Deduction Pay Element |  |  |  |  | 800.00 |  |  | 8,000.00 |  |  |
| 30 |  |  | XXXXX - Deduction Pay Element |  |  |  |  | 100.00 |  |  | 1,000.00 |  |  |
| 31 |  |  | Total Deductions |  |  |  |  | 900.00 |  |  | EUR |  |  |
| 33 |  |  |  |  |  |  |  | Net Pay: |  |  | 1,350.00 |  |  |
| 35 | Here, you can add Bank info by inserting row if there is also Secoundary bank account. If the provided columns are not applicable to the country, rename or merge them with other fields. <br> Don't delete the columns otherwise it messes up the design. | Details | Employer Contributions |  |  |  |  | Amount |  |  | Year-to-date |  |  |
| 36 |  |  | XXXXX - Employer Contribution Pay Element |  |  |  |  | 400.00 |  |  | 4,000.00 |  |  |
| 37 |  |  | Total Employer Contributions |  |  |  |  | 400.00 |  |  | EUR |  |  |
| 39 | Here, you can add Bank info by inserting row if there is also Secoundary bank account. If the provided columns are not applicable to the country, rename or merge them with other fields. <br> Don't delete the columns otherwise it messes up the design. | Bank Info | Banking details |  |  |  |  |  |  |  |  |  |  |
| 40 |  |  | Bank name | SWIFT |  | Beneficiary name |  | Acc. Number |  | Account currency |  | Type |  |
| 41 |  |  | Swed Bank AS | SW121212 |  | Jhon Doe |  | EE121212121212 |  | EUR |  | Primary |  |
| 43 | This is a filler section designed to ensure the template fills the entire page and the footer remains in the correct position. If you add or delete rows in other sections, make sure to adjust this filler section by adding or removing the same number of rows. For example, if you add two rows in the ‘Earnings’ section, you should delete two rows from the ‘Filler’ section. | Filler |  |  |  |  |  |  |  |  |  |  |  |
| 59 |  |  | This document has been generated by Mercans |  |  |  |  |  |  |  |  |  |  |
| 60 |  |  | REF-P26-663 |  |  | © All rights reserved |  |  |  |  |  |  |  |


## Sheet: Compliance Payslip

Example Payslip  
Net Pay:  

| Row | Employer Name |  | Mercans Estonia |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
| 8 | Employer Address |  | Väike-Tähe 20, Tartu, Tartumaa, 51010 |  |  |  | MZN |  | 2520 |  |
| 9 | Country |  | MZN |  |  |  |  |  |  |  |
| 10 | Period |  | 01/10/2023 - 31/10/2023 |  |  |  |  |  |  |  |
| 12 | Employee name |  | John Doe |  | Email |  | jdoe@mercan.com |  |  |  |
| 13 | Employee ID |  | EID-1337 |  | Hire date |  | 01/10/2019 |  |  |  |
| 14 | Employee Position |  | Operational Support |  | Payment Method |  | Bank |  |  |  |
| 16 | Basic Salary (EUR) |  | 2000 |  | Custom Field |  | XXXXX |  |  |  |
| 17 | Daily (EUR) |  | 100 |  | Custom Field |  | XXXXX |  |  |  |
| 18 | Hourly (EUR) |  | 12.5 |  | Custom Field |  | XXXXX |  |  |  |
| 20 | Details |  |  |  |  |  |  |  |  |  |
| 21 | Earnings |  |  |  |  |  | Rate | Unit | Amount |  |
| 22 | XXXXX - Earning Pay Element |  |  |  |  |  |  |  | 3210 |  |
| 23 | XXXXX - Earning Pay Element |  |  |  |  |  |  |  | 200 |  |
| 24 | XXXXX - Earning Pay Element |  |  |  |  |  |  |  | 10 |  |
| 25 | Total Gross |  |  |  |  |  |  |  | 3 420.00 MZN |  |
| 27 | Deductions |  |  |  |  |  | Rate | Unit | Amount |  |
| 28 | XXXXX - Deduction Pay Element |  |  |  |  |  |  |  | 800 |  |
| 29 | XXXXX - Deduction Pay Element |  |  |  |  |  |  |  | 100 |  |
| 30 | Total Deductions |  |  |  |  |  |  |  | 900.00 MZN |  |
| 32 |  |  |  |  |  | Net Pay: |  |  | 2 520.00 MZN |  |
| 34 | Employer Contributions |  |  |  |  |  |  |  | Amount |  |
| 35 | XXXXX - Employer Contribution Pay Element |  |  |  |  |  |  |  | 400 |  |
| 36 | Total Employer Contributions |  |  |  |  |  |  |  | 400.00 MZN |  |
| 38 | Banking details |  |  |  |  |  |  |  |  |  |
| 39 | Bank name | SWIFT |  | Beneficiary name |  | Acc. Number |  | Account currency |  | Type |
| 40 | Swed Bank AS | SW121212 |  | Jhon Doe |  | EE121212121212 |  | EUR |  | Primary |
| 57 | This document has been generated by Mercans |  |  |  |  |  |  |  |  |  |
| 58 | REF-P26-663 |  |  | © All rights reserved |  |  |  |  |  |  |


## Sheet: Colombia (EN)

Colombia Payslip (Desprendible de Pago) - Documento Soporte de Pago de Nomina Electronica  
Net Pay:  

| Row | Employer Name | Mercans Colombia S.A.S. |  |  |  | COP |  |  |
|---|---|---|---|---|---|---|---|---|
| 8 | Employer Address | Calle 100 No. 7-33, Bogota D.C., Colombia |  |  |  | COP |  | 15478848 |
| 9 | NIT (Employer Tax ID) | 900.123.456-7 |  |  |  |  |  |  |
| 10 | ARL Risk Class | Class I (0.522%) |  |  |  |  |  |  |
| 11 | CUNE | a1b2c3d4e5f6789... |  |  |  | Prefix / Consecutive |  | NE-000123 |
| 12 | Generation Date and Time | 2026-08-31 10:30:00 |  |  |  | Payment Date |  | 2026-09-05 |
| 13 | QR Code Reference | https://catalogo-vpfe.dian.gov.co/document/searchqr?documentkey=CUNE (Illustrative: replace CUNE with the document's CUNE value; QR image min. 2 cm, on every page) |  |  |  | Technology Provider NIT / Software ID |  | Illustrative: provider NIT / DIAN-registered Software ID |
| 14 | Payment Method | Bank transfer (Transferencia bancaria) |  |  |  | Pay Period |  | 2026-08-01 - 2026-08-31 |
| 15 | Digital Signature | Digital signature of the issuer, applied to the XML |  |  |  |  |  |  |
| 17 | Employee Name | Juan Perez |  | Employee Department |  | IT |  |  |
| 18 | Employee Code |  |  |  |  |  |  |  |
| 19 | Completed Years in Service |  |  |  |  |  |  |  |
| 20 | Tax Month |  |  |  |  |  |  |  |
| 21 | Days in Month |  |  |  |  | Document ID (Documento de Identidad): C.C. 79.123.456 |  |  |
| 22 | EPS (Health) / AFP (Pension) |  |  |  |  | Contract Type (Tipo de Contrato): Indefinite Term |  |  |
| 24 | Salary Detail (Devengados) |  |  |  |  |  |  |  |
| 25 | Payment Item |  |  |  | Rate | Unit | Amount |  |
| 26 | CO-SALARIO-BASICO - Basic Salary (Salario Basico) |  |  |  |  |  | 18000000 |  |
| 27 | CO-HED / CO-HEN / CO-HEDDF / CO-HENDF - Overtime (Horas Extra) -- excluded from vacation base |  |  |  |  |  | 250000 |  |
| 28 | CO-RECARGO-NOCTURNO - Night Premium 19:00-06:00 (Recargo Nocturno) -- included in vacation base |  |  |  |  |  | 250000 |  |
| 29 | CO-COMISIONES - Commissions & Bonuses (Comisiones y Bonificaciones) |  |  |  |  |  | 700000 |  |
| 30 | CO-AUX-TRANSPORTE - Transport Allowance (Auxilio de Transporte - only up to 2 SMMLV) |  |  |  |  |  | 0 |  |
| 31 | Total Earnings (Total Devengado) |  |  |  |  |  | 19,200,000 COP |  |
| 33 | Deduction Item (Deducciones) |  |  |  | Rate | Unit | Amount |  |
| 34 | CO-DED-SALUD - Health Contribution - Employee (Salud - Empleado) |  |  |  |  |  | 768000 |  |
| 35 | CO-DED-PENSION - Pension Contribution - Employee (Pension - Empleado) |  |  |  |  |  | 768000 |  |
| 36 | CO-DED-FSP-SOLIDARIDAD - Solidarity Pension Fund FSP (Fondo de Solidaridad Pensional) |  |  |  |  |  | 192000 |  |
| 37 | CO-RETENCION-FUENTE - Income Tax Withholding (Retencion en la Fuente) |  |  |  |  |  | 1993152 |  |
| 38 | Total Deductions (Total Deducciones) |  |  |  |  |  | 3,721,152.00 COP |  |
| 40 | Net Pay (Neto a Pagar): |  |  |  |  |  | 15,478,848.00 COP |  |
| 42 | Employer Contributions (Aportes del Empleador) |  |  |  |  |  |  |  |
| 43 | Contribution Item |  |  |  | Rate | Unit | Amount |  |
| 44 | CO-ER-SALUD - Health Contribution - Employer (Salud - Empleador) |  |  |  | 8.5% |  | 1632000 |  |
| 45 | CO-ER-PENSION - Pension Contribution - Employer (Pension - Empleador) |  |  |  | 12% |  | 2304000 |  |
| 46 | CO-ER-ARL - Occupational Risk (Riesgos Laborales - ARL, Class I) |  |  |  |  |  | 100300 |  |
| 47 | CO-ER-CCF - Family Compensation Fund (Caja de Compensacion Familiar) |  |  |  |  |  | 768000 |  |
| 48 | CO-ER-SENA - SENA Training Levy (Aporte SENA) |  |  |  | 2% |  | 384000 |  |
| 49 | CO-ER-ICBF - ICBF Family Welfare (Aporte ICBF) |  |  |  | 3% |  | 576000 |  |
| 50 | Total Employer Contributions (Total Aportes Empleador) |  |  |  |  |  | 5,764,300 COP |  |
| 52 | Social Benefit Provisions (Prestaciones Sociales - Provisiones) |  |  |  |  |  |  |  |
| 53 | Contribution Item |  |  |  | Rate | Unit | Amount |  |
| 54 | CO-PROV-CESANTIAS - Severance (Cesantias) |  |  |  |  |  | 1600000 |  |
| 55 | CO-PROV-INTERESES-CESANTIAS - Interest on Severance (Intereses a las Cesantias) |  |  |  |  |  | 192000 |  |
| 56 | CO-PROV-PRIMA - Service Bonus (Prima de Servicios) |  |  |  | 8.3333% |  | 1600000 |  |
| 57 | CO-PROV-VACACIONES - Paid Leave Accrual (Provision de Vacaciones) |  |  |  | 4.1667% |  | 789583 |  |
| 58 | Total Provisions (Total Provisiones) |  |  |  |  |  | 4,181,583 COP |  |
| 60 | Banking Details |  |  |  |  |  |  |  |
| 61 | Beneficiary Name |  |  |  | Bank |  | Currency |  |
| 62 | Juan Perez |  |  |  | Bancolombia S.A. |  | COP |  |
| 64 | Contribution & Provision Summary (Resumen de Aportes) |  |  |  |  |  |  |  |
| 65 | Contribution Base / IBC (Base de Cotizacion) |  |  |  |  |  | 19200000 |  |
| 66 | Total Employee Contributions (Salud + Pension + FSP) |  |  |  |  |  | 1728000 |  |
| 67 | Total Employer Contributions & Parafiscales |  |  |  |  |  | 5764300 |  |
| 68 | Total Social Benefit Provisions (Prestaciones) |  |  |  |  |  | 4181583 |  |
| 69 | Total Employer Cost (Contributions + Provisions) |  |  |  |  |  | 9945883 |  |
| 71 | Year-to-Date (Acumulados del Ano) |  |  |  |  |  |  |  |
| 72 | YTD Gross Earnings |  |  |  |  |  |  |  |
| 73 | YTD Employee Contributions |  |  |  |  |  |  |  |
| 74 | YTD Income Tax Withheld |  |  |  |  |  |  |  |
| 75 | YTD Net Pay |  |  |  |  |  |  |  |
| 77 | Statutory Notes - Fiscal Year 2026 |  |  |  |  |  |  |  |
| 78 | * Payslip disclosure: the Codigo Sustantivo del Trabajo (CST) has no payslip-content article. Where a graphical representation of the payroll document is issued it must carry the content of the electronic payroll support document: devengados, deducciones and neto, itemised by concept, for the period (Resolucion DIAN 000227 de 2025, arts. 1.5.3.3.1 and 1.5.3.8.3). Separately, Ley 1393 de 2010, Art. 32 requires the employer to inform the employee of the social-security contributions paid or to ensure that the employee can check that they were paid; itemising them on the payslip is one way to meet it. DIAN Nomina Electronica (Resolucion 000227 de 2025, arts. 1.5.3.2.2, 1.5.3.3.1 and 1.5.3.4.1.1, which compiles Resolucion 000013 de 2021) requires a structured monthly payroll support document, transmitted within the first 10 days of the following month. |  |  |  |  |  |  |  |
| 79 | * Social Security (Ley 100 de 1993): Health/Salud 12.5% (employee 4% + employer 8.5%); Pension 16% (employee 4% + employer 12%). Contribution base (IBC) floor 1 SMMLV, ceiling 25 SMMLV (2026 = COP 43,772,625). FSP (Ley 100 arts. 20 and 27, as amended by Ley 797 de 2003 arts. 7 and 8): employee-only surcharge 1% for IBC >= 4 SMMLV, rising 1.2%-2.0% above 16 SMMLV. Auxilio de transporte is excluded from the IBC. |  |  |  |  |  |  |  |
| 80 | * Occupational Risk / ARL (Decreto 1072 de 2015, Art. 2.2.4.3.5 - minimum and maximum contribution table by class): employer-only, five risk classes by CIIU activity code; the initial rate of each class varies between the minimum and the maximum of that class (the example uses class I at 0.522%; class I minimum 0.348%). Nothing is deducted from the employee. |  |  |  |  |  |  |  |
| 81 | * Parafiscales (employer): SENA 2%, ICBF 3%, Caja de Compensacion Familiar 4%. Exoneration under Art. 114-1 Estatuto Tributario (added by Ley 1819 de 2016 art. 65): companies and legal persons filing income tax are exonerated from SENA, ICBF and the 8.5% employer health contribution for each employee earning under 10 SMMLV; natural-person employers are exonerated only if they employ two or more workers; the 4% Caja de Compensacion, pension and ARL are never exonerated. |  |  |  |  |  |  |  |
| 82 | * Income Tax Withholding / Retencion en la fuente (Arts. 383, 388, 206 & 336 Estatuto Tributario; UVT 2026 = COP 52,374 per DIAN Resolucion 000238 de 2025): progressive marginal table 0/19/28/33/35/37/39%, starting above 95 UVT (approx. COP 4,975,530/month). Depuration allows 25% exempt income capped at 790 UVT/year (Art. 206 num. 10, mod. Ley 2277 de 2022) subject to a 40% global cap of deductions/exemptions, max 1,340 UVT/year (DUR 1625 de 2016 art. 1.2.4.1.6 par. 3; Art. 336). The 790-UVT and 1,340-UVT limits are annual and tracked year-to-date per employee, with no monthly one-twelfth limit (Consejo de Estado, Seccion Cuarta, rad. 24047 of 2021); the example assumes the same monthly pay since January 2026. |  |  |  |  |  |  |  |
| 83 | * Minimum wage SMMLV 2026 = COP 1,750,905/month (Decreto 1469 de 2025; provisional suspension of 12-Feb-2026 revoked by the Consejo de Estado, Seccion Segunda, auto of 9-Jul-2026, rad. 11001-03-25-000-2026-00004-00; annulment case pending). Auxilio de transporte 2026 = COP 249,095/month (Decreto 1470 de 2025), payable to workers earning up to 2 SMMLV (Ley 15 de 1959); excluded from the IBC but included in the base for prima and cesantias. |  |  |  |  |  |  |  |
| 84 | * Leave: annual leave 15 working days/year (CST Art. 186); sick leave (enfermedad general) - employer pays days 1-2, EPS pays from day 3 at 66.67% for the first 90 days then 50% for days 91-180 (Decreto 780 de 2016 Art. 3.2.1.10; CST Art. 227); maternity 18 weeks funded by EPS (CST Art. 236, Ley 1822 de 2017); paternity 2 weeks (CST Art. 236 par. 2, as amended by Ley 2114 de 2021 art. 2). |  |  |  |  |  |  |  |
| 85 | * Prestaciones sociales (employer): prima de servicios one month's salary/year (CST Art. 306, paid half by 30 Jun and half by 20 Dec); cesantias one month's salary/year (CST Art. 249) deposited to the fund before 15 Feb of the following year (Ley 50 de 1990 Art. 99 num. 3); intereses a las cesantias 12%/year paid to the employee by 31 Jan (Ley 52 de 1975). Monthly accrual of the interest in the example = 12% x the month's cesantias (1,600,000 x 12% = 192,000, i.e. 1% of the annual cesantias balance of 19,200,000), Ley 52 de 1975 Art. 1. Identifiers: employer NIT within the RUT (DIAN, Art. 555-1 ET); employee documento de identidad - Cedula de Ciudadania (C.C.) or Cedula de Extranjeria (C.E.). Currency COP (ISO 4217). Sources: Estatuto Tributario \| CST \| Ley 100 de 1993 \| DIAN \| Ministerio del Trabajo \| Mercans CO-2026. |  |  |  |  |  |  |  |
| 87 | This document has been generated by Mercans |  |  |  |  |  |  |  |
| 88 | This document has been generated by Mercans |  | All rights reserved |  |  |  |  |  |
| 89 | REF-CO-2026 |  |  |  |  |  |  |  |


## Sheet: Colombia (ES)

Documento Soporte de Pago de Nomina Electronica - Colombia (Desprendible de Pago)  
Neto a Pagar:  

| Row | Nombre del Empleador | Mercans Colombia S.A.S. |  |  |  | COP |  |  |
|---|---|---|---|---|---|---|---|---|
| 8 | Direccion del Empleador | Calle 100 No. 7-33, Bogota D.C., Colombia |  |  |  | COP |  | 15478848 |
| 9 | NIT del Empleador | 900.123.456-7 |  |  |  |  |  |  |
| 10 | Clase de Riesgo ARL | Clase I (0,522%) |  |  |  |  |  |  |
| 11 | CUNE | a1b2c3d4e5f6789... |  |  |  | Prefijo / Consecutivo |  | NE-000123 |
| 12 | Fecha y Hora de Generacion | 2026-08-31 10:30:00 |  |  |  | Fecha de Pago |  | 2026-09-05 |
| 13 | Referencia Codigo QR | https://catalogo-vpfe.dian.gov.co/document/searchqr?documentkey=CUNE (Ilustrativo: reemplazar CUNE por el CUNE del documento; imagen QR minimo 2 cm, en todas las paginas) |  |  |  | NIT del Proveedor Tecnologico / ID del Software |  | Ilustrativo: NIT del proveedor / ID del software registrado en la DIAN |
| 14 | Medio de Pago | Transferencia bancaria |  |  |  | Periodo Liquidado |  | 2026-08-01 - 2026-08-31 |
| 15 | Firma Digital | Firma digital del emisor, aplicada al XML |  |  |  |  |  |  |
| 17 | Nombre del Trabajador | Juan Perez |  | Departamento / Area |  | TI |  |  |
| 18 | Codigo del Empleado |  |  |  |  |  |  |  |
| 19 | Anos Completos de Servicio |  |  |  |  |  |  |  |
| 20 | Mes de Liquidacion |  |  |  |  |  |  |  |
| 21 | Dias del Periodo |  |  |  |  | Documento de Identidad: C.C. 79.123.456 |  |  |
| 22 | EPS (Salud) / AFP (Pension) |  |  |  |  | Tipo de Contrato: Termino Indefinido |  |  |
| 24 | Detalle Salarial (Devengados) |  |  |  |  |  |  |  |
| 25 | Concepto |  |  |  | Tarifa | Unidad | Valor |  |
| 26 | CO-SALARIO-BASICO - Salario Basico |  |  |  |  |  | 18000000 |  |
| 27 | CO-HED / CO-HEN / CO-HEDDF / CO-HENDF - Horas Extra -- excluida de la base de vacaciones |  |  |  |  |  | 250000 |  |
| 28 | CO-RECARGO-NOCTURNO - Recargo Nocturno 19:00-06:00 -- incluido en la base de vacaciones |  |  |  |  |  | 250000 |  |
| 29 | CO-COMISIONES - Comisiones y Bonificaciones |  |  |  |  |  | 700000 |  |
| 30 | CO-AUX-TRANSPORTE - Auxilio de Transporte (solo hasta 2 SMMLV) |  |  |  |  |  | 0 |  |
| 31 | Total Devengado |  |  |  |  |  | 19,200,000 COP |  |
| 33 | Deducciones |  |  |  | Tarifa | Unidad | Valor |  |
| 34 | CO-DED-SALUD - Aporte a Salud - Empleado |  |  |  |  |  | 768000 |  |
| 35 | CO-DED-PENSION - Aporte a Pension - Empleado |  |  |  |  |  | 768000 |  |
| 36 | CO-DED-FSP-SOLIDARIDAD - Fondo de Solidaridad Pensional (FSP) |  |  |  |  |  | 192000 |  |
| 37 | CO-RETENCION-FUENTE - Retencion en la Fuente |  |  |  |  |  | 1993152 |  |
| 38 | Total Deducciones |  |  |  |  |  | 3,721,152.00 COP |  |
| 40 | Neto a Pagar: |  |  |  |  |  | 15,478,848.00 COP |  |
| 42 | Aportes del Empleador |  |  |  |  |  |  |  |
| 43 | Concepto |  |  |  | Tarifa | Unidad | Valor |  |
| 44 | CO-ER-SALUD - Aporte a Salud - Empleador |  |  |  | 8.5% |  | 1632000 |  |
| 45 | CO-ER-PENSION - Aporte a Pension - Empleador |  |  |  | 12% |  | 2304000 |  |
| 46 | CO-ER-ARL - Riesgos Laborales (ARL, Clase I) |  |  |  |  |  | 100300 |  |
| 47 | CO-ER-CCF - Caja de Compensacion Familiar |  |  |  |  |  | 768000 |  |
| 48 | CO-ER-SENA - Aporte SENA |  |  |  | 2% |  | 384000 |  |
| 49 | CO-ER-ICBF - Aporte ICBF |  |  |  | 3% |  | 576000 |  |
| 50 | Total Aportes del Empleador |  |  |  |  |  | 5,764,300 COP |  |
| 52 | Prestaciones Sociales (Provisiones) |  |  |  |  |  |  |  |
| 53 | Concepto |  |  |  | Tarifa | Unidad | Valor |  |
| 54 | CO-PROV-CESANTIAS - Cesantias |  |  |  |  |  | 1600000 |  |
| 55 | CO-PROV-INTERESES-CESANTIAS - Intereses a las Cesantias |  |  |  |  |  | 192000 |  |
| 56 | CO-PROV-PRIMA - Prima de Servicios |  |  |  | 8.3333% |  | 1600000 |  |
| 57 | CO-PROV-VACACIONES - Provision de Vacaciones |  |  |  | 4.1667% |  | 789583 |  |
| 58 | Total Provisiones |  |  |  |  |  | 4,181,583 COP |  |
| 60 | Datos Bancarios |  |  |  |  |  |  |  |
| 61 | Nombre del Titular |  |  |  | Banco |  | Moneda |  |
| 62 | Juan Perez |  |  |  | Bancolombia S.A. |  | COP |  |
| 64 | Resumen de Aportes y Provisiones |  |  |  |  |  |  |  |
| 65 | Base de Cotizacion (IBC) |  |  |  |  |  | 19200000 |  |
| 66 | Total Aportes del Trabajador (Salud + Pension + FSP) |  |  |  |  |  | 1728000 |  |
| 67 | Total Aportes del Empleador y Parafiscales |  |  |  |  |  | 5764300 |  |
| 68 | Total Provisiones (Prestaciones Sociales) |  |  |  |  |  | 4181583 |  |
| 69 | Costo Total del Empleador (Aportes + Provisiones) |  |  |  |  |  | 9945883 |  |
| 71 | Acumulados del Ano (YTD) |  |  |  |  |  |  |  |
| 72 | Acumulado Devengado |  |  |  |  |  |  |  |
| 73 | Acumulado Aportes Trabajador |  |  |  |  |  |  |  |
| 74 | Acumulado Retencion en la Fuente |  |  |  |  |  |  |  |
| 75 | Acumulado Neto Pagado |  |  |  |  |  |  |  |
| 77 | Notas Legales - Ejercicio Fiscal 2026 |  |  |  |  |  |  |  |
| 78 | * Divulgacion de nomina: el Codigo Sustantivo del Trabajo (CST) no contiene un articulo sobre el contenido del desprendible. Si se expide una representacion grafica del documento de nomina, debe llevar el contenido del documento soporte de pago de nomina electronica: devengados, deducciones y neto, detallados por concepto, del periodo (Resolucion DIAN 000227 de 2025, arts. 1.5.3.3.1 y 1.5.3.8.3). Ademas, la Ley 1393 de 2010, Art. 32 obliga al empleador a informar al trabajador los aportes pagados a la proteccion social o a garantizar que pueda consultar que fueron abonados; detallarlos en el desprendible es una forma de cumplirla. La Nomina Electronica de la DIAN (Resolucion 000227 de 2025, arts. 1.5.3.2.2, 1.5.3.3.1 y 1.5.3.4.1.1, que compila la Resolucion 000013 de 2021) exige un documento soporte de pago de nomina mensual y estructurado, transmitido dentro de los primeros 10 dias del mes siguiente. |  |  |  |  |  |  |  |
| 79 | * Seguridad Social (Ley 100 de 1993): Salud 12,5% (trabajador 4% + empleador 8,5%); Pension 16% (trabajador 4% + empleador 12%). Base de cotizacion (IBC) con piso de 1 SMMLV y tope de 25 SMMLV (2026 = COP 43.772.625). FSP (Arts. 20 y 27 Ley 100, mod. Arts. 7 y 8 Ley 797 de 2003): aporte adicional solo del trabajador, 1% para IBC >= 4 SMMLV, aumentando de 1,2% a 2,0% por encima de 16 SMMLV. El auxilio de transporte se excluye del IBC. |  |  |  |  |  |  |  |
| 80 | * Riesgos Laborales / ARL (Decreto 1072 de 2015, Art. 2.2.4.3.5 - tabla de cotizaciones minimas y maximas por clase): a cargo exclusivo del empleador, cinco clases de riesgo segun el codigo CIIU de la actividad; la tasa inicial de cada clase varia entre el minimo y el maximo de esa clase (el ejemplo usa la clase I al 0,522%; minimo de la clase I 0,348%). No se deduce nada al trabajador. |  |  |  |  |  |  |  |
| 81 | * Parafiscales (empleador): SENA 2%, ICBF 3%, Caja de Compensacion Familiar 4%. Exoneracion del Art. 114-1 del Estatuto Tributario (adicionado por la Ley 1819 de 2016 art. 65): las sociedades y personas juridicas contribuyentes declarantes del impuesto de renta estan exoneradas de SENA, ICBF y del aporte patronal de salud del 8,5% por cada trabajador que devengue menos de 10 SMMLV; las personas naturales solo se exoneran si emplean dos o mas trabajadores; la Caja de Compensacion del 4%, la pension y la ARL nunca se exoneran. |  |  |  |  |  |  |  |
| 82 | * Retencion en la fuente (Arts. 383, 388, 206 y 336 del Estatuto Tributario; UVT 2026 = COP 52.374 segun Resolucion DIAN 000238 de 2025): tabla marginal progresiva 0/19/28/33/35/37/39%, que inicia por encima de 95 UVT (aprox. COP 4.975.530/mes). La depuracion permite una renta exenta del 25% limitada a 790 UVT/ano (Art. 206 num. 10, mod. Ley 2277 de 2022), sujeta al limite global del 40% de deducciones y rentas exentas, maximo 1.340 UVT/ano (DUR 1625 de 2016 art. 1.2.4.1.6 par. 3; Art. 336). Los limites de 790 UVT y 1.340 UVT son anuales y se controlan por el acumulado del ano de cada trabajador, sin tope mensual de una doceava parte (Consejo de Estado, Seccion Cuarta, rad. 24047 de 2021); el ejemplo supone el mismo pago mensual desde enero de 2026. |  |  |  |  |  |  |  |
| 83 | * Salario minimo SMMLV 2026 = COP 1.750.905/mes (Decreto 1469 de 2025; la suspension provisional del 12-feb-2026 fue revocada por el Consejo de Estado, Seccion Segunda, auto del 9-jul-2026, rad. 11001-03-25-000-2026-00004-00; el proceso de nulidad sigue en curso). Auxilio de transporte 2026 = COP 249.095/mes (Decreto 1470 de 2025), pagadero a quienes devenguen hasta 2 SMMLV (Ley 15 de 1959); se excluye del IBC pero se incluye en la base de prima y cesantias. |  |  |  |  |  |  |  |
| 84 | * Licencias: vacaciones 15 dias habiles/ano (CST Art. 186); incapacidad por enfermedad general - el empleador paga los dias 1-2 y la EPS desde el dia 3 al 66,67% durante los primeros 90 dias y al 50% entre los dias 91-180 (Decreto 780 de 2016 Art. 3.2.1.10; CST Art. 227); licencia de maternidad 18 semanas a cargo de la EPS (CST Art. 236, Ley 1822 de 2017); licencia de paternidad 2 semanas (CST Art. 236 par. 2, mod. Ley 2114 de 2021 art. 2). |  |  |  |  |  |  |  |
| 85 | * Prestaciones sociales (empleador): prima de servicios un salario mensual/ano (CST Art. 306, mitad antes del 30 jun y mitad antes del 20 dic); cesantias un salario mensual/ano (CST Art. 249) consignado al fondo antes del 15 feb del ano siguiente (Ley 50 de 1990 Art. 99 num. 3); intereses a las cesantias 12%/ano pagados al trabajador antes del 31 ene (Ley 52 de 1975). Provision mensual de los intereses en el ejemplo = 12% x las cesantias del mes (1.600.000 x 12% = 192.000, es decir 1% del saldo anual de cesantias de 19.200.000), Ley 52 de 1975 Art. 1. Identificadores: NIT del empleador dentro del RUT (DIAN, Art. 555-1 ET); documento de identidad del trabajador - Cedula de Ciudadania (C.C.) o Cedula de Extranjeria (C.E.). Moneda COP (ISO 4217). Fuentes: Estatuto Tributario \| CST \| Ley 100 de 1993 \| DIAN \| Ministerio del Trabajo \| Mercans CO-2026. |  |  |  |  |  |  |  |
| 87 | Este documento ha sido generado por Mercans |  |  |  |  |  |  |  |
| 88 | Este documento ha sido generado por Mercans |  | Todos los derechos reservados |  |  |  |  |  |
| 89 | REF-CO-2026 |  |  |  |  |  |  |  |


## Sheet: Payslip Spec

Header Details  

| Row | Field Name | Field Local Name | HRB Mapping | Field Explanation (RA) |  |
|---|---|---|---|---|---|
| 4 | Payslip Title | Titulo de la Nomina | Static text "Colombia Payslip (Desprendible de Pago) - Documento Soporte de Pago de Nomina Electronica" | Display title at top. Identifies Colombia and document type. |  |
| 5 | Company Logo | Logo de la Empresa | Static Mercans corporate logo | Mercans corporate logo in top banner. |  |
| 6 | Net Pay Summary Label | Etiqueta Neto a Pagar | column calculated value "Net Pay" | Label for net pay summary shown top-right. |  |
| 8 | Employer Fields |  |  |  |  |
| 9 | Field Name | Field Local Name | HRB Mapping | Field Explanation (RA) | Query to RA |
| 10 | Employer Legal Name | Razon Social del Empleador | $legal_entity_hr.company_legal_name | Employer legal name (razon social). |  |
| 11 | Employer Address | Domicilio del Empleador | CONCAT($legal_entity_hr.company_street_name;' ';$legal_entity_hr.company_address_number;' ';$legal_entity_hr.company_town_city;' ';$legal_entity_hr.company_department) | Full registered address in Colombia. |  |
| 12 | Employer NIT | NIT del Empleador | $legal_entity_hr.company_tax_id | Employer tax ID (NIT) issued by DIAN within the RUT. Format NNN.NNN.NNN-DV (nine digits and the check digit). |  |
| 13 | ARL Risk Class | Clase de Riesgo ARL | $legal_entity_hr.arl_risk_class | Occupational-risk class (I-V) by CIIU code; drives the employer ARL rate. |  |
| 14 | Pay Period | Periodo Liquidado | CONCAT(DATE_FORMAT($period.begin_date;'dd-MM-yyyy');' - ';DATE_FORMAT($period.end_date;'dd-MM-yyyy')) | Remuneration period (from/to). |  |
| 15 | Pay Date | Fecha de Pago | $entry.payroll_payment_date | Date salary is credited to the employee bank account. |  |
| 17 | Employee Fields |  |  |  |  |
| 18 | Field Name | Field Local Name | HRB Mapping | Field Explanation (RA) | Query to RA |
| 19 | Employee Full Name | Nombre Completo del Trabajador | CONCAT($person.first_name;' ';$person.middle_name;' ';$person.last_name) | Full name as in HR master data. |  |
| 20 | Employee Code | Codigo del Empleado | $employee.reference_code | Internal payroll reference code. |  |
| 21 | Job Title | Cargo | $employee.position | Job title / position. |  |
| 22 | Employee Department | Departamento / Centro de Costo | $employee.department | Department or cost centre. |  |
| 23 | Employee Hire Date | Fecha de Ingreso | $employee.hire_date | Date of employment commencement. |  |
| 24 | Employee Last Working Date | Fecha de Retiro | $employee.last_working_date | Populated on termination only. |  |
| 25 | Completed Years in Service | Anos Completos de Servicio | FLOOR(YEARS_BETWEEN($employee.hire_date;$period.end_date)) | Complete years from hire date; drives prima/cesantias/vacaciones accruals. |  |
| 26 | ID Document (C.C./C.E.) | Documento de Identidad (C.C./C.E.) | CONCAT($person.national_id_type;' ';$person.national_id) | Cedula de Ciudadania (C.C.) for nationals or Cedula de Extranjeria (C.E.) for foreigners. |  |
| 27 | Days in Month | Dias del Periodo | $entry.paid_days | Actual paid days in the period (Colombia commonly bases the month on 30 days). |  |
| 28 | EPS / AFP Affiliation | Afiliacion EPS / AFP | CONCAT($hr.eps_name;' / ';$hr.pension_fund_name) | Health provider (EPS) and pension fund (AFP) the employee is affiliated to. |  |
| 29 | Contract Type | Tipo de Contrato | $employee.contract_type::orLabel | Termino indefinido / termino fijo / obra o labor / salario integral. |  |
| 31 | Earning |  |  |  |  |
| 32 | Field Name | Field Local Name | HRB Mapping | Field Explanation (RA) | Query to RA |
| 33 | Earning Wage Account | Concepto de Devengo | Formula: <br> CONCAT($entry.account;' - ';$entry.account_name) <br> Series: (62100:62999) <br> Series: (65500:65899) <br> Series: (79401:79499) <br> (Align the account codes with the CO-WTC-001 wage types at set-up.) | All earning codes (devengados). Shows code, description and amount. |  |
| 34 | Unit | Unidad | Show the unit account code for the respective earning wage code per the UnitRate Account Details worksheet. <br> (Align the account codes with the CO-WTC-001 wage types at set-up.) | Unit column for earnings (hours, days). |  |
| 35 | Rate | Tarifa | Show the rate account code for the respective earning wage code per the UnitRate Account Details worksheet. <br> (Align the account codes with the CO-WTC-001 wage types at set-up.) | Unit price of the earning; only for unit-based concepts (e.g. hourly overtime). Blank for fixed monthly Salario Basico. |  |
| 36 | Amount | Valor | Show the amount for each earning account wage code. | Monetary value of each earning line in COP. |  |
| 37 | Total Earnings | Total Devengado | Show the summed value of all earnings. | Sum of all earning lines (gross). Basis (minus auxilio de transporte) for the IBC. |  |
| 39 | Deductions & Net Field |  |  |  |  |
| 40 | Field Name | Field Local Name | HRB Mapping | Field Explanation (RA) | Query to RA |
| 41 | Deduction Wage Account | Concepto de Deduccion | Formula: <br> CONCAT($entry.account;' - ';$entry.account_name) <br> Series: (21100:21999) <br> Series: (25500:25899) <br> (Align the account codes with the CO-WTC-001 wage types at set-up.) | All employee deduction codes: Salud 4%, Pension 4%, FSP, Retencion en la fuente. |  |
| 42 | Unit | Unidad (Base) | Show the contribution base (IBC) account for each social-security deduction. <br> (Align the account codes with the CO-WTC-001 wage types at set-up.) | For SS deductions the unit is the IBC (Ingreso Base de Cotizacion). |  |
| 43 | Percentage | Tarifa / Porcentaje | Show the employee percentage: Salud 4%, Pension 4%, FSP 1% (>=4 SMMLV). Leave blank for Retencion en la fuente (progressive). <br> (Align the account codes with the CO-WTC-001 wage types at set-up.) | Rate column. Fixed-rate lines show the %; progressive lines (retencion, FSP tiers) leave blank and show amount only. |  |
| 44 | Deduction Amount | Valor Deduccion | Show the amount for each deduction account wage code. | Monetary amount per deduction in COP. |  |
| 45 | Total Deductions | Total Deducciones | Show the summed value of all deductions. | Sum of all employee deductions. |  |
| 47 | Net Pay |  |  |  |  |
| 48 | Field Name | Field Local Name | HRB Mapping | Field Explanation (RA) |  |
| 49 | Net Pay | Neto a Pagar | Total Devengado - Total Deducciones | Final net pay credited to the employee. |  |
| 51 | Employer Contribution |  |  |  |  |
| 52 | Field Name | Field Local Name | HRB Mapping | Field Explanation (RA) | Query to RA |
| 53 | Employer Contribution Account | Concepto Aporte Empleador | Formula: <br> CONCAT($entry.account;' - ';$entry.account_name) <br> Series: (23550:23900) <br> (Align the account codes with the CO-WTC-001 wage types at set-up.) | Employer contributions: Salud 8.5%, Pension 12%, ARL, Caja 4%, SENA 2%, ICBF 3%. |  |
| 54 | Unit | Unidad (Base) | Show the IBC (contribution base) account for each employer contribution. <br> (Align the account codes with the CO-WTC-001 wage types at set-up.) | Unit for employer contributions = IBC. |  |
| 55 | Percentage | Tarifa Aporte Empleador | Show the employer percentage: Salud 8.5%, Pension 12%, ARL 0.522%-6.960% (by class), Caja 4%, SENA 2%, ICBF 3%. <br> (Align the account codes with the CO-WTC-001 wage types at set-up.) | Rate column. Note Art. 114-1 ET exoneration (Salud-ER/SENA/ICBF) for employees under 10 SMMLV. |  |
| 56 | Employer Contribution Amount | Valor Aporte Empleador | Show the amount for each employer contribution account. | Monetary amount per employer contribution in COP. |  |
| 57 | Total Employer Contributions | Total Aportes Empleador | Show the summed value of all employer contributions. | Sum of employer SS + parafiscales. Informational. |  |
| 58 | Social Benefit Provisions | Prestaciones Sociales (Provisiones) | Formula: <br> CONCAT($entry.account;' - ';$entry.account_name) <br> Series: (26100:26999) <br> (Align the account codes with the CO-WTC-001 wage types at set-up.) | Employer accruals: Cesantias 8.33%, Intereses 1%, Prima 8.33%, Vacaciones 4.17%. |  |
| 60 | Banking Details |  |  |  |  |
| 61 | Field Name | Field Local Name | HRB Mapping | Field Explanation (RA) | Query to RA |
| 62 | Beneficiary Name | Nombre del Titular | $primary_employee_bank_account.beneficiary_name | Account holder name matching the employee legal name. |  |
| 63 | Account Number | Numero de Cuenta | CONCAT($primary_employee_bank_account.account_type;' ';$primary_employee_bank_account.account_number) | Colombian bank account: type (ahorros/corriente) + account number (10-11 digits). |  |
| 64 | Bank | Banco | $primary_employee_bank_account.bank_name | Name of the Colombian bank. |  |
| 65 | Banking Currency | Moneda | $primary_employee_bank_account.account_currency | COP - Colombian Peso. |  |
| 67 | Footer Details |  |  |  |  |
| 68 | Field Name | Field Local Name | HRB Mapping | Field Explanation (RA) |  |
| 69 | Generated By Note | Nota de Generacion | This document has been generated by Mercans | System note: This document has been generated by Mercans. |  |
| 70 | Reference Code | Codigo de Referencia | REF-CO-2026 | Document reference code. |  |
| 71 | Copyright Note | Nota de Derechos Reservados | All rights reserved | Copyright footer: All rights reserved. |  |
| 73 | Electronic Payroll (Nomina Electronica) Fields |  |  |  |  |
| 74 | Field Name | Field Local Name | HRB Mapping | Field Explanation (RA) | Query to RA |
| 75 | CUNE | CUNE | [HRB mapping assigned at set-up] $entry.ne_cune | Unique electronic payroll document code (CUNE) of the Nomina Electronica document (Res. DIAN 227/2025 art. 1.5.3.3.1 num. 4). |  |
| 76 | Prefix / Consecutive | Prefijo / Consecutivo | [HRB mapping assigned at set-up] CONCAT($entry.ne_prefix;$entry.ne_consecutive) | Prefix and consecutive number of the document (art. 1.5.3.3.1 num. 5). |  |
| 77 | Generation Date and Time | Fecha y Hora de Generacion | [HRB mapping assigned at set-up] $entry.ne_generation_datetime | Date and time the document was generated (art. 1.5.3.3.1 num. 11). |  |
| 78 | Payment Method | Medio de Pago | [HRB mapping assigned at set-up] $entry.payment_method | Means of payment of the remuneration (art. 1.5.3.3.1 num. 10). |  |
| 79 | Digital Signature | Firma Digital | [HRB mapping assigned at set-up] $entry.ne_digital_signature | Digital signature of the document (art. 1.5.3.3.1 num. 12). |  |
| 80 | Technology Provider NIT / Software ID | NIT del Proveedor Tecnologico / ID del Software | [HRB mapping assigned at set-up] CONCAT($entry.ne_provider_nit;' / ';$entry.ne_software_id) | NIT of the technology provider and software identifier (art. 1.5.3.3.1 num. 13). |  |
| 81 | QR Code | Codigo QR | [HRB mapping assigned at set-up] CONCAT('https://catalogo-vpfe.dian.gov.co/document/searchqr?documentkey=';$entry.ne_cune) | QR code carrying the searchqr?documentkey=CUNE URL; minimum size 2 cm; must appear on every page (Anexo Tecnico Nomina Electronica, pp. 260-261). |  |
| 83 | Version Control |  |  |  |  |
| 84 | Version | Date | Description | Author |  |
| 85 | v1.2 | 2026-10-30 | Statutory validation against an independent recalculation and the primary sources: worked example completed (solidarity fund, withholding, occupational risk, family compensation fund, severance savings and interest, contribution base), net pay 15,221,235.40 and employer contributions 5,764,300; prima and vacation provisions at 1/12 and 15/360; payslip fields of Res. DIAN 000227 de 2025 (payment means, generation time, signature, provider and software); citations updated (Res. DIAN 000227 de 2025, Decretos 1469 and 1470 de 2025, ET art. 114-1, occupational-risk classes, severance savings). | Wallisson Gomes |  |
| 86 | v1.3 | 2026-11-02 | Statutory validation, second pass: the 790-UVT and 1,340-UVT caps are annual and tracked year-to-date (no monthly one-twelfth limit); worked example (August 2026, same pay since January) withholding 1,993,152.00 and net pay 15,478,848.00; note on the withholding (row 82). Released 2026-11-02 — approved by Wallisson Gomes. | Wallisson Gomes |  |


## Sheet: Field Option


| Row | Field Name | Option Value | Option Description | Usage Context |
|---|---|---|---|---|
| 2 | CURRENCY | COP | Colombian Peso | Displayed currency in payslip summary and banking section |


## Sheet: Population Range


| Row | Worker Situation | Include? (YES/NO) | Notes |
|---|---|---|---|
| 2 | Active employees (full-time) | YES | Generate desprendible de pago for all active full-time employees on termino indefinido or termino fijo contracts. Full salary, social security and prestaciones sociales apply. |
| 3 | Active employees (part-time / part-period) | YES | Same layout with actual worked time. IBC floor 1 SMMLV (Ley 100 de 1993 art. 18). Exception: a dependent part-time worker hired for less than 30 days in the month and paid less than 1 SMMLV (Decreto 1072 de 2015 art. 2.2.1.6.4.2) is reported as cotizante 51: pension and CCF IBC in quarters of SMMLV by days worked (1-7 = 1/4, 8-14 = 1/2, 15-21 = 3/4, 22-30 = 1); ARL IBC = 1 SMMLV for 30 days (AT2 v30 p.117). Prestaciones prorated. |
| 4 | New hires during period | YES | Prorate salary, social security and prestaciones to days worked from the hire date. Auxilio de transporte prorated where applicable (salary up to 2 SMMLV). |
| 5 | Terminations during period | YES | Populate Fecha de Retiro. Include liquidacion definitiva: cesantias + intereses, vacaciones acumuladas, prima proporcional, and indemnizacion por despido sin justa causa if applicable (CST Art. 64). |
| 6 | Sick leave - enfermedad general | YES | Employer pays days 1-2; EPS pays from day 3 at 66.67% of IBC for the first 90 days, then 50% for days 91-180 (Decreto 780 de 2016; CST Art. 227). Show the incapacidad as an income line. |
| 7 | Maternity / paternity leave | YES | Maternity 18 weeks and paternity 2 weeks, funded by the EPS at 100% of IBC (CST Art. 236, paternity in par. 2; Ley 1822 de 2017; Ley 2114 de 2021 art. 2). Show EPS benefit as an income line where the employer advances it. |
| 8 | Unpaid leave (licencia no remunerada) | CONDITIONAL | Generate a record when payroll issues one. Salary suspended; social-security contributions are generally suspended by agreement, but the affiliation must be handled per EPS/AFP rules. |
| 9 | Salario integral employees | YES | Colombia-specific: salary >= 13 SMMLV agreed as integral. IBC = 70% of the integral salary (factor prestacional 30%). No separate prima / cesantias / intereses lines (already included). |
| 10 | Apprentices (contrato de aprendizaje - SENA) | CONDITIONAL | Colombia-specific: apprentices receive an apoyo de sostenimiento (not salary), affiliated to health and ARL only, no pension/parafiscales. Include only if payroll processes the apoyo. |
| 11 | Foreign workers (Cedula de Extranjeria) | YES | Same template. Identify with C.E. Same social security and retencion en la fuente as nationals unless covered by a bilateral totalization agreement for pension. |
| 12 | Board members / directors | CONDITIONAL | Include if bound by an employment contract (subordination). Statutory representatives with an employment relationship: standard nomina. Pure honorarios (fees) are billed separately. |
| 13 | Contractors / self-employed (prestacion de servicios) | NO | Do not include. Independent contractors invoice via cuenta de cobro / factura and pay their own social security on 40% of income. Verify contribution before payment; not part of nomina. |


## Sheet: Unit Rate Details


| Row |  | Earning | Rate | Unit | Illustrative account codes; align them to the CO-WTC-001 wage-type codes during set-up. |
|---|---|---|---|---|---|
| 3 | Basic Salary (Salario Basico) | 62100 | 62104 | 63100 |  |
| 4 | Salary Advance (Anticipo de Salario) | 62103 |  | 63103 |  |
| 5 | Overtime - Daytime (Hora Extra Diurna 25%) | 62110 | 62105 | 63110 |  |
| 6 | Overtime - Night (Hora Extra Nocturna 75%) | 62111 | 62106 | 63111 |  |
| 7 | Night Surcharge (Recargo Nocturno 35%) | 62120 | 62107 | 63120 |  |
| 8 | Sunday/Holiday Surcharge (Recargo Dominical y Festivo 80% to 30-Jun-2026 / 90% from 1-Jul-2026) | 62121 | 62108 | 63121 |  |
| 9 | Sunday/Holiday Overtime (Hora Extra Dominical/Festiva: overtime 25% day / 75% night plus the rest-day surcharge 80% / 90%) | 62122 | 62109 | 63122 |  |
| 10 | Commission (Comisiones) | 62200 |  | 63200 |  |
| 11 | Bonus - salary (Bonificacion Constitutiva de Salario) | 62210 |  | 63210 |  |
| 12 | Bonus - non-salary (Bonificacion No Constitutiva) | 62211 |  | 63211 |  |
| 13 | Transport Allowance (Auxilio de Transporte) | 62300 |  | 63300 |  |
| 14 | Connectivity Allowance (Auxilio de Conectividad) | 62301 |  | 63301 |  |
| 15 | Food Allowance (Auxilio de Alimentacion) | 62302 |  | 63302 |  |
| 16 | Per-diem / Subsistence (Viaticos) | 62310 |  | 63310 |  |
| 17 | Service Bonus (Prima de Servicios) | 65500 |  | 75500 |  |
| 18 | Severance (Cesantias) | 65510 |  | 75510 |  |
| 19 | Interest on Severance (Intereses a las Cesantias) | 65511 |  | 75511 |  |
| 20 | Annual Leave Pay (Vacaciones) | 65520 | 65521 | 75520 |  |
| 21 | Annual Leave Cash-out (Vacaciones Compensadas) | 65522 |  | 75522 |  |
| 22 | Sick Leave - general illness (Incapacidad Enfermedad General) | 79408 |  | 79008 |  |
| 23 | Work-injury Leave (Incapacidad de Origen Laboral - ARL) | 79409 |  | 79009 |  |
| 24 | Maternity Leave (Licencia de Maternidad) | 79406 |  | 79006 |  |
| 25 | Paternity Leave (Licencia de Paternidad) | 79407 |  | 79007 |  |
| 26 | Paid Statutory Leave (Licencia Remunerada) | 79420 |  | 79020 |  |
| 27 | Unpaid Leave (Licencia No Remunerada) | 79435 |  | 79035 |  |
| 28 | Public Holiday Pay (Dia Festivo) | 79411 |  | 79011 |  |
| 29 | Severance Indemnity (Indemnizacion por Despido - CST Art. 64) | 65650 |  | 75650 |  |
| 30 | Integral Salary (Salario Integral) | 62150 |  | 63150 |  |
