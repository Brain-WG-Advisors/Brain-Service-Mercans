# -*- coding: utf-8 -*-
"""Runs every self-check of the SIR build in order and writes checks/run_summary.txt; md5_final.txt is written last.
usage: python run_checks.py [--skip-office]"""
import hashlib
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SIRDIR = os.path.dirname(HERE)
BASE = os.path.dirname(SIRDIR)
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
rc["build"] = run("build (identical rebuild below)", PY + [os.path.join(HERE, "build_sir.py")], 2)
rc["lint"] = run("C12 / C29 / WORD+PATH / FRAC+PCT+UNIT / C30 / C46 period-aware / GAP (sir_lint)", PY + [os.path.join(HERE, "sir_lint.py")], 24)
rc["f44"] = run("F44 self-check", PY + [os.path.join(HERE, "f44_self.py")], 6)
rc["recon"] = run("SIR x RSPEC x DD reconciliation", PY + [os.path.join(HERE, "sir_recon.py")], 4)
rc["c71"] = run("C71 identical rebuild", PY + [os.path.join(HERE, "regen_check_sir.py")], 3)
rc["cc"] = run("shared consistency C42 / C43 / C46 (whole package; rows naming 03-statutory-integrations below)",
               PY + [os.path.join(SH, "consistency-checks", "consistency_checks.py"), "--base", BASE, "--code", "US", "--checks", "C42,C43,C46",
                     "--out", os.path.join(CK, "consistency.json")], 40, cwd=BASE)
rc["c46s"] = run("shared C46, SIR document only", PY + [os.path.join(HERE, "c46_sir.py")], 6)
rc["ct"] = run("shared content C53 / C70", PY + [os.path.join(SH, "content-checks", "content_checks.py"), "--base", BASE, "--code", "US",
                                                  "--checks", "C53,C70", "--out", os.path.join(CK, "content.json")], 4, cwd=BASE)
rc["vc"] = run("validate_contract --all", PY + [os.path.join(SH, "schemas", "validate_contract.py"), "--all", BASE], 3, cwd=BASE)
if "--skip-office" not in sys.argv:
    d = os.path.join(HERE, "_scratch", "openchk")
    os.makedirs(d, exist_ok=True)
    import shutil
    shutil.copy2(os.path.join(SIRDIR, (sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))) or __import__("sir_common").FILENAME)), d)
    rc["open"] = run("Word open check", ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File",
                                         os.path.join(SH, "release", "open_check.ps1"), "-Root", d, "-Json", os.path.join(CK, "open_check.json")], 3)
open(os.path.join(CK, "run_summary.txt"), "w", encoding="utf-8").write("\n".join(lines))
rc["log"] = run("build log", PY + [os.path.join(HERE, "write_buildlog.py")], 2)
# md5 last
files = [os.path.join(SIRDIR, (sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))) or __import__("sir_common").FILENAME)), os.path.join(SIRDIR, "integration-landscape.json")]
files += [os.path.join(HERE, f) for f in sorted(os.listdir(HERE)) if f.endswith(".py")]
files += [os.path.join(CK, f) for f in ("sir_recon.csv", "f44_self.json", "sir_requests.json")]
files += [os.path.join(BASE, "_pipeline", f) for f in ("SIR-bindings.csv", "SIR-build-log.md")]
files += [os.path.join(BASE, "_research", "SIR-research-request.json")]
with open(os.path.join(CK, "md5_final.txt"), "w", encoding="utf-8") as fh:
    for f in files:
        if os.path.exists(f):
            fh.write(f"{hashlib.md5(open(f, 'rb').read()).hexdigest()} *{os.path.relpath(f, BASE).replace(os.sep, '/')}\n")
print("\n".join(lines))
print({k: v for k, v in rc.items()})
