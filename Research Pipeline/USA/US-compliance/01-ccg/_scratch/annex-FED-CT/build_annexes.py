"""Build CCG annex units (FED, MULTI, AK, AL, AR, AZ, CA, CO, CT) from the research packs
and facts files. Every fact value is written as a [[FACT:key=value]] tag taken from the
facts file. Re-run: python build_annexes.py [UNIT ...]   (writes 01-ccg/modules/annex_XX.md)
Reads only: _research/CCG-annex_XX-research-pack.md, _research/CCG-annex_XX-facts.json,
00-official-sources/legal-basis-register.csv, overrides.py (hand-written narrative per unit).
"""
import csv, glob, json, os, re, sys
from collections import OrderedDict, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
RES = os.path.join(BASE, "_research")
OUT = os.path.join(BASE, "01-ccg", "annexes")
sys.path.insert(0, os.path.join(BASE, "01-ccg", "_build", "common"))
import ccg_common as CC  # noqa: E402  round 2 (QA r1): finalize, annex skeleton, [[GAP:]] tags
sys.path.insert(0, HERE)
import overrides as OV  # noqa: E402

UNITS = ["FED", "MULTI", "AK", "AL", "AR", "AZ", "CA", "CO", "CT"]
NAMES = {"FED": "Federal layer", "MULTI": "Multistate routing layer", "AK": "Alaska", "AL": "Alabama",
         "AR": "Arkansas", "AZ": "Arizona", "CA": "California", "CO": "Colorado", "CT": "Connecticut"}

REG = {r["id"]: r for r in csv.DictReader(open(os.path.join(BASE, "00-official-sources", "legal-basis-register.csv"),
                                                encoding="utf-8"))}

# all facts of the build (for the C46-style residual scan)
ALLF = []
for _fp in sorted(glob.glob(os.path.join(RES, "CCG-annex_*-facts.json"))) + sorted(glob.glob(os.path.join(RES, "*-facts.json"))):
    ALLF.extend(json.load(open(_fp, encoding="utf-8")).get("facts", []))
ALL = defaultdict(set)
for fp in glob.glob(os.path.join(RES, "*-facts.json")):
    try:
        for f in json.load(open(fp, encoding="utf-8")).get("facts", []):
            ALL[f["key"]].add(json.dumps(f.get("value")))
    except Exception:
        pass

# ----------------------------------------------------------------- sections
SECTION_ORDER = [
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
    ("OR", "Authority worked examples (oracle values)"),
    ("SP", "Special populations"),
    ("LG", "Language"),
]
DOMAIN_TO_SEC = {
    "labour_code": "1", "income_tax": "2", "income_tax_nonresident": "2b", "non_resident": "2b",
    "local_tax": "2c", "social_security": "3", "payslip_statute": "4", "reporting": "5",
    "reporting_instruments": "5", "leave": "6", "termination": "7", "benefits_in_kind": "8",
    "deductions_garnishments": "9", "collective_agreements": "10", "indexation": "11",
    "data_protection": "12", "live_legal_change": "13", "live_change": "13", "oracle": "OR",
    "special_populations": "SP",
}


NOTE_VOCAB = re.compile(r"R\d 20\d\d|effective_from|local copy|script shell|\bbytes?\b", re.I)


def drop_vocab_clauses(t):
    """Printed notes carry no round / history / retrieval wording: drop the ';'-separated clauses that do."""
    return '; '.join(c for c in re.split(r';\s*', t or '') if not NOTE_VOCAB.search(c))


def pack_section_id(title):
    t = title.strip()
    m = re.match(r"^(\d+[a-z]?)\s+—", t)
    if m:
        return m.group(1)
    if t.startswith("Oracle"):
        return "OR"
    if t.startswith("Special populations"):
        return "SP"
    if t.startswith("Language"):
        return "LG"
    if t.startswith("Routing algorithm"):
        return "RT"
    return None  # Synthesis D additions, Open questions: redistributed


# ----------------------------------------------------------------- formatting
ABBR = {"sui": "SUI", "sdi": "SDI", "pfml": "PFML", "pit": "PIT", "sit": "state income tax", "wh": "withholding",
        "fit": "FIT", "fica": "FICA", "oasdi": "OASDI", "futa": "FUTA", "suta": "SUTA", "minwage": "minimum wage",
        "garn": "garnishment", "iwo": "IWO", "ee": "employee", "er": "employer", "nonres": "non-resident",
        "std": "standard", "bik": "benefit in kind", "ot": "overtime", "mfj": "MFJ", "hoh": "HoH",
        "ccpa": "CCPA", "nra": "NRA", "w2": "W-2", "w4": "W-4", "ui": "UI", "ett": "ETT", "tdi": "TDI",
        "famli": "FAMLI", "opt": "OPT", "abcr": "ABCR", "step": "STEP", "tvep": "TVEP", "efw2": "EFW2",
        "aca": "ACA", "hsa": "HSA", "fsa": "FSA", "irs": "IRS", "ssa": "SSA", "eap": "EAP", "pub15t": "Pub. 15-T",
        "ctpl": "CT Paid Leave", "de44": "DE 44", "ct": "CT", "ca": "CA", "co": "CO", "az": "AZ", "al": "AL",
        "ak": "AK", "ny": "NY", "nj": "NJ", "pa": "PA", "oh": "OH", "ga": "GA", "sc": "SC",
        "ms": "MS", "ma": "MA", "wi": "WI", "il": "IL", "ky": "KY", "md": "MD",
        "mi": "MI", "mn": "MN", "nd": "ND", "va": "VA", "wv": "WV", "dc": "DC", "ia": "IA", "de": "DE",
        "mo": "MO", "la": "LA", "vt": "VT", "ks": "KS", "ne": "NE", "wa": "WA", "ri": "RI",
        "mt": "MT", "ut": "UT", "nm": "NM", "nh": "NH", "tn": "TN",
        "tx": "TX", "nv": "NV", "fl": "FL", "sd": "SD", "wy": "WY", "nc": "NC", "vi": "VI", "eo13706": "EO 13706", "de9c": "DE 9C", "gtl": "GTL", "pub701": "Pub. 701", "ssn": "SSN", "econsent": "electronic consent"}


def label(key, prefix):
    parts = key.split(".")
    if parts and parts[0] == prefix:
        parts = parts[1:]
    words = []
    for p in parts:
        for w in p.split("_"):
            words.append(ABBR.get(w, w))
    s = " ".join(words)
    return s[:1].upper() + s[1:]


def numstr(v):
    if isinstance(v, bool):
        return str(v)
    if isinstance(v, int):
        return f"{v:,}" if abs(v) >= 10000 else str(v)
    if isinstance(v, float):
        if v.is_integer():
            return f"{int(v):,}" if abs(v) >= 10000 else str(int(v))
        s = ("%.10f" % v).rstrip("0").rstrip(".")
        ip, _, dp = s.partition(".")
        ip_i = int(ip)
        ip_s = f"{ip_i:,}" if abs(ip_i) >= 10000 else ip
        return ip_s + ("." + dp if dp else "")
    return str(v)


def money(v):
    if isinstance(v, bool):
        return str(v)
    if isinstance(v, (int, float)) and round(float(v), 2) == float(v):
        if float(v).is_integer():
            return f"{int(v):,}"
        return f"{float(v):,.2f}"
    return numstr(v)


def tag(f):
    v = f["value"]
    if isinstance(v, str):
        vs = v.replace("]", ")").replace("[", "(")
        return f"[[FACT:{f['key']}={vs}]]"
    if f.get("currency") == "USD":
        return f"[[FACT:{f['key']}={money(v)}]]"
    return f"[[FACT:{f['key']}={numstr(v)}]]"


def value_cell(f):
    t = tag(f)
    u = f.get("unit_of_measure")
    if isinstance(f["value"], str):
        return t
    if f.get("currency") == "USD":
        return f"USD {t}"
    if u == "percent":
        return f"{t} %"
    if u and not isinstance(f["value"], bool):
        return f"{t} {u}"
    return t


def eff(f):
    import deliverable_wording as DW     # v1.1 QA r1: a proposed or historical register row is never shown as an in-force date
    a, b = f.get("effective_from") or "", f.get("effective_to") or ""
    st = DW.period_cell(f)
    if st:
        return st
    return f"{a} to {b}" if b else f"from {a}"


# ----------------------------------------------------------------- text cleaning
REGID = r"US-[A-Z0-9]+(?:-[A-Z0-9]+)*-\d{3,4}"
META_LINE = re.compile(r"^(> \*\*Synthesis|Synthesis [A-D]|Source: browser-pass|Facts added:|Open questions narrowed|"
                       r"\*\*Reuse rule|\*\*Register-id pattern defect|\*\*Corrections to MULTI\.md|Mirrors `unresolved|"
                       r"Facts (re)?(added|promoted)|Open questions added)")


def clean(text):
    t = text
    t = re.sub(r"\s*\[[^\[\]]*" + REGID + r"[^\[\]]*\]", "", t)
    t = re.sub(r"\s*\((?:[^()]*?)(?:" + REGID + r"|US-OWN-\d{3}|US-MQ-\d+|[A-Z]{2,5}-OQ-\d+)(?:[^()]*?)\)", "", t)
    t = re.sub(REGID, "", t)
    t = re.sub(r"\bUS-OWN-\d{3}\b|\bUS-MQ-\d+\b", "", t)
    t = re.sub(r"\(\s*\)", "", t)
    t = t.replace("`", "")
    t = re.sub(r"\s+([,.;:])", r"\1", t)
    t = re.sub(r"[ \t]{2,}", " ", t)
    return t.strip()


NOTE_DROP_SENT = re.compile(r"(Stage[- ]?\d|Synthesis|tier[- ]?[ABC]\b|\bMANUAL\b|PENDING|not a fact|register|facts? file|legacy id|"
                            r"promoted|PyMuPDF|pdftotext|never-do|G-RULING|G-CALIBER|annex_|owning file|corroborated only|"
                            r"browser pass|Chrome pass|\bOQ-|fan-out|\bunit\b|\bFED unit|\bState unit)", re.I)


def clean_note(n):
    n = clean(n)
    n = re.sub(r"\[PARTIAL ROW:[^\]]*\]", "Source edition partially verified.", n)
    n = n.replace("G-DERIVE:", "Derivation:").replace("G-DERIVE", "Derivation")
    n = re.sub(r"\s*\((?:re-derived|reproduced) in Python\)", "", n)
    n = re.sub(r"(Reproduced|Re-derived|re-derived|reproduced|recomputed) in Python[:.]?", "Recomputed", n)
    n = n.replace("in Python", "")
    sents = re.split(r"(?<=[.;])\s+(?=[A-Z(])", n)
    # QA r3d finding 4: a sentence carrying a legal citation or quoted statute text is dropped only for a
    # strictly internal phrase, never for a loose word ('register', 'unit', 'facts file')
    keep = [x for x in sents if not (NOTE_DROP_STRICT.search(x) if CC.LEGAL_CITE_RX.search(x) else NOTE_DROP_SENT.search(x))]
    out = " ".join(keep).strip()
    out = re.sub(r"LEVEL:\s*[^.]*\.?", "", out).strip()
    return out


NOTE_DROP_STRICT = re.compile(r"(Stage[- ]?\d|Synthesis|tier[- ]?[ABC]\b|\bMANUAL\b|PENDING|PyMuPDF|pdftotext|never-do|"
                              r"G-RULING|G-CALIBER|annex_|browser pass|Chrome pass|\bOQ-|fan-out)", re.I)
DROP_NOTE = re.compile(r"^Derivation recorded in register row")
PIPE_WORDS = re.compile(r"\b(Stage[- ]?5|Stage 9b?|G-DERIVE|Synthesis [A-D]|in Python|re-derived in Python|"
                        r"Reproduced in Python|facts? file|register row|tier[- ][BC]\b|MANUAL|PENDING|legacy id)", re.I)

# numbers that are citations / dates / identifiers rather than quantities
CIT_BEFORE = re.compile(r"(§|Code|U\.S\.C\.|USC|CFR|C\.F\.R\.|\bAS|AAC|\bAct|Acts|Pub\.|Publication|Form|Forms|Rev\.|ORC|RCW|KRS|"
                        r"Sec\.|sec\.|Section|section|art\.|Article|Ch\.|ch\.|chapter|Title|title|C\.R\.S\.|CRS|Gen\. Stat\.|"
                        r"Lab\. Code|UIC|R&TC|Rule|Regs?\.|Reg\.|P\.L\.|Pub\. L\.|H\.?B\.?|S\.?B\.?|SB|HB|AB|No\.|no\.|IP|"
                        r"Notice|Proc\.|Rul\.|box|Box|line|Line|code|Schedule|schedule|Table|table|Worksheet|step|Step|"
                        r"page|p\.|pp\.|Cal\.|Ariz\.|Ark\.|Ala\.|Conn\.|Colo\.|CMR|O\.S\.|NYCRR|Pa\.|Del\. C\.|LAC|LR|"
                        r"IRC|I\.R\.C\.|Rev\. Rul\.|DE|TQ|A-|W-|IT|ITEP|EFW|Class|class|classes|group|Ex\.)\s*$")


def quantitative_numbers(t):
    """untagged quantity-like numbers left in text (for review), excluding tags, dates, citations."""
    bare = re.sub(r"\[\[FACT:[^\]]*\]\]", " ", t)
    bare = re.sub(r"\d{4}-\d{2}-\d{2}", " ", bare)
    out = []
    for m in re.finditer(r"(?<![\w.,/-])(\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?)(\s?%)?(?![\w/-]|\.\d)", bare):
        s = m.group(1)
        before = bare[max(0, m.start() - 22):m.start()]
        if CIT_BEFORE.search(before):
            continue
        n = float(s.replace(",", ""))
        if n.is_integer() and 1900 <= n <= 2100 and not m.group(2):
            continue
        out.append(m.group(0).strip())
    return out


# ----------------------------------------------------------------- tagging numbers in prose
def num_val(s):
    try:
        return float(s.replace(",", ""))
    except ValueError:
        return None


# QA r3d finding 8 / finding 1 guard: a filing-status word directly before a number names the key family
# ("single 2,500 / married filing separately 2,500 / married filing jointly 5,000 / head of family 2,500")
STATUS_CTX = re.compile(r"(married filing separately|married filing jointly|married separate|head of family|"
                        r"head of household|single|married)\s*(?:\([A-Z0-9/]{1,4}\))?\s*:?\s*\$?\s*$", re.I)
STATUS_SEG = {"married filing separately": "married_separate", "married separate": "married_separate",
              "married filing jointly": "married", "married": "married", "head of family": "head_of_family",
              "head of household": "head_of_family", "single": "single"}
CUR_UNIT = [""]
REBIND = []   # (unit, old choice, new choice, context): every binding that differs from the r3c rule


def _prefix_len(a, b):
    n = 0
    for x, y in zip(a.split("."), b.split(".")):
        if x != y:
            break
        n += 1
    return n


def autotag(text, facts_by_val, prefer_keys=()):
    """Replace a number in prose by the tag of the unit fact carrying that value, when the
    match is unique (or when one of prefer_keys carries it). Percent numbers match percent facts.
    QA r3d: (1) a key is bound only when CC.binding_ok() holds (same jurisdiction; a place-named key only in a
    sentence naming the place); (2) a filing-status word directly before the number selects that status's key;
    (3) among several equal-value keys, the one sharing the longest key prefix with the row key wins."""
    used = defaultdict(int)
    jur = CUR_UNIT[0].lower()

    def rep(m):
        s, pct = m.group(1), m.group(2)
        n = num_val(s)
        if n is None:
            return m.group(0)
        before = text[max(0, m.start() - 22):m.start()]
        if CIT_BEFORE.search(before):
            return m.group(0)
        # QA r2 (C46 wrong binding): a day of a date ("1 Jan", "January 1") is never a quantity
        if not pct and (DATE_AFTER.match(text, m.end()) or DATE_BEFORE.search(before)):
            return m.group(0)
        allc = facts_by_val.get((round(n, 6), bool(pct)), [])
        cands = [f for f in allc if f["key"] in prefer_keys or (STRICT_SIG(n, pct) and not f.get("_small"))]
        # r3c choice (kept to log every binding the r3d rules change)
        old = None
        if cands:
            pref0 = [f for f in cands if f["key"] in prefer_keys]
            pool0 = list(OrderedDict((f["key"], f) for f in (pref0 or cands)).values())
            old = pool0[used[(round(n, 6), bool(pct))] % len(pool0)]["key"] if len(pool0) > 1 and not pref0 else pool0[0]["key"]
        # r3d: status context
        sm = STATUS_CTX.search(text[max(0, m.start() - 40):m.start()])
        f = None
        if sm and allc:
            seg = "." + STATUS_SEG[sm.group(1).lower()] + "."
            st = list(OrderedDict((x["key"], x) for x in allc if seg in "." + x["key"] + ".").values())
            if len(st) > 1 and prefer_keys:
                st = [x for x in st if x["key"].rsplit(".", 1)[-1] == prefer_keys[0].rsplit(".", 1)[-1]]
            if len(st) == 1:
                f = st[0]
        if f is None:
            if not cands:
                return m.group(0)
            pref = [x for x in cands if x["key"] in prefer_keys]
            pool = pref or cands
            keys = list(OrderedDict((x["key"], x) for x in pool).values())
            if len(keys) > 1 and not pref:
                if prefer_keys:
                    best = max(_prefix_len(k["key"], prefer_keys[0]) for k in keys)
                    top = [k for k in keys if _prefix_len(k["key"], prefer_keys[0]) == best]
                else:
                    top = keys
                f = top[used[(round(n, 6), bool(pct))] % len(top)]
                used[(round(n, 6), bool(pct))] += 1
                AMBIG.append((f["key"], [k["key"] for k in keys], text[:120]))
            else:
                f = keys[0]
        if not CC.binding_ok(f["key"], jur, text, m.start(), anchor=prefer_keys[0] if prefer_keys else None):
            if old is not None:
                REBIND.append((CUR_UNIT[0], old, None, text[max(0, m.start() - 60):m.end() + 20]))
            return m.group(0)
        if f["key"] != old:
            REBIND.append((CUR_UNIT[0], old, f["key"], text[max(0, m.start() - 60):m.end() + 20]))
        t = tag(f)
        return t + (" %" if pct else "")
    return re.sub(r"(?<![\w.,/=-])(\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?)(\s?%)?(?![\w-]|\.\d|\]\])", rep, text)


AMBIG = []
PACKPROSE = []
DATE_AFTER = re.compile(r"\s?(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)[a-z]*\.?\b")
DATE_BEFORE = re.compile(r"\b(?:January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)\.?\s$")


def STRICT_SIG(n, pct):
    s = f"{abs(n):.10f}".replace(".", "").lstrip("0").rstrip("0")
    return len(s) >= 3 or (pct and not float(n).is_integer())


def index_by_value(facts):
    idx = defaultdict(list)
    for f in facts:
        v = f["value"]
        if isinstance(v, bool) or not isinstance(v, (int, float)):
            continue
        is_pct = f.get("unit_of_measure") == "percent"
        n = float(v)
        if not is_pct and (n.is_integer() and abs(n) < 100):
            f = dict(f)
            f["_small"] = True  # small integers bind only to the row's own key
        idx[(round(n, 6), is_pct)].append(f)
    return idx


def fill(text, facts):
    """{{key}} or {{key@effective_from}} -> tag; {{key|v}} -> value cell (with unit)."""
    def rep(m):
        k, frm, mode = m.group(1), m.group(2), m.group(3)
        c = [f for f in facts if f["key"] == k and (frm is None or f.get("effective_from") == frm)]
        if not c:
            c = [f for f in ALLF if f["key"] == k and (frm is None or f.get("effective_from") == frm)]
        if not c:
            raise KeyError(f"fill: no fact {k}@{frm}")
        if len(c) > 1:
            uniq = {}
            for x in c:
                uniq.setdefault((x.get("effective_from"), json.dumps(x.get("value"))), x)
            c = list(uniq.values())
        if len(c) > 1 and frm is None:
            # round 2: a key that gained a dated period after the hand text was written (facts re-run by
            # a parallel worker) defaults to the value in force mid build year; give @effective_from to
            # show another period
            mid = [x for x in c if (x.get("effective_from") or "0000") <= "2026-06-30" <= (x.get("effective_to") or "9999")]
            if len(mid) == 1:
                c = mid
                print("fill: default period 2026-06-30 for", k)
            else:
                raise KeyError(f"fill: {k} has {len(c)} values, give @effective_from")
        HAND.append(k)
        return value_cell(c[0]) if mode else tag(c[0])
    return re.sub(r"\{\{([a-z0-9_.]+)(?:@(\d{4}-\d{2}-\d{2}))?(\|v)?\}\}", rep, text)


HAND = []


# ----------------------------------------------------------------- build
def build(unit):
    global AMBIG
    AMBIG = []
    CUR_UNIT[0] = unit
    prefix = unit.lower()
    fj = json.load(open(os.path.join(RES, f"CCG-annex_{unit}-facts.json"), encoding="utf-8"))
    facts = fj["facts"]
    unresolved = fj.get("unresolved", [])
    pack = open(os.path.join(RES, f"CCG-annex_{unit}-research-pack.md"), encoding="utf-8").read().splitlines()

    # parse pack
    secs, cur, intro = OrderedDict(), None, []
    bullet_keys = defaultdict(list)
    for ln in pack:
        if ln.startswith("# "):
            continue
        if ln.startswith("## "):
            cur = pack_section_id(ln[3:])
            if cur is not None:
                secs.setdefault(cur, [])
            continue
        m = re.match(r"^- `([a-z0-9_.]+)` = .*?\((\d{4}-\d{2}-\d{2})", ln)
        if m:
            if cur is not None:
                bullet_keys[cur].append((m.group(1), m.group(2)))
            continue
        if re.match(r"^- `([a-z0-9_.]+)` = ", ln):
            if cur is not None:
                bullet_keys[cur].append((re.match(r"^- `([a-z0-9_.]+)`", ln).group(1), None))
            continue
        if META_LINE.match(ln.strip()):
            continue
        if cur is None:
            intro.append(ln)
        else:
            secs[cur].append(ln)

    # assign facts to sections
    placed = {}
    for sid, kl in bullet_keys.items():
        for k, frm in kl:
            for i, f in enumerate(facts):
                if i in placed:
                    continue
                if f["key"] == k and (frm is None or f.get("effective_from") == frm):
                    placed[i] = sid
                    break
    for i, f in enumerate(facts):
        if i not in placed:
            placed[i] = DOMAIN_TO_SEC.get(f.get("_domain"), OV.default_section(unit, f))
    # overrides of placement
    for i, f in enumerate(facts):
        s = OV.place(unit, f["key"])
        if s:
            placed[i] = s

    by_sec = defaultdict(list)
    for i, f in enumerate(facts):
        by_sec[placed[i]].append(f)
    hand_ids = {id(f) for i, f in enumerate(facts) if placed[i] == "HAND"}

    def placed_of(f):
        return "HAND" if id(f) in hand_ids else "x"

    vidx = index_by_value(facts)
    gaps_by_sec = defaultdict(list)
    for u in unresolved:
        gaps_by_sec[OV.gap_section(unit, u["key"])].append(u)

    L = []
    W = L.append
    title = NAMES[unit]
    W(f"# Annex {unit}: {title}")
    W("")
    for p in OV.intro(unit):
        W(fill(p, facts))
        W("")
    bindings = []
    residual = []

    def prose(lines, sid):
        out = []
        para = []
        for ln in lines + [""]:
            if not ln.strip():
                if para:
                    txt = clean(" ".join(para)) if not para[0].lstrip().startswith("- ") else None
                    if txt is None:
                        for b in para:
                            c = clean(b)
                            if c and c != "-":
                                out.append(c)
                    elif txt:
                        out.append(txt)
                    if out and out[-1] != "":
                        out.append("")
                    para = []
                continue
            para.append(ln)
        res = []
        for o in out:
            if not o:
                res.append(o)
                continue
            if PIPE_WORDS.search(o) and not OV.keep_pipe_line(unit, o):
                o = OV.rewrite(unit, o)
                if o is None:
                    continue
            o = OV.rewrite(unit, o) if o else o
            if o is None:
                continue
            res.append(autotag(o, vidx))
        return res

    rows_for_sec = by_sec
    nsec = 0
    for sid, stitle in SECTION_ORDER:
        narrative = secs.get(sid, [])
        flist = rows_for_sec.get(sid, [])
        extra = OV.section_text(unit, sid)
        if callable(extra):
            extra = extra(facts, value_cell, tag)
        glist = gaps_by_sec.get(sid, [])
        if not (narrative or flist or extra or glist):
            continue
        heading = OV.section_title(unit, sid) or stitle
        num = sid if sid not in ("OR", "SP", "LG") else {"OR": "14", "SP": "15", "LG": "16"}[sid]
        W(f"## {unit}.{num} {heading}")
        W("")
        if extra is not None and extra != "":
            for p in extra:
                W(fill(p, facts))
                W("")
        use_pack = OV.keep_pack_prose(unit, sid) or (extra is None and not flist and sid not in ("SP", "LG", "OR"))
        if use_pack and narrative:
            PACKPROSE.append((unit, sid))
        if use_pack:
            for p in prose(narrative, sid):
                W(p)
            if L[-1] != "":
                W("")
        flist = [f for f in flist if placed_of(f) != "HAND"]
        # state pivots
        for pv in OV.pivots(unit, sid):
            rx = re.compile(pv["regex"])
            hit = [f for f in flist if rx.match(f["key"])]
            ghit = [g for g in glist if rx.match(g["key"])]
            if not hit and not ghit:
                continue
            flist = [f for f in flist if f not in hit]
            glist = [g for g in glist if g not in ghit]
            cols = pv["columns"]
            rows = OrderedDict()
            for f in hit:
                m = rx.match(f["key"])
                gd = m.groupdict()
                st = gd.get("st") or gd.get("st2")
                fld = gd.get("fld") or gd.get("fld2") or ""
                rows.setdefault(st, {}).setdefault(fld, []).append(f)
            for g in ghit:
                m = rx.match(g["key"])
                gd = m.groupdict()
                st = gd.get("st") or gd.get("st2")
                fld = gd.get("fld") or gd.get("fld2") or ""
                rows.setdefault(st, {}).setdefault(fld, []).append(g)
            W(f"**{pv['title']}**")
            W("")
            W("| " + pv.get("rowhead", "State") + " | " + " | ".join(h for _, h in cols) + " | Effective | Source |")
            W("|---" * (len(cols) + 3) + "|")
            for st in sorted(rows, key=lambda x: (x == "default", x)):
                cells, srcs, effs = [], set(), set()
                for fld, _h in cols:
                    items = rows[st].get(fld, [])
                    parts = []
                    for it in items:
                        if "value" in it:
                            parts.append(value_cell(it))
                            srcs.add(it["register_id"])
                            effs.add(eff(it))
                            bindings.append((f"{unit}.{num} {pv['title']} / {st.upper()} / {_h}", it["key"], it["register_id"]))
                        else:
                            blk = "blocking" if it.get("blocking") else "non-blocking"
                            GAPLOC[it["key"]] = blk
                            GAPLINES[(unit, it["key"])] = (sum(x.count("\n") + 1 for x in L) + 1 + 4 + list(rows).index(st), f"{unit}.{num}")
                            cl = OV.gap_close(unit, it["key"]) or clean_close(it.get("what_would_close_it", ""))
                            parts.append(f"⚠️ RESEARCH-GAP [[GAPKEY:{it['key']}]] ({blk}): not established. Would close it: {cl}")
                    cells.append("<br>".join(parts) if parts else "—")
                W(f"| {st.upper()} | " + " | ".join(c.replace('|', '/') for c in cells) + f" | {'; '.join(sorted(effs))} | {src_cell(srcs)} |")
            W("")
        # bracket families
        fams = OrderedDict()
        singles = []
        for f in flist:
            m = re.match(r"^(.*?\.bracket(?:\.[a-z_]+)?)\.(\d+|top)\.(\w+)$", f["key"])
            if m:
                fams.setdefault(m.group(1), []).append((m.group(2), m.group(3), f))
            else:
                singles.append(f)
        for fam, items in fams.items():
            fields = list(OrderedDict((it[1], 1) for it in items).keys())
            nums = list(OrderedDict((it[0], 1) for it in items).keys())
            W(f"**{label(fam, prefix)}: bracket table**")
            W("")
            W("| Bracket | " + " | ".join(fd.replace('_', ' ') for fd in fields) + " | Effective | Source |")
            W("|---" * (len(fields) + 3) + "|")
            for n in nums:
                cells = []
                srcs = set()
                effs = set()
                for fd in fields:
                    ff = [it[2] for it in items if it[0] == n and it[1] == fd]
                    if ff:
                        cells.append(value_cell(ff[0]))
                        srcs.add(ff[0]["register_id"])
                        effs.add(eff(ff[0]))
                        bindings.append((f"{unit}.{num} {label(fam, prefix)} bracket {n} {fd}", ff[0]["key"], ff[0]["register_id"]))
                    else:
                        cells.append("—")
                W(f"| {n} | " + " | ".join(cells) + f" | {'; '.join(sorted(effs))} | {src_cell(srcs)} |")
            W("")
            OV.after_bracket(unit, fam, W)
        if singles:
            W("| Parameter | Value | Effective | Level | Source | Qualification |")
            W("|---|---|---|---|---|---|")
            for f in singles:
                note = f.get("note") or ""
                note = OV.note(unit, f["key"], note)
                if "{{" in note:
                    note = fill(note, facts)
                if note and DROP_NOTE.match(note):
                    note = ""
                note = clean_note(note)
                if note:
                    note = autotag(note, vidx, prefer_keys=(f["key"],))
                note = note.replace("|", "/")
                if f["key"] in CITE_RID and f["register_id"] not in note:
                    # QA r3c finding 2: the same fact is cited by register id in Module 2; FED.5 names it too
                    note = (note.rstrip() + f" [{f['register_id']}]").strip()
                lvl = f.get("_level") or ""
                W(f"| {label(f['key'], prefix)} | {value_cell(f)} | {eff(f)} | {lvl} | {src_cell({f['register_id']})} | {note} |")
                bindings.append((f"{unit}.{num} {label(f['key'], prefix)}", f["key"], f["register_id"]))
            W("")
        for p in OV.after_section(unit, sid):
            W(fill(p, facts))
            W("")
        if L[-1] == "" and L[-2].startswith("## "):
            W(f"No {title}-specific rule for this domain is recorded in the research.")
            W("")
        if glist:
            for g in glist:
                GAPLINES[(unit, g["key"])] = (sum(x.count("\n") + 1 for x in L) + 1, f"{unit}.{num}")
                W(gap_line(unit, g))
                W("")
    for p in OV.tail(unit):
        W(p)
        W("")
    # sources
    used = sorted({b[2] for b in bindings} | OV.extra_sources(unit))
    W(f"## {unit}.S Sources")
    W("")
    W("| Ref | Instrument | Article / section | Authority |")
    W("|---|---|---|---|")
    for rid in sorted(used, key=lambda x: int(SRC.get(x, "S9999")[1:]) if x in SRC else 9999):
        if rid not in SRC:
            src_cell({rid})
        r = REG.get(rid, {})
        W(f"| {SRC[rid]} | {autotag(clip(r.get('instrument_name', '')), vidx)} | {clip(drop_vocab_clauses(r.get('article_or_section', '')), None)} | {clip(r.get('authority', ''), 80)} |")
    W("")
    text = "\n".join(L).rstrip() + "\n"
    present = set(re.findall(r"\[\[FACT:([a-z0-9_.]+)=", text))
    missing = sorted({f["key"] for f in facts} - present)
    if missing:
        print(unit, "MISSING FACT KEYS:", missing)
    for g in unresolved:
        if g["key"] not in GAPLOC:
            print(unit, "GAP NOT PLACED:", g["key"])
    for i, ln in enumerate(text.splitlines(), 1):
        for q in quantitative_numbers(ln):
            residual.append((i, q, ln[:160]))
    return text, bindings, residual, facts, unresolved


SRC = {}
CITE_RID = {"fed.ein.format"}  # QA r3c: register id printed next to the fact (C32 alignment with m02)


def src_cell(ids):
    out = []
    for rid in sorted(ids):
        if rid not in SRC:
            SRC[rid] = f"S{len(SRC) + 1}"
        out.append(SRC[rid])
    return ", ".join(out)


def clip(s, n=160):
    s = (s or "").replace("|", "/").replace("\n", " ")
    s = re.sub(r"\[\[|\]\]", "", s)
    # CCG r3e minor 1: n=None renders the text in full (Sources locators are never truncated)
    return s if n is None or len(s) <= n else s[: n - 1].rsplit(" ", 1)[0] + " …"


GAPLOC = {}
GAPLINES = {}


def clean_close(t):
    t = clean(t)
    t = re.sub(r"\s*\((?:[^()]*?(?:browser pass|Chrome pass|curl|md5|one fetch|VPN|held file|held PDF)[^()]*)\)", "", t)
    t = re.sub(r",?\s*(?:read )?(?:via|through|with) (?:the )?(?:orchestrator )?(?:browser pass|VPN|Wayback(?: route)?)", "", t)
    t = re.sub(r"\s*(?:Parallel|parallel) fan-out per [a-z]+\.?", "", t)
    t = re.sub(r";\s*$", "", t).strip()
    t = t.replace(" read via Wayback", "").replace(" on akleg", " (Alaska Legislature site)")
    return t


def gap_line(unit, g):
    blk = "blocking" if g.get("blocking") else "non-blocking"
    GAPLOC[g["key"]] = blk
    topic = OV.gap_topic(unit, g["key"]) or (label(g["key"], unit.lower()) + ": not established by the research")
    close = OV.gap_close(unit, g["key"]) or clean_close(g.get("what_would_close_it", ""))
    return f"⚠️ RESEARCH-GAP [[GAPKEY:{g['key']}]] ({blk}): {topic}. Source that would close it: {close}"


if __name__ == "__main__":
    units = sys.argv[1:] or UNITS
    report = {}
    for u in units:
        SRC.clear()
        text, bindings, residual, facts, unresolved = build(u)
        path = os.path.join(OUT, f"annex_{u}.md")
        text = CC.finalize(f"annex_{u}.md", CC.normalize_annex(f"annex_{u}.md", text, CC.MAP_FED_CT))
        open(path, "w", encoding="utf-8", newline="\n").write(text)
        report[u] = {"path": path, "facts": len(facts), "bindings": len(bindings),
                     "keys_bound": len({b[1] for b in bindings}), "keys_in_facts": len({f['key'] for f in facts}),
                     "residual": residual, "ambiguous": AMBIG[:], "gaps": [(g["key"], g.get("blocking")) for g in unresolved],
                     "bindings_list": bindings, "c38": OV.c38(u, facts),
                     "r3d_rebind": [r for r in REBIND if r[0] == u],
                     "gaplines": {k[1]: v for k, v in GAPLINES.items() if k[0] == u}}
        report_c38 = OV.c38(u, facts)
        for line in report_c38:
            print("  C38", line)
        print(u, len(facts), "facts", len(bindings), "bindings", len(residual), "residual numbers", len(AMBIG), "ambiguous")
    json.dump(report, open(os.path.join(HERE, "report.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
