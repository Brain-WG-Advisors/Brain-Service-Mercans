import sys; sys.stdout.reconfigure(encoding="utf-8",errors="replace")
import sys,re
sys.path.insert(0,'.')
from lib import *
fields,rows=load_reg(); R={r['id']:r for r in rows}
def grep(rid,pat,n=4,w=160):
    for p in files_of(R[rid]):
        t=text_of(p)
        if not t and p.endswith('.bin'):
            import pymupdf
            try: d=pymupdf.open(p,filetype='pdf'); t='\n'.join(f'[[PAGE {i+1}]]\n'+pg.get_text() for i,pg in enumerate(d))
            except Exception as e: t=''; print('  binerr',e)
        print(' ',rid,p.split('/')[-1][:60],'len',len(t))
        k=0
        for m in re.finditer(pat,t,re.I):
            print('    p',page_at(t,m.start()),'|',snippet(t,m.start(),w)); k+=1
            if k>=n: break

def grepall(st,pat,n=6,w=150):
    k=0
    for r in rows:
        if not r['id'].startswith('US-'+st) or r['status'] not in ('active','partial'): continue
        for p in files_of(r):
            t=text_of(p)
            for m in re.finditer(pat,t,re.I):
                print('   ',r['id'],p.split('/')[-1][:50],'p',page_at(t,m.start()),'|',snippet(t,m.start(),w)); k+=1
                if k>=n: return
