# -*- coding: utf-8 -*-
import sys, docx
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.ns import qn

def iter_block(parent):
    body = parent.element.body
    for child in body.iterchildren():
        if child.tag == qn('w:p'):
            yield Paragraph(child, parent)
        elif child.tag == qn('w:tbl'):
            yield Table(child, parent)

def cell_txt(c):
    t = " ".join(p.text.strip() for p in c.paragraphs if p.text.strip())
    return t.replace("|", "\|").replace("\n", " ").strip()

def run(path, out):
    d = docx.Document(path)
    lines = []
    for b in iter_block(d):
        if isinstance(b, Paragraph):
            txt = b.text.strip()
            st = (b.style.name or "")
            if not txt:
                continue
            if st.startswith("Heading"):
                try: lvl = int(st.split()[-1])
                except: lvl = 1
                lines.append("\n" + "#"*(lvl+1) + " " + txt + "\n")
            elif st.startswith("List"):
                lines.append("- " + txt)
            elif st == "Title":
                lines.append("\n# " + txt + "\n")
            else:
                lines.append(txt)
        else:
            rows = b.rows
            if not rows: continue
            ncol = max(len(r.cells) for r in rows)
            lines.append("")
            for i, r in enumerate(rows):
                cells = [cell_txt(c) for c in r.cells]
                cells += [""]*(ncol-len(cells))
                lines.append("| " + " | ".join(cells) + " |")
                if i == 0:
                    lines.append("|" + "---|"*ncol)
            lines.append("")
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(out, len("\n".join(lines)))

run(sys.argv[1], sys.argv[2])
