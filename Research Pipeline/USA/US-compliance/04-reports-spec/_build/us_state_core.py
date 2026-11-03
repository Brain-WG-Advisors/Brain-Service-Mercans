# -*- coding: utf-8 -*-
"""Generic builder of a per-jurisdiction Report Specification (one workbook per scope filing,
one Report Matrix row and one core-sheet section per jurisdiction return)."""
import re

from us_common import (STATE_NAMES, DD_REF, CCG_REF, FACTS, fact, tag, tagr, rid, rids, url, src, gap, gap_subject, gap_close,
                       channel_types, portals_in, RSPEC_GAPS, UNRESOLVED, at)
from us_rows import row, section, param_row, gap_row, classify, NONE_OPEN
from us_federal import FIELD_MODEL, OUTBOUND, accuracy, common_remarks
from us_alloc import allocation, jur_of

ALLOC, ORPHANS = allocation()
CHANNEL_CODES = [
    ("online_form", "Portal entry (keyed or web form) on the authority portal"),
    ("file_upload", "File upload (fixed-length, CSV, EFW2, ICESA or another authority layout)"),
    ("xml", "XML file under a published schema or file specification"),
    ("api", "System-to-system transmission (web service, FSET)"),
    ("paper", "Paper form, coupon, CD/DVD, mail or fax"),
]


# ---------------------------------------------------------------------------------------------------------------
# Report Matrix: the Authority (column D) and the portal (columns G / J) are those of the FILING, not of the
# document that carries the legal basis (QA r2 finding 5). A legal-basis row is often hosted by a legislature or a
# code reviser; that host is the source document, never the filing authority. The authority is the first agency
# named by the jurisdiction's own facts for this return, then by any fact of the same jurisdiction and programme;
# the portal is a portal named by a channel or form fact of that agency. The source document stays in "Source:".
LEGIS = re.compile(r"legislat|general assembly|revisor|reviser|council of the district|\bLSC\b|code online|"
                   r"statutes|code of regulations", re.I)
TOPIC = {
    "US-DOR-001": r"(^|\.)(wh|withholding|pit|sit)(\.|_|$)|wh_|\.report\.wh|mo941",
    "US-DOR-002": r"w2|annual_recon|annual_reconciliation|(^|\.)withholding(\.|$)",
    "US-UI-001": r"(^|\.)(sui|ui)(\.|_|$)|ui_qtr|ui_monthly",
    "US-PFML-001": r"pfml|(^|\.)(sdi|tdi|fli|ltc)(\.|_|$)|paid_leave|wa_cares",
    "US-SDNH-001": r"new_?hire",
    "US-WC-001": r"(^|\.)(wc|wbf)(\.|_|$)|wc_report|workers_comp|lni_wc",
    "US-LOC-001": r"(^|\.)local(\.|$)|municipal|school_district",
    "US-LOC-002": r"(^|\.)local(\.|$)",
    "US-LOC-003": r"seattle",
    "US-DOR-003": r"mbt",
    "US-DOR-004": r"mctmt|transit",
}


def agency(a):
    """The agency part of an authority string, or None when it names only a legislative / code host."""
    if not a:
        return None
    a2 = re.sub(r"\s*\((?:published by|wayback)[^)]*\)", "", str(a), flags=re.I)
    parts, depth, cur = [], 0, ""
    for ch in a2:                      # split on ';' outside parentheses
        depth += (ch == "(") - (ch == ")")
        if ch == ";" and depth == 0:
            parts.append(cur)
            cur = ""
        else:
            cur += ch
    parts.append(cur)
    for part in (x.strip() for x in parts):
        if part and not LEGIS.search(part) and not re.search(r"official authority", part, re.I):
            return part
    return None


def _jur_facts(doc, jur):
    """Facts of the same jurisdiction and programme (all facts files), RSPEC first."""
    rx = re.compile(TOPIC.get(doc, r"$^"))
    out = []
    for k, es in FACTS.items():
        if jur_of(k) != jur or not rx.search(k):
            continue
        for f in es:
            out.append(f)
    chan = re.compile(r"return|format|channel|efile|recon|w2|report|form")
    out.sort(key=lambda f: (f["_file"] != "RSPEC-facts.json", not chan.search(f["key"]), f["key"]))
    return out


def filing_authority(doc, jur, ordered_keys, programme=True):
    """(authority, register id it was read from). Agency of the return's own facts first, then (programme=True) of
    any fact of the same jurisdiction and programme; None when only a legislative host is named."""
    for k in ordered_keys:
        a = agency(fact(k).get("authority"))
        if a:
            return a, rid(k)
    for f in (_jur_facts(doc, jur) if programme else []):
        a = agency(f.get("authority"))
        if a:
            return a, f["register_id"]
    return None, None


def filing_portals(doc, jur, auth, chan_txt):
    """[(portal, register id)] of the filing: portals named by the return's own channel / form facts, else by a
    channel or form fact of the same agency, jurisdiction and programme."""
    own = portals_in(chan_txt)
    if own:
        return [(p, None) for p in own]
    out = []
    for f in _jur_facts(doc, jur):
        if auth and agency(f.get("authority")) != auth:
            continue
        for p in portals_in(f.get("value")):
            if p not in [x for x, _ in out]:
                out.append((p, f["register_id"]))
    return out


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
    order = [first] + [k for k in forms + chans + freqs + dues + lays + list(keys) if k != first]
    auth, auth_rid = filing_authority(doc, jur, list(dict.fromkeys(order)))
    host = fact(first).get("authority")
    auth_txt = auth or (f"State authority (not named in the cited sources; legal basis published by {host})"
                        if host else "State authority")
    local = "; ".join(tag(k) for k in forms[:2]) if forms else tag(first)
    fq = "; ".join(tag(k) for k in freqs[:2]) if freqs else freq_default
    du = "; ".join(tag(k) for k in dues[:2]) if dues else (f"As stated in column C ({tag(forms[0])})" if forms else
                                                           f"Open point {gap(gap_key)}" if gap_key else "As stated in column C")
    chan_txt = " ".join(str(fact(k)["value"]) for k in (chans + forms + lays))
    xsd = bool(re.search(r"xsd|schema|spec", chan_txt, re.I))
    ch = channel_types(chan_txt, xsd=xsd) or ["online_form"]
    pmap = filing_portals(doc, jur, auth, chan_txt)
    portals = [p for p, _ in pmap]
    if portals and ch == ["paper"] and re.search(r"electronic", chan_txt, re.I):
        ch = ["online_form", "paper"]   # electronic route through a named portal, paper below the threshold
    if ch[0] == "paper" and len(ch) > 1:
        ch = ch[1:] + ["paper"]
    method = ", ".join(ch) + (f" ({'; '.join(portals)})" if portals else "")
    portal_txt = ("; ".join(p + (f" (named in [{r}])" if r else "") for p, r in pmap) if pmap
                  else "not named in the cited channel sources")
    if chans or lays:
        ff = "; ".join(tag(k) for k in (chans + lays)[:3])
    elif gap_key:
        ff = f"Not configured in this release {gap(gap_key)}"
    else:
        ff = f"Portal or form as stated in column C. {FIELD_MODEL}."
    regs = sorted({r for k in keys for r in rids(k)})
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
    acc = accuracy(", ".join(ch), portal_txt, srcu,
                   "CONFIRMED" if (conf and (chans or forms)) else "TO CONFIRM", pct_txt, closes)
    if extra_note:
        acc += " " + extra_note
    return [f"{doc}-{jur}", f"{name}: {ret_name}", local, auth_txt, fq, du, method, ff, legal, acc]


def jur_section(doc, jur, keys, prefix_base, freq, gap_key=None, extra_keys=(), what="Return parameters and file layout",
                custom_rows=None, skip=()):
    name = STATE_NAMES.get(jur, jur)
    rows = [section(f"{jur}: {name.upper()}")]
    n = 0
    pfx = f"{prefix_base}-{jur}"
    for k in list(keys) + [k for k in extra_keys if k not in keys]:
        if k in skip:
            continue
        n += 1
        rows.append(param_row(jur, k, n, freq, pfx))
    if custom_rows:
        rows += list(custom_rows(pfx, n + 1) if callable(custom_rows) else custom_rows)
        n += sum(1 for r in rows if r[0] != "section") - n
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
               sample_note=None, what="Return parameters and file layout", report_type=OUTBOUND, remarks=None,
               custom=None, skip=(), matrix_fix=None):
    gaps = gaps or {}
    none = none or {}
    extra = extra or {}
    matrix, rows = [], [section("COMMON FIELD MODEL (all jurisdictions)")] + list(common_rows)
    for jur in jurs:
        ks = keys_for(doc, jur) + [k for k in extra.get(jur, []) if k not in keys_for(doc, jur)]
        if jur in none:
            at(f"{doc}-{jur} matrix")
            k = none[jur]
            na, _ = filing_authority(doc, jur, [k], programme=False)   # no return: only the fact's own agency
            matrix.append([f"{doc}-{jur}", f"{STATE_NAMES.get(jur, jur)}: {ret_name}", "No return",
                           na or fact(k).get("authority") or "State authority", "Not applicable", "Not applicable",
                           "Not applicable", "Not applicable", f"[{rid(k)}] {url(k)}",
                           f"No return for this jurisdiction: {tag(k)} [{rid(k)}]. CONFIRMED."])
            continue
        # a value with square brackets cannot be tagged: it is quoted in its custom row, not in the matrix
        mrow = matrix_row(doc, jur, [k for k in ks if "]" not in str(fact(k)["value"])], ret_name, freq_label,
                          gaps.get(jur))
        for col, val in ((matrix_fix or {}).get(jur) or {}).items():
            mrow[col] = val
        matrix.append(mrow)
        w = what.get(jur, "Return parameters and file layout") if isinstance(what, dict) else what
        rows += jur_section(doc, jur, ks, doc.split("-")[1], freq_label, gaps.get(jur), what=w,
                            custom_rows=(custom or {}).get(jur), skip=skip)
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
