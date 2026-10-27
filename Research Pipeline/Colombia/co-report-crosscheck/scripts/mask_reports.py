"""Masks personal data in the client's reports LOCALLY (no AI involved).
Reads 02-client-reports-raw/*.xlsx, writes 03-client-reports-masked/*.xlsx (values only, same sheets and cell positions),
keeps the raw->token key in 99-local-only/masking-key.json and writes 04-output/pii-check.txt with any remaining suspected names.
PDFs are NOT processed (names cannot be masked reliably); they are listed for manual review.
Usage: python3 scripts/mask_reports.py"""
import os,re,json,glob,hashlib
from openpyxl import load_workbook, Workbook
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW=os.path.join(ROOT,'02-client-reports-raw'); OUT=os.path.join(ROOT,'03-client-reports-masked')
KEY=os.path.join(ROOT,'99-local-only','masking-key.json'); CHK=os.path.join(ROOT,'04-output','pii-check.txt')
os.makedirs(OUT,exist_ok=True); os.makedirs(os.path.dirname(KEY),exist_ok=True); os.makedirs(os.path.dirname(CHK),exist_ok=True)
RULES=[('NAME',r'nombre|name|apellid|^employee$|^empleado$|manager|supervisor|jefe|approver|aprobador|reports to|responsable|elaborad|revisad|aprobad|emplead[oa]\s*$|trabajador|beneficiari|funcionario|colaborador|razon social del empleado|enterprise id|login|user id'),
       ('ID',r'c[eé]dula|documento|identificaci|n[uú]mero de id|id number|nro\.?\s*doc|num\.?\s*doc|^nit$|^id$|employee id|c\.c\.|^cc$|nuip|citizenship card|national id'),
       ('ACCOUNT',r'cuenta|account|iban|n[uú]mero de cuenta|nro\.?\s*cuenta'),
       ('EMAIL',r'correo|e-?mail'),('PHONE',r'tel[eé]fono|phone|celular|m[oó]vil'),
       ('ADDRESS',r'direcci[oó]n|address|domicilio'),('DOB',r'nacimiento|birth')]
EXCLUDE=r'^\d{4,5}\s*-|tipo|type|c[oó]digo de|code|banco$|bank name|entidad|fondo|eps|afp|arl|ccf|concepto|cargo|centro|provider|company|empresa|department|division|job title|position'
key={}; counters={}
def token(kind,val):
    k=f'{kind}|{val}'
    if k in key: return key[k]
    counters[kind]=counters.get(kind,0)+1; n=counters[kind]; s=str(val)
    if kind in('ID','ACCOUNT','PHONE'):
        h=hashlib.sha256(k.encode()).hexdigest(); digits=''.join(str(int(c,16)%10) for c in h)
        t=''.join(digits[i%len(digits)] if ch.isdigit() else ch for i,ch in enumerate(s))
    elif kind=='EMAIL': t=f'user{n:04d}@masked.example'
    elif kind=='DOB': t='1900-01-01'
    else: t=f'{kind}_{n:04d}'
    key[k]=t; return t
def header_row(ws):
    for r in range(1,min(ws.max_row,25)+1):
        vals=[ws.cell(r,c).value for c in range(1,ws.max_column+1)]
        if sum(isinstance(v,str) and v.strip()!='' for v in vals)>=3: return r
    return None
EMAIL=re.compile(r'[\w.+-]+@[\w-]+\.[\w.]+')
susp={}
SAFE=re.compile(r'job|title|cargo|depart|divisi|[aá]rea|function|funci[oó]n|eps|afp|arl|ccf|caja|provider|bank|banco|city|ciudad|municip|nationality|nacionalidad|country|pa[ií]s|company|empresa|cost cent|centro de costo|location|ubicaci|sede|concept|descrip|position|posici|status|estado|tipo|type|grupo|group|level|nivel|payroll|n[oó]mina|contract|contrato|currency|moneda|frequen|frecuen|legal entity|entidad|fondo|fund|sucursal|branch|gender|g[eé]nero|marital|civil',re.I)
NAMEISH=re.compile(r"^[A-ZÁÉÍÓÚÑ][A-Za-zÁÉÍÓÚÑáéíóúñ'\-]+(\s+[A-ZÁÉÍÓÚÑ][A-Za-zÁÉÍÓÚÑáéíóúñ'\-]+){1,4}$")
for f in sorted(glob.glob(os.path.join(RAW,'*.xlsx'))):
    wb=load_workbook(f,data_only=True); out=Workbook(); out.remove(out.active)
    for ws in wb:
        o=out.create_sheet(ws.title[:31]); hr=header_row(ws); kinds={}
        if hr:
            for c in range(1,ws.max_column+1):
                h=str(ws.cell(hr,c).value or '').strip().lower()
                if not h or re.search(EXCLUDE,h): continue
                for kind,rx in RULES:
                    if re.search(rx,h): kinds[c]=kind; break
        for row in ws.iter_rows():
            for cell in row:
                v=cell.value
                if v is None: continue
                c=cell.column
                if hr and cell.row>hr and c in kinds and str(v).strip()!='': v=token(kinds[c],v)  # ID/ACCOUNT/PHONE columns: whole value is digit-substituted, whatever its length
                elif isinstance(v,str):
                    v=EMAIL.sub(lambda m: token('EMAIL',m.group(0)),v)
                    v=re.sub(r'\b\d{7,15}\b',lambda m: token('ID',m.group(0)),v)
                    hdr=str(ws.cell(hr,c).value or '') if hr else ''
                    if hr and cell.row>hr and NAMEISH.match(v.strip()) and not SAFE.search(hdr):
                        k=(os.path.basename(f),ws.title,cell.column_letter,hdr); susp[k]=susp.get(k,0)+1
                o.cell(cell.row,cell.column,v)
    out.save(os.path.join(OUT,os.path.basename(f)))
    print('masked',os.path.basename(f))
json.dump(key,open(KEY,'w'),ensure_ascii=False,indent=0)
pdfs=[os.path.basename(p) for p in glob.glob(os.path.join(RAW,'*.pdf'))]
with open(CHK,'w') as fh:
    fh.write('PDFs not processed (review by hand, not by Claude):\n'+'\n'.join(pdfs)+'\n\n')
    fh.write(f'Columns with values that look like personal names (job titles, departments, EPS, banks, cities and nationalities are excluded): {len(susp)}\n')
    for (fn,sh,col,h),n in sorted(susp.items()): fh.write(f'{fn} | {sh} | column {col} | header="{h}" | {n} cells\n')
print(f'Done. Key: 99-local-only/masking-key.json ({len(key)} values). Check 04-output/pii-check.txt before running the agents.')
