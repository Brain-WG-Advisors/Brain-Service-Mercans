# US_Compliance_Payslip_Generator


## How to set up Payslip

|  | United States of America Compliance Payslip Generator |  |
|---|---|---|
|  | Document ID | US-PSL-001 |
|  | Package version | v1.0 |
|  | Status | For QA |
|  | Related documents | US-CCG-001 v1.0; US-WTC-001 v1.0; US-DD-001 v1.0 |
|  | Version Control | Version \| Issue date \| Author \| Status |
|  | v1.0 | 2027-03-31 \| Wallisson Gomes \| For QA |
|  | What this workbook is | One US payslip template with per-State rules. The tab Compliance Payslip is the language-neutral master. The tabs United States (EN) and United States (ES) carry the same fields in English and Spanish. Payslip Spec maps every printed field to the HR and payroll system. Field Option lists the controlled values and the pay-statement rules per work-location State. Population Range says who receives the payslip. Unit Rate Details lists the earning codes with their rate and unit accounts. |
|  | 1. Pick the rule set | Read the work-location State of the employee. Open Field Option, block STATE_STATEMENT_RULE, and read the row of that State. The rule set follows the work location, not the residence. |
|  | 2. Copy the master | Create a new tab, copy the payslip from Compliance Payslip, and translate the labels. Keep the pay element lines in the form code, dash, wage type name; the codes come from US-WTC-001 v1.0. |
|  | 3. Switch the optional blocks | Print the paid leave balance block, the tips and gratuities line, the compensation sources, the pay-code guide reference, compensatory time, minimum-wage allowances, piece-rate units, sick pay received (Arizona), the New York City protected time off detail, benefits earned (New Mexico) and the employer operating name and mailing address (Minnesota) only for the work-location States whose rule names them (Field Option, block STATE_STATEMENT_RULE and block LEAVE_BALANCE_RULE). |
|  | 4. Social Security number | Print the last four digits at most, and no digits for the States whose rule bars it (Field Option, block SSN_DISPLAY_RULE). |
|  | 5. Check the totals | Gross earnings is the sum of the earnings lines; total deductions is the sum of the deduction lines; net pay is gross earnings minus total deductions. The net pay box in the title band repeats the net pay row. The tax lines come from the calculation basis blocks under the payslip: the social security line is the lesser of the remaining annual maximum and the rate times the period base. |
|  | 6. Export | Use Normal margins, save the tab as PDF, and deliver it electronically with the consent record and the free print or download access described in Field Option, block ELECTRONIC_DELIVERY_RULE. |
|  | Illustrative sample | Every name, address, identifier and amount on the payslip tabs is fictitious and shows the layout only. The amounts are computed from the statutory rates, not typed. |

## Compliance Payslip

|  |  |  |  |  |  |  | Net Pay: |
|---|---|---|---|---|---|---|---|
|  |  | United States Payslip - master |  |  |  |  | =H34 |
|  |  |  |  |  |  |  | USD |
| Employer Name |  | Mercans Compliance Sample Inc. |  |  | Pay Period |  | 10/05/2026 - 10/18/2026 |
| Employer Address |  | 100 Sample Street, Austin, TX 00000 |  |  | Pay Date |  | 10/23/2026 |
| Employer Phone |  | (000) 000-0000 |  |  | Pay Frequency |  | Biweekly |
| Employer Identification Number (EIN) |  | 00-0000000 |  |  | Work-location State |  | TX |
| Employee Name |  | Alex Sample |  |  | Employee ID |  | E-000045 |
| Employee Home Address |  | 200 Example Avenue, Austin, TX 00000 |  |  | Social Security Number (last 4 digits) |  | ***-**-0000 |
| Job Title |  | Operations Analyst |  |  | Hire Date |  | 03/01/2021 |
| Rate-of-Pay Basis |  | Hourly |  |  | Federal Filing Status (Form W-4) |  | Single or Married filing separately |
| Earnings |  |  |  |  |  |  |  |
| Earnings |  |  |  |  | Rate | Hours / units | Amount |
| 62100 - Basic salary |  |  |  |  | 36 | 80 | 2880 |
| 62110 - Overtime - type 1 |  |  |  |  | 54 | 4 | 216 |
| US-042 - Commission |  |  |  |  |  |  | 17000 |
| Gross Earning |  |  |  |  |  |  | =SUM(H19:H21) |
| Total Hours Worked |  |  |  |  |  | =SUM(G19:G21) |  |
| Deduction Item |  |  |  |  | Rate | Hours / units | Amount |
| 21640 - Pre-tax 401(k) elective deferral - employee deduction |  |  |  |  |  |  | 1004.8 |
| 21610 - Health insurance & Life insurance contributions - type 1 |  |  |  |  |  |  | 85 |
| US-001 - Federal income tax withholding (FIT) - regular wages |  |  |  |  |  |  | =H126 |
| 21900 - Social security tax (OASDI) - employee |  |  |  |  |  |  | =H86 |
| US-006 - Medicare tax - employee |  |  |  |  |  |  | =H95 |
| US-008 - Additional Medicare Tax - employee |  |  |  |  |  |  | =H102 |
| Total Deductions |  |  |  |  |  |  | =SUM(H26:H31) |
| Net Pay: |  |  |  |  |  |  | =H22-H32 |
| Employer Contribution |  |  |  |  | Rate | Hours / units | Amount |
| US-005 - Social security tax (OASDI) - employer |  |  |  |  |  |  | =H91 |
| US-007 - Medicare tax - employer |  |  |  |  |  |  | =H97 |
| Total Employer Contribution |  |  |  |  |  |  | =SUM(H37:H38) |
| Paid Leave Balance |  |  |  |  |  |  |  |
| Paid sick leave accrued (hours) |  |  |  |  |  |  | not printed |
| Paid sick leave used (hours) |  |  |  |  |  |  | not printed |
| Paid sick leave available (hours) |  |  |  |  |  |  | not printed |
| Payment details |  |  |  |  |  |  |  |
| Bank name |  | Account (masked) |  |  | Payment method |  | Amount |
| Sample Bank |  | ****0000 |  |  | Direct deposit |  | =H34 |
| State-switched fields (printed when the work-location State requires them) |  |  |  |  |  |  |  |
| Tips and gratuities (separate line) |  |  |  |  |  |  | not printed |
| Compensation sources |  |  |  |  |  |  | not printed |
| Pay-code guide reference |  |  |  |  |  |  | not printed |
| Compensatory time |  |  |  |  |  |  | not printed |
| Allowances credited toward minimum wage |  |  |  |  |  |  | not printed |
| Piece-rate units and rate |  |  |  |  |  |  | not printed |
| Paid sick leave pay received year to date (USD) |  |  |  |  |  |  | not printed |
| PTO accrued this period (hours) |  |  |  |  |  |  | not printed |
| Paid PTO used this period (hours) |  |  |  |  |  |  | not printed |
| Unpaid PTO used this period (hours) |  |  |  |  |  |  | not printed |
| Unpaid PTO available (hours) |  |  |  |  |  |  | not printed |
| Benefits earned (employer-paid) |  |  |  |  |  |  | not printed |
| Employer operating name (if different) |  |  |  |  |  |  | not printed |
| Employer mailing address (if different) |  |  |  |  |  |  | not printed |
| YTD Cumulative Figures |  |  |  |  |  |  |  |
| YTD Gross Earnings |  |  |  |  |  |  | =H103+H22 |
| YTD Federal Income Tax Withheld |  |  |  |  |  |  | 31000 |
| YTD Social Security Tax Withheld |  |  |  |  |  |  | =H83+H86 |
| YTD Medicare Tax Withheld |  |  |  |  |  |  | =H94+H95+H102 |
| YTD Pre-tax 401(k) Deferral |  |  |  |  |  |  | 9000 |
| Illustrative sample: fictitious employee and amounts |  |  |  |  |  |  |  |
| This document has been generated by Mercans |  |  |  |  |  |  |  |
| Language-neutral master: copy this tab to add a language tab |  |  |  |  |  |  |  |
| Supporting calculations: not printed with the payslip |  |  |  |  |  |  |  |
| FICA calculation basis (lesser of the remaining annual maximum or rate x period base) |  |  |  |  |  |  |  |
| Social security wage base: 184,500 USD |  |  |  |  |  |  | 184500 |
| Social security rate, employee: 6.2% |  |  |  |  |  |  | 0.062 |
| Social security wages of this payslip (gross earnings less the cafeteria-plan contribution) |  |  |  |  |  |  | =H22-H27 |
| Social security wages paid before this payslip (year to date, limited to the wage base) |  |  |  |  |  |  | 181500 |
| Social security tax withheld before this payslip (year to date) |  |  |  |  |  |  | =ROUND(H82*H80,2) |
| Remaining annual maximum tax = rate x wage base less tax withheld to date |  |  |  |  |  |  | =ROUND(H79*H80,2)-H83 |
| Rate x social security wages of this payslip |  |  |  |  |  |  | =ROUND(H81*H80,2) |
| Social security tax withheld = lesser of the two amounts above |  |  |  |  |  |  | =MAX(0,MIN(H84,H85)) |
| Social security rate, employer: 6.2% |  |  |  |  |  |  | 0.062 |
| Employer social security tax paid before this payslip (year to date) |  |  |  |  |  |  | =ROUND(H82*H87,2) |
| Remaining annual maximum employer tax = rate x wage base less employer tax paid to date |  |  |  |  |  |  | =ROUND(H79*H87,2)-H88 |
| Employer rate x social security wages of this payslip |  |  |  |  |  |  | =ROUND(H81*H87,2) |
| Employer social security tax = lesser of the two amounts above |  |  |  |  |  |  | =MAX(0,MIN(H89,H90)) |
| Medicare rate, employee: 1.45% |  |  |  |  |  |  | 0.0145 |
| Medicare wages paid before this payslip (year to date, no wage base) |  |  |  |  |  |  | 181500 |
| Medicare tax withheld before this payslip (year to date) |  |  |  |  |  |  | =ROUND(H93*H92,2) |
| Medicare tax withheld = rate x Medicare wages of this payslip |  |  |  |  |  |  | =ROUND(H81*H92,2) |
| Medicare rate, employer: 1.45% |  |  |  |  |  |  | 0.0145 |
| Employer Medicare tax = rate x Medicare wages of this payslip |  |  |  |  |  |  | =ROUND(H81*H96,2) |
| Additional Medicare Tax withholding threshold: 200,000 USD |  |  |  |  |  |  | 200000 |
| Additional Medicare Tax rate: 0.9% |  |  |  |  |  |  | 0.009 |
| Medicare wages year to date including this payslip |  |  |  |  |  |  | =H93+H81 |
| Wages above the threshold, limited to this payslip |  |  |  |  |  |  | =MAX(0,MIN(H81,H100-H98)) |
| Additional Medicare Tax withheld = rate x wages above the threshold |  |  |  |  |  |  | =ROUND(H101*H99,2) |
| Earnings paid before this payslip (year to date) |  |  |  |  |  |  | 185000 |
| Federal income tax calculation basis (annual percentage method, standard table) |  |  |  |  |  |  |  |
| Method: IRS Pub. 15-T (2026) Worksheet 1A with the Annual Percentage Method tables (STANDARD schedule; Step-2-checked schedule when W-4 Step 2 box checked) |  |  |  |  |  |  |  |
| Line 1a: taxable wages of this payslip (gross less 401(k) deferral and cafeteria-plan contribution) |  |  |  |  |  |  | =H22-H26-H27 |
| Line 1b: pay periods per year |  |  |  |  |  |  | 26 |
| Line 1c: annualised wages = 1a x 1b |  |  |  |  |  |  | =H107*H108 |
| Line 1g: Step 2 box not checked, single or married filing separately: 8,600 USD |  |  |  |  |  |  | 8600 |
| Line 1i: adjusted annual wage amount = 1c less 1g |  |  |  |  |  |  | =MAX(0,H109-H110) |
| Standard table thresholds, single or married filing separately: 0/7500/19900/57900/113200/209275/263725/648100 |  |  |  |  |  |  |  |
| Marginal rates of the table: 0/10/12/22/24/32/35/37 |  |  |  |  |  |  |  |
| Bracket 1: Tax in the bracket = (adjusted annual wage - threshold) x increase in the rate |  |  |  |  | 0 | 0 | =MAX(0,H111-F114)*(G114-0) |
| Bracket 2: Tax in the bracket = (adjusted annual wage - threshold) x increase in the rate |  |  |  |  | 7500 | 0.1 | =MAX(0,H111-F115)*(G115-G114) |
| Bracket 3: Tax in the bracket = (adjusted annual wage - threshold) x increase in the rate |  |  |  |  | 19900 | 0.12 | =MAX(0,H111-F116)*(G116-G115) |
| Bracket 4: Tax in the bracket = (adjusted annual wage - threshold) x increase in the rate |  |  |  |  | 57900 | 0.22 | =MAX(0,H111-F117)*(G117-G116) |
| Bracket 5: Tax in the bracket = (adjusted annual wage - threshold) x increase in the rate |  |  |  |  | 113200 | 0.24 | =MAX(0,H111-F118)*(G118-G117) |
| Bracket 6: Tax in the bracket = (adjusted annual wage - threshold) x increase in the rate |  |  |  |  | 209275 | 0.32 | =MAX(0,H111-F119)*(G119-G118) |
| Bracket 7: Tax in the bracket = (adjusted annual wage - threshold) x increase in the rate |  |  |  |  | 263725 | 0.35 | =MAX(0,H111-F120)*(G120-G119) |
| Bracket 8: Tax in the bracket = (adjusted annual wage - threshold) x increase in the rate |  |  |  |  | 648100 | 0.37 | =MAX(0,H111-F121)*(G121-G120) |
| Tentative annual withholding amount |  |  |  |  |  |  | =SUM(H114:H121) |
| Tentative withholding per pay period = annual amount / pay periods, rounded half-up to the cent |  |  |  |  |  |  | =ROUND(H122/H108,2) |
| Step 3 credits per pay period (none in this sample) |  |  |  |  |  |  | 0 |
| Step 4(c) extra withholding per pay period (none in this sample) |  |  |  |  |  |  | 0 |
| Federal income tax withheld this payslip |  |  |  |  |  |  | =MAX(0,H123-H124+H125) |

## United States (EN)

|  |  |  |  |  |  |  | Net Pay: |
|---|---|---|---|---|---|---|---|
|  |  | United States Payslip |  |  |  |  | =H34 |
|  |  |  |  |  |  |  | USD |
| Employer Name |  | Mercans Compliance Sample Inc. |  |  | Pay Period |  | 10/05/2026 - 10/18/2026 |
| Employer Address |  | 100 Sample Street, Austin, TX 00000 |  |  | Pay Date |  | 10/23/2026 |
| Employer Phone |  | (000) 000-0000 |  |  | Pay Frequency |  | Biweekly |
| Employer Identification Number (EIN) |  | 00-0000000 |  |  | Work-location State |  | TX |
| Employee Name |  | Alex Sample |  |  | Employee ID |  | E-000045 |
| Employee Home Address |  | 200 Example Avenue, Austin, TX 00000 |  |  | Social Security Number (last 4 digits) |  | ***-**-0000 |
| Job Title |  | Operations Analyst |  |  | Hire Date |  | 03/01/2021 |
| Rate-of-Pay Basis |  | Hourly |  |  | Federal Filing Status (Form W-4) |  | Single or Married filing separately |
| Earnings |  |  |  |  |  |  |  |
| Earnings |  |  |  |  | Rate | Hours / units | Amount |
| 62100 - Basic salary |  |  |  |  | 36 | 80 | 2880 |
| 62110 - Overtime - type 1 |  |  |  |  | 54 | 4 | 216 |
| US-042 - Commission |  |  |  |  |  |  | 17000 |
| Gross Earning |  |  |  |  |  |  | =SUM(H19:H21) |
| Total Hours Worked |  |  |  |  |  | =SUM(G19:G21) |  |
| Deduction Item |  |  |  |  | Rate | Hours / units | Amount |
| 21640 - Pre-tax 401(k) elective deferral - employee deduction |  |  |  |  |  |  | 1004.8 |
| 21610 - Health insurance & Life insurance contributions - type 1 |  |  |  |  |  |  | 85 |
| US-001 - Federal income tax withholding (FIT) - regular wages |  |  |  |  |  |  | =H125 |
| 21900 - Social security tax (OASDI) - employee |  |  |  |  |  |  | =H85 |
| US-006 - Medicare tax - employee |  |  |  |  |  |  | =H94 |
| US-008 - Additional Medicare Tax - employee |  |  |  |  |  |  | =H101 |
| Total Deductions |  |  |  |  |  |  | =SUM(H26:H31) |
| Net Pay: |  |  |  |  |  |  | =H22-H32 |
| Employer Contribution |  |  |  |  | Rate | Hours / units | Amount |
| US-005 - Social security tax (OASDI) - employer |  |  |  |  |  |  | =H90 |
| US-007 - Medicare tax - employer |  |  |  |  |  |  | =H96 |
| Total Employer Contribution |  |  |  |  |  |  | =SUM(H37:H38) |
| Paid Leave Balance |  |  |  |  |  |  |  |
| Paid sick leave accrued (hours) |  |  |  |  |  |  | not printed |
| Paid sick leave used (hours) |  |  |  |  |  |  | not printed |
| Paid sick leave available (hours) |  |  |  |  |  |  | not printed |
| Payment details |  |  |  |  |  |  |  |
| Bank name |  | Account (masked) |  |  | Payment method |  | Amount |
| Sample Bank |  | ****0000 |  |  | Direct deposit |  | =H34 |
| State-switched fields (printed when the work-location State requires them) |  |  |  |  |  |  |  |
| Tips and gratuities (separate line) |  |  |  |  |  |  | not printed |
| Compensation sources |  |  |  |  |  |  | not printed |
| Pay-code guide reference |  |  |  |  |  |  | not printed |
| Compensatory time |  |  |  |  |  |  | not printed |
| Allowances credited toward minimum wage |  |  |  |  |  |  | not printed |
| Piece-rate units and rate |  |  |  |  |  |  | not printed |
| Paid sick leave pay received year to date (USD) |  |  |  |  |  |  | not printed |
| PTO accrued this period (hours) |  |  |  |  |  |  | not printed |
| Paid PTO used this period (hours) |  |  |  |  |  |  | not printed |
| Unpaid PTO used this period (hours) |  |  |  |  |  |  | not printed |
| Unpaid PTO available (hours) |  |  |  |  |  |  | not printed |
| Benefits earned (employer-paid) |  |  |  |  |  |  | not printed |
| Employer operating name (if different) |  |  |  |  |  |  | not printed |
| Employer mailing address (if different) |  |  |  |  |  |  | not printed |
| YTD Cumulative Figures |  |  |  |  |  |  |  |
| YTD Gross Earnings |  |  |  |  |  |  | =H102+H22 |
| YTD Federal Income Tax Withheld |  |  |  |  |  |  | 31000 |
| YTD Social Security Tax Withheld |  |  |  |  |  |  | =H82+H85 |
| YTD Medicare Tax Withheld |  |  |  |  |  |  | =H93+H94+H101 |
| YTD Pre-tax 401(k) Deferral |  |  |  |  |  |  | 9000 |
| Illustrative sample: fictitious employee and amounts |  |  |  |  |  |  |  |
| This document has been generated by Mercans |  |  |  |  |  |  |  |
| Supporting calculations: not printed with the payslip |  |  |  |  |  |  |  |
| FICA calculation basis (lesser of the remaining annual maximum or rate x period base) |  |  |  |  |  |  |  |
| Social security wage base: 184,500 USD |  |  |  |  |  |  | 184500 |
| Social security rate, employee: 6.2% |  |  |  |  |  |  | 0.062 |
| Social security wages of this payslip (gross earnings less the cafeteria-plan contribution) |  |  |  |  |  |  | =H22-H27 |
| Social security wages paid before this payslip (year to date, limited to the wage base) |  |  |  |  |  |  | 181500 |
| Social security tax withheld before this payslip (year to date) |  |  |  |  |  |  | =ROUND(H81*H79,2) |
| Remaining annual maximum tax = rate x wage base less tax withheld to date |  |  |  |  |  |  | =ROUND(H78*H79,2)-H82 |
| Rate x social security wages of this payslip |  |  |  |  |  |  | =ROUND(H80*H79,2) |
| Social security tax withheld = lesser of the two amounts above |  |  |  |  |  |  | =MAX(0,MIN(H83,H84)) |
| Social security rate, employer: 6.2% |  |  |  |  |  |  | 0.062 |
| Employer social security tax paid before this payslip (year to date) |  |  |  |  |  |  | =ROUND(H81*H86,2) |
| Remaining annual maximum employer tax = rate x wage base less employer tax paid to date |  |  |  |  |  |  | =ROUND(H78*H86,2)-H87 |
| Employer rate x social security wages of this payslip |  |  |  |  |  |  | =ROUND(H80*H86,2) |
| Employer social security tax = lesser of the two amounts above |  |  |  |  |  |  | =MAX(0,MIN(H88,H89)) |
| Medicare rate, employee: 1.45% |  |  |  |  |  |  | 0.0145 |
| Medicare wages paid before this payslip (year to date, no wage base) |  |  |  |  |  |  | 181500 |
| Medicare tax withheld before this payslip (year to date) |  |  |  |  |  |  | =ROUND(H92*H91,2) |
| Medicare tax withheld = rate x Medicare wages of this payslip |  |  |  |  |  |  | =ROUND(H80*H91,2) |
| Medicare rate, employer: 1.45% |  |  |  |  |  |  | 0.0145 |
| Employer Medicare tax = rate x Medicare wages of this payslip |  |  |  |  |  |  | =ROUND(H80*H95,2) |
| Additional Medicare Tax withholding threshold: 200,000 USD |  |  |  |  |  |  | 200000 |
| Additional Medicare Tax rate: 0.9% |  |  |  |  |  |  | 0.009 |
| Medicare wages year to date including this payslip |  |  |  |  |  |  | =H92+H80 |
| Wages above the threshold, limited to this payslip |  |  |  |  |  |  | =MAX(0,MIN(H80,H99-H97)) |
| Additional Medicare Tax withheld = rate x wages above the threshold |  |  |  |  |  |  | =ROUND(H100*H98,2) |
| Earnings paid before this payslip (year to date) |  |  |  |  |  |  | 185000 |
| Federal income tax calculation basis (annual percentage method, standard table) |  |  |  |  |  |  |  |
| Method: IRS Pub. 15-T (2026) Worksheet 1A with the Annual Percentage Method tables (STANDARD schedule; Step-2-checked schedule when W-4 Step 2 box checked) |  |  |  |  |  |  |  |
| Line 1a: taxable wages of this payslip (gross less 401(k) deferral and cafeteria-plan contribution) |  |  |  |  |  |  | =H22-H26-H27 |
| Line 1b: pay periods per year |  |  |  |  |  |  | 26 |
| Line 1c: annualised wages = 1a x 1b |  |  |  |  |  |  | =H106*H107 |
| Line 1g: Step 2 box not checked, single or married filing separately: 8,600 USD |  |  |  |  |  |  | 8600 |
| Line 1i: adjusted annual wage amount = 1c less 1g |  |  |  |  |  |  | =MAX(0,H108-H109) |
| Standard table thresholds, single or married filing separately: 0/7500/19900/57900/113200/209275/263725/648100 |  |  |  |  |  |  |  |
| Marginal rates of the table: 0/10/12/22/24/32/35/37 |  |  |  |  |  |  |  |
| Bracket 1: Tax in the bracket = (adjusted annual wage - threshold) x increase in the rate |  |  |  |  | 0 | 0 | =MAX(0,H110-F113)*(G113-0) |
| Bracket 2: Tax in the bracket = (adjusted annual wage - threshold) x increase in the rate |  |  |  |  | 7500 | 0.1 | =MAX(0,H110-F114)*(G114-G113) |
| Bracket 3: Tax in the bracket = (adjusted annual wage - threshold) x increase in the rate |  |  |  |  | 19900 | 0.12 | =MAX(0,H110-F115)*(G115-G114) |
| Bracket 4: Tax in the bracket = (adjusted annual wage - threshold) x increase in the rate |  |  |  |  | 57900 | 0.22 | =MAX(0,H110-F116)*(G116-G115) |
| Bracket 5: Tax in the bracket = (adjusted annual wage - threshold) x increase in the rate |  |  |  |  | 113200 | 0.24 | =MAX(0,H110-F117)*(G117-G116) |
| Bracket 6: Tax in the bracket = (adjusted annual wage - threshold) x increase in the rate |  |  |  |  | 209275 | 0.32 | =MAX(0,H110-F118)*(G118-G117) |
| Bracket 7: Tax in the bracket = (adjusted annual wage - threshold) x increase in the rate |  |  |  |  | 263725 | 0.35 | =MAX(0,H110-F119)*(G119-G118) |
| Bracket 8: Tax in the bracket = (adjusted annual wage - threshold) x increase in the rate |  |  |  |  | 648100 | 0.37 | =MAX(0,H110-F120)*(G120-G119) |
| Tentative annual withholding amount |  |  |  |  |  |  | =SUM(H113:H120) |
| Tentative withholding per pay period = annual amount / pay periods, rounded half-up to the cent |  |  |  |  |  |  | =ROUND(H121/H107,2) |
| Step 3 credits per pay period (none in this sample) |  |  |  |  |  |  | 0 |
| Step 4(c) extra withholding per pay period (none in this sample) |  |  |  |  |  |  | 0 |
| Federal income tax withheld this payslip |  |  |  |  |  |  | =MAX(0,H122-H123+H124) |

## United States (ES)

|  |  |  |  |  |  |  | Pago neto: |
|---|---|---|---|---|---|---|---|
|  |  | Recibo de pago de Estados Unidos |  |  |  |  | =H34 |
|  |  |  |  |  |  |  | USD |
| Nombre del empleador |  | Mercans Compliance Sample Inc. |  |  | Período de pago |  | 10/05/2026 - 10/18/2026 |
| Dirección del empleador |  | 100 Sample Street, Austin, TX 00000 |  |  | Fecha de pago |  | 10/23/2026 |
| Teléfono del empleador |  | (000) 000-0000 |  |  | Frecuencia de pago |  | Cada dos semanas |
| Número de identificación del empleador (EIN) |  | 00-0000000 |  |  | Estado del lugar de trabajo |  | TX |
| Nombre del empleado |  | Alex Sample |  |  | Número de empleado |  | E-000045 |
| Domicilio del empleado |  | 200 Example Avenue, Austin, TX 00000 |  |  | Número de Seguro Social (últimos 4 dígitos) |  | ***-**-0000 |
| Puesto |  | Analista de operaciones |  |  | Fecha de contratación |  | 03/01/2021 |
| Base de la tarifa de pago |  | Por hora |  |  | Estado civil federal (Formulario W-4) |  | Soltero o casado que declara por separado |
| Ingresos |  |  |  |  |  |  |  |
| Ingresos |  |  |  |  | Tarifa | Horas / unidades | Importe |
| 62100 - Basic salary |  |  |  |  | 36 | 80 | 2880 |
| 62110 - Overtime - type 1 |  |  |  |  | 54 | 4 | 216 |
| US-042 - Commission |  |  |  |  |  |  | 17000 |
| Ingreso bruto |  |  |  |  |  |  | =SUM(H19:H21) |
| Total de horas trabajadas |  |  |  |  |  | =SUM(G19:G21) |  |
| Concepto de deducción |  |  |  |  | Tarifa | Horas / unidades | Importe |
| 21640 - Pre-tax 401(k) elective deferral - employee deduction |  |  |  |  |  |  | 1004.8 |
| 21610 - Health insurance & Life insurance contributions - type 1 |  |  |  |  |  |  | 85 |
| US-001 - Federal income tax withholding (FIT) - regular wages |  |  |  |  |  |  | =H125 |
| 21900 - Social security tax (OASDI) - employee |  |  |  |  |  |  | =H85 |
| US-006 - Medicare tax - employee |  |  |  |  |  |  | =H94 |
| US-008 - Additional Medicare Tax - employee |  |  |  |  |  |  | =H101 |
| Total de deducciones |  |  |  |  |  |  | =SUM(H26:H31) |
| Pago neto: |  |  |  |  |  |  | =H22-H32 |
| Aportación del empleador |  |  |  |  | Tarifa | Horas / unidades | Importe |
| US-005 - Social security tax (OASDI) - employer |  |  |  |  |  |  | =H90 |
| US-007 - Medicare tax - employer |  |  |  |  |  |  | =H96 |
| Total de aportaciones del empleador |  |  |  |  |  |  | =SUM(H37:H38) |
| Saldo de licencia pagada |  |  |  |  |  |  |  |
| Licencia por enfermedad acumulada (horas) |  |  |  |  |  |  | no se imprime |
| Licencia por enfermedad usada (horas) |  |  |  |  |  |  | no se imprime |
| Licencia por enfermedad disponible (horas) |  |  |  |  |  |  | no se imprime |
| Datos de pago |  |  |  |  |  |  |  |
| Banco |  | Cuenta (enmascarada) |  |  | Forma de pago |  | Importe |
| Banco de muestra |  | ****0000 |  |  | Depósito directo |  | =H34 |
| Campos según el Estado (se imprimen cuando el Estado del lugar de trabajo los exige) |  |  |  |  |  |  |  |
| Propinas y gratificaciones (línea separada) |  |  |  |  |  |  | no se imprime |
| Fuentes de compensación |  |  |  |  |  |  | no se imprime |
| Referencia de la guía de códigos de pago |  |  |  |  |  |  | no se imprime |
| Tiempo compensatorio |  |  |  |  |  |  | no se imprime |
| Asignaciones acreditadas al salario mínimo |  |  |  |  |  |  | no se imprime |
| Unidades y tarifa por pieza |  |  |  |  |  |  | no se imprime |
| Pago recibido por licencia por enfermedad en el año (USD) |  |  |  |  |  |  | no se imprime |
| Tiempo libre pagado acumulado en el período (horas) |  |  |  |  |  |  | no se imprime |
| Tiempo libre pagado usado en el período (horas) |  |  |  |  |  |  | no se imprime |
| Tiempo libre no pagado usado en el período (horas) |  |  |  |  |  |  | no se imprime |
| Tiempo libre no pagado disponible (horas) |  |  |  |  |  |  | no se imprime |
| Beneficios devengados (pagados por el empleador) |  |  |  |  |  |  | no se imprime |
| Nombre comercial del empleador (si es distinto) |  |  |  |  |  |  | no se imprime |
| Domicilio postal del empleador (si es distinto) |  |  |  |  |  |  | no se imprime |
| Acumulado del año |  |  |  |  |  |  |  |
| Ingreso bruto acumulado |  |  |  |  |  |  | =H102+H22 |
| Impuesto federal sobre la renta retenido acumulado |  |  |  |  |  |  | 31000 |
| Seguro Social retenido acumulado |  |  |  |  |  |  | =H82+H85 |
| Medicare retenido acumulado |  |  |  |  |  |  | =H93+H94+H101 |
| Aplazamiento 401(k) antes de impuestos acumulado |  |  |  |  |  |  | 9000 |
| Muestra ilustrativa: empleado e importes ficticios |  |  |  |  |  |  |  |
| Este documento ha sido generado por Mercans |  |  |  |  |  |  |  |
| Cálculos de apoyo: no se imprimen con el recibo |  |  |  |  |  |  |  |
| Base de cálculo FICA (el menor entre el máximo anual restante o la tasa x base del período) |  |  |  |  |  |  |  |
| Base salarial del Seguro Social: 184,500 USD |  |  |  |  |  |  | 184500 |
| Tasa del Seguro Social, empleado: 6.2% |  |  |  |  |  |  | 0.062 |
| Salario sujeto al Seguro Social de este recibo (ingreso bruto menos la contribución del plan cafetería) |  |  |  |  |  |  | =H22-H27 |
| Salario sujeto al Seguro Social pagado antes de este recibo (acumulado, limitado a la base salarial) |  |  |  |  |  |  | 181500 |
| Seguro Social retenido antes de este recibo (acumulado) |  |  |  |  |  |  | =ROUND(H81*H79,2) |
| Máximo anual restante = tasa x base salarial menos lo retenido |  |  |  |  |  |  | =ROUND(H78*H79,2)-H82 |
| Tasa x salario sujeto de este recibo |  |  |  |  |  |  | =ROUND(H80*H79,2) |
| Seguro Social retenido = el menor de los dos importes anteriores |  |  |  |  |  |  | =MAX(0,MIN(H83,H84)) |
| Tasa del Seguro Social, empleador: 6.2% |  |  |  |  |  |  | 0.062 |
| Seguro Social del empleador pagado antes de este recibo (acumulado) |  |  |  |  |  |  | =ROUND(H81*H86,2) |
| Máximo anual restante del empleador = tasa x base salarial menos lo pagado |  |  |  |  |  |  | =ROUND(H78*H86,2)-H87 |
| Tasa del empleador x salario sujeto de este recibo |  |  |  |  |  |  | =ROUND(H80*H86,2) |
| Seguro Social del empleador = el menor de los dos importes anteriores |  |  |  |  |  |  | =MAX(0,MIN(H88,H89)) |
| Tasa Medicare, empleado: 1.45% |  |  |  |  |  |  | 0.0145 |
| Salario sujeto a Medicare pagado antes de este recibo (acumulado, sin base salarial) |  |  |  |  |  |  | 181500 |
| Medicare retenido antes de este recibo (acumulado) |  |  |  |  |  |  | =ROUND(H92*H91,2) |
| Medicare retenido = tasa x salario sujeto de este recibo |  |  |  |  |  |  | =ROUND(H80*H91,2) |
| Tasa Medicare, empleador: 1.45% |  |  |  |  |  |  | 0.0145 |
| Medicare del empleador = tasa x salario sujeto de este recibo |  |  |  |  |  |  | =ROUND(H80*H95,2) |
| Umbral del Medicare adicional: 200,000 USD |  |  |  |  |  |  | 200000 |
| Tasa del Medicare adicional: 0.9% |  |  |  |  |  |  | 0.009 |
| Salario Medicare acumulado incluyendo este recibo |  |  |  |  |  |  | =H92+H80 |
| Salario sobre el umbral, limitado a este recibo |  |  |  |  |  |  | =MAX(0,MIN(H80,H99-H97)) |
| Medicare adicional retenido = tasa x salario sobre el umbral |  |  |  |  |  |  | =ROUND(H100*H98,2) |
| Ingresos pagados antes de este recibo (acumulado) |  |  |  |  |  |  | 185000 |
| Base de cálculo del impuesto federal sobre la renta (método porcentual anual, tabla estándar) |  |  |  |  |  |  |  |
| Método: IRS Pub. 15-T (2026) Worksheet 1A with the Annual Percentage Method tables (STANDARD schedule; Step-2-checked schedule when W-4 Step 2 box checked) |  |  |  |  |  |  |  |
| Línea 1a: salario sujeto de este recibo (bruto menos 401(k) y plan cafetería) |  |  |  |  |  |  | =H22-H26-H27 |
| Línea 1b: períodos de pago por año |  |  |  |  |  |  | 26 |
| Línea 1c: salario anualizado = 1a x 1b |  |  |  |  |  |  | =H106*H107 |
| Línea 1g: casilla del Paso 2 sin marcar, soltero o casado por separado: 8,600 USD |  |  |  |  |  |  | 8600 |
| Línea 1i: salario anual ajustado = 1c menos 1g |  |  |  |  |  |  | =MAX(0,H108-H109) |
| Umbrales de la tabla estándar, soltero o casado por separado: 0/7500/19900/57900/113200/209275/263725/648100 |  |  |  |  |  |  |  |
| Tasas marginales de la tabla: 0/10/12/22/24/32/35/37 |  |  |  |  |  |  |  |
| Tramo 1: Impuesto del tramo = (salario ajustado - umbral) x aumento de la tasa |  |  |  |  | 0 | 0 | =MAX(0,H110-F113)*(G113-0) |
| Tramo 2: Impuesto del tramo = (salario ajustado - umbral) x aumento de la tasa |  |  |  |  | 7500 | 0.1 | =MAX(0,H110-F114)*(G114-G113) |
| Tramo 3: Impuesto del tramo = (salario ajustado - umbral) x aumento de la tasa |  |  |  |  | 19900 | 0.12 | =MAX(0,H110-F115)*(G115-G114) |
| Tramo 4: Impuesto del tramo = (salario ajustado - umbral) x aumento de la tasa |  |  |  |  | 57900 | 0.22 | =MAX(0,H110-F116)*(G116-G115) |
| Tramo 5: Impuesto del tramo = (salario ajustado - umbral) x aumento de la tasa |  |  |  |  | 113200 | 0.24 | =MAX(0,H110-F117)*(G117-G116) |
| Tramo 6: Impuesto del tramo = (salario ajustado - umbral) x aumento de la tasa |  |  |  |  | 209275 | 0.32 | =MAX(0,H110-F118)*(G118-G117) |
| Tramo 7: Impuesto del tramo = (salario ajustado - umbral) x aumento de la tasa |  |  |  |  | 263725 | 0.35 | =MAX(0,H110-F119)*(G119-G118) |
| Tramo 8: Impuesto del tramo = (salario ajustado - umbral) x aumento de la tasa |  |  |  |  | 648100 | 0.37 | =MAX(0,H110-F120)*(G120-G119) |
| Retención anual provisional |  |  |  |  |  |  | =SUM(H113:H120) |
| Retención provisional por período = anual / períodos, redondeada al centavo |  |  |  |  |  |  | =ROUND(H121/H107,2) |
| Créditos del Paso 3 por período (ninguno en esta muestra) |  |  |  |  |  |  | 0 |
| Retención adicional del Paso 4(c) por período (ninguna en esta muestra) |  |  |  |  |  |  | 0 |
| Impuesto federal retenido en este recibo |  |  |  |  |  |  | =MAX(0,H122-H123+H124) |

## Payslip Spec

|  | Header Details |  |  |  |
|---|---|---|---|---|
|  | Field Name (EN) | Field Name (Local) | HRP Mapping (TA & BA) | Field Explanation |
|  | Payslip Title | Título del recibo | Report Title in English: United States Payslip | Display title at the top of the payslip. Identifies the country and the document type. The English tab is the issued payslip; the Spanish tab carries the same fields with Spanish labels. |
|  | Company Logo | Logotipo de la empresa | Mercans corporate logo in the top banner | Mercans logo in the top banner. Part of the layout, not data. Keep the image anchored at cell A1 when the tab is copied. |
|  | Net Pay Summary Label | Etiqueta del pago neto | column calculated value 'Net Pay' | Label of the net pay box in the title band. The amount in the box repeats the Net Pay row of the Deductions section, so the two always agree. |
|  | Net Pay Summary Amount | Importe del pago neto | $payroll.net_pay | Gross earnings minus total deductions of the pay run, in USD with two decimals. Computed by the payroll calculation, never typed. Repeats the Net Pay row. |
|  | Work-location State | Estado del lugar de trabajo | $employment.work_state | Two-letter State code of the place of work. It selects the pay-statement rule set of that State (Field Option, block STATE_STATEMENT_RULE) and switches the optional blocks on or off. The rule set follows the work location, not the residence. Default: the pay-statement statute of the work-location state; no other state reach rule identified [US-MULTIS5-018] DD fields (US-DD-001 v1.0): Work State. |
|  | Pay Period | Período de pago | CONCAT(DATE_FORMAT($period.begin_date;'MM/DD/YYYY');' - ';DATE_FORMAT($period.end_date;'MM/DD/YYYY')) | First and last day of the pay period covered by the payslip, written MM/DD/YYYY. Taken from the payroll calendar of the pay run. Rows naming this element in Field Option, block STATE_STATEMENT_RULE: AK, CA, CO, DE, HI, ID, IL, IN, KS, ME, MI, MN, NC, ND, NH, NJ, NY, OH, OR, SC, WA. |
|  | Pay Date | Fecha de pago | $payroll.payment_date | Date the wages are paid to the employee. Taken from the payroll calendar. Rows naming this element in Field Option, block STATE_STATEMENT_RULE: DC, HI, IA, MD, NE, NM, OH, OR, RI, UT, VA, WA, WV. |
|  | Pay Frequency | Frecuencia de pago | $employment.pay_frequency | Weekly, biweekly, semimonthly or monthly. It sets the number of pay periods per year used by the federal income tax calculation basis. DD fields (US-DD-001 v1.0): Pay frequency. |
|  | Employer Fields |  |  |  |
|  | Field Name (EN) | Field Name (Local) | HRP Mapping (TA & BA) | Field Explanation |
|  | Employer Legal Name | Razón social del empleador | $legal_entity.name | Legal name of the paying entity as held in the company master data. Rows naming this element in Field Option, block STATE_STATEMENT_RULE: CA, CO, HI, MA, MD, NE, NM, OH, OR, VA. DD fields (US-DD-001 v1.0): Employer legal name. |
|  | Employer Address | Dirección del empleador | CONCAT($legal_entity_address.1.address_line_1;' ';$legal_entity_address.1.address_line_2;', ';$legal_entity_address.1.city;', ';$legal_entity_address.1.state;' ';$legal_entity_address.1.zip) | Full address of the paying entity. Merge the address cells so that a long address is never clipped. Rows naming this element in Field Option, block STATE_STATEMENT_RULE: CA, CO, HI, MD, NY, OR, VA. DD fields (US-DD-001 v1.0): Employer address delivery line; Employer address city; Employer address State; Employer address ZIP code. |
|  | Employer Phone | Teléfono del empleador | $legal_entity.contact_phone | Telephone number of the employer. Rows naming this element in Field Option, block STATE_STATEMENT_RULE: HI, MD, MN, NY, OR. DD fields (US-DD-001 v1.0): Employer contact phone number. |
|  | Employer Identification Number (EIN) | Número de identificación del empleador (EIN) | $legal_entity.ein; IF($employment.work_state='OR';$legal_entity.state_account_number;'') | Federal EIN of the legal entity; the State employer account number is printed where the State requires an employer registry or identification number. Rows naming this element in Field Option, block STATE_STATEMENT_RULE: OR. DD fields (US-DD-001 v1.0): Employer Identification Number (EIN); State employer account number. |
|  | Employee Fields |  |  |  |
|  | Field Name (EN) | Field Name (Local) | HRP Mapping (TA & BA) | Field Explanation |
|  | Employee Full Name | Nombre completo del empleado | CONCAT($person.first_name;' ';$person.middle_name;' ';$person.last_name) | Legal name of the employee as held in the HR master data. The DD carries the legal name; the payslip prints it as one string. Rows naming this element in Field Option, block STATE_STATEMENT_RULE: CA, CO, HI, MA, MD, MN, NY, OH, OR, TX, VA. DD fields (US-DD-001 v1.0): Employee legal first name; Employee middle name or initial; Employee legal last name. |
|  | Employee Home Address | Domicilio del empleado | CONCAT($person_address.1.address_line_1;', ';$person_address.1.city;', ';$person_address.1.state;' ';$person_address.1.zip) | Home address of the employee as held in the HR master data. Rows naming this element in Field Option, block STATE_STATEMENT_RULE: OH. DD fields (US-DD-001 v1.0): Employee home address delivery line; Employee home address city; Employee home address State; Employee home address ZIP code. |
|  | Employee ID | Número de empleado | $employment.employee_number | System-generated employee number of the payroll system. It is a system identifier, not a DD master-data field. It stands in for the Social Security number where a State accepts an employee ID, and it is the only identifier printed where the State bars every Social Security number digit. |
|  | Social Security Number (display) | Número de Seguro Social (presentación) | IF($employment.work_state='MD';'';CONCAT('***-**-';SUBSTRING($person.ssn;6;4))) | Rule: last four digits at most, never the full number. Maryland prints no Social Security number digits at all and identifies the employee by the Employee ID: No SSN at all on the wage check, any attachment, a direct-deposit notice or a card-credit notice (LE 3-502(d)); treat truncated SSN as barred too [US-MDS5-008] Rows naming an SSN display rule in Field Option, block SSN_DISPLAY_RULE: AK, CA, CO, HI, MD, MI, MO, NC, NE, NY, OK, PA, RI, SC, TX, VT. DD fields (US-DD-001 v1.0): Employee Social Security Number (SSN). |
|  | Job Title | Puesto | $employment.job_title | Job title of the employee as held in the HR master data. Optional field; leave blank where not held. DD fields (US-DD-001 v1.0): Job title. |
|  | Hire Date | Fecha de contratación | DATE_FORMAT($employment.start_date;'MM/DD/YYYY') | Date the employee first performed services. Used for the new-hire period of the sick-leave accrual and for service-based rules. DD fields (US-DD-001 v1.0): Date services first performed (hire date). |
|  | Rate-of-Pay Basis | Base de la tarifa de pago | $employment.rate_basis | Hourly, salary, piece rate or another basis. It decides whether hours are printed. Rows naming this element in Field Option, block STATE_STATEMENT_RULE: AK, CA, CT, DC, DE, HI, IA, IL, IN, MA, MD, ME, MI, MN, ND, NE, NJ, NM, NY, OH, OR, PA, RI, TX, VA, VT, WA, WI, WV. DD fields (US-DD-001 v1.0): Rate-of-pay basis. |
|  | Federal Filing Status (Form W-4) | Estado civil federal (Formulario W-4) | $tax_profile.w4_filing_status | Filing status from Step 1(c) of the employee's Form W-4. It selects the standard withholding table of the federal income tax calculation basis. DD fields (US-DD-001 v1.0): Form W-4 filing status (Step 1(c)). |
|  | Bank Name | Nombre del banco | $person_bank_account.bank_name | Name of the bank that receives the net pay, printed in the payment details block. Printed only for payment by direct deposit. No DD master-data field of US-DD-001 v1.0 holds it; the value is read from the payment instruction of the pay run. |
|  | Account (masked) | Cuenta (enmascarada) | CONCAT('****';SUBSTRING($person_bank_account.account_number;LENGTH($person_bank_account.account_number)-3;4)) | Bank account that receives the net pay, masked so that only the last four digits show. Never print the full account number. No DD master-data field of US-DD-001 v1.0 holds it; the value is read from the payment instruction of the pay run. |
|  | Payment Method | Forma de pago | $payroll.payment_method | How the net pay is delivered: direct deposit, check or pay card. Result of the pay run payment instruction, shown next to the amount paid in the payment details block. |
|  | Compensation Sources | Fuentes de compensación | $payroll.compensation_sources | Printed where the work-location State asks for a list of the compensation sources beyond base wages and tips. One line per source other than base wages and tips, taken from the earning wage types of the pay run. Rows naming this element in Field Option, block STATE_STATEMENT_RULE: DC. |
|  | Pay-Code Guide Reference | Referencia de la guía de códigos de pago | $legal_entity.pay_code_guide_url | Web address of the pay-code guide of the employer, printed on each record of hours where the State requires it. From 2026-10-01 (PA 26-12 sec. 38, 31-13a(c)): employers with 100+ employees publish a pay-code guide (overtime and common differentials, min 10 codes where applicable) in English, Spanish and other common languages; its Internet web site address appears on each record of hours and is given at hire; a payroll provider guide satisfies it [US-CTS5-028] |
|  | Compensatory Time | Tiempo compensatorio | $leave.comp_time.earned_or_paid | Compensatory time earned or paid in the period, printed where the State asks for it. Result of the leave module. Rows naming this element in Field Option, block STATE_STATEMENT_RULE: MI. |
|  | Employer Operating Name (if different) | Nombre comercial del empleador (si es distinto) | IF($legal_entity.operating_name<>$legal_entity.name;$legal_entity.operating_name;'') | Operating name of the employer, printed only when it differs from the legal name and the work-location State asks for it. No DD master-data field of US-DD-001 v1.0 holds it. Earnings statement at the end of each pay period, in writing or by electronic means. Under 181.032(b) it must include: (1) the name of the employee; (2) the rate or rates of pay and basis thereof, including whether the employee is paid by hour, shift, day, week, salary, piece, commission, or other method; (3) allowances, if any, claimed pursuant to permitted meals and lodging; (4) the total number of hours worked by the employee unless exempt from chapter 177; (5) the total amount of gross pay earned by the employee during that period; (6) a list of deductions made from the employee's pay; (7) any amount deducted by the employer under section 268B.14, subdivision 3, and the amount paid by the employer based on the employee's wages under section 268B.14, subdivision 1; (8) the net amount of pay after all deductions are made; (9) the date on which the pay period ends; (10) the legal name of the employer and the operating name of the employer if different from the legal name; (11) the physical address of the employer's main office or principal place of business, and a mailing address if different; and (12) the telephone number of the employer [US-MNP6-001] |
|  | Employer Mailing Address (if different) | Domicilio postal del empleador (si es distinto) | CONCAT($legal_entity_address.2.address_line_1;', ';$legal_entity_address.2.city;', ';$legal_entity_address.2.state;' ';$legal_entity_address.2.zip) | Mailing address of the employer, printed only when it differs from the physical address of the main office and the work-location State asks for it. US-DD-001 v1.0 holds the employer physical-address fields (see Employer Address) but no separate mailing-address field. Rows naming this element in Field Option, block STATE_STATEMENT_RULE: MN. |
|  | Paid Sick Leave Accrued | Licencia por enfermedad acumulada | $leave.paid_sick.entitlement | Hours of paid sick leave accrued under the applicable State or city rule. The balance fields print for the work-location States that require a balance on the statement. Leave entitlement is a result of the leave module, not a DD field. Rows naming a leave balance in Field Option, block LEAVE_BALANCE_RULE: AK, AZ, CA, MD, MN, NM, NV, WA, NYC. |
|  | Paid Sick Leave Used | Licencia por enfermedad usada | $leave.paid_sick.taken | Hours of paid sick leave used in the accrual year to date. Result of the leave module. Rows naming a leave balance in Field Option, block LEAVE_BALANCE_RULE: AK, AZ, CA, MD, MN, NM, NV, WA, NYC. |
|  | Paid Sick Leave Available | Licencia por enfermedad disponible | $leave.paid_sick.entitlement - $leave.paid_sick.taken | Balance = accrued minus used, a formula on the balance row only. Rows naming a leave balance in Field Option, block LEAVE_BALANCE_RULE: AK, AZ, CA, MD, MN, NM, NV, WA, NYC. |
|  | Paid Sick Leave Pay Received (year to date) | Pago recibido por licencia por enfermedad (acumulado) | $leave.paid_sick.pay_received_ytd | Amount of pay received as earned paid sick time in the year to date, in USD. Printed for the work-location State that asks for it (Arizona). Result of the payroll calculation of the sick-leave wage type. Every regular paycheck or attachment: earned paid sick time available, used to date in the year, and pay received as sick time (A.R.S. 23-375(C)) [US-AZS5-011] |
|  | PTO Accrued This Period | Tiempo libre pagado acumulado en el período | $leave.pto.accrued_period | Hours of protected time off accrued in the pay period, printed for employees whose work location is New York City. Result of the leave module. NYC Earned Safe and Sick Time (Protected Time Off): each pay period show PTO accrued in the period, paid and unpaid PTO used in the period, unpaid immediately available hours available in the calendar year, and accrued PTO available for use in the calendar year (pay statement or other written documentation) [US-NYB5-003] |
|  | Paid PTO Used This Period | Tiempo libre pagado usado en el período | $leave.pto.paid_used_period | Hours of paid protected time off used in the pay period, printed for New York City work locations. Result of the leave module. |
|  | Unpaid PTO Used This Period | Tiempo libre no pagado usado en el período | $leave.pto.unpaid_used_period | Hours of unpaid protected time off used in the pay period, printed for New York City work locations. Result of the leave module. |
|  | Unpaid PTO Available | Tiempo libre no pagado disponible | $leave.pto.unpaid_available | Hours of unpaid protected time off immediately available in the calendar year, printed for New York City work locations. Result of the leave module. |
|  | Earnings Fields |  |  |  |
|  | Field Name (EN) | Field Name (Local) | HRP Mapping (TA & BA) | Field Explanation |
|  | Regular Hours | Horas regulares | $payroll.hours.regular | Hours paid at the regular rate in the period; the Hours / units column of the basic-salary line. Hours worked are accumulated by the payroll calculation (wage type US-030). Rows naming this element in Field Option, block STATE_STATEMENT_RULE: AK, CA, CT, DC, DE, HI, IA, IL, IN, MA, MD, ME, MI, MN, ND, NE, NJ, NM, NY, OH, OR, PA, RI, TX, VA, VT, WA, WI, WV. |
|  | Total Hours Worked | Total de horas trabajadas | SUM($payroll.hours.*) | Total hours worked in the pay period: the sum of the hours of the time-based earning lines (hours worked accumulator, wage type US-030), a formula on the total row only. Not printed for salaried exempt employees where the State exempts them. Rows naming this element in Field Option, block STATE_STATEMENT_RULE: AK, CA, CT, DC, DE, HI, IA, IL, IN, MA, MD, ME, MI, MN, ND, NE, NJ, NM, NY, OH, OR, PA, RI, TX, VA, VT, WA, WI, WV. |
|  | Overtime Hours | Horas extra | $payroll.hours.overtime | Hours paid at the overtime rate. Straight-time and overtime pay print on separate lines. Rows naming this element in Field Option, block STATE_STATEMENT_RULE: AK, CT, HI, NE, NY, OR, WV. |
|  | Rate of Pay | Tarifa de pago | $employment.rate | Hourly or periodic rate of the line. Every rate prints with the hours it applies to. Rows naming this element in Field Option, block STATE_STATEMENT_RULE: AK, CA, CO, HI, IL, MA, MD, MN, ND, NJ, NY, OH, OR, PA, RI, TX, VA, VT, WA, WI, WV. DD fields (US-DD-001 v1.0): Rate-of-pay basis. |
|  | Piece-Rate Units and Rate | Unidades y tarifa por pieza | $payroll.piece.units | Number of piece-rate units and the rate per unit, printed for employees paid by the piece. Rows naming this element in Field Option, block STATE_STATEMENT_RULE: CA, HI, MN, NY, OR. |
|  | Allowances Credited toward Minimum Wage | Asignaciones acreditadas al salario mínimo | $payroll.mw_allowance | Amount of any allowance credited toward the minimum wage (for example a tip credit). Prints only where the State rule requires it. Rows naming this element in Field Option, block STATE_STATEMENT_RULE: AR, CO, HI, MN, NY, OR, PA. |
|  | Earnings Line | Línea de ingresos | $payroll.earning.[code] - $payroll.earning.[name] | One line per earning wage type of the pay run, printed as the wage type code, a dash and the wage type name, with rate, hours or units and amount. Earnings are shown only when not zero. |
|  | Tips and Gratuities Line | Línea de propinas y gratificaciones | $payroll.earning.cash_tips | Cash tips reported by the employee print on their own line where the State rule asks for gratuities on a separate line. Level of the tips and overtime deductions: assessment; withholding only via W-4 Step 4(b); employer reporting W-2 TP/TT/14b; FICA unchanged [US-FEDS5-030] Rows naming this element in Field Option, block STATE_STATEMENT_RULE: CO, DC. |
|  | Benefits Earned (employer-paid) | Beneficios devengados (pagados por el empleador) | $payroll.benefits_earned.total | Total value of the benefits earned in the period that the employer pays, printed with total wages where the State asks for wages and benefits earned. Result of the payroll calculation. Rows naming this element in Field Option, block STATE_STATEMENT_RULE: NM. |
|  | Gross Earnings | Ingreso bruto | SUM($payroll.earnings.*) | Sum of the earnings lines, a formula on the total row only. |
|  | Deductions Fields |  |  |  |
|  | Field Name (EN) | Field Name (Local) | HRP Mapping (TA & BA) | Field Explanation |
|  | Deduction Line | Línea de deducción | $payroll.deduction.[code] - $payroll.deduction.[name] | One line per deduction wage type of the pay run, with code, name and amount. Each deduction prints separately with its purpose. Rows naming this element in Field Option, block STATE_STATEMENT_RULE: AK, CA, CO, CT, DC, DE, FL, HI, IA, ID, IL, IN, KS, KY, MA, MD, ME, MI, MN, MO, MT, NC, ND, NE, NH, NJ, NM, NV, NY, OH, OK, OR, PA, RI, SC, TX, UT, VA, VT, WA, WI, WV, WY. |
|  | Pre-tax Deduction Lines | Líneas de deducción antes de impuestos | $payroll.deduction.pretax.* | Elective deferrals to a 401(k) and cafeteria-plan contributions print as deduction lines. Their effect on the federal income tax, social security and Medicare bases follows the Subject-to-tax flags of the wage type in US-WTC-001 v1.0. 401(k), 403(b) and 457(b) elective deferrals and SIMPLE salary-reduction contributions reduce federal income-tax withholding wages only (within the 402(g) / 457(b) limits); they remain FICA and FUTA wages. Section 125 cafeteria-plan salary reductions for a qualified benefit (accident and health premiums, health FSA, dependent care, HSA) take the treatment of that benefit outside the plan, so they reduce income-tax, FICA and FUTA wages within the benefit limits. [US-FEDS5-029] |
|  | Federal Income Tax Withholding | Retención del impuesto federal sobre la renta | $payroll.tax.fit | Federal income tax withheld by the percentage method of IRS Publication 15-T on the Form W-4 data. Calculation basis block below the payslip shows the lines of the worksheet. DD fields (US-DD-001 v1.0): Form W-4 filing status (Step 1(c)); Form W-4 multiple jobs or spouse works (Step 2); Form W-4 dependents and other credits (Step 3); Form W-4 other income (Step 4(a)); Form W-4 deductions (Step 4(b)); Form W-4 extra withholding (Step 4(c)); Form W-4 exempt from withholding. |
|  | Social Security Tax (lesser-of rule) | Seguro Social (regla del menor) | MIN($tax.oasdi.remaining_max;ROUND($tax.oasdi.rate*$tax.oasdi.period_base;2)) | Employee social security tax is the lesser of the remaining annual maximum tax and the rate times the period base; it is never an annualised amount divided by the number of periods. 6.2% [US-FEDS5-005] (effective 2026-01-01 to 2026-12-31) Wage base: 184,500 USD [US-FEDS5-005] (effective 2026-01-01 to 2026-12-31) DD fields (US-DD-001 v1.0): Nonresident alien flag; Totalization agreement FICA exemption. |
|  | Medicare Tax | Impuesto Medicare | ROUND($tax.medicare.rate*$tax.medicare.period_base;2) | Employee Medicare tax on the Medicare wages of the period, with no wage base. 1.45% [US-FEDS5-005] (effective 2026-01-01 to 2026-12-31) DD fields (US-DD-001 v1.0): Nonresident alien flag. |
|  | Additional Medicare Tax | Impuesto Medicare adicional | ROUND($tax.addl_medicare.rate*$tax.addl_medicare.excess;2) | Withheld on Medicare wages above the threshold; the excess is limited to the wages of this period. 0.9% [US-FEDS5-005] (effective 2026-01-01 to 2026-12-31) Threshold: 200,000 USD [US-FEDS5-005] (effective 2026-01-01 to 2026-12-31) DD fields (US-DD-001 v1.0): Nonresident alien flag. |
|  | State and Local Withholding Lines | Líneas de retención estatal y local | $payroll.tax.state.* / $payroll.tax.local.* | State income tax, State programme contributions (unemployment, disability, paid family and medical leave, long-term care) and local taxes print as separate employee deduction lines, selected by the work-location State and the locality fields of the DD. Where the State requires the amount deducted for its paid leave programme, that deduction prints on its own line (wage type US-185 for Minnesota). Rows naming this element in Field Option, block STATE_STATEMENT_RULE: MN. DD fields (US-DD-001 v1.0): Work State; Residence State; State withholding certificate on file; State withholding allowances or exemptions claimed. |
|  | Total Deductions | Total de deducciones | SUM($payroll.deductions.*) | Sum of the deduction lines, a formula on the total row only. |
|  | Net Pay | Pago neto | $payroll.gross - $payroll.total_deductions | Gross earnings minus total deductions, a formula on the total row only. Printed in the net pay row and in the title band. |
|  | Employer Contribution Lines | Líneas de aportación del empleador | $payroll.employer.* | Employer-side social security and Medicare print in the employer contribution block for information; they are not deducted from the employee's net pay. |
|  | Year-to-Date Figures | Acumulados del año | $payroll.ytd.* | Year-to-date gross, federal income tax, social security tax, Medicare tax and 401(k) deferral, carried by the year-to-date load of the wage types; they feed the annual wage statement. |

## Field Option

| Field Name | Option Value | Option Description | Usage Context |
|---|---|---|---|
| CURRENCY | USD | United States dollar | All amounts print in USD with two decimals. |
| PAYSLIP_LANGUAGE | EN | English: the issued payslip | Language of the payslip tab United States (EN). |
| PAYSLIP_LANGUAGE | ES | Spanish label set: documented seam | Labels only; amounts and pay element codes are identical to the English tab. |
| PAY_FREQUENCY | Weekly | Weekly pay | Pay periods per year come from the payroll calendar. |
| PAY_FREQUENCY | Biweekly | Every two weeks | Pay periods per year come from the payroll calendar. |
| PAY_FREQUENCY | Semimonthly | Twice a month | Pay periods per year come from the payroll calendar. |
| PAY_FREQUENCY | Monthly | Once a month | Pay periods per year come from the payroll calendar. |
| RATE_OF_PAY_BASIS | Hourly | Paid by the hour: hours and rate print | Decides which of hours, rate and piece units print. |
| RATE_OF_PAY_BASIS | Salary | Paid a fixed salary per period | Decides which of hours, rate and piece units print. |
| RATE_OF_PAY_BASIS | Piece rate | Paid by units produced: units and rate print | Decides which of hours, rate and piece units print. |
| RATE_OF_PAY_BASIS | Commission | Paid by commission | Decides which of hours, rate and piece units print. |
| RATE_OF_PAY_BASIS | Shift | Paid a rate per shift: shifts and rate print | Decides which of hours, rate and piece units print. |
| RATE_OF_PAY_BASIS | Day | Paid a rate per day: days and rate print | Decides which of hours, rate and piece units print. |
| RATE_OF_PAY_BASIS | Week | Paid a rate per week: weeks and rate print | Decides which of hours, rate and piece units print. |
| RATE_OF_PAY_BASIS | Other | Paid on another basis: the basis prints with the rate | Decides which of hours, rate and piece units print. |
| FEDERAL_BASELINE | required | False [US-FED-010] | Federal rule that sets the baseline of the payslip; State rules add content. |
| FEDERAL_BASELINE | official_federal | en: English designated by presidential action of 2025-03-01; no obligation on private employers [US-FED-020] | Federal rule that sets the baseline of the payslip; State rules add content. |
| FEDERAL_BASELINE | flsa | 3 years [US-FEDS5-021] | Federal rule that sets the baseline of the payslip; State rules add content. |
| FEDERAL_BASELINE | irs | 4 years [US-FEDS5-003] | Federal rule that sets the baseline of the payslip; State rules add content. |
| STATE_STATEMENT_RULE | AK | Alaska: Written or electronic, each pay period: rate; gross and net; pay-period dates; federal income tax and Federal Insurance Contribution Act deductions; Alaska Employment Security Act contributions; board/lodging deductions; advances; straight-time and overtime hours; other authorised deductions; sick leave used in accrual year; sick leave balance [US-AKS5-001] | Rule set switched on when the work-location State is AK. |
| STATE_STATEMENT_RULE | AL | Alabama: none: no state pay-statement content statute; federal records rules apply [US-ALP52-001] | Rule set switched on when the work-location State is AL. |
| STATE_STATEMENT_RULE | AR | Arkansas: none: no itemised pay-statement statute; tipped employees get the tip-credit amount per hour in writing each time it changes (11 CAR 11) [US-ARP52-006] | Rule set switched on when the work-location State is AR. |
| STATE_STATEMENT_RULE | AZ | Arizona: Statement (no content list) required only when paying by direct deposit or payroll card (A.R.S. 23-351(E),(F)) [US-AZS5-001] | Rule set switched on when the work-location State is AZ. |
| STATE_STATEMENT_RULE | CA | California: Lab. Code 226(a), semimonthly or each payment: gross; total hours (not for salaried exempt); piece units and rates; deductions; net; pay-period dates; name + last 4 SSN or employee ID; employer legal name and address; each hourly rate with hours [US-CAS5-005] | Rule set switched on when the work-location State is CA. |
| STATE_STATEMENT_RULE | CO | Colorado: C.R.S. 8-4-103(4), at least monthly or each payment: gross; all withholdings and deductions; net; pay-period dates; employee name or SSN; employer name and address. COMPS Rule 7 adds rate, tips, credits and time worked [US-COP51-005] [US-COP9L-001] | Rule set switched on when the work-location State is CO. |
| STATE_STATEMENT_RULE | CT | Connecticut: Each payment: hours worked; gross pay with straight time and overtime separate; itemised deductions; net (hours and split not for OT-exempt) [US-CTP51-005] | Rule set switched on when the work-location State is CT. |
| STATE_STATEMENT_RULE | DC | District of Columbia: Each payment (32-1008(b)): date of payment; gross; deductions and additions with gratuities on a separate line; net; hours worked; tip declaration split cash/card; from 2026-01-01 a list of compensation sources beyond base wages and tips [US-DCS5-010] | Rule set switched on when the work-location State is DC. |
| STATE_STATEMENT_RULE | DE | Delaware: Employers with more than 3 employees, each payment: wages due; pay period; total deductions each separately specified; total hours for hourly employees (19 Del. C. 1108) [US-DES5-002] | Rule set switched on when the work-location State is DE. |
| STATE_STATEMENT_RULE | FL | Florida: none for general employers; labor pools only (448.24(2)(g),(h)): itemised deductions each payment and annual earnings summary by 1 February [US-FLL-002] | Rule set switched on when the work-location State is FL. |
| STATE_STATEMENT_RULE | GA | Georgia: none: O.C.G.A. 34-7-2 has no statement duty; GDOL handbook has no pay-stub rule [US-GAP9L-001] [US-GAW1B-001] | Rule set switched on when the work-location State is GA. |
| STATE_STATEMENT_RULE | HI | Hawaii: HRS 387-6(c), 14 items: employee name; employer name; employer address and phone; total hours; regular and OT hours; straight-time pay; OT pay; other compensation incl. allowances toward minimum wage; gross; amount and purpose of each deduction; net; pay date; pay period; rates and basis incl. OT and piece rates with counts [US-HIP52-001] | Rule set switched on when the work-location State is HI. |
| STATE_STATEMENT_RULE | IA | Iowa: Each regular payday: hours worked, wages earned, deductions (91A.6(4)); itemised computation within 10 working days on request [US-IAP51-002] | Rule set switched on when the work-location State is IA. |
| STATE_STATEMENT_RULE | ID | Idaho: deductions_only: written statement of deductions for each pay period with deductions (45-609(2)) [US-IDP51-002] | Rule set switched on when the work-location State is ID. |
| STATE_STATEMENT_RULE | IL | Illinois: Pay stub each pay period with itemized deductions (820 ILCS 115/10 as amended by P.A. 103-953); payroll-card payees also get hours, rate and deductions [US-ILS5-024] | Rule set switched on when the work-location State is IL. |
| STATE_STATEMENT_RULE | IL | Illinois: Not configured in this release (open gap PSL-RQ-07) | Open item for this State's rule set. |
| STATE_STATEMENT_RULE | IN | Indiana: Each pay period at least hours worked, wages paid, deductions (IC 22-2-2-8(a)) [US-INP6-001] | Rule set switched on when the work-location State is IN. |
| STATE_STATEMENT_RULE | IN | Indiana: Duty binds employers subject to IC 22-2-2 = 2+ employees NOT subject to the FLSA minimum wage (IC 22-2-2-3); literal reading excludes FLSA-covered employers [US-INS5-001] | Rule set switched on when the work-location State is IN. |
| STATE_STATEMENT_RULE | IN | Indiana: Not configured in this release (open gap PSL-RQ-08) | Open item for this State's rule set. |
| STATE_STATEMENT_RULE | KS | Kansas: on_request: itemized statement of deductions on request for each pay period with deductions (K.S.A. 44-320(d)) [US-KSP52-001] | Rule set switched on when the work-location State is KS. |
| STATE_STATEMENT_RULE | KY | Kentucky: Employers with 10+ employees that make deductions: each payment, paper or electronic statement of each deduction and its purpose; electronic requires access to a computer and printer (section 337.070) [US-KYP8-001] | Rule set switched on when the work-location State is KY. |
| STATE_STATEMENT_RULE | LA | Louisiana: Not configured in this release (open gap PSL-RQ-10) | Rule set switched on when the work-location State is LA. |
| STATE_STATEMENT_RULE | MA | Massachusetts: Each payment (c.149 s.148): employer name; employee name; date; hours worked; hourly rate; deductions or increases for the period [US-MAP51-008] | Rule set switched on when the work-location State is MA. |
| STATE_STATEMENT_RULE | MD | Maryland: LE 3-504: employer name, address, phone; pay date and period; hours (unless exempt); rates; gross and net; each deduction by name and amount; other bases of pay; written or online [US-MDP51-005] | Rule set switched on when the work-location State is MD. |
| STATE_STATEMENT_RULE | ME | Maine: Each payment: date of the pay period, hours, total earnings, itemized deductions (Title 26 section 665, subsection 1) [US-MES5-006] | Rule set switched on when the work-location State is ME. |
| STATE_STATEMENT_RULE | MI | Michigan: At payment (MCL 408.479(2)): hours worked, gross, pay-period identification, separate itemisation of deductions; comp time earned or paid [US-MIS5-009] | Rule set switched on when the work-location State is MI. |
| STATE_STATEMENT_RULE | MN | Minnesota: Earnings statement at the end of each pay period, in writing or by electronic means. Under 181.032(b) it must include: (1) the name of the employee; (2) the rate or rates of pay and basis thereof, including whether the employee is paid by hour, shift, day, week, salary, piece, commission, or other method; (3) allowances, if any, claimed pursuant to permitted meals and lodging; (4) the total number of hours worked by the employee unless exempt from chapter 177; (5) the total amount of gross pay earned by the employee during that period; (6) a list of deductions made from the employee's pay; (7) any amount deducted by the employer under section 268B.14, subdivision 3, and the amount paid by the employer based on the employee's wages under section 268B.14, subdivision 1; (8) the net amount of pay after all deductions are made; (9) the date on which the pay period ends; (10) the legal name of the employer and the operating name of the employer if different from the legal name; (11) the physical address of the employer's main office or principal place of business, and a mailing address if different; and (12) the telephone number of the employer [US-MNP6-001] | Rule set switched on when the work-location State is MN. |
| STATE_STATEMENT_RULE | MO | Missouri: deductions_only: statement of total deductions at least monthly (290.080) [US-MOP52-002] | Rule set switched on when the work-location State is MO. |
| STATE_STATEMENT_RULE | MS | Mississippi: Not configured in this release (open gap PSL-RQ-14) | Rule set switched on when the work-location State is MS. |
| STATE_STATEMENT_RULE | MT | Montana: Every payment: itemized statement of state and federal income tax, social security and other deductions with amounts; statement saying none if nothing deducted (MCA 39-3-101) [US-MTP51-006] | Rule set switched on when the work-location State is MT. |
| STATE_STATEMENT_RULE | NC | North Carolina: deductions_only: itemized statement of deductions each pay period with deductions (G.S. 95-25.13), plus hire wage notice [US-NCW1B-003] [US-NCS5-006] | Rule set switched on when the work-location State is NC. |
| STATE_STATEMENT_RULE | ND | North Dakota: Each pay period a check stub or pay voucher: hours worked, rate, required state and federal deductions, authorized deductions (46-02-07-02, recordkeeping item 10) [US-NDS5-007] | Rule set switched on when the work-location State is ND. |
| STATE_STATEMENT_RULE | NE | Nebraska: Each regular payday: employer identity, hours paid, wages earned, deductions (48-1230(2)); hours not required for FLSA-exempt unless OT/hours-based [US-NEP51-004] | Rule set switched on when the work-location State is NE. |
| STATE_STATEMENT_RULE | NH | New Hampshire: deductions_only: statement of deductions each pay period with a deduction (RSA 275:49 IV); written monthly accounting for 275:48 I(d) deductions [US-NHP51-001] | Rule set switched on when the work-location State is NH. |
| STATE_STATEMENT_RULE | NJ | New Jersey: Statement of deductions each pay period with deductions; employers with 10+ employees add gross, net, rate and hours where relevant (34:11-4.6(c)) [US-NJP8-001] | Rule set switched on when the work-location State is NJ. |
| STATE_STATEMENT_RULE | NM | New Mexico: Written receipt each payday: employer identity; gross; hours worked; total wages and benefits earned; itemized deductions (50-4-2(B)) [US-NMP8-001] | Rule set switched on when the work-location State is NM. |
| STATE_STATEMENT_RULE | NV | Nevada: Itemized list of deductions at each payment (NRS 608.110(2)) [US-NVR3-001] | Rule set switched on when the work-location State is NV. |
| STATE_STATEMENT_RULE | NY | New York: Labor Law 195(3), every payment: dates of work; names; employer address and phone; rates and basis; gross; deductions; allowances toward minimum wage; net; non-exempt: regular and OT rates and hours; piece rates and counts [US-NYS5-006] | Rule set switched on when the work-location State is NY. |
| STATE_STATEMENT_RULE | NY | New York: Not configured in this release (open gap PSL-RQ-29) | Open item for this State's rule set. |
| STATE_STATEMENT_RULE | OH | Ohio: ORC 4113.14 (from 2025-04-09), each pay period written or electronic: employee name and address; employer name; gross and net; amount and purpose of each addition and deduction; pay date and period; hourly employees hours and rate [US-OHP51-001] | Rule set switched on when the work-location State is OH. |
| STATE_STATEMENT_RULE | OK | Oklahoma: deductions_only: brief itemized statement of all deductions with each payment (40 O.S. 165.2) [US-OKS5-003] | Rule set switched on when the work-location State is OK. |
| STATE_STATEMENT_RULE | OR | Oregon: ORS 652.610(1)(b): payment date; dates of work; employee name; employer name and registry/ID number; employer address and phone; rates; basis; gross; net; each deduction with amount and purpose; allowances toward minimum wage; non-exempt regular and OT rates, hours and pay; piece rates and counts [US-ORS5-026] | Rule set switched on when the work-location State is OR. |
| STATE_STATEMENT_RULE | PA | Pennsylvania: Every payment: hours worked, rates, gross, allowances toward minimum wage, deductions, net (34 Pa. Code 231.36) [US-PAP51-001] | Rule set switched on when the work-location State is PA. |
| STATE_STATEMENT_RULE | RI | Rhode Island: Every regular payday: hours worked (except 28-12-4.3 exempt), every deduction with explanation; commercial construction also regular hourly rate (28-14-2.1); electronic allowed, free printed copy on written request [US-RIP51-002] | Rule set switched on when the work-location State is RI. |
| STATE_STATEMENT_RULE | SC | South Carolina: Itemized statement of gross pay and deductions each pay period (41-10-30(C)); direct deposit: statement of earnings and withholdings (41-10-40(B)) [US-SCP52-006] | Rule set switched on when the work-location State is SC. |
| STATE_STATEMENT_RULE | SD | South Dakota: none: no SD statute requires a pay statement (Title 60 full-text scan) [US-SDS5-001] | Rule set switched on when the work-location State is SD. |
| STATE_STATEMENT_RULE | TN | Tennessee: none: no TN itemised pay-statement statute located; federal records rules [US-TNS5-001] | Rule set switched on when the work-location State is TN. |
| STATE_STATEMENT_RULE | TX | Texas: non_flsa_only: Labor Code 62.003 earnings statement (name, rate, gross, each deduction and purpose, net, hours or units; signed by employer or agent) applies only to employees not covered by the FLSA (62.151); best practice for everyone else [US-TXS5-003] | Rule set switched on when the work-location State is TX. |
| STATE_STATEMENT_RULE | TX | Texas: Not configured in this release (open gap PSL-RQ-28) | Open item for this State's rule set. |
| STATE_STATEMENT_RULE | UT | Utah: deductions_only: statement of each deduction on each regular payday (34-28-3(4)); construction-trade licensees full statement (34-28-3(5)) [US-UTP6-001] | Rule set switched on when the work-location State is UT. |
| STATE_STATEMENT_RULE | VA | Virginia: Each regular pay date, paystub or online accounting: employer name and address; hours (hourly and salaried below the FLSA level); rate; gross; amount and purpose of each deduction; enough detail to work out gross and net [US-VAS5-003] | Rule set switched on when the work-location State is VA. |
| STATE_STATEMENT_RULE | VT | Vermont: Detailed written statement with each weekly pay: gross, hours, hourly rate, itemised deductions incl. meals [US-VTP9-001] | Rule set switched on when the work-location State is VT. |
| STATE_STATEMENT_RULE | WA | Washington: Every payday, separate from the paycheck: hours or days worked, rates, gross, all deductions, pay period, payment date (WAC 296-126-040) [US-WAS5-004] | Rule set switched on when the work-location State is WA. |
| STATE_STATEMENT_RULE | WI | Wisconsin: Hours worked, rate, amount and reason for each deduction, on the check, envelope or accompanying paper; coding system allowed (103.457; DWD 272.10) [US-WIP52-001] | Rule set switched on when the work-location State is WI. |
| STATE_STATEMENT_RULE | WV | West Virginia: Scheduled payday itemized statement: hourly rate or salary; hours paid; OT rate; bonus or incentive pay; itemized deductions (42 CSR 5 s.7.3, sunset 2029-07-01) [US-WVS5-008] (effective 2019-07-01 to 2029-07-01) | Rule set switched on when the work-location State is WV. |
| STATE_STATEMENT_RULE | WY | Wyoming: deductions_only: detachable part of the check or attached slip with an itemized statement of all deductions (27-4-101(b)); agricultural operations exempt [US-WYP51-005] | Rule set switched on when the work-location State is WY. |
| LEAVE_BALANCE_RULE | AK | Sick leave used in the accrual year and sick leave balance on every statement (since 2025-09-25); a combined PTO plan satisfies it by showing PTO used and balance [US-AKS5-001] | Print the paid leave balance block of the payslip for this work location. |
| LEAVE_BALANCE_RULE | AZ | Every regular paycheck or attachment: earned paid sick time available, used to date in the year, and pay received as sick time (A.R.S. 23-375(C)) [US-AZS5-011] | Print the paid leave balance block of the payslip for this work location. |
| LEAVE_BALANCE_RULE | CA | Available paid sick leave on the wage statement or a separate writing each payday [US-CAS5-011] | Print the paid leave balance block of the payslip for this work location. |
| LEAVE_BALANCE_RULE | MD | Available earned sick and safe leave balance each time wages are paid; an online balance system satisfies it (LE 3-1305(f)) [US-MDS5-013] | Print the paid leave balance block of the payslip for this work location. |
| LEAVE_BALANCE_RULE | MN | ESST hours available and used each pay period, on or attached to the statement or via an electronic system [US-MNS5-011] | Print the paid leave balance block of the payslip for this work location. |
| LEAVE_BALANCE_RULE | NM | Year-to-date earned sick leave accrued and used, at least quarterly, on the earnings statement or electronically [US-NMS5-002] | Print the paid leave balance block of the payslip for this work location. |
| LEAVE_BALANCE_RULE | NV | Accounting of available paid-leave hours on every payday, employers with 50+ NV employees (608.0197(1)(h)) [US-NVS5-001] | Print the paid leave balance block of the payslip for this work location. |
| LEAVE_BALANCE_RULE | WA | At least monthly: paid sick leave accrued, used and available; may be on the regular pay statement (WAC 296-128-755(2)) [US-WAS5-005] | Print the paid leave balance block of the payslip for this work location. |
| LEAVE_BALANCE_RULE | NYC | NYC Earned Safe and Sick Time (Protected Time Off): each pay period show PTO accrued in the period, paid and unpaid PTO used in the period, unpaid immediately available hours available in the calendar year, and accrued PTO available for use in the calendar year (pay statement or other written documentation) [US-NYB5-003] | Print the paid leave balance block of the payslip for this work location. |
| SSN_DISPLAY_RULE | AK | SSN may not be printed on mailed material unless authorised by law (AS 45.48.400-.480); 8 AAC 15.160(h) does not require it: omit or truncate [US-AKS5-016] [US-AKL-001] | Governs the Social Security number display on pay documents and the annual statement. |
| SSN_DISPLAY_RULE | CA | Only the last 4 SSN digits or an employee ID (226(a)(7)) [US-CAS5-005] | Governs the Social Security number display on pay documents and the annual statement. |
| SSN_DISPLAY_RULE | CO | SSN may appear instead of the name (8-4-103(4)(e)); no truncation rule in the Wage Act [US-COP51-005] | Governs the Social Security number display on pay documents and the annual statement. |
| SSN_DISPLAY_RULE | HI | Not required on the statement; section 487J-2 bars making an entire SSN available to the general public and printing an entire SSN on mailed materials, except employer-to-employee communications or where the individual requests it [US-HIS5-028] | Governs the Social Security number display on pay documents and the annual statement. |
| SSN_DISPLAY_RULE | MD | No SSN at all on the wage check, any attachment, a direct-deposit notice or a card-credit notice (LE 3-502(d)); treat truncated SSN as barred too [US-MDS5-008] | Governs the Social Security number display on pay documents and the annual statement. |
| SSN_DISPLAY_RULE | MI | No more than 4 sequential SSN digits displayed (SSN Privacy Act, MCL 445.83/.84); employer must publish an SSN privacy policy [US-MIS5-013] | Governs the Social Security number display on pay documents and the annual statement. |
| SSN_DISPLAY_RULE | MO | No public display; SSN or its last four digits may not be required as an employee number (407.1355); no explicit pay-statement rule [US-MOS5-016] | Governs the Social Security number display on pay documents and the annual statement. |
| SSN_DISPLAY_RULE | NC | G.S. 75-62: no SSN on mailed material unless law requires [US-NCS5-016] | Governs the Social Security number display on pay documents and the annual statement. |
| SSN_DISPLAY_RULE | NE | No more than the last 4 SSN digits displayed publicly or to coworkers (48-237) [US-NES5-013] | Governs the Social Security number display on pay documents and the annual statement. |
| SSN_DISPLAY_RULE | NY | Labor Law 203-d: no public display, no SSN on badges or time cards; not a required statement field [US-NYS5-009] | Governs the Social Security number display on pay documents and the annual statement. |
| SSN_DISPLAY_RULE | OK | No SSN on materials mailed to the employee unless law requires (40 O.S. 173.1); mask on mailed payslips [US-OKS5-008] | Governs the Social Security number display on pay documents and the annual statement. |
| SSN_DISPLAY_RULE | PA | Act 60 of 2006: no SSN on mailed materials unless law requires; mailed stubs omit the SSN [US-PAS5-020] | Governs the Social Security number display on pay documents and the annual statement. |
| SSN_DISPLAY_RULE | RI | No part of the SSN on material mailed to the individual unless law requires (6-48-8) [US-RIS5-020] | Governs the Social Security number display on pay documents and the annual statement. |
| SSN_DISPLAY_RULE | SC | No 6 or more SSN digits on mailed material or public display (37-20-180): mailed statements show 5 digits at most [US-SCS5-009] | Governs the Social Security number display on pay documents and the annual statement. |
| SSN_DISPLAY_RULE | TX | Bus. & Com. Code 501.001(a)(5): no SSN printed on any material sent by mail unless state or federal law requires it [US-TXS5-013] | Governs the Social Security number display on pay documents and the annual statement. |
| SSN_DISPLAY_RULE | VT | No full SSN on mailed materials (9 V.S.A. 2440); redacted SSN permitted [US-VTS5-015] | Governs the Social Security number display on pay documents and the annual statement. |
| SSN_DISPLAY_RULE | W2 | SSN may be truncated (first five digits masked, last four shown, e.g. ***-**-1234) on employee W-2 copies only; never on Copy A; EIN never truncated [US-FEDS5-022] | Governs the Social Security number display on pay documents and the annual statement. |
| SSN_DISPLAY_RULE | UNREAD | Not configured in this release (open gap PSL-RQ-26) | Jurisdictions whose SSN display statute is not yet read: apply the default: last four digits at most. |
| ELECTRONIC_DELIVERY_RULE | AK | Written or electronic; no separate consent rule [US-AKS5-001] | Electronic delivery condition of the work-location State. |
| ELECTRONIC_DELIVERY_RULE | CT | Electronic only with the employee explicit consent, a secure private way to access and print, and confidentiality safeguards (31-13a(b)) [US-CTS5-027] | Electronic delivery condition of the work-location State. |
| ELECTRONIC_DELIVERY_RULE | DE | On the check, a separate slip, or electronically if the employee can retain it; employee may ask for paper [US-DES5-002] | Electronic delivery condition of the work-location State. |
| ELECTRONIC_DELIVERY_RULE | HI | Electronic with the employee written authorization; direct deposit still requires a statement [US-HIS5-007] | Electronic delivery condition of the work-location State. |
| ELECTRONIC_DELIVERY_RULE | IA | Mail, secure electronic means, at the workplace, or access to view; no separate consent [US-IAP51-002] | Electronic delivery condition of the work-location State. |
| ELECTRONIC_DELIVERY_RULE | ME | Electronic allowed only with ready access and printing at no cost; same record due when a direct deposit is made [US-MES5-006] | Electronic delivery condition of the work-location State. |
| ELECTRONIC_DELIVERY_RULE | MN | Electronic requires access to an employer computer during work hours and statements kept available 3 years [US-MNP6-001] | Electronic delivery condition of the work-location State. |
| ELECTRONIC_DELIVERY_RULE | NC | In writing, printable e-mail or any means the employee can keep; no separate consent [US-NCS5-024] | Electronic delivery condition of the work-location State. |
| ELECTRONIC_DELIVERY_RULE | NJ | Electronic allowed unless the employee asks for paper [US-NJP8-001] | Electronic delivery condition of the work-location State. |
| ELECTRONIC_DELIVERY_RULE | OR | Electronic only with the employee express agreement and ability to print or store on receipt (652.610(1)(c)) [US-ORS5-026] | Electronic delivery condition of the work-location State. |
| ELECTRONIC_DELIVERY_RULE | WA | Electronic if the employee can receive and copy it on payday; otherwise paper [US-WAS5-004] | Electronic delivery condition of the work-location State. |
| ELECTRONIC_DELIVERY_RULE | CA | Not configured in this release (open gap PSL-RQ-02) | Electronic delivery condition of the work-location State is not yet configured. |
| ELECTRONIC_DELIVERY_RULE | CO | Not configured in this release (open gap PSL-RQ-03) | Electronic delivery condition of the work-location State is not yet configured. |
| ELECTRONIC_DELIVERY_RULE | MA | Not configured in this release (open gap PSL-RQ-11) | Electronic delivery condition of the work-location State is not yet configured. |
| ELECTRONIC_DELIVERY_RULE | NY | Not configured in this release (open gap PSL-RQ-23) | Electronic delivery condition of the work-location State is not yet configured. |
| ELECTRONIC_DELIVERY_RULE | NV | Not configured in this release (open gap PSL-RQ-22) | Electronic delivery condition of the work-location State is not yet configured. |
| ELECTRONIC_DELIVERY_RULE | DEFAULT | Electronic delivery with an opt-in consent record and free print or download access | Default that meets the strictest rules listed in this block. |
| RETENTION_PERIOD | AR | records withholding retention: 6 years [US-ARP51-002] | Minimum keeping period of the record named. |
| RETENTION_PERIOD | AZ | records payroll retention: 4 years [US-AZS5-006] | Minimum keeping period of the record named. |
| RETENTION_PERIOD | CT | records retention: 3 years [US-CTS5-027] | Minimum keeping period of the record named. |
| RETENTION_PERIOD | DC | records retention: 3 years [US-DCS5-010] | Minimum keeping period of the record named. |
| RETENTION_PERIOD | FED | records flsa retention: 3 years [US-FEDS5-021] | Minimum keeping period of the record named. |
| RETENTION_PERIOD | FED | records irs retention: 4 years [US-FEDS5-003] | Minimum keeping period of the record named. |
| RETENTION_PERIOD | GA | records gdol retention: 7 years [US-GAS5-005] | Minimum keeping period of the record named. |
| RETENTION_PERIOD | IL | records paystub retention: 3 years [US-ILS5-024] | Minimum keeping period of the record named. |
| RETENTION_PERIOD | KS | records retention: 3 years [US-KSS5-011] | Minimum keeping period of the record named. |
| RETENTION_PERIOD | MA | records retention: 3 years [US-MAS5-005] | Minimum keeping period of the record named. |
| RETENTION_PERIOD | ME | records retention: 3 years [US-MES5-006] | Minimum keeping period of the record named. |
| RETENTION_PERIOD | MI | records retention: 3 years [US-MIS5-009] | Minimum keeping period of the record named. |
| RETENTION_PERIOD | MN | records retention: 3 years [US-MNS5-020] | Minimum keeping period of the record named. |
| RETENTION_PERIOD | MO | records retention: 3 years [US-MOB5-402] | Minimum keeping period of the record named. |
| RETENTION_PERIOD | MS | records retention: 3 years [US-MSS5-019] | Minimum keeping period of the record named. |
| RETENTION_PERIOD | MT | records payroll tax retention: 5 years [US-MTS5-005] | Minimum keeping period of the record named. |
| RETENTION_PERIOD | NH | records retention: 3 years [US-NHS5-003] | Minimum keeping period of the record named. |
| RETENTION_PERIOD | NJ | records wage hour retention: 6 years [US-NJS5-022] | Minimum keeping period of the record named. |
| RETENTION_PERIOD | NV | records retention: 2 years [US-NVS5-001] | Minimum keeping period of the record named. |
| RETENTION_PERIOD | OH | records wage hour retention: 3 years [US-OHS5-005] (effective 2026-01-01 to 2027-12-31) | Minimum keeping period of the record named. |
| RETENTION_PERIOD | OK | records payroll tax retention: 4 years [US-OKS5-014] | Minimum keeping period of the record named. |
| RETENTION_PERIOD | OR | records retention: 2 years [US-ORS5-019] | Minimum keeping period of the record named. |
| RETENTION_PERIOD | AK | retention wage hour: 3 years [US-AKS5-001] | Minimum keeping period of the record named. |
| RETENTION_PERIOD | CA | retention wage statements: 3 years [US-CAS5-005] | Minimum keeping period of the record named. |
| RETENTION_PERIOD | DE | retention wage records: 3 years [US-DES5-001] | Minimum keeping period of the record named. |
| RETENTION_PERIOD | IA | retention payroll records: 3 years [US-IAP51-002] | Minimum keeping period of the record named. |
| RETENTION_PERIOD | ID | retention employment records: 3 years [US-IDS5-006] | Minimum keeping period of the record named. |
| RETENTION_PERIOD | KY | retention pay records: 1 years [US-KYP8-002] | Minimum keeping period of the record named. |
| RETENTION_PERIOD | NC | retention withholding records: 10 years [US-NC-001] | Minimum keeping period of the record named. |
| RETENTION_PERIOD | NY | retention payroll records: 6 years [US-NYS5-006] | Minimum keeping period of the record named. |
| RETENTION_PERIOD | VA | retention pay statements: 3 years [US-VAS5-003] | Minimum keeping period of the record named. |
| RETENTION_PERIOD | SC | records wage retention: 3 years [US-SCP52-006] | Minimum keeping period of the record named. |
| RETENTION_PERIOD | WA | records esd retention: 4 years [US-WAS5-030] | Minimum keeping period of the record named. |
| RETENTION_PERIOD | WI | records retention: 3 years [US-WIS5-002] | Minimum keeping period of the record named. |
| RETENTION_PERIOD | WV | records retention: 5 years [US-WVS5-008] (effective 2019-07-01 to 2029-07-01) | Minimum keeping period of the record named. |
| RETENTION_PERIOD | WY | records retention: 2 years [US-WYS5-001] | Minimum keeping period of the record named. |
| RETENTION_PERIOD | RI | Not configured in this release (open gap PSL-RQ-24) | Keeping period is not yet configured. |
| RETENTION_PERIOD | DEFAULT | Archive every payslip for the longest keeping period among the rules listed in this block | Default: one archive period that satisfies every listed rule. |
| W2_FEED_ITEM | new_codes_2026 | TP (cash tips), TT (qualified overtime), TA (Trump-account employer contributions) [US-FEDS5-007] | Item the payslip and year-to-date figures must feed on the annual wage statement. |
| W2_FEED_ITEM | tipped_occupation_code | Box 14 split into 14a Other and 14b Treasury Tipped Occupation Code(s) from TY2026 [US-FEDS5-007] | Item the payslip and year-to-date figures must feed on the annual wage statement. |
| W2_FEED_ITEM | vt_child_care_contribution | VT CCC employee share (max 0.11% of wages, of the 0.44% total) reported in W-2 Box 14 [US-VTS5-030] | Item the payslip and year-to-date figures must feed on the annual wage statement. |
| W2_FEED_ITEM | w2_box14_label | MEPFML [US-MES5-025] | Item the payslip and year-to-date figures must feed on the annual wage statement. |
| W2_FEED_ITEM | ca_sdi | CASDI (or VPDI) in Box 14; CA PIT wages Box 16; CA PIT withheld Box 17 [US-CAS5-018] (effective 2026-01-01 to 2026-12-31) | Item the payslip and year-to-date figures must feed on the annual wage statement. |
| W2_FEED_ITEM | boxes_15_20 | Up to two states and two localities per W-2; more requires a second W-2 repeating boxes a-f, never duplicating federal data on Copy A; W-3 box 15 = X when more than one state [US-MULTIS5-011] | Item the payslip and year-to-date figures must feed on the annual wage statement. |
| W2_FEED_ITEM | level | assessment; withholding only via W-4 Step 4(b); employer reporting W-2 TP/TT/14b; FICA unchanged [US-FEDS5-030] | Item the payslip and year-to-date figures must feed on the annual wage statement. |
| MULTISTATE_REACH | ca | Lab. Code 226 applies when the principal place of work is CA (majority of working time); if no majority state, when CA is the base of work operations and some work is done in CA (Ward v. United Airlines, S248702, 2020-06-29; level: pay-statement content) [US-MULTIS5-018] | Which State's pay-statement rule applies to the employee. |
| MULTISTATE_REACH | default | Default: the pay-statement statute of the work-location state; no other state reach rule identified [US-MULTIS5-018] | Which State's pay-statement rule applies to the employee. |
| MULTISTATE_REACH | reach | Employees employed in Iowa (work location, not residence) (91A.2(3),(4)) [US-IAS5-027] | Which State's pay-statement rule applies to the employee. |
| COMPANION_DOCUMENT | OR | From 2026-01-01 (SB 906): written explanation of earnings and deductions incl. all payroll codes at hire, updated by 1 January each year [US-ORS5-022] | Document that accompanies the payslip in this State. |
| COMPANION_DOCUMENT | CT | From 2026-10-01 (PA 26-12 sec. 38, 31-13a(c)): employers with 100+ employees publish a pay-code guide (overtime and common differentials, min 10 codes where applicable) in English, Spanish and other common languages; its Internet web site address appears on each record of hours and is given at hire; a payroll provider guide satisfies it [US-CTS5-028] | Document that accompanies the payslip in this State. |
| NOTICE_LANGUAGE | AZ | Minimum-wage and earned-paid-sick-time posters/notice in English and Spanish (A.R.S. 23-375(B)) [US-AZL-001] | Language rule of a notice or poster that is not the payslip itself. |
| NOTICE_LANGUAGE | CA | Hire notice (Lab. Code 2810.5) in the language the employer normally uses [US-CAP6-001] | Language rule of a notice or poster that is not the payslip itself. |
| NOTICE_LANGUAGE | CO_COMPS | COMPS Order Rule 7.4.3: Spanish COMPS Order/poster where employees with limited English language ability speak Spanish, or a Division version in another language [US-COP9L-001] | Language rule of a notice or poster that is not the payslip itself. |
| NOTICE_LANGUAGE | CO_PAID_LEAVE | C.R.S. 8-13.3-408(2): notice in English and the first language of 5%+ of the workforce [US-COL-001] | Language rule of a notice or poster that is not the payslip itself. |
| NOTICE_LANGUAGE | CT | C.G.S. 31-57w(b) paid sick leave poster in English and Spanish [US-CTL-001] | Language rule of a notice or poster that is not the payslip itself. |
| NOTICE_LANGUAGE | DC | Hire/change notice (32-1008(c)) in English and also the primary language where the Mayor has a template [US-DCS5-010] | Language rule of a notice or poster that is not the payslip itself. |
| NOTICE_LANGUAGE | DE | 19 Del. C. 3710(c) paid-leave notice in English, Spanish and any first language of 5%+ of the workforce [US-DEL-001] | Language rule of a notice or poster that is not the payslip itself. |
| NOTICE_LANGUAGE | FL | Fla. Stat. 448.109(3)(a) minimum-wage poster in English and Spanish [US-FLL-001] | Language rule of a notice or poster that is not the payslip itself. |
| NOTICE_LANGUAGE | MA | M.G.L. c.149 s.148C(o) earned sick time notice languages [US-MAL-002] | Language rule of a notice or poster that is not the payslip itself. |
| NOTICE_LANGUAGE | MI | ESTA notice/poster in English, Spanish and any language that is the first language of 10%+ of the workforce if the Department has translated it [US-MIL-001] [US-MIP9L-001] | Language rule of a notice or poster that is not the payslip itself. |
| NOTICE_LANGUAGE | MN | Hire notice (181.032) in English; other language on request [US-MNP6-001] | Language rule of a notice or poster that is not the payslip itself. |
| NOTICE_LANGUAGE | NJ_GENDER_EQUITY | N.J.S.A. 34:11-56.12(c): employers with 50+ employees post and provide in English, Spanish and Commissioner-available first languages; deliverable as a pay-check insert [US-NJP9M-001] | Language rule of a notice or poster that is not the payslip itself. |
| NOTICE_LANGUAGE | NJ_SICK_LEAVE | NJ earned sick leave notice in the languages published by NJDOL [US-FEDR3-010] | Language rule of a notice or poster that is not the payslip itself. |
| NOTICE_LANGUAGE | NY | Hire notice (Labor Law 195(1)(a)) in English and the employee primary language [US-NYP51-003] | Language rule of a notice or poster that is not the payslip itself. |
| NOTICE_LANGUAGE | OR | ORS 652.610(6): BOLI template in English and Spanish for the new-hire earnings/deductions explanation [US-ORL-001] [US-OR-002] | Language rule of a notice or poster that is not the payslip itself. |
| NOTICE_LANGUAGE | TX_WORKPLACE_VIOLENCE | Workplace-violence reporting notice in English and Spanish, every employer with 1+ employees since 2024-01-08 (HB 915; 40 TAC 800.600) [US-TXP9M-001] | Language rule of a notice or poster that is not the payslip itself. |
| NOTICE_LANGUAGE | VT_PAYCARD | 21 V.S.A. 342(f) payroll-card disclosures in the primary language [US-VTL-001] | Language rule of a notice or poster that is not the payslip itself. |
| STATE_RULE_DETAIL | VT | 0.11% [US-VTS5-030] | Further rule of the jurisdiction that bears on the payslip. |
| STATE_RULE_DETAIL | CA | Section 226 does not apply to any employer of a person employed by the owner or occupant of a residential dwelling whose duties are incidental to the ownership, maintenance, or use of the dwelling, including the care and supervision of children, or whose duties are personal and not in the course of the trade, business, profession, or occupation of the owner or occupant [US-CAS5-005] | Further rule of the jurisdiction that bears on the payslip. |
| STATE_RULE_DETAIL | CA | 4,000 USD [US-CAS5-005] | Further rule of the jurisdiction that bears on the payslip. |
| STATE_RULE_DETAIL | CO | Statement shows total pay, rate, tips, credits and time worked; kept 3 years [US-COS5-001] (effective 2026-01-01 to 2026-12-31) | Further rule of the jurisdiction that bears on the payslip. |
| STATE_RULE_DETAIL | CT | 100 employees [US-CTS5-028] | Further rule of the jurisdiction that bears on the payslip. |
| STATE_RULE_DETAIL | DE | more than 3 employees [US-DES5-002] | Further rule of the jurisdiction that bears on the payslip. |
| STATE_RULE_DETAIL | IL | Stubs kept 3 years; copies within 21 days on request (max twice per 12 months; former employees for one year); if electronic stubs become inaccessible after separation, offer prior-year stubs by the final pay period and record the offer [US-ILS5-024] | Further rule of the jurisdiction that bears on the payslip. |
| STATE_RULE_DETAIL | KY | 10 employees [US-KYP8-001] | Further rule of the jurisdiction that bears on the payslip. |
| STATE_RULE_DETAIL | MD | Tip Credit Wage Statement for restaurants [US-MDS5-007] | Further rule of the jurisdiction that bears on the payslip. |
| STATE_RULE_DETAIL | NJ | 10 employees [US-NJP8-001] | Further rule of the jurisdiction that bears on the payslip. |
| STATE_RULE_DETAIL | NV | 50 employees [US-NVS5-001] | Further rule of the jurisdiction that bears on the payslip. |
| STATE_RULE_DETAIL | UT | All lawful offsets itemized on a statement or detachable check stub (R610-3-20) [US-UTS5-012] | Further rule of the jurisdiction that bears on the payslip. |
| STATE_RULE_DETAIL | SC | Section 41-10-30 (notification to employees) does not apply to domestic labour in private homes or to employers with fewer than five employees at all times in the preceding twelve months (41-10-20) [US-SCP52-006] | Further rule of the jurisdiction that bears on the payslip. |
| PAYSLIP_LINE | 21100 | Basic salary deduction | Employee deductions: prints as '21100 - Basic salary deduction' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 21110 | Overtime deduction - type 1 | Employee deductions: prints as '21110 - Overtime deduction - type 1' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 21140 | Salary addition deduction - type 1 | Employee deductions: prints as '21140 - Salary addition deduction - type 1' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 21150 | Premium pay (i.e. Shift premium) deduction - type 1 | Employee deductions: prints as '21150 - Premium pay (i.e. Shift premium) deduction - type 1' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 21190 | Long Term Disability deduction | Employee deductions: prints as '21190 - Long Term Disability deduction' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 21400 | Housing allowance deduction | Employee deductions: prints as '21400 - Housing allowance deduction' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 21520 | Transportation allowance deduction | Employee deductions: prints as '21520 - Transportation allowance deduction' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 21610 | Health insurance & Life insurance contributions - type 1 | Employee deductions: prints as '21610 - Health insurance & Life insurance contributions - type 1' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 21611 | Health insurance & Life insurance contributions - type 2 | Employee deductions: prints as '21611 - Health insurance & Life insurance contributions - type 2' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 21640 | Pre-tax 401(k) elective deferral - employee deduction | Employee deductions: prints as '21640 - Pre-tax 401(k) elective deferral - employee deduction' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 21641 | Pre-tax 403(b) salary reduction - employee deduction | Employee deductions: prints as '21641 - Pre-tax 403(b) salary reduction - employee deduction' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 21642 | Pre-tax 457(b) salary reduction - employee deduction | Employee deductions: prints as '21642 - Pre-tax 457(b) salary reduction - employee deduction' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 21645 | Pre-tax SIMPLE plan salary reduction - employee deduction | Employee deductions: prints as '21645 - Pre-tax SIMPLE plan salary reduction - employee deduction' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 21670 | Benefits plan 1 deduction - type 1 | Employee deductions: prints as '21670 - Benefits plan 1 deduction - type 1' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 21800 | Expense reimbursement deduction | Employee deductions: prints as '21800 - Expense reimbursement deduction' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 21810 | Parking deduction | Employee deductions: prints as '21810 - Parking deduction' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 21820 | Donation deduction | Employee deductions: prints as '21820 - Donation deduction' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 21890 | Stock options and grants deduction | Employee deductions: prints as '21890 - Stock options and grants deduction' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 21900 | Social security tax (OASDI) - employee | Employee deductions: prints as '21900 - Social security tax (OASDI) - employee' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 23640 | Pensions & Pension Contributions (employer, no-recon) | Employer contributions: prints as '23640 - Pensions & Pension Contributions (employer, no-recon)' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 23670 | Benefits plan 1 deduction - type 1 | Employer contributions: prints as '23670 - Benefits plan 1 deduction - type 1' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 23671 | Company contribution liability - type 1 | Employer contributions: prints as '23671 - Company contribution liability - type 1' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 62100 | Basic salary | Earnings: prints as '62100 - Basic salary' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 62104 | Basic salary rate (rate of pay) | Earnings: prints as '62104 - Basic salary rate (rate of pay)' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 62110 | Overtime - type 1 | Earnings: prints as '62110 - Overtime - type 1' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 62140 | Salary addition - type 1 | Earnings: prints as '62140 - Salary addition - type 1' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 62150 | Premium pay (i.e. Shift premium) - type 1 | Earnings: prints as '62150 - Premium pay (i.e. Shift premium) - type 1' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 62160 | Holiday Allowance | Earnings: prints as '62160 - Holiday Allowance' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 62170 | On-call duty | Earnings: prints as '62170 - On-call duty' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 62180 | Severance & Seniority - type 1 | Earnings: prints as '62180 - Severance & Seniority - type 1' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 62190 | Long Term Disability | Earnings: prints as '62190 - Long Term Disability' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 62200 | Bonus (annual, referral, etc) - type 1 | Earnings: prints as '62200 - Bonus (annual, referral, etc) - type 1' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 62210 | Bonus - profit sharing - type 1 | Earnings: prints as '62210 - Bonus - profit sharing - type 1' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 62220 | Bonuses - discretionary or one-time - type 1 | Earnings: prints as '62220 - Bonuses - discretionary or one-time - type 1' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 62300 | Annual leave pay | Earnings: prints as '62300 - Annual leave pay' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 62310 | Expat allowance - type 1 | Earnings: prints as '62310 - Expat allowance - type 1' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 62400 | Housing allowance | Earnings: prints as '62400 - Housing allowance' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 62500 | Car allowance | Earnings: prints as '62500 - Car allowance' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 62520 | Transportation allowance | Earnings: prints as '62520 - Transportation allowance' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 62540 | Relocation allowance - type 1 | Earnings: prints as '62540 - Relocation allowance - type 1' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 62550 | Travel ticket allowance | Earnings: prints as '62550 - Travel ticket allowance' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 62570 | Per diem allowance | Earnings: prints as '62570 - Per diem allowance' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 62590 | Birth and Marriage Allowance - type 1 | Earnings: prints as '62590 - Birth and Marriage Allowance - type 1' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 62599 | COVID-19 Allowance | Earnings: prints as '62599 - COVID-19 Allowance' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 62610 | Medical insurance / Medical Care - type 1 | Earnings: prints as '62610 - Medical insurance / Medical Care - type 1' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 62640 | Pensions & Pension Refunds - type 1 | Earnings: prints as '62640 - Pensions & Pension Refunds - type 1' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 62650 | Social raise / Social allowance | Earnings: prints as '62650 - Social raise / Social allowance' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 62660 | Personal Allowance 1 | Earnings: prints as '62660 - Personal Allowance 1' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 62670 | Benefits plan 1 | Earnings: prints as '62670 - Benefits plan 1' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 62700 | Education allowance | Earnings: prints as '62700 - Education allowance' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 62710 | Schooling allowance | Earnings: prints as '62710 - Schooling allowance' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 62760 | Family allowance (MLA, Children) | Earnings: prints as '62760 - Family allowance (MLA, Children)' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 62770 | Recognition Award | Earnings: prints as '62770 - Recognition Award' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 62870 | Special allowance - type 1 | Earnings: prints as '62870 - Special allowance - type 1' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 62880 | Post-termination payment - type 1 | Earnings: prints as '62880 - Post-termination payment - type 1' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 62890 | Stock options and grants - nonstatutory option spread and restricted stock | Earnings: prints as '62890 - Stock options and grants - nonstatutory option spread and restricted stock' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 62900 | Statutory Gratuity, EOS | Earnings: prints as '62900 - Statutory Gratuity, EOS' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | 62901 | Supplemental basic (i.e. 13th or 14th months salary) | Earnings: prints as '62901 - Supplemental basic (i.e. 13th or 14th months salary)' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-001 | Federal income tax withholding (FIT) - regular wages | Employee deductions: prints as 'US-001 - Federal income tax withholding (FIT) - regular wages' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-002 | FIT on supplemental wages - optional flat rate | Employee deductions: prints as 'US-002 - FIT on supplemental wages - optional flat rate' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-003 | FIT on supplemental wages - mandatory rate above the annual threshold | Employee deductions: prints as 'US-003 - FIT on supplemental wages - mandatory rate above the annual threshold' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-006 | Medicare tax - employee | Employee deductions: prints as 'US-006 - Medicare tax - employee' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-008 | Additional Medicare Tax - employee | Employee deductions: prints as 'US-008 - Additional Medicare Tax - employee' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-042 | Commission | Earnings: prints as 'US-042 - Commission' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-043 | Cash tips reported by the employee | Earnings: prints as 'US-043 - Cash tips reported by the employee' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-065 | Pre-tax 408(k)(6) salary reduction - employee deduction | Employee deductions: prints as 'US-065 - Pre-tax 408(k)(6) salary reduction - employee deduction' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-066 | Pre-tax 501(c)(18)(D) contribution - employee deduction | Employee deductions: prints as 'US-066 - Pre-tax 501(c)(18)(D) contribution - employee deduction' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-067 | Designated Roth 401(k) deferral - employee deduction | Employee deductions: prints as 'US-067 - Designated Roth 401(k) deferral - employee deduction' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-068 | Designated Roth 403(b) deferral - employee deduction | Employee deductions: prints as 'US-068 - Designated Roth 403(b) deferral - employee deduction' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-069 | Child support income withholding order | Employee deductions: prints as 'US-069 - Child support income withholding order' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-070 | Federal tax levy on wages | Employee deductions: prints as 'US-070 - Federal tax levy on wages' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-071 | Creditor garnishment | Employee deductions: prints as 'US-071 - Creditor garnishment' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-072 | Union dues deduction (voluntary, after tax) | Employee deductions: prints as 'US-072 - Union dues deduction (voluntary, after tax)' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-073 | Loan or advance repayment deduction (voluntary, after tax) | Employee deductions: prints as 'US-073 - Loan or advance repayment deduction (voluntary, after tax)' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-074 | State income tax withholding - Alabama | Employee deductions: prints as 'US-074 - State income tax withholding - Alabama' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-075 | State income tax withholding - Arkansas | Employee deductions: prints as 'US-075 - State income tax withholding - Arkansas' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-076 | State income tax withholding - Arizona | Employee deductions: prints as 'US-076 - State income tax withholding - Arizona' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-077 | State income tax withholding - California | Employee deductions: prints as 'US-077 - State income tax withholding - California' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-078 | State income tax withholding - Colorado | Employee deductions: prints as 'US-078 - State income tax withholding - Colorado' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-079 | State income tax withholding - Connecticut | Employee deductions: prints as 'US-079 - State income tax withholding - Connecticut' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-080 | State income tax withholding - District of Columbia | Employee deductions: prints as 'US-080 - State income tax withholding - District of Columbia' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-081 | State income tax withholding - Delaware | Employee deductions: prints as 'US-081 - State income tax withholding - Delaware' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-082 | State income tax withholding - Georgia | Employee deductions: prints as 'US-082 - State income tax withholding - Georgia' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-083 | State income tax withholding - Hawaii | Employee deductions: prints as 'US-083 - State income tax withholding - Hawaii' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-084 | State income tax withholding - Iowa | Employee deductions: prints as 'US-084 - State income tax withholding - Iowa' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-085 | State income tax withholding - Idaho | Employee deductions: prints as 'US-085 - State income tax withholding - Idaho' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-086 | State income tax withholding - Illinois | Employee deductions: prints as 'US-086 - State income tax withholding - Illinois' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-087 | State income tax withholding - Indiana | Employee deductions: prints as 'US-087 - State income tax withholding - Indiana' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-088 | State income tax withholding - Kansas | Employee deductions: prints as 'US-088 - State income tax withholding - Kansas' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-089 | State income tax withholding - Kentucky | Employee deductions: prints as 'US-089 - State income tax withholding - Kentucky' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-090 | State income tax withholding - Louisiana | Employee deductions: prints as 'US-090 - State income tax withholding - Louisiana' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-091 | State income tax withholding - Massachusetts | Employee deductions: prints as 'US-091 - State income tax withholding - Massachusetts' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-092 | State income tax withholding - Maryland | Employee deductions: prints as 'US-092 - State income tax withholding - Maryland' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-093 | State income tax withholding - Maine | Employee deductions: prints as 'US-093 - State income tax withholding - Maine' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-094 | State income tax withholding - Michigan | Employee deductions: prints as 'US-094 - State income tax withholding - Michigan' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-095 | State income tax withholding - Minnesota | Employee deductions: prints as 'US-095 - State income tax withholding - Minnesota' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-096 | State income tax withholding - Missouri | Employee deductions: prints as 'US-096 - State income tax withholding - Missouri' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-097 | State income tax withholding - Mississippi | Employee deductions: prints as 'US-097 - State income tax withholding - Mississippi' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-098 | State income tax withholding - Montana | Employee deductions: prints as 'US-098 - State income tax withholding - Montana' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-099 | State income tax withholding - North Carolina | Employee deductions: prints as 'US-099 - State income tax withholding - North Carolina' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-100 | State income tax withholding - North Dakota | Employee deductions: prints as 'US-100 - State income tax withholding - North Dakota' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-101 | State income tax withholding - Nebraska | Employee deductions: prints as 'US-101 - State income tax withholding - Nebraska' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-102 | State income tax withholding - New Jersey | Employee deductions: prints as 'US-102 - State income tax withholding - New Jersey' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-103 | State income tax withholding - New Mexico | Employee deductions: prints as 'US-103 - State income tax withholding - New Mexico' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-104 | State income tax withholding - New York | Employee deductions: prints as 'US-104 - State income tax withholding - New York' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-105 | State income tax withholding - Ohio | Employee deductions: prints as 'US-105 - State income tax withholding - Ohio' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-106 | State income tax withholding - Oklahoma | Employee deductions: prints as 'US-106 - State income tax withholding - Oklahoma' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-107 | State income tax withholding - Oregon | Employee deductions: prints as 'US-107 - State income tax withholding - Oregon' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-108 | State income tax withholding - Pennsylvania | Employee deductions: prints as 'US-108 - State income tax withholding - Pennsylvania' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-109 | State income tax withholding - Rhode Island | Employee deductions: prints as 'US-109 - State income tax withholding - Rhode Island' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-110 | State income tax withholding - South Carolina | Employee deductions: prints as 'US-110 - State income tax withholding - South Carolina' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-111 | State income tax withholding - Utah | Employee deductions: prints as 'US-111 - State income tax withholding - Utah' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-112 | State income tax withholding - Virginia | Employee deductions: prints as 'US-112 - State income tax withholding - Virginia' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-113 | State income tax withholding - Vermont | Employee deductions: prints as 'US-113 - State income tax withholding - Vermont' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-114 | State income tax withholding - Wisconsin | Employee deductions: prints as 'US-114 - State income tax withholding - Wisconsin' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-115 | State income tax withholding - West Virginia | Employee deductions: prints as 'US-115 - State income tax withholding - West Virginia' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-167 | State unemployment insurance - employee - Alaska | Employee deductions: prints as 'US-167 - State unemployment insurance - employee - Alaska' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-168 | State unemployment insurance - employee - New Jersey | Employee deductions: prints as 'US-168 - State unemployment insurance - employee - New Jersey' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-169 | State unemployment insurance - employee - Pennsylvania | Employee deductions: prints as 'US-169 - State unemployment insurance - employee - Pennsylvania' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-170 | State disability insurance (SDI) - employee - California | Employee deductions: prints as 'US-170 - State disability insurance (SDI) - employee - California' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-171 | Paid family and medical leave insurance (FAMLI) - employee - Colorado | Employee deductions: prints as 'US-171 - Paid family and medical leave insurance (FAMLI) - employee - Colorado' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-173 | Paid family and medical leave (PFML) - employee - Connecticut | Employee deductions: prints as 'US-173 - Paid family and medical leave (PFML) - employee - Connecticut' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-175 | Paid leave (PFML) - employee - Delaware | Employee deductions: prints as 'US-175 - Paid leave (PFML) - employee - Delaware' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-177 | Temporary disability insurance (TDI) - employee - Hawaii | Employee deductions: prints as 'US-177 - Temporary disability insurance (TDI) - employee - Hawaii' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-178 | Prepaid health care (PHC) - employee - Hawaii | Employee deductions: prints as 'US-178 - Prepaid health care (PHC) - employee - Hawaii' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-179 | Paid family and medical leave (PFML) - employee - Massachusetts | Employee deductions: prints as 'US-179 - Paid family and medical leave (PFML) - employee - Massachusetts' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-181 | Paid family and medical leave insurance (FAMLI) - employee - Maryland | Employee deductions: prints as 'US-181 - Paid family and medical leave insurance (FAMLI) - employee - Maryland' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-183 | Paid family and medical leave (PFML) - employee - Maine | Employee deductions: prints as 'US-183 - Paid family and medical leave (PFML) - employee - Maine' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-185 | Paid leave (PFML) - employee - Minnesota | Employee deductions: prints as 'US-185 - Paid leave (PFML) - employee - Minnesota' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-187 | Temporary disability insurance (TDI) and family leave insurance (FLI) - employee - New Jersey | Employee deductions: prints as 'US-187 - Temporary disability insurance (TDI) and family leave insurance (FLI) - employee - New Jersey' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-189 | Paid family leave (PFL) - employee - New York | Employee deductions: prints as 'US-189 - Paid family leave (PFL) - employee - New York' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-190 | Disability benefits law (DBL) - employee - New York | Employee deductions: prints as 'US-190 - Disability benefits law (DBL) - employee - New York' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-191 | Paid leave Oregon (PFML) - employee - Oregon | Employee deductions: prints as 'US-191 - Paid leave Oregon (PFML) - employee - Oregon' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-193 | Workers' Benefit Fund assessment - employee - Oregon | Employee deductions: prints as 'US-193 - Workers' Benefit Fund assessment - employee - Oregon' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-195 | Temporary disability insurance (TDI) - employee - Rhode Island | Employee deductions: prints as 'US-195 - Temporary disability insurance (TDI) - employee - Rhode Island' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-196 | Child Care Contribution - employee - Vermont | Employee deductions: prints as 'US-196 - Child Care Contribution - employee - Vermont' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-198 | Paid family and medical leave (PFML) - employee - Washington | Employee deductions: prints as 'US-198 - Paid family and medical leave (PFML) - employee - Washington' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-200 | WA Cares Fund long-term care premium - employee - Washington | Employee deductions: prints as 'US-200 - WA Cares Fund long-term care premium - employee - Washington' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-201 | Workers' compensation State fund premium - employee share - employee - Washington | Employee deductions: prints as 'US-201 - Workers' compensation State fund premium - employee share - employee - Washington' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-202 | Workers' compensation fee - employee - New Mexico | Employee deductions: prints as 'US-202 - Workers' compensation fee - employee - New Mexico' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-204 | Illinois Secure Choice payroll deduction - employee - Illinois | Employee deductions: prints as 'US-204 - Illinois Secure Choice payroll deduction - employee - Illinois' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-208 | Statewide transit tax - employee - Oregon | Employee deductions: prints as 'US-208 - Statewide transit tax - employee - Oregon' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-211 | Alabama municipal occupational tax - Leeds | Employee deductions: prints as 'US-211 - Alabama municipal occupational tax - Leeds' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-212 | Colorado occupational privilege tax - employee share | Employee deductions: prints as 'US-212 - Colorado occupational privilege tax - employee share' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-214 | Wilmington earned income tax | Employee deductions: prints as 'US-214 - Wilmington earned income tax' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-215 | Indiana county income tax | Employee deductions: prints as 'US-215 - Indiana county income tax' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-216 | Kentucky occupational license tax - Louisville and Lexington | Employee deductions: prints as 'US-216 - Kentucky occupational license tax - Louisville and Lexington' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-217 | Maryland county income tax | Employee deductions: prints as 'US-217 - Maryland county income tax' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-218 | Michigan city income tax - Detroit | Employee deductions: prints as 'US-218 - Michigan city income tax - Detroit' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-219 | Michigan city income tax - self-administered cities | Employee deductions: prints as 'US-219 - Michigan city income tax - self-administered cities' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-220 | St. Louis and Kansas City earnings tax | Employee deductions: prints as 'US-220 - St. Louis and Kansas City earnings tax' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-223 | New York City and Yonkers income tax withholding | Employee deductions: prints as 'US-223 - New York City and Yonkers income tax withholding' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-224 | Ohio municipal income tax | Employee deductions: prints as 'US-224 - Ohio municipal income tax' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-225 | Ohio school district income tax | Employee deductions: prints as 'US-225 - Ohio school district income tax' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-226 | Oregon Metro supportive housing services personal income tax | Employee deductions: prints as 'US-226 - Oregon Metro supportive housing services personal income tax' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-227 | Multnomah County preschool for all personal income tax | Employee deductions: prints as 'US-227 - Multnomah County preschool for all personal income tax' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-228 | Pennsylvania local earned income tax (EIT) | Employee deductions: prints as 'US-228 - Pennsylvania local earned income tax (EIT)' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-229 | Pennsylvania local services tax (LST) | Employee deductions: prints as 'US-229 - Pennsylvania local services tax (LST)' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-230 | Philadelphia wage tax | Employee deductions: prints as 'US-230 - Philadelphia wage tax' when the amount is not zero. Wage type of US-WTC-001 v1.0. |
| PAYSLIP_LINE | US-233 | Charleston municipal service fee | Employee deductions: prints as 'US-233 - Charleston municipal service fee' when the amount is not zero. Wage type of US-WTC-001 v1.0. |

## Population Range

| Worker Situation | Include? (YES/NO) | Notes |
|---|---|---|
| Active employees (full-time) | YES | Generate the payslip with the union of the State elements; the work-location State switches the optional blocks. |
| Active employees (part-time) | YES | Same layout with the actual hours, rate, earnings and deductions of the period. |
| New hires during period | YES | Same fields; the pay period, hire date and any partial-period amounts reflect the start date. |
| Terminations during period | YES | Same layout for the final pay; prints the last pay with every deduction itemised. |
| Sick leave | YES | Include when wages or deductions are processed; the paid sick leave balance block prints where the work-location State requires it. |
| Maternity / parental / family leave | YES | Include when payroll records an amount for the period (employer pay or State programme top-up). |
| Unpaid leave | YES | Generate the payslip when payroll issues a record for the period, including a zero-wage statement where the State rule asks for a statement on every payment. |
| Suspended contracts | CONDITIONAL | Include only if payroll produces a payslip for the period. |
| Multiple contracts, same employee | YES | One payslip per payroll result; social security and Medicare wages are accumulated per employer and employee across the result. |
| Foreign workers / nonresident aliens | YES | Same template; the nonresident alien flag and the Form 8233 and totalization fields of the DD switch the tax lines. |
| Household (domestic) employees | CONDITIONAL | Federal populations are all in scope. The payslip is still issued; the California content rule does not apply to an employee of the owner or occupant of a residential dwelling. Section 226 does not apply to any employer of a person employed by the owner or occupant of a residential dwelling whose duties are incidental to the ownership, maintenance, or use of the dwelling, including the care and supervision of children, or whose duties are personal and not in the course of the trade, business, profession, or occupation of the owner or occupant [US-CAS5-005] |
| Agricultural employees | CONDITIONAL | Federal populations are all in scope; State carve-outs apply. deductions_only: detachable part of the check or attached slip with an itemized statement of all deductions (27-4-101(b)); agricultural operations exempt [US-WYP51-005] |
| Employees outside FLSA coverage (non-FLSA) | CONDITIONAL | State statement duty limited to these employees: non_flsa_only: Labor Code 62.003 earnings statement (name, rate, gross, each deduction and purpose, net, hours or units; signed by employer or agent) applies only to employees not covered by the FLSA (62.151); best practice for everyone else [US-TXS5-003] Duty binds employers subject to IC 22-2-2 = 2+ employees NOT subject to the FLSA minimum wage (IC 22-2-2-3); literal reading excludes FLSA-covered employers [US-INS5-001] |
| Board members / directors | CONDITIONAL | Include if they are processed through payroll as common-law employees and receive this layout. |
| Independent contractors (Form 1099-NEC) | NO | Outside the payroll scope of this release; contractors are not issued this payslip. |

## Unit Rate Details

|  | Earning Description | Earning Code | Rate Account | Unit Account | Basis |
|---|---|---|---|---|---|
|  | Basic salary | 62100 | 62104 | US-030 | Regular hours from the hours worked accumulator US-030, with the rate of wage type 62104; amount = hours x rate. |
|  | Overtime - type 1 | 62110 | No rate wage type in the catalogue | US-030 | Overtime hours from the hours worked accumulator US-030; amount = overtime hours x overtime rate of the line, printed apart from straight time. |
|  | Salary addition - type 1 | 62140 | Amount only, no rate account | Amount only, no unit account | Amount only: the line prints the amount of salary addition - type 1 of the pay run; no hours, units or rate print. |
|  | Premium pay (i.e. Shift premium) - type 1 | 62150 | No rate wage type in the catalogue | US-030 | Premium hours from the hours worked accumulator US-030; amount = premium hours x premium rate of the line. |
|  | Holiday Allowance | 62160 | No rate wage type in the catalogue | US-030 | Holiday hours from the hours worked accumulator US-030; amount = holiday hours x rate of the line. |
|  | On-call duty | 62170 | No rate wage type in the catalogue | US-030 | On-call hours from the hours worked accumulator US-030; amount = on-call hours x on-call rate of the line. |
|  | Severance & Seniority - type 1 | 62180 | Amount only, no rate account | Amount only, no unit account | Amount only: the line prints the amount of severance & Seniority - type 1 of the pay run; no hours, units or rate print. |
|  | Long Term Disability | 62190 | Amount only, no rate account | Amount only, no unit account | Amount only: the line prints the amount of long Term Disability of the pay run; no hours, units or rate print. |
|  | Bonus (annual, referral, etc) - type 1 | 62200 | Amount only, no rate account | Amount only, no unit account | Amount only: the line prints the amount of bonus (annual, referral, etc) - type 1 of the pay run; no hours, units or rate print. |
|  | Bonus - profit sharing - type 1 | 62210 | Amount only, no rate account | Amount only, no unit account | Amount only: the line prints the amount of bonus - profit sharing - type 1 of the pay run; no hours, units or rate print. |
|  | Bonuses - discretionary or one-time - type 1 | 62220 | Amount only, no rate account | Amount only, no unit account | Amount only: the line prints the amount of bonuses - discretionary or one-time - type 1 of the pay run; no hours, units or rate print. |
|  | Annual leave pay | 62300 | No rate wage type in the catalogue | US-030 | Annual leave hours from the hours worked accumulator US-030; amount = leave hours x rate of the line. |
|  | Expat allowance - type 1 | 62310 | Amount only, no rate account | Amount only, no unit account | Amount only: the line prints the amount of expat allowance - type 1 of the pay run; no hours, units or rate print. |
|  | Housing allowance | 62400 | Amount only, no rate account | Amount only, no unit account | Amount only: the line prints the amount of housing allowance of the pay run; no hours, units or rate print. |
|  | Car allowance | 62500 | Amount only, no rate account | Amount only, no unit account | Amount only: the line prints the amount of car allowance of the pay run; no hours, units or rate print. |
|  | Transportation allowance | 62520 | Amount only, no rate account | Amount only, no unit account | Amount only: the line prints the amount of transportation allowance of the pay run; no hours, units or rate print. |
|  | Relocation allowance - type 1 | 62540 | Amount only, no rate account | Amount only, no unit account | Amount only: the line prints the amount of relocation allowance - type 1 of the pay run; no hours, units or rate print. |
|  | Travel ticket allowance | 62550 | Amount only, no rate account | Amount only, no unit account | Amount only: the line prints the amount of travel ticket allowance of the pay run; no hours, units or rate print. |
|  | Per diem allowance | 62570 | Amount only, no rate account | Amount only, no unit account | Amount only: the line prints the amount of per diem allowance of the pay run; no hours, units or rate print. |
|  | Birth and Marriage Allowance - type 1 | 62590 | Amount only, no rate account | Amount only, no unit account | Amount only: the line prints the amount of birth and Marriage Allowance - type 1 of the pay run; no hours, units or rate print. |
|  | COVID-19 Allowance | 62599 | Amount only, no rate account | Amount only, no unit account | Amount only: the line prints the amount of cOVID-19 Allowance of the pay run; no hours, units or rate print. |
|  | Medical insurance / Medical Care - type 1 | 62610 | Amount only, no rate account | Amount only, no unit account | Amount only: the line prints the amount of medical insurance / Medical Care - type 1 of the pay run; no hours, units or rate print. |
|  | Pensions & Pension Refunds - type 1 | 62640 | Amount only, no rate account | Amount only, no unit account | Amount only: the line prints the amount of pensions & Pension Refunds - type 1 of the pay run; no hours, units or rate print. |
|  | Social raise / Social allowance | 62650 | Amount only, no rate account | Amount only, no unit account | Amount only: the line prints the amount of social raise / Social allowance of the pay run; no hours, units or rate print. |
|  | Commission | US-042 | Amount only, no rate account | Amount only, no unit account | Amount only: the line prints the amount of commission of the pay run; no hours, units or rate print. |
|  | Cash tips reported by the employee | US-043 | Amount only, no rate account | Amount only, no unit account | Amount only: the line prints the amount of cash tips reported by the employee of the pay run; no hours, units or rate print. |


## Fact index

Every value above with its key, effective period and register id.

| Key | Value | Effective | Register id |
|---|---|---|---|
| `ar.records.withholding.retention_years` | 6 | from 2026-01-01 | US-ARP51-002 |
| `az.records.payroll.retention_years` | 4 | from 2007-01-01 | US-AZS5-006 |
| `ct.payslip.pay_code_guide_url.employer_threshold` | 100 | from 2026-10-01 | US-CTS5-028 |
| `ct.records.retention_years` | 3 | from 2026-01-01 | US-CTS5-027 |
| `dc.records.retention_years` | 3 | from 2026-01-01 | US-DCS5-010 |
| `fed.fica.addl_medicare.rate` | 0.9 | from 2026-01-01 to 2026-12-31 | US-FEDS5-005 |
| `fed.fica.addl_medicare.withholding_threshold` | 200,000 | from 2026-01-01 to 2026-12-31 | US-FEDS5-005 |
| `fed.fica.medicare.rate.employee` | 1.45 | from 2026-01-01 to 2026-12-31 | US-FEDS5-005 |
| `fed.fica.medicare.rate.employer` | 1.45 | from 2026-01-01 to 2026-12-31 | US-FEDS5-005 |
| `fed.fica.oasdi.rate.employee` | 6.2 | from 2026-01-01 to 2026-12-31 | US-FEDS5-005 |
| `fed.fica.oasdi.rate.employer` | 6.2 | from 2026-01-01 to 2026-12-31 | US-FEDS5-005 |
| `fed.fica.oasdi.wage_base` | 184,500 | from 2026-01-01 to 2026-12-31 | US-FEDS5-005 |
| `fed.fit.method` | IRS Pub. 15-T (2026) Worksheet 1A with the Annual Percentage Method tables (STANDARD schedule; Step-2-checked schedule when W-4 Step 2 box checked) | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.rates` | 0/10/12/22/24/32/35/37 | from 2026-01-01 | US-FEDS5-001 |
| `fed.fit.standard.single.thresholds` | 0/7500/19900/57900/113200/209275/263725/648100 | from 2026-01-01 | US-FEDS5-001 |
| `fed.fit.worksheet1a.line1g.other` | 8,600 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.plaw119_21.tips_overtime.level` | assessment; withholding only via W-4 Step 4(b); employer reporting W-2 TP/TT/14b; FICA unchanged | from 2026-01-01 | US-FEDS5-030 |
| `fed.records.flsa.retention_years` | 3 | from 2026-11-02 | US-FEDS5-021 |
| `fed.records.irs.retention_years` | 4 | from 2026-01-01 | US-FEDS5-003 |
| `fed.retirement.pretax.tax_treatment` | 401(k), 403(b) and 457(b) elective deferrals and SIMPLE salary-reduction contributions reduce federal income-tax withholding wages only (within the 402(g) / 457(b) limits); they remain FICA and FUTA wages. Section 125 cafeteria-plan salary reductions for a qualified benefit (accident and health premiums, health FSA, dependent care, HSA) take the treatment of that benefit outside the plan, so they reduce income-tax, FICA and FUTA wages within the benefit limits. | from 2026-01-01 | US-FEDS5-029 |
| `ga.records.gdol.retention_years` | 7 | from 2026-01-01 | US-GAS5-005 |
| `il.records.paystub.retention_years` | 3 | from 2025-01-01 | US-ILS5-024 |
| `ks.records.retention_years` | 3 | from 1978-01-01 | US-KSS5-011 |
| `ma.records.retention_years` | 3 | from 2026-01-01 | US-MAS5-005 |
| `me.pfml.w2_box14_label` | MEPFML | from 2025-01-01 | US-MES5-025 |
| `me.records.retention_years` | 3 | from 2026-01-01 | US-MES5-006 |
| `mi.records.retention_years` | 3 | from 1979-01-04 | US-MIS5-009 |
| `mn.records.retention_years` | 3 | from 2026-01-01 | US-MNS5-020 |
| `mo.records.retention_years` | 3 | from 2006-12-07 | US-MOB5-402 |
| `ms.records.retention_years` | 3 | from 2026-01-01 | US-MSS5-019 |
| `mt.records.payroll_tax.retention_years` | 5 | from 2026-01-01 | US-MTS5-005 |
| `nh.records.retention_years` | 3 | from 2011-08-21 | US-NHS5-003 |
| `nj.payslip.full_content.employer_threshold` | 10 | from 2026-01-01 | US-NJP8-001 |
| `nj.records.wage_hour.retention_years` | 6 | from 2026-01-01 | US-NJS5-022 |
| `nv.leave.paid.coverage_min_employees` | 50 | from 2025-10-01 | US-NVS5-001 |
| `nv.records.retention_years` | 2 | from 2025-10-01 | US-NVS5-001 |
| `oh.records.wage_hour.retention_years` | 3 | from 2026-01-01 to 2027-12-31 | US-OHS5-005 |
| `ok.records.payroll_tax.retention_years` | 4 | from 2019-08-11 | US-OKS5-014 |
| `or.records.retention_years` | 2 | from 2026-01-01 | US-ORS5-019 |
| `psl.ak.retention.wage_hour.years` | 3 | from 2025-09-25 | US-AKS5-001 |
| `psl.ak.sick_leave.on_statement` | Sick leave used in the accrual year and sick leave balance on every statement (since 2025-09-25); a combined PTO plan satisfies it by showing PTO used and balance | from 2025-09-25 | US-AKS5-001 |
| `psl.ak.ssn.rule` | SSN may not be printed on mailed material unless authorised by law (AS 45.48.400-.480); 8 AAC 15.160(h) does not require it: omit or truncate | from 2026-01-01 | US-AKS5-016 |
| `psl.ak.statement.content` | Written or electronic, each pay period: rate; gross and net; pay-period dates; federal income tax and Federal Insurance Contribution Act deductions; Alaska Employment Security Act contributions; board/lodging deductions; advances; straight-time and overtime hours; other authorised deductions; sick leave used in accrual year; sick leave balance | from 2025-09-25 | US-AKS5-001 |
| `psl.ak.statement.electronic_delivery` | Written or electronic; no separate consent rule | from 2025-09-25 | US-AKS5-001 |
| `psl.al.statement.scope` | none: no state pay-statement content statute; federal records rules apply | from 2025-10-02 | US-ALP52-001 |
| `psl.ar.statement.scope` | none: no itemised pay-statement statute; tipped employees get the tip-credit amount per hour in writing each time it changes (11 CAR 11) | from 2026-07-21 | US-ARP52-006 |
| `psl.az.sick_leave.on_statement` | Every regular paycheck or attachment: earned paid sick time available, used to date in the year, and pay received as sick time (A.R.S. 23-375(C)) | from 2017-07-01 | US-AZS5-011 |
| `psl.az.statement.scope` | Statement (no content list) required only when paying by direct deposit or payroll card (A.R.S. 23-351(E),(F)) | from 2026-01-01 | US-AZS5-001 |
| `psl.ca.penalty.max_per_employee` | 4,000 | from 2023-10-13 | US-CAS5-005 |
| `psl.ca.retention.wage_statements.years` | 3 | from 2023-10-13 | US-CAS5-005 |
| `psl.ca.sick_leave.on_statement` | Available paid sick leave on the wage statement or a separate writing each payday | from 2024-01-01 | US-CAS5-011 |
| `psl.ca.ssn.rule` | Only the last 4 SSN digits or an employee ID (226(a)(7)) | from 2023-10-13 | US-CAS5-005 |
| `psl.ca.statement.content` | Lab. Code 226(a), semimonthly or each payment: gross; total hours (not for salaried exempt); piece units and rates; deductions; net; pay-period dates; name + last 4 SSN or employee ID; employer legal name and address; each hourly rate with hours | from 2023-10-13 | US-CAS5-005 |
| `psl.ca.statement.household_exclusion` | Section 226 does not apply to any employer of a person employed by the owner or occupant of a residential dwelling whose duties are incidental to the ownership, maintenance, or use of the dwelling, including the care and supervision of children, or whose duties are personal and not in the course of the trade, business, profession, or occupation of the owner or occupant | from 2023-10-13 | US-CAS5-005 |
| `psl.co.ssn.rule` | SSN may appear instead of the name (8-4-103(4)(e)); no truncation rule in the Wage Act | from 2025-08-06 | US-COP51-005 |
| `psl.co.statement.comps_rule7` | Statement shows total pay, rate, tips, credits and time worked; kept 3 years | from 2026-01-01 to 2026-12-31 | US-COS5-001 |
| `psl.co.statement.content` | C.R.S. 8-4-103(4), at least monthly or each payment: gross; all withholdings and deductions; net; pay-period dates; employee name or SSN; employer name and address. COMPS Rule 7 adds rate, tips, credits and time worked | from 2025-08-06 | US-COP51-005 |
| `psl.ct.pay_code_guide.url_on_pay_record` | From 2026-10-01 (PA 26-12 sec. 38, 31-13a(c)): employers with 100+ employees publish a pay-code guide (overtime and common differentials, min 10 codes where applicable) in English, Spanish and other common languages; its Internet web site address appears on each record of hours and is given at hire; a payroll provider guide satisfies it | from 2026-10-01 | US-CTS5-028 |
| `psl.ct.statement.content` | Each payment: hours worked; gross pay with straight time and overtime separate; itemised deductions; net (hours and split not for OT-exempt) | from 2026-01-01 | US-CTP51-005 |
| `psl.ct.statement.electronic_delivery` | Electronic only with the employee explicit consent, a secure private way to access and print, and confidentiality safeguards (31-13a(b)) | from 2026-01-01 | US-CTS5-027 |
| `psl.dc.statement.content` | Each payment (32-1008(b)): date of payment; gross; deductions and additions with gratuities on a separate line; net; hours worked; tip declaration split cash/card; from 2026-01-01 a list of compensation sources beyond base wages and tips | from 2026-01-01 | US-DCS5-010 |
| `psl.de.retention.wage_records.years` | 3 | from 2025-01-01 | US-DES5-001 |
| `psl.de.statement.content` | Employers with more than 3 employees, each payment: wages due; pay period; total deductions each separately specified; total hours for hourly employees (19 Del. C. 1108) | from 2026-01-01 | US-DES5-002 |
| `psl.de.statement.electronic_delivery` | On the check, a separate slip, or electronically if the employee can retain it; employee may ask for paper | from 2026-01-01 | US-DES5-002 |
| `psl.de.statement.employer_threshold` | more than 3 employees | from 2026-01-01 | US-DES5-002 |
| `psl.fed.statement.required` | False | from 2026-10-01 | US-FED-010 |
| `psl.fl.statement.scope` | none for general employers; labor pools only (448.24(2)(g),(h)): itemised deductions each payment and annual earnings summary by 1 February | from 2026-01-01 | US-FLL-002 |
| `psl.ga.statement.scope` | none: O.C.G.A. 34-7-2 has no statement duty; GDOL handbook has no pay-stub rule | from 2015-05-05 | US-GAP9L-001 |
| `psl.hi.ssn.rule` | Not required on the statement; section 487J-2 bars making an entire SSN available to the general public and printing an entire SSN on mailed materials, except employer-to-employee communications or where the individual requests it | from 2026-01-01 | US-HIS5-028 |
| `psl.hi.statement.content` | HRS 387-6(c), 14 items: employee name; employer name; employer address and phone; total hours; regular and OT hours; straight-time pay; OT pay; other compensation incl. allowances toward minimum wage; gross; amount and purpose of each deduction; net; pay date; pay period; rates and basis incl. OT and piece rates with counts | from 2026-01-01 | US-HIP52-001 |
| `psl.hi.statement.electronic_delivery` | Electronic with the employee written authorization; direct deposit still requires a statement | from 2026-01-01 | US-HIS5-007 |
| `psl.ia.retention.payroll_records.years` | 3 | from 2026-01-01 | US-IAP51-002 |
| `psl.ia.statement.content` | Each regular payday: hours worked, wages earned, deductions (91A.6(4)); itemised computation within 10 working days on request | from 2026-01-01 | US-IAP51-002 |
| `psl.ia.statement.electronic_delivery` | Mail, secure electronic means, at the workplace, or access to view; no separate consent | from 2026-01-01 | US-IAP51-002 |
| `psl.ia.statement.reach` | Employees employed in Iowa (work location, not residence) (91A.2(3),(4)) | from 2023-07-01 | US-IAS5-027 |
| `psl.id.retention.employment_records.years` | 3 | from 1999-07-01 | US-IDS5-006 |
| `psl.id.statement.scope` | deductions_only: written statement of deductions for each pay period with deductions (45-609(2)) | from 2026-01-01 | US-IDP51-002 |
| `psl.il.statement.content` | Pay stub each pay period with itemized deductions (820 ILCS 115/10 as amended by P.A. 103-953); payroll-card payees also get hours, rate and deductions | from 2025-01-01 | US-ILS5-024 |
| `psl.il.statement.electronic_access` | Stubs kept 3 years; copies within 21 days on request (max twice per 12 months; former employees for one year); if electronic stubs become inaccessible after separation, offer prior-year stubs by the final pay period and record the offer | from 2025-01-01 | US-ILS5-024 |
| `psl.in.statement.content` | Each pay period at least hours worked, wages paid, deductions (IC 22-2-2-8(a)) | from 2026-01-01 | US-INP6-001 |
| `psl.in.statement.scope` | Duty binds employers subject to IC 22-2-2 = 2+ employees NOT subject to the FLSA minimum wage (IC 22-2-2-3); literal reading excludes FLSA-covered employers | from 2007-06-30 | US-INS5-001 |
| `psl.ks.statement.scope` | on_request: itemized statement of deductions on request for each pay period with deductions (K.S.A. 44-320(d)) | from 1973-07-01 | US-KSP52-001 |
| `psl.ky.retention.pay_records.years` | 1 | from 2010-07-15 | US-KYP8-002 |
| `psl.ky.statement.content` | Employers with 10+ employees that make deductions: each payment, paper or electronic statement of each deduction and its purpose; electronic requires access to a computer and printer (section 337.070) | from 2017-06-29 | US-KYP8-001 |
| `psl.ky.statement.employer_threshold` | 10 | from 2017-06-29 | US-KYP8-001 |
| `psl.language.official_federal` | en: English designated by presidential action of 2025-03-01; no obligation on private employers | from 2025-03-01 | US-FED-020 |
| `psl.ma.statement.content` | Each payment (c.149 s.148): employer name; employee name; date; hours worked; hourly rate; deductions or increases for the period | from 2026-01-01 | US-MAP51-008 |
| `psl.md.sick_leave.on_statement` | Available earned sick and safe leave balance each time wages are paid; an online balance system satisfies it (LE 3-1305(f)) | from 2018-02-11 | US-MDS5-013 |
| `psl.md.ssn.rule` | No SSN at all on the wage check, any attachment, a direct-deposit notice or a card-credit notice (LE 3-502(d)); treat truncated SSN as barred too | from 2026-01-01 | US-MDS5-008 |
| `psl.md.statement.content` | LE 3-504: employer name, address, phone; pay date and period; hours (unless exempt); rates; gross and net; each deduction by name and amount; other bases of pay; written or online | from 2026-01-01 | US-MDP51-005 |
| `psl.md.statement.tip_credit` | Tip Credit Wage Statement for restaurants | from 2026-01-01 | US-MDS5-007 |
| `psl.me.statement.content` | Each payment: date of the pay period, hours, total earnings, itemized deductions (Title 26 section 665, subsection 1) | from 2026-01-01 | US-MES5-006 |
| `psl.me.statement.electronic_delivery` | Electronic allowed only with ready access and printing at no cost; same record due when a direct deposit is made | from 2026-01-01 | US-MES5-006 |
| `psl.mi.ssn.rule` | No more than 4 sequential SSN digits displayed (SSN Privacy Act, MCL 445.83/.84); employer must publish an SSN privacy policy | from 2006-01-01 | US-MIS5-013 |
| `psl.mi.statement.content` | At payment (MCL 408.479(2)): hours worked, gross, pay-period identification, separate itemisation of deductions; comp time earned or paid | from 1979-01-04 | US-MIS5-009 |
| `psl.mn.sick_leave.on_statement` | ESST hours available and used each pay period, on or attached to the statement or via an electronic system | from 2024-01-01 | US-MNS5-011 |
| `psl.mn.statement.content` | Earnings statement at the end of each pay period, in writing or by electronic means. Under 181.032(b) it must include: (1) the name of the employee; (2) the rate or rates of pay and basis thereof, including whether the employee is paid by hour, shift, day, week, salary, piece, commission, or other method; (3) allowances, if any, claimed pursuant to permitted meals and lodging; (4) the total number of hours worked by the employee unless exempt from chapter 177; (5) the total amount of gross pay earned by the employee during that period; (6) a list of deductions made from the employee's pay; (7) any amount deducted by the employer under section 268B.14, subdivision 3, and the amount paid by the employer based on the employee's wages under section 268B.14, subdivision 1; (8) the net amount of pay after all deductions are made; (9) the date on which the pay period ends; (10) the legal name of the employer and the operating name of the employer if different from the legal name; (11) the physical address of the employer's main office or principal place of business, and a mailing address if different; and (12) the telephone number of the employer | from 2026-01-01 | US-MNP6-001 |
| `psl.mn.statement.electronic_delivery` | Electronic requires access to an employer computer during work hours and statements kept available 3 years | from 2026-01-01 | US-MNP6-001 |
| `psl.mo.ssn.rule` | No public display; SSN or its last four digits may not be required as an employee number (407.1355); no explicit pay-statement rule | from 2012-08-28 | US-MOS5-016 |
| `psl.mo.statement.scope` | deductions_only: statement of total deductions at least monthly (290.080) | from 1955-08-28 | US-MOP52-002 |
| `psl.mt.statement.content` | Every payment: itemized statement of state and federal income tax, social security and other deductions with amounts; statement saying none if nothing deducted (MCA 39-3-101) | from 2026-01-01 | US-MTP51-006 |
| `psl.multi.reach.ca` | Lab. Code 226 applies when the principal place of work is CA (majority of working time); if no majority state, when CA is the base of work operations and some work is done in CA (Ward v. United Airlines, S248702, 2020-06-29; level: pay-statement content) | from 2020-06-29 | US-MULTIS5-018 |
| `psl.multi.reach.default` | Default: the pay-statement statute of the work-location state; no other state reach rule identified | from 2020-06-29 | US-MULTIS5-018 |
| `psl.nc.retention.withholding_records.years` | 10 | from 2026-01-01 | US-NC-001 |
| `psl.nc.ssn.rule` | G.S. 75-62: no SSN on mailed material unless law requires | from 2026-01-01 | US-NCS5-016 |
| `psl.nc.statement.electronic_delivery` | In writing, printable e-mail or any means the employee can keep; no separate consent | from 1999-04-01 | US-NCS5-024 |
| `psl.nc.statement.scope` | deductions_only: itemized statement of deductions each pay period with deductions (G.S. 95-25.13), plus hire wage notice | from 2026-01-01 | US-NCW1B-003 |
| `psl.nd.statement.content` | Each pay period a check stub or pay voucher: hours worked, rate, required state and federal deductions, authorized deductions (46-02-07-02, recordkeeping item 10) | from 2012-10-01 | US-NDS5-007 |
| `psl.ne.ssn.rule` | No more than the last 4 SSN digits displayed publicly or to coworkers (48-237) | from 2026-01-01 | US-NES5-013 |
| `psl.ne.statement.content` | Each regular payday: employer identity, hours paid, wages earned, deductions (48-1230(2)); hours not required for FLSA-exempt unless OT/hours-based | from 2026-01-01 | US-NEP51-004 |
| `psl.nh.statement.scope` | deductions_only: statement of deductions each pay period with a deduction (RSA 275:49 IV); written monthly accounting for 275:48 I(d) deductions | from 2026-01-01 | US-NHP51-001 |
| `psl.nj.statement.content` | Statement of deductions each pay period with deductions; employers with 10+ employees add gross, net, rate and hours where relevant (34:11-4.6(c)) | from 2026-01-01 | US-NJP8-001 |
| `psl.nj.statement.electronic_delivery` | Electronic allowed unless the employee asks for paper | from 2026-01-01 | US-NJP8-001 |
| `psl.nm.sick_leave.on_statement` | Year-to-date earned sick leave accrued and used, at least quarterly, on the earnings statement or electronically | from 2022-07-01 | US-NMS5-002 |
| `psl.nm.statement.content` | Written receipt each payday: employer identity; gross; hours worked; total wages and benefits earned; itemized deductions (50-4-2(B)) | from 2026-01-01 | US-NMP8-001 |
| `psl.notice_language.az` | Minimum-wage and earned-paid-sick-time posters/notice in English and Spanish (A.R.S. 23-375(B)) | from 2026-01-01 | US-AZL-001 |
| `psl.notice_language.ca` | Hire notice (Lab. Code 2810.5) in the language the employer normally uses | from 2024-01-01 | US-CAP6-001 |
| `psl.notice_language.co_comps` | COMPS Order Rule 7.4.3: Spanish COMPS Order/poster where employees with limited English language ability speak Spanish, or a Division version in another language | from 2026-01-01 | US-COP9L-001 |
| `psl.notice_language.co_paid_leave` | C.R.S. 8-13.3-408(2): notice in English and the first language of 5%+ of the workforce | from 2026-01-01 | US-COL-001 |
| `psl.notice_language.ct` | C.G.S. 31-57w(b) paid sick leave poster in English and Spanish | from 2026-01-01 | US-CTL-001 |
| `psl.notice_language.dc` | Hire/change notice (32-1008(c)) in English and also the primary language where the Mayor has a template | from 2026-01-01 | US-DCS5-010 |
| `psl.notice_language.de` | 19 Del. C. 3710(c) paid-leave notice in English, Spanish and any first language of 5%+ of the workforce | from 2026-01-01 | US-DEL-001 |
| `psl.notice_language.fl` | Fla. Stat. 448.109(3)(a) minimum-wage poster in English and Spanish | from 2026-01-01 | US-FLL-001 |
| `psl.notice_language.ma` | M.G.L. c.149 s.148C(o) earned sick time notice languages | from 2026-01-01 | US-MAL-002 |
| `psl.notice_language.mi` | ESTA notice/poster in English, Spanish and any language that is the first language of 10%+ of the workforce if the Department has translated it | from 2025-02-21 | US-MIL-001 |
| `psl.notice_language.mn` | Hire notice (181.032) in English; other language on request | from 2026-01-01 | US-MNP6-001 |
| `psl.notice_language.nj_gender_equity` | N.J.S.A. 34:11-56.12(c): employers with 50+ employees post and provide in English, Spanish and Commissioner-available first languages; deliverable as a pay-check insert | from 2026-01-01 | US-NJP9M-001 |
| `psl.notice_language.nj_sick_leave` | NJ earned sick leave notice in the languages published by NJDOL | from 2026-01-01 | US-FEDR3-010 |
| `psl.notice_language.ny` | Hire notice (Labor Law 195(1)(a)) in English and the employee primary language | from 2026-01-01 | US-NYP51-003 |
| `psl.notice_language.or` | ORS 652.610(6): BOLI template in English and Spanish for the new-hire earnings/deductions explanation | from 2026-01-01 | US-ORL-001 |
| `psl.notice_language.tx_workplace_violence` | Workplace-violence reporting notice in English and Spanish, every employer with 1+ employees since 2024-01-08 (HB 915; 40 TAC 800.600) | from 2024-01-08 | US-TXP9M-001 |
| `psl.notice_language.vt_paycard` | 21 V.S.A. 342(f) payroll-card disclosures in the primary language | from 2024-07-01 | US-VTL-001 |
| `psl.nv.paid_leave.on_statement` | Accounting of available paid-leave hours on every payday, employers with 50+ NV employees (608.0197(1)(h)) | from 2025-10-01 | US-NVS5-001 |
| `psl.nv.statement.content` | Itemized list of deductions at each payment (NRS 608.110(2)) | from 2026-01-01 | US-NVR3-001 |
| `psl.ny.retention.payroll_records.years` | 6 | from 2020-10-02 | US-NYS5-006 |
| `psl.ny.ssn.rule` | Labor Law 203-d: no public display, no SSN on badges or time cards; not a required statement field | from 2014-09-22 | US-NYS5-009 |
| `psl.ny.statement.content` | Labor Law 195(3), every payment: dates of work; names; employer address and phone; rates and basis; gross; deductions; allowances toward minimum wage; net; non-exempt: regular and OT rates and hours; piece rates and counts | from 2020-10-02 | US-NYS5-006 |
| `psl.nyc.pto.on_statement` | NYC Earned Safe and Sick Time (Protected Time Off): each pay period show PTO accrued in the period, paid and unpaid PTO used in the period, unpaid immediately available hours available in the calendar year, and accrued PTO available for use in the calendar year (pay statement or other written documentation) | from 2026-02-22 | US-NYB5-003 |
| `psl.oh.statement.content` | ORC 4113.14 (from 2025-04-09), each pay period written or electronic: employee name and address; employer name; gross and net; amount and purpose of each addition and deduction; pay date and period; hourly employees hours and rate | from 2025-04-09 | US-OHP51-001 |
| `psl.ok.ssn.rule` | No SSN on materials mailed to the employee unless law requires (40 O.S. 173.1); mask on mailed payslips | from 2004-11-01 | US-OKS5-008 |
| `psl.ok.statement.scope` | deductions_only: brief itemized statement of all deductions with each payment (40 O.S. 165.2) | from 2022-11-01 | US-OKS5-003 |
| `psl.or.new_hire_explanation` | From 2026-01-01 (SB 906): written explanation of earnings and deductions incl. all payroll codes at hire, updated by 1 January each year | from 2025-05-07 | US-ORS5-022 |
| `psl.or.statement.content` | ORS 652.610(1)(b): payment date; dates of work; employee name; employer name and registry/ID number; employer address and phone; rates; basis; gross; net; each deduction with amount and purpose; allowances toward minimum wage; non-exempt regular and OT rates, hours and pay; piece rates and counts | from 2026-01-01 | US-ORS5-026 |
| `psl.or.statement.electronic_delivery` | Electronic only with the employee express agreement and ability to print or store on receipt (652.610(1)(c)) | from 2026-01-01 | US-ORS5-026 |
| `psl.pa.ssn.rule` | Act 60 of 2006: no SSN on mailed materials unless law requires; mailed stubs omit the SSN | from 2006-12-26 | US-PAS5-020 |
| `psl.pa.statement.content` | Every payment: hours worked, rates, gross, allowances toward minimum wage, deductions, net (34 Pa. Code 231.36) | from 2026-01-01 | US-PAP51-001 |
| `psl.ri.ssn.rule` | No part of the SSN on material mailed to the individual unless law requires (6-48-8) | from 2008-01-01 | US-RIS5-020 |
| `psl.ri.statement.content` | Every regular payday: hours worked (except 28-12-4.3 exempt), every deduction with explanation; commercial construction also regular hourly rate (28-14-2.1); electronic allowed, free printed copy on written request | from 2026-01-01 | US-RIP51-002 |
| `psl.sc.ssn.rule` | No 6 or more SSN digits on mailed material or public display (37-20-180): mailed statements show 5 digits at most | from 2026-01-01 | US-SCS5-009 |
| `psl.sc.statement.content` | Itemized statement of gross pay and deductions each pay period (41-10-30(C)); direct deposit: statement of earnings and withholdings (41-10-40(B)) | from 2026-01-01 | US-SCP52-006 |
| `psl.sc.statement.exemptions` | Section 41-10-30 (notification to employees) does not apply to domestic labour in private homes or to employers with fewer than five employees at all times in the preceding twelve months (41-10-20) | from 2026-01-01 | US-SCP52-006 |
| `psl.sd.statement.scope` | none: no SD statute requires a pay statement (Title 60 full-text scan) | from 2026-01-01 | US-SDS5-001 |
| `psl.tn.statement.scope` | none: no TN itemised pay-statement statute located; federal records rules | from 2026-01-01 | US-TNS5-001 |
| `psl.tx.ssn.rule` | Bus. & Com. Code 501.001(a)(5): no SSN printed on any material sent by mail unless state or federal law requires it | from 2026-01-01 | US-TXS5-013 |
| `psl.tx.statement.scope` | non_flsa_only: Labor Code 62.003 earnings statement (name, rate, gross, each deduction and purpose, net, hours or units; signed by employer or agent) applies only to employees not covered by the FLSA (62.151); best practice for everyone else | from 1993-09-01 | US-TXS5-003 |
| `psl.ut.statement.format` | All lawful offsets itemized on a statement or detachable check stub (R610-3-20) | from 2012-04-16 | US-UTS5-012 |
| `psl.ut.statement.scope` | deductions_only: statement of each deduction on each regular payday (34-28-3(4)); construction-trade licensees full statement (34-28-3(5)) | from 2014-05-13 | US-UTP6-001 |
| `psl.va.retention.pay_statements.years` | 3 | from 2026-07-01 | US-VAS5-003 |
| `psl.va.statement.content` | Each regular pay date, paystub or online accounting: employer name and address; hours (hourly and salaried below the FLSA level); rate; gross; amount and purpose of each deduction; enough detail to work out gross and net | from 2026-07-01 | US-VAS5-003 |
| `psl.vt.ssn.rule` | No full SSN on mailed materials (9 V.S.A. 2440); redacted SSN permitted | from 2007-01-01 | US-VTS5-015 |
| `psl.vt.statement.content` | Detailed written statement with each weekly pay: gross, hours, hourly rate, itemised deductions incl. meals | from 2009-01-01 | US-VTP9-001 |
| `psl.w2.box12.new_codes_2026` | TP (cash tips), TT (qualified overtime), TA (Trump-account employer contributions) | from 2026-01-01 | US-FEDS5-007 |
| `psl.w2.box14.ca_sdi` | CASDI (or VPDI) in Box 14; CA PIT wages Box 16; CA PIT withheld Box 17 | from 2026-01-01 to 2026-12-31 | US-CAS5-018 |
| `psl.w2.box14.vt_child_care_contribution` | VT CCC employee share (max 0.11% of wages, of the 0.44% total) reported in W-2 Box 14 | from 2024-07-01 | US-VTS5-030 |
| `psl.w2.box14b.tipped_occupation_code` | Box 14 split into 14a Other and 14b Treasury Tipped Occupation Code(s) from TY2026 | from 2026-01-01 | US-FEDS5-007 |
| `psl.w2.multistate.boxes_15_20` | Up to two states and two localities per W-2; more requires a second W-2 repeating boxes a-f, never duplicating federal data on Copy A; W-3 box 15 = X when more than one state | from 2026-01-01 | US-MULTIS5-011 |
| `psl.w2.ssn_truncation.rule` | SSN may be truncated (first five digits masked, last four shown, e.g. ***-**-1234) on employee W-2 copies only; never on Copy A; EIN never truncated | from 2019-07-03 | US-FEDS5-022 |
| `psl.wa.sick_leave.on_statement` | At least monthly: paid sick leave accrued, used and available; may be on the regular pay statement (WAC 296-128-755(2)) | from 2026-01-01 | US-WAS5-005 |
| `psl.wa.statement.content` | Every payday, separate from the paycheck: hours or days worked, rates, gross, all deductions, pay period, payment date (WAC 296-126-040) | from 2026-01-01 | US-WAS5-004 |
| `psl.wa.statement.electronic_delivery` | Electronic if the employee can receive and copy it on payday; otherwise paper | from 2026-01-01 | US-WAS5-004 |
| `psl.wi.statement.content` | Hours worked, rate, amount and reason for each deduction, on the check, envelope or accompanying paper; coding system allowed (103.457; DWD 272.10) | from 2026-10-01 | US-WIP52-001 |
| `psl.wv.statement.content` | Scheduled payday itemized statement: hourly rate or salary; hours paid; OT rate; bonus or incentive pay; itemized deductions (42 CSR 5 s.7.3, sunset 2029-07-01) | from 2019-07-01 to 2029-07-01 | US-WVS5-008 |
| `psl.wy.statement.scope` | deductions_only: detachable part of the check or attached slip with an itemized statement of all deductions (27-4-101(b)); agricultural operations exempt | from 2026-01-01 | US-WYP51-005 |
| `sc.records.wage.retention_years` | 3 | from 2026-01-01 | US-SCP52-006 |
| `vt.ccc.employee.max_rate` | 0.11 | from 2024-07-01 | US-VTS5-030 |
| `wa.records.esd.retention_years` | 4 | from 2026-01-01 | US-WAS5-030 |
| `wi.records.retention_years` | 3 | from 2009-07-24 | US-WIS5-002 |
| `wv.records.retention_years` | 5 | from 2019-07-01 to 2029-07-01 | US-WVS5-008 |
| `wy.records.retention_years` | 2 | from 2026-05-08 | US-WYS5-001 |
