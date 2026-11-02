---
name: "chad-design-blueprint-claude-v6"
description: "Chad (TD) payroll regulation design v6 — the v5 rules (CGI 2026, CNPS decrees and guide, two QA rounds) in the form of the development team's td_2026 design: same regulation IDs, names, ordinals, rule groups, accounts and formula conventions wherever the law allows; each remaining difference is marked Deliberate divergence (law). Design Blueprint format, tax year td_2026."
---

> **Analysis instructions:** read and follow `Regulation_Design_Analysis_Engine.md` before interpreting or computing any regulation below.

> **Companions:** `CHANGELOG.md` — v5 → v6 changes of form, regulation by regulation (and the v4 → v5 history) · `ASSUMPTIONS.md` — decisions taken, alternatives and what is still not settled · `RESEARCH_GAPS.md` — what compliance must fix · `VALIDATION.md` — the scenarios executed: v6 = v5, value by value.

> **Source of every article cited:** Code Général des Impôts du Tchad 2026, DGI edition (`raw/docs/oficiais/TD/2026-11-01-CGI-TCHAD-2026-FINAL-dgi.pdf`, md5 139d5326…); LF 2024–2026 where the CGI says so; CNPS: Dec. 1635 and 1636/PR/PM/MFPT/2009 and the CNPS Guide de l’employeur 2019 (`raw/docs/oficiais/TD/2026-11-01-*`).

# 0 - Flags

| Account | Flag | Formula | Values |
| --- | --- | --- | --- |
| 58218 | Status (global flag) | `$hr.employee_type` | As the Dev (`$hr.employee_type`): 0 resident · 1 non-resident · 2 disabled (CGI Art. 45-18°) · 3 young graduate (Art. 3-4°) · 4 diplomatic (Art. 3-2°); routing uses `LESS($58218;1)` for residents, never an equality test against zero |
| 58202 | CNPS PVID eligible | `IF(EQUALS($hr.cnps_eligibility_pvid::key;'N');2;1)` | 1 yes (default, every employee, **non-residents included**: « quelle que soit… leur nationalité », CNPS guide p. 6) · 2 no — only a seconded employee covered by a bilateral or multilateral convention (CIPRES) with a secondment certificate |
| 58203 | CNPS PFM eligible | `IF(EQUALS($hr.cnps_eligibility_pfm::key;'N');2;1)` | 1 yes (default) · 2 no — as 58202 |
| 58204 | CNPS AT/MP eligible | `IF(EQUALS($hr.cnps_eligibility_atmp::key;'N');2;1)` | 1 yes (default) · 2 no — as 58202 |
| 58205 | Art. 3-4° exemption months (young graduate / worker) | `CEIL(MULTIPLY(YEARS_BETWEEN($hr.young_graduate_employee_exemption_start_date;$entry.period_end_date);12))` | As the Dev formula. Months since the Art. 3-4° exemption start (date of recruitment by the real-regime entity), current month included; IRPP exemption while ≤ 60 (« pendant une période de cinq ans »). The same DD date is used for workers. WTC V3.0 names 58205 "Young Graduate Start Date" but its formula (and the Dev) also yields months; read by the IRPP-TS report |
| 58206 | TFE / TAFP relief (entity) | `IF(EQUALS($legal_entity_hr.tfe_tafp_relief::key;'100');1;IF(EQUALS($legal_entity_hr.tfe_tafp_relief::key;'50');2;0))` | 0 none · 1 exempt (LF 2020 Art. 14 as amended by LF 2024 Art. 6 / LF 2026 Art. 6) · 2 50% (CGI Art. 158) — **entity field** |
| 58207 | Transport allowance granted to all staff | `IF(EQUALS($legal_entity_hr.transport_uniform::key;'Y');1;2)` | 1 yes · 2 no — **entity field**, default 1 (Art. 45-13°) |
| 58210 | Plan social (collective redundancy) | `IF(EQUALS($hr.termination_plan_social::key;'Y');1;2)` | 1 yes · 2 no — **DD field** (Art. 45-10°) |
| 58212 | Dependent children | `$hr.number_of_dependent_children` | count of **children** (not dependants) — DAS report and the Art. 45-4° cap (5,000 XAF per child per month) |
| 58213 | CNPS family allowance received (monthly) | `$hr.cnps_family_allowance_monthly` | XAF a month paid by the CNPS for the children — **new DD field**, default 0. Art. 45-4°: imputed on the 5,000 XAF per-child cap |
| 58215 | Entity under the real regime (régime du réel) | `IF(EQUALS($legal_entity_hr.tax_regime::key;'REEL');1;2)` | 1 yes · 2 no — **new entity field**, default 1. Condition of Art. 188-10° and Art. 174-3° |
| 58216 | Employee age (years) | `FLOOR(DIVIDE(DAYS_BETWEEN($hr.date_of_birth;$period.end_date);365.25))` | completed years at period end — `under 35` test of Art. 188-10° and Art. 174-3° (TF/TA, read each month) |
| 58225 | Age at the Art. 3-4° exemption start | `FLOOR(DIVIDE(DAYS_BETWEEN($hr.date_of_birth;$hr.young_graduate_employee_exemption_start_date);365.25))` | completed years at recruitment — `under 35` test of the young graduate in Art. 3-4° (IRPP), checked at recruitment because the exemption then runs five years (A27) |
| 58217 | Worker (ouvrier) | `IF(EQUALS($hr.worker_category::key;'OUVRIER');1;2)` | 1 yes · 2 no — **new DD field**, default 2 |
| 58219 | TFE / TAFP exempt payroll share (youth, disabled, workers) | `IF(AND(EQUALS($58215;1);OR(EQUALS($58218;2);AND(EQUALS($58218;3);LESS($58216;35));AND(EQUALS($58217;1);LESS($58216;35))));1;0)` | 1 = the pay of this employee is outside TFE and TAFP: real-regime entity and (disabled, or young graduate under 35, or worker under 35). Art. 188-10° (TF) and Art. 174-3° (TA), CGI 2026 p. 59–61 — no five-year limit in these articles |
| 58226 | Art. 3-4° IRPP exempt (derived) | `IF(AND(EQUALS($58215;1);GREATER($58205;0);LESS($58205;61);LESS($58225;35);OR(EQUALS($58218;3);EQUALS($58217;1)));1;0)` | 1 = IRPP exempt: CGI Art. 3-4° (p. 15) « Les salaires versés aux jeunes diplômés âgés de moins de 35 ans et aux ouvriers recrutés par les entreprises du régime du réel… pendant une période de cinq ans » — real-regime entity (58215), start date given and within 60 months (0 < 58205 ≤ 60; **the start date is mandatory in the DD when 58218 = 3 or 58217 = 1** — without it there is no exemption), under 35 at recruitment (58225), and young graduate (58218 = 3) or worker (58217 = 1). Round 4: the under-35 limit is applied to workers too — technical decision of the front, 60% (A34): Art. 3-4° attaches the age to « jeunes diplômés » only, but does not expressly set it aside for « ouvriers », and Arts. 188-10° / 174-3° of the same policy (LFI 2021) say « les ouvriers âgés de moins de 35 ans » |
| 58223 | Leave travel ticket — annual limit | `$hr.leave_ticket_annual_limit` | XAF a year: one ticket a year per person (employee, spouse, dependants) at the normal fare from the place of work to the place of origin — **new DD field**, default 0. CGI Art. 45-15° |

Flags of the Dev reused where they cover the case: 58218 (`$hr.employee_type`) and 58205 (Dev formula) as the Dev; 58206 (relief 0 / 1 / 2 — the Dev field is 0 / 1: Deliberate divergence (law), Art. 158 50%) and 58212 (children, not all dependants — Deliberate divergence (law), Art. 45-4°) keep the Dev number with the field the law needs; the others have no Dev equivalent (ASSUMPTIONS A14). 58219 and 58226 are derived from the other flags. 58201 is reserved for advanced reconciliation and is not used.

---

# 9148009 - TD Annual Reporting Limit

## **Regulation Name: TD Annual Reporting Limit**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148009

**Status:** active

**Processing Order (Ordinal):** 9

**1. Classification**

* **Tax Group:** income_tax
* **Tax Rule Group:** simple_tax_monthly
* **Taxation Type:** flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** 

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 100.000 |  | 60,000.000 | 60,000.000 |  |  |  | 01-01-2026 |  |  |  |  |  |  | 58106 | 99999 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 62104 |  | No |
| 62560 |  | No |
| 62561 |  | No |
| 62562 |  | No |
| 62563 |  | No |
| 65579 | 6557% | Yes |
| 65589 | 6558% | Yes |
| 62199 | 621%% | Yes |
| 62299 | 622%% | Yes |
| 62399 | 623%% | Yes |
| 62499 | 624%% | Yes |
| 62599 | 625%% | Yes |
| 62619 | 6261% | Yes |
| 62639 | 6263% | Yes |
| 62659 | 6265% | Yes |
| 62669 | 6266% | Yes |
| 62799 | 627%% | Yes |
| 62869 | 6286% | Yes |
| 62879 | 6287% | Yes |
| 62889 | 6288% | Yes |
| 62890 |  | Yes |
| 62999 | 629%% | Yes |
| 65519 | 6551% | Yes |
| 65619 | 6561% | Yes |
| 65669 | 6566% | Yes |
| 65799 | 657%% | Yes |
| 79499 | 794%% | Yes |

> As the Dev: fixed 60,000 XAF a month (Floor = Ceiling), ordinal 9, before 58105 exists — so, as the Dev, the matrix is the cash pay codes themselves (the same matrix as 9148010); written only when the employee has cash pay; read by the DAS report. Reporting parameter, not a statutory value.

---

# 9148010 - TD Gross Salary

## **Regulation Name: TD Gross Salary**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148010

**Status:** active

**Processing Order (Ordinal):** 10

**1. Classification**

* **Tax Group:** income_tax
* **Tax Rule Group:** simple_tax
* **Taxation Type:** flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** 

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 100.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  |  | 58105 | 99999 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 62104 |  | No |
| 62560 |  | No |
| 62561 |  | No |
| 62562 |  | No |
| 62563 |  | No |
| 65579 | 6557% | Yes |
| 65589 | 6558% | Yes |
| 62199 | 621%% | Yes |
| 62299 | 622%% | Yes |
| 62399 | 623%% | Yes |
| 62499 | 624%% | Yes |
| 62599 | 625%% | Yes |
| 62619 | 6261% | Yes |
| 62639 | 6263% | Yes |
| 62659 | 6265% | Yes |
| 62669 | 6266% | Yes |
| 62799 | 627%% | Yes |
| 62869 | 6286% | Yes |
| 62879 | 6287% | Yes |
| 62889 | 6288% | Yes |
| 62890 |  | Yes |
| 62999 | 629%% | Yes |
| 65519 | 6551% | Yes |
| 65619 | 6561% | Yes |
| 65669 | 6566% | Yes |
| 65799 | 657%% | Yes |
| 79499 | 794%% | Yes |

> Cash pay subject to IRPP (CGI Art. 44-I, Art. 46-I) and base of the Art. 46 caps and of the Art. 45-2° 15% limit. Deliberate divergence (law): cash only — benefits in kind 65%%% and pensions 6264x are not in 58105 (Art. 46-I/II; Art. 45-1°); 6286x, 6255x, 62570 / 6557x / 6558x and 6287x are in, each relieved by its own exemption. 62867 Death allowance taxable (technical decision of the front, pending the user’s ok; ASSUMPTIONS D2). **58105 is read by the DAS report.**

---

# 9148021 - TD Transport Allowance Exemption

## **Regulation Name: TD Transport Allowance Exemption**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148021

**Status:** active

**Processing Order (Ordinal):** 21

**1. Classification**

* **Tax Group:** income_tax
* **Tax Rule Group:** simple_tax
* **Taxation Type:** flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** NOT(EQUALS($58218;4))

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 30.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  |  | 58103 | 99999 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 62104 |  | No |
| 62105 |  | No |
| 62108 |  | No |
| 62109 | 6210% | Yes |

> As the Dev: 30% of base salary into 58103 (CGI Art. 45-13° « salaire de base mensuel »). Pattern 6210% as the Dev; 62104 (rate flag), 62105 and 62108 (Historic Pay) left out as in v5.

---

# 9148031 - TD Transport Allowance - Exempt

## **Regulation Name: TD Transport Allowance - Exempt**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148031

**Status:** active

**Processing Order (Ordinal):** 31

**1. Classification**

* **Tax Group:** income_tax
* **Tax Rule Group:** simple_tax_post_formula
* **Taxation Type:** flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** NOT(EQUALS($58218;4))

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 100.000 |  |  |  |  | MIN($band_amount_raw;$58103) | EQUALS($58207;1) | 01-01-2026 |  |  |  |  |  |  | 99999 | 58104 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 62519 | 6251% | Yes |
| 62529 | 6252% | Yes |

> As the Dev: MIN($band_amount_raw;$58103) into 58104 (negative), read by the DAS report. Deliberate divergence (law): only when the allowance is paid to all staff (58207; Art. 45-13° « lorsqu’elles profitent à tout le personnel ») and 6251x Car & Transportation shares the 30%. Leaves the IRPP base only (not TF/TA, Arts. 173, 189; not CNPS: whole transport out, 9148155).

---

# 9148032 - TD Family Allowance Exemption

## **Regulation Name: TD Family Allowance Exemption**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148032

**Status:** active

**Processing Order (Ordinal):** 32

**1. Classification**

* **Tax Group:** income_tax
* **Tax Rule Group:** simple_tax
* **Taxation Type:** formula
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** NOT(EQUALS($58218;4))

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 100.000 |  |  |  |  | MAX(ADD(MULTIPLY(5000;$58212);MULTIPLY(-1;$58213));0) |  | 01-01-2026 |  |  |  |  |  |  | 58107 | 99999 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 62759 | 6275% | Yes |
| 62769 | 6276% | Yes |
| 62789 | 6278% | Yes |
| 62866 |  | Yes |

> As the Dev: limit in 58107, matrix = family codes. Deliberate divergence (law): 5,000 per **child** (58212 reads children) less the CNPS family allowance (58213) — CGI Art. 45-4° (p. 29; LF 2026 Art. 8, p. 15) « par enfant… sur laquelle viennent… s’imputer les allocations versées par la CNPS ». Codes 6275x, 6276x, 6278x, 62866.

---

# 9148033 - TD Family Allowance final Exemption

## **Regulation Name: TD Family Allowance final Exemption**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148033

**Status:** active

**Processing Order (Ordinal):** 33

**1. Classification**

* **Tax Group:** income_tax
* **Tax Rule Group:** simple_tax_post_formula
* **Taxation Type:** flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** NOT(EQUALS($58218;4))

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 100.000 |  |  |  |  | MIN($band_amount_raw;$58107) |  | 01-01-2026 |  |  |  |  |  |  | 99999 | 58108 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 62759 | 6275% | Yes |
| 62769 | 6276% | Yes |
| 62789 | 6278% | Yes |
| 62866 |  | Yes |

> As the Dev: MIN($band_amount_raw;$58107) into 58108 (negative), read by the DAS report. Excess taxable IRPP; still in the TF/TA base (Art. 189-1° « allocations »).

---

# 9148034 - TD Plan-Social Severance Exemption

## **Regulation Name: TD Plan-Social Severance Exemption**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148034

**Status:** active

**Processing Order (Ordinal):** 34

**1. Classification**

* **Tax Group:** income_tax
* **Tax Rule Group:** simple_tax
* **Taxation Type:** flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** EQUALS($58210;1)

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 100.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  |  | 99999 | 58113 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 62189 | 6218% | Yes |

> Additional regulation (no Dev pair), Dev pattern. Deliberate divergence (law): only plan-social severance is exempt (CGI Art. 45-10°); individual severance stays taxable (Art. 44-I). The Dev excludes all 6218x from the gross instead.

---

# 9148035 - TD Function Allowance Exemption

## **Regulation Name: TD Function Allowance Exemption**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148035

**Status:** active

**Processing Order (Ordinal):** 35

**1. Classification**

* **Tax Group:** income_tax
* **Tax Rule Group:** simple_tax_post_formula
* **Taxation Type:** flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** NOT(EQUALS($58218;4))

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 100.000 |  |  |  |  | MIN($band_amount_raw;MULTIPLY($58105;0.15)) |  | 01-01-2026 |  |  |  |  |  |  | 99999 | 58114 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 62879 | 6287% | Yes |
| 62570 |  | Yes |
| 65579 | 6557% | Yes |
| 65589 | 6558% | Yes |

> Additional regulation (no Dev pair), in the Dev convention (limit inside the formula, % × 58105). Deliberate divergence (law): CGI Art. 45-2° (p. 29) — function-expense allowances and fixed per diem exempt up to 15% of salaries plus those allowances. Codes 6287x (to create, R15), 62570, 6557x, 6558x. IRPP base only.

---

# 9148036 - TD Leave Ticket Exemption

## **Regulation Name: TD Leave Ticket Exemption**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148036

**Status:** active

**Processing Order (Ordinal):** 36

**1. Classification**

* **Tax Group:** income_tax
* **Tax Rule Group:** simple_tax_post_formula
* **Taxation Type:** flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** NOT(EQUALS($58218;4))

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 100.000 |  |  |  |  | MIN($band_amount_raw;$58223) |  | 01-01-2026 |  |  |  |  |  |  | 99999 | 58115 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 62559 | 6255% | Yes |

> Additional regulation (no Dev pair), Dev convention. Deliberate divergence (law): CGI Art. 45-15° (p. 30) — one ticket a year per person (annual limit 58223 from the DD, applied per payment, A24). IRPP base only; in TF/TA; out of CNPS.

---

# 9148041 - TD Housing Capped Value for Tax

## **Regulation Name: TD Housing Capped Value for Tax**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148041

**Status:** active

**Processing Order (Ordinal):** 41

**1. Classification**

* **Tax Group:** income_tax
* **Tax Rule Group:** simple_tax_post_formula
* **Taxation Type:** flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** 

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 100.000 |  |  |  |  | MIN($band_amount_raw;MULTIPLY($58105;0.20)) |  | 01-01-2026 |  |  |  |  |  |  | 58120 | 99999 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 65499 | 654%% | Yes |

> As the Dev: ID, name, ordinal, rule group, % × 58105 inside the formula, account 58120 (read by the DAS report). Deliberate divergence (law): MIN(real value; MULTIPLY($58105;0.20)) instead of the forfait MULTIPLY($58105;0.20) — CGI Art. 46-III « Ceux-ci sont plafonnés », Art. 46-V « dans la limite des taux »; the matrix holds the real benefit codes.

---

# 9148051 - TD Vehicle Capped Value for Tax

## **Regulation Name: TD Vehicle Capped Value for Tax**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148051

**Status:** active

**Processing Order (Ordinal):** 51

**1. Classification**

* **Tax Group:** income_tax
* **Tax Rule Group:** simple_tax_post_formula
* **Taxation Type:** flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** 

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 100.000 |  |  |  |  | MIN($band_amount_raw;MULTIPLY($58105;0.10)) |  | 01-01-2026 |  |  |  |  |  |  | 58121 | 99999 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 65509 | 6550% | Yes |
| 65529 | 6552% | Yes |

> As the Dev: ID, name, ordinal, rule group, % × 58105 inside the formula, account 58121 (read by the DAS report). Deliberate divergence (law): MIN(real value; MULTIPLY($58105;0.10)) instead of the forfait MULTIPLY($58105;0.10) — CGI Art. 46-III « Ceux-ci sont plafonnés », Art. 46-V « dans la limite des taux »; the matrix holds the real benefit codes.

---

# 9148061 - TD Food Capped Value for Tax

## **Regulation Name: TD Food Capped Value for Tax**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148061

**Status:** active

**Processing Order (Ordinal):** 61

**1. Classification**

* **Tax Group:** income_tax
* **Tax Rule Group:** simple_tax_post_formula
* **Taxation Type:** flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** 

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 100.000 |  |  |  |  | MIN($band_amount_raw;MIN(MULTIPLY($58105;0.15);75000)) |  | 01-01-2026 |  |  |  |  |  |  | 58122 | 99999 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 65659 | 6565% | Yes |
| 65679 | 6567% | Yes |

> As the Dev: ID, name, ordinal, rule group, % × 58105 inside the formula, account 58122 (read by the DAS report). Deliberate divergence (law): MIN(real value; MIN(MULTIPLY($58105;0.15);75000)) instead of the forfait MIN(MULTIPLY($58105;0.15);75000) — CGI Art. 46-III « Ceux-ci sont plafonnés », Art. 46-V « dans la limite des taux »; the matrix holds the real benefit codes.

---

# 9148071 - TD Interior furnishings Capped Value for Tax

## **Regulation Name: TD Interior furnishings Capped Value for Tax**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148071

**Status:** active

**Processing Order (Ordinal):** 71

**1. Classification**

* **Tax Group:** income_tax
* **Tax Rule Group:** simple_tax_post_formula
* **Taxation Type:** flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** 

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 100.000 |  |  |  |  | MIN($band_amount_raw;MULTIPLY($58105;0.05)) |  | 01-01-2026 |  |  |  |  |  |  | 58123 | 99999 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 65853 |  | Yes |

> As the Dev: ID, name, ordinal, rule group, % × 58105 inside the formula, account 58123 (read by the DAS report). Deliberate divergence (law): MIN(real value; MULTIPLY($58105;0.05)) instead of the forfait MULTIPLY($58105;0.05) — CGI Art. 46-III « Ceux-ci sont plafonnés », Art. 46-V « dans la limite des taux »; the matrix holds the real benefit codes.

---

# 9148081 - TD Domestic help / security staff Capped Value for Tax

## **Regulation Name: TD Domestic help / security staff Capped Value for Tax**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148081

**Status:** active

**Processing Order (Ordinal):** 81

**1. Classification**

* **Tax Group:** income_tax
* **Tax Rule Group:** simple_tax_post_formula
* **Taxation Type:** flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** 

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 100.000 |  |  |  |  | MIN($band_amount_raw;MULTIPLY($58105;0.04)) |  | 01-01-2026 |  |  |  |  |  |  | 58124 | 99999 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 65854 |  | Yes |

> As the Dev: ID, name, ordinal, rule group, % × 58105 inside the formula, account 58124 (read by the DAS report). Deliberate divergence (law): MIN(real value; MULTIPLY($58105;0.04)) instead of the forfait MULTIPLY($58105;0.04) — CGI Art. 46-III « Ceux-ci sont plafonnés », Art. 46-V « dans la limite des taux »; the matrix holds the real benefit codes.

---

# 9148091 - TD Electricity Capped Value for Tax

## **Regulation Name: TD Electricity Capped Value for Tax**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148091

**Status:** active

**Processing Order (Ordinal):** 91

**1. Classification**

* **Tax Group:** income_tax
* **Tax Rule Group:** simple_tax_post_formula
* **Taxation Type:** flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** 

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 100.000 |  |  |  |  | MIN($band_amount_raw;MULTIPLY($58105;0.04)) |  | 01-01-2026 |  |  |  |  |  |  | 58125 | 99999 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 65855 |  | Yes |

> As the Dev: ID, name, ordinal, rule group, % × 58105 inside the formula, account 58125 (read by the DAS report). Deliberate divergence (law): MIN(real value; MULTIPLY($58105;0.04)) instead of the forfait MULTIPLY($58105;0.04) — CGI Art. 46-III « Ceux-ci sont plafonnés », Art. 46-V « dans la limite des taux »; the matrix holds the real benefit codes.

---

# 9148101 - TD Water Capped Value for Tax

## **Regulation Name: TD Water Capped Value for Tax**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148101

**Status:** active

**Processing Order (Ordinal):** 101

**1. Classification**

* **Tax Group:** income_tax
* **Tax Rule Group:** simple_tax_post_formula
* **Taxation Type:** flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** 

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 100.000 |  |  |  |  | MIN($band_amount_raw;MULTIPLY($58105;0.04)) |  | 01-01-2026 |  |  |  |  |  |  | 58126 | 99999 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 65856 |  | Yes |

> As the Dev: ID, name, ordinal, rule group, % × 58105 inside the formula, account 58126 (read by the DAS report). Deliberate divergence (law): MIN(real value; MULTIPLY($58105;0.04)) instead of the forfait MULTIPLY($58105;0.04) — CGI Art. 46-III « Ceux-ci sont plafonnés », Art. 46-V « dans la limite des taux »; the matrix holds the real benefit codes.

---

# 9148111 - TD Phone Capped Value for Tax

## **Regulation Name: TD Phone Capped Value for Tax**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148111

**Status:** active

**Processing Order (Ordinal):** 111

**1. Classification**

* **Tax Group:** income_tax
* **Tax Rule Group:** simple_tax_post_formula
* **Taxation Type:** flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** 

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 100.000 |  |  |  |  | MIN($band_amount_raw;MULTIPLY($58105;0.03)) |  | 01-01-2026 |  |  |  |  |  |  | 58127 | 99999 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 65609 | 6560% | Yes |
| 65620 |  | Yes |

> As the Dev: ID, name, ordinal, rule group, % × 58105 inside the formula, account 58127 (read by the DAS report). Deliberate divergence (law): MIN(real value; MULTIPLY($58105;0.03)) instead of the forfait MULTIPLY($58105;0.03) — CGI Art. 46-III « Ceux-ci sont plafonnés », Art. 46-V « dans la limite des taux »; the matrix holds the real benefit codes.

---

# 9148121 - TD Gas Capped Value for Tax

## **Regulation Name: TD Gas Capped Value for Tax**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148121

**Status:** active

**Processing Order (Ordinal):** 121

**1. Classification**

* **Tax Group:** income_tax
* **Tax Rule Group:** simple_tax_post_formula
* **Taxation Type:** flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** 

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 100.000 |  |  |  |  | MIN($band_amount_raw;MULTIPLY($58105;0.02)) |  | 01-01-2026 |  |  |  |  |  |  | 58128 | 99999 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 65857 |  | Yes |

> As the Dev: ID, name, ordinal, rule group, % × 58105 inside the formula, account 58128 (read by the DAS report). Deliberate divergence (law): MIN(real value; MULTIPLY($58105;0.02)) instead of the forfait MULTIPLY($58105;0.02) — CGI Art. 46-III « Ceux-ci sont plafonnés », Art. 46-V « dans la limite des taux »; the matrix holds the real benefit codes.

---

# 9148131 - TD Gross Taxable Salary

## **Regulation Name: TD Gross Taxable Salary**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148131

**Status:** active

**Processing Order (Ordinal):** 131

**1. Classification**

* **Tax Group:** income_tax
* **Tax Rule Group:** simple_tax
* **Taxation Type:** flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** NOT(EQUALS($58218;4))

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 100.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  |  | 58008 | 99999 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 58105 |  | Yes |
| 58120 |  | Yes |
| 58121 |  | Yes |
| 58122 |  | Yes |
| 58123 |  | Yes |
| 58124 |  | Yes |
| 58125 |  | Yes |
| 58126 |  | Yes |
| 58127 |  | Yes |
| 58128 |  | Yes |
| 65853 |  | No |
| 65854 |  | No |
| 65855 |  | No |
| 65856 |  | No |
| 65857 |  | No |
| 62679 | 6267% | Yes |
| 62689 | 6268% | Yes |
| 65299 | 652%% | Yes |
| 65630 |  | Yes |
| 65809 | 6580% | No |
| 65899 | 658%% | Yes |

> As the Dev: 58008, read by the DAS report. Deliberate divergence (law): built on the cash gross 58105 plus the capped BIK values; individual severance in (Art. 44-I), 6274x and health insurance 65630 in, 6580x scholarship out (Art. 45-9°).

---

# 9148141 - TD Apprenticeship Base

## **Regulation Name: TD Apprenticeship Base**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148141

**Status:** active

**Processing Order (Ordinal):** 141

**1. Classification**

* **Tax Group:** income_tax
* **Tax Rule Group:** simple_tax_post_formula_period
* **Taxation Type:** flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** AND(NOT(EQUALS($58218;4));NOT(EQUALS($58219;1)))

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 100.000 |  |  |  |  | MULTIPLY(FLOOR(DIVIDE($band_amount_raw;1000));1000) |  | 01-01-2026 |  |  |  |  |  |  | 58534 | 99998 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 62104 |  | No |
| 62560 |  | No |
| 62561 |  | No |
| 62562 |  | No |
| 62563 |  | No |
| 65579 | 6557% | Yes |
| 65589 | 6558% | Yes |
| 62199 | 621%% | Yes |
| 62299 | 622%% | Yes |
| 62399 | 623%% | Yes |
| 62499 | 624%% | Yes |
| 62599 | 625%% | Yes |
| 62619 | 6261% | Yes |
| 62639 | 6263% | Yes |
| 62659 | 6265% | Yes |
| 62669 | 6266% | Yes |
| 62799 | 627%% | Yes |
| 62869 | 6286% | Yes |
| 62879 | 6287% | Yes |
| 62889 | 6288% | Yes |
| 62890 |  | Yes |
| 62999 | 629%% | Yes |
| 65519 | 6551% | Yes |
| 65619 | 6561% | Yes |
| 65669 | 6566% | Yes |
| 65799 | 657%% | Yes |
| 79499 | 794%% | Yes |
| 62679 | 6267% | Yes |
| 62689 | 6268% | Yes |
| 65299 | 652%% | Yes |
| 65499 | 654%% | Yes |
| 65509 | 6550% | Yes |
| 65529 | 6552% | Yes |
| 65699 | 656%% | Yes |
| 65899 | 658%% | Yes |
| 62229 | 6222% | No |
| 62189 | 6218% | No |
| 62900 |  | No |
| 62909 |  | No |
| 62919 | 6291% | No |
| 62929 | 6292% | No |
| 62939 | 6293% | No |

> As the Dev: rule group, truncation to the 1,000 (Art. 177), 58534 read by the TAFP report. Deliberate divergence (law): gross base of Art. 173 (no Art. 45 carve-out; one-time bonuses 6222x, pensions 6264x and — v6 r3 — termination payments 6218x, 62900/62909, 6291x–6293x out: Art. 173 lists remuneration and regular gratifications only) and the Art. 174-3° share out (58219).

---

# 9148151 - TD Employer Lump-Sum Tax Base

## **Regulation Name: TD Employer Lump-Sum Tax Base**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148151

**Status:** active

**Processing Order (Ordinal):** 151

**1. Classification**

* **Tax Group:** income_tax
* **Tax Rule Group:** simple_tax_period
* **Taxation Type:** flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** AND(NOT(EQUALS($58218;4));NOT(EQUALS($58219;1)))

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 100.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  |  | 58563 | 99998 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 62104 |  | No |
| 62649 | 6264% | Yes |
| 62560 |  | No |
| 62561 |  | No |
| 62562 |  | No |
| 62563 |  | No |
| 65579 | 6557% | Yes |
| 65589 | 6558% | Yes |
| 62199 | 621%% | Yes |
| 62299 | 622%% | Yes |
| 62399 | 623%% | Yes |
| 62499 | 624%% | Yes |
| 62599 | 625%% | Yes |
| 62619 | 6261% | Yes |
| 62639 | 6263% | Yes |
| 62659 | 6265% | Yes |
| 62669 | 6266% | Yes |
| 62799 | 627%% | Yes |
| 62869 | 6286% | Yes |
| 62879 | 6287% | Yes |
| 62889 | 6288% | Yes |
| 62890 |  | Yes |
| 62999 | 629%% | Yes |
| 65519 | 6551% | Yes |
| 65619 | 6561% | Yes |
| 65669 | 6566% | Yes |
| 65799 | 657%% | Yes |
| 79499 | 794%% | Yes |
| 62679 | 6267% | Yes |
| 62689 | 6268% | Yes |
| 65299 | 652%% | Yes |
| 65499 | 654%% | Yes |
| 65509 | 6550% | Yes |
| 65529 | 6552% | Yes |
| 65699 | 656%% | Yes |
| 65899 | 658%% | Yes |

> As the Dev: rule group, 58563 read by the TFE report. Deliberate divergence (law): gross base of Art. 189 (« indemnités diverses, allocations, gratifications », pensions; benefits at real value) — v6 r3: severance 6218x and EOS gratuities 629xx **in** (« indemnités diverses ») — technical decision of the front, pending the user’s ok; reverses `correcoes.md` 2026-07-07 ("severance outside the TFE"; ASSUMPTIONS A20), medical insurance 6261x and social allowance 6265x in, cash-in-lieu 6561x / 6566x in; the Art. 188-10° share out (58219).

---

# 9148155 - TD CNPS Insurable Salary without capping

## **Regulation Name: TD CNPS Insurable Salary without capping**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148155

**Status:** active

**Processing Order (Ordinal):** 155

**1. Classification**

* **Tax Group:** social_security
* **Tax Rule Group:** simple_tax
* **Taxation Type:** flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** NOT(EQUALS($58218;4))

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 100.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  |  | 58130 | 99999 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 62104 |  | No |
| 62180 |  | No |
| 62181 |  | No |
| 62182 |  | No |
| 62540 |  | No |
| 62541 |  | No |
| 62542 |  | No |
| 62550 |  | No |
| 62551 |  | No |
| 62552 |  | No |
| 62560 |  | No |
| 62561 |  | No |
| 62562 |  | No |
| 62563 |  | No |
| 62570 |  | No |
| 62900 |  | No |
| 62909 |  | No |
| 65570 |  | No |
| 65571 |  | No |
| 65572 |  | No |
| 65580 |  | No |
| 65581 |  | No |
| 65582 |  | No |
| 62519 | 6251% | No |
| 62529 | 6252% | No |
| 62759 | 6275% | No |
| 62769 | 6276% | No |
| 62789 | 6278% | No |
| 62869 | 6286% | Yes |
| 62879 | 6287% | No |
| 65669 | 6566% | No |
| 62199 | 621%% | Yes |
| 62299 | 622%% | Yes |
| 62399 | 623%% | Yes |
| 62499 | 624%% | Yes |
| 62599 | 625%% | Yes |
| 62919 | 6291% | No |
| 62929 | 6292% | No |
| 62939 | 6293% | No |
| 62619 | 6261% | Yes |
| 62639 | 6263% | Yes |
| 62659 | 6265% | Yes |
| 62669 | 6266% | Yes |
| 62679 | 6267% | Yes |
| 62689 | 6268% | Yes |
| 62799 | 627%% | Yes |
| 62890 |  | Yes |
| 62999 | 629%% | Yes |
| 65299 | 652%% | Yes |
| 65499 | 654%% | Yes |
| 65599 | 655%% | Yes |
| 65699 | 656%% | Yes |
| 65799 | 657%% | Yes |
| 65899 | 658%% | Yes |
| 79499 | 794%% | Yes |

> As the Dev: 58130, read by the CNPS Récapitulatif. Deliberate divergence (law): base per Dec. 1635 art. 3 / Dec. 1636 art. 2 and the CNPS guide p. 7–8 — benefits in kind, 6286x, 6274x, 6580x in; family allowances, meal cash 6566x, severance, ticket, per diem, relocation, 6287x out; transport 6251x/6252x out in full (technical decision of the front, guide p. 8, pending the user’s ok; ASSUMPTIONS D1).

---

# 9148161 - TD CNPS Insurable Salary

## **Regulation Name: TD CNPS Insurable Salary**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148161

**Status:** active

**Processing Order (Ordinal):** 161

**1. Classification**

* **Tax Group:** social_security
* **Tax Rule Group:** simple_tax_period
* **Taxation Type:** flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** AND(NOT(EQUALS($58218;4));GREATER($58130;0))

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 100.000 |  | 720,000.000 | 6,000,000.000 |  |  |  | 01-01-2026 |  |  |  |  |  |  | 58550 | 99998 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 58130 |  | Yes |

> As the Dev: rule group, floor 720,000 / ceiling 6,000,000 a year (60,000 / 500,000 a month; Dec. 1635 art. 4, Dec. 1636 art. 3; guide p. 9), 58550. Deliberate divergence (law): `GREATER($58130;0)` — no floor in a month without pay (guide p. 7). December regularisation of the annual ceiling not built (A23).

---

# 9148171 - TD CNPS Contribution EE and ER

## **Regulation Name: TD CNPS Contribution EE and ER**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148171

**Status:** active

**Processing Order (Ordinal):** 171

**1. Classification**

* **Tax Group:** social_security
* **Tax Rule Group:** simple_tax_$$_post_formula
* **Taxation Type:** flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** NOT(EQUALS($58218;4))

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 3.500 |  |  |  |  | FLOOR(ADD($band_amount_raw;0.5)) | EQUALS($58202;1) | 01-01-2026 |  |  |  |  |  |  | 2610 | 2551 |
|  |  |  | 7.500 |  |  |  | FLOOR(ADD($band_amount_raw;0.5)) | EQUALS($58203;1) | 01-01-2026 |  |  |  |  |  |  | 6020 | 2550 |
|  |  |  | 4.000 |  |  |  | FLOOR(ADD($band_amount_raw;0.5)) | EQUALS($58204;1) | 01-01-2026 |  |  |  |  |  |  | 6040 | 2560 |
|  |  |  | 5.000 |  |  |  | FLOOR(ADD($band_amount_raw;0.5)) | EQUALS($58202;1) | 01-01-2026 |  |  |  |  |  |  | 6037 | 2537 |
|  |  | 3.500 |  |  |  |  | FLOOR(ADD($band_amount_raw;0.5)) | EQUALS($58202;1) | 01-01-2026 |  |  |  |  |  |  | 99999 | 58100 |
|  |  | 100.000 |  |  |  |  | 20 | GREATER($58550;0) | 01-01-2026 |  |  |  |  |  |  | 58131 | 99999 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 58550 |  | Yes |

> As the Dev: one regulation, band order (3.5 EE · 7.5 PFM · 4 AT/MP · 5 PVID ER · 3.5 deduction to 58100 · rate 20 to 58131), FLOOR(ADD(x;0.5)), `_$$`. Not copied: the Dev posts the 3.5% employee band to 6020/2550 and the 7.5% employer band to 2610/2551 — an error against the WTC V3.0 (2551 = EE, 2550 = ER); v6 keeps EE 2610/2551, PFM 6020/2550. Deliberate divergence (law): each band gated by a branch flag (seconded employee under a convention, guide p. 6); rate 58131 only when 58550 > 0. Rates: Dec. 1635 arts. 1–2, Dec. 1636 art. 1, Dec. 1634/2009 (guide p. 8).

---

# 9148175 - TD Retirement Contribution Limit

## **Regulation Name: TD Retirement Contribution Limit**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148175

**Status:** active

**Processing Order (Ordinal):** 175

**1. Classification**

* **Tax Group:** income_tax
* **Tax Rule Group:** simple_tax
* **Taxation Type:** flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** NOT(EQUALS($58218;4))

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 3.500 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  |  | 58172 | 99999 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 62104 |  | No |
| 62105 |  | No |
| 62108 |  | No |
| 62109 | 6210% | Yes |

> Additional regulation (no Dev pair), Dev pattern. Deliberate divergence (law): 3.5% of the appointments, the deduction cap of CGI Art. 47-I (p. 30), into 58172, read by 9148181.

---

# 9148181 - TD Voluntary Contribution

## **Regulation Name: TD Voluntary Contribution**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148181

**Status:** active

**Processing Order (Ordinal):** 181

**1. Classification**

* **Tax Group:** income_tax
* **Tax Rule Group:** simple_tax_post_formula
* **Taxation Type:** flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** NOT(EQUALS($58218;4))

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 100.000 |  |  |  |  | MIN($band_amount_raw;$58172) |  | 01-01-2026 |  |  |  |  |  |  | 99999 | 58101 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 21610 |  | No |
| 21611 |  | No |
| 21670 |  | No |
| 21649 | 2164% | No |
| 21699 | 216%% | Yes |

> As the Dev: ID, name, ordinal, account 58101. Deliberate divergence (law): capped at 3.5% (MIN with 58172, Art. 47-I) and only compulsory schemes — 2164x "Voluntary Contribution" No (Art. 47-II « caractère obligatoire »); compulsory-scheme code to create (R16).

---

# 9148191 - TD Taxable Income

## **Regulation Name: TD Taxable Income**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148191

**Status:** active

**Processing Order (Ordinal):** 191

**1. Classification**

* **Tax Group:** income_tax
* **Tax Rule Group:** simple_tax
* **Taxation Type:** flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** NOT(EQUALS($58218;4))

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 100.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  |  | 58552 | 99999 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 58008 |  | Yes |
| 58104 |  | Yes |
| 58108 |  | Yes |
| 58113 |  | Yes |
| 58114 |  | Yes |
| 58115 |  | Yes |
| 58100 |  | Yes |
| 58101 |  | Yes |

> As the Dev: 58552 = IRPP gross less the exempt parts and deductions (CGI Art. 47-I), read by the IRPP-TS and DAS reports. Deliberate divergence (law): also nets plan social 58113, the 15% allowance 58114 and the leave ticket 58115.

---

# 9148192 - TD Non-Resident Tax Base

## **Regulation Name: TD Non-Resident Tax Base**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148192

**Status:** active

**Processing Order (Ordinal):** 192

**1. Classification**

* **Tax Group:** income_tax
* **Tax Rule Group:** simple_tax_period
* **Taxation Type:** flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** EQUALS($58218;1)

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 100.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  |  | 58592 | 99998 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 58552 |  | Yes |

> Deliberate divergence (law) (replaces Dev 9148011): the non-resident employee is taxed on the progressive scale with the Art. 45–47 reliefs (CGI Arts. 44-II-2°, 847; Art. 116 covers only Art. 2-VI and Art. 60), so its base is 58552, known only after 9148191; copied into 58592 for the IRPP-TS report.

---

# 9148201 - TD Taxable Income - Annualised

## **Regulation Name: TD Taxable Income - Annualised**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148201

**Status:** active

**Processing Order (Ordinal):** 201

**1. Classification**

* **Tax Group:** income_tax
* **Tax Rule Group:** simple_tax_post_formula
* **Taxation Type:** flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** AND(OR(LESS($58218;2);EQUALS($58218;3));NOT(EQUALS($58226;1)))

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 100.000 |  |  |  |  | MULTIPLY($band_amount_raw;$period_divisor) |  | 01-01-2026 |  |  |  |  |  |  | 58110 | 99999 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 58552 |  | Yes |

> As the Dev: 58552 × period divisor into 58110. Pre-condition SCALE instead of the Dev NOT(EQUALS($58218;4)) so that 58110–58112 stay 0 for the exempt (disabled, Art. 3-4°), as in v5 — the reports must not read a tax for someone who owes none. Irregular payments are annualised with the month (A26: method depends on the DGI barème, Art. 847).

---

# 9148211 - TD Taxable Income - Annual Tax

## **Regulation Name: TD Taxable Income - Annual Tax**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148211

**Status:** active

**Processing Order (Ordinal):** 211

**1. Classification**

* **Tax Group:** income_tax
* **Tax Rule Group:** simple_tax_monthly
* **Taxation Type:** differential
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** 

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.000 | 800,000.000 | 0.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  |  | 58111 | 99999 |
| 800,000.000 | 6,000,000.000 | 10.500 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  |  | 58111 | 99999 |
| 6,000,000.000 | 7,500,000.000 | 15.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  |  | 58111 | 99999 |
| 7,500,000.000 | 9,000,000.000 | 20.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  |  | 58111 | 99999 |
| 9,000,000.000 | 12,000,000.000 | 25.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  |  | 58111 | 99999 |
| 12,000,000.000 | 9,999,999,999,999.000 | 30.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  |  | 58111 | 99999 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 58110 |  | Yes |

> As the Dev: annual scale on 58110 (`_monthly`: bands not divided), result 58111. CGI Art. 1-IV (p. 14; LF 2026 Art. 3). Deliberate divergence (law): limits at the round figure (incomeTo 800,000 = next incomeFrom) — the tax starts at the 800,001st franc; the Dev's `x.99` limits give 1 XAF less at a half franc.

---

# 9148221 - TD Taxable Income - Period Tax

## **Regulation Name: TD Taxable Income - Period Tax**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148221

**Status:** active

**Processing Order (Ordinal):** 221

**1. Classification**

* **Tax Group:** income_tax
* **Tax Rule Group:** simple_tax_post_formula
* **Taxation Type:** flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** NOT(EQUALS($58218;4))

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 100.000 |  |  |  |  | DIVIDE($band_amount_raw;$period_divisor) |  | 01-01-2026 |  |  |  |  |  |  | 58112 | 99999 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 58111 |  | Yes |

> As the Dev: annual tax ÷ period divisor into 58112.

---

# 9148231 - TD Taxable Income - Period Tax - Resident

## **Regulation Name: TD Taxable Income - Period Tax - Resident**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148231

**Status:** active

**Processing Order (Ordinal):** 231

**1. Classification**

* **Tax Group:** income_tax
* **Tax Rule Group:** simple_tax_$$_post_formula
* **Taxation Type:** flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** AND(OR(LESS($58218;1);EQUALS($58218;3));NOT(EQUALS($58226;1)))

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 100.000 |  |  |  |  | FLOOR(ADD($band_amount_raw;0.5)) |  | 01-01-2026 |  |  |  |  |  |  | 2610 | 2552 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 58112 |  | Yes |

> As the Dev: FLOOR(ADD(x;0.5)) on 58112 (technical convention, no rule in the CGI), `_$$`, 2610/2552. Deliberate divergence (law): pre-condition with the Art. 3-4° test (58226: real-regime employer, start date, ≤ 60 months, under 35 at recruitment, young graduate or worker); disabled (Art. 45-18°) and diplomatic (Art. 3-2°) out.

---

# 9148241 - TD Taxable Income - Period Tax - Non-Resident

## **Regulation Name: TD Taxable Income - Period Tax - Non-Resident**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148241

**Status:** active

**Processing Order (Ordinal):** 241

**1. Classification**

* **Tax Group:** income_tax
* **Tax Rule Group:** simple_tax_$$_post_formula
* **Taxation Type:** flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** AND(EQUALS($58218;1);NOT(EQUALS($58226;1)))

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 100.000 |  |  |  |  | FLOOR(ADD($band_amount_raw;0.5)) |  | 01-01-2026 |  |  |  |  |  |  | 2610 | 2592 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 58112 |  | Yes |

> As the Dev: ID, rule group, rounding, 2610/2592. Deliberate divergence (law): 100% of the scale result 58112, not 18% (CGI Arts. 44-II-2°, 847; Art. 116 only for Art. 2-VI and Art. 60).

---

# 9148251 - TD Apprenticeship Tax

## **Regulation Name: TD Apprenticeship Tax**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148251

**Status:** active

**Processing Order (Ordinal):** 251

**1. Classification**

* **Tax Group:** income_tax
* **Tax Rule Group:** simple_tax_post_formula
* **Taxation Type:** flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** NOT(EQUALS($58218;4))

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | 1.200 |  |  |  | MULTIPLY(FLOOR(DIVIDE(ADD(MULTIPLY($band_amount_raw;IF(EQUALS($58206;1);0;IF(EQUALS($58206;2);0.5;1)));5);10));10) |  | 01-01-2026 |  |  |  |  |  |  | 6034 | 2534 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 58534 |  | Yes |

> As the Dev: 12‰ (Art. 178), rounding to the nearest 10 (Art. 177), 6034/2534. Deliberate divergence (law): relief 50% / 100% (58206; CGI Art. 158 « 50% de la taxe d’apprentissage »; LF 2020 Art. 14).

---

# 9148261 - TD Lump Sum Tax

## **Regulation Name: TD Lump Sum Tax**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148261

**Status:** active

**Processing Order (Ordinal):** 261

**1. Classification**

* **Tax Group:** income_tax
* **Tax Rule Group:** simple_tax_post_formula
* **Taxation Type:** flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** NOT(EQUALS($58218;4))

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | 7.500 |  |  |  | FLOOR(ADD(MULTIPLY($band_amount_raw;IF(EQUALS($58206;1);0;IF(EQUALS($58206;2);0.5;1)));0.5)) |  | 01-01-2026 |  |  |  |  |  |  | 6063 | 2563 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 58563 |  | Yes |

> As the Dev: 7.5% (Art. 190), 6063/2563. Deliberate divergence (law): relief 0 / 50% / 100% (58206; Art. 158; the Dev only has the total exemption) and payment to the whole franc, FLOOR(x+0.5) — technical payment convention (Art. 190 has no rounding rule).

---

# 9148271 - TD Food Security Levy (PSA)

## **Regulation Name: TD Food Security Levy (PSA)**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148271

**Status:** active

**Processing Order (Ordinal):** 271

**1. Classification**

* **Tax Group:** income_tax
* **Tax Rule Group:** simple_tax_$$_monthly
* **Taxation Type:** flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** AND(NOT(EQUALS($58218;4));GREATER($58105;0))

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 100.000 |  | 400.000 | 400.000 |  |  |  | 01-01-2026 |  |  |  |  |  |  | 2610 | 2570 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 58105 |  | Yes |

> Additional regulation (no Dev pair), Dev pattern (floor = ceiling, `_monthly`, as 9148009). Deliberate divergence (law): CGI Arts. 837–839 (p. 166) — 400 FCFA a month per employee, employee deduction, recovered as IRPP. Liability 2570, new WTC code (R17).

---
