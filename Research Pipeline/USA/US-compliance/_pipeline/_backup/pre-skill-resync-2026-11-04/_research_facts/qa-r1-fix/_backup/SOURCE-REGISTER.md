# SOURCE-REGISTER - United States (US-compliance)

Generated 2026-11-02 by the Stage 5 synthesis part A (register merge) from `legal-basis-register.csv` (2533 rows after the merge of the 53 `S5-*` shards). Counts are of rows with `status=active`; domains are grouped onto the 13-domain sweep (the register's own `domain` column is not normalised and keeps the worker's label). ACCESS gaps = distinct URLs in the jurisdiction's findings file; Wayback fallback URLs are folded into the line of the URL they wrap; the full list is in `_research/stage5/ACCESS-GAPS.md`. Open questions = top-level items in the findings file's `## Open questions`; part B carries them into `unresolved[]`.

## Totals

| Status | Rows |
|---|---|
| active | 2113 |
| superseded | 205 |
| MANUAL | 127 |
| partial | 54 |
| gated | 26 |
| historical | 6 |
| provisional | 1 |
| not_applicable | 1 |

| Tier | Rows |
|---|---|
| A.1 | 1031 |
| A.2 | 1164 |
| A.3 | 216 |
| B | 86 |
| C | 29 |
| owner | 7 |

Tier-B rows still `active` or `partial`: 0 - every tier-B row is MANUAL, superseded, historical, gated or not_applicable.

## Per jurisdiction

| JUR | active | MANUAL | gated | partial | superseded | ACCESS gap items | Open questions |
|---|---|---|---|---|---|---|---|
| FED | 84 | 0 | 5 | 3 | 8 | 5 | 8 |
| MULTI | 47 | 1 | 0 | 0 | 1 | 6 | 8 |
| AK | 37 | 1 | 0 | 0 | 6 | 5 | 7 |
| AL | 34 | 1 | 0 | 3 | 1 | 4 | 6 |
| AR | 29 | 6 | 0 | 0 | 1 | 7 | 21 |
| AZ | 52 | 2 | 0 | 0 | 1 | 10 | 9 |
| CA | 31 | 2 | 0 | 1 | 0 | 7 | 11 |
| CO | 30 | 6 | 0 | 2 | 1 | 13 | 8 |
| CT | 51 | 2 | 0 | 0 | 6 | 5 | 9 |
| DC | 40 | 0 | 1 | 0 | 10 | 4 | 9 |
| DE | 32 | 2 | 0 | 0 | 10 | 3 | 8 |
| FL | 40 | 2 | 0 | 0 | 1 | 2 | 6 |
| GA | 27 | 6 | 0 | 6 | 8 | 9 | 9 |
| HI | 47 | 0 | 1 | 2 | 1 | 7 | 9 |
| IA | 43 | 4 | 0 | 0 | 1 | 3 | 9 |
| ID | 36 | 1 | 0 | 1 | 4 | 7 | 10 |
| IL | 40 | 2 | 0 | 1 | 1 | 6 | 10 |
| IN | 29 | 2 | 1 | 3 | 5 | 10 | 13 |
| KS | 41 | 3 | 0 | 0 | 3 | 6 | 7 |
| KY | 45 | 2 | 1 | 0 | 1 | 2 | 11 |
| LA | 30 | 2 | 1 | 2 | 6 | 9 | 23 |
| MA | 48 | 2 | 0 | 0 | 2 | 8 | 18 |
| MD | 33 | 0 | 0 | 0 | 3 | 7 | 11 |
| ME | 43 | 2 | 1 | 0 | 7 | 6 | 13 |
| MI | 47 | 4 | 1 | 1 | 6 | 3 | 8 |
| MN | 38 | 1 | 1 | 1 | 5 | 4 | 10 |
| MO | 40 | 0 | 0 | 1 | 4 | 7 | 8 |
| MS | 31 | 7 | 0 | 1 | 1 | 3 | 6 |
| MT | 39 | 0 | 0 | 1 | 0 | 12 | 8 |
| NC | 38 | 2 | 0 | 4 | 4 | 5 | 9 |
| ND | 33 | 1 | 0 | 0 | 1 | 3 | 6 |
| NE | 30 | 0 | 0 | 2 | 4 | 8 | 7 |
| NH | 36 | 1 | 1 | 0 | 6 | 10 | 8 |
| NJ | 44 | 3 | 0 | 1 | 8 | 10 | 11 |
| NM | 35 | 4 | 1 | 0 | 6 | 10 | 23 |
| NV | 32 | 0 | 0 | 0 | 7 | 9 | 8 |
| NY | 42 | 3 | 0 | 1 | 3 | 6 | 12 |
| OH | 43 | 5 | 2 | 1 | 6 | 7 | 11 |
| OK | 46 | 4 | 0 | 0 | 0 | 5 | 8 |
| OR | 42 | 0 | 0 | 0 | 6 | 4 | 8 |
| PA | 42 | 6 | 0 | 2 | 2 | 7 | 10 |
| RI | 37 | 0 | 1 | 2 | 5 | 7 | 7 |
| SC | 42 | 0 | 0 | 0 | 7 | 5 | 7 |
| SD | 30 | 0 | 0 | 2 | 2 | 2 | 6 |
| TN | 24 | 4 | 0 | 0 | 2 | 9 | 12 |
| TX | 35 | 2 | 0 | 0 | 5 | 5 | 11 |
| UT | 34 | 5 | 1 | 0 | 8 | 15 | 10 |
| VA | 49 | 4 | 0 | 1 | 6 | 6 | 7 |
| VT | 56 | 1 | 0 | 1 | 4 | 7 | 12 |
| WA | 49 | 1 | 0 | 0 | 1 | 5 | 12 |
| WI | 39 | 1 | 0 | 0 | 2 | 7 | 6 |
| WV | 36 | 6 | 1 | 5 | 5 | 5 | 10 |
| WY | 33 | 4 | 1 | 3 | 1 | 4 | 4 |
| OTHER | 22 | 7 | 5 | 0 | 0 | 0 | - |

OTHER = cross-cutting rows outside a jurisdiction prefix (US-OWN-*, US-FIL-*, etc.).

## Active rows by jurisdiction and domain

### FED
labour_code 6; income_tax 12; multistate/nonresident 1; social_security 11; payslip_statute 1; reporting_instruments 15; leave 1; termination 1; benefits_in_kind 2; deductions_garnishments 9; collective_agreements 3; indexation 7; data_protection 1; live_legal_change 2; language 3; special_populations 9

### MULTI
labour_code 2; multistate/nonresident 35; social_security 4; payslip_statute 1; reporting_instruments 2; deductions_garnishments 1; live_legal_change 2

### AK
labour_code 3; income_tax 5; social_security 6; reporting_instruments 6; leave 1; deductions_garnishments 2; collective_agreements 1; data_protection 1; live_legal_change 3; employer_levies 7; language 2
_No active row in:_ multistate/nonresident, payslip_statute, termination, benefits_in_kind, indexation. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### AL
labour_code 2; income_tax 12; multistate/nonresident 1; social_security 3; payslip_statute 1; reporting_instruments 3; leave 1; benefits_in_kind 1; deductions_garnishments 1; live_legal_change 1; employer_levies 5; language 2; special_populations 1
_No active row in:_ termination, collective_agreements, indexation, data_protection. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### AR
labour_code 1; income_tax 7; multistate/nonresident 3; social_security 1; payslip_statute 2; reporting_instruments 1; termination 2; deductions_garnishments 2; live_legal_change 3; employer_levies 4; language 3
_No active row in:_ leave, benefits_in_kind, collective_agreements, indexation, data_protection. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### AZ
labour_code 6; income_tax 9; multistate/nonresident 1; social_security 8; payslip_statute 3; reporting_instruments 5; leave 3; termination 1; benefits_in_kind 1; deductions_garnishments 4; indexation 1; data_protection 2; employer_levies 4; language 4
_No active row in:_ collective_agreements, live_legal_change. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### CA
labour_code 4; income_tax 4; social_security 1; payslip_statute 3; reporting_instruments 2; leave 1; termination 1; benefits_in_kind 3; deductions_garnishments 3; indexation 1; data_protection 1; live_legal_change 1; employer_levies 6
_No active row in:_ multistate/nonresident, collective_agreements. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### CO
labour_code 4; income_tax 8; social_security 3; payslip_statute 1; reporting_instruments 3; termination 1; benefits_in_kind 1; deductions_garnishments 2; employer_levies 3; language 4
_No active row in:_ multistate/nonresident, leave, collective_agreements, indexation, data_protection, live_legal_change. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### CT
labour_code 5; income_tax 4; multistate/nonresident 2; social_security 5; payslip_statute 2; reporting_instruments 8; leave 2; termination 1; deductions_garnishments 3; collective_agreements 1; indexation 2; data_protection 1; live_legal_change 3; employer_levies 6; language 3; special_populations 3
_No active row in:_ benefits_in_kind. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### DC
labour_code 4; income_tax 10; social_security 6; payslip_statute 1; reporting_instruments 8; leave 3; termination 1; deductions_garnishments 1; collective_agreements 2; live_legal_change 1; employer_levies 3
_No active row in:_ multistate/nonresident, benefits_in_kind, indexation, data_protection. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### DE
labour_code 4; income_tax 6; social_security 4; reporting_instruments 5; benefits_in_kind 1; deductions_garnishments 2; collective_agreements 1; data_protection 1; live_legal_change 1; employer_levies 4; language 3
_No active row in:_ multistate/nonresident, payslip_statute, leave, termination, indexation. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### FL
labour_code 7; income_tax 2; social_security 8; payslip_statute 2; reporting_instruments 8; leave 2; termination 1; deductions_garnishments 2; data_protection 1; employer_levies 4; language 3
_No active row in:_ multistate/nonresident, benefits_in_kind, collective_agreements, indexation, live_legal_change. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### GA
labour_code 4; income_tax 5; multistate/nonresident 1; social_security 3; reporting_instruments 5; termination 1; benefits_in_kind 1; deductions_garnishments 1; live_legal_change 1; employer_levies 3; language 2
_No active row in:_ payslip_statute, leave, collective_agreements, indexation, data_protection. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### HI
labour_code 5; income_tax 4; multistate/nonresident 1; social_security 7; payslip_statute 3; reporting_instruments 6; leave 3; termination 1; deductions_garnishments 3; collective_agreements 1; data_protection 1; live_legal_change 1; employer_levies 5; language 4; special_populations 2
_No active row in:_ benefits_in_kind, indexation. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### IA
labour_code 4; income_tax 9; social_security 4; payslip_statute 2; reporting_instruments 7; termination 2; benefits_in_kind 1; deductions_garnishments 3; indexation 2; data_protection 1; live_legal_change 2; employer_levies 3; language 3
_No active row in:_ multistate/nonresident, leave, collective_agreements. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### ID
labour_code 7; income_tax 7; multistate/nonresident 1; social_security 3; payslip_statute 2; reporting_instruments 6; termination 1; benefits_in_kind 1; deductions_garnishments 2; live_legal_change 2; employer_levies 2; language 2
_No active row in:_ leave, collective_agreements, indexation, data_protection. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### IL
labour_code 9; income_tax 6; multistate/nonresident 1; social_security 2; payslip_statute 2; reporting_instruments 8; leave 1; termination 2; deductions_garnishments 3; data_protection 1; employer_levies 4; language 1
_No active row in:_ benefits_in_kind, collective_agreements, indexation, live_legal_change. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### IN
labour_code 5; income_tax 6; social_security 3; payslip_statute 1; reporting_instruments 7; leave 1; termination 1; deductions_garnishments 2; employer_levies 2; language 1
_No active row in:_ multistate/nonresident, benefits_in_kind, collective_agreements, indexation, data_protection, live_legal_change. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### KS
labour_code 6; income_tax 6; multistate/nonresident 1; social_security 5; payslip_statute 2; reporting_instruments 6; termination 2; benefits_in_kind 1; deductions_garnishments 3; data_protection 1; live_legal_change 2; employer_levies 2; language 4
_No active row in:_ leave, collective_agreements, indexation. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### KY
labour_code 9; income_tax 7; social_security 8; payslip_statute 4; reporting_instruments 3; leave 3; termination 1; benefits_in_kind 2; deductions_garnishments 2; employer_levies 5; language 1
_No active row in:_ multistate/nonresident, collective_agreements, indexation, data_protection, live_legal_change. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### LA
labour_code 3; income_tax 5; social_security 2; payslip_statute 2; reporting_instruments 6; leave 1; deductions_garnishments 2; collective_agreements 1; indexation 1; employer_levies 3; language 3; other:local 1
_No active row in:_ multistate/nonresident, termination, benefits_in_kind, data_protection, live_legal_change. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### MA
labour_code 7; income_tax 10; social_security 7; payslip_statute 1; reporting_instruments 6; leave 1; deductions_garnishments 1; collective_agreements 1; data_protection 1; live_legal_change 1; employer_levies 9; language 3
_No active row in:_ multistate/nonresident, termination, benefits_in_kind, indexation. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### MD
labour_code 6; income_tax 6; social_security 5; payslip_statute 1; reporting_instruments 3; leave 1; termination 1; deductions_garnishments 2; collective_agreements 1; employer_levies 4; language 3
_No active row in:_ multistate/nonresident, benefits_in_kind, indexation, data_protection, live_legal_change. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### ME
labour_code 7; income_tax 6; multistate/nonresident 3; social_security 4; payslip_statute 3; reporting_instruments 2; leave 1; termination 2; benefits_in_kind 2; deductions_garnishments 4; collective_agreements 1; indexation 1; data_protection 1; employer_levies 5; language 1
_No active row in:_ live_legal_change. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### MI
labour_code 7; income_tax 9; multistate/nonresident 1; social_security 6; payslip_statute 3; reporting_instruments 8; leave 1; termination 1; deductions_garnishments 3; collective_agreements 1; data_protection 1; live_legal_change 1; employer_levies 3; language 2
_No active row in:_ benefits_in_kind, indexation. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### MN
labour_code 8; income_tax 5; social_security 6; payslip_statute 3; reporting_instruments 4; leave 1; termination 3; deductions_garnishments 3; data_protection 1; live_legal_change 1; employer_levies 2; language 1
_No active row in:_ multistate/nonresident, benefits_in_kind, collective_agreements, indexation. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### MO
labour_code 7; income_tax 7; social_security 4; payslip_statute 4; reporting_instruments 2; leave 1; termination 2; benefits_in_kind 1; deductions_garnishments 2; data_protection 2; live_legal_change 1; employer_levies 5; language 2
_No active row in:_ multistate/nonresident, collective_agreements, indexation. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### MS
labour_code 3; income_tax 8; multistate/nonresident 2; social_security 4; reporting_instruments 7; benefits_in_kind 1; deductions_garnishments 1; data_protection 1; live_legal_change 1; employer_levies 2; language 1
_No active row in:_ payslip_statute, leave, termination, collective_agreements, indexation. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### MT
labour_code 6; income_tax 4; multistate/nonresident 2; social_security 6; payslip_statute 2; reporting_instruments 3; leave 2; termination 1; deductions_garnishments 2; collective_agreements 2; indexation 4; data_protection 1; employer_levies 2; language 2
_No active row in:_ benefits_in_kind, live_legal_change. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### NC
labour_code 6; income_tax 5; multistate/nonresident 1; social_security 3; payslip_statute 5; reporting_instruments 4; leave 1; termination 2; benefits_in_kind 1; deductions_garnishments 4; data_protection 1; live_legal_change 1; employer_levies 2; language 2
_No active row in:_ collective_agreements, indexation. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### ND
labour_code 4; income_tax 7; social_security 7; payslip_statute 1; reporting_instruments 4; termination 1; deductions_garnishments 3; data_protection 1; live_legal_change 2; employer_levies 1; language 2
_No active row in:_ multistate/nonresident, leave, benefits_in_kind, collective_agreements, indexation. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### NE
labour_code 4; income_tax 6; multistate/nonresident 1; social_security 2; payslip_statute 3; reporting_instruments 4; leave 2; termination 2; deductions_garnishments 1; data_protection 1; employer_levies 2; language 2
_No active row in:_ benefits_in_kind, collective_agreements, indexation, live_legal_change. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### NH
labour_code 7; income_tax 2; social_security 6; payslip_statute 4; reporting_instruments 4; leave 1; termination 1; deductions_garnishments 3; data_protection 1; employer_levies 4; language 2; other:ui_agent_authorisation 1
_No active row in:_ multistate/nonresident, benefits_in_kind, collective_agreements, indexation, live_legal_change. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### NJ
labour_code 7; income_tax 8; social_security 7; payslip_statute 3; reporting_instruments 4; leave 1; termination 3; benefits_in_kind 2; deductions_garnishments 2; indexation 1; employer_levies 5; language 1
_No active row in:_ multistate/nonresident, collective_agreements, data_protection, live_legal_change. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### NM
labour_code 6; income_tax 5; multistate/nonresident 1; social_security 6; payslip_statute 3; reporting_instruments 5; leave 2; termination 1; deductions_garnishments 2; collective_agreements 1; employer_levies 2; language 1
_No active row in:_ benefits_in_kind, indexation, data_protection, live_legal_change. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### NV
labour_code 8; income_tax 2; social_security 6; payslip_statute 1; reporting_instruments 5; deductions_garnishments 2; indexation 1; data_protection 1; employer_levies 4; language 2
_No active row in:_ multistate/nonresident, leave, termination, benefits_in_kind, collective_agreements, live_legal_change. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### NY
labour_code 9; income_tax 6; multistate/nonresident 2; social_security 3; payslip_statute 2; reporting_instruments 1; leave 1; termination 2; benefits_in_kind 1; deductions_garnishments 3; data_protection 1; live_legal_change 2; employer_levies 8; language 1
_No active row in:_ collective_agreements, indexation. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### OH
labour_code 6; income_tax 14; multistate/nonresident 2; social_security 2; payslip_statute 2; reporting_instruments 5; leave 1; termination 1; benefits_in_kind 1; deductions_garnishments 2; indexation 1; data_protection 1; employer_levies 3; language 2
_No active row in:_ collective_agreements, live_legal_change. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### OK
labour_code 4; income_tax 9; multistate/nonresident 3; social_security 7; payslip_statute 2; reporting_instruments 5; leave 2; termination 1; deductions_garnishments 3; collective_agreements 1; data_protection 1; live_legal_change 3; employer_levies 3; language 2
_No active row in:_ benefits_in_kind, indexation. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### OR
labour_code 5; income_tax 7; multistate/nonresident 1; social_security 6; payslip_statute 2; reporting_instruments 4; leave 2; termination 1; deductions_garnishments 1; indexation 1; data_protection 1; live_legal_change 2; employer_levies 7; language 2
_No active row in:_ benefits_in_kind, collective_agreements. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### PA
labour_code 6; income_tax 9; social_security 6; payslip_statute 2; reporting_instruments 5; termination 1; benefits_in_kind 2; deductions_garnishments 2; data_protection 2; employer_levies 5; language 2
_No active row in:_ multistate/nonresident, leave, collective_agreements, indexation, live_legal_change. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### RI
labour_code 7; income_tax 3; multistate/nonresident 2; social_security 4; payslip_statute 1; reporting_instruments 6; leave 1; termination 1; deductions_garnishments 2; indexation 2; data_protection 1; live_legal_change 1; employer_levies 4; language 2
_No active row in:_ benefits_in_kind, collective_agreements. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### SC
labour_code 2; income_tax 15; multistate/nonresident 2; social_security 5; payslip_statute 1; reporting_instruments 7; leave 1; deductions_garnishments 2; data_protection 1; employer_levies 3; language 3
_No active row in:_ termination, benefits_in_kind, collective_agreements, indexation, live_legal_change. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### SD
labour_code 6; income_tax 2; social_security 4; payslip_statute 1; reporting_instruments 4; leave 2; termination 1; deductions_garnishments 2; indexation 1; data_protection 1; employer_levies 3; language 3
_No active row in:_ multistate/nonresident, benefits_in_kind, collective_agreements, live_legal_change. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### TN
labour_code 3; income_tax 3; social_security 4; payslip_statute 1; reporting_instruments 4; leave 1; termination 2; deductions_garnishments 2; employer_levies 2; language 2
_No active row in:_ multistate/nonresident, benefits_in_kind, collective_agreements, indexation, data_protection, live_legal_change. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### TX
labour_code 4; income_tax 2; social_security 8; payslip_statute 2; reporting_instruments 5; leave 2; termination 1; deductions_garnishments 3; collective_agreements 1; data_protection 1; employer_levies 4; language 2
_No active row in:_ multistate/nonresident, benefits_in_kind, indexation, live_legal_change. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### UT
labour_code 5; income_tax 8; multistate/nonresident 1; social_security 4; payslip_statute 1; reporting_instruments 6; termination 1; deductions_garnishments 2; indexation 1; employer_levies 4; language 1
_No active row in:_ leave, benefits_in_kind, collective_agreements, data_protection, live_legal_change. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### VA
labour_code 7; income_tax 9; social_security 11; payslip_statute 2; reporting_instruments 4; leave 2; benefits_in_kind 1; deductions_garnishments 2; collective_agreements 1; data_protection 1; live_legal_change 2; employer_levies 4; language 2; other:calculator 1
_No active row in:_ multistate/nonresident, termination, indexation. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### VT
labour_code 7; income_tax 14; social_security 8; payslip_statute 5; reporting_instruments 4; leave 6; termination 1; benefits_in_kind 1; deductions_garnishments 3; data_protection 1; employer_levies 3; language 3
_No active row in:_ multistate/nonresident, collective_agreements, indexation, live_legal_change. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### WA
labour_code 4; income_tax 3; social_security 12; payslip_statute 3; reporting_instruments 3; leave 2; termination 2; benefits_in_kind 2; deductions_garnishments 3; collective_agreements 1; indexation 1; data_protection 1; live_legal_change 2; employer_levies 6; language 4
_No active row in:_ multistate/nonresident. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### WI
labour_code 6; income_tax 4; social_security 6; payslip_statute 2; reporting_instruments 6; leave 1; deductions_garnishments 3; data_protection 1; live_legal_change 3; employer_levies 2; language 3; special_populations 2
_No active row in:_ multistate/nonresident, termination, benefits_in_kind, collective_agreements, indexation. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### WV
labour_code 4; income_tax 12; social_security 5; payslip_statute 3; reporting_instruments 4; termination 1; deductions_garnishments 1; live_legal_change 2; employer_levies 2; language 2
_No active row in:_ multistate/nonresident, leave, benefits_in_kind, collective_agreements, indexation, data_protection. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### WY
labour_code 6; income_tax 1; social_security 10; payslip_statute 1; reporting_instruments 4; leave 2; deductions_garnishments 2; data_protection 1; live_legal_change 1; employer_levies 3; language 2
_No active row in:_ multistate/nonresident, termination, benefits_in_kind, collective_agreements, indexation. (May be covered by FED/MULTI rows or by a row under another domain label; part B checks per domain.)

### OTHER
reporting_instruments 15; governance 7

