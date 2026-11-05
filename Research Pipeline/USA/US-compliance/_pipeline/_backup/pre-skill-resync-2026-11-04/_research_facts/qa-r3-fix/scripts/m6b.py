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
grep('US-MAS5-012',r'2027|0\.88%',6)
grep('US-DEP52-001',r'1\.25|one and one-quarter|1 1/4',4)
grep('US-OHS5-017',r'5747\.02|highest',3)
grep('US-NCS5-003',r'one and one-half|time and',3)
grep('US-PAS5-001',r'one and one-half|time and',3)
grep('US-NDS5-017',r'two hundred fifty|250',3)
grep('US-SDS5-017',r'two hundred fifty|250',3)
grep('US-ARP9V-001',r'250',4)
grep('US-WVS5-015',r'seven and one-half|one percent|8\.5|eight and one-half',6)
grep('US-WAS5-017',r'million|threshold|9.9|ESSB|6346',6)
grep('US-MSS5-003',r'2,300|10,000|4%|4\.0',4)
