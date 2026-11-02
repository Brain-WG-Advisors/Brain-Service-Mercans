# Annex MULTI: Multistate routing layer

This annex is the routing layer. It decides, per employee, which State annexes apply in addition to Annex FED. Three master-data keys drive every decision: work location (income-tax withholding State and wage-hour law), residence (resident withholding, reciprocity, transport-worker and military-spouse rules) and the UI State resulting from the localization test (UI, and by default PFML/SDI). Every value is shown with its effective dates and its source.

Routing order for the engine:

1. Wage-hour law: the more protective of federal, State and local law at the place of performance ([[FACT:multi.wage_hour.overlay_rule=FLSA does not excuse a higher State/municipal minimum wage, a lower maximum workweek or a stricter child-labour standard: apply the more protective standard of the place where the work is performed]]).
2. UI State: the localization test, applied once per employee and employer ([[FACT:multi.sui.localization_test=One State covers the entire service with one employer, in order: (1) localized (entirely in the State, or out-of-state service incidental: temporary, transitory, isolated); (2) else some service in the base-of-operations State; (3) else some service in the State of direction or control; (4) else some service in the State of residence]]).
3. Work-State income-tax withholding: start when the non-resident threshold of the work State is met (MULTI.2 table), unless reciprocity with the residence State applies and the employee has filed the certificate (MULTI.2 reciprocity table).
4. Residence-State withholding: apply the residence State's rule for residents working elsewhere (MULTI.2 table); the credit for tax paid to another State is an assessment matter, never a payroll deduction.
5. Federal carve-outs override State sourcing for transport workers, seamen and military spouses.
6. PFML/SDI premium State: the UI State unless the State's own coverage test differs (MULTI.3 table).

## MULTI.1 Employment and labour code

Wage-hour law follows the place of performance. California's reach is decided statute by statute (court rulings below).

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Wage hour overlay rule | [[FACT:multi.wage_hour.overlay_rule=FLSA does not excuse a higher State/municipal minimum wage, a lower maximum workweek or a stricter child-labour standard: apply the more protective standard of the place where the work is performed]] | from 2026-01-01 |  | S1 |  |
| CA oman rule | [[FACT:multi.ca.oman.rule=Oman v. Delta Air Lines, Cal. S. Ct. S248726 (2020-06-29), Lab. Code 204 and 226: do not reach pay periods in which the employee works in CA only episodically and for less than a day at a time, unless the employee works primarily in CA in that period, or works primarily in no State and has the CA base of operations. Minimum-wage reach left undecided.]] | from 2020-06-29 | employer pay timing and pay statement | S2 | STATUS: in force (final answer to certified question). |

⚠️ RESEARCH-GAP (non-blocking): Paid sick leave multistate scope: not established by the research. Source that would close it: Per-State PSL statutes/regulations and agency FAQs (State annexes).

⚠️ RESEARCH-GAP (non-blocking): Payslip reach other states: not established by the research. Source that would close it: Per-State pay-statement statute reach (State annexes) or agency guidance.

⚠️ RESEARCH-GAP (non-blocking): CA minimum wage nonresident reach: not established by the research. Source that would close it: A later CA appellate ruling or DLSE guidance on minimum-wage reach.

## MULTI.2 Income tax withholding

General rule: [[FACT:multi.pit.sourcing.general=No general federal rule: each State taxes residents on all wages (credit at assessment for tax paid to the work State) and nonresidents on wages for services performed in the State; federal limits only for transport workers and military spouses. 4 U.S.C. 114 is retirement income only, not wages.]]. Everywhere without a convenience rule: [[FACT:multi.convenience.default=Everywhere else wages follow the place of physical performance]]. Local taxes sit outside State reciprocity (State annexes). The federal Mobile Workforce bills are drafts and are not modelled.

**Residents working in another State: withholding rule and credit level**

| State | Withholding rule | Credit for other-State tax operates at | Effective | Source |
|---|---|---|---|---|
| AR | — | [[FACT:multi.resident_credit.ar.level=assessment]] | from 2021-01-01 | S3 |
| AZ | — | [[FACT:multi.resident_credit.az.level=assessment]] | from 2026-01-01 | S4 |
| CO | [[FACT:multi.resident_out_of_state.co.withholding_rule=Withhold CO on all wages except wages for services in another State that itself requires withholding]] | — | from 2026-01-01 | S5 |
| CT | [[FACT:multi.resident_out_of_state.ct.withholding_rule=All wages subject; where the employer must withhold for the other jurisdiction, CT tax is prorated and only the excess remitted]] | — | from 2026-01-01 | S6 |
| DC | — | [[FACT:multi.resident_credit.dc.level=assessment]] | from 2026-01-01 | S7 |
| GA | [[FACT:multi.resident_out_of_state.ga.withholding_rule=No GA withholding if the other State requires withholding; otherwise withhold GA]] | — | from 2026-01-01 | S8 |
| IL | [[FACT:multi.resident_out_of_state.il.withholding_rule=IL resident working entirely in another State whose compensation is subject to that State's withholding: no IL withholding (credit on the return)]] | — | from 2026-02-01 | S9 |
| KS | [[FACT:multi.resident_out_of_state.ks.withholding_rule=KS tax on total wages less the other State's required withholding (example 250 - 130 = 120); zero if the other State's withholding is higher]] | — | from 2024-07-01 | S10 |
| LA | [[FACT:multi.resident_out_of_state.la.withholding_rule=LA residents working in another State may be subject to LA withholding if those wages are not subject to withholding there]] | — | from 2026-01-01 | S11 |
| MA | [[FACT:multi.resident_out_of_state.ma.withholding_rule=MA amount minus the other jurisdiction's amount (credit method, 830 CMR 62B.2.1(9)(b)); employer without MA office may withhold for MA residents as a convenience]] | — | from 2026-01-01 | S12 |
| ME | — | [[FACT:multi.resident_credit.me.level=assessment]] | from 2026-01-01 | S13 |
| MS | [[FACT:multi.resident_out_of_state.ms.withholding_rule=Withhold MS on total wages except to the extent withheld for another State; commuter to a no-income-tax State is withheld MS on total wages (credit at assessment). Corrects MULTI.md 2.2, which listed MS as credit-only.]] | [[FACT:multi.resident_credit.ms.level=assessment]] | from 2026-01-01 | S14, S15 |
| NC | [[FACT:multi.resident_out_of_state.nc.withholding_rule=Withhold on all wages wherever earned, except no NC withholding on wages for services in a State that requires the employer to withhold]] | — | from 2026-01-01 | S16 |
| NY | [[FACT:multi.resident_out_of_state.ny.withholding_rule=Withhold NYS tax for NY residents even if wages are earned outside NY]] | — | from 2026-01-01 | S17 |
| OH | [[FACT:multi.resident_out_of_state.oh.withholding_rule=Every employer with an office or transacting business in Ohio withholds on residents (resident credit IT RC at assessment)]] | [[FACT:multi.resident_credit.oh.level=assessment]] | from 2025-01-01; from 2026-10-29 | S18, S19 |
| OK | [[FACT:multi.resident_out_of_state.ok.withholding_rule=Residents are withheld on services within or without Oklahoma (68 O.S. 2385.1 employee definition)]] | [[FACT:multi.resident_credit.ok.level=assessment]] | from 2023-07-01; from 2025-01-01 | S20, S21 |
| RI | — | [[FACT:multi.resident_credit.ri.level=assessment]] | from 2025-01-01 | S22 |
| SC | [[FACT:multi.resident_out_of_state.sc.withholding_rule=Withhold for the other State; if that State has no income tax, withhold 100% SC (12-8-520(C)(1))]] | [[FACT:multi.resident_credit.sc.level=assessment]] | from 2026-01-01 | S23, S24 |
| VT | [[FACT:multi.resident_out_of_state.vt.withholding_rule=Compute on the full payment, then reduce by tax withheld for the State where services were performed]] | — | from 2026-01-01 | S25 |
| WI | [[FACT:multi.resident_out_of_state.wi.withholding_rule=Residents working outside WI: withholding on all wages; Minnesota special arrangement - no WI withholding if MN withholds]] | — | from 2026-01-01 | S26 |

**Reciprocity: partner States and exemption certificate**

| State | Partners | One-way rule | Non-resident exemption | Certificate | Effective | Source |
|---|---|---|---|---|---|---|
| AR | [[FACT:multi.reciprocity.ar.partners=none (zero hits for reciprocity in the AR instructions)]] | — | — | — | from 2025-01-01 | S27 |
| AZ | — | [[FACT:multi.reciprocity.az.unilateral=AZ exempts residents of CA, IN, OR, VA on Form WEC (they can claim the AZ credit); one-way - an AZ resident working in CA is withheld by CA]] | — | — | from 2026-01-01 | S28 |
| CT | [[FACT:multi.reciprocity.ct.partners=none]] | — | — | — | from 2026-01-01 | S6 |
| DC | [[FACT:multi.reciprocity.dc.partners=MD, VA (from the partner side; DC taxes no nonresident at all)]] | — | [[FACT:multi.reciprocity.dc.nonresident_exempt=D.C. Code 1-206.02(a)(5): DC may not tax any nonresident's personal income; DC withholding stops for ANY nonresident (D-4A: domicile outside DC and under 183 days)]] | [[FACT:multi.reciprocity.dc.certificate=D-4A]] | from 2026-01-01 | S29, S30 |
| DE | [[FACT:multi.reciprocity.de.partners=none]] | — | — | — | from 2026-01-01 | S31 |
| GA | [[FACT:multi.reciprocity.ga.partners=none]] | — | — | — | from 2026-01-01 | S32 |
| IA | [[FACT:multi.reciprocity.ia.partners=IL]] | — | — | [[FACT:multi.reciprocity.ia.certificate=IA 44-016 (IL resident in IA); IL-W-5-NR (IA resident in IL)]] | from 2026-01-01 | S33 |
| IL | [[FACT:multi.reciprocity.il.partners=IA, KY, MI, WI]] | — | — | [[FACT:multi.reciprocity.il.certificate=IL-W-5-NR]] | from 2026-02-01 | S34, S9 |
| IN | [[FACT:multi.reciprocity.in.partners=KY, MI, OH, PA, WI (county tax still withheld)]] | — | — | [[FACT:multi.reciprocity.in.certificate=WH-47]] | from 2026-01-01 | S35 |
| KY | [[FACT:multi.reciprocity.ky.partners=IL, IN, MI, OH (unless 20% S-corp shareholder-employee), VA (daily commuters only), WV, WI]] | — | — | [[FACT:multi.reciprocity.ky.certificate=42A809]] | from 2026-01-01 | S36 |
| MD | [[FACT:multi.reciprocity.md.partners=DC, PA, VA, WV (not for abode in MD > 6 months and 183+ days, except WV)]] | — | — | [[FACT:multi.reciprocity.md.certificate=MW507]] | from 2026-01-01 | S37 |
| ME | [[FACT:multi.reciprocity.me.partners=none in force (agreements authorised by statute, none identified)]] | — | — | — | from 2026-01-01 | S38 |
| MI | [[FACT:multi.reciprocity.mi.partners=IL, IN, KY, MN, OH, WI]] | — | — | [[FACT:multi.reciprocity.mi.certificate=per MI Guide 446 (form not named in the row)]] | from 2026-01-01 | S39 |
| MN | [[FACT:multi.reciprocity.mn.partners=MI, ND (employee returns home at least monthly)]] | — | — | [[FACT:multi.reciprocity.mn.certificate=MWR (yearly; copies to MN DOR by Mar 31)]] | from 2026-01-01 | S40 |
| MO | [[FACT:multi.reciprocity.mo.partners=none]] | — | — | — | 2026-01-01 to 2026-12-31 | S41 |
| MT | [[FACT:multi.reciprocity.mt.partners=ND]] | — | — | [[FACT:multi.reciprocity.mt.certificate=MW-4 (annual renewal)]] | from 2026-01-01 | S42 |
| NC | [[FACT:multi.reciprocity.nc.partners=none]] | — | — | — | from 2026-01-01 | S16 |
| ND | [[FACT:multi.reciprocity.nd.partners=MN, MT]] | — | — | [[FACT:multi.reciprocity.nd.certificate=NDW-R (yearly, by Feb 28 or within 30 days)]] | from 2026-01-01 | S43 |
| NJ | [[FACT:multi.reciprocity.nj.partners=PA (compensation only)]] | — | — | [[FACT:multi.reciprocity.nj.certificate=NJ-165 (PA resident in NJ); REV-419EX (NJ resident with PA employer)]] | from 2026-01-01 | S44 |
| OH | [[FACT:multi.reciprocity.oh.partners=IN, KY, MI, PA, WV]] | — | — | [[FACT:multi.reciprocity.oh.certificate=IT 4 (combined certificate)]] | from 2026-01-01 | S45 |
| PA | [[FACT:multi.reciprocity.pa.partners=IN, MD, NJ, OH, VA, WV]] | — | — | [[FACT:multi.reciprocity.pa.certificate=REV-419]] | from 2026-01-01 | S46 |
| VA | [[FACT:multi.reciprocity.va.partners=DC, KY (daily commuters), MD, PA, WV]] | — | — | [[FACT:multi.reciprocity.va.certificate=VA certificate (not named in the row; VA annex)]] | from 2026-01-01 | S47 |
| VT | [[FACT:multi.reciprocity.vt.partners=none (four official withholding texts, none lists one)]] | — | — | — | from 2026-01-01 | S48 |
| WI | [[FACT:multi.reciprocity.wi.partners=IL, IN, KY, MI]] | — | — | [[FACT:multi.reciprocity.wi.certificate=W-220]] | from 2026-01-01 | S49 |
| WV | [[FACT:multi.reciprocity.wv.partners=KY, MD, OH, PA, VA]] | — | — | [[FACT:multi.reciprocity.wv.certificate=WV/IT-104]] | from 2026-01-01 | S50 |

**Non-resident thresholds before work-State withholding starts**

| State | Days | Amount | Share | Rule | Allocation | Employer start | Catch-up | Other | Effective | Source |
|---|---|---|---|---|---|---|---|---|---|---|
| AL | [[FACT:multi.nonresident.al.threshold_days=30]] days | — | — | — | — | — | — | — | from 2026-01-01 | S51 |
| AR | — | — | — | — | [[FACT:multi.nonresident.ar.allocation_rule=No threshold: apportioned by AR working days (HB1116 of 2025, 15 days / 2,500, died)]] | — | — | — | from 2026-01-01 | S52 |
| AZ | [[FACT:multi.nonresident.az.threshold_days=60]] days | — | — | — | — | — | — | — | from 2026-01-01 | S28 |
| CA | — | — | — | — | [[FACT:multi.nonresident.ca.allocation_rule=No threshold: working-day ratio from day 1 (commission pay: volume ratio)]] | — | — | — | from 2026-01-01 | S53 |
| CO | — | — | — | — | [[FACT:multi.nonresident.co.allocation_rule=No threshold: apportioned by days worked in CO (a day counts if majority of working time is in CO)]] | — | — | — | from 2026-01-01 | S5 |
| CT | [[FACT:multi.nonresident.ct.threshold_days=15]] days | — | — | — | — | — | — | — | from 2026-01-01 | S6 |
| GA | — | USD [[FACT:multi.nonresident.ga.threshold_amount=5,000]] | [[FACT:multi.nonresident.ga.threshold_share=5]] % | — | — | — | — | — | from 2026-01-01 | S8 |
| HI | [[FACT:multi.nonresident.hi.threshold_days=60]] days | — | — | — | — | — | — | — | from 2026-01-01 | S54 |
| ID | — | USD [[FACT:multi.nonresident.id.threshold_amount=1,000]] | — | — | — | — | — | — | from 2026-04-12 | S55 |
| IL | [[FACT:multi.nonresident.il.threshold_days=30]] days | — | — | — | — | — | — | — | from 2026-01-01 | S56 |
| LA | [[FACT:multi.nonresident.la.threshold_days=30]] days | — | — | — | — | [[FACT:multi.nonresident.la.employer_start_rule=Begin withholding and report on Form L-1 beginning in the period in which the 31st day fell]] | ⚠️ RESEARCH-GAP (non-blocking): not established. Would close it: The codified R.S. 47:112.2(A) text, or an LDR RIB/FAQ on the mobile workforce exemption. | — | from 2026-01-01; from 2026-03-20 | S57, S58 |
| ME | [[FACT:multi.nonresident.me.threshold_days=12]] days | USD [[FACT:multi.nonresident.me.threshold_amount=3,000]] | — | — | — | — | — | — | from 2026-01-01 | S59 |
| MN | — | USD [[FACT:multi.nonresident.mn.threshold_amount=15,300]] | — | — | — | — | — | — | 2026-01-01 to 2026-12-31 | S60 |
| MS | — | — | — | [[FACT:multi.nonresident.ms.threshold_rule=Day 1 by earnings ratio, except no withholding when annual MS earnings will be below the standard deduction for the filing status]] | [[FACT:multi.nonresident.ms.allocation_rule=Earnings ratio; principal place of employment in MS -> total wages unless the other State requires withholding]] | — | — | — | from 2025-07-01; from 2026-01-01 | S61, S15 |
| MT | [[FACT:multi.nonresident.mt.threshold_days=30]] days | — | — | — | — | — | — | — | from 2026-01-01 | S62 |
| ND | — | — | — | [[FACT:multi.nonresident.nd.threshold_rule=Mobile workforce exclusion (57-38-59.3): present 20 days or fewer, no other ND income, home State reciprocal exclusion or no income tax; not athletes, entertainers, persons of prominence, construction workers, key employees]] | — | — | — | — | from 2026-01-01 | S63 |
| NE | [[FACT:multi.nonresident.ne.threshold_days=7]] days | — | — | — | — | — | — | — | from 2025-01-01 | S64 |
| NM | [[FACT:multi.nonresident.nm.threshold_days=15]] days | — | — | — | — | — | — | — | from 2026-01-01 | S65 |
| NY | — | — | — | — | [[FACT:multi.nonresident.ny.allocation_rule=No threshold: NY working days / total working days with the convenience test]] | — | — | — | from 2006-05-15 | S66 |
| OK | — | USD [[FACT:multi.nonresident.ok.threshold_amount=300]] | — | — | — | — | — | — | from 2023-07-01 | S21 |
| SC | — | — | — | — | — | — | — | ⚠️ RESEARCH-GAP (non-blocking): not established. Would close it: SC Code 12-8-520(A) reconciled with the SC DOR withholding guide (WH-1603F / WH105) |  |  |
| UT | [[FACT:multi.nonresident.ut.threshold_days=20]] days | — | — | — | — | — | — | — | from 2026-01-01 | S67 |
| VT | [[FACT:multi.nonresident.vt.threshold_days=30]] days | — | — | — | — | — | — | — | from 2026-01-01 | S48 |
| WI | — | USD [[FACT:multi.nonresident.wi.threshold_amount=1,500]] | — | — | — | — | — | — | from 2026-01-01 | S26 |
| WV | [[FACT:multi.nonresident.wv.threshold_days=30]] days | — | — | — | — | — | — | — | from 2026-01-01 | S50 |

**Convenience-of-the-employer rules**

| State | Rule | Litigation | Effective | Source |
|---|---|---|---|---|
| AR | [[FACT:multi.convenience.ar.rule=Not a convenience State: Act 1019 of 2021 (SB 484), in force from TY2021 - a nonresident works in AR only when physically located in AR]] | — | from 2021-01-01 | S3 |
| CT | [[FACT:multi.convenience.ct.rule=From tax years beginning 2019-01-01 CT applies the resident State's convenience test to nonresidents working for a CT employer]] | — | from 2019-01-01 | S68 |
| DE | [[FACT:multi.convenience.de.rule=30 Del. C. 1124(b)(1): compensation is DE-source if attributable to employment in DE and not required to be performed elsewhere; working from home does not qualify for the PIT-SCW exclusion]] | — | from 2026-01-01 | S69 |
| NE | [[FACT:multi.convenience.ne.rule=From 2025: services performed outside NE for the nonresident's convenience are NE-sourced (77-2733(8)(c))]] | — | from 2025-01-01 | S64 |
| NJ | [[FACT:multi.convenience.nj.rule=From 2023 NJ applies the convenience rule against residents of States that apply one (DE, NE, NY; CT by reciprocal law); PA residents excluded by the reciprocal agreement]] | — | from 2023-01-01 | S70 |
| NY | [[FACT:multi.convenience.ny.rule=20 NYCRR 132.18(a): nonresident allocates by NY working days / total working days; days outside NY count only if worked of NECESSITY; home-office days are NY days unless the home is a bona fide employer office]] | ⚠️ RESEARCH-GAP (non-blocking): not established. Would close it: NY DTF / Tax Appeals Tribunal decisions list for 2026. | from 2006-05-15 | S66 |
| PA | [[FACT:multi.convenience.pa.rule=61 Pa. Code 109.8: same necessity test as NY; PA reciprocal agreements prevail]] | — | from 1999-12-11 | S71 |

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Transport motor carrier | [[FACT:multi.transport.motor_carrier=Employee with regularly assigned duties in 2+ States: taxable ONLY by the residence State/subdivision (49 U.S.C. 14503)]] | from 1996-01-01 | withholding | S72 |  |
| Transport rail | [[FACT:multi.transport.rail=Residence State/subdivision only (49 U.S.C. 11502)]] | from 2026-01-01 | withholding | S73 |  |
| Transport air carrier | [[FACT:multi.transport.air_carrier=Residence State plus the State where more than 50% of carrier pay is earned (scheduled flight time) (49 U.S.C. 40116(f))]] | from 2018-10-05 | withholding | S74 |  |
| Transport air carrier share threshold | [[FACT:multi.transport.air_carrier.share_threshold=50]] % | from 2018-10-05 | withholding | S74 |  |
| Transport seamen | [[FACT:multi.transport.seamen=Seamen's wages may not be withheld for State/local tax; multi-State vessel crew and pilots taxable only by the residence State (46 U.S.C. 11108)]] | from 2010-10-15 | withholding | S75 |  |
| PIT sourcing general | [[FACT:multi.pit.sourcing.general=No general federal rule: each State taxes residents on all wages (credit at assessment for tax paid to the work State) and nonresidents on wages for services performed in the State; federal limits only for transport workers and military spouses. 4 U.S.C. 114 is retirement income only, not wages.]] | from 2026-01-01 |  | S76 |  |
| Convenience default | [[FACT:multi.convenience.default=Everywhere else wages follow the place of physical performance]] | from 2026-01-01 |  | S76 |  |
| Military spouse rule | [[FACT:multi.military_spouse.rule=Spouse's service income not sourced to the duty State; election of the servicemember's residence, the spouse's residence or the permanent duty station (50 U.S.C. 4001); payroll effect: stop work-State withholding on the State certificate]] | 2018-12-31 to 2025-12-31 | withholding | S77 |  |

## MULTI.3 Social insurance: unemployment, disability, paid leave and payroll levies

UI covers the whole service with one employer in one State. Employee UI contributions exist only in the States listed in [[FACT:multi.sui.employee_contribution_states=AK, NJ, PA (only three States levy employee UI contributions; take 2026 rates from the State annexes)]]. The FUTA base counts wages across all States.

**Other-State wage-base credit for UI (wages reported to another State count toward this State's base)**

| State | Credit | Effective | Source |
|---|---|---|---|
| AK | [[FACT:multi.sui.other_state_wage_credit.ak=True]] | from 2026-01-01 | S78 |
| AL | [[FACT:multi.sui.other_state_wage_credit.al=True]] | from 2026-01-01 | S79 |
| AR | ⚠️ RESEARCH-GAP (non-blocking): not established. Would close it: the Arkansas UI handbook page that states the transfer-credit clause, registered as a source |  |  |
| AZ | ⚠️ RESEARCH-GAP (non-blocking): not established. Would close it: The AZ UI taxable-wage statute/definition (State annex), or the DOL "Significant Provisions of State UI Laws" 2026 line for AZ. |  |  |
| CA | [[FACT:multi.sui.other_state_wage_credit.ca=True]] | from 2026-01-01 | S53 |
| CO | ⚠️ RESEARCH-GAP (non-blocking): not established. Would close it: C.R.S. 8-76-102 (chargeable wages) or the CDLE Employer Handbook |  |  |
| CT | [[FACT:multi.sui.other_state_wage_credit.ct=True]] | from 2025-01-01 | S80 |
| DC | ⚠️ RESEARCH-GAP (non-blocking): not established. Would close it: 7 DCMR chapter 3 or the DOES UI Employer Handbook (51-103(e)(6) as read is silent) |  |  |
| DE | [[FACT:multi.sui.other_state_wage_credit.de=True]] | 2026-01-01 to 2026-12-31 | S81 |
| FL | [[FACT:multi.sui.other_state_wage_credit.fl=True]] | from 2026-01-01 | S82 |
| GA | ⚠️ RESEARCH-GAP (non-blocking): not established. Would close it: The GA UI taxable-wage statute/definition (State annex), or the DOL "Significant Provisions of State UI Laws" 2026 line for GA. |  |  |
| HI | [[FACT:multi.sui.other_state_wage_credit.hi=True]] | from 2026-01-01 | S83 |
| IA | [[FACT:multi.sui.other_state_wage_credit.ia=False]] | from 2025-02-26 | S84 |
| ID | [[FACT:multi.sui.other_state_wage_credit.id=conditional: only if tax was paid on them to that State (72-1349(1))]] | from 2025-11-05 | S85 |
| IL | ⚠️ RESEARCH-GAP (non-blocking): not established. Would close it: The IL UI taxable-wage statute/definition (State annex), or the DOL "Significant Provisions of State UI Laws" 2026 line for IL. |  |  |
| IN | ⚠️ RESEARCH-GAP (non-blocking): not established. Would close it: The IN UI taxable-wage statute/definition (State annex), or the DOL "Significant Provisions of State UI Laws" 2026 line for IN. |  |  |
| KS | [[FACT:multi.sui.other_state_wage_credit.ks=True]] | from 2026-01-01 | S86 |
| KY | [[FACT:multi.sui.other_state_wage_credit.ky=True]] | from 2022-03-24 | S87 |
| LA | ⚠️ RESEARCH-GAP (non-blocking): not established. Would close it: R.S. 23:1536 |  |  |
| MA | ⚠️ RESEARCH-GAP (non-blocking): not established. Would close it: The MA UI taxable-wage statute/definition (State annex), or the DOL "Significant Provisions of State UI Laws" 2026 line for MA. |  |  |
| MD | ⚠️ RESEARCH-GAP (non-blocking): not established. Would close it: LE Title 8 taxable-wage definition |  |  |
| ME | [[FACT:multi.sui.other_state_wage_credit.me=True]] | from 2026-01-01 | S88 |
| MI | [[FACT:multi.sui.other_state_wage_credit.mi=True]] | from 2016-01-01 | S89 |
| MN | ⚠️ RESEARCH-GAP (non-blocking): not established. Would close it: The MN UI taxable-wage statute/definition (State annex), or the DOL "Significant Provisions of State UI Laws" 2026 line for MN. |  |  |
| MO | ⚠️ RESEARCH-GAP (non-blocking): not established. Would close it: In-force RSMo 288.036 or the DES MODES-4-5 instructions |  |  |
| MS | [[FACT:multi.sui.other_state_wage_credit.ms=True]] | from 2011-01-01 | S90 |
| MT | [[FACT:multi.sui.other_state_wage_credit.mt=False]] | from 2025-07-01 | S91 |
| NC | [[FACT:multi.sui.other_state_wage_credit.nc=True]] | from 2026-01-01 | S92 |
| ND | [[FACT:multi.sui.other_state_wage_credit.nd=True]] | from 2026-01-01 | S93 |
| NE | [[FACT:multi.sui.other_state_wage_credit.ne=True]] | from 2025-09-11 | S94 |
| NH | [[FACT:multi.sui.other_state_wage_credit.nh=True]] | from 2026-01-01 | S95 |
| NJ | ⚠️ RESEARCH-GAP (non-blocking): not established. Would close it: The NJ UI taxable-wage statute/definition (State annex), or the DOL "Significant Provisions of State UI Laws" 2026 line for NJ. |  |  |
| NM | ⚠️ RESEARCH-GAP (non-blocking): not established. Would close it: NMSA 51-1-11 and 51-1-42 or 11.3.300 NMAC |  |  |
| NV | [[FACT:multi.sui.other_state_wage_credit.nv=True]] | from 2026-01-01 | S96 |
| NY | ⚠️ RESEARCH-GAP (non-blocking): not established. Would close it: The NY UI taxable-wage statute/definition (State annex), or the DOL "Significant Provisions of State UI Laws" 2026 line for NY. |  |  |
| OH | ⚠️ RESEARCH-GAP (non-blocking): not established. Would close it: The OH UI taxable-wage statute/definition (State annex), or the DOL "Significant Provisions of State UI Laws" 2026 line for OH. |  |  |
| OK | [[FACT:multi.sui.other_state_wage_credit.ok=True]] | from 2025-11-01 | S97 |
| OR | [[FACT:multi.sui.other_state_wage_credit.or=True]] | from 2026-01-01 | S98 |
| PA | ⚠️ RESEARCH-GAP (non-blocking): not established. Would close it: The PA UI taxable-wage statute/definition (State annex), or the DOL "Significant Provisions of State UI Laws" 2026 line for PA. |  |  |
| RI | [[FACT:multi.sui.other_state_wage_credit.ri=True]] | from 2026-01-01 | S99 |
| SC | [[FACT:multi.sui.other_state_wage_credit.sc=True]] | from 2015-01-01 | S100 |
| SD | [[FACT:multi.sui.other_state_wage_credit.sd=True]] | from 2026-01-01 | S101 |
| TN | ⚠️ RESEARCH-GAP (non-blocking): not established. Would close it: The TN UI taxable-wage statute/definition (State annex), or the DOL "Significant Provisions of State UI Laws" 2026 line for TN. |  |  |
| TX | ⚠️ RESEARCH-GAP (non-blocking): not established. Would close it: The TX UI taxable-wage statute/definition (State annex), or the DOL "Significant Provisions of State UI Laws" 2026 line for TX. |  |  |
| UT | ⚠️ RESEARCH-GAP (non-blocking): not established. Would close it: Utah Code 35A-4-303 current text or the DWS Employer Handbook, Contributions chapter |  |  |
| VA | ⚠️ RESEARCH-GAP (non-blocking): not established. Would close it: The VA UI taxable-wage statute/definition (State annex), or the DOL "Significant Provisions of State UI Laws" 2026 line for VA. |  |  |
| VT | [[FACT:multi.sui.other_state_wage_credit.vt=True]] | from 2012-01-01 | S102 |
| WA | ⚠️ RESEARCH-GAP (non-blocking): not established. Would close it: The WA UI taxable-wage statute/definition (State annex), or the DOL "Significant Provisions of State UI Laws" 2026 line for WA. |  |  |
| WI | ⚠️ RESEARCH-GAP (non-blocking): not established. Would close it: The WI UI taxable-wage statute/definition (State annex), or the DOL "Significant Provisions of State UI Laws" 2026 line for WI. |  |  |
| WV | [[FACT:multi.sui.other_state_wage_credit.wv=True]] | from 2024-07-01 | S103 |
| WY | [[FACT:multi.sui.other_state_wage_credit.wy=True]] | from 2026-05-08 | S104 |

**PFML / SDI / TDI coverage test**

| State | Coverage test | Effective | Source |
|---|---|---|---|
| CA | ⚠️ RESEARCH-GAP (non-blocking): not established. Would close it: The CA programme coverage definition (statute or agency rule); until then key the premium to sui_state. |  |  |
| CO | ⚠️ RESEARCH-GAP (non-blocking): not established. Would close it: The CO programme coverage definition (statute or agency rule); until then key the premium to sui_state. |  |  |
| CT | [[FACT:multi.pfml.coverage_test.ct=Follows UI localization: employees for whom CT UI and payroll taxes are paid are working in CT]] | from 2026-01-01 | S105 |
| DC | [[FACT:multi.pfml.coverage_test.dc=More than 50% of work time in DC, or DC-based with substantial DC time and not more than 50% elsewhere; not by residence]] | from 2026-01-01 | S106 |
| DE | [[FACT:multi.pfml.coverage_test.de=Follows the primary DE worksite (3701(6)a), not UI localization]] | from 2025-01-01 | S107 |
| HI | ⚠️ RESEARCH-GAP (non-blocking): not established. Would close it: The HI programme coverage definition (statute or agency rule); until then key the premium to sui_state. |  |  |
| MA | ⚠️ RESEARCH-GAP (non-blocking): not established. Would close it: The MA programme coverage definition (statute or agency rule); until then key the premium to sui_state. |  |  |
| MD | [[FACT:multi.pfml.coverage_test.md=FAMLI covers employees in positions localized in MD (LE 8-202 UI localization); contributions start 2027-01-01 (US-MDS5-014)]] | from 2026-01-01 | S108 |
| ME | [[FACT:multi.pfml.coverage_test.me=Follows the Maine UI localization test (FAQ 6)]] | from 2025-01-01 | S109 |
| MN | ⚠️ RESEARCH-GAP (non-blocking): not established. Would close it: The MN programme coverage definition (statute or agency rule); until then key the premium to sui_state. |  |  |
| NJ | ⚠️ RESEARCH-GAP (non-blocking): not established. Would close it: The NJ programme coverage definition (statute or agency rule); until then key the premium to sui_state. |  |  |
| NY | ⚠️ RESEARCH-GAP (non-blocking): not established. Would close it: The NY programme coverage definition (statute or agency rule); until then key the premium to sui_state. |  |  |
| OR | [[FACT:multi.pfml.coverage_test.or=Follows UI localization (ORS 657B.175); employer size counts out-of-state employees too (US-ORS5-013)]] | from 2023-01-01 | S110 |
| RI | [[FACT:multi.pfml.coverage_test.ri=TDI follows the UI localization test (28-39-2 uses the chapter 42 definition)]] | from 2026-01-01 | S111 |
| VT | ⚠️ RESEARCH-GAP (non-blocking): not established. Would close it: The VT programme coverage definition (statute or agency rule); until then key the premium to sui_state. |  |  |
| WA | [[FACT:multi.pfml.coverage_test.wa=Follows the UI localization test (RCW 50A.05.010(8))]] | 2026-01-01 to 2027-06-30 | S112 |
| DEFAULT | [[FACT:multi.pfml.coverage_test.default=Key the PFML/SDI premium State to sui_state unless the State annex proves otherwise (WA, CT, ME, OR, MD, RI proven; DC and DE differ)]] | 2026-01-01 to 2027-06-30 | S112 |

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| SUI localization test | [[FACT:multi.sui.localization_test=One State covers the entire service with one employer, in order: (1) localized (entirely in the State, or out-of-state service incidental: temporary, transitory, isolated); (2) else some service in the base-of-operations State; (3) else some service in the State of direction or control; (4) else some service in the State of residence]] | from 2026-01-01 | employer UI reporting | S113 | DOL OUI restatement; same test in the 2023 DOL Comparison and UIPL 20-04; statutory instance Fla. Stat. 443.1216. |
| SUI localization telecommuting | [[FACT:multi.sui.localization.telecommuting=UIPL 20-04 (2004, continuing) reissues the UIPL 291 interpretation with telecommuting examples]] | from 2004-05-10 | employer UI reporting | S114 |  |
| SUI reciprocal coverage election | [[FACT:multi.sui.reciprocal_coverage_election=Where no test resolves the case, employer, employee and States may elect coverage of all service in one State (performance, residence or place of business); CA CUIC 602/603]] | from 2026-01-01 | employer UI reporting | S53 |  |
| FUTA wage base scope | [[FACT:multi.futa.wage_base.scope=FUTA 7,000 counts remuneration paid by the employer in the calendar year across all States: one base per employer, not per State; successor carry-over]] | from 2026-01-01 |  | S115 |  |
| SUI employee contribution states | [[FACT:multi.sui.employee_contribution_states=AK, NJ, PA (only three States levy employee UI contributions; take 2026 rates from the State annexes)]] | from 2023-01-01 |  | S116 |  |

## MULTI.4 Pay statement

Default: the pay-statement statute of the work-location State ([[FACT:multi.payslip.reach.default=Default: the pay-statement statute of the work-location State (no other State reach rule researched); payslip in English (US-OWN-006)]]). California applies its own rule under the ruling recorded below.

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| CA ward rule | [[FACT:multi.ca.ward.rule=Ward v. United Airlines, Cal. S. Ct. S248702 (2020-06-29), Lab. Code 226: applies if the PRINCIPAL place of work is in CA (majority of working time); with no majority State, where CA is the base of work operations and some work is done in CA. Employer location, residence, place of pay receipt, taxes paid and a CBA are irrelevant.]] | from 2020-06-29 | employer pay-statement output | S117 | STATUS: in force. |
| Payslip reach default | [[FACT:multi.payslip.reach.default=Default: the pay-statement statute of the work-location State (no other State reach rule researched); payslip in English (US-OWN-006)]] | from 2020-06-29 |  | S117 |  |

## MULTI.5 Statutory reporting

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| W-2 states per form | [[FACT:multi.w2.states_per_form=2]] count | from 2026-01-01 | employer reporting | S118 | Boxes 15-20 carry up to TWO States and TWO localities; for more, a second W-2 repeating boxes a-f, never duplicating federal data on Copy A; W-3 box 15 = X when more than one State. |
| Newhire designated state | [[FACT:multi.newhire.designated_state=A multistate employer reporting electronically may send all new-hire reports to ONE designated State in which it has employees, after notifying HHS in writing]] | from 2026-01-01 | employer reporting | S119 |  |
| UI wage report routing | [[FACT:multi.ui_wage_report.routing=UI quarterly wage report to the sui_state only (localization); State income-tax withholding returns to every State where withholding applies]] | from 2026-01-01 | employer reporting | S113 |  |

⚠️ RESEARCH-GAP (non-blocking): Newhire multistate registration channel: not established by the research. Source that would close it: the ACF multistate employer registration page

## MULTI.9 Deductions and garnishments

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| IWO governing law | [[FACT:multi.iwo.governing_law=Interstate IWO: apply the income-withholding law of the State of the obligor's PRINCIPAL PLACE OF EMPLOYMENT for the employer fee, the maximum withheld, timing, priority among obligees and terms not in the order]] | from 2026-01-01 | employer withholding | S120 |  |
| IWO remittance business days | [[FACT:multi.iwo.remittance_business_days=7]] days | from 2026-01-01 | employer withholding | S120 | Remit to the SDU within [[FACT:multi.iwo.remittance_business_days=7]] business days. |

## MULTI.13 Live legal change

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Mobile workforce bill senate | [[FACT:multi.mobile_workforce_bill.senate=S. 1443 (introduced 2025-04-10, Senate Finance): DRAFT, NOT ENACTED - do not model]] | from 2026-01-01 | withholding and tax (if enacted) | S121 |  |
| Mobile workforce bill house | [[FACT:multi.mobile_workforce_bill.house=H.R. 10271 (introduced 2026-09-03, House Judiciary): DRAFT, NOT ENACTED - do not model]] | from 2026-01-01 | withholding and tax (if enacted) | S122 |  |
| Reciprocity IL partners | [[FACT:multi.reciprocity.il.partners=IA,KY,MI,WI]] | 2026-01-01 to 2026-01-31 |  | S56 | Bilateral; confirmed on both sides (MULTI 2.3). |
| Military spouse rule | [[FACT:multi.military_spouse.rule=election of servicemember residence, spouse residence or duty station (50 USC 4001)]] | from 2026-01-01 |  | S77 |  |

## MULTI.15 Special populations

Transport workers, seamen and military spouses follow the federal carve-outs in MULTI.2. All other special populations follow the State annexes of the States the routing selects.

## MULTI.16 Language

No multistate language rule: the payslip is in English and its content follows the work-location State.

## MULTI.S Sources

| Ref | Instrument | Article / section | Authority |
|---|---|---|---|
| S1 | 29 U.S.C. 218(a) FLSA relation to other laws (US Code 2024 ed.) | 218(a) | US Congress / GPO |
| S2 | Oman v. Delta Air Lines, Inc. (Cal. Supreme Court, S248726, 2020-06-29), 9 Cal.5th 762: reach of Lab. Code 204 and 226 to multistate workers; Sullivan v. … | Part II.A; answers (1)-(3) | Supreme Court of California |
| S3 | Arkansas Act 1019 of 2021 (SB 484): allocation of nonresident income by physical location | Sec. 2 (26-51-202(c)), Sec. 3 (26-51-504(a)(1)), Sec. 4 (26-51-902(5)), Sec. 5-6 | Arkansas General Assembly |
| S4 | A.R.S. 43-1096 credit for income taxes paid by nonresident | A.R.S. 43-1096 | Arizona Legislature |
| S5 | Colorado Wage Withholding Tax Guide (Revised January 2026), full read | Part 2; Part 3 | Colorado Department of Revenue |
| S6 | DRS Informational Publication 2026(1) Connecticut Employer's Tax Guide (Circular CT) | Q5 (gross CT wages); 'Residents working outside CT' (proration among qualifying jurisdictions); '15-Day Rule for Nonresident Employees' p.8; CT-W4NA allocation | Connecticut Department of Revenue Services |
| S7 | D.C. Code 47-1806.04(a) resident credit for taxes paid to other states | 47-1806.04(a) | Council of the District of Columbia |
| S8 | GA DOR Employer's Withholding Tax Guide 2026: definitions, G-4, special payments | pp. 9-10, 14-17, 24-27 | Georgia Department of Revenue |
| S9 | IDOR Publication 130 (R-02/26) Who is Required to Withhold Illinois Income Tax: compensation paid in Illinois, exceptions, special categories | When is compensation paid in Illinois; Limited exceptions; When am I not required to withhold; Form IL-W-6 | Illinois Department of Revenue |
| S10 | KW-100 - residents working in other states; nonresidents | Specific Withholding Situations | Kansas Department of Revenue |
| S11 | Louisiana DOR Withholding page (Wayback copy) | Withholding | Louisiana Department of Revenue |
| S12 | 830 CMR 62B.2.1 Withholding of Taxes on Wages and Other Payments (local copy) | (4)(a)1, (8), (9)(a)-(b); page dated 06/05/2026 | Massachusetts Department of Revenue (Massachusetts Register) |
| S13 | 36 MRSA 5217-A credit for income tax paid to other jurisdictions | 36 MRSA 5217-A(1) | Maine Legislature |
| S14 | 35 Miss. Admin. Code Part III (Income and Franchise), Subpart 11 Withholding and Subpart 2 (gross income) | 35.III.11 Ch.02 (101 supplemental), Ch.03 (exclusions: agricultural, domestic, ministers), Ch.07 (101-102 no-liability certificate), Ch.09 … | Mississippi Department of Revenue (filed with Secretary of State) |
| S15 | MDOR Business Tax Frequently Asked Questions - Withholding Tax section | Withholding Tax; Filing Withholding Returns; Registration and Updating Account Information | Mississippi Department of Revenue |
| S16 | NC-30 2026 Income Tax Withholding Tables and Instructions for Employers, Section 5 | Sections 1, 4, 5 | North Carolina Department of Revenue |
| S17 | NY DTF Withholding tax requirements page (out-of-state employers, nonresidents) | Who you must withhold tax for | NY Department of Taxation and Finance |
| S18 | Ohio IT 1040 booklet TY2025 - IT RC (resident credit) and IT NRC (nonresident credit) instructions | Pages 35-40 (IT NRC), 40 (IT RC) | Ohio Department of Taxation |
| S19 | Ohio tax.ohio.gov Employer Withholding - Who Must Withhold (ORC 5747.06) | Who Must Withhold; exemptions | Ohio Department of Taxation |
| S20 | Oklahoma Form 511-TX (2025) Credit for Tax Paid to Another State | Who Qualifies / Who Does Not Qualify | Oklahoma Tax Commission |
| S21 | 68 O.S. 2385.1, 2385.2, 2385.3 Withholding - definitions, amount, remittance, statements, annual reconciliation | 68 O.S. 2385.1(b),(c),(e); 2385.2(A)-(C); 2385.3(A)-(D),(F),(G) (Laws 2023 c. 113) | Oklahoma Legislature (Oklahoma Statutes, Title 68) |
| S22 | 2025 RI-1040 Resident Instructions (Schedule II, credit for income taxes paid to another state) | Schedule II lines 23-29; RI-1040MU | RI Division of Taxation |
| S23 | SC Revenue Ruling #22-3 Employer Wage Withholding Requirements (income tax) | Summary of Employer SC Wage Withholding Requirements; Examples 1-7 | South Carolina Department of Revenue |
| S24 | SC Code 12-6-3400 credit for income tax paid by a resident to another state; absence of a reciprocity provision | 12-6-3400(A)-(C); text search of chapter 6 and chapter 8 | SC Legislative Services Agency |
| S25 | GB-1210-2026 full-text re-read (rounding, reciprocity, residents) | pp.3-4, tables pp.6-18 | Vermont Department of Taxes |
| S26 | Wisconsin Publication W-166 Withholding Tax Guide (1/26): deposits, reconciliation, nonresidents, alternate-method examples | Reminders; 2C; 3C-3P; 4A-4E; Withholding methods pp. 25-27 | Wisconsin Department of Revenue |
| S27 | Arkansas 2025 AR1000F/AR1000NR Instructions - Other State Tax Credit; reciprocity search | Line 36 (Form AR1000TC Other State Tax Credit); Texarkana | Arkansas Department of Finance and Administration |
| S28 | Arizona DOR: Withholding Tax (employer page) | Nonresidents; Employment Excluded From Withholding | Arizona DOR |
| S29 | D.C. Code 1-206.02(a)(5) commuter-tax prohibition | 1-206.02(a)(5) | Council of the District of Columbia |
| S30 | DC OTR Form D-4A Certificate of Nonresidence (rev. 02/2015) | instructions | DC Office of Tax and Revenue |
| S31 | Delaware Division of Revenue: Employer Guide (withholding regulations) | Section 11 | Delaware Division of Revenue |
| S32 | Georgia DOR 2026 Employer Withholding Tax Guide (rev. September 2026) - scan for 23-day, reciprocity, rounding, POA | Whole guide (185,530 chars) | Georgia Department of Revenue |
| S33 | Iowa DOR: Iowa-Illinois Reciprocal Agreement | page text | Iowa DOR |
| S34 | IDOR Publication 130 (February 2026) Who is Required to Withhold Illinois Income Tax | Reciprocal agreements; Form IL-W-5-NR | Illinois Department of Revenue |
| S35 | Indiana Information Bulletin 33 - nonresident withholding; reciprocity | Form WH-47 Certificate of Residence | Indiana Department of Revenue |
| S36 | Kentucky Form 42A809 Certificate of Nonresidence (3-07) | form + instructions | Kentucky DOR |
| S37 | Maryland Income Tax Administrative Release No. 3 (Sep 2011) | II.B, II.C | Maryland Comptroller |
| S38 | 36 MRSA 5250(3) withholding agreements with other states | 36 MRSA 5250(3) | Maine Legislature |
| S39 | Michigan Treasury: Withholding Reciprocity Examples | Analysis | Michigan Treasury |
| S40 | Minnesota DOR: Reciprocity - Employee Withholding | page text | Minnesota DOR |
| S41 | Missouri Employer's Tax Guide Form 4282 (Revised 03-2026, published Dec 2025) - 2026 withholding formula, filing frequencies, due dates, W-2/MO W-3 | Sections 4, 7, 8, 9, 10, 11, 12, 21; 2026 Withholding Tax Formula pp.12-13 | Missouri Department of Revenue |
| S42 | Montana DOR: North Dakota Reciprocity Agreement | page | Montana Department of Revenue |
| S43 | North Dakota Tax: Income Tax Withholding (Reciprocity) | Reciprocity | ND Office of State Tax Commissioner |
| S44 | NJ Division of Taxation: PA/NJ Reciprocal Income Tax Agreement | page text | NJ Division of Taxation |
| S45 | Ohio Dept of Taxation: Employer Withholding FAQ (exempt compensation list) | exempt-from-withholding list | Ohio Dept of Taxation |
| S46 | Pennsylvania PIT Guide: Income Subject to Tax Withholding (Reciprocal Agreements) | Reciprocal Agreements | Pennsylvania DOR |
| S47 | Virginia Tax: Reciprocity | page text | Virginia Dept of Taxation |
| S48 | Vermont Withholding page: out-of-state employers 30-day rule | Withholding (employers) | Vermont Department of Taxes |
| S49 | Wisconsin DOR Publication 121 (01/26) Reciprocity | parts 2-5 | Wisconsin DOR |
| S50 | West Virginia TSD 381 Withholding Information for Employers (Rev. Sep 2025) | withholding not required list | WV Tax Division |
| S51 | ADOR 30-Day Safe Harbor Rule page (Act 2025-334) | whole page | Alabama Department of Revenue |
| S52 | Arkansas DFA Withholding Tax Employer's Instructions (Effective 01/01/2026, Revised 4/27/26) | Introduction; Supplemental Wages; Nonresident Employees; Texarkana Residents | Arkansas Department of Finance and Administration |
| S53 | California EDD DE 44 Employer Guide Rev. 52 (4-26): Wages in Another State; Interstate Reciprocal Coverage Elections; nonresident apportionment; multistate … | p.78 (PDF p.86) Wages in Another State + Interstate Reciprocal Coverage Elections; nonresident table (PIT); New Employee Registry | California EDD |
| S54 | Hawaii Booklet A sections 10 and 13 - nonresident employees (Wayback copy) | Section 10(a); Section 13 Form HW-6 | Hawaii Department of Taxation |
| S55 | Idaho State Tax Commission - Income you don't have to withhold on | exceptions list | Idaho State Tax Commission |
| S56 | Illinois DOR Publication 130 (R-02/26) Who is Required to Withhold Illinois Income Tax: 'When is compensation paid in Illinois' (localization rules 1-4, … | pp.3-5 When is compensation paid in Illinois, rules 1-4; examples | Illinois Department of Revenue |
| S57 | Louisiana Register Vol. 52 No. 3 (2026-03-20), Rule 2603#037: Mobile Workforce Exemption (LAC 61:I.1923), adopted | LAC 61:I.1923 A.2.a, A.2.d (repealed), C.1.a, C.1.b.i, C.2; LR 52:358 | Louisiana Department of Revenue, Tax Policy and Planning Division (published … |
| S58 | Louisiana Act 382 of the 2025 Regular Session (HB 567, enrolled): R.S. 47:112.2(A) and 47:248(B)(1)(a) mobile workforce exemption 30 days; R.S. … | Sec. 1 (R.S. 47:112.2(A), 47:248(B)(1)(a)); Sec. 2 (repeal of 47:248(B)(1)(d)); Sec. 3 (income tax periods beginning on or after 2026-01-01); Sec. 4 … | Louisiana Legislature |
| S59 | 2026 Withholding Tables instruction 3 (nonresident employees) and 36 MRSA 5142(8-B) | 36 MRSA 5142(8-B)(A); booklet instruction 3 | Maine Legislature; Maine Revenue Services |
| S60 | Minnesota Income Tax Withholding Instruction Booklet and Tax Tables 2026 (wh-inst-26): computer formula, deposits, returns, W-2 | pp. 3-12 and p. 34 Computer Formula | Minnesota Department of Revenue |
| S61 | Mississippi Pub 89-700-25-1 (Rev. 07/25) - Treatment of Residents and Nonresidents; reciprocity search | Instructions sec. 5 (a)-(d) | Mississippi Department of Revenue |
| S62 | Montana Guide: nonresident withholding and 30-day exemption | Withholding from Nonresidents; Thirty-Day Nonresident Wage Withholding Exemption | Montana Department of Revenue |
| S63 | NDCC chapter 57-38 Income tax (57-38-30.3, 57-38-59, 57-38-59.1, 57-38-59.3) | 57-38-30.3(1)(g),(2); 57-38-59(1)-(4); 57-38-59.1; 57-38-59.3 | ND Legislative Council |
| S64 | 2026 Nebraska Circular EN - nonresident employees (Wayback copy) | p.6 Nonresident Employees; Neb. Rev. Stat. 77-2733(8) | Nebraska Department of Revenue |
| S65 | NM TRD FYI-104 (Rev. 11/2025) notes on nonresidents and other-state tax | Who Must Withhold Note 2; Special Situations | New Mexico Taxation and Revenue Department |
| S66 | NY DTF TSB-M-06(5)I Application of the Convenience of the Employer Test to Telecommuters and Others (2006-05-15), quoting 20 NYCRR 132.18(a) | pp.1-2; 20 NYCRR 132.18(a) quoted; bona fide employer office factors | NY State Dept of Taxation and Finance |
| S67 | Utah Pub 14 Rev. 04/26 - nonresidents working temporarily in Utah; residents working outside Utah | Employee Withholding Exclusions; Who must withhold | Utah State Tax Commission |
| S68 | Connecticut DRS Special Notice 2018(9.1) (convenience of employer test) | Convenience of the Employer Test; 2018 Pub. Act 49 sec.20 | Connecticut DRS |
| S69 | 30 Del. C. 1121-1124 Nonresident individuals: tax and Delaware-source income | 30 Del. C. 1121, 1122, 1124(b)(1) | Delaware General Assembly (Delaware Code Online) |
| S70 | NJ Convenience of the Employer Sourcing Rule FAQ | Who does the rule apply to | NJ Division of Taxation |
| S71 | 61 Pa. Code 109.8 Earnings of nonresident employes or casual employes and officers | 109.8 (amended 1999-12-11, 29 Pa.B. 6249); site current through 56 Pa.B. 5370 (2026-08-08) | Pennsylvania Code & Bulletin (PA DOR regulation) |
| S72 | 49 U.S.C. 14503 Withholding State and local income tax by certain carriers (US Code 2024 ed., GPO govinfo) | 14503(a)(1), (b)(1)-(3), (c) | US Congress / GPO |
| S73 | 49 U.S.C. 11502 Withholding State and local income tax by rail carriers (US Code 2024 ed., GPO govinfo) | 11502(a)-(b) | US Congress / GPO |
| S74 | 49 U.S.C. 40116(f) Pay of air carrier employees (US Code 2024 ed., GPO govinfo) | 40116(f)(1)-(3) | US Congress / GPO |
| S75 | 46 U.S.C. 11108 Taxes (seamen) (US Code 2024 ed., GPO govinfo) | 11108(a), (b) | US Congress / GPO |
| S76 | 4 U.S.C. 114 Limitation on State income taxation of certain pension income (LII republication) | 114(a)-(b) | Cornell LII (republication) |
| S77 | 50 U.S.C. 4001 Residence for tax purposes (SCRA sec. 511, as amended by Pub. L. 115-407 (2018) and Pub. L. 117-333 (2023)) (US Code 2024 ed.) | 4001(a)(1)-(3), (b), (c) | US Congress / GPO |
| S78 | Alaska Employment Security Tax Employer Handbook (taxbook.pdf, PDF modified 2025-05-05) | pp. 6-25 (employer, multistate, TQ01, wage base, employee contribution, records, excluded employment, wages, retirement/125/fringe, rates) | Alaska DOLWD Employment Security Tax |
| S79 | Code of Alabama 1975 Sec. 25-4-16 (wages, 8,000 USD taxable base, other-state employment counted) and Sec. 25-4-54 (experience-rated contributions, shared cost) | 25-4-16(b)(1); 25-4-54(a),(f) | Alabama Legislature (ALISON Code of Alabama) |
| S80 | Conn. Gen. Stat. 31-222(b) UI taxable wages (indexed wage base; other-state wage credit) | Sec. 31-222(b)(1)(A)(v)-(vi) | Connecticut General Assembly |
| S81 | 19 Del. C. ch. 33 subch. I Unemployment Compensation - definitions (3302): taxable wage base, localization, exclusions | 19 Del. C. 3302(12)(H)-(I), (15)(A)-(N), (28)(A)(vii)-(x), (28)(B) | Delaware General Assembly (Delaware Code Online) |
| S82 | Florida DOR Employer Guide to Reemployment Tax (RT-800002, R. 03/25) | pp.2-3 liability; pp.8-11 RT-6, wage base, annual option, taxable/exempt wages, BLS-3020, RT-6EW, E-Verify | Florida Department of Revenue |
| S83 | DLIR UI Handbook for Employers (web edition) | I Contributions: Registration; Quarterly Wage, Contribution and E&T Assessment Report; Taxable wages; Penalties; SIDES | Hawaii DLIR Unemployment Insurance Division |
| S84 | Iowa Administrative Code 871 chapter 23 Employer's contribution and charges (IAC 3/4/26) | 871-23.1(5),(17),(18); 23.5; 23.6(1)-(4); 23.8(1),(2),(5); 23.13; 23.24 | Iowa Workforce Development (published by Iowa Legislature) |
| S85 | Idaho Department of Labor - Unemployment Insurance Tax Information Handbook for Businesses (rev. 2025-11-05) | Who must pay; quarterly reports TX20/TX26/TX20C; standard rate; taxable wage base; corporate officers; claiming wages in another state; exempt services | Idaho Department of Labor (Wayback id_ 20260113182918) |
| S86 | K.S.A. 44-703 Employment security law definitions (employer coverage, employment exclusions, wages, taxable wage base) | (h)(1),(h)(5), (i)(4)(C),(F),(I),(J),(K),(N),(O),(T),(W), (o), (o)(1), (o)(2)(A)-(C), (jj), (kk) | Kansas Office of the Revisor of Statutes |
| S87 | KRS 341.030(7)(a) multistate wage-base credit (covered employment under another state's law) | KRS 341.030(7)(a) last sentence | Kentucky Legislative Research Commission |
| S88 | 26 MRSA 1043 Employment Security Law definitions (wages, employment, exclusions, localization) | 1043(1),(9),(11) incl. A-2, A-3, E-F localization, exclusions; (19) | Maine Legislature, Office of the Revisor of Statutes |
| S89 | Michigan Employment Security Act sec. 44 (MCL 421.44) remuneration, wages and taxable wage limit | MCL 421.44(1)-(5) | Michigan Legislature |
| S90 | Mississippi Employment Security Law (MDES compilation of Miss. Code Title 71 ch.5, web edition 2024-02-15): coverage 71-5-11, contributions 71-5-351, taxable … | 71-5-11 I(6),(7),(8)-(10),(15)(b)-(h); 71-5-351(1)-(3); 71-5-353(4) | Mississippi Department of Employment Security (compilation of statute) |
| S91 | Montana DLI UI Division Employer Handbook (Revised January 2025; PDF modified 2026-03-04) | Sections 2-6 (special classes table pp. 5-8; multistate test p. 9; excess wages p. 14; payments and reports p. 16; penalties p. 17) | Montana Department of Labor and Industry, Unemployment Insurance Division |
| S92 | G.S. 96-9.3 Determination of taxable wages (UI wage base indexation) | 96-9.3(a),(b) | NC General Assembly (General Statutes, official host ncleg.gov) |
| S93 | NDCC chapter 52-04 Contributions and payments by employers (UI) | 52-04-01, 52-04-03, 52-04-06, 52-04-11 | ND Legislative Council |
| S94 | NDOL Employer's Guide to Unemployment Insurance (Revised 9/11/2025): registration, wage reports, deadlines, multistate, wage-base credit | pp.6-7, 11-13, 16 | Nebraska Department of Labor |
| S95 | NH RSA chapter 282-A Unemployment Compensation: 282-A:9 (employment, localization, exclusions), 282-A:15 (wages), 282-A:69 (payment of contributions) | RSA 282-A:9 I, IV; 282-A:15 I-II; 282-A:69 I | NH General Court |
| S96 | NRS chapter 612 Unemployment Compensation, wayback snapshot 2026-10-19 | NRS 612.080, 612.090, 612.095, 612.105, 612.118, 612.119, 612.121, 612.130, 612.133, 612.190, 612.540, 612.545, 612.606 | Nevada Legislature (Legislative Counsel Bureau) |
| S97 | Employment Security Act of 1980 - 40 O.S. 1-201(48) taxable wages; 1-223 applicable percentages; 3-102 contributions | 40 O.S. 1-201(48); 1-223 (Laws 2025 c. 140, eff. 2025-11-01); 3-102(A)-(C) | Oklahoma Legislature (Oklahoma Statutes, Title 40) |
| S98 | ORS chapter 657 Unemployment Insurance (2025 Edition): 657.035, 657.095, 657.435, 657.462 | ORS 657.035(1),(4); 657.095(1)-(2); 657.435; 657.462 Table A | Oregon Legislature (ORS) |
| S99 | RIGL 28-42-3 Definitions (wages, taxable wage base, other-state employment) | 28-42-3 'Wages' (i) | Rhode Island General Assembly |
| S100 | SC Code Title 41 ch. 27 (Employment Security Law definitions): 41-27-260, 41-27-265, 41-27-380, 41-27-410 | 41-27-260 exempted employment; 41-27-265 corporate officers; 41-27-380(A)-(B) wages and taxable wage base; 41-27-410 DACA | South Carolina Legislature |
| S101 | SDCL Title 61 Reemployment Assistance (unemployment compensation), full official text | SDCL 61-1-17, 61-1-19, 61-1-46, 61-5-24, 61-5-25, 61-5-25.7, 61-5-28, 61-5-28.1, 61-5-29 | South Dakota Legislature (Legislative Research Council) |
| S102 | 21 V.S.A. 1321(b)(2) wages for other-state employment count toward the Vermont base | 1321(b)(1)-(2) | Vermont General Assembly (Wayback copy 2026-04-18) |
| S103 | W. Va. SB 841 (2024 Regular Session) enrolled committee substitute - amends 21A-1A-28 Wages | 21A-1A-28(b)(1),(d) | West Virginia Legislature |
| S104 | W.S. 27-3-102(a)(xviii) definition of wage for UI contributions (taxable wage base and exclusions); 27-3-303(a) statewide average annual wage | 27-3-102(a)(xviii)(A)-(W); 27-3-303(a); 27-3-306(d)(i) | Wyoming Legislature |
| S105 | CT Paid Leave Authority Guide for Employers (fact sheet updated October 2024) | Eligibility footnote | Connecticut Paid Leave Authority |
| S106 | D.C. Code 32-541.01 Universal Paid Leave - definitions (covered employee, wages) | 32-541.01(3),(22) | Council of the District of Columbia |
| S107 | 19 Del. C. ch. 37 Healthy Delaware Families Act (Delaware Paid Leave): coverage, contributions, benefits | 19 Del. C. 3701(3),(6),(7),(24); 3703; 3704(a); 3705(a)-(l); 3714 | Delaware General Assembly (Delaware Code Online) |
| S108 | Md. Code, Labor and Employment 8-202 (UI covered employment: localization) | LE 8-202(b)-(d) | Maryland General Assembly |
| S109 | Maine DOL PFML Employer FAQ (July 2026): wage definition, locality, tax treatment, W-2 Box 14 | FAQ 5, 6, 9-15, 17, 24, 26-27 | Maine Department of Labor, Paid Family and Medical Leave |
| S110 | ORS chapter 657B Paid Family and Medical Leave Insurance (2025 Edition) | ORS 657B.150(1)-(5); 657B.175 | Oregon Legislature (ORS) |
| S111 | RIGL 28-39-2 TDI definitions (employment = chapter 42 definition) | 28-39-2(14) | Rhode Island General Assembly |
| S112 | RCW 50A.05.010(8) Washington Paid Family and Medical Leave: definition of employment (localization), effective until 2027-06-30 (Wayback copy 2026-04-23) | 50A.05.010(8)(a)(i)-(ii), (24); a version effective 2027-06-30 also printed | Washington State Legislature |
| S113 | DOL OUI memo to State UI Directors: Spirit Airlines, reminder to review localization of work guidance (undated; Acting Deputy Administrator S. Simonetta) | full text (2 pp.) | US DOL ETA Office of Unemployment Insurance |
| S114 | DOL ETA Unemployment Insurance Program Letter No. 20-04 Localization of Work Provisions (2004-05-10) | paras 1-7; Attachment I Localization of Work Provisions (attachment not held) | US DOL Employment and Training Administration |
| S115 | 26 U.S.C. 3306(b)(1) FUTA wages: 7,000 per employer per calendar year; successor rule (US Code 2024 ed.) | 3306(b)(1) | US Congress / GPO |
| S116 | DOL OUI Comparison of State UI Laws 2023 Ch.2 Financing, Employee Contributions | Ch.2 Employee Contributions | US DOL ETA OUI |
| S117 | Ward v. United Airlines, Inc. (Cal. Supreme Court, S248702, 2020-06-29), 9 Cal.5th 732: geographic reach of Labor Code 226 | Part III; Part IV answers (1)-(2); Lab. Code 226; Wage Order 9 sec.1(E) | Supreme Court of California |
| S118 | General Instructions for Forms W-2 and W-3 (2026): Boxes 15-20 State and local income tax information; Multiple forms; W-3 box 15 | Specific Instructions for Form W-2, Boxes 15 through 20; Multiple forms; Form W-3 Box 15, Boxes 16-19 | IRS |
| S119 | 42 U.S.C. 653a(b) National new-hire reporting: multistate employers and timing (US Code 2024 ed.) | 653a(b)(1)(B), (b)(2) | US Congress / GPO |
| S120 | 42 U.S.C. 666(b)(6)(A), (b)(9), (f) Income withholding: orders from another State (US Code 2024 ed.) | 666(b)(6)(A)(i)(I)-(V), (b)(9), (f) | US Congress / GPO |
| S121 | S. 1443 (119th Congress) Mobile Workforce State Income Tax Simplification Act of 2025, introduced text (GPO BILLS-119s1443is) | secs. 2(a)-(c), 3 | US Senate / GPO |
| S122 | H.R. 10271 (119th Congress) Mobile Workforce State Income Tax Simplification Act of 2026, introduced text (GPO BILLS-119hr10271ih) | secs. 1-3 | US House of Representatives / GPO |
