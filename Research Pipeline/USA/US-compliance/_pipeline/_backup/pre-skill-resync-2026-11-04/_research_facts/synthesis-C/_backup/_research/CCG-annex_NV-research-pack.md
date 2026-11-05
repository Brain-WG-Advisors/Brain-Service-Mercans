# CCG research pack - annex_NV (Nevada)

Synthesis-B worker MN-WY, 2026-11-02. Unit `annex_NV` of the CCG (jurisdiction annex, all 13 domains + special populations).
Facts file: `_research/CCG-annex_NV-facts.json` (39 facts, 6 pending on the register_id pattern defect, 9 unresolved). Every claim below carries its register_id inline; numbers may be cited in the CCG only through a fact key.

## 0. How to use this pack

- Body sections 1-13 and Special populations are the stage-5 findings (`_research/stage5/NV.md`), carried verbatim because they are already organised by the 13 CCG domains with register ids inline.
- Federal layer (FIT, FICA, FUTA, W-2/941/940), the multistate rules (reciprocity, sourcing) and the language seams (US-OWN-006: payslip in English; second-language duties attach to notices and posters only) live in annex_FED / annex_MULTI and are not repeated here.
- Special populations (US-OWN-005): the state-level rules are in the Special populations table below; the country-wide coverage matrix is CCG unit `coverage`.
- Values are 2026 unless the fact says otherwise. 2027 values appear only where the row carries an enacted or published 2027 figure; projections are never facts.

## 0.1 Synthesis decisions and traps (bind the builder)

- NV has NO wage tax (T1). The MBT (1.17% over 50,000/quarter) is an EMPLOYER tax on UI wages; from 2026 Taxation reconciles MBT wages with ESD wages each quarter - DD must make MBT line 1 = UI gross wages.
- Daily overtime >8 h applies only to employees earning less than 18.00/h (1.5x minimum) from 2026-07-01.
- UI 2027 base 45,400 is derived from the DETR R&A memo by the 612.545 rule (medium); re-check against the DETR 2027 notice.
- Do not model NRS 608.250 two-tier minimum (overridden by the Constitution).

## 0.2 Register status check of the ids cited in the findings

All ids cited in the findings are `active` in the register.

## 0.3 Facts emitted

| key | value | from | to | register_id | conf |
|---|---|---|---|---|---|
| `nv.minwage.hourly` | 12.0 USD | 2024-07-01 |  | US-NVS5-013 | high |
| `nv.minwage.tip_credit.allowed` | False | 2024-07-01 |  | US-NVS5-013 | high |
| `nv.overtime.daily_threshold_hours` | 8 hours | 2025-10-01 |  | US-NVS5-001 | high |
| `nv.labour.overtime.daily_ot_wage_ceiling.hourly` | 18.0 USD | 2026-07-01 | 2027-06-30 | US-NVS5-003 | high |
| `nv.overtime.weekly_threshold_hours` | 40 hours | 2025-10-01 |  | US-NVS5-001 | high |
| `nv.overtime.premium.multiplier` | 1.5 ratio | 2025-10-01 |  | US-NVS5-001 | high |
| `nv.pay_frequency.rule` | at least semimonthly (by 15th / last day of month) | 2025-10-01 |  | US-NVS5-001 | high |
| `nv.payment.method` | cash or negotiable check unless employee agrees in writing to another disposition | 2025-10-01 |  | US-NVS5-001 | high |
| `nv.labour.lodging_credit.weekly_multiple_of_minwage` | 5 | 2025-10-01 |  | US-NVS5-001 | high |
| `nv.pit.exists` | False | 2026-01-01 |  | US-NVS5-014 | high |
| `nv.local_wage_tax.exists` | False | 2026-01-01 |  | US-NVS5-014 | high |
| `nv.sui.wage_base` | 45400 USD | 2027-01-01 | 2027-12-31 | US-NVS5-019 | medium |
| `nv.sui.new_employer.rate` | 2.95 % | 2026-01-01 |  | US-NVS5-006 | high |
| `nv.ui.cep.rate` | 0.05 % | 2026-01-01 |  | US-NVS5-006 | high |
| `nv.sui.wage_base.other_state_credit` | True | 2026-01-01 |  | US-NVS5-006 | high |
| `nv.sui.wages.401k_included` | True | 2026-01-01 |  | US-NVS5-006 | medium |
| `nv.mbt.general.rate` | 1.17 % | 2026-01-01 |  | US-NVS5-011 | high |
| `nv.mbt.general.quarterly_threshold` | 50000 USD | 2026-01-01 |  | US-NVS5-011 | high |
| `nv.mbt.financial_mining.rate` | 1.554 % | 2026-01-01 |  | US-NVS5-011 | high |
| `nv.mbt.base` | UI gross wages + tips as reported to ESD less employer-paid health benefits | 2026-01-01 |  | US-NVS5-011 | high |
| `nv.payslip.items` | itemized deductions each payment; available paid-leave hours each payday (50+ NV employees) | 2025-10-01 |  | US-NVS5-001 | high |
| `nv.records.retention_years` | 2 years | 2025-10-01 |  | US-NVS5-001 | high |
| `nv.report.ui.quarterly_due` | Apr 30; Jul 31; Oct 31; Jan 31 (received) | 2026-01-01 |  | US-NVS5-008 | medium |
| `nv.report.mbt.due` | last day of month after quarter (file even if no tax) | 2025-12-02 |  | US-NVS5-010 | high |
| `nv.newhire.report_days` | 20 days | 2026-01-01 |  | US-NVS5-007 | high |
| `nv.leave.paid.coverage_min_employees` | 50 | 2025-10-01 |  | US-NVS5-001 | high |
| `nv.leave.paid.accrual_per_hour_worked` | 0.01923 hours | 2025-10-01 |  | US-NVS5-001 | high |
| `nv.leave.paid.payout_at_separation` | False | 2025-10-01 |  | US-NVS5-001 | high |
| `nv.leave.dv_sa.hours_per_12_months` | 160 hours | 2025-10-01 |  | US-NVS5-001 | high |
| `nv.final_pay.discharge` | immediately | 2025-10-01 |  | US-NVS5-001 | high |
| `nv.term.final_pay.resignation` | earlier of regular payday or 7 days | 2025-10-01 |  | US-NVS5-001 | high |
| `nv.garn.consumer.low_wage.max_rate` | 18 % | 2026-01-01 |  | US-NVS5-004 | high |
| `nv.garn.creditor.max_percent` | 25 % | 2026-01-01 |  | US-NVS5-004 | high |
| `nv.garn.consumer.low_wage.weekly_threshold` | 770 USD | 2026-01-01 |  | US-NVS5-004 | high |
| `nv.garn.consumer.employer_fee.per_period` | 3 USD | 2026-01-01 |  | US-NVS5-004 | high |
| `nv.garn.support.treasurer_fee.per_withholding` | 2 USD | 2026-01-01 |  | US-NVS5-005 | high |
| `nv.garn.iwo.remit_days` | 7 days | 2026-01-01 |  | US-NVS5-005 | high |
| `nv.prevailing_wage.exists` | True | 2026-01-01 |  | US-NVR3-002 | high |
| `nv.data.pi.ssn_last4_excluded` | True | 2026-01-01 |  | US-NVS5-017 | high |
| `nv.sui.wage_base` | 43700 USD | 2026-01-01 | 2026-12-31 | US-NV-P5-1-001 (PENDING id pattern) | high |
| `nv.sui.employer.rate.min` | 0.25 % | 2026-01-01 | 2026-12-31 | US-NV-P5-1-001 (PENDING id pattern) | high |
| `nv.sui.employer.rate.max` | 5.4 % | 2026-01-01 | 2026-12-31 | US-NV-P5-1-001 (PENDING id pattern) | high |
| `nv.sui.employee.rate` | 0 % | 2026-01-01 |  | US-NV-P5-1-001 (PENDING id pattern) | high |
| `nv.sdi_pfml.exists` | False | 2023-07-01 |  | US-NV-P5-1-002 (PENDING id pattern) | high |
| `nv.report.ui.registration_threshold.quarterly` | 225 USD | 2026-01-01 |  | US-NV-P5-1-001 (PENDING id pattern) | high |

# Findings by domain (stage 5)

## 1. labour_code
- **Minimum wage: USD 12.00/hour.** It has applied to every employee since 2024-07-01, whether or not health benefits are offered. Ballot Question 2 (2022) removed the two-tier rate.
  - Basis: Const. art. 15 s. 16(1) [US-NVS5-013, A.1]. The 2026 Annual Bulletin, posted 2026-06-29, confirms 12.00 for 2026-07-01 [US-NVS5-002, A.2]. Confidence: high.
  - If the federal minimum exceeds 12.00, the federal rate applies. The Legislature may set a higher rate. The constitution has **no automatic indexation**.
  - No 2027 rate has been enacted.
  - The NRS 608.250 text still shows the two-tier 11.00/12.00. The amended constitution overrides it, so do not model the two tiers.
  - No local (city/county) minimum wage was located.
- **No tip credit:** tips may not be credited against the minimum wage (Const. art. 15 s. 16(4)) [US-NVS5-013].
- **Daily overtime: 1.5x the regular rate** [US-NVS5-001 (NRS 608.018), US-NVS5-003].
  - It applies over 8 hours in a workday (or over 40 in a week) when the employee earns less than 1.5x the minimum wage. From 2026-07-01 that threshold is **USD 18.00/hour** (12.00 x 1.5, re-derived).
  - A 4x10 schedule by mutual agreement is excepted.
  - At or above 18.00, only weekly overtime over 40 hours applies.
  - Exemptions, NRS 608.018(3):
    - agricultural employees;
    - enterprises under USD 250,000 gross sales;
    - executive, administrative and professional employees;
    - CBA overtime;
    - motor carrier, rail and air employees;
    - taxi and limousine drivers;
    - retail commission employees above 1.5x the minimum;
    - auto, truck and farm-equipment sales staff and mechanics;
    - live-in domestic workers who agree in writing.
- **Meal and rest breaks:** a 30-minute meal period for 8 continuous hours, and a paid 10-minute rest per 4 hours or major fraction [US-NVS5-018, A.3]. Rest periods count as hours worked.
- **Pay frequency** (NRS 608.060) [US-NVS5-001, high]:
  - Wages are due at least semimonthly.
  - Wages earned before the 1st are due by 8 a.m. on the 15th of the following month.
  - Wages earned before the 16th are due by 8 a.m. on the last day of the same month.
  - An employer whose principal place of business and payroll are outside NV may pay exempt executive, administrative and professional staff, outside sales staff and supervisors on fixed monthly paydays.
  - Other frequencies by voluntary agreement (608.070).
- **Paydays** (608.080) [US-NVS5-001]:
  - Paydays and the place of payment must be posted in 2 places.
  - A change of payday needs 7 days' written notice.
  - A pay decrease needs 7 days' written notice before the work is done (608.100).
- **Method of payment:** cash or a negotiable check, unless the employee has agreed **in writing** to another disposition (direct deposit or paycard), or a court or agency directs otherwise (NRS 608.120) [US-NVS5-001]. No NV paycard-specific statute was located (open question Q3).
- **Uniforms:** distinctive uniforms are furnished free [US-NVS5-018].
- **Lodging and meals credit, by agreement** (608.154/.155) [US-NVS5-001]:
  - lodging at most 5x the minimum hourly wage per week;
  - meals at most 100% of the minimum hourly wage per day (25% breakfast, 25% lunch, 50% dinner);
  - the limits do not apply to agricultural workers.

## 2. income_tax
- **No state income tax on wages and no withholding.** Const. art. 10 s. 1(9): "No income tax shall be levied upon the wages or personal income of natural persons" [US-NVS5-014, A.1; US-NV-001, A.2]. Confidence: high.
  - So there is no state W-4, no supplemental rate, no rounding rule, no withholding return or deposit schedule, no annual reconciliation and no state W-2 filing.
- **No local income or wage tax.** The constitutional bar covers all levels of government [US-NVS5-014].
- **Reciprocity and resident/nonresident rules:** not applicable.
  - An NV resident working in another state is withheld for that state (MULTI unit).
  - A worker in NV has no state withholding.
- **Oracle:** there is no state withholding calculator (nothing to compute). For MBT, the My Nevada Tax e-services return computes the tax [US-NVS5-010].

## 3. social_security
- **SUI (DETR Employment Security Division)**:
  - **2026 wage base: USD 43,700** [US-NV-P5-1-001].
  - **2027 wage base: USD 45,400** [US-NVS5-019, A.2, `derived arithmetically`]. The DETR R&A memo of 2026-06-01 gives the 2025 average annual wage as 93,841,589,718 / 1,377,412 = 68,128.92. Two-thirds of that is 45,419.28, rounded to the nearest hundred = 45,400. I re-derived this in Python and it matches.
  - **Rule:** NRS 612.545(1), 66 2/3% of the prior-year average annual wage [US-NVS5-006, A.1].
  - **New-employer rate: 2.95%** (NRS 612.540) [US-NVS5-006]. DETR says it lasts 14 to 17 quarters [US-NV-P5-1-001].
  - **Experience rates:** 0.25% to 5.40% (18 rates, reserve ratio) [US-NV-P5-1-001].
  - **Career Enhancement Program: 0.05%** on the same base, separate from the UI rate. It does not apply to 5.4%-rated or reimbursing employers (NRS 612.606) [US-NVS5-006, US-NVP7-003]. My reading of 612.545(1) is that the CEP base equals the UI wage base, which closes the "base unverified" gap in US-NVP7-003.
  - **No employee contribution** [US-NV-P5-1-001].
- **UI wage definition** (NRS 612.190) [US-NVS5-006]:
  - Included: reported tips (26 USC 6053(a)) and non-cash pay at cash value.
  - Excluded: employer payments to retirement, sickness, medical and death plans; 401(a) trust payments; employer-paid employee FICA; non-cash pay to agricultural labour.
- **SDI/TDI/PFML:** none in Nevada [US-LA-P5-2-002 (DOL list), US-NV-P5-1-002].
- **Employer levies** (P7 list, not redone):
  - MBT general business 1.17% of quarterly wages above USD 50,000.
  - MBT financial institutions and mining 1.554% of all wages.
  - Base: gross wages + tips as reported to ESD, less employer-paid health benefits.
  - Rows: US-NVP7-001/-002, re-read 2026-11-02 [US-NVS5-009, US-NVS5-011 (NRS 363B.110/.115)].
  - **The rate is frozen:** NRS 360.203(4) stops the biennial reduction once the rate reaches 1.17%, so no 2027 change is possible without a statute change [US-NVS5-012, high].
  - MBT may not be deducted from employee wages (363B.110(2)(b)).

## 4. payslip_statute
- **Content** [US-NVR3-001, US-NVS5-001]:
  - An itemized list of deductions at each payment (NRS 608.110(2)).
  - **An accounting of available paid-leave hours on every payday** (608.0197(1)(h)), for employers with 50+ NV employees. This is a pay-statement data element, and the payroll system may be used to give it.
- **Records** (608.115) [US-NVS5-001]:
  - Per pay period: gross wage, deductions, net, hours per day and date of payment.
  - Furnished within 10 days of a request.
  - Kept 2 years. Paid-leave records are kept 1 year (608.0197(5)).
- **Language:** English. NV has no language rule (US-NVL-001, US-OWN-006).
- **Electronic delivery:** no statute located → Q4.
- **SSN on the pay statement:** no rule. See section 12.

## 5. reporting_instruments
- **Withholding return, annual reconciliation and state W-2:** none (section 2).
- **Quarterly UI** [US-NVS5-008, A.3; US-NV-P5-1-001]:
  - Forms: Employer's Quarterly Contribution Report (RPT3795) and Wage Report (NEW0098). The Taxation MBT page calls the ESD report "NUCS 4072" (see Q5).
  - Due (received) by Apr 30, Jul 31, Oct 31 and Jan 31.
  - Wages are reported in the quarter paid.
  - Filing in ESS (`ui.nv.gov/ess`) by data entry, by **SFTP upload in EFW2 format**, or by CSV/tab file.
  - Payment by check only under USD 10,000 per quarter; otherwise ACH credit or debit.
  - The handbook is the 2023 edition (age caveat).
- **MBT quarterly return** [US-NVS5-010, US-NVS5-011]:
  - Form TAX-F003 (general business, V2026.1). Financial institutions use TAX-F002 and mining TAX-F004.
  - Due the last day of the month after the quarter, on My Nevada Tax.
  - It must be filed even when no tax is due.
  - **From 2026-01-01 Taxation compares MBT wages with ESD wages every quarter.** A mismatch produces a deficiency determination [US-NVS5-009].
  - So the DD must make MBT line 1 equal the UI gross wages.
- **New hire** [US-NVS5-007, A.1 + A.2]:
  - Report within 20 days of hire, and of rehire after 60+ days of separation (NRS 606.120 → 42 USC 653a), to the DETR ESD New Hire Unit.
  - Required: employee name, address, SSN and start date; employer FEIN, name and address. Optional: DOB and state of hire.
  - Channels: portal, SFTP, fax or mail.
- **Registration:** with ESD once wages reach USD 225 in a quarter [US-NV-P5-1-001]. The MBT account opens automatically with UI registration [US-NVS5-009].
- **Agent access:** ESS external user [US-NVR3-003].

## 6. leave
- **Paid leave, NRS 608.0197** [US-NVS5-001, high]:
  - Applies to private employers with **50+ employees in NV**. Employers are exempt during their first 2 years of operation.
  - Accrual is **0.01923 h per hour worked** (about 40 h/year), or front-loaded.
  - Use starts on day 90, for any reason.
  - The employer may cap use at 40 h per benefit year and carry-over at 40 h.
  - Minimum increment is up to 4 h.
  - Pay is at the current rate on the normal payday. For salaried, commission or piece-rate staff it is the 90-day average (total wages / hours). Discretionary bonuses, OT, hazard pay, holiday pay and tips are excluded.
  - **No payout at separation is required.** Balances are reinstated on rehire within 90 days after an involuntary separation.
  - Temporary, seasonal and on-call employees are excluded.
  - An equivalent PTO policy at 0.01923 or more satisfies the law.
- **Family sick leave** (608.01975, employers with 50+): the employee may use sick leave for immediate family. Read by heading only.
- **Domestic violence / sexual assault leave** (608.0198) [US-NVS5-001]: up to 160 h per 12 months after 90 days of service. It **may be paid or unpaid**.
- **COVID-19 vaccination leave:** 2-4 h paid (SB 209, 2021) [US-NVS5-018]. This is a still-posted summary item; the statute was not read.
- **PFML benefit side:** not applicable (no NV program).

## 7. termination
- **Final pay** [US-NVS5-001, high]:
  - Discharge, or placement on nonworking status (temporary layoff): due immediately (608.020).
  - Resignation: due on the earlier of the regular payday or 7 days (608.030).
  - Penalty wages continue at the same rate until paid, max 30 days (608.040). The 3-day grace applies only to discharged and laid-off employees.
- **Vacation and PTO payout:** paid leave under 608.0197 need not be paid out. No NV statute requiring payout of other vacation was located, and the Labor Commissioner's position was not read → Q2.
- **Separation notice:** no NV statute or DETR requirement for an employee separation notice was located in the sources read (handbook and NRS 612 headings). The employer answers DETR claim requests. Confidence: medium.
- **Mini-WARN:** not researched (budget).

## 8. benefits_in_kind
- **Income-tax conformity:** not applicable, since there is no income tax [US-NVS5-014].
- **The UI wage base follows NRS 612.190** [US-NVS5-006]:
  - Employer contributions to retirement and health plans are excluded.
  - Employee 401(k) elective deferrals are not listed as excluded, so they are treated as UI wages. This matches FUTA.
  - Section 125 is not addressed in 612.190 (Q6).
- **MBT:** the base is the 612.190 wages, less employer-paid health insurance or plan costs (NRS 363B.115). Employee-paid premiums and workers' comp medical costs are excluded from the deduction [US-NVS5-011].
- **Meals and lodging credit limits:** see section 1.

## 9. deductions_garnishments
- **Wage deductions:** only by written order of the employee (or for the listed associations). No rebate of wages is allowed (608.100(2), 608.110(1)) [US-NVS5-001, US-NVS5-018].
- **Creditor garnishment** (NRS 31.295) [US-NVS5-004, A.1, high]:
  - The cap is the lesser of:
    - 18% of disposable earnings if gross weekly pay is USD 770 or less (25% above 770);
    - disposable earnings above 50 x the federal minimum wage.
  - This is stricter than the CCPA for lower earners.
  - Gross weekly pay = YTD gross / weeks worked (31.2955).
  - A writ lasts 180 days.
  - The employer fee is USD 3 per pay period, max USD 12/month, and not for the first period (31.296).
  - Support orders, bankruptcy orders and tax debts are outside the 18/25% cap.
- **Child support IWO** (NRS 31A) [US-NVS5-005, A.1]:
  - Limits: 50/60% (55/65% with arrears over 12 weeks).
  - Withholding starts with the first payment within 14 days of the notice. Remit within 7 days of payment.
  - Deduct the State Treasurer fee of USD 2 per withholding (max 2 a month) and remit the fees at least quarterly.
  - The employer may deduct USD 3 per withholding for its own costs.
  - Child support has priority over all other proceedings, and current support over other support orders (31A.160).
- **State tax levies:** no wage tax. MBT and UI tax are employer-only.

## 10. collective_agreements
- **Prevailing wage on public works** [US-NVR3-002 (reused)]: NRS 338.020 rates go in the contract and must be posted. The DOL threshold table is in that row.
- Hours worked under 338.020(3)/(4) are excluded from the 608.018 overtime rules [US-NVS5-001].
- A CBA may waive the minimum wage, but only explicitly (Const. art. 15 s. 16(5)). A CBA may also set overtime terms (608.018(3)(e)).

## 11. indexation
- **SUI wage base:** set each year as 66 2/3% of the prior-year average annual wage (612.545). DETR R&A computes it by July 1, and the memo is published. 2026 = 43,700; 2027 = 45,400, derived [US-NVS5-019].
- **UI maximum weekly benefit:** indexed every July 1 (657 USD from 2026-07-01). This is benefit-side only.
- **Minimum wage:** not indexed. It is fixed at 12.00 unless the federal rate is higher or the Legislature acts. The Labor Commissioner posts an annual bulletin each June/July [US-NVS5-013, US-NVS5-002].
- **Daily-overtime threshold:** 1.5 x minimum = 18.00, posted in the annual bulletin [US-NVS5-003].
- **MBT rate:** frozen at 1.17% / 1.554% under 360.203(4) [US-NVS5-012].
- **MBT USD 50,000 threshold:** statutory, not indexed.

## 12. data_protection
- **NRS 603A** [US-NVS5-017, A.1]:
  - Personal information = name + SSN, driver licence or ID number, financial account, medical/health-insurance ID, or online credentials. The last 4 digits of an SSN are excluded.
  - Duties: reasonable security, encryption on transfer outside the secure system, breach notice and destruction of records.
- **SSN on pay statements:** no NV rule requiring truncation was located. NRS 608 is silent and 603A does not regulate pay statements.
  - Recommendation for the build: print the last 4 digits only. That is a design choice and not a NV mandate.
- **Retention:** wage records 2 years (608.115(3)); paid-leave records 1 year.

## 13. live_legal_change (2026-01-01 → 2026-11-02, plus 2027)
1. **SUI wage base 2027 = 45,400**, effective 2027-01-01 [US-NVS5-019].
2. **MBT/ESD quarterly wage comparison resumed 2026-01-01** [US-NVS5-009]. Operating level: employer reporting.
3. **2025 36th Special Session** amended NRS 608.016 and 608.018 [US-NVS5-001].
   - 608.016 now has two versions: one through 2029-10-31, and one from 2029-11-01 that drops the donning/doffing clause.
   - The 608.018 exemptions now include live-in domestic service employees by written agreement.
   - Level: labour code / payroll calculation.
4. **NRS 608.250, version effective 2028-01-01** (2023 Statutes p. 2956): it bars sub-minimum wages under 29 USC 214(c) special certificates [US-NVS5-001]. Status: enacted, effective 2028-01-01.
5. **MBT returns reissued 12/2/2025** (V2026.1) [US-NVS5-010]. The rate is unchanged.
6. **2025 regular-session bills seen only in tier-B leads:**
   - AB 388 (state family leave);
   - SB 198 (final pay);
   - AB 179 (paid leave);
   - AB 112.
   - The NRS 608 text as of 2026-10-22 shows no change to 608.030 or 608.0197, so those two were not enacted in that form. The outcome of AB 388 was not verified (Q1).
7. **DV/SA leave bulletin re-issued 2026-04-24**, and an AB 307 posting dated 2026-10-01 appears on the Labor Commissioner postings page [US-NVP9L-001]. Neither PDF was read: the bot check blocked curl, and the archive had no copy of the AB 307 file (Q7).

## MULTI hand-offs (answers for NV)
- **SUI wage-base credit for wages reported to another state: YES.** Wages paid by the same employer for services in another state, on which that state's UI contributions were required, count toward the NV base (NRS 612.545(2)(b)) [US-NVS5-006, A.1].
- **PFML/SDI coverage of multistate workers:** not applicable, as NV has no program.
- **Paid sick leave for employees working partly in NV:** 608.0197 covers employers with "50 or more employees in private employment in this State". The statute has no hours-in-state threshold for the individual employee. Coverage of a partly-in-NV worker is not addressed in the text (Q8; medium).
- **Pay-statement reach to out-of-state work:** no NV extraterritorial rule was located. Default: 608.110 applies to work in NV.
- **UI localization:** NRS 612.080 (localized if all or substantially all work is in NV) [US-NVS5-006].

## Special populations (state rules)
| Population | NV rule | register_id |
|---|---|---|
| Domestic / household | Domestic Workers' Bill of Rights: written agreement, minimum wage, daily OT, rest days, consent-based meal/lodging deductions, no uniform deduction (613.620). Live-in workers may opt out of OT in writing (608.018(3)(o)(p)). UI only if cash wages of USD 1,000+ in a quarter (612.095). Household-only employers are exempt from MBT | US-NVS5-016, US-NVS5-001, US-NVS5-006, US-NVS5-009 |
| Agricultural | Exempt from daily and weekly state OT (608.018(3)(k)). Meal/lodging credit caps do not apply. UI coverage if USD 20,000 cash wages in a quarter or 10+ workers in 20 weeks (612.090). Non-cash agricultural pay is not UI wages | US-NVS5-001, US-NVS5-006 |
| Minors | Under 16: max 8 h/day and 48 h/week (609.240). Minimum wage applies, except under-18s at a nonprofit in after-school or summer jobs (Const.). UI excludes a child under 18 working for a parent and newspaper-delivery minors | US-NVS5-015, US-NVS5-013, US-NVS5-006 |
| Tipped | No tip credit (Const. 15-16(4)). Tips belong to employees, and pooling among employees is allowed. Reported tips are UI wages and MBT wages | US-NVS5-013, US-NVS5-018, US-NVS5-006, US-NVS5-009 |
| Clergy / religious | UI covers nonprofit and religious employers only under 612.121 conditions (FUTA 3306(c)(8) exclusion plus 4+ workers in 20 weeks). The 612.120 religious-service exclusion was read by heading only. MBT exempts 501(c) nonprofits. No wage tax | US-NVS5-006, US-NVS5-009 (partial) |
| Students | UI excludes work-experience and school financial-assistance programs (612.118/.119). Trainees for up to 90 days are outside the constitutional minimum-wage definition | US-NVS5-006, US-NVS5-013 |
| Nonresident aliens | No state rule beyond federal (no wage tax; UI by localization) | US-NVS5-014, US-NVS5-006 |
| Statutory employees | UI uses the ABC test (612.085). Agent/commission drivers are included (612.142). Licensed real-estate salespersons (612.133) and direct sellers (612.144) are excluded | US-NVS5-006, US-NV-P5-1-001 |
| Government | Out of private scope. MBT exempts political subdivisions. UI includes State employment (612.115). NRS 608 governs "private employment" | US-NVS5-009, US-NVS5-006, US-NVS5-001 |

## ACCESS gaps (exact URLs, 2026-11-02, BR IP, VPN off)
- `https://www.leg.state.nv.us/NRS/NRS-608.html`: HTTP 403. Same for every leg.state.nv.us page. All read via web.archive.org.
- `https://detr.nv.gov/Page/UI_Information_for_Employers` and `https://detr.nv.gov/Page/New_Hire_Reporting_Info`: HTTP 403 (archive copies used).
- `https://ui.nv.gov/`: HTTP 403.
- `https://cms.detr.nv.gov/Content/Media/Unemployment_Insurance_Tax.pdf`: HTTP 403, with no archive copy.
- `https://nevadaworkforce.com/_docs/EDS_Wage-Benefit/MWB-Statewide-2026.pdf`: HTTP 000 (archive copy used).
- `https://labor.nv.gov/uploadedFiles/labornvgov/content/Employer/*.pdf`: bot-check (captcha) page.
- `https://labor.nv.gov/uploadedFiles/labornvgov/content/Employer/AB%20307%20Q1%20Required%20Posting%2010.01.2026%20(EN).pdf`: bot check, and the archive has no copy (404). **For the browser pass.**
- `https://labor.nv.gov/uploadedFiles/labornvgov/content/Employer/Domestic%20Violence%20and%20Sexual%20Assault%20Victim's%20Leave%20Bulletin%2004.24.2026.pdf`: not fetched (budget). **For the browser pass.**

## Confidence
- High: domains 1, 2, 3, 7 (final pay) and 9.
- Medium-high: domains 4, 5 (form identity open), 6, 11 and 12.
- Medium: domains 8 and 13 (2025 bills unverified).
- Not researched: mini-WARN.

## Open questions

Mirrors `unresolved[]` of the facts file (same keys, same wording).

- **nv.meta.register_id_pattern** (blocking): 6 facts rest on active register rows whose ids (US-NV-P5-1-001, US-NV-P5-1-002) do not match the facts-schema register_id pattern ^[A-Z]{2}-[A-Z0-9]{2,12}-[0-9]{3,4}$ (multi-hyphen legacy ids). They are carried in full in _facts_pending_register_id_pattern and are NOT yet consumable facts. What would close it: Orchestrator decision: a PATCH of facts.schema.json loosening the register_id pattern (e.g. ^[A-Z]{2}-[A-Z0-9-]{2,16}-[0-9]{3,4}$), or register alias ids; then run _research/synthesis-B/_work-MN-WY/promote.py to move the pending facts into facts[].
- **nv.leave.family_leave_ab388** (non-blocking): AB 388 (2025) state family leave enactment not verified. What would close it: NELIS bill history for AB 388 (83rd session) or Labor Commissioner 2025 legislative summary.
- **nv.term.vacation.payout** (non-blocking): No statute on vacation/PTO payout outside 608.0197. What would close it: Labor Commissioner FAQ or NAC 608 provision.
- **nv.labour.paycard** (non-blocking): Paycard rules beyond 608.120 written consent not read. What would close it: NAC 608 section on payroll cards.
- **nv.payslip.electronic** (non-blocking): Electronic pay-statement delivery not addressed. What would close it: Labor Commissioner FAQ or NAC 608.
- **nv.report.ui.form_identity** (non-blocking): RPT3795/NEW0098 (2023 handbook) vs Taxation's NUCS 4072. What would close it: Current ESS forms list (browser pass).
- **nv.ui_mbt.section125** (non-blocking): Section 125 salary reductions in UI and MBT wages not addressed in 612.190. What would close it: NAC 612 or DETR wage guide plus the Taxation MBT FAQ.
- **nv.live.ab307_dvsa** (non-blocking): AB 307 posting (2026-10-01) and the 2026-04-24 DV/SA bulletin not read (bot check). What would close it: Browser read of the two labor.nv.gov PDFs.
- **nv.leave.paid.partial_state** (non-blocking): 608.0197 coverage of employees working partly in NV not addressed. What would close it: Labor Commissioner FAQ or NAC 608.
