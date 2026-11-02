# Stage 5 — AR (Arkansas): findings across the 13 domains

Worker: compliance-source-hunter, 2026-11-02. Budget declared: 60 fetches / 2 h (stop at 45 / 1 h 30). Used about 35 network calls (fetches + searches + Wayback/CDX lookups) and about 20 minutes, under the 75% mark.

Outputs:
- Register shard: `00-official-sources/_register-shards/S5-AR.csv`, rows US-ARS5-001..014 (13 active, 1 MANUAL).
- Sources: `00-official-sources/ccg-sources/AR/`, 15 files, about 5.1 MB. No single file is over 1 MB.

**Access.** The VPN was off (BR exit). How each host behaved:
- dfa.arkansas.gov, labor.arkansas.gov, sos.arkansas.gov and senate.arkansas.gov work with plain curl.
- arkleg.state.ar.us fails at TLS (curl exit 35). Acts were read from Wayback `id_` copies.
- myworkers.ocse.arkansas.gov (OCSE employer guide) returns 403, and there is no Wayback copy.

**Reused active rows (not re-fetched):**
- US-ARWH-001/-002: formula and branch page. The formula now also has a local file, as US-ARS5-001.
- US-ARP51-002: 2026 employer instructions (local; read in full this run).
- US-ARP51-003, US-ARP9V-001 (DWS Employer Handbook, local; read for new hire, quarterly report, localization) and US-ARP9V-002: UI.
- US-ARP9V-003: DFA tax list, no local income tax.
- US-ARP51-004 and US-ARL-001: 2008 wage-hour compilation.
- US-ARP52-001: other-state credit.
- US-ARP52-002: HB1116 of 2025 died.
- US-ARP52-003: POA.
- US-ARP52-006: 11 CAR Part 11, 2026-07-21 compilation, local.
- US-ARP52-007: DOL paid-leave list.
- US-ARP51-001: prevailing wage repealed in 2017.
- US-ARP9L-001: required postings.

## MULTI hand-off (MULTI-OQ-5): convenience rule — ANSWERED from the primary text
- **Act 1019 of 2021 (SB 484)** [US-ARS5-006, A.1, inspected directly]. Status: in force; approved 2021-04-29 with an emergency clause. Level: assessment and withholding.
  - 26-51-202(c): a nonresident pays AR tax only on income reasonably allocable to work performed in AR. A nonresident performs work in AR when **physically located** in AR while working. This ends convenience-of-employer sourcing, effective for tax years from 2021-01-01.
  - 26-51-504(a)(1): the resident credit for tax owed to another state is capped at the AR tax on that income. Income for work physically performed in AR is not "outside income".
  - 26-51-902(5): an out-of-state person who controls payment of wages for services performed in AR is an "employer" for withholding.
- **No day or dollar threshold.** HB1116 of 2025 (15 days / USD 2,500) died in committee [US-ARP52-002]. The 2026 instructions apportion a nonresident's wages by AR working days over total working days. Sales-volume-paid staff are apportioned by sales negotiated in AR [US-ARP51-002].
- **SUI wage-base credit (MULTI-OQ-2).** Arkansas gives a credit against its USD 7,000 base for wages paid toward the former state's base in the same calendar year when an employee permanently moves to AR with the same employer. Handbook example: MO wages 6,000 in Q1, so only 1,000 is AR-taxable in Q2 [US-ARP9V-001, A.3].
  - Localization follows the four-step test: only AR; only another state; primarily AR; equal → base of operations or the state of direction and control [US-ARP9V-001].
- **PFML/SDI coverage (MULTI-OQ-3):** not applicable. AR has no SDI, TDI or PFML programme [US-ARP52-007].
- **Paid-sick-leave coverage (MULTI-OQ-4):** not applicable. No AR paid-sick-leave statute was located (see §6).
- **Pay-statement reach (MULTI-OQ-8):** not applicable. AR has no itemised pay-statement statute [US-ARP52-006, US-ARP51-004].

## 1 — labour_code
- **Minimum wage:** **USD 11.00/h from 2021-01-01** (2018 Initiated Act, Issue 5). It applies to employers with **4 or more employees**. Where FLSA also covers the employer, the higher rate is paid [US-ARS5-002, A.2, high].
  - No 2027 increase is enacted. The 2026-11-03 ballot carries no citizen initiative (the SOS lists "None"); Issues 1–4 are non-payroll referrals [US-ARS5-004, A.2, high].
  - There is no local minimum wage on the DOLL page. Confidence medium: no statute preempting local wages was read.
- **Overtime:** 1.5× the regular rate over 40 h per workweek. There is no daily overtime. Agricultural employees and FLSA-exempt employees are excluded (11-4-211) [US-ARS5-002; US-ARP51-004 text]. Compensatory time is for public agencies only.
- **Pay frequency** (11-4-401, 2008 compilation; later amendment not checked) [US-ARP51-004, medium]:
  - corporations pay salespersons, mechanics, laborers and other servants **semimonthly**;
  - corporations with gross income of USD 500,000 or more may pay FLSA-exempt management and executive employees earning over USD 25,000 a year **at least monthly**.
  - No pay-day lag rule was located.
- **Method of payment:** Act 853 of 2019 added 11-4-403(f) [US-ARS5-003, A.1, high].
  - Automatic deposit or a preloaded debit card is lawful.
  - A paycard must allow at least **one free withdrawal per wage load**.
  - The text has no employee-consent clause.
- **Board, lodging and apparel credit:** fair and reasonable cost under 29 USC 203(m) / 29 CFR 531. It replaces the old 30-cent cap [US-ARS5-003].

## 2 — income_tax
- **Method 2026.** DFA Formula Method, effective 2026-01-01 [US-ARS5-001, A.2, high]:
  - annualise (×12/24/26/52; daily ×260);
  - subtract the standard deduction of **2,470**;
  - net taxable below 100,001 is taken at the USD 50 midpoint of its USD 100 band. The example text says "less than 97,701", an internal inconsistency; the build uses the band midpoint up to the last stepped row.
  - Brackets:
    - 0–5,599: 0%
    - 5,600–11,199: 2% − 111.98
    - 11,200–15,999: 3% − 223.97
    - 16,000–26,399: 3.4% − 287.97
    - 26,400–94,700: 3.7% − 367.16
    - 94,701–97,600: 3.7% with stepped adjustments from 369.90 down to 89.90
    - 97,601 and over: 3.7% − 79.90
  - Round the annual gross tax to the whole dollar.
  - Subtract a **personal credit of 29.00 per AR4EC exemption**, then divide by the number of periods.
- **Oracle (G-DERIVE):** 2,127 monthly with 2 exemptions → 25,524 − 2,470 = 23,054 → midpoint 23,050 → ×3.4% − 287.97 = 495.73 → 496 − 58 = 438 / 12 = **36.50**. Reproduced in Python.
- **Low-income tables.** These are a separate, table-only method for employees who tick AR4EC line 5. Single weekly 0–281.60 → 0, and 281.60 × 52 = 14,643.20, consistent with the AR4ECSP ceiling of 14,643 [US-ARS5-011, A.2]. The engine needs these tables in addition to the formula.
- **Certificate:** AR4EC (R 12/04/2025) [US-ARS5-009, A.2, high]. The federal W-4 is not used.
  - Exemptions: self 1; with spouse 2; head of household 2; plus 1 per dependent.
  - It allows an additional amount per paycheck and has a low-income check box with 2026 bands.
  - No certificate filed → withhold with zero exemptions.
  - A decrease must be reported within 10 days.
  - AR4ECSP gives a full exemption under the 2026 income ceilings: 14,643 / 24,695 / 29,722 / 20,820 / 24,818 [US-ARS5-010].
  - Other certificates: ARW-4MS (military spouse) and AR-TX-4EC (Texarkana) [US-ARP51-002].
- **Supplemental rate: 3.7%** for bonus and commission paid with regular wages. Vacation pay in addition to regular pay is treated as supplemental [US-ARP51-002, A.2].
- **Mid-year rate change (live).** Act 1 of the 2026 First Extraordinary Session (HB 1001 = SB 1) cut the top individual rate from 3.9% to **3.7% effective 2026-01-01**. It was signed in the week of 2026-05-04 [US-ARS5-005, A.3; US-ARS5-013, A.2].
  - The corporate rate falls from 4.3% to 4.1% from 2027.
  - Level: assessment for the whole of 2026, and withholding through the reissued formula and tables. The formula in force today already carries 3.7%.
  - The exact date employers had to switch tables is not stated on the DFA documents read → AR-OQ-1.
- **Local income tax:** none. The DFA tax list's only wage-based item is withholding [US-ARP9V-003].
- **Reciprocity:** none. There is no statutory authority (HB1116 died). Texarkana border-city exemption (26-52-604):
  - residents of Texarkana AR are exempt on all income;
  - residents of Texarkana TX are exempt on wages earned in Texarkana AR;
  - forms AR-TX and AR-3Q-TEX, due 28 Feb [US-ARP51-002].
- **Nonresidents:** withhold on AR-performed services, apportioned by working days. Interstate rail and motor carriers withhold only for AR residents and for nonresidents with all duties in AR. Air carriers withhold where 50% or more of scheduled flight time is in AR [US-ARP51-002].
- **Pass-through entity withholding:** 3.7%, or 4.3% for C-corp members (AR941PT, 15 April). This is outside payroll.

## 3 — social_security
- **SUI 2026** [US-ARP9V-001, US-ARP9V-002]:
  - taxable wage base **7,000**;
  - new employer 2.0%;
  - experienced 0.2–5.1%; deficit 6.1/8.1/10.1%. These figures include the 0.1% Administrative Assessment (A.C.A. 11-10-706).
  - Conditional add-ons: 0.2% advance interest and 0.1% extended benefit.
  - No employee contribution.
- **SDI, TDI, PFML, LTC, transit:** none [US-ARP52-007, US-ARP9V-003].
- **Coverage triggers** [US-ARP9V-001]:
  - domestic service: USD 1,000 or more cash wages in a quarter;
  - agricultural labour: USD 20,000 or more in a quarter, or 10 workers in 20 weeks.
  - Excluded services include: family employment; insurance and real-estate agents paid solely on commission; students employed by their school; student nurses.
  - Section 125 payments are excluded from UI wages.

## 4 — payslip_statute
- There is **no itemised pay-statement statute** [US-ARP52-006 (11 CAR 11, 2026-07-21), US-ARP51-004]. Confidence medium-high.
- Tipped employees: the employer reports the tip-credit amount per hour to the employee **in writing each time it changes** (11 CAR 11 records section) [US-ARP52-006].
- Retention:
  - wage-hour records 3 years (11-4-217) [US-ARL-001];
  - withholding records **6 years**, including AR4EC copies [US-ARP51-002].
- Electronic delivery: there is no AR rule.

## 5 — reporting_instruments
- **Withholding** [US-ARP51-002, A.2, high]:
  - registration on AR-1R; there are three account types: wage, pension, pass-through;
  - new registrations file monthly: **AR941M by the 15th of the following month**, with a zero voucher when nothing was withheld;
  - DFA reclassifies an account to annual (**AR941A by 31 Jan**) when deposits are under USD 1,000;
  - **EFT is mandatory** at an average of USD 20,000 or more per month (ATAP, ACH credit CCD+TXP, ACH debit);
  - the annual reconciliation **AR3MAR is due 28 Feb**, or within 30 days of business termination;
  - penalties: 5% per month up to 35%; interest 10% a year.
  - On closure: notify within 15 days of ceasing wages (AR-20/40).
- **State W-2** [US-ARP51-002]:
  - due **31 Jan** with ARW-3;
  - electronic in **EFW2** (SSA Pub. 42-007) via ATAP bulk upload or CD/DVD;
  - **mandatory electronic filing at 125 or more employees**;
  - records required: RA, RE, RW, RS, RT, RF and RCS; RO and RU optional; **RV not allowed**;
  - 512-byte records, CR/LF.
- **1099:** combined Fed/State programme (Pub. 1220, state fields 663–748). AR filing threshold USD 2,500 (USD 100 for DIV/INT), or any amount withheld.
- **Quarterly UI wage report** [US-ARP9V-001, A.3]:
  - filed through Tax21 online or on paper (DWS-ARK-209B / 209BR / 209BS);
  - **electronic filing is mandatory at 250 or more employees**;
  - due **30 Apr, 31 Jul, 31 Oct and 31 Jan**, even when no wages were paid;
  - late penalties: the greater of USD 10 or 5%, rising to USD 30 or 15%;
  - liability registration on DWS-ARK-201 by the last day of the second month after liability arises.
- **New hire** [US-ARP9V-001]:
  - report **within 20 days** via Tax21;
  - covers all employees living or working in AR, including out-of-state employers;
  - fields: employee name, address and SSN; employer name, address and FEIN;
  - multistate employers may choose one state (with the HHS letter).
- **Child-support verification of employment:** answer within 30 days [US-ARS5-008].

## 6 — leave
- **Paid sick leave:** no statute located. The DOLL minimum-wage/overtime page and the postings list carry none, and no ballot measure is pending [US-ARS5-002, US-ARP9L-001, US-ARS5-004]. Confidence medium, because this is an absence finding.
- **PFML:** none [US-ARP52-007].
- **Vacation and sick pay:** taxed as ordinary wages [US-ARP51-002]. Entitlement depends on company policy; the DOLL wage-claim unit requires the written policy [US-ARS5-014, A.3].
- Other mandated leave with pay impact (jury, voting, military): not researched this run → AR-OQ-5.

## 7 — termination
- **Discharge:** all wages due by the **next regular payday**. If the employer has not paid within 7 days of that payday, it owes **double wages** (11-4-405 as rewritten by Act 853 of 2019) [US-ARS5-003, A.1, high].
- **Resignation:** no statutory deadline located. The default is the next regular payday under policy. Confidence medium → AR-OQ-2.
- **Accrued vacation payout:** no statute. It is owed only if the employer's policy promises it (DOLL wage-claims page) [US-ARS5-014, A.3].
- **Separation notice to UI:** no employer separation-notice duty was located in the Employer Handbook. Confidence medium.

## 8 — benefits_in_kind
- AR adopts the following IRC exclusions, which are therefore excluded from withholding wages: §§ 112, 125, 219, 401(k), 403(b), 408(k), 408(p) and 457 [US-ARP51-002, A.2].
- Non-cash wages (stock, merchandise, room, board, rent) are subject to withholding at fair market value.
- Tips of USD 20 or more a month are wages.
- **HSA:** the individual return allows "Payments to HSA" as an AR1000ADJ adjustment [US-ARP52-001 file, AR1000F 2025]. Whether employer payroll excludes HSA contributions outside a §125 plan is not stated → AR-OQ-3.
- **Transit (§132(f)) and group-term life (§79):** not listed in the employer guide → AR-OQ-3.

## 9 — deductions_garnishments
- **Minimum wage floor:** "non-standard" deductions (breakage, shortages, fines) may not reduce pay below the minimum wage. Court orders, third-party assignments and board/lodging/apparel deductions may [US-ARS5-002, A.2].
- **Child support** [US-ARS5-007, A.3]:
  - AR orders usually add **10%** of current support toward arrears, now **20%** in some cases after a recent law change; the act is not named;
  - withholding is capped by the CCPA;
  - payments go to the **Arkansas Child Support Clearinghouse**;
  - employers manage orders in OCSE MyWorkers [US-ARS5-008].
  - The employer administrative fee is not on any official page read. A tier-B lead gives USD 2.50 per pay period (9-14-218) → AR-OQ-4.
- **Creditor garnishment:** the state exemption (16-66-208: first USD 25/week of net wages of laborers and mechanics) rests on **tier B only** [US-ARS5-012, MANUAL]. The build applies the CCPA limits until it is replaced.

## 10 — collective_agreements (prevailing wage)
- The AR prevailing wage law was **repealed in 2017** [US-ARP51-001, A.2]. Davis-Bacon applies to federal contracts only. There is no state certified-payroll duty.

## 11 — indexation
- **Minimum wage:** not indexed. It is fixed at 11.00 since 2021 [US-ARS5-002].
- **SUI base:** fixed at 7,000 by statute (11-10-215 per the handbook). The rate schedule is set yearly by fund balance [US-ARP9V-001/-002].
- **Withholding:** the standard deduction (2,470), personal credit (29) and low-income bands are republished each year in the DFA formula, tables and AR4EC/AR4ECSP editions [US-ARS5-001, -009, -010, -011]. There is no published index factor; the bands moved by legislation.

## 12 — data_protection
- No AR rule on SSN truncation on pay statements was located. Absence is not verified; the federal W-2 truncation rules apply.
- The DFA requires employers to keep employee SSNs, AR4EC copies and W-2 records for 6 years [US-ARP51-002].
- Confidence low; not searched further → AR-OQ-6.

## 13 — live_legal_change (sweep 2026-01-01 → 2026-11-02)
- **Act 1 of 2026 (1st Ex. Sess.).** Top individual rate 3.7% from 2026-01-01, applied mid-year to withholding. Corporate rate 4.1% from 2027 [US-ARS5-005, US-ARS5-013].
- **2026-11-03 ballot:** no payroll measure [US-ARS5-004].
- **2026 forms reissued:** AR4EC and AR4ECSP (R 12/04/2025); employer instructions revised 4/27/26 [US-ARS5-009/-010, US-ARP51-002].
- **UI:** 2026 rates as registered. 2027 rates are not yet published (the DWS page shows 2026 only) [US-ARP9V-002].
- **11 CAR Part 11:** compilation dated 2026-07-21 [US-ARP52-006]. No substantive change in pay-statement or record rules was found by keyword search.
- Not swept: the full list of Acts from the 2025 Regular Session and the 2026 Fiscal Session (arkleg unreachable) → AR-OQ-7.

## Special populations (state level)

| Population | AR rule | register_id |
|---|---|---|
| Domestic / household | Exempt from AR income-tax withholding (private home, college club, fraternity/sorority). UI coverage at USD 1,000 or more cash wages per quarter | US-ARP51-002; US-ARP9V-001 |
| Agricultural | Withholding required when wages are paid to 4 or more agricultural employees in a period, optional at 3 or fewer. No state overtime for agricultural employees. UI at USD 20,000 per quarter or 10 workers in 20 weeks | US-ARP51-002; US-ARP51-004; US-ARP9V-001 |
| Minors | Child-labour rules not researched (no payroll-rate effect located) | — (AR-OQ-5) |
| Tipped | Cash wage at least 2.63/h; tip credit up to minimum wage; written notice of tip-credit change; tips of USD 20 or more a month reported and withheld on | US-ARS5-002; US-ARP52-006; US-ARP51-002 |
| Clergy / religious | Ministers' services exempt from AR withholding | US-ARP51-002 |
| Students | Full-time students: 85% of the minimum wage (up to 20 h in school weeks, 40 h otherwise) with a DOLL certificate. UI: students employed by their own school are excluded | US-ARP51-004 (11-4-210(b)); US-ARP52-006; US-ARP9V-001 |
| Nonresident aliens | No AR rule beyond federal. AR withholding follows AR work location (guide read) | US-ARP51-002 |
| Statutory employees / commission agents | UI excludes insurance and real-estate agents paid solely on commission. Sales-volume apportionment for nonresident salespeople | US-ARP9V-001; US-ARP51-002 |
| Government employees | Covered by AR withholding (employer includes the state and its subdivisions). UI reimbursable option for government and nonprofit employers | US-ARP51-002; US-ARP9V-001 |
| Military / military spouses | Active-duty military pay 100% exempt (Act 1408 of 2013). Military spouse uses ARW-4MS, renewed yearly | US-ARP51-002 |
| Border residents (Texarkana) | Exempt as described in §2; AR-TX-4EC; AR-3Q-TEX by 28 Feb | US-ARP51-002 |
| Small employers (fewer than 4 employees) | Outside the AR Minimum Wage Act (FLSA may still apply) | US-ARS5-002; US-ARP52-006 |

## ACCESS gaps
- `https://arkleg.state.ar.us/...` (all paths): TLS failure, curl exit 35. Acts 853/2019 and 1019/2021 were read from Wayback. Act 1 of 2026 (1st Ex. Sess.) text, `https://www.arkleg.state.ar.us/Acts/FTPDocument?path=%2FACTS%2F2026S1%2FPublic%2F&file=1.pdf&ddBienniumSession=2025%2F2026S1`: not in Wayback (CDX empty).
- `https://myworkers.ocse.arkansas.gov/MyWorkers/Content/PDF/MyWorkersEmployerResources.pdf`: HTTP 403. The `https://www.ark.org/myworkers/...` mirror also returns 403. No Wayback copy.
- `https://www.dfa.arkansas.gov/child-support/ocse-partners/employers`: 404 (the live page is under `/office/child-support-enforcement/ocse-partners/`).
- `https://www.dfa.arkansas.gov/wp-content/uploads/AR4EC.pdf`: 404 (the current file is `AR4EC2026.pdf`).
- Official Arkansas Code (LexisNexis public portal): not attempted, because it is bot-gated. Needed for 16-66-208, 11-4-401 (current) and 9-14-218.

## Open questions
- **AR-OQ-1.** The date from which employers had to apply the 3.7% withholding formula and tables in 2026, and whether DFA asked for any catch-up. A tier-B lead (Bloomberg Tax) says DFA reissued the formula on 29 May 2026. What would close it: the DFA withholding release or notice of May 2026, or the text of Act 1 of 2026 (1st Ex. Sess.).
- **AR-OQ-2.** Final pay on resignation. What would close it: the current text of Ark. Code 11-4-405, to confirm there is no resignation clause (LexisNexis public portal or arkleg Act history).
- **AR-OQ-3.** State treatment of employer HSA contributions outside §125, of §132(f) transit and of §79 group-term life for AR withholding. What would close it: DFA Rule 2.26-51 conformity list or the AR IRC-conformity act (26-51-404).
- **AR-OQ-4.** The employer fee for child-support withholding (lead: USD 2.50 per pay period, 9-14-218) and the act that raised arrears add-ons to 20%. What would close it: the OCSE MyWorkers employer guide (needs the Chrome pass) or Ark. Code 9-14-218 / 9-14-226.
- **AR-OQ-5.** Mandated leave with pay impact (jury, voting, military, crime victim) and child-labour hour limits. Not researched in this run, which was held to the payroll core. What would close it: the DOLL child-labour page and Ark. Code 16-31-106 and 7-1-102 (official text).
- **AR-OQ-6.** SSN truncation or protection rules for pay statements (e.g. Ark. Code 4-86-107). What would close it: the official Code text.
- **AR-OQ-7.** Bulletin sweep of all 2025 Regular Session and 2026 Fiscal Session acts touching payroll (e.g. the child-support arrears change and any UI changes). What would close it: the arkleg Acts index, through the orchestrator's browser pass, since TLS fails here.
- **AR-OQ-8.** Creditor-garnishment exemption (16-66-208), today only on the tier-B row US-ARS5-012 (MANUAL). What would close it: the official Code text.

Confidence by domain:
- labour_code 85%
- income_tax 90% (the mid-year switch date is open)
- social_security 90%
- payslip 80%
- reporting 90%
- leave 70%
- termination 80%
- benefits_in_kind 65%
- deductions 55%
- collective 90%
- indexation 85%
- data_protection 40%
- live_change 70%
