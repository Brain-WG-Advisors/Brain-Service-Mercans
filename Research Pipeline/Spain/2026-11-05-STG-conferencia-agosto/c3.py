import sys, openpyxl
sys.stdout.reconfigure(encoding='utf-8')
D='C:/Users/instituto/Documents/brain-service/raw/tickets/api/anexos/HRBS-16884/'
wb=openpyxl.load_workbook(D+'20261104-2318 - ES03 Mod 145 extraction ADP.xlsx',data_only=True)
ws=wb['Family Situation']
for r in range(8,ws.max_row+1):
    v=[c.value for c in ws[r]]; v[1]=None if len(v)>1 else None
    print(v)
ws=wb['Mod 145 updated']
for r in range(1,ws.max_row+1):
    v=[c.value for c in ws[r]]; 
    print(v[0],v[2],v[4],v[5],v[6],v[7],v[8])
