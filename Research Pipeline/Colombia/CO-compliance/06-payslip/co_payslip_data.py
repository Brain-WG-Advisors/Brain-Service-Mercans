# -*- coding: utf-8 -*-
"""
Colombia Compliance Payslip Generator - sample data, labels and statutory notes.

Every figure below is derived from CO-CCG-001-v1.0 (Modules 3-10), CO-WTC-001-v1.0
(Wage Type Catalogue) and CO-DD-001-v1.0 (Country Option Mappers).

Sample period: August 2026 - i.e. AFTER both mid-2026 cut-overs
  * ordinary-hour divisor 220 -> 210 from 15 Jul 2026 (Ley 2101 de 2021, 42-hour week)
  * rest-day / holiday premium 80% -> 90% from 1 Jul 2026 (Ley 2466 de 2025)
and after the night-work boundary moved to 19:00 (Ley 2466 de 2025 art. 10,
in force 25 Dec 2025).

The withholding engine reproduces the CO-CCG-001 Module 6.1 worked example
(salary 8,000,000 -> retencion 92,049.30) to the cent; see _calc_co.py.
"""

# --------------------------------------------------------------------------
# 2026 statutory parameters
# --------------------------------------------------------------------------
SMMLV = 1750905          # Decreto 1469 de 2025 art. 1
AUX_TRANSPORTE = 249095  # Decreto 1470 de 2025 (<= 2 SMMLV only)
UVT = 52374              # Resolucion DIAN 000238 de 15 Dec 2025
IBC_CEILING = 25 * SMMLV       # 43,772,625
FSP_TRIGGER = 4 * SMMLV        # 7,003,620
FSP_SUB_TRIGGER = 16 * SMMLV   # 28,014,480
EXO_1141_THRESHOLD = 10 * SMMLV  # 17,509,050 - ET art. 114-1 exoneration ceiling
HOUR_DIVISOR = 210             # from 15 Jul 2026

CURRENCY = "COP"

# --------------------------------------------------------------------------
# Sample employer / employee
# --------------------------------------------------------------------------
EMPLOYER = {
    "name": "Mercans Colombia S.A.S.",
    "nit": "NI 901.234.567-8",
    "address": "Calle 93B No. 17-25, Oficina 502, Chapinero, Bogota D.C., Colombia",
    "city": "Bogota D.C. (11 / 11001)",
    "arl": "Class I - minimum risk (0.522%) | CIIU 6201",
    "operator": "PILA operator: Aportes en Linea | Planilla type E",
    "cune": "a1f4c9e07b3d5286bb41c0e9d7f2a6c85b30e94d",
    "prefix": "NE 10250",
    "gendate": "31/08/2026",
    "person_type": "Legal person (J) - private (2) - income-tax filer",
}

EMPLOYEE = {
    "name": "Carlos Andres Mejia Restrepo",
    "doc": "CC 79.482.615 (13 - Cedula de ciudadania)",
    "code": "CO-000482",
    "position": "Senior Software Engineer",
    "department": "Technology / Engineering",
    "contract": "2 - Indefinite term (termino indefinido)",
    "hire": "01/03/2023",
    "service": "3 years 6 months",
    "worker_type": "01 - Dependiente / sub-type 00 - No aplica",
    "frequency": "5 - Monthly (mensual)",
    "eps": "EPS Sura S.A.",
    "afp": "Porvenir S.A. - RAIS",
    "cesantias": "Porvenir Cesantias (03) - Ley 50 de 1990, annual deposit",
    "ccf": "Compensar (Bogota D.C.)",
    "days_worked": "30 of 30 (commercial month)",
    "days_absent": "0 - no absence, no unpaid leave",
    "modality": "TT-SUP - Supplementary telework",
    "tax_status": "RES - Colombian tax resident | Procedure 1 (ET art. 385)",
    "payment": "42 - Consignacion bancaria | Contado",
}

PERIOD_START = "01/08/2026"
PERIOD_END = "31/08/2026"
PAY_DATE = "31/08/2026"

BANK = {
    "beneficiary": "Carlos Andres Mejia Restrepo",
    "bank": "Bancolombia S.A.",
    "acct_type": "AHORROS - Cuenta de ahorros",
    "acct_no": "123-456789-01",
}

# --------------------------------------------------------------------------
# Pay elements.  code / rate / unit / amount-or-None (None = Excel formula)
# --------------------------------------------------------------------------
HOUR_VALUE = 38095.24          # 8,000,000 / 210, rounded half-even
HED_RATE = 47619.05            # ordinary hour x 1.25 (CST art. 168)
RN_RATE = 13333.33             # ordinary hour x 0.35 (CST art. 168 par.)

EARNINGS = [
    # (wtc code, EN name, ES name, rate, unit, unit_fmt, amount)
    ("CO-SALARIO-BASICO", "Basic salary", "Salario basico",
     None, 30, 'DAYS', 8000000.00),
    ("CO-HED", "Day overtime (+25%)", "Hora extra diurna (25%)",
     HED_RATE, 6, 'HOURS', None),
    ("CO-RECARGO-NOCTURNO", "Night premium (35%, 19:00-06:00)",
     "Recargo nocturno (35%, 19:00-06:00)", RN_RATE, 10, 'HOURS', None),
    ("CO-COMISIONES", "Commissions", "Comisiones",
     None, None, None, 1200000.00),
    ("CO-BONIF-NOSALARIAL", "Extra-statutory bonus - non-salary (CST art. 128 pact)",
     "Bonificacion extralegal no salarial (pacto CST art. 128)",
     None, None, None, 500000.00),
    ("CO-AUX-TRANSPORTE", "Statutory transport allowance - not payable above 2 SMMLV",
     "Auxilio de transporte - no aplica por encima de 2 SMMLV",
     None, None, None, 0.00),
]

DEDUCTIONS = [
    # (code, EN, ES, rate label, formula-key)
    ("CO-DED-SALUD", "Health contribution - employee (EPS)",
     "Aporte a salud - empleado (EPS)", "4.00% of IBC", "IBC*0.04"),
    ("CO-DED-PENSION", "Mandatory pension contribution - employee (AFP)",
     "Aporte a pension obligatoria - empleado (AFP)", "4.00% of IBC", "IBC*0.04"),
    ("CO-DED-FSP-SOLIDARIDAD", "Solidarity pension fund - solidarity sub-account",
     "Fondo de Solidaridad Pensional - subcuenta de solidaridad",
     "1.00% of IBC (IBC >= 4 SMMLV)", "IBC*0.01"),
    ("CO-RETENCION-FUENTE", "Income tax withholding (retencion en la fuente)",
     "Retencion en la fuente sobre rentas de trabajo",
     "Marginal 19% (ET art. 383)", "TAX"),
    ("CO-DED-MEDICINA-PREPAGADA", "Prepaid health plan - employee share (authorised)",
     "Medicina prepagada - parte del empleado (autorizada)",
     "Written authorisation", 200000.00),
    ("CO-DED-LIBRANZA", "Payroll lending repayment (Ley 1527 de 2012)",
     "Libranza (Ley 1527 de 2012)", "Written authorisation", 350000.00),
]

EMPLOYER_CONTRIB = [
    ("CO-ER-SALUD", "Health contribution - employer (EPS)",
     "Aporte a salud - empleador (EPS)",
     "8.50% - EXONERATED (ET art. 114-1)", "ZERO"),
    ("CO-ER-PENSION", "Mandatory pension contribution - employer (AFP)",
     "Aporte a pension obligatoria - empleador (AFP)", "12.00% of IBC", "IBC*0.12"),
    ("CO-ER-ARL", "Occupational risk - ARL (Class I)",
     "Riesgos laborales - ARL (Clase I)", "0.522% of IBC", "IBC*0.00522"),
    ("CO-ER-CCF", "Family compensation fund - CCF",
     "Caja de Compensacion Familiar - CCF", "4.00% of levy base", "PARA*0.04"),
    ("CO-ER-SENA", "Apprenticeship training levy - SENA",
     "Aporte al SENA", "2.00% - EXONERATED (ET art. 114-1)", "ZERO"),
    ("CO-ER-ICBF", "Family welfare levy - ICBF",
     "Aporte al ICBF", "3.00% - EXONERATED (ET art. 114-1)", "ZERO"),
]

PROVISIONS = [
    ("CO-PROV-PRIMA", "Service bonus accrual (prima de servicios)",
     "Provision de prima de servicios", "1/12 (8.3333%) of benefit base", "PREST/12"),
    ("CO-PROV-CESANTIAS", "Severance-savings accrual (cesantias)",
     "Provision de cesantias", "1/12 (8.3333%) of benefit base", "PREST/12"),
    ("CO-PROV-INTERESES-CESANTIAS", "Interest on severance savings",
     "Provision de intereses a las cesantias",
     "12% per year (1.00% per month)", "PREST*0.01"),
    ("CO-PROV-VACACIONES", "Annual leave accrual (vacaciones)",
     "Provision de vacaciones",
     "15 working days / year (1/24 per month)", "VAC/24"),
]

LEAVE = [
    ("Annual leave - vacaciones (CST art. 186)",
     "Vacaciones (CST art. 186)", 52.50, 45.00,
     "15 working days per year of service; 3.5 years accrued to 31/08/2026"),
    ("Bereavement leave - licencia de luto (CST art. 57 num. 10)",
     "Licencia de luto (CST art. 57 num. 10)", 5.00, 0.00,
     "5 working days per event (Ley 1280 de 2009)"),
    ("Paternity leave (CST art. 236A, Ley 2114 de 2021)",
     "Licencia de paternidad (CST art. 236A, Ley 2114 de 2021)", 14.00, 0.00,
     "2 weeks per birth, funded by the EPS"),
    ("Statutory paid leave (CST art. 57 num. 6)",
     "Licencia remunerada legal (CST art. 57 num. 6)", 3.00, 1.00,
     "Employer policy - CST art. 57 num. 6 fixes no statutory duration"),
]

YTD = [
    ("YTD gross earnings (Jan-Aug 2026, incl. June service bonus)",
     "Total devengado acumulado (ene-ago 2026, incl. prima de junio)", 85761904.60),
    ("YTD employee social-security contributions (health + pension + FSP)",
     "Aportes del trabajador acumulados (salud + pension + FSP)", 6925714.56),
    ("YTD income tax withheld (retencion en la fuente)",
     "Retencion en la fuente acumulada", 2757994.32),
    ("YTD authorised voluntary deductions",
     "Deducciones voluntarias autorizadas acumuladas", 4400000.00),
    ("YTD net pay", "Neto pagado acumulado", 71678195.72),
]
