# Stage 5 — LA (Louisiana): findings across the 13 domains

Worker: compliance-source-hunter, 2026-11-02. Budget declared: 60 fetches / 2 h. Used about 40 network calls (fetches + searches) and about 45 min, so I stopped under the 75% mark.

Outputs:
- Register shard: `00-official-sources/_register-shards/S5-LA.csv`, rows US-LAS5-001..016 (14 active, 2 partial, 0 MANUAL).
- Sources: `00-official-sources/ccg-sources/LA/`, 13 files, about 4.1 MB. The largest is the LR rule page at 1.7 MB.

**Access.** The live hosts would not serve the pages, so statutes were read from Wayback `id_` snapshots:
- legis.la.gov does not resolve from this machine;
- revenue.louisiana.gov, laworks.net and doa.la.gov return HTTP 403 to curl.

dam.ldr.la.gov (LDR documents) works with plain curl. The VPN was off (BR exit), and that made no difference for dam.ldr.

**Reused active rows (not re-fetched):**
- US-LA-PIT-001: R-1306. Its local file was missing; it is now held as US-LAS5-001.
- US-LA-P5-1-001 and US-LA-P5-1-002: the withholding page and the supplemental FAQ.
- US-LA-SUI-001 and US-LAP9V-001/-002: UI.
- US-LA-P5-2-001: the constitutional bar on local income tax.
- US-LAR3-001/-002 and US-LAL-001/-002: wage-payment chapter 23:631-638.
- US-LAP6-001: prevailing wage repealed.
- US-LA-P5-2-005: LAWATS POA.
- US-LAP9M-001: posters in Spanish.
- US-MULTIS5-021: Act 382.

## PRIORITY (MULTI-OQ-1): Act 382 of 2025 and LAC 61:I.1923 — ANSWERED

- **Statute.** Act 382 of the 2025 Regular Session (HB 567) amends R.S. 47:112.2(A) and 47:248(B)(1)(a) [US-MULTIS5-021, A.1]. Status: in force, effective 2025-06-20, and applies to income tax periods beginning on or after 2026-01-01. Level: withholding and nonresident taxation. The rule:
  - wages of a nonresident for duties performed in LA on **30 or fewer days** in the calendar year are exempt (previously 25);
  - the home-state condition, 47:248(B)(1)(d), is repealed.
- **Regulation: ADOPTED.** The final Rule *Mobile Workforce Exemption (LAC 61:I.1923)*, Department of Revenue, Tax Policy and Planning Division, is published in the **Louisiana Register Vol. 52 No. 3, 2026-03-20, LR 52:358 (doc 2603#037)**. It is "adopted on the day of promulgation", so effective 2026-03-20 [US-LAS5-002, A.1, inspected directly; the page images were read because the PDF has no text layer]. It supersedes the NOI row US-MULTIS5-022, which can now be closed.
  - A.2.a: the exemption covers duties performed in LA on 30 or fewer days in the calendar year. A.2.d is repealed.
  - C.1.a: an exempt nonresident files no LA return. If the nonresident has **other Louisiana-source income**, the exemption does not apply and all LA income goes on the NPR worksheet of IT-540B.
  - C.1.b.i: the employee notifies the employer within **10 days from the 31st day** of duties in LA.
  - C.2 (employer): if duties in LA exceed 30 days, the employer **begins withholding and reports on Form L-1 beginning in the period in which the 31st day fell**.
- **Drafting inconsistency.** C.1.a says "less than 30 days", while A.2.a and the statute say "30 or fewer". The statute governs, so the build models ≤ 30 days exempt.
- **Retroactive catch-up.** MULTI's row says that from day 31 the employer withholds for every day, including the first 30 (from the Act text). The regulation only says "begin withholding … in the period in which the 31st day fell". It does not say how the first 30 days are caught up. Open question LA-OQ-1.
- **What the build does** (WTC/DD): add a per-employee counter of LA workdays for nonresident employees (employer plus related entities, per Act 382). Also add a flag for "other LA-source income declared".

## 1 — labour_code
- **Minimum wage:** LA has **no state minimum wage law**. FLSA-covered employers pay the federal USD 7.25/h [US-LAS5-006, A.2, high]. No 2027 rate is enacted.
- **Local minimum wage:** prohibited. No local subdivision may set a minimum wage or a mandatory number of vacation or sick days, paid or unpaid [R.S. 23:642, US-LAS5-005, A.1, high].
- **Overtime:** no state overtime statute was located; the FLSA applies. Confidence medium: this is an absence, and no LA overtime text was searched beyond chapter 6.
- **Pay frequency** (R.S. 23:633) [US-LAS5-004, A.1, high]:
  - The employer must tell employees at hire the wage, the **method** and the **frequency** of payment, and any later change.
  - An employer that does not designate paydays pays on the 1st and 16th.
  - Manufacturing, oil-boring and mining employers with 10+ employees, and public-service corporations, pay at least twice monthly, about two weeks apart, with wages due by the payday ending the next payroll period. Clerical staff and salesmen are excluded except at public-service corporations.
  - FLSA-exempt employees are outside the section.
  - Fine: USD 25-250 per day.
- **Method of payment (direct deposit / paycard):** no LA consent statute was located. 23:633 requires only notice of the "method" [US-LAS5-004]. Tier-B leads (ezel.ai) say the same. Confidence medium → LA-OQ-3.
- **Live change:** SB 133 (2025 RS) would have added "laborers" to 23:631/633/635. It is NOT codified (the 2026-03 snapshot history stops at Acts 2014) and was technical only [US-LAS5-014, partial].

## 2 — income_tax
- **Withholding method 2026** [US-LAS5-001, A.2, high]: LDR R-1306 (1/26), flat **3.09%**.
  - Formulas:
    - no deduction: W = S × 0.0309;
    - single / married-separate (L-4 "1"): W = (S − 12,875/N) × 0.0309;
    - MFJ / QSS / HoH (L-4 "2"): W = (S − 25,750/N) × 0.0309.
  - N = 365/52/26/24/12/1. A negative term is treated as 0.
  - **Oracle examples, reproduced (G-DERIVE):**
    - (700 − 12,875/52) × 0.0309 = 13.9793 → **13.98**;
    - (4,600 − 25,750/26) × 0.0309 = 111.5371 → **111.54**.
    - Both are consistent with rounding to the cent.
  - Certificate: **Form R-1300 (L-4)**. The edition was not re-fetched: `taxforms/1300(L4).pdf` returned 404.
- **Emergency rule** [US-LAS5-011, A.2]: RIB 26-005 (2026-01-12) says the tables are set by an emergency rule under LAC 61:I.1501 effective 2026-01-01. The official 2026 standard deduction may differ slightly once January-2026 CPI-U is applied. Status: emergency rule in force; final rule not checked.
- **Supplemental and vacation pay:** withheld like regular wages, with no separate flat supplemental rate [US-LA-P5-1-002, A.3].
- **Who is withheld** [US-LA-P5-1-001 / US-LAS5-003]:
  - residents, and nonresidents performing services in LA (subject to the 30-day rule above);
  - residents working outside LA, if those wages are not subject to withholding in the other state.
- **Local income tax:** none. The constitution bars parishes and municipalities from levying an income tax [US-LA-P5-2-001, A.1].
- **Reciprocity:** none (MULTI matrix: no LA agreement).

## 3 — social_security
- **SUI:**
  - 2026 taxable wage base **USD 7,000**; rates 0.09%-6.20% [US-LA-SUI-001, US-LAP9V-002].
  - New-employer rate = the average rate of its NAICS industrial classification; experience rating follows a 24-month eligibility period [US-LAP9V-001, US-LAS5-007].
  - Social charges (non-charge, Incumbent Worker Training, Integrity) are inside the total rate. The IWTP and Integrity shares are not FUTA-creditable [US-LAP9V-001/-002].
  - No employee contribution.
- **SDI/TDI/PFML:** none [US-LA-P5-2-002 (DOL WB list)].
- **Agency name:** "Louisiana Works" replaces "Louisiana Workforce Commission" in current statute text (23:633(D)) and in 2026 act titles [US-LAS5-004, US-LAS5-016]. The SIR and RSPEC should use the current name and keep laworks.net.

## 4 — payslip_statute
- No itemised pay-statement statute exists in the wage-payment chapter (R.S. 23:631-638, all read) [US-LAR3-002]. The only content duty is the notice at hire of rate, method and frequency [US-LAS5-004]. Confidence medium-high.
- Retention: no LA payroll-record retention rule was read → LA-OQ-4.

## 5 — reporting_instruments
- **Withholding** [US-LAS5-003, US-LAS5-008]:
  - Form **L-1**, quarterly, filed electronically (LaTAP or approved software), zero returns required.
  - Payment frequency by average monthly withholding: quarterly if < USD 500; monthly if 500 to < 5,000; semi-monthly if ≥ 5,000.
  - Quarterly due dates: Apr 30 / Jul 31 / Oct 31 / Jan 31 (LAC 61:I.1501).
- **Annual reconciliation and W-2** [US-LAS5-003, US-LAS5-008, US-LAS5-009]:
  - Form **L-3** + W-2s due on or before the first business day after **January 31**; within 30 days if the business closes.
  - Electronic filing is mandatory at **50+ W-2s**, through **LaWage** or another method the secretary authorises. Magnetic media and CD/DVD are refused.
  - State boxes 16-18.
  - **The file format for LaWage bulk upload (EFW2 or state layout) was not read** → LA-OQ-2.
- **Quarterly UI report** [US-LAS5-007, A.3; snapshot 2025-04]: due the last day of the month after the quarter; domestic annual filers due Jan 31. Mandatory electronic filing (LAWATS). Part-time and temporary employees are reported; DE students earning school credit are not. Form name and upload format not read → LA-OQ-5.
- **New hire** [US-LAS5-010, A.1, high]:
  - Report to DCFS (state directory of new hires) within **20 days** of hire or rehire. Rehire covers return after layoff, furlough, separation, leave without pay or termination; the statute sets no 60-day threshold, the 60 days is a tier-B claim.
  - Electronic filers send two monthly transmissions 12-16 days apart. Multistate employers may designate one state.
  - Fields: employee name, address, SSN, occupation, first-day-of-work date; employer name, address, EIN.
  - Penalty up to USD 25 per failure, or 500 with conspiracy.
- **Registration and agents:** LaTAP (LDR); LAWATS online POA (UI) [US-LA-P5-2-005]; R-7006 (LDR POA).

## 6 — leave
- **Paid sick leave:** no state statute, and local mandates are prohibited [R.S. 23:642, US-LAS5-005]. No PFML.
- **Jury duty:** up to **one paid day**, without loss of wages or of sick, emergency or personal leave. No adverse action. Fine USD 100-500, or 100-1,000 plus reinstatement for a discharge [R.S. 23:965, US-LAS5-013, A.1].
- Not covered: other leaves with pay impact (voting, military, school conference, bone-marrow donation) → LA-OQ-6.

## 7 — termination
- **Final pay:**
  - discharge: by the next regular payday or within 15 days of discharge, whichever comes first;
  - resignation: by the next regular payday for the pay cycle in which the employee was working, or within 15 days, whichever comes first.
  - Payment is made where and how it was customary, or by prepaid mail. CBA override allowed [R.S. 23:631(A), US-LAL-001 / US-LAR3-002].
- **Vacation payout:** accrued and unused vacation that is eligible under the employer's policy is an "amount then due". Earned vacation cannot be forfeited [23:631(D)].
- **Commissions and bonuses:** due if earned and not modified under a written policy [23:631(E)].
- **Penalty wages:** the lesser of 90 days' wages or full wages from demand, plus attorney fees; a good-faith dispute limits liability to the wages plus interest [23:632, US-LAR3-001].
- **Pre-employment test costs:** may be withheld from final pay if the employee resigns within 90 working days, only if pay is at least the federal minimum + USD 1 and the employee is not part-time or seasonal [23:634(B), US-LAS5-004].
- Not covered: UI separation notice (LWC Form 1?) → LA-OQ-7.

## 8 — benefits_in_kind
- No LA source was read this run. The LDR FAQ on cafeteria-plan pre-tax contributions exists in the FAQ index, but its Wayback URL returned 404. LA computes tax from federal AGI (lead only, not registered). Confidence low → LA-OQ-8.

## 9 — deductions_garnishments
- **Creditor garnishment:** 75% of weekly disposable earnings is exempt, never less than 30 × the federal minimum wage. This matches the CCPA [R.S. 13:3881(A)(1)(a), US-LAS5-012, A.1].
- **Support (stricter than CCPA):** the exemption is **50%** for child support and **60%** for spousal support. A mixed or unclear DCFS order is treated as child support. So the maximum child-support withholding is **50%**, not CCPA's 50-65% [US-LAS5-012].
- **Disposable earnings:** pay after legally required deductions and after usual-course retirement, medical and life-insurance deductions and amounts owed to the employer [US-LAS5-012].
- **Fines and deductions:** fines are prohibited except for wilful or negligent damage or theft of employer funds, capped at the actual damage [R.S. 23:635, US-LAS5-004].
- Not read: IWO fee and priority specifics (DCFS) → LA-OQ-9.

## 10 — collective_agreements
- The state prevailing wage law was repealed in 1988 [US-LAP6-001].
- CBA fringe-benefit amounts are treated as wages under 23:631-639, so the penalty-wage rules apply [R.S. 23:640, US-LAS5-015].

## 11 — indexation
- **PIT standard deduction:** indexed annually by the previous year's CPI-U increase [R.S. 47:294(B), cited in RIB 26-005, US-LAS5-011]. The new value is published in R-1306 and the LDR emergency or final rule (LAC 61:I.1501).
- **Derivation:**
  - 25,750 = 2 × 12,875 exactly.
  - 12,875 / 12,500 = 1.0300 exactly. The 2025 base of 12,500 comes from a tier-B lead (USDA NFC bulletin) and is NOT registered.
  - Write-up: the step is consistent with a 3.0% CPI-U adjustment rounded to 25; not proven against an A-tier 2025 figure.
- **SUI wage base:** 7,000 in 2026. A tier-B lead puts 2025 at 7,700. The statutory mechanism (wage base tied to the trust-fund level, R.S. 23:1536 per leads) was not read → LA-OQ-10.
- **Minimum wage:** not indexed (no state law).

## 12 — data_protection
- Not researched this run: SSN truncation on pay statements and LA personal-information statutes → LA-OQ-11. No federal pay-statement SSN rule exists either.

## 13 — live_legal_change
- **Act 382 (2025) and LAC 61:I.1923:** adopted (see PRIORITY).
- **RIB 26-005 / emergency rule:** 2026 tables [US-LAS5-011].
- **2026 Regular Session:**
  - Page 1 of the Acts list (Acts 1-100) was read: no withholding, UI-tax, minimum-wage or wage-payment act. Act 61 HB232 on employment certificates for minors has no payroll impact on its title [US-LAS5-016, partial].
  - Pages 2-10+ are unreachable (ASP.NET postback).
  - Tier-B lead: a 2026 "Act 33" on state withholding from UI benefits. That is benefit side, not employer payroll, and was not verified.
- **SB 133 (2025):** not enacted / technical [US-LAS5-014].
- The 2027 standard deduction is not yet published (no R-1306 1/27; probes of `1306-*-26` / `1306-1-27` returned 404).

## Special populations (state rules)
| Population | LA rule | register_id |
|---|---|---|
| Nonresident employees (incl. nonresident aliens working in LA) | 30-day mobile-workforce exemption; withhold from the period of the 31st day; exemption lost if other LA-source income | US-MULTIS5-021, US-LAS5-002 |
| Domestic / household | UI: annual domestic filers due Jan 31. State withholding on household employees: the LDR FAQ exists but its answer was not read | US-LAS5-007; LA-OQ-12 |
| Students | UI: Distributive Education students earning school credit are not reported (summer employment is) | US-LAS5-007 |
| Minors | No payroll-calculation rule found. 2026 Act 61 (HB232) changes employment certificates | US-LAS5-016 |
| Tipped employees | No state minimum wage, so federal tip credit rules only | US-LAS5-006 |
| Exempt (FLSA) staff | Outside the 23:633 pay-frequency and notice section | US-LAS5-004 |
| Part-time / seasonal | Excluded from the 23:634(B) test-cost recovery | US-LAS5-004 |
| Agricultural, clergy/religious, statutory employees, government employees | No state rule read this run; federal treatment assumed, not verified | LA-OQ-12 |
| Military spouses | Form L-4E military spouse exemption exists (LDR FAQ title only) | LA-OQ-12 |

## MULTI hand-offs
- **Act 382 / LAC 61:I.1923:** answered above. Rule adopted LR 52:358, 2026-03-20.
- **SUI wage-base credit for wages reported to another state:** not read this run → LA-OQ-10.
- **PFML/SDI for multistate workers:** not applicable (LA has none).
- **Paid sick leave for employees working partly in LA:** not applicable (no state law; local mandates preempted, 23:642).
- **Pay-statement reach to out-of-state work:** not applicable (no LA pay-statement statute).

## ACCESS gaps (exact URLs)
- `https://legis.la.gov/…` and `https://www.legis.la.gov/…`: host does not resolve from this machine; Wayback used for every statute.
- `https://www.legis.la.gov/legis/ActNumbers.aspx?sid=26RS`: pages 2-10+ (postback). Wayback holds only page 1.
- `https://revenue.louisiana.gov/tax-education-and-faqs/faqs/withholding-tax/are-employees-pre-tax-contributions-to-a-qualified-cafeteria-plan-subject-to-withholding-income-tax/`: live 403, Wayback 404.
- `https://dam.ldr.la.gov/taxforms/1300(L4).pdf`: 404. The current L-4 file name is unknown.
- `https://revenue.louisiana.gov/`, `https://www.laworks.net/`, `https://www.doa.la.gov/doa/osr/louisiana-register/`: HTTP 403 to curl.
- `https://dcfs.la.gov/assets/docs/searchable/New-Hire-Registry/Louisiana_New_Hire_Reporting_Form-3.pdf`: 404.

## Open questions
- **LA-OQ-1:** Act 382 catch-up. When day 31 is reached, how are days 1-30 withheld (lump catch-up in the period of the 31st day)? Closes with the Act 382 text of R.S. 47:112.2(A) as codified, or an LDR RIB/FAQ on the mobile workforce exemption.
- **LA-OQ-2:** LaWage bulk W-2 file format (EFW2 or LA layout) and 2025-tax-year specs. Closes with the LDR LaWage / W-2 electronic filing specification (LDR, dam.ldr.la.gov).
- **LA-OQ-3:** direct deposit / paycard consent. Closes with a Louisiana Works wage-payment FAQ, or confirmation that none exists beyond 23:633.
- **LA-OQ-4:** payroll record retention (state). Closes with R.S. 23:1660 (UI records) and any LDR withholding-record retention rule.
- **LA-OQ-5:** UI quarterly report form name and LAWATS upload format (ICESA?), plus a 2026 copy of the LWC FAQ. Closes with Louisiana Works' LAWATS file specification.
- **LA-OQ-6:** other paid or protected leaves (voting, military, school conference, bone marrow / organ donation). Closes with a read of R.S. 23:961-1015 via Wayback.
- **LA-OQ-7:** UI separation notice (LWC Form 1) duty on separation. Closes with LAC 40:IV or a Louisiana Works employer page.
- **LA-OQ-8:** state conformity for §125, 401(k), HSA, transit and group-term life. Closes with the LDR cafeteria-plan FAQ (403/404 today) and R.S. 47:293 (AGI definition).
- **LA-OQ-9:** LA IWO specifics (employer fee, priority, remittance to the LA SDU). Closes with R.S. 46:236.3 / 9:303 and the DCFS employer page.
- **LA-OQ-10:** SUI wage-base mechanism (R.S. 23:1536) and credit for wages paid to another state. Closes with a Wayback read of R.S. 23:1536.
- **LA-OQ-11:** SSN on pay statements and payroll data. Closes with the LA statutes on SSN display (R.S. 51:3071 et seq. is the breach law) via Wayback.
- **LA-OQ-12:** household-employee withholding (LDR FAQ answer), ag/clergy/statutory/government UI coverage (R.S. 23:1472), and military spouse L-4E reporting in box 16. Closes with the LDR FAQ pages and R.S. 23:1472.
- **For the synthesis:** US-MULTIS5-022 (NOI, partial) can be closed as superseded by US-LAS5-002 (the adopted rule). The pre-existing LA row US-LA-P5-1-001 is silent on the 30-day rule; the MULTI conflict is resolved by US-MULTIS5-021 + US-LAS5-002.

Confidence by domain:
- income_tax: 95%.
- reporting: 85%. The LaWage and UI file formats are open.
- labour_code: 85%.
- termination: 90%.
- garnishment: 85%.
- SUI: 85%.
- leave: 70%.
- live_legal_change: 70%. The 2026 Acts sweep is partial.
- benefits_in_kind: 30%.
- data_protection: 20%.
