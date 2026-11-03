# VALIDATION — Colombia design v2.0

**Reference:** an independent calculation written from the statutes (separate code, not derived from this design), on the cases of the validation suite and the research examples (minimum wage, all-inclusive, 4 / 10 / 16–20 / 25 SMMLV bands, overtime and the 14 / 15 July 2026 change, transport allowance at 2 SMMLV, art. 114-1, Law 1393, service bonus, severance savings and interest, vacation, illness, maternity, art. 64 indemnity, contributor type 51, the 18 art. 383 table boundaries), with the 790 / 1,340 UVT caps tracked year-to-date (same pay since 1 January). Design checks by hand calculation from the law cover what the suite does not exercise (Procedure 2, retirement bonus, short service, projection, 204-UVT test, rounding, gross / net).

**What the sweep proves.** The matrices are generated from the WTC columns, so their content is equal by construction; the sweep runs each row through the engine and checks the mechanism (bases, floors, the Law 1393 excess, routing, signs) against the flags.

## Results

```
co_design_v2.json: 79 regulations; WTC CO-WTC-001-v1.9.xlsx: 405 rows, 298 active

=== reproduction: v1.2-faithful variant (v1.2 IDs, ordinals and formulas) ===
[a] order check (v1.2): 47 defect(s)
    9170015 (ordinal 15) reads $R156: posted only at ordinal 86
    9170015 (ordinal 15) reads $R320: posted only at ordinal 82
    9170015 (ordinal 15) reads $R321: posted only at ordinal 83
    9170015 (ordinal 15) reads $R322: posted only at ordinal 84
    9170015 (ordinal 15) reads $R323: posted only at ordinal 85
    9170015 (ordinal 15) reads $R324: posted only at ordinal 85
    9170015 (ordinal 15) reads $R326: posted only at ordinal 93
    9170015 (ordinal 15) reads $R327: posted only at ordinal 93, 93
    9170015 (ordinal 15) reads $R330: posted only at ordinal 94
    9170015 (ordinal 15) reads $R338: posted only at ordinal 96
    9170015 (ordinal 15) reads $R339: posted only at ordinal 91
    9170016 (ordinal 16) reads $R323: posted only at ordinal 85
    9170021 (ordinal 21) reads $R323: posted only at ordinal 85
    9170021 (ordinal 21) reads $R326: posted only at ordinal 93
    9170021 (ordinal 21) reads $R327: posted only at ordinal 93, 93
    9170021 (ordinal 21) reads $R330: posted only at ordinal 94
    9170021 (ordinal 21) reads $R338: posted only at ordinal 96
    9170023 (ordinal 23) reads $R156: posted only at ordinal 86
    9170023 (ordinal 23) reads $R323: posted only at ordinal 85
    9170023 (ordinal 23) reads $R324: posted only at ordinal 85
    9170026 (ordinal 26) reads $R323: posted only at ordinal 85
    9170026 (ordinal 26) reads $R326: posted only at ordinal 93
    9170026 (ordinal 26) reads $R327: posted only at ordinal 93, 93
    9170026 (ordinal 26) reads $R330: posted only at ordinal 94
    9170027 (ordinal 27) reads $R323: posted only at ordinal 85
    9170027 (ordinal 27) reads $R326: posted only at ordinal 93
    9170027 (ordinal 27) reads $R327: posted only at ordinal 93, 93
    9170027 (ordinal 27) reads $R330: posted only at ordinal 94
    9170028 (ordinal 28) reads $R338: posted only at ordinal 96
    9170039 (ordinal 39) reads $58127: posted only at ordinal 97
    9170049 (ordinal 49) reads $58137: posted only at ordinal 97
    9170049 (ordinal 49) reads $58138: posted only at ordinal 97
    9170049 (ordinal 49) reads $58139: posted only at ordinal 97
    9170051 (ordinal 51) reads $R156: posted only at ordinal 86
    9170051 (ordinal 51) reads $R320: posted only at ordinal 82
    9170051 (ordinal 51) reads $R323: posted only at ordinal 85
    9170051 (ordinal 51) reads $R324: posted only at ordinal 85
    9170051 (ordinal 51) reads $R326: posted only at ordinal 93
    9170051 (ordinal 51) reads $R327: posted only at ordinal 93, 93
    9170051 (ordinal 51) reads $R330: posted only at ordinal 94
    9170051 (ordinal 51) reads $R338: posted only at ordinal 96
    9170051 (ordinal 51) reads $R339: posted only at ordinal 91
    9170064 (ordinal 64) reads $R339: posted only at ordinal 91
    9170065 (ordinal 65) reads $R320: posted only at ordinal 82
    9170065 (ordinal 65) reads $R320: posted only at ordinal 82
    9170065 (ordinal 65) reads $R320: posted only at ordinal 82
    9170081 (ordinal 81) reads $R323: posted only at ordinal 85
[b] scenarios (v1.2, monthly cases): 59 cases, 2153 values compared, 11 difference(s)
    ('C23', 'ret_exenta_25', 8545991.24, 8545991.25)
    ('C23', 'ret_beneficios_aplicados', 8545991.24, 8545991.25)
    ('C23', 'ret_base_gravable', 57112946.26, 57112946.25)
    ('C23', 'ret_valor_retener_raw', 16855453.02, 16855453.01)
    ('RC01', 'ret_ingreso_laboral', 2649095.0, 0.0)
    ('RC01', 'ret_incrngo_ss', 192000.0, 128000.0)
    ('RC01', 'ret_subtotal_tras_incrngo', 2457095.0, 1638063.33)
    ('RC01', 'ret_exenta_25', 614273.75, 409515.83)
    ('RC01', 'ret_cap_40_1340', 982838.0, 655225.33)
    ('RC01', 'ret_beneficios_aplicados', 614273.75, 409515.83)
    ('RC01', 'ret_base_gravable', 1842821.25, 1228547.5)
[b] scenarios (v1.2, all cases): 112 cases, 2293 values compared, 34 difference(s)
    C23    ret_exenta_25                independent 8545991.24  engine 8545991.25
    C23    ret_beneficios_aplicados     independent 8545991.24  engine 8545991.25
    C23    ret_base_gravable            independent 57112946.26  engine 57112946.25
    C23    ret_valor_retener_raw        independent 16855453.02  engine 16855453.01
    P01    base_prima_cesantias         independent 3249095  engine 3498190
    P01    prima                        independent 1624548  engine 1749095
    P02    base_prima_cesantias         independent 2000000  engine 2249095
    P02    prima                        independent 1000000  engine 1124548
    P04    base_prima_cesantias         independent 3249095  engine 3498190
    P04    cesantias                    independent 3249095  engine 3498190
    P04    intereses_cesantias          independent 389891  engine 419783
    P05    base_prima_cesantias         independent 2000000  engine 2249095
    P05    cesantias                    independent 2000000  engine 2249095
    P05    intereses_cesantias          independent 240000  engine 269891
    I03    inc_dias_91_180_EPS          independent 500000  engine 583635
    I03    inc_total                    independent 6500000  engine 6583635
    I03    IBC_incapacidad              independent 6500000  engine 6583635
    I04    inc_dias_91_180_EPS          independent 4500000  engine 5252715
    I04    inc_total                    independent 10500000  engine 11252715
    I04    IBC_incapacidad              independent 10505430  engine 11252715
    L15    pension_total                independent 210109  engine 210108
    L21    pension_total                independent 210109  engine 210108
    RC01   ret_ingreso_laboral          independent 2649095.0  engine 0.0
    RC01   ret_incrngo_ss               independent 192000.0  engine 128000.0
    RC01   ret_subtotal_tras_incrngo    independent 2457095.0  engine 1638063.33
    RC01   ret_exenta_25                independent 614273.75  engine 409515.83
    RC01   ret_cap_40_1340              independent 982838.0  engine 655225.33
    RC01   ret_beneficios_aplicados     independent 614273.75  engine 409515.83
    RC01   ret_base_gravable            independent 1842821.25  engine 1228547.5
    RC08   base_prima_cesantias         independent 2649095  engine 2898190
    RC08   prima                        independent 1324548  engine 1449095
    RC12   base_prima_cesantias         independent 2000000  engine 2249095
    RC12   cesantias                    independent 2000000  engine 2249095
    RC12   intereses_cesantias          independent 240000  engine 269891
[c] sweep (v1.2): 2682 checks; 18 difference(s): column N flag Yes: 6; column P flag Yes: 12
    ('R241', 'Pensions & Pension Refunds', 'P', 'Yes', 1000000.0, 0.0)
    ('R242', 'Pensions & Pension Refunds', 'P', 'Yes', 1000000.0, 0.0)
    ('R243', 'Pensions & Pension Refunds', 'P', 'Yes', 1000000.0, 0.0)
    ('R244', 'Pensions & Pension Refunds', 'P', 'Yes', 1000000.0, 0.0)
    ('R245', 'Pensions & Pension Refunds', 'P', 'Yes', 1000000.0, 0.0)
    ('R246', 'Pensions & Pension Refunds', 'P', 'Yes', 1000000.0, 0.0)
    ('R247', 'Pensions & Pension Refunds', 'P', 'Yes', 1000000.0, 0.0)
    ('R248', 'Pensions & Pension Refunds', 'P', 'Yes', 1000000.0, 0.0)
    ('R282', 'Statutory Gratuity, EOS', 'P', 'Yes', 1000000.0, 0.0)
    ('R284', 'Gratuity, EOS, Post-termination, etc.', 'P', 'Yes', 1000000.0, 0.0)
    ('R285', 'Gratuity, EOS, Post-termination, etc.', 'P', 'Yes', 1000000.0, 0.0)
    ('R286', 'Gratuity, EOS, Post-termination, etc.', 'P', 'Yes', 1000000.0, 0.0)

=== v2.0 ===
[a] order check (v2.0): 0 defect(s)
[b] scenarios (v2.0 with the rounding convention of the independent calculation (each share; raw contributions in the non-taxable income)): 112 cases, 2293 values compared, 12 difference(s)
    C23    ret_exenta_25                independent 8545991.24  engine 8545991.25
    C23    ret_beneficios_aplicados     independent 8545991.24  engine 8545991.25
    C23    ret_base_gravable            independent 57112946.26  engine 57112946.25
    C23    ret_valor_retener_raw        independent 16855453.02  engine 16855453.01
    I03    inc_dias_91_180_EPS          independent 500000  engine 583635
    I03    inc_total                    independent 6500000  engine 6583635
    I03    IBC_incapacidad              independent 6500000  engine 6583635
    I04    inc_dias_91_180_EPS          independent 4500000  engine 5252715
    I04    inc_total                    independent 10500000  engine 11252715
    I04    IBC_incapacidad              independent 10505430  engine 11252715
    L15    pension_total                independent 210109  engine 210108
    L21    pension_total                independent 210109  engine 210108
[b] scenarios (v2.0 (one rounding per contributor and fund; contributions withheld in the non-taxable income)): 112 cases, 2293 values compared, 293 difference(s)
      42 x employee share = statutory 4% to the peso (Law 100 arts. 20, 204); the rounding goes to the fund total
      43 x employer share = total rounded once - employee share (Decree 780 art. 3.2.1.5 num. 2)
     198 x non-taxable income = contributions withheld (Tax Code arts. 55, 56)
[b] scenarios (v2.0 against the adjusted independent calculation (one rounding per fund; contributions withheld)): 112 cases, 2293 values compared, 6 difference(s)
    I03    inc_dias_91_180_EPS          independent 500000  engine 583635
    I03    inc_total                    independent 6500000  engine 6583635
    I03    IBC_incapacidad              independent 6500000  engine 6583635
    I04    inc_dias_91_180_EPS          independent 4500000  engine 5252715
    I04    inc_total                    independent 10500000  engine 11252715
    I04    IBC_incapacidad              independent 10505430  engine 11252715
[d] employee / employer coding: 0 error(s)
[d] same check on a copy with the employer health band coded as employee: 1 error(s) (must be > 0)
[b] design checks (hand calculation): 20, 20 exact
    X1 indemnity withholding 20% (T-B): engine 28083333 / expected 28083333; engine 5616667 / expected 5616667
    X2 service bonus read 750,000 -> 0; monthly base excludes it (salary + transport allowance only): engine 0 / expected 0; engine 3249095.0 / expected 3249095.0
    X3 non-resident 20% (severance outside): engine 2000000 / expected 2000000; engine 0 / expected 0
    X4 illness days 91-100 floored at SMMLV / 30 (C-543): engine 583635 / expected 583635; engine 133333 / expected 133333
    X5 all-inclusive: IBC 70%, no transport allowance: engine 17500000 / expected 17500000; engine 0 / expected 0
    X6 day overtime across 15 July 2026 (220 -> 210): engine 349025.97 / expected 349025.97
    X7 apprentice classroom: support 75%, IBC 1 SMMLV, no transport: engine 1313178.75 / expected 1313178.75; engine 1750905 / expected 1750905
    X8 CCG retention bonus Sep 2026 (8,000,000 + 20,000,000 pacted) (engine / CCG; independent 3947554.8): engine 3947554.8 / expected 3947554.8
    X9 CCG habitual bonus Oct 2026 (6,000,000 + 12,000,000) (engine / CCG; independent 1763832.0): engine 1763832.0 / expected 1763832.0
    X10 CCG same with a non-salary pact (engine / CCG; independent 1899912.0): engine 1899912.0 / expected 1899912.0
    X11 CCG all-inclusive 25,000,000, July (engine / CCG; independent 3243282.0): engine 3243282.0 / expected 3243282.0
    X12 Procedure 2 with the service bonus in the monthly base: engine 1057500 / expected 1057500; engine 0 / expected 0
    X13 retirement bonus withheld by Decree 1625 art. 1.2.4.1.8 (0%), outside the monthly base: engine 0 / expected 0; engine 4500000.0 / expected 4500000.0
    X14 average over the months of service when fewer than 12: engine 194649 / expected 194649
    X15 projection option on does not reach Procedure 2: engine 341250 / expected 341250; engine 1.0 / expected 1.0
    X16 204-UVT test on the monthly salary (termination payments out): engine 937813 / expected 937813
    X17 health and pension EE + ER = total rounded once (Decree 780 art. 3.2.1.5 num. 2): engine 218900 / expected 218900; engine 280200 / expected 280200
    X18 gross without deposited severance; net = gross - in kind - EE - tax - voluntary: engine 5300000.0 / expected 5300000.0; engine 4376000.0 / expected 4376000.0
    X19 severance savings and interest paid on termination are in the gross: engine 6120000.0 / expected 6120000.0
    X20 deduction rows carry negative amounts (R6 unpaid leave): engine 4000000.0 / expected 4000000.0
[c] sweep: 298 active WTC rows x 9 bases = 2682 checks; 0 difference(s)
[c] column O (table read): 0 finding(s)
    The sweep tests the mechanism (bases, floors, the Law 1393 excess, routing, signs) against the WTC flags; the matrices are generated from the same columns, so their content is checked by construction.
    Yes/No rows set to false pending a wage-type split (21): R6, R37, R227, R241, R242, R243, R244, R245, R246, R247, R248, R282, R284, R285, R286, R338, R346, R349, R350, R353, R358
```

## The remaining differences, each explained

| Case | Lines | Cause | Who is right |
|---|---|---|---|
| I03, I04 | days 91–180, total, IBC of the incapacity | the independent calculation applies 1/2 of the daily salary on days 91–180 without the minimum-wage floor; C-543 of 2007 (resolutive part) conditions all of Labour Code art. 227: the benefit "no podrá ser inferior al salario mínimo legal vigente" | the design (floor per day) |

**Against the adjusted independent calculation** (same code, with the contribution of each contributor and fund rounded once - Decree 780 art. 3.2.1.5 num. 2, AT2 v30 field 47 - and the contributions withheld out of the withholding base - Tax Code arts. 55, 56): only the six I03 / I04 lines above remain. Against the unadjusted calculation, the further differences come from those two conventions only (employer share, withholding chain; one cent on C23 from its cent-rounded annual consumption).

## Reproduction of v1.2 (same engine, v1.2 IDs / ordinals / formulas)

Monthly cases: 59 cases, 2,153 values, 11 differences — the one-cent C23 consumption (4) and RC01 (7: the sub-30-day projection option did not exist in v1.2). The v1.2 method is therefore reproduced on the monthly chain. On the other modules and checks the v1.2 defects appear: order (47 reads), transport allowance twice in the benefit base (P01, P02, P04, P05, RC08, RC12), the sweep (non-resident base misses column P on 12 rows; service bonus, indemnities and retirement bonus in the monthly read) — see `CHANGELOG.md`.

## Not validated

- Production engine (no Colombia regulation set loaded there yet): the semantics of `ASSUMPTIONS.md` are to be confirmed on acceptance.
- Procedure 2 fixed-percentage computation, history reads, apprentice practical phase, absence-day IBC split (`RESEARCH_GAPS.md`).
