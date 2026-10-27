"""Statistics-only PII audit of masked workbooks in a folder: for every column whose header looks like an identity,
account, phone, address, e-mail, name or login column, prints the masking kind the rules assign and the category mix of
its values (token / digit-substituted / raw short digits / raw text), never a value. Usage: python3 scripts/pii_audit_masked.py <dir>"""
import os,re,sys,glob,collections,openpyxl
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src=open(os.path.join(ROOT,'scripts','mask_reports.py'),encoding='utf-8').read().splitlines()
ns={}; exec('import re\n'+'\n'.join(l for l in src if l.startswith(('RULES=','       (','EXCLUDE=','SAFE=','NAMEISH='))),ns)
RULES,EXCLUDE,NAMEISH=ns['RULES'],ns['EXCLUDE'],ns['NAMEISH']
TOK=re.compile(r'^(NAME|ID|EMAIL|ACCOUNT|PHONE|ADDRESS|ENTID|SHORTID|POSTAL)_\d{4,}$|^user\d{4}@masked\.example$|^1900-01-01$|^MASKED')
def header_row(ws,rows):
    best=None;bn=2
    for i,r in enumerate(rows[:25],1):
        n=sum(isinstance(v,str) and v.strip()!='' for v in r)
        if n>bn: best,bn=i,n
    return best
flag_total=0
for f in sorted(glob.glob(os.path.join(sys.argv[1],'*.xlsx'))):
    wb=openpyxl.load_workbook(f,read_only=True)
    for ws in wb:
        rows=list(ws.iter_rows(values_only=True)); hr=header_row(ws,rows)
        if not hr: continue
        for ci,h in enumerate(rows[hr-1],1):
            hl=str(h or '').strip().lower()
            share=None
            if not hl or not re.search(r'\bid\b|identif|c[eé]dula|cedula|documento|document|\bnit\b|account|cuenta|phone|tel[eé]fono|celular|address|direcc|email|correo|name|nombre|apellid|birth|nacimiento|login|user|enterprise|postal|empleado|employee|trabajador',hl): continue
            kind=None
            if not re.search(EXCLUDE,hl) and hl:
                for k,rx in RULES:
                    if re.search(rx,hl): kind=k;break
            vals=[r[ci-1] for r in rows[hr:] if len(r)>=ci and r[ci-1] is not None and str(r[ci-1]).strip()!='']
            cat=collections.Counter()
            for v in vals:
                sv=str(v).strip()
                if TOK.match(sv): cat['token']+=1
                elif isinstance(v,(int,float)) and kind in ('ID','ACCOUNT','PHONE'): cat['digit-substituted']+=1
                elif isinstance(v,(int,float)): cat['NUMERIC-raw']+=1
                elif re.fullmatch(r'\d{7,15}',sv): cat['digit-substituted' if kind in ('ID','ACCOUNT','PHONE') else 'digits7-15 (inline rule)']+=1
                elif re.fullmatch(r'\d{1,6}',sv): cat['digits<7 '+('substituted' if kind in ('ID','ACCOUNT','PHONE') else 'RAW')]+=1
                elif re.fullmatch(r'\d{12,15}',sv): cat['digits12-15 RAW']+=1
                elif NAMEISH.match(sv): cat['name-like RAW']+=1
                else: cat['other-text']+=1
            risky=[k for k in cat if 'RAW' in k]
            flag='  <== CHECK' if (risky and kind not in ('ID','ACCOUNT','PHONE')) or (kind in ('NAME','EMAIL','ADDRESS','DOB') and 'other-text' in cat) else ''
            if flag: flag_total+=1
            print(f"{os.path.basename(f)[:40]:40} | {ws.title[:22]:22} | {ws.cell(hr,ci).column_letter if hasattr(ws,'cell') else ci:>3} {str(h)[:38]!r:40} kind={kind!s:8} {dict(cat)}{flag}")
print('--- text cells with an embedded 7-11 digit run (possible glued employee number), per column, non-token cells only ---')
EMB=re.compile(r'(?<!\d)\d{7,11}(?!\d)')
for f in sorted(glob.glob(os.path.join(sys.argv[1],'*.xlsx'))):
    wb=openpyxl.load_workbook(f,read_only=True)
    for ws in wb:
        rows=list(ws.iter_rows(values_only=True)); hr=header_row(ws,rows) or 0; emb=collections.Counter()
        for r in rows[hr:]:
            for ci,v in enumerate(r):
                if isinstance(v,str) and not TOK.match(v.strip()) and not re.fullmatch(r'[\d.,\-\s]+',v.strip()) and EMB.search(v): emb[ci]+=1
        for ci,n in emb.items():
            h=str(rows[hr-1][ci] if hr and ci<len(rows[hr-1]) else '')
            print(f"{os.path.basename(f)[:40]:40} | {ws.title[:22]:22} | col {openpyxl.utils.get_column_letter(ci+1):>3} header={h[:30]!r:32} cells={n}  (substituted consistently if the column is in embedded_id_cols; otherwise REVIEW)")
print('--- name-like share >=10% in any column (header not SAFE) ---')
SAFE=ns['SAFE']
for f in sorted(glob.glob(os.path.join(sys.argv[1],'*.xlsx'))):
    wb=openpyxl.load_workbook(f,read_only=True)
    for ws in wb:
        rows=list(ws.iter_rows(values_only=True)); hr=header_row(ws,rows) or 0
        tot=collections.Counter(); nl=collections.Counter()
        for r in rows[hr:]:
            for ci,v in enumerate(r):
                if isinstance(v,str) and v.strip() and not TOK.match(v.strip()):
                    tot[ci]+=1
                    if NAMEISH.match(v.strip()): nl[ci]+=1
        for ci in nl:
            h=str(rows[hr-1][ci] if hr and ci<len(rows[hr-1]) else '') 
            if nl[ci]>=5 and nl[ci]/tot[ci]>=0.10 and not SAFE.search(h or ''):
                print(f"{os.path.basename(f)[:40]:40} | {ws.title[:22]:22} | col {openpyxl.utils.get_column_letter(ci+1):>3} header={h[:30]!r:32} name-like {nl[ci]}/{tot[ci]}  <== REVIEW (WT descriptions are false positives)"); flag_total+=1
print('columns flagged for a look:',flag_total)
