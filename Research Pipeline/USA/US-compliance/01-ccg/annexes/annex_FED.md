# Annex FED: Federal layer

This annex sets out the federal payroll layer for the 2026 build year. It applies to every in-scope employee, in addition to the State layer that Annex MULTI selects. Every value is shown with its effective dates and its source (list at the end of the annex).

Classification: federal income tax withholding and FICA are one calculation per employee with one authority (the IRS); FUTA is federal but its credit depends on the State UI paid and on the State's credit-reduction status, so it is a cross-layer dependency. Independent contractors (Form 1099-NEC) are out of scope.

## FED.1 Employment and labour code

The federal Fair Labor Standards Act sets the floor. The employer pays the highest of the federal, State and local minimum wage (State annexes; rule in Annex MULTI, [[FACT:multi.wage_hour.overlay_rule=FLSA does not excuse a higher State/municipal minimum wage, a lower maximum workweek or a stricter child-labour standard: apply the more protective standard of the place where the work is performed]]). There is no federal daily overtime; pay frequency, pay-day timing and the method of payment are State law.

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Minimum wage hourly | USD [[FACT:fed.minwage.hourly=7.25]] | from 2009-07-24 |  | S1 | FLSA 206(a)(1)(C); not indexed; no 2026/2027 change enacted. Employer pays the highest of federal, state and local minimum (state annexes). |
| Overtime weekly threshold hours | [[FACT:fed.overtime.weekly_threshold_hours=40]] hours | from 1938-10-24 |  | S2 | No federal daily overtime; daily OT is state law (state annexes). |
| Overtime premium multiplier | [[FACT:fed.overtime.premium.multiplier=1.5]] ratio | from 1938-10-24 |  | S2 | 0.5 premium portion = qualified overtime compensation for P.L. 119-21 / W-2 code TT. |
| Tipped cash wage hourly | USD [[FACT:fed.tipped.cash_wage.hourly=2.13]] | from 1996-08-20 |  | S3 |  |
| Tipped tip credit max hourly | USD [[FACT:fed.tipped.tip_credit.max_hourly=5.12]] | from 1996-08-20 |  | S3 | [[FACT:fed.minwage.hourly=7.25]] - [[FACT:fed.tipped.cash_wage.hourly=2.13]] = [[FACT:fed.tipped.tip_credit.max_hourly=5.12]]. |
| Tipped monthly tips threshold | USD [[FACT:fed.tipped.monthly_tips_threshold=30]] | from 1996-08-20 |  | S3 | Tipped employee = customarily and regularly receives more than [[FACT:fed.tipped.monthly_tips_threshold=30]]/month in tips (29 USC 203(t)). |
| Exempt salary floor weekly | USD [[FACT:fed.exempt.salary_floor.weekly=684]] | from 2020-01-01 |  | S4 | EAP exemption, 29 CFR 541.600 current eCFR text (2024 increase not in the CFR). |
| Exempt salary floor biweekly | USD [[FACT:fed.exempt.salary_floor.biweekly=1,368]] | from 2020-01-01 |  | S4 | EAP exemption, 29 CFR 541.600 current eCFR text (2024 increase not in the CFR). |
| Exempt salary floor semimonthly | USD [[FACT:fed.exempt.salary_floor.semimonthly=1,482]] | from 2020-01-01 |  | S4 | EAP exemption, 29 CFR 541.600 current eCFR text (2024 increase not in the CFR). |
| Exempt salary floor monthly | USD [[FACT:fed.exempt.salary_floor.monthly=2,964]] | from 2020-01-01 |  | S4 | EAP exemption, 29 CFR 541.600 current eCFR text (2024 increase not in the CFR). |
| Exempt salary floor territories weekly | USD [[FACT:fed.exempt.salary_floor.territories_weekly=455]] | from 2020-01-01 |  | S4 | CNMI, Guam, PR, USVI. |
| Exempt salary floor american samoa weekly | USD [[FACT:fed.exempt.salary_floor.american_samoa_weekly=380]] | from 2020-01-01 |  | S4 |  |

## FED.2 Income tax withholding

**Method.** [[FACT:fed.fit.method=IRS Pub. 15-T (2026) Worksheet 1A with the Annual Percentage Method tables (STANDARD schedule; Step-2-checked schedule when W-4 Step 2 box checked)]]. Employee inputs come from Form W-4: [[FACT:fed.w4.input_fields=filing status (Single/MFS, MFJ/QSS, HoH); Step 2 flag; Step 3 amount; Step 4(a); Step 4(b); Step 4(c); exempt checkbox]]. The computation, per pay period:

```
annual_wages   = period_wages x pay_periods            # periods: [[FACT:fed.fit.pay_periods_per_year=2 / 4 / 12 / 24 / 26 / 52 / 260 (semiannual, quarterly, monthly, semimonthly, biweekly, weekly, daily)]]
adjusted       = annual_wages + W4_Step4a - W4_Step4b
if not W4_Step2_checked: adjusted -= line_1g            # MFJ [[FACT:fed.fit.worksheet1a.line1g.mfj=12,900]]; other [[FACT:fed.fit.worksheet1a.line1g.other=8,600]]
schedule       = STANDARD if not W4_Step2_checked else STEP2_CHECKED   # tables below, by filing status
tentative      = schedule.cumulative_tax(bracket) + (adjusted - bracket.floor) x bracket.rate
period_tax     = max(0, tentative - W4_Step3) / pay_periods + W4_Step4c
```

A pre-2020 Form W-4 is converted with the allowance value USD [[FACT:fed.fit.allowance.pre2020_value=4,300]] per allowance. Rounding: [[FACT:fed.fit.rounding=Optional: wages may be rounded to the nearest dollar and the period tax rounded to the nearest dollar (drop under 50 cents, 50-99 cents up)]]. The exempt status on a 2026 Form W-4 lapses at year end: [[FACT:fed.w4.exempt.validity=2026 only: the exemption checkbox certification lapses; a new W-4 is required for 2027]].

**Supplemental wages** (bonuses, commissions, severance, back pay): optional flat rate [[FACT:fed.fit.supplemental.flat_rate=22]] %, or the aggregate method; mandatory rate [[FACT:fed.fit.supplemental.mandatory_rate=37]] % on supplemental wages above USD [[FACT:fed.fit.supplemental.mandatory_threshold=1,000,000]] in the calendar year. Backup withholding ([[FACT:fed.fit.backup_withholding.rate=24]] %) applies to reportable payments, not to wages.

The cumulative-tax column of each STANDARD schedule was recomputed from the floors and rates (each row = previous row + (floor difference x previous rate)); every row agrees. The research published no cumulative-tax column for the Step-2-checked schedules; an engine computes it the same way from the floors and rates shown.

**FIT standard MFJ bracket: bracket table**

| Bracket | floor | rate | cumulative tax | Effective | Source |
|---|---|---|---|---|---|
| 1 | USD [[FACT:fed.fit.standard.mfj.bracket.1.floor=0]] | [[FACT:fed.fit.standard.mfj.bracket.1.rate=0]] % | USD [[FACT:fed.fit.standard.mfj.bracket.1.cumulative_tax=0]] | 2026-01-01 to 2026-12-31 | S5 |
| 2 | USD [[FACT:fed.fit.standard.mfj.bracket.2.floor=19,300]] | [[FACT:fed.fit.standard.mfj.bracket.2.rate=10]] % | USD [[FACT:fed.fit.standard.mfj.bracket.2.cumulative_tax=0]] | 2026-01-01 to 2026-12-31 | S5 |
| 3 | USD [[FACT:fed.fit.standard.mfj.bracket.3.floor=44,100]] | [[FACT:fed.fit.standard.mfj.bracket.3.rate=12]] % | USD [[FACT:fed.fit.standard.mfj.bracket.3.cumulative_tax=2,480]] | 2026-01-01 to 2026-12-31 | S5 |
| 4 | USD [[FACT:fed.fit.standard.mfj.bracket.4.floor=120,100]] | [[FACT:fed.fit.standard.mfj.bracket.4.rate=22]] % | USD [[FACT:fed.fit.standard.mfj.bracket.4.cumulative_tax=11,600]] | 2026-01-01 to 2026-12-31 | S5 |
| 5 | USD [[FACT:fed.fit.standard.mfj.bracket.5.floor=230,700]] | [[FACT:fed.fit.standard.mfj.bracket.5.rate=24]] % | USD [[FACT:fed.fit.standard.mfj.bracket.5.cumulative_tax=35,932]] | 2026-01-01 to 2026-12-31 | S5 |
| 6 | USD [[FACT:fed.fit.standard.mfj.bracket.6.floor=422,850]] | [[FACT:fed.fit.standard.mfj.bracket.6.rate=32]] % | USD [[FACT:fed.fit.standard.mfj.bracket.6.cumulative_tax=82,048]] | 2026-01-01 to 2026-12-31 | S5 |
| 7 | USD [[FACT:fed.fit.standard.mfj.bracket.7.floor=531,750]] | [[FACT:fed.fit.standard.mfj.bracket.7.rate=35]] % | USD [[FACT:fed.fit.standard.mfj.bracket.7.cumulative_tax=116,896]] | 2026-01-01 to 2026-12-31 | S5 |
| 8 | USD [[FACT:fed.fit.standard.mfj.bracket.8.floor=788,000]] | [[FACT:fed.fit.standard.mfj.bracket.8.rate=37]] % | USD [[FACT:fed.fit.standard.mfj.bracket.8.cumulative_tax=206,583.50]] | 2026-01-01 to 2026-12-31 | S5 |

**FIT standard single bracket: bracket table**

| Bracket | floor | rate | cumulative tax | Effective | Source |
|---|---|---|---|---|---|
| 1 | USD [[FACT:fed.fit.standard.single.bracket.1.floor=0]] | [[FACT:fed.fit.standard.single.bracket.1.rate=0]] % | USD [[FACT:fed.fit.standard.single.bracket.1.cumulative_tax=0]] | 2026-01-01 to 2026-12-31 | S5 |
| 2 | USD [[FACT:fed.fit.standard.single.bracket.2.floor=7,500]] | [[FACT:fed.fit.standard.single.bracket.2.rate=10]] % | USD [[FACT:fed.fit.standard.single.bracket.2.cumulative_tax=0]] | 2026-01-01 to 2026-12-31 | S5 |
| 3 | USD [[FACT:fed.fit.standard.single.bracket.3.floor=19,900]] | [[FACT:fed.fit.standard.single.bracket.3.rate=12]] % | USD [[FACT:fed.fit.standard.single.bracket.3.cumulative_tax=1,240]] | 2026-01-01 to 2026-12-31 | S5 |
| 4 | USD [[FACT:fed.fit.standard.single.bracket.4.floor=57,900]] | [[FACT:fed.fit.standard.single.bracket.4.rate=22]] % | USD [[FACT:fed.fit.standard.single.bracket.4.cumulative_tax=5,800]] | 2026-01-01 to 2026-12-31 | S5 |
| 5 | USD [[FACT:fed.fit.standard.single.bracket.5.floor=113,200]] | [[FACT:fed.fit.standard.single.bracket.5.rate=24]] % | USD [[FACT:fed.fit.standard.single.bracket.5.cumulative_tax=17,966]] | 2026-01-01 to 2026-12-31 | S5 |
| 6 | USD [[FACT:fed.fit.standard.single.bracket.6.floor=209,275]] | [[FACT:fed.fit.standard.single.bracket.6.rate=32]] % | USD [[FACT:fed.fit.standard.single.bracket.6.cumulative_tax=41,024]] | 2026-01-01 to 2026-12-31 | S5 |
| 7 | USD [[FACT:fed.fit.standard.single.bracket.7.floor=263,725]] | [[FACT:fed.fit.standard.single.bracket.7.rate=35]] % | USD [[FACT:fed.fit.standard.single.bracket.7.cumulative_tax=58,448]] | 2026-01-01 to 2026-12-31 | S5 |
| 8 | USD [[FACT:fed.fit.standard.single.bracket.8.floor=648,100]] | [[FACT:fed.fit.standard.single.bracket.8.rate=37]] % | USD [[FACT:fed.fit.standard.single.bracket.8.cumulative_tax=192,979.25]] | 2026-01-01 to 2026-12-31 | S5 |

**FIT standard HoH bracket: bracket table**

| Bracket | floor | rate | cumulative tax | Effective | Source |
|---|---|---|---|---|---|
| 1 | USD [[FACT:fed.fit.standard.hoh.bracket.1.floor=0]] | [[FACT:fed.fit.standard.hoh.bracket.1.rate=0]] % | USD [[FACT:fed.fit.standard.hoh.bracket.1.cumulative_tax=0]] | 2026-01-01 to 2026-12-31 | S5 |
| 2 | USD [[FACT:fed.fit.standard.hoh.bracket.2.floor=15,550]] | [[FACT:fed.fit.standard.hoh.bracket.2.rate=10]] % | USD [[FACT:fed.fit.standard.hoh.bracket.2.cumulative_tax=0]] | 2026-01-01 to 2026-12-31 | S5 |
| 3 | USD [[FACT:fed.fit.standard.hoh.bracket.3.floor=33,250]] | [[FACT:fed.fit.standard.hoh.bracket.3.rate=12]] % | USD [[FACT:fed.fit.standard.hoh.bracket.3.cumulative_tax=1,770]] | 2026-01-01 to 2026-12-31 | S5 |
| 4 | USD [[FACT:fed.fit.standard.hoh.bracket.4.floor=83,000]] | [[FACT:fed.fit.standard.hoh.bracket.4.rate=22]] % | USD [[FACT:fed.fit.standard.hoh.bracket.4.cumulative_tax=7,740]] | 2026-01-01 to 2026-12-31 | S5 |
| 5 | USD [[FACT:fed.fit.standard.hoh.bracket.5.floor=121,250]] | [[FACT:fed.fit.standard.hoh.bracket.5.rate=24]] % | USD [[FACT:fed.fit.standard.hoh.bracket.5.cumulative_tax=16,155]] | 2026-01-01 to 2026-12-31 | S5 |
| 6 | USD [[FACT:fed.fit.standard.hoh.bracket.6.floor=217,300]] | [[FACT:fed.fit.standard.hoh.bracket.6.rate=32]] % | USD [[FACT:fed.fit.standard.hoh.bracket.6.cumulative_tax=39,207]] | 2026-01-01 to 2026-12-31 | S5 |
| 7 | USD [[FACT:fed.fit.standard.hoh.bracket.7.floor=271,750]] | [[FACT:fed.fit.standard.hoh.bracket.7.rate=35]] % | USD [[FACT:fed.fit.standard.hoh.bracket.7.cumulative_tax=56,631]] | 2026-01-01 to 2026-12-31 | S5 |
| 8 | USD [[FACT:fed.fit.standard.hoh.bracket.8.floor=656,150]] | [[FACT:fed.fit.standard.hoh.bracket.8.rate=37]] % | USD [[FACT:fed.fit.standard.hoh.bracket.8.cumulative_tax=191,171]] | 2026-01-01 to 2026-12-31 | S5 |

**FIT step2 MFJ bracket: bracket table**

| Bracket | floor | rate | Effective | Source |
|---|---|---|---|---|
| 1 | USD [[FACT:fed.fit.step2.mfj.bracket.1.floor=0]] | [[FACT:fed.fit.step2.mfj.bracket.1.rate=0]] % | 2026-01-01 to 2026-12-31 | S5 |
| 2 | USD [[FACT:fed.fit.step2.mfj.bracket.2.floor=16,100]] | [[FACT:fed.fit.step2.mfj.bracket.2.rate=10]] % | 2026-01-01 to 2026-12-31 | S5 |
| 3 | USD [[FACT:fed.fit.step2.mfj.bracket.3.floor=28,500]] | [[FACT:fed.fit.step2.mfj.bracket.3.rate=12]] % | 2026-01-01 to 2026-12-31 | S5 |
| 4 | USD [[FACT:fed.fit.step2.mfj.bracket.4.floor=66,500]] | [[FACT:fed.fit.step2.mfj.bracket.4.rate=22]] % | 2026-01-01 to 2026-12-31 | S5 |
| 5 | USD [[FACT:fed.fit.step2.mfj.bracket.5.floor=121,800]] | [[FACT:fed.fit.step2.mfj.bracket.5.rate=24]] % | 2026-01-01 to 2026-12-31 | S5 |
| 6 | USD [[FACT:fed.fit.step2.mfj.bracket.6.floor=217,875]] | [[FACT:fed.fit.step2.mfj.bracket.6.rate=32]] % | 2026-01-01 to 2026-12-31 | S5 |
| 7 | USD [[FACT:fed.fit.step2.mfj.bracket.7.floor=272,325]] | [[FACT:fed.fit.step2.mfj.bracket.7.rate=35]] % | 2026-01-01 to 2026-12-31 | S5 |
| 8 | USD [[FACT:fed.fit.step2.mfj.bracket.8.floor=400,450]] | [[FACT:fed.fit.step2.mfj.bracket.8.rate=37]] % | 2026-01-01 to 2026-12-31 | S5 |

**FIT step2 single bracket: bracket table**

| Bracket | floor | rate | Effective | Source |
|---|---|---|---|---|
| 1 | USD [[FACT:fed.fit.step2.single.bracket.1.floor=0]] | [[FACT:fed.fit.step2.single.bracket.1.rate=0]] % | 2026-01-01 to 2026-12-31 | S5 |
| 2 | USD [[FACT:fed.fit.step2.single.bracket.2.floor=8,050]] | [[FACT:fed.fit.step2.single.bracket.2.rate=10]] % | 2026-01-01 to 2026-12-31 | S5 |
| 3 | USD [[FACT:fed.fit.step2.single.bracket.3.floor=14,250]] | [[FACT:fed.fit.step2.single.bracket.3.rate=12]] % | 2026-01-01 to 2026-12-31 | S5 |
| 4 | USD [[FACT:fed.fit.step2.single.bracket.4.floor=33,250]] | [[FACT:fed.fit.step2.single.bracket.4.rate=22]] % | 2026-01-01 to 2026-12-31 | S5 |
| 5 | USD [[FACT:fed.fit.step2.single.bracket.5.floor=60,900]] | [[FACT:fed.fit.step2.single.bracket.5.rate=24]] % | 2026-01-01 to 2026-12-31 | S5 |
| 6 | USD [[FACT:fed.fit.step2.single.bracket.6.floor=108,938]] | [[FACT:fed.fit.step2.single.bracket.6.rate=32]] % | 2026-01-01 to 2026-12-31 | S5 |
| 7 | USD [[FACT:fed.fit.step2.single.bracket.7.floor=136,163]] | [[FACT:fed.fit.step2.single.bracket.7.rate=35]] % | 2026-01-01 to 2026-12-31 | S5 |
| 8 | USD [[FACT:fed.fit.step2.single.bracket.8.floor=328,350]] | [[FACT:fed.fit.step2.single.bracket.8.rate=37]] % | 2026-01-01 to 2026-12-31 | S5 |

**FIT step2 HoH bracket: bracket table**

| Bracket | floor | rate | Effective | Source |
|---|---|---|---|---|
| 1 | USD [[FACT:fed.fit.step2.hoh.bracket.1.floor=0]] | [[FACT:fed.fit.step2.hoh.bracket.1.rate=0]] % | 2026-01-01 to 2026-12-31 | S5 |
| 2 | USD [[FACT:fed.fit.step2.hoh.bracket.2.floor=12,075]] | [[FACT:fed.fit.step2.hoh.bracket.2.rate=10]] % | 2026-01-01 to 2026-12-31 | S5 |
| 3 | USD [[FACT:fed.fit.step2.hoh.bracket.3.floor=20,925]] | [[FACT:fed.fit.step2.hoh.bracket.3.rate=12]] % | 2026-01-01 to 2026-12-31 | S5 |
| 4 | USD [[FACT:fed.fit.step2.hoh.bracket.4.floor=45,800]] | [[FACT:fed.fit.step2.hoh.bracket.4.rate=22]] % | 2026-01-01 to 2026-12-31 | S5 |
| 5 | USD [[FACT:fed.fit.step2.hoh.bracket.5.floor=64,925]] | [[FACT:fed.fit.step2.hoh.bracket.5.rate=24]] % | 2026-01-01 to 2026-12-31 | S5 |
| 6 | USD [[FACT:fed.fit.step2.hoh.bracket.6.floor=112,950]] | [[FACT:fed.fit.step2.hoh.bracket.6.rate=32]] % | 2026-01-01 to 2026-12-31 | S5 |
| 7 | USD [[FACT:fed.fit.step2.hoh.bracket.7.floor=140,175]] | [[FACT:fed.fit.step2.hoh.bracket.7.rate=35]] % | 2026-01-01 to 2026-12-31 | S5 |
| 8 | USD [[FACT:fed.fit.step2.hoh.bracket.8.floor=332,375]] | [[FACT:fed.fit.step2.hoh.bracket.8.rate=37]] % | 2026-01-01 to 2026-12-31 | S5 |

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| FIT method | [[FACT:fed.fit.method=IRS Pub. 15-T (2026) Worksheet 1A with the Annual Percentage Method tables (STANDARD schedule; Step-2-checked schedule when W-4 Step 2 box checked)]] | 2026-01-01 to 2026-12-31 | withholding | S5 |  |
| FIT worksheet1a line1g MFJ | USD [[FACT:fed.fit.worksheet1a.line1g.mfj=12,900]] | 2026-01-01 to 2026-12-31 |  | S5 | Applied when the W-4 Step 2 box is NOT checked. |
| FIT worksheet1a line1g other | USD [[FACT:fed.fit.worksheet1a.line1g.other=8,600]] | 2026-01-01 to 2026-12-31 |  | S5 |  |
| FIT allowance pre2020 value | USD [[FACT:fed.fit.allowance.pre2020_value=4,300]] | 2026-01-01 to 2026-12-31 |  | S5 | Per allowance on a pre-2020 Form W-4 (line 1k). |
| FIT standard deduction MFJ | USD [[FACT:fed.fit.std_deduction.mfj=32,200]] | 2026-01-01 to 2026-12-31 |  | S6 | Rev. Proc. 2025-32; Derivation: standard deduction minus line 1g = zero bracket [[FACT:fed.fit.standard.mfj.bracket.2.floor=19,300]] of Pub. 15-T. |
| FIT standard deduction single | USD [[FACT:fed.fit.std_deduction.single=16,100]] | 2026-01-01 to 2026-12-31 |  | S6 | Rev. Proc. 2025-32; Derivation: standard deduction minus line 1g = zero bracket 7500 of Pub. 15-T. |
| FIT standard deduction HoH | USD [[FACT:fed.fit.std_deduction.hoh=24,150]] | 2026-01-01 to 2026-12-31 |  | S6 | Rev. Proc. 2025-32; Derivation: standard deduction minus line 1g = zero bracket [[FACT:fed.fit.standard.hoh.bracket.2.floor=15,550]] of Pub. 15-T. |
| FIT pay periods per year | [[FACT:fed.fit.pay_periods_per_year=2 / 4 / 12 / 24 / 26 / 52 / 260 (semiannual, quarterly, monthly, semimonthly, biweekly, weekly, daily)]] | 2026-01-01 to 2026-12-31 |  | S5 |  |
| FIT rounding | [[FACT:fed.fit.rounding=Optional: wages may be rounded to the nearest dollar and the period tax rounded to the nearest dollar (drop under 50 cents, 50-99 cents up)]] | from 2026-01-01 |  | S7 |  |
| FIT supplemental flat rate | [[FACT:fed.fit.supplemental.flat_rate=22]] % | from 2026-01-01 | withholding | S8 | Optional flat method; made permanent by P.L. 119-21. |
| FIT supplemental mandatory rate | [[FACT:fed.fit.supplemental.mandatory_rate=37]] % | from 2026-01-01 | withholding | S8 |  |
| FIT supplemental mandatory threshold | USD [[FACT:fed.fit.supplemental.mandatory_threshold=1,000,000]] | from 2026-01-01 |  | S8 | Supplemental wages above [[FACT:fed.fit.supplemental.mandatory_threshold=1,000,000]] paid to one employee in the calendar year. |
| FIT backup withholding rate | [[FACT:fed.fit.backup_withholding.rate=24]] % | from 2026-01-01 |  | S8 |  |
| W-4 input fields | [[FACT:fed.w4.input_fields=filing status (Single/MFS, MFJ/QSS, HoH); Step 2 flag; Step 3 amount; Step 4(a); Step 4(b); Step 4(c); exempt checkbox]] | 2026-01-01 to 2026-12-31 |  | S9 |  |
| W-4 exempt validity | [[FACT:fed.w4.exempt.validity=2026 only: the exemption checkbox certification lapses; a new W-4 is required for 2027]] | 2026-01-01 to 2026-12-31 |  | S9 |  |

## FED.2b Non-resident regime and reciprocity

Non-resident aliens are handled at withholding level: the Pub. 15-T add-on (tables below) is added to the wages used for the federal income tax computation only. It is not reported on the W-2, has no FICA or FUTA effect and is not applied to flat-rate supplemental wages. Form W-4 rule: [[FACT:fed.fit.nra.w4.rule=Check Single or MFS regardless of marital status; write NRA below Step 4(c); exempt not allowed; Step 3 only for residents of Canada, Mexico, South Korea or India (students/apprentices)]]. Treaty-exempt wages: [[FACT:fed.fit.nra.treaty_exempt.reporting=Treaty-exempt wages claimed on Form 8233 are reported on Form 1042-S (not W-2 box 1); 2026 Forms 1042-S due 2027-03-15 and must be e-filed via IRIS]]. Commercial-traveller exception: present no more than [[FACT:fed.fit.nra.commercial_traveler.max_days=90]] days and paid no more than USD [[FACT:fed.fit.nra.commercial_traveler.max_pay=3,000]] by a foreign employer not engaged in a US trade or business. Other-State residents are a State matter (Annex MULTI).

**Resident / non-resident matrix (federal income tax)**

| Income type | US citizen or resident alien | Non-resident alien |
|---|---|---|
| Regular salary | Worksheet 1A, annual percentage method, base = federal income tax wages (FED.2) | Same method; the annual add-on (USD [[FACT:fed.fit.nra.addon.table2.annual=16,100]], Table 2; USD [[FACT:fed.fit.nra.addon.table1.annual=11,800]], Table 1) is added to the wage base before the computation; W-4 completed per the NRA rule |
| Annual bonus / supplemental pay | Optional flat [[FACT:fed.fit.supplemental.flat_rate=22]] % or aggregate; [[FACT:fed.fit.supplemental.mandatory_rate=37]] % above USD [[FACT:fed.fit.supplemental.mandatory_threshold=1,000,000]] | Same rates; no add-on on flat-rate supplemental wages |
| Severance | Wages ([[FACT:fed.severance.is_wages=True]]); supplemental-wage rules | Same as the non-resident supplemental row |
| Equity (option exercise, share vesting) | ⚠️ RESEARCH-GAP (blocking): the federal classification and withholding treatment of equity income are not in the research | ⚠️ RESEARCH-GAP (blocking): same request |
| Benefits in kind | Taxable fringe benefits are wages; exclusions in FED.8 | Same; treaty exemption only where claimed on Form 8233 |
| Contractor / labour-service pay | Out of scope (Form 1099-NEC, owner decision) | Out of scope |

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| FIT NRA addon table2 weekly | USD [[FACT:fed.fit.nra.addon.table2.weekly=309.60]] | 2026-01-01 to 2026-12-31 | withholding | S10 | Table 2: 2020+ W-4 or first paid 2020+. Added to wages for the FIT computation only (not on W-2, no FICA/FUTA effect); not applied to 22%/37% supplemental. Annual = single standard deduction [[FACT:fed.fit.std_deduction.single=16,100]]. |
| FIT NRA addon table2 biweekly | USD [[FACT:fed.fit.nra.addon.table2.biweekly=619.20]] | 2026-01-01 to 2026-12-31 | withholding | S10 | Table 2: 2020+ W-4 or first paid 2020+. Added to wages for the FIT computation only (not on W-2, no FICA/FUTA effect); not applied to 22%/37% supplemental. Annual = single standard deduction [[FACT:fed.fit.std_deduction.single=16,100]]. |
| FIT NRA addon table2 semimonthly | USD [[FACT:fed.fit.nra.addon.table2.semimonthly=670.80]] | 2026-01-01 to 2026-12-31 | withholding | S10 | Table 2: 2020+ W-4 or first paid 2020+. Added to wages for the FIT computation only (not on W-2, no FICA/FUTA effect); not applied to 22%/37% supplemental. Annual = single standard deduction [[FACT:fed.fit.std_deduction.single=16,100]]. |
| FIT NRA addon table2 monthly | USD [[FACT:fed.fit.nra.addon.table2.monthly=1,341.70]] | 2026-01-01 to 2026-12-31 | withholding | S10 | Table 2: 2020+ W-4 or first paid 2020+. Added to wages for the FIT computation only (not on W-2, no FICA/FUTA effect); not applied to 22%/37% supplemental. Annual = single standard deduction [[FACT:fed.fit.std_deduction.single=16,100]]. |
| FIT NRA addon table2 quarterly | USD [[FACT:fed.fit.nra.addon.table2.quarterly=4,025]] | 2026-01-01 to 2026-12-31 | withholding | S10 | Table 2: 2020+ W-4 or first paid 2020+. Added to wages for the FIT computation only (not on W-2, no FICA/FUTA effect); not applied to 22%/37% supplemental. Annual = single standard deduction [[FACT:fed.fit.std_deduction.single=16,100]]. |
| FIT NRA addon table2 semiannual | USD [[FACT:fed.fit.nra.addon.table2.semiannual=8,050]] | 2026-01-01 to 2026-12-31 | withholding | S10 | Table 2: 2020+ W-4 or first paid 2020+. Added to wages for the FIT computation only (not on W-2, no FICA/FUTA effect); not applied to 22%/37% supplemental. Annual = single standard deduction [[FACT:fed.fit.std_deduction.single=16,100]]. |
| FIT NRA addon table2 annual | USD [[FACT:fed.fit.nra.addon.table2.annual=16,100]] | 2026-01-01 to 2026-12-31 | withholding | S10 | Table 2: 2020+ W-4 or first paid 2020+. Added to wages for the FIT computation only (not on W-2, no FICA/FUTA effect); not applied to 22%/37% supplemental. Annual = single standard deduction [[FACT:fed.fit.std_deduction.single=16,100]]. |
| FIT NRA addon table2 daily | USD [[FACT:fed.fit.nra.addon.table2.daily=61.90]] | 2026-01-01 to 2026-12-31 | withholding | S10 | Table 2: 2020+ W-4 or first paid 2020+. Added to wages for the FIT computation only (not on W-2, no FICA/FUTA effect); not applied to 22%/37% supplemental. Annual = single standard deduction [[FACT:fed.fit.std_deduction.single=16,100]]. |
| FIT NRA addon table1 weekly | USD [[FACT:fed.fit.nra.addon.table1.weekly=226.90]] | 2026-01-01 to 2026-12-31 | withholding | S10 | Table 1: first paid before 2020 with no 2020+ W-4. Annual [[FACT:fed.fit.nra.addon.table1.annual=11,800]] = [[FACT:fed.fit.std_deduction.single=16,100]] - [[FACT:fed.fit.allowance.pre2020_value=4,300]]. |
| FIT NRA addon table1 biweekly | USD [[FACT:fed.fit.nra.addon.table1.biweekly=453.80]] | 2026-01-01 to 2026-12-31 | withholding | S10 | Table 1: first paid before 2020 with no 2020+ W-4. Annual [[FACT:fed.fit.nra.addon.table1.annual=11,800]] = [[FACT:fed.fit.std_deduction.single=16,100]] - [[FACT:fed.fit.allowance.pre2020_value=4,300]]. |
| FIT NRA addon table1 semimonthly | USD [[FACT:fed.fit.nra.addon.table1.semimonthly=491.70]] | 2026-01-01 to 2026-12-31 | withholding | S10 | Table 1: first paid before 2020 with no 2020+ W-4. Annual [[FACT:fed.fit.nra.addon.table1.annual=11,800]] = [[FACT:fed.fit.std_deduction.single=16,100]] - [[FACT:fed.fit.allowance.pre2020_value=4,300]]. |
| FIT NRA addon table1 monthly | USD [[FACT:fed.fit.nra.addon.table1.monthly=983.30]] | 2026-01-01 to 2026-12-31 | withholding | S10 | Table 1: first paid before 2020 with no 2020+ W-4. Annual [[FACT:fed.fit.nra.addon.table1.annual=11,800]] = [[FACT:fed.fit.std_deduction.single=16,100]] - [[FACT:fed.fit.allowance.pre2020_value=4,300]]. |
| FIT NRA addon table1 quarterly | USD [[FACT:fed.fit.nra.addon.table1.quarterly=2,950]] | 2026-01-01 to 2026-12-31 | withholding | S10 | Table 1: first paid before 2020 with no 2020+ W-4. Annual [[FACT:fed.fit.nra.addon.table1.annual=11,800]] = [[FACT:fed.fit.std_deduction.single=16,100]] - [[FACT:fed.fit.allowance.pre2020_value=4,300]]. |
| FIT NRA addon table1 semiannual | USD [[FACT:fed.fit.nra.addon.table1.semiannual=5,900]] | 2026-01-01 to 2026-12-31 | withholding | S10 | Table 1: first paid before 2020 with no 2020+ W-4. Annual [[FACT:fed.fit.nra.addon.table1.annual=11,800]] = [[FACT:fed.fit.std_deduction.single=16,100]] - [[FACT:fed.fit.allowance.pre2020_value=4,300]]. |
| FIT NRA addon table1 annual | USD [[FACT:fed.fit.nra.addon.table1.annual=11,800]] | 2026-01-01 to 2026-12-31 | withholding | S10 | Table 1: first paid before 2020 with no 2020+ W-4. Annual [[FACT:fed.fit.nra.addon.table1.annual=11,800]] = [[FACT:fed.fit.std_deduction.single=16,100]] - [[FACT:fed.fit.allowance.pre2020_value=4,300]]. |
| FIT NRA addon table1 daily | USD [[FACT:fed.fit.nra.addon.table1.daily=45.40]] | 2026-01-01 to 2026-12-31 | withholding | S10 | Table 1: first paid before 2020 with no 2020+ W-4. Annual [[FACT:fed.fit.nra.addon.table1.annual=11,800]] = [[FACT:fed.fit.std_deduction.single=16,100]] - [[FACT:fed.fit.allowance.pre2020_value=4,300]]. |
| FIT NRA W-4 rule | [[FACT:fed.fit.nra.w4.rule=Check Single or MFS regardless of marital status; write NRA below Step 4(c); exempt not allowed; Step 3 only for residents of Canada, Mexico, South Korea or India (students/apprentices)]] | from 2020-01-01 | withholding | S11 | Notice 1392 (Rev. 1-2020) still the posted edition. |
| FIT NRA treaty exempt reporting | [[FACT:fed.fit.nra.treaty_exempt.reporting=Treaty-exempt wages claimed on Form 8233 are reported on Form 1042-S (not W-2 box 1); 2026 Forms 1042-S due 2027-03-15 and must be e-filed via IRIS]] | from 2026-01-01 | employer reporting | S12 |  |
| FIT NRA commercial traveler max days | [[FACT:fed.fit.nra.commercial_traveler.max_days=90]] days | from 2026-01-01 |  | S12 | Exception from withholding: NRA present <= [[FACT:fed.fit.nra.commercial_traveler.max_days=90]] days, total pay <= 3,000, foreign employer not engaged in US trade/business. |
| FIT NRA commercial traveler max pay | USD [[FACT:fed.fit.nra.commercial_traveler.max_pay=3,000]] | from 2026-01-01 |  | S12 |  |

## FED.3 Social insurance: unemployment, disability, paid leave and payroll levies

**FICA.** Social security (OASDI): employee [[FACT:fed.fica.oasdi.rate.employee=6.2]] % and employer [[FACT:fed.fica.oasdi.rate.employer=6.2]] % on wages up to the annual base (USD [[FACT:fed.fica.oasdi.wage_base=184,500]] for 2026; USD [[FACT:fed.fica.oasdi.wage_base=192,300]] for 2027, carried with medium confidence, see the gap below). Medicare: employee [[FACT:fed.fica.medicare.rate.employee=1.45]] % and employer [[FACT:fed.fica.medicare.rate.employer=1.45]] %, no base. Additional Medicare tax: employee only, [[FACT:fed.fica.addl_medicare.rate=0.9]] % on wages paid above USD [[FACT:fed.fica.addl_medicare.withholding_threshold=200,000]] in the calendar year, regardless of filing status; no employer match.

```
oasdi_ee   = min(period_FICA_wages, max(0, oasdi_base - ytd_FICA_wages)) x oasdi_rate_ee
medicare   = period_FICA_wages x medicare_rate_ee
addl_med   = max(0, ytd_wages_after - max(addl_threshold, ytd_wages_before)) x addl_medicare_rate
```

**FUTA.** Gross rate [[FACT:fed.futa.rate.gross=6]] % less the maximum credit for State UI [[FACT:fed.futa.credit.max=5.4]] % gives the net [[FACT:fed.futa.rate.net=0.6]] % on the first USD [[FACT:fed.futa.wage_base=7,000]] per employee per year, across all States ([[FACT:multi.futa.wage_base.scope=FUTA 7,000 counts remuneration paid by the employer in the calendar year across all States: one base per employer, not per State; successor carry-over]]). A State with an outstanding Title XII advance reduces the credit (2025 final reductions in the table; 2026 reductions pending, gaps below). Employer only.

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| FICA OASDI rate employee | [[FACT:fed.fica.oasdi.rate.employee=6.2]] % | 2026-01-01 to 2026-12-31 |  | S13 |  |
| FICA OASDI rate employer | [[FACT:fed.fica.oasdi.rate.employer=6.2]] % | 2026-01-01 to 2026-12-31 |  | S13 |  |
| FICA OASDI wage base | USD [[FACT:fed.fica.oasdi.wage_base=184,500]] | 2026-01-01 to 2026-12-31 |  | S13 | Derivation: 60,600 x AWI(2024) 69,846.57 / AWI(1992) 22,935.42 = 184,548.71, rounded to a multiple of 300 = [[FACT:fed.fica.oasdi.wage_base=184,500]]. |
| FICA OASDI wage base | USD [[FACT:fed.fica.oasdi.wage_base=192,300]] | 2027-01-01 to 2027-12-31 |  | S14 | SSA published 2027 figure (cbb.html table 1937-2027). Re-verification on 2026-11-02 blocked (ssa.gov 403); not derived (AWI 2025 not held). |
| FICA medicare rate employee | [[FACT:fed.fica.medicare.rate.employee=1.45]] % | 2026-01-01 to 2026-12-31 |  | S13 | No wage base. |
| FICA medicare rate employer | [[FACT:fed.fica.medicare.rate.employer=1.45]] % | 2026-01-01 to 2026-12-31 |  | S13 |  |
| FICA addl medicare rate | [[FACT:fed.fica.addl_medicare.rate=0.9]] % | 2026-01-01 to 2026-12-31 |  | S13 | Employee only, no employer match. |
| FICA addl medicare withholding threshold | USD [[FACT:fed.fica.addl_medicare.withholding_threshold=200,000]] | 2026-01-01 to 2026-12-31 | withholding | S13 | Wages paid in excess of [[FACT:fed.fica.addl_medicare.withholding_threshold=200,000]] in the calendar year, regardless of filing status. |
| FUTA rate gross | [[FACT:fed.futa.rate.gross=6]] % | from 2025-01-01 |  | S15 |  |
| FUTA credit max | [[FACT:fed.futa.credit.max=5.4]] % | from 2025-01-01 |  | S15 |  |
| FUTA rate net | [[FACT:fed.futa.rate.net=0.6]] % | from 2025-01-01 |  | S15 | Plus any credit reduction for the state of the wages (Schedule A). |
| FUTA wage base | USD [[FACT:fed.futa.wage_base=7,000]] | from 2025-01-01 |  | S15 | Per employee per employer per calendar year across all States. |
| FUTA credit reduction CA | [[FACT:fed.futa.credit_reduction.ca=1.2]] % | 2025-01-01 to 2025-12-31 |  | S16 | FINAL for 2025 (Form 940 for 2025, Schedule A). Source edition partially verified. |
| FUTA credit reduction VI | [[FACT:fed.futa.credit_reduction.vi=4.5]] % | 2025-01-01 to 2025-12-31 |  | S16 | FINAL for 2025, U.S. Virgin Islands. Source edition partially verified. |
| FUTA deposit threshold | USD [[FACT:fed.futa.deposit_threshold=500]] | from 2026-01-01 |  | S17 | Deposit FUTA for a quarter when accumulated liability exceeds [[FACT:fed.futa.deposit_threshold=500]]. Source edition partially verified. |

⚠️ RESEARCH-GAP (non-blocking): FUTA credit reduction CA: not established by the research. Source that would close it: The DOL OUI "FUTA Credit Reductions" page/xlsx after 2026-11-10, or the 2026 Schedule A (Form 940) instructions.

⚠️ RESEARCH-GAP (non-blocking): FUTA credit reduction VI: not established by the research. Source that would close it: Same DOL OUI update after 2026-11-10.

⚠️ RESEARCH-GAP (non-blocking): FICA OASDI wage base next year reverification: not established by the research. Source that would close it: the SSA 2027 COLA fact sheet or contribution-and-benefit-base page, or the 2027 Federal Register notice

## FED.4 Pay statement

There is no federal pay-statement statute ([[FACT:fed.payslip.statute.exists=False]]); the FLSA prescribes records only. Pay-statement content, delivery and language follow the State of the work location (State annexes; Annex MULTI).

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Payslip statute exists | [[FACT:fed.payslip.statute.exists=False]] | from 2026-11-02 |  | S18 | No federal pay-statement content/delivery rule; FLSA prescribes records only. Pay statements = state law. |
| Records flsa retention years | [[FACT:fed.records.flsa.retention_years=3]] years | from 2026-11-02 |  | S18 | 29 CFR 516.5; supplementary records 2 years (516.6). |
| Records IRS retention years | [[FACT:fed.records.irs.retention_years=4]] years | from 2026-01-01 |  | S8 |  |

## FED.5 Statutory reporting

All federal returns are filed by the third-party filing provider (no system integration in scope). Deposit schedule from the lookback period; Form 941 quarterly (Form 944 only on IRS notice); Form 940 annually; W-2/W-3 to SSA in the EFW2 format; ACA Forms 1094-C/1095-C for applicable large employers; new-hire reports to the State new-hire directory.

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Deposit lookback period | [[FACT:fed.deposit.lookback_period=2024-07-01 to 2025-06-30 (Form 941 filers); CY2024 for 943/944/945 filers]] | 2026-01-01 to 2026-12-31 |  | S19 |  |
| Deposit monthly max lookback liability | USD [[FACT:fed.deposit.monthly_max_lookback_liability=50,000]] | from 2026-01-01 |  | S19 | <= [[FACT:fed.deposit.monthly_max_lookback_liability=50,000]] monthly depositor (by the 15th of the following month); > [[FACT:fed.deposit.monthly_max_lookback_liability=50,000]] semiweekly (Wed/Thu/Fri paydays -> following Wednesday; Sat-Tue -> following Friday). |
| Deposit next day threshold | USD [[FACT:fed.deposit.next_day_threshold=100,000]] | from 2026-01-01 |  | S19 | [[FACT:fed.deposit.next_day_threshold=100,000]] or more accumulated on any day -> deposit next business day; deposit holidays = DC legal holidays. |
| Form941 frequency | [[FACT:fed.form941.frequency=quarterly; due last day of the month after the quarter; amounts in cents]] | from 2026-01-01 |  | S17 | Source edition partially verified. |
| Form944 max liability | USD [[FACT:fed.form944.max_liability=1,000]] | from 2026-01-01 |  | S17 | Annual Form 944 only on written IRS notice. Source edition partially verified. |
| Form940 due | [[FACT:fed.form940.due=January 31 (10 more days if all FUTA deposited on time)]] | from 2026-01-01 |  | S17 | Source edition partially verified. |
| W-2 due date | [[FACT:fed.w2.due_date=2027-02-01]] | from 2026-01-01 |  | S20 | TY2026 Copy A to SSA and employee copies. |
| W-2 no withholding threshold | USD [[FACT:fed.w2.no_withholding_threshold=2,000]] | from 2026-01-01 |  | S20 | W-2 required at [[FACT:fed.w2.no_withholding_threshold=2,000]]+ wages even with no withholding (was 600); indexed after 2026. |
| W-2 box12 new codes | [[FACT:fed.w2.box12.new_codes=TP (cash tips reported to employer); TT (qualified overtime compensation); TA (employer Trump-account contributions)]] | from 2026-01-01 | employer reporting | S20 |  |
| W-2 box14b | [[FACT:fed.w2.box14b=Box 14 split into 14a Other and 14b Treasury Tipped Occupation Code(s)]] | from 2026-01-01 | employer reporting | S20 |  |
| ACA ale fte threshold | [[FACT:fed.aca.ale.fte_threshold=50]] employees | from 2025-01-01 |  | S21 | TY2025 instructions (TY2026 edition not yet published). Source edition partially verified. |
| ACA efile threshold | [[FACT:fed.aca.efile_threshold=10]] returns | from 2025-01-01 |  | S21 | Source edition partially verified. |
| ACA affordability rate | [[FACT:fed.aca.affordability.rate=9.96]] % | 2026-01-01 to 2026-12-31 |  | S22 | Required contribution percentage, plan years beginning in 2026. |
| Newhire deadline days | [[FACT:fed.newhire.deadline_days=20]] days | from 1997-10-01 |  | S23 | Or, electronic filers, two monthly transmissions 12-16 days apart; state deadlines shorter per state annex. |
| Newhire fields | [[FACT:fed.newhire.fields=employee name, address, SSN, date services first performed; employer name, address, FEIN]] | from 1997-10-01 |  | S23 |  |
| Reporting agent authorization | [[FACT:fed.reporting_agent.authorization=Form 8655 (Rev. Jan 2024); agent may sign/file 940/941 and deposit; taxpayer stays liable]] | from 2012-11-19 |  | S24 |  |
| Newhire electronic interval | [[FACT:fed.newhire.electronic_interval=Electronic/magnetic filers: two monthly transmissions, not less than 12 nor more than 16 days apart]] | from 1997-10-01 |  | S25 | OCSS employer page restating 42 USC 653a(b)(2). |
| Newhire state penalty max per hire | USD [[FACT:fed.newhire.state_penalty.max_per_hire=25]] | from 1997-10-01 |  | S25 | State civil penalty cap per newly hired employee; 500 USD if failure results from a conspiracy (42 USC 653a(d)). |
| Newhire state penalty conspiracy max per hire | USD [[FACT:fed.newhire.state_penalty.conspiracy.max_per_hire=500]] | from 1997-10-01 |  | S25 |  |
| Newhire form | [[FACT:fed.newhire.form=W-4 copy or an equivalent form; seven federal data elements (employee name, address, SSN, date of hire = first day of services for pay; employer name, address, FEIN)]] | from 1997-10-01 |  | S25 |  |
| EFW2 edition | [[FACT:fed.efw2.edition=SSA Publication No. 42-007, EFW2 Tax Year 2026 (page header dated 2026-09-14; no version change entries yet)]] | from 2026-01-01 |  | S26 |  |
| EFW2 record length | [[FACT:fed.efw2.record_length=512]] bytes | from 2026-01-01 |  | S26 |  |
| EFW2 records | [[FACT:fed.efw2.records=512-byte records in order RA, RE, RW, (RO), (RS), RT, (RU), (RV), RF; RA/RE/RW/RT/RF required; RO/RS/RU/RV optional; RS and RV are not read or processed by SSA or IRS (state-defined)]] | from 2026-01-01 |  | S26 |  |
| EFW2 ty2026 changes | [[FACT:fed.efw2.ty2026_changes=TY2026 changes: RE adds Employer Signature PIN (319-328); RW adds Box 14b Primary/Secondary Treasury Tipped Occupation Code (490-492 / 493-495); RO/RU split Codes A and B into separate money fields (combined A+B field valid through TY2025 only), add money fields for existing Codes J, K, L, P and new Codes TA, TP, TT; SS wage base 184,500; FIRE replaced by IRIS]] | from 2026-01-01 |  | S26 |  |

⚠️ RESEARCH-GAP (non-blocking): Form940 instructions edition: not established by the research. Source that would close it: IRS i940 (2026), usually December-January.

⚠️ RESEARCH-GAP (non-blocking): ACA instructions edition: not established by the research. Source that would close it: IRS i109495c (2026).

## FED.6 Leave

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Fmla weeks | [[FACT:fed.fmla.weeks=12]] weeks | from 1993-08-05 |  | S27 | In a 12-month period; may be unpaid; employer may require substitution of accrued paid leave. |
| Fmla military caregiver weeks | [[FACT:fed.fmla.military_caregiver.weeks=26]] weeks | from 1993-08-05 |  | S27 |  |
| Paid leave private employers exists | [[FACT:fed.paid_leave.private_employers.exists=False]] | from 1993-08-05 |  | S27 | No federal paid sick or annual leave for private employers; contractors under EO 13706 (accrual not transcribed). |
| PFML employee contribution is W-2 wages | [[FACT:fed.pfml.employee_contribution.is_w2_wages=True]] | from 2026-01-01 |  | S20 | State PFML employee contribution and employer voluntary payment are W-2 wages (Rev. Rul. 2025-4, Notice 2026-6). |

⚠️ RESEARCH-GAP (non-blocking): Leave EO 13706 accrual: not established by the research. Source that would close it: 29 CFR 13.5 on eCFR

## FED.7 Termination and final pay

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Final pay rule | [[FACT:fed.final_pay.rule=No federal immediate final-pay rule; wages due by the regular payday; timing and vacation payout are state law]] | from 1989-02-04 |  | S28 |  |
| Warn notice days | [[FACT:fed.warn.notice_days=60]] days | from 1989-02-04 |  | S28 | Pay in lieu = back-pay liability (29 USC 2104). |
| Severance is wages | [[FACT:fed.severance.is_wages=True]] | from 2026-01-01 |  | S29 | Severance is wages for FIT, FICA and FUTA. |

## FED.8 Benefits in kind and taxable wages

Federal exclusions below are the baseline the States conform to or depart from (State annexes carry each State's departures).

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Benefit in kind parking monthly exclusion | USD [[FACT:fed.bik.parking.monthly_exclusion=340]] | from 2026-01-01 |  | S30 |  |
| Benefit in kind transit monthly exclusion | USD [[FACT:fed.bik.transit.monthly_exclusion=340]] | from 2026-01-01 |  | S30 |  |
| Benefit in kind health FSA salary reduction cap | USD [[FACT:fed.bik.health_fsa.salary_reduction_cap=3,400]] | 2026-01-01 to 2026-12-31 |  | S6 |  |
| Benefit in kind health FSA carryover max | USD [[FACT:fed.bik.health_fsa.carryover_max=680]] | 2026-01-01 to 2026-12-31 |  | S6 |  |
| Benefit in kind dependent care exclusion | USD [[FACT:fed.bik.dependent_care.exclusion=7,500]] | from 2026-01-01 |  | S30 | Half for married filing separately; raised by P.L. 119-21. |
| Benefit in kind educational assistance exclusion | USD [[FACT:fed.bik.educational_assistance.exclusion=5,250]] | from 2026-01-01 |  | S30 | Exclusion made permanent. |
| Benefit in kind group term life excluded coverage | USD [[FACT:fed.bik.group_term_life.excluded_coverage=50,000]] | from 2026-01-01 |  | S30 | Imputed cost of coverage above [[FACT:fed.bik.group_term_life.excluded_coverage=50,000]] is FICA wages; FIT withholding not required. |
| Benefit in kind group term life monthly cost per 1000 under 25 | USD [[FACT:fed.bik.group_term_life.monthly_cost_per_1000.under_25=0.05]] | from 2026-01-01 |  | S30 | Pub. 15-B Table 2-2. |
| Benefit in kind group term life monthly cost per 1000 25 29 | USD [[FACT:fed.bik.group_term_life.monthly_cost_per_1000.25_29=0.06]] | from 2026-01-01 |  | S30 | Pub. 15-B Table 2-2. |
| Benefit in kind group term life monthly cost per 1000 30 34 | USD [[FACT:fed.bik.group_term_life.monthly_cost_per_1000.30_34=0.08]] | from 2026-01-01 |  | S30 | Pub. 15-B Table 2-2. |
| Benefit in kind group term life monthly cost per 1000 35 39 | USD [[FACT:fed.bik.group_term_life.monthly_cost_per_1000.35_39=0.09]] | from 2026-01-01 |  | S30 | Pub. 15-B Table 2-2. |
| Benefit in kind group term life monthly cost per 1000 40 44 | USD [[FACT:fed.bik.group_term_life.monthly_cost_per_1000.40_44=0.10]] | from 2026-01-01 |  | S30 | Pub. 15-B Table 2-2. |
| Benefit in kind group term life monthly cost per 1000 45 49 | USD [[FACT:fed.bik.group_term_life.monthly_cost_per_1000.45_49=0.15]] | from 2026-01-01 |  | S30 | Pub. 15-B Table 2-2. |
| Benefit in kind group term life monthly cost per 1000 50 54 | USD [[FACT:fed.bik.group_term_life.monthly_cost_per_1000.50_54=0.23]] | from 2026-01-01 |  | S30 | Pub. 15-B Table 2-2. |
| Benefit in kind group term life monthly cost per 1000 55 59 | USD [[FACT:fed.bik.group_term_life.monthly_cost_per_1000.55_59=0.43]] | from 2026-01-01 |  | S30 | Pub. 15-B Table 2-2. |
| Benefit in kind group term life monthly cost per 1000 60 64 | USD [[FACT:fed.bik.group_term_life.monthly_cost_per_1000.60_64=0.66]] | from 2026-01-01 |  | S30 | Pub. 15-B Table 2-2. |
| Benefit in kind group term life monthly cost per 1000 65 69 | USD [[FACT:fed.bik.group_term_life.monthly_cost_per_1000.65_69=1.27]] | from 2026-01-01 |  | S30 | Pub. 15-B Table 2-2. |
| Benefit in kind group term life monthly cost per 1000 70 plus | USD [[FACT:fed.bik.group_term_life.monthly_cost_per_1000.70_plus=2.06]] | from 2026-01-01 |  | S30 | Pub. 15-B Table 2-2. |
| Benefit in kind trump account employer contribution max | USD [[FACT:fed.bik.trump_account.employer_contribution_max=2,500]] | from 2026-07-04 |  | S31 | Sec. 128 program; W-2 code TA; indexed after 2027. |
| Benefit in kind moving and bicycle excluded | [[FACT:fed.bik.moving_and_bicycle.excluded=False]] | from 2026-01-01 |  | S30 | Moving-expense and bicycle-commuting exclusions eliminated (moving: except Armed Forces / intelligence community). |
| Retirement 401k elective deferral limit | USD [[FACT:fed.retirement.401k.elective_deferral_limit=24,500]] | 2026-01-01 to 2026-12-31 |  | S32 |  |
| Retirement 401k catch up 50 | USD [[FACT:fed.retirement.401k.catch_up_50=8,000]] | 2026-01-01 to 2026-12-31 |  | S32 |  |
| Retirement 401k catch up 60 63 | USD [[FACT:fed.retirement.401k.catch_up_60_63=11,250]] | 2026-01-01 to 2026-12-31 |  | S32 |  |
| Retirement simple deferral limit | USD [[FACT:fed.retirement.simple.deferral_limit=17,000]] | 2026-01-01 to 2026-12-31 |  | S32 | 18,100 for SIMPLE plans with the higher limit. |
| HSA limit self only | USD [[FACT:fed.hsa.limit.self_only=4,400]] | 2026-01-01 to 2026-12-31 |  | S33 |  |
| HSA limit family | USD [[FACT:fed.hsa.limit.family=8,750]] | 2026-01-01 to 2026-12-31 |  | S33 |  |
| Feie amount | USD [[FACT:fed.feie.amount=132,900]] | 2026-01-01 to 2026-12-31 |  | S34 | Rev. Proc. 2025-32 sec. 911 item, also stated in (same document, item.38). Foreign earned income exclusion; employer may stop FIT withholding on the employee statement. |

⚠️ RESEARCH-GAP (non-blocking): Benefit in kind mileage rate: not established by the research. Source that would close it: The IRS 2026 standard mileage rate notice.

## FED.9 Deductions and garnishments

The federal Consumer Credit Protection Act sets the floor; a State may be stricter (State annexes). An IRS levy is not subject to the CCPA cap: the employee keeps only the exempt amount from the Publication 1494 tables (selected rows below). Interstate income-withholding orders follow Annex MULTI.

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| CCPA max rate | [[FACT:fed.ccpa.max_rate=25]] % | from 1970-07-01 |  | S35 | Lesser of [[FACT:fed.ccpa.max_rate=25]] % of weekly disposable earnings or the amount above 30 x [[FACT:fed.minwage.hourly=7.25]]. |
| CCPA protected weekly | USD [[FACT:fed.ccpa.protected_weekly=217.50]] | from 1970-07-01 |  | S35 | 30 x [[FACT:fed.minwage.hourly=7.25]]. |
| CCPA support max rate with dependents | [[FACT:fed.ccpa.support.max_rate.with_dependents=50]] % | from 1970-07-01 |  | S35 | 55% with arrears older than 12 weeks. |
| CCPA support max rate without dependents | [[FACT:fed.ccpa.support.max_rate.without_dependents=60]] % | from 1970-07-01 |  | S35 | 65% with arrears older than 12 weeks. |
| CCPA support arrears addon | [[FACT:fed.ccpa.support.arrears_addon=5]] % | from 1970-07-01 |  | S35 | +5 points (55/65) where arrears older than 12 weeks. |
| Levy exempt single 0dep daily | USD [[FACT:fed.levy.exempt.single_0dep.daily=61.92]] | 2026-01-01 to 2026-12-31 |  | S36 | Pub. 1494 (2026); MFS = Single. Weekly = [[FACT:fed.fit.std_deduction.single=16,100]]/52; monthly = [[FACT:fed.fit.std_deduction.single=16,100]]/12. |
| Levy exempt single 0dep weekly | USD [[FACT:fed.levy.exempt.single_0dep.weekly=309.62]] | 2026-01-01 to 2026-12-31 |  | S36 | Pub. 1494 (2026); MFS = Single. Weekly = [[FACT:fed.fit.std_deduction.single=16,100]]/52; monthly = [[FACT:fed.fit.std_deduction.single=16,100]]/12. |
| Levy exempt single 0dep biweekly | USD [[FACT:fed.levy.exempt.single_0dep.biweekly=619.23]] | 2026-01-01 to 2026-12-31 |  | S36 | Pub. 1494 (2026); MFS = Single. Weekly = [[FACT:fed.fit.std_deduction.single=16,100]]/52; monthly = [[FACT:fed.fit.std_deduction.single=16,100]]/12. |
| Levy exempt single 0dep semimonthly | USD [[FACT:fed.levy.exempt.single_0dep.semimonthly=670.83]] | 2026-01-01 to 2026-12-31 |  | S36 | Pub. 1494 (2026); MFS = Single. Weekly = [[FACT:fed.fit.std_deduction.single=16,100]]/52; monthly = [[FACT:fed.fit.std_deduction.single=16,100]]/12. |
| Levy exempt single 0dep monthly | USD [[FACT:fed.levy.exempt.single_0dep.monthly=1,341.67]] | 2026-01-01 to 2026-12-31 |  | S36 | Pub. 1494 (2026); MFS = Single. Weekly = [[FACT:fed.fit.std_deduction.single=16,100]]/52; monthly = [[FACT:fed.fit.std_deduction.single=16,100]]/12. |
| Levy exempt per dependent daily | USD [[FACT:fed.levy.exempt.per_dependent.daily=20.38]] | 2026-01-01 to 2026-12-31 |  | S36 | 5,300/52 weekly; 5,300/12 monthly. |
| Levy exempt per dependent weekly | USD [[FACT:fed.levy.exempt.per_dependent.weekly=101.92]] | 2026-01-01 to 2026-12-31 |  | S36 | 5,300/52 weekly; 5,300/12 monthly. |
| Levy exempt per dependent biweekly | USD [[FACT:fed.levy.exempt.per_dependent.biweekly=203.85]] | 2026-01-01 to 2026-12-31 |  | S36 | 5,300/52 weekly; 5,300/12 monthly. |
| Levy exempt per dependent semimonthly | USD [[FACT:fed.levy.exempt.per_dependent.semimonthly=220.83]] | 2026-01-01 to 2026-12-31 |  | S36 | 5,300/52 weekly; 5,300/12 monthly. |
| Levy exempt per dependent monthly | USD [[FACT:fed.levy.exempt.per_dependent.monthly=441.67]] | 2026-01-01 to 2026-12-31 |  | S36 | 5,300/52 weekly; 5,300/12 monthly. |
| Levy exempt MFJ 0dep weekly | USD [[FACT:fed.levy.exempt.mfj_0dep.weekly=619.23]] | 2026-01-01 to 2026-12-31 |  | S36 |  |
| Levy exempt MFJ 0dep monthly | USD [[FACT:fed.levy.exempt.mfj_0dep.monthly=2,683.33]] | 2026-01-01 to 2026-12-31 |  | S36 |  |
| Levy exempt HoH 0dep weekly | USD [[FACT:fed.levy.exempt.hoh_0dep.weekly=464.42]] | 2026-01-01 to 2026-12-31 |  | S36 |  |
| IWO priority | [[FACT:fed.iwo.priority=IWO for support ranks before other garnishments, except an IRS levy served before the underlying support order]] | 2026-01-01 to 2026-12-31 |  | S36 | Stated in (Pub. 1494 row) citing the OCSS employer page. |
| IWO omb expiry | [[FACT:fed.iwo.omb_expiry=2029-08-31]] | 2026-08-25 to 2029-08-31 | employer withholding | S37 | OMB 0970-0154 approved without change 2026-08-25; current form extended one year while states reprogram the revised (gig-worker fields) IWO/e-IWO. Supersedes. |

⚠️ RESEARCH-GAP (non-blocking): IWO revised form go live: not established by the research. Source that would close it: An OCSE Action Transmittal implementing ICR 202607-0970-002.

## FED.10 Collective agreements and prevailing wage

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Cba scope | [[FACT:fed.cba.scope=A CBA binds the certified bargaining unit only; no sector-wide extension mechanism]] | from 2026-01-01 |  | S38 |  |
| Davis bacon contract threshold | USD [[FACT:fed.davis_bacon.contract_threshold=2,000]] | from 2026-01-01 |  | S39 | Federal construction contracts over [[FACT:fed.davis_bacon.contract_threshold=2,000]]. |
| Davis bacon certified payroll frequency | [[FACT:fed.davis_bacon.certified_payroll.frequency=weekly, to the contracting agency; prime responsible for subcontractors; optional form WH-347; records 3 years]] | from 2023-10-23 |  | S40 |  |

## FED.11 Indexation

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Indexation caliber | [[FACT:fed.indexation.caliber=C-CPI-U (chained CPI-U) under 26 U.S.C. 1(f)(3)]] | from 2026-01-01 |  | S41 | Rev. Proc. 2025-32 applies it for 2026. OASDI base indexed on AWI. FLSA minimum wage, CCPA multiplier and the [[FACT:fed.exempt.salary_floor.weekly=684]] salary floor are NOT indexed. |
| Indexation OASDI caliber | [[FACT:fed.indexation.oasdi_caliber=National Average Wage Index (AWI), base rounded to a multiple of 300]] | from 2026-01-01 |  | S42 |  |

⚠️ RESEARCH-GAP (non-blocking): Indexation next year: not established by the research. Source that would close it: IRS releases expected Nov-Dec 2026: the TY2027 Rev. Proc., the 2027 retirement-plan limits notice and the 2027 Pub. 15-T (draft or final).

## FED.12 Payroll data protection and records

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| SSN truncation format | [[FACT:fed.ssn.truncation.format=XXX-XX-1234 (TTIN); allowed on employee W-2 copies only; never on Copy A; EIN never truncated]] | from 2019-07-03 |  | S43 |  |

## FED.13 Live legal change

P.L. 119-21 is in force. Its tips and overtime deductions operate at **assessment** level: they reach withholding only through the employee's W-4 Step 4(b); the employer duty is **reporting** (W-2 box 12 codes and box 14b). Do not build them as payroll deductions; tips and overtime stay fully subject to FICA.

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Plaw119 21 qualified tips deduction cap | USD [[FACT:fed.plaw119_21.qualified_tips.deduction_cap=25,000]] | 2025-01-01 to 2028-12-31 | assessment | S31 | IN FORCE (enacted 2025-07-04). Reaches withholding only via W-4 Step 4(b); employer reporting via W-2 TP/14b; tips stay fully FICA-subject. Do NOT model as a payroll deduction. |
| Plaw119 21 qualified overtime deduction cap | USD [[FACT:fed.plaw119_21.qualified_overtime.deduction_cap=12,500]] | 2025-01-01 to 2028-12-31 | assessment | S31 | 25,000 MFJ. Employer reporting via W-2 TT; overtime stays fully FICA-subject. |
| Plaw119 21 qualified overtime deduction cap MFJ | USD [[FACT:fed.plaw119_21.qualified_overtime.deduction_cap_mfj=25,000]] | 2025-01-01 to 2028-12-31 | assessment | S31 |  |
| Plaw119 21 reporting penalty relief | [[FACT:fed.plaw119_21.reporting_penalty_relief=TY2025 only (Notice 2025-62); separate reporting of tips/TTOC/overtime mandatory from TY2026]] | 2025-01-01 to 2025-12-31 | employer reporting | S44 |  |

## FED.14 Authority worked examples (oracle values)

Pub. 15-T 2026 publishes two worked examples, recorded below as oracle values: a non-resident alien paid weekly (USD [[FACT:fed.oracle.pub15t.nra_example.wages=526.90]] after the add-on, withholding USD [[FACT:fed.oracle.pub15t.nra_example.withholding=31]] from the wage-bracket table) and a tribal gaming payment (USD [[FACT:fed.oracle.pub15t.tribal_example.payment=6,000]], withholding USD [[FACT:fed.oracle.pub15t.tribal_example.withholding=584.09]]). No full percentage-method example is published; the percentage method is reproduced from Worksheet 1A and the tables in FED.2 in Module 12 (worked examples). The IRS Tax Withholding Estimator is not an oracle.

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Oracle Pub. 15-T NRA example wages | USD [[FACT:fed.oracle.pub15t.nra_example.wages=526.90]] | from 2026-01-01 |  | S45 | Weekly wages 300 + Table 1 add-on [[FACT:fed.fit.nra.addon.table1.weekly=226.90]] = [[FACT:fed.oracle.pub15t.nra_example.wages=526.90]] (Pub. 15-T 2026 example). |
| Oracle Pub. 15-T NRA example withholding | USD [[FACT:fed.oracle.pub15t.nra_example.withholding=31]] | from 2026-01-01 |  | S45 | Wage-bracket result for [[FACT:fed.oracle.pub15t.nra_example.wages=526.90]] weekly; residual none recorded. |
| Oracle Pub. 15-T tribal example payment | USD [[FACT:fed.oracle.pub15t.tribal_example.payment=6,000]] | from 2026-01-01 |  | S45 | Tribal monthly gaming payment example. |
| Oracle Pub. 15-T tribal example withholding | USD [[FACT:fed.oracle.pub15t.tribal_example.withholding=584.09]] | from 2026-01-01 |  | S45 |  |

## FED.15 Special populations

All special populations are in scope. Federal rules are below; State rules are in the State annexes. US citizens working abroad: withholding may stop on the employee's foreign-earned-income-exclusion statement (exclusion USD [[FACT:fed.feie.amount=132,900]] for 2026).

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Household FICA cash threshold | USD [[FACT:fed.household.fica_cash_threshold=3,000]] | 2026-01-01 to 2026-12-31 |  | S29 | FICA if cash wages [[FACT:fed.household.fica_cash_threshold=3,000]]+ in 2026 (exempt under 18 unless principal occupation); FIT only by agreement; Schedule H. |
| Household FUTA quarter threshold | USD [[FACT:fed.household.futa_quarter_threshold=1,000]] | from 2026-01-01 |  | S29 | FUTA if [[FACT:fed.household.futa_quarter_threshold=1,000]]+ cash wages in any quarter of current or prior year. |
| Agricultural per worker threshold | USD [[FACT:fed.agricultural.per_worker_threshold=150]] | from 2026-01-01 |  | S46 | Cash wages [[FACT:fed.agricultural.per_worker_threshold=150]]+ to a farmworker in a year, or 2,500+ total farm pay, make cash wages subject to FICA and FIT; Form 943. |
| Agricultural total threshold | USD [[FACT:fed.agricultural.total_threshold=2,500]] | from 2026-01-01 |  | S46 |  |
| Agricultural FUTA quarter threshold | USD [[FACT:fed.agricultural.futa_quarter_threshold=20,000]] | from 2026-01-01 |  | S46 | Or 10+ farmworkers on some part of a day in 20+ weeks. |
| Election worker FICA threshold | USD [[FACT:fed.election_worker.fica_threshold=2,500]] | 2026-01-01 to 2026-12-31 |  | S8 |  |
| Tips reporting threshold monthly | USD [[FACT:fed.tips.reporting_threshold_monthly=20]] | from 2026-01-01 |  | S8 | Tips of [[FACT:fed.tips.reporting_threshold_monthly=20]]+ in a month are subject to FIT/FICA. |
| Minister withholding | [[FACT:fed.minister.withholding=No FIT, social security or Medicare withholding (SE tax; voluntary FIT withholding agreement allowed); parsonage allowance excluded from W-2 box 1]] | from 2026-01-01 |  | S47 |  |
| Statutory employee treatment | [[FACT:fed.statutory_employee.treatment=FICA withheld, no FIT withholding; W-2 box 13 checked; FUTA for drivers and traveling salespersons only]] | from 2026-01-01 |  | S48 |  |
| Family employment treatment | [[FACT:fed.family_employment.treatment=Child under 18 of a sole proprietor/parents-only partnership: FICA exempt, FUTA exempt under 21; spouse: FUTA exempt; parent employed by child: FUTA exempt]] | from 2026-01-01 |  | S29 |  |
| Students treatment | [[FACT:fed.students.treatment=Private school/college students: FIT withheld, FICA and FUTA exempt; public school: FICA exempt unless sec. 218 agreement; work-experience full-time student: FICA taxable]] | from 2026-01-01 |  | S29 |  |
| Government employee treatment | [[FACT:fed.government_employee.treatment=FIT withheld; no FUTA; FICA with sec. 218 / Medicare-only exceptions]] | from 2026-01-01 |  | S29 |  |

## FED.16 Language

English is the only federal official language and places no obligation on private employers; no federal instrument fixes pay-statement content or language. IRS and SSA filings are in English. Second-language duties attach to State notices and posters only (State annexes).

## FED.S Sources

| Ref | Instrument | Article / section | Authority |
|---|---|---|---|
| S1 | 29 U.S.C. 206(a)(1)(C) FLSA minimum wage (U.S. Code 2024 ed., govinfo) + DOL WHD Minimum Wage page | 29 U.S.C. 206(a)(1)(C) | U.S. Congress (OLRC/GPO); U.S. DOL Wage and Hour Division |
| S2 | 29 U.S.C. 207(a)(1) FLSA overtime (U.S. Code 2024 ed.) | 29 U.S.C. 207(a)(1) | U.S. Congress (OLRC/GPO) |
| S3 | 29 U.S.C. 203(m),(t) tip credit / tipped employee + DOL WHD Fact Sheet #15 | 29 U.S.C. 203(m)(2), 203(t); FS #15 | U.S. Congress; U.S. DOL WHD |
| S4 | 29 CFR 541.600 Amount of salary required (white-collar exemption), eCFR current | 29 CFR 541.600(a)-(b) | U.S. DOL (eCFR, OFR/GPO) |
| S5 | IRS Publication 15-T (2026) Federal Income Tax Withholding Methods - Worksheet 1A and Annual Percentage Method tables (Automated Payroll) | Sec. 1 Worksheet 1A; 2026 Percentage Method Tables for Automated Payroll Systems (p.12) | IRS |
| S6 | IRS Rev. Proc. 2025-32 (2026 inflation adjustments) - local copy re-acquired | Sec. 3 .01 tax rate tables, standard deduction, .xx 125(i) FSA, 132(f) transportation | IRS |
| S7 | IRS Publication 15-T (2026) Federal Income Tax Withholding Methods | Rounding rules; NRA withholding adjustment; supplemental wages; Tax Withholding Estimator reference | IRS |
| S8 | IRS Publication 15 (2026) Employer's Tax Guide - What's New: supplemental wage rates, backup withholding, information-return threshold, household/election … | What's New; sec. 7 Supplemental Wages; Backup withholding | IRS |
| S9 | IRS Form W-4 (2026) Employee's Withholding Certificate | Steps 1-5; Exempt checkbox below Step 4(c); Step 4(b) Deductions Worksheet | IRS |
| S10 | IRS Publication 15-T (2026) - Withholding Adjustment for Nonresident Alien Employees (Tables 1 and 2) | Sec. 1, Withholding Adjustment for Nonresident Alien Employees, Tables 1-2 (p.5-6) | IRS |
| S11 | IRS Notice 1392 (Rev. January 2020) Supplemental Form W-4 Instructions for Nonresident Aliens | Steps 1(c), 2, 3, 4(a)-(c); Exempt | IRS |
| S12 | IRS Publication 515 (2026) Withholding of Tax on Nonresident Aliens and Foreign Entities | What's New (IRIS for 1042-S); Pay for personal services | IRS |
| S13 | IRS Instructions for Form 941 (Rev. March 2026) - FICA rates and wage base, Additional Medicare Tax | What's New; lines 5a-5d | IRS |
| S14 | SSA Contribution and Benefit Base page | 2026 and 2027 rows | SSA |
| S15 | Instructions for Form 940 (2025) | FUTA rate; credit reduction; rounding option | IRS |
| S16 | DOL ETA/OUI FUTA Credit Reductions page + Potential 2026 FUTA Credit Reductions table (xlsx, dated 2026-01-15) + Historical 2010-2025 table | FUTA 3302(c)(2), 3302(d)(3); potential_credit_states_2026.xlsx; reduced_credit_states_2010-2025.xlsx | U.S. Department of Labor, ETA Office of Unemployment Insurance |
| S17 | IRS Pub. 15 (2026) / Instructions for Form 940 (2025) - Form 940 and Form 944 filing rules | Pub. 15 sec. 12 and sec. 14; i940 What's New, Credit reduction state | IRS |
| S18 | 29 CFR 516.5 Records to be preserved 3 years (FLSA), eCFR current | 29 CFR 516.5(a)-(c); eCFR current as of retrieval; original promulgation date not printed in the retrieved rendering - effective_from = date verified in force | U.S. DOL (eCFR) |
| S19 | IRS Publication 15 (2026) sec. 11 Depositing Taxes - lookback, monthly/semiweekly schedule, 100,000 next-day rule, 2026 DC legal holidays | Sec. 11 When To Deposit; Table 2 Semiweekly Deposit Schedule; Legal holiday | IRS |
| S20 | IRS General Instructions for Forms W-2 and W-3 (2026) - P.L. 119-21 reporting changes, due dates, SSN truncation | What's New; Due date for filing with SSA; Box 12 codes TA/TP/TT; Box 14a/14b; Truncating SSN | IRS |
| S21 | IRS Instructions for Forms 1094-C and 1095-C (2025, rev. 2025-10-30) - ALE reporting | What's New (alternative furnishing, Notice 2025-15); When to file; Electronic filing 10 or more | IRS |
| S22 | IRS Rev. Proc. 2025-25 - 2026 ACA applicable percentage table and required contribution percentage | Sec. 3.01-3.02 | IRS |
| S23 | 42 U.S.C. 653a(b)-(c) employer new-hire reporting (U.S. Code 2024 ed.) - local copy | 42 U.S.C. 653a(b)(1)(A)-(B), (b)(2), (c) | U.S. Congress (OLRC/GPO) |
| S24 | Rev. Proc. 2012-32 Reporting Agent Authorization (Form 8655) | Sec. 1.01, 5.04, 5.05, 15 | IRS |
| S25 | OCSS New Hire Reporting - employer page and Answers to Employer Questions | Employer questions: data elements, timing, electronic transmissions, penalties, multistate employers, form | HHS Administration for Children and Families, Office of Child Support Services |
| S26 | SSA EFW2 Specifications for Filing Forms W-2 Electronically, Tax Year 2026 (Pub. 42-007) - ACCESS gap | Whole document (RA/RE/RW/RO/RS/RT/RU/RV/RF records) | Social Security Administration |
| S27 | 29 U.S.C. 2612 FMLA leave entitlement (U.S. Code 2024 ed.) | 29 U.S.C. 2612(a)(1), (c), (d)(2) | U.S. Congress (OLRC/GPO) |
| S28 | 29 U.S.C. 2102 WARN Act notice (U.S. Code 2024 ed.) + DOL Last Paycheck page | 29 U.S.C. 2102(a); dol.gov/general/topic/wages/lastpaycheck | U.S. Congress; U.S. DOL |
| S29 | IRS Publication 15 (2026) sec. 15 Special Rules for Various Types of Services and Payments (table) + sec. 3 family employees + state/local government employers | Sec. 3 (Child employed by parents); sec. 15 table pp. 47-52; State and local government employers | IRS |
| S30 | IRS Publication 15-B (2026) Employer's Tax Guide to Fringe Benefits | What's New; Table 2-1; Table 2-2 group-term life | IRS |
| S31 | P.L. 119-21 (One Big Beautiful Bill Act, enacted 2025-07-04) - payroll-relevant changes as implemented in IRS 2026 employer publications | W-2/W-3 instructions 2026 What's New; Pub. 15 2026 What's New; Pub. 15-B 2026 What's New; Pub. 15-T 2026 What's New | IRS (implementing P.L. 119-21) |
| S32 | IRS IR-2025-111 (2025-11-13): 401(k) limit [[FACT:fed.retirement.401k.elective_deferral_limit=24,500]] for 2026; Notice 2025-67 referenced | Highlights of changes for 2026 | IRS |
| S33 | Rev. Proc. 2025-19 (2026 HSA limits) | sec.3.01 223(b)(2)(A)/(B) | IRS |
| S34 | Rev. Proc. 2025-32 re-read (payroll-relevant items) | sec.1; 4.09, 4.15, 4.16, 4.27, 4.28, 4.39 | IRS |
| S35 | 15 U.S.C. 1673 CCPA restriction on garnishment (U.S. Code 2024 ed.) - local copy | 15 U.S.C. 1673(a), (b)(2) | U.S. Congress (OLRC/GPO) |
| S36 | IRS Publication 1494 (2026) Tables for Figuring Amount Exempt from Levy on Wages (Forms 668-W) | Table 1 (Single, MFJ, HoH, MFS by pay period and dependents) | IRS |
| S37 | OMB/OIRA ICR 202607-0970-002 Income Withholding for Support (IWO), OMB 0970-0154 - OIRA conclusion (reginfo.gov, live page) | ICR 202607-0970-002, OIRA Conclusion | OMB Office of Information and Regulatory Affairs / HHS ACF OCSE |
| S38 | 29 U.S.C. 159(a) NLRA exclusive representation | 159(a) | US Congress (GovInfo US Code 2024) |
| S39 | 40 U.S.C. 3142 Davis-Bacon Act prevailing wages | 3142(a); (c)(1) | US Congress (GovInfo US Code 2024) |
| S40 | 29 CFR 5.5(a)(3) Davis-Bacon contract clauses - payrolls and basic records, weekly certified payroll (eCFR current) | 29 CFR 5.5(a)(3)(i)-(ii) | U.S. DOL (eCFR) |
| S41 | 26 USC 1(f)(3) cost-of-living adjustment uses C-CPI-U (LII republication of US Code) | 1(f)(3)(A)-(C) | Cornell LII (republication of US Code; uscode.house.gov returned 404 in pass 1) |
| S42 | SSA notice: Cost-of-Living Increase and Other Determinations for 2026 (Federal Register 90 FR 49047, Doc. 2025-19763) | OASDI Contribution and Benefit Base - Computation (sec. 230(b) Social Security Act) | Social Security Administration |
| S43 | 26 CFR 301.6109-4 IRS truncated taxpayer identification numbers (TTIN), eCFR current | 301.6109-4(a), (b)(2), (c) Example; source T.D. 9675 (79 FR 41131, 2014-07-15) as amended by T.D. 9861 (84 FR 31720, 2019-07-03) | Treasury/IRS (eCFR) |
| S44 | IRS Notice 2025-62 - penalty relief for TY2025 reporting of qualified tips and qualified overtime (P.L. 119-21 secs. 70201/70202) | Secs. 1-3 | IRS |
| S45 | IRS Publication 15-T (2026) worked examples and Worksheet 1A constants | Worksheet 1A lines 1g/1k; NRA example; Indian gaming example | IRS |
| S46 | IRS Publication 15 (2026) farmwork tests and Form 943; IRS About Pub. 51 (discontinued) | Farmwork $150/$2,500 tests; Form 943; FUTA farmworkers test; about-publication-51 Recent developments | IRS |
| S47 | IRS Publication 15-A (2026) sec.4 Religious exemptions and special rules for ministers | section 4 | IRS |
| S48 | IRS Publication 15-A (2026) Employer's Supplemental Tax Guide - statutory employees | Statutory employees (four categories; income tax; reporting) | IRS |
