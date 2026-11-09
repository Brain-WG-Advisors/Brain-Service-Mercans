# -*- coding: utf-8 -*-
"""C71: rebuild the catalogue in a temp folder (no sidecars) and compare it cell by cell with the issued workbook."""
import os
import sys
import tempfile

from openpyxl import load_workbook

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_wtc as B  # noqa: E402
import wtc_common as W  # noqa: E402


def cells(p):
    wb = load_workbook(p)
    return {ws.title: [[c.value for c in r] for r in ws.iter_rows()] for ws in wb.worksheets}


if __name__ == "__main__":
    tmp = tempfile.mkdtemp()
    B.build(tmp, sidecars=False)
    a, b = cells(os.path.join(W.WTCDIR, W.FILENAME)), cells(os.path.join(tmp, W.FILENAME))
    diff = 0
    for k in a:
        if a[k] != b.get(k):
            diff += 1
            print("DIFF sheet", k)
    print("C71", "PASS" if diff == 0 and a.keys() == b.keys() else "FAIL", "sheets", len(a), "differences", diff)
