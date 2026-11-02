import sys, zipfile, re, difflib, hashlib
from lxml import etree
sys.stdout.reconfigure(encoding='utf-8')
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
def paras(xml, mode):
    root=etree.fromstring(xml)
    out=[]
    for p in root.iter(W+'p'):
        # skip paragraphs nested? iter covers all incl. table cells
        # paragraph-level deletion mark (paragraph mark deleted) ignored for text compare
        t=[]
        for el in p.iter():
            if el.tag in (W+'t',W+'delText'):
                anc=el.getparent(); ins=dl=False
                while anc is not None and anc is not p:
                    if anc.tag==W+'ins': ins=True
                    if anc.tag==W+'del': dl=True
                    anc=anc.getparent()
                if mode=='accept' and dl: continue
                if mode=='reject' and ins: continue
                t.append(el.text or '')
            elif el.tag==W+'tab': t.append('\t')
        # whole paragraph inserted (rPr of pPr has ins mark)?
        ppr=p.find(W+'pPr'); pins=pdel=False
        if ppr is not None:
            rpr=ppr.find(W+'rPr')
            if rpr is not None:
                pins = rpr.find(W+'ins') is not None
                pdel = rpr.find(W+'del') is not None
        out.append((''.join(t),pins,pdel))
    return out
b=zipfile.ZipFile(sys.argv[1]); d=zipfile.ZipFile(sys.argv[2])
# entries
nb,nd=set(b.namelist()),set(d.namelist())
print('entries only base',nb-nd,'only draft',nd-nb)
print('changed entries',[n for n in sorted(nb&nd) if b.read(n)!=d.read(n)])
base=[x[0] for x in paras(b.read('word/document.xml'),'reject')]
rej=paras(d.read('word/document.xml'),'reject')
acc=paras(d.read('word/document.xml'),'accept')
# reject: drop paragraphs fully inserted (pins and empty text)
rej_t=[t for (t,pi,pd) in rej if not (pi and t=='')]
print('base paras',len(base),'draft paras',len(rej),'reject-kept',len(rej_t))
print('REJECT==BASE:', rej_t==base)
if rej_t!=base:
    for l in list(difflib.unified_diff(base,rej_t,lineterm='',n=0))[:40]: print('  ',l[:300])
acc_t=[t for (t,pi,pd) in acc if not (pd and t=='')]
sm=difflib.SequenceMatcher(None,base,acc_t,autojunk=False)
n=0
with open(sys.argv[3],'w',encoding='utf-8') as f:
    for op,i1,i2,j1,j2 in sm.get_opcodes():
        if op=='equal': continue
        n+=1
        f.write(f'### {op} base[{i1}:{i2}] acc[{j1}:{j2}]\n')
        for t in base[i1:i2]: f.write('- '+t+'\n')
        for t in acc_t[j1:j2]: f.write('+ '+t+'\n')
print('diff hunks',n)
