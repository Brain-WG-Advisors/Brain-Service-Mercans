# -*- coding: utf-8 -*-
"""
CO-DIAN-001 - Documento Soporte de Pago de Nomina Electronica.
Filing ID: CO-DIAN-NE-MONTHLY-001.

EVERY field code (NIE/NIAE), XPath, length, cardinality and code table in this
module is taken verbatim from the OFFICIAL source held at
  00-official-sources/pdfs/AnexoTecnico-NominaElectronica-V1.0.pdf
(Anexo Tecnico del Documento Soporte de Pago de Nomina Electronica, Version 1.0,
annexed to Resolucion DIAN 000013 of 11 February 2021, 269 pages).
Extraction artefacts: _txt/ne_anexo.txt and _txt/ne_fields.json (195 NIE codes).
C19 prefix pattern: ^NIE[0-9]{3}$ for the payroll document, ^NIAE[0-9]{3}$ for
the adjustment note. No code in this Spec falls outside those patterns.
"""

from build_co_specs import (R_XML, R_NONE, RA)
from co_scope_common import SCOPE_WHO, SCOPE_TIMING


def F(en, es, rec, pos, mand, cond, xpath, length, fmt, ex, mapping, expl,
      rel, opts, rnd, neg, vt, freq, q, ra, kind):
    """Build one 21-column Spec row plus its colour-coding kind."""
    return [en, es, rec, pos, "", mand, cond, xpath, length, fmt, ex, mapping,
            expl, rel, opts, rnd, neg, vt, freq, q, ra, kind]


# --- the seven overtime / premium hour blocks (Anexo Tecnico table 5.5.5) ---
# (element, NIE HoraInicio, NIE HoraFin, NIE Cantidad, NIE Porcentaje, NIE Pago,
#  code, EN label, ES label, statutory percentage as printed in table 5.5.5)
HOUR_BLOCKS = [
    ("HED",   "NIE074", "NIE075", "NIE076", "NIE077", "NIE078", "1",
     "Day overtime hour", "Hora Extra Diurna", "25.00"),
    ("HEN",   "NIE079", "NIE080", "NIE081", "NIE082", "NIE083", "2",
     "Night overtime hour", "Hora Extra Nocturna", "75.00"),
    ("HRN",   "NIE084", "NIE085", "NIE086", "NIE087", "NIE088", "3",
     "Night-work surcharge hour", "Hora Recargo Nocturno", "35.00"),
    ("HEDDF", "NIE089", "NIE090", "NIE091", "NIE092", "NIE093", "4",
     "Day overtime hour, Sunday / public holiday", "Hora Extra Diurna Dominical y Festivos", "100.00"),
    ("HRDDF", "NIE094", "NIE095", "NIE096", "NIE097", "NIE098", "5",
     "Day surcharge hour, Sunday / public holiday", "Hora Recargo Diurno Dominical y Festivos", "75.00"),
    ("HENDF", "NIE099", "NIE100", "NIE101", "NIE102", "NIE103", "6",
     "Night overtime hour, Sunday / public holiday", "Hora Extra Nocturna Dominical y Festivos", "150.00"),
    ("HRNDF", "NIE104", "NIE105", "NIE106", "NIE107", "NIE108", "7",
     "Night surcharge hour, Sunday / public holiday", "Hora Recargo Nocturno Dominical y Festivos", "110.00"),
]

_STALE_PCT_QUERY = (
    "SOURCE CONFLICT, escalate. Anexo Tecnico table 5.5.5 hard-codes the Sunday / holiday "
    "surcharge at 75.00 and the derived Sunday / holiday overtime rates at 100.00 / 150.00 / 110.00. "
    "Those figures pre-date Ley 2101 de 2021 and Ley 2466 de 2025, under which the Sunday and "
    "public-holiday surcharge steps to 80% on 1 July 2025 and to 90% on 1 JULY 2026. From 1 July "
    "2026 the statutory surcharge (90%) therefore no longer equals the annex value (75.00). The "
    "annex is still at version 1.0 and DIAN has not reissued table 5.5.5. Confirm with the RA "
    "whether DIAN expects the ANNEX code percentage or the STATUTORY percentage in @Porcentaje.")


def _hour_rows():
    rows = []
    for el, n_ini, n_fin, n_cant, n_pct, n_pago, code, en, es, pct in HOUR_BLOCKS:
        base = "/NominaIndividual/Devengados/%ss/%s" % (el, el)
        stale = _STALE_PCT_QUERY if el in ("HEDDF", "HRDDF", "HENDF", "HRNDF") else ""
        rows += [
            F("%s - start time" % en, "%s - Hora de inicio" % es, "Devengados / %s" % el, n_ini, "C",
              "Optional in the schema (0-1) but required by the RA whenever the client reports the "
              "day/night split for the overtime register. Pairs with '%s - end time' (%s): if one is "
              "present the other must be present." % (en, n_fin),
              "%s/@HoraInicio" % base, "19", "AAAA-MM-DDTHH:MM:SS", "2026-03-11T18:00:00",
              "Payroll.Overtime_Detail.Start_Time",
              "Clock time at which this overtime or surcharge block began. The XML models overtime as "
              "a repeating block, not as a single monthly total, so each contiguous stretch of hours "
              "is one %s element. Cardinality 0-N under %ss." % (el, el),
              "Y", "-", R_NONE, "N", "Date", "Per record", stale, RA, "payroll"),
            F("%s - end time" % en, "%s - Hora de finalizacion" % es, "Devengados / %s" % el, n_fin, "C",
              "Optional in the schema (0-1); required whenever '%s - start time' (%s) is present. "
              "Bidirectional pair." % (en, n_ini),
              "%s/@HoraFin" % base, "19", "AAAA-MM-DDTHH:MM:SS", "2026-03-11T20:00:00",
              "Payroll.Overtime_Detail.End_Time",
              "Clock time at which the block ended. Must be later than @HoraInicio; a block that "
              "crosses midnight is split into two elements, because the day/night boundary (21:00 "
              "under CST art. 160 as amended by Ley 2101 de 2021) also changes the applicable code.",
              "Y", "-", R_NONE, "N", "Date", "Per record", stale, RA, "payroll"),
            F("%s - quantity" % en, "%s - Cantidad" % es, "Devengados / %s" % el, n_cant, "Y", "",
              "%s/@Cantidad" % base, "Var", "N (integer hours)", "2",
              "Payroll.Overtime_Detail.Hours",
              "Number of hours of this type in the block. Colombia caps overtime at 2 hours per day "
              "and 12 per week (CST art. 167 / 168); the engine must maintain those counters "
              "independently, because the XML does not enforce them.",
              "Y", "-", R_NONE, "N", "Count", "Per record", "", RA, "payroll"),
            F("%s - percentage" % en, "%s - Porcentaje" % es, "Devengados / %s" % el, n_pct, "Y", "",
              "%s/@Porcentaje" % base, "4-6", "N (decimal, e.g. 25.00)", pct,
              "Mercans.Overtime_Rate_%s" % el,
              "The premium percentage applied. Anexo Tecnico table 5.5.5 assigns code %s to '%s' with "
              "printed percentage %s. This is the only place the XML carries the rate; the amount in "
              "@Pago must be consistent with it." % (code, es, pct),
              "Y", "-> Sheet 6: Overtime / surcharge type (table 5.5.5)",
              "Rate expressed to 2 decimals, not rounded by the payroll engine.",
              "N", "Rate", "Per record", stale, RA, "system"),
            F("%s - amount" % en, "%s - Pago" % es, "Devengados / %s" % el, n_pago, "Y", "",
              "%s/@Pago" % base, "Var", "N (decimal 2)", "104166.67",
              "Payroll.Overtime_Detail.Amount",
              "Money value of the block. Base for the hourly rate is the ordinary hourly wage; note "
              "that the hourly divisor changes from 220 to 210 on 15 July 2026 as the working week "
              "steps to 42 hours (Ley 2101 de 2021), so the engine must stamp the divisor used.",
              "Y", "-", R_XML, "N", "Amount", "Per record", "", RA, "payroll"),
        ]
    return rows


# ===========================================================================
#  SHEET 4 - FIELD SPECIFICATION
# ===========================================================================
FIELDS = [
    "DOCUMENT ENVELOPE - UBL EXTENSIONS AND SIGNATURE",
    F("UBL extensions container", "UBLExtensions", "Envelope", "NIE001", "Y", "",
      "/NominaIndividual/UBLExtensions", "-", "Empty element (group)", "(group)",
      "System.UBL_Extension_Block",
      "Group element opening the UBL 2.1 extension area. It carries the XAdES-EPES advanced digital "
      "signature (ds:Signature) and any sector-specific additional information under Anexo Tecnico "
      "s.10.1. Generated by the signing component, never by payroll.",
      "N", "-", R_NONE, "N", "Code", "Per document", "", RA, "system"),
    F("Digital signature", "ds:Signature", "Envelope", "NIE001 (child)", "Y", "",
      "/NominaIndividual/UBLExtensions/UBLExtension/ExtensionContent/ds:Signature", "-",
      "XAdES-EPES enveloped signature", "(base64 signature)", "System.Signing_Certificate",
      "Advanced digital signature over the whole document, using an X.509 certificate issued by a "
      "certification authority accredited by ONAC. Signature policy, canonicalisation and the "
      "ClaimedRole (thirdparty or supplier) are fixed by Anexo Tecnico s.7. Validation rules "
      "s.6.1.3 reject a document whose signature does not verify.",
      "N", "-", R_NONE, "N", "Code", "Per document", "", RA, "system"),
    F("QR code string", "CodigoQR", "Envelope", "NIE021", "Y", "",
      "/NominaIndividual/CodigoQR", "Var", "URL text", "https://catalogo-vpfe.dian.gov.co/document/"
      "searchqr?documentkey=16560dc8...", "System.QR_URL",
      "The DIAN document-search URL with the CUNE as the key. Anexo Tecnico s.13.1 fixes the payload. "
      "If a graphical representation (payslip PDF) is issued, this QR must be printed at not less "
      "than 2 cm x 2 cm on EVERY page (Res. 000013 de 2021 art. 24 and Anexo s.13.1).",
      "N", "-", R_NONE, "N", "Text", "Per document", "", RA, "system"),

    "GENERAL INFORMATION - InformacionGeneral",
    F("Version literal", "Version", "InformacionGeneral", "NIE022", "Y", "",
      "/NominaIndividual/InformacionGeneral/@Version", "Var", "Fixed text",
      "V1.0: Documento Soporte de Pago de Nomina Electronica", "Mercans.NE_Version_Literal",
      "A CONSTANT. The element must carry this exact literal string, accents included. Validation "
      "rule NIE022 rejects any other value. Do not derive it, do not localise it, do not trim it.",
      "N", "-> Sheet 6: Version literal", R_NONE, "N", "Text", "Per document", "", RA, "const"),
    F("Environment", "Ambiente", "InformacionGeneral", "NIE023", "Y", "",
      "/NominaIndividual/InformacionGeneral/@Ambiente", "1", "N (code)", "1",
      "Mercans.NE_Environment",
      "Destination environment of the document, from Anexo Tecnico table 5.1.1: 1 = Produccion, "
      "2 = Pruebas (habilitacion). It is ALSO one of the eleven inputs to the CUNE hash, so a "
      "document generated in test can never be replayed into production - the CUNE would differ.",
      "N", "-> Sheet 6: Ambiente (table 5.1.1)", R_NONE, "N", "Code", "Per document", "", RA, "system"),
    F("XML document type", "TipoXML", "InformacionGeneral", "NIE202", "Y", "",
      "/NominaIndividual/InformacionGeneral/@TipoXML", "2", "N (code)", "102",
      "Mercans.NE_Document_Type",
      "Anexo Tecnico table 5.5.7: 102 = NominaIndividual (the payroll support document), "
      "103 = NominaIndividualDeAjuste (the adjustment note). Also an input to the CUNE.",
      "N", "-> Sheet 6: Tipo de XML (table 5.5.7)", R_NONE, "N", "Code", "Per document", "", RA, "system"),
    F("CUNE - unique payroll document code", "CUNE - Codigo Unico de Nomina Electronica",
      "InformacionGeneral", "NIE024", "Y", "",
      "/NominaIndividual/InformacionGeneral/@CUNE", "96", "A (hex, 96 chars)",
      "16560dc8956122e84ffb743c817fe7d494e058a44d9ca3fa4c234c268b4f766003253fbee7ea4af9682dd57210f3bac2",
      "System.CUNE",
      "COMPOSITE KEY - position breakdown. The CUNE is the SHA-384 hexadecimal digest (96 hex "
      "characters) of ELEVEN concatenated inputs, in this exact order and with no separators "
      "(Anexo Tecnico s.8.1.1.1): "
      "[1] NumNE = Prefijo + Consecutivo (NIE012); "
      "[2] FecNE = FechaGen (NIE026, AAAA-MM-DD); "
      "[3] HorNE = HoraGen including the GMT offset (NIE027); "
      "[4] ValDev = DevengadosTotal (NIE187), decimal point, 2 decimals TRUNCATED, no thousand "
      "separators, no currency symbol; "
      "[5] ValDed = DeduccionesTotal (NIE188), same format; "
      "[6] ValTolNE = ComprobanteTotal (NIE189), same format; "
      "[7] NitNE = employer NIT (NIE033) without dots, hyphens or the verification digit; "
      "[8] DocEmp = employee document number (NIE045) without dots or hyphens; "
      "[9] TipoXML (NIE202); "
      "[10] Software-Pin - the secret PIN, which NEVER appears in the XML; "
      "[11] TipAmb = Ambiente (NIE023). "
      "PERSISTENCE: the CUNE is immutable once the document is validated. Any change to any of the "
      "eleven inputs produces a different CUNE and therefore a different document; corrections are "
      "made by an adjustment note carrying its own CUNE and referencing the original.",
      "N", "-", R_NONE, "N", "Identifier", "Per document", "", RA, "system"),
    F("CUNE algorithm literal", "EncripCUNE", "InformacionGeneral", "NIE025", "Y", "",
      "/NominaIndividual/InformacionGeneral/@EncripCUNE", "11", "Fixed text", "CUNE-SHA384",
      "Mercans.CUNE_Algorithm",
      "A CONSTANT. Must contain exactly the words 'CUNE-SHA384'. Declares the hash algorithm used "
      "for NIE024 so that a verifier can reproduce the digest.",
      "N", "-> Sheet 6: Algoritmo CUNE (table 5.1.2)", R_NONE, "N", "Text", "Per document", "", RA, "const"),
    F("Generation date", "FechaGen", "InformacionGeneral", "NIE026", "Y", "",
      "/NominaIndividual/InformacionGeneral/@FechaGen", "10", "AAAA-MM-DD", "2026-04-05",
      "System.Document_Generation_Date",
      "Date on which the XML was generated, in Colombian time. Distinct from the payment date "
      "(NIE203) and from the settlement period (NIE004 / NIE005). It is input [2] to the CUNE, and "
      "it is the date against which the art. 8 deadline - transmission within the first 10 days of "
      "the month following the payment - is measured.",
      "Y", "-", R_NONE, "N", "Date", "Per document", "", RA, "system"),
    F("Generation time", "HoraGen", "InformacionGeneral", "NIE027", "Y", "",
      "/NominaIndividual/InformacionGeneral/@HoraGen", "14", "HH:MM:SS-05:00", "10:53:10-05:00",
      "System.Document_Generation_Time",
      "Time of generation INCLUDING the GMT offset. Colombia is UTC-05:00 all year and does not "
      "observe daylight saving, so the offset is always -05:00. Input [3] to the CUNE - a missing "
      "or wrong offset silently breaks the hash.",
      "N", "-", R_NONE, "N", "Date", "Per document", "", RA, "system"),
    F("Payroll period frequency", "PeriodoNomina", "InformacionGeneral", "NIE029", "Y", "",
      "/NominaIndividual/InformacionGeneral/@PeriodoNomina", "1", "N (code)", "5",
      "Contract.Pay_Frequency_Code",
      "Anexo Tecnico table 5.5.1: 1 Semanal, 2 Decenal, 3 Catorcenal, 4 Quincenal, 5 Mensual, 6 Otro. "
      "IMPORTANT: this describes how the EMPLOYEE IS PAID; it does NOT change the document frequency. "
      "Res. 000013 de 2021 art. 3 requires ONE monthly document per employee whatever the pay cycle, "
      "so a quincenal payroll reports PeriodoNomina = 4 on a single monthly document.",
      "Y", "-> Sheet 6: Periodo de Nomina (table 5.5.1)", R_NONE, "N", "Code", "Monthly", "", RA, "payroll"),
    F("Currency", "TipoMoneda", "InformacionGeneral", "NIE030", "Y", "",
      "/NominaIndividual/InformacionGeneral/@TipoMoneda", "3", "A (ISO 4217)", "COP",
      "Mercans.NE_Currency",
      "ISO 4217 currency of the amounts. For a Colombian payroll this is COP. Res. 000013 de 2021 "
      "art. 26 makes the Colombian peso mandatory; another currency may be ADDED to a graphical "
      "representation but never substituted.",
      "N", "-> Sheet 6: Moneda (table 5.3.2)", R_NONE, "N", "Code", "Per document", "", RA, "const"),
    F("Exchange rate", "TRM", "InformacionGeneral", "NIE200", "C",
      "Populated only where 'Currency' (NIE030) is NOT COP. Bidirectional pair: NIE030 must be a "
      "non-COP ISO code for NIE200 to be present, and NIE200 must be absent when NIE030 = COP.",
      "/NominaIndividual/InformacionGeneral/@TRM", "Var", "N (decimal)", "3950.20",
      "Mercans.FX_Rate",
      "Market representative exchange rate against the Colombian peso, used only where the document "
      "is expressed in a foreign currency. Out of scope for a standard Colombian payroll; carried "
      "here for completeness because the schema permits it.",
      "N", "-", R_XML, "N", "Rate", "Per document", "", RA, "na"),
    F("Free-text notes", "Notas", "NominaIndividual", "NIE031", "N", "",
      "/NominaIndividual/Notas", "Var", "Text", "Nomina correspondiente al mes de marzo de 2026",
      "Mercans.NE_Notes",
      "Repeating free-text element (0-N). Not read by any validation rule. Useful for a human-readable "
      "period label on the graphical representation. Never place a monetary value here - it will not "
      "be picked up by the totals.",
      "N", "-", R_NONE, "N", "Text", "Per document", "", RA, "system"),

    "DOCUMENT NUMBERING - NumeroSecuenciaXML",
    F("Employee code (in numbering block)", "CodigoTrabajador", "NumeroSecuenciaXML", "NIE009", "N", "",
      "/NominaIndividual/NumeroSecuenciaXML/@CodigoTrabajador", "Var", "A", "EMP-00417",
      "Employee.Internal_Code",
      "The employer's own internal employee code, echoed in the numbering block. Optional (0-1). "
      "Distinct from NIE063, which carries the same value inside the Trabajador element; keep both "
      "consistent or reconciliation against the HR master becomes ambiguous.",
      "Y", "-", R_NONE, "N", "Identifier", "Per document", "", RA, "payroll"),
    F("Numbering prefix", "Prefijo", "NumeroSecuenciaXML", "NIE010", "C",
      "Optional in the schema, but mandatory in practice wherever the employer has been authorised a "
      "prefix range. Bidirectional pair with 'Document number' (NIE012): NIE012 must equal Prefijo "
      "concatenated with Consecutivo (NIE011), so a Prefijo that is present here must reappear in NIE012.",
      "/NominaIndividual/NumeroSecuenciaXML/@Prefijo", "Var", "A", "NE",
      "Mercans.NE_Prefix",
      "Alphabetic prefix of the authorised numbering range, assigned to the employer by DIAN at "
      "enablement. Payroll never invents it.",
      "N", "-", R_NONE, "N", "Code", "Per document", "", RA, "system"),
    F("Consecutive number", "Consecutivo", "NumeroSecuenciaXML", "NIE011", "Y", "",
      "/NominaIndividual/NumeroSecuenciaXML/@Consecutivo", "Var", "N", "1042",
      "System.NE_Sequence",
      "Strictly increasing sequence within the authorised range. Global validation rule 90 permits a "
      "given document number to be transmitted only ONCE per employee, so the engine must persist the "
      "last-used consecutive and must never reuse it, even after a rejection.",
      "N", "-", R_NONE, "N", "Identifier", "Per document", "", RA, "system"),
    F("Document number", "Numero", "NumeroSecuenciaXML", "NIE012", "Y", "",
      "/NominaIndividual/NumeroSecuenciaXML/@Numero", "Var", "A (no spaces, no hyphens)", "NE1042",
      "System.NE_Document_Number",
      "COMPOSITE KEY - position breakdown. Numero = Prefijo (NIE010) immediately followed by "
      "Consecutivo (NIE011), with NO spaces and NO hyphens (the annex says so expressly). Sub-field 1 "
      "= the DIAN-authorised alphabetic prefix; sub-field 2 = the numeric consecutive. PERSISTENCE: "
      "unique per employee for the life of the range; it is input [1] to the CUNE, so it can never be "
      "re-issued after transmission.",
      "N", "-", R_NONE, "N", "Identifier", "Per document", "", RA, "system"),

    "PLACE OF GENERATION - LugarGeneracionXML",
    F("Generation country", "Pais", "LugarGeneracionXML", "NIE013", "Y", "",
      "/NominaIndividual/LugarGeneracionXML/@Pais", "2", "A (ISO 3166-1 alpha-2)", "CO",
      "Company.Country_Code",
      "Country in which the document was generated. Table 5.4.1. Almost always CO; it may legitimately "
      "differ where a shared service centre generates outside Colombia, which does not change the "
      "obligation.",
      "Y", "-> Sheet 6: Paises (table 5.4.1)", R_NONE, "N", "Code", "Per document", "", RA, "payroll"),
    F("Generation department", "DepartamentoEstado", "LugarGeneracionXML", "NIE014", "Y", "",
      "/NominaIndividual/LugarGeneracionXML/@DepartamentoEstado", "2", "N (DIVIPOLA)", "11",
      "Company.Department_Code",
      "Two-digit DANE DIVIPOLA department code (table 5.4.2). 11 = Bogota D.C. Must be the first two "
      "digits of the municipality code in NIE015.",
      "Y", "-> Sheet 6: Departamentos (table 5.4.2)", R_NONE, "N", "Code", "Per document", "", RA, "payroll"),
    F("Generation municipality", "MunicipioCiudad", "LugarGeneracionXML", "NIE015", "Y", "",
      "/NominaIndividual/LugarGeneracionXML/@MunicipioCiudad", "5", "N (DIVIPOLA)", "11001",
      "Company.Municipality_Code",
      "COMPOSITE KEY - position breakdown. Five-digit DANE DIVIPOLA code: positions 1-2 = department "
      "code (must equal NIE014), positions 3-5 = municipality within that department. 11001 = Bogota "
      "D.C. The annex prints the full municipality catalogue at table 5.4.3.",
      "Y", "-> Sheet 6: Municipios (table 5.4.3)", R_NONE, "N", "Code", "Per document", "", RA, "payroll"),
    F("Document language", "Idioma", "LugarGeneracionXML", "NIE016", "Y", "",
      "/NominaIndividual/LugarGeneracionXML/@Idioma", "2", "A (ISO 639-1)", "es",
      "Mercans.NE_Language",
      "ISO 639-1 two-letter language code. For Colombia this is 'es'. Res. 000013 de 2021 art. 26 "
      "makes Spanish mandatory on the graphical representation; another language may be added, never "
      "substituted.",
      "N", "-> Sheet 6: Idioma (table 5.3.1)", R_NONE, "N", "Code", "Per document", "", RA, "const"),

    "SOFTWARE PROVIDER - ProveedorXML",
    F("Provider corporate name", "RazonSocial", "ProveedorXML", "NIE205", "C",
      "Populated where the provider is a legal person. Mutually exclusive with the provider natural-"
      "person name fields NIE206-NIE209: populate RazonSocial OR the four name fields, never both.",
      "/NominaIndividual/ProveedorXML/@RazonSocial", "Var", "A", "MERCANS COLOMBIA S.A.S.",
      "Mercans.Provider_Legal_Name",
      "Corporate name of the technology provider that generated and transmits the document. Where "
      "Mercans generates on the client's behalf, Res. 000013 de 2021 art. 22 additionally requires "
      "the provider to be enabled by DIAN, registered in the RUT, and both parties to retain the "
      "mandate document.",
      "N", "-", R_NONE, "N", "Text", "Per document", "", RA, "system"),
    F("Provider first surname", "PrimerApellido", "ProveedorXML", "NIE206", "C",
      "Populated only where the provider is a natural person. Mutually exclusive with provider "
      "'RazonSocial' (NIE205).",
      "/NominaIndividual/ProveedorXML/@PrimerApellido", "60", "A", "-",
      "Mercans.Provider_First_Surname",
      "First surname of a natural-person provider. Not used where Mercans (a legal person) is the "
      "provider.", "N", "-", R_NONE, "N", "Text", "Per document", "", RA, "na"),
    F("Provider second surname", "SegundoApellido", "ProveedorXML", "NIE207", "C",
      "Populated only where the provider is a natural person. Mutually exclusive with provider "
      "'RazonSocial' (NIE205).",
      "/NominaIndividual/ProveedorXML/@SegundoApellido", "60", "A", "-",
      "Mercans.Provider_Second_Surname",
      "Second surname of a natural-person provider. Not used for a legal-person provider.",
      "N", "-", R_NONE, "N", "Text", "Per document", "", RA, "na"),
    F("Provider first name", "PrimerNombre", "ProveedorXML", "NIE208", "C",
      "Populated only where the provider is a natural person. Mutually exclusive with provider "
      "'RazonSocial' (NIE205).",
      "/NominaIndividual/ProveedorXML/@PrimerNombre", "60", "A", "-",
      "Mercans.Provider_First_Name",
      "First given name of a natural-person provider.", "N", "-", R_NONE, "N", "Text",
      "Per document", "", RA, "na"),
    F("Provider other names", "OtrosNombres", "ProveedorXML", "NIE209", "C",
      "Populated only where the provider is a natural person. Mutually exclusive with provider "
      "'RazonSocial' (NIE205).",
      "/NominaIndividual/ProveedorXML/@OtrosNombres", "60", "A", "-",
      "Mercans.Provider_Other_Names",
      "Remaining given names of a natural-person provider.", "N", "-", R_NONE, "N", "Text",
      "Per document", "", RA, "na"),
    F("Provider NIT", "NIT", "ProveedorXML", "NIE017", "Y", "",
      "/NominaIndividual/ProveedorXML/@NIT", "Var", "N (no dots, no hyphens, no DV)", "901234567",
      "Mercans.Provider_NIT",
      "Tax identification number of the software provider, without separators and WITHOUT the "
      "verification digit (which goes in NIE018). Where the employer generates its own documents, "
      "this equals the employer NIT (NIE033).",
      "N", "-", R_NONE, "N", "Identifier", "Per document", "", RA, "system"),
    F("Provider NIT verification digit", "DV", "ProveedorXML", "NIE018", "Y", "",
      "/NominaIndividual/ProveedorXML/@DV", "2", "N", "3", "Mercans.Provider_NIT_DV",
      "The DIAN check digit of the provider NIT, computed by the standard weighted modulus-11 "
      "algorithm. Carried separately from the NIT itself in every DIAN artefact.",
      "N", "-", R_NONE, "N", "Identifier", "Per document", "", RA, "system"),
    F("Software identifier", "SoftwareID", "ProveedorXML", "NIE019", "Y", "",
      "/NominaIndividual/ProveedorXML/@SoftwareID", "Var", "A (GUID)",
      "56f2ae23-4a7c-4e51-9b7d-1f2c3d4e5f60", "Mercans.SoftwareID",
      "GUID of the software enabled by DIAN for the issue of the payroll support document. Assigned "
      "at software activation. Global validation rule 92 rejects any document from an issuer or "
      "software that is not enabled.",
      "N", "-", R_NONE, "N", "Identifier", "Per document", "", RA, "system"),
    F("Software security code", "SoftwareSC", "ProveedorXML", "NIE020", "Y", "",
      "/NominaIndividual/ProveedorXML/@SoftwareSC", "96", "A (SHA-384 hex)",
      "9b1c2d3e4f5061728394a5b6c7d8e9f0a1b2c3d4e5f60718293a4b5c6d7e8f9001122334455667788990aabbccddeeff",
      "Mercans.SoftwareSC",
      "COMPOSITE KEY - position breakdown. SHA-384 digest of three concatenated inputs (Anexo Tecnico "
      "s.8.2): [1] SoftwareID (NIE019), [2] the secret software PIN - which never appears in the XML, "
      "[3] the document number (NIE012). PERSISTENCE: it therefore changes with EVERY document, "
      "unlike the SoftwareID which is constant. Treat the PIN as a secret of restricted circulation; "
      "it is also input [10] to the CUNE.",
      "N", "-", R_NONE, "N", "Identifier", "Per document", "", RA, "system"),

    "EMPLOYER - Empleador",
    F("Employer corporate name", "RazonSocial", "Empleador", "NIE032", "C",
      "Populated where the employer is a legal person. Mutually exclusive with the employer natural-"
      "person name fields NIE210-NIE213: populate RazonSocial OR the four name fields, never both.",
      "/NominaIndividual/Empleador/@RazonSocial", "Var", "A", "MERCANS COLOMBIA S.A.S.",
      "Company.Legal_Name",
      "Registered corporate name exactly as held in the RUT. Item 1 of the thirteen mandatory content "
      "items of Res. 000013 de 2021 art. 5.",
      "Y", "-", R_NONE, "N", "Text", "Per document", "", RA, "payroll"),
    F("Employer first surname", "PrimerApellido", "Empleador", "NIE210", "C",
      "Populated only where the employer is a natural person. Mutually exclusive with employer "
      "'RazonSocial' (NIE032).",
      "/NominaIndividual/Empleador/@PrimerApellido", "60", "A", "-", "Company.First_Surname",
      "First surname where the employer is an individual (a natural-person employer is common in "
      "Colombian domestic service and micro-enterprise).",
      "Y", "-", R_NONE, "N", "Text", "Per document", "", RA, "payroll"),
    F("Employer second surname", "SegundoApellido", "Empleador", "NIE211", "C",
      "Populated only where the employer is a natural person. Mutually exclusive with employer "
      "'RazonSocial' (NIE032).",
      "/NominaIndividual/Empleador/@SegundoApellido", "60", "A", "-", "Company.Second_Surname",
      "Second surname of a natural-person employer.", "Y", "-", R_NONE, "N", "Text",
      "Per document", "", RA, "payroll"),
    F("Employer first name", "PrimerNombre", "Empleador", "NIE212", "C",
      "Populated only where the employer is a natural person. Mutually exclusive with employer "
      "'RazonSocial' (NIE032).",
      "/NominaIndividual/Empleador/@PrimerNombre", "60", "A", "-", "Company.First_Name",
      "First given name of a natural-person employer.", "Y", "-", R_NONE, "N", "Text",
      "Per document", "", RA, "payroll"),
    F("Employer other names", "OtrosNombres", "Empleador", "NIE213", "C",
      "Populated only where the employer is a natural person. Mutually exclusive with employer "
      "'RazonSocial' (NIE032).",
      "/NominaIndividual/Empleador/@OtrosNombres", "60", "A", "-", "Company.Other_Names",
      "Remaining given names of a natural-person employer.", "Y", "-", R_NONE, "N", "Text",
      "Per document", "", RA, "payroll"),
    F("Employer NIT", "NIT", "Empleador", "NIE033", "Y", "",
      "/NominaIndividual/Empleador/@NIT", "Var", "N (no dots, no hyphens, no DV)", "900123456",
      "Company.NIT",
      "Tax identification number of the employer issuing the document, without dots, hyphens or the "
      "verification digit. It is input [7] to the CUNE and the join key to Formulario 350, "
      "Formulario 220 and PILA. Item 1 of the art. 5 mandatory content.",
      "Y", "-", R_NONE, "N", "Identifier", "Per document", "", RA, "payroll"),
    F("Employer NIT verification digit", "DV", "Empleador", "NIE034", "Y", "",
      "/NominaIndividual/Empleador/@DV", "2", "N", "7", "Company.NIT_DV",
      "DIAN check digit of the employer NIT. Deliberately excluded from the CUNE input, which uses "
      "the NIT alone - a frequent source of hash mismatches.",
      "Y", "-", R_NONE, "N", "Identifier", "Per document", "", RA, "payroll"),
    F("Employer country", "Pais", "Empleador", "NIE035", "Y", "",
      "/NominaIndividual/Empleador/@Pais", "2", "A (ISO 3166-1 alpha-2)", "CO",
      "Company.Country_Code",
      "Country of the employer. Item 11 of the art. 5 mandatory content (country, department and "
      "municipality of origin).",
      "Y", "-> Sheet 6: Paises (table 5.4.1)", R_NONE, "N", "Code", "Per document", "", RA, "payroll"),
    F("Employer department", "DepartamentoEstado", "Empleador", "NIE036", "Y", "",
      "/NominaIndividual/Empleador/@DepartamentoEstado", "2", "N (DIVIPOLA)", "11",
      "Company.Department_Code",
      "Two-digit DIVIPOLA department of the employer. Must be the first two digits of NIE037.",
      "Y", "-> Sheet 6: Departamentos (table 5.4.2)", R_NONE, "N", "Code", "Per document", "", RA, "payroll"),
    F("Employer municipality", "MunicipioCiudad", "Empleador", "NIE037", "Y", "",
      "/NominaIndividual/Empleador/@MunicipioCiudad", "5", "N (DIVIPOLA)", "11001",
      "Company.Municipality_Code",
      "COMPOSITE KEY - position breakdown: positions 1-2 = department (= NIE036), positions 3-5 = "
      "municipality. Sourced from the DANE DIVIPOLA catalogue reproduced at annex table 5.4.3.",
      "Y", "-> Sheet 6: Municipios (table 5.4.3)", R_NONE, "N", "Code", "Per document", "", RA, "payroll"),
    F("Employer address", "Direccion", "Empleador", "NIE038", "Y", "",
      "/NominaIndividual/Empleador/@Direccion", "Var", "A", "CALLE 100 No 7-33 PISO 12",
      "Company.Address",
      "Street address of the employer as registered. Free text; the annex imposes no structure. Part "
      "of art. 5 item 11.",
      "Y", "-", R_NONE, "N", "Text", "Per document", "", RA, "payroll"),

    "EMPLOYEE - Trabajador",
    F("Worker type", "TipoTrabajador", "Trabajador", "NIE041", "Y", "",
      "/NominaIndividual/Trabajador/@TipoTrabajador", "2", "N (code)", "01",
      "Employee.Worker_Type_Code",
      "Annex table 5.5.3 - a SIXTEEN-value list (01, 02, 04, 12, 18, 19, 21, 22, 23, 30, 31, 47, 51, "
      "54, 56, 58). It is a SUBSET of the PILA tipo cotizante list, which has far more values, so the "
      "engine must map, not copy: PILA codes with no DIAN equivalent (for example 03 independiente, "
      "16, 20, 32-45, 52, 53, 55, 57, 59-63) are not valid here.",
      "Y", "-> Sheet 6: Tipo de Trabajador (table 5.5.3)", R_NONE, "N", "Code", "Monthly", "", RA, "payroll"),
    F("Worker sub-type", "SubTipoTrabajador", "Trabajador", "NIE042", "Y", "",
      "/NominaIndividual/Trabajador/@SubTipoTrabajador", "2", "N (code)", "00",
      "Employee.Worker_SubType_Code",
      "Annex table 5.5.4 recognises only TWO values: 00 No Aplica and 01 Dependiente pensionado por "
      "vejez activo. This is much narrower than the twelve-value PILA subtipo list; an employed "
      "old-age pensioner is 01, everyone else is 00.",
      "Y", "-> Sheet 6: Subtipo de Trabajador (table 5.5.4)", R_NONE, "N", "Code", "Monthly", "", RA, "payroll"),
    F("High-risk pension flag", "AltoRiesgoPension", "Trabajador", "NIE043", "Y", "",
      "/NominaIndividual/Trabajador/@AltoRiesgoPension", "4-5", "Boolean (true / false)", "false",
      "Employee.High_Risk_Pension_Flag",
      "Whether the employee performs an activity classified as high-risk under Decreto Ley 2090 de "
      "2003, which carries an ADDITIONAL employer pension contribution and a reduced pension age. "
      "Always present (1-1); write the literal true or false. See scope_manifest CO-GAP-02: the 2026 "
      "additional rate and its base require RA confirmation before any high-risk employee is "
      "configured.",
      "Y", "-", R_NONE, "N", "Flag", "Monthly",
      "CO-GAP-02: confirm the 2026 additional high-risk pension rate and its base against the current "
      "implementing decree before configuring any high-risk employee.", RA, "payroll"),
    F("Employee document type", "TipoDocumento", "Trabajador", "NIE044", "Y", "",
      "/NominaIndividual/Trabajador/@TipoDocumento", "2", "N (code)", "13",
      "Employee.Document_Type",
      "Annex table 5.2.1: 11 Registro civil, 12 Tarjeta de identidad, 13 Cedula de ciudadania, "
      "21 Tarjeta de extranjeria, 22 Cedula de extranjeria, 31 NIT, 41 Pasaporte, 42 Documento de "
      "identificacion extranjero, 47 PEP, 50 NIT de otro pais, 91 NUIP (employee only). NOTE "
      "CO-GAP-06: there is NO code for the PPT (Permiso por Proteccion Temporal, Decreto 216 de "
      "2021), created one month after this annex; 47 (PEP) is the only available proxy.",
      "Y", "-> Sheet 6: Tipo de Documento (table 5.2.1)", R_NONE, "N", "Code", "Monthly",
      "CO-GAP-06: confirm the client's position on reporting PPT holders under code 47 (PEP).",
      RA, "payroll"),
    F("Employee document number", "NumeroDocumento", "Trabajador", "NIE045", "Y", "",
      "/NominaIndividual/Trabajador/@NumeroDocumento", "Var", "N (xsd:integer in the XSD)",
      "1020304050", "Employee.Document_Number",
      "Identity document number without dots or hyphens. It is input [8] to the CUNE and the join key "
      "to Formulario 220 and Formato 2276. CO-GAP-07 - KNOWN SCHEMA DEFECT: the XSD types this "
      "attribute as xsd:integer, so a passport or foreign identity document containing letters "
      "(document types 21, 41, 42, 50) cannot be schema-valid. DIAN has published no workaround; "
      "escalate per client.",
      "Y", "-", R_NONE, "N", "Identifier", "Monthly",
      "CO-GAP-07: xsd:integer typing blocks alphanumeric foreign document numbers. Confirm the "
      "client-specific escalation route with DIAN.", RA, "payroll"),
    F("Employee first surname", "PrimerApellido", "Trabajador", "NIE046", "Y", "",
      "/NominaIndividual/Trabajador/@PrimerApellido", "60", "A", "PEREZ",
      "Employee.First_Surname",
      "First surname. Item 2 of the art. 5 mandatory content.",
      "Y", "-", R_NONE, "N", "Text", "Monthly", "", RA, "payroll"),
    F("Employee second surname", "SegundoApellido", "Trabajador", "NIE047", "Y", "",
      "/NominaIndividual/Trabajador/@SegundoApellido", "60", "A", "GOMEZ",
      "Employee.Second_Surname",
      "Second surname. CO-GAP-07 - KNOWN SCHEMA DEFECT: this attribute is use=required, yet many "
      "Colombians and virtually all foreign nationals have only one surname. Mercans emits a "
      "placeholder; no official workaround is published.",
      "Y", "-", R_NONE, "N", "Text", "Monthly",
      "CO-GAP-07: confirm the client's chosen placeholder for a single-surname employee.", RA, "payroll"),
    F("Employee first name", "PrimerNombre", "Trabajador", "NIE048", "Y", "",
      "/NominaIndividual/Trabajador/@PrimerNombre", "60", "A", "JUAN",
      "Employee.First_Name",
      "First given name. Mandatory (1-1).", "Y", "-", R_NONE, "N", "Text", "Monthly", "", RA, "payroll"),
    F("Employee other names", "OtrosNombres", "Trabajador", "NIE049", "N", "",
      "/NominaIndividual/Trabajador/@OtrosNombres", "60", "A", "CARLOS",
      "Employee.Other_Names",
      "Remaining given names. The ONLY optional (0-1) name attribute on the employee - the two "
      "surnames and the first name are all required.",
      "Y", "-", R_NONE, "N", "Text", "Monthly", "", RA, "payroll"),
    F("Place of work - country", "LugarTrabajoPais", "Trabajador", "NIE050", "Y", "",
      "/NominaIndividual/Trabajador/@LugarTrabajoPais", "3", "N / A (table 5.4.1)", "CO",
      "Employee.Work_Country_Code",
      "Country where the work is performed. Materially important for tax: employment income of a "
      "NON-RESIDENT for work performed entirely OUTSIDE Colombia is foreign-source and not subject "
      "to Colombian withholding (DIAN Oficio 28380 of 2019), whereas a resident is taxed on worldwide "
      "income.",
      "Y", "-> Sheet 6: Paises (table 5.4.1)", R_NONE, "N", "Code", "Monthly", "", RA, "payroll"),
    F("Place of work - department", "LugarTrabajoDepartamentoEstado", "Trabajador", "NIE051", "Y", "",
      "/NominaIndividual/Trabajador/@LugarTrabajoDepartamentoEstado", "2", "N (DIVIPOLA)", "11",
      "Employee.Work_Department_Code",
      "DIVIPOLA department of the place of work. Should reconcile to PILA Registro Tipo 2 field 9 "
      "(codigo del departamento de la ubicacion laboral) for the same employee and month.",
      "Y", "-> Sheet 6: Departamentos (table 5.4.2)", R_NONE, "N", "Code", "Monthly", "", RA, "payroll"),
    F("Place of work - municipality", "LugarTrabajoMunicipioCiudad", "Trabajador", "NIE052", "Y", "",
      "/NominaIndividual/Trabajador/@LugarTrabajoMunicipioCiudad", "5", "N (DIVIPOLA)", "11001",
      "Employee.Work_Municipality_Code",
      "COMPOSITE KEY - positions 1-2 = department (= NIE051), positions 3-5 = municipality. Reconciles "
      "to PILA Registro Tipo 2 field 10.",
      "Y", "-> Sheet 6: Municipios (table 5.4.3)", R_NONE, "N", "Code", "Monthly", "", RA, "payroll"),
    F("Place of work - address", "LugarTrabajoDireccion", "Trabajador", "NIE053", "Y", "",
      "/NominaIndividual/Trabajador/@LugarTrabajoDireccion", "Var", "A", "CALLE 100 No 7-33 PISO 12",
      "Employee.Work_Address",
      "Street address of the place of work. For a teleworker this is the agreed remote workplace, not "
      "the employer's registered office.",
      "Y", "-", R_NONE, "N", "Text", "Monthly", "", RA, "payroll"),
    F("All-inclusive salary flag", "SalarioIntegral", "Trabajador", "NIE056", "Y", "",
      "/NominaIndividual/Trabajador/@SalarioIntegral", "4-5", "Boolean (true / false)", "false",
      "Employee.Integral_Salary_Flag",
      "Whether the employee is on an all-inclusive salary under CST art. 132 num. 2 (minimum 13 SMMLV "
      "= COP 22,761,765 in 2026, of which 70% is salary and 30% is the prestacional factor). Where "
      "true, the contribution base is 70% of the integral salary and no separate prima, cesantias or "
      "interest accrues - which changes what may legitimately appear in the Devengados block.",
      "Y", "-", R_NONE, "N", "Flag", "Monthly", "", RA, "payroll"),
    F("Contract type", "TipoContrato", "Trabajador", "NIE061", "Y", "",
      "/NominaIndividual/Trabajador/@TipoContrato", "1", "N (code)", "2",
      "Contract.Type_Code",
      "Annex table 5.5.2: 1 Termino Fijo, 2 Termino Indefinido, 3 Obra o Labor, 4 Aprendizaje, "
      "5 Practicas o Pasantias. Ley 2466 de 2025 art. 21 recast the apprenticeship as a labour "
      "contract, so code 4 now denotes a genuine employment relationship.",
      "Y", "-> Sheet 6: Tipo de Contrato (table 5.5.2)", R_NONE, "N", "Code", "Monthly", "", RA, "payroll"),
    F("Contractual salary", "Sueldo", "Trabajador", "NIE062", "Y", "",
      "/NominaIndividual/Trabajador/@Sueldo", "Var", "N (decimal 2)", "12000000.00",
      "Contract.Contractual_Salary",
      "The CONTRACTUAL monthly salary, not the amount actually paid for the period. It stays constant "
      "across a month with unpaid leave or a mid-month hire, whereas SueldoTrabajado (NIE070) moves. "
      "Never below 1 SMMLV (COP 1,750,905 in 2026) for a full-time employee.",
      "Y", "-", R_XML, "N", "Amount", "Monthly", "", RA, "payroll"),
    F("Employee internal code", "CodigoTrabajador", "Trabajador", "NIE063", "N", "",
      "/NominaIndividual/Trabajador/@CodigoTrabajador", "Var", "A", "EMP-00417",
      "Employee.Internal_Code",
      "The employer's own payroll number for the employee. Optional. Keep consistent with NIE009, "
      "which carries the same value in the numbering block.",
      "Y", "-", R_NONE, "N", "Identifier", "Monthly", "", RA, "payroll"),

    "PAYMENT - Pago and FechasPagos",
    F("Payment form", "Forma", "Pago", "NIE064", "Y", "",
      "/NominaIndividual/Pago/@Forma", "1", "N (code)", "1", "Contract.Payment_Form_Code",
      "Annex table 5.3.3.1. The table publishes a SINGLE value, 1 = Contado (cash / immediate). Item "
      "10 of the art. 5 mandatory content (payment method and medium).",
      "Y", "-> Sheet 6: Forma de Pago (table 5.3.3.1)", R_NONE, "N", "Code", "Monthly", "", RA, "payroll"),
    F("Payment method", "Metodo", "Pago", "NIE065", "Y", "",
      "/NominaIndividual/Pago/@Metodo", "2", "N (code)", "42", "Contract.Payment_Method_Code",
      "Annex table 5.3.3.2 - the full UN/EDIFACT 4461 medium-of-payment list (1 to 97). For a "
      "Colombian salary the realistic values are 42 Consignacion bancaria, 45 Transferencia Credito "
      "Bancario, 10 Efectivo and 20 Cheque. Item 10 of the art. 5 mandatory content.",
      "Y", "-> Sheet 6: Medio de Pago (table 5.3.3.2)", R_NONE, "N", "Code", "Monthly", "", RA, "payroll"),
    F("Bank", "Banco", "Pago", "NIE066", "C",
      "Populated where 'Payment method' (NIE065) is a bank-mediated medium (42, 45, 46, 47, 48, 49 "
      "and similar). Must be absent or empty where NIE065 = 10 Efectivo. Bidirectional pair with "
      "NIE065 and with 'Account number' (NIE068).",
      "/NominaIndividual/Pago/@Banco", "Var", "A", "BANCOLOMBIA", "Employee.Bank_Name",
      "Name of the receiving bank. Free text - Colombia has no national bank-code catalogue in this "
      "annex, and the clearing-house entity codes used in the bank payment file are bank-specific "
      "and obtained per client.",
      "Y", "-", R_NONE, "N", "Text", "Monthly", "", RA, "payroll"),
    F("Account type", "TipoCuenta", "Pago", "NIE067", "C",
      "Populated together with 'Bank' (NIE066) and 'Account number' (NIE068) whenever 'Payment "
      "method' (NIE065) is a bank-mediated medium. Absent for a cash payment.",
      "/NominaIndividual/Pago/@TipoCuenta", "Var", "A", "AHORROS", "Employee.Bank_Account_Type",
      "Ahorros (savings) or Corriente (current). Free text in the annex; standardise it at "
      "configuration so the value is stable across the payment file and the XML.",
      "Y", "-", R_NONE, "N", "Text", "Monthly", "", RA, "payroll"),
    F("Account number", "NumeroCuenta", "Pago", "NIE068", "C",
      "Populated together with 'Bank' (NIE066) and 'Account type' (NIE067) whenever 'Payment method' "
      "(NIE065) is a bank-mediated medium. Absent for a cash payment.",
      "/NominaIndividual/Pago/@NumeroCuenta", "Var", "A", "12345678901",
      "Employee.Bank_Account_Number",
      "Domestic account number. COLOMBIA DOES NOT USE IBAN. Account numbers are numeric, of "
      "bank-specific length (commonly 10-17 digits) with no national check-digit standard, so the "
      "engine cannot validate them structurally - only by bank-specific rule or by pre-notification.",
      "Y", "-", R_NONE, "N", "Identifier", "Monthly", "", RA, "payroll"),
    F("Payment date", "FechaPago", "FechasPagos", "NIE203", "Y", "",
      "/NominaIndividual/FechasPagos/FechaPago", "10", "AAAA-MM-DD", "2026-03-31",
      "Payroll.Payment_Date",
      "Repeating element, cardinality 1-N: one occurrence per actual payment inside the reported "
      "month. A quincenal payroll reports TWO FechaPago values on ONE monthly document. Item 5 of "
      "the art. 5 mandatory content, and the date that fixes the art. 8 transmission deadline.",
      "Y", "-", R_NONE, "N", "Date", "Per record", "", RA, "payroll"),

    "PERIOD - Periodo",
    F("Hire date", "FechaIngreso", "Periodo", "NIE002", "Y", "",
      "/NominaIndividual/Periodo/@FechaIngreso", "10", "AAAA-MM-DD", "2021-01-11",
      "Contract.Start_Date",
      "Date the employee joined the employer. Constant across every document for that relationship; "
      "it drives TiempoLaborado (NIE006), the cesantias accrual and the seniority-based severance "
      "calculation.",
      "Y", "-", R_NONE, "N", "Date", "Monthly", "", RA, "payroll"),
    F("Termination date", "FechaRetiro", "Periodo", "NIE003", "C",
      "Populated only on the document for the month in which the employment relationship ends. "
      "Where present, it must fall inside or before the settlement window bounded by "
      "'Settlement start' (NIE004) and 'Settlement end' (NIE005).",
      "/NominaIndividual/Periodo/@FechaRetiro", "10", "AAAA-MM-DD", "-", "Contract.End_Date",
      "Leaving date. Cardinality 0-1. Its presence signals the final settlement document, which "
      "typically also carries VacacionesCompensadas, Cesantias, Indemnizacion and BonifRetiro "
      "devengado elements that do not appear in an ordinary month.",
      "Y", "-", R_NONE, "N", "Date", "Per event", "", RA, "payroll"),
    F("Settlement period start", "FechaLiquidacionInicio", "Periodo", "NIE004", "Y", "",
      "/NominaIndividual/Periodo/@FechaLiquidacionInicio", "10", "AAAA-MM-DD", "2026-03-01",
      "PayPeriod.Start_Date",
      "First day of the period the document settles. For the standard monthly document this is the "
      "first day of the calendar month, or the hire date in a joining month.",
      "Y", "-", R_NONE, "N", "Date", "Monthly", "", RA, "system"),
    F("Settlement period end", "FechaLiquidacionFin", "Periodo", "NIE005", "Y", "",
      "/NominaIndividual/Periodo/@FechaLiquidacionFin", "10", "AAAA-MM-DD", "2026-03-31",
      "PayPeriod.End_Date",
      "Last day of the settled period. Must be on or after NIE004. One document per employee per "
      "month whatever the pay cycle (art. 3).",
      "Y", "-", R_NONE, "N", "Date", "Monthly", "", RA, "system"),
    F("Time worked", "TiempoLaborado", "Periodo", "NIE006", "Y", "",
      "/NominaIndividual/Periodo/@TiempoLaborado", "Var", "N (days, decimal 2)", "1875.00",
      "Payroll.Service_Days",
      "COMPOSITE VALUE - construction rule. Cumulative service with the employer expressed in DAYS on "
      "the Colombian commercial-year convention fixed by Anexo Tecnico s.8.3.1: 1 year = 360 days, "
      "1 month = 30 days. The annex's own worked example is 5 years + 3 months + 18 days = "
      "(5 x 360) + (3 x 30) + 18 = 1908.00. Sub-fields: [years x 360] + [months x 30] + [odd days]. "
      "PERSISTENCE: recomputed every month from FechaIngreso (NIE002) to the settlement end; it is "
      "cumulative service, NOT days worked in the period (that is DiasTrabajados, NIE069).",
      "Y", "-", "Two decimals, per the annex example (1908.00).", "N", "Count", "Monthly", "", RA, "payroll"),
    F("Generation date (period block)", "FechaGen", "Periodo", "NIE008", "Y", "",
      "/NominaIndividual/Periodo/@FechaGen", "10", "AAAA-MM-DD", "2026-04-05",
      "System.Document_Generation_Date",
      "The generation date repeated inside the Periodo element, considering the Colombian time zone "
      "(UTC-05:00). Must equal NIE026; a mismatch between the two is a common rejection.",
      "N", "-", R_NONE, "N", "Date", "Monthly", "", RA, "system"),

    "ACCRUED - BASIC AND TRANSPORT (Devengados)",
    F("Days worked", "DiasTrabajados", "Devengados / Basico", "NIE069", "Y", "",
      "/NominaIndividual/Devengados/Basico/@DiasTrabajados", "1-2", "N (integer)", "30",
      "Payroll.Days_Worked",
      "Days actually worked and paid in the period, on the 30-day commercial month. Distinct from "
      "TiempoLaborado (NIE006), which is cumulative service. Reduced by unpaid leave, by suspension "
      "and by a mid-month hire or leave.",
      "Y", "-", R_NONE, "N", "Count", "Monthly", "", RA, "payroll"),
    F("Salary paid for the period", "SueldoTrabajado", "Devengados / Basico", "NIE070", "Y", "",
      "/NominaIndividual/Devengados/Basico/@SueldoTrabajado", "Var", "N (decimal 2)", "12000000.00",
      "Payroll.Basic_Salary_Paid",
      "The basic salary actually earned for the days worked. Moves with DiasTrabajados; contrast "
      "Sueldo (NIE062), which is the static contractual figure. This is the single largest input to "
      "the ET art. 388 depurated withholding base and to the PILA contribution base.",
      "Y", "-", R_XML, "N", "Amount", "Monthly", "", RA, "payroll"),
    F("Transport allowance", "AuxilioTransporte", "Devengados / Transporte", "NIE071", "C",
      "Payable ONLY where the employee earns up to 2 SMMLV (COP 3,501,810 in 2026) - Ley 15 de 1959 "
      "and the annual transport-allowance decree. Where the employee is above the threshold this "
      "element is omitted, not zero-filled.",
      "/NominaIndividual/Devengados/Transporte/@AuxilioTransporte", "Var", "N (decimal 2)", "-",
      "Payroll.Transport_Allowance",
      "The statutory transport allowance, COP 249,095 per month in 2026. It is NOT salary for "
      "contribution purposes but IS included in the base of cesantias, prima and the severance "
      "indemnity (CST art. 7 of Ley 1 de 1963) - one of the sharpest base differences in Colombian "
      "payroll.",
      "Y", "-", R_XML, "N", "Amount", "Monthly", "", RA, "payroll"),
    F("Travel and accommodation allowance - salary", "ViaticoManuAlojS",
      "Devengados / Transporte", "NIE072", "C",
      "Paired salary / non-salary element. Populate the S element for the PERMANENT portion of "
      "viaticos, which is salary under CST art. 130; the accidental portion goes to the NS element "
      "(NIE073). Bidirectional pair - the split must be decided at wage-type configuration, never "
      "derived at reporting time.",
      "/NominaIndividual/Devengados/Transporte/@ViaticoManuAlojS", "Var", "N (decimal 2)", "-",
      "Payroll.Per_Diem_Salary",
      "Permanent travel, meal and accommodation allowances that constitute salary and therefore enter "
      "the contribution base and the withholding base.",
      "Y", "-", R_XML, "N", "Amount", "Monthly", "", RA, "payroll"),
    F("Travel and accommodation allowance - non-salary", "ViaticoManuAlojNS",
      "Devengados / Transporte", "NIE073", "C",
      "Paired with 'Travel and accommodation allowance - salary' (NIE072). Populate NS for the "
      "accidental / occasional portion, which is not salary under CST art. 130.",
      "/NominaIndividual/Devengados/Transporte/@ViaticoManuAlojNS", "Var", "N (decimal 2)", "-",
      "Payroll.Per_Diem_NonSalary",
      "Accidental travel allowances that are not salary. Still reported, still part of the accrued "
      "total, but excluded from the contribution base - subject to the 40% non-salary clamp of "
      "Ley 1393 de 2010 art. 30.",
      "Y", "-", R_XML, "N", "Amount", "Monthly", "", RA, "payroll"),
]

FIELDS += ["ACCRUED - OVERTIME AND PREMIUM HOURS (7 types, table 5.5.5)"]
FIELDS += _hour_rows()

FIELDS += [
    "ACCRUED - VACATION AND STATUTORY BENEFITS",
    F("Vacation taken - start date", "VacacionesComunes - FechaInicio",
      "Devengados / VacacionesComunes", "NIE109", "C",
      "Optional (0-1) but required by the RA where vacation is reported, and pairs with 'Vacation "
      "taken - end date' (NIE110): if one is present the other must be.",
      "/NominaIndividual/Devengados/Vacaciones/Comunes/@FechaInicio", "10", "AAAA-MM-DD", "-",
      "Payroll.Vacation_Start_Date",
      "First day of the vacation period actually enjoyed. Repeating block (0-N) - two separate "
      "vacation stretches in one month are two elements.",
      "Y", "-", R_NONE, "N", "Date", "Per record", "", RA, "payroll"),
    F("Vacation taken - end date", "VacacionesComunes - FechaFin",
      "Devengados / VacacionesComunes", "NIE110", "C",
      "Pairs with 'Vacation taken - start date' (NIE109); required whenever NIE109 is present.",
      "/NominaIndividual/Devengados/Vacaciones/Comunes/@FechaFin", "10", "AAAA-MM-DD", "-",
      "Payroll.Vacation_End_Date",
      "Last day of the vacation period enjoyed. Must be on or after NIE109.",
      "Y", "-", R_NONE, "N", "Date", "Per record", "", RA, "payroll"),
    F("Vacation taken - days", "VacacionesComunes - Cantidad",
      "Devengados / VacacionesComunes", "NIE111", "Y", "",
      "/NominaIndividual/Devengados/Vacaciones/Comunes/@Cantidad", "Var", "N (integer days)", "-",
      "Payroll.Vacation_Days_Taken",
      "Number of vacation days enjoyed. Colombia grants 15 WORKING days per year of service "
      "(CST art. 186); the accumulation limits of CST art. 190 are an engine rule, not an XML rule.",
      "Y", "-", R_NONE, "N", "Count", "Per record", "", RA, "payroll"),
    F("Vacation taken - amount", "VacacionesComunes - Pago",
      "Devengados / VacacionesComunes", "NIE112", "Y", "",
      "/NominaIndividual/Devengados/Vacaciones/Comunes/@Pago", "Var", "N (decimal 2)", "-",
      "Payroll.Vacation_Pay",
      "Money value of the vacation enjoyed. Vacation pay IS part of the contribution base; note that "
      "vacation is paid on ordinary salary excluding overtime (CST art. 192).",
      "Y", "-", R_XML, "N", "Amount", "Per record", "", RA, "payroll"),
    F("Vacation compensated in cash - days", "VacacionesCompensadas - Cantidad",
      "Devengados / VacacionesCompensadas", "NIE115", "Y", "",
      "/NominaIndividual/Devengados/Vacaciones/Compensadas/@Cantidad", "Var", "N (integer days)", "-",
      "Payroll.Vacation_Days_Compensated",
      "Vacation days paid in cash instead of enjoyed. A SEPARATE element from vacation taken, because "
      "compensated vacation is NOT part of the social-security contribution base while enjoyed "
      "vacation is - the engine must not merge them.",
      "Y", "-", R_NONE, "N", "Count", "Per record", "", RA, "payroll"),
    F("Vacation compensated in cash - amount", "VacacionesCompensadas - Pago",
      "Devengados / VacacionesCompensadas", "NIE116", "Y", "",
      "/NominaIndividual/Devengados/Vacaciones/Compensadas/@Pago", "Var", "N (decimal 2)", "-",
      "Payroll.Vacation_Compensation",
      "Cash value of the compensated vacation days. Typical on a final settlement.",
      "Y", "-", R_XML, "N", "Amount", "Per record", "", RA, "payroll"),
    F("Service bonus - days", "Primas - Cantidad", "Devengados / Primas", "NIE117", "Y", "",
      "/NominaIndividual/Devengados/Primas/@Cantidad", "Var", "N (integer days)", "-",
      "Payroll.Prima_Days",
      "Days of service on which the statutory service bonus (prima de servicios, CST art. 306) is "
      "computed. Paid in two instalments, by 30 June and by 20 December.",
      "Y", "-", R_NONE, "N", "Count", "Per record", "", RA, "payroll"),
    F("Service bonus - amount (salary)", "Primas - Pago", "Devengados / Primas", "NIE118", "Y", "",
      "/NominaIndividual/Devengados/Primas/@Pago", "Var", "N (decimal 2)", "-",
      "Payroll.Prima_Amount",
      "The statutory service bonus. Under Procedure 1 the STATUTORY MINIMUM bonus is withheld "
      "SEPARATELY on its own read of the ET art. 383 table (art. 385) - it does not merge into the "
      "ordinary monthly base. Any excess over the statutory minimum is ordinary income.",
      "Y", "-", R_XML, "N", "Amount", "Per record", "", RA, "payroll"),
    F("Service bonus - amount (non-salary)", "Primas - PagoNS", "Devengados / Primas", "NIE119", "C",
      "Populated only for the extra-legal, non-salary portion of a bonus agreed as non-salary. Pairs "
      "with 'Service bonus - amount (salary)' (NIE118): the salary and non-salary portions are "
      "separate elements and must never be summed into one.",
      "/NominaIndividual/Devengados/Primas/@PagoNS", "Var", "N (decimal 2)", "-",
      "Payroll.Prima_NonSalary",
      "Non-salary portion of a bonus. Counts toward the 40% non-salary clamp of Ley 1393 de 2010 "
      "art. 30 for contribution purposes.",
      "Y", "-", R_XML, "N", "Amount", "Per record", "", RA, "payroll"),
    F("Severance savings - amount", "Cesantias - Pago", "Devengados / Cesantias", "NIE120", "Y", "",
      "/NominaIndividual/Devengados/Cesantias/@Pago", "Var", "N (decimal 2)", "-",
      "Payroll.Cesantias_Amount",
      "Severance savings (auxilio de cesantia, CST art. 249 / Ley 50 de 1990 art. 99): one month's "
      "salary per year of service. EXCLUDED from the monthly withholding base under both procedures "
      "because of the ET art. 206 num. 4 exemption and its taper. Cross-report: this is the figure "
      "that must reconcile to Formulario 220 casillas 47-49 and to Formato 2276 numerals 18-20.",
      "Y", "-", R_XML, "N", "Amount", "Per record", "", RA, "payroll"),
    F("Severance savings - interest rate", "Cesantias - Porcentaje",
      "Devengados / Cesantias", "NIE121", "Y", "",
      "/NominaIndividual/Devengados/Cesantias/@Porcentaje", "Var", "N (decimal)", "12.00",
      "Mercans.Cesantias_Interest_Rate",
      "The statutory interest rate on severance savings: 12% per annum, or pro rata for a partial "
      "year (Ley 52 de 1975 art. 1). A CONFIGURATION constant, not a payroll calculation.",
      "Y", "-> Sheet 6: Cesantias interest rate", "Rate to 2 decimals.", "N", "Rate",
      "Per record", "", RA, "system"),
    F("Severance savings - interest amount", "Cesantias - PagoIntereses",
      "Devengados / Cesantias", "NIE122", "Y", "",
      "/NominaIndividual/Devengados/Cesantias/@PagoIntereses", "Var", "N (decimal 2)", "-",
      "Payroll.Cesantias_Interest",
      "Interest on severance savings, payable TO THE EMPLOYEE during January for the balance at the "
      "preceding 31 December. Ley 2466 de 2025 art. 64 additionally permits monthly payment of the "
      "1% by written agreement, which the engine must support as a configurable option.",
      "Y", "-", R_XML, "N", "Amount", "Per record", "", RA, "payroll"),

    "ACCRUED - INCAPACITY AND LEAVE",
    F("Incapacity - start date", "Incapacidad - FechaInicio",
      "Devengados / Incapacidad", "NIE123", "C",
      "Optional (0-1); pairs with 'Incapacity - end date' (NIE124). Where one is present the other "
      "must be present.",
      "/NominaIndividual/Devengados/Incapacidades/Incapacidad/@FechaInicio", "10", "AAAA-MM-DD", "-",
      "Payroll.Incapacity_Start_Date",
      "First day of the incapacity. Repeating block (0-N): one element per incapacity episode, and "
      "an episode that changes type mid-way is split.",
      "Y", "-", R_NONE, "N", "Date", "Per record", "", RA, "payroll"),
    F("Incapacity - end date", "Incapacidad - FechaFin",
      "Devengados / Incapacidad", "NIE124", "C",
      "Pairs with 'Incapacity - start date' (NIE123); required whenever NIE123 is present.",
      "/NominaIndividual/Devengados/Incapacidades/Incapacidad/@FechaFin", "10", "AAAA-MM-DD", "-",
      "Payroll.Incapacity_End_Date",
      "Last day of the incapacity episode.", "Y", "-", R_NONE, "N", "Date", "Per record", "", RA, "payroll"),
    F("Incapacity - days", "Incapacidad - Cantidad", "Devengados / Incapacidad", "NIE125", "Y", "",
      "/NominaIndividual/Devengados/Incapacidades/Incapacidad/@Cantidad", "Var",
      "N (integer days)", "-", "Payroll.Incapacity_Days",
      "Days of incapacity in the episode. Must reconcile to the PILA change-event day counts (IGE, "
      "IRL) for the same employee and month.",
      "Y", "-", R_NONE, "N", "Count", "Per record", "", RA, "payroll"),
    F("Incapacity - type", "Incapacidad - Tipo", "Devengados / Incapacidad", "NIE126", "Y", "",
      "/NominaIndividual/Devengados/Incapacidades/Incapacidad/@Tipo", "1", "N (code)", "-",
      "Payroll.Incapacity_Type_Code",
      "Annex table 5.5.6: 1 Comun (general illness, funded by the EPS after the employer's first two "
      "days), 2 Profesional, 3 Laboral (both funded by the ARL from day one). The code determines "
      "who bears the cost, so it must be set from the medical certificate, not defaulted.",
      "Y", "-> Sheet 6: Tipo de Incapacidad (table 5.5.6)", R_NONE, "N", "Code", "Per record", "", RA, "payroll"),
    F("Incapacity - amount", "Incapacidad - Pago", "Devengados / Incapacidad", "NIE127", "Y", "",
      "/NominaIndividual/Devengados/Incapacidades/Incapacidad/@Pago", "Var", "N (decimal 2)", "-",
      "Payroll.Incapacity_Pay",
      "Amount paid to the employee for the incapacity. Colombian employers universally ADVANCE the "
      "benefit and recover it from the EPS or ARL, so this line is paid to the employee but "
      "receivable from the institution - see the inbound EPS/ARL determination in the Report Matrix. "
      "CO-GAP-03 / CO-GAP-04: the employer's first-two-days rate (Mercans default 66.67%) and the "
      "one-minimum-wage floor are configurable and require the client's election.",
      "Y", "-", R_XML, "N", "Amount", "Per record",
      "CO-GAP-03 / CO-GAP-04: confirm the client's election on the first-two-days rate and on the "
      "minimum-wage floor for incapacity payments.", RA, "payroll"),
    F("Maternity / paternity leave - start date", "LicenciaMP - FechaInicio",
      "Devengados / LicenciaMP", "NIE128", "C",
      "Optional (0-1); pairs with 'Maternity / paternity leave - end date' (NIE129).",
      "/NominaIndividual/Devengados/Licencias/LicenciaMP/@FechaInicio", "10", "AAAA-MM-DD", "-",
      "Payroll.Maternity_Leave_Start",
      "First day of maternity or paternity leave. Funded by the EPS, advanced by the employer.",
      "Y", "-", R_NONE, "N", "Date", "Per record", "", RA, "payroll"),
    F("Maternity / paternity leave - end date", "LicenciaMP - FechaFin",
      "Devengados / LicenciaMP", "NIE129", "C",
      "Pairs with 'Maternity / paternity leave - start date' (NIE128).",
      "/NominaIndividual/Devengados/Licencias/LicenciaMP/@FechaFin", "10", "AAAA-MM-DD", "-",
      "Payroll.Maternity_Leave_End",
      "Last day of the leave.", "Y", "-", R_NONE, "N", "Date", "Per record", "", RA, "payroll"),
    F("Maternity / paternity leave - days", "LicenciaMP - Cantidad",
      "Devengados / LicenciaMP", "NIE130", "Y", "",
      "/NominaIndividual/Devengados/Licencias/LicenciaMP/@Cantidad", "Var", "N (integer days)", "-",
      "Payroll.Maternity_Leave_Days",
      "Days of leave in the period. Must reconcile to the PILA LMA change-event flag and its dates.",
      "Y", "-", R_NONE, "N", "Count", "Per record", "", RA, "payroll"),
    F("Maternity / paternity leave - amount", "LicenciaMP - Pago",
      "Devengados / LicenciaMP", "NIE131", "Y", "",
      "/NominaIndividual/Devengados/Licencias/LicenciaMP/@Pago", "Var", "N (decimal 2)", "-",
      "Payroll.Maternity_Leave_Pay",
      "Amount paid. Advanced by the employer and recovered from the EPS.",
      "Y", "-", R_XML, "N", "Amount", "Per record", "", RA, "payroll"),
    F("Paid leave - start date", "LicenciaR - FechaInicio", "Devengados / LicenciaR", "NIE132", "C",
      "Optional (0-1); pairs with 'Paid leave - end date' (NIE133).",
      "/NominaIndividual/Devengados/Licencias/LicenciaR/@FechaInicio", "10", "AAAA-MM-DD", "-",
      "Payroll.Paid_Leave_Start",
      "First day of remunerated leave other than maternity or paternity (bereavement, marriage, "
      "voting, trade-union leave).",
      "Y", "-", R_NONE, "N", "Date", "Per record", "", RA, "payroll"),
    F("Paid leave - end date", "LicenciaR - FechaFin", "Devengados / LicenciaR", "NIE133", "C",
      "Pairs with 'Paid leave - start date' (NIE132).",
      "/NominaIndividual/Devengados/Licencias/LicenciaR/@FechaFin", "10", "AAAA-MM-DD", "-",
      "Payroll.Paid_Leave_End", "Last day of the remunerated leave.",
      "Y", "-", R_NONE, "N", "Date", "Per record", "", RA, "payroll"),
    F("Paid leave - days", "LicenciaR - Cantidad", "Devengados / LicenciaR", "NIE134", "Y", "",
      "/NominaIndividual/Devengados/Licencias/LicenciaR/@Cantidad", "Var", "N (integer days)", "-",
      "Payroll.Paid_Leave_Days", "Days of remunerated leave. Maps to the PILA VAC-LR flag with value L.",
      "Y", "-", R_NONE, "N", "Count", "Per record", "", RA, "payroll"),
    F("Paid leave - amount", "LicenciaR - Pago", "Devengados / LicenciaR", "NIE135", "Y", "",
      "/NominaIndividual/Devengados/Licencias/LicenciaR/@Pago", "Var", "N (decimal 2)", "-",
      "Payroll.Paid_Leave_Pay",
      "Money value of the remunerated leave. Fully in the contribution base and the withholding base.",
      "Y", "-", R_XML, "N", "Amount", "Per record", "", RA, "payroll"),
    F("Unpaid leave - start date", "LicenciaNR - FechaInicio",
      "Devengados / LicenciaNR", "NIE136", "C",
      "Optional (0-1); pairs with 'Unpaid leave - end date' (NIE137).",
      "/NominaIndividual/Devengados/Licencias/LicenciaNR/@FechaInicio", "10", "AAAA-MM-DD", "-",
      "Payroll.Unpaid_Leave_Start",
      "First day of unpaid leave or suspension. Maps to the PILA SLN change-event flag.",
      "Y", "-", R_NONE, "N", "Date", "Per record", "", RA, "payroll"),
    F("Unpaid leave - end date", "LicenciaNR - FechaFin", "Devengados / LicenciaNR", "NIE137", "C",
      "Pairs with 'Unpaid leave - start date' (NIE136).",
      "/NominaIndividual/Devengados/Licencias/LicenciaNR/@FechaFin", "10", "AAAA-MM-DD", "-",
      "Payroll.Unpaid_Leave_End", "Last day of the unpaid leave.",
      "Y", "-", R_NONE, "N", "Date", "Per record", "", RA, "payroll"),
    F("Unpaid leave - days", "LicenciaNR - Cantidad", "Devengados / LicenciaNR", "NIE138", "Y", "",
      "/NominaIndividual/Devengados/Licencias/LicenciaNR/@Cantidad", "Var", "N (integer days)", "-",
      "Payroll.Unpaid_Leave_Days",
      "Days of unpaid leave. NOTE: this block carries NO amount element - unpaid leave has no money "
      "value by definition. It still reduces DiasTrabajados (NIE069) and the contribution days.",
      "Y", "-", R_NONE, "N", "Count", "Per record", "", RA, "payroll"),
    F("Legal strike - start date", "HuelgaLegal - FechaInicio",
      "Devengados / HuelgaLegal", "NIE143", "C",
      "Optional (0-1); pairs with 'Legal strike - end date' (NIE144).",
      "/NominaIndividual/Devengados/HuelgasLegales/HuelgaLegal/@FechaInicio", "10",
      "AAAA-MM-DD", "-", "Payroll.Strike_Start",
      "First day of a lawful strike. Suspends the contract without terminating it.",
      "Y", "-", R_NONE, "N", "Date", "Per record", "", RA, "payroll"),
    F("Legal strike - end date", "HuelgaLegal - FechaFIn", "Devengados / HuelgaLegal", "NIE144", "C",
      "Pairs with 'Legal strike - start date' (NIE143). NOTE the annex spells this attribute "
      "'FechaFIn' with a capital I - reproduce it exactly or the document will not validate.",
      "/NominaIndividual/Devengados/HuelgasLegales/HuelgaLegal/@FechaFIn", "10", "AAAA-MM-DD", "-",
      "Payroll.Strike_End",
      "Last day of the strike. The attribute name is mis-cased in the official annex (FechaFIn); it "
      "must be emitted exactly as published.",
      "Y", "-", R_NONE, "N", "Date", "Per record",
      "Confirm with the RA that XSD v1.0.6 still carries the mis-cased attribute name 'FechaFIn'.",
      RA, "payroll"),
    F("Legal strike - days", "HuelgaLegal - Cantidad", "Devengados / HuelgaLegal", "NIE145", "Y", "",
      "/NominaIndividual/Devengados/HuelgasLegales/HuelgaLegal/@Cantidad", "Var",
      "N (integer days)", "-", "Payroll.Strike_Days",
      "Days of lawful strike. Like unpaid leave, this block carries no amount element.",
      "Y", "-", R_NONE, "N", "Count", "Per record", "", RA, "payroll"),

    "ACCRUED - BONUSES, ALLOWANCES AND OTHER CONCEPTS (paired S / NS)",
    F("Bonus - salary", "BonificacionS", "Devengados / Bonificacion", "NIE139", "C",
      "Paired salary / non-salary element. Populate S where the bonus is salary under CST art. 127; "
      "populate 'Bonus - non-salary' (NIE140) where the parties have agreed it is not salary under "
      "CST art. 128. Bidirectional pair: the S/NS split is a hard flag on the wage type set at "
      "configuration and must never be derived at reporting time.",
      "/NominaIndividual/Devengados/Bonificaciones/Bonificacion/@BonificacionS", "Var",
      "N (decimal 2)", "-", "Payroll.Bonus_Salary",
      "Discretionary or contractual bonus that constitutes salary. Fully in the contribution base and "
      "in the withholding base.",
      "Y", "-", R_XML, "N", "Amount", "Per record", "", RA, "payroll"),
    F("Bonus - non-salary", "BonificacionNS", "Devengados / Bonificacion", "NIE140", "C",
      "Paired with 'Bonus - salary' (NIE139). Populate NS only where an express non-salary agreement "
      "exists under CST art. 128.",
      "/NominaIndividual/Devengados/Bonificaciones/Bonificacion/@BonificacionNS", "Var",
      "N (decimal 2)", "-", "Payroll.Bonus_NonSalary",
      "Non-salary bonus. Excluded from the contribution base, but counts toward the 40% non-salary "
      "clamp of Ley 1393 de 2010 art. 30 - the excess over 40% of total remuneration is added back "
      "into the contribution base.",
      "Y", "-", R_XML, "N", "Amount", "Per record", "", RA, "payroll"),
    F("Allowance - salary", "AuxilioS", "Devengados / Auxilio", "NIE141", "C",
      "Paired salary / non-salary element; pairs with 'Allowance - non-salary' (NIE142). The split "
      "is a configuration flag on the wage type.",
      "/NominaIndividual/Devengados/Auxilios/Auxilio/@AuxilioS", "Var", "N (decimal 2)", "-",
      "Payroll.Allowance_Salary",
      "Employer allowance that constitutes salary (for example a fixed, habitual connectivity or "
      "housing allowance not agreed as non-salary).",
      "Y", "-", R_XML, "N", "Amount", "Per record", "", RA, "payroll"),
    F("Allowance - non-salary", "AuxilioNS", "Devengados / Auxilio", "NIE142", "C",
      "Paired with 'Allowance - salary' (NIE141).",
      "/NominaIndividual/Devengados/Auxilios/Auxilio/@AuxilioNS", "Var", "N (decimal 2)", "-",
      "Payroll.Allowance_NonSalary",
      "Employer allowance expressly agreed as non-salary. Counts toward the 40% clamp.",
      "Y", "-", R_XML, "N", "Amount", "Per record", "", RA, "payroll"),
    F("Other concept - description", "OtroConcepto - DescripcionConcepto",
      "Devengados / OtroConcepto", "NIE146", "Y", "",
      "/NominaIndividual/Devengados/OtrosConceptos/OtroConcepto/@DescripcionConcepto", "Var",
      "A", "-", "Payroll.Other_Concept_Description",
      "Free-text label of a concept that has no dedicated element. Mandatory (1-1) inside the block: "
      "an amount without a description is not admissible.",
      "Y", "-", R_NONE, "N", "Text", "Per record", "", RA, "payroll"),
    F("Other concept - salary", "OtroConcepto - ConceptoS",
      "Devengados / OtroConcepto", "NIE147", "C",
      "Paired salary / non-salary element; pairs with 'Other concept - non-salary' (NIE148). At least "
      "one of the two must be present where 'Other concept - description' (NIE146) is populated.",
      "/NominaIndividual/Devengados/OtrosConceptos/OtroConcepto/@ConceptoS", "Var",
      "N (decimal 2)", "-", "Payroll.Other_Concept_Salary",
      "Salary-constituting amount of the described concept.",
      "Y", "-", R_XML, "N", "Amount", "Per record", "", RA, "payroll"),
    F("Other concept - non-salary", "OtroConcepto - ConceptoNS",
      "Devengados / OtroConcepto", "NIE148", "C",
      "Paired with 'Other concept - salary' (NIE147) and conditioned on 'Other concept - "
      "description' (NIE146).",
      "/NominaIndividual/Devengados/OtrosConceptos/OtroConcepto/@ConceptoNS", "Var",
      "N (decimal 2)", "-", "Payroll.Other_Concept_NonSalary",
      "Non-salary amount of the described concept.",
      "Y", "-", R_XML, "N", "Amount", "Per record", "", RA, "payroll"),
    F("Ordinary cooperative compensation", "Compensacion - CompensacionO",
      "Devengados / Compensacion", "NIE149", "C",
      "Applies only to worker type 31 (cooperados o precooperativas de trabajo asociado). Pairs with "
      "'Extraordinary cooperative compensation' (NIE150).",
      "/NominaIndividual/Devengados/Compensaciones/Compensacion/@CompensacionO", "Var",
      "N (decimal 2)", "-", "Payroll.Coop_Compensation_Ordinary",
      "Ordinary compensation for associated cooperative work. Not an employment salary; reported here "
      "because worker type 31 is within the annex's TipoTrabajador list.",
      "Y", "-", R_XML, "N", "Amount", "Per record", "", RA, "payroll"),
    F("Extraordinary cooperative compensation", "Compensacion - CompensacionE",
      "Devengados / Compensacion", "NIE150", "C",
      "Applies only to worker type 31; pairs with 'Ordinary cooperative compensation' (NIE149).",
      "/NominaIndividual/Devengados/Compensaciones/Compensacion/@CompensacionE", "Var",
      "N (decimal 2)", "-", "Payroll.Coop_Compensation_Extraordinary",
      "Extraordinary compensation for associated cooperative work.",
      "Y", "-", R_XML, "N", "Amount", "Per record", "", RA, "payroll"),
    F("Voucher / card payment - salary", "BonoEPCTV - PagoS", "Devengados / BonoEPCTV", "NIE151", "C",
      "Paired salary / non-salary element for payments made in electronic or paper service vouchers, "
      "cheques, cards or vales. Pairs with 'Voucher / card payment - non-salary' (NIE152).",
      "/NominaIndividual/Devengados/BonoEPCTVs/BonoEPCTV/@PagoS", "Var", "N (decimal 2)", "-",
      "Payroll.Voucher_Salary",
      "Salary-constituting portion of voucher, cheque, card or vale payments. Cross-report: this is "
      "the concept reported at Formulario 220 casilla 37 and Formato 2276 numeral 7.",
      "Y", "-", R_XML, "N", "Amount", "Per record", "", RA, "payroll"),
    F("Voucher / card payment - non-salary", "BonoEPCTV - PagoNS",
      "Devengados / BonoEPCTV", "NIE152", "C",
      "Pairs with 'Voucher / card payment - salary' (NIE151).",
      "/NominaIndividual/Devengados/BonoEPCTVs/BonoEPCTV/@PagoNS", "Var", "N (decimal 2)", "-",
      "Payroll.Voucher_NonSalary",
      "Non-salary portion of voucher or card payments.",
      "Y", "-", R_XML, "N", "Amount", "Per record", "", RA, "payroll"),
    F("Meal payment - salary", "BonoEPCTV - PagoAlimentacionS",
      "Devengados / BonoEPCTV", "NIE153", "C",
      "Paired salary / non-salary element for third-party meal payments. Pairs with 'Meal payment - "
      "non-salary' (NIE154). The engine must ALSO maintain the ET art. 387-1 split at 41 UVT "
      "(COP 2,147,334 per month in 2026), because Formato 2276 reports the amount up to 41 UVT at "
      "numeral 32 and the EXCESS at numeral 8, in two different fields.",
      "/NominaIndividual/Devengados/BonoEPCTVs/BonoEPCTV/@PagoAlimentacionS", "Var",
      "N (decimal 2)", "-", "Payroll.Meal_Payment_Salary",
      "Salary-constituting meal payments made through a third party.",
      "Y", "-", R_XML, "N", "Amount", "Per record", "", RA, "payroll"),
    F("Meal payment - non-salary", "BonoEPCTV - PagoAlimentacionNS",
      "Devengados / BonoEPCTV", "NIE154", "C",
      "Pairs with 'Meal payment - salary' (NIE153). Under ET art. 387-1 the payment is NOT income to "
      "the worker up to 41 UVT per month where salary does not exceed 310 UVT (COP 16,235,940 in "
      "2026); above either limit the excess is taxable.",
      "/NominaIndividual/Devengados/BonoEPCTVs/BonoEPCTV/@PagoAlimentacionNS", "Var",
      "N (decimal 2)", "-", "Payroll.Meal_Payment_NonSalary",
      "Non-salary meal payments through a third party.",
      "Y", "-", R_XML, "N", "Amount", "Per record", "", RA, "payroll"),
    F("Commission", "Comision", "Devengados / Comisiones", "NIE155", "C",
      "Populated where commission was paid in the period. Repeating (0-N).",
      "/NominaIndividual/Devengados/Comisiones/Comision", "Var", "N (decimal 2)", "-",
      "Payroll.Commission",
      "Sales or performance commission. ALWAYS salary in Colombia (CST art. 127) - it is not a "
      "paired S/NS element, which is the deliberate signal that it cannot be agreed as non-salary.",
      "Y", "-", R_XML, "N", "Amount", "Per record", "", RA, "payroll"),
    F("Third-party payment (accrued)", "PagoTercero", "Devengados / PagosTerceros", "NIE193", "C",
      "Populated where the employer paid a third party on the employee's behalf and it constitutes "
      "employee income. Distinct from NIE195, which is the DEDUCTION-side third-party element; do "
      "not confuse the two - they carry different NIE codes in different parents.",
      "/NominaIndividual/Devengados/PagosTerceros/PagoTercero", "Var", "N (decimal 2)", "-",
      "Payroll.Third_Party_Payment_Accrued",
      "Payments made to third parties that are income of the employee. Repeating (0-N).",
      "Y", "-", R_XML, "N", "Amount", "Per record", "", RA, "payroll"),
    F("Advance (accrued)", "Anticipo", "Devengados / Anticipos", "NIE194", "C",
      "Populated where an advance was paid in the period. Its recovery appears on the DEDUCTIONS side "
      "as NIE196 - the two are a bidirectional pair across the accrued and deducted blocks.",
      "/NominaIndividual/Devengados/Anticipos/Anticipo", "Var", "N (decimal 2)", "-",
      "Payroll.Advance_Paid",
      "Salary advance paid to the employee. Repeating (0-N).",
      "Y", "-", R_XML, "N", "Amount", "Per record", "", RA, "payroll"),
    F("Work clothing", "Dotacion", "Devengados", "NIE156", "C",
      "Populated where work clothing was delivered in the period. Colombia mandates three annual "
      "deliveries - by 30 April, 31 August and 20 December (CST art. 232) - for employees earning up "
      "to 2 SMMLV.",
      "/NominaIndividual/Devengados/Dotacion", "Var", "N (decimal 2)", "-",
      "Payroll.Work_Clothing",
      "Value of work clothing and footwear delivered. Never salary (CST art. 128) and never "
      "convertible into cash.",
      "Y", "-", R_XML, "N", "Amount", "Monthly", "", RA, "payroll"),
    F("Apprentice maintenance support", "ApoyoSost", "Devengados", "NIE157", "C",
      "Populated only for apprentices - contract type 4 (NIE061) and worker type 12 or 19 (NIE041). "
      "Bidirectional: where NIE157 is present, NIE061 must be 4 and NIE041 must be 12 or 19.",
      "/NominaIndividual/Devengados/ApoyoSost", "Var", "N (decimal 2)", "-",
      "Payroll.Apprentice_Support",
      "Apoyo de sostenimiento paid to an apprentice. Ley 2466 de 2025 art. 21 recast the "
      "apprenticeship as a labour contract, so from 2026 the support is remuneration of an employee, "
      "not a training stipend, and is regulated by Decreto 0223 of 5 March 2026.",
      "Y", "-", R_XML, "N", "Amount", "Monthly", "", RA, "payroll"),
    F("Telework allowance", "Teletrabajo", "Devengados", "NIE158", "C",
      "Populated for teleworkers and remote workers whose employer contributes to connectivity and "
      "energy costs under Ley 1221 de 2008 as amended by Ley 2466 de 2025 arts. 52-54.",
      "/NominaIndividual/Devengados/Teletrabajo", "Var", "N (decimal 2)", "-",
      "Payroll.Telework_Allowance",
      "Employer contribution toward the teleworker's connectivity and energy costs.",
      "Y", "-", R_XML, "N", "Amount", "Monthly", "", RA, "payroll"),
    F("Retirement bonus", "BonifRetiro", "Devengados", "NIE159", "C",
      "Populated on a termination document only. Typically co-occurs with 'Termination date' "
      "(NIE003) and with 'Indemnity' (NIE160).",
      "/NominaIndividual/Devengados/BonifRetiro", "Var", "N (decimal 2)", "-",
      "Payroll.Retirement_Bonus",
      "Ex gratia or negotiated bonus paid on departure. Fully taxable employment income; it enters "
      "the ordinary monthly withholding base.",
      "Y", "-", R_XML, "N", "Amount", "Per event", "", RA, "payroll"),
    F("Dismissal indemnity", "Indemnizacion", "Devengados", "NIE160", "C",
      "Populated on a termination document only; co-occurs with 'Termination date' (NIE003).",
      "/NominaIndividual/Devengados/Indemnizacion", "Var", "N (decimal 2)", "-",
      "Payroll.Termination_Indemnity",
      "Indemnity for dismissal without just cause (CST art. 64). Fully taxable and enters the "
      "ordinary monthly base; only the statutory-minimum indemnities of ET art. 206 nums. 1-3 are "
      "exempt, and then only up to the legal minimum (art. 206 par. 1).",
      "Y", "-", R_XML, "N", "Amount", "Per event", "", RA, "payroll"),
    F("Reimbursement (accrued)", "Reintegro", "Devengados", "NIE201", "C",
      "Populated where an amount previously deducted is being returned to the employee. Distinct "
      "from the deduction-side Reintegro (NIE184); the two carry different codes and opposite signs.",
      "/NominaIndividual/Devengados/Reintegro", "Var", "N (decimal 2)", "-",
      "Payroll.Reimbursement_Accrued",
      "Reimbursement returned to the employee - for example an over-deduction corrected in a later "
      "month.",
      "Y", "-", R_XML, "N", "Amount", "Monthly", "", RA, "payroll"),

    "DEDUCTIONS - MANDATORY SOCIAL SECURITY AND TAX",
    F("Health contribution - rate", "Salud - Porcentaje", "Deducciones / Salud", "NIE161", "Y", "",
      "/NominaIndividual/Deducciones/Salud/@Porcentaje", "Var", "N (decimal)", "4.00",
      "Mercans.Health_Employee_Rate",
      "Employee health contribution rate: 4.00% of the contribution base (Ley 100 de 1993 art. 204 as "
      "amended). The employer's 8.5% is NOT an employee deduction and must never appear here.",
      "Y", "-> Sheet 6: Contribution rates 2026", "Rate to 2 decimals.", "N", "Rate", "Monthly", "", RA, "system"),
    F("Health contribution - amount", "Salud - Deduccion", "Deducciones / Salud", "NIE163", "Y", "",
      "/NominaIndividual/Deducciones/Salud/@Deduccion", "Var", "N (decimal 2)", "480000.00",
      "Payroll.Health_Employee_Contribution",
      "Employee health deduction. FORMATTING TRAP: this is the XML figure at 2 decimals, "
      "round-half-to-even. The PILA figure for the same contribution is rounded UP to the next "
      "multiple of 100 and will legitimately differ by up to 99 pesos - the two must never be "
      "interchanged, and the payslip must show the XML figure.",
      "Y", "-", R_XML, "N", "Amount", "Monthly", "", RA, "payroll"),
    F("Pension contribution - rate", "FondoPension - Porcentaje",
      "Deducciones / FondoPension", "NIE164", "Y", "",
      "/NominaIndividual/Deducciones/FondoPension/@Porcentaje", "4-6", "N (decimal)", "4.00",
      "Mercans.Pension_Employee_Rate",
      "Employee pension contribution rate: 4.00% of the contribution base, against the employer's "
      "12.00%, for a total of 16% (Ley 100 de 1993 art. 20 as substituted by Ley 797 de 2003 art. 7). "
      "Set to 0.00 for an employed old-age pensioner (worker sub-type 01).",
      "Y", "-> Sheet 6: Contribution rates 2026", "Rate to 2 decimals.", "N", "Rate", "Monthly", "", RA, "system"),
    F("Pension contribution - amount", "FondoPension - Deduccion",
      "Deducciones / FondoPension", "NIE166", "Y", "",
      "/NominaIndividual/Deducciones/FondoPension/@Deduccion", "Var", "N (decimal 2)", "480000.00",
      "Payroll.Pension_Employee_Contribution",
      "Employee pension deduction. Must NOT include the solidarity-fund surcharge, which has its own "
      "element (FondoSP, NIE167-NIE170) with four separate attributes.",
      "Y", "-", R_XML, "N", "Amount", "Monthly", "", RA, "payroll"),
    F("Solidarity fund - solidarity rate", "FondoSP - Porcentaje",
      "Deducciones / FondoSP", "NIE167", "C",
      "Payable ONLY where the contribution base is at least 4 SMMLV (COP 7,003,620 in 2026). "
      "Bidirectional set of four: NIE167 pairs with 'Solidarity fund - solidarity amount' (NIE168), "
      "and the subsistence pair NIE169 / NIE170 has its own higher 16-SMMLV trigger.",
      "/NominaIndividual/Deducciones/FondoSP/@Porcentaje", "4-6", "N (decimal)", "1.00",
      "Mercans.FSP_Solidarity_Rate",
      "Rate of the solidarity sub-account surcharge: 1.00% of the contribution base once the base "
      "reaches 4 SMMLV (Ley 100 art. 20 as substituted by Ley 797 de 2003 art. 7). Employee-only, "
      "and ADDITIONAL to the 4% pension.",
      "Y", "-> Sheet 6: Solidarity pension fund bands", "Rate to 2 decimals.", "N", "Rate",
      "Monthly", "", RA, "system"),
    F("Solidarity fund - solidarity amount", "FondoSP - DeduccionSP",
      "Deducciones / FondoSP", "NIE168", "C",
      "Pairs with 'Solidarity fund - solidarity rate' (NIE167); present whenever the base is at least "
      "4 SMMLV.",
      "/NominaIndividual/Deducciones/FondoSP/@DeduccionSP", "Var", "N (decimal 2)", "120000.00",
      "Payroll.FSP_Solidarity_Amount",
      "Money value of the solidarity sub-account surcharge. THE SINGLE MOST COMMON COLOMBIAN MAPPING "
      "ERROR is merging this into the pension line: the XML models the solidarity fund as FOUR "
      "distinct attributes and DIAN validates them separately.",
      "Y", "-", R_XML, "N", "Amount", "Monthly", "", RA, "payroll"),
    F("Solidarity fund - subsistence rate", "FondoSP - PorcentajeSub",
      "Deducciones / FondoSP", "NIE169", "C",
      "Payable ONLY where the contribution base is at least 16 SMMLV (COP 28,014,480 in 2026) - a "
      "HIGHER trigger than the solidarity sub-account. Pairs with 'Solidarity fund - subsistence "
      "amount' (NIE170), and cannot be present unless NIE167 / NIE168 are also present.",
      "/NominaIndividual/Deducciones/FondoSP/@PorcentajeSub", "4-6", "N (decimal)", "-",
      "Mercans.FSP_Subsistence_Rate",
      "Banded subsistence surcharge, 0.2% to 1.0%, rising by band from 16 SMMLV to above 20 SMMLV "
      "(Ley 797 de 2003 art. 7).",
      "Y", "-> Sheet 6: Solidarity pension fund bands", "Rate to 2 decimals.", "N", "Rate",
      "Monthly", "", RA, "system"),
    F("Solidarity fund - subsistence amount", "FondoSP - DeduccionSub",
      "Deducciones / FondoSP", "NIE170", "C",
      "Pairs with 'Solidarity fund - subsistence rate' (NIE169); present only from 16 SMMLV.",
      "/NominaIndividual/Deducciones/FondoSP/@DeduccionSub", "Var", "N (decimal 2)", "-",
      "Payroll.FSP_Subsistence_Amount",
      "Money value of the subsistence sub-account surcharge. Reported separately from the solidarity "
      "amount; the two are never summed in the XML.",
      "Y", "-", R_XML, "N", "Amount", "Monthly", "", RA, "payroll"),
    F("Income tax withheld", "RetencionFuente", "Deducciones", "NIE177", "C",
      "Present where withholding was applied. A depurated base in the 0% band of the ET art. 383 "
      "table produces no element rather than a zero. For a NON-RESIDENT this carries the flat 20% of "
      "ET art. 408 on the GROSS, with no depuration.",
      "/NominaIndividual/Deducciones/RetencionFuente", "Var", "N (decimal 2)", "617000.00",
      "Payroll.Income_Tax_Withheld",
      "Retencion en la fuente sobre rentas de trabajo. RESIDENT: the ET art. 383 progressive table "
      "(0 / 19 / 28 / 33 / 35 / 37 / 39%) applied to the art. 388 depurated monthly base, under "
      "Procedure 1 or Procedure 2. NON-RESIDENT: the flat 20% of ET art. 408 on the gross payment, "
      "with no art. 388 depuration, no 25% exempt income, no art. 387 deductions and no tax-free "
      "band (DIAN Concepto 011108 of 29 June 2026). Cross-report: the sum of this element across all "
      "employees for the month must reconcile to Formulario 350 casilla 93.",
      "Y", "-", "Whole pesos, approximated to the nearest 1,000 per ET art. 868 par., then expressed "
      "with 2 decimals in the XML.", "N", "Amount", "Monthly", "", RA, "payroll"),

    "DEDUCTIONS - VOLUNTARY, JUDICIAL AND THIRD-PARTY",
    F("Voluntary pension contribution", "PensionVoluntaria", "Deducciones", "NIE198", "C",
      "Present where the employee has authorised a voluntary pension contribution in writing.",
      "/NominaIndividual/Deducciones/PensionVoluntaria", "Var", "N (decimal 2)", "-",
      "Payroll.Voluntary_Pension",
      "Voluntary contribution to a pension fund. Reduces the withholding base within the ET art. 336 "
      "40% / 1,340 UVT annual limit. Cross-report: Formulario 220 casillas 55-56 and Formato 2276 "
      "numerals 25-26 split RAIS voluntary contributions from voluntary pension-fund contributions, "
      "so the engine must carry the two separately even though the XML has one element.",
      "Y", "-", R_XML, "N", "Amount", "Monthly",
      "Confirm how the client wants RAIS voluntary contributions (2276 numeral 25) distinguished from "
      "voluntary pension-fund contributions (numeral 26) when both map to NIE198.", RA, "payroll"),
    F("AFC savings account contribution", "AFC", "Deducciones", "NIE179", "C",
      "Present where the employee has authorised a contribution to an AFC (Ahorro para el Fomento de "
      "la Construccion) account.",
      "/NominaIndividual/Deducciones/AFC", "Var", "N (decimal 2)", "-",
      "Payroll.AFC_Contribution",
      "Long-term construction-savings contribution. Shares the ET art. 336 40% / 1,340 UVT cap with "
      "voluntary pension contributions. Cross-report: Formulario 220 casilla 57, Formato 2276 "
      "numeral 27.",
      "Y", "-", R_XML, "N", "Amount", "Monthly", "", RA, "payroll"),
    F("Union dues", "Sindicato - Porcentaje", "Deducciones / Sindicato", "NIE171", "C",
      "Present only for a unionised employee. Pairs with 'Union dues - amount' (NIE172): both "
      "attributes are 1-1 inside the element, so where the element exists both must be populated.",
      "/NominaIndividual/Deducciones/Sindicato/@Porcentaje", "Var", "N (decimal)", "-",
      "Mercans.Union_Dues_Rate",
      "Percentage rate of the union subscription, set by the union's statutes.",
      "Y", "-", "Rate to 2 decimals.", "N", "Rate", "Monthly", "", RA, "system"),
    F("Union dues - amount", "Sindicato - Deduccion", "Deducciones / Sindicato", "NIE172", "C",
      "Pairs with 'Union dues' rate (NIE171); both are required where the Sindicato element is present.",
      "/NominaIndividual/Deducciones/Sindicato/@Deduccion", "Var", "N (decimal 2)", "-",
      "Payroll.Union_Dues",
      "Money value of the union subscription withheld. Requires the employee's written authorisation "
      "(CST art. 400).",
      "Y", "-", R_XML, "N", "Amount", "Monthly", "", RA, "payroll"),
    F("Public sanction", "Sancion - SancionPublic", "Deducciones / Sancion", "NIE173", "C",
      "Present where a disciplinary sanction with a public destination is being withheld. Pairs with "
      "'Private sanction' (NIE174) - both attributes are 1-1 inside the Sancion element.",
      "/NominaIndividual/Deducciones/Sanciones/Sancion/@SancionPublic", "Var",
      "N (decimal 2)", "-", "Payroll.Sanction_Public",
      "Disciplinary fine whose proceeds go to a public destination. Colombian fines are capped by "
      "CST art. 113 and must be provided for in the internal work rules.",
      "Y", "-", R_XML, "N", "Amount", "Monthly", "", RA, "payroll"),
    F("Private sanction", "Sancion - SancionPriv", "Deducciones / Sancion", "NIE174", "C",
      "Pairs with 'Public sanction' (NIE173) inside the Sancion element.",
      "/NominaIndividual/Deducciones/Sanciones/Sancion/@SancionPriv", "Var",
      "N (decimal 2)", "-", "Payroll.Sanction_Private",
      "Disciplinary fine retained by the employer's welfare fund.",
      "Y", "-", R_XML, "N", "Amount", "Monthly", "", RA, "payroll"),
    F("Payroll loan - description", "Libranza - Descripcion", "Deducciones / Libranza", "NIE175", "C",
      "Present where a libranza deduction is being made. Pairs with 'Payroll loan - amount' (NIE176): "
      "both attributes are 1-1 inside the element.",
      "/NominaIndividual/Deducciones/Libranzas/Libranza/@Descripcion", "Var", "A", "-",
      "Payroll.Libranza_Description",
      "Description identifying the lender and the loan. Repeating (0-N) - an employee may carry "
      "several libranzas.",
      "Y", "-", R_NONE, "N", "Text", "Per record", "", RA, "payroll"),
    F("Payroll loan - amount", "Libranza - Deduccion", "Deducciones / Libranza", "NIE176", "C",
      "Pairs with 'Payroll loan - description' (NIE175).",
      "/NominaIndividual/Deducciones/Libranzas/Libranza/@Deduccion", "Var", "N (decimal 2)", "-",
      "Payroll.Libranza_Deduction",
      "Instalment withheld under a libranza authorisation (Ley 1527 de 2012). ENGINE RULE: the "
      "aggregate of all libranza deductions must leave the employee at least 50% of net salary - a "
      "validation the XML does not perform.",
      "Y", "-", R_XML, "N", "Amount", "Per record", "", RA, "payroll"),
    F("Third-party payment (deduction)", "PagoTercero", "Deducciones / PagosTerceros", "NIE195", "C",
      "Present where an amount is withheld and remitted to a third party. Distinct from NIE193, the "
      "ACCRUED-side third-party element - same element name, different NIE code and different parent.",
      "/NominaIndividual/Deducciones/PagosTerceros/PagoTercero", "Var", "N (decimal 2)", "-",
      "Payroll.Third_Party_Deduction",
      "Amounts withheld for payment to third parties. Repeating (0-N).",
      "Y", "-", R_XML, "N", "Amount", "Per record", "", RA, "payroll"),
    F("Advance recovery (deduction)", "Anticipo", "Deducciones / Anticipos", "NIE196", "C",
      "Present where a previously paid advance is being recovered. Bidirectional pair with the "
      "accrued-side advance (NIE194) across the two blocks.",
      "/NominaIndividual/Deducciones/Anticipos/Anticipo", "Var", "N (decimal 2)", "-",
      "Payroll.Advance_Recovery",
      "Recovery of a salary advance. Repeating (0-N).",
      "Y", "-", R_XML, "N", "Amount", "Per record", "", RA, "payroll"),
    F("Other deduction", "OtraDeduccion", "Deducciones / OtrasDeducciones", "NIE197", "C",
      "Present where a deduction has no dedicated element. Repeating (0-N).",
      "/NominaIndividual/Deducciones/OtrasDeducciones/OtraDeduccion", "Var", "N (decimal 2)", "-",
      "Payroll.Other_Deduction",
      "Catch-all deduction element. Use sparingly: DIAN expects concepts that have a dedicated "
      "element to use that element.",
      "Y", "-", R_XML, "N", "Amount", "Per record", "", RA, "payroll"),
    F("Cooperative deduction", "Cooperativa", "Deducciones", "NIE180", "C",
      "Present where the employee has authorised a deduction for a cooperative.",
      "/NominaIndividual/Deducciones/Cooperativa", "Var", "N (decimal 2)", "-",
      "Payroll.Cooperative_Deduction",
      "Contribution or repayment withheld for an employee cooperative.",
      "Y", "-", R_XML, "N", "Amount", "Monthly", "", RA, "payroll"),
    F("Judicial or tax attachment", "EmbargoFiscal", "Deducciones", "NIE181", "C",
      "Present where a court or tax authority has ordered an attachment of salary.",
      "/NominaIndividual/Deducciones/EmbargoFiscal", "Var", "N (decimal 2)", "-",
      "Payroll.Attachment",
      "Attachment of salary. Colombian salary is unattachable up to the minimum wage, and only 20% of "
      "the excess is attachable, except for maintenance debts and cooperative debts (CST arts. "
      "154-156) - an engine rule, not an XML rule.",
      "Y", "-", R_XML, "N", "Amount", "Monthly", "", RA, "payroll"),
    F("Complementary health plan", "PlanComplementarios", "Deducciones", "NIE182", "C",
      "Present where the employee has authorised a deduction for a complementary or prepaid health "
      "plan.",
      "/NominaIndividual/Deducciones/PlanComplementarios", "Var", "N (decimal 2)", "-",
      "Payroll.Prepaid_Health",
      "Prepaid or complementary health-plan premium withheld. Deductible from the withholding base "
      "under ET art. 387 up to 16 UVT per month.",
      "Y", "-", R_XML, "N", "Amount", "Monthly", "", RA, "payroll"),
    F("Education deduction", "Educacion", "Deducciones", "NIE183", "C",
      "Present where an education-related amount is withheld.",
      "/NominaIndividual/Deducciones/Educacion", "Var", "N (decimal 2)", "-",
      "Payroll.Education_Deduction",
      "Education debt or contribution withheld from salary.",
      "Y", "-", R_XML, "N", "Amount", "Monthly", "", RA, "payroll"),
    F("Reimbursement (deduction)", "Reintegro", "Deducciones", "NIE184", "C",
      "Present where the employee is repaying an amount to the employer. Distinct from the accrued-"
      "side Reintegro (NIE201).",
      "/NominaIndividual/Deducciones/Reintegro", "Var", "N (decimal 2)", "-",
      "Payroll.Reimbursement_Deduction",
      "Repayment by the employee of an amount previously overpaid.",
      "Y", "-", R_XML, "N", "Amount", "Monthly", "", RA, "payroll"),
    F("Debt", "Deuda", "Deducciones", "NIE185", "C",
      "Present where a debt owed by the employee to the employer is being recovered.",
      "/NominaIndividual/Deducciones/Deuda", "Var", "N (decimal 2)", "-",
      "Payroll.Employee_Debt",
      "Recovery of an employee debt. Requires written authorisation (CST art. 149).",
      "Y", "-", R_XML, "N", "Amount", "Monthly", "", RA, "payroll"),

    "TOTALS AND ROUNDING",
    F("Rounding residual", "Redondeo", "NominaIndividual", "NIE186", "C",
      "Present ONLY where the round-half-to-even rounding of the individual concepts produces a "
      "difference between the calculated total and the sum of the parts. Bidirectional with the "
      "three totals NIE187 / NIE188 / NIE189: where Redondeo is present, ComprobanteTotal must "
      "already incorporate it.",
      "/NominaIndividual/Redondeo", "Var", "N (decimal 2)", "0.00", "System.Rounding_Residual",
      "The explicit residual carried so that the totals tie. Anexo Tecnico s.1.1.1 mandates "
      "round-half-to-even (NTC 3711 / JIS Z 8401) and allows a validation tolerance of +/- 2.00; any "
      "residual within that tolerance must be disclosed here rather than absorbed silently into a "
      "concept.",
      "N", "-", R_XML, "Y", "Amount", "Monthly", "", RA, "system"),
    F("Total accrued", "DevengadosTotal", "NominaIndividual", "NIE187", "Y", "",
      "/NominaIndividual/DevengadosTotal", "Var", "N (decimal 2)", "12000000.00",
      "SUM(all Devengados elements)",
      "Sum of every element in the Devengados block. Item 6 and item 8 of the art. 5 mandatory "
      "content. Input [4] to the CUNE, where it must be TRUNCATED to two decimals - truncated, not "
      "rounded, a distinction that catches many implementations.",
      "Y", "-", R_XML, "N", "Amount", "Monthly", "", RA, "payroll"),
    F("Total deducted", "DeduccionesTotal", "NominaIndividual", "NIE188", "Y", "",
      "/NominaIndividual/DeduccionesTotal", "Var", "N (decimal 2)", "1697000.00",
      "SUM(all Deducciones elements)",
      "Sum of every element in the Deducciones block. Item 7 of the art. 5 mandatory content. Input "
      "[5] to the CUNE, truncated to two decimals.",
      "Y", "-", R_XML, "N", "Amount", "Monthly", "", RA, "payroll"),
    F("Total payable", "ComprobanteTotal", "NominaIndividual", "NIE189", "Y", "",
      "/NominaIndividual/ComprobanteTotal", "Var", "N (decimal 2)", "10303000.00",
      "NIE187 - NIE188 (+/- NIE186)",
      "DevengadosTotal minus DeduccionesTotal, adjusted for the Redondeo residual. Item 8 of the "
      "art. 5 mandatory content. Input [6] to the CUNE, truncated to two decimals.",
      "Y", "-", R_XML, "N", "Amount", "Monthly", "", RA, "payroll"),

    "CONTRACTUAL CHANGE EVENT - Novedad",
    F("Contractual change flag", "Novedad", "NominaIndividual", "NIE199", "C",
      "Present (0-1) where the document reports a contractual change event. Bidirectional pair with "
      "'Referenced CUNE' (NIE204): where Novedad is present, CUNENov is mandatory (1-1) inside it.",
      "/NominaIndividual/Novedad", "Var", "Boolean (true / false)", "-", "Payroll.Novedad_Flag",
      "Set to the literal true or false. Signals that this document reports a change to a "
      "previously transmitted document's contractual data (Anexo Tecnico s.11).",
      "N", "-", R_NONE, "N", "Flag", "Per event", "", RA, "system"),
    F("Referenced CUNE", "CUNENov", "Novedad", "NIE204", "C",
      "Mandatory (1-1) whenever the 'Contractual change flag' (NIE199) element is present; must be "
      "absent otherwise. Bidirectional pair with NIE199.",
      "/NominaIndividual/Novedad/@CUNENov", "96", "A (SHA-384 hex)", "-",
      "System.Referenced_CUNE",
      "The CUNE of the document to which the contractual change relates. Establishes the cross-"
      "reference chain between documents for the same employment relationship.",
      "N", "-", R_NONE, "N", "Identifier", "Per event", "", RA, "system"),

    "ADJUSTMENT NOTE - NominaIndividualDeAjuste (C19 prefix NIAE)",
    F("Adjustment note type", "TipoNota", "NominaIndividualDeAjuste", "NIAE214", "Y", "",
      "/NominaIndividualDeAjuste/TipoNota", "1", "N (code)", "1", "Mercans.Adjustment_Type",
      "Annex table 5.5.8: 1 Reemplazar (replace, for arithmetic, accounting or content errors) and "
      "2 Eliminar (cancel a document transmitted in error). NOTE the annex's own caveat: code 2 only "
      "INVALIDATES the erroneous document - it does not by itself restore the position, so a "
      "corrected document must follow.",
      "N", "-> Sheet 6: Tipo de Nota de Ajuste (table 5.5.8)", R_NONE, "N", "Code", "Per event", "", RA, "system"),
    F("Adjustment note - replaced block", "Reemplazar", "NominaIndividualDeAjuste",
      "NIAE001-NIAE213", "C",
      "The Reemplazar block is present when 'Adjustment note type' (NIAE214) = 1, and absent when it "
      "= 2. Mutually exclusive with the Eliminar block. Bidirectional pair with NIAE214.",
      "/NominaIndividualDeAjuste/Reemplazar/...", "-", "Full document structure", "(group)",
      "(mirrors the whole NominaIndividual structure)",
      "Where the note replaces a document, the Reemplazar block repeats the ENTIRE NominaIndividual "
      "structure with corrected values, under NIAE-prefixed codes that mirror the NIE codes one for "
      "one (NIAE023 = Ambiente, NIAE044 = TipoDocumento, NIAE187 = DevengadosTotal, and so on). It "
      "carries its OWN CUNE, computed on the same eleven inputs from the Reemplazar block.",
      "Y", "-", R_XML, "N", "Code", "Per event", "", RA, "system"),
    F("Adjustment note - cancelled block", "Eliminar", "NominaIndividualDeAjuste",
      "NIAE236, NIAE237 et seq.", "C",
      "The Eliminar block is present when 'Adjustment note type' (NIAE214) = 2, and absent when it "
      "= 1. Mutually exclusive with the Reemplazar block.",
      "/NominaIndividualDeAjuste/Eliminar/...", "-", "Reduced document structure", "(group)",
      "(references the original document by its CUNE)",
      "Cancellation block. Its CUNE is computed with ValDev, ValDed and ValTol FORCED TO 0.00 and "
      "DocEmp forced to 0 (Anexo Tecnico s.8.1.1.4) - a deliberate divergence from the replace case "
      "that a naive shared CUNE routine will get wrong.",
      "Y", "-", R_XML, "N", "Code", "Per event", "", RA, "system"),

    "INBOUND - DIAN VALIDATION RESPONSE (integration CO-IN-NE-APPRESPONSE)",
    F("Validation response envelope", "SendNominaSyncResponse", "Inbound / SOAP", "INB-01", "Y", "",
      "/s:Envelope/s:Body/SendNominaSyncResponse", "-", "SOAP 1.2 response", "(envelope)",
      "System.NE_Response_Envelope",
      "Synchronous SOAP response returned in the same call as SendNominaSync. THIS IS A HARD INBOUND "
      "DEPENDENCY, not a receipt: a payroll cost is tax-deductible only where the supporting document "
      "has been validated, so the engine must parse and persist the outcome.",
      "N", "-", R_NONE, "N", "Code", "Per document", "", RA, "system"),
    F("Application response (base64)", "ApplicationResponse", "Inbound / SOAP", "INB-02", "Y", "",
      "/s:Envelope/s:Body/SendNominaSyncResponse/.../ApplicationResponse", "Var",
      "Base64-encoded UBL ApplicationResponse", "(base64)", "System.NE_ApplicationResponse",
      "The validation verdict, base64-encoded inside the SOAP response. Decode it, read the "
      "acceptance or rejection, and store the raw payload for audit - it is the employer's evidence "
      "that the document exists in DIAN's system.",
      "N", "-", R_NONE, "N", "Code", "Per document", "", RA, "system"),
    F("Validation status", "Estado de validacion", "Inbound / derived", "INB-03", "Y", "",
      "(decoded from INB-02)", "Var", "Code", "Aceptado", "Payroll.NE_Validation_Status",
      "Derived acceptance status. Store per document per employee per period. A rejection must "
      "trigger correction and re-transmission; an unvalidated document must block the tax deduction "
      "of the corresponding payroll cost in the client's ledger.",
      "N", "-> Sheet 6: Validation outcome", R_NONE, "N", "Code", "Per document", "", RA, "system"),
    F("Rejection rule codes", "Codigos de regla de rechazo", "Inbound / derived", "INB-04", "C",
      "Present only where 'Validation status' (INB-03) is a rejection. Bidirectional pair with "
      "INB-03: a rejection status without rule codes is an incomplete parse.",
      "(decoded from INB-02)", "Var", "Code list", "NIE022, 90", "Payroll.NE_Rejection_Codes",
      "The validation rules breached, from Anexo Tecnico s.6.1. The frequent ones are NIE022 (wrong "
      "Version literal), rule 90 (document number already used for that employee) and rule 92 "
      "(issuer not enabled). Persist them: they drive the correction path.",
      "N", "-", R_NONE, "N", "Code", "Per document", "", RA, "system"),
]


# ===========================================================================
#  CONFIG
# ===========================================================================
CFG = {
    "doc_id": "CO-DIAN-001",
    "filing_id": "CO-DIAN-NE-MONTHLY-001",
    "name_en": "Electronic Payroll Support Document",
    "name_es": "Documento Soporte de Pago de Nomina Electronica",
    "spec_sheet": "Nomina Electronica Spec",
    "authority_full": "Direccion de Impuestos y Aduanas Nacionales (DIAN)",
    "frequency": "Monthly - ONE document per employee per month, irrespective of the pay cycle "
                 "(Res. DIAN 000013 de 2021 art. 3)",
    "due_date": "Transmitted for validation within the FIRST TEN DAYS of the month following the "
                "payment or credit in account (Res. DIAN 000013 de 2021 art. 8). The deadline runs "
                "from the payment, not from the accrual.",
    "submission": "MACHINE-TO-MACHINE web service. SOAP 1.2, Document/Literal, operation "
                  "SendNominaSync, over TLS 1.2 with MUTUAL certificate authentication; WS-Security "
                  "1.0 with X.509 Certificate Token Profile 1.1. Portal: DIAN Sistema de Validacion "
                  "y Gestion de Documentos (catalogo-vpfe.dian.gov.co). Companion query operation "
                  "GetStatus.",
    "file_format": "XML (UBL 2.1 extension area for the signature; DIAN's own structure elsewhere), "
                   "base64 of a ZIP containing the XML, maximum 500 KB, UTF-8 only, XAdES-EPES "
                   "signature. XSD version 1.0.6; Anexo Tecnico version 1.0.",
    "legal_basis": "Resolucion DIAN 000013 de 11 de febrero de 2021, arts. 1, 2, 3, 5, 8, 15, 22, 23, "
                   "24, 26 and its Anexo Tecnico version 1.0 (269 pp.); Estatuto Tributario arts. "
                   "383, 385, 386, 387, 387-1, 388 (resident) and 408-415 (non-resident); CST "
                   "(Decreto 2663 de 1950) arts. 127, 128, 130, 132, 186, 192, 232, 249, 306; "
                   "Ley 50 de 1990 art. 99; Ley 52 de 1975 art. 1; Ley 1393 de 2010 art. 30; "
                   "Ley 2101 de 2021; Ley 2466 de 2025 arts. 21, 52-54, 64; Decreto 0223 de 5 de "
                   "marzo de 2026.",
    "accuracy": "95% (PRIMARY SOURCE). Every field code, XPath, length, cardinality and code table "
                "in this Spec is transcribed from the official 269-page Anexo Tecnico version 1.0 "
                "held at 00-official-sources/pdfs/AnexoTecnico-NominaElectronica-V1.0.pdf, and the "
                "SOAP contract and CUNE algorithm are quoted from its sections 8 and 9. The 5% "
                "reservation is: (a) the Spec is written against Anexo v1.0 / XSD v1.0.6 and DIAN "
                "has not published a v1.1, so a silent XSD revision would not be reflected; (b) the "
                "annex's own table 5.5.5 Sunday / holiday percentages conflict with Ley 2101 de 2021 "
                "from 1 July 2026 (see the RA query on those rows); (c) three schema defects "
                "recorded as CO-GAP-06 and CO-GAP-07 have no published DIAN workaround. It would "
                "rise to 100% with a DIAN-issued sample XML and a written DIAN position on the "
                "table 5.5.5 percentages.",
    "source_status": "PRIMARY. AnexoTecnico-NominaElectronica-V1.0.pdf (Res. DIAN 000013 de 2021), "
                     "269 pages, extracted to _txt/ne_anexo.txt and _txt/ne_fields.json. 195 "
                     "official NIE / NIAE field codes captured with element name, type, format, "
                     "length, parent, cardinality and XPath. C19 prefix patterns ^NIE[0-9]{3}$ and "
                     "^NIAE[0-9]{3}$ verified against the full extracted list - no invented codes.",
    "channel_notes": [
        "Channel: xml (machine-to-machine) | Portal: DIAN Sistema de Validacion y Gestion de "
        "Documentos, catalogo-vpfe.dian.gov.co | Source: Anexo Tecnico v1.0 s.9.3 to s.9.8 (SOAP 1.2, "
        "Document/Literal, TLS 1.2 mutual authentication, WS-Security 1.0 X.509 Token Profile 1.1) | "
        "CONFIRMED.",
        "This is the ONE Colombian payroll filing that is genuinely machine-to-machine. It inverts "
        "the Colombian default: Formulario 350, Formulario 220 and Formato 2276 are portal "
        "round-trips, and PILA is filed through a licensed private operador de informacion. Do not "
        "generalise the M2M posture from this filing to the others.",
        "Operation SendNominaSync takes a single parameter, wcf:contentFile, carrying the base64 of "
        "a ZIP that contains the signed XML. Maximum 500 KB. Anexo s.9.5 and s.9.7.2 print the exact "
        "envelope, reproduced on Sheet 9.",
        "Enablement (habilitacion) with DIAN is a PROJECT PREREQUISITE with a lead time, not a "
        "configuration step: global validation rule 92 rejects any document from a non-enabled "
        "issuer, and rule 90 permits a given document number only once per employee.",
    ],
    "integration_notes": [
        "integration_type = BOTH (scope_manifest CO-BOTH-NE). Outbound: the signed XML. Inbound: the "
        "synchronous base64 ApplicationResponse in the same call.",
        "The inbound leg (CO-IN-NE-APPRESPONSE) is specified in this workbook rather than in a "
        "separate file, because it is not an independent government-to-employer flow - it is the "
        "response half of a single synchronous exchange and shares this filing's identifiers. See "
        "the section 'INBOUND - DIAN VALIDATION RESPONSE' on the Spec sheet.",
        "product_mapping_required = true. The XML separates salary from non-salary at ELEMENT level "
        "with paired S / NS element names, so every wage type must carry a HARD salary / non-salary "
        "flag set at configuration time. It cannot be derived at reporting time.",
    ],
    "b1_notes": [
        "RESIDENT: RetencionFuente (NIE177) carries the ET art. 383 progressive table "
        "(0 / 19 / 28 / 33 / 35 / 37 / 39% on the tax-unit bands 0-95, 95-150, 150-360, 360-640, "
        "640-945, 945-2,300, above 2,300 UVT), applied to the art. 388 depurated monthly base under "
        "Procedure 1 or Procedure 2.",
        "NON-RESIDENT: RetencionFuente (NIE177) carries the FLAT 20% of ET art. 408 on the GROSS "
        "payment - no art. 388 depuration, no 25% exempt income, no art. 387 deductions, no tax-free "
        "band. Confirmed by DIAN Concepto 011108 of 29 June 2026, upholding Concepto 1789 "
        "(int. 14595) of 2025.",
        "The XML has NO residence attribute. Residence is therefore invisible to DIAN in this "
        "document and visible only through the amount in NIE177 and, on Formulario 350, through the "
        "hoja-2 pagos-al-exterior section. The engine must carry a residence flag with an effective "
        "date on the employee record, re-evaluate it EVERY period, and switch the schedule "
        "PROSPECTIVELY from the payment following the date the 183-day test is met. Never "
        "retroactively - there is no payroll true-up of the earlier months.",
        "Where the non-resident's work is performed ENTIRELY outside Colombia the income is "
        "foreign-source and not subject to withholding at all (DIAN Oficio 28380 of 2019); "
        "LugarTrabajoPais (NIE050) is the field that evidences this.",
        "Treaty relief can reduce or eliminate the 20% where a double-tax treaty assigns taxing "
        "rights to the residence state. Mercans applies treaty relief ONLY on written client "
        "instruction supported by a residence certificate.",
    ],
    "related": [
        "The monthly sum of RetencionFuente (NIE177) across all employees must reconcile to "
        "Formulario 350 casilla 93 (retenciones - rentas de trabajo, personas naturales) for the "
        "same period - CO-DIAN-002.",
        "Salud (NIE163), FondoPension (NIE166) and FondoSP (NIE168 / NIE170) must reconcile to the "
        "corresponding PILA Registro Tipo 2 fields 55, 47 and 51 / 52 - CO-PILA-003 - subject to the "
        "different rounding conventions.",
        "Cesantias (NIE120) and PagoIntereses (NIE122) feed Formulario 220 casillas 47-49 and "
        "Formato 2276 numerals 18-20 - CO-DIAN-004 and CO-DIAN-005.",
        "The annual accumulation of every Devengados element feeds Formulario 220 casillas 36-52 "
        "and Formato 2276 numerals 5-22.",
        "The graphical representation (payslip) is PERMISSIVE under art. 24, but if issued it must "
        "carry the thirteen art. 5 items and a QR of at least 2 cm on EVERY page. Colombia has NO "
        "statutory payslip-content article in its labour code - the itemisation rule is this tax "
        "resolution. See 06-payslip.",
    ],
    "scope": (SCOPE_WHO + [
        "AMOUNTS AND CALCULATIONS",
        ("Basic salary for the days worked", "YES",
         "SueldoTrabajado (NIE070). The single largest input to every downstream filing."),
        ("Statutory transport allowance", "YES",
         "AuxilioTransporte (NIE071), where the employee earns up to 2 SMMLV. Not salary for "
         "contributions, but IS in the base of cesantias, prima and the severance indemnity."),
        ("Overtime and premium hours, itemised by type with times and percentages", "YES",
         "Seven separate hour-type blocks (table 5.5.5), each with start time, end time, quantity, "
         "percentage and amount. A single aggregated 'overtime' figure is NOT admissible."),
        ("Vacation taken and vacation compensated in cash, as separate elements", "YES",
         "VacacionesComunes and VacacionesCompensadas. They must not be merged: enjoyed vacation is "
         "in the contribution base, compensated vacation is not."),
        ("Service bonus, severance savings and interest on severance savings", "YES",
         "Primas, Cesantias and Cesantias/@PagoIntereses. Reported here even though severance "
         "savings are excluded from the monthly withholding base."),
        ("Incapacity, maternity / paternity leave and paid leave", "YES",
         "Each with its own dates, quantity and amount, and - for incapacity - its type code."),
        ("Unpaid leave and lawful strike", "YES",
         "Reported as days ONLY. Both blocks deliberately carry no amount element."),
        ("Benefits in kind (salary in kind)", "YES",
         "Through the paired OtroConcepto S / NS elements or the specific allowance elements. "
         "Valued contractually or by expert appraisal; Colombia has no notional valuation scale."),
        ("Employer social-security contributions", "NO",
         "The document reports what the EMPLOYEE accrued and what was DEDUCTED from the employee. "
         "The employer's 12% pension, 8.5% health, occupational-risk premium and 9% levies are an "
         "employer cost reported on PILA, never a deduction here."),
        ("Employer payroll levies (SENA 2%, ICBF 3%, CCF 4%)", "NO",
         "Employer cost, reported on PILA. Never an employee deduction."),
        ("Documented business-expense reimbursements", "NO",
         "Not remuneration. Excluded from the accrued block; only the permanent portion of viaticos "
         "(NIE072) is reportable, and only because it is salary."),
        ("Amounts in a currency other than the Colombian peso", "NO",
         "Res. 000013 de 2021 art. 26 makes the peso mandatory. A foreign currency may be ADDED to a "
         "graphical representation but never substituted; the TRM element (NIE200) exists in the "
         "schema but is out of scope for a Colombian payroll."),
    ] + SCOPE_TIMING + [
        "SPECIAL CASES",
        ("Employee with zero net pay (deductions equal accrued)", "YES",
         "A document is still required. ComprobanteTotal (NIE189) is 0.00; the accrued and deducted "
         "blocks are fully itemised."),
        ("Employee whose withholding falls in the 0% band", "YES",
         "The payment is still reported. RetencionFuente (NIE177) is simply omitted rather than "
         "zero-filled."),
        ("Mid-month hire or mid-month leaver", "YES",
         "DiasTrabajados (NIE069) is reduced; FechaIngreso or FechaRetiro is set; TiempoLaborado is "
         "computed to the settlement end on the 360/30 convention."),
        ("Second employer of a multi-employer employee", "YES",
         "Each employer issues its own document for its own payments. There is no aggregation across "
         "employers at document level."),
        ("Employee paid semi-monthly", "YES",
         "ONE monthly document carrying PeriodoNomina = 4 (Quincenal) and TWO FechaPago (NIE203) "
         "occurrences. Not two documents."),
        ("Correction of a previously validated document", "YES",
         "By adjustment note (NominaIndividualDeAjuste), never by re-sending the original number - "
         "global rule 90 forbids reuse."),
        ("Employee holding a PPT (Permiso por Proteccion Temporal)", "YES",
         "Reported, but see CO-GAP-06: the annex has no PPT document-type code because the PPT "
         "post-dates it. Code 47 (PEP) is the only available proxy."),
    ]),
    "fields": FIELDS,
}
