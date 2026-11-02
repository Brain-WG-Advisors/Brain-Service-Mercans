---
name: "chad-design-blueprint-claude-v4"
description: "Chad (TD) payroll regulation design v4 — built by Claude from CCG v1.2, WTC v1.2 (compliance sheet), DD v1.0 and the 7 report specs, applying KB_Design_Rulebook_v4 and the answers of the 16 Oct 2026 design call. Design Blueprint format, tax year td_2026."
---

> **Analysis instructions:** read and follow `Regulation_Design_Analysis_Engine.md` before interpreting or computing any regulation below.

> **Companions:** `CHANGELOG.md` — what changed from v3 and which rule drove it · `ASSUMPTIONS.md` — what is still not settled · `RESEARCH_GAPS.md` — what compliance must fix · `VALIDATION.md` — the scenarios executed.

# 0 - Flags

| Account | Flag | Formula | Values |
| --- | --- | --- | --- |
| 58218 | Status (global flag) | `IF(EQUALS($hr.residency_status::key;'NRES');1;IF(EQUALS($hr.residency_status::key;'DISABLED');2;IF(EQUALS($hr.residency_status::key;'YOUNG-GRAD');3;IF(EQUALS($hr.residency_status::key;'DIPLO');4;0))))` | 0 resident · 1 non-resident · 2 disabled · 3 young graduate · 4 diplomatic — catalogue numbering; routing uses `LESS($58218;1)` for residents, never an equality test against zero |
| 58202 | CNPS PVID eligible | `IF(EQUALS($hr.cnps_eligibility_pvid::key;'Y');1;2)` | 1 yes · 2 no |
| 58203 | CNPS PFM eligible | `IF(EQUALS($hr.cnps_eligibility_pfm::key;'Y');1;2)` | 1 yes · 2 no |
| 58204 | CNPS AT/MP eligible | `IF(EQUALS($hr.cnps_eligibility_atmp::key;'Y');1;2)` | 1 yes · 2 no |
| 58205 | Young-graduate months consumed | `ADD(FLOOR(DIVIDE(DAYS_BETWEEN($hr.young_graduate_employee_exemption_start_date;$period.end_date);30.4375));1)` | months since the exemption start, current month included; exemption while ≤ 60 (read by the IRPP-TS report) |
| 58206 | TFE / TAFP relief (entity) | `IF(EQUALS($legal_entity_hr.tfe_tafp_relief::key;'100');1;IF(EQUALS($legal_entity_hr.tfe_tafp_relief::key;'50');2;0))` | 0 none · 1 exempt (new companies, LF 2024) · 2 50% (CGI Art. 158) — **entity field** |
| 58207 | Transport allowance granted to all staff | `IF(EQUALS($legal_entity_hr.transport_uniform::key;'Y');1;2)` | 1 yes · 2 no — **new entity field**, default 1 |
| 58210 | Plan social (collective redundancy) | `IF(EQUALS($hr.termination_plan_social::key;'Y');1;2)` | 1 yes · 2 no — **new DD field** |
| 58212 | Dependent children | `$hr.number_of_dependent_children` | count — reporting only (DAS) |

Flags take the meaning the global catalogue gives them: 58218 status, 58205 young-graduate months, 58206 TFE relief, 58212 dependants. 58201 is reserved for advanced reconciliation and is not used.

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
| 62550 |  | No |
| 62551 |  | No |
| 62552 |  | No |
| 62560 |  | No |
| 62561 |  | No |
| 62562 |  | No |
| 62563 |  | No |
| 62570 |  | No |
| 62199 | 621%% | Yes |
| 62299 | 622%% | Yes |
| 62399 | 623%% | Yes |
| 62499 | 624%% | Yes |
| 62599 | 625%% | Yes |
| 62639 | 6263% | Yes |
| 62650 |  | Yes |
| 62669 | 6266% | Yes |
| 62799 | 627%% | Yes |
| 62867 |  | Yes |
| 62879 | 6287% | Yes |
| 62889 | 6288% | Yes |
| 62890 |  | Yes |
| 62999 | 629%% | Yes |
| 65519 | 6551% | Yes |
| 65619 | 6561% | Yes |
| 65669 | 6566% | Yes |
| 65799 | 657%% | Yes |
| 79499 | 794%% | Yes |

> Cash earnings subject to IRPP (Art. 44); base of the Art. 46 limits. **58105 is the account the DAS report reads** (gross vs the 58106 limit).

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

> Fixed 60,000 XAF a month (Floor = Ceiling, `_monthly`), written only when the employee has cash gross. Read by the DAS report to split employees above / at or below 60,000 XAF.

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
|  |  | 30.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  |  | 58171 | 99999 |
|  |  | 3.500 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  |  | 58172 | 99999 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 58109 |  | Yes |

> Derived limits in their own regulation, applied downstream as ceiling accounts (rulebook §5 · reunião 16/10, Suman): 58171 = 30% of base salary (Art. 45-13°, transport) · 58172 = 3.5% of base salary (Art. 47, retirement). One regulation: same base, two bands.

---

# 9148015 - TD Limits on Cash Remuneration — Benefits in Kind

## **Regulation Name: TD Limits on Cash Remuneration — Benefits in Kind**

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

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 58105 |  | Yes |

> Art. 46-III (LF 2019) caps, one band per benefit, all on the cash remuneration 58105: housing 20 · vehicle 10 · food 15 (and 75,000 XAF a month, stated annually as the band ceiling) · furnishings 5 · domestic 4 · electricity 4 · water 4 · telephone 3 · gas 2. Read as ceiling accounts by 9148031–9148039.

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
|  |  | 100.000 |  |  |  |  |  | EQUALS($58207;1) | 01-01-2026 |  |  |  |  |  | 58171 | 99999 | 58104 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 62529 | 6252% | Yes |

> Art. 45-13°: exempt up to 30% of base salary when granted to all staff (58207). Limit from 58171 as the ceiling account. Credit side → 58104 negative; subtracts in the taxable and CNPS bases (not in TFE/TAFP, Art. 189). 58104 is read by the DAS report.

---

# 9148022 - TD Family Allowance — Exempt

## **Regulation Name: TD Family Allowance — Exempt**

**System Tax Years:** td_2026

**System Reporting Periods:**

**Regulation ID:** 9148022

**Status:** active

**Processing Order (Ordinal):** 22

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
|  |  | 100.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  |  | 99999 | 58108 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 62759 | 6275% | Yes |
| 62769 | 6276% | Yes |

> CGI Art. 45: family allowances exempt from IRPP in full; no per-child cap in Chadian law (the 5,000 XAF wording is the Congo-Brazzaville CGI, Art. 38-2°). Negative in 58108, read by the DAS report.

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

> Art. 45-10°: severance under a collective-redundancy plan is fully exempt. Individual severance stays taxable. Negative in 58113.

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

> CGI Art. 46-III (LF 2019): « plafonnés » — IRPP takes the real value, capped at 20% of the cash remuneration (limit 58161, ceiling account). CNPS, TFE and TAFP take the real value. 58120 is the account the DAS report reads.

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

> CGI Art. 46-III (LF 2019): « plafonnés » — IRPP takes the real value, capped at 10% of the cash remuneration (limit 58162, ceiling account). CNPS, TFE and TAFP take the real value. 58121 is the account the DAS report reads.

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

> CGI Art. 46-III (LF 2019): « plafonnés » — IRPP takes the real value, capped at 15% of the cash remuneration and 75,000 XAF a month (limit 58163, ceiling account). CNPS, TFE and TAFP take the real value. 58122 is the account the DAS report reads.

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

> CGI Art. 46-III (LF 2019): « plafonnés » — IRPP takes the real value, capped at 5% of the cash remuneration (limit 58164, ceiling account). CNPS, TFE and TAFP take the real value. 58123 is the account the DAS report reads.

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

> CGI Art. 46-III (LF 2019): « plafonnés » — IRPP takes the real value, capped at 4% of the cash remuneration (limit 58165, ceiling account). CNPS, TFE and TAFP take the real value. 58124 is the account the DAS report reads.

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

> CGI Art. 46-III (LF 2019): « plafonnés » — IRPP takes the real value, capped at 4% of the cash remuneration (limit 58166, ceiling account). CNPS, TFE and TAFP take the real value. 58125 is the account the DAS report reads.

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

> CGI Art. 46-III (LF 2019): « plafonnés » — IRPP takes the real value, capped at 4% of the cash remuneration (limit 58167, ceiling account). CNPS, TFE and TAFP take the real value. 58126 is the account the DAS report reads.

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

> CGI Art. 46-III (LF 2019): « plafonnés » — IRPP takes the real value, capped at 3% of the cash remuneration (limit 58168, ceiling account). CNPS, TFE and TAFP take the real value. 58127 is the account the DAS report reads.

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

> CGI Art. 46-III (LF 2019): « plafonnés » — IRPP takes the real value, capped at 2% of the cash remuneration (limit 58169, ceiling account). CNPS, TFE and TAFP take the real value. 58128 is the account the DAS report reads.

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
| 65899 | 658%% | Yes |

> Cash gross plus each benefit at its capped value. Benefit codes with no Art. 46 category enter at real value. 58008 is read by the DAS report.

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
| 62760 |  | No |
| 62762 |  | No |
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
| 62879 | 6287% | Yes |
| 62890 |  | Yes |
| 62999 | 629%% | Yes |
| 65299 | 652%% | Yes |
| 65499 | 654%% | Yes |
| 65599 | 655%% | Yes |
| 65699 | 656%% | Yes |
| 65799 | 657%% | Yes |
| 65899 | 658%% | Yes |
| 79499 | 794%% | Yes |
| 58104 |  | Yes |

> Art. 7 CNPS guide: salaries, indemnities, bonuses and benefits at REAL value; exempt transport (58104) out. Rupture indemnities, family allowance, prime de panier and statutory EOS gratuity outside (WTC). Uncapped; **58130 is the account the CNPS Récapitulatif reads** (months worked, cumulative salary).

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

> Floor 60,000 / ceiling 500,000 a month, stated annually. Confirmed on 16/10 (Suman): with an empty matrix the floor still applies, so the `GREATER($58130;0)` condition is what keeps a month with no salary out. `_period` + 99998: report-feeding base (Appel Mensuel, DNTS, Récapitulatif).

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
|  |  | 3.500 |  |  |  |  | FLOOR(ADD($band_amount_raw;0.5)) | EQUALS($58202;1) | 01-01-2026 |  |  |  |  |  |  | 99999 | 58141 |
|  |  | 100.000 |  |  |  |  | 20 |  | 01-01-2026 |  |  |  |  |  |  | 58131 | 99999 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 58550 |  | Yes |

> One regulation, one base, all branches as bands (rulebook §5). PVID 3.5% EE + 5% ER, PFM 7.5%, AT/MP 4%, each gated by its eligibility flag. Band 5: negative copy of the EE share for the IRPP deduction. Band 6: total rate 20 in 58131, read by the CNPS Récapitulatif (expected annual contribution) — the report percentages live in the design (Mohit, 16/10). `_$$`: the EE share is gross-up eligible (Suman, 16/10). GL pairs: EE 2551 / ER 2550 coherent pair as on 16/10; the report specs map them the other way round (research gap R13).

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
|  |  | 100.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  | 58172 | 99999 | 58142 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 21610 |  | No |
| 21611 |  | No |
| 21670 |  | No |
| 21699 | 216%% | Yes |

> Art. 47 CGI: compulsory employee retirement contributions deductible up to 3.5% of base salary — limit 58172 as the ceiling account. Negative in 58142.

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
| 58141 |  | Yes |
| 58142 |  | Yes |

> IRPP gross less the exempt portions, the EE CNPS share and the deductible retirement contribution — negatives summed in the matrix (Art. 47). **58552 is the account the IRPP-TS and DAS reports read** (residents, young graduates and disabled alike), so it runs for every status except diplomatic.

---

# 9148072 - TD IRPP-TS — Resident Scale

## **Regulation Name: TD IRPP-TS — Resident Scale**

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

* **Pre-condition:** OR(LESS($58218;1);AND(EQUALS($58218;3);GREATER($58205;60)))

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.000 | 800,000.990 | 0.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  |  | 58152 | 99999 |
| 800,001.000 | 6,000,000.990 | 10.500 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  |  | 58152 | 99999 |
| 6,000,001.000 | 7,500,000.990 | 15.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  |  | 58152 | 99999 |
| 7,500,001.000 | 9,000,000.990 | 20.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  |  | 58152 | 99999 |
| 9,000,001.000 | 12,000,000.990 | 25.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  |  | 58152 | 99999 |
| 12,000,001.000 | 9,999,999,999,999.000 | 30.000 |  |  |  |  |  |  | 01-01-2026 |  |  |  |  |  |  | 58152 | 99999 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 58552 |  | Yes |

> Art. 1-IV CGI, annual bands auto-divided by the period; last band closed (Suman, 16/10: an open last band takes nothing). Resident (58218 = 0), or young graduate past 60 months (58205 > 60).

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

* **Pre-condition:** OR(LESS($58218;1);AND(EQUALS($58218;3);GREATER($58205;60)))

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 100.000 |  |  |  |  | FLOOR(ADD($band_amount_raw;0.5)) |  | 01-01-2026 |  |  |  |  |  |  | 2610 | 2552 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 58152 |  | Yes |

> Rounded once, on the total, to the whole XAF. `_$$`: gross-up eligible (Suman, 16/10). 2552 read by IRPP-TS and DAS.

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
| 58105 |  | Yes |
| 58104 |  | Yes |
| 58108 |  | Yes |
| 58113 |  | Yes |

> Art. 116: 18% on the remuneration paid, net of the amounts Art. 45 exempts. Report-feeding base (IRPP-TS reads 58592).

---

# 9148075 - TD IRPP — Non-Resident 18%

## **Regulation Name: TD IRPP — Non-Resident 18%**

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

* **Pre-condition:** EQUALS($58218;1)

**3. Calculation Logic (Bands)**

| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 18.000 |  |  |  |  | FLOOR(ADD($band_amount_raw;0.5)) |  | 01-01-2026 |  |  |  |  |  |  | 2610 | 2592 |

**4. Taxability Rules (Applicable Accounts)**

| Account | Pattern | Is Taxable? |
| --- | --- | --- |
| 58592 |  | Yes |

> Flat 18%, final. `_$$` as for residents. Disabled (2), young graduate within 60 months (3) and diplomatic (4) run neither 9148073 nor 9148075; CNPS still applies to 2 and 3.

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

* **Pre-condition:** AND(NOT(EQUALS($58218;1));NOT(EQUALS($58218;4)))

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
| 62550 |  | No |
| 62551 |  | No |
| 62552 |  | No |
| 62560 |  | No |
| 62561 |  | No |
| 62562 |  | No |
| 62563 |  | No |
| 62570 |  | No |
| 62199 | 621%% | Yes |
| 62299 | 622%% | Yes |
| 62399 | 623%% | Yes |
| 62499 | 624%% | Yes |
| 62599 | 625%% | Yes |
| 62639 | 6263% | Yes |
| 62650 |  | Yes |
| 62669 | 6266% | Yes |
| 62799 | 627%% | Yes |
| 62867 |  | Yes |
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

> Art. 189: gross salaries, indemnities, allowances and gratifications, and benefits at REAL value. No Art. 45 carve-out: exempt transport and family allowances stay in. Severance (damages in nature) out. TFE report reads 58563.

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

* **Pre-condition:** AND(NOT(EQUALS($58218;1));NOT(EQUALS($58218;4)))

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
| 62550 |  | No |
| 62551 |  | No |
| 62552 |  | No |
| 62560 |  | No |
| 62561 |  | No |
| 62562 |  | No |
| 62563 |  | No |
| 62570 |  | No |
| 62199 | 621%% | Yes |
| 62299 | 622%% | Yes |
| 62399 | 623%% | Yes |
| 62499 | 624%% | Yes |
| 62599 | 625%% | Yes |
| 62639 | 6263% | Yes |
| 62650 |  | Yes |
| 62669 | 6266% | Yes |
| 62799 | 627%% | Yes |
| 62867 |  | Yes |
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

> Same base as TFE (Art. 173, Art. 189). Fraction below 1,000 XAF dropped (CCG, Art. 177). TAFP report reads 58534.

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

> Art. 190, 7.5%. Reduced by 50% (CGI Art. 158) or exempt (LF 2024) per entity flag 58206.

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

> Art. 178, 12‰, rounded to the nearest 10 XAF. Same relief as TFE (58206).

---
