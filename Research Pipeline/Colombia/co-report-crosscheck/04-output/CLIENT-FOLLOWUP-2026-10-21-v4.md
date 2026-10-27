Reply in the 'PMI Review' thread (Reply all). Replaces v3 (approved by Wallisson on 21 Oct 2026: only what was done with the BAU answers and what BAU presented / asked; the scope question to Manju / Andy goes in a separate message).

Hi Heidy, Hi Cinthya,

Thank you for the answers of 21 Oct and for the Conceptos CIR 2025 file. They are now reflected in the Colombia specifications:

- Termination date: taken from the system Termination record (electronic payroll, PILA and Form 220).
- Six-month average (Formato 2276 numeral 33 / Form 220 casilla 59): computed as you described, per DIAN Concepto 4443 de 2025.
- Voluntary pension (Formato 2276 numeral 26 / Form 220 casilla 56): only the amount deducted from the employee.
- Pensioners: health contribution 4% / 10% / 12% by pension band (Ley 100 art. 204 par. 5); retirees' amounts and withholding taken as client inputs.
- Res. DIAN 000013 de 2021: citations updated to Res. 000227 de 2025 in the electronic payroll specification and the SIR, as you pointed out on 14 Oct.

Three points from your answers, for your information:
- Fractional vacation days (Q16): the DIAN XSD defines VacacionesCompensadas / Cantidad as an integer (xsd:integer), so a value such as 47.75 is rejected.
- Late terminations (Q14): a type N return can add an omitted RET only for the same period and when the corrected values are equal to or higher than the original ones; where days or IBC go down, the excess is requested from each administradora (PILA Anexo Técnico 2, v30).
- Parafiscales on vacation (Q17): vacation paid in cash, also on termination, is part of the CCF / SENA / ICBF base (Ley 21 de 1982 art. 17; Consejo de Estado, Sala de Consulta 2027 de 2010), while it is not part of the health and pension base.

On the electronic payroll files: please put the 871 September files in one zip file in a Google Drive folder shared with me. The folder 'September 2026 Payroll Validation Files' from your 21 Oct e-mail shows 'You need access' for my account; could you share it?

Thanks a lot,
Wallisson
