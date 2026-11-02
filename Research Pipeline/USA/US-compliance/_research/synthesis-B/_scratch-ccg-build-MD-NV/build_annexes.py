# -*- coding: utf-8 -*-
"""Builds CCG jurisdiction annexes MD..NV from _research/CCG-annex_{JUR}-facts.json
(+ qualitative, number-free lines of the research pack). Every value is written as
[[FACT:key=value]]. Run: python -I build_annexes.py <BASE>"""
import json, os, re, sys, glob, collections

BASE = sys.argv[1]
JURS = {"MD": "Maryland", "ME": "Maine", "MI": "Michigan", "MN": "Minnesota", "MO": "Missouri",
        "MS": "Mississippi", "MT": "Montana", "NC": "North Carolina", "ND": "North Dakota",
        "NE": "Nebraska", "NH": "New Hampshire", "NJ": "New Jersey", "NM": "New Mexico", "NV": "Nevada"}
if len(sys.argv) > 2:
    JURS = {k: v for k, v in JURS.items() if k in sys.argv[2].split(",")}
OUTDIR = os.path.join(BASE, "01-ccg", "annexes")
SCR = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUTDIR, exist_ok=True)

DOMAINS = [
    ("labour_code", "Employment and labour code"),
    ("income_tax", "State income tax withholding"),
    ("non_resident", "Non-residents, residents working elsewhere and reciprocity"),
    ("local_tax", "Local wage taxes"),
    ("social_security", "Unemployment insurance, disability and paid-leave contributions, other payroll levies"),
    ("payslip_statute", "Pay statement"),
    ("reporting_instruments", "Statutory reporting"),
    ("leave", "Leave"),
    ("termination", "Termination and final pay"),
    ("benefits_in_kind", "Taxable wages and benefits in kind"),
    ("deductions_garnishments", "Deductions and garnishments"),
    ("collective_agreements", "Prevailing wage and collective agreements"),
    ("indexation", "Indexation"),
    ("data_protection", "Payroll data protection and records"),
    ("live_change", "Legal change in force or enacted"),
]
DTITLE = dict(DOMAINS)
REQ_DOMAIN = {"labour_code": "labour_code", "income_tax": "income_tax", "non_resident": "income_tax",
              "local_tax": "income_tax", "social_security": "social_security",
              "payslip_statute": "payslip_statute", "reporting_instruments": "statutory_reporting",
              "leave": "leave", "termination": "termination", "benefits_in_kind": "benefits_in_kind",
              "deductions_garnishments": "deductions_garnishments",
              "collective_agreements": "collective_agreements", "indexation": "indexation",
              "data_protection": "payroll_data_protection", "live_change": "live_legal_change"}
SEG = {}
for s in "minwage labour local_minwage overtime pay_frequency payment direct_deposit exempt comp_time local_mandates".split():
    SEG[s] = "labour_code"
for s in "pit wh oracle".split():
    SEG[s] = "income_tax"
for s in "nonres reciprocity".split():
    SEG[s] = "non_resident"
for s in "local local_wage_tax".split():
    SEG[s] = "local_tax"
for s in "sui ui pfml sdi sdi_pfml tdi fli tdi_fli wc mbt ui_mbt".split():
    SEG[s] = "social_security"
SEG.update({"payslip": "payslip_statute", "report": "reporting_instruments", "newhire": "reporting_instruments",
            "leave": "leave", "term": "termination", "final_pay": "termination", "severance": "termination",
            "termination": "termination", "bik": "benefits_in_kind", "garn": "deductions_garnishments",
            "deduction": "deductions_garnishments", "deductions": "deductions_garnishments",
            "prevailing_wage": "collective_agreements", "data": "data_protection",
            "data_protection": "data_protection", "records": "data_protection", "live": "live_change"})
DOM_ALIAS = {"oracle": "income_tax"}


def domain_of(key, explicit=None):
    p = key.split(".")
    if p[1] == "pit" and len(p) > 2:
        if p[2] == "local":
            return "local_tax"
        if p[2] in ("nonresident", "resident", "nra"):
            return "non_resident"
        if p[2].startswith("conformity"):
            return "benefits_in_kind"
    if explicit:
        return DOM_ALIAS.get(explicit, explicit)
    return SEG.get(p[1], "labour_code")


# ------------------------------------------------------------------ numbers / tags
NUM_IN_TEXT = re.compile(r"(?<![\w.,])(\d{1,3}(?:[ ,]\d{3})+(?:\.\d+)?|\d+(?:[.,]\d+)?)(\s?%)?(?![\w])")
TAG = re.compile(r"\[\[FACT:\s*([A-Za-z0-9_.]+)\s*=\s*([^\]]+?)\s*\]\]")


def _num(v):
    s = str(v).replace(" ", "").replace("%", "")
    if re.fullmatch(r"-?\d{1,3}(,\d{3})+(\.\d+)?", s):
        s = s.replace(",", "")
    try:
        return float(s)
    except ValueError:
        return None


def _sig(x):
    s = f"{abs(x):.10f}".replace(".", "").lstrip("0").rstrip("0")
    return len(s)


def distinctive_forms(key, value):
    v = _num(value) if not isinstance(value, (int, float)) else float(value)
    if v is None or isinstance(value, bool) or v == 0:
        return []
    is_rate = bool(re.search(r"(^|\.)rate(\.|$)", key)) and abs(v) < 1
    if is_rate:
        pct = round(v * 100, 6)
        if _sig(pct) >= 3 or pct != int(pct):
            return [(pct, True)]
        return []
    if float(v).is_integer() and 1900 <= v <= 2100:
        return []
    return [(v, False)] if _sig(v) >= 3 else []


ALLFORMS = {}
ALLNUM = []  # (key, value, file) of every numeric fact in every facts file
for fp in glob.glob(os.path.join(BASE, "_research", "*-facts.json")):
    try:
        for f in json.load(open(fp, encoding="utf-8")).get("facts", []):
            if isinstance(f.get("value"), (int, float)) and not isinstance(f.get("value"), bool):
                ALLNUM.append((f["key"], float(f["value"]), os.path.basename(fp)))
            for n, pct in distinctive_forms(f["key"], f.get("value")):
                ALLFORMS.setdefault((round(n, 6), pct), set()).add(f["key"])
    except Exception:
        pass


def vstr(v):
    if isinstance(v, bool):
        return "True" if v else "False"
    return str(v)


def tag(key, value):
    return f"[[FACT:{key}={vstr(value)}]]"


def common_prefix(a, b):
    n = 0
    for x, y in zip(a.split("."), b.split(".")):
        if x != y:
            break
        n += 1
    return n


def autotag(text, own_numeric, anchor_key, stats):
    """Tag distinctive numbers that equal a fact value of this annex; record others."""
    out, last = [], 0
    protected = [(m.start(), m.end()) for m in TAG.finditer(text)]
    for m in NUM_IN_TEXT.finditer(text):
        if any(a <= m.start() < b for a, b in protected):
            continue
        n = _num(m.group(1))
        if n is None:
            continue
        pct = bool(m.group(2))
        keys_all = ALLFORMS.get((round(n, 6), pct))
        if not keys_all:
            continue
        # a percent written in text only collides with fraction-valued rates of other annexes: never auto-bind
        cands = [] if pct else [k for k, v in own_numeric if abs(v - n) < 1e-9]
        tier = "own"
        if not cands and not pct:
            pre = anchor_key.split(".")[0] + "."
            cands = sorted({k for k, v, _ in ALLNUM if k.startswith(pre) and abs(v - n) < 1e-9})
            tier = "same-jurisdiction"
            if not cands:
                cands = sorted({k for k, v, _ in ALLNUM if k == "fed.minwage.hourly" and abs(v - n) < 1e-9})
                tier = "federal"
        if cands:
            k = sorted(cands, key=lambda c: (-common_prefix(c, anchor_key), c))[0]
            out.append(text[last:m.start(1)])
            out.append(f"[[FACT:{k}={m.group(1)}]]")
            last = m.end(1)
            stats["autotag"].append((anchor_key, m.group(1), k, tier))
        else:
            stats["unbound"].append((anchor_key, m.group(0).strip(), sorted(keys_all)[:3]))
    out.append(text[last:])
    return "".join(out)


# ------------------------------------------------------------------ pack filtering
INTERNAL = re.compile(r"(Synthesis|G-DERIVE|Python|\bpack\b|facts? file|register row|legacy|stage ?5|stage5|"
                      r"MANUAL|tier-B|tier B|browser|VPN|BR IP|WebFetch|curl|worker|PENDING|parked|"
                      r"\bfacts\[\]|unresolved|\bA\.[123]\b|re-point|rebind|derivation|attempted|re-read|this round|OQ-|hand-off|handoff|\bP\d+(/P\d+)?\b(?!-)|not researched|not searched|not obtained|reused|sweep|census|dated note|confidence|re-bind|MULTI owner|annex_|"
                      r"\bWTC\b|\bDD\b|\bCCG\b|oracle|Oracle|superseded|correct(s|ing|ed)? (the )?earlier|"
                      r"open\b|not read|not fetched|unread|lead\b|leads\b|reproduced|derived|\bQ\d+\b|MQ-)", re.I)
CITE_TOKEN = re.compile(r"\b[A-Za-z]+-?\d+[A-Za-z0-9\-]*\b")
EXC = re.compile(r"^(except|unless|but|only|other than|provided|save)\b", re.I)


def clause_ok(c):
    if not c or INTERNAL.search(c):
        return False
    s = CITE_TOKEN.sub("", c)
    return not re.search(r"\d", s)


def filter_line(text, stats, strict=True):
    ids = re.findall(r"US-[A-Z0-9]+-\d{3}", text)
    t = re.sub(r"\[[^\]]*\]", "", text)
    t = re.sub(r"\((?:[^()]*US-[A-Z0-9]+-\d{3}[^()]*)\)", "", t)
    t = t.replace("etc. ", "etc. ")
    t = re.sub(r"\s+([.;,])", r"\1", t)
    t = t.replace("**", "").replace("`", "").strip()
    t = re.sub(r"\s+", " ", t)
    label = ""
    m = re.match(r"^([A-Z][A-Za-z ,/()'\-]{1,45}):\s+(.*)$", t)
    if m and not re.search(r"\d", m.group(1)):
        label, t = m.group(1), m.group(2)
    clauses = [c.strip() for c in re.split(r";\s+|(?<=[a-z\)])\.\s+(?=[A-Z])", t) if c.strip()]
    kept, dropped = [], []
    for c in clauses:
        c2 = c.rstrip(".").strip()
        (kept if clause_ok(c2) and not c2.endswith(":") and len(c2) > 3 else dropped).append(c2)
    if strict and (dropped or t[:1].islower() or t.rstrip().endswith((";", ":", ",")) or len((label + " " + t).split()) < 5 or (not label and t.split()[0] in ("It", "This", "These", "So", "They", "Both", "Coverage")) or " therefore " in t):
        stats["dropped_lines"] += 1
        return None, label, len(dropped) or 1
    if any(EXC.match(d) for d in dropped):
        stats["dropped_lines"] += 1
        return None, label, len(dropped)
    if not kept:
        stats["dropped_lines"] += 1
        return None, label, len(dropped)
    stats["dropped_clauses"] += len(dropped)
    body = (t.replace("**", "").replace("`", "").strip().rstrip(".") if strict else "; ".join(kept)).replace(" ", " ")
    body = re.sub(r"\s+([.;,])", r"\1", body)
    if not label:
        body = body[0].upper() + body[1:]
    src = f" ({', '.join(dict.fromkeys(ids))})" if ids else ""
    return (f"{label}: {body}." if label else f"{body}.") + src, label, len(dropped)


def pack_sections(path):
    secs, cur = collections.OrderedDict(), None
    for line in open(path, encoding="utf-8"):
        line = line.rstrip("\n")
        m = re.match(r"^##\s+(.*)$", line)
        if m:
            h = m.group(1)
            mm = re.match(r"^(\d+)([a-c]?)\b", h)
            if mm:
                n, sfx = int(mm.group(1)), mm.group(2)
                cur = {(2, "b"): "non_resident", (2, "c"): "local_tax"}.get((n, sfx)) or \
                    [None, "labour_code", "income_tax", "social_security", "payslip_statute",
                     "reporting_instruments", "leave", "termination", "benefits_in_kind",
                     "deductions_garnishments", "collective_agreements", "indexation",
                     "data_protection", "live_change"][n] if n <= 13 else None
            elif h.lower().startswith("special populations"):
                cur = "special"
            elif h.lower().startswith("language"):
                cur = "language"
            else:
                cur = None
            continue
        if cur:
            secs.setdefault(cur, []).append(line)
    return secs


def pack_lines(lines, top_only=False):
    for ln in lines:
        if top_only and ln[:1] in (" ", "	"):
            continue
        s = ln.strip()
        if not s or s.startswith("|") or s.startswith("#") or s.startswith(">"):
            continue
        if re.match(r"^-\s+`[a-z]{2}\.", s):
            continue
        if re.match(r"^(-\s+)?(Confidence|Source|Facts added|Still open|Oracle)\b", s):
            continue
        s = re.sub(r"^[-*]\s+", "", s)
        yield s


# ------------------------------------------------------------------ hand-written content
DECISIONS = json.load(open(os.path.join(SCR, "decisions.json"), encoding="utf-8"))
NOTE_OVR = json.load(open(os.path.join(SCR, "note_overrides.json"), encoding="utf-8"))
BASIS_OVR = {
    "MI": "State flat rate [[FACT:mi.pit.rate.flat=4.25]] percent [US-MIP52-001]; [[FACT:mi.local.cities.count=24]] cities levy income tax, the Treasury administers Detroit only, the other 23 administer their own filing [US-MIP52-002, US-MIP51-002]",
    "NJ": "State withholding [US-NJP51-001]; Jersey City employer payroll tax of [[FACT:nj.pit.local.jersey_city.employer_payroll_tax.rate=1]] percent, quarterly returns to the City (city ordinance) [US-NJP6-001]; Newark employer payroll tax of [[FACT:nj.pit.local.newark.employer_payroll_tax.rate=1]] percent (a reduced rate applies where most of the workforce lives in Newark), quarterly returns to the City [US-NJP6-002]: employer-only city calculation and city return",
}
GAP_TEXT = json.load(open(os.path.join(SCR, "gap_overrides.json"), encoding="utf-8"))


def tier_row(jur):
    for line in open(os.path.join(BASE, "00-official-sources", "MANDATE.md"), encoding="utf-8"):
        if line.startswith(f"| {jur} | US-MQ-"):
            c = [x.strip() for x in line.strip().strip("|").split("|")]
            return c[2], c[3]
    return None, None


SANITIZE = [
    (r"\s*\blegacy\b(?= ?row)", ""), (r"(US-[A-Z0-9]+-\d{3}) legacy", r"\1"), (r"\blegacy\s+", ""),
    (r"\s*reproduced in Python", " reproduced"), (r"\s*\(Python\)", ""), (r"\(stage-5 derivation\)", "(derived)"),
    (r"\s*\(stage-5 finding\)", ""), (r"\s+in stage 5\b", ""), (r"G-DERIVE:\s*", "Derived: "),
    (r"annex_([A-Z]{2,5})", r"Annex \1"), (r"TRAP:\s*", "Caution: "), (r"\btier-B\b", "secondary"),
    (r"\s*\(Q\d+\)", ""), (r"\s*\([A-Z]{2}-OQ-\d+\)", ""), (r"WebFetch summary", "summary"),
    (r"webfetch quote \(summarizer\)", "summary quote"),
    (r"Synthesis C: rebound from", "also cited:"), (r"register row verification is weak:\s*", "source check: "),
    (r"register row is PARTIAL - carry the partial flag", "source graded partial"), (r"\s+this round", ""),
    (r"no verified register row carries it", "no verified source carries it"),
    (r"\((?:the )?MULTI unit\)", "(Annex MULTI)"), (r"the MULTI unit", "Annex MULTI"),
    (r"in the FED unit", "in Annex FED"), (r"the FED unit", "Annex FED"), (r"\(FED unit\)", "(Annex FED)"), (r"\(MULTI unit\)", "(Annex MULTI)"),
    (r"\s+\.", "."),
]


def sanitize(s):
    for a, b in SANITIZE:
        s = re.sub(a, b, s)
    return s


def esc(s):
    return str(s).replace("|", "/").replace("\n", " ")


def build(jur):
    name = JURS[jur]
    lo = jur.lower()
    facts_doc = json.load(open(os.path.join(BASE, "_research", f"CCG-annex_{jur}-facts.json"), encoding="utf-8"))
    facts, unresolved = facts_doc["facts"], facts_doc["unresolved"]
    own_numeric = [(f["key"], float(f["value"])) for f in facts
                   if isinstance(f["value"], (int, float)) and not isinstance(f["value"], bool)]
    stats = {"autotag": [], "unbound": [], "dropped_lines": 0, "dropped_clauses": 0}
    secs = pack_sections(os.path.join(BASE, "_research", f"CCG-annex_{jur}-research-pack.md"))
    rel = f"01-ccg/annexes/annex_{jur}.md"
    L = []
    gaps = []  # (key, blocking, section, line)
    bindings = []

    L.append(f"# Annex {jur}: {name}")
    L.append("")
    L.append(f"United States Country Configuration Guide, jurisdiction annex {jur}. Tax year 2026; "
             f"currency USD (two decimal places).")
    L.append("")
    L.append(f"## {jur}.0 Scope of this annex")
    L.append("")
    L.append(f"This annex holds the {name} layer only. The federal layer (federal income tax withholding, "
             "Social Security and Medicare, federal unemployment tax, Forms W-4, W-2, 941 and 940) is in Annex FED, "
             "and the rules for employees who live and work in different jurisdictions (sourcing, resident credits, "
             "reciprocity mechanics) are in Annex MULTI. Neither is repeated here. Independent contractors and "
             "Form 1099-NEC are out of scope. The pay statement is issued in English.")
    L.append("")
    L.append("In every table, *Valid from* and *Valid to* give the period in which the value applies "
             "(*open* means no end date has been published), and *Source* is the identifier of the row in the "
             "legal-basis register (00-official-sources/legal-basis-register.csv), with the authority and address "
             f"listed in section {jur}.{3 + len(DOMAINS) + 2} (the source address is held in the register row). Items marked as a research gap are not yet confirmed and must not be "
             "configured from this annex.")
    L.append("")
    tier, basis = tier_row(jur)
    basis = BASIS_OVR.get(jur, basis)
    L.append(f"## {jur}.1 Jurisdiction layer")
    L.append("")
    L.append("| Item | Value |")
    L.append("|---|---|")
    L.append(f"| Annex tier | {esc(tier)} |")
    L.append(f"| Basis | {esc(autotag(basis, own_numeric, lo + '.pit', stats))} |")
    L.append("")
    L.append("Tier key: T1 = no state wage tax (unemployment insurance and levies only); T3 = state withholding "
             "with no local layer remitted separately; T4 = a local layer remitted to a separate local authority "
             "on its own return.")
    L.append("")
    L.append(f"## {jur}.2 Configuration decisions")
    L.append("")
    for d in DECISIONS.get(jur, []):
        L.append(f"- {d}")
    L.append("")

    by_dom = collections.defaultdict(list)
    for f in facts:
        by_dom[domain_of(f["key"], f.get("_domain"))].append(f)
    gaps_dom = collections.defaultdict(list)
    for u in unresolved:
        gaps_dom[domain_of(u["key"])].append(u)

    n = 3
    for dom, title in DOMAINS:
        sec = f"{jur}.{n}"
        L.append(f"## {sec} {title}")
        L.append("")
        fs = by_dom.get(dom, [])
        order = {}
        for f in fs:
            order.setdefault(f["key"], len(order))
        fs = sorted(fs, key=lambda f: (order[f["key"]], f["effective_from"]))
        if fs:
            L.append("| Item | Value | Valid from | Valid to | Source | Note |")
            L.append("|---|---|---|---|---|---|")
            for f in fs:
                unit = f.get("unit_of_measure") or f.get("currency") or ""
                val = tag(f["key"], f["value"]) + (f" {unit}" if unit else "")
                note = NOTE_OVR.get(f["key"], f.get("note") or "")
                if note.startswith("Derivation recorded in register row"):
                    note = ""
                note = autotag(esc(sanitize(note)), own_numeric, f["key"], stats)
                L.append(f"| `{f['key']}` | {esc(val)} | {f['effective_from']} | {f['effective_to'] or 'open'} | "
                         f"{f['register_id']} ({f['tier']}, {f['authority']}) | {note} |")
                bindings.append((f"{rel} §{sec}", f["key"], vstr(f["value"])[:60], f["register_id"]))
            L.append("")
        rules = []
        for s in pack_lines(secs.get(dom, []), top_only=True):
            r, _, _ = filter_line(s, stats)
            if r:
                rules.append(sanitize(r))
        if rules:
            L.append("Rules:")
            L.append("")
            for r in dict.fromkeys(rules):
                L.append(f"- {r}")
            L.append("")
        if not fs and not rules and dom != "indexation":
            L.append(f"No {name} rule is configured in this domain; the federal treatment in Annex FED applies.")
            L.append("")
        if dom == "indexation" and not fs and not rules:
            L.append("Indexation of each value is stated in the note of the value concerned.")
            L.append("")
        for u in gaps_dom.get(dom, []):
            txt = sanitize(GAP_TEXT.get(u["key"], u["why"]))
            close = GAP_TEXT.get(u["key"] + "#close", u.get("what_would_close_it", ""))
            b = "blocking" if u.get("blocking") else "non-blocking"
            L.append(f"- ⚠️ RESEARCH-GAP ({b}, `{u['key']}`): {txt} To close: {close}")
            gaps.append((u, sec, dom, txt))
        if gaps_dom.get(dom):
            L.append("")
        n += 1

    # special populations
    sec = f"{jur}.{n}"
    L.append(f"## {sec} Special populations")
    L.append("")
    sp_lines, sp_dropped = [], []
    sp_src = []
    for ln in secs.get("special", []):
        c = [x.strip() for x in ln.strip().strip("|").split("|")] if ln.strip().startswith("|") else None
        if c is None:
            sp_src.append(ln)
            continue
        if len(c) < 2 or set(c[0]) <= set("-: ") or c[0].lower() in ("population", "group"):
            continue
        ids, prev = [], None
        for tok in re.findall(r"US-[A-Z0-9]+-\d{3}|(?<![\w])-\d{3}\b", " ".join(c[2:])):
            if tok.startswith("US-"):
                prev = tok.rsplit("-", 1)[0]
                ids.append(tok)
            elif prev:
                ids.append(prev + tok)
        sp_src.append(f"- {c[0]}: {c[1]}" + (f" [{', '.join(ids)}]" if ids else ""))
    for s in pack_lines(sp_src):
        r, label, nd = filter_line(s, stats, strict=False)
        if r:
            sp_lines.append(r)
        if nd or not r:
            sp_dropped.append(label or s[:40])
    for r in sp_lines:
        L.append(f"- {r}")
    if sp_dropped:
        key = f"{lo}.special_populations.thresholds"
        txt = ("thresholds, amounts or conditions for these populations are stated in the research without a "
               "confirmed value record and are not configured from this annex: " + "; ".join(dict.fromkeys(x.rstrip(":") for x in sp_dropped)) + ".")
        L.append(f"- ⚠️ RESEARCH-GAP (non-blocking, `{key}`): {txt} To close: one confirmed value per threshold, "
                 "with its source row.")
        gaps.append(({"key": key, "why": txt, "blocking": False,
                      "what_would_close_it": "one confirmed value per threshold, with its source row"},
                     sec, "labour_code", txt))
    L.append("")
    n += 1
    sec = f"{jur}.{n}"
    L.append(f"## {sec} Language")
    L.append("")
    lang = []
    for s in pack_lines(secs.get("language", [])):
        r, _, _ = filter_line(s, stats)
        if r and not re.match(r"^payslip (in )?english", r, re.I):
            lang.append(r)
    L.append("- The pay statement and all filings are in English (owner decision US-OWN-006).")
    for r in lang:
        L.append(f"- {r}")
    L.append("")
    n += 1
    sec = f"{jur}.{n}"
    L.append(f"## {sec} Sources")
    L.append("")
    L.append("| Source | Authority |")
    L.append("|---|---|")
    seen = {}
    for f in facts:
        seen.setdefault(f["register_id"], (f["authority"], f.get("url", "")))
    for rid in sorted(seen):
        a, u = seen[rid]
        L.append(f"| {rid} | {esc(a)} |")
    L.append("")
    text = "\n".join(L)
    open(os.path.join(OUTDIR, f"annex_{jur}.md"), "w", encoding="utf-8", newline="\n").write(text)
    # line numbers of gaps
    lines = text.split("\n")
    gap_out = []
    for u, s, dom, txt in gaps:
        ln = next((i + 1 for i, x in enumerate(lines) if f"`{u['key']}`)" in x and "RESEARCH-GAP" in x), None)
        gap_out.append({"key": u["key"], "blocking": bool(u.get("blocking")), "section": s, "domain": dom,
                        "line": ln, "text": txt, "close": GAP_TEXT.get(u["key"] + "#close", u.get("what_would_close_it", ""))})
    return {"jur": jur, "file": rel, "facts": len(facts), "tags": len(TAG.findall(text)),
            "bindings": bindings, "gaps": gap_out, "autotag": stats["autotag"], "unbound": stats["unbound"],
            "dropped_lines": stats["dropped_lines"], "dropped_clauses": stats["dropped_clauses"],
            "chars": len(text)}


if __name__ == "__main__":
    res = [build(j) for j in JURS]
    json.dump(res, open(os.path.join(SCR, "build_result.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    for r in res:
        print(r["jur"], "facts", r["facts"], "tags", r["tags"], "gaps", len(r["gaps"]),
              "autotag", len(r["autotag"]), "unbound", len(r["unbound"]), "dropped", r["dropped_lines"],
              r["dropped_clauses"], "chars", r["chars"])
