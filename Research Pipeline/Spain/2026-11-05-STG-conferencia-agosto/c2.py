import sys, openpyxl
sys.stdout.reconfigure(encoding='utf-8')
D='C:/Users/instituto/Documents/brain-service/raw/tickets/api/anexos/HRBS-16884/'
for fn in ['20261104-2318 - 2608 ES03 %IRPF.xlsx','20261104-2318 - ES03 Mod 145 extraction ADP.xlsx']:
    wb=openpyxl.load_workbook(D+fn,data_only=True)
    for ws in wb.worksheets:
        print('##',fn,ws.title,ws.max_row,ws.max_column)
        for r in range(1,min(ws.max_row,8)+1):
            print([c.value for c in ws[r]])
