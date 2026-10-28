# 07 — QA Report: Colombia (CO), fiscal year 2026

## 0. Status update at recompilation — 28 October 2026 (read first)

The QA report below is the research-pass report of **27 August 2026**, kept unchanged as the history of the
build. Since then the artifacts went through the Drive lineage (CCG 1.1–1.4, WTC 1.2–1.6, DD 1.1–1.3, seven
Report Specs v1.0, SIR v1.1) and the audits of 22–26 October 2026. The table gives the **current** status
of each open item against the artifacts in force; where an item is not listed, no change was recorded.
"Pending validation" = the country hub carries the item as F6-20261027-CO-Cnn awaiting human validation.

| Item | Status on 28 Oct 2026 | Where (current artifact) |
|---|---|---|
| Q-2 monthly apportionment of the 790 / 1.340 UVT caps | **Still open** — 1/12 per month is market practice, kept as Mercans default | CCG v1.4 Module 6.1.1 ("Open item — monthly apportionment of annual caps") |
| Q-3 DIAN overtime-percentage enum | **Conflict between artifacts.** CCG v1.4 Module 4.4 says it is resolved by DIAN Concepto 013840 (int. 1568) of 1 Oct 2025 — report the statutory 80%/90%. CO-DIAN-001 Field Options row 65 still carries the annex values in `@Porcentaje` "until a written DIAN position". Not resolved here | `01-ccg.md` Module 4.4; `04-reports-spec.md` CO-DIAN-001 Field Options row 65 |
| Q-4 no document-type code for the PPT | **Still open** — code 47 used as proxy | CCG v1.4 Module 2.2; CO-DIAN-001 Payroll Scope Summary row 49 |
| Q-5 apprentices after Ley 2466 | **Advanced** — contract regulated by Decreto 0223 de 5 marzo 2026; PILA tipo cotizante 19 = "lectiva Ley 2466" from Aug 2025; base ≥ 1 SMMLV. The annex names no code for the productive phase after Aug 2025 | CCG v1.4 Module 4.1; CO-PILA-003 C12 / Field Options D99; specs Payroll Scope Summary "Apprentice" rows |
| Q-6 / Q-7 employer rate for incapacity days 1–2; 1-SMMLV floor | **Still open; artifacts diverge** — WTC 'Employer Sick Pay' OPEN ITEM 1 and 2 (default 66.67%, configurable); CCG v1.4 Module 8 applies the floor (C-543 de 2007) as a configurable default. Pending validation (hub C25) | `02-wtc.md` Employer Sick Pay; `01-ccg.md` Module 8 |
| Q-10 PILA record layout | **Closed for the layout** — CO-PILA-003 is field-level on Anexo Técnico 2 of Res. MSPS 2388/2016 (planilla and apprentice types re-checked against version 30 on 22 Oct 2026); pensioners in CO-PILA-007 (Anexo Técnico 3 v15). Institution code lists (EPS/AFP/ARL/CCF) are still not in the artifacts (published by the Ministry through the operators). Other v09-derived tables not confirmed against v30 (hub C16) | `04-reports-spec.md` CO-PILA-003, CO-PILA-007 |
| Q-11 Formato 2276 technical specification | **Still DERIVED** — element names derived; DIAN annex/XSD for 2276 v4 not obtained (hub C28) | `04-reports-spec.md` CO-DIAN-005 |
| Q-12 MinTrabajo disability-contract report | **Out of scope** (HR scope); not a spec gap (hub C29, pending validation) | CCG v1.4 Module 10.1 ("None (out of scope)") |
| Q-14 `AltoRiesgoPension` | **Closed in the CCG** — 26% total pension (16% + 10 points employer), Decreto-Ley 2090 de 2003 art. 5 | CCG v1.4 Module 5.1 |
| Q-19 hourly divisor (Circular 101 de 2025) | **Unchanged in substance** — 220 to 14 Jul 2026, 210 from 15 Jul 2026; Circular §5.1 "75%" treated as a residual error. Circular not re-read (hub C26, pending validation) | CCG v1.4 Module 4.4 |
| Q-21 transport allowance in the prestaciones base | CCG v1.4 Module 9.1 states the severance base "includes the transport allowance" citing CST art. 253; the article was not re-read (hub C31, pending validation) | CCG v1.4 Module 9.1; CO-CESANTIAS-006 |
| Q-23 Formulario 350 layout | **Closed for the layout** — casilla-level spec on the form prescribed by Res. DIAN 000031 de 2024 (portal entry; no upload file) | `04-reports-spec.md` CO-DIAN-002 |
| Q-24 pension reform Ley 2381/2024 | Not in force for 2026 (unchanged). CCG v1.4 dates entry into force at 1 Apr 2027 (Judgment C-264 of 25 Aug 2026, case D-15989) — **not confirmed in a primary source** (hub C24, pending validation) | CCG v1.4 Module 5.1 |
| D-1 ARL class IV maximum 6,060% | Unchanged | CCG v1.4 Module 5.1.1 (occupational-risk class table) |
| Further Technical Annex defects (SendBillSync vs SendNominaSync, `NumeroDocumento` xsd:integer, `SegundoApellido` required) | Recorded as alerts (hub C27, pending validation) | `03-sir.md` header |

**Other conflicts found in the current artifacts (pending validation, not resolved here):** SMMLV instrument
(hub C21); Res. 000227/2025 article numbers for the former Res. 13/2021 arts. 5 and 24 (hub C19); the art. 5
item list in CCG v1.4 Module 10.3 differs from the verbatim text in `06-payslip.md` §2.1; non-resident
withholding — CCG v1.4 Module 2.2 vs Module 6.2 and CO-DIAN-001 row 191 (hub C22); CO-DIAN-001 Population
Rules row 24 still describes the monthly cesantías deposit of Ley 2466 art. 64 par. 1 as "a configurable
engine option", while that option was taken out of CO-CESANTIAS-006 on 23 Oct 2026 because the
implementing decree is still a draft (hub C20).

---


**Build type:** from-scratch primary-source research. No pre-existing Colombia CCG, WTC or DD existed.
**Research date:** 27 August 2026. **Verdict: READY WITH DOCUMENTED GAPS.**

**Gate applied.** Where post-research confidence on a section fell below the 95% floor, it is marked
below-floor here **and in the section itself**, with what would close it. Fifteen open items are recorded;
one was closed on a second pass. This is not a clean pass and should not be read as one.

---

## 1. Per-section confidence summary

| Section | Confidence | Basis |
|---|---|---|
| **01-ccg** — fiscal year, currency, SMMLV, UVT, auxilio de transporte | **97%** | Gazette PDFs read directly (Decreto 0159 de 2026 — instrument now in conflict, see §0 and hub C21 — Decreto 1470 de 2025); UVT read by page render from the scanned Resolución DIAN 000238 de 15-12-2025 |
| **01-ccg** — social security rates and ceilings | **96%** | Ley 100 arts. 18, 20, 204; Ley 797/2003 art. 7; Ley 1122/2007 art. 10 read verbatim from the Senate compilation. One derivation gap: the 15,5% → 16% final half-point (Q-16) |
| **01-ccg** — ARL rates | **92%** | Two conflicting official texts found; resolved in favour of the original decree (Q-17) |
| **01-ccg** — parafiscales (CCF/SENA/ICBF) | **97%** | Ley 21 de 1982 arts. 9, 12, 17; Ley 89 de 1988 art. 1 read verbatim |
| **01-ccg** — ET art. 114-1 exoneration | **97%** | Read verbatim; one interpretive question on the measurement base (Q-18) |
| **01-ccg** — income-tax withholding (table, depuration, procedures) | **95%** | ET arts. 206, 336, 383, 385–388, 55, 56, 119, 126-1, 387-1 read verbatim; art. 383 table read from Ley 2010 de 2019 art. 42 itself; DIAN Concepto 015007 de 2023 read verbatim. Monthly apportionment of annual caps is DERIVED (Q-2) |
| **01-ccg** — working time, overtime, surcharges | **93%** | Ley 2466 de 2025 arts. 10–14 and CST arts. 160, 161, 168, 172–179 read verbatim; the **hourly divisor** rests on MinTrabajo Circular 101 de 2025 read via a compilation mirror (Q-19) |
| **01-ccg** — prestaciones sociales | **94%** | CST arts. 186–192, 227–233, 236, 249–254, 306–308 and Ley 52 de 1975 read verbatim; Ley 50/1990 art. 99 via secondary source (Q-20); auxilio de transporte in the prestaciones base is settled practice, not statute (Q-21) |
| **01-ccg** — termination | **97%** | CST arts. 64, 65, 66 read verbatim |
| **01-ccg** — benefits in kind | **93%** | CST arts. 128, 129 and ET arts. 387, 387-1, 126-1 read verbatim; the *absence* of a valuation schedule is an argued negative, not a retrieved statement |
| **01-ccg** — rounding (three regimes) | **95%** | Each rule read verbatim from its own instrument; ET art. 577 via secondary source (Q-22) |
| **01-ccg** — filing calendar | **93%** | PILA table verbatim from Decreto 1990/2016; Form 350 table via a model-mediated read of the DIAN normograma (Q-23) |
| **01-ccg** — pension reform status | **70%** — **BELOW FLOOR** | Suspension verbatim from Corte Constitucional Auto 841 de 2025; the 25 Aug 2026 ruling and the 1 Apr 2027 commencement are **press-reported only** (Q-24) |
| **02-wtc** — wage-type taxonomy and XSD mapping | **96%** | Element tree read directly from `NominaIndividualElectronicaXSDV1.0.6.xsd`; code tables from the 269-page Anexo Técnico |
| **02-wtc** — subjection matrix (SAL / IBC / PARAF / RTF / PREST) | **92%** | Each cell traced to a named article. The vacation-base composition and the auxilio-de-transporte treatment rest partly on settled practice (Q-21) |
| **02-wtc** — apprentices (`ApoyoSost`) | **45%** — **BELOW FLOOR** | Ley 2466 arts. 21–23 located but the implementing rules were not (Q-5) |
| **03-sir** — DIAN nómina electrónica (M2M) | **96%** | SOAP envelope, payload encoding, signature policy, CUNE and SoftwareSC formulae, environments, validation-rule taxonomy all read verbatim from the annex. Endpoint URL is not published (by design) |
| **03-sir** — Formulario 350 channel | **85%** — **BELOW FLOOR** | The *absence* of a published M2M filing API is an argued negative (Q-23) |
| **03-sir** — PILA channel | **70%** — **BELOW FLOOR** | Framework verbatim from Decreto 1990/2016; the operator interface and file layout were not retrieved (Q-10) |
| **03-sir** — exógena channel | **80%** — **BELOW FLOOR** | Legal basis and deadlines verbatim; upload mechanics not retrieved (Q-11) |
| **03-sir** — MinTrabajo disability report | **80%** — **BELOW FLOOR** | Obligation verbatim from Ley 2466 art. 15; portal module not identified (Q-12) |
| **04-reports-spec** — CO-RPT-001 nómina electrónica | **96%** | Full XSD + all chapter-5 code tables + rule taxonomy |
| **04-reports-spec** — CO-RPT-002 Formulario 350 | **60%** — **BELOW FLOOR** | Deadline table and form version verified; **field layout DERIVED** |
| **04-reports-spec** — CO-RPT-003 PILA | **55%** — **BELOW FLOOR** | Deadlines and rounding verified; **record layout not retrieved** — not usable to build a file |
| **04-reports-spec** — CO-RPT-004 Formulario 220 | **85%** — **BELOW FLOOR** | ET art. 379 statutory content verbatim; **form layout DERIVED** |
| **04-reports-spec** — CO-RPT-005 Formato 2276 v4 | **90%** — **BELOW FLOOR** | 36 fields and both deadline tables read verbatim from Res. 000227 de 2025; **technical encoding spec not retrieved** (Q-11) |
| **04-reports-spec** — CO-RPT-006 cesantías deposit | **30%** — **BELOW FLOOR** | No national standard format exists; per-fund interfaces |
| **04-reports-spec** — CO-RPT-007 MinTrabajo report | **25%** — **BELOW FLOOR** | Obligation known, format unknown |
| **05-data-dictionary** — employer and employee fields | **94%** | Derived from XSD `use="required"` attributes and the annex code tables — an unusually hard evidentiary base for a data dictionary |
| **05-data-dictionary** — NIT check digit | **97%** | Algorithm implemented and **verified against two known NIT/DV pairs** this session |
| **05-data-dictionary** — institution code lists (EPS/AFP/ARL/CCF/fondo) | **0%** — **NOT RETRIEVED** | Q-10 |
| **05-data-dictionary** — bank-entity codes | **0%** — **NOT RETRIEVED** | §5.5 of that file |
| **06-payslip** | **96%** | Res. 000013/2021 arts. 5, 24, 26 (formerly; now compiled in Res. 000227/2025, see §0) and Anexo §13.1 read verbatim; the **absence** of a CST payslip article is grep-tested |

---

## 2. What is solid

These are read-from-source and re-derived, and can be relied on:

1. **SMMLV 2026 = $1.750.905** and its unusual legal history — Decreto 1469 de 2025 (23%, +$327.405 over
   the 2025 figure of $1.423.500), its provisional suspension by the Consejo de Estado in nulidad
   11001-03-25-000-2026-00004-00, and the **transitory** re-fixing at the same amount by **Decreto 0159
   de 19 de febrero de 2026**. Both decrees' *DECRETA* sections were read from the gazette PDFs.
2. **Auxilio de transporte 2026 = $249.095** for employees up to 2 SMMLV — Decreto 1470 de 2025 art. 1,
   read verbatim, in force 1 January 2026, derogating Decreto 1573 de 2024.
3. **UVT 2026 = $52.374** — Resolución DIAN 000238 de 15-12-2025 art. 1. The PDF is a **scanned image
   with zero extractable text**; the value was confirmed by rendering page 2 at 200 dpi and reading it
   visually, including the *considerando* citing oficio 100152176-0707 of 18 November 2025.
4. **The art. 383 withholding table** — read from **Ley 2010 de 2019 art. 42** itself (the consolidated ET
   page renders the table as a collapsed element and does not expose it). All seven bands and all seven
   formula strings captured verbatim.
5. **The full nómina-electrónica contract** — XSD element tree with occurrence constraints and
   `use="required"` flags; all chapter-5 code tables; the SOAP 1.2 / `SendNominaSync` envelope; the
   base64-ZIP payload rule; the 500 KB and UTF-8 reject rules; XAdES-EPES with an ONAC-accredited
   certificate and `ClaimedRole ∈ {thirdparty, supplier}`; the CUNE and SoftwareSecurityCode SHA-384
   formulae; the two environments and their QR hosts.
6. **Formato 2276 v4's 36 fields and both deadline tables** — Resolución DIAN 000227 de 2025
   art. 1.3.7.1.1 and art. 1.3.9.1, read verbatim.
7. **The Ley 2466 de 2025 changes** — night window moved to 19:00 (art. 10, effective 6 months after the
   25 June 2025 sanction = 25 December 2025); 42-hour week (art. 11); overtime limit 2/day and 12/week
   (art. 13); dominical/festivo surcharge 80% / 90% / 100% by 1 July 2025 / 2026 / 2027 (art. 14);
   auxilio de conectividad (art. 53); the new CST art. 57 numerals and par. 4 (art. 15).
8. **PILA deadlines and rounding** — Decreto 1990 de 2016 arts. 1–2 read verbatim, including the uneven
   NIT-band widths and the round-**up**-to-100 rule.
9. **The exoneration** — ET art. 114-1 read verbatim, including the *"menos de diez"* comparator, the
   two-employee condition for natural persons, and par. 6's exclusion.
10. **The FSP is an INCRNGO** — argued from ET art. 55 and **corroborated by a primary source on the
    reporting side**: Res. 000227/2025 art. 1.3.7.1.1 field 24 groups *"aportes obligatorios a fondos de
    pensiones **y solidaridad pensional** a cargo del trabajador"* in one line.
11. **Colombia has no statutory payslip-content article** — grep-tested to **zero hits** across the full
    consolidated CST for seven distinct Colombian terms for a payslip, with Ley 2466 art. 15 read in full
    to confirm it added none.
12. **The NIT check-digit algorithm** — implemented and verified against two known NIT/DV pairs
    (902025831→4 and 800197268→4).
13. **The worked gross-to-net example** — every line arithmetically re-derived this session. Spot check:
    base gravable 5.460.000 = 104,2502 UVT; (5.460.000 − 95×52.374) × 19% = 484.470 × 19% =
    **92.049,30**; net 7.187.950,70; employer cost 11.068.466,67 → factor **1,3836**.

---

## 3. Defects found in official documents

Four discrepancies were found in government-published material. All were verified by direct reading, not
inferred.

### D-1 — Corrected: ARL class IV maximum is 6,060%, not 6,960%

| Source | Class IV maximum |
|---|---|
| **Decreto 1772 de 1994 art. 13**, as reproduced by the official government compilation at normograma.mintic.gov.co | **6,060%** |

An earlier draft of this pack misread the table and used 6,960% for class IV's maximum — that figure
is actually class V's *initial* value (see the full table: class IV = 1,740% / 4,350% / 6,060%
min/initial/max; class V = 3,219% / 6,960% / 8,700%). Verified directly against the government's own
compiled text of Decreto 1772 art. 13 (compiled into Decreto 1072 art. 2.2.4.3.5 without substantive
change — both sources now confirmed consistent at 6,060%). **Corrected value: 6,060%.** Recorded in
`01-ccg.md` §3.4.

### D-2 — The Anexo Técnico's CUNE worked example does not reproduce

Published inputs (annex §8.1.1.3): `NumNE=N00001`, `FecNE=2020-01-16`, `HorNE=10:53:10-05:00`,
`ValDev=3500000.00`, `ValDed=1000000.00`, `ValTolNE=2500000.00`, `NitNE=700085371`,
`DocEmp=800199436`, `TipoXML=102`, `Software-Pin=693`, `TipAmb=1`.
Published result:
`16560dc8956122e84ffb743c817fe7d494e058a44d9ca3fa4c234c268b4f766003253fbee7ea4af9682dd57210f3bac2`

**16 plausible readings were computed and none reproduces the published hash** — including the annex's
own printed *"Composición del CUNE"* string, which is itself internally inconsistent: it renders
`HorNE` as `1053:10-05:00`, one colon short of the stated input. Variants tested: both `HorNE` forms,
with and without the `.00` decimals, and both `Software-Pin`/`TipAmb` orderings.

**Consequence:** the annex example must **not** be used as a conformance test for CUNE generation.
Validate against the habilitación environment (`catalogo-vpfe-hab.dian.gov.co`) instead.

### D-3 — The Anexo Técnico's QR worked example carries an impossible date

Annex §13.1 prints `FecNIE: 2019-16-01`, which is not a valid date under any field ordering (month 16
does not exist; day 2019 does not exist). An editorial defect in the same family as D-2.

### D-4 — The Anexo Técnico's overtime-percentage enum is stale against the labour statute

See Q-3 below. Not strictly a transcription error — it is a document that has not been updated for a
subsequent statute — but it produces a live compliance contradiction and is recorded as a defect because
the annex's validation rules make the stale values **mandatory** (reject class).

---

## 4. Open items

### Q-1 — Monthly cap on the housing-loan interest deduction *(engine)*

**Status:** DERIVED. ET art. 119 caps the deduction at the equivalent of 1.000 UPAC, with an editor's
note "(Hoy 1.200 Uvt)" annually; ET art. 387 inciso 1 says only that *"la base de retención se disminuirá
**proporcionalmente en la forma que indique el reglamento**"*. The customary monthly cap of **100 UVT**
(2026: 5.237.400) is the market convention derived from that annual figure, but the specific DUR 1625
article prescribing 100 UVT/month was **not retrieved**.
**Confidence: ~80%.** **Would close it:** DUR 1625 de 2016 art. 1.2.4.1.7 (or its current equivalent) in
consolidated form, and/or Decreto 3750 de 1986 art. 5 as compiled.

### Q-2 — Monthly apportionment of the 790-UVT and 1.340-UVT annual caps *(engine)*

**Status:** DERIVED, and materially so. **DUR 1625 art. 1.2.4.1.6 par. 3** (as modified by Decreto 2231
de 2023 art. 9) was read verbatim and imposes **both** the 40% limit **and** the absolute **1.340 UVT
annual** limit on the withholding depuration — but **prescribes no monthly conversion**. The same is
true of the 790 UVT cap in ET art. 206 num. 10. The engine convention of dividing by 12
(→ 111,6667 UVT and 65,8333 UVT monthly, i.e. 5.848.430 and 3.447.955 in 2026) is a **derivation**.

Alternative readings that a Colombian practitioner could defend: cumulative year-to-date tracking
against the annual cap; or applying only the 40% limit monthly and reconciling the absolute cap in the
annual return. These produce **different monthly withholding** for high earners.
**Confidence: ~75%.** **Would close it:** a DIAN *concepto* addressing monthly apportionment of the
1.340 UVT cap in retención, or an amending decree.

### Q-3 — DIAN overtime-percentage enum vs the Ley 2466 dominical surcharge *(engine)* — **UNRESOLVED CONFLICT**

The *Anexo Técnico* §5.5.5 publishes a closed `Porcentaje` table whose dominical/festivo values
(codes 4, 5, 6, 7 = 100 / 75 / 150 / 110) encode the **pre-Ley-2466 75%** surcharge. The annex's
validation rules make the table mandatory — *"Se debe colocar el Porcentaje que corresponda de la
tabla 5.5.5"*, class **R** (reject). The statute now requires **80%** (Jan–Jun 2026) and **90%**
(Jul–Dec 2026), rising to 100% from 1 July 2027.

**Verified:** the annex is still at **version 1.0** — DIAN's own technical-documentation micro-site was
checked this session and lists no version newer than 1.0.

**Two possible engine postures, neither confirmed:**
- **(a)** Emit the true statutory percentage (e.g. `90.00`) and rely on the validator not enforcing the
  enum as a closed list. Risk: rejection of every affected document.
- **(b)** Emit the annex value (`75.00`) with the correct `@Pago` amount. Risk: the reported percentage
  contradicts the paid amount, exposing the employer on a UGPP or MinTrabajo review.

**Confidence that the conflict exists: ~95%. Confidence in either resolution: below 50%.**
**Would close it:** a DIAN *concepto* or an updated annex; or empirical testing against the habilitación
environment with each value.

### Q-4 — No document-type code for the PPT *(engine / master data)*

Annex §5.2.1 lists code **47 = PEP** (*Permiso Especial de Permanencia*) but has **no code for the PPT**
(*Permiso por Protección Temporal*), created by **Decreto 216 de 2021** — one month **after** the
11 February 2021 annex — and now held by the large majority of regularised Venezuelan migrants in
Colombia. The annex remains at version 1.0.
**Confidence that the gap exists: ~92%.** **Confidence in a workaround: none — no guidance located.**
**Would close it:** an updated annex, or a DIAN *concepto* on which existing code to use for PPT holders.

### Q-5 — Apprentices after Ley 2466 de 2025 art. 21 *(engine)* — **BELOW FLOOR, 45%**

Ley 2466 art. 21 rewrote **CST art. 81** on the *naturaleza y características de la relación de
aprendizaje*, restructuring it as a special labour contract, and art. 23 rewrote the *monetización de la
cuota de aprendizaje* (Ley 789 de 2002 art. 34). The full text of both articles was located, but their
interaction with the SENA regulations and Ley 789 de 2002 arts. 30 et seq. — specifically the *etapa
lectiva* and *etapa productiva* remuneration percentages and which of pensión / salud / ARL / CCF apply in
each stage for 2026 — was **not resolved**. The implementing decree was not retrieved.
**Do not configure apprentice payroll from this pack.**
**Would close it:** the implementing decree for Ley 2466 arts. 21–23, plus the current SENA
*contrato de aprendizaje* regulation.

### Q-6 — Rate for the employer's first two days of general-illness incapacity *(engine)*

**Verified:** the *allocation* is settled — employer days 1–2, EPS from day 3 (Decreto 2943 de 2013 art. 1,
compiled at Decreto 780/2016 art. 3.2.1.10, read verbatim). CST art. 227's rate of **2/3 (66,67%)** for
the first 90 days was also read verbatim.
**Not settled:** whether the employer's first two days are payable at **66,67%** or at **100%**. This is a
long-standing Colombian controversy with divided doctrine; neither position was traced to a primary
source this session.
**Confidence: ~70%** for the 66,67% position adopted in `01-ccg.md` §6.5 and `02-wtc.md` §5.1.
**Would close it:** a MinSalud or MinTrabajo *concepto*, or Corte Suprema / Consejo de Estado
jurisprudence on the point.

### Q-7 — Minimum-wage floor on incapacity payments *(engine)*

Whether an incapacity payment computed at 66,67% of a sub-1,5-SMMLV base must be **topped up to
1 SMMLV** was **not resolved** from a primary source. The rule is widely applied in practice.
**Confidence: not established.** **Would close it:** the relevant Decreto 780 de 2016 article or a
MinSalud *concepto*.

### Q-8 — Contributions during unpaid leave and contract suspension *(engine)*

Unpaid leave (`Licencias/LicenciaNR`) and contract suspension change the contribution picture — which
funds remain payable, on what base, and whether the employer or the employee bears them. Not resolved
from a primary source.
**Confidence: not established.** **Would close it:** Decreto 780 de 2016 Libro 2 on *novedades*, and the
PILA SLN (*suspensión / licencia no remunerada*) novedad rules in Resolución 2388 de 2016.

### Q-9 — Anexo Técnico worked examples (see D-2, D-3)

Recorded as defects above rather than as gaps in this pack. **No engine impact if the annex examples are
not used as conformance tests.**

### Q-10 — PILA record layout and institution code lists — **BELOW FLOOR, 55%**

**Resolución MinSalud 2388 de 2016** and its amendments — which prescribe the PILA *Tipo 1* / *Tipo 2*
record layout, field positions and lengths, the *tipo de aportante* / *clase de aportante* code values,
the EPS / AFP / ARL / CCF / fondo-de-cesantías institution code lists, and the *novedad* mnemonics
(ING, RET, TDE, TAE, VSP, SLN, IGE, LMA, VAC, IRL, …) — was **not retrieved this session**.
**Consequence:** `04-reports-spec.md` CO-RPT-003 **cannot be used to build a PILA file**, and
`05-data-dictionary.md` §4.1 has no code values. The *novedad* mnemonics listed in CO-RPT-003 are
practitioner knowledge, explicitly flagged as unverified.
**Would close it:** Resolución MinSalud 2388 de 2016 in current consolidated form with its annexes, plus
any licensed *operador de información*'s published technical specification.

### Q-11 — Formato 2276 v4 technical specification — **BELOW FLOOR, 70%**

The **field list** was read verbatim (36 fields, Res. 000227/2025 art. 1.3.7.1.1). The DIAN
*especificaciones técnicas* document giving the XSD, field lengths, decimal handling and the `Concepto`
code values within each numeral was **not retrieved**.
**Would close it:** the *Especificaciones técnicas Formato 2276 V4* PDF/XSD from the DIAN
*Presentación de Información por Envío de Archivos* micro-site.

### Q-12 — MinTrabajo disability-contract report — **BELOW FLOOR, 25%**

The obligation and the 15-day deadline are verbatim from Ley 2466 art. 15. The MinTrabajo portal module
and its field set were **not identified**; no implementing regulation was located.
**Would close it:** the MinTrabajo resolution or portal user guide for the *registro de contratos con
personas con discapacidad*.

### Q-13 — XSD type constraints that conflict with real-world data *(engine)*

Two structural problems in `NominaIndividualElectronicaXSDV1.0.6.xsd`, both read directly:

1. **`Trabajador/@NumeroDocumento` is typed `xsd:integer`.** Document types **21** (tarjeta de
   extranjería), **41** (pasaporte), **42** (documento de identificación extranjero) and **50** (NIT de
   otro país) routinely contain **letters**. Such a value **cannot be schema-valid**, and rule ZB01
   ("Fallo en el esquema XML del archivo") is class **R**. No workaround is published in the annex.
2. **`Trabajador/@SegundoApellido` is `use="required"`.** Many Colombians and virtually all foreign
   nationals have only one surname. An engine must emit a placeholder (a space, or a repeat of the first
   surname) or fail validation. No official guidance was located.

**Confidence that both constraints exist: ~97%** (read from the schema). **Confidence in a compliant
workaround: none.**
**Would close it:** a DIAN *concepto*, or observed behaviour of the habilitación validator.

### Q-14 — `AltoRiesgoPension` additional contribution *(engine)*

`Trabajador/@AltoRiesgoPension` is `use="required"` in the XSD, so the engine must carry the flag. The
**2026 additional employer pension contribution rate for high-risk activities and its base** were
**not verified this session**.
**Confidence: not established.** **Would close it:** Decreto 2090 de 2003 and its current amendments.

### Q-15 — Minimum QR print size — **CLOSED**

Initially unresolved; closed on a second pass. Anexo Técnico §13.1: *"El tamaño mínimo que debe tener el
código bidimensional QR es de **2cm** para facilitar la lectura por los diferentes dispositivos."*
**Confidence: ~95%.**

### Q-16 — The final half-point taking pension from 15,5% to 16%

**Ley 100 art. 20** (Ley 797/2003 art. 7) was read verbatim and sets 13,5% plus increments of 1% (2004),
0,5% (2005) and 0,5% (2006) = 15,5%, then authorises a further point from 2008 conditional on GDP growth.
**Ley 1122 de 2007 art. 10** was read verbatim and limits that further step to **0,5%**
(*"el cual sólo será incrementado por el Gobierno Nacional en cero punto cinco por ciento (0,5%)"*).
The enacting instrument — **Decreto 4982 de 2007** — was fetched but the retrieved page did **not**
contain a *DECRETA* section; the 16% figure and the 1 January 2008 effective date rest on that statutory
arithmetic plus secondary confirmation.
**Confidence in the 16% rate: ~96%** (it is universally applied and arithmetically forced by the two
statutes). **Confidence in the specific decree citation: ~85%.**
**Would close it:** the text of Decreto 4982 de 2007 from SUIN-Juriscol or the Diario Oficial.

### Q-17 — ARL class IV maximum (see D-1) — RESOLVED, verified externally

Corrected to **6,060%**, confirmed against the official government compilation (normograma.mintic.gov.co)
of Decreto 1772 art. 13. **Confidence: ~99%.** No longer an open item.

### Q-18 — What "devenguen" measures in ET art. 114-1 *(engine)*

The exoneration applies to employees who *"devenguen, individualmente considerados, **menos de diez (10)
salarios mínimos** mensuales legales vigentes"*. **Verified:** the comparator is strictly less than, and
the test is per employee per month. **Not fully settled:** whether "devengue" means the *salary* (basic +
salary-constituting payments), the *total devengado* including non-salary payments, or the *IBC*. The
three diverge for an employee with a large non-salary component or a variable month.
This pack applies it to the **salary-constituting devengado of the month**, which is the market
convention.
**Confidence: ~85%.** **Would close it:** a DIAN or UGPP *concepto* on the measurement base. Materially
important — the cliff is worth **~2,36 million pesos/month** at 10 SMMLV (see `01-ccg.md` §9 variant).

### Q-19 — MinTrabajo Circular Externa 101 de 2025: sourcing and legal weight *(engine)* — **BELOW FLOOR, 88%**

The **hourly divisor** (220 → 210) and the confirmed 80/90/100% dominical schedule come from
**Circular Externa 101 de 22 de septiembre de 2025**. Two caveats:

1. **Sourcing.** `mintrabajo.gov.co` was unreachable from this environment (`curl` returned HTTP 000);
   `cancilleria.gov.co`'s normogram returned **403**; `alcaldiabogota.gov.co` returned
   **ECONNREFUSED**. The circular's divisor table and recargo passages were therefore read from a
   third-party **legal-compilation mirror** (`normograma.com`), which reproduces the official text but is
   not the Ministry's own publication. The **235 / 230 / 220 / 210** progression it gives is internally
   consistent (weekly hours × 30 ÷ 6) and consistent with Ley 2101 art. 3, which raises confidence.
2. **Legal weight.** A *circular externa* is **administrative doctrine**, not a decree. Part of Colombian
   doctrine still defends the legacy divisor **240**. Ley 2101 art. 4 (*"…ni el valor de la hora
   ordinaria de trabajo"*) is the pivot: reducing the divisor **raises** the hourly value, which is the
   reading favourable to the employee and therefore the one an inspector will apply. But the point is
   **judicially untested**.

**Engine impact: large.** Every overtime and surcharge amount changes by 220/210 ≈ 4,8% at the
15 July 2026 cut-over, and by 240/210 ≈ 14,3% against the legacy divisor.
**Would close it:** the circular PDF from `mintrabajo.gov.co` directly, plus any judicial ruling.

### Q-20 — Ley 50 de 1990 art. 99 sourcing

The cesantías annual regime — 31 December liquidation, deposit *"antes del 15 de febrero"*, penalty of
one day's salary per day of delay — was read from **secondary sources** (a Consejo de Estado / tribunal
judgment summary and practitioner material). Direct fetches of the Senate and Función Pública texts of
Ley 50 de 1990 **failed** (HTTP 000 / certificate error). The **14 February** deadline and the penalty are
universally applied and are quoted consistently across the secondary sources.
**Confidence: ~88%** — **BELOW FLOOR.** **Would close it:** the text of Ley 50 de 1990 art. 99 from
secretariasenado.gov.co or the Diario Oficial.

### Q-21 — Auxilio de transporte in the prestaciones base, and the vacation base *(engine)*

**Verified:** the auxilio de transporte is **non-salary** (Decreto 1470 de 2025 recitals; Ley 15 de 1959),
and it is therefore **outside the IBC and the parafiscal base**.
**Settled practice, not statute:** that it **is** part of the base for prima de servicios, cesantías and
intereses a las cesantías, and **is not** part of the base for vacaciones. No article was found stating
either proposition directly; the inference runs through CST arts. 253 and 306 (which speak of *salario*)
plus long-standing jurisprudence and MinTrabajo doctrine that treats the allowance as part of the
*prestaciones* base by way of Ley 15 de 1959's purpose.
Ley 2466 art. 53 provides indirect statutory support: for the **auxilio de conectividad** it says
expressly *"será base de liquidación de prestaciones sociales"*, and that allowance is defined as
*"equivalente al auxilio de transporte vigente"* and *"en reemplazo"* of it.
**Confidence: ~90%** — **BELOW FLOOR.** **Would close it:** the relevant Corte Suprema de Justicia,
Sala de Casación Laboral judgment, or a MinTrabajo *concepto*.

### Q-22 — ET art. 577 sourcing

The nearest-multiple-of-1.000 rounding rule for tax return forms was read from a **secondary source**
reproducing the article text; the consolidated ET pages retrieved this session did not include
art. 577's range.
**Confidence: ~90%** — **BELOW FLOOR.** **Would close it:** the ET article from
secretariasenado.gov.co or the DIAN normogram.

### Q-23 — Formulario 350: deadline table sourcing and channel

**Deadline table:** obtained via **WebFetch**, i.e. a model-mediated read of the DIAN normogram page for
Decreto 2229 de 2023, not a raw text extraction. The ten rows (last NIT digit 1→7th business day
through 0→16th business day) are internally consistent and consistent with the DIAN 2026 calendar press
release (*Comunicado No. 128* of 26 December 2025), which confirms the same 7th-to-16th business-day
pattern for other obligations. **Confidence: ~90%.**
**Channel:** the assertion that there is **no published M2M filing API** for Form 350 is an argued
negative — DIAN publishes web-service contracts for the *sistema de facturación electrónica* family and
none for declaration forms. **Confidence: ~85%** — **BELOW FLOOR.**
**Field layout:** **DERIVED at ~60%.** Resolución DIAN 000031 de 2024's form annex was not retrieved.
**Would close it:** the Resolución DIAN 000031 de 2024 annex with the prescribed form image, plus the
DIAN electronic-filing technical specification for Form 350.

### Q-24 — Pension reform Ley 2381 de 2024 — **BELOW FLOOR, 70%**

**Verified from the Court's own document:** Auto 841 de 2025 found a *consecutividad* defect in the
Cámara de Representantes session of 14 June 2024, held it **subsanable**, **suspended** the law's entry
into force (originally 1 July 2025) and returned it to the Cámara.
**Press-reported only:** that on **25 August 2026** the Court upheld the bulk of the law (reported 7–1),
returned around ten provisions to the Cámara, and **set the entry into force of the approved provisions
at 1 April 2027**. The *sentencia* was not published in the Court's *relatoria* at research time;
repeated attempts to locate the corresponding *comunicado de prensa* (probing plausible URLs for
comunicados 27–30 of August 2026) all failed.

**What this does and does not affect.** It does **not** affect any 2026 payroll figure — the Ley 100
architecture (16%, 12%/4%, FSP, 25-SMMLV ceiling, RPM/RAIS election) governs throughout 2026, and that
is stated at high confidence. It **does** mean the **1 April 2027 date must not be hard-coded**.
**Would close it:** the published *sentencia* and *comunicado de prensa* from
corteconstitucional.gov.co.

---

## 5. Items with no primary source found at all

Named plainly, not papered over:

| Item | Status |
|---|---|
| **PILA record layout** (Resolución MinSalud 2388 de 2016 and amendments) | Not retrieved. Blocks building a PILA file. Q-10 |
| **EPS / AFP / ARL / CCF / fondo-de-cesantías institution code lists** | Not retrieved. Q-10 |
| **PILA `tipo de aportante` / `clase de aportante` code values** | Not retrieved. Q-10 |
| **PILA *novedad* mnemonics** | Practitioner knowledge only, explicitly unverified. Q-10 |
| **ACH Colombia / Superintendencia Financiera bank-entity code catalogue** | Not retrieved. Needed only for the payment file, not for any statutory filing |
| **Formulario 350 form image and electronic-filing layout** | Not retrieved. Q-23 |
| **Formulario 220 form image** (Resolución DIAN 000022 de 2024 annex) | Not retrieved. Q-4 in `04-reports-spec.md` |
| **Formato 2276 v4 technical specification / XSD** | Not retrieved. Q-11 |
| **Nómina-electrónica web-service endpoint URL** | **Not public by design** — annex §14.5 states it is exposed in the participant catalogue after habilitación. Not a research failure |
| **DIAN signature-policy `Identifier` value** | Rules DC50/DC51 require "the identifier defined by DIAN" without printing it. Obtained at habilitación |
| **`AltoRiesgoPension` 2026 rate and base** (Decreto 2090 de 2003 as amended) | Not retrieved. Q-14 |
| **Ley 776 de 2002 art. 3** — the 100% rate for occupational-incapacity temporary benefits | Not read. Stated at ~85% in `02-wtc.md` §5.1 |
| **Apprentice remuneration and contribution rules after Ley 2466 arts. 21–23** | Implementing decree not retrieved. Q-5 |
| **MinTrabajo disability-report portal field set** | Not identified. Q-12 |
| **Sectoral or collective-agreement payslip requirements** | **Not searched.** Colombian *convenciones colectivas* can impose payslip content contractually; none would be nationally applicable |

---

## 6. Environment and technique notes (for the next Colombia pass)

Recorded because they cost time this session and will recur.

1. **`curl` fails on several Colombian government hosts from this environment.** `mintrabajo.gov.co`
   returned HTTP 000; `secretariasenado.gov.co` returned HTTP 000 on a direct fetch (though its
   already-downloaded pages in `_co_sources/` work fine). `funcionpublica.gov.co`'s
   `gestornormativo/norma.php?i=NNN` endpoint returns a **13.097-byte error page** for many valid IDs —
   detect that exact size as a failure signal rather than parsing it.
   `alcaldiabogota.gov.co` → ECONNREFUSED. `cancilleria.gov.co` normogram → **403**.
   **Working alternatives:** `normograma.dian.gov.co` (DIAN's own compilation, reliable),
   `normograma.com` mirrors, `dian.gov.co/normatividad/Normatividad/...` for resolution PDFs, and
   `WebFetch` where `curl` fails.
2. **Several official Colombian PDFs are scanned images with zero text layer** — including
   **Resolución DIAN 000238 de 2025** (the UVT resolution) and the minimum-wage/auxilio decrees in part.
   `pdftotext` yields 2 bytes. **`pdftoppm` is not installed** in this environment. Use
   **PyMuPDF `page.get_pixmap(dpi=200).save(...)`** and then read the PNG with the Read tool — this
   worked first time and is the only way the UVT was confirmed from its own instrument.
3. **Set `PYTHONIOENCODING=utf-8` for every Python invocation.** The Windows console defaults to cp1252
   and any Spanish accent or U+FFFD replacement character raises `UnicodeEncodeError` mid-script.
4. **The Senate's consolidated ET renders the art. 383 table inside a collapsed element** that is not in
   the fetched HTML. Go to the amending law instead — **Ley 2010 de 2019 art. 42** carries the table
   inline as a real HTML `<table>`.
5. **The 269-page Anexo Técnico is multi-column and `pdftotext` scrambles it badly** (validation-rule
   tables interleave across columns). **PyMuPDF `page.get_text()` per page is clean**, and the code
   tables of chapter 5 live on printed pages 178–181 = PDF pages 177–180.
6. **Use the Write tool, not heredocs, for the reference files.** Colombian legal text is dense in
   `$`, `"`, `«»` and accented characters; a heredoc quoting failure mid-write loses the section.

---

## 7. Verdict

**READY WITH DOCUMENTED GAPS.**

The pack is usable today for: gross-to-net calculation, the wage-type catalogue, employer cost, the
income-tax withholding engine, the nómina-electrónica integration (the deepest and most technically
specified of the three channels), the payslip, and the master-data model.

It is **not** usable today for: **building a PILA file** (Q-10 — no record layout, no institution codes),
**building a Formulario 350 electronic filing** (Q-23 — no form layout), **configuring apprentice
payroll** (Q-5), or **configuring high-risk pension activities** (Q-14).

Two items would materially change calculated amounts if resolved against this pack's position and should
be treated as live risks, not settled facts: **Q-19** (the 210 hourly divisor — administrative doctrine,
read from a mirror, judicially untested) and **Q-3** (the stale DIAN overtime-percentage enum — a genuine
contradiction between the labour statute and a mandatory tax-filing enum, with no defensible resolution
found).
