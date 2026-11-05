# STG Spain, August 2026 parallel run (REF-P205-215) compared with CCG v1.8 and WTC V4.9

Scope: 60 employees, every G2N column. Scripts are in `conf/` (`ss.py`, `irpf.py`, `rate.py`, `q.py`, `c6.py`). IDs only.

## What matches the design (checked on all 60 employees)
- **SS bases:** 58150/58152 = sum of the wage types flagged BCCC/BCCP = Yes, plus 58140 and the IT base 64552/64553. Two employees differ by 0.01–0.02 from rounding. 79413–79416 are excluded, which matches the WTC and LGSS art. 147.2.d. Floors/ceiling in 58151/58153 are applied correctly.
- **SS contributions:** all 10 EE/ER contributions = capped base × 525xx %, with 0 differences above 0.01. Solidarity 2515/2535 on 58535 (3 tiers) also has 0 differences.
- **IRPF steps:** 58590, 58167 (−2,000), 58169 (incl. €600 for 3+ descendants), 58170 (personal minimum + descendants at ½), 58171–58173 on the art. 85 scale, 58115 and 58117 all follow the CCG. The 43 % cap of art. 85.3 does not bind for the 4 employees under €35,200. Art. 81 does not apply.
- **Totals:** gross, total deductions and total ER cost agree.

## Summary

| # | Item | Design | Output | Employees | € Aug | Owner |
|---|---|---|---|---|---|---|
| 1 | Company car missing from the BIK tax base | WTC 65500 Tax = Yes, AEAT Work_InKind_Valuation; CCG 7.3 | 58572 = 65850 + 58105 only, so 65500 is never taxed | 37 | 2,493.76 tax missing | Configuration |
| 2 | Health insurance chain | CCG 7.2 bucket; WTC 65630 Tax = Yes; Art. 42.3.c LIRPF | 65630 is not added to 58572, and 58106 subtracts the **cumulative** exempt amount (176.39) instead of this month's 58.51. Result: negative BIK base and negative 2572 | 58 (+1017112: −59.37) | 2,322.92 | Configuration |
| 3 | Rate applied = 58217 (holds ADP's %), even when lower than calculated | RIRPF 88.5: a voluntary rate can only be **higher** | 2552/58552 = 58217 in 58/60. In 6 cases 58217 < 58118 | 1001476, 1001478, 1001484, 1016187, 1016646, 1016838 | 168.15 under-withheld vs own rate | Configuration (+ data) |
| 4 | 58217 empty for one employee | Same parallel input as the others | Own 30.63 % applied vs ADP 34.85 % | 1001440 | 397.92 | Data input |
| 5 | Payslip prints the calculated rate, not the rate applied | Payslip must show the rate applied | Printed 58118, while the amount uses 58217 | 4/4 payslips in the PDF | presentation | Configuration (payslip) |
| 6 | Net pay ≠ gross − total deductions | Net = gross − deductions | 3,206.34 − 1,049.78 = 2,156.56, but net = 2,087.57 | 1016737 | 68.99 unexplained | Configuration / report |
| 7 | IRNR base reduced by the health item | CCG silent (flat 19/24 %) | 2582 = 24 % × (58552 − 176.39) | 1018096 | 42.33 | Config / our CCG |
| 8 | Annual projection (58163) formula | CCG 6.1.1/6.1.2; RIRPF 83.2 | 58163 = 58149 + (58294+1) × 58008 (exact for 59/59) | all | B | Configuration |
| 9 | 58118 is rounded, not truncated | CCG 6.1.2 TRUNCATE; RIRPF 86.1/87.3.c | Rounded in all 29 cases where the two differ | 29 | 0 (rate not applied) | Configuration |
| 10 | Under-3 increase missing | LIRPF 58.2 + RIRPF 84 → +1,400 per child | 58892 = 1,200 per child | 1001455, 1001469, 1014186, 1016187, 1016646, 1016838 | B | Data (`child_count_under_3`) + our WTC |
| 11 | Cómputo por entero ignored | RIRPF 84.2.º; CCG 7.1.3 | 1,200 used instead of 2,400 | 1001484 | B | Data input |
| 12 | Child-support annuities (9,955) not applied | RIRPF 85.2 | Standard scale used | 1001454 | B | Config / data |
| 13 | Housing −2 points not applied | RIRPF 86.1 (58163 31,914.37 < 33,007.20) | 14.87 % | 1001483 | B | Config / data |
| 14 | Ascendant born 1934 on Modelo 145 | LIRPF 59; CCG 6.1.1 step 4 | Not in 58170 | 1001452 | B | Data (to confirm) |
| 15 | Health YTD load | Bucket needs the real YTD amount | 58101 = 117.88 (2 new hires: 101.04). 7 × 58.51 = 409.57 | 59 | B | Data (YTD) |
| 16 | Extra pay composition | CCG 1.3 (per convenio, check against the prorrata); WTC 64993 = $62100 | 64993 = 62100 + 62182 (60/60), but 62147 = 62100 × 3/12 (base only) | 48 (+12 at 1/12) | to confirm | Config + our WTC |
| 17 | IT month: salary days | CCG 4.3/8.1 (30 − days on leave) | Salary paid for 6 days (62100 = 0.2 × 1,752.78) + 25 IT days | 1001489 | ≈233.84 if 5/30 applies | Question |
| 18–22 | Our artifacts wrong or silent | see (C) | | | | Our artifact |

## (A) Items that change August (fix before sign-off)

**A1. Items 1–2: BIK base (58572).**
- Example 1001440: 65500 528.21 + 65630 58.51 + 65850 100.00; 58106 = 176.39; 58105 = −176.39.
- Output: 58572 = 100 − 176.39 = −76.39, so 2572 = −23.40 (a tax refund on in-kind income).
- Design: health is exempt in August (cumulative ≤ €500), so 58572 = 528.21 + 100 = 628.21 and 2572 = 628.21 × 30.63 % = 192.42.
- Difference: 215.82 for this employee. Total for 57 employees: **4,816.71**.
- Also: 2572 is deducted from the employee, so the employee bears this tax (EE / repercutido).

**A2. Item 3: voluntary rate.**
- Example 1001484: 58118 = 19.71 % but 58217 = 18.37 % is applied.
- 3,543.62 × 1.34 % = 47.48 under-withheld.
- 58217 = `hr.voluntary_irpf_rate`/100 and is loaded with ADP's %. Rule needed: apply MAX(58118, 58217).

**A3. Item 4.** 1001440 is the only employee without 58217. 9,429.51 × (34.85 − 30.63) % = 397.92.

**A4. Item 5: payslips.** The PDF has only 4 employees (16 pages), so the requested sample of 10 could not be done.
- 1018380: prints 21.02 % / 935.00, but 935.00 ÷ 4,166.67 = 22.44 %.
- 1018479: prints 17.69 %, applied 19.76 %.
- 1018681: prints 22.01 %, applied 28.30 %.
- 1019084: prints 21.76 %, applied 30.71 %.

**A5. Item 6.** 1016737 has 68.99 deducted that is not in any G2N column (gross − deductions = 2,156.56; net = 2,087.57).

**A6. Item 7.** 1018096 (58205 = 4, 58218 = 1): 2582 = 1,631.94 = 24 % × 6,799.74, where 6,799.74 = 58552 6,976.13 − 176.39. The health-exemption logic from item 2 reaches the non-resident base.

## (B) Items that only matter for the system's own rate (Sep 2026 / Jan 2027)

In August, 58118 is applied only for 1001440. For everyone else 58217 overrides it.

- **B1. Projection (item 8).** 58117 = 5 × 58008 (1001440: 5 × 9,432.95 = 47,164.75) and 58163 = 58149 + 58117. Compared with the CCG:
  - (a) This month's actual variable pay (58009: 62512, 62875, net BIK) is not in the annual gross, but the rate is applied to it.
  - (b) 62512 Plus Transporte (96.56/month, 59 employees) is never projected: −482.80 per employee.
  - (c) The 65500 car is not projected (CCG 6.1.1 "Benefits in Kind in the Projection").
  - (d) No term for previous-year variable (RIRPF 83.2 regla 1.ª). 62875 was paid to 36 employees (18,565.22) and no field holds the previous-year amount.
  - (e) No term for extras paid separately: the 12 employees with 58238 = 2 / 58140 > 0.
  - (f) 64992 (= 64440 for 60/60) is not used.
  - Example 1001440: the CCG monthly fixed amount is 9,429.51 + 628.21 = 10,057.72, against 9,432.95 used.
- **B2. Rounding (item 9).** 1001442: 24.9057 → output 24.91; truncated is 24.90.
- **B3. Family items, rate if fixed (all else equal):**
  - Under-3 increase (item 10): 1001455 14.40 → 12.40; 1001469 14.24 → 12.21; 1014186 15.27 → 13.01; 1016187 29.26 → 28.46; 1016646 23.92 → 22.83; 1016838 30.71 → 30.01.
  - Cómputo por entero (item 11): 1001484 19.71 → 18.38.
  - Child-support annuities (item 12): 1001454 14.93 → 3.11.
  - Housing (item 13): 1001483 14.87 → 12.87.
  - Ascendant, if valid (item 14): 1001452 18.78 → 15.36.
- **B4. Family situation (58216) differs from Modelo 145:** 1001452 (M145 2 vs 3), 1001464 (1 vs 3), 1016590 (1 vs 3). This only affects the art. 81/85.3 thresholds; all three have 58163 > 35,200, so there is no effect now. 1017112 is not in the M145 file and cannot be verified.
- **B5. Health YTD (item 15).** With 117.88 carried in, the €500 bucket is never reached in 2026. If the premium was 58.51 since January, ~26.59 becomes taxable in September and 58.51/month in October–December.

## (C) Where our CCG/WTC is wrong or silent

- **C1. WTC 58892** adds `child_count_under_3 × 2800` without the ½ factor. This contradicts CCG 7.1.3 (€1,400) and RIRPF 84. The 4th+ child also uses only the child-4 flag.
- **C2. WTC 58890** uses age at period end (58210). LIRPF 61 uses age at 31/12. No STG employee is affected (oldest is 62.98).
- **C3. WTC 64993** formula is "$62100 only". CCG 1.3 says the composition must follow the convenio and must not be hard-coded. STG's convenio is not in our files.
- **C4. WTC 58140 note** calls Tax = No "a likely data error". CCG 1.3 says the prorrata of separately paid extras is excluded from IRPF, so the flag is right and the note is wrong.
- **C5. WTC Projection flags.**
  - Projection = No on 62147/62148/62871 (fixed monthly, "Part of 64440") and on 65500/65630/65850 contradicts CCG 6.1.1.
  - The configuration also ignores these flags (it projects 62147/62871 and not 62512).
- **C6. CCG 6.1.1 work-income reduction.** The pseudo-code applies it after the €2,000, while RIRPF 83.3.d and the CCG's own letter-d row apply it before. No STG effect: the lowest 58163 is 31,914.
- **C7. Names, missing codes and gross-up.**
  - WTC names do not match the configuration: 62875 (WTC "Salary Sacrifice (Negative Earning)", an Auvik placeholder, vs "Incentives"), 62147, 62512, 65850, 58162 (WTC "Variable YTM" vs G2N "Fixed YTM"). WTC 58105 and 58106 have the same name.
  - 21142, 64440 and 68458 are not in the WTC.
  - WTC 6268 gross-up has Tax = No, which contradicts CCG 7.3.2 (an employer-absorbed ingreso a cuenta adds to the IRPF base).
  - 65850 is named "Parking (BIK ER)", but there is no gross-up and the tax is charged to the employee. Confirm with the client.
- **C8. Gaps in our CCG.** The CCG does not cover in-kind exemptions in the IRNR base (item 7). It is also ambiguous on calendar vs commercial salary days in a 31-day month with IT (item 17).

**Confidence:** 95 % on the recomputations (scripts above, all 60 employees). Lower on items 14 and 17 (they depend on facts not in the files) and on item 16 (depends on the convenio).
