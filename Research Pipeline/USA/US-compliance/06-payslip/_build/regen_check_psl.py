# -*- coding: utf-8 -*-
"""C71: rebuild the payslip from the generator into a scratch path (no side files) and compare with the issued workbook.
Every part of the package is compared byte for byte. 0 differences required."""
import os
import subprocess
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
PSLDIR = os.path.dirname(HERE)
FN = "US_Compliance_Payslip_Generator.xlsx"
tmp = os.path.join(HERE, "_scratch", "regen.xlsx")
r = subprocess.run([sys.executable, "-I", os.path.join(HERE, "build_psl.py"), "--out", tmp, "--no-side"], capture_output=True, text=True)
if r.returncode:
    print(r.stdout, r.stderr)
    sys.exit(2)
a, b = zipfile.ZipFile(os.path.join(PSLDIR, FN)), zipfile.ZipFile(tmp)
diff = []
for n in sorted(set(a.namelist()) | set(b.namelist())):
    if n not in a.namelist() or n not in b.namelist() or a.read(n) != b.read(n):
        diff.append(n)
print(f"C71: {len(diff)} differences" + (": " + ", ".join(diff) if diff else ""))
sys.exit(1 if diff else 0)
