import sys, openpyxl
sys.stdout.reconfigure(encoding='utf-8')
wb=openpyxl.load_workbook(sys.argv[1],read_only=True)
for ws in wb.worksheets:
    for r in ws.iter_rows():
        for c in r:
            v=c.value
            if isinstance(v,str) and ('discretion' in v.lower() or 'Discretionary bonus' in v):
                print(ws.title,c.coordinate,v[:200])
ws=wb['Wage Type Catalogue']
rows=list(ws.iter_rows(min_row=226,max_row=232,values_only=True))
for r in rows: print([str(x)[:50] for x in r[:6]])
