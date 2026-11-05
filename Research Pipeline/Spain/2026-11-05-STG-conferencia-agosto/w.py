import sys, openpyxl, json
sys.stdout.reconfigure(encoding='utf-8')
W='C:/Users/instituto/Documents/brain-service/Research Pipeline/Spain/2026-11-02-CRA-WTC-indenizacao-v1.8/Spain_Wage_Type_Catalogue_V4.9.xlsx'
wb=openpyxl.load_workbook(W,data_only=False)
print(wb.sheetnames)
ws=wb['Wage Type Catalogue']
hr=None
for r in range(1,20):
    if ws.cell(r,1).value and 'Mercans Code' in str(ws.cell(r,1).value): hr=r;break
hdr=[c.value for c in ws[hr]]
print(hr); 
for i,h in enumerate(hdr): print(i,repr(h))
codes=json.load(open('g2n.json',encoding='utf-8'))['hdr']
codes=[str(h).split(' - ')[0] for h in codes if h]
out={}
for r in range(hr+1, ws.max_row+1):
    v=[c.value for c in ws[r]]
    if v[0] is None: continue
    out[str(v[0]).strip()]=v
json.dump({'hdr':hdr,'rows':{k:[str(x) if x is not None else None for x in v] for k,v in out.items()}},open('wtc.json','w',encoding='utf-8'),ensure_ascii=False)
missing=[c for c in codes if c not in out]
print('missing',missing)
