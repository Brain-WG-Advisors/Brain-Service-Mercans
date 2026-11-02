import sys, openpyxl
sys.stdout.reconfigure(encoding='utf-8')
wb=openpyxl.load_workbook(sys.argv[1],read_only=True)
for ws in wb.worksheets:
    print('==',ws.title,ws.max_row,ws.max_column)
    for i,row in enumerate(ws.iter_rows(values_only=True)):
        if i<2: print(row); continue
        r=[str(x)[:60] if x is not None else '' for x in row]
        print(' | '.join(r[:3]), '||', ' | '.join(r[-4:]))
