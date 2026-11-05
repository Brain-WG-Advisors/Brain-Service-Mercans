import sys, openpyxl
sys.stdout.reconfigure(encoding='utf-8')
G='C:/Users/instituto/Documents/brain-service/raw/tickets/api/anexos/HRBS-16884/20261105-1331 - Gross To Net Spain 2026-08-01 - 2026-08-31@05.11.xlsx'
wb=openpyxl.load_workbook(G,data_only=True)
ws=wb.worksheets[0]
for r in range(1,14):
    print(r,[c.value for c in ws[r]][:45])
for r in range(ws.max_row-12, ws.max_row+1):
    print(r,[c.value for c in ws[r]][:12])
