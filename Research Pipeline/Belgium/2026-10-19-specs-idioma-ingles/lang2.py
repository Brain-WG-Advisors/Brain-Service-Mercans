import sys,glob,os,re
from openpyxl import load_workbook
sys.path.insert(0,'.')
FR=set("le la les des du une est sont pour avec dans par sur qui que ou si doit être cette ce ces aux au lorsque été pas ne il elle leur nombre montant valeur valeurs voir annexe obligatoire interdit facultatif présent travailleur employeur déclaration jour mois année heures minutes heure semaine trimestre élément entier positif exprimé caractères série moment début selon entre lequel laquelle dont commission paritaire ouvriers employés banques auxiliaire".split())
NL=set("het een van voor met zijn wordt worden niet deze die dat bij aan door naar als ook werkgever werknemer bijdrage jaar maand dag uren verplicht".split())
EN=set("the and of for with is are be to in on by if must when this that which not from or field value values amount mandatory employee employer see annex number date month year day hours code".split())
ISOL={"interdit","obligatoire","facultatif","non présent"}
def clean(s): s=re.sub(r"\([^()]*\)","",s); s=re.sub(r"[«“\"‘'][^»”\"’']*[»”\"’']","",s); return s.lower()
def cnt(s):
    w=re.findall(r"[a-zàâçéèêëîïôûùüÿœ]+",clean(s)); return sum(x in FR for x in w)+sum(x in NL for x in w), sum(x in EN for x in w), w
TARGET={"G":"Conditional Reason","J":"Format","M":"Field Explanation","O":"Option Values","T":"Query to RA"}
for f in sorted(glob.glob(sys.argv[1]+'/*.xlsx')):
    wb=load_workbook(f,read_only=True); name=os.path.basename(f)
    core=[s for s in wb.sheetnames if s.endswith('Spec')][0]
    rows=list(wb[core].iter_rows(values_only=True))
    print("##",name)
    for col,lab in TARGET.items():
        j=ord(col)-65; V=[];D=[];n=0
        for i,r in enumerate(rows[1:],start=2):
            v=r[j] if j<len(r) else None
            if not isinstance(v,str) or not v.strip() or v.startswith("═"): continue
            n+=1; loc,en,w=cnt(v); st=clean(v).strip(" .;")
            if st in ISOL or (loc>=3 and loc>=en): V.append((i,v))
            elif loc>=2: D.append((i,v))
        print(f"  {col} {lab}: V {len(V)} D {len(D)} de {n}")
        for i,v in (V[:1]+V[len(V)//2:len(V)//2+1]) if V else []: print(f"     V {col}{i}: {v[:170]!r}")
        for i,v in D[:1]: print(f"     D {col}{i}: {v[:170]!r}")
    if 'Field Options' in wb.sheetnames:
        fo=list(wb['Field Options'].iter_rows(values_only=True)); C=[]
        for i,r in enumerate(fo,start=1):
            v=r[2] if len(r)>2 else None
            if isinstance(v,str):
                loc,en,w=cnt(v)
                if loc>=2 and en==0: C.append((i,v))
        print(f"  Field Options C Description (EN): V {len(C)}", [f"C{i}: {v[:90]}" for i,v in C[:2]])
