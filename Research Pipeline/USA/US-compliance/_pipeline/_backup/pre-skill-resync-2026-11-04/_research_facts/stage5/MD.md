# Stage 5 — Maryland (MD): 13-domain findings

Worker: compliance-source-hunter, 2026-11-02. Brief: `_prompts/stage5-brief.md`. Mandate block: MD — Maryland (MANDATE.md line 703), answered at the seal; this pass extends it to all 13 domains.
Budget declared: 60 fetches / 2 h. Used: about 43 fetches (curl and web search) and about 40 minutes. I stopped fetching at the 75% fetch mark.
Network: no VPN at run time (ipinfo shows a Brazil IP). All MD official hosts answered plain curl: mgaleg.maryland.gov, marylandcomptroller.gov, labor.maryland.gov, paidleave.maryland.gov, dls.maryland.gov and dhs.maryland.gov.
Register shard: `00-official-sources/_register-shards/S5-MD.csv` has 21 rows, US-MDS5-001..021. New sources are in `00-official-sources/ccg-sources/MD/`: 33 files, 4.8 MB, no file over 1 MB.

Active rows reused without a re-fetch (their local files were re-read this pass):
- US-MDP51-001: 2026 Employer Withholding Guide, `pdfs/MD/withholding-guide-2026_webfetch-20261029.pdf`. I re-read it in full; the parameters are carried in US-MDS5-021.
- US-MDP9V-001: DOL UI tax-rate page, `pdfs/MD/DOL-UI-tax-rate_2026-11-01.html`.
- US-MDP9L-001 and -002: HWFA 3-1301..3-1311 files and the poster. These files now also carry the ESSL rule, in US-MDS5-013.
- US-MULTI-008 (AR IT-3, reciprocity), US-MDP51-005 (LE 3-504 pay statement), US-MDP51-006 (SFP 17-201).
- US-MDP51-003 is restated, not changed, by US-MDS5-014 (FAMLI page re-read 2026-11-02). The `supersedes` link is set so the synthesis can close the older row.

---

## 1. labour_code
- **State minimum wage:** **15.00 USD/h** since 2024-01-01, for every employer size [US-MDS5-005].
  - The statute has no indexation, and no 2027 step is enacted.
  - Employees under 18 may be paid 85%, which is 12.75 [US-MDS5-005, US-MDS5-015].
- **Local minimum wages** (DOL page) [US-MDS5-015]:
  - **Montgomery County**, from 2026-07-01: **18.00** for 51+ employees; **16.50** for 11–50 employees (and for 501(c)(3) or Medicaid home-care employers with 11+); **15.95** for 10 or fewer.
    - Indexed every July 1 by the prior year's CPI-W for Washington-Baltimore.
    - Excluded: workers under 19 working 20 h/week or less.
    - Workers under 20 may be paid 85% for their first 6 months.
    - Tipped cash wage: 4.00.
  - **Howard County**, from 2026-07-01: **16.00**, all employers.
  - **Prince George's County**, from 2026-07-01: **15.30**, all employers.
  - Only the DOL page was read. The county ordinances themselves were not read (montgomerycountymd.gov returned 404, see ACCESS).
- **Tipped employees:** cash wage at least **3.63**, so the maximum tip credit at 15.00 is 11.37 [US-MDS5-007].
  - Restaurants that use the tip credit must give a Tip Credit Wage Statement each pay period [US-MDS5-007, US-MDS5-015].
- **Overtime:** 1.5× for hours over 40 per workweek. There is no daily overtime [US-MDS5-006].
  - The threshold is 48 h for bowling establishments and for non-hospital residential care institutions, and 60 h for FLSA-exempt agricultural work.
  - Exemptions follow FLSA patterns (carriers, DOT drivers, auto-dealer mechanics and salespeople, taxicab drivers, seasonal amusement).
- **Pay frequency:** at least every 2 weeks or twice a month. Administrative, executive and professional employees may be paid less often [US-MDS5-008].
  - If payday falls on a nonworkday, pay on the **preceding** workday.
- **Method of payment** [US-MDS5-008]:
  - Cash, or a check convertible at face value.
  - Direct deposit only with the employee's authorisation.
  - Pay card only if the employee authorises it and the fees are disclosed in writing in at least 12-point type.
- Confidence: 95% (statute plus DOL page). County figures: 85%, because the ordinances were not read.

## 2. income_tax
- **Who withholds:** every employer must withhold State tax plus the **county-of-residence local tax**, combined, on MW506 [US-MDP51-001, US-MDS5-021]. The local tax is piggybacked on the state return, which is why MD is T3 in the mandate.
- **Certificate:** MW507, with MW507M (military spouse) and MW507P (annuity/sick pay). An employee who gives no certificate is withheld as if claiming one exemption.
  - The Comptroller's state-payroll memo defaults the local rate to 3.30% when the county is unknown [US-MDS5-021, US-MDS5-003].
- **State rates, TG 10-105** [US-MDS5-001]: 2 / 3 / 4 / 4.75 / 5 / 5.25 / 5.5 / 5.75 / **6.25 / 6.50**%.
  - Single top bands: 6.25% above 500,000, 6.50% above 1,000,000.
  - Joint top bands: 6.25% above 600,000, 6.50% above 1,200,000.
  - The 6.25 and 6.50 bands are the 2025 BRFA bands, flagged "new" for 2026 withholding by the Comptroller [US-MDS5-003].
  - The 2% capital-gain surcharge (FAGI > 350,000) applies at **assessment only**. It is not part of withholding.
- **Percentage method** [US-MDS5-021]:
  - Steps: wages − standard deduction − (exemptions × per-period exemption), then apply the county table.
  - Annual exemption: **3,200**. Standard deduction: **3,400** (flat).
  - G-DERIVE: TG 10-217 fixes 3,350 and indexes it from 2026, rounding down to a multiple of 50 [US-MDS5-002]. 3,400 is consistent with that rule. The Comptroller's own COLA figure was not read.
  - Per-period values re-derived in Python:
    - Weekly 61.54 / 65.38 and monthly 266.67 / 283.33 match.
    - Biweekly 130.76 and semimonthly 141.66 are **truncated** (130.769 → 130.76; 141.667 → 141.66).
    - Daily values use /365: 8.77 / 9.31.
  - The tables ignore the 2/3/4% bands and start at 4.75%, as the law directs.
  - There are ten local tables: 2.25, 2.40, 2.65, 2.75, 2.85, 3.00, 3.05, 3.10, 3.20 and 3.30. Use the table that **equals or slightly exceeds** the county rate. Example: Harford 3.06 uses the 3.10 table; Cecil 2.74 uses the 2.75 table.
  - Arithmetic check: 3.30 table, single, annual. Bases 8,050 / 10,125 / 12,262.50 / 21,062.50 / 43,687.50 / 91,437.50 are reproduced exactly from (state band + 3.30). The joint bases 12,075 … 109,475 are also exact.
  - Withholding floors (no withholding below): weekly 96, biweekly 192, semimonthly 208, monthly 417, daily 13.70, annual 5,000.
- **2026 county rates** [US-MDS5-003, A.2; cross-checked with DLS US-MDS5-004]:

| Rate | Counties (code) |
|---|---|
| 2.25 | Worcester (24); out-of-state (25-76) |
| 2.40 | Talbot (21) |
| 2.65 | Garrett (12) |
| 2.74 | Cecil (08) |
| 2.95 | Washington (22) |
| 3.03 | Carroll (07), Charles (09) |
| 3.06 | Harford (13) |
| 3.20 | Allegany (01), Baltimore Co (03), Baltimore City (04), Calvert (05), Caroline (06), Howard (14), Montgomery (16), Prince George's (17), Queen Anne's (18), St. Mary's (19), Somerset (20), Wicomico (23) |
| 3.30 | Dorchester (10), Kent (15); unknown MD county (default) |
| Graduated | Anne Arundel (02): single 2.70 to 50,000 / 2.94 to 400,000 / 3.20 over; joint 2.70 to 75,000 / 2.94 to 480,000 / 3.20 over. Frederick (11): single 2.25 to 25,000 / 2.75 to 50,000 / 2.96 to 150,000 / 3.20 over; joint 2.25 / 2.75 to 100,000 / 2.96 to 250,000 / 3.20 over |

  - 3.30 is the new county maximum from TY2026.
  - Changes from CY2025 (DLS column): Allegany 3.03 → 3.20, and Kent 3.20 → 3.30.
- **Supplemental wages:** for a lump-sum annual bonus, withhold at the top state rate **6.50% plus the county's top local rate** (for example 9.80% in the 3.30 table; 9.70% in the 3.20 table) [US-MDS5-021].
  - The guide has no flat supplemental rate for other supplemental pay and no rounding rule. Withholding is computed in cents; retirement withholding is in whole dollars [US-MDP51-001].
- **Nonresidents** [US-MDS5-021, US-MDS5-003]:
  - A resident of a nonreciprocal state is withheld at the state rate plus the **special nonresident 2.25%**, with no local tax. The flat nonresident rate is 7.0% (4.75 + 2.25).
  - A resident of a reciprocal state is exempt when MW507 is filed: DC, PA, VA, WV [US-MULTI-008].
  - The exemption is lost when the employee keeps an abode in MD for more than 6 months **and** spends 183 days or more in MD. This test does not apply to WV.
  - An MD resident working in DE or in another nonreciprocal state uses the Delaware/nonreciprocal table, which carries local tax and the credit [US-MDS5-021].
- **Oracle:** the Comptroller online withholding calculator (referenced in the guide) and the Central Payroll Bureau Net Pay Calculator [US-MDS5-003]. Neither was run.
- Confidence: 95% for the method and rates; 90% for the county table (two-source match; one DLS cell lost in layout).

## 3. social_security
- **SUI** (A.2 page US-MDP9V-001 / US-MDP51-002):
  - 2026 taxable wage base **8,500** (not indexed). Table A applies in 2026 (same as 2025).
  - Experience rates 0.30–7.50%; standard rate 7.50%; new employers 1.0–2.6%.
  - Foreign construction contractors pay the construction-industry average, but not less than the new-employer rate.
  - There is **no employee UI contribution**.
- **UI localization:** LE 8-202 follows the uniform test: in-state, incidental out-of-state, base of operations, direction and control, residence [US-MDS5-019].
- **MULTI hand-off (SUI wage-base credit):** the BEACON wage file has an optional field "Out of State taxable wages subject to UI paid to employee for the year" [US-MDS5-017]. This implies wages reported to another state count toward the 8,500.
  - The statute defining taxable wages was not located: it is not in LE 8-101 or 8-606, the two sections read. Status: **partial**, see Q2.
- **FAMLI (PFML)** [US-MDS5-014]:
  - **No contribution in 2026.** From **2027-01-01**: 0.9% of wages up to the Social Security wage base, split 0.45 employer / 0.45 employee. The employer may withhold up to 50%.
  - Employers with fewer than 15 employees (headcount inside and outside MD under one EIN) remit only the employee share.
  - The statutory cap is 1.2%. The next-year rate is announced each November from 2027.
  - Remittance is quarterly with the wage and hour report on paidleave.maryland.gov, due the last day of the month after the quarter; first due 2027-04-30.
  - Benefits start 2028-01-01: up to 12 weeks, up to 1,000 per week.
  - **MULTI hand-off (MULTI-OQ-3):** FAMLI covers "all employees working in positions localized in Maryland" and nobody may opt out. Coverage therefore follows UI localization (LE 8-202) [US-MDS5-014, US-MDS5-019].
- **SDI/TDI:** none. **Other payroll levies:** none beyond withholding (P9 list, US-MDP9V-002).
- Confidence: 90%.

## 4. payslip_statute
- **Content, LE 3-504** [US-MDP51-005]: employer name, address and phone; pay date and period; hours (unless exempt); rates; gross and net; each deduction by name and amount; other bases of pay.
  - Notice at hire, and notice of any change one pay period in advance [US-MDL-001].
- **Additional pay-statement content:**
  - The **available ESSL balance** each time wages are paid; an online balance system satisfies this (LE 3-1305(f)) [US-MDS5-013].
  - A Tip Credit Wage Statement for restaurants [US-MDS5-007].
  - For State agencies only, the combined state + local tax is shown as "STATE TAX" and the county is coded [US-MDS5-003].
- **Delivery:** "written or online" statement (3-504) [US-MDP51-005]. No separate e-consent rule was found.
- **SSN:** see section 12.
- **Retention:** 3 years for withholding records (guide) [US-MDS5-021]. The wage-hour record period (LE 3-424) was not read; see Q5.
- Confidence: 85%.

## 5. reporting_instruments
- **Withholding** [US-MDS5-021]:
  - Registration: Combined Registration Application (CRA), which issues the 8-digit CRN.
  - **MW506** is filed on Maryland Tax Connect. Frequency:
    - accelerated: 15,000+ in the prior year and 700+ accumulated, due within 3 business days of the pay date;
    - monthly: over 700 in any quarter, due on the 15th of the following month;
    - quarterly: under 700 per quarter;
    - seasonal: needs prior approval;
    - annual: under 250 per year, due 31 January.
  - Amendments on MW506A/MW506AM. Final returns on MW506FR.
- **Annual reconciliation:** **MW508** plus the W-2s, due **31 January** [US-MDS5-016].
  - Electronic filing is mandatory at 25+ W-2s (TG 13-706.1; 100 penalty per violation).
  - Format: **SSA EFW2 in the modified Maryland format**, by bulk upload on Maryland Tax Connect.
  - RS record: FEIN at positions 328-336 and CRN at 338-345.
  - RV record = MW508, with a NAICS code at positions 333-338.
  - Date-time stamp at positions 497-512 of RS and RV.
  - A zero MW508 is required for any open account.
  - The TY2025 spec says layouts are unchanged. The TY2026 edition is **not yet posted** (Q1).
- **Quarterly UI wage report:** filed in BEACON within 1 month after the quarter end [US-MDS5-017; US-MDP9V-001].
  - Formats: online entry, CSV, XML, ICESA or EFW2. Spec updated 2026-04-20.
  - Amounts in cents with no decimal point; adjustment codes 00-10.
  - Penalty 35 per late report; interest 1.5% per month.
- **New hire:** within 20 days, LE 8-626.1 [US-MDS5-018].
  - Fields: SSN, name, address, hire date, employer name and address, **starting wage**, **whether employer health insurance is offered**, FEIN, **MD UI account number**.
  - Multistate electronic filers may pick one state and must name it.
  - Penalty: warning first, then 20 per month (500 for conspiracy).
- **POA / third-party filing:**
  - Comptroller: Form 548P (limited POA / reporting agent) [US-MDP51-001].
  - DOL UI: Power of Attorney Authorization Form, plus third-party-agent file specs [US-MDS5-017].
  - FAMLI: TPA support is announced [US-MDS5-014].
- Confidence: 90%.

## 6. leave
- **Earned Sick and Safe Leave (HWFA, LE 3-1301..3-1311)** [US-MDS5-013]:
  - Employers with 15+ employees give **paid** leave; employers with 14 or fewer give **unpaid** leave. Headcount = average monthly count of the prior year, all employees counted.
  - Accrual: at least 1 h per 30 h worked.
  - Caps the employer may apply: earn 40 h a year, use 64 h a year, hold a 64 h balance. Use can wait 106 days.
  - No accrual in a period below 24 h (biweekly) or 26 h (semimonthly).
  - FLSA-exempt employees are assumed to work 40 h.
  - Carry-over up to 40 h, or front-load the full amount instead.
  - Rehire within 37 weeks: the balance is reinstated.
  - **No payout at termination is required**. Advanced leave may be recovered from final pay with a signed agreement.
  - Tipped employees are paid not more than minimum wage for ESSL.
  - Excluded: under 12 h/week, under 18, agricultural, certain temps and as-needed health workers, construction workers whose CBA waives the law.
  - **Local:** laws enacted after 2017-01-01 are preempted. Pre-2017 local laws (Montgomery County ESSL) survive and may be amended. The Montgomery text was not read (Q4).
  - **MULTI hand-off:** coverage reaches any "employee" of an employer, with no in-state hours test. The only threshold is "regularly works less than 12 hours a week for an employer" (3-1303(a)(1)). Whether the 12 hours means MD hours only is not stated (Q3).
- **FAMLI benefits:** from 2028. They do not affect payroll in 2026; payroll impact starts with 2027 contributions [US-MDS5-014].
- Confidence: 90%.

## 7. termination
- **Final pay:** due on or before the next regular payday. The rule is the same for discharge and resignation [US-MDS5-010].
- **Accrued vacation must be paid out** unless all three hold [US-MDS5-010]:
  - a written policy limits payout;
  - the employee was notified at hire under 3-504(a)(1);
  - the policy denies the payout.
- **ESSL:** not payable at termination [US-MDS5-013].
- UI separation notice and the Maryland Economic Stabilization Act (state WARN) were not researched (Q6; low payroll impact).
- Confidence: 90%.

## 8. benefits_in_kind
- The guide says MD withholding wages track federal withholding wages, with "similar" exclusions. Non-cash pay (lodging, meals, property) is taxed at fair market value. Tips are wages as for federal purposes. Agricultural wages subject to FICA are subject to MD withholding [US-MDS5-021].
- No Maryland departure from the 401(k)/125/HSA/transit/group-term-life exclusions was found in the sources read. The conformity statute (TG 10-203 / 10-204 starting point federal AGI) was not read (Q7).
- Confidence: 70%.

## 9. deductions_garnishments
- **Wage deductions:** only if ordered by a court, authorised in writing by the employee, allowed by the Commissioner, or required by law (LE 3-503) [US-MDS5-009].
- **Creditor attachment, CL 15-601.1** [US-MDS5-011]:
  - Exempt amount: the greater of 75% of disposable wages, or **30 × the State minimum wage × the weeks in the period** (30 × 15.00 = **450.00/week**, against the CCPA floor of 217.50).
  - Medical insurance deductions are also exempt.
  - The calculation is per pay period.
- **Child-support IWO:** Maryland fee, priority and SDU specifics were not read (Q8). The MULTI rule applies: use the law of the principal place of employment [MULTI §9].
- **State tax levy:** the guide mentions personal liability for willful non-compliance with a "wage lien" (salary lien) [US-MDS5-021]. The lien statute was not read.
- Confidence: 80%.

## 10. collective_agreements (prevailing wage)
- State prevailing wage applies to public works of **250,000 or more**. It does not apply to federally funded parts under Davis-Bacon [US-MDS5-012].
  - It extends to TIF-bond construction where authorised, and to mechanical systems service contracts above the SCA threshold.
  - Rates are set by the Commissioner [US-MDP51-006].
- The certified-payroll submission duty (SFP 17-220 range) was not read (Q9).
- Confidence: 75%.

## 11. indexation
| Item | Indexed? | Publication | register_id |
|---|---|---|---|
| State minimum wage | No (15.00 fixed since 2024) | statute | US-MDS5-005 |
| Montgomery County minimum wage | Yes, July 1, CPI-W Washington-Baltimore | DOL page / county | US-MDS5-015 |
| Standard deduction | Yes from TY2026 (IRC 1(f)(3) COLA, 2024 base, round down to 50) | Withholding Guide | US-MDS5-002, US-MDS5-021 |
| Personal exemption, brackets | No (statutory) | TG 10-105 | US-MDS5-001 |
| County rates | Set by each county (max 3.30) | Comptroller memo / DLS | US-MDS5-003, US-MDS5-004 |
| SUI wage base | No (8,500) | DOL page | US-MDP9V-001 |
| SUI table | Yearly, by trust-fund level (Tables A–F) | DOL page | US-MDP9V-001 |
| FAMLI rate | Yearly from Nov 2027 (cap 1.2%); base = SS wage base | FAMLI page | US-MDS5-014 |
| Garnishment floor | Follows State minimum wage | CL 15-601.1 | US-MDS5-011 |

## 12. data_protection
- **SSN rule, LE 3-502(d):** an employer may not print the SSN on any of these [US-MDS5-008]:
  - the wage check;
  - any attachment to the check;
  - a direct-deposit notice;
  - a card-credit notice.

  The rule covers governmental units too. This is stricter than truncation: the SSN must not appear at all. A truncated SSN on the stub should also be treated as barred; the statute says "Social Security number" without a truncation safe harbour.
- The withholding guide requires the employee's name exactly as on the Social Security card [US-MDS5-021].
- The breach-notice law (CL 14-3504) was not read.
- Confidence: 90%.

## 13. live_legal_change
1. **County rates for TY2026:** the county maximum rose to 3.30%. Dorchester and Kent are at 3.30; Allegany rose to 3.20 [US-MDS5-003, US-MDS5-004]. In force since 2026-01-01; operating level: withholding.
2. **6.25% / 6.50% state bands** (2025 BRFA, retroactive to 2025-01-01) are in the 2026 tables [US-MDS5-001, US-MDS5-003]. In force; operating level: withholding and assessment.
3. **Standard deduction indexation** from TY2026 (3,400) [US-MDS5-002]. In force; operating level: withholding.
4. **County minimum wages from 2026-07-01:** Montgomery 18.00 / 16.50 / 15.95, Howard 16.00, Prince George's 15.30 [US-MDS5-015]. In force; operating level: payroll rate.
5. **FAMLI:** contributions from 2027-01-01 at 0.9%; benefits from 2028-01-01 [US-MDS5-014]. Enacted and in force for 2027 (registration open); operating level: payroll deduction and employer contribution.
6. **BEACON wage-file spec** updated 2026-04-20 [US-MDS5-017].
7. **2026 BRFA:** per a tier-B search summary, it postponed "broader taxable income changes" to TY2027. It is not read on an official host and has no number attached (Q10). Operating level unknown; probably assessment.
8. **Next year (2027):**
   - TY2026 W-2 spec and the 2027 withholding guide: not yet published.
   - 2027 SUI table: not yet published (the DOL notice comes in January).
   - The FAMLI 2027 rate is fixed at 0.9%.

## Special populations (US-OWN-005, state level)
| Population | Maryland rule | register_id |
|---|---|---|
| Domestic / household workers | MD withholding **not required** for domestic service in a private home, local college club or fraternity/sorority chapter (voluntary arrangement possible). UI: the domestic-service coverage section was not located in this pass | US-MDS5-021 |
| Agricultural | Agricultural wages subject to FICA are subject to MD withholding. UI covers them only at 20,000 cash in a quarter or 10 workers in 20 weeks; crew-leader rules apply. Overtime after 60 h for FLSA-exempt farm work. ESSL excludes the agricultural sector | US-MDS5-021, US-MDS5-020, US-MDS5-006, US-MDS5-013 |
| Minors | Under 18: 85% of the State minimum. Montgomery: under 19 working 20 h/week or less excluded; under 20 at 85% for the first 6 months. ESSL excludes anyone under 18 at the start of the year. Under 16 working under 20 h/week exempt from minimum wage and overtime (DOL list). Work-permit rules not read | US-MDS5-005, US-MDS5-015, US-MDS5-013 |
| Tipped employees | Cash wage 3.63 (Montgomery 4.00). Tip Credit Wage Statement. Tips are withholding wages as for federal purposes. ESSL paid at not more than minimum wage | US-MDS5-007, US-MDS5-015, US-MDS5-021, US-MDS5-013 |
| Clergy / religious | Withholding not required for ministers and members of religious orders. Churches and church-controlled organizations, ministers and religious orders are outside UI | US-MDS5-021, US-MDS5-020 |
| Students | Single and student employees below the filing threshold (annual 15,750 under 65 / 17,750 aged 65+) may be exempt from withholding. UI excludes students at their own school, seasonal camp students (<13 weeks) and certified work-study | US-MDS5-021, US-MDS5-020 |
| Nonresident aliens | No MD-specific rule located beyond the general nonresident treatment (special 2.25% nonresident rate, no local) | US-MDS5-021 |
| Nonresident seamen | Not withheld while the vessel is in an MD port (oceanic/foreign trade) | US-MDS5-021 |
| Statutory employees / commission workers | UI excludes commission-only insurance producers, real estate salespersons (to the federal extent), yacht salespersons, and direct sellers / newspaper / messenger / taxi / booth renters meeting written-agreement tests | US-MDS5-020 |
| Government employees | Withholding applies. UI excludes elected officials, legislators, judges, National Guard, emergency temporaries, major policymaking posts, advisers working 8 h/week or less, and election workers under 1,000/yr. ESSL: a government unit's own system applies if it is equal or better | US-MDS5-020, US-MDS5-013 |
| Military spouses | MW507M exemption (MSRRA) | US-MDS5-021 |
| Low earners | No withholding for employees paid under 5,000 a year | US-MDS5-021 |

## ACCESS gaps (exact URLs)
- `https://www.marylandcomptroller.gov/content/dam/mdcomp/tax/instructions/2026/reporting-w2-instructions.pdf` → 404 (2026-11-02). The TY2026 W-2 spec is not yet at the expected path.
- `https://www.marylandcomptroller.gov/content/dam/mdcomp/tax/forms/2026/MW507.pdf` → 404 (guessed path). The 2026 MW507 was not obtained; the existing row US-MDP51-001 covers the certificate via the guide.
- `https://www.montgomerycountymd.gov/humanrights/minimumwage.html` → 404 (guessed path). The Montgomery County ordinance or page was not read.
- `https://www.labor.maryland.gov/labor/wages/wagehrmw.shtml` → 404 (guessed path). Content was read on `wagehrfacts.shtml` instead.
- `https://www.mdnewhire.com/faq.html` → 403. `https://mdnewhire.com/` returns only the "Employer Services Portal" shell (JavaScript). The statute (LE 8-626.1) was read instead.
- `https://mgaleg.maryland.gov/...section=3-1304.1` (local file `pdfs/MD/MD_LE-3-1304.1_mgaleg_2026-11-01.html` from the earlier pass) holds only the text "Okay". The section was not captured; the synthesis should not cite that file.

## Open questions
- **Q1** `reporting.w2.md.layout.ty2026`: the TY2026 Maryland W-2/MW508 EFW2 spec. Closes with "2026 Maryland Employer Reporting of W2s Instructions and Specifications", expected on marylandcomptroller.gov under `/tax/instructions/2026/`, usually October to December.
- **Q2** `sui.wage_base.other_state_credit`: whether wages already taxed by another state count toward MD's 8,500. The BEACON field "Out of State taxable wages" points to yes, but this rests on a file spec, not a statute. Closes with the LE Title 8 section defining taxable wages (LE 8-625 or 8-101(w) range) or the DOL employer handbook.
- **Q3** `leave.essl.multistate_scope`: whether the 12 h/week threshold and the accrual count MD hours only for an employee working partly in MD. Closes with COMAR 09.12.80 (DOL HWFA regulations) or the DOL HWFA FAQ.
- **Q4** `leave.essl.montgomery`: Montgomery County Code ch. 27 Art. XIII (pre-2017 ESSL, surviving under 3-1302(d)(2)), covering any accrual or pay-statement duty beyond State law. Closes with the county code text (codelibrary.amlegal.com is tier B; an official county page is needed).
- **Q5** `payslip.records.retention.wagehour`: the wage-hour record retention period (LE 3-424) and any e-delivery consent rule. Closes with LE 3-424 on mgaleg.
- **Q6** `termination.ui_separation_notice`: whether MD requires a written UI notice at separation (COMAR 09.32.01) and the Economic Stabilization Act (LE 11-301 ff.) payroll duties. Closes with those texts.
- **Q7** `bik.conformity.md`: Maryland conformity to federal exclusions (TG 10-203 / 10-204 / 10-205 and the annual IRC conformity act). Closes with those sections.
- **Q8** `garnish.iwo.md`: the Maryland IWO employer fee and remittance timing (Family Law 10-123 / 10-128) and the Comptroller salary-lien statute (TG 13-811). Closes with those sections.
- **Q9** `prevailing_wage.certified_payroll.md`: certified payroll filing duty (SFP 17-220) and the DOL prevailing-wage portal. Closes with SFP 17-220 on mgaleg.
- **Q10** `live.brfa2026.payroll_effect`: what the 2026 BRFA changed for TY2027 individual taxable income or withholding. Closes with the 2026 BRFA as enacted (mgaleg 2026RS chapters) or a Comptroller tax alert for 2027 withholding.
- **Q11** `sui.domestic.coverage.md`: the LE Title 8 domestic-service coverage threshold (expected 1,000 cash in a quarter, mirroring FUTA; not verified). Closes with the LE 8-2xx section on domestic service.

## Parallelism note
Q2–Q9 and Q11 are mgaleg section reads, independent of each other. One cheap worker could close them with plain curl, about 12 fetches. Q1 and Q10 depend on publication timing.
