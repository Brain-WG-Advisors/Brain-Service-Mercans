# -*- coding: utf-8 -*-
"""SIR x RSPEC x DD reconciliation -> checks/sir_recon.csv.

  REPORT_ROW  every Report Matrix row of the 20 Report Specs has a hand-off row in the SIR (channel, authorisation, due date),
              with the DD elements its Report Spec cites; UNMAPPED = 0 required
  SPEC        every Report Spec is in the outbound register with direction OUTBOUND (the Report Type of the spec)
  SIR_ROW     every hand-off row of the SIR names a Report Matrix row that exists (reverse direction)
  DD_ELEMENT  every DD element has a consumer: a Report Spec row, the WTC, or this SIR (the DD fact tagged in the document);
              an element consumed by none is listed with the reason it is not a filing input
usage: python sir_recon.py -> checks/sir_recon.csv and a one-line summary
"""
import csv
import json
import os
import re
import sys

import docx

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import sir_common as S  # noqa: E402
import sir_defs as D  # noqa: E402
import sir_specs as P  # noqa: E402

TAG = re.compile(r"\[\[FACT:([A-Za-z0-9_.]+)=")


def main():
    d = docx.Document(os.path.join(S.SIRDIR, S.FILENAME))
    cells = []
    for t in d.tables:
        for r in t.rows:
            hdr0 = t.rows[0].cells[0].text.strip()
            cells.append((hdr0, [c.text for c in r.cells]))
    bound = set()
    for _h, cs in cells:
        for c in cs:
            bound.update(TAG.findall(c))
    for p in d.paragraphs:
        bound.update(TAG.findall(p.text))
    rows_in_doc = {cs[0].strip(): cs for h, cs in cells if h == "Report row" and cs[0].strip() != "Report row"}
    reg = {cs[0].strip(): cs for h, cs in cells if h == "Report Spec" and cs[0].strip() != "Report Spec"}
    # DD elements per spec
    dd_by_spec = {}
    for r in csv.DictReader(open(os.path.join(S.BASE, "05-data-dictionary", "_build", "checks", "rspec_dd_recon.csv"), encoding="utf-8")):
        for e in (r["dd_elements"] or "").split(" | "):
            if e.strip():
                dd_by_spec.setdefault(r["spec"], set()).add(e.strip())
    out, unmapped = [], 0
    spec_rows = {r["row_id"]: (s["id"], r) for s in P.specs() for r in s["rows"]}
    for rid, (sid, r) in spec_rows.items():
        cs = rows_in_doc.get(rid)
        st = "MAPPED" if cs else "UNMAPPED"
        if not cs:
            unmapped += 1
        gaps = re.findall(r"SIR-RQ-\d+", cs[3]) if cs else []
        rs_ids = sorted(r.get("rspec_gap_ids") or [])
        in_sir = sorted(set(re.findall(r"RSPEC-(?:GAP|RQ)-\d+", cs[4]))) if cs else []
        gid_ok = bool(cs) and rs_ids == in_sir
        if cs and not gid_ok:
            unmapped += 1
        out.append(dict(kind="REPORT_ROW", item=rid, spec=sid, sir_location=("section " + str(cs and "7") if cs else ""),
                        channel=(r["channel"] or ""), dd_elements=" | ".join(sorted(dd_by_spec.get(sid, []))),
                        status=st + ("_LIMITATION" if gaps and not re.search(r"\[\[FACT:", cs[3]) else ""),
                        note=" ".join(sorted(set(gaps))), rspec_gap_ids=" | ".join(rs_ids), sir_rspec_gap_ids=" | ".join(in_sir),
                        gap_id_equal="YES" if gid_ok else "NO"))
    for rid in rows_in_doc:
        if rid not in spec_rows:
            unmapped += 1
            out.append(dict(kind="SIR_ROW", item=rid, spec="", sir_location="section 7", channel="", dd_elements="",
                            status="UNMAPPED", note="hand-off row without a Report Matrix row"))
    for s in P.specs():
        cs = reg.get(s["id"])
        ok = bool(cs) and cs[1].strip() == "OUTBOUND" and "outbound" in s["rtype"].lower()
        if not ok:
            unmapped += 1
        out.append(dict(kind="SPEC", item=s["id"], spec=s["id"], sir_location="section 2.1", channel=(cs[4] if cs else ""),
                        dd_elements=" | ".join(sorted(dd_by_spec.get(s["id"], []))), status="MAPPED" if ok else "UNMAPPED",
                        note=f"direction OUTBOUND = Report Type of the spec: {s['rtype'][:60]}"))
    # DD elements
    usage = list(csv.DictReader(open(os.path.join(S.BASE, "05-data-dictionary", "_build", "checks", "dd_element_usage.csv"), encoding="utf-8")))
    wtc = list(csv.DictReader(open(os.path.join(S.BASE, "02-wtc", "_build", "checks", "wtc_recon.csv"), encoding="utf-8")))
    wtc_cons = set()
    for r in wtc:
        if r["direction"] == "WTC->DD":
            wtc_cons.add(r["detail"])
            wtc_cons.update(x.strip() for x in (r["mapped_to"] or "").split(" | "))
        elif r["direction"] == "DD->WTC" and r["status"] == "MAPPED":
            wtc_cons.add(r["item"])
    no_cons = 0
    for u in usage:
        el = u["dd_element"]
        n_spec = int(u["spec_rows"] or 0)
        if n_spec:
            out.append(dict(kind="DD_ELEMENT", item=el, spec=u["spec_ids_citing"], sir_location="via the Report Spec rows of section 7",
                            channel="", dd_elements=el, status="CONSUMED_BY_SPEC", note=""))
            continue
        if el in wtc_cons:
            out.append(dict(kind="DD_ELEMENT", item=el, spec="", sir_location="", channel="", dd_elements=el,
                            status="CONSUMED_BY_WTC", note="mapped in the WTC reconciliation"))
            continue
        disp = D.DD_DISPOSITION.get(el)
        if not disp:
            no_cons += 1
            out.append(dict(kind="DD_ELEMENT", item=el, spec="", sir_location="", channel="", dd_elements=el,
                            status="NO_CONSUMER", note="not mapped in the Report Specs, the WTC or the SIR"))
            continue
        verdict, why, key = disp
        if verdict == "inbound":
            out.append(dict(kind="DD_ELEMENT", item=el, spec="", sir_location="section 1.2 (inbound register)", channel="",
                            dd_elements=el, status="CONSUMED_BY_SIR", note=why))
            continue
        if verdict == "consumed":
            ok = key in bound
            if not ok:
                no_cons += 1
            out.append(dict(kind="DD_ELEMENT", item=el, spec="", sir_location="section 8 (provider input data set)", channel="",
                            dd_elements=el, status="CONSUMED_BY_SIR" if ok else "NO_CONSUMER", note=f"{why}; DD fact {key}"))
        else:
            ok = key in bound
            out.append(dict(kind="DD_ELEMENT", item=el, spec="", sir_location="section 8 (inputs not carried by any filing)", channel="",
                            dd_elements=el, status="NOT_A_FILING_INPUT" if ok else "NO_CONSUMER", note=f"{why}; DD fact {key}"))
            if not ok:
                no_cons += 1
    os.makedirs(S.CHECKS, exist_ok=True)
    with open(os.path.join(S.CHECKS, "sir_recon.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["kind", "item", "spec", "sir_location", "channel", "dd_elements", "status", "note", "rspec_gap_ids", "sir_rspec_gap_ids", "gap_id_equal"], restval="")
        w.writeheader()
        w.writerows(out)
    import collections
    c = collections.Counter((r["kind"], r["status"]) for r in out)
    print("recon rows", len(out), dict(c))
    print(f"UNMAPPED {unmapped}; DD elements with no consumer {no_cons}")
    return 1 if unmapped or no_cons else 0


if __name__ == "__main__":
    sys.exit(main())
