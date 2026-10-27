import sys, openpyxl
wb = openpyxl.load_workbook(sys.argv[1], data_only=False)
maxr = int(sys.argv[3]) if len(sys.argv) > 3 else 100000
out = []
out.append("WORKBOOK: %s" % sys.argv[1])
out.append("SHEETS(%d): %s" % (len(wb.sheetnames), wb.sheetnames))
for ws in wb.worksheets:
    out.append("\n===== SHEET '%s'  dims=%s  max_row=%s max_col=%s =====" % (ws.title, ws.dimensions, ws.max_row, ws.max_column))
    n = 0
    for row in ws.iter_rows():
        n += 1
        if n > maxr:
            out.append("... truncated at %d rows" % maxr)
            break
        vals = []
        for c in row:
            v = c.value
            if v is None:
                v = ""
            vals.append(str(v).replace("\n", "\\n"))
        while vals and vals[-1] == "":
            vals.pop()
        if not vals:
            continue
        out.append("R%d| %s" % (n, " ~ ".join(vals)))
open(sys.argv[2], "w", encoding="utf-8").write("\n".join(out))
print("wrote", sys.argv[2], len(out))
