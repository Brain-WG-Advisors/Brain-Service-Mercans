# Stage 5 — AZ (Arizona) — findings by domain

Worker: compliance-source-hunter, 2026-11-02. Budget declared: 60 fetches and 2 h. Used about 45 fetches, including access probes and blocked attempts (the 75% stop), in about 25 minutes.
Shard: `00-official-sources/_register-shards/S5-AZ.csv` (US-AZS5-001..028, 28 rows). New sources: `00-official-sources/ccg-sources/AZ/` (27 files, about 0.65 MB). Earlier AZ files stay in `00-official-sources/pdfs/AZ/` and are cited through their existing register rows; nothing was re-fetched where an active row already had a local file.

**Access picture.**
- These hosts answer plain curl:
  - `www.azleg.gov/ars/{title}/{section5}.htm` (A.R.S., A.1; dotted sections use a hyphen, e.g. `23/00722-01`);
  - `azdor.gov/business/withholding-tax`;
  - `tucsonaz.gov`;
  - `api.bls.gov`.
- These hosts return 403 direct:
  - `www.azica.gov` (every page and PDF tried; the Wayback `2026id_` copies of the PDFs also return 403);
  - `des.az.gov`;
  - azdor.gov form/PDF paths.
- Pub 701 was read from Wayback.

## 1 — labour_code
- **State minimum wage (A.R.S. 23-363).**
  - Fixed steps ran to 12.00 in 2020. From 2021 the rate rises each 1 January by the August-over-August change in CPI-U (US city average, all items), with the increase rounded to the nearest 0.05 [US-AZS5-005, A.1, high].
  - **2026 = 15.15 USD and 2027 = 15.65 USD (MANUAL).** Both are derived from a 2025 base of 14.70, which no source read this pass confirms. The Industrial Commission of Arizona (ICA) page that publishes the rate returned 403 [US-AZS5-028, tier C, MANUAL].
  - The arithmetic, in Python with BLS CPI-U Aug 2024 314.796, Aug 2025 323.976, Aug 2026 334.980 [US-AZS5-026, A.2]:
    - 14.70 × 2.9162% = 0.4287 → +0.45 = **15.15**;
    - 15.15 × 3.3965% = 0.5146 → +0.50 = **15.65**.
  - Consistency check: Tucson states that its 2026 rate (15.45) and 2027 rate (16.00) are above the state rate [US-AZS5-027].
  - ICA published a "Minimum Wage Poster 2027" on 09/25/2026 [US-AZP9M-001], so the 2027 rate exists. Its amount was not read.
- **Tipped employees:** the employer may pay up to 3.00/h below the minimum, if tips plus wages reach the minimum each week [US-AZS5-005]. Derived cash wage: 12.15 (2026) and 12.65 (2027) (MANUAL).
- **Local minimum wages.** 23-364(I) allows county, city and town ordinances above the state rate [US-AZS5-006, A.1].
  - **Tucson:** 15.45 for 2026 (from 2026-01-01) and 16.00 for 2027 (from 2027-01-01). Covers employees with 5 or more hours per pay cycle in the city; the tip credit is at most 3.00. State of AZ, federal and tribal employers are excluded [US-AZS5-027, A.2].
    - G-DERIVE: 15.00 × 1.029162 = 15.437 → 15.45; 15.45 × 1.033965 = 15.975 → 16.00 (both reproduce exactly).
  - **Flagstaff:** has a local rate, but it was not read (the URL I guessed returned 404; see ACCESS gaps).
  - Conflict on the page: azleg serves 23-362 in its 1997 legislative version, which bars local rates above the federal minimum [US-AZS5-004]. The later voter-protected 23-364(I) permits them. Build rule: local rates apply. Flag for counsel.
- **Overtime:** no Arizona overtime statute was located in title 23, art. 8 (minimum wage) or art. 7 (payment of wages). Overtime follows the FLSA. Confidence medium: this is not a full-title negative.
- **Pay frequency and timing** (23-351) [US-AZS5-001, A.1, high]:
  - Two or more fixed paydays a month, no more than 16 days apart.
  - An employer whose principal place of business and centralized payroll are outside AZ may pay FLSA-exempt executive, administrative, professional and outside-sales staff, and NLRA supervisors, once a month.
  - Up to 5 days of labour may be held back. Overtime and exception pay are due within 16 days after the period ends.
- **Method of payment** [US-AZS5-001]:
  - Cash or a negotiable check.
  - Direct deposit with written consent.
  - Payroll card, if the employee was offered direct deposit and neither consents nor names an institution (D5, H).
  - Deposit and payroll-card plans: one free withdrawal per deposit, and a fee list for payroll cards.
- **Minors under 16:** at most 40 h/week and 8 h/day outside the school session; at most 18 h/week and 3 h/day in session; no night work (23-233) [US-AZS5-013].

## 2 — income_tax
- **Method.** The employer withholds a percentage of gross taxable wages, elected by the employee on Form A-4 (A.R.S. 43-401(A), (E)) [US-AZS5-020, A.1; US-AZS5-024, A.2; existing US-AZ-P5-1-001/-002/-003].
  - Taxable wages are federal wages (IRC 3401, generally W-2 box 1). Anything excluded federally is excluded here [US-AZS5-024].
  - Options: 0.5, 1.0, 1.5, 2.0, 2.5, 3.0 or 3.5%, plus any extra amount the employee requests.
  - The A-4 is due within 5 days of hire. Default is 2.0% until the employee elects. A zero-percent election must be renewed each year (the A-4 instructions say by 15 February, US-AZ-P5-1-001).
  - High confidence on the method.
- **Supplemental wages:** no separate rate exists. 43-401(A) applies the elected percentage to "wages, salary, bonus or other emolument" [US-AZS5-020]. Confidence medium-high: no ADOR statement on supplemental pay was read.
- **Rounding:** no rule in the statute or on the ADOR pages read (open).
- **December opt-out:** an employer may elect not to withhold in December. It must tell ADOR and the employees before 1 July (43-401(B), (F)) [US-AZS5-020].
- **Form A-4C tax-credit reduction** [US-AZS5-020, US-AZS5-024]:
  - On request, the employer may reduce withholding for designated contributions.
  - The amount goes to the charity or school within 15 days after quarter end.
  - The employee gets a statement within 30 days after year end, or 15 days after termination.
- **Exclusions (43-403)** [US-AZS5-021, A.1]:
  - nonresident common-carrier employees;
  - domestic service in a private home;
  - casual labour;
  - seasonal hand farm labour;
  - nonresidents present fewer than 60 days for an employer with AZ property, payroll and sales (does not apply to athletes and entertainers);
  - disaster-recovery workers.
- **Resident and nonresident** [US-AZS5-024; existing US-MULTI-017, US-AZ-WH-002, US-AZ-WH-003]:
  - A resident working in AZ is withheld from the first day, wherever the employer is based.
  - A resident working outside AZ may opt in with Form A-4V.
  - A nonresident is withheld after 60 days, or earlier by agreement.
  - Form WEC exemptions cover residents of CA, IN, OR and VA who claim the credit, MSRRA military spouses, and Native Americans living and working on their own reservation.
  - The credit is an assessment-level rule (43-1096, US-AZ-WH-003).
- **Local income tax:** none (existing US-AZR3-006, Pub 10).
- **Oracle:** no official ADOR calculator. The method is a flat percentage, so the A-4 instructions are the worked rule.

## 3 — social_security (UI only; no SDI/TDI/PFML)
- **Already registered, reused:**
  - DES UI wage base 8,000 for 2026; new employer 2.00%; 2026 rates 0.03%–8.36% (UIT-0603A); no employee contribution ("You cannot take these taxes out of employee pay") [US-AZR3-001, US-AZR3-002, US-AZR3-003, US-AZ-P5-2-004].
  - The UI Operating Fund diversion of 3.15% of UI liability starts 2027-01-01 [US-AZR3-004].
  - No SDI, PFML or other levy [US-AZR3-005, US-AZP9V-001, US-AZP9V-002].
- **New:** UI coverage exclusions under 23-617 and 23-615 [US-AZS5-014, US-AZS5-015, A.1]:
  - farm labour below 10 workers in 20 weeks or 20,000 in cash wages a quarter;
  - family employment (spouse or child; a child under 21 working for a parent);
  - students working for their own school;
  - 501(c)(3)-type religious and charitable organizations;
  - churches and ministers;
  - commission-only insurance, real estate, securities and tax-preparer salespeople;
  - under-18 newspaper carriers;
  - casual labour.
- **Indexation of the wage base:** none. The 8,000 is fixed (the 7,000 base applied before 2023).
- **Domestic coverage threshold:** not extracted (see Open questions).

## 4 — payslip_statute
- **Statement required only for direct deposit or payroll card.** Pay by deposit or payroll card requires a written or electronic statement of earnings and withholdings. The statute gives no content list (23-351(E), (F)) [US-AZS5-001].
- **Mandatory sick-time content on every regular paycheck** (23-375(C)): sick time available, sick time used to date in the year, and the pay received as sick time, on the paycheck or an attachment [US-AZS5-011, A.1, high]. This is a hard PSL/DD field set, and earlier passes had not registered it.
- **Other records and notices** (23-364(D)) [US-AZS5-006]:
  - Business name, address and phone in writing at hire.
  - **Payroll records** (hours each day, wages, sick time paid) kept **4 years**.
  - Employees may inspect and copy their own payroll records.
- **Language:** English and Spanish for the sick-time notice (23-375(B), existing US-AZL-001). The payslip itself is in English (US-OWN-006).

## 5 — reporting_instruments
- **Withholding returns** (ADOR Employer Withholding Filing Obligations, existing US-AZ-P5-2-005, A.2; read in full this pass):
  - **Deposit schedule**, by average withholding over the prior 4 quarters:
    - under 200: annual, on A1-APR, due 31 January;
    - 200 to 1,500: quarterly;
    - over 1,500: on the same schedule as the federal deposit (monthly, semi-weekly or next business day).
  - Detail of the schedule is in WTP 16-1 (not read).
  - **EFT** is mandatory at a liability of 500 or more. No general e-file waiver from 2022.
  - **A1-QRT** is filed quarterly, even with zero liability. Due 30 April, 31 July, 31 October and 31 January. Timely payers get 10 extra days (10 May, 10 Aug, 10 Nov, 10 Feb).
  - **A1-R** is the annual reconciliation with the W-2s, due 31 January. A 30-day extension is available for good cause (WTP 11-1).
  - Statute: 43-412(B), annual return due 31 January [US-AZS5-022, A.1].
- **State W-2 format** (ADOR Pub 701, rev. Jan 2025) [US-AZS5-025, A.2, high on text, medium on edition]:
  - Electronic filing is mandatory, as a .txt upload through AZTaxes or AZFSET, or by a transmitter. Optical media is allowed only for attachments.
  - The SSA EFW2 layout is used. The RS record is required for each employee, the RV record is optional, and the AZ state code is 04.
  - 1099s with AZ withholding are filed directly with ADOR (Pub 1220 format, one form type per file).
  - SSNs and EINs must not be truncated.
  - A1-R and A1-APR go electronically through AZFSET (.csv), AZTaxes data entry or a transmitter.
- **Quarterly UI wage report** (DES UC-018): not re-read, because des.az.gov returns 403. Existing rows cover only the tax pages; format and deadline are open.
- **New-hire reporting** (23-722.01) [US-AZS5-012, A.1, high]:
  - Report to DES every hire, rehire or return to work within 20 days. Electronic filers send two transmissions a month, no more than 16 days apart.
  - Report on a W-4 or equivalent with employee name, address and SSN; employer name, address and FEIN; and the first day of paid work.
  - A multistate employer may designate one state. There is no employer penalty.
- **Registration:** Form JT-1 registers both the ADOR withholding account and the DES UI account (existing US-AZ-P5-2-005).
- **POA:** Forms 821-PSC and UIT-1146A (existing US-AZ-P5-2-001/-002).

## 6 — leave
- **Earned paid sick time** (Prop. 206; 23-371..377) [US-AZS5-007..010, A.1, high]:
  - Accrual is 1 hour per 30 hours worked.
  - The yearly cap is 40 hours (15 or more employees) or 24 hours (fewer than 15), unless the employer sets a higher limit.
  - Exempt employees are treated as working 40 hours a week.
  - Unused time carries over, unless the employer pays it out at year end and front-loads the next year.
  - A 90-day use wait is allowed. Balances are reinstated on rehire within 9 months.
  - Sick time is paid at the normal hourly rate with normal benefits, and never below the minimum wage.
  - Time is used in hourly or smaller payroll increments.
  - **No payout at separation.**
  - The State of Arizona and federal employers are excluded.
  - An equivalent PTO policy satisfies the law.
- **PFML:** none (domain 3). No other state paid leave with a payroll effect was located.

## 7 — termination
- **Final pay** (23-353) [US-AZS5-003, A.1, high]:
  - Discharge: within 7 working days or at the end of the next regular pay period, whichever comes sooner.
  - Resignation: by the regular payday of the period in which employment ended, by mail if the employee asks.
- **Accrued vacation:** no statutory payout rule in 23-353 or 23-351.
- **Sick time:** no payout at separation (23-372(F)).
- **UI separation notice:** not read (DES 403).
- **WARN-style state law:** none located (not searched in depth).

## 8 — benefits_in_kind
- **Conformity date:** Arizona follows the IRC as in force on 2026-01-01 for tax years beginning after 2025 (43-105(A)) [US-AZS5-023, A.1].
- **Withholding base:** the base is federal wages, so federal exclusions flow through to AZ withholding (401(k), §125, HSA, transit, group-term life) [US-AZS5-024].
- **Departures:** no AZ departure was found for withholding. Form 140 additions and subtractions were not read. Medium confidence.

## 9 — deductions_garnishments
- **Deductions** (23-352) [US-AZS5-002, A.1]: allowed only when required by law, with prior written authorization (revocable), or during a good-faith wage dispute.
- **Creditor garnishment** (33-1131(B)) [US-AZS5-016, A.1, high]: the cap is the **lesser** of **10%** of disposable earnings or the excess over 60 × the highest applicable minimum wage. This is stricter than the federal CCPA (25% or 30 × the federal minimum).
  - Support orders: 50% of disposable earnings is exempt.
  - Tax debts and chapter XIII orders are not limited by this section.
  - Earnings garnishment is a continuing lien, with termination events in 12-1598.10 [US-AZS5-017]. 12-1598.10(F) still cites "25 percent": an inconsistency in the statute text.
- **Child-support income withholding** (25-504) [US-AZS5-018, A.1, high]:
  - Start no later than 14 days after receipt. For an ex parte order, the first employer waits 14 days and serves the employee within 5 days.
  - Remit to the clearinghouse within 2 business days of payday. Also deduct the 25-510 handling fee monthly (amount not read).
  - The employer may keep 1 USD per payment, at most 4 USD a month.
  - Report termination and the new employer within 10 days.
  - Support takes priority over all other garnishments, and current support is paid first.

## 10 — collective_agreements / prevailing wage
- There is no state prevailing-wage mandate: 34-321(B) bars agencies from requiring it (existing US-AZ-P5-2-003). No state certified-payroll duty was located.

## 11 — indexation
- **State minimum wage:** CPI-U, August over August, increase rounded to 0.05 (23-363(B)) [US-AZS5-005, US-AZS5-026].
- **Tucson minimum wage:** CPI-U [US-AZS5-027].
- **UI wage base:** fixed at 8,000, not indexed.
- **Withholding percentages:** fixed options, not indexed.
- **Publication vehicle for the state rate:** the ICA minimum wage page and posters (403, see gaps).

## 12 — data_protection
- **SSN use** (44-1373) [US-AZS5-019, A.1]: no public display of an SSN, no SSN on a card needed to obtain services, and secure transmission only. No pay-statement truncation rule was found in AZ law.
- **W-2s filed with ADOR:** Pub 701 forbids truncating SSNs [US-AZS5-025].
- **Sick-time health and domestic-violence information** is confidential (23-377) [US-AZS5-010].
- **New-hire data** may be used only for the listed purposes; unauthorized disclosure carries a 1,000 penalty for state agents (23-722.01(F), (G)) [US-AZS5-012].

## 13 — live_legal_change
- **2027 minimum wages:**
  - Tucson 16.00 from 2027-01-01 [US-AZS5-027].
  - The state 2027 poster was published 09/25/2026 [US-AZP9M-001]. Derived value 15.65 (MANUAL) [US-AZS5-028].
- **UI Operating Fund diversion (3.15%)** from 2027-01-01 [US-AZR3-004].
- **IRC conformity** moved to 2026-01-01 [US-AZS5-023].
- **Not done:** no sweep of ADOR or DES news and bulletins for 2026-01-01 to today (DES 403; budget). Open.

## Special populations (state level)
| Population | Arizona rule | register_id |
|---|---|---|
| Domestic / household | No AZ withholding on domestic service in a private home (43-403(A)(2)). UI coverage threshold not extracted. Tucson MW excludes casual babysitting at the employer's home. | US-AZS5-021, US-AZS5-027 |
| Agricultural | No AZ withholding for part-time/seasonal hand field labour, except machine operators (43-403(A)(4)); the employee may elect withholding. UI excludes farm labour below 10 workers in 20 weeks or 20,000 cash wages a quarter. | US-AZS5-021, US-AZS5-014 |
| Minors | Hours limits under 16 (23-233). Minors under 18 delivering newspapers are excluded from UI. No youth minimum wage was read. | US-AZS5-013, US-AZS5-014 |
| Tipped | Tip credit up to 3.00 under the state minimum (state and Tucson). | US-AZS5-005, US-AZS5-027 |
| Clergy / religious | Churches, primarily religious organizations, ministers and members of religious orders are excluded from UI (23-615). No AZ withholding exception for ministers; AZ follows federal wages. | US-AZS5-015, US-AZS5-024 |
| Students | A student working for their own school, student nurses and interns, and co-op students are excluded from UI. | US-AZS5-014 |
| Nonresident aliens | No AZ-specific rule. Withholding follows federal wages and the 60-day nonresident rule applies to state residence. | US-AZS5-024, US-AZS5-021 |
| Statutory employees | No AZ rule beyond federal. ADOR follows the IRS employee-status determination (WTR 16-4, not read). | US-AZS5-024 |
| Government employees | Sick-time law and Tucson MW exclude the State of Arizona and the US. UI: federal service is exempt. School-district pay lag is 7 business days (23-351(C)). | US-AZS5-007, US-AZS5-014, US-AZS5-001 |
| Native Americans / military spouses | Exempt from AZ withholding via Form WEC (on-reservation enrolled member; MSRRA spouse). | US-AZS5-024 |
| Common-carrier and motion-picture nonresidents; disaster-recovery workers | Excluded from AZ withholding. | US-AZS5-021, US-AZS5-020 |

## ACCESS gaps (exact URLs, 2026-11-02)
- `https://www.azica.gov/labor-minimum-wage-main-page`: 403 direct; Wayback `2026id_` also 403.
- `https://www.azica.gov/sites/default/files/2025-09/2026%20THE%20FAIR%20WAGES%20AND%20HEALTHY%20FAMILIES%20ACT_1.pdf`: 403 direct; Wayback 403.
- `https://www.azica.gov/sites/default/files/2026-09/2027%20THE%20FAIR%20WAGES%20AND%20HEALTHY%20FAMILIES%20ACT_1.pdf` (guessed path): 403.
- `https://des.az.gov/services/employment/unemployment-employer`: 403 (UC-018 quarterly report, separation notice and news not read).
- `https://azdor.gov/forms/withholding-forms/arizona-withholding-percentage-election`: 403.
- `https://azdor.gov/sites/default/files/document/FORMS_WITHHOLDING_2026_A-4.pdf`: 404 (the A-4 instructions are already held by US-AZ-P5-1-001).
- `https://azdor.gov/sites/default/files/2023-03/PUBLICATION_701.pdf`: 403 (the Wayback copy was read).
- `https://www.flagstaff.az.gov/3685/Minimum-Wage`: 404 (guessed URL; the Flagstaff MW page was not found).
- `https://www.tucsonaz.gov/Departments/Business-Services/Minimum-Wage`: 404 (the correct page was found and read).
- BLS API v1 ignores `startyear`, so only 2024–2026 data was returned. The full 2020–2025 chain needs a POST or v2.

## Open questions
1. **State minimum wage 2026/2027.** Read the ICA 2026 and 2027 posters (single browser pass). This would confirm 15.15 and 15.65 and replace the MANUAL US-AZS5-028. To check the whole 2021–2025 chain, the BLS series is needed from 2019.
2. **Flagstaff minimum wage 2026/2027** (city ordinance; flagstaff.az.gov). Values not read.
3. **DES quarterly UI wage report** (UC-018): format, deadline and e-file mandate. Also the DES UI separation notice and the domestic-service UI threshold (rest of 23-615/23-613.01).
4. **Rounding of AZ withholding.** Read A.A.C. R15-2B-101 on azsos.gov.
5. **Pub 701 edition.** A 2026 edition was not located; the Jan 2025 text speaks of calendar year 2024.
6. **33-1131(B) and 12-1598.10(F) text conflict** (10% vs 25%). Check the effective date of the 10% amendment (Prop. 209) and the 25-510 handling-fee amount.
7. **23-362:** the azleg page serves only the L97 version, so the Prop. 202 definitional text was not seen.
8. **AZ departures from federal exclusions** (Form 140 additions and subtractions) for HSA and other items, at assessment level, not withholding.
9. **2026 bulletin sweep** of ADOR and DES news. Not done.
