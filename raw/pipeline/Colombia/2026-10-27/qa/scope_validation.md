# Colombia (CO) — Scope Lock-In Validation

**Artifact validated:** `CO-compliance/scope_manifest.json` (47,503 bytes, `scope_version` 1.0, `source_document` CO-CCG-001 v1.0)
**Schema:** `shared/scope_manifest_template.json`
**Validator:** Agent 07 (QA cross-check), gate v2.8 (B7 decision-row format, B1 non-resident rule)
**Validated:** 2026-09-04
**Result: PASS — 0 errors, 0 warnings, 42 assertions passed, 0 blocking findings.**

---

## 1. Gate results

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | File exists and is valid JSON | **PASS** | `json.load()` succeeded; 47,503 bytes; top-level object with 18 keys |
| 2 | Every required section present and non-empty | **PASS** | 17/17 required keys present, all non-empty (see below) |
| 3 | Every `authority_filings.in_scope` entry carries all required fields | **PASS** | 6/6 filings complete; all `integration_type` in enum; all `product_mapping_required` boolean |
| 4 | Every `integrations.inbound` entry has `product_mapping_required` set | **PASS** | 5/5 set, **all `true`** — **no F8 warning raised** |
| 5 | No code in both `in_scope` and `out_of_scope` for the same mapper | **PASS** | 0 collisions; 0 intra-list duplicates across 5 mappers |
| 6 | `known_failure_patterns_to_check` populated with F1–F15 | **PASS** | F1–F22 present (22 patterns, superset of the required 15) |
| B1 | Non-resident handling for covered income types | **PASS** | ET art. 408 flat 20% on gross, no depuration, until ET art. 10 residence; then art. 383 table **prospectively**. Stated in 3 independent places. |

### Check 2 detail — section inventory

| Section | Key | Length |
|---|---|---|
| employment_types | in_scope / out_of_scope / rationale | 13 / 11 / 1,242 chars |
| authority_filings | in_scope / out_of_scope | 6 / 7 |
| wage_type_categories | in_scope / out_of_scope / special_rules | 33 / 8 / 8 |
| option_mapper_scope | personal_id_type / insurance_type / contract_type / correction_codes / benefit_type | 10 / 8 / 5 / 6 / 12 |
| integrations | outbound / inbound / both | 8 / 5 / 3 |

The manifest also carries four sections beyond the template — `employment_types.inbound_data_contract`, `known_gaps` (11), `resolved_in_this_pass` (8) and `failure_pattern_notes` (5). These are additive and do not conflict with the schema.

### Check 3 detail — in-scope filings

| filing_id | authority | frequency | format | integration_type | product_mapping_required |
|---|---|---|---|---|---|
| CO-DIAN-NE-MONTHLY-001 | DIAN | monthly | XML | both | true |
| CO-DIAN-F350-MONTHLY-002 | DIAN | monthly | XLSX | outbound | true |
| CO-PILA-MONTHLY-003 | MSPS via operador de informacion | monthly | TXT | both | true |
| CO-DIAN-F220-ANNUAL-004 | DIAN (employer to employee) | annual | XLSX | outbound | true |
| CO-DIAN-EXO2276-ANNUAL-005 | DIAN | annual | XML | outbound | true |
| CO-CESANTIAS-DEPOSIT-ANNUAL-006 | Fondos de Cesantias | annual | CSV | both | true |

All 7 `out_of_scope` filings carry a `descoping_reason`; all 7 also carry `client_impact`, which the schema does not require.

### Check 4 detail — F8 exposure

All five inbound integrations are `product_mapping_required: true`, each with an explicit `product_mapping_rationale`. Failure mode F8 ("inbound integrations wrongly excluded from product mapping") is not present. The DIAN `ApplicationResponse` is correctly flagged as mandatory to parse — tax-deductibility of the payroll cost is gated on the stored validation status and CUNE.

### Check 5 detail

`option_mapper_scope` declares in-scope codes only; no per-mapper `out_of_scope` list exists, so no in/out collision is possible by construction. Cross-checking the in-scope code sets against descoped items elsewhere in the manifest also returns clean:

- `correction_codes` in scope = E, A, N, M, J, X. Descoped planillas = T, F (public sector), I, Y (independents), B, D (Social Protection Floor / Solidarity), H (substitute mothers), K (Law 789 students). **Disjoint.**
- `contract_type` in scope = 1–5, including 4 (Aprendizaje) and 5 (Practicas), both of which appear in `employment_types.in_scope`. **Consistent.**
- `integrations.both` = NE, PILA, CESANTIAS — exactly the three filings whose `integration_type` is `both`. **Consistent.**

---

## 2. Non-blocking observations (recorded, not gate failures)

1. **Numeral `47` carries two unrelated meanings.** It is an in-scope `personal_id_type` (PEP, Permiso Especial de Permanencia) and simultaneously an out-of-scope *worker type* (public servant, listed in `employment_types.out_of_scope` as types 18/30/47/58). Different mappers, so Check 5 is not violated, but downstream agents building the DD and specs must not treat a bare "47" as scope-decidable — it is an F2 leak surface. Recommend the DD label the columns explicitly (`Tipo de documento` vs `Tipo de cotizante`).
2. **No `worker_type` (tipo de cotizante) mapper is declared.** The template requires only the five mappers present, and worker types are referenced in prose (`employment_types.out_of_scope` types 18/30/47/58; `inbound_data_contract` requires "worker type and sub-type"). Downstream 05-DD will need to materialise this mapper from the CCG rather than from the manifest.
3. **Mapper entries are descriptive strings, not code/label pairs.** For `insurance_type` and `benefit_type` the leading token is a fund name or a novedad mnemonic rather than a numeric code, so only 2 of 8 `insurance_type` entries parse as coded. The template mandates no format (empty arrays), so this passes, but 05-DD must not assume a uniform `NN - Label` shape.
4. **`known_gaps` carries 11 open items.** These are declared, not hidden, and each has an `action`. They are inputs to later gates, not scope defects.

---

## 3. B1 — non-resident handling

Not a finding. Covered income types include non-resident foreign nationals, and the treatment is specified rather than merely acknowledged:

- `employment_types.in_scope[10]`: non-resident foreign nationals under a Colombian contract are **explicitly IN scope**, withheld at the flat 20% of ET art. 408 until tax residence is acquired (DIAN Concepto 011108 of 29 June 2026).
- `employment_types.rationale`: restates the flat 20% and the **prospective** switch to the ET art. 383 table on acquisition of residence.
- `wage_type_categories.special_rules[7]`: flat 20% **on gross, with no depuration and no exemptions**.
- `employment_types.inbound_data_contract`: requires a tax-residence flag **with an effective date**, plus a presence-day accumulator over a rolling 365-day window — i.e. the engine can actually determine when the switch fires.

That last point is what makes this pass rather than a paper mention: the residence test has a data contract behind it.

---

## 4. Scope decision register (v2.8 B7)

Every scope decision in the manifest, one row each. `OWNED-UPSTREAM` = the artifact or data originates outside the payroll engine. `INBOUND-DATA-CONTRACT` = the engine must receive data from an external party to execute the decision. `REVERSIBLE` = the decision can be changed later without re-architecting the engine (N = statutory obligation, or a base/rounding architecture choice rather than a toggle).

### A. Employment types

| DECISION | IN-SCOPE | OWNED-UPSTREAM | INBOUND-DATA-CONTRACT | REVERSIBLE(Y/N) | BASIS |
|---|---|---|---|---|---|
| Indefinite-term employment contract (contrato a termino indefinido) - CST art.... | Y | N | Y | Y | CST art. 47; Law 2466/2025 art. 5 |
| Fixed-term employment contract, maximum 4 years (contrato a termino fijo) - CS... | Y | N | Y | Y | CST art. 46; Law 2466/2025 art. 6 |
| Specific work or task contract (contrato por obra o labor determinada) - CST a... | Y | N | Y | Y | CST art. 46 |
| Occasional, accidental or transitory work contract - CST art. 6 | Y | N | Y | Y | CST art. 6 |
| Apprenticeship contract (contrato de aprendizaje) - special fixed-term LABOUR ... | Y | N | Y | Y | CST art. 81 as substituted by Law 2466/2025 art. 21 and regulated by Decreto 0223 of 5 March 20... |
| Internship / practical placement (practicas o pasantias) - nomina electronica ... | Y | N | Y | Y | CO-CCG-001 v1.0 |
| Part-time employees (no separate Colombian regime; contribution base floored a... | Y | N | Y | Y | CO-CCG-001 v1.0 |
| All-inclusive salary employees (salario integral, >= 13 minimum wages) - CST a... | Y | N | Y | Y | CST art. 132 num. 2 |
| Employees on telework and remote work (Law 1221/2008 as amended by Law 2466/20... | Y | N | Y | Y | Law 1221/2008 as amended by Law 2466/2025 arts. 52-54 |
| Resident foreign national employees under a Colombian contract | Y | N | Y | Y | CO-CCG-001 v1.0 |
| NON-RESIDENT foreign national employees under a Colombian contract (withheld a... | Y | N | Y | Y | ET art. 408 until tax residence is acquired - DIAN Concepto 011108 of 29 June 2026 |
| Employed old-age pensioners in active service (worker sub-type 01, no pension ... | Y | N | Y | Y | CO-CCG-001 v1.0 |
| Executive directors and statutory legal representatives holding an employment ... | Y | N | Y | Y | CO-CCG-001 v1.0 |
| Public servants / servidores publicos (nomina electronica worker types 18, 30,... | N | Y | N | Y | CO-CCG-001 v1.0 |
| Military and national police special regimes | N | Y | N | Y | CO-CCG-001 v1.0 |
| Independent workers and service contractors (trabajadores independientes / con... | N | Y | N | Y | CO-CCG-001 v1.0 |
| Non-executive directors receiving attendance fees only (corporate mandate, not... | N | Y | N | Y | Law 1955/2019 art. 244 |
| Domestic workers (worker type 02) and family drivers - private sector but outs... | N | Y | N | Y | CO-CCG-001 v1.0 |
| Community mothers / madres comunitarias (worker type 04) and substitute mother... | N | Y | N | Y | CO-CCG-001 v1.0 |
| Medical interns under CST art. 81A (remuneration paid by the health-system res... | N | Y | N | Y | CST art. 81A (remuneration paid by the health-system resource administrator |
| Digital delivery-platform workers - Law 2466/2025 arts. 24-30 do not enter int... | N | Y | N | Y | Law 2466/2025 arts. 24-30 do not enter into force until 12 months after the Government complete... |
| Self-insured categories and voluntary occupational-risk affiliates (Decree 156... | N | Y | N | Y | Decree 1563/2016 |
| Social Protection Floor contributors (PILA planilla B) and Solidarity Contribu... | N | Y | N | Y | CO-CCG-001 v1.0 |
| Students under the Law 789/2002 special regime (PILA planilla K) | N | Y | N | Y | Law 789/2002 special regime (PILA planilla K |

### B. Authority filings

| DECISION | IN-SCOPE | OWNED-UPSTREAM | INBOUND-DATA-CONTRACT | REVERSIBLE(Y/N) | BASIS |
|---|---|---|---|---|---|
| CO-DIAN-NE-MONTHLY-001 - Documento Soporte de Pago de Nomina Electronica (Electr... | Y | N | Y | N | Resolucion DIAN 000013 de 11 Feb 2021 arts. 1, 2, 3, 5, 8; Anexo Tecnico v1.0; XSD v1.0.6 |
| CO-DIAN-F350-MONTHLY-002 - Formulario 350 - Declaracion mensual de retenciones en ... | Y | N | N | N | Resolucion DIAN 000031 de 29 Feb 2024 (in force from 1 Aug 2024); DUR 1625 de 2016 art. 1.6.1.1... |
| CO-PILA-MONTHLY-003 - Planilla Integrada de Liquidacion de Aportes (PILA) - s... | Y | N | Y | N | Resolucion MSPS 2388 de 2016 and Anexo Tecnico 2; Decreto 780 de 2016 arts. 3.2.1.5, 3.2.2.1, 3... |
| CO-DIAN-F220-ANNUAL-004 - Formulario 220 - Certificado de Ingresos y Retenciones ... | Y | N | N | N | ET arts. 378, 379, 380; DUR 1625 de 2016 art. 1.6.1.13.2.40; form prescribed by Resolucion DIAN... |
| CO-DIAN-EXO2276-ANNUAL-005 - Informacion exogena - Formato 2276 version 4, rentas de... | Y | N | N | N | Resolucion DIAN 000227 de 23 Sep 2025 arts. 1.3.7.1.1 and 1.3.9.1 |
| CO-CESANTIAS-DEPOSIT-ANNUAL-006 - Consignacion anual de cesantias al fondo elegido por el... | Y | N | Y | N | Ley 50 de 1990 art. 99 num. 3; CST art. 57 par. 4 as added by Ley 2466 de 2025 art. 15; Ley 246... |
| CO-MINTRABAJO-DISCAPACIDAD-REPORT - Reporte de contratos con personas con discapacidad al M... | N | Y | N | Y | HR-scope - requires data beyond payroll system. Requires MinSalud disability certification, per... |
| CO-SENA-CUOTA-APRENDICES - Cuota de aprendices (apprentice quota determination) an... | N | Y | N | Y | HR-scope - requires data beyond payroll system. The quota is fixed by SENA on the employer's he... |
| CO-RUAF-NOVEDADES - RUAF-ND vital-events registry notifications (births, de... | N | Y | N | Y | HR-scope - requires data beyond payroll system. Reported by health providers and by the employe... |
| CO-PILA-PLANILLA-T-F - PILA planilla types T and F (Sistema General de Partici... | N | Y | N | Y | Employment type out of scope - public-sector only (contributor type 47). Not applicable to priv... |
| CO-PILA-PLANILLA-I-Y - PILA planilla types I and Y (independent workers, and t... | N | Y | N | Y | Employment type out of scope - independent workers and service contractors. The contribution ba... |
| CO-ICA-RETENCION - Retencion de Industria y Comercio (municipal turnover-t... | N | Y | N | Y | Not a payroll filing - a municipal business-turnover tax withheld on supplier payments, with no... |
| CO-DIAN-F110-RENTA - Employee annual income-tax return (declaracion de renta... | N | Y | N | Y | Employee obligation, not an employer filing. Colombia imposes NO employer year-end tax reconcil... |

### C. Wage type categories

| DECISION | IN-SCOPE | OWNED-UPSTREAM | INBOUND-DATA-CONTRACT | REVERSIBLE(Y/N) | BASIS |
|---|---|---|---|---|---|
| Basic salary (salario basico), fixed and variable | Y | N | N | Y | CO-CCG-001 v1.0 |
| All-inclusive salary (salario integral) - contribution and payroll-levy bases ... | Y | N | N | Y | CO-CCG-001 v1.0 |
| Auxilio de transporte (statutory transport allowance) - COP 249,095 for 2026, ... | Y | N | N | Y | CO-CCG-001 v1.0 |
| Auxilio de conectividad (connectivity allowance for teleworkers) - COP 249,095... | Y | N | N | Y | CO-CCG-001 v1.0 |
| Overtime - day (+25%) and night (+75%) | Y | N | N | Y | CO-CCG-001 v1.0 |
| Night premium (recargo nocturno) +35%, window 19:00-06:00 from 25 Dec 2025 | Y | N | N | Y | CO-CCG-001 v1.0 |
| Obligatory rest-day / holiday premium - 80% to 30 Jun 2026, 90% from 1 Jul 202... | Y | N | N | Y | CO-CCG-001 v1.0 |
| Paid weekly rest day and paid public holidays | Y | N | N | Y | CO-CCG-001 v1.0 |
| Commissions and sales percentages | Y | N | N | Y | CO-CCG-001 v1.0 |
| Habitual bonuses (salary) and occasional gratuities (non-salary) | Y | N | N | Y | CO-CCG-001 v1.0 |
| Extra-statutory bonuses under a written CST art. 128 non-salary pact (clamped ... | Y | N | N | Y | CST art. 128 non-salary pact (clamped at 40% by Ley 1393/2010 art. 30 |
| Salary in kind (salario en especie) - capped at 50% of total salary, 30% at th... | Y | N | N | Y | CO-CCG-001 v1.0 |
| Prima de servicios (statutory service bonus) - 30 days per year, half by 30 Ju... | Y | N | N | Y | CO-CCG-001 v1.0 |
| Cesantias (severance savings) - one month's salary per year of service | Y | N | N | Y | CO-CCG-001 v1.0 |
| Intereses a las cesantias - 12% per year | Y | N | N | Y | CO-CCG-001 v1.0 |
| Vacaciones (annual leave) - 15 working days; paid rest, so IN the contribution... | Y | N | N | Y | CO-CCG-001 v1.0 |
| Compensacion en dinero de vacaciones - up to half, on the employee's prior wri... | Y | N | N | Y | CO-CCG-001 v1.0 |
| Dotacion (work clothing and footwear) - three deliveries per year for employee... | Y | N | N | Y | CO-CCG-001 v1.0 |
| Incapacidad por enfermedad general - employer days 1-2, EPS from day 3 (66.67%... | Y | N | N | Y | CO-CCG-001 v1.0 |
| Incapacidad de origen laboral - ARL from the day after the event, 100% of the ... | Y | N | N | Y | CO-CCG-001 v1.0 |
| Licencia de maternidad (18 weeks) and licencia de paternidad (2 weeks), paid b... | Y | N | N | Y | CO-CCG-001 v1.0 |
| Licencia parental compartida and flexible parental leave | Y | N | N | Y | CO-CCG-001 v1.0 |
| Statutory paid leave under CST art. 57 num. 6 - voting, transitory office, gra... | Y | N | N | Y | CST art. 57 num. 6 - voting |
| Licencia de luto (bereavement) - 5 working days | Y | N | N | Y | CO-CCG-001 v1.0 |
| Apoyo de sostenimiento del aprendiz - 75% / 100% of the minimum wage by phase | Y | N | N | Y | CO-CCG-001 v1.0 |
| Indemnizacion por despido sin justa causa (CST art. 64) - tiered by salary and... | Y | N | N | Y | CST art. 64 |
| Indemnizacion moratoria (CST art. 65) and the cesantias non-deposit and unpaid... | Y | N | N | Y | CST art. 65 |
| Pagos de alimentacion a terceros (ET art. 387-1) - not income up to 41 UVT/mon... | Y | N | N | Y | ET art. 387-1 |
| Employer-paid prepaid health / supplementary health plans | Y | N | N | Y | CO-CCG-001 v1.0 |
| Employer contributions to voluntary pension funds and to the individual pensio... | Y | N | N | Y | CO-CCG-001 v1.0 |
| Equity and share-incentive awards - taxable at exercise or vesting on the spre... | Y | N | N | Y | CO-CCG-001 v1.0 |
| Employee deductions: health 4%, pension 4%, Fondo de Solidaridad Pensional 1% ... | Y | N | N | Y | CO-CCG-001 v1.0 |
| Post-tax deductions: union dues, cooperative and savings-fund dues, disciplina... | Y | N | N | Y | CO-CCG-001 v1.0 |
| Independent-contractor fees and honorarios de junta directiva paid to non-empl... | N | Y | N | Y | CO-CCG-001 v1.0 |
| Public-sector allowances: prima especial, prima de costo de vida, and ET art. ... | N | Y | N | Y | ET art. 206 nums. 6-9 exemptions (military |
| Pension payments made by the pension administrator (not by the employer) | N | Y | N | Y | CO-CCG-001 v1.0 |
| Bono pensional (pension bond on transfer between regimes) | N | Y | N | Y | CO-CCG-001 v1.0 |
| Subsidio familiar paid by the Caja de Compensacion Familiar to the employee (a... | N | Y | N | Y | CO-CCG-001 v1.0 |
| Medical-intern remuneration paid by ADRES under CST art. 81A | N | Y | N | Y | CST art. 81A |
| Digital delivery-platform earnings (Ley 2466/2025 arts. 24-30, not yet in forc... | N | Y | N | Y | Ley 2466/2025 arts. 24-30 |
| Value-added tax withholding, industry and commerce tax withholding, stamp duty... | N | Y | N | Y | CO-CCG-001 v1.0 |

**Special rules (non-reversible engine architecture, not scope toggles):**

| DECISION | IN-SCOPE | OWNED-UPSTREAM | INBOUND-DATA-CONTRACT | REVERSIBLE(Y/N) | BASIS |
|---|---|---|---|---|---|
| THREE SEPARATE BASES, never interchangeable: (a) IBC for health, pension, occupational ris... | Y | N | N | N | Ley 21 de 1982 art. 17 'nomina mensual de salarios' INCLUDING paid rest days; ET art. 388 depur... |
| THE 40% CLAMP (Ley 1393 de 2010 art. 30): non-salary payments may not exceed 40% of total ... | Y | N | N | N | Ley 1393 de 2010 art. 30; Ley 100 arts. 18 and 204 purposes. The excess is forced BACK INTO the... |
| THE EXONERATION CLIFF (ET art. 114-1): employer health 8.5%, SENA 2% and ICBF 3% are exone... | Y | N | N | N | ET art. 114-1 |
| THE 25% RENTA EXENTA IS COMPUTED LAST (ET art. 206 num. 10), on the figure net of non-taxa... | Y | N | N | N | ET art. 206 num. 10; ET art. 336 num. 3 |
| THREE ROUNDING REGIMES IN ONE PAYROLL MONTH: PILA rounds UP (IBC to the peso, each contrib... | Y | N | N | N | Decreto 1990 de 2016 art. 1; ET art. 577 |
| TWO MID-2026 CUT-OVERS, TWO WEEKS APART: the rest-day premium steps 80% -> 90% on 1 JULY 2... | Y | N | N | N | CST art. 179 par. transitorio; Ley 2466/2025 art. 14 |
| VACACIONES ARE NOT A PRESTACION SOCIAL. They are paid rest, so they ENTER the IBC and the ... | Y | N | N | N | CST art. 192; CST art. 132 num. 2 |
| NON-RESIDENT WITHHOLDING IS A FLAT 20% ON GROSS (ET art. 408), with no depuration and no e... | Y | N | N | N | ET art. 408; ET art. 10 is acquired |

### D. Option mapper scope

| DECISION | IN-SCOPE | OWNED-UPSTREAM | INBOUND-DATA-CONTRACT | REVERSIBLE(Y/N) | BASIS |
|---|---|---|---|---|---|
| personal_id_type: 12 - Tarjeta de identidad (authorised minors 15-17) | Y | N | Y | Y | CO-CCG-001 v1.0 |
| personal_id_type: 13 - Cedula de ciudadania (default for Colombian nationals 1... | Y | N | Y | Y | CO-CCG-001 v1.0 |
| personal_id_type: 21 - Tarjeta de extranjeria (foreign minors) | Y | N | Y | Y | CO-CCG-001 v1.0 |
| personal_id_type: 22 - Cedula de extranjeria (resident foreign nationals) | Y | N | Y | Y | CO-CCG-001 v1.0 |
| personal_id_type: 31 - NIT (rare; where the beneficiary is a legal person) | Y | N | Y | Y | CO-CCG-001 v1.0 |
| personal_id_type: 41 - Pasaporte (non-resident foreign nationals) | Y | N | Y | Y | CO-CCG-001 v1.0 |
| personal_id_type: 42 - Documento de identificacion extranjero | Y | N | Y | Y | CO-CCG-001 v1.0 |
| personal_id_type: 47 - PEP, Permiso Especial de Permanencia | Y | N | Y | Y | CO-CCG-001 v1.0 |
| personal_id_type: 50 - NIT de otro pais | Y | N | Y | Y | CO-CCG-001 v1.0 |
| personal_id_type: 91 - NUIP (employee use only; not present in the RUT databas... | Y | N | Y | Y | CO-CCG-001 v1.0 |
| insurance_type: Salud (health) - EE 4% / ER 8.5%, IBC capped at 25 SMMLV, ER... | Y | N | Y | Y | CO-CCG-001 v1.0 |
| insurance_type: Pension - EE 4% / ER 12%, IBC capped at 25 SMMLV, never exon... | Y | N | Y | Y | CO-CCG-001 v1.0 |
| insurance_type: Fondo de Solidaridad Pensional, subcuenta de solidaridad - E... | Y | N | Y | Y | CO-CCG-001 v1.0 |
| insurance_type: Fondo de Solidaridad Pensional, subcuenta de subsistencia - ... | Y | N | Y | Y | CO-CCG-001 v1.0 |
| insurance_type: Riesgos Laborales (occupational risk) - ER only, class I-V, ... | Y | N | Y | Y | CO-CCG-001 v1.0 |
| insurance_type: Caja de Compensacion Familiar - ER 4%, payroll-levy base, no... | Y | N | Y | Y | CO-CCG-001 v1.0 |
| insurance_type: SENA - ER 2%, payroll-levy base, no ceiling, exonerable belo... | Y | N | Y | Y | CO-CCG-001 v1.0 |
| insurance_type: ICBF - ER 3%, payroll-levy base, no ceiling, exonerable belo... | Y | N | Y | Y | CO-CCG-001 v1.0 |
| contract_type: 1 - Termino fijo (maximum 4 years, Ley 2466/2025 art. 6) | Y | N | Y | Y | Ley 2466/2025 art. 6 |
| contract_type: 2 - Termino indefinido (the default vinculation, Ley 2466/20... | Y | N | Y | Y | Ley 2466/2025 art. 5 |
| contract_type: 3 - Obra o labor determinada | Y | N | Y | Y | CO-CCG-001 v1.0 |
| contract_type: 4 - Aprendizaje (special fixed-term labour contract, Ley 246... | Y | N | Y | Y | Ley 2466/2025 art. 21 |
| contract_type: 5 - Practicas o pasantias | Y | N | Y | Y | CO-CCG-001 v1.0 |
| correction_codes: Planilla E - Empleados (regular payment for dependent contri... | Y | N | Y | Y | CO-CCG-001 v1.0 |
| correction_codes: Planilla A - Cotizante con novedad de ingreso (omitted hires... | Y | N | Y | Y | CO-CCG-001 v1.0 |
| correction_codes: Planilla N - Correcciones (correction of IBC, rate, contribu... | Y | N | Y | Y | CO-CCG-001 v1.0 |
| correction_codes: Planilla M - Mora (periods with total absence of payment, be... | Y | N | Y | Y | CO-CCG-001 v1.0 |
| correction_codes: Planilla J - Cumplimiento de sentencia judicial (reinstateme... | Y | N | Y | Y | CO-CCG-001 v1.0 |
| correction_codes: Planilla X - Empresa liquidada | Y | N | Y | Y | CO-CCG-001 v1.0 |
| benefit_type: ING - Ingreso (hire) | Y | N | Y | Y | CO-CCG-001 v1.0 |
| benefit_type: RET - Retiro (termination) | Y | N | Y | Y | ET - Retiro (termination |
| benefit_type: TDE / TAE - Traslado desde / hacia EPS | Y | N | Y | Y | CO-CCG-001 v1.0 |
| benefit_type: TDP / TAP - Traslado desde / hacia AFP | Y | N | Y | Y | CO-CCG-001 v1.0 |
| benefit_type: VSP / VST - Variacion permanente / transitoria de salario | Y | N | Y | Y | CO-CCG-001 v1.0 |
| benefit_type: SLN - Suspension o licencia no remunerada (health moves to 8... | Y | N | Y | Y | CO-CCG-001 v1.0 |
| benefit_type: IGE - Incapacidad general | Y | N | Y | Y | CO-CCG-001 v1.0 |
| benefit_type: LMA - Licencia de maternidad o paternidad | Y | N | Y | Y | CO-CCG-001 v1.0 |
| benefit_type: VAC / LR - Vacaciones o licencia remunerada | Y | N | Y | Y | CO-CCG-001 v1.0 |
| benefit_type: IRL - Incapacidad por accidente o enfermedad laboral | Y | N | Y | Y | CO-CCG-001 v1.0 |
| benefit_type: AVP - Aporte voluntario a pension | Y | N | Y | Y | CO-CCG-001 v1.0 |
| benefit_type: VCT - Variacion de centro de trabajo (may change the occupat... | Y | N | Y | Y | CO-CCG-001 v1.0 |

### E. Integrations

| DECISION | IN-SCOPE | OWNED-UPSTREAM | INBOUND-DATA-CONTRACT | REVERSIBLE(Y/N) | BASIS |
|---|---|---|---|---|---|
| OUT CO-OUT-NE-SOAP -> DIAN Validation Service (catalogo-vpfe.d... | Y | N | N | N | SOAP 1.2 / base64 ZIP containing XML / Operation SendNominaSync. Max 500 KB. UTF-8 only. XAdES-... |
| OUT CO-OUT-F350 -> DIAN Muisca electronic filing portal | Y | N | N | N | Portal form / Monthly. Values rounded to the nearest 1,000 (ET art. 577). Withholdings on natur... |
| OUT CO-OUT-PILA -> Licensed operador de informacion PILA | Y | N | N | N | TXT fixed-width / Archivo Tipo 1 (34 fields, 567 positions) and Archivo Tipo 2 (header 22 field... |
| OUT CO-OUT-F220 -> The employee (retained by the employer) | Y | N | N | N | Prescribed form, whole pesos / Annual, by the last business day of March. |
| OUT CO-OUT-2276 -> DIAN informacion exogena service | Y | N | N | N | XML / Annual, May-June by NIT. Requires three separate cesantias lines and the meal-payment spl... |
| OUT CO-OUT-CESANTIAS -> Fondos de Cesantias | Y | N | N | N | CSV or fund portal / Annual, by 14 February. Optional monthly 8.33% advance deposit under Ley 2... |
| OUT CO-OUT-BANKFILE -> The client's paying bank | Y | N | N | N | Bank-specific fixed-width or delimited / Colombia does NOT use IBAN. Domestic account numbers a... |
| OUT CO-OUT-PAYSLIP -> The employee | Y | N | N | N | PDF / Representacion grafica. PERMISSIVE under Resolucion DIAN 000013 de 2021 art. 24, but if i... |
| IN CO-IN-NE-APPRESPONSE <- DIAN Validation Service | Y | Y | Y | N | pmr=True / true - validation status and CUNE are stored fields; tax-deductibility... |
| IN CO-IN-PILA-SETTLEMENT <- Licensed operador de informacion PILA | Y | Y | Y | N | pmr=True / true - planilla number, payment date and per-contributor rejection fla... |
| IN CO-IN-EPS-ARL-BENEFIT <- EPS (health insurer) and ARL (occupation... | Y | Y | Y | N | pmr=True / true - modelled as a benefit wage-type line (paid to employee, receiva... |
| IN CO-IN-CESANTIAS-CONFIRMATION <- Fondos de Cesantias | Y | Y | Y | N | pmr=True / true - deposit-by-14-Feb compliance is tracked as a per-employee/per-y... |
| IN CO-IN-LIBRANZA-SCHEDULE <- Payroll lenders (entidades operadoras de... | Y | Y | Y | N | pmr=True / true - instalment amounts are a deduction wage-type; the 50%-of-net fl... |
| BOTH CO-BOTH-NE <-> DIAN | Y | N | Y | N | Outbound transmission and inbound validation response in a single M2M exchange. |
| BOTH CO-BOTH-PILA <-> Licensed operador de informacion PILA | Y | N | Y | N | Outbound settlement file and inbound settlement/payment confirmation. |
| BOTH CO-BOTH-CESANTIAS <-> Fondos de Cesantias | Y | N | Y | N | Outbound deposit file and inbound deposit confirmation. |

---

## 5. Verdict

All six gate checks pass with zero errors and zero warnings. The B1 non-resident rule is satisfied with an executable data contract, not just a citation. The four observations in section 2 are advisory notes for agents 04 and 05 and do not block lock-in.

**The scope is LOCKED. Downstream agents (02-WTC, 03-SIR, 04-reports-spec, 05-DD, 06-payslip, 08-skill) may proceed against `scope_manifest.json` v1.0.**

PASS
