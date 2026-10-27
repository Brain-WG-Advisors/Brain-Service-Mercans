"""Targeted fix for residual PII found on 15 Oct 2026 in the MASKED copies only.
Does NOT touch 02-client-reports-raw/, 99-local-only/ or the masking key, and does not re-run mask_reports.py.
Never prints a cell value.

1. Master Data col M "Enterprise ID"  -> consistent tokens ENTID_0001.. (same handle -> same token).
1c. Master Data col AO "Indentity Card for Foreigners" -> values under 7 digits -> SHORTDOC_0001.. (added 16 Oct 2026).
1b. Master Data col AU "Postal Code"  -> consistent tokens POSTAL_0001.. (added 15 Oct 2026, second pass). Idempotent: already-tokenised cells are skipped.
2. Accumulated Report col C "EE Citizenship Card ID" and Bank Payments col B "Citizenship Card ID":
   values with fewer than 7 digits (missed by the 7-15 digit rule) -> consistent tokens SHORTID_0001..
   (same number -> same token across both files, so joins on this column still work).
Then regenerates the profiles with scripts/profile_reports.py.
"""
import os,re,sys,subprocess,openpyxl
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
M=os.path.join(ROOT,'03-client-reports-masked')
ent={}; short={}
def tok(d,prefix,v):
    k=str(v).strip()
    if k not in d: d[k]=f'{prefix}_{len(d)+1:04d}'
    return d[k]
postal={}; shortdoc={}
jobs=[("1764_Master_Data_Report_202609.xlsx","Master Data Report","AO",12,lambda v: tok(shortdoc,'SHORTDOC',v), lambda v: re.fullmatch(r'\d{1,6}',str(v).strip()) is not None),("1764_Master_Data_Report_202609.xlsx","Master Data Report","M",12,lambda v: tok(ent,'ENTID',v), lambda v: isinstance(v,str) and v.strip()!='' and not re.fullmatch(r'ENTID_\d{4}',v.strip())),
      ("1764_Master_Data_Report_202609.xlsx","Master Data Report","AU",12,lambda v: tok(postal,'POSTAL',v), lambda v: str(v).strip()!='' and not re.fullmatch(r'POSTAL_\d{4}',str(v).strip())),
      ("Accumulated Report.xlsx","Accumulated Report","C",None,lambda v: tok(short,'SHORTID',v), lambda v: re.fullmatch(r'\d{1,6}',str(v).strip()) is not None),
      ("1764_PMI_Bank_Payments_Report_202609.xlsx","Bank Payments Report","B",None,lambda v: tok(short,'SHORTID',v), lambda v: re.fullmatch(r'\d{1,6}',str(v).strip()) is not None)]
for f,s,col,hr,fn,cond in jobs:
    p=os.path.join(M,f); wb=openpyxl.load_workbook(p); ws=wb[s]; ci=openpyxl.utils.column_index_from_string(col)
    if hr is None:  # find header row: first row with >=3 strings
        for r in range(1,26):
            if sum(isinstance(ws.cell(r,c).value,str) for c in range(1,ws.max_column+1))>=3: hr=r;break
    n=0
    for r in range(hr+1,ws.max_row+1):
        v=ws.cell(r,ci).value
        if v is not None and cond(v): ws.cell(r,ci).value=fn(v); n+=1
    wb.save(p); print(f'{f} col {col}: {n} cells replaced')
print('distinct Enterprise IDs tokenised:',len(ent),'| distinct short document numbers tokenised:',len(short),'| distinct postal codes tokenised:',len(postal),'| short foreigner-card numbers tokenised:',len(shortdoc))
if '--no-profile' not in sys.argv: subprocess.run(['python3',os.path.join(ROOT,'scripts','profile_reports.py')],check=True)
