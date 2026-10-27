import sys,os,glob,json,re,zipfile,hashlib
from openpyxl import load_workbook
sys.path.insert(0,'.'); from langdefs import *
OUT=sys.argv[1]
targets=json.load(open('targets.json',encoding='utf-8'))
def sig(c):
    g=lambda o,a: getattr(o,a,None)
    b=c.border
    return (c.value, c.number_format, g(c.font,'name'),g(c.font,'sz'),g(c.font,'b'),g(c.font,'i'),str(g(c.font.color,'rgb') if c.font.color else None),
            c.fill.fill_type, str(c.fill.fgColor.rgb), c.alignment.horizontal,c.alignment.vertical,c.alignment.wrap_text,
            tuple(g(getattr(b,s),'style') for s in ('left','right','top','bottom')))
FRW=None
def fr_left(v):
    t=re.sub(r"\([^()]*\)","",v); t=re.sub(r"[«“\"‘'][^»”\"’']*[»”\"’']","",t).lower()
    w=re.findall(r"[a-zàâçéèêëîïôûùüÿœ]+",t); return sum(x in FR for x in w if x not in EN)+sum(x in NL for x in w if x not in EN), w
tot={}
for f in sorted(glob.glob(OUT+'/*_v1.1.xlsx')):
    name=os.path.basename(f).replace('_v1.1',''); a=load_workbook('be19/'+name); b=load_workbook(f)
    allowed={(t['cell']) for t in targets if t['file']==name}
    diffs=[];changed=0;notblue=[]
    assert a.sheetnames==b.sheetnames
    for sn in a.sheetnames:
        wa,wb_=a[sn],b[sn]
        mr=max(wa.max_row,wb_.max_row); mc=max(wa.max_column,wb_.max_column)
        for r in range(1,mr+1):
            for c in range(1,mc+1):
                ca,cb=wa.cell(r,c),wb_.cell(r,c); sa,sb=sig(ca),sig(cb)
                if sa==sb: continue
                if sn.endswith('Spec') and cb.coordinate in allowed:
                    changed+=1
                    if sa[1:7]!=sb[1:7] or sa[9:]!=sb[9:] or sb[8]!='FFDDEBF7' or sa[0]==sb[0]: notblue.append(cb.coordinate)
                elif sn=='Version Control' and ca.value is None: pass
                else: diffs.append((sn,cb.coordinate,sa[0] if not isinstance(sa[0],str) else sa[0][:40],sb[0] if not isinstance(sb[0],str) else sb[0][:40]))
    core=[s for s in b.sheetnames if s.endswith('Spec')][0]; ws=b[core]; viol=[]
    for row in ws.iter_rows(min_row=2):
        for c in row:
            if c.column_letter in 'GM' and isinstance(c.value,str):
                v=c.value.replace("Restated at its corrected value for the original quarter. ","")
                n,w=fr_left(v); st=v.strip(' .;').lower()
                if n>=2 or st in ('interdit','obligatoire','facultatif'): viol.append((c.coordinate,n,v[:140]))
    vc=[[c.value for c in r] for r in b['Version Control'].iter_rows(min_row=13) if any(c.value for c in r)]
    z=zipfile.ZipFile(f); bad=z.testzip()
    print('##',os.path.basename(f),hashlib.md5(open(f,'rb').read()).hexdigest())
    print('  targets',len(allowed),'changed',changed,'| style/value problems',len(notblue),notblue[:5],'| other diffs',len(diffs),diffs[:8])
    print('  residual FR in G/M',len(viol)); [print('    ',x) for x in viol[:12]]
    print('  VC',vc,'zip',bad)
