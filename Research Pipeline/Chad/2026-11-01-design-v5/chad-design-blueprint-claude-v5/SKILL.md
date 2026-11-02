---
name: "chad-design-blueprint-claude-v5"
description: "Chad (TD) payroll regulation design v5 — v4 plus the statutory verdicts of 1 Nov 2026 read in the CGI 2026 (DGI edition) and the WTC V3.0, the CNPS decrees of 2009 and the CNPS employer guide (round 2, same day), and the engine structures where the Dev design is better. Design Blueprint format, tax year td_2026. Round 3 after the independent QA review."
---

> **Analysis instructions:** read and follow `Regulation_Design_Analysis_Engine.md` before interpreting or computing any regulation below.

> **Companions:** `CHANGELOG.md` — what changed from v4 and the article behind it · `ASSUMPTIONS.md` — decisions taken, alternatives and what is still not settled · `RESEARCH_GAPS.md` — what compliance must fix · `VALIDATION.md` — the scenarios executed, expected × obtained, and v5 × Dev.

> **Source of every article cited:** Code Général des Impôts du Tchad 2026, DGI edition (`raw/docs/oficiais/TD/2026-11-01-CGI-TCHAD-2026-FINAL-dgi.pdf`, md5 139d5326…); LF 2024–2026 where the CGI says so; CNPS: Dec. 1635 and 1636/PR/PM/MFPT/2009 and the CNPS Guide de l’employeur 2019 (`raw/docs/oficiais/TD/2026-11-01-*`).

# 0 - Flags

| Account | Flag | Formula | Values |
| --- | --- | --- | --- |
| 58218 | Status (global flag) | `IF(EQUALS($hr.residency_status::key;'NRES');1;IF(EQUALS($hr.residency_status::key;'DISABLED');2;IF(EQUALS($hr.residency_status::key;'YOUNG-GRAD');3;IF(EQUALS($hr.residency_status::key;'DIPLO');4;0))))` | 0 resident · 1 non-resident · 2 disabled (CGI Art. 45-18°) · 3 young graduate (Art. 3-4°) · 4 diplomatic (Art. 3-2°) — catalogue numbering; routing uses `LESS($58218;1)` for residents, never an equality test against zero |
| 58202 | CNPS PVID eligible | `IF(EQUALS($hr.cnps_eligibility_pvid::key;'N');2;1)` | 1 yes (default, every employee, **non-residents included**: « quelle que soit… leur nationalité », CNPS guide p. 6) · 2 no — only a seconded employee covered by a bilateral or multilateral convention (CIPRES) with a secondment certificate |
| 58203 | CNPS PFM eligible | `IF(EQUALS($hr.cnps_eligibility_pfm::key;'N');2;1)` | 1 yes (default) · 2 no — as 58202 |
| 58204 | CNPS AT/MP eligible | `IF(EQUALS($hr.cnps_eligibility_atmp::key;'N');2;1)` | 1 yes (default) · 2 no — as 58202 |
| 58205 | Art. 3-4° exemption months (young graduate / worker) | `ADD(FLOOR(DIVIDE(DAYS_BETWEEN($hr.young_graduate_employee_exemption_start_date;$period.end_date);30.4375));1)` | months since the Art. 3-4° exemption start (date of recruitment by the real-regime entity), current month included; IRPP exemption while ≤ 60 (« pendant une période de cinq ans »). The same DD date is used for workers. WTC V3.0 names 58205 "Young Graduate Start Date" but its formula (and the Dev) also yields months; read by the IRPP-TS report |
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

Flag numbers follow the WTC V3.0 / Dev where they exist (58205, 58206, 58212, 58218 — 58212 counts children, not all dependants); the others are new (ASSUMPTIONS A14). 58219 and 58226 are derived from the other flags. 58201 is reserved for advanced reconciliation and is not used.

---

# 9148011 - TD Base Salary

## **Regulation Name: TD Base Salary**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148011

**Status:** active

**Processing Order (Ordinal):** 11

**1. Classification**

* **Tax Group:** Income Tax
* **Tax Rule Group:** simple_tax
* **Taxation Type:** Flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** 

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 100.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  |  | 58109 | 99999 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 62100 |  | Yes |
| 62101 |  | Yes |
| 62102 |  | Yes |
| 62103 |  | Yes |
| 62109 |  | Yes |

> Basic salary series 6210 (62104 rate flag, 62105 and 62108 Historic Pay excluded). Measure for the 30% transport limit and the 3.5% retirement limit.

---

# 9148012 - TD Cash Gross

## **Regulation Name: TD Cash Gross**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148012

**Status:** active

**Processing Order (Ordinal):** 12

**1. Classification**

* **Tax Group:** Income Tax
* **Tax Rule Group:** simple_tax
* **Taxation Type:** Flat
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
| 62639 | 6263% | Yes |
| 62650 |  | Yes |
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

> Cash earnings subject to IRPP (CGI Art. 44-I, Art. 46-I); base of the Art. 46 caps and of the Art. 45-2° 15% limit. v5: the whole 6286x series is in (meal/food 62860–62865, birth 62866, death 62867, gift 62868–62869; WTC V3.0) — Art. 45 exempts none of them, Art. 44-I includes « gratifications ». 62866 is then relieved by the Art. 45-4° cap (9148022). Round 2: leave travel ticket 6255x and per diem 62570 / 6557x / 6558x are in (relieved by 9148025 and 9148024); relocation 2 (6256x, reimbursement) stays out. 6274x schooling allowance taxable (627%%). 62867 (death allowance) is taxable (technical decision of the Chade front (source: WTC V3.0 code name "Death allowance" read as an employer allowance, not the « capital décès » of Art. 45-11°), pending the user’s ok; alternative and its effect in ASSUMPTIONS D2 / RESEARCH_GAPS R28). Pensions 6264x out (Art. 45-1°). **58105 is the account the DAS report reads.**

---

# 9148013 - TD Annual Reporting Limit

## **Regulation Name: TD Annual Reporting Limit**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148013

**Status:** active

**Processing Order (Ordinal):** 13

**1. Classification**

* **Tax Group:** Income Tax
* **Tax Rule Group:** retro_simple_tax_monthly
* **Taxation Type:** Flat
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
| 58105 |  | Yes |

> Fixed 60,000 XAF a month (Floor = Ceiling, `_monthly`), written only when the employee has cash gross. Read by the DAS report to split employees above / at or below 60,000 XAF. Reporting parameter, not a statutory value.

---

# 9148014 - TD Limits on Base Salary

## **Regulation Name: TD Limits on Base Salary**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148014

**Status:** active

**Processing Order (Ordinal):** 14

**1. Classification**

* **Tax Group:** Income Tax
* **Tax Rule Group:** retro_simple_tax
* **Taxation Type:** Flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** 

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 30.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  |  | 58103 | 99999 |
|  |  | 3.500 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  |  | 58172 | 99999 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 58109 |  | Yes |

> Derived limits in their own regulation, applied downstream as ceiling accounts: 58103 = 30% of base salary (CGI Art. 45-13°, transport; WTC V3.0 account "TD Transport Allowance Exemption") · 58172 = 3.5% of the appointments (CGI Art. 47-I, retirement).

---

# 9148015 - TD Limits on Cash Remuneration

## **Regulation Name: TD Limits on Cash Remuneration**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148015

**Status:** active

**Processing Order (Ordinal):** 15

**1. Classification**

* **Tax Group:** Income Tax
* **Tax Rule Group:** retro_simple_tax
* **Taxation Type:** Flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** 

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 20.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  |  | 58161 | 99999 |
|  |  | 10.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  |  | 58162 | 99999 |
|  |  | 15.000 |  |  | 900,000.000 |  |  |  | 01-01-2026 |  |  |  |  |  |  | 58163 | 99999 |
|  |  | 5.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  |  | 58164 | 99999 |
|  |  | 4.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  |  | 58165 | 99999 |
|  |  | 4.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  |  | 58166 | 99999 |
|  |  | 4.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  |  | 58167 | 99999 |
|  |  | 3.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  |  | 58168 | 99999 |
|  |  | 2.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  |  | 58169 | 99999 |
|  |  | 15.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  |  | 58173 | 99999 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 58105 |  | Yes |

> Bands 1–9: CGI Art. 46-III caps, one band per benefit, on the cash remuneration 58105 (Art. 46-I/II): housing 20 · vehicle 10 · food 15 (and 75,000 XAF a month, stated annually as the band ceiling) · furnishings 5 · domestic 4 · electricity 4 · water 4 · telephone 3 · gas 2. **Band 10 (v5): 58173 = 15% of the cash remuneration**, CGI Art. 45-2° (« 15 % calculé sur la masse globale des salaires et desdites allocations »; 58105 already contains the allowance). Read as ceiling accounts by 9148024 and 9148031–9148039.

---

# 9148016 - TD Family Allowance Exemption Limit

## **Regulation Name: TD Family Allowance Exemption Limit**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148016

**Status:** active

**Processing Order (Ordinal):** 16

**1. Classification**

* **Tax Group:** Income Tax
* **Tax Rule Group:** simple_tax
* **Taxation Type:** Formula
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

> v5, structure taken from the Dev (limit in its own regulation, matrix = the family codes, so it only matters when a family allowance is paid; account 58107 as in WTC V3.0). Scope: the cap is written for « l'employeur autre que l'État, les Communes ou les organismes para administratifs » — every Mercans client entity is private, so it is applied to all (A29). CGI Art. 45-4° (CGI 2026 p. 29; LF 2026 Art. 8, p. 15): the allowances paid by an employer other than the State « ne peut excéder mensuellement par enfant la somme de 5.000 Francs sur laquelle viennent… s'imputer les allocations versées par la CNPS ». Limit = max(0; 5,000 × children (58212) − CNPS family allowance (58213)). Monthly amount, no period division.

---

# 9148021 - TD Transport Allowance — Exempt Portion

## **Regulation Name: TD Transport Allowance — Exempt Portion**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148021

**Status:** active

**Processing Order (Ordinal):** 21

**1. Classification**

* **Tax Group:** Income Tax
* **Tax Rule Group:** retro_simple_tax
* **Taxation Type:** Flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** 

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 100.000 |  |  |  |  |  | EQUALS($58207;1) | 01-01-2026 |  |  |  |  |  | 58103 | 99999 | 58104 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 62519 | 6251% | Yes |
| 62529 | 6252% | Yes |

> CGI Art. 45-13°: exempt up to 30% of base salary when granted to all staff (58207). Round 3: 6251x "Car & Transportation allowance" and 6252x "Transportation allowance" share the one 30% limit (58103, ceiling account) — both are transport, as in the CNPS base where both are out. Negative in 58104; subtracts in the IRPP taxable base only (not in TFE/TAFP, Arts. 173 and 189). v5 round 2: no longer used in the CNPS base — the whole transport allowance is outside CNPS (9148051). 58104 is read by the DAS report.

---

# 9148022 - TD Family Allowance — Exempt Portion

## **Regulation Name: TD Family Allowance — Exempt Portion**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148022

**Status:** active

**Processing Order (Ordinal):** 22

**1. Classification**

* **Tax Group:** Income Tax
* **Tax Rule Group:** retro_simple_tax
* **Taxation Type:** Flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** 

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 100.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  | 58107 | 99999 | 58108 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 62759 | 6275% | Yes |
| 62769 | 6276% | Yes |
| 62789 | 6278% | Yes |
| 62866 |  | Yes |

> v5: CGI Art. 45-4° — exempt only up to the limit 58107 (5,000 XAF per child per month, less the CNPS allowance); the excess is taxable IRPP. v4 exempted the whole amount on the basis of `correcoes.md` 2026-07-07, which the Art. 45-4° text contradicts. Codes: 6275x, 6276x (Family allowance, WTC V3.0), 6278x (Family allowance), 62866 (Birth allowance: « allocation d'assistance à famille »). Negative in 58108, read by the DAS report. Still in the TFE/TAFP base (Art. 189-1° « allocations »).

---

# 9148023 - TD Plan-Social Severance — Exempt Portion

## **Regulation Name: TD Plan-Social Severance — Exempt Portion**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148023

**Status:** active

**Processing Order (Ordinal):** 23

**1. Classification**

* **Tax Group:** Income Tax
* **Tax Rule Group:** simple_tax
* **Taxation Type:** Flat
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

> CGI Art. 45-10°: severance under a collective-redundancy plan is fully exempt. Individual severance stays taxable (Art. 44-I). Negative in 58113.

---

# 9148024 - TD Function Expense Allowance — Exempt Portion (15%)

## **Regulation Name: TD Function Expense Allowance — Exempt Portion (15%)**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148024

**Status:** active

**Processing Order (Ordinal):** 24

**1. Classification**

* **Tax Group:** Income Tax
* **Tax Rule Group:** retro_simple_tax
* **Taxation Type:** Flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** 

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 100.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  | 58173 | 99999 | 58114 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 62879 | 6287% | Yes |
| 62570 |  | Yes |
| 65579 | 6557% | Yes |
| 65589 | 6558% | Yes |

> v5, new. CGI Art. 45-2° (CGI 2026 p. 29): « allocations spéciales destinées à couvrir les frais inhérents à la fonction ou à l'emploi et effectivement utilisées conformément à leur objet » exempt while they do not exceed 15% of salaries plus those allowances. Exempt = MIN(allowances; 58173), one cap shared by all the codes in the matrix. Negative in 58114; subtracts in the IRPP base only (TFE/TAFP: Art. 189-1° « indemnités diverses, allocations », no carve-out; CNPS: outside, 9148051). Codes (round 2, decision of 1 Nov on Art. 45-2°): per diem allowance 62570 and per diem benefit 6557x / 6558x (fixed amounts, no receipts) and 6287x "Function expense allowance (Art. 45-2°)" — **6287x not in WTC V3.0**, to be created (R15). A reimbursement of real expenses with receipts is not income (Art. 44-I) and must be paid on a code outside every base (as relocation 2, 6256x). No 30% professional-expense deduction exists for salaries (Art. 47 allows only compulsory pension and social security) and none is built.

---

# 9148025 - TD Leave Travel Ticket — Exempt Portion

## **Regulation Name: TD Leave Travel Ticket — Exempt Portion**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148025

**Status:** active

**Processing Order (Ordinal):** 25

**1. Classification**

* **Tax Group:** Income Tax
* **Tax Rule Group:** retro_simple_tax
* **Taxation Type:** Flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** 

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 100.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  | 58223 | 99999 | 58115 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 62559 | 6255% | Yes |

> v5 round 2, new. CGI Art. 45-15° (p. 30): « frais de voyage pour congé réellement exposés… dans la limite de la valeur d'un billet par an et par personne au tarif normal du lieu de travail au lieu d'origine ». Travel ticket allowance 6255x is now in the cash gross (IRPP) and the TFE/TAFP base; the exempt part = MIN(amount; 58223, the annual ticket limit from the DD) goes negative to 58115 and leaves the IRPP base only. CNPS: outside (« indemnités de déplacement », guide p. 8). The limit is annual and applied per payment (A24: assumes one ticket payment a year; a YTD version needs `_ytd` on 58223 vs the year's 58115).

---

# 9148031 - TD BIK Housing — Capped Value for IRPP

## **Regulation Name: TD BIK Housing — Capped Value for IRPP**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148031

**Status:** active

**Processing Order (Ordinal):** 31

**1. Classification**

* **Tax Group:** Income Tax
* **Tax Rule Group:** retro_simple_tax
* **Taxation Type:** Flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** 

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 100.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  | 58161 | 58120 | 99999 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 65499 | 654%% | Yes |

> CGI Art. 46-III: « plafonnés » — IRPP takes the real value, capped at 20% of the cash remuneration (limit 58161, ceiling account). CNPS, TFE and TAFP take the real value (Art. 189-2°, Art. 173). 58120 is the account the DAS report reads.

---

# 9148032 - TD BIK Vehicle — Capped Value for IRPP

## **Regulation Name: TD BIK Vehicle — Capped Value for IRPP**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148032

**Status:** active

**Processing Order (Ordinal):** 32

**1. Classification**

* **Tax Group:** Income Tax
* **Tax Rule Group:** retro_simple_tax
* **Taxation Type:** Flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** 

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 100.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  | 58162 | 58121 | 99999 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 65509 | 6550% | Yes |
| 65520 |  | Yes |

> CGI Art. 46-III: « plafonnés » — IRPP takes the real value, capped at 10% of the cash remuneration (limit 58162, ceiling account). CNPS, TFE and TAFP take the real value (Art. 189-2°, Art. 173). 58121 is the account the DAS report reads.

---

# 9148033 - TD BIK Food — Capped Value for IRPP

## **Regulation Name: TD BIK Food — Capped Value for IRPP**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148033

**Status:** active

**Processing Order (Ordinal):** 33

**1. Classification**

* **Tax Group:** Income Tax
* **Tax Rule Group:** retro_simple_tax
* **Taxation Type:** Flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** 

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 100.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  | 58163 | 58122 | 99999 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 65659 | 6565% | Yes |
| 65679 | 6567% | Yes |

> CGI Art. 46-III: « plafonnés » — IRPP takes the real value, capped at 15% of the cash remuneration and 75,000 XAF a month (limit 58163, ceiling account). CNPS, TFE and TAFP take the real value (Art. 189-2°, Art. 173). 58122 is the account the DAS report reads.

---

# 9148034 - TD BIK Interior Furnishings — Capped Value for IRPP

## **Regulation Name: TD BIK Interior Furnishings — Capped Value for IRPP**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148034

**Status:** active

**Processing Order (Ordinal):** 34

**1. Classification**

* **Tax Group:** Income Tax
* **Tax Rule Group:** retro_simple_tax
* **Taxation Type:** Flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** 

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 100.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  | 58164 | 58123 | 99999 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 65853 |  | Yes |

> CGI Art. 46-III: « plafonnés » — IRPP takes the real value, capped at 5% of the cash remuneration (limit 58164, ceiling account). CNPS, TFE and TAFP take the real value (Art. 189-2°, Art. 173). 58123 is the account the DAS report reads.

---

# 9148035 - TD BIK Domestic Help / Security — Capped Value for IRPP

## **Regulation Name: TD BIK Domestic Help / Security — Capped Value for IRPP**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148035

**Status:** active

**Processing Order (Ordinal):** 35

**1. Classification**

* **Tax Group:** Income Tax
* **Tax Rule Group:** retro_simple_tax
* **Taxation Type:** Flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** 

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 100.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  | 58165 | 58124 | 99999 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 65854 |  | Yes |

> CGI Art. 46-III: « plafonnés » — IRPP takes the real value, capped at 4% of the cash remuneration (limit 58165, ceiling account). CNPS, TFE and TAFP take the real value (Art. 189-2°, Art. 173). 58124 is the account the DAS report reads.

---

# 9148036 - TD BIK Electricity — Capped Value for IRPP

## **Regulation Name: TD BIK Electricity — Capped Value for IRPP**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148036

**Status:** active

**Processing Order (Ordinal):** 36

**1. Classification**

* **Tax Group:** Income Tax
* **Tax Rule Group:** retro_simple_tax
* **Taxation Type:** Flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** 

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 100.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  | 58166 | 58125 | 99999 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 65855 |  | Yes |

> CGI Art. 46-III: « plafonnés » — IRPP takes the real value, capped at 4% of the cash remuneration (limit 58166, ceiling account). CNPS, TFE and TAFP take the real value (Art. 189-2°, Art. 173). 58125 is the account the DAS report reads.

---

# 9148037 - TD BIK Water — Capped Value for IRPP

## **Regulation Name: TD BIK Water — Capped Value for IRPP**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148037

**Status:** active

**Processing Order (Ordinal):** 37

**1. Classification**

* **Tax Group:** Income Tax
* **Tax Rule Group:** retro_simple_tax
* **Taxation Type:** Flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** 

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 100.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  | 58167 | 58126 | 99999 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 65856 |  | Yes |

> CGI Art. 46-III: « plafonnés » — IRPP takes the real value, capped at 4% of the cash remuneration (limit 58167, ceiling account). CNPS, TFE and TAFP take the real value (Art. 189-2°, Art. 173). 58126 is the account the DAS report reads.

---

# 9148038 - TD BIK Telephone — Capped Value for IRPP

## **Regulation Name: TD BIK Telephone — Capped Value for IRPP**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148038

**Status:** active

**Processing Order (Ordinal):** 38

**1. Classification**

* **Tax Group:** Income Tax
* **Tax Rule Group:** retro_simple_tax
* **Taxation Type:** Flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** 

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 100.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  | 58168 | 58127 | 99999 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 65609 | 6560% | Yes |
| 65620 |  | Yes |

> CGI Art. 46-III: « plafonnés » — IRPP takes the real value, capped at 3% of the cash remuneration (limit 58168, ceiling account). CNPS, TFE and TAFP take the real value (Art. 189-2°, Art. 173). 58127 is the account the DAS report reads.

---

# 9148039 - TD BIK Gas — Capped Value for IRPP

## **Regulation Name: TD BIK Gas — Capped Value for IRPP**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148039

**Status:** active

**Processing Order (Ordinal):** 39

**1. Classification**

* **Tax Group:** Income Tax
* **Tax Rule Group:** retro_simple_tax
* **Taxation Type:** Flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** 

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 100.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  | 58169 | 58128 | 99999 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 65857 |  | Yes |

> CGI Art. 46-III: « plafonnés » — IRPP takes the real value, capped at 2% of the cash remuneration (limit 58169, ceiling account). CNPS, TFE and TAFP take the real value (Art. 189-2°, Art. 173). 58128 is the account the DAS report reads.

---

# 9148041 - TD IRPP Gross

## **Regulation Name: TD IRPP Gross**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148041

**Status:** active

**Processing Order (Ordinal):** 41

**1. Classification**

* **Tax Group:** Income Tax
* **Tax Rule Group:** simple_tax
* **Taxation Type:** Flat
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
| 62670 |  | Yes |
| 62680 |  | Yes |
| 65299 | 652%% | Yes |
| 65630 |  | Yes |
| 65809 | 6580% | No |
| 65899 | 658%% | Yes |

> Cash gross plus each benefit at its capped value. Benefit codes with no Art. 46 category enter at real value. v5: **6580x School Scholarship out** (CGI Art. 45-9°, « bourses d'enseignement ou de perfectionnement »; WTC V3.0) — it stays in the TFE/TAFP base (Art. 189-1°, Art. 173). 58008 is read by the DAS report.

---

# 9148051 - TD CNPS Gross

## **Regulation Name: TD CNPS Gross**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148051

**Status:** active

**Processing Order (Ordinal):** 51

**1. Classification**

* **Tax Group:** Social Security
* **Tax Rule Group:** simple_tax
* **Taxation Type:** Flat
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
| 62910 |  | No |
| 62920 |  | No |
| 62930 |  | No |
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
| 62639 | 6263% | Yes |
| 62650 |  | Yes |
| 62669 | 6266% | Yes |
| 62670 |  | Yes |
| 62680 |  | Yes |
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

> Base decided in round 2 (Dec. 1635/PR/PM/MFPT/2009 arts. 1–4, Dec. 1636/PR/PM/MFPT/2009 arts. 1–3, Dec. 1634/2009 (AT/MP; text not obtained, rate from the guide p. 8), effective date 2009-12-04 per the guide p. 8 (Journal Officiel not obtained); CNPS Guide de l'employeur 2019, p. 6–9 and 12): « salaires, gains, indemnités (à l'exception de celles ayant un caractère de remboursement de frais), primes, gratifications… et tous autres avantages versés… entre le premier et le dernier jour du mois » (guide p. 7) — benefits in kind at real value in (Dec. 1635 art. 3, « contre valeur des avantages en nature »); 6286x meal/food in; **6274x schooling allowance and 6580x scholarship in** (« tout autre avantage en espèce »). Out: family allowances 6275x/6276x/6278x (guide p. 8; Dec. 1635 art. 3), prime de panier / meal cash 6566x (guide p. 7), severance 6218x (« indemnités ayant un caractère de dédommagement », Dec. 1635 art. 3, Dec. 1636 art. 2), travel ticket, per diem, relocation 6254x–6257x, 6557x, 6558x and the 6287x function allowance (« indemnités de déplacement », reimbursement of expenses). **Transport 6251x / 6252x out in full** — technical decision of the Chade front (source: CNPS guide p. 8), pending the user’s ok (« Indemnité mensuelle de transport » among the exclusions); the decrees (Dec. 1635 art. 3, Dec. 1636 art. 2) exclude only expense reimbursements and « indemnités ayant un caractère de dédommagement » and do not name transport. The 30% limit is IRPP only. Would supersede `correcoes.md` 2026-07-07 ("excess subject to CNPS") once the user agrees. Uncapped; **58130 is the account the CNPS Récapitulatif reads**.

---

# 9148052 - TD CNPS Insurable Salary

## **Regulation Name: TD CNPS Insurable Salary**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148052

**Status:** active

**Processing Order (Ordinal):** 52

**1. Classification**

* **Tax Group:** Social Security
* **Tax Rule Group:** retro_simple_tax_period
* **Taxation Type:** Flat
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

> Floor 60,000 a month = SMIG 59,995 rounded (Dec. 1111/PR/PM/MFPT/2011; guide p. 7 and 9), applied **only in a month with pay** — the `GREATER($58130;0)` condition (guide p. 7: contributions on what is « versé… entre le premier et le dernier jour du mois »; with an empty matrix the engine would still apply the floor). Ceiling 500,000 a month, the same for the three branches (Dec. 1635 art. 4; Dec. 1636 art. 3), stated annually (6,000,000). The ceiling is **annual**: « l'employeur doit procéder à une régularisation… en fin d'année » (guide p. 12) — December regularisation not built as a regulation (A23). `_period` + 99998: report-feeding base (Appel Mensuel, DNTS, Récapitulatif).

---

# 9148053 - TD CNPS Contributions

## **Regulation Name: TD CNPS Contributions**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148053

**Status:** active

**Processing Order (Ordinal):** 53

**1. Classification**

* **Tax Group:** Social Security
* **Tax Rule Group:** simple_tax_$$_post_formula
* **Taxation Type:** Flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** 

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 3.500 |  |  |  |  | FLOOR(ADD($band_amount_raw;0.5)) | EQUALS($58202;1) | 01-01-2026 |  |  |  |  |  |  | 2610 | 2551 |
|  |  |  | 5.000 |  |  |  | FLOOR(ADD($band_amount_raw;0.5)) | EQUALS($58202;1) | 01-01-2026 |  |  |  |  |  |  | 6037 | 2537 |
|  |  |  | 7.500 |  |  |  | FLOOR(ADD($band_amount_raw;0.5)) | EQUALS($58203;1) | 01-01-2026 |  |  |  |  |  |  | 6020 | 2550 |
|  |  |  | 4.000 |  |  |  | FLOOR(ADD($band_amount_raw;0.5)) | EQUALS($58204;1) | 01-01-2026 |  |  |  |  |  |  | 6040 | 2560 |
|  |  | 3.500 |  |  |  |  | FLOOR(ADD($band_amount_raw;0.5)) | EQUALS($58202;1) | 01-01-2026 |  |  |  |  |  |  | 99999 | 58100 |
|  |  | 100.000 |  |  |  |  | 20 | GREATER($58550;0) | 01-01-2026 |  |  |  |  |  |  | 58131 | 99999 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 58550 |  | Yes |

> Rates from 2009-12-04: PVID 3.5% EE + 5% ER (Dec. 1636 art. 1), PFM 7.5% ER (Dec. 1635 arts. 1–2; 0.25% of it passed by the CNPS to ONAPE, no extra rate), AT/MP 4% ER, single rate (Dec. 1634/2009; guide p. 8); total 20%. Each band gated by its eligibility flag; **non-residents pay every branch** (flags default 1; guide p. 6). Accounts: **employee share → 2610 / 2551** (WTC V3.0: 2551 "TD CNPS Contribution EE"); **employer shares → 6037 / 2537, 6020 / 2550, 6040 / 2560** (WTC V3.0: 2537, 2550, 2560 "TD CNPS Contribution ER"). The Dev posts the 3.5% EE band to 6020/2550 and the 7.5% ER band to 2610/2551 — inverted; v5 keeps the v4 pairs. Band 5: negative copy of the EE share for the IRPP deduction (CGI Art. 47-I « retenues effectuées au titre de la sécurité sociale »). Band 6: total rate in 58131, only when there is an insurable salary (read by the Récapitulatif; WTC V3.0 names 58131 "TD CNPS Contribution EE" — rename requested, R27). `_$$`: the EE share is gross-up eligible.

---

# 9148061 - TD Supplementary Retirement — Deductible Portion

## **Regulation Name: TD Supplementary Retirement — Deductible Portion**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148061

**Status:** active

**Processing Order (Ordinal):** 61

**1. Classification**

* **Tax Group:** Income Tax
* **Tax Rule Group:** retro_simple_tax
* **Taxation Type:** Flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** 

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 100.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  | 58172 | 99999 | 58101 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 21610 |  | No |
| 21611 |  | No |
| 21670 |  | No |
| 21649 | 2164% | No |
| 21699 | 216%% | Yes |

> CGI Art. 47-I: employee retirement contributions deductible up to 3.5% of the appointments (58172, ceiling account); **Art. 47-II (v5): only if compulsory** (« doivent revêtir un caractère obligatoire »). 2164x is "Voluntary Contribution" in WTC V3.0 → **No**. Other 216xx = compulsory scheme codes (none in WTC V3.0 today: research gap R16). Negative in 58101.

---

# 9148071 - TD IRPP Taxable Income

## **Regulation Name: TD IRPP Taxable Income**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148071

**Status:** active

**Processing Order (Ordinal):** 71

**1. Classification**

* **Tax Group:** Income Tax
* **Tax Rule Group:** simple_tax
* **Taxation Type:** Flat
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

> IRPP gross less the Art. 45 exempt portions (transport 58104, family 58108, plan social 58113, function allowance / per diem 58114, leave ticket 58115), the EE CNPS share (58100) and the deductible compulsory retirement contribution (58101; WTC V3.0 names it "TD Voluntary Contribution" — rename requested, R27) — CGI Art. 47-I. **58552 is the account the IRPP-TS and DAS reports read**; it runs for every status except diplomatic, non-residents included.

---

# 9148072 - TD IRPP-TS — Progressive Scale

## **Regulation Name: TD IRPP-TS — Progressive Scale**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148072

**Status:** active

**Processing Order (Ordinal):** 72

**1. Classification**

* **Tax Group:** Income Tax
* **Tax Rule Group:** retro_simple_tax
* **Taxation Type:** Differential
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** AND(OR(LESS($58218;2);EQUALS($58218;3));NOT(EQUALS($58226;1)))

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.000 | 800,000.000 | 0.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  |  | 58112 | 99999 |
| 800,000.000 | 6,000,000.000 | 10.500 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  |  | 58112 | 99999 |
| 6,000,000.000 | 7,500,000.000 | 15.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  |  | 58112 | 99999 |
| 7,500,000.000 | 9,000,000.000 | 20.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  |  | 58112 | 99999 |
| 9,000,000.000 | 12,000,000.000 | 25.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  |  | 58112 | 99999 |
| 12,000,000.000 | 9,999,999,999,999.000 | 30.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  |  | 58112 | 99999 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 58552 |  | Yes |

> CGI Art. 1-IV (CGI 2026 p. 14; LF 2026 Art. 3): « 0 et 800 000 0% … Plus de 12 000 000 30% », annual bands auto-divided by the period; last band closed. Round 3: limits written at the round figure (incomeTo 800,000 = incomeFrom of the next band), so the tax starts at the 800,001st franc as the table says (the `x.99` limits of v4 and the Dev taxed 0.99 XAF a year less and gave 1 XAF less at a half franc). Annualisation: each month × 12 — irregular payments see ASSUMPTIONS A26. Runs for residents (58218 = 0), **non-residents (58218 = 1, round 2)** and young graduates (3), except the Art. 3-4° exempt (58226 = 1: real-regime entity, start date given and ≤ 60 months, under 35 at recruitment, young graduate or worker). Disabled (Art. 45-18°) and diplomatic (Art. 3-2°) do not run it. Non-resident (decided 1 Nov): the salary of a non-domiciled employee working in Chad for an employer established in Chad is Art. 44 income (Art. 44-II-2°, p. 29), withheld on the scale (Art. 847, p. 168) with the Art. 45 exemptions, Art. 46 caps and Art. 47 deductions; the 18% of Art. 116 (p. 43) covers only Art. 2-VI (royalties, BNC of Art. 49) and Art. 60 (artists).

---

# 9148073 - TD IRPP-TS — Resident Withholding

## **Regulation Name: TD IRPP-TS — Resident Withholding**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148073

**Status:** active

**Processing Order (Ordinal):** 73

**1. Classification**

* **Tax Group:** Income Tax
* **Tax Rule Group:** simple_tax_$$_post_formula
* **Taxation Type:** Flat
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

> Rounded once, on the total, to the whole XAF — **technical convention, no rule in the CGI** (no IRPP rounding rule in the CGI 2026; Art. 847 refers to a DGI barème not obtained; XAF has no subunit). `_$$`: gross-up eligible. 2552 read by IRPP-TS and DAS.

---

# 9148074 - TD Non-Resident Tax Base

## **Regulation Name: TD Non-Resident Tax Base**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148074

**Status:** active

**Processing Order (Ordinal):** 74

**1. Classification**

* **Tax Group:** Income Tax
* **Tax Rule Group:** simple_tax_period
* **Taxation Type:** Flat
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

> Round 2: copy of the non-resident's taxable income 58552 (same base as residents) into 58592, kept only because the IRPP-TS report reads 58592 for non-residents. Report-feeding base (`_period`, 99998).

---

# 9148075 - TD IRPP-TS — Non-Resident Withholding (scale)

## **Regulation Name: TD IRPP-TS — Non-Resident Withholding (scale)**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148075

**Status:** active

**Processing Order (Ordinal):** 75

**1. Classification**

* **Tax Group:** Income Tax
* **Tax Rule Group:** simple_tax_$$_post_formula
* **Taxation Type:** Flat
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

> Round 2: **progressive scale, not 18%** — the 9148072 result for a non-resident, posted to 2592 so the IRPP-TS report keeps residents (2552) and non-residents (2592) apart. Same rounding convention as 9148073. `_$$`: gross-up eligible.

---

# 9148081 - TD TFE Base

## **Regulation Name: TD TFE Base**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148081

**Status:** active

**Processing Order (Ordinal):** 81

**1. Classification**

* **Tax Group:** Income Tax
* **Tax Rule Group:** simple_tax_period
* **Taxation Type:** Flat
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
| 62180 |  | No |
| 62181 |  | No |
| 62182 |  | No |
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
| 62639 | 6263% | Yes |
| 62650 |  | Yes |
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
| 65610 |  | No |
| 65611 |  | No |
| 65612 |  | No |
| 65660 |  | No |
| 65661 |  | No |
| 65662 |  | No |
| 62670 |  | Yes |
| 62680 |  | Yes |
| 65299 | 652%% | Yes |
| 65499 | 654%% | Yes |
| 65509 | 6550% | Yes |
| 65520 |  | Yes |
| 65699 | 656%% | Yes |
| 65899 | 658%% | Yes |

> CGI Art. 189: gross salaries, « indemnités diverses, allocations, gratifications », and benefits « pour leur montant réel ». No Art. 45 carve-out (exempt transport, family allowances, scholarships, leave ticket 6255x and per diem 62570 / 6557x / 6558x stay in — round 2; reimbursements with receipts, 6256x, out). v5: **non-residents in** (Art. 187: tax on the payer, no residence condition) — only diplomatic (4) and the Art. 188-10° exempt share (58219 = 1: real-regime entity paying a disabled person, or a young graduate or worker under 35) are out. Severance 6218x out as in v4 (see ASSUMPTIONS A20). Round 3: pensions 6264x in (Arts. 187, 189-1° « pensions »). TFE report reads 58563.

---

# 9148082 - TD TAFP Base

## **Regulation Name: TD TAFP Base**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148082

**Status:** active

**Processing Order (Ordinal):** 82

**1. Classification**

* **Tax Group:** Income Tax
* **Tax Rule Group:** simple_tax_post_formula_period
* **Taxation Type:** Flat
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
| 62180 |  | No |
| 62181 |  | No |
| 62182 |  | No |
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
| 62639 | 6263% | Yes |
| 62650 |  | Yes |
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
| 65610 |  | No |
| 65611 |  | No |
| 65612 |  | No |
| 65660 |  | No |
| 65661 |  | No |
| 65662 |  | No |
| 62670 |  | Yes |
| 62680 |  | Yes |
| 65299 | 652%% | Yes |
| 65499 | 654%% | Yes |
| 65509 | 6550% | Yes |
| 65520 |  | Yes |
| 65699 | 656%% | Yes |
| 65899 | 658%% | Yes |
| 62229 | 6222% | No |

> CGI Art. 173: « montant brut des appointements, salaires, avantages en nature et rétributions quelconques, **y compris les gratifications servies régulièrement** ». Round 3: own matrix — TFE base less one-time / discretionary bonuses 6222x (a contrario, not regular; WTC V3.0 Apprenticeship No) and less pensions 6264x (not in Art. 173). Annual bonus 6220x treated as regular (A30). v5: non-residents in (Art. 173: paid by the enterprise, no residence condition); Art. 174-3° exempt share out (58219). Fraction up to 1,000 XAF dropped (Art. 177) — per employee here, while Art. 177 speaks of the « montant global » (A31). TAFP report reads 58534.

---

# 9148083 - TD TFE — Employer Lump-Sum Tax

## **Regulation Name: TD TFE — Employer Lump-Sum Tax**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148083

**Status:** active

**Processing Order (Ordinal):** 83

**1. Classification**

* **Tax Group:** Income Tax
* **Tax Rule Group:** simple_tax_post_formula
* **Taxation Type:** Flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** 

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | 7.500 |  |  |  | FLOOR(ADD(MULTIPLY($band_amount_raw;IF(EQUALS($58206;1);0;IF(EQUALS($58206;2);0.5;1)));0.5)) |  | 01-01-2026 |  |  |  |  |  |  | 6063 | 2563 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 58563 |  | Yes |

> CGI Art. 190: « 7,5 % du montant brut des sommes imposables ». Art. 190 has no rounding rule (only the TAFP has one, Art. 177); round 3: the amount is **paid to the whole franc — technical payment convention, FLOOR(x+0.5), not a statutory rounding** (XAF has no subunit), the same convention as the IRPP. Reduced by 50% (Art. 158) or exempt (LF 2020 Art. 14) per entity flag 58206.

---

# 9148084 - TD TAFP — Apprenticeship & Training Tax

## **Regulation Name: TD TAFP — Apprenticeship & Training Tax**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148084

**Status:** active

**Processing Order (Ordinal):** 84

**1. Classification**

* **Tax Group:** Income Tax
* **Tax Rule Group:** simple_tax_post_formula
* **Taxation Type:** Flat
* **Currency:** XAF

**2. Execution Conditions (Assertions)**

* **Pre-condition:** 

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | 1.200 |  |  |  | MULTIPLY(FLOOR(DIVIDE(ADD(MULTIPLY($band_amount_raw;IF(EQUALS($58206;1);0;IF(EQUALS($58206;2);0.5;1)));5);10));10) |  | 01-01-2026 |  |  |  |  |  |  | 6034 | 2534 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 58534 |  | Yes |

> CGI Art. 178, 12‰; Art. 177: « arrondi à la dizaine de Francs la plus voisine ». Same relief as TFE (58206; Art. 158 « 50% de la taxe d'apprentissage »).

---

# 9148091 - TD PSA — Food Security Levy

## **Regulation Name: TD PSA — Food Security Levy**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148091

**Status:** active

**Processing Order (Ordinal):** 91

**1. Classification**

* **Tax Group:** Income Tax
* **Tax Rule Group:** simple_tax_$$_monthly
* **Taxation Type:** Flat
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

> v5, new. CGI Arts. 837–839 (LF 2024 Art. 21; CGI 2026 p. 166): « dû par les employés du secteur public, du secteur formel privé… » · « établi, recouvré… comme en matière d'impôt sur le revenu des personnes physiques » · « fixé à 400 FCFA/mois et par employé ». Employee deduction, 400 XAF a month (Floor = Ceiling, `_monthly`), every status except diplomatic, only in a month with cash pay. Liability 2570 — **new WTC code needed** (research gap R17); reported with the IRPP. `_$$`: employee withholding, gross-up eligible as the IRPP.

---
