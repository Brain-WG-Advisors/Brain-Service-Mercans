import re,json,sys,collections
sys.stdout.reconfigure(encoding='utf-8')
PFX='Anomaly codes on the ACRF:'; HDR='Intitulé anomalie Code anomalie Gravité'
RX=re.compile(r'\s*(.*?)\s+(\d{5}-\d{3})\s+(B|NP|NB|P|W|I|A|NBP)\b')
def parse(v):
    body=v[len(PFX):]; hdr=HDR in body; body=body.replace(HDR,'',1)
    out=[];pos=0
    for m in RX.finditer(body):
        out.append((m.group(1).strip(),m.group(2),m.group(3))); pos=m.end()
    rest=body[pos:].strip()
    return out,rest
if __name__=='__main__':
    c=json.load(open('jot_cells.json',encoding='utf-8'))
    T=set(v for _,_,v in c['T'] if v.startswith(PFX)); labs=collections.Counter(); bad=[]
    sev=collections.Counter()
    for v in T:
        o,rest=parse(v)
        if rest or not o: bad.append((v[:120],rest[:80]))
        for l,cd,s in o: labs[l]+=1; sev[s]+=1
        # completeness: rebuild
        rebuilt=' '.join(f'{l} {cd} {s}' for l,cd,s in o)
        if re.sub(r'\s+','',rebuilt)!=re.sub(r'\s+','',v[len(PFX):].replace(HDR,'',1)): bad.append(('REBUILD',v[:150]))
    print('bad',len(bad)); [print(b) for b in bad[:10]]; print(sev)
    json.dump(sorted(labs),open('tlabels.json','w',encoding='utf-8'),ensure_ascii=False,indent=0); print(len(labs))
    for l in sorted(labs): print(repr(l))
