# Stage 5 — Ohio (OH), 13-domain hunt

Worker run 2026-11-02 (07:10 to 07:40 local). Budget declared: 60 fetches / 2 h; stopped at about 45 fetches (75%).
New rows: `00-official-sources/_register-shards/S5-OH.csv`, ids US-OHS5-001..023 (23 rows). I reused the active rows of `legal-basis-register.csv` (US-OH-*, US-OHR3-*, US-OHP7-*, US-OHL-*, US-MULTI-005) without re-fetching them.
Source files: `00-official-sources/ccg-sources/OH/` (22 files, 1.76 MB).
Access note: tax.ohio.gov HTML pages return a 403/404 shell to scripts, and the Wayback copy of /business/employer-withholding also gives 404. dam.assets.ohio.gov (PDFs) and codes.ohio.gov (ORC/OAC) work.

## 1 labour_code
- **Minimum wage, 2026:** 11.00 USD/h non-tipped and 5.50 USD/h tipped (tipped = more than 30 USD/month in tips). Employers grossing under 405,000 USD and employees under 16 pay the federal 7.25 USD. Vigência 2026-01-01..2026-12-31 [US-OHS5-005].
- **Minimum wage, 2027 (published):** 11.40 / 5.70 USD/h, small-employer threshold 419,000 USD, from 2027-01-01 [US-OHS5-004]. The G-DERIVE proof is in domain 11.
- **No local minimum wages.** Ohio law preempts local regulation of hours, scheduling and benefits for private employers (ORC 4113.85) [US-OHS5-012]. No city minimum wage was located; the 4113.85 text covers benefits and scheduling, and minimum-wage preemption itself (ORC 4111.02) was not read. Confidence 80%.
- **Overtime:** 1.5x over 40 hours per workweek, following FLSA s.7/s.13 exemptions; no daily overtime (ORC 4111.03) [US-OHS5-003]. The poster excludes employers grossing under 150,000 USD/year [US-OHS5-004/005].
- **Pay frequency and pay day:** at least semimonthly. Wages for the 1st–15th are due by the 1st of the next month; wages for the 16th–month end by the 15th of the next month. Daily or weekly pay is allowed, as is a longer lapse that is customary or set by contract. Liquidated damages apply after 30 days unpaid (ORC 4113.15) [US-OHS5-015, US-OH-004].
- **Method of payment** (direct deposit or paycard consent): no Ohio statute was read this pass. This is an open question.
- **Records:** kept 3 years — name, address, occupation, rate, pay per period, hours per day and per week [US-OHS5-004].
- **Confidence:** High for the minimum wage and overtime; Medium for the method of payment.

## 2 income_tax
- **Statutory rate (HB 96):**
  - TY2026 and later: flat 332.00 + 2.75% of Ohio taxable income over 26,050 USD; no tax up to 26,050.
  - TY2025: 2.75% / 3.125%. TY2024: 2.75% / 3.5%.
  - Source: ORC 5747.02(A)(3), effective 2025-09-30 [US-OHS5-007].
- **Withholding duty:** ORC 5747.06 [US-OHS5-008]. The commissioner's tables define the method. They apply to residents and nonresidents, and also to the state and its political subdivisions as employers.
- **Withholding method, two editions in 2026 (mid-year change):**
  - Pay dates 2025-10-01 to 2026-07-31:
    - optional computer formula with 650 USD per exemption and rates 1.775% / 2.990% / 3.640% (breaks at 26,050 and 100,000) [US-OH-P5-2-001];
    - percentage tables of the same period [US-OH-002].
  - Pay dates from 2026-08-01:
    - percentage tables: weekly 12.50 per exemption, then 1.600% up to 500.96, 8.02 + 2.990% up to 1,923.08, 50.54 + 3.400% above. Biweekly, semimonthly, monthly and daily tables also exist [US-OH-006];
    - computer formula: TW = pay x PP − 650 x exemptions; WD = TW x 0.016 / PP up to 26,050; ((TW − 26,050) x 0.0299 + 416.80) / PP up to 100,000; ((TW − 100,000) x 0.034 + 2,627.91) / PP above [US-OHS5-001].
  - The withholding schedule still graduates up to 3.4%, although the TY2026 statutory rate is flat 2.75%. These are two different instruments: the 5747.06 rule versus the 5747.02 rate. The tables do not mis-transcribe the rate.
- **Derivation (G-DERIVE):**
  - The constants reconcile: 26,050 x 0.016 = 416.80, and 416.80 + 73,950 x 0.0299 = 2,627.91.
  - Oracle seed: biweekly 2,000 USD with 1 exemption, paid on or after 2026-08-01.
    - Table: TW 1,975.00 gives 16.03 + 973.08 x 0.0299 = 45.13.
    - Formula: TW 51,350 gives (25,300 x 0.0299 + 416.80) / 26 = 45.13.
    - The 2025 formula gives 46.88.
- **No rounding instruction** appears in the tables or the formula. ORC 718.25 optional whole-dollar rounding applies to municipal returns only [US-OH-P5-2-002].
- **Supplemental rate:** OAC 5703-7-10, effective 2026-01-01, withholds supplemental pay (bonuses, commissions, nonrecurring pay) at the highest 5747.02(A)(3) rate for the year. That is **2.75% for TY2026** [US-OHS5-017], which confirms US-OH-002.
- **Certificate:** IT 4 (rev. 12/2020), a combined form that replaces IT 4NR, IT 4 MIL and IT MIL-SP. If no IT 4 is on file, withhold at zero exemptions. Keep the form 4 years [US-OH-P5-2-006; 2026 Filing Guidelines Rev. 11/25 on disk under pdfs/OH, row US-OH-P5-1-002 superseded].
- **Reciprocity:** no Ohio withholding for residents of IN, KY, MI, PA or WV working in Ohio [US-MULTI-005, US-OH-P5-2-006]. The resident credit is IT RC; no credit for wages from the reciprocity states [US-OH-P5-2-004].
- **Exemptions from withholding (5747.06):** agricultural labour, domestic service, service in a quarter with cash pay under 300 USD, foreign government service, newspaper carriers under 18 [US-OHS5-008].
- **School district income tax (ch. 5748):**
  - Withheld for employees who *reside* in a taxing district, even if the employer has no operations there [US-OH-002, US-OHS5-017].
  - 2026 changes: 6 new districts (e.g. Westerville CSD 0.75%, Findlay CSD 1.00%), 2 expired, 3 rate changes and 21 renewals [US-OHS5-018]. The 2025 full list is US-OHS5-019; no consolidated 2026 full list was located.
  - Lookup tool: The Finder [US-OHS5-023, partial].
- **Municipal income tax (ch. 718):**
  - Work-location based. The employer withholds qualifying wages x the municipal rate and remits to the municipality or its collector (RITA, CCA) [US-OH-P5-2-003, US-OH-010].
  - 20-day occasional-entrant rule [US-OH-008].
  - The base is Medicare wages less section 125, so 401(k) deferrals are taxable [US-OHS5-013].
  - Rates may not exceed 1% without voter approval [US-OHP7-001].
  - **No consolidated municipal rate table was obtained** (ACCESS gap).
- **Confidence:** High for state withholding; Medium for the local layer (no rate table).

## 3 social_security (SUI, SDI/PFML, levies)
- **ODJFS rate year 2026** [US-OHS5-002 (rate-detail PDF), US-OH-005 (ODJFS page); second document family, consistent]:
  - taxable wage base 9,000 USD;
  - new employer 2.85% (2.7% + 0.15% Technology & Customer Service Fee, ORC 4141.251); construction 5.85%;
  - experienced rates 0.4%–10.1% before the fee, 0.55%–10.25% total; mutualized 0.0%;
  - delinquency 12.75%; SUTA dumping 12.75%; tax-avoidance penalty 14.75%;
  - employer-only, no employee contribution.
- **TCSF levy (0.15%):** see US-OHP7-003.
- **No SDI/TDI/PFML** [US-OH-P5-1-004].
- **No transit or workforce levy on wages** [US-OHL-002].
- **Not covered:** how the wage base is indexed (ORC 4141.01) was not read. The base has been fixed at 9,000 in recent years, but that is unverified this pass. Open question.
- **Confidence:** High.

## 4 payslip_statute
- **Content (ORC 4113.14, Pay Stub Protection Act, HB 106, effective 2025-04-09):** a written or electronic statement every pay period showing:
  - employee name and address, employer name;
  - gross and net pay;
  - amount and purpose of each addition and deduction;
  - pay date and pay period;
  - for hourly employees, hours worked and rate.

  Sources: [US-OH-P5-1-001, US-OHL-001]. The statute has no language clause.
- **SSN on the stub:** not required.
- **Retention:** 3 years for wage and hour records [US-OHS5-004]; 4 years for withholding records [2026 Filing Guidelines].
- **Confidence:** High.

## 5 reporting_instruments
- **State withholding** [US-OH-009; Filing Guidelines]:
  - IT 501 return, filed electronically through OH|TAX eServices or the Treasurer.
  - Frequency by look-back (12 months ending June 30):
    - up to 2,000 USD: quarterly, due the last day of the month after the quarter;
    - more than 2,000 and less than 84,000 USD: monthly, due within 15 days;
    - 84,000 USD or more: partial-weekly EFT within 3 banking days;
    - 100,000 USD or more in one pay period: next banking day.
  - IT 941 annual reconciliation by January 31.
  - W-2/1099 upload through OH|TAX "Upload Income Statement" by January 31; the CD option has been eliminated; a simplified format is available up to 500 statements. W-2s carry the four-digit school district code [US-OHS5-018].
  - Registration within 15 days of liability.
- **School district:** SD 101 (periodic) and SD 141 (annual, January 31). Bulk filing uses FSET XML 4.4 [US-FIL-012]. Agent authorisation is WT 8655 [US-FIL-011].
- **Municipal:** returns go to each municipality or collector. Under 718.03: monthly (15 days after month-end) if prior-year withholding exceeded 2,399 USD or any month of the preceding quarter exceeded 200 USD; otherwise quarterly. A municipality may require semimonthly remittance [US-OH-P5-2-003]. CCA uses Form CCA-102 [US-OH-010]. RITA Form 11/17 is gated [US-OH-014].
- **UI quarterly report (ORC 4141.20):** contribution and wage report by the last day of the month after the quarter. Fields: total and taxable remuneration, each employee's name and SSN, wages per employee, number of weeks paid. Late-filing forfeiture is 0.25% of remuneration, 50–1,000 USD [US-OHS5-020]. The channel or format for the employer filing portal was not read.
- **New hire (ORC 3121.891–.893):** to ODJFS within 20 days of hire. Fields: name, address, date of birth, SSN, hire date, plus employer name, address and ID. Contractors are also reported. A copy of the W-4 is allowed; multistate employers may designate one state [US-OHS5-009, US-OHS5-014].
- **Representatives:** TBOR 1 [US-OH-P5-2-005]; JFS-20106 (UI taxes) [US-OHR3-001].
- **Confidence:** High for the state; Medium for municipal (per collector).

## 6 leave
- **No state paid sick leave law.** ORC 4113.85 makes leave and fringe benefits matters of employer policy or agreement and preempts local mandates for private employers [US-OHS5-012].
- **No PFML,** so there is no benefit-side payroll interaction [US-OH-P5-1-004].
- **Other leave** (jury duty 2313.19, military 5903.02, voting): not read this pass. Open question.
- **Confidence:** Medium-High.

## 7 termination
- **No dedicated final-pay statute.** Final wages fall on the next regular payday under the 4113.15 schedule [US-OHS5-015].
- **Accrued vacation payout:** follows employer policy (4113.85 lists vacation and separation pay as policy matters) [US-OHS5-012].
- **UI separation:**
  - ODJFS asks the separating employer for the reason when a claim is filed.
  - Mass layoff of 50 or more people in 7 days for lack of work: notify the director 3 working days ahead and give each worker the eligibility information (ORC 4141.28(C)) [US-OHS5-016].
  - No individual separation-notice duty was found in 4141.28 (the OAC 4141 rules were not read).
- **No state WARN law located;** federal WARN applies.
- **Confidence:** Medium-High.

## 8 benefits_in_kind
- **State tax:** Ohio AGI starts from federal AGI (ORC 5747.01(A), latest amendment SB 9 effective 2026-03-05). None of the add-backs read touch 401(k), section 125, HSA, transit or group-term life, so the state follows federal exclusions [US-OHS5-022].
- **Municipal tax departs from federal.** The base is IRC 3121(a) wages: 401(k)/403(b) elective deferrals are **taxable**, section 125 is excluded, and NQDC and stock options depend on a municipal ordinance adopted before 2016 [US-OHS5-013].
- **School district tax:** follows the district base ("T" traditional or "E" earned income) [US-OHS5-019].
- **Confidence:** High for state and municipal; Medium for the SD earned-income base detail.

## 9 deductions_garnishments
- **Creditor garnishment (ORC 2329.66(A)(13)):** exempt amount is the greater of 75% of disposable earnings or 30x / 60x / 65x / 130x the federal minimum wage (weekly / biweekly / semimonthly / monthly) [US-OHS5-011]. This matches the CCPA.
- **Child support IWO fee (ORC 3121.18):** the employer may deduct the greater of 2 USD or up to 1% of the amount withheld [US-OHS5-010].
- **Not covered:** wage-deduction authorisation rules and the support priority order were not read. Open question.
- **Confidence:** Medium.

## 10 collective_agreements / prevailing wage
- **State prevailing wage (ORC ch. 4115):** the Director of Commerce determines rates (4115.04). Thresholds: 250,000 USD new construction and 75,000 USD remodeling; road, sewer and bridge work 78,258 / 23,447 USD; adjusted biennially under 4115.034 [US-OHR3-002, US-OHR3-003, US-OH-P5-1-003].
- **Not covered:** the certified-payroll obligation (4115.071) was not read. The 2026 adjusted threshold figures come from the DOL table, with the date of adjustment unconfirmed.
- **Confidence:** Medium.

## 11 indexation
- **Minimum wage (Ohio Const. art. II s.34a):** indexed each 1 January by CPI-W for the 12 months to the preceding September (rounded to 5 cents). The small-employer gross-receipts threshold uses the same index, rounded to 1,000. The tipped wage is 50% of the minimum [US-OHS5-006].
  - **2026 derivation:** 10.70 x 317.306 / 308.640 = 11.0004, which gives 11.00 ✓.
  - **2027 derivation:** 11.00 x 328.481 / 317.306 = 11.387, which gives 11.40 ✓. Threshold: 405,000 x 1.03522 = 419,263, which gives 419,000 ✓. Tipped: 5.70 ✓.
  - CPI-W August values come from the BLS API (series CWUR0000SA0, file on disk).
- **SUI wage base:** 9,000 USD, statutory (4141.01) and not indexed. That reading of the statute is not confirmed this pass.
- **Withholding tables:** the commissioner re-issues them within 45 days of a rate change (OAC 5703-7-10) [US-OHS5-017]. Hence the 2026-08-01 edition.
- **Prevailing-wage thresholds:** biennial (4115.034).
- **School district rates:** an annual change list each January [US-OHS5-018].

## 12 data_protection
- **Breach notice (ORC 1349.19):** goes to affected Ohio residents within 45 days of discovery. Personal information includes a name combined with an SSN or an account number [US-OHS5-021].
- **SSN on pay statements:** no SSN-truncation rule for pay statements was located. 4113.14 does not require the SSN [US-OH-P5-1-001].
- **Confidence:** Medium.

## 13 live_legal_change (2026-01-01 to today)
- **HB 96 (136th GA):**
  - flat 2.75% PIT from TY2026 [US-OHS5-007];
  - municipal 718.01 amendments effective 2025-09-30 [US-OH-P5-2-003];
  - 2329.66 amended effective 2025-09-30 [US-OHS5-011].
- **Mid-year withholding tables and formula,** effective 2026-08-01 [US-OH-006, US-OHS5-001].
- **OAC 5703-7-10:** new supplemental rule effective 2026-01-01 [US-OHS5-017].
- **ORC 5747.01:** amended by SB 9, effective 2026-03-05 [US-OHS5-022]. The substance of SB 9 was not analysed.
- **School district changes,** effective 2026-01-01 [US-OHS5-018].
- **Already enacted for 2027:** minimum wage 11.40 / 5.70 [US-OHS5-004].
- **Not yet published:** 2027 withholding tables, 2027 ODJFS rates, 2027 school district changes.
- **Tier-B lead only (not a source):** news from EY and the Ohio CPA society (July 2026) about the 2026-08-01 tables and the 3.4% top withholding rate versus the 2.75% statutory rate. It is consistent with the A.2 files.

## Special populations (US-OWN-005, state round)

| Population | Ohio rule | register_id |
|---|---|---|
| Domestic / household | No Ohio withholding on domestic service in a private home (5747.06(A)(2)); babysitters in the employer's home and live-in companions are exempt from the minimum wage | US-OHS5-008, US-OHS5-004 |
| Agricultural | No Ohio withholding on agricultural labour (IRC 3121(g)) | US-OHS5-008 |
| Minors | Under 16: federal minimum wage 7.25; newspaper carriers under 18: no withholding; Minor Labor Law ORC 4109 (work permits) not read | US-OHS5-005, US-OHS5-008 |
| Tipped | 5.50 (2026) / 5.70 (2027) cash wage, tip credit to the full minimum; threshold more than 30 USD/month in tips | US-OHS5-005, US-OHS5-004 |
| Clergy / religious | No state rule beyond federal located (Ohio AGI follows federal; 5747.06 read) | US-OHS5-008, US-OHS5-022 |
| Students | No state withholding rule located; UI exclusions in 4141.01(B)(3) not read | open |
| Nonresident aliens | No state rule beyond federal located; Ohio withholds on nonresidents generally | US-OHS5-008 |
| Statutory employees | No state rule beyond federal located | US-OHS5-022 |
| Government employees | State and political subdivisions must withhold (5747.06(A)); public employers are outside the 4113.85 employer definition; federal employees are exempt from the Ohio minimum wage | US-OHS5-008, US-OHS5-012, US-OHS5-004 |
| Reciprocity-state residents | IN/KY/MI/PA/WV residents: no Ohio withholding; nonresident military spouse: no withholding | US-MULTI-005, US-OH-P5-2-006 |
| Small employers | Gross under 405,000 (2026) / 419,000 (2027): federal minimum wage; under 150,000: no state overtime duty | US-OHS5-005, US-OHS5-004 |

## ACCESS gaps
- https://tax.ohio.gov/business/employer-withholding: 404/403 shell to scripts. The Wayback copy https://web.archive.org/web/2026id_/https://tax.ohio.gov/business/employer-withholding resolves to 20260923233444 and also gives 404. Tried once.
- https://tax.ohio.gov/employer and https://tax.ohio.gov/business/ohio-business-taxes/employer-withholding: 404 shell. The municipal rate table on tax.ohio.gov could therefore not be read.
- https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/ohio_individual/2026_All_School_Districts.pdf: 404 (no 2026 full list at that path).
- https://jfs.ohio.gov/unemployment-services/for-employers/file-unemployment-taxes/tax-resources/contribution-rates: 404 to curl. The contents are held by US-OH-005 (earlier read) and US-OHS5-002.
- https://thefinder.tax.ohio.gov/: application shell only (lookup per address, no table).
- RITA https://www.ritaohio.com/Businesses/Faqs: HTTP 200 at the root this pass, but the employer FAQ was not re-read (US-OH-014 stays gated).

## Open questions
1. **ohio.municipal.rate_table:** no consolidated official table of municipal income tax rates and credits. To close: the Ohio Department of Taxation municipal income tax rate table (tax.ohio.gov, browser pass) or per-municipality ordinances via The Finder.
2. **ohio.sd.full_list_2026:** no consolidated 2026 list. The 2025 list plus the 2026 delta is the current basis. To close: the 2026 IT 1040 booklet school-district list (published January 2027) or a browser read of The Finder.
3. **Method of payment** (direct deposit / paycard consent): no statute read. To close: ORC 4113.15/4113.16 neighbourhood or ORC 1321, checked by the orchestrator's browser pass.
4. **ss.ui.wage_base indexation:** the 9,000 USD base is assumed statutory and fixed (ORC 4141.01(G)), not read. To close: ORC 4141.01(G)(1) text.
5. **Other leave with pay impact** (jury duty 2313.19, military 5903.02, voting 3599.06): not read.
6. **Deduction authorisation rules and IWO priority** (ORC 3121.03/3121.034): not read.
7. **Certified payroll** under ORC 4115.071 and the 2026 prevailing-wage threshold adjustment date: not read.
8. **UI quarterly report channel and format** (ODJFS employer portal / bulk upload spec): not read. Belongs to RSPEC.
9. **Individual UI separation notice under OAC 4141:** not read. 4141.28 has only the mass-layoff duty.
10. **2027 withholding tables, ODJFS 2027 rates and school district changes:** not yet published as of 2026-11-02. Re-check in January 2027.
11. **Fan-out note:** items 1–2 (municipal and SD tables) need one browser pass on tax.ohio.gov. Items 3–9 are independent ORC/OAC reads on codes.ohio.gov, which is reachable by curl and can go to one cheap worker.
