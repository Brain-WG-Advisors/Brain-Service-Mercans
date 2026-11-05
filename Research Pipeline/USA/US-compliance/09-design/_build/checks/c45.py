# -*- coding: utf-8 -*-
"""Gate reachability of the US design: every LESS / GREATER / EQUALS gate on a flag compares it with a value the flag can take.
Runs the shared check and an own stricter pass (undeclared flags, flags with more than six values, unit errors, forward reads).
usage: python c45.py   -> checks/c45.json ; exit 1 on any dead or undeclared gate."""
import glob
import importlib.util
import json
import os
import re
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
spec = importlib.util.spec_from_file_location("ccs", os.path.expanduser("~/mercans-pipeline/shared/consistency-checks/consistency_checks.py"))
CCS = importlib.util.module_from_spec(spec)
spec.loader.exec_module(CCS)

path = glob.glob(os.path.join(BASE, "09-design", "US_Regulation_Design_v*.md"))[0]
lines = open(path, encoding="utf-8").read().splitlines()

# own domain parse: every flag row of Part 1 (any number of values)
dom = {}
in1 = False
for ln in lines:
    if ln.startswith("## PART 1"):
        in1 = True
        continue
    if ln.startswith("## PART 2"):
        in1 = False
    if in1:
        m = re.match(r"^\|\s*(\d{5})\s*\|", ln)
        if m:
            cells = [c.strip() for c in ln.strip().strip("|").split("|")]
            vals = {float(v) for v in re.findall(r"(?:^|[\s,;(])(-?\d+)\s*=\s*\S", cells[3])}
            dom[m.group(1)] = vals
GATE = re.compile(r"\b(LESS|GREATER|EQUALS|NOT_EQUALS|LESS_OR_EQUAL|GREATER_OR_EQUAL)\(\s*\$(\d+)\s*;\s*(-?\d+(?:\.\d+)?)\s*\)")
dead, undeclared, nodomain, n = [], [], [], 0
for i, ln in enumerate(lines, 1):
    for m in GATE.finditer(ln):
        n += 1
        op, fid, c = m.group(1), m.group(2), float(m.group(3))
        if fid not in dom:
            undeclared.append({"line": i, "gate": m.group(0)})
        elif not dom[fid]:
            nodomain.append({"line": i, "gate": m.group(0), "why": "flag without declared values"})
        elif not CCS.reachable(op, dom[fid], c):
            dead.append({"line": i, "gate": m.group(0), "values": sorted(dom[fid])})
# a flag read as $58xxx that is not declared in Part 1 nor an account of Part 2
accts = set(re.findall(r"^\|\s*(585\d\d)\s*\|", "\n".join(lines), re.M))
reads_bad = []
for i, ln in enumerate(lines, 1):
    for fid in re.findall(r"\$(584\d\d)\b", ln):
        if fid not in dom:
            reads_bad.append({"line": i, "flag": fid})
    for fid in re.findall(r"\$(585\d\d)\b", ln):
        if fid not in accts:
            reads_bad.append({"line": i, "account": fid})
# strict pass (auditor level): every declared flag with values is used by a gate unless it is a [SOURCE] flag; every gate flag is named in the
# prose "Reads" of the regulation section that holds the gate
src_flags = set(re.findall(r"^\|\s*(\d{5})\s*\|[^|]*\|[^|]*\*\*\[SOURCE\]\*\*", "\n".join(lines), re.M))
gated = set()
sec, incode, sec_flags_gate, sec_prose = None, False, {}, {}
for ln in lines:
    if ln.startswith("```"):
        incode = not incode
        continue
    if ln.startswith("### ") or ln.startswith("## "):
        sec = ln
        continue
    if sec is None:
        continue
    if incode:
        for m in GATE.finditer(ln):
            gated.add(m.group(2))
            sec_flags_gate.setdefault(sec, set()).add(m.group(2))
    else:
        sec_prose.setdefault(sec, "")
        sec_prose[sec] += " " + ln
unused = sorted(f for f, v in dom.items() if v and f not in gated and f not in src_flags)
unnamed = []
for sc, fl in sec_flags_gate.items():
    for f in sorted(fl):
        if f not in sec_prose.get(sc, ""):
            unnamed.append({"section": sc[:60], "flag": f})
shared = CCS.c45(BASE, "US", [path])
rep = {"file": os.path.basename(path), "flags_declared": len(dom), "gates": n, "dead": dead, "undeclared": undeclared,
       "no_domain": nodomain, "unused_flags": unused, "gate_flag_not_in_reads": unnamed, "reads_undeclared": reads_bad, "shared": shared}
json.dump(rep, open(os.path.join(HERE, "c45.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
bad = dead or undeclared or nodomain or reads_bad or unused or unnamed or shared["status"] != "PASS"
print(f"unused flags {unused}  unnamed {len(unnamed)}")
print(f"flags {len(dom)}  gates {n}  dead {len(dead)}  undeclared {len(undeclared)}  reads undeclared {len(reads_bad)}  shared {shared['status']} "
      f"(checked {shared.get('conditions_checked')}, dead {shared.get('dead')}, unit {shared.get('unit_errors')}, forward {shared.get('forward_refs')})")
for x in (dead + undeclared + nodomain + reads_bad)[:20]:
    print(x)
sys.exit(1 if bad else 0)
