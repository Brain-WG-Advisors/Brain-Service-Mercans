# Module 13: Common Business Practices & Non-Statutory Rules

*Purpose: To capture prevalent, non-statutory conventions.*

### Describe the common practice for off-cycle or ad-hoc payments.

An off-cycle payment (bonus, correction, final pay on a non-payday) is a supplemental wage when paid apart from the regular wages. Withhold at the optional flat [[FACT:fed.fit.supplemental.flat_rate=22]]%, or aggregate with the last regular payment [US-FEDS5-003]. FICA and FUTA run against the cumulative annual bases (Module 9.2). The State supplemental rule of Module 9, Table 9.2.1 applies. ⚠️ RESEARCH-GAP: employer-practice conventions for off-cycle runs (frequency, approval, use of the flat vs aggregate method) were not researched.

### How are non-recoverable draws against future commissions typically handled?

Draws and commissions are wages when paid. The facts carry one related State rule: Iowa's final-pay rule ([[FACT:ia.final_pay.rule=next regular payday for the period in which wages were earned (no discharge/resignation distinction); commission true-up within 30 days; vacation only per agreement/pro-rata policy (91A.4)]]) [US-IAS5-003]. ⚠️ RESEARCH-GAP: the treatment of recoverable and non-recoverable commission draws (wage status when advanced, recovery limits under minimum-wage and wage-deduction law) is not keyed.

### Are there common non-statutory leave types? How are they managed and reported?

Vacation and paid time off are not statutory entitlements. They are granted by employer policy. State law governs their payout at separation where a policy grants them (Module 8, Table 8.1.3). Leave pay is wages, reported in the ordinary W-2 boxes. Some States require sick-leave balances on the pay statement (Module 10, Table 10.3.1). ⚠️ RESEARCH-GAP: prevalent non-statutory leave types (bereavement, floating holidays, volunteer days) were not researched.

## 13.1 Configuration Practices and Known Traps

Each row is a build rule held as a fact. It records a point where a published source, a statute and the withholding method diverge, and which one the engine follows.

| Jurisdiction | Practice (value) | Register |
|---|---|---|
| SC | [[FACT:practice.sc.withholding_rates_2026=Use WH-1603 tables 0/3/6% for 2026 withholding; Act 110 rates (1.99%/5.21%) apply at the 2026 annual return only]] | US-SCS5-004 |
| WI | [[FACT:practice.wi.use_w166_tables=Withholding uses W-166 schedule (3.54/4.65/5.30/7.65%), not the assessment brackets (3.50/4.40/5.30/7.65%)]] | US-WIS5-010 |
| NE | [[FACT:practice.ne.use_circular_en_tables=Withholding uses DOR Circular EN tables (2026 2.26-4.60%), not the statutory 4.55% rate]] | US-NES5-018 |
| KS | [[FACT:practice.ks.kw100_header_stale=KW-100 header prints "wages paid on and after January 1, 2021" but figures are the 2024 values in force for 2026 (5.20/5.58%)]] | US-KSS5-001 |
| MI | [[FACT:practice.mi.tips_ot_deduction_level=MI 2025 PA 24 tips/overtime deduction (TY2026-2028) is ASSESSMENT only; no change to withholding]] | US-MIS5-017 |
| VA | [[FACT:practice.va.std_deduction_2027_not_modelled=Statute: 2027 standard deduction 9,200/18,400; do not model 2027 withholding until Virginia Tax publishes the 2027 formula (guide Rev. 10/26 says the deduction sunsets - wrong)]] | US-VAS5-018 |
| DC | [[FACT:practice.dc.2026_method_unpublished=D.C. Act 26-416 (emergency, from 2026-08-13) revoked personal exemptions; no 2026 withholding method published (D-4 under review)]] (from 2026-08-13) | US-DCS5-021 |
| CT | [[FACT:practice.ct.tables_vs_rules=DRS permits tables or TPG-211 rules; results differ up to 0.48/period; engine must choose one method (CT-OQ-1)]] | US-CTS5-010 |
| OH | [[FACT:practice.oh.flat_rate_vs_tables=TY2026 statute flat 2.75% but withholding tables graduated to 3.4% (5747.06 rule vs 5747.02 rate) - use the tables]] | US-OHS5-007 |
| OR | [[FACT:practice.or.federal_cap=Use 8,750 federal-tax subtraction cap (pp.6-7 formula); DOR publication also prints 8,500 and its example 1 is mis-computed]] | US-ORS5-009 |
| HI | [[FACT:practice.hi.2027_tables_pending=Act 24 SLH 2026 changes TY2027 brackets (new 13% top); 2027 withholding indeterminate until DOTAX issues 2027 Booklet A]] | US-HIS5-029 |
| GA | [[FACT:practice.ga.rate_change_2026=4.99% for TY2026 (5.19% before); 2027 0.125-point step conditional on OPB report of 2026-12-01]] | US-GAS5-009 |
| MA | [[FACT:practice.ma.pfml_split=Follow DFML: 2026 split unchanged, swap from 2027-01-01 (Ch. 101/2026 s.45 conflict recorded)]] | US-MAS5-012 |
| AL | [[FACT:practice.al.fit_before_sit=AL state base deducts federal withholding: order FIT before AL SIT]] | US-ALS5-001 |
| FED | [[FACT:practice.fed.estimator_not_oracle=IRS Tax Withholding Estimator is not an employer engine or oracle]] | US-FED-021 |
| FED | [[FACT:practice.fed.pl119_21_withholding=Do not reduce FIT withholding for tips/overtime deductions except through W-4 Step 4(b)]] | US-FEDS5-030 |

**Tips and overtime deductions at assessment only (do not reduce withholding).** Federal: [[FACT:fed.plaw119_21.tips_overtime.level=assessment; withholding only via W-4 Step 4(b); employer reporting W-2 TP/TT/14b; FICA unchanged]] [US-FEDS5-030]. States keyed in the facts:

| State | Rule | Register |
|---|---|---|
| MI | [[FACT:mi.pit.tips_overtime_deduction=2025 PA 24 (MCL 206.30(1)(ee)): tax years 2026-2028 deduct federally allowed qualified tips (IRC 224) and overtime (IRC 225); level ASSESSMENT (MI-1040) only - no withholding change]] | [US-MIS5-017] |
| AL | Overtime premium deduction up to [[FACT:al.pit.overtime_premium_deduction.max=1,000]] (tax years 2026-2028); assessment only | [US-ALS5-004] |
| GA | Overtime subtraction up to [[FACT:ga.pit.overtime_subtraction.max=1,750]] and tip subtraction up to [[FACT:ga.pit.tip_subtraction.max=1,750]]; assessment only | [US-GAS5-009] |
| IA | [[FACT:ia.pit.obbba=tips, overtime, car-loan interest conformed at ASSESSMENT only (no withholding allowance); senior deduction (up to 6,000) may be claimed as an IA W-4 allowance]] | [US-IAS5-019] |
| HI | Tips deduction conformed at assessment; overtime deduction not conformed | [US-HIS5-029] |
| DC | [[FACT:dc.pit.obbba_deductions=disallowed TY2025; allowed as DC deductions from TY2026; operating level assessment only (no withholding change)]] | [US-DCS5-021] |

**Open practice points (not facts):**

- Massachusetts PFML split, transition date: ⚠️ RESEARCH-GAP: Chapter 101 of 2026 (s.45) applies the family/medical split change to taxable years from 2026-01-01, while the Department of Family and Medical Leave applies it from 2027-01-01. The build follows the Department (2026 split unchanged) until a notice or regulation settles the transition.
- DOL compilation lists: ⚠️ RESEARCH-GAP: the U.S. DOL compilation of State paid-leave laws could not be read, and the DOL prevailing-wage compilation is out of date for Michigan. Never read Michigan's paid-leave or prevailing-wage status from a DOL compilation table.
- Utah Pub. 14 effective date: ⚠️ RESEARCH-GAP: the effective date of Utah Pub. 14 (Rev. 04/26) is not established, so its six reproduced examples are not dated facts.
- District of Columbia 2026 method: ⚠️ RESEARCH-GAP: the District of Columbia has published no 2026 withholding method: an emergency act effective 2026-08-13 revoked personal exemptions and the D-4 is under review.
- North Dakota booklet: the Section 2 example is a booklet defect. Configure from the table (Module 12, 12.2.1) [US-NDS5-001].
- Virginia 2027: statutory standard deduction [[FACT:va.pit.std_deduction.single=9,200]] single / [[FACT:va.pit.std_deduction.married=18,400]] married (2026: [[FACT:va.pit.std_deduction.single=8,750]] / [[FACT:va.pit.std_deduction.married=17,500]]) [US-VAS5-018]. It is not modelled in withholding until Virginia Tax publishes the 2027 formula (row above).
