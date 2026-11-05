# Stage 5 - MI (Michigan) - 13-domain findings

Worker: compliance-source-hunter, 2026-11-02. Scope: `_prompts/stage5-brief.md`, JUR = MI. Mandate block US-MQ-42 (answered at seal attempt 4) reused, not re-researched.
Budget: declared 60 fetches / 2 h; working ceiling 45. Used about 33 fetches and 8 searches, roughly 15 min of wall clock. Acquisition stopped at the 75% mark.
New register shard: `00-official-sources/_register-shards/S5-MI.csv` (rows US-MIS5-001 .. 026; 25 active, 1 partial). New files: `00-official-sources/ccg-sources/MI/` (27 files, 8.5 MB total, largest 1.5 MB).
Reused active rows (not re-fetched): US-MIPIT-001, US-MIP51-001..006, US-MIP51-008, US-MIP52-001/-002/-004/-005/-011/-012, US-MIR3-001..003, US-MIL-001/-002, US-MIP9V-001, US-MIP9W-001/-002, US-MIP9L-001, US-MULTI-010; federal anchors US-FED-011, US-FED-017, US-FEDP52-006.
legislature.mi.gov answered directly today (HTTP 200; the attempt-3 ECONNREFUSED did not recur). Every Act PDF read today carries the banner "Michigan Compiled Laws Complete Through PA 114 of 2026", rendered 2026-10-24/26.

## 1. labour_code
- **Minimum wage** (IWOWA, 2018 PA 337 as amended by 2025 PA 1, MCL 408.934) [US-MIS5-001, A.1]:
  - 12.48 from 2025-02-21;
  - **13.73 from 2026-01-01**;
  - **15.00 from 2027-01-01** (already enacted).
  - From October 2027 the State Treasurer indexes the rate by the 12-month Midwest CPI-U. The new rate is published by 1 November and takes effect 1 January. There is no increase if MI unemployment was 8.5% or more the year before.
  - Coverage: the act applies to employers with 2+ employees and to employees aged 16+. It does not apply to FLSA-covered employers unless the federal rate is lower (408.940(1)).
  - Statute compiled through PA 114 of 2026: no 2026 amendment.
- **Local minimum wage: none.** The Local Government Labor Regulatory Limitation Act (2015 PA 105, MCL 123.1385/.1386/.1388/.1389) preempts:
  - local minimum wages,
  - local prevailing-wage rates (except state projects),
  - local leave mandates,
  - local scheduling mandates.
  [US-MIS5-014, A.1]
- **Overtime** (MCL 408.934a) [US-MIS5-002, A.1]:
  - 1.5x the regular rate over 40 hours in a workweek. Public hospitals may use an 8/80 schedule by written agreement.
  - Exemptions: executive/administrative/professional (EAP), seasonal amusement (7 months or less), agriculture.
  - Comp time is allowed in lieu of overtime pay: 1.5 hours per overtime hour, cap 240 hours, cashed out within 30 days of a request and paid at termination. Comp time earned or paid must appear on the earnings statement.
- **Training, minor and tipped wages** [US-MIS5-003, A.1]:
  - Training wage: 4.25 for the first 90 days, for new employees under 20.
  - Under 18: 85% of the minimum. 2026: 13.73 x 0.85 = **11.6705** (derived; the statute gives no rounding rule).
  - Tipped: 40% of the minimum from 2026-01-01, so 13.73 x 0.40 = **5.492** (derived). The percentage rises to 42% (2027), 44% (2028), 46% (2029), 48% (2030) and 50% (2031). 2027 tipped = 15.00 x 0.42 = 6.30.
  - Conditions for the tipped wage: tips cover the gap; tips declared for FICA; tips kept by the employee (pooling only within the chain of service); written notice and written consent at hire.
- **Pay frequency** (Act 390 of 1978, MCL 408.472) [US-MIS5-005, A.1]:
  - Default semi-monthly: days 1-15 paid by the 1st of the next month; days 16-end paid by the 15th.
  - Weekly or biweekly payrolls comply if payday falls no later than 14 days after the period ends.
  - Monthly payrolls comply if paid within 15 days.
  - December overtime may go on the next regular payday.
  - Employer = 1+ employees.
- **Method of payment** (MCL 408.476) [US-MIS5-006, A.1]:
  - Permitted methods: cash, check, direct deposit, payroll debit card.
  - Direct deposit and paycard each need full, free, written consent. The exception is a mandated DD-or-paycard election: the employer gives an election form, and if the form is not returned within 30 days the employee is presumed to accept the paycard (this never moves an existing DD employee to a card), with fee disclosures.
  - A change of method takes effect within 1 pay period.
  - Paycard: 1 free withdrawal per pay period, 21 days' notice of fee changes, free balance inquiries, no credit link.
  - The employer may not pass payment-method costs to the employee.
- Confidence: high (A.1 read in full).

## 2. income_tax
- **Rate and method** (Guide 446 Rev. 02-26) [US-MIPIT-001, A.2]: flat 4.25% of compensation minus personal exemptions of 5,900 x the number on the MI-W4 / pay periods. MCL 206.703 [US-MIP52-001, A.1].
  - Per-period exemption (derived): weekly 113.46, biweekly 226.92, semi-monthly 245.83, monthly 491.67.
  - Oracle seed: biweekly 2,000.00 with 1 exemption gives (2,000 - 226.92) x 0.0425 = **75.36**. The official oracle is the Treasury withholding calculator at www.michigan.gov/taxes/business-taxes/withholding/tax-calculator [US-MIS5-021; US-MIPIT-001].
- **Supplemental**: bonuses and payments made separately from regular payroll are withheld at 4.25% with no exemption adjustment [US-MIPIT-001].
- **Rounding**: no rule in statute or guide [US-MIP52-001].
- **Certificate**: MI-W4 (Rev. 12-20), and the federal W-4 may not substitute [US-MIS5-019, A.2].
  - Line 6 = exemptions; line 7 = additional amount; lines 8a/8b = exempt.
  - No certificate: withhold on zero exemptions.
  - Copies go to Treasury when 10+ exemptions or exempt status is claimed.
  - Nonresidency proof is an employer-designed certificate or letter.
- **Taxable base and conformity**: MI taxable income starts from federal AGI (MCL 206.30(1)) [US-MIS5-015, A.1].
  - The personal exemption is CPI-indexed (base 3,700 x CPI ratio + 600, rounded to the nearest 100) [US-MIS5-015].
  - The 2027 exemption is not yet published (open).
- **Tips and overtime deduction (LIVE, enacted)**: 2025 PA 24 (signed 2025-10-07) added MCL 206.30(1)(ee) [US-MIS5-015, US-MIS5-017 A.2].
  - Tax years 2026-2028: deduct federally allowed qualified tips (IRC 224) and qualified overtime (IRC 225). Nonresidents deduct only MI-sourced amounts.
  - **Level = assessment (MI-1040).** No change to employer withholding: none appears in the Treasury notice of 2026-01-06, in Guide 446 Rev. 02-26 or in the statute.
  - A tier-B search summary says employers must stop MI withholding on tips. It is **not supported** and must not be modelled.
- **Reciprocity**: IL, IN, KY, MN, OH, WI, for state tax only, not city tax [US-MULTI-010, US-MIP51-001].
- **Residents and nonresidents**:
  - MI employers withhold from nonresidents for MI work unless a reciprocity agreement covers them.
  - MI residents temporarily working in another state are still withheld for MI.
  - Out-of-state employers register and withhold for all employees working in MI [US-MIPIT-001].
- **Local income taxes**: 24 cities levy them [US-MIR3-001, US-MIP52-002].
  - Detroit (Treasury-administered) [US-MIR3-002, US-MIP51-002]:
    - Rates: 2.4% residents (wherever they work), 1.2% nonresidents whose predominant place of work is Detroit.
    - Exemption 600/year. Derived per period: weekly 11.54, biweekly 23.08, semi-monthly 25.00, monthly 50.00, daily 1.64 (600/365), which matches the guide figures.
    - Certificate DW-4 (Form 5527); without one, withhold at the resident rate with no exemption.
    - Returns: monthly Form 5323, due the 15th; annual Form 5321, due 2027-02-28 for TY2026.
    - Oracle seed: resident biweekly 2,000 gives (2,000 - 23.08) x 0.024 = 47.45.
  - The other 23 cities self-administer on separate city returns (T4). Uniform ordinance: 1% residents / 0.5% nonresidents, unless a city resolves a lower rate (MCL 141.611) [US-MIR3-003].
  - **The rates, forms and due dates of the 23 cities were not read in this pass** (annex data; see Open questions).
- Confidence: state high; Detroit high; 23 cities: existence only.

## 3. social_security
- **SUI (UIA)**:
  - Taxable wage limit (MCL 421.44(4)) [US-MIS5-010, A.1]: 9,500, reduced to 9,000 for the year for non-delinquent employers when the fund is at 2.5 billion or more on 30 June of the prior year and projected to stay there.
  - **2026 = 9,000** for qualified employers and 9,500 for delinquent ones [US-MIP51-004, US-MIS5-025].
  - G-DERIVE: the FAQ's average 14 saving per employee at 2.7% reconciles: 0.027 x 500 = 13.50 [US-MIS5-025].
  - Not CPI-indexed; the base is a fund-balance switch.
  - New employer 2.7% in years 1-2 (MCL 421.19) [US-MIS5-012, A.1]. Construction employers pay the average construction rate (5.0% for 2026).
  - 2026 rate range 0.06%-12.2% (15.2% with penalty) [US-MIP51-003, US-MIP9W-001].
  - **No employee contribution** (only AK/NJ/PA have one) [US-FEDP52-006].
  - UI wage definition: FICA-reported tips included. Excluded: retirement/health plan payments, employer-paid employee FICA, 401(a) trust payments, SUB pay. Wages paid in other states count toward the limit [US-MIS5-010].
- **SDI/TDI/PFML/LTC: none** [US-MIP51-008]. ESTA is employer-paid leave, not a premium.
- **Other levies**: no transit, workforce or administrative surcharge (absence read at A.2 on both the revenue and UI sides) [US-MIP9V-001, US-MIP9W-001/-002].
- Confidence: high.

## 4. payslip_statute
- **Statement at the time of payment** (MCL 408.479(2)) [US-MIS5-009, US-MIP51-005]: hours worked, gross wages, pay-period identification, a separate itemisation of deductions (piece-rate hand harvesters: units).
  - Hours may be omitted for EAP-exempt staff, elected officials and political appointees.
  - IWOWA 408.937 repeats the hours/wages/deductions duty each pay period.
- **Employer record** [US-MIS5-009]: name, address, birth date, occupation, basic rate, hours and wages per period, deductions, fringe benefits. Kept 3 years.
- Comp-time earned or paid must appear on the statement [US-MIS5-002].
- **Electronic delivery**: the statute is silent, and no consent rule was located.
- **Language**: none for the payslip [US-MIL-002]. The ESTA notice and poster must be in English and Spanish, plus any language that is the first language of 10%+ of the workforce if LEO has translated it [US-MIL-001, US-MIS5-004].
- SSN: at most 4 digits on the statement (see domain 12).
- Confidence: high on content; medium on e-delivery (silence).

## 5. reporting_instruments
- **Withholding returns** (combined SUW return; Treasury assigns frequency yearly) [US-MIS5-018, US-MIS5-021, A.2]:
  - Form 5080 monthly/quarterly, due the 20th after the period (20 Apr / 20 Jul / 20 Oct / 20 Jan).
  - Form 5081 annual reconciliation for 2026, due **2027-02-28** (W-2/1099 count, MI tax withheld, payments). Every filer files it.
  - **Accelerated EFT**: prior-year withholding liability of 480,000 or more means paying by EFT on the federal deposit day (Treasury notifies in April; the change applies from July).
  - Late penalty: 5%.
  - Channel: MTO (online form / file upload), approved software, or paper.
- **State W-2** [US-MIPIT-001]:
  - Due 31 January, the federal date.
  - 10+ income record forms: upload through MTO in EFW2 (SSA) / Pub 1220 magnetic-media format. Fewer than 10: MTO upload, physical media (Form 447) or paper.
  - W-2s are not shared through CF/SF (CF/SF covers 1099s only), so W-2 state copies always go directly to Treasury.
  - Employer that ceases business: W-2s to Treasury within 30 days.
- **Quarterly UI wage/tax report (MiUI)**:
  - Due 25 Jan / 25 Apr / 25 Jul / 25 Oct, moved to the next business day when needed [US-MIS5-020, A.2].
  - MiUI (live 2026-02-23) accepts four file formats [US-MIS5-022, A.2]:
    - Delimited CSV (2026 spec v3, 2026-04-08);
    - ICESA (v2);
    - EFW2 (v2, 2026-04-03; 512-byte RE/RS records, UIA profile);
    - XML (v1, 2026-02-23).
  - The legacy MiWAM format is no longer accepted. Specs are on disk.
- **New-hire reporting**: report to the Michigan New Hires Operation Center (Office of Child Support), (800) 524-9846, online at mi-newhire.com; Form 3281 [US-MIS5-026 A.3 partial; US-MIPIT-001 Guide 446 p.5; US-MIS5-018 forms list].
  - Deadline: the federal 20 days applies [US-FED-017].
  - **The Michigan statute and penalty were not located** (open).
- **Registration**: Treasury e-Registration (MTO). The Treasury account number is usually the FEIN. A new FEIN is needed on acquisition [US-MIPIT-001].
- **Discontinuance**: Form 163 [US-MIS5-018].
- **Authorisation**: Form 151 [US-MIP52-004/-011]; UIA 1488 [US-MIP52-005].
- Confidence: high, except the new-hire statute.

## 6. leave
- **ESTA** (2018 PA 338 as amended by 2025 PA 2) [US-MIS5-004, A.1]:
  - Covers every employer (1+ employees).
  - Accrual: 1 hour per 30 hours worked.
  - Small business (10 or fewer): use and carry-over cap 40 hours, or frontload 40; obligations start 2025-10-01. Others: cap 72, or frontload 72. Part-time staff can be frontloaded proportionally with written notice of expected hours.
  - FLSA-exempt employees are assumed to work 40 h/week.
  - Pay rate: the greater of the normal/base rate or the minimum wage, excluding overtime, bonuses, commissions and tips.
  - Increments: 1 hour. New hires can be made to wait up to 120 days.
  - **No payout at separation.** Rehire within 2 months restores the balance.
  - An equivalent PTO policy complies.
  - Documentation may be required for absences over 3 days (employer pays the cost).
  - Records kept 3 years.
- **PFML**: none [US-MIP51-008]. Local leave mandates are preempted [US-MIS5-014].
- Confidence: high.

## 7. termination
- **Final pay** (MCL 408.475) [US-MIS5-007, A.1]:
  - Discharge: immediately, "as soon as the amount can with due diligence be determined".
  - Voluntary quit: as soon as the amount can with due diligence be determined (hand harvesters: within 3 days).
  - Contract workers: estimated pay, with the final payment at contract end.
- **Accrued vacation**: payout follows the written contract or policy (fringe benefits, MCL 408.471(e)/408.473). There is no statutory payout. Withholding a benefit due at termination needs written consent (408.474).
- **ESTA**: no payout [US-MIS5-004].
- **Comp time**: paid at termination [US-MIS5-002].
- **Deceased employee**: pay a written designee or next-of-kin in statutory order [US-MIS5-007].
- UI separation notice and state WARN: not researched (no payroll calculation impact; open, low priority).
- Confidence: high.

## 8. benefits_in_kind
- MI taxable income starts from federal AGI with rolling conformity [US-MIS5-015].
- Guide 446: "Michigan reporting and withholding on fringe benefits follows federal guidelines (Pub. 15)", including 401(k) deferrals and cafeteria plans [US-MIPIT-001].
- No state departure was located for 401(k), sec. 125, HSA, transit or group-term life.
- UI wages exclude retirement and health plan payments and employer-paid employee FICA; non-cash pay is valued by UIA rule [US-MIS5-010].
- Confidence: medium-high (conformity by construction; no item-by-item Treasury list read).

## 9. deductions_garnishments
- **Wage deductions** (MCL 408.477) [US-MIS5-008, A.1]:
  - Written consent for each deduction not required by law or a CBA.
  - Deductions for the employer's benefit: consent for each pay, and gross may not fall below the state minimum.
  - Overpayment recovery without consent: within 6 months, clerical error, written notice 1 period ahead, max 15% of gross, never below the minimum wage.
- **Child support** [US-MIS5-016, A.1]: the total withheld under all support orders is capped at **50% of disposable earnings** (MCL 552.608). This is stricter than the CCPA 55/60/65% tiers [US-FED-011].
- Payments go to MiSDU, the single remittance point [US-MIS5-024].
- Employer IWO processing fee: **not located** (open).
- Creditor garnishment: CCPA 25% applies [US-FED-011]. The MCL 600.4012 periodic-garnishment procedure was not read (open, low).
- State tax levy: not researched (open, low).
- Confidence: medium.

## 10. collective_agreements (prevailing wage)
- Prevailing Wages on State Projects (2023 PA 10, effective 2024-02-13; 2024 PA 110 from 2025-04-02 adds energy facilities of 2 MW or more and contractor registration) [US-MIP51-006, US-MIS5-023, A.1]:
  - **No dollar threshold.**
  - Contractor and subcontractor state-project registration.
  - **Certified payroll** within 10 days after each pay period, to the contracting agent and then to the LEO database. Fields: classification, skill level, gross wages, daily hours, start/end times, hourly, overtime and fringe rates. No SSN.
  - Records kept 3 years. Fine up to 5,000 per violation.
- Local prevailing-wage ordinances are preempted (except state projects) [US-MIS5-014].
- Confidence: high.

## 11. indexation
| Item | Mechanism | Publication | Register |
|---|---|---|---|
| Minimum wage | Fixed to 15.00 (2027-01-01); then Midwest CPI-U every October from 2027, unless unemployment is 8.5% or more | State Treasurer, by 1 November | US-MIS5-001 |
| Tipped / minor wage | % of minimum (tipped schedule to 50% in 2031; minor 85%) | Statute | US-MIS5-003 |
| PIT personal exemption | 3,700 x US CPI (state FY) ratio to FY2010-11, + 600, rounded to the nearest 100 | Guide 446 (annual) | US-MIS5-015, US-MIPIT-001 |
| PIT rate | 4.25% (statutory; no 2026 change) | Guide 446 | US-MIPIT-001 |
| SUI wage base | Not indexed: 9,500 / 9,000 switch on the fund balance at 30 June | UIA Employer Advisor / FAQ | US-MIS5-010, US-MIS5-025 |
| Detroit exemption | 600 fixed | Form 5469 | US-MIR3-002 |
- G-DERIVE lines (Bash): 13.73 x 0.40 = 5.492; 13.73 x 0.85 = 11.6705; 15.00 x 0.42 = 6.30; 0.027 x (9,500 - 9,000) = 13.50; 5,900/26 = 226.92; 600/26 = 23.08 (matches 5469). The 2026 exemption of 5,900 could not be re-derived because the CPI inputs were not fetched.

## 12. data_protection
- **SSN Privacy Act** (2004 PA 454, MCL 445.83/445.84) [US-MIS5-013, A.1]:
  - The following are prohibited for more than 4 sequential SSN digits: public display, use as an account number, printing on cards, unsecured transmission, and visibility through envelopes.
  - Uses required by law (W-2, filings) are exempt.
  - An employer holding SSNs must publish an SSN privacy policy (handbook or manual) covering confidentiality, access limits, disposal and penalties.
  - Payslip effect: show the last 4 digits at most.
- **ESTA**: employee health and domestic-violence information is confidential [US-MIS5-004].
- **Prevailing-wage database**: excludes SSN and home address [US-MIS5-023].
- Confidence: high.

## 13. live_legal_change (2026-01-01 to 2026-11-02, plus enacted 2027)
- 2026-01-01: minimum wage 13.73; tipped 40% [US-MIS5-001/-003].
- 2027-01-01 (enacted): minimum wage 15.00; tipped 42% [US-MIS5-001/-003].
- 2026-01-01 to 2028-12-31: state tips and overtime deduction.
  - Instrument: 2025 PA 24 / MCL 206.30(1)(ee).
  - Status: **enacted, in force**. Level: **assessment**. No withholding change [US-MIS5-015, US-MIS5-017].
  - MCL 206.30 was later amended again by 2026 PA 39 (immediate effect 2026-07-22). That amendment's content was not isolated (open).
- 2026-02-23: MiUI replaced MiWAM for the tax side; new wage-file specs; the MiWAM file format is retired [US-MIP51-004, US-MIS5-022].
  - UIA waived penalties for Q1 2026 reports filed by 2026-05-31. This rests on a tier-B lead only (SBAM/MICPA), so it is not registered.
- 2025-10-01: ESTA small-business obligations began [US-MIS5-004].
- 2025-04-02: prevailing wage extended to energy facilities, plus contractor registration [US-MIS5-023].
- IWOWA, ESTA and the Payment of Wages Act read today are compiled through PA 114 of 2026 with no 2026 amendment.
- **Not yet published**: the 2027 SUI wage base (depends on the fund on 2026-06-30) and the 2027 personal exemption.

## Special populations (US-OWN-005, state round)
| Population | MI rule | register_id |
|---|---|---|
| Domestic / household workers | Minimum wage and overtime apply to companionship and non-live-in childcare workers (except casual under-18 sitters working 20 h/week or less), 408.940(2). UI excludes private-home domestic service unless the employer meets the MES Act sec. 41(6) threshold (threshold amount not read). | US-MIS5-001, US-MIS5-011 |
| Agricultural | State overtime exempt (408.934a(4)(e)). Harvest piece-rate employers outside the act until a piece scale is set (408.940(4)). Hand harvesters paid within 2 days after the work week; final pay within 3 days; statement shows units. UI excludes agricultural labor unless the employer meets sec. 41(5); H-2A excluded. | US-MIS5-002, US-MIS5-001, US-MIS5-005, US-MIS5-007, US-MIS5-009, US-MIS5-011 |
| Minors | 85% of the minimum under 18; 4.25 training wage for the first 90 days under 20; minimum wage act covers 16+ (and minors under the youth act sec. 15(1)). ESTA excludes youth-employment-standards minors. UI excludes children under 18 working for a parent, newspaper carriers under 18, and some minor students. Hours limits (1978 PA 90) not read. | US-MIS5-003, US-MIS5-001, US-MIS5-004, US-MIS5-011 |
| Tipped employees | 40% of the minimum (2026), with written notice/consent conditions; tips remain the employee's; service-charge notice; UI wages include reported tips; state tips deduction at assessment 2026-2028. | US-MIS5-003, US-MIS5-010, US-MIS5-017 |
| Clergy / religious | State withholding follows the federal duty (no federal withholding duty, so no MI duty); nonprofit and religious employers must withhold where federal withholding applies. UI: church employment excluded for MES Act sec. 42(8)-(10) purposes (421.43(o)(i)). | US-MIPIT-001, US-MIS5-011 |
| Students | UI excludes students employed by their own school (30 h/week or less), certified co-op students under 22, and college students in an accredited curriculum. MI-W4 copies not sent for part-time/student employees under the exemption allowance. | US-MIS5-011, US-MIPIT-001 |
| Nonresident aliens | No state rule beyond federal found: MI withholding follows the federal duty (Guide 446 "who must withhold"); H-2A agricultural aliens excluded from UI. | US-MIPIT-001, US-MIS5-011 |
| Statutory employees | Guide 446 defines employer/employee by IRS Pub. 15. UI excludes commission-only real estate, investment and insurance agents and direct sellers. | US-MIPIT-001, US-MIS5-011 |
| Government employees | State and political subdivisions are employers under IWOWA (with 7k fire/police overtime rules) and under Act 390. Federal employees are excluded from ESTA. UI excludes service for another state. Public-safety pension rules (assessment) in Guide 446. | US-MIS5-001, US-MIS5-002, US-MIS5-004, US-MIS5-011 |

## ACCESS gaps
- https://www.mi-newhire.com/ : HTTP 200, but the body is a JavaScript single-page app with no readable text, so it is unreadable with curl (browser pass needed).
- https://www.michigan.gov/leo/bureaus-agencies/ber/wage-and-hour/minimum-wage : HTTP 404 (guessed URL). The figure rests on A.1 statute text; no second-authority page was obtained.
- (Not a gap) legislature.mi.gov was reachable; the earlier ECONNREFUSED did not recur.

## Open questions (what_would_close_it)
1. **Rates, forms and due dates of the 23 self-administered city income taxes** (Albion ... Walker). Close with each city's income-tax withholding instructions for 2026 (city income-tax department pages or employer withholding guides). This is naturally parallel: 23 independent lookups that can be fanned out across workers.
2. **Michigan new-hire statute and state penalty / fields.** Close with the Michigan statute that establishes the New Hires Operation Center reporting duty, or the MDHHS/OCS employer new-hire guide (DHS-Pub-95/96 on michigan.gov were seen as leads, not read). The federal 20-day rule applies meanwhile [US-FED-017].
3. **Employer fee for processing support IWOs (if any) and periodic-garnishment procedure.** Close with the Support and Parenting Time Enforcement Act income-withholding sections (MCL 552.601 et seq.) and MCL 600.4012 / MCR 3.101 on legislature.mi.gov / courts.michigan.gov.
4. **2026 PA 39 (imd. eff. 2026-07-22) content in MCL 206.30.** Close with the 2026 PA 39 enrolled bill on legislature.mi.gov. Check whether it touches subdivision (ee) or the personal exemption.
5. **2027 SUI taxable wage base (9,000 vs 9,500) and 2027 personal exemption.** Close with the UIA Employer Advisor / Form 6354 notices for 2027 (usually Dec-Feb) and the Guide 446 TY2027 edition.
6. **Payslip electronic delivery.** Act 390 is silent and no LEO guidance was read. Close with a LEO Wage and Hour FAQ on electronic pay statements, if one exists.
7. **MES Act sec. 41(5)/(6) thresholds for agricultural and domestic employers.** Close with MCL 421.41 on legislature.mi.gov (1 fetch).
8. **Register hygiene for the synthesis (no action taken here; this worker does not edit the main register):**
   - US-MIWPA-001 (MANUAL) is now covered by A.1 US-MIS5-009 / US-MIP51-005.
   - US-MIPOA-001 (MANUAL) is covered by US-MIP52-004/-005/-011.
   - US-MILOC-002 (gated) is the same Form 5469 read through Wayback in US-MIP51-002 / US-MIR3-002.
   - US-MIP7-001 (MANUAL) is superseded in substance by US-MIR3-002. US-MIP7-002 stays a gap (open question 1).

## Confidence
Overall MI about 88%. State layer 90-95% (A.1 statute text and A.2 Treasury/UIA pages for every number). The local layer (23 cities) is the main residual; new-hire and garnishment detail are secondary residuals.
