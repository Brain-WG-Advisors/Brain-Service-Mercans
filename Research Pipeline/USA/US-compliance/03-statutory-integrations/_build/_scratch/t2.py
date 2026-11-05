import sys,os,re,collections
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import sir_common as S
J=S.C.STATES
topics={'wh':r'withholding\.returns?|nys45|oq|ui_pit\.returns','w2':r'w2\.|de9c','ui':r'ui\.wage_report|ui\.flat|ui\.xml|ui\.csv|ui_pit','auth':r'agent_authorization|representative|ui\.agent','nh':r'new_hire\.(days|recipient)|newhire'}
cov=collections.defaultdict(lambda: collections.defaultdict(list))
for k in S.SIR_KEYS+['ks.newhire.report_days','rspec.mn.pfml_qtr.form','rspec.ny.mctmt.form']:
    p=k.split('.')
    j=p[1].upper() if p[0] in('sir','rspec') else p[0].upper()
    for t,rx in topics.items():
        if re.search(rx,'.'.join(p[2:] if p[0] in ('sir','rspec') else p[1:])): cov[j][t].append(k)
for j in J:
    row=[ (t,len(cov[j][t])) for t in topics]
    print(j,row)
