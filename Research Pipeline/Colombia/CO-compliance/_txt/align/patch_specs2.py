# -*- coding: utf-8 -*-
"""CO v1.1 alignment patch - STEP 3 part 2: missing Sheet 6 code tables (F14),
composite-key documentation (F12) and code-prefix patterns in column J (CHECK 6).
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SP = os.path.abspath(os.path.join(HERE, "..", "..", "04-reports-spec"))
applied = []


def edit(fn, old, new, count=1, label=""):
    p = os.path.join(SP, fn)
    src = open(p, encoding="utf-8").read()
    n = src.count(old)
    assert n == count, "%s: expected %d of %r, found %d" % (fn, count, old[:70], n)
    open(p, "w", encoding="utf-8").write(src.replace(old, new, count))
    applied.append("%-26s %s" % (fn, label))


# =====================================================================
# CHECK 4 (F14) - PILA Sheet 6: two referenced sections did not exist.
#   A1-034   -> "Sheet 6: Ley 1429 de 2010"        (no section at all)
#   T2R2-003 -> "Sheet 6: Tipo documento cotizante" (no section at all)
# T2R2-003 is the EMPLOYEE document type on the social-security channel and is
# a Payroll Field = Y master-data field, so an absent code table is a hard gap.
# Source for the eight values: PILA Anexo Tecnico 2 (AT2 version 09, 16-09-2019),
# Archivo Tipo 2 Registro Tipo 2 campo 3, verbatim.
# =====================================================================
NEW_SECTIONS = '''    "TIPO DOCUMENTO COTIZANTE (T2R2-003 and T2R2-074) - VERBATIM from Anexo Tecnico 2 campo 3; "
    "eight values, and NOT the DIAN numeric catalogue. Mirrors the Data Dictionary mapper "
    "'Employee Document Type (PILA / Cesantias)'",
    ("CC", "13", "Cedula de ciudadania", "Colombian national identity card. Numeric only. DIAN "
     "numeric equivalent 13."),
    ("CE", "22", "Cedula de extranjeria", "Foreign resident's identity card. Numeric only. DIAN "
     "numeric equivalent 22."),
    ("TI", "12", "Tarjeta de identidad", "Identity card for a person aged 7 to 17. Numeric only. "
     "DIAN numeric equivalent 12."),
    ("PA", "41", "Pasaporte", "Passport. ALPHANUMERIC permitted here - the annex names PA and CD "
     "as the only two alphanumeric types. DIAN numeric equivalent 41."),
    ("CD", "-", "Carne diplomatico", "Diplomatic card. ALPHANUMERIC permitted. NO DIAN numeric "
     "equivalent exists, so this document type cannot be carried on the nomina electronica."),
    ("SC", "-", "Salvoconducto de permanencia", "Safe-conduct of stay. Numeric only. NO DIAN "
     "numeric equivalent exists."),
    ("RC", "11", "Registro civil", "Civil birth registration. Available in the CONTRIBUTOR list "
     "but NOT in the employer list (A1-002). DIAN numeric equivalent 11."),
    ("PE", "47", "Permiso Especial de Permanencia", "Numeric only and EXACTLY 15 digits (SOI hard "
     "rule). DIAN numeric equivalent 47, abbreviated PEP in Anexo table 5.2.1."),
    ("(not PT)", "-", "Permiso por Proteccion Temporal", "PT is NOT in this fixed-width list. It "
     "is printed in the cesantias XLS document-type list only - see CO-CESANTIAS-006. CO-GAP-06."),

    "LEY 1429 DE 2010 (A1-034) - eleccion del beneficio del art. 5 para la caja de compensacion "
    "familiar",
    ("S", "SI", "Si - el aportante se acoge al beneficio", "The employer elects the Ley 1429 art. 5 "
     "progressive CCF contribution. Decreto 1074 de 2015 art. 2.2.2.42.1. Normally accompanies "
     "Clase de aportante = D, and it makes the commercial registry date (A1-031) and the "
     "registered-seat department code (A1-032) MANDATORY."),
    ("N", "NO", "No - el aportante no se acoge", "THE DEFAULT for an established employer. The "
     "full 4% CCF contribution applies."),
    ("(hard rule)", "-", "-", "The election is only available to an employer that qualifies under "
     "Ley 1429 de 2010 as a small business formalised in the benefit window. Where A1-034 = S but "
     "A1-007 (clase de aportante) is not D, the operador rejects the archivo tipo 1."),

'''

edit("co_r3_sheets.py",
     '    "MODALIDAD DE LA PLANILLA (T2R1-002)",',
     NEW_SECTIONS + '    "MODALIDAD DE LA PLANILLA (T2R1-002)",',
     label="CHECK 4 - added missing 'Tipo documento cotizante' and 'Ley 1429 de 2010' sections")

# =====================================================================
# CHECK 4 (F14) - Formato 2276 document-type table was a single placeholder
# row. Complete it from the catalogues already verified in this pipeline.
# =====================================================================
edit("co_r5_sheets.py",
     '    "TIPO DE DOCUMENTO (numerals 2 and 34)",\n'
     '    ("(DIAN catalogue)", "-", "Tipo de documento de identificacion",\n'
     '     "The document-type codes are fixed by the especificaciones tecnicas, not by Res. 227. DERIVED "\n'
     '     "- confirm the exact list before configuring. Note that the three artefacts in this pipeline "\n'
     '     "use THREE different document-type catalogues: the nomina electronica uses Anexo table 5.2.1 "\n'
     '     "(11, 12, 13, 21, 22, 31, 41, 42, 47, 50, 91), Formulario 220 prints a six-value list (12, 13, "\n'
     '     "21, 22, 31, 41), and PILA uses two-letter codes (CC, CE, TI, PA, CD, SC, PE, RC). Build a "\n'
     '     "mapping table; never copy between them."),\n',
     '    "TIPO DE DOCUMENTO (numerals 2 and 34) - the DIAN NUMERIC catalogue (Anexo Tecnico de la "\n'
     '    "nomina electronica, table 5.2.1). Res. 227 does not print the list; the especificaciones "\n'
     '    "tecnicas of the exogena reuse the DIAN catalogue, so the codes below are DERIVED from "\n'
     '    "table 5.2.1 and are the SAME table the Data Dictionary mapper \'Employee Document Type\' "\n'
     '    "holds. CONFIRM against the especificaciones tecnicas of formato 2276 version 4 before "\n'
     '    "configuring",\n'
     '    ("11", "RC", "Registro civil", "Civil birth registration. Realistic only at numeral 34 "\n'
     '     "(economic dependant), never at numeral 2."),\n'
     '    ("12", "TI", "Tarjeta de identidad", "Identity card for a person aged 7 to 17."),\n'
     '    ("13", "CC", "Cedula de ciudadania", "National identity card. The great majority of "\n'
     '     "beneficiaries and dependants."),\n'
     '    ("21", "TE", "Tarjeta de extranjeria", "Foreigner\'s identity card."),\n'
     '    ("22", "CE", "Cedula de extranjeria", "Foreign resident\'s identity card."),\n'
     '    ("31", "NIT", "NIT", "Tax identification number, where the beneficiary is an entity."),\n'
     '    ("41", "PA", "Pasaporte", "Passport."),\n'
     '    ("42", "DIE", "Documento de identificacion extranjero", "Foreign identity document."),\n'
     '    ("47", "PEP", "PEP - Permiso Especial de Permanencia", "Special residence permit. "\n'
     '     "CO-GAP-06: there is still no code for the PPT."),\n'
     '    ("50", "NIT-EXT", "NIT de otro pais", "Foreign tax identification number."),\n'
     '    ("91", "NUIP", "NUIP", "Unique personal identification number; employee only."),\n'
     '    ("(mapping warning)", "-", "-", "THREE artefacts, THREE catalogues. Formulario 220 prints "\n'
     '     "a SIX-value list (12, 13, 21, 22, 31, 41) and PILA uses two-letter codes (CC, CE, TI, "\n'
     '     "PA, CD, SC, RC, PE). Map by MEANING through the Data Dictionary master value; never "\n'
     '     "copy a code between channels."),\n',
     label="CHECK 4 - Formato 2276 document-type table completed (was a placeholder row)")

# =====================================================================
# CHECK 5 (F12) - Formulario 220 casilla 4 is an employer-assigned composite
# series (example 2026-000417) with no structure documented.
# (Formulario 350 casilla 4 was checked and needs NO change: the instructivo
# says it is "el numero unico asignado por la DIAN" - opaque, not composite.)
# =====================================================================
edit("co_r4_formulario220.py",
     '      "SHARP CONTRAST WITH FORMULARIO 350. The instructivo says this number is \'asignado por la "\n'
     '      "persona natural o juridica que expide la certificacion\' - the EMPLOYER assigns it, not DIAN. "\n'
     '      "On Form 350 casilla 4 is DIAN-assigned. The engine must therefore maintain its own "\n'
     '      "certificate numbering series and keep it stable, because the employee quotes it.",',
     '      "SHARP CONTRAST WITH FORMULARIO 350. The instructivo says this number is \'asignado por la "\n'
     '      "persona natural o juridica que expide la certificacion\' - the EMPLOYER assigns it, not DIAN. "\n'
     '      "On Form 350 casilla 4 is DIAN-assigned and opaque. The engine must therefore maintain its "\n'
     '      "own certificate numbering series and keep it stable, because the employee quotes it. "\n'
     '      "COMPOSITE KEY - position breakdown. Because DIAN prescribes NO structure, the series is "\n'
     '      "Mercans-designed and is fixed here so that it is stable and auditable: positions 1-4 = "\n'
     '      "accrual year AAAA, source PayPeriod.Fiscal_Year, the year the income was earned and NOT "\n'
     '      "the year of issue; position 5 = literal hyphen; positions 6-11 = a six-digit zero-filled "\n'
     '      "consecutive, source Mercans.Certificate_Sequence, restarting at 000001 for each accrual "\n'
     '      "year and unique per employer per year. PERSISTENCE: assigned once and NEVER reused, "\n'
     '      "including after a reissue - a corrected certificate takes the NEXT consecutive and cites "\n'
     '      "the superseded number, because ET art. 378 makes the employee\'s copy the evidential "\n'
     '      "document and two certificates may not share a number.",',
     label="CHECK 5 - casilla 4 Composite Key Structure documented")

# =====================================================================
# CHECK 6 - code-prefix patterns recorded in column J (Format).
# =====================================================================
# PILA administradora codes: 3 alphabetic subsystem letters + 3 digits.
# Verified in the PILA anexo text itself, which names FSP001 (Fondo de
# Solidaridad Pensional), MIN001 and MIN002 in running prose.
edit("co_r3_pila.py",
     'def R(rec, campo, en, mand, cond, ex, mapping, expl, opts="-", rnd=R_NONE,\n'
     '      vt="Text", freq="Monthly", kind="payroll", q="", neg="N"):\n'
     '    """Build a 21-column Spec row from the official layout plus enrichment."""\n'
     '    n, lng, ini, fin, tipo, desc = _LAYOUT[rec][campo]\n'
     '    fmt = ("N(%d) - numeric, right-justified, ZERO-filled to the left" % lng\n'
     '           if tipo == "N" else\n'
     '           "A(%d) - alphanumeric, left-justified, SPACE-filled to the right" % lng)\n',
     'def R(rec, campo, en, mand, cond, ex, mapping, expl, opts="-", rnd=R_NONE,\n'
     '      vt="Text", freq="Monthly", kind="payroll", q="", neg="N", fmt_extra=""):\n'
     '    """Build a 21-column Spec row from the official layout plus enrichment.\n'
     '\n'
     '    fmt_extra (v1.1 alignment patch, CHECK 6) appends a code-prefix pattern to\n'
     '    column J for coded identifier fields, so the pattern is stated where the\n'
     '    dev team reads the format and not only in the Sheet 6 note.\n'
     '    """\n'
     '    n, lng, ini, fin, tipo, desc = _LAYOUT[rec][campo]\n'
     '    fmt = ("N(%d) - numeric, right-justified, ZERO-filled to the left" % lng\n'
     '           if tipo == "N" else\n'
     '           "A(%d) - alphanumeric, left-justified, SPACE-filled to the right" % lng)\n'
     '    if fmt_extra:\n'
     '        fmt = fmt + ". " + fmt_extra\n',
     label="CHECK 6 - R() gained fmt_extra for code-prefix patterns")

ADMIN = ("Prefix pattern ^(ARL|EPS|EOC|AFP|CCF|FSP)[0-9]{3}$ - THREE alphabetic positions "
         "identifying the subsystem followed by THREE numeric positions identifying the "
         "administradora. Verified against the PILA anexo, which names FSP001, MIN001 and MIN002 "
         "in running prose. The code LIST itself is master data published by the Ministerio de "
         "Salud y Proteccion Social; validate the prefix here and the code against the catalogue")

for campo_ref, note in [
    ('R("T2R1", 14, "ARL code"', ADMIN),
    ('R("T2R2", 31, "Pension fund of the member"', ADMIN),
    ('R("T2R2", 32, "Pension fund to which the member transfers"', ADMIN),
    ('R("T2R2", 33, "EPS or EOC of the member"', ADMIN),
    ('R("T2R2", 34, "EPS or EOC to which the member transfers"', ADMIN),
    ('R("T2R2", 35, "CCF of the member"', ADMIN),
]:
    p = os.path.join(SP, "co_r3_pila.py")
    src = open(p, encoding="utf-8").read()
    i = src.index(campo_ref)
    j = src.index('vt="Code")', i)
    src = src[:j] + 'vt="Code", fmt_extra="%s")' % note + src[j + len('vt="Code")'):]
    open(p, "w", encoding="utf-8").write(src)
    applied.append("%-26s CHECK 6 - prefix pattern on %s" % ("co_r3_pila.py", campo_ref[2:40]))

edit("co_r2_formulario350.py",
     '      "Hoja 1, casilla 983", "Var", "A", "123456-T", "Mercans.Accountant_Card_Number",\n'
     '      "Professional card number issued by the Junta Central de Contadores.",',
     '      "Hoja 1, casilla 983", "Var",\n'
     '      "AN - prefix pattern ^[0-9]{1,6}-T$: the numeric registration followed by a hyphen and "\n'
     '      "the literal suffix T (for Contador). Store the printed value including the -T suffix; "\n'
     '      "do not strip it, because the Junta quotes the card with it",\n'
     '      "123456-T", "Mercans.Accountant_Card_Number",\n'
     '      "Professional card number issued by the Junta Central de Contadores. The -T suffix is "\n'
     '      "part of the identifier, not a separator.",',
     label="CHECK 6 - casilla 983 professional-card prefix pattern in column J")

edit("co_r1_nomina_electronica.py",
     '      "/NominaIndividual/NumeroSecuenciaXML/@Prefijo", "Var", "A", "NE",',
     '      "/NominaIndividual/NumeroSecuenciaXML/@Prefijo", "Var",\n'
     '      "A - prefix pattern ^[A-Z]{1,4}$: uppercase alphabetic only, no digits, no spaces and "\n'
     '      "no punctuation, exactly as authorised by DIAN at enablement. The same string must open "\n'
     '      "NIE012, whose pattern is therefore ^[A-Z]{1,4}[0-9]+$",\n'
     '      "NE",',
     label="CHECK 6 - NIE010 numbering-prefix pattern in column J")

edit("co_r1_nomina_electronica.py",
     '"COMPOSITE KEY - position breakdown. Numero = Prefijo (NIE010) immediately followed by "',
     '"COMPOSITE KEY - position breakdown. Pattern ^[A-Z]{1,4}[0-9]+$. Numero = Prefijo (NIE010) "\n'
     '      "immediately followed by "',
     label="CHECK 6 - NIE012 document-number pattern stated with the composite key")

print("STEP 3 part 2 done")
for a in applied:
    print("   ", a)
