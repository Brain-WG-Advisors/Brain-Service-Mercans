import glob, os, re, sys, json, collections, docx
from openpyxl import load_workbook
sys.stdout.reconfigure(encoding="utf-8")
R = "10-release"
PAT = {"review_id": r"\b(?:QA[0-9]?-?\d{2}|r[1-9][a-e]?\b(?= (?:fix|finding|review))|[A-Z]{2,5}-QA\d-\d+|review-r\d)",
       "corrected_stamp": r"\bCorrected (?:on )?20\d\d", "now_reads": r"\bnow reads\b", "was_colon": r"\bwas:", "changelog": r"\b(?:changelog|change log|Round \d|round \d fix|regenerated|rebuilt|re-sync|resync)\b",
       "fact_tag": r"\[\[FACT:", "pipeline": r"\b(?:orchestrator|agent 2|source hunter|builder|auditor|precheck|wayback|_research/|_pipeline/)\b",
       "rule_hits": r"reissued formula|later amendment not checked|pre-amendment amount|the reissued formula"}
hits = collections.defaultdict(list); opened = 0; fails = []
def scan(t, loc):
    for k, p in PAT.items():
        for m in re.finditer(p, t or "", re.I if k not in ("review_id",) else 0):
            hits[k].append((loc, (t[max(0, m.start()-70): m.end()+70]).replace("\n", " ")))
for p in sorted(glob.glob(R + "/0*/**/*.*", recursive=True)):
    try:
        if p.endswith(".docx"):
            d = docx.Document(p); opened += 1
            for i, x in enumerate(d.paragraphs): scan(x.text, f"{p} p{i}")
            for ti, t in enumerate(d.tables):
                for ri, r in enumerate(t.rows):
                    for c in r.cells: scan(c.text, f"{p} t{ti}r{ri}")
        elif p.endswith(".xlsx"):
            wb = load_workbook(p, read_only=True); opened += 1
            for ws in wb.worksheets:
                for row in ws.iter_rows():
                    for c in row:
                        if isinstance(c.value, str): scan(c.value, f"{p}!{ws.title}!{c.coordinate}")
        elif p.endswith(".md"):
            for i, l in enumerate(open(p, encoding="utf-8")): scan(l, f"{p}:{i+1}")
    except Exception as e:
        fails.append((p, str(e)[:100]))
print("opened docx/xlsx", opened, "fails", fails)
for k, v in hits.items():
    print(f"== {k}: {len(v)}")
    print("   words", collections.Counter(re.search(PAT[k], c, re.I).group(0).lower() for _, c in v).most_common(8))
    for loc, ctx in v[:4]: print("   ", loc[-70:], "|", ctx[:200])
