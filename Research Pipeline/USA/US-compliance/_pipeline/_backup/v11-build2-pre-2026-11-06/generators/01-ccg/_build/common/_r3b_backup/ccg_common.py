# -*- coding: utf-8 -*-
"""Shared round-2 helpers for every CCG unit generator (US build, artifact-builder, QA r1 fixes).

Imported by: 01-ccg/_build-m01-m07/ccglib.py, 01-ccg/_build/m08_m13/factlib.py,
01-ccg/_scratch/annex-FED-CT/build_annexes.py, 01-ccg/_scratch/annex-DC-MA/build_annexes.py,
_research/synthesis-B/_scratch-ccg-build-MD-NV/build_annexes.py, 01-ccg/_build-annex-NY-WY/build.py.

Every generator calls finalize(unit_file, text) on the unit text just before writing it.
finalize() is deterministic and idempotent and only reads _research/gaps.json, the facts
files and the override tables in this folder, so a re-run after agent 2 adds or closes a fact
gives the new text without hand edits. It does five things:

  1. alias()          old fact key -> canonical key (KEY-ALIAS-MAP.csv, QA r1 fix 1)
  2. gap tags         every "RESEARCH-GAP" statement gets [[GAP:<RQ id>]] (C70, fix 3); a gap
                      whose gaps.json status is documented_limitation (next-year value not yet
                      published) is written as a "Not yet published (expected ...)" note (fix 8);
                      a marker whose request is closed (absent from gaps.json) is dropped (fix 8)
  3. internal paths   pipeline-internal file paths removed from deliverable text (fix 5)
  4. percent tags     untagged percentages bound to their fact key (percent_tags.json, fix 2)
  5. annex skeleton   one heading scheme for the 53 annexes (annex_skeleton(), fix 4)
"""
import csv
import glob
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
RES = os.path.join(BASE, "_research")

# QA r1 finding 57: one contractor out-of-scope sentence everywhere, citing US-OWN-008
CONTRACTOR_SENTENCE = ("Independent contractors and Form 1099-NEC reporting are out of scope "
                       "(owner instruction of 2026-10-29) [US-OWN-008].")

# ------------------------------------------------------------------ aliases --
ALIAS = {}
_amap = os.path.join(RES, "qa-r1-fix", "KEY-ALIAS-MAP.csv")
if os.path.exists(_amap):
    for r in csv.DictReader(open(_amap, encoding="utf-8")):
        if re.fullmatch(r"[a-z0-9_]+(\.[a-z0-9_]+)+", r["canonical_key"]):
            ALIAS[r["old_key"]] = r["canonical_key"]


def alias(key):
    seen = set()
    while key in ALIAS and key not in seen:
        seen.add(key)
        key = ALIAS[key]
    return key


# --------------------------------------------------------------------- gaps --
GAPS = []
_gp = os.path.join(RES, "gaps.json")
if os.path.exists(_gp):
    GAPS = json.load(open(_gp, encoding="utf-8")).get("gaps", [])
REQS = {}
_rp = os.path.join(RES, "CCG-research-request.json")
if os.path.exists(_rp):
    for q in json.load(open(_rp, encoding="utf-8")).get("requests", []):
        REQS[q["id"]] = q


def _unit_of(loc):
    m = re.match(r"01-ccg/(?:modules|annexes)/([^!]+)", loc or "")
    return m.group(1) if m else None


GAP_BY_UNIT_KEY = {}
for _g in GAPS:
    GAP_BY_UNIT_KEY.setdefault((_unit_of(_g.get("location")), _g["key"]), []).append(_g)
CLOSED_KEYS = {}
for _q in REQS.values():
    if str(_q.get("_status", "")).startswith("closed"):
        CLOSED_KEYS.setdefault(_unit_of(_q.get("location")), set()).add(_q["key"])
        CLOSED_KEYS.setdefault(None, set()).add(_q["key"])

# r1 marker text -> RQ id, for markers whose text does not carry the key (built once from the
# round-1 units by build_gap_text_map.py; the line numbers of gaps.json point at round 1)
_tm = os.path.join(HERE, "gap_text_map.json")
GAP_TEXT_MAP = json.load(open(_tm, encoding="utf-8")) if os.path.exists(_tm) else {}

GAP_LOG = {"tagged": [], "limitation": [], "dropped": [], "unmapped": []}

# unresolved[] items settled by a configuration decision (written as the decision, not as a gap)
DECIDED = {
    ("annex_CT.md", "ct.wh.engine_method"):
        "Withholding engine method (configuration decision of 2026-11-02): the DRS per-period tables of IP 2026(1) "
        "up to each table maximum, the TPG-211 rules above it; see the method choice in CT.2.",
}

MARK = "⚠️ RESEARCH-GAP"
_TAGRX = re.compile(r"\[\[(?:FACT|GAP):[^\]]*\]\]")


def norm_marker(s):
    s = _TAGRX.sub("", s)
    s = re.sub(r"`", "", s)
    s = re.sub(r"\s+", " ", s).strip().lower()
    return s[:160]


def gap_entry(unit, key):
    xs = GAP_BY_UNIT_KEY.get((unit, key)) or GAP_BY_UNIT_KEY.get((unit, alias(key)))
    return xs[0] if xs else None


def gap_tag(unit, key):
    g = gap_entry(unit, key)
    return f"[[GAP:{g['id']}]]" if g else ""


def _expected(g):
    q = REQS.get(g["id"], {})
    e = q.get("_expected_publication") or ""
    e = re.sub(r"\s*\(per the request\)", "", e)
    e = re.sub(r"\s*per the request", "", e)
    e = re.sub(r"\s*\(date passed on (\d{4}-\d{2}-\d{2})[^)]*\)", r"; not yet found when last checked on \1", e)
    return e.strip()


def _keys_in(seg, unit):
    """Gap entries of this unit whose key appears in the segment (longest key first)."""
    out = []
    cands = [k for (u, k) in GAP_BY_UNIT_KEY if u == unit]
    for k in sorted(cands, key=len, reverse=True):
        if re.search(r"(?<![A-Za-z0-9_.])" + re.escape(k) + r"(?![A-Za-z0-9_]|\.[A-Za-z0-9_])", seg):
            out.append(k)
    return out


def _closed_key_in(seg, unit):
    for k in sorted(CLOSED_KEYS.get(unit, set()) | CLOSED_KEYS.get(None, set()), key=len, reverse=True):
        if re.search(r"(?<![A-Za-z0-9_.])" + re.escape(k) + r"(?![A-Za-z0-9_]|\.[A-Za-z0-9_])", seg):
            return k
    return None


def _segments(line):
    """Split a line into marker segments: [(start, end)] of each RESEARCH-GAP occurrence up to the
    next occurrence or the next table-cell boundary."""
    idx = [m.start() for m in re.finditer(re.escape(MARK) + "|RESEARCH-GAP", line)]
    # collapse 'RESEARCH-GAP' hits that are part of a '⚠️ RESEARCH-GAP'
    starts = []
    for i in idx:
        if starts and i - starts[-1] <= len(MARK) and line[starts[-1]:i + 12].endswith("RESEARCH-GAP"):
            continue
        starts.append(i)
    segs = []
    for n, s in enumerate(starts):
        e = starts[n + 1] if n + 1 < len(starts) else len(line)
        cell = line.find(" | ", s)
        if line.lstrip().startswith("|") and cell != -1 and cell < e:
            e = cell
        segs.append((s, e))
    return segs


def _limitation_text(g, seg):
    exp = _expected(g)
    body = re.sub(r"^" + re.escape(MARK) + r"\s*(\([^)]*\))?\s*:?\s*", "", seg).strip()
    body = re.sub(r"^RESEARCH-GAP\s*(\([^)]*\))?\s*:?\s*", "", body).strip()
    body = clean_gap_body(body)
    exp_txt = f" (expected {exp})" if exp else ""
    return f"Not yet published{exp_txt} [[GAP:{g['id']}]]" + (f": {body}" if body else ".")


# ------------------------------------------------- round 3: no marker text in the deliverable --
# QA r2 (C29 v2.12): 'RESEARCH-GAP' is a HARD marker. Orchestrator decision of round 3: every open
# item is a documented limitation carried by the QA report; the CCG states what is configured,
# keeps the [[GAP:id]] tag (C70; release strips it) and never writes a value without a fact.
NEUTRAL_PREFIX = "Not configured in this release"
_BODY_RULES = [
    # builder flags and request bookkeeping
    (r"\(\s*(?:non-)?blocking\s*;\s*research request filed under this key\s*\)\s*-?\s*", ""),
    (r"\(\s*(?:non-)?blocking\s*,\s*`[^`]+`\s*\)\s*:?\s*", ""),
    (r"\(\s*(?:non-)?blocking\s*\)\s*:?\s*", ""),
    (r"\s*\((?:request key|request|research request)\s+`[^`]+`[^()]*\)", ""),
    (r"\s*\(open item `[^`]+`.*$", ""),
    (r"\s*\bopen item `[^`]+`;?", ""),
    (r"\s*(?:Closes with|To close|Source that would close it|Would close it|would close it)\s*:.*$", ""),
    (r"(?:;\s*|\.\s*)?\bsee (?:research )?request `[^`]+`\.?", ""),
    (r"\bresearch request `[^`]+`", "an open research item"),
    (r"^`[a-z0-9_.]+`\s*(?:-|:)?\s*", ""),
    (r"\s*\((?:research request|request|request key)\b[^()]*\)", ""),
    (r"\bcarry no facts key\b|\bcarries no facts key\b", lambda m: "are not established as values" if m.group(0).startswith("carry") else "is not established as a value"),
    (r"\bfacts key\b", "established value"),
    (r"\bin the research\b", "in the sources read"),
    (r"\s*\(`[a-z0-9_.]+`\)", ""),
    # pipeline wording -> deliverable wording (accurate, no value)
    (r"\bnot established by the research\b", "not established from an official source"),
    (r"\bNot established by the research\b", "Not established from an official source"),
    (r"\bis not stated in the facts\b", "is not established from an official source"),
    (r"\bis not in the facts\b|\bare not in the facts\b", lambda m: m.group(0).replace("in the facts", "established from an official source")),
    (r"\bnot in the facts\b", "not established from an official source"),
    (r"\bnot carried as a fact\b", "not established from an official source"),
    (r"\bthe facts carry no\b", "no official source read for this release gives a"),
    (r"\bno fact states\b", "no official source read for this release states"),
    (r"\bhas no fact\b", "is not established from an official source"),
    (r"\bkeyed\b", "established"),
    (r"\bin the FED unit\b", ""),
    (r"\bwas not researched\b", "is not established from an official source"),
    (r"^Not researched\.?", "Not established from an official source."),
    (r"\s*\((?:budget|browser pass|Chrome pass)\)", ""),
    (r"\s*via (?:a )?browser(?: pass)?", ""),
    (r"\s*in a browser pass", ""),
    (r"\bto be (?:confirmed|verified)\b", "not confirmed"),
    (r",?\s*see the open item on this key", ""),
    (r"\s*\(QA r\d[^)]*\)", ""),
    (r"\bnot run within budget\b", "not completed"),
    (r"\s*within budget\b", ""),
    (r"\bnot fetched\b", "not read"),
    (r"\bnot swept\b", "not reviewed"),
    (r"\bnot researched\b", "not established from an official source"),
    (r"\bcarry no facts key\b", "are not established as values"),
    (r"\bcarries no facts key\b", "is not established as a value"),
    (r"\bfacts key\b", "established value"),
    (r"\bin the research\b", "in the sources read"),
    (r"\s*\(research request raised\)", ""),
    (r"\bper-band rate keys\b", "per-band rates"),
    (r"\bkeys? for\b", "values for"),
    (r"\s*carried in the [a-z0-9_.]+\*? facts", " written in this annex"),
    (r"\bnot established in the facts\b", "not established from an official source"),
    (r"\bare not carried as facts\b", "are not established from an official source"),
    (r"\bnot dated facts\b", "not dated results"),
    (r"\bhave not been swept\b", "are not established"),
    (r"\bthe open items are in\b", "the related items are in"),
    (r"\s*named in `[a-z0-9_]+(?:\.[a-z0-9_]+)+`", ""),
    (r"\s*`[a-z0-9_]+(?:\.[a-z0-9_]+)+`", ""),
]


def clean_gap_body(body):
    """Deliverable wording for the description that followed a marker: no request bookkeeping,
    no 'what would close it' (that lives in the QA report), no pipeline vocabulary."""
    body = re.sub(r"^\s*:\s*", "", body)
    parts = re.split(r"(\[\[(?:FACT|GAP):[^\]]*\]\])", body)
    for i in range(0, len(parts), 2):
        for rx, rep in _BODY_RULES:
            if i > 0 and isinstance(rx, str) and rx.startswith("^"):
                continue
            parts[i] = re.sub(rx, rep, parts[i])
    b = "".join(parts)
    b = re.sub(r"\s{2,}", " ", b).strip()
    b = re.sub(r"^[\s:;,.-]+", "", b)
    b = re.sub(r"[\s;,:-]+$", "", b)
    b = re.sub(r"\s+([.;,])", r"\1", b)
    if b and b[0].islower() and not b.startswith(("e.g.", "i.e.")):
        b = b[0].upper() + b[1:]
    if b and not b.endswith((".", ")", "]")):
        b += "."
    if b in ("Not established.", "Not established"):
        b = "Not established from an official source."
    for rx, rep in BODY_OVERRIDES:
        if re.search(rx, b):
            return rep
    return b


# Round 3: marker bodies written by agent 2 for secondary-only numbers (QA r2 finding 3 / C30): the
# number is removed from the deliverable and carried as a limitation in the QA report.
BODY_OVERRIDES = [
    (r"^1 USD fee and 150 USD lump-sum", "The per-payment employer fee and the lump-sum reporting threshold rest on a secondary source and are not configured."),
    (r"^The 40,000 sales \(and related\) thresholds", "The thresholds for the State UI rate exclusions are not established from an official source."),
    (r"^FEN125 \(2003\) timing figures", "The remittance and start timing of income withholding orders (form FEN125) are not established from an official source."),
    (r"^The statement that Iowa has no state SDI/TDI/PFML programme", "Whether Iowa has a State SDI/TDI/PFML programme is not established from an official Iowa source; none is configured."),
    (r"^The 2026-07-01 effective date of the move of the garnishment limit", "The effective date of the move of the garnishment limit to IC 37-2-6-4 is not established from an official source."),
    (r"^The 1 USD per-payment IWO fee", "The employer fee per income-withholding payment is not established from an official source."),
    (r"^The 150 USD lump-sum reporting threshold", "The lump-sum reporting threshold for child-support obligors is not established from an official source."),
    (r"^The 4\.67% \(2027\) rate of initiative petition IP 25-18", "The rate and ballot status of initiative petition IP 25-18 are not established from an official source."),
    (r"^G\.S\. 95-25\.3\(b\) sets the full-time student", "The full-time student, learner, apprentice and messenger rate of G.S. 95-25.3(b) (ninety percent of the minimum wage) is not configured: no official NCDOL page states the rounded hourly figure."),
]


_NEUTRAL_RX = re.compile(r"(?:⚠️\s*)?RESEARCH-GAP\s*(\[\[GAP:[^\]]+\]\])?\s*")
NEUTRAL_LOG = []


def neutralize_markers(unit, text):
    """Replace each tagged RESEARCH-GAP marker by 'Not configured in this release [[GAP:id]]: <rule
    as far as established>'. A marker without a GAP tag is left (and logged) so C70 still sees it."""
    out = []
    for line in text.split("\n"):
        if "RESEARCH-GAP" not in line:
            out.append(line)
            continue
        segs = _segments(line)
        new, last = [], 0
        for s, e in segs:
            seg = line[s:e]
            new.append(line[last:s])
            last = e
            m = _NEUTRAL_RX.match(seg)
            if not m:
                NEUTRAL_LOG.append((unit, "untagged", seg[:120]))
                new.append(seg)
                continue
            if not m.group(1):
                # no gaps.json entry yet (e.g. an unresolved item added after gaps.json was written):
                # neutral wording without a tag, logged for agent 2 (C70 needs the entry only when the
                # text states a source gap with a C70 phrase)
                NEUTRAL_LOG.append((unit, "untagged", seg[:120]))
            tail = ""
            body = seg[m.end():]
            # keep the table-cell separator / trailing spaces that belonged to the segment
            mt = re.search(r"\s+$", body)
            if mt:
                tail, body = body[mt.start():], body[:mt.start()]
            body = clean_gap_body(body)
            if m.group(1):
                NEUTRAL_LOG.append((unit, "neutralized", m.group(1)))
            tag = f" {m.group(1)}" if m.group(1) else ""
            new.append(f"{NEUTRAL_PREFIX}{tag}" + (f": {body}" if body else ".") + tail)
        new.append(line[last:])
        out.append("".join(new))
    return "\n".join(out)


# ------------------------------------------------------ round 3: unit text fixes --
# text_fixes.json {unit: [{"find", "replace", "why"}]}: exact substring replacements applied in
# finalize() before tagging (outside [[...]] tags unless the find string spans a tag). Used for
# QA r2 wording findings in text that comes from fact notes or research-pack narrative.
_tf = os.path.join(HERE, "text_fixes.json")
TEXT_FIXES = json.load(open(_tf, encoding="utf-8")) if os.path.exists(_tf) else {}
TEXTFIX_LOG = []


def apply_text_fixes(unit, text):
    for r in TEXT_FIXES.get(unit, []) + TEXT_FIXES.get("*", []):
        find = r["find"]
        if r.get("regex"):
            text, n = re.subn(find, r["replace"], text)
            TEXTFIX_LOG.append((unit, find[:80], n))
            continue
        if "[[" in find:
            n = text.count(find)
            text = text.replace(find, r["replace"])
        else:
            parts = re.split(r"(\[\[(?:FACT|GAP):[^\]]*\]\])", text)
            n = sum(parts[i].count(find) for i in range(0, len(parts), 2))
            for i in range(0, len(parts), 2):
                parts[i] = parts[i].replace(find, r["replace"])
            text = "".join(parts)
        TEXTFIX_LOG.append((unit, find[:80], n))
    return text


def tag_gaps(unit, text):
    out = []
    for ln_no, line in enumerate(text.split("\n"), 1):
        if "RESEARCH-GAP" not in line:
            out.append(line)
            continue
        if "RESEARCH-GAP` marks" in line or "RESEARCH-GAP marks" in line:
            out.append(line)        # explanatory sentence of an annex intro, handled by the generator
            continue
        segs = _segments(line)
        new, last, drop_line = [], 0, False
        for s, e in segs:
            seg = line[s:e]
            new.append(line[last:s])
            last = e
            if "[[GAP:" in seg:
                new.append(seg)
                continue
            gk = re.search(r"\s?\[\[GAPKEY:([a-z0-9_.]+)\]\]", seg)
            if gk:
                seg = seg.replace(gk.group(0), "")
                keys = [gk.group(1)]
            else:
                keys = _keys_in(seg, unit)
                if not keys and line.lstrip().startswith("|"):
                    # table-row marker in a value cell: the key sits in the first cell of the row
                    keys = _keys_in(line, unit)
                if not keys:
                    # open request raised after gaps.json (round 2) named in the marker text
                    rk = sorted({q["key"] for q in REQS.values() if q["key"] in seg}, key=len, reverse=True)
                    keys = rk[:1]
            if keys and (unit, keys[0]) in DECIDED:
                # open point settled by a recorded configuration decision: no marker
                GAP_LOG.setdefault("decided", []).append((unit, keys[0]))
                new.append(DECIDED[(unit, keys[0])])
                continue
            g = gap_entry(unit, keys[0]) if keys else None
            if g is None and not gk:
                # key named in the text but raised by another unit (e.g. Module 6 citing a Module 4 request)
                allk = sorted({x["key"] for x in GAPS}, key=len, reverse=True)
                hit = next((k for k in allk if re.search(r"(?<![A-Za-z0-9_.])" + re.escape(k) + r"(?![A-Za-z0-9_]|\.[A-Za-z0-9_])", seg)), None)
                if hit:
                    g = next(x for x in GAPS if x["key"] == hit)
            if g is None and gk:
                # key carried by the generator but not a gap of this unit: try any unit
                xs = [x for x in GAPS if x["key"] in (gk.group(1), alias(gk.group(1)))]
                g = xs[0] if xs else None
            if g is None:
                rid = GAP_TEXT_MAP.get(unit, {}).get(norm_marker(seg))
                g = next((x for x in GAPS if x["id"] == rid), None) if rid else None
            if g is None and keys:
                # open research request raised after gaps.json was written (round 2): tag with the
                # request id and log it so agent 2 adds the gaps.json entry
                q = next((q for q in REQS.values() if q["key"] in (keys[0], alias(keys[0]))
                          and str(q.get("_status", "open")).startswith("open")), None)
                if q:
                    g = {"id": q["id"], "status": "open", "_request_only": True}
                    GAP_LOG.setdefault("request_only", []).append((unit, q["id"], q["key"]))
            if g is None:
                if gk:
                    ck = gk.group(1) if gk.group(1) in CLOSED_KEYS.get(None, set()) else None
                else:
                    ck = _closed_key_in(seg, unit)
                if ck:
                    GAP_LOG["dropped"].append((unit, ln_no, ck))
                    if line.lstrip().startswith("|"):
                        new.append("see the rule in this table")
                    else:
                        drop_line = True
                    continue
                GAP_LOG["unmapped"].append((unit, ln_no, seg[:160]))
                new.append(seg)
                continue
            if g.get("status") == "documented_limitation":
                GAP_LOG["limitation"].append((unit, g["id"]))
                new.append(_limitation_text(g, seg))
                continue
            GAP_LOG["tagged"].append((unit, g["id"]))
            m = re.match(re.escape(MARK) + "|RESEARCH-GAP", seg)
            new.append(seg[:m.end()] + f" [[GAP:{g['id']}]]" + seg[m.end():])
        new.append(line[last:])
        if drop_line and not "".join(new).strip("-* ").strip():
            continue
        if drop_line:
            # marker removed from a prose line; keep the rest of the line if any
            rest = "".join(new).rstrip()
            if re.fullmatch(r"[-*\s]*", rest):
                continue
            out.append(rest)
            continue
        out.append("".join(new))
    return "\n".join(out)


# ----------------------------------------------------------- internal paths --
_PATH_RULES = [
    (re.compile(r"\s*\(`?00-official-sources/legal-basis-register\.csv`?\)"), ""),
    # NY-WY intro sentence
    (re.compile(r"Every value in this annex is bound to a key of `?_research/CCG-annex_[A-Z]+-facts\.json`? and carries"),
     "Every value in this annex is bound to a verified fact and carries"),
    (re.compile(r"\(open item `([^`]+)` in CCG-[A-Za-z0-9_]+-facts\.json;"), r"(open item `\1`;"),
    (re.compile(r" in `?(?:_research/)?(?:CCG|WTC|PSL|SIR|RSPEC|DD)-[A-Za-z0-9_-]+-facts\.json`?"), ""),
    (re.compile(r"`?_research/[A-Za-z0-9_./-]+`?"), "the research record"),
    (re.compile(r"`?(?:CCG|WTC|PSL|SIR|RSPEC|DD)-[A-Za-z0-9_-]+-facts\.json`?"), "the research record"),
    (re.compile(r"`?(?:01-ccg|_pipeline|_validation|00-official-sources)/[A-Za-z0-9_./-]+`?"), "the build record"),
    (re.compile(r"`?build_examples(?:_[A-Za-z0-9_-]+)?\.py`?"), "the example calculator"),
]
INTERNAL_RX = re.compile(r"_research/|-facts\.json|01-ccg/|_pipeline/|build_examples|\.py\b")


def strip_internal(text):
    parts = re.split(r"(\[\[(?:FACT|GAP):[^\]]*\]\])", text)
    for i in range(0, len(parts), 2):
        for rx, rep in _PATH_RULES:
            parts[i] = rx.sub(rep, parts[i])
    return "".join(parts)


# ---------------------------------------------------------- percent tagging --
_pt = os.path.join(HERE, "percent_tags.json")
PERCENT_TAGS = json.load(open(_pt, encoding="utf-8")) if os.path.exists(_pt) else {}
PCT_LOG = []


def tag_percents(unit, text):
    """Apply percent_tags.json: {unit: [{"find": "...", "replace": "..."}]} - exact substring
    replacements outside existing tags; each replacement writes [[FACT:key=value]] whose value
    is checked against the facts files by validate_percent_tags()."""
    for r in PERCENT_TAGS.get(unit, []):
        find = r["find"]
        if "[[FACT:" in find:
            # the find string itself spans a tag: plain replacement
            n = text.count(find)
            text = text.replace(find, r["replace"])
        else:
            # never edit inside an existing [[FACT:]] / [[GAP:]] tag (fact values stay verbatim)
            parts = re.split(r"(\[\[(?:FACT|GAP):[^\]]*\]\])", text)
            n = sum(parts[i].count(find) for i in range(0, len(parts), 2))
            for i in range(0, len(parts), 2):
                parts[i] = parts[i].replace(find, r["replace"])
            text = "".join(parts)
        PCT_LOG.append((unit, find if n else "NOT FOUND: " + find, n))
    return autotag_percents(unit, text)


# percent facts by value, per jurisdiction prefix (rates stored in percent, unit_of_measure percent)
PCT_FACTS = {}
for _fp in glob.glob(os.path.join(RES, "*-facts.json")):
    for _f in json.load(open(_fp, encoding="utf-8")).get("facts", []):
        _v = _f.get("value")
        if isinstance(_v, bool) or not isinstance(_v, (int, float)):
            continue
        if _f.get("unit_of_measure") == "percent" or re.search(r"(^|\.)(rate|percent|pct)(\.|_|$)", _f["key"]):
            PCT_FACTS.setdefault((_f["key"].split(".")[0], round(float(_v), 6)), set()).add(_f["key"])
PCT_RX = re.compile(r"(?<![\w.,/])(\d{1,3}(?:\.\d+)?)(\s?%| percent\b)")


def _sigdigits(x):
    return len(f"{abs(x):.10f}".replace(".", "").lstrip("0").rstrip("0"))


def autotag_percents(unit, text):
    """Annex units: a distinctive percentage (decimal part or 3+ significant digits, the C46
    distinctiveness rule) written untagged is bound to the one fact of the same jurisdiction
    with that value. Ambiguous or cross-jurisdiction matches are left to percent_tags.json;
    contexts listed in percent_tags.json "_exclude" are never auto-tagged (coincidental numbers)."""
    m = re.match(r"annex_([A-Z]+)\.md$", unit)
    if not m:
        return text
    jur = m.group(1).lower()
    excl = [e["contains"] for e in PERCENT_TAGS.get("_exclude", []) if e["unit"] == unit]
    out = []
    for ln in text.split("\n"):
        if ln.startswith("#") or any(c in ln for c in excl):
            out.append(ln)
            continue
        parts = re.split(r"(\[\[(?:FACT|GAP):[^\]]*\]\])", ln)
        for i in range(0, len(parts), 2):
            def rep(mo):
                s = mo.group(1)
                n = float(s)
                if n == 0 or not ("." in s or _sigdigits(n) >= 3):
                    return mo.group(0)
                keys = PCT_FACTS.get((jur, round(n, 6)), set())
                if len(keys) != 1:
                    return mo.group(0)
                k = next(iter(keys))
                PCT_LOG.append((unit, f"auto {s}% -> {k}", 1))
                return f"[[FACT:{k}={s}]]{mo.group(2)}"
            parts[i] = PCT_RX.sub(rep, parts[i])
        out.append("".join(parts))
    return "\n".join(out)


# ------------------------------------------------------------ annex skeleton --
SKELETON = [
    ("1", "Employment and labour code"),
    ("2", "Income tax withholding"),
    ("2b", "Non-resident regime and reciprocity"),
    ("2c", "Local wage taxes"),
    ("3", "Social insurance: unemployment, disability, paid leave and payroll levies"),
    ("4", "Pay statement"),
    ("5", "Statutory reporting"),
    ("6", "Leave"),
    ("7", "Termination and final pay"),
    ("8", "Benefits in kind and taxable wages"),
    ("9", "Deductions and garnishments"),
    ("10", "Collective agreements and prevailing wage"),
    ("11", "Indexation"),
    ("12", "Payroll data protection and records"),
    ("13", "Live legal change"),
    ("14", "Authority worked examples (oracle values)"),
    ("15", "Special populations"),
    ("16", "Language"),
    ("S", "Sources"),
]
SKELETON_IDS = [s for s, _ in SKELETON]
EMPTY_TEXT = {
    "2b": "The non-resident and reciprocity rules of this jurisdiction are written in {J}.2.",
    "2c": "The local wage taxes of this jurisdiction, where any exist, are written in {J}.2.",
    "14": "No authority worked example is reproduced in this annex; recomputed withholding examples are in Module 12.",
    "16": "No language rule for employee documents is written for this jurisdiction in this annex.",
    "S": "The legal basis of each value (legal-basis register id, authority, source tier and verification method) is given in the row that carries it.",
}


def annex_skeleton(jur, title, intro, sections, empty_text=None):
    """Render one annex in the single skeleton.

    jur      jurisdiction code (FED, MULTI, AK ...)
    title    jurisdiction name ("New York")
    intro    list of lines written under the H1 before the first section
    sections dict skeleton id -> list of body lines (may be missing / empty)
    """
    et = dict(EMPTY_TEXT)
    et.update(empty_text or {})
    L = [f"# Annex {jur}: {title}", ""]
    L += list(intro)
    if L[-1] != "":
        L.append("")
    for sid, name in SKELETON:
        L += [f"## {jur}.{sid} {name}", ""]
        body = sections.get(sid) or []
        while body and not body[0].strip():
            body = body[1:]
        while body and not body[-1].strip():
            body = body[:-1]
        if not body:
            body = [et.get(sid, "No rule for this jurisdiction is written under this heading.").replace("{J}", jur)]
        L += body + [""]
    return "\n".join(L).rstrip("\n") + "\n"


def split_sections(text):
    """Split an annex markdown on its H2 headings -> (h1 line, intro lines, [(h2 title, lines)])."""
    lines = text.split("\n")
    h1, intro, secs, cur = None, [], [], None
    for ln in lines:
        if ln.startswith("# ") and h1 is None:
            h1 = ln
            continue
        if ln.startswith("## "):
            cur = (ln[3:].strip(), [])
            secs.append(cur)
            continue
        (cur[1] if cur else intro).append(ln)
    return h1, intro, secs


# annex numbering of each builder scheme -> skeleton id ("intro:<label>" = lead-in paragraph of the intro)
MAP_FED_CT = {s: s for s in SKELETON_IDS}            # FED-CT and DC-MA scheme = the skeleton (22 of 53 annexes)
MAP_MD_NV = {"0": "intro:Scope of this annex", "1": "intro:Jurisdiction layer", "2": "intro:Configuration decisions",
             "3": "1", "4": "2", "5": "2b", "6": "2c", "7": "3", "8": "4", "9": "5", "10": "6", "11": "7",
             "12": "8", "13": "9", "14": "10", "15": "11", "16": "12", "17": "13", "18": "15", "19": "16",
             "20": "S"}
MAP_NY_WY = {"1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9",
             "10": "10", "11": "11", "12": "12", "13": "13", "14": "15", "15": "S"}
ANNEX_LOG = []


def normalize_annex(unit_file, text, idmap, renumber_refs=False):
    """Re-render an annex in the single skeleton (QA r1 finding 51). Section bodies are kept
    verbatim; only H1/H2 lines change, missing sections get a structural sentence, and (MD-NV)
    in-text references to the builder's old section numbers are re-pointed."""
    jur = re.match(r"annex_([A-Z]+)\.md", unit_file).group(1)
    h1, intro, secs = split_sections(text)
    m = re.match(r"#\s+Annex\s+[A-Z]+\s*(?::|-|–|—)\s*(.+)$", h1 or "")
    title = m.group(1).strip() if m else jur
    sections, extra_intro, seen = {}, [], []
    for t, lines in secs:
        mm = re.match(r"(?:" + jur + r"\.)?([0-9]+[a-z]?|S)\.?\s", t + " ")
        old = mm.group(1) if mm else None
        sid = idmap.get(old) if old else None
        if sid is None:
            raise ValueError(f"{unit_file}: section {t!r} has no skeleton id")
        seen.append((old, sid))
        if sid.startswith("intro:"):
            body = list(lines)
            while body and not body[0].strip():
                body = body[1:]
            extra_intro += [f"**{sid[6:]}.**", ""] + body
            continue
        if sid in sections:
            sections[sid] += [""] + list(lines)
        else:
            sections[sid] = list(lines)
    intro = [ln for ln in intro] + extra_intro
    out = annex_skeleton(jur, title, intro, sections)
    if renumber_refs:
        ref = {o: s for o, s in seen if not s.startswith("intro:")}

        def rep(mo):
            o = mo.group(1)
            if o in ref:
                return f"{jur}.{ref[o]}"
            return mo.group(0)
        body = out.split("\n")
        for i, ln in enumerate(body):
            if ln.startswith("#"):
                continue
            parts = re.split(r"(\[\[(?:FACT|GAP):[^\]]*\]\])", ln)
            for j in range(0, len(parts), 2):
                parts[j] = re.sub(r"\b" + jur + r"\.([0-9]+)\b(?!\.[0-9])", rep, parts[j])
            body[i] = "".join(parts)
        out = "\n".join(body)
    ANNEX_LOG.append((unit_file, [o + "->" + s for o, s in seen]))
    return out


# ---------------------------------------------------------------- finalize --
_PRIOR = re.compile(r"\b(?:20(?:1\d|2[0-5])): (?:USD )?\d[\d,]*(?:\.\d+)?(?: ?%)?(?:\s*/\s*\d[\d,]*(?:\.\d+)?(?: ?%)?)?(?:;\s*|\.\s+|\.(?=\s*\|)|(?=\s*\|))")
PRIOR_LOG = []


def strip_prior_year(unit, text):
    """QA r1 finding 49 / fix 6: configuration tables show in-force values only. Fact notes that
    still carry an untagged prior-year comparison ("2025: 72,800") lose it; the history stays in
    the facts files (_history) and the register."""
    out = []
    for ln in text.split("\n"):
        if ln.lstrip().startswith("|"):
            parts = re.split(r"(\[\[(?:FACT|GAP):[^\]]*\]\])", ln)
            for i in range(0, len(parts), 2):
                n = len(_PRIOR.findall(parts[i]))
                if n:
                    PRIOR_LOG.append((unit, parts[i][:80]))
                    parts[i] = _PRIOR.sub("", parts[i])
            ln = "".join(parts)
        out.append(ln)
    return "\n".join(out)


_gpt = os.path.join(HERE, "gap_phrase_tags.json")
GAP_PHRASES = json.load(open(_gpt, encoding="utf-8")) if os.path.exists(_gpt) else {}
C70_PHRASE = re.compile(r"\b(not obtained|could not be obtained|not retrievable|could not be retrieved|was not available)\b", re.I)


def tag_gap_phrases(unit, text):
    """C70: a source-gap statement outside a RESEARCH-GAP marker ("... not obtained") carries the
    [[GAP:<id>]] of its research request (gap_phrase_tags.json: {unit: [{find, gap | key, replace?}]});
    'replace' rewords a statement that is not a gap of its own (the value is sourced elsewhere)."""
    for r in GAP_PHRASES.get(unit, []):
        if r["find"] not in text:
            GAP_LOG.setdefault("phrase_not_found", []).append((unit, r["find"][:60]))
            continue
        if "replace" in r:
            text = text.replace(r["find"], r["replace"])
            continue
        gid = r.get("gap")
        if not gid and r.get("key"):
            q = next((q for q in REQS.values() if q["key"] == r["key"]), None)
            gid = q["id"] if q else None
        if gid and f"{r['find']} [[GAP:{gid}]]" not in text:
            text = text.replace(r["find"], f"{r['find']} [[GAP:{gid}]]")
            GAP_LOG["tagged"].append((unit, gid))
    left = [ln[:120] for ln in text.split("\n") if C70_PHRASE.search(_TAGRX.sub("", ln)) and "[[GAP:" not in ln]
    if left:
        GAP_LOG.setdefault("c70_phrase_untagged", []).extend((unit, x) for x in left)
    return text


def finalize(unit_file, text, annex=False):
    before = {k: len(v) for k, v in GAP_LOG.items()}
    npct = len(PCT_LOG)
    npr = len(PRIOR_LOG)
    ntf = len(TEXTFIX_LOG)
    nnl = len(NEUTRAL_LOG)
    text = strip_prior_year(unit_file, text)
    text = apply_text_fixes(unit_file, text)
    text = tag_percents(unit_file, text)
    text = tag_gaps(unit_file, text)
    text = tag_gap_phrases(unit_file, text)
    text = neutralize_markers(unit_file, text)
    text = strip_internal(text)
    os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
    rec = {k: v[before.get(k, 0):] for k, v in GAP_LOG.items()}
    rec["percent_tags"] = PCT_LOG[npct:]
    rec["prior_year_removed"] = PRIOR_LOG[npr:]
    rec["text_fixes"] = TEXTFIX_LOG[ntf:]
    rec["markers_neutralized"] = len([x for x in NEUTRAL_LOG[nnl:] if x[1] == "neutralized"])
    rec["markers_left_untagged"] = [x for x in NEUTRAL_LOG[nnl:] if x[1] == "untagged"]
    rec["internal_path_hits_left"] = [ln[:160] for ln in text.split("\n") if INTERNAL_RX.search(_TAGRX.sub("", ln))]
    json.dump(rec, open(os.path.join(HERE, "out", f"finalize_{unit_file}.json"), "w", encoding="utf-8"),
              indent=1, ensure_ascii=False)
    return text


def write_logs(path):
    json.dump({"gaps": {k: len(v) for k, v in GAP_LOG.items()}, "gap_detail": GAP_LOG,
               "percent_tags": PCT_LOG}, open(path, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
