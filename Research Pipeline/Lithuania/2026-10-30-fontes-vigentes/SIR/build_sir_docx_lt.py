"""Assemble the Lithuania Statutory Integration Register into LT-SIR-001-v1.2.docx.
v1.2 (2026-10-30): baseline for the DDEBF7 shading is now v1.1 (sections rendered with the
v1.1 builder from 2026-10-29-correcoes/SIR, read only), so the highlight marks only v1.1 -> v1.2.
(Copied from BE-compliance/03-statutory-integrations/build_sir_docx.py; same house format.)
v1.1 (2026-10-29): every paragraph, heading or table cell whose rendered text does not exist
anywhere in v1.0 (rendered with the v1.0 builder from 2026-10-27-SIR) gets light-blue
shading DDEBF7, so the highlight marks exactly what changed; code inside bold is rendered without backticks;
TOC refreshed on open (w:updateFields); page number in the footer; core properties set.

Reads sections/s00..s08 markdown, emits a Word document in the same house format
as BE-SIR-001 v1.0:
  Arial 11pt body, 14pt H1, 12pt H2, 11pt H3 bold
  Title page, TOC field on page 2, page breaks between sections,
  footer "LT-SIR-001 v1.2 | Mercans Compliance Regulations Team | 2026 | Page N"
"""
import datetime
import glob
import os
import re

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor

BASE = os.path.dirname(os.path.abspath(__file__))
SECTIONS = os.path.join(BASE, "sections")
OUT = os.path.join(BASE, "LT-SIR-001-v1.2.docx")

FOOTER = "LT-SIR-001 v1.2 | Mercans Compliance Regulations Team | 2026 | Page "
TITLE = "Lithuania Statutory Integration Register — LT-SIR-001 v1.2"
SHADE = "DDEBF7"
MARK_ROW = "{++}"
MARK = "{+}"


def take_mark(text):
    """Return (clean_text, marked); strips {++}/{+} anywhere in the text."""
    marked = MARK in text or MARK_ROW in text
    text = text.replace(MARK_ROW, "").replace(MARK, "")
    return re.sub(r"  +", " ", text).strip(), marked


OLD_DIR = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "2026-10-29-correcoes", "SIR"))
CURRENT_BASE = set()


def norm(text):
    return re.sub(r"\s+", " ", text).strip()


def load_baseline():
    """Rendered texts of the previous version (v1.1), per section file, using its own builder (read only)."""
    import importlib.util
    import sys
    sys.dont_write_bytecode = True  # never write into the previous-version folder
    spec = importlib.util.spec_from_file_location("old_sir_builder", os.path.join(OLD_DIR, "build_sir_docx_lt.py"))
    old = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(old)
    base = {}
    for path in sorted(glob.glob(os.path.join(OLD_DIR, "sections", "s*.md"))):
        d = Document()
        with open(path, encoding="utf-8") as fh:
            old.render_markdown(d, fh.read(), [True])
        texts = {norm(p.text) for p in d.paragraphs}
        for tb in d.tables:
            for r in tb.rows:
                for c in r.cells:
                    texts.add(norm(c.text))
        base[os.path.basename(path)] = texts
    return base


def changed(text):
    n = norm(text)
    return bool(n) and n not in CURRENT_BASE


def _shd():
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), SHADE)
    return shd


def shade_paragraph(paragraph):
    paragraph._p.get_or_add_pPr().append(_shd())


def shade_cell(cell):
    cell._tc.get_or_add_tcPr().append(_shd())


# ---------------------------------------------------------------- styles
def setup_styles(doc):
    normal = doc.styles["Normal"]
    normal.font.name = "Arial"
    normal.font.size = Pt(11)
    normal.element.rPr.rFonts.set(qn("w:eastAsia"), "Arial")
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.space_before = Pt(0)

    for name, size, bold, before, after in (
        ("Heading 1", 14, True, 18, 8),
        ("Heading 2", 12, True, 14, 6),
        ("Heading 3", 11, True, 12, 4),
    ):
        st = doc.styles[name]
        st.font.name = "Arial"
        st.font.size = Pt(size)
        st.font.bold = bold
        st.font.color.rgb = RGBColor(0x00, 0x00, 0x00)
        st.paragraph_format.space_before = Pt(before)
        st.paragraph_format.space_after = Pt(after)
        st.paragraph_format.keep_with_next = True

    for name in ("List Bullet", "List Number"):
        st = doc.styles[name]
        st.font.name = "Arial"
        st.font.size = Pt(11)


def add_footer(doc):
    for section in doc.sections:
        p = section.footer.paragraphs[0]
        p.text = FOOTER
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run()
        fc = OxmlElement("w:fldChar")
        fc.set(qn("w:fldCharType"), "begin")
        r._r.append(fc)
        it = OxmlElement("w:instrText")
        it.set(qn("xml:space"), "preserve")
        it.text = " PAGE "
        r._r.append(it)
        fc = OxmlElement("w:fldChar")
        fc.set(qn("w:fldCharType"), "separate")
        r._r.append(fc)
        tx = OxmlElement("w:t")
        tx.text = "1"
        r._r.append(tx)
        fc = OxmlElement("w:fldChar")
        fc.set(qn("w:fldCharType"), "end")
        r._r.append(fc)
        for run in p.runs:
            run.font.name = "Arial"
            run.font.size = Pt(8)
            run.font.color.rgb = RGBColor(0x60, 0x60, 0x60)


def set_update_fields(doc):
    """Ask Word to refresh the TOC and page fields when the file is opened."""
    uf = OxmlElement("w:updateFields")
    uf.set(qn("w:val"), "true")
    doc.settings.element.append(uf)


def set_core_properties(doc):
    now = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0, tzinfo=None)
    cp = doc.core_properties
    cp.author = "Mercans Compliance"
    cp.last_modified_by = "Mercans Compliance"
    cp.title = "Lithuania Statutory Integration Register (LT-SIR-001 v1.2)"
    cp.subject = "Statutory Integration Register, Lithuania, tax year 2026"
    cp.created = now
    cp.modified = now
    cp.revision = 2


# ---------------------------------------------------------------- inline
INLINE = re.compile(r"(\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`)")


def add_runs(paragraph, text):
    """Render **bold**, *italic* and `code` inside a paragraph."""
    for chunk in INLINE.split(text):
        if not chunk:
            continue
        if chunk.startswith("**") and chunk.endswith("**") and len(chunk) > 4:
            for k, part in enumerate(chunk[2:-2].split("`")):
                if not part:
                    continue
                r = paragraph.add_run(part)
                r.bold = True
                if k % 2 == 1:
                    r.font.name = "Consolas"
                    r.font.size = Pt(9.5)
        elif chunk.startswith("*") and chunk.endswith("*") and len(chunk) > 2:
            r = paragraph.add_run(chunk[1:-1])
            r.italic = True
        elif chunk.startswith("`") and chunk.endswith("`") and len(chunk) > 2:
            r = paragraph.add_run(chunk[1:-1])
            r.font.name = "Consolas"
            r.font.size = Pt(9.5)
        else:
            paragraph.add_run(chunk)


# ---------------------------------------------------------------- blocks
def add_toc(doc):
    p = doc.add_paragraph()
    r = p.add_run()
    fld = OxmlElement("w:fldChar")
    fld.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = r'TOC \o "1-3" \h \z \u'
    sep = OxmlElement("w:fldChar")
    sep.set(qn("w:fldCharType"), "separate")
    txt = OxmlElement("w:t")
    txt.text = "Right-click and select 'Update Field' to build the table of contents."
    end = OxmlElement("w:fldChar")
    end.set(qn("w:fldCharType"), "end")
    for el in (fld, instr, sep, txt, end):
        r._r.append(el)


def add_table(doc, rows):
    ncols = max(len(r) for r in rows)
    table = doc.add_table(rows=0, cols=ncols)
    table.style = "Table Grid"
    table.autofit = True
    for i, row in enumerate(rows):
        cells = table.add_row().cells
        for j in range(ncols):
            cell = cells[j]
            cell.paragraphs[0].text = ""
            para = cell.paragraphs[0]
            para.paragraph_format.space_after = Pt(2)
            para.paragraph_format.space_before = Pt(2)
            value = row[j] if j < len(row) else ""
            value, marked = take_mark(value)
            add_runs(para, value)
            if changed(cell.text):
                shade_cell(cell)
            for run in para.runs:
                run.font.name = "Arial"
                run.font.size = Pt(9)
                if i == 0:
                    run.bold = True
    return table


def split_table_row(line):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c.strip() for c in line.split("|")]


def is_separator_row(line):
    return bool(re.fullmatch(r"\|?[\s:\-\|]+\|?", line.strip())) and "-" in line


def add_code(doc, lines):
    for line in lines:
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.left_indent = Pt(18)
        r = p.add_run(line if line.strip() else " ")
        r.font.name = "Consolas"
        r.font.size = Pt(8.5)


# ---------------------------------------------------------------- parser
def render_markdown(doc, text, first_section):
    lines = text.split("\n")
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        if stripped.startswith("```"):
            i += 1
            block = []
            while i < n and not lines[i].strip().startswith("```"):
                block.append(lines[i])
                i += 1
            i += 1
            add_code(doc, block)
            continue

        if stripped.startswith("|") and i + 1 < n and is_separator_row(lines[i + 1]):
            rows = [split_table_row(stripped)]
            i += 2
            while i < n and lines[i].strip().startswith("|"):
                rows.append(split_table_row(lines[i]))
                i += 1
            add_table(doc, rows)
            doc.add_paragraph()
            continue

        stripped, marked = take_mark(stripped)
        if stripped.startswith("### "):
            h = doc.add_paragraph(stripped[4:].strip(), style="Heading 3")
            if changed(h.text):
                shade_paragraph(h)
            i += 1
            continue
        if stripped.startswith("## "):
            h = doc.add_paragraph(stripped[3:].strip(), style="Heading 2")
            if changed(h.text):
                shade_paragraph(h)
            i += 1
            continue
        if stripped.startswith("# "):
            if not first_section[0]:
                doc.add_page_break()
            first_section[0] = False
            h = doc.add_paragraph(stripped[2:].strip(), style="Heading 1")
            if changed(h.text):
                shade_paragraph(h)
            i += 1
            continue

        if stripped.startswith("> "):
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Pt(18)
            p.paragraph_format.space_before = Pt(6)
            add_runs(p, stripped[2:].strip())
            for run in p.runs:
                run.font.size = Pt(10)
            i += 1
            continue

        if re.match(r"^[-*] ", stripped):
            p = doc.add_paragraph(style="List Bullet")
            add_runs(p, stripped[2:].strip())
            if changed(p.text):
                shade_paragraph(p)
            i += 1
            continue

        if re.match(r"^\d+\. ", stripped):
            p = doc.add_paragraph(style="List Number")
            add_runs(p, re.sub(r"^\d+\.\s*", "", stripped))
            i += 1
            continue

        p = doc.add_paragraph()
        add_runs(p, stripped)
        if changed(p.text):
            shade_paragraph(p)
        i += 1


# ---------------------------------------------------------------- build
def build():
    doc = Document()
    setup_styles(doc)

    section = doc.sections[0]
    section.left_margin = Pt(56)
    section.right_margin = Pt(56)
    section.top_margin = Pt(56)
    section.bottom_margin = Pt(50)

    # ---- title page
    for _ in range(6):
        doc.add_paragraph()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(TITLE)
    r.bold = True
    r.font.size = Pt(22)
    r.font.name = "Arial"
    shade_paragraph(p)  # title changed: v1.1 -> v1.2

    for text, size, bold in (
        ("Statutory Integration Register", 14, False),
        ("Tax year 2026", 12, False),
        ("Currency: EUR  |  Country code: LT", 12, False),
        ("", 11, False),
        ("Mercans Compliance Regulations Team", 12, True),
        ("Version 1.2 — 30 October 2026", 11, False),
        ("", 11, False),
        ("Technical content is sourced to the authorities' own published documentation "
         "(Sodra and VMI) and dated in Section 7. Related Report Specifications: "
         "LT-SODRA-003 v1.2, LT-VMI-001 v1.3 and LT-VMI-002 v1.2.", 10, False),
    ):
        q = doc.add_paragraph()
        q.alignment = WD_ALIGN_PARAGRAPH.CENTER
        rr = q.add_run(text)
        rr.font.size = Pt(size)
        rr.bold = bold
        rr.font.name = "Arial"
        if text.startswith("Version 1.2") or "LT-SODRA-003 v1.2" in text:
            shade_paragraph(q)

    doc.add_page_break()

    # ---- TOC page
    doc.add_paragraph("Table of Contents", style="Heading 1")
    add_toc(doc)

    # ---- sections
    first_section = [True]
    files = sorted(glob.glob(os.path.join(SECTIONS, "s*.md")))
    if not files:
        raise SystemExit("no section files found in %s" % SECTIONS)
    global CURRENT_BASE
    baseline = load_baseline()
    for path in files:
        CURRENT_BASE = set().union(*baseline.values())
        with open(path, encoding="utf-8") as fh:
            render_markdown(doc, fh.read(), first_section)

    add_footer(doc)
    set_update_fields(doc)
    set_core_properties(doc)
    doc.save(OUT)
    return OUT, len(files)


if __name__ == "__main__":
    out, count = build()
    d = Document(out)
    h1 = [p.text for p in d.paragraphs if p.style.name == "Heading 1"]
    h2 = [p.text for p in d.paragraphs if p.style.name == "Heading 2"]
    h3 = [p.text for p in d.paragraphs if p.style.name == "Heading 3"]
    print("sections read : %d" % count)
    print("H1 count      : %d" % len(h1))
    for t in h1:
        print("   - %s" % t)
    print("H2 count      : %d" % len(h2))
    print("H3 count      : %d" % len(h3))
    print("tables        : %d" % len(d.tables))
    print("paragraphs    : %d" % len(d.paragraphs))
    print("size (bytes)  : %d" % os.path.getsize(out))
    print("saved         : %s" % out)
