# -*- coding: utf-8 -*-
"""Re-run every CCG unit generator in dependency order, then the DOCX assembler (round 2+).

Every unit .md in 01-ccg/modules and 01-ccg/annexes is generated; never hand-edit it.
Re-run this after any facts / gaps / request change (e.g. a browser worker adding State facts).

usage: python rebuild_all.py [--no-docx]
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
ENV = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONUTF8="1")
J = lambda *p: os.path.join(BASE, *p)  # noqa: E731

STEPS = [
    ("examples m01-m07", [J("01-ccg", "_examples", "build_examples_m01_m07.py")]),
] + [(f"m0{i}", [J("01-ccg", "_build-m01-m07", f"build_m0{i}.py")]) for i in range(1, 8)] + [
    ("examples m12 / m09", [J("01-ccg", "_examples", "build_examples.py")]),
    ("m08-m13 + coverage", [J("01-ccg", "_build", "m08_m13", "build_m08_m13.py")]),
    ("annexes FED-CT", [J("01-ccg", "_scratch", "annex-FED-CT", "build_annexes.py")]),
    ("examples DC-MA", [J("01-ccg", "_scratch", "annex-DC-MA", "build_examples_annex_DC-MA.py"), BASE]),
    ("annexes DC-MA", [J("01-ccg", "_scratch", "annex-DC-MA", "build_annexes.py"), BASE,
                       "DC,DE,FL,GA,HI,IA,ID,IL,IN,KS,KY,LA,MA"]),
    ("annexes MD-NV", [J("_research", "synthesis-B", "_scratch-ccg-build-MD-NV", "build_annexes.py"), BASE]),
    ("annexes NY-WY", [J("01-ccg", "_build-annex-NY-WY", "build.py")]),
]
if "--no-docx" not in sys.argv:
    STEPS.append(("assemble DOCX", [J("01-ccg", "_build", "assemble", "build_ccg_docx.py"), BASE]))

for name, cmd in STEPS:
    r = subprocess.run([sys.executable] + cmd, cwd=os.path.dirname(cmd[0]), env=ENV,
                       capture_output=True, text=True, encoding="utf-8")
    tail = (r.stdout or "").strip().splitlines()[-1:] or [""]
    print(f"[{'OK' if r.returncode == 0 else 'FAIL'}] {name}: {tail[0][:150]}")
    if r.returncode:
        print(r.stderr[-3000:])
        sys.exit(1)
