# -*- coding: utf-8 -*-
"""
Colombia (CO) Wage Type Catalogue — build_co_wtc.py
====================================================
Compliant builder (v2.4 / v2.5).

  * LOADS shared/_CZ_Wage_Type_Catalogue_V2_0.xlsx (does NOT create a new
    Workbook), preserving sheet order and the blue(theme8) / orange(FFFF9900)
    header formatting.
  * Includes ALL 300 global baseline codes from shared/Global_WTC_V1_0.xlsx,
    each configured FRESH for Colombia 2026 - nothing copied from any other
    country.
  * Adds 102 Colombia-specific wage types.
  * Expands the single CZ "Subject to Social Insurance" column into FIVE
    per-fund columns (Salud / FSP / ARL / Parafiscales / Pension) and adds
    three Colombia-specific base columns (salary flag / statutory-benefit
    base / vacation base), because Colombia runs on THREE SEPARATE BASES.
  * Adds the "Global WTC Coverage" sheet (5th) and the "Form Reference Guide"
    sheet (6th, C17); repurposes "Tax Credit" and "Sick Leave Paid By
    Employer" for Colombia.
  * Runs the v2.5 C3 post-generation validation and guards the Egypt F20
    failures (commission present, no foreign tax codes, no unexplained
    ambiguity).

Run with `python build_co_wtc.py`. Console: set PYTHONIOENCODING=utf-8.
Output: CO-WTC-001-v1.0.xlsx
"""

import copy
import datetime
import json
import os
import sys

import openpyxl
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from co_wtc_config import (  # noqa: E402
    COLUMNS, NCOL, COL_WIDTHS, TAX_SS_COLS_1B, BASE_COLS_1B, TAX_CODES,
    SMMLV, UVT, AUX_TTE, IBC_CAP, FSP_TRIG, EXON_CUT, INTEGRAL, DIVISOR,
)
from co_wtc_global import classify_global                      # noqa: E402
from co_wtc_specific import CO_EARNINGS                        # noqa: E402
from co_wtc_specific2 import CO_DEDUCTIONS, CO_EMPLOYER        # noqa: E402
from co_wtc_specific3 import CO_STRUCTURAL                     # noqa: E402

CO_SPECIFIC = CO_EARNINGS + CO_DEDUCTIONS + CO_EMPLOYER + CO_STRUCTURAL

BASE = os.path.expanduser("~/mercans-pipeline")
SHARED = os.path.join(BASE, "shared")
CO = os.path.join(BASE, "CO-compliance")
CZ_TEMPLATE = os.path.join(SHARED, "_CZ_Wage_Type_Catalogue_V2_0.xlsx")
GLOBAL_WTC = os.path.join(SHARED, "Global_WTC_V1_0.xlsx")
OUT = os.path.join(CO, "02-wtc", "CO-WTC-001-v1.0.xlsx")


# ---------------------------------------------------------------------------
# FORM REFERENCE GUIDE (C17) — wage-type category -> target row in each spec
# Row numbers are the ACTUAL worksheet rows of the 04-reports-spec files.
# ---------------------------------------------------------------------------
SP = {
    "NE":   "CO-DIAN-001-NominaElectronica-Spec.xlsx",
    "F350": "CO-DIAN-002-Formulario350-Spec.xlsx",
    "PILA": "CO-PILA-003-AportesSeguridadSocial-Spec.xlsx",
    "F220": "CO-DIAN-004-Formulario220-Spec.xlsx",
    "2276": "CO-DIAN-005-Formato2276-Spec.xlsx",
    "CES":  "CO-CESANTIAS-006-ConsignacionAnual-Spec.xlsx",
}
SH = {
    "NE": "Nomina Electronica Spec", "F350": "Formulario 350 Spec",
    "PILA": "PILA Spec", "F220": "Formulario 220 Spec",
    "2276": "Formato 2276 Spec", "CES": "Consignacion Cesantias Spec",
}

FORM_MAP = [
    ("Basic salary (CO-SALARIO-BASICO, global 62100-62109)", SP["NE"], SH["NE"], "Rows 84-85 (NIE069, NIE070)",
     "DiasTrabajados and SueldoTrabajado. Days on the 30-day commercial month."),
    ("Basic salary -> annual salary certificate", SP["F220"], SH["F220"], "Row 27 (casilla 36)",
     "'Pagos por salarios'. Also Formato 2276 numeral N05 (row 9)."),
    ("Basic salary -> contribution bases", SP["PILA"], SH["PILA"], "Rows 106-111 (T2R2-040 to T2R2-045)",
     "Salario basico, salario integral flag, then IBC pension / salud / ARL / CCF. T2R2-095 (row 112) carries "
     "the separate base for parafiscals other than the CCF."),
    ("All-inclusive salary flag (CO-SALARIO-INTEGRAL)", SP["NE"], SH["NE"], "Row 65 (NIE056)",
     "SalarioIntegral. PILA row 107 (T2R2-041). Drives IBC and levy base at 70%."),
    ("Transport / connectivity allowance (CO-AUX-TRANSPORTE, CO-AUX-CONECTIVIDAD, global 62520-62523)",
     SP["NE"], SH["NE"], "Row 86 (NIE071)",
     "AuxilioTransporte. OUT of the IBC and the levy base, so it appears in no PILA base field; IN the "
     "statutory-benefit base, so it feeds the Primas and Cesantias amounts."),
    ("Per diem - board and lodging portion (CO-VIATICOS-PERMANENTES)", SP["NE"], SH["NE"],
     "Row 87 (NIE072)", "ViaticoManuAlojS - the SALARY portion under CST art. 130. F220 casilla 43 (row 34)."),
    ("Per diem - transport / representation and occasional (CO-VIATICOS-OCASIONALES)", SP["NE"], SH["NE"],
     "Row 88 (NIE073)", "ViaticoManuAlojNS - the NON-SALARY portion. Paired element; never merge the two."),
    ("Day overtime (CO-HED, global overtime codes)", SP["NE"], SH["NE"], "Rows 90-94 (NIE074-NIE078)",
     "HED block: start time, end time, quantity, percentage, amount. Percentage reported at the real "
     "statutory rate per DIAN Concepto 013840 de 2025, not the annex literal."),
    ("Night overtime (CO-HEN)", SP["NE"], SH["NE"], "Rows 95-99 (NIE079-NIE083)", "HEN block."),
    ("Night premium (CO-RECARGO-NOCTURNO)", SP["NE"], SH["NE"], "Rows 100-104 (NIE084-NIE088)",
     "HRN block. 19:00-06:00 window since 25 December 2025."),
    ("Day overtime on a rest day (CO-HEDDF)", SP["NE"], SH["NE"], "Rows 105-109 (NIE089-NIE093)", "HEDDF block."),
    ("Rest-day / holiday premium (CO-RECARGO-DOMINICAL)", SP["NE"], SH["NE"], "Rows 110-114 (NIE094-NIE098)",
     "HRDDF block. 80% to 30 Jun 2026, 90% from 1 Jul 2026 - the annex's legacy 75/100/150/110 literals must "
     "not be configured."),
    ("Night overtime on a rest day (CO-HENDF)", SP["NE"], SH["NE"], "Rows 115-119 (NIE099-NIE103)", "HENDF block."),
    ("Night premium on a rest day (CO-HRNDF)", SP["NE"], SH["NE"], "Rows 120-124 (NIE104-NIE108)", "HRNDF block."),
    ("Vacation taken (CO-VACACIONES)", SP["NE"], SH["NE"], "Rows 126-129 (NIE109-NIE112)",
     "VacacionesComunes. IN the IBC and the levy base - PILA change event VAC/LR at rows 90, 164-165."),
    ("Vacation compensated in cash (CO-VACACIONES-COMPENSADAS)", SP["NE"], SH["NE"],
     "Rows 130-131 (NIE115, NIE116)", "VacacionesCompensadas. Contributory - the most commonly missed line "
     "in a termination settlement."),
    ("Service bonus (CO-PRIMA-SERVICIOS, global 62901)", SP["NE"], SH["NE"], "Rows 132-134 (NIE117-NIE119)",
     "Primas, with PAIRED salary (Pago) and non-salary (PagoNS) amounts. F220 casilla 42 'prestaciones "
     "sociales' (row 33) / 2276 numeral N12 (row 16)."),
    ("Severance savings and interest (CO-CESANTIAS, CO-INTERESES-CESANTIAS)", SP["NE"], SH["NE"],
     "Rows 135-137 (NIE120-NIE122)", "Cesantias: Pago, Porcentaje, PagoIntereses."),
    ("Severance savings -> THREE separate certificate lines", SP["F220"], SH["F220"],
     "Rows 38-40 (casillas 47, 48, 49)",
     "Paid to the employee / traditional CST regime / deposited to the fund. Formato 2276 numerals N18, N20, "
     "N19 (rows 23-25). Never collapse the three."),
    ("Severance savings -> annual deposit planilla", SP["CES"], SH["CES"], "Rows 25-30 (T09-T14)",
     "Fund code, days worked, basic salary of the last month, and the cesantias value. Deposit by 14 "
     "February; MA01-MA05 (rows 39-43) cover the Ley 2466/2025 art. 64 monthly advance."),
    ("Sickness / occupational incapacity (CO-INCAP-EG-EMPLEADOR, CO-INCAP-EG-EPS, CO-INCAP-IRL)",
     SP["NE"], SH["NE"], "Rows 139-143 (NIE123-NIE127)",
     "Incapacidad block with a Tipo discriminator. PILA IGE (row 88) and IRL (row 93); authorisation number "
     "and value at PILA rows 126-127 (T2R2-057, T2R2-058) for the employer's recovery."),
    ("Maternity / paternity / shared parental leave (CO-LIC-MATERNIDAD, CO-LIC-PATERNIDAD, "
     "CO-LIC-PARENTAL-COMPARTIDA)", SP["NE"], SH["NE"], "Rows 144-147 (NIE128-NIE131)",
     "LicenciaMP. PILA LMA (row 89); authorisation number and value at PILA rows 128-129."),
    ("Statutory paid leave and bereavement (CO-LIC-REMUNERADA, CO-LIC-LUTO, CO-DESCANSO-REMUNERADO)",
     SP["NE"], SH["NE"], "Rows 148-151 (NIE132-NIE135)",
     "LicenciaR. Paid rest, so IN the Ley 21/1982 levy base by name."),
    ("Unpaid leave (CO-LIC-NO-REMUNERADA)", SP["NE"], SH["NE"], "Rows 152-154 (NIE136-NIE138)",
     "LicenciaNR. PILA SLN at rows 87, 158-159 - the levies fall to 0% for those days."),
    ("Legal strike (CO-HUELGA-LEGAL)", SP["NE"], SH["NE"], "Rows 155-157 (NIE143-NIE145)", "HuelgaLegal block."),
    ("Bonuses - salary and non-salary (CO-BONIF-HABITUAL, CO-BONIF-NOSALARIAL, CO-GRATIF-OCASIONAL, "
     "global 62200-62229)", SP["NE"], SH["NE"], "Rows 159-160 (NIE139, NIE140)",
     "BonificacionS / BonificacionNS. The salary flag is a hard configuration value, never derived at "
     "reporting time."),
    ("Allowances - salary and non-salary (global 62400-62880, CO-TELETRABAJO, CO-MEDICINA-PREPAGADA-ER)",
     SP["NE"], SH["NE"], "Rows 161-162 (NIE141, NIE142)", "AuxilioS / AuxilioNS."),
    ("Salary in kind, equity, and any other concept (CO-SALARIO-ESPECIE, CO-ACCIONES)", SP["NE"], SH["NE"],
     "Rows 163-165 (NIE146-NIE148)",
     "OtroConcepto with a mandatory description and paired ConceptoS / ConceptoNS amounts. No valuation scale "
     "exists in Colombia - a contractual value is required on every in-kind wage type."),
    ("Cooperative compensation (CO-COMPENSACION-COOP)", SP["NE"], SH["NE"], "Rows 166-167 (NIE149, NIE150)",
     "CompensacionO / CompensacionE. Out of employment-payroll scope; F220 casilla 45 / 2276 numeral N15."),
    ("Voucher and meal payments (CO-BONO-EPCTV, CO-PAGO-ALIMENTACION-3P)", SP["NE"], SH["NE"],
     "Rows 168-171 (NIE151-NIE154)",
     "BonoEPCTV: PagoS / PagoNS and PagoAlimentacionS / PagoAlimentacionNS. The ET art. 387-1 within-limit "
     "and excess portions are reported on SEPARATE information-return numerals - 2276 N32 (row 41) and N08 "
     "(row 12); F220 casillas 37 and 38 (rows 28-29)."),
    ("Commissions (CO-COMISIONES)", SP["NE"], SH["NE"], "Row 172 (NIE155)",
     "Comision - its own dedicated element. F220 casilla 41 (row 32) / 2276 numeral N11 (row 15)."),
    ("Third-party payments and advances (CO-PAGO-TERCERO, CO-ANTICIPO-NOMINA)", SP["NE"], SH["NE"],
     "Rows 173-174 (NIE193, NIE194)",
     "PagoTercero and Anticipo in the DEVENGADOS block, paired with rows 200-201 (NIE195, NIE196) in the "
     "DEDUCCIONES block so the two legs net to zero."),
    ("Work clothing (CO-DOTACION)", SP["NE"], SH["NE"], "Row 175 (NIE156)",
     "Dotacion - a dedicated non-taxable, non-contributory informational element."),
    ("Apprentice maintenance support (CO-APOYO-APRENDIZ)", SP["NE"], SH["NE"], "Row 176 (NIE157)",
     "ApoyoSost. Contribution base floored at 1 SMMLV per Decreto 0223 de 2026 art. 2.2.6.3.3.4 par. 2."),
    ("Telework allowance (CO-TELETRABAJO)", SP["NE"], SH["NE"], "Row 177 (NIE158)", "Teletrabajo."),
    ("Retirement / settlement bonus (CO-BONIF-RETIRO)", SP["NE"], SH["NE"], "Row 178 (NIE159)",
     "BonifRetiro - separate from Indemnizacion."),
    ("Termination indemnities and penalties (CO-INDEM-DESPIDO, CO-INDEM-MORATORIA, CO-SANCION-CESANTIAS, "
     "CO-SANCION-INTERESES, CO-INDEM-FIJO-OBRA, CO-INDEM-PROTECCION)", SP["NE"], SH["NE"],
     "Row 179 (NIE160)", "Indemnizacion. Fully taxable, out of every social-security base."),
    ("Reimbursement (CO-REINTEGRO)", SP["NE"], SH["NE"], "Row 180 (NIE201)",
     "Reintegro in devengados, paired with row 207 (NIE184) in deducciones."),
    ("Employee health 4% (CO-DED-SALUD)", SP["NE"], SH["NE"], "Rows 182-183 (NIE161, NIE163)",
     "Salud percentage and amount. PILA rows 123-124 (T2R2-054, T2R2-055). Non-taxable income at F220 "
     "casilla 53 / 2276 numeral N23."),
    ("Employee pension 4% (CO-DED-PENSION)", SP["NE"], SH["NE"], "Rows 184-185 (NIE164, NIE166)",
     "FondoPension percentage and amount. PILA rows 114-115. F220 casilla 54 / 2276 numeral N24 group the "
     "pension and solidarity contributions on ONE line."),
    ("Solidarity pension fund (CO-DED-FSP-SOLIDARIDAD, CO-DED-FSP-SUBSISTENCIA)", SP["NE"], SH["NE"],
     "Rows 186-189 (NIE167-NIE170)",
     "FondoSP with FOUR attributes - solidarity percentage and amount, subsistence percentage and amount. "
     "MUST NOT be merged into the pension line. PILA rows 119-120 (T2R2-051, T2R2-052)."),
    ("Income tax withheld (CO-RETENCION-FUENTE, CO-RETENCION-NO-RESIDENTE)", SP["NE"], SH["NE"],
     "Row 190 (NIE177)", "RetencionFuente."),
    ("Income tax withheld -> monthly return", SP["F350"], SH["F350"], "Rows 22-23 (casillas 77 and 93)",
     "Rentas de trabajo: base sujeta a retencion and retenciones. Pension income at casillas 78 / 94 "
     "(rows 24-25). NON-RESIDENT payments at casillas 109-112 (rows 31-34) with the hoja-2 annex at casillas "
     "141-155 (rows 36-50)."),
    ("Income tax withheld -> annual certificate and information return", SP["F220"], SH["F220"],
     "Row 52 (casilla 60)", "Retencion on labour and pension income. Formato 2276 numeral N29 (row 37). The "
     "six-month average labour income for the cesantias taper sits at F220 casilla 59 (row 51) / 2276 "
     "numeral N33 (row 42)."),
    ("Voluntary pension, AFC / AVC and RAIS contributions (CO-DED-PENSION-VOLUNTARIA, CO-DED-AFC-AVC, "
     "CO-DED-RAIS-VOLUNTARIO, CO-APORTE-PENSION-VOL-ER, CO-APORTE-RAIS-VOL-ER)", SP["NE"], SH["NE"],
     "Rows 192-193 (NIE198, NIE179)",
     "PensionVoluntaria and AFC. F220 casillas 55-58 (rows 47-50) / 2276 numerals N25-N28 (rows 32-35) "
     "distinguish all four vehicles. PILA AVP at rows 91, 116-117, 121."),
    ("Union dues (CO-DED-SINDICATO)", SP["NE"], SH["NE"], "Rows 194-195 (NIE171, NIE172)",
     "Sindicato percentage and amount."),
    ("Disciplinary sanctions (CO-DED-SANCION-DISCIPLINARIA)", SP["NE"], SH["NE"], "Rows 196-197 (NIE173, NIE174)",
     "SancionPublic / SancionPriv. Lawful only under a duly approved reglamento interno."),
    ("Payroll lending (CO-DED-LIBRANZA)", SP["NE"], SH["NE"], "Rows 198-199 (NIE175, NIE176)",
     "Libranza description and amount. Must leave at least 50% of net salary (Ley 1527 de 2012)."),
    ("Cooperative dues (CO-DED-COOPERATIVA)", SP["NE"], SH["NE"], "Row 203 (NIE180)", "Cooperativa."),
    ("Garnishments (CO-DED-EMBARGO, CO-DED-ALIMENTOS)", SP["NE"], SH["NE"], "Row 204 (NIE181)",
     "EmbargoFiscal. Art. 155 20%-of-excess and art. 156 50%-of-whole ceilings are different ceilings for "
     "different claim types, tested independently."),
    ("Prepaid health / complementary plan (CO-DED-MEDICINA-PREPAGADA)", SP["NE"], SH["NE"], "Row 205 (NIE182)",
     "PlanComplementarios. Separately generates the 16-UVT/month art. 387 deduction."),
    ("Education debt and Contribucion Sabes (CO-DED-SABES)", SP["NE"], SH["NE"], "Row 206 (NIE183)",
     "Educacion. A DEDUCTION, not a tax - never aggregate it with the retencion on Formulario 350."),
    ("Employer loans, advances and other deductions (CO-DED-PRESTAMO, CO-DED-OTRAS)", SP["NE"], SH["NE"],
     "Rows 201-202, 208 (NIE196, NIE197, NIE185)", "Anticipo, OtraDeduccion and Deuda."),
    ("Employer health 8.5% and the exoneration test (CO-ER-SALUD, CO-FLAG-EXONERACION-114-1)", SP["PILA"],
     SH["PILA"], "Rows 123-124, 36, 150 (T2R2-054, T2R2-055, A1-033, T2R2-076)",
     "Employer-level and contributor-level exoneration flags. Not a nomina electronica element - employer "
     "contributions never appear there."),
    ("Employer pension 12% and high-risk uplift (CO-ER-PENSION, CO-ER-PENSION-ALTO-RIESGO)", SP["PILA"],
     SH["PILA"], "Rows 114-118, 152 (T2R2-046 to T2R2-050, T2R2-079)",
     "Rate, mandatory contribution, voluntary member and employer amounts, total, and the special-rate "
     "indicator. Nomina electronica AltoRiesgoPension flag at row 54 (NIE043)."),
    ("Occupational risk (CO-ER-ARL)", SP["PILA"], SH["PILA"],
     "Rows 131-135 (T2R2-061, T2R2-062, T2R2-063, T2R2-077, T2R2-078)",
     "Rate, work centre, contribution, ARL code and risk class. Class varies by WORK CENTRE, not geography."),
    ("Payroll levies CCF / SENA / ICBF (CO-ER-CCF, CO-ER-SENA, CO-ER-ICBF)", SP["PILA"], SH["PILA"],
     "Rows 137-142 (T2R2-064 to T2R2-069)",
     "Rate and value per levy. Bases at rows 111-112: T2R2-045 for the CCF and T2R2-095 for the other "
     "parafiscals, which diverge when SENA and ICBF are exonerated and the CCF is not. ESAP and MEN "
     "(rows 143-146) are public-sector only."),
    ("Contributory days per subsystem", SP["PILA"], SH["PILA"], "Rows 101-104 (T2R2-036 to T2R2-039)",
     "Pension / health / occupational risk / CCF days, reported per subsystem because a change event can "
     "reduce them for one and not another."),
    ("Change events (novedades) driving every base", SP["PILA"], SH["PILA"], "Rows 78-93 (T2R2-015 to T2R2-030)",
     "ING, RET, TDE/TAE, TDP/TAP, VSP/VST, SLN, IGE, LMA, VAC-LR, AVP, VCT, IRL, with the paired date fields "
     "at rows 155-170."),
    ("Statutory benefit accruals (CO-PROV-PRIMA, CO-PROV-CESANTIAS, CO-PROV-INTERESES-CESANTIAS, "
     "CO-PROV-VACACIONES)", "DERIVED - no statutory filing", "n/a", "DERIVED",
     "Accounting provisions totalling 21.8333%. They feed the Primas, Cesantias and Vacaciones amounts when "
     "the benefit is actually paid, but no return reports the provision itself."),
    ("Rounding residual (CO-REDONDEO)", SP["NE"], SH["NE"], "Rows 210-213 (NIE186-NIE189)",
     "Redondeo, DevengadosTotal, DeduccionesTotal, ComprobanteTotal. Round-half-to-even with a +/-2.00 "
     "tolerance - distinct from the PILA's round-up-to-100 and the DIAN forms' nearest-1,000."),
    ("Tax residence and place of service (CO-FLAG-RESIDENCIA-FISCAL)", SP["NE"], SH["NE"],
     "Rows 61-64 (NIE050-NIE053)",
     "LugarTrabajoPais and the rest of the place-of-work block. PILA 'colombiano en el exterior' (row 70) and "
     "'extranjero no obligado a cotizar a pensiones' (row 69) carry the related flags."),
    ("Dependants declaration (CO-FLAG-DEPENDIENTES)", SP["F220"], SH["F220"], "Rows 68-71 (casillas 79-82)",
     "Document type, number, names and relationship per dependant. Formato 2276 numeral N34 (row 43) requires "
     "the DOCUMENT, not merely a count."),
    ("Withholding procedure election (CO-FLAG-PROCEDIMIENTO-RETENCION)", "DERIVED - no statutory filing",
     "n/a", "DERIVED",
     "Elected by the employer per employee; no return discloses the election. It nonetheless changes the "
     "reported withholding in June and December materially."),
    ("Bases (CO-BASE-IBC, CO-BASE-PARAFISCAL, CO-BASE-RETENCION, CO-BASE-PRESTACIONAL, CO-BASE-VACACIONES) "
     "and the 40% clamp intermediary (CO-INT-CLAMP40)", SP["PILA"], SH["PILA"],
     "Rows 108-112 (T2R2-042 to T2R2-045, T2R2-095)",
     "The IBC columns are where the 40% clamp lands. The withholding base surfaces at Formulario 350 casilla "
     "77; the statutory-benefit and vacation bases are DERIVED and surface only through the benefit amounts "
     "they produce."),
]


def make_row(code, en, es, p, formula, expl, xml):
    """Assemble one catalogue row keyed by 1-based column index."""
    src = TAX_CODES[p["tc"]][1]
    return {
        1: code, 2: en, 3: es, 4: expl, 5: p["cat"], 6: formula, 7: p["tc"],
        8: ("Lump Sum" if p["occ"] in ("Additional", "NA") else "Pro Rata"),
        9: None,
        10: p["occ"],
        11: "No", 12: "No", 13: "Regular (System default)",
        14: p["N"], 15: p["O"], 16: p["P"],
        17: p["Q1"], 18: p["Q2"], 19: p["Q3"], 20: p["Q4"], 21: p["R"],
        22: p["S"], 23: p["T"], 24: p["U"],
        25: xml,
        26: src,
        27: ("No" if p["cat"] in ("Deduction", "Employer Contribution", "Percentage",
                                  "Base", "Flag", "Intermediary", "Notional") else "Yes"),
        28: None,
    }


def build_rows():
    gwb = openpyxl.load_workbook(GLOBAL_WTC)
    gws = gwb["Sheet1"]
    global_rows = [(int(float(r[0])), str(r[1]), str(r[2]))
                   for r in gws.iter_rows(min_row=2, values_only=True) if r[0] is not None]
    assert len(global_rows) == 300, "expected 300 global codes, got %d" % len(global_rows)

    rows = []
    for code, desc, gtype in global_rows:
        p, formula, expl, xml = classify_global(code, desc, gtype)
        rows.append(make_row(code, desc, "(codigo global - ver la explicacion para el tratamiento colombiano)",
                             p, formula, expl, xml))
    for s in CO_SPECIFIC:
        rows.append(make_row(s["code"], s["en"], s["es"], s["p"], s["formula"], s["expl"], s["xml"]))
    return rows, global_rows


def main():
    import co_wtc_main
    rows, global_rows = build_rows()
    counts = dict(specific=len(CO_SPECIFIC), earn=len(CO_EARNINGS), ded=len(CO_DEDUCTIONS),
                  er=len(CO_EMPLOYER), struct=len(CO_STRUCTURAL))
    names = co_wtc_main.write_workbook(CZ_TEMPLATE, OUT, rows, counts, FORM_MAP)
    print("Saved:", OUT)
    print("Rows in Wage Type Catalogue: %d (300 global + %d Colombia-specific)"
          % (len(rows), len(CO_SPECIFIC)))
    print("Sheets:", names)
    co_wtc_main.validate(OUT, GLOBAL_WTC, os.path.join(CO, "scope_manifest.json"))
    return OUT


if __name__ == "__main__":
    main()
