import sys,glob,os,re,json,collections
sys.stdout.reconfigure(encoding='utf-8',errors='replace'); sys.path.insert(0,'.')
from langdefs import FR,NL,EN
from openpyxl import load_workbook
HOM={'moment','minutes','date','zone','si','ce','au','entre','ne','commission','type','code','de','service','occupation','pension','article','base','cotisation','note','position'}
FRX=FR|set("à été être où après avant chaque lorsqu autre autres cas même ainsi peut doivent concerné cadre ayant auprès fixant correspondant relative mesure période travailleurs données numéro invalide présent domaine définition longueur incorrecte erreur séquence cardinalité admis numérique zone pas application non chiffres maximum composé".split())-HOM
NLX=NL-{'die','dat','van','met'}|{'werknemers','bijdragen','werkgevers','onderworpen'}
def local_hdr(h):
    h=(h or '').lower(); return ('(fr' in h or '(nl' in h or 'local' in h or '(de' in h) and '(en' not in h
def strip(v): v=re.sub(r"\([^()]*\)","",v); return re.sub(r"[«“\"‘'][^»”\"’']*[»”\"’']","",v)
def score(v):
    w=re.findall(r"[a-zàâçéèêëîïôûùüÿœ]+",strip(v).lower()); return sum(x in FRX for x in w)+sum(x in NLX for x in w), sum(x in EN for x in w)
res=collections.defaultdict(list); v14=collections.Counter()
for f in sorted(glob.glob(sys.argv[1]+'/*.xlsx')):
    wb=load_workbook(f,read_only=True); name=os.path.basename(f)
    for sn in wb.sheetnames:
        rows=list(wb[sn].iter_rows(values_only=True))
        if not rows: continue
        hr=0
        for i,r in enumerate(rows[:6]):
            if sum(1 for v in r if v)>=3: hr=i; break
        hdr={j:str(v) for j,v in enumerate(rows[hr]) if v}
        for i,r in enumerate(rows,start=1):
            for j,v in enumerate(r):
                if not isinstance(v,str): continue
                if 'v1.4' in v: v14[(name,sn)]+=1
                if sn=='Sample File' or local_hdr(hdr.get(j)) or i<=hr+1 and sn!='Version Control' and False: continue
                if v.startswith('═'): continue
                fr,en=score(v)
                if fr>=2 or (fr>=1 and en==0 and len(v)<60):
                    col=chr(65+j) if j<26 else '?'
                    res[(name,sn,col,hdr.get(j,'')[:30])].append((f"{col}{i}",v))
json.dump({ '|'.join(k):v for k,v in res.items()},open(sys.argv[2],'w',encoding='utf-8'),ensure_ascii=False)
for k,v in sorted(res.items()): print(k,len(v),'|',v[0][0],v[0][1][:90])
print('v1.4 by sheet'); [print('  ',k,n) for k,n in sorted(v14.items())]
