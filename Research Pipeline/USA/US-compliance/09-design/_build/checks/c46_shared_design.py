# -*- coding: utf-8 -*-
"""Shared C46 (and C42/C43/C45) restricted to the design document, so the figure is not mixed with the other artifacts."""
import glob, importlib.util, json, os, sys
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
spec = importlib.util.spec_from_file_location("ccs", os.path.expanduser("~/mercans-pipeline/shared/consistency-checks/consistency_checks.py"))
CCS = importlib.util.module_from_spec(spec); spec.loader.exec_module(CCS)
path = glob.glob(os.path.join(BASE, "09-design", "US_Regulation_Design_v*.md"))[0]
CCS.deliverables = lambda base: [path]
r = CCS.c46(BASE, "US")
out = {k: v for k, v in r.items() if k != "details"}
out["details"] = r.get("details", [])[:40]
json.dump(out, open(os.path.join(HERE, "c46_shared_design.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
sys.stdout.reconfigure(encoding="utf-8")
print({k: v for k, v in out.items() if k != "details"})
for d in out["details"][:12]: print(d)
