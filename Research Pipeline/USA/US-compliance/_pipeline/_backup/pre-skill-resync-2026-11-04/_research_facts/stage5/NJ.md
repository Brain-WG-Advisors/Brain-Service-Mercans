# Stage 5 — New Jersey (NJ): 13-domain findings

Worker: compliance-source-hunter, 2026-11-02. Brief: `_prompts/stage5-brief.md`. Mandate block: US-MQ-51 (answered at seal attempt 5).
Budget declared: 60 fetches / 2 h. Used: about 45 fetches (35 curl, 10 web searches) and about 35 min. I stopped acquiring at the 75% fetch mark.
Register shard: `00-official-sources/_register-shards/S5-NJ.csv` (25 rows, US-NJS5-001..025: 24 active, 1 partial; tiers A.1 ×8, A.2 ×13, A.3 ×4; no tier-B row carries a number). New sources: `00-official-sources/ccg-sources/NJ/` (17 files, 2.2 MB, none above 1 MB).
Active rows reused, not re-fetched: US-NJP51-001 (NJ-WT Sept 2025, re-read in full; a fresh download on 2026-11-02 is byte-identical, md5 3357da32…), US-NJP51-002 (percentage-method tables), US-NJP51-004 (M-6025 2026), US-NJP51-007 (Prevailing Wage Act), US-NJP52-002 / US-NJP6-003 (Treasury payroll page), US-NJP6-001 (Jersey City), US-NJP6-002 (Newark), US-NJP7-001..006 (levies), US-NJP8-001 (34:11-4.6 pay statement), US-NJP9M-001 (gender-equity notice), US-NJR3-004/-005 (POA forms), US-FEDR3-010 (ESL notice language). The local Selected-Labor-Laws reprint (`pdfs/NJ/NJ_DOL-selectedstatelaborlaws_2026-10-30.html`) was mined again for 34:11-4.2 to 4.4a, N.J.A.C. 12:55-2.1 to 2.5 and Appendix A (rows 001–005 and 022).

**Process incident, to be fixed by the orchestrator.** The scratchpad directory is shared by the parallel Stage-5 workers. My first `addrow.py` was overwritten by the VA worker's copy of the same name, so batch 1 (US-NJS5-001..011) was appended to `S5-VA.csv`. I removed those 11 rows from `S5-VA.csv` within the minute. Before my write the file held only the header that my write had created, so no VA row was touched. `S5-VA.csv` now contains just the header line. I re-wrote the 11 rows to `S5-NJ.csv`, with my helpers moved into `scratchpad/NJw/`. Please check that the VA worker's later rows landed after that header.

---

## 1. labour_code
- **Minimum wage 2026** (in force from 2026-01-01) [US-NJS5-009]:
  - most employees: **15.92 USD/h**;
  - seasonal and small employers (fewer than 6 employees): **15.23**;
  - farm workers paid hourly or piece-rate: **14.20**;
  - direct care staff in long-term care facilities: **18.92**;
  - tipped employees: cash wage **6.05**, maximum tip credit **9.87**.
- **Minimum wage 2027** (already published, from 2027-01-01) [US-NJS5-008; DOL FAQ banner US-NJS5-012]:
  - most employees: **16.48**;
  - small/seasonal employers: **16.25**;
  - farm: **15.00**;
  - long-term care: **19.48**;
  - tipped: cash wage **6.61**, tip credit stays **9.87**.
  - G-DERIVE, run in Python: 6.05 + 9.87 = 15.92 and 6.61 + 9.87 = 16.48. Long-term care = general rate + 3.00 in both years.
- **Local minimum wages:** none found. No NJ municipality appears in DOL material. Local payroll taxes are covered in §2.
- **Overtime:** 1.5× the regular rate for hours actually worked above 40 in a 7-day workweek [US-NJS5-012].
  - No daily overtime and no holiday or weekend premium.
  - Paid holiday hours do not count toward the 40.
  - The right cannot be waived.
  - With several pay rates, use the weighted-average regular rate with a half-time premium.
  - Exempt: executive, administrative and professional employees on salary.
  - Excluded from minimum wage: auto salespersons, outside salespersons, and minors except in the listed industries.
- **Pay frequency** [US-NJS5-001]:
  - at least twice each calendar month, on regular paydays set in advance;
  - overtime-exempt classes may be paid monthly (N.J.A.C. 12:55-2.4(k));
  - a payday falling on a nonwork day moves to the preceding work day;
  - the pay period must end no more than **10 working days** before the payday.
- **Method of payment** [US-NJS5-001, US-NJS5-002]:
  - cash or a check that can be cashed without difficulty; the employer pays check-cashing fees at the drawee bank and check-deposit-return fees;
  - **direct deposit** only with prior written, uncoerced consent; it may not be a condition of hire or employment, and the employee may revoke it;
  - **paycard** needs the same consent, plus written disclosure of all features and fees, one free full withdrawal per pay period, and an opt-out.
- **Domestic workers:** the Domestic Workers' Bill of Rights has applied since 2024-07-01. A household employing a domestic worker for more than 5 h/month must give a written contract in the worker's language. The implementing rule was proposed (NJ Register 2025-09-02); adoption is unconfirmed [US-NJS5-025].
- Confidence: 92%. The statutory text of 34:11-56a4 (overtime and minimum wage) was not read; the DOL FAQ and press releases were used instead.

## 2. income_tax
- **Method:** NJ-WT (September 2025) is still the current edition; the 2026-11-02 download is byte-identical [US-NJP51-001, US-NJS5-006]. The percentage-method tables apply to wages paid on and after 2020-10-01 [US-NJP51-002].
  - Rate A: filing status box 1 or 3.
  - Rate B: box 2, 4 or 5 with line 3 blank.
  - Otherwise the rate letter the employee picks on line 3.
  - Allowance per period: weekly 19.20, biweekly 38.40, semimonthly 41.60, monthly 83.30, quarterly 250, semiannual 500, annual 1,000, daily 2.70.
  - Wages "may be rounded to the nearest dollar".
  - The employer may apply to the Director for another method.
- **Certificate:** NJ-W4, edition **(1-21)**. Lines: 2 filing status, 3 rate letter from the wage chart (for two earners or several jobs with combined wages above 50,000), 4 allowances, 5 additional amount, 6 "EXEMPT" [US-NJS5-024]. The federal W-4 may not be used for NJ. Certificates stay with the employer and go to the Division only on request [US-NJP51-001].
- **Supplemental wages:**
  - paid with regular wages: withhold on the combined amount;
  - paid separately: withhold without allowances;
  - payouts of accumulated sick or vacation time count as supplemental.
  - NJ has **no flat supplemental rate** [US-NJP51-001].
- **Residence and work location** [US-NJP51-001; US-NJP52-002]:
  - Residents: withhold on all wages. Exception: wages earned entirely outside NJ that are subject to another state's withholding at least as high as NJ's. Otherwise withhold NJ on top, reduced by the other state's withholding.
  - Nonresidents: withhold on NJ-source wages only, allocated by NJ days ÷ total days if exact records are lacking.
  - Since TY2023, a **convenience-of-the-employer** test applies to residents of states that use one.
  - **Reciprocity with PA only**, through Form **NJ-165**, which also serves military spouses under the SCRA. The agreement does not cover PA local wage taxes.
- **Courtesy withholding:** with the employee's written authorization, an NJ employer may withhold another state's or locality's tax (N.J.A.C. 12:55-2.5) [US-NJS5-005].
- **Local taxes:** there is no local income tax withheld from employees. The only local taxes are the **employer-paid 1% payroll taxes of Newark and Jersey City** [US-NJP6-001, US-NJP6-002]. The enabling law forbids any deduction from employee pay (C.40:48C-16(e)). Returns and payments are quarterly, due the last day of April, July, October and January.
  - S.B. 4219 adds that the local tax does not apply when the employee's remuneration is subject to an out-of-state employer payroll tax, once documentation is filed with the city [US-NJS5-013; see §13].
  - LEVEL: employer reporting, not withholding.
- **Domestic employers:** withhold NJ tax only where federal withholding applies. They file annually [US-NJP51-001].
- Confidence: 95%.

## 3. social_security (UI, TDI, FLI, WF/SWF)

| Item | 2026 | 2027 (published) | Source |
|---|---|---|---|
| Worker UI | 0.3825% | 0.3825% | US-NJS5-010 |
| Worker WF/SWF | 0.0425% | 0.0425% | US-NJS5-010 |
| Worker DI (TDI) | 0.19% | **0.24%** | US-NJS5-010 |
| Worker FLI | 0.23% | **0.24%** | US-NJS5-010 |
| Governmental reimbursable worker UI | 0.0825% | 0.0825% | US-NJS5-010 |
| Wage base UI + WF/SWF (worker and employer) and TDI employer | 44,800 | 46,400 | US-NJS5-010, US-NJS5-011 |
| Wage base TDI/FLI, worker | 171,100 | 177,100 | same |
| New employer UI / DI / WF-SWF / FLI (FY 2025-26 and 2026-27) | 2.6825% / 0.50% / 0.1175% / 0 | — | US-NJS5-010 |
| Employer UI range FY 2026-27 (Table C) | total 0.5%–5.8%, UI part 0.3825%–5.6825% | — | US-NJS5-023 |
| Max weekly benefit TDI/FLI · UI · WC | 1,119 · 905 · 1,199 | 1,158 · 937 · 1,241 | US-NJS5-010 |

- The 2026 worker amounts were cross-checked against Treasury M-6025: 0.425% × 44,800 = **190.40**; 0.19% × 171,100 = **325.09**; 0.23% × 171,100 = **393.53** [US-NJP51-004]. This is the second independent authority.
- **Experience rate:** reserve ratio = reserve balance ÷ average annual payroll. New employers keep the new-employer rate for 3 calendar years. Voluntary contributions use Form UC-45 [US-NJS5-010].
- **Taxable remuneration for UI/TDI/FLI is broader than for NJ GIT** [US-NJS5-017]. It includes:
  - 401(k) deferrals and Section 125 contributions, to the extent the employee could have taken cash;
  - dependent care assistance;
  - personal use of a company car;
  - S-corp officer distributions;
  - contractual or customary separation pay;
  - sick-pay continuation and top-ups.
  - State-plan or approved private-plan TDI/FLI benefits are **not** wages.
- **In-kind values (N.J.A.C. 12:16-4.8)**, used only when the employer assigns no value [US-NJS5-010]:
  - 2026: room and board 301.50/week; lodging 129.20/week; meals 34.50/day (breakfast 10.40, lunch 10.40, dinner 13.80);
  - 2027: 312.30; 133.90; 35.70 (10.70 / 10.70 / 14.30).
- **TDI/FLI benefit side:**
  - TDI up to 26 weeks; FLI up to 12 consecutive weeks or 56 intermittent days.
  - The benefit is 85% of the average weekly wage, capped at 70% of SAWW.
  - State-plan TDI is third-party sick pay: the Division withholds the employee's FICA on the employer-attributable portion. FIT is withheld only if the worker files Form W4S.
  - An approved private plan replaces the State-plan contributions [US-NJS5-019].
- **Levies:** P7 rows reused (US-NJP7-001..006). The Health Care Subsidy Fund rate is 0.0000% in Table C [US-NJS5-023].
- **G-DERIVE / G-CALIBER** (Python). The indexing caliber is the **statewide average weekly wage (SAWW) of the second preceding year**: 2024 SAWW = **1,598.66** [US-NJS5-011].
  - 70% × 1,598.66 = 1,119.06 → **1,119** (TDI max).
  - 56⅔% × 1,598.66 = 905.91 → **905** (UI max, truncated).
  - 75% × 1,598.66 = 1,198.995 → **1,199** (WC max).
  - 28 × 1,598.66 = 44,762.48 → **44,800** (UI base, rounded up to the next 100).
  - 107 × 1,598.66 = 171,056.62 → **171,100** (TDI/FLI worker base, rounded up to the next 100).
  - The 2027 figures imply a 2025 SAWW of about 1,654–1,657, consistent across all four quantities (46,400/28, 177,100/107, 1,158/0.70, 937/0.5667).
  - The multipliers 28 and 107 and the rounding rules are **inferred** from exact reproduction. The statutory text (N.J.S.A. 43:21-7(b)(3), 43:21-3(c), 43:21-46) was not read.
- Confidence: 95%.

## 4. payslip_statute
- **Content (34:11-4.6(c))** [US-NJP8-001]:
  - a statement of deductions for each pay period in which deductions are made;
  - employers with **10 or more employees**, public employers included, add gross wages, net wages, rate of pay and, where relevant, hours worked.
- **Delivery:** electronic is allowed unless the employee asks for paper.
- **Notices:** pay rate and payday at hire; any change before it takes effect (34:11-4.6(a),(b)).
- **Retention:** wage and hour records **6 years**, kept at the workplace or a central NJ office [US-NJS5-022]. Required content of those records:
  - name, address, and birth date if under 18;
  - hours worked each day and each week;
  - gross-to-net with itemized deductions;
  - tips, and tip reports carrying the SSN;
  - substantiation of any food or lodging credit.
- **Other retention periods:** UI/TDI records for the current year plus 4 preceding years [US-NJS5-017]. Earned sick leave records 5 years [US-NJS5-007].
- **Language:** no payslip-language rule (US-OWN-006). Gender-equity notice: US-NJP9M-001.
- Confidence: 93%.

## 5. reporting_instruments
- **Withholding (Treasury)** [US-NJP51-001]:
  - **NJ-927** quarterly, mandatory electronic, due the 30th of the month after the quarter (next business day per NJ-WT), filed even with zero tax.
  - **NJ-500** monthly payment, due the 15th, if more than 500 USD was withheld in month 1 or 2 of the quarter. The third month is paid with the NJ-927.
  - **NJ-927-W** for weekly payers: prior-year liability of 10,000 USD or more, paid on the payroll frequency.
  - **NJ-927-H** for domestic employers: annual, due January 31.
  - **NJ-W-3** annual reconciliation by **February 15**, or within 30 days after wages stop. The NJ-W-3 and every W-2/W-2G/1099 have been mandatory electronic since TY2020. Channels: online, the Online Upload Service (pre-specified format), Axway bulk transfer for 100+ forms, or third-party software.
  - EFT payment codes: quarterly 01130, monthly 01120, weekly 01170. Tax-period end date format: YYMMDD.
  - W-2 box 16 rules: §8. the W-2 must show the combined UI/WF/SWF amount and DI and FLI separately (NJ-WT p.16; amounts per Treasury M-6025, US-NJP51-004).
- **UI wage report:** **WR-30** [US-NJS5-017, US-NJS5-010].
  - Content per employee: SSN (an ITIN is not valid), name, gross NJ wages, base weeks.
  - Due the 30th of the month after the quarter, with **no** weekend or holiday extension (DOL rate-info page). Note that this conflicts with NJ-WT's "next business day" for the NJ-927: two authorities, two rules. The DOL rule is the stricter one.
  - Mandatory electronic, online or SFTP (SFTP needs prior authorization).
  - Penalties: 5 / 10 / 25 USD per employee.
  - Severance paid under contract or policy goes on the WR-30 with **0 base weeks**. Pay in lieu of notice counts as base weeks. A base week requires 20 × the prior-year minimum wage: **310** in 2026, **319** in 2027.
- **New-hire reporting** [US-NJS5-018]: N.J.S.A. 2A:17-56.61.
  - Report within **20 days** of hire, rehire or return to work.
  - Independent contractors must be reported too. This is an NJ-specific rule.
  - Required fields: name, address, SSN, DOB, date of hire (first day of paid services); employer name, IWO address and FEIN (the same FEIN as for wage reporting).
  - Channels: the CSESP portal, file upload or SFTP, form, printed list, or W-4.
  - Fine up to 25 USD.
  - The portal also takes termination reports and IWO responses.
  - The older DOL handbook still lists DOB and hire date as optional; CSESP is the directory operator and controls [US-NJS5-016].
- **Separation notice:** **BC-10** (8/23), given at every separation, permanent or temporary [US-NJS5-015]. Separation-information requests (BC-3E.1 / BC-28) must be answered within 10 days [US-NJS5-016].
- **Local:** Newark and Jersey City quarterly employer payroll tax returns [US-NJP6-001/-002; US-NJS5-013].
- **Registration and POA:** reused (US-NJR3-004 M-5008-R; US-NJR3-005 DOL POA).
- Confidence: 93%.

## 6. leave
- **Earned Sick Leave** (N.J.S.A. 34:11D-1 et seq., DOL guide MW-566 12/23) [US-NJS5-007]:
  - covers all employers;
  - accrual of 1 h per 30 h worked up to 40 h per benefit year, or front-loading of at least 40 h;
  - usable from day 120;
  - paid at the normal rate and at least the minimum wage, in the same or next pay period;
  - unused leave: carry over (use capped at 40 h a year) **or** pay out at the end of the benefit year;
  - documentation may be required after 3 or more consecutive days;
  - records kept 5 years.
  - Payout at termination is not stated as required; the statute was not read (Q8).
- **TDI/FLI** benefits come from the State plan or a private plan, not through payroll. See §3 for how they interact with payroll [US-NJS5-019].
- Vacation and holiday pay are not required by NJ law; if offered, the policy is enforceable [US-NJS5-012]. Jury duty: unpaid time off is protected [US-NJS5-012].
- Confidence: 88%.

## 7. termination
- **Final pay:** by the regular payday for the period in which employment ended, for discharge, layoff and resignation alike. Labor-dispute suspension involving payroll staff: +10 days. Paid by mail if the employee asks [US-NJS5-003]. N.J.A.C. 12:55-2.4(a) words this as "within 10 days from the end of the work period".
- **Accrued vacation:** no statutory payout; the policy or contract governs [US-NJS5-003, US-NJS5-012].
- **Deductions from final pay** for unreturned property: prohibited [US-NJS5-012].
- **Separation notice:** BC-10 to every separated worker [US-NJS5-015].
- **NJ WARN** (N.J.S.A. 34:21-1 et seq.): employers with 100+ employees [US-NJS5-020].
  - Mass layoff: 50+ terminations in 30 days.
  - **Mandatory severance of 1 week per full year of service**, plus **4 weeks** if notice is shorter than 90 days.
  - Pay rate: the higher of the 3-year average regular rate or the final rate.
  - The employee receives the greater of statutory and CBA/policy severance.
  - Payroll impact: a separate earning type. For UI it is separation pay (WR-30, 0 base weeks).
  - DOL handbook: notify DOL 48 h before a separation of 25+ workers for 7+ days [US-NJS5-016].
- **Death of employee:** wages may be paid, on demand and without letters of administration, in a statutory order: spouse, adult children, parents, siblings or whoever paid the funeral (34:11-4.5; local reprint, no separate row).
- Confidence: 88% (WARN rests on the DOL form's restatement, not the statute).

## 8. benefits_in_kind (state conformity)
- **NJ GIT (withholding, W-2 box 16)** [US-NJS5-006]:
  - **401(k):** excluded up to the federal limit.
  - **403(b), 457 and other employee retirement deferrals:** **taxable when contributed**.
  - **Section 125:** only plans requiring purchase of minimum medical/life/LTD coverage, or the cash-option cases listed, are excluded. Other cafeteria contributions are taxable, and "amounts taken out of cafeteria plans" count as wages.
  - **IRC 129 dependent care** and **IRC 137 adoption:** included in NJ wages.
  - **Commuter transportation:** excluded up to a limit, with proof of payment.
  - **Archer MSA:** excluded.
  - **HSA (IRC 223):** **not excluded**. The conformity bill A2634 is pre-filed for 2026 and not enacted [US-NJS5-014]. LEVEL: withholding.
  - TDI benefits: not NJ-taxable.
  - **Group-term life:** follows the federal treatment; no NJ departure was found in NJ-WT ("generally, if federal compensation then NJ").
- **UI/TDI/FLI base:** 401(k) and 125 contributions **are** wages where cash was electable. Personal use of a company car counts at IRC 61 value [US-NJS5-017].
- **Board and lodging values:** §3 [US-NJS5-010].
- Confidence: 90%.

## 9. deductions_garnishments
- **Wage deductions:** closed list (34:11-4.4; N.J.A.C. 12:55-2.1 to 2.3) [US-NJS5-004].
  - Written authorization is needed for benefits, savings and political deductions.
  - Political deductions: at most 5 USD a week, to one committee only.
  - Employer approval is needed for several categories.
  - **No deductions** for shortages, breakage, damage, unreturned property, uniforms, testing or job-required licenses [US-NJS5-012].
- **Creditor wage execution (N.J.S.A. 2A:17-56; court form CN 11471, rev. 07/01/2022)** [US-NJS5-021]:
  - withhold the **lesser of 10% of gross**, 25% of disposable earnings, or disposable earnings above 217.50/week (435.00 biweekly, 471.25 semimonthly, 942.50 monthly);
  - **never more than 10% of gross**;
  - **one execution at a time**;
  - give the debtor a copy immediately.
  - 217.50 = 30 × 7.25 (derived). This is stricter than the CCPA's 25%.
  - Higher court-ordered percentages (income above 250% of poverty, State debts) appear only in tier-B summaries; the statute was not read (Q5).
- **Child support IWO:** handled through the CSESP portal [US-NJS5-018]. NJ fee and priority specifics were not read (Q5). The federal layer is in the FED unit.
- **Courtesy deduction for State debts:** voluntary, with written authorization (12:55-2.3) [US-NJS5-004].
- Confidence: 85%.

## 10. collective_agreements (prevailing wage)
- **Prevailing Wage Act** (N.J.S.A. 34:11-56.25 et seq.): certified payroll is filed through the NJ Wage Hub within 10 days of each payment [US-NJP51-007, reused]. Threshold and rate determinations are not refreshed in this pass.
- Confidence: 80%.

## 11. indexation
- **Minimum wage:** CPI (BLS) under N.J. Const. Art. I ¶23 and N.J.A.C. 12:56-3.1(c). Announced each autumn by DOL press release; the 2027 release is dated 2026-09-29 [US-NJS5-008].
  - The small/seasonal employer schedule ends in 2028 and the farm schedule in 2030; after that they index like the general rate.
  - Tipped: only the cash wage moves; the tip credit stays fixed at 9.87.
  - The CPI-W index values are not in the press release, so no CPI derivation is attempted.
- **UI/TDI/FLI wage bases and maximum benefits:** SAWW of the second preceding year; announced each December by DOL press release and the rate-info page [US-NJS5-011, US-NJS5-010]. The derivation is in §3.
- **Base week and alternative earnings:** based on the minimum wage in force on October 1 of the prior year [US-NJS5-011].
  - Base week: 20 × 15.49 = 309.80 → 310 (2026); 20 × 15.92 = 318.40 → **319** (2027).
  - Alternative earnings: 1,000 × 15.49 → 15,500; 1,000 × 15.92 → **16,000**.
  - Both are consistent with rounding up (to the next dollar and the next 100 respectively). The rounding rule is inferred.
- **Withholding tables:** not indexed. They have been unchanged since 2020-10-01 [US-NJP51-002].
- **W-2 notice of worker contributions:** Treasury M-6025 (8-2026) [US-NJP51-004].

## 12. data_protection
- **SSN handling:** valid SSNs are mandatory in UI records (N.J.A.C. 12:16-2.2(a)1); DOL recommends SSNVS or E-Verify [US-NJS5-017].
- **SSN on pay statements:** the Identity Theft Prevention Act (P.L.2005, c.226, C.56:8-164) was **not obtained**: pub.njleg.gov failed to connect twice (ACCESS gap; Q2). No truncation rule is asserted.
- **Confidentiality:** ESL reasons are confidential unless the employee consents in writing [US-NJS5-007]. UI employer information is confidential [US-NJS5-017]. Local payroll-tax returns are confidential (C.40:48C-16(f)) [US-NJS5-013].
- Confidence: 60%.

## 13. live_legal_change (2026-01-01 → 2026-11-02, and 2027 already enacted)
- **2027 minimum wages** published 2026-09-29: in force 2027-01-01 [US-NJS5-008].
- **2027 UI/TDI/FLI rates and bases** published on the DOL rate-info page: worker DI 0.24% and FLI 0.24% (up from 0.19% and 0.23%); bases 46,400 and 177,100 [US-NJS5-010]. The Treasury M-6025-style notice for 2027 has not been seen yet.
- **FY 2026-27 UI Table C** in force 2026-07-01 [US-NJS5-023].
- **S.B. 4219: local employer payroll tax administration** [US-NJS5-013, status `partial`].
  - Identity: Senate No. 4219, 221st Legislature, Third Reprint. Amends C.40:48C-15, -16 and -18 and R.S.54:50-9.
  - Status: the text was read as reported 2026-01-05. Signature on 2026-02-18, effective immediately, comes **only from a tier-B source** (EY 2026-0463, US-NJR3-003). The chapter number was not obtained.
  - Level: employer-paid local tax and employer reporting (no withholding effect).
- **A2634 HSA conformity:** pre-filed for the 2026 session, **not enacted**. Level: withholding [US-NJS5-014].
- **Domestic Workers' Bill of Rights rule:** proposed (NJR 2025-09-02), adoption not confirmed [US-NJS5-025].
- **NJ-WT:** no 2026 edition. The Sept 2025 file is unchanged [US-NJS5-006].
- **Not swept:** the Treasury news page (`/treasury/taxation/news.shtml` returned 404). The full DOL press-release index for 2026 also 404'd. The sweep is therefore partial (Q6).

---

## Special populations (US-OWN-005, state round)

| Population | NJ rule affecting payroll | register_id |
|---|---|---|
| Domestic / household | UI/TDI coverage once cash wages reach 1,000 USD in a quarter. Annual NJ-927-H plus four WR-30s by 30 January (DOL handbook); NJ-WT says January 31 for the NJ-927-H, so use the earlier date. NJ GIT withheld only where federal withholding applies. Written contract if > 5 h/month (DWBR) | US-NJS5-017, US-NJP51-001, US-NJS5-025 |
| Agricultural | Minimum wage 14.20 (2026) → 15.00 (2027), schedule to 2030. UI coverage if 20,000 USD cash in a quarter or 10+ workers in 20 weeks; crew-leader rule | US-NJS5-009, US-NJS5-008, US-NJS5-017 |
| Minors | Working papers for all under 18. Minimum wage applies only in the listed industries. 30-minute meal break after 5 h. Birth date recorded. Hour limits not read (Q10) | US-NJS5-012, US-NJS5-022 |
| Tipped | Cash wage 6.05 (2026) / 6.61 (2027), tip credit 9.87, employer tops up to the minimum wage. Tips are UI wages if reported in writing; service charges are remuneration | US-NJS5-009, US-NJS5-008, US-NJS5-017 |
| Clergy / religious | Church service exempt from NJ UI. No NJ GIT rule beyond federal (NJ-WT read; none found) | US-NJS5-017, US-NJP51-001 |
| Students | Service by a student at their own school is exempt from UI. ESL and minimum wage apply (no student sub-minimum in NJ) | US-NJS5-017, US-NJS5-012 |
| Nonresident aliens | No NJ-specific NRA withholding rule found in NJ-WT (contrast NC). Wages of aliens are UI-taxable under a valid SSN | US-NJP51-001, US-NJS5-017 |
| Statutory employees | No state rule beyond federal found. Home-to-home commission salespersons are exempt from UI | US-NJS5-017 |
| Government employees | Governmental reimbursable worker UI 0.0825% (2026 and 2027); government contributing-employer UI 0.5% (2026) | US-NJS5-010, US-NJS5-011 |
| Long-term care direct care staff | Minimum wage 18.92 (2026) / 19.48 (2027) | US-NJS5-009, US-NJS5-008 |
| Small/seasonal employers (< 6 employees) | Minimum wage 15.23 (2026) / 16.25 (2027) | US-NJS5-009, US-NJS5-008 |
| PA residents, military spouses | No NJ withholding with Form NJ-165 on file | US-NJP51-001 |

---

## ACCESS gaps (exact URLs)
- `https://pub.njleg.gov/Bills/2004/PL05/226_.HTM` and `https://pub.njleg.gov/bills/2004/PL05/226_.HTM`: curl returned status 000 (connection failed), twice. Needed for the SSN rule, C.56:8-164.
- `https://lis.njleg.state.nj.us/nxt/gateway.dll?f=templates&fn=default.htm&vid=Publish:10.1048/Enu`: the NJ statutes database renders only in a browser (see US-NJP9M-001). Not tried with curl. Sections needed: 2A:17-56, 34:21-2, 34:11-56a4, 34:11D-2/-3, 43:21-6(a), 43:21-7(b)(3), 56:8-164.
- `https://www.njleg.state.nj.us/bill-search/2024/S4219`: a JS application. Needed for the chapter number and approval date of S.B. 4219.
- `https://www.njcourts.gov/sites/default/files/forms/11471_wage_exec_appndx_xi_j.pdf`: 403. The Wayback `2026id_` copy was used instead (row US-NJS5-021).
- `https://www.nj.gov/treasury/taxation/news.shtml`: 404. `https://www.nj.gov/labor/lwdhome/press/2026/`: 404. Bulletin sweep incomplete.
- `https://www.nj.gov/labor/employer-services/warn/`: returns an Incapsula meta-refresh to `https://www.nj.gov/labor/business-services/layoffs-and-closing/file-warn-notice/` (not followed; the WARN form was used instead).
- `https://www.nj.gov/labor/wageandhour/tools-resources/laws/minimumwage.shtml`: 404 (the press releases and FAQ were used instead).

## Open questions
- **Q1** S.B. 4219: chapter number (P.L.2026, c.?) and approval date from an A.1 source. *Closes with:* the njleg bill-search page or the chaptered law text (browser pass).
- **Q2** SSN truncation or printing limits on pay statements (C.56:8-164). *Closes with:* the P.L.2005 c.226 text on pub.njleg.gov, or the statutes database (browser pass).
- **Q3** BC-10: whether employers must send DOL an electronic copy at the same time as they hand the form to the worker (tier-B leads only, citing a 2021–2023 amendment). *Closes with:* N.J.S.A. 43:21-6(a) amended text or the DOL employer-resources page for BC-10.
- **Q4** NJ WARN: statute text, including the timing of severance payment (tier B says a lump sum on the termination date). *Closes with:* N.J.S.A. 34:21-2 text.
- **Q5** Garnishment: 2A:17-56 text on above-10% orders, plus NJ child-support IWO fee and priority rules. *Closes with:* the statute (browser pass) and the CSESP NJ LSP Employer Guide (`https://www.njcsesp.com/files/NJ_LSP_Employer_Guide.pdf`, not fetched).
- **Q6** Treasury 2026 bulletin sweep (withholding changes, 2027 notice of worker-contribution amounts). *Closes with:* the Division of Taxation "What's New" / notices index (current URL unknown; the old one 404s).
- **Q7** UI/TDI/FLI multipliers (28 × SAWW, 107 × SAWW) and rounding rules are inferred from exact reproduction. *Closes with:* N.J.S.A. 43:21-7(b)(3) and 43:21-3(c) text.
- **Q8** Earned Sick Leave: statutory carry-over cap and treatment at termination. *Closes with:* N.J.S.A. 34:11D-2/-3 text or the mysickdays.nj.gov FAQ.
- **Q9** Domestic Workers' Bill of Rights: chapter number and adoption status of the rule. *Closes with:* the NJ Register adoption notice.
- **Q10** Minor hour limits (N.J.S.A. 34:2-21.2 et seq.). *Closes with:* the DOL youth-employment page.
- **Q11** NJ-927 due date on weekends and holidays: NJ-WT says next business day; DOL rate-info says no extension (for the NJ-927 and WR-30). *Closes with:* a written Treasury/DOL statement. Until then, build to the stricter DOL rule.

**Shape of the remaining work.** Q1, Q2, Q4, Q5, Q7, Q8 and Q10 all sit behind the browser-only NJ statutes database or njleg bill search. One browser pass can close them together.

**Confidence (overall NJ): about 90%.** Numbers: 97% (all from A.2 pages, cross-checked by arithmetic or a second authority). Rules resting on the statute's own text, as opposed to an agency restatement: about 80%.
