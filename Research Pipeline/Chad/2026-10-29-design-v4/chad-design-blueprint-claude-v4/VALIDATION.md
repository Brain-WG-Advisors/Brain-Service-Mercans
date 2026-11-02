# Chad v4 — validation

Results come from executing the regulations as written (`_build_v4.py`, next to this folder: it generates SKILL.md from the same data it executes).

## Scenarios — v4 against v3

| Scenario | EE CNPS | IRPP | TFE | TAFP | Net | Same as v3 |
|---|---|---|---|---|---|---|
| 1 Active baseline 350,000 | 12,250 | 28,464 | 26,250 | 4,200 | 309,286 | ✅ |
| 9 Zero salary | 0 | 0 | 0 | 0 | 0 | ✅ |
| 10 13th month | 17,500 | 75,750 | 52,500 | 8,400 | 606,750 | ✅ |
| Housing real 50,000 under a 120,000 cap | 17,500 | 65,750 | 48,750 | 7,800 | 516,750 | ✅ |
| Individual severance 900,000 | 10,500 | 208,600 | 22,500 | 3,600 | 980,900 | ✅ |
| Supplementary pension 30,000 (cap 14,000) | 14,000 | 32,060 | 30,000 | 4,800 | 323,940 | ✅ |
| Transport 120,000, granted to all | 11,550 | 26,437 | 31,500 | 5,040 | 382,013 | ✅ |
| Family allowance 30,000 | 10,500 | 23,397 | 24,750 | 3,960 | 296,103 | ✅ |
| Entity with 50% relief | 12,250 | 28,464 | 13,125 | 2,100 | 309,286 | ✅ |
| Young graduate, month 30 | 12,250 | 0 | 26,250 | 4,200 | 337,750 | ✅ |

Non-resident 800,000 (CCG Scenario B, CNPS branches off): IRPP 144,000 on 58592 = 800,000; no TFE / TAFP.

Reporting values: 58106 = 60,000 when there is cash gross, 0 otherwise; 58131 = 20.

## Not re-run in v4
The v3 cases for mid-month hire and exit, backdated hire, retro increase, future-dated termination, post-termination payment, unpaid leave and plan-social final pay depend on proration and retro behaviour of the engine; v4 does not change their logic, so they are not repeated here. The `retro_` effect itself can only be seen in the engine.

## Pre-flight
`preflight_check.py`: 32 regulations checked, no engine-rule violations.

## What is not validated
The design has not been loaded into an engine. Ceiling accounts (A10), `retro_` (A11) and `_$$` (A12) are written as the 16 Oct answers describe them; their behaviour must be confirmed in the acceptance environment.
