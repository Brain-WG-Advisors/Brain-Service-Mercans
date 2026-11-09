# build text cache (incremental: rows whose register entry or local file is newer than the cache, or missing from it, are re-read)
# build text cache of every register row's local copy: id -> list of (page,text)
import csv,json,os,sys,re,subprocess,zipfile,html
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

def refresh(BASE, OUT, force=False):
    reg = os.path.join(BASE, '00-official-sources/legal-basis-register.csv')
    rows = list(csv.DictReader(open(reg, encoding='utf-8')))
    cache = {}
    t0 = 0
    if os.path.exists(OUT) and not force:
        cache = json.load(open(OUT, encoding='utf-8'))
        t0 = os.path.getmtime(OUT)
    redo = 0
    for r in rows:
        lf = r['local_file'].strip()
        if not lf:
            continue
        parts = [p.strip() for p in re.split(r'[;|]', lf) if p.strip()]
        files = [os.path.join(BASE, p) for p in parts]
        old = cache.get(r['id'])
        newer = any(os.path.isfile(f) and os.path.getmtime(f) > t0 for f in files)
        recorded = sorted({e[0] for e in old}) if old else []
        if old is not None and old and not newer and recorded == sorted(p for p, f in zip(parts, files) if os.path.isfile(f)):
            continue
        out = []
        for part, p in zip(parts, files):
            if os.path.isfile(p):
                for pg, t in extract(p):
                    out.append((part, pg, re.sub(r'\s+', ' ', t)))
        cache[r['id']] = out
        redo += 1
    json.dump(cache, open(OUT, 'w', encoding='utf-8'))
    missing = [r['id'] for r in rows if r['local_file'].strip() and r['id'] not in cache]
    assert not missing, f"bound rows without a cache entry: {missing[:5]}"
    return redo, len(cache)


if __name__ == '__main__':
    redo, n = refresh(sys.argv[1], sys.argv[2], force='--force' in sys.argv)
    print(n, 'rows;', redo, 're-read')
