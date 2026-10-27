# -*- coding: utf-8 -*-
"""
Shared Sheet-3 Payroll Scope blocks for the Colombia report specifications.

WHO gets reported is very nearly identical across the six in-scope filings,
because Colombia keys every one of them to the same population - persons paid
under a Colombian employment or statutory relationship. WHAT gets reported
differs sharply, so the AMOUNTS block is provided per-filing and only the WHO
and TIMING blocks are shared.

Source: scope_manifest.json -> employment_types; CCG Modules 1, 4, 5, 6, 10.
"""

# --- WHO GETS REPORTED (shared verbatim by all six filings) ----------------
SCOPE_WHO = [
    "WHO GETS REPORTED",
    ("Indefinite-term employee (contrato a termino indefinido)", "YES",
     "The core private-sector population. CST art. 47; Ley 2466 de 2025 art. 5."),
    ("Fixed-term employee (contrato a termino fijo, max 4 years)", "YES",
     "Identical reporting treatment to an indefinite-term contract. CST art. 46; Ley 2466 de 2025 art. 6."),
    ("Specific-work or task employee (contrato por obra o labor)", "YES",
     "An employment contract; CST art. 46. Nomina electronica TipoContrato = 3 (Obra o Labor)."),
    ("Occasional / accidental / transitory worker (< 1 month, non-core activity)", "YES",
     "Still an employee under CST art. 6. Reported on every filing; the PILA planilla type and the "
     "day counts differ, not the obligation."),
    ("Part-time employee", "YES",
     "Colombia has no separate part-time regime. Reported normally; the PILA contribution base is "
     "floored at 1 SMMLV (COP 1,750,905) except for the worker type 51 partial-time regime."),
    ("All-inclusive salary employee (salario integral, >= 13 SMMLV)", "YES",
     "CST art. 132 num. 2. Reported with the integral-salary flag set; the contribution base is 70% "
     "of the integral salary, and the nomina electronica carries SalarioIntegral = true."),
    ("Apprentice (contrato de aprendizaje)", "YES",
     "Ley 2466 de 2025 art. 21 converted the apprenticeship into a special fixed-term LABOUR contract, "
     "regulated by Decreto 0223 of 5 March 2026. Nomina electronica TipoContrato = 4; PILA worker "
     "type 12 (lectiva) or 19 (productiva)."),
    ("Intern / practical placement (practicas o pasantias)", "YES",
     "Nomina electronica TipoContrato = 5. Reported where remunerated."),
    ("Teleworkers and remote workers", "YES",
     "Ley 1221 de 2008 as amended by Ley 2466 de 2025 arts. 52-54. No reporting difference; the "
     "nomina electronica carries a dedicated Teletrabajo devengado element (NIE158)."),
    ("Resident foreign national under a Colombian contract", "YES",
     "Full reporting. Withheld under the ET art. 383 progressive table once tax residence is acquired."),
    ("NON-RESIDENT foreign national under a Colombian contract", "YES",
     "IN SCOPE and frequently mis-configured. Withheld at the flat 20% of ET art. 408 on the GROSS, "
     "with no art. 388 depuration, until the 183-day residence test is met (DIAN Concepto 011108 of "
     "29 June 2026). See the resident / non-resident block in the Report Matrix."),
    ("Employed old-age pensioner in active service", "YES",
     "PILA worker sub-type 01; no pension contribution (PILA pension rate field = 0), health and the "
     "levies still apply."),
    ("Executive director / statutory legal representative holding an employment contract", "YES",
     "Reported as an ordinary employee where an employment contract exists."),
    ("Independent contractor (contrato de prestacion de servicios)", "NO",
     "Not an employee. The contractor self-files PILA on 40% of fees (planilla types I / Y, descoped) "
     "and is reported by the payer in the third-party information return, not in this employer filing. "
     "Withholding on their fees does pass through Formulario 350, but under a different casilla."),
    ("Public-sector employee (contributor type 47, SGP-funded entity)", "NO",
     "Public-sector only; PILA planilla types T and F are descoped in scope_manifest."),
    ("Non-executive director paid honorarios only (junta directiva)", "NO",
     "Not employment income. Reported by the payer as honorarios, not as rentas de trabajo of an employee."),
    ("Pensioner whose pension is paid by a fund, not by the employer", "NO",
     "The paying fund is the withholding agent and the reporting party, not the employer."),
]

# --- TIMING AND RELATIONSHIP (shared) --------------------------------------
SCOPE_TIMING = [
    "TIMING AND RELATIONSHIP",
    ("Reported on the accrual (causacion) date", "NO",
     "Every Colombian payroll filing is keyed to the PAYMENT or credit-in-account date, not to the "
     "accrual date. A December salary paid in January falls in the January filing."),
    ("Reported on the payment or credit-in-account date", "YES",
     "The universal Colombian rule - pago o abono en cuenta. Applies to the nomina electronica "
     "(Res. DIAN 000013 de 2021 art. 3), to Formulario 350, to Formulario 220 and to Formato 2276."),
    ("A semi-monthly payroll produces two filings a month", "NO",
     "It does not. The nomina electronica is expressly ONE monthly document per employee "
     "'irrespective of whether the obliged party makes payments in different or shorter periods' "
     "(art. 3). PILA and Formulario 350 are likewise monthly."),
    ("Nil period still filed", "VARIES",
     "Formulario 350: NOT required where no operation subject to withholding occurred in the period "
     "(ET art. 606 par. 2). Nomina electronica: no document where there was no payment. PILA: a "
     "planilla is still required while the employment relationship subsists."),
    ("Corrections handled by re-filing the whole period", "VARIES",
     "Nomina electronica: NO - a dedicated adjustment note (NominaIndividualDeAjuste, Reemplazar or "
     "Eliminar) referencing the original CUNE. Formulario 350: yes, a corrective return. PILA: a "
     "planilla type N (correcciones) or M (mora)."),
]
