import sys,os
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.stdout.reconfigure(encoding='utf-8')
import sir_common as S, sir_defs as D
keys=[]
for name in ('PROVIDER_ROWS','TECH_ROWS','RULE_ROWS','DEADLINE_ROWS'):
    keys+= [(name,k) for _,k in getattr(D,name)]
for g in D.INBOUND_FACTS.values(): keys+=[('INB',k) for _,k in g]
for sec,rows in D.DATA_SET.items(): keys+=[('DATA',k) for _,_,k in rows]
for sp,ch in D.FED_ROWS.items():
    for _,ks in ch: keys+=[(sp,k) for k in ks]
for n,k in keys:
    ok,why=S.usable(k)
    if not ok: print(n,k,why if not isinstance(why,tuple) else ('f44',why[1][:3]))
