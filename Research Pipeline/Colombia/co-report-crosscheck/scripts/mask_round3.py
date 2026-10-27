"""Round-3 masking (v3): the '16oct' files in 02-client-reports-raw -> 03-client-reports-masked/round3/.
Runs LOCALLY; never prints a cell value. Steps:
1. sha256 of every raw file; a 16oct file identical to an earlier raw file or to another 16oct file is SKIPPED (listed in the check file).
2. Tabular files (Base of Withholding, Gross to net, Formato 2276): header-row rules of mask_reports.py + explicit column kinds.
3. Termination settlements (Liquidacion ...): every sheet is processed in 'shape' mode - a text cell is kept ONLY when it is a concept
   label (all words in the payroll vocabulary, or a '<WT code> - <description>' label, or the WT-description column of the WT tables);
   every other text becomes NAME_nnnn (3+ capitalised words) or MASKED_TEXT; digit-only strings of 5+ digits and integers of 5+ digits in
   the identification blocks become ID tokens; dates and amounts are kept; 7-15 digit runs embedded in text are digit-substituted.
Key: existing 99-local-only/masking-key.json is loaded first (same raw value -> same token) and saved back.
Writes 04-output/round3/pii-check.txt (statistics only). Usage: python3 scripts/mask_round3.py [--dry]"""
import os,re,sys,json,hashlib,unicodedata,collections
from openpyxl import load_workbook, Workbook
from openpyxl.utils import get_column_letter as GL, column_index_from_string as cidx
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW=os.path.join(ROOT,'02-client-reports-raw'); OUT=os.path.join(ROOT,'03-client-reports-masked','round3')
KEY=os.path.join(ROOT,'99-local-only','masking-key.json'); CHK=os.path.join(ROOT,'04-output','round3','pii-check.txt')
os.makedirs(OUT,exist_ok=True); os.makedirs(os.path.dirname(CHK),exist_ok=True)
src=open(os.path.join(ROOT,'scripts','mask_reports.py'),encoding='utf-8').read()
defs=src.split('for f in sorted(glob.glob')[0]
defs='\n'.join(l for l in defs.splitlines() if not l.startswith(('RAW=','OUT=','KEY=','CHK=','os.makedirs')))
exec(defs)   # RULES, EXCLUDE, key, counters, token(), EMAIL, SAFE, NAMEISH
RULES=[(k,(rx+'|cod employee|cod\\.? ?empleado' if k=='ID' else rx)) for k,rx in RULES]
if os.path.exists(KEY):
    key.update(json.load(open(KEY,encoding='utf-8')))
    for v in key.values():
        m=re.fullmatch(r'([A-Z]+)_(\d{4})',str(v))
        if m: counters[m.group(1)]=max(counters.get(m.group(1),0),int(m.group(2)))
        m=re.fullmatch(r'user(\d{4})@masked\.example',str(v))
        if m: counters['EMAIL']=max(counters.get('EMAIL',0),int(m.group(1)))
n_key_before=len(key)
# ---------- vocabulary for the settlement forms (a text cell is a label only if every word is here) ----------
VOC=open(os.path.join(ROOT,'scripts','probe_round3.py'),encoding='utf-8').read().split('VOCAB=set("""')[1].split('""".split())')[0].split()
VOCAB=set(VOC)|set("""ultimas ultimo ultima disfrutados disfrutadas disfrute causados causadas causacion pendiente proporcional proporcionales
legal legales extralegal extralegales compensacion compensadas compensada descanso remuneradas remunerado remunerada pagadas pagados liquidadas
liquidados acumulado acumulados acumulada promedio promedios mensual mensuales anual anuales diario diaria semestre semestral trimestre laborados
trabajados trabajadas calendario habiles novedad novedades ajuste ajustes reintegro reintegros devolucion devoluciones favor contra antiguedad
causal justa motivo renuncia despido mutuo acuerdo vencimiento obra labor termino indefinido definido aprendizaje practica practicante
fija fijo variable sin con parcial completo completa mes meses dia dias valor valores base bases porcentaje % total totales neto bruto pagar
pagos descuentos deducciones devengos devengados retenciones aportes seguridad social eps afp arl ccf sena icbf caja compensacion familiar
parafiscales fondo fondos solidaridad subsistencia pension pensional pensiones salud riesgos laborales retencion fuente renta gravable exenta exento
cuantia cesantias cesantia intereses interes prima primas servicios vacaciones vacacion indemnizacion indemnizaciones sancion moratoria
salario salarios sueldo basico basica integral transporte auxilio auxilios conectividad alimentacion bonificacion bonificaciones bono bonos
comision comisiones horas extras extra recargo recargos nocturno dominical festivo festivos incapacidad incapacidades licencia licencias
maternidad paternidad enfermedad general prestamo prestamos libranza embargo embargos cuota cuotas saldo saldos anticipo anticipos
concepto conceptos codigo codigos cantidad unidad tarifa tasa factor formula cuenta banco bancos transferencia cheque efectivo
empresa empleador compania sociedad nit razon social empleado empleada trabajador trabajadora colaborador cargo centro costo costos area
departamento division ubicacion documento identificacion cedula tipo numero numeros apellido apellidos nombre nombres primer segundo otros
fecha fechas ingreso egreso retiro inicio fin desde hasta periodo periodos semana semanas quincena ano anos contrato contratos terminacion
liquidacion liquidaciones final definitiva observaciones observacion notas nota firma firmas elaborado revisado aprobado el la los las de del
y o a en con por para un una al que se su sus e no si
amount amounts employee employees name names full first last id number type date dates code codes description payroll run reference withholding
tax taxable exempt income deduction deductions contribution contributions pension health fund funds severance interest premium bonus vacation
vacations termination settlement hire start end status group subgroup weekly monthly month year company legal entity cost center centre
department position title currency cop cod national bank account leaving effective days worked on leave wt wage concept nature accrual accruals
provision provisions balance previous current ytd to indemnity compensation sanction final liquidation reason resignation dismissal mutual
agreement expiry fixed term indefinite apprentice intern internship allowance transportation reunification cash out payment loan loans union
insurance prepaid solidarity subsistence theoretical contingent with without average annual semester basic integral variable salary assigned
ordinary legal retention percentage others obligatory dependents exemption voluntary gross net total subtotal entitlements earnings non social
security bases employer jan feb mar apr may jun jul aug sep oct nov dec january february march april june july august september october november
december pct renta ibc check validation diff difference ok""".split())
def strip(s): return ''.join(c for c in unicodedata.normalize('NFD',s) if unicodedata.category(c)!='Mn').lower()
def safe(s):
    words=re.findall(r'[A-Za-zÁÉÍÓÚÑáéíóúñÜü]+',s)
    return (not words) or all(strip(w) in VOCAB for w in words)
WTPAT=re.compile(r'^\s*\d{3,5}\s*-\s*\S')
CAPWORDS=re.compile(r"^[A-ZÁÉÍÓÚÑ][A-Za-zÁÉÍÓÚÑáéíóúñ'\-]*(\s+[A-ZÁÉÍÓÚÑ][A-Za-zÁÉÍÓÚÑáéíóúñ'\-]*){2,5}$")
def sub_digits(v):
    return re.sub(r'(?<!\d)\d{7,15}(?!\d)',lambda m: token('ID',m.group(0)),v)
# ---------- per-file configuration ----------
G2N={'Gross to net PMI':{'header':12,'cols':{'A':'ID','B':'NAME','C':'ID','D':'ACCOUNT'}}}
BOW={'Base of Withholding':{'header':12,'cols':{'A':'ID','B':'NAME'}}}
LIQ={'Liquidacion':{'mode':'shape','id_block':(1,10),'value_cols_in_block':'CDEFGHIJ'},
     'Acumulados- Prestaciones':{'mode':'shape','cols':{'A':'ID','B':'NAME','C':'ID','D':'ID','E':'TEXT'},'keep_cols':{'F','G'},'repeat_header':r'^ID Number$'},
     'Acumulados':{'mode':'shape','cols':{'A':'ID','B':'NAME','C':'ID','D':'ID','E':'TEXT'},'keep_cols':{'F','G'},'repeat_header':r'^ID Number$'},
     'Accruals':{'mode':'shape','cols':{'A':'ID','B':'NAME'},'keep_cols':{},'repeat_header':r'^ID Number$'},
     'Net Mes - Salario':{'mode':'shape','id_block':(1,5),'value_cols_in_block':'B'},
     'Naturaleza conceptos':{'mode':'keep'},
     'Sheet1':{'mode':'shape'}}
CFG={'1764_PMI_Base of Withholding 2026-09-01 - 2026-09-30 (1) - 16oct.xlsx':BOW,
     '1764_PMI_Base of Withholding 2026-09-01 - 2026-09-30 - Weekly (1) - 16oct.xlsx':BOW,
     'Formato 2276 - Preliminar - Envio - 16oct.xlsx':{'2276':{'header':1,'explicit_only':True,'cols':{'C':'ID','D':'NAME','E':'NAME','F':'NAME','G':'NAME','H':'ADDRESS'}}},
     'Gross to net PMI 2026-09-01-2026-09-30 - 16oct.xlsx':G2N,
     'Gross to net PMI 2026-09-01-2026-09-30 - Monthly (1) - 16oct.xlsx':G2N,
     'Gross to net PMI 2026-10-01-2026-10-31 - 16oct.xlsx':G2N,
     'Liquidacion termination 1 - 16oct.xlsx':LIQ,'Liquidacion termination 2 - 16oct.xlsx':LIQ}
BOOL={'true','false','si','no','yes','x','n/a','na','-'}
# ---------- step 1: hashes ----------
h={n:hashlib.sha256(open(os.path.join(RAW,n),'rb').read()).hexdigest() for n in sorted(os.listdir(RAW)) if os.path.isfile(os.path.join(RAW,n)) and not n.startswith('.')}
new=[n for n in h if '16oct' in n]; old=[n for n in h if '16oct' not in n]
todo=[]; skipped=[]
for n in new:
    so=[o for o in old if h[o]==h[n]]; sn=[o for o in todo if h[o]==h[n]]
    if so: skipped.append((n,'identical to earlier raw file: '+', '.join(so)))
    elif sn: skipped.append((n,'identical to 16oct file: '+', '.join(sn)))
    else: todo.append(n)
lines=['Round 3 masking (v3) of the 16oct files - '+str(len(todo))+' distinct files masked, '+str(len(skipped))+' identical copies skipped','']
for n,why in skipped: lines.append(f'SKIPPED {n} -> {why}')
lines.append('')
def best_header_row(ws):
    best=None;bn=2
    for r in range(1,min(ws.max_row,25)+1):
        n=sum(1 for c in range(1,ws.max_column+1) if isinstance(ws.cell(r,c).value,str) and ws.cell(r,c).value.strip()!='')
        if n>bn: best,bn=r,n
    return best
susp={}; stats={}
for name in todo:
    f=os.path.join(RAW,name); wb=load_workbook(f,data_only=True); out=Workbook(); out.remove(out.active); fcfg=CFG.get(name,{})
    for ws in wb:
        o=out.create_sheet(ws.title[:31]); scfg=fcfg.get(ws.title,{}); mode=scfg.get('mode','table')
        cnt=collections.Counter(); maxc=min(ws.max_column, 60 if mode in('shape','keep') else ws.max_column)
        if mode=='table':
            hr=scfg['header'] if 'header' in scfg else best_header_row(ws); kinds={}
            if hr and not scfg.get('explicit_only'):
                for c in range(1,ws.max_column+1):
                    hd=str(ws.cell(hr,c).value or '').strip().lower()
                    if not hd or re.search(EXCLUDE,hd): continue
                    for kind,rx in RULES:
                        if re.search(rx,hd): kinds[c]=kind; break
            for L,k in scfg.get('cols',{}).items(): kinds[cidx(L)]=k
            for row in ws.iter_rows():
                for cell in row:
                    v=cell.value
                    if v is None: continue
                    c=cell.column; r=cell.row; sv=str(v).strip()
                    if hr and r>hr and c in kinds and sv!='' and not (kinds[c]=='NAME' and sv.lower() in BOOL):
                        v=token(kinds[c],v); cnt['col-rule']+=1
                    elif isinstance(v,str) and scfg.get('explicit_only') and hr and r>hr: pass   # codes / amounts stored as text stay as they are
                    elif isinstance(v,str):
                        v2=EMAIL.sub(lambda m: token('EMAIL',m.group(0)),v)
                        v2=re.sub(r'\b\d{7,11}\b',lambda m: token('ID',m.group(0)),v2) if re.fullmatch(r'\d+',sv) else sub_digits(v2)
                        if v2!=v: cnt['inline']+=1
                        v=v2; hd=str(ws.cell(hr,c).value or '') if hr else ''
                        if (not hr or r>hr) and NAMEISH.match(sv) and not SAFE.search(hd):
                            k=(name,ws.title,GL(c),hd); susp[k]=susp.get(k,0)+1
                    o.cell(r,c,v)
            stats[(name,ws.title)]=('table',hr,dict(cnt)); continue
        # ---- settlement workbooks: 'keep' (WT nature table) or 'shape' ----
        cols={cidx(L):k for L,k in scfg.get('cols',{}).items()}; keep_cols={cidx(L) for L in scfg.get('keep_cols',set())}
        blk=scfg.get('id_block'); vcols=set(scfg.get('value_cols_in_block','')); rep=scfg.get('repeat_header')
        header_rows=set()
        if rep:
            for r in range(1,ws.max_row+1):
                if isinstance(ws.cell(r,1).value,str) and re.match(rep,ws.cell(r,1).value.strip()): header_rows.add(r)
        for r in range(1,ws.max_row+1):
            for c in range(1,maxc+1):
                v=ws.cell(r,c).value
                if v is None: continue
                sv=str(v).strip(); L=GL(c)
                if mode=='keep':
                    if isinstance(v,str):
                        v2=sub_digits(EMAIL.sub(lambda m: token('EMAIL',m.group(0)),v))
                        if v2!=v: cnt['inline']+=1
                        v=v2
                    o.cell(r,c,v); continue
                in_block=bool(blk) and blk[0]<=r<=blk[1]
                if isinstance(v,bool) or sv=='' : pass
                elif isinstance(v,(int,float)):
                    if in_block and L in vcols and float(v).is_integer() and abs(v)>=10000: v=token('ID',str(int(v))); cnt['id-number']+=1
                elif isinstance(v,str):
                    if r in header_rows: v=sub_digits(v)                      # header labels stay
                    elif c in keep_cols and r not in header_rows: v=sub_digits(v); cnt['label-kept']+=1
                    elif re.fullmatch(r'\d{5,}',sv): v=token('ID',sv); cnt['id-digits']+=1
                    elif in_block and L in vcols: v=token('NAME',sv) if CAPWORDS.match(sv) else 'MASKED_TEXT'; cnt['block-value']+=1
                    elif c in cols and r not in header_rows and sv.lower() not in BOOL:
                        k=cols[c]; v=token(k,sv) if k!='TEXT' else 'MASKED_TEXT'; cnt['col-rule']+=1
                    elif c in keep_cols or WTPAT.match(sv): v=sub_digits(v); cnt['label-kept']+=1
                    elif safe(sv): v=sub_digits(v); cnt['label-kept']+=1
                    elif CAPWORDS.match(sv): v=token('NAME',sv); cnt['name']+=1
                    else: v='MASKED_TEXT'; cnt['masked-text']+=1
                o.cell(r,c,v)
        stats[(name,ws.title)]=(mode,None,dict(cnt))
    if '--dry' not in sys.argv: out.save(os.path.join(OUT,name)); print('masked',name)
for (fn,sh),(mode,hr,cnt) in stats.items(): lines.append(f'{fn} | {sh} | mode={mode} header_row={hr} | masked cells: {cnt}')
lines.append(f'\nColumns (table mode) with values that look like personal names (job titles, departments, EPS, banks, cities are excluded): {len(susp)}')
for (fn,sh,col,hd),n in sorted(susp.items()): lines.append(f'{fn} | {sh} | column {col} | header="{hd}" | {n} cells')
if '--dry' not in sys.argv:
    json.dump(key,open(KEY,'w'),ensure_ascii=False,indent=0)
    open(CHK,'w',encoding='utf-8').write('\n'.join(lines)+'\n')
print('\n'.join(lines)); print(f'Key entries: {n_key_before} -> {len(key)}')
