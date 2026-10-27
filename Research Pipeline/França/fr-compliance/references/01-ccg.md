# France Country Configuration Guide (CCG) - FR-CCG-001 v1.0

Complete text of the delivered France CCG: all 13 modules, every rate, bracket, ceiling, threshold, treatment matrix and worked example, with the legal citations as delivered. Income year 2026, assessment year 2027. Currency EUR.


## Provenance

| Source artifact | Bytes | SHA-256 |
|---|---|---|
| `FR-compliance/01-ccg/FR-CCG-001-v1.0.docx` | 208,322 | `dae13206a21290eb…` |

This file is a complete, verbatim conversion of the artifacts above. Figures, dates, code values, French terminology and legal citations are reproduced exactly as delivered; nothing is summarised or rounded.


## Navigation index

Read with `offset` / `limit` rather than opening the whole file.

| Line | Section |
|---|---|
| 244 | &nbsp;&nbsp;&nbsp;&nbsp;Table of Contents |
| 248 | &nbsp;&nbsp;&nbsp;&nbsp;Module 1: Foundational Jurisdictional Parameters |
| 251 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1.1 Fiscal, Currency, and Language |
| 254 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;What is the statutory tax year? |
| 260 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Can employers adopt an alternate tax year? If yes, under what circumstances and what are the implications? |
| 265 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;What is the official currency for payroll processing and reporting? Provide the ISO code. |
| 271 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;What is the official language for statutory reports and employee payslips? |
| 285 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1.2 Pay Cycles and Dates |
| 288 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;What are the permissible payroll payment frequencies in the country? |
| 302 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For each frequency, detail the corresponding statutory reporting and payment deadlines for both income tax withholding and social security contributions. |
| 322 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Describe the statutory rule for handling pay dates that fall on a weekend or public holiday. |
| 329 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;What are the common payroll pay dates and cut-off dates for payroll processing? |
| 342 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1.3 Extra Pay Period Handling |
| 345 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Describe the statutory handling and calculation adjustments required for fiscal years containing extra pay periods (e.g., 53 weekly pays). |
| 351 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Detail the impact on annualized tax calculations and social security contributions. |
| 362 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If optional adjustment methods are permitted, provide a step-by-step guide. |
| 372 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1.4 Holiday Calendar |
| 375 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;What are the official public holidays? |
| 396 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Are there any regional, state-specific, or company-specific holidays? |
| 409 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1.5 Rounding and Precision Rules |
| 412 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;What are the statutory or common business practice rules for rounding final net pay and individual calculation components? |
| 428 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;What level of decimal precision is required for statutory reporting? |
| 442 | &nbsp;&nbsp;&nbsp;&nbsp;Module 2: Master Data Configuration |
| 446 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.1 Employer Information |
| 449 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;What are the different boards or authorities where an employer must register? |
| 466 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;What is the configuration/format of registration numbers allotted by each authority? |
| 482 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Are registration numbers allotted at the central level or at the state/township level? |
| 497 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.2 Employee Information |
| 500 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;What are the different residential statuses for an individual? |
| 512 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;What employee fields are required for processing payroll and statutory reporting? |
| 526 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;What is the configuration/format of registration numbers (e.g., tax ID, social security number) allotted to employees? |
| 538 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Provide any relevant combo values or sample inputs for each field. |
| 555 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;What previous employment information must new joiners declare? |
| 573 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.3 Data Management and Retention |
| 576 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;What are the statutory requirements for payroll record retention (e.g., number of years)? |
| 592 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Are there specific data privacy laws (like GDPR) that govern the storage and handling of employee payroll data? |
| 608 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;How should historical payroll data (e.g., from a previous provider) be handled for cumulative calculations? |
| 627 | &nbsp;&nbsp;&nbsp;&nbsp;Module 3: The Gross-to-Net Calculation Framework |
| 630 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.1 Gross-to-Net Flow |
| 633 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Deliverable: Provide a definitive, step-by-step description or text-based flowchart illustrating the standard Gross-to-Net (G2N) calculation framework, and explain where employer on-costs are calculated in parallel. |
| 642 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Step 1 — Summation of gross earnings |
| 659 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Step 2 — Build the contribution bases |
| 670 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Step 3 — Apply employee contributions |
| 690 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Step 4 — Compute the statutory net social amount |
| 694 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Step 5 — Determine the net taxable amount |
| 709 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Step 6 — Calculate the income tax withheld at source |
| 712 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Step 7 — Apply post-tax deductions |
| 722 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Step 8 — Finalise net pay |
| 730 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Employer on-costs, calculated in parallel |
| 756 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Order of operations, and why it matters |
| 762 | &nbsp;&nbsp;&nbsp;&nbsp;Module 4: Gross Compensation |
| 765 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.1 Minimum Wage |
| 768 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Is there a minimum wage? Who is eligible? |
| 781 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Is the minimum wage applicable at a national level or does it vary by province/state? |
| 787 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Provide all applicable minimum wage rates. |
| 802 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Does the minimum wage impact any tax or social security calculations? |
| 818 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;How are deductions handled if they cannot be made due to minimum wage constraints? |
| 843 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.2 Salary Components |
| 846 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;What are the mandatory and common salary components? |
| 866 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;What is the general definition and pay cycle for each component? |
| 882 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Which components are taxable vs non-taxable and sociable vs non-sociable? |
| 905 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Are components uniform across the country or do they differ by state/province? |
| 917 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;What is the calculation logic for each salary component? |
| 934 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Which components require employee-declared values and submissions? |
| 949 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Deliverable: Define the primary earnings base for social security contributions and produce a comprehensive inclusion/exclusion analysis. |
| 981 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.3 Proration |
| 984 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Are fixed wages prorated for the number of working days? |
| 998 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Describe the statutory or standard business practice for prorating fixed salary components for mid-period hires and terminations. |
| 1011 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Provide the proration formula and a worked example. |
| 1039 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.4 Overtime |
| 1042 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Detail the statutory rules for overtime, including eligibility criteria and mandatory rates. |
| 1062 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Explain how overtime is treated for income tax and social security calculations. |
| 1078 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.5 Bonuses |
| 1081 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Is there a statutory requirement to pay bonuses? If so, how are they calculated? |
| 1095 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Is there a specific tax treatment for bonuses? |
| 1112 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.6 Wage Classification (Country-Specific) |
| 1115 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Are there country-specific classifications for wages critical for social security or tax calculations? |
| 1127 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Provide a detailed definition for each classification. |
| 1146 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Create a reference table classifying common pay components. |
| 1174 | &nbsp;&nbsp;&nbsp;&nbsp;Module 5: Social Security & Pension Systems |
| 1177 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.1 Contribution Types and Rates |
| 1180 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;List all mandatory social security and pension contributions for both employer and employee. |
| 1215 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Are contributions managed at a national or sub-national level? |
| 1230 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.1.1 Contribution Basis Definition |
| 1233 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For each mandatory contribution, provide the statutory definition of the earnings base. |
| 1251 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Clarify the legal definitions of any specific terms used. |
| 1279 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Deliverable: Provide a comprehensive summary of current contribution rates, describing rates across regions and residential statuses, including tiers, ceilings, floors, and variations by age or gender. |
| 1341 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.2 Calculation Logic and Edge Cases |
| 1344 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;What is the step-by-step calculation logic for all types of social security contributions? |
| 1377 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Are contributions based on actual or standard salary? |
| 1389 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Describe rules for eligibility, joining month, termination month, mid-period hires, mid-period terminations, and mid-period salary changes. |
| 1407 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do different payment frequencies affect contribution rates or parameters? |
| 1422 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Detail variations based on employee age or gender. |
| 1434 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Is there a minimum number of working days required for contributions? |
| 1439 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;How are contributions calculated for Board of Directors who are also employees? |
| 1453 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Are year-end adjustments required? |
| 1467 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.3 Voluntary Contributions & Private Schemes |
| 1470 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Can employees and employers make additional voluntary contributions? |
| 1482 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Which employee contributions are allowed as pre-tax deductions? |
| 1505 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Are there private insurance schemes with employer and employee contributions? |
| 1524 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;What documents or declarations are required from an employee? |
| 1538 | &nbsp;&nbsp;&nbsp;&nbsp;Module 6: Income Tax Withholding System |
| 1541 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.0 Resident and Non-Resident Treatment Matrix |
| 1560 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.1 System Overview and Methodology |
| 1563 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Describe the country's income tax withholding system. |
| 1570 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;What types of taxes are withheld by the employer? |
| 1585 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;At what level are tax rates published (central or state)? |
| 1591 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.1.1 Taxable Income Definition |
| 1594 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Provide the statutory definition of 'Taxable Income'. |
| 1599 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Explain how this base is derived from total gross earnings. |
| 1623 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Deliverable: Provide a step-by-step decision guide to determine the correct tax schedule for an employee. |
| 1679 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Deliverable: Explain the official tax calculation method with formulas and examples. |
| 1725 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.2 Tax Rates and Logic |
| 1728 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;What are the latest tax rates by tax type, residential status, and payment frequency? |
| 1795 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;How are rates applied for different frequencies? |
| 1801 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;How does tax applicability and calculation logic differ by residential status? |
| 1815 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Provide the tax calculation logic covering eligibility, joining month, termination month, mid-month joining, mid-month terminations, and mid-month salary revisions. |
| 1830 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do tax rates vary by gender or age? |
| 1837 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;What is the minimum tax rate applicable? |
| 1850 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.3 Adjustments and Special Cases |
| 1853 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For annualized tax systems, which salary components must be projected? |
| 1865 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Are year-end tax adjustments required? |
| 1878 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Are there minimum or higher tax requirements if employees fail to submit a tax ID or social security number? |
| 1890 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;What is the income tax and social security refund procedure? |
| 1911 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Deliverable: Provide detailed worked examples for a standard resident employee, a non-resident employee, and an irregular payment. |
| 1984 | &nbsp;&nbsp;&nbsp;&nbsp;Module 7: Deductions, Exemptions & Benefits |
| 1987 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7.1 Statutory Tax Reliefs, Deductions, and Exemptions |
| 1990 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Deliverable: For each statutory tax relief, deduction, exemption, or other tax advantage, provide the name and definition, eligibility rules, statutory limits and amounts, calculation method, application point, and employee declaration requirements. |
| 2155 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Are salary sacrifice arrangements allowed? |
| 2169 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;List common types of post-tax deductions and any specific ordering rules or limitations. |
| 2192 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;List any income types that are statutorily exempt from income tax. |
| 2216 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7.2 Benefits in Kind (BIK) |
| 2219 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Are non-cash benefits taxed via the standard payroll system, or a separate employer-paid regime? |
| 2225 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;What is the definition of fringe benefits and how is the taxable amount evaluated? |
| 2248 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If a separate FBT regime exists, describe it in detail. |
| 2252 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;What is the calculation logic for fringe benefit tax? |
| 2276 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Are benefits-in-kind also subject to withholding tax? |
| 2280 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Which benefits-in-kind must be processed via payroll, and which require declarations? |
| 2295 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7.3 Garnishments and Court Orders |
| 2298 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;What are the rules for processing statutory deductions like child support, court-ordered fines, or tax levies? |
| 2320 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Is there a statutory priority order if an employee has multiple garnishments? |
| 2329 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Are there protected earnings limits? |
| 2363 | &nbsp;&nbsp;&nbsp;&nbsp;Module 8: Statutory Leave Management |
| 2366 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8.1 Leave Entitlements |
| 2369 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For each type of statutory leave, what are the eligibility criteria and accrual methodology? |
| 2415 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;How are unpaid or partially paid leaves handled? |
| 2432 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Which wage types are affected by unpaid/partially paid leave? |
| 2449 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Are there any mandatory national military service leaves? |
| 2460 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Are any other kinds of leave paid by government authorities? |
| 2477 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;What are the payout rules for statutory leaves? |
| 2504 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;How are unused paid leaves treated upon termination? |
| 2519 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Provide the calculation logic for each leave type where applicable. |
| 2557 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;How does extended unpaid leave impact social security contributions, tax status, and accrual? |
| 2575 | &nbsp;&nbsp;&nbsp;&nbsp;Module 9: Termination & Irregular Payments |
| 2578 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;9.1 Termination Payments |
| 2581 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;What are the different types of termination payments? |
| 2612 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;How do termination rules and calculations differ by residential status and employer type? |
| 2634 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Detail the calculation and tax withholding rules for unused leave paid out on termination. |
| 2658 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Describe the rules for statutory severance/redundancy payments. |
| 2679 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Provide the statutory formula for any tax-free portion. |
| 2699 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Deliverable: For other Employment Termination Payments (ETPs), provide a reference guide. |
| 2724 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Deliverable: Detail the rules for any applicable concessional tax cap. |
| 2754 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Deliverable: Provide a detailed worked example of a redundancy termination payout. |
| 2822 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;9.2 Irregular and Retrospective Payments |
| 2825 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Describe the specific tax calculation method required for irregular payments. |
| 2840 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;How are backdated payments and retrospective salary adjustments handled? |
| 2854 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For arrears, how are contributions and deductions computed? |
| 2869 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Deliverable: Provide a worked example of a bonus calculation. |
| 2912 | &nbsp;&nbsp;&nbsp;&nbsp;Module 10: Reporting, Compliance & Finalisation |
| 2916 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10.1 Statutory Reporting |
| 2919 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Describe the country's primary digital payroll reporting system. |
| 2974 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Deliverable: Provide a Data Disaggregation Mapping Guide describing the main reporting categories. |
| 3014 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;List all other mandatory reports, stating the frequency, file format, due date, reporting authority. |
| 3046 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;What pay elements are required as intermediates from payroll for reporting? |
| 3071 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10.2 Integrations |
| 3074 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Is there any mandatory inbound integration? |
| 3092 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Is there any mandatory outbound integration beyond standard reporting? |
| 3106 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10.3 Payslip Requirements |
| 3109 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;List all mandatory components that must be itemized on an employee payslip. |
| 3130 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10.4 Other Compliance |
| 3133 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Is payroll software certification mandatory? |
| 3147 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10.5 Year-End Processing and Finalisation |
| 3150 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Describe the mandatory year-end finalisation process. |
| 3168 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;What documentation or annual statements must be provided to employees? |
| 3182 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Is there a formal process for correcting errors discovered after the fiscal year has been closed? |
| 3198 | &nbsp;&nbsp;&nbsp;&nbsp;Module 11: Advanced Scenarios & Cross-Cutting Logic |
| 3201 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;11.1 Calculation Logic |
| 3204 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;How is the proration and projection logic applied for income tax, social security, exemptions, and deductions? |
| 3225 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If tax or contribution rates change mid-pay period, which rates apply? |
| 3241 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;How are tax and social security handled when an employee is paid multiple times in a single pay period? |
| 3255 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;How is payroll calculated if an employee's pay cycle changes mid-year? |
| 3270 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;11.2 Special Employee Groups & Income |
| 3273 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;How does taxation and social security differ for part-time employees and Board of Directors? |
| 3299 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;How is taxation handled for employees with multiple employers? |
| 3318 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;What is the treatment of foreign-sourced employment income for residents? |
| 3331 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;How do employer stock option plans work and how are they taxed? |
| 3361 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;How is payroll handled for employees who transfer between different legal entities mid-year? |
| 3389 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;What is the process for an employee who changes citizenship or residency status during the fiscal year? |
| 3406 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Are there specific rules for expatriates or inpatriates? |
| 3426 | &nbsp;&nbsp;&nbsp;&nbsp;Module 12: Gross-to-Net Worked Examples |
| 3429 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;12.1 Comprehensive Gross-to-Net Examples |
| 3434 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Deliverable: Example 1 — A full-time resident employee on a standard salary |
| 3505 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Deliverable: Example 2 — A casual or part-time employee |
| 3555 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Deliverable: Example 3 — An employee with a pre-tax deduction |
| 3605 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Deliverable: Example 4 — An employee with a student loan or other special tax obligation |
| 3644 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Deliverable: Example 5 — Other complex scenarios that are common in the country: a managerial employee above the ceiling with a company vehicle |
| 3691 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Deliverable: Example 6 — Other complex scenarios that are common in the country: an Alsace-Moselle employee with overtime |
| 3761 | &nbsp;&nbsp;&nbsp;&nbsp;Module 13: Common Business Practices & Non-Statutory Rules |
| 3764 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;13.1 Common Business Practices |
| 3767 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Describe the common practice for off-cycle or ad-hoc payments. |
| 3794 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;How are non-recoverable draws against future commissions typically handled? |
| 3820 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Are there common non-statutory leave types? How are they managed and reported? |

---

France Country Configuration Guide — FR-CCG-001 v1.0
Country Configuration Guide
Income year 2026 — assessment year 2027
Currency: EUR  |  Country code: FR
Mercans Compliance Regulations Team
Version 1.0 — 26 August 2026
Scope: the French general social security scheme (régime général) for private-sector employment. The sector-specific schemes (régimes spéciaux) are out of scope and are listed in scope_manifest.json.

## Table of Contents

Right-click and select 'Update Field' to build the table of contents.

## Module 1: Foundational Jurisdictional Parameters


### 1.1 Fiscal, Currency, and Language


#### What is the statutory tax year?

The statutory tax year for individuals in France is the calendar year: 1 January to 31 December (General Tax Code (Code général des impôts, CGI), Article 12). Income received in a calendar year is taxed by reference to that year, and the annual income tax return covering it is filed in the spring of the following year.
Payroll follows the same calendar-year cycle. The withholding-at-source system (prélèvement à la source, PAS) operates month by month within the calendar year under CGI Article 204 A; social security contributions are assessed per calendar year, with both the annual ceiling and the annual contribution-relief calculation resetting on 1 January; and the monthly social declaration (Déclaration Sociale Nominative, DSN) is filed per calendar month.
One consequence matters for 2026 specifically. Because the 2026 Finance Act (LOI n° 2026-103 of 19 February 2026) was enacted after 1 January, two different default withholding grids apply inside the same tax year — the 2025 grid from January to April and the 2026 grid from 1 May. This is set out in Module 6 and must be configured as two rate tables within a single fiscal year, not one.

#### Can employers adopt an alternate tax year? If yes, under what circumstances and what are the implications?

No. The individual tax year is fixed by statute as the calendar year and cannot be varied by the employer, by the employee, by collective agreement or by contract. There is no election, no approval route and no transitional-period mechanism.
A company may close its accounting year on a date other than 31 December for corporate income tax purposes, and many do. This has no effect whatsoever on payroll: the withholding-at-source rates supplied by the tax administration, the social security ceiling, the annual contribution-relief calculation and the DSN calendar all remain aligned to the calendar year. The only practical consequence for system configuration is that a client whose financial year is not the calendar year needs its payroll-to-general-ledger postings mapped to its own accounting periods, while every statutory output stays on the calendar year.

#### What is the official currency for payroll processing and reporting? Provide the ISO code.

The euro, ISO 4217 code EUR, with two decimal places (cents). France has used the euro as sole legal tender since 1 January 2002.
Wages must be paid in euro. Labour Code (Code du travail) Article L3241-1 restricts the permitted payment methods: salary may be paid in cash, by crossed cheque or by bank transfer to an account of which the employee is the holder or joint holder, but where net monthly pay exceeds EUR 1,500 cash payment is prohibited and settlement must be by crossed cheque or transfer. The same threshold applies to a mid-month advance (acompte).
All statutory outputs — the DSN, the withholding-at-source remittance to the public finances directorate (Direction Générale des Finances Publiques, DGFiP), the payroll tax return and the payslip — are denominated in euro.

#### What is the official language for statutory reports and employee payslips?

French, and this is a legal requirement rather than a convention. Labour Code Article L1321-6 provides that any document containing obligations for the employee, or provisions whose knowledge is necessary for the performance of the work, must be drafted in French. The payslip (bulletin de paie) is such a document and must therefore be issued in French, as must the internal rules, the employment contract and every statutory declaration.
Three qualifications matter for a multinational client.

| Situation | Rule | Legal basis |
|---|---|---|
| Employee is a foreign national | The employee may require a translation of the employment contract into their own language; in a dispute only the foreign-language version may be relied on against the employee | Labour Code Article L1221-3 |
| Document received from abroad, or intended for a non-French-speaking foreign national | The French-language obligation does not apply | Labour Code Article L1321-6, third paragraph |
| Statutory filings (DSN, PAS, payroll tax return, disabled-worker employment return) | French only; there is no alternative-language channel | Practice of the collecting bodies (URSSAF, DGFiP) |

An English payslip is therefore never sufficient on its own. English may be provided as an additional courtesy document alongside the legally valid French one, and many international employers do exactly that, but the French version is the payslip in law.
Legal basis: General Tax Code, Articles 12 and 204 A; LOI n° 2026-103 of 19 February 2026 (Finance Act for 2026); Labour Code, Articles L1221-3, L1321-6, L3241-1 and L3243-2.

### 1.2 Pay Cycles and Dates


#### What are the permissible payroll payment frequencies in the country?

France is a monthly-payroll country by statute. Labour Code Article L3242-1 imposes monthly payment (mensualisation) as the default and, importantly, provides that pay is independent of the number of days actually falling in the month for a given contractual working time — this is the basis of the smoothed 151.67-hour month described in Module 4.

| Population | Permitted frequency | Legal basis |
|---|---|---|
| Employees generally | Once per month | Labour Code Article L3242-1 |
| Any employee who requests it | A mid-month advance (acompte) equal to half the monthly pay, in addition to the monthly settlement — a right, not a discretion | Labour Code Article L3242-1, second paragraph |
| Home workers, seasonal workers, intermittent and temporary workers | At least twice per month, at intervals of no more than 16 days | Labour Code Article L3242-3 |
| Employees paid by piece or by task where the work spans more than a fortnight | Fortnightly instalments on account, with settlement at completion | Labour Code Article L3242-3 |

Weekly payroll is not a recognised French cycle for ordinary employment. Where a client asks for it, the correct configuration is a monthly cycle plus an acompte, not a weekly cycle.
The acompte is a payment on account, not a separate pay period. It generates no separate payslip, no separate DSN and no separate withholding calculation; it is netted off against the month's single payslip. Configuring it as a second pay run is a common and expensive modelling error.

#### For each frequency, detail the corresponding statutory reporting and payment deadlines for both income tax withholding and social security contributions.

Reporting deadlines in France do not follow the pay frequency. Every employer, whatever its pay cycle, files one DSN per calendar month, and both the social security contributions and the withheld income tax are declared inside that same DSN. The deadline depends on headcount, not on how often wages are paid.

| Obligation | Authority / channel | Periodicity | Deadline |
|---|---|---|---|
| DSN (social contributions and withheld income tax combined) — employers with 50 or more employees | URSSAF, via net-entreprises.fr | Monthly | The 5th of the month following the pay month |
| DSN — employers with fewer than 50 employees | URSSAF, via net-entreprises.fr | Monthly | The 15th of the month following the pay month |
| Social security contribution payment — 50 or more employees | URSSAF | Monthly | The 5th, with the DSN |
| Social security contribution payment — fewer than 50 employees | URSSAF | Monthly | The 15th, with the DSN |
| Social security contribution payment — fewer than 11 employees, on option | URSSAF | Quarterly | The 15th of the month following the quarter; the DSN itself remains monthly |
| Withholding at source (PAS) remittance — 50 or more employees | DGFiP, by direct debit initiated from the DSN | Monthly | The 8th of the month following the pay month |
| Withholding-at-source remittance — fewer than 50 employees | DGFiP | Monthly | The 18th of the month following the pay month |
| Withholding-at-source remittance — fewer than 11 employees, on option | DGFiP | Quarterly | The 18th of the month following the quarter |
| Supplementary pension contributions (Agirc-Arrco) | Agirc-Arrco institutions, through the same DSN | Monthly | Same deadline as the URSSAF DSN |
| Pre-hire declaration (Déclaration Préalable À l'Embauche, DPAE) | URSSAF | Per event | Within the eight days preceding the hire, and in any event before the employee starts work |
| Event notifications (end of contract, work stoppage) | DSN event signal (signalement d'événement) | Per event | Within 5 days of the event |

Two configuration points follow. First, there is no separate income-tax return for payroll: the PAS is declared inside the DSN and collected by direct debit, so a failure in the DSN is simultaneously a social security failure and a tax failure. Second, the quarterly option for employers with fewer than 11 employees changes the payment rhythm only — the monthly DSN obligation is unaffected.

#### Describe the statutory rule for handling pay dates that fall on a weekend or public holiday.

Two distinct rules apply and must not be conflated.
For statutory filing and payment deadlines — the DSN, the URSSAF payment and the PAS remittance — where the deadline falls on a Saturday, Sunday or public holiday it is postponed to the next working day. This is the general administrative rule and it is applied by both URSSAF and DGFiP to the DSN calendar.
For payment of wages to employees there is no postponement rule. Article L3242-1 requires payment once a month, and the settled interpretation is that the interval between two payments may not exceed one month. A pay date falling on a Saturday, Sunday or bank holiday must therefore be brought forward to the preceding banking day, not deferred. In practice payroll providers schedule the SEPA credit transfer so that funds are available to the employee on or before the contractual pay date, and the internal rules or the collective agreement normally state that where the fixed date is not a banking day the payment is executed on the preceding banking day.
The distinction matters because deferring a wage payment past month end can, in a dispute, be characterised as late payment of wages, whereas deferring a DSN to the next working day is expressly permitted.

#### What are the common payroll pay dates and cut-off dates for payroll processing?

There is no statutory pay date; it is fixed by the employment contract, the collective agreement or the internal rules, and once fixed it must be respected consistently.

| Population | Common pay date | Common cut-off for variable data |
|---|---|---|
| Salaried staff (managerial grade (cadres) and non-managerial) on a smoothed monthly salary | The last working day of the month, or between the 25th and month end | Between the 10th and the 20th of the pay month |
| Employees with significant variable pay (overtime, bonuses, allowances) | The first days of the following month, with variable elements paid one month in arrears | Month end of the reference month |
| Hourly-paid and site-based populations (construction, hospitality) | Between the 1st and the 5th of the following month | Month end |

The dominant French market practice is to pay a smoothed fixed salary at or near month end for the current month, and to pay variable elements — overtime, absences, bonuses, expense reimbursements — one month in arrears. This "current fixed, arrears variable" split is the single most important design assumption in a French payroll implementation, because it drives the timing of the withholding-at-source calculation, the treatment of a mid-month leaver, and every reconciliation between the DSN and the general ledger.
Legal basis: Labour Code, Articles L3242-1, L3242-3 and L3241-1; Social Security Code (Code de la sécurité sociale, CSS), Articles R243-6 and following; General Tax Code, Articles 204 A and 1671.

### 1.3 Extra Pay Period Handling


#### Describe the statutory handling and calculation adjustments required for fiscal years containing extra pay periods (e.g., 53 weekly pays).

The 53-pay-period problem does not arise in French payroll, because the statutory cycle is monthly and a calendar year contains exactly twelve monthly periods. There is no weekly or fortnightly statutory cycle for ordinary employees, and consequently no year in which a 53rd period can occur.
The French analogue of the problem is different in kind and must not be modelled as an extra period: it is the smoothing of the monthly salary under Article L3242-1. A full-time employee on the 35-hour statutory week is paid for 151.67 hours every month regardless of whether the month contains 20, 21, 22 or 23 working days. The figure derives as 35 hours × 52 weeks ÷ 12 months = 151.666…, conventionally written 151.67. Because the salary is by law independent of the number of days in the month, no annual true-up is required and no thirteenth period is generated.
Where a client's legacy system carries a 53-period concept, the correct migration treatment is to collapse it to twelve monthly periods and to recompute the monthly rate as annual pay ÷ 12.

#### Detail the impact on annualized tax calculations and social security contributions.

Because there is no extra period, there is no distortion to correct. Two genuinely annual mechanisms nonetheless need to be understood, and both operate on a twelve-month calendar-year basis.

| Mechanism | How the annual dimension works | Detailed in |
|---|---|---|
| Social security ceiling (plafond de la sécurité sociale) | The monthly ceiling of EUR 4,005 is applied month by month, then reconciled cumulatively against the annual ceiling of EUR 48,060 through the progressive ceiling reconciliation (régularisation progressive des plafonds) | Module 5.2 |
| Unified degressive general reduction (réduction générale dégressive unifiée, RGDU) | Calculated on annual gross pay, applied provisionally each month and reconciled cumulatively across the year | Module 5.2 |

Both mechanisms assume twelve monthly periods sharing a common reference to the calendar year. If a client operates a non-standard cycle for the populations permitted under Article L3242-3, the ceiling and the RGDU are still computed on the calendar year and the periodic figures are prorated to the employment period, not to the number of pay events.

#### If optional adjustment methods are permitted, provide a step-by-step guide.

Not applicable in the 53-period sense. The one election that genuinely exists in French payroll and is often confused with it is the choice of ceiling reconciliation method, and a payroll implementation must make it explicitly.
1. Establish the reconciliation basis. For each employee, accumulate from 1 January (or from the hire date within the year) the gross pay subject to contributions and the ceiling entitlement for the same periods.
1. Compute the cumulative ceiling. Cumulative ceiling = the sum of the monthly ceilings for the months in the accumulation, each prorated where the employee was present for only part of the month, worked part-time, or had unpaid absence.
1. Compare and reconcile. Compare cumulative gross to cumulative ceiling. Split the cumulative gross into the capped band and the uncapped excess, apply the year-to-date contribution rates, and deduct the contributions already declared in earlier months. The difference — positive or negative — is the current month's adjustment.
1. Choose the frequency. The reconciliation may be performed every month (progressive reconciliation, the market standard and the method assumed throughout this guide) or once at the year end or at departure (annual reconciliation). Progressive reconciliation is strongly preferred because it prevents a large December correction and because it produces DSN figures that reconcile month by month.
1. Handle departures. On termination, run the reconciliation to the leaving date in the final payslip; do not defer it to the year end.
Legal basis: Labour Code, Article L3242-1; Social Security Code, Articles R242-2 and D242-1 and following; Arrêté of 22 December 2025 fixing the social security ceiling for 2026.

### 1.4 Holiday Calendar


#### What are the official public holidays?

Eleven public holidays (jours fériés) are listed for the whole territory by Labour Code Article L3133-1. Their 2026 dates are:

| Holiday | 2026 date | Day of week |
|---|---|---|
| New Year's Day (Jour de l'An) | 1 January 2026 | Thursday |
| Easter Monday (Lundi de Pâques) | 6 April 2026 | Monday |
| Labour Day (Fête du Travail) | 1 May 2026 | Friday |
| Victory in Europe Day (Victoire 1945) | 8 May 2026 | Friday |
| Ascension Day (Ascension) | 14 May 2026 | Thursday |
| Whit Monday (Lundi de Pentecôte) | 25 May 2026 | Monday |
| National Day (Fête nationale) | 14 July 2026 | Tuesday |
| Assumption (Assomption) | 15 August 2026 | Saturday |
| All Saints' Day (Toussaint) | 1 November 2026 | Sunday |
| Armistice Day (Armistice 1918) | 11 November 2026 | Wednesday |
| Christmas Day (Noël) | 25 December 2026 | Friday |

Only 1 May is a compulsory non-working, fully paid holiday for all employees with no length-of-service condition (Labour Code Articles L3133-4 to L3133-6); where the nature of the activity makes interruption impossible, work on 1 May carries a 100 % premium, that is, double pay. For the other ten, non-working status depends on the collective agreement or on custom; where the day is not worked, pay is maintained for employees with at least three months' service with the employer (Article L3133-3).
Two of the eleven fall on a weekend in 2026 — Assumption on a Saturday and All Saints' Day on a Sunday. French law confers no right to a substitute day off, and no compensating payment is due unless the collective agreement provides one. This is a frequent source of client queries and the answer is negative by default.

#### Are there any regional, state-specific, or company-specific holidays?

Yes, in three distinct ways.

| Category | Detail | Legal basis |
|---|---|---|
| Alsace-Moselle (Bas-Rhin, Haut-Rhin, Moselle) | Two additional public holidays: Good Friday (3 April 2026) and Saint Stephen's Day (26 December 2026), giving thirteen in total | Labour Code Articles L3134-13 and L3134-16 |
| Overseas departments | An additional holiday commemorating the abolition of slavery, on a date specific to each territory — for example 27 May in Guadeloupe, 22 May in Martinique, 10 June in Guyane, 20 December in La Réunion, 27 April in Mayotte | Décret n° 83-1003 of 23 November 1983 |
| Collective agreement or company custom | A sector or company agreement may add days off or make a listed holiday compulsorily non-working; established custom can create an enforceable entitlement | Labour Code Article L3133-3-1 |

A separate mechanism must not be confused with a holiday: the solidarity day (journée de solidarité), created by the Act of 30 June 2004 and now Labour Code Article L3133-7. It requires seven additional hours of work per year, unpaid, to fund support for elderly and disabled people. Its date is set by collective agreement or, failing that, by the employer; Whit Monday is the traditional but no longer the default choice. For payroll the effect is that up to seven hours are worked without additional pay and are not counted as overtime.
Legal basis: Labour Code, Articles L3133-1, L3133-3, L3133-3-1, L3133-4 to L3133-6, L3133-7, L3134-13 and L3134-16; Décret n° 83-1003 of 23 November 1983.

### 1.5 Rounding and Precision Rules


#### What are the statutory or common business practice rules for rounding final net pay and individual calculation components?

France applies different rounding rules at different points of the calculation, and applying a single rule throughout is a defect.

| Item | Rule | Basis |
|---|---|---|
| Individual payslip lines (bases, rates, amounts) | Two decimals, rounded half-up to the nearest cent | Market practice; no statutory rule, but the payslip must be arithmetically verifiable |
| Aggregated social security contributions declared and paid to URSSAF | Rounded to the nearest whole euro, a fraction of exactly 0.50 counting as 1 | Social Security Code Article L130-1 |
| Nominative (per-employee) data inside the DSN | Not rounded — carried at two decimals exactly as calculated | DSN technical specification; only the aggregate blocks take the Article L130-1 rounding |
| Withholding at source (PAS) — the amount remitted to DGFiP | Rounded to the nearest whole euro, 0.50 counting as 1.00 | General Tax Code Article 204 H and the DSN withholding guide |
| Withholding-at-source rate supplied by DGFiP | Applied exactly as transmitted, to two decimals | General Tax Code Article 204 H |
| Net pay to the employee | Two decimals | Market practice |
| Social security ceiling prorated for a part period or part-time work | Two decimals, rounded to the nearest cent | Social Security Code Article R242-2 |

The trap worth naming: the whole-euro rounding of Article L130-1 applies to the aggregate contribution blocks, not to the individual employee lines. A system that rounds each employee's contribution to the euro and then sums will not reconcile to a system that sums at the cent and rounds once — and only the second is correct.

#### What level of decimal precision is required for statutory reporting?


| Report | Precision required |
|---|---|
| DSN — nominative amount fields (remuneration block S21.G00.51, contribution base block S21.G00.78 and equivalents) | Two decimals |
| DSN — aggregate contribution blocks (S21.G00.23 and following) | Whole euro, per Social Security Code Article L130-1 |
| DSN — withholding block (net taxable amount, applied rate, withheld amount in S21.G00.50) | Net taxable amount and withheld amount to two decimals per employee; rate to two decimals; the aggregate remittance to the whole euro |
| Payroll tax return (déclaration de la taxe sur les salaires, form 2502) | Whole euro |
| Disabled-worker employment return, filed inside the DSN | Whole units for headcount, whole euro for the contribution |
| Payslip | Two decimals throughout, including the hourly rate and every contribution rate |

Legal basis: Social Security Code, Articles L130-1 and R242-2; General Tax Code, Article 204 H; DSN technical specification (cahier technique de la norme DSN), 2026 version.

## Module 2: Master Data Configuration

This module gives the configuration-level summary of the employer and employee data France requires. The field-by-field definitions, formats, validation rules and option mappers are held in the France Data Dictionary (FR-DD-001) and are deliberately not reproduced here.

### 2.1 Employer Information


#### What are the different boards or authorities where an employer must register?

An employer operating in France registers once through a single electronic window and is then known to several bodies, each of which issues or uses a different identifier. All company-formation and modification formalities have been routed through the single formalities window (guichet unique des formalités des entreprises) operated by the National Industrial Property Institute (Institut National de la Propriété Industrielle, INPI) since 1 January 2023.

| Authority | What it does for payroll | Identifier used |
|---|---|---|
| National Institute of Statistics and Economic Studies (INSEE) | Allocates the business and establishment identifiers and the activity code on which the industrial-accident rate and several sector rules depend | SIREN, SIRET, activity code (code APE / NAF) |
| URSSAF (network of social contribution collection bodies) | Collects social security contributions, the unemployment contribution, the wage guarantee contribution, the training and apprenticeship contributions and the mobility levy; receives the DSN | Contributor account (compte cotisant), keyed on the SIRET |
| Public Finances Directorate (DGFiP) | Collects the income tax withheld at source and, where applicable, the payroll tax | SIREN; intra-Community VAT number for other purposes |
| Agirc-Arrco supplementary pension scheme | Mandatory supplementary pension for all private-sector employees; the employer must be affiliated to a member institution | Membership number with the institution |
| Occupational health and prevention service (Service de Prévention et de Santé au Travail, SPST) | Mandatory affiliation; medical examinations | Membership number |
| Insurer for the compulsory health cover, and where applicable death-and-disability cover | Mandatory collective health cover; managerial-grade death-and-disability cover | Policy number |
| France Travail (public employment service) | Receives end-of-contract data through the DSN; unemployment entitlement | SIRET |
| Sector paid-leave fund (caisse de congés payés), in construction and public works, entertainment, dockers and transport | In these sectors paid leave is paid by the fund, not by the employer — a decisive payroll design difference | Membership number with the fund (for example a CIBTP fund) |

The paid-leave fund line deserves emphasis. In the construction and public works sector and in the entertainment sector the employer pays a contribution to the fund and the fund pays the employee's holiday pay. A payroll engine configured on the general-regime assumption that the employer pays holiday pay will be wrong for these clients in both the payslip and the DSN.

#### What is the configuration/format of registration numbers allotted by each authority?


| Identifier | Format | Notes |
|---|---|---|
| SIREN | 9 digits | Identifies the legal entity. Constant for the life of the entity, unaffected by relocation or change of activity. Carries a Luhn check |
| SIRET | 14 digits = SIREN (9) + establishment sequence (NIC, 5) | Identifies a specific establishment. Changes when the establishment moves to another commune. Carries a Luhn check |
| NIC (numéro interne de classement) | 5 digits, the last being a check digit | The establishment sequence inside the SIRET |
| Activity code (APE / NAF) | 4 digits + 1 letter, for example 6201Z | Assigned by INSEE. Drives the presumed sector agreement, several sector levies and the industrial-accident risk classification |
| URSSAF contributor account | Assigned by URSSAF and keyed on the SIRET | Quoted on every DSN and on every payment |
| Intra-Community VAT number | FR + 2-character key + SIREN (9 digits) | Not a payroll identifier, but frequently requested on the same onboarding form |
| Collective agreement identifier (IDCC) | 4 digits | Identifies the applicable sector agreement. Mandatory on the payslip and in the DSN |
| Industrial-accident risk code | 5 characters (3 digits + 2 letters) with an associated net rate | Assigned per establishment and per activity by the regional sickness-insurance fund |

Two of these are not registration numbers in the strict sense but behave like them in payroll configuration and must be captured per establishment: the collective agreement identifier (IDCC) and the industrial-accident risk code with its rate. Both are mandatory outputs.

#### Are registration numbers allotted at the central level or at the state/township level?

France is a unitary state and social security is organised nationally, so the identifiers are national — but several of them are allocated and several rates are set per establishment, which is the practical equivalent of a local level for configuration purposes.

| Level | What is fixed at that level |
|---|---|
| Legal entity (SIREN) | Legal identity, VAT, corporate reporting, headcount thresholds (the headcount is assessed at entity level, not establishment level) |
| Establishment (SIRET) | Industrial-accident risk code and net rate; mobility levy rate, which depends on the establishment's commune; the sector paid-leave fund; the occupational health service; the DSN establishment block |
| National | Contribution rates, the social security ceiling, the income tax scale and withholding grids, the statutory minimum wage |

There are two genuine territorial regimes that change the contribution set rather than merely the rate:
- Alsace-Moselle (Bas-Rhin, Haut-Rhin, Moselle): employees working in these departments pay an additional employee health contribution — 1.30 % of total remuneration for 2026, unchanged from 2025 by decision of the local scheme's board — and benefit from two extra public holidays. The trigger is the place of work, not the employee's residence.
- Overseas departments (Guadeloupe, Martinique, Guyane, La Réunion, Mayotte): reduced non-resident withholding rates, specific exemption schemes, and a different public holiday.
Legal basis: Labour Code, Articles L1221-16, R1221-1 and following; Social Security Code, Articles L242-1, L243-1-2, D242-6-1 and following; Local Alsace-Moselle scheme, Social Security Code Articles L325-1 and D242-10; General Tax Code, Article 1671.

### 2.2 Employee Information


#### What are the different residential statuses for an individual?

France operates two independent status tests, and confusing them is a classic source of error because an individual can be a French tax resident but affiliated to a foreign social security scheme, or the reverse.

| Test | Statuses | Criterion | Legal basis |
|---|---|---|---|
| Tax residence | Resident (domicilié fiscalement en France) / Non-resident | Any one of: household or principal place of stay in France; professional activity carried on in France as the main activity; centre of economic interests in France — subject to the applicable double tax treaty | General Tax Code Article 4 B |
| Social security affiliation | Affiliated to the French scheme / Posted worker (travailleur détaché) covered by a foreign scheme / Expatriate (expatrié) outside the French scheme | Place where the work is physically performed, subject to EU Regulation 883/2004 or a bilateral social security agreement, evidenced by a portable document A1 or the equivalent certificate | Social Security Code Article L111-2-2; EU Regulation (EC) No 883/2004 |

For payroll, the tax residence status determines the income-tax mechanism — withholding at source under the personal or default rate for a resident, and the specific non-resident withholding of General Tax Code Article 182 A for a non-resident (Module 6). The social security affiliation status determines whether French contributions are due at all.
A third status affects only the employer's contribution calculation and is worth capturing at master-data level: managerial grade (statut cadre). It has no separate pension scheme since the 2019 Agirc-Arrco merger, but it still governs the compulsory 1.50 % employer death-and-disability contribution on the first band of pay, membership of the executive employment association, and many collective-agreement entitlements including the notice period.

#### What employee fields are required for processing payroll and statutory reporting?

The complete field list, with formats and validation, is in the France Data Dictionary. At configuration level the mandatory data falls into six groups.

| Group | Content | Why it is mandatory |
|---|---|---|
| Identity | Social security number (NIR) or a temporary technical number, family name at birth and used name, given names, sex, date and place of birth, country of birth | DSN individual block; without a valid NIR the entitlement cannot be posted to the employee's record |
| Contact and banking | Postal address, IBAN and BIC of an account the employee holds or jointly holds | Payment method under Labour Code Article L3241-1 |
| Contract | Contract type, start date, end date and reason for a fixed-term contract, occupational category code, collective agreement identifier, workplace establishment SIRET, job title, managerial-grade flag | DSN contract block; drives the contribution set and the notice and severance rules |
| Working time | Contractual weekly or monthly hours, part-time percentage, day-count arrangement (forfait jours) where applicable, work pattern | Ceiling proration, minimum wage test, overtime, and the unified reduction calculation |
| Tax | Withholding rate transmitted by the tax administration, its validity period and type (personal, individualised, default), tax residence status | Withholding at source |
| Statutory add-ons | Disabled-worker recognition, apprenticeship or work-study status, health-cover exemption evidence, garnishment orders, public transport season ticket, prior-employer end-of-contract certificate | Employment-obligation return, exemptions, deductions |


#### What is the configuration/format of registration numbers (e.g., tax ID, social security number) allotted to employees?


| Identifier | Format | Structure and validation |
|---|---|---|
| Social security number (numéro d'inscription au répertoire, NIR) | 15 characters: 13 digits + a 2-digit key | Position 1: sex (1 male, 2 female). Positions 2–3: year of birth. Positions 4–5: month of birth. Positions 6–7: department of birth. Positions 8–10: commune of birth. Positions 11–13: order number within the birth register. The 2-digit key = 97 − (the 13-digit number modulo 97). For births in Corsica the department codes 2A and 2B are converted by substituting A = 0 and B = 0 and subtracting 1,000,000 and 2,000,000 respectively before computing the key |
| Temporary technical number (numéro technique temporaire, NTT) | Up to 40 characters, conventionally the SIRET followed by an internal sequence | Used in the DSN when the NIR is not yet known, for example for a newly arrived foreign employee. It must be replaced by the NIR as soon as it is issued; a contract left on an NTT beyond a few months generates a DSN anomaly |
| Tax reference number (numéro fiscal / SPI) | 13 digits | Held by the individual, not by the employer. The employer does not need it: the withholding rate is delivered by the tax administration keyed on the NIR |
| Withholding rate identifier | Rate to two decimals, with a validity period and a rate-type code | Delivered in the DSN return flow (compte rendu métier) |

The design point to carry into the Data Dictionary: the employer never captures the employee's tax number. The link between the employee and their tax file is made by the tax administration itself from the NIR and civil-status data transmitted in the DSN. A field asking the employee for their tax number is both unnecessary and, under data-minimisation principles, questionable.

#### Provide any relevant combo values or sample inputs for each field.

Illustrative values only; the authoritative code lists are in the Data Dictionary option mappers.

| Field | Sample or permitted values |
|---|---|
| Social security number | 1 85 03 75 116 042 21 — male, born March 1985, Paris (75), commune register 116, order 042, key 21 |
| SIRET of the workplace | 552 100 554 00021 |
| Collective agreement identifier | 1486 (consultancy and engineering), 1090 (motor trade), 3239 (metalworking) |
| Contract type | Permanent contract (CDI), fixed-term contract (CDD), apprenticeship contract, professionalisation contract, temporary-agency assignment |
| Occupational category | Executive, engineer or manager; supervisor or technician; clerical or administrative employee; manual worker |
| Working-time arrangement | 35 hours per week (151.67 hours per month); 218-day annual day-count arrangement; part-time at 80 % (121.33 hours per month) |
| Withholding rate type | Personal rate (taux personnalisé); individualised rate (taux individualisé); default rate (taux non personnalisé) |
| Withholding rate value | 7.50 % |
| Health cover status | Member; exempt — covered as a dependant under a spouse's compulsory scheme; exempt — fixed-term contract shorter than three months with individual cover |


#### What previous employment information must new joiners declare?

France has no carry-forward of cumulative payroll figures between employers. Each employer restarts the social security ceiling, the unified reduction calculation and the contribution-base caps at zero on the hire date. What the new joiner must supply is therefore documentary rather than numerical.

| Item | Why it is needed | Consequence if missing |
|---|---|---|
| Social security number | Every declaration and entitlement | Contract must be declared on a temporary technical number, generating recurring DSN anomalies |
| End-of-contract certificate from the previous employer (attestation France Travail, now transmitted through the DSN) | Confirms the end date and the reason, needed where a notice period overlaps | Risk of overlapping declarations for the same period |
| Final settlement statement (solde de tout compte) from the previous employer | Shows whether accrued paid leave was already paid out | Risk of paying the same leave entitlement twice |
| Evidence supporting an exemption from the compulsory health cover | The exemption is only lawful if evidenced and renewed annually | Employer contribution wrongly omitted, and a contribution adjustment on inspection |
| Any wage garnishment order in force | Garnishments follow the employee, not the employer | Employer personally liable to the creditor |
| Disabled-worker recognition, where the employee wishes to declare it | Counts toward the employment obligation and reduces the annual contribution | Overstated contribution |
| Public transport season ticket | Compulsory 50 % employer reimbursement | Breach of Labour Code Article L3261-2 |
| Apprenticeship or work-study certificate | Different contribution and tax treatment | Wrong contribution set |

Two things the employee does not need to supply: the previous employer's payslips, because there is no cumulative carry-forward; and the withholding rate, because the tax administration transmits it directly. Until that rate arrives — typically in the return flow following the first DSN — the employer applies the default grid.
Legal basis: General Tax Code, Articles 4 B and 204 H; Social Security Code, Articles L111-2-2, L114-12-1 and R115-1; Labour Code, Articles L1234-19, L3241-1 and L3261-2; EU Regulation (EC) No 883/2004.

### 2.3 Data Management and Retention


#### What are the statutory requirements for payroll record retention (e.g., number of years)?


| Record | Retention period | Legal basis |
|---|---|---|
| Payslip — employer's copy, paper form | 5 years | Labour Code Article L3243-4 |
| Payslip — issued in electronic form | Availability must be guaranteed for 50 years, or until the employee reaches the age of 75, whichever is later | Labour Code Article D3243-8 |
| Single staff register (registre unique du personnel) | 5 years from the date the employee left the establishment | Labour Code Article R1221-26 |
| Working-time records, on-call and rest records | 1 year | Labour Code Article D3171-16 |
| Records supporting social security contributions, including the DSN | 6 years | Social Security Code Article L243-16; recovery is barred after 3 years plus the current year, and the CNIL human-resources reference framework sets 6 years as the intermediate-archiving period |
| Employment contracts, and evidence relating to pay and leave | 5 years, matching the general limitation period for pay claims | Civil Code Article 2224; Labour Code Article L3245-1 |
| Accounting books and supporting documents including payroll journals | 10 years | Commercial Code Article L123-22 |
| Industrial-accident declarations | 5 years | Social Security Code Article D242-6-1 and following |

The 50-year rule for electronic payslips is the one most often missed in a system design. If the client elects electronic payslips — which requires informing the employee, who may object — the archiving obligation is on the employer or its service provider and survives the end of the service contract. A five-year retention setting on an electronic payslip archive is a breach.

#### Are there specific data privacy laws (like GDPR) that govern the storage and handling of employee payroll data?

Yes. Three layers apply cumulatively.

| Layer | Instrument | What it adds for payroll |
|---|---|---|
| European | Regulation (EU) 2016/679 (GDPR) | Lawful basis, minimisation, storage limitation, security, records of processing, data subject rights, and a data protection impact assessment where large-scale processing of employee data is involved |
| National | Act n° 78-17 of 6 January 1978 on data processing and liberties, as amended | Supplements the GDPR; gives the national data protection authority (Commission Nationale de l'Informatique et des Libertés, CNIL) its powers |
| Sectoral guidance | CNIL human-resources reference framework on retention periods, and CNIL guidance on staff management | Sets the retention periods used in the table above and is the benchmark used in an inspection |

Four practical consequences for a payroll implementation:
1. Lawful basis. Payroll processing rests on the performance of the contract and on legal obligation, not on consent. Consent is not a valid basis for core payroll processing because it is not freely given in an employment relationship.
1. Minimisation. Fields must be justified. Collecting a bank card number, marital status beyond what benefits require, or the employee's tax reference number is not justifiable.
1. Special categories. Disabled-worker status and health data linked to sick pay are special-category data; they require a distinct justification, restricted access and separate retention.
1. Transfers outside the European Economic Area. If payroll is processed or supported from outside the EEA, a transfer mechanism is required. This is a live design question for any shared-service model and must be settled before go-live, not after.

#### How should historical payroll data (e.g., from a previous provider) be handled for cumulative calculations?

A change of payroll provider does not change the employer. The legal entity is the same, the SIREN is the same, and all cumulative mechanisms therefore continue uninterrupted across the changeover. Year-to-date figures must be migrated; restarting them mid-year overstates or understates several results.
The cumulative figures that must be loaded, and what breaks if they are not:

| Cumulative figure | Why it must be carried | Effect of restarting at zero |
|---|---|---|
| Gross pay subject to contributions, and the ceiling entitlement, since 1 January | Progressive ceiling reconciliation | Capped and uncapped bands recomputed from zero; contributions on the first pay band charged twice |
| Annual gross pay for the unified degressive reduction | The reduction is computed on annual pay | The reduction is recalculated as though the employee had joined mid-year, materially overstating the relief |
| Base subject to the general social contribution and the social debt repayment contribution, for the 1.75 % allowance capped at four annual ceilings | The allowance is capped annually | The allowance is granted twice on the same pay |
| Net taxable pay and tax withheld since 1 January | Employee's annual tax statement and the year-end statement of amounts withheld | Employee's pre-filled tax return is wrong |
| Overtime pay exempt from income tax, against the EUR 7,500 annual cap | The cap is annual and per employee | Exemption granted beyond the statutory cap |
| Paid-leave balances, by accrual period, in days and in value | Leave accrual and the leave-pay comparison rule | Leave under- or over-paid; balance wrong on termination |
| Length of service and seniority date | Severance, notice, and collective-agreement entitlements | Severance under-calculated |
| Value-sharing bonus already paid in the calendar year | Exemption caps are annual and per employee | Exemption granted beyond the cap |

The migration should be reconciled against the DSN already filed by the outgoing provider for the same periods, not against its payslips alone, because the DSN is what the collecting bodies hold. Any difference must be resolved before the first DSN filed by the incoming provider, since the DSN carries a cumulative dimension that the collecting bodies check.
Legal basis: Regulation (EU) 2016/679; Act n° 78-17 of 6 January 1978; Labour Code, Articles L3243-4, D3243-8, R1221-26, D3171-16 and L3245-1; Social Security Code, Article L243-16; Commercial Code, Article L123-22; CNIL reference framework on retention periods in human-resources management.

## Module 3: The Gross-to-Net Calculation Framework


### 3.1 Gross-to-Net Flow


#### Deliverable: Provide a definitive, step-by-step description or text-based flowchart illustrating the standard Gross-to-Net (G2N) calculation framework, and explain where employer on-costs are calculated in parallel.

French gross-to-net is a single-pass, multi-base calculation. Its defining characteristic — and the one that separates it from most other jurisdictions — is that there is no single "taxable income" figure. A French payslip carries at least five distinct bases, each built from gross pay by a different set of adjustments, and each feeding a different obligation:
1. the base subject to social security contributions, split into a capped band and an uncapped band;
1. the base subject to the general social contribution and the social debt repayment contribution, which is gross pay reduced by a capped 1.75 % allowance and then increased by employer contributions to supplementary cover;
1. the net social amount, a statutory payslip figure used by the benefits authorities;
1. the net taxable amount, which is the base for withholding at source;
1. the net payable to the employee.
A system that derives one from another by a simple offset will produce a payslip that does not survive an inspection.
#### Step 1 — Summation of gross earnings
Add every element of remuneration for the period:

| Component | Included in gross |
|---|---|
| Base salary for the contractual working time (151.67 hours for a full-time 35-hour week) | Yes |
| Overtime and additional hours, base rate and premium | Yes |
| Contractual and collectively agreed bonuses — seniority, thirteenth month, holiday bonus, performance bonus | Yes |
| Commission | Yes |
| Benefits in kind — company vehicle, accommodation, meals, communication tools — at their statutory flat value or real cost | Yes |
| Paid-leave pay, public holiday pay, and the employer top-up on sick pay | Yes |
| Value-sharing bonus | Yes as a component of remuneration, but with its own exemption treatment (Module 7) |
| Reimbursement of professional expenses within the exemption limits | No — not remuneration |
| Daily social security benefits paid directly by the sickness fund | No — not employer remuneration, though they may transit the payslip where the employer is subrogated |
| Profit-sharing and incentive-scheme amounts | No — outside gross pay, with their own regime (Module 7) |

The result is gross pay (salaire brut), the figure shown at the top of the payslip.
#### Step 2 — Build the contribution bases

| Base | Construction | Used for |
|---|---|---|
| Capped band (tranche A) | Gross pay up to the monthly ceiling, EUR 4,005 for 2026, prorated for part-time and part periods | Capped old-age contribution |
| Uncapped band | Total gross pay | Health, uncapped old-age, family allowances, industrial accidents, and most employer levies |
| Supplementary pension band 1 | Gross pay up to 1 monthly ceiling (EUR 4,005) | Agirc-Arrco band 1, general balance contribution band 1 |
| Supplementary pension band 2 | Gross pay from 1 to 8 monthly ceilings (EUR 4,005 to EUR 32,040) | Agirc-Arrco band 2, general balance contribution band 2 |
| Unemployment base | Gross pay up to 4 monthly ceilings (EUR 16,020) | Unemployment contribution and wage guarantee contribution |
| General social contribution base | Gross pay × 98.25 % for the portion up to 4 annual ceilings (EUR 192,240), then 100 %; plus employer contributions to supplementary health, death-and-disability and supplementary pension cover, with no allowance on those | General social contribution and social debt repayment contribution |

#### Step 3 — Apply employee contributions
Deduct, in this order on the payslip:

| Contribution | Employee rate 2026 | Base |
|---|---|---|
| Old-age, capped | 6.90 % | Capped band |
| Old-age, uncapped | 0.40 % | Total gross |
| Supplementary pension, band 1 | 3.15 % | Band 1 |
| Supplementary pension, band 2 | 8.64 % | Band 2 |
| General balance contribution, band 1 | 0.86 % | Band 1 |
| General balance contribution, band 2 | 1.08 % | Band 2 |
| Technical balance contribution | 0.14 % | Bands 1 and 2, only where pay exceeds the ceiling |
| Executive employment association contribution | 0.024 % | Bands 1 and 2, managerial grade only |
| Additional local health contribution, Alsace-Moselle | 1.30 % | Total gross |
| Employee share of the compulsory health cover, and of any death-and-disability or supplementary pension scheme | Per the policy | Per the policy |
| General social contribution, deductible portion | 6.80 % | General social contribution base |
| General social contribution, non-deductible portion | 2.40 % | General social contribution base |
| Social debt repayment contribution | 0.50 % | General social contribution base |

There is no employee unemployment contribution in metropolitan France; it was abolished on 1 January 2019 and the levy is now wholly employer-borne.
#### Step 4 — Compute the statutory net social amount
The net social amount (montant net social) has been a compulsory payslip line since 1 July 2023 and is transmitted in the DSN. It is a defined statutory quantity, not a derived convenience figure:
Net social amount = all remuneration and income paid, including benefits in kind and including employer contributions to supplementary health, death-and-disability and supplementary pension cover, less all employee social contributions, compulsory and non-compulsory.
It is the reference income used by the benefits authorities to calculate the earned-income top-up and the active-solidarity income. It sits between gross and net payable and equals neither.
#### Step 5 — Determine the net taxable amount
Start from gross pay, deduct the employee contributions that are deductible for income tax, then add back what is not:
Gross pay
−  employee social contributions, deductible portion
(old-age, supplementary pension, balance contributions,
general social contribution at 6.80 %, employee share of
the compulsory health cover)
+  general social contribution, non-deductible portion (2.40 %)
+  social debt repayment contribution (0.50 %)
+  employer contribution to the compulsory health cover
(not deductible for the employee)
+  benefits in kind not already in gross
−  the exempt portion of overtime pay, within the EUR 7,500
annual cap
=  NET TAXABLE AMOUNT (net imposable)
#### Step 6 — Calculate the income tax withheld at source
Withholding = Net taxable amount × the rate supplied by the tax administration
The employer applies the rate it is given and performs no tax computation of its own. Where no rate has been transmitted, the default grid applies to the net taxable amount. The result is rounded to the nearest euro for the remittance. Full detail is in Module 6.
#### Step 7 — Apply post-tax deductions

| Deduction | Nature |
|---|---|
| Employee share of meal vouchers | Contractual |
| Wage garnishment or maintenance order | Statutory, within the seizable fraction |
| Repayment of an advance or a salary loan | Contractual, within the seizable fraction where it is an advance |
| Union dues, where the employee has mandated the deduction | Voluntary |
| Recovery of an overpayment | Contractual, within the seizable fraction |

#### Step 8 — Finalise net pay
Net payable before income tax
−  income tax withheld at source
−  post-tax deductions
+  reimbursement of professional expenses within the exemption limits
+  50 % employer reimbursement of the public transport season ticket
−  any mid-month advance already paid
=  NET PAID TO THE EMPLOYEE
#### Employer on-costs, calculated in parallel
Employer contributions do not enter the employee's gross-to-net chain at any point; they are calculated on the same bases, in parallel, and are shown on the payslip in the employer column and in the employer's cost of employment.

| Employer contribution | 2026 rate | Base |
|---|---|---|
| Health, maternity, disability, death | 13.00 % | Total gross |
| Old-age, capped | 8.55 % | Capped band |
| Old-age, uncapped | 2.11 % | Total gross |
| Family allowances | 5.25 % | Total gross |
| Industrial accidents and occupational disease | Establishment-specific net rate | Total gross |
| Autonomy solidarity contribution | 0.30 % | Total gross |
| National housing aid fund — fewer than 50 employees | 0.10 % | Capped band |
| National housing aid fund — 50 employees or more | 0.50 % | Total gross |
| Supplementary pension, band 1 / band 2 | 4.72 % / 12.95 % | Band 1 / band 2 |
| General balance contribution, band 1 / band 2 | 1.29 % / 1.62 % | Band 1 / band 2 |
| Technical balance contribution | 0.21 % | Bands 1 and 2 where pay exceeds the ceiling |
| Executive employment association contribution | 0.036 % | Bands 1 and 2, managerial grade |
| Unemployment insurance | 4.00 % | Up to 4 monthly ceilings |
| Wage guarantee scheme | 0.25 % | Up to 4 monthly ceilings |
| Social dialogue contribution | 0.016 % | Total gross |
| Mobility levy, where the establishment employs 11 or more | Local rate set by the transport authority | Total gross |
| Single training and apprenticeship contribution | 0.55 % or 1.00 % training, plus 0.68 % apprenticeship tax | Total gross |
| Employer share of the compulsory health cover, at least 50 % | Per the policy | Per the policy |
| Managerial-grade death-and-disability contribution | 1.50 % | Capped band |

The unified degressive general reduction is then subtracted from these employer contributions. It is not an employee-side item and never appears in the gross-to-net chain. Its formula, the 2026 parameters and the frozen minimum-wage reference are in Module 5.2.
#### Order of operations, and why it matters
Two sequencing points are load-bearing:
- The general social contribution base is not gross pay minus contributions; it is gross pay reduced by the capped 1.75 % allowance and increased by employer supplementary-cover contributions. Computing it after the other contributions produces a wrong figure.
- The net taxable amount is not the net payable before tax. It is higher, because the non-deductible portion of the general social contribution, the social debt repayment contribution and the employer's health-cover contribution are all added back. A system that withholds tax on the net payable systematically under-withholds.
Legal basis: Social Security Code, Articles L136-1 to L136-8 (general social contribution), L242-1 (contribution base), L241-13 (unified degressive reduction), D242-1 (ceiling), R242-2; Ordinance n° 96-50 of 24 January 1996 (social debt repayment contribution); General Tax Code, Articles 204 A to 204 N and 83; Arrêté of 25 February 2016 as amended by the Arrêté of 31 January 2023 (payslip content and net social amount); Arrêté of 22 December 2025 (2026 social security ceiling).

## Module 4: Gross Compensation


### 4.1 Minimum Wage


#### Is there a minimum wage? Who is eligible?

Yes. France has a statutory national minimum growth wage (salaire minimum interprofessionnel de croissance, SMIC), governed by Labour Code Articles L3231-1 to L3231-12. Every employee in the private sector is entitled to it, whatever the contract type, whatever the sector, and irrespective of length of service.
The entitlement applies to permanent and fixed-term employees, part-time employees pro rata, temporary-agency workers, and home workers. Three populations are treated differently:

| Population | Treatment | Legal basis |
|---|---|---|
| Employees under 17 years old | 20 % reduction, unless they have six months' professional practice in the branch, in which case the full rate applies | Labour Code Article D3231-3 |
| Employees aged 17 to 18 | 10 % reduction, subject to the same six-month exception | Labour Code Article D3231-3 |
| Apprentices and employees on a professionalisation contract | Paid a percentage of the minimum wage set by a scale crossing age with the year of the contract, from 27 % for a minor in the first year up to 78 % | Labour Code Articles D6222-26 and D6325-15 |

Company directors treated as employees for social security purposes, and interns, are outside the minimum wage: an intern receives a statutory gratuity, not a wage.

#### Is the minimum wage applicable at a national level or does it vary by province/state?

It is national and uniform across metropolitan France and the overseas departments of Guadeloupe, Martinique, Guyane and La Réunion. There is no regional minimum wage.
Mayotte is the sole exception. It has its own lower minimum wage, converging by statute toward the national rate. From 1 June 2026 the Mayotte hourly rate is EUR 9.56 gross, giving EUR 1,449.93 gross per month, against EUR 12.31 nationally.
Above the statutory floor, sector-level collective agreements set their own minimum pay scales by grade and coefficient. These are frequently higher than the statutory minimum and are legally binding on every employer covered by the agreement. In practice the binding minimum for a given employee is the higher of the statutory minimum wage and the applicable collective-agreement minimum for their grade — a point that must be built into the payroll's minimum-wage test rather than left to the sector-agreement module.

#### Provide all applicable minimum wage rates.

2026 contains two minimum wage levels, because the annual revaluation on 1 January was followed by a mid-year revaluation on 1 June triggered by the inflation clause of Labour Code Article L3231-5.

| Effective from | Hourly gross | Monthly gross, 35-hour week | Annual gross | Guaranteed minimum (minimum garanti) |
|---|---|---|---|---|
| 1 January 2026 | EUR 12.02 | EUR 1,823.03 | EUR 21,876.36 | EUR 4.22 |
| 1 June 2026 | EUR 12.31 | EUR 1,867.02 | EUR 22,404.24 | EUR 4.35 |

Two arithmetic points, both of which matter for configuration:
- The monthly figure is not the hourly rate multiplied by 151.67. It is the hourly rate multiplied by the exact fraction 35 × 52 ÷ 12 = 151.6666…, then rounded to the cent. 12.31 × 151.6666… = 1,867.0166…, giving EUR 1,867.02, whereas 12.31 × 151.67 gives EUR 1,867.06. The four-cent difference is systematic, appears every year, and a minimum-wage compliance test built on 151.67 will produce spurious near-threshold failures.
- The June increase is 2.41 %: 12.31 ÷ 12.02 = 1.02413. The January increase was 1.18 % over the 2025 rate of EUR 11.88. Both reconcile exactly to the published percentages, which confirms the hourly figures against the announcements.
The guaranteed minimum shown in the last column is a separate statutory reference, not a wage. It is used to value certain benefits in kind and professional-expense allowances, and it is revalued on the same dates.
For the reduced rates: at the 1 June 2026 level, an employee under 17 without six months' branch practice is on EUR 9.85 per hour (12.31 × 0.80), and an employee aged 17 to 18 on EUR 11.08 per hour (12.31 × 0.90).

#### Does the minimum wage impact any tax or social security calculations?

Extensively. The minimum wage is the single most reused parameter in French payroll, and 2026 makes it doubly so because two different minimum-wage values are in force simultaneously on the same payslip.

| Parameter driven by the minimum wage | Which value it uses in 2026 |
|---|---|
| The statutory pay floor itself | The live value: EUR 12.02 to 31 May, EUR 12.31 from 1 June |
| Unified degressive general reduction of employer contributions | Frozen at EUR 12.02 for the whole of 2026, by Décret n° 2026-509 of 12 June 2026 |
| Enhanced exemption regime for the value-sharing bonus (pay below 3 times the minimum wage) | The live value |
| Cap on daily sickness benefits (1.4 times the minimum wage) | The live value |
| Apprentice pay scale and the apprentice contribution exemption threshold | The live value |
| Reduced-rate thresholds in the overseas exemption schemes | The live value |

The frozen reference for the general reduction is the most consequential parameter change of the 2026 French payroll year. The Minister for public accounts announced on 22 May 2026 that the June minimum wage revaluation would not be passed through to the general reductions; the freeze was confirmed by the official social security doctrine and then enacted by Décret n° 2026-509 of 12 June 2026, published on 14 June. The practical effect is that from 1 June an employer pays a higher wage but calculates its relief against the January reference, so the relief falls as a proportion of pay. A payroll engine that reads a single "current minimum wage" variable will silently overstate the relief for seven months of the year.
Configuration requirement: hold two minimum-wage parameters — a live pay reference and a frozen relief reference — and never let one default to the other.

#### How are deductions handled if they cannot be made due to minimum wage constraints?

Three distinct floors operate, and they protect different things.

| Floor | What it protects | Consequence |
|---|---|---|
| The minimum wage itself | The employee's gross entitlement for the hours worked | The employer may not agree, and the employee may not waive, pay below the floor. A shortfall is recoverable for five years, with a criminal fine per employee concerned |
| The absolutely protected amount in a garnishment (the active-solidarity income for a single person, EUR 651.69 per month in 2026) | A minimum sum that must remain payable to the employee whatever the number of creditors | Garnishment is reduced to leave this amount intact. Maintenance orders take priority but the protected amount still applies |
| The seizable fraction scale | The proportion of pay that may be attached | Deductions beyond the scale are void; the employer that over-deducts is liable to the employee |

Elements that count toward the minimum-wage comparison are narrower than gross pay, and the distinction produces most of the practical errors:

| Counts toward the minimum wage | Does not count |
|---|---|
| Base salary for the contractual hours | Overtime premiums |
| Benefits in kind, at their statutory flat value | Seniority bonuses |
| Bonuses that directly reward the work performed, where paid monthly | Bonuses tied to attendance or general company results |
| Commission on the employee's own sales | Thirteenth-month and holiday bonuses, unless paid in monthly instalments |
|  | Reimbursement of professional expenses |
|  | Profit-sharing and incentive-scheme amounts |
|  | Value-sharing bonus |

Where a voluntary deduction — a salary advance, an employee loan, recovery of an overpayment — would take pay below one of these floors, the deduction is capped and the balance carries forward to later periods. It is not written off, but it cannot be recovered faster than the scale allows.
Legal basis: Labour Code, Articles L3231-1 to L3231-12, L3232-1, D3231-3, D6222-26 and D6325-15; Décret fixing the minimum wage from 1 June 2026; Décret n° 2026-509 of 12 June 2026 (freezing the minimum-wage reference for the general reduction); Social Security Code, Article L241-13; Code of Civil Enforcement Procedures, Articles L3252-1 to L3252-13 and R3252-2.

### 4.2 Salary Components


#### What are the mandatory and common salary components?

Only one component is mandatory in every French employment relationship: the base salary for the contractual working time, at or above the applicable minimum. Everything else is mandatory only if imposed by the applicable collective agreement, by the employment contract, by a company agreement or by established custom — and in France the collective agreement makes a great many of them mandatory in practice.

| Component | Nature | Typical basis |
|---|---|---|
| Base salary (salaire de base) | Universal, mandatory | Contract, at or above the statutory and collective-agreement minimum |
| Overtime and additional hours | Statutory where hours are worked beyond the contractual duration | Labour Code |
| Seniority bonus (prime d'ancienneté) | Very common, mandatory where the collective agreement provides | Sector agreement; typically a percentage of the grade minimum rising with service |
| Thirteenth month (13ème mois) | Common, mandatory where the collective agreement or custom provides | Sector or company agreement |
| Holiday bonus (prime de vacances) | Common in several sectors | Sector agreement |
| Performance and objectives bonus | Contractual | Contract or company scheme |
| Commission | Contractual | Contract |
| On-call and shift premiums, Sunday and night premiums | Statutory or agreement-based | Labour Code and sector agreement |
| Benefits in kind | Contractual | Valued under statutory flat rates or real cost |
| Value-sharing bonus (prime de partage de la valeur) | Discretionary | Company agreement or unilateral decision |
| Meal vouchers, transport reimbursement, sustainable mobility allowance | Partly statutory | See Module 7 |

The 50 % employer reimbursement of the employee's public transport season ticket is compulsory nationwide under Labour Code Article L3261-2 and is best modelled as a payroll component even though it is a reimbursement rather than remuneration.

#### What is the general definition and pay cycle for each component?


| Component | Definition | Cycle |
|---|---|---|
| Base salary | Consideration for the contractual working time, smoothed across the year under Labour Code Article L3242-1 | Monthly, current month |
| Overtime | Hours worked beyond 35 per week, or beyond the agreed reference period | Monthly, usually one month in arrears |
| Seniority bonus | Percentage of the grade minimum or of base salary, rising in steps with completed years of service | Monthly |
| Thirteenth month | One additional month of salary, or a fraction of annual salary | Annually in November or December, or in two instalments, or spread monthly |
| Holiday bonus | Fixed sum or percentage of leave pay | Annually, generally with the May or June payroll |
| Performance bonus | Amount determined against measurable objectives | Annually or quarterly |
| Commission | Percentage of sales achieved | Monthly or quarterly, in arrears |
| Benefits in kind | Value of a good or service made available free or below cost | Monthly, for as long as the benefit is available |
| Value-sharing bonus | Discretionary sum, subject to statutory caps | Up to four instalments per calendar year |


#### Which components are taxable vs non-taxable and sociable vs non-sociable?

France distinguishes three separate liabilities, and a component can be treated differently under each. "Subject to contributions" and "subject to the general social contribution" are not the same test.

| Component | Social security contributions | General social contribution and social debt repayment contribution | Income tax |
|---|---|---|---|
| Base salary | Yes, in full | Yes, on 98.25 % up to 4 annual ceilings | Yes |
| Overtime, base and premium | Yes, with the employee old-age relief up to 11.31 % | Yes | Exempt up to EUR 7,500 net per year, then taxable |
| Seniority, thirteenth month, holiday, performance bonuses | Yes, in full | Yes | Yes |
| Commission | Yes | Yes | Yes |
| Benefits in kind | Yes, at the flat or real value | Yes | Yes |
| Professional expense reimbursement within the statutory limits | No | No | No |
| Professional expense reimbursement above the limits | Yes on the excess | Yes on the excess | Yes on the excess |
| Employer share of the compulsory health cover | Exempt from contributions within limits | Yes, with no 1.75 % allowance | Yes — added to net taxable |
| Employer share of death-and-disability and supplementary pension cover | Exempt within limits, then the 8 % social lump-sum levy for employers with 11 or more employees | Yes, with no allowance | Death-and-disability employer share is taxable; supplementary pension employer share is exempt within limits |
| Value-sharing bonus | Exempt within the cap | Subject, except under the enhanced regime | Taxable, except under the enhanced regime |
| Incentive scheme and profit-sharing amounts, when invested | Exempt from contributions | Subject, with no allowance | Exempt if invested for the lock-in period |
| Statutory severance, within the exempt fraction | Exempt within limits | Exempt only up to the legal or collectively agreed amount | Exempt within limits |
| 50 % transport season ticket reimbursement | Exempt | Exempt | Exempt |
| Meal vouchers, employer share up to EUR 7.32 per voucher | Exempt | Exempt | Exempt |

The recurring configuration error is treating the employer's compulsory health-cover contribution as fully exempt. It is exempt from social security contributions within limits, but it is subject to the general social contribution with no allowance and added to the employee's net taxable amount. Three different answers for one component.

#### Are components uniform across the country or do they differ by state/province?

The statutory framework is national. Variation comes from three sources, none of them geographic in the federal sense:

| Source of variation | Effect |
|---|---|
| Sector collective agreement (identified by its four-digit IDCC) | Determines minimum pay scales by grade, seniority bonus, thirteenth month, holiday bonus, notice periods, severance above the statutory floor, and sector-specific premiums. This is by far the largest source of variation and it follows the activity, not the location |
| Company or establishment agreement | May improve on the sector agreement and may create bonuses of its own |
| Genuine territorial regimes | Alsace-Moselle adds the 1.30 % employee health contribution and two public holidays; the overseas departments have specific exemption schemes and, for Mayotte, a separate minimum wage |

For system design the practical consequence is that the collective agreement identifier is a first-class configuration key alongside the establishment identifier, not an informational field.

#### What is the calculation logic for each salary component?


| Component | Formula |
|---|---|
| Monthly base salary, full-time 35-hour week | Contractual annual salary ÷ 12; the hourly rate for other purposes is the monthly salary ÷ 151.67 |
| Part-time base salary | Full-time monthly salary × contractual hours ÷ 151.67 |
| Overtime | Hourly rate × hours × (1 + premium rate); premium 25 % for the first eight hours beyond 35 in the week, 50 % thereafter, reducible by agreement to no less than 10 % |
| Additional hours for part-timers | Hourly rate × hours × 1.10 within one tenth of the contractual duration, × 1.25 beyond |
| Seniority bonus | Grade minimum (or base salary, per the agreement) × the seniority percentage for completed years of service |
| Thirteenth month | Base salary of the reference month, prorated for time present in the reference year |
| Benefit in kind, meals | Statutory flat value of EUR 5.50 per meal for 2026, EUR 11.00 for two meals |
| Benefit in kind, accommodation | Statutory flat scale by number of rooms and pay bracket, from EUR 79.70 to EUR 225.60 per room per month |
| Benefit in kind, company vehicle | 20 % of the inclusive purchase price for a vehicle made available on or after 1 February 2025, or the flat percentage of the annual lease cost, with a 70 % abatement capped at EUR 4,641.60 per year for a qualifying low-emission vehicle |
| Commission | Contractual rate × the qualifying sales base |


#### Which components require employee-declared values and submissions?


| Component or treatment | What the employee must supply | Frequency |
|---|---|---|
| 50 % public transport reimbursement | The season ticket or proof of subscription | On subscription and on renewal |
| Sustainable mobility allowance | A sworn statement, or evidence of the mode of travel used | Annually |
| Exemption from the compulsory health cover | Evidence of the alternative cover relied on | On hire and annually |
| Meal vouchers | Enrolment; the employee share is then deducted automatically | Once |
| Benefit in kind on a company vehicle | Business and private mileage where the real-cost method is used | Annually |
| Disabled-worker recognition | The certificate, if the employee chooses to declare it | On issue and on renewal |
| Wage garnishment | Nothing — the order arrives from the enforcement officer | Per event |
| Withholding-at-source rate | Nothing — the rate is transmitted by the tax administration | Automatic |


#### Deliverable: Define the primary earnings base for social security contributions and produce a comprehensive inclusion/exclusion analysis.

The statutory definition. Social Security Code Article L242-1 defines the contribution base as all sums paid to workers in consideration of or on the occasion of the work, whatever their designation and whatever their form, including wages, indemnities, bonuses, gratuities and benefits in cash or in kind. The definition is deliberately broad: the starting presumption is that everything paid because of the employment relationship is in the base, and an exclusion must be found in a specific text.
Article L136-1-1 defines the base for the general social contribution in near-identical terms but with a different allowance and a different set of add-backs, which is why the two bases never coincide.
Inclusion and exclusion analysis.

| Item | In the contribution base? | Authority and condition |
|---|---|---|
| Base salary, overtime, bonuses, commission | Included | Article L242-1 |
| Benefits in kind | Included at the statutory flat value or real cost | Article L242-1; Arrêté of 10 December 2002 |
| Employer top-up to sickness benefits | Included | Article L242-1 |
| Holiday pay paid by the employer | Included | Article L242-1 |
| Paid-leave amounts paid by a sector leave fund | Excluded from the employer's base; the fund contributes | Article L243-1-3 |
| Reimbursement of professional expenses, within the statutory limits and properly evidenced | Excluded | Arrêté of 20 December 2002 |
| Professional expense allowances above the limits | Included on the excess | Arrêté of 20 December 2002 |
| Meal vouchers, employer share up to EUR 7.32 per voucher and between 50 % and 60 % of face value | Excluded | Article L136-1-1, III |
| 50 % public transport reimbursement | Excluded | Article L3261-2 Labour Code |
| Sustainable mobility allowance within the annual limit | Excluded | Article L3261-3-1 Labour Code |
| Employer contributions to the compulsory health cover, within limits | Excluded from contributions, subject to the general social contribution and to income tax | Article L242-1, II |
| Employer contributions to death-and-disability and supplementary pension cover, within limits | Excluded from contributions, then subject to the 8 % social lump-sum levy where the employer has 11 or more employees | Articles L242-1, II and L137-15 |
| Incentive-scheme and profit-sharing amounts | Excluded; subject to the general social contribution and, above 50 employees for profit-sharing, to the social lump-sum levy | Labour Code Articles L3312-4 and L3325-1 |
| Employer contribution to a company savings plan | Excluded within the caps | Labour Code Article L3332-27 |
| Value-sharing bonus within the cap | Excluded from contributions | Act n° 2022-1158 of 16 August 2022, Article 1 |
| Statutory or collectively agreed severance, within two annual ceilings and within the income-tax-exempt fraction | Excluded | Article L242-1, III |
| Any termination payment exceeding ten annual ceilings | Included in full, from the first euro | Article L242-1, III |
| Works council social and cultural benefits within the administrative tolerances | Excluded in practice | Administrative tolerance, restated in the official social security doctrine |
| Gifts and vouchers within 5 % of the monthly ceiling per event | Excluded | Administrative tolerance |
| Free share awards and share options | Excluded from ordinary contributions; subject to specific employer and employee contributions | Article L137-13 |

The two limits that catch clients most often: the value-sharing bonus is exempt from contributions but not from the general social contribution except under the enhanced regime; and a termination payment that crosses ten annual ceilings loses its exemption entirely rather than only on the excess.
Legal basis: Social Security Code, Articles L242-1, L136-1-1, L137-13, L137-15, L243-1-3; Labour Code, Articles L3121-28 to L3121-39, L3123-28 to L3123-31, L3242-1, L3261-2, L3261-3-1, L3312-4, L3325-1, L3332-27; Arrêté of 10 December 2002 (benefits in kind); Arrêté of 20 December 2002 (professional expenses); Act n° 2022-1158 of 16 August 2022.

### 4.3 Proration


#### Are fixed wages prorated for the number of working days?

No — and this is one of the most misunderstood features of French payroll. Labour Code Article L3242-1 provides that monthly remuneration is independent of the number of days worked in the month for a given contractual working time. A full-time employee present all month receives the same salary in February as in March, even though March contains more working days.
Proration arises only when the employee is not present, or not entitled, for the whole month:

| Situation | Proration |
|---|---|
| Full month, employee present throughout | None — the full smoothed salary is paid |
| Hire or termination during the month | Yes, for the days of the employment relationship |
| Unpaid absence | Yes, by deducting the value of the absence |
| Part-time work | The contractual hours are reduced; the monthly salary is fixed at that reduced level and is then itself smoothed |
| Change of contractual hours during the month | Two smoothed salaries, each prorated to its sub-period |


#### Describe the statutory or standard business practice for prorating fixed salary components for mid-period hires and terminations.

There is no single statutory method. The Labour Code says only that the deduction must be strictly proportionate to the absence, and case law adds that it must be calculated consistently and must not disadvantage the employee. Three methods are in general use.

| Method | Formula | Comment |
|---|---|---|
| Real working hours | Monthly salary × hours actually worked ÷ hours the employee should have worked that month | The most accurate and the method preferred by the courts, because it never produces a result that penalises the employee for the calendar |
| Working days present (jours ouvrés) | Monthly salary × working days present ÷ working days in the month | Widely used; acceptable if applied consistently in both directions |
| Calendar days | Monthly salary × calendar days of employment ÷ calendar days in the month | Simple and common for hires and departures; must not be used for short absences, where it under-deducts on a Monday and over-deducts on a Saturday |

The market standard, and the recommendation for a new implementation, is: calendar days for a hire or a departure, real hours for an absence. Using calendar days for absences is the single most frequent source of unlawful deductions in French payroll audits.
Bonuses are prorated on their own reference period, not on the month. A thirteenth month is prorated over the calendar year of service, a holiday bonus over the leave accrual year.

#### Provide the proration formula and a worked example.

Formula, mid-month hire, calendar-day method
Prorated salary = Monthly salary × calendar days of employment in the month
÷ calendar days in the month
Worked example — hire on 12 October 2026
An employee is hired on Monday 12 October 2026 on a full-time contract at EUR 3,200.00 gross per month.

| Step | Calculation | Result |
|---|---|---|
| 1. Calendar days in October 2026 | — | 31 |
| 2. Calendar days of employment | 12 October to 31 October inclusive | 20 |
| 3. Prorated base salary | 3,200.00 × 20 ÷ 31 | EUR 2,064.52 |
| 4. Prorated monthly social security ceiling | 4,005.00 × 20 ÷ 31 | EUR 2,583.87 |
| 5. Capped band | Lower of 2,064.52 and 2,583.87 | EUR 2,064.52 |
| 6. Uncapped band | Full gross | EUR 2,064.52 |

Worked example — the same hire, real-hours method for comparison
October 2026 contains 22 working days. From 12 October the employee is present for 15 of them, that is 105 hours against 154 hours in the month at 7 hours per day.

| Step | Calculation | Result |
|---|---|---|
| Prorated base salary | 3,200.00 × 105 ÷ 154 | EUR 2,181.82 |

The EUR 117.30 difference between the two methods is not an error in either: it reflects that the employee started on a Monday and so worked proportionately more of the month's working days than of its calendar days. Both methods are lawful; what is unlawful is switching between them to the employee's disadvantage.
The ceiling must be prorated with the same method as the salary. Step 4 above uses calendar days precisely because step 3 did. Prorating salary on working days and the ceiling on calendar days produces a capped band that is wrong every time.
Legal basis: Labour Code, Articles L3242-1 and L3123-1 and following; Social Security Code, Article R242-2; settled case law of the Social Chamber of the Court of Cassation on proportionate deduction for absence.

### 4.4 Overtime


#### Detail the statutory rules for overtime, including eligibility criteria and mandatory rates.

The statutory working week is 35 hours (Labour Code Article L3121-27). Hours worked beyond it, at the employer's request or with its agreement, are overtime.

| Rule | Content | Legal basis |
|---|---|---|
| Premium rate, first eight hours (the 36th to the 43rd in the week) | 25 % | Article L3121-36 |
| Premium rate, from the 44th hour | 50 % | Article L3121-36 |
| Minimum rate where a collective agreement provides otherwise | 10 %, an absolute floor | Article L3121-33 |
| Default annual overtime quota | 220 hours per employee per year | Article D3121-24 |
| Compensatory rest beyond the quota | 50 % of the hours beyond the quota in establishments with 20 employees or fewer; 100 % above 20 | Article L3121-30 |
| Maximum daily working time | 10 hours, extendable to 12 by agreement | Article L3121-18 |
| Maximum weekly working time | 48 hours in any one week; 44 hours on average over any 12 consecutive weeks | Articles L3121-20 and L3121-22 |
| Minimum daily rest | 11 consecutive hours | Article L3131-1 |
| Minimum weekly rest | 24 consecutive hours plus the daily rest, that is 35 hours | Article L3132-2 |

Overtime may be replaced, in whole or in part, by equivalent compensatory rest where a collective agreement so provides; hours so compensated do not count against the annual quota.
Part-time employees do not work overtime. They work additional hours (heures complémentaires), capped at one tenth of the contractual duration, or one third where a collective agreement allows, and premiumed at 10 % within the first tenth and 25 % beyond (Labour Code Articles L3123-28 to L3123-31). Additional hours may never bring a part-timer to the full-time duration; if they do, the contract is reclassified as full-time.
Employees on a day-count arrangement (forfait annuel en jours, typically 218 days) are outside the hours framework entirely. They have no overtime. Days worked beyond the agreed count, with the employer's agreement, are paid at a premium of at least 10 %.

#### Explain how overtime is treated for income tax and social security calculations.

Overtime carries three separate reliefs in 2026, each with a different mechanic. All three apply to additional hours worked by part-timers and to days beyond the count in a day-count arrangement.

| Relief | 2026 treatment | Legal basis |
|---|---|---|
| Employee old-age contribution relief | A reduction equal to the employee's statutory and compulsory supplementary old-age contribution rate applied to the overtime pay, capped at 11.31 %. The 11.31 % is the sum of 7.30 % basic old-age (6.90 % capped plus 0.40 % uncapped), 3.15 % supplementary pension band 1 and 0.86 % general balance contribution band 1. Where the employee's effective rate is lower, the lower rate applies | Social Security Code Article L241-17 |
| Employer flat deduction | EUR 1.50 per overtime hour for employers with fewer than 20 employees; EUR 0.50 per hour for employers with 20 or more. From 1 January 2026 this is available to employers of every size, the previous 250-employee exclusion having been removed by Article 21 of the Social Security Financing Act for 2026 (Act n° 2025-1403 of 30 December 2025) amending Social Security Code Article L241-18-1. For a day-count arrangement the deduction is seven times the hourly amount per additional day | Social Security Code Articles L241-18 and L241-18-1 |
| Income tax exemption | Overtime and additional-hours pay, base rate and premium together, is exempt from income tax up to EUR 7,500 net per year per employee. Parliamentary amendments to raise the cap to EUR 10,000 were not retained in the final 2026 Finance Act | General Tax Code Article 81 quater |

Three points that decide whether an implementation is correct:
1. Overtime remains fully subject to the general social contribution and the social debt repayment contribution. The reliefs above touch old-age contributions, employer contributions and income tax. They do not touch the 9.70 % social levies.
1. The income tax exemption is on the net amount, and the cap is annual and cumulative. Once EUR 7,500 of exempt overtime has been reached in the calendar year, further overtime enters the net taxable amount in full. The year-to-date counter must be migrated on a provider change.
1. The employer flat deduction is deducted from employer contributions, in the same way as the general reduction, and is capped so that the two together cannot exceed the employer contributions actually due.
Legal basis: Labour Code, Articles L3121-18, L3121-20, L3121-22, L3121-27, L3121-30, L3121-33, L3121-36, L3123-28 to L3123-31, L3131-1, L3132-2, D3121-24; Social Security Code, Articles L241-17, L241-18 and L241-18-1; General Tax Code, Article 81 quater; Act n° 2025-1403 of 30 December 2025, Article 21.

### 4.5 Bonuses


#### Is there a statutory requirement to pay bonuses? If so, how are they calculated?

There is no general statutory bonus in France — no statutory thirteenth month, no statutory holiday bonus, no statutory annual bonus. A bonus becomes compulsory through one of four routes, and once compulsory it is enforceable exactly like base salary:

| Route | How the obligation arises | How to withdraw it |
|---|---|---|
| Sector collective agreement | The agreement provides for it; it binds every covered employer | Only by renegotiating the agreement |
| Company or establishment agreement | Negotiated with the union representatives or the staff body | By denouncing the agreement, with notice and a survival period |
| Employment contract | Written into the individual contract | Only with the employee's written agreement — a variation of contract |
| Established custom (usage) | Paid generally, consistently and with a fixed method over a period | By denouncing the custom: individual notice to each employee, notice to the staff representatives, and a reasonable notice period |

The custom route deserves attention in a due-diligence exercise. Three consecutive years of an identical discretionary bonus, paid to the whole workforce on a stable formula, will normally be held to constitute a custom, and unwinding it requires a formal denunciation procedure. Clients frequently assume a discretionary bonus can simply be stopped.
Two schemes are compulsory but are not bonuses: statutory profit-sharing (participation), compulsory for companies with 50 or more employees, and — for companies of 11 to 49 employees meeting a profitability test — the obligation to operate at least one value-sharing device. Both are covered in Module 7.

#### Is there a specific tax treatment for bonuses?

For ordinary bonuses, no. A seniority bonus, a thirteenth month, a holiday bonus, a performance bonus and a commission are all ordinary remuneration: fully subject to social security contributions, fully subject to the general social contribution and the social debt repayment contribution, and fully included in the net taxable amount of the month in which they are paid.
France has no separate annual-bonus tax schedule and no spreading mechanism. A thirteenth month paid in December is taxed in December, at the withholding rate then in force. Because the withholding rate is a fixed percentage rather than a progressive scale applied to the month, a large bonus does not push the employee into a higher withholding band; any correction happens the following year when the tax administration recalculates the rate from the annual return.
The exception is the value-sharing bonus (prime de partage de la valeur), which has a genuinely distinct regime:

| Feature | 2026 treatment |
|---|---|
| Exemption from social security contributions | Up to EUR 3,000 per calendar year per employee, or EUR 6,000 where the employer also operates a profit-sharing or incentive scheme, or is a qualifying social-economy body |
| General social contribution, social debt repayment contribution and income tax — standard regime | Subject |
| Enhanced regime | For bonuses paid between 1 January 2024 and 31 December 2026 by an employer with fewer than 50 employees to an employee whose pay over the preceding twelve months was below three times the minimum wage, the bonus is additionally exempt from the general social contribution, the social debt repayment contribution and income tax |
| Instalments | Up to four payments per calendar year; the annual cap applies to the total |
| Substitution | The bonus may not replace any element of pay |

The enhanced regime's expiry on 31 December 2026 is a dated item that must be carried into the 2027 configuration review rather than left as a permanent setting.
Legal basis: Labour Code, Articles L2253-1 and following, L3312-1 and following, L3322-1 and following; Act n° 2022-1158 of 16 August 2022, Article 1, as amended; Act n° 2023-1107 of 29 November 2023; settled case law of the Social Chamber of the Court of Cassation on customs and their denunciation.

### 4.6 Wage Classification (Country-Specific)


#### Are there country-specific classifications for wages critical for social security or tax calculations?

Yes. Four classification systems operate simultaneously and each one changes a calculation. They are independent of each other, so a component's position in one says nothing about its position in the others.

| Classification | What it decides |
|---|---|
| Contribution bands (tranches) | Which contributions apply, and at what rate, to which slice of pay |
| Remuneration versus expense reimbursement | Whether the item is in the contribution base at all |
| Managerial grade (cadre) versus non-managerial | The 1.50 % employer death-and-disability contribution, the executive employment association contribution, notice periods and severance under many agreements |
| Occupational category code (PCS-ESE) | Statistical classification declared in the DSN; drives no calculation but is validated on filing |


#### Provide a detailed definition for each classification.

Contribution bands. France slices pay against the social security ceiling, and the slices differ between the basic scheme and the supplementary pension scheme. Using one set of bands for both is a defect.

| Band | Definition | 2026 monthly range | Contributions using it |
|---|---|---|---|
| Capped band (tranche A) | Pay up to 1 monthly ceiling | EUR 0 to 4,005 | Basic old-age capped 6.90 % employee / 8.55 % employer; housing fund at 0.10 %; managerial death-and-disability 1.50 % |
| Uncapped band | Total pay, with no upper limit | Unlimited | Health 13 %, uncapped old-age 0.40 % / 2.11 %, family allowances 5.25 %, industrial accidents, autonomy solidarity 0.30 %, social dialogue, mobility levy, training and apprenticeship levies |
| Supplementary pension band 1 | Pay up to 1 monthly ceiling | EUR 0 to 4,005 | Agirc-Arrco 3.15 % / 4.72 %; general balance contribution 0.86 % / 1.29 % |
| Supplementary pension band 2 | Pay from 1 to 8 monthly ceilings | EUR 4,005 to 32,040 | Agirc-Arrco 8.64 % / 12.95 %; general balance contribution 1.08 % / 1.62 % |
| Bands 1 and 2 combined, above the ceiling only | Pay from 0 to 8 ceilings, but only for employees whose pay exceeds 1 ceiling | Up to EUR 32,040 | Technical balance contribution 0.14 % / 0.21 % |
| Unemployment band | Pay up to 4 monthly ceilings | EUR 0 to 16,020 | Unemployment 4.00 %; wage guarantee 0.25 % |
| General social contribution band | 98.25 % of pay up to 4 annual ceilings (EUR 192,240), 100 % above | — | General social contribution 9.20 %; social debt repayment contribution 0.50 % |
| Above 8 ceilings | Pay above EUR 32,040 per month | — | No supplementary pension contribution is due; the uncapped basic contributions and the social levies continue |

Remuneration versus expense reimbursement. An expense reimbursement is outside the contribution base only if the expense was genuinely incurred in the interest of the business, and only within the limits of the Arrêté of 20 December 2002. Above those limits the excess is remuneration. Where the employer applies the flat-rate professional-expense deduction available in certain sectors, a further set of rules applies and the reimbursement is reintegrated into the base before the deduction.
Managerial grade. The grade is fixed by the collective agreement, by reference to the employee's classification level, and not by job title or by pay level. Since the 2019 merger of the executive and general supplementary pension schemes there is no separate managerial pension scheme, but the grade still carries the compulsory 1.50 % employer death-and-disability contribution on the capped band, with at least half the resulting benefit covering death risk, and the 0.06 % executive employment association contribution split 0.036 % employer and 0.024 % employee.
Occupational category code. A four-character code from the national statistical nomenclature of occupations, declared in the DSN contract block. It drives no payroll calculation but is validated on filing and an inconsistent code generates a filing anomaly.

#### Create a reference table classifying common pay components.


| Component | Contribution bands it enters | In the contribution base | In the general social contribution base | In net taxable |
|---|---|---|---|---|
| Base salary | All applicable bands | Yes | Yes, at 98.25 % | Yes |
| Overtime pay | All applicable bands | Yes, with relief to 11.31 % on employee old-age | Yes, at 98.25 % | Exempt to EUR 7,500 net per year |
| Seniority bonus | All applicable bands | Yes | Yes, at 98.25 % | Yes |
| Thirteenth month | All applicable bands | Yes | Yes, at 98.25 % | Yes |
| Commission | All applicable bands | Yes | Yes, at 98.25 % | Yes |
| Company vehicle benefit | All applicable bands | Yes, at the flat value | Yes, at 98.25 % | Yes |
| Accommodation benefit | All applicable bands | Yes, at the flat scale | Yes, at 98.25 % | Yes |
| Meal benefit | All applicable bands | Yes, at EUR 5.50 per meal | Yes, at 98.25 % | Yes |
| Meal vouchers, employer share within limits | None | No | No | No |
| Public transport reimbursement, 50 % | None | No | No | No |
| Expense reimbursement within limits | None | No | No | No |
| Expense reimbursement above limits | All applicable bands, on the excess | Yes on the excess | Yes on the excess | Yes on the excess |
| Employer health-cover contribution | None for contributions | No | Yes, at 100 % with no allowance | Yes |
| Employer death-and-disability contribution within limits | None for contributions; 8 % social lump-sum levy where 11 or more employees | No | Yes, at 100 % with no allowance | Yes |
| Employer supplementary pension contribution within limits | None for contributions; 20 % social lump-sum levy | No | Yes, at 100 % with no allowance | No, within limits |
| Value-sharing bonus within the cap | None | No | Yes, unless the enhanced regime applies | Yes, unless the enhanced regime applies |
| Incentive-scheme amount, invested | None | No | Yes, at 100 % with no allowance | No |
| Profit-sharing amount, invested | None | No | Yes, at 100 % with no allowance | No |
| Statutory severance within the exempt fraction | None | No, within two annual ceilings | Only above the legal or agreed amount | No, within limits |
| Contractual termination indemnity | None for contributions within limits; 40 % specific employer contribution | No, within limits | Only above the legal or agreed amount | No, within limits |

Legal basis: Social Security Code, Articles L136-1-1, L241-3, L241-13, L242-1, D242-1, L137-15 and following; national interprofessional agreement of 17 November 2017 on the supplementary pension scheme; national interprofessional agreement of 14 March 1947 as continued for the 1.50 % death-and-disability contribution; Arrêté of 20 December 2002 (professional expenses); Arrêté of 10 December 2002 (benefits in kind).

## Module 5: Social Security & Pension Systems


### 5.1 Contribution Types and Rates


#### List all mandatory social security and pension contributions for both employer and employee.

France has no single "social security contribution". An ordinary private-sector payslip carries between eighteen and twenty-four separate levies, collected by three networks — the contribution collection body (URSSAF) for the general scheme and most attached levies, the supplementary pension institutions (Agirc-Arrco), and the insurers of the compulsory health and death-and-disability cover — but all declared through one monthly DSN.

| # | Contribution | Employee | Employer |
|---|---|---|---|
| 1 | Health, maternity, disability, death | — | 13.00 % |
| 2 | Additional local health contribution, Alsace-Moselle only | 1.30 % | — |
| 3 | Old-age, capped | 6.90 % | 8.55 % |
| 4 | Old-age, uncapped | 0.40 % | 2.11 % |
| 5 | Family allowances | — | 5.25 % |
| 6 | Industrial accidents and occupational disease | — | Establishment-specific net rate |
| 7 | Autonomy solidarity contribution | — | 0.30 % |
| 8 | National housing aid fund (fewer than 50 employees) | — | 0.10 % on the capped band |
| 9 | National housing aid fund (50 employees or more) | — | 0.50 % on total pay |
| 10 | Social dialogue contribution | 0.016 % | 0.016 % |
| 11 | Mobility levy (11 or more employees, where a transport authority has set a rate) | — | Local rate |
| 12 | Supplementary pension, band 1 | 3.15 % | 4.72 % |
| 13 | Supplementary pension, band 2 | 8.64 % | 12.95 % |
| 14 | General balance contribution, band 1 | 0.86 % | 1.29 % |
| 15 | General balance contribution, band 2 | 1.08 % | 1.62 % |
| 16 | Technical balance contribution | 0.14 % | 0.21 % |
| 17 | Executive employment association contribution (managerial grade) | 0.024 % | 0.036 % |
| 18 | Managerial-grade death-and-disability contribution | — | 1.50 % on the capped band |
| 19 | Unemployment insurance | — | 4.00 % |
| 20 | Wage guarantee scheme | — | 0.25 % |
| 21 | General social contribution, deductible portion | 6.80 % | — |
| 22 | General social contribution, non-deductible portion | 2.40 % | — |
| 23 | Social debt repayment contribution | 0.50 % | — |
| 24 | Compulsory health cover | Up to 50 % of the premium | At least 50 % of the premium |
| 25 | Single training and apprenticeship contribution | — | 0.55 % or 1.00 % training, plus 0.68 % apprenticeship tax |

Two frequently assumed contributions do not exist in metropolitan France: there is no employee unemployment contribution — it was abolished on 1 January 2019 — and there is no employee health contribution outside Alsace-Moselle. The general social contribution and the social debt repayment contribution, at a combined 9.70 %, are the employee's health and solidarity funding.
The single most important structural change for 2026 is on the employer side and does not appear in the table above as a rate: the reduced rates for health and family allowances have been abolished. Until 31 December 2025 an employer paid 7.00 % rather than 13.00 % for health, and 3.45 % rather than 5.25 % for family allowances, where the employee's pay was below defined multiples of the minimum wage. Both reduced-rate bands are repealed from 1 January 2026 and their value is delivered instead through the unified degressive general reduction described in section 5.2. Every employer now applies the full 13.00 % and 5.25 % rates, and the relief is a separate, calculated deduction.

#### Are contributions managed at a national or sub-national level?

Nationally, with two genuine territorial variations and one establishment-level rate.

| Level | What is set there |
|---|---|
| National | All contribution rates in the table above except items 6, 9 and 11; the social security ceiling; the general reduction parameters |
| Regional / establishment | The industrial accident net rate, set per establishment by the regional sickness insurance fund from the establishment's risk classification and, above a size threshold, its own claims history |
| Local transport authority | The mobility levy rate, which depends on the commune where the establishment is located and is nil where no authority has set one |
| Alsace-Moselle | The additional 1.30 % employee health contribution, triggered by the place of work, not by the employee's residence |
| Overseas departments | Specific reduced-rate exemption schemes replace or modify the general reduction |

Administratively, contributions are collected by a national network — URSSAF for the general scheme, the agricultural social mutual fund for agricultural employers — and the employer deals with the office covering its establishment. This is an administrative allocation, not a rate difference.
Legal basis: Social Security Code, Articles L136-1 to L136-8, L241-1 to L241-6, L242-1, L243-1-2, L325-1, D242-6-1 and following; Ordinance n° 96-50 of 24 January 1996; national interprofessional agreement of 17 November 2017 on the supplementary pension scheme; unemployment insurance convention of 15 November 2024.

### 5.1.1 Contribution Basis Definition


#### For each mandatory contribution, provide the statutory definition of the earnings base.


| Contribution | Statutory base | Text |
|---|---|---|
| Health, family allowances, uncapped old-age, autonomy solidarity, industrial accidents, social dialogue, mobility levy, training and apprenticeship levies | All sums paid to the worker in consideration of or on the occasion of the work — total gross pay, uncapped | Social Security Code Article L242-1 |
| Old-age, capped | The same base, limited to one monthly ceiling: EUR 4,005 in 2026 | Articles L241-3 and D242-1 |
| National housing aid fund, employers with fewer than 50 employees | Capped band | Article L834-1 |
| National housing aid fund, employers with 50 or more | Total gross pay | Article L834-1 |
| Supplementary pension and general balance contribution, band 1 | Gross pay up to one monthly ceiling | National interprofessional agreement of 17 November 2017 |
| Supplementary pension and general balance contribution, band 2 | Gross pay from one to eight monthly ceilings: EUR 4,005 to EUR 32,040 | Same |
| Technical balance contribution | Bands 1 and 2 together, but only for employees whose pay exceeds one ceiling | Same |
| Executive employment association contribution | Bands 1 and 2, managerial grade only | Executive employment association agreement |
| Managerial-grade death-and-disability contribution | Capped band | National interprofessional agreement of 14 March 1947, continued |
| Unemployment insurance and wage guarantee scheme | Gross pay up to four monthly ceilings: EUR 16,020 in 2026 | Unemployment insurance convention of 15 November 2024 |
| General social contribution and social debt repayment contribution | Gross pay reduced by a 1.75 % professional-expense allowance on the portion up to four annual ceilings (EUR 192,240), then no allowance; plus employer contributions to supplementary health, death-and-disability and supplementary pension cover, taken at 100 % with no allowance | Article L136-1-1 |


#### Clarify the legal definitions of any specific terms used.


| Term | Definition |
|---|---|
| Contribution base (assiette) | The amount to which a rate is applied. France has several, not one |
| Social security ceiling (plafond de la sécurité sociale) | An annual amount, fixed by decree, used to cap certain contributions and to define the bands. EUR 48,060 for 2026 |
| Band (tranche) | A slice of pay defined by reference to the ceiling. The basic scheme uses a capped band and an uncapped base; the supplementary pension scheme uses bands 1 and 2 |
| Gross pay (salaire brut) | Total remuneration before employee contributions, including benefits in kind |
| Benefit in kind (avantage en nature) | The provision of a good or service free of charge or below cost, valued at a statutory flat amount or at real cost |
| Professional expense (frais professionnels) | An outlay incurred by the employee in the interest of the business, reimbursed within the limits of the Arrêté of 20 December 2002 and outside the contribution base |
| Headcount (effectif) | The average annual workforce of the legal entity, computed under Social Security Code Article L130-1. A threshold crossed upward takes effect only after it has been reached for five consecutive calendar years; a threshold crossed downward takes effect immediately |
| Average wage per head (salaire moyen par tête) | The macroeconomic wage aggregate for the non-agricultural market sector used to revalue the social security ceiling |
| Minimum growth wage (SMIC) | The statutory hourly minimum wage, indexed on consumer prices for the lowest-income households and on half the gain in the basic hourly wage of manual and clerical workers |
| Guaranteed minimum (minimum garanti) | A separate statutory reference, indexed on prices only, used to value certain benefits in kind and allowances. EUR 4.35 from 1 June 2026 |

Which wage caliber drives which parameter — the reconciliation. France publishes several distinct wage aggregates and it is essential not to mix them. The reconciliation for 2026 is:

| Parameter | Wage caliber it derives from | 2026 value | Reconciliation |
|---|---|---|---|
| Social security ceiling, and everything expressed as a multiple of it — supplementary pension bands, the 4-ceiling unemployment and social-levy caps, the severance exemption caps, the savings-scheme caps | Average wage per head (salaire moyen par tête) in the non-agricultural market sector, per Social Security Code Article D242-17 | Monthly EUR 4,005; annual EUR 48,060 | The annual ceiling is exactly twelve times the monthly ceiling: 4,005 × 12 = 48,060. The monthly ceiling rose from EUR 3,925 in 2025, a ratio of 1.02038 — slightly above the announced "+2 %", because the decree applies the forecast average-wage growth plus a correction of the previous year's estimate, and then rounds. The headline percentage therefore does not reproduce the figure, and the ceiling itself must be taken from the decree, never computed from the percentage |
| Unified degressive general reduction of employer contributions | Minimum growth wage, at its 1 January 2026 value, frozen for the whole year | EUR 12.02 per hour; EUR 21,876.40 per year on a 1,820-hour basis | 12.02 × 1,820 = 21,876.40, and the reduction ceases to be available at three times that figure, EUR 65,629.20 — where the coefficient is at its floor of 0.0200 rather than at zero |
| Daily sickness benefit cap | Minimum growth wage, at its live value, at 1.4 times | Live: EUR 12.02 to 31 May, EUR 12.31 from 1 June | The benefit cap changed on 1 February and again on 1 July 2026, tracking the live wage |
| Enhanced value-sharing bonus regime | Minimum growth wage, at its live value, at 3 times | Live | — |
| Benefits in kind for meals; certain expense allowances | Guaranteed minimum, a price-indexed reference distinct from the minimum wage | EUR 4.35 from 1 June 2026 | Revalued on the same dates as the minimum wage but by a different mechanism |

The consequence for 2026 configuration is stated plainly: three different wage references are simultaneously live — the frozen minimum wage of EUR 12.02 for the general reduction, the live minimum wage of EUR 12.31 from 1 June for everything else indexed on it, and the average wage per head behind the ceiling. A single "minimum wage" parameter cannot express this.

#### Deliverable: Provide a comprehensive summary of current contribution rates, describing rates across regions and residential statuses, including tiers, ceilings, floors, and variations by age or gender.

Rates by band, metropolitan France, 2026

| Contribution | Band | Employee | Employer | Monthly band ceiling 2026 |
|---|---|---|---|---|
| Health, maternity, disability, death | Uncapped | — | 13.00 % | None |
| Old-age capped | Capped band | 6.90 % | 8.55 % | EUR 4,005 |
| Old-age uncapped | Uncapped | 0.40 % | 2.11 % | None |
| Family allowances | Uncapped | — | 5.25 % | None |
| Industrial accidents | Uncapped | — | Establishment rate | None |
| Autonomy solidarity | Uncapped | — | 0.30 % | None |
| Housing fund, under 50 employees | Capped band | — | 0.10 % | EUR 4,005 |
| Housing fund, 50 or more | Uncapped | — | 0.50 % | None |
| Social dialogue | Uncapped | 0.016 % | 0.016 % | None |
| Supplementary pension | Band 1 | 3.15 % | 4.72 % | EUR 4,005 |
| Supplementary pension | Band 2 | 8.64 % | 12.95 % | EUR 4,005 to 32,040 |
| General balance contribution | Band 1 | 0.86 % | 1.29 % | EUR 4,005 |
| General balance contribution | Band 2 | 1.08 % | 1.62 % | EUR 4,005 to 32,040 |
| Technical balance contribution | Bands 1 + 2, above the ceiling only | 0.14 % | 0.21 % | EUR 32,040 |
| Executive employment association | Bands 1 + 2, managerial grade | 0.024 % | 0.036 % | EUR 32,040 |
| Managerial death-and-disability | Capped band | — | 1.50 % | EUR 4,005 |
| Unemployment insurance | 4 ceilings | — | 4.00 % | EUR 16,020 |
| Wage guarantee scheme | 4 ceilings | — | 0.25 % | EUR 16,020 |
| General social contribution, deductible | 98.25 % base | 6.80 % | — | Allowance capped at EUR 192,240 per year |
| General social contribution, non-deductible | 98.25 % base | 2.40 % | — | Same |
| Social debt repayment contribution | 98.25 % base | 0.50 % | — | Same |

Derivation check on the employer / employee splits. The supplementary pension scheme fixes a total contribution and a 60 / 40 employer / employee split. Band 1: total 7.87 %, so 7.87 × 0.60 = 4.722 and 7.87 × 0.40 = 3.148, published as 4.72 % and 3.15 %. Band 2: total 21.59 %, so 12.954 and 8.636, published as 12.95 % and 8.64 %. General balance contribution band 1: total 2.15 %, giving 1.29 % and 0.86 %. Band 2: total 2.70 %, giving 1.62 % and 1.08 %. Technical balance contribution: total 0.35 %, giving 0.21 % and 0.14 %. Every published rate reproduces from its total and the 60 / 40 rule, which confirms the transcription.
Variation by region

| Region | Difference |
|---|---|
| Metropolitan France, general case | The table above |
| Alsace-Moselle (Bas-Rhin, Haut-Rhin, Moselle) | Add an employee health contribution of 1.30 % on total pay, maintained at that rate for 2026 by the local scheme's board. Triggered by the place of work |
| Overseas departments (Guadeloupe, Martinique, Guyane, La Réunion) | The general reduction is replaced by the specific overseas exemption scheme, which is more generous and structured differently |
| Mayotte | A distinct social security scheme with its own rates and its own minimum wage |

Variation by residence status

| Status | Treatment |
|---|---|
| Employee working in France, whatever their nationality or residence | Full French contributions. Social security follows the place of work, not tax residence |
| Employee posted to France from another EU or agreement state, holding a valid portable document A1 or equivalent certificate | No French contributions; the home scheme continues. The employer must still declare the posting and, where it operates in France, comply with the posted-worker declaration rules |
| Employee posted from France to another state | French contributions continue for the duration permitted by the applicable instrument |
| Employee working abroad for a French employer outside any coordination instrument (expatriate) | Outside the French compulsory scheme; voluntary cover through the fund for French nationals abroad |
| Company director treated as an employee | Full contributions except unemployment insurance and the wage guarantee scheme, from which they are excluded because they have no employment contract |

Variation by age
There is no age-graded contribution rate. Age affects the base and the exemptions instead:

| Population | Effect |
|---|---|
| Apprentices | Pay is a percentage of the minimum wage by age and contract year; the employer benefits from the general reduction; specific employee-contribution relief applies within the statutory threshold |
| Employees on a professionalisation contract | Reduced pay scale for those under 26; the general reduction applies |
| Trainees and interns | The statutory gratuity is exempt from contributions up to 15 % of the hourly ceiling per hour of attendance — EUR 4.50 per hour for 2026, the hourly ceiling being EUR 30. Above that threshold the excess is fully subject |
| Employees drawing a pension while working | Full contributions are due on the earnings |

Variation by gender
None. Differentiating any element of pay or of contribution by gender is prohibited by Labour Code Articles L3221-2 and L1142-1. Any client requirement to model a gender-dependent rate should be treated as an error in the requirement.
Legal basis: Social Security Code, Articles L130-1, L136-1-1, L241-3, L241-6, L242-1, L325-1, L834-1, D242-1, D242-17; Labour Code, Articles L1142-1 and L3221-2; national interprofessional agreement of 17 November 2017; unemployment insurance convention of 15 November 2024; Arrêté of 22 December 2025 (2026 ceiling); EU Regulation (EC) No 883/2004.

### 5.2 Calculation Logic and Edge Cases


#### What is the step-by-step calculation logic for all types of social security contributions?

Step 1 — Establish gross pay subject to contributions. Total remuneration under Article L242-1, including benefits in kind at their statutory value, excluding evidenced professional expenses within the limits.
Step 2 — Determine the period's ceiling entitlement. Start from the monthly ceiling of EUR 4,005 and prorate it for part-time work, for a part month of employment, and for unpaid absence, using the same method used to prorate the salary.
Step 3 — Slice gross pay into the bands. Capped band; uncapped base; supplementary pension bands 1 and 2; the four-ceiling unemployment base.
Step 4 — Apply the employee rates to their respective bands, and deduct from gross.
Step 5 — Build the general social contribution base separately. Gross pay × 98.25 % on the portion up to four annual ceilings, then 100 %; then add the employer's contributions to supplementary health, death-and-disability and supplementary pension cover at 100 % with no allowance. Apply 6.80 % deductible, 2.40 % non-deductible and 0.50 %.
Step 6 — Apply the employer rates to their respective bands, in parallel.
Step 7 — Calculate the unified degressive general reduction and deduct it from the employer contributions.
The 2026 formula is:
C = Tmin + Tdelta × [ 0.5 × ( 3 × annual reference minimum wage
÷ annual gross pay − 1 ) ] ^ 1.75
with, for 2026:

| Parameter | Value |
|---|---|
| Tmin | 0.0200 |
| Tdelta, employer paying the housing fund at 0.10 % | 0.3781 |
| Tdelta, employer paying the housing fund at 0.50 % | 0.3821 |
| Exponent | 1.75 |
| Maximum coefficient | 0.3981 or 0.4021 respectively |
| Annual reference minimum wage | EUR 21,876.40, being EUR 12.02 × 1,820 hours, frozen for the whole of 2026 |
| Rounding of the coefficient | Four decimals, to the nearest ten-thousandth |
| Eligibility threshold | Annual gross pay below 3 × EUR 21,876.40 = EUR 65,629.20 |
| Behaviour at the threshold | The coefficient does not decay to zero. It falls to its floor of Tmin = 0.0200 as pay approaches three times the reference wage, and the reduction then stops altogether because the eligibility threshold is passed. This is a cliff of two percentage points, not a taper: an employee on EUR 65,629 attracts relief of about 2 % of pay and an employee on EUR 65,630 attracts none. An engine that models the curve as decaying smoothly to zero understates the relief across the whole upper range and misses the cliff |
| Pay taken into account | Annual gross pay subject to contributions, increased by any value-sharing bonus paid in the year. The bonus is outside the contribution bands but is inside the reference pay for this calculation |

The reduction equals the coefficient × annual gross pay, and is imputed against the employer contributions it covers: health, capped and uncapped old-age, family allowances, the housing fund, the autonomy solidarity contribution, the supplementary pension and general balance contributions, unemployment insurance, the social dialogue contribution, and a fixed 0.49 percentage points of the industrial accident contribution — the mutualised fraction set for 2026 by Social Security Code Article D241-2-4, down from 0.50 in 2025. The establishment's actual industrial accident rate is not used in the reduction; only the 0.49 points.
The calculation is annual. In practice it is applied provisionally each month on year-to-date figures and reconciled cumulatively, in the same movement as the ceiling reconciliation.
Step 8 — Apply any other targeted reliefs, principally the flat employer deduction on overtime hours.
Step 9 — Reconcile the ceiling cumulatively (progressive ceiling reconciliation).
Step 10 — Round. Employee and employer amounts at the cent on the payslip; aggregate blocks to the whole euro in the DSN.

#### Are contributions based on actual or standard salary?

On actual pay. Article L242-1 bases contributions on the sums actually paid, and there is no notional or standard-salary basis for ordinary employment.
Three exceptions exist and all are narrow:

| Population | Basis |
|---|---|
| Occasional trainers, holiday-centre staff, certain artists and sports officials | Flat contribution bases fixed by ministerial order, banded by the amount paid |
| Employees whose pay includes a flat-rate professional-expense deduction, in specified sectors such as construction and journalism | Contributions are calculated on gross pay increased by the reimbursed expenses, then reduced by the flat percentage, subject to an annual cap |
| Interns | The gratuity is exempt up to 15 % of the hourly ceiling per hour of attendance; only the excess is a contribution base |


#### Describe rules for eligibility, joining month, termination month, mid-period hires, mid-period terminations, and mid-period salary changes.

Eligibility. Affiliation is automatic and immediate from the first hour of work. There is no waiting period, no minimum earnings threshold and no opt-out. The employer must file the pre-hire declaration within the eight days preceding the start and in any event before the employee begins work.
Joining month. Contributions are due from the first day of employment. The monthly ceiling is prorated to the days of employment. The general reduction is calculated on the annual pay actually received from the hire date, with the annual reference minimum wage prorated to the same period.
Termination month. Contributions are due to the last day of the contract, including on the final settlement. The ceiling is prorated to the days of employment. The ceiling reconciliation and the annual reduction reconciliation must both be run in the final payslip, not deferred to the year end.
Mid-period salary change. No proration of the ceiling: the employee was present for the whole month, so the full monthly ceiling applies. The two salary levels are simply summed into one gross for the month. This is the case most often modelled wrongly, because systems that prorate the ceiling on any change will halve it.
Successive contracts with the same employer in the same year. Since January 2022 the ceiling is no longer prorated contract by contract. The reconciliation takes account of all sums paid since the start date of the first contract in the year, so a temporary employee returning for a second assignment continues the same cumulative calculation rather than restarting it.
Illustration — proration of the monthly ceiling

| Situation | Prorated ceiling for the month |
|---|---|
| Full-time, present all of March 2026 | EUR 4,005.00 |
| Hired on 16 March 2026 (16 calendar days of 31) | 4,005.00 × 16 ÷ 31 = EUR 2,067.10 |
| Part-time at 80 % (121.33 hours against 151.67) | 4,005.00 × 121.33 ÷ 151.67 = EUR 3,203.85 |
| Left on 10 March 2026 (10 calendar days of 31) | 4,005.00 × 10 ÷ 31 = EUR 1,292.00 |
| Salary increased on 15 March 2026, employee present all month | EUR 4,005.00 — no proration |


#### Do different payment frequencies affect contribution rates or parameters?

Rates never change with frequency. The ceiling does, because it is expressed per period. The decree of 22 December 2025 fixes the 2026 ceiling for each period; the values needed for ordinary payroll are:

| Period | 2026 ceiling |
|---|---|
| Annual | EUR 48,060 |
| Quarterly | EUR 12,015 (three monthly ceilings) |
| Monthly | EUR 4,005 |
| Daily | EUR 220 |
| Hourly, for engagements shorter than five hours | EUR 30 |

Fortnightly and weekly values are also published in the decree and should be taken from it where a client operates one of the fortnightly cycles permitted by Labour Code Article L3242-3; they are not reproduced here because they are used by a small minority of employers and the decree is the only reliable source.
Whatever the period ceiling used, the annual reconciliation converges on the annual figure, so the choice of periodicity affects cash flow across the year but not the total.

#### Detail variations based on employee age or gender.

Gender: none. Any gender-based variation in pay or contributions is prohibited.
Age: no rate varies by age, but three age-linked populations have a distinct contribution profile.

| Population | Age link | Effect |
|---|---|---|
| Apprentices | Pay scale runs by age band and contract year, from 27 % to 78 % of the minimum wage | Employee contribution relief within the statutory threshold; the employer applies the general reduction |
| Professionalisation contracts | Reduced pay scale below 26 | Ordinary contributions, plus the general reduction |
| Employees drawing a pension while working | Statutory retirement age | Full contributions on earnings; since 1 September 2023 these can generate new pension entitlement in defined circumstances |


#### Is there a minimum number of working days required for contributions?

No. Contributions are due from the first hour of the first day. There is no de minimis threshold in hours, days or earnings. A one-day assignment generates a pre-hire declaration, a payslip, a DSN entry and a full set of contributions, with the ceiling prorated to that day, or the daily ceiling of EUR 220 applied where the daily basis is used.
The one adjacent rule that is sometimes mistaken for a threshold is the validation of a pension quarter, which requires earnings of at least 150 times the hourly minimum wage in the year. That is an entitlement rule for the employee, not a contribution rule for the employer: contributions are due regardless.

#### How are contributions calculated for Board of Directors who are also employees?

France distinguishes sharply between officers treated as employees for social security and officers who are self-employed. The test is the legal form of the company and the officer's shareholding, not the existence of a contract.

| Position | Social security status | Contributions |
|---|---|---|
| Chair or managing director of a simplified joint-stock company or a public limited company | Treated as an employee (assimilé salarié) | Full general-scheme and supplementary pension contributions on the officer's pay, except unemployment insurance and the wage guarantee scheme, from which they are excluded for want of an employment contract |
| Minority or equal-shareholding manager of a private limited company | Treated as an employee | Same as above |
| Majority-shareholding manager of a private limited company | Self-employed | Outside payroll; contributions are assessed and paid personally under the self-employed scheme. Out of scope for the payroll engine |
| Board member holding a genuine and distinct employment contract alongside the office | Employee for the employment contract | Full contributions including unemployment insurance on the employment pay; the officer's pay follows the officer rules |
| Board member's attendance fees (jetons de présence) | Not employment income | Outside social security contributions; taxed as investment income, and subject to the 20 % social lump-sum levy where paid by a company subject to that levy |

The unemployment exclusion is a genuine payroll rule and a frequent client query: an officer treated as an employee does not contribute to unemployment insurance and correspondingly acquires no unemployment entitlement, whatever the company would prefer.

#### Are year-end adjustments required?

Yes — four, and all are compulsory rather than optional good practice.

| Adjustment | What it does | When |
|---|---|---|
| Progressive ceiling reconciliation | Compares cumulative pay to the cumulative ceiling and corrects the split between the capped and uncapped bands | Every month, and definitively in December or in the final payslip |
| Annual reconciliation of the unified degressive reduction | The reduction is an annual amount; the monthly figures are provisional | December, or in the final payslip |
| Capping of the 1.75 % allowance on the general social contribution base | The allowance stops at four annual ceilings, EUR 192,240 for 2026; once cumulative pay passes that point the allowance ceases and any excess already granted is recovered | When the threshold is crossed |
| Reconciliation of the exempt overtime pay against the EUR 7,500 annual income tax cap | The cap is annual and cumulative | When the threshold is crossed, and at the year end |

Where an adjustment relates to a prior period, it is reported in the DSN through the correction mechanism, which carries the period concerned so that the collecting body allocates it correctly. Correcting a prior period by adding an amount to the current month's base is wrong and will be picked up on inspection.
Legal basis: Social Security Code, Articles L241-13, L241-17, L241-18, L242-1, R242-2, D241-2-4, D241-7 to D241-11, D242-1; Décret n° 2025-1446 of 31 December 2025 and Décret n° 2026-509 of 12 June 2026 (parameters of the unified degressive reduction and freezing of the minimum-wage reference); Arrêté of 22 December 2025 (2026 ceiling); Labour Code, Articles L1221-10 and L3242-3.

### 5.3 Voluntary Contributions & Private Schemes


#### Can employees and employers make additional voluntary contributions?

Yes, in three distinct forms, and only the first two run through payroll.

| Form | Mechanism | Runs through payroll |
|---|---|---|
| Supplementary pension scheme set up by the employer — a defined-contribution company retirement savings plan, or an obligatory company retirement plan | Employer and employee contributions, compulsory for the category of staff covered once established | Yes |
| Voluntary employee saving into a company savings plan or a collective retirement savings plan, with employer matching | Employee payment, employer top-up within statutory caps | Yes, for the employer top-up and the deduction of the employee payment |
| Individual purchase of pension quarters, and voluntary insurance for expatriates | Paid by the individual to the fund | No |

For a scheme's contributions to be exempt from social security contributions, the scheme must be collective and compulsory: it must cover an objectively defined category of staff, and membership must be compulsory for everyone in that category. A scheme offered on an individual opt-in basis loses the exemption entirely, and the employer's contribution becomes ordinary pay.

#### Which employee contributions are allowed as pre-tax deductions?


| Employee contribution | Deductible from the net taxable amount | Limit |
|---|---|---|
| Basic old-age, capped and uncapped | Yes | None |
| Supplementary pension, general balance and technical balance contributions | Yes | None |
| General social contribution, deductible portion at 6.80 % | Yes | By construction |
| General social contribution, non-deductible portion at 2.40 %, and the social debt repayment contribution at 0.50 % | No — added back to the net taxable amount | — |
| Employee share of the compulsory health cover | Yes | Within the combined limit below |
| Employee share of a death-and-disability scheme | Yes | 5 % of the annual ceiling plus 2 % of remuneration, the total not exceeding 2 % of eight annual ceilings (General Tax Code Article 83, 1° quater) |
| Employee share of a supplementary pension scheme | Yes | 8 % of gross annual remuneration, itself capped at eight annual ceilings (General Tax Code Article 83, 2°) |
| Voluntary payment into a company savings plan | No | It is a saving, not a contribution |

The corresponding social security exemption limits are different figures under a different text, and this is a classic source of error — one limit for tax, another for contributions, on the same premium.

| Employer and employee contributions to | Social exemption limit, Social Security Code Article D242-1 | 2026 value |
|---|---|---|
| Supplementary health and death-and-disability cover, taken together | 6 % of the annual ceiling + 1.5 % of the employee's gross pay, the total not exceeding 12 % of the annual ceiling | 6 % × 48,060 = EUR 2,883.60, plus 1.5 % of pay, capped at EUR 5,767.20 |
| Supplementary pension cover | The higher of 5 % of the annual ceiling, or 5 % of pay capped at five annual ceilings | At least EUR 2,403.00 |

Amounts above these limits are reintegrated into the social security contribution base. Note the combined cap: an employer whose health premium already absorbs the envelope will find its death-and-disability premium partly reintegrated even though each policy looks compliant in isolation.

#### Are there private insurance schemes with employer and employee contributions?

Yes, and one of them is compulsory for every private-sector employer.

| Scheme | Compulsory | Employer share | Notes |
|---|---|---|---|
| Supplementary health cover (complémentaire santé, commonly "mutuelle") | Yes, for every private-sector employer, for all employees | At least 50 % of the premium | Must at minimum cover the statutory minimum basket of care: the patient co-payment on general and hospital medicine, the full daily hospital charge of EUR 20 per day, dental prosthetics at 125 % of the social security tariff, and a defined optical allowance |
| Managerial-grade death-and-disability cover | Yes, for managerial-grade employees | 1.50 % of the capped band, wholly employer-paid, with at least half devoted to death cover | Failure to insure makes the employer liable to the beneficiaries for a capital sum equal to three years' pay |
| Wider death-and-disability cover for all staff | Only where the collective agreement imposes it — and many do | Per the agreement | Covers sick pay top-up, disability and death |
| Supplementary pension scheme | No | Per the scheme | Contributions exempt within the limits above |

The health cover carries a defined set of exemptions from membership, which are lawful only if the employee requests them in writing and provides evidence, and only if the founding document of the scheme provides for them:
- employees already covered as a dependant under a spouse's compulsory scheme;
- employees present when the scheme was set up unilaterally by the employer and required to contribute;
- employees on a fixed-term contract or an assignment shorter than three months who hold responsible individual cover;
- part-time employees whose contribution would exceed 10 % of their pay;
- employees covered by certain other compulsory schemes, including the solidarity health scheme.
An exemption granted without evidence is the most common finding in a contribution inspection of this area, because the employer's contribution is then treated as ordinary pay for the whole period concerned.

#### What documents or declarations are required from an employee?


| Document | Purpose | Frequency |
|---|---|---|
| Written request for exemption from the health cover, with supporting evidence | Establishes the lawfulness of the exemption | On hire or on scheme set-up, and renewed annually |
| Certificate of cover from a spouse's employer | Evidences the dependant exemption | Annually |
| Beneficiary designation for the death benefit | Directs payment of the death capital | On joining, and on any change of circumstances |
| Instruction to pay into a company savings plan, or to invest a profit-sharing entitlement | Directs the amount and the vehicle | Per event; a default investment rule applies if no instruction is given |
| Portable document A1 or equivalent certificate | Evidences continued affiliation to a foreign scheme | For the duration of the posting |
| Election to have profit-sharing paid immediately rather than invested | Changes the tax treatment — an immediate payment is taxable, an invested amount is not | At each allocation, within the statutory election window |

Legal basis: Social Security Code, Articles L911-1 and following, L242-1, II, D242-1, R242-1-1 to R242-1-6; General Tax Code, Article 83, 1° quater and 2°; Labour Code, Articles L911-7 and D911-1 (minimum basket of care); national interprofessional agreement of 14 March 1947 as continued (managerial-grade death-and-disability cover); national interprofessional agreement of 11 January 2013.

## Module 6: Income Tax Withholding System


### 6.0 Resident and Non-Resident Treatment Matrix

France operates two entirely separate employer withholding mechanisms depending on the employee's tax residence, and they are not variants of each other: they use different bases, different rates, different legal texts and different DSN reporting. Nothing in this module may be read across from one column to the other.

| Income type | RESIDENT — withholding at source (prélèvement à la source) | NON-RESIDENT — specific withholding (retenue à la source) |
|---|---|---|
| Regular salary | Rate: the personal rate supplied by the tax administration, or an individualised rate, or the default grid where no rate has been transmitted. Base: net taxable amount for the month. Method: base × rate, rounded to the nearest euro. General Tax Code Articles 204 A to 204 N | Rate: progressive scale of 0 % / 12 % / 20 % applied to periodic bands. Base: net taxable amount after a 10 % flat deduction for professional expenses. Method: the 0 % and 12 % fractions are liberatory — the tax is final and the income is excluded from the annual assessment; the 20 % fraction is not liberatory and is credited against the final assessment. General Tax Code Article 182 A |
| Annual bonus, thirteenth month | Same as regular salary. Added to the month's net taxable amount and taxed at the same fixed rate. There is no separate bonus schedule and no spreading | Aggregated with the salary of the period of payment and run through the same periodic 0 / 12 / 20 bands. A large bonus therefore pushes the period into the 20 % band |
| Severance and termination payments | The exempt fraction (Module 9) is outside the net taxable amount; the taxable excess is added to the month's net taxable amount and taxed at the employee's withholding rate | The exempt fraction is likewise outside; the taxable excess enters the Article 182 A base for the period. The 20 % fraction remains creditable and a return is required |
| Equity and share incentives — free share awards, share options | The acquisition gain is taxable on disposal, not through payroll withholding. No withholding at source applies; the employer reports the award and the gain but withholds no income tax. The employee pays through the annual assessment. The employee's 10 % specific contribution on the acquisition gain is a social levy, not income tax | The acquisition gain from French-source awards is subject to a specific withholding under General Tax Code Article 182 A ter, operated by the entity making the award. Rates follow the applicable regime for the gain concerned. This is not the ordinary payroll withholding and must be modelled separately |
| Contractor or labour-service pay (self-employed, service provider) | Not in payroll scope. A genuinely self-employed contractor invoices the company; no employer withholding applies and the contractor accounts for their own tax and contributions | A withholding under General Tax Code Article 182 B applies at 25 % to sums paid to a non-resident for services rendered or used in France. This is an accounts-payable obligation, not a payroll obligation, and it is out of scope for the payroll engine — but it must be flagged to the client's finance function because it is frequently missed |
| Benefits in kind | Included in the net taxable amount at their statutory flat or real value, and therefore taxed at the withholding rate like cash pay | Included in the Article 182 A base at the same values, after the 10 % flat deduction |

Additional non-resident rules that must be configured:
- Overseas department rates. Where the income arises in Guadeloupe, Martinique, Guyane, La Réunion or Mayotte, the 12 % and 20 % rates fall to 8 % and 14.4 % respectively (General Tax Code Article 182 A).
- Minimum tax rate on assessment. Independently of the payroll withholding, a non-resident's French income is assessed at a minimum rate of 20 % up to EUR 29,579 of French net taxable income and 30 % above, or 14.4 % and 20 % for income arising in the overseas departments (General Tax Code Article 197 A). The taxpayer may displace the minimum rate by proving that the rate applicable to their worldwide income would be lower. This operates at assessment level, not at withholding level, and must not be modelled inside the payroll engine.
- Treaty override. A double tax treaty may remove France's right to tax the employment income altogether, typically where the employee spends fewer than 183 days in France, is paid by a non-French employer and the cost is not borne by a French establishment. Where the treaty exempts, no withholding is due. Treaty analysis is a per-assignment determination and is not automatable.
- Social security is a separate question. A non-resident for tax may still be fully liable to French social security if they work in France, and a French tax resident may be outside French social security if they hold a portable document A1 for another state. The two tests are decided independently (Module 2.2).

### 6.1 System Overview and Methodology


#### Describe the country's income tax withholding system.

France operates withholding at source (prélèvement à la source, PAS) for residents, introduced on 1 January 2019 by Article 60 of the Finance Act for 2017 and now codified at General Tax Code Articles 204 A to 204 N.
Its defining characteristic is that the employer performs no tax computation. The tax administration calculates a rate from the employee's most recent annual return, taking the whole tax household into account, and transmits it to the employer through the DSN return flow. The employer applies that rate to the net taxable amount, deducts the result from net pay, declares it in the DSN and remits it by direct debit. It never sees the employee's family situation, never applies an allowance and never operates a progressive scale.
Where no rate has been transmitted — a new hire, a first-time taxpayer, an employee who has opted for confidentiality — the employer applies a statutory default grid (grille de taux par défaut, commonly called the neutral rate) determined solely by the amount of the monthly net taxable pay. The default grid ignores family circumstances entirely, which is why an employee with dependants will usually be over-withheld on it and should be encouraged to have their personal rate transmitted.
The system is a cash-flow mechanism, not a final settlement. The employee still files an annual return; the withholding is credited against the assessed liability, and any balance is paid or refunded in the following autumn.

#### What types of taxes are withheld by the employer?

Only one: income tax (impôt sur le revenu). France has no municipal, regional or provincial income tax on employment income, no separate employee surcharge withheld through payroll, and no employee-side solidarity levy.
The 9.70 % general social contribution and social debt repayment contribution are frequently mistaken for a tax withheld at source. They are social contributions, not income tax: they are governed by the Social Security Code, collected by URSSAF rather than the tax administration, calculated on a different base, and 6.80 of the 9.70 points is deductible from the income tax base while the remaining 2.90 is not. They are covered in Module 5.
For completeness, the employer itself may owe taxes computed on payroll but not withheld from the employee:

| Employer tax | Who owes it | Rate |
|---|---|---|
| Payroll tax (taxe sur les salaires) | Employers not liable to value added tax on at least 90 % of turnover — mainly banks, insurers, associations, health bodies and holding companies | 4.25 %, 8.50 % and 13.60 % by band |
| Apprenticeship tax | Most employers | 0.68 % of payroll, 0.44 % in Alsace-Moselle |
| Training contribution | All employers | 0.55 % under 11 employees, 1.00 % at 11 and above |
| Construction investment contribution | Employers with 50 or more employees | 0.45 % of payroll |

These are employer costs. They never appear in the employee's gross-to-net chain.

#### At what level are tax rates published (central or state)?

Centrally, and only centrally. The income tax scale, the withholding default grids and the non-resident scale are all fixed by the annual Finance Act voted by Parliament and published in the official journal, then restated by the tax administration in its official doctrine. There is no local rate-setting power over employment income.
For 2026 the relevant instrument is LOI n° 2026-103 of 19 February 2026, the Finance Act for 2026, and its Article 4 both indexes the income tax scale by 0.9 % and revalues the non-resident withholding bands.
Legal basis: General Tax Code, Articles 197, 197 A, 204 A to 204 N, 182 A, 182 A ter, 182 B, 231; LOI n° 2026-103 of 19 February 2026, Article 4; Official Tax Bulletin BOI-BAREME-000037 and BOI-BAREME-000043.

### 6.1.1 Taxable Income Definition


#### Provide the statutory definition of 'Taxable Income'.

For payroll purposes the operative quantity is the net taxable amount (montant net imposable), and it is not defined in a single article. It is built from General Tax Code Article 79 — which brings salaries, allowances, emoluments and benefits within the category of taxable employment income — read with Article 83, which lists the deductible items, and Article 204 F, which fixes the base for the withholding.
Working definition: the net taxable amount is total employment remuneration of the period, including benefits in kind, less the employee social contributions that are deductible for income tax, plus the social contributions that are not deductible and the employer contributions that are not exempt, less any statutorily exempt element.

#### Explain how this base is derived from total gross earnings.

Gross pay for the period
−  employee old-age contributions, capped and uncapped
−  employee supplementary pension, general balance and
technical balance contributions
−  general social contribution, deductible portion (6.80 %)
−  employee share of the compulsory health cover
−  employee share of a death-and-disability or supplementary
pension scheme, within the Article 83 limits
+  general social contribution, non-deductible portion (2.40 %)
+  social debt repayment contribution (0.50 %)
+  employer contribution to the compulsory health cover
+  employer contribution to a death-and-disability scheme
−  exempt overtime pay, within the EUR 7,500 annual cap
−  the exempt fraction of any termination payment
−  the exempt fraction of an expatriation premium under the
inbound-assignee regime
=  NET TAXABLE AMOUNT
Two derivations are load-bearing and are wrong in a surprising number of implementations:
- The employer's health-cover contribution is added. It is exempt from social security contributions within limits, but it has been non-deductible for income tax since 2014 and must be added to the net taxable amount. Omitting it under-withholds every month.
- The net taxable amount is higher than the net payable before tax. It is not a variant of the net figure. A system that applies the withholding rate to net pay under-withholds by roughly the value of the non-deductible levies and the employer health contribution.
Not in the net taxable amount at all: reimbursed professional expenses within the limits, meal-voucher employer shares within the limits, the 50 % transport reimbursement, and invested profit-sharing and incentive-scheme amounts.

#### Deliverable: Provide a step-by-step decision guide to determine the correct tax schedule for an employee.

START
|
1. Is the employee tax-resident in France under General Tax
Code Article 4 B, as modified by any applicable treaty?
|
|--- NO  --> 2. Does a double tax treaty give France the right
|             to tax this employment income?
|             |--- NO  --> NO FRENCH WITHHOLDING. Document the
|             |             treaty article relied on. Social
|             |             security is decided separately.
|             |--- YES --> 3. Does the income arise in an
|                           overseas department?
|                           |--- YES --> ARTICLE 182 A SCALE
|                           |            at 0 % / 8 % / 14.4 %
|                           |--- NO  --> ARTICLE 182 A SCALE
|                                        at 0 % / 12 % / 20 %
|                           In both cases: 10 % flat professional-
|                           expense deduction first; 0 % and the
|                           12 % (or 8 %) fraction are liberatory;
|                           the top fraction is creditable.
|
|--- YES -> 4. Has the tax administration transmitted a rate for
this employee in the DSN return flow, still within
its validity period?
|
|--- YES --> APPLY THAT RATE.
|            It may be a personal rate, an
|            individualised rate for a couple, or
|            a rate the employee has had reduced or
|            increased. The employer applies it as
|            received and asks no questions.
|
|--- NO  --> 5. Is this a fixed-term contract or an
assignment whose initial term does not
exceed two months?
|--- YES --> DEFAULT GRID, after
|            deducting the short-contract
|            allowance of EUR 748 per
|            month (EUR 766 from 1 June
|            2026; the January figure may
|            be kept all year by
|            administrative tolerance)
|--- NO  --> DEFAULT GRID on the full
net taxable amount
|
6. Which default grid applies to the period?
|--- Pay for January to April 2026 --> the 2025 grid
|--- Pay from 1 May 2026            --> the 2026 grid
|--- Employee based in Guadeloupe, Martinique
|    or La Réunion                  --> that territory's grid
|--- Employee based in Guyane or Mayotte --> that grid
|--- Otherwise                       --> the metropolitan grid
END

#### Deliverable: Explain the official tax calculation method with formulas and examples.

A. The employer's calculation — withholding at source
Withholding = Net taxable amount for the period × the applicable rate
Rounded to the nearest euro for the remittance, with 0.50 counting as 1.00. That is the whole of the employer's arithmetic.
Worked example — resident on a personal rate. An employee has a net taxable amount of EUR 3,142.68 for June 2026 and a personal rate of 8.30 % transmitted by the tax administration.

| Step | Calculation | Result |
|---|---|---|
| 1. Net taxable amount | — | EUR 3,142.68 |
| 2. Apply the rate | 3,142.68 × 8.30 % | EUR 260.84 |
| 3. Deduct from net payable | — | EUR 260.84 withheld |
| 4. Round for the remittance | 260.84 → nearest euro | EUR 261 |

Worked example — resident on the default grid. A new hire, permanent contract, no rate yet transmitted, net taxable amount EUR 2,400.00 for June 2026. June falls after 1 May, so the 2026 metropolitan grid applies. EUR 2,400.00 falls in the band EUR 2,315 to EUR 2,737.99, giving a rate of 5.30 %.

| Step | Calculation | Result |
|---|---|---|
| 1. Net taxable amount | — | EUR 2,400.00 |
| 2. Read the 2026 grid | Band 2,315 – 2,737.99 | 5.30 % |
| 3. Withholding | 2,400.00 × 5.30 % | EUR 127.20 |

Note that the default grid is a flat rate read from a band, not a progressive scale. The whole EUR 2,400.00 is taxed at 5.30 %; there is no slicing.
B. The tax administration's calculation — how the personal rate is produced
The employer does not perform this calculation, but understanding it answers most employee queries.
Rate = ( income tax due on the household's employment-type income
÷ that income )   as computed from the most recent return
The tax on the household's total income is itself computed on the progressive scale by the family-quotient method:
1. Compute net taxable household income after the 10 % flat professional-expense deduction or actual expenses.
1. Divide by the number of family-quotient parts.
1. Apply the 2026 scale to the result.
1. Multiply back by the number of parts.
1. Apply the caps and reliefs, including the cap on the family-quotient benefit and the low-income discount.
The 2026 income tax scale, per family-quotient part (Finance Act for 2026, Article 4; applied to 2025 income):

| Band of net taxable income per part | Rate |
|---|---|
| Up to EUR 11,600 | 0 % |
| EUR 11,601 to EUR 29,579 | 11 % |
| EUR 29,580 to EUR 84,577 | 30 % |
| EUR 84,578 to EUR 181,917 | 41 % |
| Above EUR 181,917 | 45 % |

This scale is not used in payroll. It produces the rate that the tax administration transmits; the employer uses only that rate. Configuring the progressive scale into a payroll engine is a category error, and it is exactly the error that the separate default grid exists to prevent.
Legal basis: General Tax Code, Articles 79, 83, 197, 204 A to 204 N, 204 F, 204 H; LOI n° 2026-103 of 19 February 2026, Article 4; Official Tax Bulletin BOI-BAREME-000037.

### 6.2 Tax Rates and Logic


#### What are the latest tax rates by tax type, residential status, and payment frequency?

Default withholding grid — metropolitan France, 1 January to 30 April 2026 (the 2025 grid, carried over because the Finance Act for 2026 was enacted on 19 February 2026):

| Monthly net taxable amount | Rate |
|---|---|
| Below EUR 1,620 | 0 % |
| EUR 1,620 to 1,682.99 | 0.5 % |
| EUR 1,683 to 1,790.99 | 1.3 % |
| EUR 1,791 to 1,910.99 | 2.1 % |
| EUR 1,911 to 2,041.99 | 2.9 % |
| EUR 2,042 to 2,150.99 | 3.5 % |
| EUR 2,151 to 2,293.99 | 4.1 % |
| EUR 2,294 to 2,713.99 | 5.3 % |
| EUR 2,714 to 3,106.99 | 7.5 % |
| EUR 3,107 to 3,538.99 | 9.9 % |
| EUR 3,539 to 3,982.99 | 11.9 % |
| EUR 3,983 to 4,647.99 | 13.8 % |
| EUR 4,648 to 5,573.99 | 15.8 % |
| EUR 5,574 to 6,973.99 | 17.9 % |
| EUR 6,974 to 8,710.99 | 20 % |
| EUR 8,711 to 12,090.99 | 24 % |
| EUR 12,091 to 16,375.99 | 28 % |
| EUR 16,376 to 25,705.99 | 33 % |
| EUR 25,706 to 55,061.99 | 38 % |
| EUR 55,062 and above | 43 % |

Default withholding grid — metropolitan France, from 1 May 2026:

| Monthly net taxable amount | Rate |
|---|---|
| Below EUR 1,635 | 0 % |
| EUR 1,635 to 1,697.99 | 0.5 % |
| EUR 1,698 to 1,806.99 | 1.3 % |
| EUR 1,807 to 1,927.99 | 2.1 % |
| EUR 1,928 to 2,059.99 | 2.9 % |
| EUR 2,060 to 2,169.99 | 3.5 % |
| EUR 2,170 to 2,314.99 | 4.1 % |
| EUR 2,315 to 2,737.99 | 5.3 % |
| EUR 2,738 to 3,134.99 | 7.5 % |
| EUR 3,135 to 3,570.99 | 9.9 % |
| EUR 3,571 to 4,018.99 | 11.9 % |
| EUR 4,019 to 4,689.99 | 13.8 % |
| EUR 4,690 to 5,623.99 | 15.8 % |
| EUR 5,624 to 7,036.99 | 17.9 % |
| EUR 7,037 to 8,788.99 | 20 % |
| EUR 8,789 to 12,199.99 | 24 % |
| EUR 12,200 to 16,522.99 | 28 % |
| EUR 16,523 to 25,936.99 | 33 % |
| EUR 25,937 to 55,557.99 | 38 % |
| EUR 55,558 and above | 43 % |

The 2026 grid is the 2025 grid revalued by 0.9 %, the same indexation applied to the income tax scale. Both grids must be held simultaneously: the applicable grid is determined by the date the income is paid, so a payment made on 30 April 2026 uses the first grid and one made on 4 May 2026 uses the second. No retrospective adjustment is made for January to April; the two grids simply coexist in the tax year.
Overseas grids from 1 May 2026: the same twenty bands and the same twenty rates, with thresholds beginning at EUR 1,875 for Guadeloupe, Martinique and La Réunion (top band from EUR 60,893), and at EUR 2,008 for Guyane and Mayotte (top band from EUR 64,341).
Non-resident withholding scale under General Tax Code Article 182 A, income paid in 2026:

| Period | 0 % band | 12 % band | 20 % band |
|---|---|---|---|
| Annual | Up to EUR 17,275 | EUR 17,276 to 50,112 | Above EUR 50,112 |
| Quarterly | Up to EUR 4,319 | EUR 4,320 to 12,528 | Above EUR 12,528 |
| Monthly | Up to EUR 1,440 | EUR 1,441 to 4,176 | Above EUR 4,176 |
| Weekly | Up to EUR 332 | EUR 333 to 964 | Above EUR 964 |
| Daily | Up to EUR 55 | EUR 56 to 161 | Above EUR 161 |

In the overseas departments the 12 % and 20 % rates fall to 8 % and 14.4 %.
Verification of the upper annual limit. Secondary sources give this figure variously as EUR 50,112 and EUR 50,122. The published quarterly limit of EUR 12,528 multiplied by four gives exactly 50,112, and the monthly limit of EUR 4,176 multiplied by twelve gives exactly 50,112; the 2025 limit of EUR 49,665 indexed by the Finance Act's 0.9 % gives 50,111.98. Three independent derivations converge on EUR 50,112, and the ten-euro variant is a transcription error.

#### How are rates applied for different frequencies?

For residents, the rate is a percentage and is frequency-neutral. It applies unchanged to a monthly payslip, a mid-month advance settled in the same monthly payslip, or an off-cycle payment. Where more than one payment is made to the same employee in the same month, the rate applies to each, and there is no aggregation or re-banding.
The default grid, by contrast, is frequency-sensitive, because it reads a band from an amount. The tax administration publishes monthly, quarterly, weekly, daily and hourly versions of the grid, and the version matching the pay period must be used. Applying the monthly grid to a weekly payment produces a 0 % rate on nearly every payslip.
For non-residents, the Article 182 A scale is expressly published per period — annual, quarterly, monthly, weekly and daily — precisely because it is progressive. The employer applies the version matching the payment period and slices the base across the bands.

#### How does tax applicability and calculation logic differ by residential status?

The full comparison is in the matrix at section 6.0. The four operational differences to carry into configuration:

| Dimension | Resident | Non-resident |
|---|---|---|
| Rate source | Transmitted by the tax administration, or the default grid | The statutory Article 182 A scale; nothing is transmitted |
| Base | Net taxable amount, with no flat deduction | Net taxable amount after a 10 % flat professional-expense deduction |
| Method | Flat rate on the whole base | Progressive slicing across the 0 / 12 / 20 bands of the period |
| Finality | Never final; always credited against the annual assessment | The 0 % and 12 % fractions are liberatory and final; only the 20 % fraction is credited |
| DSN reporting | Withholding block with the rate type and rate | Reported under the non-resident withholding arrangements, not as ordinary withholding at source |

The liberatory character is the difference that most affects employees. A non-resident whose French pay stays within the 12 % band pays that and nothing more, and does not include the income in a French return. Once any part of the pay reaches the 20 % band, a return becomes necessary and the minimum-rate rules of Article 197 A come into play.

#### Provide the tax calculation logic covering eligibility, joining month, termination month, mid-month joining, mid-month terminations, and mid-month salary revisions.


| Situation | Treatment |
|---|---|
| Eligibility | Every employee receiving employment income is within the withholding system from the first payslip. There is no threshold and no election |
| Joining month | No rate will have been transmitted for a first payslip, because the tax administration derives the rate from the employer's own first DSN. Apply the default grid. The rate normally arrives in the return flow within five days of that first DSN and is applied from the following payslip |
| Joining on a contract of two months or less | Apply the default grid after deducting the short-contract allowance — EUR 748 per month, or EUR 766 from 1 June 2026, prorated for a part month |
| Termination month | Apply the rate in force on the payment date to the whole final settlement, including the taxable fraction of any severance. Do not annualise and do not attempt a year-end true-up: that is the tax administration's function |
| Mid-month joining or leaving | The withholding is applied to whatever net taxable amount is actually paid. Because the default grid reads a band from the amount, a part-month payment naturally falls in a lower band; no annualisation of the part-month amount is permitted |
| Mid-month salary revision | Irrelevant to the withholding. The month's net taxable amount is simply the sum of the two salary levels, and one rate applies to it |
| Rate arriving mid-month | Applied from the next payslip, not retrospectively |
| Rate expiring | Transmitted rates carry a validity period. On expiry, if no new rate has arrived, revert to the default grid. A payroll engine must date-check the rate on every run rather than treating it as a static employee attribute |


#### Do tax rates vary by gender or age?

No. Neither the income tax scale, the withholding rate, the default grid nor the non-resident scale varies by gender or by age. Gender-based differentiation is prohibited by law.
Two adjacent rules involve age but are not rate variations:
- Apprentices and interns are exempt from income tax on their pay up to an annual threshold equal to the annual minimum wage, and their exempt pay is outside the net taxable amount and therefore outside the withholding.
- Employees over 65 receive an additional allowance in the annual assessment where their income is below a threshold. It affects the rate the tax administration computes; it changes nothing the employer does.

#### What is the minimum tax rate applicable?

For residents there is no minimum. The default grid begins at 0 % for a monthly net taxable amount below EUR 1,635 from 1 May 2026, and a transmitted personal rate can itself be 0 %. An employer must apply a 0 % rate exactly as transmitted; it may not substitute a positive rate.
For non-residents two different figures are sometimes both called a minimum and they operate at different levels:

| Figure | Level | Content |
|---|---|---|
| 0 % band of the Article 182 A scale | Withholding, operated by the employer | Monthly pay up to EUR 1,440 bears no withholding |
| Minimum assessment rate under Article 197 A | Assessment, operated by the tax administration | 20 % up to EUR 29,579 of French net taxable income and 30 % above; 14.4 % and 20 % for overseas-source income. Displaceable by proof of a lower worldwide rate |

The distinction must be repeated in every downstream artefact. The Article 197 A minimum rate is an assessment-level rule: it must not be modelled in the payroll engine, in the wage type catalogue or in the data dictionary. A previous jurisdiction in this pipeline had an assessment-level levy wrongly propagated into withholding artefacts, and the shape of the error is identical here.
Legal basis: General Tax Code, Articles 182 A, 182 A ter, 182 B, 197 A, 204 A to 204 N, 204 H, 81 bis; LOI n° 2026-103 of 19 February 2026, Article 4; Official Tax Bulletin BOI-BAREME-000037 (default grids, version of 7 April 2026) and BOI-BAREME-000043 (non-resident scale, version of 2 April 2026).

### 6.3 Adjustments and Special Cases


#### For annualized tax systems, which salary components must be projected?

None. France does not annualise employment income for withholding purposes. The employer applies a rate to the amount actually paid in the period, and makes no projection, no estimate of full-year income and no cumulative recalculation.
This is a genuine simplification relative to cumulative-basis systems, and it must be stated affirmatively rather than left as an absence, because implementation teams migrating from a cumulative jurisdiction routinely build projection logic that France neither needs nor permits. What the employer does maintain cumulatively is the year-to-date net taxable amount and the year-to-date tax withheld, both of which are reported in the DSN and appear on the payslip and on the annual statement of amounts withheld — but neither feeds back into the current period's rate.
Two cumulative counters that genuinely do affect the calculation, and must be maintained:

| Counter | Effect |
|---|---|
| Exempt overtime pay against the EUR 7,500 annual cap | Once the cap is reached, further overtime enters the net taxable amount and so becomes subject to withholding |
| Exempt apprentice or intern pay against the annual minimum wage threshold | Once the threshold is reached, further pay enters the net taxable amount |


#### Are year-end tax adjustments required?

Not by the employer. There is no employer year-end reconciliation of income tax, no annual return of employee income tax to file, no equivalent of a year-end certificate that the employer must compute.
Three things do happen at the year end, and none is a calculation:

| Item | Who does it | Content |
|---|---|---|
| Annual statement of net taxable pay and tax withheld | Employer, automatically from the DSN | Reported through the DSN and used to pre-fill the employee's return; also shown as a year-to-date total on the December payslip |
| Annual return and assessment | Employee, in the spring | The withholding is credited; a balance is paid or refunded in the autumn |
| Recalculation of the personal rate | Tax administration, in September | The new rate is transmitted to the employer and applies from the September or October payroll |

Where the employer discovers that it withheld the wrong amount for a past period — a wrong rate applied, a wrong base — the correction is made through the DSN correction mechanism for the period concerned, not by adjusting the current month. The DSN carries the period so the tax administration can allocate the correction.

#### Are there minimum or higher tax requirements if employees fail to submit a tax ID or social security number?

No, and this is a point where French practice differs from most jurisdictions, so it is worth being explicit.

| Missing item | Consequence |
|---|---|
| Tax reference number | None. The employer never collects it. There is no penalty rate and no obligation on the employee to provide it |
| No withholding rate transmitted | The default grid applies. It is not a penalty rate: it is the statutory fallback and it is often close to, and can be lower than, the personal rate. There is no uplift |
| Social security number not supplied | A payroll consequence, not a tax one. The contract is declared under a temporary technical number; the DSN is accepted but generates recurring anomalies, and the employee's entitlements are not posted to their record until the number is supplied. No penalty rate applies |
| Employee elects confidentiality | The employee may ask the tax administration not to transmit the personal rate, in which case the default grid applies and the employee pays any shortfall directly to the administration. The employer is not told, does nothing differently, and may not question it |


#### What is the income tax and social security refund procedure?

The two follow entirely different routes.
Income tax over-withheld.

| Who discovers it | Route |
|---|---|
| Employer, in the same calendar year | Correct the withholding in a later payslip of the same year and file a corrective DSN for the period concerned. The correction flows through to the employee's net pay |
| Employer, after the year end | File a corrective DSN for the closed period. The employee obtains the correction through their annual assessment; the employer does not repay the employee directly for a closed year |
| Employee, because the rate was too high | Not a refund at all. The employee may ask the tax administration at any time to reduce the rate, or may wait for the annual assessment, which refunds the excess in the autumn. The employer plays no part |

Social security contributions over-paid.

| Situation | Route |
|---|---|
| Employer error discovered within the year | Regularise in the next DSN, which nets the correction against the current month's liability. This is the normal route and requires no application |
| Employer error relating to a closed year | File a corrective DSN for the period, or submit a repayment claim to the collecting body. Claims are time-barred three years after the end of the year in which the contributions were paid |
| Employee share over-deducted | The employer must repay the employee directly; recovering it from the collecting body does not discharge the obligation to the employee |
| Contribution relief not claimed | Claimable retrospectively within the same three-year limitation period, through corrective DSN filings |


#### Deliverable: Provide detailed worked examples for a standard resident employee, a non-resident employee, and an irregular payment.

Example 1 — standard resident employee, June 2026
Gross pay EUR 4,000.00; managerial grade; employer with 60 employees; personal withholding rate 9.90 % transmitted by the tax administration; employer health-cover contribution EUR 45.00 per month; employee health-cover share EUR 45.00.

| Line | Basis | Rate | Amount |
|---|---|---|---|
| Gross pay | — | — | 4,000.00 |
| Old-age, capped | 4,000.00 (below the EUR 4,005 ceiling) | 6.90 % | −276.00 |
| Old-age, uncapped | 4,000.00 | 0.40 % | −16.00 |
| Supplementary pension, band 1 | 4,000.00 | 3.15 % | −126.00 |
| General balance contribution, band 1 | 4,000.00 | 0.86 % | −34.40 |
| Executive employment association | 4,000.00 | 0.024 % | −0.96 |
| Employee health-cover share | — | — | −45.00 |
| General social contribution base | (4,000.00 × 98.25 %) + 45.00 employer share | — | 3,975.00 |
| General social contribution, deductible | 3,975.00 | 6.80 % | −270.30 |
| General social contribution, non-deductible | 3,975.00 | 2.40 % | −95.40 |
| Social debt repayment contribution | 3,975.00 | 0.50 % | −19.88 |
| Total employee contributions |  |  | −883.94 |
| Net payable before income tax |  |  | 3,116.06 |
| Net social amount | 4,000.00 + 45.00 − 883.94 |  | 3,161.06 |
| Net taxable amount | 3,116.06 + 95.40 + 19.88 + 45.00 |  | 3,276.34 |
| Income tax withheld | 3,276.34 × 9.90 % |  | −324.36 |
| Net paid | 3,116.06 − 324.36 |  | 2,791.70 |

The three figures EUR 3,116.06, EUR 3,161.06 and EUR 3,276.34 are all correct and all different. They are the net payable before tax, the net social amount and the net taxable amount respectively, and a payslip must show all three.
Example 2 — non-resident employee, June 2026
A resident of Germany works two days a week in France for a French establishment; the treaty gives France the taxing right over the French workdays. French-source net taxable pay for June is EUR 2,600.00.

| Step | Calculation | Result |
|---|---|---|
| 1. Net taxable amount | — | 2,600.00 |
| 2. Flat professional-expense deduction | 2,600.00 × 10 % | −260.00 |
| 3. Withholding base | — | 2,340.00 |
| 4. First band, 0 % | Up to 1,440.00 | 0.00 |
| 5. Second band, 12 % | (2,340.00 − 1,440.00) = 900.00 × 12 % | 108.00 |
| 6. Third band, 20 % | Base does not reach EUR 4,176 | 0.00 |
| 7. Withholding under Article 182 A |  | 108.00 |
| 8. Liberatory character | The whole EUR 108.00 falls in the 0 % and 12 % bands | Final; the income is excluded from a French return |
| 9. Net paid | 2,600.00 − 108.00 | 2,492.00 |

Had the June base reached EUR 5,000.00, the third band would have produced (5,000.00 − 4,176.00) × 20 % = EUR 164.80, that fraction would not have been liberatory, a French return would have been required, and the minimum assessment rate of Article 197 A would have applied on assessment.
Example 3 — irregular payment: a thirteenth month, December 2026
The employee of Example 1 receives their ordinary EUR 4,000.00 plus a thirteenth month of EUR 4,000.00, giving EUR 8,000.00 gross for December. The personal rate is unchanged at 9.90 %.

| Line | Basis | Rate | Amount |
|---|---|---|---|
| Gross pay | — | — | 8,000.00 |
| Old-age, capped | Capped at the ceiling, 4,005.00 | 6.90 % | −276.35 |
| Old-age, uncapped | 8,000.00 | 0.40 % | −32.00 |
| Supplementary pension, band 1 | 4,005.00 | 3.15 % | −126.16 |
| Supplementary pension, band 2 | 8,000.00 − 4,005.00 = 3,995.00 | 8.64 % | −345.17 |
| General balance contribution, band 1 | 4,005.00 | 0.86 % | −34.44 |
| General balance contribution, band 2 | 3,995.00 | 1.08 % | −43.15 |
| Technical balance contribution | 8,000.00 | 0.14 % | −11.20 |
| Executive employment association | 8,000.00 | 0.024 % | −1.92 |
| Employee health-cover share | — | — | −45.00 |
| General social contribution base | (8,000.00 × 98.25 %) + 45.00 | — | 7,905.00 |
| General social contribution, deductible | 7,905.00 | 6.80 % | −537.54 |
| General social contribution, non-deductible | 7,905.00 | 2.40 % | −189.72 |
| Social debt repayment contribution | 7,905.00 | 0.50 % | −39.53 |
| Total employee contributions |  |  | −1,682.18 |
| Net payable before income tax |  |  | 6,317.82 |
| Net taxable amount | 6,317.82 + 189.72 + 39.53 + 45.00 |  | 6,592.07 |
| Income tax withheld | 6,592.07 × 9.90 % |  | −652.62 |
| Net paid |  |  | 5,665.20 |

Three observations that generalise:
1. The withholding rate does not change. France has no bonus schedule and no re-banding; a doubled month is taxed at the same 9.90 %. Any correction is made by the tax administration the following year.
1. The supplementary pension bands do change, because gross pay has crossed the ceiling. Band 2 appears for the first time, and the technical balance contribution becomes due — it is payable only for employees whose pay exceeds one ceiling.
1. The capped old-age contribution is limited to EUR 4,005.00, not to EUR 8,000.00. This is exactly where the progressive ceiling reconciliation of Module 5.2 does its work: if the employee's pay was below the ceiling earlier in the year, unused ceiling entitlement is recovered here and the capped base rises above EUR 4,005.00 accordingly.
Legal basis: General Tax Code, Articles 79, 81 bis, 83, 182 A, 197 A, 204 A to 204 N; Social Security Code, Articles L243-6 (limitation period for repayment claims) and L242-1; LOI n° 2026-103 of 19 February 2026; Official Tax Bulletins BOI-BAREME-000037 and BOI-BAREME-000043.

## Module 7: Deductions, Exemptions & Benefits


### 7.1 Statutory Tax Reliefs, Deductions, and Exemptions


#### Deliverable: For each statutory tax relief, deduction, exemption, or other tax advantage, provide the name and definition, eligibility rules, statutory limits and amounts, calculation method, application point, and employee declaration requirements.

France distributes its reliefs across two levels, and the distinction decides whether the payroll engine has to do anything at all.
- Payroll-level reliefs change the net taxable amount, the contribution base or both, and must be configured.
- Assessment-level reliefs are applied by the tax administration to the annual return. They influence the withholding rate the employer later receives, but the employer never applies them. Building them into a payroll engine is a modelling error.
Each relief below is labelled accordingly.
---
1. Flat 10 % professional-expense deduction (déduction forfaitaire de 10 %)

| Aspect | Content |
|---|---|
| Definition | A standard deduction from employment income representing professional expenses |
| Level | Assessment. Applied by the tax administration to the annual return, never by the employer |
| Eligibility | Every employee, automatically, unless actual expenses are claimed instead |
| Limits, 2026 (2025 income) | Minimum EUR 509; maximum EUR 14,555 |
| Method | 10 % of net taxable employment income, floored and capped |
| Declaration | None; automatic |

2. Actual professional expenses (frais réels)

| Aspect | Content |
|---|---|
| Definition | Deduction of expenses actually incurred, in place of the 10 % flat deduction |
| Level | Assessment |
| Eligibility | Any employee whose evidenced expenses exceed the flat deduction. Typically long commutes, professional training, a home office |
| Limits | No overall cap, but each category has its own rules; commuting beyond 40 km each way needs justification |
| Method | Itemised, with the mileage scale published annually for vehicle use |
| Declaration | Detailed statement with the annual return; evidence kept for three years |

3. Sector-specific flat deduction (déduction forfaitaire spécifique)

| Aspect | Content |
|---|---|
| Definition | A percentage reduction of the social security contribution base for listed occupations — construction, journalism, commercial travellers, performing artists and others |
| Level | Payroll, on the contribution base only |
| Eligibility | Occupations listed in Article 5 of the annex to the Décret of 17 November 1936, where the applicable collective agreement or a company agreement provides for it and the employee has consented |
| Limits | Capped at EUR 7,600 per employee per year. The percentage is being progressively reduced by one point a year toward abolition; for journalists it stands at 24 % in 2026 |
| Method | Gross pay is first increased by any reimbursed professional expenses, then reduced by the percentage; the result is the contribution base |
| Application point | Before the contribution calculation. It does not reduce the income tax base |
| Declaration | Employee consent, renewed annually; a company or sector agreement authorising the deduction |

4. Income tax exemption on overtime and additional hours

| Aspect | Content |
|---|---|
| Definition | Exemption of overtime and additional-hours pay from income tax |
| Level | Payroll — the exempt amount is excluded from the net taxable amount |
| Eligibility | Every employee working overtime or, for a part-timer, additional hours; also days worked beyond an annual day-count arrangement |
| Limit | EUR 7,500 net per year per employee, cumulative across the calendar year and across employers |
| Method | Base rate and premium together are excluded from the net taxable amount until the cap is reached |
| Application point | In the build of the net taxable amount, before the withholding rate is applied |
| Declaration | None from the employee; the employer tracks the cumulative counter |

5. Employee old-age contribution relief on overtime

| Aspect | Content |
|---|---|
| Definition | A reduction of the employee's old-age contributions on overtime pay |
| Level | Payroll, contributions |
| Eligibility | The same hours as relief 4 |
| Limit | The employee's effective old-age rate, capped at 11.31 % |
| Method | Overtime pay × the lower of the effective rate and 11.31 %, deducted from the employee's contributions |
| Declaration | None |

6. Employer flat deduction on overtime hours

| Aspect | Content |
|---|---|
| Definition | A fixed reduction of employer contributions per overtime hour |
| Level | Payroll, employer contributions |
| Eligibility | All employers from 1 January 2026, the previous 250-employee exclusion having been removed by Article 21 of the Social Security Financing Act for 2026 |
| Limit | EUR 1.50 per hour below 20 employees; EUR 0.50 per hour at 20 and above; seven times the hourly amount per additional day under a day-count arrangement. Capped at the employer contributions actually due |
| Declaration | None |

7. Apprentice and intern income tax exemption

| Aspect | Content |
|---|---|
| Definition | Exemption of apprenticeship pay and internship gratuities from income tax |
| Level | Payroll — outside the net taxable amount |
| Limit | The annual minimum wage, per calendar year |
| Method | Excluded from the net taxable amount until the threshold is reached |
| Declaration | Apprenticeship or internship agreement |

8. Intern gratuity exemption from social security contributions

| Aspect | Content |
|---|---|
| Definition | Exemption of the statutory internship gratuity from contributions |
| Level | Payroll, contributions |
| Limit | 15 % of the hourly social security ceiling per hour of attendance — EUR 4.50 per hour for 2026, the hourly ceiling being EUR 30 |
| Method | Only the excess above the threshold is a contribution base |
| Declaration | Tripartite internship agreement |

9. Inbound-assignee regime (régime des impatriés)

| Aspect | Content |
|---|---|
| Definition | Exemption of an expatriation premium and of the portion of pay relating to work performed abroad |
| Level | Payroll for the premium — it is excluded from the net taxable amount; assessment for the passive-income element |
| Eligibility | Recruited abroad by a French company, or transferred within a group; must not have been tax-resident in France in the five calendar years before taking up the post; must become tax-resident in France |
| Limits | The premium is exempt for its real amount or, at the taxpayer's election, at a flat 30 % of total net remuneration. The combined exemption of the premium and the foreign-work portion is capped, on election, either at 50 % of total remuneration or at 20 % of taxable remuneration excluding the foreign-work portion |
| Duration | Until 31 December of the eighth calendar year following the year of taking up the post; a 2026 start therefore runs to 31 December 2034 |
| Application point | Excluded from the net taxable amount month by month |
| Declaration | Employment contract or assignment letter identifying the premium; evidence of the five-year non-residence condition |

10. Journalists' allowance for employment expenses

| Aspect | Content |
|---|---|
| Definition | A fixed deduction replacing the 10 % flat deduction for professional journalists |
| Level | Assessment |
| Limit | EUR 7,650, withdrawn where annual gross income exceeds EUR 93,510 |
| Declaration | Professional press card |

11. Meal vouchers (titres-restaurant)

| Aspect | Content |
|---|---|
| Definition | Exemption of the employer's share of a meal voucher |
| Level | Payroll — outside the contribution base, outside the social levies and outside income tax |
| Eligibility | Employees with no company canteen; one voucher per working day on which a meal falls within the working hours |
| Limit 2026 | EUR 7.32 per voucher, provided the employer's share is between 50 % and 60 % of face value. The corresponding face value range is therefore EUR 12.20 to EUR 14.64 — 7.32 ÷ 0.60 and 7.32 ÷ 0.50 respectively |
| Method | The employer share up to the limit is exempt; any excess is fully subject to contributions and to income tax |
| Declaration | Enrolment |

12. Compulsory 50 % reimbursement of public transport season tickets

| Aspect | Content |
|---|---|
| Definition | Statutory obligation to reimburse half the cost of the employee's home-to-work public transport or public bike-hire subscription |
| Level | Payroll — outside every base |
| Eligibility | Every employee, pro rata for part-timers below half time |
| Limit | 50 % of the subscription cost, on a second-class basis for the shortest route |
| Declaration | Proof of subscription |

13. Sustainable mobility allowance (forfait mobilités durables)

| Aspect | Content |
|---|---|
| Definition | Optional employer allowance for home-to-work travel by bicycle, car-sharing, shared mobility or public-service hire |
| Level | Payroll — outside every base within the limit |
| Limit 2026 | EUR 600 per year, raised to EUR 900 per year where combined with the compulsory 50 % transport reimbursement |
| Declaration | Sworn statement or evidence of the mode of travel, annually |

14. Value-sharing bonus (prime de partage de la valeur)
Covered in full at Module 4.5. Payroll-level; exempt from contributions up to EUR 3,000 or EUR 6,000; additionally exempt from the social levies and income tax under the enhanced regime for employers with fewer than 50 employees, for employees below three times the minimum wage, until 31 December 2026.
15. Incentive scheme and statutory profit-sharing (intéressement, participation)

| Aspect | Content |
|---|---|
| Definition | Collective schemes distributing a share of results or performance |
| Level | Payroll for the exemption from contributions; the income tax exemption depends on the employee's election |
| Eligibility | Profit-sharing is compulsory at 50 or more employees; incentive schemes are optional at any size. Employers with 11 to 49 employees meeting a sustained profitability test must operate at least one value-sharing device |
| Limits | Individual cap of 75 % of the annual social security ceiling, EUR 36,045 for 2026, for each scheme |
| Method | Exempt from social security contributions; subject to the general social contribution and the social debt repayment contribution with no allowance; exempt from income tax only if invested for the lock-in period, taxable if taken immediately |
| Application point | Outside gross pay; reported separately |
| Declaration | The employee elects between immediate payment and investment within the statutory window; failing an election, the amount is invested by default |

16. Employer contribution to a company savings plan (abondement)
Payroll-level. Exempt from contributions within a cap set by reference to the annual ceiling, subject to the general social contribution with no allowance, and exempt from income tax. Subject to the 20 % social lump-sum levy except for employers with fewer than 50 employees.
17. Employee deduction for supplementary cover contributions
Payroll-level, in the build of the net taxable amount. Limits are at General Tax Code Article 83: for death-and-disability cover, 5 % of the annual ceiling plus 2 % of remuneration, the total not exceeding 2 % of eight annual ceilings; for supplementary pension cover, 8 % of gross annual remuneration itself capped at eight annual ceilings.
---

#### Are salary sacrifice arrangements allowed?

No — not in the sense used in the United Kingdom or Australia. France has no general mechanism by which an employee may give up contractual pay in exchange for an exempt benefit and thereby reduce the contribution and tax base.
The obstacle is the non-substitution principle, which appears in every exemption text: an exempt payment loses its exemption if it substitutes for any element of remuneration paid by the employer, or which becomes compulsory under a rule, unless a period of twelve months has elapsed between the withdrawal of the pay element and the first exempt payment. It applies expressly to the value-sharing bonus, to incentive-scheme and profit-sharing amounts, to the sustainable mobility allowance and to employer savings-plan contributions.
Three arrangements are sometimes described as salary sacrifice and are not:

| Arrangement | What it actually is |
|---|---|
| Converting rest days from a working-time reduction agreement into pay | A monetisation of rest, which increases pay. The converted days are ordinary taxable and contributable pay, with the overtime social reliefs applying to hours beyond the statutory duration |
| Time savings account (compte épargne-temps) | Deferral of pay and rest, not conversion into an exempt benefit. Sums drawn from the account are ordinary pay when drawn, save where transferred into a retirement savings plan within the statutory limits |
| Investing a profit-sharing entitlement rather than taking it in cash | A statutory election within an existing exempt scheme, not a reduction of contractual pay |

The practical answer to a client asking for salary sacrifice is therefore: the structure must be built as a genuine employer-funded benefit within one of the statutory exemptions, never as a reduction of contractual pay in exchange for a benefit.

#### List common types of post-tax deductions and any specific ordering rules or limitations.


| Deduction | Nature | Limit |
|---|---|---|
| Wage garnishment for an ordinary debt | Statutory, on an enforcement officer's notice | The seizable fraction scale in section 7.3 |
| Direct payment of a maintenance order (paiement direct) | Statutory, priority over all other creditors | Payable from the whole salary above the absolutely protected amount, outside the seizable fraction scale |
| Tax levy notice (avis à tiers détenteur) | Statutory, on the tax administration's notice | The seizable fraction scale |
| Employee share of meal vouchers | Contractual | 40 % to 50 % of face value |
| Repayment of a salary advance (avance) | Contractual | One tenth of pay per period, under Labour Code Article L3251-3 |
| Recovery of a payment on account already made in the month (acompte) | Not a deduction at all | Netted against the same month's pay in full, because it is a payment of that month's salary |
| Recovery of an overpayment | Contractual | The seizable fraction scale |
| Union dues | Voluntary, on the employee's written mandate | None |
| Employee share of supplementary cover | Contractual, but taken pre-tax | Per the scheme |

Ordering rule. Where several claims compete, the order is:
1. the absolutely protected amount is reserved to the employee — EUR 651.69 per month in 2026;
1. maintenance orders paid by direct payment, in priority to everything else;
1. tax levies;
1. ordinary garnishments, within the seizable fraction, shared between creditors by the distributing enforcement officer;
1. the employer's own claims, limited to one tenth for advances.
The employer that pays a creditor out of order, or that exceeds the seizable fraction, becomes personally liable.

#### List any income types that are statutorily exempt from income tax.


| Income type | Basis | Limit |
|---|---|---|
| Reimbursement of professional expenses within the statutory limits | General Tax Code Article 81, 1° | The limits of the Arrêté of 20 December 2002 |
| Employer share of meal vouchers | Article 81, 19° | EUR 7.32 per voucher |
| 50 % reimbursement of public transport season tickets | Article 81, 19° ter | 50 % of the subscription |
| Sustainable mobility allowance | Article 81, 19° ter b | EUR 600, or EUR 900 combined |
| Overtime and additional-hours pay | Article 81 quater | EUR 7,500 net per year |
| Apprenticeship pay and internship gratuities | Article 81 bis | The annual minimum wage |
| Statutory and collectively agreed severance, within limits | Article 80 duodecies | See Module 9 |
| Severance paid under a collective redundancy plan | Article 80 duodecies, 1° | Fully exempt, without limit |
| Damages for unfair dismissal awarded by a court | Article 80 duodecies, 1° | Fully exempt |
| Incentive-scheme and profit-sharing amounts, if invested | Articles 81, 18° bis and 18° ter | EUR 36,045 per scheme |
| Employer contributions to a company savings plan | Article 81, 18° | Within the statutory caps |
| Expatriation premium under the inbound-assignee regime | Article 155 B | Real amount or 30 % flat, subject to the overall cap |
| Value-sharing bonus, enhanced regime only | Act of 16 August 2022, Article 1 | EUR 3,000 or EUR 6,000, until 31 December 2026 |
| Employer contributions to supplementary pension cover, within limits | Article 83, 2° | 8 % of pay capped at eight annual ceilings |
| Works council social and cultural benefits within the tolerances | Administrative tolerance | Per event |

Two items commonly assumed to be exempt and which are not: the employer's contribution to the compulsory health cover, which is added to the net taxable amount; and daily social security benefits for ordinary sickness, which are taxable in full.
Legal basis: General Tax Code, Articles 80 duodecies, 81, 81 bis, 81 quater, 83, 155 B; Social Security Code, Articles L136-1-1, L241-13, L241-17, L241-18, L241-18-1, L242-1, D242-1; Labour Code, Articles L3251-1 to L3251-3, L3261-2, L3261-3-1, L3312-1 and following, L3322-1 and following; Arrêté of 20 December 2002; Décret of 17 November 1936, annex Article 5; Act n° 2022-1158 of 16 August 2022; Act n° 2025-1403 of 30 December 2025.

### 7.2 Benefits in Kind (BIK)


#### Are non-cash benefits taxed via the standard payroll system, or a separate employer-paid regime?

Through the standard payroll system. France has no separate fringe benefits tax and no employer-paid benefits regime of the Australian or New Zealand kind. A benefit in kind is remuneration: it is added to gross pay at its statutory value, bears employee and employer social contributions, bears the general social contribution and the social debt repayment contribution, and enters the employee's net taxable amount.
Because the benefit is not paid in cash, the payslip adds its value to gross for the calculation and then deducts the same value after the contributions, so that net pay is reduced by the employee's contributions on the benefit and by nothing else.
There is one adjacent employer-only levy that is sometimes mistaken for a fringe benefits tax: the company vehicle tax (taxes annuelles sur l'affectation des véhicules à des fins économiques). It is a corporate tax on the fleet, assessed on emissions and seniority, filed with the tax authorities and not through payroll, and it is entirely separate from the employee's benefit in kind. It is out of payroll scope but must be flagged to the client's finance function.

#### What is the definition of fringe benefits and how is the taxable amount evaluated?

A benefit in kind is the provision by the employer of a good or service, either free of charge or for a payment lower than its real value, for the employee's private use.
Valuation follows one of two methods, and the choice belongs to the employer, exercised per benefit category and per calendar year:

| Method | When available | Effect |
|---|---|---|
| Statutory flat value (évaluation forfaitaire) | For meals, accommodation, vehicles and communication tools | Simple, predictable, and the market default |
| Real cost (dépenses réelles) | For any benefit; compulsory for company officers treated as employees, other than for the vehicle and communication tools | Requires evidence of the actual cost and of the private-use share |

Meals. EUR 5.50 per meal for 2026; EUR 11.00 for two meals a day. Where the employee contributes at least half the flat value — EUR 2.75 — no benefit is assessed.
Accommodation. An eight-band flat scale by the employee's gross monthly pay, expressed in multiples of the monthly social security ceiling. For 2026 the scale runs from EUR 79.70 per month for one room where gross monthly pay is below EUR 2,002.50 — half the monthly ceiling — up to EUR 225.60 per room where gross monthly pay reaches EUR 6,007.50, one and a half times the monthly ceiling. The bracket boundaries are pure multiples of the ceiling, which is how the scale revalues automatically each year. The flat value includes water, gas, electricity, heating and a garage.
Company vehicle. The rules changed materially on 1 February 2025 and the treatment depends on when the vehicle was made available, not on the year of the payslip. Both sets of rules are live in 2026.

| Vehicle made available | Purchased by the employer | Leased or long-term hire |
|---|---|---|
| Before 1 February 2025 | 9 % of the inclusive purchase price if less than 5 years old, 6 % if older; 12 % and 9 % respectively where the employer pays for private fuel | 30 % of the total annual cost, capped at the value of the purchase rules; 40 % where the employer pays for private fuel |
| On or after 1 February 2025 | 15 % of the inclusive purchase price if less than 5 years old, 10 % if older; 20 % and 15 % respectively where the employer pays for private fuel | 50 % of the total annual cost; 67 % where the employer pays for private fuel |

The new percentages represent an increase of roughly two thirds on values that had not been revised since 2002, and the effect on a payslip is significant. A vehicle transferred to a different employee, or renewed, is a new availability and falls under the new rules.
Fully electric vehicles. Where the flat method is used, the benefit is reduced by a 70 % abatement, capped at EUR 4,641.60 per year for 2026 (EUR 4,582 for 2025). Only wholly electric vehicles qualify; hybrids do not. Electricity supplied by the employer for charging is disregarded, and a charging point made available at the employee's home is valued at nil within the conditions set by the official doctrine.
Communication tools. Where a telephone, computer or internet subscription made available for professional use is also used privately, the benefit is 10 % of the inclusive purchase price, or 10 % of the annual subscription cost.

#### If a separate FBT regime exists, describe it in detail.

Not applicable — France has no fringe benefits tax. Benefits in kind are taxed as remuneration in the hands of the employee, and the employer bears only the ordinary employer contributions on their value.

#### What is the calculation logic for fringe benefit tax?

Not applicable for the reason above. The calculation logic for a benefit in kind is:
1. Determine the benefit value from the statutory scale, or the real cost
2. Deduct any amount the employee actually pays toward the benefit
3. Add the net value to gross pay
4. Calculate all employee and employer contributions on the increased gross
5. Deduct the same net value after the contributions, so that net pay falls
only by the employee's contributions on the benefit
6. The value remains in the net taxable amount and is therefore withheld on
Worked example — company vehicle, 2026. An employee is given a petrol vehicle purchased new by the employer in March 2026 for EUR 30,000 inclusive of tax; the employer pays for private fuel. Gross salary EUR 3,000.00 per month.

| Step | Calculation | Result |
|---|---|---|
| 1. Availability date | March 2026, so the post-1 February 2025 rules apply | — |
| 2. Flat percentage | Purchased, under 5 years old, employer pays private fuel | 20 % |
| 3. Annual benefit | 30,000 × 20 % | EUR 6,000.00 |
| 4. Monthly benefit | 6,000 ÷ 12 | EUR 500.00 |
| 5. Gross for the calculation | 3,000.00 + 500.00 | EUR 3,500.00 |
| 6. Contributions | Calculated on EUR 3,500.00 | — |
| 7. After contributions | Deduct EUR 500.00 | Net reduced only by the contributions on the benefit |

Had the same vehicle been fully electric, step 3 would give 6,000 × 30 % = EUR 1,800.00, the 70 % abatement being EUR 4,200.00 and therefore below the EUR 4,641.60 cap.

#### Are benefits-in-kind also subject to withholding tax?

Yes. The benefit's value is part of the net taxable amount, so the withholding rate applies to it exactly as to cash pay. Because the benefit itself is not paid in cash, the tax on it is deducted from the cash element of net pay — which means an employee with a large benefit and a small cash salary can see a disproportionate reduction in net pay. This is the correct result and a frequent employee query.

#### Which benefits-in-kind must be processed via payroll, and which require declarations?


| Benefit | Route |
|---|---|
| Meals, accommodation, company vehicle, communication tools | Payroll, monthly, at the statutory or real value |
| Employer share of the compulsory health cover | Payroll: exempt from contributions within limits, subject to the social levies, added to the net taxable amount |
| Employer share of death-and-disability cover | Payroll: exempt from contributions within limits, then the 8 % social lump-sum levy at 11 or more employees, and added to the net taxable amount |
| Works council gifts, vouchers and cultural benefits within the tolerances | Not through payroll; managed by the works council. Above the tolerances they become payroll items |
| Free share awards and share options | Not ordinary payroll. The employer declares the award in the DSN and pays the specific 30 % employer contribution; the employee's acquisition gain is taxed on disposal through the annual return, not withheld at source |
| Loans at below-market rates | Payroll, at the interest saved, where the advantage is material |
| Company vehicle tax on the fleet | Corporate tax return, not payroll |

Legal basis: Social Security Code, Article L242-1; Arrêté of 10 December 2002 as amended by the Arrêté of 25 February 2025 (benefits in kind); General Tax Code, Articles 82 and 82 bis; Official social security doctrine on benefits in kind, 2026 edition.

### 7.3 Garnishments and Court Orders


#### What are the rules for processing statutory deductions like child support, court-ordered fines, or tax levies?

The wage garnishment procedure was fundamentally reformed with effect from 1 July 2025. Under Act n° 2023-1059 of 20 November 2023 and the implementing Décret of 12 February 2025, the procedure ceased to be judicial and is now conducted by court enforcement officers (commissaires de justice).

| Aspect | Position since 1 July 2025 |
|---|---|
| Who initiates | The creditor's enforcement officer, without a court hearing |
| What the employer receives | A record of attachment (procès-verbal de saisie) issued by the enforcement officer, accompanied by a certificate confirming that no challenge is outstanding |
| What the employer must do | Confirm the employment relationship and pay the seizable fraction each month to the distributing enforcement officer (commissaire de justice répartiteur), who allocates it among the creditors |
| Timing | The employer must respond to the attachment within fifteen days and pay monthly thereafter |
| If the employee leaves | The employer must inform the enforcement officer, giving the new employer's details if known |
| Sanction | An employer that fails to respond, or that fails to pay over the seizable fraction, may be declared personally liable for the debt |

Three distinct instruments must be distinguished, because they do not follow the same rules:

| Instrument | Route | Limit |
|---|---|---|
| Ordinary wage attachment | Enforcement officer's record of attachment | The seizable fraction scale |
| Direct payment of a maintenance order (paiement direct) | Notice served on the employer by the creditor's enforcement officer | Payable from the whole salary above the absolutely protected amount; it is not confined to the seizable fraction, and it ranks ahead of every other creditor |
| Tax levy notice (avis à tiers détenteur, or saisie administrative à tiers détenteur) | Notice from the public finances directorate | The seizable fraction scale |


#### Is there a statutory priority order if an employee has multiple garnishments?

Yes, and it is not negotiable:
1. The absolutely protected amount is reserved to the employee before anything is paid to any creditor. For 2026 this is EUR 651.69 per month, the amount of the active-solidarity income for a single person with no dependants.
1. Maintenance orders paid by direct payment, in priority to all other creditors and outside the seizable fraction scale.
1. Tax levies and other public-law claims.
1. Ordinary creditors, sharing the seizable fraction; where there are several, the employer pays the single seizable fraction to the distributing enforcement officer, who allocates it. The employer never apportions between creditors itself.
1. The employer's own claims — recovery of advances, limited to one tenth of pay.

#### Are there protected earnings limits?

Yes, at two levels.
The seizable fraction scale. The scale is revalued annually and was indexed by 0.9 % for 2026 by Décret n° 2025-1299 of 24 December 2025. It applies to net pay after social contributions and after the withheld income tax.

| Annual net pay band | Monthly equivalent | Seizable fraction |
|---|---|---|
| Up to EUR 4,480 | Up to EUR 373.33 | 1/20 |
| EUR 4,480.01 to 8,730 | EUR 373.34 to 727.50 | 1/10 |
| EUR 8,730.01 to 13,000 | EUR 727.51 to 1,083.33 | 1/5 |
| EUR 13,000.01 to 17,230 | EUR 1,083.34 to 1,435.83 | 1/4 |
| EUR 17,230.01 to 21,470 | EUR 1,435.84 to 1,789.17 | 1/3 |
| EUR 21,470.01 to 25,810 | EUR 1,789.18 to 2,150.83 | 2/3 |
| Above EUR 25,810 | Above EUR 2,150.83 | Entirely seizable |

Consistency check. Each monthly threshold is exactly one twelfth of its annual band limit: 727.50 × 12 = 8,730; 1,083.33 × 12 = 12,999.96, published as 13,000; 1,435.83 × 12 = 17,229.96, published as 17,230; 2,150.83 × 12 = 25,809.96, published as 25,810. Where a secondary source shows the second band beginning at EUR 4,440.01 rather than EUR 4,480.01, the arithmetic identifies it as a transposition error: 373.33 × 12 = 4,479.96, so the first band ends at EUR 4,480.
The bands are cumulative, not selective. The scale slices the pay: the first EUR 373.33 of monthly pay yields one twentieth, the next slice one tenth, and so on. Reading a single fraction from the band containing total pay is wrong and materially over-deducts.
Increase for dependants. Each band limit is increased by EUR 1,740 per year, EUR 145 per month, for each dependant — the spouse or partner, and each child or ascendant living with and supported by the employee. The employee must supply evidence of dependants; the employer applies the increase on that evidence.
The absolutely protected amount. Whatever the scale produces, the employee must retain at least EUR 651.69 per month in 2026. This floor is not increased for dependants and yields only to a maintenance order paid by direct payment.
Worked example — garnishment, 2026. An employee has monthly net pay after contributions and withheld tax of EUR 1,900.00 and two dependent children.

| Step | Calculation | Result |
|---|---|---|
| 1. Increase each band by 2 × EUR 145 | Bands rise by EUR 290 | — |
| 2. Band 1, 1/20 | Up to 373.33 + 290 = 663.33 → 663.33 × 1/20 | EUR 33.17 |
| 3. Band 2, 1/10 | (727.50 + 290) − 663.33 = 354.17 → × 1/10 | EUR 35.42 |
| 4. Band 3, 1/5 | (1,083.33 + 290) − 1,017.50 = 355.83 → × 1/5 | EUR 71.17 |
| 5. Band 4, 1/4 | (1,435.83 + 290) − 1,373.33 = 352.50 → × 1/4 | EUR 88.13 |
| 6. Band 5, 1/3 | 1,900.00 − 1,725.83 = 174.17 → × 1/3 | EUR 58.06 |
| 7. Seizable fraction | Sum of steps 2 to 6 | EUR 285.95 |
| 8. Amount left to the employee | 1,900.00 − 285.95 = 1,614.05, above EUR 651.69 | No further restriction |

Legal basis: Labour Code, Articles L3252-1 to L3252-13, R3252-2 to R3252-5; Code of Civil Enforcement Procedures, Articles L212-1 and following; Act n° 2023-1059 of 20 November 2023; Décret of 12 February 2025 (transfer of the wage attachment procedure to court enforcement officers); Décret n° 2025-1299 of 24 December 2025 (2026 scale); Social Action and Families Code, Article L262-2 (active-solidarity income).

## Module 8: Statutory Leave Management


### 8.1 Leave Entitlements


#### For each type of statutory leave, what are the eligibility criteria and accrual methodology?


| Leave | Eligibility | Accrual or duration | Who pays |
|---|---|---|---|
| Paid annual leave (congés payés) | Every employee from the first day of work; no length-of-service condition since 2008 | 2.5 working days (jours ouvrables) per month of actual work, capped at 30 working days, that is five weeks, per reference year | Employer, or the sector leave fund in construction and entertainment |
| Working-time reduction days (jours de RTT) | Only where a collective or company agreement organises working time above 35 hours with compensating days | Per the agreement; commonly 10 to 12 days a year | Employer |
| Public holidays | Every employee; pay maintained on ordinary holidays after 3 months' service, and unconditionally on 1 May | 11 days nationally, 13 in Alsace-Moselle | Employer |
| Maternity leave | Every pregnant employee, no service condition | 16 weeks for a first or second child — 6 before and 10 after the birth; 26 weeks from the third child; 34 weeks for twins; 46 weeks for triplets or more. The 8 weeks around the birth, of which 6 after, are compulsory | Social security daily benefit, usually topped up by the employer under the collective agreement |
| Birth leave (congé de naissance) | The employee whose child is born, and the spouse or partner of the mother | 3 days, taken at the birth | Employer, at full pay |
| Paternity and child-welcome leave | Father, and the mother's spouse or partner, whatever the length of service | 25 calendar days, 32 for a multiple birth, in addition to the 3 days of birth leave. The first 4 days immediately following the birth leave are compulsory and the employer may not allow work | Social security daily benefit |
| Supplementary birth leave (congé supplémentaire de naissance) | New from 1 July 2026. Each parent of a child born or adopted from 1 January 2026 | Up to 2 months per parent, taken as one month, two months, or two separate periods of one month, after the maternity, paternity or adoption leave | Social security daily benefit at 70 % of net pay for the first month and 60 % for the second |
| Adoption leave | Employee adopting a child | 16 weeks, extended for multiple adoptions or from the third child, and increased where shared between the parents | Social security daily benefit |
| Parental education leave (congé parental d'éducation) | 1 year's service at the birth or adoption | Up to the child's third birthday, taken as full leave or as part-time work | Unpaid by the employer; a family allowance may be payable |
| Sick leave, non-occupational | Statutory benefit from the first stoppage; employer top-up requires 1 year's service | Duration set by the doctor | Social security daily benefit after a 3-day waiting period, plus the employer top-up |
| Work accident and occupational disease leave | Every employee, no service condition | Duration set by the doctor | Social security daily benefit from the first day, plus the employer top-up with no waiting period |
| Family event leave | Every employee, no service condition | See the table below | Employer, at full pay |
| Bereavement leave for a child (congé de deuil) | Every employee on the death of a child under 25, or of a dependent person under 25 | 8 days, in addition to the family-event leave, which may be split and taken within one year of the death | Shared between the employer and social security |
| Carer's leave (congé de proche aidant) | Every employee caring for a dependent relative | Up to 3 months, renewable to one year over a career | Unpaid by the employer; a daily carer's allowance is payable |
| Parental presence leave (congé de présence parentale) | Parent of a seriously ill, injured or disabled child | 310 working days over a maximum of 3 years | Unpaid by the employer; a daily parental-presence allowance is payable |
| Reserve-forces leave | Employee who is a member of the operational reserve | 5 working days a year as of right, more by agreement | Unpaid by the employer unless a collective agreement provides otherwise |

Family event leave, minimum statutory durations (Labour Code Article L3142-4, as amended, most recently by Act n° 2026-492 of 12 June 2026). Collective agreements frequently improve on these and the more favourable provision applies.

| Event | Minimum days |
|---|---|
| Employee's own marriage or civil partnership | 4 |
| Marriage of a child | 1 |
| Each birth or adoption placement | 3 |
| Death of a child | 12 working days; 14 where the child was under 25, where the child had themselves a child, or on the death of a dependent person under 25 |
| Death of the spouse, civil partner, cohabiting partner, parent, parent-in-law, sibling | 3 |
| Announcement in a child of a disability, a cancer, or a chronic condition requiring prolonged treatment | 5 |

Act n° 2026-492 of 12 June 2026 also created new authorised absences for employees undergoing medically assisted reproduction treatment and for employees attending the compulsory interviews in an adoption approval procedure. These are authorised absences with pay maintained, on the same model as family event leave.
Paid annual leave — the accrual mechanics that matter for configuration:

| Point | Rule |
|---|---|
| Unit of account | The Labour Code counts in working days (jours ouvrables): Monday to Saturday inclusive, six days a week, 30 days a year. Many agreements count in worked days (jours ouvrés): Monday to Friday, five days a week, 25 days a year. The two must never be mixed in one calculation, and the worked-days count must always be at least as favourable |
| Reference period | 1 June to 31 May by default; a company agreement, or the existence of an annualised working-time arrangement, may set the calendar year instead |
| Rounding | Where the total is not a whole number, it is rounded up to the next whole day |
| Sick leave | Since the Act of 22 April 2024 transposing European requirements, non-occupational sick leave accrues 2 working days per month, capped at 24 working days per reference period; work accident and occupational disease leave accrues the ordinary 2.5 working days per month up to 30. The Court of Cassation held on 21 January 2026 that the 24-day cap is assessed reference period by reference period, without regard to leave carried over from an earlier period |
| Carry-over after sickness | Leave that could not be taken because of sickness may be carried for 15 months. Critically, the 15-month period runs only from the day the employer informs the employee of their entitlement on return to work, and the employer bears the burden of proving it gave that information. Absent proof, the leave never lapses |
| Splitting | At least 12 consecutive working days must be taken between 1 May and 31 October; splitting the main leave outside that window can generate additional splitting days |


#### How are unpaid or partially paid leaves handled?

An unpaid absence is processed as a deduction from the smoothed monthly salary, calculated by the same method used consistently for that employer — real hours being the method preferred by the courts.

| Effect of an unpaid absence | Treatment |
|---|---|
| Gross pay | Reduced by the value of the absence |
| Social security ceiling | Prorated down for the unpaid period; the ceiling follows the paid period, not the calendar |
| Contributions | Calculated on the reduced gross and the reduced ceiling |
| Net taxable amount | Falls with gross; the withholding rate is unchanged |
| Paid leave accrual | Suspended, unless the absence is one of the periods treated as time worked |
| Length of service | Generally continues to run for seniority purposes, but parental leave counts only for half its duration |
| Pension entitlement | No contributions, therefore no quarters validated for the period |
| Health cover | The compulsory health cover normally continues, and the collective agreement determines who funds the contribution during the absence |

Partially paid leave — principally sickness where the employer tops up the social security benefit — is processed as a combination of three lines: the deduction of the absence from the smoothed salary, the daily social security benefit where the employer is subrogated, and the employer top-up.

#### Which wage types are affected by unpaid/partially paid leave?


| Wage type | Effect |
|---|---|
| Base salary | Reduced by the absence |
| Seniority bonus | Usually reduced in the same proportion, unless the agreement provides otherwise |
| Thirteenth month | Prorated for the absence over its reference period, unless the agreement treats the absence as time present |
| Overtime | Not applicable during absence |
| Benefits in kind | Continue where the benefit remains available — a company vehicle retained during sick leave continues to generate a benefit |
| Meal vouchers | Not issued for days not worked |
| Transport reimbursement | Suspended for a full month of absence; maintained for a partial month |
| Social security ceiling | Prorated |
| Employer health-cover contribution | Continues, and remains in the net taxable amount |
| Paid leave accrual | Suspended, except for the assimilated periods |


#### Are there any mandatory national military service leaves?

Compulsory military service was suspended in France for those born after 31 December 1978, so there is no conscription leave. Three residual obligations exist and only the first two touch payroll.

| Obligation | Content | Pay |
|---|---|---|
| Defence and citizenship day (journée défense et citoyenneté) | One day, for citizens aged 16 to 25 | The employee is entitled to one day's authorised absence, which does not reduce pay and is not deducted from paid leave |
| Operational reserve leave | Members of the operational reserve are entitled to 5 working days a year as of right, and to longer periods with the employer's agreement or under a collective agreement | Unpaid by the employer by default; the reserve pays the reservist. Many collective agreements and a reserve-support agreement with the employer improve on this |
| Civil defence and civil-security reserve | Similar, on the same model | Same |


#### Are any other kinds of leave paid by government authorities?

Yes. The distinction between employer-paid and authority-paid leave is one of the primary configuration decisions in French payroll, because authority-paid leave generates a benefit that may or may not transit the payslip.

| Leave | Paying authority | Transits the payslip |
|---|---|---|
| Sick leave, maternity, paternity, adoption, work accident, occupational disease | Sickness insurance fund (CPAM) | Only where the employer is subrogated — that is, where it maintains pay and receives the benefit directly. Otherwise the fund pays the employee and the payslip shows only the deduction and the top-up |
| Supplementary birth leave, from 1 July 2026 | Sickness insurance fund | Same subrogation logic |
| Bereavement leave for a child | Employer for part, sickness insurance fund for the balance | Partly |
| Parental education leave | Family allowance fund, through a shared child-rearing benefit | No |
| Carer's leave | Family allowance fund, through a daily carer's allowance | No |
| Parental presence leave | Family allowance fund, through a daily parental-presence allowance | No |
| Paid annual leave in construction, public works and entertainment | Sector paid-leave fund | No — the fund pays the employee directly. The employer pays a contribution to the fund and shows no holiday pay on the payslip |
| Partial activity (activité partielle) | The State and the unemployment insurance body | Yes — the employer pays the allowance and is reimbursed |

Subrogation is worth stating plainly because it changes the payslip structure. Where the employer is subrogated it maintains full pay, shows the daily benefit as an offsetting line, and receives the benefit from the fund. Where it is not, the employee receives the benefit directly and the payslip shows a reduced salary. Both are lawful; the collective agreement usually decides, and the choice must be recorded per client and per absence type.

#### What are the payout rules for statutory leaves?

Paid annual leave. The employee must receive the higher of two amounts, compared leave by leave — this is a statutory rule, not an employer option, and it is the single most commonly mis-implemented rule in French payroll.

| Method | Calculation |
|---|---|
| One-tenth rule (règle du dixième) | One tenth of the total gross pay received during the reference period, divided across the days of leave acquired |
| Salary maintenance rule (maintien de salaire) | The pay the employee would have received had they worked during the leave |

The comparison is made at the point the leave is taken, and it is the more favourable result that is paid. The one-tenth rule normally wins where pay has fallen, or where the employee received substantial variable pay in the reference period; the maintenance rule wins where pay has risen.
Elements included in the one-tenth base: base salary, overtime, commission, bonuses that are consideration for work, and benefits in kind. Excluded: reimbursed expenses, bonuses covering the whole year including the leave period such as a thirteenth month, and profit-sharing.
Sickness. The social security daily benefit is 50 % of the daily base wage, itself the average gross of the last three months divided by 91.25, and the base wage used is capped at 1.4 times the minimum wage, a cap reduced from 1.8 by Décret n° 2025-160 of 20 February 2025. Because the minimum wage rose on 1 June 2026 the cap moved during the year:

| Period | Maximum gross daily sickness benefit |
|---|---|
| 1 February 2026 to 30 June 2026 | EUR 41.95 |
| From 1 July 2026 | EUR 42.97 |

A three-day waiting period applies before the benefit begins, and none applies for a work accident or occupational disease.
The maximum daily benefit for maternity, paternity, adoption and bereavement leave is EUR 104.02 for 2026. These benefits use a different and much higher base, because they are calculated on the capped monthly wage rather than on the 1.4 minimum-wage cap.
Employer top-up on sickness (Labour Code Article L1226-1 and Article D1226-1). Available after one year's service, after a seven-day waiting period for non-occupational sickness and with no waiting period for a work accident, at:
- 90 % of the gross pay the employee would have received, for the first 30 days;
- 66.66 % for the following 30 days;
- each of the two periods increased by 10 days per five years of service beyond the first, up to 90 days at each rate.
Collective agreements very frequently improve on this — full pay from day one is common for managerial grades — and the more favourable rule applies.
Work accident and occupational disease. The daily benefit is 60 % of the daily wage for the first 28 days and 80 % from the 29th, with no waiting day, and the base is not subject to the 1.4 minimum-wage cap that applies to ordinary sickness.

#### How are unused paid leaves treated upon termination?

Accrued but untaken paid leave must be paid out as a compensatory leave indemnity (indemnité compensatrice de congés payés) in the final settlement, whatever the reason for the termination — including dismissal for serious misconduct, since a 2016 change in the law.

| Rule | Content |
|---|---|
| Amount | Calculated by the same comparison as leave pay: the higher of the one-tenth rule and the salary maintenance rule, applied to the untaken days |
| Scope | Covers both the leave accrued in the current reference period and any balance carried from an earlier period |
| Social treatment | Ordinary pay. Fully subject to social security contributions, to the general social contribution and the social debt repayment contribution, and to income tax. It is not a severance payment and carries none of the severance exemptions |
| Working-time reduction days | Untaken days are paid out where the agreement so provides; there is no statutory obligation |
| Time savings account | The balance is paid out or transferred, per the agreement |
| Construction and entertainment sectors | No indemnity is paid by the employer; the employee claims from the sector leave fund, and the employer issues a leave certificate |

An employee dismissed for serious misconduct who is not required to work their notice still accrues leave over the notice period where the notice is paid, and the accrual must be included in the payout.

#### Provide the calculation logic for each leave type where applicable.

Paid leave accrual
Days accrued = 2.5 working days × months of actual work in the reference period
capped at 30 working days
Months of actual work include: work performed, paid leave taken, maternity,
paternity, adoption and supplementary birth leave, work accident and
occupational disease leave, and non-occupational sick leave (at 2 days per
month, capped at 24 days per reference period)
Leave pay — the comparison
A = one-tenth rule
= ( total gross pay of the reference period × 1/10 )
× ( days of leave taken ÷ days of leave acquired )
B = salary maintenance rule
= ( monthly salary ÷ working days in the month ) × days of leave taken
Leave pay = max(A, B)
Worked example. An employee acquired 30 working days over a reference period in which gross pay totalled EUR 39,600.00. Their current monthly salary is EUR 3,400.00 and they take 12 working days of leave in a month containing 26 working days.

| Step | Calculation | Result |
|---|---|---|
| One-tenth rule, total | 39,600.00 × 1/10 | EUR 3,960.00 |
| One-tenth rule, for 12 of 30 days | 3,960.00 × 12 ÷ 30 | EUR 1,584.00 |
| Maintenance rule | 3,400.00 × 12 ÷ 26 | EUR 1,569.23 |
| Leave pay due | The higher of the two | EUR 1,584.00 |

The EUR 14.77 difference is small here, but the comparison is mandatory and must be run every time; where an employee had significant overtime or commission in the reference period the one-tenth rule can exceed the maintenance rule substantially.
Sickness — the combined payslip
1. Deduct the absence from the smoothed salary
( monthly salary ÷ working days in the month ) × days absent
2. Add the daily social security benefit, where the employer is subrogated
min( 50 % × (gross of the last 3 months ÷ 91.25) , the daily cap )
× the days indemnified, after the 3-day waiting period
3. Add the employer top-up
( 90 % or 66.66 % × the pay the employee would have received )
less the daily benefit already counted, after the 7-day waiting period
and subject to one year's service
The daily social security benefit is exempt from social security contributions but subject to the general social contribution at the reduced 6.20 % rate and to the social debt repayment contribution, and it is fully taxable. The employer top-up is ordinary pay in every respect.

#### How does extended unpaid leave impact social security contributions, tax status, and accrual?


| Dimension | Effect of extended unpaid leave |
|---|---|
| Social security contributions | None are due, because there is no pay. The employment relationship is suspended, not ended |
| Social security ceiling | Prorated down for the unpaid period |
| Entitlement to health cover | Rights are maintained for a statutory continuation period, then the individual moves to residence-based universal cover |
| Pension quarters | No quarters validated, because no contributions are paid. Parental education leave is partly assimilated for pension purposes |
| Compulsory health cover | The scheme's founding document decides whether cover continues and who funds it. Where cover is suspended, the employer must inform the employee |
| Income tax | No pay, therefore no net taxable amount and no withholding. The employee remains within the withholding system and the rate persists for later periods |
| Paid leave accrual | Suspended, except for the assimilated periods listed above |
| Length of service | Continues for parental education leave, but counted at half its duration; continues in full for sick leave and family-event leave |
| Unified degressive general reduction | Calculated on the pay actually received; unpaid periods reduce annual pay and therefore increase the coefficient. This is arithmetically correct and requires no adjustment |
| DSN | The contract remains open and is declared each month with the suspension reason coded; it must not be closed |

Legal basis: Labour Code, Articles L1225-17 to L1225-46 (maternity, paternity, adoption), L1226-1 and D1226-1 (employer sick pay), L3141-3 to L3141-33 (paid leave), L3142-1 to L3142-5 (family event leave), L3142-16 and following (carer's leave), L3142-89 and following (reserve-forces leave); Social Security Code, Articles L321-1, L323-4, L331-3 to L331-8, L433-1 and following; Act n° 2024-364 of 22 April 2024 (paid leave accrual during sickness); Act n° 2025-1403 of 30 December 2025 (supplementary birth leave); Act n° 2026-492 of 12 June 2026 (family event leave); Décret n° 2025-160 of 20 February 2025 (daily sickness benefit cap); Court of Cassation, Social Chamber, judgment of 21 January 2026 (24-day accrual cap assessed per reference period).

## Module 9: Termination & Irregular Payments


### 9.1 Termination Payments


#### What are the different types of termination payments?

French termination pay is not one payment but a final settlement (solde de tout compte) made up of several distinct items, each with its own legal basis and its own social and tax treatment. The single most damaging modelling error in this area is to treat the settlement as one taxable lump: two of its components are ordinary pay in every respect, while the others carry a three-layer exemption regime that differs between social security contributions, the social levies and income tax.

| Payment | When it arises | Legal basis | Nature |
|---|---|---|---|
| Salary to the last day of the contract | Always | Labour Code Article L3242-1 | Ordinary pay |
| Compensatory notice indemnity (indemnité compensatrice de préavis) | Where the employer releases the employee from working the notice period | Labour Code Article L1234-5 | Ordinary pay — fully contributable and taxable |
| Compensatory leave indemnity (indemnité compensatrice de congés payés) | Whenever paid leave remains untaken, including after serious misconduct | Labour Code Article L3141-28 | Ordinary pay — fully contributable and taxable |
| Statutory redundancy payment (indemnité légale de licenciement) | Dismissal of an employee with 8 months' continuous service, other than for serious or gross misconduct | Labour Code Articles L1234-9 and R1234-1 to R1234-4 | Exempt within limits |
| Collectively agreed redundancy payment | Where the sector or company agreement provides a higher amount | The applicable agreement | Exempt within limits |
| Mutually agreed termination indemnity (indemnité de rupture conventionnelle) | Termination by mutual agreement, approved by the labour administration | Labour Code Articles L1237-11 to L1237-16 | Exempt within limits, plus a 40 % employer contribution |
| Compulsory retirement indemnity (indemnité de mise à la retraite) | Retirement at the employer's initiative | Labour Code Article L1237-7 | Exempt within limits, plus a 40 % employer contribution |
| Voluntary retirement indemnity (indemnité de départ à la retraite) | Retirement at the employee's initiative | Labour Code Article L1237-9 | Fully contributable and taxable, unless paid under a collective redundancy plan |
| End-of-contract indemnity for a fixed-term contract (indemnité de fin de contrat, commonly the "precarity bonus") | Expiry of a fixed-term contract or a temporary-agency assignment | Labour Code Articles L1243-8 and L1243-9 | Ordinary pay — fully contributable and taxable |
| Non-compete indemnity (contrepartie financière à la clause de non-concurrence) | Where a non-compete clause is enforced after departure | Labour Code, and the applicable agreement | Ordinary pay, paid after the contract has ended and still declared in the DSN |
| Settlement sum (indemnité transactionnelle) | Where a settlement agreement closes a dispute | Civil Code Article 2044 | Treated according to what it actually compensates — see below |
| Court-awarded damages for dismissal without real and serious cause | Judgment of the labour court | Labour Code Article L1235-3 | Exempt from income tax and, within limits, from contributions |
| Damages for early termination of a fixed-term contract by the employer | Termination without one of the statutory grounds | Labour Code Article L1243-4 | At least the pay the employee would have received to the contract's term; ordinary pay |

Notice periods, which drive the compensatory notice indemnity, are set by Labour Code Article L1234-1 and may be improved by the applicable agreement:

| Length of service at dismissal | Statutory notice |
|---|---|
| Less than 6 months | No statutory duration — the collective agreement, the contract or local and sector custom applies |
| 6 months to less than 2 years | 1 month |
| 2 years or more | 2 months |

Resignation is different: Labour Code Article L1237-1 fixes no statutory notice at all and refers entirely to the collective agreement, the contract or custom. A payroll engine that defaults resignation notice to the dismissal scale will be wrong for most sectors, because agreements routinely set three months for managerial grades.
The end-of-contract indemnity for fixed-term contracts is 10 % of the total gross remuneration paid over the contract (Article L1243-8), reducible to 6 % by a branch agreement that provides compensating access to vocational training (Article L1243-9). It is not due where the contract converts into a permanent contract, where the employee refuses an offer of a permanent contract for the same job at at least equivalent pay, for seasonal contracts and customary-use contracts, for apprenticeship and professionalisation contracts, for contracts with young people during school holidays, or where the contract ends on the employee's initiative or for serious misconduct.

#### How do termination rules and calculations differ by residential status and employer type?

Residential status changes nothing in the labour-law calculation and everything in the tax mechanics. The statutory redundancy payment, the notice period and the leave payout are identical for a resident and a non-resident working in France, because they derive from the Labour Code and follow the contract, not the employee's tax domicile. What differs is how the taxable fraction is withheld.

| Dimension | Resident | Non-resident |
|---|---|---|
| Amount of the statutory redundancy payment | Identical | Identical |
| Exemption from social security contributions | Identical, if the employee is within the French scheme | Identical, if the employee is within the French scheme; nothing is due if the employee holds a portable document A1 for another state |
| Social levies on the non-exempt fraction | 9.70 %, on 100 % with no allowance | Same, if within the French scheme |
| Income tax on the taxable fraction | Added to the month's net taxable amount and taxed at the transmitted rate or the default grid | Enters the specific non-resident withholding base of General Tax Code Article 182 A for the period, after the 10 % flat deduction, and is sliced across the 0 / 12 / 20 bands. A large severance therefore pushes the period into the 20 % band, which is not liberatory and requires a French return |
| Treaty position | Not applicable | A treaty may allocate the severance to the state of former employment rather than the state of payment. Where the employee worked in several states, more than one treaty may apportion it. This is a per-case determination and is not automatable |

Employer type affects three things and only three.

| Employer characteristic | Effect |
|---|---|
| Fewer than 11 employees | The cap on court-awarded damages for dismissal without real and serious cause (Labour Code Article L1235-3) uses a lower scale for the first ten years of service. No effect at all on the statutory redundancy payment |
| 50 or more employees, dismissing 10 or more employees in 30 days | A collective redundancy plan (plan de sauvegarde de l'emploi) is compulsory. Severance paid under such a plan is fully exempt from income tax without limit (General Tax Code Article 80 duodecies, 1°), and a voluntary retirement indemnity paid under the plan likewise becomes exempt |
| Construction, public works and entertainment employers affiliated to a sector paid-leave fund | The employer pays no compensatory leave indemnity; the employee claims from the fund and the employer issues a leave certificate |

Public-sector employers and their statutory staff are outside this guide, which is scoped to the general private-sector scheme.

#### Detail the calculation and tax withholding rules for unused leave paid out on termination.

The compensatory leave indemnity is ordinary remuneration. This is worth stating flatly because it sits next to the severance payment in the same settlement and is repeatedly given the severance treatment by mistake.

| Dimension | Treatment |
|---|---|
| Amount | The higher of the one-tenth rule and the salary maintenance rule, applied to the untaken days — the same comparison as leave actually taken (Module 8) |
| Scope | The current reference period and any balance carried forward from an earlier period, including leave carried over after sickness |
| Serious misconduct | Still payable. The forfeiture that used to apply was abolished, and withholding it is unlawful |
| Notice not worked | Leave continues to accrue over a paid notice period the employee is released from working, and that accrual is added to the payout |
| Social security contributions | Due in full, on all bands, with the ceiling prorated to the employment period |
| Social levies | Due, on 98.25 % of the amount like ordinary pay — not on 100 %, because it is remuneration and not a rupture indemnity |
| Income tax | Included in the month's net taxable amount and withheld at the employee's rate or the default grid |
| Working-time reduction days and time-savings-account balances | Paid out only where the agreement provides; when paid they are ordinary pay on the same footing |

Worked example. An employee leaving on 31 October 2026 has 8 working days of leave untaken. Gross pay over the reference period 1 June 2025 to 31 May 2026 was EUR 44,800.00, against 30 working days acquired. Current monthly salary is EUR 3,600.00 and October 2026 contains 26 working days.

| Method | Calculation | Result |
|---|---|---|
| One-tenth rule | (44,800.00 × 1/10) × 8 ÷ 30 | EUR 1,194.67 |
| Salary maintenance rule | 3,600.00 × 8 ÷ 26 | EUR 1,107.69 |
| Compensatory leave indemnity due | The higher of the two | EUR 1,194.67 |


#### Describe the rules for statutory severance/redundancy payments.

Eligibility. Labour Code Article L1234-9 gives the statutory redundancy payment to an employee on a permanent contract with at least eight months' continuous service with the same employer, dismissed for any reason other than serious misconduct (faute grave) or gross misconduct (faute lourde). It is due on both personal-grounds and economic dismissals. Length of service is measured to the end of the notice period, whether or not the notice is actually worked.
The formula is fixed by Labour Code Article R1234-2:

| Slice of service | Fraction of a month's reference salary per year |
|---|---|
| Each year up to and including the tenth | 1/4 |
| Each year from the eleventh | 1/3 |

An incomplete year is counted in proportion to the number of complete months (Article R1234-1). The collectively agreed amount applies instead where it is higher, and in many sectors it is substantially higher for managerial grades.
The reference salary is fixed by Labour Code Article R1234-4 as the more favourable to the employee of two calculations:

| Basis | Definition |
|---|---|
| Twelve-month average | The average monthly remuneration of the twelve months preceding the dismissal, or of all months of service where service is shorter than twelve months |
| Three-month average | One third of the last three months' remuneration, with any annual or exceptional bonus paid in that window counted only in proportion — a thirteenth month paid in December counts for 3/12 of its value in a three-month window |

The comparison is compulsory, not an option, and the pro-rating of annual bonuses inside the three-month basis is the detail most often missed. Where the employee's pay was reduced by sickness, part-time parental leave or partial activity during the reference window, the reference salary is reconstituted at the pay the employee would have received had they worked normally.
Doubling for occupational incapacity. Where the dismissal follows a declaration of unfitness arising from a work accident or an occupational disease, the statutory redundancy payment is doubled (Labour Code Article L1226-14), and the employee also receives a special compensatory indemnity equal to the notice pay even though no notice is worked.

#### Provide the statutory formula for any tax-free portion.

France applies three separate exemption tests to the same payment, in a fixed order, and they give three different answers. Computing one exemption and reusing it for the others is the defining error of this area.
Test 1 — income tax (General Tax Code Article 80 duodecies, 1°). The payment is exempt up to the highest of:

| Limb | Amount | Cap |
|---|---|---|
| (a) The amount fixed by the sector agreement, the professional agreement or, failing either, by law | The legal or collectively agreed redundancy payment | No cap |
| (b) Twice the gross annual remuneration received in the calendar year preceding the termination | 2 × previous year's gross | 6 PASS = EUR 288,360 for 2026 |
| (c) Half the total indemnity | 50 % of the amount paid | 6 PASS = EUR 288,360 for 2026 |

Severance paid under a collective redundancy plan, and damages awarded by a court for dismissal without real and serious cause, are fully exempt from income tax with no ceiling.
Test 2 — social security contributions (Social Security Code Article L242-1, III). The payment is exempt for the fraction that is exempt from income tax under Test 1, but the exemption is itself capped at 2 PASS = EUR 96,120 for 2026.
Test 3 — the social levies (Social Security Code Article L136-1-1). The general social contribution and the social debt repayment contribution are exempt only up to the lower of:
- the legal or collectively agreed redundancy payment; and
- the fraction exempt from social security contributions under Test 2.
Any excess bears the two levies at a combined 9.70 % on 100 % of the amount — the 1.75 % professional-expense allowance does not apply to rupture indemnities. That levy is entirely non-deductible for income tax, because the underlying payment is itself exempt from income tax (General Tax Code Article 154 quinquies).
The cliff at 10 PASS. Where the total of all indemnities paid on the termination exceeds 10 PASS = EUR 480,600 for 2026, every social exemption is lost and the whole amount is subject to social security contributions and to the social levies from the first euro. This is a cliff, not a taper: a package of EUR 480,601 is treated worse in its entirety than one of EUR 480,600. It must be modelled as a threshold test on the aggregate, evaluated before any of the three tests above.
The specific employer contribution. Social Security Code Article L137-12, as amended by Article 15 of the Social Security Financing Act for 2026, charges the employer 40 % — raised from 30 % with effect from 1 January 2026 — on the fraction of a mutually agreed termination indemnity or a compulsory retirement indemnity that is exempt from social security contributions. It does not apply to a dismissal, to a voluntary retirement or to the expiry of a fixed-term contract. It is an employer cost, is never deducted from the employee, and does not change the employee's net.

#### Deliverable: For other Employment Termination Payments (ETPs), provide a reference guide.


| Payment | Social security contributions | Social levies (9.70 %) | Income tax | 40 % employer contribution |
|---|---|---|---|---|
| Salary to the leaving date | Due in full | Due, on 98.25 % | Taxable | No |
| Compensatory notice indemnity | Due in full | Due, on 98.25 % | Taxable | No |
| Compensatory leave indemnity | Due in full | Due, on 98.25 % | Taxable | No |
| Fixed-term end-of-contract indemnity (10 % or 6 %) | Due in full | Due, on 98.25 % | Taxable | No |
| Non-compete indemnity | Due in full | Due, on 98.25 % | Taxable | No |
| Statutory or collectively agreed redundancy payment | Exempt to the income-tax-exempt fraction, capped at 2 PASS (EUR 96,120) | Exempt only to the legal or agreed amount, and no further than the contribution exemption | Exempt per Article 80 duodecies | No |
| Redundancy payment above the legal or agreed amount | Exempt within the same 2 PASS ceiling if income-tax exempt | Due on the excess over the legal or agreed amount | Exempt only within the Article 80 duodecies limbs | No |
| Severance under a collective redundancy plan | Exempt to 2 PASS | Exempt to the legal or agreed amount | Fully exempt, no ceiling | No |
| Mutually agreed termination indemnity, employee not entitled to a full-rate pension | Exempt to 2 PASS | Exempt to the legal or agreed amount | Exempt per Article 80 duodecies | Yes, 40 % |
| Mutually agreed termination indemnity, employee entitled to a full-rate pension | Due in full from the first euro | Due in full | Taxable in full | No — ordinary contributions apply instead |
| Compulsory retirement indemnity | Exempt to 2 PASS | Exempt to the legal or agreed amount | Exempt per Article 80 duodecies | Yes, 40 % |
| Voluntary retirement indemnity, outside a collective redundancy plan | Due in full | Due in full, on 98.25 % | Taxable in full | No |
| Voluntary retirement indemnity, under a collective redundancy plan | Exempt to 2 PASS | Exempt to the legal or agreed amount | Fully exempt | No |
| Court damages for dismissal without real and serious cause | Exempt to 2 PASS | Exempt to the legal or agreed amount | Fully exempt | No |
| Settlement sum compensating loss of employment | Follows the severance regime | Follows the severance regime | Follows the severance regime | Only where the underlying termination was a mutually agreed termination or a compulsory retirement |
| Settlement sum compensating a pay element — unpaid notice, an unpaid bonus, unpaid overtime | Ordinary pay, due in full | Due, on 98.25 % | Taxable | No |
| Any package whose aggregate exceeds 10 PASS (EUR 480,600) | Due in full from the first euro | Due in full from the first euro | The Article 80 duodecies limbs still apply | Not applicable — the exempt base is nil |

Two entries deserve emphasis in a client conversation. A settlement sum is not automatically severance: the collecting body looks at what each element actually compensates, and a settlement that is silent on its composition risks being reclassified as ordinary pay in full. And a mutually agreed termination with an employee who can already draw a full-rate pension loses the exemption entirely — a trap in terminations negotiated with employees in their sixties, and one that reverses the usual cost comparison against a dismissal.

#### Deliverable: Detail the rules for any applicable concessional tax cap.

The caps are the three ceiling multiples above, and they operate at different levels. Set out as a single decision sequence:
1. AGGREGATE all indemnities paid on this termination
(severance + any supra-legal top-up + settlement sums
compensating loss of employment; NOT salary, notice or
leave, which are ordinary pay).
2. IS THE AGGREGATE > 10 PASS  (EUR 480,600 for 2026) ?
|-- YES -> Social security contributions and the 9.70 %
|          levies are due on the WHOLE amount from the
|          first euro. Go to step 3 for income tax only.
|-- NO  -> continue.
3. INCOME TAX (General Tax Code Article 80 duodecies, 1°)
Exempt fraction = MAX of
(a) legal or collectively agreed amount        [no cap]
(b) 2 x previous calendar year's gross pay     [cap 6 PASS = 288,360]
(c) 50 % of the total indemnity                [cap 6 PASS = 288,360]
Collective redundancy plan, or court damages -> fully exempt.
4. SOCIAL SECURITY CONTRIBUTIONS (Social Security Code L242-1, III)
Exempt fraction = MIN ( the step-3 exempt fraction ,
2 PASS = EUR 96,120 )
5. SOCIAL LEVIES (Social Security Code L136-1-1)
Exempt fraction = MIN ( legal or collectively agreed amount ,
the step-4 exempt fraction )
Excess bears 9.70 % on 100 %, entirely non-deductible.
6. EMPLOYER 40 % CONTRIBUTION (Social Security Code L137-12)
Applies only to a mutually agreed termination or a
compulsory retirement, on the step-4 exempt fraction.
Two caps that are not concessional tax caps and must not be confused with them: the cap on court-awarded damages for dismissal without real and serious cause (Labour Code Article L1235-3), which limits what a court may award and is a litigation rule rather than a tax rule; and the six-annual-ceiling limit on tax-free savings-scheme amounts, which belongs to Module 7.

#### Deliverable: Provide a detailed worked example of a redundancy termination payout.

Facts. A non-managerial employee joined a company of 30 employees on 1 March 2014 and is dismissed on economic grounds outside a collective redundancy plan. The two-month notice is worked and the contract ends on 31 October 2026. Monthly gross salary was EUR 3,400.00 to 30 April 2026 and EUR 3,600.00 from 1 May 2026. An annual bonus of EUR 4,800.00 was paid in December 2025. Gross pay for the calendar year 2025 was EUR 45,600.00. The collective agreement fixes a redundancy payment of EUR 15,000.00 for this length of service, and the employer negotiates a total of EUR 20,000.00. Eight working days of leave are untaken. The employee is on a transmitted personal withholding rate of 9.90 %.
Step 1 — length of service. 1 March 2014 to 31 October 2026 = 12 years and 8 complete months.
Step 2 — reference salary (Labour Code Article R1234-4, the more favourable of the two):

| Basis | Calculation | Result |
|---|---|---|
| Twelve-month average (Nov 2025 – Oct 2026) | (6 × 3,400.00) + (6 × 3,600.00) + 4,800.00 = 46,800.00, ÷ 12 | EUR 3,900.00 |
| Three-month average (Aug – Oct 2026) | (3 × 3,600.00) + (4,800.00 × 3/12) = 12,000.00, ÷ 3 | EUR 4,000.00 |
| Reference salary retained | The higher of the two | EUR 4,000.00 |

Step 3 — statutory redundancy payment (Labour Code Article R1234-2):

| Slice | Calculation | Result |
|---|---|---|
| First 10 years, at 1/4 | 10 × 1/4 × 4,000.00 | EUR 10,000.00 |
| Years 11 and 12, at 1/3 | 2 × 1/3 × 4,000.00 | EUR 2,666.67 |
| 8 complete months beyond, at 1/3 | 1/3 × 4,000.00 × 8/12 | EUR 888.89 |
| Statutory minimum |  | EUR 13,555.56 |
| Collectively agreed amount | Per the sector agreement | EUR 15,000.00 |
| Floor that applies | The higher of the two | EUR 15,000.00 |
| Amount actually paid | Negotiated | EUR 20,000.00 |

Step 4 — the three exemption tests on the EUR 20,000.00.

| Test | Rule | Calculation | Outcome |
|---|---|---|---|
| Aggregate against 10 PASS | 20,000.00 against EUR 480,600 | Far below | No cliff; exemptions available |
| Income tax, limb (a) | Collectively agreed amount, uncapped | — | EUR 15,000.00 |
| Income tax, limb (b) | 2 × 2025 gross, capped at 6 PASS | 2 × 45,600.00 = 91,200.00, below 288,360 | EUR 91,200.00 |
| Income tax, limb (c) | 50 % of the indemnity, capped at 6 PASS | 50 % × 20,000.00 | EUR 10,000.00 |
| Income tax exempt fraction | The highest limb | 91,200.00 exceeds the 20,000.00 paid | The whole EUR 20,000.00 is exempt |
| Social security contributions | The income-tax-exempt fraction, capped at 2 PASS | min(20,000.00 ; 96,120) | The whole EUR 20,000.00 is exempt |
| Social levies | The lower of the agreed amount and the contribution-exempt fraction | min(15,000.00 ; 20,000.00) | EUR 15,000.00 exempt; EUR 5,000.00 subject |
| Levies due | 9.70 % on 100 % of EUR 5,000.00, no allowance | 5,000.00 × 9.70 % | EUR 485.00, wholly non-deductible |
| 40 % employer contribution | A dismissal, not a mutually agreed termination or a compulsory retirement | — | Not due |

Step 5 — the October 2026 final settlement.

| Line | Basis | Amount |
|---|---|---|
| October salary (notice worked) | Ordinary pay | 3,600.00 |
| Compensatory leave indemnity, 8 days | Higher of the two methods, from the example above | 1,194.67 |
| Gross subject to contributions |  | 4,794.67 |
| Old-age, capped | Full month present, ceiling EUR 4,005.00, at 6.90 % | −276.35 |
| Old-age, uncapped | 4,794.67 × 0.40 % | −19.18 |
| Supplementary pension, band 1 | 4,005.00 × 3.15 % | −126.16 |
| Supplementary pension, band 2 | (4,794.67 − 4,005.00) = 789.67 × 8.64 % | −68.23 |
| General balance contribution, band 1 | 4,005.00 × 0.86 % | −34.44 |
| General balance contribution, band 2 | 789.67 × 1.08 % | −8.53 |
| Technical balance contribution | 4,794.67 × 0.14 % — due, because pay exceeds the ceiling | −6.71 |
| Employee health-cover share | Per the policy | −30.00 |
| Social levies on ordinary pay | ((4,794.67 × 98.25 %) + 30.00) = 4,740.81, at 9.70 % | −459.86 |
| Social levies on the non-exempt severance fraction | 5,000.00 × 9.70 %, on 100 % | −485.00 |
| Total employee deductions |  | −1,514.46 |
| Net payable before income tax | 4,794.67 − 1,514.46 | 3,280.21 |
| Net taxable amount | 3,280.21 + non-deductible levies on pay (4,740.81 × 2.90 % = 137.48) + 30.00 employer health share. The severance is income-tax exempt and the levies on it are non-deductible, so neither enters this figure | 3,447.69 |
| Income tax withheld | 3,447.69 × 9.90 % | −341.32 |
| Severance paid | EUR 20,000.00, exempt from income tax | +20,000.00 |
| Net paid in the final settlement | 3,280.21 − 341.32 + 20,000.00 | EUR 22,938.89 |

Three points that generalise from this settlement:
1. The severance never enters the net taxable amount, so it bears no withholding at source — but the EUR 5,000.00 fraction above the collectively agreed amount still bears EUR 485.00 of social levies. "Exempt from income tax" and "exempt from the levies" are different questions with different answers, and the second is decided by a different comparison from the first.
1. The leave payout is ordinary pay and sits inside the contribution bands alongside the salary, which is why supplementary pension band 2 and the technical balance contribution appear in a month where salary alone would not have crossed the ceiling.
1. The progressive ceiling reconciliation and the annual reconciliation of the general reduction must both be run in this payslip, not deferred to December. There will be no further payslip for this employee.
Legal basis: Labour Code, Articles L1226-14, L1234-1, L1234-5, L1234-9, L1235-3, L1237-1, L1237-7, L1237-9, L1237-11 to L1237-16, L1243-4, L1243-8, L1243-9, L3141-28, L3242-1, R1234-1 to R1234-4; Social Security Code, Articles L136-1-1, L137-12, L242-1, III; General Tax Code, Articles 80 duodecies, 154 quinquies, 182 A; Civil Code, Article 2044; Act n° 2025-1403 of 30 December 2025 (Social Security Financing Act for 2026), Article 15; Arrêté of 22 December 2025 (2026 social security ceiling).

### 9.2 Irregular and Retrospective Payments


#### Describe the specific tax calculation method required for irregular payments.

There is none, and that absence is what must be configured. France has no separate schedule for irregular payments, no annualisation, no spreading and no re-banding. An irregular payment — a bonus, a commission catch-up, the taxable excess of a severance, a settlement sum, a leave payout — is added to the net taxable amount of the month in which it is paid, and the employee's ordinary withholding rate is applied to the total.

| Question a client will ask | Answer for France |
|---|---|
| Does a large bonus push the employee into a higher withholding band? | No for an employee on a transmitted rate: the rate is a fixed percentage, so doubling the month's pay doubles the tax but not the rate |
| And for an employee on the default grid? | Yes, because the default grid reads a band from the month's amount. A bonus month lands in a higher band and the whole month is then taxed at that higher flat rate. This is the one place where an irregular payment does change the rate, and a further reason to encourage employees to have their personal rate transmitted |
| Should the payment be spread over the year? | No. There is no spreading mechanism in payroll |
| Should the employer re-run prior months? | No. The withholding attaches to the period of payment |
| Will the employee be over-taxed? | Possibly for a year, and the tax administration corrects it: the annual assessment settles the true liability and the recalculated rate applies from the following September |
| Is there any relief for a genuinely exceptional payment? | Yes, but at assessment level, not in payroll: the employee may claim the quotient system for exceptional income on their annual return (General Tax Code Article 163-0 A). The employer neither applies it nor reports anything for it |

For a non-resident the answer is the opposite in shape: the Article 182 A scale is genuinely progressive across the period's bands, so an irregular payment does slice into the 12 % and then the 20 % band. Where the payment reaches the 20 % band, that fraction ceases to be liberatory and the employee must file a French return.

#### How are backdated payments and retrospective salary adjustments handled?

The governing principle is that social security and income tax attach the payment to different periods, and a system that uses one period for both will file a DSN that does not reconcile.

| Dimension | Period the payment attaches to | Consequence |
|---|---|---|
| Social security contributions | The period of employment the pay relates to (Social Security Code Article R242-1) | The rates, the ceiling and the reduction parameters of that original period apply, not those of the payment month |
| Income tax withholding | The period of payment (General Tax Code Article 204 B) | The rate in force when the arrears are paid applies to the whole amount, in the month it is paid |
| DSN reporting | Both, simultaneously | The arrears are declared in the current month's DSN. The contribution correction is carried in the contribution-base block, which holds the start and end dates of the period the pay attaches to; a withholding correction is carried in the separate withholding-regularisation block, dated to the month of the original error. The two use different blocks and must not be conflated |

Within the same calendar year, a back-payment is normally absorbed by the progressive ceiling reconciliation: adding the arrears to the current month's base and letting the cumulative reconciliation re-slice the capped and uncapped bands produces the correct result automatically, because the cumulative ceiling entitlement already covers the earlier months.
Across a year boundary it does not. Arrears relating to 2025 but paid in 2026 must be calculated at the 2025 rates and against the 2025 ceiling of EUR 3,925, and declared in the 2026 DSN with a regularisation block carrying the 2025 period. Applying 2026 rates to 2025 arrears is the most common finding on a contribution inspection of this area, and in 2026 it produces an error in both directions: the employer loses the reduced sickness and family-allowance rates that were still available in 2025, and it computes the general reduction against the wrong minimum-wage reference.
Two further rules complete the picture. Limitation: an employee's claim for unpaid wages is barred three years after the day they knew or should have known of the facts, and where the contract has ended the claim may reach back three years from that date (Labour Code Article L3245-1). Collective pay rises with retrospective effect, common in French sector bargaining where an agreement signed in June applies from 1 January, are handled exactly as arrears: contributions at the rates of each month covered, income tax in the month of payment.

#### For arrears, how are contributions and deductions computed?

Step by step, for a back-payment covering a period already declared:
1. Identify the months the arrears relate to and split the amount across them. Where the arrears derive from a rate increase, split in proportion to the pay of each month; where they derive from unpaid hours, allocate to the months the hours were worked.
1. Recompute each affected month's contribution base, adding the allocated arrears to the pay already declared for that month.
1. Re-slice the bands for each month against that month's ceiling — EUR 3,925 for a 2025 month, EUR 4,005 for a 2026 month — and apply that month's rates.
1. Recompute the general reduction for the affected months on the corrected annual pay, using the minimum-wage reference of the year concerned: the frozen EUR 12.02 for 2026 months, and the 2025 parameters for 2025 months.
1. Recompute the social levies on the arrears at 98.25 % where the arrears are ordinary pay, and re-test the year's cumulative pay against the four-annual-ceiling limit on the 1.75 % allowance.
1. Take the difference between the recomputed contributions and those already declared, per month and per contribution.
1. Declare the arrears in the current month's DSN as remuneration, and the contribution differences in the contribution-base block (S21.G00.78), which carries the start and end dates of each period the pay attaches to, with the corresponding individual contribution block (S21.G00.81).
1. Withhold income tax on the whole amount in the current month, at the current rate, and include it in the current month's net taxable amount. Do not allocate it back to the earlier months for tax purposes.
1. Re-test any deduction that is a fraction of net pay — a garnishment in particular. A back-payment increases the month's net and therefore increases the seizable fraction, which is computed on the actual net of the month in which the arrears are paid.
1. Update the exempt-overtime counter if the arrears include overtime, against the EUR 7,500 annual income tax cap of the year of payment.
Where the employee has left, the arrears are still contributable and attach to the last period of employment; the employer issues a supplementary payslip and files a DSN for the month of payment carrying the former employee with the contract still identified. The employment relationship is not reopened, and no new pre-hire declaration is made.

#### Deliverable: Provide a worked example of a bonus calculation.

Facts. A non-managerial employee of a company with 30 employees is paid EUR 2,300.00 gross a month. In March 2026 they receive a performance bonus of EUR 1,500.00 and a value-sharing bonus of EUR 1,000.00. Employee and employer each pay EUR 30.00 a month toward the compulsory health cover. No withholding rate has been transmitted, so the default grid applies; March 2026 falls before 1 May, so the grid carried over from 2025 is used. The employee's pay over the preceding twelve months was EUR 27,600.00, below three times the annual minimum-wage reference of EUR 21,876.40, and the employer has fewer than 50 employees — so the enhanced value-sharing regime applies.

| Line | Basis | Rate | Amount |
|---|---|---|---|
| Base salary | — | — | 2,300.00 |
| Performance bonus | Ordinary remuneration | — | 1,500.00 |
| Gross subject to contributions | The value-sharing bonus is excluded |  | 3,800.00 |
| Old-age, capped | 3,800.00, below the EUR 4,005 ceiling | 6.90 % | −262.20 |
| Old-age, uncapped | 3,800.00 | 0.40 % | −15.20 |
| Supplementary pension, band 1 | 3,800.00 | 3.15 % | −119.70 |
| General balance contribution, band 1 | 3,800.00 | 0.86 % | −32.68 |
| Employee health-cover share | — | — | −30.00 |
| Social levies base | (3,800.00 × 98.25 %) + 30.00 employer share | — | 3,763.50 |
| General social contribution, deductible | 3,763.50 | 6.80 % | −255.92 |
| General social contribution, non-deductible | 3,763.50 | 2.40 % | −90.32 |
| Social debt repayment contribution | 3,763.50 | 0.50 % | −18.82 |
| Total employee contributions |  |  | −824.84 |
| Net payable before income tax | 3,800.00 − 824.84 |  | 2,975.16 |
| Net taxable amount | 2,975.16 + 90.32 + 18.82 + 30.00 |  | 3,114.30 |
| Default grid band | EUR 3,107 to 3,538.99 | 9.90 % | — |
| Income tax withheld | 3,114.30 × 9.90 % |  | −308.32 |
| Value-sharing bonus | Enhanced regime: exempt from contributions, from the social levies and from income tax |  | +1,000.00 |
| Net paid | 2,975.16 − 308.32 + 1,000.00 |  | EUR 3,666.84 |

The same value-sharing bonus in a company of 60 employees. The enhanced regime is unavailable and only the exemption from social security contributions survives:

| Line | Calculation | Amount |
|---|---|---|
| Value-sharing bonus | — | 1,000.00 |
| Social security contributions | Exempt within the EUR 3,000 annual cap | 0.00 |
| Social levies | 9.70 % on 100 %, with no 1.75 % allowance | −97.00 |
| Amount added to the net taxable amount | The gross bonus; the levies on it are non-deductible | +1,000.00 |
| Additional income tax withheld | The month's net taxable amount rises to EUR 4,114.30, moving the default grid to the EUR 3,983 – 4,647.99 band at 13.80 %; the withholding becomes 4,114.30 × 13.80 % = 567.77 | −259.45 more than before |
| Net value of the bonus to the employee | 1,000.00 − 97.00 − 259.45 | EUR 643.55 |

The same EUR 1,000.00 is worth EUR 1,000.00 to one employee and about EUR 644.00 to another, on nothing but the employer's headcount and the employee's pay level. Three further points follow for configuration:
1. The performance bonus would not change the withholding rate for an employee on a transmitted personal rate, but it does here, because the default grid bands on the month's amount. Both behaviours must be supported by the same engine.
1. The value-sharing bonus never enters the contribution bands, so it consumes no ceiling entitlement and cannot push the employee into supplementary pension band 2 — unlike the performance bonus, which can.
1. The enhanced regime expires on 31 December 2026. From 1 January 2027 the second table becomes the only treatment. This is a dated parameter and must carry a review flag rather than be set as a permanent rule.
Legal basis: Social Security Code, Articles L136-1-1, L137-15, L242-1, R242-1; General Tax Code, Articles 163-0 A, 182 A, 204 B; Labour Code, Article L3245-1; Act n° 2022-1158 of 16 August 2022, Article 1, as amended; DSN technical specification (cahier technique NEODeS), version CT2026.1.2 — contribution-base block S21.G00.78 and individual contribution block S21.G00.81 for contribution regularisations, withholding-regularisation block S21.G00.56 for corrections to the income tax withheld.

## Module 10: Reporting, Compliance & Finalisation

This module gives the configuration-level summary of France's reporting obligations. The field-level layouts, code lists and validation rules for each filing are held in the France Report Specifications (FR-NSSO / FR-FIN series) and are deliberately not reproduced here.

### 10.1 Statutory Reporting


#### Describe the country's primary digital payroll reporting system.

France has a single monthly payroll declaration, the nominative social declaration (Déclaration Sociale Nominative, DSN), and virtually everything an employer must report about pay travels inside it. This is the defining feature of French payroll reporting and it is the opposite of the multi-filing model used in most jurisdictions: there is no separate social security return, no separate income tax return for payroll, no separate pension return and no separate unemployment return. There is one file.

| Attribute | Content |
|---|---|
| Legal basis | Social Security Code Articles L133-5-3 and R133-13 to R133-14; Labour Code Article L1221-12-1 |
| Who files | Every private-sector employer, from the first employee, with no size threshold |
| Frequency | Monthly, one file per establishment, generated directly from the payroll result |
| Technical standard | The NEODeS norm, specified in the DSN technical specification (cahier technique), version CT2026.1.2 for the 2026 filing year |
| Format | A structured flat file of hierarchically numbered blocks, transmitted as a deposited file or through a machine-to-machine interface |
| Channel | The net-entreprises.fr portal, operated by the public-interest grouping for the modernisation of social declarations (GIP-MDS), or the equivalent agricultural channel for agricultural employers |
| Deadline | The 5th of the following month for employers with 50 or more employees paying wages in the same month; the 15th for all others. Postponed to the next working day where it falls on a Saturday, Sunday or public holiday |
| Payment | The social contributions and the income tax withheld are collected by direct debit initiated from the same file |

What the DSN replaces. A single monthly file discharges the employer's obligations to the contribution collection network (URSSAF), the old-age insurance funds, the sickness insurance funds, the supplementary pension institutions (Agirc-Arrco), the public employment service (France Travail), the public finances directorate (DGFiP) for the income tax withheld at source, the supplementary health and death-and-disability insurers, the sector paid-leave funds, and the statistical services. In its current scope it has absorbed some forty-five previously separate declarations.
Event signals. Alongside the monthly file, certain events must be reported within five days of the employer learning of them, through an event signal (signalement d'événement):

| Event signal | Purpose |
|---|---|
| End of contract (fin du contrat de travail) | Replaces the paper end-of-contract certificate transmitted to France Travail, and opens the employee's unemployment entitlement |
| Work stoppage (arrêt de travail) | Triggers the sickness, maternity, paternity or work-accident daily benefit |
| Resumption of work (reprise du travail) | Closes the benefit period |
| Amendment or cancellation of a previous signal | Corrects a signal already sent |

The pre-hire declaration (Déclaration Préalable À l'Embauche, DPAE) remains a separate filing to URSSAF in 2026. The technical specification provides for it to move into the DSN as a further event signal, but production was deferred and it is not expected before 1 January 2027; a build must not assume it is inside the DSN.
The second national withholding channel, and why it is out of scope here (scope decision). France
operates two declaration channels for withholding at source, and it is a common and costly error to
assume the payroll engine needs both. Wages and salaries travel in the DSN. Income that is not wages or
salaries travels in a separate monthly declaration, PASRAU, carried by its own norm (NEORAU) and its own
technical specification, version CT2026.1.1 for 2026. The PASRAU specification states its perimeter
expressly: the arrangement concerns bodies paying income other than wages and salaries — principally
pension and retirement funds, bodies paying replacement income, and the single-window schemes.

| Scope element | Determination for this build |
|---|---|
| What is in scope | The withholding at source on employment income for régime général private-sector employees, declared in the DSN (FR-DSN-001). The payroll engine builds no PASRAU file |
| What is owned upstream | Any PASRAU obligation belongs to the paying body, not to this employer's payroll: pension funds for retirement income, provident and insurance institutions where they pay replacement income directly to the employee, and the single-window schemes for the populations they cover. Individual employers are expressly excluded from PASRAU and keep their existing channels |
| The inbound data contract this implies | Where a third party pays income directly to an employee and files its own PASRAU, the employer's payroll must not withhold on that income and must not carry it in the DSN individual block. The engine therefore needs a flag on the payment source distinguishing paid by employer from paid directly by a third-party body. Where an insurer pays sickness top-up benefits through the employer (subrogation), the income stays in the DSN and this exclusion does not apply |
| What would reverse the decision | The client population extending beyond wage earners — for example an entity paying pensions or annuities, or an employer paying post-employment income to a person for whom no DSN individual block exists. That is a contained addition of one outbound flow, not a redesign |

Recorded in scope_manifest.json as FR-DGFIP-006, out of scope.
The return flow is part of the system, not an optional extra. After each filing the employer receives business return messages (comptes rendus métier, CRM) that must be read and acted on:

| Return | Sender | Content |
|---|---|---|
| Withholding rate return | DGFiP | The personal or individualised withholding rate for each employee, its type and its validity period. This is the only route by which the employer learns the rate |
| Identification return | URSSAF and the old-age insurance fund | Certification or rejection of each employee's social security number, and correction of civil-status data |
| Anomaly return | URSSAF | Blocking and non-blocking anomalies to correct in the next filing |
| Annual reminder return | URSSAF, issued in March | A list of anomalies left uncorrected over the preceding year |
| Post-substitution return | URSSAF | Notification that a substituted declaration has been applied — see below |

Substituted declarations, from June 2026. Where an employer leaves an anomaly uncorrected and raises no admissible objection, URSSAF and the agricultural fund may now correct the data themselves, transmit the corrected figures to the pension bodies and notify the employer. For 2026 this power is confined to the capped gross contribution base, because that base drives employees' pension entitlement. The practical consequence for an implementation is that unresolved anomalies are no longer merely untidy: the authority will substitute its own figure, and the employer's records will then diverge from the authority's unless the correction is brought back into payroll.
Penalties. Late filing, omission of an employee or inaccurate data each attract a penalty expressed as a fraction of the monthly social security ceiling per employee per month, and a failure to file at all exposes the employer to an assessment on an estimated basis.

#### Deliverable: Provide a Data Disaggregation Mapping Guide describing the main reporting categories.

The DSN is not a report of totals. It is a hierarchy of nested blocks that disaggregates each payroll result down to the individual employee, the individual contract, the individual contribution base and the individual contribution, and then re-aggregates it into the payment due to each collecting body. Every payroll engine feeding it must be able to produce the same figure at both levels and reconcile them.
The structural hierarchy

| Level | Block | What it carries | Principal consumer |
|---|---|---|---|
| Emitter | S10.G00.00 and following | Who produced and transmitted the file | GIP-MDS |
| Declaration | S20.G00.05 | Declaration type (monthly, event signal, cancel-and-replace), period, nature | All |
| Legal entity | S21.G00.06 | SIREN, legal name, address, headcount | All |
| Establishment | S21.G00.11 | SIRET, activity code, collective agreement identifier, industrial-accident risk code and rate | URSSAF, CARSAT, France Travail |
| Individual | S21.G00.30 | Social security number or temporary technical number, civil status, address | Old-age fund, sickness fund |
| Contract | S21.G00.40 | Contract type and dates, occupational category code, working time, managerial-grade flag, workplace establishment | France Travail, Agirc-Arrco, URSSAF |
| Payment to the individual | S21.G00.50 | Date of payment, net taxable amount, withholding rate and rate type, income tax withheld, net social amount | DGFiP |
| Remuneration | S21.G00.51 | Each remuneration component, its type code, the period it attaches to, hours paid | URSSAF, Agirc-Arrco |
| Bonuses and indemnities | S21.G00.52 | Bonuses and indemnities by type code | URSSAF |
| Other gross and net elements | S21.G00.53 and S21.G00.54 | Elements outside ordinary remuneration — severance, benefits in kind, expense reimbursements | URSSAF |
| Contribution base | S21.G00.78 | Each assessable base, its code, and the start and end dates of the period it attaches to | URSSAF, Agirc-Arrco, insurers |
| Individual contribution | S21.G00.81 | The contribution computed on that base, by code and by collecting body | URSSAF, Agirc-Arrco, insurers |
| Withholding regularisation | S21.G00.56 | Corrections to income tax withheld in an earlier month, dated to the month of the error | DGFiP |
| Aggregate contribution | S21.G00.23 | The employer-level total per contribution code and rate, rounded to the whole euro | URSSAF |
| Contribution schedule | S21.G00.22 | The schedule of amounts due for the period | URSSAF |
| Payment to a body | S21.G00.20 | The amount, method and date of payment to each collecting body | URSSAF, Agirc-Arrco, insurers |

How one payroll result disaggregates. A single employee's monthly payslip does not map to one DSN line; it explodes across the categories below, and each has a different rounding and period rule.

| Payroll quantity | Reporting category | Rounding | Period it attaches to |
|---|---|---|---|
| Base salary, overtime, bonuses, benefits in kind | Remuneration blocks, one per component type code | 2 decimals | The employment period the pay is for, which may not be the payment month |
| Capped gross base, uncapped gross base, supplementary pension bands 1 and 2, unemployment base, social levies base | Contribution-base block, one per base code | 2 decimals | The period of attachment, carried explicitly |
| Each employee and employer contribution | Individual contribution block, one per contribution code | 2 decimals | Follows its base |
| The same contributions summed for the establishment | Aggregate contribution block | Whole euro | The declared month |
| Net taxable amount, withholding rate, tax withheld | Individual payment block | 2 decimals; the remitted total to the whole euro | The payment month |
| Net social amount | Individual payment block | 2 decimals | The payment month |
| Hours paid and hours worked | Remuneration and contract blocks | 2 decimals | The employment period |
| The unified degressive general reduction, and the employer flat overtime deduction | Individual contribution blocks with their own negative-amount codes | 2 decimals | The employment period |

The reconciliation that must hold. The sum of the individual contribution blocks for a contribution code, rounded once at the end, must equal the aggregate contribution block for that code, which must equal the amount in the payment block. A system that rounds each employee to the euro and then sums will fail this test — the rounding rule of Social Security Code Article L130-1 applies to the aggregate, never to the individual line.
Field-level layouts, the full code lists for remuneration types, base codes and contribution codes, and the validation rules applied on deposit are held in the France Report Specifications and are not reproduced here.

#### List all other mandatory reports, stating the frequency, file format, due date, reporting authority.

In scope for the payroll engine.

| Report | Authority | Frequency | Format and channel | Due date |
|---|---|---|---|---|
| Nominative social declaration (DSN) | URSSAF and all attached bodies | Monthly | NEODeS structured file, net-entreprises.fr | 5th or 15th of the following month by headcount |
| DSN event signal — end of contract | France Travail | Per event | NEODeS signal, net-entreprises.fr | Within 5 days |
| DSN event signal — work stoppage and resumption | Sickness insurance fund | Per event | NEODeS signal, net-entreprises.fr | Within 5 days |
| Pre-hire declaration (DPAE) | URSSAF | Per hire | Online form or structured file, net-entreprises.fr | In the 8 days before the start, and before the employee begins work |
| Withholding at source remittance | DGFiP | Monthly, or quarterly on option below 11 employees | Direct debit initiated from the DSN | 8th or 18th of the following month by headcount |
| Disabled-worker employment return (DOETH) | URSSAF, for the Agefiph | Annual | Declared inside the April DSN; no separate filing | With the April DSN, due 5 or 15 May |
| Apprenticeship tax balance (0.09 %) | URSSAF | Annual | Declared inside the April DSN | With the April DSN, due 5 or 15 May |
| Allocation of the apprenticeship tax balance | Caisse des Dépôts | Annual | SOLTéA online platform | During the annual allocation window, which ran from 26 May to 21 October in 2026 |
| Payroll tax return, form 2501-SD | DGFiP | Monthly or quarterly, by amount | EDI or online filing, impots.gouv.fr | Within 15 days of the period |
| Payroll tax annual return and regularisation, form 2502-SD | DGFiP | Annual | EDI or online filing, impots.gouv.fr | 15 January of the following year where the tax is below EUR 4,000; 31 January where instalments were filed |
| Work accident declaration | Sickness insurance fund | Per event | Online form, net-entreprises.fr | Within 48 hours of learning of the accident |
| Posted-worker declaration | Ministry of Labour | Per posting | SIPSI online platform | Before the posting begins |

The payroll tax applies only to employers not liable to value added tax on at least 90 % of turnover — banks, insurers, associations, health bodies, holding companies. For a client outside that population the filing does not arise at all, and the engine should be configured to suppress it rather than to file a nil return.
Out of scope — reports that require data beyond payroll (C1).

| Report | Authority | Why it is out of scope | Client impact |
|---|---|---|---|
| Professional equality index (Index de l'égalité professionnelle femmes-hommes) | Ministry of Labour, Egapro platform, annually by 1 March, employers with 50 or more employees | Scores individual pay gaps by age band and occupational category and requires promotion rates, pay-rise rates and the sex of the ten highest earners. Promotion and pay-review data are held in the human-resources system, not in payroll | Refer to the HRMS team. Payroll can supply the remuneration and headcount inputs as an extract, but cannot produce or file the index |
| Social report (bilan social), employers with 300 or more employees | Works council | Requires recruitment, training, health-and-safety, industrial-relations and working-conditions data | Refer to the HRMS team |
| Economic, social and environmental database (BDESE) | Works council | Requires investment, environmental and governance data | Refer to the HRMS team |
| Labour activity and employment-conditions survey (ACEMO) | Ministry of Labour statistical service | A statistical survey of a sample of employers, requiring vacancy and working-conditions data | Refer to the HRMS team |
| Gender balance among senior executives and governing bodies, employers above 1,000 employees | Ministry of Labour | Requires the composition of governing bodies, which is corporate-secretariat data | Refer to the client's corporate secretariat |
| Company-vehicle taxes | DGFiP | Assessed on the fleet — vehicle emissions, age and use — not on payroll. Related to but distinct from the company-vehicle benefit in kind, which is in payroll scope | Refer to the client's finance or fleet function |


#### What pay elements are required as intermediates from payroll for reporting?

France requires the payroll engine to expose a number of quantities that are not shown as such on the payslip and are not needed to compute net pay, but without which the DSN cannot be built. Each must be a first-class stored value, not derived at reporting time.

| Intermediate | Why reporting needs it | Where it appears |
|---|---|---|
| Capped gross base (assiette brute plafonnée), after progressive ceiling reconciliation | Drives the employee's pension entitlement; it is the base URSSAF may now substitute | Contribution-base block |
| Uncapped gross base (assiette brute déplafonnée) | Base of most employer contributions | Contribution-base block |
| Supplementary pension bands 1 and 2, separately | Agirc-Arrco point allocation | Contribution-base block |
| Unemployment base, capped at four ceilings | Unemployment and wage-guarantee contributions | Contribution-base block |
| Social levies base, distinguishing the 98.25 % fraction from the 100 % fraction | The 1.75 % allowance is capped annually and the split must be evidenced | Contribution-base block |
| Net social amount (montant net social) | A statutory quantity used by the benefits authorities to assess the earned-income top-up and the active-solidarity income | Individual payment block and a compulsory payslip line |
| Net taxable amount (rémunération nette fiscale) | Base of the withholding, and the figure that pre-fills the employee's tax return | Individual payment block |
| Withholding rate, rate type and validity period | Evidences which rate was applied and why | Individual payment block |
| Income tax withheld | Remitted by direct debit | Individual payment block |
| Hours paid and hours worked, separately | Entitlement calculations and the working-time record | Remuneration and contract blocks |
| Overtime hours, and the exempt overtime pay year to date | The employer flat deduction and the EUR 7,500 annual income tax cap | Remuneration block and the year-to-date counter |
| The unified degressive general reduction, monthly and reconciled | Reported as a negative contribution with its own code | Individual contribution block |
| Average annual headcount of the legal entity | Determines the DSN deadline, the housing-fund rate, the training rate, the mobility levy liability and the disabled-worker obligation | Legal entity block |
| Industrial-accident risk code and net rate, per establishment | Contribution calculation and the establishment block | Establishment block |
| Collective agreement identifier (IDCC) and occupational category code | Validated on deposit; an inconsistent value generates an anomaly | Establishment and contract blocks |
| Disabled-worker status, work-study status, and the qualifying expenditure deductible from the disabled-worker contribution | Consolidated from the monthly flows into the April return | Contract block |
| Period of attachment on every base and every remuneration line | Arrears and corrections must be allocated to the right month | Every base and remuneration block |


### 10.2 Integrations


#### Is there any mandatory inbound integration?

Yes — and this is a point where France differs sharply from jurisdictions in which the employer is purely a sender. Two inbound flows are compulsory and payroll cannot be operated correctly without consuming them.

| Inbound flow | Source | Channel | What breaks without it |
|---|---|---|---|
| Withholding rate return (compte rendu métier from the tax administration) | DGFiP | Returned automatically against each monthly DSN, collected from net-entreprises.fr | The employer has no other lawful source for the employee's withholding rate. Without it every employee stays on the default grid, which over-withholds for employees with dependants and is a service failure rather than a compliance failure — but a rate received and not applied, or applied after its validity period, is a compliance failure |
| Industrial-accident rate notification | The regional sickness insurance fund (CARSAT), through the AT/MP account | Dematerialised notification on net-entreprises.fr. Subscribing to the account has been compulsory from the first employee since 1 January 2022 | The employer cannot lawfully receive its establishment-specific rate. Failure to subscribe attracts a penalty of between 0.5 % and 1.5 % of the monthly ceiling per employee, at 1 % for employers of 20 to 149 employees and at the maximum rate above that |

Three further inbound flows are operationally mandatory in the sense that ignoring them produces incorrect filings:

| Inbound flow | Source | Effect of ignoring it |
|---|---|---|
| Identification return certifying or rejecting each employee's social security number | URSSAF and the old-age insurance fund | Contracts remain on a temporary technical number, entitlements are not posted to the employee's record, and anomalies recur every month |
| Anomaly return, and the annual reminder issued in March | URSSAF | From June 2026 uncorrected anomalies on the capped gross base may be substituted by the authority, after which the employer's records and the authority's diverge |
| Daily social security benefit statements where the employer is subrogated | Sickness insurance fund | The offsetting payslip line cannot be reconciled and the employer's cash position is wrong |


#### Is there any mandatory outbound integration beyond standard reporting?


| Outbound flow | Recipient | Mandatory | Notes |
|---|---|---|---|
| Net pay by bank transfer | The employee's bank | Yes above EUR 1,500 net per month, where cash payment is prohibited by Labour Code Article L3241-1 | SEPA credit transfer, ISO 20022 payment initiation message. The account must be one the employee holds or jointly holds |
| Direct debit of social contributions and of the income tax withheld | URSSAF and DGFiP | Yes | Initiated from the DSN itself; the employer authorises the debit rather than pushing a payment |
| Allocation of the apprenticeship tax balance | Caisse des Dépôts, SOLTéA platform | The payment is compulsory; the allocation is optional | Where the employer makes no allocation the funds are distributed by a default rule. This is a client decision, not a payroll one |
| Contributions and membership data to the sector paid-leave fund | The fund (for example a construction-sector fund) | Yes, for employers in the covered sectors | These employers pay no holiday pay themselves; the fund does. A general-regime payroll configuration is wrong for them in both the payslip and the DSN |
| Supplementary health, death-and-disability and pension data | The insurers | Yes, but through the DSN | No separate file. The insurer is identified in the DSN by its membership reference; a wrong reference silently misroutes the contribution |
| Electronic payslip issue and archiving | The employee, and the archiving service | Only where the client elects electronic payslips | Election requires informing the employee, who may object. The archive must remain available for 50 years, or until the employee turns 75, whichever is later — an obligation that survives the end of the service contract |
| Payroll journal to the general ledger | The client's finance system | Not a statutory obligation | Mapped to the client's own accounting periods, which need not be the calendar year |


### 10.3 Payslip Requirements


#### List all mandatory components that must be itemized on an employee payslip.

The payslip is governed by Labour Code Articles L3243-1 to L3243-5 and R3243-1 to R3243-9. The presentation follows the simplified model of the Arrêté of 25 February 2016, amended by the Arrêté of 31 January 2023 which added the net social amount. A renovated model was scheduled for 2026 but was deferred by the Arrêté of 11 August 2025 to 1 January 2027; for the whole of 2026 the current simplified model remains the applicable one, and a build must not implement the renovated layout early.

| Group | Mandatory content |
|---|---|
| Employer | Name and address; the establishment's SIRET; the activity code; the collective agreement identifier (IDCC) and the agreement's title, or a reference to the Labour Code where none applies |
| Employee | Name; job title; occupational classification level or coefficient; managerial or non-managerial grade where the agreement uses it |
| Period and hours | The period covered; the dates of paid leave taken in the period and the corresponding amount; hours paid at the ordinary rate and hours paid at a premium rate, shown separately with their rates; where the employee is on a day-count or annualised arrangement, the nature and duration of that arrangement instead of hours |
| Gross | The gross amount, and each element of remuneration making it up |
| Contributions | Employee and employer contributions grouped by risk category — health, work accidents, retirement, family, unemployment, other — showing for each the base, the rate and the amount; the total of employee contributions and the total of employer contributions |
| Employer relief | The total of the exemptions and reliefs applied to employer contributions, shown as a single line |
| Statutory nets | Net social amount (montant net social); net payable before income tax; net paid |
| Income tax | The net taxable amount; the withholding rate applied; the amount of income tax withheld; the net paid after withholding |
| Cumulative figures | Year-to-date gross, net taxable amount and income tax withheld |
| Other | Total cost of employment for the employer; the date of payment; a statement that the payslip must be kept without time limit; and a reference to the public information page on the payslip |

Prohibited content. Article R3243-4 forbids any mention of the exercise of the right to strike or of activity as an employee representative. Where pay is affected by such an absence, the payslip shows only the amount, under a neutral description, and the nature of the absence is communicated separately.
Language and retention. The payslip must be in French (Module 1.1). The employer keeps its copy for five years; where the payslip is issued electronically, availability must be guaranteed for fifty years or until the employee reaches 75, whichever is later.
The line-by-line layout, the grouping of contributions into the statutory risk categories and the wording of every caption are specified in the France Payslip artefact and are not reproduced here.

### 10.4 Other Compliance


#### Is payroll software certification mandatory?

No. France does not certify, licence, approve or register payroll software, and there is no equivalent of the fiscal-cash-register or accreditation regimes found in some jurisdictions. A client asking whether a product must be "approved for France" should be told plainly that no such approval exists.
Four adjacent obligations are regularly mistaken for one and should be distinguished:

| Obligation | What it actually covers | Applies to payroll software? |
|---|---|---|
| Certification of cash-management software against the anti-fraud rules of General Tax Code Article 286, I, 3° bis | Software recording payments from private customers — point of sale, cash registers, takings management | No |
| Electronic invoicing and e-reporting reform | Supplier and customer invoices between businesses | No |
| Conformity of the DSN file to the NEODeS technical specification | The structure, code lists and internal consistency of the filed file | Not a certification, but effectively binding: a non-conforming file is rejected on deposit. Conformity is tested by the employer with the free self-check tool and the test environment on net-entreprises.fr before going live |
| Registration of the payroll service provider on net-entreprises.fr | Authorisation to file on the client's behalf | A registration and mandate, not a product certification |

What is mandatory is the substance rather than the tool: the employer must be able to produce a payslip that is arithmetically verifiable, keep the underlying records for the statutory periods, file a conforming DSN, and satisfy the data protection obligations of Module 2.3. Any product meeting those tests may be used.

### 10.5 Year-End Processing and Finalisation


#### Describe the mandatory year-end finalisation process.

France has no employer year-end tax return and no annual social security return. There is no equivalent of an annual reconciliation filing: the December DSN is an ordinary monthly DSN. What the year end does require is a set of calculations that must land inside that December payroll, because there is no later opportunity to make them.

| Step | What must happen | Where it lands |
|---|---|---|
| 1. Final progressive ceiling reconciliation | Compare cumulative pay to the cumulative ceiling entitlement for the year and correct the split between the capped and uncapped bands definitively | December payslip and DSN |
| 2. Annual reconciliation of the unified degressive general reduction | The reduction is an annual amount computed on annual gross pay; the monthly figures were provisional. For 2026 the reconciliation uses the frozen minimum-wage reference of EUR 21,876.40, not the June rate | December payslip and DSN |
| 3. Close the 1.75 % allowance cap on the social levies | The allowance stops at four annual ceilings, EUR 192,240 for 2026; recover any excess already granted | December payslip |
| 4. Close the exempt-overtime counter | Reconcile exempt overtime pay against the EUR 7,500 annual income tax cap; anything above enters the net taxable amount | December payslip |
| 5. Reconcile the disabled-worker data | The annual return is built from the twelve monthly flows and filed in the April DSN, so any correction to the year's data must be made before then | April DSN of the following year |
| 6. Payroll tax regularisation, where the client is liable | Form 2502-SD reconciles the instalments to the annual liability | By 15 January where no instalments were due, by 31 January where they were |
| 7. Apprenticeship tax balance | Computed on the closed year's payroll and declared in the April DSN of the following year | April DSN |
| 8. Refresh the year's parameters | New ceiling, new minimum wage, new grids, new reduction parameters, new attachment scale | Before the January payroll |
| 9. Roll the paid-leave reference period | The default period ends on 31 May, not 31 December — this is not a year-end task and must not be attached to one | 31 May |

The single trap worth naming is step 9. Almost every year-end checklist written for another jurisdiction assumes leave balances roll at the fiscal year end. In France they roll on 31 May by default, so the calendar year end and the leave year end are different events three weeks and five months apart.

#### What documentation or annual statements must be provided to employees?

Very little, and less than clients expect — because the tax administration receives the data directly from the DSN and pre-fills the employee's return with it.

| Document | Statutory? | Content and timing |
|---|---|---|
| Monthly payslip | Yes | The document of record. The December payslip carries the year-to-date gross, net taxable amount and income tax withheld, and in practice serves as the annual statement |
| Annual income tax certificate | No | There is none. The employer files no annual employee tax statement and issues no certificate. The employee's pre-filled return is populated from the DSN |
| End-of-contract documents | Yes, on departure | Work certificate (certificat de travail), the France Travail statement — transmitted electronically through the DSN event signal and given to the employee in signed form, the two being complementary — and the final settlement statement (reçu pour solde de tout compte). All three are due on the last day of work, and the work certificate and the France Travail statement may not be withheld pending payment |
| Employee savings statement | Yes, where a scheme exists | An annual statement of the employee's holdings in the company savings and retirement savings plans, issued by the scheme administrator rather than by payroll |
| Supplementary cover documents | Yes | The scheme's founding document and information notice on joining, and the annual renewal of any exemption from the compulsory health cover |
| Working-time record | On request | Where working time is not collective and uniform, the employer must be able to produce the individual record |


#### Is there a formal process for correcting errors discovered after the fiscal year has been closed?

Yes, and it is the same mechanism used during the year, because the DSN carries the period each figure attaches to. There is no year-end lock and no separate amendment return.

| Error | Correction route | Limit |
|---|---|---|
| Contribution error in a closed year | Regularise in a subsequent monthly DSN, carrying the closed period in the contribution-base block. The collecting body allocates it to the right month and applies that month's rates | Repayment claims are barred three years after the end of the year in which the contributions were paid (Social Security Code Article L243-6). The authority's own recovery right runs for three years plus the current year |
| Income tax withheld incorrectly in a closed year | File a withholding-regularisation block dated to the month of the error. The employer does not repay the employee directly for a closed year; the employee receives the correction through their annual assessment | Same three-year framework |
| Employee under-paid in a closed year | Pay the arrears now; contributions at the rates and ceiling of the original period, income tax in the month of payment (Module 9.2) | Pay claims are barred three years from when the employee knew or should have known of the facts |
| Employee over-paid in a closed year | Recover from future pay within the seizable fraction, or by agreement. Recovery of an overpayment of wages is barred after three years | The employer may not simply deduct the whole amount from one payslip |
| Data error only, with no financial effect — a wrong occupational category code, a wrong contract end reason | Correct in the next monthly DSN; where the error affects an event signal, send an amending signal | None, but uncorrected anomalies now risk substitution |
| Error discovered before the filing deadline of the month concerned | File a cancel-and-replace declaration for that month, which supersedes the first entirely | Only available until the deadline for that month |

Two rules govern all of them. Correct in the period, not in the current month: adding a prior-year amount to the current month's base without carrying the period is the error that inspections find most often, because it puts the contribution in the wrong year for both the employer's liability and the employee's entitlement. And the employee's income tax position is not the employer's to settle for a closed year: the employer corrects its declaration, and the tax administration settles with the employee through the assessment.
Legal basis: Social Security Code, Articles L130-1, L133-5-3, L243-6, R133-13 to R133-14, R243-6; Labour Code, Articles L1221-12-1, L1234-19, L3241-1, L3243-1 to L3243-5, R3243-1 to R3243-9, D3243-8, R5212-1 and following (disabled-worker employment obligation); General Tax Code, Articles 231 and following (payroll tax), 286, I, 3° bis, 1671; Arrêté of 25 February 2016 as amended by the Arrêté of 31 January 2023 (payslip model and net social amount); Arrêté of 11 August 2025 (deferral of the renovated payslip model to 1 January 2027); DSN technical specification (cahier technique NEODeS), version CT2026.1.2.

## Module 11: Advanced Scenarios & Cross-Cutting Logic


### 11.1 Calculation Logic


#### How is the proration and projection logic applied for income tax, social security, exemptions, and deductions?

France separates the two ideas cleanly, and the separation is the answer: social security prorates heavily and projects not at all; income tax neither prorates nor projects. An implementation migrating from a cumulative-basis jurisdiction will typically build projection logic that France does not use, and will typically forget half the proration France does require.

| Domain | Prorated? | Projected? | Rule |
|---|---|---|---|
| Income tax withholding | No | No | The rate is applied to the amount actually paid in the period. There is no annualisation, no estimate of full-year income and no cumulative recalculation. A part-month payment naturally falls in a lower default-grid band and must not be grossed up to a notional full month |
| Social security ceiling | Yes | No | Prorated for part-time work, for a part month of employment and for unpaid absence, then reconciled cumulatively month by month against the annual ceiling |
| Basic and supplementary pension bands | Yes, through the ceiling | No | The bands are defined by reference to the prorated ceiling |
| Unified degressive general reduction | Yes | Provisionally | Computed on annual gross pay with the annual minimum-wage reference prorated to the employment period. Applied provisionally each month on year-to-date figures and reconciled definitively in December or in the final payslip. This is a cumulative recalculation, not a projection: it never estimates pay not yet received |
| 1.75 % allowance on the social levies | Yes | No | The allowance stops at four ceilings and follows the ceiling's own proration |
| Exemption limits for supplementary health, death-and-disability and pension cover | Yes | No | The annual-ceiling component of the limit is prorated to the employment period; the percentage-of-pay component follows actual pay |
| Exempt overtime pay, EUR 7,500 income tax cap | No | No | An annual per-employee cap. It is not prorated for a part-year employment and it is not shared between employers |
| Value-sharing bonus caps, EUR 3,000 and EUR 6,000 | No | No | Per calendar year, per employee, per employer. Not prorated |
| Severance exemption ceilings, 2, 6 and 10 PASS | No | No | Full annual multiples, whatever the length of service |
| Garnishment seizable fraction | No | No | Computed on the net actually paid in the month, against the annual scale bands converted to monthly equivalents. A short month simply produces a smaller fraction |
| Minimum wage test | Yes | No | Compared on the hours actually worked in the period |

Two counters must be maintained cumulatively even though nothing is projected, and both break on a provider migration if they are not carried across: exempt overtime pay against the EUR 7,500 cap, and exempt apprentice or intern pay against the annual minimum-wage threshold. They are covered in Module 2.3.
One proration rule that is easy to get wrong. The ceiling must be prorated by the same method used to prorate the salary — calendar days if the salary was prorated on calendar days, hours if on hours. Mixing the two produces a capped band that is wrong in every part-period payslip (Module 4.3).

#### If tax or contribution rates change mid-pay period, which rates apply?

The two systems answer differently, and 2026 contains a live example of each.

| Change | Governing rule | Effect |
|---|---|---|
| Social security rates and the ceiling | The rate in force for the period of employment the pay relates to | The ceiling changes on 1 January and nothing else moves during the year. A back-payment relating to 2025 uses the 2025 rates and the 2025 ceiling of EUR 3,925, whatever month it is paid in (Module 9.2) |
| Income tax default grid | The grid in force at the date of payment | The 2026 grid took effect on 1 May 2026. A payment made on 30 April uses the carried-over grid; one made on 4 May uses the new grid. There is no retrospective adjustment for January to April, and the two grids coexist inside one tax year |
| A transmitted withholding rate arriving mid-month | Applied from the next payslip | Never applied retrospectively to the current month |
| A transmitted rate expiring mid-month | Revert to the default grid once the validity period has passed | The rate must be date-checked on every run, not held as a static employee attribute |
| Minimum wage | Live value from its effective date | The 1 June 2026 increase to EUR 12.31 applies to hours worked from 1 June. A June payslip spanning the change tests the floor separately for each sub-period |
| The minimum-wage reference inside the general reduction | Frozen at EUR 12.02 for the whole of 2026 | Deliberately decoupled from the live minimum wage by Décret n° 2026-509 of 12 June 2026. An engine that reads one "current minimum wage" variable will overstate the relief from June onward |
| Industrial-accident rate | The rate notified for the calendar year, from 1 January | A mid-year rate change occurs only where the establishment's risk classification is corrected, and then applies from the date stated in the notification |

Where a contribution rate genuinely changes mid-month — which is rare and arises mainly from a change in the employer's headcount band or a change of establishment — the base is split in proportion to the days in each sub-period and each fraction bears its own rate.

#### How are tax and social security handled when an employee is paid multiple times in a single pay period?

France is a one-payslip-per-month country, and the correct answer to most multiple-payment questions is that there is only one pay period, however many transfers leave the bank.

| Situation | Treatment |
|---|---|
| Mid-month advance (acompte) | Not a pay event. It is a payment on account of the same month's single salary. No separate payslip, no separate DSN, no separate withholding. It is netted against the month's payslip. Configuring it as a second pay run is a common and expensive error (Module 1.2) |
| A supplementary payslip in the same month — a corrected run, a late bonus, a final settlement issued after the ordinary run | One monthly contribution base and one monthly ceiling entitlement. The two payments are summed, the bands re-sliced on the total, and the contributions already declared deducted. The ceiling is not doubled |
| Income tax, employee on a transmitted rate | The rate is a percentage and is frequency-neutral. It applies to each payment; the result is identical to applying it once to the total |
| Income tax, employee on the default grid | The grid must be read against the month's total net taxable amount, not against each payment separately. Reading it twice on two smaller amounts places both in lower bands and systematically under-withholds. Where the second payment follows a DSN already filed, the correct route is to band on the cumulative monthly figure and carry the difference in a withholding-regularisation block |
| Payments to an employee who has already left | Attached to the last period of employment for contributions; taxed in the month of payment; declared in that month's DSN with the contract still identified (Module 9.2) |
| Two contracts with the same employer in the same year | Since January 2022 the ceiling is not restarted contract by contract. The reconciliation runs from the start date of the first contract in the year (Module 5.2) |


#### How is payroll calculated if an employee's pay cycle changes mid-year?

A genuine change of cycle is unusual in France because Labour Code Article L3242-1 makes monthly payment the statutory norm. The realistic cases are a move between the monthly cycle and one of the more frequent cycles permitted by Article L3242-3 for home workers, seasonal, intermittent and temporary workers, or a change of pay date within the month.

| Aspect | Rule on a cycle change |
|---|---|
| The statutory constraint | The interval between two payments may not exceed one month. A cycle change must therefore not create a gap — moving a pay date later is constrained, moving it earlier is not |
| Social security ceiling | The annual reconciliation is unaffected. The periodic ceiling switches to the value published for the new period, and the cumulative reconciliation converges on the annual figure of EUR 48,060 regardless of how the year was sliced. The choice of periodicity changes cash flow across the year, not the total |
| The general reduction | Computed on annual gross pay. Unaffected in total; the monthly provisional figures simply follow the new rhythm |
| Income tax | The default grid version must change with the cycle — the tax administration publishes monthly, quarterly, weekly, daily and hourly grids and the version matching the period must be used. Applying the monthly grid to a weekly payment produces a 0 % rate on nearly every payslip. A transmitted personal rate needs no change, being frequency-neutral |
| DSN | Unchanged: one DSN per calendar month, whatever the pay cycle. The filing rhythm is set by headcount, not by pay frequency |
| Paid leave | The reference period runs to 31 May regardless and is unaffected |
| Practical recommendation | Where a client asks for a weekly cycle for ordinary employees, the correct configuration is a monthly cycle plus an advance, not a weekly cycle. Weekly payroll is not a recognised French cycle for ordinary employment |


### 11.2 Special Employee Groups & Income


#### How does taxation and social security differ for part-time employees and Board of Directors?

Part-time employees. Income tax is identical — the same withholding rate, the same default grid, no special treatment. Social security differs only through the base and one exemption.

| Dimension | Part-time treatment |
|---|---|
| Contribution rates | Identical to full-time. No reduced or graded rate exists |
| Social security ceiling | Prorated in the ratio of contractual hours to the full-time duration — 121.33 hours against 151.67 for an employee at 80 % gives a monthly ceiling of EUR 3,203.85 |
| Overtime | Does not exist. Part-timers work additional hours (heures complémentaires), capped at one tenth of the contractual duration or one third by agreement, premiumed at 10 % within the first tenth and 25 % beyond. Additional hours may never bring the employee to the full-time duration, on pain of reclassification |
| Unified degressive general reduction | Computed on actual annual pay, so a part-timer's lower pay produces a higher coefficient. This is arithmetically correct and needs no adjustment |
| Minimum wage | Applies pro rata to the contractual hours |
| Minimum weekly duration | 24 hours a week under Labour Code Article L3123-7, subject to the statutory derogations — a written request from the employee, a branch agreement, students under 26, and multi-employer arrangements |
| Compulsory health cover | The employee may be exempted on written request where their contribution would exceed 10 % of their pay — one of the few exemptions that exists specifically for part-timers |
| Paid leave | Accrues at the same 2.5 working days a month. Leave is not prorated by working time; a part-timer acquires the same 30 working days as a full-timer |

Board of directors. The determining test is the legal form of the company and the officer's shareholding, not the presence of a contract. The classification and the resulting contribution set are set out in full in Module 5.2; the operative points are:

| Position | Social security | Income tax |
|---|---|---|
| Chair or managing director of a simplified joint-stock company or a public limited company; minority or equal-shareholding manager of a private limited company | Treated as an employee. Full general-scheme and supplementary pension contributions on the officer's pay, except unemployment insurance and the wage guarantee scheme | Taxed as employment income under General Tax Code Article 80 ter, with withholding at source in the ordinary way |
| Majority-shareholding manager of a private limited company | Self-employed. Contributions assessed and paid personally under the self-employed scheme, outside payroll entirely | Employment-income category, but no employer withholding: the individual pays instalments directly to the tax administration |
| Board member with a genuine and distinct employment contract alongside the office | Employee for the contract, including unemployment insurance on the employment pay; officer rules for the officer's pay | Both taxed as employment income |
| Attendance fees (jetons de présence) | Outside social security contributions and outside the gross-to-net chain. The company owes a 20 % flat social contribution on fees paid to non-executive directors | Taxed as investment income, not employment income: a flat levy of 12.8 % income tax plus capital social levies at 18.6 % for 2026, unless the recipient elects the progressive scale. No withholding at source applies |

The exclusion from unemployment insurance is a genuine payroll rule and a frequent client query: an officer treated as an employee does not contribute and correspondingly acquires no unemployment entitlement, whatever the company would prefer to arrange.

#### How is taxation handled for employees with multiple employers?

The two systems again diverge, and in opposite directions: social security coordinates between employers, income tax does not.
Social security. Each employer applies the ceiling prorated in the ratio of the pay it pays to the employee's total pay from all employers:
Ceiling applied by employer A
=  monthly ceiling  ×  pay from employer A
-----------------------------
total pay from all employers
The employee is obliged to tell each employer, at the end of each month or quarter, the total remuneration received across all of them. Where the employee does not do so, the employer applies the ceiling as though the employee were part-time, on its own contractual hours. Because each employer applies the ceiling independently, the aggregate can exceed the true entitlement, and a regularisation then restores the correct level — either between the employers and the collecting body, or through a claim by the employee.
Income tax. There is no coordination and none is needed, because the withholding is not progressive for a resident:

| Case | Treatment |
|---|---|
| Employee on a transmitted personal rate | The same rate is transmitted to every employer. Each applies it to its own net taxable amount. Because the rate is a flat percentage derived from the whole household's income, the sum of the withholdings is correct without any employer knowing about the others |
| Employee on the default grid | Each employer reads the grid against its own payment only. Two employers each paying EUR 1,500 will both read a low band, and the employee will be materially under-withheld across the year. This is a structural feature, corrected at the annual assessment — and the strongest practical reason for a multi-employer employee to have a personal rate transmitted |
| Non-resident with two French employers | Each applies the Article 182 A scale to its own payment, so the progressive bands are each used twice. The under-withholding is corrected on assessment, where the liberatory character of the lower bands is re-tested on the total |

Working time is the third dimension and is not a payroll calculation but a compliance risk the employer must manage: the statutory maximum daily and weekly durations apply to the employee's total work across all employers, and an employer that knowingly allows the maxima to be exceeded is liable.

#### What is the treatment of foreign-sourced employment income for residents?

A French tax resident is taxable on worldwide employment income (General Tax Code Article 4 A). Three mechanisms may then remove all or part of it from the French base, and only two of them touch payroll.

| Mechanism | Level | Effect on payroll |
|---|---|---|
| Double tax treaty | Assessment, and payroll where the employer knows of it | Where a treaty allocates the taxing right to the other state, the income is either exempt in France with progression, or taxed with a credit. Where the income is exempt, it is outside the net taxable amount and bears no withholding |
| Total exemption for employees posted abroad (General Tax Code Article 81 A, I) | Payroll — the exempt pay is excluded from the net taxable amount | Available where the employer is established in France, the European Union or the European Economic Area, and the employee either paid foreign tax of at least two thirds of the French tax that would have been due, or worked abroad for more than 183 days in 12 consecutive months on construction and installation sites, on the prospecting or exploitation of natural resources, or at sea — or more than 120 days on commercial prospecting |
| Partial exemption of expatriation supplements (General Tax Code Article 81 A, II) | Payroll | Supplements paid for stays abroad are exempt where they are fixed before the assignment, relate to it, and do not exceed 40 % of the remuneration that would have been paid without them |

Two points close the picture. Exempt amounts under Article 81 A are still taken into account to set the effective rate on the employee's remaining income (General Tax Code Article 197 C), which is an assessment-level mechanism the employer neither computes nor reports. And cross-border workers are expressly outside Article 81 A — an employee living in France and commuting daily to Germany, Belgium, Luxembourg or Switzerland is governed by the relevant treaty's frontier-worker article, not by the posting exemption.
Social security is decided separately and by a different test. A French resident working abroad remains in the French scheme only for the duration permitted by the applicable coordination instrument, evidenced by a portable document A1 or its equivalent; beyond that they leave the French compulsory scheme entirely, whatever their tax position (Module 5.1).

#### How do employer stock option plans work and how are they taxed?

France operates two distinct equity vehicles, and neither is withheld through payroll. That is the single most important configuration point: share-based gains carry no withholding at source, and an engine that tries to withhold on them is wrong.

| Vehicle | Mechanism |
|---|---|
| Free share awards (attributions gratuites d'actions) | Shares awarded at no cost, definitively acquired at the end of a vesting period of at least one year, sometimes followed by a holding period |
| Share options (options sur titres, commonly "stock options") | A right to subscribe or purchase shares at a fixed price, exercised after a vesting period |

The employer's obligations are contribution obligations, not withholding obligations:

| Obligation | Content |
|---|---|
| Employer specific contribution | 30 %, raised from 20 % with effect for shares acquired from 1 March 2025, under Social Security Code Article L137-13. For free share awards the base is the value of the shares at the acquisition date; for share options it is the value of the options at grant. Payable in the month following the acquisition or the grant, and declared in the DSN |
| Exemption for smaller employers | Small and medium-sized enterprises and mid-caps that have never distributed a dividend since incorporation are exempt from the employer contribution, within a limit of one annual ceiling per employee — EUR 48,060 for 2026 |
| Ordinary social security contributions | Not due. The gains are outside the ordinary contribution base (Social Security Code Article L137-13); they never enter the capped or uncapped bands |
| Withholding at source | None. The gains are outside the scope of withholding at source and are settled by the employee through the annual assessment |
| Reporting | The award and the gain are reported by the employer, and the employee receives an individual statement enabling them to complete their return |

The employee's position, taxed in the year the shares are disposed of, not the year they are acquired:

| Gain | Income tax | Social levies | Employee specific contribution |
|---|---|---|---|
| Free share acquisition gain, fraction up to EUR 300,000 | Progressive scale after a 50 % allowance | Capital social levies at 18.6 % for 2026, raised from 17.2 % by the Social Security Financing Act for 2026 | None |
| Free share acquisition gain, fraction above EUR 300,000 | Progressive scale, taxed as employment income with no allowance | Activity social levies at 9.70 % | 10 % under Social Security Code Article L137-14 |
| Share option exercise gain, options granted from 28 September 2012 | Progressive scale, taxed as employment income | Activity social levies at 9.70 % | 10 % under Social Security Code Article L137-14 |
| Disposal gain (sale price less value at acquisition or exercise) | Capital gains regime | Capital social levies at 18.6 % | None |

Two consequences follow for the client conversation. The 10 % employee contribution creates a data dependency the employer does not naturally have: it becomes due when the employee disposes of the shares, an event payroll does not observe. Where a client operates plans that can generate gains above EUR 300,000, the flow of disposal information from the plan administrator to payroll must be designed explicitly rather than assumed. And the 30 % employer contribution is a real and often unbudgeted cost — for a plan awarding EUR 1,000,000 of shares it is EUR 300,000, payable at acquisition, years before the employee sells anything and irrespective of whether the shares later prove worthless.

#### How is payroll handled for employees who transfer between different legal entities mid-year?

Everything turns on whether the transfer falls under Labour Code Article L1224-1, and the two answers are opposites.
Case A — a transfer of undertaking within Article L1224-1 (sale, merger, contribution of a business, incorporation of a business, succession). The employment contracts subsist automatically with the new employer. There is no termination, no final settlement, no new hire.

| Element | Treatment |
|---|---|
| Employment contract | Continues unchanged, with all its terms |
| Length of service | Preserved in full, and carries into severance and notice calculations |
| Paid leave balance | Transfers; the old employer pays no compensatory leave indemnity |
| Social security ceiling and the annual reconciliation | Continue. The new employer must regularise at the year end as though it had been the employer since 1 January, on the total pay received by the transferred employee across the whole year. It applies the full annual ceiling, not a reduced one, because there has been no departure or hire to justify a reduced ceiling |
| Unified degressive general reduction | Likewise computed on the whole year's pay |
| Year-to-date counters | Must be migrated: capped and uncapped bases, the general reduction, the four-ceiling allowance cap, exempt overtime against the EUR 7,500 cap, net taxable pay and tax withheld |
| Pre-hire declaration | Not required — there is no hire |
| Withholding rate | Follows the employee's social security number, but the new employer's first DSN precedes the first return flow, so the default grid applies for one month before the personal rate arrives. This is unavoidable and should be explained to transferred employees in advance |

The obligation on the receiving employer to reconcile the whole year is the point most often missed, and it fails in a specific way: the new employer restarts the ceiling at zero from the transfer date, the employee's capped base is understated across the year, and the shortfall surfaces on inspection or in the employee's pension record.
Case B — a move between group companies that is not an Article L1224-1 transfer, typically a resignation from one entity and a new contract with another. This is two employment relationships and everything restarts.

| Element | Treatment |
|---|---|
| Old entity | Full final settlement: notice, compensatory leave indemnity, end-of-contract documents, DSN end-of-contract event signal |
| New entity | Pre-hire declaration, new contract, ceiling and reduction counters from zero |
| Length of service | Statutorily restarts. It may be recognised contractually for severance and notice, and usually is in a group transfer agreement, but the statutory counters do not follow |
| Consequence | Because both entities apply a full ceiling for the overlapping months, contributions are over-collected relative to a continuous employment. This is a known and lawful outcome of the structure, not an error to be corrected |

The distinction is a legal characterisation, not a payroll one, and it must be settled by the client's employment counsel before configuration. It changes the final settlement, the DSN, the leave payout and the year's contribution total.

#### What is the process for an employee who changes citizenship or residency status during the fiscal year?

Citizenship: no effect whatsoever. French payroll turns on tax residence and on the place where work is performed. It does not turn on nationality, and there is no payroll field, rate, threshold or filing that varies with it. The only adjacent obligations are immigration ones — the right to work and the residence permit — which are compliance matters for the employer but do not enter any calculation. A client asking to model nationality-driven payroll rules should be told there are none.
Residency: a genuine mid-year switch, and one of the more error-prone events in French payroll.

| Step | What happens |
|---|---|
| 1. The change of tax residence | Occurs on a date, not at a year boundary. The year is split: the employee is taxed as a resident on worldwide income for the resident part, and as a non-resident on French-source income for the rest (General Tax Code Article 166) |
| 2. Evidence | The employer needs the effective date and evidence of the change. It cannot decide the question itself, and it should not: residence is determined by Article 4 B as modified by any treaty, and a treaty tie-breaker can reverse an apparently obvious answer |
| 3. Switching the withholding mechanism | From the effective date, the employer switches between withholding at source and the specific non-resident withholding of Article 182 A, or the reverse. These are different mechanisms with different bases, not two rates of one mechanism — the non-resident base carries a 10 % flat professional-expense deduction and is sliced progressively, the resident base carries neither |
| 4. Informing the tax administration | The employee must report the change. The administration then ceases or begins transmitting a personal rate. Until it does, the employer applies the default grid on becoming resident, and the Article 182 A scale on becoming non-resident |
| 5. Cumulative counters | The year-to-date net taxable amount and tax withheld continue for the calendar year; they are not restarted at the residence change |
| 6. Social security | Decided separately and usually does not change. Affiliation follows the place where the work is physically performed. An employee who moves house across a border but continues working in France stays fully in the French scheme; an employee who starts working abroad may leave it even though their tax residence has not moved |
| 7. DSN | The contract is not closed and not reopened. The residence status and the withholding arrangements change within the existing contract |

The failure to separate steps 3 and 6 is the recurring error. Tax residence and social security affiliation are independent tests decided by independent criteria, and an employee can change one without changing the other (Module 2.2).

#### Are there specific rules for expatriates or inpatriates?

Yes, and they are separate regimes running in opposite directions. Both are set out here because clients routinely use the two words interchangeably.
Inbound assignees — the impatriate regime (General Tax Code Article 155 B). This is one of the few tax reliefs in France that is a payroll item: it reduces the net taxable amount and therefore the withholding, month by month.

| Aspect | Content |
|---|---|
| Who qualifies | Employees, and directors treated as employees under General Tax Code Article 80 ter, who were not French tax resident in the five calendar years preceding the year they take up duties, and who are recruited from abroad by a French entity or transferred within a group. Self-employed workers and majority-shareholding managers of a private limited company are excluded |
| Impatriation premium | Exempt either at its real amount, where the contract fixes it or makes it objectively determinable, or — at the employee's annual election — at a flat 30 % of total net remuneration. The flat option needs no contractual clause and is the practical default for a recruit hired directly from abroad |
| Foreign workdays | The portion of pay relating to duties performed outside France is additionally exempt |
| Overall cap, elected annually | Either the total exemption is capped at 50 % of total remuneration, or the foreign-workday exemption alone is capped at 20 % of the remuneration taxable after the premium exemption. The first suits employees who travel heavily; the second suits employees with a large premium and little travel |
| Duration | Until 31 December of the eighth calendar year following the year duties are taken up. Taking up duties in 2026 therefore runs the regime to 31 December 2034. Not renewable |
| Social security | Contributions to a foreign supplementary pension scheme the employee belonged to before arriving in France are deductible in France for the life of the regime. Separately, and by a different route, an inbound assignee who remains affiliated abroad under a coordination instrument pays no French contributions at all while their portable document A1 is valid |
| Assessment-level extras | A 50 % exemption on certain foreign passive income, and a partial wealth-tax exemption for five years. Neither is a payroll item and neither may be modelled in the engine |

Configuration consequence: the impatriation premium must be a separately identified pay component with its own exemption logic, an annual election flag for the flat-versus-real choice and for the cap choice, and an end date computed as year of arrival plus eight. It cannot be handled as a generic allowance.
Outbound assignees — employees posted abroad by a French employer. The applicable relief is Article 81 A, described in the foreign-source income answer above: total exemption on a day-count or foreign-tax test, or partial exemption of expatriation supplements within 40 %. It too reduces the net taxable amount in payroll.
Posted workers coming into France under a foreign contract are a third category and are largely outside payroll scope: the foreign employer pays them, they hold a portable document A1 so no French contributions are due, and their French tax position follows the treaty. What the receiving entity must do is real but administrative — the posting must be declared on the Ministry of Labour's online platform before it begins, and the core French labour standards (minimum wage, working time, paid leave, health and safety) apply to the posted worker for the duration.
Legal basis: General Tax Code, Articles 4 A, 4 B, 80 ter, 81 A, 155 B, 166, 182 A, 197 C, 204 A to 204 N; Social Security Code, Articles L130-1, L137-13, L137-14, L241-13, L242-1, R242-2, D242-1; Labour Code, Articles L1224-1 to L1224-4, L3121-18 to L3121-22, L3123-1 and following, L3123-7, L3123-28 to L3123-31, L3242-1, L3242-3, L1262-1 to L1262-4; EU Regulation (EC) No 883/2004; Décret n° 2026-509 of 12 June 2026 (frozen minimum-wage reference for the general reduction); Act n° 2025-1403 of 30 December 2025 (capital social levies at 18.6 %); Official Tax Bulletin BOI-RSA-GEO-10 (employees posted abroad) and the impatriate-regime guidance of 11 August 2025.

## Module 12: Gross-to-Net Worked Examples


### 12.1 Comprehensive Gross-to-Net Examples

Every example below uses the 2026 parameters established in Modules 4, 5 and 6: monthly social security ceiling EUR 4,005; annual ceiling EUR 48,060; minimum wage EUR 12.02 an hour to 31 May and EUR 12.31 from 1 June; frozen annual minimum-wage reference for the general reduction EUR 21,876.40. Rates for the industrial-accident contribution and the mobility levy are establishment-specific; the illustrative values used here are stated in each example's facts and must be replaced with the client's own.
Each example produces the three distinct net figures a French payslip must carry — net payable before income tax, net social amount and net taxable amount — because they are never equal and a payslip showing only one of them is non-compliant.

#### Deliverable: Example 1 — A full-time resident employee on a standard salary

Facts. Non-managerial employee, permanent contract, full-time 35-hour week (151.67 hours). Gross salary EUR 2,800.00 a month. Employer has 30 employees, so the housing-fund contribution is 0.10 % on the capped band and the training contribution is 1.00 %. Industrial-accident net rate 2.08 %; mobility levy 2.00 %. Compulsory health cover: EUR 30.00 employee, EUR 30.00 employer. June 2026 payroll. No withholding rate transmitted, so the default grid applies; June falls after 1 May, so the 2026 grid is used.
Employee calculation

| Line | Base | Rate | Amount |
|---|---|---|---|
| Gross pay | — | — | 2,800.00 |
| Old-age, capped | 2,800.00 (below the EUR 4,005 ceiling) | 6.90 % | −193.20 |
| Old-age, uncapped | 2,800.00 | 0.40 % | −11.20 |
| Supplementary pension, band 1 | 2,800.00 | 3.15 % | −88.20 |
| General balance contribution, band 1 | 2,800.00 | 0.86 % | −24.08 |
| Employee health-cover share | — | — | −30.00 |
| Social levies base | (2,800.00 × 98.25 % = 2,751.00) + 30.00 employer share | — | 2,781.00 |
| General social contribution, deductible | 2,781.00 | 6.80 % | −189.11 |
| General social contribution, non-deductible | 2,781.00 | 2.40 % | −66.74 |
| Social debt repayment contribution | 2,781.00 | 0.50 % | −13.91 |
| Total employee contributions |  |  | −616.44 |
| Net payable before income tax | 2,800.00 − 616.44 |  | 2,183.56 |
| Net social amount | 2,800.00 + 30.00 − 616.44 |  | 2,213.56 |
| Net taxable amount | 2,183.56 + 66.74 + 13.91 + 30.00 |  | 2,294.21 |
| Default grid, 2026 metropolitan | Band EUR 2,170 – 2,314.99 | 4.10 % | — |
| Income tax withheld | 2,294.21 × 4.10 % |  | −94.06 |
| NET PAID | 2,183.56 − 94.06 |  | EUR 2,089.50 |

Employer calculation

| Contribution | Base | Rate | Amount |
|---|---|---|---|
| Health, maternity, disability, death | 2,800.00 | 13.00 % | 364.00 |
| Old-age, capped | 2,800.00 | 8.55 % | 239.40 |
| Old-age, uncapped | 2,800.00 | 2.11 % | 59.08 |
| Family allowances | 2,800.00 | 5.25 % | 147.00 |
| Industrial accidents | 2,800.00 | 2.08 % | 58.24 |
| Autonomy solidarity | 2,800.00 | 0.30 % | 8.40 |
| Housing fund, under 50 employees | 2,800.00 capped band | 0.10 % | 2.80 |
| Supplementary pension, band 1 | 2,800.00 | 4.72 % | 132.16 |
| General balance contribution, band 1 | 2,800.00 | 1.29 % | 36.12 |
| Unemployment insurance | 2,800.00 | 4.00 % | 112.00 |
| Wage guarantee scheme | 2,800.00 | 0.25 % | 7.00 |
| Social dialogue | 2,800.00 | 0.016 % | 0.45 |
| Mobility levy | 2,800.00 | 2.00 % | 56.00 |
| Training contribution | 2,800.00 | 1.00 % | 28.00 |
| Apprenticeship tax | 2,800.00 | 0.68 % | 19.04 |
| Employer health-cover share | — | — | 30.00 |
| Total employer contributions before relief |  |  | 1,299.69 |

The unified degressive general reduction

| Step | Calculation | Result |
|---|---|---|
| Annual gross pay | 2,800.00 × 12 | EUR 33,600.00 |
| Below the eligibility threshold? | 33,600.00 against 3 × 21,876.40 = 65,629.20 | Yes — eligible |
| Inner term | (3 × 21,876.40 ÷ 33,600.00) − 1 = 0.953250 | — |
| Half it | × 0.5 | 0.476625 |
| Raise to the power 1.75 | 0.476625 ^ 1.75 | 0.273726 |
| Apply Tdelta (housing fund at 0.10 %) | × 0.3781 | 0.103500 |
| Add Tmin | + 0.0200, rounded to 4 decimals | C = 0.1234 |
| Annual reduction | 33,600.00 × 0.1234 | EUR 4,146.24 |
| Monthly provisional reduction | ÷ 12 | EUR 345.52 |


| Result | Amount |
|---|---|
| Employer contributions before relief | 1,299.69 |
| Less the general reduction | −345.52 |
| Employer contributions payable | 954.17 |
| Total cost of employment | 2,800.00 + 954.17 = EUR 3,754.17 |

Reconciliation. Gross 2,800.00 = net paid 2,089.50 + employee contributions 616.44 + income tax 94.06. The employer bears a further 954.17, so EUR 3,754.17 of employer cost delivers EUR 2,089.50 to the employee — a wedge of 44.3 %.

#### Deliverable: Example 2 — A casual or part-time employee

Facts. Part-time employee at 80 % — 121.33 contractual hours against 151.67 — paid at the minimum wage of EUR 12.31 an hour from 1 June 2026. Employer has 30 employees. Industrial-accident net rate 2.08 %; mobility levy not applicable (no transport authority rate). Health cover EUR 20.00 each way. July 2026 payroll, no withholding rate transmitted.

| Line | Base | Rate | Amount |
|---|---|---|---|
| Gross pay | 121.33 hours × EUR 12.31 | — | 1,493.57 |
| Prorated monthly ceiling | 4,005.00 × 121.33 ÷ 151.67 | — | 3,203.84 |
| Old-age, capped | 1,493.57 (below the prorated ceiling) | 6.90 % | −103.06 |
| Old-age, uncapped | 1,493.57 | 0.40 % | −5.97 |
| Supplementary pension, band 1 | 1,493.57 | 3.15 % | −47.05 |
| General balance contribution, band 1 | 1,493.57 | 0.86 % | −12.84 |
| Employee health-cover share | — | — | −20.00 |
| Social levies base | (1,493.57 × 98.25 % = 1,467.43) + 20.00 | — | 1,487.43 |
| General social contribution, deductible | 1,487.43 | 6.80 % | −101.15 |
| General social contribution, non-deductible | 1,487.43 | 2.40 % | −35.70 |
| Social debt repayment contribution | 1,487.43 | 0.50 % | −7.44 |
| Total employee contributions |  |  | −333.21 |
| Net payable before income tax |  |  | 1,160.36 |
| Net social amount | 1,493.57 + 20.00 − 333.21 |  | 1,180.36 |
| Net taxable amount | 1,160.36 + 35.70 + 7.44 + 20.00 |  | 1,223.50 |
| Default grid, 2026 | Below EUR 1,635 | 0 % | — |
| Income tax withheld | — |  | 0.00 |
| NET PAID |  |  | EUR 1,160.36 |

The general reduction reaches its ceiling. Annual gross is 1,493.57 × 12 = EUR 17,922.84, below the annual minimum-wage reference itself, so the formula returns a coefficient above the maximum and the maximum applies:

| Step | Result |
|---|---|
| Inner term: (3 × 21,876.40 ÷ 17,922.84) − 1 | 2.661733 |
| × 0.5, then ^ 1.75 | 1.643726 |
| × 0.3781, + 0.0200 | 0.641493 |
| Capped at Tmin + Tdelta | C = 0.3981 |
| Annual reduction: 17,922.84 × 0.3981 | EUR 7,135.09 |
| Monthly provisional reduction | EUR 594.59 |

The employer contributions the reduction may be set against — health, capped and uncapped old-age, family allowances, the housing fund, autonomy solidarity, the supplementary pension and general balance contributions, unemployment, social dialogue and a fixed 0.49 points of the industrial-accident contribution — total EUR 594.82 for this month. The reduction of EUR 594.59 therefore absorbs all but 23 cents of them.

| Employer position | Amount |
|---|---|
| Contributions the reduction may be set against | 594.82 |
| Contributions it may not be set against — the remaining 1.59 points of the industrial-accident rate (23.75), the wage guarantee scheme (3.73), training (14.94), the apprenticeship tax (10.16), the health-cover share (20.00) | 72.58 |
| Total before relief | 667.40 |
| Less the general reduction | −594.59 |
| Employer contributions payable | 72.81 |
| Total cost of employment | EUR 1,566.38 |

This is the intended shape of the 2026 reform: at the minimum wage the relief is calibrated to cancel almost the whole of the imputable employer contribution set, and the residual employer cost is 4.9 % of gross rather than the 40 % of Example 1.
Two configuration points. The reduction may never exceed the contributions it is imputed against, so the engine must compute the imputable set and cap against it — a coefficient alone is not enough. And a 0 % withholding is not "no withholding": the employee is still declared, the net taxable amount is still reported, and a rate transmitted later must be applied from the next payslip.

#### Deliverable: Example 3 — An employee with a pre-tax deduction

Facts. Non-managerial employee, gross salary EUR 4,500.00 a month, above the EUR 4,005 ceiling. The employer operates an obligatory company retirement plan covering all non-managerial staff: employer 4 % of gross, employee 2 % of gross. Health cover EUR 35.00 each way. Employer has 30 employees; industrial-accident rate 2.08 %; mobility levy 2.00 %. Transmitted personal withholding rate 9.90 %. October 2026 payroll.
The two limits must be tested before anything else, and they are different figures under different texts.

| Test | Rule | Calculation | Result |
|---|---|---|---|
| Income tax deductibility of the employee's own contribution (General Tax Code Article 83, 2°) | 8 % of gross annual pay, itself capped at 8 annual ceilings | 8 % × 54,000.00 = EUR 4,320.00 a year; employee and employer contributions together are 270.00 × 12 = EUR 3,240.00 | Within the limit — fully deductible |
| Exemption from social security contributions (Social Security Code Article D242-1) | The higher of 5 % of the annual ceiling, or 5 % of pay capped at 5 annual ceilings | max(5 % × 48,060.00 = 2,403.00 ; 5 % × 54,000.00 = 2,700.00) = EUR 2,700.00 a year; employer contribution is 180.00 × 12 = EUR 2,160.00 | Within the limit — exempt from contributions |


| Line | Base | Rate | Amount |
|---|---|---|---|
| Gross pay | — | — | 4,500.00 |
| Band 1 / capped band | up to the ceiling | — | 4,005.00 |
| Band 2 | 4,500.00 − 4,005.00 | — | 495.00 |
| Old-age, capped | 4,005.00 | 6.90 % | −276.35 |
| Old-age, uncapped | 4,500.00 | 0.40 % | −18.00 |
| Supplementary pension, band 1 | 4,005.00 | 3.15 % | −126.16 |
| Supplementary pension, band 2 | 495.00 | 8.64 % | −42.77 |
| General balance contribution, band 1 | 4,005.00 | 0.86 % | −34.44 |
| General balance contribution, band 2 | 495.00 | 1.08 % | −5.35 |
| Technical balance contribution | 4,500.00 — due, pay exceeds the ceiling | 0.14 % | −6.30 |
| Employee health-cover share | — | — | −35.00 |
| Employee retirement-plan contribution — the pre-tax deduction | 4,500.00 | 2.00 % | −90.00 |
| Social levies base | (4,500.00 × 98.25 % = 4,421.25) + 35.00 health + 180.00 employer retirement contribution | — | 4,636.25 |
| General social contribution, deductible | 4,636.25 | 6.80 % | −315.27 |
| General social contribution, non-deductible | 4,636.25 | 2.40 % | −111.27 |
| Social debt repayment contribution | 4,636.25 | 0.50 % | −23.18 |
| Total employee contributions |  |  | −1,084.09 |
| Net payable before income tax |  |  | 3,415.91 |
| Net social amount | 4,500.00 + 35.00 + 180.00 − 1,084.09 |  | 3,630.91 |
| Net taxable amount | 3,415.91 + 111.27 + 23.18 + 35.00. The employer retirement contribution is not added — it is exempt for income tax within the Article 83 limit, unlike the health-cover contribution |  | 3,585.36 |
| Income tax withheld | 3,585.36 × 9.90 % |  | −354.95 |
| NET PAID | 3,415.91 − 354.95 |  | EUR 3,060.96 |

Employer position

| Item | Amount |
|---|---|
| Contributions before relief, including the employer retirement contribution of 180.00 and the 20 % social lump-sum levy on it of 36.00 | 2,120.58 |
| General reduction: annual gross 54,000.00, coefficient C = 0.0277, annual relief 1,495.80 | −124.65 |
| Employer contributions payable | 1,995.93 |
| Total cost of employment | EUR 6,495.93 |

Three things this example is designed to show.
1. The employer's retirement contribution behaves differently in all three systems at once. It is exempt from social security contributions within the Article D242-1 limit; it is inside the social levies base at 100 % with no allowance; and it is outside the net taxable amount within the Article 83 limit. Compare the health-cover contribution, which is exempt from contributions, inside the levies base and inside the net taxable amount. Two employer benefit contributions, two different answers.
1. The two limits are different numbers under different texts — EUR 4,320 for tax, EUR 2,700 for contributions, on the same plan. Testing one and assuming the other is the standard failure here.
1. The general reduction is nearly exhausted at this salary. At EUR 54,000 a year the coefficient has fallen to 0.0277, only 0.0077 above its floor of Tmin. A further EUR 11,629 of annual pay would take the employee past EUR 65,629.20 and the relief would drop to nil in a single step.

#### Deliverable: Example 4 — An employee with a student loan or other special tax obligation

Not Applicable as framed — France has no student loan repayment deducted through payroll. Higher education is publicly funded and there is no income-contingent repayment scheme, no employer collection obligation and no payroll deduction code for one. Any client requirement referring to a student loan deduction for France is an error in the requirement and should be raised rather than configured.
The nearest French equivalent — a compulsory, court-backed deduction the employer must operate on pain of personal liability — is a wage attachment, and it is worked below. This example deliberately combines the two instruments that behave differently, because a single-order example conceals the rule that matters.
Facts. An employee's net pay, after social contributions and after the income tax withheld, is EUR 1,450.00 for the month. No dependants. The employer holds two instruments: a maintenance order enforced by direct payment for EUR 500.00 a month, and an ordinary wage attachment for a consumer debt of EUR 4,200.00.
Step 1 — compute the seizable fraction. The 2026 scale is applied in slices, not by reading one fraction from the band containing total pay.

| Slice of monthly net | Width | Fraction | Seizable |
|---|---|---|---|
| Up to EUR 373.33 | 373.33 | 1/20 | 18.67 |
| EUR 373.34 to 727.50 | 354.17 | 1/10 | 35.42 |
| EUR 727.51 to 1,083.33 | 355.83 | 1/5 | 71.17 |
| EUR 1,083.34 to 1,435.83 | 352.50 | 1/4 | 88.13 |
| EUR 1,435.84 to 1,450.00 | 14.17 | 1/3 | 4.72 |
| Total seizable fraction |  |  | EUR 218.11 |

Reading a single fraction from the band containing EUR 1,450.00 would give 1,450.00 × 1/3 = EUR 483.33 — more than double the lawful amount, and an over-deduction for which the employer is personally liable to the employee.
Step 2 — apply the priority order.

| Rank | Claim | Available to it | Paid |
|---|---|---|---|
| 1 | The absolutely protected amount reserved to the employee — the active-solidarity income for a single person | — | EUR 651.69 is untouchable |
| 2 | Maintenance order by direct payment — payable from the whole salary above the protected amount, not confined to the seizable fraction, and ranking ahead of every other creditor | 1,450.00 − 651.69 = 798.31 | EUR 500.00 in full |
| 3 | Tax levies | None outstanding | — |
| 4 | Ordinary wage attachment — confined to the seizable fraction of EUR 218.11, which the maintenance order has already absorbed in its entirety | 218.11 − 500.00 → nil | EUR 0.00 this month |
| 5 | The employer's own claims | None | — |

Step 3 — the payslip result.

| Line | Amount |
|---|---|
| Net after contributions and income tax | 1,450.00 |
| Maintenance order paid to the creditor's enforcement officer | −500.00 |
| Ordinary attachment paid to the distributing enforcement officer | −0.00 |
| Amount paid to the employee | EUR 950.00 |
| Check against the protected amount | 950.00 exceeds EUR 651.69 — compliant |

What the employer must do beyond the arithmetic. Respond to the record of attachment within fifteen days; pay the seizable fraction monthly to the distributing enforcement officer, never directly to individual creditors and never apportioned by the employer itself; and notify the enforcement officer if the employee leaves, giving the new employer's details if known. The consumer debt is not written off — it simply cannot be recovered faster than the scale allows, and it will begin to be paid in any month in which the maintenance claim falls below the seizable fraction, or in which pay rises.

#### Deliverable: Example 5 — Other complex scenarios that are common in the country: a managerial employee above the ceiling with a company vehicle

Facts. Managerial-grade employee on a 35-hour week (not a day-count arrangement). Base salary EUR 6,000.00 a month. A company vehicle is made available; its statutory flat benefit value is EUR 500.00 a month (Module 4.2). Employer has 60 employees, so the housing-fund contribution is 0.50 % on total pay and the general-reduction parameter Tdelta is 0.3821. Industrial-accident rate 2.08 %; mobility levy 2.00 %. Health cover EUR 45.00 each way. Transmitted personal withholding rate 15.80 %. May 2026 payroll.

| Line | Base | Rate | Amount |
|---|---|---|---|
| Base salary | — | — | 6,000.00 |
| Company vehicle benefit in kind | Statutory flat value | — | 500.00 |
| Gross pay |  |  | 6,500.00 |
| Band 1 / capped band | — | — | 4,005.00 |
| Band 2 | 6,500.00 − 4,005.00 | — | 2,495.00 |
| Old-age, capped | 4,005.00 | 6.90 % | −276.35 |
| Old-age, uncapped | 6,500.00 | 0.40 % | −26.00 |
| Supplementary pension, band 1 | 4,005.00 | 3.15 % | −126.16 |
| Supplementary pension, band 2 | 2,495.00 | 8.64 % | −215.57 |
| General balance contribution, band 1 | 4,005.00 | 0.86 % | −34.44 |
| General balance contribution, band 2 | 2,495.00 | 1.08 % | −26.95 |
| Technical balance contribution | 6,500.00 | 0.14 % | −9.10 |
| Executive employment association | 6,500.00, managerial grade only | 0.024 % | −1.56 |
| Employee health-cover share | — | — | −45.00 |
| Social levies base | (6,500.00 × 98.25 % = 6,386.25) + 45.00 | — | 6,431.25 |
| General social contribution, deductible | 6,431.25 | 6.80 % | −437.33 |
| General social contribution, non-deductible | 6,431.25 | 2.40 % | −154.35 |
| Social debt repayment contribution | 6,431.25 | 0.50 % | −32.16 |
| Total employee contributions |  |  | −1,384.97 |
| Net payable before income tax | 6,500.00 − 1,384.97 |  | 5,115.03 |
| Net social amount | 6,500.00 + 45.00 − 1,384.97 |  | 5,160.03 |
| Net taxable amount | 5,115.03 + 154.35 + 32.16 + 45.00 |  | 5,346.54 |
| Income tax withheld | 5,346.54 × 15.80 % |  | −844.75 |
| Deduction of the benefit in kind | The vehicle was added to gross to be contributed and taxed; it is now removed, because the employee received a car and not EUR 500.00 in cash |  | −500.00 |
| NET PAID | 5,115.03 − 844.75 − 500.00 |  | EUR 3,770.28 |

Employer position

| Item | Amount |
|---|---|
| Total employer contributions, including the managerial-grade death-and-disability contribution of 1.50 % on the capped band (EUR 60.08), the executive employment association contribution at 0.036 % and the housing fund at 0.50 % on total pay | 3,094.81 |
| General reduction — annual gross 6,500.00 × 12 = EUR 78,000.00, above the eligibility threshold of EUR 65,629.20 | 0.00 |
| Employer contributions payable | 3,094.81 |
| Total cost of employment | EUR 9,594.81 |

Four points this example carries.
1. The benefit in kind is added and then removed. It enters gross so that it bears contributions and income tax, and is deducted after them so that net pay falls only by the employee's contributions and tax on it — here about EUR 213. A system that simply adds EUR 500.00 to net over-pays the employee; one that omits it from gross under-contributes and under-withholds.
1. Three contributions appear that never appear below the ceiling — supplementary pension band 2, the technical balance contribution and, on the employer side, the managerial death-and-disability contribution. The technical balance contribution is due only for employees whose pay exceeds one ceiling, so it switches on and off with pay.
1. The general reduction is nil, not small. At EUR 78,000 a year the employee is past the eligibility threshold and the relief is zero. Compare Example 3 at EUR 54,000, where it was still EUR 124.65 a month, and note the two-percentage-point cliff described in Module 5.2.
1. The managerial grade is a configuration key, not a job title. It is fixed by the collective agreement's classification level, and it drives the 1.50 % employer death-and-disability contribution, the executive employment association contribution both ways, and in most agreements a longer notice period.

#### Deliverable: Example 6 — Other complex scenarios that are common in the country: an Alsace-Moselle employee with overtime

Facts. Non-managerial employee working at an establishment in Moselle, so the additional local health contribution of 1.30 % applies — triggered by the place of work, not by the employee's residence. Base salary EUR 2,600.00 for the contractual 151.67 hours. Eight overtime hours are worked in the month, all within the first eight beyond 35 in their weeks, so the 25 % premium applies. Employer has 15 employees, so the employer flat overtime deduction is EUR 1.50 an hour and the housing-fund contribution is 0.10 % on the capped band. Industrial-accident rate 2.08 %; the commune has set no mobility levy. Health cover EUR 30.00 each way. September 2026 payroll, default grid, no rate transmitted. The employee has used none of the annual overtime exemption so far this year.
Step 1 — value the overtime.

| Step | Calculation | Result |
|---|---|---|
| Hourly rate | 2,600.00 ÷ 151.67 | EUR 17.14 |
| Overtime pay, 8 hours at 125 % | 8 × 17.14 × 1.25 | EUR 171.40 |
| Gross pay | 2,600.00 + 171.40 | EUR 2,771.40 |

Step 2 — the payslip.

| Line | Base | Rate | Amount |
|---|---|---|---|
| Gross pay | — | — | 2,771.40 |
| Old-age, capped | 2,771.40 (below the ceiling) | 6.90 % | −191.23 |
| Old-age, uncapped | 2,771.40 | 0.40 % | −11.09 |
| Supplementary pension, band 1 | 2,771.40 | 3.15 % | −87.30 |
| General balance contribution, band 1 | 2,771.40 | 0.86 % | −23.83 |
| Additional local health contribution, Alsace-Moselle | 2,771.40 | 1.30 % | −36.03 |
| Employee health-cover share | — | — | −30.00 |
| Overtime old-age relief | 171.40 overtime pay | 11.31 % | +19.39 |
| Social levies base | (2,771.40 × 98.25 % = 2,722.90) + 30.00 | — | 2,752.90 |
| General social contribution, deductible | 2,752.90 | 6.80 % | −187.20 |
| General social contribution, non-deductible | 2,752.90 | 2.40 % | −66.07 |
| Social debt repayment contribution | 2,752.90 | 0.50 % | −13.76 |
| Total employee contributions |  |  | −627.12 |
| Net payable before income tax | 2,771.40 − 627.12 |  | 2,144.28 |
| Net social amount | 2,771.40 + 30.00 − 627.12 |  | 2,174.28 |

Step 3 — the income tax exemption on the overtime. The exemption removes the overtime pay net of the employee contributions actually borne on it from the net taxable amount, within EUR 7,500 a year.

| Step | Calculation | Result |
|---|---|---|
| Overtime gross | — | 171.40 |
| Old-age and supplementary pension on the overtime slice | 6.90 + 0.40 + 3.15 + 0.86 = 11.31 %, exactly cancelled by the 11.31 % relief | 0.00 |
| Local health contribution on the overtime | 171.40 × 1.30 % | −2.23 |
| Deductible general social contribution on the overtime | (171.40 × 98.25 % = 168.40) × 6.80 % | −11.45 |
| Exempt overtime amount |  | EUR 157.72 |
| Year-to-date against the EUR 7,500 cap | 157.72 of 7,500.00 used | 7,342.28 remaining |

Step 4 — finish the payslip.

| Line | Calculation | Amount |
|---|---|---|
| Net taxable before the exemption | 2,144.28 + 66.07 + 13.76 + 30.00 | 2,254.11 |
| Less the exempt overtime | −157.72 |  |
| Net taxable amount |  | 2,096.39 |
| Default grid, 2026 | Band EUR 2,060 – 2,169.99 | 3.50 % |
| Income tax withheld | 2,096.39 × 3.50 % | −73.37 |
| NET PAID | 2,144.28 − 73.37 | EUR 2,070.91 |

Employer position

| Item | Amount |
|---|---|
| Total employer contributions before reliefs — no mobility levy, no managerial-grade contributions | 1,231.29 |
| General reduction: annual gross EUR 33,256.80, coefficient C = 0.1272, annual relief EUR 4,230.27 | −352.52 |
| Employer flat overtime deduction, EUR 1.50 × 8 hours (employer has fewer than 20 employees) | −12.00 |
| Employer contributions payable | 866.77 |
| Total cost of employment | EUR 3,638.17 |

What this example is designed to prove.
1. The three overtime reliefs are three different mechanisms and all three appear here: an employee contribution relief capped at 11.31 %, an employer flat deduction of EUR 1.50 an hour, and an income tax exemption capped at EUR 7,500 net a year. They touch different parties, different bases and different systems.
1. Overtime remains fully subject to the social levies. The EUR 171.40 sits inside the 9.70 % base at 98.25 % like any other pay. The reliefs do not touch it, and an engine that exempts overtime from the levies over-pays the employee and under-declares.
1. The Alsace-Moselle contribution is triggered by the workplace. An employee living in Metz but working at an establishment in Nancy pays nothing extra; an employee living in Nancy but working in Metz pays the 1.30 %. Because it survives the overtime relief, it is also the reason the exempt overtime figure here is not simply the gross.
1. The employer flat overtime deduction is now available at every size. The former 250-employee exclusion was removed with effect from 1 January 2026, so the only distinction left is the rate — EUR 1.50 an hour below 20 employees, EUR 0.50 at 20 and above.
Legal basis: Social Security Code, Articles L130-1, L136-1-1, L137-15, L241-3, L241-13, L241-17, L241-18, L241-18-1, L242-1, L325-1, L834-1, D241-2-4, D242-1, R242-2; General Tax Code, Articles 81 quater, 83, 2°, 204 A to 204 N; Labour Code, Articles L3121-27, L3121-36, L3123-1 and following, L3252-1 to L3252-13, R3252-2; Code of Civil Enforcement Procedures, Articles L212-1 and following; Arrêté of 22 December 2025 (2026 social security ceiling); Décret n° 2025-1299 of 24 December 2025 (2026 wage attachment scale); Décret n° 2026-509 of 12 June 2026 (frozen minimum-wage reference for the general reduction); Official Tax Bulletin BOI-BAREME-000037 (default withholding grids).

## Module 13: Common Business Practices & Non-Statutory Rules


### 13.1 Common Business Practices


#### Describe the common practice for off-cycle or ad-hoc payments.

France constrains off-cycle payment more tightly than most jurisdictions, and the market has settled on a small number of mechanisms that work within the constraint. Labour Code Article L3242-1 requires payment once a month, and the settled reading is that the interval between two payments may not exceed one month; the payroll cycle is therefore not something a client may vary at will.
The dominant mechanism is the advance on the current month (acompte), and it is not a pay run.

| Attribute | Content |
|---|---|
| What it is | A payment on account of the same month's single salary, typically half the monthly pay, usually paid around the 15th |
| Legal status | A right of the employee on request under Labour Code Article L3242-1, not an employer discretion |
| Payslip | None. It generates no separate payslip |
| DSN | None. No separate declaration and no separate withholding calculation |
| Treatment | Netted off against the month's single payslip as a deduction from net pay |
| Payment method | Cash is prohibited where the amount exceeds EUR 1,500; a crossed cheque or a transfer is required |

Modelling the advance as a second pay run is the classic and expensive error here: it duplicates the ceiling entitlement, produces two withholding calculations and files two contract lines in the DSN.
The mechanisms actually used for genuinely ad-hoc payments

| Situation | Market practice |
|---|---|
| A variable element missed at the cut-off — overtime, a commission, an expense | Carried to the following month as a regularisation rather than paid off cycle. The dominant French design pays fixed salary for the current month and variable elements one month in arrears, precisely so that late data has a natural home |
| A payroll error discovered after the run | A supplementary or corrected payslip for the same month. One monthly contribution base and one monthly ceiling entitlement: the two payments are summed, the bands re-sliced on the total, and the contributions already declared deducted. For an employee on the default grid the grid must be read against the month's total net taxable amount, not against each payment (Module 11.1) |
| A leaver paid after the ordinary run | A final settlement outside the cycle is normal and expected, because the end-of-contract documents may not be withheld pending the ordinary pay date. The ceiling reconciliation and the annual reconciliation of the general reduction must both be run in it |
| An annual bonus, a thirteenth month, profit-sharing or incentive-scheme amounts | Often produced in a dedicated run for operational reasons, but declared inside the same monthly DSN as the ordinary payroll. There is no separate bonus filing |
| A genuine loan to the employee | An advance (avance) in the strict sense — money for a period not yet worked. Recoverable only at one tenth of pay per period under Labour Code Article L3251-3, and subject to the wage-attachment floors |

Two rules bound all of this. Recovery is capped: outside the same-month advance on account, the employer may not set its claims against wages beyond one tenth per period, and never below the absolutely protected amount. And an off-cycle payment does not reset the monthly interval: paying a bonus on the 10th does not license deferring the salary to the 10th of the following month.

#### How are non-recoverable draws against future commissions typically handled?

The Anglo-American structure — a draw advanced against future commission, recovered from later commission, and written off if the commission never arrives — does not transplant cleanly into France, and clients from a United States or United Kingdom sales organisation should be told why before the plan is drafted rather than after.
Two constraints reshape the arrangement.

| Constraint | Effect |
|---|---|
| The wage floor is monthly and unconditional | Whatever the commission plan says, the employee must receive at least the statutory minimum wage for the hours worked and at least the collective agreement's minimum for their grade, in every month. A pure commission plan that pays nothing in a bad month is unlawful regardless of what the annual total shows |
| Set-off against wages is capped | Labour Code Articles L3251-1 to L3251-3 prohibit the employer from setting its claims off against wages except within one tenth of pay per period for advances. A clause allowing the employer to recover a draw at any faster rate, or to recover it from a final settlement in full, is void to that extent |

The structure the French market actually uses is therefore a guaranteed minimum against commission rather than a recoverable draw:

| Element | Treatment |
|---|---|
| The guaranteed monthly amount | Paid as ordinary salary in the month: fully within the contribution bands, fully in the social levies base, fully in the net taxable amount. It is not an advance and not a loan |
| The commission when it crystallises | Gross pay in the month it becomes due, reduced by the guaranteed amounts already paid for the same reference period, where the contract expresses the commission as payable over and above the guarantee |
| A shortfall — commission below the guarantee | Not recovered. Settled case law treats a contractual guaranteed minimum as pay definitively acquired; it may be offset against later commission for the same reference period if the contract so provides, but it may not be clawed back as a debt |
| A genuine advance, expressed as a loan | Recoverable, but only at one tenth of pay per period, and never below the absolutely protected amount of EUR 651.69 a month |
| Sales representatives on the statutory status (VRP) | Have their own minimum-resource regime under the applicable national agreement, which operates on a quarterly reference period and overrides a weaker contractual guarantee |

Configuration consequences, and the one that matters most is the last:
1. Model the guarantee as a pay component contributed and taxed in the month it is paid, not as a balance-sheet advance.
1. Model the offset as a reduction of the commission's gross, computed before contributions, where the contract makes the commission payable net of the guarantee.
1. Where the arrangement is a genuine loan, model it as a post-tax deduction capped at one tenth, sitting in the same priority stack as garnishments (Module 7.3).
1. Never process a clawback as a negative gross in a later month. A negative gross retroactively alters a base already declared, and it is not a payslip line: a correction to a declared base is a DSN regularisation carrying the period concerned (Module 9.2). This is the single most common technical failure when an Anglo-American commission plan is lifted into a French engine.

#### Are there common non-statutory leave types? How are they managed and reported?

Yes, and in France the non-statutory layer is unusually large, because sector collective agreements are binding on every covered employer and routinely improve on the Labour Code. The practical consequence is that the statutory entitlements of Module 8 are a floor that very few employees actually sit on.

| Leave type | Source | Paid | Prevalence |
|---|---|---|---|
| Working-time reduction days (jours de RTT) | A collective or company agreement organising working time above 35 hours with compensating days | Yes — treated as time worked | Very common; typically 10 to 12 days a year, and near-universal for managerial grades on a day-count arrangement |
| Seniority leave (congés d'ancienneté) | Sector agreement | Yes | Very common; typically 1 to 5 additional days rising with completed years of service |
| Enhanced family-event leave | Sector or company agreement | Yes | Common; agreements frequently double the statutory minimums of Module 8 |
| Enhanced sick-pay top-up | Sector agreement | Partly | Very common; full pay from day one for managerial grades is the norm in many sectors, against the statutory 90 % after a seven-day waiting period |
| Bridge days (ponts) and company closure days | Company agreement, custom, or unilateral decision | Usually yes, sometimes charged to the leave balance | Common around the May holidays |
| Unpaid leave by agreement (congé sans solde) | Purely contractual — no statutory framework at all | No | Common. Duration, conditions and the right to return must be agreed in writing case by case, because no statute supplies default terms |
| Time savings account (compte épargne-temps) | Company or sector agreement | Deferred | Common in larger employers. Stores untaken days and deferred pay for later use as paid leave, as cash, or as a transfer into a retirement savings plan |
| Additional splitting days (jours de fractionnement) | Statutory in origin, but very frequently waived by agreement or by the employee's written consent | Yes | Common as a waived entitlement — the waiver must be evidenced |

Two entitlements are often assumed to be non-statutory and are not: the sabbatical leave and the leave to create or take over a business are both statutory (Labour Code Article L3142-28 and following), unpaid, and subject to service and notice conditions. They should not be modelled as discretionary company benefits.
How they are managed.

| Dimension | Treatment |
|---|---|
| Accrual | Per the agreement, and independent of the statutory paid-leave rules. Seniority days usually accrue on the service anniversary; working-time reduction days usually accrue monthly or are credited annually in advance |
| Reference period | Frequently the calendar year, where the statutory paid-leave period runs 1 June to 31 May. An employer can therefore be running two leave years at once, and the balances must be held separately and never netted |
| Payment | Paid at the ordinary salary rate. The compulsory comparison between the one-tenth rule and the salary maintenance rule applies to statutory paid leave only — it does not extend to working-time reduction days or seniority days unless the agreement says so |
| Unpaid leave | Suspends the contract. Gross falls, the social security ceiling is prorated down, contributions follow the reduced base, statutory paid leave stops accruing, and the compulsory health cover normally continues with the agreement deciding who funds it |
| Payout on termination | Untaken statutory paid leave must always be paid out. Untaken working-time reduction days and time-savings-account balances are paid out only where the agreement provides — there is no statutory obligation, and this is a per-client configuration decision, not a default |

How they are reported. Nowhere, to any authority — and this is worth stating plainly because it is the reverse of the statutory position.

| Channel | What it carries |
|---|---|
| Payslip | The dates and the amount of statutory paid leave taken in the period are a mandatory payslip item. Working-time reduction days and other agreement leave are shown separately by market convention and by good practice, but no statute requires it |
| DSN | Carries no leave balances. Non-statutory leave reaches the DSN only through its effect on pay, hours and the contract's suspension status. The one exception is the sector paid-leave funds in construction, public works and entertainment, which receive their own flows |
| Authorities | No authority receives a leave balance, and there is no statutory leave return |
| Accounts | Accrued untaken leave is a provision in the client's accounts, and the payroll system is normally its source. Where the agreement provides for a payout on termination, the provision must include the associated employer contributions, not just the gross days |

The design point to carry forward: because none of this is reported, the collective agreement identifier (IDCC) is the field that determines most of it, and it must be a first-class configuration key per establishment rather than an informational attribute. Two clients in the same town with the same headcount and the same salaries will have materially different leave entitlements, sick-pay top-ups and severance floors purely because their activity places them under different sector agreements.
Legal basis: Labour Code, Articles L1226-1 and D1226-1 (sick-pay top-up), L2253-1 and following (relationship between sector, company and individual agreements), L3121-41 and following (working-time arrangements), L3141-3 to L3141-33 (statutory paid leave), L3142-28 and following (sabbatical and business-creation leave), L3151-1 to L3153-2 (time savings account), L3241-1, L3242-1, L3243-3 (payslip content on paid leave), L3251-1 to L3251-3 (set-off against wages); Social Security Code, Article R242-2 (ceiling proration); settled case law of the Social Chamber of the Court of Cassation on guaranteed minimum commission and on the denunciation of customs.
