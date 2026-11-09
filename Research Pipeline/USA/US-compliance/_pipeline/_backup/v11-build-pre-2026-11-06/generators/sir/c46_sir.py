# -*- coding: utf-8 -*-
"""Shared consistency C46 (v2.12: every tag equals the facts; a distinctive fact value without a tag is a FAIL) restricted to
the SIR document, so that the verdict of this deliverable is not mixed with findings in other deliverables."""
import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(os.path.dirname(HERE))
spec = importlib.util.spec_from_file_location("ccs", os.path.expanduser("~/mercans-pipeline/shared/consistency-checks/consistency_checks.py"))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
sir = os.path.join(BASE, "03-statutory-integrations", "US-SIR-INDEX-001-v1.0.docx")
m.deliverables = lambda base: [sir]
r = m.c46(BASE, "US")
print("C46 (SIR only):", r["status"], {k: v for k, v in r.items() if not isinstance(v, (list, dict)) and k != "status"})
for x in r.get("details", [])[:10]:
    print(" ", x)
sys.exit(0 if r["status"] == "PASS" else 1)
