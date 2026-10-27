# Belgium — Country Compliance Guide (CCG) — BE-CCG-001 v1.0 (Drive, as at 2026-10-21)

Belgium Country Configuration Guide — BE-CCG-001 v1.0

Country Configuration Guide

Income year 2026 — assessment year 2027

Currency: EUR  |  Country code: BE

Mercans Compliance Regulations Team

Version 1.2 — 16 September 2026 (supersedes version 1.1 of 21 August 2026)

Revised 16 September 2026 (Stage 9.5 gap closure): social work bonus annual cap from 1 July 2026 closed at EUR 3,594.36 from the NSSO instructions 2026/3; written part-time contract requirement added under Article 11bis of the Employment Contracts Act of 3 July 1978; the 180-hour overtime ceiling citation confirmed against the 15 July 2026 income tax reform. The Stage 9.5 pass deliberately left the version number and the file name at 1.1 so that the citations carried by the Data Dictionary, the Wage Type Catalogue and the nine report specifications would continue to resolve. That deferral was closed in the Stage 9.6 version-and-file-name pass of 16 September 2026: these changes are released as version 1.2, the file is renamed BE-CCG-001-v1.2.docx, and every citation of the old string in the nine report specifications was updated in the same pass.

Revised 13 October 2026: basic employer contribution for category 1 workers corrected to 19.88% (24.92% was the basic rate from Q1 2015, before the tax shift), plus wage moderation of up to 5.12%; updated in Employer On-Costs (Module 3) and in 5.1 / 5.1.1 (Module 5). Source: ONSS DmfA instructions, “Les cotisations”.

Scope: Belgium national (federal) payroll. Regional and municipal income-tax layers are documented, unbuilt seams settled at the annual assessment.

<!-- nav-index -->
## Navigation — line numbers in this file

*Read this file with `offset`/`limit` rather than whole; it is large.*

- L82: Table of Contents
- L84: Module 1: Foundational Jurisdictional Parameters
  - L86: 1.1 Fiscal, Currency, and Language
  - L121: 1.2 Pay Cycles and Dates
  - L173: 1.3 Extra Pay Period Handling
  - L207: 1.4 Holiday Calendar
  - L240: 1.5 Rounding and Precision Rules
  - L270: 1.6 Complexity Tier Classification
- L298: Module 2: Master Data Configuration
  - L302: 2.1 Employer Information
  - L341: 2.2 Employee Information
  - L418: 2.3 Data Management and Retention
- L467: Module 3: The Gross-to-Net Calculation Framework
  - L469: 3.1 Gross-to-Net Flow
- L598: Module 4: Gross Compensation
  - L600: 4.1 Minimum Wage
  - L660: 4.2 Salary Components
  - L807: 4.3 Proration
  - L859: 4.4 Overtime
  - L899: 4.5 Bonuses
  - L947: 4.6 Wage Classification (Country-Specific)
- L1008: Module 5: Social Security & Pension Systems
  - L1010: 5.1 Contribution Types and Rates
  - L1050: 5.1.1 Contribution Basis Definition
  - L1265: 5.2 Calculation Logic and Edge Cases
  - L1368: 5.3 Voluntary Contributions & Private Schemes
- L1425: Module 6: Income Tax Withholding System
  - L1440: 6.1 System Overview and Methodology
  - L1476: 6.1.1 Taxable Income Definition
  - L1687: 6.2 Tax Rates and Logic
  - L1782: 6.3 Adjustments and Special Cases
- L1901: Module 7: Deductions, Exemptions & Benefits
  - L1903: 7.1 Statutory Tax Reliefs, Deductions, and Exemptions
  - L2105: 7.2 Benefits in Kind (BIK)
  - L2255: 7.3 Garnishments and Court Orders
- L2325: Module 8: Statutory Leave Management
  - L2327: 8.1 Leave Entitlements
- L2527: Module 9: Termination & Irregular Payments
  - L2529: 9.1 Termination Payments
  - L2808: 9.2 Irregular and Retrospective Payments
- L2913: Module 10: Reporting, Compliance & Finalisation
  - L2917: 10.1 Statutory Reporting
  - L3102: 10.2 Integrations
  - L3140: 10.3 Payslip Requirements
  - L3161: 10.4 Other Compliance
  - L3177: 10.5 Year-End Processing and Finalisation
- L3223: Module 11: Advanced Scenarios & Cross-Cutting Logic
  - L3225: 11.1 Calculation Logic
  - L3292: 11.2 Special Employee Groups & Income
- L3432: Module 12: Gross-to-Net Worked Examples
  - L3434: 12.1 Comprehensive Gross-to-Net Examples
- L3671: Module 13: Common Business Practices & Non-Statutory Rules
  - L3673: 13.1 Common Business Practices

---

## Table of Contents

## Module 1: Foundational Jurisdictional Parameters

### 1.1 Fiscal, Currency, and Language

#### What is the statutory tax year?

The statutory tax year for individuals in Belgium is the calendar year: 1 January to 31 December (Income Tax Code 1992 (ITC 92), Articles 199 and 360). Income earned in a calendar year (the income year, inkomstenjaar) is assessed in the following year (the assessment year, aanslagjaar). Income year 2026 therefore corresponds to assessment year 2027.

Payroll follows the same calendar-year cycle: the wage withholding tax (bedrijfsvoorheffing) scales are published per income year, the annual employee tax certificate (form 281.10) covers the calendar year, and social security is reported per calendar quarter within that year.

#### Can employers adopt an alternate tax year? If yes, under what circumstances and what are the implications?

No. The individual tax year is fixed by law as the calendar year and cannot be varied by the employer, by the employee, or by contract. A company may close its accounting year on a date other than 31 December for corporate income tax purposes, but this has no effect whatsoever on payroll: wage withholding tax, the 281.10 certificate, the social security quarters and the annual scales all remain aligned to the calendar year.

The only practical consequence for payroll configuration is that a client whose financial year is not the calendar year needs its payroll-to-general-ledger postings mapped to its own accounting periods, while all statutory outputs stay on the calendar year.

#### What is the official currency for payroll processing and reporting? Provide the ISO code.

The euro, ISO 4217 code EUR, symbol EUR, with two decimal places (cents). Belgium has used the euro as its sole legal tender since 1 January 2002. All wages must be paid in euro; payment in kind is restricted and capped by the Wage Protection Act of 12 April 1965 (Articles 4 to 6). All statutory declarations — the multifunctional social security declaration (DmfA), the wage withholding tax return, and the 281.10 certificate — are denominated in euro.

#### What is the official language for statutory reports and employee payslips?

Belgium has three official languages — Dutch, French and German — and the language of a personnel document is imposed by law according to the employer's seat of operation (exploitatiezetel), not by the employee's residence, the contract language, or the parties' preference.

| Region of the seat of operation | Required language | Legal basis | Sanction if the wrong language is used |
| --- | --- | --- | --- |
| Dutch-language region (Flanders) | Dutch | Decree of 19 July 1973 | Nullity — the document is deemed never to have existed |
| French-language region (Wallonia) | French | Decree of 30 June 1982 | Nullity |
| Brussels-Capital (bilingual) | Language of the employee (Dutch or French) | Coordinated laws of 18 July 1966 | Translation at the employer's expense, with retroactive effect |
| German-language region (Ostbelgien) | German | German-language regime | Replacement of the document |

Two consequences are decisive for system design. First, there are no bilingual personnel documents in Belgium, not even in officially bilingual Brussels: each payslip, contract and set of work rules is unilingual. Second, an English payslip is never sufficient on its own; English may only be provided as an additional courtesy document alongside the legally valid one.

Statutory reports to the authorities follow the same logic: DmfA and Dimona are submitted through Dutch-, French- or German-language channels, and the 281.10 tax certificate is issued in the language of the tax office to which the employer reports.

Legal basis: Income Tax Code 1992, Articles 199 and 360; Wage Protection Act of 12 April 1965, Articles 4 to 6; Decree of the Flemish Community of 19 July 1973; Decree of the French Community of 30 June 1982; Coordinated laws on the use of languages in administrative matters of 18 July 1966.

### 1.2 Pay Cycles and Dates

#### What are the permissible payroll payment frequencies in the country?

The Wage Protection Act of 12 April 1965 (Article 9) governs payment frequency.

| Population | Permitted frequency | Practice |
| --- | --- | --- |
| Employees remunerated per month (white-collar, bedienden) | Once per month | Universal; paid at or near month end |
| Employees remunerated per hour, per piece or per task (blue-collar, arbeiders) | At least twice per month, at intervals of no more than 16 days | An advance around mid-month plus the balance early in the following month |
| Any population where a sector-level collective bargaining agreement (CBA) made binding by Royal Decree provides otherwise | As set by that CBA | Several joint committees have moved blue-collar staff to a single monthly payment |

Weekly and fortnightly cycles are legally possible for hourly-paid staff but are now rare outside a few sectors and temporary agency work. Whatever the frequency, the pay must be settled at the latest on the fourth working day following the end of the work period to which it relates (Article 9, third paragraph), and the actual pay date must be fixed in the work rules (arbeidsreglement).

#### For each frequency, detail the corresponding statutory reporting and payment deadlines for both income tax withholding and social security contributions.

Reporting deadlines in Belgium do not follow the pay frequency. Wage withholding tax is reported monthly or quarterly depending on the size of the employer's withholding, and social security is reported quarterly by every employer regardless of how often wages are paid.

| Obligation | Authority / channel | Periodicity | Deadline |
| --- | --- | --- | --- |
| Wage withholding tax return and payment — standard | FPS Finance, via Finprof | Monthly | The 15th of the month following the month of payment |
| Wage withholding tax return and payment — small employers | FPS Finance, via Finprof | Quarterly | The 15th of the month following the quarter |
| Social security declaration (DmfA) | National Social Security Office (NSSO, RSZ/ONSS) | Quarterly | The last day of the month following the quarter — 30 April, 31 July, 31 October, 31 January |
| Social security balance payment | NSSO | Quarterly | The same date as the DmfA deadline |
| Social security monthly advances | NSSO | Monthly, where due | The 5th day following each month of the quarter |
| Immediate employment declaration (Dimona) | NSSO | Per event | Before the employee starts work; end of employment by the first working day after |
| Annual employee tax certificate 281.10 | FPS Finance, via Belcotax-on-web | Annual | 28 February of the year following the income year |

An employer may file and pay wage withholding tax quarterly only where the total withholding tax of the reference year did not exceed the threshold of Article 412, third paragraph, ITC 92 (fixed annually; the reference amount used to set the 2026 periodicity was EUR 50,240). All other employers file monthly.

Monthly social security advances are compulsory where the contributions due for quarter K-2 exceeded EUR 6,197.34. The advance amounts are calculated and communicated by the NSSO; the difference between the advances paid and the amount finally due under the DmfA must reach the NSSO by the quarterly deadline.

#### Describe the statutory rule for handling pay dates that fall on a weekend or public holiday.

Two distinct rules apply and must not be conflated.

For statutory filing and payment deadlines (wage withholding tax, DmfA, NSSO advances), the general administrative rule applies: where the deadline falls on a Saturday, Sunday or public holiday, it is postponed to the next working day.

For the payment of wages to employees, there is no postponement rule. The Article 9 deadline is absolute, so a pay date falling on a Saturday, Sunday or public holiday must be brought forward to the preceding banking day, not deferred. In practice payroll providers schedule the SEPA credit transfer so that the funds are available to the employee on or before the contractual pay date, and the work rules normally state that where the fixed date is not a banking day the payment is executed on the preceding banking day.

#### What are the common payroll pay dates and cut-off dates for payroll processing?

| Population | Common pay date | Common cut-off for variable data |
| --- | --- | --- |
| White-collar, monthly | The last working day of the month, or a fixed date between the 25th and month end | Between the 10th and the 20th of the same month |
| Blue-collar, twice monthly | An advance between the 15th and the 20th; the balance between the 1st and the 10th of the following month | Around the 12th for the advance; around the 2nd for the balance |
| Temporary agency workers | Weekly | End of the worked week |

Variable elements known only after the cut-off — overtime worked in the last days of the month, late sickness certificates, expense claims — are conventionally carried into the following month's payroll as a retroactive correction rather than delaying the pay run.

Legal basis: Wage Protection Act of 12 April 1965, Article 9; Income Tax Code 1992, Articles 412 and 412bis; NSSO administrative instructions 2026/2, "Obligations towards the NSSO — payment of contributions"; Royal Decree of 5 November 2002 (Dimona).

### 1.3 Extra Pay Period Handling

#### Describe the statutory handling and calculation adjustments required for fiscal years containing extra pay periods (e.g., 53 weekly pays).

Belgium has no statutory concept of an extra pay period and requires no year-end catch-up mechanism, for two structural reasons.

First, the dominant cycle is monthly, and a calendar year always contains exactly twelve months. A 53rd period can only arise for the small population paid weekly (mainly temporary agency work and a few blue-collar sectors), where a calendar year contains 52 or 53 pay weeks depending on how the weeks fall.

Second — and this is the decisive point — Belgian employee social security contributions are a flat percentage of gross pay with no annual or monthly earnings ceiling. A 53rd payment therefore attracts contributions on exactly the same basis as the other 52, and no reconciliation is possible or required.

#### Detail the impact on annualized tax calculations and social security contributions.

Wage withholding tax. The withholding on each payment is computed by annualising that payment (the periodic taxable amount is converted to an annual amount, the annual tax is determined, and the result is divided back down). A 53rd week is annualised on the same basis as any other week, so the withholding rate does not change. Any over-withholding across a 53-week year is not corrected in payroll; it is settled when the employee files the personal income tax return, where the actual annual income is taxed and the total withholding is credited against it.

Social security. There is no impact at contribution level, because there is no ceiling. Two secondary effects should nevertheless be modelled:

The special social security contribution is banded on the quarterly wage, so a quarter containing an extra weekly payment can push the employee into a higher band for that quarter. This is self-correcting, because the contribution is capped per quarter and finally settled through the tax assessment.

The employer exemption on high wages is applied per quarter against a quarterly threshold (EUR 86,700 from 1 January 2026, confirmed unchanged at least through mid-2026; the 1 July 2026 change to this measure excludes paid athletes and professional cyclists from combining it with their sport-specific contribution reduction (Programme Law of 30 May 2026, Articles 109-110), rather than raising the threshold), so an extra pay period in a quarter marginally increases the exempted portion for very high earners.

#### If optional adjustment methods are permitted, provide a step-by-step guide.

No statutory adjustment method exists, and none is permitted or required. Where an employer wishes to smooth a 53-week year for budgeting purposes, the accepted market practice is as follows.

Confirm the pay calendar at the start of the income year and identify whether 52 or 53 weekly pay dates fall within it.

Leave the statutory calculation untouched — apply the ordinary weekly withholding and the ordinary contribution percentages to all 53 payments.

Accrue the cost of the 53rd week in the general ledger across the year, so that the extra period is a budgeting adjustment rather than a payroll calculation adjustment.

Do not attempt an annual withholding true-up in payroll. Any excess withholding is refunded to the employee through the personal income tax assessment, and a payroll-level correction would put the 281.10 certificate out of step with the amounts actually paid to the Treasury.

Legal basis: Income Tax Code 1992, Articles 270 to 275 and Annex III to the Royal Decree implementing ITC 92; Law of 27 June 1969 on social security for employees, Article 23 (no contribution ceiling); NSSO administrative instructions 2026/2.

### 1.4 Holiday Calendar

#### What are the official public holidays?

Belgium has ten statutory public holidays, set by the Royal Decree of 18 April 1974. They apply nationwide and to all private-sector employers.

| # | Holiday | Date in 2026 | Weekday |
| --- | --- | --- | --- |
| 1 | New Year's Day | 1 January 2026 | Thursday |
| 2 | Easter Monday | 6 April 2026 | Monday |
| 3 | Labour Day | 1 May 2026 | Friday |
| 4 | Ascension Day | 14 May 2026 | Thursday |
| 5 | Whit Monday | 25 May 2026 | Monday |
| 6 | National Day | 21 July 2026 | Tuesday |
| 7 | Assumption | 15 August 2026 | Saturday |
| 8 | All Saints' Day | 1 November 2026 | Sunday |
| 9 | Armistice Day | 11 November 2026 | Wednesday |
| 10 | Christmas Day | 25 December 2026 | Friday |

Two holidays fall on a non-working day in 2026 — Assumption (Saturday 15 August) and All Saints' Day (Sunday 1 November). Each must be replaced by a paid day of rest on another day. The replacement days had to be fixed before 15 December 2025 by the joint committee, the works council, or failing that by the employer, and must be posted in the workplace. Where nothing is agreed, the holiday is automatically replaced by the next ordinary working day.

#### Are there any regional, state-specific, or company-specific holidays?

The ten statutory holidays are federal and identical across the country; there is no regional variation in the statutory list. Three additional layers exist and must be configured per client.

Community days — 11 July (Flemish Community), 27 September (French Community), 15 November (German-speaking Community and the King's Feast). These are public-sector and regional-administration holidays and are not statutory paid holidays for private-sector employees, although a sector or company CBA may grant them.

Sectoral holidays and bridge days — many joint committees grant additional paid days off, for example collective closure days or a bridge day following Ascension Day. These are contractual, not statutory.

Company-specific closure — an employer may fix a collective annual closure (collectieve sluiting), which consumes the employees' statutory annual leave and must be set in the work rules.

Legal basis: Law of 4 January 1974 on public holidays; Royal Decree of 18 April 1974 determining the general implementing measures.

### 1.5 Rounding and Precision Rules

#### What are the statutory or common business practice rules for rounding final net pay and individual calculation components?

| Component | Rule |
| --- | --- |
| Gross wage and all wage elements | Calculated and stored to the eurocent (two decimals) |
| Employee social security contribution (13.07%) | Applied to the gross, result rounded to the nearest eurocent |
| Employer social security contributions | Calculated per employee to the eurocent; totals aggregated per quarter in the DmfA |
| Special social security contribution | Determined from the published quarterly band table; the amounts in that table are themselves expressed to the cent |
| Wage withholding tax | From 1 January 2026 the taxable base is no longer rounded down to a lower multiple of EUR 15; the withholding is computed directly from the scale or key formula and the result is rounded to the eurocent |
| Net pay | Rounded to the eurocent; there is no statutory rounding of net pay to a whole e uro |
| Benefits in kind | Valued to the eurocent, except where the law fixes a flat annual amount (for example the minimum company-car benefit of EUR 1,690 for 2026, applied as EUR 140.83 per month) |

The change to the withholding tax rounding is one of the substantive 2026 changes: the Royal Decree of 11 December 2025 amending Annex III to the Royal Decree implementing ITC 92 (Belgian Official Gazette, 29 December 2025) replaced the EUR 15-step rounding of the taxable base with a continuous computation, so that the withholding rises smoothly with the wage instead of in steps.

#### What level of decimal precision is required for statutory reporting?

| Report | Precision |
| --- | --- |
| DmfA (social security) | Amounts in eurocent (two decimals); working days and hours to two decimals where hours are declared |
| Wage withholding tax return (Finprof) | Amounts in euro and cent |
| Form 281.10 via Belcotax-on-web | Amounts in euro and cent |
| Payslip | Euro and cent on every line |
| Annual accounts and social balance sheet | Whole euro in the statutory annual accounts, derived from cent-level payroll data |

Payroll should carry full precision internally and round only at the point of presentation or declaration, so that the sum of the monthly declared amounts reconciles exactly to the annual 281.10 total. Rounding at intermediate steps is the usual cause of one-cent reconciliation differences between the 281.10 certificate and the twelve monthly withholding tax returns.

Legal basis: Royal Decree of 11 December 2025 amending Annex III to the Royal Decree implementing ITC 92 (Belgian Official Gazette, 29 December 2025); NSSO administrative instructions 2026/2; Royal Decree of 27 August 1993 implementing ITC 92, Annex III.

### 1.6 Complexity Tier Classification

#### What is this country's complexity tier, and what reasoning fixes it?

TIER CLASSIFICATION - BELGIUM IS T3 OVERALL, recorded on 2026-08-18 as a decision and not as an inference. The discriminator is what the EMPLOYER must operate, not how sovereignty is allocated: T4 requires a sub-national jurisdiction to impose on the employer a second independent calculation AND a separate remittance to a second authority. Belgium fails that test in both of its devolved layers, so it is T3 and not T4. INCOME TAX: the regions set their own additional percentages and the municipalities their own rate, but neither is applied at source and neither is published as a payroll withholding rate; the employer computes one withholding under ITC 92 Articles 270 to 275 from exactly one published rate set, Annex III to the Royal Decree implementing ITC 92 as replaced for income year 2026 by the Royal Decree of 11 December 2025 (Belgian Official Gazette, 29 December 2025), and remits it to one authority, FPS Finance; the regional and municipal surcharges are settled at the annual assessment and are only approximated inside the federal scale. SOCIAL SECURITY: contributions are set, collected and administered nationally by the National Social Security Office on one base (Law of 27 June 1969, Articles 14 and 23, and the Royal Decree of 28 November 1969), rates are identical across the regions, and the target-group reductions regionalised by the sixth state reform change the AMOUNT of a reduction inside the same DmfA to the same authority - not the number of calculations and not the number of remittances. Blue-collar holiday pay has the same shape: it is financed inside the ordinary NSSO contribution by the 108% uplift on the blue-collar base and paid to the worker by the holiday fund on DmfA data, so the employer still declares once and pays once. This states in the tier vocabulary the determination the scope owner had already recorded in BE-COVERAGE.md section 2 on 2026-08-12 - Quebec-style wrinkle: NO - and it is the same architectural choice Canada made for non-Quebec provincial tax. PER-DOMAIN VERDICTS: statutory_reporting T4-shaped; labour_code T3; income_tax T3; social_security T3; payslip_statute T3; leave T3; termination T3; benefits_in_kind T3; indexation T3; live_legal_change T3; deductions_garnishments T2; payroll_data_protection T2; collective_agreements data-problem. STATUTORY_REPORTING IS T4-SHAPED, which means it behaves like T4 without meeting the discriminator, and the evidence is measured rather than asserted: eight authority filings in scope across the NSSO, two independent FPS Finance channels running on different cycles (Finprof monthly or quarterly, Belcotax-on-web annual), Fedris with the employer's private work accident insurer, and the paying institutions; 36 distinct integration flows registered in scope_manifest.json (18 outbound and 18 inbound, against OUT-01 to OUT-19 and IN-01 to IN-19 in BE-SIR-001-v1.0, whose two Limosa legs are descoped); an NSSO declaration anomaly model of 498 codes; and a 281.10 annual return that is NOT derived from the twelve monthly withholding returns but is an independent annual submission built from the payroll ledger and reconciled against them. That last point is a genuine second independent calculation and a separate return to a second authority, but the second layer is federal and functional rather than sub-national, so the verdict is T4-shaped and not T4 and it must not be quoted as T4. COLLECTIVE_AGREEMENTS IS DATA-PROBLEM because the variability axis in Belgium is not geography but the joint committee (Law of 5 December 1968): the sectoral minimum scales, the index dates and the end-of-year premiums that actually bind an employer are published per joint committee and not as a machine-readable national rate table, which is why the joint-committee code list is still one of the unresolved code tables at limitation L-10. PAYSLIP_STATUTE STAYS AT T3 and no higher because Belgium's three official languages, the rule fixing the language of every personnel document by the employer's seat of operation, and nullity as the sanction in the Dutch- and French-language regions (Decree of 19 July 1973; Decree of 30 June 1982) multiply the DELIVERABLE and not the CALCULATION; the unbuilt French and German payslips are registered at limitation L-16.

The wording above is the recorded tier decision and is reproduced without alteration in _pipeline/build-manifest.json and in scope_manifest.json. It must be changed in all three places at once or in none.

| Domain | Tier | Why |
| --- | --- | --- |
| labour_code | T3 | Employment Contracts Act of 3 July 1978 and the Wage Protection Act of 12 April 1965 over a sectoral CBA layer made binding by Royal Decree, with distinct blue- and white-collar regimes |
| income_tax | T3 | Progressive federal scale, non-cumulative per-payment annualisation, a separate exceptional-payment table and several special regimes; one rate set, one authority |
| social_security | T3 | One authority and one uncapped base, but an indexation mechanism, sectoral funds and a long tail of special contributions |
| payslip_statute | T3 | Three official languages and nullity as the sanction, which multiplies the deliverable rather than the calculation |
| statutory_reporting | T4-shaped | Eight in-scope filings across four authority families on independent cycles, 36 integration flows, a 498-code anomaly model, and a 281.10 that is an independent second calculation |
| leave | T3 | Two entirely different holiday-pay mechanisms by worker category, the blue-collar one financed through the holiday fund |
| termination | T3 | Statutory notice tables by seniority band, with the nr. 58 severance table and unified-status transitional rules |
| benefits_in_kind | T3 | Flat statutory valuations, the CO2 company-car formula, and tax and NSSO valuations that diverge for the same benefit |
| deductions_garnishments | T2 | One national band table under Judicial Code Article 1409, indexed annually by Royal Decree, with a fixed priority order |
| collective_agreements | data-problem | The binding content varies by joint committee and is not published as a machine-readable national rate table |
| indexation | T3 | A published federal mechanism whose arithmetic is derivable and is proved in Module 4.1; the per-sector application date belongs to collective_agreements |
| payroll_data_protection | T2 | Regulation (EU) 2016/679 as applied by the Belgian implementing law, with one supervisory authority |
| live_legal_change | T3 | Several load-bearing 2026 changes with different effective dates, plus a CJEU ruling and a corrective bill not yet enacted |

The two non-T verdicts are load-bearing and are not hedges. T4-shaped means the domain behaves like a parallel system without meeting the discriminator, so it is scoped and staffed as a declared exception rather than as a second country. data-problem means the law is not the obstacle; the figures are, because nobody publishes them in a form a payroll engine can read.

Legal basis: Income Tax Code 1992, Articles 270 to 275; Annex III to the Royal Decree implementing ITC 92, as replaced by the Royal Decree of 11 December 2025 (Belgian Official Gazette, 29 December 2025); Law of 27 June 1969 on social security for employees, Articles 14 and 23; Royal Decree of 28 November 1969; Law of 5 December 1968 on collective bargaining agreements and joint committees; Decree of the Flemish Community of 19 July 1973; Decree of the French Community of 30 June 1982; Judicial Code, Article 1409.

## Module 2: Master Data Configuration

Scope note for the development team. This module gives the concise business summary of the employer and employee data required for Belgian payroll. Field-level definitions, formats, mandatory flags and option-mapper codes are held in the Belgium Data Dictionary (BE-DD-001) and are deliberately not reproduced here. Where a field is named below, BE-DD-001 is the single source of truth for its internal code, length and validation rule.

### 2.1 Employer Information

#### What are the different boards or authorities where an employer must register?

An employer operating in Belgium must be present in the following registers before the first employee starts work.

| Authority | Purpose | When |
| --- | --- | --- |
| Crossroads Bank for Enterprises (Kruispuntbank van Ondernemingen, KBO/BCE) | Legal existence of the enterprise and of each establishment unit | Before any activity |
| FPS Finance — VAT | VAT identification, derived from the enterprise number | Before taxable activity |
| FPS Finance — wage withholding tax | Registration as a withholding agent, giving access to Finprof and Belcotax-on-web | Before the first wage payment |
| National Social Security Office (NSSO) | Employer identification for DmfA and Dimona | Automatically on the first Dimona declaration |
| Joint committee (paritair comité) | Determines the applicable sectoral CBAs, minimum wages, end-of-year premium and sectoral funds | Determined by the main activity; confirmed with the FPS Employment |
| External service for prevention and protection at work | Compulsory occupational health service | Before the first employee starts |
| Work accident insurer | Compulsory private insurance against occupational accidents | Before the first employee starts |
| Sectoral funds (fonds voor bestaanszekerheid), sectoral pension scheme | Sector-specific contributions collected through the DmfA | On affiliation to the joint committee |
| Regional child benefit agency | Child benefit is a regional competence; affiliation is normally automatic through the enterprise number | On registration |

A foreign employer without a Belgian establishment can still employ staff in Belgium; it registers with the NSSO as a foreign employer and, where it has no Belgian presence, may appoint a representative. Posting of foreign workers to Belgium additionally requires a Limosa declaration — filed by that foreign employer itself, not by the Belgian host company, and out of scope for this payroll build (Programmawet/Loi-programme (I) du 27 décembre 2006, art. 139; see the note under the reporting table in Module 10.1).

#### What is the configuration/format of registration numbers allotted by each authority?

| Number | Format | Notes |
| --- | --- | --- |
| Enterprise number (KBO/BCE) | 10 digits, presented as 0nnn.nnn.nnn | The first digit is 0 or 1; the last two digits are a modulo-97 check on the preceding eight |
| Establishment unit number | 10 digits beginning with 2 | One per physical place of activity |
| VAT number | BE + the 10-digit enterprise number | Identical body to the enterprise number |
| NSSO employer number | 9 or 12 positions | Composed of an employer category prefix, a registration number, and a two-digit modulo-97 check computed on the preceding positions |
| Wage withholding tax registration | The enterprise number is used | Access to Finprof is granted per enterprise number |
| Joint committee number | 3 to 6 digits, for example 200, 118, 124, 302 | Drives sectoral wage scales and premiums |

#### Are registration numbers allotted at the central level or at the state/township level?

All payroll-relevant registration numbers are allotted centrally at federal level. The enterprise number, VAT number, NSSO employer number and withholding tax registration are national; none of them varies by region, province or municipality.

Two qualifications matter for configuration. The establishment unit number is granted per physical location and therefore carries the address that determines which language regime applies to personnel documents (see Module 1.1). And child benefit, work-related training incentives and certain target-group employment reductions are administered by the regions (Flanders, Wallonia, Brussels-Capital, German-speaking Community), so the region of the establishment unit — not of the employee's home — drives those entitlements.

Legal basis: Law of 16 January 2003 creating the Crossroads Bank for Enterprises; Law of 27 June 1969 on social security for employees; Royal Decree of 28 November 1969; Law of 5 December 1968 on collective bargaining agreements and joint committees; Law of 4 August 1996 on well-being at work.

### 2.2 Employee Information

#### What are the different residential statuses for an individual?

| Status | Definition | Payroll consequence |
| --- | --- | --- |
| Resident (rijksinwoner) | Domicile or seat of wealth in Belgium (ITC 92, Article 2, §1, 1°). Entry in the National Register creates a rebuttable presumption of residence | Taxed on worldwide income; withholding uses scale I or II with full family reductions |
| Non-resident, meeting the 75% condition | A non-resident whose Belgian professional income represents at least 75% of total professional income, or who works for at least 75% of the contractual working time | Withholding under scale I or II, with the personal and family allowances taken into account |
| Non-resident, not meeting the 75% condition | Any other non-resident receiving Belgian-source employment income | Withholding under scale III, which grants no personal or family allowances |
| Inbound taxpayer or inbound researcher (bijzonder belastingstelsel voor ingekomen belastingplichtigen) | Special regime since 1 January 2022, reformed with effect from income year 2025 | Up to 35% of gross remuneration may be paid as a tax-free reimbursement of employer's own costs; minimum gross remuneration of EUR 70,000 per year (nil for researchers); no absolute cap on the exempt amount since the reform |
| Frontier worker under a double tax treaty | Resident of a neighbouring state working in Belgium, covered by a specific treaty article | Treaty allocation of taxing rights overrides the domestic rule; social security follows Regulation (EC) 883/2004 |

Social security residence is a separate question from tax residence. An employee physically working in Belgium is in principle subject to Belgian social security regardless of tax residence, unless an A1 certificate under Regulation (EC) 883/2004 or a bilateral social security agreement assigns them elsewhere.

#### What employee fields are required for processing payroll and statutory reporting?

Grouped by the obligation that drives them (definitions in BE-DD-001).

Identification — national register number (INSZ/NISS) or BIS number, surname and first name, date and place of birth, gender, nationality, legal home address.

Tax — tax residency status, marital or legal-cohabitation status, spouse's income situation, number and status of dependants (children, disabled children, ascendants), disability of the employee, withholding scale to apply, any specific exemption applied.

Social security — worker category and NSSO worker code, joint committee, blue- or white-collar status, occupational risk class for the work accident insurer, contract type, start and end dates, working time regime and contractual hours, reference person of the reference employment.

Payment — IBAN and BIC, payment method, currency EUR.

Contract and remuneration — function, sectoral wage scale and seniority date, gross salary, fixed premiums, benefits in kind, meal and eco vouchers entitlement, company car reference (catalogue value, CO2 value, fuel type, first registration date, personal contribution), supplementary pension affiliation.

Leave and absence — holiday certificate data from the previous employer, holiday entitlement in days, seniority for notice purposes.

Deductions — garnishment and wage assignment orders, priority, creditor, balance.

#### What is the configuration/format of registration numbers (e.g., tax ID, social security number) allotted to employees?

Belgium uses one number for both tax and social security purposes.

| Number | Format | Construction |
| --- | --- | --- |
| National register number (INSZ/NISS, rijksregisternummer) | 11 digits, presented as YY.MM.DD-SSS.CC | Positions 1-6: date of birth (YYMMDD). Positions 7-9: sequence number — odd for men, even for women. Positions 10-11: check digits = 97 − (first 9 digits mod 97). For persons born from 1 January 2000, a 2 is prefixed to the first nine digits before the modulo is taken |
| BIS number | Same 11-digit structure | Issued to persons not entered in the National Register (for example short-term foreign workers). The birth month is increased by 20 where the gender is unknown at the time of allocation, or by 40 where it is known |

The INSZ is the key for the DmfA, Dimona, the 281.10 certificate and every interaction with the health insurance fund. It is mandatory; an employee cannot be declared without one, which is why the BIS number exists for foreign staff.

#### Provide any relevant combo values or sample inputs for each field.

Representative values only; the authoritative code lists live in BE-DD-001 and in the DmfA code tables.

| Field | Sample values |
| --- | --- |
| INSZ | 86.04.12-345.62 |
| Enterprise number | 0123.456.789 |
| Gender | M, F, X |
| Worker status | Blue-collar (worker), White-collar (employee), Student, Flexi-job worker, Company director |
| Joint committee | 200 (supplementary joint committee for white-collar employees), 124 (construction), 302 (hotel and catering), 118 (food industry) |
| Contract type | Indefinite, Fixed-term, Clearly defined work, Replacement, Student |
| Withholding scale | I (single, or spouse also with professional income), II (spouse without professional income), III (non-resident not meeting the 75% condition) |
| Working time regime | Full-time 38h/5 days; Part-time 19h/2.5 days |
| Payment method | SEPA credit transfer (cash payment is only permitted in the narrow cases of the Wage Protection Act) |
| Meal voucher | Face value EUR 10.00, employer part EUR 8.91, employee part EUR 1.09 |

#### What previous employment information must new joiners declare?

| Item | Source | Why payroll needs it |
| --- | --- | --- |
| Holiday certificate (vakantieattest) | Previous employer, for white-collar staff | The new employer must deduct the early holiday pay already settled by the previous employer when the employee takes leave, and when paying the double holiday pay |
| Holiday rights already used in the year | Previous employer | Prevents double granting of the 20-day statutory entitlement |
| Form C4 | Previous employer | Confirms the reason and date of the end of the previous contract; required for unemployment benefit and relevant to notice calculations |
| Seniority acquired with the same employer or within the group | Employee declaration, prior contracts | Drives the notice period table and any sectoral seniority premiums |
| Family and dependant situation | Employee declaration | Determines the withholding scale and the reductions applied |
| Supplementary pension history | Previous employer or the DB2P database | Relevant where the sectoral scheme carries over |
| Existing garnishments and wage assignments | Court or creditor notification | These follow the employee and must be re-established with the new employer |
| Prior gross income in the same year, where relevant | Fiche 281.10 of the previous employer | Not used for the withholding calculation, which is not cumulative, but needed to explain the annual assessment to the employee and to set the reference wage for exceptional payments |

Belgium does not operate a cumulative year-to-date withholding system, so a new employer does not take over the previous employer's tax position. Each employer withholds as though its own payments were the employee's only income; the final position is settled in the annual tax return.

Legal basis: Income Tax Code 1992, Articles 2, §1, 1°, 227 and 243/1; Royal Decree implementing ITC 92, Annex III; Law of 8 August 1983 on the National Register; Royal Decree of 30 March 1967 (annual holidays); Regulation (EC) 883/2004.

### 2.3 Data Management and Retention

#### What are the statutory requirements for payroll record retention (e.g., number of years)?

| Document | Retention period | Source |
| --- | --- | --- |
| Individual account (individuele rekening) | 5 years from the end of the period to which it relates | Royal Decree of 8 August 1980 on the keeping of social documents |
| Payslips and pay records | 5 years | Royal Decree of 8 August 1980 |
| Work rules, staff register, employment contracts | 5 years after the end of the contract | Royal Decree of 8 August 1980 |
| DmfA supporting data | 5 years | Law of 27 June 1969 |
| Dimona acknowledgement | Kept as part of the social documents; the immediate declaration itself is retained by the NSSO | Royal Decree of 5 November 2002 |
| Tax documents, including 281.10 and the withholding tax returns | Until the end of the 7th year or accounting period following the taxable period | Income Tax Code 1992, Article 315 |
| Supplementary pension records | Long-term, through the DB2P database | Law of 28 April 2003 |

The practical planning rule is 7 years, because the tax retention obligation is the longest of the payroll-relevant obligations and the social documents fall inside it.

#### Are there specific data privacy laws (like GDPR) that govern the storage and handling of employee payroll data?

Yes. Payroll data is personal data and often special-category data (health data behind sickness absence, trade union membership behind certain premiums).

Regulation (EU) 2016/679 (GDPR) applies directly.

The Law of 30 July 2018 on the protection of natural persons with regard to the processing of personal data is the Belgian implementing act; it also governs the processing of the national register number, which may only be used where a legal basis exists — payroll and social security reporting is such a basis.

CBA no. 81 governs the monitoring of electronic online communications data at work.

The Data Protection Authority (Gegevensbeschermingsautoriteit) is the supervisory authority.

Consequences for the payroll platform: a documented lawful basis per processing purpose (legal obligation for statutory reporting, contract perfo payroll provider, and breach notification within 72 hours. Personal data must not be transferred outside the EEA without an adequacy decision or standard contrarmance for wage payment), a record of processing activities, retention limits aligned to the table above with deletion at expiry, encryption in transit and at rest, role-based access, a data processing agreement between the client and thectual clauses.

#### How should historical payroll data (e.g., from a previous provider) be handled for cumulative calculations?

Belgian payroll is not cumulative for withholding tax, which removes the largest category of take-over risk. Several elements are nevertheless year-to-date dependent and must be loaded at implementation.

| Item | Why it is year-to-date dependent | Take-on requirement |
| --- | --- | --- |
| Double holiday pay for white-collar staff | Calculated as 92% of the monthly salary, prorated on the months worked in the holiday service year | Months of service in the service year, and any holiday pay already paid |
| Departure holiday pay already paid by a previous employer | Must be deducted when the new employer pays holiday pay or grants leave | The holiday certificate of the previous employer |
| Special social security contribution | Banded on the quarterly wage and capped per quarter | Quarterly gross already declared in the current quarter |
| Employer exemption on high wages | Applied against a quarterly threshold | Quarterly gross already declared |
| Reference wage for exceptional payments | The withholding rate on a bonus or holiday pay depends on the normal annual gross remuneration | The current annual gross reference |
| Form 281.10 for the year of transfer | Must present the full calendar year | Year-to-date gross, withholding and benefit amounts from the previous provider |
| Fiscal and social work bonus | Capped per calendar year | Amounts already granted in the year |
| Garnishment balances | The attachable amount depends on the outstanding debt | Outstanding balance per creditor |

The recommended sequence is: load employee master data, then load year-to-date balances per wage type as at the last period processed by the previous provider, then run a parallel payroll for at least one period and reconcile the DmfA totals and the withholding tax return to the previous provider's output before cutover. Where the transfer occurs mid-year, agree explicitly which party issues the 281.10 for the year — one certificate per employer per year is the norm, so a change of provider (not of employer) must produce a single combined certificate.

Legal basis: Royal Decree of 8 August 1980 on the keeping of social documents; Income Tax Code 1992, Article 315; Regulation (EU) 2016/679; Law of 30 July 2018; CBA no. 81; Royal Decree of 30 March 1967 (annual holidays).

## Module 3: The Gross-to-Net Calculation Framework

### 3.1 Gross-to-Net Flow

#### Deliverable: Step-by-step description of the standard Gross-to-Net calculation framework

The Belgian gross-to-net sequence is fixed by the interaction of three statutes: the Wage Protection Act of 12 April 1965 (what may be deducted and in what order), the Law of 27 June 1969 (social security), and the Income Tax Code 1992 with Annex III to its implementing decree (wage withholding tax). The order below is not a convention — reversing steps 2 and 4 would change the result, because the taxable base is defined net of the employee social security contribution.

GROSS EARNINGS

|

[1] Sum all wage elements subject to social security (the NSSO wage concept)

|

[2] Employee social security contribution 13.07%   -->  paid to the NSSO

|     (reduced by the social work bonus for low wages)

v

TAXABLE BASE  =  gross - employee social security contribution

|

[3] Add benefits in kind and other taxable items that carry no social security

|

[4] Wage withholding tax (bedrijfsvoorheffing), from the Annex III scales

|     less the fiscal work bonus and other Annex III reductions

v

[5] Special social security contribution (banded on the quarterly wage)

|

[6] Post-tax deductions: employee meal voucher part, personal supplementary

|  pension contribution, garnishments and wage assignments, company loans

v

NET PAY  -->  SEPA credit transfer

In parallel, on the same gross:

[E1] Employer social security contributions (approx. 25% facial rate)

[E2] Special employer contributions: company car CO2 contribution,

8.86% on supplementary pension premiums, sectoral fund contributions

[E3] Employer share of meal vouchers, insurance premiums, work accident premium

[E4] Provisions: double holiday pay, end-of-year premium, notice indemnity

#### Step 1: Summation of Gross Earnings

All amounts that qualify as wage under Article 2 of the Wage Protection Act, as extended for social security purposes by Article 14 of the Law of 27 June 1969 and the Royal Decree of 28 November 1969, are added together: basic salary for the period, sectoral and company premiums, commission, overtime pay including the overtime supplement, the single holiday pay paid when leave is taken, the end-of-year premium, guaranteed salary during sickness, and benefits in kind that the NSSO treats as wage (company car, free housing, free electricity).

Items explicitly excluded from the NSSO wage concept are not added here: genuine reimbursements of expenses proper to the employer, meal and eco vouchers meeting all their conditions, and the double holiday pay (which is excluded from employer contributions but not from the employee contribution).

#### Step 2: Employee Social Security Contribution

A single global contribution of 13.07% is withheld from the gross, with no ceiling. For blue-collar workers the contribution base is the gross increased by 8%, because their holiday pay is paid by the holiday fund rather than by the employer.

The social work bonus reduces this contribution for low wages, up to EUR 137.74 per month for a blue-collar worker and EUR 127.54 for a white-collar worker at the rates in force from 1 July 2026. The bonus can never exceed the contribution itself, so it cannot create a negative deduction.

#### Step 3: Determination of Taxable Income

Taxable income for withholding purposes is the gross remuneration minus the employee social security contribution actually withheld, plus any taxable item that is not subject to social security (for example the taxable part of a benefit in kind that the NSSO does not treat as wage), minus items that are exempt from tax (for example the exempt part of a bicycle allowance or a homeworking allowance).

The special social security contribution is not deductible from the taxable base.

#### Step 4: Calculation of Income Tax Withholding

The withholding is computed by annualising the periodic taxable base, deducting the lump-sum professional expenses (30% capped at EUR 6,070 for income year 2026), applying the annual withholding scale, deducting the reduction for the tax-free allowance and for dependants, and dividing back to the period. Exceptional payments (bonus, double holiday pay, arrears, termination indemnity) bypass this scale and use the separate exceptional-payment percentage table driven by the employee's normal annual gross remuneration.

#### Step 5: Special Social Security Contribution

The special social security contribution (bijzondere bijdrage voor de sociale zekerheid) is a separate employee withholding, banded on the quarterly gross wage and capped at EUR 182.82 per quarter for an individually assessed employee. Because the band depends on the quarterly total, the withholding taken in months 1 and 2 of a quarter is provisional and is corrected at the last payment of the quarter.

#### Step 6: Application of Post-Tax Deductions

Deducted from the net, in this order:

The employee's own contribution to meal vouchers (minimum EUR 1.09 per voucher).

The employee's personal contribution to the supplementary pension plan, if any. This is withheld from net pay but generates a reduction in the wage withholding tax of 30% of the contribution, applied at step 4.

Wage assignments and garnishments, within the protected-earnings bands of Article 1409 of the Judicial Code.

Repayment of advances and company loans, subject to the 20% aggregate cap of Article 23 of the Wage Protection Act.

#### Step 7: Finalization of Net Pay

The result is the amount transferred to the employee's IBAN. Non-cash entitlements that never pass through net pay — the meal voucher face value, the eco voucher, the company car — are shown on the payslip for information but are not added to the transfer.

#### Employer On-Costs (Calculated in Parallel)

Employer costs are computed on the same gross but never touch the employee's net.

| Component | 2026 basis |
| --- | --- |
| Ordinary employer contributions, white-collar | Approximately 25% facial rate (basic contribution 19.88% including the branches, plus wage moderation, less the structural reduction) |
| Ordinary employer contributions, blue-collar | Approximately 30.57%, calculated on the gross at 108%, because holiday pay is funded through the holiday fund |
| Exemption on high wages | Basic and wage moderation contributions are not due on the part of the quarterly wage above EUR 86,700 from 1 January 2026 (confirmed unchanged at least through mid-2026; the 1 July 2026 change to this measure excludes paid athletes and professional cyclists from combining it with their sport-specific contribution reduction (Programme Law of 30 May 2026, Articles 109-110), rather than raising the threshold) |
| Company car CO2 solidarity contribution | Per vehicle, per month, formula in Module 7.2 |
| Supplementary pension | 8.86% special employer contribution on premiums, plus the 4.4% insurance premium tax |
| Sectoral funds | Per joint committee, collected through the DmfA |
| Work accident insurance | Private premium, risk-rated |
| Provisions | Double holiday pay (roughly 92% of a month's salary per year), end-of-year premium (commonly one month), notice indemnity risk |

#### G2N Flow Summary

| Line | Description | Sign |
| --- | --- | --- |
| A | Gross remuneration for the period | + |
| B | Employee social security contribution, 13.07% of A, less the social work bonus | − |
| C | Taxable base = A − B, adjusted for non-sociable taxable items and tax-exempt items | = |
| D | Wage withholding tax on C, less the fiscal work bonus and Annex III reductions | − |
| E | Special social security contribution, from the quarterly band table | − |
| F | Post-tax deductions: meal voucher employee part, personal pension contribution, garnishments | − |
| G | Net pay = A − B − D − E − F | = |

Legal basis: Wage Protection Act of 12 April 1965, Articles 2, 23 and 23bis; Law of 27 June 1969, Articles 14 and 23; Royal Decree of 28 November 1969; Income Tax Code 1992, Articles 270 to 275; Annex III to the Royal Decree implementing ITC 92, as amended by the Royal Decree of 11 December 2025; Judicial Code, Article 1409.

## Module 4: Gross Compensation

### 4.1 Minimum Wage

#### Is there a minimum wage? Who is eligible?

Yes. Belgium has a two-tier minimum wage system.

The national floor is the guaranteed average minimum monthly income (gewaarborgd gemiddeld minimum maandinkomen, GMMI), set by CBA no. 43 concluded in the National Labour Council and made binding by Royal Decree. It applies to every private-sector employee aged 18 or over who is employed under a contract of at least one month, whatever the sector, and it is a floor that no sector or company may undercut.

Above that floor, each joint committee sets its own sectoral minimum wage scales, generally by function classification and seniority. In most sectors the sectoral minimum is materially higher than the GMMI, so the GMMI operates as a backstop rather than as the operative minimum. The sectoral scale of the joint committee to which the employer belongs is therefore the amount payroll must actually validate against.

The GMMI is a global concept: the test is whether the employee's total annual remuneration divided over the year reaches the threshold. Variable pay, the end-of-year premium and a thirteenth month count towards it; genuine expense reimbursements, meal vouchers and the double holiday pay do not.

#### Is the minimum wage applicable at a national level or does it vary by province/state?

The GMMI is national. It does not vary by region, province or municipality. Variation comes from the sector (joint committee), not from geography — an employee in Antwerp and an employee in Charleroi in joint committee 200 face the same scale.

#### Provide all applicable minimum wage rates.

| Effective date | GMMI, gross per month, full-time | Basis of the change |
| --- | --- | --- |
| 1 January 2026 | EUR 2,154.11 | Carried over from 2025 |
| 1 April 2026 | EUR 2,189.81 | Agreed increase under CBA no. 43 |
| 1 August 2026 | EUR 2,233.61 | Indexation of 2% following the crossing of the pivot index in June 2026 |

The August amount reconciles exactly with the April amount increased by the statutory 2% indexation step (2,189.81 x 1.02 = 2,233.61), which confirms that the April movement was a negotiated increase and the August movement an index adjustment.

Two derived rates matter in practice:

Hourly equivalent — the GMMI divided by the sectoral weekly working time. On a 38-hour week the monthly figure is divided by 164.67 hours (38 x 52 / 12), giving approximately EUR 13.57 per hour at the August 2026 level.

Employees under 18 — reduced percentages of the GMMI applied by age still exist in some sectoral scales, but CBA no. 43 itself no longer provides a general youth reduction for employees aged 18 and above.

Sectoral minimum scales are published per joint committee and change on the sector's own indexation date; for the largest white-collar committee (joint committee 200) wages were indexed by 2.21% on 1 January 2026.

#### Does the minimum wage impact any tax or social security calculations?

Yes, in three ways.

Social work bonus. The maxima and the full-amount (lower) limits of the social work bonus, which reduces the employee's 13.07% contribution, are set as percentages of the GMMI, so a GMMI increase feeds through to them. The two calendars are not the same and must not be conflated. The GMMI steps on 1 January, 1 April and 1 August 2026 (table above); the work bonus parameter set steps five times — 1 January, 1 March, 1 April, 1 July and 1 September 2026 — and has no 1 August row. The 1 March and 1 September steps are not GMMI movements at all: they index the upper limit, the wage at which the bonus reaches zero, on the social-benefit calendar rather than on the GMMI. Component A's full-amount (lower) limit runs EUR 2,833.36 from 1 January, EUR 2,880.32 from 1 April and EUR 2,937.93 from 1 July 2026; the wage at which component A reaches zero runs EUR 3,271.48 from 1 January, EUR 3,336.98 from 1 March and EUR 3,403.62 from 1 September 2026. Row selection is by the pay month. Module 5.1.1 carries the full two-component parameter tables — component B, the blue-collar maxima and the degressive coefficients — and governs.

Structural reduction of employer contributions. Its low-wage component is calibrated on the same wage levels, so a GMMI increase widens the population that benefits.

Fiscal work bonus. The tax-side counterpart, deducted from the wage withholding tax, is available only to employees who receive the social work bonus and is therefore governed by the same thresholds.

The minimum wage does not change any contribution rate or tax rate; it changes who qualifies for the low-wage reliefs.

#### How are deductions handled if they cannot be made due to minimum wage constraints?

Belgian law protects the employee's net pay through Articles 23 and 23bis of the Wage Protection Act rather than through a minimum-wage carve-out. The rules that govern an insufficient net are:

The total of the deductions listed in Article 23 (fines, damage caused by the employee, advances, security deposits) may not exceed one fifth of the net wage due at each payment, after deduction of social security contributions and tax.

The one-fifth cap does not apply where the employee has fraudulently terminated the contract, and it does not apply to the deductions imposed by law: social security contributions, wage withholding tax, and the special social security contribution.

Garnishments and wage assignments are separately limited by Article 1409 of the Judicial Code, which protects a floor of net income that cannot be attached at all (see Module 7.3).

Where the deductions cannot all be made in the period, the payroll rule is: statutory deductions first and in full, then garnishments within their own protected bands, then contractual deductions up to the one-fifth cap. Any unrecovered contractual balance is carried forward to the following period; it is never taken from a period in which it would breach the cap. Where an employee's remuneration falls below the GMMI because of unpaid absence in the month, the GMMI test is not breached — the guarantee applies to the pay for work actually performed, prorated.

Legal basis: CBA no. 43 of the National Labour Council; Wage Protection Act of 12 April 1965, Articles 23 and 23bis; Judicial Code, Article 1409; NSSO administrative instructions 2026/2 (work bonus).

### 4.2 Salary Components

#### What are the mandatory and common salary components?

| Component | Mandatory? | Source |
| --- | --- | --- |
| Basic salary | Yes | Contract, sectoral scale, GMMI floor |
| Automatic index adjustment | Yes, where the sector provides for it | Sectoral CBA; nearly universal in Belgium |
| Single holiday pay | Yes | Royal Decree of 30 March 1967 |
| Double holiday pay | Yes | Royal Decree of 30 March 1967 |
| End-of-year premium (thirteenth month) | Only where a sectoral or company CBA provides it — not a general statutory right | Sectoral CBA |
| Overtime supplement | Yes, where overtime is worked | Labour Act of 16 March 1971 |
| Guaranteed salary during sickness | Yes | Employment Contracts Act of 3 July 1978 |
| Public holiday pay | Yes | Law of 4 January 1974 |
| Commuting allowance | Yes for public transport and, in most sectors, for private transport | CBA no. 19/9 and sectoral CBAs |
| Bicycle allowance | Yes since 1 May 2023 where no sectoral scheme exists | CBA no. 164 |
| Meal vouchers | No, but present in a large majority of companies | Royal Decree of 28 November 1969, Article 19bis |
| Eco vouchers | Only where the sector provides them | Sectoral CBA; being phased out |
| Company car and fuel card | No | Company policy |
| Supplementary pension (second pillar) | Only where a sectoral or company scheme exists | Law of 28 April 2003 |
| Non-recurring result-tied bonus (CBA no. 90) | No | CBA no. 90 |
| Homeworking allowance | No | NSSO instructions and tax circular |

#### What is the general definition and pay cycle for each component?

| Component | Definition | Pay cycle |
| --- | --- | --- |
| Basic salary | Fixed remuneration for the contractual working time | Monthly (white-collar); at least twice monthly (hourly-paid) |
| Index adjustment | Automatic uplift of scales and actual wages tracking the smoothed health index | On the sector's index date — for joint committee 200, 1 January |
| Single holiday pay | The normal salary paid for days of statutory leave taken | With the salary of the month in which the leave is taken |
| Double holiday pay | A supplement of 92% of the monthly salary for a fully worked service year | Once a year, usually May or June |
| End-of-year premium | Commonly one gross month, or a percentage of annual earnings | December |
| Overtime supplement | 50% or 100% on top of the normal hourly rate | With the salary of the month worked |
| Guaranteed salary | Continued pay during the first period of incapacity | With the monthly salary |
| Commuting allowance | Reimbursement of home-to-work travel | Monthly |
| Bicycle allowance | EUR 0.30 per kilometre under CBA no. 164 for 2026, for up to 40 km per day | Monthly |
| Meal vouchers | Electronic voucher per day actually worked; maximum face value EUR 10.00 from 1 January 2026 | Monthly, in the month following the worked days |
| Company car | Private use of an employer-provided vehicle | Continuous; taxed monthly |
| CBA no. 90 bonus | Collective bonus tied to measurable objectives | Once per plan period |

#### Which components are taxable vs non-taxable and sociable vs non-sociable?

"Sociable" means subject to social security contributions. Belgium has a distinctive feature: several components are treated differently by the NSSO and by the tax authority, so a single flag is never sufficient.

| Component | Social security | Income tax | Note |
| --- | --- | --- | --- |
| Basic salary | Subject | Taxable | Ordinary scale |
| Overtime pay and supplement | Subject | Taxable, with the overtime tax relief on up to 180 hours | Relief is a reduction, not an exemption |
| Single holiday pay | Subject | Taxable at the ordinary scale for the days taken |  |
| Double holiday pay | Employee contribution of 13.07% is due; employer contributions are not | Taxable at the exceptional-payment rate | The asymmetry is the classic Belgian trap |
| End-of-year premium | Subject | Taxable at the exceptional-payment rate |  |
| CBA no. 90 bonus | Exempt from ordinary contributions up to EUR 4,255 (2026); a special employer contribution of 33% and an employee solidarity contribution of 13.07% apply | Exempt up to EUR 3,701 (2026); the excess is taxable | Two different ceilings — a frequent configuration error |
| Meal vouchers | Not subject, if all conditions are met (employee part of at least EUR 1.09, face value not above EUR 10.00, one per worked day, electronic) | Not taxable under the same conditions | If a condition fails, the whole voucher becomes wage |
| Eco vouchers | Not subject, within the sectoral ceiling | Not taxable | Being phased out |
| Company car (private use) | Not subject to ordinary contributions; the employer pays the CO2 solidarity contribution instead | Taxable benefit in kind, minimum EUR 1,690 per year for 2026 |  |
| Bicycle allowance | Exempt up to EUR 0.37 per km | Exempt up to EUR 0.37 per km and EUR 3,700 per year |  |
| Homeworking allowance | Exempt up to EUR 160.99 per month from 1 March 2026 | Same limit | Flat office allowance |
| Commuting allowance, public transport | Exempt | Exempt within limits |  |
| Employer supplementary pension premium | Not wage, but a special employer contribution of 8.86% applies | Not taxable on payment; the benefit is taxed at retirement |  |
| Genuine expenses proper to the employer | Not subject | Not taxable | Must be justified |
| Severance indemnity | Subject | Taxable at the average rate of the last normal year |  |

#### Are components uniform across the country or do they differ by state/province?

The statutory rules — social security, wage withholding tax, holiday pay, minimum wage floor — are federal and uniform. Differences do not come from geography but from the joint committee, which is determined by the employer's main activity and applies nationwide within its scope. Two employers on the same street can therefore owe different end-of-year premiums, different sectoral supplements and different index dates because they sit in different joint committees.

The only genuinely geographic variations relevant to payroll are: the language of the payslip (Module 1.1), the regionally administered target-group reductions of employer contributions, and the regional and municipal income tax surcharges, which are settled at the annual assessment and are only approximated inside the withholding.

#### What is the calculation logic for each salary component?

| Component | Logic |
| --- | --- |
| Basic salary, monthly | Fixed amount; prorated by the fraction of the month worked (Module 4.3) |
| Hourly wage | Hourly rate x hours worked |
| Index adjustment | Existing wage x index coefficient, applied on the sector's index date; applies to actual wages, not only to scale minima |
| Single holiday pay, white-collar | The normal salary continues to be paid for the leave days; already contained in the monthly salary |
| Double holiday pay, white-collar | 92% of the gross monthly salary of the month in which it is paid, x months of service in the holiday service year / 12 |
| Departure holiday pay, white-collar | 15.34% of the gross earned in the service year, of which 7.67% single and 7.67% double |
| Holiday pay, blue-collar | Paid by the holiday fund at 15.38% of the gross of the service year at 108%, of which 8% single and 7.38% double |
| Overtime supplement | Normal hourly rate x 50% (or 100% on Sundays and public holidays) x overtime hours |
| End-of-year premium | Per sectoral CBA; commonly one gross month, prorated on months of service in the reference year |
| Guaranteed salary | 100% of normal pay for the statutory period, then partial (Module 8) |
| Meal vouchers | Number of days actually worked x face value; employee part withheld from net |
| Company car benefit | Catalogue value x CO2 percentage x 6/7 x age coefficient, with a floor of EUR 1,690 per year for 2026 |
| CBA no. 90 bonus | Per the approved bonus plan, subject to the social and tax ceilings |

#### Which components require employee-declared values and submissions?

| Component | Employee declaration | Frequency |
| --- | --- | --- |
| Family situation for withholding purposes | Dependants, spouse's income, disability | On hire and on any change |
| Commuting allowance | Distance, mode of transport, proof of a season ticket | On hire and on any change of address |
| Bicycle allowance | Days cycled and kilometres | Monthly |
| Homeworking allowance | Structural homeworking arrangement | Once, in the policy or addendum |
| Company car | Personal contribution, private kilometres if relevant | On allocation |
| Meal vouchers | Nothing; derived from the attendance record | — |
| Supplementary pension personal contribution | Consent, beneficiary designation | On affiliation |
| Garnishment and wage assignment | Not employee-declared; served by the creditor or court | On event |
| Holiday certificate from a previous employer | Employee provides the certificate | On hire |
| Inbound taxpayer regime | Joint employer and employee application to the tax administration within 3 months | Once, then annual list |

#### Deliverable: Define the primary earnings base for social security contributions. Produce a comprehensive Inclusion/Exclusion analysis.

The base is the NSSO wage concept: the wage as defined by Article 2 of the Wage Protection Act of 12 April 1965, applied for social security purposes by Article 14 of the Law of 27 June 1969, and then narrowed by the exclusions listed in Article 19 and following of the Royal Decree of 28 November 1969. In plain terms: everything the employee receives as consideration for work under the contract is contributory, unless the Royal Decree of 28 November 1969 explicitly takes it out.

Two mechanical adjustments to the base:

For blue-collar workers, the base is the gross increased by 8%, because their holiday pay is funded through the holiday fund and not paid by the employer.

For double holiday pay, the employee contribution of 13.07% is due but employer contributions are not.

Inclusions

| Item | Reason |
| --- | --- |
| Basic salary, hourly wage, piece rates | Direct consideration for work |
| Commission, sales bonuses, individual performance bonuses | Consideration for work |
| Overtime pay and the overtime supplement | Consideration for work |
| Premiums for shift work, night work, standby, dirty work | Consideration for work |
| Single holiday pay | Deferred salary |
| Double holiday pay | Employee contribution only |
| End-of-year premium and thirteenth month | Deferred salary |
| Guaranteed salary during sickness | Continued pay by the employer |
| Public holiday pay and replacement day pay | Continued pay |
| Benefits in kind treated as wage: free housing, free heating and electricity, free meals above the statutory value | Advantage in money's worth |
| Severance and notice indemnities | Explicitly treated as wage for contribution purposes |
| Employee's personal use of a company car | Excluded from ordinary contributions but replaced by the employer CO2 solidarity contribution |

Exclusions

| Item | Condition for exclusion |
| --- | --- |
| Reimbursement of expenses proper to the employer | Must be genuine and justified, either on the basis of actual costs or on a flat rate accepted by the NSSO |
| Meal vouchers | All conditions of Article 19bis met: one per worked day, employee part of at least EUR 1.09, face value not above EUR 10.00 from 1 January 2026, electronic, granted under a CBA or individual agreement |
| Eco, sport and culture vouchers | Within their own conditions and ceilings; being phased out |
| Employer premiums to a supplementary pension scheme | Replaced by the 8.86% special employer contribution |
| CBA no. 90 non-recurring result-tied bonus | Up to EUR 4,255 for 2026; replaced by a 33% special employer contribution and a 13.07% employee solidarity contribution |
| Homeworking allowance | Up to EUR 160.99 per month from 1 March 2026 |
| Bicycle allowance | Up to EUR 0.37 per kilometre |
| Commuting reimbursement | Within the CBA no. 19/9 and sectoral limits |
| Amounts paid by third parties without employer involvement | Not paid in consideration of the employment relationship |
| Statutory benefits paid by the health insurance fund or the holiday fund | Not employer wage |

The exclusions are conditional, not absolute. A meal voucher that breaches any single condition is requalified as ordinary wage in full, retroactively and with contributions due on the entire face value; the same all-or-nothing logic applies to the CBA no. 90 bonus above its ceiling and to flat-rate expense allowances that cannot be justified.

Legal basis: Wage Protection Act of 12 April 1965, Article 2; Law of 27 June 1969, Articles 14 and 23; Royal Decree of 28 November 1969, Articles 19 and 19bis; CBA no. 90; CBA no. 164; CBA no. 19/9; Royal Decree of 30 March 1967.

### 4.3 Proration

#### Are fixed wages prorated for the number of working days?

Yes. A monthly-paid employee who is not present for the whole month receives a proportion of the monthly salary. Belgium has no single statutory proration formula; the method is set by the sectoral or company CBA, by the work rules, or failing that by settled practice, and it must be applied consistently.

#### Describe the statutory or standard business practice for prorating fixed salary components for mid-period hires and terminations.

Three methods are in general use.

| Method | Formula | Typical use |
| --- | --- | --- |
| Calendar-day method | Monthly salary x calendar days of employment / calendar days in the month | Less common; disadvantages employees hired at the start of a long month |
| Working-day method | Monthly salary x working days present / working days in the month | The most widespread method for white-collar staff |
| Hourly method | Monthly salary / 4.3333 / weekly hours x hours worked | Used where the working pattern is irregular; the coefficient 4.3333 is 52/12 |

The working-day method is the market standard, and the same method must be used for both entry and exit so that an employee who joins and leaves in the same year is not paid twice or short-paid for the transition month. Fixed premiums that are expressed per month follow the salary; premiums expressed per day or per worked hour are simply counted.

For absence within a month, the mirror rule applies: the unpaid days are valued using the same method and deducted from the full monthly salary, rather than the present days being multiplied up.

#### Provide the proration formula and a worked example.

Formula (working-day method)

Prorated salary = Monthly salary x (working days actually covered / total working days in the month)

Worked example — mid-month hire, 2026

An employee joins on Monday 16 March 2026 with a full-time gross monthly salary of EUR 3,600.00, in a five-day week. March 2026 has 22 working days (Monday to Friday, no public holiday falls in March 2026). From 16 March to 31 March there are 12 working days.

| Step | Calculation | Result |
| --- | --- | --- |
| 1. Full monthly salary | — | EUR 3,600.00 |
| 2. Working days in March 2026 | Mondays to Fridays | 22 |
| 3. Working days covered | 16 to 31 March | 12 |
| 4. Proration factor | 12 / 22 | 0.545455 |
| 5. Prorated gross | 3,600.00 x 0.545455 | EUR 1,963.64 |
| 6. Employee social security | 1,963.64 x 13.07% | EUR 256.65 |
| 7. Taxable base | 1,963.64 − 256.65 | EUR 1,706.99 |

The meal voucher entitlement for the month follows the days actually worked (12 days x EUR 10.00 face value, of which EUR 1.09 per day is withheld from the employee's net), and the holiday pay service-year counter is credited with the fraction of the month worked.

Worked example — mid-month termination

The same employee leaves on Friday 17 April 2026. April 2026 has 21 working days after excluding Easter Monday (6 April), which is a paid public holiday and therefore counts as covered. Working days from 1 to 17 April, including Easter Monday, are 13.

Prorated gross = 3,600.00 x 13 / 21 = EUR 2,228.57

The final settlement additionally carries the departure holiday pay of 15.34% of the gross earned (Module 8), any pro rata end-of-year premium under the sectoral CBA, and the notice indemnity if the contract is ended without notice (Module 9).

Legal basis: Employment Contracts Act of 3 July 1978; Wage Protection Act of 12 April 1965; sectoral CBAs per joint committee.

### 4.4 Overtime

#### Detail the statutory rules for overtime, including eligibility criteria and mandatory rates.

The framework is the Labour Act of 16 March 1971.

Normal limits. The standard working time is 38 hours per week on average, with daily and weekly ceilings of 9 hours and 40 hours in the ordinary regime. Sectoral CBAs may organise the 38-hour average over a reference period of up to one year, in which case hours above the weekly schedule inside that period are not overtime.

Overtime supplements.

| When the overtime is worked | Minimum supplement |
| --- | --- |
| Ordinary weekdays and Saturdays | 50% |
| Sundays and public holidays | 100% |

Compensatory rest. As a rule, overtime must be compensated by paid rest so that the average working time is respected over the reference period, and only the supplement is paid in cash. There are two important exceptions in which the overtime is paid in cash without compensatory rest:

Voluntary overtime (vrijwillige overuren), worked at the employee's written request renewable every six months. Until 31 March 2026 the annual quota was 100 hours, extendable to 220 by counting the 120 additional recovery hours. From 1 April 2026 the annual quota per employer rises to 360 hours (450 in the hotel and catering sector), of which the first 240 hours may be paid without an overtime supplement and are exempt from ordinary social security contributions and withholding tax, and 120 hours carry the supplement and the favourable tax regime.

Overtime worked for an extraordinary increase in work or an unforeseen necessity, within the quotas of the Labour Act.

Excluded populations. Employees in a position of trust or with managerial authority, as listed in the Royal Decree of 10 February 1965, are outside the working time rules and are not entitled to overtime pay. Company directors are not employees and are outside the regime entirely.

#### Explain how overtime is treated for income tax and social security calculations.

Social security. Ordinary overtime pay and its supplement are fully subject to the 13.07% employee contribution and to employer contributions. The net overtime hours under the reformed voluntary overtime scheme are the exception: those hours are exempt from ordinary contributions.

Income tax. Overtime that carries a statutory supplement benefits from a two-sided relief, capped at 180 hours per employee per calendar year. The 180-hour ceiling was temporary until 31 December 2025 and has been made permanent from 2026; higher ceilings apply in construction with an electronic attendance system and in the hotel and catering sector with a registered cash register.

| Side | Relief |
| --- | --- |
| Employee | A reduction of the wage withholding tax equal to 66.81% of the gross base used to calculate the supplement, where the supplement is 50% or 100%; 57.75% where the supplement is 20% |
| Employer | An exemption from remitting part of the wage withholding tax on the same base — 41.25% where the supplement is 50% or 100%, 32.19% where it is 20% |

The relief is computed on the base on which the supplement is calculated, not on the supplement itself. It is a withholding relief that is confirmed in the annual assessment, so an employee who exceeds 180 hours has the excess taxed normally.

Overtime paid in a month is not an exceptional payment: it is added to the ordinary monthly remuneration and taxed with it at the ordinary scale, unless it relates to a previous year, in which case it is arrears and follows the exceptional-payment rules of Module 9.2.

Legal basis: Labour Act of 16 March 1971, Articles 19, 20, 25, 26bis and 29; Royal Decree of 10 February 1965; Income Tax Code 1992, Articles 154bis and 275/1; Law of 15 July 2026 reforming personal income tax (Belgian Official Gazette, 29 July 2026), which makes the 180-hour ceiling permanent with retroactive effect from 1 January 2026 and reforms voluntary overtime with effect from 1 April 2026; Royal Decree of 30 July 2026 implementing the précompte-professionnel aspects of that law (Belgian Official Gazette, 30 July 2026). The two effective dates match this Law precisely, which is why the earlier generic citations to a "Programme Law of 2026" and a separate "Law reforming voluntary overtime" have been consolidated into this single 15 July 2026 Law. CONFIRMED 16 September 2026: no distinct Programme Law touches this ceiling. The 180-hour quota is made permanent and retroactive to 1 January 2026 by the personal income tax reform itself, and the voluntary-overtime extension to 240 net hours takes effect from 1 April 2026 under the same reform, so the two effective dates that prompted the earlier generic citations both belong to this Law. The sectoral exceptions are unaffected and remain 280 hours for road and rail works and 360 hours in the horeca sector.

### 4.5 Bonuses

#### Is there a statutory requirement to pay bonuses? If so, how are they calculated?

There is no general statutory obligation to pay a bonus or a thirteenth month. The obligation, where it exists, comes from one of four sources.

| Source | Nature | Typical content |
| --- | --- | --- |
| Sectoral CBA | The most common source of the end-of-year premium | One gross month for joint committee 200; a percentage of annual earnings or a fixed amount in other sectors |
| Company CBA or individual contract | Contractual | Thirteenth or fourteenth month, target bonus |
| CBA no. 90 collective bonus | Optional collective scheme | Tied to measurable, uncertain objectives that are collective, never individual |
| Usage | Repeated, constant, general and fixed payments create an acquired right | Discretionary bonuses can become binding through repetition |

The end-of-year premium under a sectoral CBA is normally calculated on the December gross salary, prorated on the months of service in the reference year, and often requires a minimum period of service and forfeits the premium where the employee resigns before the payment date. Those conditions are strictly sectoral and must be configured per joint committee.

The CBA no. 90 bonus is the only bonus with its own parafiscal regime. It requires a written plan filed with the FPS Employment, objectives that are collective and genuinely uncertain when the plan is filed, and payment to a defined group of employees.

#### Is there a specific tax treatment for bonuses?

Yes. Two distinct regimes apply.

Ordinary bonuses — the end-of-year premium, a target bonus, a thirteenth month — are exceptional remuneration (uitzonderlijke vergoedingen) for withholding purposes. They are subject to the ordinary 13.07% employee contribution and to employer contributions, but the withholding tax is not taken from the monthly scale. It is taken from a fixed percentage table driven by the employee's normal annual gross remuneration, computed as the monthly gross x 13.92 (the factor that reflects twelve months plus holiday pay and end-of-year premium).

| Annual gross reference remuneration | Withholding rate on the exceptional payment |
| --- | --- |
| Up to EUR 10,675.00 | 0.00% |
| EUR 10,675.01 – 13,660.00 | 23.22% |
| EUR 13,660.01 – 17,375.00 | 25.23% |
| EUR 17,375.01 – 20,840.00 | 30.28% |
| EUR 20,840.01 – 23,580.00 | 35.33% |
| EUR 23,580.01 – 26,340.00 | 38.36% |
| EUR 26,340.01 – 31,830.00 | 40.38% |
| EUR 31,830.01 – 34,640.00 | 43.41% |
| EUR 34,640.01 – 45,860.00 | 46.44% |
| EUR 45,860.01 – 59,900.00 | 51.48% |
| Above EUR 59,900.00 | 53.50% |

CBA no. 90 bonuses follow a parallel and more favourable regime, with two different ceilings that must both be configured:

| Ceiling | 2026 amount | Consequence above the ceiling |
| --- | --- | --- |
| Social ceiling | EUR 4,255 | The excess becomes ordinary wage, subject to full employee and employer contributions |
| Tax ceiling | EUR 3,701 | The excess is taxable as exceptional remuneration |

Within the social ceiling the employer pays a special contribution of 33% and the employee a solidarity contribution of 13.07%; within the tax ceiling the bonus is exempt from income tax. The gap between the two ceilings is deliberate: the amount between EUR 3,701 and EUR 4,255 is socially exempt but taxable.

Legal basis: CBA no. 90 of the National Labour Council; Law of 21 December 2007 on the execution of the interprofessional agreement 2007-2008; Annex III to the Royal Decree implementing ITC 92, scale of exceptional remuneration, version applicable from 1 January 2026; sectoral CBAs per joint committee.

### 4.6 Wage Classification (Country-Specific)

#### Are there country-specific classifications for wages critical for social security or tax calculations?

Yes. Four classifications drive the Belgian calculation and none of them can be inferred from the others.

The three wage concepts — the same payment can be wage under one statute and not under another.

Blue-collar versus white-collar (arbeider / bediende) — this survived the unified status reform of 2014 for holiday pay and for the contribution base.

Ordinary versus exceptional remuneration — determines whether the monthly withholding scale or the exceptional-payment table applies.

Worker category and NSSO worker code — determines the contribution rates actually applied in the DmfA.

#### Provide a detailed definition for each classification.

The three wage concepts.

| Concept | Governed by | What it covers | Practical effect |
| --- | --- | --- | --- |
| Wage Protection Act concept | Law of 12 April 1965, Article 2 | Remuneration in money or in money's worth to which the employee is entitled as consideration for work | Determines what must be paid in euro, what may be deducted and the protection against attachment |
| NSSO wage concept | Law of 27 June 1969, Article 14, and Royal Decree of 28 November 1969 | The Wage Protection Act concept, extended to some items and narrowed by the exclusion list | Determines the contribution base |
| Tax wage concept | Income Tax Code 1992, Articles 30 and 31 | All remuneration, benefits in kind and advantages of any kind obtained by reason of the employment | Determines the taxable base |

The concepts overlap but are not identical. The company car is the clearest example: excluded from the NSSO wage concept (replaced by the employer CO2 contribution), but fully taxable as a benefit in kind.

Blue-collar versus white-collar. Since the unified status law of 26 December 2013, notice periods, the waiting day and the guaranteed salary rules are largely aligned. Two differences remain and are decisive for payroll:

Holiday pay for blue-collar workers is paid by the holiday fund and financed by an employer contribution, whereas white-collar holiday pay is paid directly by the employer.

Consequently, the contribution base for blue-collar workers is the gross increased by 8%, and the employer's facial contribution rate is approximately 30.57% rather than approximately 25%.

Ordinary versus exceptional remuneration. Ordinary remuneration is the periodic pay for the period; exceptional remuneration is a payment that does not relate to the ordinary period — the end-of-year premium, the double holiday pay, arrears, a termination indemnity, a bonus. The distinction changes only the withholding calculation, never the social security treatment.

Worker category and worker code. Every employee is declared in the DmfA under a worker code that reflects the applicable scheme (ordinary employee, student with solidarity contribution, flexi-job worker, apprentice, and so on) and an employer category that reflects the sector. These two codes determine which contributions the NSSO calculates.

#### Create a reference table classifying common pay components.

| Pay component | Wage Protection Act | NSSO wage | Taxable | Withholding method |
| --- | --- | --- | --- | --- |
| Basic salary | Yes | Yes | Yes | Ordinary scale |
| Overtime pay and supplement | Yes | Yes | Yes | Ordinary scale, with the 180-hour relief |
| Voluntary net overtime hours (from 1 April 2026, first 240) | Yes | No | No | Exempt |
| Single holiday pay | Yes | Yes | Yes | Ordinary scale |
| Double holiday pay | Yes | Employee contribution only | Yes | Exceptional-payment table |
| End-of-year premium | Yes | Yes | Yes | Exceptional-payment table |
| Commission | Yes | Yes | Yes | Ordinary scale if periodic, exceptional if one-off |
| CBA no. 90 bonus, within ceilings | Yes | Special 33% employer and 13.07% employee contributions | Exempt up to EUR 3,701 | Exempt within the ceiling |
| Meal vouchers, conditions met | Yes | No | No | Not applicable |
| Eco vouchers, conditions met | Yes | No | No | Not applicable |
| Company car private use | Yes | No, replaced by the CO2 contribution | Yes | Ordinary scale, added to the base |
| Bicycle allowance up to EUR 0.37 per km | Yes | No | No | Not applicable |
| Homeworking allowance up to EUR 160.99 per month | No | No | No | Not applicable |
| Genuine expense reimbursement | No | No | No | Not applicable |
| Guaranteed salary during sickness | Yes | Yes | Yes | Ordinary scale |
| Severance or notice indemnity | Yes | Yes | Yes | Average rate of the last normal year |
| Employer supplementary pension premium | No | No, replaced by the 8.86% contribution | No at payment | Not applicable |
| Employee personal pension contribution | Deducted from net | Not applicable | Gives a 30% withholding reduction | Reduction in Annex III |

Legal basis: Wage Protection Act of 12 April 1965, Article 2; Law of 27 June 1969, Article 14; Royal Decree of 28 November 1969, Articles 19 and 19bis; Income Tax Code 1992, Articles 30, 31 and 171; Law of 26 December 2013 on the unified status; NSSO administrative instructions 2026/2.

## Module 5: Social Security & Pension Systems

### 5.1 Contribution Types and Rates

#### List all mandatory social security and pension contributions for both employer and employee.

Belgian employee social security is a single global scheme (globaal beheer): one consolidated contribution is withheld from the employee and one set of employer contributions is paid, and the National Social Security Office then distributes the proceeds across the branches. The employee therefore sees one line on the payslip, not six.

Employee contributions

| Contribution | Rate | Nature |
| --- | --- | --- |
| Global employee social security contribution | 13.07% of gross, uncapped | Covers pensions (7.50%), medical care (3.55%), sickness and disability benefits (1.15%) and unemployment (0.87%) |
| Special social security contribution | Banded on the quarterly wage, maximum EUR 182.82 per quarter for an individually assessed employee | A separate levy created in 1994, withheld monthly and settled through the tax assessment |
| Employee solidarity contribution on a CBA no. 90 bonus | 13.07% | Only on the exempt bonus, in place of ordinary contributions |
| Student solidarity contribution | 2.71% | Replaces the 13.07% for the first 650 hours of student work per year |

Employer contributions

| Contribution | Rate for 2026 | Notes |
| --- | --- | --- |
| Basic employer contribution | 19.88% (pensions 8.86%, medical care 3.80%, sickness and disability benefits 2.35%, unemployment 1.46%, occupational diseases 1.00%, work accidents 0.30%, and the remaining branches) | The facial rate after the tax shift is approximately 25% for white-collar staff |
| Wage moderation contribution | 5.67% of the wage plus 5.67% of the employer contributions due, capped at 7.48%; reduced to 4.27% (maximum 5.12%) for the categories covered by the tax shift | Included in the facial rate |
| Blue-collar uplift | The whole base is the gross at 108%, giving a facial rate of approximately 30.57% | Funds the holiday fund |
| Asbestos fund | 0.01% |  |
| Additional employer contributions for large employers | For example the closure fund contribution, and the 0.10% training contribution where no sectoral agreement exists | Depends on headcount and sector |
| Company car CO2 solidarity contribution | Per vehicle per month, formula in Module 7.2 | Replaces ordinary contributions on the car benefit |
| Special contribution on supplementary pension premiums | 8.86% | On employer premiums to second-pillar schemes |
| Wijninckx contribution on high supplementary pensions | Increased from 3% to 12.5% in 2026 | Due in the fourth quarter |
| Special employer contribution on a CBA no. 90 bonus | 33% | On the exempt bonus |
| Employer contribution on flexi-job wages | 28% | Replaces ordinary contributions |
| Student employer solidarity contribution | 5.42% | First 650 hours per year |
| Sectoral fund contributions | Per joint committee | Collected through the DmfA |

The first pillar pension is inside these contributions — there is no separate pension deduction. Occupational pensions are the second pillar and are contractual, not mandatory, except where a sectoral scheme makes them compulsory for the joint committee.

#### Are contributions managed at a national or sub-national level?

Contributions are set, collected and administered nationally, by the National Social Security Office. Rates are identical across the regions and there is no regional social security contribution.

Two qualifications. First, several target-group reductions of employer contributions (for older workers, for first hires in some configurations, for specific groups) have been regionalised since the sixth state reform, so the reduction available depends on the region in which the establishment unit is located — Flanders, Wallonia, Brussels-Capital and the German-speaking Community each run their own set. The contribution is federal; the reduction may be regional. Second, child benefit is a fully regional competence and is no longer financed through an identifiable employer contribution.

### 5.1.1 Contribution Basis Definition

#### For each mandatory contribution, provide the statutory definition of the earnings base.

| Contribution | Statutory base |
| --- | --- |
| Global employee contribution 13.07% | The wage within the meaning of Article 14 of the Law of 27 June 1969, that is, the Wage Protection Act concept as narrowed by the Royal Decree of 28 November 1969. Uncapped. For blue-collar workers the base is the gross at 108% |
| Employer basic and wage moderation contributions | The same base. From 1 January 2026 the basic and wage moderation contributions are not due on the part of the quarterly wage above EUR 86,700 -- confirmed unchanged at least through mid-2026; the 1 July 2026 change to this measure excludes paid athletes and professional cyclists from combining it with their sport-specific contribution reduction (Programme Law of 30 May 2026, Articles 109-110), rather than raising the threshold |
| Special social security contribution | The gross quarterly wage declared to the NSSO (at 108% for blue-collar workers), banded per fiscal household situation |
| Double holiday pay | Employee contribution of 13.07% is due; employer contributions are not |
| CO2 solidarity contribution | Not a wage-based contribution: it is a flat monthly amount per vehicle, derived from CO2 emissions and fuel type |
| 8.86% supplementary pension contribution | The employer premium or contribution paid to the pension institution |
| Wijninckx contribution | The increase in the pension reserve over the year, where the pension target is exceeded |
| CBA no. 90 bonus contributions | The bonus amount within the social ceiling of EUR 4,255 for 2026 |
| Flexi-job employer contribution 28% | The flexi-wage and the flexi holiday pay |
| Student solidarity contribution | The student's gross wage, for the first 650 hours per calendar year |

#### Clarify the legal definitions of any specific terms used.

Wage (NSSO concept) — remuneration in money or in money's worth to which the employee is entitled as consideration for work performed under the employment contract, as defined in Article 2 of the Wage Protection Act of 12 April 1965 and applied by Article 14 of the Law of 27 June 1969, minus the exclusions of Articles 19 and following of the Royal Decree of 28 November 1969.

Gross at 108% — for blue-collar workers, the declared wage is multiplied by 1.08 before contributions are calculated, because their holiday pay is paid by the holiday fund and not by the employer. This applies to the whole contribution calculation, including the employee's 13.07%.

Facial rate (facial(e) voet) — the headline employer rate quoted in the market (approximately 25% for white-collar staff) after the tax shift consolidation of the basic and wage moderation contributions.

Global management (globaal beheer) — the mechanism under which one consolidated contribution finances all branches, so that a shortfall in one branch is covered from the whole.

Quarterly wage — the sum of the wages declared for the employee in the DmfA for a calendar quarter. This is the base for the special social security contribution and for the high-wage exemption.

Pivot index (spilindex) — the threshold of the smoothed health index whose crossing triggers a 2% increase in social benefits and in public-sector wages, and, through sectoral CBAs, in many private-sector wage scales.

One-caliber wage rule. Belgian social security ceilings and floors are not derived from any published average wage. This must be stated explicitly, because a caliber mismatch is a standard cross-country failure. The figures Belgium publishes and their calibers are:

| Published figure | Caliber | Used for |
| --- | --- | --- |
| Consumer price index | All goods and services | Not used directly in payroll |
| Health index | Consumer price index excluding alcohol, tobacco and motor fuel | Input to the smoothed health index |
| Smoothed health index (afgevlakte gezondheidsindex) | Four-month moving average of the health index | The single caliber that drives wage indexation, the pivot index, the GMMI, the bicycle and homeworking allowances, and the CO2 contribution indexation coefficient |
| Pivot index | A specific level of the smoothed health index | Triggers the 2% step |
| Average gross wage published by Statbel | Statistical only | Not used in any payroll parameter |

Every indexed payroll parameter used in this guide traces back to the smoothed health index, and to no other caliber. Two verifiable derivations confirm it: the GMMI moved from EUR 2,189.81 to EUR 2,233.61 on 1 August 2026, exactly the 2% pivot-index step; and the 2026 CO2 contribution indexation coefficient of 1.6291 is the September 2025 health index (185.85) divided by the September 2004 health index (114.08). There is no parameter in Belgian payroll whose value must be reproduced from an average wage, so no caliber choice arises.

#### Deliverable: Comprehensive summary of current contribution rates, across regions and residential statuses, including tiers, ceilings, floors and variations by age or gender

Ordinary private-sector scheme, 2026

| Branch | Employee | Employer |
| --- | --- | --- |
| Pensions | 7.50% | 8.86% |
| Medical care | 3.55% | 3.80% |
| Sickness and disability benefits | 1.15% | 2.35% |
| Unemployment | 0.87% | 1.46% |
| Occupational diseases | — | 1.00% |
| Work accidents | — | 0.30% |
| Other branches within the basic contribution | — | balance to 19.88% |
| Sub-total | 13.07% | 19.88% |
| Wage moderation | — | 5.67% of wage plus 5.67% of employer contributions, capped at 7.48%; 4.27% (maximum 5.12%) for tax-shift categories |
| Asbestos fund | — | 0.01% |
| Facial rate, white-collar | 13.07% | approximately 25% |
| Facial rate, blue-collar (on the gross at 108%) | 13.07% of the 108% base | approximately 30.57% |

Ceilings, floors and tiers

| Parameter | 2026 value | Applies to |
| --- | --- | --- |
| Contribution ceiling on ordinary contributions | None | Employee and employer contributions are uncapped in principle |
| Exemption on high wages | Quarterly wage above EUR 86,700 from 1 January 2026; confirmed unchanged at least through mid-2026; the 1 July 2026 change to this measure excludes paid athletes and professional cyclists from combining it with their sport-specific contribution reduction (Programme Law of 30 May 2026, Articles 109-110), rather than raising the threshold | Employer basic and wage moderation contributions only. Special contributions and the whole employee contribution remain due on the full wage |
| Special social security contribution, individually assessed employee | Maximum EUR 182.82 per quarter, that is EUR 731.28 per year | Employee |
| Special social security contribution, jointly assessed, spouse has professional income | Maximum EUR 154.92 per quarter, that is EUR 619.68 per year | Employee |
| Special social security contribution, jointly assessed, spouse has no professional income | Maximum EUR 182.82 per quarter, that is EUR 731.28 per year | Employee |
| Social work bonus | Two components with their own limits, maxima and degressive coefficients, stepping five times in 2026 — see the parameter tables and formula below | Employee |

Special social security contribution — quarterly bands, 2026

The contribution has three band tables, one per fiscal household situation. The engine selects the table from the employee's declared household situation; it is not a single scale. All three are stated below, because the tables are genuinely different and cannot be derived from one another — the entry band is 4.22% in the first table and 5.90% in the other two, and the base amount above EUR 6,570.54 differs by EUR 12.33 (EUR 30.99 against EUR 43.32) at every wage.

Table 1 — INDIVIDUALLY ASSESSED EMPLOYEE, 2026 bands per quarter. The employee is assessed individually, that is, is not jointly assessed with a spouse or legal cohabitant.

| Quarterly wage W | Contribution per quarter |
| --- | --- |
| Up to EUR 5,836.14 | Nil |
| EUR 5,836.15 to EUR 6,570.54 | 4.22% x (W − 5,836.14) |
| EUR 6,570.55 to EUR 11,211.00 | EUR 30.99 + 1.10% x (W − 6,570.54) |
| EUR 11,211.01 to EUR 12,300.00 | EUR 82.05 + 3.38% x (W − 11,211.00) |
| EUR 12,300.01 to EUR 18,116.46 | EUR 118.83 + 1.10% x (W − 12,300.00) |
| Above EUR 18,116.46 | EUR 182.82 (maximum) |

Table 2 — JOINTLY ASSESSED EMPLOYEE, SPOUSE WITH PROFESSIONAL INCOME, 2026 bands per quarter.

| Quarterly wage W | Contribution per quarter |
| --- | --- |
| Up to EUR 3,285.28 | Nil |
| EUR 3,285.29 to EUR 5,836.14 | EUR 15.45 (a fixed amount, not a percentage) |
| EUR 5,836.15 to EUR 6,570.54 | 5.90% x (W − 5,836.14), with a minimum of EUR 15.45 |
| Above EUR 6,570.54 | EUR 43.32 + 1.10% x (W − 6,570.54), capped at EUR 154.92 |

The cap of EUR 154.92 is reached at a quarterly wage of EUR 16,715.99 and applies above it. This table has no 3.38% band: the 1.10% rate runs unbroken from EUR 6,570.54 to the cap.

Table 3 — JOINTLY ASSESSED EMPLOYEE, SPOUSE WITHOUT PROFESSIONAL INCOME, 2026 bands per quarter.

| Quarterly wage W | Contribution per quarter |
| --- | --- |
| Up to EUR 5,836.14 | Nil |
| EUR 5,836.15 to EUR 6,570.54 | 5.90% x (W − 5,836.14) |
| Above EUR 6,570.54 | EUR 43.32 + 1.10% x (W − 6,570.54), capped at EUR 182.82 |

The cap of EUR 182.82 is reached at a quarterly wage of EUR 19,252.36 and applies above it. This table has no 3.38% band and, unlike Table 2, no fixed EUR 15.45 amount in the low band — an employee in this situation pays nothing until the quarterly wage reaches EUR 5,836.15.

Three warnings that follow directly from the three tables:

The maximum of EUR 182.82 belongs to two different situations — Table 1 and Table 3 — which are otherwise unlike each other at every wage below the cap. Matching on the maximum alone will select the wrong table.

The fixed EUR 15.45 amount exists only in Table 2. It is not a general low-band withholding and must not be applied under Tables 1 or 3.

The band joins are the published statutory constants and are not exactly reproducible from the preceding band: 4.22% x (6,570.54 − 5,836.14) = 30.99 exactly, but 5.90% x (6,570.54 − 5,836.14) = 43.33 against a published base of 43.32, and 30.99 + 1.10% x (11,211.00 − 6,570.54) = 82.03 against a published base of 82.05. Use the published constants, not a recomputation, or the bands will not join.

A legislative reform progressively reducing and eventually abolishing this contribution is confirmed to be underway. The exact phase-in percentages and the precise year of conversion to a genuinely individual levy are NOT independently confirmed against a primary source in this review and must be checked before the Wage Type Catalogue build depends on them - do not carry a specific 'reduced from X%' figure forward without that check.

Social work bonus — parameters and formula, 2026

The social work bonus (werkbonus / bonus à l'emploi) reduces the employee social security contribution for low wages. Since 1 April 2024 it has two components, each with its own full-amount limit, its own maximum and its own degressive coefficient:

Component B — the very low wage component;

Component A — the low wage component.

The two are computed separately and added. Component B's degressive band ends exactly where component A's full-amount limit sits, so the two dovetail.

S = the reference monthly wage at 100%, full-time equivalent.

For blue-collar workers S is the wage at 100%, NOT the 108%

contribution base. The wage limits are therefore identical for

blue-collar and white-collar workers; only the maxima differ,

the blue-collar maxima being the white-collar maxima x 1.08,

because the contribution itself is computed on the 108% base.

Component B    S <= S_B            ->  R_B = maximum B

S_B < S <= S_A      ->  R_B = maximum B - (coefficient B x (S - S_B))

S > S_A             ->  R_B = 0.00

Component A    S <= S_A            ->  R_A = maximum A

S_A < S <= S_zero   ->  R_A = maximum A - (coefficient A x (S - S_A))

S > S_zero          ->  R_A = 0.00

Social work bonus P = R_B + R_A

P is capped at the employee social security contribution actually

due for the period and can never make it negative.

Where the services are incomplete or the employee is part-time,

P is prorated by (H/U) or (J/D), the ratio being capped at 1.00.

Component B parameters, 2026

| Effective from | Full amount up to S_B | Maximum B, white-collar | Maximum B, blue-collar | Coefficient B, white-collar | Coefficient B, blue-collar | B reaches zero at S_A |
| --- | --- | --- | --- | --- | --- | --- |
| 1 January 2026 | EUR 2,218.73 | EUR 165.87 | EUR 179.14 | 0.2699 | 0.2915 | EUR 2,833.36 |
| 1 March 2026 | EUR 2,218.73 | EUR 165.87 | EUR 179.14 | 0.2699 | 0.2915 | EUR 2,833.36 |
| 1 April 2026 | EUR 2,255.50 | EUR 168.62 | EUR 182.11 | 0.2699 | 0.2915 | EUR 2,880.32 |
| 1 July 2026 | EUR 2,300.62 | EUR 171.99 | EUR 185.75 | 0.2699 | 0.2915 | EUR 2,937.93 |
| 1 September 2026 | EUR 2,300.62 | EUR 171.99 | EUR 185.75 | 0.2699 | 0.2915 | EUR 2,937.93 |

Component A parameters, 2026

| Effective from | Full amount up to S_A | Maximum A, white-collar | Maximum A, blue-collar | Coefficient A, white-collar | Coefficient A, blue-collar | A reaches zero at S_zero |
| --- | --- | --- | --- | --- | --- | --- |
| 1 January 2026 | EUR 2,833.36 | EUR 123.00 | EUR 132.84 | 0.2807 | 0.3032 | EUR 3,271.48 |
| 1 March 2026 | EUR 2,833.36 | EUR 123.00 | EUR 132.84 | 0.2442 | 0.2638 | EUR 3,336.98 |
| 1 April 2026 | EUR 2,880.32 | EUR 125.04 | EUR 135.04 | 0.2738 | 0.2957 | EUR 3,336.98 |
| 1 July 2026 | EUR 2,937.93 | EUR 127.54 | EUR 137.74 | 0.3196 | 0.3452 | EUR 3,336.98 |
| 1 September 2026 | EUR 2,937.93 | EUR 127.54 | EUR 137.74 | 0.2739 | 0.2958 | EUR 3,403.62 |

The parameter set steps five times inside income year 2026 — 1 January, 1 March, 1 April, 1 July and 1 September — and two of those steps move the coefficient without moving the maximum. The 1 March and 1 September steps raise the point at which component A reaches zero (to EUR 3,336.98 and then to EUR 3,403.62) by flattening the coefficient while the maximum is unchanged; the 1 April and 1 July steps are indexations of the amounts. Select the parameter row by the pay month, not by the year.

How to read the two limits. The full-amount limit is the lower limit: the maximum applies only at or below it. Between the full-amount limit and the point at which the component reaches zero, the degressive formula applies. Above that point the component is nil. The published zero point governs; the coefficients are stated to four decimals and reproduce it to within a few cents.

Correction of record. An earlier reading of this guide instructed the engine to grant the bonus wherever the reference wage was below the upper limit, which would hand the full maximum to an employee just under EUR 3,403.62. That is wrong. The full maximum is granted only at or below the lower (full-amount) limit; the band between the two limits is degressive. The worked examples in Module 12 that apply the maximum only below the lower limit are the correct reading.

Annual cap on the social work bonus. The total reduction per employee is capped at EUR 3,466.44 per calendar year from 1 January 2026 and EUR 3,523.92 from 1 April 2026. EUR 3,594.36 from 1 July 2026. CLOSED 16 September 2026. The January figure comes from the NSSO administrative instructions edition 2026/1 and the April figure from edition 2026/2; the July figure was left open at build time, with an explicit instruction not to extrapolate it, until the edition covering the third quarter of 2026 appeared. It has: edition 2026/3 states "het totaal van de vermindering per werknemer niet meer bedragen dan 3.594,36 EUR per kalenderjaar" (the werkbonus annex). The figure was taken from that instruction and not extrapolated, and it reconciles exactly against the component maxima in force from the same date: EUR 171.99 plus EUR 127.54 is EUR 299.53 a month white-collar, and twelve times that is EUR 3,594.36, so the annual cap and the monthly parameters now agree independently.

CLOSED — the Module 12 worked examples now apply both components. Examples 2, 4 and 6 previously granted only EUR 127.54 (white-collar) or EUR 137.74 (blue-collar) and described it as "the maximum". Those are the component A maxima, and under the two-component formula above an employee below the component B limit also receives component B, so the three examples understated the bonus. All three have been recomputed on the parameters in force from 1 July 2026, together with every figure downstream of the bonus — taxable base, withholding, the derived fiscal work bonus and net pay. The resulting bonuses are: Example 2, EUR 171.99 + EUR 127.54 = EUR 299.53 full-time equivalent, EUR 179.72 after proration at 60%, capped at the EUR 169.91 of contribution actually due; Example 4, EUR 37.21 + EUR 127.54 = EUR 164.75; Example 6, EUR 80.99 + EUR 137.74 = EUR 218.73. Note the knock-on to the fiscal work bonus, which is a percentage of the social work bonus granted (Module 7): it rises to EUR 741.84 per year in Example 4 and, in Example 6, to a derived EUR 1,058.40 that the EUR 765.00 annual cap cuts back.

Correction of record — the establishing instrument. Earlier editions of this guide cited Programme Law (I) of 24 December 2002, Article 353bis as the legal basis of the social work bonus. That is the wrong instrument. Article 353bis sits in Title IV, Chapter 7, Section 3bis of that Programme Law and governs the continuation of the employer-side target-group reduction where the employer is restructured or legally transformed; it was inserted by Article 200 of the Law of 22 December 2008 with effect from 1 January 2009 and says nothing about the employee's own contribution. The social work bonus is a reduction of the personal social security contribution and rests on the Law of 20 December 1999 and its implementing Royal Decree of 17 January 2000, cited in full below.

Legal basis: Law of 20 December 1999 granting a work bonus in the form of a reduction of the personal social security contributions of employees with low wages, of certain employees who were the victims of a restructuring and of paid sportspeople, Article 2 — the enabling provision; Royal Decree of 17 January 2000 implementing that Article 2 (BS 28 January 2000, numac 2000022082), which carries the formula and the parameters, as amended for the structure described above by the Royal Decree of 27 March 2023 (BS 12 April 2023, erratum BS 21 April 2023, in force 1 July 2023), which inserted the additional very-low-wage threshold, and by the Royal Decree of 5 March 2024 (BS 18 March 2024, in force 1 April 2024), which split the reduction into the two components used above and expressed each maximum as a percentage of the GMMI; CBA no. 43 of the National Labour Council, which sets the GMMI the decrees refer to; NSSO administrative instructions editions 2026/1 and 2026/2, the work bonus annex.

No 2026 instrument sets the 2026 figures, and none was found in the Belgian Official Gazette. Each 2026 step follows parametrically from the decrees above: the maxima and the full-amount limits are fixed percentages of the GMMI (the Royal Decree of 5 March 2024 sets them at 5.71% and 7.70% of it, the Royal Decree of 27 March 2023 sets the component A full-amount limit at 131.5328% of it), so they move when the GMMI moves; the upper limit is indexed on the social-benefit calendar, which is why it steps on 1 March and 1 September while the GMMI does not. The published NSSO figures are therefore the operative source for the values, and the decrees for the mechanism.

Variation by residential status

| Status | Social security treatment |
| --- | --- |
| Resident employee working in Belgium | Full Belgian scheme |
| Non-resident employee working in Belgium | Full Belgian scheme — social security follows the place of work, not tax residence |
| Employee posted to Belgium with an A1 certificate | Exempt from Belgian contributions; remains in the home scheme (Regulation (EC) 883/2004 or a bilateral agreement) |
| Employee working in several Member States | Applicable legislation determined under Article 13 of Regulation (EC) 883/2004; the 25% substantial-activity test applies |
| Inbound taxpayer under the special tax regime | The tax regime does not change the social security position; Belgian contributions remain due unless an A1 says otherwise |

Variation by age or gender

There is none for the ordinary contributions: rates do not vary by age or by gender. Age enters only through separate schemes and reductions — the student solidarity contribution for students, apprenticeship arrangements for young workers, and the regional target-group reductions for older workers.

Legal basis: Law of 27 June 1969, Articles 14, 23 and 38; Royal Decree of 28 November 1969, Articles 19 and following; Law of 30 March 1994 (special social security contribution), Article 106; Programme Law introducing the exemption on high wages with effect from 1 January 2026; NSSO administrative instructions 2026/2; Regulation (EC) 883/2004.

### 5.2 Calculation Logic and Edge Cases

#### What is the step-by-step calculation logic for all types of social security contributions?

Determine the worker category and the NSSO worker code — ordinary employee, blue-collar or white-collar, student, flexi-job worker, apprentice. This selects the rate set.

Build the contribution base for the quarter: sum all wage elements included in the NSSO wage concept. For blue-collar workers, multiply by 1.08.

Calculate the employee contribution: base x 13.07%.

Apply the social work bonus using the two-component formula and the dated parameter tables in Module 5.1.1. Select the parameter row by the pay month, compute component B and component A separately, and add them. Each component pays its maximum only at or below its own full-amount (lower) limit, pays a degressive amount between that limit and the point at which it reaches zero, and pays nothing above that point. The bonus reduces the employee contribution and can never make it negative; it is prorated for incomplete or part-time services and is subject to the annual cap.

Calculate the employer basic and wage moderation contributions on the same base, applying the high-wage exemption to the part of the quarterly wage above EUR 86,700 (confirmed unchanged at least through mid-2026; the 1 July 2026 change to this measure excludes paid athletes and professional cyclists from combining it with their sport-specific contribution reduction (Programme Law of 30 May 2026, Articles 109-110), rather than raising the threshold).

Apply the structural reduction and any target-group reduction, which reduce the employer contribution, not the employee contribution.

Add the special contributions: CO2 solidarity contribution per vehicle, 8.86% on supplementary pension premiums, 33% on CBA no. 90 bonuses, sectoral fund contributions, the Wijninckx contribution in Q4.

Calculate the special social security contribution by first selecting which of the three quarterly band tables in Module 5.1.1 applies to the employee's fiscal household situation — individually assessed (Table 1), jointly assessed with a spouse having professional income (Table 2), or jointly assessed with a spouse having no professional income (Table 3) — then applying that table's bands. The three tables differ in their entry rate, their base amounts and their maximum; two of them share the maximum of EUR 182.82, so the situation, not the maximum, selects the table. Withhold provisionally in months 1 and 2 and correct at the last pay of the quarter.

Declare in the DmfA per employee, per worker code, per occupation line, with the days and hours, by the last day of the month following the quarter.

Pay: monthly advances by the 5th day following each month where the K-2 threshold of EUR 6,197.34 was exceeded, and the balance by the DmfA deadline.

#### Are contributions based on actual or standard salary?

On actual salary. Belgium does not use notional, standard or class-based earnings for employee contributions. Three narrow exceptions exist:

Blue-collar workers — the actual gross is uplifted by 8%, a fixed statutory factor rather than a notional wage.

Fictitious wage for equivalent days — periods of inactivity treated as equivalent for holiday purposes are valued at a fictitious wage when computing holiday pay, not when computing ordinary contributions.

Benefits in kind with a flat statutory value — the company car benefit and the flat values for free meals or housing are fixed amounts, but these feed the tax base rather than the ordinary contribution base.

#### Describe rules for eligibility, joining month, termination month, mid-period hires, mid-period terminations, and mid-period salary changes.

| Event | Rule |
| --- | --- |
| Eligibility | Liability starts on the first day of actual work under an employment contract, evidenced by the Dimona declaration. There is no waiting period and no minimum age or minimum earnings threshold |
| Joining month | Contributions are due on the wage actually earned from the start date. No monthly minimum applies; a person who works one day owes contributions on one day of pay |
| Termination month | Contributions are due on the wage earned up to the last day of the contract, plus on the termination indemnity and on the departure holiday pay |
| Mid-period hire | Purely proportional — the contribution follows the prorated wage. There is no rounding up to a full month |
| Mid-period termination | Same. The final settlement (departure holiday pay, pro rata end-of-year premium, notice indemnity) is included in the quarter in which it is paid |
| Mid-period salary change | The contribution follows the wage actually paid in the period, so the change takes effect immediately. No recalculation of earlier periods is required unless the change is retroactive, in which case the arrears are declared in the quarter to which they relate through a DmfA correction |

Because the special social security contribution and the high-wage exemption are computed on the quarterly total, a mid-quarter hire, termination or salary change changes the quarterly total and therefore the band. The engine must recompute both at the last pay of the quarter rather than treating them as monthly-final.

#### Do different payment frequencies affect contribution rates or parameters?

No. Rates are identical whether the employee is paid weekly, twice monthly or monthly, and there is no ceiling that a frequency could interact with. Two parameters are frequency-sensitive only in their timing:

the special social security contribution, because it is banded on the quarterly total and the provisional monthly withholding must be trued up at the last payment of the quarter;

the social work bonus, which is expressed as a monthly maximum and must be prorated where the reference period is not a full month.

#### Detail variations based on employee age or gender.

There are no rate variations by age or by gender. All employees pay 13.07% and all employers pay the same facial rate, regardless of age or gender.

Age-related variation arises only through separate schemes:

| Population | Treatment |
| --- | --- |
| Students, first 650 hours per calendar year | Solidarity contribution of 2.71% employee and 5.42% employer, in place of ordinary contributions. From the 651st hour, ordinary rates apply |
| Apprentices and pupils in alternating training | Reduced or nil contributions until the end of the year in which they turn 18, per the specific scheme |
| Older workers | No rate change; regional target-group reductions of employer contributions may apply |
| Employees who have reached statutory pension age but continue working | Ordinary contributions remain due |

Gender enters payroll only through maternity protection, which is a benefit paid by the health insurance fund, not a contribution difference.

#### Is there a minimum number of working days required for contributions?

No. There is no minimum number of days, no minimum number of hours and no minimum earnings threshold for liability. One hour of work under an employment contract creates a full contribution obligation on the wage for that hour.

Minimum-duration rules exist elsewhere in the system and must not be confused with contribution liability: the guaranteed average minimum monthly income applies to contracts of at least one month, and certain part-time arrangements have minimum weekly durations under the Labour Act, but neither affects whether contributions are due.

#### How are contributions calculated for Board of Directors who are also employees?

The default position is that a company director (bestuurder / administrateur) exercising a mandate is self-employed, not an employee, and falls under the self-employed social security scheme administered by a social insurance fund. The director's remuneration is then outside the DmfA entirely and outside this payroll scope.

A director can hold an employee contract in parallel, but only where the two functions are genuinely distinct and the employed function is exercised under the authority of the company. Where that is accepted:

The employed function is declared in the DmfA and attracts the ordinary employee and employer contributions on the wage for that function.

The director's mandate remains self-employed, with quarterly contributions paid by the director to a social insurance fund. It never enters payroll.

A director who is a majority shareholder or who effectively controls the company will normally fail the subordination test, and the tax and social security administrations will requalify an employment contract in those circumstances.

The practical configuration rule: a director on the payroll must have a wage type set restricted to the employed function, and the director's fee must be excluded from the DmfA and from the 281.10 (director's fees are reported on form 281.20).

#### Are year-end adjustments required?

No annual reconciliation of the ordinary contributions is required, because there is no annual ceiling to true up. Four year-end or quarter-end actions are nevertheless required.

| Action | When |
| --- | --- |
| True-up of the special social security contribution | At the last payment of each quarter, once the quarterly wage is final |
| Wijninckx contribution on high supplementary pensions | Declared and paid in the fourth-quarter DmfA |
| DmfA corrections for retroactive wage changes | In the quarter to which the wage relates, by a corrective declaration |
| Reconciliation of the four DmfA declarations against the payroll ledger and the 281.10 certificates | Before the 28 February Belcotax deadline |

Legal basis: Law of 27 June 1969, Articles 14, 21, 23 and 38; Royal Decree of 28 November 1969; Royal Decree of 5 November 2002 (Dimona); NSSO administrative instructions 2026/2; Royal Decree no. 38 of 27 July 1967 (self-employed social security).

### 5.3 Voluntary Contributions & Private Schemes

#### Can employees and employers make additional voluntary contributions?

The first pillar is closed to voluntary contributions through payroll: an employee cannot pay more than 13.07% and an employer cannot pay more than the statutory rates to obtain a better statutory pension. Voluntary continued insurance exists in narrow situations (for example the continuation of pension insurance during certain periods of inactivity) but is arranged directly between the individual and the institution, outside payroll.

Additional provision is made through the second and third pillars.

| Pillar | Vehicle | Employer role | Employee role |
| --- | --- | --- | --- |
| Second | Occupational pension plan (group insurance or pension fund), sectoral or company-level | Pays the premium; owes 8.86% and the 4.4% insurance premium tax | May pay a personal contribution where the plan provides for it, withheld from net pay |
| Second | Sectoral pension scheme | Compulsory where the joint committee has established one | Usually no personal contribution |
| Third | Individual pension saving and long-term saving | None | Paid privately; claimed in the tax return, not through payroll |

#### Which employee contributions are allowed as pre-tax deductions?

Only the statutory employee social security contribution of 13.07% is a genuine pre-tax deduction: it is subtracted from the gross before the taxable base is determined.

Everything else that reduces the employee's tax operates as a reduction of the withholding, not as a reduction of the base:

| Item | Mechanism |
| --- | --- |
| Employee social security contribution 13.07% | Deducted from the gross to form the taxable base |
| Personal contribution to the employer's supplementary pension plan | Withheld from net pay; generates a reduction of the wage withholding tax equal to 30% of the contribution, applied under Annex III |
| Fiscal work bonus | A direct reduction of the withholding for employees receiving the social work bonus |
| Overtime relief | A reduction of the withholding on up to 180 hours per year |
| Special social security contribution | Not deductible from the taxable base and gives no reduction |
| Trade union contributions, third-pillar pension saving | Not handled in payroll |

#### Are there private insurance schemes with employer and employee contributions?

Yes, and they are widespread. The main ones a Belgian payroll must be able to carry:

| Scheme | Employer side | Employee side | Payroll treatment |
| --- | --- | --- | --- |
| Group insurance or pension fund (second pillar) | Premium, plus 8.86% NSSO contribution and 4.4% insurance premium tax | Optional personal contribution | Employer premium is not wage; personal contribution is withheld from net and gives the 30% withholding reduction |
| Hospitalisation insurance | Premium, commonly fully employer-paid | Optional cover for family members | Employer premium for the employee is exempt from contributions and tax where the policy meets the conditions; family cover paid by the employee is withheld from net |
| Guaranteed income insurance (disability top-up) | Premium | Optional | Treated with the pension plan where it is an accessory cover |
| Work accident insurance | Compulsory premium | None | Employer cost only; never a payroll deduction |
| Sectoral supplementary pension | Contribution through the DmfA | None | Collected by the NSSO and forwarded to the sector |

The Wijninckx contribution applies where the total supplementary pension provision for an employee exceeds the pension target; it rose from 3% to 12.5% in 2026 and is calculated as 12.5% of the increase in the pension reserve between 1 January 2025 and 1 January 2026, declared in the fourth-quarter DmfA.

#### What documents or declarations are required from an employee?

| Document | Purpose | When |
| --- | --- | --- |
| Affiliation form for the supplementary pension plan | Affiliation and beneficiary designation | On entry into the plan |
| Consent to the personal contribution | Authorises the deduction from net pay | On affiliation |
| Health questionnaire, where the insurer requires one | Underwriting of death or disability cover | On affiliation |
| Declaration of family members for hospitalisation cover | Determines the premium withheld from net | On affiliation and on change |
| Statement of dependants and family situation | Determines the withholding scale and the reductions | On hire and on change |
| A1 certificate | Proves affiliation to another Member State's scheme | Before the assignment starts |
| Holiday certificate from the previous employer | Needed for holiday pay and the departure holiday pay offset | On hire |

Legal basis: Law of 28 April 2003 on supplementary pensions; Programme Law of 22 June 2012 (Wijninckx contribution) as amended for 2026; Income Tax Code 1992, Articles 1451 and 1453; Annex III to the Royal Decree implementing ITC 92; Law of 10 April 1971 on occupational accidents; NSSO administrative instructions 2026/2.

## Module 6: Income Tax Withholding System

Resident versus non-resident treatment matrix (control B1). This matrix is the reference for every rule stated in the rest of this module. No cell is left empty: where a treatment is out of payroll scope, the reason is given.

| Income type | Resident — rate, method and base | Non-resident — rate, method and base |
| --- | --- | --- |
| Regular salary | Withholding under scale I or II of Annex III, on the gross less the 13.07% employee contribution, annualised then divided back; full tax-free allowance of EUR 11,170 and family reductions | Withholding under scale I or II where Belgian professional income is at least 75% of total professional income or the employee works at least 75% of contractual time in Belgium; otherwise scale III, which grants no personal or family allowance. Same base and same annualisation |
| Annual or thirteenth-month bonus, end-of-year premium | Exceptional-remuneration table, 0% to 53.50% by reference to the normal annual gross remuneration | Same table and same percentages. Under scale III no family reduction is applied afterwards |
| Double holiday pay | Separate holiday-pay table, 0% to 53.50% | Same table |
| Severance and notice indemnity | Taxed separately at the average rate of the last previous year of normal professional activity (ITC 92, Article 171); withheld at the Annex III nr. 58 arrears-and-severance percentage (0.00% to 48.00%), to which nr. 62 routes notice indemnities — not at the nr. 53 exceptional-payment percentage, which excludes them in terms | Same separate taxation; Belgium retains taxing rights over the part relating to Belgian employment, subject to the applicable double tax treaty |
| Equity and share incentives | Stock options accepted in writing within 60 days of the offer are taxed at grant as a benefit in kind, valued at a flat 18% of the underlying share value (9% where the plan meets the conditions of the Law of 26 March 1999), increased by 1 percentage point (0.5 percentage point under the reduced 9% rate) per year or part-year of the exercise period beyond 5 years from the offer -- not doubled. Withholding applies; no social security | Same domestic rule where the benefit relates to Belgian employment. Treaty allocation by reference to the period of employment between grant and vesting |
| Labour-service or contractor pay | Not employment income. No wage withholding; the self-employed person invoices and pays their own tax and social contributions | Withholding tax of 30% may apply on certain payments to non-resident service providers under Article 228 ITC 92; out of payroll scope, handled by accounts payable |
| Benefits in kind (company car, housing, free electricity) | Added to the taxable base at their statutory or actual value and taxed at the ordinary scale | Identical valuation; taxed at the ordinary scale under the applicable scale (I, II or III) |
| Directors' fees | Not employment income. Reported on form 281.20; withholding applies to resident directors under the specific rules | Withholding on non-resident directors' fees under Article 228; out of payroll scope for employed populations |

### 6.1 System Overview and Methodology

#### Describe the country's income tax withholding system.

Belgium operates a pay-as-you-earn withholding at source called the bedrijfsvoorheffing (wage withholding tax). Its defining characteristics are:

It is a payment on account, not a final tax. The definitive liability is established when the individual files the annual personal income tax return; the withholding is credited against the assessment and the difference is refunded or collected.

It is non-cumulative. Each payment is taxed as though it were the employee's only income; the employer does not carry a year-to-date tax position and does not true up in December. This is the single most important structural difference from cumulative systems.

It is calculated per payment, by annualisation. The periodic taxable amount is grossed up to an annual figure, the annual tax is computed on the scale, and the result is divided back to the period.

It approximates the final burden, including the regional and municipal surcharges, by applying rates that are the personal income tax rates increased by a notional 7% — 25% becomes 26.75%, 40% becomes 42.80%, 45% becomes 48.15% and 50% becomes 53.50%.

Exceptional payments are carved out and taxed at a single percentage from a separate table, so that a bonus does not distort the monthly calculation.

The rules are contained in Annex III to the Royal Decree implementing ITC 92, republished each year. The 2026 version was enacted by the Royal Decree of 11 December 2025, published in the Belgian Official Gazette of 29 December 2025 and in force from 1 January 2026. Two July 2026 texts amend this baseline within the same tax year: the Law of 15 July 2026 reforming personal income tax (Belgian Official Gazette, 29 July 2026), and the Royal Decree of 30 July 2026 amending the précompte-professionnel application rules in partial execution of that law (Belgian Official Gazette, 30 July 2026). Only three effects reach the withholding stage in 2026 rather than waiting for the year-end assessment: the fiscal work bonus enhancement for very low salaries (from 1 August 2026 — see Module 6.3, Fiscal work bonus), the 180-hour overtime-quota tax advantage being made permanent (retroactive to 1 January 2026 — see Module 4.4), and the voluntary-overtime exemption (retroactive to 1 April 2026 — see Module 4.4).

#### What types of taxes are withheld by the employer?

| Levy | Nature | Withheld by the employer? |
| --- | --- | --- |
| Wage withholding tax (bedrijfsvoorheffing) | Advance payment of personal income tax; the Annex III scales embed a notional surcharge component standing in for the commune-specific rate, which is why the withholding rarely matches the final assessment exactly | Yes |
| Regional personal income tax surcharge | Regional additional percentage on federal tax | No — settled at the annual assessment; only approximated inside the withholding |
| Municipal tax (0% to approximately 9% depending on the commune) | Local additional percentage on federal tax | No — settled at the annual assessment; only approximated inside the withholding |
| Special social security contribution | A social levy administered alongside tax and settled through the tax assessment | Yes, as a separate line |
| Withholding on directors' fees and on payments to non-residents | Separate withholding regimes | Not in payroll scope; handled by accounts payable |

There is no employer-level payroll tax on the wage bill in Belgium. Employer cost is entirely social security and contractual.

#### At what level are tax rates published (central or state)?

Centrally, by the Federal Public Service Finance. The personal income tax scale, the tax-free allowance, the family reductions and the entire Annex III withholding mechanism are federal. The FPS Finance publishes each year, at the same time, the rules text, the key formula (sleutelformule), the withholding scales and an official simulator.

Regions set their own surcharge percentages and municipalities set their own municipal tax rate, but neither is published as a payroll withholding rate and neither is applied at source. Payroll therefore reads exactly one published rate set: the federal Annex III.

### 6.1.1 Taxable Income Definition

#### Provide the statutory definition of 'Taxable Income'.

Article 31 of ITC 92 defines employment income (bezoldigingen van werknemers) as all remuneration obtained by an employee by reason of or on the occasion of the employment, whatever its form or denomination. It expressly includes salaries, wages, commissions, gratuities, premiums, benefits obtained by reason of the employment, holiday pay, and indemnities that are the consequence of the termination of the employment or of the loss of remuneration.

Article 30 places this income in the general category of professional income, and Article 52, 3° makes the compulsory employee social security contribution a deductible professional expense — which is why the withholding base is the gross after the 13.07% deduction.

#### Explain how this base is derived from total gross earnings.

Total gross earnings for the period

−  Employee social security contribution (13.07%), after the social work bonus

=  Gross taxable remuneration

+  Taxable benefits in kind not subject to social security

(company car benefit, free housing, free electricity and heating)

−  Statutorily exempt items

(bicycle allowance up to EUR 0.37/km and EUR 3,700/year,

homeworking allowance up to EUR 160.99/month,

meal and eco vouchers meeting their conditions,

genuine expenses proper to the employer,

CBA no. 90 bonus up to EUR 3,701)

=  TAXABLE BASE for the withholding calculation

The special social security contribution is not deductible from this base, and neither is the employee's personal contribution to a supplementary pension plan — the latter is relieved through a 30% reduction of the withholding rather than through the base.

#### Deliverable: Step-by-step decision guide to determine the correct tax schedule for an employee

START

|

1. Is the individual a Belgian resident (domicile or seat of wealth in Belgium,

or presumed so by entry in the National Register)?

YES -> go to 3

NO  -> go to 2

|

2. Does the non-resident earn at least 75% of total professional income in

Belgium, or work at least 75% of contractual working time in Belgium?

YES -> treat as if resident for the choice of scale; go to 3

NO  -> SCALE III. No tax-free allowance, no family reduction. STOP

|

3. Does the employee have a spouse or legal cohabitant?

NO  -> SCALE I

YES -> go to 4

|

4. Does the spouse have own professional income above the statutory threshold?

YES -> SCALE I (each spouse taxed on own income)

NO  -> SCALE II (the marital quotient is anticipated in the withholding)

|

5. Apply the reductions on top of the chosen scale:

- basic tax-free allowance EUR 11,170 (income year 2026), granted

as a reduction of EUR 2,987.98 (= 11,170 x 26.75%)

- dependent children: a SEPARATE flat euro reduction of the

basisbelasting, not an increase of the allowance —

EUR 624 for one child, EUR 1,656 for two, EUR 4,404 for three,

rising further beyond (Annex III nr. 38)

- disabled employee, disabled dependants, single parent

- fiscal work bonus where the social work bonus applies

- 30% of any personal supplementary pension contribution

- overtime relief on up to 180 hours per year

|

6. Is the payment exceptional (bonus, end-of-year premium, double holiday

pay, arrears, termination indemnity)?

YES -> do not use the scale. Use the exceptional-payment or

holiday-pay percentage table, keyed on the normal annual

gross remuneration

NO  -> use the scale

END

#### Deliverable: Explain the official tax calculation method with formulas and examples

Formula for ordinary monthly remuneration, income year 2026

Step 1  A = monthly gross taxable remuneration

Step 2  B = A − employee social security contribution (13.07% of gross)

Step 3  C = B x 12                            (annualisation)

Step 4  D = lump-sum professional expenses

= 30% of C, capped at EUR 6,070

Step 5  E = C − D                             (annual net taxable income)

Step 6  F = tax on E using the Annex III nr. 31 withholding base scale,

which has its OWN ceilings, distinct from the assessment

brackets of Article 130 ITC 92:

0.01 –  16,710   26.75%

16,710 –  29,500    4,469.93 + 42.80% on the slice above 16,710

29,500 –  51,050    9,944.05 + 48.15% on the slice above 29,500

above   51,050   20,320.38 + 53.50% on the slice above 51,050

Step 7  G = reduction for the basic tax-free allowance

= 26.75% x 11,170 = EUR 2,987.98

F − G = the BASISBELASTING

Step 8  K = reduction for dependent children — a SEPARATE flat euro

amount deducted from the basisbelasting (Annex III nr. 38),

not a supplement to the tax-free allowance:

1 child      624        5 children   11,100

2 children 1,656        6 children   14,592

3 children 4,404        7 children   18,120

4 children 7,620        8 children   21,996

more than 8: 21,996 + 3,864 per child above the eighth.

A disabled dependent child counts as two (Annex III nr. 8).

Step 9  H = other reductions (fiscal work bonus, 30% of the personal

pension contribution, overtime relief, other Annex III items)

Step 10 Annual withholding = F − G − K − H, floored at zero

Step 11 Monthly withholding = annual withholding / 12, rounded to the cent

Every amount is rounded to the eurocent at each step, half-up, as Annex III nr. 12 requires.

The scale percentages are the personal income tax rates of 25%, 40%, 45% and 50% increased by 7%, which is how the withholding anticipates the regional and municipal surcharges.

Two tax-free allowance figures are in circulation for income year 2026 — EUR 11,170 and EUR 11,550 — and only EUR 11,170 belongs in this calculation. They are amounts of two different instruments, governing two different stages of the same tax. EUR 11,170 is the withholding allowance of Annex III nr. 32, and it is the amount step G applies to the monthly bedrijfsvoorheffing. EUR 11,550 is the assessment allowance of Article 131 ITC 92 as amended by the Law of 15 July 2026 reforming the personal income tax (Belgian Official Gazette 29 July 2026), which the tax authority applies to the employee's annual tax return for assessment year 2027. That law raised the non-indexed Article 131 amount from EUR 4,785 to EUR 4,945; indexed at the assessment year 2027 coefficient of 2.3356 it gives 11,549.53, published as EUR 11,550 in the indexation notice of 12 August 2026. Annex III is a separate instrument, amended by its own Royal Decree; it has not been amended on this point and still carries the pre-reform indexed amount rounded down to the lower multiple of ten, EUR 11,170. The EUR 10 gap between the two conventions is systematic: assessment amounts are rounded to the nearest ten, Annex III amounts down to the lower ten.

The withholding therefore runs on EUR 11,170, because that is the rule in force for withholding. Putting EUR 11,550 into step G would describe a computation that no Belgian payroll engine is lawfully performing, and would under-withhold. Nothing is lost to the employee: withholding is an advance payment credited against the final liability, so the higher Article 131 allowance is applied in full when income year 2026 is assessed in 2027, and the excess withheld is refunded on assessment. The difference is a cash-flow timing difference, not a compliance exposure, and no payroll true-up is required — there is no amended withholding rule to recompute against. A Royal Decree amending Annex III is expected; if it is issued with retroactive effect to 1 January 2026, the corrected amount is to be absorbed prospectively in the next available payroll run and reconciled at assessment, not by reissuing earlier payslips.

Worked example — single resident, no dependants, gross EUR 4,000 per month, 2026

| Step | Calculation | Amount (EUR) |
| --- | --- | --- |
| A. Monthly gross | — | 4,000.00 |
| Employee social security | 4,000.00 x 13.07% | 522.80 |
| B. Monthly taxable | 4,000.00 − 522.80 | 3,477.20 |
| C. Annualised | 3,477.20 x 12 | 41,726.40 |
| D. Lump-sum expenses | 30% = 12,517.92, capped | 6,070.00 |
| E. Annual net taxable | 41,726.40 − 6,070.00 | 35,656.40 |
| F1. First slice | 16,710.00 x 26.75% | 4,469.93 |
| F2. Second slice | 12,790.00 x 42.80% | 5,474.12 |
| F3. Third slice | 6,156.40 x 48.15% | 2,964.31 |
| F. Annual tax before reductions | 4,469.93 + 5,474.12 + 2,964.31 | 12,908.36 |
| G. Tax-free allowance reduction | 11,170.00 x 26.75% | 2,987.98 |
| Basisbelasting | 12,908.36 − 2,987.98 | 9,920.38 |
| Annual withholding | No dependent children, no other reduction | 9,920.38 |
| Monthly withholding | 9,920.38 / 12 | 826.70 |

Worked example — the same employee with two dependent children

The tax-free allowance is unchanged at EUR 11,170, so the basisbelasting is still EUR 9,920.38. The relief for two dependent children is a flat reduction of EUR 1,656.00 taken from that basisbelasting (Annex III nr. 38), not an increase of the allowance. The annual withholding falls to 9,920.38 − 1,656.00 = EUR 8,264.38, and the monthly withholding to EUR 688.70 — a monthly saving of exactly EUR 138.00 compared with the childless case, which is 1,656.00 / 12. Every amount in the nr. 38 table is an exact multiple of 12, so the monthly saving is always a whole number of euro.

Legal basis: Income Tax Code 1992, Articles 30, 31, 51, 52, 130, 131, 132 and 270 to 275; Annex III to the Royal Decree implementing ITC 92 as replaced by the Royal Decree of 11 December 2025.

### 6.2 Tax Rates and Logic

#### What are the latest tax rates by tax type, residential status, and payment frequency?

Personal income tax scale — income year 2026, assessment year 2027

| Slice of annual net taxable income | Rate |
| --- | --- |
| EUR 0 – 16,720 | 25% |
| EUR 16,720 – 29,510 | 40% |
| EUR 29,510 – 51,070 | 45% |
| Above EUR 51,070 | 50% |

Basic tax-free allowance applied in the withholding: EUR 11,170 (Annex III nr. 32), delivered as a reduction of EUR 2,987.98. Relief for dependent children is not an increase of that allowance: it is a separate flat reduction of the basisbelasting of EUR 624 for one child, EUR 1,656 for two and EUR 4,404 for three, rising further beyond (Annex III nr. 38).

Withholding scale actually used in payroll — Annex III nr. 31 sets its own base scale, with ceilings that are not the assessment ceilings above and are not derivable from them by any rounding rule. They must be read from the annex each year.

| Slice of annual net taxable income | Withholding tax |
| --- | --- |
| EUR 0.01 – 16,710 | 26.75% |
| EUR 16,710 – 29,500 | EUR 4,469.93 + 42.80% on the slice above 16,710 |
| EUR 29,500 – 51,050 | EUR 9,944.05 + 48.15% on the slice above 29,500 |
| Above EUR 51,050 | EUR 20,320.38 + 53.50% on the slice above 51,050 |

The four rates are the assessment rates of 25%, 40%, 45% and 50% increased by the notional 7%; the four ceilings are set independently in the annex and differ from the assessment ceilings by EUR 10 to EUR 20.

Exceptional remuneration — the tables in Module 4.5 (bonuses and end-of-year premium) and Module 8 (double holiday pay), from 0% to 53.50%, keyed on the normal annual gross remuneration.

By residential status

| Status | Scale | Allowances |
| --- | --- | --- |
| Resident | I or II | Full |
| Non-resident meeting the 75% condition | I or II | Full |
| Non-resident not meeting the 75% condition | III | None |
| Inbound taxpayer under the special regime | I or II on the taxable part | Up to 35% of gross may be paid as an exempt reimbursement of employer's own costs, with the former EUR 90,000 annual cap abolished for tax purposes since the reform effective from income year 2025 (Law of 18 December 2025). Minimum gross remuneration for tax purposes: EUR 70,000/year, reduced from EUR 75,000, with no minimum for researchers. Existing contracts could be aligned retroactively to the new parameters until 30 June 2026. Note: NSSO/ONSS did not adopt the same reform - for social security purposes the prior EUR 75,000 minimum and EUR 90,000 annual cap on the exempt reimbursement still apply, so the tax-exempt and SS-exempt amounts diverge above EUR 90,000 of reimbursement. |

By payment frequency — the rates are identical. Annex III provides conversion factors so that weekly, fortnightly and monthly payments are annualised consistently; the rate itself never changes with the frequency.

#### How are rates applied for different frequencies?

The scale is annual. Each payment is converted to an annual equivalent, taxed, and converted back:

| Frequency | Annualisation factor | Division factor |
| --- | --- | --- |
| Monthly | x 12 | / 12 |
| Fortnightly | x 26 | / 26 |
| Weekly | x 52 | / 52 |
| Exceptional payment | Not annualised; the percentage is read from the exceptional-payment table using the normal annual gross remuneration, computed as the monthly gross x 13.92 | Not applicable |

The factor 13.92 used for exceptional payments reflects twelve monthly salaries plus the double holiday pay and the end-of-year premium, and is the reason a bonus paid to an employee on EUR 3,000 per month is taxed by reference to an annual reference of EUR 41,760 rather than EUR 36,000.

#### How does tax applicability and calculation logic differ by residential status?

| Aspect | Resident | Non-resident |
| --- | --- | --- |
| Scope of taxation | Worldwide professional income | Belgian-source professional income only |
| Withholding scale | I or II | I or II if the 75% condition is met; otherwise III |
| Tax-free allowance in the withholding | Applied | Applied only under scales I and II |
| Family reductions | Applied | Applied only under scales I and II |
| Annual return | Personal income tax return, filed in the year following the income year | Non-resident income tax return, with its own filing window (for income year 2025 the window ran from 3 September to 20 November 2026) |
| Treaty relief | Foreign employment income may be exempt with progression | Belgium may be prevented from taxing by the treaty; the employer must then be instructed not to withhold, on the basis of documented treaty analysis |
| Municipal and regional surcharge | Settled at the assessment on the basis of the commune of residence | A fixed federal additional levy of 7% (ITC 92 Article 245) applies in place of the municipal tax, because a non-resident has no Belgian commune of residence. In Chefquet (Case C-119/24, judgment of 12 March 2026) the Court of Justice of the European Union held that fixed rate contrary to Article 45 TFEU, since it can impose a heavier burden than that borne by a resident of a commune levying less than 7%. Being a preliminary ruling, it sets the fixed rate aside with immediate effect; affected non-residents may claim within one year of the assessment or seek relief ex officio for up to five years. A preliminary draft bill of corrective measures — allowing a non-resident to establish a connection to a commune levying below 7% — was approved by the Council of Ministers on 18 July 2026 and is before the Council of State; it is not yet enacted. This is an assessment-level matter and does not of itself alter payroll withholding. |

Because the withholding for a non-resident who fails the 75% test grants no allowances, the effective withholding rate is materially higher than for a comparable resident. That is by design: the non-resident is expected to claim any relief in the annual non-resident return.

#### Provide the tax calculation logic covering eligibility, joining month, termination month, mid-month joining, mid-month terminations, and mid-month salary revisions.

| Event | Logic |
| --- | --- |
| Eligibility | The withholding obligation arises on the first payment of taxable remuneration. There is no threshold below which no withholding is due, although a very low annualised amount produces a nil result from the scale |
| Joining month | The prorated gross is annualised as if it were a full monthly salary. A person joining on the 16th of the month therefore has a lower annualised income and a proportionately lower rate applied to that month. No catch-up is performed later |
| Termination month | Identical treatment for the prorated salary. The final settlement items — departure holiday pay, pro rata end-of-year premium, notice indemnity — are each taxed under their own rule and not merged into the monthly calculation |
| Mid-month joining | See joining month. The annualisation of a part-month is a deliberate feature of the non-cumulative design, not an error to be corrected |
| Mid-month termination | See termination month |
| Mid-month salary revision | The new gross applies from the effective date. Where the month contains two salary levels, market practice is to compute one taxable amount for the month and apply the ordinary calculation once; where the revision is retroactive to a previous month, the retroactive part is arrears and is taxed at the exceptional-payment rate |

#### Do tax rates vary by gender or age?

No. The scale, the tax-free allowance and the withholding rules are identical regardless of gender and regardless of age. Two age-related items exist but are not rate variations:

Students — no wage withholding tax is due on the first 650 hours of student work per calendar year, an exemption formally incorporated into Annex III.

Pensioners in employment — ordinary rates apply to the employment income; the pension itself is subject to its own withholding scale outside payroll.

#### What is the minimum tax rate applicable?

There is no statutory minimum withholding rate. The scale starts at 26.75% for the first slice of annual net taxable income, but after the reduction for the tax-free allowance the effective withholding on low wages is nil: an employee whose annual net taxable income after the lump-sum professional expenses is at or below EUR 11,170 has a computed withholding of zero.

For exceptional payments the tables themselves begin at 0.00% for an annual gross reference remuneration up to EUR 10,675.00, so a bonus paid to a very low earner attracts no withholding.

Two special flat rates should be noted because they are sometimes mistaken for minima: the flexi-job wage carries no wage withholding tax at all, and student work carries none within the 650-hour quota.

Legal basis: Income Tax Code 1992, Articles 130 to 134, 227, 232, 243/1, 244 and 270 to 275; Annex III to the Royal Decree implementing ITC 92 (Royal Decree of 11 December 2025); Law of 21 January 2022 introducing the special regime for inbound taxpayers, as amended with effect from income year 2025; ITC 92 Article 245 (federal additional levy on non-residents); Court of Justice of the European Union, Chefquet, Case C-119/24, judgment of 12 March 2026 (Article 245 fixed 7% rate contrary to Article 45 TFEU).

### 6.3 Adjustments and Special Cases

#### For annualized tax systems, which salary components must be projected?

Belgium annualises the current payment only; it does not forecast the year. Nothing is projected from future months into the current calculation, which removes an entire class of configuration risk.

What is nevertheless treated as a full-year figure:

| Component | How it enters the calculation |
| --- | --- |
| The current period's ordinary taxable remuneration | Multiplied by the frequency factor (12, 26 or 52) |
| Recurring fixed premiums paid every period | Included in the periodic amount and therefore annualised with it |
| Benefits in kind with an annual statutory value | Divided by 12 and added to each month, so that they annualise back to the correct figure |
| Normal annual gross remuneration, used to key the exceptional-payment tables | Monthly gross x 13.92 |
| Variable pay such as commission | Included in the month in which it is paid; a large variable element paid monthly will push that month into a higher annualised rate, and the excess is recovered through the annual assessment |

The consequence to communicate to clients is that an employee with strongly variable monthly pay experiences visible month-to-month swings in the withholding rate. This is correct behaviour, not a defect.

#### Are year-end tax adjustments required?

No year-end adjustment is performed in payroll. The employer does not recompute the year, does not true up the withholding and does not refund over-withholding.

The year-end obligations are reporting obligations:

| Obligation | Deadline |
| --- | --- |
| Issue form 281.10 to each employee and file it through Belcotax-on-web | 28 February following the income year |
| Populate the <Opgave32510> wrapper and zone 2.029 inside the 281.10 submission. The summary statement 325.10 is derived by FPS Finance from the 281.10 data and is never separately submitted | Discharged by the 281.10 filing; no separate deadline |
| Reconcile the twelve monthly withholding tax returns to the 281.10 totals | Before the Belcotax filing |
| Correct any error found after filing, through a corrective Belcotax submission | As soon as identified |

The definitive settlement happens in the employee's personal income tax return, where the total withholding shown on the 281.10 is credited against the assessed tax.

#### Are there minimum or higher tax requirements if employees fail to submit a tax ID or social security number?

There is no penal withholding rate for a missing identification number, because an employee cannot be declared at all without one. The Dimona declaration and the DmfA both require the national register number (INSZ) or a BIS number; a foreign employee without a National Register entry is issued a BIS number precisely so that the declaration can be made.

What does change with missing information:

| Missing item | Consequence |
| --- | --- |
| INSZ or BIS number | The employee cannot be declared. The employer must obtain a BIS number before the first pay run |
| Declaration of family situation | The employer applies scale I with no dependants, the least favourable position that is still lawful. The employee recovers any excess in the annual return |
| Proof of non-resident status or treaty relief | The employer withholds under the domestic rule, applying scale III where the 75% condition is not demonstrated |
| Proof of dependants claimed | The employer must not apply an unsubstantiated reduction; the risk of an incorrect reduction falls on the employer as withholding agent |

Failure to withhold or to remit the withholding tax exposes the employer to the tax increases and administrative fines of Articles 444 and following of ITC 92, and to late-payment interest.

#### What is the income tax and social security refund procedure?

| Situation | Procedure |
| --- | --- |
| Over-withholding of wage withholding tax during the year | Not refunded by the employer. The employee recovers it through the personal income tax assessment, which normally issues in the second half of the year following the income year |
| Employer error in the withholding, discovered in the same calendar year | Corrected in a subsequent pay run of the same year and reflected in the monthly withholding tax return; the 281.10 then shows the corrected annual figure |
| Employer error discovered after the year is closed | A corrective 281.10 is filed through Belcotax-on-web and the employee amends the return. Corrections to the withholding tax returns for income year 2025 had to be filed by 15 May 2026 for exemption-related corrections and by 10 July 2026 for other corrections, with the Finprof channel for that income year closing on 31 August 2026 |
| Over-payment of social security contributions | The employer files a corrective DmfA for the quarter concerned. The NSSO refunds or offsets the difference against the following quarter |
| Employee contribution wrongly withheld | Repaid to the employee in the next pay run and corrected in the DmfA; the corresponding tax base and the 281.10 must be corrected in the same movement |
| Special social security contribution | Provisionally withheld and finally settled through the tax assessment, so a small over- or under-withholding within the year is normal and self-correcting |

#### Deliverable: Detailed worked examples for a standard resident employee, a non-resident employee, and an irregular payment

Example 1 — standard resident employee

Single, no dependants, white-collar, joint committee 200, gross EUR 4,000.00 per month, 21 worked days, meal vouchers of EUR 10.00 face value.

| Line | Calculation | Amount (EUR) |
| --- | --- | --- |
| Gross remuneration | — | 4,000.00 |
| Employee social security | 4,000.00 x 13.07% | −522.80 |
| Taxable base | — | 3,477.20 |
| Wage withholding tax | Scale calculation of Module 6.1.1 | −826.70 |
| Special social security contribution | Quarterly wage 12,000.00 -> 82.05 + 3.38% x 789.00 = 108.72 per quarter | −36.24 |
| Meal voucher employee part | 21 x 1.09 | −22.89 |
| Net paid | — | 2,591.37 |
| Meal vouchers received | 21 x 10.00 face value | 210.00 (not cash) |
| Employer social security | 4,000.00 x approximately 25% | 1,000.00 |
| Employer meal voucher part | 21 x 8.91 | 187.11 |
| Employer cost for the month | — | 5,187.11 plus holiday pay and end-of-year premium provisions |

Example 2 — non-resident employee failing the 75% condition

A French resident employed by a Belgian company, working 40% of contractual time in Belgium, gross EUR 4,000.00 per month for the Belgian part of the activity. Belgian social security applies to the Belgian activity unless an A1 assigns it elsewhere; the example assumes Belgian social security applies.

| Line | Calculation | Amount (EUR) |
| --- | --- | --- |
| Gross remuneration | — | 4,000.00 |
| Employee social security | 4,000.00 x 13.07% | −522.80 |
| Taxable base | — | 3,477.20 |
| Annualised | 3,477.20 x 12 | 41,726.40 |
| Lump-sum professional expenses | 30%, capped | −6,070.00 |
| Annual net taxable | — | 35,656.40 |
| Tax on the scale | 4,469.93 + 5,474.12 + 2,964.31 | 12,908.36 |
| Reduction for the tax-free allowance | Not granted under scale III | 0.00 |
| Annual withholding | — | 12,908.36 |
| Monthly withholding | 12,908.36 / 12 | 1,075.70 |
| Special social security contribution | As Example 1 | −36.24 |
| Net paid | 4,000.00 − 522.80 − 1,075.70 − 36.24 | 2,365.26 |

Scale III uses the same Annex III nr. 31 base scale (nr. 108) but deducts no allowance. The difference against the resident case is therefore exactly the tax-free allowance reduction — EUR 249.00 per month, or EUR 2,987.98 per year. If the same employee met the 75% condition, scale I would apply and the outcome would be identical to Example 1.

Example 3 — irregular payment (annual bonus)

The Example 1 employee receives a gross bonus of EUR 6,000.00 in March 2026.

| Line | Calculation | Amount (EUR) |
| --- | --- | --- |
| Bonus gross | — | 6,000.00 |
| Employee social security | 6,000.00 x 13.07% | −784.20 |
| Taxable amount | — | 5,215.80 |
| Normal annual gross reference remuneration | 4,000.00 x 13.92 | 55,680.00 |
| Applicable rate from the exceptional-payment table | Band EUR 45,860.01 – 59,900.00 | 51.48% |
| Wage withholding tax | 5,215.80 x 51.48% | −2,685.09 |
| Net bonus | 5,215.80 − 2,685.09 | 2,530.71 |
| Employer social security | 6,000.00 x approximately 25% | 1,500.00 |

The bonus also increases the quarterly wage from EUR 12,000.00 to EUR 18,000.00, which moves the special social security contribution for that quarter into the band above EUR 12,300.00: 118.83 + 1.10% x (18,000.00 − 12,300.00) = EUR 181.53 per quarter, against EUR 108.72 without the bonus. The additional EUR 72.81 is taken at the last payment of the quarter.

Legal basis: Income Tax Code 1992, Articles 171, 270 to 275, 302, 306 and 444 and following; Annex III to the Royal Decree implementing ITC 92 (Royal Decree of 11 December 2025); Royal Decree of 27 August 1993, Articles 90 to 95.

## Module 7: Deductions, Exemptions & Benefits

### 7.1 Statutory Tax Reliefs, Deductions, and Exemptions

#### Deliverable: For each statutory tax relief, deduction, exemption or other tax advantage — name and definition, eligibility rules, statutory limits and amounts, calculation method, application point, and employee declaration requirements

1. Employee social security contribution

Name and definition — the compulsory 13.07% contribution, treated as a deductible professional expense.

Eligibility — every employee subject to Belgian social security.

Limits — none; uncapped.

Calculation — 13.07% of the gross (of the gross at 108% for blue-collar workers).

Application point — deducted from the gross before the taxable base is formed.

Declaration — none; system-derived.

2. Lump-sum professional expenses

Definition — a flat deduction in place of actual professional expenses.

Eligibility — all employees; an employee may instead prove actual expenses in the annual return, which payroll never applies.

Limits — 30% of the gross taxable income, capped at EUR 6,070 for income year 2026.

Calculation — min(30% x annual taxable income, 6,070).

Application point — step 4 of the annual withholding calculation.

Declaration — none.

3. Basic tax-free allowance and dependent-child relief

Definition — the portion of income relieved from tax, delivered in the withholding as a reduction at the lowest rate. Relief for dependent children is a separate flat euro reduction of the basisbelasting, not an increase of that allowance.

Eligibility — residents, and non-residents meeting the 75% condition.

Limits, income year 2026 — basic allowance EUR 11,170 (Annex III nr. 32), giving a reduction of EUR 2,987.98. Dependent-child relief (Annex III nr. 38), deducted from the basisbelasting after that reduction: EUR 624 for one child, EUR 1,656 for two, EUR 4,404 for three, EUR 7,620 for four, EUR 11,100 for five, EUR 14,592 for six, EUR 18,120 for seven, EUR 21,996 for eight, plus EUR 3,864 per child above the eighth; a disabled dependent child counts as two. Separate reductions apply for a disabled employee, a disabled dependant, a dependent ascendant aged 65 or over, and a single parent.

Calculation — the basic allowance multiplied by 26.75%, then the flat child amount subtracted from the resulting basisbelasting.

Application point — steps 7 and 8 of the annual withholding calculation.

Declaration — employee statement of family situation on hire and on change; the employer must not apply an unsubstantiated claim.

4. Fiscal work bonus

Definition — a reduction of the withholding tax for low-wage employees, complementing the social work bonus.

Eligibility — employees actually receiving the social work bonus.

Limits — a maximum of EUR 765 per calendar year applied from income year 2025, with a reinforcement STATUS UPDATE (21 August 2026): a Law of 15 July 2026 reforming personal income tax (Belgian Official Gazette, 29 July 2026) and an implementing Royal Decree of 30 July 2026 (Belgian Official Gazette, 30 July 2026) have now been enacted and confirm that a fiscal work bonus enhancement for very low salaries applies from 1 August 2026 — this supersedes the March 2026 "not yet definitively adopted by the Chamber" status. The specific EUR 2,000/63%/72% figures previously reported by secondary sources have NOT been independently re-confirmed against these two July 2026 texts as part of this review; do not configure them without pulling the actual Annex III / Article 154bis wording introduced by the 30 July 2026 Royal Decree, since a reform law commonly adjusts a proposal's headline figures before enactment.

Limits — indexation status of the EUR 765 is NOT RESOLVED. Secondary payroll sources describe the statutory maximum as a basisbedrag ("te indexeren bedrag") that is indexed before application — one states EUR 550 basic against EUR 1,030 indexed for assessment year 2024 — while another presents the same EUR 550 as both the basic and the applied figure. The two readings differ by roughly a factor of two on the annual cap. Resolve against Income Tax Code 1992, Article 154bis and the FPS Finance indexation notice for income year 2026 before the cap is configured; do not assume EUR 765 is the amount actually applied.

Calculation — the fiscal work bonus is a percentage of the social work bonus actually granted in the period, and the percentage differs by component of the social work bonus (Module 5.1.1): 33.14% of component A and 52.54% of component B, subject to the annual cap above. The reinforcement referred to above would raise the component B percentage to 63% for assessment years 2027 and 2028 and to 72% from assessment year 2029, and the component A percentage to 35% from assessment year 2029; income year 2026 is assessment year 2027, so the 63% figure — not 52.54% — is the one that governs this guide's income year if the measure is enacted. Both readings are stated because the enactment is unconfirmed; the 33.14% on component A is unaffected either way.

Application point — a reduction of the computed withholding.

Declaration — none; derived from the social work bonus.

5. Overtime relief

Definition — relief on overtime carrying a statutory supplement.

Eligibility — employees who worked overtime with a legal supplement; managerial staff outside the working time rules are excluded.

Limits — 180 hours per employee per calendar year, made permanent from 2026; higher ceilings in construction with electronic attendance and in hotels and catering with a registered cash register.

Calculation — employee reduction of 66.81% of the base on which the 50% or 100% supplement is calculated (57.75% where the supplement is 20%); employer exemption from remitting 41.25% (32.19% where the supplement is 20%) of the withholding on the same base.

Application point — a reduction of the withholding on the payslip and a reduction of the amount remitted in the withholding tax return.

Declaration — none from the employee; the employer must keep the overtime records.

6. Reduction for a personal supplementary pension contribution

Definition — relief for the employee's own contribution to the employer's second-pillar plan.

Eligibility — employees affiliated to a plan providing for a personal contribution, where the 80% limit of the plan is respected.

Limits — no separate payroll cap; the plan itself is constrained by the 80% rule.

Calculation — a withholding reduction of 30% of the contribution withheld.

Application point — a reduction of the computed withholding; the contribution itself is withheld from net pay.

Declaration — affiliation and consent to the deduction.

7. Exemption for student work

Definition — no wage withholding tax on student pay within the quota.

Eligibility — students employed under a student contract with a Dimona STU declaration.

Limits — the first 650 hours per calendar year; the same quota governs the reduced solidarity contribution of 2.71% employee and 5.42% employer.

Calculation — no withholding within the quota; from the 651st hour, ordinary withholding and ordinary contributions of 13.07% and approximately 25%.

Application point — the whole calculation is bypassed within the quota.

Declaration — student status; the employer must check the remaining quota through the student counter before engaging.

8. Flexi-job regime

Definition — a parallel regime for secondary employment in eligible sectors.

Eligibility — a person already employed at least four fifths elsewhere, or a pensioner, in a sector opened to flexi-jobs.

Limits — the tax exemption of the flexi-wage applies up to EUR 18,440 for income year 2026; above that the excess is taxable.

Calculation — no ordinary employee contribution and no withholding tax on the flexi-wage; the employer pays a special contribution of 28%.

Application point — a separate wage type set and a separate DmfA worker code.

Declaration — a flexi-job framework agreement and a Dimona FLX declaration.

9. Special regime for inbound taxpayers and inbound researchers

Definition — a regime allowing part of the remuneration to be paid as a tax-free reimbursement of costs proper to the employer.

Eligibility — recruited abroad or transferred within a group, not a Belgian resident in the 60 months before taking up the post, and not living within 150 km of the Belgian border in that period.

Limits — up to 35% of the gross remuneration, with the former EUR 90,000 annual cap abolished; a minimum gross remuneration of EUR 70,000 per year, reduced from EUR 75,000, with no minimum for researchers. Existing contracts could be aligned retroactively to the new parameters until 30 June 2026.

Calculation — the exempt part is excluded from the taxable base and from the social security base; the balance is taxed and contributory normally.

Application point — before the taxable base is formed.

Declaration — a joint employer and employee application to the tax administration within three months of taking up the post, plus an annual nominative list.

10. Exempt allowances

| Allowance | 2026 limit | Application point |
| --- | --- | --- |
| Bicycle allowance | EUR 0.37 per km, annual ceiling EUR 3,700; the CBA no. 164 obligation itself is EUR 0.30 per km for up to 40 km per day | Excluded from the base |
| Homeworking (office) allowance | EUR 160.99 per month from 1 March 2026, up from EUR 157.83 | Excluded from the base |
| Meal vouchers | Face value up to EUR 10.00 from 1 January 2026; employee part at least EUR 1.09; one per worked day | Excluded from the base |
| Eco vouchers | Sectoral ceiling; being phased out | Excluded from the base |
| Commuting reimbursement | Within the CBA no. 19/9 and sectoral limits | Excluded from the base |
| Genuine expenses proper to the employer | Actual cost, or a flat rate accepted by the NSSO and the tax administration | Excluded from the base |
| CBA no. 90 bonus | Tax ceiling EUR 3,701; social ceiling EUR 4,255 | Excluded up to the ceiling |

#### Are salary sacrifice arrangements allowed?

Yes, but within tight limits, and Belgium calls them cafeteria plans or flexible remuneration plans. The framework is not a single statute but the interaction of the Wage Protection Act, the NSSO wage concept and settled administrative rulings.

Permitted structures:

Exchanging a future discretionary bonus, or a future increase, for a benefit such as an additional pension contribution, a company bicycle, extra leave days or IT equipment.

Reallocating an existing benefit budget between benefits within a company plan.

Prohibited or restricted:

Reducing the acquired salary below the sectoral minimum or the guaranteed average minimum monthly income.

Sacrificing salary that is already due — the Wage Protection Act prevents an employee from waiving remuneration already earned.

Any arrangement that converts contributory wage into a non-contributory benefit without a genuine change in the underlying entitlement; the NSSO requalifies these as wage.

Sacrifice affecting the base of holiday pay, the end-of-year premium or the notice indemnity without the plan explicitly addressing it — a common source of dispute on termination.

Because a cafeteria plan changes the contributory base, the mobility budget (Law of 17 March 2019) is the one arrangement with an explicit statutory framework: an employee entitled to a company car can exchange it for a budget spendable across three pillars, with pillar 2 spending exempt from tax and contributions.

#### List common types of post-tax deductions and any specific ordering rules or limitations.

| Deduction | Nature | Limit |
| --- | --- | --- |
| Employee part of meal vouchers | Contractual | At least EUR 1.09 per voucher |
| Personal contribution to the supplementary pension plan | Contractual | Per the plan |
| Personal contribution for a company car | Contractual | Reduces the taxable benefit but never below zero |
| Hospitalisation insurance for family members | Contractual | Per the policy |
| Wage assignment (loonoverdracht) | Contractual, notified | Article 1409 bands |
| Wage garnishment (loonbeslag) | Court or administrative | Article 1409 bands |
| Maintenance and child support debts | Court or notarial | Attachable without limit, ahead of all other creditors |
| Repayment of advances on salary | Contractual | Within the one-fifth cap of Article 23 of the Wage Protection Act |
| Fines under the work rules, and compensation for damage caused by the employee | Disciplinary or contractual | Within the same one-fifth cap |
| Trade union contributions | Voluntary | By employee mandate |

Ordering rule. Deductions are applied in this sequence: statutory levies first (social security, wage withholding tax, special social security contribution — none of which is subject to any cap), then maintenance debts, then garnishments and wage assignments within the Article 1409 protected bands, then contractual deductions subject to the aggregate one-fifth cap of Article 23. A contractual deduction that cannot be made in full is carried forward, never taken out of the protected floor.

#### List any income types that are statutorily exempt from income tax.

| Exempt item | Condition |
| --- | --- |
| Meal, eco, sport and culture vouchers | Within their statutory conditions and ceilings |
| Genuine reimbursement of expenses proper to the employer | Justified by actual cost or an accepted flat rate |
| Bicycle allowance | Up to EUR 0.37 per km and EUR 3,700 per year |
| Homeworking allowance | Up to EUR 160.99 per month from 1 March 2026 |
| Commuting reimbursement | Within the statutory exemption for public transport and the sectoral limits for private transport |
| CBA no. 90 non-recurring result-tied bonus | Up to EUR 3,701 for 2026 |
| Student pay | No withholding within the 650-hour quota |
| Flexi-job wage | Exempt up to EUR 18,440 for income year 2026 |
| Voluntary net overtime hours under the regime from 1 April 2026 | The first 240 of the 360-hour quota |
| Social benefits of small value (a gift voucher for a company anniversary, a retirement gift, a St Nicholas gift within the fixed amounts) | Within the amounts accepted by the NSSO and the tax administration |
| Employer-paid hospitalisation insurance premium | Where the policy meets the conditions |
| Statutory benefits paid by the health insurance fund | Paid outside payroll; taxed under their own regime where taxable |

Legal basis: Income Tax Code 1992, Articles 38, 51, 52, 131, 132, 154bis, 1451 and 1453; Annex III to the Royal Decree implementing ITC 92; Law of 21 January 2022 (inbound taxpayers) as amended; Law of 17 March 2019 (mobility budget); Royal Decree of 28 November 1969, Article 19bis; CBA no. 90; CBA no. 164; CBA no. 19/9; Wage Protection Act of 12 April 1965, Article 23.

### 7.2 Benefits in Kind (BIK)

#### Are non-cash benefits taxed via the standard payroll system, or a separate employer-paid regime?

Both, depending on the benefit. Belgium has no general fringe benefits tax, so the default is that a benefit in kind is valued, added to the employee's taxable base and taxed through the ordinary payroll withholding. For a small number of benefits the legislator replaced the ordinary social security treatment with a separate employer-paid levy, which is the closest Belgian equivalent to a fringe benefits tax.

| Benefit | Employee tax | Employer levy |
| --- | --- | --- |
| Company car with private use | Taxable benefit in the payroll | CO2 solidarity contribution to the NSSO, replacing ordinary contributions |
| Company car fuel or charging card | Included in the car benefit | Included in the CO2 contribution; a corporate tax disallowance of 17% or 40% of the benefit applies at company level |
| Free housing, free heating and electricity | Taxable benefit in the payroll | Ordinary social security contributions |
| Free meals, personal use of a PC or internet | Taxable benefit at the flat statutory values | Ordinary social security contributions |
| Employer premium to a supplementary pension plan | Not taxed on payment | 8.86% special contribution plus 4.4% insurance premium tax |
| CBA no. 90 bonus | Exempt to the tax ceiling | 33% special employer contribution |
| Meal and eco vouchers, conditions met | Not taxed | None |

#### What is the definition of fringe benefits and how is the taxable amount evaluated?

Article 31, 2° of ITC 92 makes taxable any advantage of any kind (voordeel van alle aard) obtained by reason of or on the occasion of the employment. The valuation rule of Article 36 is that the benefit is valued at the actual value to the beneficiary, unless the King has fixed a flat valuation — which he has done, in Article 18 of the Royal Decree implementing ITC 92, for the benefits that matter most in payroll.

| Benefit | 2026 valuation |
| --- | --- |
| Company car | Catalogue value x CO2 percentage x 6/7 x age coefficient, with an annual minimum of EUR 1,690 (EUR 140.83 per month) |
| Free housing | A multiple of the indexed cadastral income, per the Royal Decree |
| Free heating | Flat annual amount, higher for management staff |
| Free electricity | Flat annual amount, higher for management staff |
| Free meals | Flat amount per meal |
| Personal use of a PC, tablet, internet connection or mobile phone | Flat annual amounts per device or service |
| Interest-free or low-interest loan | The difference against the statutory reference rate published annually |

Where no flat valuation exists, the actual cost to the employer is used as the best evidence of the value to the beneficiary.

#### If a separate FBT regime exists, describe it in detail.

The CO2 solidarity contribution is the separate regime. It is an employer-only social security levy, due monthly per vehicle made available for private use, independent of the employee's income and independent of the taxable benefit.

Monthly contribution =

[ (CO2 emission in g/km x 9.00) − F ] / 12  x  index coefficient

where F = 768 for petrol, 600 for diesel, 990 for LPG

index coefficient for 2026 = 1.6291

(health index September 2025 = 185.85

divided by September 2004 = 114.08)

| Parameter | 2026 value |
| --- | --- |
| Index coefficient | 1.6291, up from 1.5948 |
| Minimum monthly contribution, vehicle ordered before 1 July 2023 | EUR 33.93 |
| Minimum monthly contribution, vehicle ordered from 1 July 2023 | EUR 42.34 |
| Default CO2 value where the emission is unknown | 182 g/km petrol, 165 g/km diesel |
| Electric and hydrogen vehicles | Always liable to the minimum contribution |
| Multiplier for combustion vehicles ordered from 1 July 2023 | 4.00 from 1 January 2026, and the figure is fixed in the law itself, not inferred from commentary. Law of 25 November 2021 organising the fiscal and social greening of mobility, Article 34, 1° (Belgian Official Gazette 3 December 2021, numac 2021033910) completes Article 38, §3quater, 3° of the Law of 29 June 1981 establishing the general principles of the social security of salaried workers with the full schedule: "a) la cotisation calculée : multipliée par un facteur de 2,25 à partir du 1er juillet 2023, par un facteur de 2,75 à partir du 1er janvier 2025, par un facteur de 4,00 à partir du 1er janvier 2026 et par un facteur de 5,50 à partir du 1er janvier 2027" — so 2.25 (2023-2024), 2.75 (2025), 4.00 (2026), 5.50 (from 2027), the French text using the decimal comma. The NSSO reproduces the same four factors and the same dates in its administrative instructions 2026/2, Les cotisations spéciales — la cotisation de solidarité pour les véhicules de société. The factor multiplies the calculated contribution only. The minimum contribution is not multiplied: the same Article 34, 1° raises it separately, in its point b), to EUR 25.99 non-indexed from 1 January 2026 (EUR 42.34 once indexed — the row above), then EUR 28.57 from 2027 and EUR 31.15 from 2028. The final sentence of the inserted text excludes vehicles achetés, pris en leasing ou en location avant le 1er juillet 2023 from both increases, which is why the two minimum-contribution rows above differ. |

The contribution is declared and paid through the quarterly DmfA, per vehicle, for each month in which the vehicle was available for private use, prorated by day where the availability starts or ends mid-month.

#### What is the calculation logic for fringe benefit tax?

Company car benefit — the main case.

CO2 percentage = 5.5% + 0.1% x (CO2 of the vehicle − reference CO2)

floored at 4%, capped at 18%

Reference CO2 for 2026:  70 g/km  petrol, LPG and natural gas

58 g/km  diesel

Taxable benefit (annual) = catalogue value

x CO2 percentage

x 6/7

x age coefficient

with an annual floor of EUR 1,690

Age coefficient: 100% in the first 12 months from first registration,

then reduced by 6 percentage points per elapsed year,

with a floor of 70%

The coefficient is a function of the number of months

that have run between the date of first registration

and the month for which the benefit is computed:

months elapsed        coefficient

0 to 12               100%

13 to 24                94%

25 to 36                88%

37 to 48                82%

49 to 60                76%

over 60                 70%   (floor)

The coefficient is driven by the benefit month, not by the calendar year. Counting elapsed years from the year of registration rather than from the registration date is the standard error here: a car first registered in March 2024 is in its 94% period only until February 2026, and moves to 88% from March 2026.

The employee's own contribution for the vehicle is deducted from the taxable benefit but can never make it negative.

Worked example — company car, 2026

A petrol car with a catalogue value of EUR 38,000, CO2 emission of 120 g/km, first registered in March 2024, with the benefit computed for May 2026 — the month used by the Module 12 Example 5 scenario that consumes this figure.

| Step | Calculation | Result |
| --- | --- | --- |
| CO2 percentage | 5.5% + 0.1% x (120 − 70) = 5.5% + 5.0% | 10.50% |
| Age coefficient | Registered March 2024, benefit month May 2026: 26 months elapsed, so the 25-to-36 band applies — 100% − (6 x 2) | 88% |
| Annual benefit | 38,000 x 10.50% x 6/7 x 88% | EUR 3,009.60 |
| Monthly taxable benefit | 3,009.60 / 12 | EUR 250.80 |
| Employer CO2 contribution | [(120 x 9.00) − 768] / 12 x 1.6291 = (1,080 − 768) / 12 x 1.6291 | EUR 42.36 per month |

The annual benefit of EUR 3,009.60 is above the annual floor of EUR 1,690, so the floor does not bite. The monthly benefit of EUR 250.80 is added to the employee's taxable base and taxed at the ordinary scale; it is not added to the social security base. The employer pays EUR 42.36 per month to the NSSO in addition to the ordinary contributions on the cash salary.

#### Are benefits-in-kind also subject to withholding tax?

Yes. A taxable benefit in kind is part of the taxable base and is subject to the ordinary wage withholding tax in the period in which it is enjoyed. Because the benefit is not paid in cash, the withholding on it is funded out of the cash salary, which reduces the employee's net.

Where the benefit is granted annually rather than monthly (for example a one-off gift above the exempt limits), it is treated as an exceptional payment and taxed at the exceptional-payment percentage.

Benefits that are exempt — compliant meal and eco vouchers, the exempt part of the bicycle and homeworking allowances, genuine expense reimbursements — carry no withholding.

#### Which benefits-in-kind must be processed via payroll, and which require declarations?

| Benefit | Payroll processing | Separate declaration |
| --- | --- | --- |
| Company car | Monthly taxable benefit on the payslip; employer CO2 contribution in the DmfA | Reported in the 281.10 |
| Fuel or charging card | Included in the car benefit | Reported in the 281.10; corporate tax disallowance handled in the tax return |
| Free housing, heating, electricity | Monthly taxable benefit | Reported in the 281.10 |
| PC, tablet, internet, mobile | Monthly taxable benefit at the flat values | Reported in the 281.10 |
| Meal vouchers | Employee part deducted from net; face value shown for information | Employer cost only; the deductible part is a corporate tax item |
| Eco vouchers | Shown for information | Corporate tax item |
| Supplementary pension premium | Not on the payslip as a benefit; the 8.86% contribution appears in the DmfA | Declared in the DB2P database |
| Stock options accepted within 60 days | Taxable benefit at grant, processed in the payroll of the month of acceptance | Reported in the 281.10 |
| Hospitalisation insurance | Not taxable where the conditions are met | None |
| Employer-provided bicycle | Exempt where used for commuting | None |

Legal basis: Income Tax Code 1992, Articles 31, 36 and 38; Royal Decree implementing ITC 92, Article 18; Programme Law of 27 December 2005 (CO2 solidarity contribution) as indexed for 2026; Law of 29 June 1981 establishing the general principles of the social security of salaried workers, Article 38, §3quater; Law of 25 November 2021 organising the fiscal and social greening of mobility, Article 34 (Belgian Official Gazette 3 December 2021, numac 2021033910) — the multiplier and minimum-contribution schedule for vehicles ordered from 1 July 2023; NSSO administrative instructions 2026/2, special contributions, company vehicles; Law of 26 March 1999 (stock options); Law of 28 April 2003 (supplementary pensions).

### 7.3 Garnishments and Court Orders

#### What are the rules for processing statutory deductions like child support, court-ordered fines, or tax levies?

Two mechanisms exist and both are governed by Articles 1409 to 1412 of the Judicial Code.

Wage garnishment (loonbeslag) — imposed by a court or, for tax and social security debts, by the administration through a simplified attachment in the hands of the employer. The employer becomes garnishee: on receipt of the attachment it must, within fifteen days, file a declaration of the sums it holds, then withhold and remit the attachable part to the bailiff or the administration.

Wage assignment (loonoverdracht) — a contractual assignment by the employee, typically to secure a consumer credit. It becomes enforceable against the employer only after a notification procedure in which the employee may object within ten days.

The employer's duties on receiving either instrument: acknowledge, verify the identity of the employee, compute the attachable amount for each pay period under the Article 1409 bands, remit to the creditor or bailiff, keep the employee informed on the payslip, and notify the creditor when the employee leaves. An employer that ignores an attachment can be held personally liable for the sums it should have withheld.

Special rules:

Maintenance and child support debts are attachable without any limit — the protected bands do not apply — and they rank ahead of all other creditors.

Tax and social security debts use the simplified attachment procedure but respect the ordinary bands.

Criminal fines are recovered through ordinary attachment and respect the bands.

#### Is there a statutory priority order if an employee has multiple garnishments?

Yes.

Maintenance and child support debts — paid first and in full, without limit, from the whole net income.

Wage assignments and garnishments served earlier in time — within the attachable portion determined by the Article 1409 bands.

Competing ordinary creditors — where several attachments compete for the same attachable portion, the amount is distributed by the bailiff among the creditors, in principle proportionally, unless a creditor holds a preferential right. The employer withholds a single global attachable amount and remits it to the bailiff, who performs the distribution; the employer does not adjudicate between creditors.

Contractual deductions by the employer (advances, fines) — last, and within the separate one-fifth cap of Article 23 of the Wage Protection Act.

#### Are there protected earnings limits?

Yes. Article 1409 of the Judicial Code protects a floor of monthly net income that cannot be attached at all, and then allows an increasing proportion of the bands above it. The amounts are indexed each year; the 2026 figures were set by the Royal Decree of 3 December 2025, published in the Belgian Official Gazette of 10 December 2025 and applicable from 1 January 2026.

Employment income — 2026 bands

| Monthly net income | Attachable portion |
| --- | --- |
| Up to EUR 1,419.00 | Nothing |
| EUR 1,419.01 – 1,524.00 | 20% |
| EUR 1,524.01 – 1,682.00 | 30% |
| EUR 1,682.01 – 1,839.00 | 40% |
| Above EUR 1,839.00 | 100% |

Replacement income (unemployment benefit, sickness benefit, pension) follows the same thresholds, but the two middle bands are merged so that 40% is attachable across the whole range from EUR 1,524.01 to EUR 1,839.00, and the portion above EUR 1,839.00 is fully attachable.

Dependent children. The protected amount is increased by EUR 88 per dependent child from 1 January 2026. The child must be under 25 or under extended guardianship, must be maintained by the employee, and must not have net own resources above the thresholds fixed by the same decree (EUR 4,015 where the parent cohabits, EUR 5,799 for a single parent, EUR 7,352 for a child with a disability). The employee claims the increase by filing the statutory declaration form with the creditor and the employer.

The base for the bands is the net income — the gross less social security contributions, withholding tax and the special social security contribution — before any contractual deduction.

Worked example

An employee with a net monthly income of EUR 2,100.00 and one dependent child, subject to an ordinary garnishment for a consumer debt.

| Step | Calculation | Result (EUR) |
| --- | --- | --- |
| Protected floor | 1,419.00 + 88.00 for one child | 1,507.00 |
| Band 20% | From 1,507.00 to 1,612.00 (bands shifted by the child supplement) | 21.00 |
| Band 30% | From 1,612.01 to 1,770.00 | 47.40 |
| Band 40% | From 1,770.01 to 1,927.00 | 62.80 |
| Band 100% | 2,100.00 − 1,927.00 | 173.00 |
| Total attachable | 21.00 + 47.40 + 62.80 + 173.00 | 304.20 |
| Paid to the employee | 2,100.00 − 304.20 | 1,795.80 |

Had the debt been a maintenance obligation, the whole EUR 2,100.00 would have been attachable and the bands would not have applied.

Legal basis: Judicial Code, Articles 1409, 1409bis, 1410, 1411 and 1412; Royal Decree of 3 December 2025 implementing Article 1409, §2 of the Judicial Code (Belgian Official Gazette, 10 December 2025); Wage Protection Act of 12 April 1965, Articles 23 and 27 to 35.

## Module 8: Statutory Leave Management

### 8.1 Leave Entitlements

#### For each type of statutory leave, what are the eligibility criteria and accrual methodology?

Belgian annual leave is built on a service-year system: the entitlement taken in a calendar year (the holiday year, vakantiejaar) is earned in the preceding calendar year (the holiday service year, vakantiedienstjaar). Leave taken in 2026 is therefore earned by the work performed in 2025.

| Leave type | Eligibility | Accrual |
| --- | --- | --- |
| Statutory annual leave | All employees | 4 weeks for a full holiday service year — 20 days on a five-day week, 24 days on a six-day week. Prorated on the months worked and on equivalent days in the service year |
| European leave (Europese vakantie) | Employees starting or restarting work who have no or insufficient accrued entitlement | After a three-month qualifying period in the year of starting, the employee may take leave in advance; the pay is an advance on the following year's double holiday pay |
| Supplementary leave | Same population, as an extension of the European leave mechanism | Up to the full four-week entitlement in the first year |
| Public holidays | All employees | 10 paid days per year, plus replacement days for holidays falling on a non-working day |
| Sickness or accident (guaranteed salary) | All employees; blue-collar workers need one month of uninterrupted service | 30 calendar days at the employer's expense for white-collar staff on an indefinite contract or a contract of at least three months |
| Maternity leave | Pregnant employees | 15 weeks (17 for multiple births, extendable to 19), of which 6 prenatal (1 compulsory) and 9 compulsory postnatal |
| Birth leave (geboorteverlof) | The parent other than the mother with a legal link to the child | 20 days, freely taken within four months of the birth. For children born from 2026, an additional week of 5 separate days may be taken until the child's first birthday |
| Adoption and foster-parent leave | Adoptive and foster parents | 6 weeks per parent, with the statutory increases |
| Parental leave | Employees with one year of service in the 15 months before the request | 4 months full-time per child under 12, or the equivalent in half-time, one-fifth or one-tenth reduction |
| Thematic leave — medical assistance, palliative care | Per the scheme conditions | Full-time or reduced, with a National Employment Office allowance |
| Time credit with a motive | Per CBA no. 103 and the sector | Duration per motive, with a National Employment Office allowance |
| Care leave and force majeure leave | All employees | 10 days of care leave per year (unpaid) and short absences for compelling family reasons |
| Short leave (klein verlet) | All employees | Paid days for defined family events — marriage, birth, death, communion — per the Royal Decree of 28 August 1963 |
| Paid educational leave / Flemish training leave | Employees following a recognised course | Per the regional scheme; the employer pays and claims reimbursement |
| Political leave | Employees holding an elected local mandate | Per the specific statute |

#### How are unpaid or partially paid leaves handled?

| Category | Treatment |
| --- | --- |
| Fully paid by the employer | Annual leave, public holidays, short leave, the first period of sickness (guaranteed salary), the Flemish or regional training leave (reimbursed afterwards) |
| Paid by a public authority | Maternity leave, birth leave from day 4 onwards, parental and thematic leave, sickness after the guaranteed salary period, temporary unemployment |
| Partially paid | Birth leave — the first 3 days at the employer's full expense, the following 17 days at 82% of the capped gross paid by the health insurance fund. Sickness for blue-collar workers — 7 days at full pay, then a reducing scale |
| Unpaid | Care leave, force majeure leave beyond the paid days, unpaid leave agreed between the parties, unauthorised absence |

For any day that is not paid by the employer, payroll must suppress the salary for that day using the applicable proration method (Module 4.3), record the day with the correct DmfA absence code, and ensure that the day is or is not counted as equivalent for holiday accrual according to the code used. The DmfA absence code is the single most important field here, because it drives both the employee's benefit entitlement and the holiday accrual.

#### Which wage types are affected by unpaid/partially paid leave?

| Wage type | Effect of an unpaid day |
| --- | --- |
| Basic monthly salary | Reduced by the value of the day |
| Fixed monthly premiums | Reduced in the same proportion, unless the CBA says otherwise |
| Variable pay based on hours worked | Naturally reduced |
| Meal vouchers | Not granted — the entitlement follows days actually worked |
| Company car benefit | Unaffected — the benefit follows the availability of the vehicle, not attendance |
| Homeworking and bicycle allowances | Reduced or suspended, since they reimburse costs actually incurred |
| Holiday accrual | Reduced, unless the absence is an equivalent day under the Royal Decree of 30 March 1967 (sickness within the guaranteed period, maternity leave, and certain thematic leaves are equivalent; ordinary unpaid leave is not) |
| End-of-year premium | Reduced per the sectoral CBA rules on qualifying absences |
| Seniority for notice purposes | Unaffected — the contract continues to run during suspension |
| Employee and employer social security contributions | Reduced, because there is less wage. The employment relationship itself continues |

#### Are there any mandatory national military service leaves?

No. Compulsory military service in Belgium has been suspended since 1 January 1994 by the Law of 31 December 1992. There is therefore no statutory military service leave to configure.

Two residual items exist and are marginal for payroll: voluntary military service, which is an employment relationship with the Ministry of Defence rather than a leave from a civilian employer, and the specific leave arrangements for reservists, which are contractual or governed by the Defence statute rather than by general labour law.

#### Are any other kinds of leave paid by government authorities?

Yes, and this is a defining feature of the Belgian system: after a short employer-funded period, income replacement is taken over by public institutions.

| Leave | Paying authority | Amount |
| --- | --- | --- |
| Sickness after the guaranteed salary period | Health insurance fund, under the National Institute for Health and Disability Insurance | 60% of the capped gross during the first year of incapacity |
| Maternity leave | Health insurance fund | 82% of the uncapped gross for the first 30 days, then 75% of the capped gross |
| Birth leave from day 4 | Health insurance fund | 82% of the capped gross |
| Adoption and foster-parent leave | Health insurance fund | 82% of the capped gross after the employer-paid days |
| Parental leave, thematic leave, time credit | National Employment Office | Flat monthly allowance per scheme |
| Temporary unemployment (economic, weather, force majeure) | National Employment Office | A percentage of the capped gross, plus any sectoral supplement |
| Holiday pay for blue-collar workers | Holiday fund, under the National Annual Holidays Office | 15.38% of the gross of the service year at 108% |
| Work accident benefit | The employer's private work accident insurer | Per the Law of 10 April 1971 |

Payroll's role for these is to stop the salary, produce the correct DmfA absence code and, where applicable, the electronic scenario declaration (ASR) that triggers the benefit, and to pay any sectoral supplement.

#### What are the payout rules for statutory leaves?

White-collar employees — the employer pays both components:

| Component | Rule |
| --- | --- |
| Single holiday pay | The normal salary continues to be paid for the days of leave taken. For a monthly-paid employee this means the salary is simply not reduced |
| Double holiday pay | 92% of the gross monthly salary, prorated on the months of the holiday service year that were worked or equivalent. Paid once a year, usually in May or June |

Blue-collar workers — the holiday fund pays:

| Component | Rule |
| --- | --- |
| Total holiday pay | 15.38% of the gross earned in the holiday service year at 108%, of which 8% is single holiday pay and 7.38% double holiday pay |
| Payment | Made directly by the holiday fund or a sectoral fund, normally between May and June. The employer pays nothing at the time of the leave |

Withholding tax on double holiday pay uses its own table, keyed on the annual gross remuneration:

| Annual gross remuneration | Rate |
| --- | --- |
| Up to EUR 10,675.00 | 0.00% |
| EUR 10,675.01 – 13,660.00 | 19.17% |
| EUR 13,660.01 – 17,375.00 | 21.20% |
| EUR 17,375.01 – 20,840.00 | 26.25% |
| EUR 20,840.01 – 23,580.00 | 31.30% |
| EUR 23,580.01 – 26,340.00 | 34.33% |
| EUR 26,340.01 – 31,830.00 | 36.34% |
| EUR 31,830.01 – 34,640.00 | 39.37% |
| EUR 34,640.01 – 45,860.00 | 42.39% |
| EUR 45,860.01 – 59,900.00 | 47.44% |
| Above EUR 59,900.00 | 53.50% |

The employee contribution of 13.07% is withheld on the double holiday pay; employer contributions are not due on it.

Sickness during annual leave. Since 1 January 2024, an employee who falls sick during a period of annual leave keeps the leave days: the days are converted into sickness days, the guaranteed salary applies, and the leave days are recovered and may be taken later, including after 31 December where the employee could not take them.

#### How are unused paid leaves treated upon termination?

Unused statutory leave is never paid out as such. Instead, the employer settles the departure holiday pay (vertrekvakantiegeld), which covers both the leave already accrued for the following holiday year and the leave of the current year not yet taken.

White-collar employees

| Component | Rate | Base |
| --- | --- | --- |
| Departure holiday pay for the current year | 15.34% | The gross earned in the current calendar year, less any holiday pay already paid |
| Departure holiday pay for the previous service year, where the double holiday pay has not yet been paid | 15.34% | The gross of the previous year |
| Split of the 15.34% | 7.67% single + 7.67% double | — |

The departure holiday pay is subject to the 13.07% employee contribution and is taxed as an exceptional payment. The employer issues a holiday certificate (vakantieattest) stating the amounts paid, and the next employer deducts the corresponding value when the employee takes leave, so that the employee is not paid twice.

Blue-collar workers — nothing is settled by the employer on termination. The holiday fund pays the entitlement in the following year on the basis of the DmfA data.

#### Provide the calculation logic for each leave type where applicable.

Annual leave accrual

Days of leave (five-day week)

= 20 x (months worked or equivalent in the holiday service year) / 12

rounded up to the nearest half day

Double holiday pay, white-collar, worked example 2026

An employee on a gross monthly salary of EUR 3,600.00 who worked the whole of 2025.

| Step | Calculation | Result (EUR) |
| --- | --- | --- |
| Gross double holiday pay | 3,600.00 x 92% x 12/12 | 3,312.00 |
| Employee social security | 3,312.00 x 13.07% | −432.88 |
| Taxable amount | — | 2,879.12 |
| Annual gross remuneration for the table | 3,600.00 x 13.92 | 50,112.00 |
| Rate from the holiday-pay table | Band 45,860.01 – 59,900.00 | 47.44% |
| Withholding tax | 2,879.12 x 47.44% | −1,365.85 |
| Net double holiday pay | — | 1,513.27 |

The reference remuneration uses the factor 13.92 — twelve monthly salaries plus the double holiday pay and the end-of-year premium — as Module 6.2 prescribes for every exceptional payment. Keying the table on 12 monthly salaries instead would understate the reference and select a lower band.

Employer social security contributions are not due on this amount.

Departure holiday pay, white-collar, worked example

The same employee leaves on 30 June 2026 having earned EUR 21,600.00 gross in 2026 and having already received the 2026 double holiday pay for service year 2025.

Departure holiday pay = 21,600.00 x 15.34% = EUR 3,313.44

of which single = 21,600.00 x 7.67% = EUR 1,656.72

of which double = 21,600.00 x 7.67% = EUR 1,656.72

The single part is taxed at the ordinary scale as remuneration; the double part is taxed at the holiday-pay percentage. Both parts carry the 13.07% employee contribution.

Guaranteed salary during sickness

| Population | Days 1 to 7 | Days 8 to 14 | Days 15 to 30 |
| --- | --- | --- | --- |
| White-collar, indefinite contract or contract of at least 3 months | 100% of normal pay | 100% | 100% |
| Blue-collar, after one month of service | 100% | 85.88% of the gross | 25.88% of the gross up to the ceiling and 85.88% of the part above, with the health insurance fund paying the balance |

Two changes took effect on 1 January 2026 and must be configured:

The relapse period was extended from 14 days to 8 weeks. Where an employee falls sick again within 8 weeks of a previous incapacity, no new guaranteed salary period starts unless the balance of the previous period is unused or the employee proves a different illness.

No guaranteed salary is due for an incapacity arising during a period of progressive work resumption.

Maternity leave — the employer pays nothing during the 15 weeks. The health insurance fund pays 82% of the uncapped gross for the first 30 days and 75% of the capped gross thereafter. Any employer top-up agreed by CBA is ordinary taxable and contributory wage.

Birth leave — the employer pays the normal salary for the first 3 days; days 4 to 20 are paid by the health insurance fund at 82% of the capped gross. For children born from 2026 an additional week of 5 days may be taken until the first birthday, on the same basis.

#### How does extended unpaid leave impact social security contributions, tax status, and accrual?

| Dimension | Effect |
| --- | --- |
| Employment contract | Suspended, not terminated. Seniority continues to run for notice purposes |
| Social security contributions | No wage, therefore no contributions. The employee remains affiliated but accrues no new rights for the unpaid period unless the period is assimilated |
| Social security cover | Health insurance cover continues for a period; a long unpaid absence can put continued entitlement at risk and the employee should be referred to the health insurance fund |
| Pension accrual | Ordinary unpaid leave is not assimilated and creates a gap in the career; thematic leave and time credit with a motive are assimilated within their limits |
| Holiday accrual | Ordinary unpaid days are not equivalent days and reduce the following year's entitlement and holiday pay. Maternity leave, sickness within the guaranteed period, and certain thematic leaves are equivalent and preserve accrual |
| Income tax | No remuneration, therefore no withholding. The employee's annual taxable income falls and the personal income tax assessment reflects it. Where a fixed annual benefit continues to be provided (a company car retained during the leave) the benefit remains taxable and the withholding must be funded |
| End-of-year premium | Reduced per the sectoral CBA |
| Meal vouchers | Not granted for unpaid days |
| DmfA | The days are declared with the appropriate absence code; the employment line remains open |

The practical configuration rule is that unpaid leave suspends the pay, not the employment: master data, benefits and statutory declarations continue, and only the wage types tied to time worked are switched off.

Legal basis: Royal Decree of 30 March 1967 and coordinated laws of 28 June 1971 on annual holidays; Law of 4 January 1974 on public holidays; Employment Contracts Act of 3 July 1978, Articles 52, 54, 70 and following; Labour Act of 16 March 1971 (maternity protection); Royal Decree of 28 August 1963 (short leave); CBA no. 103 (time credit); Law of 31 December 1992 suspending compulsory military service; Law of 17 July 2023 on annual leave and sickness during leave; Law of 19 December 2025 implementing a reinforced return-to-work policy for incapacity for work (relapse period extended from 14 days to 8 weeks; the 20-week limit on neutralising guaranteed salary during progressive work resumption removed); Annex III to the Royal Decree implementing ITC 92 (holiday pay withholding scale, 2026 version).

## Module 9: Termination & Irregular Payments

### 9.1 Termination Payments

#### What are the different types of termination payments?

| Payment | Trigger | Social security | Income tax |
| --- | --- | --- | --- |
| Salary for the notice period worked | Notice served and worked | Ordinary | Ordinary scale |
| Notice indemnity (opzeggingsvergoeding / verbrekingsvergoeding) | Contract ended without notice, or with insufficient notice | Full employee and employer contributions | Separate taxation at the average rate of the last normal year |
| Departure holiday pay (vertrekvakantiegeld) | Any termination of a white-collar contract | Employee contribution of 13.07% | Single part at the ordinary scale, double part at the holiday-pay rate |
| Pro rata end-of-year premium | Where the sectoral CBA provides it | Ordinary | Exceptional-payment rate |
| Outstanding variable pay, commission, expenses | Contract | Per the item | Per the item |
| Protection indemnity — unfair dismissal under CBA no. 109 | Dismissal manifestly unreasonable | Treated as damages, not wage | Taxed as an indemnity for loss of income where it replaces remuneration |
| Protection indemnity — discrimination, pregnancy, works council or prevention committee member | Breach of a protected status | Damages; generally outside the wage concept where they repair non-professional damage | Follows the same analysis |
| Non-competition indemnity | Enforcement of a non-competition clause | Not wage; a separate levy applies | Taxed separately |
| Dismissal compensation allowance (ontslagcompensatievergoeding) | Blue-collar workers with pre-2014 seniority | Paid by the National Employment Office, not by the employer | Taxable |
| Supplementary allowance under the unemployment-with-company-supplement scheme | Restructuring or age-based schemes | Specific employer contributions | Specific regime |
| Outplacement | Dismissal with a notice or indemnity of at least 30 weeks | Not a cash payment; a service | Not taxable to the employee |

#### How do termination rules and calculations differ by residential status and employer type?

By residential status. The labour-law calculation — notice period, indemnity, holiday pay — is identical for residents and non-residents, because it flows from the employment contract and the Belgian Employment Contracts Act, not from tax residence. The differences are on the tax side:

| Aspect | Resident | Non-resident |
| --- | --- | --- |
| Withholding on the indemnity | Annex III nr. 58 arrears-and-severance percentage, to which nr. 62 routes notice indemnities, keyed on the remuneration that served as the basis for the indemnity | Same percentage; under scale III no family reduction is applied |
| Final taxation | Separate taxation at the average rate of the last previous year with normal professional activity | Same domestic rule, subject to the applicable double tax treaty. Where the employment was exercised partly abroad, the indemnity is in principle allocated in proportion to the place where the work was performed during the reference period |
| Reporting | Form 281.10 | Form 281.10, with the non-resident indicators |

By employer type. The private-sector rules described here apply to all private employers. Three variations matter:

Public-sector employers and statutory staff follow their own administrative statutes and are outside this scope.

Sectoral variation is significant: many joint committees add supplementary indemnities, extended notice arrangements or sectoral outplacement obligations on top of the statutory minimum.

Employers in restructuring recognised by the Minister of Employment can access reduced notice arrangements and the employment-cell obligations, which change both the calculation and the reporting.

#### Detail the calculation and tax withholding rules for unused leave paid out on termination.

Belgium does not pay out unused leave days as such. It settles the departure holiday pay, which discharges both the untaken leave of the current year and the entitlement already earned for the following year.

White-collar employees

Departure holiday pay = 15.34% x gross earned in the reference period

of which single holiday pay   = 7.67%

of which double holiday pay   = 7.67%

Two amounts may be due at the same time: 15.34% on the gross of the current calendar year, and 15.34% on the gross of the previous year where the double holiday pay for that service year has not yet been paid.

| Component | Social security | Withholding tax |
| --- | --- | --- |
| Single departure holiday pay | 13.07% employee contribution, ordinary employer contributions | Exceptional-payment percentage table |
| Double departure holiday pay | 13.07% employee contribution; no employer contributions | Holiday-pay percentage table |

The employer must issue a holiday certificate stating the gross amounts paid and the number of days covered. The next employer deducts the corresponding value when the employee takes leave, which is why the certificate is a mandatory take-on document in Module 2.2.

Blue-collar workers — nothing is paid by the employer. The holiday fund settles the entitlement in the following year on the basis of the DmfA data.

#### Describe the rules for statutory severance/redundancy payments.

Belgium has no severance pay in the sense of a lump sum tied to years of service. What exists is the notice obligation: the employer must either let the employee work a statutory notice period or pay an indemnity equal to the remuneration for that period.

Notice indemnity = current remuneration x length of the notice period

where "current remuneration" is the gross salary in force at the time

of dismissal, INCLUDING all benefits acquired under the contract:

- the taxable value of the company car

- meal vouchers (the employer's share)

- variable pay, averaged over the preceding 12 months

- the pro rata end-of-year premium and holiday pay

- group insurance and hospitalisation premiums

Statutory notice periods on dismissal by the employer — contracts started from 1 January 2014:

| Seniority | Weeks | Seniority | Weeks |
| --- | --- | --- | --- |
| Less than 3 months | 1 | 8 to 9 years | 27 |
| 3 to 4 months | 3 | 9 to 10 years | 30 |
| 4 to 5 months | 4 | 10 to 11 years | 33 |
| 5 to 6 months | 5 | 11 to 12 years | 36 |
| 6 to 9 months | 6 | 12 to 13 years | 39 |
| 9 to 12 months | 7 | 13 to 14 years | 42 |
| 12 to 15 months | 8 | 14 to 15 years | 45 |
| 15 to 18 months | 9 | 15 to 16 years | 48 |
| 18 to 21 months | 10 | 16 to 17 years | 51 |
| 21 to 24 months | 11 | 17 to 18 years | 54 |
| 2 to 3 years | 12 | 18 to 19 years | 57 |
| 3 to 4 years | 13 | 19 to 20 years | 60 |
| 4 to 5 years | 15 | 20 to 21 years | 62 |
| 5 to 6 years | 18 | 21 to 22 years | 63 |
| 6 to 7 years | 21 | 22 to 23 years | 64 |
| 7 to 8 years | 24 | 23 years and above | 65 |

Two reforms take effect during 2026 and must both be configured.

| Contracts whose performance started | Rule |
| --- | --- |
| From 1 January 2014 to 31 May 2026 | The table above, rising to 65 weeks |
| From 1 June 2026 to 31 July 2026 | The same table, but the notice period is capped at 52 weeks from 17 years of seniority |
| From 1 August 2026 | The first six months of seniority carry a uniform notice of 1 week, the bands from 6 to 12 months are unchanged (6 and 7 weeks), the remainder of the table applies, and the cap of 52 weeks from 17 years applies |

Resignation by the employee — notice periods are shorter and capped at 13 weeks.

*Employees with seniority before 1 January 2014 — the two-part (dubbele foto / double photo) calculation.* Where the contract began before 1 January 2014, the notice is the sum of two separately computed parts (Law of 26 December 2013, Articles 67 to 69):

Part 1 covers seniority acquired up to and including 31 December 2013 and is frozen at that date, computed under the statutory, regulatory and collectively agreed rules that were in force on 31 December 2013 — including the joint committee's rules as they then stood, irrespective of any later sectoral change.

Part 2 covers seniority acquired from 1 January 2014 and is computed under the table above as if the employee had started on 1 January 2014: the seniority counter is reset to zero.

The two results are added. The 52-week cap and the 2026 reform regimes described below bear on Part 2 only; Part 1 is not recomputed.

Part 1 — the rules as they stood on 31 December 2013, dismissal by the employer

| Status on 31 December 2013 | Test | Part 1 notice |
| --- | --- | --- |
| Blue-collar worker — sector has its own periods | The joint committee's conventional periods in force on 31/12/2013 | The sectoral periods, which prevail over the general rules below |
| Blue-collar worker — no sectoral periods, contract begun from 1 January 2012 | CBA no. 75 of 20 December 1999 | Under 6 months 28 days; 6 months to under 5 years 35 days; 5 to under 10 years 42 days; 10 to under 15 years 56 days; 15 to under 20 years 84 days; 20 years and over 112 days |
| Blue-collar worker — no sectoral periods, contract begun before 1 January 2012 | Employment Contracts Act, Article 59 as it read on 31/12/2013 | Under 20 years 28 days; 20 years and over 56 days |
| White-collar, lower — annual gross remuneration at or below EUR 32,254 on 31/12/2013 | Employment Contracts Act, Article 82 §2 as it read on 31/12/2013 | 3 months per commenced period of 5 years of seniority acquired to 31/12/2013 |
| White-collar, higher — annual gross remuneration above EUR 32,254 on 31/12/2013, no valid pre-2014 notice clause | Law of 26 December 2013, Article 68, third paragraph | 1 month per commenced year of seniority acquired to 31/12/2013, with a minimum of 3 months |
| White-collar, higher, with a notice clause validly agreed no later than 31 December 2013 | Law of 26 December 2013, Article 68, as completed by the Law of 26 October 2023 | The agreed clause governs Part 1, in place of the row above |

Four points that decide the build and are easy to get wrong:

The higher white-collar Part 1 is a statutory formula, not the Claeys formula. The Claeys formula was market practice for fixing notice for higher white-collar employees before 2014 and is still used to value claims in litigation, but Article 68 of the Law of 26 December 2013 replaced it for the frozen Part 1 with the flat 1-month-per-commenced-year rule above. A payroll engine must apply the statutory rule; it must not implement Claeys.

That rule survived a legislative accident and is current. The Law of 20 March 2023, in force 28 October 2023, repealed the third and fourth paragraphs of Article 68. For higher white-collar dismissal this was unintended, and a corrective law adopted on 26 October 2023 restored the third paragraph before the repeal could take effect, adding the notice-clause rule in the table above. Commentary written between March and October 2023 states that the rule was abolished and that Part 1 reverts to Article 82 §3 of the Employment Contracts Act as it read on 31/12/2013 — that is, to agreement or court determination, in practice Claeys. That commentary describes a state of the law that never came into force; do not build from it.

The EUR 32,254 threshold is read at 31 December 2013 and is never indexed forward. It is a historical constant, not a 2026 parameter. The employee's 2026 salary is irrelevant to it.

Part 1 is master data, not a computation. The engine cannot derive it from anything it holds in 2026: it needs the status, the seniority and the annual remuneration as at 31 December 2013, the joint committee that applied then, and any pre-2014 notice clause. These must be carried as stored fields on the employee record and migrated at implementation; an engine that computes seniority only from the hire date will silently produce Part 2 alone and under-state the indemnity for every employee hired before 2014.

Resignation by the employee — the two-part calculation does not apply at all. The Law of 20 March 2023, in force 28 October 2023, abolished the transitional two-part rule for resignations. Every employee who resigns, blue-collar or white-collar, whatever the date the contract began, serves only the notice of Article 37/2 §2 of the Employment Contracts Act, capped at 13 weeks. Pre-2014 seniority gives no additional resignation notice. The employer-dismissal two-part rule above is unaffected by this change.

Outplacement. Where the notice or indemnity is at least 30 weeks, the employer must offer an outplacement package of 60 hours, valued at one twelfth of the gross annual remuneration of the calendar year preceding the dismissal, with a floor of EUR 1,800 and a ceiling of EUR 5,500. Where the contract is ended with an indemnity, the employer may deduct 4 weeks of the indemnity as consideration for the outplacement offered.

#### Provide the statutory formula for any tax-free portion.

There is no tax-free portion of a Belgian notice indemnity. The whole amount is taxable and fully subject to social security contributions. The concession Belgium grants is a rate concession, not an exemption:

Tax on the notice indemnity

= indemnity x average tax rate of the total net taxable income of the

most recent previous year in which the taxpayer had a normal

professional activity

(ITC 92, Article 171, 5°, a)

The withholding taken at source is not that average rate — the employer cannot know it — but a single percentage from the Annex III arrears and notice-indemnity scale of nr. 58, to which nr. 62 routes notice indemnities. It is not the exceptional-payment table of nr. 53: that provision applies in terms only to exceptional allowances other than notice indemnities (andere exceptionele vergoedingen en toelagen dan opzeggingsvergoedingen). Under nr. 62 the percentage is keyed on the remuneration that served as the basis for determining the indemnity. The difference between the withholding and the definitive separate taxation is settled in the annual assessment. Where the separate rate would be higher than the ordinary progressive taxation of the whole income, the ordinary rate applies instead, so the mechanism can never disadvantage the employee.

Annex III nr. 58 — withholding percentages on notice indemnities and arrears, income year 2026

| Reference remuneration (EUR) | % | Reference remuneration (EUR) | % |
| --- | --- | --- | --- |
| Up to 11,860.00 | 0.00 | 42,695.01 – 55,355.00 | 31.30 |
| 11,860.01 – 14,235.00 | 2.68 | 55,355.01 – 62,465.00 | 36.90 |
| 14,235.01 – 15,810.00 | 6.57 | 62,465.01 – 71,160.00 | 38.96 |
| 15,810.01 – 18,980.00 | 10.77 | 71,160.01 – 83,020.00 | 40.93 |
| 18,980.01 – 20,565.00 | 13.55 | 83,020.01 – 99,630.00 | 42.92 |
| 20,565.01 – 22,935.00 | 16.55 | 99,630.01 – 124,925.00 | 44.99 |
| 22,935.01 – 26,885.00 | 19.17 | 124,925.01 – 143,905.00 | 46.47 |
| 26,885.01 – 34,790.00 | 24.92 | 143,905.01 – 169,205.00 | 47.48 |
| 34,790.01 – 42,695.00 | 29.93 | Above 169,205.00 | 48.00 |

This scale has eighteen bands and tops out at 48.00%, materially below the exceptional-payment table's 53.50%. It is deliberately constructed so that the withholding approximates the Article 171 average rate rather than exceeding it, which is why a correctly withheld notice indemnity produces only a small settlement difference at assessment. A large excess to be refunded is a signal that the nr. 53 table has been applied by mistake, not normal Belgian practice.

Genuinely tax-free amounts on termination are narrow and must each be substantiated:

| Item | Treatment |
| --- | --- |
| Damages repairing non-professional damage (moral damage, damage to reputation) | Not remuneration; not taxable and not contributory, provided the compensatory nature is documented in the settlement |
| Reimbursement of expenses actually incurred up to the departure date | Not taxable |
| The value of the outplacement service | Not a taxable benefit to the employee |
| Payment of legal costs under a court order | Not remuneration |

Everything characterised as compensation for the loss of remuneration is taxable in full.

#### Deliverable: Reference guide for other Employment Termination Payments

| Payment | Legal source | Amount | Social security | Withholding |
| --- | --- | --- | --- | --- |
| Notice indemnity | Employment Contracts Act, Articles 37/2 and 39 | Remuneration for the statutory notice period | Full | Annex III nr. 58 percentage (routed there by nr. 62), 0.00% to 48.00% |
| Departure holiday pay | Royal Decree of 30 March 1967 | 15.34% of the reference gross | Employee 13.07%; employer only on the single part | Ordinary scale on the single part; holiday-pay table on the double part |
| Pro rata end-of-year premium | Sectoral CBA | Per the sector, usually months of service / 12 | Full | Exceptional-payment percentage |
| Unfair dismissal indemnity, CBA no. 109 | CBA no. 109 | 3 to 17 weeks of remuneration | Treated as damages | Taxed as an indemnity replacing income |
| Discrimination indemnity | Anti-discrimination laws of 10 May 2007 | 6 months of gross remuneration, or actual damage | Damages | Per the analysis of the compensated damage |
| Pregnancy or maternity protection indemnity | Labour Act, Article 40 | 6 months of gross remuneration | Damages | Per the analysis |
| Works council or prevention committee member indemnity | Law of 19 March 1991 | A fixed part by seniority plus a variable part | Specific regime | Per the analysis |
| Non-competition indemnity | Employment Contracts Act, Article 65 | At least half the gross remuneration for the duration of the clause | Not wage; a specific contribution applies | Separate taxation |
| Dismissal compensation allowance | Law of 26 December 2013 | Per the transitional rules for pre-2014 blue-collar seniority | Paid by the National Employment Office | Taxable |
| Supplementary allowance under the unemployment-with-company-supplement scheme | CBA no. 17 and sectoral CBAs | Per the scheme | Specific employer contributions, including the Decava levies | Specific regime |
| Company car returned late, or retained after termination | Contract | The benefit continues to be taxable while the car is available | CO2 contribution continues | Ordinary scale |

#### Deliverable: Rules for any applicable concessional tax cap

Belgium applies no cap on the amount of a termination payment that benefits from the concessional treatment. The whole indemnity, however large, is taxed separately at the average rate of the last normal year.

Two caps that exist in the neighbouring rules and are frequently confused with a tax cap:

| Cap | What it limits | 2026 value |
| --- | --- | --- |
| Notice period cap | The length of the notice, and therefore the size of the indemnity | 65 weeks for contracts started before 1 June 2026; 52 weeks from 17 years of seniority for contracts started from 1 June 2026 |
| Outplacement value | The value of the outplacement service | Floor EUR 1,800, ceiling EUR 5,500, with 4 weeks deductible from the indemnity |

The absence of a tax cap has one important consequence for high earners: the separate rate is compared with the ordinary progressive taxation of all income, and the more favourable of the two applies. An employee with a very low reference year can therefore end up with a very low average rate on a very large indemnity.

#### Deliverable: Detailed worked example of a redundancy termination payout

Facts. A white-collar employee in joint committee 200, single with no dependants, dismissed with immediate effect on 30 April 2026. Gross monthly salary EUR 4,500.00. Seniority from 1 March 2014, so 12 years and 2 months at the date of dismissal. Company car with a monthly taxable benefit of EUR 250.00. Meal vouchers of EUR 10.00 per worked day, employer share EUR 8.91. End-of-year premium under the sectoral CBA equal to one gross month. Average tax rate of the last normal year: 38.5%. Gross earned in 2026 up to 30 April: EUR 18,000.00.

Step 1 — Notice period. Contract started before 1 June 2026, so the table rising to 65 weeks applies. Seniority of 12 to 13 years gives 39 weeks.

Step 2 — Current remuneration for the indemnity.

| Element | Monthly value (EUR) |
| --- | --- |
| Gross salary | 4,500.00 |
| Company car benefit | 250.00 |
| Employer share of meal vouchers (20 days x 8.91) | 178.20 |
| Pro rata end-of-year premium (one month / 12) | 375.00 |
| Pro rata double holiday pay (92% of a month / 12) | 345.00 |
| Monthly current remuneration | 5,648.20 |
| Annual current remuneration | 67,778.40 |

Step 3 — Notice indemnity.

Indemnity = 67,778.40 x 39 / 52 = EUR 50,833.80

Step 4 — Outplacement deduction. The notice exceeds 30 weeks, so outplacement is due and 4 weeks may be deducted:

Deduction = 67,778.40 x 4 / 52 = EUR 5,213.72

Indemnity after deduction = 50,833.80 − 5,213.72 = EUR 45,620.08

Step 5 — Social security on the indemnity.

Employee contribution = 45,620.08 x 13.07% = EUR 5,962.54

Taxable amount        = 45,620.08 − 5,962.54 = EUR 39,657.54

Employer contribution = 45,620.08 x approximately 25% = EUR 11,405.02

Step 6 — Withholding tax on the indemnity. The indemnity takes the Annex III nr. 58 percentage, not the nr. 53 exceptional-payment percentage. Under nr. 62 the reference is the remuneration that served as the basis for determining the indemnity, which is the annual current remuneration established in Step 2: EUR 67,778.40. That falls in the band EUR 62,465.01 – 71,160.00, so the rate is 38.96%:

Withholding = 39,657.54 x 38.96% = EUR 15,450.58

The monthly gross x 13.92 = EUR 62,640.00 reading of the reference falls in the same nr. 58 band, so the rate is 38.96% either way. Applying the nr. 53 top rate of 53.50% instead would have withheld EUR 21,216.78 — an over-withholding of EUR 5,766.20 on this single settlement.

Step 7 — Other final settlement items.

| Item | Gross (EUR) | Employee social security (EUR) | Withholding rate | Withholding (EUR) |
| --- | --- | --- | --- | --- |
| April salary | 4,500.00 | 588.15 | Ordinary scale, taxable base includes the EUR 250.00 monthly car benefit (enjoyed through 30 April) | 1,156.36 |
| Departure holiday pay, current year: 18,000.00 x 15.34% | 2,761.20 | 360.89 | 7.67% single at 53.50%, 7.67% double at 53.50% (both halves fall in the top band since the reference remuneration exceeds EUR 59,900 in both tables) | 1,284.17 |
| Pro rata end-of-year premium: 4,500.00 x 4/12 | 1,500.00 | 196.05 | 53.50% applied to 1,500.00 − 196.05 = 1,303.95 | 697.61 |

Step 8 — Summary of the payout.

| Line | Gross (EUR) | Employee social security (EUR) | Withholding (EUR) | Net (EUR) |
| --- | --- | --- | --- | --- |
| April salary | 4,500.00 | 588.15 | 1,156.36 | 2,755.49 |
| Notice indemnity after outplacement deduction | 45,620.08 | 5,962.54 | 15,450.58 | 24,206.96 |
| Departure holiday pay | 2,761.20 | 360.89 | 1,284.17 | 1,116.14 |
| Pro rata end-of-year premium | 1,500.00 | 196.05 | 697.61 | 606.34 |
| Total | 54,381.28 | 7,107.63 | 18,588.72 | 28,684.93 |

Step 9 — Definitive taxation. The indemnity of EUR 39,657.54 taxable is finally taxed separately at the average rate of the last normal year, 38.5%, giving EUR 15,268.15 against EUR 15,450.58 withheld. The excess of only EUR 182.43 is refunded through the personal income tax assessment for income year 2026, issued during 2027. The closeness of the two figures — 38.96% withheld against 38.5% finally due — is the nr. 58 scale working as designed: it is built to approximate the Article 171 average rate. A large refund on a notice indemnity should therefore be investigated rather than explained away, because it usually means the nr. 53 exceptional-payment table was applied instead of nr. 58.

Legal basis: Employment Contracts Act of 3 July 1978, Articles 37/2, 37/4, 39, 59 and 82 as those last two read on 31 December 2013, 65, 86/1 to 86/4; Law of 26 December 2013 on the unified status, Articles 67 to 69 (the two-part calculation for pre-2014 seniority), Article 68, third paragraph as repealed by the Law of 20 March 2023 and restored and completed by the Law of 26 October 2023, both in force 28 October 2023; Law reforming notice periods with effect from 1 June and 1 August 2026; CBA no. 75 of 20 December 1999 (blue-collar notice periods applicable on 31 December 2013); CBA no. 109; CBA no. 82 (outplacement); Income Tax Code 1992, Articles 171, 5° and 270 to 275; Annex III to the Royal Decree implementing ITC 92, nrs. 53, 58 to 60 and 62 (notice indemnities take the arrears-and-severance scale of nr. 58, nr. 53 excluding them in terms); Royal Decree of 30 March 1967.

### 9.2 Irregular and Retrospective Payments

#### Describe the specific tax calculation method required for irregular payments.

Irregular payments are taxed under the exceptional remuneration mechanism, not the monthly scale. The method is:

1. Determine the normal annual gross reference remuneration

= current monthly gross x 13.92

(or, for an employee paid other than monthly, the annualised

equivalent of the normal periodic pay)

2. Read the applicable percentage from the exceptional-payment table

for that reference amount (Module 4.5), from 0.00% to 53.50%.

Double holiday pay uses its own table (Module 8), which is more

favourable in the middle bands. A NOTICE INDEMNITY uses neither:

it takes the Annex III nr. 58 scale, 0.00% to 48.00% (Module 9.1),

keyed on the remuneration that served as the basis for the

indemnity rather than on the monthly gross x 13.92.

3. Apply the percentage to the taxable amount of the irregular payment,

that is the gross of the payment less the 13.07% employee contribution

on that payment.

4. Apply no monthly scale, no annualisation and no family reduction to

the irregular payment itself. Family reductions are already reflected

in the ordinary monthly withholding.

Payments that follow this route: end-of-year premium and thirteenth month, bonuses and gratuities, double holiday pay, departure holiday pay (double part), arrears and retroactive increases relating to a previous year, and any payment that does not relate to the ordinary work of the current period.

Notice indemnities follow the same structure — one percentage, no annualisation, no family reduction — but a different table. Annex III nr. 62 routes them to the nr. 58 arrears-and-severance scale set out in Module 9.1, and nr. 53 excludes them from the exceptional-payment table in terms. Steps 1 and 2 above must be read with that substitution whenever the payment is a notice indemnity.

#### How are backdated payments and retrospective salary adjustments handled?

The treatment turns on which period the payment relates to, not on when it is paid.

| Situation | Treatment |
| --- | --- |
| Retroactive increase relating to earlier months of the same calendar year | Market practice is to add the arrears to the current month's ordinary remuneration and tax the whole at the ordinary scale, because the annualisation still produces a defensible result. The DmfA for the earlier quarters must be corrected so that the wage is declared in the quarter to which it relates |
| Retroactive increase relating to a previous calendar year | Treated as arrears and taxed at the exceptional-payment percentage. The 281.10 shows the amount in the year of payment, with the arrears indicator |
| Index adjustment applied late | Same rules; index arrears within the year follow the ordinary scale |
| Correction of an underpayment | Same rules, plus a corrective DmfA for the quarter concerned |
| Correction of an overpayment | Recovered from net pay within the one-fifth cap of Article 23 of the Wage Protection Act, with a corrective DmfA and a corrected 281.10 where the year has closed. The employee repays the net amount received; the employer recovers the social security and tax through the corrections |

Corrections to the social security declaration are made by a corrective DmfA for the original quarter, which preserves the employee's benefit rights for that period. Corrections to the withholding tax are made in the monthly return of the month of payment, so the two declarations deliberately sit in different periods; this is expected behaviour and not a reconciliation error.

#### For arrears, how are contributions and deductions computed?

| Element | Rule |
| --- | --- |
| Employee social security contribution | 13.07% at the rate in force in the period to which the arrears relate, not the rate at the time of payment. Since the rate has been stable at 13.07% this rarely bites, but the principle governs any future rate change |
| Employer contributions | Same principle; the rates and reductions of the original quarter apply, which is why the arrears must be declared through a corrective DmfA for that quarter rather than in the current one |
| Special social security contribution | The arrears increase the quarterly wage of the original quarter, so the band for that quarter must be recomputed |
| Social work bonus | Recomputed for the original quarter, because the reference wage changes |
| Withholding tax | At the exceptional-payment percentage where the arrears relate to a previous year; at the ordinary scale where they relate to the current year |
| Holiday pay | Arrears increase the base of the departure holiday pay and of the double holiday pay for the service year concerned |
| End-of-year premium | Recomputed where the sectoral CBA bases it on the annual gross |
| Garnishment | The attachable amount is recomputed on the corrected net of the period |

#### Deliverable: Worked example of a bonus calculation

Facts. A white-collar employee on a gross monthly salary of EUR 3,200.00, single, no dependants, receives a performance bonus of EUR 5,000.00 gross in September 2026. The employee also participates in a CBA no. 90 collective bonus plan that pays EUR 3,500.00 gross in the same month.

Part A — the ordinary performance bonus of EUR 5,000.00

| Step | Calculation | Amount (EUR) |
| --- | --- | --- |
| Gross bonus | — | 5,000.00 |
| Employee social security | 5,000.00 x 13.07% | −653.50 |
| Taxable amount | — | 4,346.50 |
| Annual gross reference remuneration | 3,200.00 x 13.92 | 44,544.00 |
| Band of the exceptional-payment table | EUR 34,640.01 – 45,860.00 | 46.44% |
| Withholding tax | 4,346.50 x 46.44% | −2,018.51 |
| Net bonus | 4,346.50 − 2,018.51 | 2,327.99 |
| Employer social security | 5,000.00 x approximately 25% | 1,250.00 |

Part B — the CBA no. 90 bonus of EUR 3,500.00

| Step | Calculation | Amount (EUR) |
| --- | --- | --- |
| Gross bonus | Within the social ceiling of EUR 4,255 | 3,500.00 |
| Employee solidarity contribution | 3,500.00 x 13.07% | −457.45 |
| Taxable amount | Within the tax ceiling of EUR 3,701, therefore exempt | 0.00 |
| Withholding tax | — | 0.00 |
| Net bonus | 3,500.00 − 457.45 | 3,042.55 |
| Special employer contribution | 3,500.00 x 33% | 1,155.00 |

Part C — effect on the special social security contribution. The third quarter gross rises from 9,600.00 to 18,100.00. The band above EUR 12,300.00 applies: 118.83 + 1.10% x (18,100.00 − 12,300.00) = EUR 182.63 per quarter, just below the maximum of EUR 182.82. The additional amount is taken at the last payment of the quarter.

Part D — comparison. The two bonuses cost the employer EUR 6,250.00 and EUR 4,655.00 respectively and deliver EUR 2,327.99 and EUR 3,042.55 net. Per euro of employer cost, the CBA no. 90 bonus delivers EUR 0.65 net against EUR 0.37 for the ordinary bonus. This is the arithmetic that drives the popularity of CBA no. 90 plans in Belgium, and it is why the two ceilings — EUR 4,255 social and EUR 3,701 tax — must be configured separately and monitored per employee per calendar year.

Legal basis: Income Tax Code 1992, Articles 171 and 270 to 275; Annex III to the Royal Decree implementing ITC 92, scales of exceptional remuneration and of holiday pay, 2026 version; CBA no. 90; Wage Protection Act of 12 April 1965, Article 23; NSSO administrative instructions 2026/2 on corrective declarations.

## Module 10: Reporting, Compliance & Finalisation

Scope note for the development team. This module gives the summary view of Belgium's statutory reporting obligations. Field-level layouts, XML paths, validation rules and code tables are held in the Belgium Report Specifications and are deliberately not reproduced here.

### 10.1 Statutory Reporting

#### Describe the country's primary digital payroll reporting system.

Belgium's primary system is the DmfA (multifunctionele aangifte / déclaration multifonctionnelle), the quarterly declaration filed with the National Social Security Office through the portal socialsecurity.be.

Its defining characteristics:

One consolidated declaration, not a set of separate filings. The DmfA carries, in a single quarterly submission, the wages and working time of every employee, the ordinary employee and employer contributions, every special contribution (special social security contribution, CO2 solidarity contribution, 8.86% on supplementary pensions, Wijninckx, CBA no. 90 contributions), every contribution reduction (structural reduction, target-group reductions, social work bonus), and the sectoral fund contributions. There is no separate return per contribution type.

Multifunctional by design. The same data feeds the pension administration, the health insurance funds, the National Employment Office, the holiday funds and the statistical services, which is why the declaration is structured per employee, per occupation line, per contribution type, rather than as an employer-level summary.

Quarterly, due by the last day of the month following the quarter, with monthly advance payments where the K-2 threshold of EUR 6,197.34 is exceeded.

Two channels — web entry for small employers and a batch XML channel for payroll providers.

Preceded by Dimona, the immediate declaration of employment, which opens and closes the employment relationship in real time and is the key against which the DmfA is validated.

Filing mechanics — explicit statement (control C4). Belgium mixes consolidated and separate filings, and the distinction must not be assumed:

| Obligation | Consolidated or separate | Derived from another filing? |
| --- | --- | --- |
| DmfA | One consolidated quarterly grid covering all social security contributions and reductions | No |
| Dimona | Separate, event-driven | No |
| Wage withholding tax return (Finprof) | Separate from the DmfA, filed with a different authority on a different cycle | No |
| Belcotax-on-web annual filing (281.10) | Separate annual submission | No — it is not generated from the twelve monthly withholding tax returns. It is an independent filing built from the payroll ledger, and it must be reconciled against them |
| Summary statement 325.10 | Not a submission at all — no separate filing exists | Yes — derived by FPS Finance from the 281.10 data. Only the 281 fiches are submitted; the engine's whole obligation is to populate the <Opgave32510> wrapper and zone 2.029 inside the 281.10 file |
| Social balance sheet | Separate, filed with the annual accounts | Built from payroll data but filed by the accountant |

#### Deliverable: Data Disaggregation Mapping Guide describing the main reporting categories

The DmfA is hierarchical. Payroll must be able to disaggregate its own data along the same axes, because a total that cannot be split along these lines cannot be declared.

EMPLOYER LEVEL

Employer identification, employer category, quarter

|

+-- WORKER LEVEL  (one block per employee per quarter, keyed on the INSZ)

|

+-- OCCUPATION LINE  (a new line whenever a determining

|    characteristic changes within the quarter: worker code,

|    joint committee, working time regime, contract type,

|    start or end date)

|     |

|     +-- REMUNERATION CODES

|     |     Code 1  ordinary remuneration

|     |     Code 2  premiums not linked to a period of work

|     |     Code 3  departure holiday pay

|     |     Code 4  benefits not calculated per period

|     |     Code 5  premiums for the quarter

|     |     (plus the codes for indemnities, arrears and

|     |      single holiday pay for blue-collar workers)

|     |

|     +-- SERVICE CODES  (days and hours)

|           Code 1  ordinary working days

|           Code 2  recovery days

|           Code 3  annual leave, blue-collar

|           Code 5  guaranteed salary during sickness

|           Code 10 maternity leave

|           Code 12 temporary unemployment

|           (plus the full set of absence codes)

|

+-- CONTRIBUTION BLOCKS  (per contribution type code)

|

+-- DEDUCTION BLOCKS  (structural reduction, target-group

|    reductions, social work bonus)

|

+-- SPECIAL CONTRIBUTION BLOCKS  (CO2 per vehicle, 8.86% on

supplementary pensions, CBA no. 90, Wijninckx)

Mapping requirements imposed on payroll by this structure:

| Reporting category | What payroll must be able to produce |
| --- | --- |
| Per employee, per quarter | Gross by remuneration code, days and hours by service code |
| Per occupation line | A new line whenever the joint committee, worker code, working regime or contract changes mid-quarter |
| Per contribution type | The base and the amount separately, not a net figure |
| Per reduction | The reduction amount and the parameters that justified it |
| Per vehicle | The CO2 contribution, per month of availability |
| Per absence | The correct DmfA service code, since it drives both benefit entitlement and holiday accrual |

The general rule is that no netting is permitted: a contribution and its reduction are declared separately, and a gross and its deduction are declared separately.

#### List all other mandatory reports, stating the frequency, file format, due date, reporting authority.

| Report | Authority | Frequency | Format | Due date |
| --- | --- | --- | --- | --- |
| Dimona | NSSO | Per event | Web or XML batch | Before the employee starts work; end of employment by the first working day after |
| DmfA | NSSO | Quarterly | XML batch or web | Last day of the month following the quarter |
| Wage withholding tax return | FPS Finance, Finprof | Monthly, or quarterly for small employers | Web or XML | The 15th of the month following the period |
| Form 281.10 (employee income certificate) | FPS Finance, Belcotax-on-web | Annual | XML | 28 February following the income year |
| Form 325.10 (summary statement) — derived by FPS Finance, never filed by the employer | FPS Finance, Belcotax-on-web | Annual | Not applicable — no separate submission. The engine populates the <Opgave32510> wrapper and zone 2.029 within the 281.10 file | No employer deadline; discharged by the 281.10 filing |
| Electronic scenario declarations (ASR/DRS) — scenarios for sickness, unemployment and maternity. The work accident scenario is an ASR scenario too and is listed separately below, because it has its own authority and its own fixed deadline | NSSO and the paying institutions | Per event | XML | On the triggering event, except the work accident scenario — see the separate row |
| Limosa declaration — mandatory for the FOREIGN posting employer, NOT for the Belgian payroll client. Out of scope for this build | NSSO | Per posting | Web | Before the posted worker starts — a deadline that binds the foreign employer. See the note below this table |
| Individual account | Kept by the employer; provided to inspection on request | Annual | Electronic or paper | Closed within two months of the end of the year |
| Social balance sheet | National Bank of Belgium, with the annual accounts | Annual | Filed with the annual accounts | With the annual accounts |
| Work rules | FPS Employment (deposit) | On change | Paper or electronic | On adoption or amendment |
| Work accident declaration (ASR/DRS scenario AOAT) | The employer's work accident insurer, and Fedris (Federaal agentschap voor beroepsrisico's / Agence fédérale des risques professionnels), through the social security portal | Per event | XML over SFTP or FTP, application code AOAT; or the online service on the social security portal; or the insurer's own channel | Within 8 days of the accident — a fixed statutory deadline |
| DB2P declarations for supplementary pensions | Sigedis | Per event and annual | XML | Filed by the pension institution, not by payroll |

The Limosa row is in this table for completeness, and it is the one row that is not the Belgian employer's obligation. Every other report above is filed by, or on behalf of, the Belgian employer whose payroll this guide governs. Limosa is not, and an unqualified "mandatory" in a table a Belgian payroll implementer reads is a scope error rather than a nuance:

Who files it. The foreign posting employer, or its authorised representative, files the prior notification before the posting starts — Programmawet (I) van 27 december 2006 / Loi-programme (I) du 27 décembre 2006, Title IV, Chapter VIII, article 139 for posted workers and article 155 for posted self-employed persons (MB/BS 28 December 2006), executed by the Royal Decree of 20 March 2007. Independently confirmed on the NSSO's own Working in Belgium / Limosa portal, on socialsecurity.be, and by Securex. The Belgian host company is never the filer.

Why it is not a payroll matter here. The posted population normally remains subject to its home social security scheme under an A1 portable document and is not processed through Belgian payroll at all — it stays on the home-country payroll for the duration of the posting. Belgian payroll therefore holds none of the source data the declaration needs, and produces no output from it.

What the Belgian side does owe, and it is narrow. Article 141 obliges any person for whom or at whose premises the activities are carried out to verify that the prior declaration was made and to be able to produce the acknowledgement of receipt — the Limosa-1 — and, only where it cannot be produced, to report the worker's identification data electronically to the NSSO. Failure carries a level 3 sanction under the Social Criminal Code. This is a document check at onboarding and an exception report, owned by HR or the onboarding function: it fires on a missing document, not on a pay run, and it requires no payroll data.

Where this is recorded. Descoped in scope_manifest.json as BE-NSSO-LIMOSA-009 (the declaration — a third party's obligation) and BE-NSSO-LIMOSA-L1-VERIFY (the article 141 check — HR scope). BE-SIR-001-v1.0 registers it as OUT-08 and marks it descoped and exception-only. BE-NSSO-005-Limosa-Spec.xlsx exists on disk as a descoped artefact and is not a build target. Module 11.2 states the same position for the posted-worker population.

Legal basis for the Limosa position: Programmawet/Loi-programme (I) van/du 27 december/décembre 2006, Title IV, Chapter VIII, arts. 137–141 and 155, MB/BS 28 December 2006; Royal Decree of 20 March 2007; Social Criminal Code (level 3 sanction).

The work accident declaration appears once, not twice — and its deadline is 8 days. The work accident declaration is technically a scenario of the ASR/DRS family, which is why an earlier version of this table carried it both inside the ASR row and as a row of its own, with two authorities, two formats and two deadlines. The two rows describe one obligation. Where they conflicted, the separate row is correct and the ASR row was wrong, on both points:

Authority. The declaration goes to the employer's work accident insurer and to Fedris, through the social security portal — not to the NSSO and the paying institutions, which is the ASR row's generic destination. Fedris is the federal agency that supervises work accident compensation and holds the central register; it is a named recipient of this declaration and appears nowhere else in the payroll reporting set. BE-FEDRIS-001-WorkAccident-Spec.xlsx is the governing specification.

Deadline. "On the triggering event", the generic ASR wording, is not a deadline and understates the obligation. The work accident declaration carries a fixed statutory deadline of 8 days from the accident, which runs whether or not any benefit is claimed. BE-FEDRIS-001 records the same correction in terms: "This is a fixed statutory deadline, not a 'on the triggering event' obligation."

The ASR row above therefore now excludes the work accident scenario and points at the dedicated row, so the guide states one authority, one format and one deadline for it.

Legal basis: Work Accidents Act of 10 April 1971; the Royal Decrees implementing it on the declaration of work accidents; NSSO DRS scenario AOAT, glossary edition 2026/2.

Reports considered out of payroll scope. The following are excluded because more than half of their data does not exist in a payroll system; they are HR or finance obligations and must be referred to the relevant team rather than built into the payroll engine:

| Report | Reason for exclusion | Owner |
| --- | --- | --- |
| Social balance sheet — the training and workforce-structure sections | Requires headcount by qualification, training hours by type and workforce composition data held in the HR information system | HR / finance, filed with the annual accounts |
| Analytical reporting to the joint committee on employment structure | Workforce census data | HR |
| Occupational health and prevention reporting | Medical surveillance data | Prevention service |
| Diversity and equal-opportunity reporting where a sector imposes it | Protected characteristics not held in payroll | HR |

#### What pay elements are required as intermediates from payroll for reporting?

| Intermediate | Used by |
| --- | --- |
| Gross per DmfA remuneration code | DmfA |
| Gross at 108% for blue-collar workers | DmfA contribution base |
| Days and hours per DmfA service code | DmfA, holiday accrual, benefit entitlements |
| Quarterly gross per employee | Special social security contribution, high-wage exemption |
| Reference monthly wage for the social work bonus | DmfA deduction block |
| Employee contribution before and after the work bonus | DmfA |
| Taxable base per employee per month | Wage withholding tax return, 281.10 |
| Withholding tax per employee per month | Wage withholding tax return, 281.10 |
| Withholding tax exemptions claimed (overtime, shift and night work, student work) | Wage withholding tax return, which reports the exemption separately from the gross withholding |
| Taxable benefits in kind per type | 281.10 |
| Company car data: CO2, fuel type, order date, days of availability | DmfA CO2 block, 281.10 |
| Supplementary pension premiums | 8.86% contribution block, DB2P |
| Exceptional payments by type | 281.10 boxes |
| Departure holiday pay | DmfA code 3, 281.10, holiday certificate |
| Termination indemnity and the period it covers | 281.10, C4 |
| Garnishment amounts per creditor | Remittance to the bailiff; shown on the payslip |

### 10.2 Integrations

#### Is there any mandatory inbound integration?

Yes. Belgian payroll cannot run correctly on outbound declarations alone; several inbound flows are mandatory in the sense that the process fails or becomes non-compliant without them.

| Inbound flow | Source | What it carries | Why it is mandatory |
| --- | --- | --- | --- |
| Dimona acknowledgement and Dimona period reference | NSSO | The Dimona reference number and the accepted period | The DmfA is validated against the Dimona; a rejected Dimona blocks the quarterly declaration |
| DmfA validation report | NSSO | Anomalies, blocking and non-blocking | Anomalies must be corrected before the deadline |
| NSSO contribution statement and advance notice | NSSO | The advance amounts to pay and the balance calculated by the NSSO | The advances are calculated by the NSSO, not by the employer |
| Student quota counter (Student@work) | NSSO | Hours already consumed of the 650-hour quota | Determines whether the solidarity contribution or ordinary contributions apply |
| Belcotax validation report | FPS Finance | Acceptance or rejection of the 281.10 filing | Determines whether the annual obligation is discharged |
| Finprof acknowledgement | FPS Finance | Acceptance of the withholding tax return | Evidence of filing |
| Holiday certificate from the previous employer | Previous employer | Holiday pay already settled and days already taken | Without it the new employer over-pays holiday |
| Holiday fund data for blue-collar workers | National Annual Holidays Office and sectoral funds | The holiday pay paid to the worker | Needed for the payslip and for the leave administration |
| Fleet data | The leasing company | Catalogue value, CO2, fuel type, order date, availability dates | Drives both the taxable benefit and the CO2 contribution |
| Meal and eco voucher confirmations | The voucher issuer | Vouchers actually issued per employee | Reconciles the deduction from net |
| Time and attendance | The client's system | Days and hours, overtime, absences | Drives proration, meal vouchers and the DmfA service codes |

Every one of these is in scope for the pipeline unless the scope manifest records an explicit descoping decision with its rationale.

#### Is there any mandatory outbound integration beyond standard reporting?

| Outbound flow | Destination | Nature |
| --- | --- | --- |
| SEPA credit transfer file for net pay | The client's bank | Mandatory in practice; wages must be paid by transfer |
| SEPA payment of social security contributions | NSSO | Mandatory |
| SEPA payment of the withholding tax | FPS Finance | Mandatory |
| Electronic scenario declarations (ASR) | NSSO and the paying institutions | Mandatory on each triggering event; without them the employee receives no benefit |
| Meal and eco voucher order file | The voucher issuer | Mandatory where the benefit is granted |
| Payments to bailiffs and creditors for garnishments | The bailiff | Mandatory where an attachment is served |
| General ledger posting file | The client's accounting system | Contractual |
| Supplementary pension premium file | The insurer or pension fund | Mandatory where a plan exists |
| Work accident declaration (ASR/DRS scenario AOAT) | The employer's work accident insurer, and Fedris, through the social security portal | Mandatory on each accident, within 8 days of the accident |

Scope decisions are first-class and reversible (control B7). For each of the flows above, the scope manifest records three things: what is in scope for the payroll engine, what is explicitly owned upstream (the client, the leasing company, the insurer, the authority), and the inbound data contract this implies — that is, which fields the engine must receive in order to compute correctly. Recording the data contract alongside the scope decision is what makes a later reversal a contained change rather than a search across four artefacts.

### 10.3 Payslip Requirements

#### List all mandatory components that must be itemized on an employee payslip.

The payslip (loonbrief / fiche de paie) is compulsory with every definitive wage payment under Article 15 of the Wage Protection Act of 12 April 1965, and its minimum content is fixed by the Royal Decree of 20 September 2009.

| Block | Mandatory content |
| --- | --- |
| Identification | Name and address of the employer; the employer's NSSO number; name of the employee; the joint committee |
| Period | The pay period covered, and the payment date |
| Working time | The contractual working time regime; days and hours worked; days of absence by type |
| Earnings | The gross salary; each premium, allowance and supplement separately; overtime hours and the overtime supplement separately; holiday pay; the end-of-year premium; benefits in kind with their valuation |
| Deductions | The employee social security contribution, shown separately; the social work bonus, shown as a separate reduction; the wage withholding tax; the special social security contribution; each other deduction individually, with its reason |
| Net | The net amount due, and the amount actually paid, with the payment method |
| Non-cash entitlements | Meal vouchers and eco vouchers granted, with their number and value |
| Attachments | Any garnishment or wage assignment, with the amount withheld |
| Cumulative data | Not mandatory on the payslip; provided through the individual account |
| Language | Dutch, French or German according to the employer's seat of operation (Module 1.1). A bilingual payslip is not permitted |

Sectoral CBAs frequently add items — a seniority indicator, a sectoral premium reference, the balance of an hours account — so the payslip layout must be configurable per joint committee. Electronic payslips are permitted where the employee's consent and the conditions of the Law of 3 June 2007 on electronic social documents are met.

### 10.4 Other Compliance

#### Is payroll software certification mandatory?

No. Belgium does not certify or approve payroll software, and there is no register of approved payroll packages. Any system may be used provided its output complies.

Three related requirements are sometimes mistaken for certification and must be met:

| Requirement | Nature |
| --- | --- |
| Technical conformity of the DmfA XML | The batch channel validates each submission against the published NSSO schema and rejects non-conforming files. This is validation of the file, not certification of the software |
| Registration as a sender in the batch channel | The payroll provider registers as a technical sender with the NSSO and receives credentials. This is an access authorisation, not a certification |
| Recognised social secretariat status | An employer may delegate its obligations to a recognised social secretariat, which is approved by the FPS Social Security. This is an approval of the service provider, not of the software, and it is optional — an employer may file directly |

Sector-specific electronic systems are mandatory in some industries — the electronic attendance registration in construction (Checkinandcheckout) and the registered cash register in hotels and catering — but these are attendance and turnover systems, not payroll certification.

### 10.5 Year-End Processing and Finalisation

#### Describe the mandatory year-end finalisation process.

| Step | Action | Deadline |
| --- | --- | --- |
| 1 | Process the December payroll, including the end-of-year premium and any year-end corrections | December |
| 2 | Close and reconcile the individual account for each employee | Within two months of the end of the year |
| 3 | Reconcile the twelve monthly wage withholding tax returns against the payroll ledger | January |
| 4 | Reconcile the four DmfA declarations against the payroll ledger | January |
| 5 | Produce and issue form 281.10 to each employee | Before the Belcotax deadline |
| 6 | File form 281.10 through Belcotax-on-web, with the <Opgave32510> wrapper and zone 2.029 populated. The 325.10 is derived by FPS Finance and is not separately filed | 28 February |
| 7 | File the fourth-quarter DmfA, including the Wijninckx contribution | 31 January |
| 8 | Supply the payroll data required for the social balance sheet | With the annual accounts |
| 9 | Apply the new-year parameters: withholding scales, indexation, contribution thresholds, allowance ceilings | 1 January, with further steps at 1 March, 1 April, 1 July, 1 August and 1 September 2026 for the indexed amounts (1 August is the GMMI's final 2026 indexation step, confirmed in Module 4) |
| 10 | Archive the year in line with the retention rules of Module 2.3 | Ongoing |

Note that there is no annual tax reconciliation in payroll: step 3 is a reconciliation of what was declared against what was paid, not a recomputation of the employee's tax.

#### What documentation or annual statements must be provided to employees?

| Document | Content | When |
| --- | --- | --- |
| Form 281.10 | Gross remuneration, withholding tax, benefits in kind, exceptional payments, social security contributions withheld, for the calendar year | Before the employee files the tax return; in practice with or before the 28 February filing |
| Individual account | A full-year statement of work performed and remuneration, by period | Within two months of the end of the year, and on leaving |
| Holiday certificate | Holiday pay settled and days taken | On leaving |
| Form C4 | Reason and date of the end of the contract, and the data needed for unemployment benefit | On leaving |
| Pension benefit statement | The second-pillar position | Annually, issued by the pension institution through the MyPension portal |
| Payslip | Per pay period | With each definitive payment |

#### Is there a formal process for correcting errors discovered after the fiscal year has been closed?

Yes, and the process differs by authority.

| Error | Correction route | Timing |
| --- | --- | --- |
| Social security — wrong wage, days or contribution | Corrective DmfA for the original quarter. The NSSO recalculates and issues a debit or credit | No general deadline, but corrections beyond the three-year limitation period are subject to the prescription rules |
| Wage withholding tax — under- or over-withheld | Correction through the withholding tax channel. For income year 2025, corrections relating to withholding exemptions had to be filed by 15 May 2026 and other corrections by 10 July 2026, and the Finprof channel for that income year closed on 31 August 2026 | Within the published correction windows |
| Form 281.10 — wrong amount | A corrective filing through Belcotax-on-web, which produces a corrected certificate for the employee | As soon as identified |
| Employee tax return already filed | The employee files an amendment, or requests an ex officio relief within five years where the correction is in their favour | Within the statutory relief period |
| Overpayment to the employee | Recovered from net pay within the one-fifth cap of Article 23 of the Wage Protection Act, with the corresponding DmfA and 281.10 corrections. The employee repays the net; the employer recovers the tax and contributions from the authorities | On discovery |

Corrections cascade: a corrective DmfA changes the quarterly wage, which can change the special social security contribution band and the social work bonus, which changes the net, which changes the taxable base and therefore the 281.10. The engine must be able to re-run the affected quarter end to end rather than patching a single figure.

Legal basis: Law of 27 June 1969 and Royal Decree of 28 November 1969 (DmfA); Royal Decree of 5 November 2002 (Dimona); Income Tax Code 1992, Articles 270 to 275, 302, 306 and 376; Royal Decree implementing ITC 92, Articles 90 to 95; Wage Protection Act of 12 April 1965, Article 15; Royal Decree of 20 September 2009 (payslip content); Royal Decree of 8 August 1980 (social documents); Law of 3 June 2007 (electronic social documents); Law of 22 December 1995 (social balance sheet).

## Module 11: Advanced Scenarios & Cross-Cutting Logic

### 11.1 Calculation Logic

#### How is the proration and projection logic applied for income tax, social security, exemptions, and deductions?

| Element | Proration | Projection |
| --- | --- | --- |
| Income tax withholding | The prorated gross for the period is annualised as though it were a full period's pay. A half-month therefore annualises to roughly half a year's salary and attracts a lower rate | None. Belgium does not project future earnings into the current calculation |
| Employee social security | Strictly proportional to the wage actually paid; no minimum and no ceiling | None |
| Employer social security | Same, with the high-wage exemption applied against the quarterly threshold | None |
| Special social security contribution | Not prorated per month. Banded on the quarterly total and corrected at the last payment of the quarter | Implicitly projected during the quarter: months 1 and 2 use an estimate of the quarterly total, which is trued up in month 3 |
| Social work bonus | Prorated where the employee does not work the full month or works part-time, using the fraction of full-time performance | None |
| Tax-free allowance and dependant reductions | Applied in full in every period; the annualisation mechanism already scales them correctly | None |
| Meal vouchers | Strictly per day actually worked | None |
| Homeworking and bicycle allowances | Per the days on which the cost is incurred | None |
| Company car benefit | Prorated by day of availability, not by attendance | The annual statutory value is divided by 12 and charged monthly |
| Holiday accrual and holiday pay | Prorated on months worked or equivalent in the service year | The double holiday pay is a look-back on the service year, not a projection |
| Garnishment | Computed on the actual net of each period | None |

The single most important consequence is that a partial period is genuinely taxed as a partial period, and no catch-up occurs later in payroll. An employee who joins on 20 December is under-withheld relative to their eventual annual liability; the difference is collected in the assessment.

#### If tax or contribution rates change mid-pay period, which rates apply?

The governing principle is the date of payment for tax and the period of work for social security.

| Change | Rule |
| --- | --- |
| New withholding scales, published to apply from 1 January | Applied to remuneration paid from that date, even where it relates to work performed in December |
| New social security rate or threshold | Applied to the wage relating to the period in which the change takes effect. Where a threshold genuinely changes mid-quarter, the threshold applicable to that quarter is the one in force for the quarter as a whole. Illustrative case: had the high-wage exemption threshold (EUR 86,700 from 1 January 2026) itself been re-indexed mid-year, the quarter spanning the change would use the rate in force for that whole quarter. In practice, confirmed unchanged at least through mid-2026; the 1 July 2026 change to this measure excludes paid athletes and professional cyclists from combining it with their sport-specific contribution reduction (Programme Law of 30 May 2026, Articles 109-110), rather than raising the threshold -- this is a population-scope change, not a threshold value change, so it does not exercise the mid-quarter-threshold rule in force for the quarter |
| Indexation of a wage scale | Applied from the date fixed by the sectoral CBA. Where it falls mid-month, the month is split and each part is valued at its own rate |
| Indexation of an exempt allowance ceiling, such as the homeworking allowance moving to EUR 160.99 on 1 March 2026 | Applied from the effective date; the earlier months keep the previous ceiling |
| Change in the employee's family situation | Applied from the month following the notification, unless the change is retroactive by law (for example a birth), in which case it applies from the month of the event |
| Change of joint committee | Applied from the effective date, and it opens a new occupation line in the DmfA |

Belgium does not apply the rate in force at the end of the year to the whole year. Each period stands on its own.

#### How are tax and social security handled when an employee is paid multiple times in a single pay period?

This is common — an advance plus a balance for hourly-paid staff, or a salary plus a bonus in the same month.

| Component | Rule |
| --- | --- |
| Social security | Contributions are due on the total wage for the period. Where an advance is paid, contributions are computed on the final total and adjusted at the balance payment, so that the quarter is correct |
| Ordinary withholding tax | The ordinary remuneration of the period is taxed once, on the total for the period, at the ordinary scale. An advance should therefore not be taxed as a separate payment; it is a payment on account of the period |
| Exceptional payments in the same period | Taxed separately at the exceptional-payment percentage. A bonus paid in the same month as the salary does not increase the rate applied to the salary, and vice versa |
| Special social security contribution | Computed on the quarterly total, so multiple payments in a period simply increase that total |
| Meal vouchers | Granted once per worked day, regardless of the number of payments |

The configuration rule is: one ordinary-remuneration calculation per period, plus one calculation per exceptional payment. Splitting the ordinary remuneration into two taxed events would under-withhold, because each half would annualise to a lower rate.

#### How is payroll calculated if an employee's pay cycle changes mid-year?

A change from a twice-monthly to a monthly cycle, or from weekly to monthly, is permitted where the Wage Protection Act limits are respected and the work rules are amended.

| Step | Action |
| --- | --- |
| 1 | Amend the work rules and inform the employee; the change cannot leave a gap that breaches the Article 9 payment deadlines |
| 2 | Close the old cycle by paying all remuneration earned up to the changeover date, using the old annualisation factor |
| 3 | Open the new cycle from the changeover date, using the new annualisation factor |
| 4 | Do not re-annualise the earlier periods. Each period keeps the rate that was correct when it was paid |
| 5 | Keep the DmfA declaration on the quarter; the pay cycle does not change the reporting cycle. Where the change alters the working time regime, open a new occupation line |
| 6 | Recompute the special social security contribution for the quarter on the full quarterly total, which is unaffected by the cycle change |
| 7 | Explain to the employee that the transition month may show an unusual net, because a shorter or longer period annualises differently |

Because the withholding is non-cumulative, a cycle change produces a one-off distortion in the transition period that is corrected only in the annual assessment. This is expected and is not a defect to be engineered around.

Legal basis: Wage Protection Act of 12 April 1965, Article 9; Annex III to the Royal Decree implementing ITC 92; NSSO administrative instructions 2026/2.

### 11.2 Special Employee Groups & Income

#### How does taxation and social security differ for part-time employees and Board of Directors?

Part-time employees

| Aspect | Treatment |
| --- | --- |
| Social security rates | Identical — 13.07% employee and the ordinary employer rates, with no minimum |
| Social work bonus | Prorated by the fraction of full-time performance, so a half-time employee on a low wage receives half the maximum reduction |
| Withholding tax | Identical mechanism; the lower gross annualises to a lower amount and therefore a lower rate |
| Minimum wage | The guaranteed average minimum monthly income applies pro rata to the working time |
| Meal vouchers | One per day actually worked, regardless of the hours in the day, unless the company scheme uses the hours-based alternative |
| Holiday | Entitlement in days is proportional to the working pattern |
| Working time documentation | The variable part-time schedule must be published in advance and the deviations recorded, on pain of a presumption of full-time employment, which would retroactively increase contributions |
| Written contract requirement | A written individual contract is required for EACH part-time employee, in place at the latest at the moment the employee starts performing the contract, stating the agreed part-time regime and the work schedule; where the schedule is variable it is fixed by the work rules instead. Employment Contracts Act of 3 July 1978, Article 11bis. The sanction is not a fine but a reversal of the bargain: absent a compliant written contract the employee may choose, from the part-time regimes and schedules actually in use in the undertaking, whichever is most favourable to them - which is a payroll exposure, because the chosen regime then drives pay, the DmfA occupation line and the contribution base |

Company directors

| Aspect | Treatment |
| --- | --- |
| Status | Presumed self-employed. Directors' fees are not employment income |
| Social security | The self-employed scheme, with quarterly contributions paid by the director to a social insurance fund. Not declared in the DmfA and not in payroll |
| Income tax | Taxed as director's remuneration under Article 32 ITC 92; reported on form 281.20, not 281.10 |
| Withholding | A withholding applies to directors' remuneration under its own rules; it is not the employee wage withholding tax |
| Combination with an employment contract | Possible only where the two functions are genuinely distinct and the employed function is exercised under authority. A controlling shareholder will normally fail that test |
| Payroll configuration | Where both exist, only the employed function enters payroll; the mandate is excluded from the DmfA and from the 281.10 |

#### How is taxation handled for employees with multiple employers?

Each employer withholds independently and without knowledge of the other, because the Belgian withholding is not cumulative. Each treats its own payments as though they were the employee's only income and applies the full tax-free allowance.

The consequences:

| Consequence | Detail |
| --- | --- |
| Systematic under-withholding | Two employers each granting the full allowance and each starting at the bottom of the scale produce a combined withholding well below the final liability. The employee owes the difference at the assessment |
| Employee mitigation | The employee may ask one employer to apply a voluntary additional withholding, which is a supplementary amount agreed in writing and reported in the withholding tax return |
| Social security | Contributions are due in full by each employer on its own wage. There is no ceiling and therefore no over-payment to reclaim |
| Special social security contribution | Computed by each employer on the wage it declares. Because the contribution is due per fiscal household and is capped, the final position is corrected in the assessment |
| Work bonus | Applied by each employer on its own reference wage, which can result in an over-granted bonus that the NSSO recovers |
| Flexi-jobs | The specific regime for secondary employment exists precisely to make this configuration workable, with a 28% employer contribution and no employee contribution or withholding on the flexi-wage |

#### What is the treatment of foreign-sourced employment income for residents?

A Belgian resident is taxable on worldwide income (ITC 92, Article 5). Foreign employment income must be declared in the annual return even where Belgium cannot tax it.

| Situation | Treatment |
| --- | --- |
| Work performed abroad, taxing right allocated to Belgium by the treaty | Fully taxable in Belgium; the Belgian employer withholds normally |
| Work performed abroad, taxing right allocated to the other state | Belgium exempts the income with progression — it is excluded from the taxable base but taken into account to set the rate on the remaining income. The Belgian employer should not withhold on the exempt part, on the basis of documented treaty analysis |
| Foreign employer, no Belgian establishment | No Belgian wage withholding obligation in most cases; the resident declares the income and pays through the assessment or through advance payments |
| Salary split between Belgium and another state | Each state taxes its part; the Belgian employer withholds on the Belgian part only. A ruling or at least a documented allocation key is strongly advisable |
| Social security | Determined independently of tax by Regulation (EC) 883/2004 or by a bilateral agreement. A person may be taxable in one state and insured in another |

#### How do employer stock option plans work and how are they taxed?

Belgium taxes share options under the Law of 26 March 1999, and the defining feature is that taxation occurs at grant, not at exercise.

| Element | Rule |
| --- | --- |
| Trigger | The employee accepts the offer in writing within 60 days of the offer. Acceptance within that window brings the plan into the Law of 26 March 1999 |
| Timing of taxation | At acceptance, as a benefit in kind, in the month of acceptance |
| Valuation, listed shares | Based on the average share price over the 30 days preceding the offer, or the closing price on the day before the offer |
| Valuation, flat rate | 18% of the value of the underlying shares, reduced to 9% where the plan meets the conditions of the Law (notably that the option cannot be exercised before the end of the third calendar year after the grant and not after the tenth year, that the exercise price is fixed at grant, and that the option is not transferable). The percentage is increased by 1 percentage point per year beyond five years |
| Reduction | The flat valuation is halved where the plan meets the additional conditions on the exercise price and the underlying shares |
| Social security | No social security contributions, provided the employer does not guarantee the exercise gain and the option relates to shares of the employer or of a group company |
| Later gain | The gain realised on exercise or sale is in principle not taxed again as professional income |
| Options not accepted within 60 days | Fall outside the 1999 Law and are taxed at exercise, on the actual gain, as an ordinary benefit in kind |
| Warrants | Follow the same regime |
| Payroll processing | The taxable benefit is added to the base in the month of acceptance and taxed at the ordinary scale; it is reported on form 281.10 |

Note that a general capital gains tax on financial instruments applies to gains built up from 31 December 2025 and in force from 1 January 2026; it operates outside payroll but changes the after-tax analysis employees will expect on the eventual disposal of the shares.

#### How is payroll handled for employees who transfer between different legal entities mid-year?

| Scenario | Treatment |
| --- | --- |
| Transfer of undertaking under CBA no. 32bis | The employment contract transfers automatically with all its rights: seniority, notice entitlement, holiday rights and the terms of the contract. The transferee continues the employment relationship |
| Group transfer with a new contract | Legally a new employer. The old employer settles the departure holiday pay and issues the holiday certificate, the C4 and a 281.10; the new employer starts fresh |
| Same employer, different establishment unit or joint committee | The employment continues; a new occupation line is opened in the DmfA and the sectoral terms change from the effective date |

Payroll consequences in every case:

Dimona — close the employment with the old entity and open it with the new one, unless the transfer is a pure CBA no. 32bis continuation within the same NSSO number.

DmfA — each legal entity declares its own quarter under its own NSSO number.

Form 281.10 — one certificate per employer per year; an employee transferring mid-year receives two.

Special social security contribution and the high-wage exemption — computed per employer, so a mid-year transfer resets both counters. This produces a genuine over- or under-deduction that is corrected at the assessment.

Holiday — the transferee must honour the accrued entitlement where CBA no. 32bis applies, and must apply the holiday certificate where it does not.

Seniority for notice — preserved under CBA no. 32bis; contractual continuity of seniority should be documented explicitly where a new contract is signed.

#### What is the process for an employee who changes citizenship or residency status during the fiscal year?

Citizenship in itself has no effect on Belgian payroll: taxation follows residence, not nationality, and social security follows the place of work. A change of citizenship therefore requires only a master-data update, unless it changes the employee's right to work, in which case the work permit or single permit must be verified.

A change of tax residence does have consequences.

| Step | Action |
| --- | --- |
| 1 | Establish the date on which the residence changed, evidenced by the National Register entry or deregistration |
| 2 | Apply the correct withholding scale from that date — from scale III to scale I or II on becoming resident, and the reverse on leaving |
| 3 | Do not recompute the earlier months. Each period keeps the treatment that was correct at the time |
| 4 | The employee files two returns for the year of change: a resident return for the resident period and a non-resident return for the other period |
| 5 | Verify whether the social security position changes. In most cases it does not, because the employee continues to work in Belgium; obtain or cancel an A1 certificate where the place of work changes |
| 6 | Update the address and language regime where the employee moves between regions, since the language of the payslip follows the employer's seat of operation and not the employee's home |
| 7 | Reassess eligibility for the inbound taxpayer regime, which is lost on a change that breaks its conditions |

#### Are there specific rules for expatriates or inpatriates?

Yes. The special tax regime for inbound taxpayers and inbound researchers replaced the former expatriate circular regime with effect from 1 January 2022 and was made more favourable from income year 2025.

| Element | Rule |
| --- | --- |
| Population | Employees and company directors recruited abroad or transferred within an international group, and researchers |
| Entry conditions | Not a Belgian resident and not taxed as a non-resident on Belgian professional income in the 60 months before taking up the post, and not resident within 150 km of the Belgian border in that period |
| Minimum remuneration | EUR 70,000 gross per year, reduced from EUR 75,000; no minimum for inbound researchers |
| Benefit | Up to 35% of the gross remuneration may be paid as a tax-free and contribution-free reimbursement of costs proper to the employer, in addition to specific school-fee and moving-cost reimbursements. The former annual ceiling of EUR 90,000 has been abolished |
| Duration | 5 years, extendable by 3 years where the conditions continue to be met |
| Formalities | A joint employer and employee application to the tax administration within 3 months of taking up the post, and an annual nominative list of beneficiaries |
| Transitional alignment | Existing contracts could be adjusted retroactively until 30 June 2026 to apply the EUR 70,000 minimum and the 35% rate without a ceiling |
| Social security | Unaffected by the tax regime. Belgian contributions remain due unless an A1 certificate or a bilateral agreement assigns the employee elsewhere |

Other cross-border populations to configure:

| Population | Rule |
| --- | --- |
| Posted workers into Belgium | A Limosa declaration is required before the start, filed by the foreign posting employer — not by the Belgian client, and not by this payroll product (Programmawet/Loi-programme (I) du 27 décembre 2006, art. 139; art. 155 for posted self-employed persons; Royal Decree of 20 March 2007). The home social security scheme continues with an A1, so the worker is not on Belgian payroll while posted and there is nothing to configure in the payroll engine for the declaration itself. Belgian minimum working conditions apply under the Posting of Workers Directive. The Belgian-side duty is only the art. 141 check: verify the posted worker can produce the Limosa-1 acknowledgement, and report to the NSSO only if it cannot be produced — an onboarding document check owned by HR, out of payroll scope (scope_manifest.json: BE-NSSO-LIMOSA-009, BE-NSSO-LIMOSA-L1-VERIFY). See the note under the reporting table in Module 10.1 |
| Employees working in several Member States | Applicable legislation determined under Article 13 of Regulation (EC) 883/2004, with the 25% substantial-activity test |
| Frontier workers | Treaty-specific rules; the current Belgium-France, Belgium-Netherlands, Belgium-Germany and Belgium-Luxembourg positions must each be checked, including the tolerance thresholds for homeworking days |
| Non-EU nationals | A single permit (combined work and residence authorisation) issued by the region of employment |

Legal basis: Income Tax Code 1992, Articles 5, 32, 155, 227 and 243/1; Employment Contracts Act of 3 July 1978, Article 11bis (written contract required for each part-time employee, in place at the latest when performance starts); Law of 26 March 1999 on share options; Law of 21 January 2022 introducing the special regime for inbound taxpayers and inbound researchers, as amended with effect from income year 2025; CBA no. 32bis; Regulation (EC) 883/2004; Programmawet/Loi-programme (I) van/du 27 december/décembre 2006, Title IV, Chapter VIII, arts. 137–141 and 155 (the Limosa prior notification), MB/BS 28 December 2006, executed by the Royal Decree of 20 March 2007; Directive 96/71/EC as amended.

Citation corrected. Earlier versions of this legal-basis line cited the Law of 11 February 2013 for Limosa. That is the wrong instrument: the Act of 11 February 2013 transposes Directive 2009/52/EC and governs sanctions and measures against employers of illegally staying third-country nationals — a different obligation, on a different population, with its own residence-permit check and notification duties. It is not the legal basis of the Limosa prior notification, which is the 2006 programme law cited above. The same mis-citation was carried in BE-NSSO-005-Limosa-Spec.xlsx and has been corrected there in the same pass.

## Module 12: Gross-to-Net Worked Examples

### 12.1 Comprehensive Gross-to-Net Examples

All examples use 2026 parameters: employee social security contribution 13.07%, lump-sum professional expenses 30% capped at EUR 6,070, basic tax-free allowance EUR 11,170 giving a reduction of EUR 2,987.98, the Annex III nr. 31 withholding scale slices of 26.75% to EUR 16,710, 42.80% to EUR 29,500, 48.15% to EUR 51,050 and 53.50% above, dependent-child relief as a flat reduction of the basisbelasting under Annex III nr. 38, social work bonus parameters in force from 1 July 2026, and the special social security contribution bands for an individually assessed employee. The social work bonus is computed as two components, P = R_B + R_A, each with its own full-amount limit, maximum and degressive coefficient (Module 5.1.1); the fiscal work bonus is derived from it at 33.14% of component A and 52.54% of component B, capped at EUR 765.00 per year. Rounding is to the eurocent at each presented line.

#### Deliverable: Example 1 — A full-time resident employee on a standard salary

Profile. White-collar, joint committee 200, single, no dependants, full-time 38 hours, gross EUR 3,500.00 per month, 21 worked days in the month, meal vouchers of EUR 10.00 face value with an employee share of EUR 1.09.

| Step | Calculation | Amount (EUR) |
| --- | --- | --- |
| 1. Gross remuneration | — | 3,500.00 |
| 2. Employee social security | 3,500.00 x 13.07% | −457.45 |
| 3. Social work bonus | Reference wage 3,500.00 exceeds 3,336.98, the point at which component A reaches zero under the parameters in force from 1 July 2026; component B reached zero at 2,937.93 | 0.00 |
| 4. Taxable base | 3,500.00 − 457.45 | 3,042.55 |
| 5. Annualised | 3,042.55 x 12 | 36,510.60 |
| 6. Lump-sum professional expenses | 30% = 10,953.18, capped | −6,070.00 |
| 7. Annual net taxable | — | 30,440.60 |
| 8. Tax, slice 1 | 16,710.00 x 26.75% | 4,469.93 |
| 9. Tax, slice 2 | 12,790.00 x 42.80% | 5,474.12 |
| 10. Tax, slice 3 | 940.60 x 48.15% | 452.90 |
| 11. Annual tax before reductions | — | 10,396.95 |
| 12. Reduction for the tax-free allowance | 11,170.00 x 26.75% | −2,987.98 |
| 13. Annual withholding | — | 7,408.97 |
| 14. Monthly withholding tax | 7,408.97 / 12 | −617.41 |
| 15. Special social security contribution | Quarterly wage 10,500.00 -> 30.99 + 1.10% x (10,500.00 − 6,570.54) = 74.21 per quarter | −24.74 |
| 16. Meal voucher employee share | 21 x 1.09 | −22.89 |
| 17. Net pay | 3,500.00 − 457.45 − 617.41 − 24.74 − 22.89 | 2,377.51 |

Employer cost for the same month

| Element | Calculation | Amount (EUR) |
| --- | --- | --- |
| Gross salary | — | 3,500.00 |
| Employer social security | 3,500.00 x approximately 25% | 875.00 |
| Meal voucher employer share | 21 x 8.91 | 187.11 |
| Provision for double holiday pay | 3,500.00 x 92% / 12 | 268.33 |
| Provision for the end-of-year premium | 3,500.00 / 12 | 291.67 |
| Employer contributions on those provisions | approximately 25% on the end-of-year premium provision only | 72.92 |
| Total monthly employer cost | — | 5,195.03 |

The employee receives EUR 2,377.51 in cash plus EUR 210.00 in meal vouchers, for a total employer cost of approximately EUR 5,195.03 — a ratio of about 2.0 between employer cost and net cash, which is the figure clients most often ask for.

#### Deliverable: Example 2 — A casual or part-time employee

Profile. White-collar, single, no dependants, part-time at 60% of a 38-hour week (22.8 hours), gross EUR 1,300.00 per month, 13 worked days, meal vouchers of EUR 10.00.

| Step | Calculation | Amount (EUR) |
| --- | --- | --- |
| 1. Gross remuneration | — | 1,300.00 |
| 2. Employee social security before the work bonus | 1,300.00 x 13.07% | −169.91 |
| 3a. Social work bonus, component B | Full-time equivalent reference wage 1,300.00 / 0.60 = 2,166.67, at or below the component B full-amount limit of 2,300.62, so the component B maximum applies | 171.99 |
| 3b. Social work bonus, component A | 2,166.67 is also at or below the component A full-amount limit of 2,937.93, so the component A maximum applies | 127.54 |
| 3c. Social work bonus, full-time equivalent | P = R_B + R_A = 171.99 + 127.54 | 299.53 |
| 3d. Prorated at the performance fraction | 299.53 x 0.60 | 179.72 |
| 3. Social work bonus applied | Capped at the employee social security contribution actually due, 169.91 | +169.91 |
| 4. Net employee social security | 169.91 − 169.91 | 0.00 |
| 5. Taxable base | 1,300.00 − 0.00 | 1,300.00 |
| 6. Annualised | 1,300.00 x 12 | 15,600.00 |
| 7. Lump-sum professional expenses | 30%, below the cap | −4,680.00 |
| 8. Annual net taxable | — | 10,920.00 |
| 9. Tax on the first slice | 10,920.00 x 26.75% | 2,921.10 |
| 10. Reduction for the tax-free allowance | 11,170.00 x 26.75% | −2,987.98 |
| 11. Annual withholding | Negative, floored at zero | 0.00 |
| 12. Monthly withholding tax | — | 0.00 |
| 13. Special social security contribution | Quarterly wage 3,900.00, below the threshold for an individually assessed employee | 0.00 |
| 14. Meal voucher employee share | 13 x 1.09 | −14.17 |
| 15. Net pay | 1,300.00 − 0.00 − 14.17 | 1,285.83 |

Points this example demonstrates. The social work bonus is calculated on the full-time equivalent reference wage and then prorated by the performance fraction, so the absolute wage of EUR 1,300.00 is not what drives entitlement — the FTE wage of EUR 2,166.67 is, and it sits below both components' full-amount limits, so both maxima are granted before proration. This example is also the clearest illustration of the cap: the prorated bonus of EUR 179.72 exceeds the EUR 169.91 of employee social security actually due, so it is cut back to EUR 169.91 and the employee's social security contribution falls to nil. The bonus can never exceed the contribution and never turns into a payment. The fiscal work bonus, which is a percentage of the social work bonus granted, likewise cannot be applied here, because the withholding it would reduce is already nil. The withholding is nil, not negative — the reduction for the tax-free allowance can never generate a refund through payroll. And the special social security contribution does not bite at this level.

Employer cost. Employer contributions of approximately 25% on EUR 1,300.00 give EUR 325.00, reduced further by the structural reduction for low wages, plus EUR 115.83 for the employer share of the meal vouchers.

#### Deliverable: Example 3 — An employee with a pre-tax deduction

Profile. White-collar, single, no dependants, full-time, gross EUR 4,200.00 per month, personal contribution to the employer's supplementary pension plan of EUR 120.00 per month, 21 worked days.

| Step | Calculation | Amount (EUR) |
| --- | --- | --- |
| 1. Gross remuneration | — | 4,200.00 |
| 2. Employee social security | 4,200.00 x 13.07% | −548.94 |
| 3. Taxable base | 4,200.00 − 548.94 | 3,651.06 |
| 4. Annualised | 3,651.06 x 12 | 43,812.72 |
| 5. Lump-sum professional expenses | Capped | −6,070.00 |
| 6. Annual net taxable | — | 37,742.72 |
| 7. Tax, slice 1 | 16,710.00 x 26.75% | 4,469.93 |
| 8. Tax, slice 2 | 12,790.00 x 42.80% | 5,474.12 |
| 9. Tax, slice 3 | 8,242.72 x 48.15% | 3,968.87 |
| 10. Annual tax before reductions | — | 13,912.92 |
| 11. Reduction for the tax-free allowance | 11,170.00 x 26.75% | −2,987.98 |
| 12. Reduction for the personal pension contribution | 30% x (120.00 x 12) | −432.00 |
| 13. Annual withholding | — | 10,492.94 |
| 14. Monthly withholding tax | 10,492.94 / 12 | −874.41 |
| 15. Special social security contribution | Quarterly wage 12,600.00 -> 118.83 + 1.10% x 300.00 = 122.13 per quarter | −40.71 |
| 16. Personal pension contribution | Withheld from net | −120.00 |
| 17. Meal voucher employee share | 21 x 1.09 | −22.89 |
| 18. Net pay | — | 2,593.05 |

Points this example demonstrates. The personal pension contribution is not deducted from the taxable base — it is withheld from net pay and relieved through a reduction of the withholding equal to 30% of the contribution, which is EUR 36.00 per month. The net cost of a EUR 120.00 contribution to the employee is therefore EUR 84.00. Only the 13.07% social security contribution is a genuine pre-tax deduction in the Belgian system.

#### Deliverable: Example 4 — An employee with a student loan or other special tax obligation

Belgium has no student loan repayment mechanism operated through payroll. Student debt is a private banking obligation and is not deducted at source. The nearest equivalent special obligation processed by payroll is a wage garnishment, so this example uses one.

Profile. White-collar, full-time, gross EUR 2,800.00 per month, one dependent child, subject to an ordinary garnishment for a consumer debt, 21 worked days.

| Step | Calculation | Amount (EUR) |
| --- | --- | --- |
| 1. Gross remuneration | — | 2,800.00 |
| 2. Employee social security before the work bonus | 2,800.00 x 13.07% | −365.96 |
| 3a. Social work bonus, component B | Reference wage 2,800.00 is above the component B full-amount limit of 2,300.62, so the degressive formula applies: 171.99 − (0.2699 x (2,800.00 − 2,300.62)) | 37.21 |
| 3b. Social work bonus, component A | 2,800.00 is at or below the component A full-amount limit of 2,937.93, so the component A maximum applies | 127.54 |
| 3. Social work bonus | P = R_B + R_A = 37.21 + 127.54, below the 365.96 due, so the cap does not bite | +164.75 |
| 4. Net employee social security | 365.96 − 164.75 | −201.21 |
| 5. Taxable base | 2,800.00 − 201.21 | 2,598.79 |
| 6. Annualised | 2,598.79 x 12 | 31,185.48 |
| 7. Lump-sum professional expenses | 30% = 9,355.64, capped | −6,070.00 |
| 8. Annual net taxable | — | 25,115.48 |
| 9. Tax, slice 1 | 16,710.00 x 26.75% | 4,469.93 |
| 10. Tax, slice 2 | 8,405.48 x 42.80% | 3,597.55 |
| 11. Annual tax before reductions | — | 8,067.48 |
| 12. Reduction for the tax-free allowance | 11,170.00 x 26.75% | −2,987.98 |
| 13. Basisbelasting | 8,067.48 − 2,987.98 | 5,079.50 |
| 14. Reduction for one dependent child | Flat amount from Annex III nr. 38 | −624.00 |
| 15. Fiscal work bonus | 33.14% x 127.54 = 42.27 on component A plus 52.54% x 37.21 = 19.55 on component B, that is 61.82 per month or 741.84 per year, below the 765.00 annual cap | −741.84 |
| 16. Annual withholding | — | 3,713.66 |
| 17. Monthly withholding tax | 3,713.66 / 12 | −309.47 |
| 18. Special social security contribution | Quarterly wage 8,400.00 -> 30.99 + 1.10% x (8,400.00 − 6,570.54) = 51.11 per quarter | −17.04 |
| 19. Net for the purposes of Article 1409 | 2,800.00 − 201.21 − 309.47 − 17.04 | 2,272.28 |

Garnishment calculation, with the protected bands increased by EUR 88.00 for the dependent child:

| Band | Range (EUR) | Attachable % | Amount (EUR) |
| --- | --- | --- | --- |
| Protected | up to 1,507.00 | 0% | 0.00 |
| First | 1,507.01 – 1,612.00 | 20% | 21.00 |
| Second | 1,612.01 – 1,770.00 | 30% | 47.40 |
| Third | 1,770.01 – 1,927.00 | 40% | 62.80 |
| Fourth | above 1,927.00 | 100% | 345.28 |
| Total attachable | — | — | 476.48 |

| Final settlement | Amount (EUR) |
| --- | --- |
| Net before the attachment | 2,272.28 |
| Attachment remitted to the bailiff | −476.48 |
| Meal voucher employee share, 21 x 1.09 | −22.89 |
| Net paid to the employee | 1,772.91 |

Had the debt been a maintenance obligation, the full EUR 2,272.28 would have been attachable, because maintenance debts are not subject to the protected bands.

Note that granting the second component of the work bonus raises the net before attachment by EUR 19.36 but leaves the net paid to the employee unchanged at EUR 1,772.91: the whole increase falls inside the fourth band, which is 100% attachable, so the attachment absorbs it exactly. This is correct behaviour, not an error. It also means an employee under an ordinary garnishment gets no cash benefit from the work bonus — the creditor does.

#### Deliverable: Example 5 — Other complex scenarios that are common in the country: double holiday pay month with a company car

Profile. White-collar, single, no dependants, gross EUR 3,800.00 per month, company car with a monthly taxable benefit of EUR 250.80 (petrol, catalogue value EUR 38,000, CO2 120 g/km, first registered March 2024; at the May 2026 benefit month 26 months have elapsed, so the age coefficient is 88% — see Module 7.2), double holiday pay paid in May 2026, 20 worked days.

Part A — ordinary monthly remuneration

| Step | Calculation | Amount (EUR) |
| --- | --- | --- |
| Gross remuneration | — | 3,800.00 |
| Employee social security | 3,800.00 x 13.07% | −496.66 |
| Cash taxable base | — | 3,303.34 |
| Company car benefit added to the taxable base | Not subject to social security | +250.80 |
| Total taxable base | — | 3,554.14 |
| Annualised | x 12 | 42,649.68 |
| Lump-sum professional expenses | Capped | −6,070.00 |
| Annual net taxable | — | 36,579.68 |
| Tax, slices 1 to 3 | 4,469.93 + 5,474.12 + (7,079.68 x 48.15% = 3,408.87) | 13,352.92 |
| Reduction for the tax-free allowance | 11,170.00 x 26.75% | −2,987.98 |
| Annual withholding | — | 10,364.94 |
| Monthly withholding tax | / 12 | −863.75 |

Part B — double holiday pay

| Step | Calculation | Amount (EUR) |
| --- | --- | --- |
| Gross double holiday pay | 3,800.00 x 92% for a full service year | 3,496.00 |
| Employee social security | 3,496.00 x 13.07% | −456.93 |
| Taxable amount | — | 3,039.07 |
| Annual gross reference remuneration | 3,800.00 x 13.92 | 52,896.00 |
| Rate from the holiday-pay table | Band 45,860.01 – 59,900.00 | 47.44% |
| Withholding tax | 3,039.07 x 47.44% | −1,441.73 |
| Net double holiday pay | — | 1,597.34 |

Part C — special social security contribution for the second quarter. The employee is single, so Table 1 of Module 5.1.1 applies — the individually assessed employee scale.

Quarterly wage = 3 x 3,800.00 + 3,496.00 = EUR 14,896.00

Band above 12,300.00: 118.83 + 1.10% x (14,896.00 − 12,300.00)

= 118.83 + 28.56 = EUR 147.39 per quarter

Part D — combined May net and employer cost

| Line | Amount (EUR) |
| --- | --- |
| Net of the ordinary remuneration (3,800.00 − 496.66 − 863.75) | 2,439.59 |
| Net double holiday pay | 1,597.34 |
| Special social security contribution taken at the last pay of the quarter | −147.39 |
| Net paid in the quarter-end month | 3,889.54 |
| Employer social security on the ordinary salary, approximately 25% | 950.00 |
| Employer social security on the double holiday pay | 0.00 |
| CO2 solidarity contribution for the car | 42.36 |

Points this example demonstrates. The company car increases the taxable base but not the social security base, and it costs the employer a separate CO2 contribution rather than ordinary contributions. The double holiday pay carries the employee contribution but no employer contribution, and it uses its own withholding table, which is materially more favourable than the exceptional-payment table at the same reference wage — 47.44% against 51.48%. The reference wage for both tables is the monthly gross x 13.92, not x 12.

#### Deliverable: Example 6 — Other complex scenarios that are common in the country: blue-collar worker and the 108% contribution base

Profile. Blue-collar, joint committee 124, single, hourly rate EUR 17.50, 152 hours worked in the month, gross EUR 2,660.00.

| Step | Calculation | Amount (EUR) |
| --- | --- | --- |
| Gross remuneration | 17.50 x 152 | 2,660.00 |
| Contribution base at 108% | 2,660.00 x 1.08 | 2,872.80 |
| Employee social security before the work bonus | 2,872.80 x 13.07% | −375.47 |
| Social work bonus, component B, blue-collar | The reference wage is the wage at 100%, that is 2,660.00, not the 108% base; it is above the component B full-amount limit of 2,300.62, so the degressive formula applies: 185.75 − (0.2915 x (2,660.00 − 2,300.62)) | +80.99 |
| Social work bonus, component A, blue-collar | 2,660.00 is at or below the component A full-amount limit of 2,937.93, so the blue-collar component A maximum applies | +137.74 |
| Social work bonus | P = R_B + R_A = 80.99 + 137.74, below the 375.47 due, so the cap does not bite | +218.73 |
| Net employee social security | 375.47 − 218.73 | −156.74 |
| Taxable base | 2,660.00 − 156.74 | 2,503.26 |
| Annualised | x 12 | 30,039.12 |
| Lump-sum professional expenses | 30% = 9,011.74, capped | −6,070.00 |
| Annual net taxable | — | 23,969.12 |
| Tax, slice 1 | 16,710.00 x 26.75% | 4,469.93 |
| Tax, slice 2 | 7,259.12 x 42.80% | 3,106.90 |
| Annual tax before reductions | — | 7,576.83 |
| Reduction for the tax-free allowance | 11,170.00 x 26.75% | −2,987.98 |
| Fiscal work bonus | 33.14% x 137.74 = 45.65 on component A plus 52.54% x 80.99 = 42.55 on component B, that is 88.20 per month or 1,058.40 per year, which exceeds the 765.00 annual cap | −765.00 |
| Annual withholding | — | 3,823.85 |
| Monthly withholding tax | / 12 | −318.65 |
| Special social security contribution | Quarterly wage at 108% = 8,618.40 -> 30.99 + 1.10% x 2,047.86 = 53.52 per quarter | −17.84 |
| Net pay | 2,660.00 − 156.74 − 318.65 − 17.84 | 2,166.77 |

Points this example demonstrates. The 108% uplift applies to the whole contribution calculation, including the employee's own 13.07%, so a blue-collar worker pays more in contributions than a white-collar worker on the same gross. Note the one place the 108% does not reach: the work bonus reference wage S is the wage at 100%, so the wage limits are the same for both categories and only the maxima differ, the blue-collar maxima being the white-collar maxima x 1.08. This example is also the case where the fiscal work bonus's annual cap genuinely binds — the derived amount of EUR 1,058.40 per year is cut back to EUR 765.00, so the last EUR 293.40 of the entitlement is lost. The compensation is that the worker receives holiday pay from the holiday fund rather than from the employer, at 15.38% of the annual gross at 108%. The employer facial rate is correspondingly higher, at approximately 30.57%, and the employer pays no double holiday pay in May.

Legal basis: Law of 27 June 1969, Articles 14 and 23; Royal Decree of 28 November 1969; Income Tax Code 1992, Articles 31, 51, 52, 130 to 134 and 270 to 275; Annex III to the Royal Decree implementing ITC 92 (Royal Decree of 11 December 2025, as amended for this income year by the Royal Decree of 30 July 2026 implementing the Law of 15 July 2026 reforming personal income tax — Belgian Official Gazette, 29 and 30 July 2026); Judicial Code, Article 1409 and the Royal Decree of 3 December 2025; NSSO administrative instructions 2026/2 (work bonus, special social security contribution, CO2 solidarity contribution); Royal Decree of 30 March 1967. The fiscal work bonus figures used in this worked example should be re-verified against the 30 July 2026 Royal Decree before publication — see Module 6.3.

## Module 13: Common Business Practices & Non-Statutory Rules

### 13.1 Common Business Practices

#### Describe the common practice for off-cycle or ad-hoc payments.

Off-cycle runs are common in Belgium but are kept deliberately narrow, because the quarterly DmfA and the monthly withholding tax return are both period-based and every off-cycle payment has to land in the right period.

| Situation | Common practice |
| --- | --- |
| Salary advance before the normal pay date | Paid as an advance on the period, not as a separate taxable event. Social security and withholding are computed once, on the total for the period, at the balance payment. The advance is shown on the payslip as a deduction from the net due |
| Correction of an underpayment | Paid off-cycle, taxed at the ordinary scale where it relates to the current year; the DmfA for the quarter concerned is corrected |
| Final settlement on termination | Almost always processed off-cycle, because the departure holiday pay, the pro rata premium and the notice indemnity each follow their own tax rule and the C4 and holiday certificate must be produced at the same time |
| Bonus payment | Processed either in the ordinary run as a separate exceptional payment, or off-cycle. Either way it must be taxed at the exceptional-payment percentage and never merged into the ordinary monthly base |
| Expense reimbursement | Frequently paid off-cycle through accounts payable rather than through payroll. This is acceptable for genuine expenses proper to the employer, but the amounts must still be traceable, because a flat-rate allowance that cannot be justified is requalified as wage |
| Recovery of an overpayment | Deducted from the next ordinary run within the one-fifth cap of Article 23 of the Wage Protection Act, with a repayment plan agreed in writing where the amount is significant |

Two conventions are near-universal. First, an off-cycle payment is allocated to the pay period it belongs to for DmfA purposes, even where it is paid later, so the employee's social security record stays accurate. Second, the withholding tax follows the date of payment, so an off-cycle payment made in January for December work appears in the January withholding tax return and in the following year's form 281.10. The two declarations deliberately fall in different periods and this is not a reconciliation error.

Payroll in Belgium is overwhelmingly outsourced to a recognised social secretariat (erkend sociaal secretariaat), which files the DmfA, the Dimona and the withholding tax return on the employer's behalf. Off-cycle runs therefore also carry a commercial cost per run, which is why clients concentrate corrections into the next ordinary cycle wherever the law allows.

#### How are non-recoverable draws against future commissions typically handled?

Commission-based remuneration is common in sales, insurance brokerage and real estate, and the Belgian treatment of a draw is shaped by the Wage Protection Act, which makes it difficult to claw back remuneration already paid.

| Aspect | Common practice |
| --- | --- |
| Nature of the draw | Structured as a guaranteed minimum monthly remuneration rather than as a loan. This is the safer construction, because it respects the guaranteed average minimum monthly income and the sectoral minimum scales, which a pure advance would not |
| Recoverable draw | Where the parties do agree a recoverable advance, the recovery is a deduction under Article 23 of the Wage Protection Act and is therefore capped at one fifth of the net per pay period. A contractual clause purporting to allow full recovery in one month is unenforceable |
| Non-recoverable draw | Treated as ordinary wage from the outset: fully subject to the 13.07% employee contribution and to employer contributions, and taxed at the ordinary monthly scale. It enters the base for holiday pay, the end-of-year premium and the notice indemnity |
| Commission paid later, above the draw | The excess is paid as variable pay. Where it is paid periodically it is taxed at the ordinary scale; where it is a one-off annual settlement it is an exceptional payment |
| Effect on the notice indemnity | Variable pay is included in the current remuneration used for the indemnity, averaged over the 12 months preceding the dismissal. A draw structure therefore raises the cost of dismissal, which clients regularly underestimate |
| Effect on holiday pay | Variable pay enters the base of the double holiday pay and of the departure holiday pay, with the averaging rules of the Royal Decree of 30 March 1967 |
| On termination with a negative balance | A non-recoverable draw is not recovered. A recoverable balance may be set off against the final settlement only within the protected limits, and never against the part of the net that is protected under Article 1409 of the Judicial Code |

The practical drafting rule Belgian employers follow is to define the guaranteed part explicitly as remuneration and the commission as an addition to it, rather than defining the whole as commission with an advance against it. The second construction repeatedly fails before the labour courts.

#### Are there common non-statutory leave types? How are they managed and reported?

Yes. Belgian sectors and companies layer a substantial amount of contractual leave on top of the statutory minimum, and the payroll engine must be able to hold entitlements that have no statutory basis.

| Leave type | Source | Payment | Payroll and reporting treatment |
| --- | --- | --- | --- |
| Extra-statutory leave days (extralegale vakantiedagen) | Company policy or CBA | Paid by the employer | Paid as ordinary salary; the days are not reported as statutory holiday in the DmfA but as ordinary working days, since the salary continues |
| Seniority days (anciënniteitsdagen) | Sectoral or company CBA | Paid | Same treatment; entitlement usually increases in steps of 5, 10, 15 and 20 years of service |
| Age-related days | Sectoral CBA | Paid | Same treatment |
| Reduction-of-working-time days (ADV or RTT days) | Sectoral CBA, compensating a working week above 38 hours | Paid | Compensatory rest for hours already paid. Reported with the appropriate DmfA service code for recovery days |
| Collective closure days | Company decision, fixed in the work rules | Consume statutory leave | Reported as annual leave; where the employee has insufficient entitlement, temporary unemployment or unpaid leave applies |
| Bridge days | Company practice | Paid or taken from leave, per the policy | As agreed |
| Unpaid leave by agreement | Individual agreement | Unpaid | Salary suppressed; declared with the correct DmfA absence code; not equivalent for holiday accrual |
| Sabbatical | Usually structured as time credit or as unpaid leave | Per the structure | Time credit carries a National Employment Office allowance and is assimilated for pension purposes; pure unpaid leave is not |
| Additional birth or care leave above the statutory minimum | Company policy | Paid by the employer | Ordinary taxable and contributory wage |
| Volunteering or charity days | Company policy | Paid | Ordinary salary |

Management conventions. Extra-statutory days are almost always tracked in a separate counter from statutory leave, for three reasons: they are not covered by the departure holiday pay of 15.34%, so they must be settled separately or lapse on termination according to the policy; they are not protected by the annual holidays legislation, so the employer may impose when they are taken; and they must not be included in the holiday certificate given to a subsequent employer, which covers statutory entitlement only.

Additional common non-statutory practices worth capturing in configuration:

| Practice | Prevalence | Note |
| --- | --- | --- |
| Thirteenth month or end-of-year premium | Near-universal, through sectoral CBAs | Not a general statutory right; the sectoral rule governs eligibility, proration and forfeiture on resignation |
| Meal vouchers | Very widespread | Maximum face value raised to EUR 10.00 from 1 January 2026 |
| Eco vouchers | Widespread but declining | Being phased out in favour of the higher meal voucher ceiling |
| Hospitalisation insurance | Very widespread | Employer-paid premium is exempt where the conditions are met |
| Group insurance (second pillar) | Widespread; compulsory in some sectors | Employer premium attracts the 8.86% contribution |
| Company car | Very widespread, and a core part of Belgian remuneration packages | Taxed as a benefit in kind; the employer pays the CO2 contribution |
| Cafeteria and flexible remuneration plans | Growing | Must respect the minimum wage and the prohibition on waiving acquired remuneration |
| Mobility budget | Growing | Statutory framework under the Law of 17 March 2019 |
| Homeworking allowance | Very widespread since 2020 | EUR 160.99 per month from 1 March 2026 |
| CBA no. 90 collective bonus | Widespread | Two separate ceilings for 2026: EUR 4,255 social and EUR 3,701 tax |

Legal basis: Wage Protection Act of 12 April 1965, Articles 9 and 23; Royal Decree of 30 March 1967 on annual holidays; CBA no. 103 (time credit); CBA no. 90; Law of 17 March 2019 (mobility budget); Employment Contracts Act of 3 July 1978, Article 39; sectoral CBAs per joint committee; NSSO administrative instructions 2026/2.
