exec(open('base.py',encoding='utf-8').read())
for e in E:
    if e['id'] in ('1018096','1001489') or f(e,'2582') or f(e,'79413') or f(e,'79414') or f(e,'79415') or f(e,'79416') or f(e,'58213')!=100 or f(e,'58205')!=1 or f(e,'58218'):
        print({k:v for k,v in e.items() if v not in (0,0.0,'')})
        print()
