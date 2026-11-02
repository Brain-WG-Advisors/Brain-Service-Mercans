## @labour
- **Minimum wage (40 O.S. 197.2) [US-OKS5-001].** The state rate equals the current federal minimum wage (follows federal: {{ok.labour.minwage.state.follows_federal}}); the figure is in Annex FED. No state increase is possible in 2027 without a federal change. Coverage and exclusions of the state Act are in Section 14.
- **Local minimum wage and local leave mandates:** preempted (40 O.S. 160): {{ok.local_mandates.preempted}} [US-OKS5-002].
- **Overtime:** {{ok.labour.overtime.state_rule}}; the FLSA rule applies (Annex FED) [US-OKS5-017, US-OKS5-022].
- **Pay frequency (40 O.S. 165.2) [US-OKS5-003, US-OK-003]:** {{ok.pay_frequency.rule}}. Exempt staff and public employees may be paid at least monthly.
- **Method of payment (165.2) [US-OKS5-003]:** {{ok.payment.method}}. ODOL guidance reads the paycard rule differently (open point below).
- **Dishonoured paycheck:** the employer reimburses the employee's bank fees within {{ok.labour.dishonoured_check.reimburse_days}} days [US-OKS5-003]. Rest breaks apply only to minors under 16 (40 O.S. 75) [US-OKS5-017].

## @income_tax
- **Statutory rates from tax year 2026 (68 O.S. 2355(D), HB 2764) [US-OKS5-009].** Single bands: zero rate on the first {{ok.pit.statutory.bracket.single.1.width}} USD; {{ok.pit.statutory.rate.2}} % on the next {{ok.pit.statutory.bracket.single.2.width}} USD; {{ok.pit.statutory.rate.3}} % on the next {{ok.pit.statutory.bracket.single.3.width}} USD; {{ok.pit.statutory.rate.top}} % on the remainder. Joint filers use double-width bands (statute; widths not carried as facts).
- **Standard deduction (68 O.S. 2358, not indexed) [US-OKS5-011]:** single {{ok.pit.std_deduction.single}} USD; married filing jointly {{ok.pit.std_deduction.mfj}} USD; head of household {{ok.pit.std_deduction.hoh}} USD. Allowance {{ok.pit.allowance.annual}} USD per year [US-OK-001].
- **Withholding method [US-OK-001]:** {{ok.wh.method}}, effective 2026-01-01. The annual percentage-method thresholds are the standard deduction plus the statutory band edges: single {{ok.pit.wh.single.annual.thresholds}}; married {{ok.pit.wh.married.annual.thresholds}} (USD, at which the zero, first, second and top bands begin). "Married, but withhold at the higher Single rate" uses the Single table. Per-period tables are published in OW-2.
- **Rounding (68 O.S. 2385.2(B)) [US-OKS5-010]:** {{ok.pit.rounding}}.
- **Oracle:** OW-2 percentage-method example (semimonthly, married, two allowances): {{ok.pit.oracle.example_1.withholding}} USD, reproduced exactly [US-OK-001]. Recomputation in Module 12.
- **Certificate [US-OKS5-014, US-OKS5-021]:** {{ok.wh.certificate}}. A federal W-4 signed before the 2018 changeover still governs for older hires.
- **Supplemental wages [US-OK-005, US-OKS5-014]:** if paid separately or identified, the highest statutory rate ({{ok.wh.supplemental.rate}} % for 2026) or the aggregate method; if paid together with regular wages and not separated, treat as one regular payment. The rule still cross-references the pre-2026 subsection; the rates sit in 2355(D).
- **Exclusions from withholding wages (68 O.S. 2385.1(e)) [US-OKS5-010]:** farm work up to {{ok.pit.agricultural.monthly_threshold}} USD a month; domestic service in a private home; casual work outside the trade or business; nonresidents with no more than {{ok.pit.nonresident.quarterly_threshold}} USD of Oklahoma income in a quarter; ministers and members of religious orders.
- **Nonresident aliens:** {{ok.pit.nra.rate}} % under 68 O.S. 2355(G) and OAC 710:90-1-8 [US-OKS5-009]; whether it replaces table withholding on wages is open (below).
- **Local wage tax:** none (exists: {{ok.local_wage_tax.exists}}) [US-OKP9V-001]. **Reciprocity:** {{ok.reciprocity.states}} [US-OKP51-002]. Residents get a credit for tax paid to another state on Form 511-TX [US-OKP52-002].
- **Resident and nonresident matrix.**

| Income type | Resident | Nonresident (US) |
|---|---|---|
| Regular salary | Withheld on services inside or outside Oklahoma (2385.1(c)), OW-2 | Withheld only on services performed in Oklahoma, above the quarterly de minimis |
| Bonus / supplemental | Top statutory rate or aggregate | Same, Oklahoma-source share |
| Nonresident alien | - | Flat NRA rate per 2355(G) (interaction with tables open) |
| Severance, equity, benefits in kind | Follow the IRC wage definition (2385.1) | Oklahoma-source share |

- **Rate-cut trigger:** the earliest possible statutory cut takes effect 2028-01-01 (62 O.S. 34.103(D)); none in 2027 [US-OKS5-025].

## @social
- **Unemployment insurance (OESC) [US-OK-002, US-OKS5-018].** Employer-only; the law forbids deducting contributions from wages (employee rate {{ok.sui.employee.rate}} %) [US-OKS5-005].

| Year | Taxable wage base | Experienced rate range | New employer | Register id |
|---|---|---|---|---|
| 2026 | {{ok.sui.wage_base@2026-01-01}} USD | {{ok.sui.employer.rate.min@2026-01-01}} % to {{ok.sui.employer.rate.max@2026-01-01}} % | {{ok.sui.new_employer.rate}} % | US-OK-002 |
| 2027 | {{ok.sui.wage_base@2027-01-01}} USD | {{ok.sui.employer.rate.min@2027-01-01}} % to {{ok.sui.employer.rate.max@2027-01-01}} % | same rate, 2026-2027 | US-OKS5-018 |

- **Wage-base mechanism (40 O.S. 1-201(48), 1-223) [US-OKS5-005]:** a percentage of the state average annual wage of the second preceding year, rounded to the nearest hundred dollars; the 2027 caliber is {{ok.ui.average_annual_wage.caliber}} USD [US-OKS5-018]. The 2026 and 2025 bases reproduce only with the pre-amendment percentages (open point below).
- **Wages reported to another state count toward the base:** {{ok.sui.wage_base.other_state_credit}} [US-OKS5-005].
- **UI wages (40 O.S. 1-218) [US-OKS5-006]:** elective retirement deferrals included ({{ok.sui.wages.401k_included}}); cafeteria-plan payments included: {{ok.sui.wages.section125_included}}. UI therefore departs from income tax for deferrals.
- **No SDI, TDI, PFML, LTC, transit or workforce levy** [US-OKP9V-001, US-OKP9V-002, US-OKS5-026].

## @payslip
- **Content (40 O.S. 165.2) [US-OKS5-003, US-OK-003]:** {{ok.payslip.items}}. No other content is mandated by state law; gross, hours and rates follow from FLSA records (Annex FED). Paper or electronic delivery per ODOL guidance [US-OKS5-022]. The rule follows work in Oklahoma (165.1(1)).
- **Retention:** payroll-tax records {{ok.records.payroll_tax.retention_years}} years after the due or payment date, whichever is later (OAC 710:90-1-11) [US-OKS5-014].

## @reporting
- **Withholding return (68 O.S. 2385.3; OAC 710:90-3-4) [US-OKS5-010, US-OKS5-014, US-OK-001]:** quarterly, due {{ok.report.wh.return_due}}; zero return required. Remittance monthly once quarterly withholding reaches {{ok.report.wh.monthly_threshold.quarterly}} USD; federal semiweekly depositors follow the federal dates. Channel: OkTAP.
- **W-2 and annual reconciliation:** {{ok.report.w2.due}} [US-OKS5-010]; to a departing employee within the statutory period after the last wage payment.
- **UI quarterly wage report (OES-3) [US-OKS5-020]:** filed in EZ Tax Express by manual entry or upload; upload format {{ok.report.ui.format}}; required on every active account. Statutory due date: open point below.
- **New hire (40 O.S. 2-802) [US-OKS5-007, US-OKS5-029]:** every hire who resides or works in Oklahoma, within {{ok.newhire.report_days}} days of start, to OESC.
- **Registration:** OTC withholding account at tax.ok.gov; OESC account via EZ Tax Express; powers of attorney BT-129 (OTC) and OES-190T (OESC) [US-OKP51-004, US-OKP51-005].

## @leave
- **Paid sick leave:** no state statute (exists: {{ok.leave.sick.state_statute.exists}}); local mandates preempted (40 O.S. 160) [US-OKS5-002]. No PFML or SDI [US-OKS5-026].
- **Voting leave (26 O.S. 7-101):** {{ok.leave.voting.paid_hours}} hours paid on proof of voting, with advance notice; not due where the shift leaves enough time before or after the polls [US-OKS5-023].
- **Jury duty:** no duty to pay non-exempt employees; the employer may not require use of paid leave; exempt employees keep their salary with an offset for jury fees [US-OKS5-024, US-OKS5-022]. Military leave: open point below.

## @termination
- **Final pay (40 O.S. 165.3) [US-OKS5-004]:** {{ok.final_pay.rule}}, or by certified mail on request; amounts in bona fide dispute excluded; liquidated damages for wilful failure.
- **Accrued vacation:** {{ok.term.vacation.payout}} (165.1(7)) [US-OKS5-003]; no statute forces payout.
- **Separation notice:** no general UI separation-notice duty in Title 40. W-2 to a departing employee within the statutory period [US-OKS5-010]; IWO termination notice to the support agency [US-OKS5-015].

## @bik
- **Income tax:** withholding wages carry the IRC meaning apart from the 2385.1(e) exclusions, so the federal exclusions carry over [US-OKS5-010]; Oklahoma adjustments (68 O.S. 2358) not reviewed item by item (open point below).
- **UI departs:** elective deferrals are UI wages; cafeteria-plan, educational-assistance and dependent-care payments are excluded [US-OKS5-006].

## @deductions
- **Wage deductions:** beyond statutory deductions and court orders, a written agreement signed by both parties is required (ODOL guidance) [US-OKS5-022]; the underlying rule is open (below).
- **Creditor garnishment (31 O.S. 1(A)(18)) [US-OKS5-013]:** maximum {{ok.garn.creditor.max_percent}} % of disposable earnings, subject to the federal CCPA floor (Annex FED).
- **Continuing earnings garnishment (12 O.S. 1173.4) [US-OKS5-012]:** lien of {{ok.garn.continuing.lien_days}} days; the earlier lien has priority.
- **Child support (12 O.S. 1171.2, 1171.3) [US-OKS5-012, US-OKS5-015]:** CCPA support percentages; priority current support, health premiums, arrears, then other; remit to the Centralized Support Registry within {{ok.garn.iwo.remit_days}} days of payday; employer fee {{ok.garn.iwo.employer_fee.per_period}} USD per pay period, with a monthly cap.

## @cba
- **No state prevailing wage** (exists: {{ok.prevailing_wage.exists}}): the Minimum Wages on Public Works Act was held unconstitutional and repealed by Laws 2015 c. 71, effective 2015-11-01 [US-OKS5-016]. Federal Davis-Bacon applies on federally funded work.

## @indexation
- **Minimum wage:** follows the federal rate only [US-OKS5-001].
- **SUI wage base and rate range:** yearly, published by OESC (Section 3) [US-OKS5-005, US-OKS5-018].
- **PIT brackets, standard deduction, allowance:** not indexed; rates fall only through the revenue trigger (earliest 2028-01-01) [US-OKS5-009, US-OKS5-011, US-OKS5-025].
- **Withholding tables:** reissued when the law changes (OW-2) [US-OK-001].

## @data
- **40 O.S. 173.1 (private employers) [US-OKS5-008]:** no public display of SSNs; no SSN on access cards; no unsecured transmission; no SSN as sole login; no SSN on materials mailed to the employee unless law requires it ({{ok.data.ssn.mailed_materials_prohibited}}). A mailed paper payslip falls under this rule: mask the SSN.
- **Annual withholding statement:** may show only the last digits of the SSN ({{ok.data.w2.ssn_last4_allowed}}) (OAC 710:90-1-10) [US-OKS5-014].

## @live
- **2026-01-01:** new statutory rates in force; OW-2 (Rev. 11-2025) implements them [US-OKS5-009, US-OK-001].
- **2025-11-01:** UI percentage amendments (Laws 2025 c. 140) and tip-credit link to the federal cash wage (Laws 2025 c. 401) [US-OKS5-005, US-OKS5-001].
- **2027-01-01:** published SUI numbers (Section 3) [US-OKS5-018]. Paid-leave and tips/overtime bills (SB 277, SB 470, SB 1986) not enacted [US-OKS5-026]; OTC announced no withholding change [US-OKS5-028]. The 2026 session laws were not swept as a whole (open point below).

## @special
| Population | Oklahoma rule | Register id |
|---|---|---|
| Domestic / household | Exempt from withholding (2385.1(e)(2)); UI covered above a quarterly cash test; excluded from the state minimum-wage Act (FLSA may apply) | US-OKS5-010, US-OKS5-006, US-OKS5-001 |
| Agricultural | Withholding exempt up to {{ok.pit.agricultural.monthly_threshold}} USD a month; UI coverage tests; H-2A excluded; excluded from the state minimum-wage Act | US-OKS5-010, US-OKS5-006, US-OKS5-027, US-OKS5-001 |
| Minors | Under 16: hours and rest-break limits; state Act excludes minor non-graduates; minor newspaper carriers excluded from UI | US-OKS5-017, US-OKS5-001, US-OKS5-027 |
| Tipped | Tip credit if the cash wage is at least the federal 29 CFR 531.50 amount; UI wages include tips | US-OKS5-001, US-OKS5-006 |
| Clergy / religious | Exempt from withholding and excluded from UI | US-OKS5-010, US-OKS5-027 |
| Students | UI excludes own-school employment, work-study and student nurses; state Act excludes students below the statutory age | US-OKS5-027, US-OKS5-001 |
| Nonresident aliens | NRA rate {{ok.pit.nra.rate}} % (interaction with tables open) | US-OKS5-009, US-OKS5-014 |
| Nonresidents (US) | Withheld on Oklahoma services above the quarterly de minimis; no reciprocity; no convenience rule found | US-OKS5-010, US-OKP51-002, US-OKP52-001 |
| Military / spouses | OK-W-4 exemption lines for MSRRA (with OW-9-MSE) and active-duty pay | US-OKS5-021 |
| Statutory employees / officers | Corporate officers are employees for withholding (2385.1(c)) | US-OKS5-010 |
| Government employees | Paid at least monthly; elected officials excluded from UI; the SSN rule does not bind the state | US-OKS5-003, US-OKS5-001, US-OKS5-027, US-OKS5-008 |
| Family employment | UI excludes service for a child or spouse, and a minor child working for a parent | US-OKS5-027 |
| Commission insurance / real-estate agents | Excluded from UI | US-OKS5-027 |

## @gaps
- ok.ui.wage_base.history :: The 2025 and 2026 wage bases reproduce only with the percentages in force before Laws 2025 c. 140 (an inference from arithmetic; the old text was not read). :: Laws 2025 c.140 enrolled text.
- ok.pit.nra.wages :: Whether the flat NRA rate of 2355(G) replaces table withholding on nonresident-alien wages is open. :: OTC withholding FAQ/ruling or OAC 710:90-1-8 rulemaking history.
