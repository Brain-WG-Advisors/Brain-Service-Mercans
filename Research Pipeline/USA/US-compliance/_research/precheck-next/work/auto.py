import sys,json,re,os,csv
sys.argv=['x','../../..','cache.json','/dev/null','DD-8_sheets']
src=open('selfcheck.py',encoding='utf-8').read().split('res, miss = [], []')[0]
exec(src)
before=json.load(open('before.json',encoding='utf-8'))
reg={r['id']:r for r in csv.DictReader(open('../../../00-official-sources/legal-basis-register.csv',encoding='utf-8'))}
def pref(rid):
    m=re.match(r'US-([A-Z]{2})',rid);return m.group(1)
JUNK={'NOT','URL','AND','THE'}
plan={}   # (file,key)->list of (el, rid, quote)
left=[]
for m in before['misses']:
    kind,el=m['kind'],m['element']
    if kind=='numv' or m['no_copy'] and False: pass
    if kind=='word' and el in JUNK: left.append(m);continue
    if kind=='num':
        s=str(el)
        if not (len(s.replace(',','').replace('.',''))>=4 or '.' in s or ',' in s): left.append(m);continue
    p=pref(m['rids'][0])
    cands=[r for r in cache if r not in m['rids'] and cache[r] and (r.startswith('US-'+p) or r.startswith(('US-FED','US-FIL','US-MULTI')))]
    if kind=='numv': h=None;
    hit=None
    for r in cands:
        T=texts([r])
        h=numv_find(el,T) if kind=='numv' else find(el,kind,T)
        if h: hit=(r,h);break
    if hit:
        plan.setdefault((m['file'],m['key']),[]).append((kind,el,hit[0],hit[1][1],hit[1][2],hit[1][3][:200]))
    else: left.append(m)
json.dump({'plan':{f'{a}||{b}':v for (a,b),v in plan.items()},'left':left},open('auto.json','w'),ensure_ascii=False,indent=1)
print(len(plan),'facts with repoints;',len(left),'misses left')
