# Document Control

| Field | Value |
|---|---|
| Document ID | LT-SIR-001 |
| Version | v1.1 |
| Country | Lithuania (LT) |
| Jurisdictions | National — State Social Insurance Fund Board (Sodra) and State Tax Inspectorate (VMI) |
| Tax year | 2026 |
| Currency | Euro (EUR) |
| Prepared by | Mercans Compliance Regulations Team |
| Status | Issued |
| Related deliverables | Report Specifications LT-SODRA-003 (SAM) v1.1, LT-VMI-001 (GPM313) v1.2 and LT-VMI-002 (GPM312) v1.2 (A1 to A3); Lithuania Payroll Regulation Guide 2026; Lithuania WTC; Lithuania Data Dictionary |

## Version history

| Version | Date | Author | Change |
|---|---|---|---|
| v1.0 | 2026-10-27 | Mercans Compliance Regulations Team | Initial version: integration landscape for the Sodra and VMI payroll filings (SAM, NP-SD2, GPM313, GPM312), built from the authorities' current published sources |
| v1.1 | 2026-10-29 | Mercans Compliance Regulations Team | Corrections after independent review: IN-01 as the NP-SD2 return leg made conditional on G5; 9-SD recorded as an open scope decision (G13); VMI error notices to the EDS contacts (IN-04, 5.2); SAM validation and correction rows in 5.1 (G10, G14); Document Control, 0.2, 0.5, 3.3, 5.3 and 6.3 added; Sodra source status stated (G16); references to A1 v1.1, A2 v1.2 and A3 v1.2 |

# 0. Purpose, Scope and Audit Compliance

## 0.1 Purpose and scope

This is the Statutory Integration Register (SIR) for Lithuania. It registers every data flow between the payroll engine and a Lithuanian authority that Lithuanian statutory payroll filing depends on: the State Social Insurance Fund Board (**Sodra**) and the State Tax Inspectorate (**VMI**). For each flow it records the identifying fields, the authentication mechanism, the technical specification, the error-handling model and the deadlines, so that the Configuration team can set up the submissions.

Calculation rules are out of scope; they are in the Payroll Regulation Guide 2026, the WTC and the DD. Field-level layouts are in the Report Specifications LT-SODRA-003 (SAM), LT-VMI-001 (GPM313) and LT-VMI-002 (GPM312).

Scope: the two integrations in scope are **statutory filing** (Sodra and VMI) and **leave** (sickness and maternity data sent to Sodra on NP-SD2). Whether the 9-SD notice also belongs to the leave integration is an open scope decision (Section 8, G13).

## 0.2 Build order

This register was built as Stage 6 of the pipeline, after the Report Specifications (Stage 3): the SAM, GPM313 and GPM312 specifications existed when it was written, and Section 2.3 names each one with its version. NP-SD2 has no Report Specification (G5). Version 1.1 follows an independent review of version 1.0 and refers to the specification versions issued at the same time (A1 v1.1, A2 v1.2, A3 v1.2).

## 0.3 Source discipline

Two classes of statement appear in this register and they are not interchangeable.

| Class | Where it comes from | How it is marked |
|---|---|---|
| Technical and procedural content — channels, authentication, protocol, file format, error codes, deadlines | The authority's own published pages, instructions and technical documentation | Cited by source key S1 to S12; the sources are listed with version and date in Appendix A |
| Absent content | A genuine search returned no published source | Written as **NOT LOCATED** and collected in Appendix B with the enquiry that would close it, never filled with a plausible value |

Nothing was tested against the live services: no login and no calls to production endpoints.

## 0.4 Product Mapping Required — what the flag means

The column answers one question: **does the Mercans product need a configured mapping layer — wage type to field, or code list to code list — for this flow to work?** It is not a scope flag and it is not an importance flag.

- **true** means a mapping must be built and maintained, and a change in the authority's form definition is a product change.
- **false** means the flow is a status response or a notice that carries no payroll-element semantics.

## 0.5 Completeness verification against the Payroll Regulation Guide

The statutory reports section of the Lithuania Payroll Regulation Guide 2026 lists GPM313 and SAM as monthly reports and GPM312 as the annual report (A4, paragraphs P377 to P402): they are OUT-03, OUT-01 and OUT-04 here, with the same deadlines. The Guide also mentions the 1-SD new-hire notice (P206), which is recorded in Section 2.4. NP-SD2 (OUT-02) is not in the Guide; it is registered because the leave integration is in scope. Nothing in the Guide's report list was dropped.

## 0.6 Currency of the sources

The sources behind this register were read on **27 October 2026**. Two technical documents are materially older than the forms they serve and this is flagged where it matters: the Sodra DataService instruction is **version 1.0 of 19 January 2016**, and the VMI web-service specification is **version 2.01 of 2010**. Both are the versions offered on the authorities' current pages. S11 and S12 were read on 29 October 2026. The Sodra sources S1 to S4 are held as extracts only; the originals are not archived (Appendix A, G16).
