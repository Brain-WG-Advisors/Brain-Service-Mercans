# -*- coding: utf-8 -*-
"""Self-checks of the US Report Specifications (run on a folder of *-Spec.xlsx).

  C29   residual markers in every cell (toolkit regex), tags stripped and unstripped
  WORD  pipeline wording outside tags
  C46p  period-aware C46: every [[FACT:key=value]] equals a dated value of the key; distinctive
        fact values written without a tag (shared rule + percent-aware), listed with context.
        DERIVED: a number of a row rendered from a layout or line-map fact (a position, a line
        number, a code of a code list) is not counted as unbound when the same sheet row cites the
        register id of a fact whose full value is tagged in the same workbook and contains that
        number; such hits are counted separately (rule documented in the RSPEC build log).
  C12   core sheet: columns populated (of 21), blank column M on field rows, row width <= 21
  WIDTH every sheet: no value right of the header's last column
  C30   tagged numbers whose register rows are all weak (tier B/C or status MANUAL)
  COVER RSPEC facts never bound in any workbook
  GAPS  [[GAP:id]] ids: recorded limitation ids or research-request ids
usage: python spec_lint.py <dir> [--json out.json]
"""
import csv
import glob
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import us_common as C  # noqa: E402

from openpyxl import load_workbook  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "ccs", os.path.expanduser("~/mercans-pipeline/shared/consistency-checks/consistency_checks.py"))
CCS = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(CCS)

TAG = CCS.TAG
GAPTAG = re.compile(r"\[\[GAP:\s*([A-Za-z0-9_.-]+)\s*\]\]")
ANYTAG = re.compile(r"\[\[(?:FACT|GAP):[^\]]*\]\]")
REG = {r["id"]: r for r in csv.DictReader(open(os.path.join(C.BASE, "00-official-sources", "legal-basis-register.csv"),
                                               encoding="utf-8"))}


def weak(rid):
    r = REG.get(rid)
    return r is None or r.get("tier") in ("B", "C") or r.get("status") == "MANUAL"


def same(a, b):
    x, y = CCS._num(a), CCS._num(b)
    if x is not None and y is not None:
        return abs(x - y) < 1e-9
    return str(a).strip() == str(b).strip()


forms = {}
for k, es in C.FACTS.items():
    for f in es:
        v = f.get("value")
        for n, p in CCS.distinctive_forms(k, v):
            forms.setdefault((round(n, 6), p), set()).add(k)
        if isinstance(v, (int, float)) and not isinstance(v, bool) and re.search(r"(^|\.)rate(\.|$)", k):
            n = float(v)
            if n and (CCS._sig(n) >= 3 or n != int(n)):
                forms.setdefault((round(n, 6), True), set()).add(k)

POS = re.compile(r"^\d{1,3}(-\d{1,3})?$")
RID = re.compile(r"US-[A-Z0-9]+-\d+")


def tagged_tokens(wb):
    """register id -> numbers appearing in the full values tagged in this workbook."""
    out = {}
    for ws in wb.worksheets:
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
                        for mm in CCS.NUM_IN_TEXT.finditer(str(val)):
                            n = CCS._num(mm.group(1))
                            if n is not None:
                                toks.add(round(n, 6))
                        for x in re.findall(r"\d+(?:\.\d+)?", str(val)):
                            toks.add(round(float(x), 6))
    return out


def run(d):
    rep = {"files": 0, "C29": [], "WORD": [], "tags": 0, "mismatch": [], "missing_key": [], "unbound": [],
           "C12": {}, "blankM": [], "width": [], "C30": [], "gaps": set(), "bound_keys": set(), "derived": 0}
    known_gap = {g["id"] for g in C.RSPEC_GAPS.values()}
    for p in sorted(glob.glob(os.path.join(d, "*-Spec.xlsx"))):
        rep["files"] += 1
        name = os.path.basename(p)
        wb = load_workbook(p)
        toks = tagged_tokens(wb)
        for ws in wb.worksheets:
            hdr_row = 1 if ws.title.endswith("Spec") or ws.title in ("Field Options", "Population Rules") else None
            last = None
            if hdr_row:
                last = max(c.column for c in ws[hdr_row] if c.value is not None)
            for row in ws.iter_rows():
                row_rids = set(RID.findall(" ".join(str(x.value) for x in row if isinstance(x.value, str))))
                for c in row:
                    v = c.value
                    if not isinstance(v, str):
                        continue
                    loc = f"{name}!{ws.title}!{c.coordinate}"
                    if C.C29.search(v):
                        rep["C29"].append((loc, C.C29.search(v).group(0)))
                    bare = ANYTAG.sub(" ", v)
                    m = C.PIPELINE_WORDS.search(bare)
                    if m:
                        rep["WORD"].append((loc, m.group(0)))
                    for t in TAG.finditer(v):
                        rep["tags"] += 1
                        k, val = t.group(1), t.group(2)
                        rep["bound_keys"].add(k)
                        if k not in C.FACTS:
                            rep["missing_key"].append((loc, k))
                            continue
                        hit = [f for f in C.FACTS[k] if same(val, f.get("value"))]
                        if not hit:
                            rep["mismatch"].append((loc, k, val[:60]))
                        elif re.search(r"\d", val) and all(weak(f["register_id"]) for f in hit):
                            rep["C30"].append((loc, k))
                    for g in GAPTAG.findall(v):
                        rep["gaps"].add(g)
                    if POS.match(v.strip()) and ws.title.endswith("Spec") and c.column in (8, 9):
                        continue   # file positions / lengths, not fact values
                    for mm in CCS.NUM_IN_TEXT.finditer(GAPTAG.sub(" ", TAG.sub(" ", v))):
                        n = CCS._num(mm.group(1))
                        if n is None:
                            continue
                        ks = forms.get((round(n, 6), bool(mm.group(2))))
                        if ks and any(round(n, 6) in toks.get(r, ()) for r in row_rids):
                            rep["derived"] += 1
                            continue
                        if ks:
                            ctx = bare[max(0, mm.start() - 50): mm.end() + 30]
                            rep["unbound"].append((loc, mm.group(0).strip(), sorted(ks)[:2], ctx))
                    if last and c.column > last:
                        rep["width"].append(loc)
            if ws.title.endswith("Spec"):
                pop = {i: 0 for i in range(1, 22)}
                for r in range(2, ws.max_row + 1):
                    a = ws.cell(r, 1).value
                    if a is None or str(a).startswith("═══"):
                        continue
                    for i in range(1, 22):
                        if ws.cell(r, i).value not in (None, ""):
                            pop[i] += 1
                    if not ws.cell(r, 13).value:
                        rep["blankM"].append(f"{name}!{ws.title}!M{r}")
                rep["C12"][name] = sum(1 for i in pop if pop[i] > 0)
    unused = sorted(set(C.RSPEC_KEYS) - rep["bound_keys"])
    # a value with square brackets cannot be tagged; it is quoted with parentheses and its register id
    quoted = []
    if unused:
        alltext = []
        for p in sorted(glob.glob(os.path.join(d, "*-Spec.xlsx"))):
            for ws in load_workbook(p).worksheets:
                for row in ws.iter_rows():
                    alltext += [c.value for c in row if isinstance(c.value, str)]
        blob = chr(10).join(alltext)
        for k in unused:
            f = C.fact(k)
            if "]" in str(f["value"]) and (str(f["value"]).replace("[", "(").replace("]", ")") + f" [{f['register_id']}]") in blob:
                quoted.append(k)
    unused = [k for k in unused if k not in quoted]
    rep["quoted_untaggable"] = quoted
    rep["unbound_rspec_facts"] = unused
    rep["gap_ids_unknown"] = sorted(g for g in rep["gaps"] if g not in known_gap and not g.startswith("RSPEC-RQ-"))
    rep["gaps"] = sorted(rep["gaps"])
    rep["bound_keys"] = len(rep["bound_keys"])
    return rep


if __name__ == "__main__":
    r = run(sys.argv[1])
    summ = {k: (len(v) if isinstance(v, list) else v) for k, v in r.items() if k not in ("C12",)}
    summ["C12_min_columns"] = min(r["C12"].values()) if r["C12"] else None
    sys.stdout.reconfigure(encoding="utf-8")
    print(json.dumps(summ, indent=1))
    for k in ("C29", "WORD", "mismatch", "missing_key", "blankM", "width", "C30", "gap_ids_unknown"):
        for x in r[k][:15]:
            print(k, x)
    for x in r["unbound"][:60]:
        print("UNBOUND", x)
    print("UNUSED RSPEC FACTS", r["unbound_rspec_facts"])
    if "--json" in sys.argv:
        json.dump(r, open(sys.argv[sys.argv.index("--json") + 1], "w", encoding="utf-8"), indent=1, ensure_ascii=False, default=list)
