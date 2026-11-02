# CCG research pack - annex_WY (Wyoming)

Synthesis-B worker MN-WY, 2026-11-02. Unit `annex_WY` of the CCG (jurisdiction annex, all 13 domains + special populations).
Facts file: `_research/CCG-annex_WY-facts.json` (24 facts, 9 pending on the register_id pattern defect, 5 unresolved). Every claim below carries its register_id inline; numbers may be cited in the CCG only through a fact key.

## 0. How to use this pack

- Body sections 1-13 and Special populations are the stage-5 findings (`_research/stage5/WY.md`), carried verbatim because they are already organised by the 13 CCG domains with register ids inline.
- Federal layer (FIT, FICA, FUTA, W-2/941/940), the multistate rules (reciprocity, sourcing) and the language seams (US-OWN-006: payslip in English; second-language duties attach to notices and posters only) live in annex_FED / annex_MULTI and are not repeated here.
- Special populations (US-OWN-005): the state-level rules are in the Special populations table below; the country-wide coverage matrix is CCG unit `coverage`.
- Values are 2026 unless the fact says otherwise. 2027 values appear only where the row carries an enacted or published 2027 figure; projections are never facts.

## 0.1 Synthesis decisions and traps (bind the builder)

- WY has NO wage tax (T1). State minimum 5.15 matters only outside FLSA coverage.
- Accrued vacation is payable at termination unless a written forfeiture policy was acknowledged in writing - DD flag required.
- Monopolistic state workers' compensation fund: monthly payroll reports (employer-paid).
- UI 2026 rate table values not published - blocking for the WTC rate setup.

## 0.2 Register status check of the ids cited in the findings

These ids appear in the findings but are not plain `active`; do not cite them for a number:

- US-WYP9W-001: partial
- US-WYP9W-002: partial
- US-WYS5-010: partial

## 0.3 Facts emitted

| key | value | from | to | register_id | conf |
|---|---|---|---|---|---|
| `wy.minwage.hourly` | 5.15 USD | 2026-05-08 |  | US-WYS5-001 | high |
| `wy.minwage.tipped.cash_wage` | 2.13 USD | 2026-05-08 |  | US-WYS5-001 | high |
| `wy.labour.minwage.youth_training.hourly` | 4.25 USD | 2026-05-08 |  | US-WYS5-001 | high |
| `wy.labour.overtime.state_rule` | none for private sector (FLSA only) | 2026-05-08 |  | US-WYS5-005 | high |
| `wy.labour.pay_frequency.semimonthly_industries` | railroads, mines, refineries, oil and gas, factories, mills, workshops: semimonthly (1-15 by 1st; rest by 15th) | 2026-05-08 |  | US-WYS5-002 | high |
| `wy.labour.direct_deposit.consent_required` | True | 2026-05-08 |  | US-WYS5-002 | high |
| `wy.records.retention_years` | 2 years | 2026-05-08 |  | US-WYS5-001 | high |
| `wy.sui.wage_base` | 32400 USD | 2025-01-01 | 2025-12-31 | US-WYS5-008 | high |
| `wy.sui.wage_base` | 33800 USD | 2026-01-01 | 2026-12-31 | US-WYS5-008 | high |
| `wy.sui.wage_base` | 34900 USD | 2027-01-01 |  | US-WYS5-008 | high |
| `wy.ui.rate.max` | 10 % | 2025-01-01 |  | US-WYS5-011 | high |
| `wy.ui.delinquent_surcharge.rate` | 2 % | 2026-01-01 |  | US-WYP9W-001 | medium |
| `wy.sui.wage_base.other_state_credit` | True | 2026-05-08 |  | US-WYS5-003 | high |
| `wy.sui.wages.401k_included` | True | 2026-05-08 |  | US-WYS5-003 | high |
| `wy.wc.state_fund.monopolistic` | True | 2026-01-01 |  | US-WYS5-012 | high |
| `wy.report.ui.quarterly_due` | Apr 30; Jul 31; Oct 31; Jan 31 | 2026-01-01 |  | US-WYS5-009 | high |
| `wy.newhire.report_days` | 20 days | 2026-05-08 |  | US-WYS5-006 | high |
| `wy.leave.voting.paid_hours` | 1 hours | 2026-01-01 |  | US-WYS5-016 | high |
| `wy.final_pay.rule` | no later than the usual regular payday | 2026-05-08 |  | US-WYS5-002 | high |
| `wy.term.vacation.payout` | payable unless written forfeiture policy acknowledged in writing by employee | 2026-05-08 |  | US-WYS5-002 | high |
| `wy.garn.creditor.max_percent` | 25 % | 2026-01-01 |  | US-WYS5-013 | high |
| `wy.garn.iwo.employer_fee.per_payment` | 5 USD | 2026-01-01 |  | US-WYS5-014 | high |
| `wy.garn.iwo.remit_days` | 7 days | 2026-01-01 |  | US-WYS5-014 | high |
| `wy.data.breach.redaction_digits` | 5 | 2026-01-01 |  | US-WYS5-015 | high |
| `wy.pit.exists` | False | 2026-01-01 |  | US-WY-P5-1-001 (PENDING id pattern) | high |
| `wy.local_wage_tax.exists` | False | 2026-01-01 |  | US-WY-P5-1-001 (PENDING id pattern) | high |
| `wy.ui.rate.statutory_base` | 8.5 % | 2026-01-01 |  | US-WY-P5-2-001 (PENDING id pattern) | high |
| `wy.ui.rate.new_employer.floor` | 1 % | 2026-01-01 |  | US-WY-P5-1-002 (PENDING id pattern) | high |
| `wy.sui.employee.rate` | 0 % | 2026-01-01 |  | US-WY-P5-1-002 (PENDING id pattern) | high |
| `wy.sdi_pfml.exists` | False | 2026-01-01 |  | US-WY-P5-1-004 (PENDING id pattern) | high |
| `wy.payslip.items` | itemized written statement of all deductions on detachable part of check/voucher or attached slip | 2026-01-01 |  | US-WY-P5-1-005 (PENDING id pattern) | high |
| `wy.leave.sick.state_statute.exists` | False | 2026-01-01 |  | US-WY-P5-1-004 (PENDING id pattern) | high |
| `wy.prevailing_wage.construction_threshold` | 100000 USD | 2026-01-01 |  | US-WY-P5-1-006 (PENDING id pattern) | medium |

# Findings by domain (stage 5)

## 1. labour_code
- **Minimum wage: USD 5.15/hour.** Source: W.S. 27-4-202(a) [US-WYS5-001, A.1]. The DWS state poster (June 2025) is a second document family and says the same [US-WYS5-012, A.2].
  - The rate is not indexed.
  - No 2027 change has been enacted (2026 session check, see section 13).
  - There is no local minimum wage, and no local power to set one was found.
  - **In practice the FLSA rate of USD 7.25 binds every FLSA-covered employer.** The state rate matters only for employment outside the FLSA.
  - Confidence: high.
- **Tipped employees:** the cash wage is at least USD 2.13. The employer makes up the difference to 5.15 if wage plus tips fall short. A tipped employee is one who customarily receives more than USD 30 a month in tips, and must furnish a monthly tip record (27-4-202(b)) [US-WYS5-001]. Tips are the employee's sole property (27-4-507(a)) [US-WYS5-002].
- **Youth training wage:** USD 4.25 for employees under 20, during the first 90 consecutive days (27-4-202(c)) [US-WYS5-001, US-WYS5-012].
- **Exclusions from the minimum-wage article** (27-4-201(a)(iv)) [US-WYS5-001]:
  - agriculture;
  - domestic service in a private home;
  - bona fide executive, administrative and professional employees;
  - federal, state and political-subdivision employees;
  - volunteers and non-employment nonprofit service;
  - outside salesmen paid only by commission;
  - on-call ambulance drivers.
- **Overtime:** there is no private-sector state rule, so the FLSA governs. 27-5-101 covers only state and county employees (8 hours a day, 40 a week, 1.5x when the governing body authorises it) [US-WYS5-005].
- **Pay frequency and paydays** (27-4-101(a)) [US-WYS5-002]:
  - Semimonthly pay is mandatory only for railroads, mines, refineries, oil and gas, factories, mills and workshops.
  - Wages for the 1st to 15th are due by the 1st of the next month. Wages for the second half are due by the 15th of the next month.
  - If the payday is not a working day, pay on the preceding working day.
  - The law must be posted in 2 places.
  - No general pay-frequency rule was found for other employers.
  - Agricultural operations are exempt (27-4-101(c)).
- **Method of payment:** lawful money or a check cashable at a bank. Direct deposit is allowed only if the employee has *voluntarily authorised* it (27-4-101(b), 27-4-104(a)) [US-WYS5-002]. No paycard statute was located.
- **Records:** name, address, occupation, rate, amount paid per pay period, and hours per day and per week, kept 2 years (27-4-203) [US-WYS5-001].
- **Enforcement:** DWS Labor Standards takes wage claims for work physically done in Wyoming. Claims are capped at 2 months' wages outside bankruptcy (27-4-502(a)). The filing window is generally 2 years [US-WYS5-002, US-WYS5-018].

## 2. income_tax
- **No state income tax and no withholding.** The state preempts income, earnings and wage-based taxes, and no county, city or subdivision may levy them (W.S. 39-12-101). Chapter 7 (income taxes) was repealed in 1998 [US-WY-P5-1-001, A.1, reused].
- Not applicable, all for the same reason: W-4 equivalent, supplemental rate, rounding, withholding return, state W-2 and reconciliation.
- Reciprocity, resident/nonresident rules and convenience rule: not applicable.
- **Oracle:** the federal one only (Pub. 15-T, FED unit).
- Confidence: high.

## 3. social_security
- **SUI agency:** DWS Unemployment Insurance Division, through the WYUI portal [US-WY-SUI-002].
- **Taxable wage base** [US-WYS5-008, A.2, local copy; same figures as US-WY-SUI-001]:

| Year | Wage base (USD) | Applies |
|---|---|---|
| 2025 | 32,400 | closed 2025-12-31 |
| 2026 | 33,800 | from 2026-01-01 |
| 2027 | 34,900 | from 2027-01-01 |

- **Indexation (G-DERIVE):** the base is 55% of the statewide average annual wage, rounded down to the lowest USD 100 (27-3-102(a)(xviii)(A), 27-3-303(a)) [US-WYS5-003, A.1]. Section 11 has the derivation.
- **Employer only.** Contributions "shall not be deducted from employee wages" (27-3-503(a)) [US-WY-P5-1-002]. There is no employee UI contribution.
- **Rates:**
  - Total rate = base rate + adjustment factors. The base rate is the benefit ratio, or the industry average for employers with under 3 years of experience.
  - The statutory base rate is 8.5%, which also applies when registration is incomplete [US-WY-P5-2-001].
  - A new employer pays the prior-year average rate of its industry plus the factors, never less than 1% plus the factors (27-3-503(f)) [US-WY-P5-1-002].
  - Delinquent employers pay +2% [US-WYP9W-001].
  - The maximum is **10%**, re-derived: 8.5% base + the 1.5% cap on factors (a)+(b) = 10.0%. The DWS memo says the same: "statutory maximum tax rate of 10%" [US-WYS5-011, A.2].
  - **The 2025 minimum was 0.14%:** 0.0014 x 32,400 = USD 45.36, which matches the memo [US-WYS5-011].
  - **The numeric 2026 minimum rate, the industry new-employer rates and the factor values are NOT published on any authority page read.** Open question WY-OQ-1.
- **SUI wage-base credit for wages reported to another state (MULTI-OQ-2): YES.** The base counts wages "paid during any calendar year to an individual by each employer or a predecessor... including employment under any other state unemployment compensation law" (27-3-102(a)(xviii)(A)) [US-WYS5-003]. Confidence: high.
- **UI wage exclusions:** these follow FUTA. The section 8 table lists them [US-WYS5-003].
- **SDI/TDI/PFML/LTC:** none.
  - No PFML or TDI in Title 27 [US-WY-P5-1-004].
  - Wyoming is not on the DOL list of PFML states [US-WIR3-004].
  - No 2026 enactment (section 13).
- **Other levies:** the employer-paid adjustment factor sits inside the UI rate and is split 20% UI fund / 60% Employment Support Fund / 20% Workforce Development Training Fund [US-WY-P5-1-003, US-WYP9W-001]. No transit levy and no separate payroll levy.
- **Workers' compensation (payroll-relevant): Wyoming has a monopolistic state fund.**
  - Coverage is mandatory for extra-hazardous employment and elective otherwise [US-WYS5-012].
  - Payroll reports and the employer-paid premium are due monthly, by the last day of the month after the month the earnings are paid. Quarterly reporting needs permission.
  - Joint UI/WC payroll reporting is available through DWS (27-14-202) [US-WYS5-007].
  - No employee-share provision was located.
- Confidence: high on base and structure; low on the 2026 rate numbers (unpublished).

## 4. payslip_statute
- **Content:** at each payment the employer furnishes a detachable part of the check, draft or voucher, or an attached slip. It gives "an itemized statement in writing showing all deductions made" (27-4-101(b)) [US-WY-P5-1-005, A.1]. No other content is mandated: no hours, rates, employer name or pay period required.
- **Exemption:** agricultural operations (27-4-101(c)).
- **Electronic delivery:** the statute is silent. No electronic-consent rule was found.
- **Retention:** the payroll record is kept 2 years (27-4-203) [US-WYS5-001].
- **Language:** no language rule [US-WYL-001].
- **Reach:** no extraterritorial rule. DWS enforces wage claims for "work physically done within the state" [US-WYS5-018, A.3]. **Rule: the pay-statement duty applies to work performed in Wyoming (MULTI-OQ-8 default holds).**
- Confidence: high.

## 5. reporting_instruments
- **Withholding return, deposits, annual reconciliation, state W-2:** none, because there is no income tax [US-WY-P5-1-001].
- **Quarterly UI contribution and wage report (WYUI)** [US-WYS5-009, A.2; US-WY-SUI-002]:

| Quarter | Due | Delinquent from |
|---|---|---|
| Q1 | Apr 30 | May 1 |
| Q2 | Jul 31 | Aug 1 |
| Q3 | Oct 31 | Nov 1 |
| Q4 | Jan 31 | Feb 1 |

  Weekend or holiday dates roll to the next business day. The file format/spec of the WYUI wage file was not read (WY-OQ-3).
- **Service suppliers (PEOs):** the service supplier keeps separate records, submits a quarterly client list and files a separate quarterly report for each client; the client is jointly liable if the supplier defaults; a temporary service contractor is the employing unit of its temporary workers (27-3-502) [US-WYS5-019, A.1].
- **Workers' compensation payroll report:** monthly (quarterly by permission), with joint UI/WC reporting [US-WYS5-007].
- **New-hire reporting** (27-1-115) [US-WYS5-006, A.1]:
  - Report to DWS within 20 days. Electronic filers may instead send 2 monthly transmissions 12-16 days apart.
  - Fields: employee name, address, SSN and first day of services; employer name, address and FEIN.
  - Form: the IRS W-4 or a DWS-approved equivalent.
  - The multistate single-state election is available.
  - Channel: the "Wyoming New Hire Reporting Center", newhire-reporting.com/wy-newhire [US-WYS5-010, A.3, partial]. The portal was unreachable (ACCESS gap).
- **Registration:** Joint Business Registration in WYUI [US-WY-P5-2-001].
- **Third-party access:** POA form MODES-4444 (7/19) [US-WYR3-001].
- Confidence: high on deadlines; medium on formats.

## 6. leave
- **Paid sick leave:** no statute. Title 27 has none; the one "sick leave" hit is in workers' compensation [US-WY-P5-1-004, US-WYL-001].
- **PFML benefit interaction:** none, as there is no programme.
- **Voting leave:** 1 hour paid on election day (primary, general, special congressional), unless the employee has 3+ consecutive non-working hours while the polls are open. Pay is kept only if the employee votes (22-2-111) [US-WYS5-016, A.1].
- **Jury service:** protected from discharge, but no duty to pay (1-11-401) [US-WYS5-013].
- **Public employees:** firefighters' paid leave and hazard pay, HB0035 (2026, chapter 4), applies to public employers only (out of private scope) [US-WYS5-017].
- Confidence: high.

## 7. termination
- **Final pay, quit or discharge:** due no later than the employer's usual regular payday, or the time a CBA sets. The employer may offset sums the employee owes. Commission sales agents with custody of accounts are excluded. In a suit, 18% p.a. interest plus attorney fees apply (27-4-104) [US-WYS5-002].
- **Layoff or suspension:** wages are paid on the next regular payday (27-4-101(d)).
- **Accrued vacation:** it is wages, payable at termination, *unless* a written policy provides for forfeiture *and* the employee has acknowledged it in writing (27-4-501(a)(iii)) [US-WYS5-002]. **The DD needs a flag: `vacation_forfeiture_policy_acknowledged`.**
- **Notices:** no state UI separation notice and no state WARN law were found in Title 27.
- **Child support:** the employer notifies the clerk within 30 days of termination (20-6-212(e)) [US-WYS5-014].
- **Non-competes:** most are void from 2025-07-01 (W.S. 1-23-108, per the DWS poster) [US-WYS5-012]. Not a payroll item.
- Confidence: high.

## 8. benefits_in_kind
- **Income tax:** no conformity question arises (no tax).
- **UI wage definition** (27-3-102(a)(xviii)) [US-WYS5-003]: each item below is excluded only to the extent it is not FUTA wages. Excluded:
  - sec. 125 benefits, except cash;
  - sec. 129 dependent care;
  - sec. 120 legal services;
  - educational assistance;
  - achievement awards;
  - group-term life cost;
  - moving expenses;
  - employer contributions to qualified plans, IRAs and 403(b);
  - convenience meals and lodging on premises;
  - retirement, health and death plan premiums;
  - employer-paid FICA;
  - SUB pay;
  - sick pay after 6 months of illness.
- **Effect:** employee 401(k) elective deferrals stay UI wages, as under FUTA. No Wyoming departure from FUTA was found.
- The cash value of non-cash remuneration is "prescribed by rule of the commission". The rule was not read.
- Confidence: high.

## 9. deductions_garnishments
- **Wage-deduction authorisation:**
  - No general written-authorisation statute.
  - The employer may offset sums the employee owes against final wages (27-4-104(a)).
  - Dishonoured-check deductions are banned except listed cases (27-4-116).
  - Assignments of future wages need the spouse's written consent if the employee is married (27-4-111). For loans under USD 200 they need written employer acceptance plus filing (27-4-110) [US-WYS5-002].
- **Continuing garnishment** (1-15-501..511) [US-WYS5-013, A.1]:
  - The limit is the lesser of 25% of weekly disposable earnings or the excess over 30x the federal minimum hourly wage. This is the same as CCPA.
  - The writ lasts 90 days.
  - Only one writ is satisfied at a time, in order of service.
  - No discharge for garnishment.
  - "Earnings" include pension and deferred compensation and exclude per diem.
- **Child support IWO** (20-6-201..222) [US-WYS5-014, A.1]:
  - Start no later than the first pay period after service.
  - Remit to the SDU within 7 days of payday, with name, SSN and date.
  - **The employer fee is USD 5 per payment.** It is taken from the remaining income, and support plus fee stay within 15 U.S.C. 1673.
  - The IWO has priority over any other state-law process (20-6-219), and over a continuing garnishment, which it tolls (1-15-504(c)).
  - Notify the clerk within 30 days of a health-coverage lapse.
  - The federal uniform IWO form is accepted.
- **State tax levies:** none. There is no income tax, and no wage levy power was located.
- Confidence: high.

## 10. collective_agreements (prevailing wage)
- **Statute:** the Wyoming Prevailing Wage Act, 27-4-401 to -413. The "construction" threshold is USD 100,000. Work not exceeding USD 25,000 is exempt [US-WY-P5-1-006, reused].
- **Records:** contractors and subcontractors keep a record of workers' names, occupations and actual wages paid. It is open to the director and the awarding body (27-4-410) [Title 27 text, US-WY-P5-1-006 family]. There is no certified-payroll *submission* form in the statute.
- **Enforcement:** DWS Labor Standards runs prevailing-wage surveys and the resident-contractor certificates [US-WYS5-018].
- Right-to-work state (27-7-108 ff., not read in detail). No sector CBA minima.
- Confidence: medium. The current survey rates were not fetched (out of payroll-engine scope).

## 11. indexation
- **Minimum wage:** not indexed.
- **SUI wage base:** indexed annually to 55% of the statewide average annual wage, rounded down to USD 100. The wage is computed from wages in the calendar year preceding June 1 [US-WYS5-003]. DWS publishes it on the wage-base page [US-WYS5-008].
- **Derivation (G-DERIVE), done in Python:**
  - The 2026 base of 33,800 implies an average annual wage in [61,454.55, 61,636.36).
  - The DWS memo states 8% of the wage, "for 2025", = USD 4,900, rounded down to USD 50 under 27-3-306(d)(i). That implies a wage in [61,250, 61,875).
  - The two intervals overlap, so the two DWS figures agree.
  - The wage behind the 2025 base of 32,400, in [58,909, 59,091), would give 4,700. So the memo's "2025" wage (the benefit year from July 2025) is the one that sets the **2026** base.
  - The exact average annual wage is not published on the pages read, so the derivation is consistent but not exact (WY-OQ-2).
  - 2027 base 34,900: wage in [63,454.55, 63,636.36). Not cross-checked.
- **Adjustment factors:** computed annually by DWS (27-3-505). The values are unpublished (WY-OQ-1).
- **Maximum weekly benefit:** 55% of the statewide weekly wage (27-3-303(a)). It matters for benefits, not payroll.

## 12. data_protection
- **No SSN-truncation rule for pay statements.** Keyword scans of Titles 27 and 40 found none [US-WYS5-015].
- **Breach notification** (40-12-501/502): notify affected Wyoming residents when personal identifying information is misused or likely to be. That means name + SSN or other listed elements, unless redacted to 5 digits or fewer [US-WYS5-015, A.1].
- **Retention:** payroll records 2 years (27-4-203).
- UI records are confidential (27-3-607, not read).
- Confidence: medium-high.

## 13. live_legal_change (2026-01-01 to 2026-11-02, and 2027)
- **Sweep:** the LSO bill list for the 2026 budget session, from the API (335 bills, 107 chaptered) [US-WYS5-017, A.3].
- **Enacted:** no act amends minimum wage, wage payment, UI contributions or the wage base formula, and no act creates a payroll tax.
- **HB0006** (UI coverage-period and reporting; would reduce maximum benefits): **failed introduction 2026-02-09 (29-33)**. Not enacted. It would have operated at benefits, not payroll.
- **2025 SF0176** (employer contribution floor/cap): **died in committee 2025-03-03**. Not enacted.
- **SF0041 Portable benefit accounts** (chapter 63): enacted, and its text is in the Title 27 compiled 2026-05-08. Hiring parties may contribute to independent contractors' accounts, and a contribution is not a classification factor (27-3-104, 27-14-102). Level: worker classification. Not employee payroll.
- **Next year (2027):** wage base USD 34,900 from 2027-01-01 [US-WYS5-008]. The 2027 rate notices are due by 2026-12-31 (DWS rates page). Nothing else is enacted for 2027.
- The 2027 general session (Jan 2027) is not yet searchable.
- Confidence: high for enacted law.

## Special populations (US-OWN-005, state round)

| Population | Wyoming rule | register_id |
|---|---|---|
| Domestic / household | Excluded from the minimum-wage article (FLSA still applies). UI-covered at USD 1,000 cash wages in a quarter. No income tax. | US-WYS5-001; US-WYS5-004 |
| Agricultural | Excluded from the minimum-wage article. Exempt from paydays and the pay-statement rule (27-4-101(c)). UI-covered at USD 20,000 in a quarter or 10+ workers in 20 weeks. H-2A exempt from UI. | US-WYS5-001; US-WYS5-002; US-WYS5-004 |
| Minors | Hours limits under 16. Proof of age on file. No work under 14 except farm, domestic or yard. Youth wage USD 4.25 (under 20, first 90 days). UI excludes an under-21 child working for a parent. | US-WYS5-005; US-WYS5-001; US-WYS5-004 |
| Tipped | Cash wage USD 2.13 with make-up to 5.15 (FLSA 7.25 governs covered employers). Tips are the employee's property. Monthly tip record. | US-WYS5-001; US-WYS5-002 |
| Clergy / religious | UI excludes ministers, religious-order members and church organisations. No income tax. | US-WYS5-004 |
| Students | UI excludes students employed by their school (and spouses in aid programmes) and certified co-op students. | US-WYS5-004 |
| Nonresident aliens | No state income tax. UI follows FUTA (H-2A exempt). No state rule beyond federal. | US-WY-P5-1-001; US-WYS5-004 |
| Statutory employees / contractors | UI excludes under-18 newspaper carriers, real-estate licensees, leased owner-operators and booth-rent stylists. LLC members are excluded unless the LLC elects. Portable benefit accounts (SF0041). | US-WYS5-004; US-WYS5-017 |
| Government employees | Excluded from the state minimum-wage article. State/county overtime under 27-5-101. UI-covered (elected officials, legislature, judiciary and guard excluded). WC on a July-June rate year. | US-WYS5-001; US-WYS5-005; US-WYS5-004; US-WYS5-007 |

## MULTI hand-offs
- **SUI wage-base credit for other-state wages:** yes, 27-3-102(a)(xviii)(A) [US-WYS5-003].
- **PFML/SDI for multistate workers:** not applicable, as there is no programme [US-WY-P5-1-004].
- **Paid-sick-leave coverage of partial-state workers:** not applicable, as there is no statute.
- **Pay-statement reach:** work physically performed in Wyoming (DWS enforcement scope) [US-WYS5-018]. No statutory extraterritorial rule.

## ACCESS gaps
- `https://dws.wyo.gov/*`: HTTP 403 to plain curl (no US VPN). Read through wayback `id_` copies dated 2026-02-13 to 2026-10-20.
- `https://newhire-reporting.com/wy-newhire/`: the direct connection failed (HTTP 000), and the wayback copy returned 403. New-hire portal formats and fields beyond the statute were not read.
- `https://web.archive.org/web/2026id_/https://dws.wyo.gov/dws-division/labor-standards/employers/faq/`: 404 (not archived).
- The wayback availability API returned 429 (rate-limited, shared by parallel workers).

## Open questions

Mirrors `unresolved[]` of the facts file (same keys, same wording).

- **wy.meta.register_id_pattern** (blocking): 9 facts rest on active register rows whose ids (US-WY-P5-1-001, US-WY-P5-1-002, US-WY-P5-1-004, US-WY-P5-1-005, US-WY-P5-1-006, US-WY-P5-2-001) do not match the facts-schema register_id pattern ^[A-Z]{2}-[A-Z0-9]{2,12}-[0-9]{3,4}$ (multi-hyphen legacy ids). They are carried in full in _facts_pending_register_id_pattern and are NOT yet consumable facts. What would close it: Orchestrator decision: a PATCH of facts.schema.json loosening the register_id pattern (e.g. ^[A-Z]{2}-[A-Z0-9-]{2,16}-[0-9]{3,4}$), or register alias ids; then run _research/synthesis-B/_work-MN-WY/promote.py to move the pending facts into facts[].
- **wy.ui.rates.2026_values** (blocking): 2026 minimum/maximum assigned rates, industry new-employer rates and adjustment-factor values not published on pages read. What would close it: DWS January 2026 UI rate release or WYUI rate notice (Chrome pass) / DWS helpline 307-235-3217.
- **wy.ui.wage_base.average_wage** (non-blocking): Exact statewide average annual wage behind 2026/2027 bases not published (interval check only). What would close it: DWS Research & Planning average annual wage publication.
- **wy.report.file_formats** (non-blocking): WYUI wage file format and new-hire electronic format not read. What would close it: WYUI employer user guide and newhire-reporting.com/wy-newhire specs.
- **wy.ui.noncash_valuation** (non-blocking): Non-cash remuneration valuation rule (commission rule) not read. What would close it: Wyoming UI Commission rules (SOS rules database).
