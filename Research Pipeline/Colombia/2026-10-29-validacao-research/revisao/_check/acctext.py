import sys,zipfile,re
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0,sys.argv[2])
from lxml import etree
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
root=etree.fromstring(zipfile.ZipFile(sys.argv[1]).read('word/document.xml'))
out=[]
for p in root.iter(W+'p'):
    t=[]
    for el in p.iter():
        if el.tag==W+'t':
            a=el.getparent(); dl=False
            while a is not None and a is not p:
                if a.tag==W+'del': dl=True
                a=a.getparent()
            if not dl: t.append(el.text or '')
    out.append(''.join(t))
open(sys.argv[3],'w',encoding='utf-8').write('\n'.join(f'{i}\t{x}' for i,x in enumerate(out)))
