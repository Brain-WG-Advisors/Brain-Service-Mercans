import sys, json
sys.stdout.reconfigure(encoding='utf-8')
w=json.load(open('wtc.json',encoding='utf-8'))
for c in ['62100','62147','62148','62182','62512','62871','62875','79413','79414','79415','79416','65500','65630','65850','21140','21142','2582','6268']:
    v=w['rows'].get(c)
    if not v: print(c,'MISSING');continue
    print(c,v[1],'| cat',v[4],'| proj',v[12],'| tax',v[13],'| BCCC',v[15],'| BCCP',v[16],'| AEATamt',v[22],'| pay',v[27],'| xpay',v[29],'| irreg',v[31])
    print('   F:',(v[5] or '')[:400])
