# -*- coding: utf-8 -*-
"""Deliverable wording for limitations (v1.1 QA r1, 2026-11-06).

The open points of the facts files (`unresolved[].why`, gaps.json subjects) are written by the research
agents as research-process notes ("X not read", "the site returned an error", "fetched 2026-11-02").
The generators print them as the body of a documented limitation. This module restates that wording in
deliverable language at render time; the facts, the register and gaps.json are never edited.

    "<subject> not read"                  -> "<subject> not verified against the official source"
    "Not read: <subject>"                 -> "Not verified against the official source: <subject>"
    "not checked" / "not obtained"        -> "not verified" / "not verified against the official source"
    "(... site returned an error)"        -> removed (access narrative)
    "(Wayback id_ copy, fetched <date>)"  -> removed (retrieval stamp; the authority name stays)
    "this pass"                           -> "this release"
    ", extracted and inspected"           -> removed

Only text OUTSIDE [[FACT:...]] / [[GAP:...]] tags is changed: a tag value must equal its fact (C46,
tag_sync), so a fact value is never rewritten here. Legitimate domain uses are kept ("RS and RV are not
read or processed by SSA", "not read by SSA", "SSA does not read them").

Used by: 01-ccg/_build/common/ccg_common.finalize (every CCG unit), 03-statutory-integrations/_build
(sir_docx text writer), 02-wtc/_build (cell writer), 04-reports-spec/_build/us_book.write (every string of a
spec workbook) and 05-data-dictionary/_build (cell writer).
"""
import re

_TAG = re.compile(r"(\[\[(?:FACT|GAP|GAPKEY):[^\]]*\]\])")
OFFICIAL = "verified against the official source"

RULES = [
    # retrieval stamps: ', fetched 2026-11-02' is dropped; an archived-copy attribution ('Wayback copy') stays as provenance
    (r",?\s*\b(?:fetched|retrieved) (?:on )?20\d\d-\d\d-\d\d\b", ""),
    # access narrative: a parenthetical saying a page could not be reached
    (r"\s*\([^()|]*\b(?:returned (?:an error|a? ?(?:HTTP )?\d{3})|was unreachable|is unreachable|unreachable)\b[^()|]*\)", ""),
    (r"\s*\((?:LDR [^()]*)?\b40[34](?:/40[34])?\)", ""),
    # verification wording
    (r"(?<!does )(?<!do )\bnot read\b(?! (?:or processed|by SSA))", "not " + OFFICIAL),
    (r"(?<![\w])Not read\b", "Not " + OFFICIAL),
    (r"\bnot re-read in this pass\b", "not re-verified for this release"),
    (r"\bin this pass\b", "in this release"),
    (r"\bthis pass\b", "this release"),
    (r"(?<!box is )\bnot checked\b", "not verified"),
    (r"\bnot obtained\b", "not " + OFFICIAL),
    (r",?\s*\b(?:extracted|downloaded) and inspected(?:;\s*parallel lookups)?", ""),
    (r"\binspected directly\b", "verified"),
    (r",?\s*and the [\w ]{0,30}?site was unreachable", ""),
    (r"\b(?:were|was|are|is) not readable\b", lambda m: m.group(0).split(" ")[0] + " not verified against the official source"),
    (r"\bnot transcribed\b", "not configured"),
    # access narrative and lookup steps (v1.1 QA r1 sweep of the limitation lines)
    (r"\s*\((?:the )?[\w.\- ]{0,30}?\bblocked\b[^()|]*\)", ""),
    (r"\s*\(behind the employer login\)", ""),
    (r"\s*\(Lexis-only [^()|]*\)", ""),
    (r"\s*\((?i:cdx) [^()|]*\)", ""),
    (r"\s*\((?:bulletin )?texts? not opened\)", ""),
    (r";\s*secondary lead only\.", "; only a secondary source refers to it."),
    (r"\bcould not be read\b", "is not " + OFFICIAL),
    (r"\bnot (?:located|isolated)\b", "not established from an official source"),
    (r"(?<!was )(?<!is )\bnot found\b", "not established from an official source"),
    (r"\bnot (?:downloaded|captured)\b", "not " + OFFICIAL),
    (r"\bin the saved copy of its cited source\b", "in its cited source"),
    (r"\s*Re-derived annual/periods in Python\.", ""),
    (r",\s*re-derived\.", "."),
    (r"\s*\bin Python\b", ""),
]
_RULES = [(re.compile(a), b) for a, b in RULES]
LOG = []


def restate(text):
    """Deliverable wording outside tags; returns the text unchanged when nothing matches."""
    if not isinstance(text, str) or not text:
        return text
    parts = _TAG.split(text)
    changed = False
    for i in range(0, len(parts), 2):
        s = parts[i]
        for rx, rep in _RULES:
            s2 = rx.sub(rep, s)
            if s2 != s:
                LOG.append(rx.pattern[:60])
                s = s2
        if s != parts[i]:
            parts[i] = re.sub(r"  +", " ", s)
            changed = True
    return "".join(parts) if changed else text


def restate_tree(x):
    if isinstance(x, str):
        return restate(x)
    if isinstance(x, list):
        return [restate_tree(i) for i in x]
    if isinstance(x, tuple):
        return tuple(restate_tree(i) for i in x)
    if isinstance(x, dict):
        return {k: restate_tree(v) for k, v in x.items()}
    return x


# ---------------------------------------------------------------- effective-period wording (C41) --
# v1.1 QA r1: the generic C41 wording "in force for <year>; the source carries no effective date" was printed
#   - next to an item with its own end date (SIR US-UI-001-GA period 1: "until 2026-08-08 ... in force for 2026"),
#   - next to an item that is proposed only (DD/RSPEC/SIR Texas enhanced wage-report content, US-TXV6-005),
# and a provisional or historical register row (proposed rule, dead bill) could be shown as an effective date.
# period_status() returns the wording that replaces the date for those items, or None (caller keeps its wording).
import csv as _csv
import os as _os

_REG = None


def _register():
    global _REG
    if _REG is None:
        base = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "..", ".."))
        with open(_os.path.join(base, "00-official-sources", "legal-basis-register.csv"), encoding="utf-8", newline="") as fh:
            _REG = {r["id"]: r for r in _csv.DictReader(fh)}
    return _REG


def reg_status(rid):
    return str(_register().get(rid, {}).get("status", "")).strip().lower()


def period_status(f):
    """'proposed, not in force' / 'historical source, not confirmed in force' / 'implementing rule proposed only, not in
    force' for a fact whose own register row, or a register row its note cites, is provisional or historical."""
    own = [f.get("register_id")] + list(f.get("_also_register_ids") or [])
    st = {reg_status(r) for r in own if r}
    if "provisional" in st:
        return "proposed, not in force"
    if "historical" in st:
        return "historical source, not confirmed in force"
    cited = set(re.findall(r"\bUS-[A-Z0-9]+-\d{3}\b", str(f.get("note") or ""))) - set(own)
    if any(reg_status(r) == "provisional" for r in cited):
        return "implementing rule proposed only, not in force"
    return None


def period_wording(f, generic):
    """Effective-period wording of a fact for the WTC / SIR / DD writers. `generic` is the writer's own wording for
    a fact whose register row gives no effective date; an item with its own end date prints its dates instead."""
    s = period_status(f)
    if s:
        return s
    a, b = f.get("effective_from"), f.get("effective_to")
    if f.get("_effective_from_basis") and not b:
        return generic
    if a and b:
        return f"effective {a} to {b}"
    if a:
        return f"effective from {a}"
    return ""


def period_cell(f):
    """Effective column of a CCG parameter table for a proposed / historical item, else None (caller prints its dates)."""
    st = period_status(f)
    if not st:
        return None
    a = f.get("effective_from")
    if st.startswith("implementing"):
        return f"from {a} (statute); {st}" if a else st
    return f"{st} (dated {a})" if a else st
