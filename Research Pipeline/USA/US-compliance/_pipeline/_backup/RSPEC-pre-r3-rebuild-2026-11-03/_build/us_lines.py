# -*- coding: utf-8 -*-
"""Form line maps and fixed-length record layouts rendered row by row from layout facts.

A line map or record layout fact is written once in full (tagged) in the workbook; each
rendered row cites the same register id and is logged as a derived location of the key
(us_common.note_use). Figures quoted inside a label are re-tagged with their own facts
(us_common.retag) where such a fact exists."""
import re

from us_common import DD_REF, fact, tag, tagr, rid, src, at, note_use, per_draft, is_draft, retag, retag_sum
from us_rows import row, NONE_OPEN


# ------------------------------------------------------------------ parsing ---
def split_top(s, sep):
    """Split on `sep` outside parentheses / brackets."""
    out, depth, cur, i = [], 0, "", 0
    while i < len(s):
        ch = s[i]
        if ch in "([":
            depth += 1
        elif ch in ")]":
            depth = max(0, depth - 1)
        if depth == 0 and s.startswith(sep, i):
            out.append(cur)
            cur = ""
            i += len(sep)
            continue
        cur += ch
        i += 1
    out.append(cur)
    return [x.strip() for x in out if x.strip()]


LINE_ID = re.compile(r"^(?:lines?\s+)?(\d{1,2}[a-z]?(?:\s*(?:-|,|and)\s*\d{1,2}[a-z]?)*)\s+(.*)$", re.S)
PART = re.compile(r"^(P\d+|Part [IVX]+)(?:\s*\(([^)]*)\))?\s*:\s*(.*)$", re.S)
PART_BARE = re.compile(r"^(P\d+|Part [IVX]+)\s+(.*)$", re.S)


def part_name(p):
    m = re.match(r"P(\d+)$", p or "")
    return f"Part {m.group(1)}" if m else (p or "Form")


def parse_line_map(value):
    """'<header> | P1: 1 label; 2 label | P2 ...' -> (header, [(part, line_id, label, columns)])."""
    segs = split_top(str(value), " | ")
    header, items = "", []
    for i, s in enumerate(segs):
        m = PART.match(s)
        if m:
            part, cols, body = m.group(1), m.group(2), m.group(3)
        else:
            b = PART_BARE.match(s)
            if b:
                lm = LINE_ID.match(b.group(2))
                if lm:
                    items.append((b.group(1), lm.group(1), lm.group(2), None))
                else:
                    items.append((b.group(1), "", b.group(2), None))
                continue
            if i == 0:
                head, _, rest = s.partition(": ")
                if rest and LINE_ID.match(rest):
                    header, part, cols, body = head, "", None, rest
                else:
                    header = s
                    continue
            else:
                part, cols, body = "", None, s
        for it in split_top(body, "; "):
            lm = LINE_ID.match(it)
            if lm:
                items.append((part, lm.group(1), lm.group(2), cols))
            elif items:
                p, lid, lab, c = items[-1]
                items[-1] = (p, lid, f"{lab}; {it}", c)
            else:
                items.append((part, "", it, cols))
    return header, items


def parse_layout(value):
    """'1-2 Record Identifier ...; 3-11 SSN; ...' -> [(start, end, name)]."""
    out = []
    for it in split_top(str(value), "; "):
        m = re.match(r"^(\d{1,3})(?:-(\d{1,3}))?\s+(.*)$", it)
        if m:
            out.append((int(m.group(1)), int(m.group(2) or m.group(1)), m.group(3).strip()))
    return out


def parse_named_positions(value):
    """'name a-b (note); name a; ...' (RS / RO / RU style) -> [(start, end, name)]."""
    v = str(value)
    if ": " in v.split(";")[0]:
        v = v.split(": ", 1)[1]
    out = []
    for it in split_top(v, "; "):
        m = re.match(r"^(.*)\s(\d{1,3})(?:-(\d{1,3}))?(?:\s*\(([^)]*)\))?(?:\s+([A-Za-z].*))?$", it.strip())
        if m:
            name = (m.group(1).strip() + (f" ({m.group(4)})" if m.group(4) else "")
                    + (f", {m.group(5)}" if m.group(5) else ""))
            out.append((int(m.group(2)), int(m.group(3) or m.group(2)), name))
    return out


def parse_codes(value):
    """'A=Agriculture (Form 943); H=Household; blank otherwise' -> [(code, description)]."""
    out = []
    for it in split_top(str(value), "; "):
        m = re.match(r"^\s*([^=]{1,8}?)\s*=\s*(.+)$", it)
        if m:
            out.append((m.group(1).strip(), m.group(2).strip()))
        else:
            out.append(("(other)", it.strip()))
    return out


def check_contiguous(layout, length, label):
    """G-SPOT: a full record covers 1..length with no gap or overlap."""
    pos = 1
    for a, b, _ in sorted(layout):
        if a != pos or b < a:
            raise ValueError(f"{label}: gap or overlap at position {pos} (field starts {a})")
        pos = b + 1
    if pos - 1 != length:
        raise ValueError(f"{label}: record ends at {pos - 1}, expected {length}")


# ------------------------------------------------------------- line rows ---
def line_class(label):
    lab = label.lower()
    if re.match(r"(reserved|legacy)\b", lab):
        return "reserved"
    if re.search(r"signature|designee", lab):
        return "display"
    if re.search(r"number of|employees in pay period|covered employees|total forms|employee count", lab):
        return "count"
    if re.search(r"checkbox|business closed|seasonal|certification|^claim$|adjusted employment tax return|abbreviation|"
                 r"multi-state|member of aggregated|authoritative|explanation|reclassified|under- and over-reported|"
                 r"contact|\bname\b|^ein$|street|^city$|^state$|zip|designated government|special condition|final payroll date|"
                 r"certifications|indicator", lab):
        return "flag"
    if re.match(r"(overpayment|balance due)\b", lab):
        return "calc"
    if re.search(r"\btax\b[^(]*\(\d+[a-z]? x ", lab):
        return "calc"
    if re.search(r"deposit|payments", lab):
        return "amount"
    if re.search(r"balance due|overpayment|\btotal\b|subtotal|before adjustments|after adjustments|refund|credit$", lab):
        return "calc"
    return "amount"


CLASS_TEXT = {
    "amount": ("Input (Amount)", "Payroll result aggregated for the period of the return", "Y"),
    "calc": ("Calculated (Amount)", "Calculated by the return generator from the lines named in the label", "N"),
    "count": ("Input (Count)", "Payroll result: count of employees as the line label defines", "Y"),
    "flag": ("Input (Code / text)", f"{DD_REF}: employer master data or return configuration (forward reference)", "N"),
    "display": ("Display-only (Text)", "Provider hand-off configuration (reporting agent signature / designee)", "N"),
    "reserved": ("Display-only (Text)", "Not mapped (reserved or legacy line, no 2026 payroll content)", "N"),
}
KIND = {"amount": "payroll", "calc": "payroll", "count": "payroll", "flag": "system", "display": "constant",
        "reserved": "excluded"}


def short_name(label, n=70):
    s = re.split(r"\s\(|;\s", label)[0]
    return s if len(s) <= n else s[:n].rsplit(" ", 1)[0]


def line_rows(P, key, form, freq, fm=None, mandatory=(), retag_keys=(), start=1, neg_ok=r"adj|correction|difference",
              sums=()):
    """Rows for every line of the line-map fact `key`. fm = {line_id: field-model row id}.
    Returns (rows, population_rules, n_next)."""
    fm = fm or {}
    f = fact(key)
    hdr, items = parse_line_map(f["value"])
    draft = is_draft(key)
    edition = hdr or form
    rows, prs = [], []
    n = start
    for part, lid, label, cols in items:
        loc = f"{P}-L{n:02d}"
        at(loc)
        note_use(key)
        cls = line_class(label)
        vtype, mapping, pay = CLASS_TEXT[cls]
        ref = fm.get(lid)
        if ref:
            mapping = f"Field-model row {ref} (same amount definition)"
        label_t = _bind(label, retag_keys, sums)
        mand = "Y" if lid in mandatory else ("N" if cls in ("reserved", "display") else "C")
        lid_txt = f"line {lid}" if lid and not lid.startswith(("P", "Part")) else part_name(part)
        cond = ("Not conditional: carried on every return." if mand == "Y" else
                "Not completed for 2026 payrolls (reserved or legacy line)." if cls == "reserved" else
                "Completed by the reporting agent at signature, not by the payroll." if cls == "display" else
                f"Completed only when the situation in the line label applies (column M)"
                + (f"; see field-model row {ref}." if ref else "."))
        colnote = f" Columns: {_bind(cols, retag_keys, sums)}." if cols else ""
        expl = (f"{form} {lid_txt} ({edition}): {label_t}.{colnote} "
                + {"amount": "The return generator fills it from the period payroll results.",
                   "calc": "Never keyed: the return generator computes it from the lines it names.",
                   "count": "The return generator counts the employees as the label defines.",
                   "flag": "Taken from employer master data or the return configuration.",
                   "display": "Completed by the reporting agent (provider) when the return is signed and transmitted.",
                   "reserved": "No payroll content for 2026; the generator leaves it empty."}[cls]
                + (f" Same amount as field-model row {ref}." if ref else "")
                + per_draft(key) + f" {src(key)}")
        q = (f"Confirm against the final 2026 revision: line read from the IRS early-release draft [{f['register_id']}]."
             if draft else NONE_OPEN)
        neg = "Y" if re.search(neg_ok, label, re.I) and cls in ("amount", "calc") else "N"
        rows.append(row(KIND[cls], f"{form} {lid_txt}: {short_name(label)}", label_t, f"{form} {part_name(part)}", loc,
                        pay, mand, cond, f"Form {lid_txt}", {"amount": "Amount", "calc": "Amount", "count": "Integer",
                                                             "flag": "Text / flag", "display": "Text",
                                                             "reserved": "Not applicable"}[cls],
                        {"amount": "Decimal 13.2", "calc": "Decimal 13.2", "count": "Integer", "flag": "Text",
                         "display": "Text", "reserved": "Not applicable"}[cls],
                        {"amount": "See Example Analysis", "calc": "See Example Analysis", "count": "12",
                         "flag": "As held in master data", "display": "Agent signature", "reserved": "Empty"}[cls],
                        mapping, expl, f"Yes: {form} {lid_txt}" if cls not in ("reserved", "display") else "No: not payroll content",
                        "Not applicable", "Cents (2 decimals)" if cls in ("amount", "calc") else "Not applicable", neg,
                        vtype, freq, q))
        if mand == "C":
            prs.append(("Conditional (form line)", f"{loc} {form} {lid_txt}", mapping,
                        f"{form} {lid_txt} ({short_name(label, 90)}) is completed only when the situation named in the line "
                        f"label applies to the employer in the {freq.lower()} period; the return generator then takes the value "
                        f"from {mapping[0].lower() + mapping[1:]}.",
                        "When the situation does not apply the line carries no amount; a later correction of the line goes "
                        "through the correction route of the return, never through the next period's return."))
        n += 1
    return rows, prs, n


def line_source_row(P, key, form, freq):
    """The line-map fact written once in full (the source of the rendered line rows)."""
    loc = f"{P}-L00"
    at(loc)
    f = fact(key)
    return row("constant", f"{form} line map (source)", "Line map", f"{form} (all parts)", loc, "N", "Y",
               "Not conditional.", "Not applicable", "Not applicable", "Text", "See the line rows below",
               "Return generator line table (system constant)",
               f"Line map of {form}: {tagr(key)}.{per_draft(key)} Each line below is one row of this map, in form order. "
               f"{src(key)}", "Yes: completeness of the return", "Not applicable", "Not applicable", "N",
               "Display-only (Text)", freq,
               (f"Confirm against the final 2026 revision [{f['register_id']}]." if is_draft(key) else NONE_OPEN))


def _bind(text, retag_keys=(), sums=()):
    """Figures printed inside a line label, bound to their facts (retag), then combined rates (retag_sum)."""
    out = retag(text, retag_keys) if retag_keys else text
    return retag_sum(out, sums) if sums else out


def fs_line_table(key, form, retag_keys=(), sums=()):
    """File Structure lines: the form's line map as a table (same register id on every line)."""
    hdr, items = parse_line_map(fact(key)["value"])
    r = rid(key)
    lines = [f"Line map: {tag(key)}", "|  Part      | Line          | Label"]
    for part, lid, label, cols in items:
        lines.append(f"|  {part_name(part):<9} | {lid or '-':<13} | {_bind(label, retag_keys, sums)}  [{r}]")
    return lines
