# Gotchas and traps

Each rule below is a point where a published source, a statute and the withholding instrument diverge, or where a dated value changes. The value, key, effective period and register id of every number are in the fact index at the end of this file.

## 1. Values that change over time (select by the date the rule keys on)

- **OASDI wage base:** USD 184,500 for wages paid 2026-01-01 to 2026-12-31 [US-FEDS5-005]; USD 192,300 from 2027-01-01 [US-FEDB5-401] (medium confidence). Never carry the 2026 figure into 2027.
- **Utah withholding allowance and phase-out:** base allowance USD 485 single and USD 970 married, phase-out rate 1.3 %, all with a period start of 2026-04-01 (Pub. 14, revision dated April 2026; the publication states no effective date) [US-UTPIT-003]. The flat rate is 4.45 % from 2026-01-01 [US-UTS5-001]. The 2026-01-01 to 2026-03-31 allowance values are an open gap (RQ-596); do not back-date the April figures.
- **Massachusetts PFML:** total 0.88 % in both years, but the split swaps. 2026: family 0.18 % and medical 0.7 %. From 2027-01-01: family 0.7 % and medical 0.18 % [US-MAS5-012]. PFML follows the earning date, not the payment date. Statute (Chapter 101 of 2026, s.45) and the Department differ on the transition. Configuration rule: Follow DFML: 2026 split unchanged, swap from 2027-01-01 (Ch. 101/2026 s.45 conflict recorded) [US-MAS5-012].
- **Ohio withholding tables** apply from 2026-08-01 [US-OHS5-001].
- **District of Columbia minimum wage:** USD 17.95 per hour for hours worked to 2026-06-30, USD 18.40 for hours worked from 2026-07-01 [US-DCS5-011]. Minimum wage follows hours worked, not the payment date: June hours paid in July stay at the June rate.
- **Selection rule:** tax and contribution values are selected by the payment date of the run; minimum-wage rates by hours worked on or after the effective date; Massachusetts PFML by earning date.

## 2. Statute is not the withholding instrument

| Jurisdiction | Rule for the engine | Register |
|---|---|---|
| SC | Withholding tables in force: SCDOR WH-1603 (Rev. 10/30/25) 2026 tables, 0/3/6%; SCDOR Information Letter #26-20 gives the Act 110 2026 schedule 1.99% (0-29,999) / 5.21% minus 966 (30,000+) and says withholding is unchanged until DOR republishes the tables. Act 110 of 2026 must not be loaded into 2026 withholding. | US-SCS5-004 |
| WI | Withholding uses W-166 schedule (3.54/4.65/5.30/7.65%), not the assessment brackets (3.50/4.40/5.30/7.65%) | US-WIS5-010 |
| NE | Withholding uses the DOR Circular EN 2026 percentage-method tables (2.26% to 4.60% rates); the statute (77-2715.03) sets 4.55% for rate three in tax year 2026 | US-NES5-018 |
| KS | KW-100 header prints "wages paid on and after January 1, 2021" but figures are the 2024 values in force for 2026 (5.20/5.58%) | US-KSS5-001 |
| OH | Ohio withholding follows the tax commissioner's tables under ORC 5747.06, graduated 1.6% / 2.99% / 3.4% from 2026-08-01 (US-OH-006, US-OHS5-001); the ORC 5747.02 statute rate for TY2026 and thereafter is a flat 2.75% over 26,050 (US-OHS5-007) - use the tables for withholding | US-OHS5-007 |
| CT | DRS: 'Use either the withholding calculation rules or the withholding tables' (TPG-211); the two methods can give different amounts; configured: DRS per-period tables up to each table maximum, TPG-211 rules above (CT.2, configuration decision of 2026-11-02) | US-CTS5-010 |
| OR | Use 8,750 federal-tax subtraction cap (pp.6-7 formula); DOR publication also prints 8,500 and its example 1 is mis-computed | US-ORS5-009 |
| VA | Statute: 2027 standard deduction 9,200/18,400; do not model 2027 withholding until Virginia Tax publishes the 2027 formula (guide Rev. 10/26 says the deduction sunsets - wrong) | US-VAS5-018 |
| HI | Act 24 SLH 2026 changes TY2027 brackets (new 13% top); 2027 withholding indeterminate until DOTAX issues 2027 Booklet A | US-HIS5-029 |
| AL | AL state base deducts federal withholding: order FIT before AL SIT | US-ALS5-001 |
| GA | 4.99% for taxable years beginning on/after 2026-01-01 (5.19% before); from 2027-01-01 reduced by 0.125 point annually to 3.99%, each step delayed one year if an OPB trigger holds at 1 December | US-GAS5-009 |
| DC | D.C. Act 26-416 (emergency, from 2026-08-13) revoked personal exemptions; no 2026 withholding method published (D-4 under review). The last published instruction is Notice 2022-08: apply current rate schedule with the federal allowance amount (no FR-230 after 2018); applying to 2026 is an inference; the payroll calculation must flag that result as an inference (open gap RQ-138). | US-DCS5-021, US-DCP51-002 |

The Wisconsin, Nebraska, Kansas and Ohio withholding tables are therefore not the statutory brackets: use the withholding instrument, and keep the statutory rate for the annual return.

## 3. Tips and overtime deductions (Public Law 119-21) are assessment items

- Federal: Do not reduce FIT withholding for tips/overtime deductions except through W-4 Step 4(b) [US-FEDS5-030]. Level: assessment; withholding only via W-4 Step 4(b); employer reporting W-2 TP/TT/14b; FICA unchanged.
- MI: MI 2025 PA 24 tips/overtime deduction (TY2026-2028) is ASSESSMENT only; no change to withholding [US-MIS5-017].
- IA: tips, overtime, car-loan interest conformed at ASSESSMENT only (no withholding allowance); senior deduction (up to 6,000) may be claimed as an IA W-4 allowance [US-IAS5-019].
- DC: disallowed TY2025; allowed as DC deductions from TY2026; operating level assessment only (no withholding change) [US-DCS5-021].
- AL and GA: assessment only [US-ALS5-004], [US-GAS5-009]. HI: tips deduction conformed at assessment, overtime deduction not conformed [US-HIS5-029]; the withholding level in Hawaii is not established from an official source.

## 4. Channels and identifiers that are easy to mix up

- **Louisiana: LAWATS is not the wage-report channel.** The quarterly UI wage report is filed through the Louisiana Workforce Commission online services: due last day of month after quarter; domestic annual Jan 31; electronic filing required for reports due after 2014-01-31 ("Use LWC's online services to file wage reports and pay taxes"); DE students earning credit not reported [US-LAS5-007]. LAWATS appears only as the online power-of-attorney portal: Online Power of Attorney in LAWATS [US-LAP52-005]. Withholding L-1: L-1 quarterly, electronic (LaTAP/software), zero returns required, due Apr 30 / Jul 31 / Oct 31 / Jan 31; payment quarterly < 500/month average, monthly 500 to < 5,000, semi-monthly >= 5,000 [US-LAS5-003]. Annual: L-3 + W-2s due first business day after January 31 (30 days on closure); electronic mandatory at 50+ W-2s via LaWage; no magnetic media/CD; state boxes 16-18 [US-LAS5-009].
- **Hawaii HRS 487J:** Not required on the statement; section 487J-2 bars making an entire SSN available to the general public and printing an entire SSN on mailed materials, except employer-to-employee communications or where the individual requests it [US-HIS5-028]. The employer-to-employee mailing exemption applies; a full number must not appear in public or third-party material.
- **IRS Tax Withholding Estimator** is not an employer engine or oracle: IRS Tax Withholding Estimator is not an employer engine or oracle [US-FED-021].
- **North Dakota booklet:** the Section 2 worked example is a recorded defect; configure from the method and table [US-NDS5-001].

## 5. Federal FICA

- **Additional Medicare Tax uses its own year-to-date base.** Rate 0.9 % on wages paid above USD 200,000 in the calendar year, regardless of filing status; employee only, no employer match [US-FEDS5-005]. It is computed on the employee's cumulative calendar-year Medicare wages from the employer, separate from the OASDI base: Medicare wages are not capped (key `fed.fica.medicare.wage_base.capped`) while OASDI stops at its annual base. Do not reuse the OASDI year-to-date accumulator, and do not reset it on a filing-status basis.
- OASDI is capped by its annual base (section 1); Medicare is not.

## 6. Scope

- Independent contractors and Form 1099-NEC reporting are out of scope [US-OWN-008]. Employers in scope are private-sector employers; workers are common-law employees.
- Prevailing-wage and certified payroll reports are an informational overlay only [US-OWN-009].
- Territories are not covered; the jurisdiction set is the 50 States and the District of Columbia [US-OWN-002].


## Fact index

Every value above with its key, effective period and register id.

| Key | Value | Effective | Register id |
|---|---|---|---|
| `dc.minwage.hourly` | 17.95 | from 2025-07-01 to 2026-06-30 | US-DCS5-011 |
| `dc.minwage.hourly` | 18.40 | from 2026-07-01 | US-DCS5-011 |
| `dc.pit.obbba_deductions` | disallowed TY2025; allowed as DC deductions from TY2026; operating level assessment only (no withholding change) | from 2026-01-01 | US-DCS5-021 |
| `dc.wh.notice_2022_08` | apply current rate schedule with the federal allowance amount (no FR-230 after 2018); applying to 2026 is an inference | from 2022-01-01 | US-DCP51-002 |
| `fed.fica.addl_medicare.rate` | 0.9 | from 2026-01-01 to 2026-12-31 | US-FEDS5-005 |
| `fed.fica.addl_medicare.withholding_threshold` | 200,000 | from 2026-01-01 to 2026-12-31 | US-FEDS5-005 |
| `fed.fica.oasdi.wage_base` | 184,500 | from 2026-01-01 to 2026-12-31 | US-FEDS5-005 |
| `fed.fica.oasdi.wage_base` | 192,300 | from 2027-01-01 to 2027-12-31 | US-FEDB5-401 |
| `fed.plaw119_21.tips_overtime.level` | assessment; withholding only via W-4 Step 4(b); employer reporting W-2 TP/TT/14b; FICA unchanged | from 2026-01-01 | US-FEDS5-030 |
| `ia.pit.obbba` | tips, overtime, car-loan interest conformed at ASSESSMENT only (no withholding allowance); senior deduction (up to 6,000) may be claimed as an IA W-4 allowance | from 2026-01-01 | US-IAS5-019 |
| `la.report.annual.l3` | L-3 + W-2s due first business day after January 31 (30 days on closure); electronic mandatory at 50+ W-2s via LaWage; no magnetic media/CD; state boxes 16-18 | from 2026-01-01 | US-LAS5-009 |
| `la.report.sui.quarterly` | due last day of month after quarter; domestic annual Jan 31; electronic filing required for reports due after 2014-01-31 ("Use LWC's online services to file wage reports and pay taxes"); DE students earning credit not reported | from 2025-04-01 | US-LAS5-007 |
| `la.report.wh.l1` | L-1 quarterly, electronic (LaTAP/software), zero returns required, due Apr 30 / Jul 31 / Oct 31 / Jan 31; payment quarterly < 500/month average, monthly 500 to < 5,000, semi-monthly >= 5,000 | from 2026-01-01 | US-LAS5-003 |
| `ma.pfml.family.rate` | 0.18 | from 2026-01-01 to 2026-12-31 | US-MAS5-012 |
| `ma.pfml.family.rate` | 0.7 | from 2027-01-01 | US-MAS5-012 |
| `ma.pfml.medical.rate` | 0.18 | from 2027-01-01 | US-MAS5-012 |
| `ma.pfml.medical.rate` | 0.7 | from 2026-01-01 to 2026-12-31 | US-MAS5-012 |
| `ma.pfml.total.rate` | 0.88 | from 2026-01-01 | US-MAS5-012 |
| `oh.wh.tables.effective_from` | 2026-08-01 | from 2026-08-01 | US-OHS5-001 |
| `practice.al.fit_before_sit` | AL state base deducts federal withholding: order FIT before AL SIT | from 2026-01-01 | US-ALS5-001 |
| `practice.ct.tables_vs_rules` | DRS: 'Use either the withholding calculation rules or the withholding tables' (TPG-211); the two methods can give different amounts; configured: DRS per-period tables up to each table maximum, TPG-211 rules above (CT.2, configuration decision of 2026-11-02) | from 2026-01-01 | US-CTS5-010 |
| `practice.dc.2026_method_unpublished` | D.C. Act 26-416 (emergency, from 2026-08-13) revoked personal exemptions; no 2026 withholding method published (D-4 under review) | from 2026-08-13 | US-DCS5-021 |
| `practice.fed.estimator_not_oracle` | IRS Tax Withholding Estimator is not an employer engine or oracle | from 2026-01-01 | US-FED-021 |
| `practice.fed.pl119_21_withholding` | Do not reduce FIT withholding for tips/overtime deductions except through W-4 Step 4(b) | from 2026-01-01 | US-FEDS5-030 |
| `practice.ga.rate_change_2026` | 4.99% for taxable years beginning on/after 2026-01-01 (5.19% before); from 2027-01-01 reduced by 0.125 point annually to 3.99%, each step delayed one year if an OPB trigger holds at 1 December | from 2026-01-01 | US-GAS5-009 |
| `practice.hi.2027_tables_pending` | Act 24 SLH 2026 changes TY2027 brackets (new 13% top); 2027 withholding indeterminate until DOTAX issues 2027 Booklet A | from 2026-01-01 | US-HIS5-029 |
| `practice.ks.kw100_header_stale` | KW-100 header prints "wages paid on and after January 1, 2021" but figures are the 2024 values in force for 2026 (5.20/5.58%) | from 2024-07-01 | US-KSS5-001 |
| `practice.ma.pfml_split` | Follow DFML: 2026 split unchanged, swap from 2027-01-01 (Ch. 101/2026 s.45 conflict recorded) | from 2026-01-01 | US-MAS5-012 |
| `practice.mi.tips_ot_deduction_level` | MI 2025 PA 24 tips/overtime deduction (TY2026-2028) is ASSESSMENT only; no change to withholding | from 2026-01-01 to 2028-12-31 | US-MIS5-017 |
| `practice.ne.use_circular_en_tables` | Withholding uses the DOR Circular EN 2026 percentage-method tables (2.26% to 4.60% rates); the statute (77-2715.03) sets 4.55% for rate three in tax year 2026 | from 2026-01-01 | US-NES5-010 |
| `practice.oh.flat_rate_vs_tables` | Ohio withholding follows the tax commissioner's tables under ORC 5747.06, graduated 1.6% / 2.99% / 3.4% from 2026-08-01 (US-OH-006, US-OHS5-001); the ORC 5747.02 statute rate for TY2026 and thereafter is a flat 2.75% over 26,050 (US-OHS5-007) - use the tables for withholding | from 2025-09-30 | US-OHS5-007 |
| `practice.or.federal_cap` | Use 8,750 federal-tax subtraction cap (pp.6-7 formula); DOR publication also prints 8,500 and its example 1 is mis-computed | from 2026-01-01 | US-ORS5-009 |
| `practice.sc.withholding_rates_2026` | Withholding tables in force: SCDOR WH-1603 (Rev. 10/30/25) 2026 tables, 0/3/6%; SCDOR Information Letter #26-20 gives the Act 110 2026 schedule 1.99% (0-29,999) / 5.21% minus 966 (30,000+) and says withholding is unchanged until DOR republishes the tables | from 2026-01-01 | US-SCS5-004 |
| `practice.va.std_deduction_2027_not_modelled` | Statute: 2027 standard deduction 9,200/18,400; do not model 2027 withholding until Virginia Tax publishes the 2027 formula (guide Rev. 10/26 says the deduction sunsets - wrong) | from 2025-01-01 | US-VAS5-018 |
| `practice.wi.use_w166_tables` | Withholding uses W-166 schedule (3.54/4.65/5.30/7.65%), not the assessment brackets (3.50/4.40/5.30/7.65%) | from 2025-01-01 | US-WIS5-010 |
| `psl.hi.ssn.rule` | Not required on the statement; section 487J-2 bars making an entire SSN available to the general public and printing an entire SSN on mailed materials, except employer-to-employee communications or where the individual requests it | from 2026-01-01 | US-HIS5-028 |
| `sir.la.ui.agent_authorization` | Online Power of Attorney in LAWATS | from 2026-01-01 | US-LAP52-005 |
| `ut.pit.base_allowance.married.annual` | 970 | from 2026-04-01 | US-UTPIT-003 |
| `ut.pit.base_allowance.single.annual` | 485 | from 2026-04-01 | US-UTPIT-003 |
| `ut.pit.phaseout.rate` | 1.3 | from 2026-04-01 | US-UTPIT-003 |
| `ut.pit.rate.flat` | 4.45 | from 2026-01-01 | US-UTS5-001 |
