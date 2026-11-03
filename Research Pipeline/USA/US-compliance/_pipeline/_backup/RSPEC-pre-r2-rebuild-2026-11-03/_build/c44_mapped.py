# -*- coding: utf-8 -*-
"""C44 on the filing -> spec crosswalk. The shared C44 matches a spec to a filing only when the
filing_id IS a document id, which the US scope ids are not, so it SKIPs; this applies the same
format-family rule (shared FAMILIES / families()) through the crosswalk below and checks that every
in-scope filing has exactly one spec. usage: python c44_mapped.py [--json out.json]"""
import glob
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SPECS = os.path.dirname(HERE)
BASE = os.path.dirname(SPECS)
_s = importlib.util.spec_from_file_location("ccs", os.path.expanduser(
    "~/mercans-pipeline/shared/consistency-checks/consistency_checks.py"))
CCS = importlib.util.module_from_spec(_s)
_s.loader.exec_module(CCS)

CROSSWALK = ["US-IRS-001", "US-IRS-002", "US-IRS-003", "US-IRS-004", "US-IRS-005", "US-SSA-001", "US-IRS-006",
             "US-IRS-007", "US-IRS-008", "US-DOR-001", "US-DOR-002", "US-UI-001", "US-PFML-001", "US-LOC-001",
             "US-LOC-002", "US-LOC-003", "US-DOR-003", "US-DOR-004", "US-WC-001", "US-SDNH-001"]


def main():
    sm = json.load(open(os.path.join(BASE, "scope_manifest.json"), encoding="utf-8"))
    fil = sm["authority_filings"]["in_scope"]
    specs = {CCS.doc_id_of(p): p for p in glob.glob(os.path.join(SPECS, "*-Spec.xlsx"))}
    rows, problems = [], []
    if len(fil) != len(CROSSWALK):
        problems.append(f"{len(fil)} in-scope filings vs {len(CROSSWALK)} crosswalk entries")
    for f, did in zip(fil, CROSSWALK):
        p = specs.get(did)
        if not p:
            problems.append(f"{f['filing_id']}: spec {did} missing")
            continue
        sf = CCS.spec_format(p)
        mpos, mneg = CCS.families(f.get("format"))
        spos, sneg = CCS.families(sf)
        why = []
        if mpos & sneg:
            why.append(f"manifest says {sorted(mpos & sneg)}, the spec says NOT")
        if spos and mpos and not mpos <= spos:
            why.append(f"manifest {sorted(mpos)} not all in spec {sorted(spos)}")
        status = "FAIL" if why else ("PASS" if mpos else "PASS (manifest format names no family)")
        if why:
            problems.append(f"{f['filing_id']} -> {did}: " + "; ".join(why))
        rows.append({"filing_id": f["filing_id"], "spec": did, "manifest_format": f.get("format"),
                     "manifest_families": sorted(mpos), "spec_families": sorted(spos), "status": status})
    extra = sorted(set(specs) - set(CROSSWALK))
    if extra:
        problems.append(f"specs without a filing: {extra}")
    rep = {"check": "C44 (crosswalk)", "status": "FAIL" if problems else "PASS", "filings": len(fil),
           "specs": len(specs), "problems": problems, "rows": rows}
    sys.stdout.reconfigure(encoding="utf-8")
    print(json.dumps({k: v for k, v in rep.items() if k != "rows"}, indent=1, ensure_ascii=False))
    for r in rows:
        print(r["spec"], r["status"], r["manifest_families"], r["spec_families"])
    if "--json" in sys.argv:
        json.dump(rep, open(sys.argv[sys.argv.index("--json") + 1], "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
