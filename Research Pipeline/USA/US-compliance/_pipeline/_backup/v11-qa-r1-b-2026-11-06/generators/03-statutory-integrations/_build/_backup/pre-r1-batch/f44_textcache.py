# build text cache of every register row's local copy: id -> list of (page,text)
import csv,json,os,sys,re,subprocess,zipfile,html
BASE=sys.argv[1]; OUT=sys.argv[2]
rows=list(csv.DictReader(open(os.path.join(BASE,'00-official-sources/legal-basis-register.csv'),encoding='utf-8')))
cache={}
def pdfpages(p):
    try:
        out=subprocess.run(['pdftotext','-layout',p,'-'],capture_output=True,timeout=120).stdout.decode('utf-8','ignore')
        return [(i+1,t) for i,t in enumerate(out.split('\f'))]
    except Exception as e: return [(0,'')]
import gzip,tempfile
def extract(p):
    with open(p,'rb') as fh: head=fh.read(8)
    if head[:2]==bytes([31,139]):
        data=gzip.open(p).read(); tf=tempfile.NamedTemporaryFile(delete=False,suffix=os.path.splitext(p)[1]); tf.write(data); tf.close()
        return extract(tf.name)
    if head.startswith(b'%PDF'): return pdfpages(p)
    if head.startswith(b'PK'):
        ext=p.lower()
        if ext.endswith(('.xlsx','.xlsm')):
            import openpyxl
            wb=openpyxl.load_workbook(p,read_only=True,data_only=True); res=[]
            for ws in wb.worksheets:
                lines=[' | '.join(str(c) for c in r if c is not None) for r in ws.iter_rows(values_only=True)]
                res.append((ws.title,'\n'.join(lines)))
            return res
        if ext.endswith('.docx'):
            z=zipfile.ZipFile(p); x=z.read('word/document.xml').decode('utf-8','ignore')
            return [(1,html.unescape(re.sub(r'<[^>]+>',' ',x)))]
        try:
            z=zipfile.ZipFile(p); return [(1,'ZIP: '+' '.join(z.namelist()))]
        except Exception: return [(0,'')]
    raw=open(p,'rb').read().decode('utf-8','ignore')
    if re.search(r'<html|<body|<div',raw[:5000],re.I):
        raw=re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>',' ',raw)
        raw=html.unescape(re.sub(r'<[^>]+>',' ',raw))
    return [(1,raw)]
n=0
for r in rows:
    lf=r['local_file'].strip()
    if not lf: continue
    out=[]
    for part in re.split(r'[;|]',lf):
        part=part.strip()
        if not part: continue
        p=os.path.join(BASE,part)
        if os.path.isfile(p):
            for pg,t in extract(p): out.append((part,pg,re.sub(r'\s+',' ',t)))
    cache[r['id']]=out; n+=1
json.dump(cache,open(OUT,'w',encoding='utf-8'))
print(n,'rows;',sum(1 for v in cache.values() if not v),'with missing file')
