import csv,glob,sys,re
sys.stdout.reconfigure(encoding="utf-8")
keys=sys.argv[1].split(',')
for p in glob.glob('_pipeline/*bindings*.csv'):
    art=p.split('_pipeline')[1][1:].split('-bindings')[0]
    for r in csv.DictReader(open(p,encoding='utf-8')):
        k=r.get('key')
        if k in keys:
            print(k,'|',art,'|',(r.get('location') or '')[:110],'|',r.get('section','')[:50],'|',r.get('register_id'),'|',r.get('value_shown','')[:40])
