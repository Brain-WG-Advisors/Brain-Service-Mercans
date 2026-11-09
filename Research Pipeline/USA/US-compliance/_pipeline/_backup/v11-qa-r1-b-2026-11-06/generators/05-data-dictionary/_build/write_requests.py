# -*- coding: utf-8 -*-
"""Write _research/DD-research-request.json (contract research-request 1.4.0) from the markers of the built workbook.

New gaps (RQ-01..RQ-05) carry the in-place marker in the workbook; documented limitations (RQ-06..RQ-10, the
unresolved[] of the DD facts) use the neutral wording 'not named in the cited sources' in the cells and are listed
here so that agent 2 sees them in one queue.
"""
import json
import os
import re
import sys

from openpyxl import load_workbook

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import dd_common as D  # noqa: E402

REL = f"05-data-dictionary/{D.FILENAME}"


def markers(wb):
    out = {}
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if isinstance(c.value, str) and "[[GAP:DD-RQ-" in c.value:
                    for i in re.findall(r"DD-RQ-(\d{2})", c.value):
                        out.setdefault(i, []).append(f"{ws.title}!{c.coordinate}")
    return out


def find_row(wb, sheet, name):
    ws = wb[sheet]
    col = 3 if sheet == "ID Information" else 4
    for r in range(5, ws.max_row + 1):
        if ws.cell(r, col).value == name:
            return f"{sheet}!{ws.cell(r, col).coordinate}"
    return f"{sheet}!A1"


def find_mapper(wb, name):
    ws = wb["Country Option Mappers"]
    for r in range(5, ws.max_row + 1):
        if ws.cell(r, 2).value == name:
            return f"Country Option Mappers!B{r}"
    return "Country Option Mappers!B5"


def main():
    wb = load_workbook(os.path.join(D.OUT, D.FILENAME))
    mk = markers(wb)

    def loc(i, fallback):
        cells = mk.get(i)
        return f"{REL}!{cells[0]}" if cells else f"{REL}!{fallback}"

    def also(i):
        return mk.get(i, [])

    unresolved = {u["key"]: u for u in D.DDFACTS.get("unresolved", [])}
    reqs = [
        dict(id="RQ-01", key="dd.state.w4.line_structure", location=loc("01", "Country Fields!A1"),
             question="For each State that levies income tax withholding, which fields does the current employee withholding "
                      "certificate carry (allowances or exemptions, additional amount, exemption claim, filing status codes) and "
                      "which limits does the form set, for 2026 (and 2027 where published)?",
             why_blocking="The DD field 'State withholding certificate on file' holds only the form identifier of each State; "
                          "the certificate fields that the State withholding calculation reads cannot be modelled as DD fields "
                          "without the form structure.",
             domain="income_tax", acceptable_tier="A.2", severity="major",
             expected_shape="per State: ordered field list with type and limits, with the register row of the form and its revision",
             attempted_by_requester=["_research/DD-8_sheets-facts.json (dd.state.w4.* carry form identifiers only)",
                                     "_research/DD-research-pack.md (tax certificates table)"],
             _status="open_non_blocking", _placeholder_written="in-place marker at " + ", ".join(also("01"))),
        dict(id="RQ-02", key="dd.codelists.external", location=loc("02", "Country Option Mappers!B1"),
             question="Which values of the Ohio school district codes, Ohio municipal codes, Indiana county codes, Maryland "
                      "county codes, Pennsylvania PSD codes, SOC codes, NAICS codes and the Alaska occupational and geographic "
                      "codes must the DD carry as option mapper values, and what are they, with their register rows?",
             why_blocking="The option mappers of these fields are pointer rows; the dictionary cannot list the values "
                          "without facts that carry them.",
             domain="statutory_reporting", acceptable_tier="A.2", severity="minor",
             expected_shape="per list: code, description and effective period, one register row per list",
             attempted_by_requester=["_research/DD-8_sheets-facts.json (field facts carry no list values)",
                                     "register rows US-OHS5-019 (school district list, local copy) and US-OHB5-002 "
                                     "(municipal rate table, local copy) hold the Ohio lists but no fact carries their values"],
             _status="open_non_blocking", _placeholder_written="in-place marker at " + ", ".join(also("02"))),
        dict(id="RQ-03", key="dd.ui.adjustment_reason.codes", location=loc("03", "Country Option Mappers!B1"),
             question="What are the adjustment reason codes of the Maryland and Massachusetts unemployment insurance wage "
                      "reports (the research pack names the Maryland codes 00-10 on register row US-MDS5-017), effective 2026?",
             why_blocking="The option mapper 'UI adjustment reason code (State list)' has no values: the register row carries "
                          "the Maryland codes but no DD fact does.",
             domain="statutory_reporting", acceptable_tier="A.2", severity="minor",
             expected_shape="code list per State with descriptions, as a DD fact bound to US-MDS5-017 and the Massachusetts row",
             attempted_by_requester=["_research/DD-research-pack.md (Country Option Mappers section)",
                                     "_research/DD-8_sheets-facts.json"],
             _status="open_non_blocking", _placeholder_written="in-place marker at " + ", ".join(also("03"))),
        dict(id="RQ-04", key="dd.fed.depositor_status.codes", location=loc("04", "Country Option Mappers!B1"),
             question="Which federal deposit schedule names does Form 941 use for the depositor status (monthly and "
                      "semiweekly schedule depositor), per the IRS instructions for the 2026 Form 941?",
             why_blocking="The option mapper 'Federal depositor status' mirrors the two values of the Report Specification "
                          "US-IRS-001 Field Options; no fact carries them, so they are not bound to a key.",
             domain="statutory_reporting", acceptable_tier="A.2", severity="minor",
             expected_shape="a DD fact with the two names bound to register row US-FEDS5-004",
             attempted_by_requester=["_research/*-facts.json searched by key and value (fed.deposit.* carry thresholds only)"],
             _status="open_non_blocking", _placeholder_written="in-place marker at " + ", ".join(also("04"))),
        dict(id="RQ-05", key="dd.fed.special_population.category", location=f"{REL}!" + find_mapper(wb, "Employee special population category"),
             question="Can the owner scope statement dd.fed.special_population.category (register row US-OWN-005; held in "
                      "_owner_scope, not in facts[] of the DD facts file) be promoted to a fact, so that the option mapper "
                      "'Employee special population category' can carry a tag?",
             why_blocking="The seven categories are written as a scope decision with a citation; a [[FACT:]] tag needs the "
                          "statement in facts[].",
             domain="payroll_data_protection", acceptable_tier="A.2", severity="minor",
             expected_shape="facts[] entry dd.fed.special_population.category with register_id US-OWN-005",
             attempted_by_requester=["_research/DD-8_sheets-facts.json _owner_scope"],
             _status="open_non_blocking"),
    ]
    docs = [("RQ-06", "dd.tx.ui.enhanced_mandatory_from", "Country Fields", "Remote-work status", "payroll_data_protection"),
            ("RQ-07", "dd.ct.ui.q3_2026_positions", "Country Fields", "Worksite ZIP code", "statutory_reporting"),
            ("RQ-08", "dd.pa.psd_code.format", "Option", "Pennsylvania PSD code", "income_tax"),
            ("RQ-09", "dd.oh.municipal_rate_table.code_identity", "Option", "Ohio municipal code", "income_tax"),
            ("RQ-10", "dd.fed.nra.visa_class.examples", "Option", "Nonresident alien visa class", "income_tax")]
    for rid_, key, sheet, nm, dom in docs:
        u = unresolved[key]
        if sheet == "Option":
            ws = wb["Country Option Mappers"]
            cell = "B1"
            for r in range(5, ws.max_row + 1):
                if ws.cell(r, 2).value == nm:
                    cell = f"B{r}"
                    break
            where = f"{REL}!Country Option Mappers!{cell}"
        else:
            where = f"{REL}!{find_row(wb, sheet, nm)}"
        reqs.append(dict(
            id=rid_, key=key, location=where,
            question=("What closes the documented limitation " + key + ": " + u["why"]).rstrip(".") + "?"
                     if len(u["why"]) > 10 else "Documented limitation",
            why_blocking="Documented limitation carried from the DD facts; the cell states it in the neutral wording 'not named "
                         "in the cited sources' and no value is invented.",
            domain=dom, acceptable_tier="A.2", severity="minor",
            expected_shape=u.get("what_would_close_it", ""),
            attempted_by_requester=list(u.get("attempted", [])),
            _status="documented_limitation"))
    for r in reqs:
        if not r.get("_placeholder_written"):
            r.pop("_placeholder_written", None)
        if not r.get("expected_shape"):
            r.pop("expected_shape", None)
    doc = dict(schema_version="1.4.0", artifact="DD", unit="8_sheets", requested_by="artifact-builder", round=1,
               created_on="2026-11-03",
               _note="Open points of the DD build round 1. RQ-01 to RQ-05 are new and carry the in-place marker "
                     "(DD-RQ-nn in the cell); RQ-06 to RQ-10 are the documented limitations of the DD facts and use the "
                     "neutral wording in the cells. None blocks the artifact.",
               requests=reqs)
    path = os.path.join(D.RESEARCH, "DD-research-request.json")
    json.dump(doc, open(path, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print("written", path, len(reqs), "requests;", {k: len(v) for k, v in mk.items()}, "markers")


if __name__ == "__main__":
    main()
