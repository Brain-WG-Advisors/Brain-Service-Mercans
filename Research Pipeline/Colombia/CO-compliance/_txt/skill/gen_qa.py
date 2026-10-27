# -*- coding: utf-8 -*-
import io, json

OUT = "08-skill/co-compliance/references/07-qa-report.md"
L = []
W = L.append

W("""# Colombia - QA Cross-Check, Known Limitations and Open Items - COMPLETE REFERENCE

**Sources reproduced in full below:**
- `07-qa-crosscheck/CO-QA-REPORT.md` - the stage-07 QA cross-check (2026-09-07)
- `scope_manifest.json` - the 14 numbered known gaps `CO-GAP-01`...`CO-GAP-14` and the 10 items resolved in
  this pass
- `07-qa-crosscheck/CO-ALIGNMENT-PATCH.md` - the mandatory DD-to-spec alignment patch (v1.1, 2026-09-07)
- `07-qa-crosscheck/handover_status.md` - the pre-submission audit gate verdict

**Headline verdict: 94 / 100 - PASS WITH PATCHES (`NEEDS PATCHES`) - 0 CRITICAL - 3 MAJOR - 12 MINOR.**
The compliance *content* is dev-ready; the three MAJORs are wiring and cross-reference defects in two files
(the payslip generator and CCG Module 10), not calculation errors.

---

## Quick index of open items by artifact

| Artifact | Open items |
|---|---|
| **Payslip** (`06-payslip.md`) | **MAJOR-01** `XXXXX` wage-type placeholders (36 cells) - **MAJOR-02** no CUNE / QR / generation date / payment date / prefix+consecutive - MINOR-05 vacation base includes bundled overtime - MINOR-06 no navy header / green net-pay fill - `Unit Rate Details` account codes are illustrative placeholders `[VERIFY WITH RA]` |
| **CCG** (`01-ccg.md`) | **MAJOR-03** Module 10 scope note cites a non-existent `CO-RPT-007` spec and `CO-SIR-001...007` register; CO-RPT-007 row not marked out of scope - MINOR-04 Module 4.6 table contradicts its own 40%-clamp narrative on two rows |
| **WTC** (`02-wtc.md`) | MINOR-01 CZ template residue in Version Control row 14 - MINOR-09 `CO-TX-08` defined but assigned to zero rows (by design - column-P overlay) - 4 substantive OPEN ITEMS (sick-pay rate, incapacity floor, high-risk pension rate, monthly apportionment of annual UVT caps) |
| **DD** (`05-data-dictionary.md`) | MINOR-03 four document-type codes the manifest declares out of scope (`11`, `CD`, `SC`, `PT`) - MINOR-11 active-pensioner flag has no discrete field (carried by `Worker Sub-Type = 01`) - option-mapper count 35 in the file vs 30 in the QA report `[VERIFY WITH RA]` |
| **Report specs** (`04-reports-spec.md`) | MINOR-02 PILA composite key not labelled - MINOR-07 five Sheet-4 column labels vary from the standard - MINOR-08 Version-Control column order - MINOR-10 column L carries no WTC code for amount fields - MINOR-12 F350 uses 4 of 5 row colours (legitimate) - **all 563 Sheet-4 rows carry `Query to RA` = *Pending RA review*** |
| **SIR** (`03-sir.md`) | 2 open questions in the landscape (below) - per-tenant secrets (`SoftwareID`, PIN, ONAC X.509) are issued at habilitacion and cannot pre-exist a client engagement |

## The four substantive OPEN ITEMS carried in the WTC (engine defaults, all configurable)

| # | Item | Position | Mercans default |
|---|---|---|---|
| 1 | **Rate for the employer's first two days of general-illness incapacity.** Decreto 2943 de 2013 art. 1 (compiled at Decreto 780 de 2016 art. 3.2.1.10) allocates days 1-2 to the employer but **does not state the rate**. CST art. 227 sets the *auxilio* at two thirds for the first 90 days; market practice applies 66.67% on that basis, a minority pays 100%. | `CO-INCAP-EG-EMPLEADOR` | **66.67%**, configurable |
| 2 | **Minimum-wage floor on incapacity payments.** Where 66.67% of salary falls below one SMMLV (1,750,905), market practice and settled administrative doctrine top the payment up to one minimum wage. The primary regulatory source was **not retrieved**. | incapacity cascade | **apply the floor**, configurable |
| 3 | **Additional employer pension contribution for Decreto Ley 2090 de 2003 high-risk activities.** The Resolucion 2388 rate table implies +10 pp employer-borne (26% total vs 16% standard); the 2026 rate and base are **not confirmed from a primary regulatory source** (`CO-GAP-02`). | `AltoRiesgoPension` | read from the Res. 2388 table; **DERIVED** |
| 4 | **Monthly apportionment of the ANNUAL 790-UVT and 1,340-UVT tax caps.** Both caps are stated annually while withholding is monthly. No regulation prescribes the apportionment expressly. | ET arts. 206 num. 10, 388 | **one twelfth** - 65.8333 UVT (3,447,955) and 111.6667 UVT (5,848,430), configurable |

---

# Part A - CO-QA-REPORT.md (verbatim, in full)

""")

W(io.open("07-qa-crosscheck/CO-QA-REPORT.md", encoding="utf-8").read().strip())

# ---------------- known gaps -------------------
d = json.load(io.open("scope_manifest.json", encoding="utf-8"))

W("""

---

# Part B - Known gaps and resolved items (`scope_manifest.json` v%s, verbatim)

Every gap below is a **disclosed limitation**, not a silent omission. Treat each as a live
`[VERIFY WITH RA]` item.

## B.1 The 14 numbered known gaps
""" % d.get("scope_version", "1.0"))

for g in d["known_gaps"]:
    W("\n### %s - %s\n" % (g.get("id", ""), g.get("item", "")))
    for k, v in g.items():
        if k in ("id", "item"):
            continue
        W("- **%s:** %s" % (k, v))

W("\n## B.2 Items RESOLVED in this pass (%d)\n" % len(d["resolved_in_this_pass"]))
for i, r in enumerate(d["resolved_in_this_pass"], start=1):
    if isinstance(r, dict):
        W("\n%d. " % i + "; ".join("**%s**: %s" % (k, v) for k, v in r.items()))
    else:
        W("\n%d. %s" % (i, r))

W("\n## B.3 Known failure patterns checked (control C20)\n")
kf = d.get("known_failure_patterns_to_check", [])
if isinstance(kf, list):
    for x in kf:
        if isinstance(x, dict):
            W("- " + "; ".join("**%s**: %s" % (k, v) for k, v in x.items()))
        else:
            W("- %s" % x)
elif isinstance(kf, dict):
    for k, v in kf.items():
        W("- **%s**: %s" % (k, v))

fpn = d.get("failure_pattern_notes")
if fpn:
    W("\n### Failure-pattern notes\n")
    if isinstance(fpn, dict):
        for k, v in fpn.items():
            W("- **%s**: %s" % (k, v))
    elif isinstance(fpn, list):
        for x in fpn:
            W("- %s" % x)
    else:
        W(str(fpn))

# ---------------- integrations open questions ---------------
land = json.load(io.open("03-statutory-integrations/integration-landscape.json", encoding="utf-8"))
W("\n## B.4 Integration-landscape open questions\n")
for q in land["open_questions"]:
    if isinstance(q, dict):
        W("- " + "; ".join("**%s**: %s" % (k, v) for k, v in q.items()))
    else:
        W("- %s" % q)

W("""

---

# Part C - DD-to-Report-Specs alignment patch v1.1 (verbatim, in full)

""")
W(io.open("07-qa-crosscheck/CO-ALIGNMENT-PATCH.md", encoding="utf-8").read().strip())

W("""

---

# Part D - Pre-submission audit gate / handover status (verbatim, in full)

""")
W(io.open("07-qa-crosscheck/handover_status.md", encoding="utf-8").read().strip())

W("""

---

# Part E - Accuracy notes: what was independently re-derived, and what is DERIVED

## Verified by recomputation (exact, no rounding tolerance)

| Item | Result |
|---|---|
| Payslip income-tax withholding (ET arts. 383 / 388 / 206 num. 10) | **2,250,765 COP - exact.** Gross 19,200,000 - contributions 1,728,000 = 17,472,000; less 25% exempt capped at 790 UVT / 12 = 3,447,955 -> base 14,024,045 = 267.76732 UVT; band 150-360 UVT -> 0.28 x (267.76732 - 150) + 10 = 42.97485 UVT x 52,374. The 40% / 1,340-UVT art. 388 caps were tested and are not binding. |
| Payslip net pay | **15,221,235 COP** (`SUM(H21:J24) - SUM(H28:J31)`) |
| YTD block (7 months) | 134,400,000 / 12,096,000 / 15,755,355 / **106,548,645**; YTD net / 7 = the monthly net exactly |
| Employer block + provisions | 8.5 / 12 / 0.522 / 4 / 2 / 3 % and 8.33 + 1 + 8.33 + 4.17 = **21.83%**, agreeing with the WTC's 21.8333% |
| PILA record lengths | Archivo Tipo 1 **34 fields / 567 positions**; Archivo Tipo 2 Registro Tipo 1 **22 / 359**; Registro Tipo 2 **97 / 686** - arithmetically verified |
| Global WTC coverage | **300 of 300**, set difference empty in both directions |
| Form Reference Guide pointers | **65 of 65** resolve to a real file, sheet and in-range row - 0 broken |
| Fiscal parameters | SMMLV **1,750,905** (Decreto 1469 de 2025 art. 1) and UVT **52,374** (Res. DIAN 000238 de 15-12-2025 art. 1) verified in the source PDFs. **No stale parameters**: every occurrence of 1,423,500 (2025 SMMLV) or 49,799 (2025 UVT) is an explicit historical comparison. |

## Declared DERIVED (must be reconciled at configuration time)

| Item | Why |
|---|---|
| The Mercans code numbers of the 102 Colombia-specific WTC rows | No Mercans numeric code range has been assigned for Colombia; mnemonic `CO-` codes are used and **must be renumbered**. |
| Auxilio de transporte 2026 = **249,095** | Carried from the CCG because Decreto 1470 de 2025 is not held in `00-official-sources`. |
| The additional high-risk pension rate | Read from the Resolucion 2388 rate table (26% total vs 16% standard, implying +10 pp employer-borne), **not** from the implementing decree - `CO-GAP-02`. |
| Formato 2276 v4 XML layout | Marked **DERIVED** in the spec because the DIAN *especificaciones tecnicas* annex is not held locally. |
| The 7-phase `P1`-`P7` DIAN-NE runbook decomposition | The canonical `shared/si-runbook` module is not installed in this checkout; the phase boundaries are reconstructed from the stage-6 contract. Content maps across cleanly; file names may need renaming. |
| `Unit Rate Details` account codes on the payslip generator | Sheet is headed *"illustrative placeholder account codes; align to actual CO-WTC once available"*. |

## Defects found in OFFICIAL sources and recorded rather than propagated

| Source | Defect |
|---|---|
| MinTrabajo Circular Externa 101 de 2025, section 5.1 | States the Sunday/holiday supplementary-work premium as *"75% (Art. 179 CST)"* - the **pre-reform** figure - contradicting its own section 4, which correctly sets out the 80% / 90% / 100% phase-in. |
| Nomina electronica Anexo Tecnico v1.0, section 5.5.5 | Hard-codes the pre-reform rest-day percentages **75 / 100 / 150 / 110**. Settled by **DIAN Concepto 013840 (int. 1568) of 1 October 2025**: the statutory Ley 2466 de 2025 percentages govern; the annex literals **must not be configured**. |
| Decreto 1607 de 2002 | ARL class-IV rate defect. |
| Nomina electronica XSD | `Trabajador/@NumeroDocumento` typed `xsd:integer`, so no passport or alphanumeric foreign ID can be schema-valid (document types 21, 41, 42, 50); `Trabajador/@SegundoApellido` is `use=required`, yet many Colombians and virtually all foreign nationals have only one surname. No official workaround published - `CO-GAP-07`. |
| Nomina electronica document-type catalogue | **No code for the PPT** (*Permiso por Proteccion Temporal*, Decreto 216 de 2021), created one month after the annex and now held by the large majority of regularised Venezuelan migrants. Code 47 (PEP) is its legally superseded predecessor and the only proxy - `CO-GAP-06`. |
| Ley 2466 de 2025 art. 15 | The enacting formula announces *"los paragrafos 2 y 3"* but the published text prints a **Paragrafo 4** - `CO-GAP-14`. |
| Cesantias operator (Simple S.A.) auto-calculator | Uses `salario basico * (dias trabajados / 360)` and names campo 12 *"salario basico"*, whereas **CST art. 253 requires the auxilio de transporte in the base**. The operator's own calculator is wrong. |

## Time-sensitive parameters - reverify before each cycle

| Parameter | 2026 value | Watch |
|---|---|---|
| SMMLV | **1,750,905** COP/month | Decreto 1469 de 2025 was provisionally suspended (Consejo de Estado, 12 Feb 2026), re-fixed at the identical amount by Decreto 0159 de 2026, and the suspension was revoked on 9 July 2026. The **amount** was continuously in force from 1 Jan 2026 and was never in doubt - but an **annulment action on the merits is still pending** (`CO-GAP-08`). |
| Auxilio de transporte | **249,095** COP/month | Decreto 1470 de 2025 art. 1 - DERIVED, decree not held locally |
| UVT | **52,374** COP | Res. DIAN 000238 de 15-12-2025 art. 1 (uprating certified at 5.17%, from 49,799) |
| IBC ceiling / FSP trigger | 25 SMMLV = **43,772,625** / 4 SMMLV = **7,003,620** | move with the SMMLV |
| Rest-day premium | 80% -> **90% on 1 Jul 2026** -> 100% on 1 Jul 2027 | Ley 2466 de 2025 |
| Hourly divisor | 220 -> **210 on 15 Jul 2026** | Ley 2101 de 2021 + MinTrabajo Circular 101 de 2025 (the circular's legal weight is `CO-GAP-09`) |
| Pension architecture | **Ley 100 de 1993 as amended by Ley 797 de 2003** governs all of 2026 | Ley 2381 de 2024 is NOT in force for any 2026 period: art. 94 entry into force was suspended by Auto 841 de 2025 and, per **Sentencia C-264 de 25 August 2026**, the upheld provisions take effect **1 April 2027** (`CO-GAP-11`) |
| Cesantias 8.33% monthly advance deposit | permitted by Ley 2466 de 2025 art. 64 par. 1 but **not yet operable** | the implementing decree was still a MinTrabajo draft as at 4 September 2026 (`CO-GAP-13`) |
""")

txt = "\n".join(L)
io.open(OUT, "w", encoding="utf-8").write(txt)
print(OUT, len(txt))
