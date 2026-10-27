"""Counts, per spec, the field rows of the main spec sheet whose content differs between the original in 01-specs and the
final in 05-final. A field row = a row below the header whose column D (Field Position) or A is non-empty and is not a
section header (column A starting with '═══' or '='). Columns compared: A-S (T and U are reported separately since they are
emptied in the finals). Usage: python3 scripts/count_field_diffs.py"""
import os,glob,re,openpyxl
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAIRS={'CO-PILA-003':('CO-PILA-003-AportesSeguridadSocial-Spec-v1.1-DRAFT-2026-10-06.xlsx','CO-PILA-003-AportesSeguridadSocial-Spec.xlsx'),
 'CO-DIAN-001':('CO-DIAN-001-NominaElectronica-Spec-v1_1-DRAFT-2026-10-06.xlsx','CO-DIAN-001-NominaElectronica-Spec.xlsx'),
 'CO-DIAN-002':('CO-DIAN-002-Formulario350-Spec.xlsx','CO-DIAN-002-Formulario350-Spec.xlsx'),
 'CO-DIAN-004':('CO-DIAN-004-Formulario220-Spec.xlsx','CO-DIAN-004-Formulario220-Spec.xlsx'),
 'CO-DIAN-005':('CO-DIAN-005-Formato2276-Spec-v1_1-DRAFT-2026-10-06.xlsx','CO-DIAN-005-Formato2276-Spec.xlsx'),
 'CO-CESANTIAS-006':('CO-CESANTIAS-006-ConsignacionAnual-Spec.xlsx','CO-CESANTIAS-006-ConsignacionAnual-Spec.xlsx')}
norm=lambda v: None if v is None else re.sub(r'\s+',' ',str(v)).strip()
print(f"{'spec':18} {'fields':>6} {'differ A-S':>10} {'M only':>7} {'other cols':>10} {'T/U emptied':>11}  other sheets with differences")
for spec,(orig,final) in PAIRS.items():
    wo=openpyxl.load_workbook(os.path.join(ROOT,'01-specs',orig)); wf=openpyxl.load_workbook(os.path.join(ROOT,'05-final',final))
    so=[wo[s] for s in wo.sheetnames if s.endswith('Spec')][0]; sf=wf[so.title]
    fields=diff=monly=other=tu=0
    for r in range(3,so.max_row+1):
        a=norm(so.cell(r,1).value); d=norm(so.cell(r,4).value)
        if not (a or d) or (a and (a.startswith('═') or a.startswith('='))): continue
        fields+=1
        cols=[c for c in range(1,20) if norm(so.cell(r,c).value)!=norm(sf.cell(r,c).value)]
        if cols:
            diff+=1
            if cols==[13]: monly+=1
            else: other+=1
        if any(norm(so.cell(r,c).value) and not norm(sf.cell(r,c).value) for c in (20,21)): tu+=1
    others=[]
    for sn in wo.sheetnames:
        if sn==so.title or sn=='Version Control': continue
        a,b=wo[sn],wf[sn]; n=sum(1 for row in a.iter_rows() for c in row if norm(c.value)!=norm(b[c.coordinate].value))
        if n: others.append(f'{sn} {n}')
    print(f"{spec:18} {fields:>6} {diff:>10} {monly:>7} {other:>10} {tu:>11}  {', '.join(others)}")
