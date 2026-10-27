# -*- coding: utf-8 -*-
"""Record explicit spec-coverage decisions for the five inbound integrations
(v2.7 STEP 3 audit trail). Run once from CO-compliance/."""
import collections
import io
import json

P = "scope_manifest.json"
d = json.load(io.open(P, encoding="utf-8"), object_pairs_hook=collections.OrderedDict)

COVERAGE = {
    "CO-IN-NE-APPRESPONSE": (
        "COVERED INSIDE CO-DIAN-001-NominaElectronica-Spec.xlsx. The ApplicationResponse is "
        "synchronous in the same SOAP call as the outbound document, so it belongs to that Spec's "
        "own file structure and is modelled there rather than as a separate workbook."),
    "CO-IN-PILA-SETTLEMENT": (
        "COVERED INSIDE CO-PILA-003-AportesSeguridadSocial-Spec.xlsx. The settlement output is the "
        "return leg of the same planilla and is modelled with the outbound record."),
    "CO-IN-CESANTIAS-CONFIRMATION": (
        "COVERED INSIDE CO-CESANTIAS-006-ConsignacionAnual-Spec.xlsx, Spec fields E10, E11, E90, "
        "E91 and E93 (planilla number, control total, payment date, per-employee deposit-compliance "
        "status, fund certificate reference), with the channel documented on Sheets 5 and 9."),
    "CO-IN-EPS-ARL-BENEFIT": (
        "NO SEPARATE SPEC - deliberate, and the reason is that there is nothing to specify at field "
        "level. The amount and period of a recognised sickness, maternity, paternity or "
        "occupational-injury benefit is retrieved from each EPS's or ARL's own portal, and there "
        "are dozens of EPS and several ARL, each with its own screen or export and NO published "
        "file format, schema or column layout from any of them - and no government-published one "
        "either, because the recognition is an act of the insurer, not of an authority. A 9-sheet "
        "Spec written without a source would be a fabricated layout and a C25 failure. The "
        "SUBSTANCE is nonetheless carried in the pipeline: the benefit is modelled as a wage-type "
        "line paid to the employee and receivable from the institution (see 02-wtc and CCG Modules "
        "5 and 8), and the employer-borne first two days of general-illness incapacity are tracked "
        "at CO-GAP-03. REVISIT if a client standardises on one EPS/ARL and can supply that "
        "institution's export layout."),
    "CO-IN-LIBRANZA-SCHEDULE": (
        "NO SEPARATE SPEC - deliberate, and out of STEP 3's scope on two independent grounds. "
        "First, it is not a government-to-employer flow at all: the counterparty is a private "
        "payroll lender (entidad operadora de libranza) under Ley 1527 de 2012, and scope_manifest "
        "already records the flow as owned upstream by the lender. Second, the format is "
        "lender-specific with no published schema. The two things the ENGINE must do are specified "
        "elsewhere: carry the instalment as a deduction wage type (02-wtc), and enforce the Ley "
        "1527 floor that the aggregate of libranza deductions must leave the employee at least 50% "
        "of net salary as an engine validation rule (CCG Module 7)."),
}

n = 0
for entry in d["integrations"]["inbound"]:
    key = entry.get("id")
    if key in COVERAGE:
        entry["spec_coverage"] = COVERAGE[key]
        n += 1

io.open(P, "w", encoding="utf-8").write(json.dumps(d, indent=1, ensure_ascii=True))
print("spec_coverage recorded on %d of %d inbound integrations"
      % (n, len(d["integrations"]["inbound"])))
