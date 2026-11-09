# -*- coding: utf-8 -*-
"""python-docx helpers for the SIR index: styles (Arial 11 body, 14 pt H1, 12 pt H2, 11 pt bold H3), cover,
TOC field, bordered tables with a shaded header row, landscape sections, footer."""
import os
import sys as _sys_dw
_DW_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "01-ccg", "_build", "common"))
if _DW_DIR not in _sys_dw.path:
    _sys_dw.path.insert(0, _DW_DIR)
import deliverable_wording as DW  # noqa: E402  v1.1 QA r1: open points in deliverable wording
from docx import Document
from docx.enum.section import WD_ORIENT, WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

HDR_FILL = "D9E1F2"
BORDER = "4F81BD"


def new_document(footer_text, core_title):
    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Inches(8.5), Inches(11)
    sec.left_margin = sec.right_margin = Inches(0.7)
    sec.top_margin = sec.bottom_margin = Inches(0.9)
    n = doc.styles["Normal"]
    n.font.name = "Arial"
    n.font.size = Pt(11)
    n.element.rPr.rFonts.set(qn("w:eastAsia"), "Arial")
    n.paragraph_format.space_after = Pt(6)
    for name, size, before, after in (("Heading 1", 14, 18, 8), ("Heading 2", 12, 14, 6), ("Heading 3", 11, 10, 4)):
        st = doc.styles[name]
        st.font.name = "Arial"
        st.font.size = Pt(size)
        st.font.bold = True
        st.font.color.rgb = RGBColor(0, 0, 0)
        st.element.rPr.rFonts.set(qn("w:eastAsia"), "Arial")
        st.element.rPr.rFonts.set(qn("w:ascii"), "Arial")
        st.element.rPr.rFonts.set(qn("w:hAnsi"), "Arial")
        st.paragraph_format.space_before = Pt(before)
        st.paragraph_format.space_after = Pt(after)
        st.paragraph_format.keep_with_next = True
    p = sec.footer.paragraphs[0]
    p.text = footer_text
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r in p.runs:
        r.font.name = "Arial"
        r.font.size = Pt(8)
        r.font.color.rgb = RGBColor(0x60, 0x60, 0x60)
    doc.core_properties.title = core_title
    doc.core_properties.author = "Mercans Compliance Regulations Team"
    return doc


def para(doc, text, bold=False, italic=False, size=None, align=None, style=None, after=None):
    p = doc.add_paragraph(style=style)
    r = p.add_run(DW.restate(text))
    r.bold = bold
    r.italic = italic
    if size:
        r.font.size = Pt(size)
    if align:
        p.alignment = align
    if after is not None:
        p.paragraph_format.space_after = Pt(after)
    return p


def bullet(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.25)
    p.paragraph_format.first_line_indent = Inches(-0.2)
    p.add_run("•  " + DW.restate(text))
    return p


def h(doc, text, level):
    return doc.add_heading(text, level=level)


def page_break(doc):
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)


def toc(doc):
    p = doc.add_paragraph()
    r = p.add_run()
    for kind, txt in (("begin", None), ("instr", ' TOC \\o "1-2" \\h \\z \\u '), ("separate", None),
                      ("text", "Right-click to update the Table of Contents."), ("end", None)):
        if kind == "instr":
            el = OxmlElement("w:instrText")
            el.set(qn("xml:space"), "preserve")
            el.text = txt
            r._r.append(el)
        elif kind == "text":
            t = OxmlElement("w:t")
            t.text = txt
            r._r.append(t)
        else:
            fc = OxmlElement("w:fldChar")
            fc.set(qn("w:fldCharType"), kind)
            r._r.append(fc)
    return p


def _shade(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill)
    tcPr.append(shd)


def _borders(table):
    tblPr = table._tbl.tblPr
    b = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        e = OxmlElement(f"w:{edge}")
        e.set(qn("w:val"), "single")
        e.set(qn("w:sz"), "6")
        e.set(qn("w:space"), "0")
        e.set(qn("w:color"), BORDER)
        b.append(e)
    tblPr.append(b)


def _repeat_header(row):
    trPr = row._tr.get_or_add_trPr()
    el = OxmlElement("w:tblHeader")
    el.set(qn("w:val"), "1")
    trPr.append(el)


def _cell(cell, text, bold=False, size=8.5):
    cell.text = ""
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    r = p.add_run(DW.restate(str(text)))
    r.font.name = "Arial"
    r.font.size = Pt(size)
    r.bold = bold


def table(doc, header, rows, widths, size=8.5):
    """Bordered table, shaded repeating header row, fixed layout. widths in inches."""
    t = doc.add_table(rows=1, cols=len(header))
    t.alignment = WD_TABLE_ALIGNMENT.LEFT
    t.autofit = False
    _borders(t)
    tblPr = t._tbl.tblPr
    lay = OxmlElement("w:tblLayout")
    lay.set(qn("w:type"), "fixed")
    tblPr.append(lay)
    for i, htxt in enumerate(header):
        c = t.rows[0].cells[i]
        _cell(c, htxt, bold=True, size=size)
        _shade(c, HDR_FILL)
        c.width = Inches(widths[i])
    _repeat_header(t.rows[0])
    for row in rows:
        cells = t.add_row().cells
        for i, v in enumerate(row):
            _cell(cells[i], v, size=size)
            cells[i].width = Inches(widths[i])
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    return t


def landscape_section(doc):
    s = doc.add_section(WD_SECTION.NEW_PAGE)
    s.orientation = WD_ORIENT.LANDSCAPE
    s.page_width, s.page_height = Inches(11), Inches(8.5)
    s.left_margin = s.right_margin = Inches(0.6)
    s.top_margin = s.bottom_margin = Inches(0.8)
    return s


def portrait_section(doc):
    s = doc.add_section(WD_SECTION.NEW_PAGE)
    s.orientation = WD_ORIENT.PORTRAIT
    s.page_width, s.page_height = Inches(8.5), Inches(11)
    s.left_margin = s.right_margin = Inches(0.7)
    s.top_margin = s.bottom_margin = Inches(0.9)
    return s
