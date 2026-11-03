import json,sys,re
sys.path.insert(0,'.')
from lib import *
Q=[('ar.report.sui.efile_threshold_employees',250,'AR',r'electronic|e-?file|online|employees'),
('co.famli.employee.rate',0.44,'CO',r'premium|FAMLI|0\.9'),
('co.famli.employee.rate',0.43,'CO',r'premium|FAMLI|0\.86'),
('co.famli.rate.total',0.86,'CO',r'premium'),
('co.famli.rate.total',0.88,'CO',r'premium'),
('de.local.wilmington.eit.rate',1.25,'DE',r'Wilmington|earned income|wage'),
('ma.pfml.medical.rate',0.7,'MA',r'medical|contribution'),
('ma.pfml.family.rate',0.18,'MA',r'family|contribution'),
('ma.pfml.total',0.88,'MA',r'contribution'),
('ms.oracle',8.94,'MS',r''),
('nc.ot',1.5,'NC',r'one and one-half|overtime|time and'),
('pa.ot',1.5,'PA',r'one and one-half|overtime'),
('nd.breach',250,'ND',r'breach|attorney general'),
('sd.breach',250,'SD',r'breach|attorney general'),
('oh.supp',2.75,'OH',r'supplemental|bonus|rate'),
('wa.agi',1000000,'WA',r'income|million|1,000,000'),
('wv.max',8.5,'WV',r'rate|contribution'),
('sc.band2',3,'SC',r'3\.0%|3%'),
('sc.band3',6,'SC',r'6\.0%|6%'),
]
fields,rows=load_reg()
for key,val,st,ctx in Q:
    print('#####',key,val)
    seen=0
    for r in rows:
        if not r['id'].startswith('US-'+st) or r['status'] not in ('active','partial'): continue
        for p in files_of(r):
            t=text_of(p)
            if not t: continue
            for pos,s in find(val,t):
                sn=snippet(t,pos,110)
                if ctx and not re.search(ctx,sn,re.I): continue
                print(' ',r['id'],p.split('/')[-1][:60],'p',page_at(t,pos),'|',sn[:220]); seen+=1
                if seen>=8: break
            if seen>=8: break
        if seen>=8: break
