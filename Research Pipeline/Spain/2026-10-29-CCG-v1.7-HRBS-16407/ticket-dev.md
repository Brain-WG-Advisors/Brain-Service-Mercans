**Summary:** Spain: CCG v1.7 — IRPF rate truncation (58118) and health insurance exemption (65630) — from HRBS-16407

Spain is live (STG). CCG v1.7 changes the configuration rules below; please review them against the production setup.

1. IRPF withholding rate (6.1.2, 58118): the final rate has two decimals and is truncated, not rounded (RIRPF arts. 86.1 and 87.3.c; AEAT algorithm, TRUNCAR (TIPO)). In HRBS-16407, 58118 holds 0.395 for 48,879.93 / 123,883.63 = 39.45%; the expected value is 0.3945.
2. Health insurance (65630): the exemption is EUR 500 per year for each covered person (employee, spouse and descendants; EUR 1,500 with a disability), LIRPF art. 42.3.c and RIRPF art. 46. It is applied on the premiums paid in the year (YTD), not as a fixed 41.67 a month, and it is not prorated for starters or leavers (DGT V1967-17). Please confirm the setup multiplies the limit by the number of persons covered.

CCG v1.7: [link no Drive após a importação]
