# Period-aware C46 over every deliverable of the package (uses the CCG period-aware checker's run()).
import importlib.util, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); BASE = os.path.abspath(os.path.join(HERE, "..", ".."))
p = os.path.join(BASE, "01-ccg", "_build", "common", "c46_period_aware.py")
sp = importlib.util.spec_from_file_location("c46pa", p); m = importlib.util.module_from_spec(sp); sys.argv = [p]; sp.loader.exec_module(m)
paths = m.CCS.deliverables(BASE)
r = m.run(paths)
json.dump(r, open(os.path.join(HERE, "out", "c46_period_pkg.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print("deliverables", len(paths)); print(json.dumps({k: v for k, v in r.items() if k != "detail"}))
