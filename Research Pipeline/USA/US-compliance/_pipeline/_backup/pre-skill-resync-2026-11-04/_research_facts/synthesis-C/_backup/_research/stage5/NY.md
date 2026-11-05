# Stage 5: New York (NY), 13-domain findings

Worker: compliance-source-hunter, JUR = NY. Date: 2026-11-02. Brief: `_prompts/stage5-brief.md`.
Budget: 60 fetches / 2 h declared. Used about 33 fetches and 10 searches, roughly 20 minutes. Acquisition stopped at the 75% line.
Shard: `00-official-sources/_register-shards/S5-NY.csv`, rows US-NYS5-001 to 023 (21 A.1/A.2 rows, 2 MANUAL tier-B leads).
Sources: `00-official-sources/ccg-sources/NY/` (21 files, 2.2 MB).
Reused active rows (not re-fetched): US-NY-001, US-NY-P5-2-001 (NYS-50-T-NYS/-NYC/-Y 1/26, local PDFs), US-NY-008, US-NY-007, US-NYP8-001 (PFL 2026, local), US-NYP9V-001 (UI rates 2026, local), US-NY-003/US-NYP7-001 (MCTMT), US-NY-010 (DBL), US-NYP7-004 (RSF), US-NY-P5-1-002 (Labor Law 220), US-NY-P5-2-002 / US-NY-013 / US-NY-009 (nonresident and convenience rule), US-FIL-007 (Pub 72.5), US-NYP9L-001 (postings).

**Housekeeping note.** The session scratchpad is shared by all Stage-5 workers. Early in the run, four US-ILS5 rows (IL worker data) were appended to S5-NY.csv by mistake. They were removed at once, and they still exist in S5-IL.csv. No other shard was touched. Later NY tooling ran from the private `scratchpad/ny5/`.

---

## 1. labour_code
- **Minimum wage.** From 2026-01-01: **17.00** per hour in NYC, Nassau, Suffolk and Westchester; **16.00** in the rest of the state (Labor Law 652(1-a)) [US-NYS5-002, A.1].
  - **2027.** No increase on 2027-01-01. DOL states that an off-ramp condition of 652(1-b)(d) was met. Rates stay 17.00 / 16.00 [US-NYS5-001, A.2].
  - Home care aides from 2027-01-01: 20.00 / 19.00 [US-NYS5-001].
  - Governor's proposal to change the off-ramps: a proposal only, not enacted.
- **Local minimum wages.** None by ordinance. The state law itself sets the regions (NYC; Nassau/Suffolk/Westchester; remainder) [US-NYS5-002].
- **Overtime (12 NYCRR 142-2.2).**
  - 1.5 × regular rate after 40 h per week, or 44 h for residential employees.
  - FLSA 13(a)(2)/(4) exemptions are not applied.
  - FLSA-exempt employees other than exec/admin/professional get 1.5 × the minimum rate.
  - Call-in pay: 4 h, or the scheduled shift if shorter.
  - Spread of hours over 10 h, or a split shift: +1 h at the minimum rate.
  - Exec/admin salary threshold from 2026-01-01: **1,275.00 per week** in NYC/LI/Westchester and **1,199.10 per week** in the rest of the state [US-NYS5-011, A.1, CR 142 (12/25)].
  - Farm workers: overtime after **52 h from 2026-01-01**, then 48 (2028), 44 (2030), 40 (2032) [US-NYS5-012].
  - Domestic workers: 40 h, or 44 h if live-in [US-NYS5-013].
- **Pay frequency (Labor Law 191).**
  - Manual workers: weekly, at most 7 days after the week ends. Semi-monthly only with commissioner authorisation (1,000+ NY employees) or for nonprofits.
  - Clerical and other workers: at least semi-monthly, on regular paydays fixed in advance.
  - Commission salespersons: at least monthly, with a written agreement kept for 3 years [US-NYS5-003].
  - Damages for manual-worker frequency violations are limited to lost interest on a first violation, where pay was at least semi-monthly (198, revision 2025-05-16) [US-NYS5-021].
- **Method of payment.** Direct deposit only with the employee's advance written consent (192). Exempt: exec/admin/professional earning over 1,300 per week, and farm workers [US-NYS5-004]. Pay-card rules (12 NYCRR Part 192) were not read (open question).
- **Confidence:** High.

## 2. income_tax
- **Withholding method.**
  - Tables: NYS-50-T-NYS (1/26), effective 2026-01-01 to 2026-12-31. Method I uses wage-bracket tables; Method II is exact calculation; Method III (top income) applies when annualised net wages are 1,077,550 or more [US-NY-001, US-NY-P5-2-001].
  - Certificate: IT-2104 (2026). An employee with a 2020+ W-4 and no IT-2104 is treated as zero allowances [US-NYS5-010].
  - Change notice: DTF page of 2025-12-02. The NYS and Yonkers tables changed for 2026; the NYC tables did not. No 2027 change is announced [US-NYS5-020].
- **Method II parameters, 2026.** The oracle is the official worked examples [US-NY-P5-2-001].
  - Deduction allowance (Table B), single / married: weekly 142.30 / 152.90; biweekly 284.60 / 305.80; semimonthly 308.35 / 331.25; monthly 616.70 / 662.50; annual 7,400 / 7,950.
  - Exemption: 1,000 per year (weekly 19.25; monthly 83.30).
  - Single annual schedule: 3.90% to 8,500; 4.40% to 11,700; 5.15% to 13,900; 5.40% to 80,650; 5.90% to 96,800; 7.03% to 107,650; 7.53% to 157,650; 6.40% to 215,400; 11.44% to 265,400; 7.35% to 1,077,550.
  - Married annual schedule: identical up to 96,800; then 6.57%, 7.07%, 8.01% to 211,550; 6.40% to 323,200; 13.49% to 373,200; 7.35% to 1,077,550; 7.65% above.
  - These are withholding schedules with recapture bands, not the statutory brackets.
- **G-DERIVE on the official examples** (Python, Decimal, ROUND_HALF_UP).
  - Table A = Table B + n × Table C, reproduced exactly (200.05, 866.60, 350.00, 36.15).
  - Examples 1, 3 and 4 reproduce exactly: 8.01, 3,576.63, 44.10.
  - **Example 2 does not reproduce:** 165.00 × 0.0753 = 12.4245, which rounds to 12.42, giving **258.50**. The booklet prints 12.43 and **258.51**. This one-cent residual is recorded as an oracle open question.
- **Supplemental rates.** NYS 11.70%; NYC resident 4.25%; Yonkers resident 1.95975%; Yonkers nonresident 0.50% [US-NY-001, US-NY-011]. Alternatively use the aggregate method [US-NYS5-010].
- **Rounding.** The tax does not fix a rounding rule. Withhold to the cent per the tables or the formula [US-NY-P5-2-001].
- **Exempt certificate.** Tax Law 671(a)(3): under 18, over 65, or full-time student under 25 with no prior-year and no expected liability [US-NYS5-010].
- **Local income taxes.**
  - NYC resident tax: residence-based, withheld regardless of work location.
  - Yonkers resident surcharge, and Yonkers nonresident earnings tax on work in Yonkers. No Yonkers withholding is needed where Yonkers wages are expected to be 3,000 or less.
  - All of these are withheld and filed on the NYS-1 / NYS-45 (T3 piggyback) [US-NY-008, US-NYS5-010].
  - The NYC tables did not change for 2026 [US-NYS5-020].
- **Resident and nonresident.**
  - Residents: all wages are withheld, wherever earned.
  - Nonresidents: NY-source wages only, allocated on IT-2104.1. TSB-M-12(5)I covers the 14-day rule.
  - Convenience-of-employer rule applies [US-NY-013, US-NY-P5-2-002, US-NY-009].
  - No reciprocity agreements [US-NY-P5-2-002].
- **Confidence:** High for state. Medium-High for NYC/Yonkers, which rest on existing rows.

## 3. social_security
- **SUI.**
  - 2026 wage base **17,600**. From 2026 the base is 18% of the state average annual wage, rounded up to 100, and is never reduced [US-NYS5-010; US-NY-007].
  - The 2027 base was not published on the pages read as of 2026-11-01 [US-NYP9V-001].
  - New employer: 4.025% total (3.4% normal + 0.625% subsidiary), plus RSF 0.075%, which gives 4.1%. Range 1.625% to 9.425% [US-NYP9V-001].
  - No employee UI contribution.
  - The FY2026 budget paid off the UI loan. Relevant to FUTA credit reduction; see the FED/MULTI units [US-NYP9V-001 page text].
- **PFL.**
  - 2026: 0.432% of wages, annual employee maximum 411.91 [US-NYP8-001]. The benefit is 67% of the employee's average weekly wage, capped at 67% of the NYSAWW, for up to 12 weeks [US-NYP8-001 text].
  - Derivation, not an authority figure: 411.91 / 0.00432 = 95,349.54, which implies an NYSAWW of 1,833.64 and a maximum benefit of 1,228.54. Not used as a fact.
  - **2027: lead only.** 0.452%, maximum 451.81 [US-NYS5-022, MANUAL]. The DFS page is blocked to curl.
- **DBL.** Employee 0.5% of wages, at most 0.60 per week; the employer pays the rest [US-NY-010].
- **Employer levies.** MCTMT and RSF, per the P7/P9 list [US-NYP7-001, US-NYP7-004]. Not redone.
- **Confidence:** High for 2026. Low for 2027 PFL until the DFS page is read.

## 4. payslip_statute
- **Content (Labor Law 195(3)), with every payment.**
  - Dates of work; employee name; employer name, address and phone.
  - Rate(s) and basis; gross; deductions; allowances claimed toward minimum wage; home-care aide benefits; prevailing-wage supplements; net.
  - Non-exempt employees: regular and overtime rates, and regular and overtime hours.
  - Piece-rate employees: piece rates and counts [US-NYS5-006].
- **Electronic delivery.** The statute is silent. The DOL guidance on electronic statements was not read (open question).
- **Retention.** Payroll records: 6 years (195(4)). Hire-notice acknowledgement: 6 years [US-NYS5-006]. Tax records: 4 years [US-NYS5-010].
- **Hire notice.** In English and in the employee's primary language (195(1)) [US-NY-P5-1-003].
- **NYC PTO.** Lead only: the accrued, used and balance figures on each pay statement [US-NYS5-023, MANUAL].
- **Confidence:** High for state. NYC pay-statement item still open.

## 5. reporting_instruments
- **NYS-45** (quarterly, combined withholding + wage reporting + UI): due 30 Apr, 31 Jul, 31 Oct, 31 Jan. Parts A, B and C are all mandatory. E-file and ACH are mandatory, with a 50 USD penalty per paper document or payment [US-NYS5-010]. Upload spec: Pub 72.5 [US-FIL-007].
- **NYS-1 deposit.** Due within 3 business days (if 15,000+ was withheld in the year before the previous year) or 5 business days after the payroll that takes quarter-to-date withholding to 700 or more. Below 700, pay with the NYS-45. New employers use 5 days [US-NYS5-010].
- **W-2.** No copy is filed with NY. Quarterly NYS-45 Part C replaces it.
  - State wages box = federal box 1, for residents and for nonresidents with any NY service.
  - NYC local box = box 1 for full-year residents, and resident-period wages for part-year residents.
  - Yonkers follows the NYS rule [US-NYS5-010].
  - The separate annual-reconciliation mechanics in the Q4 NYS-45 instructions (NYS-45-I) were not read (open question).
- **New hire.** Report to DTF within **20 calendar days**. This includes rehires after 60+ days of separation. Electronic reporting: two monthly submissions 12 to 16 days apart. Fields: name, address, SSN, hire date, employer name and address, EIN, dependent health insurance availability and date. For a nonresident alien, the 20 days run from SSN issue [US-NYS5-010].
- **Registration.** NY Business Express (NYBE) for UI, wage reporting and withholding [US-NYS5-010].
- **MCTMT.** MTA-305, quarterly [US-NY-003].
- **Confidence:** High.

## 6. leave
- **State paid sick leave (196-b).**
  - Entitlement by employer size: 4 or fewer employees, 40 h unpaid (paid if net income over 1M); 5 to 99 employees, 40 h paid; 100 or more, 56 h paid.
  - Accrual: 1 h per 30 h worked; front-loading allowed.
  - Paid at the regular rate, or the minimum wage if higher. Maximum use increment 4 h.
  - Carryover required, but use may be capped. No payout at separation [US-NYS5-007].
- **Paid prenatal leave.** 20 h per 52 weeks from 2025-01-01, paid at the regular rate, no payout [US-NYS5-007].
- **NYC Protected Time Off.** Paid 40 or 56 h, plus **32 h unpaid** from the start of employment, plus 20 h paid prenatal leave [US-NYS5-018, partial, wayback copy]. Start date and rule details are leads only [US-NYS5-023].
- **PFL benefit-side payroll interaction.** Benefit 67% of AAWW, capped at 67% of NYSAWW, for 12 weeks [US-NYP8-001]. Paid by the insurer, so not wages from the employer. Taxability was not researched.
- **Confidence:** High for state. Medium for NYC.

## 7. termination
- **Final pay.** By the next regular payday for the period in which termination occurred, for both discharge and resignation; by mail on request (191(3)) [US-NYS5-003].
- **Termination notice.** Written notice of the exact termination date and the benefits cancellation date, within 5 working days (195(6)) [US-NYS5-006].
- **Accrued vacation.**
  - No statutory payout. It is a "wage supplement" under 198-c, payable per the policy or agreement [US-NYS5-008].
  - The forfeiture-notice rule comes from DOL guidance and case law and was not read.
  - Unused sick leave and prenatal leave: no payout [US-NYS5-007].
- **UI separation notice.** Form **IA 12.3** goes to every worker who is laid off, discharged or quits, or whose hours are cut to 30 or fewer per week [US-NYS5-017]. The timing rule (12 NYCRR 472.8) was not read.
- **NY WARN.** Not researched (not payroll-calculating).
- **Confidence:** High for timing. Medium for vacation.

## 8. benefits_in_kind
- **Conformity.** The NY return starts from federal wages (W-2 box 1), so the federal exclusions for 401(k), 403(b), 457, 125, HSA, transit and group-term life carry over.
- **Departures.** 414(h) contributions of NY public employees are added back (IT-201 line 21) [US-NYS5-019]. NYC flexible-benefits (IRC 125) addback for NYC employees via IT-225: not read (open question).
- **UI.** UI remuneration includes the reasonable value of meals and lodging, and tips [US-NYS5-010].
- **Minimum-wage credits, 2026 (Part 142).**
  - Meals: 5.80 per meal (NYC/LI/Westchester) and 5.50 (rest of state).
  - Lodging: 7.15 and 6.75 per day.
  - Uniform maintenance, weekly: 21.10 / 16.75 / 10.10 (NYC/LI/Westchester) and 19.85 / 15.80 / 9.55 (rest of state) [US-NYS5-011].
- **Confidence:** Medium-High.

## 9. deductions_garnishments
- **Authorised deductions (193).**
  - Allowed only if required by law, or authorised voluntarily in writing within the listed categories. Authorisations are kept for the period of employment plus 6 years.
  - Overpayment and advance recovery follow DOL regulations.
  - Revocation takes effect within 4 pay periods or 8 weeks.
  - The expanded text is marked effective until **2028-11-06**; the site's latest revision is dated 2026-07-03 [US-NYS5-005].
- **Creditor income execution (CPLR 5231).**
  - Up to **10% of gross**, and never more than 25% of disposable earnings.
  - The withholding must not reduce weekly disposable earnings below the greater of 30 × the federal minimum wage or 30 × the NY 652 minimum wage. Derived floor: 30 × 17.00 = **510.00** (NYC/LI/Westchester) and 30 × 16.00 = **480.00** (rest of state). Which regional rate applies is an open question.
  - When support is also withheld, the creditor's share is capped at 25% of disposable minus the support deducted.
  - No income execution for medical-debt judgments [US-NYS5-015].
- **Support (CPLR 5241).**
  - Start no later than the first pay period 14 days after service; remit to the SDU within 7 business days of payday.
  - Limits 50% / 60% of disposable, or 55% / 65% with arrears over 12 weeks.
  - Support takes priority over any other process. Multiple support orders are prorated. Order: current support, then health premium, then arrears.
  - Notify the issuer on termination [US-NYS5-016]. The employer fee amount is not in the section read.
- **State tax levies.** Not researched (open).
- **Confidence:** High.

## 10. collective_agreements (prevailing wage)
- **Labor Law 220.** Public-work prevailing rates and supplements [US-NY-P5-1-002].
- **Pay statement.** Must identify prevailing-wage supplements (195(3)) [US-NYS5-006].
- Certified payroll mechanics and thresholds were not re-researched (P5/P6 rows reused).
- **Confidence:** Medium.

## 11. indexation
- **Minimum wage.** From 2027, current rate × change in the 3-year average of August-to-July CPI-W Northeast, rounded to 0.05. Off-ramps limited to 2 consecutive years; published by October 1 [US-NYS5-002]. 2027 result: no increase [US-NYS5-001].
- **Exempt salary thresholds and meal/lodging credits.** Move with the minimum-wage orders (652(2)) [US-NYS5-002, US-NYS5-011].
- **UI wage base.** 18% of the state average annual wage, rounded up to 100 [US-NYS5-010].
- **PFL.** DFS rate and cap published by September 1 each year [US-NYP8-001].
- **Withholding tables.** Reissued as the law changes [US-NYS5-020].
- **Derivation line.** 2027 minimum wage = 17.00 / 16.00 (off-ramp, no step). PFL cap derivation in §3.

## 12. data_protection
- **Labor Law 203-d.** No public display of SSNs, no SSN on badges or time cards, no SSN in unrestricted files, no disclosure of employee personal information to the public. Penalty up to 500 USD [US-NYS5-009].
- **SSN on payslips.** Not a required pay-statement field. No truncation rule found.
- **UI information.** Confidential under UI Law 537 [US-NYS5-010].
- **Confidence:** High. General Business Law 399-ddd was not read.

## 13. live_legal_change (2026-01-01 to 2026-11-02, and enacted for 2027)
- **2026-01-01.**
  - New NYS and Yonkers withholding tables (NYC unchanged) [US-NYS5-020].
  - Minimum wage 17.00 / 16.00 [US-NYS5-002].
  - Exempt thresholds 1,275 / 1,199.10 [US-NYS5-011].
  - Farm overtime threshold 52 h [US-NYS5-012].
  - UI wage base 17,600 under the new formula [US-NYS5-010].
  - PFL 0.432% / 411.91 [US-NYP8-001].
- **2026-02-22 / 2026-07-23 (lead).** NYC Protected Time Off: 32 h unpaid, and the rules [US-NYS5-023 MANUAL; US-NYS5-018].
- **2026-07-03.** Labor Law 193 revision on the official site; the 2028-11-06 sunset is visible [US-NYS5-005].
- **2027-01-01.** Minimum wage frozen by off-ramp [US-NYS5-001]. Home care aides 20.00 / 19.00 [US-NYS5-001]. PFL 2027 lead [US-NYS5-022 MANUAL].
- **No 2027 withholding change announced** [US-NYS5-020].
- **2025 (in force).** Pay-frequency damages limitation (198) [US-NYS5-021]. Prenatal leave [US-NYS5-007].

---

## Special populations (state round, US-OWN-005)
| Population | NY rule | register_id |
|---|---|---|
| Domestic/household | Overtime after 40 h (44 live-in). UI and wage reporting if cash wages of 500+ in a quarter. Income tax withholding voluntary. Babysitters under 18 excluded from UI. Registration via NYBE. | US-NYS5-013, US-NYS5-010 |
| Agricultural | Farm minimum wage 17 / 16. Overtime after 52 h (2026), then 48 (2028). UI liability at 20,000 cash wages in a quarter or 10+ workers on a day in 20 weeks. H-2A excluded from UI. Direct-deposit consent rule does not apply. | US-NYS5-012, US-NYS5-010, US-NYS5-004 |
| Minors | Employment certificate for ages 16-17 (exceptions listed). No youth minimum wage found. Withholding exemption under 18 if no liability (671(a)(3)). Daytime school students excluded from UI (except nonprofit/government employers). | US-NYS5-014, US-NYS5-010 |
| Tipped | Cash wage / tip credit 2026-27: service employees 14.15 / 2.85 (NYC/LI/Westchester), 13.30 / 2.70 (rest of state); food service 11.35 / 5.65 and 10.70 / 5.30. Hospitality employers only. Tips are UI remuneration. | US-NYS5-001, US-NYS5-010 |
| Clergy/religious | Ordained ministers and religious-order members excluded from UI for nonprofits. Income tax: no state rule beyond federal wage definition (NYS-50 uses federal wages). | US-NYS5-010 |
| Students | Tax Law 671(a)(3) exemption: full-time under 25 with no liability. UI exclusions: own-school student employment, work-study, camp students. College students generally covered. | US-NYS5-010 |
| Nonresident aliens | Treaty-exempt under IRS rules = exempt for NYS/NYC/Yonkers with no extra form. New-hire report due 20 days after SSN issue. | US-NYS5-010 |
| Statutory employees | No state rule beyond federal located (NYS-50 read). Misclassification: the business directing the work is liable for UI. | US-NYS5-010 |
| Government employees | 414(h) addback in NY income. Nonprofit/government/tribe: UI via the reimbursement option, and student wages are covered. | US-NYS5-019, US-NYS5-010 |

---

## ACCESS gaps (exact URLs; for the orchestrator's browser pass)
1. `https://www.dfs.ny.gov/apps-and-licensing/health-insurers/pfl-rate-decision-2027-page`: HTTP 403 (curl). `https://web.archive.org/web/2026id_/…pfl-rate-decision-2027-page`: 404. Needed for PFL 2027 rate and cap (US-NYS5-022).
2. `https://paidfamilyleave.ny.gov/2026`: 403. Wayback 2026id_: 403. Needed for the PFL 2026 maximum weekly benefit as an authority figure.
3. `https://www.nyc.gov/site/dca/about/paid-sick-leave-law.page`: 403 (wayback copy used). The DCWP FAQ (02/2026) PDF and NYC Admin. Code 20-911 ff. were not reached (US-NYS5-023).
4. `https://dol.ny.gov/overtime-0` and `https://dol.ny.gov/overtime-frequently-asked-questions`: 404 (overtime covered instead by CR 142).
5. `https://www.tax.ny.gov/pdf/publications/withholding/nys50.pdf`: 404. The guide now exists only as HTML (`/forms/publications/wt/nys50.htm`, used).

## Open questions
- **nys.wh.oracle.example2.residual.** NYS-50-T-NYS (1/26) Method II Example 2 prints 12.43 / 258.51. Straight half-up arithmetic gives 12.42 / 258.50 (165.00 × 0.0753 = 12.4245). Engine-versus-booklet residual of 0.01. **Would close it:** a DTF statement of the rounding convention, or the DTF online withholding calculator result for the same case.
- **pfl.rate.2027 / pfl.contribution.max.annual (2027).** Lead 0.452% / 451.81 (tier B). **Would close it:** the DFS 2027 rate decision page, read in a browser.
- **pfl.benefit.max.weekly (2026).** Derived 1,228.54; not authority-stated. **Would close it:** the DOL/PFL "2026 updates" page or the NYSAWW notice from DOL R&S.
- **nyc.pto.paystatement / nyc.pto.unpaid.effective_from.** **Would close it:** NYC Admin. Code 20-913/20-919 text, or the DCWP FAQ (02/2026).
- **sui.wage_base (2027).** Not yet published. **Would close it:** the DOL UI rate page or the NYS-50 2027 edition (expected December 2026).
- **garn.creditor.floor.region.** Does 5231 use the regional 652 rate of the work location (510 vs 480 per week)? **Would close it:** DOL or court guidance, or the income execution form text.
- **paycard.rules.** 12 NYCRR Part 192 (pay cards / direct deposit notice) not read. **Would close it:** DOL CR 192 copy.
- **payslip.electronic.** DOL position on electronic wage statements not read. **Would close it:** DOL wage-statement FAQ.
- **nys45.annual_reconciliation.** Q4 NYS-45 annual-reconciliation mechanics. **Would close it:** NYS-45-I instructions (DTF).
- **bik.nyc.flex125.addback.** **Would close it:** IT-225-I (DTF), addition code for the NYC flexible benefits program.
- **term.ia12_3.timing.** **Would close it:** 12 NYCRR 472.8 text (DOL).
- **garn.state_tax_levy.** NY DTF income execution for tax warrants (Tax Law 692 / CPLR 5231 interplay) not researched.
