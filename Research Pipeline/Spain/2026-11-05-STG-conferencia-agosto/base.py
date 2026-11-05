import sys, json
sys.stdout.reconfigure(encoding='utf-8')
g=json.load(open('g2n.json',encoding='utf-8'))
H=g['hdr']
NAMES={19:'GROSS',30:'TOTDED',31:'NET',39:'TOTER',40:'LIAB'}
E=[]
for r in g['rows']:
    if not r[0]: continue
    d={'id':str(r[0]),'hire':r[3],'term':r[4]}
    for i,h in enumerate(H):
        k = h.split(' - ')[0] if h else NAMES.get(i)
        if k is None or i<5: continue
        v=r[i]
        if isinstance(v,str):
            try: v=float(v) if v!='' else 0.0
            except: pass
        d[k]=v if v is not None else 0.0
    E.append(d)
def f(e,k):
    v=e.get(k,0.0)
    return v if isinstance(v,(int,float)) else 0.0
