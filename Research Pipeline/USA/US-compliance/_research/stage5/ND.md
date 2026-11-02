# Stage 5 - ND (North Dakota) - 13-domain findings

Worker: compliance-source-hunter, 2026-11-02. Scope: `_prompts/stage5-brief.md`, JUR = ND. The mandate block US-MQ-48 (answered at seal attempt 3) is reused, not researched again.

**Budget.** I declared 60 fetches and 2 hours. I used about 34 fetches (30 curl, 4 web searches) in roughly 50 minutes.

**Access.** The VPN was off (the exit IP was in Brazil). Even so, ndlegis.gov, tax.nd.gov, jobsnd.com and hhs.nd.gov all answered plain curl with HTTP 200, so every file below is a direct fetch, not a Wayback copy.

**Register shard.** `00-official-sources/_register-shards/S5-ND.csv` holds rows US-NDS5-001 to US-NDS5-019. All 19 are `active`: 16 are tier A.1/A.2 and 3 are tier A.3 (HHS child-support FAQs, used for mechanics only).

**Files.** New files are in `00-official-sources/ccg-sources/ND/`, about 9.1 MB in total. The largest is the 2026 withholding booklet at 3.8 MB; it is kept because it holds the wage-bracket tables. No file is over 5 MB.

**Reused active rows (not fetched again).**
- US-ND-004 and US-ND-005: the 2026 UI schedules. US-NDS5-012 re-reads the same file live, and the figures are identical.
- US-NDP51-001: withholding guideline, reciprocity section.
- US-NDP51-002: Form 500 POA.
- US-NDP51-003: the DOL table listing no ND prevailing-wage law. This is a WebFetch summary (MEDIUM confidence).
- US-NDP52-001: no local income tax (NDCC 40-05.1-06).
- US-NDP52-002: no PFML (34-01-15.1).
- US-NDP52-003: no employee UI contribution (52-06-31).
- US-MULTI-014: reciprocity.
- US-NDP9L-001 and US-NDP9L-002, US-NDP9V-001: language and levies.

**Correction for the synthesis.** US-ND-003 and the US-MQ-48 part-6 answer say ND has "no pay-statement content provision". That is true of NDCC ch. 34-14 only. **NDAC 46-02-07-02(10) does require a check stub or pay voucher every pay period** [US-NDS5-007]. See section 4.

## 1. labour_code
- **Minimum wage**: 7.25/h from 2009-07-24 (NDCC 34-06-22) [US-NDS5-006, A.1].
  - No indexation exists and no 2027 change is enacted. The commissioner may set a different rate by rule, and none appears in NDAC 46-02-07, which points back to 34-06-22 [US-NDS5-007].
- **Local minimum wages**: none. Political subdivisions may not enact a living-wage mandate above the state minimum (34-06-23) [US-NDS5-006].
- **Overtime** (NDAC 46-02-07-02(4)) [US-NDS5-007]:
  - 1.5x the regular rate over 40 hours per workweek, computed weekly with no averaging across the pay period.
  - Paid holidays, PTO and sick time do not count as hours worked.
  - All jobs held under the same employer are combined.
  - Taxicab drivers: overtime starts over 50 hours.
  - Hospitals and residential care may use an 8/80 period by agreement.
  - Exemptions include EAP (executive, administrative, professional), agriculture, live-in domestic workers, computer professionals paid at least 27.63/h, outside sales, retail commission employees (regular rate above 1.5x the minimum), motor carriers, teachers and highly compensated employees.
- **Other work conditions**:
  - Meal period: 30 minutes for shifts over 5 hours when 2 or more employees are on duty; the employee may waive it (02(5)).
  - Retail employers must give one day of rest in seven (34-06-05.1) [US-NDS5-006].
- **Pay frequency**: at least once each calendar month, on regular paydays designated in advance (34-14-02) [US-NDS5-005].
- **Payment method** (34-14-02):
  - Cash, check, or direct deposit to the financial institution the employee chooses.
  - Stored-value card only at the employee's election when the employer offers it. The card must be FDIC/NCUA insured and funded in advance.
- **Board and lodging credit**: up to 18.00/day, with a written voluntary agreement (02(13)).
- **Uniform purchases**: may not take the wage below the minimum (02(11)) [US-NDS5-007].
- Confidence: high (A.1, full text read).

## 2. income_tax
- **Basis**: NDCC 57-38-59(1) sets withholding as a commissioner percentage of federal withholding. 57-38-59(3) lets the commissioner adopt tables instead, and employers must then follow them. The 2026 booklet is that table route [US-NDS5-004, US-NDS5-001].
  - A search summary claimed that "from 2026-01-01 employers withhold a percentage of federal withholding". That misreads the long-standing 57-38-59(1). The 2026 booklet uses tables, and no 2025/2026 change appears on the OST history or news pages [US-NDS5-018, US-NDS5-019].
- **Certificate**: the federal Form W-4. There is no state certificate. A new hire with no W-4 is treated as single (Section 2) [US-NDS5-001].
- **2026 Annual Percentage Method (2020+ W-4)** [US-NDS5-001]. Annual wage = period wage x periods (52/26/24/12/4/2/260).

| Status | 0% up to | 1.95% from - to | Above top |
|---|---|---|---|
| Married filing jointly | 57,500 | 57,500 - 168,525 | 2,164.99 + 2.50% over 168,525 |
| Head of household | 78,475 | 78,475 - 289,675 | 4,118.40 + 2.50% over 289,675 |
| Single | 57,625 | 57,625 - 258,450 | 3,916.09 + 2.50% over 258,450 |

- **Pre-2020 W-4 (Section 1)** [US-NDS5-001]:
  - Allowance values: weekly 97, biweekly 194, semimonthly 210, monthly 420, quarterly 1,268, semiannual 2,525, annual 5,050, daily 19.
  - The single and married annual tables use the same thresholds as above.
- **G-DERIVE on the booklet** (Python, 2026-11-02):
  - The bracket constants reproduce: (258,450 - 57,625) x 1.95% = 3,916.09; (168,525 - 57,500) x 1.95% = 2,164.99; (289,675 - 78,475) x 1.95% = 4,118.40.
  - The Section 1 example reproduces: weekly 1,800, single, 2 allowances: (1,606 - 1,108) x 1.95% = 9.71, rounded to **10**, as printed.
  - **The Section 2 example does NOT reproduce.** Weekly 1,800, single gives an annual wage of 93,600. The table gives (93,600 - 57,625) x 1.95% = 701.51, and 701.51 / 52 = 13.49, rounded to **13**. The booklet prints 734.00 annual and **14**.
  - 734 would need a threshold of about 55,960, so the example looks carried over from an earlier year.
  - The weekly wage-bracket table (midpoint basis) shows 14 for the 1,800-1,825 line, so the exact formula and the bracket table differ by 1.00 at this wage.
  - Oracle consequence: use the formula and table, not this printed example, for 9b. See Open questions.
- **Rounding**: the period amount is rounded to the nearest whole dollar, and an amount under 1.00 need not be withheld [US-NDS5-001].
- **Supplemental wages** (separately paid or identified) [US-NDS5-001]:
  - Option 1: flat **1.50%**.
  - Option 2: aggregate with regular wages.
  - The booklet's supplemental examples ($1,000 -> $15; aggregate $32 - $12 = $20) are consistent.
- **Who must withhold** [US-NDS5-002, US-NDS5-003]:
  - Services performed in ND and wages subject to federal withholding.
  - ND residents working outside ND. Exception: an ND-based employer that is required to withhold the other state's tax.
  - Wages are IRC 3401 wages.
- **Exempt from ND withholding** [US-NDS5-002]:
  - Farmer or rancher agricultural wages.
  - Enrolled tribal members who live and work on a reservation.
  - MN and MT residents who give Form NDW-R (renewed by Feb 28; a MN resident must return home at least monthly).
  - Military spouses with Form NDW-M (renewed by Jan 31).
  - Interstate carrier nonresidents.
  - Military pay deductible under 57-38-30.3(2)(g), unless the employee asks for withholding.
- **Nonresident mobile workforce exclusion** (57-38-59.3) [US-NDS5-004]. It applies when all of these hold:
  - the nonresident is present 20 days or fewer;
  - the nonresident has no other ND income;
  - the home state has a reciprocal exclusion or no income tax.
  - It does not apply to athletes, entertainers, persons of prominence, construction workers or key employees.
- **Nonresident aliens** [US-NDS5-002]:
  - A separate W-4 marked "North Dakota only - nonresident alien", status Single, Exempt not allowed.
  - A treaty exemption is not recognised unless the treaty covers states.
- **Severance paid to a nonresident**: taxable in ND by the ratio of past ND service [US-NDS5-002].
- **Local income taxes**: none [US-NDP52-001].
- **Reciprocity**: MN and MT [US-MULTI-014, US-NDP51-001].
- Confidence: high (A.2 booklet read in full, A.1 statute), except the booklet-example defect.

## 3. social_security
- **SUI 2026** [US-NDS5-012, US-ND-004]:
  - Taxable wage base **46,600**.
  - New-employer rate: non-construction 1.00% (positive balance) / 6.07% (negative balance); construction 9.67%.
  - Experience range: positive schedule 0.07%-1.10%; negative schedule 6.07%-9.67%.
- **Employee contribution**: none. Contributions may not be deducted from wages (52-04-01) [US-NDS5-009, US-NDP52-003].
- **Wage-base rule**: 70% of the statewide average annual wage, rounded to the nearest 100, fixed by Oct 1 for the next year, and never below FUTA (52-04-03(3)-(4)) [US-NDS5-009].
- **Coverage**:
  - Corporate officers and certain LLC managers are covered. Owners with 25% or more may elect exclusion in January or within 60 days of formation.
  - Domestic workers are covered at 1,000/quarter.
  - Agricultural workers are covered at 10+ workers in 20 weeks or 20,000 cash wages/quarter [US-NDS5-011, US-NDS5-010].
- **SDI/TDI/PFML**: none. 34-01-15.1 bars local mandates [US-NDP52-002].
- **Other levies**: none on the revenue list [US-NDP9V-001].
- **Penalties**: interest 1.5%/month; late report penalty 5%/month, minimum 25.00 [US-NDS5-009].
- Confidence: high.

## 4. payslip_statute
- **NDAC 46-02-07-02(10)**: every employer must give each pay period a "check stub or pay voucher" showing:
  - hours worked;
  - rate of pay;
  - required state and federal deductions;
  - authorized deductions.
  [US-NDS5-007, A.1]
- Electronic delivery: no rule was found in the rules or statutes read. Retention period: none stated (34-06-07 requires only a register of employees) [US-NDS5-006].
- Language: no rule [US-NDP9L-001].
- **This supersedes the "no provision" reading** in US-ND-003 and in the US-MQ-48 part 6 answer.
- Confidence: high on content; electronic consent and retention open.

## 5. reporting_instruments

| Filing | Rule | register_id |
|---|---|---|
| Registration | ND TAP (withholding); UI EASY (Job Service) | US-NDS5-002, -011 |
| Form 306 withholding return | Quarterly, due Apr 30 / Jul 31 / Oct 31 / Jan 31, filed even with zero wages. Annual option if prior-year withholding < 1,000 with 4 timely quarters (apply before Q1). E-file mandatory if prior-year withholding >= 1,000 or a third-party provider e-files federally. Channel: TAP / ACH debit / ACH credit (Form 301-EF) | US-NDS5-002, -003 |
| Form 307 annual reconciliation + W-2 | Due Jan 31. Satisfied by e-filing the W-2s; e-filing of Form 307 is required even with zero W-2s. W-2 e-file mandatory since 2022 (57-38-60(12)). Format EFW2 (SSA 42-007), W-2c EFW2C. Channel: TAP upload/key-entry or software web service; test files can be validated in TAP | US-NDS5-002, -003 |
| UI Employer's Contribution and Wage Report | Quarterly, electronic (UI EASY or Secure FTP); report and payment due by the end of the month after the quarter; excess wages per quarter | US-NDS5-011, -009 |
| New hire | Within 20 days of the first day of work, to the State Directory of New Hires (HHS Child Support). Fields: name, address, SSN, hire date, health insurance offered; employer name, address, FEIN | US-NDS5-013 |
| POA | Form 500 (OST); payroll provider designated on the registration form | US-NDP51-002, US-NDS5-002 |

- Channels: Form 306 = `online_form` / `api` (ACH); W-2 = `file_upload` (EFW2); UI report = `file_upload` / `online_form`.

## 6. leave
- **Paid sick leave**: no state statute in the chapters read (34-01, 34-06, 34-14, NDAC 46-02-07). PFML: none (34-01-15.1) [US-NDP52-002].
- **PTO**: earned or awarded PTO is wages at separation (NDAC 46-02-07-02(12)) [US-NDS5-007].
  - Use-it-or-lose-it is allowed with notice.
  - Forfeiture at separation is not allowed, except under 34-14-09.2 (section 7) [US-NDS5-005].
- Confidence: 80% (no exhaustive search of Title 34 for other paid-leave mandates, e.g. jury or voting leave pay).

## 7. termination
- **Final pay** (34-14-03) [US-NDS5-005]:
  - On discharge, resignation or suspension, wages are due at the next regular payday.
  - A discharged employee is paid by certified mail to a designated address, or as agreed.
  - Default penalty: the daily contract wage, for up to 30 days.
- **PTO payout**: PTO available for use is paid at the regular rate [US-NDS5-007]. On a voluntary quit, a private employer may withhold it only if all three hold:
  - written notice was given at hire;
  - service is under one year;
  - the employee gave less than 5 days' notice.
  [US-NDS5-005]
- **Child support**: report a layoff or termination within 7 (business) days for employees with an IWO or NMSN [US-NDS5-016, US-NDS5-014].
- UI separation notice and state WARN: not found (not searched in depth). See Open questions.

## 8. benefits_in_kind
- ND taxable income = federal taxable income (57-38-30.3(2)), and ND withholding wages = IRC 3401 wages [US-NDS5-004, US-NDS5-002]. ND follows the federal exclusions (401(k), 125, HSA, transit, group-term life); no state departure was found.
- The 2025 employer child-care contribution credit is an employer income-tax credit with no payroll effect [US-NDS5-018].

## 9. deductions_garnishments
- **Wage deductions**: only those required by law or court, advances, or deductions authorised in writing (recurring, or specific non-recurring). Damage, breakage or shortage must be authorised at the time of deduction (34-14-04.1) [US-NDS5-005].
- **Creditor garnishment** [US-NDS5-008]: the lesser of 25% of disposable earnings or the excess over 40 x the federal minimum wage (**290.00/week**, derived).
  - It is reduced by **20.00 per week per resident dependent**. The debtor gives the list within 10 days; if not, no dependents are counted.
- **Support limits**: 50/60%, or 55/65% with arrears.
- **IWO** [US-NDS5-014]:
  - Start the first pay period after receipt; remit within 7 business days.
  - **Employer fee: up to 3.00/month**.
  - Cap: 50% of disposable income when the full amount cannot be withheld.
  - E-remittance is mandatory for employers with 25+ employees and more than 4 IWOs.
- **Lump sums of 1,000 or more** (bonus, commission, leave cash-out) for obligors in arrears: notify Child Support before payment, release one half, and hold the other half for 30 days [US-NDS5-015].

## 10. collective_agreements
- No state prevailing-wage law [US-NDP51-003, MEDIUM: WebFetch summary of the DOL table; no ND statute was read to confirm absence]. Federal Davis-Bacon applies to federal projects.

## 11. indexation
- **PIT brackets**: indexed annually by the federal IRC 1(f) cost-of-living adjustment, with rates fixed (57-38-30.3(1)(g)). Published in the annual OST withholding booklet [US-NDS5-004, US-NDS5-001].
- **UI wage base**: 70% of the statewide average annual wage, set by Oct 1 and published in the Job Service rate schedules [US-NDS5-009, US-NDS5-012].
  - G-DERIVE is not possible: the statewide average wage is not published in the documents read. 46,600 / 0.70 = 66,571 is the implied average, unverified.
- **Minimum wage**: not indexed [US-NDS5-006].

## 12. data_protection
- Breach notice to ND residents, and to the Attorney General when more than 250 people are affected. Name + SSN is personal information (NDCC 51-30) [US-NDS5-017].
- No pay-statement SSN-truncation rule was found.

## 13. live_legal_change
- **OST news sweep, 2026-01-01 to 2026-11-02** (latest item 2026-10-08): no withholding or employer-tax change [US-NDS5-019].
- **2025 session**: the only income-tax item is the employer child-care credit [US-NDS5-018].
- **2027**:
  - The withholding booklet is not yet published (guessed URL 404).
  - The UI 2027 schedule is not yet available (guessed URL HTTP 403).
  - Minimum wage: no change.

## Special populations

| Population | ND rule | register_id |
|---|---|---|
| Domestic / household | Excluded from ND withholding (IRC 3401 excludes domestic service in a private home). UI covered at 1,000/quarter. Live-in domestic workers exempt from overtime. Casual babysitters exempt from minimum wage | US-NDS5-002, -011, -007 |
| Agricultural | Farmer/rancher wages exempt from ND withholding (57-38-60(10)). UI only at 10+ workers / 20,000 per quarter. Overtime exempt | US-NDS5-002, -011, -007 |
| Minors | Same minimum wage, no youth subminimum. Vocational students may be licensed at 85% or more of the minimum. Newspaper carriers under 18 and a minor employed by a parent are UI-excluded. Child-labour hours (34-07) not read | US-NDS5-007, -010 |
| Tipped | Tip credit up to 33% of the minimum wage, so the cash wage is 4.86 at 7.25 (derived). Advance notice and records required. Tip pool by vote of tipped employees | US-NDS5-007 |
| Clergy / religious | UI excludes ministers, religious orders and church organisations. Withholding follows federal (no state rule beyond federal) | US-NDS5-010, -002 |
| Students | UI excludes enrolled students (52-01-01(17)). Vocational subminimum 85% | US-NDS5-010, -007 |
| Nonresident aliens | ND withholding on a separate W-4 (Single, no Exempt). Treaty exemption ignored unless it covers states | US-NDS5-002 |
| Statutory employees | UI excludes commission-only insurance, real estate and securities agents. Otherwise no state rule beyond federal | US-NDS5-010 |
| Government employees | Covered by minimum wage and withholding (the state is an "employer"). Comp time per FLSA (34-06-04.1). Trade-time rules (46-02-07-04) | US-NDS5-006, -007, -002 |
| Military spouses / military pay | NDW-M exemption. No withholding on deductible military pay unless requested | US-NDS5-002, -004 |
| Tribal members | Exempt when enrolled, living on a reservation and working there | US-NDS5-002 |

## MULTI hand-offs (ND answers)
- **SUI wage-base credit for wages reported to another state**: yes for the same employer. Taxable wages include "service constituting employment under the employment security law of any other state" (52-04-03(1)) [US-NDS5-009]. Confidence 75%: the statute is read, but no Job Service worked example.
- **UI localization**: out-of-state residents are reported to ND if their principal place of employment is ND; temporary ND work is reported to the principal state [US-NDS5-011, US-NDS5-010].
- **PFML/SDI coverage of multistate workers**: not applicable (none in ND).
- **Paid sick leave reach**: not applicable (no ND statute).
- **Pay-statement reach to out-of-state work**: NDAC 46-02-07 does not state a territorial rule. Default: it applies to employees employed in ND (34-14-01, "employing any person in this state"). Confidence 60%.

## ACCESS gaps
- `https://www.jobsnd.com/sites/www/files/documents/jsnd-documents/uitaxrateschedules2027.pdf`: HTTP 403 on 2026-11-02 (probably not published yet; the rates are set after September).
- `https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2027-iit/2027-income-tax-withholding-rates-booklet.pdf`: 404 on 2026-11-02 (guessed URL; not yet published).
- `https://www.tax.nd.gov/sites/www/files/documents/forms/business/form-ndw-r.pdf`: HTTP 403 (guessed URL; the form itself was not needed, since the rule is in US-NDS5-002).

## Open questions
1. **Booklet example defect (oracle).** The 2026 Section 2 example (weekly 1,800, single, annual 734, withhold 14) does not reproduce from the printed 2026 table (701.51, so 13). Closes with: OST (withhold@nd.gov) confirming that the example is stale and that the table governs, or a corrected booklet.
2. **US-ND-003 / US-MQ-48 part 6** needs re-pointing to US-NDS5-007 (the NDAC 46-02-07-02(10) pay stub rule). This is a synthesis action, not research.
3. **Pay-statement electronic delivery and payroll record retention**: no ND rule was found in the chapters read. Closes with: a read of the NDDOLHR wage-and-hour FAQ, or of NDAC 46-02 recordkeeping provisions beyond ch. 46-02-07.
4. **Prevailing wage absence** rests on a WebFetch summary of the DOL table. Closes with: a direct read of `https://www.dol.gov/agencies/whd/state/prevailing-wages`, or an NDDOLHR statement.
5. **2027 values**: the UI wage base and rates (Job Service, after Oct 1, 2026) and the 2027 withholding booklet (OST, about December 2026). Closes with: those two publications.
6. **UI separation notice / state WARN, and child-labour hours (34-07)**: not researched. Closes with: the Job Service Employer's Guide to UI, and a read of NDCC 34-07.
