"""Build the FINAL (initial-version) spec from a v1.1 DRAFT by XML surgery, then run the checks.

usage: python3 scripts/make_final.py <SPEC> [--dry-run]
Reads 04-output/final-prep/<SPEC>-cleanup-map.json: {"spec","draft","final_name","edits":[{"sheet","cell","current","proposed"}],"unrewritable":[...]}
 - proposed = "" or null clears the cell (keeps its style).
Steps: (1) spec sheet columns T and U: every field row cleared (header kept); (2) Version Control: a single entry
"1.0 | 2026-10-16 | Initial version. | Approved | Wallisson Gomes", every other entry row blanked; (3) cleanup edits applied
with a current-text check; (4) every cell containing "PLACEHOLDER" rewritten with "illustrative value"; (5) byte-for-byte
repack of every untouched zip part to 05-final/<final_name>.
Checks: diff against the DRAFT (only T/U field cells, Version Control rows, cleanup cells and PLACEHOLDER cells may differ),
zero formula cells, zero masked tokens, zero hits of the review/process word list in every sheet (counts printed per word).
"""
import sys,os,re,json,zipfile,html,argparse,collections
from xml.sax.saxutils import escape
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ap=argparse.ArgumentParser(); ap.add_argument('spec'); ap.add_argument('--dry-run',action='store_true'); ap.add_argument('--on-final',action='store_true',help='apply a map onto the existing final in 05-final (previous copy kept in 05-final/_previous)'); ap.add_argument('--map',default='rules-map',help='map file suffix for --on-final: <SPEC>-<map>.json'); A=ap.parse_args()
import shutil,datetime
OUTDIR=os.path.join(ROOT,'05-final'); os.makedirs(OUTDIR,exist_ok=True)
if A.on_final:
    cm=json.load(open(os.path.join(ROOT,'04-output','final-prep',A.spec+'-'+A.map+'.json'),encoding='utf-8'))
    src=os.path.normpath(os.path.join(ROOT,cm['final'])); assert os.path.exists(src) and os.sep+'05-final'+os.sep in src, src
    cm['final_name']=os.path.basename(src); final_out=src; out=src.replace('.xlsx','.new.xlsx')
    prev_dir=os.path.join(OUTDIR,'_previous'); os.makedirs(prev_dir,exist_ok=True)
    prev_copy=os.path.join(prev_dir,os.path.basename(src).replace('.xlsx','.'+datetime.datetime.now().strftime('%Y%m%d-%H%M%S')+'.xlsx'))
else:
    cm=json.load(open(os.path.join(ROOT,'04-output','final-prep',A.spec+'-cleanup-map.json'),encoding='utf-8'))
    src=os.path.normpath(os.path.join(ROOT,cm['draft'])); assert os.path.exists(src) and os.sep+'02-specs-out'+os.sep in src, src
    out=os.path.join(OUTDIR,cm['final_name']); final_out=out; prev_copy=None
VC_ROW=['1.0','2026-10-16','Initial version.','Approved','Wallisson Gomes']

z=zipfile.ZipFile(src); parts={n:z.read(n) for n in z.namelist()}; infos={i.filename:i for i in z.infolist()}
wbx=parts['xl/workbook.xml'].decode('utf-8'); rels=parts['xl/_rels/workbook.xml.rels'].decode('utf-8')
rid2t={re.search(r'Id="([^"]+)"',m).group(1):re.search(r'Target="([^"]+)"',m).group(1) for m in re.findall(r'<Relationship\b[^>]*/>',rels)}
sheet_part={}
for name,rid in re.findall(r'<sheet\b[^>]*name="([^"]+)"[^>]*r:id="([^"]+)"',wbx):
    t=rid2t[rid].lstrip('/'); t=t if t.startswith('xl/') else 'xl/'+t; sheet_part[html.unescape(name)]=t
sst=[]
if 'xl/sharedStrings.xml' in parts:
    for si in re.findall(r'<si>(.*?)</si>',parts['xl/sharedStrings.xml'].decode('utf-8'),re.S): sst.append(html.unescape(''.join(re.findall(r'<t[^>]*>(.*?)</t>',si,re.S))))
modified={}
get_xml=lambda p: modified.get(p) or parts[p].decode('utf-8')
def col_num(col):
    n=0
    for ch in col: n=n*26+ord(ch)-64
    return n
def find_cell(xml,ref):
    m=re.compile(r'<c r="%s"(?: [^>]*)?/>'%ref).search(xml)
    if m: return m,'self'
    m=re.compile(r'<c r="%s"(?: [^>]*)?(?<!/)>.*?</c>'%ref,re.S).search(xml)
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
    if t=='inlineStr': return html.unescape(''.join(re.findall(r'<t[^>]*>(.*?)</t>',c,re.S))),style
    v=re.search(r'<v>(.*?)</v>',c,re.S); return (html.unescape(v.group(1)) if v else None),style
def set_cell(xml,ref,text,style=None):
    m,kind=find_cell(xml,ref)
    if m and style is None:
        s=re.search(r' s="(\d+)"',m.group(0)); style=s.group(1) if s else None
    sattr=(' s="%s"'%style if style else '')
    new=('<c r="%s"%s/>'%(ref,sattr)) if text is None or text=='' else '<c r="%s"%s t="inlineStr"><is><t xml:space="preserve">%s</t></is></c>'%(ref,sattr,escape(text))
    if m: return xml[:m.start()]+new+xml[m.end():]
    if text is None or text=='': return xml
    row=int(re.search(r'\d+',ref).group(0)); col=col_num(re.match(r'[A-Z]+',ref).group(0))
    rm=re.search(r'<row r="%d"[^>]*>(.*?)</row>'%row,xml,re.S); body=rm.group(1); pos=len(body)
    for cm_ in re.finditer(r'<c r="([A-Z]+)%d"'%row,body):
        if col_num(cm_.group(1))>col: pos=cm_.start(); break
    return xml[:rm.start(1)]+body[:pos]+new+body[pos:]+xml[rm.end(1):]
norm=lambda s: None if s is None else re.sub(r'\s+',' ',str(s).replace('\r\n','\n')).strip()
touched=set()  # (sheet, ref)

spec_sheet=[n for n in sheet_part if n.endswith('Spec')][0]; sp=sheet_part[spec_sheet]; xml=get_xml(sp)
hdr_row=2
vp=sheet_part['Version Control']; vx=get_xml(vp)
rows=list(re.finditer(r'<row r="(\d+)"[^>]*>(.*?)</row>',vx,re.S))
hdr=next(int(r.group(1)) for r in rows if norm(cell_text(vx,'B'+r.group(1))[0])=='Version')
entries=[int(r.group(1)) for r in rows if int(r.group(1))>hdr and cell_text(vx,'B%d'%int(r.group(1)))[0]]
if A.on_final:
    # state check: T/U empty, single initial-version line
    tu=[ref for ref in re.findall(r'<c r="([TU]\d+)"',xml) if int(ref[1:])>hdr_row and cell_text(xml,ref)[0] not in (None,'')]
    assert not tu, 'T/U field cells are not empty: '+str(tu[:5])
    # the effective date is the spec's own (new specs, e.g. CO-PILA-007, were born after 2026-10-16); the other columns must match
    vc=[cell_text(vx,f'{c}{entries[0]}')[0] for c in 'BCDEF'] if len(entries)==1 else None
    assert vc and vc[:1]+vc[2:]==VC_ROW[:1]+VC_ROW[2:] and re.fullmatch(r'\d{4}-\d{2}-\d{2}',str(vc[1])), 'Version Control is not the single initial-version line'
else:
    # ---- 1. clear T and U field cells of the spec sheet
    for m in re.finditer(r'<c r="([TU])(\d+)"',xml):
        r=int(m.group(2))
        if r>hdr_row: touched.add((spec_sheet,m.group(1)+m.group(2)))
    for sheet,ref in sorted(touched):
        xml=set_cell(xml,ref,'')
    modified[sp]=xml
    # ---- 2. Version Control
    assert entries, 'no Version Control entries'
    styles={c:cell_text(vx,f'{c}{entries[0]}')[1] for c in 'BCDEF'}
    for i,c in enumerate('BCDEF'): vx=set_cell(vx,f'{c}{entries[0]}',VC_ROW[i],styles[c]); touched.add(('Version Control',f'{c}{entries[0]}'))
    for rn in entries[1:]:
        for c in 'BCDEF': vx=set_cell(vx,f'{c}{rn}',''); touched.add(('Version Control',f'{c}{rn}'))
    modified[vp]=vx
# ---- 2b. declared unmerges (pre_apply.unmerge), e.g. scenario rows that must receive B/C values
unmerged=set()
for u in (cm.get('pre_apply') or {}).get('unmerge',[]):
    part=sheet_part[u['sheet']]; xml=get_xml(part); rng=u['range']
    m=re.search(r'<mergeCell ref="%s"/>'%re.escape(rng),xml)
    assert m, f'merge {rng} not found in {u["sheet"]}'
    xml=xml[:m.start()]+xml[m.end():]
    xml=re.sub(r'<mergeCells count="(\d+)">',lambda mm: '<mergeCells count="%d">'%(int(mm.group(1))-1),xml,count=1)
    xml=re.sub(r'<mergeCells count="0"></mergeCells>','',xml)
    modified[part]=xml; unmerged.add((u['sheet'],rng))
# ---- 3. cleanup edits
problems=[]
for e in cm['edits']:
    part=sheet_part.get(e['sheet'])
    if not part: problems.append('sheet not found: '+e['sheet']); continue
    cur,style=cell_text(get_xml(part),e['cell'])
    if (norm(cur) or '')!=(norm(e.get('current')) or ''): problems.append(f"{e['sheet']}!{e['cell']}: current mismatch\n   file: {str(cur)[:140]!r}\n   map : {str(e.get('current'))[:140]!r}")
if problems: print('ABORT: %d problem(s)'%len(problems)); print('\n'.join(problems)); sys.exit(2)
for e in cm['edits']:
    part=sheet_part[e['sheet']]; modified[part]=set_cell(get_xml(part),e['cell'],e.get('proposed') or ''); touched.add((e['sheet'],e['cell']))
# ---- 4. PLACEHOLDER -> illustrative value (any sheet)
ph=0
for sheet,part in sheet_part.items():
    xml=get_xml(part)
    for ref in re.findall(r'<c r="([A-Z]+\d+)"',xml):
        if (sheet,ref) in touched: continue
        cur,style=cell_text(xml,ref)
        if cur and 'PLACEHOLDER' in cur and not cur.startswith('='):
            xml=set_cell(xml,ref,cur.replace('PLACEHOLDER','illustrative value'),style); touched.add((sheet,ref)); ph+=1
    if ph: modified[part]=xml
print(f'{A.spec}: {len(cm["edits"])} edits'+('' if A.on_final else ', T/U cleared, Version Control reset')+f', {ph} PLACEHOLDER cells rewritten')
if A.dry_run: print('dry run'); sys.exit(0)
if A.on_final: shutil.copy2(src,prev_copy)
with zipfile.ZipFile(out,'w') as zo:
    for n in z.namelist():
        info=infos[n]; zi=zipfile.ZipInfo(n,date_time=info.date_time); zi.external_attr=info.external_attr
        if n in modified: zi.compress_type=zipfile.ZIP_DEFLATED; zo.writestr(zi,modified[n].encode('utf-8'))
        else: zi.compress_type=info.compress_type; zo.writestr(zi,parts[n])
if A.on_final: z.close(); os.replace(out,final_out); out=final_out; src=prev_copy
print('written',out)
# ---- checks
import openpyxl
zc=zipfile.ZipFile(out); assert zc.testzip() is None and set(zc.namelist())==set(z.namelist())
for n in z.namelist():
    if n not in modified: assert zc.read(n)==parts[n], 'untouched part changed: '+n
wo=openpyxl.load_workbook(src); wf=openpyxl.load_workbook(out); fail=[]
assert wo.sheetnames==wf.sheetnames
changed=[]; formulas=0; tokens=[]
TOK=re.compile(r'\b(NAME|ID|EMAIL|ACCOUNT|PHONE|ADDRESS|ENTID|SHORTID|POSTAL)_\d{4,}\b|\busr?\d{4}@masked\.example\b|\bMASKED_TEXT\b|\bMASKED_POSTAL\b')
for sn in wo.sheetnames:
    a,b=wo[sn],wf[sn]
    if a.max_row!=b.max_row or a.max_column!=b.max_column: fail.append(f'{sn}: dimensions changed')
    ma,mb=set(map(str,a.merged_cells.ranges)),set(map(str,b.merged_cells.ranges))
    if ma!=mb and not (mb<=ma and all((sn,r) in unmerged for r in ma-mb)): fail.append(f'{sn}: merged ranges changed beyond the declared unmerges')
    if len(a._images)!=len(b._images): fail.append(f'{sn}: images changed')
    for row in a.iter_rows():
        for c in row:
            v2=b[c.coordinate].value
            if c.value!=v2 and not (c.value in (None,'') and v2 in (None,'')): changed.append((sn,c.coordinate))
    for row in b.iter_rows():
        for c in row:
            if c.data_type=='f': formulas+=1
            if isinstance(c.value,str) and TOK.search(c.value): tokens.append(f'{sn}!{c.coordinate}')
unexpected=[(s,r) for s,r in changed if (s,r) not in touched]
if unexpected: fail.append('unexpected changed cells: '+', '.join(f'{s}!{r}' for s,r in unexpected[:30]))
if formulas: fail.append(f'{formulas} formula cells')
if tokens: fail.append('masked tokens in: '+', '.join(tokens[:20]))
WORDS={'corrected':r'\bcorrected\b','revised':r'\brevised\b','review':r'\breview(?:s|ed|er|ers|ing)?\b','verified':r'\bverified\b','verifier':r'\bverifier\b','cross-check':r'\bcross-?check(?:s|ed|er|ing)?\b','round 1/2':r'\bround[- ]?[12]\b','proposed status':r'\bproposed status\b','DRAFT':r'\bDRAFT\b','previously':r'\bpreviously\b','no longer':r'\bno longer\b','added after the original build':r'added after the original build','not <number>':r'\bnot \d[\d,.]*\b','corrected from':r'\bcorrected from\b','was X to Y':r'\bwas [A-Z][A-Za-z0-9]* to [A-Z]',"the client's":r"\bthe client'?s\b",'client file/certificates':r"\bclient'?s? (?:file|files|certificates?)\b",'PLACEHOLDER':r'\bPLACEHOLDER\b','rule to be set':r'[Rr]ule to be set|to be set at implementation|set at implementation|\ba definir\b','supplied/agreed at implementation':r'supplied at implementation|agreed and documented at implementation|confirmed at implementation|to be (?:confirmed|defined|decided|agreed)\b','scope_manifest':r'scope_manifest','CO-GAP':r'CO-GAP-\d+','CCG control':r'CCG control|control B\d','CO-SEVERANCE SAVINGS':r'(?i)co-severance savings'}
wc=collections.Counter(); where=collections.defaultdict(list)
for sn in wf.sheetnames:
    for row in wf[sn].iter_rows():
        for c in row:
            if isinstance(c.value,str):
                for w,rx in WORDS.items():
                    n=len(re.findall(rx,c.value))
                    if n: wc[w]+=n; where[w].append(f'{sn}!{c.coordinate}')
print('word counts (must be 0):',{w:wc.get(w,0) for w in WORDS})
for w,l in where.items(): print('   ',w,'->',', '.join(l[:12]))
if sum(wc.values()): fail.append('review/process words remain')
print(f'declared unmerges applied: {sorted(unmerged) if unmerged else "none"}')
print(f'changed cells vs DRAFT: {len(changed)} (all in T/U, Version Control, cleanup or PLACEHOLDER sets: {not unexpected}) | formulas: {formulas} | masked tokens: {len(tokens)} | images per sheet unchanged')
if cm.get('unrewritable'): print('sentences the cleanup could not rewrite without losing content:'); [print('   -',u) for u in cm['unrewritable']]
print('FAIL\n - '+'\n - '.join(fail) if fail else 'PASS')
sys.exit(1 if fail else 0)
