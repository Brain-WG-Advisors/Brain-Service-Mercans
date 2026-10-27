"""Profiles every masked report: sheets, title lines, header row, columns, type, max length, blanks, distinct count, 3 masked examples.
Writes 04-output/profiles/<file>.json. Usage: python3 scripts/profile_reports.py [masked_dir] [profiles_out_dir]"""
import os,glob,json,datetime
from openpyxl import load_workbook
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import sys
IN=sys.argv[1] if len(sys.argv)>1 else os.path.join(ROOT,'03-client-reports-masked'); OUT=sys.argv[2] if len(sys.argv)>2 else os.path.join(ROOT,'04-output','profiles'); os.makedirs(OUT,exist_ok=True)
def header_row(ws):
    best=None;bn=2
    for r in range(1,min(ws.max_row,25)+1):
        n=sum(isinstance(ws.cell(r,c).value,str) and ws.cell(r,c).value.strip()!='' for c in range(1,ws.max_column+1))
        if n>bn: best,bn=r,n
    return best
def kind(v):
    if isinstance(v,bool): return 'bool'
    if isinstance(v,(int,float)): return 'number'
    if isinstance(v,(datetime.date,datetime.datetime)): return 'date'
    return 'text'
for f in sorted(glob.glob(os.path.join(IN,'*.xlsx'))):
    wb=load_workbook(f); prof={'file':os.path.basename(f),'sheets':[]}
    for ws in wb:
        hr=header_row(ws); s={'sheet':ws.title,'rows':ws.max_row,'cols':ws.max_column,'header_row':hr,
           'title_lines':[str(ws.cell(r,1).value) for r in range(1,(hr or 1)) if ws.cell(r,1).value][:6],'columns':[]}
        if hr:
            for c in range(1,ws.max_column+1):
                h=ws.cell(hr,c).value
                vals=[ws.cell(r,c).value for r in range(hr+1,ws.max_row+1)]
                nn=[v for v in vals if v not in (None,'')]
                if h is None and not nn: continue
                kinds={}
                for v in nn: kinds[kind(v)]=kinds.get(kind(v),0)+1
                ex=[]; 
                for v in nn:
                    sv=str(v)
                    if sv not in ex: ex.append(sv)
                    if len(ex)==3: break
                s['columns'].append({'col':ws.cell(hr,c).column_letter,'header':h,'types':kinds,'max_len':max((len(str(v)) for v in nn),default=0),
                    'blank_ratio':round(1-len(nn)/max(len(vals),1),2),'distinct':len(set(map(str,nn))),'examples_masked':ex})
        prof['sheets'].append(s)
    json.dump(prof,open(os.path.join(OUT,os.path.basename(f).replace('.xlsx','.json')),'w'),ensure_ascii=False,indent=1,default=str)
    print('profiled',os.path.basename(f))
