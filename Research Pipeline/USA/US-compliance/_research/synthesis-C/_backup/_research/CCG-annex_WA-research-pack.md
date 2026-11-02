# CCG research pack - annex_WA (Washington)

Synthesis-B worker MN-WY, 2026-11-02. Unit `annex_WA` of the CCG (jurisdiction annex, all 13 domains + special populations).
Facts file: `_research/CCG-annex_WA-facts.json` (62 facts, 1 pending on the register_id pattern defect, 13 unresolved). Every claim below carries its register_id inline; numbers may be cited in the CCG only through a fact key.

## 0. How to use this pack

- Body sections 1-13 and Special populations are the stage-5 findings (`_research/stage5/WA.md`), carried verbatim because they are already organised by the 13 CCG domains with register ids inline.
- Federal layer (FIT, FICA, FUTA, W-2/941/940), the multistate rules (reciprocity, sourcing) and the language seams (US-OWN-006: payslip in English; second-language duties attach to notices and posters only) live in annex_FED / annex_MULTI and are not repeated here.
- Special populations (US-OWN-005): the state-level rules are in the Special populations table below; the country-wide coverage matrix is CCG unit `coverage`.
- Values are 2026 unless the fact says otherwise. 2027 values appear only where the row carries an enacted or published 2027 figure; projections are never facts.

## 0.1 Synthesis decisions and traps (bind the builder)

- WA has NO wage tax in 2026/2027 (SB 6346 9.9% from 2028 is assessment-level). Employee deductions: PFML (1.13% x 71.43% in 2026; 1.2% x 70.7% in 2027), WA Cares 0.58% no cap, workers' comp hourly share.
- Local minimum wages with MID-YEAR steps (Everett, Renton on 2026-07-01).
- PFML wages EXCLUDE tips; UI wages INCLUDE reported tips.
- UI quarterly report requires hours worked and SOC code per employee.

## 0.2 Register status check of the ids cited in the findings

All ids cited in the findings are `active` in the register.

## 0.3 Facts emitted

| key | value | from | to | register_id | conf |
|---|---|---|---|---|---|
| `wa.minwage.hourly` | 17.13 USD | 2026-01-01 | 2026-12-31 | US-WAS5-006 | high |
| `wa.minwage.hourly` | 17.73 USD | 2027-01-01 |  | US-WAS5-007 | high |
| `wa.labour.minwage.youth_14_15.hourly` | 14.56 USD | 2026-01-01 | 2026-12-31 | US-WAS5-006 | high |
| `wa.labour.minwage.youth_14_15.hourly` | 15.07 USD | 2027-01-01 |  | US-WAS5-007 | high |
| `wa.minwage.indexation` | CPI-W Aug-Aug, announced Sept 30, effective Jan 1, nearest cent | 2021-01-01 |  | US-WAS5-001 | high |
| `wa.labour.minwage.local.seattle.hourly` | 21.3 USD | 2026-01-01 | 2026-12-31 | US-WAS5-008 | high |
| `wa.labour.minwage.local.tukwila.hourly` | 21.65 USD | 2026-01-01 | 2026-12-31 | US-WAS5-008 | high |
| `wa.labour.minwage.local.bellingham.hourly` | 19.13 USD | 2026-01-01 | 2026-12-31 | US-WAS5-008 | high |
| `wa.labour.minwage.local.seatac.hourly` | 20.74 USD | 2026-01-01 | 2026-12-31 | US-WAS5-008 | high |
| `wa.labour.minwage.local.burien.large.hourly` | 21.78 USD | 2026-01-01 | 2026-12-31 | US-WAS5-008 | high |
| `wa.labour.minwage.local.burien.mid.hourly` | 20.78 USD | 2026-01-01 | 2026-12-31 | US-WAS5-008 | high |
| `wa.labour.minwage.local.burien.small.hourly` | 19.28 USD | 2026-01-01 | 2026-12-31 | US-WAS5-008 | high |
| `wa.labour.minwage.local.king_county_uninc.large.hourly` | 20.82 USD | 2026-01-01 | 2026-12-31 | US-WAS5-008 | high |
| `wa.labour.minwage.local.everett.large.hourly` | 20.77 USD | 2026-01-01 | 2026-12-31 | US-WAS5-008 | high |
| `wa.labour.minwage.local.everett.mid.hourly` | 18.77 USD | 2026-01-01 | 2026-06-30 | US-WAS5-008 | high |
| `wa.labour.minwage.local.everett.mid.hourly` | 19.77 USD | 2026-07-01 | 2026-12-31 | US-WAS5-008 | high |
| `wa.labour.minwage.local.renton.large.hourly` | 21.57 USD | 2026-01-01 | 2026-12-31 | US-WAS5-008 | high |
| `wa.labour.minwage.local.renton.mid.hourly` | 20.57 USD | 2026-01-01 | 2026-06-30 | US-WAS5-008 | high |
| `wa.labour.minwage.local.renton.mid.hourly` | 21.57 USD | 2026-07-01 | 2026-12-31 | US-WAS5-008 | high |
| `wa.minwage.tip_credit.allowed` | False | 2021-01-01 |  | US-WAS5-001 | high |
| `wa.overtime.weekly_threshold_hours` | 40 hours | 2021-01-01 |  | US-WAS5-001 | high |
| `wa.overtime.premium.multiplier` | 1.5 ratio | 2021-01-01 |  | US-WAS5-001 | high |
| `wa.exempt.salary.weekly_min` | 1541.7 USD | 2026-01-01 | 2026-12-31 | US-WAS5-005 | high |
| `wa.labour.exempt_salary.large.weekly` | 1773.0 USD | 2027-01-01 | 2027-12-31 | US-WAS5-007 | high |
| `wa.labour.exempt_salary.small.weekly` | 1595.7 USD | 2027-01-01 | 2027-12-31 | US-WAS5-007 | high |
| `wa.labour.computer_professional.hourly` | 59.96 USD | 2026-01-01 | 2026-12-31 | US-WAS5-005 | high |
| `wa.labour.computer_professional.hourly` | 62.06 USD | 2027-01-01 |  | US-WAS5-007 | high |
| `wa.pay_frequency.rule` | at least monthly; pay day max 10 days after period end for shorter periods | 2026-01-01 |  | US-WAS5-004 | high |
| `wa.pit.exists` | False | 2028-01-01 |  | US-WAS5-017 | high |
| `wa.sui.wage_base` | 78200 USD | 2026-01-01 | 2026-12-31 | US-WAS5-012 | high |
| `wa.ui.rate.min_total` | 0.27 % | 2026-01-01 | 2026-12-31 | US-WAS5-012 | high |
| `wa.ui.rate.max_total` | 6.02 % | 2026-01-01 | 2026-12-31 | US-WAS5-012 | high |
| `wa.ui.rate.new_employer.rule` | 115% of industry average, floor 1% | 2026-01-01 | 2026-12-31 | US-WAS5-029 | medium |
| `wa.sui.employee.rate` | 0 % | 2026-01-01 | 2026-12-31 | US-WAS5-012 | high |
| `wa.pfml.rate.total` | 1.13 % | 2026-01-01 | 2026-12-31 | US-WAS5-011 | high |
| `wa.pfml.employee.share` | 71.43 % | 2026-01-01 | 2026-12-31 | US-WAS5-011 | high |
| `wa.pfml.rate.total` | 1.2 % | 2027-01-01 |  | US-WAS5-015 | high |
| `wa.pfml.employee.share` | 70.7 % | 2027-01-01 |  | US-WAS5-015 | high |
| `wa.pfml.wage_cap.annual` | 184500 USD | 2026-01-01 | 2026-12-31 | US-WAS5-011 | high |
| `wa.pfml.small_employer.threshold` | 50 | 2026-01-01 |  | US-WAS5-011 | high |
| `wa.pfml.wages.tips_included` | False | 2026-01-01 |  | US-WAS5-023 | high |
| `wa.ltc.wa_cares.employee.rate` | 0.58 % | 2023-07-01 |  | US-WAS5-016 | high |
| `wa.wc.employee_deduction.rule` | 50% x (Stay-at-Work + Medical Aid + Supplemental Pension) per hour per risk class | 2026-01-01 | 2026-12-31 | US-WAS5-019 | high |
| `wa.wc.supplemental_pension.rate` | 0.1912 USD | 2026-01-01 | 2026-12-31 | US-WAS5-019 | high |
| `wa.payslip.items` | pay basis (hours/days), rates, gross, all deductions, pay period dates, payment date; separate from paycheck | 2026-01-01 |  | US-WAS5-004 | high |
| `wa.payslip.sick_leave_balance.monthly` | True | 2026-01-01 |  | US-WAS5-005 | high |
| `wa.records.esd.retention_years` | 4 years | 2026-01-01 |  | US-WAS5-030 | high |
| `wa.report.ui.quarterly_due` | Apr 30; Jul 31; Oct 31; Jan 31 | 2026-01-01 |  | US-WAS5-013 | high |
| `wa.newhire.report_days` | 20 days | 2026-01-01 |  | US-WAS5-018 | high |
| `wa.leave.paid_sick.accrual_ratio_hours_worked` | 40 hours | 2021-01-01 |  | US-WAS5-001 | high |
| `wa.leave.sick.payout_on_separation` | False | 2021-01-01 |  | US-WAS5-001 | high |
| `wa.leave.pfml.job_protection.employer_threshold` | 25 | 2026-01-01 | 2026-12-31 | US-WAS5-028 | high |
| `wa.final_pay.rule` | end of established pay period (discharge and resignation) | 2026-01-01 |  | US-WAS5-002 | high |
| `wa.term.discharge_statement.days` | 21 days | 2026-01-01 |  | US-WAS5-004 | high |
| `wa.garn.consumer.exempt_rate` | 80 % | 2026-01-01 |  | US-WAS5-009 | high |
| `wa.garn.consumer.exempt.weekly` | 599.55 USD | 2026-01-01 | 2026-12-31 | US-WAS5-009 | high |
| `wa.garn.general.exempt.weekly` | 253.75 USD | 2026-01-01 |  | US-WAS5-009 | high |
| `wa.garn.answer_fee.first` | 20 USD | 2026-01-01 |  | US-WAS5-009 | high |
| `wa.garn.iwo.employer_fee.first` | 10 USD | 2026-01-01 |  | US-WAS5-018 | high |
| `wa.garn.iwo.max_rate` | 50 % | 2026-01-01 |  | US-WAS5-018 | high |
| `wa.prevailing_wage.certified_payroll` | monthly in L&I online system; records 3 years | 2026-01-01 |  | US-WAS5-010 | high |
| `wa.data.breach.notice_days` | 30 days | 2026-01-01 |  | US-WAS5-025 | high |
| `wa.pit.local.employee_tax.exists` | False | 2026-01-01 |  | US-WA-P5-1-001 (PENDING id pattern) | high |

# Findings by domain (stage 5)

## Access findings

**The Code Reviser hosts fail TLS from this network.** `app.leg.wa.gov` and `lawfilesext.leg.wa.gov` return `SEC_E_INVALID_TOKEN` under schannel and `WRONG_VERSION_NUMBER` under OpenSSL; plain http returns an empty reply. This is the "RCW page SSL error" that earlier passes noted.
- Every RCW, WAC and session-law row in this shard therefore comes from a Wayback `id_` snapshot of the official URL. The snapshot date is in the `authority` column.
- The snapshots run from 2025-05 to 2026-10.
- The text is the Code Reviser's own HTML: A.1 content, served through an archive.
- Two snapshots predate 2026 amendments:
  - The RCW 50A.10 snapshot (2025-05) predates 2025 c 304 and 2SHB 2345. The 2026 text of 50A.10.030 was read from the 2SHB 2345 session law instead [US-WAS5-020].
  - The RCW 26.23 snapshot is from 2025-09.

Other hosts:
- **Readable directly:** `lni.wa.gov`, `esd.wa.gov`, `dor.wa.gov`, `wacaresfund.wa.gov`.
- **Not readable:** `paidleave.wa.gov` returns 403, directly and on Wayback. `www.seattle.gov` fails TLS, and Wayback returns 403.

## 1 — labour_code
- **State minimum wage:**
  - 2026: **USD 17.13/h** [US-WAS5-006, A.2].
  - 2027: **USD 17.73/h** from 2027-01-01 [US-WAS5-006, US-WAS5-007].
  - Statute: RCW 49.46.020(2)(b). L&I recalculates each Sept 30 by CPI-W, August to August, to the nearest cent, effective Jan 1 [US-WAS5-001, A.1].
  - **G-DERIVE:** 17.13 x 1.035 = 17.7295, which rounds to **17.73**. This matches the published "+3.5%" [US-WAS5-007, `derived arithmetically`]. High confidence.
- **Youth (14-15):** 85% of the minimum wage. 2026: 0.85 x 17.13 = 14.5605, published as 14.56. 2027: 0.85 x 17.73 = 15.0705, published as 15.07. Both reproduced [US-WAS5-006/007]. Under-18 rates are set by rule (49.46.020(5)).
- **Local minimum wages, 2026** [US-WAS5-008, A.2, from the L&I page]:

  | Locality | 2026 rate (USD/h) | Tiers and periods |
  |---|---|---|
  | Bellingham | 19.13 | single rate |
  | Burien | 21.78 / 20.78 / 19.28 | 501+ / 16-500 / up to 15 employees |
  | Everett | 20.77 | more than 500 WA employees |
  | Everett | 18.77, then 19.77 | 15-499 employees: Jan-Jun, then Jul-Dec |
  | Everett | not covered | 14 or fewer employees |
  | King County (unincorporated) | 20.82 / 19.82 / 18.32 | see the US-WAS5-008 tiers |
  | Renton | 21.57 | more than 500 employees |
  | Renton | 20.57, then 21.57 | 15-500 employees: Jan-Jun, then Jul-Dec |
  | SeaTac | 20.74 | hospitality and transportation |
  | Seattle | 21.30 | single rate |
  | Tukwila | 21.65 | single rate |

  - Two localities change rate mid-year: Everett and Renton step up on 2026-07-01. This is a `mid_year_rate_change` case.
  - Each city defines employer size itself.
  - **2027 local rates:** not obtained, because seattle.gov is blocked and the L&I page still shows 2026. Open question.
- **Overtime (RCW 49.46.130):** 1.5x the regular rate over 40 h per week.
  - Agricultural employees are owed overtime over 40 h from 2024-01-01 (6)(c).
  - Exemptions are listed in (2), and the retail-commission and vehicle-sales rules in (3)-(4) [US-WAS5-001].
  - WA has no daily overtime.
- **Exempt salary threshold** (WAC 296-128-545) [US-WAS5-005 A.1; US-WAS5-007 A.2]:
  - 2026: 2.25x minimum wage x 40 h, any employer size. 2.25 x 17.13 x 40 = **USD 1,541.70/week** (80,168.40/year), derived.
  - 2027: 51+ employees, 2.5x = **1,773.00/week** (92,196.00/year). 1-50 employees, 2.25x = **1,595.70/week** (82,976.40/year).
  - 2028 onward: 2.5x for all employers.
  - Computer professionals: 3.5x per hour, so 59.96 (2026) and 62.06 (2027). All figures reproduced.
- **Pay frequency and pay day** (WAC 296-126-023 / 296-128-035):
  - Wages are paid at no longer than monthly intervals, on an established regular pay day.
  - For a pay period shorter than a month, pay day is no later than 10 calendar days after the period ends.
  - A monthly payroll may carry the last 7 days of the period to the next pay day.
  - Overtime is paid on the regular pay day of the period in which it was earned.
  - Mailed cheques must be postmarked by pay day. Direct deposit must be available on pay day [US-WAS5-004].
- **Method of payment:** RCW 49.48.010(1) requires reimbursing the employee's bank NSF fee within 30 days [US-WAS5-002].
  - A WA direct-deposit or paycard consent statute was **not read in this pass**. Open question.
- **Tips and service charges:** paid in full to the employee and **no tip credit** (49.46.020(3)). Automatic service charges must be disclosed (49.46.160) [US-WAS5-001].
- **Non-compete:** ban from July 2027. Salary threshold for Jan-Jun 2027: USD 131,326.59 (employees) and 328,316.49 (contractors) [US-WAS5-007]. This is not a payroll calculation; for CCG awareness only.

## 2 — income_tax
- **No state income tax on wages in 2026 or 2027.** There is no withholding, no state W-4, no supplemental rate, no state W-2 filing and no reciprocity [US-WAS5-017, A.2, a local copy re-verifying US-WA-PIT-001].
- **2028 watch item:** a 9.9% tax on individuals and joint filers with AGI above USD 1 million, from 2028-01-01, under SB 6346 (2026). First returns are due April 2029.
  - Operating level: **assessment**. The DOR page names no employer withholding mechanism [US-WAS5-017].
  - The SB 6346 text was not read in this pass. Open question: confirm there is no withholding clause.
- **Local income taxes:** none are withheld from employees.
  - The Seattle Payroll Expense Tax is an **employer** business tax on a city return [US-WA-P5-1-001, US-WAP7-005].
  - The Seattle Social Housing Tax is 5% of compensation above USD 1,000,000, paid by the employer [US-WAP9V-001].
  - Both already registered (employer_payroll_levies, T4-shaped element).
- **Residents and nonresidents:** not applicable for state tax. WA residents working elsewhere follow the work state's rules (MULTI unit).

## 3 — social_security (UI, PFML, WA Cares, workers' compensation)

**UI (ESD)** [US-WAS5-012, US-WAS5-029]:
- Taxable wage base 2026 **USD 78,200** (2025: 72,800). Also in US-WA-SUI-001.
- The 2027 base was **not yet published** on 2026-11-02. ESD indexes it on average WA wages under RCW 50.24.010, which was not read.
- 2026 qualified-employer rates:
  - Experience rate: 0.00-5.40%.
  - Graduated social cost: 0.24-0.72%. The ESD page states a 1.22% statutory cap.
  - Employment Administration Fund (EAF): 0.02-0.03%.
  - Total: **0.27% to 6.02%**. Arithmetic: 0+0.24+0.03 = 0.27; min(5.40+0.72, 6.00)+0.02 = 6.02.
- Delinquent employers: up to 8.15%.
- New employers: 115% of the industry average, with a floor of 1% (WAC 192-320-025; US-WA-SUI-002).
- No employee UI contribution.

**UI wages** (RCW 50.04.320) [US-WAS5-022]:
- Include commissions, bonuses, non-cash pay and tips reported to the employer.
- A successor employer counts the predecessor's wages toward the base.

**PFML** [US-WAS5-011, US-WAS5-015, US-WAS5-020, US-WA-PFML-001]:
- 2026 total premium **1.13%**; the employee may bear up to 71.43%.
- 2027 total premium **1.2%** (= the statutory cap in 50A.10.030(6)(b)(ii)). The split is employer **29.3%** and employee **70.7%** (ESD release, 2026-10-16).
- The premium applies to wages up to the Social Security wage base: 2026 USD 184,500; 2027 = the SSA 2027 base, taken from the FED unit.
- Employers with fewer than 50 WA employees (size fixed on Sept 30) owe no employer share but must still collect the employee share.
- **2SHB 2345** (c 26, Laws 2026; effective 2026-06-11; applied by ESD from 2027 premiums):
  - The employee share moves between the family and medical premium lines. It may now be up to 100% of the medical premium plus a family portion.
  - The total employee share is unchanged: family + 45% of medical.
  - Payroll impact: two deduction lines with new proportions, and the quarterly Paid Leave report.
  - **G-DERIVE:** with employee share = f + 0.45m and f + m = 1, the implied medical share of the total premium is 51.95% (2026) and 53.27% (2027). ESD does not state these shares on a readable page, so they are recorded as a derivation and not as a fact.
- **PFML wages** (RCW 50A.05.010(22), (29)) exclude tips and employer top-ups of PFML benefits [US-WAS5-023]. **This differs from UI wages**, which include reported tips.

**WA Cares (long-term care)** [US-WAS5-016, US-WAS5-024; US-WA-LTC-001]:
- Employee-only premium of **0.58% of gross wages, with no cap**.
- Reported on the same quarterly report as Paid Leave. Suggested paystub label: "WA Cares Fund".
- Exemptions:
  - Out-of-state residence, active-duty military, military spouses, and veterans rated 70%+.
  - **Non-immigrant work visa holders are automatically exempt from 2026-01-01**, unless they opt in in writing to the employer.
  - Private-LTC exemptees may cancel their exemption between 2026-01-01 and 2028-06-30.
  - The employer must stop deducting once shown an ESD approval letter.

**Workers' compensation (L&I state fund)** [US-WAS5-019 A.2; US-WA-LTC-002 A.1]:
- Hourly rates per risk class.
- Worker payroll deduction = **50% x (Stay-at-Work + Medical Aid + Supplemental Pension)**. Verified across 318 of 320 classes in the 2026 xlsx; classes 6901 and 6906 carry no deduction.
- 2026 Supplemental Pension Fund rate is 0.1912 for every class.
- Example, class 101: worker deduction USD 0.3532 per hour.
- 2027 rates are only *proposed* on the L&I page. Final adoption is normally in December.
- The supplemental-pension half deduction rests on the L&I table. The statute for it (RCW 51.32.073) was not read. Open question.
- Not in this pass: the L&I quarterly report page (404 at the URL tried).

**Other employer levies:** none beyond the P7/P9 list (Seattle elements above). Not redone.

## 4 — payslip_statute
- **Content** (WAC 296-126-040), on every payday:
  - pay basis (hours or days worked), rate(s) of pay, gross wages and all deductions;
  - the pay period by month/day/year, and the payment date;
  - a statement separate from the paycheck.
  - [US-WAS5-004 A.1; US-WA-LAB-001]
- **Paid sick leave balance:** at least monthly, the balance accrued, used and available, which may go on the regular pay statement (WAC 296-128-755(2)) [US-WAS5-005]. In practice this is a **payslip field**.
- **Electronic delivery:** allowed if the employee can receive and copy the statement on payday. Otherwise it must be on paper [US-WAS5-004].
- **WA Cares label:** recommended, not mandatory [US-WAS5-016].
- **Language:** none required (US-WAL-001, US-WAP9M-001; already registered).
- **Retention:**
  - L&I: 3 years (WAC 296-126-050 and 296-128-020).
  - ESD: **4 years** from the date of payment, including name, SSN, SOC code, daily hours, work location and separation reason (RCW 50.12.070 / WAC 192-310-050) [US-WAS5-030].
  - Public works: 3 years from project acceptance [US-WAS5-010].
  - The build should keep the longest: 4 years.

## 5 — reporting_instruments
- **Withholding return:** none, because there is no income tax.
- **Registration:** an employer with WA employees needs a DOR business license, or an update when it first hires. Operating unregistered costs the greater of USD 1,000 or 2x the unpaid tax per quarter [US-WAS5-013].
- **UI quarterly tax and wage report** (ESD, in EAMS through SAW: online, file import or ESD paper forms) [US-WAS5-013; US-FIL-016]:
  - Per employee: name, SSN, gross pay, **hours worked in the quarter** (rounded up to whole hours; 40 per week if a salaried worker's hours are not tracked; paid leave hours included) and **SOC code**.
  - Due Apr 30, Jul 31, Oct 31 and Jan 31.
  - A nil report is required.
  - Corporate officers without voluntary coverage go in the Exempt Officer section, as a count plus combined wages [US-WAS5-027].
- **Paid Leave + WA Cares combined quarterly report:** wages and hours. Filed on the paidleave.wa.gov portal, which is blocked from here.
  - Its field list and deadline are not re-read in this pass and rest on US-WA-PFML-001 / US-WA-LTC-001.
  - The ESD release states that Q3 reports are due in October [US-WAS5-015].
- **Workers' compensation quarterly report** (L&I): hours per risk class. Page not obtained. Open question.
- **State W-2 filing:** not applicable.
- **New-hire reporting** (RCW 26.23.040):
  - Report to the WA state support registry (DSHS Division of Child Support) within **20 days** of hire.
  - Covers rehires after a separation of 60 or more consecutive days.
  - Fields: employee name, address, SSN, date of birth and first day of paid work; employer name, address and FEIN.
  - Electronic reporters may send two monthly transmissions, 12 to 16 days apart.
  - Penalty: USD 25 per employee per month.
  - [US-WAS5-018 A.1; US-WAS5-014 A.2]
- **Third-party filing:** a UI power of attorney per client [US-FED-P5-1-016]. For the Seattle PET, a Taxpayer Authorization Form per client [US-WA-P5-1-001].
- **Public works certified payroll:** monthly through the L&I online system [US-WAS5-010].

## 6 — leave
- **Paid sick leave** (RCW 49.46.210, WAC 296-128-600 to -790) [US-WAS5-001, US-WAS5-005]:
  - Accrual: at least 1 h per 40 h worked.
  - Usable from day 90 of employment.
  - Paid at the greater of the minimum wage or the normal hourly rate.
  - Carryover may be capped at 40 h.
  - **No payout at separation.** Construction workers are the exception (49.46.210(1)(l)).
  - The balance is reinstated if the employee is rehired within 12 months.
  - Notice of entitlement at hire, and a balance statement at least monthly.
  - Purposes include immigration proceedings and health-related school closures.
- **Seattle Paid Sick and Safe Time:** not obtained (seattle.gov blocked).
- **PFML job protection** (RCW 50A.35.010, version effective 2026-01-01) [US-WAS5-028]:
  - Employer size: 25+ employees in 2026, 15+ in 2027, 8+ from 2028.
  - The employee must have started at least 180 days before the leave.
  - This replaces the 50 employees / 12 months / 1,250 hours test.
- **PFML premiums during leave:** premiums are assessed on wages paid, so none are due on benefits paid by ESD. Not separately sourced.
- **Vacation:** no WA statute requiring paid vacation was located.

## 7 — termination
- **Final pay:** due at the end of the established pay period, **for both discharge and resignation** (RCW 49.48.010(2)). A CBA may provide otherwise [US-WAS5-002].
- **Final-pay deductions** (WAC 296-126-025) [US-WAS5-004]:
  - Deductions for cash shortages or breakage are allowed only for incidents in the final period, and may not take pay below the minimum wage.
  - Deductions that are required by law, or authorized and for the employee's benefit, may go below the minimum wage.
- **Accrued vacation payout:** no WA statute located. It follows the employer's policy or contract. The L&I administrative policy was not read. Open question.
- **Sick leave:** not paid out (above).
- **Former-employee discharge statement:** within 21 days of a written request, the employer gives the discharge date and the reason (WAC 296-126-050(4)) [US-WAS5-004].
- **WARN:** ESD hosts the WARN database, and the federal 60-day notice applies [US-WAS5-026, A.3]. The state mini-WARN statute and any UI separation-notice duty were **not read**. Open question.
- **Domestic workers from 2027-07-01:** two weeks' written termination notice (four weeks in the cases the Act sets), with exceptions (SHB 2355) [US-WAS5-021].

## 8 — benefits_in_kind
- **Income tax:** not applicable, because there is no state income tax, so no conformity question arises for 401(k), s.125, HSA, transit or group-term life.
- **UI and PFML wage bases:**
  - Both count "remuneration" as all compensation, including the cash value of non-cash compensation [US-WAS5-022, US-WAS5-023].
  - Tips: included for UI, excluded for PFML.
- **Not answered in this pass:** whether pre-tax s.125 or 401(k) deferrals are excluded from UI and PFML remuneration. The ESD WAC rules (WAC 192-310-030 and the PFML rules in chapter 192-510) were not read. This is a material open question for the WTC flags.
- **WA Cares:** applies to "gross wages", with no cap [US-WAS5-016]. The same deferral question applies.

## 9 — deductions_garnishments
- **Authorization:** a deduction must be required by law, agreed (RCW 49.48.010(3) allows oral or written agreement; RCW 49.52.060 requires express written advance authorization), or for medical care, with no employer profit [US-WAS5-002, US-WAS5-003].
  - Agreed deductions for the employee's benefit may go below the minimum wage (WAC 296-126-028) [US-WAS5-004].
- **Overpayments:**
  - Private employers may recoup if the overpayment was infrequent and inadvertent, detected within 90 days, with advance written notice (WAC 296-126-030) [US-WAS5-004].
  - Public employers may deduct at most 5% of disposable earnings per period (RCW 49.48.200) [US-WAS5-002].
- **Garnishment exemption** (RCW 6.27.150), weekly [US-WAS5-009]:

  | Debt type | Exempt amount (the greater of) | Weekly figure |
  |---|---|---|
  | General | 35x the federal minimum wage, or 75% | 35 x 7.25 = 253.75 |
  | **Consumer debt** | 35x the **state** minimum wage, or **80%** | 2026: 35 x 17.13 = **599.55**; 2027: 620.55 |
  | Private student loans | 50x the "highest minimum wage law in the state", or 85% | depends on which wage counts |
  | Spousal maintenance | 50% exempt | — |

  - **Processing fee:** USD 20 for the first answer and USD 10 for the second (6.27.095).
- **Child support** (RCW 26.23.060) [US-WAS5-018]:
  - The DCS income withholding order takes **priority over any garnishment**.
  - Cap: 50% of disposable earnings per period.
  - Remit to the WA state support registry within **7 working days** of payday.
  - Answer within 20 days.
  - Employer processing fee: up to **USD 10 for the first disbursement and USD 1 for each later one**.
  - The federal IWO form is used.
- **State tax levies on wages:** none relevant, because there is no income tax. ESD and L&I collection orders were not researched.

## 10 — collective_agreements (prevailing wage)
- **RCW 39.12** [US-WA-P5-1-002 (39.12.020); US-WAS5-010]:
  - The prevailing rate applies on public works and public building service maintenance contracts.
  - A statement of intent is required on contracts over USD 10,000.
  - Certified payroll is filed **at least monthly** in the L&I online system.
  - Records are kept 3 years: SSN, classification, straight and overtime rates, the hourly rate of usual benefits, daily and weekly hours, gross pay, itemized deductions and net pay.
- **Private sector:** WA CBAs can override some rules, such as the pay interval (WAC 296-126-023(8)) and final-pay timing (49.48.010(2)). No sector CBA sets statutory payroll minima.

## 11 — indexation (what is indexed, and where the new value is published)

| Item | Mechanism | Publication | Rows |
|---|---|---|---|
| State minimum wage | CPI-W, Aug-to-Aug, announced Sept 30, effective Jan 1 | L&I release (26-17 for 2027) | US-WAS5-001/006/007 |
| Youth minimum, exempt salary threshold, computer-professional hourly rate, non-compete thresholds | multiples of the minimum wage (85%, 2.25/2.5x x 40, 3.5x), or CPI-W | the same L&I release | US-WAS5-005/007 |
| Consumer-debt garnishment exemption | 35x the state minimum wage (moves with it automatically) | — | US-WAS5-009 |
| Local minimum wages | each city's own ordinance (mostly CPI-W) | city sites; L&I summary | US-WAS5-008 |
| UI wage base | average WA wages (RCW 50.24.010, not read) | ESD tax-rate page | US-WAS5-012 |
| PFML wage cap | equals the SSA wage base | SSA (FED unit) | US-WAS5-011 |
| PFML rate | formula, set around Oct 20, capped at 1.20% | ESD release | US-WAS5-011/015 |
| WA Cares | fixed at 0.58%, not indexed | — | US-WAS5-016 |
| Workers' comp | set annually by L&I rule (proposed in autumn, final in December) | L&I | US-WAS5-019 |
| Seattle PET thresholds | indexed by the city | — | US-WAP7-005 |

## 12 — data_protection
- **Breach notification** (RCW 19.255.010) [US-WAS5-025]:
  - Notify affected residents within 30 calendar days of discovery.
  - Notify the Attorney General if more than 500 WA residents are affected.
  - A processor must notify the data owner immediately. This covers payroll providers.
- **SSN on pay statements:** no WA rule was located that requires or forbids SSN truncation on a pay statement. WAC 296-126-040 has no SSN element.
  - SSNs are *required* in ESD records (copy of the card), in the UI report, in new-hire reports and in public-works certified payroll [US-WAS5-030, -013, -018, -010].
  - Absence was read only in the pay-statement rule. A general WA SSN-display statute was not searched. Open question; low impact.
- **Personnel files:** the employee may inspect them within 21 days of a request (WAC 296-126-050(3)) [US-WAS5-004].

## 13 — live_legal_change (2026-01-01 to 2026-11-02, and enacted for 2027 or later)

| Change | Effective | Status | Operating level | Row |
|---|---|---|---|---|
| Minimum wage 17.73; exempt threshold 2.5x (51+ employees); youth 15.07; computer professionals 62.06 | 2027-01-01 | in force (announced 2026-09-30) | payroll rate tables | US-WAS5-007 |
| Everett and Renton mid-year local minimum wage steps | 2026-07-01 | in force | payroll | US-WAS5-008 |
| PFML premium 1.2%, split 29.3 / 70.7 | 2027-01-01 | in force (ESD 2026-10-16) | withholding | US-WAS5-015 |
| 2SHB 2345 (c 26, Laws 2026): family/medical premium allocation | in force 2026-06-11; applied to 2027 premiums | enacted | withholding split and Paid Leave report | US-WAS5-020 |
| PFML job protection at 25+ (2026), 15+ (2027), 8+ (2028) employees; 180-day tenure | 2026-01-01 | in force | leave administration | US-WAS5-028 |
| WA Cares: non-immigrant visa holders auto-exempt; private-LTC exemptees may rejoin until 2028-06-30 | 2026-01-01 | in force | withholding eligibility | US-WAS5-024 |
| SHB 2355 (c 15, Laws 2026): Domestic Workers Bill of Rights | 2027-07-01 | enacted, not yet in force | labour standards / termination notice | US-WAS5-021 |
| Non-compete ban | July 2027 | per L&I release; statute not read | not payroll | US-WAS5-007 |
| SB 6346: 9.9% tax on AGI above USD 1M | 2028-01-01 | enacted | **assessment** (no withholding stated) | US-WAS5-017, US-WA-PIT-001 |
| Workers' comp 2027 rates | 2027-01-01 | proposed only | payroll deduction per hour | US-WAS5-019 |
| UI wage base 2027 | 2027-01-01 | not yet published | UI | US-WAS5-012 |

The bulletin sweep for this unit covered the ESD news releases to 2026-10-27, L&I release 26-17, and the session-law banners found on RCW 49.46.010 (2355-S) and 50A.10.030 (2345-S2). A full sweep of the 2026 WA session laws was **not** done. Next-year note: the ESD 2027 UI wage base and rate notice are due in December, and the L&I final 2027 workers' comp rates are also due in December.

## Special populations (state level)

| Population | WA rule | Rows |
|---|---|---|
| Domestic / household workers | Casual labour in a private home is excluded from the MWA (49.46.010(4)(b)). From 2027-07-01, SHB 2355 requires minimum wage, overtime over 40 h, a written agreement and termination notice. UI: domestic wages are reported once USD 1,000 is paid in a quarter, then for the whole year. | US-WAS5-001, -021, -013 |
| Agricultural | Overtime over 40 h from 2024. A narrow exclusion from the MWA for piece-rate hand harvesters (49.46.010(4)(a)). Minors in agriculture are outside WAC 296-128-400. | US-WAS5-001, -005 |
| Minors | 14-15 year olds: 85% of the minimum wage. 16-17 year olds: the full state rate (per the L&I page). Prohibited occupations under 14 (WAC 296-128-400). | US-WAS5-006, -005 |
| Tipped employees | No tip credit. All tips and service charges go to the employee. UI wages include reported tips; PFML wages exclude tips. | US-WAS5-001, -022, -023 |
| Clergy / religious | Volunteers for religious bodies are not "employees" where there is no real employment relationship (49.46.010(4)(d)). The WA UI exemption for clergy was not read. | US-WAS5-001 (UI: open) |
| Students | A student-learner certificate allows a sub-minimum wage (WAC 296-128-175 to -215, by certificate). The UI student exemption was not read. | US-WAS5-005 (UI: open) |
| Nonresident aliens | No state income tax. WA Cares: non-immigrant visa holders auto-exempt from 2026-01-01 (opt-in allowed). PFML: no visa exemption located. | US-WAS5-024 |
| Corporate officers | Exempt from UI by default for for-profit corporations. Written notice is required; FUTA is paid at the full rate; coverage is optional. | US-WAS5-027 |
| Statutory employees | No WA-specific rule located beyond federal. | — (no state rule located; not specifically searched) |
| Government employees | Elected and appointed officials and legislature staff are excluded from the MWA (49.46.010(4)(l)). Public-employer overpayment rules apply (49.48.200-.210). Fire and police overtime work periods (49.46.130(5)). | US-WAS5-001, -002 |
| Apprentices / learners / workers with disabilities | A sub-minimum wage needs a special certificate (49.46.060; WAC 296-128-100 to -315). | US-WAS5-001, -005 |
| Construction workers | Accrued sick leave is paid out at separation before the 90-day eligibility point (49.46.210(1)(l)). | US-WAS5-001 |

## ACCESS gaps (exact URLs)
- `https://paidleave.wa.gov/employer-roles-responsibilities/`: HTTP 403 directly. The Wayback copy `https://web.archive.org/web/2026id_/https://paidleave.wa.gov/employer-roles-responsibilities/` also returns 403 (snapshot 20260916). This blocks the PFML/WA Cares quarterly report field list and the 2026/2027 family-medical split tables.
- `https://www.seattle.gov/` (all paths): TLS failure (`SEC_E_INVALID_TOKEN`). The Wayback copy `https://web.archive.org/web/2026id_/https://www.seattle.gov/laborstandards/ordinances/minimum-wage` returns 403. This blocks Seattle's 2027 minimum wage, Paid Sick and Safe Time, and the PET 2027 thresholds.
- `https://app.leg.wa.gov/` and `https://lawfilesext.leg.wa.gov/`: TLS failure. Handled through Wayback `id_` snapshots (see Access findings). Before stage 1 consumes them, the synthesis should re-verify the RCW 26.23 snapshot (2025-09) against the live site through the browser pass.
- `https://lni.wa.gov/insurance/premiums/report-pay-premiums/`: 404. This was a guessed URL; the L&I quarterly report page was not located.

## Open questions

Mirrors `unresolved[]` of the facts file (same keys, same wording).

- **wa.meta.register_id_pattern** (blocking): 1 facts rest on active register rows whose ids (US-WA-P5-1-001) do not match the facts-schema register_id pattern ^[A-Z]{2}-[A-Z0-9]{2,12}-[0-9]{3,4}$ (multi-hyphen legacy ids). They are carried in full in _facts_pending_register_id_pattern and are NOT yet consumable facts. What would close it: Orchestrator decision: a PATCH of facts.schema.json loosening the register_id pattern (e.g. ^[A-Z]{2}-[A-Z0-9-]{2,16}-[0-9]{3,4}$), or register alias ids; then run _research/synthesis-B/_work-MN-WY/promote.py to move the pending facts into facts[].
- **wa.labour.minwage.local.next_year** (blocking): 2027 local minimum wages not obtained (seattle.gov blocked). What would close it: Each city's 2027 rate notice or the updated L&I local-rates page.
- **wa.ui_pfml_ltc.deferrals** (blocking): Whether 125/401(k)/HSA deferrals are excluded from UI, PFML and WA Cares wages is unanswered. What would close it: WAC 192-310-030, chapter 192-510 WAC, chapter 192-910 WAC / 50B.04 RCW.
- **wa.report.pfml_ltc.fields** (non-blocking): PFML/WA Cares quarterly report fields and deadline not re-read (paidleave.wa.gov 403). What would close it: paidleave.wa.gov Employer Help Center report guide (browser pass).
- **wa.sui.wage_base.next_year** (non-blocking): 2027 UI wage base not published. What would close it: ESD tax-rate page (December) and RCW 50.24.010.
- **wa.wc.next_year_and_statute** (non-blocking): Final 2027 WC rates and RCW 51.32.073 not read. What would close it: L&I 2027 adopted rates (December) and RCW 51.32.073.
- **wa.pit.sb6346_text** (non-blocking): SB 6346 text not read to confirm no withholding clause before 2028. What would close it: The session law text.
- **wa.term.notices** (non-blocking): State mini-WARN and ESD separation-notice rules not read. What would close it: WA mini-WARN statute and RCW 50.20 / WAC 192.
- **wa.term.vacation.payout** (non-blocking): Vacation payout at separation: L&I policy not read. What would close it: L&I ES.B administrative policy.
- **wa.labour.paycard** (non-blocking): Direct deposit/paycard consent rule not read. What would close it: L&I policy or RCW search.
- **wa.garn.student_loan_wage_meaning** (non-blocking): "Highest minimum wage law in the state" (6.27.150(3)(a)): state vs local rate unresolved. What would close it: Court or AG reading.
- **wa.ui.exclusions_clergy_students** (non-blocking): UI exclusions for clergy and students (50.44.040) not read. What would close it: RCW 50.44.040.
- **wa.pfml.family_medical_split** (non-blocking): 2027 family/medical line split under 2SHB 2345 derived only (medical 51.95%/53.27% of premium); ESD tables not readable. What would close it: ESD/paidleave.wa.gov premium split tables.
