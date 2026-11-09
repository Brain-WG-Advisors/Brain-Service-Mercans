# -*- coding: utf-8 -*-
"""Self-checks of the US Wage Type Catalogue: C29 (shared v2.12 HARD + X-run), WORD/PATH, FRAC/PCT/UNIT, C46 period-aware,
C30, unbound distinctive values, C12 structure, gap markers vs request file. usage: python wtc_lint.py [workbook] [--json out]"""
import importlib.util
import json
import os
import re
import sys

from openpyxl import load_workbook

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import wtc_common as W  # noqa: E402
import build_wtc as B  # noqa: E402
import wtc_taxcodes as _T  # noqa: E402
_T.define()

C = W.C
D = W.D
_spec = importlib.util.spec_from_file_location("ccs", os.path.expanduser("~/mercans-pipeline/shared/consistency-checks/consistency_checks.py"))
CCS = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(CCS)
TAG = CCS.TAG
ANYTAG = re.compile(r"\[\[(?:FACT|GAP):[^\]]*\]\]")
URL = re.compile(r"https?://\S+")
PCT_TOK = re.compile(r"(?<![\d.,\w])(\d+(?:\.\d+)?)\s?%")
FRAC_TOK = re.compile(r"(?<![\d.,\w])(0\.\d{3,})(?![\d%\w])")
UNIT_RX = {"days": r"^\s?days?\b", "percent": r"^\s?%", "%": r"^\s?%", "hours": r"^\s?hours?\b", "weeks": r"^\s?weeks?\b",
           "months": r"^\s?months?\b", "employees": r"^\s?employees?\b"}
XRUN = re.compile(r"X{3,}")
BARE = re.compile(r"^[\s\-\*_.:;,\"'\[\]\(\)]*(?:PENDING|PLACEHOLDER|TBC|FILL[\s_-]*IN|TO BE COMPLETED)[\s\-\*_.:;,\"'\[\]\(\)]*$", re.I)
RID = re.compile(r"US-[A-Z0-9]+-\d+")


def same(a, b):
    x, y = CCS._num(a), CCS._num(b)
    if x is not None and y is not None:
        return abs(x - y) < 1e-9
    return str(a).strip() == str(b).strip()


FORMS = {}
for _k, _es in C.FACTS.items():
    for _f in _es:
        for _n, _p in CCS.distinctive_forms(_k, _f.get("value")):
            FORMS.setdefault((round(_n, 6), _p), set()).add(_k)


def run(path):
    wb = load_workbook(path)
    rep = dict(C29=[], WORD=[], mismatch=[], missing_key=[], C30=[], FRAC=[], PCT=[], UNIT=[], unbound=[], C12=[], tags=0, gaps=set(), info={})
    toks = {}
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if isinstance(c.value, str):
                    for t in TAG.finditer(c.value):
                        for f in C.FACTS.get(t.group(1), []):
                            if same(t.group(2), f.get("value")):
                                s = toks.setdefault(f["register_id"], set())
                                for x in re.findall(r"\d+(?:\.\d+)?", t.group(2)):
                                    s.add(round(float(x), 6))
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            row_rids = set(RID.findall(" ".join(str(x.value) for x in row if isinstance(x.value, str))))
            for c in row:
                v = c.value
                if not isinstance(v, str):
                    continue
                loc = f"{ws.title}!{c.coordinate}"
                bare = ANYTAG.sub(" ", v)
                hh = D.hard_hits(v) or D.hard_hits(bare)
                if hh:
                    rep["C29"].append((loc, hh[0]))
                if BARE.match(v):
                    rep["C29"].append((loc, "bare placeholder"))
                for m in XRUN.finditer(bare):
                    lo, hi = m.start(), m.end()
                    if not (re.search(r"[.\d]$", bare[max(0, lo - 2):lo]) or re.match(r"\s*[.:\d]", bare[hi:hi + 2])):
                        rep["C29"].append((loc, "X-run"))
                if C.C29.search(v) or C.C29.search(bare):
                    rep["C29"].append((loc, (C.C29.search(v) or C.C29.search(bare)).group(0)))
                m = C.PIPELINE_WORDS.search(bare)
                if m:
                    rep["WORD"].append((loc, m.group(0)))
                pm = C.PATH_RX.search(v)
                if pm:
                    rep["WORD"].append((loc, "internal path: " + pm.group(0)))
                for t in TAG.finditer(v):
                    rep["tags"] += 1
                    k, val = t.group(1), t.group(2)
                    if k not in C.FACTS:
                        rep["missing_key"].append((loc, k))
                        continue
                    hit = [f for f in C.FACTS[k] if same(val, f.get("value"))]
                    if not hit:
                        rep["mismatch"].append((loc, k, val[:60]))
                        continue
                    r0 = D.REG.get(hit[0]["register_id"])
                    if all((D.REG.get(f["register_id"]) is None or D.REG[f["register_id"]].get("tier") in ("B", "C")
                            or D.REG[f["register_id"]].get("status") == "MANUAL") for f in hit) and re.search(r"\d", val):
                        rep["C30"].append((loc, k))
                    f0 = hit[0]
                    if isinstance(f0.get("value"), (int, float)) and not isinstance(f0.get("value"), bool) and f0.get("unit_of_measure"):
                        rx = UNIT_RX.get(str(f0["unit_of_measure"]).lower())
                        if rx and not re.search(rx, v[t.end():t.end() + 20], re.I):
                            rep["UNIT"].append((loc, k))
                for gg in re.findall(r"\[\[GAP:\s*([A-Za-z0-9_.-]+)\s*\]\]", v):
                    rep["gaps"].add(gg)
                plain = URL.sub(" ", ANYTAG.sub(" ", v))
                for mm in PCT_TOK.finditer(plain):
                    rep["PCT"].append((loc, mm.group(0)))
                for mm in FRAC_TOK.finditer(plain):
                    rep["FRAC"].append((loc, mm.group(0)))
                body = re.sub(r"\[US-[A-Z0-9]+-\d+\]|\bUS-[A-Z0-9]+-\d{3}\b( v\d+\.\d+)?|\bUS-\d{3}\b", " ", plain)
                body = re.sub(r"\b\d{4}-\d{2}-\d{2}\b", " ", body)
                for mm in CCS.NUM_IN_TEXT.finditer(body):
                    n = CCS._num(mm.group(1))
                    if n is None:
                        continue
                    ks = FORMS.get((round(n, 6), bool(mm.group(2))))
                    if ks:
                        integer_tok = (not mm.group(2)) and "." not in mm.group(1) and n == int(n)
                        if integer_tok and any(round(n, 6) in toks.get(r_, ()) for r_ in row_rids):
                            continue
                        if ws.title == "Wage Type Catalogue" and c.column == 1:
                            continue
                        rep["unbound"].append((loc, mm.group(0).strip(), sorted(ks)[:2], body[max(0, mm.start() - 30):mm.end() + 20]))
    # ---------------------------------------------------------------- C12
    exp = ["Version Control", "Wage Type Catalogue", "Sick Leave Paid By Employer", "Tax Credit", "Global WTC Coverage", "Form Reference Guide"]
    if wb.sheetnames != exp:
        rep["C12"].append(f"sheets {wb.sheetnames} != {exp}")
    ws = wb["Wage Type Catalogue"]
    hdr = [c.value for c in ws[1] if c.value is not None]
    if hdr != B.HEADERS:
        rep["C12"].append("header row differs from the contract")
    tpl = load_workbook(W.TEMPLATE)["Wage Type Catalogue"]
    for i in range(1, 14):
        if tpl.cell(1, i).value != ws.cell(1, i).value and i not in (3,):
            rep["C12"].append(f"template header col {i} changed: {ws.cell(1, i).value!r}")
    if ws.freeze_panes != "C1":
        rep["C12"].append(f"freeze {ws.freeze_panes}")
    codes, n = [], 0
    for r in range(2, ws.max_row + 1):
        a = ws.cell(r, 1).value
        if a in (None, "") or a == "Mercans Code":
            continue
        n += 1
        codes.append(str(a))
        for h in ("Wage Type Explanation", "Category", "Tax Code", "Wage Type Name in English"):
            if ws.cell(r, B.COL[h]).value in (None, ""):
                rep["C12"].append(f"row {r}: blank {h}")
        for h in B.ORANGE:
            if ws.cell(r, B.COL[h]).value not in (None, ""):
                rep["C12"].append(f"row {r}: dev column {h} not empty")
        for f, hh in B.M.FLAG_COLS:
            v = ws.cell(r, B.COL[hh]).value
            if v not in ("Yes", "No", "Yes-No", "NA"):
                rep["C12"].append(f"row {r}: flag {hh} = {v!r}")
            if v == "Yes-No" and not ws.cell(r, B.COL["Wage Type Explanation"]).value:
                rep["C12"].append(f"row {r}: Yes-No without explanation")
        tcode = ws.cell(r, B.COL["Tax Code"]).value
        if tcode not in B.M.TAXCODES:
            rep["C12"].append(f"row {r}: tax code {tcode!r} not in the legend")
    if len(codes) != len(set(codes)):
        rep["C12"].append("duplicate codes")
    gl = [int(x) for x in codes if x.isdigit()]
    from wtc_global import load_global
    gcodes = [c for c, _, _ in load_global()]
    if sorted(gl) != sorted(gcodes) or len(gcodes) != 300:
        rep["C12"].append(f"global codes {len(gl)} != 300 or changed")
    typ = {}
    for _, _, t in load_global():
        typ[t] = typ.get(t, 0) + 1
    rep["info"] = dict(rows=n, global_types=typ, tags=rep["tags"])
    req = json.load(open(os.path.join(W.RESEARCH, "WTC-research-request.json"), encoding="utf-8"))
    known = {"WTC-RQ-" + r["id"].split("-")[1] for r in req["requests"]}
    gj = {x["id"] for x in json.load(open(os.path.join(W.RESEARCH, "gaps.json"), encoding="utf-8"))["gaps"]}
    for gg in rep["gaps"]:
        if gg not in known or gg not in gj:
            rep["C12"].append(f"gap {gg} not in the request file or gaps.json")
    rep["gaps"] = sorted(rep["gaps"])
    return rep


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a.endswith(".xlsx")]
    path = args[0] if args else os.path.join(W.WTCDIR, W.FILENAME)
    r = run(path)
    sys.stdout.reconfigure(encoding="utf-8")
    print({k: (len(v) if isinstance(v, list) else v) for k, v in r.items() if k not in ("info", "gaps")}, r["info"], len(r["gaps"]), "gaps used")
    for k in ("C29", "WORD", "mismatch", "missing_key", "C30", "UNIT", "FRAC", "PCT", "C12"):
        for x in r[k][:15]:
            print(k, x)
    for x in r["unbound"][:30]:
        print("UNBOUND", x)
    if "--json" in sys.argv:
        json.dump(r, open(sys.argv[sys.argv.index("--json") + 1], "w", encoding="utf-8"), indent=1, default=list, ensure_ascii=False)
