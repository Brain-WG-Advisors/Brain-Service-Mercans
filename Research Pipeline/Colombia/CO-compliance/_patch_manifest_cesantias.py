# -*- coding: utf-8 -*-
"""One-shot manifest update for CO-CESANTIAS-DEPOSIT-ANNUAL-006 (04-reports-spec pass)."""
import collections
import io
import json

P = "scope_manifest.json"
d = json.load(io.open(P, encoding="utf-8"), object_pairs_hook=collections.OrderedDict)

f = [x for x in d["authority_filings"]["in_scope"]
     if x["filing_id"] == "CO-CESANTIAS-DEPOSIT-ANNUAL-006"][0]

f["format"] = ("Fixed-width TXT (20 fields / 258 positions) or XLS 97-2003 (16 columns A-P), both "
               "without a header row; CSV is also accepted by SOI. NOT XML - no XSD exists. Layout "
               "VERIFIED from the published Simple S.A. 'Manual Cesantias' ss. 3.1-3.2.")
f["channel"] = ("Operador de informacion portal, TWO channels: online_form (Planilla En Linea) or "
                "file_upload (Envio de Archivo Unificado de Cesantias). VERIFIED independently in "
                "the published manuals of ACH Colombia S.A. (SOI, www.nuevosoi.com.co, instructivo "
                "DDS-DES-INS-008 v2) and Simple S.A. (www.pagosimple.com). Not machine-to-machine: "
                "no XSD, no SOAP, no signature, no certificate. The channel returns a planilla "
                "number, a comprobante PDF and post-payment reports; the fund itself issues the "
                "deposit certificate.")
f["deadline"] = ("Before 15 February of the year following the 31 December liquidation, so the last "
                 "compliant day is 14 February (Ley 50 de 1990 art. 99 num. 3; the MinTrabajo draft "
                 "decree states mora runs from 15 February). Where 14 February falls on a "
                 "non-business day Colombian practice moves it to the next business day - for "
                 "accrual year 2025 the shift from Saturday 14 to Monday 16 February 2026 was "
                 "uniformly reported in the press - but no MinTrabajo concepto was located, so the "
                 "shift is TO CONFIRM and must not be relied on. For accrual year 2026 the last day "
                 "is Sunday 14 February 2027: deposit by Friday 12 February 2027.")
f["legal_basis"] = ("Ley 50 de 1990 art. 99 nums. 1-3; Ley 2466 de 2025 art. 64 (two new paragraphs "
                    "to Ley 50 art. 99: the 8.33% monthly advance and the 1% monthly interest); CST "
                    "arts. 249, 250, 253, 254, 310; CST art. 57 par. 4 as added by Ley 2466 de 2025 "
                    "art. 15; Ley 52 de 1975 art. 1; Decreto 1072 de 2015 arts. 2.2.1.3.1, "
                    "2.2.1.3.4, 2.2.1.3.5 and 2.2.1.3.13; CST art. 488 as substituted by Ley 2466 "
                    "de 2025 art. 62; Decreto 1469 de 2025 (SMMLV 1,750,905 and transport allowance "
                    "249,095)")
f["source_status"] = ("PRIMARY for the law and PRIMARY for a published field layout. No longer "
                      "DERIVED - see the CO-CESANTIAS-006 entries in resolved_in_this_pass.")

d["resolved_in_this_pass"].append(
    "CO-CESANTIAS-006 LAYOUT SOURCING CLOSED: scope_manifest previously recorded the annual "
    "cesantias deposit as having no published schema ('each fondo publishes its own layout'). It "
    "does have one. The Simple S.A. 'Manual Cesantias' (licensed operador de informacion), section "
    "3.2, publishes a byte-exact fixed-width layout of 20 campos in 258 positions with "
    "Inicial-Final positions, lengths, types and validations, and section 3.1 publishes the "
    "parallel XLS 97-2003 layout of 16 columns A-P; both carry the five-value fondo code table (02 "
    "Proteccion, 03 Porvenir, 10 Colfondos, 15 FNA, 19 Skandia) and the document-type table. The "
    "positions are arithmetically consistent "
    "(2+5+2+16+20+20+20+20+2+3+4+9+4+9+50+2+3+7+50+10 = 258). The CHANNEL is independently "
    "confirmed by the ACH Colombia (SOI) instructivo DDS-DES-INS-008 v2. Both PDFs are now in "
    "00-official-sources/pdfs/ and extracted to _txt/. Spec accuracy 88%, against the previous "
    "DERIVED assumption.")
d["resolved_in_this_pass"].append(
    "CO-CESANTIAS-006 TRANSPORT-ALLOWANCE DEFECT IDENTIFIED IN THE CHANNEL ITSELF: the operator's "
    "auto-calculator uses 'Salario basico * (dias trabajados / 360)' and its campo 12 is named "
    "'salario basico', whereas CST art. 253 requires the auxilio de transporte in the base and Ley "
    "2466 de 2025 art. 64 par. 1 says so expressly for the monthly advance. For a 2026 minimum-wage "
    "employee the portal computes COP 1,750,905 against a statutory COP 2,000,000 - a COP 249,095 "
    "short deposit per employee, penalised as non-deposit at one day's salary per day of delay, "
    "uncapped. The engine must always write its own figure into campo 14. Documented at Spec field "
    "T14 and on Sheets 5, 7, 8 and 9.")

d["known_gaps"].append(collections.OrderedDict([
    ("id", "CO-GAP-12"),
    ("item", "Whether every licensed operador de informacion accepts the same 258-position "
             "cesantias record"),
    ("status", "The layout is published by Simple S.A. and the channel is confirmed independently "
               "by ACH Colombia (SOI), but SOI publishes its own column layout only inside the "
               "upload screen, behind an authenticated session. Aportes en Linea, Asopagos, Enlace "
               "Operativo and MiPlanilla were not verified. The Fondo Nacional del Ahorro's "
               "employer instructivo, which as a state entity would be the one genuinely official "
               "schema for this filing, is no longer retrievable - its published URL "
               "(fna.gov.co/empleadores/.../INSTRUCTIVO ARCHIVO PLANO ENTIDADES PRIVADAS.pdf) "
               "returns 404 after the FNA site redesign. Also unstated in the source: the code page "
               "and the line terminator."),
    ("action", "Confirm the layout against one real accepted filing per client operator before a "
               "productive run; retry the FNA instructivo through the redesigned site.")]))
d["known_gaps"].append(collections.OrderedDict([
    ("id", "CO-GAP-13"),
    ("item", "The 8.33% monthly advance deposit of cesantias is not yet operable"),
    ("status", "Ley 2466 de 2025 art. 64 par. 1 is IN FORCE and permits it, but routes it through "
               "PILA and instructs MinSalud to regulate. As at 4 September 2026 the implementing "
               "decree is still a MinTrabajo DRAFT (proyecto amending Decreto 1072 de 2015 arts. "
               "2.2.1.3.1, 2.2.1.3.4, 2.2.1.3.5 and 2.2.1.3.13, held at "
               "00-official-sources/pdfs/proyecto_decreto_cesantias_2026.pdf). That draft would "
               "give MinSalud six months from its entry into force to adjust PILA, and then the "
               "fondos and operadores a FURTHER six months to build; no PILA tipo de cotizacion for "
               "cesantias exists yet. The annual planilla therefore remains the only lawful route. "
               "The draft also confirms two rules that survive regardless: the definitive annual "
               "consolidation on the average-of-the-year base, and mora running from 15 February."),
    ("action", "Build the fields but keep the feature switched OFF (Spec fields MA01-MA05, all "
               "flagged DRAFT). Monitor for the enacted decree AND the MinSalud PILA resolution; "
               "when both land, add a contribution type to the CO-PILA-003 Spec.")]))
d["known_gaps"].append(collections.OrderedDict([
    ("id", "CO-GAP-14"),
    ("item", "Ley 2466 de 2025 art. 15 announces two paragraphs but enacts three"),
    ("status", "The enacting formula of art. 15 reads 'adicionese ... los paragrafos 2 y 3 del "
               "articulo 57 del Codigo Sustantivo del Trabajo', yet the published text prints a "
               "Paragrafo 4 - the one making proven direct payment of cesantias discharging. "
               "Verified against the local Ley_2466_de_2025.pdf. The substance is not in doubt and "
               "the CCG citation (CST art. 57 par. 4, added by Ley 2466 de 2025 art. 15) matches "
               "the printed text, but the internal inconsistency should be expected to be raised."),
    ("action", "Cite CST art. 57 par. 4 as added by Ley 2466 de 2025 art. 15 and note the drafting "
               "discrepancy where challenged. No engine impact.")]))

io.open(P, "w", encoding="utf-8").write(json.dumps(d, indent=1, ensure_ascii=True))
print("manifest updated - gaps: %d, resolved: %d"
      % (len(d["known_gaps"]), len(d["resolved_in_this_pass"])))
