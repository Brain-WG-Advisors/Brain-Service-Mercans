import sys,json,re,os,csv,time,io,functools,collections,glob
sys.argv=['x','../../..','cache.json','/dev/null','DD-8_sheets']
src=open('selfcheck.py',encoding='utf-8').read().split('res, miss = [], []')[0]
exec(src)
_t=texts
@functools.lru_cache(maxsize=None)
def tx1(r): return _t([r])
def texts(rids):
    o=[]
    for r in rids: o+=tx1(r)
    return o
R='../..'
JUNK={'NOT','URL','AND','THE','DOES','MANDATE','MULTI'}
rs=json.load(open('resync.json',encoding='utf-8'))
ref={}
for fn in sorted(glob.glob(R+'/CCG-*-facts.json'))+[R+'/RSPEC-facts.json']:
    for f in json.load(open(fn,encoding='utf-8'))['facts']: ref[(f['key'],f.get('effective_from'))]=f
LOCK=R+'/facts.lock'
def lock():
    for i in range(600):
        try: return os.open(LOCK,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
        except FileExistsError: time.sleep(1)
    raise SystemExit('lock busy')
tok={'DD-8_sheets':'DD/8_sheets','WTC-global_baseline':'WTC/global_baseline','WTC-country_specific':'WTC/country_specific','SIR':'SIR/third_party_provider_handoff','PSL':'PSL/payslip'}
newrefs=collections.defaultdict(set); log=[]
def distinct(kind,el):
    if kind in('form','iso','qtr'): return True
    if kind=='chan': return False
    if kind=='word': return len(el)>=4 and el not in JUNK
    if kind in('num','numv'):
        s=str(el); return ('.' in s and len(s.split('.')[1])>=2) or (',' in s and len(s.replace(',',''))>=5)
    return False
for fn in tok:
    path=R+'/%s-facts.json'%fn
    fd=lock()
    try:
        raw=open(path,encoding='utf-8').read(); d=json.loads(raw)
        ind=1 if raw.startswith('{\n "') else 2
        ch=collections.Counter(); unm=[]
        for f in d['facts']:
            r=ref.get((f['key'],f.get('effective_from')))
            if r:
                for fld in('value','effective_to'):
                    if f.get(fld)!=r.get(fld):
                        f.setdefault('_precheck_prev_'+fld,f.get(fld)); f[fld]=r.get(fld); ch['resync_'+fld]+=1
                if f['register_id']!=r['register_id']:
                    old=f['register_id']; f['register_id']=r['register_id']
                    a=f.setdefault('_also_register_ids',[])
                    if old not in a: a.append(old)
                    f['_precheck_prev_register_id']=old; ch['resync_register_id']+=1
            rids=[f['register_id']]+list(f.get('_also_register_ids',[]))
            T=texts(rids); loc=[]; left=[]
            for kind,el in elements(f['value']):
                h=numv_find(el,T) if kind=='numv' else find(el,kind,T)
                if not h and kind=='form' and ' ' in el:
                    a_,b_=el.split(' ',1)
                    h1=find(a_,'form' if re.search(r'\d',a_) else 'word',T); h2=find(b_,'form',T) or find(b_.split('-')[0],'num',T)
                    if h1 and h2: h=True
                if h: continue
                if distinct(kind,el):
                    p=re.match(r'US-([A-Z]{2})',rids[0]).group(1)
                    cands=[c for c in cache if c not in rids and cache[c] and c.startswith('US-'+p) and not (p in('FE','FI','MU') and False)]
                    if p not in('FE','FI','MU'): cands=[c for c in cands if not c.startswith(('US-FED','US-FIL','US-MULTI'))]
                    hit=None
                    for c in cands:
                        h=numv_find(el,tx1(c)) if kind=='numv' else find(el,kind,tx1(c))
                        if h: hit=(c,h);break
                    if hit:
                        c,h=hit; a=f.setdefault('_also_register_ids',[])
                        if c not in a: a.append(c)
                        newrefs[c].add(tok[fn]); ch['repointed']+=1
                        loc.append("%s '%s' found in %s %s p%s: \"%s\""%(kind,el,c,h[1],h[2],h[3][40:190].strip()))
                        continue
                left.append('%s:%s'%(kind,el))
            if loc:
                f['_figure_located']=(f.get('_figure_located','')+' | ' if f.get('_figure_located') else '')+'2026-11-03 agent 2 (precheck-next): '+' ; '.join(loc)
            if left:
                f['_precheck_unmatched']=left; ch['unmatched_facts']+=1; unm.append((f['key'],f.get('effective_from'),left))
            else: f.pop('_precheck_unmatched',None)
        # aggregate non-blocking unresolved
        d['unresolved']=[u for u in d['unresolved'] if u.get('key')!='precheck.next.text_elements_unmatched']
        if unm:
            d['unresolved'].append({'key':'precheck.next.text_elements_unmatched','why':'Pre-build text check 2026-11-03: %d fact values carry text elements (acronym expansions, our own wording, derived numbers, worked-example arithmetic, or rows whose copy is blocked) that do not appear in the local copy of the cited register row(s); each is listed in the fact _precheck_unmatched'%len(unm),'attempted':['selfcheck over local copies of register_id + _also_register_ids','same-jurisdiction rows of the register','re-download of 41 copy-less rows into 00-official-sources/precheck-copies (15 blocked: 403/429/Cloudflare/JS)'],'what_would_close_it':'Builder treats listed elements as our gloss (not source-quoted); or agent 2 rewrites the value to the copy wording / adds the row carrying it; blocked rows need a browser-read copy','blocking':False})
        open(path,'w',encoding='utf-8').write(json.dumps(d,ensure_ascii=False,indent=ind)+('\n' if raw.endswith('\n') else ''))
        log.append((fn,dict(ch)))
    finally:
        os.close(fd); os.remove(LOCK)
print(log)
# consumed_by
fd=lock()
try:
    REG='../../../00-official-sources/legal-basis-register.csv'
    raw=open(REG,encoding='utf-8',newline='').read(); rows=list(csv.reader(io.StringIO(raw)))
    h=rows[0]; ii=h.index('id'); ci=h.index('consumed_by'); n=0
    for r in rows[1:]:
        if r[ii] in newrefs:
            cur=[x for x in r[ci].split(';') if x]
            for t in newrefs[r[ii]]:
                if t not in cur: cur.append(t); n+=1
            r[ci]=';'.join(cur)
    o=io.StringIO(); csv.writer(o,lineterminator='\r\n' if '\r\n' in raw else '\n').writerows(rows); open(REG,'w',encoding='utf-8',newline='').write(o.getvalue()); print('consumed_by tokens added',n)
finally: os.close(fd); os.remove(LOCK)
