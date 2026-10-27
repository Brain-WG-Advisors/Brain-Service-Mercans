"""Dump every non-empty cell (value + fill) of a workbook. Usage: dump.py <xlsx> <out.txt>"""
import sys, openpyxl
wb = openpyxl.load_workbook(sys.argv[1])
with open(sys.argv[2], "w", encoding="utf-8") as out:
    for ws in wb.worksheets:
        out.write(f"##### SHEET {ws.title} dims={ws.dimensions} state={ws.sheet_state}\n")
        for row in ws.iter_rows():
            for c in row:
                if c.value is not None:
                    v = str(c.value).replace("\n", "\n")
                    out.write(f"{c.coordinate}\t{v}\n")
