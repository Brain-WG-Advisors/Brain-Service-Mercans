# -*- coding: utf-8 -*-
"""F44 per artifact (v1.1 rebuild, 2026-11-06): every [[FACT:key=value]] tag of the artifact resolves to a fact whose
register row(s) exist, are tier A, are not MANUAL, carry effective_from and were verified within 120 days of the
check date; every register id printed in the artifact exists in legal-basis-register.csv.
usage: python v11_f44_check.py [--today YYYY-MM-DD] [--json out.json]   (BASE = parent of _pipeline)"""
import csv
import datetime as dt
import glob
import json
import os
import re
import sys

import docx
from openpyxl import load_workbook

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = dt.date.fromisoformat(sys.argv[sys.argv.index("--today") + 1]) if "--today" in sys.argv else dt.date.today()
TAG = re.compile(r"\[\[FACT:([A-Za-z0-9_.]+)=([^\]]*)\]\]")
RID = re.compile(r"\bUS-[A-Z0-9]+-\d{3}\b")
REG = {r["id"]: r for r in csv.DictReader(open(os.path.join(BASE, "00-official-sources", "legal-basis-register.csv"), encoding="utf-8"))}
REG_PREFIXES = {i.rsplit("-", 1)[0] for i in REG} - {"US-CCG", "US-DD", "US-WTC", "US-SIR", "US-DOR", "US-IRS", "US-SSA", "US-UI",
                                                     "US-LOC", "US-PFML", "US-SDNH", "US-WC", "US-INB", "US-OUT"}
FACTS = {}
for p in glob.glob(os.path.join(BASE, "_research", "*-facts.json")):
    for f in json.load(open(p, encoding="utf-8"))["facts"]:
        FACTS.setdefault(f["key"], []).append(f)
ART = {"CCG": "01-ccg/US-CCG-001-v*.docx", "WTC": "02-wtc/US-WTC-001-v*.xlsx", "SIR": "03-statutory-integrations/US-SIR-INDEX-001-v*.docx",
       "RSPEC": "04-reports-spec/*-Spec.xlsx", "DD": "05-data-dictionary/US-DD-001-v*.xlsx"}


def same(a, b):
    try:
        return abs(float(str(a).replace(",", "")) - float(str(b).replace(",", ""))) < 1e-9
    except ValueError:
        return re.sub(r"\s+", " ", str(a)).strip() == re.sub(r"\s+", " ", str(b)).strip()


def texts(p):
    if p.endswith(".docx"):
        d = docx.Document(p)
        for x in d.paragraphs:
            yield x.text
        for t in d.tables:
            for r in t.rows:
                for c in r.cells:
                    yield c.text
    else:
        for ws in load_workbook(p, read_only=True).worksheets:
            for row in ws.iter_rows(values_only=True):
                for v in row:
                    if isinstance(v, str):
                        yield v


def row_problems(rid):
    r = REG.get(rid)
    if r is None:
        return ["register id not in register"]
    out = []
    if not str(r.get("tier", "")).startswith("A"):
        out.append(f"tier {r.get('tier')}")
    if "MANUAL" in str(r.get("status", "")).upper():
        out.append("MANUAL")
    if not r.get("effective_from"):
        out.append("no effective_from")
    try:
        vo = dt.date.fromisoformat(str(r.get("verified_on"))[:10])
        if (TODAY - vo).days > 120:
            out.append(f"verified_on {vo} older than 120 days")
    except ValueError:
        out.append("no verified_on")
    return out


rep = {}
for art, pat in ART.items():
    files = sorted(glob.glob(os.path.join(BASE, pat)))
    if art in ("CCG", "WTC", "SIR", "DD"):
        files = files[-1:]
    pairs, rids, issues = set(), set(), []
    for p in files:
        for t in texts(p):
            for m in TAG.finditer(t):
                pairs.add((m.group(1), m.group(2)))
            rids.update(RID.findall(TAG.sub(" ", t)))
    for k, v in sorted(pairs):
        fs = [f for f in FACTS.get(k, []) if same(v, f["value"])]
        if not fs:
            issues.append({"key": k, "value": v[:60], "why": "no fact with this value"})
            continue
        best = None
        for f in fs:
            ids = [f["register_id"]] + list(f.get("_also_register_ids") or [])
            probs = {i: row_problems(i) for i in ids}
            if any(not v_ for v_ in probs.values()):
                best = None
                break
            best = probs
        if best:
            issues.append({"key": k, "value": v[:60], "why": best})
    for rid in sorted(rids):
        if rid not in REG and rid.rsplit("-", 1)[0] in REG_PREFIXES:   # document / row ids (US-CCG-001, US-UI-001) are not register ids
            issues.append({"register_id": rid, "why": "printed register id not in register"})
    rep[art] = {"files": [os.path.basename(x) for x in files], "tag_pairs": len(pairs), "register_ids_printed": len(rids),
                "issues": len(issues), "details": issues[:60]}
    print(f"F44 {art}: files {len(files)}, tag pairs {len(pairs)}, printed ids {len(rids)}, issues {len(issues)}")
if "--json" in sys.argv:
    json.dump(rep, open(sys.argv[sys.argv.index("--json") + 1], "w", encoding="utf-8"), indent=1, ensure_ascii=False)
sys.exit(1 if any(v["issues"] for v in rep.values()) else 0)
