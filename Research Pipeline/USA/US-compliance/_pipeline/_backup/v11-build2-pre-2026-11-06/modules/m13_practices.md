# Module 13: Common Business Practices & Non-Statutory Rules

*Purpose: To capture prevalent, non-statutory conventions.*

### Describe the common practice for off-cycle or ad-hoc payments.

An off-cycle payment (bonus, correction, final pay on a non-payday) is a supplemental wage when paid apart from the regular wages. Withhold at the optional flat [[FACT:fed.fit.supplemental.flat_rate=22]]%, or aggregate with the last regular payment [US-FEDS5-003]. FICA and FUTA run against the cumulative annual bases (Module 9.2). The State supplemental rule of Module 9, Table 9.2.1 applies. Not configured in this release [[GAP:RQ-537]]: Employer-practice conventions for off-cycle runs (frequency, approval, use of the flat vs aggregate method) were not established from an official source.

### How are non-recoverable draws against future commissions typically handled?

Draws and commissions are wages when paid. The verified sources give one related State rule: Iowa's final-pay rule ([[FACT:ia.final_pay.rule=next regular payday for the period in which wages were earned (no discharge/resignation distinction); commission true-up within 30 days; vacation only per agreement/pro-rata policy (91A.4)]]) [US-IAS5-003]. Not configured in this release [[GAP:RQ-538]]: The treatment of recoverable and non-recoverable commission draws (wage status when advanced, recovery limits under minimum-wage and wage-deduction law) is not established from an official source.

### Are there common non-statutory leave types? How are they managed and reported?

Vacation and paid time off are not statutory entitlements. They are granted by employer policy. State law governs their payout at separation where a policy grants them (Module 8, Table 8.1.3). Leave pay is wages, reported in the ordinary W-2 boxes. Some States require sick-leave balances on the pay statement (Module 10, Table 10.3.1). Not configured in this release [[GAP:RQ-539]]: Prevalent non-statutory leave types (bereavement, floating holidays, volunteer days) were not established from an official source.

## 13.1 Configuration Practices and Known Traps

Each row is a build rule established from an official source. It records a point where a published source, a statute and the withholding method diverge, and which one the engine follows.

| Jurisdiction | Practice (value) | Register |
|---|---|---|
| SC | [[FACT:practice.sc.withholding_rates_2026=Withholding tables in force: SCDOR WH-1603 (Rev. 10/30/25) 2026 tables, 0/3/6%; SCDOR Information Letter #26-20 gives the Act 110 2026 schedule 1.99% (0-29,999) / 5.21% minus 966 (30,000+) and says withholding is unchanged until DOR republishes the tables]] | US-SCS5-004; US-SCS5-005 |
| WI | [[FACT:practice.wi.use_w166_tables=Withholding uses W-166 schedule (3.54/4.65/5.30/7.65%), not the assessment brackets (3.50/4.40/5.30/7.65%)]] | US-WIS5-010; US-WIS5-011 |
| NE | [[FACT:practice.ne.use_circular_en_tables=Withholding uses the DOR Circular EN 2026 percentage-method tables (2.26% to 4.60% rates); the statute (77-2715.03) sets 4.55% for rate three in tax year 2026]] | US-NES5-010; US-NES5-018 |
| KS | [[FACT:practice.ks.kw100_header_stale=KW-100 header prints "wages paid on and after January 1, 2021" but figures are the 2024 values in force for 2026 (5.20/5.58%)]] | US-KSS5-001 |
| MI | [[FACT:practice.mi.tips_ot_deduction_level=MI 2025 PA 24 tips/overtime deduction (TY2026-2028) is ASSESSMENT only; no change to withholding]] | US-MIV6-002 |
| VA | [[FACT:practice.va.std_deduction_2027_not_modelled=Statute: 2027 standard deduction 9,200/18,400; do not model 2027 withholding until Virginia Tax publishes the 2027 formula (guide Rev. 10/26 says the deduction sunsets - wrong)]] | US-VAS5-018 |
| DC | [[FACT:practice.dc.2026_method_unpublished=D.C. Act 26-416 (emergency, from 2026-08-13) revoked personal exemptions; no 2026 withholding method published (D-4 under review)]] (from 2026-08-13) | US-DCS5-021 |
| CT | [[FACT:practice.ct.tables_vs_rules=DRS: 'Use either the withholding calculation rules or the withholding tables' (TPG-211); the two methods can give different amounts; configured: DRS per-period tables up to each table maximum, TPG-211 rules above (CT.2, configuration decision of 2026-11-02)]] | US-CTS5-010; US-CTWH-001 |
| OH | [[FACT:practice.oh.flat_rate_vs_tables=Ohio withholding follows the tax commissioner's tables under ORC 5747.06, graduated 1.6% / 2.99% / 3.4% from 2026-08-01 (US-OH-006, US-OHS5-001); the ORC 5747.02 statute rate for TY2026 and thereafter is a flat 2.75% over 26,050 (US-OHS5-007) - use the tables for withholding]] | US-OHS5-007; US-OHS5-008; US-OH-006; US-OHS5-001 |
| OR | [[FACT:practice.or.federal_cap=Use 8,750 federal-tax subtraction cap (pp.6-7 formula); DOR publication also prints 8,500 and its example 1 is mis-computed]] | US-ORS5-009 |
| HI | [[FACT:practice.hi.2027_tables_pending=Act 24 SLH 2026 changes TY2027 brackets (new 13% top); 2027 withholding indeterminate until DOTAX issues 2027 Booklet A]] | US-HIS5-029 |
| GA | [[FACT:practice.ga.rate_change_2026=4.99% for taxable years beginning on/after 2026-01-01 (5.19% before); from 2027-01-01 reduced by 0.125 point annually to 3.99%, each step delayed one year if an OPB trigger holds at 1 December]] | US-GAS5-009 |
| MA | [[FACT:practice.ma.pfml_split=Follow DFML: 2026 split unchanged, swap from 2027-01-01 (Ch. 101/2026 s.45 conflict recorded)]] | US-MAS5-012; US-MAS5-026 |
| AL | [[FACT:practice.al.fit_before_sit=AL state base deducts federal withholding: order FIT before AL SIT]] | US-ALS5-001 |
| FED | [[FACT:practice.fed.estimator_not_oracle=IRS Tax Withholding Estimator is not an employer engine or oracle]] | US-FED-021 |
| FED | [[FACT:practice.fed.pl119_21_withholding=Do not reduce FIT withholding for tips/overtime deductions except through W-4 Step 4(b)]] | US-FEDS5-030 |

**Mid-year changes are applied by payment date.** Configure every dated value with its effective date and select it by the payment date of the run, never by the period worked (Module 11, Table 11.1.1). Massachusetts PFML is the exception and follows the earning date [US-MAS5-012]. Examples in 2026: Ohio withholding tables from [[FACT:oh.wh.tables.effective_from=2026-08-01]]; District of Columbia minimum wage [[FACT:dc.minwage.hourly=17.95]] (2025-07-01 to 2026-06-30); [[FACT:dc.minwage.hourly=18.40]] (from 2026-07-01); Idaho zero bracket [[FACT:id.wh.zero_bracket.single.biweekly=577]] (2025-04-28 to 2026-07-22); [[FACT:id.wh.zero_bracket.single.biweekly=619]] (from 2026-07-23).

**Tips and overtime deductions at assessment only (do not reduce withholding).** Federal: [[FACT:fed.plaw119_21.tips_overtime.level=assessment; withholding only via W-4 Step 4(b); employer reporting W-2 TP/TT/14b; FICA unchanged]] [US-FEDS5-030]. States established from official sources:

| State | Rule | Register |
|---|---|---|
| MI | [[FACT:mi.pit.tips_overtime_deduction=2025 PA 24 (MCL 206.30(1)(ee)): tax years 2026-2028 deduct federally allowed qualified tips (IRC 224) and overtime (IRC 225); level ASSESSMENT (MI-1040) only - no withholding change]] | [US-MIV6-002] |
| AL | Overtime premium deduction up to [[FACT:al.pit.overtime_premium_deduction.max=1,000]] (tax years 2026-2028); assessment only | [US-ALS5-004] |
| GA | Overtime subtraction up to [[FACT:ga.pit.overtime_subtraction.max=1,750]] and tip subtraction up to [[FACT:ga.pit.tip_subtraction.max=1,750]]; assessment only | [US-GAS5-009] |
| IA | [[FACT:ia.pit.obbba=tips, overtime, car-loan interest conformed at ASSESSMENT only (no withholding allowance); senior deduction (up to 6,000) may be claimed as an IA W-4 allowance]] | [US-IAS5-019] |
| HI | Tips deduction conformed at assessment; overtime deduction not conformed | [US-HIS5-029] |
| DC | [[FACT:dc.pit.obbba_deductions=disallowed TY2025; allowed as DC deductions from TY2026; operating level assessment only (no withholding change)]] | [US-DCS5-021] |

**Open practice points:**

- Massachusetts PFML split, transition date: Not configured in this release [[GAP:RQ-540]]: Chapter 101 of 2026 (s.45) applies the family/medical split change to taxable years from 2026-01-01, while the Department of Family and Medical Leave applies it from 2027-01-01. The build follows the Department (2026 split unchanged) until a notice or regulation settles the transition.
- DOL compilation lists: Not configured in this release [[GAP:RQ-541]]: The U.S. DOL compilation of State paid-leave laws could not be read, and the DOL prevailing-wage compilation is out of date for Michigan. Never read Michigan's paid-leave or prevailing-wage status from a DOL compilation table.
- Utah Pub. 14 effective date: Not configured in this release [[GAP:RQ-542]]: The effective date of Utah Pub. 14 (Rev. 04/26) is not established, so its six reproduced examples are not dated results.
- District of Columbia 2026 method: Not configured in this release [[GAP:RQ-543]]: The District of Columbia has published no 2026 withholding method: an emergency act effective 2026-08-13 revoked personal exemptions and the D-4 is under review.
- North Dakota booklet: the Section 2 example is a booklet defect. Configure from the table (Module 12, 12.2.1) [US-NDS5-001].
- Virginia 2027: statutory standard deduction [[FACT:va.pit.std_deduction.single=9,200]] single / [[FACT:va.pit.std_deduction.married=18,400]] married (2026: [[FACT:va.pit.std_deduction.single=8,750]] / [[FACT:va.pit.std_deduction.married=17,500]]) [US-VAS5-018]. It is not modelled in withholding until Virginia Tax publishes the 2027 formula (row above).
