# Pre-Submission Audit — Colombia v2.4

**Overall verdict:** READY_FOR_HANDOVER

**Date:** 7 September 2026
**Auditor:** Pre-Submission Audit Gate (content review)
**Country code:** CO · **Currency:** COP · **Local language:** ES · **Fiscal year:** 2026

---

## Mechanical audit raw result

| Run | Command | PASS | MANUAL | FAIL | Overall |
|---|---|---|---|---|---|
| Original (`logs/audit_v24_mechanical.json`) | `python _audit_v24_mechanical.py` | 12 | 3 | 3 | **BLOCKED** |
| Re-check (`logs/audit_v24_recheck.json`) | same, after fixes | **16** | **2** | **0** | **READY_FOR_HANDOVER** |

The three original FAILs (C12, C20, C29) were all investigated at the artifact level and all three
proved to be **matcher defects in the shared audit harness, not artifact defects**. Two of them
(C12 = F25, C20 = F24) are already-logged shared-harness bugs now reproduced on a sixth country.
The third (C29) is a new regression of the previously-fixed Spanish-`todo` defect. One of the three
MANUALs (C33) was likewise a matcher defect, but investigating it surfaced **one genuine content
defect in the CCG**, which was fixed.

> **Interpreter / environment note.** The audit must be run with `python` (has `python-docx` 1.2.0 +
> `openpyxl`), not `python3`, and requires the country environment to be injected:
> ```
> CL_AUDIT_CODE=CO CL_AUDIT_COUNTRY=Colombia CL_AUDIT_LOCAL_LANG_SHORT=ES \
> CL_AUDIT_CURRENCY=COP python _audit_v24_mechanical.py
> ```
> Run bare, `CODE` defaults to `XX` and every artifact check reports "missing" — a false BLOCKED.
> This is the same interpreter mismatch logged on BH/OM/TN/CI.

---

## Artifacts produced

| Artifact | File | Size |
|---|---|---|
| CCG | `01-ccg/CO-CCG-001-v1.0.docx` | 279 KB |
| CCG source modules | `01-ccg/modules/m01…m13*.md` | 13 files, 442 KB |
| WTC | `02-wtc/CO-WTC-001-v1.0.xlsx` | 300 KB |
| SIR index | `03-statutory-integrations/CO-SIR-INDEX-001-v1.0.docx` | 40 KB |
| Integration landscape | `03-statutory-integrations/integration-landscape.json` | 35 KB |
| Integration runbook | `03-statutory-integrations/DIAN-NE/` (P1–P7 + interlinkages + effort estimates) | 10 files, 86 KB |
| Report Specs | `04-reports-spec/` | 6 files, 425 KB |
| DD | `05-data-dictionary/CO-DD-001-v1.0.xlsx` | 551 KB |
| DD classification | `05-data-dictionary/CO-DD-001-classification.md` | 31 KB |
| Payslip | `06-payslip/CO_Compliance_Payslip_Generator.xlsx` | 492 KB |
| QA cross-check | `07-qa-crosscheck/` (alignment patch, payslip verification, scope validation) | 3 files, 60 KB |

### Report spec inventory (6 in-scope filings, all specced)

| Filing ID | Spec file | Rows |
|---|---|---|
| CO-DIAN-NE-MONTHLY-001 | `CO-DIAN-001-NominaElectronica-Spec.xlsx` | 225 |
| CO-DIAN-F350-MONTHLY-002 | `CO-DIAN-002-Formulario350-Spec.xlsx` | 69 |
| CO-PILA-MONTHLY-003 | `CO-PILA-003-AportesSeguridadSocial-Spec.xlsx` | 170 |
| CO-DIAN-F220-ANNUAL-004 | `CO-DIAN-004-Formulario220-Spec.xlsx` | 75 |
| CO-DIAN-EXO2276-ANNUAL-005 | `CO-DIAN-005-Formato2276-Spec.xlsx` | 50 |
| CO-CESANTIAS-DEPOSIT-ANNUAL-006 | `CO-CESANTIAS-006-ConsignacionAnual-Spec.xlsx` | 52 |

7 further filings are descoped in `scope_manifest.json`, each with a written reason
(MinTrabajo disability report, SENA apprentice quota, RUAF novedades — all HR-scope; PILA planillas
T/F and I/Y — out-of-scope employment types; ICA withholding — not a payroll filing; Form 110 —
employee obligation, not employer).

### Integration coverage

Exactly one authority is a genuine machine-to-machine channel, so exactly one 7-phase runbook exists.
This is by design, not a gap:

| Authority | Channel | Integration | Runbook | Filings carried |
|---|---|---|---|---|
| DIAN-NE | SOAP 1.2 web service (`SendNominaSync`) | **Yes (M2M)** | `DIAN-NE/` P1–P7 | 001 |
| DIAN-MUISCA | Portal round-trip | No | n/a | 002, 004, 005 |
| PILA-OI | Licensed intermediary portal / file upload | No | n/a | 003 |
| FONDOS-CESANTIAS | Licensed intermediary portal / file upload | No | n/a | 006 |

The M2M verdict was verified live on 4 September 2026, not inferred: both the production
(`vpfe.dian.gov.co`) and habilitación (`vpfe-hab.dian.gov.co`) WSDLs returned HTTP 200 unauthenticated
and both declare `wsdl:operation name="SendNominaSync"`.

---

## Audit results (C1–C33)

| Check | Original | Final | Detail (final) |
|---|---|---|---|
| C1 — CCG structural completeness | PASS | PASS | 13 modules |
| C8 — Open-item resolution (CCG) | PASS | PASS | No open-item markers |
| C11 — CCG question coverage | PASS | PASS | 96/96 (100%) |
| C12 — Spec column schema depth | **FAIL** | **PASS** | All 6 specs adequate — 13/16 keywords each, 21 columns |
| C20 — Scope decision audit trail | **FAIL** | **PASS** | 6 in-scope all specced, 7 descoped with reasons |
| C21 — Payslip 8-sheet structure | PASS | PASS | All 8 sheets present |
| C22 — Payslip spec depth | PASS | PASS | All sections, 62 rows |
| C23 — XML/XSD justification | PASS | PASS | No unsupported XML in specs |
| C24 — Portal/institution labels | PASS | PASS | Consistent |
| C25 — Sample-file fabrication guard | MANUAL | MANUAL | Dispositioned below — verified genuine |
| C26 — Payslip formula + currency hygiene | PASS | PASS | 8-sheet + currency format OK |
| C27 — System Mapping → DD traceability | MANUAL | MANUAL | 476 → 230, all derived/structural; dispositioned below |
| C28 — Zero-minor-unit currency rule | PASS | PASS | COP has a minor unit — rule N/A |
| C29 — Residual-marker lint (all artifacts) | **FAIL** | **PASS** | No residual markers |
| C30 — Source-tier flag | PASS | PASS | No tier-3 aggregator sources |
| C31 — Resident / non-resident treatment | PASS | PASS | Both present |
| C32 — Cross-artifact fact consistency | PASS | PASS | No `[[FACT:]]` tags (country pre-dates tagging) |
| C33 — CCG English-only prose | MANUAL | **PASS** | English-only; 1 genuine defect found and fixed |

---

## False positives identified

### C12 override — merged title banner on row 1 (known bug **F25**, 6th country)

C12 reported `6/6 specs have thin schema` with 0–1/16 keywords. Manual inspection: every spec's
Field Specification sheet carries a **merged single-cell title banner on row 1** and the real column
headers on **row 2**. `check_c12` read only `next(spec_sheet.iter_rows(max_row=1))`, so it scanned the
banner and matched nothing.

Evidence — `CO-PILA-003-AportesSeguridadSocial-Spec.xlsx`, sheet `PILA Spec`, dimensions `A1:U170`:

- **Row 1** (1 cell): `"Integrated Contribution Settlement Return (PILA) — social security and payroll levies - Planilla Integrada de Liquidacion de Aportes (PILA)"`
- **Row 2** (21 cells): `Field Name (EN)` · `Field Name (Local ES)` · `Record Type` · `Field Position` ·
  `Payroll Field (Y/N)` · `Mandatory (Y/N/C)` · `Conditional Reason` · `Position (in file)` · `Length` ·
  `Format` · `Example` · `System Mapping` · `Explanation` · `Relevant for Payroll (Y/N)` · `Option Values` ·
  `Rounding` · `Negative (Y/N)` · `Value Type` · `Frequency` · `Query to RA` · `RA Comments`

Row 2 scores **13/16** keywords against the standard schema — above the 12 threshold — for all six
specs. The 3 unmatched keywords are labelling differences, not missing columns: the specs use
`Query to RA` / `RA Comments` instead of `Error Code` / `Error Message`, and `Option Values` instead of
`Code Table`. The 21-column standard schema is fully present. This is exactly the defect logged as
F25 on Oman and reproduced on TN, CI and CG.

### C20 override — spec-traceability matcher (known bug **F24**, 6th country)

C20 reported all six in-scope filings as `In-scope without spec`. All six specs exist and pass C12.
`check_c20` tested `filing_id.lower().replace(' ','')` as a substring of a spec filename with `_` and
`-` stripped — it strips separators from the filename but **not** from the filing ID, so a dashed
semantic ID can never match a dash-stripped filename, and the word order is transposed besides
(`NE-MONTHLY-001` vs `001-NominaElectronica`).

`scope_manifest.json` already carries an explicit `spec_file` link on every in-scope filing, and all
six resolve on disk (verified):

```
CO-DIAN-NE-MONTHLY-001          -> CO-DIAN-001-NominaElectronica-Spec.xlsx        exists=True
CO-DIAN-F350-MONTHLY-002        -> CO-DIAN-002-Formulario350-Spec.xlsx            exists=True
CO-PILA-MONTHLY-003             -> CO-PILA-003-AportesSeguridadSocial-Spec.xlsx   exists=True
CO-DIAN-F220-ANNUAL-004         -> CO-DIAN-004-Formulario220-Spec.xlsx            exists=True
CO-DIAN-EXO2276-ANNUAL-005      -> CO-DIAN-005-Formato2276-Spec.xlsx              exists=True
CO-CESANTIAS-DEPOSIT-ANNUAL-006 -> CO-CESANTIAS-006-ConsignacionAnual-Spec.xlsx   exists=True
```

All 7 out-of-scope filings carry a `descoping_reason`. Pure naming-convention false negative.

### C29 override — the Spanish word *todo*, not an English TODO marker

C29 reported `CO-WTC-001-v1.0.xlsx[Wage Type Catalogue]: \bTODO\b`. Manual inspection: **29 cells,
every one of them the ordinary Spanish word `todo`/`Todo`** inside quoted statutory text. Exact case
forms found: `todo` ×27, `Todo` ×2 — **zero** uppercase `TODO`. `check_c29` matches with
`re.IGNORECASE`, so the Spanish word is unavoidably caught.

The six distinct contexts, all quoted statute:

| Occurrences | Context | Source |
|---|---|---|
| 24 | *"…debe valorarse expresamente en **todo** contrato de trabajo"* | Labour Code art. 129 (salary in kind) |
| 1 | *"…en reemplazo del auxilio de transporte. En **todo** caso, los teletrabajadores…"* | Law 1221 of 2008 (telework) |
| 1 | *"…el salario en especie debe valorarse expresamente en **todo** contrato de trabajo."* | Labour Code art. 129 |
| 1 | *"**Todo** empleador que habitualmente ocupe uno (1) o …"* | Law 11 of 1984 art. 7 |
| 1 | *"…provides that 'en **todo** caso la base de cotizacion debe ser…'"* | Decree 1072 of 2015 art. 2.2.6.3.3.4 par. 2 |
| 1 | *"**Todo** empleador que se afilie por primera vez al S…"* | occupational-risk affiliation |

This is the same defect the harness docstring says was already fixed for C8 ("C8 uses word-boundary
regex (no false positive on Spanish 'todo' etc.)") — C29, added later in v2.8, reintroduced it by
adding `re.IGNORECASE`. It is the Chile v2.4 precedent recurring.

### C33 override — mathematical and typographic symbols misread as non-Latin script

C33 flagged 158 CCG passages as "possible local-language passage". Every flagged sample was a fully
English sentence. Root cause: the detector excludes only a hand-written list of punctuation, so any
symbol outside that list is treated as foreign script. Character-level analysis of all
**7,292 CCG prose strings** shows the 170 flagged strings are triggered by exactly nine characters,
**all of them mathematical or typographic**:

| Char | Codepoint | Name | Hits |
|---|---|---|---|
| → | U+2192 | RIGHTWARDS ARROW | 87 |
| − | U+2212 | MINUS SIGN | 33 |
| § | U+00A7 | SECTION SIGN | 31 |
| ≤ | U+2264 | LESS-THAN OR EQUAL TO | 29 |
| · | U+00B7 | MIDDLE DOT | 27 |
| ≥ | U+2265 | GREATER-THAN OR EQUAL TO | 19 |
| ± | U+00B1 | PLUS-MINUS SIGN | 3 |
| Σ | U+03A3 | GREEK CAPITAL LETTER SIGMA | 1 |
| ≈ | U+2248 | ALMOST EQUAL TO | 1 |

Not one is a letter in any language. They appear in legitimate English prose such as
`"NIT 902025831 → DV 4"`, `"the Technical Annex §1.1.1.1"`, `"round half to even, with a ±2.00 tolerance"`,
and the NIT check-digit formula `S = Σ (digit_i × W_i)`.

**Independently confirmed no leakage exists.** C33's own curated Spanish function-word branch never
runs on these strings (the code `continue`s after a non-Latin hit), so it was executed separately over
all 7,292 strings: **0 hits**. A second, much broader scan with ~90 Spanish function and payroll words
returned 16 candidates, all of which are English sentences caught on English/Spanish cognates
("social", "pension", "literal") or on retained terms of art. Spot-checks confirm the B10 citation form
is followed — *"the integrated contribution return (Planilla Integrada de Liquidación de Aportes, PILA)"*,
*"the statutory service bonus (prima de servicios)"*, *"Unpaid leave (licencia no remunerada)"*.

**No translation was required.** Per the audit instruction, a hit that is only a proper noun or an
already-parenthesised citation is recorded as an override, not "translated". One genuine exception was
found and is recorded under Real fixes below.

### C25 disposition — sample file verified genuine, not fabricated

C25 flagged `CO-DIAN-001-NominaElectronica-Spec.xlsx` because its `Sample File` sheet contains XML
while `00-official-sources/sample-files/` is empty. The check only looks in that one directory; the
official DIAN Technical Annex **is** on disk at
`00-official-sources/pdfs/AnexoTecnico-NominaElectronica-V1.0.pdf` (extracted to `_txt/ne_anexo.txt`,
557,807 characters). Verified against it:

- The sheet **self-declares its provenance in a "PROVENANCE NOTE — READ FIRST" block**, stating that
  the SOAP envelopes are quoted verbatim from Anexo Técnico v1.0 §9.5 and §9.7.2, that the XML instance
  is *constructed* from the annex's own XPath inventory, that **DIAN publishes no sample instance**, and
  that it is therefore *"a faithful reconstruction of the documented structure — NOT an official DIAN
  sample"*, to be validated against XSD v1.0.6 in habilitación before use.
- The SOAP terms all occur in the annex text: `SendNominaSync` ×13, `wcf.dian.colombia` ×7,
  `IWcfDianCustomerServices` ×2, `contentFile` ×4, `soap-envelope` ×5, `ApplicationResponse` ×40.
- **All 29 distinct XML element names in the constructed instance are traceable to the annex.** A
  first pass matched 28/29; the lone miss, `LugarGeneracionXML`, is present as NIE013 but was split
  across lines by the PDF's column layout (`LugarGeneracionXM` / `L`), with the XPath
  `/NominaIndividual/LugarGeneracionXML` intact in the annex.

Nothing is fabricated, and the artifact does not overclaim. **MANUAL retained** — this is the check
working as designed (a human confirms), and the disposition is now recorded.

### C27 disposition — dotted identifiers vs prose DD field names

C27 flagged 476 System Mapping values as needing a DD link. Column L **is** `System Mapping`, so the
check reads the right column, but it compares by substring: it requires a whole DD cell string (>4
chars) to appear inside the mapping text. DD fields are named in prose (`Employee Document Type`,
`Employer NIT`) while mappings are dotted identifiers (`Employee.Document_Type`, `Company.NIT`), so the
test can essentially never succeed. Two further contributors: `min_row=2` reads the banner-offset
header row itself as data (6 of the 476 were the literal header cell `"System Mapping"`), and the
`DERIVED` classifier does not recognise the canonical system namespaces.

Under an alphanumeric-only normalisation, **459 of the 465 non-header values (98%) resolve to a DD
field**. After the C27 fix (below), the count falls 476 → **230**, and every remaining item is
genuinely derived or structural:

| Count | Namespace | Example | Class |
|---|---|---|---|
| 158 | `Payroll.*` | `Payroll.Overtime_Detail`, `Payroll.Meal_Excess_41UVT` | payroll-engine result, not DD master data |
| 69 | `Mercans.*` | `Mercans.Cesantias_Accrual_Year`, `Mercans.Payment_Channel_Config` | pipeline configuration |
| 3 | arithmetic / n-a | `NIE187 - NIE188 (+/- NIE186)`, `T2R2-047 + T2R2-048 + T2R2-049`, `(not an input)` | cross-field computation |

The 261 distinct identifiers are coherent payroll concepts, not placeholders — `Income_Tax_Withheld`,
`Health_Employee_Contribution`, `Prestaciones_Sociales`, `Cesantias_Paid_To_Employee`,
`NonResident_Withholding`. **MANUAL retained** by choice: extending `DERIVED` to auto-accept the
`Payroll.*` namespace would let a genuinely unmapped payroll field pass silently in a future country.
A human confirming the class is the correct outcome here.

---

## Real fixes applied

### 1. CCG — B10 violation: bare Spanish noun in English prose (found via C33)

Investigating C33 surfaced one genuine defect the mechanical check could not have flagged (it was
masked by the symbol false positives). Module 8, the sickness-incapacity open item, used the bare
Spanish common noun *auxilio* standing alone in an English sentence, with no English wording and no
first-use introduction — a real breach of control B10. It was the **first** use of that term in
document order; the later *"auxilio de cesantía"* (a different benefit) is correctly introduced.

- **Was:** "…Labour Code art. 227 sets the *auxilio* at two thirds for the first 90 days…"
- **Now:** "…Labour Code art. 227 sets the cash sickness benefit (*auxilio monetario*) at two thirds for the first 90 days…"

English wording first, statutory term in parentheses on first use, existing italic run formatting
preserved. Verified verbatim against the source PDF on disk
(`00-official-sources/pdfs/Decreto_2663_de_1950.pdf`), CST art. 227:

> "ARTICULO 227. VALOR DE AUXILIO. En caso de incapacidad comprobada para desempeñar sus labores,
> ocasionada por enfermedad no profesional, el trabajador tiene derecho a que el {empleador} le pague
> un **auxilio monetario** hasta por ciento ochenta (180) días, así: las dos terceras (2/3) partes del
> salario durante los primeros noventa (90) días y la mitad del salario por el tiempo restante."

This also independently confirms the CCG's substantive claim (two thirds for the first 90 days). No
rate, base, ceiling or legal citation changed.

### 2. CCG — Version Control entry for the language pass

Added row **1.0 rev B** (7 September 2026) to the Version Control table, recording the C33 language
pass, the 158-passage false-positive finding, and the one genuine B10 correction — consistent with how
rev A logged the earlier compliance pass.

### 3. Audit harness — four matcher fixes (`_audit_v24_mechanical.py`, v2.9)

Following the TN/CI/CG precedent, the false positives were fixed **in the harness**, not merely
overridden, so the next country does not re-hit them. Backup at `_audit_v24_mechanical.py.bak`;
patch script `_patch_audit_v29.py`. All changes compile clean.

| Check | Fix |
|---|---|
| **C12** (F25) | Scan the first 3 rows for the header, skipping any row with fewer than 2 non-empty cells (a merged title banner); keep the best keyword match instead of assuming row 1. |
| **C20** (F24) | Prefer the explicit `spec_file` link when the manifest carries one, and report it only if the declared file is genuinely absent from disk. Fall back to fuzzy matching only when absent, now stripping separators from **both** sides. |
| **C29** | An open-item marker is an ALL-CAPS convention. `TODO` is now matched **case-sensitively**; markers that cannot collide with a natural-language word (`TBD`, `FIXME`, `VERIFY No`, `[placeholder]`, `[CHECK]`, `[?]`) keep `IGNORECASE`. A real marker written `Todo:` is still caught by an explicit pattern, so detection strength is preserved. |
| **C33** | Replaced the punctuation-blocklist regex with a Unicode **general-category** test: only a character in category `L*` (a letter) outside the Latin blocks counts as script leakage. Symbols, punctuation, marks and digits can never trigger it. A short whitelist covers Greek letters used as mathematical notation (Σ, Π, Δ, μ, σ, …). |
| **C27** | Compare on an alphanumeric-only normalisation so `Payroll.Basic_Salary` matches `Basic Salary`; skip the banner-offset header row; treat `PayPeriod.*`, `System.*` and `Constant` as the structural class. (This implements the C27 widening already recommended in the CG v2.4 log entry.) |

**Regression-tested, not just applied.** The new C33 detector was run against known-positive and
known-negative cases: all nine CO symbol cases now read clean, while Bulgarian Cyrillic, Arabic,
Japanese and Greek prose are **still flagged**, and Latin-accented terms (`Liquidación de Aportes`,
`São Paulo`, `Köln`, `Ångström`) correctly read clean. Detection strength is preserved in every case.

---

## Remaining issues

**None blocking.** No FAIL remains and nothing was left unfixed.

Two MANUALs are retained deliberately, both dispositioned with evidence above — C25 (sample file
verified genuine against the official annex; the check is doing its job by asking a human) and C27
(230 derived/structural mappings; auto-accepting the `Payroll.*` namespace would weaken the check for
future countries).

Two open questions are carried forward from the SIR stage. Neither affects the handover verdict and
both are recorded in `integration-landscape.json`:

1. Whether any licensed PILA *operador de información* besides ARUS/SuAporte offers a contractual API.
   The ARUS "APIS PILA" developer portal renders no public content; closeable only with an operator
   contract. Does not change the verdict — PILA is a portal round-trip either way.
2. Whether DIAN publishes a standalone XSD for Formato 2276 v4, or whether the *prevalidador* remains
   the only validator. Affects `04-reports-spec` fidelity for filing 005, not the integration verdict.

Stage `08-skill/` is empty — the claude.ai compliance skill has not been built for Colombia. That is a
separate pipeline stage and is outside this gate's scope; flagging it only so it is not mistaken for
a missing handover artifact.

---

## Sign-off recommendation

**READY_FOR_HANDOVER.**

All 18 mechanical checks pass or are dispositioned: 16 PASS, 2 MANUAL with written evidence, 0 FAIL.
Every artifact in the v2.4 set is present and structurally complete — CCG (13 modules, 96/96 question
coverage), WTC, DD, 6 report specs covering all 6 in-scope filings, SIR index with a 7-phase runbook
for the one genuine M2M channel, and the 8-sheet payslip generator.

Three of the four original blocking/manual signals were harness defects and are now fixed in the
harness rather than papered over. The one genuine content defect found (a bare Spanish noun breaching
control B10) was corrected against the primary source and logged in the CCG's own version control.

---

## Next steps

1. Open the artifacts and review — particularly `CO-CCG-001-v1.0.docx` Module 8 (the corrected
   sickness-incapacity passage) and the Version Control table entry 1.0 rev B.
2. Manual confirmations to close the two retained MANUALs at review:
   - **C25** — confirm the DIAN NE sample XML is accepted as a documented reconstruction. It must be
     validated against XSD v1.0.6 in the DIAN habilitación environment before production use, as the
     sheet's own provenance note instructs.
   - **C27** — confirm the `Payroll.*` and `Mercans.*` namespaces are the accepted pipeline-side
     convention for engine results and configuration.
3. Two CCG open items remain flagged in-document for the dev team (both carry a Mercans configurable
   default and are already carried in the QA report, so neither blocks): the employer's rate for the
   first two days of incapacity (default 66.67%), and the minimum-wage floor on incapacity payments
   (primary regulatory source not retrieved this pass).
4. **If READY:** share with the dev team.
5. **Port the v2.9 harness fixes to `shared/`.** C12, C20, C27, C29 and C33 were fixed in the CO copy
   of `_audit_v24_mechanical.py`. F24 and F25 have now recurred on six consecutive countries
   (BH, OM, TN, CI, CG, CO) — the fixes should be promoted to the shared harness so country seven does
   not repeat this investigation.
6. Failure log updated — see `shared/country_failure_log.md`: F24/F25 reproduction recorded for CO,
   and **F27** (C29 `todo` regression) and **F28** (C33 symbol misread) added.
