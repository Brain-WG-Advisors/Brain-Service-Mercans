# -*- coding: utf-8 -*-
"""Build 03-statutory-integrations/US-SIR-INDEX-001-v1.0.docx (the provider hand-off index).

Re-runnable and the only source of the document (C71): a correction goes into this script or sir_defs.py,
never into the .docx. Two passes: pass 1 collects the research requests (F44 gaps, open questions, missing
sources) and assigns SIR-RQ ids in sorted key order; pass 2 writes the document with those ids.

usage: python build_sir.py [--out path]
Writes: the docx, integration-landscape.json, _pipeline/SIR-bindings.csv, _research/SIR-research-request.json,
the SIR entries of _research/gaps.json, _build/checks/sir_requests.json.
"""
import csv
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import sys
from urllib.parse import urlparse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sir_common as S  # noqa: E402
import sir_defs as D  # noqa: E402
import sir_docx as X  # noqa: E402
import sir_specs as P  # noqa: E402

CH_ORDER = ["online_form", "file_upload", "xml", "api", "paper"]
SECTION_OF = {"US-DOR-001": "7.2", "US-DOR-002": "7.3", "US-UI-001": "7.4", "US-SDNH-001": "7.5", "US-PFML-001": "7.6",
              "US-LOC-001": "7.7", "US-LOC-002": "7.7", "US-LOC-003": "7.7", "US-DOR-003": "7.8", "US-DOR-004": "7.8",
              "US-WC-001": "7.8"}
FED_SPECS = ["US-IRS-001", "US-IRS-002", "US-IRS-003", "US-IRS-004", "US-IRS-005", "US-IRS-006", "US-IRS-007",
             "US-IRS-008", "US-SSA-001"]
SPEC_TOPIC = {"US-DOR-001": "State withholding returns and deposits", "US-DOR-002": "State annual reconciliation and W-2 copies",
              "US-UI-001": "State UI quarterly wage reports", "US-SDNH-001": "State new-hire reports",
              "US-PFML-001": "State paid-leave, disability and long-term-care programme reports",
              "US-LOC-001": "Local income and wage tax returns", "US-LOC-002": "City employer payroll tax returns",
              "US-LOC-003": "Seattle payroll expense tax and social housing tax", "US-DOR-003": "Nevada Modified Business Tax",
              "US-DOR-004": "Employer payroll transit levies", "US-WC-001": "State-fund workers' compensation reports"}

RECON = []            # rows of sir_recon.csv, built during pass 2
SPECROW_SIR = {}      # report row id -> (section, keys used, gap ids)


def short(s, n=300):
    s = re.sub(r"\s+", " ", str(s)).strip()
    return s if len(s) <= n else s[: n - 3].rstrip() + "..."


def jn(code):
    return S.state_name(code) if code in S.STATE_NAMES else code


# ======================================================================== sections ===
def cover(doc):
    X.para(doc, "United States of America", bold=True, size=14, after=2)
    X.para(doc, f"Statutory Integration Index — {S.SIR_REF}", bold=True, size=20, after=12)
    X.para(doc, "Provider-agnostic hand-off of federal, State and local statutory filings", size=12, after=24)
    X.table(doc, ["Field", "Value"], [
        ["Document ID", S.SIR_ID], ["Version", f"v{S.PKG}"], ["Country", "United States of America (US)"],
        ["Issue date", S.ISSUE], ["Prepared by", "Mercans Compliance Regulations Team"],
        ["Companion documents", f"{S.CCG_REF}; {S.WTC_REF}; {S.DD_REF}; the Report Specifications US-*-Spec"]], [1.8, 5.3], size=10)
    X.page_break(doc)


def doc_control(doc):
    S.at("Document Control verdict")
    X.h(doc, "Table of Contents", 1)
    X.toc(doc)
    X.page_break(doc)
    X.h(doc, "Document Control", 1)
    X.table(doc, ["Field", "Value"], [
        ["Document ID", S.SIR_ID], ["Version", f"v{S.PKG}"], ["Country", "United States of America (US)"],
        ["Jurisdictions", "Federal; 50 States and the District of Columbia; local taxing authorities named in section 7.7"],
        ["Discovery verdict", S.clean(f"{D.VERDICT}. " + D.verdict_sentence())], ["Language", "English"],
        ["Currency", f"{S.MANIFEST['currency']}"], ["Package version", f"v{S.PKG}"], ["Issue date", S.ISSUE]], [1.8, 5.3], size=9)
    X.h(doc, "Version history", 2)
    X.table(doc, ["Version", "Date", "Author", "Status"], [[f"v{S.PKG}", S.ISSUE, S.AUTHOR, S.STATUS]], [1.0, 1.4, 2.6, 2.1], size=9)


def sec0(doc):
    X.h(doc, "0. Purpose, Scope & Audit Compliance", 1)
    S.at("0 purpose")
    X.para(doc, S.clean(
        "This index is the statutory-integration record for the United States of America. For every federal, State and "
        "local filing in scope it states who receives it, on which channel, under which agent authorisation and what a "
        "third-party filing provider must be given. Mercans produces the provider input and never submits to an authority; "
        "the provider transmits to each authority. The employer keeps legal liability for every return and deposit: "
        f"retained by the employer = {S.fv('sir.fed.agent_authorization.employer_liability_retained')}."))
    S.at("0 verdict")
    X.para(doc, S.clean(
        f"Discovery verdict: {D.VERDICT}. " + D.verdict_sentence() + " Every inbound item is a document the employer acts on; "
        "no inbound file or message from an authority is parsed by the engine. Section 0.4 lists the integration status of each "
        "authority group."))
    S.at("0 provider selection")
    X.para(doc, S.clean(
        "The choice of filing provider is a business decision outside this document. Provider-specific input layouts "
        f"replace the generic minimum data set of section 8 once a provider is chosen: {S.fv('sir.provider.selection')}"))
    X.h(doc, "0.1 Canonical integration inventory", 2)
    rows = []
    ids = {("outbound", 0): "US-OUT-001", ("outbound", 1): "US-OUT-002", ("inbound", 0): "US-INB-001",
           ("inbound", 1): "US-INB-002", ("inbound", 2): "US-INB-003"}
    for d_ in ("outbound", "inbound"):
        for i, it in enumerate(S.SCOPE["integrations"][d_]):
            rows.append([ids[(d_, i)], S.clean(it["name"]), d_.upper(), "Yes" if it.get("product_mapping_required") else "No"])
    X.table(doc, ["Integration ID", "System", "Direction", "Product mapping required"], rows, [1.1, 3.9, 0.9, 1.2], size=9)
    X.h(doc, "0.2 Direction & product-mapping rule", 2)
    X.para(doc, S.clean(
        "Direction is stated from the payroll engine outward: OUTBOUND is a submission or hand-off produced by the engine, "
        "INBOUND is a document or notice from an authority that the engine must act on. Product mapping is required "
        "wherever data held by the payroll product must be produced in, or read from, an authority or provider layout. "
        "Every Report Specification is outbound; the three inbound items of section 1 have no Report Specification because "
        "they are received, not filed."))
    X.h(doc, "0.3 Confidence and accuracy disclosure", 2)
    sp = P.specs()
    accs = [r["accuracy"] for s in sp for r in s["rows"] if r["accuracy"] is not None]
    X.para(doc, S.clean(
        "Each hand-off row in section 7 carries the channel class, portal, confirmation status and accuracy statement of the "
        "matching Report Specification row (accuracy is stated on the Report Matrix scale of 0 to 100: "
        f"lowest {min(accs)}, highest {max(accs)}). No filing was submitted and no real file was checked against an authority "
        "validator, so every channel stays marked as in the Report Specification; the closing evidence for each row is the "
        "provider's acceptance report or one accepted real filing."))
    X.para(doc, S.clean("Open questions recorded with the research (none blocks the document):"))
    for k in D.OPEN_KEYS:
        S.at(f"0.3 open {k}")
        X.para(doc, S.clean(f"•  {OPEN_LABEL.get(k, k)}: " + S.gap(k, "open")), size=9, after=1)
    X.para(doc, S.clean(
        "Where the research does not support a statement, the cell reads \"Not configured in this release\" with a request "
        "number; the list is in Appendix B. A value is written only when every text element of it (numbers, form names, "
        "dates, channel names) was found in the saved copy of its cited source."))
    X.h(doc, "0.4 Integration landscape by authority group", 2)
    X.para(doc, S.clean(
        "One row per integrable party or authority group: whether a system-to-system channel exists, which channel, the direction "
        "from the payroll engine, the developer portal and the location of the configuration runbook. Authority channels that exist "
        "are operated by the filing provider, not by Mercans, so no authority runbook is issued."))
    rows = []
    for g in landscape_groups(docx_mode=True):
        rows.append([g["name"], g["integration_txt"], g["channel_txt"], g["dir_txt"], g["portal_txt"], g["runbook_txt"]])
    X.table(doc, ["Party or authority group", "Integration", "Channel", "Direction", "Developer portal", "Runbook location"], rows,
            [1.5, 0.9, 2.3, 0.8, 0.9, 0.9], size=8)


def sec1(doc):
    X.h(doc, "1. Inbound Integrations (documents from authorities)", 1)
    X.h(doc, "1.1 Finding: three inbound documents drive payroll configuration", 2)
    X.para(doc, S.clean(
        "No inbound file or message from an authority is parsed by the engine. Three kinds of document arrive and change "
        "what the payroll does, so the product must be able to take their data in: income withholding orders, the federal "
        "notice of levy on wages, and the State UI contribution rate notice."))
    X.h(doc, "1.2 Inbound register", 2)
    S.at("1.2 inbound")
    rows = []
    iw = [S.fv(k, jur=None) for _, k in D.INBOUND_FACTS["iwo"]]
    lv = [S.fv(k) for _, k in D.INBOUND_FACTS["levy"]]
    rows.append(["US-INB-001", "State child-support agencies (income withholding order, electronic or paper)", "INBOUND",
                 "Set up the deduction, apply the governing law, remit within the State period. "
                 + " ".join(f"{lab}: {v}" for (lab, _), v in zip(D.INBOUND_FACTS["iwo"], iw)),
                 "Yes; none (received, not filed)"])
    rows.append(["US-INB-002", "Internal Revenue Service (notice of levy on wages, with the employee's exemption statement)", "INBOUND",
                 "Exempt amount by filing status and dependents; the rest goes to the IRS. "
                 + " ".join(f"{lab}: {v}" for (lab, _), v in zip(D.INBOUND_FACTS["levy"], lv)),
                 "Yes; none (received, not filed)"])
    rows.append(["US-INB-003", "State workforce agencies (annual UI contribution rate notice)", "INBOUND",
                 "Employer rate per State and year, loaded as configuration data before the first payroll of the year.",
                 "Yes; none (received, not filed)"])
    X.table(doc, ["ID", "Authority / document", "Direction", "What the engine must do", "Product mapping; Report Spec"], rows,
            [0.8, 1.7, 0.75, 2.85, 1.0], size=8)


def spec_register(doc):
    X.h(doc, "2. Outbound Integrations (submissions through the provider)", 1)
    X.h(doc, "2.1 Outbound register: one row per Report Specification", 2)
    X.para(doc, S.clean(
        "Channel classes are those of the Report Matrix of each specification (online_form, file_upload, xml, api, paper); "
        "xml is recorded only where the specification cites a published schema. Section 7 lists every report row."))
    rows = []
    for s in P.specs():
        chans = set()
        for r in s["rows"]:
            for c in re.split(r",\s*", r["channel"] or ""):
                if c in CH_ORDER:
                    chans.add(c)
        accs = [r["accuracy"] for r in s["rows"] if r["accuracy"] is not None]
        accs_t = (f"{min(accs)} to {max(accs)}" if min(accs) != max(accs) else f"{min(accs)}") if accs else "Not rated"
        sect = SECTION_OF.get(s["id"], "7.1")
        rows.append([s["id"], "OUTBOUND", s["title"].replace(s["id"] + " ", ""), short(s["authority"], 120),
                     ", ".join(c for c in CH_ORDER if c in chans) or "none (routing flag)", accs_t, f"Section {sect}"])
    X.table(doc, ["Report Spec", "Direction", "Report", "Authority", "Channel classes", "Accuracy (0 to 100)", "Hand-off register"],
            rows, [0.95, 0.8, 1.6, 1.5, 1.0, 0.7, 0.55], size=7.5)
    X.h(doc, "2.2 What each channel carries", 2)
    X.table(doc, ["Category", "Reported to", "Specification"], [
        ["Federal employment tax returns, deposits and corrections", "IRS", "US-IRS-001 to US-IRS-008"],
        ["Wage and tax statements and transmittals", "SSA; State revenue departments", "US-SSA-001; US-DOR-002"],
        ["State withholding returns and deposits", "State revenue departments", "US-DOR-001; US-DOR-003; US-DOR-004"],
        ["State UI wage reports", "State workforce agencies", "US-UI-001"],
        ["Paid-leave, disability and workers' compensation reports", "State programme agencies", "US-PFML-001; US-WC-001"],
        ["Local returns", "Cities, counties, school districts, collectors", "US-LOC-001; US-LOC-002; US-LOC-003"],
        ["New-hire reports", "State Directories of New Hires", "US-SDNH-001"]], [3.0, 2.2, 1.9], size=8.5)


def auth_row(j, topic):
    """(text, keys) for the withholding ('wh') or UI ('ui') authorisation instrument of jurisdiction j."""
    jl = j.lower()
    if topic == "wh":
        if j in D.NO_WAGE_TAX:
            t, k = S.pick([f"sir.{jl}.withholding.return", f"rspec.{jl}.wh_return.applicable"], jur=j)
            return ("No State wage tax, so no withholding authorisation: " + t if k else t), k
        keys = D.WH_AUTH(jl)
    else:
        keys = D.UI_AUTH(jl)
    if (j, topic) in D.OPEN_BY_JUR and not any(S.usable(k)[0] for k in keys):
        return S.gap(D.OPEN_BY_JUR[(j, topic)], "open", j), None
    t, k = S.pick(keys, jur=j, gap_key=f"sir.state.{topic}.agent_authorization.missing")
    return t, k


def sec3(doc):
    X.h(doc, "3. Authorisation Requirements", 1)
    X.h(doc, "3.1 Federal appointment", 2)
    S.at("3.1 federal")
    X.table(doc, ["Item", "Requirement", "Source"], [
        ["Reporting agent authorisation", S.tag("sir.fed.agent_authorization.form"), S.cite_f(S.fact("sir.fed.agent_authorization.form"))],
        ["Returns and deposits covered; State and local extension", S.fv("sir.fed.agent_authorization.returns", with_cite=False), S.cite_f(S.fact("sir.fed.agent_authorization.returns"))],
        ["Technical specification for reporting agents", S.fv("sir.fed.reporting_agent.tech_spec", with_cite=False), S.cite_f(S.fact("sir.fed.reporting_agent.tech_spec"))],
        ["Third-party payer arrangements", S.fv("sir.fed.third_party_payer.rules", with_cite=False), S.cite_f(S.fact("sir.fed.third_party_payer.rules"))]],
        [1.9, 3.9, 1.3], size=8)
    X.h(doc, "3.2 Two authorisations per State", 2)
    X.para(doc, S.clean(
        "The federal agreement does not replace the State instruments. Each wage-tax State needs an authorisation from the "
        "employer to the revenue department (withholding) and another to the workforce agency (UI); the revenue department "
        "and the workforce agency are separate institutions with separate portals. Several States now use an online "
        "link or handshake instead of a paper form; the instrument of each jurisdiction is listed in section 3.3."))
    X.h(doc, "3.3 Authorisation instrument per jurisdiction", 2)
    rows = []
    for j in D.J:
        S.at(f"3.3 {j}")
        wh, _k1 = auth_row(j, "wh")
        ui, _k2 = auth_row(j, "ui")
        rows.append([f"{jn(j)} ({j})", wh, ui])
    X.table(doc, ["Jurisdiction", "Withholding authorisation (revenue department)", "UI authorisation (workforce agency)"], rows,
            [1.2, 2.95, 2.95], size=7.5)
    X.h(doc, "3.4 Provider programmes and duties", 2)
    prov = []
    for lab, key in D.PROVIDER_ROWS:
        S.at(f"3.4 {lab}")
        f = S.fact(key)
        prov.append([lab, S.fv(key, with_cite=False), S.cite_f(f)])
    X.table(doc, ["Programme or duty", "Requirement", "Source"], prov, [1.9, 3.9, 1.3], size=8)


def sec4(doc):
    X.h(doc, "4. Technical Specifications", 1)
    X.para(doc, S.clean(
        "File layouts are those published by the authority and read for this release. Where a layout is not configured the "
        "cell says so; the provider's own import layout is recorded in the provider contract, not here."))
    rows = []
    for lab, key in D.TECH_ROWS:
        S.at(f"4 {lab}")
        f = S.fact(key)
        rows.append([lab, S.fv(key, with_cite=False), S.cite_f(f)])
    X.table(doc, ["Layout or specification", "What it fixes", "Source"], rows, [1.9, 3.9, 1.3], size=8)
    S.at("4 state W-2 editions")
    X.para(doc, S.clean("State W-2 editions for TY2026: " + S.fv("sir.w2.state_specs_ty2026")))
    S.at("4 UI file layouts")
    X.para(doc, S.clean("State UI wage-file layouts: " + S.fv("sir.ui.file_specs_missing")))


def sec5(doc):
    X.h(doc, "5. Error Handling: routing, rejection and correction rules", 1)
    S.at("5 error catalogue")
    X.para(doc, S.clean(
        "Authority error-code catalogue (reject and business-rule lists per channel class): "
        + S.gap(ERR_KEY, "missing") + " The rules below are the routing and rejection rules the research found, each stated by "
        "the authority that applies it."))
    rows = []
    for lab, key in D.RULE_ROWS:
        S.at(f"5 {lab}")
        if key not in S.C.FACTS:
            continue
        f = S.fact(key)
        rows.append([lab, S.fv(key, with_cite=False), S.cite_f(f)])
    X.table(doc, ["Rule", "Statement", "Source"], rows, [1.9, 3.9, 1.3], size=8)


def sec6(doc):
    X.h(doc, "6. SLA and Deadlines", 1)
    X.h(doc, "6.1 Federal and cross-cutting deadlines", 2)
    rows = []
    for lab, key in D.DEADLINE_ROWS:
        S.at(f"6.1 {lab}")
        f = S.fact(key)
        rows.append([lab, S.fv(key, with_cite=False), S.cite_f(f)])
    X.table(doc, ["Item", "Deadline or threshold", "Source"], rows, [1.9, 3.9, 1.3], size=8)
    X.h(doc, "6.2 State deadlines", 2)
    S.at("6.2 acknowledgement")
    X.para(doc, S.clean(
        "State due dates are written on the report row of section 7 that they govern. State acknowledgement and response-time "
        "rules were not read for this release: " + S.gap(ACK_KEY, "missing")))


def hand_off_cell(spec, jur, recs):
    """Text of the hand-off requirement cell of a report row; returns (text, keys_used)."""
    parts, used = [], []
    chain = D.chains(spec, jur) if jur else D.FED_ROWS.get(spec, [])
    for lab, keys in chain:
        gk = re.sub(r"[^a-z0-9_.]", "_", f"sir.state.{spec.lower().replace('-', '_')}.{lab.lower().split()[0]}.missing")
        if not keys:
            continue
        if not any(k in S.C.FACTS for k in keys):
            # nothing in the facts for this label: only the first label of a row is a request (the others are optional detail)
            if lab == chain[0][0]:
                parts.append(f"{lab}: " + S.gap(gk, "missing", jur))
            continue
        keys = [x for x in keys if x not in used]
        if lab != chain[0][0]:
            ok_keys = [x for x in keys if S.usable(x)[0]]
            if not ok_keys:
                continue        # optional detail unavailable: leave out rather than open a request for it
            keys = ok_keys
        t, k = S.pick(keys, jur=jur, gap_key=gk)
        parts.append(f"{lab}: {t}")
        if k:
            used.append(k)
    return ("; ".join(parts) if parts else S.gap(re.sub(r"[^a-z0-9_.]", "_", f"sir.state.{spec.lower().replace('-', '_')}.missing"), "missing", jur)), used


def reg_table(doc, spec_ids, title, sect):
    X.h(doc, f"{sect} {title}", 2)
    rows = []
    for sid in spec_ids:
        spec = P.by_id()[sid]
        for r in spec["rows"]:
            jur = r["jur"] if r["jur"] in S.STATE_NAMES else ""
            S.at(f"{sect} {r['row_id']}")
            text, used = hand_off_cell(sid, jur, r)
            ids = [g for g in re.findall(r"\[\[GAP:(SIR-RQ-\d+)\]\]", text)]
            SPECROW_SIR[r["row_id"]] = (sect, used, ids)
            acc = (f"{r['status']}; accuracy {r['accuracy']}" if r["accuracy"] is not None else (r["status"] or "Not rated"))
            if r["closes"]:
                acc += f". Closes with: {r['closes_ref']}"
            chan = f"{r['channel']}; portal: {short(r['portal'], 90)}"
            rows.append([r["row_id"], short(re.sub(r"\(see column [A-Z]\)", "(not named in the cited sources)", r["authority"]), 90), chan, text, S.clean(acc)])
            RECON.append(dict(report_row=r["row_id"], spec=sid, jurisdiction=jur or "FED", section=sect,
                              sir_keys=" | ".join(used), gap_ids=" | ".join(ids),
                              status="MAPPED" if used else "MAPPED_LIMITATION"))
    X.table(doc, ["Report row", "Authority", "Channel class; portal", "Hand-off requirement", "Status; accuracy"], rows,
            [0.95, 1.25, 1.55, 4.0, 2.05], size=7)


def sec7(doc):
    X.h(doc, "7. Per-report hand-off register", 1)
    X.para(doc, S.clean(
        "One row per report row of the Report Specifications. The hand-off requirement is the rule the research found for "
        "that authority; the status and accuracy statement is the one of the Report Matrix."))
    reg_table(doc, FED_SPECS, "Federal returns, wage statements and corrections", "7.1")
    reg_table(doc, ["US-DOR-001"], "State withholding returns and deposits", "7.2")
    reg_table(doc, ["US-DOR-002"], "State annual reconciliation and W-2 copies", "7.3")
    reg_table(doc, ["US-UI-001"], "State UI quarterly wage reports", "7.4")
    reg_table(doc, ["US-SDNH-001"], "State new-hire reports", "7.5")
    reg_table(doc, ["US-PFML-001"], "State paid-leave, disability and long-term-care programme reports", "7.6")
    reg_table(doc, ["US-LOC-001", "US-LOC-002", "US-LOC-003"], "Local income, wage and city payroll tax returns", "7.7")
    reg_table(doc, ["US-DOR-003", "US-DOR-004", "US-WC-001"], "Nevada MBT, payroll transit levies and State-fund workers' compensation", "7.8")


def sec8(doc):
    X.h(doc, "8. Provider input data set", 1)
    X.para(doc, S.clean(
        "The minimum data a provider must receive, derived from the layouts read. Field names and types are owned by "
        f"{S.DD_REF}; the authority's own box and block identifiers are used here. Elements that accumulate payroll results "
        "(hours, weeks, wage totals) are produced by the payroll calculation and are listed because the provider needs them, "
        "not because the data dictionary holds them."))
    n = 0
    for grp, items in D.DATA_SET.items():
        n += 1
        X.h(doc, f"8.{n} {grp}", 2)
        rows = []
        for lab, need, key in items:
            S.at(f"8.{n} {lab}")
            f = S.fact(key)
            rows.append([lab, need, S.fv(key, with_cite=False), S.cite_f(f)])
        X.table(doc, ["Data element", "Needed for", "Statement", "Source"], rows, [1.9, 1.4, 2.7, 1.1], size=7.5)
    n += 1
    X.h(doc, f"8.{n} Inputs not carried by any filing", 2)
    X.para(doc, S.clean(
        "Three data elements of the data dictionary reach no authority filing and no provider hand-off: the employee primary "
        "language is an input of the employee notice template, the supplemental wage withholding method election is an input "
        "of the payroll calculation, and the Iowa school district of residence is an input of the individual assessment. "
        "They are therefore not part of the provider data set."))
    rows = []
    for el, (verdict, why, key) in D.DD_DISPOSITION.items():
        if verdict == "not_consumed":
            S.at(f"8.{n} {el}")
            rows.append([el, why, S.fv(key, with_cite=False), S.cite_f(S.fact(key))])
    X.table(doc, ["Data element", "Why it is not a provider input", "Statement", "Source"], rows, [1.8, 2.2, 2.0, 1.1], size=7.5)


def appendix_a(doc, used_rids):
    X.h(doc, "Appendix A. Sources", 1)
    X.para(doc, S.clean("Sources cited in this document, by register id."))
    rows = []
    for rid in sorted(used_rids):
        r = S.REG.get(rid, {})
        rows.append([rid, S.clean(r.get("authority", ""))[:70], r.get("instrument_type", "").replace("_", " "), urlparse(r.get("url", "")).netloc])
    X.table(doc, ["Register id", "Authority", "Instrument type", "Published on (host)"], rows, [1.0, 2.6, 1.5, 2.0], size=6.5)


def appendix_b(doc):
    X.h(doc, "Appendix B. Not configured in this release", 1)
    X.para(doc, S.clean("Each request number below appears in the cell it concerns; none blocks the document."))
    rows = []
    for key in sorted(S.GAPS):
        rq = REQ[key]
        rows.append([rq["gid"], rq["doc_what"], rq["doc_closes"]])
    X.table(doc, ["Request", "What is missing", "What would close it"], rows, [0.9, 3.4, 2.8], size=7.5)


REQ = {}
ERR_KEY = "sir.error_handling.catalogue.missing"
ACK_KEY = "sir.state.ack_response_times.missing"
TAIL = [ERR_KEY, ACK_KEY]          # ids after the research gaps, in this order (SIR-QA1-07)
SPECIAL = {
    ERR_KEY: dict(q=("Which authority publications list the reject, business-rule and resubmission rules per channel class (IRS e-file "
                     "business rules for Forms 94x, SSA EFW2 resubmission notices, State bulk-file error reports), or is error handling "
                     "an owner decision that belongs to the provider contract (US-MQ-09)?"),
                  what="Authority error-code catalogue per channel class (reject and business-rule lists)",
                  closes=("The authority reject / business-rule lists per channel class, or an owner decision that error handling "
                          "belongs to the provider contract (US-MQ-09)")),
    ACK_KEY: dict(q=("Which authority pages state the acknowledgement and response-time rules of State filing channels "
                     "(electronic acknowledgement, rejection notice and resubmission periods)?"),
                  what="State acknowledgement and response-time rules for electronic filings",
                  closes="The State authority pages that state acknowledgement and response times, saved and read"),
}


OPEN_LABEL = {
    "sir.provider.selection": "the choice of filing provider and its input layout",
    "sir.ny.withholding.agent_authorization": "the New York withholding authorisation form",
    "sir.me.withholding.agent_authorization": "the Maine withholding and UI authorisation forms",
    "sir.ms.withholding.agent_authorization": "the Mississippi withholding authorisation form",
    "sir.ky.agent_authorization": "the Kentucky withholding and UI authorisation instruments",
    "sir.la.withholding.agent_authorization": "the Louisiana withholding authorisation form",
    "sir.wy.ui.agent_authorization_form_text": "the text of the Wyoming UI power of attorney form",
    "sir.ca.de9c.file_spec": "the California electronic file layout of the quarterly wage detail",
    "sir.in.w2.xml_schema": "the Indiana W-2 XML schema",
    "sir.w2.state_specs_ty2026": "the tax-year State W-2 specification editions of eight jurisdictions",
    "sir.ui.file_specs_missing": "the UI wage-file layouts of eleven States",
    "sir.tx.ui.due_date": "the Texas UI quarterly due date",
    "sir.mi.new_hire.statute": "the Michigan new-hire statute and penalty",
    "fed.aca.efile_threshold.ty2026": "the 2026 electronic-filing threshold in the Instructions for Forms 1094-C and 1095-C",
    "rspec.fed.form940.due.ty2026": "the 2026 Form 940 due date in the 2026 Instructions for Form 940",
    "sir.fl.agent_authorization.rts9": "the Florida agent registration form RTS-9",
    "sir.ks.live_kw100_page": "the current Kansas Department of Revenue KW-100 withholding guide page",
    "sir.ma.agent_authorization.m2848": "the Massachusetts power of attorney form M-2848",
    "sir.ms.ui.agent_authorization.j9": "the Mississippi reporting agent authorisation form J-9",
    "sir.ne.agent_authorization.form33": "the Nebraska reporting agent form 33",
    "sir.nh.ui.tpa_registration": "the New Hampshire third-party administrator registration",
    "sir.oh.local.municipal.thresholds": "the Ohio municipal monthly-filing thresholds",
    "sir.oh.ui.agent_authorization.jfs20106": "the Ohio Form JFS-20106",
}


PLAIN_F44 = {"rspec.fed.form940.due": "the Form 940 due date rule in force from 2026-02-11"}


def make_requests():
    """One request per gap key; ids SIR-RQ-nn in sorted key order. Open questions keep the closing source of the facts."""
    unres = {u["key"]: u for u in S.UNRESOLVED}
    out = {}
    for i, key in enumerate(sorted(S.GAPS, key=lambda k: (k in TAIL, TAIL.index(k) if k in TAIL else 0, k)), start=1):
        g = S.GAPS[key]
        gid = f"SIR-RQ-{i:02d}"
        why = g.get("why")
        domain, tier = "statutory_reporting", "A.2"
        if key in SPECIAL:
            sp_ = SPECIAL[key]
            q, doc_what, closes, doc_closes = sp_["q"], sp_["what"], sp_["closes"], sp_["closes"]
            searched = ["_research/SIR-facts.json", "_research/RSPEC-facts.json", "00-official-sources/legal-basis-register.csv"]
        elif key in unres:
            u = unres[key]
            lab = OPEN_LABEL.get(key, key)
            q = f"What does the official source state for {lab}? Recorded reason: {u['why']}"
            doc_what = f"Not read: {lab}"
            closes = u["what_would_close_it"]
            doc_closes = closes
            searched = list(u.get("attempted") or []) + ["_research/SIR-facts.json unresolved[]"]
        elif why == "f44":
            miss = S.BLOCKED.get(key) or []
            els = ", ".join(f"{k} {e if not isinstance(e, (list, tuple)) else '-'.join(map(str, e))}" for k, e in miss[:6])
            f = S.fact(key)
            q = (f"Which official source row carries the wording of the statement recorded for {key} "
                 f"(text elements not found in the saved copy of {', '.join(S.rids(f))}: {els})?")
            closes = ("A saved copy of the cited authority page or form that contains these elements, or a corrected statement "
                      "with the row that carries it")
            doc_what = f"Statement for {PLAIN_F44.get(key) or jur_label(key)} whose wording is not proven in the saved copy of its source"
            doc_closes = "The authority page or form that carries the wording, saved and read"
            searched = [f"saved copies of {', '.join(S.rids(f))}", "same-jurisdiction rows of the register"]
        else:
            jurs = ", ".join(sorted(g["jurs"])) or "the jurisdictions concerned"
            q = (f"Which authority page or form states the instrument or channel recorded for {key} in {jurs}, "
                 "for 2026 and 2027 where published?")
            closes = "The authority's own page or form for each jurisdiction named, read on the official host"
            doc_what = f"No source recorded for {key.split('.')[-2].replace('_', ' ')} in: {jurs}"
            doc_closes = closes
            searched = ["_research/SIR-facts.json", "_research/RSPEC-facts.json", "00-official-sources/legal-basis-register.csv"]
        out[key] = dict(gid=gid, rq=f"RQ-{i:02d}", key=key, question=q, question_short=short(q, 230), closes=short(closes, 230),
                        doc_what=short(doc_what, 200), doc_closes=short(doc_closes, 200),
                        why=why, domain=domain, tier=tier, searched=searched, locations=g["locations"], jurs=sorted(g["jurs"]))
    return out


def jur_label(key):
    p = key.split(".")
    if len(p) > 2 and len(p[1]) == 2 and p[1].upper() in S.STATE_NAMES:
        return f"{S.state_name(p[1].upper())} ({'.'.join(p[2:]).replace('_', ' ')})"
    return ".".join(p[1:]).replace("_", " ")


def new_key_ok(key):
    return re.match(r"^[a-z][a-z0-9_]*(\.[a-z0-9_]+)+$", key) is not None


# ============================================================================= main ===
def assemble(final):
    S.USED.clear()
    S.GAPS.clear()
    RECON.clear()
    SPECROW_SIR.clear()
    doc = X.new_document(S.FOOTER, f"{S.COUNTRY} Statutory Integration Index {S.SIR_REF}")
    cover(doc)
    doc_control(doc)
    sec0(doc)
    sec1(doc)
    spec_register(doc)
    sec3(doc)
    sec4(doc)
    sec5(doc)
    sec6(doc)
    X.landscape_section(doc)
    sec7(doc)
    X.portrait_section(doc)
    sec8(doc)
    if final:
        used_rids = set()
        for (k, ef) in S.USED:
            f = S.fact(k) if S.has(k) else None
            if f:
                used_rids.update(S.rids(f))
        appendix_a(doc, used_rids)
        appendix_b(doc)
    return doc


def main():
    out = os.path.join(S.SIRDIR, S.FILENAME)
    if "--out" in sys.argv:
        out = sys.argv[sys.argv.index("--out") + 1]
    # open questions referenced from the places they concern (so that each has its request id and cell)
    S.GAP_IDS.clear()
    assemble(final=False)
    # make sure every open question of the facts is raised at least once
    for k in D.OPEN_KEYS:
        if k not in S.GAPS:
            S.at("0 open questions")
            S.gap(k, "open")
    REQ.clear()
    REQ.update(make_requests())
    for k, r in REQ.items():
        S.GAP_IDS[k] = r["gid"]
    doc = assemble(final=True)
    for k in D.OPEN_KEYS:
        if k not in S.GAPS:
            S.at("0 open questions")
            S.gap(k, "open")
    # pass 2 may have found the same gaps; the ids must be identical
    REQ2 = make_requests()
    assert {k: v["gid"] for k, v in REQ2.items()} == {k: v["gid"] for k, v in REQ.items()}, "gap ids changed between passes"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    if os.path.exists(out) and "--no-side" not in sys.argv:       # keep a copy of the previous build before it is replaced
        h = hashlib.md5(open(out, "rb").read()).hexdigest()[:8]
        bk = os.path.join(S.HERE, "_backup", f"{os.path.splitext(os.path.basename(out))[0]}.{h}.docx")
        if not os.path.exists(bk):
            shutil.copy2(out, bk)
    doc.save(out)
    if "--no-side" not in sys.argv:
        write_side_files(out)
        write_landscape()
    print("written", out)


def write_side_files(out):
    # bindings csv
    rows = []
    for (key, ef), locs in sorted(S.USED.items(), key=lambda x: (x[0][0], str(x[0][1]))):
        f = S.fact(key, ef) if S.has(key) else None
        if not f:
            continue
        for loc in sorted(locs):
            rows.append([loc, key, f["register_id"], ";".join(S.rids(f)[1:]), f.get("effective_from"), f["_file"]])
    p = os.path.join(S.BASE, "_pipeline", "SIR-bindings.csv")
    with open(p, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["location", "key", "register_id", "also_register_ids", "effective_from", "facts_file"])
        w.writerows(rows)
    # research request
    reqs = []
    for key, r in sorted(REQ.items(), key=lambda x: x[1]["gid"]):
        reqs.append({"id": r["rq"], "key": key if new_key_ok(key) else "sir.unspecified.missing",
                     "location": f"03-statutory-integrations/{S.FILENAME}!Appendix B!{r['gid']}",
                     "question": r["question"] if len(r["question"]) >= 20 else r["question"] + " (see the cell)",
                     "why_blocking": f"The hand-off cell {r['gid']} cannot state the requirement ("
                                     f"{'open question recorded with the facts' if (r['why'] in ('open', 'no_fact') and r['key'] in {u['key'] for u in S.UNRESOLVED}) else 'text not proven in the saved source' if r['why']=='f44' else 'no source recorded'}).",
                     "domain": r["domain"], "acceptable_tier": r["tier"], "attempted_by_requester": r["searched"],
                     "severity": "minor", "expected_shape": "the statement with the register row that carries it; effective date",
                     "_gap_id": r["gid"], "_cells": r["locations"][:6], "_jurisdictions": r["jurs"]})
    doc = {"schema_version": "1.4.0", "artifact": "SIR", "unit": "third_party_provider_handoff", "requested_by": "artifact-builder",
           "round": 1, "created_on": dt.date.today().isoformat(),
           "_note": "Requests of the SIR build, round 1. Every request is non-blocking; each has a cell reading "
                    "'Not configured in this release [[GAP:SIR-RQ-nn]]' and an entry in _research/gaps.json.",
           "requests": reqs}
    json.dump(doc, open(os.path.join(S.RESEARCH, "SIR-research-request.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    # gaps.json (C70): replace the SIR entries, keep every other entry untouched
    gp = os.path.join(S.RESEARCH, "gaps.json")
    g = json.load(open(gp, encoding="utf-8"))
    g["gaps"] = [x for x in g["gaps"] if not str(x.get("id", "")).startswith("SIR-RQ-")]
    for key, r in sorted(REQ.items(), key=lambda x: x[1]["gid"]):
        g["gaps"].append({"id": r["gid"], "key": key, "subject": f"{r['gid']} - {r['question_short']}",
                          "location": f"03-statutory-integrations/{S.FILENAME}!Appendix B!{r['gid']}",
                          "research_request_id": r["rq"], "blocking": False, "severity": "minor",
                          "searched": r["searched"], "searched_on": dt.date.today().isoformat(),
                          "what_would_close_it": r["closes"], "status": "open", "artifact": "SIR"})
    json.dump(g, open(gp, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    json.dump({k: {**v, "locations": v["locations"][:20]} for k, v in REQ.items()},
              open(os.path.join(S.CHECKS, "sir_requests.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    # recon
    os.makedirs(S.CHECKS, exist_ok=True)
    json.dump(RECON, open(os.path.join(S.SCRATCH, "recon_rows.json"), "w", encoding="utf-8"), indent=1)


LANDSCAPE_GROUPS = [("IRS", "Internal Revenue Service", "US-IRS-001 to US-IRS-008", "outbound"),
                    ("SSA", "Social Security Administration", "US-SSA-001", "outbound"),
                    ("STATE-REV", "State departments of revenue / taxation (50 States and the District of Columbia)",
                     "US-DOR-001 to US-DOR-004", "outbound"),
                    ("STATE-UI", "State workforce / unemployment insurance agencies", "US-UI-001", "outbound"),
                    ("STATE-PROG", "State programme agencies (paid leave, disability, workers' compensation)", "US-PFML-001; US-WC-001", "outbound"),
                    ("STATE-NH", "State Directories of New Hires", "US-SDNH-001", "outbound"),
                    ("LOCAL", "Local taxing authorities (cities, counties, school districts, collectors)", "US-LOC-001 to US-LOC-003", "outbound"),
                    ("INBOUND-DOCS", "Child-support agencies, IRS levy, State UI rate notices", "none (received, not filed)", "inbound")]
PROVIDER_NAME = "Third-party filing provider (owner decision US-MQ-09)"
PROVIDER_CHANNEL = "File hand-off of the provider input data set of section 8; product mapping required"


def landscape_groups(docx_mode):
    """Records of the integration landscape: the filing provider first, then one per authority group. In docx mode the
    cells carry tagged fact values (F44-gated); in JSON mode plain text of the same facts."""
    out = []
    S.at("0.4 provider")
    gap_txt = S.gap(D.PROVIDER_GAP_KEY, "no_fact")
    out.append(dict(code="FILING-PROVIDER", name=PROVIDER_NAME, integration=True, integration_txt="Yes", direction="out",
                    dir_txt="OUTBOUND", channel_txt=PROVIDER_CHANNEL, channel=PROVIDER_CHANNEL, portal_txt="Not applicable",
                    runbook_txt=gap_txt, keys=[], rids=["US-MQ-09"], specs="all Report Specifications"))
    for code, name, specs_, direction in LANDSCAPE_GROUPS:
        keys = [k for k in D.MACHINE_FACTS.get(code, []) if S.usable(k)[0]]
        S.at(f"0.4 {code}")
        if keys:
            keys = keys[:3]
            ch_docx = "; ".join(S.fv(k) for k in keys)
            ch_plain = "; ".join(f"{S.fact(k)['value']}" for k in keys)
            rids = sorted({r for k in keys for r in S.rids(S.fact(k))})
            out.append(dict(code=code, name=name, integration=True, integration_txt="Yes, operated by the filing provider",
                            direction="out", dir_txt="OUTBOUND", channel_txt=ch_docx, channel=ch_plain,
                            portal_txt="None recorded", runbook_txt="None; no Mercans runbook (provider operates the channel)",
                            keys=keys, rids=rids, specs=specs_))
        else:
            ch = ("Provider-transmitted portal, file upload or electronic return; no system-to-system channel recorded"
                  if direction == "outbound" else "Document received by the employer; not parsed by the engine")
            out.append(dict(code=code, name=name, integration=False, integration_txt="No", direction="none",
                            dir_txt=direction.upper(), channel_txt=ch, channel=ch, portal_txt="None recorded",
                            runbook_txt="None (no integration)", keys=[], rids=[], specs=specs_))
    return out


def write_landscape():
    """integration-landscape.json in the si-discovery schema (summary, notes, per authority: receives_payroll_data,
    integration, channel, directions, dev_portal, artefacts_public, source)."""
    sp = P.specs()
    grp = landscape_groups(docx_mode=False)
    prov_gid = S.GAP_IDS.get(D.PROVIDER_GAP_KEY, "SIR-RQ-00")
    auth = []
    for g in grp:
        e = {"code": g["code"], "name": g["name"],
             "receives_payroll_data": g["code"] != "INBOUND-DOCS",
             "integration": g["integration"], "channel": g["channel"], "directions": g["direction"],
             "dev_portal": None, "artefacts_public": (True if g["keys"] else None),
             "source": ("; ".join(g["rids"]) if g["rids"] else f"Report Specifications {g['specs']}; Report Matrix channel statements"),
             "report_specs": g["specs"], "runbook_location": None}
        if g["code"] == "FILING-PROVIDER":
            e.update(product_mapping_required=True, operated_by=None,
                     reason=f"P1-P7 runbook deferred until the provider is chosen [[GAP:{prov_gid}]]")
        elif g["integration"]:
            e.update(operated_by="filing provider (owner decision US-MQ-09)", product_mapping_required=True,
                     notes="Machine channel published by the authority; no Mercans runbook; the provider operates it.")
        else:
            e.update(product_mapping_required=(g["code"] != "INBOUND-DOCS"), notes="No system-to-system channel recorded for this group.")
        auth.append(e)
    n_int = sum(1 for g in grp if g["integration"])
    sentence = D.verdict_sentence().replace("[[GAP:SIR-RQ-00]]", f"[[GAP:{prov_gid}]]")
    doc = {"country": S.COUNTRY, "code": S.CODE, "year": S.YEAR, "package_version": S.PKG, "produced_by": "artifact-builder (SIR build)",
           "verdict": D.VERDICT,
           "verdict_rationale": sentence,
           "summary": (f"{D.VERDICT}: the single integrable party for Mercans is the third-party filing provider; {n_int - 1} authority groups "
                       "publish a machine channel (SFTP, web service or bulk file) that the provider operates. All other filings are "
                       "portal, upload or paper through the provider, and the inbound items are documents. The index records the "
                       "provider hand-off contract."),
           "notes": ["Provider runbook set deferred until the provider is chosen.",
                     "Authority entries with integration=true have no Mercans runbook; operated_by is the filing provider."],
           "provider_handoff": {"outbound_integrations": [x["name"] for x in S.SCOPE["integrations"]["outbound"]],
                                "inbound_integrations": [x["name"] for x in S.SCOPE["integrations"]["inbound"]],
                                "report_specs": [x["id"] for x in sp]},
           "authorities": auth}
    json.dump(doc, open(os.path.join(S.SIRDIR, "integration-landscape.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)


if __name__ == "__main__":
    main()
