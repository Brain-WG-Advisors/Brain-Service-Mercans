# -*- coding: utf-8 -*-
"""Generic builder of a per-jurisdiction Report Specification (one workbook per scope filing,
one Report Matrix row and one core-sheet section per jurisdiction return)."""
import re

from us_common import (STATE_NAMES, DD_REF, CCG_REF, fact, tag, tagr, rid, url, src, gap, gap_subject, gap_close,
                       channel_types, portals_in, RSPEC_GAPS, UNRESOLVED, at)
from us_rows import row, section, param_row, gap_row, classify, NONE_OPEN
from us_federal import FIELD_MODEL, OUTBOUND, accuracy, common_remarks
from us_alloc import allocation

ALLOC, ORPHANS = allocation()
CHANNEL_CODES = [
    ("online_form", "Portal entry (keyed or web form) on the authority portal"),
    ("file_upload", "File upload (fixed-length, CSV, EFW2, ICESA or another authority layout)"),
    ("xml", "XML file under a published schema or file specification"),
    ("api", "System-to-system transmission (web service, FSET)"),
    ("paper", "Paper form, coupon, CD/DVD, mail or fax"),
]


def keys_for(doc, jur):
    return list(ALLOC.get(doc, {}).get(jur, []))


def pick(keys, label):
    return [k for k in keys if classify(k)[0] == label]


def matrix_row(doc, jur, keys, ret_name, freq_default, gap_key=None, extra_note=""):
    name = STATE_NAMES.get(jur, jur)
    at(f"{doc}-{jur} matrix")
    if not keys:
        g = gap(gap_key) if gap_key else ""
        return [f"{doc}-{jur}", f"{name}: {ret_name}", "Not configured in this release", "State authority (see column I)",
                freq_default, f"Open point {g}", "Not configured in this release", f"Not configured in this release {g}",
                "See column J", accuracy("not configured", "not configured", "not configured", "TO CONFIRM", "50%",
                                         f"{gap_close(gap_key) if gap_key else 'the authority return page'} {g}")]
    forms = pick(keys, "Return form and filing rule") + pick(keys, "Return applicability")
    freqs = pick(keys, "Filing and deposit frequency rule")
    dues = pick(keys, "Due date rule")
    chans = pick(keys, "Submission channel and file format")
    lays = pick(keys, "Record layout")
    first = (forms or keys)[0]
    auth = fact(first).get("authority") or "State authority"
    local = "; ".join(tag(k) for k in forms[:2]) if forms else tag(first)
    fq = "; ".join(tag(k) for k in freqs[:2]) if freqs else freq_default
    du = "; ".join(tag(k) for k in dues[:2]) if dues else (f"As stated in column C ({tag(forms[0])})" if forms else
                                                           f"Open point {gap(gap_key)}" if gap_key else "As stated in column C")
    chan_txt = " ".join(str(fact(k)["value"]) for k in (chans + forms + lays))
    xsd = bool(re.search(r"xsd|schema|spec", chan_txt, re.I))
    ch = channel_types(chan_txt, xsd=xsd) or ["online_form"]
    portals = portals_in(chan_txt)
    method = ", ".join(ch) + (f" ({'; '.join(portals)})" if portals else "")
    if chans or lays:
        ff = "; ".join(tag(k) for k in (chans + lays)[:3])
    elif gap_key:
        ff = f"Not configured in this release {gap(gap_key)}"
    else:
        ff = f"Portal or form as stated in column C. {FIELD_MODEL}."
    regs = sorted({rid(k) for k in keys})
    urls = sorted({url(k) for k in keys if url(k)})
    legal = " ".join(f"[{r}]" for r in regs) + "; " + " ".join(urls[:2])
    srcu = url((chans or forms or keys)[0])
    conf = all(fact(k).get("confidence") == "high" for k in (chans or forms or keys))
    inspected = any("artifact inspection" in str(fact(k).get("verification_method")) for k in (chans + lays))
    pct_txt = ("90% (authority file specification read)" if inspected else
               "80% (authority page read; no layout or real filing)" if (chans or lays) else
               "75% (form and timing read; channel detail from the form rule)")
    closes = (f"{gap_close(gap_key)} {gap(gap_key)}" if gap_key else
              "a real filing or the provider's acceptance report for this jurisdiction")
    acc = accuracy(", ".join(ch), (", ".join(portals) or "authority portal") + f" {srcu}", srcu,
                   "CONFIRMED" if (conf and (chans or forms)) else "TO CONFIRM", pct_txt, closes)
    if extra_note:
        acc += " " + extra_note
    return [f"{doc}-{jur}", f"{name}: {ret_name}", local, auth, fq, du, method, ff, legal, acc]


def jur_section(doc, jur, keys, prefix_base, freq, gap_key=None, extra_keys=(), what="Return parameters and file layout"):
    name = STATE_NAMES.get(jur, jur)
    rows = [section(f"{jur}: {name.upper()}")]
    n = 0
    pfx = f"{prefix_base}-{jur}"
    for k in list(keys) + [k for k in extra_keys if k not in keys]:
        n += 1
        rows.append(param_row(jur, k, n, freq, pfx))
    if gap_key:
        n += 1
        rows.append(gap_row(jur, gap_key, n, pfx, freq, what))
    if n == 0:
        n += 1
        rows.append(gap_row(jur, "RSPEC-RQ-10", n, pfx, freq, what))
    return rows


def cond_rules(rows, doc_label):
    """Population rules for every conditional jurisdiction parameter row (>= 100 characters)."""
    out = []
    for kind, vals in [r for r in rows if r[0] != "section"]:
        if vals[5] != "C" or not str(vals[3]).count("-") >= 2:
            continue
        txt = (f"{vals[0]}: {vals[6]} The rule text and figure are in column M of row {vals[3]}; the payroll evaluates the "
               f"condition each {str(vals[18]).lower()} period for every employer registered in the jurisdiction before "
               f"generating the {doc_label}.")
        edge = ("Scenarios: an employer crossing the threshold mid-year switches route from the next period the authority names; "
                "a multistate employer applies the rule only to the wages of this jurisdiction; nonresident aliens, household and "
                "agricultural employees follow the federal population rules unless the jurisdiction rule says otherwise.")
        out.append(("Conditional (jurisdiction)", f"{vals[3]} {vals[0]}", "Jurisdiction configuration", txt, edge))
    return out


def option_blocks(extra=None):
    blocks = [("SUBMISSION CHANNEL CLASS (Report Matrix column G)",
               [("Channel class", c, d, d, "Mercans Report Specification standard (channel classes)")
                for c, d in CHANNEL_CODES])]
    if extra:
        blocks += extra
    return blocks


def state_book(doc, report_name, sheet, title, authority, tax_type, relationship, frequency, deadline, file_format,
               record_types, official, last_update, similar, purpose, jurs, ret_name, freq_label, common_rows,
               scope_blocks, fo_extra, pr_common, ex_blocks, fs_extra, gaps=None, none=None, extra=None,
               sample_note=None, what="Return parameters and file layout", report_type=OUTBOUND, remarks=None):
    gaps = gaps or {}
    none = none or {}
    extra = extra or {}
    matrix, rows = [], [section("COMMON FIELD MODEL (all jurisdictions)")] + list(common_rows)
    for jur in jurs:
        ks = keys_for(doc, jur) + [k for k in extra.get(jur, []) if k not in keys_for(doc, jur)]
        if jur in none:
            at(f"{doc}-{jur} matrix")
            k = none[jur]
            matrix.append([f"{doc}-{jur}", f"{STATE_NAMES.get(jur, jur)}: {ret_name}", "No return",
                           fact(k).get("authority") or "State authority", "Not applicable", "Not applicable",
                           "Not applicable", "Not applicable", f"[{rid(k)}] {url(k)}",
                           f"No return for this jurisdiction: {tag(k)} [{rid(k)}]. CONFIRMED."])
            continue
        matrix.append(matrix_row(doc, jur, ks, ret_name, freq_label, gaps.get(jur)))
        rows += jur_section(doc, jur, ks, doc.split("-")[1], freq_label, gaps.get(jur), what=what)
    pr = list(pr_common) + [("CONDITIONAL JURISDICTION PARAMETERS", cond_rules(rows, title))]
    fs = [("FILE FORMAT", [f"{FIELD_MODEL} for the common field model; each jurisdiction's own channel and layout are in "
                           "its section of the core sheet and in the Report Matrix.",
                           "Where a jurisdiction layout is published and read, its positions are given in the jurisdiction section; "
                           "otherwise the provider maps the field model to the authority format.",
                           "FORMAT TO CONFIRM vs a real filing in every jurisdiction."])] + list(fs_extra)
    note = sample_note or ("No official sample filing is held for these returns and none is constructed. Verified channels: "
                           "the per-jurisdiction channel classes and portals in the Report Matrix (column G and the accuracy note).")
    return dict(doc_id=doc, report_name=report_name, sheet_name=sheet, title=title, authority=authority,
                report_type=report_type, tax_type=tax_type, relationship=relationship, frequency=frequency,
                deadline=deadline, file_format=file_format, extension="Per jurisdiction (see Report Matrix)",
                encoding="Per jurisdiction (ASCII for fixed-length layouts)", record_length="Per jurisdiction",
                record_types=record_types, official_source=official, last_update=last_update, similar_to=similar,
                matrix_rows=matrix, scope_purpose=purpose, scope_blocks=scope_blocks, spec_rows=rows, fs_blocks=fs,
                fo_blocks=option_blocks(fo_extra), pr_blocks=pr, ex_blocks=ex_blocks, sample_note=note,
                remarks=remarks or common_remarks())
