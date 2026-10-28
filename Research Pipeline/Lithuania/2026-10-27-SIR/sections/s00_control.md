# Document Control and How to Read This Register

## Purpose

This is the Statutory Integration Register (SIR) for Lithuania. It registers every data flow between the payroll engine and a Lithuanian authority that Lithuanian statutory payroll filing depends on: the State Social Insurance Fund Board (**Sodra**) and the State Tax Inspectorate (**VMI**). For each flow it records the identifying fields, the authentication mechanism, the technical specification, the error-handling model and the deadlines, so that the Configuration team can set up the submissions.

Calculation rules are out of scope; they are in the Payroll Regulation Guide 2026, the WTC and the DD. Field-level layouts are in the Report Specifications LT-SODRA-003 (SAM), LT-VMI-001 (GPM313) and LT-VMI-002 (GPM312).

## Scope

The two integrations named for the Accenture Lithuania implementation: **statutory filing** (Sodra and VMI) and **leave** (sickness and maternity data sent to Sodra on NP-SD2).

## Version control

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0 | 2026-10-27 | Mercans Compliance Regulations Team | Initial version: integration landscape for the Sodra and VMI payroll filings (SAM, NP-SD2, GPM313, GPM312), built from the authorities' current published sources |

## Source discipline

Two classes of statement appear in this register and they are not interchangeable.

| Class | Where it comes from | How it is marked |
|---|---|---|
| Technical and procedural content — channels, authentication, protocol, file format, error codes, deadlines | The authority's own published pages, instructions and technical documentation | Cited by source key S1 to S9; the sources are listed with version and date in Section 7 |
| Absent content | A genuine search returned no published source | Written as **NOT LOCATED** and collected in Section 8 with the enquiry that would close it, never filled with a plausible value |

Nothing was tested against the live services: no login and no calls to production endpoints.

## Product Mapping Required — what the flag means

The column answers one question: **does the Mercans product need a configured mapping layer — wage type to field, or code list to code list — for this flow to work?** It is not a scope flag and it is not an importance flag.

- **true** means a mapping must be built and maintained, and a change in the authority's form definition is a product change.
- **false** means the flow is a status response that carries no payroll-element semantics.

## Currency of the sources

The sources behind this register were read on **27 October 2026**. Two technical documents are materially older than the forms they serve and this is flagged where it matters: the Sodra DataService instruction is **version 1.0 of 19 January 2016**, and the VMI web-service specification is **version 2.01 of 2010**. Both are the versions offered on the authorities' current pages.
