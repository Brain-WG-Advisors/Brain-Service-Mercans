import sys,os,re
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.stdout.reconfigure(encoding='utf-8')
import sir_specs as P
seen=set()
for s in P.specs():
    for r in s['rows']:
        if r['channel'] is None and not r['acc_text'].startswith('No return'):
            print(r['row_id'],'||',r['acc_text'][:700],'\n')
