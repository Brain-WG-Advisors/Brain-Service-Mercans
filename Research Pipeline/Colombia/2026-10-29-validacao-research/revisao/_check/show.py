import json,sys
sys.stdout.reconfigure(encoding='utf-8')
d=json.load(open(sys.argv[1],encoding='utf-8'))
mode=sys.argv[2] if len(sys.argv)>2 else 'all'
L=int(sys.argv[3]) if len(sys.argv)>3 else 100000
for c in d['cells']:
    if mode=='old' and c['old'] is None: continue
    if mode=='new' and c['old'] is not None: continue
    print(f"[{c['sheet']}!{c['cell']}] fill={c['fill']}\n  OLD: {str(c['old'])[:L]}\n  NEW: {str(c['new'])[:L]}")
