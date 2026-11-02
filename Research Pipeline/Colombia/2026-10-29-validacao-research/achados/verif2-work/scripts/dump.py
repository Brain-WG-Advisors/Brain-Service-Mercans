import sys, openpyxl, os
src, out = sys.argv[1], sys.argv[2]
wb = openpyxl.load_workbook(src, data_only=False)
with open(out, 'w', encoding='utf-8') as f:
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if c.value is not None:
                    v = str(c.value).replace('\n', ' | ')
                    f.write(f"{ws.title}!{c.coordinate}\t{v}\n")
print(out)
