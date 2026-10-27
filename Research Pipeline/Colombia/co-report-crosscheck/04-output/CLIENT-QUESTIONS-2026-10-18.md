Subject: PMI Colombia - open questions on the 16 Oct files (statutory report specs)

Hi Cinthya, Hi Heidy,

Thank you for the 16 Oct files and for the list of the September payroll runs. They closed several points: the September withholding reconciles to the Accumulated Report for the monthly and weekly groups, WT 21610-21612 are prepaid medicine (PlanComplementarios, as the spec states), the filed Formulario 350 and the DIAN validation responses of the electronic payroll stay with you, there is no PILA flat file (contributions are settled in Mi Planilla) and the cesantías deposit is made in the Aportes en Línea portal (balance at 31 December less the January advances). Below is what is still open. Please answer with wage-type codes, field names and counts only - no employee data.

**Payroll runs and withholding (Formulario 350)**
1. Please send the gross-to-net and the Base of Withholding of the CO - Retirees run REF-P199-994 (2026-09-04, 21 payees). It is the only run that can carry the pension withholding WT 21140 we see on 13 pensioners in September; the CO - Pensionaries run REF-P201-184 has no withholding column.
2. Please send the gross-to-net of the runs we do not have, so that the September withholding of 4 employees (WT 2552, with WT 62116 / 62110 / 62203 / 62115 on them - settlement and off-cycle payments) can be placed in its run: REF-P199-263, REF-P199-250, REF-P199-836, REF-P200-455, REF-P201-209, REF-P199-776, REF-P200-272 and REF-P199-483.
3. Weekly group: the Base of Withholding we have (report id REF-P201-216, 132 employees, generated 2026-09-18) equals the whole September withholding of those employees. Is WT 2552 deducted only in the last weekly run of the month (REF-P201-332), or in each of the four weekly runs (REF-P199-307, REF-P199-846, REF-P200-438, REF-P201-332)? If in each, please send the gross-to-net of the four runs.
4. For the runs dated 2026-08-31 (REF-P199-263, REF-P199-250, REF-P199-307): were they paid on 31 August or in September? The withholding is declared in the month of payment.
5. Contingent withholding: the Base of Withholding carries a 'CONTINGENT WITHHOLDING' column (ET arts. 126-1 / 126-4; 20 employees in the monthly group in September). Is this the contingent withholding report you mentioned, or is there a separate report? We treat it as outside Formulario 350.

**Formato 2276 (the file received is the complete tax year 2025, not a 2026 extract)**
6. Please confirm the file is the Formato 2276 of tax year 2025, and whether DIAN accepted it as sent: every amount is rounded to thousands and 50 pensioner records have no first name (the XSD requires it).
7. Meal allowance (WT 65818, with deduction WT 21115): is it paid through vouchers / cards or to a food supplier? Why are numerals 8 and 32 zero for every employee (the ET art. 387-1 split at 41 UVT per month and the 310 UVT threshold)?
8. Numeral 33 (six-month average income): it is populated for 52 employees without any severance paid or deposited and left empty for 5 employees with severance. On what basis is it populated, and how is the average computed (which wage types, last six months on termination)?
9. Municipality code 25/001 appears on 31 records (29 active employees): real location or a default value?
10. First name missing on 50 pensioner records: incomplete pensioner master data, or records keyed to an estate / entity?
11. Numerals 25 vs 26: please confirm that every '(FVOL)' wage type and every institutional-plan wage type (25811-25815, 25823, 25820, 25821, 21210, 21211, 65803, 65804) is an ET art. 126-1 voluntary-pension contribution; the file reports all of them in numeral 26.

**Cesantías**
12. Please confirm that the January advances deducted from the deposit (WT 62126 'Advance Severance Last Year') are the authorised cases only - housing or education (Ley 50/1990 art. 102; CST art. 256).

**Terminations (two final settlements and the October run REF-P203-119)**
13. Which HR or payroll field holds the termination date? Master Data has no termination-date column and the gross-to-net 'Effective Leaving Date' is blank even on the settlement run; only the manual settlement form carries it. It feeds Form 220 casilla 31, PILA campo 81 and the electronic payroll FechaRetiro.
14. For the employee who left on 15 September: PILA and the electronic payroll of September carried 30 days and no RET / FechaRetiro. Was a correction return filed, and was the full September salary recovered in the settlement?
15. Form 220: which line do you use for cesantías paid directly (WT 62110, 62117, 62126, 62127 have no line in your 'Renglon CIR' table) and for the dismissal indemnity (WT 62181, also unassigned)? And why are WT 79403, 62137 and 62150 assigned to the salary line?
16. Vacation days paid on termination are fractional (e.g. 47.75 days): how does the current provider report VacacionesCompensadas / Cantidad in the electronic payroll?
17. WT 62116 and 79403 are flagged 'Parafiscales' in your wage-type table, while the October settlement run shows zero employer contributions on them. Which one is right?
18. Settlement file 1 computes a 'Prima de vacaciones en liquidación de contrato' (133.7 days) that appears neither in the settlement nor in the October run. Was it paid elsewhere?

**Still open from the earlier requests**
19. WT 62151 'Retirement Payment - PRV': a pension or a one-off payment to retirees?
20. WT 62839: what is it and how is it paid?
21. Electronic payroll files of the other pay groups (weekly, pensioners, retirees) for September 2026 - we only have the monthly group.

Thanks a lot,
Wallisson
