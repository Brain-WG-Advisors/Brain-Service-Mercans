import sys, docx
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.ns import qn

d = docx.Document(sys.argv[1])
out = []
body = d.element.body
for child in body.iterchildren():
    if child.tag == qn('w:p'):
        p = Paragraph(child, d)
        t = p.text.strip()
        if t:
            out.append("[%s] %s" % (p.style.name, t))
    elif child.tag == qn('w:tbl'):
        tb = Table(child, d)
        out.append("[TABLE %dx%d]" % (len(tb.rows), len(tb.columns)))
        for r in tb.rows:
            out.append("  | " + " | ".join(c.text.strip().replace("\n", " ") for c in r.cells))
open(sys.argv[2], "w", encoding="utf-8").write("\n".join(out))
print("wrote", sys.argv[2], len(out), "blocks")
