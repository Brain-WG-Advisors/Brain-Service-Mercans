# -*- coding: utf-8 -*-
"""Round-3 check battery on the assembled CCG DOCX (artifact-builder, QA r2).

Runs, on 01-ccg/US-CCG-001-v1.0.docx: structure (reopened), md5, C11 and C29 (v2.12 logic copied
verbatim from mercans_pipeline_v2_12.sh c11()/c29(), docx part only), C38, C40, C42/C43/C46 (shared),
C46 period-aware, C69, C70, C37 and validate_contract --all. Word open check is run separately
(open_check.ps1 on a copy). Writes out/checks_r3.json and prints one line per check.

usage: python run_checks_r3.py
"""
import hashlib
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SH = os.path.expanduser("~/mercans-pipeline/shared")
DOCX = os.path.join(BASE, "01-ccg", "US-CCG-001-v1.0.docx")
OUT = os.path.join(HERE, "out")
ENV = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONUTF8="1")
R = {}
sys.stdout.reconfigure(encoding="utf-8")


def run(name, cmd, cwd=BASE):
    p = subprocess.run([sys.executable] + cmd, cwd=cwd, env=ENV, capture_output=True, text=True, encoding="utf-8")
    txt = (p.stdout or "") + (p.stderr or "")
    R[name] = {"rc": p.returncode, "out": txt[-4000:]}
    first = next((ln for ln in txt.splitlines() if ln.strip()), "")
    print(f"[{name}] rc={p.returncode} {first[:200]}")
    return txt


from docx import Document  # noqa: E402

d = Document(DOCX)
md5 = hashlib.md5(open(DOCX, "rb").read()).hexdigest()
styles = [p.style.name for p in d.paragraphs]
R["structure"] = {"md5": md5, "bytes": os.path.getsize(DOCX), "paragraphs": len(d.paragraphs), "tables": len(d.tables),
                  "sections": len(d.sections), "H1": styles.count("Heading 1"), "H2": styles.count("Heading 2"),
                  "H3": styles.count("Heading 3"), "H4": styles.count("Heading 4"),
                  "annex_H1": sum(1 for p in d.paragraphs if p.style.name == "Heading 1" and p.text.startswith("Annex ")),
                  "module_H1": sum(1 for p in d.paragraphs if p.style.name == "Heading 1" and p.text.startswith("Module ")),
                  "toc_field": "TOC" in d.element.body.xml}
vc = d.tables[0]
R["structure"]["version_control"] = [[c.text for c in r.cells] for r in vc.rows]
print("[structure]", json.dumps({k: v for k, v in R["structure"].items() if k != "version_control"}))
print("[version control]", R["structure"]["version_control"])

# ---- C11 (v2.12 c11 logic)
tq = open(os.path.join(SH, "CCG_TEMPLATE_QUESTIONS.md"), encoding="utf-8").read()
h3s = [p.text.strip() for p in d.paragraphs if p.style.name in ("Heading 3", "Heading3")]
qs = [ln.strip()[2:] for ln in tq.split("\n") if ln.strip().startswith("- ") and ("?" in ln or "Deliverable" in ln)]
matched = sum(1 for q in qs if any(q[:30].lower().strip() in h.lower() for h in h3s))
R["C11"] = {"status": "PASS" if matched / max(len(qs), 1) >= 0.95 else "FAIL", "matched": matched, "questions": len(qs),
            "h3": len(h3s)}
print("[C11]", R["C11"])

# ---- C29 (v2.12 c29 logic, docx paragraphs + table cells incl. nested)
HARD_CS = [r'\bTODO\b', r'\bTBD\b', r'\bFIXME\b', r'\bVERIFY\s+No\b', r'RESEARCH-GAP', r'\?\?\?']
HARD_CI = [r'\[\s*placeholder\s*\]', r'\[\s*CHECK\s*\]', r'\[\s*\?\s*\]', r'to be confirmed', r'to be verified', r'lorem ipsum']
BARE = r'(?:PENDING|PLACEHOLDER|TBC|FILL[\s_-]*IN|TO BE COMPLETED)'
BARE_FULL = re.compile(r'^[\s\-\*_.:;,"\'\[\]\(\)]*' + BARE + r'[\s\-\*_.:;,"\'\[\]\(\)]*$', re.IGNORECASE)
XRUN = re.compile(r'X{3,}')
hard, bare, xr, gapc = [], [], [], {}


def scan(t, loc):
    if not t:
        return
    for pat in HARD_CS:
        if re.search(pat, t):
            hard.append((loc, pat, t.strip()[:120]))
    for pat in HARD_CI:
        if re.search(pat, t, re.I):
            hard.append((loc, pat, t.strip()[:120]))
    if BARE_FULL.match(t):
        bare.append((loc, t.strip()[:40]))
    for pat in (r'\bNOT\s+FOUND\b', r'\bNOT\s+AVAILABLE\b'):
        n = len(re.findall(pat, t))
        if n:
            gapc[pat] = gapc.get(pat, 0) + n
    for m in XRUN.finditer(t):
        lo, hi = m.start(), m.end()
        if re.search(r'[.\d]$', t[max(0, lo - 2):lo]) or re.match(r'\s*[.:\d]', t[hi:hi + 2]):
            continue
        xr.append((loc, m.group(0), t.strip()[:120]))


for i, p in enumerate(d.paragraphs):
    scan(p.text, f"para{i}")


def walk(tables, prefix):
    for ti, t in enumerate(tables):
        for ri, row in enumerate(t.rows):
            for ci, cell in enumerate(row.cells):
                scan(cell.text, f"{prefix}tbl{ti}!r{ri}c{ci}")
                if cell.tables:
                    walk(cell.tables, f"{prefix}tbl{ti}.")


walk(d.tables, "")
R["C29"] = {"status": "FAIL" if (hard or bare or xr) else "PASS", "hard": len(hard), "bare": len(bare), "xrun_hard": len(xr),
            "gap_census": gapc, "first": (hard + bare + xr)[:10]}
print("[C29]", {k: v for k, v in R["C29"].items() if k != "first"}, R["C29"]["first"][:3])

# ---- internal paths / pipeline vocabulary left in the deliverable text (QA r2 OH fact path)
alltext = "\n".join(p.text for p in d.paragraphs) + "\n" + "\n".join(
    c.text for t in d.tables for r in t.rows for c in r.cells)
R["internal_paths"] = sorted(set(re.findall(r"00-official-sources/\S+|_research/\S+|01-ccg/\S+|_pipeline/\S+", alltext)))[:20]
R["marker_vocab"] = {w: len(re.findall(w, alltext)) for w in
                     (r"request key", r"research request filed", r"open item `", r"Closes with:", r"To close:",
                      r"Not configured in this release", r"Not yet published")}
print("[internal paths]", R["internal_paths"][:5], "[vocab]", R["marker_vocab"])

# ---- shared checks
run("C38", [os.path.join(SH, "validation-suite-template", "worked_examples_check.py"), DOCX, "--module", "",
            "--json", os.path.join(OUT, "c38.json")])
run("C40", [os.path.join(SH, "research-checks", "research_checks.py"), "--base", BASE, "--code", "US", "--checks", "C40",
            "--out", os.path.join(OUT, "c40.json")])
run("C42/C43/C46 shared", [os.path.join(SH, "consistency-checks", "consistency_checks.py"), "--base", BASE, "--code", "US",
                           "--checks", "C42,C43,C46", "--package-version", "1.0", "--out", os.path.join(OUT, "c42_c46.json")])
run("C46 period-aware", [os.path.join(HERE, "c46_period_aware.py"), "--docx", DOCX, "--json", os.path.join(OUT, "c46_period_aware.json")])
run("C69", [os.path.join(SH, "validation-suite-template", "suite_coverage_check.py"), "--base", BASE, "--code", "US",
            "--json", os.path.join(OUT, "c69.json")])
run("C70", [os.path.join(SH, "content-checks", "content_checks.py"), "--base", BASE, "--code", "US", "--year", "2026",
            "--checks", "C70", "--out", os.path.join(OUT, "c70.json")])
run("C37", [os.path.join(SH, "validation-suite-template", "run_suite.py"), os.path.join(BASE, "_validation"), "--no-engine"])
run("validate_contract --all", [os.path.join(SH, "schemas", "validate_contract.py"), "--all", BASE])
json.dump(R, open(os.path.join(OUT, "checks_r3.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print("md5", md5)
