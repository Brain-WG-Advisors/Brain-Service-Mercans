# -*- coding: utf-8 -*-
"""Shared consistency C46 (v2.12) restricted to the payslip workbook, so that the verdict of this deliverable is not mixed
with findings in other deliverables."""
import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(os.path.dirname(HERE))
spec = importlib.util.spec_from_file_location("ccs", os.path.expanduser("~/mercans-pipeline/shared/consistency-checks/consistency_checks.py"))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
psl = os.path.join(BASE, "06-payslip", "US_Compliance_Payslip_Generator.xlsx")
m.deliverables = lambda base: [psl]
r = m.c46(BASE, "US")
print("C46 (PSL only):", r["status"], {k: v for k, v in r.items() if not isinstance(v, (list, dict)) and k != "status"})
for x in r.get("details", [])[:12]:
    print(" ", x)
sys.exit(0 if r["status"] == "PASS" else 1)
