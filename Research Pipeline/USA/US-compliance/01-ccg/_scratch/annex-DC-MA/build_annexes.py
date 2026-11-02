# -*- coding: utf-8 -*-
"""Build CCG jurisdiction annexes (DC..MA) from _research/CCG-annex_{JUR}-facts.json
and the section layout of _research/CCG-annex_{JUR}-research-pack.md.

Every fact value is written as [[FACT:key=value]]. Pack narrative is carried only after
pipeline-internal wording is removed; distinctive numbers equal to a fact of the same
annex are tagged automatically. Unresolved items become in-place RESEARCH-GAP markers.
Writes 01-ccg/modules/annex_{JUR}.md and a JSON binding report per annex (scratch)."""
import json, os, re, sys, collections

BASE = sys.argv[1]
JURS = sys.argv[2].split(",")
OUT = os.path.join(BASE, "01-ccg", "modules")
SCR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCR)
OVR = []
os.makedirs(OUT, exist_ok=True)

TIER = {}
for j in "AK FL NH NV SD TN TX WA WY".split():
    TIER[j] = "T1"
for j in "AL CO DE KY MI MO NJ OH OR PA WV".split():
    TIER[j] = "T4"
TIER_TXT = {
    "T1": "T1: no state wage tax; the annex carries unemployment insurance, levies and labour rules only.",
    "T3": "T3: separate state withholding calculation and state return; no local layer, or a local layer piggybacked on the state return.",
    "T4": "T4: separate state withholding calculation and state return, plus a local layer remitted to the locality on its own return.",
}

SECTIONS = [
    ("1", "Employment and labour code"),
    ("2", "State income tax withholding"),
    ("2b", "Non-resident regime and reciprocity"),
    ("2c", "Local wage taxes"),
    ("3", "Social insurance (unemployment, disability, paid leave, levies)"),
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
    ("WE", "Worked examples"),
    ("SP", "Special populations"),
    ("LG", "Language of employee documents"),
]
SEC_NAME = dict(SECTIONS)

PACK_HEAD = [
    (r"^## 1 ", "1"), (r"^## 2 ", "2"), (r"^## 2b ", "2b"), (r"^## 2c ", "2c"), (r"^## 3 ", "3"),
    (r"^## 4 ", "4"), (r"^## 5 ", "5"), (r"^## 6 ", "6"), (r"^## 7 ", "7"), (r"^## 8 ", "8"),
    (r"^## 9 ", "9"), (r"^## 10 ", "10"), (r"^## 11 ", "11"), (r"^## 12 ", "12"), (r"^## 13 ", "13"),
    (r"^## Oracle", "WE"), (r"^## Special populations", "SP"), (r"^## Language", "LG"),
    (r"^## Synthesis D", "SKIP"), (r"^## Open questions", "SKIP"),
]
DOMAIN_SEC = {
    "labour_code": "1", "income_tax": "2", "non_resident": "2b", "local_tax": "2c",
    "social_security": "3", "payslip_statute": "4", "reporting_instruments": "5", "leave": "6",
    "termination": "7", "benefits_in_kind": "8", "deductions_garnishments": "9",
    "collective_agreements": "10", "indexation": "11", "data_protection": "12",
    "live_change": "13", "oracle": "WE",
}
# research-request domain enum
REQ_DOMAIN = {"1": "labour_code", "2": "income_tax", "2b": "income_tax", "2c": "income_tax",
              "3": "social_security", "4": "payslip_statute", "5": "statutory_reporting", "6": "leave",
              "7": "termination", "8": "benefits_in_kind", "9": "deductions_garnishments",
              "10": "collective_agreements", "11": "indexation", "12": "payroll_data_protection",
              "13": "live_legal_change", "WE": "income_tax", "SP": "labour_code", "LG": "payslip_statute"}


def gap_section(key):
    k = key.split(".", 1)[1]
    rules = [
        (r"^(nonres|reciproc)", "2b"), (r"^local\.", "2c"), (r"^local_leave", "6"),
        (r"^(wh|pit|tax)\b", "2"), (r"^(sui|sdi|tdi|pfml|pfl|sit_ui|ui)\b", "3"),
        (r"^payslip", "4"), (r"^(report|newhire)", "5"), (r"^leave|^other_leave", "6"),
        (r"^(termination|final_pay)", "7"), (r"^garn", "9"), (r"^(prevailing|living_wage)", "10"),
        (r"^(data_protection|records|breach)", "12"), (r"^live", "13"),
        (r"^(minwage|overtime|payment|paycard|local_mandates|pay_frequency)", "1"),
        (r"^special_populations", "SP"),
    ]
    for pat, s in rules:
        if re.search(pat, k):
            return s
    return "13"


def fmt_num(v, unit):
    if isinstance(v, bool):
        return str(v)
    if isinstance(v, int):
        return f"{v:,}"
    if isinstance(v, float):
        if unit == "USD":
            if v.is_integer():
                return f"{int(v):,}"
            s = f"{v:,.2f}"
            return s if abs(float(s.replace(',', '')) - v) < 1e-12 else f"{v:,}".rstrip("0")
        r = repr(v)
        return r
    return str(v)


def tag(key, v, unit=None):
    s = fmt_num(v, unit) if not isinstance(v, str) else v
    if "]" in s or "[" in s:
        return None
    return f"[[FACT:{key}={s}]]"


def unit_txt(u):
    if not u:
        return ""
    return {"percent": "%", "USD": "USD"}.get(u, u)


INTERNAL = [
    (r"\s*—\s*promoted to fact in Synthesis C", ""),
    (r"TRAP \(brief\):\s*", "Configuration warning: "),
    (r"\bG-DERIVE:\s*", "Derivation: "),
    (r"\s*legacy\]", "]"),
    (r"\s*\(recorded limit\)", ""),
    (r"Overall confidence \d+%\.?", ""),
]


def clean(t):
    import overrides
    for a, b in INTERNAL + overrides.CLEAN:
        t = re.sub(a, b, t)
    return t.strip()


NUM = re.compile(r"(?<![\w.,])(\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?)(\s?%)?(?![\w])")


def sig(x):
    s = f"{abs(x):.10f}".replace(".", "").lstrip("0").rstrip("0")
    return len(s)


def autotag(text, index, sec, bound):
    """Tag distinctive numbers equal to a fact value of this annex. index: {(value, is_pct): [(sec, key, raw)]}"""
    if "[[FACT:" in text:
        parts = re.split(r"(\[\[FACT:[^\]]*\]\])", text)
    else:
        parts = [text]
    out = []
    for p in parts:
        if p.startswith("[[FACT:"):
            out.append(p)
            continue
        def rep(m):
            raw, pct = m.group(1), m.group(2)
            try:
                n = float(raw.replace(",", ""))
            except ValueError:
                return m.group(0)
            if float(n).is_integer() and 1900 <= n <= 2100 and not pct:
                return m.group(0)
            if not pct and sig(n) < 3 and not (n >= 100 or "." in raw):
                return m.group(0)
            if pct and sig(n) < 2 and float(n).is_integer():
                return m.group(0)
            cands = index.get((round(n, 6), bool(pct)))
            if not cands:
                return m.group(0)
            same = [c for c in cands if c[0] == sec]
            s, key, val = (same or cands)[0]
            t = f"[[FACT:{key}={raw}]]"
            bound.append(key)
            return t + (pct or "")
        out.append(NUM.sub(rep, p))
    return "".join(out)


def parse_pack(path):
    sec = None
    narr = collections.defaultdict(list)
    keysec = {}
    summary = ""
    for line in open(path, encoding="utf-8").read().splitlines():
        if line.startswith("## "):
            sec = None
            for pat, s in PACK_HEAD:
                if re.match(pat, line):
                    sec = s
                    break
            continue
        if line.startswith("**Summary.**"):
            summary = line[len("**Summary.**"):].strip()
            continue
        if sec is None or sec == "SKIP" or not line.strip():
            continue
        m = re.match(r"^- `([a-z0-9_.]+)` = ", line)
        if m:
            keysec.setdefault(m.group(1), sec)
            continue
        if line.startswith(">") or line.startswith("Synthesis") or line.startswith("Source: browser-pass") \
                or line.startswith("Still open") or line.startswith("Mirrors `unresolved"):
            continue
        narr[sec].append(line)
    return summary, narr, keysec


def overrides_extra(jur, sid):
    import overrides
    return overrides.EXTRA.get((jur, sid))


def esc(t):
    return str(t).replace("|", "\\|").replace("\n", " ")


def build(jur):
    facts_doc = json.load(open(os.path.join(BASE, "_research", f"CCG-annex_{jur}-facts.json"), encoding="utf-8"))
    name = facts_doc.get("_jurisdiction", jur)
    facts = facts_doc["facts"]
    unresolved = facts_doc.get("unresolved", [])
    summary, narr, keysec = parse_pack(os.path.join(BASE, "_research", f"CCG-annex_{jur}-research-pack.md"))
    blocking_keys = {u["key"] for u in unresolved if u.get("blocking")}

    def sec_of(f):
        return keysec.get(f["key"]) or DOMAIN_SEC.get(f.get("_domain"), "13")

    by_sec = collections.defaultdict(list)
    for f in facts:
        by_sec[sec_of(f)].append(f)
    index = collections.defaultdict(list)
    for f in facts:
        v = f["value"]
        if isinstance(v, bool) or not isinstance(v, (int, float)):
            continue
        is_pct = f.get("unit_of_measure") == "percent"
        if not (is_pct or f.get("currency") == "USD" or f.get("unit_of_measure") == "ratio"):
            continue
        index[(round(float(v), 6), is_pct)].append((sec_of(f), f["key"], v))

    bindings = []   # (section, key, register_id, how)
    gaps = []
    untagged_values = []
    L = []
    L.append(f"# Annex {jur}: {name}")
    L.append("")
    tier = TIER.get(jur, "T3")
    L.append(f"**Layer classification ({tier}).** {TIER_TXT[tier]} Source: build manifest tier census, local income tax domain.")
    L.append("")
    if summary:
        b = []
        s = autotag(clean(summary), index, "S", b)
        bindings += [("Summary", k, None, "auto") for k in b]
        L.append(f"**Summary.** {s}")
        L.append("")
    L.append("Each parameter row gives its key, the period in force and its legal basis: the legal-basis register row, the authority, the source tier and how the value was verified.")
    L.append("")

    gap_by_sec = collections.defaultdict(list)
    for u in unresolved:
        gap_by_sec[gap_section(u["key"])].append(u)

    for sid, title in SECTIONS:
        rows = by_sec.get(sid, [])
        nar = narr.get(sid, [])
        gl = gap_by_sec.get(sid, [])
        num = sid if sid[0].isdigit() else {"WE": "14", "SP": "15", "LG": "16"}[sid]
        L.append(f"## {jur}.{num} {title}")
        L.append("")
        if not rows and not nar and not gl and not overrides_extra(jur, sid) and not (sid == "WE" and os.path.exists(os.path.join(SCR, "examples_" + jur + ".md"))):
            L.append("No published state worked example is recorded for this jurisdiction." if sid == "WE" else "No jurisdiction-specific item was recorded in the research for this domain.")
            L.append("")
            continue
        import overrides
        nar = list(overrides.EXTRA.get((jur, sid), [])) + list(nar)
        for line in nar:
            b = []
            t = autotag(clean(line), index, sid, b)
            if not t:
                continue
            bindings += [(SEC_NAME[sid], k, None, "auto") for k in b]
            L.append(t)
        if nar:
            L.append("")
        if rows:
            L.append("| Parameter (key) | Value | In force | Legal basis | Note |")
            L.append("|---|---|---|---|---|")
            for f in sorted(rows, key=lambda x: (x["key"], x.get("effective_from") or "")):
                u = f.get("currency") or f.get("unit_of_measure")
                tg = tag(f["key"], f["value"], u)
                if tg is None:
                    val = esc(f["value"]) + f" (key `{f['key']}`; value carried verbatim, not taggable)"
                    untagged_values.append(f["key"])
                else:
                    val = tg + ((" " + unit_txt(u)) if u else "")
                    if u == "percent":
                        val = tg + " %"
                if f["key"] in blocking_keys:
                    val += " ⚠️ RESEARCH-GAP: value not final, see the open item on this key"
                eff = f"{f.get('effective_from') or 'n/a'} to {f.get('effective_to') or 'open'}"
                basis = f"{f['register_id']} ({esc(f.get('authority',''))}; {f.get('tier','')}, {esc(f.get('verification_method',''))}, confidence {f.get('confidence','')})"
                note = f.get("note") or ""
                if note.startswith("Derivation recorded in register row"):
                    note = f"Derivation recorded in register row {f['register_id']}."
                b = []
                note = autotag(clean(note), index, sid, b)
                bindings.append((SEC_NAME[sid], f["key"], f["register_id"], "value"))
                bindings += [(SEC_NAME[sid], k, None, "auto-note") for k in b]
                L.append(f"| `{f['key']}` | {esc(val)} | {eff} | {basis} | {esc(note)} |")
            L.append("")
        for u in gl:
            blk = "blocking" if u.get("blocking") else "non-blocking"
            b = []
            gl_txt = f"⚠️ RESEARCH-GAP: {esc(clean(u['why']))} (open item `{u['key']}`, {blk}; would close it: {esc(clean(u.get('what_would_close_it','')))})"
            gl_txt = autotag(gl_txt, index, sid, b)
            bindings += [(SEC_NAME[sid], k, None, "auto-gap") for k in b]
            L.append(gl_txt)
            L.append("")
            gaps.append((sid, u))
    text = "\n".join(L).rstrip() + "\n"
    import overrides
    for a, b in overrides.GLOBAL + overrides.PER.get(jur, []):
        if "[[FACT:" in a:
            if a in text:
                OVR.append((jur, a, b, text.count(a)))
                text = text.replace(a, b)
            continue
        parts = re.split(r"(\[\[FACT:[^\]]*\]\])", text)
        n = sum(x.count(a) for x in parts if not x.startswith("[[FACT:"))
        if n:
            OVR.append((jur, a, b, n))
            text = "".join(x if x.startswith("[[FACT:") else x.replace(a, b) for x in parts)
    if os.path.exists(os.path.join(SCR, "examples_" + jur + ".md")):
        ex = open(os.path.join(SCR, "examples_" + jur + ".md"), encoding="utf-8").read().strip()
        text = text.replace(f"## {jur}.14 Worked examples\n", f"## {jur}.14 Worked examples\n\n{ex}\n", 1)
    open(os.path.join(OUT, f"annex_{jur}.md"), "w", encoding="utf-8").write(text)
    rep = {"jur": jur, "facts": len(facts), "keys": sorted({f['key'] for f in facts}),
           "bindings": bindings, "untagged_values": untagged_values,
           "gaps": [{"section": s, "title": SEC_NAME[s], **u} for s, u in gaps]}
    json.dump(rep, open(os.path.join(SCR, f"report_{jur}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(jur, "facts", len(facts), "gaps", len(gaps), "auto-tags", sum(1 for b in bindings if b[3] != 'value'), "untagged", untagged_values)


for j in JURS:
    build(j)
json.dump(OVR, open(os.path.join(SCR, "overrides_applied.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("overrides applied", len(OVR))
