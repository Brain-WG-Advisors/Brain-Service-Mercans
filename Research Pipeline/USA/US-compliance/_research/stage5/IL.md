# Stage 5 — IL (Illinois): 13-domain findings

Worker: compliance-source-hunter, 2026-11-02 (07:10–07:30 local). Budget declared: 60 fetches / 2 h; stopped acquiring at about 48 fetches (past the 75% line, see the "Budget" note at the end).
Register shard: `00-official-sources/_register-shards/S5-IL.csv` (26 rows, US-ILS5-001..026; 6 A.1, 15 A.2, 5 A.3; 25 active, 1 partial; no tier-B row).
Source files: `00-official-sources/ccg-sources/IL/` (27 files, 3.8 MB).
Rows from earlier passes reused, not re-fetched: US-ILR3-001 (IL-700-T), US-ILR3-002 / US-ILP51-001 (Pub-130), US-IL-002 (IDES rates), US-ILP52-001 (no local tax), US-ILP52-002 (Secure Choice), US-ILP52-003 (PLAWA, not a levy), US-ILP52-004 (prevailing wage), US-IL-004 / P5-2-005 / P5-2-009 / P5-2-010 (POA), US-MULTI-018 (IA reciprocity), US-ILP9L-001 (posters / languages).

**Re-verification of the MANUAL part-1 blocker (US-MQ-34).** The IL-700-T booklet was fetched directly with curl on 2026-11-02 from `tax.illinois.gov/.../currentyear/il-700-t.pdf`. It is byte-identical (cmp) to the local file behind US-ILR3-001 (`pdfs/IL/il-700-t_2026_webfetch-20261029.pdf`), so the duplicate was not kept. Its text confirms: R-12/25, effective 2026-01-01, rate 4.95%, Line 1 allowance $2,925, Line 2 allowance $1,000. The worked example also checks out: $800 a week with 2+2 allowances gives $32.13 withheld. US-ILR3-001 can be stamped verified_on 2026-11-02 at merge.

**Access finding for the orchestrator.** ilga.gov answers 403 ("Automated Request Blocked") to curl, and Wayback answered 429 during this pass. The 403 page itself points automated clients to the **ILGA public file repository, `https://ftp.ilga.gov/ILCS/`**, which is synchronised nightly and reachable with plain curl (A.1). Path pattern: `ftp.ilga.gov/ILCS/Ch%20{CCCC}/Act%20{AAAA}/{CCCC}{AAAA}0K{section}.html`, for example `.../Ch%200820/Act%200115/082001150K10.html`. Admin Code: `ftp.ilga.gov/JCAR/`. Every remaining Illinois statute or rule gap in this file can be closed through this route without the browser.

---

## 1 — Labour code
- **State minimum wage:** $15.00/h for workers aged 18+ since 2025-01-01. The statute has no later step and no indexation [US-ILS5-001 A.1, US-ILS5-002 A.2].
  - Under 18 working ≤ 650 h/calendar year: $13.00.
  - New hire, first 90 consecutive days: may be paid up to $0.50 less (not day/temporary laborers).
  - Tip credit: up to 40%, so tipped cash wage = $9.00.
  - No 2027 rate is enacted in 820 ILCS 105/4.
- **Local minimum wages:**
  - **Chicago**, from 2026-07-01 to 2027-06-30, employers with 4+ employees: $17.05; tipped $12.96; City contracts $18.50 [US-ILS5-008 A.2]. Indexed every July 1 by CPI, capped at 2.5%. Arithmetic: 17.05 × 0.76 = 12.958 → 12.96.
  - **Suburban Cook County**, from 2026-07-01: $15.40; tipped $9.25; overtime $23.10 / tipped OT $16.94. Covers employees over 18 who work ≥ 2 h/week in the County. Chicago and opted-out municipalities are excluded [US-ILS5-009 A.2]. Derivations: 15.40 × 1.5 = 23.10; 23.10 − 0.40 × 15.40 = 16.94 (matches); 0.60 × 15.40 = 9.24, against the published 9.25.
- **Overtime:** 1.5× the regular rate over 40 h/workweek (820 ILCS 105/4a). Exemptions in 4a(2) include agricultural labor, FLSA EAP employees and 7(i) commissioned employees [US-ILS5-001]. No daily overtime rule.
- **Coverage (105/3):** an employer with fewer than 4 employees is outside the Minimum Wage Law, except for domestic workers. Also excluded: small-farm agricultural workers, outside salesmen, members of religious organisations, students employed by their own college, DOT motor-carrier drivers [US-ILS5-026 A.1].
- **Pay frequency:** at least semi-monthly, paid within 13 days after the end of the pay period. EAP employees and commissions may be paid monthly (115/3) [US-ILS5-003 A.3].
- **Method of payment:** the employer cannot impose direct deposit (it must be voluntary). Cash requires a signed receipt [US-ILS5-005 A.3].
  - Payroll card: voluntary, with written fee disclosure and a free-fee regime; consent can be revoked [US-ILS5-007 A.2].
  - An employer that offers card or direct deposit must also offer cash or check (115/4, 115/14.5).
- Confidence: high (statute + authority page for every number).

## 2 — Income tax
- **Method:** flat 4.95% on (wages − exemptions). Annual exemptions = IL-W-4 Line 1 × $2,925 + Line 2 × $1,000, divided by the number of pay periods. IL-W-4 Line 3 extra amount is added. Booklet IL-700-T R-12/25, effective 2026-01-01 [US-ILR3-001, re-verified today].
  - No separate supplemental rate: bonus, overtime and commission are wages [US-ILR3-002].
  - No rounding rule; the tables are in cents [US-ILR3-001].
- **Certificate:** Form IL-W-4, edition R-07/23, is still the current-year form [US-ILS5-010 A.2].
  - No exemptions if AGI exceeds $500k (joint) / $250k (other).
  - No IL-W-4 on file: withhold on the full amount with no exemptions.
  - Changes take effect at the next quarter date (Jan 1, Apr 1, Jul 1, Oct 1) that is at least 30 days after filing.
- **Reciprocity:** IA, KY, MI and WI residents use IL-W-5-NR; military spouses are also excluded [US-ILP51-001, US-ILS5-014].
- **Nonresident / sourcing:**
  - Withholding applies to compensation "paid in Illinois" (service localized in IL).
  - No withholding for a nonresident with fewer than 31 days of service in IL whose service is not localized in IL. Nonresidents expected to work more than 30 days in IL need an IL-W-6 certificate of days on file.
  - Special rules for STB carriers, air carriers (>50% of flight miles in IL) and vessels.
  - An IL resident working only in another state that withholds: no IL withholding; credit on the return [US-ILS5-014 A.2].
- **Local income tax:** none administered by IDOR [US-ILP52-001].
- **2027:** no 2027 IL-700-T or rate change found. The 4.95% rate is statutory (35 ILCS 5/201, not read this pass, see Open questions).
- Film production / loan-out withholding: P.A. 104-0453, for projects from 2025-12-12 (FY 2026-16) [US-ILS5-014].
- Confidence: high.

## 3 — Social security (UI / SDI / PFML / levies)
- **IDES 2026 UI rates** [US-ILS5-015 A.2, direct copy; same values as US-IL-002]:
  - Wage base $14,250 (2025: $13,916).
  - New / standard (ineligible) employer 3.350%; Administrative Support & Waste Management 3.450%.
  - Range 0.750%–7.050%, fund builder 0.550% included.
  - Small-employer option 5.4% (gross wages < $50k). State experience factor 102%.
  - No employee contribution.
- **SDI/TDI/PFML:** none. PLAWA is an employer-provided benefit, not a premium [US-ILP52-003].
- **Levies:** Secure Choice Roth IRA payroll deduction [US-ILP52-002]. No other levy (P7/P9 list not redone).
- The 2027 wage base is not yet published (IDES usually publishes in December; see domain 11).
- Confidence: high.

## 4 — Payslip statute
- **820 ILCS 115/10 as amended by P.A. 103-953 (eff. 2025-01-01)** [US-ILS5-024 A.1]:
  - Written notice at hire of the rate of pay and the time and place of payment.
  - Records of names, addresses and wages paid each payday; a pay stub each pay period.
  - Pay stubs kept **at least 3 years**, whether paper or electronic.
  - Copies within 21 days on request, at most twice per 12 months. Former employees can ask for one year after separation, in the format they choose.
  - If electronic stubs become inaccessible after separation, the employer must offer the prior year's stubs by the end of the final pay period and record that offer.
- **Content:** itemized statement of deductions each pay period [US-ILS5-005]. Payroll-card payees must also get hours worked, rate of pay and deductions [US-ILS5-007].
- Electronic delivery is allowed, as 115/10(c) contemplates electronic stubs. No separate consent rule for electronic stubs was found.
- **Language:** none required [US-ILP9L-001, MANDATE US-OWN-006].
- Confidence: medium-high. The full content list in 56 Ill. Adm. Code 300.600 was not read (closable via ftp.ilga.gov/JCAR).

## 5 — Reporting instruments
- **IL-941 quarterly**, due the last day of the month after the quarter. Illinois has **no annual reconciliation**. IL-941 must be filed electronically (MyTax or approved software) [US-ILS5-011 A.2].
- **2026 due dates:** Q1 04-30, Q2 07-31, Q3 11-02, Q4 2027-02-01 [US-ILS5-012 A.2].
- **Deposits:**
  - Monthly (15th of the following month) when look-back liability ≤ $12,000.
  - Semi-weekly (federal Wed/Fri rule) when look-back > $12,000, or from the quarter after $12,000 is exceeded. Semi-weekly payers must pay electronically.
  - Payment voucher IL-501.
- **W-2 to IDOR:** electronic only. Methods: MyTax (manual entry, CSV or EFW2 upload under IDR-996) or bulk EFW2 with an ETIN under IDR-986.
  - Due January 31; **2026 W-2s by 2027-02-01**. A federal extension applies automatically.
  - 1099/W-2G bulk filing moved to IRIS (IDR-987) from 2026-09-18 [US-ILS5-013 A.2].
- **UI-3/40 quarterly wage report + contributions:** due Apr 30 / Jul 31 / Oct 31 / Jan 31 [US-ILS5-016 A.2].
- **Monthly wage report:** required for employers with ≥ 25 employees in the prior year (P.A. 97-0689). Months 1 and 2 of each quarter; name, SSN and wages only; MyTax CSV upload only [US-ILS5-017 A.2].
- **New hire:** to IDES within 20 days of the first day on payroll. Includes rehires and independent contractors. Data: name, address, SSN, hire date, employer name/address/FEIN, optional IWO address [US-ILS5-018 A.2].
- POA / service bureau: existing rows [US-IL-004, US-ILP52-009/-010].
- Confidence: high. The IDR-986 EFW2 Illinois specification itself was not downloaded (RSPEC stage).

## 6 — Leave
- **PLAWA (820 ILCS 192, eff. 2024-01-01)** [US-ILS5-019 A.3]:
  - 1 h per 40 h worked, up to 40 h per 12 months (frontloading allowed); usable after 90 days, for any reason.
  - Exempt employees are deemed to work 40 h/week.
  - Carryover allowed, but not for frontloaded leave. Year-end payout only by annual written agreement (56 IAC 200.320(d)).
  - **No payout at separation unless the leave sits in a vacation/PTO bank.** Frontloaded leave cannot be recouped.
  - Tipped and commissioned employees are paid at least the full minimum wage while on leave.
  - PLAWA does not apply in Chicago or Cook County.
- **Chicago Paid Leave + Paid Sick Leave:** covers anyone working ≥ 80 h in 120 days. Accrual is 1 h paid leave **and** 1 h paid sick leave per 35 h worked, from day 1. Notice with the first paycheck and annually around July 1 [US-ILS5-020 A.2, **partial**]. Caps, carryover and the employer-size payout rule are not obtained (FAQ PDF 403).
- Cook County Paid Leave Ordinance: not read (see ACCESS / Open questions).
- Confidence: medium (state high; Chicago partial; Cook missing).

## 7 — Termination
- Final compensation in full at separation if possible, **no later than the next regularly scheduled payday**, whether the employee was discharged or resigned. Paid by mailed check if the employee asks in writing (115/5) [US-ILS5-023 A.1, US-ILS5-003].
- **Earned vacation must be paid at the final rate of pay and cannot be forfeited** (CBA exception). Pro-rata accrual, IDOL worked examples [US-ILS5-004 A.3].
  - Use-it-or-lose-it is allowed during employment if the employee had notice and a reasonable opportunity (56 IAC 300.520).
- No statutory severance [US-ILS5-003].
- IDES lists "Employee Separation Information" as an employer obligation [US-ILS5-018]. The form or notice to the employee at separation was **not identified**.
- Confidence: high for final pay and vacation; low for the separation notice.

## 8 — Benefits in kind
- IL withholding follows federal: wages "from which federal income tax is required to be withheld" [US-ILR3-002]. The IL base starts from federal AGI, so federal exclusions (401(k), §125, HSA, transit, GTL) follow automatically.
- No Illinois departure from federal was found in any document read. A departure is not proven absent: no IDOR conformity bulletin was read.
- Confidence: medium.

## 9 — Deductions & garnishments
- **Wage deductions:** only when required by law, for the employee's benefit, or under a wage assignment/order or express written consent given at the time of the deduction (recurring-consent rule 300.720) [US-ILS5-006 A.3].
  - No deductions for shortages, damage or uniforms without that consent; no holding back pay until equipment is returned.
  - Cash advances: repayment at most 15% of wages per paycheck. Overpayment rules in 115/9.
- **Creditor wage deduction (735 ILCS 5/12-803)** [US-ILS5-022 A.1]: lesser of 15% of **gross** or disposable earnings − 45 × the greater of the federal or IL minimum wage. 2026 floor: 45 × 15 = **$675/week**. This is stricter than the federal CCPA 25%.
- **Child support IWO (HFS)** [US-ILS5-021 A.2]:
  - Form HFS 3683; **$5/month** employer fee, deducted from the employee's remaining income.
  - Remit 1–7 business days after payday; up to 50% of disposable income.
  - Multiple orders for different children: allocate pro rata under Illinois law, not first-come first-served.
- State tax levies (IDOR wage levy): not read.
- Confidence: medium-high.

## 10 — Collective agreements / prevailing wage
- Prevailing Wage Act 820 ILCS 130: public works; IDOL county rates; certified payroll portal [US-ILP52-004, existing]. Not re-fetched this pass.
- A CBA can override the vacation-payout rule (115/5) [US-ILS5-023].

## 11 — Indexation
| Item | Indexed? | Publication |
|---|---|---|
| State minimum wage | No (fixed at $15 from 2025-01-01) [US-ILS5-001] | — |
| Chicago minimum wage | Yes, every July 1, CPI capped at 2.5% [US-ILS5-008] | BACP page / notice |
| Cook County minimum wage | Yes, every July 1, greatest of federal / IL / County CPI calculation; CPI step suspended if County unemployment ≥ 8.5% [US-ILS5-009] | CCHR FAQ / notice |
| UI wage base | Yes, annual (14,250 for 2026) [US-ILS5-015] | IDES rate chart (statutory formula 820 ILCS 405/235 not read) |
| PIT exemption $2,925 | Indexed by IDOR (2,925 in 2026) [US-ILR3-001] | IL-700-T booklet |
| Garnishment floor | Follows the minimum wage (45×) [US-ILS5-022] | — |

Derivation lines are in domains 1 and 9 above. A Chicago CPI derivation was not possible because the 2025 Chicago rate is not registered.

## 12 — Data protection
- **BIPA 740 ILCS 14/15:** written retention/destruction policy (≤ 3 years after the last interaction); notice plus a written release before collection; no sale; limits on disclosure. Relevant to biometric time clocks [US-ILS5-025 A.1].
- No Illinois rule was found that requires SSN truncation on pay stubs. Absence is not proven: the Personal Information Protection Act and 815 ILCS 505 SSN-use provisions were not read.
- Confidence: medium-low.

## 13 — Live legal change (2026-01-01 to today)
| Change | Status | Level | Effective | register_id |
|---|---|---|---|---|
| Chicago minimum wage $17.05 / tipped $12.96 | in force | wages / payroll | 2026-07-01 | US-ILS5-008 |
| Cook County minimum wage $15.40 / tipped $9.25 | in force | wages / payroll | 2026-07-01 | US-ILS5-009 |
| IDOR 1099/W-2G bulk transmission moved to IRIS; re-registration | in force | employer reporting | 2026-09-18 | US-ILS5-013 |
| P.A. 104-0453 film production / loan-out withholding responsibilities | in force | withholding | projects from 2025-12-12 | US-ILS5-014 |
| IL-W-4 edition unchanged (R-07/23); IL-700-T R-12/25 | in force | withholding | 2026-01-01 | US-ILS5-010, US-ILR3-001 |
| 14(c) sub-minimum licences end | enacted, future | wages | 2029-12-31 | US-ILS5-002 |
| P.A. 103-953 pay-stub copy rules (115/10) | in force (earlier, 2025) | payslip | 2025-01-01 | US-ILS5-024 |

No 2027 enactment was located. The IDOL, IDOR and IDES news pages were **not swept** in this pass (budget). See Open questions.

## Special populations (US-OWN-005, state round)
| Population | Illinois rule | register_id |
|---|---|---|
| Domestic / household workers | Covered by the Minimum Wage Law even with fewer than 4 employees (Domestic Workers' Bill of Rights). IL withholding not required unless the employer withholds federal tax under a voluntary agreement, in which case IL withholding is required. Report on IL-1040 Line 20 or IL-941 (Pub. 121). | US-ILS5-026, US-ILS5-014 |
| Agricultural | No state overtime (105/4a(2)C). Small farms (≤ 500 man-days in any quarter), family and some piece-rate hand harvesters are outside the minimum wage. UI agricultural coverage not read. | US-ILS5-001, US-ILS5-026 |
| Minors | Under 18 working ≤ 650 h/year: $13.00; above that, the adult rate. Cook County ordinance does not apply under 18. | US-ILS5-001, US-ILS5-009 |
| Tipped | State cash wage $9.00 (60%); Chicago $12.96; Cook $9.25. PLAWA leave paid at the full minimum wage. | US-ILS5-001/-008/-009/-019 |
| Clergy / religious | Members of religious organisations are outside the Minimum Wage Law. No IL withholding where compensation is exempt from federal withholding (ministers). | US-ILS5-026, US-ILS5-014 |
| Students | Students employed by their own college are outside the Minimum Wage Law; part-time college students employed by their school are exempt from PLAWA. UI student exclusion not read. | US-ILS5-026, US-ILS5-019 |
| Nonresident aliens | No state rule beyond federal located. IL withholding attaches to wages subject to federal withholding (Pub-130 read). | US-ILR3-002 |
| Statutory employees | No state rule located. IL follows federal withholding (Pub-130 read); not proven. | US-ILR3-002 |
| Government employees | IWPCA excludes State and federal employees (local government covered). Minimum Wage Law covers governmental bodies; 4a(2)D overtime carve-out. IL withholding applies. UI: reimbursement option. | US-ILS5-003, US-ILS5-001, US-ILS5-016 |
| Nonresidents (other states) | Reciprocity IA/KY/MI/WI; 30-day threshold; IL-W-6. | US-ILS5-014 |

---

## ACCESS gaps (exact URLs)
1. `https://www.chicago.gov/content/dam/city/depts/bacp/OSL/faqpaidandpaidsickleave10022025.pdf`: 403 Access Denied (Akamai). Wayback `web.archive.org/web/2026id_/...` returned 404. Holds Chicago Paid Leave caps, carryover and the employer-size payout rule.
2. `https://www.chicago.gov/content/dam/city/depts/bacp/OSL/faqminimumwage09302025.pdf`: 403 (Chicago minimum wage FAQ; tipped phase-out schedule).
3. `https://www.cookcountyil.gov/content/cook-county-minimum-wage`: 404 (the FAQ PDF was obtained instead). The Cook County Paid Leave Ordinance page was not attempted.
4. `https://web.archive.org/web/2026id_/https://www.ilga.gov/legislation/ilcs/ilcs3.asp?ActID=2402&ChapterID=68` (IWPCA full act): 404. ilga.gov returns 403 to automated clients. **Workaround found: `https://ftp.ilga.gov/ILCS/`** (used for US-ILS5-022..025).
5. `https://labor.illinois.gov/faqs/paid-leave-for-all-workers-faq.html`: 404 (the correct URL `/faqs/paidleavefaq.html` was obtained).
6. archive.org availability API: 429 Too Many Requests (rate-limited during this pass).

## Open questions
- `il.leave.chicago.paid_leave.payout`: Chicago paid-leave payout at separation by employer size, annual caps and carryover. **Would close it:** the BACP FAQ PDF above or the OLS Paid Leave rules (Chicago rules portal) via the browser pass, or MCC 6-130 from the Chicago municipal code.
- `il.leave.cook.paid_leave`: Cook County Paid Leave Ordinance (accrual, cap, payout). **Would close it:** the Cook County Commission on Human Rights Paid Leave FAQ (cookcountyil.gov).
- `il.minwage.chicago.tipped.schedule`: the page gives tipped $12.96 = 76% of $17.05. The One Fair Wage ordinance phase-out percentage for 2026 was not read, so it is unclear whether the phase-out is paused. **Would close it:** MCC 6-105-020 text or the BACP 2026 notice.
- `il.termination.ui_separation_notice`: whether Illinois requires a notice to the employee at separation (IDES leaflet). **Would close it:** 56 Ill. Adm. Code 2770 / 820 ILCS 405 via ftp.ilga.gov, or the IDES employer handbook.
- `il.pit.rate.statutory`: confirm 35 ILCS 5/201(b)(5.4) 4.95% and the absence of a 2027 change. **Would close it:** `ftp.ilga.gov/ILCS/Ch%200035/Act%200005/` section 201, plus the IDOR news page.
- `il.ui.wage_base.2027` and the 820 ILCS 405/235 indexing formula. **Would close it:** the IDES 2027 rate chart (expected December 2026) and 405/235 via ftp.ilga.gov.
- `il.payslip.content.list`: 56 Ill. Adm. Code 300.600 content items. **Would close it:** `ftp.ilga.gov/JCAR/` Title 56 Part 300.
- `il.data.ssn_paystub`: whether any Illinois rule restricts SSN on pay statements. **Would close it:** 815 ILCS 505/2RR and 815 ILCS 530 via ftp.ilga.gov.
- `il.bik.conformity`: a formal IDOR statement on decoupling (e.g., HSA, 125). **Would close it:** IDOR Pub. 101 / the IL-1040 instructions subtraction list.
- `il.live.news_sweep`: the IDOL, IDOR and IDES newsrooms 2026-01-01..today were not swept (budget). **Would close it:** one sweep of `tax.illinois.gov/research/news.html`, `labor.illinois.gov/news.html` and `ides.illinois.gov/resources/newsroom.html`.

## Budget
About 48 fetches against the declared 60 (ceiling 45 at 75%); wall clock about 20 min of 2 h. I went past 45 by 3 to read four A.1 statute sections once the ftp.ilga.gov route turned up, then stopped. The remaining work is independent lookups: Chicago and Cook leave via the browser pass, 4–6 ftp.ilga.gov statute reads, and one newsroom sweep. It can be fanned out.
