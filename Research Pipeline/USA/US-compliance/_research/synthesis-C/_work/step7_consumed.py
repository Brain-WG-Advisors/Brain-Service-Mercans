import csv,json,glob,os,sys,re,collections
BASE=sys.argv[1]; RES=os.path.join(BASE,'_research'); P=os.path.join(BASE,'00-official-sources','legal-basis-register.csv')
use=collections.defaultdict(set)
for f in glob.glob(os.path.join(RES,'*-facts.json')):
    d=json.load(open(f,encoding='utf-8')); tok=d['artifact']+('/'+d['unit'] if d.get('unit') else '')
    for x in d['facts']: use[x['register_id']].add(tok)
    for row in (d.get('coverage_matrix') or {}).values():
        for s in row.get('sources',[]): use[s['register_id']].add(tok)
    for v in (d.get('_annex_keys_cited') or {}).values():
        m=re.search(r'\((US-[A-Z0-9]+-[0-9]{3,4})\)',v)
        if m: use[m.group(1)].add(tok)
rows=list(csv.DictReader(open(P,encoding='utf-8',newline=''))); F=list(rows[0].keys())
ids={r['id'] for r in rows}; missing=sorted(set(use)-ids)
n=0; t=0
for r in rows:
    if r['id'] in use:
        cur=[x for x in r['consumed_by'].split(';') if x.strip()]
        add=[x for x in sorted(use[r['id']]) if x not in cur]
        if add: r['consumed_by']=';'.join(cur+add); n+=1; t+=len(add)
w=csv.DictWriter(open(P,'w',encoding='utf-8',newline=''),fieldnames=F,lineterminator='\n'); w.writeheader(); w.writerows(rows)
bad=[(r['id'],r['status'],r['tier']) for r in rows if r['id'] in use and (r['status'] not in('active','partial') or r['tier'] not in('A.1','A.2','A.3'))]
json.dump({'rows_cited':len(use),'rows_updated':n,'tokens_added':t,'missing_ids':missing,'cited_rows_not_active_A':bad},open(os.path.join(RES,'synthesis-C','_work','step7-consumed.json'),'w'),indent=1)
print('rows cited',len(use),'rows updated',n,'tokens added',t,'missing',missing[:10],'non-active/B cited',bad[:10])
