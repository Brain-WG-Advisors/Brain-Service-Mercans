# -*- coding: utf-8 -*-
"""Build every US Report Specification.

usage: python build_specs.py [--out <dir>] [--only US-IRS-001,...] [--bindings <csv>]
Default --out is 04-reports-spec/. The script is the only source of the workbooks (C71).
"""
import argparse
import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import us_common as C  # noqa: E402
import us_book  # noqa: E402
import us_federal as FED  # noqa: E402
import us_fed_annual as FA  # noqa: E402
import us_fed_info as FI  # noqa: E402
import us_state as ST  # noqa: E402
import us_w2 as W2  # noqa: E402

BUILDERS = [
    FED.irs_941, FA.irs_944, FA.irs_943, FA.irs_940, FA.irs_schedule_h, W2.ssa_w2, FI.irs_1042s,
    FI.irs_aca, FI.irs_941x,
    ST.dor_withholding, ST.dor_annual, ST.ui_wage, ST.pfml, ST.local_tax, ST.city_employer, ST.seattle,
    ST.nv_mbt, ST.transit, ST.workers_comp, ST.new_hire,
]


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=C.SPECS)
    ap.add_argument("--only", default="")
    ap.add_argument("--bindings", default="")
    a = ap.parse_args(argv)
    os.makedirs(a.out, exist_ok=True)
    only = {x.strip() for x in a.only.split(",") if x.strip()}
    paths = []
    for b in BUILDERS:
        d = b()
        if only and d["doc_id"] not in only:
            continue
        paths.append(us_book.write(d, a.out))
    if a.bindings:
        with open(a.bindings, "w", encoding="utf-8", newline="") as fh:
            w = csv.writer(fh)
            w.writerow(["location", "key", "register_id", "effective_from", "facts_file"])
            for kk in sorted(C.USED):
                k, _, per = kk.partition("@")
                f = C.fact(k, per or None)
                for loc in sorted(C.USED[kk]):
                    w.writerow([loc, k, f["register_id"], f.get("effective_from"), f["_file"]])
    for p in paths:
        print(os.path.basename(p))
    return 0


if __name__ == "__main__":
    sys.exit(main())
