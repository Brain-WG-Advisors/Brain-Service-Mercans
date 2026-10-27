import zipfile,re,json,sys,os,html,glob
from xml.sax.saxutils import escape
SRC='be19'; OUT=sys.argv[1]
os.makedirs(OUT,exist_ok=True)
targets=json.load(open('targets.json',encoding='utf-8'))
tr={}
for i in range(1,5):
    src=json.load(open(f'batch{i}.json',encoding='utf-8')); en=json.load(open(f'batch{i}_en.json',encoding='utf-8'))
    assert set(src)==set(en)
    for k in src: tr[src[k]]=en[k]
BLUE='FFDDEBF7'; VCTEXT="Field Explanation (M) and Conditional Reason (G) translated to English, per Suman Rai's request"
def unesc(s): return html.unescape(s)
def shared(z):
    x=z.read('xl/sharedStrings.xml').decode('utf-8'); out=[]
    for si in re.findall(r'<si>(.*?)</si>',x,re.S):
        out.append(unesc(''.join(re.findall(r'<t[^>]*>(.*?)</t>',si,re.S))))
    return out
def tcell(ref,s,text): return f'<c r="{ref}" s="{s}" t="inlineStr"><is><t xml:space="preserve">{escape(text)}</t></is></c>'
report={}
for f in sorted(glob.glob(SRC+'/*.xlsx')):
    name=os.path.basename(f); mine=[t for t in targets if t['file']==name]
    if not mine: continue
    z=zipfile.ZipFile(f); sst=shared(z)
    wbx=z.read('xl/workbook.xml').decode(); rels=z.read('xl/_rels/workbook.xml.rels').decode()
    rid={m[0]:m[1] for m in re.findall(r'<sheet [^>]*name="([^"]+)"[^>]*r:id="(rId\d+)"',wbx)}
    tgt={m[0]:m[1] for m in re.findall(r'Id="(rId\d+)"[^>]*Target="([^"]+)"',rels)}
    tgt.update({m[1]:m[0] for m in re.findall(r'Target="([^"]+)"[^>]*Id="(rId\d+)"',rels)})
    core=[n for n in rid if n.endswith('Spec')][0]
    cpath='xl/'+tgt[rid[core]]; vpath='xl/'+tgt[rid['Version Control']]
    sty=z.read('xl/styles.xml').decode()
    # new fill
    fm=re.search(r'<fills count="(\d+)">(.*?)</fills>',sty,re.S); nf=int(fm.group(1))
    sty=sty.replace(fm.group(0),f'<fills count="{nf+1}">{fm.group(2)}<fill><patternFill patternType="solid"><fgColor rgb="{BLUE}"/><bgColor rgb="{BLUE}"/></patternFill></fill></fills>')
    xm=re.search(r'<cellXfs count="(\d+)">(.*?)</cellXfs>',sty,re.S); xfs=re.findall(r'<xf\b[^>]*?(?:/>|>.*?</xf>)',xm.group(2),re.S); assert len(xfs)==int(xm.group(1))
    clones={}
    def blue(s):
        s=int(s)
        if s not in clones:
            x=xfs[s]; x=re.sub(r'fillId="\d+"',f'fillId="{nf}"',x) if 'fillId=' in x else x.replace('<xf ',f'<xf fillId="{nf}" ',1)
            x=x.replace('applyFill="0"','applyFill="1"') if 'applyFill=' in x else x.replace('<xf ','<xf applyFill="1" ',1)
            clones[s]=len(xfs)+len(clones); newx.append(x)
        return clones[s]
    newx=[]
    sx=z.read(cpath).decode('utf-8'); n=0
    for t in mine:
        ref=t['cell']; m=re.search(rf'<c r="{ref}" s="(\d+)" t="s"><v>(\d+)</v></c>',sx); assert m,(name,ref)
        assert sst[int(m.group(2))]==t['text'],(name,ref)
        new=t['prefix']+tr[t['body']]
        sx=sx.replace(m.group(0),tcell(ref,blue(m.group(1)),new),1); n+=1
    # version control row
    vx=z.read(vpath).decode('utf-8')
    rows=re.findall(r'<row r="(\d+)"[^>]*>(.*?)</row>',vx,re.S)
    last=max(int(r) for r,c in rows if re.search(rf'<c r="B{r}"',c) and int(r)>12)
    lastrow=dict(rows)[str(last)]; st=dict(re.findall(r'<c r="([B-F])\d+" s="(\d+)"',lastrow))
    nr=last+1
    cells=(tcell(f'B{nr}',blue(st['B']),'1.1')+f'<c r="C{nr}" s="{blue(st["C"])}"><v>46314</v></c>' if st['C']!='' else '')
    # effective date style: if original C was a string date, keep string
    if f'<c r="C{last}" s="{st["C"]}" t="s">' in lastrow: cells=tcell(f'B{nr}',blue(st['B']),'1.1')+tcell(f'C{nr}',blue(st['C']),'2026-10-19')
    cells+=tcell(f'D{nr}',blue(st['D']),VCTEXT)+tcell(f'E{nr}',blue(st['E']),'Draft')+tcell(f'F{nr}',blue(st['F']),'Wallisson Gomes')
    em=re.search(rf'<row r="{nr}"([^>]*?)(/>|>(.*?)</row>)',vx,re.S); assert em and not (em.group(3) or '').strip(),'row not empty'
    vx=vx.replace(em.group(0),f'<row r="{nr}"{em.group(1)}>{cells}</row>',1)
    sty=sty.replace(xm.group(0),f'<cellXfs count="{len(xfs)+len(newx)}">{xm.group(2)}{"".join(newx)}</cellXfs>')
    outname=name.replace('.xlsx','_v1.1.xlsx'); zo=zipfile.ZipFile(os.path.join(OUT,outname),'w')
    for it in z.infolist():
        data=z.read(it.filename)
        if it.filename==cpath: data=sx.encode('utf-8')
        elif it.filename==vpath: data=vx.encode('utf-8')
        elif it.filename=='xl/styles.xml': data=sty.encode('utf-8')
        zo.writestr(it,data,compress_type=it.compress_type)
    zo.close(); report[outname]=dict(cells=n,vcrow=nr,core=core)
print(json.dumps(report,indent=1))
