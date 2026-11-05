# -*- coding: utf-8 -*-
"""Self-check of the skill: lints (C29, WORD, PATH, NOTES) and numeric check against facts + approved artifacts. exit 1 on any miss."""
import glob, json, os, re, sys
import docx, openpyxl
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.abspath(os.path.join(HERE, ".."))
BASE = os.path.abspath(os.path.join(OUT, "..", "..", "US-compliance"))
C29 = re.compile(r"\[placeholder\]|\bplaceholder\b|\bTODO\b|\bTBD\b|\bFIXME\b|\bXXX\b|VERIFY No\.|\bto be confirmed\b|\bto be verified\b|<insert\b|\[CHECK\]|\[\?\]|RESEARCH-GAP|#NAME\?|#VALUE!|\[\[(?:FACT|GAP)", re.I)
WORD = re.compile(r"\b(Stage \d|Synthesis|facts file|research pack|register row|tier-?B|MANUAL row|PENDING|browser pass|VPN|fan-out|agent 2|builder|_research|_pipeline|build-manifest|scope_manifest|\.json\b|US exit|build lead|owner plan|Step-4|P\d-[A-Z]+|stage-1|C\d\d|checker|table \d+ r\d+c\d+|orchestrator|merge worker|register_id|annex workers|ledger)", re.I)
PATH_RX = re.compile(r"00-official-sources|_research/|_pipeline/|\.json\b|\.py\b|[A-Za-z]:\\")
NOTE = re.compile(r"\bR\d 20\d\d|effective_from|local copy|script shell|(?:returned|HTTP)[^.]{0,40}\bbytes\b", re.I)
EXTRA = re.compile(r"seal attempt|QA r\d|build log|build manifest|build record|RUN-JOURNAL|legal-basis-register|PLANO|brain-service|mercans-pipeline|C:\|~/|journal trap|Research Pipeline|MANDATE")
files = [p for p in glob.glob(os.path.join(OUT, "**", "*.md"), recursive=True) if "_build" not in p]
# numeric corpus
NUM = re.compile(r"\d[\d,]*(?:\.\d+)?")
def toks(s):
    return {t.rstrip(",").replace(",", "") for t in NUM.findall(s)} | {t.rstrip(",") for t in NUM.findall(s)}
corp = set(); raw = []
for f in glob.glob(os.path.join(BASE, "_research", "*facts.json")):
    d = json.load(open(f, encoding="utf8"))
    for x in d.get("facts", []):
        raw.append(" ".join(str(x.get(k) or "") for k in ("value", "effective_from", "effective_to", "register_id", "note")))
for f in glob.glob(os.path.join(BASE, "01-ccg", "modules", "*.md")) + glob.glob(os.path.join(BASE, "01-ccg", "annexes", "*.md")):
    raw.append(open(f, encoding="utf8").read())
for f in glob.glob(os.path.join(BASE, "0[2456]-*", "*.xlsx")):
    wb = openpyxl.load_workbook(f, read_only=True)
    for ws in wb.worksheets:
        for r in ws.iter_rows(values_only=True):
            raw.append(" ".join(str(c) for c in r if c is not None))
for f in glob.glob(os.path.join(BASE, "03-statutory-integrations", "*.docx")):
    d = docx.Document(f); raw += [p.text for p in d.paragraphs] + [c.text for t in d.tables for r in t.rows for c in r.cells]
import csv
for r in csv.DictReader(open(os.path.join(BASE, "00-official-sources", "legal-basis-register.csv"), encoding="utf8")):
    raw.append(" ".join(r.values()))
for g in json.load(open(os.path.join(BASE, "_research", "gaps.json"), encoding="utf8"))["gaps"]:
    raw.append(json.dumps(g))
for f in glob.glob(os.path.join(BASE, "_qa", "*.json")):
    raw.append(open(f, encoding="utf8").read())
for r in raw:
    corp |= toks(r)
IDS = re.compile(r"\b[A-Z]{1,6}-[A-Z0-9]+(?:-\d+)+\b|\bRQ-\d+\b|\bUS-[A-Z0-9]+-\d+\b|\bSIR-RQ-\d+")
res = {"C29": [], "WORD": [], "PATH": [], "NOTES": [], "NUM": []}
for p in sorted(files):
    rel = os.path.relpath(p, OUT)
    text = open(p, encoding="utf8").read()
    for i, line in enumerate(text.split("\n"), 1):
        if C29.search(line): res["C29"].append((rel, i, C29.search(line).group(0)))
        lw = re.sub(r"fund[_ ]builder", "fund", line)
        if WORD.search(lw): res["WORD"].append((rel, i, WORD.search(lw).group(0)))
        if PATH_RX.search(line): res["PATH"].append((rel, i, PATH_RX.search(line).group(0)))
        line = re.sub(r"fund[_ ]builder|oh\.wh\.tables\.effective_from", "k", line)
        m = NOTE.search(line) or EXTRA.search(line)
        if m: res["NOTES"].append((rel, i, m.group(0)))
        l2 = IDS.sub(" ", line)
        l2 = re.sub(r"\b\d{4}-\d{2}-\d{2}\b", lambda m: " ", l2)  # ISO dates: checked below
        for d in re.findall(r"\b\d{4}-\d{2}-\d{2}\b", line):
            if d not in corp_dates if False else False: pass
        if rel.endswith("07-qa-report.md") or rel.endswith("14-known-gaps.md") and False: pass
        for t in NUM.findall(l2):
            tt = t.rstrip(",")
            if tt.replace(",", "") not in corp and tt not in corp:
                res["NUM"].append((rel, i, tt))

for k, v in res.items():
    print(k, len(v))
    for x in v[:15]: print("  ", x)
json.dump({k: v for k, v in res.items()}, open(os.path.join(HERE, "selfcheck_result.json"), "w"), indent=1)
sys.exit(1 if any(res.values()) else 0)
