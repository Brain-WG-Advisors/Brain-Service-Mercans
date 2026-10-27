"""Round-2 masking (v2): ONLY the files listed on the command line (names inside 02-client-reports-raw) -> 03-client-reports-masked/round2/.
Differences from mask_reports.py: header row = the row with the MOST non-empty strings in the first 25 rows; per-sheet overrides
(explicit header row, explicit column kinds, segment-based masking for Nomina Electronica layouts, whole-cell MASKED_TEXT);
header cells listed per sheet in header_name_cols are tokenised (a person's name used as a column header); the generic pure-digit rule covers 7-11 digits (cedula / NIT), while
digit runs embedded in mixed text keep the 7-15 rule; the existing key is loaded first (same raw value -> same token) and
'ID|' entries of 12-15 pure digits added by the first v1 run are pruned (ID tokens are hash-based, so pruning is lossless).
.xlsm is read values-only and written as .xlsx. Writes 04-output/round2/pii-check.txt. Never prints a cell value.
Usage: python3 scripts/mask_round2.py "<file1>" "<file2>" ..."""
import os,re,json,sys,hashlib
from openpyxl import load_workbook, Workbook
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW=os.path.join(ROOT,'02-client-reports-raw'); OUT=os.path.join(ROOT,'03-client-reports-masked','round2')
KEY=os.path.join(ROOT,'99-local-only','masking-key.json'); CHK=os.path.join(ROOT,'04-output','round2','pii-check.txt')
os.makedirs(OUT,exist_ok=True); os.makedirs(os.path.dirname(CHK),exist_ok=True)
src=open(os.path.join(ROOT,'scripts','mask_reports.py'),encoding='utf-8').read()
defs=src.split('for f in sorted(glob.glob')[0]
defs='\n'.join(l for l in defs.splitlines() if not l.startswith(('RAW=','OUT=','KEY=','CHK=','os.makedirs')))
exec(defs)   # RULES, EXCLUDE, key, counters, token(), EMAIL, SAFE, NAMEISH
RULES=[(k,(rx+'|cod employee|cod\\.? ?empleado' if k=='ID' else rx)) for k,rx in RULES]
if os.path.exists(KEY):
    loaded=json.load(open(KEY,encoding='utf-8'))
    pruned=sum(1 for k in loaded if re.fullmatch(r'ID\|\d{12,15}',k))
    key.update({k:v for k,v in loaded.items() if not re.fullmatch(r'ID\|\d{12,15}',k)})
    for v in key.values():
        m=re.fullmatch(r'([A-Z]+)_(\d{4})',str(v))
        if m: counters[m.group(1)]=max(counters.get(m.group(1),0),int(m.group(2)))
        m=re.fullmatch(r'user(\d{4})@masked\.example',str(v))
        if m: counters['EMAIL']=max(counters.get('EMAIL',0),int(m.group(1)))
else: pruned=0
def best_header_row(ws):
    best=None;bn=2
    for r in range(1,min(ws.max_row,25)+1):
        n=sum(1 for c in range(1,ws.max_column+1) if isinstance(ws.cell(r,c).value,str) and ws.cell(r,c).value.strip()!='')
        if n>bn: best,bn=r,n
    return best
BOOL={'true','false','si','no','yes','x'}
LABEL=re.compile(r'^\d{1,2}\.\s|certificado|antes de|informaci[oó]n|n[uú]mero|c[oó]digo|verificaci|apellido|nombre|tipo|fecha|valor|total|firma|ciudad|pa[ií]s|departamento|entidad|concepto|periodo|per[ií]odo|empleador|raz[oó]n social|nit\b|dv\b|a[ñn]o',re.I)
# per-sheet overrides: header row, column kinds (letters), segment rules (key column, key value, columns -> kind), masked_text cells
CFG={
 'Formulario 220.xlsm':{'NOM_U_203':{'header':2,'cols':{'C':'ID','D':'NAME','E':'NAME','F':'NAME','G':'NAME'}},
                        'DATOS':{'header':None,'free':{'rows':(7,12),'name_cols':'BCDEF'}},
                        'CIR 2024':{'header':None,'free':{'rows':(5,20),'name_cols':None}}},
 'Gross to net PMI 2026-09-01-2026-09-30 - Monthly.xlsx':{'Gross to net PMI':{'header':12,'cols':{'A':'ID','B':'NAME','C':'ID','D':'ACCOUNT'}}},
 'Monthly_fixed.xlsx':{'Nómina':{'header':None,'no_inline':True,'segment':{'key_col':'A','ENC':{'I':'ID'},'REC':{'D':'NAME','G':'NAME','H':'NAME','I':'NAME','J':'NAME','N':'ADDRESS','F':'ID','R':'ID'},'PAG':{'F':'ACCOUNT'}}}},
 'Validado ConsolidadoCCT_ Monthly  sep.xlsx':{
    'ConsolidadoCCT':{'header':None,'no_inline':True,'cols':{'C':'NAME'},'embedded_id_cols':['E'],'segment':{'key_col':'I','ENC':{'Q':'ID'},'REC':{'L':'NAME','O':'NAME','P':'NAME','Q':'NAME','R':'NAME','V':'ADDRESS','N':'ID','Z':'ID'},'PAG':{'N':'ACCOUNT'}}},
    'Acumulados':{'header':7,'cols':{'A':'ID','B':'NAME','C':'ID','D':'ID','E':'NAME','Y':'NAME'},'header_name_cols':['Y'],'embedded_id_cols':['Z','AD']},
    'Pivot check ':{'header':4,'cols':{'A':'NAME','B':'ID'}},
    'Sheet1':{'header':1,'cols':{'A':'NAME','C':'NAME'}},
    'Validacion netos':{'header':1,'cols':{'C':'NAME'},'embedded_id_cols':['E']},
    'Mapping':{'header':1,'namelike_cols':['F']},
    'Sheet2':{'header':None,'cols':{'C':'NAME'},'masked_text':['B9','B12']}}}
from openpyxl.utils import column_index_from_string as cidx, get_column_letter as cl
n_before=len(key); susp={}; done=[]; stats={}
for name in sys.argv[1:]:
    f=os.path.join(RAW,name)
    if not os.path.exists(f): print('NOT FOUND:',name); continue
    wb=load_workbook(f,data_only=True); out=Workbook(); out.remove(out.active); fcfg=CFG.get(name,{})
    for ws in wb:
        o=out.create_sheet(ws.title[:31]); scfg=fcfg.get(ws.title,{})
        hr=scfg['header'] if 'header' in scfg else best_header_row(ws)
        kinds={}
        if hr:
            for c in range(1,ws.max_column+1):
                h=str(ws.cell(hr,c).value or '').strip().lower()
                if not h or re.search(EXCLUDE,h): continue
                for kind,rx in RULES:
                    if re.search(rx,h): kinds[c]=kind; break
        for L,k in scfg.get('cols',{}).items(): kinds[cidx(L)]=k
        seg=scfg.get('segment'); free=scfg.get('free'); mt=set(scfg.get('masked_text',[]))
        cnt={'col-rule':0,'segment':0,'free':0,'header-name':0,'inline':0,'masked_text':0}
        for row in ws.iter_rows():
            for cell in row:
                v=cell.value
                if v is None: continue
                c=cell.column; r=cell.row; sv=str(v).strip()
                if cell.coordinate in mt: v='MASKED_TEXT'; cnt['masked_text']+=1
                elif hr and r==hr and cl(c) in scfg.get('header_name_cols',[]) and isinstance(v,str) and sv!='':
                    v=token('NAME',v); cnt['header-name']+=1
                elif (not hr or r>hr) and c in kinds and sv!='' and not (kinds[c]=='NAME' and sv.lower() in BOOL):
                    v=token(kinds[c],v); cnt['col-rule']+=1
                elif seg and str(ws.cell(r,cidx(seg['key_col'])).value or '').strip() in seg and cl(c) in seg[str(ws.cell(r,cidx(seg['key_col'])).value).strip()] and sv!='':
                    k=seg[str(ws.cell(r,cidx(seg['key_col'])).value).strip()][cl(c)]
                    if not (k in('NAME','ADDRESS') and (sv.lower() in BOOL or re.fullmatch(r'[\d.,\-]+',sv))): v=token(k,v); cnt['segment']+=1
                elif cl(c) in scfg.get('namelike_cols',[]) and isinstance(v,str) and NAMEISH.match(sv) and (not hr or r>hr):
                    v=token('NAME',v); cnt['col-rule']+=1
                elif free and free['rows'][0]<=r<=free['rows'][1] and isinstance(v,str) and sv!='' and not LABEL.search(sv) and (free['name_cols'] is None or cl(c) in free['name_cols']):
                    v=token('ID',v) if re.fullmatch(r'\d{5,15}',sv) else token('NAME',v); cnt['free']+=1
                elif free and free['rows'][0]<=r<=free['rows'][1] and isinstance(v,(int,float)) and 10000<=abs(v)<10**15 and float(v).is_integer():
                    v=token('ID',str(int(v))); cnt['free']+=1
                elif cl(c) in scfg.get('embedded_id_cols',[]) and isinstance(v,str) and (not hr or r>hr):
                    v2=re.sub(r'(?<!\d)\d{7,11}(?!\d)',lambda m: token('ID',m.group(0)),v)
                    if v2!=v: cnt['inline']+=1
                    v=v2
                elif isinstance(v,str) and not scfg.get('no_inline'):
                    v2=EMAIL.sub(lambda m: token('EMAIL',m.group(0)),v)
                    v2=re.sub(r'\b\d{7,11}\b',lambda m: token('ID',m.group(0)),v2) if re.fullmatch(r'\d+',sv) else re.sub(r'\b\d{7,15}\b',lambda m: token('ID',m.group(0)),v2)
                    if v2!=v: cnt['inline']+=1
                    v=v2
                    hdr=str(ws.cell(hr,c).value or '') if hr else ''
                    if (not hr or r>hr) and NAMEISH.match(sv) and not SAFE.search(hdr):
                        k=(name,ws.title,cell.column_letter,hdr); susp[k]=susp.get(k,0)+1
                o.cell(r,c,v)
        stats[(name,ws.title)]=(hr,cnt)
    outname=re.sub(r'\.xlsm$','.xlsx',name); out.save(os.path.join(OUT,outname)); done.append(outname); print('masked',name,'->',outname)
json.dump(key,open(KEY,'w'),ensure_ascii=False,indent=0)
with open(CHK,'w') as fh:
    fh.write('Round 2 masking (v2) of: '+', '.join(done)+'\n')
    for (fn,sh),(hr,cnt) in stats.items(): fh.write(f'{fn} | {sh} | header_row={hr} | masked cells: {cnt}\n')
    fh.write(f'\nColumns with values that look like personal names (job titles, departments, EPS, banks, cities and nationalities are excluded): {len(susp)}\n')
    for (fn,sh,col,h),n in sorted(susp.items()): fh.write(f'{fn} | {sh} | column {col} | header="{h}" | {n} cells\n')
print(f'Done. Key entries: {n_before} (after pruning {pruned} 12-15-digit ID entries) -> {len(key)}. Check {os.path.relpath(CHK,ROOT)}')
