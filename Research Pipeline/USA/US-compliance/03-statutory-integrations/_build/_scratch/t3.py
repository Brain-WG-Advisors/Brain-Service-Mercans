import sys,os,collections
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.stdout.reconfigure(encoding='utf-8')
import sir_specs as P
bad=0
for s in P.specs():
    cc=collections.Counter(r['channel'] for r in s['rows']); acc=[r['accuracy'] for r in s['rows'] if r['accuracy']]
    nom=[r['row_id'] for r in s['rows'] if r['channel'] is None]
    print(s['id'],len(s['rows']),dict(cc),(min(acc),max(acc)) if acc else None, nom[:3])
