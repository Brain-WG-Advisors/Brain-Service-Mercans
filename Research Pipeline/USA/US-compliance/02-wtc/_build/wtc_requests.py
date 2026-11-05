# -*- coding: utf-8 -*-
"""Write _research/WTC-research-request.json (contract 1.4.0) and the WTC limitation entries of _research/gaps.json (C70)."""
import json
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import wtc_common as W  # noqa: E402

REL = f"02-wtc/{W.FILENAME}"
# Review r1 item 16: the status reads the same everywhere (facts blocking = true). key -> impact on the WTC.
BLOCKING = {"dc.sit.method.2026": "none: catalogue carries no method", "ut.sit.schedule.effective_date": "D412 dating"}


def main():
    reqs, entries = [], []
    for gid in sorted(W.GAPS):
        d = W.GAPS[gid]
        if gid not in W.GAP_USED:
            continue
        locs = sorted(W.GAP_USED[gid])
        n = gid.split("-")[-1]
        key = d["key"]
        reqs.append(dict(
            id=f"RQ-{n}", key=key, location=f"{REL}!{locs[0]}",
            question=f"What closes the limitation: {d['subject']}?",
            why_blocking="Documented limitation: the cell states it in the neutral wording 'Not configured in this release' and no value is written.",
            domain=d["domain"], acceptable_tier="A.2", severity=d["severity"],
            expected_shape=d["close"], attempted_by_requester=["_research/WTC-global_baseline-facts.json and WTC-country_specific-facts.json (unresolved and facts)"],
            _status="documented_limitation", _cells=len(locs), _facts_blocking=bool(d.get("facts_blocking"))))
        if key in BLOCKING:
            reqs[-1]["_blocking"] = True
            reqs[-1]["why_blocking"] = "Blocking per the facts and review r1. Impact on the catalogue: " + BLOCKING[key] + "."
            reqs[-1]["_wtc_impact"] = BLOCKING[key]
        entries.append(dict(
            id=gid, key=key, subject=f"{gid} - {d['subject']}", location=f"{REL} (see _research/WTC-research-request.json RQ-{n})",
            research_request_id=gid, blocking=key in BLOCKING, severity=d["severity"],
            searched=["_research/WTC-global_baseline-facts.json and WTC-country_specific-facts.json (facts and unresolved)",
                      "00-official-sources/legal-basis-register.csv"], searched_on="2026-11-03", what_would_close_it=d["close"],
            status="documented_limitation", reason="not carried by the research facts at the build date", closure_source=d["close"],
            decided_by="WTC build r1"))
        if key in BLOCKING:
            entries[-1]["_wtc_impact"] = BLOCKING[key]
    doc = dict(schema_version="1.4.0", artifact="WTC", unit="catalogue", requested_by="artifact-builder", round=1, created_on="2026-11-03",
               _note="Open points of the WTC build round 1. None blocks the artifact except those marked blocking (WTC-RQ-25 none for the catalogue, WTC-RQ-42 D412 dating); each is a documented limitation written as 'Not configured in this release [[GAP:WTC-RQ-nn]]'. "
                     "Items WTC-RQ-20 upward are open items of the facts; _facts_blocking marks those the facts file flags as blocking.",
               requests=reqs)
    json.dump(doc, open(os.path.join(W.RESEARCH, "WTC-research-request.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    gp = os.path.join(W.RESEARCH, "gaps.json")
    bk = os.path.join(W.BACKUP, "gaps.json.bak")
    if not os.path.exists(bk):
        shutil.copy(gp, bk)
    g = json.load(open(gp, encoding="utf-8"))
    g["gaps"] = [x for x in g["gaps"] if not str(x.get("id", "")).startswith("WTC-RQ-")] + entries
    json.dump(g, open(gp, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print("requests", len(reqs), "gaps.json entries", len(entries))


if __name__ == "__main__":
    main()
