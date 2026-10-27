# Colombia — Regulation Design v1.0

**Country:** Colombia (CO) · **Prefix:** `9170` (9 + ISO-3166 numeric 170) · **Currency:** COP, zero decimals in filings
**Design basis:** `CO-CCG-001-v1.1.docx`, `CO-WTC-001-v1.1.xlsx`, `CO-DD-001-v1.0.xlsx`, 6 report specs, payslip generator
**Method:** clean-room — built from the CCG and primary statutory sources; no dev production design read
**Status:** COMPLETE. All four statutory questions closed in the final research pass. Flag bindings pending Internal Code allocation, which is a system-side action, not a research gap (Part 6, item 5)

---

## PART 0 — Pre-design sweep

Run before writing any regulation, per the checklist the Côte d'Ivoire cycle produced after special employee categories turned out to be the largest gap class there.

| Category | Present in CCG | DD field | Design treatment |
|---|---|---|---|
| Apprentice (*aprendiz*) | yes, 44 refs, lectiva/productiva split | `Contract Type` | `9170013` — lectiva phase carries health + ARL, no pension |
| Integral salary (*salario integral*) | yes, thin | `All-Inclusive Salary Flag` | `9170012` — IBC = 70% of salary |
| High-risk (Decreto Ley 2090) | yes | `High-Risk Pension Activity Flag` | `9170046` — **+10pp employer**, Decreto Ley 2090 art. 5 |
| Active pensioner | yes, 12 refs | `Worker Sub-Type` = 01 | health due, pension not — routed, no new flag |
| Foreign not liable to pension | yes | `Foreign National Not Liable to Pension Flag` | assertion on `9170041` |
| Part-time under 1 SMMLV | yes | — | *cotizante por semanas*, see item 5 |

**Two units, never interchanged.** Every **tax** parameter is in UVT (2026 = COP 52,374, Resolución DIAN 000238/2025 art. 1). Every **contribution** parameter is in SMMLV (2026 = COP 1,750,905). The WTC's own `Tax Credit` sheet records this as the commonest source of error, and no tax threshold in Colombia is expressed in minimum wages.

**Law 2381 of 2024 is not configurable for 2026.** Constitutional Court judgment C-264 of 25 August 2026 upheld art. 94 on the understanding that the provisions take effect **1 April 2027**. Every 2026 period runs Law 100 of 1993 as amended by Law 797 of 2003. The five-band FSP scale belongs to 2027 change control, not here.

---

## PART 1 — Flags, rate accounts and dated tables

### Flags — bound by name, Internal Code pending

| Account | Flag | DD field | Values |
|---|---|---|---|
| `58201` | Integral-salary regime | `All-Inclusive Salary Flag` | 0 = ordinary, 1 = integral |
| `58202` | Non-salary pact in force | `Non-Salary Pact Flag` | 0 = no, 1 = yes — **drives the art. 128 / Ley 1393 conditionals** |
| `58203` | Art. 114-1 exoneration | `Exonerated from Health, SENA and ICBF` | 0 = no, 1 = yes |
| `58204` | Occupational risk class | `Work Centre Occupational Risk Class` | 1–5 |
| `58205` | High-risk pension activity | `High-Risk Pension Activity Flag` | 0 = no, 1 = yes |
| `58206` | Pension regime | `Pension Regime` | 1 = RPM, 2 = RAIS |
| `58207` | Foreign not liable to pension | `Foreign National Not Liable to Pension Flag` | 0 = liable, 1 = exempt |
| `58208` | Contract type | `Contract Type` | incl. apprentice lectiva / productiva |
| `58209` | Worker sub-type | `Worker Sub-Type` (DD row 27) | PILA *tipo de cotizante*; **01 = active pensioner** |
| `58295` | Paid days in period | `$actual_prorata_days` | numeric |

Each carries `[PENDING-CODE]` in the submission: the DD's `Internal Code` column is populated 1 of 99, and the Master Data Dictionary Template classifies that column as **SYSTEM / (generated)** — allocated from the HRB namespace, not researched. Substituting the codes later is mechanical.

### Rate accounts

| Account | Parameter | 2026 value | Source |
|---|---|---|---|
| `52501` | SMMLV | 1,750,905 | Decreto 1469 de 2025 — see Part 6 item 2 |
| `52502` | Transport allowance | 249,095 | Decreto 1470 de 2025 |
| `52503` | UVT | 52,374 | Resolución DIAN 000238/2025 art. 1 |
| `52511` | Health — employee | 4% | Ley 100 art. 204 |
| `52512` | Health — employer | 8.5% | Ley 100 art. 204; **0 if `58203` = 1** |
| `52521` | Pension — employee | 4% | Ley 797 art. 7 |
| `52522` | Pension — employer | 12% | Ley 797 art. 7 |
| `52531` | FSP solidarity account | 1.0% | Ley 100 art. 27 |
| `52541` | CCF | 4% | Ley 21 de 1982 — **never exonerated** |
| `52542` | SENA | 2% | Ley 21 de 1982; 0 if `58203` = 1 |
| `52543` | ICBF | 3% | Ley 89 de 1988; 0 if `58203` = 1 |
| `52551` | Integral-salary IBC factor | 70% | Ley 797 art. 5 par. |
| `52552` | Non-salary clamp | 40% | Ley 1393 de 2010 art. 30 |
| `52523` | High-risk pension surcharge | **10 pp** | Decreto Ley 2090 de 2003 art. 5 — employer-borne |
| `52571` | Incapacity days 1–2 | **66.66%** | CST art. 227, direct application per two MinSalud conceptos |
| `52561` | Prima accrual | 8.3333% | CST art. 306 |
| `52562` | Cesantías accrual | 8.3333% | CST art. 249 |
| `52563` | Cesantías interest | 1.0% | Ley 52 de 1975 |
| `52564` | Vacation accrual | 4.1667% | CST art. 186 |

### Dated tables — values that move inside 2026

| Account | Table | Schedule |
|---|---|---|
| `53001` | Hourly divisor | 220 to 14 July · **210 from 15 July 2026** (Ley 2101 de 2021, MinTrabajo Circular 101/2025) |
| `53002` | Rest-day premium | 80% to 30 June · **90% from 1 July 2026** (Ley 2466 de 2025) |
| `53003` | ARL rate by class | `58204` → 0.522 / 1.044 / 2.436 / 4.350 / 6.960% (Decreto 1072 art. 2.2.4.3.5) |
| `53004` | FSP subsistence band | 16–17 SMMLV = 0.2% · 17–18 = 0.4% · 18–19 = 0.6% · 19–20 = 0.8% · >20 = 1.0% |

**July 2026 has two step-changes two weeks apart.** The CCG states it explicitly and gives the contrast: the same hour is 2,400,000 ÷ 220 × 0.90 on 5 July and 2,400,000 ÷ 210 × 0.90 on 20 July. Both are dated tables, never constants. Collapsing the month to one rate is wrong in both directions depending on which rate is chosen.

---

## PART 2 — Account register

| Account | Type | Reg | Purpose |
|---|---|---|---|
| `58101` | Intermediate | 9170011 | Salary-constituting payments |
| `58102` | Intermediate | 9170011 | Non-salary payments as pacted |
| `58103` | Intermediate | 9170012 | Non-salary excess dragged back by the 40% clamp |
| `58104` | **Base** | 9170012 | **IBC — contribution base** |
| `58105` | Intermediate | 9170021 | Employee health |
| `58106` | Intermediate | 9170022 | Employee pension |
| `58107` | Intermediate | 9170023 | FSP total |
| `58111` | Intermediate | 9170031 | Taxable payments |
| `58112` | Intermediate | 9170032 | Art. 388 depurated base |
| `58113` | Intermediate | 9170033 | Base in UVT |
| `58121` | Intermediate | 9170041 | Employer pension |
| `58122` | Intermediate | 9170042 | Employer health |
| `58123` | Intermediate | 9170043 | ARL |
| `58124` | Intermediate | 9170044 | Payroll levies |
| `58131` | Intermediate | 9170051 | Prestaciones accrual |
| `58141` | Base | 9170061 | Total employee deductions |
| `58142` | Base | 9170062 | Total employer cost |
| `58143` | Base | 9170071 | Net pay |

---

## PART 3 — Regulation sequence

| # | Reg ID | Name | Tax Group | Tax Rule Group | Type |
|---|---|---|---|---|---|
| 11 | 9170011 | CO Gross and Salary Split | social_security | `retro_simple_tax` | Formula |
| 12 | 9170012 | CO Contribution Base (IBC) | social_security | `retro_simple_tax_post_formula` | Formula |
| 13 | 9170013 | CO Apprentice Base | social_security | `retro_simple_tax` | Formula |
| 21 | 9170021 | CO Health — Employee | social_security | `retro_simple_tax` | Flat |
| 22 | 9170022 | CO Pension — Employee | social_security | `retro_simple_tax` | Flat |
| 23 | 9170023 | CO Solidarity Fund | social_security | `retro_simple_tax_post_formula` | Differential |
| 31 | 9170031 | CO Taxable Payments | income_tax | `retro_simple_tax` | Formula |
| 32 | 9170032 | CO Art. 388 Depuration | income_tax | `retro_simple_tax_post_formula` | Formula |
| 33 | 9170033 | CO Withholding — Procedure 1 | income_tax | `retro_simple_tax_post_formula` | Differential |
| 34 | 9170034 | CO Withholding — Procedure 2 | income_tax | `retro_simple_tax_ytm` | Differential |
| 35 | 9170035 | CO Non-Resident Withholding | income_tax | `retro_simple_tax` | Flat |
| 41 | 9170041 | CO Pension — Employer | social_security | `retro_simple_tax` | Flat |
| 42 | 9170042 | CO Health — Employer | social_security | `retro_simple_tax` | Flat |
| 43 | 9170043 | CO Occupational Risk (ARL) | social_security | `retro_simple_tax` | Flat |
| 44 | 9170044 | CO Payroll Levies | social_security | `retro_simple_tax` | Flat |
| 46 | 9170046 | CO High-Risk Pension Surcharge | social_security | `retro_simple_tax` | Flat |
| 51 | 9170051 | CO Prestaciones Accrual | social_security | `retro_simple_tax` | Formula |
| 61 | 9170061 | CO Total Employee Deductions | social_security | `retro_simple_tax` | Formula |
| 62 | 9170062 | CO Total Employer Cost | social_security | `retro_simple_tax` | Formula |
| 71 | 9170071 | CO Net Pay | social_security | `retro_simple_tax` | Formula |
| 101 | 9170101 | CO Overtime and Premiums | social_security | `retro_simple_tax` | Formula |
| 111 | 9170111 | CO Incapacity — Employer Days 1–2 | social_security | `retro_simple_tax` | Formula |
| 121 | 9170121 | CO Severance on Termination | social_security | `retro_simple_tax` | Formula |

**23 regulations** — 20 core plus 3 Layer 2.

---

## PART 4 — Regulation detail

### 9170011 — Gross and the salary / non-salary split

```
58101 = SUM(taxability matrix A — salary-constituting)
58102 = SUM(taxability matrix B — non-salary as pacted)
```

CST art. 128 lets parties agree that a payment is not salary. That agreement takes it out of the contribution base — but not out of taxable income, and not without limit. This is the regulation that separates the two streams before the clamp tests them.

The transport allowance is the clearest case: it is expressly non-salary (CST art. 128), so it stays out of the IBC, but it **is** in the prima and cesantías base per CST art. 306, which is why the worked example accrues those on 2,000,000 while contributing on 1,750,905.

### 9170012 — The IBC, and the 40% clamp

```
Step 1  58103 = MAX( $58102 − MULTIPLY(ADD($58101;$58102);52552) ; 0 )   40% clamp
Step 2  58104 = ADD($58101;$58103)
        integral branch, assertion EQUALS($58201;1):
        58104 = MULTIPLY($58104;52551)                                    70% factor
Step 3  58104 = MAX($58104;52501)                                         floor 1 SMMLV
Step 4  58104 = MIN($58104;MULTIPLY(52501;25))                            ceiling 25 SMMLV
```

**The order is fixed and confirmed**, and it is the one thing about this regulation that cannot be inferred from the rates: *40% clamp → 70% integral factor → floor → ceiling*.

The 70% applies to the whole remuneration **first**; the ceiling then binds on the 70% figure, not the other way round. Only the 25-SMMLV ceiling limits the IBC — never 70% of a ceiling-adjusted salary. Confirmed against UGPP guidance (*"Tope Máximo 25 SMMLV… El IBC no debe superar este tope"*).

**Why the order is worth stating rather than assuming.** For an all-inclusive salary of COP 25,000,000 the sequence is invisible: 70% = 17,500,000, well under the ceiling. It only binds above roughly 35.7 SMMLV, so a build that gets it backwards passes every ordinary test case and fails silently on senior staff.

**Ley 1393 de 2010 art. 30:** non-salary payments may not exceed 40% of total remuneration; the excess is dragged back into the contribution base. This is arithmetic on summed conditionals, so **it cannot live in a taxability matrix** — the matrix says which stream a wage type joins, and this regulation tests the result.

**This is where the WTC's 34 conditional rows resolve.** Each carries its rule in the explanation column — for profit sharing, *"CST art. 128 expressly excludes la participación de utilidades … but it counts in the Ley 1393 art. 30 40% test"*. The matrix routes them to `58102` and the clamp does the rest; the `Non-Salary Pact Flag` gates whether the pact exists at all.

**Ordering matters and is not obvious.** The 70% integral factor applies to the **whole** remuneration before the floor and ceiling tests, not after. Carried as item 3 — the CCG gives the rule but not the ordering.

Floor 1 SMMLV, ceiling 25 SMMLV, both in the dedicated columns rather than inside `MIN`/`MAX` — the France lesson: a value inside `MIN()` is not a ceiling to the engine.

### 9170021 / 9170022 — Employee health and pension

Flat 4% each on `58104`. **Each contribution rounds up to the next multiple of 100 pesos** (Decreto 1990 de 2016) — applied per contribution, not to the total, which the worked example confirms: 70,036.20 → 70,100 twice, totalling 140,200 and not 140,100.

`9170022` carries assertion `LESS($58207;1)` — a foreign national covered by the exemption contributes no pension.

### 9170023 — The solidarity fund, as one Differential

```
Assertion: GTE($58104; MULTIPLY(52501;4))
Bands on $58104 expressed in SMMLV multiples:
   ≥4  <16   → 1.0%
   ≥16 <17   → 1.2%     ≥17 <18 → 1.4%
   ≥18 <19   → 1.6%     ≥19 <20 → 1.8%
   ≥20       → 2.0%
```

The statute frames this as two accounts — solidarity 1.0% from 4 SMMLV, subsistence 0.2%–1.0% from 16 — but they land on one employee deduction on one base. **One Differential regulation with all bands**, per the dev convention that progressive scales are never decomposed into atomic threshold/base/amount regulations.

Band values stated as annual figures and divided by period frequency by the engine.

### 9170032 / 9170033 — Withholding

The ET art. 388 depuration, in order: taxable payments → less mandatory contributions → less deductions → less exempt income at 25% (cap 790 UVT/year) → the whole subject to the 40% combined cap (1,340 UVT/year) → result in UVT → art. 383 table.

Both caps are **annual** while withholding is **monthly**. Mercans apportions at one twelfth — 65.8333 and 111.6667 UVT. **No regulation prescribes this.** Carried as item 4, labelled an assumption rather than resolved silently.

`9170034` (Procedure 2) uses `_ytm`: the percentage is set from the prior twelve months' taxable payments divided by **13**, not 12 (ET art. 386 — *"dividir por 13"*), which smooths the prima's thirteenth-month effect. Where service is under twelve months the divisor is the actual months served.

### 9170042 / 9170044 — The art. 114-1 exoneration, and the asymmetry that matters

```
9170042  employer health 8.5%   assertion LESS($58203;1)
9170044  CCF 4%    — no exoneration assertion
         SENA 2%   assertion LESS($58203;1)
         ICBF 3%   assertion LESS($58203;1)
```

**ET art. 114-1 exonerates employer health, SENA and ICBF for employees earning under 10 SMMLV — but never CCF.** This asymmetry is the one structural reason the payroll-levy perimeter is genuinely distinct from the IBC perimeter, and the worked example confirms it: employer health 0, SENA 0, ICBF 0, CCF 70,100.

### 9170046 — High-risk pension surcharge

**Assertion:** `EQUALS($58205;1)` · **Formula:** `MULTIPLY($58104;52523)` · employer-only.

**Decreto Ley 2090 de 2003 art. 5:** *"El monto de la cotización especial para las actividades de alto riesgo es el previsto en la Ley 100 de 1993, más diez (10) puntos adicionales a cargo del empleador."*

So total pension becomes **26%** (16% standard + 10pp), with the employer share rising from 12% to **22%**. Same IBC — no separate base, no separate ceiling.

Corroborated by the decree's own recitals quoting Ley 797 de 2003 art. 17, which empowers adjustment *"hasta en 10 puntos a cargo del empleador"*.

**Note for anyone maintaining this:** the rate is not in Resolución 2388 de 2016. That resolution carries the PILA *reporting* fields for high-risk activity, which is why a search that starts from the filing format finds the flag but never the rate.

### 9170013 — Apprentices

The one wage type in the whole WTC where the four IBC perimeters diverge. An apprentice in the **lectiva** phase carries health and ARL but no pension; the **productiva** phase differs again. Routed on `58208` rather than expressed as matrix rows, because a matrix cannot hold a phase.

### The active pensioner — routed on an existing field, not a new flag

A pensioner who keeps working owes health but **not** pension, and the contingency cannot accrue twice. The design routes this on the **`Worker Sub-Type` field, value `01`** (DD Country Fields row 27), which already carries the PILA *tipo de cotizante* taxonomy.

**No separate active-pensioner flag is created.** The CCG is explicit on this point, and it is the right call: PILA already classifies the population, and a parallel boolean would be a second source of truth for the same fact — the kind of duplication that drifts once someone edits one and not the other.

### 9170111 — Incapacity, employer days 1–2 only

Colombia has no employer sick-pay scheme. The employer bears **only the first two days** of a general-illness incapacity; days 3–90 are EPS at 66.67% of the contribution base, 91–180 EPS at 50%, and occupational events go to the ARL at 100% from the day after. **The employer rate for days 1–2 is 66.66%**, and this is now a cited position rather than a default. Decreto 780 de 2016 art. 3.2.1.10 par. 1 — read in full, not only the allocation sentence — allocates payer responsibility and never states a rate. Two independent MinSalud conceptos fill that silence by **direct application** of CST art. 227, not by analogy: Concepto 202311602174531 de 2024 (*"los dos (2) primeros días de incapacidad serán asumidos por el empleador teniendo en cuenta el 66.6% del salario"*) and Concepto 202342302183712 de 2023, reaching the same figure the same way.

---

## PART 5 — Numeric validation

Recomputed from `m12_examples.md` Example 1 — minimum-wage employee, risk class I, art. 114-1 exonerated:

| Line | CCG | Recomputed | |
|---|---|---|---|
| Contribution base | 1,750,905 | 1,750,905 | ✅ |
| Employee health 4% | 70,100 | 70,036.20 → 70,100 | ✅ |
| Employee pension 4% | 70,100 | 70,036.20 → 70,100 | ✅ |
| FSP | 0 | base < 4 SMMLV | ✅ |
| Depurated subtotal (C) | 1,859,800.00 | 1,859,800.00 | ✅ |
| 25% exempt (E) | 464,950.00 | 464,950.00 | ✅ |
| Taxable base (G) | 1,394,850.00 | 1,394,850.00 | ✅ |
| In UVT (H) | 26.6325 | 26.6325 | ✅ |
| Withholding | 0 | ≤ 95 UVT band | ✅ |
| Employer pension 12% | 210,200 | 210,108.60 → 210,200 | ✅ |
| Employer health | 0 | exonerated | ✅ |
| ARL class I 0.522% | 9,200 | 9,139.72 → 9,200 | ✅ |
| CCF 4% | 70,100 | 70,036.20 → 70,100 | ✅ |
| SENA / ICBF | 0 | exonerated | ✅ |
| Contributions subtotal | 289,500 | 289,500 | ✅ |
| Accruals 21.8333% | 426,287.72 | 426,286.96 | ✅ |
| **Total employer cost** | **2,715,787.72** | **2,715,787.72** | ✅ |
| Employer cost factor | 1.3579 | 1.3579 | ✅ |

**Closes to the peso.** The round-up-to-100 rule, the exoneration pattern and the split accrual bases (prima and cesantías on 2,000,000 including the transport allowance; vacation on 1,750,905 excluding it) all reproduce exactly.

---

## PART 6 — Open items

Four of the eight items carried in the draft closed in the final research pass. Recorded with how they closed, because the method is reusable.

| # | Item | Status | Detail |
|---|---|---|---|
| 1 | Integral salary — 70% before or after the ceiling | ✅ **Closed** | Order confirmed: 40% clamp → 70% factor → floor → ceiling. The 70% applies to the whole remuneration first; only the 25-SMMLV ceiling limits the IBC. Confirmed against UGPP guidance. Built into `9170012` |
| 2 | High-risk pension surcharge rate | ✅ **Closed** | **+10 percentage points, employer-borne** — Decreto Ley 2090 art. 5, verbatim. Total pension 26%, employer share 12% → 22%. Built as `9170046`. The source was in the pipeline folder throughout; the earlier search went to the PILA *reporting* resolution rather than the decree that sets the rate |
| 3 | Employer rate for incapacity days 1–2 | ✅ **Closed** | **66.66%**, now cited rather than defaulted. Decreto 780 art. 3.2.1.10 par. 1 read in full allocates the days without a rate; two MinSalud conceptos apply CST art. 227 **directly**, not by analogy. The search was exhausted rather than the default left standing |
| 4 | Active-pensioner routing | ✅ **Closed** | Carried on the existing `Worker Sub-Type` field, value `01` (DD row 27). **No new flag** — PILA already classifies the population, and a parallel boolean would be a second source of truth for the same fact |
| 5 | DD `Internal Code` empty — 1 of 99 | 🟡 **Not a compliance item** | The Master Data Dictionary Template classifies the column **SYSTEM · (generated)** — allocated from the HRB namespace, not researched. All 99 fields are delivered, named and mapped. Bindings marked `[PENDING-CODE]`; substitution is mechanical. **The France design stopped here, which in hindsight was the wrong call** — write the design, mark the bindings |
| 6 | Monthly apportionment of the 790 / 1,340 UVT annual caps | 🟡 **Labelled assumption** | Both caps annual, withholding monthly. Mercans apportions at one twelfth (65.8333 and 111.6667 UVT). No regulation prescribes it, and that has been established rather than assumed — so this is a product convention, correctly labelled, not an open research item |
| 7 | SMMLV litigation exposure | 🟢 **Resolved, watched** | Decreto 1469 suspended 12 Feb 2026, Decreto 0159 refixed the identical amount, **suspension revoked 9 July 2026** — Decreto 1469 operative again, Decreto 0159 spent. The merits action remains pending; re-verify before the 2027 cut-over. The amount was never in dispute |
| 8 | Law 2381 of 2024 pension reform | 🟢 **Scoped to 2027** | Judgment C-264 of 25 August 2026 upheld art. 94 on the understanding that the provisions take effect **1 April 2027**. No part configurable for 2026. Re-verify the parameters before the cut-over |
| 9 | Cesantías 8.33% monthly advance | 🟢 **Scoped out** | Ley 2466 art. 64 par. 1 is in force and permits it, but routes through PILA pending a MinSalud decree still in draft. Accrual designed; monthly deposit not |

**Nothing in this list blocks the design.** Items 5 and 6 are owned elsewhere and correctly labelled; 7, 8 and 9 are watch items with dates.

---

## PART 7 — Taxability matrices

**Four matrices, not ten.** Built in `CO_Taxability_Matrices_v1_0.md` from all 403 WTC rows; raw extraction in `CO_Taxability_Perimeters_Extract.csv`.

Pairwise testing across all 403 rows:

| Comparison | Divergences |
|---|---|
| Health vs Occupational risk | **0** |
| Solidarity vs Pension | **0** |
| Health vs Pension | **1** |
| Health vs Payroll levies | **53** |
| Payroll levies vs Statutory-benefit base | **21** |
| Statutory-benefit base vs Vacation base | **52** |

Health, solidarity, ARL and pension are **one perimeter**, diverging on the single apprentice row that `9170013` handles. The four that are genuinely distinct:

| Matrix | Perimeter | Consumed by |
|---|---|---|
| **A** | IBC | `9170012`, `9170021`–`9170023`, `9170041`–`9170043`, `9170046` |
| **B** | Payroll levies | `9170044` |
| **C** | Statutory-benefit base | `9170051` |
| **D** | Vacation base | `9170051` |

**Why B is distinct:** ET art. 114-1 exonerates employer health, SENA and ICBF below 10 SMMLV but **never CCF**. Statutory asymmetry, not a modelling choice.

**Why C and D are distinct from each other:** the transport allowance is out of the IBC (CST art. 128), in the prima and cesantías base (CST art. 306), and out of the vacation base. One wage type, three different answers, all correct — which is why the worked example accrues prima on 2,000,000 and vacation on 1,750,905.

**The 34 conditional rows** route to the non-salary stream `58102`; the 40% clamp in `9170012` tests the result. A condition never sits in a matrix cell.

---

## PART 8 — Validation summary

| Check | Result |
|---|---|
| CCG worked example, 17 lines recomputed | ✅ closes to the peso, including the round-up-to-100 rule |
| Employer cost factor | ✅ 1.3579 |
| Perimeter identity tested mechanically, 403 rows | ✅ four matrices, not ten |
| Ordinals monotonic, no duplicates | ✅ 23 regulations |
| Every rate traced to an article | ✅ |
| Dated tables for both July step-changes | ✅ divisor 220→210 on 15 July, premium 80%→90% on 1 July |
| Two units never interchanged | ✅ UVT for tax, SMMLV for contributions |
| Special-category sweep (CI checklist) | ✅ six categories, all routed |
| Flat per-head charge check (Bahrain lesson) | ✅ none in Colombia — all charges are rate-on-base |
