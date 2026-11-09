# -*- coding: utf-8 -*-
"""Self-checks of the US Data Dictionary workbook.

  C29    residual markers in every cell (toolkit regex), raw and tag-stripped
  WORD   pipeline wording outside tags (RESEARCH-GAP is a C29 HARD marker; documented limitations read "Not configured in this release [[GAP:DD-RQ-nn]]")
  C46p   period-aware C46: every [[FACT:key=value]] equals a dated value of the key; distinctive fact values
         written without a tag (numbers, percents)
  FRAC/PCT/UNIT  a '%' or a 3+ decimal fraction outside a tag; a numeric tag whose unit does not follow it
  C30    tagged numbers whose register rows are all weak (tier B/C or status MANUAL)
  C12    structure per template: sheets and order, header rows and columns, blue/orange discipline, unique names,
         option mappers referenced and defined, repeated header rows counted out of the data rows
  COVER  DD facts never bound in the workbook (each must be a documented exclusion)
usage: python dd_lint.py [workbook] [--json out.json]
"""
import importlib.util
import json
import os
import re
import sys

from openpyxl import load_workbook

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import dd_common as D  # noqa: E402

C = D.C
_spec = importlib.util.spec_from_file_location(
    "ccs", os.path.expanduser("~/mercans-pipeline/shared/consistency-checks/consistency_checks.py"))
CCS = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(CCS)
TAG = CCS.TAG
ANYTAG = re.compile(r"\[\[(?:FACT|GAP):[^\]]*\]\]")
GAPTAG = re.compile(r"\[\[GAP:\s*([A-Za-z0-9_.-]+)\s*\]\]")
URL = re.compile(r"https?://\S+")
ISO = ("Currency Codes - ISO 4217", "Country Codes - ISO 3166-1")
ORANGE = {"ID Information": {2, 4} | set(range(12, 22)), "Country Fields": {3, 5} | set(range(13, 23))}
PCT_TOK = re.compile(r"(?<![\d.,\w])(\d+(?:\.\d+)?)\s?%")
FRAC_TOK = re.compile(r"(?<![\d.,\w])(0\.\d{3,})(?![\d%\w])")
UNIT_RX = {"days": r"^\s?days?\b", "percent": r"^\s?%", "%": r"^\s?%", "hours": r"^\s?hours?\b",
           "weeks": r"^\s?weeks?\b", "months": r"^\s?months?\b", "employees": r"^\s?employees?\b"}


def same(a, b):
    x, y = CCS._num(a), CCS._num(b)
    if x is not None and y is not None:
        return abs(x - y) < 1e-9
    return str(a).strip() == str(b).strip()


def weak(rid):
    r = D.REG.get(rid)
    return r is None or r.get("tier") in ("B", "C") or r.get("status") == "MANUAL"


FORMS = {}
for _k, _es in C.FACTS.items():
    for _f in _es:
        for _n, _p in CCS.distinctive_forms(_k, _f.get("value")):
            FORMS.setdefault((round(_n, 6), _p), set()).add(_k)


RID = re.compile(r"US-[A-Z0-9]+-\d+")


def tagged_tokens(wb):
    """register id -> numbers inside the full values tagged in this workbook (for the DERIVED rule)."""
    out = {}
    for ws in wb.worksheets:
        if ws.title in ISO:
            continue
        for row in ws.iter_rows():
            for c in row:
                if not isinstance(c.value, str):
                    continue
                for t in TAG.finditer(c.value):
                    k, val = t.group(1), t.group(2)
                    for f in C.FACTS.get(k, []):
                        if not same(val, f.get("value")):
                            continue
                        toks = out.setdefault(f["register_id"], set())
                        for x in re.findall(r"\d+(?:\.\d+)?", str(val)):
                            toks.add(round(float(x), 6))
    return out


def run(path):
    wb = load_workbook(path)
    toks = tagged_tokens(wb)
    rep = dict(gapmarks=[], derived=0, C29=[], WORD=[], mismatch=[], missing_key=[], unbound=[], C30=[], FRAC=[], PCT=[], UNIT=[], tags=0,
               bound=set(), gaps=set(), C12=[], names=[], info={})
    for ws in wb.worksheets:
        if ws.title in ISO:
            continue
        for row in ws.iter_rows():
            row_rids = set(RID.findall(" ".join(str(x.value) for x in row if isinstance(x.value, str))))
            for c in row:
                v = c.value
                if not isinstance(v, str):
                    continue
                loc = f"{ws.title}!{c.coordinate}"
                for gid in re.findall(r"\[\[GAP:\s*(DD-RQ-\d{2})\s*\]\]", v):
                    rep["gapmarks"].append((loc, [gid]))
                bare = ANYTAG.sub(" ", v)
                hh = D.hard_hits(v) or D.hard_hits(bare)       # shared pipeline v2.12 C29 HARD tier
                if hh:
                    rep["C29"].append((loc, hh[0]))
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
                    rep["bound"].add(k)
                    if k not in C.FACTS:
                        rep["missing_key"].append((loc, k))
                        continue
                    hit = [f for f in C.FACTS[k] if same(val, f.get("value"))]
                    if not hit:
                        rep["mismatch"].append((loc, k, val[:60]))
                    elif re.search(r"\d", val) and all(weak(f["register_id"]) for f in hit):
                        rep["C30"].append((loc, k))
                    f0 = hit[0] if hit else None
                    if f0 is not None and isinstance(f0.get("value"), (int, float)) and f0.get("unit_of_measure"):
                        u = str(f0["unit_of_measure"]).lower()
                        rx = UNIT_RX.get(u)
                        if rx and not re.search(rx, v[t.end():t.end() + 20], re.I):
                            rep["UNIT"].append((loc, k, u))
                for g_ in GAPTAG.findall(v):
                    rep["gaps"].add(g_)
                plain = URL.sub(" ", ANYTAG.sub(" ", v))
                for mm in PCT_TOK.finditer(plain):
                    rep["PCT"].append((loc, mm.group(0), plain[max(0, mm.start() - 40): mm.end() + 20]))
                for mm in FRAC_TOK.finditer(plain):
                    rep["FRAC"].append((loc, mm.group(0)))
                body = re.sub(r"\[US-[A-Z0-9]+-\d+\]|\bUS-[A-Z0-9]+-\d{3}\b( v\d+\.\d+)?", " ", plain)
                body = re.sub(r"\b(?:effective|read)[^()]*\d{4}-\d{2}-\d{2}", " ", body)
                body = re.sub(r"\b\d{4}-\d{2}-\d{2}\b", " ", body)
                for mm in CCS.NUM_IN_TEXT.finditer(body):
                    n = CCS._num(mm.group(1))
                    if n is None:
                        continue
                    ks = FORMS.get((round(n, 6), bool(mm.group(2))))
                    integer_tok = (not mm.group(2)) and "." not in mm.group(1) and n == int(n)
                    if ks and integer_tok and any(round(n, 6) in toks.get(r_, ()) for r_ in row_rids):
                        rep["derived"] += 1       # a code of a list whose full value is tagged in the same workbook
                        continue
                    if ks:
                        rep["unbound"].append((loc, mm.group(0).strip(), sorted(ks)[:2],
                                               body[max(0, mm.start() - 40): mm.end() + 25]))
    # ---------------------------------------------------------------- C12 structure
    names = wb.sheetnames
    exp = ["Version Control", "Introduction", "Instructions", "ID Information", "Country Fields", "Country Option Mappers",
           "Currency Codes - ISO 4217", "Country Codes - ISO 3166-1"]
    if names != exp:
        rep["C12"].append(f"sheets {names} != {exp}")
    tpl = load_workbook(D.TEMPLATE)
    for n in ("ID Information", "Country Fields", "Country Option Mappers"):
        a = [c.value for c in tpl[n][4]]
        b = [c.value for c in wb[n][4]]
        if a != b:
            rep["C12"].append(f"{n}: header row 4 differs from the template")
    for n in ("Instructions", "Currency Codes - ISO 4217", "Country Codes - ISO 3166-1"):
        ta = [[c.value for c in r] for r in tpl[n].iter_rows(min_row=1, max_row=40)]
        wa = [[c.value for c in r] for r in wb[n].iter_rows(min_row=1, max_row=40)]
        if ta != wa:
            rep["C12"].append(f"{n}: not preserved as in the template")
    if wb["ID Information"].freeze_panes != tpl["ID Information"].freeze_panes:
        rep["C12"].append("ID Information freeze panes differ from the template")
    for n, hdr_last in (("ID Information", 22), ("Country Fields", 23)):
        ws = wb[n]
        hdrs = {c.column: c.value for c in ws[4] if c.value is not None}
        if max(hdrs) != hdr_last:
            rep["C12"].append(f"{n}: header runs to column {max(hdrs)}, expected {hdr_last}")
        data = []
        for r in range(5, ws.max_row + 1):
            vals = {c.column: c.value for c in ws[r] if c.value not in (None, "")}
            if not vals:
                continue
            first = vals.get(1 if n == "ID Information" else 2)
            if first == "Country" or (len(vals) == 1 and 1 in vals):
                continue            # repeated header row / section title: not data
            data.append(r)
            for ci in ORANGE[n]:
                if ws.cell(r, ci).value not in (None, ""):
                    rep["C12"].append(f"{n}!{ws.cell(r, ci).coordinate}: orange (dev-team) column is not empty")
        nm_col = 3 if n == "ID Information" else 4
        for r in data:
            nm = ws.cell(r, nm_col).value
            rep["names"].append(nm)
            for ci, lab in ((nm_col, "Field Name"), (nm_col + 4, "Data Type"), (nm_col + 6, "Field Type")):
                if ws.cell(r, ci).value in (None, ""):
                    rep["C12"].append(f"{n}!{ws.cell(r, ci).coordinate}: blank {lab}")
            if ws.cell(r, nm_col + 4).value not in ("M", "CM", "O"):
                rep["C12"].append(f"{n}!row {r}: Data Type not M/CM/O")
            if ws.cell(r, nm_col + 6).value not in ("Text", "Number", "Date", "Integer", "Decimal", "Counter"):
                rep["C12"].append(f"{n}!row {r}: Field Type outside the template list")
            if ws.cell(r, nm_col + 4).value == "CM" and not ws.cell(r, nm_col + 5).value:
                rep["C12"].append(f"{n}!row {r}: Conditional Mandatory without a Pre-Condition")
        rep["info"][n] = len(data)
    dup = sorted({x for x in rep["names"] if rep["names"].count(x) > 1})
    if dup:
        rep["C12"].append(f"duplicate Field Names: {dup}")
    wm = wb["Country Option Mappers"]
    defined, rows_by = set(), {}
    cur = None
    for r in range(5, wm.max_row + 1):
        b, c_ = wm.cell(r, 2).value, wm.cell(r, 3).value
        if b == "Option Mapper Description":
            cur = None
            continue
        if b:
            cur = b
            defined.add(b)
        if cur and c_ not in (None, ""):
            rows_by.setdefault(cur, []).append(str(c_))
    refs = set()
    for n, col in (("ID Information", 11), ("Country Fields", 12)):
        for r in range(5, wb[n].max_row + 1):
            v = wb[n].cell(r, col).value
            if v and v != "Option Mapper":
                refs.add(v)
    for m in sorted(refs - defined):
        rep["C12"].append(f"option mapper {m!r} referenced by a field but not defined")
    for m in sorted(defined - refs):
        rep["C12"].append(f"option mapper {m!r} defined but referenced by no field")
    for m, codes in rows_by.items():
        if len(codes) != len(set(codes)):
            rep["C12"].append(f"option mapper {m!r}: duplicate codes")
    rep["info"]["mappers"] = len(defined)
    rep["info"]["mapper_rows"] = sum(len(v) for v in rows_by.values())
    rep["info"]["tags"] = rep["tags"]
    rq = os.path.join(D.RESEARCH, "DD-research-request.json")
    known = set()
    if os.path.exists(rq):
        known = {"DD-" + x["id"] for x in json.load(open(rq, encoding="utf-8")).get("requests", [])}
    for loc, ids in rep["gapmarks"]:
        for i in ids:
            if i not in known:
                rep["C12"].append(f"{loc}: gap marker cites {i}, which is not in DD-research-request.json")
    rep["unbound_dd_facts"] = sorted(set(D.DD_KEYS) - rep["bound"])
    rep["bound"] = sorted(rep["bound"])
    rep["gaps"] = sorted(rep["gaps"])
    return rep


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    path = args[0] if args and args[0].endswith(".xlsx") else os.path.join(D.OUT, D.FILENAME)
    r = run(path)
    sys.stdout.reconfigure(encoding="utf-8")
    summ = {k: (len(v) if isinstance(v, list) else v) for k, v in r.items() if k not in ("names", "info")}
    summ["info"] = r["info"]
    print(json.dumps(summ, indent=1, default=list))
    for k in ("C29", "WORD", "mismatch", "missing_key", "C30", "UNIT", "FRAC", "PCT", "C12"):
        for x in r[k][:25]:
            print(k, x)
    for x in r["unbound"][:40]:
        print("UNBOUND", x)
    print("DD FACTS NOT BOUND IN THE WORKBOOK:", r["unbound_dd_facts"])
    if "--json" in sys.argv:
        json.dump(r, open(sys.argv[sys.argv.index("--json") + 1], "w", encoding="utf-8"), indent=1, ensure_ascii=False,
                  default=list)
