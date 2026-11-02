import sys, openpyxl, collections
p = sys.argv[1]
wb = openpyxl.load_workbook(p, data_only=True)
errs = []
cnt = collections.Counter()
diffs = []
for ws in wb.worksheets:
    for row in ws.iter_rows():
        for c in row:
            v = c.value
            if isinstance(v, str) and v.startswith("#") and v[1:4] in ("REF", "VAL", "NAM", "DIV", "N/A", "NUM", "NUL"):
                errs.append((ws.title, c.coordinate, v))
    # check column K (index 11) where present
    if ws.max_column >= 11:
        for r in range(1, ws.max_row + 1):
            k = ws.cell(r, 11).value
            if k in ("OK", "DIFF", "n/a"):
                cnt[k] += 1
                if k == "DIFF":
                    diffs.append((ws.title, r, ws.cell(r, 2).value, ws.cell(r, 6).value, ws.cell(r, 9).value, ws.cell(r, 10).value))
print("errors", len(errs), errs[:20])
print(cnt)
for d in diffs[:60]:
    print(d)
