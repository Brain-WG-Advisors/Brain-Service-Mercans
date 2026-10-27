"""Round-3 structural probe of the '16oct' raw files. Runs LOCALLY, prints NO cell value except strings made only of
payroll vocabulary words (whitelist), so that Claude can configure the masking without seeing personal data.
Step 1: sha256 of every raw file -> which '16oct' files are identical to earlier files or to each other.
Step 2: for each distinct '16oct' workbook: sheets, dims, best header row, header texts ONLY if whitelist-safe
(headers are column labels; a header is printed only when every word is in VOCAB or it is short and has no name-like shape),
per-column type mix, digit-length histogram of integers, count of name-like strings, count of strings with embedded 7-11 digit runs.
Usage: python3 scripts/probe_round3.py"""
import os,re,sys,hashlib,unicodedata,collections
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter as GL
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW=os.path.join(ROOT,'02-client-reports-raw')
def strip(s): return ''.join(c for c in unicodedata.normalize('NFD',s) if unicodedata.category(c)!='Mn').lower()
VOCAB=set("""de del la el y o a en con sin no al los las por para un una e se su sus que
total totales valor valores dias dia days day base bases neto netos bruto brutos gross net
salario salarios sueldo sueldos basico basica ordinario integral variable fijo
cesantias cesantia intereses interes prima primas servicios servicio vacaciones vacacion compensadas disfrutadas pendientes
liquidacion liquidaciones final definitiva contrato contratos terminacion retiro fecha fechas ingreso egreso inicio fin
periodo periodos ano anos mes meses semana semanas quincena desde hasta
devengado devengados deduccion deducciones descuento descuentos retencion retenciones fuente aportes aporte
salud pension pensiones fondo fondos solidaridad subsistencia arl riesgos laborales caja compensacion familiar parafiscales
sena icbf eps afp ccf cotizacion cotizaciones ibc
auxilio auxilios transporte conectividad alimentacion bonificacion bonificaciones bono bonos comision comisiones
horas hora extra extras recargo recargos nocturno nocturnas dominical dominicales festivo festivos diurna diurnas
incapacidad incapacidades licencia licencias maternidad paternidad enfermedad general
indemnizacion indemnizaciones sancion sanciones moratoria mora
prestamo prestamos libranza embargo embargos cuota cuotas saldo saldos anticipo anticipos
concepto conceptos codigo codigos cantidad unidad porcentaje tarifa tasa factor formula
pagar pago pagos pagado abono abonos cuenta banco bancos transferencia cheque efectivo
empresa empleador compania sociedad nit razon social
empleado empleada trabajador trabajadora colaborador persona cargo centro costo costos area departamento division ubicacion
documento identificacion cedula tipo numero numeros apellido apellidos nombre nombres primer segundo otros
direccion ciudad municipio pais telefono correo email
observaciones observacion notas nota firma firmas elaborado revisado aprobado
amount amounts employee employees name names id number type date dates code codes description payroll run reference
withholding tax taxable exempt income deduction deductions contribution contributions pension health fund fund
severance interest premium bonus vacation vacations termination settlement hire start end status group subgroup
weekly monthly month year company legal entity cost center department position title currency cop
formato preliminar envio registro registros columna fila
pasa potro cuantia certificado certificados retenido retenida renta ano gravable
otro otra otros otras ninguno ninguna si subtotal subtotales
""".split())
NAMEISH=re.compile(r"^[A-ZÁÉÍÓÚÑ][A-Za-zÁÉÍÓÚÑáéíóúñ'\-]+(\s+[A-ZÁÉÍÓÚÑ][A-Za-zÁÉÍÓÚÑáéíóúñ'\-]+){1,4}$")
EMB=re.compile(r'(?<!\d)\d{7,11}(?!\d)'); HASDIGIT=re.compile(r'\d')
def safe(s):
    """True when every alphabetic word of s is in VOCAB (digits/punctuation ignored) -> printable."""
    words=re.findall(r'[A-Za-zÁÉÍÓÚÑáéíóúñÜü]+',s)
    if not words: return True
    return all(strip(w) in VOCAB for w in words)
def show(s,n=60):
    s=str(s).replace('\n',' ')
    if safe(s): return re.sub(r'\d{5,}', lambda m: '#'*len(m.group(0)), s[:n])   # never print a digit run of 5+ (employee numbers)
    nm=" nameish" if NAMEISH.match(s.strip()) else ""; dg=" digits" if HASDIGIT.search(s) else ""
    return "<unsafe text len=%d%s%s>"%(len(s),nm,dg)
# step 1: hashes
h={}
for n in sorted(os.listdir(RAW)):
    p=os.path.join(RAW,n)
    if os.path.isfile(p) and not n.startswith('.'): h[n]=hashlib.sha256(open(p,'rb').read()).hexdigest()[:16]
new=[n for n in h if '16oct' in n]; old=[n for n in h if '16oct' not in n]
distinct=[]
print('=== STEP 1: hashes of 16oct files')
for n in new:
    same_old=[o for o in old if h[o]==h[n]]; same_new=[o for o in distinct if h[o]==h[n]]
    tag='IDENTICAL to earlier file(s): '+', '.join(same_old) if same_old else ('IDENTICAL to new file: '+', '.join(same_new) if same_new else 'NEW')
    print(f'{h[n]} {os.path.getsize(os.path.join(RAW,n)):>8} {n} -> {tag}')
    if not same_old and not same_new: distinct.append(n)
print('\nDISTINCT new files:',len(distinct))
if '--hash-only' in sys.argv: sys.exit()
def best_header_row(ws):
    best=None;bn=2
    for r in range(1,min(ws.max_row,25)+1):
        n=sum(1 for c in range(1,ws.max_column+1) if isinstance(ws.cell(r,c).value,str) and ws.cell(r,c).value.strip()!='')
        if n>bn: best,bn=r,n
    return best
FORM=[a for a in sys.argv[1:] if not a.startswith('--')]
for n in (FORM or distinct):
    print(f'\n===== {n}')
    wb=load_workbook(os.path.join(RAW,n),data_only=True,read_only=False)
    for ws in wb:
        hr=best_header_row(ws)
        print(f"--- sheet {ws.title!r}: rows={ws.max_row} cols={ws.max_column} best_header_row={hr}")
        # row profile for the first 25 rows (counts only) when the sheet looks like a form (few columns or hr late)
        MAXR=ws.max_row if FORM else min(ws.max_row,30)
        for r in range(1,MAXR+1):
            cells=[(c,ws.cell(r,c).value) for c in range(1,ws.max_column+1) if ws.cell(r,c).value not in (None,'')]
            if not cells: continue
            desc=[]
            for c,v in cells[:14]:
                L=GL(c)
                if isinstance(v,str): desc.append(f'{L}:"{show(v,28)}"')
                elif isinstance(v,bool): desc.append(f'{L}:bool')
                elif isinstance(v,(int,float)): desc.append(f'{L}:num{len(str(abs(int(v)))) if float(v).is_integer() else "dec"}')
                else: desc.append(f'{L}:{type(v).__name__}')
            print(f'  r{r:<3} n={len(cells):<3} '+' '.join(desc)+(' ...' if len(cells)>14 else ''))
        if hr and ws.max_row>hr+1 and not FORM:
            print('  columns (header | types | int-digit-length histogram | nameish | embedded-digit-run strings | distinct):')
            for c in range(1,ws.max_column+1):
                hv=ws.cell(hr,c).value
                vals=[ws.cell(r,c).value for r in range(hr+1,ws.max_row+1)]
                nn=[v for v in vals if v not in (None,'')]
                if hv is None and not nn: continue
                types=collections.Counter(type(v).__name__ for v in nn)
                dl=collections.Counter(len(str(abs(int(v)))) for v in nn if isinstance(v,(int,float)) and not isinstance(v,bool) and float(v).is_integer())
                dl2=collections.Counter(len(v.strip()) for v in nn if isinstance(v,str) and re.fullmatch(r'\d+',v.strip()))
                nameish=sum(1 for v in nn if isinstance(v,str) and NAMEISH.match(v.strip()))
                emb=sum(1 for v in nn if isinstance(v,str) and not re.fullmatch(r'\d+',v.strip()) and EMB.search(v))
                safe_strings=sum(1 for v in nn if isinstance(v,str) and safe(v))
                print(f'   {GL(c):>3} "{show(hv,45)}" | {dict(types)} | int-len {dict(sorted(dl.items()))} digit-str-len {dict(sorted(dl2.items()))} | nameish={nameish} emb={emb} safe_str={safe_strings} | distinct={len(set(map(str,nn)))} n={len(nn)}')
        elif not FORM:
            # form-like sheet: summarise ALL string cells beyond row 30 by safety
            cnt=collections.Counter()
            for row in ws.iter_rows(min_row=31):
                for cell in row:
                    v=cell.value
                    if isinstance(v,str) and v.strip(): cnt['safe' if safe(v) else ('nameish' if NAMEISH.match(v.strip()) else 'unsafe')]+=1
                    elif isinstance(v,(int,float)) and not isinstance(v,bool): cnt['num']+=1
                    elif v not in (None,''): cnt[type(v).__name__]+=1
            print('  cells from row 31:',dict(cnt))

# --headers mode: print header-row labels of the tabular sheets of the files given, only when every word is header vocabulary
if '--headers' in sys.argv:
    HV=VOCAB|set("""cod national bank account hire leaving effective days worked on leave group pay wt wage concept description
    nature code amount jan feb mar apr may jun jul aug sep oct nov dec january february march april june july august september october november december
    month year ytd acumulado acumulados prestaciones accrual accruals provision cost center centre entity legal company payroll id number
    status active inactive retiro ingreso basic variable average promedio base bases premium severance interest vacation vacations sueldo
    cesantias intereses prima vacaciones indemnizacion dias valor total subtotal percentage pct renta gravable exenta exempt taxable withholding
    retencion ibc salud pension arl ccf sena icbf parafiscales fondo solidaridad subsistencia employee name full first last surname given
    nombre nombres apellido apellidos identificacion documento cedula tipo type class clase risk riesgo contract contrato term termino start end
    fecha inicio fin desde hasta periodo period reference ref run corrida nomina net neto gross bruto deduction deductions earning earnings
    entitlement entitlements employer contribution contributions social security seguridad quantity cantidad unit unidad rate tarifa factor
    reason motivo causa city ciudad department departamento division area position cargo job title pay group paygroup subgroup level grade
    observation observations observaciones note notes comment comments check validation validacion diff difference diferencia ok""".split())
    def hsafe(s):
        words=re.findall(r'[A-Za-zÁÉÍÓÚÑáéíóúñÜü]+',str(s)); return bool(words) and all(strip(w) in HV for w in words)
    for n in FORM:
        wb=load_workbook(os.path.join(RAW,n),data_only=True)
        print('=====',n)
        for ws in wb:
            if ws.title in ('Liquidacion',): continue
            for hr in ([1,3,6] if ws.max_column<40 else [1]):
                vals=[(GL(c),ws.cell(hr,c).value) for c in range(1,min(ws.max_column,40)+1) if isinstance(ws.cell(hr,c).value,str) and ws.cell(hr,c).value.strip()]
                if len(vals)>=5:
                    print(f'--- {ws.title!r} row {hr}: '+' | '.join(f'{L}:{re.sub(r"[0-9]{3,}","#",v)[:30]}' if hsafe(v) else f'{L}:<unsafe {len(v)}>' for L,v in vals))
    sys.exit()
