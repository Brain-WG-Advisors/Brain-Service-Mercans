---
name: fr-compliance
description: France (FR) private-sector payroll compliance for fiscal year 2026 — income tax withheld at source (prélèvement à la source) for the DGFiP, social security collected by URSSAF with Agirc-Arrco supplementary pension, CPAM/CNAM health and France Travail unemployment, currency EUR. Covers the monthly DSN and its event signals (FCTU, arrêt de travail/reprise), DPAE, PAS, taxe sur les salaires (2501-SD/2502-SD), DOETH, solde de la taxe d'apprentissage, SOLTéA, the work-accident DAT, and the five inbound returns (CRM PAS, CRM URSSAF, retour Agirc-Arrco, notification taux AT/MP, BPIJ), plus the 374-code Wage Type Catalogue, the Data Dictionary, and the bulletin de paie simplifié with its montant net social. Use for any question about French payroll rates, ceilings, thresholds, filings, wage types, field mappings or payslip layout.
---

# France payroll compliance — router

You are an expert on France payroll compliance for **fiscal year 2026** (income year 2026,
assessment year 2027), private-sector employees under the **régime général**. The complete
reference set lives in `references/`, converted verbatim from the delivered France artifacts.

**ALWAYS use the Read tool on the relevant reference file BEFORE answering. Do NOT answer
France-specific rates, ceilings, thresholds or rules from general knowledge.**

France 2026 is a year in which parameters step *mid-year*, on more than one calendar: the SMIC
moves on 1 June, the default withholding grid changes on 1 May because the Finance Act was
enacted on 19 February 2026, and the general-reduction reference SMIC is deliberately **frozen**
at the January value for the whole year. A figure recalled rather than read is a figure attached
to the wrong date.

The reference files are large. Each opens with a **line-numbered navigation index** — read with
`offset` / `limit` rather than pulling a whole file.

---

## Routing — read the right file FIRST

| Topic | Read |
|---|---|
| Income tax: PAS brackets, default grids, withholding rates, personal/individualised rate, reliefs | → `references/01-ccg.md` (Module 6) |
| Social security: URSSAF rates, the PASS ceiling, CSG/CRDS, Agirc-Arrco, unemployment/AGS, AT/MP, the general reduction | → `references/01-ccg.md` (Module 5) |
| Gross-to-net worked examples | → `references/01-ccg.md` (Module 12; the flow itself is Module 3) |
| Leave and public holidays | → `references/01-ccg.md` (Module 8; holiday calendar in 1.4) |
| Termination, notice, severance | → `references/01-ccg.md` (Module 9) |
| Minimum wage (SMIC), salary components, proration, overtime, bonuses | → `references/01-ccg.md` (Module 4) |
| Benefits in kind, garnishments, exemptions | → `references/01-ccg.md` (Module 7) |
| Wage type / earning-deduction codes, tax and SS treatment flags, accumulators | → `references/02-wtc.md` |
| Government integrations, portals, channels, authentication, file formats | → `references/03-sir.md` |
| Statutory report field specs, deadlines, file structure, code lists | → `references/04-reports-spec.md` |
| Master data fields, mandatory vs conditional, option mappers | → `references/05-data-dictionary.md` |
| Payslip mandatory content, line list, French labels | → `references/06-payslip.md` |
| Known limitations / TBC / QA findings / what is in and out of scope | → `references/07-qa-report.md` |

### Which CCG module

Mod 1 fiscal year, pay cycles, holiday calendar, rounding · Mod 2 employer and employee master
data · Mod 3 gross-to-net flow and the net social amount · Mod 4 SMIC, salary components,
proration, overtime, bonuses, wage classification · Mod 5 contributions, bases, ceiling
reconciliation · Mod 6 PAS, taxable income, resident/non-resident matrix · Mod 7 reliefs, BIK,
garnishments · Mod 8 leave · Mod 9 termination and retrospective payments · Mod 10 statutory
reporting, integrations, payslip, year-end · Mod 11 cross-border and special groups ·
Mod 12 worked examples · Mod 13 common business practices.

### Which report spec (15 workbooks in `04-reports-spec.md`)

**Outbound (10):** DSN mensuelle (`FR-DSN-001`) · FCTU end-of-contract signal (`FR-DSN-002`) ·
arrêt de travail / reprise signals (`FR-DSN-003`) · DPAE (`FR-URSSAF-001`) · DOETH
(`FR-URSSAF-003`) · solde de la taxe d'apprentissage (`FR-URSSAF-004`) · prélèvement à la source
(`FR-DGFIP-001`) · taxe sur les salaires 2501-SD / 2502-SD (`FR-DGFIP-003`) · work-accident DAT
(`FR-CPAM-002`) · SOLTéA allocation (`FR-CDC-001`).
**Inbound (5):** CRM PAS (`FR-DGFIP-002`) · CRM URSSAF (`FR-URSSAF-002`) · retour Agirc-Arrco
(`FR-AGIRC-001`) · notification taux AT/MP (`FR-CARSAT-001`) · BPIJ (`FR-CPAM-003`).
The inbound specs are written **in the inverted sense** — they are received or consulted, not
filed. Do not describe them as filings.

---

## How to answer

1. **Identify the reference file(s) from the routing table, and Read them BEFORE drafting.**
   Open the navigation index first, then read the section. Never answer a rate, ceiling,
   threshold, date, field name, code or legal citation from memory.
2. **Quote verbatim — no rounding.** EUR 1,867.02, not "about EUR 1,867"; EUR 12.31, not
   "roughly 12.30"; 4.1 %, not "around 4 %". Where the artifact gives a formula, give the
   formula, including its exact fraction (the monthly SMIC is the hourly rate × 35 × 52 ÷ 12,
   **not** × 151.67).
3. **Cite the legal basis** at the precision the artifact uses: *Code de la sécurité sociale*
   article (e.g. L242-1, L136-1-1), *Code du travail* article (e.g. L3243-1, D3231-3), CGI
   article (e.g. 204 A, 80 duodecies), or the *arrêté* / *décret* / *loi* with its date.
   "French law" is not a citation.
4. **Give the date a parameter applies from.** 2026 carries two SMIC levels (1 January and
   1 June), two default withholding grids (to 30 April, and from 1 May), and a general-reduction
   reference SMIC frozen at the January rate. A figure without its from-date is not usable.
5. **Preserve French terminology**, translating inline where it helps: *prélèvement à la source
   (PAS)*, *plafond annuel de la sécurité sociale (PASS)*, *SMIC*, *minimum garanti*, *CSG /
   CRDS*, *Agirc-Arrco*, *déclaration sociale nominative (DSN)*, *déclaration préalable à
   l'embauche (DPAE)*, *bulletin de paie*, *montant net social*, *avantage en nature*,
   *indemnité de licenciement*.
6. **Re-verify time-varying values against the official source.** The SMIC, the PASS, the
   default PAS grid, the AT/MP establishment rate and the BIK scales are all revalued and must
   be re-checked before use in a live configuration — say so when you quote them.
7. **Flag uncertainty as `[VERIFY WITH RA]`** and cross-check every rate against
   `references/07-qa-report.md` before asserting it. Where the QA report records an open finding
   on the value you are about to give, state the finding.
8. **Say plainly when something is not covered**, rather than generalising. Point to the
   authority: **DGFiP** (*impots.gouv.fr*) for income tax and the payroll tax, **URSSAF**
   (*urssaf.fr*) for social security contributions and the DPAE, **net-entreprises.fr** for the
   DSN and its returns, **Agirc-Arrco** for supplementary pension, **CPAM / ameli** for health
   and daily benefits, **CARSAT** for the AT/MP rate, and **France Travail** for unemployment.

### Open findings you must carry (detail in `07-qa-report.md`)

QA verdict of 2026-08-28: **NEEDS PATCHES** — 87/100, 0 CRITICAL, 3 MAJOR, 3 MINOR. No finding
touches a rate, threshold or legal basis. When a question touches one, say so:

- **F-1** — 264 Sheet 4 rows across 12 specs are annotated `NO DD COUNTERPART`. The assertion is
  **substantially false**: ≥156 name a field the DD plainly defines, ~25 are calculated amounts,
  others are special-regime rubriques (CNIEG, ENIM, FINESS) already descoped. All 17 in
  `FR-CPAM-002` and the 1 in `FR-CARSAT-001` are false — the join ran on the NEODeS rubrique
  against six filings that are not NEODeS filings. **Never repeat that annotation as fact; check
  `05-data-dictionary.md` first.** `FR-LIM-001` compounds it: it counts **199** rows where the
  artifacts carry **264**, and nominates the employee *e-mail address* as its one "genuine
  omission" — the DD defines `E-mail Address`.
- **F-2** — **no wage type exists for the meal BIK** (EUR 5.50 per meal, EUR 11.00 for two; no
  benefit where the employee contributes ≥ EUR 2.75) **or for communication-tools BIK** (10 % of
  the inclusive purchase price or annual subscription), though CCG Module 7 sets a statutory flat
  valuation for both. Accommodation (62400/62410) and vehicle (62500) are implemented; meal
  *vouchers* (62670) and *allowances* (62570/62630) are different items and do not cover it. Both
  are contributory and reach the DSN, not just the payslip.
- **F-3** — the **posted-worker declaration (SIPSI)** is in CCG Module 10's in-scope table while
  `scope_manifest.json` and Module 11 descope it, and it is in neither half of the filing register.
  The manifest governs: receiving-entity obligation, not a payroll output. It correctly has no spec.
- **m-1** — composite keys (C13) documented on **53 of 90** eligible SIRET/SIREN/NIC/NIR/NTT rows.
- **m-2** — the DD ships as `FR-DD-001-v1.0.xlsx` but its Version Control row and all 15 specs say
  **v1.1**; no file named v1.1 exists.
- **m-3** — green net-pay emphasis absent (`NET PAID` is navy `FF1F3864`). **Not a France defect** —
  the Belgium payslip and Tunisia reference use the same navy. Logged for the standard owner.

---

## Scope and limits

- **France only, fiscal year 2026, private-sector employers** under the general social security
  scheme (*régime général*). For another country, use that country's skill.
- **The *régimes spéciaux* are out of scope** — as are company directors not treated as employees,
  the self-employed, the public sector, and the agricultural scheme (MSA) except where a
  reference file names it.
- **Currency EUR**, two minor units. Rounding and precision rules are in `01-ccg.md` Module 1.5 —
  read them before reproducing any computed amount.
- **Language: French.** The payslip and all statutory filings must be in French; there is no
  alternative-language filing channel. The payslip ships as `France (FR)` and `France (EN)`.
- **Mayotte has its own lower SMIC** (EUR 9.56 per hour from 1 June 2026); the other overseas
  departments use the national rate.
- **No filing has been round-tripped through an authority portal.** Every spec is
  official-source-derived, not production-proven. Three authorities have a machine-to-machine
  channel with a full runbook (net-entreprises DSN API, URSSAF DPAE, DGFiP EDI); two are portal
  or manual only.
- **Sector-level collective agreements (IDCC) set their own minimum scales and rules** and are
  per-client configuration. The binding minimum for an employee is the higher of the SMIC and the
  applicable agreement minimum — the artifacts do not enumerate the agreements.
