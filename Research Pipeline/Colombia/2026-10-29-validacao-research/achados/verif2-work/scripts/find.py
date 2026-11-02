import sys,re,unicodedata
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
t=open(sys.argv[1],encoding='utf-8',errors='replace').read()
parts=re.split(r'--- p\.(\d+) ---',t)
def norm(s): return re.sub(r'\s+',' ',s)
for q in sys.argv[2:]:
    pat=re.compile(r'\s*'.join(re.escape(w) for w in q.split()),re.I)
    hits=[]
    for i in range(1,len(parts),2):
        for m in pat.finditer(parts[i+1]):
            hits.append((parts[i], norm(parts[i+1][max(0,m.start()-150):m.end()+200])))
    print(f'## {q}: {len(hits)} hits')
    for p,s in hits[:4]: print(f'  p.{p}: ...{s}...')
