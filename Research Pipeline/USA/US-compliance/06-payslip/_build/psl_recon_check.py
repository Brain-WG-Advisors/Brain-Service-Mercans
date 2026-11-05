# -*- coding: utf-8 -*-
"""Payslip reconciliation: every payslip line maps to a WTC wage type (code) and to its DD fields or to an explained
payroll-result reason; every PSL fact is placed in the workbook. 0 unmapped required. Reads checks/psl_recon.csv."""
import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import psl_common as S  # noqa: E402
import psl_content as K  # noqa: E402

rows = list(csv.DictReader(open(os.path.join(S.CHECKS, "psl_recon.csv"), encoding="utf-8")))
bad = [r for r in rows if r["status"].startswith("UNMAPPED")]
cat = {r["wtc_code"] for r in rows if r["kind"] == "CATALOGUE_LINE"}
want = {c for c, *_ in K.catalogue()}
miss_cat = sorted(want - cat)
import csv as _c
bind = list(_c.DictReader(open(os.path.join(S.BASE, "_pipeline", "PSL-bindings.csv"), encoding="utf-8")))
used = {b["key"] for b in bind}
gaps = set(S.json.loads(open(os.path.join(S.CHECKS, "psl_requests.json"), encoding="utf-8").read())) if hasattr(S, "json") else set()
import json
gaps = set(json.load(open(os.path.join(S.CHECKS, "psl_requests.json"), encoding="utf-8")))
unplaced = sorted(f["key"] for f in S.PSLFACTS["facts"] if f["key"] not in used and f["key"] not in gaps)
print(f"recon rows {len(rows)}; UNMAPPED {len(bad)}; payslip lines of the crosswalk missing {len(miss_cat)}; PSL facts not placed {len(unplaced)}")
for r in bad[:10]:
    print("UNMAPPED", r["id"], r["status"])
for k in unplaced[:10]:
    print("UNPLACED", k)
sys.exit(1 if bad or miss_cat or unplaced else 0)
