Colombia (PMI) report specs - corrections applied on 15 Oct 2026 (6 DRAFTs v1.1 in 02-specs-out)

Basis: cross-check of the 6 specs against 18 client reports (round 1) and 4 new files (round 2: client's Form 220 working file, monthly gross-to-net, Nómina Electrónica document file and the client's NE validation/mapping), each with an independent verification pass. No spec in 01-specs was touched; no spec is approved. Version Control (VC) counts below are entries dated 2026-10-15; "administrative" = the one entry per spec about section-header cells converted from formulas to text.

CO-PILA-003 (PILA) - 26 VC entries (25 substantive)
- T2R1-020 total payroll value = sum of campo 45 (IBC CCF) per AT2 v30; System Mapping, Example Analysis, Population Rules and Sample File corrected from campo 95.
- IBC CCF (T2R2-045/065) has no 25 SMMLV ceiling: base = monthly salary payroll (Ley 21/1982 art. 17), 70% for integral salary (Ley 789/2002 art. 49); ceiling kept only for pension, health and ARL (Example Analysis D21).
- Art. 114-1 exoneration (T2R2-076/043) restated: total earnings of the month < 10 SMMLV (Decreto 1828/2013 art. 7) and N whenever campo 43 >= 10 SMMLV.
- T2R2-057 to 060 (IGE/LMA authorisations and values) always blank/zero under AT2 v30; Population Rules aligned.
- Client sources written into the explanations: document type/number from the four Master Data document columns and join on type + number; contributor type via a client-confirmed Employee Group mapping; work location needs a DIVIPOLA table; AFP/EPS held as names, code tables required; IBC computation order (70% integral, Ley 1393 add-back, floor/ceiling, round up to the peso); single FSP wage type 2553 to be split into solidarity and subsistence; contribution amounts recomputed and rounded up to the next 100, not copied from payroll; absence dates DD-MM-YYYY to AAAA-MM-DD and split incapacity rows merged; risk class normalised to 1-5.
- 19 amount fields had 12-position examples against a 9-position length; examples corrected.

CO-DIAN-001 (Nómina Electrónica) - 102 VC entries (101 substantive; 49 fields corrected in round 1, 52 in round 2 against the client's real NE file)
- Transport allowance: AuxilioTransporte only up to 2 SMMLV (Ley 15/1959); the collective-agreement allowance WT 62523 above that goes to AuxilioS/AuxilioNS.
- Days worked (NIE069) re-opened: DiasTrabajados = monthly G2N "Days Worked" (261/261), replacing the "30 minus leave days" fallback.
- Complementary health plan rule (NIE182): prepaid medicine, complementary plan or health policy -> PlanComplementarios; other insurance -> OtrasDeducciones.
- Totals (NIE187-189): ComprobanteTotal = cash net paid; the client's file takes totals from G2N groupings, excludes informative pairs and adds back WT 21215, which the spec must not replicate; TOT order confirmed as XSD order; WT 26998 is not a reconciliation source.
- Version literal NIE022 corrected to the accented "Nómina Electrónica" string in Example, Field Options, Example Analysis and Sample File.
- Client sources and observed practice recorded field by field: pay group -> PeriodoNomina; worker type and contract type have no Master Data source (client file codes 14 of 20 interns as 01/2); document type derivation (13 / 22) and number source; second surname blank for 144; place of work has no DIVIPOLA source and the client file wrongly reports the employer's 05/05001 and the home address for everyone; integral-salary flag from WT 62140 (client file flags only 45 of 88); salary = WT 62100 + 62140; vacation, incapacity, maternity/paternity and other leave dates from the Leave Absence Report; service bonus, cesantías, bonuses, allowances, per diems, meal benefit (WT 65818) and informative third-party benefits mapped to elements with the open points flagged; withholding (NIE177) = WT 2552 plus WT 21330 for 6 employees; FSP split; union dues per union WT; advances and WT 21215 legalisation; loans, garnishments, voluntary pension and AFC wage types named.
- Generation country and work country must not copy the home country (client file does so for 6 employees); TiempoLaborado per the annex 360-day rule, not calendar days.

CO-DIAN-002 (Formulario 350) - 8 VC entries (7 substantive)
- Casilla 93 = withholding actually practised: WT 2552 plus WT 21330 for 6 employees, reconciled to the Base of Withholding column V (261/261) and to the NE RetencionFuente element (261/261); scope = every pay group and every run of the month; the single-run Base of Withholding must not be used alone.
- Rounding: whole pesos per employee, nearest 1,000 applied once to the aggregated casilla (ET art. 577).
- Casilla 144: recipient country = tax-residence country, not nationality; code standard left to RA.
- Factual correction: all 9 Tax Procedure 3 employees are in the September run (7 withheld at 20% of gross, 2 at rate 0).

CO-DIAN-004 (Formulario 220) - 30 VC entries (29 substantive)
- Casilla 52 must be computed by the engine from casillas 36-51 and the certificate blocked on mismatch (the client's certificates show 52 = 0 with 46 filled).
- Casillas 34/35: DIVIPOLA code held once as 5 digits and split 2 + 3; casilla 33 is an employer parameter.
- Casilla 50: the client pays pensions directly to 491 payees outside the employee master and certifies the WT 62151/62152 retirees in casilla 46; recorded, placement with RA.
- Casilla 60 = WT 2552 + 21129 (terminations) + 21140 (retirees), excluding theoretical/hypothetical wage types.
- Wage-type sources named for casillas 36, 37, 38, 43, 46, 47, 49, 53, 54, 56, 57; the payroll "Salary Payment Indicator" flag cannot drive the casilla; the Accumulated Report total is a rolling 12 months and cannot feed a tax-year certificate.
- Casilla 25: identity source for payees outside the employee master; casilla 78 label must carry the tax year; payer-name position corrected.

CO-DIAN-005 (Formato 2276) - 18 VC entries (17 substantive)
- Every amount numeral is the calendar-year sum by payment date (ENV-03), never the rolling 12-month accumulator.
- N02/N03/N04: document-type code source linked to the Field Options table; four name columns mapped; DIVIPOLA codes must be held as master data (client has letter department codes and free-text cities).
- N05/N12/N13/N17: numerals fed from a wage-type-to-numeral classification, not from the payroll salary flag.
- N21: employer-paid pensions are populated (491 pensioners outside the master data).
- N23/N24: separate EPS and AFP+FSP wage types; no combined figure. N25/N26: wage-type attribute RAIS voluntary vs voluntary fund, list of PMI wage types to classify. N27: AFC per payment date across the per-bank wage types. N29: withholding actually practised, candidate wage types named. N32: monthly 41 UVT test limited to months with salary up to 310 UVT.

CO-CESANTIAS-006 (Consignación de cesantías) - 15 VC entries (14 substantive)
- E08 and Report Matrix: an employee who leaves is excluded from the deposit and paid directly (Ley 50/1990 art. 99 num. 4); the "owed a pro rata deposit" sentence removed.
- T14: deposit = consolidated 31 December balance net of direct payments already made; January direct payments to employees who left before the deposit are lawful; E92 covers a full discharge only.
- Client sources: December salary = WT 63807 (not 62100); days = Population Rules with WT 68029 as a check only; balance IN01 = |WT 63814| in January; interest IN02 = WT 62127 (not 63815); hire date = "Hire Date" in AAAA-MM-DD.
- Format gaps recorded: fund held as a name (blank for 63), no DANE department/municipality codes, 12-digit phone against the 7-position field, address built from two lines.

PENDING - queries left in column T of the drafts, by owner

Client (via Cinthya)
- Master data: document-type code behind "National ID" and "Identity Card" and precedence when several are filled (PILA, NE, 220, 2276, cesantías); fund-name-to-code list and the 63 employees without a fund (cesantías); Employee Group -> contributor/worker type mapping and the 20 interns' type and contract (PILA, NE); contract term per employee; which start date is the hire date (NE, 220, cesantías); work location address and DIVIPOLA per site; meaning of "Pensioner Effective Date" for 2 employees and of Regime "AReg"; Basic Salary as source of Sueldo and the 4 integral employees with a different G2N salary.
- Wage-type classification: salary character of WT 62523 (transport, convention), of per diems 62805-62810/62820/62821, of extralegal bonuses 62204/62208-62210/62831; product behind WTs 21610-21612 (health); Foncoltabaco and cooperative wage types; informative "Inf." benefits per element; expatriate items 65821/1910/1204/21126; WT 62203, 62133, 62116, 62845; union rates per WT and the combined 1.50%; WT 21215 legalisation lines; advances 61100/62838; employer-loan disbursements 67010/67090; AFC reimbursement 62839; FVOL / Plan Institucional split (RAIS vs voluntary fund), including 65803/65804.
- NE file defects to explain: Sueldo 0.00 for interns and 2x for 2 integral employees; integral flag false for 43 WT 62140 earners; place of work 05/05001 and home address for all; home country as generation/work country for 6; TipoCuenta "02" and Metodo 47 for everyone including zero-net expatriates; whole WT 2553 as solidarity; totals not equal to the element sums and WT 21215 added back; off-cycle payment left out of the monthly document; empty SegundoApellido as placeholder decision; overtime hours source.
- Missing files: list of all September payroll runs (id, group, payment date, headcount); G2N and Base of Withholding of the advance and settlement runs (97 IDs with 144.6M of WT 2552 outside the monthly run); retirees' run (WT 62151/62152/62154, 21140); NE documents of the other pay groups; a genuine PILA flat file (the E-Payroll .txt received is an NE sample for one employee); the Contingent Withholding Report; the Form 220 source for the 62154 monthly pensioners; which entity the DATOS sheet belongs to.
- Sick leave paid at 100% for employer and EPS days: confirm as the client's election (CO-GAP-03/04).

RA / Compliance
- PILA: VST definition and triggering wage types; VAC-LR for cash-compensated vacation (WT 79003); how V (salario variable) is determined; Ley 1393 40% test on the full integral salary; IGE/LMA/VAC-LR days in the ARL base; whether campo 45 and campo 95 may differ in practice; exact "total devengado" for the Decreto 1828/2013 art. 7 test; Risk_Class as an employee-level field (Data Dictionary).
- Form 350: non-resident position (casilla 77 vs 109-112) and depurated base vs gross for Tax Procedure 3; contingent withholding (ET art. 126-1/126-4) and theoretical/hypothetical wage types 21330/25834/21114/21619; nature of WT 62151 "Retirement Payment - PRV" and placement of 62151/62152 in casillas 77/93 or 78/94; whether retiree withholding reported in NIE177 means casilla 93 reconciles to 93 + 94; country-code standard for casilla 144.
- Form 220: rounding to the nearest 1,000 (ET art. 577 rounds returns; the 220 is a certificate under ET arts. 378-379, so only if the instruction guide requires it); casilla 4 numbering series vs Format N; 62151/62152 in casilla 46 or 50; vacation pay in casilla 42 vs 36; tax year of the February severance deposit (casilla 49); institutional-plan wage types in casilla 56; which withholding result is certified in casilla 60; casilla 33 System Mapping design point (Company.City_Code) for the development team.
- Formato 2276: numeral 4 for a foreign address; in-kind meal benefit above 310 UVT (numeral 7 vs 17/5); extralegal bonuses and salary per diems (numerals 12/13 vs 5/17); lump-sum retirement payments (numeral 21 vs 17); pensioner health and solidarity deductions in numerals 23/24; tax year of the February severance deposit (numeral 19) and alignment with the Example Analysis; AFC reimbursement in numeral 27; theoretical withholding in numeral 29.
- Nómina Electrónica: document type 21 vs 22 for foreigners' cards; payment method 42/45 vs 47 and the Metodo of a zero-net document; TiempoLaborado 360-day construction; Salud/FondoPension values for apprentices without contributions; EMI record position repeating the corporate name; whether the annual cesantías fund deposit is reported in NIE120; off-cycle payments under Res. 000013/2021 art. 3; negative entitlement lines; carry-forward wage types 1910/1204.
- Cesantías: lawfulness of a January partial direct payment (WT 62126) to an employee still in service and the floor when the remainder is below one day of SMMLV; T15-T17 for affiliates resident abroad; 10-digit landline into the 7-position T18; T20 date for intra-group transfers or rehires; T03 code mapping.
