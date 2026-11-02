import json,sys,re
sys.stdout.reconfigure(encoding='utf-8')
d=json.load(open(sys.argv[1],encoding='utf-8'))
cl=open(sys.argv[2],encoding='utf-8').read()
diff=set(f"{c['sheet']}!{c['cell']}" for c in d['cells'])
# find Sheet!Cell mentions in changelog
sheets=set(c['sheet'] for c in d['cells'])|set(d['sheets_draft'])
ment=set()
for s in sorted(d['sheets_draft'],key=len,reverse=True):
    for m in re.finditer(re.escape(s)+r'!([A-Z]{1,3}\d+(?::[A-Z]{1,3}\d+)?)',cl):
        ment.add(f"{s}!{m.group(1)}")
print('diff cells not mentioned in changelog:',sorted(diff-ment))
print('mentioned but not in diff:',sorted(m for m in ment-diff if ':' not in m)[:60])
