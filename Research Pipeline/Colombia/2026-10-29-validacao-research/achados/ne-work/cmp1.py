import json,re,openpyxl
rec=json.load(open('anexo_nie.json',encoding='utf-8'))
wb=openpyxl.load_workbook('C:/Users/instituto/Documents/brain-service/Research Pipeline/Colombia/co-report-crosscheck/05-final/CO-DIAN-001-NominaElectronica-Spec.xlsx')
ws=wb['Nomina Electronica Spec']
spec={}
for r in range(3,ws.max_row+1):
    code=ws.cell(r,4).value
    if code and str(code).startswith('NIE'):
        c=str(code).split()[0]
        if c in spec: print('dup',c)
        spec[c]=dict(row=r,name=ws.cell(r,2).value,F=ws.cell(r,6).value,path=ws.cell(r,8).value,len=ws.cell(r,9).value,fmt=ws.cell(r,10).value)
print(len(spec),'spec NIE codes;',len(rec),'anexo')
print('anexo not in spec:',sorted(set(rec)-set(spec)))
print('spec not in anexo:',sorted(set(spec)-set(rec)))
bad=0
for c in sorted(set(spec)&set(rec)):
    a=rec[c];s=spec[c]
    out=[]
    mn=a['oc'].split('-')[0] if a['oc'] else '?'
    if mn=='1' and s['F']!='Y': out.append(f"oc {a['oc']} vs F={s['F']}")
    if mn=='0' and s['F']=='Y': out.append(f"oc {a['oc']} vs F={s['F']}")
    sp=(s['path'] or '').replace('/@','/@')
    if a['xp'] and a['xp'].lower()!=sp.replace(' ','').lower(): out.append(f"path anexo={a['xp']} spec={sp}")
    if out: bad+=1; print(c,s['row'],a['name'][:25],'|',' ; '.join(out))
print(bad)
