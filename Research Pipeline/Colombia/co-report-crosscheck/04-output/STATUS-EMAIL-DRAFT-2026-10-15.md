Subject: Colombia (PMI) – Report specs vs client reports: cross-check status, 15 Oct 2026

Hi Manju, hi Cinthya,

Following the 14 Oct minutes, here is the status of the cross-check of our 6 Colombia report specs against the reports PMI produces today. The check covered the 18 client workbooks received (masked copies), field by field against each spec, with an independent second pass per spec. No spec has been changed; every proposed change is in a change map awaiting approval. No spec is marked approved.

STATUS PER ARTIFACT

1. CO-PILA-003 – PILA (social security). Status: cross-checked, change map drafted (54 edits), verifier agreement 94%.
   - 5 conflicts to rule against the official text (Anexo Técnico 2 v30): total payroll value campo 45 vs 95 (the spec contradicts itself in 4 places); CCF base capped at 25 SMMLV vs the client's 4% on the uncapped base; the basis of the art. 114-1 exoneration test (client appears to test total earnings, not the IBC).
   - Format gaps: AFP/EPS held as names, not codes; no DIVIPOLA code for work location; risk class per employee; leave dates DD-MM-YYYY.
   - Pending: Wallisson (ruling on the 3 conflict groups with RA); Cinthya/client (CCF of affiliation, ARL administrator, document-type meaning of "National ID"/"Identity Card", interns' contributor type, 2 employees with a "Pensioner Effective Date" equal to hire date).

2. CO-DIAN-001 – Nómina Electrónica. Status: cross-checked, change map drafted (79 edits), verifier agreement 85%.
   - 2 conflicts: collective-agreement transport allowance paid above 2 SMMLV (74 employees); pension rate for 2 "pensioners" (verifier recommends downgrading to a client query, the date looks defaulted).
   - Format gaps: contract type is "WM" for everyone; no DIVIPOLA for place of work; account type stored as code "02"; leave dates DD-MM-YYYY.
   - Build-relevant: no source for overtime hours; single wage type for the solidarity fund (engine must split); informative benefits booked as earning + equal deduction; the monthly NE must combine all payroll runs (advances and some leave run outside the monthly G2N).
   - Pending: Wallisson (RA queries, whether Bank Payments becomes a reconciliation source); Cinthya/client (hire date to use, contract term and interns' status, payment-method code, union rates, Foncoltabaco classification, salary character of bonuses, sick-leave rate confirmation).

3. CO-DIAN-002 – Formulario 350. Status: cross-checked (only spec with a direct client report), change map drafted (9 edits), verifier agreement 83%.
   - Confirmed by data: casilla 93 = "WITH CONTRIBUTION" withholding (WT 2552 + WT 21330 equals the report total to the peso); casilla 77 = depurated base, with the AFC/APV relief and the 40% / 1,340 UVT cap missing from the spec text.
   - 3 conflicts: procedure-3 (non-resident) base and placement; retiree payments below 1,000 UVT that the client still withholds on.
   - The Base of Withholding covers one payroll run, not the month; Form 350 must sum all runs.
   - Pending: Wallisson (contingent withholding treatment, which other withholding WTs enter casilla 93, retiree income classification, recipient country code source).

4. CO-DIAN-004 – Formulario 220. Status: cross-checked, change map drafted (23 edits), verifier agreement 77% (verifier downgraded 1 conflict to an RA query and 2 format mismatches to "not evidenced").
   - Build-relevant: the client pays pensions directly to 491 pensioners who are not in Master Data (no source for their names, document type or location); the Accumulated Report "Total" spans Oct-2025 to Sep-2026, so it cannot feed a tax-year certificate; a wage-type-to-casilla table is required (the client's salary flag cannot drive it).
   - Pending: Wallisson/BAU (meaning of "Beneficiary National Id / Name" on pension rows: substitute pension or bank-account holder); Cinthya/client (termination date source, dependants' identification).

5. CO-DIAN-005 – Formato 2276. Status: cross-checked, change map drafted (19 edits), verifier agreement 92%, no conflicts.
   - Same structural points as Form 220 (pensioners outside Master Data, rolling-12-month accumulations, wage-type-to-numeral table, no DANE codes).
   - Pending: Wallisson (meal benefit above 310 UVT routing; tax year of the February severance deposit, where the Field Explanation and the Example Analysis must say the same thing).

6. CO-CESANTIAS-006 – Consignación anual de cesantías. Status: cross-checked, change map drafted (14 edits), verifier agreement 94%.
   - 1 conflict inside the spec itself: E08 says leavers still get a pro-rata deposit, the Population Rules say they are excluded; the client data agrees with the Population Rules (Law 50/1990 art. 99 num. 4 to be confirmed by RA).
   - Build-relevant: the deposit is a net amount (balance at 31 Dec minus direct payments); two wage types paid directly (62110/62117, 62126) have no spec field.
   - Format gaps: fund code held as a name (blank for 63 employees); hire date DD-MM-YYYY; phone 12 digits vs 7; no DANE codes.
   - Pending: Wallisson/RA (leaver rule; lawfulness of January direct payments of an already consolidated balance); Cinthya/client (12 employees deposited in February with no fund in master data).

CLIENT REPORTS WITH NO STATUTORY SPEC (decision needed: build as client-specific reports or out of scope)
Bank Payments, Zero/Negative Net Pay, Variance per Employee (Gross, Net), Variance on Total Statutory, Loans Balance (2 sheets), ESS Benefit Request, Leave Reimbursement, Pac Reports (leave-request log), CARGA_MASIVA_AFC (SAP FI journal upload), CCT Third-Party deductions, Severance Massive Calculation (dismissal-indemnity simulation, not cesantías).

STILL MISSING FROM THE CLIENT
Contingent Withholding Report (not received; the Base of Withholding carries a "CONTINGENT WITHHOLDING" column that may cover it). The 3 PDFs (Duplicate Bank Accounts, Bank Payments PDF, OP Bancarizados) were not analysed; Bank Payments was analysed from its xlsx.

NEXT STEPS
- Wallisson: rule on the 12 conflicts with RA and the official texts; approve or reject the 6 change maps; send the agreed deltas to Mohit's team before 31 Oct.
- Cinthya: raise the client questions listed above (master-data gaps: fund/administrator codes, CCF, DANE codes, document type, worker type, termination date, overtime hours, dependants).
- Manju: decision on the client-only reports (client-specific build or out of scope).

The full workbook (verdict per field, evidence, proposed explanation, uncovered columns, report map) is at 04-output/CO-SPECS-vs-CLIENT-REPORTS-CROSSCHECK.xlsx.

Best regards,
Wallisson
