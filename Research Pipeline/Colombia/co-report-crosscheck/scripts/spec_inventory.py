"""Dumps every field of every spec in 01-specs/ to 04-output/specs/<CODE>.json. Usage: python3 scripts/spec_inventory.py"""
import os,glob,json,re
from openpyxl import load_workbook
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import sys
IN=sys.argv[1] if len(sys.argv)>1 else os.path.join(ROOT,'01-specs'); OUT=sys.argv[2] if len(sys.argv)>2 else os.path.join(ROOT,'04-output','specs'); os.makedirs(OUT,exist_ok=True)
for f in sorted(glob.glob(os.path.join(IN,'*.xlsx'))):
    wb=load_workbook(f); found=False
    for ws in wb:
        for hr in (1,2,3):
            H=[ws.cell(hr,c).value for c in range(1,30)]
            if 'Field Explanation' in H or 'Field Position' in H:
                found=True; fields=[]
                for r in range(hr+1,ws.max_row+1):
                    v={str(h):ws.cell(r,i+1).value for i,h in enumerate(H) if h}
                    if any(x not in (None,'') for x in v.values()): v['_row']=r; fields.append(v)
                code=re.match(r'(CO-[A-Z]+-\d{3})',os.path.basename(f)).group(1)
                json.dump({'file':os.path.basename(f),'sheet':ws.title,'header_row':hr,'fields':fields},open(os.path.join(OUT,code+'.json'),'w'),ensure_ascii=False,indent=1,default=str)
                print(code,ws.title,len(fields),'rows'); break
        if found: break
    if not found: print('NO SPEC SHEET FOUND in',os.path.basename(f))
