"""Assemble the United States CCG (stage 1, final assembly step) into US-CCG-001-v{package}.docx.

Inputs (read-only):
  _pipeline/build-manifest.json            country, code, year, currency, package version/date
  01-ccg/modules/m01..m13 *.md + coverage.md   (coverage = Module 11 section 11.3, right after m11)
  01-ccg/annexes/annex_FED.md, annex_MULTI.md, annex_{USPS}.md x 51

Output: 01-ccg/{CODE}-CCG-001-v{version}.docx

Rendering rules (FR/BE build_ccg_docx.py pattern + agent contract 5.1):
  Arial 11 pt body, H1 14 pt, H2 12 pt, H3 11 pt bold, H4 11 pt bold italic;
  title page, TOC field on page 2, Version Control, page break before every H1;
  footer "{CODE}-CCG-001 v{version} | Mercans Compliance Regulations Team | {YEAR}".
  [[FACT:key=value]] tags are kept literally (the release step strips them) and are
  protected from inline markdown parsing. RESEARCH-GAP markers are copied as written.
  No text of the units is altered.

Run: python -I build_ccg_docx.py <BASE>
"""
import json
import os
import re
import sys

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor

BASE = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "..", "..", ".."))
MAN = json.load(open(os.path.join(BASE, "_pipeline", "build-manifest.json"), encoding="utf-8"))
CODE = MAN["code"]
VERSION = MAN["package"]["version"]
ISSUE = MAN["package"]["issue_date"]
# QA r2: the manifest issue_date is a planning placeholder until the owner sets it (its _note says
# so). Until then the Version Control row carries the build date with status Draft, never the
# placeholder. CCG_BUILD_DATE pins the date for a reproducible rebuild.
if "placeholder" in str(MAN["package"].get("_note", "")).lower():
    import datetime as _dt
    ISSUE = os.environ.get("CCG_BUILD_DATE") or _dt.date.today().isoformat()
ISSUED_BY = MAN["package"].get("issued_by", "Mercans Compliance Regulations Team")
YEAR = MAN["year"]
COUNTRY = MAN["country"]
CURRENCY = MAN["currency"]

CCG = os.path.join(BASE, "01-ccg")
MODDIR = os.path.join(CCG, "modules")
ANXDIR = os.path.join(CCG, "annexes")
OUT = os.path.join(CCG, f"{CODE}-CCG-001-v{VERSION}.docx")
DOC_ID = f"{CODE}-CCG-001 v{VERSION}"
FOOTER = f"{DOC_ID} | Mercans Compliance Regulations Team | {YEAR}"
TITLE = f"{COUNTRY} Country Configuration Guide \u2014 {DOC_ID}"

MODULES = ["m01_foundational", "m02_master_data", "m03_gross_to_net", "m04_compensation",
           "m05_social_security", "m06_tax", "m07_deductions", "m08_leave", "m09_termination",
           "m10_reporting", "m11_advanced", "coverage", "m12_worked_examples", "m13_practices"]
USPS = sorted(["AK", "AL", "AR", "AZ", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "IA", "ID",
               "IL", "IN", "KS", "KY", "LA", "MA", "MD", "ME", "MI", "MN", "MO", "MS", "MT", "NC",
               "ND", "NE", "NH", "NJ", "NM", "NV", "NY", "OH", "OK", "OR", "PA", "RI", "SC", "SD",
               "TN", "TX", "UT", "VA", "VT", "WA", "WI", "WV", "WY"])
ANNEXES = ["annex_FED", "annex_MULTI"] + [f"annex_{j}" for j in USPS]


def unit_path(unit):
    d = MODDIR if not unit.startswith("annex_") else ANXDIR
    p = os.path.join(d, unit + ".md")
    if not os.path.exists(p):
        raise SystemExit(f"missing unit file: {p}")
    return p


# ---------------------------------------------------------------- styles
def setup_styles(doc):
    normal = doc.styles["Normal"]
    normal.font.name = "Arial"
    normal.font.size = Pt(11)
    normal.element.rPr.rFonts.set(qn("w:eastAsia"), "Arial")
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.space_before = Pt(0)
    for name, size, italic, before, after in (
        ("Heading 1", 14, False, 18, 8),
        ("Heading 2", 12, False, 14, 6),
        ("Heading 3", 11, False, 12, 4),
        ("Heading 4", 11, True, 10, 4),
    ):
        st = doc.styles[name]
        st.font.name = "Arial"
        rfonts = st.element.rPr.find(qn("w:rFonts"))
        for att in ("w:asciiTheme", "w:hAnsiTheme", "w:eastAsiaTheme", "w:cstheme"):
            if rfonts is not None and rfonts.get(qn(att)) is not None:
                del rfonts.attrib[qn(att)]
        st.font.size = Pt(size)
        st.font.bold = True
        st.font.italic = italic
        # round 3b (QA r3 minor 14): heading colour of the precedent REFERENCE_CCG_Bulgaria.docx (Heading 1-3 = 1F4E79,
        # measured with python-docx on 2026-11-02)
        st.font.color.rgb = RGBColor(0x1F, 0x4E, 0x79)
        st.paragraph_format.space_before = Pt(before)
        st.paragraph_format.space_after = Pt(after)
        st.paragraph_format.keep_with_next = True
    for name in ("List Bullet", "List Bullet 2", "List Number"):
        st = doc.styles[name]
        st.font.name = "Arial"
        st.font.size = Pt(11)


def add_footer(doc):
    for section in doc.sections:
        p = section.footer.paragraphs[0]
        p.text = FOOTER
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for run in p.runs:
            run.font.name = "Arial"
            run.font.size = Pt(8)
            run.font.color.rgb = RGBColor(0x60, 0x60, 0x60)


# ---------------------------------------------------------------- inline
TAG = re.compile(r"\[\[FACT:[^\]]*\]\]")
INLINE = re.compile(r"(\*\*[^*]+\*\*|(?<![\w*])\*[^*\s][^*]*?[^*\s]\*(?![\w*])|(?<![\w*])\*[^*\s]\*(?![\w*])|`[^`]+`)")
TOK = re.compile("\ue000(\\d+)\ue001")


def add_runs(paragraph, text, size=None, bold_all=False):
    """Render **bold**, *italic* and `code`; FACT tags are protected and copied literally."""
    stash = []

    def hide(m):
        stash.append(m.group(0))
        return f"\ue000{len(stash) - 1}\ue001"

    hidden = TAG.sub(hide, text)
    unhide = lambda s: TOK.sub(lambda m: stash[int(m.group(1))], s)  # noqa: E731
    for chunk in INLINE.split(hidden):
        if not chunk:
            continue
        if chunk.startswith("**") and chunk.endswith("**") and len(chunk) > 4:
            r = paragraph.add_run(unhide(chunk[2:-2]))
            r.bold = True
        elif chunk.startswith("*") and chunk.endswith("*") and len(chunk) > 2 and not chunk.startswith("**"):
            r = paragraph.add_run(unhide(chunk[1:-1]))
            r.italic = True
        elif chunk.startswith("`") and chunk.endswith("`") and len(chunk) > 2:
            r = paragraph.add_run(unhide(chunk[1:-1]))
            r.font.name = "Consolas"
            r.font.size = Pt(max((size or 11) - 1.5, 7))
            if bold_all:
                r.bold = True
            continue
        else:
            r = paragraph.add_run(unhide(chunk))
        if size:
            r.font.size = Pt(size)
        if bold_all:
            r.bold = True


# ---------------------------------------------------------------- blocks
def add_toc(doc):
    p = doc.add_paragraph()
    r = p.add_run()
    els = []
    fld = OxmlElement("w:fldChar"); fld.set(qn("w:fldCharType"), "begin"); els.append(fld)
    instr = OxmlElement("w:instrText"); instr.set(qn("xml:space"), "preserve")
    instr.text = r'TOC \o "1-2" \h \z \u'; els.append(instr)
    sep = OxmlElement("w:fldChar"); sep.set(qn("w:fldCharType"), "separate"); els.append(sep)
    txt = OxmlElement("w:t"); txt.text = "Right-click and select 'Update Field' to build the table of contents."
    els.append(txt)
    end = OxmlElement("w:fldChar"); end.set(qn("w:fldCharType"), "end"); els.append(end)
    for el in els:
        r._r.append(el)


def shade(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear"); shd.set(qn("w:color"), "auto"); shd.set(qn("w:fill"), fill)
    tcPr.append(shd)


def repeat_header(row):
    trPr = row._tr.get_or_add_trPr()
    h = OxmlElement("w:tblHeader"); h.set(qn("w:val"), "true")
    trPr.append(h)


def add_table(doc, rows):
    ncols = max(len(r) for r in rows)
    size = 8 if ncols >= 6 else 9
    table = doc.add_table(rows=len(rows), cols=ncols)
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = True
    for i, row in enumerate(rows):
        r = table.rows[i]
        cells = r.cells
        if i == 0:
            repeat_header(r)
        for j in range(ncols):
            cell = cells[j]
            para = cell.paragraphs[0]
            para.paragraph_format.space_after = Pt(1)
            para.paragraph_format.space_before = Pt(1)
            value = row[j] if j < len(row) else ""
            add_runs(para, value, size=size, bold_all=(i == 0))
            for run in para.runs:
                run.font.name = run.font.name or "Arial"
            if i == 0:
                shade(cell, "E8EDF2")  # round 3b: content-table header fill of the precedent (nested tables, 392 cells)
    return table


def split_table_row(line):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    # round 2: a fact value may contain '|' (CT per-period table rows, layout fact ct.wh.tables.columns);
    # pipes inside [[FACT:]] / [[GAP:]] tags are not cell separators
    line = re.sub(r"\[\[(?:FACT|GAP):[^\]]*\]\]", lambda m: m.group(0).replace("|", ""), line)
    # QA r3c finding 3: a markdown-escaped pipe '\|' in cell text is a literal character, not a separator,
    # and its backslash is not printed
    line = line.replace(r"\|", "")
    return [c.strip().replace("", "|") for c in line.split("|")]


TABLE_LINT = []


def lint_table(rows, where):
    """QA r3c finding 3: every row must have the header's cell count; a mismatch fails the build."""
    n = len(rows[0])
    bad = [(i, len(r)) for i, r in enumerate(rows) if len(r) != n]
    if bad:
        TABLE_LINT.append({"where": where, "header_cols": n, "bad_rows": bad[:10], "header": rows[0]})
    return not bad


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


STATS = {"tables": 0, "code_lines": 0}


def render_markdown(doc, text, state):
    lines = text.split("\n")
    i, n = 0, len(lines)
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
                block.append(lines[i].rstrip())
                i += 1
            i += 1
            add_code(doc, block)
            STATS["code_lines"] += len(block)
            continue
        if stripped.startswith("|") and i + 1 < n and is_separator_row(lines[i + 1]):
            rows = [split_table_row(stripped)]
            i += 2
            while i < n and lines[i].strip().startswith("|"):
                rows.append(split_table_row(lines[i]))
                i += 1
            lint_table(rows, f"{state.get('unit', '?')} table {STATS['tables'] + 1}: {stripped[:80]}")
            add_table(doc, rows)
            STATS["tables"] += 1
            doc.add_paragraph().paragraph_format.space_after = Pt(2)
            continue
        m = re.match(r"^(#{1,4}) (.*)$", stripped)
        if m:
            level = len(m.group(1))
            if level == 1:
                if state["started"]:
                    doc.add_page_break()
                state["started"] = True
            p = doc.add_paragraph(style=f"Heading {level}")
            add_runs(p, m.group(2).strip())
            i += 1
            continue
        if stripped.startswith(">"):
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Pt(18)
            p.paragraph_format.space_before = Pt(6)
            add_runs(p, stripped.lstrip(">").strip(), size=10)
            i += 1
            continue
        mb = re.match(r"^(\s*)[-*] (.*)$", line)
        if mb:
            style = "List Bullet 2" if len(mb.group(1).expandtabs(4)) >= 2 else "List Bullet"
            p = doc.add_paragraph(style=style)
            add_runs(p, mb.group(2).strip())
            i += 1
            continue
        mn = re.match(r"^\s*(\d+)\. (.*)$", line)
        if mn:
            # keep the source numeral (lists are short; Word auto-numbering would restart unpredictably)
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Pt(18)
            p.paragraph_format.first_line_indent = Pt(-14)
            add_runs(p, f"{mn.group(1)}. {mn.group(2).strip()}")
            i += 1
            continue
        p = doc.add_paragraph()
        add_runs(p, stripped)
        i += 1


def centered(doc, text, size, bold=False):
    q = doc.add_paragraph()
    q.alignment = WD_ALIGN_PARAGRAPH.CENTER
    rr = q.add_run(text)
    rr.font.size = Pt(size)
    rr.bold = bold
    rr.font.name = "Arial"


def build():
    doc = Document()
    setup_styles(doc)
    s = doc.sections[0]
    s.left_margin = s.right_margin = Pt(56)
    s.top_margin = Pt(56)
    s.bottom_margin = Pt(50)

    # ---- title page
    for _ in range(6):
        doc.add_paragraph()
    centered(doc, TITLE, 22, True)
    for text, size, bold in (
        ("Country Configuration Guide", 14, False),
        (f"Tax year {YEAR} (calendar year)", 12, False),
        (f"Currency: {CURRENCY}  |  Country code: {CODE}", 12, False),
        ("", 11, False),
        ("Mercans Compliance Regulations Team", 12, True),
        (f"Version {VERSION}", 11, False),
        ("", 11, False),
        ("Scope: private-sector employers and their common-law employees; the federal layer, the "
         "multistate routing layer and one annex per State and the District of Columbia. Independent "
         "contractors and Form 1099-NEC reporting are out of scope (owner instruction of 2026-10-29) "
         "[US-OWN-008].", 10, False),
    ):
        centered(doc, text, size, bold)
    doc.add_page_break()

    # ---- TOC page (page 2)
    doc.add_paragraph("Table of Contents", style="Heading 1")
    add_toc(doc)
    doc.add_page_break()

    # ---- Version Control (Bulgaria precedent: first H1, 5-column table)
    doc.add_paragraph("Version Control", style="Heading 1")
    add_table(doc, [["Version", "Effective Date", "Change Description", "Status", "Updated By"],
                    [VERSION, ISSUE,
                     "Initial issue: core modules, population coverage matrix, federal and multistate "
                     "annexes, and one annex per State and the District of Columbia.",
                     "For QA" if "placeholder" in str(MAN["package"].get("_note", "")).lower() else "Issued", ISSUED_BY]])
    state = {"started": True}

    order = []
    for u in MODULES:
        order.append(u)
        state["unit"] = u
        with open(unit_path(u), encoding="utf-8") as fh:
            render_markdown(doc, fh.read(), state)

    # ---- annex part divider
    doc.add_page_break()
    doc.add_paragraph("Jurisdiction Annexes", style="Heading 1")
    p = doc.add_paragraph()
    add_runs(p, "The annexes carry the parameters of each layer: Annex FED (federal layer), Annex MULTI "
                "(multistate routing layer), then one annex per State and the District of Columbia in "
                "order of the two-letter postal code.")
    for u in ANNEXES:
        order.append(u)
        state["unit"] = u
        with open(unit_path(u), encoding="utf-8") as fh:
            render_markdown(doc, fh.read(), state)

    add_footer(doc)
    doc.core_properties.title = TITLE
    doc.core_properties.author = "Mercans Compliance Regulations Team"
    doc.core_properties.last_modified_by = "Mercans Compliance Regulations Team"
    doc.core_properties.comments = ""
    import datetime as _dt
    now = _dt.datetime.now(_dt.timezone.utc).replace(microsecond=0, tzinfo=None)
    doc.core_properties.created = now
    doc.core_properties.modified = now
    doc.core_properties.revision = 1
    doc.save(OUT)
    return order


if __name__ == "__main__":
    order = build()
    _lint_out = os.path.join(BASE, "01-ccg", "_build", "common", "out", "table_column_lint.json")
    os.makedirs(os.path.dirname(_lint_out), exist_ok=True)
    json.dump({"tables": STATS["tables"], "mismatched_tables": len(TABLE_LINT), "detail": TABLE_LINT},
              open(_lint_out, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    if TABLE_LINT:
        print("TABLE COLUMN LINT FAILED:", json.dumps(TABLE_LINT[:5], ensure_ascii=False))
        sys.exit(2)
    d = Document(OUT)
    lv = {}
    for p in d.paragraphs:
        if p.style.name.startswith("Heading "):
            lv[p.style.name] = lv.get(p.style.name, 0) + 1
    print(json.dumps({"out": OUT, "bytes": os.path.getsize(OUT), "units": len(order), "order": order,
                      "headings": lv, "tables": len(d.tables), "paragraphs": len(d.paragraphs),
                      "code_lines": STATS["code_lines"]}, indent=1))
