# Diff linha a linha entre resultados do oraculo v1 e v2 (rodada 4). Uso: python -I diff_v1_v2r4.py <v1.json> <v2.json>
import json, sys
sys.stdout.reconfigure(encoding="utf-8")
a = {x["id"]: x for x in json.load(open(sys.argv[1], encoding="utf-8"))["results"]}
b = {x["id"]: x for x in json.load(open(sys.argv[2], encoding="utf-8"))["results"]}
nch = 0
for k in a:
    la, lb = a[k].get("lines", {}), b[k].get("lines", {})
    d = []
    for key in sorted(set(la) | set(lb)):
        if la.get(key) != lb.get(key):
            d.append((key, la.get(key), lb.get(key)))
    if d:
        nch += 1
        print(k, a[k]["name"])
        for x in d: print("   ", x)
print("casos", len(a), "com mudanca", nch)
