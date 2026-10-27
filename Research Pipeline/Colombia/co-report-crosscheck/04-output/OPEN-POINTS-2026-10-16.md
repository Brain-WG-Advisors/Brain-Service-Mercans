# Open points after the 16 Oct 2026 rules - internal control (not for the development team)

What stays open: (1) questions to the client (via Cinthya); (2) configuration points the 16 Oct rules left open, including Form 220 casilla 56 (employer contributions to institutional plans); (3) items removed from the specs in the third pass because no rule exists; appendix: RA / compliance queries of the specs the 16 Oct rules did not address (PILA, cesantías), to be confirmed as closed or kept. The full column T/U export of the v1.1 drafts is kept in OPEN-POINTS-2026-10-16-draft-export.md.

## 1. Questions to the client (via Cinthya)

### CO-PILA-003 (PILA)
- **T2R2-003 (row 65)**: Query (15 Oct 2026): client to confirm the PILA document type behind the Master Data columns 'National ID' and 'Identity Card' and the precedence rule where more than one document column is populated (14 of 261 employees in Sept-2026).
- **T2R2-005 (row 67)**: Query (15 Oct 2026): client to confirm whether the 20 interns of Employee Group 6 / Subgroup E2 (paid WT 62149, no contributions in Sept-2026) are reported in PILA and under which tipo cotizante, and to supply the Employee Group / Subgroup to tipo cotizante mapping table.
- **T2R2-006 (row 68)**: Client to confirm whether these employees are active pensioners (sub-type 1, pension rate 0 per AT2 v30) or whether the date is a defaulted value; also to explain Master Data 'Regime' = AReg (8 employees).

### CO-DIAN-001 (Nómina Electrónica)
- **NIE041 (row 53)**: Client to provide the mapping Employee Group/Subgroup -> TipoTrabajador (in particular Group 6 / Subgroup E2 interns: 12, 19 or other). Client to explain why only 6 of the 20 Group 6 / E2 interns are coded 19 / contract 4 in the current electronic payroll file while the other 14 are coded 01 / contract 2 and still receive ApoyoSost.
- **NIE042 (row 54)**: Client to confirm what Master Data 'Pensioner Effective Date' means for the 2 employees carrying it: the date equals their Hire Date and Adjusted Service Date (18-11-2025 / 02-12-2025) and both still pay the 4% pension (WT 2556) in Sep-2026, so it is not evidenced as an old-age-pension recognition date.
- **NIE044 (row 56)**: Client to confirm (a) the DIAN code for Master Data columns 'Identity Card' and 'National ID' and (b) the precedence when an employee has more than one document column filled.
- **NIE061 (row 67)**: Client to provide the contract term per employee (table 5.5.2), and confirm whether the INKOMPASS interns hold apprenticeship contracts (4) or internships (5). Client to name the field or table that feeds TipoContrato (2 / 4) in the current electronic payroll file.
- **NIE062 (row 68)**: Client to confirm Master Data 'Basic Salary' as the source of the contractual salary (Sueldo) and to explain the 4 integral employees in Sep-2026 whose G2N 'Salary Assigned' differs from it (2 with Basic Salary 0 in Master Data; 2 with Salary Assigned exactly twice the Basic Salary). Client to explain (a) Sueldo 0.00 for the 20 interns in the current electronic payroll file and what Sueldo must carry for an apprentice, and (b) the 2 integral employees reported with twice their G2N 'Salary Assigned'.
- **NIE065 (row 72)**: Client to confirm whether bank salary payments are reported as 42 or 45. The 15 Oct mapping (Bank 42/45, Cash 10) stays; client to confirm the code for bank salary payments (42, 45 or 47) and RA to confirm which Metodo (and whether bank details) a zero-net document carries.
- **NIE002 (row 78)**: Client to confirm whether FechaIngreso is 'Hire Date', 'Original Hire Date' or 'Adjusted Service Date' for rehired/transferred employees.
- **NIE069 (row 85)**: Client to name a payroll counter that carries the days worked net of vacation/leave for DiasTrabajados, or confirm the computation 30 minus the Leave Absence Report days of the month (Accumulated WT 63812 is a gross count: 30 for all employees on vacation in Sep-2026). Client to confirm that 'Days Worked' is also reduced by unpaid leave / suspension.
- **NIE070 (row 86)**: Client to confirm where salary arrears (WT 62101 / 62141) are reported: SueldoTrabajado of the payment month, or another element.
- **NIE071 (row 87)**: Client to confirm the salary character (salary or non-salary) agreed in the collective agreement for WT 62523 'Transportation Allowance CLA- 2008', which decides whether it is reported in AuxilioS (NIE141) or AuxilioNS (NIE142).
- **NIE108 (row 125)**: Client to confirm what WT 62845 'Night, Sunday or holiday surcharge' covers (HRNDF code 7, HRDDF code 5, or both).
- **NIE117 (row 133)**: Client to explain the difference between Accumulated WT 63811 and WT 42961 (both 'Worked Days In Semester'; 63811 resets each semester, 42961 does not) and confirm which one, if either, is net of unpaid leave for Primas - Cantidad.
- **NIE119 (row 135)**: Client to confirm the salary character of WTs 62204, 62208, 62209, 62210 and whether they are reported as Primas (PagoNS) or Bonificacion.
- **NIE127 (row 144)**: Client to confirm this as its election.
- **NIE146 (row 164)**: Client to confirm the NE treatment of expatriate WTs 65821, 1910 (and the deduction-side 1204 / 21126) - catch-all OtroConcepto/OtraDeduccion, or excluded as shadow-payroll items. Evidence: the current electronic payroll file reports 65821 as OtroConcepto NS and leaves 1910, 67010 and 62216 out; client to confirm, together with the zero-amount stock-award lines.
- **NIE194 (row 175)**: Client to confirm that WT 61100/62838 are salary advances and WT 21215 'Legalization Salary Payment' is their recovery.
- **NIE164 (row 185)**: Client to confirm what the date means and whether it marks a recognised old-age pension; the spec rule (0.00 for sub-type 01) stays until then.
- **NIE167 (row 187)**: Client to explain the base of WT 2553 'Solidarity Pension Fund' for the 7 employees whose Sep-2026 amount exceeds 2% of WT 64990 (arrears or another base), so that the solidarity / subsistence split (NIE167-NIE170) can be reconciled to 2553.
- **NIE177 (row 191)**: Client to confirm which WTs are real withholding remitted to DIAN: 2552, 21330 'Theoretical' (6 employees, 5 of them Employment Status 'D'), 21129, 25832, 25833. On 'CONTINGENT WITHHOLDING' (20 employees, all with AFC/APV, equal to 'WITHOUT CONTRIBUTION' minus 'WITH CONTRIBUTION'): it appears to be the contingent withholding of ET art. 126-1 / 126-4 on early withdrawal (inference); client to confirm it is not withheld this month and is excluded from RetencionFuente.
- **NIE171 (row 195)**: Client to provide the statutory rate per union WT (21550, 21552, 21560, 21562, 21670, 21680), and confirm whether WT 21803 'Deduct. Client to confirm the combined union rate 1.50% used in the current electronic payroll file and how it splits between WTs 21550, 21680 and the sectional WT.
- **NIE196 (row 202)**: Client to state what each WT 21215 'Legalization Salary Payment' line legalises (advance recovery, off-cycle payment or loan refinancing); only advance recoveries are reported in Anticipo (NIE196).
- **NIE013 (row 26)**: Client to confirm that the 6 documents with Pais (NIE013) = CR, CA, DO, CH or MX in the current electronic payroll file are an error and that the generation country is CO.
- **NIE213 (row 45)**: Client/provider to confirm the meaning of the EMI record position after the four natural-person name positions: it repeats the corporate name on all 261 documents and, by XSD attribute order, would be Empleador/@OtrosNombres, which must stay empty for a legal-person employer.
- **NIE050 (row 62)**: Client to confirm that the 6 non-CO LugarTrabajoPais values in the current electronic payroll file are home-address countries and that these employees work in Colombia.
- **NIE051 (row 63)**: Client to confirm why the current electronic payroll file reports the employer's municipality (05 / 05001) as place of work for every employee, and to approve the 'Work location' -> DIVIPOLA table.
- **NIE053 (row 65)**: Client to confirm that LugarTrabajoDireccion in the current electronic payroll file is the employee's home address (= Master Data 'Address Line 1' for 261 of 261) and to provide the address of each work location.
- **NIE056 (row 66)**: Client to explain why 43 employees paid WT 62140 'Integral Salary' (contributions on 70% of salary) are reported with SalarioIntegral = false in the current electronic payroll file.
- **NIE203 (row 76)**: Client validation note (ConsolidadoCCT; a single free-text cell, not tied to an identified payment): an off-cycle payment of the month 'stays in the accumulators but it is OK not to report it in the e-payroll'; the current file carries one FechaPago (2026-09-22) on all 261 documents.
- **NIE072 (row 88)**: Client to confirm whether per-diem WTs 62805-62810, 62820 and 62821 are permanent (salary, NIE072) or accidental (non-salary, NIE073) per diems; the current file reports all of them as salary.
- **NIE082 (row 99)**: Client to provide a month with overtime so that the percentage (75.00 for HEN, annex table 5.5.5) can be checked.
- **NIE116 (row 132)**: Client to confirm that vacation paid in cash on termination is reported here.
- **NIE118 (row 134)**: Client to give the description of WT 62831, which its wage-type table assigns to Primas - Pago together with WT 62211.
- **NIE141 (row 162)**: Client to confirm that WT 62133 'Variable' belongs in AuxilioS (current file) rather than BonificacionS.
- **NIE157 (row 177)**: Client to confirm the worker type (12 or 19) and contract type (4) of all 20 INKOMPASS interns; the current electronic payroll file codes 14 of them as 01 / 2.
- **NIE159 (row 179)**: Client to confirm the nature of WT 62203 'Reconciliations PMI additionall payment' (client table: BonifRetiro; spec NIE146: OtroConcepto candidate).
- **NIE182 (row 206)**: Client to confirm which product WTs 21610, 21611 and 21612 ('Private Health Insurance' Colsanitas / Sura, 135 documents in Sep-2026) are: prepaid medicine, a complementary health plan or a health insurance policy are reported in PlanComplementarios; other insurance products in OtrasDeducciones.
- **NIE187 (row 212)**: Client to confirm that the totals will be the sums of the elements reported (the current file uses G2N Gross / Total Deductions and excludes the informative pairs), and how WTs 62202, 1910, 67010 and 65821 are treated.
- **NIE189 (row 214)**: Client to explain why ComprobanteTotal in the current file adds back WT 21215 for 34 employees and is 0.00 for the 6 expatriates;

### CO-DIAN-004 (Formulario 220)
- **casilla 24 (row 13)**: Confirm with the client the mapping of the employee master document columns to the casilla-24 codes: 'Citizenship Card ID' -> 13 and 'Indentity Card for Foreigners' -> 22 are the evident candidates; 'National ID' and 'Identity Card' have no evident code (they appear next to a Citizenship Card for Colombian nationals).
- **casilla 25 (row 14)**: Confirm with the client the identification source (document type, document number and split names) for the 777 Accumulated Report payees without an employee-master row (491 pension payees of 62154 and 286 others, 132 of them paid salary in September 2026).
- **casilla 30 (row 20)**: Confirm with the client which start date feeds casilla 30 for an employee who joined during the tax year: 'Hire Date', 'Original Hire Date' (differs from 'Hire Date' for 40 of 261 employees) or 'Adjusted Service Date'.

### CO-DIAN-005 (Formato 2276)
- **N02 (row 5)**: Client to confirm the mapping of each master-data document column (Citizenship Card ID, Indentity Card for Foreigners, Identity Card, National ID) to the DIAN document-type code and the priority rule where more than one column is filled (14 of 261 rows), and to provide the identity of the 8 persons paid in the year who have no identification number in any mapped report.
- **N04 (row 7)**: Client to confirm the source of the DIVIPOLA municipality code, since the reports hold only a letter department code and a free-text city.
- **N08 (row 12)**: Client to confirm that 65818 is a payment to a third-party food supplier (the ET art. 387-1 condition) and which wage type feeds the 41-UVT split.
- **N19 (row 24)**: Client to confirm which of the two mirror wage types 'Payment Severance Funds Inf.' (25827 / 65805, identical totals, booked only in February) is the source, so that the deposit is counted once.
- **N25 (row 32)**: Client to classify each voluntary-pension wage type as RAIS voluntary (ET art. 55, numeral 25) or voluntary pension fund (ET art. 126-1, numeral 26): 25811, 25812, 25813, 25814, 25815, 25823 (FVOL) and 25820, 25821, 21210, 21211, 65803, 65804 (Plan Institucional PROTECCION).
- **N27 (row 34)**: Client to explain the one September employee whose AFC column in the withholding working report (2,661,343) differs from the AFC wage type (4,300,000).

### CO-CESANTIAS-006 (Consignación de cesantías)
- **T03 (row 18)**: RA / client to confirm the mapping of the Master Data identity columns to the T03 codes ('Citizenship Card ID' -> CC and 'Indentity Card for Foreigners' -> CE are inferred; 'Identity Card' and 'National ID' are undetermined) and how the 14 employees with more than one column filled and the 2 with none are to be typed.
- **T09 (row 25)**: Client to provide the list of 'Severance Fund Name' values with the operator fund code (02/03/10/15/19) for each, and to explain the 63 employees with a blank fund, 12 of whom received a February-2026 deposit (WT 25827) - to which fund was that deposit made?
- **T14 (row 30)**: Client to explain one employee who left in early 2026 (identified in the cross-check evidence file CO-CESANTIAS-006-verification.json): January |WT 63814| = 4,413,519, no WT 25827 deposit, no WT 62126, and the February WT 62110 of 935,967 equals only the 2026 accruals - the 2025 balance is not evidenced as deposited or paid in the Accumulated Report.

## 2. Configuration points left open by the 16 Oct rules

### CO-DIAN-002 (Formulario 350)
- Formulario 350 Spec!M37 (142): the rule names the sheet-2 concept (5 without treaty, 24 with treaty), which the cell already states; the source conflict on the casilla numbering in Res. 000227/2025 art. 1.2.2.26 is not a rule and is not in the cell - no change.

### CO-DIAN-005 (Formato 2276)
- Formato 2276 Spec!L7 (N04 System Mapping): kept as Employee.Department_Code + Employee.Municipality_Code; the address and country sub-fields are described in M7 as coming from the employee address record, no new mapping name is introduced.

## 3. Items removed from the specs on 16 Oct 2026 (no defined rule) - owner in brackets

### CO-PILA-003 (PILA)
- [RA] Payroll Scope Summary!C12 (-): Which PILA contributor type (campo 5) is reported for an apprentice in the productive phase of a Ley 2466 de 2025 art. 21 apprenticeship contract, given that AT2 v30 names code 19 for the lectiva phase only?
- [RA] Field Options!D99 (-): Which PILA contributor type (campo 5) is reported for an apprentice in the productive phase of a Ley 2466 de 2025 art. 21 apprenticeship contract, given that AT2 v30 names code 19 for the lectiva phase only?
- [RA] PILA Spec!M107 (T2R2-041): Under which condition is V (salario variable) reported in campo 41 instead of F - which contract attribute or pay composition makes the salary variable for PILA purposes?
- [RA] PILA Spec!M108 (T2R2-042): For an integral salary, is the Ley 1393 de 2010 art. 30 40% non-salary test run on the full integral salary or on its 70% base, and is the excess added in full on top of the 70% base?
- [RA] PILA Spec!M110 (T2R2-044): How do general-illness incapacity (IGE) days enter the occupational-risk contribution base (campo 44) and the occupational-risk day count (campo 38)?
- [RA] Population Rules!D21 (-): Where an employee changes work centre mid-period (VCT) and the risk class changes, is the period settled at one ARL rate or split between the two work centres?

### CO-DIAN-001 (Nómina Electrónica)
- [RA] Nomina Electronica Spec!M57 (NIE045): Which value is emitted in NumeroDocumento (NIE045) for an employee whose identity document number contains letters or leading zeros (document types 21, 41, 42, 50), given that XSD v1.0.6 types the attribute as xsd:integer and DIAN has published no workaround?
- [client] Nomina Electronica Spec!M133 (NIE117): Is WT 63811 'Worked Days In Semester' net of unpaid-leave and suspension days (licencia no remunerada), so that it can be reported as the days on which the service bonus is computed without further adjustment?
- [RA] Nomina Electronica Spec!M202 (NIE196): Which deduction element carries a WT 21215 'Legalization Salary Payment' line that legalises an off-cycle payment already made (a line that neither recovers an advance of wage types 61100 / 61101 / 61150 / 61200 / 62838 nor is matched by WT 67090)?

### CO-DIAN-002 (Formulario 350)
- [RA] Formulario 350 Spec!M53 (79-92 / 95-108): For fees paid to resident natural persons, which fees are declared in casillas 77 / 93 (withheld under the ET art. 383 table, art. 383 para. 2 as amended by Law 2277 of 2022 art. 8) and which in casillas 79 / 95 (withheld at the ET art. 392 rates), under the 2024 Form 350 instruction guide?
- [RA] Population Rules!D4 (Casilla 77 - base employment income): For fees paid to resident natural persons, which fees are declared in casillas 77 / 93 (withheld under the ET art. 383 table, art. 383 para. 2 as amended by Law 2277 of 2022 art. 8) and which in casillas 79 / 95 (withheld at the ET art. 392 rates), under the 2024 Form 350 instruction guide?

### CO-DIAN-004 (Formulario 220)
- [client] Formulario 220 Spec!M13 (24): Which admitted document of the Form 220 list (21 Tarjeta de extranjeria, 22 Cedula de extranjeria or 41 Pasaporte) does each foreign employee who holds a PEP or a PPT hold, so that casillas 24 and 25 can be certified with it?
- [RA] Formulario 220 Spec!M48 (56): Are the employer's institutional-plan contributions (Plan Institucional PROTECCION, deduction wage types 21210 / 21211 and 25820 / 25821 Plan Institucional PROTECCION - IC Bonus) certified in casilla 56 as voluntary contributions to a voluntary pension fund under ET art. 126-1?
- [RA] Formulario 220 Spec!M37 (46): Is the earning side of the employer's institutional-plan contributions (65803 Plan Institucional PROTECCION - Payment- 6785 and 65804 Plan Institucional PROTECCION - IC Bonus) certified as income of the employee on Form 220 and, if so, in casilla 36 or casilla 46?

### CO-DIAN-005 (Formato 2276)
- [client] Formato 2276 Spec!M5 (N02): Which admitted DIAN document type (21 tarjeta de extranjeria, 22 cedula de extranjeria, 41 pasaporte or another code of the 'Tipo de documento' table) does each foreign employee hold, so that the 'Identity Card for Foreigners' and 'National ID' master-data columns can be mapped in the document-type configuration table?
- [RA] Formato 2276 Spec!M33 (N26): Are employer-side contributions to institutional voluntary-pension plans (the institutional-plan wage types 25820, 25821, 21210, 21211, 65803 and 65804 where they carry the employer-side attribute) reported in Formato 2276 numeral 26 and Form 220 casilla 56, or excluded from both?

### CO-CESANTIAS-006 (Consignación de cesantías)
- [RA] Consignacion Cesantias Spec!M32 (T15): For an affiliate whose residence is abroad (Master Data field 'Country' other than CO), what do the funds and the information operator accept in T15 (free-text address), T16 (DANE department) and T17 (DANE municipality), given that a foreign address has no DANE code and the three fields must describe one place?
- [RA] Consignacion Cesantias Spec!M35 (T18): For a landline held in the 10-digit national numbering format (60 + area code + seven-digit subscriber number), do the funds and the information operator expect the seven-digit subscriber number in T18, or is the field zero-filled unless a seven-digit number is held?
- [client] Consignacion Cesantias Spec!M37 (T20): For an employee transferred within the group, is the transfer executed as a termination and a new contract (T20 = hire date of the new contract, prior cesantias settled in the final settlement) or as an employer substitution with contract continuity (T20 = original hire date), and which of the two dates does the fund expect?

## Appendix. RA / compliance queries not covered by the 16 Oct rules (PILA, cesantías) - confirm closed or keep

### CO-PILA-003 (PILA)
- **T2R2-023 (row 86)**: Query (15 Oct 2026): RA to confirm the annex definition of VST and the PMI wage types that trigger it (46 of 241 employees had an IBC Total above their Salary Value in Sept-2026 because of WTs 62133, 62150, 62207 or vacation days valued in the base).
- **T2R2-027 (row 90)**: Query (15 Oct 2026): RA to confirm whether vacation compensated in cash (PMI WT 79003, no rest period; 2 of 7 Sept-2026 rows have a blank Date To) raises VAC-LR, or is excluded from the flag and its date pair.
- **T2R2-041 (row 107)**: Query (15 Oct 2026): RA to confirm how V (salario variable) is determined for PMI, since Master Data has no salary-type field and the explanation derives only X (WT 62140) and F (WT 62100).
- **T2R2-042 (row 108)**: Query (15 Oct 2026): RA to confirm that, for an integral salary, the Ley 1393 de 2010 art. 30 40% test is run on the full integral salary and the excess is added at 100% on top of the 70% base - observed in the client's Sept-2026 IBC Total, not a confirmed instruction.
- **T2R2-044 (row 110)**: Query (15 Oct 2026): RA to confirm how IGE, LMA and VAC-LR days enter the ARL base (T2R2-044) and the ARL day count (T2R2-038); the client charges ARL (WT 2560) on the same base as pension and health, including sick-leave and vacation days.

### CO-CESANTIAS-006 (Consignación de cesantías)
- **T15 (row 32)**: RA to confirm what the fund expects in T15, T16 and T17 for an affiliate whose residence is abroad (6 employees with a non-CO 'Country' in Master Data: CA, CR, DO, CH, MX), given that a foreign address has no DANE department or municipality code.
- **T18 (row 35)**: RA to confirm how a landline held in the current 10-digit national numbering format is to be reduced to the 7 positions of T18, and whether the field may be zero-filled for the whole population when only a mobile number is held.
- **T20 (row 37)**: RA to confirm which date the fund expects in T20 for an employee transferred within the group or rehired - the current-contract 'Hire Date' or the recognised-seniority 'Adjusted Service Date' (the two differ for 21 of 261 employees).


Totals: client 57 (section 1 + section 3 client items), RA 23 (section 3 RA items + appendix), configuration notes 2.