"""Statutory Payroll Audit Report (Mercans QCRM model, as Mammoet_P09-P13_Audit_Report.docx).
Copies the model .docx and replaces its content, keeping every format (Raleway/Open Sans, colours, tables).
Usage: python -I audit_report.py <spec.py> <out.docx>   (spec defines SPEC dict; refuses to overwrite)"""
import copy
import importlib.util
import os
import shutil
import sys

import docx
from docx.shared import RGBColor

MODEL = r"C:\Users\instituto\Downloads\Mammoet_P09-P13_Audit_Report.docx"
GREEN, ORANGE, GREY, INK = RGBColor(0x0E, 0x7C, 0x66), RGBColor(0xFF, 0x5C, 0x00), RGBColor(0xA7, 0xB1, 0xB6), \
    RGBColor(0x35, 0x3D, 0x41)


def set_runs(p, texts):
    """Write texts into the existing runs of paragraph p (keeps run formatting); extra runs emptied."""
    for i, r in enumerate(p.runs):
        r.text = texts[i] if i < len(texts) else ""


def bullets(doc, first_idx, count_old, items):
    """Replace a block of bullet paragraphs (3 runs: marker, bold label, text) with items [(label, text)]."""
    paras = doc.paragraphs[first_idx:first_idx + count_old]
    proto = paras[0]._p
    anchor = paras[-1]._p
    new = []
    for lab, txt in items:
        el = copy.deepcopy(proto)
        anchor.addnext(el)
        anchor = el
        new.append(el)
    for p in paras:
        p._p.getparent().remove(p._p)
    for el, (lab, txt) in zip(new, items):
        p = docx.text.paragraph.Paragraph(el, None)
        set_runs(p, ["▪  ", lab + " ", txt])


def fill_table(t, rows, colour_col=None, colours=None):
    """Keep header row 0, use row 1 as prototype for every data row."""
    proto = copy.deepcopy(t.rows[1]._tr)
    for r in list(t.rows)[1:]:
        t._tbl.remove(r._tr)
    for vals in rows:
        tr = copy.deepcopy(proto)
        t._tbl.append(tr)
        row = t.rows[-1]
        for ci, v in enumerate(vals):
            cell = row.cells[ci]
            p = cell.paragraphs[0]
            set_runs(p, [v])
            for extra in cell.paragraphs[1:]:
                extra._p.getparent().remove(extra._p)
            if colour_col is not None and ci == colour_col and colours:
                for run in p.runs:
                    run.font.color.rgb = colours(v)


def result_colour(v):
    v = v.lower()
    if any(w in v for w in ("finding", "invalid", "error", "not evidenced", "to confirm", "presentation")):
        return ORANGE
    if "pending" in v or "not tested" in v:
        return GREY
    return GREEN


def build(spec, out):
    if os.path.exists(out):
        sys.exit(f"refusing to overwrite {out}")
    shutil.copyfile(MODEL, out)
    d = docx.Document(out)
    P = d.paragraphs
    set_runs(P[2], [spec["subtitle_lead"], spec["subtitle_bold"]])
    set_runs(P[4], [spec.get("audience", "FOR SENIOR MANAGEMENT")])
    fill_table(d.tables[1], spec["engagement"])
    set_runs(P[7], [spec["opinion_lead"], spec["opinion_bold"]])
    set_runs(P[8], [spec["opinion_detail"]])
    # bullets: scope (11-13), methodology (16-22), key findings (25-30) - replace from the bottom up
    bullets(d, 25, 6, spec["key_findings"])
    bullets(d, 16, 7, spec["methodology"])
    bullets(d, 11, 3, spec["scope"])
    P = d.paragraphs
    fill_table(d.tables[3], spec["areas"], colour_col=1, colours=result_colour)
    # observations intro + 6 category tables (tables 5-10)
    i35 = next(i for i, p in enumerate(P) if p.text.startswith("The observations below"))
    set_runs(P[i35], spec["obs_intro"])
    cats = spec["observations"]
    for k, t in enumerate(d.tables[5:11]):
        rows = cats[k][1]
        prev = t._tbl.getprevious()           # the category title sits right above its table
        set_runs(docx.text.paragraph.Paragraph(prev, None), [f"{k + 1} · {cats[k][0]}"])
        fill_table(t, rows if rows else [("-", "No observation in this category.")])
    P = d.paragraphs
    ic = next(i for i, p in enumerate(P) if p.text.startswith("On the audit performed"))
    set_runs(P[ic], spec["conclusion"])
    set_runs(P[-1], [spec["footer"]])
    d.save(out)
    print("written", out)


if __name__ == "__main__":
    s = importlib.util.spec_from_file_location("spec", sys.argv[1])
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    build(m.SPEC, sys.argv[2])
