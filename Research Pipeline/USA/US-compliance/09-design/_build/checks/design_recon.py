# -*- coding: utf-8 -*-
"""Reconciliation design x WTC x DD x register, read from the finished markdown (not from the generator).
Writes checks/design_recon.csv (one row per distinct reference) and prints the unmapped count (must be 0).
Also: every flag account of the design is a number that is not a WTC code; every regulation id is used in Parts 3 and 4."""
import csv
import glob
import json
import os
import re
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
import design_common as C  # noqa: E402

path = glob.glob(os.path.join(C.BASE, "09-design", "US_Regulation_Design_v*.md"))[0]
text = open(path, encoding="utf-8").read()
lines = text.splitlines()
rows = []


def add(kind, ref, where, found, detail=""):
    rows.append([kind, ref, where, "mapped" if found else "UNMAPPED", detail])


loc = {}
for i, ln in enumerate(lines, 1):
    for m in re.finditer(r"\bUS-(\d{3})\b", ln):
        code = f"US-{m.group(1)}"
        loc.setdefault(("WTC", code), i)
    for m in re.finditer(r"WTC `(\d{5})`", ln):
        loc.setdefault(("WTC", m.group(1)), i)
    if ln.startswith("| ") and re.search(r"\| (Deduction|Earning|Tax|Employer Contribution|Notional|Flag|Base|Intermediary|Percentage) \|", ln):
        for m in re.finditer(r"`(\d{5}|US-\d{3})`", ln):
            loc.setdefault(("WTC", m.group(1)), i)
    for m in re.finditer(r"DD:`([^`]+)`", ln):
        loc.setdefault(("DD", m.group(1)), i)
    for m in re.finditer(r"\[(US-[A-Z0-9]+-\d+)\]", ln):
        loc.setdefault(("REG", m.group(1)), i)
    for m in re.finditer(r"\[\[GAP:([A-Za-z0-9_.-]+)\]\]", ln):
        loc.setdefault(("GAP", m.group(1)), i)
# ranges: expand `US-aaa` to `US-bbb`
for m in re.finditer(r"`(US-\d{3})` to `(US-\d{3})`", text):
    a, b = int(m.group(1)[3:]), int(m.group(2)[3:])
    for n in range(a, b + 1):
        loc.setdefault(("WTC", f"US-{n:03d}"), 0)
for m in re.finditer(r"`(US-\d{3})` to `(US-\d{3})` \(\d+\)", text):
    pass
# Part 5 ranges of global codes: first and last code of a group, expanded through the catalogue order
for m in re.finditer(r"`(\d{5})` to `(\d{5})` \((\d+)\)", text):
    a, b, n = int(m.group(1)), int(m.group(2)), int(m.group(3))
    inside = [c for c in C.WTC if c.isdigit() and a <= int(c) <= b]
    if len(inside) < n:
        rows.append(["WTC-RANGE", f"{a}-{b}", "part 5", "UNMAPPED", f"{len(inside)} codes in the catalogue, {n} stated"])
for (kind, ref), ln in sorted(loc.items(), key=lambda x: (x[0][0], x[0][1])):
    if kind == "WTC":
        ok = ref in C.WTC
        add("WTC", ref, f"line {ln}", ok, C.WTC[ref]["name"] if ok else "")
    elif kind == "DD":
        ok = ref in C.DDF
        add("DD", ref, f"line {ln}", ok, C.DDF.get(ref, ""))
    elif kind == "REG":
        ok = ref in C.REG
        add("REG", ref, f"line {ln}", ok, C.REG[ref].get("status", "") if ok else "")
    else:
        ok = ref in C.GAPS or ref.startswith("DESIGN-RQ-")
        gg = C.GAPS.get(ref)
        add("GAP", ref, f"line {ln}", bool(gg), gg["status"] if gg else "")
# flag accounts are not WTC codes; every regulation id of Part 4 headings is in the Part 3 sequence
flags = set(re.findall(r"^\|\s*(584\d\d)\s*\|", text, re.M))
for f in sorted(flags):
    add("FLAG", f, "part 1", f not in C.WTC, "not a catalogue code")
seq = set(re.findall(r"^\|\s*\d+\s*\|\s*(9840\d{3})\s*\|", text, re.M))
heads = set()
for m in re.finditer(r"^### ([\d/ ]+) —", text, re.M):
    heads |= set(re.findall(r"9840\d{3}", m.group(1)))
for r in sorted(seq | heads):
    add("REGULATION", r, "parts 3 and 4", r in seq and r in heads, "in the sequence and detailed" if (r in seq and r in heads) else "missing in Part 3 or Part 4")
with open(os.path.join(HERE, "design_recon.csv"), "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["kind", "reference", "where", "status", "detail"])
    w.writerows(rows)
un = [r for r in rows if r[3] == "UNMAPPED"]
by = {}
for r in rows:
    by[r[0]] = by.get(r[0], 0) + 1
print("references:", by, " unmapped:", len(un))
for r in un[:20]:
    print(r)
sys.exit(1 if un else 0)
