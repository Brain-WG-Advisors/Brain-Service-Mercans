# -*- coding: utf-8 -*-
"""C71 for the Data Dictionary: regenerate = issued. Rebuilds the workbook into a temp folder with the build command
of 05-data-dictionary/dd_checks.json and compares it, cell for cell, with the delivered workbook."""
import json
import os
import subprocess
import sys
import tempfile

from openpyxl import load_workbook

HERE = os.path.dirname(os.path.abspath(__file__))
DDDIR = os.path.dirname(HERE)
cfg = json.load(open(os.path.join(DDDIR, "dd_checks.json"), encoding="utf-8"))
name = cfg["workbook"]
ref = os.path.join(DDDIR, name)
with tempfile.TemporaryDirectory() as tmp:
    cmd = [c.replace("{out}", tmp) for c in cfg["build_command"]]
    r = subprocess.run(cmd, cwd=DDDIR, capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        print("C71 FAIL: build command failed", r.stderr[-400:])
        sys.exit(1)
    a, b = load_workbook(ref), load_workbook(os.path.join(tmp, name))
    diffs = []
    if a.sheetnames != b.sheetnames:
        diffs.append(f"sheets {a.sheetnames} != {b.sheetnames}")
    for sn in a.sheetnames:
        x, y = a[sn], b[sn]
        if sorted(map(str, x.merged_cells.ranges)) != sorted(map(str, y.merged_cells.ranges)):
            diffs.append(f"[{sn}] merged ranges differ")
        for i in range(1, max(x.max_row, y.max_row) + 1):
            for j in range(1, max(x.max_column, y.max_column) + 1):
                u, v = x.cell(i, j).value, y.cell(i, j).value
                if u != v:
                    diffs.append(f"[{sn}]{x.cell(i, j).coordinate}: {str(u)[:50]!r} != {str(v)[:50]!r}")
    res = dict(check="C71", status="PASS" if not diffs else "FAIL", file=name, differences=len(diffs), details=diffs[:20])
    print(json.dumps(res, indent=1))
    sys.exit(0 if not diffs else 1)
