# -*- coding: utf-8 -*-
"""Build CCG jurisdiction annexes (NY..WY) from facts + hand-written narrative.

Usage: python build.py [--states NY,OH] [--assign-rq]
 - Narrative sources: src/{ST}.md, sections '## @<domain>' ; placeholders:
     {{key}}            -> [[FACT:key=value]] (key must be unique, or the first/only dated value)
     {{key@YYYY-MM-DD}} -> the dated value whose effective_from matches
 - Every fact of the facts file appears in the domain parameter table (100 % carried).
 - Every unresolved[] item becomes a RESEARCH-GAP marker in its domain + a request item.
 - Research requests are appended to _research/CCG-research-request.json (re-read before write).
"""
import json, re, sys, os, argparse, datetime, glob
from decimal import Decimal

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HERE, "..", ".."))
RES = os.path.join(BASE, "_research")
OUT = os.path.join(BASE, "01-ccg", "annexes")
sys.path.insert(0, os.path.join(BASE, "01-ccg", "_build", "common"))
import ccg_common as CC  # noqa: E402  round 2 (QA r1): finalize, annex skeleton, [[GAP:]] tags
RQ_FILE = os.path.join(RES, "CCG-research-request.json")
RQMAP = os.path.join(HERE, "rq-map.json")
TODAY = "2026-11-02"
STATES = "NY OH OK OR PA RI SC SD TN TX UT VA VT WA WI WV WY".split()
NAMES = {"NY": "New York", "OH": "Ohio", "OK": "Oklahoma", "OR": "Oregon", "PA": "Pennsylvania",
         "RI": "Rhode Island", "SC": "South Carolina", "SD": "South Dakota", "TN": "Tennessee",
         "TX": "Texas", "UT": "Utah", "VA": "Virginia", "VT": "Vermont", "WA": "Washington",
         "WI": "Wisconsin", "WV": "West Virginia", "WY": "Wyoming"}
# Layer classification, quoted from build-manifest.json -> tier.rationale (re-checked 2026-10-30, seal attempt 5)
LAYER = {
    "T1": "T1 - no state wage tax; SUI and levies only",
    "T3": "T3 - state withholding; local layer absent or piggybacked on the state return",
    "T4": "T4 - local layer remitted to the locality on its own return",
}
TIER = {"NY": "T3", "OH": "T4", "OK": "T3", "OR": "T4", "PA": "T4", "RI": "T3", "SC": "T3", "SD": "T1",
        "TN": "T1", "TX": "T1", "UT": "T3", "VA": "T3", "VT": "T3", "WA": "T1", "WI": "T3", "WV": "T4", "WY": "T1"}
TIER_NOTE = {
    "NY": "NYC and Yonkers taxes are piggybacked on NYS-1 / NYS-45 [US-NY-008].",
    "OH": "Ohio municipal income tax, ORC 718.03 [US-OHP52-003].",
    "OR": "City of Portland Metro SHS / Multnomah PFA [US-ORS5-004].",
    "PA": "Pennsylvania Act 32 EIT/LST to the local collector [US-PA-004].",
    "WV": "Municipal service fees withheld and remitted to the city, W. Va. Code 8-13-13 [US-WVR3-001], Charleston [US-WVR3-002].",
    "WA": "The Seattle payroll expense tax, a threshold-conditional employer tax on a city return [US-WAP51-001], is declared as a T4-shaped element.",
}

DOMAINS = [
    ("labour", "1. Labour code and pay rules", "labour_code"),
    ("income_tax", "2. Income tax withholding (state and local)", "income_tax"),
    ("social", "3. Social insurance and payroll levies", "social_security"),
    ("payslip", "4. Payslip statute and payroll records", "payslip_statute"),
    ("reporting", "5. Statutory reporting", "statutory_reporting"),
    ("leave", "6. Leave", "leave"),
    ("termination", "7. Termination", "termination"),
    ("bik", "8. Benefits in kind and the taxable base", "benefits_in_kind"),
    ("deductions", "9. Deductions and garnishments", "deductions_garnishments"),
    ("cba", "10. Collective agreements and prevailing wage", "collective_agreements"),
    ("indexation", "11. Indexation", "indexation"),
    ("data", "12. Payroll data protection", "payroll_data_protection"),
    ("live", "13. Live legal change", "live_legal_change"),
    ("special", "14. Special populations", None),
]
SEG2DOM = {
    "labour": "labour", "minwage": "labour", "overtime": "labour", "exempt": "labour", "pay_frequency": "labour",
    "payment": "labour", "local_mandates": "labour", "local": "income_tax",  # r2: xx.local.* = local wage taxes
    "wh": "income_tax", "pit": "income_tax", "reciprocity": "income_tax", "local_wage_tax": "income_tax",
    "sui": "social", "ui": "social", "pfl": "social", "dbl": "social", "pfml": "social", "tdi": "social",
    "ui_tdi": "social", "sdi_pfml": "social", "stt": "social", "transit": "social", "wbf": "social",
    "ltc": "social", "cares": "social", "ccc": "social", "wc": "social", "rates": "social", "ui_pfml_ltc": "social",
    "payslip": "payslip", "records": "payslip",
    "report": "reporting", "newhire": "reporting",
    "leave": "leave", "final_pay": "termination", "term": "termination",
    "bik": "bik", "garn": "deductions", "deduction": "deductions",
    "prevailing_wage": "cba", "data": "data", "live": "live",
}
DOM_ENUM = {d[0]: d[2] for d in DOMAINS}
TITLE = {d[0]: d[1] for d in DOMAINS}


DROPPED = []
_FORMS = None
# F44 final (QA r3b minor UT): oracle scenario inputs (frequency, status, wages) are inputs, not statutory values;
# keep the note even when a number collides with an unrelated fact value (175 = AL married reduction per step).
KEEP_NOTE_KEYS = {"ut.pit.oracle.example_6.withholding"}
# QA r3c finding 2: the new scenario-input fact ut.pit.oracle.example_6.wages carries a note whose source sentence
# is a local file path (dropped by sanitize) and whose remainder names a key; the cell states what the value is.
NOTE_OVERRIDE = {
                 "ut.pit.base_allowance.single.annual": "Period start 2026-04-01; Pub. 14 Rev. 04/26 (revision dated April 2026); effective date not stated. 2026-01-01 to 2026-03-31: Not configured in this release [[GAP:RQ-596]]",
                 "ut.pit.base_allowance.married.annual": "Period start 2026-04-01; Pub. 14 Rev. 04/26 (revision dated April 2026); effective date not stated. 2026-01-01 to 2026-03-31: Not configured in this release [[GAP:RQ-596]]",
                 "ut.pit.phaseout_threshold.single.annual": "Period start 2026-04-01; Pub. 14 Rev. 04/26 (revision dated April 2026); effective date not stated. 2026-01-01 to 2026-03-31: Not configured in this release [[GAP:RQ-596]]",
                 "ut.pit.phaseout_threshold.married.annual": "Period start 2026-04-01; Pub. 14 Rev. 04/26 (revision dated April 2026); effective date not stated. 2026-01-01 to 2026-03-31: Not configured in this release [[GAP:RQ-596]]",
                 "ut.pit.phaseout.rate": "Period start 2026-04-01; Pub. 14 Rev. 04/26 (revision dated April 2026); effective date not stated. 2026-01-01 to 2026-03-31: Not configured in this release [[GAP:RQ-596]]",
                 "ut.pit.oracle.example_6.wages":
                 "Utah taxable wages of the daily, married worked example (input of the withholding row below)."}


# QA r3d finding 4: the bare HTTP status pattern was '\b40[34]\b', which also matched statute section numbers
# ('T.C.A. 50-7-402 and 50-7-403') and dropped the quoted clause of the TN note. It now matches only a
# status code that stands alone (not inside a hyphenated / dotted section number). INTERNAL_STRICT holds the
# phrases that are pipeline wording in any context; a clause carrying a legal citation or quoted statute
# text (CC.LEGAL_CITE_RX) is dropped only for those, never for the looser words of INTERNAL.
INTERNAL = re.compile(r"R\d 20\d\d|effective_from|local copy|script shell|(?:returned|HTTP)[^.;]{0,40}\bbytes?\b|webfetch|summari[sz]er|verification is weak|wayback|\bMANUAL\b|tier[- ]B\b|synthesis|stage[- ]?5|\bpython\b|\bOQ-|\bQ\d\b|\bcurl\b|HTTP \d{3}|\(40[34]\)|(?<![-.§\w])40[34](?![-\w(]|\.\w)|research pack|register row|\bpartial\b|superseded|G-DERIVE|legacy|browser pass|chrome pass|\bVPN\b|US-MQ-|derived arithmetically|internal conflict|\bpp\.\s?\d|\bFAQ\s?\d", re.I)
INTERNAL_STRICT = re.compile(r"R\d 20\d\d|effective_from|local copy|script shell|(?:returned|HTTP)[^.;]{0,40}\bbytes?\b|webfetch|summari[sz]er|wayback|\bMANUAL\b|tier[- ]B\b|synthesis|stage[- ]?5|\bpython\b|\bOQ-|\bcurl\b|HTTP \d{3}|research pack|register row|G-DERIVE|browser pass|chrome pass|\bVPN\b|US-MQ-", re.I)


def tag_scenario_inputs(f, note, facts):
    """QA r3c finding 2: a kept scenario note prints its inputs (UT example 6 'daily married 175'); a number that is
    the value of a sibling fact of the same scenario (same key prefix, e.g. ut.pit.oracle.example_6.wages) is
    written as that fact's tag, so no fact value stays untagged (C46)."""
    prefix = f["key"].rsplit(".", 1)[0] + "."
    for sib in facts:
        if sib["key"] == f["key"] or not sib["key"].startswith(prefix):
            continue
        v = sib.get("value")
        if isinstance(v, bool) or not isinstance(v, (int, float)):
            continue
        sv = fmt_value(sib)
        parts = re.split(r"(\[\[(?:FACT|GAP):[^\]]*\]\])", note)
        for i in range(0, len(parts), 2):
            parts[i] = re.sub(rf"(?<![\d.,]){re.escape(sv)}(?![\d.,]*\d)", tag(sib), parts[i])
        note = "".join(parts)
    return note


def sanitize(text, fallback=""):
    """Drop clauses that carry pipeline-internal wording (C47: no history or process in the deliverable)."""
    if not text:
        return text
    text = re.sub(r"\s*\((?:local copy|retrieved)[^)]*\)", "", text)       # a parenthetical retrieval stamp is dropped, the name stays
    parts = re.split(r"(?<=[;.])\s+", text)
    keep = [p for p in parts if not (INTERNAL_STRICT if CC.LEGAL_CITE_RX.search(p) else INTERNAL).search(p)]
    out = " ".join(keep).strip().rstrip(";").strip()
    return out if out else fallback


_REG = None


def _register():
    global _REG
    if _REG is None:
        import csv
        with open(os.path.join(BASE, "00-official-sources", "legal-basis-register.csv"), encoding="utf-8", newline="") as fh:
            _REG = {r["id"]: r for r in csv.DictReader(fh)}
    return _REG


# v1.1 QA r1 (F27 regression, OK/VT): the ~660 New York per-period Method II values (NYS-50-T tables) made the guard
# drop notes of other States whose numbers merely coincide with a table cell (OK married base amounts 57.50 / 218.50,
# VT Saves penalty notes). A number that equals only a NY per-period table value is not a value of the other State's
# own facts, so for a State other than NY those forms are ignored by the guard.
NY_PER_PERIOD = ("ny.wh.method2.", "ny.local.nyc.method2.", "ny.local.nyc.wh.method2.", "ny.wh.conversion.")


def note_collides(text, st=None):
    """True if the note carries a number that C46 would treat as an unbound fact value."""
    global _FORMS
    sys.path.insert(0, os.path.expanduser("~/mercans-pipeline/shared/consistency-checks"))
    import consistency_checks as cc
    if _FORMS is None:
        _FORMS = {}
        for fp in glob.glob(os.path.join(RES, "*-facts.json")):
            for f in json.load(open(fp, encoding="utf-8")).get("facts", []):
                for n, pct in cc.distinctive_forms(f["key"], f.get("value")):
                    _FORMS.setdefault((round(n, 6), pct), set()).add(f["key"])
    for m in cc.NUM_IN_TEXT.finditer(text):
        n = cc._num(m.group(1))
        keys = _FORMS.get((round(n, 6), bool(m.group(2)))) if n is not None else None
        if not keys:
            continue
        if st and st != "NY" and all(k.startswith(NY_PER_PERIOD) for k in keys):
            continue
        return True
    return False


def dom_of(key):
    return SEG2DOM.get(key.split(".")[1], "live")


def load(st):
    return json.load(open(os.path.join(RES, f"CCG-annex_{st}-facts.json"), encoding="utf-8"))


def fmt_value(f):
    """Readable but numerically identical form for the tag (C46 compares numerically
    for numbers, exactly for strings)."""
    v = f["value"]
    if isinstance(v, bool):
        return str(v)
    if isinstance(v, (int, float)):
        d = Decimal(repr(v)) if isinstance(v, float) else Decimal(v)
        cur = f.get("currency")
        if cur == "USD" and isinstance(v, float) and d.as_tuple().exponent >= -2:
            s = f"{d:,.2f}"
        else:
            s = format(d.normalize(), "f") if d == d.to_integral_value() else format(d, "f")
            if d == d.to_integral_value():
                s = f"{int(d):,}" if abs(int(d)) >= 10000 else str(int(d))
        return s
    return str(v)


def tag(f):
    v = fmt_value(f)
    if "]" in v:
        raise ValueError(f"value of {f['key']} contains ']' - cannot be tagged")
    return f"[[FACT:{f['key']}={v}]]"


def unit_of(f):
    u = f.get("unit_of_measure") or ""
    cur = f.get("currency")
    if u in ("percent", "%"):
        return "%"
    if cur and u:
        return f"{cur} ({u})"
    return cur or u or ""


def period(f):
    import deliverable_wording as DW     # v1.1 QA r1: a proposed or historical register row is never shown as an in-force date
    a, b = f.get("effective_from"), f.get("effective_to")
    st = DW.period_cell(f)
    if st:
        return st
    if a and b:
        return f"{a} to {b}"
    if a:
        return f"from {a}"
    return "undated (see note)"


def clean_cell(s):
    return str(s).replace("|", "/").replace("\n", " ").strip()


def render(st, rqmap, gaps_out, bind_log):
    d = load(st)
    facts = d["facts"]
    by_key = {}
    for f in facts:
        by_key.setdefault(f["key"], []).append(f)
    src = open(os.path.join(HERE, "src", f"{st}.md"), encoding="utf-8").read()
    # split narrative
    parts = re.split(r"^## @(\w+)\s*$", src, flags=re.M)
    head = parts[0].strip()
    narr = {parts[i]: parts[i + 1].strip() for i in range(1, len(parts), 2)}
    gap_over = {}
    for line in narr.pop("gaps", "").splitlines():
        line = line.strip()
        if line.startswith("- "):
            k, why, close = [x.strip() for x in line[2:].split("::")]
            gap_over[k] = (why, close)
    for k in narr:
        if k not in TITLE and k not in ("intro",):
            raise SystemExit(f"{st}: unknown section @{k}")
    used = set()

    def sub(m):
        k, dt = m.group(1), m.group(2)
        if k not in by_key:
            raise SystemExit(f"{st}: placeholder key not in facts: {k}")
        cands = by_key[k]
        if dt:
            cands = [f for f in cands if f.get("effective_from") == dt]
            if len(cands) != 1:
                raise SystemExit(f"{st}: no unique dated value {k}@{dt}")
        elif len(cands) > 1:
            # QA r3d (agent 2 split a key into two periods with the SAME value, e.g. OH 4141.23 versions): the
            # narrative states the value once; it binds to the period in force on 2026-06-30. Different values
            # still need {{key@date}}.
            if len({json.dumps(f.get("value")) for f in cands}) == 1:
                mid = [f for f in cands if (f.get("effective_from") or "0000") <= "2026-06-30" <= (f.get("effective_to") or "9999")]
                cands = mid or cands[:1]
                print(f"{st}: {k} has {len(by_key[k])} dated values with one value; narrative bound to {cands[0].get('effective_from')}")
            else:
                raise SystemExit(f"{st}: key {k} has {len(cands)} dated values - use {{{{{k}@date}}}}")
        used.add((k, cands[0].get("effective_from")))
        return tag(cands[0])

    ph = re.compile(r"\{\{([a-z0-9_.]+)(?:@(\d{4}-\d{2}-\d{2}))?\}\}")
    unres = d.get("unresolved", [])
    gaps_by_dom = {}
    for u in unres:
        gaps_by_dom.setdefault(dom_of(u["key"]), []).append(u)
    facts_by_dom = {}
    for f in facts:
        dm = dom_of(f["key"])
        facts_by_dom.setdefault(dm, []).append(f)

    rel = f"01-ccg/annexes/annex_{st}.md"
    L = []
    L.append(f"# Annex {st} - {NAMES[st]}")
    L.append("")
    L.append(f"Jurisdiction annex of the United States Country Configuration Guide (US-CCG-001). "
             f"Layer classification: **{LAYER[TIER[st]]}** (build manifest, tier rationale). {TIER_NOTE.get(st, '')}".rstrip())
    L.append("")
    L.append("The federal layer (federal income tax withholding, FICA, FUTA, Forms W-2, 941 and 940) and the multistate "
             "rules (residence and work-location sourcing, reciprocity mechanics) are in Annex FED and Annex MULTI and are not repeated here. "
             + CC.CONTRACTOR_SENTENCE + " Payslip language: English; "
             "second-language duties attach to notices and posters only (US-OWN-006).")
    L.append("")
    L.append("Every value in this annex is bound to a verified fact and carries its "
             "legal-basis register id. A value that changes during the year is shown with its effective dates. "
             "A point marked as a research gap has not been closed by the research; it is not filled with an estimate.")
    L.append("")
    if head:
        L.append(ph.sub(sub, head))
        L.append("")
    if "intro" in narr:
        L.append(ph.sub(sub, narr["intro"]))
        L.append("")
    gap_count = [0, 0]
    for dk, title, enum in DOMAINS:
        L.append(f"## {title}")
        L.append("")
        if dk in narr and narr[dk]:
            L.append(ph.sub(sub, narr[dk]))
            L.append("")
        fs = facts_by_dom.get(dk, [])
        if fs:
            L.append(f"**Parameters ({TITLE[dk].split('. ', 1)[1].lower()})**")
            L.append("")
            L.append("| Parameter key | Value | Unit | Effective | Register id | Note |")
            L.append("|---|---|---|---|---|---|")
            for f in fs:
                try:
                    tv = tag(f)
                except ValueError:
                    tv = "see the rule text above (formula value carries brackets; components tagged there)"
                note = f.get("note") or ""
                if note in ("-", "—"):
                    note = ""
                note = sanitize(note)
                if f["key"] in NOTE_OVERRIDE:
                    note = NOTE_OVERRIDE[f["key"]]
                if note and note_collides(note, st) and f["key"] not in KEEP_NOTE_KEYS:
                    DROPPED.append((st, f["key"], note))
                    note = ""
                if note and f["key"] in KEEP_NOTE_KEYS:
                    note = tag_scenario_inputs(f, note, facts)
                L.append(f"| `{f['key']}` | {tv} | {clean_cell(unit_of(f))} | {period(f)} | {f['register_id']} | {clean_cell(note)} |")
                bind_log.append((rel, f"§{title.split('.')[0]} parameter table", f["key"], fmt_value(f) if "]" not in fmt_value(f) else "(formula)", f["register_id"], period(f)))
            L.append("")
        gs = gaps_by_dom.get(dk, [])
        if gs:
            L.append("**Open research points**")
            L.append("")
            for u in gs:
                rq = rqmap.get(f"{st}:{u['key']}", "RQ-?")
                blk = "blocking" if u.get("blocking") else "non-blocking"
                gap_count[0 if u.get("blocking") else 1] += 1
                why = u.get("why", "").strip().replace("\n", " ")
                close = u.get("what_would_close_it", "").strip().replace("\n", " ")
                why = sanitize(why, "Not established by the research.")
                close = sanitize(close, "an authority source (A.1 / A.2) for this point")
                if u["key"] in gap_over:
                    why, close = gap_over.pop(u["key"])
                    why, close = ph.sub(sub, why), ph.sub(sub, close)
                L.append(f"- ⚠️ RESEARCH-GAP: `{u['key']}` ({blk}; research request filed under this key) - {why} Closes with: {close}")
                gaps_out.append({"st": st, "u": u, "location": f"{rel}!{title}!open research points", "domain": enum or "labour_code"})
            L.append("")
    if gap_over:
        # round 2: an override whose key left unresolved[] (gap closed by agent 2 or a parallel worker)
        # is obsolete, not an error; listed so the src file can be cleaned
        closed = [k for k in gap_over if any(k == g.get("key") for g in json.load(open(
            os.path.join(RES, "CCG-research-request.json"), encoding="utf-8"))["requests"])]
        unknown = [k for k in gap_over if k not in closed]
        if unknown:
            raise SystemExit(f"{st}: gap overrides for unknown keys {unknown}")
        print(f"{st}: obsolete gap overrides (gap no longer open in the facts): {closed}")
    left = re.findall(r"\{\{[^}]*\}\}", "\n".join(L))
    if left:
        raise SystemExit(f"{st}: unresolved placeholders {left}")
    L.append("## 15. Sources")
    L.append("")
    L.append("Register ids cited in this annex resolve to `00-official-sources/legal-basis-register.csv`; the URL of each "
             "value is in the facts file. Authorities:")
    L.append("")
    auth = {}
    for f in facts:
        auth.setdefault(f.get("authority") or "(not stated)", set()).add(f["register_id"])
    # F44 final (QA r3b minor OH): a register id cited in the annex text but carried by no fact (e.g. US-OHS5-017
    # after oh.wh.supplemental.rate was re-pointed) stays in the Sources list, under its register authority.
    listed = set().union(*auth.values()) if auth else set()
    for rid in sorted(set(re.findall(r"\bUS-[A-Z0-9]+-\d+\b", chr(10).join(L))) - listed):
        row = _register().get(rid)
        if row:
            auth.setdefault(row.get("authority") or "(not stated)", set()).add(rid)
    for a in sorted(auth):
        shown = re.sub(r",?\s*via Wayback.*$", "", a, flags=re.I)
        shown = sanitize(shown, "(authority named in the register)")
        if note_collides(shown):
            shown = re.sub(r"\s*\(.*?\)", "", shown)
        if note_collides(shown):
            shown = "(authority named in the register row)"
        L.append(f"- {shown}: {', '.join(sorted(auth[a]))}")
    L.append("")
    txt = "\n".join(L).rstrip() + "\n"
    return txt, len(facts), gap_count, used


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--states", default=",".join(STATES))
    ap.add_argument("--assign-rq", action="store_true")
    ap.add_argument("--dry", action="store_true")
    a = ap.parse_args()
    sts = a.states.split(",")
    rqmap = json.load(open(RQMAP, encoding="utf-8")) if os.path.exists(RQMAP) else {}
    if a.assign_rq:
        assign(sts, rqmap)
        rqmap = json.load(open(RQMAP, encoding="utf-8"))
    summary = []
    allbind = []
    for st in sts:
        gaps, bind = [], []
        txt, nf, gc, used = render(st, rqmap, gaps, bind)
        allbind += bind
        if not a.dry:
            os.makedirs(OUT, exist_ok=True)
            txt = CC.finalize(f"annex_{st}.md", CC.normalize_annex(f"annex_{st}.md", txt, CC.MAP_NY_WY))
            open(os.path.join(OUT, f"annex_{st}.md"), "w", encoding="utf-8", newline="\n").write(txt)
        summary.append((st, nf, gc[0], gc[1], len(used)))
    json.dump(allbind, open(os.path.join(HERE, "bindings.json"), "w", encoding="utf-8"), indent=0, ensure_ascii=False)
    json.dump(DROPPED, open(os.path.join(HERE, "dropped-notes.json"), "w", encoding="utf-8"), indent=0, ensure_ascii=False)
    for s in summary:
        print("%s facts=%d gaps_blocking=%d gaps_nonblocking=%d narrative_keys=%d" % s)


def tier_for(close):
    return "A.1" if re.search(r"\b(text|statute|code|regulation|rule|CFR|NYCRR|ORC|Law|Act|section|R\.S\.|RCW|WAC|OAR|ORS)\b", close or "") else "A.2"


def assign(sts, rqmap):
    """Append one request per unresolved item not yet requested; re-read the shared file just before writing."""
    items = []
    for st in sts:
        d = load(st)
        for u in d.get("unresolved", []):
            mk = f"{st}:{u['key']}"
            if mk in rqmap:
                continue
            dk = dom_of(u["key"])
            title = TITLE[dk]
            items.append((mk, st, u, dk, title))
    if not items:
        return
    if os.path.exists(RQ_FILE):
        doc = json.load(open(RQ_FILE, encoding="utf-8"))
    else:
        doc = {"schema_version": "1.4.0", "artifact": "CCG", "requested_by": "artifact-builder", "round": 1,
               "created_on": TODAY, "requests": []}
    used = {r["id"] for r in doc.get("requests", [])}
    n = max([int(x[3:]) for x in used] + [0])
    new_reqs = []
    for mk, st, u, dk, title in items:
        n += 1
        rid = f"RQ-{n:03d}"
        why = (u.get("why") or "").strip()
        close = (u.get("what_would_close_it") or "").strip()
        q = f"For {NAMES[st]} ({st}), 2026 payroll: {why.rstrip('.')}. What does the official source state? Expected closing source: {close}"
        req = {
            "id": rid, "key": u["key"],
            "location": f"01-ccg/annexes/annex_{st}.md!{title}!open research points",
            "question": q,
            "why_blocking": (f"Annex {st} {title} cannot state this rule or value; it is written as a RESEARCH-GAP marker"
                             + (" and the facts file marks it blocking." if u.get("blocking") else " (non-blocking: the annex ships with the marker as a named limitation).")),
            "domain": DOM_ENUM[dk],
            "acceptable_tier": tier_for(close),
            "attempted_by_requester": [f"_research/CCG-annex_{st}-facts.json unresolved[] ({u['key']})",
                                        f"_research/CCG-annex_{st}-research-pack.md (Open questions)"] + list(u.get("attempted", [])),
            "severity": "blocker" if u.get("blocking") else "minor",
            "expected_shape": "a fact with this key, a value (number with unit or rule text), effective_from, and an active A.1/A.2 register row",
            "_unit": f"annex_{st}",
            "_blocking": bool(u.get("blocking")),
            "_placeholder_written": f"RESEARCH-GAP at 01-ccg/annexes/annex_{st}.md, {title}",
            "_raised_by": "artifact-builder (annexes NY-WY)",
        }
        new_reqs.append(req)
        rqmap[mk] = rid
    # re-read just before writing (parallel builders append to the same file)
    if os.path.exists(RQ_FILE):
        cur = json.load(open(RQ_FILE, encoding="utf-8"))
        cur_ids = {r["id"] for r in cur.get("requests", [])}
        mine = new_reqs
        if cur_ids != used:  # someone appended meanwhile: renumber mine after their max
            m = max([int(x[3:]) for x in cur_ids] + [0])
            for r in mine:
                m += 1
                old = r["id"]
                r["id"] = f"RQ-{m:03d}"
                for k2, v2 in list(rqmap.items()):
                    if v2 == old:
                        rqmap[k2] = r["id"]
        cur["requests"] = cur.get("requests", []) + mine
        doc = cur
    else:
        doc["requests"] += new_reqs
    json.dump(doc, open(RQ_FILE, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    json.dump(rqmap, open(RQMAP, "w", encoding="utf-8"), indent=1)


if __name__ == "__main__":
    main()
