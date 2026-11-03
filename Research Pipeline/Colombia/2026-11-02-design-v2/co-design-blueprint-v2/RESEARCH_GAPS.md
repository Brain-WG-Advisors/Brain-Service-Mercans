# RESEARCH GAPS — Colombia design v2.0

| # | Gap | Severity | What closes it |
|---|---|---|---|
| R1 | 21 `Yes/No` wage types need an exempt / subject split at configuration (R6, R37, R227, R241–R248, R282, R284–R286, R338, R346 withholding, R349, R350, R353, R358). | 🟡 | configuration of the split wage types |
| R2 | Apprentice in the practical phase ("all rights of an employment contract", Labour Code art. 81; CCG v1.7): the WTC marks the support R338 `Yes/No` in pension (U), solidarity fund (R), levies (T), benefit base (W) and vacation base (X), so the practical-phase pension, solidarity fund, CCF and statutory benefits are 0 until the support is split by phase (classroom: health and occupational risk only). | 🟡 | split wage type + phase field in the DD |
| R3 | History reads: Procedure 2 fixed percentage (12 months ÷ 13, art. 386; input `58250`, not computed), termination percentage (taxable payments of the 12 months before termination, input `58255`, and months of service, input `58259`; Decree 1625 art. 1.2.4.1.8), severance-savings exemption (6-month average, art. 206 num. 4). | 🟡 | engine history-read mechanism |
| R4 | IBC of the absence days (vacation taken: IBC before the vacation, Decree 780 art. 3.2.5.1; incapacity / leave: benefit value) needs a per-novelty day split; this design gives the benefit IBC as information (`58195`, `58194`). | 🟡 | PILA novelty fields |
| R5 | Occupational-risk rate notified by the insurer per work centre overrides the class initial rate (`9170055`). | 🟡 | DD link work centre → employee |
| R6 | Multi-employer: the 25-SMMLV ceiling applies to the sum across employers. | 🟡 | not modelled |
| R7 | 204-UVT test of the indemnity withholding reads the monthly salary (`$64992`), as the CCG v1.7 worked example (Module 9: 4,500,000 = 85.92 UVT; termination payments out); Tax Code art. 401-3 ("trabajadores que devenguen ingresos superiores a 204 UVT") does not define the income measured. | 🟡 75% | DIAN doctrine |
| R8 | Penalties R341 / R342 (late deposit of severance savings / unpaid interest; Law 50 of 1990 art. 99, text not read): whether they are "indemnizaciones derivadas de una relación laboral" for Tax Code art. 401-3; kept in the monthly read. R340 (Labour Code art. 65, "como indemnización") is routed with the indemnities. | 🟡 | DIAN doctrine |
| R9 | Art. 64 variants (fixed-term contract, work contract, probation, Law 789 transitional table) not built. | 🟡 | research |
| R10 | Solidarity-fund bands of Law 2381 of 2024 from 1 April 2027 (Constitutional Court C-264 of 2026): effective-date the band table. | 🟡 2027 | — |
| R11 | Electronic payroll incapacity type labels 2 / 3 (report side): only a DIAN consultation closes it (75%). | report | DIAN |
| R12 | CCG v1.7 is internally inconsistent on the payroll-levy base of the all-inclusive salary: one passage caps it at 25 SMMLV (43,772,625), another says "no ceiling at all". This design follows Law 21 of 1982 art. 17 (no ceiling). To correct in the CCG. | 🟡 source | CCG |
| R13 | PILA AT2 v30 describes the distribution of contributions under Law 2381 of 2024 from a 2025 period, while the CCG v1.7 dates Law 2381 at 1 April 2027 (Constitutional Court C-264 of 2026). This design follows the CCG; re-check before 2027. | 🟡 2027 | — |
