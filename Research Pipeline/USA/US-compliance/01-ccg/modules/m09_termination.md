# Module 9: Termination & Irregular Payments

*Objective: To detail calculation and tax rules for non-standard payments.*

## 9.1 Termination Payments

### What are the different types of termination payments?

| Payment | Rule | Tax treatment | Source |
|---|---|---|---|
| Final regular wages | [[FACT:fed.final_pay.rule=No federal immediate final-pay rule; wages due by the regular payday; timing and vacation payout are state law]]. State timing: Table 9.1.1. | Regular wages | [US-FEDS5-025] |
| Accrued vacation / PTO | Payable only where State law or the employer's written policy makes it wages due (Module 8, Table 8.1.3) | Wages | Module 8 |
| Severance pay | Contractual or policy-based. No general federal severance entitlement is established from an official source. | Wages for FIT, FICA and FUTA (severance is wages) | [US-FEDS5-029] |
| Pay in lieu of WARN notice | WARN requires [[FACT:fed.warn.notice_days=60]] days' notice of a plant closing or mass layoff. Pay in lieu of the notice is wages. | Wages | [US-FEDS5-025] |
| Maine statutory severance | [[FACT:me.severance.mass_layoff=establishments with 100+ employees: one week pay per year of service, within one pay period after last day; 90 days notice]] | Wages | [US-MES5-010] |
| New Jersey mass-layoff severance | [[FACT:nj.term.warn.severance.weeks_per_year=1]] week of pay per year of service on a covered mass layoff | Wages | [US-NJS5-020] |

**Fixed-term contracts.** Employment is at will and a fixed term is a matter of contract; no federal or general State fixed-term regime exists. The expiry of the term is a separation: final wages follow Table 9.1.1, and any State separation notice below applies (Module 11, 11.3; [US-SDS5-010], [US-TNS5-012], [US-FEDS5-025]).

**Table 9.1.1: State final-pay timing (States with a verified rule).** Timing runs from the separation. Discharge and resignation differ in many States.

| State | Verified rule (parameter: value) | Register |
|---|---|---|
| Alaska (AK) | discharge, working days: [[FACT:ak.final_pay.discharge.working_days=3]]; penalty, max working days: [[FACT:ak.final_pay.penalty.max_working_days=90]] | US-AKS5-001 |
| Arkansas (AR) | discharge: [[FACT:ar.final_pay.discharge=next regular payday; double wages if unpaid within 7 days of that payday]]; double wages after days: [[FACT:ar.final_pay.double_wages_after_days=7]] | US-ARS5-003 |
| Arizona (AZ) | discharge: [[FACT:az.final_pay.discharge=within 7 working days or end of next regular pay period, whichever sooner; resignation: regular payday of the period]] | US-AZS5-003 |
| California (CA) | discharge: [[FACT:ca.final_pay.discharge=immediately (72 h for seasonal perishable-food layoffs); quit: within 72 h or last day with 72 h notice; waiting-time penalty 1 day wages per day up to 30 days]]; waiting time penalty max days: [[FACT:ca.final_pay.waiting_time_penalty_max_days=30]] | US-CAS5-010 |
| Colorado (CO) | penalty, min: [[FACT:co.final_pay.penalty.min=1,000]]; rule: [[FACT:co.final_pay.rule=discharge: immediately (6 h after next workday start if payroll unit closed, 24 h if off-site); resignation: next regular payday; unclaimed check mailed after 60 days]] | US-COS5-003 |
| Connecticut (CT) | rule: [[FACT:ct.final_pay.rule=discharge: business day after; quit/layoff: next regular payday]] | US-CTS5-005 |
| District of Columbia (DC) | rule: [[FACT:dc.final_pay.rule=discharge: working day after (4 days if employee handled employer money); resignation: next regular payday or 7 days, whichever first; liquidated damages lesser of 10%/working day or treble; CBA may override]] | US-DCS5-003 |
| Delaware (DE) | rule: [[FACT:de.final_pay.rule=later of next regular payday or 3 business days after last day worked (quit, discharge, suspension, layoff); liquidated damages lower of 10%/day or unpaid wages]] | US-DES5-002 |
| Florida (FL) | statewide paid-sick-leave law: no | US-FLS5-016 |
| Hawaii (HI) | rule: [[FACT:hi.final_pay.rule=discharge: at discharge or next working day; resignation: next regular payday (at quitting if one pay period notice); layoff: next regular payday (HRS 388-3)]] | US-HIS5-008 |
| Iowa (IA) | rule: [[FACT:ia.final_pay.rule=next regular payday for the period in which wages were earned (no discharge/resignation distinction); commission true-up within 30 days; vacation only per agreement/pro-rata policy (91A.4)]] | US-IAS5-003 |
| Idaho (ID) | max days: [[FACT:id.final_pay.max_days=10]]; rule: [[FACT:id.final_pay.rule=earlier of next regular payday or 10 days excluding weekends/holidays; within 48 hours on written request; piece/commission: MW for last period then balance next payday (45-606)]] | US-IDS5-005 |
| Illinois (IL) | rule: [[FACT:il.final_pay.rule=in full at separation if possible, no later than next regularly scheduled payday (discharge or resignation); mailed on written request (115/5)]] | US-ILS5-023 |
| Indiana (IN) | rule: [[FACT:in.final_pay.rule=discharge: regular payday for the period of separation (22-2-9-2); resignation: next usual payday; employer pays conceded part of disputed amount (22-2-9-3)]] | US-INS5-005 |
| Kansas (KS) | rule: [[FACT:ks.final_pay.rule=next regular payday for discharge and resignation, by mail on request; willful non-payment 1%/day after 8th day, max 100% (44-315)]] | US-KSS5-014 |
| Kentucky (KY) | max days: [[FACT:ky.final_pay.max_days=14]]; rule: [[FACT:ky.final_pay.rule=later of next normal payday or 14 days after separation, discharge or resignation (KRS 337.055); vested vacation and earned bonuses are wages]] | US-KYS5-005 |
| Louisiana (LA) | max days: [[FACT:la.final_pay.max_days=15]]; penalty wages, max days: [[FACT:la.final_pay.penalty_wages.max_days=90]]; rule: [[FACT:la.final_pay.rule=discharge or resignation: earlier of next regular payday (for the cycle worked) or 15 days; customary place/method or prepaid mail; CBA override; earned eligible vacation is due and cannot be forfeited; commissions/bonuses due if earned (23:631)]] | US-LAR3-001 US-LAR3-002 |
| Massachusetts (MA) | rule: [[FACT:ma.final_pay.rule=discharge: in full on the day of discharge; resignation: next regular payday (or following Saturday); agreed vacation/holiday pay are wages payable at termination (c.149 s.148)]] | US-MAP51-008 |
| Maryland (MD) | rule: [[FACT:md.final_pay.rule=on or before next regular payday, discharge or resignation; accrued vacation payable unless written policy limits payout, employee notified at hire and policy denies it; ESSL not payable]] | US-MDS5-010 |
| Maine (ME) | rule: [[FACT:me.final_pay.rule=no later than next established payday (discharge or resignation); on demand earlier of next payday or 2 weeks; accrued vacation from 2023-01-01 payable (not employers with <= 10 employees or public; CBA overrides); liquidated damages 2x]] | US-MES5-007 |
| Michigan (MI) | rule: [[FACT:mi.final_pay.rule=discharge and quit: as soon as the amount can with due diligence be determined (hand harvesters within 3 days); contract workers estimated pay then final at contract end; deceased: designee/next-of-kin (MCL 408.475)]] | US-MIS5-007 |
| Minnesota (MN) | discharge: [[FACT:mn.final_pay.discharge=within 24 hours after written demand]]; resignation: [[FACT:mn.term.final_pay.resignation=next regular payday; max 20 calendar days]] | US-MNS5-006 US-MNS5-007 |
| Missouri (MO) | discharge: [[FACT:mo.final_pay.discharge=day of discharge; penalty wages up to 60 days after 7-day written request]] | US-MOS5-004 |
| Montana (MT) | discharge: [[FACT:mt.final_pay.discharge=immediately (policy may extend to next payday or 15 days)]]; quit: [[FACT:mt.term.final_pay.quit=next regular payday or 15 days, whichever first]] | US-MTS5-002 |
| North Carolina (NC) | rule: [[FACT:nc.final_pay.rule=next regular payday (discharge and resignation)]] | US-NCS5-006 |
| North Dakota (ND) | rule: [[FACT:nd.final_pay.rule=next regular payday (discharge, resignation, suspension)]] | US-NDS5-005 |
| Nebraska (NE) | rule: [[FACT:ne.final_pay.rule=next regular payday or within two weeks, whichever sooner]] | US-NES5-006 |
| New Hampshire (NH) | discharge, hours: [[FACT:nh.term.final_pay.discharge.hours=72]]; resignation: [[FACT:nh.term.final_pay.resignation=next regular payday, or 72 hours if one pay period's notice]] | US-NHS5-002 |
| New Jersey (NJ) | rule: [[FACT:nj.final_pay.rule=regular payday for the period in which employment ended]] | US-NJS5-003 |
| New Mexico (NM) | discharge: [[FACT:nm.final_pay.discharge=fixed wages within 5 days; task/piece/commission within 10 days]]; quit: [[FACT:nm.term.final_pay.quit=next regular payday]] | US-NMS5-014 |
| Nevada (NV) | discharge: [[FACT:nv.final_pay.discharge=immediately]]; resignation: [[FACT:nv.term.final_pay.resignation=earlier of regular payday or 7 days]] | US-NVS5-001 |
| New York (NY) | rule: [[FACT:ny.final_pay.rule=next regular payday (discharge and resignation)]] | US-NYS5-003 |
| Ohio (OH) | rule: [[FACT:oh.final_pay.rule=next regular payday under 4113.15 schedule]] | US-OHS5-015 |
| Oklahoma (OK) | rule: [[FACT:ok.final_pay.rule=next regular designated payday (discharge and resignation)]] | US-OKS5-004 |
| Oregon (OR) | discharge: [[FACT:or.final_pay.discharge=end of first business day]]; resignation with notice: [[FACT:or.term.final_pay.resignation_with_notice=immediately (48 h notice)]] | US-ORS5-006 |
| Pennsylvania (PA) | rule: [[FACT:pa.final_pay.rule=next regular payday (any separation)]] | US-PAS5-005 |
| Rhode Island (RI) | rule: [[FACT:ri.final_pay.rule=next regular payday; within 24 hours on liquidation/merger/sale/move out of state]] | US-RIS5-006 |
| South Carolina (SC) | rule: [[FACT:sc.final_pay.rule=within 48 hours or next regular payday (max 30 days)]] | US-SCP52-006 |
| South Dakota (SD) | rule: [[FACT:sd.final_pay.rule=next regular payday (or when property returned)]] | US-SDS5-001 |
| Tennessee (TN) | rule: [[FACT:tn.final_pay.rule=later of next regular payday or 21 days after separation]] | US-TNS5-001 |
| Texas (TX) | discharge, days: [[FACT:tx.term.final_pay.discharge.days=6]]; other: [[FACT:tx.term.final_pay.other=next regularly scheduled payday]] | US-TXS5-004 |
| Utah (UT) | discharge, hours: [[FACT:ut.term.final_pay.discharge.hours=24]]; resignation: [[FACT:ut.term.final_pay.resignation=next regular payday]] | US-UTS5-002 |
| Virginia (VA) | rule: [[FACT:va.final_pay.rule=next regular payday (discharge and resignation)]] (from 2026-07-01) | US-VAS5-003 |
| Vermont (VT) | discharge, hours: [[FACT:vt.term.final_pay.discharge.hours=72]] | US-VTS5-002 |
| Washington (WA) | rule: [[FACT:wa.final_pay.rule=end of established pay period (discharge and resignation)]] | US-WAS5-002 |
| Wisconsin (WI) | rule: [[FACT:wi.final_pay.rule=earlier of next regular payday or 31-day limit (quit and discharge)]] | US-WIS5-004 |
| West Virginia (WV) | rule: [[FACT:wv.final_pay.rule=next regular payday (discharge and resignation)]] | US-WVS5-003 |
| Wyoming (WY) | rule: [[FACT:wy.final_pay.rule=no later than the usual regular payday]] (from 2026-05-08) | US-WYS5-002 |

States with no verified final-pay rule: AL, GA, MS. Not configured in this release [[GAP:RQ-523]]: Final-pay timing is not established from an official source for these States; see each jurisdiction annex.

**State separation notices established from official sources:** California [[FACT:ca.separation_notice=CUIC 1089 Notice to Employee as to Change in Relationship + DE 2320 at discharge, layoff or leave; email only with opt-in]] [US-CAS5-018]; Connecticut [[FACT:ct.separation_notice=UC-21 Separation Packet with UC-21A to every separating employee]] [US-CTS5-031]; Georgia [[FACT:ga.separation_notice.dol800=DOL-800 (R-02-24) to every separated worker stating reason, on last day or within 3 days; electronic with e-signature allowed (Oct 2026 rules)]] [US-GAS5-007]; New Jersey [[FACT:nj.term.separation_notice.form=BC-10 at every separation]] [US-NJS5-015]; Tennessee within [[FACT:tn.term.separation_notice.hours=24]] hours [US-TNS5-007].

### How do termination rules and calculations differ by residential status and employer type?

- **Federal resident vs nonresident alien.** Severance and final wages are wages for both. For a nonresident alien the nonresident add-on increases the wage used in the regular withholding computation only. It is not applied to supplemental wages withheld at the flat rate (the add-on is not applied to the flat-rate method) [US-FEDS5-002]. Treaty-exempt wages claimed on Form 8233 go on Form 1042-S, not on Form W-2 ([[FACT:fed.fit.nra.treaty_exempt.reporting=Treaty-exempt wages claimed on Form 8233 are reported on Form 1042-S (not W-2 box 1); 2026 Forms 1042-S due 2027-03-15 and must be e-filed via IRIS]]) [US-FEDS5-016].
- **State residence.** Final-pay timing follows the work State (Table 9.1.1). State withholding on a termination payment follows the same residence/work-State routing as regular wages (Module 6 and the MULTI annex).
- **Employer type and size.** WARN applies to covered plant closings and mass layoffs. Maine's statutory severance applies to establishments of the size stated in the first table of 9.1. Household and agricultural employers follow the special thresholds of Module 11.

### Detail the calculation and tax withholding rules for unused leave paid out on termination.

- **When it is due:** only where Module 8, Table 8.1.3 makes the balance wages due, and on the final-pay date of Table 9.1.1.
- **Federal withholding:** where due, the payout is paid with the final wages. Classification: [[FACT:fed.vacation_payout.supplemental_status=Vacation pay is withheld on as regular wages; when it is in addition to regular wages for the vacation period (e.g. an annual lump-sum payment for unused vacation leave) it is a supplemental wage payment; vacation pay for longer than the usual payroll period is spread over the pay periods for which it is paid.]] [US-FEDQ1-002]. A lump-sum payout of unused leave is withheld on with the supplemental-wage methods of Module 6 §6.2 (optional flat rate or aggregate).
- **State example:** Louisiana withholds vacation pay like regular wages, with no flat supplemental rate ([[FACT:la.wh.supplemental.method=withheld like regular wages; no flat supplemental rate (vacation pay likewise)]]) [US-LAP51-002].

### Describe the rules for statutory severance/redundancy payments.

Federal law sets a notice duty, not a severance entitlement. WARN requires [[FACT:fed.warn.notice_days=60]] days' notice of a covered plant closing or mass layoff [US-FEDS5-025]. Pay in lieu of the notice is wages. Statutory severance established from official sources: Maine ([[FACT:me.severance.mass_layoff=establishments with 100+ employees: one week pay per year of service, within one pay period after last day; 90 days notice]]) [US-MES5-010]; New Jersey [[FACT:nj.term.warn.severance.weeks_per_year=1]] week per year of service on a covered mass layoff [US-NJS5-020]. Severance is withheld as supplemental wages (9.2).

### Provide the statutory formula for any tax-free portion.

**Federal:** none. Severance is wages for FIT, FICA and FUTA in full [US-FEDS5-029].

**Alabama:** severance pay up to [[FACT:al.wh.severance.exempt_max=50,000]] is exempt from Alabama withholding [US-ALS5-001].

```
AL_exempt_part  = min(severance, AL_SEVERANCE_EXEMPT_MAX)
AL_taxable_part = severance - AL_exempt_part      # withheld under the AL method
FED_taxable     = severance                       # no federal exclusion
```

### For other Employment Termination Payments (ETPs), provide a reference guide.

| Payment | FIT | OASDI / Medicare | FUTA | Reported on |
|---|---|---|---|---|
| Final wages, overtime, commissions | Regular method | Yes | Yes | W-2 |
| Severance / pay in lieu of notice | Supplemental (flat or aggregate) | Yes | Yes | W-2 |
| Bonus paid at exit | Supplemental (flat or aggregate) | Yes | Yes | W-2 |
| Accrued vacation payout (where due) | Paid with final wages (regular or supplemental: gap above) | Not established (gap above) | Not established (gap above) | W-2 |
| Treaty-exempt wages of a nonresident alien | Per Form 8233 | Per the nonresident rules | Per the nonresident rules | 1042-S |

### Detail the rules for any applicable concessional tax cap.

No federal concessional cap applies to termination payments. Supplemental wages paid to one employee above [[FACT:fed.fit.supplemental.mandatory_threshold=1,000,000]] in the calendar year must be withheld at [[FACT:fed.fit.supplemental.mandatory_rate=37]]% [US-FEDS5-003]. This is a mandatory higher rate, not a concession. Alabama's severance exemption ([[FACT:al.wh.severance.exempt_max=50,000]]) is the only State cap established from official sources.

### Provide a detailed worked example of a redundancy termination payout.

**Scenario.** An employee whose position is eliminated receives severance pay of 18,000.00 in a separate payment, after 60,000.00 of 2026 wages from this employer. Severance is wages for FIT, FICA and FUTA [US-FEDS5-029]. Paid separately, it is withheld as supplemental wages at the optional flat rate. FUTA is already exhausted for the year at this wage level. State withholding and final-pay timing follow the work State (Table 9.1.1). Alabama, for example, exempts severance up to [[FACT:al.wh.severance.exempt_max=50,000]] from its withholding [US-ALS5-001].

*Redundancy severance payout (federal layer)*

| Line | Calculation | Result (USD) |
|---|---|---|
| Supplemental payment (paid separately from regular wages) | — | 18,000.00 |
| FIT, optional flat rate (supplemental wages up to [[FACT:fed.fit.supplemental.mandatory_threshold=1,000,000]] in the year) | 18,000.00 × [[FACT:fed.fit.supplemental.flat_rate=22]]% | 3,960.00 |
| OASDI base remaining before this pay | [[FACT:fed.fica.oasdi.wage_base=184,500]] − 60,000.00 | 124,500.00 |
| OASDI base for this pay (lesser of remaining base and pay) | min(124,500.00, 18,000.00) | 18,000.00 |
| OASDI employee | 18,000.00 × [[FACT:fed.fica.oasdi.rate.employee=6.2]]% | 1,116.00 |
| Medicare employee | 18,000.00 × [[FACT:fed.fica.medicare.rate.employee=1.45]]% | 261.00 |
| Net payment | 18,000.00 − 3,960.00 − 1,116.00 − 261.00 | 12,663.00 |

## 9.2 Irregular and Retrospective Payments

### Describe the specific tax calculation method required for irregular payments.

Bonuses, commissions, severance and similar payments are **supplemental wages**. Three federal rules apply [US-FEDS5-003]:
1. **Optional flat rate** of [[FACT:fed.fit.supplemental.flat_rate=22]]%, when the supplemental payment is identified separately from regular wages.
2. **Aggregate method:** the supplemental payment is withheld together with regular wages under the regular tables (procedure detail: Module 11.1, gap).
3. **Mandatory rate:** above [[FACT:fed.fit.supplemental.mandatory_threshold=1,000,000]] of supplemental wages in the year, [[FACT:fed.fit.supplemental.mandatory_rate=37]]% applies to the excess, whatever the W-4.

FICA and FUTA apply as to any wage. **Table 9.2.1** lists the State supplemental rules established from official sources.

| State | Rule (parameter: value) | Register |
|---|---|---|
| Alabama (AL) | rate: [[FACT:al.wh.supplemental.rate=5]] | US-ALS5-001 |
| Arkansas (AR) | rate: [[FACT:ar.wh.supplemental.rate=3.7]] | US-ARP51-002 |
| Arizona (AZ) | rate: [[FACT:az.wh.supplemental.rate=same elected percentage (no separate supplemental rate)]] | US-AZS5-020 |
| California (CA) | rate, bonus stock options: [[FACT:ca.wh.supplemental.rate.bonus_stock_options=10.23]] | US-CAS5-004 |
| California (CA) | rate, other: [[FACT:ca.wh.supplemental.rate.other=6.6]] | US-CAS5-004 |
| Connecticut (CT) | method: [[FACT:ct.wh.supplemental.method=aggregate only (no flat supplemental rate)]] | US-CTS5-012 |
| Delaware (DE) | method: [[FACT:de.wh.supplemental.method=with regular wages: one payment; separately: annualized-with minus annualized-without; tips same; deferred compensation recommended 5%]] | US-DES5-006 |
| Georgia (GA) | rate: [[FACT:ga.wh.supplemental.rate=applicable income tax rate in effect when paid (4.99% from 2026-05-11); no separate table]] | US-GAS5-004 |
| Iowa (IA) | rate: [[FACT:ia.wh.supplemental.rate=3.8]] | US-IAS5-016 |
| Idaho (ID) | rate: [[FACT:id.wh.supplemental.rate=5.3]] | US-IDS5-008 |
| Indiana (IN) | rate: [[FACT:in.wh.supplemental.rate=2.95]] | US-INS5-007 |
| Kansas (KS) | rate: [[FACT:ks.wh.supplemental.rate=5]] | US-KSS5-001 |
| Kentucky (KY) | method: [[FACT:ky.wh.supplemental.method=no separate rate; bonuses and severance through the same formula; film-incentive companies at max 141.020 rate]] | US-KY-001 |
| Louisiana (LA) | method: [[FACT:la.wh.supplemental.method=withheld like regular wages; no flat supplemental rate (vacation pay likewise)]] | US-LAP51-002 |
| Massachusetts (MA) | rate: [[FACT:ma.wh.supplemental.rate=5]] | US-MAP51-003 |
| Massachusetts (MA) | rule: [[FACT:ma.wh.supplemental.rule=5% while annualized regular + supplemental to date + this payment <= 1,107,750; above, lesser of 9% of payment or 9% of excess plus 5% of remainder; percentage method excludes supplemental]] | US-MAP51-003 |
| Maryland (MD) | lump sum bonus: [[FACT:md.wh.supplemental.lump_sum_bonus=top state rate 6.50% + county top local rate (e.g. 9.80% in 3.30 table; 9.70% in 3.20 table); no flat rate for other supplemental pay; computed in cents (retirement whole dollars)]] | US-MDS5-021 |
| Maine (ME) | rate: [[FACT:me.wh.supplemental.rate=5]] | US-MES5-011 |
| Michigan (MI) | rate: [[FACT:mi.wh.supplemental.rate=4.25]] | US-MIPIT-001 |
| Minnesota (MN) | rate: [[FACT:mn.wh.supplemental.rate=6.25]] | US-MNS5-010 |
| Missouri (MO) | rate: [[FACT:mo.wh.supplemental.rate=4.7]] | US-MOS5-001 |
| Mississippi (MS) | method: [[FACT:ms.pit.supplemental.method=aggregate; no fixed flat rate (top rate 4% allowed where aggregation over-withholds)]] | US-MSS5-002 |
| Montana (MT) | rate: [[FACT:mt.wh.supplemental.rate=5]] | US-MTP51-001 |
| North Carolina (NC) | rate: [[FACT:nc.wh.supplemental.rate=4.09]] | US-NC-001 |
| North Dakota (ND) | rate: [[FACT:nd.wh.supplemental.rate=1.5]] | US-NDS5-001 |
| Nebraska (NE) | rate: [[FACT:ne.wh.supplemental.rate=3.5]] | US-NEP51-001 |
| New Jersey (NJ) | method: [[FACT:nj.pit.supplemental.method=combined with regular wages, or without allowances if separate; no flat rate]] | US-NJP51-001 |
| New Mexico (NM) | rate: [[FACT:nm.wh.supplemental.rate=5.9]] | US-NMP52-001 |
| New York (NY) | nys, rate: [[FACT:ny.pit.supplemental.nys.rate=11.7]] | US-NY-001 |
| Ohio (OH) | rate: [[FACT:oh.wh.supplemental.rate=2.75]] | US-OHS5-007 |
| Oklahoma (OK) | rate: [[FACT:ok.wh.supplemental.rate=4.5]] | US-OK-001 |
| Oregon (OR) | rate: [[FACT:or.wh.supplemental.rate=8]] | US-ORS5-009 |
| Rhode Island (RI) | rate: [[FACT:ri.wh.supplemental.rate=5.99]] | US-RIS5-019 |
| South Carolina (SC) | flat rate, exists: no | US-SCS5-002 |
| Virginia (VA) | rate: [[FACT:va.wh.supplemental.rate=5.75]] | US-VAS5-013 |
| Vermont (VT) | ratio of federal: [[FACT:vt.pit.supplemental.ratio_of_federal=30]] | US-VTS5-016 |
| Wisconsin (WI) | flat rates: [[FACT:wi.pit.supplemental.flat_rates=3.54 (0-12,760); 4.65 (to 25,520); 5.30 (to 280,950); 7.65 (above) by estimated annual gross]] | US-WIP51-001 |

### How are backdated payments and retrospective salary adjustments handled?

Federal payroll taxes follow the **payment date**, not the period the pay relates to ([[FACT:fed.tax_year.basis=calendar year (W-2 on calendar-year basis)]]) [US-FED-006]. A retroactive increase paid in 2026 is 2026 wages. It takes the 2026 tables and the 2026 wage bases, even when it relates to 2025. Massachusetts PFML is the exception: its rate follows the wages earned date [US-MAS5-012]. Not configured in this release [[GAP:RQ-525]]: The federal classification of back pay and retroactive increases (supplemental or regular wages) is not established from an official source.

### For arrears, how are contributions and deductions computed?

- Arrears paid now are wages of the payment period. OASDI is due on the lesser of the arrears and the remaining annual wage base ([[FACT:fed.fica.oasdi.wage_base=184,500]] for 2026) [US-FEDS5-005]. Medicare is due on the full amount. Additional Medicare is due on the part above [[FACT:fed.fica.addl_medicare.withholding_threshold=200,000]] of wages paid in the year [US-FEDS5-005].
- FIT uses the supplemental method if the arrears are paid separately (9.2), or the aggregate method if they are paid with regular wages.
- Child-support arrears withheld under an income withholding order follow the CCPA limits (add [[FACT:fed.ccpa.support.arrears_addon=5]] percentage points when arrears exceed 12 weeks) [US-FEDS5-023]; see Module 7.

### Provide a worked example of a bonus calculation.

**Scenario.** An annual bonus of 5,000.00 is paid on its own check to an employee with 40,000.00 of 2026 wages. Supplemental wages identified separately from regular wages may be withheld at the optional flat rate [US-FEDS5-003]. FICA applies in full.

*Annual bonus, optional flat-rate method (federal layer)*

| Line | Calculation | Result (USD) |
|---|---|---|
| Supplemental payment (paid separately from regular wages) | — | 5,000.00 |
| FIT, optional flat rate (supplemental wages up to [[FACT:fed.fit.supplemental.mandatory_threshold=1,000,000]] in the year) | 5,000.00 × [[FACT:fed.fit.supplemental.flat_rate=22]]% | 1,100.00 |
| OASDI base remaining before this pay | [[FACT:fed.fica.oasdi.wage_base=184,500]] − 40,000.00 | 144,500.00 |
| OASDI base for this pay (lesser of remaining base and pay) | min(144,500.00, 5,000.00) | 5,000.00 |
| OASDI employee | 5,000.00 × [[FACT:fed.fica.oasdi.rate.employee=6.2]]% | 310.00 |
| Medicare employee | 5,000.00 × [[FACT:fed.fica.medicare.rate.employee=1.45]]% | 72.50 |
| Net payment | 5,000.00 − 1,100.00 − 310.00 − 72.50 | 3,517.50 |
