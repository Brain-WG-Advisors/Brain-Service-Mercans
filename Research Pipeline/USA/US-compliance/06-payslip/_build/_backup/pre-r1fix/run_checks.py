# -*- coding: utf-8 -*-
"""Runs every self-check of the PSL build in order and writes checks/run_summary.txt; md5_final.txt is written last.
usage: python run_checks.py [--skip-office] [--skip-content]"""
import hashlib
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PSLDIR = os.path.dirname(HERE)
BASE = os.path.dirname(PSLDIR)
CK = os.path.join(HERE, "checks")
SH = os.path.expanduser("~/mercans-pipeline/shared")
PY = [sys.executable, "-I"]
env = dict(os.environ, PYTHONIOENCODING="utf-8")
lines = []


def run(label, cmd, tail=14, cwd=None):
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", env=env, cwd=cwd)
    out = (r.stdout + r.stderr).strip().splitlines()
    lines.append(f"## {label} (exit {r.returncode})")
    lines.extend(out[-tail:])
    lines.append("")
    return r.returncode


rc = {}
rc["build"] = run("build", PY + [os.path.join(HERE, "build_psl.py")], 4)
rc["lint"] = run("C12 / C29 / WORD+PATH / FRAC+PCT+UNIT / C30 / C46 period-aware / GAP (psl_lint)", PY + [os.path.join(HERE, "psl_lint.py")], 30)
rc["f44"] = run("f44_self", PY + [os.path.join(HERE, "f44_self.py")], 6)
rc["recon"] = run("recon (payslip lines x WTC x DD; PSL facts placed)", PY + [os.path.join(HERE, "psl_recon_check.py")], 6)
rc["c71"] = run("C71 identical rebuild", PY + [os.path.join(HERE, "regen_check_psl.py")], 3)
rc["cc"] = run("shared consistency C42 / C43 (whole package)", PY + [os.path.join(SH, "consistency-checks", "consistency_checks.py"), "--base", BASE, "--code", "US",
                                                                    "--checks", "C42,C43", "--out", os.path.join(CK, "consistency.json")], 8, cwd=BASE)
rc["c46"] = run("shared C46 on the payslip workbook alone (not period-aware: known limit, see build log)", PY + [os.path.join(HERE, "c46_psl.py")], 8)
if "--skip-content" not in sys.argv:
    rc["ct"] = run("shared content C49 / C57 / C70", PY + [os.path.join(SH, "content-checks", "content_checks.py"), "--base", BASE, "--code", "US",
                                                           "--checks", "C49,C57,C70", "--out", os.path.join(CK, "content.json")], 10, cwd=BASE)
rc["vc"] = run("validate_contract --all", PY + [os.path.join(SH, "schemas", "validate_contract.py"), "--all", BASE], 3, cwd=BASE)
if "--skip-office" not in sys.argv:
    d = os.path.join(HERE, "_scratch", "openchk")
    shutil.rmtree(d, ignore_errors=True)
    os.makedirs(d, exist_ok=True)
    shutil.copy2(os.path.join(PSLDIR, "US_Compliance_Payslip_Generator.xlsx"), d)
    rc["open"] = run("Excel open check", ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File",
                                          os.path.join(SH, "release", "open_check.ps1"), "-Root", d, "-Json", os.path.join(CK, "open_check.json")], 3)
open(os.path.join(CK, "run_summary.txt"), "w", encoding="utf-8").write("\n".join(lines))
rc["log"] = run("build log", PY + [os.path.join(HERE, "write_buildlog.py")], 2)
files = [os.path.join(PSLDIR, "US_Compliance_Payslip_Generator.xlsx")]
files += [os.path.join(HERE, f) for f in sorted(os.listdir(HERE)) if f.endswith(".py")]
files += [os.path.join(CK, f) for f in ("psl_recon.csv", "f44_self.json", "psl_requests.json", "run_summary.txt")]
files += [os.path.join(BASE, "_pipeline", f) for f in ("PSL-bindings.csv", "PSL-build-log.md")]
files += [os.path.join(BASE, "_research", f) for f in ("PSL-research-request.json", "PSL-legal-items.json")]
with open(os.path.join(CK, "md5_final.txt"), "w", encoding="utf-8") as fh:
    for f in files:
        if os.path.exists(f):
            fh.write(f"{hashlib.md5(open(f, 'rb').read()).hexdigest()} *{os.path.relpath(f, BASE).replace(os.sep, '/')}\n")
print("\n".join(lines))
print({k: v for k, v in rc.items()})
