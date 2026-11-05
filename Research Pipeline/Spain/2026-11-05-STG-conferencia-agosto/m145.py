import openpyxl, json
D='C:/Users/instituto/Documents/brain-service/raw/tickets/api/anexos/HRBS-16884/'
wb=openpyxl.load_workbook(D+'20261104-2318 - ES03 Mod 145 extraction ADP.xlsx',data_only=True)
ws=wb['Mod 145 updated']
M={}; cur=None
for r in range(2,ws.max_row+1):
    v=[c.value for c in ws[r]]
    if v[0] is None: continue
    k=str(v[0]).strip()
    m=M.setdefault(k,{'sit':None,'fam':[],'alim':None,'viv':None,'entero':None})
    if v[2] is not None: m['sit']=v[2]
    if v[4] is not None: m['fam'].append((v[4],v[3].strip() if v[3] else ''))
    if v[6]: m['alim']=v[6]
    if v[7]: m['viv']=v[7]
    if v[8]: m['entero']=v[8]
ws=wb['Family Situation']
F={}
for r in range(12,ws.max_row+1):
    v=[c.value for c in ws[r]]
    if v[0] is None: continue
    k=str(v[0]).strip()
    if len(k)==6: k='1'+k
    F.setdefault(k,[]).append(v[4])
json.dump({'M':M,'F':F},open('m145.json','w'))
