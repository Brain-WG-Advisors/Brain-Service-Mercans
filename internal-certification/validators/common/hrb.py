"""Generic HRBLIZZ report readers (G2N 'Employee ID' row layout; GL Report layout)."""
import pandas as pd

from framework import num


def _engine(p):
    p = p.lower()
    return "xlrd" if p.endswith(".xls") else ("odf" if p.endswith(".ods") else "openpyxl")


def read_g2n(path):
    """Header block (label | value) on top, then a row with 'Employee ID' (section labels) and a row with
    pay-element labels. Returns header dict, ordered employee dicts keyed by 'Employee ID', 'Employee name',
    ..., section names (e.g. 'Gross Pay', 'Net Pay') and pay elements ('62100 - Salary'), plus a totals row
    if present (first column empty/'Total')."""
    df = pd.read_excel(path, header=None, dtype=object, engine=_engine(path))
    vals = [[None if (isinstance(x, float) and pd.isna(x)) else x for x in r] for r in df.values.tolist()]
    hi = next(i for i, r in enumerate(vals) if r and str(r[0]).strip() == "Employee ID")
    header = {}
    for r in vals[:hi]:
        if r[0] is not None:
            header[str(r[0]).strip()] = r[1]
    sec, sub = vals[hi], vals[hi + 1]
    start = hi + 2
    if sub and sub[0] is not None and str(sub[0]).strip():
        # single header row (element labels on the 'Employee ID' row); the row above may hold sections
        sub, start = sec, hi + 1
    keys, cur = [], None
    for j in range(len(sec)):
        s = None if sec[j] is None else str(sec[j]).strip()
        b = None if (j >= len(sub) or sub[j] is None) else str(sub[j]).strip()
        if s:
            cur = s
        keys.append(b if b else (s if s else cur))
    emps, totals = [], None
    for r in vals[start:]:
        if all(x is None or str(x).strip() == "" for x in r):
            continue
        first = None if r[0] is None else str(r[0]).strip()
        d = {keys[j]: r[j] for j in range(min(len(keys), len(r))) if keys[j]}
        if first and first.lower() == "confidential":
            continue
        if not first or first.lower().startswith(("total", "grand total")):
            totals = d
            continue
        d["Employee ID"] = first
        emps.append(d)
    return {"header": header, "keys": keys, "emps": emps, "totals": totals}


def code(emp, c):
    """Amount of pay element by code (e.g. '62100'); 0.0 if absent."""
    c = str(c)
    for k, v in emp.items():
        if isinstance(k, str) and (k.startswith(c + " - ") or k == c):
            return num(v) or 0.0
    return 0.0


def read_gl_report(path, sheet=0):
    """HRBLIZZ 'GL Report': header block, then a row starting with 'GL Code'."""
    df = pd.read_excel(path, header=None, dtype=object, engine=_engine(path), sheet_name=sheet)
    vals = [[None if (isinstance(x, float) and pd.isna(x)) else x for x in r] for r in df.values.tolist()]
    hi = next(i for i, r in enumerate(vals) if r and str(r[0]).strip() in ("GL Code", "GL Account", "Account", "Country Code"))
    hdr = [None if x is None else str(x).strip() for x in vals[hi]]
    header = {str(r[0]).strip(): r[1] for r in vals[:hi] if r and r[0] is not None}
    lines, foot = [], None
    for r in vals[hi + 1:]:
        if all(x is None for x in r):
            continue
        d = dict(zip(hdr, r))
        if d.get(hdr[0]) is None:
            if foot is None:
                foot = d
            continue
        if str(d.get(hdr[0])).strip().lower() in ("confidential",):
            continue
        lines.append(d)
    return {"header": header, "cols": hdr, "lines": lines, "footer": foot}
