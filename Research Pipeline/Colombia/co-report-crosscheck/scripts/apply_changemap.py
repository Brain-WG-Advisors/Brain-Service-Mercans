"""Apply an APPROVED change map to a spec, cell by cell, by XML surgery (no openpyxl save).

usage: python3 scripts/apply_changemap.py 04-output/<SPEC>-changemap-APPROVED.json [--date 2026-10-15] [--dry-run]

- Source spec is read from 01-specs/ and NEVER modified. Output goes to 02-specs-out/ as a DRAFT.
- Every edit is checked against the cell's current text before anything is written; any mismatch aborts.
- Edited cells are rewritten as inline strings, keeping the cell's style id. Rows/merges/drawings untouched.
- Column U of every row in mark_corrected_rows is set to "Corrected".
- Section-header / separator cells stored as formulas are converted to plain text (PILA v1.1 precedent) and logged.
- Version Control: one row per sentence, written into the already-styled empty rows below the last entry.
- Repack: unmodified zip entries are copied byte for byte.
"""
import sys,os,re,json,zipfile,html,shutil,argparse,datetime
from xml.sax.saxutils import escape

ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ap=argparse.ArgumentParser(); ap.add_argument('changemap'); ap.add_argument('--date',default=datetime.date.today().isoformat()); ap.add_argument('--dry-run',action='store_true'); ap.add_argument('--updated-by',default='Wallisson Gomes')
ap.add_argument('--on-draft',action='store_true',help='apply onto the existing DRAFT named in spec_file (02-specs-out): the previous draft is moved to 02-specs-out/_previous/<name>.<timestamp>.xlsx and the new file keeps the same name')
ap.add_argument('--log-suffix',default='',help='suffix for the apply-log file name, e.g. -r2')
A=ap.parse_args()
cm=json.load(open(A.changemap,encoding='utf-8'))
src=os.path.join(ROOT,cm['spec_file']) if not os.path.isabs(cm['spec_file']) else cm['spec_file']
if not os.path.exists(src): src=os.path.join(ROOT,'01-specs',os.path.basename(cm['spec_file']))
assert os.path.exists(src), src
OUTDIR=os.path.join(ROOT,'02-specs-out'); os.makedirs(OUTDIR,exist_ok=True)
base=os.path.basename(src)
if A.on_draft:
    assert os.path.sep+'02-specs-out'+os.path.sep in src and '-DRAFT-' in base, 'with --on-draft the source must be a DRAFT in 02-specs-out'
    prev_dir=os.path.join(OUTDIR,'_previous'); os.makedirs(prev_dir,exist_ok=True)
    prev_copy=os.path.join(prev_dir,base.replace('.xlsx','.'+datetime.datetime.now().strftime('%Y%m%d-%H%M%S')+'.xlsx'))
    if not A.dry_run: shutil.copy2(src,prev_copy)
    out=src.replace('.xlsx','.new.xlsx'); final_out=src
else:
    assert os.path.sep+'01-specs'+os.path.sep in src, 'source must come from 01-specs (or use --on-draft)'
    if '-DRAFT-' in base: out_name=re.sub(r'-DRAFT-\d{4}-\d{2}-\d{2}\.xlsx$',f'-DRAFT-{A.date}.xlsx',base)
    else: out_name=base.replace('.xlsx',f'-v1_1-DRAFT-{A.date}.xlsx')
    out=os.path.join(OUTDIR,out_name); final_out=out; prev_copy=None
NEW_VERSION='v1.1'

z=zipfile.ZipFile(src); parts={n:z.read(n) for n in z.namelist()}; infos={i.filename:i for i in z.infolist()}
wbx=parts['xl/workbook.xml'].decode('utf-8'); rels=parts['xl/_rels/workbook.xml.rels'].decode('utf-8')
rid2t={}
for m in re.finditer(r'<Relationship\b[^>]*/>',rels):
    s=m.group(0); rid2t[re.search(r'Id="([^"]+)"',s).group(1)]=re.search(r'Target="([^"]+)"',s).group(1)
sheet_part={}
for name,rid in re.findall(r'<sheet\b[^>]*name="([^"]+)"[^>]*r:id="([^"]+)"',wbx):
    t=rid2t[rid]; t=t.lstrip('/'); t=t if t.startswith('xl/') else 'xl/'+t; sheet_part[html.unescape(name)]=t
# shared strings
sst=[]
if 'xl/sharedStrings.xml' in parts:
    for si in re.findall(r'<si>(.*?)</si>',parts['xl/sharedStrings.xml'].decode('utf-8'),re.S):
        sst.append(html.unescape(''.join(re.findall(r'<t[^>]*>(.*?)</t>',si,re.S))))
modified={}  # part -> new text
def get_xml(part):
    return modified.get(part) or parts[part].decode('utf-8')
def col_num(col):
    n=0
    for ch in col: n=n*26+ord(ch)-64
    return n
CELL_SELF=lambda ref: re.compile(r'<c r="%s"(?: [^>]*)?/>'%ref)
CELL_FULL=lambda ref: re.compile(r'<c r="%s"(?: [^>]*)?(?<!/)>.*?</c>'%ref,re.S)
def find_cell(xml,ref):
    m=CELL_SELF(ref).search(xml)
    if m: return m,'self'
    m=CELL_FULL(ref).search(xml)
    return (m,'full') if m else (None,None)
def cell_text(xml,ref):
    m,kind=find_cell(xml,ref)
    if not m: return None,None
    c=m.group(0); s=re.search(r' s="(\d+)"',c); style=s.group(1) if s else None
    if kind=='self': return None,style
    f=re.search(r'<f\b[^>]*>(.*?)</f>|<f\b[^>]*/>',c,re.S)
    if f: return '='+html.unescape(f.group(1) or ''),style
    t=re.search(r' t="([^"]+)"',c); t=t.group(1) if t else 'n'
    if t=='s':
        v=re.search(r'<v>(.*?)</v>',c,re.S); return (sst[int(v.group(1))] if v else None),style
    if t=='inlineStr':
        return html.unescape(''.join(re.findall(r'<t[^>]*>(.*?)</t>',c,re.S))),style
    v=re.search(r'<v>(.*?)</v>',c,re.S); return (html.unescape(v.group(1)) if v else None),style
def set_cell(xml,ref,text,style=None):
    m,kind=find_cell(xml,ref)
    if m and style is None:
        s=re.search(r' s="(\d+)"',m.group(0)); style=s.group(1) if s else None
    new='<c r="%s"%s t="inlineStr"><is><t xml:space="preserve">%s</t></is></c>'%(ref,(' s="%s"'%style if style else ''),escape(text))
    if m: return xml[:m.start()]+new+xml[m.end():]
    # cell absent: insert into the row in column order
    row=int(re.search(r'\d+',ref).group(0)); col=col_num(re.match(r'[A-Z]+',ref).group(0))
    rm=re.search(r'<row r="%d"[^>]*>(.*?)</row>'%row,xml,re.S)
    if not rm: raise SystemExit(f'row {row} not found for {ref}')
    body=rm.group(1); pos=len(body)
    for cm_ in re.finditer(r'<c r="([A-Z]+)%d"'%row,body):
        if col_num(cm_.group(1))>col: pos=cm_.start(); break
    nb=body[:pos]+new+body[pos:]
    return xml[:rm.start(1)]+nb+xml[rm.end(1):]
def norm(s):
    if s is None: return None
    return re.sub(r'\s+',' ',str(s).replace('\r\n','\n')).strip()

# ---- 1. verify every edit against the current text
problems=[]; plan=[]
for e in cm['edits']:
    sheet=e['sheet']; part=sheet_part.get(sheet)
    if not part: problems.append(f'sheet not found: {sheet}'); continue
    ref=e.get('cell') or f"{e['column_letter']}{e['row']}"
    cur,style=cell_text(get_xml(part),ref)
    if norm(cur)!=norm(e.get('current')):
        problems.append(f"{sheet}!{ref}: current text mismatch\n   file: {str(cur)[:160]!r}\n   map : {str(e.get('current'))[:160]!r}")
    if not isinstance(e.get('proposed'),str) or not e['proposed'].strip(): problems.append(f'{sheet}!{ref}: empty proposed text')
    plan.append((part,ref,e['proposed'],style))
if problems:
    print('ABORT: %d problem(s), nothing written'%len(problems)); print('\n'.join(problems)); sys.exit(2)

# ---- 2. apply edits
for part,ref,text,style in plan: modified[part]=set_cell(get_xml(part),ref,text,style)
# ---- 3. column U = Corrected on changed field rows
spec_part=sheet_part[cm['spec_sheet']]
for row in sorted(set(cm.get('mark_corrected_rows',[]))):
    xml=get_xml(spec_part); cur,style=cell_text(xml,f'U{row}')
    if style is None: _,style=cell_text(xml,f'T{row}')
    if style is None: _,style=cell_text(xml,f'M{row}')
    modified[spec_part]=set_cell(xml,f'U{row}','Corrected',style)
# ---- 4. formulas -> text
conv=[]
for sheet,part in sheet_part.items():
    xml=get_xml(part)
    for m in list(re.finditer(r'<c r="([A-Z]+\d+)"(?: [^>]*)?(?<!/)>(?:(?!</c>).)*?<f\b[^>]*>(.*?)</f>.*?</c>',xml,re.S)):
        pass
    refs=re.findall(r'<c r="([A-Z]+\d+)"(?: [^>]*)?(?<!/)>(?:(?!</c>).)*?<f\b',xml,re.S)
    for ref in refs:
        cur,style=cell_text(xml,ref)
        ftxt=cur[1:] if cur and cur.startswith('=') else (cur or '')
        if re.fullmatch(r'=*',ftxt): text='═'*max(len(ftxt),3)
        else: text='═══ '+ftxt.rstrip('=').strip()+' ═══'
        xml=set_cell(xml,ref,text,style); conv.append((sheet,ref))
    if refs: modified[part]=xml
# ---- 5. Version Control rows
vc_part=sheet_part['Version Control']; vx=get_xml(vc_part)
rows=list(re.finditer(r'<row r="(\d+)"[^>]*>(.*?)</row>',vx,re.S))
hdr=next(r for r in rows if norm(cell_text(vx,'B'+r.group(1))[0])=='Version')
hdr_row=int(hdr.group(1)); last=None
for r in rows:
    rn=int(r.group(1))
    if rn>hdr_row and cell_text(vx,'B%d'%rn)[0]: last=r
assert last, 'no Version Control entry row found'
last_row=int(last.group(1)); prev_status=cell_text(vx,'E%d'%last_row)[0] or ''
if not prev_status.lower().startswith('draft'): prev_status='Draft - RA review in progress'
tmpl_open=re.match(r'<row r="\d+"([^>]*)>',last.group(0)).group(1)
styles={c:cell_text(vx,f'{c}{last_row}')[1] for c in 'ABCDEFG'}
sentences=cm.get('version_control') or []
if conv: sentences=sentences+[f'{len(conv)} section-header and separator cells stored as formulas (rendered as #NAME? in Excel) converted to plain text in: '+', '.join(sorted(set(s for s,_ in conv)))+'. No content change.']
def build_row(rn,vals):
    cells=[]
    for c in 'ABCDEFG':
        st=styles.get(c); v=vals.get(c)
        if v is None: cells.append('<c r="%s%d"%s/>'%(c,rn,(' s="%s"'%st if st else '')))
        else: cells.append('<c r="%s%d"%s t="inlineStr"><is><t xml:space="preserve">%s</t></is></c>'%(c,rn,(' s="%s"'%st if st else ''),escape(v)))
    return '<row r="%d"%s>%s</row>'%(rn,tmpl_open,''.join(cells))
for i,sent in enumerate(sentences,1):
    rn=last_row+i
    rm=re.search(r'<row r="%d"[^>]*>.*?</row>'%rn,vx,re.S)
    if not rm: raise SystemExit(f'Version Control: no spare styled row {rn}')
    if cell_text(vx,'B%d'%rn)[0]: raise SystemExit(f'Version Control row {rn} is not empty')
    vx=vx[:rm.start()]+build_row(rn,{'B':NEW_VERSION,'C':A.date,'D':sent,'E':prev_status,'F':A.updated_by})+vx[rm.end():]
modified[vc_part]=vx

print(f'{cm["spec"]}: {len(plan)} cell edits, {len(cm.get("mark_corrected_rows",[]))} rows marked Corrected, {len(conv)} formula cells converted, {len(sentences)} Version Control rows')
if A.dry_run: print('dry run: nothing written'); sys.exit(0)
# ---- 6. repack byte for byte
with zipfile.ZipFile(out,'w') as zo:
    for n in z.namelist():
        info=infos[n]
        if n in modified:
            zi=zipfile.ZipInfo(n,date_time=info.date_time); zi.compress_type=zipfile.ZIP_DEFLATED; zi.external_attr=info.external_attr
            zo.writestr(zi,modified[n].encode('utf-8'))
        else:
            zi=zipfile.ZipInfo(n,date_time=info.date_time); zi.compress_type=info.compress_type; zi.external_attr=info.external_attr
            zo.writestr(zi,parts[n])
# ---- 7. validation
import openpyxl
zc=zipfile.ZipFile(out); assert zc.testzip() is None
assert set(zc.namelist())==set(z.namelist()), 'zip entry set changed'
for n in z.namelist():
    if n not in modified: assert zc.read(n)==parts[n], f'unmodified entry changed: {n}'
wb=openpyxl.load_workbook(out); wo=openpyxl.load_workbook(src)
assert wb.sheetnames==wo.sheetnames
for sn in wo.sheetnames: assert len(wb[sn]._images)==len(wo[sn]._images), f'images changed in {sn}'
if A.on_draft:
    os.replace(out,final_out); out=final_out; src=prev_copy
print('written',out); json.dump({'spec':cm['spec'],'source':src,'draft':out,'edits':[(p,r) for p,r,_,_ in plan],'corrected_rows':sorted(set(cm.get('mark_corrected_rows',[]))),'formula_cells_converted':conv,'vc_rows':list(range(last_row+1,last_row+1+len(sentences))),'vc_sentences':sentences},open(os.path.join(OUTDIR,cm['spec']+'-apply-log'+A.log_suffix+'.json'),'w',encoding='utf-8'),ensure_ascii=False,indent=1)
