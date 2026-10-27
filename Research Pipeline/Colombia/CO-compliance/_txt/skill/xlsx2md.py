# -*- coding: utf-8 -*-
import sys, openpyxl, datetime

def fmt(v):
    if v is None: return ""
    if isinstance(v, (datetime.datetime, datetime.date)): return v.isoformat()[:10]
    s = str(v).replace("|", "\|").replace("\r"," ").replace("\n", "<br>").strip()
    return s

def dump(path, out, maxcol=None):
    wb = openpyxl.load_workbook(path, data_only=True)
    L = []
    L.append("# FILE: " + path.split("/")[-1])
    L.append("SHEETS: " + " || ".join(wb.sheetnames))
    for ws in wb.worksheets:
        L.append("\n\n=== SHEET: %s (dims %s, max_row %s, max_col %s) ===\n" % (ws.title, ws.dimensions, ws.max_row, ws.max_column))
        nc = ws.max_column if maxcol is None else min(ws.max_column, maxcol)
        for r in ws.iter_rows(min_row=1, max_row=ws.max_row, max_col=nc):
            vals = [fmt(c.value) for c in r]
            while vals and vals[-1] == "": vals.pop()
            if not vals: 
                L.append("~")
                continue
            L.append("R%d| " % r[0].row + " | ".join(vals))
    txt = "\n".join(L)
    open(out, "w", encoding="utf-8").write(txt)
    print(out, len(txt))

dump(sys.argv[1], sys.argv[2])
