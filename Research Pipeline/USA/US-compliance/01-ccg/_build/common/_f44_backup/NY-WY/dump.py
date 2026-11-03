import json,sys,re
st=sys.argv[1]
d=json.load(open(f'../../_research/CCG-annex_{st}-facts.json',encoding='utf-8'))
for f in d['facts']:
    print(f"{f['key']} = {f['value']!r} [{f.get('effective_from')}..{f.get('effective_to') or ''}] {f['register_id']}")
print('--- unresolved')
for u in d['unresolved']: print(('B ' if u.get('blocking') else '  ')+u['key'])
if len(sys.argv)>2:
    p=open(f'../../_research/CCG-annex_{st}-research-pack.md',encoding='utf-8').read()
    p=re.sub(r'## 0\.3 Facts emitted.*?(?=\n# )','',p,flags=re.S)
    p=re.sub(r'## ACCESS gaps.*?(?=\n## )','',p,flags=re.S)
    p=re.sub(r'\n## Open questions.*','',p,flags=re.S)
    print(p)
if '--why' in sys.argv:
    for u in d['unresolved']: print('W', u['key'],'::',u.get('why'),'::',u.get('what_would_close_it'))
