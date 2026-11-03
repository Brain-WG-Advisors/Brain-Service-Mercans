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

## QA round 1 research pass (2026-11-02, compliance-source-hunter agent 2)

Routed by `_qa/CCG-review-r1.json`; log `_research/qa-r1-fix/AGENT2-R1.md`. Federal scope only; State 2026 blockers are with the parallel browser worker P3 (shard `_register-shards/S5B-P3.csv`).

**1 - Employment / labour code (holidays).** What governs it: 5 U.S.C. 6103 [A.1, US-FEDQ1-009]; OPM 2026/2027 holiday schedules [A.2, US-FEDQ1-010]; for federal tax due dates, the District of Columbia legal holidays listed in Pub. 15 (2026) sec. 11 [A.2, US-FEDQ1-011]. What was obtained: all three texts (local files under `ccg-sources/FED/`); the 22 dates of 2026-2027 re-derived from the statute and matching both authorities. What could not be: State legal holidays (51 jurisdictions, not in this pass). What would close it: each State holiday statute and revenue-department due-date rule (fan-out).

**2 - Income tax / 2b - Non-resident (equity and fringe benefits).** What governs it: Pub. 15-B (2026) Employee Stock Options and 83(i) [A.2, US-FEDQ1-001], sec. 4 and group-term life [A.2, US-FEDQ1-008]; Pub. 15 (2026) sec. 5/7 [A.2, US-FEDQ1-002]; Pub. 15-T (2026) Introduction and Table 3 [A.2, US-FEDQ1-007]; Pub. 515 (2026) [A.2, US-FEDQ1-006]; Pub. 525 (TY2025) [A.3, US-FEDQ1-003, mechanics]. What was obtained: the full treatment for NSO, ISO/ESPP, restricted stock, RSU and 83(i), for residents and NRAs; the NRA fringe-benefit rule. What could not be: the grant-to-vest sourcing period of 26 CFR 1.861-4(b)(2)(ii)(F) (eCFR API returned paragraph (a) only); the IRS equity audit-techniques guide URL is 404. What would close it: 1.861-4 full text from ecfr.gov (browser) or the govinfo CFR annual edition.

**3 - Social security (equity timing).** 26 CFR 31.3121(v)(2)-1 [A.1, US-FEDQ1-004] and 31.3306(r)(2)-1 [A.1, US-FEDQ1-005] via the eCFR API. No gap.

**11 - Indexation.** The C-CPI-U caliber now rests on the govinfo text of 26 U.S.C. 1(f)(3) [A.1, US-FEDQ1-012], superseding the LII copy US-FED-026. No gap.

**Multistate.** 4 U.S.C. 114 govinfo text [A.1, US-MULTIQ1-001] supersedes the LII copy US-FEDP51-009.

**Register hygiene.** US-CAEDD-004 superseded by US-CAP7-002 (one active CA SDI 2026 row; MANDATE still cites US-CAEDD-004 - scaffolder to re-point). Superseded rows with a generic `article_or_section`, or whose citation is still carried by an active row (source-copy supersessions), now carry the source identity in that column, so C70 no longer reports them as repealed law (5,575 -> 0 hits). `effective_from` is still empty on 485 active rows consumed by CCG facts: listed with candidates in `_research/qa-r1-fix/EFFECTIVE-FROM-UNFILLED.csv` (statutes 262; one lookup per instrument, 53 independent jurisdictions).

## QA r1b (2026-11-02, agent 2): register changes

**What was added.** Shard `_register-shards/S5B-P3.csv` (browser pass P3, 22 rows, ids US-{JUR}B5-301..308; no old ids needed translating via `_research/stage5/ID-RENAME-MAP.csv`) merged: CA DIR health-care and fast-food minimums and six local minimums [US-CAB5-301..308]; CO FAMLI 2027 bulletin and Boulder City/County [US-COB5-301..303]; DE W-4 FAQ [US-DEB5-301]; DC Law 26-189 [US-DCB5-301]; NYC and Yonkers supplemental rates [US-NYB5-301/302]; TX proposed 40 TAC 815.107 [US-TXB5-301]; Cook County paid leave [US-ILB5-301]; WV SB 392 [US-WVB5-301]; MI city list [US-MIB5-301]; MA 830 CMR 62B.2.1 and Directive 07-2 [US-MAB5-301/302]; Santa Fe County living wage [US-NMB5-301]. New row US-CTQ1B-001: the CT 2026 per-period withholding tables (IP 2026(1) pp. 31-38), decoded from vector glyphs, Examples 8-10 reproduced.
**Supersessions.** US-NYB5-301/302 supersede US-NY-011 (already superseded). US-COB5-302/303 supersede US-COS5-011 for the Boulder localities only (US-COS5-011 stays MANUAL for Edgewater 2026 and Denver 2027). US-DEB5-301 supersedes US-DES5-008 for the certificate claim only: "federal W-4 accepted" was wrong (a 2020+ federal W-4 may not be accepted; Delaware W-4 required); US-DES5-008 and US-DES5-006 carry a correction note and stay active for their other claims.
**effective_from.** 162 rows filled from the instrument (high/medium proposals in `_research/qa-r1-fix/effective-from-*.csv`); 323 low/undated rows left empty with the note "effective_from not stated in the instrument; in force as at retrieved_on (QA r1 note)". Log: `_research/qa-r1-fix/r1b_register.log`.
**Hygiene.** 72 local_file paths gained the `00-official-sources/` prefix; US-CTS5-027 points to the ch. 557 file for Sec. 31-13a (and ch. 558 for 31-66); US-ALR3-001 is the 2020 edition per its cover.
**What could not be.** San Jose, Edgewater and Denver 2027 minimums, Chicago paid leave, and the 19 state items P3 left open (geo/WAF blocks: maine.gov, revenue.louisiana.gov, tax.idaho.gov, rilegislature.gov, vec.virginia.gov, chicago.gov) - see `_research/gaps.json`.
**What would close it.** The same lookups from a US network exit; they are independent and can run in parallel, one per jurisdiction.

## QA r3 (2026-11-02, agent 2): register changes
**What governs it (new rows).** US-FEDQ3-001 26 U.S.C. 3401(a) [A.1, new local copy `ccg-sources/FED/FED_USC-26-3401_govinfo-2024_2026-11-02.htm`, govinfo HTTP 200]; US-FEDQ3-002 26 U.S.C. 3121(a) and (v)(1) [A.1]; US-FEDQ3-003 26 U.S.C. 3306(b) and (r)(1) [A.1] (both on the local govinfo copies already behind US-FEDR2-001/-002); US-FEDQ3-004 Pub. 15 (2026) sec. 9 W-4 default and sec. 4 SSN [A.2].
**What was obtained.** Federal gross-to-net inclusion/exclusion rules (Pub. 15 sec. 15 table pp.46-52, Pub. 15-B Table 2-1 p.6 and sections 1-4), CA DE 44 married/HoH Method B annual rates (US-CAS5-001), AL standard-deduction phase-out (US-ALS5-001). Quotes or derivation lines added to verification_method of US-SCP51-002, US-OHS5-007, US-COB5-003, US-COB5-301, US-MAS5-012, US-DEP52-001, US-NCS5-003, US-PAS5-001, US-NDS5-017, US-SDS5-017, US-WAS5-017, US-MSS5-003, US-OHB5-002, US-WVS5-015. consumed_by filled for US-FEDR2-001..004 and US-FEDQ1-001/002/004/006/007/008 (WTC/global_baseline, DD/8_sheets, CCG units).
**What could not be.** US-NH-001 re-verification: revenue.nh.gov 403, Wayback 429, gc.nh.gov 403, so verified_on stays empty. Trump account FICA/FUTA treatment is not published (RQ-591). AR e-file threshold 250 is not in any local file (RQ-590).
**What would close it.** One US-exit or browser read of the NHDRA I&D repeal notice; IRS Trump account guidance; Ark. Code Ann. 11-10-215 or the DWS reporting page.

## S5B-P4 merge (2026-11-02, agent 2): 41 register rows

Shard `_register-shards/S5B-P4.csv` (browser pass P4) merged into `legal-basis-register.csv` on 2026-11-02 (log `_research/qa-r3b-fix/AGENT2-F44.md`, `apply-f44-p4-log.json`). Each new row supersedes exactly one earlier row; the earlier row carries `effective_to` 2026-11-02 and `status=superseded`, and its `consumed_by` was carried into the successor. All 41 successor rows are `active`, read in a browser and held as local files. Register status totals after the merge and the non-active citation clean-up of the same day: active 2206; superseded 250; MANUAL 114; partial 53; gated 25; historical 6; provisional 2; not_applicable 1 (2657 rows).

| new id | supersedes | domain | tier | instrument | figure or rule carried | local file |
|---|---|---|---|---|---|---|
| US-AKB5-401 | US-AKP51-005 | prevailing_wage | A.1 | AS 36.05.005 and 36.05.010 prevailing wage on public construction | Chapter applies to a public construction contract exceeding 25,000 USD; contractor pays not less than the prevailing rate in the latest D... | AK_AS-36.05.005-010_akleg_2026-11-02.txt |
| US-AKB5-402 | US-AKP7-001 | employer_payroll_levies | A.2 | State Training and Employment Program (STEP) employee contribution | 0.10% of wages, credited back in full against employee UI (net nil); inside the 0.50% employee UI rate; payer=employee; base=54,200 USD; ... | AK_AS-23.15.620-640_akleg_2026-11-02.txt |
| US-AKB5-403 | US-AKP7-002 | employer_payroll_levies | A.2 | Technical and Vocational Education Program (TVEP) employee contribution | 0.25% of wages, credited back in full against UI (net nil); payer=employee; base=54,200 USD; scope=statewide; GAP: Statute text not read ... | AK_AS-23.15.835_akleg_2026-11-02.txt |
| US-AZB5-401 | US-AZR3-001 | sui | A.2 | DES Payment Taxes - Overview (Arizona UI employer) | "State unemployment taxes pay for unemployment benefits only. You cannot take these taxes out of employee pay."; taxable wages are the fi... | AZ_DES_payment-taxes-overview_browser_2026-11-02.txt |
| US-AZB5-402 | US-AZR3-004 | payroll_levies | A.2 | DES Unemployment Insurance Operating Fund (UIOF) | Employer-side fund effective 2027-01-01 (NOT 2026): each quarter of calendar 2027 an experience-rated employer pays 3.15% of its UI tax l... | AZ_DES_UIOF_browser_2026-11-02.txt |
| US-COB5-401 | US-COFAMLI-001 | payroll_levies | A.2 | Colorado FAMLI 2026 premiums | Premium 0.88% of wages: 0.44% employer + 0.44% employee; paid on wages up to the Social Security wage cap; statutory cap 1.2%; Director r... | CO_FAMLI_employers_2026-11-02.txt |
| US-COB5-402 | US-COP52-002 | prevailing_wage | A.2 | Colorado OSA Public Projects Defined / Prevailing Wage on Public Projects | State prevailing wage exists: contractors on public projects of 500,000 or more pay employees weekly and comply with 24-92-209 enforcemen... | CO_OSA_public-projects-defined_2026-11-02.txt |
| US-COB5-403 | US-COP7-004 | employer_payroll_levies | A.2 | Denver Occupational Privilege Tax - employee share | 5.75 USD/month when earnings >= 500 USD/month; payer=employee; base=flat monthly; scope=City and County of Denver; GAP: 2026 edition not ... | CO_Denver_TaxGuideTopic61_OPT_wayback-20250731_transcription_2026-1... |
| US-COB5-404 | US-COP7-005 | employer_payroll_levies | A.2 | Denver Occupational Privilege Tax - employer share | 4.00 USD/month per taxable employee; payer=employer; base=flat monthly; scope=City and County of Denver; GAP: 2026 edition not read | CO_Denver_TaxGuideTopic61_OPT_wayback-20250731_transcription_2026-1... |
| US-CTB5-401 | US-CTQ1B-001 | income_tax | A.2 | DRS IP 2026(1) Connecticut Employer's Tax Guide (Circular CT): State of Connecticut 202... | Per-period withholding amounts by wage band and withholding code A/B/C/D/F: 139 bands per period (weekly to 1,932; bi-weekly to 3,865; se... | CT_IP-2026-1_withholding-tables-max-wages_transcription_2026-11-02.txt |
| US-DCB5-401 | US-DCP7-001 | employer_payroll_levies | A.2 | DC UI administrative funding assessment | 0.2% of all wages (also reimbursing employers); employees do not contribute; payer=employer; base=all wages; scope=District of Columbia | DC_Code-51-103_dccouncil_2026-11-02.txt |
| US-DEB5-401 | US-DEP7-001 | employer_payroll_levies | A.2 | Operations and Technology Assessment | 0.2% of taxable wages through 2026; 0.175% from 2027; payer=employer; base=14,500 USD; scope=statewide | DE_Code-T19-c33-sc03_delcode_2026-11-02.txt |
| US-FEDB5-401 | US-FED-022 | social_security | A.2 | SSA Contribution and Benefit Base page | OASDI taxable maximum 2026 = 184,500; 2027 = 192,300 (6.2% each = 11,922.60 max for 2027); HI 1.45% each, no limit; table 1937-2027 | FED_SSA_cbb_browser_2026-11-02.txt |
| US-IDB5-401 | US-IDP52-002 | multistate | A.2 | Idaho State Tax Commission - Income you don't have to withhold on | Complete list of no-withholding cases: nonresident earning under 1,000 USD in Idaho in the calendar year; agricultural laborer under 1,00... | ID_STC_income-dont-withhold-on_wayback-20260412_2026-11-02.txt |
| US-IDB5-402 | US-IDP7-001 | employer_payroll_levies | A.2 | Workforce Development rate (inside UI tax) | 0.03% standard (positive classes 0.00624%-0.02082%); administrative rate 0.000%; payer=employer; base=58,300 USD; scope=statewide | ID_DOL_Tax-rate-Class-array-2026_wayback-20260712_transcription_202... |
| US-KYB5-401 | US-KYP7-001 | employer_payroll_levies | A.2 | Service Capacity Upgrade Fund (SCUF) diversion | Suspended all of 2026 (0.00%); 0.0115% diverted from rate from 2027-01-01; payer=employer; base=12,000 USD; scope=statewide; GAP: Not a 2... | KY_UI_SCUF-information_2026-11-02.txt |
| US-MAB5-401 | US-MAP7-001 | employer_payroll_levies | A.2 | Workforce Training Fund contribution | 0.056% (commissioner may adjust to ~22M USD/year); payer=employer; base=15,000 USD; scope=statewide; GAP: 2026 adjustment not confirmed | MA_GL-151A-14L_wayback-20260519_2026-11-02.txt |
| US-MAB5-402 | US-MAR3-002 | local_tax | A.2 | Mass.gov DOR Tax Rates (updated 2025-12-30): list of Massachusetts taxes and local options | ABSENCE (Medium-High): the page lists every tax by type and rate (income incl. wage withholding 5.00% with 4% surtax above 1,107,750 for ... | MA_DOR_tax-rates_browser_2026-11-02.txt |
| US-MDB5-401 | US-MDP51-002 | sui | A.2 | Maryland DOL Tax Rates and Quarterly Reporting - 2026 | Tax Table A for 2026; contributory rates 0.30% to 7.50% (standard 7.50%); taxable wages = first 8,500 per employee per calendar year; new... | MD_DOL_UI-tax-rate_2026-11-02.txt |
| US-MDB5-402 | US-MDSUI-001 | social_security | A.2 | Maryland DOL Tax Rates and Quarterly Reporting (UI) | Taxable wage base 8,500; contributory rates 0.30-7.50 pct; new employers 1.0-2.6 pct; Table A in effect 2026; wage report and payment wit... | MD_DOL_UI-tax-rate_2026-11-02.txt |
| US-MIB5-401 | US-MIR3-001 | local_income_tax | A.2 | Michigan Treasury FAQ: Which cities impose an income tax? (re-read) | Exist: yes, 24 cities levy municipal taxes related to income (individual, business incl. withholding, fiduciary). Collector: Treasury adm... | MI_Treasury_cities-income-tax_wayback-20261009_2026-11-02.txt |
| US-MNB5-401 | US-MNP7-001 | employer_payroll_levies | A.2 | Workforce Development fee | 0.10% of taxable wages; reimbursing employers exempt; payer=employer; base=44,000 USD; scope=statewide | MN_Stat-116L.20_revisor_2026-11-02.txt |
| US-MNB5-402 | US-MNP7-002 | employer_payroll_levies | A.2 | UI Additional Assessment (14%) and Special Assessment (0%) | Additional assessment 14.00% of UI tax; special assessment 0.00%; payer=employer; base=44,000 USD; scope=statewide | MN_UIMN_tax-rates_wayback-20261012_2026-11-02.txt |
| US-MOB5-401 | US-MOP52-001 | prevailing_wage | A.1 | RSMo 290.230 Prevailing wage rates required on public works | State prevailing wage law exists (RSMo 290.210-290.340): prevailing hourly rate for public works; 2x on Sunday/holiday; 1.5x overtime (>1... | MO_RSMo-290.230_wayback-20260225_2026-11-02.txt |
| US-MOB5-402 | US-MOP52-003 | payslip_statute | A.1 | RSMo 290.520 Employer records (minimum wage law) | Employer keeps 3 years: name, address, occupation, rate of pay, amount paid each pay period, hours worked per day and week; no itemized p... | MO_RSMo-290.520_wayback-20260613_2026-11-02.txt |
| US-MOB5-403 | US-MOP52-005 | sui | A.2 | Missouri DES Tax Rates page (new employer rates, taxable wage base) | 2026 taxable wage limitation 9,000 (2025 9,500); new employer rate 2026 = 2.376% (all others, mining, construction), 1.00% 501(c)(3); exp... | MO_DES_tax-rates_wayback-20260531_2026-11-02.txt |
| US-MTB5-401 | US-MTP7-001 | employer_payroll_levies | A.2 | Administrative Fund Tax | 0.18% (0.13% for eligible classes 1-2); payer=employer; base=47,300 USD; scope=statewide | MT_UID_Rate-Explanation_wayback-20260813_2026-11-02.pdf |
| US-MULTIB5-401 | US-MULTI-017 | multistate | A.2 | Arizona DOR: Withholding Tax (employer page) | AZ Form WEC exemption: residents of CA, IN, OR, VA who can claim AZ credit; nonresident withholding starts after 60 days present (transit... | AZ_DOR_withholding-tax_wayback-20261009_2026-11-02.txt |
| US-NCB5-401 | US-NC-002 | sui | A.2 | NC DES tax rate information (UI, employer-paid) | UI employer-paid; new-employer standard beginning rate 1.000%; taxable wage base 2026 $34,200 (2025 $32,600) - rate table page read; empl... | NC_DES_tax-rate-information_2026-11-02.txt |
| US-NYB5-401 | US-NY-010 | sdi_pfml | A.1 | NY Workers Compensation Law 209 (NYSenate): DBL employee contribution | DBL employee contribution one-half of one percent of wages, not in excess of sixty cents per week | NY_WCL-209_nysenate_browser_2026-11-02.txt |
| US-NYB5-402 | US-NY-005 | sdi_pfml | A.2 | NY DFS PFL 2026 rate decision; WCB Disability Benefits Law | PFL (DFS decision 2025-08-29, read): 2026 rate 0.432% of wages per pay period, annual max employee contribution $411.91. DBL (WCL 209(3)(... | NY_DFS_PFL-rate-decision-2026_browser_2026-11-02.txt |
| US-OHB5-401 | US-OH-009 | income_tax | A.2 | Ohio tax.ohio.gov employer withholding page - Required Returns and School District Retu... | Ohio IT 4 certificate (updated by employee when info is wrong); IT 501 return for Ohio income tax withheld (not required if no liability ... | OH_Tax_employer-withholding_2026-11-02.txt |
| US-OHB5-402 | US-OHP7-001 | employer_payroll_levies | A.2 | Municipal income tax withheld by employer | Per municipality; 1% cap without voter approval (grandfathered exceptions); payer=employee; base=qualifying wages; scope=Ohio taxing muni... | OH_ORC-718.04_wayback-20260514_2026-11-02.txt |
| US-ORB5-401 | US-ORP51-004 | prevailing_wage | A.2 | BOLI Prevailing Wage page | Prevailing wage rates apply to construction workers on covered public works projects (projects under 50,000 or without public-agency fund... | OR_BOLI_prevailing-wage_2026-11-02.txt |
| US-PAB5-401 | US-PAP7-005 | employer_payroll_levies | A.2 | Pittsburgh Payroll Expense Tax | 0.55% (5.5 mills) of payroll for work in Pittsburgh; not deductible from wages; payer=employer; base=total payroll; scope=City of Pittsbu... | PA_Pittsburgh_payroll-expense-tax-FAQs_2026-11-02.pdf |
| US-PAB5-402 | US-PAB5-001 | labour_code | A.1 | Pittsburgh City Code Chapter 626, Paid Sick Days Act (as amended by Ord. No. 11-2025, e... | Covers employers with 1+ employees in the City (not US/PA government). Accrual 1 hour per 30 hours worked in Pittsburgh for all employers... | PA_Pittsburgh_PSDA-626-03_transcription_2026-11-02.txt |
| US-RIB5-401 | US-RIP7-001 | employer_payroll_levies | A.2 | Job Development Assessment (JDA) | 0.21% (Schedule F rates less 0.21; new employer 1.21% incl. JDA); payer=employer; base=30,800 USD (32,300 highest); wage bases unverified... | RI_DLT_2026-UI-TDI-tax-rates-press-release_browser_2026-11-02.txt |
| US-TNB5-401 | US-TNR3-003 | other_levy | A.2 | TN DLWD UI Tax pages (liability page + UI Tax Rates) - employer taxes administered | DLWD UI-tax section shows only the UI premium: taxable wage base 7,000 for 2026, six premium rate tables (table 6 in effect 2026-01-01 an... | TN_DLWD_unemployment-insurance-tax_2026-11-02.txt |
| US-VAB5-401 | US-VASUI-001 | social_security | A.1 | Code of Virginia 60.2-229 Wages (UI taxable wage limit) | UI taxable wages: remuneration up to USD 8,000 per employee per calendar year (statute text; agency VEC pages returned 403) | VA_Code-60.2-229_lis_2026-11-02.txt |
| US-VAB5-402 | US-VAR3-003 | sui | A.1 | Code of Virginia 60.2-532 Pool cost charges and 60.2-533(C) Fund building rate (re-read... | 60.2-533(C): fund building rate 0.2 percent added to all rates unless the fund balance factor exceeds 50 percent. 60.2-532: pool cost cha... | VA_Code-60.2-533_lis_2026-11-02.txt |
| US-WYB5-401 | US-WYP52-001 | sui | A.2 | Wyoming DWS Unemployment Tax Rates page (full read in Chrome) | Rates assigned per W.S. 27-3 Art. 5. New employers (under three years experience) get a base rate by their industry plus four additional ... | WY_DWS_unemployment-tax-rates_2026-11-02.txt |

**What could not be.** `tn.sui.employee.rate` stays partial (absence fact; T.C.A. 50-7-403 text not held). Denver OPT rests on the 2025-07 Tax Guide edition; the Pittsburgh payroll-expense FAQ is undated; the MA WTF 0.056 statutory rate has no confirmed 2026 adjustment.
**What would close it.** T.C.A. 50-7-403 from the TN official code; the current Denver Tax Guide; a dated Pittsburgh FAQ; the MA DUA 2026 WTF notice.

## QA r3c additions (2026-11-02, agent 2)
**What governs it.** Zero employee UI contribution, now on primary clauses: NY Labor Law 570(6) [A.1, US-NYR3C-001]; RCW 50.24.010 [A.1, US-WAR3C-001]; W. Va. Code 21A-5-14 [A.1, US-WVR3C-001]; ORC 4141.23(A) [A.1, US-OHR3C-001]; 820 ILCS 405/1400 [A.1, US-ILR3C-001]; Neb. Rev. Stat. 48-648(1) [A.1, US-NER3C-001]; 19 Del. C. 3346 [A.1, US-DER3C-001]; K.S.A. 44-710(a) [A.1, US-KSR3C-001]; Utah Code 35A-4-302(1)(b) [A.1, US-UTR3C-001]; TN DLWD Handbook for Employers, Premiums and Taxes ("financed solely by employer premiums") [A.3, US-TNR3C-001]. NJ and PA keep their employee shares (not generalised).
**What was obtained.** Local copies with md5 for the ten clauses (several via Wayback id_ snapshots because the live legislature hosts time out or block scripts); local copies for 11 rows that had none (US-FED-019/023/024/025, US-CAP7-001/002/003, US-CAEDD-001, US-GA-001, US-NY-001, US-DCP52-001). The EDD Rates and Withholding page now publishes the 2027 SDI rate 1.4% (new fact object ca.sdi.employee.rate from 2027-01-01).
**What could not be.** T.C.A. 50-7-403 text (LexisNexis-only host); ORC 4141.23 version effective 2026-06-16 (the held copy is the 2025-09-30 version).
**What would close it.** T.C.A. 50-7-403 saved from the LexisNexis public-access Tennessee Code; the 2026-06-16 version of ORC 4141.23 from codes.ohio.gov.

## RSPEC pre-build close (2026-11-03, agent 2)
**What was obtained.**
- NCDOR TY2026 W-2 and NC-3 file specs (rev. 09-01-2026) [A.2, US-NCS6-001/-002]; they supersede US-NCS5-027.
- 40 TAC 815.107 and 815.109 (LII copy) [A.1, US-TXS6-001/-002].
- 40 O.S. 3-102/3-301 excerpts [A.1, US-OKS6-001]: 3-111 is repealed.
- VT EFW-2 spec page [A.2, US-VTS6-001].
- KY OUI guide, KUIP upload formats [A.2, US-KYS6-001].
- US-FIL-002 widened to EFW2C Pub. 42-014.
- US-MNS5-015 widened with the 268.044 due date.

**What could not be.** 18 RSPEC items remain documented limitations: 11 access from a non-US exit, 5 behind an employer portal login, 2 not yet published. List in `_research/gaps.json` → `RSPEC`.

**What would close it.** A US-exit pass over CO, ID, IL, IN, KY, LA, ME, MN, MT, OK and WA L&I (parallel per state); the operations team or a TPA login for DE, IA, NM, OH and UT; the GA TY2026 Federal Format and the adopted TX 815.107 amendment.
