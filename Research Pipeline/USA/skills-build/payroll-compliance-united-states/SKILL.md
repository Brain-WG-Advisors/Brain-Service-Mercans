---
name: payroll-compliance-united-states
description: United States private-sector payroll compliance for 2026 (with dated 2027 values) across the federal layer and all 50 States plus the District of Columbia - IRS federal income tax withholding (Pub. 15-T), FICA (OASDI, Medicare, Additional Medicare), FUTA, Forms W-2, 941, 940 and State withholding, State unemployment insurance, paid family and medical leave programmes, State minimum wage and pay-statement rules, multistate residence and reciprocity rules, wage type catalogue, data dictionary, Report Specifications, third-party filing hand-off and payslip. Currency USD. Contractors and Form 1099-NEC are out of scope. Use for any question about US payroll rates, thresholds, filings, wage types, master data or payslip content, federal or by State.
---

# United States payroll compliance - router

**ALWAYS use the Read tool on the relevant reference file BEFORE answering. Do NOT answer US-specific rates, wage bases, brackets or deadlines from general knowledge.** The United States has no single payroll regime: a federal layer (IRS, SSA, DOL) sits under 51 State layers, and many values change mid-year or between 2026 and 2027.

The reference files are long. Read with `offset`/`limit` or Grep for the heading or the fact key (for example `fed.fica.oasdi.wage_base`) instead of loading a whole file.

## Routing

| Topic | Read |
|---|---|
| Federal income tax withholding, FICA, FUTA, W-2/W-4/941/940, special populations | `references/10-federal.md` |
| Residence vs work-location sourcing, reciprocity, multistate employees | `references/11-multistate.md` |
| One State (income tax withholding, SUI, PFML, minimum wage, pay statement, new hire, filings, local taxes) | `references/12-states/<XX>.md` (index: `references/12-states.md`) |
| Cross-cutting configuration guide, modules 1-13, worked examples, practices | `references/01-ccg.md` then `references/01-ccg/<module>.md` |
| Wage types (global baseline plus US additions), tax and contribution flags | `references/02-wtc.md` |
| Statutory integrations and the third-party provider hand-off | `references/03-sir.md` |
| Report Specifications (IRS, SSA, State DOR, UI, PFML, local, new hire) | `references/04-reports-spec.md` then `references/04-reports-spec/<report>.md` |
| Data dictionary, master data, option mappers | `references/05-data-dictionary.md` |
| Payslip generator and pay-statement content | `references/06-payslip.md` |
| QA results, exemptions, limitations, source-change log | `references/07-qa-report.md` |
| Traps: statute vs withholding table, assessment-only items, channels | `references/13-gotchas.md` |
| Open gaps and the US-OWN-001..011 owner decisions | `references/14-known-gaps.md` |
| Legal basis rows (authority, article, URL, effective dates) | `references/15-sources.md` |

## How to answer

1. Read the reference first; quote the value verbatim with its unit.
2. Cite the register id in brackets (for example `[US-FEDS5-005]`) and give the effective period. Every content reference file (CCG modules, federal, multistate, State, WTC, SIR, Report Specification, data dictionary and payslip files) ends with a fact index listing key, value, effective period and register id; the index files, QA report, gaps and sources files have none.
3. A value that changes in time is multi-period: give the period asked for. Tax and contribution values are selected by the payment date of the run; minimum-wage rates by hours worked on or after the effective date; Massachusetts PFML by earning date. Example: OASDI wage base USD 184,500 (2026) and USD 192,300 (2027); Utah allowance schedule applies from 2026-04-01; Massachusetts PFML split changes from 2027-01-01.
4. If the reference prints 'Not configured in this release (open gap id)', say the point is not established and name the gap; never estimate. Re-verify time-varying values against the authority before relying on them in a live run.

## Scope and limits

- In scope: private-sector employers, common-law employees, the federal layer, the 50 States and the District of Columbia, State and local payroll levies listed in the references.
- Out of scope: independent contractors and Form 1099-NEC reporting [US-OWN-008]; territories; public-sector employers; certified payroll production (informational flag only [US-OWN-009]).
- Filings to States are made through a third-party provider hand-off, not by system-to-system integration with each agency (`references/03-sir.md`).
- Open gaps, TY2025-labelled federal items and owner decisions: `references/14-known-gaps.md`.

## Design clarifications

1. **Withholding follows the withholding instrument, not the statute.** South Carolina Act 110 rates apply to the 2026 annual return only; Wisconsin, Nebraska, Kansas and Ohio withholding tables are not the statutory brackets. See `references/13-gotchas.md` section 2.
2. **Tips and overtime deductions (Public Law 119-21) reduce assessment, not withholding,** except through federal Form W-4 Step 4(b) (section 3 of the gotchas).
3. **District of Columbia has no published 2026 withholding method.** The last published instruction is Notice 2022-08; applying it to 2026 is an inference the payroll calculation must flag (`references/12-states/DC.md`, gap RQ-138).
4. **Louisiana LAWATS is the power-of-attorney portal, not the wage-report channel;** the UI wage report goes through the Louisiana Workforce Commission online services [US-LAS5-007].
5. **Hawaii HRS 487J** bars public display and mailing of a full SSN, except employer-to-employee communications.
6. **Additional Medicare Tax runs on its own calendar-year base** with its own threshold, employee-only.
7. **Every dated value is multi-period.** Do not carry 2026 values into 2027 or the reverse. The District of Columbia minimum wage follows hours worked, not the payment date.
8. **Contractors and Form 1099-NEC are out of scope.**
