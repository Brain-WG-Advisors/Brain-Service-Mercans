# CCG research pack - annex_MT (Montana)

Synthesis-B worker MN-WY, 2026-11-02. Unit `annex_MT` of the CCG (jurisdiction annex, all 13 domains + special populations).
Facts file: `_research/CCG-annex_MT-facts.json` (42 facts, 18 pending on the register_id pattern defect, 8 unresolved). Every claim below carries its register_id inline; numbers may be cited in the CCG only through a fact key.

## 0. How to use this pack

- Body sections 1-13 and Special populations are the stage-5 findings (`_research/stage5/MT.md`), carried verbatim because they are already organised by the 13 CCG domains with register ids inline.
- Federal layer (FIT, FICA, FUTA, W-2/941/940), the multistate rules (reciprocity, sourcing) and the language seams (US-OWN-006: payslip in English; second-language duties attach to notices and posters only) live in annex_FED / annex_MULTI and are not repeated here.
- Special populations (US-OWN-005): the state-level rules are in the Special populations table below; the country-wide coverage matrix is CCG unit `coverage`.
- Values are 2026 unless the fact says otherwise. 2027 values appear only where the row carries an enacted or published 2027 figure; projections are never facts.

## 0.1 Synthesis decisions and traps (bind the builder)

- UI base INCLUDES Section 125, 401(k) deferrals and 129 (and room/board, vehicle) - unlike the income-tax base [US-MTS5-023/-025].
- Accrued vacation must be paid at separation (Langager) - flag in DD/termination.
- 2027 minimum wage 11.20 is DERIVED ONLY (US-MTS5-017 partial) - not a fact; WTC must not use it until the DLI letter is read.
- Withholding rounds UP to the next dollar (not nearest).

## 0.2 Register status check of the ids cited in the findings

These ids appear in the findings but are not plain `active`; do not cite them for a number:

- US-MTS5-017: partial

## 0.3 Facts emitted

| key | value | from | to | register_id | conf |
|---|---|---|---|---|---|
| `mt.minwage.hourly` | 10.85 USD | 2026-01-01 | 2026-12-31 | US-MTS5-014 | high |
| `mt.labour.minwage.small_business.hourly` | 4.0 USD | 2026-01-01 |  | US-MTS5-004 | high |
| `mt.minwage.indexation` | CPI-U US city average Aug/Aug; set by 30 Sep; effective 1 Jan; nearest 0.05 | 2026-01-01 |  | US-MTS5-004 | high |
| `mt.minwage.tip_credit.allowed` | False | 2026-01-01 | 2026-12-31 | US-MTS5-014 | high |
| `mt.overtime.weekly_threshold_hours` | 40 hours | 2026-01-01 |  | US-MTS5-003 | high |
| `mt.overtime.premium.multiplier` | 1.5 ratio | 2026-01-01 |  | US-MTS5-003 | high |
| `mt.labour.overtime.computer_employee_threshold.hourly` | 27.63 USD | 2026-01-01 |  | US-MTS5-006 | high |
| `mt.labour.pay_timing.max_business_days_after_due` | 10 days | 2009-10-01 |  | US-MTS5-001 | high |
| `mt.labour.direct_deposit.consent_required` | True | 2009-10-01 |  | US-MTS5-001 | high |
| `mt.labour.late_wage_penalty.max` | 110 % | 2026-01-01 |  | US-MTS5-019 | high |
| `mt.pit.bracket.1.ceiling.single` | 47500 USD | 2026-01-01 | 2026-12-31 | US-MTS5-022 | high |
| `mt.pit.bracket.1.ceiling.hoh` | 71250 USD | 2026-01-01 | 2026-12-31 | US-MTS5-022 | high |
| `mt.pit.bracket.1.ceiling.joint` | 95000 USD | 2026-01-01 | 2026-12-31 | US-MTS5-022 | high |
| `mt.pit.bracket.1.rate` | 4.7 % | 2026-01-01 |  | US-MTS5-022 | high |
| `mt.pit.bracket.2.rate` | 5.65 % | 2026-01-01 | 2026-12-31 | US-MTS5-022 | high |
| `mt.pit.bracket.2.rate` | 5.4 % | 2027-01-01 |  | US-MTS5-022 | high |
| `mt.pit.bracket.1.ceiling.single` | 65000 USD | 2027-01-01 |  | US-MTS5-022 | high |
| `mt.pit.bracket.1.ceiling.hoh` | 97500 USD | 2027-01-01 |  | US-MTS5-022 | high |
| `mt.pit.bracket.1.ceiling.joint` | 130000 USD | 2027-01-01 |  | US-MTS5-022 | high |
| `mt.pit.agricultural.withholding_required` | False | 2026-01-01 |  | US-MTS5-005 | high |
| `mt.pit.nra.treaty_at_withholding` | False | 2026-01-01 |  | US-MTS5-005 | high |
| `mt.sui.wage_base` | 45100 USD | 2025-01-01 | 2025-12-31 | US-MTS5-024 | high |
| `mt.ui.admin_fund_tax.rate` | 0.18 % | 2026-01-01 | 2026-12-31 | US-MTP7-001 | high |
| `mt.ui.admin_fund_tax.rate_class_1_2` | 0.13 % | 2026-01-01 | 2026-12-31 | US-MTP7-001 | high |
| `mt.sui.employee.rate` | 0 % | 2026-01-01 |  | US-MTS5-023 | high |
| `mt.sui.wages.section125_included` | True | 2026-01-01 |  | US-MTS5-023 | high |
| `mt.sui.wages.401k_included` | True | 2026-01-01 |  | US-MTS5-023 | high |
| `mt.sui.wage_base.other_state_credit` | False | 2025-07-01 |  | US-MTS5-025 | high |
| `mt.records.payroll_tax.retention_years` | 5 years | 2026-01-01 |  | US-MTS5-005 | high |
| `mt.report.wh.accelerated_threshold` | 12000 USD | 2026-01-01 |  | US-MTS5-005 | high |
| `mt.report.wh.monthly_threshold` | 1200 USD | 2026-01-01 |  | US-MTS5-005 | high |
| `mt.report.mw3.due` | 31 January (MW-3 + all W-2s) | 2026-01-01 |  | US-MTS5-005 | high |
| `mt.report.ui.quarterly_due` | Apr 30; Jul 31; Oct 31; Jan 31 | 2025-07-01 |  | US-MTS5-025 | high |
| `mt.newhire.report_days` | 20 days | 2026-01-01 |  | US-MTS5-012 | high |
| `mt.leave.vacation.payout_at_separation` | True | 2026-01-01 |  | US-MTS5-018 | medium |
| `mt.term.final_pay.quit` | next regular payday or 15 days, whichever first | 2026-01-01 |  | US-MTS5-002 | high |
| `mt.final_pay.discharge` | immediately (policy may extend to next payday or 15 days) | 2026-01-01 |  | US-MTS5-002 | high |
| `mt.garn.creditor.max_percent` | 25 % | 2026-01-01 |  | US-MTS5-009 | high |
| `mt.garn.iwo.employer_fee.monthly` | 5 USD | 2026-01-01 |  | US-MTS5-013 | high |
| `mt.prevailing_wage.threshold` | 25000 USD | 2026-01-01 |  | US-MTS5-010 | high |
| `mt.prevailing_wage.pay_frequency` | weekly | 2026-01-01 |  | US-MTS5-011 | high |
| `mt.data.w2.truncated_ssn_rejected` | True | 2026-01-01 |  | US-MTS5-005 | high |
| `mt.wh.method` | annual formula W = A + B(G - C); federal standard deduction; no MT allowances; round UP to next dollar | 2026-01-01 | 2026-12-31 | US-MT-P5-1-001 (PENDING id pattern) | high |
| `mt.pit.wh.single.1.ceiling` | 16100 USD | 2026-01-01 | 2026-12-31 | US-MT-P5-1-001 (PENDING id pattern) | high |
| `mt.pit.wh.single.2.rate` | 4.7 % | 2026-01-01 | 2026-12-31 | US-MT-P5-1-001 (PENDING id pattern) | high |
| `mt.pit.wh.single.2.ceiling` | 63600 USD | 2026-01-01 | 2026-12-31 | US-MT-P5-1-001 (PENDING id pattern) | high |
| `mt.pit.wh.single.3.rate` | 5.65 % | 2026-01-01 | 2026-12-31 | US-MT-P5-1-001 (PENDING id pattern) | high |
| `mt.pit.wh.single.3.base_tax` | 2233 USD | 2026-01-01 | 2026-12-31 | US-MT-P5-1-001 (PENDING id pattern) | high |
| `mt.wh.supplemental.rate` | 5 % | 2026-01-01 |  | US-MT-P5-1-001 (PENDING id pattern) | high |
| `mt.pit.nonresident.days_exemption` | 30 days | 2026-01-01 |  | US-MT-P5-1-003 (PENDING id pattern) | high |
| `mt.reciprocity.states` | ND | 2026-01-01 |  | US-MT-P5-1-004 (PENDING id pattern) | high |
| `mt.local_wage_tax.exists` | False | 2026-01-01 |  | US-MT-P5-2-001 (PENDING id pattern) | high |
| `mt.sui.wage_base` | 47300 USD | 2026-01-01 | 2026-12-31 | US-MT-P5-1-005 (PENDING id pattern) | high |
| `mt.sui.employer.rate.min` | 0.0 % | 2026-01-01 | 2026-12-31 | US-MT-P5-1-005 (PENDING id pattern) | high |
| `mt.sui.employer.rate.max` | 6.12 % | 2026-01-01 | 2026-12-31 | US-MT-P5-1-005 (PENDING id pattern) | high |
| `mt.ui.rate.new_employer.min` | 1.0 % | 2026-01-01 | 2026-12-31 | US-MT-P5-1-005 (PENDING id pattern) | high |
| `mt.ui.rate.new_employer.construction` | 2.0 % | 2026-01-01 | 2026-12-31 | US-MT-P5-1-005 (PENDING id pattern) | high |
| `mt.sdi_pfml.exists` | False | 2026-01-01 |  | US-MT-P5-2-002 (PENDING id pattern) | high |
| `mt.payslip.items` | itemized statement of state and federal income tax, social security and other deductions each payment | 2026-01-01 |  | US-MT-P5-1-006 (PENDING id pattern) | high |
| `mt.leave.sick.state_statute.exists` | False | 2026-01-01 |  | US-MT-P5-2-002 (PENDING id pattern) | medium |

# Findings by domain (stage 5)

## 1 — labour_code
- **State minimum wage: 10.85 USD/h from 2026-01-01 to 2026-12-31** [US-MTS5-014, A.2, high].
  - **G-DERIVE:** 10.55 × (1 + 2.92%) = 10.55 + 0.31 = 10.86, rounded to the nearest 0.05 = **10.85**. This reproduces the published figure.
  - Inputs: CPI-U Aug 2025 323.976 / Aug 2024 314.796 = +2.92% [US-MTS5-016]. The method is the department's own, as shown in the 2025 letter (2.53% → 10.56 → 10.55) [US-MTS5-015].
  - The calculation was done in Python Decimal.
- **Mechanism** [MCA 39-3-409, US-MTS5-004, A.1]:
  - The rate is the greater of the FLSA rate or 6.15, indexed each year.
  - Index: CPI-U U.S. city average, all items, August to August. The department must adjust by 30 September; the new rate takes effect 1 January.
  - Rounded to the nearest 5 cents.
  - **No tip credit, no training wage, no meal credit** [US-MTS5-014].
  - A business with annual gross sales of 110,000 or less that is not covered by the FLSA may pay 4.00/h. An individual employee who is FLSA-covered gets the higher rate [US-MTS5-004, US-MTS5-014].
- **2027: 11.20/h, DERIVED and not read from a publication** [US-MTS5-017, status partial].
  - 10.85 × 3.40% = 0.37; 11.22, rounded → 11.20. Input: Aug 2026 CPI-U 334.980 [US-MTS5-016].
  - The DLI 2027 Determination Letter exists in the Wayback index, but the 2026-10-07 capture is a 404. Confirm against that letter before the WTC uses the figure.
- **Local minimum wages:** none possible in practice. Local governments need delegated powers for this kind of regulation (MCA 7-1-112 limits taxation, see §2). I found no local minimum-wage ordinance and did not search for a specific preemption statute. Confidence medium.
- **Overtime** [MCA 39-3-405, US-MTS5-003, A.1]:
  - 1.5× the hourly rate over 40 hours in a workweek. No daily overtime.
  - Not for farm workers.
  - Seasonal amusement or recreation students given board or lodging: overtime starts over 48 hours.
- **Exemptions** [MCA 39-3-406, US-MTS5-006]:
  - Usual EAP and outside-sales exemptions.
  - Computer employees paid at least 27.63/h.
  - Hospitals: 8/80 work period (overtime over 8 hours a day or 80 hours in 14 days).
  - Public-sector work periods.
  - Retail commission employees.
  - Licensed-outfitter guides.
  - Taxi drivers.
  - Motor carriers (49 USC 31502).
- **Pay timing** [MCA 39-3-204, US-MTS5-001]:
  - Wages may not be withheld more than **10 business days after they are due**.
  - If no pay period is established, it is presumed **semimonthly**.
  - A late timesheet may be paid in the next pay period.
- **Method of payment:**
  - Cash, or checks convertible at face value.
  - **Direct deposit/EFT only with the employee's written or electronic consent, with a record retained. Direct deposit cannot be required** [US-MTS5-001].
  - Paycards: no Montana rule located (rules.mt.gov unreachable). See Open questions.
- **Wages definition** [MCA 39-3-201(6), US-MTS5-019]:
  - Includes bonus, piecework, tips, and service charges at food/beverage/lodging premises.
  - Service charges must be distributed to non-management serving staff.
- **Penalty** for late wages: up to 110% of the unpaid wages [MCA 39-3-206, US-MTS5-019]. The DLI applies 55% under ARM 24.16.7566 (rule not read) [US-MTS5-018].

## 2 — income_tax
- **Method from 2026-01-01** [US-MT-P5-1-001, US-MT-P5-1-002, A.2, high; reused]:
  - Annual formula W = A + B(G − C).
  - Single/MFS: 0% up to 16,100; 4.7% up to 63,600; above that, 2,233 + 5.65%.
  - The federal standard deduction is used. There are no Montana allowances.
  - Certificate: **Form MW-4**.
  - Withholding is rounded **UP to the next dollar**.
- **Reconciliation with statute** [MCA 15-30-2103 temporary version, US-MTS5-022, A.1]:
  - 2026 brackets: 4.7% up to 47,500 single/MFS, 71,250 HoH, 95,000 joint; 5.65% above.
  - 16,100 (federal standard deduction, single) + 47,500 = **63,600**, the threshold in the guide table.
  - 4.7% × 47,500 = 2,232.5, which matches the guide's 2,233 constant after rounding up to the dollar.
- **2027 (enacted)** [15-30-2103 version effective 2027-01-01, US-MTS5-022]:
  - 4.7% up to 65,000 single/MFS, 97,500 HoH, 130,000 joint; **5.4%** above.
  - Indexation begins with June 2026 CPI as the base. The 2027 factor is therefore 1.0, and the first indexed brackets are for TY2028.
  - DOR's 2027 withholding tables and the 2027 guide were not obtained. The 2026-01 Wayback news index shows no 2027 item yet.
- **Supplemental wages paid separately:** aggregate with current or preceding period wages, or **flat 5%** [US-MT-P5-1-001; guide p.3 re-read 2026-11-02].
- **Residents and nonresidents:**
  - Montana-source wages of nonresidents are subject to withholding.
  - **30-day exemption:** a nonresident who works fewer than 30 days in Montana and also works in more than one state needs no withholding. It does not apply to athletes, entertainers, per-event workers, construction workers, key employees (over 500,000) or MEDIA-credit employees [US-MT-P5-1-003].
  - **Nonresident aliens:** treaty exclusions are NOT applied at withholding; they are decided on the individual return (level = assessment). H-2A workers are exempt from withholding [US-MTS5-005].
- **Reciprocity:** with North Dakota only. The ND resident files MW-4 line 5, the employer submits it via TAP, and it is renewed each year by 31 January [US-MT-P5-1-004, US-MTS5-005].
- **Exempt from withholding without MW-4:** agricultural laborers (cannabis workers do not count as agricultural); nonresident interstate motor/rail carrier employees; active-duty armed forces [US-MTS5-005].
- **Exempt with MW-4:** tribal members living and working on their own reservation; MT National Guard on Title 10 orders; military spouses [US-MTS5-005].
- **Local income taxes:** none. Local governments cannot levy a tax on income without delegation (MCA 7-1-112) [US-MT-P5-2-001, reused].

## 3 — social_security (UI; no SDI/PFML)
- **SUI 2026** [US-MT-P5-1-005, A.2, reused]:
  - Wage base **47,300**.
  - Schedule 1: rates 0.00% to 6.12%, average 0.95%.
  - New employers by industry: 1.00–2.00% (construction 2.00, services 1.10, agriculture/mining 1.30).
  - **Administrative Fund Tax (AFT):** 0.18%, or 0.13% for eligible classes 1–2 [US-MTP7-001].
  - Penalty rate: 50% higher.
- **Wage base mechanism** [MCA 39-51-1108, US-MTS5-007, A.1]: the greater of 80% of the average annual wage (rounded to 100) or the FUTA base.
  - **G-DERIVE:** 0.8 × 59,106.64 = 47,285.31 → 47,300 (2026). 0.8 × 56,393.42 = 45,114.74 → 45,100 (2025) [US-MTS5-024].
- **No employee UI contribution.** Employers may not deduct UI from wages [MCA 39-51-3103, US-MT-P5-2-003; 39-51-1103(2), US-MTS5-023].
- **Contribution rounding:** half a cent or more rounds up to 1 cent [39-51-1103(3)].
- **UI wage definition departs from the income-tax base** [39-51-201(25), US-MTS5-023; Handbook, US-MTS5-025]:
  - **Taxable for UI:** Section 125 cafeteria salary reductions, 401(k) elective deferrals, Section 129 dependent care, corporate officer pay, personal use of a company vehicle, and room and board (minimum 130/week, 3/meal).
  - **Exempt:** employer contributions to qualified plans and employer health/life premiums.
- **SDI/TDI/PFML:** none. No family-leave or TDI chapter in Title 39 [US-MT-P5-2-002, reused].
- **Other employer levies:** the AFT only [US-MTP7-001, US-MTP9V-001].
- **MULTI hand-off, SUI credit for wages reported to another state: NO.** "Montana does not allow wages paid in other states to be used to determine excess wages" [US-MTS5-025, A.3]. The four-part localization test applies [US-MTS5-025].

## 4 — payslip_statute
- **Content** [MCA 39-3-101, US-MT-P5-1-006, A.1; text re-read 2026-11-02]:
  - Every payment comes with an itemized statement of state and federal income tax, social security and any other deductions, with each amount.
  - If nothing was deducted, a statement saying so.
  - It covers "all employers in this state".
- No Montana provision on **electronic delivery** or consent for pay statements was located.
- No **gross/hours/rate** content requirement exists beyond deductions. This is a narrow statute.
- **Retention:**
  - Payroll tax records: 5 years (ARM 42.17.203, through the DOR guide) [US-MTS5-005].
  - Wage-and-hour records rule: not read (rules.mt.gov unreachable).
- **Multistate reach:** "all employers in this state" when paying employees. No out-of-state reach rule located.
- **Language:** English [US-MTL-001, US-MTP9L-001/-002].

## 5 — reporting_instruments
- **Withholding** [US-MTS5-005, A.2]:
  - Registration via TAP; the withholding account needs the date employees started working in Montana.
  - Deposits follow the lookback period (1 July – 30 June):
    - 12,000 or more: accelerated, on the federal schedule;
    - 1,200 – 11,999: monthly, by the 15th;
    - 1,199 or less: annual, by 31 January.
  - Paper payment voucher: MW-1.
  - **MW-3 annual reconciliation + all W-2s due 31 January.** Federal W-3 is not accepted. Truncated SSNs are not accepted.
  - Electronic channel: TAP single entry, or TAP File Processing Account upload in **EFW2** (W-2) or Pub 1220 (1099). PDFs are not accepted.
  - Final MW-3/W-2 within 30 days of ceasing to pay wages.
  - Penalties:
    - late payment: 1.5%/month, up to 15%;
    - late W-2: 50 per form, minimum 250;
    - interest: 10.25% a year.
  - Representation: Montana Form POA or federal 2848, and third-party access in TAP.
  - MW-4 exemption claims go to DOR via TAP by the last day of the payroll period in which they are received.
- **Quarterly UI wage report** [US-MTS5-025, A.3]:
  - Due Apr 30 / Jul 31 / Oct 31 / Jan 31.
  - **Electronic filing is mandatory from 2025-07-01** (ARM 24.40.1609), through UI eServices for Employers.
  - Late report: 25. Interest: 1.5%/month.
  - Format specs are in the "Montana UI Contributions E-Filing Handbook", which was **not obtained**.
- **New hire** [MCA 40-5-922, US-MTS5-012, A.1]:
  - Reported to DPHHS within **20 days** of hire or rehire.
  - Fields: employee name, hire date, SSN, residential and mailing addresses; employer name, address, FEIN. Optional: DOB and availability of dependent health coverage.
  - Electronic: two transmissions a month, 12–16 days apart.
  - Multistate election allowed.
  - Portal named in the UID handbook: dphhs.mt.gov/cssd/employerinfo/newhirereporting.

## 6 — leave
- **Paid sick leave:** no private-sector statute. The Title 39 index has no sick-leave or PFML chapter [US-MT-P5-2-002]. Public-employee sick leave (MCA 2-18-618) was not read. Confidence medium-high.
- **Vacation:** no statute requires it. **Once accrued, it is wages and cannot be forfeited.** A use-it-or-lose-it condition subsequent cannot divest accrued vacation, so accrued vacation is paid at separation [Langager v. Crazy Creek Prods., 1998 MT 44, 287 Mont. 445; applied in DLI Herden, Case 1184-2020; US-MTS5-018, A.3].
  - Status: in force, settled case law.
  - Level: final pay and wage claim.
  - Primary-court text not read (court site unreachable).
- **Maternity:** reasonable leave of absence for pregnancy, unpaid; accrued disability/leave benefits must be honoured; covers all employers [MCA 49-2-310, US-MTS5-008, A.1].
- **PFML benefit-side interaction:** none (no state programme).

## 7 — termination
- **Final pay** [MCA 39-3-205, US-MTS5-002, A.1]:
  - **Quit:** next regular payday for the period, or 15 days, whichever comes first.
  - **Discharge for cause or layoff:** immediately. A written personnel policy may extend this to the next payday or 15 days, whichever comes first.
  - The DLI poster reads "immediately" as within four hours or the end of the business day, whichever is first (ARM 24.16.7511, not read) [US-MTS5-014].
  - Theft allegation: the employer may withhold the value with written consent, or after a police report within 7 business days.
- **Accrued vacation payout:** see §6 [US-MTS5-018].
- **Separation notice:** no mandatory UI separation notice to the employee was found. The handbook only requires timely answers to the UID's separation-information requests [US-MTS5-025]. Confidence medium; ARM 24.11 was not read.
- The Wrongful Discharge from Employment Act is not payroll-relevant and was not researched.

## 8 — benefits_in_kind
- **Income-tax withholding follows federal:** "if a class of employment or service is subject to wage withholding for federal purposes, it is also subject to Montana wage withholding" [US-MTS5-005].
  - Retirement deferrals are exempt to the extent they are excluded from federal AGI [guide p.3, US-MTS5-005].
  - From 2024, Montana taxable income starts from the federal parameters (the formula uses the federal standard deduction) [US-MT-P5-1-002].
  - No Montana departure was found for 401(k), 125, HSA, transit or group-term life on the income-tax side. Confidence medium: the 15-30-2110 adjustments section was not read.
- **UI departs** (§3): 125, 401(k) deferrals and 129 are taxable for UI; employer health/life premiums are not [US-MTS5-025].

## 9 — deductions_garnishments
- **Deductions:** reasonable deductions for board, room and incidentals when they are a condition of employment, "or as otherwise provided for by law" [39-3-204(1), US-MTS5-001]. No Montana written-authorization statute for other deductions was read. See Open questions.
- **Creditor garnishment:** the lesser of 25% of disposable earnings or disposable earnings above 30× the federal minimum wage. This mirrors the CCPA [MCA 25-13-614, US-MTS5-009].
  - Support orders: 50/60%, or 55/65% for arrears older than 12 weeks.
- **Child-support income withholding (IWO)** [MCA 40-5-415/-416, US-MTS5-013]:
  - The employer must remit **in the same month** the amount is withheld.
  - Arrears add the greater of a 2-year payoff or 25%.
  - **Employer fee up to 5 USD a month** if the department allows it.
  - The total, including the fee, is capped by CCPA 1673(b).
- **State tax levy** (MCA 15-1-704 family): not read.

## 10 — collective_agreements / prevailing wage
- **State prevailing-wage law applies to public works contracts over 25,000** [MCA 18-2-401(11), US-MTS5-010, A.1]. This confirms US-MT-P5-1-007 from the primary text.
  - It covers construction services and also **nonconstruction services**: maintenance, custodial, security, food service, transport driving and similar.
- **Payroll obligations** [MCA 18-2-423, US-MTS5-011]:
  - Contractors and subcontractors must pay hourly employees **weekly**.
  - Certified payroll records on request after a complaint, within 5 days.

## 11 — indexation
| Item | Mechanism | Publication | register_id |
|---|---|---|---|
| Minimum wage | CPI-U Aug/Aug, by 30 Sep, effective 1 Jan, nearest 0.05 | DLI determination letter + poster | US-MTS5-004, -014..-017 |
| UI wage base | 80% of average annual wage (year t-2), rounded to 100 | UID Rate Explanation | US-MTS5-007, -024, US-MT-P5-1-005 |
| PIT brackets | Modified inflation factor (June 2026 base), by 1 Nov, from TY2028 | DOR | US-MTS5-022 |
| Withholding tables | ARM 42.17.105, each year | DOR Employer Guide | US-MT-P5-1-001 |
| UI rate schedule | Fund ratio at 31 Oct | UID Rate Explanation | US-MT-P5-1-005 |
| Computer-employee threshold 27.63/h | Fixed in statute (not indexed) | MCA 39-3-406 | US-MTS5-006 |

## 12 — data_protection
- **No Montana rule requiring SSN truncation on pay statements was located.**
- DOR **rejects** truncated SSNs on W-2s filed with the MW-3 [US-MTS5-005].
- Montana's identity-theft law requires destruction of records that are no longer needed, and breach notice to residents and to the AG (data elements include SSN and TIN) [MCA 30-14-1703/-1704, US-MTS5-020].
- Payroll tax records: 5 years [US-MTS5-005].

## 13 — live_legal_change
- **HB 337 (Ch. 227, L. 2025)**: in force.
  - TY2026 top rate 5.65% (from 5.9%), brackets as in §2.
  - TY2027: 5.4%, with the higher brackets 65,000 / 97,500 / 130,000.
  - Montana EITC raised to 20% of the federal credit [US-MTS5-022, US-MT-P5-1-001/-002].
  - Level: withholding (tables) and assessment.
- **SB 53 (2025)**: mineral royalty withholding at 5.65% in 2026 and 5.4% in 2027 [US-MT-P5-1-001]. Not payroll wages.
- **Minimum wage 2027:** 11.20, derived [US-MTS5-017]. Status: DLI letter due by 2026-09-30, **not read**.
- **UI electronic filing mandate** effective 2025-07-01 (ARM 24.40.1609) [US-MTS5-025].
- **Bulletin sweep:** done through the Wayback index of revenue.mt.gov/news/recent-news (2026 captures). Items: 2026-withholding-updates (already US-MT-P5-1-002), mw-3-deadline, withholding-look-back, volunteer-firefighter subtraction. No 2027 withholding notice is indexed yet.
- The Montana Legislature meets in odd years, so no 2026 regular-session acts are expected; this was not source-checked.

## Special populations (state level)
| Population | Montana rule | register_id |
|---|---|---|
| Domestic/household | Minimum wage/OT excluded for babysitting and menial chores, child care hired by the head of household, and companionship hired by family (39-3-406). UI covered only if 1,000+ cash wages in a quarter; excluded if employed by family or guardian | US-MTS5-006, US-MTS5-021, US-MTS5-025 |
| Agricultural | No state overtime (39-3-405(2)). Learners under 18 may be paid 50% of minimum for 180 days. **No state income-tax withholding on agricultural laborers** (cannabis workers excepted). UI covered if 20,000 in a quarter or 10 workers on 20 days | US-MTS5-003, -006, -005, -025 |
| Minors | No youth sub-minimum beyond farm learners and apprentices/learners (30 days, commissioner). Child-labour hours not researched | US-MTS5-006 |
| Tipped | **No tip credit**; full 10.85 cash wage. Tips are wages (39-3-201). UI taxes reported tips | US-MTS5-014, -019, -025 |
| Clergy/religious | Withholding follows federal (minister exempt from federal withholding, no state rule beyond that). UI excludes ministers and religious-order members | US-MTS5-005, -021, -025 |
| Students | Distributive-education students excluded from minimum wage/OT. Seasonal amusement students: OT over 48 hours. UI excludes students working for their own school (12/9 credits) and co-op students | US-MTS5-006, -003, -021, -025 |
| Nonresident aliens | Withheld like other employees. Treaty exclusion applied at assessment only. H-2A exempt from withholding. UI excludes F/H-2A/J/M/Q | US-MTS5-005, -021 |
| Statutory employees / officers | Direct sellers excluded (min wage and UI). Corporate officers are UI employees (including S corp) | US-MTS5-006, -021, -025 |
| Government | US federal employees excluded from Montana minimum wage/OT. State/local work-period overtime rules. UI: reimbursable option for government and tribes | US-MTS5-006, -023 |
| Tribal members | Withholding exempt on own-reservation wages while living there (MW-4 line 5) | US-MTS5-005 |
| Military / Guard / spouses | Active duty exempt. MT National Guard on Title 10 and military spouses exempt with MW-4 by 31 January | US-MTS5-005 |
| Small non-FLSA business | 4.00/h minimum if gross sales are 110,000 or less | US-MTS5-004, -014 |

## MULTI hand-offs (answered for MT)
1. SUI wage-base credit for wages reported to another state: **No** [US-MTS5-025].
2. PFML/SDI coverage of multistate workers: n/a, no programme [US-MT-P5-2-002].
3. Paid sick leave for employees working partly in the state: n/a, no statute.
4. Pay-statement reach: 39-3-101 binds "all employers in this state". No reach rule for out-of-state work [US-MT-P5-1-006].

## ACCESS gaps (exact URLs)
- Local DNS failure from the BR network for all of these (not retried with a DNS override; the classifier refused that route):
  - https://revenue.mt.gov/
  - https://revenuefiles.mt.gov/files/Forms/Montana_Employer_and_Information_Agent_Guide_with_Tax_Tables.pdf
  - https://erd.dli.mt.gov/
  - https://uid.dli.mt.gov/
  - https://dli.mt.gov/
  - https://rules.mt.gov/
  - https://dphhs.mt.gov/csed
- https://erd.dli.mt.gov/_docs/labor-standards/2027-MW-Determination-Letter.pdf: the Wayback capture 20261007064405 returned 404, and no other capture exists.
- ARM rules not read because rules.mt.gov is unreachable: 24.16.7511 (final pay "immediately"), 24.16.7566 (penalty), 24.40.1609 (UI e-filing), 24.11.* (UI reports/separation), 42.17.105 (tables), 42.17.203 (records).
- Montana UI Contributions E-Filing Handbook (uid.dli.mt.gov): not located in the Wayback index search, not fetched.
- 2027 DOR withholding tables and Employer Guide: not yet indexed in Wayback (revenue.mt.gov/news/recent-news, 2026 captures).

## Open questions

Mirrors `unresolved[]` of the facts file (same keys, same wording).

- **mt.meta.register_id_pattern** (blocking): 18 facts rest on active register rows whose ids (US-MT-P5-1-001, US-MT-P5-1-003, US-MT-P5-1-004, US-MT-P5-1-005, US-MT-P5-1-006, US-MT-P5-2-001, US-MT-P5-2-002) do not match the facts-schema register_id pattern ^[A-Z]{2}-[A-Z0-9]{2,12}-[0-9]{3,4}$ (multi-hyphen legacy ids). They are carried in full in _facts_pending_register_id_pattern and are NOT yet consumable facts. What would close it: Orchestrator decision: a PATCH of facts.schema.json loosening the register_id pattern (e.g. ^[A-Z]{2}-[A-Z0-9-]{2,16}-[0-9]{3,4}$), or register alias ids; then run _research/synthesis-B/_work-MN-WY/promote.py to move the pending facts into facts[].
- **mt.minwage.hourly.next_year** (blocking): 2027 rate 11.20 is derived only (US-MTS5-017 partial); DLI 2027 letter capture is a 404. Not written as a fact. What would close it: DLI 2027 Minimum Wage Determination Letter or the 2027 poster (erd.dli.mt.gov).
- **mt.pit.tables.next_year** (non-blocking): 2027 withholding formula/tables (top 5.4%, brackets 65,000+) not published. What would close it: DOR Employer and Information Agent Guide for 2027 (revenuefiles.mt.gov), Nov/Dec 2026.
- **mt.report.ui.file_format** (non-blocking): UI quarterly report file format not obtained. What would close it: Montana UI Contributions E-Filing Handbook (uid.dli.mt.gov).
- **mt.labour.paycard_deductions_records** (non-blocking): Paycard rules, written authorization for deductions and wage-and-hour record retention not read (rules.mt.gov unreachable). What would close it: ARM Title 24 chapter 16 text from rules.mt.gov.
- **mt.bik.conformity.departures** (non-blocking): Income-tax departures from federal exclusions (HSA, 125, transit) not checked in statute. What would close it: MCA 15-30-2110 on mca.legmt.gov.
- **mt.leave.public_sick_and_child_labour** (non-blocking): Public-employee sick leave (2-18-618) and child-labour hours not read. What would close it: MCA 2-18-618 and 41-2-1xx on mca.legmt.gov.
- **mt.leave.vacation.case_text** (non-blocking): Langager v. Crazy Creek read only through the DLI decision (A.3). What would close it: Montana Supreme Court opinion text, 1998 MT 44.
