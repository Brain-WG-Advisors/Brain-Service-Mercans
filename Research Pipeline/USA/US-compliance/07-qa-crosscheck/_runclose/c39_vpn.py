import re, sys, html
sys.stdout.reconfigure(encoding="utf-8")
D = "00-official-sources/ccg-sources/_test0-opera-2026-11-05/"
def txt(f):
    if f.endswith(".pdf"):
        from pypdf import PdfReader
        t = " ".join((p.extract_text() or "") for p in PdfReader(D + f).pages)
    else:
        t = re.sub(r"<[^>]+>", " ", open(D + f, encoding="utf-8", errors="ignore").read()); t = html.unescape(t)
    return re.sub(r"\s+", " ", t)
def show(f, pats):
    t = txt(f); print("==", f, len(t))
    for p in pats:
        m = [x.group(0) for x in re.finditer(p, t, re.I)][:2]
        print("  ", p, "->", m if m else "NOT FOUND")
show("IN-DOR-rates.html", [r".{0,40}adjusted gross income tax rate for 2026.{0,40}"])
show("NC-GS105-153.7.html", [r".{0,60}After 2025.{0,30}", r"Taxable Years Beginning.{0,40}"])
show("KY-KRS141.020.pdf", [r".{0,80}January 1, 2026.{0,120}"])
show("TX-C42.html", [r".{0,20}Form C-42 is used to authorize.{0,80}", r"Written Authorization to Represent.{0,40}"])
show("OR-ORS657.html", [r"657\.095.{0,700}", r".{0,200}work performed in other states.{0,300}"])
