import zipfile,re,os,shutil,html
BLUE='FFDDEBF7'
def esc(t): return t.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
def sheetmap(z):
    wb=z.read('xl/workbook.xml').decode('utf-8'); rel=z.read('xl/_rels/workbook.xml.rels').decode('utf-8')
    rid={m.group(2):m.group(1) for m in re.finditer(r'Target="([^"]+)" Id="([^"]+)"',rel)}
    rid.update({m.group(1):m.group(2) for m in re.finditer(r'Id="([^"]+)"[^>]*Target="([^"]+)"',rel)})
    out={}
    for m in re.finditer(r'<sheet [^>]*?name="([^"]+)"[^>]*?r:id="([^"]+)"',wb):
        t=rid[m.group(2)].lstrip('/'); 
        if not t.startswith('xl/'): t='xl/'+t
        out[html.unescape(m.group(1))]=t
    return out
def blue_style(sty,s):
    # sty: styles xml str; returns (newsty,newindex)
    fills=re.search(r'<fills[^>]*>(.*?)</fills>',sty,re.S).group(1)
    fl=re.findall(r'<fill>.*?</fill>',fills,re.S)
    bid=next(i for i,f in enumerate(fl) if BLUE in f)
    m=re.search(r'<cellXfs count="(\d+)">(.*?)</cellXfs>',sty,re.S)
    xfs=re.findall(r'<xf\b[^>]*?(?:/>|>.*?</xf>)',m.group(2),re.S)
    x=xfs[s]
    if re.search(r'fillId="%d"'%bid,x): return sty,s
    nx=re.sub(r'fillId="\d+"','fillId="%d"'%bid,x)
    if 'applyFill' in nx: nx=re.sub(r'applyFill="\d"','applyFill="1"',nx)
    else: nx=nx.replace('<xf ','<xf applyFill="1" ',1)
    if nx in xfs: return sty,xfs.index(nx)
    xfs.append(nx)
    new='<cellXfs count="%d">%s</cellXfs>'%(len(xfs),''.join(xfs))
    return sty[:m.start()]+new+sty[m.end():],len(xfs)-1
def edit(path,edits,keepfill=False):
    """edits: {(sheet,ref):text}"""
    z=zipfile.ZipFile(path); sm=sheetmap(z)
    data={i.filename:z.read(i.filename) for i in z.infolist()}
    infos={i.filename:i for i in z.infolist()}; order=[i.filename for i in z.infolist()]
    sty=data['xl/styles.xml'].decode('utf-8'); z.close()
    bysheet={}
    for (sh,ref),t in edits.items(): bysheet.setdefault(sh,{})[ref]=t
    for sh,ed in bysheet.items():
        fn=sm[sh]; x=data[fn].decode('utf-8')
        for ref,t in ed.items():
            m=re.search(r'<c r="%s"([^>]*?)(/>|>.*?</c>)'%ref,x,re.S)
            if not m: raise Exception('cell not found '+sh+ref)
            sm_=re.search(r' s="(\d+)"',m.group(1)); s=int(sm_.group(1)) if sm_ else 0
            sty,ns=blue_style(sty,s)
            if t is None:
                x=x[:m.start()]+'<c r="%s" s="%d"/>'%(ref,ns)+x[m.end():]; continue
            sp=' xml:space="preserve"' if (t!=t.strip() or '  ' in t or '\n' in t or t=='') else ''
            new='<c r="%s" s="%d" t="inlineStr"><is><t%s>%s</t></is></c>'%(ref,ns,sp,esc(t))
            x=x[:m.start()]+new+x[m.end():]
        data[fn]=x.encode('utf-8')
    data['xl/styles.xml']=sty.encode('utf-8')
    tmp=path+'.tmp'
    with zipfile.ZipFile(tmp,'w') as o:
        for n in order:
            zi=zipfile.ZipInfo(n,infos[n].date_time); zi.compress_type=infos[n].compress_type; zi.external_attr=infos[n].external_attr
            o.writestr(zi,data[n])
    os.replace(tmp,path)
