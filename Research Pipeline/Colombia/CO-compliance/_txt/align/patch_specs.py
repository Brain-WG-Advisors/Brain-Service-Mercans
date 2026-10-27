# -*- coding: utf-8 -*-
"""CO v1.1 alignment patch - STEP 3: report specs (CHECKs 1, 2, 4, 5, 6)."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SP = os.path.abspath(os.path.join(HERE, "..", "..", "04-reports-spec"))
applied = []


def edit(fn, old, new, count=1, label=""):
    p = os.path.join(SP, fn)
    src = open(p, encoding="utf-8").read()
    n = src.count(old)
    assert n == count, "%s: expected %d occurrence(s) of %r, found %d" % (
        fn, count, old[:70], n)
    open(p, "w", encoding="utf-8").write(src.replace(old, new, count))
    applied.append("%-26s %s" % (fn, label))


# =====================================================================
# CHECK 2 (F3) - Contract.Contractual_Salary is an AMOUNT.
# The pipeline DD rule is explicit: "Base Salary / Basic Salary amounts ->
# WTC, NOT DD". The DD build already excludes it; the spec build was still
# flagging it Payroll Field = Y, which broke DD<->spec lock-step on
# CO-DIAN-001 NIE062, CO-PILA-003 T2R2-040 and CO-CESANTIAS-006 T12.
# =====================================================================
edit("build_co_specs.py",
     '    "Contract.Type_Code", "Contract.Start_Date", "Contract.End_Date",\n'
     '    "Contract.Contractual_Salary", "Contract.Pay_Frequency_Code",\n',
     '    "Contract.Type_Code", "Contract.Start_Date", "Contract.End_Date",\n'
     '    "Contract.Pay_Frequency_Code",\n'
     '    # Contract.Contractual_Salary is DELIBERATELY ABSENT (v1.1 alignment\n'
     '    # patch). It is an AMOUNT, and the pipeline DD scope rule routes\n'
     '    # "Base Salary / Basic Salary amounts -> WTC, NOT DD". Keeping it here\n'
     '    # set col E = Y on NIE062 / T2R2-040 / T12 while the Data Dictionary\n'
     '    # (build_co_dd.py) correctly omitted the field, breaking lock-step.\n',
     label="CHECK 2 - Contract.Contractual_Salary removed from _DD_MASTER_MAPPINGS")

# =====================================================================
# CHECK 2 (F3) - System Mapping prefix must match the classification.
# These are calculated amounts correctly flagged Payroll Field = N, but the
# "Employee." prefix reads as master data and is what a mechanical audit
# keys on. Retag to "Payroll.".
# =====================================================================
for old, new, fn in [
    ("Employee.Taxable_Base_Art388", "Payroll.Taxable_Base_Art388", "co_r2_formulario350.py"),
    ("Employee.Pension_Taxable_Base", "Payroll.Pension_Taxable_Base", "co_r2_formulario350.py"),
    ("Employee.Income_Tax_Withheld", "Payroll.Income_Tax_Withheld", "co_r2_formulario350.py"),
    ("Employee.Pension_Tax_Withheld", "Payroll.Pension_Tax_Withheld", "co_r2_formulario350.py"),
]:
    p = os.path.join(SP, fn)
    src = open(p, encoding="utf-8").read()
    assert old in src, "%s not found in %s" % (old, fn)
    open(p, "w", encoding="utf-8").write(src.replace(old, new))
    applied.append("%-26s CHECK 2 - %s -> %s" % (fn, old, new))

for tok in ("Employee.NonResident_Gross", "Employee.NonResident_Withholding"):
    p = os.path.join(SP, "co_r2_formulario350.py")
    src = open(p, encoding="utf-8").read()
    assert tok in src
    open(p, "w", encoding="utf-8").write(src.replace(tok, tok.replace("Employee.", "Payroll.")))
    applied.append("%-26s CHECK 2 - %s -> Payroll.*" % ("co_r2_formulario350.py", tok))

p = os.path.join(SP, "co_r3_pila.py")
src = open(p, encoding="utf-8").read()
assert "Employee.Parafiscal_Base" in src
open(p, "w", encoding="utf-8").write(src.replace("Employee.Parafiscal_Base", "Payroll.Parafiscal_Base"))
applied.append("%-26s CHECK 2 - Employee.Parafiscal_Base -> Payroll.Parafiscal_Base" % "co_r3_pila.py")

# =====================================================================
# CHECK 1 (F1) - option-code alignment against the DD mappers
# =====================================================================
edit("co_r1_sheets.py",
     '    ("21", "EST-P", "Estudiantes de postgrado en salud", "Health postgraduate student."),',
     '    ("21", "EST-PG", "Estudiantes de postgrado en salud", "Health postgraduate student. "\n'
     '     "Same mnemonic as the PILA tipo cotizante 21 and the DD Worker Type mapper."),',
     label="CHECK 1 - tipo trabajador 21 abbrev EST-P -> EST-PG (DD alignment)")

edit("co_r3_sheets.py",
     '    ("D", "LEY 1429", "Aportante beneficiario de la Ley de Formalizacion y Generacion de Empleo",',
     '    ("D", "LEY1429", "Aportante beneficiario de la Ley de Formalizacion y Generacion de Empleo",',
     label="CHECK 1 - clase de aportante D abbrev 'LEY 1429' -> 'LEY1429' (DD alignment)")

# ---- Form 220 PARENTESCO: carry the DD codes (CHECK 1 / CHECK 4) ----
edit("co_r4_sheets.py",
     '    "PARENTESCO - DEPENDIENTE ECONOMICO (casilla 82, ET art. 387 par. 2)",\n'
     '    ("HIJO / HIJA", "-", "Hijos menores de 18 anos", "Children under 18."),\n'
     '    ("HIJO / HIJA", "-", "Hijos entre 18 y 23 anos financiados por el contribuyente en su educacion",\n'
     '     "Children aged 18 to 23 whose education the taxpayer finances at a recognised institution."),\n'
     '    ("HIJO / HIJA", "-", "Hijos mayores de 23 anos en situacion de dependencia certificada",\n'
     '     "Children over 23 with certified physical or psychological dependency."),\n'
     '    ("CONYUGE / COMPANERO", "-", "Conyuge o companero permanente en situacion de dependencia",\n'
     '     "Spouse or permanent partner in a certified state of dependency by absence of income or "\n'
     '     "physical or psychological factors."),\n'
     '    ("PADRE / MADRE / HERMANO", "-", "Padres y hermanos en situacion de dependencia",\n'
     '     "Parents and siblings in a certified state of dependency."),\n',
     '    "PARENTESCO - DEPENDIENTE ECONOMICO (casilla 82, ET art. 387 par. 2). Casilla 82 accepts "\n'
     '    "FREE TEXT, so the engine emits the Local (ES) wording; the Code column is the "\n'
     '    "Mercans-internal normalisation and is the SAME code table as the Data Dictionary mapper "\n'
     '    "\'Dependant Relationship\'. The five limbs are EXHAUSTIVE.",\n'
     '    ("HIJO-M18", "H18", "Hijos menores de 18 anos", "Children under 18."),\n'
     '    ("HIJO-EST", "HED", "Hijos entre 18 y 23 anos financiados por el contribuyente en su educacion",\n'
     '     "Children aged 18 to 23 whose education the taxpayer finances at a recognised institution."),\n'
     '    ("HIJO-DEP", "HDP", "Hijos mayores de 23 anos en situacion de dependencia certificada",\n'
     '     "Children over 23 with certified physical or psychological dependency."),\n'
     '    ("CONYUGE", "CON", "Conyuge o companero permanente en situacion de dependencia",\n'
     '     "Spouse or permanent partner in a certified state of dependency by absence of income or "\n'
     '     "physical or psychological factors."),\n'
     '    ("ASCEND-HERM", "APH", "Padres y hermanos en situacion de dependencia",\n'
     '     "Parents and siblings in a certified state of dependency."),\n',
     label="CHECK 1/4 - PARENTESCO code table now carries the DD codes")

# =====================================================================
# CHECK 4 (F14) - Sheet 6 sections that col O references must resolve to
# =====================================================================
edit("co_r1_sheets.py",
     '    "GEOGRAPHIC CODES (Anexo tables 5.4.1 to 5.4.3)",',
     '    "GEOGRAPHIC CODES - PAISES (Anexo table 5.4.1), DEPARTAMENTOS (table 5.4.2) and "\n'
     '    "MUNICIPIOS (table 5.4.3)",',
     label="CHECK 4 - geographic section renamed so Paises/Departamentos/Municipios resolve")

edit("co_r1_sheets.py",
     '    "TIPO DE HORA EXTRA O RECARGO (Anexo table 5.5.5, @Porcentaje on the 7 hour blocks)",',
     '    "TIPO DE HORA EXTRA O RECARGO / OVERTIME - SURCHARGE TYPE (Anexo table 5.5.5, "\n'
     '    "@Porcentaje on the 7 hour blocks)",',
     label="CHECK 4 - overtime section renamed so 'Overtime / surcharge type' resolves")

edit("co_r3_pila.py",
     'opts="-> Sheet 6: Modalidad de planilla"',
     'opts="-> Sheet 6: Modalidad de la planilla"',
     label="CHECK 4 - col O ref aligned to the 'MODALIDAD DE LA PLANILLA' section header")

edit("co_r6_cesantias.py",
     'opts="-> Sheet 6: Respuesta validacion Asofondos"',
     'opts="-> Sheet 6: Respuesta a la validacion Asofondos"',
     label="CHECK 4 - col O ref aligned to the 'RESPUESTA A LA VALIDACION ASOFONDOS' header")

print("STEP 3 part 1 done")
for a in applied:
    print("   ", a)
