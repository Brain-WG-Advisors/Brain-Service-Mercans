# -*- coding: utf-8 -*-
"""Round 3b C30 scan (QA r3 blocker 4): no number in the DOCX whose only register support is a weak row.

Weak row = register tier B or C, or status MANUAL. Two passes over every paragraph and table cell of
01-ccg/US-CCG-001-v1.0.docx:
  1. tagged numbers: every [[FACT:key=value]] whose value holds a digit; the fact's register_id (all dated
     entries of the key) must include at least one non-weak row;
  2. untagged numbers: a text unit (paragraph / cell) that cites only weak register ids ([US-...]) and holds a
     number outside tags, citations, section numbers and dates is listed for review.
Also lists every text unit containing the word 'secondary' together with an untagged number.
Writes out/c30_scan.json.  usage: python c30_scan.py
"""
import csv
import glob
import json
import os
import re

from docx import Document

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
DOCX = sorted(glob.glob(os.path.join(BASE, "01-ccg", "US-CCG-001-v*.docx")))[-1]

REG = {r["id"]: r for r in csv.DictReader(open(os.path.join(BASE, "00-official-sources", "legal-basis-register.csv"),
                                               encoding="utf-8"))}


def weak(rid):
    r = REG.get(rid)
    if r is None:
        return True
    return r["tier"] in ("B", "C") or r["status"] == "MANUAL"


FACTREG = {}
for fp in glob.glob(os.path.join(BASE, "_research", "CCG-*-facts.json")):
    for f in json.load(open(fp, encoding="utf-8")).get("facts", []):
        FACTREG.setdefault(f["key"], set()).add(f.get("register_id"))

TAG = re.compile(r"\[\[FACT:([^=\]]+)=([^\]]*)\]\]")
ANYTAG = re.compile(r"\[\[(?:FACT|GAP):[^\]]*\]\]")
CITE = re.compile(r"US-[A-Z0-9]+(?:-[A-Z0-9]+)+")
NUM = re.compile(r"(?<![\w.])\d[\d,]*(?:\.\d+)?")


def strip_noise(t):
    t = ANYTAG.sub(" ", t)
    t = CITE.sub(" ", t)
    t = re.sub(r"\b\d{4}-\d{2}-\d{2}\b", " ", t)                      # dates
    t = re.sub(r"\b[A-Z]{2,5}\.\d+[a-z]?\b", " ", t)                   # section refs (CA.2)
    t = re.sub(r"\b(?:19|20)\d{2}\b", " ", t)                          # years
    t = re.sub(r"\b\d+(?:\.\d+)?\s*(?:CFR|U\.S\.C\.|MRSA|CMR|RSA|KRS|ORC|OAC|CSR)\b", " ", t)
    t = re.sub(r"(?:§|sec\.|section|s\.|art\.|ch\.|chapter|Code|IC|G\.S\.|T\.C\.A\.|KRS|RCW|ORS|MCL|ILCS|Pub\.|Form|form|DE|PC|HB|SB|SEA|P\.L\.|Rev\.|rev\.|IRC|AS|R\.S\.|NRS|NMSA|GL c\.|M\.G\.L\.|W\. Va\. Code)\s*[\d][\w.()\-:/]*", " ", t)
    return t


units = []
d = Document(DOCX)
for i, p in enumerate(d.paragraphs):
    units.append((f"para {i}", p.text))


def walk(tables, prefix):
    for ti, t in enumerate(tables):
        for ri, row in enumerate(t.rows):
            for ci, cell in enumerate(row.cells):
                units.append((f"{prefix}table {ti} r{ri}c{ci}", cell.text))
                if cell.tables:
                    walk(cell.tables, f"{prefix}table {ti}.")


walk(d.tables, "")

tagged_weak, untagged_weak, secondary_num = [], [], []
seen = set()
for loc, t in units:
    if not t or (t, loc) in seen:
        continue
    seen.add((t, loc))
    for k, v in TAG.findall(t):
        if not re.search(r"\d", v):
            continue
        rids = FACTREG.get(k, set())
        if rids and all(weak(r) for r in rids):
            tagged_weak.append({"where": loc, "key": k, "value": v[:80], "register": sorted(rids)})
    cites = set(CITE.findall(t))
    rest = strip_noise(t)
    nums = [n for n in NUM.findall(rest) if n not in ("0", "1")]
    if cites and all(weak(c) for c in cites) and nums:
        untagged_weak.append({"where": loc, "numbers": nums[:8], "cites": sorted(cites), "text": t[:200]})
    if re.search(r"secondary|tier-B", t, re.I) and nums:
        secondary_num.append({"where": loc, "numbers": nums[:8], "text": t[:220]})

out = {"docx": DOCX, "weak_definition": "register tier B or C, or status MANUAL",
       "tagged_numbers_weak_only": tagged_weak, "untagged_numbers_in_weak_only_units": untagged_weak,
       "secondary_wording_with_number": secondary_num}
json.dump(out, open(os.path.join(HERE, "out", "c30_scan.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print(f"C30 scan: tagged weak-only {len(tagged_weak)}, untagged in weak-only units {len(untagged_weak)}, "
      f"'secondary' + number {len(secondary_num)}")
