import json,sys
sys.stdout.reconfigure(encoding='utf-8')
pairs={'F2':'D002_r2','F4':'D004_r2','F5':'D005_r2','NE':'NE_r2','P3':'P003_r2','P7':'P007_r2','DD':'DD'}
for k,o in pairs.items():
    n=json.load(open(f'_check3_{k}.json',encoding='utf-8')); old=json.load(open(f'_check/{o}.json',encoding='utf-8'))
    od={(c['sheet'],c['cell']):c for c in old['cells']}
    ch=[]
    for c in n['cells']:
        p=od.get((c['sheet'],c['cell']))
        if p is None or p['new']!=c['new']: ch.append(c['sheet']+'!'+c['cell'])
    print(k,'total',n['n_changed_cells'],'(was',old['n_changed_cells'],') nonblue',n['nonblue'],'r3:',ch)
