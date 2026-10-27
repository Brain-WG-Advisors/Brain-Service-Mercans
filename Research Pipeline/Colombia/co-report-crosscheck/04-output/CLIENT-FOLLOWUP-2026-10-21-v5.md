Reply in the 'PMI Review' thread (Reply all). Replaces v4 (21 Oct 2026, Wallisson's approval). v5.1: 'as you pointed out on 14 Oct' removed - no e-mail or record of a BAU finding of 14 Oct was found (only a HANDOFF line from the Mac conversation). Earlier v5 changes: pensioners line removed (the rule is in the CCG v1.3, not in the specs, and the CCG is not on Drive yet; retirees as client inputs was not applied anywhere); Q14 refund route replaced by the AT2 rule (no primary source read for 'requested from each administradora').

Hi Heidy, Hi Cinthya,

Thank you for the answers of 21 Oct and for the Conceptos CIR 2025 file. They are now reflected in the Colombia specifications:

- Termination date: taken from the system Termination record (electronic payroll, PILA and Form 220).
- Six-month average (Formato 2276 numeral 33 / Form 220 casilla 59): computed as you described, per DIAN Concepto 4443 de 2025.
- Voluntary pension (Formato 2276 numeral 26 / Form 220 casilla 56): only the amount deducted from the employee.
- Res. DIAN 000013 de 2021: citations updated to Res. 000227 de 2025 in the electronic payroll specification and the SIR.

Three points from your answers, for your information:
- Fractional vacation days (Q16): the DIAN XSD defines VacacionesCompensadas / Cantidad as an integer (xsd:integer), so a value such as 47.75 is rejected.
- Late terminations (Q14): a type N return can add an omitted RET only for the same period and when the corrected values are equal to or higher than the original ones, and it cannot be used for a correction that leads to a refund (PILA Anexo Técnico 2, v30).
- Parafiscales on vacation (Q17): vacation paid in cash, also on termination, is part of the CCF / SENA / ICBF base (Ley 21 de 1982 art. 17; Consejo de Estado, Sala de Consulta 2027 de 2010), while it is not part of the health and pension base.

On the electronic payroll files: please put the 871 September files in one zip file in a Google Drive folder shared with me. The folder 'September 2026 Payroll Validation Files' from your 21 Oct e-mail shows 'You need access' for my account; could you share it?

Thanks a lot,
Wallisson
