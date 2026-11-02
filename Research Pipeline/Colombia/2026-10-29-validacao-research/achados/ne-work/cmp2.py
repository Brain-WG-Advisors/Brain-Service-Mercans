import json,re,openpyxl
xs=[l.rstrip('\n').split('|') for l in open('xsd_flat.txt',encoding='utf-8')]
X={r[1]:r for r in xs}
def eff(path):
    # attribute required-ness and ancestors required
    r=X[path]
    own = r[3]=='1'
    anc=True
    parts=path.split('/')
    for i in range(2,len(parts)):
        pp='/'.join(parts[:i]) 
        if pp in X and X[pp][0]=='E' and X[pp][3]=='0': anc=False
    return own,anc
rec=json.load(open('anexo_nie.json',encoding='utf-8'))
wb=openpyxl.load_workbook('C:/Users/instituto/Documents/brain-service/Research Pipeline/Colombia/co-report-crosscheck/05-final/CO-DIAN-001-NominaElectronica-Spec.xlsx')
ws=wb['Nomina Electronica Spec']
rows=[]
for r in range(3,ws.max_row+1):
    code=ws.cell(r,4).value
    if code and str(code).startswith('NIE') and ws.cell(r,8).value in X:
        p=ws.cell(r,8).value; rows.append((r,str(code).split()[0],ws.cell(r,2).value,ws.cell(r,6).value,p,ws.cell(r,9).value,ws.cell(r,10).value))
print(len(rows))
for r,c,n,F,p,ln,fmt in rows:
    own,anc=eff(p)
    t=X[p][5]
    a=rec[c]
    msg=[]
    if own and anc and F!='Y': msg.append(f'XSD required (and ancestors) but spec F={F}')
    if (not own) and F=='Y': msg.append(f'XSD optional but spec F=Y')
    # type check
    f=(fmt or '')
    if t in('xsd:decimal',) and 'decimal' not in f.lower(): msg.append(f'xsd {t} vs fmt {f}')
    if t in('xsd:integer',) and not re.search(r'^N|integer|code',f,re.I): msg.append(f'xsd {t} vs fmt {f}')
    if t=='xsd:date' and 'AAAA-MM-DD' not in f: msg.append(f'xsd {t} vs fmt {f}')
    if t=='xsd:dateTime' and 'T' not in f: msg.append(f'xsd {t} vs fmt {f}')
    if t=='xsd:boolean' and 'Boolean' not in f: msg.append(f'xsd {t} vs fmt {f}')
    if t=='xsd:string' and re.match(r'^N ',f): msg.append(f'xsd string vs fmt {f}')
    # anexo type letter vs xsd
    if a['F']=='N' and t=='xsd:string': msg.append(f"Anexo F=N, XSD string (info)")
    if msg: print(r,c,n,'|',F,t,'|',f,'|',a['F'],a['tam'],'len',ln,'||',msg)
