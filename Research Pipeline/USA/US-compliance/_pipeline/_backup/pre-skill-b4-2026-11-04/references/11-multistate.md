# the multistate reference: Multistate routing layer


This annex is the routing layer. It decides, per employee, which State annexes apply in addition to the federal reference. Three master-data keys drive every decision: work location (income-tax withholding State and wage-hour law), residence (resident withholding, reciprocity, transport-worker and military-spouse rules) and the UI State resulting from the localization test (UI, and by default PFML/SDI). Every value is shown with its effective dates and its source.

Routing order for the engine:

1. Wage-hour law: the more protective of federal, State and local law at the place of performance (FLSA does not excuse a higher State/municipal minimum wage, a lower maximum workweek or a stricter child-labour standard: apply the more protective standard of the place where the work is performed).
2. UI State: the localization test, applied once per employee and employer (One State covers the entire service with one employer, in order: (1) localized (entirely in the State, or out-of-state service incidental: temporary, transitory, isolated); (2) else some service in the base-of-operations State; (3) else some service in the State of direction or control; (4) else some service in the State of residence).
3. Work-State income-tax withholding: start when the non-resident threshold of the work State is met (MULTI.2 table), unless reciprocity with the residence State applies and the employee has filed the certificate (MULTI.2 reciprocity table).
4. Residence-State withholding: apply the residence State's rule for residents working elsewhere (MULTI.2 table); the credit for tax paid to another State is an assessment matter, never a payroll deduction.
5. Federal carve-outs override State sourcing for transport workers, seamen and military spouses.
6. PFML/SDI premium State: the UI State unless the State's own coverage test differs (MULTI.3 table).

## MULTI.1 Employment and labour code

Wage-hour law follows the place of performance. California's reach is decided statute by statute (court rulings below).

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Wage hour overlay rule | FLSA does not excuse a higher State/municipal minimum wage, a lower maximum workweek or a stricter child-labour standard: apply the more protective standard of the place where the work is performed | from 2026-01-01 |  | S1 |  |
| CA oman rule | Oman v. Delta Air Lines, Cal. S. Ct. S248726 (2020-06-29), Lab. Code 204 and 226: do not reach pay periods in which the employee works in CA only episodically and for less than a day at a time, unless the employee works primarily in CA in that period, or works primarily in no State and has the CA base of operations. Minimum-wage reach left undecided. | from 2020-06-29 | employer pay timing and pay statement | S2 | STATUS: in force (final answer to certified question). |

Not configured in this release (open gap RQ-443): Paid sick leave multistate scope: not established from an official source.

Not configured in this release (open gap RQ-446): Payslip reach other states: not established from an official source.

Not configured in this release (open gap RQ-447): CA minimum wage nonresident reach: not established from an official source.

## MULTI.2 Income tax withholding

General rule: No general federal rule: each State taxes residents on all wages (credit at assessment for tax paid to the work State) and nonresidents on wages for services performed in the State; federal limits only for transport workers and military spouses. 4 U.S.C. 114 is retirement income only, not wages.. Everywhere without a convenience rule: Everywhere else wages follow the place of physical performance. Local taxes sit outside State reciprocity (State annexes). The federal Mobile Workforce bills are drafts and are not modelled.

**Residents working in another State: withholding rule and credit level**

| State | Withholding rule | Credit for other-State tax operates at | Effective | Source |
|---|---|---|---|---|
| AR | — | assessment | from 2021-01-01 | S3 |
| AZ | — | assessment | from 2026-01-01 | S4 |
| CO | Withhold CO on all wages except wages for services in another State that itself requires withholding | — | from 2026-01-01 | S5 |
| CT | All wages subject; where the employer must withhold for the other jurisdiction, CT tax is prorated and only the excess remitted | — | from 2026-01-01 | S6 |
| DC | — | assessment | from 2026-01-01 | S7 |
| GA | No GA withholding if the other State requires withholding; otherwise withhold GA | — | from 2026-01-01 | S8 |
| IL | IL resident working entirely in another State whose compensation is subject to that State's withholding: no IL withholding (credit on the return) | — | from 2026-02-01 | S9 |
| KS | KS tax on total wages less the other State's required withholding (example 250 - 130 = 120); zero if the other State's withholding is higher | — | from 2024-07-01 | S10 |
| LA | LA residents working in another State may be subject to LA withholding if those wages are not subject to withholding there | — | from 2026-01-01 | S11 |
| MA | MA amount minus the other jurisdiction's amount (credit method, 830 CMR 62B.2.1(9)(b)); employer without MA office may withhold for MA residents as a convenience | — | from 2026-01-01 | S12 |
| ME | — | assessment | from 2026-01-01 | S13 |
| MS | Withhold MS on total wages except to the extent withheld for another State; commuter to a no-income-tax State is withheld MS on total wages (credit at assessment). MS is not a credit-only State. | assessment | from 2026-01-01 | S14, S15 |
| NC | Withhold on all wages wherever earned, except no NC withholding on wages for services in a State that requires the employer to withhold | — | from 2026-01-01 | S16 |
| NY | Withhold NYS tax for NY residents even if wages are earned outside NY | — | from 2026-01-01 | S17 |
| OH | Every employer with an office or transacting business in Ohio withholds on residents (resident credit IT RC at assessment) | assessment | from 2025-01-01; from 2026-10-29 | S18, S19 |
| OK | Residents are withheld on services within or without Oklahoma (68 O.S. 2385.1 employee definition) | assessment | from 2023-07-01; from 2025-01-01 | S20, S21 |
| RI | — | assessment | from 2025-01-01 | S22 |
| SC | Withhold for the other State; if that State has no income tax, withhold 100% SC (12-8-520(C)(1)) | assessment | from 2026-01-01 | S23, S24 |
| VT | Compute on the full payment, then reduce by tax withheld for the State where services were performed | — | from 2026-01-01 | S25 |
| WI | Residents working outside WI: withholding on all wages; Minnesota special arrangement - no WI withholding if MN withholds | — | from 2026-01-01 | S26 |

**Reciprocity: partner States and exemption certificate**

| State | Partners | One-way rule | Non-resident exemption | Certificate | Effective | Source |
|---|---|---|---|---|---|---|
| AR | none (zero hits for reciprocity in the AR instructions) | — | — | — | from 2025-01-01 | S27 |
| AZ | — | AZ exempts residents of CA, IN, OR, VA on Form WEC (they can claim the AZ credit); one-way - an AZ resident working in CA is withheld by CA | — | — | from 2026-01-01 | S28 |
| CT | none | — | — | — | from 2026-01-01 | S6 |
| DC | MD, VA (from the partner side; DC taxes no nonresident at all) | — | D.C. Code 1-206.02(a)(5): DC may not tax any nonresident's personal income; DC withholding stops for ANY nonresident (D-4A: domicile outside DC and under 183 days) | D-4A | from 2026-01-01 | S29, S30 |
| DE | none | — | — | — | from 2026-01-01 | S31 |
| GA | none | — | — | — | from 2026-01-01 | S32 |
| IA | IL | — | — | IA 44-016 (IL resident in IA); IL-W-5-NR (IA resident in IL) | from 2026-01-01 | S33 |
| IL | IA, KY, MI, WI | — | — | IL-W-5-NR | from 2026-02-01 | S34, S9 |
| IN | KY, MI, OH, PA, WI (county tax still withheld) | — | — | WH-47 | from 2026-01-01 | S35 |
| KY | IL, IN, MI, OH (unless 20% S-corp shareholder-employee), VA (daily commuters only), WV, WI | — | — | 42A809 | from 2026-01-01 | S36 |
| MD | DC, PA, VA, WV (not for abode in MD > 6 months and 183+ days, except WV) | — | — | MW507 | from 2026-01-01 | S37 |
| ME | none in force (agreements authorised by statute, none identified) | — | — | — | from 2026-01-01 | S38 |
| MI | IL, IN, KY, MN, OH, WI | — | — | per MI Guide 446 (form not named in the row) | from 2026-01-01 | S39 |
| MN | MI, ND (employee returns home at least monthly) | — | — | MWR (yearly; copies to MN DOR by Mar 31) | from 2026-01-01 | S40 |
| MT | — | — | — | MW-4 (annual renewal) | from 2026-01-01 | S41 |
| NC | none | — | — | — | from 2026-01-01 | S16 |
| ND | MN, MT | — | — | NDW-R (yearly, by Feb 28 or within 30 days) | from 2026-01-01 | S42 |
| NJ | PA (compensation only) | — | — | NJ-165 (PA resident in NJ); REV-419EX (NJ resident with PA employer) | from 2026-01-01 | S43 |
| OH | IN, KY, MI, PA, WV | — | — | IT 4 (combined certificate) | from 2026-01-01 | S44 |
| PA | IN, MD, NJ, OH, VA, WV | — | — | REV-419 | from 2026-01-01 | S45 |
| VA | DC, KY (daily commuters), MD, PA, WV | — | — | VA certificate (not named in the row; VA annex) | from 2026-01-01 | S46 |
| VT | none (four official withholding texts, none lists one) | — | — | — | from 2026-01-01 | S47 |
| WI | IL, IN, KY, MI | — | — | W-220 | from 2026-01-01 | S48 |
| WV | KY, MD, OH, PA, VA | — | — | WV/IT-104 | from 2026-01-01 | S49 |

**Non-resident thresholds before work-State withholding starts**

| State | Days | Amount | Share | Rule | Allocation | Employer start | Catch-up | Other | Effective | Source |
|---|---|---|---|---|---|---|---|---|---|---|
| AR | — | — | — | — | No threshold: apportioned by AR working days (HB1116 of 2025, 15 days / 2,500, died) | — | — | — | from 2026-01-01 | S50 |
| AZ | 60 days | — | — | — | — | — | — | — | from 2026-01-01 | S28 |
| CA | — | — | — | — | No threshold: working-day ratio from day 1 (commission pay: volume ratio) | — | — | — | from 2026-01-01 | S51 |
| CO | — | — | — | — | No threshold: apportioned by days worked in CO (a day counts if majority of working time is in CO) | — | — | — | from 2026-01-01 | S5 |
| CT | 15 days | — | — | — | — | — | — | — | from 2026-01-01 | S6 |
| ID | — | USD 1,000 | — | — | — | — | — | — | from 2026-04-12 | S52 |
| IL | 30 days | — | — | — | — | — | — | — | from 2026-01-01 | S53 |
| LA | 30 days | — | — | — | — | Begin withholding and report on Form L-1 beginning in the period in which the 31st day fell | Not configured in this release (open gap RQ-411): Not established from an official source. | — | from 2026-01-01; from 2026-03-20 | S54, S55 |
| ME | 12 days | USD 3,000 | — | — | — | — | — | — | from 2026-01-01 | S56 |
| MN | — | USD 15,300 | — | — | — | — | — | — | 2026-01-01 to 2026-12-31 | S57 |
| MS | — | — | — | Day 1 by earnings ratio, except no withholding when annual MS earnings will be below the standard deduction for the filing status | Earnings ratio; principal place of employment in MS -> total wages unless the other State requires withholding | — | — | — | from 2025-07-01; from 2026-01-01 | S58, S15 |
| ND | — | — | — | Mobile workforce exclusion (57-38-59.3): present 20 days or fewer, no other ND income, home State reciprocal exclusion or no income tax; not athletes, entertainers, persons of prominence, construction workers, key employees | — | — | — | — | from 2026-01-01 | S59 |
| NY | — | — | — | — | No threshold: NY working days / total working days with the convenience test | — | — | — | from 2006-05-15 | S60 |
| SC | — | — | — | — | — | — | — | Not configured in this release (open gap RQ-448): Not established from an official source. |  |  |
| UT | 20 days | — | — | — | — | — | — | — | from 2026-01-01 | S61 |
| VT | 30 days | — | — | — | — | — | — | — | from 2026-01-01 | S47 |
| WV | 30 days | — | — | — | — | — | — | — | from 2026-01-01 | S49 |

**Convenience-of-the-employer rules**

| State | Rule | Litigation | Effective | Source |
|---|---|---|---|---|
| AR | Not a convenience State: Act 1019 of 2021 (SB 484), in force from TY2021 - a nonresident works in AR only when physically located in AR | — | from 2021-01-01 | S3 |
| CT | From tax years beginning 2019-01-01 CT applies the resident State's convenience test to nonresidents working for a CT employer | — | from 2019-01-01 | S62 |
| DE | 30 Del. C. 1124(b)(1): compensation is DE-source if attributable to employment in DE and not required to be performed elsewhere; working from home does not qualify for the PIT-SCW exclusion | — | from 2026-01-01 | S63 |
| NE | From 2025: services performed outside NE for the nonresident's convenience are NE-sourced (77-2733(8)(c)) | — | from 2025-01-01 | S64 |
| NJ | From 2023 NJ applies the convenience rule against residents of States that apply one (DE, NE, NY; CT by reciprocal law); PA residents excluded by the reciprocal agreement | — | from 2023-01-01 | S65 |
| NY | 20 NYCRR 132.18(a): nonresident allocates by NY working days / total working days; days outside NY count only if worked of NECESSITY; home-office days are NY days unless the home is a bona fide employer office | Not configured in this release (open gap RQ-445): Not established from an official source. | from 2006-05-15 | S60 |
| PA | 61 Pa. Code 109.8: same necessity test as NY; PA reciprocal agreements prevail | — | from 1999-12-11 | S66 |

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| MO reciprocity states | none | 2026-01-01 to 2026-12-31 | withholding | S67 |  |
| AL non-resident safe harbor days | 30 days | from 2026-01-01 | withholding | S68 | 30 or fewer AL days, duties in more than one State, home State has a similar exclusion or no PIT; from day 31 all AL income for the year is withheld/reported. Qualifying States as of 2026-10-01: AK, FL, GA, IL, IN, LA, MT, NV, NH, SD, TN, TX, WA, WV, WY. Excludes athletes, entertainers, public figures. |
| Ok PIT nonresident quarterly threshold | USD 300 | from 2023-07-01 | withholding | S21 | Nonresident whose OK income in any calendar quarter is not more than 300 USD excluded (68 O.S. 2385.1). |
| GA non-resident threshold amount | USD 5,000 | from 2026-01-01 | withholding | S8 | Taxable nonresident: more than 5% of wages or more than 5,000 USD attributable to GA. |
| WI PIT nonresident DE minimis | USD 1,500 | from 2026-01-01 | withholding | S26 | Expected WI earnings under 1,500 (catch-up once exceeded). |
| GA non-resident threshold percent | 5 % | from 2026-01-01 | withholding | S8 | More than 5 % of wages attributable to GA (alternative to 5,000). |
| Transport motor carrier | Employee with regularly assigned duties in 2+ States: taxable ONLY by the residence State/subdivision (49 U.S.C. 14503) | from 1996-01-01 | withholding | S69 |  |
| Transport rail | Residence State/subdivision only (49 U.S.C. 11502) | from 2026-01-01 | withholding | S70 |  |
| Transport air carrier | Residence State plus the State where more than 50% of carrier pay is earned (scheduled flight time) (49 U.S.C. 40116(f)) | from 2018-10-05 | withholding | S71 |  |
| Transport air carrier share threshold | 50 % | from 2018-10-05 | withholding | S71 |  |
| Transport seamen | Seamen's wages may not be withheld for State/local tax; multi-State vessel crew and pilots taxable only by the residence State (46 U.S.C. 11108) | from 2010-10-15 | withholding | S72 |  |
| PIT sourcing general | No general federal rule: each State taxes residents on all wages (credit at assessment for tax paid to the work State) and nonresidents on wages for services performed in the State; federal limits only for transport workers and military spouses. 4 U.S.C. 114 is retirement income only, not wages. | from 2026-01-01 |  | S73 |  |
| MT reciprocity states | ND | from 2026-01-01 | withholding | S41 | Bilateral exemption from work-State withholding on the employee nonresidence certificate; 30 pairs confirmed on both sides. Local taxes are outside State reciprocity. |
| Hi non-resident exempt days | 60 days | from 2026-01-01 | withholding | S74 | Exempt if HW-6 on file, 60 days or fewer, paid from an office outside HI, regular workplace outside HI; employer files HW-7. Not for construction-contractor employees. |
| MT PIT nonresident days exemption | 30 days | from 2026-01-01 | withholding | S75 | No withholding if fewer than 30 days in MT AND work in more than one State; not for athletes, entertainers, per-event payees, construction workers, key employees. |
| NE PIT nonresident duty days | 7 days | from 2025-01-01 | withholding | S64 | From tax years beginning 2025-01-01: NE-sourced if services in NE exceed seven days. |
| NM PIT nonresident days threshold | 15 days | from 2026-01-01 | withholding | S76 | Not required to withhold from nonresidents working in NM 15 or fewer days in the calendar year. |
| Convenience default | Everywhere else wages follow the place of physical performance | from 2026-01-01 |  | S73 |  |
| Military spouse rule | A military spouse present in a State solely to be with the servicemember under military orders neither loses nor acquires residence or domicile; the spouse's income for services performed in that State is not income for services performed or from sources within that State if the spouse is not a resident of it; for any taxable year the spouse may elect the residence of the servicemember, the spouse's own residence or the permanent duty station (50 U.S.C. 4001(a)(2), (c)). Payroll effect: on the employee's State certificate of nonresidence, stop work-State withholding. | from 2018-12-31 | withholding | S77 |  |

## MULTI.2b Non-resident regime and reciprocity

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Reciprocity IL partners | IA,KY,MI,WI | 2026-01-01 to 2026-01-31 |  | S53 | Bilateral; confirmed on both sides. Local taxes are outside reciprocity. |

## MULTI.2c Local wage taxes

The local wage taxes of this jurisdiction, where any exist, are written in MULTI.2.

## MULTI.3 Social insurance: unemployment, disability, paid leave and payroll levies

UI covers the whole service with one employer in one State. Employee UI contributions exist only in the States listed in AK, NJ, PA (only three States levy employee UI contributions; take 2026 rates from the State annexes). The FUTA base counts wages across all States.

**Other-State wage-base credit for UI (wages reported to another State count toward this State's base)**

| State | Credit | Effective | Source |
|---|---|---|---|
| AK | True | from 2026-01-01 | S78 |
| AL | True | from 2026-01-01 | S79 |
| AR | Not configured in this release (open gap RQ-419): Not established from an official source. |  |  |
| AZ | Not configured in this release (open gap RQ-420): Not established from an official source. |  |  |
| CA | True | from 2026-01-01 | S51 |
| CO | Not configured in this release (open gap RQ-412): Not established from an official source. |  |  |
| CT | True | from 2025-01-01 | S80 |
| DC | Not configured in this release (open gap RQ-413): Not established from an official source. |  |  |
| DE | True | 2026-01-01 to 2026-12-31 | S81 |
| FL | True | from 2026-01-01 | S82 |
| GA | Not configured in this release (open gap RQ-421): Not established from an official source. |  |  |
| HI | True | from 2026-01-01 | S83 |
| IA | False | from 2025-02-26 | S84 |
| ID | conditional: only if tax was paid on them to that State (72-1349(1)) | from 2025-11-05 | S85 |
| IL | Not configured in this release (open gap RQ-422): Not established from an official source. |  |  |
| IN | Not configured in this release (open gap RQ-423): Not established from an official source. |  |  |
| KY | True | from 2022-03-24 | S86 |
| LA | Not configured in this release (open gap RQ-414): Not established from an official source. |  |  |
| MA | Not configured in this release (open gap RQ-424): Not established from an official source. |  |  |
| MD | Not configured in this release (open gap RQ-418): Not established from an official source. |  |  |
| ME | True | from 2026-01-01 | S87 |
| MI | True | from 2016-01-01 | S88 |
| MN | Not configured in this release (open gap RQ-425): Not established from an official source. |  |  |
| MO | Not configured in this release (open gap RQ-415): Not established from an official source. |  |  |
| NJ | Not configured in this release (open gap RQ-426): Not established from an official source. |  |  |
| NM | Not configured in this release (open gap RQ-416): Not established from an official source. |  |  |
| NY | Not configured in this release (open gap RQ-427): Not established from an official source. |  |  |
| OH | Not configured in this release (open gap RQ-428): Not established from an official source. |  |  |
| PA | Not configured in this release (open gap RQ-429): Not established from an official source. |  |  |
| TN | Not configured in this release (open gap RQ-430): Not established from an official source. |  |  |
| TX | Not configured in this release (open gap RQ-431): Not established from an official source. |  |  |
| UT | Not configured in this release (open gap RQ-417): Not established from an official source. |  |  |
| VA | Not configured in this release (open gap RQ-432): Not established from an official source. |  |  |
| WA | Not configured in this release (open gap RQ-433): Not established from an official source. |  |  |
| WI | Not configured in this release (open gap RQ-434): Not established from an official source. |  |  |

**PFML / SDI / TDI coverage test**

| State | Coverage test | Effective | Source |
|---|---|---|---|
| CA | Not configured in this release (open gap RQ-435): Not established from an official source. |  |  |
| CO | Not configured in this release (open gap RQ-439): Not established from an official source. |  |  |
| CT | Follows UI localization: employees for whom CT UI and payroll taxes are paid are working in CT | from 2026-01-01 | S89 |
| DC | More than 50% of work time in DC, or DC-based with substantial DC time and not more than 50% elsewhere; not by residence | from 2026-01-01 | S90 |
| DE | Follows the primary DE worksite (3701(6)a), not UI localization | from 2025-01-01 | S91 |
| HI | Not configured in this release (open gap RQ-442): Not established from an official source. |  |  |
| MA | Not configured in this release (open gap RQ-438): Not established from an official source. |  |  |
| MD | FAMLI covers employees in positions localized in MD (LE 8-202 UI localization); contributions start 2027-01-01 (US-MDS5-014) | from 2026-01-01 | S92 |
| ME | Follows the Maine UI localization test (FAQ 6) | from 2025-01-01 | S93 |
| MN | Not configured in this release (open gap RQ-440): Not established from an official source. |  |  |
| NJ | Not configured in this release (open gap RQ-436): Not established from an official source. |  |  |
| NY | Not configured in this release (open gap RQ-437): Not established from an official source. |  |  |
| OR | Follows UI localization (ORS 657B.175); employer size counts out-of-state employees too (US-ORS5-013) | from 2023-01-01 | S94 |
| RI | TDI follows the UI localization test (28-39-2 uses the chapter 42 definition) | from 2026-01-01 | S95 |
| VT | Not configured in this release (open gap RQ-441): Not established from an official source. |  |  |
| WA | Follows the UI localization test (RCW 50A.05.010(8)) | 2026-01-01 to 2027-06-30 | S96 |
| DEFAULT | Key the PFML/SDI premium State to sui_state unless the State annex proves otherwise (WA, CT, ME, OR, MD, RI proven; DC and DE differ) | 2026-01-01 to 2027-06-30 | S96 |

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| SUI localization test | One State covers the entire service with one employer, in order: (1) localized (entirely in the State, or out-of-state service incidental: temporary, transitory, isolated); (2) else some service in the base-of-operations State; (3) else some service in the State of direction or control; (4) else some service in the State of residence | from 2026-01-01 | employer UI reporting | S97 | DOL OUI restatement; same test in the 2023 DOL Comparison and UIPL 20-04; statutory instance Fla. Stat. 443.1216. |
| SUI localization telecommuting | UIPL 20-04 (2004, continuing) reissues the UIPL 291 interpretation with telecommuting examples | from 2004-05-10 | employer UI reporting | S98 |  |
| SUI reciprocal coverage election | Where no test resolves the case, employer, employee and States may elect coverage of all service in one State (performance, residence or place of business); CA CUIC 602/603 | from 2026-01-01 | employer UI reporting | S51 |  |
| FUTA wage base scope | FUTA 7,000 counts remuneration paid by the employer in the calendar year across all States: one base per employer, not per State; successor carry-over | from 2026-01-01 |  | S99 |  |
| KS SUI wage base other state credit | True | from 2026-01-01 | employer UI reporting | S100 | Wages the same employer already paid under another State's UI law in the same calendar year count toward this State's taxable wage base. 44-703(o)(2)(C)(i). |
| MS SUI wage base other state credit | True | from 2011-01-01 | employer UI reporting | S101 | Wages the same employer already paid under another State's UI law in the same calendar year count toward this State's taxable wage base. 71-5-353(4). |
| NC SUI wage base other state credit | True | from 2026-01-01 | employer UI reporting | S102 | Wages the same employer already paid under another State's UI law in the same calendar year count toward this State's taxable wage base. G.S. 96-9.3: wages paid in another State with contributions there. |
| ND SUI wage base other state credit | True | from 2026-01-01 | employer UI reporting | S103 | Wages the same employer already paid under another State's UI law in the same calendar year count toward this State's taxable wage base. 52-04-03(1); same employer. |
| NE SUI wage base other state credit | True | from 2025-09-11 | employer UI reporting | S104 | Wages the same employer already paid under another State's UI law in the same calendar year count toward this State's taxable wage base. 48-648.02. |
| NH SUI wage base other state credit | True | from 2026-01-01 | employer UI reporting | S105 | Wages the same employer already paid under another State's UI law in the same calendar year count toward this State's taxable wage base. 282-A:69 I. |
| NV SUI wage base other state credit | True | from 2026-01-01 | employer UI reporting | S106 | Wages the same employer already paid under another State's UI law in the same calendar year count toward this State's taxable wage base. NRS 612.545(2)(b): where that State's contributions were required. |
| Ok SUI wage base other state credit | True | from 2025-11-01 | employer UI reporting | S107 | Wages the same employer already paid under another State's UI law in the same calendar year count toward this State's taxable wage base. 40 O.S. 1-201(48). |
| Or SUI wage base other state credit | True | from 2026-01-01 | employer UI reporting | S108 | Wages the same employer already paid under another State's UI law in the same calendar year count toward this State's taxable wage base. ORS 657.095(2): same Oregon employer, proof prescribed by OED. |
| RI SUI wage base other state credit | True | from 2026-01-01 | employer UI reporting | S109 | Wages the same employer already paid under another State's UI law in the same calendar year count toward this State's taxable wage base. 28-42-3. |
| SC SUI wage base other state credit | True | from 2015-01-01 | employer UI reporting | S110 | Wages the same employer already paid under another State's UI law in the same calendar year count toward this State's taxable wage base. 41-27-380(B). |
| SD SUI wage base other state credit | True | from 2026-01-01 | employer UI reporting | S111 | Wages the same employer already paid under another State's UI law in the same calendar year count toward this State's taxable wage base. 61-1-46. |
| VT SUI wage base other state credit | True | from 2012-01-01 | employer UI reporting | S112 | Wages the same employer already paid under another State's UI law in the same calendar year count toward this State's taxable wage base. 21 V.S.A. 1321(b)(2). |
| WV SUI wage base other state credit | True | from 2024-07-01 | employer UI reporting | S113 | Wages the same employer already paid under another State's UI law in the same calendar year count toward this State's taxable wage base. SB 841 (2024): where contributions were required and paid. |
| WY SUI wage base other state credit | True | from 2026-05-08 | employer UI reporting | S114 | Wages the same employer already paid under another State's UI law in the same calendar year count toward this State's taxable wage base. 27-3-102(a)(xviii)(A). |
| MT SUI wage base other state credit | False | from 2025-07-01 | employer UI reporting | S115 | DLI handbook: wages reported to other States may not be used to reach the MT base. |
| SUI employee contribution states | AK, NJ, PA (only three States levy employee UI contributions; take 2026 rates from the State annexes) | from 2023-01-01 |  | S116 |  |

## MULTI.4 Pay statement

Default: the pay-statement statute of the work-location State (Default: the pay-statement statute of the work-location State (no other State reach rule researched); payslip in English (US-OWN-006)). California applies its own rule under the ruling recorded below.

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| CA ward rule | Ward v. United Airlines, Cal. S. Ct. S248702 (2020-06-29), Lab. Code 226: applies if the PRINCIPAL place of work is in CA (majority of working time); with no majority State, where CA is the base of work operations and some work is done in CA. Employer location, residence, place of pay receipt, taxes paid and a CBA are irrelevant. | from 2020-06-29 | employer pay-statement output | S117 | STATUS: in force. |
| Payslip reach default | Default: the pay-statement statute of the work-location State (no other State reach rule researched); payslip in English (US-OWN-006) | from 2020-06-29 |  | S117 |  |

## MULTI.5 Statutory reporting

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| W-2 states per form | 2 count | from 2026-01-01 | employer reporting | S118 | Boxes 15-20 carry up to TWO States and TWO localities; for more, a second W-2 repeating boxes a-f, never duplicating federal data on Copy A; W-3 box 15 = X when more than one State. |
| Newhire designated state | A multistate employer reporting electronically may send all new-hire reports to ONE designated State in which it has employees, after notifying HHS in writing | from 2026-01-01 | employer reporting | S119 |  |
| UI wage report routing | UI quarterly wage report to the sui_state only (localization); State income-tax withholding returns to every State where withholding applies | from 2026-01-01 | employer reporting | S97 |  |

Not configured in this release (open gap RQ-444): Newhire multistate registration channel: not established from an official source.

## MULTI.6 Leave

No rule for this jurisdiction is written under this heading.

## MULTI.7 Termination and final pay

No rule for this jurisdiction is written under this heading.

## MULTI.8 Benefits in kind and taxable wages

No rule for this jurisdiction is written under this heading.

## MULTI.9 Deductions and garnishments

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| IWO governing law | When an employer receives an income withholding order issued by another State, the employer shall apply the income withholding law of the State of the obligor's principal place of employment in determining the employer's fee for processing an income withholding order; the maximum amount permitted to be withheld from the obligor's income; the time periods within which the employer must implement the income withholding order and forward the child support payment; the priorities for withholding and allocating income withheld for multiple child support obligees; and any withholding terms or conditions not specified in the order | from 2026-01-01 | employer withholding | S120 |  |
| IWO remittance business days | 7 days | from 2026-01-01 | employer withholding | S120 | Remit to the SDU within 7 business days. |

## MULTI.10 Collective agreements and prevailing wage

Prevailing wage (public works) is an optional informational flag [US-OWN-009]: this guide documents prevailing-wage laws, thresholds and certified-payroll duties as an overlay, and the payroll build does not produce certified payroll reports.

No rule for this jurisdiction is written under this heading.

## MULTI.11 Indexation

No rule for this jurisdiction is written under this heading.

## MULTI.12 Payroll data protection and records

No rule for this jurisdiction is written under this heading.

## MULTI.13 Live legal change

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Mobile workforce bill senate | S. 1443 (introduced 2025-04-10, Senate Finance): DRAFT, NOT ENACTED - do not model | from 2026-01-01 | withholding and tax (if enacted) | S121 |  |
| Mobile workforce bill house | H.R. 10271 (introduced 2026-09-03, House Judiciary): DRAFT, NOT ENACTED - do not model | from 2026-01-01 | withholding and tax (if enacted) | S122 |  |

## MULTI.14 Authority worked examples (oracle values)

No authority worked example is reproduced in this annex; recomputed withholding examples are in Module 12.

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
| S6 | DRS Informational Publication 2026(1) Connecticut Employer's Tax Guide (Circular CT) | Q5 (gross CT wages); 'Residents working outside CT' (proration among qualifying jurisdictions); '15-Day Rule for Nonresident Employees' p.8; CT-W4NA allocation; Table C '2% Tax Rate Phase-Out Add-Back' p.28, Table D 'Tax Recapture' p.29, Table E 'Personal Tax Credits' p.30; State of Connecticut 2026 Withholding Tables pp.31-38 (weekly 31-32, bi-weekly 33-34, semi-monthly 35-36, monthly 37-38) | Connecticut Department of Revenue Services |
| S7 | D.C. Code 47-1806.04(a) resident credit for taxes paid to other states | 47-1806.04(a) | Council of the District of Columbia |
| S8 | GA DOR Employer's Withholding Tax Guide 2026: definitions, G-4, special payments | pp. 9-10, 14-17, 24-27 | Georgia Department of Revenue |
| S9 | IDOR Publication 130 (R-02/26) Who is Required to Withhold Illinois Income Tax: compensation paid in Illinois, exceptions, special categories | When is compensation paid in Illinois; Limited exceptions; When am I not required to withhold; Form IL-W-6 | Illinois Department of Revenue |
| S10 | KW-100 - residents working in other states; nonresidents | Specific Withholding Situations | Kansas Department of Revenue |
| S11 | Louisiana DOR Withholding page (Wayback copy) | Withholding | Louisiana Department of Revenue |
| S12 | 830 CMR 62B.2.1 Withholding of Taxes on Wages and Other Payments | (4)(a)1, (8), (9)(a)-(b); page dated 06/05/2026 | Massachusetts Department of Revenue (Massachusetts Register) |
| S13 | 36 MRSA 5217-A credit for income tax paid to other jurisdictions | 36 MRSA 5217-A(1) | Maine Legislature |
| S14 | 35 Miss. Admin. Code Part III (Income and Franchise), Subpart 11 Withholding and Subpart 2 (gross income) | 35.III.11 Ch.02 (101 supplemental), Ch.03 (exclusions: agricultural, domestic, ministers), Ch.07 (101-102 no-liability certificate), Ch.09 (resident/nonresident), Ch.11 (62-405 monthly if > 300/month; 62-400 quarterly), Ch.13 (corrections), Ch.15 (W-2 Jan 31 or 30 days after termination), Ch.16 (tables; computer formula); 35.III.2 (IRC 125/127/129; 27-7-16 deferrals) | Mississippi Department of Revenue (filed with Secretary of State) |
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
| S41 | Montana DOR: North Dakota Reciprocity Agreement | page | Montana Department of Revenue |
| S42 | North Dakota Tax: Income Tax Withholding (Reciprocity) | Reciprocity | ND Office of State Tax Commissioner |
| S43 | NJ Division of Taxation: PA/NJ Reciprocal Income Tax Agreement | page text | NJ Division of Taxation |
| S44 | Ohio Dept of Taxation: Employer Withholding FAQ (exempt compensation list) | exempt-from-withholding list | Ohio Dept of Taxation |
| S45 | Pennsylvania PIT Guide: Income Subject to Tax Withholding (Reciprocal Agreements) | Reciprocal Agreements | Pennsylvania DOR |
| S46 | Virginia Tax: Reciprocity | page text | Virginia Dept of Taxation |
| S47 | Vermont Withholding page: out-of-state employers 30-day rule | Withholding (employers) | Vermont Department of Taxes |
| S48 | Wisconsin DOR Publication 121 (01/26) Reciprocity | parts 2-5 | Wisconsin DOR |
| S49 | West Virginia TSD 381 Withholding Information for Employers (Rev. Sep 2025) | withholding not required list | WV Tax Division |
| S50 | Arkansas DFA Withholding Tax Employer's Instructions (Effective 01/01/2026, Revised 4/27/26) | Introduction; Supplemental Wages; Nonresident Employees; Texarkana Residents | Arkansas Department of Finance and Administration |
| S51 | California EDD DE 44 Employer Guide Rev. 52 (4-26): Wages in Another State; Interstate Reciprocal Coverage Elections; nonresident apportionment; multistate … | p.78 (PDF p.86) Wages in Another State + Interstate Reciprocal Coverage Elections; nonresident table (PIT); New Employee Registry | California EDD |
| S52 | Idaho State Tax Commission - Income you don't have to withhold on | exceptions list | Idaho State Tax Commission |
| S53 | Illinois DOR Publication 130 (R-02/26) Who is Required to Withhold Illinois Income Tax: 'When is compensation paid in Illinois' (localization rules 1-4, … | pp.3-5 When is compensation paid in Illinois, rules 1-4; examples | Illinois Department of Revenue |
| S54 | Louisiana Register Vol. 52 No. 3 (2026-03-20), Rule 2603#037: Mobile Workforce Exemption (LAC 61:I.1923), adopted | LAC 61:I.1923 A.2.a, A.2.d (repealed), C.1.a, C.1.b.i, C.2; LR 52:358 | Louisiana Department of Revenue, Tax Policy and Planning Division (published … |
| S55 | Louisiana Act 382 of the 2025 Regular Session (HB 567, enrolled): R.S. 47:112.2(A) and 47:248(B)(1)(a) mobile workforce exemption 30 days; R.S. … | Sec. 1 (R.S. 47:112.2(A), 47:248(B)(1)(a)); Sec. 2 (repeal of 47:248(B)(1)(d)); Sec. 3 (income tax periods beginning on or after 2026-01-01); Sec. 4 (effective on signature; bill page: effective 2025-06-20) | Louisiana Legislature |
| S56 | 2026 Withholding Tables instruction 3 (nonresident employees) and 36 MRSA 5142(8-B) | 36 MRSA 5142(8-B)(A); booklet instruction 3 | Maine Legislature; Maine Revenue Services |
| S57 | Minnesota Income Tax Withholding Instruction Booklet and Tax Tables 2026 (wh-inst-26): computer formula, deposits, returns, W-2 | pp. 3-12 and p. 34 Computer Formula | Minnesota Department of Revenue |
| S58 | Mississippi Pub 89-700-25-1 (Rev. 07/25) - Treatment of Residents and Nonresidents; reciprocity search | Instructions sec. 5 (a)-(d) | Mississippi Department of Revenue |
| S59 | NDCC chapter 57-38 Income tax (57-38-30.3, 57-38-59, 57-38-59.1, 57-38-59.3) | 57-38-30.3(1)(g),(2); 57-38-59(1)-(4); 57-38-59.1; 57-38-59.3 | ND Legislative Council |
| S60 | NY DTF TSB-M-06(5)I Application of the Convenience of the Employer Test to Telecommuters and Others (2006-05-15), quoting 20 NYCRR 132.18(a) | pp.1-2; 20 NYCRR 132.18(a) quoted; bona fide employer office factors | NY State Dept of Taxation and Finance |
| S61 | Utah Pub 14 Rev. 04/26 - nonresidents working temporarily in Utah; residents working outside Utah | Employee Withholding Exclusions; Who must withhold | Utah State Tax Commission |
| S62 | Connecticut DRS Special Notice 2018(9.1) (convenience of employer test) | Convenience of the Employer Test; 2018 Pub. Act 49 sec.20 | Connecticut DRS |
| S63 | 30 Del. C. 1121-1124 Nonresident individuals: tax and Delaware-source income | 30 Del. C. 1121, 1122, 1124(b)(1) | Delaware General Assembly (Delaware Code Online) |
| S64 | 2026 Nebraska Circular EN - nonresident employees (Wayback copy) | p.6 Nonresident Employees; Neb. Rev. Stat. 77-2733(8) | Nebraska Department of Revenue |
| S65 | NJ Convenience of the Employer Sourcing Rule FAQ | Who does the rule apply to | NJ Division of Taxation |
| S66 | 61 Pa. Code 109.8 Earnings of nonresident employes or casual employes and officers | 109.8 (amended 1999-12-11, 29 Pa.B. 6249); site current through 56 Pa.B. 5370 (2026-08-08) | Pennsylvania Code & Bulletin (PA DOR regulation) |
| S67 | Missouri Employer's Tax Guide Form 4282 (Revised 03-2026, published Dec 2025) - 2026 withholding formula, filing frequencies, due dates, W-2/MO W-3 | Sections 4, 7, 8, 9, 10, 11, 12, 21; 2026 Withholding Tax Formula pp.12-13 | Missouri Department of Revenue |
| S68 | ADOR 30-Day Safe Harbor Rule page (Act 2025-334) | whole page | Alabama Department of Revenue |
| S69 | 49 U.S.C. 14503 Withholding State and local income tax by certain carriers (US Code 2024 ed., GPO govinfo) | 14503(a)(1), (b)(1)-(3), (c) | US Congress / GPO |
| S70 | 49 U.S.C. 11502 Withholding State and local income tax by rail carriers (US Code 2024 ed., GPO govinfo) | 11502(a)-(b) | US Congress / GPO |
| S71 | 49 U.S.C. 40116(f) Pay of air carrier employees (US Code 2024 ed., GPO govinfo) | 40116(f)(1)-(3) | US Congress / GPO |
| S72 | 46 U.S.C. 11108 Taxes (seamen) (US Code 2024 ed., GPO govinfo) | 11108(a), (b) | US Congress / GPO |
| S73 | 4 U.S.C. 114 Limitation on State income taxation of certain pension income (United States Code, 2024 edition, govinfo) | 4 U.S.C. 114(a)-(b) | US Congress / GPO (govinfo) |
| S74 | Hawaii Booklet A sections 10 and 13 - nonresident employees (Wayback copy) | Section 10(a); Section 13 Form HW-6 | Hawaii Department of Taxation |
| S75 | Montana Guide: nonresident withholding and 30-day exemption | Withholding from Nonresidents; Thirty-Day Nonresident Wage Withholding Exemption | Montana Department of Revenue |
| S76 | NM TRD FYI-104 (Rev. 11/2025) notes on nonresidents and other-state tax | Who Must Withhold Note 2; Special Situations | New Mexico Taxation and Revenue Department |
| S77 | 50 U.S.C. 4001 Residence for tax purposes (SCRA sec. 511, as amended by Pub. L. 115-407 (2018) and Pub. L. 117-333 (2023)) (US Code 2024 ed.) | 4001(a)(1)-(3), (b), (c) | US Congress / GPO |
| S78 | Alaska Employment Security Tax Employer Handbook (taxbook.pdf, PDF modified 2025-05-05) | pp. 6-25 (employer, multistate, TQ01, wage base, employee contribution, records, excluded employment, wages, retirement/125/fringe, rates) | Alaska DOLWD Employment Security Tax |
| S79 | Code of Alabama 1975 Sec. 25-4-16 (wages, 8,000 USD taxable base, other-state employment counted) and Sec. 25-4-54 (experience-rated contributions, shared cost) | 25-4-16(b)(1); 25-4-54(a),(f) | Alabama Legislature (ALISON Code of Alabama) |
| S80 | Conn. Gen. Stat. 31-222(b) UI taxable wages (indexed wage base; other-state wage credit) | Sec. 31-222(b)(1)(A)(v)-(vi) | Connecticut General Assembly |
| S81 | 19 Del. C. ch. 33 subch. I Unemployment Compensation - definitions (3302): taxable wage base, localization, exclusions | 19 Del. C. 3302(12)(H)-(I), (15)(A)-(N), (28)(A)(vii)-(x), (28)(B) | Delaware General Assembly (Delaware Code Online) |
| S82 | Florida DOR Employer Guide to Reemployment Tax (RT-800002, R. 03/25) | pp.2-3 liability; pp.8-11 RT-6, wage base, annual option, taxable/exempt wages, BLS-3020, RT-6EW, E-Verify | Florida Department of Revenue |
| S83 | DLIR UI Handbook for Employers (web edition) | I Contributions: Registration; Quarterly Wage, Contribution and E&T Assessment Report; Taxable wages; Penalties; SIDES | Hawaii DLIR Unemployment Insurance Division |
| S84 | Iowa Administrative Code 871 chapter 23 Employer's contribution and charges (IAC 3/4/26) | 871-23.1(5),(17),(18); 23.5; 23.6(1)-(4); 23.8(1),(2),(5); 23.13; 23.24 | Iowa Workforce Development (published by Iowa Legislature) |
| S85 | Idaho Department of Labor - Unemployment Insurance Tax Information Handbook for Businesses (rev. 2025-11-05) | Who must pay; quarterly reports TX20/TX26/TX20C; standard rate; taxable wage base; corporate officers; claiming wages in another state; exempt services | Idaho Department of Labor (Wayback id_ 20260113182918) |
| S86 | KRS 341.030(7)(a) multistate wage-base credit (covered employment under another state's law) | KRS 341.030(7)(a) last sentence | Kentucky Legislative Research Commission |
| S87 | 26 MRSA 1043 Employment Security Law definitions (wages, employment, exclusions, localization) | 1043(1),(9),(11) incl. A-2, A-3, E-F localization, exclusions; (19) | Maine Legislature, Office of the Revisor of Statutes |
| S88 | Michigan Employment Security Act sec. 44 (MCL 421.44) remuneration, wages and taxable wage limit | MCL 421.44(1)-(5) | Michigan Legislature |
| S89 | CT Paid Leave Authority Guide for Employers (fact sheet updated October 2024) | Eligibility footnote | Connecticut Paid Leave Authority |
| S90 | D.C. Code 32-541.01 Universal Paid Leave - definitions (covered employee, wages) | 32-541.01(3),(22) | Council of the District of Columbia |
| S91 | 19 Del. C. ch. 37 Healthy Delaware Families Act (Delaware Paid Leave): coverage, contributions, benefits | 19 Del. C. 3701(3),(6),(7),(24); 3703; 3704(a); 3705(a)-(l); 3714 | Delaware General Assembly (Delaware Code Online) |
| S92 | Md. Code, Labor and Employment 8-202 (UI covered employment: localization) | LE 8-202(b)-(d) | Maryland General Assembly |
| S93 | Maine DOL PFML Employer FAQ (July 2026): wage definition, locality, tax treatment, W-2 Box 14 | FAQ 5, 6, 9-15, 17, 24, 26-27 | Maine Department of Labor, Paid Family and Medical Leave |
| S94 | ORS chapter 657B Paid Family and Medical Leave Insurance (2025 Edition) | ORS 657B.150(1)-(5); 657B.175 | Oregon Legislature (ORS) |
| S95 | RIGL 28-39-2 TDI definitions (employment = chapter 42 definition) | 28-39-2(14) | Rhode Island General Assembly |
| S96 | RCW 50A.05.010(8) Washington Paid Family and Medical Leave: definition of employment (localization), effective until 2027-06-30 (Wayback copy 2026-04-23) | 50A.05.010(8)(a)(i)-(ii), (24); a version effective 2027-06-30 also printed | Washington State Legislature |
| S97 | DOL OUI memo to State UI Directors: Spirit Airlines, reminder to review localization of work guidance (undated; Acting Deputy Administrator S. Simonetta) | full text (2 pp.) | US DOL ETA Office of Unemployment Insurance |
| S98 | DOL ETA Unemployment Insurance Program Letter No. 20-04 Localization of Work Provisions (2004-05-10) | paras 1-7; Attachment I Localization of Work Provisions (attachment not held) | US DOL Employment and Training Administration |
| S99 | 26 U.S.C. 3306(b)(1) FUTA wages: 7,000 per employer per calendar year; successor rule (US Code 2024 ed.) | 3306(b)(1) | US Congress / GPO |
| S100 | K.S.A. 44-703 Employment security law definitions (employer coverage, employment exclusions, wages, taxable wage base) | (h)(1),(h)(5), (i)(4)(C),(F),(I),(J),(K),(N),(O),(T),(W), (o), (o)(1), (o)(2)(A)-(C), (jj), (kk) | Kansas Office of the Revisor of Statutes |
| S101 | Mississippi Employment Security Law (MDES compilation of Miss. Code Title 71 ch.5, web edition 2024-02-15): coverage 71-5-11, contributions 71-5-351, taxable … | 71-5-11 I(6),(7),(8)-(10),(15)(b)-(h); 71-5-351(1)-(3); 71-5-353(4) | Mississippi Department of Employment Security (compilation of statute) |
| S102 | G.S. 96-9.3 Determination of taxable wages (UI wage base indexation) | 96-9.3(a),(b) | NC General Assembly (General Statutes, official host ncleg.gov) |
| S103 | NDCC chapter 52-04 Contributions and payments by employers (UI) | 52-04-01, 52-04-03, 52-04-06, 52-04-11 | ND Legislative Council |
| S104 | NDOL Employer's Guide to Unemployment Insurance (Revised 9/11/2025): registration, wage reports, deadlines, multistate, wage-base credit | pp.6-7, 11-13, 16 | Nebraska Department of Labor |
| S105 | NH RSA chapter 282-A Unemployment Compensation: 282-A:9 (employment, localization, exclusions), 282-A:15 (wages), 282-A:69 (payment of contributions) | RSA 282-A:9 I, IV; 282-A:15 I-II; 282-A:69 I | NH General Court |
| S106 | NRS chapter 612 Unemployment Compensation, wayback snapshot 2026-10-19 | NRS 612.080, 612.090, 612.095, 612.105, 612.118, 612.119, 612.121, 612.130, 612.133, 612.190, 612.540, 612.545, 612.606 | Nevada Legislature (Legislative Counsel Bureau) |
| S107 | Employment Security Act of 1980 - 40 O.S. 1-201(48) taxable wages; 1-223 applicable percentages; 3-102 contributions | 40 O.S. 1-201(48); 1-223 (Laws 2025 c. 140, eff. 2025-11-01); 3-102(A)-(C) | Oklahoma Legislature (Oklahoma Statutes, Title 40) |
| S108 | ORS chapter 657 Unemployment Insurance (2025 Edition): 657.035, 657.095, 657.435, 657.462 | ORS 657.035(1),(4); 657.095(1)-(2); 657.435; 657.462 Table A | Oregon Legislature (ORS) |
| S109 | RIGL 28-42-3 Definitions (wages, taxable wage base, other-state employment) | 28-42-3 'Wages' (i) | Rhode Island General Assembly |
| S110 | SC Code Title 41 ch. 27 (Employment Security Law definitions): 41-27-260, 41-27-265, 41-27-380, 41-27-410 | 41-27-260 exempted employment; 41-27-265 corporate officers; 41-27-380(A)-(B) wages and taxable wage base; 41-27-410 DACA; 41-27-230(5) agricultural and domestic-service coverage thresholds | South Carolina Legislature |
| S111 | SDCL Title 61 Reemployment Assistance (unemployment compensation), full official text | SDCL 61-1-17, 61-1-19, 61-1-46, 61-5-24, 61-5-25, 61-5-25.7, 61-5-28, 61-5-28.1, 61-5-29 | South Dakota Legislature (Legislative Research Council) |
| S112 | 21 V.S.A. 1321(b)(2) wages for other-state employment count toward the Vermont base | 1321(b)(1)-(2) | Vermont General Assembly (Wayback copy 2026-04-18) |
| S113 | W. Va. SB 841 (2024 Regular Session) enrolled committee substitute - amends 21A-1A-28 Wages | 21A-1A-28(b)(1),(d) | West Virginia Legislature |
| S114 | W.S. 27-3-102(a)(xviii) definition of wage for UI contributions (taxable wage base and exclusions); 27-3-303(a) statewide average annual wage | 27-3-102(a)(xviii)(A)-(W); 27-3-303(a); 27-3-306(d)(i) | Wyoming Legislature |
| S115 | Montana DLI UI Division Employer Handbook (Revised January 2025; PDF modified 2026-03-04) | Sections 2-6 (special classes table pp. 5-8; multistate test p. 9; excess wages p. 14; payments and reports p. 16; penalties p. 17) | Montana Department of Labor and Industry, Unemployment Insurance Division |
| S116 | DOL OUI Comparison of State UI Laws 2023 Ch.2 Financing, Employee Contributions | Ch.2 Employee Contributions | US DOL ETA OUI |
| S117 | Ward v. United Airlines, Inc. (Cal. Supreme Court, S248702, 2020-06-29), 9 Cal.5th 732: geographic reach of Labor Code 226 | Part III; Part IV answers (1)-(2); Lab. Code 226; Wage Order 9 sec.1(E) | Supreme Court of California |
| S118 | General Instructions for Forms W-2 and W-3 (2026): Boxes 15-20 State and local income tax information; Multiple forms; W-3 box 15 | Specific Instructions for Form W-2, Boxes 15 through 20; Multiple forms; Form W-3 Box 15, Boxes 16-19 | IRS |
| S119 | 42 U.S.C. 653a(b) National new-hire reporting: multistate employers and timing (US Code 2024 ed.) | 653a(b)(1)(B), (b)(2) | US Congress / GPO |
| S120 | 42 U.S.C. 666(b)(6)(A), (b)(9), (f) Income withholding: orders from another State (US Code 2024 ed.) | 666(b)(6)(A)(i)(I)-(V), (b)(9), (f) | US Congress / GPO |
| S121 | S. 1443 (119th Congress) Mobile Workforce State Income Tax Simplification Act of 2025, introduced text (GPO BILLS-119s1443is) | secs. 2(a)-(c), 3 | US Senate / GPO |
| S122 | H.R. 10271 (119th Congress) Mobile Workforce State Income Tax Simplification Act of 2026, introduced text (GPO BILLS-119hr10271ih) | secs. 1-3 | US House of Representatives / GPO |


## Fact index

Every value above with its key, effective period and register id.

| Key | Value | Effective | Register id |
|---|---|---|---|
| `al.nonres.safe_harbor.days` | 30 | from 2026-01-01 | US-ALS5-003 |
| `ga.nonres.threshold_amount` | 5,000 | from 2026-01-01 | US-GAS5-004 |
| `ga.nonres.threshold_percent` | 5 | from 2026-01-01 | US-GAS5-004 |
| `hi.nonres.exempt_days` | 60 | from 2026-01-01 | US-HIP51-002 |
| `ks.sui.wage_base.other_state_credit` | True | from 2026-01-01 | US-KSS5-020 |
| `mo.reciprocity.states` | none | from 2026-01-01 to 2026-12-31 | US-MOS5-001 |
| `ms.sui.wage_base.other_state_credit` | True | from 2011-01-01 | US-MSS5-011 |
| `mt.pit.nonresident.days_exemption` | 30 | from 2026-01-01 | US-MTP51-003 |
| `mt.reciprocity.states` | ND | from 2026-01-01 | US-MTP51-004 |
| `mt.sui.wage_base.other_state_credit` | False | from 2025-07-01 | US-MTS5-025 |
| `multi.ca.oman.rule` | Oman v. Delta Air Lines, Cal. S. Ct. S248726 (2020-06-29), Lab. Code 204 and 226: do not reach pay periods in which the employee works in CA only episodically and for less than a day at a time, unless the employee works primarily in CA in that period, or works primarily in no State and has the CA base of operations. Minimum-wage reach left undecided. | from 2020-06-29 | US-MULTIS5-019 |
| `multi.ca.ward.rule` | Ward v. United Airlines, Cal. S. Ct. S248702 (2020-06-29), Lab. Code 226: applies if the PRINCIPAL place of work is in CA (majority of working time); with no majority State, where CA is the base of work operations and some work is done in CA. Employer location, residence, place of pay receipt, taxes paid and a CBA are irrelevant. | from 2020-06-29 | US-MULTIS5-018 |
| `multi.convenience.ar.rule` | Not a convenience State: Act 1019 of 2021 (SB 484), in force from TY2021 - a nonresident works in AR only when physically located in AR | from 2021-01-01 | US-ARS5-006 |
| `multi.convenience.ct.rule` | From tax years beginning 2019-01-01 CT applies the resident State's convenience test to nonresidents working for a CT employer | from 2019-01-01 | US-MULTI-020 |
| `multi.convenience.de.rule` | 30 Del. C. 1124(b)(1): compensation is DE-source if attributable to employment in DE and not required to be performed elsewhere; working from home does not qualify for the PIT-SCW exclusion | from 2026-01-01 | US-DES5-004 |
| `multi.convenience.default` | Everywhere else wages follow the place of physical performance | from 2026-01-01 | US-MULTIQ1-001 |
| `multi.convenience.ne.rule` | From 2025: services performed outside NE for the nonresident's convenience are NE-sourced (77-2733(8)(c)) | from 2025-01-01 | US-NEP51-002 |
| `multi.convenience.nj.rule` | From 2023 NJ applies the convenience rule against residents of States that apply one (DE, NE, NY; CT by reciprocal law); PA residents excluded by the reciprocal agreement | from 2023-01-01 | US-MULTI-012 |
| `multi.convenience.ny.rule` | 20 NYCRR 132.18(a): nonresident allocates by NY working days / total working days; days outside NY count only if worked of NECESSITY; home-office days are NY days unless the home is a bona fide employer office | from 2006-05-15 | US-MULTIS5-013 |
| `multi.convenience.pa.rule` | 61 Pa. Code 109.8: same necessity test as NY; PA reciprocal agreements prevail | from 1999-12-11 | US-MULTIS5-014 |
| `multi.futa.wage_base.scope` | FUTA 7,000 counts remuneration paid by the employer in the calendar year across all States: one base per employer, not per State; successor carry-over | from 2026-01-01 | US-MULTIS5-009 |
| `multi.iwo.governing_law` | When an employer receives an income withholding order issued by another State, the employer shall apply the income withholding law of the State of the obligor's principal place of employment in determining the employer's fee for processing an income withholding order; the maximum amount permitted to be withheld from the obligor's income; the time periods within which the employer must implement the income withholding order and forward the child support payment; the priorities for withholding and allocating income withheld for multiple child support obligees; and any withholding terms or conditions not specified in the order | from 2026-01-01 | US-MULTIS5-007 |
| `multi.iwo.remittance_business_days` | 7 | from 2026-01-01 | US-MULTIS5-007 |
| `multi.military_spouse.rule` | A military spouse present in a State solely to be with the servicemember under military orders neither loses nor acquires residence or domicile; the spouse's income for services performed in that State is not income for services performed or from sources within that State if the spouse is not a resident of it; for any taxable year the spouse may elect the residence of the servicemember, the spouse's own residence or the permanent duty station (50 U.S.C. 4001(a)(2), (c)). Payroll effect: on the employee's State certificate of nonresidence, stop work-State withholding. | from 2018-12-31 | US-MULTIS5-005 |
| `multi.mobile_workforce_bill.house` | H.R. 10271 (introduced 2026-09-03, House Judiciary): DRAFT, NOT ENACTED - do not model | from 2026-01-01 | US-MULTIS5-025 |
| `multi.mobile_workforce_bill.senate` | S. 1443 (introduced 2025-04-10, Senate Finance): DRAFT, NOT ENACTED - do not model | from 2026-01-01 | US-MULTIS5-020 |
| `multi.newhire.designated_state` | A multistate employer reporting electronically may send all new-hire reports to ONE designated State in which it has employees, after notifying HHS in writing | from 2026-01-01 | US-MULTIS5-006 |
| `multi.nonresident.ar.allocation_rule` | No threshold: apportioned by AR working days (HB1116 of 2025, 15 days / 2,500, died) | from 2026-01-01 | US-ARP51-002 |
| `multi.nonresident.az.threshold_days` | 60 | from 2026-01-01 | US-MULTIB5-401 |
| `multi.nonresident.ca.allocation_rule` | No threshold: working-day ratio from day 1 (commission pay: volume ratio) | from 2026-01-01 | US-MULTIS5-010 |
| `multi.nonresident.co.allocation_rule` | No threshold: apportioned by days worked in CO (a day counts if majority of working time is in CO) | from 2026-01-01 | US-COP51-002 |
| `multi.nonresident.ct.threshold_days` | 15 | from 2026-01-01 | US-CTP10-001 |
| `multi.nonresident.id.threshold_amount` | 1,000 | from 2026-04-12 | US-IDB5-401 |
| `multi.nonresident.il.threshold_days` | 30 | from 2026-01-01 | US-MULTIS5-023 |
| `multi.nonresident.la.employer_start_rule` | Begin withholding and report on Form L-1 beginning in the period in which the 31st day fell | from 2026-03-20 | US-LAS5-002 |
| `multi.nonresident.la.threshold_days` | 30 | from 2026-01-01 | US-MULTIS5-021 |
| `multi.nonresident.me.threshold_amount` | 3,000 | from 2026-01-01 | US-MEP52-003 |
| `multi.nonresident.me.threshold_days` | 12 | from 2026-01-01 | US-MEP52-003 |
| `multi.nonresident.mn.threshold_amount` | 15,300 | from 2026-01-01 to 2026-12-31 | US-MNS5-010 |
| `multi.nonresident.ms.allocation_rule` | Earnings ratio; principal place of employment in MS -> total wages unless the other State requires withholding | from 2025-07-01 | US-MSP52-002 |
| `multi.nonresident.ms.threshold_rule` | Day 1 by earnings ratio, except no withholding when annual MS earnings will be below the standard deduction for the filing status | from 2026-01-01 | US-MSS5-019 |
| `multi.nonresident.nd.threshold_rule` | Mobile workforce exclusion (57-38-59.3): present 20 days or fewer, no other ND income, home State reciprocal exclusion or no income tax; not athletes, entertainers, persons of prominence, construction workers, key employees | from 2026-01-01 | US-NDS5-004 |
| `multi.nonresident.ny.allocation_rule` | No threshold: NY working days / total working days with the convenience test | from 2006-05-15 | US-MULTIS5-013 |
| `multi.nonresident.ut.threshold_days` | 20 | from 2026-01-01 | US-UTP51-002 |
| `multi.nonresident.vt.threshold_days` | 30 | from 2026-01-01 | US-VTP52-003 |
| `multi.nonresident.wv.threshold_days` | 30 | from 2026-01-01 | US-MULTI-015 |
| `multi.payslip.reach.default` | Default: the pay-statement statute of the work-location State (no other State reach rule researched); payslip in English (US-OWN-006) | from 2020-06-29 | US-MULTIS5-018 |
| `multi.pfml.coverage_test.ct` | Follows UI localization: employees for whom CT UI and payroll taxes are paid are working in CT | from 2026-01-01 | US-CTS5-035 |
| `multi.pfml.coverage_test.dc` | More than 50% of work time in DC, or DC-based with substantial DC time and not more than 50% elsewhere; not by residence | from 2026-01-01 | US-DCS5-007 |
| `multi.pfml.coverage_test.de` | Follows the primary DE worksite (3701(6)a), not UI localization | from 2025-01-01 | US-DES5-012 |
| `multi.pfml.coverage_test.default` | Key the PFML/SDI premium State to sui_state unless the State annex proves otherwise (WA, CT, ME, OR, MD, RI proven; DC and DE differ) | from 2026-01-01 to 2027-06-30 | US-MULTIS5-024 |
| `multi.pfml.coverage_test.md` | FAMLI covers employees in positions localized in MD (LE 8-202 UI localization); contributions start 2027-01-01 (US-MDS5-014) | from 2026-01-01 | US-MDS5-019 |
| `multi.pfml.coverage_test.me` | Follows the Maine UI localization test (FAQ 6) | from 2025-01-01 | US-MES5-025 |
| `multi.pfml.coverage_test.or` | Follows UI localization (ORS 657B.175); employer size counts out-of-state employees too (US-ORS5-013) | from 2023-01-01 | US-ORS5-014 |
| `multi.pfml.coverage_test.ri` | TDI follows the UI localization test (28-39-2 uses the chapter 42 definition) | from 2026-01-01 | US-RIS5-016 |
| `multi.pfml.coverage_test.wa` | Follows the UI localization test (RCW 50A.05.010(8)) | from 2026-01-01 to 2027-06-30 | US-MULTIS5-024 |
| `multi.pit.sourcing.general` | No general federal rule: each State taxes residents on all wages (credit at assessment for tax paid to the work State) and nonresidents on wages for services performed in the State; federal limits only for transport workers and military spouses. 4 U.S.C. 114 is retirement income only, not wages. | from 2026-01-01 | US-MULTIQ1-001 |
| `multi.reciprocity.ar.partners` | none (zero hits for reciprocity in the AR instructions) | from 2025-01-01 | US-ARP52-001 |
| `multi.reciprocity.az.unilateral` | AZ exempts residents of CA, IN, OR, VA on Form WEC (they can claim the AZ credit); one-way - an AZ resident working in CA is withheld by CA | from 2026-01-01 | US-MULTIB5-401 |
| `multi.reciprocity.ct.partners` | none | from 2026-01-01 | US-CTP10-001 |
| `multi.reciprocity.dc.certificate` | D-4A | from 2026-01-01 | US-MULTI-016 |
| `multi.reciprocity.dc.nonresident_exempt` | D.C. Code 1-206.02(a)(5): DC may not tax any nonresident's personal income; DC withholding stops for ANY nonresident (D-4A: domicile outside DC and under 183 days) | from 2026-01-01 | US-DCP51-006 |
| `multi.reciprocity.dc.partners` | MD, VA (from the partner side; DC taxes no nonresident at all) | from 2026-01-01 | US-MULTI-016 |
| `multi.reciprocity.de.partners` | none | from 2026-01-01 | US-MULTI-019 |
| `multi.reciprocity.ga.partners` | none | from 2026-01-01 | US-GAP52-003 |
| `multi.reciprocity.ia.certificate` | IA 44-016 (IL resident in IA); IL-W-5-NR (IA resident in IL) | from 2026-01-01 | US-MULTI-018 |
| `multi.reciprocity.ia.partners` | IL | from 2026-01-01 | US-MULTI-018 |
| `multi.reciprocity.il.certificate` | IL-W-5-NR | from 2026-02-01 | US-ILP51-001 |
| `multi.reciprocity.il.partners` | IA, KY, MI, WI | from 2026-02-01 | US-ILS5-014 |
| `multi.reciprocity.il.partners` | IA,KY,MI,WI | from 2026-01-01 to 2026-01-31 | US-MULTIS5-023 |
| `multi.reciprocity.in.certificate` | WH-47 | from 2026-01-01 | US-IN-002 |
| `multi.reciprocity.in.partners` | KY, MI, OH, PA, WI (county tax still withheld) | from 2026-01-01 | US-IN-002 |
| `multi.reciprocity.ky.certificate` | 42A809 | from 2026-01-01 | US-MULTI-009 |
| `multi.reciprocity.ky.partners` | IL, IN, MI, OH (unless 20% S-corp shareholder-employee), VA (daily commuters only), WV, WI | from 2026-01-01 | US-MULTI-009 |
| `multi.reciprocity.md.certificate` | MW507 | from 2026-01-01 | US-MULTI-008 |
| `multi.reciprocity.md.partners` | DC, PA, VA, WV (not for abode in MD > 6 months and 183+ days, except WV) | from 2026-01-01 | US-MULTI-008 |
| `multi.reciprocity.me.partners` | none in force (agreements authorised by statute, none identified) | from 2026-01-01 | US-MEP52-005 |
| `multi.reciprocity.mi.certificate` | per MI Guide 446 (form not named in the row) | from 2026-01-01 | US-MULTI-010 |
| `multi.reciprocity.mi.partners` | IL, IN, KY, MN, OH, WI | from 2026-01-01 | US-MULTI-010 |
| `multi.reciprocity.mn.certificate` | MWR (yearly; copies to MN DOR by Mar 31) | from 2026-01-01 | US-MULTI-013 |
| `multi.reciprocity.mn.partners` | MI, ND (employee returns home at least monthly) | from 2026-01-01 | US-MULTI-013 |
| `multi.reciprocity.mt.certificate` | MW-4 (annual renewal) | from 2026-01-01 | US-MTP51-004 |
| `multi.reciprocity.nc.partners` | none | from 2026-01-01 | US-NCP51-002 |
| `multi.reciprocity.nd.certificate` | NDW-R (yearly, by Feb 28 or within 30 days) | from 2026-01-01 | US-MULTI-014 |
| `multi.reciprocity.nd.partners` | MN, MT | from 2026-01-01 | US-MULTI-014 |
| `multi.reciprocity.nj.certificate` | NJ-165 (PA resident in NJ); REV-419EX (NJ resident with PA employer) | from 2026-01-01 | US-MULTI-011 |
| `multi.reciprocity.nj.partners` | PA (compensation only) | from 2026-01-01 | US-MULTI-011 |
| `multi.reciprocity.oh.certificate` | IT 4 (combined certificate) | from 2026-01-01 | US-MULTI-005 |
| `multi.reciprocity.oh.partners` | IN, KY, MI, PA, WV | from 2026-01-01 | US-MULTI-005 |
| `multi.reciprocity.pa.certificate` | REV-419 | from 2026-01-01 | US-MULTI-007 |
| `multi.reciprocity.pa.partners` | IN, MD, NJ, OH, VA, WV | from 2026-01-01 | US-MULTI-007 |
| `multi.reciprocity.va.certificate` | VA certificate (not named in the row; VA annex) | from 2026-01-01 | US-MULTI-004 |
| `multi.reciprocity.va.partners` | DC, KY (daily commuters), MD, PA, WV | from 2026-01-01 | US-MULTI-004 |
| `multi.reciprocity.vt.partners` | none (four official withholding texts, none lists one) | from 2026-01-01 | US-VTP52-003 |
| `multi.reciprocity.wi.certificate` | W-220 | from 2026-01-01 | US-MULTI-006 |
| `multi.reciprocity.wi.partners` | IL, IN, KY, MI | from 2026-01-01 | US-MULTI-006 |
| `multi.reciprocity.wv.certificate` | WV/IT-104 | from 2026-01-01 | US-MULTI-015 |
| `multi.reciprocity.wv.partners` | KY, MD, OH, PA, VA | from 2026-01-01 | US-MULTI-015 |
| `multi.resident_credit.ar.level` | assessment | from 2021-01-01 | US-ARS5-006 |
| `multi.resident_credit.az.level` | assessment | from 2026-01-01 | US-AZWH-003 |
| `multi.resident_credit.dc.level` | assessment | from 2026-01-01 | US-DCP51-007 |
| `multi.resident_credit.me.level` | assessment | from 2026-01-01 | US-MEP52-004 |
| `multi.resident_credit.ms.level` | assessment | from 2026-01-01 | US-MSS5-019 |
| `multi.resident_credit.oh.level` | assessment | from 2025-01-01 | US-OHP52-004 |
| `multi.resident_credit.ok.level` | assessment | from 2025-01-01 | US-OKP52-002 |
| `multi.resident_credit.ri.level` | assessment | from 2025-01-01 | US-RIP52-002 |
| `multi.resident_credit.sc.level` | assessment | from 2026-01-01 | US-SCR3-004 |
| `multi.resident_out_of_state.co.withholding_rule` | Withhold CO on all wages except wages for services in another State that itself requires withholding | from 2026-01-01 | US-COP51-002 |
| `multi.resident_out_of_state.ct.withholding_rule` | All wages subject; where the employer must withhold for the other jurisdiction, CT tax is prorated and only the excess remitted | from 2026-01-01 | US-CTP10-001 |
| `multi.resident_out_of_state.ga.withholding_rule` | No GA withholding if the other State requires withholding; otherwise withhold GA | from 2026-01-01 | US-GAS5-004 |
| `multi.resident_out_of_state.il.withholding_rule` | IL resident working entirely in another State whose compensation is subject to that State's withholding: no IL withholding (credit on the return) | from 2026-02-01 | US-ILS5-014 |
| `multi.resident_out_of_state.ks.withholding_rule` | KS tax on total wages less the other State's required withholding (example 250 - 130 = 120); zero if the other State's withholding is higher | from 2024-07-01 | US-KSP51-003 |
| `multi.resident_out_of_state.la.withholding_rule` | LA residents working in another State may be subject to LA withholding if those wages are not subject to withholding there | from 2026-01-01 | US-LAP51-001 |
| `multi.resident_out_of_state.ma.withholding_rule` | MA amount minus the other jurisdiction's amount (credit method, 830 CMR 62B.2.1(9)(b)); employer without MA office may withhold for MA residents as a convenience | from 2026-01-01 | US-MAS5-023 |
| `multi.resident_out_of_state.ms.withholding_rule` | Withhold MS on total wages except to the extent withheld for another State; commuter to a no-income-tax State is withheld MS on total wages (credit at assessment). MS is not a credit-only State. | from 2026-01-01 | US-MSS5-004 |
| `multi.resident_out_of_state.nc.withholding_rule` | Withhold on all wages wherever earned, except no NC withholding on wages for services in a State that requires the employer to withhold | from 2026-01-01 | US-NCP51-002 |
| `multi.resident_out_of_state.ny.withholding_rule` | Withhold NYS tax for NY residents even if wages are earned outside NY | from 2026-01-01 | US-NY-013 |
| `multi.resident_out_of_state.oh.withholding_rule` | Every employer with an office or transacting business in Ohio withholds on residents (resident credit IT RC at assessment) | from 2026-10-29 | US-OHP52-006 |
| `multi.resident_out_of_state.ok.withholding_rule` | Residents are withheld on services within or without Oklahoma (68 O.S. 2385.1 employee definition) | from 2023-07-01 | US-OKS5-010 |
| `multi.resident_out_of_state.sc.withholding_rule` | Withhold for the other State; if that State has no income tax, withhold 100% SC (12-8-520(C)(1)) | from 2026-01-01 | US-SCR3-003 |
| `multi.resident_out_of_state.vt.withholding_rule` | Compute on the full payment, then reduce by tax withheld for the State where services were performed | from 2026-01-01 | US-VTP51-003 |
| `multi.resident_out_of_state.wi.withholding_rule` | Residents working outside WI: withholding on all wages; Minnesota special arrangement - no WI withholding if MN withholds | from 2026-01-01 | US-WIS5-011 |
| `multi.sui.employee_contribution_states` | AK, NJ, PA (only three States levy employee UI contributions; take 2026 rates from the State annexes) | from 2023-01-01 | US-FEDP52-006 |
| `multi.sui.localization.telecommuting` | UIPL 20-04 (2004, continuing) reissues the UIPL 291 interpretation with telecommuting examples | from 2004-05-10 | US-MULTIS5-016 |
| `multi.sui.localization_test` | One State covers the entire service with one employer, in order: (1) localized (entirely in the State, or out-of-state service incidental: temporary, transitory, isolated); (2) else some service in the base-of-operations State; (3) else some service in the State of direction or control; (4) else some service in the State of residence | from 2026-01-01 | US-MULTIS5-017 |
| `multi.sui.other_state_wage_credit.ak` | True | from 2026-01-01 | US-AKS5-005 |
| `multi.sui.other_state_wage_credit.al` | True | from 2026-01-01 | US-ALS5-009 |
| `multi.sui.other_state_wage_credit.ca` | True | from 2026-01-01 | US-MULTIS5-010 |
| `multi.sui.other_state_wage_credit.ct` | True | from 2025-01-01 | US-CTS5-016 |
| `multi.sui.other_state_wage_credit.de` | True | from 2026-01-01 to 2026-12-31 | US-DES5-010 |
| `multi.sui.other_state_wage_credit.fl` | True | from 2026-01-01 | US-FLS5-020 |
| `multi.sui.other_state_wage_credit.hi` | True | from 2026-01-01 | US-HIS5-012 |
| `multi.sui.other_state_wage_credit.ia` | False | from 2025-02-26 | US-IAS5-024 |
| `multi.sui.other_state_wage_credit.id` | conditional: only if tax was paid on them to that State (72-1349(1)) | from 2025-11-05 | US-IDS5-021 |
| `multi.sui.other_state_wage_credit.ky` | True | from 2022-03-24 | US-KYS5-018 |
| `multi.sui.other_state_wage_credit.me` | True | from 2026-01-01 | US-MES5-020 |
| `multi.sui.other_state_wage_credit.mi` | True | from 2016-01-01 | US-MIS5-010 |
| `multi.sui.reciprocal_coverage_election` | Where no test resolves the case, employer, employee and States may elect coverage of all service in one State (performance, residence or place of business); CA CUIC 602/603 | from 2026-01-01 | US-MULTIS5-010 |
| `multi.transport.air_carrier` | Residence State plus the State where more than 50% of carrier pay is earned (scheduled flight time) (49 U.S.C. 40116(f)) | from 2018-10-05 | US-MULTIS5-003 |
| `multi.transport.air_carrier.share_threshold` | 50 | from 2018-10-05 | US-MULTIS5-003 |
| `multi.transport.motor_carrier` | Employee with regularly assigned duties in 2+ States: taxable ONLY by the residence State/subdivision (49 U.S.C. 14503) | from 1996-01-01 | US-MULTIS5-001 |
| `multi.transport.rail` | Residence State/subdivision only (49 U.S.C. 11502) | from 2026-01-01 | US-MULTIS5-002 |
| `multi.transport.seamen` | Seamen's wages may not be withheld for State/local tax; multi-State vessel crew and pilots taxable only by the residence State (46 U.S.C. 11108) | from 2010-10-15 | US-MULTIS5-004 |
| `multi.ui_wage_report.routing` | UI quarterly wage report to the sui_state only (localization); State income-tax withholding returns to every State where withholding applies | from 2026-01-01 | US-MULTIS5-017 |
| `multi.w2.states_per_form` | 2 | from 2026-01-01 | US-MULTIS5-011 |
| `multi.wage_hour.overlay_rule` | FLSA does not excuse a higher State/municipal minimum wage, a lower maximum workweek or a stricter child-labour standard: apply the more protective standard of the place where the work is performed | from 2026-01-01 | US-MULTIS5-008 |
| `nc.sui.wage_base.other_state_credit` | True | from 2026-01-01 | US-NCS5-015 |
| `nd.sui.wage_base.other_state_credit` | True | from 2026-01-01 | US-NDS5-009 |
| `ne.pit.nonresident.duty_days` | 7 | from 2025-01-01 | US-NEP51-002 |
| `ne.sui.wage_base.other_state_credit` | True | from 2025-09-11 | US-NES5-011 |
| `nh.sui.wage_base.other_state_credit` | True | from 2026-01-01 | US-NHS5-007 |
| `nm.pit.nonresident.days_threshold` | 15 | from 2026-01-01 | US-NMP52-002 |
| `nv.sui.wage_base.other_state_credit` | True | from 2026-01-01 | US-NVS5-006 |
| `ok.pit.nonresident.quarterly_threshold` | 300 | from 2023-07-01 | US-OKS5-010 |
| `ok.sui.wage_base.other_state_credit` | True | from 2025-11-01 | US-OKS5-005 |
| `or.sui.wage_base.other_state_credit` | True | from 2026-01-01 | US-ORS5-015 |
| `ri.sui.wage_base.other_state_credit` | True | from 2026-01-01 | US-RIS5-013 |
| `sc.sui.wage_base.other_state_credit` | True | from 2015-01-01 | US-SCS5-014 |
| `sd.sui.wage_base.other_state_credit` | True | from 2026-01-01 | US-SDS5-002 |
| `vt.sui.wage_base.other_state_credit` | True | from 2012-01-01 | US-VTS5-010 |
| `wi.pit.nonresident.de_minimis` | 1,500 | from 2026-01-01 | US-WIS5-011 |
| `wv.sui.wage_base.other_state_credit` | True | from 2024-07-01 | US-WVS5-001 |
| `wy.sui.wage_base.other_state_credit` | True | from 2026-05-08 | US-WYS5-003 |
