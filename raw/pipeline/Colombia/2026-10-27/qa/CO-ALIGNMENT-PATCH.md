# Colombia — DD ↔ REPORT SPECS ALIGNMENT PATCH

**Country:** Colombia (CO) · **Stage:** alignment patch (mandatory pre-audit step)
**Date:** 2026-09-07 · **Result:** all six checks aligned — **0 open mismatches**

## Files patched

| File | v1.0 → | Rebuilt from source |
|---|---|---|
| `05-data-dictionary/CO-DD-001-v1.0.xlsx` | v1.1 | `build_co_dd.py` + `co_dd_data_{employee,employer,employment,mappers}.py` |
| `04-reports-spec/CO-DIAN-001-NominaElectronica-Spec.xlsx` | v1.1 | `co_r1_nomina_electronica.py` / `co_r1_sheets.py` |
| `04-reports-spec/CO-DIAN-002-Formulario350-Spec.xlsx` | v1.1 | `co_r2_formulario350.py` / `co_r2_sheets.py` |
| `04-reports-spec/CO-PILA-003-AportesSeguridadSocial-Spec.xlsx` | v1.1 | `co_r3_pila.py` / `co_r3_sheets.py` |
| `04-reports-spec/CO-DIAN-004-Formulario220-Spec.xlsx` | v1.1 | `co_r4_formulario220.py` / `co_r4_sheets.py` |
| `04-reports-spec/CO-DIAN-005-Formato2276-Spec.xlsx` | v1.1 | `co_r5_formato2276.py` / `co_r5_sheets.py` |
| `04-reports-spec/CO-CESANTIAS-006-ConsignacionAnual-Spec.xlsx` | v1.1 | `co_r6_cesantias.py` / `co_r6_sheets.py` |

Every fix is applied **in the generator source**, never to the `.xlsx` by hand, so
a rebuild reproduces the aligned state exactly. Version Control sheets on all
seven files carry the v1.1 change-log entry.

## Authority order used to resolve every divergence

official government form / anexo técnico / XSD **>** CCG **>** web research.

Primary sources: DIAN Anexo Técnico Nómina Electrónica V1.0 (Res. DIAN 000013 de
2021) tables 5.1.1–5.5.8; PILA Anexo Técnico 2 (Res. MSPS 2388 de 2016, AT2
versión 09 of 16-09-2019); Formulario 350 (Res. DIAN 000031 de 2024); Formulario
220 + instructivo; Res. DIAN 000227 de 23-09-2025 (Formato 2276 v4); published
severance-savings (cesantías) XLS/PCSS layouts; Res. DIAN 000238 de 15-12-2025
(UVT 2026 = COP 52,374); Decreto 1469 de 2025 (SMMLV 2026 = COP 1,750,905).

---

## CHECK 1 — Option mapper code alignment (F1 prevention)

| Check | Field / Mapper | Issue Found | Fix Applied | File Patched |
|---|---|---|---|---|
| 1 | `Worker Type` code 40 | DD carried code 40 "Beneficiario UPC adicional". Anexo table 5.5.3 admits exactly sixteen codes (01 02 04 12 18 19 21 22 23 30 31 47 51 54 56 58); 40 is a PILA-only *tipo cotizante* for a health-coverage beneficiary, not an employee, and the mapper drives `Employee.Worker_Type_Code` → NIE041, a table-5.5.3 code. | Code 40 removed; recorded in the mapper's excluded-code list with the reason. | `co_dd_data_mappers.py` |
| 1 | `Employee Document Type` code 47 | Abbreviation read `PE`. Anexo table 5.2.1 prints **PEP**. `PE` is the PILA/SOI two-letter code — a different catalogue. | Abbreviation → `PEP`; the PILA two-letter equivalent moved to the Constraint/Notes and given its own mapper (below). | `co_dd_data_mappers.py` |
| 1 | `Worker Sub-Type` | Hard rule did not match the PILA anexo statutory list, and the dual catalogue was undocumented — DIAN table 5.5.4 admits only `00`/`01`, whereas PILA T2R2-006 runs 0–12 as a **single digit**. | Hard rule aligned to the PILA list (1, 2, 3, 4, 5, 6, 9, 12), the in-scope subset named separately, and the code-width trap recorded explicitly. | `co_dd_data_mappers.py` |
| 1 | **NEW** `Employee Document Type (PILA / Cesantías)` | `CD` and `SC` were named as valid in the numeric mapper's constraint (b) but had no row anywhere, so PILA T2R2-003 / T2R2-074 and CO-CESANTIAS-006 T03 had no complete code table. | New mapper carrying AT2 v09 campo 3 verbatim — CC CE TI PA CD SC RC PE — plus `PT`, scoped "cesantías XLS layout ONLY" (absent from the PILA fixed-width list, no DIAN numeric equivalent, CO-GAP-06). | `co_dd_data_mappers.py` |
| 1 | `Principal Contributor Document Type` (PILA T2R2-074) | **Wrong mapper attached.** The field pointed at `Employer Document Type` while its own Pre-Defined Format and notes both said it takes the PILA two-letter **contributor** catalogue. The two lists differ in exactly two places — the employer list carries `NI` and lacks `RC` — so the wrong mapper admitted a corporate NIT as a principal contributor's document type and rejected a *registro civil*, precisely the beneficiary case the field exists for. Spec T2R2-074 points at the same Sheet 6 table as T2R2-003. | Field re-pointed to `Employee Document Type (PILA / Cesantías)`; the employer mapper's own note, which had claimed T2R2-074 as a second referrer, corrected to say so and to name the two-code difference. | `co_dd_data_employment.py`, `co_dd_data_mappers.py` |
| 1 | `Tipo de trabajador` code 21 | Spec Sheet 6 abbreviation `EST-P` vs DD `EST-PG`. | Spec aligned to the DD abbreviation. | `co_r1_sheets.py` |
| 1 | `Clase de aportante` code D | Spec Sheet 6 abbreviation `LEY 1429` (with a space) vs DD `LEY1429`. | Spec aligned to the DD abbreviation. | `co_r3_sheets.py` |
| 1 / 4 | `PARENTESCO` (F220 casilla 82) | Spec Sheet 6 table did not carry the DD `Dependant Relationship` codes. | Code table rewritten to the DD codes (ET art. 387 dependant classes). | `co_r4_sheets.py` |

**Verified equal, no change needed** — all 36 DD mappers were cross-read against
every Sheet 6 section, not a sample. Reconciled exactly: Employee / Employer /
Legal-Representative / Dependant Document Type, Pay Frequency, Contract Type,
Payment Method, Payment Form, Class of Contributor, Occupational Risk Class,
Employer Status Action Type, Form of Presentation, PILA Filing Modality, PILA
Planilla Type, Employer Person Type, Employer Legal Nature, Contributor Type,
Formato 2276 Informant Type, Yes/No Indicator, Dependant Relationship,
Severance-Savings Fund, Treaty Status, Withholding Procedure.

Two apparent divergences were confirmed **correct as they stand**:

- `Worker Sub-Type` — DD holds 00/01/03/04/05/06/09 (two-digit, nómina
  electrónica convention) against PILA's single-digit 0–12. The DD is a
  documented in-scope subset: 02, 10 and 11/12 are independientes / taxi
  populations outside private-sector employment. The dual catalogue and the
  code-width trap are stated in the mapper note.
- `PILA Novedad (Change Event) Type` — DD splits 18 atomic codes where spec
  Sheet 6 groups rows (`TDE / TAE`, `TDP / TAP`, `VAC-LR`, `Correcciones A/C`).
  Same semantic content on both sides; both document the three-value VAC/LR
  flag and the two correction limbs.

## CHECK 2 — Field classification accuracy (F3 prevention)

| Check | Field / Mapper | Issue Found | Fix Applied | File Patched |
|---|---|---|---|---|
| 2 | `Contract.Contractual_Salary` → NIE062, T2R2-040, T12 | Flagged Payroll Field = **Y** in the specs, but it is an **amount**. The pipeline rule is explicit: basic/base salary amounts belong to the Wage Type Catalogue, not the Data Dictionary. The DD build already excluded it, so the two builds were out of lock-step. | The three spec rows now read **N**, and the mapping is removed from `_DD_MASTER_MAPPINGS`. The DD carries no such field, so the deviation is resolved at source rather than annotated. | `co_r1_nomina_electronica.py`, `co_r3_pila.py`, `co_r6_cesantias.py`, `build_co_specs.py` |
| 2 | calculated amounts under an `Employee.` prefix | Several computed amounts carried a master-data System Mapping namespace, which made column E unreadable as a classification. | Retagged to the `Payroll.` namespace so column E and the namespace agree on every one of the 563 fields. | `co_r1_nomina_electronica.py`, `co_r3_pila.py` |

Final state, swept over all 563 fields: **0** rows where E=N but the mapping is
`Employee.` / `Company.` / `Contract.`; **0** rows where E=Y but the mapping is
`Payroll.` / `SUM` / `COUNT` / `System.` / `Mercans.` / `PayPeriod.` /
`Constant`; **0** rows where E=Y on an Amount / Count / Rate value type. Column E
distribution 160 Y / 403 N. Every Payroll-Field=Y mapping resolves to a DD row.

## CHECK 3 — Mandatory / conditional flags and C16 bidirectionality (F13 prevention)

Mandatory distribution: 246 Y · 297 C · 20 N. **Every one of the 297 C fields
carries a conditional reason**, and none is a stub (shortest is 25+ characters).

| Check | Field / Mapper | Issue Found | Fix Applied | File Patched |
|---|---|---|---|---|
| 3 | 82 DD field notes | `Spec ref` citations were stale or incomplete — a systematic off-by-N drift across the NIE, A1 and T2R blocks. Examples: Hire Date cited `NIE057`, which does not exist (the anexo field is `NIE002` FechaIngreso); the whole PILA employer block `A1-011`–`A1-017` was displaced by one; Place of Work Municipality cited `NIE053`, which is the work *address* (municipality is `NIE052`). | All 82 citations re-derived from the System Mapping join; each now names the artefact, the field ID and the Mandatory flag per artefact. | `co_dd_data_employee.py`, `co_dd_data_employer.py`, `co_dd_data_employment.py` |
| 3 | DD notes citing artefacts in prose | Five notes named artefacts in prose with no field ID at all — "all four DIAN artefacts" (Employer NIT DV), "all four per-employee artefacts" (Employee Second Surname), "(CO-DIAN-001)" with no ID (Employer Municipality Code). | Rewritten to explicit per-artefact field IDs. | `co_dd_data_employer.py`, `co_dd_data_employee.py` |
| 3 | mapper notes | Same defect class inside the Option Mapper notes: `NIE055`→NIE041, `NIE056`→NIE042, `NIE059`→NIE061, `NIE060`→NIE029, `A1-001`→A1-002/T2R1-005, `A1-017`→A1-020, `A1-032`→A1-030/T2R1-021, cesantías `T02`→T09. | Corrected. | `co_dd_data_mappers.py` |
| 3 | **45 spec fields — C16 in the spec-internal direction** | The v2.4 C16 rule is symmetric: *if A's condition mentions B, then B's notes must mention A*. It had been enforced only in the direction **DD note → spec field ID**; the spec-internal direction was never tested. Sweeping all 563 fields for Mandatory=C rows whose conditional reason names another field on the same artefact — and accepting an ID **range** (`NIE206-NIE209`, `T2R2-036 to T2R2-039`) as a valid reverse reference — left 45 B-side fields with no reverse reference at all: **18 on CO-DIAN-001**, **27 on CO-PILA-003**. | Reverse references installed for all 45, as a keyed post-assembly `_apply_c16` pass so each sentence travels with its row and survives a rebuild. A conditional B-side field takes the sentence in its **Conditional Reason (col G)**; an unconditional one takes it in its **Explanation (col M)**, so a Mandatory=Y row never acquires a conditional reason. | `co_r1_nomina_electronica.py`, `co_r3_pila.py` |

The 45, by artefact:

- **CO-DIAN-001 (18)** — NIAE214, NIE003, NIE004, NIE005, NIE011, NIE030,
  NIE041, NIE061, NIE065, NIE066, NIE118, NIE146, NIE160, NIE168, NIE170,
  NIE187, NIE188, NIE189.
- **CO-PILA-003 (27)** — A1-007, A1-019, A1-024, A1-033, T2R1-008, T2R1-011,
  T2R1-012, T2R1-019, T2R2-003, T2R2-005, T2R2-006, T2R2-008, T2R2-009,
  T2R2-031, T2R2-033, T2R2-036, T2R2-039, T2R2-042, T2R2-043, T2R2-045,
  T2R2-046, T2R2-048, T2R2-049, T2R2-066, T2R2-068, T2R2-080, T2R2-097.

Substantive examples, not boilerplate: NIE118 (service bonus, salary) now
records that it pairs with NIE119 and that *the salary and non-salary portions
must never be summed into one*; T2R2-036/039 (day counts) now record that the
whole novedad block T2R2-015–T2R2-030 drives them, so a novedad reported without
a matching movement in the day counters is a reconciliation error; T2R2-005
(contributor type) now names each field its code gates — T2R2-009/010 blank for
type 40, T2R2-056/074 only for type 40, T2R2-096 only for part-time type 51,
T2R2-031 blank only where the type is not obliged to contribute to pension.

Final state: **350 conditional cross-reference pairs, 0 unreciprocated.**

## CHECK 4 — Option value completeness (F14 prevention)

| Check | Field / Mapper | Issue Found | Fix Applied | File Patched |
|---|---|---|---|---|
| 4 | PILA T2R2-003 → "Tipo documento cotizante" | Column O pointed at a Sheet 6 section that **did not exist**. This is the employee document type on the social-security channel and a Payroll Field = Y master-data field, so an absent code table is a hard gap. | Section built from AT2 v09 Registro Tipo 2 campo 3 verbatim: eight values with their DIAN numeric equivalents, the PA/CD alphanumeric rule, the PE 15-digit SOI rule, and the CD/SC "no DIAN equivalent" note. | `co_r3_sheets.py` |
| 4 | PILA A1-034 → "Ley 1429 de 2010" | Column O pointed at a non-existent section. | Section built (S/N election, Decreto 1074 de 2015 art. 2.2.2.42.1, plus the hard rule that A1-034=S with A1-007≠D is rejected by the operador). | `co_r3_sheets.py` |
| 4 | Formato 2276 document type (numerals 2 and 34) | Code table was a bare placeholder row. | Completed with the 11 DIAN numeric codes. | `co_r5_sheets.py` |
| 4 | geographic section (NIE) | Column O referenced "Países / Departamentos / Municipios", which did not resolve to the section header. | Section renamed so all three references resolve. | `co_r1_sheets.py` |
| 4 | overtime / surcharge type (NIE) | "Overtime / surcharge type" did not resolve. | Section renamed (table 5.5.5). | `co_r1_sheets.py` |
| 4 | PILA T2R1-002, cesantías E09 | Column O text did not match the "MODALIDAD DE LA PLANILLA" and "RESPUESTA A LA VALIDACION ASOFONDOS" headers. | References aligned to the headers. | `co_r3_sheets.py`, `co_r6_sheets.py` |

Final state: **563 of 563** non-empty column-O values resolve — every one of the
138 `-> Sheet 6:` pointers lands on a real section, and no code-table section is
left as a bare placeholder.

## CHECK 5 — Composite key documentation (F12 prevention)

| Check | Field / Mapper | Issue Found | Fix Applied | File Patched |
|---|---|---|---|---|
| 5 | F220 casilla 4 (certificate number) | Length > 8 with a concatenated example (`2026-000417`) and no Composite Key Structure. DIAN prescribes **no** structure here — the instructivo says the number is "asignado por la persona natural o jurídica que expide la certificación", i.e. the employer assigns it — so the series is Mercans-designed and had to be fixed and documented to be auditable. | Composite Key Structure documented: positions 1–4 = accrual year AAAA from `PayPeriod.Fiscal_Year` (the year earned, **not** the year of issue); position 5 = literal hyphen; positions 6–11 = six-digit zero-filled consecutive from `Mercans.Certificate_Sequence`, restarting each accrual year, unique per employer per year. **Persistence:** assigned once and never reused, including after a reissue — a corrected certificate takes the next consecutive and cites the superseded number, because ET art. 378 makes the employee's copy the evidential document and two certificates may not share a number. | `co_r4_formulario220.py` |

Verified already documented, no change needed: NIE012 (document number =
prefix + consecutive), NIE020, NIE024 (CUNE SHA-384), Formato 2276 N02 and N34,
cesantías E01 (employer document type + number) and T04.

Two candidates were examined and correctly need **no** composite documentation:
F350 casilla 4 is DIAN-assigned and opaque (the form prints *"Espacio reservado
para la DIAN"*, and DIAN publishes no breakdown — the contrast with F220 casilla
4 is recorded on both rows), and NIE025 is the fixed literal `CUNE-SHA384`, not
a key.

## CHECK 6 — Code prefix verification (F14 prevention)

| Check | Field / Mapper | Issue Found | Fix Applied | File Patched |
|---|---|---|---|---|
| 6 | `R()` builder | No mechanism existed to state a prefix pattern in column J; patterns lived only in Sheet 6 notes, which is not where a developer reads the format. | `R()` gained `fmt_extra`, appending the pattern to column J. | `co_r3_pila.py` |
| 6 | PILA administradora codes — T2R1-014, T2R2-031, T2R2-032, T2R2-033, T2R2-034, T2R2-035 | Column J stated only `A(6)`. | Pattern `^(ARL\|EPS\|EOC\|AFP\|CCF\|FSP)[0-9]{3}$` stated in column J — three alphabetic positions naming the subsystem, three numeric naming the administradora; verified against the PILA anexo, which names FSP001, MIN001 and MIN002 in running prose. | `co_r3_pila.py` |
| 6 | **PILA T2R2-077 (ARL of the member)** | **Missed by the first pass.** Carries example `ARL001` yet column J stated only `A(6)`, while all six sibling administradora fields stated the pattern. Found by sweeping every field whose example is a letter-prefixed code rather than checking a hardcoded list. | Same prefix pattern added. | `co_r3_pila.py` |
| 6 | **DD administradora fields (7)** | Employer ARL, Employee ARL, EPS, EPS Transfer, AFP, AFP Transfer and CCF stated only `A(6) - administradoras catalogue` in Pre-Defined Format while the specs stated the full six-position pattern — the two documents describing the same format differently. | The pattern is now carried on **both** sides. The severance-savings fund code is deliberately left at `N(2)`, being a different published catalogue. | `co_dd_data_employment.py`, `co_dd_data_employer.py` |
| 6 | F350 casilla 983 (professional card) | No pattern. | `^[0-9]{1,6}-T$` stated, with the note that the `-T` suffix is part of the identifier and must not be stripped, because the Junta Central de Contadores quotes the card with it. | `co_r2_formulario350.py` |
| 6 | NIE010 / NIE012 | Numbering prefix and document number had no stated pattern. | Prefix pattern stated in column J; NIE012's pattern stated alongside its composite key. | `co_r1_nomina_electronica.py` |

Final state: every prefixed administradora example states its pattern in column
J; **0** examples violate the regex their own column J states; the DD states the
same pattern on all 7 administradora fields.

---

## Verification

Two verifiers, both re-run against the rebuilt workbooks:

| Verifier | Coverage | Result |
|---|---|---|
| `_txt/align/verify_alignment.py` | Checks 1–6, 22 assertions | **0 failed** |
| `_txt/align/verify_c16_prefix.py` | C16 spec-internal direction over all 563 fields; full prefix sweep incl. the DD side | **0 failed** |
| `05-data-dictionary/_validate_co_dd.py` | DD structural conformance C1–C13 | **13 checks, 0 failures** |
| `_audit_v24_mechanical.py` (`CL_AUDIT_CODE=CO`) | mechanical v2.4 gate | 14 PASS · 2 MANUAL · 2 FAIL |

`verify_c16_prefix.py` was written for this stage because the first pass's
verifier hardcoded its Check 5 and Check 6 field lists and tested C16 in one
direction only — which is how T2R2-077 and the 45 unreciprocated pairs survived
it. The new verifier sweeps instead of sampling.

The two mechanical-audit FAILs are **C21 and C26**, both looking for the
placeholder sheet names `Unknown (EN)` / `Unknown (XX)` in
`XX_Compliance_Payslip_Generator.xlsx`. They concern `06-payslip`, are outside
this stage, and are the same known false positive recorded on TN / OM / CI. The
harness must be invoked with `CL_AUDIT_CODE=CO`; without it, `CODE` defaults to
`XX` and all path-based checks report the CCG and `scope_manifest.json` as
missing.

## Accepted by design — recorded rather than changed

1. **Twelve `Mandatory=Y` rows on CO-CESANTIAS-006 (T03, T04, T05, T07, T09,
   T10, T11, T12, T13, T14, IN01, IN02) carry text in column G.** These are deliberate
   C16 back-references ("T04 back-references this field", "see E09, which
   back-references this field") placed there by the first pass. The 45 reverse
   references added in this pass use column M for unconditional rows instead, to
   avoid putting a conditional reason on a non-conditional field. Two
   conventions therefore coexist in the pack. Left as-is: the mechanical audit's
   C12 checks header depth, not per-row column-G emptiness, and rewriting
   deliberate prior-pass text carries more risk than the cosmetic gain. Worth
   settling one way in a future revision of the standard.
2. **`Social Security Subsystem` and `PILA Novedad (Change Event) Type` remain
   reference-only mappers**, unreferenced by any DD field's Option Mapper column
   by design — they document transactional per-payrun values that gate
   master-data conditionality. `_validate_co_dd.py` C11 exempts exactly these
   two. The contributor document-type mapper is **no longer** in that category:
   it is now properly owned by `Principal Contributor Document Type`.
3. **`PT` (Permiso por Protección Temporal)** stays scoped "cesantías XLS layout
   ONLY" in the contributor mapper. It is absent from the PILA fixed-width list
   of AT2 v09 and has no DIAN numeric equivalent — carried as **CO-GAP-06**, not
   silently normalised to `PE`/47.

## Tooling written for this stage

Under `_txt/align/`:

`patch_lib.py` (adjacent-string-literal rewriter) · `patch_dd_notes.py`,
`patch_dd_notes2.py`, `patch_dd_notes3.py` (82 + 5 DD note citations) ·
`patch_dd_mappers.py` (Check 1) · `patch_specs.py`, `patch_specs2.py`
(Checks 1, 2, 4, 5, 6) · `patch_c16_reverse.py` (45 C16 reverse references) ·
`patch_versions.py` (change-log rows) · `verify_alignment.py`,
`verify_c16_prefix.py` (verification) · pre-patch source snapshots in
`_txt/align/backup/`.
