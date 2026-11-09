# -*- coding: utf-8 -*-
"""C71: rebuild the SIR from the generator into a scratch path (no side files) and compare with the issued document.
Every part of the package is compared byte for byte except docProps/core.xml (timestamps). 0 differences required."""
import os
import subprocess
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
SIRDIR = os.path.dirname(HERE)
FN = "US-SIR-INDEX-001-v1.0.docx"
tmp = os.path.join(HERE, "_scratch", "regen.docx")
r = subprocess.run([sys.executable, "-I", os.path.join(HERE, "build_sir.py"), "--out", tmp, "--no-side"], capture_output=True, text=True)
if r.returncode:
    print(r.stdout, r.stderr)
    sys.exit(2)
a, b = zipfile.ZipFile(os.path.join(SIRDIR, FN)), zipfile.ZipFile(tmp)
diff = []
for n in sorted(set(a.namelist()) | set(b.namelist())):
    if n == "docProps/core.xml":
        continue
    if n not in a.namelist() or n not in b.namelist() or a.read(n) != b.read(n):
        diff.append(n)
print(f"C71: {len(diff)} differences" + (": " + ", ".join(diff) if diff else ""))
sys.exit(1 if diff else 0)
