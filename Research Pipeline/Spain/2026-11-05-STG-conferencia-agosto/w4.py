import sys, json
sys.stdout.reconfigure(encoding='utf-8')
w=json.load(open('wtc.json',encoding='utf-8'))['rows']
for c,v in w.items():
    s=' '.join(x or '' for x in v[1:4]).lower()
    if 'ingreso a cuenta' in s or 'gross-up' in s or 'gross up' in s or c in ('6268','65630','65500','65850','62147','62875','62871','62512'):
        print(c,'|',v[1],'| tax',v[13],'BCCC',v[15],'proj',v[12],'AEAT',v[20],v[21],v[22],'|',(v[3] or '')[:600])
