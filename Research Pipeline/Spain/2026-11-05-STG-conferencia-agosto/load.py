import sys, openpyxl, json
sys.stdout.reconfigure(encoding='utf-8')
G='C:/Users/instituto/Documents/brain-service/raw/tickets/api/anexos/HRBS-16884/20261105-1331 - Gross To Net Spain 2026-08-01 - 2026-08-31@05.11.xlsx'
wb=openpyxl.load_workbook(G,data_only=True)
for ws in wb.worksheets:
    print(ws.title, ws.max_row, ws.max_column)
ws=wb.worksheets[0]
hr=None
for r in range(1,30):
    vals=[c.value for c in ws[r]]
    if any(isinstance(v,str) and '62100' in v for v in vals): hr=r;break
print('hdr',hr)
hdr=[c.value for c in ws[hr]]
rows=[]
for r in range(hr+1, ws.max_row+1):
    vals=[c.value for c in ws[r]]
    if vals[0] is None: continue
    rows.append(vals)
print(len(rows))
for i,h in enumerate(hdr): 
    nz=sum(1 for x in rows if x[i] not in (None,0,'',0.0))
    print(i,h,nz)
json.dump({'hdr':hdr,'rows':[[ (v if isinstance(v,(int,float,str)) or v is None else str(v)) for v in x] for x in rows]},open('g2n.json','w',encoding='utf-8'),ensure_ascii=False)
