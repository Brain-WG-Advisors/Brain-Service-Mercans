#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CO-CCG-001 v1.0 builder — assembles the 13 Colombia CCG module markdown files
into the official Mercans v2.4 Word format.

Arial 11pt body, 14pt H1, 12pt H2, 11pt H3 (bold). Title page, TOC field on
page 2, page breaks between modules, footer on every page.
"""
import os
import re
import glob

from docx import Document
from docx.shared import Pt, Inches, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

BASE = os.path.dirname(os.path.abspath(__file__))
MODULES = os.path.join(BASE, "modules")
OUT = os.path.join(BASE, "CO-CCG-001-v1.0.docx")
LOGO = os.path.expanduser("~/mercans-pipeline/shared/mercans_logo.png")

FOOTER_TEXT = "CO-CCG-001 v1.0 | Mercans Compliance Regulations Team | 2026"
TITLE = "Colombia Country Configuration Guide \u2014 CO-CCG-001 v1.0"

ORDER = [
    "m01_foundational.md",
    "m02_master_data.md",
    "m03_g2n.md",
    "m04_compensation.md",
    "m05_social_security.md",
    "m06_tax.md",
    "m07_deductions.md",
    "m08_leave.md",
    "m09_termination.md",
    "m10_reporting.md",
    "m11_advanced.md",
    "m12_examples.md",
    "m13_practices.md",
]


# ---------------------------------------------------------------- styling ---
def setup_styles(doc):
    normal = doc.styles["Normal"]
    normal.font.name = "Arial"
    normal.font.size = Pt(11)
    rpr = normal.element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.append(rfonts)
    for a in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(a), "Arial")
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.line_spacing = 1.15

    specs = {
        "Heading 1": (14, True, RGBColor(0x1F, 0x38, 0x64), 18, 10),
        "Heading 2": (12, True, RGBColor(0x2E, 0x5C, 0x9A), 14, 6),
        "Heading 3": (11, True, RGBColor(0x00, 0x00, 0x00), 10, 4),
        "Heading 4": (11, True, RGBColor(0x40, 0x40, 0x40), 8, 4),
    }
    for name, (size, bold, colour, before, after) in specs.items():
        st = doc.styles[name]
        st.font.name = "Arial"
        st.font.size = Pt(size)
        st.font.bold = bold
        st.font.color.rgb = colour
        st.paragraph_format.space_before = Pt(before)
        st.paragraph_format.space_after = Pt(after)
        st.paragraph_format.keep_with_next = True
        rpr = st.element.get_or_add_rPr()
        rfonts = rpr.find(qn("w:rFonts"))
        if rfonts is None:
            rfonts = OxmlElement("w:rFonts")
            rpr.append(rfonts)
        for a in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
            rfonts.set(qn(a), "Arial")


def add_footer(doc):
    for section in doc.sections:
        footer = section.footer
        p = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
        p.text = ""
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(FOOTER_TEXT)
        run.font.name = "Arial"
        run.font.size = Pt(8)
        run.font.color.rgb = RGBColor(0x60, 0x60, 0x60)


def add_toc_field(paragraph):
    r = paragraph.add_run()
    fld_begin = OxmlElement("w:fldChar")
    fld_begin.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = r'TOC \o "1-3" \h \z \u'
    fld_sep = OxmlElement("w:fldChar")
    fld_sep.set(qn("w:fldCharType"), "separate")
    placeholder = OxmlElement("w:t")
    placeholder.text = "Right-click and select \u201cUpdate Field\u201d to build the table of contents."
    fld_end = OxmlElement("w:fldChar")
    fld_end.set(qn("w:fldCharType"), "end")
    for el in (fld_begin, instr, fld_sep, placeholder, fld_end):
        r._r.append(el)


# ------------------------------------------------------------ inline text ---
INLINE = re.compile(r"(\*\*.+?\*\*|\*[^*]+?\*|`[^`]+?`)", re.S)


def add_inline(paragraph, text):
    """Render **bold**, *italic* and `code` inside a paragraph."""
    text = text.replace("\u00a0", " ")
    for part in INLINE.split(text):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**") and len(part) > 4:
            run = paragraph.add_run(part[2:-2])
            run.bold = True
        elif part.startswith("*") and part.endswith("*") and len(part) > 2:
            run = paragraph.add_run(part[1:-1])
            run.italic = True
        elif part.startswith("`") and part.endswith("`") and len(part) > 2:
            run = paragraph.add_run(part[1:-1])
            run.font.name = "Consolas"
            run.font.size = Pt(9)
        else:
            run = paragraph.add_run(part)
        run.font.name = run.font.name or "Arial"


def strip_md(text):
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text, flags=re.S)
    text = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"\1", text)
    text = text.replace("`", "")
    return text.strip()


# ----------------------------------------------------------------- tables ---
def split_row(line):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c.strip() for c in line.split("|")]


def is_sep(line):
    return bool(re.match(r"^\s*\|?[\s:\-|]+\|[\s:\-|]*$", line)) and "-" in line


def add_table(doc, rows):
    header, body = rows[0], rows[1:]
    ncols = max(len(r) for r in rows)
    table = doc.add_table(rows=0, cols=ncols)
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = True

    hr = table.add_row()
    for i in range(ncols):
        cell = hr.cells[i]
        cell.text = ""
        p = cell.paragraphs[0]
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.space_before = Pt(2)
        add_inline(p, header[i] if i < len(header) else "")
        for run in p.runs:
            run.bold = True
            run.font.size = Pt(9)
            run.font.name = "Arial"
        shd = OxmlElement("w:shd")
        shd.set(qn("w:val"), "clear")
        shd.set(qn("w:fill"), "DCE6F1")
        cell._tc.get_or_add_tcPr().append(shd)

    for row in body:
        tr = table.add_row()
        for i in range(ncols):
            cell = tr.cells[i]
            cell.text = ""
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.space_before = Pt(2)
            add_inline(p, row[i] if i < len(row) else "")
            for run in p.runs:
                run.font.size = Pt(9)
                run.font.name = "Arial"
    doc.add_paragraph()


# ------------------------------------------------------------ md renderer ---
def render(doc, md):
    lines = md.split("\n")
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        stripped = line.strip()

        # fenced code block
        if stripped.startswith("```"):
            i += 1
            buf = []
            while i < n and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.2)
            p.paragraph_format.space_after = Pt(8)
            p.paragraph_format.space_before = Pt(4)
            run = p.add_run("\n".join(buf))
            run.font.name = "Consolas"
            run.font.size = Pt(8.5)
            pPr = p._p.get_or_add_pPr()
            shd = OxmlElement("w:shd")
            shd.set(qn("w:val"), "clear")
            shd.set(qn("w:fill"), "F2F2F2")
            pPr.append(shd)
            continue

        # table
        if stripped.startswith("|") and i + 1 < n and is_sep(lines[i + 1]):
            rows = [split_row(stripped)]
            i += 2
            while i < n and lines[i].strip().startswith("|"):
                if not is_sep(lines[i]):
                    rows.append(split_row(lines[i]))
                i += 1
            add_table(doc, rows)
            continue

        # headings
        m = re.match(r"^(#{1,4})\s+(.*)$", stripped)
        if m:
            level = len(m.group(1))
            text = m.group(2).strip()
            if level == 1:
                if doc.paragraphs and any(p.text.strip() for p in doc.paragraphs[-3:]):
                    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
                h = doc.add_heading(level=1)
            else:
                h = doc.add_heading(level=level)
            add_inline(h, text)
            for run in h.runs:
                run.font.name = "Arial"
            i += 1
            continue

        # blockquote
        if stripped.startswith(">"):
            buf = []
            while i < n and lines[i].strip().startswith(">"):
                buf.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            # a blockquote may itself contain a table
            j = 0
            while j < len(buf):
                bl = buf[j].strip()
                if bl.startswith("|") and j + 1 < len(buf) and is_sep(buf[j + 1]):
                    rows = [split_row(bl)]
                    j += 2
                    while j < len(buf) and buf[j].strip().startswith("|"):
                        if not is_sep(buf[j]):
                            rows.append(split_row(buf[j]))
                        j += 1
                    add_table(doc, rows)
                    continue
                para = []
                while j < len(buf) and buf[j].strip() and not buf[j].strip().startswith("|"):
                    para.append(buf[j].strip())
                    j += 1
                if para:
                    p = doc.add_paragraph()
                    p.paragraph_format.left_indent = Inches(0.3)
                    p.paragraph_format.space_before = Pt(4)
                    p.paragraph_format.space_after = Pt(4)
                    add_inline(p, " ".join(para))
                    for run in p.runs:
                        run.font.size = Pt(10)
                        run.font.name = "Arial"
                    pPr = p._p.get_or_add_pPr()
                    shd = OxmlElement("w:shd")
                    shd.set(qn("w:val"), "clear")
                    shd.set(qn("w:fill"), "FFF7E6")
                    pPr.append(shd)
                else:
                    j += 1
            continue

        # horizontal rule
        if re.match(r"^\s*---+\s*$", line):
            i += 1
            continue

        # bullet list
        if re.match(r"^\s*[-*+]\s+", line):
            indent = len(line) - len(line.lstrip())
            p = doc.add_paragraph(style="List Bullet")
            p.paragraph_format.left_indent = Inches(0.25 + 0.25 * (indent // 2))
            p.paragraph_format.space_after = Pt(2)
            add_inline(p, re.sub(r"^\s*[-*+]\s+", "", line))
            for run in p.runs:
                run.font.name = "Arial"
            i += 1
            continue

        # numbered list
        if re.match(r"^\s*\d+\.\s+", line):
            indent = len(line) - len(line.lstrip())
            p = doc.add_paragraph(style="List Number")
            p.paragraph_format.left_indent = Inches(0.25 + 0.25 * (indent // 2))
            p.paragraph_format.space_after = Pt(2)
            add_inline(p, re.sub(r"^\s*\d+\.\s+", "", line))
            for run in p.runs:
                run.font.name = "Arial"
            i += 1
            continue

        # blank
        if not stripped:
            i += 1
            continue

        # paragraph (join soft-wrapped lines)
        buf = []
        while i < n:
            cur = lines[i]
            cs = cur.strip()
            if (not cs or cs.startswith("|") or cs.startswith("#") or cs.startswith(">")
                    or cs.startswith("```") or re.match(r"^\s*[-*+]\s+", cur)
                    or re.match(r"^\s*\d+\.\s+", cur) or re.match(r"^\s*---+\s*$", cur)):
                break
            buf.append(cs)
            i += 1
        text = " ".join(buf)
        p = doc.add_paragraph()
        if text.startswith("*Legal basis:") or text.startswith("*Source:"):
            p.paragraph_format.space_before = Pt(8)
            add_inline(p, text)
            for run in p.runs:
                run.italic = True
                run.font.size = Pt(9)
                run.font.color.rgb = RGBColor(0x44, 0x44, 0x44)
                run.font.name = "Arial"
        else:
            add_inline(p, text)
            for run in p.runs:
                run.font.name = "Arial"


# ------------------------------------------------------------- title page ---
def title_page(doc):
    for _ in range(3):
        doc.add_paragraph()
    if os.path.exists(LOGO):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        try:
            p.add_run().add_picture(LOGO, width=Cm(5.0))
        except Exception:
            pass
    doc.add_paragraph()

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("Colombia")
    r.font.name = "Arial"
    r.font.size = Pt(30)
    r.bold = True
    r.font.color.rgb = RGBColor(0x1F, 0x38, 0x64)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("Country Configuration Guide")
    r.font.name = "Arial"
    r.font.size = Pt(20)
    r.bold = True
    r.font.color.rgb = RGBColor(0x2E, 0x5C, 0x9A)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("CO-CCG-001  \u00b7  Version 1.0  \u00b7  Fiscal Year 2026")
    r.font.name = "Arial"
    r.font.size = Pt(13)

    doc.add_paragraph()
    meta = [
        ("Country", "Colombia (CO)"),
        ("Currency", "Colombian peso \u2014 COP (ISO 4217: COP)"),
        ("Fiscal year", "1 January \u2013 31 December 2026"),
        ("Minimum monthly wage 2026", "COP 1,750,905"),
        ("Tax unit (UVT) 2026", "COP 52,374"),
        ("Scope", "Private-sector employees under the Substantive Labour Code"),
        ("Authorities", "DIAN \u00b7 UGPP \u00b7 Ministry of Labour \u00b7 Ministry of Health and Social Protection"),
        ("Document", "CO-CCG-001 v1.0"),
        ("Prepared by", "Mercans Compliance Regulations Team"),
        ("Date", "September 2026"),
    ]
    t = doc.add_table(rows=0, cols=2)
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for k, v in meta:
        row = t.add_row()
        c0, c1 = row.cells
        c0.text = ""
        c1.text = ""
        r0 = c0.paragraphs[0].add_run(k)
        r0.bold = True
        r0.font.size = Pt(10)
        r0.font.name = "Arial"
        r1 = c1.paragraphs[0].add_run(v)
        r1.font.size = Pt(10)
        r1.font.name = "Arial"
        shd = OxmlElement("w:shd")
        shd.set(qn("w:val"), "clear")
        shd.set(qn("w:fill"), "F2F5FA")
        c0._tc.get_or_add_tcPr().append(shd)

    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)

    h = doc.add_paragraph()
    r = h.add_run("Table of Contents")
    r.bold = True
    r.font.size = Pt(14)
    r.font.name = "Arial"
    r.font.color.rgb = RGBColor(0x1F, 0x38, 0x64)
    add_toc_field(doc.add_paragraph())
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)

    # version control
    h = doc.add_heading(level=1)
    add_inline(h, "Version Control")
    t = doc.add_table(rows=0, cols=4)
    t.style = "Table Grid"
    hdr = ["Version", "Date", "Author", "Change"]
    row = t.add_row()
    for i, v in enumerate(hdr):
        cell = row.cells[i]
        cell.text = ""
        rr = cell.paragraphs[0].add_run(v)
        rr.bold = True
        rr.font.size = Pt(9)
        rr.font.name = "Arial"
        shd = OxmlElement("w:shd")
        shd.set(qn("w:val"), "clear")
        shd.set(qn("w:fill"), "DCE6F1")
        cell._tc.get_or_add_tcPr().append(shd)
    revisions = [
        ["1.0", "3 September 2026", "Mercans Compliance Regulations Team",
         "Initial build for fiscal year 2026 \u2014 13 modules, v2.4 template format"],
        ["1.0 rev A", "4 September 2026", "Mercans Compliance Regulations Team",
         "Compliance pass. (1) English-only prose: 85 quoted statutory passages rendered into "
         "English translation, the article citation retained as the traceability anchor "
         "(control B10). (2) Newest-law check added at Module 5.1: Law 2381 of 2024, the pension "
         "reform, recorded as suspended by Constitutional Court Auto 841 of 18 June 2025 and "
         "deferred to 1 April 2027 by Judgment C-264 of 25 August 2026 \u2014 confirming Law 100 of "
         "1993 as amended by Law 797 of 2003 as the operative FY2026 basis, with the FY2026-to-2027 "
         "delta tabulated for change control. No FY2026 rate, base or ceiling changed."],
    ]
    for vals in revisions:
        row = t.add_row()
        for i, v in enumerate(vals):
            cell = row.cells[i]
            cell.text = ""
            rr = cell.paragraphs[0].add_run(v)
            rr.font.size = Pt(9)
            rr.font.name = "Arial"
    doc.add_paragraph()

    p = doc.add_paragraph()
    add_inline(p, "**Currency of the content.** Every rate, threshold and deadline in this guide was "
                  "verified against the primary source cited, for fiscal year 2026. Where an item rests on "
                  "administrative doctrine rather than statute, or where a primary source could not be "
                  "retrieved, that is stated inline. Two items carry live legal risk and are flagged where "
                  "they arise: the 2026 minimum-wage decree remains subject to a pending annulment action on "
                  "the merits (Module 4.1), and the pension reform of Law 2381 of 2024 takes effect on "
                  "1 April 2027, outside this guide's fiscal year (Module 5).")
    for run in p.runs:
        run.font.size = Pt(10)
        run.font.name = "Arial"


# ------------------------------------------------------------------ main ----
def main():
    doc = Document()
    setup_styles(doc)
    for s in doc.sections:
        s.top_margin = Cm(2.0)
        s.bottom_margin = Cm(2.0)
        s.left_margin = Cm(2.0)
        s.right_margin = Cm(2.0)
    add_footer(doc)
    title_page(doc)

    for fname in ORDER:
        path = os.path.join(MODULES, fname)
        with open(path, encoding="utf-8") as fh:
            md = fh.read()
        render(doc, md)

    doc.save(OUT)

    # self-check
    d = Document(OUT)
    h1 = [p.text for p in d.paragraphs if p.style.name in ("Heading 1", "Heading1")]
    h2 = [p.text for p in d.paragraphs if p.style.name in ("Heading 2", "Heading2")]
    h3 = [p.text for p in d.paragraphs if p.style.name in ("Heading 3", "Heading3")]
    print("Saved:", OUT)
    print("Size : %.1f KB" % (os.path.getsize(OUT) / 1024.0))
    print("H1 count:", len(h1))
    print("H2 count:", len(h2))
    print("H3 count:", len(h3))
    print("Tables  :", len(d.tables))
    print("Paras   :", len(d.paragraphs))
    print()
    for t in h1:
        print("  H1:", t)


if __name__ == "__main__":
    main()
