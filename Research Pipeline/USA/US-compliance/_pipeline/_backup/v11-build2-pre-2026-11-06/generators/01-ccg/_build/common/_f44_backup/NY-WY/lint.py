import sys,re,json,glob,os
sys.path.insert(0, os.path.expanduser('~/mercans-pipeline/shared/consistency-checks'))
import consistency_checks as cc
BASE=os.path.abspath('../..')
facts={}
for fp in glob.glob(os.path.join(BASE,'_research','*-facts.json')):
    for f in json.load(open(fp,encoding='utf-8')).get('facts',[]):
        facts.setdefault(f['key'],[]).append(f.get('value'))
forms={}
for k,vs in facts.items():
    for v in vs:
        for n,pct in cc.distinctive_forms(k,v):
            forms.setdefault((round(n,6),pct),set()).add(k)
MARK=re.compile(r"(TODO|TBD|FIXME|XXX|\[CHECK\]|\[\?\]|VERIFY No\.|to be confirmed|to be verified|\[placeholder\])",re.I)
for st in sys.argv[1].split(','):
    p=os.path.join(BASE,'01-ccg','annexes',f'annex_{st}.md'); t=open(p,encoding='utf-8').read()
    bad=0
    for i,line in enumerate(t.splitlines(),1):
        for m in cc.TAG.finditer(line):
            k,v=m.group(1),m.group(2)
            ok=any((cc._num(v) is not None and cc._num(x) is not None and abs(cc._num(v)-cc._num(x))<1e-9) or str(v).strip()==str(x).strip() for x in facts.get(k,[]))
            if not ok: print(st,i,'TAGMISMATCH',k,v); bad+=1
        bare=cc.TAG.sub(' ',line)
        bare2=re.sub(r'`[^`]*`','',bare)
        for m in cc.NUM_IN_TEXT.finditer(bare):
            n=cc._num(m.group(1))
            if n is None: continue
            ks=forms.get((round(n,6),bool(m.group(2))))
            if ks: print(st,i,'UNBOUND',m.group(0),sorted(ks)[:3]); bad+=1
        if MARK.search(bare): print(st,i,'MARKER',MARK.search(bare).group(0)); bad+=1
        if '--show' in sys.argv:
            s=re.sub(r'\[US-[^\]]*\]|US-[A-Z0-9]+-\d+|\d{4}-\d{2}-\d{2}','',bare2)
            nums=re.findall(r'(?<![A-Za-z\-])\d[\d,.]*',s)
            if nums and not line.startswith('| `'): print(st,i,'DIGITS',nums[:8],'::',line[:110])
    print(st,'issues',bad)
