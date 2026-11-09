# -*- coding: utf-8 -*-
"""Writes one Report Specification workbook from a definition dict, through the shared
mercans_spec library (9 sheets, 21-column core sheet)."""
import json
import os

from us_common import PKG, ISSUE, AUTHOR, STATUS, CODE, clean, unitize, changelog_rows  # sets the shared library path first

from mercans_spec import workbook as W  # noqa: E402

COUNTRY = "United States of America"


def _clean_tree(x):
    if isinstance(x, str):
        return clean(x)
    if isinstance(x, (list, tuple)):
        return type(x)(_clean_tree(i) for i in x)
    return x


def metadata(d):
    return [
        ("Document ID", d["doc_id"]),
        ("Document Title", d["title"]),
        ("Country", COUNTRY),
        ("Authority", d["authority"]),
        ("Report Type", d["report_type"]),
        ("Tax Type", d["tax_type"]),
        ("Relationship", d["relationship"]),
        ("Frequency", d["frequency"]),
        ("Submission Deadline", d["deadline"]),
        ("File Format", d["file_format"]),
        ("File Extension", d["extension"]),
        ("Character Encoding", d["encoding"]),
        ("Record Length", d["record_length"]),
        ("Record Types / Sections", d["record_types"]),
        ("Version", PKG),
        ("Created Date", ISSUE.strftime("%Y-%m-%d")),
        ("Created By", "Mercans Compliance Regulations Team"),
        ("Official Source", d["official_source"]),
        ("Last Update Reference", d["last_update"]),
        ("Similar To", d["similar_to"]),
    ]


def _overlay():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dd_l_overlay.json")
    return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else {}


def write(d, outdir):
    d = {k: (_clean_tree(v) if k not in ("spec_rows",) else v) for k, v in d.items()}
    # core sheet columns G (conditional reason) and M (field explanation): every numeric tag carries its unit
    d["spec_rows"] = [r if r[0] == "section" else
                      (r[0], [unitize(v) if i in (6, 12) else v for i, v in enumerate(r[1])])
                      for r in d["spec_rows"]]
    # column L: exact DD Field Names for every row that cites the Data Dictionary (DD build writes the overlay; C27 / F25)
    ov = _overlay()
    if ov:
        rows = []
        for r in d["spec_rows"]:
            if r[0] != "section":
                key = f"{d['doc_id']}|{r[1][3]}"
                if key in ov and r[1][11]:
                    r = (r[0], [ov[key] if i == 11 else v for i, v in enumerate(r[1])])
            rows.append(r)
        d["spec_rows"] = rows
    for kind, vals in [r for r in d["spec_rows"] if r[0] != "section"]:
        for v in vals:
            if isinstance(v, str):
                clean(v)
    for r in d["spec_rows"]:
        if r[0] == "section":
            clean(r[1])
    wb = W.new_workbook()
    vc = W.sheet_version_control(
        wb, country=COUNTRY, report_name=d["title"], doc_id=d["doc_id"], version=PKG, date=ISSUE,
        author=AUTHOR, changelog=(changelog_rows("RSPEC", STATUS) or [(PKG, ISSUE, "Issued." if STATUS == "Issued" else "For QA.", STATUS)]), remarks=d["remarks"])
    vc.cell(13, 3).number_format = "d-mmm-yy"
    W.sheet_report_matrix(wb, title=d["title"], metadata=metadata(d), matrix_rows=d["matrix_rows"],
                          banner=d.get("banner"))
    W.sheet_payroll_scope(wb, title=d["title"].upper(), purpose=d["scope_purpose"], blocks=d["scope_blocks"],
                          headers=["SCENARIO", "REPORT?", "NOTES / REASONING"])
    ws4 = W.sheet_spec(wb, d["sheet_name"], d["spec_rows"], local_lang="Authority label, EN")
    W.sheet_file_structure(wb, title=d["title"], blocks=d["fs_blocks"])
    fo = W.sheet_field_options(wb, d["fo_blocks"])
    fo.cell(1, 4).value = "Description (Authority wording, EN)"
    W.sheet_population_rules(wb, d["pr_blocks"])
    W.sheet_example_analysis(wb, title=d["title"], blocks=d["ex_blocks"])
    W.sheet_sample_file(wb, title=d["title"], note=d["sample_note"], sample_lines=d.get("sample_lines", []))
    name = f"{d['doc_id']}-{d['report_name']}-v{PKG}-Spec.xlsx"
    path = os.path.join(outdir, name)
    W.save(wb, path)
    return path
