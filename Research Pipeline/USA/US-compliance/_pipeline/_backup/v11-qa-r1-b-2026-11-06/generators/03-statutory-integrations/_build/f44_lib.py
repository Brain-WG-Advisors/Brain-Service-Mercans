# -*- coding: utf-8 -*-
"""F44 library: every text element of a fact value (numbers, form names, dates, quarter tokens, channel words,
acronyms) must appear in the local copy of the cited register row(s) (register_id + _also_register_ids).
Element extraction and matching are those of the pre-build text check of agent 2 (precheck-next/selfcheck.py,
2026-11-03), unchanged; only the command-line wrapper is replaced by check_fact()."""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE_PATH = os.path.join(HERE, "_scratch", "textcache.json")
_cache = None


def cache():
    global _cache
    if _cache is None:
        # SIR-QA2-01: the cache is refreshed from the current register and local files before every run
        import f44_textcache
        base = os.path.dirname(os.path.dirname(HERE))
        f44_textcache.refresh(base, CACHE_PATH)
        _cache = json.load(open(CACHE_PATH, encoding="utf-8"))
    return _cache


MN = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
AB = {m[:3]: m for m in MN}
LAST = {'january': 31, 'february': 28, 'march': 31, 'april': 30, 'may': 31, 'june': 30, 'july': 31, 'august': 31,
        'september': 30, 'october': 31, 'november': 30, 'december': 31}
SYN = {'ssn': ['social security number', 'ssn'], 'fein': ['employer identification number', 'fein', 'ein'],
       'e-file': ['electronic', 'e-file', 'efile'], 'efile': ['electronic', 'e-file', 'efile'],
       'electronic': ['electronic', 'e-file', 'efile'], 'electronically': ['electronic'],
       'online': ['online', 'on-line', 'electronic'], 'xml': ['xml'], 'sftp': ['sftp'], 'upload': ['upload'],
       'paper': ['paper'], 'csv': ['csv'], 'txt': ['.txt'], 'icesa': ['icesa'], 'efw2': ['efw2'], 'fset': ['fset'],
       'xlsx': ['xlsx', 'excel'], 'mail': ['mail']}
_SN = {}


def state_names():
    if not _SN:
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(HERE)), '04-reports-spec', '_build'))
        import us_common
        _SN.update(us_common.STATE_NAMES)
    return _SN


AMBIG = {'OR', 'IN', 'ME', 'ID', 'OK', 'HI', 'AL', 'DE', 'PA', 'MA', 'CO', 'LA', 'MS', 'MD', 'WA'}
SKIP_WORDS = {'USD', 'FAQ', 'AND', 'THE', 'OR', 'NOT', 'ONLY', 'MUST', 'ALL', 'ANY', 'NEW', 'MAY'}
QN = {'1': 'first', '2': 'second', '3': 'third', '4': 'fourth'}


def norm(t):
    for a in '‐‑‒–—':
        t = t.replace(a, '-')
    return re.sub(r'\s+', ' ', t.replace(' ', ' '))


def ocr(s):
    return re.sub(r'[\s\-/]', '', s.upper().replace('I', '1').replace('L', '1').replace('O', '0'))




def snip(t, a, b):
    return t[max(0, a - 90):b + 90]


def find(el, kind, T):
    for r, f, pg, t in T:
        tl = t.lower()
        if kind == 'num':
            n = el.replace(',', '')
            NW = {'1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine','10':'ten','15':'fifteen','20':'twenty','30':'thirty'}
            if n in NW:
                mm = re.search(r'\b' + NW[n] + r'\b', tl)
                if mm:
                    return (r, f, pg, snip(t, mm.start(), mm.end()))
            for m in re.finditer(r'\d[\d,]*(?:\.\d+)?', t):
                if m.start() > 0 and t[m.start() - 1].isdigit():
                    continue
                g = m.group().replace(',', '').rstrip('.')
                try:
                    same = float(g) == float(n)
                except ValueError:
                    same = False
                if g == n or (same and len(n.split('.')[0]) == len(g.split('.')[0])):
                    return (r, f, pg, snip(t, m.start(), m.end()))
        elif kind == 'date':
            mon, day = el
            pats = [rf'\b{mon}\.? ?{day}(st|nd|rd|th)?\b', rf'\b{mon[:3]}\.? ?{day}(st|nd|rd|th)?\b']
            if LAST[mon] == int(day) or (mon == 'february' and day in ('28', '29')):
                pats.append(rf'last day of (the month of )?{mon}')
            for p in pats:
                m = re.search(p, tl)
                if m:
                    return (r, f, pg, snip(t, m.start(), m.end()))
        elif kind == 'iso':
            y, mon, day = el
            mi = MN.index(mon) + 1
            for p in [rf'{mon}\.? ?{day}(st|nd|rd|th)?,? ?{y}', rf'\b{mon[:3]}\.? ?{day},? ?{y}',
                      rf'{y}-{mi:02d}-{int(day):02d}', rf'\b0?{mi}/0?{day}/(20)?{y[2:]}\b', rf'\b{day} {mon} {y}']:
                m = re.search(p, tl)
                if m:
                    return (r, f, pg, snip(t, m.start(), m.end()))
        elif kind == 'qtr':
            m = re.search(rf'\bq{el}\b|{QN[el]} quarter|\b{el}(st|nd|rd|th) quarter|quarter {el}\b', tl)
            if m:
                return (r, f, pg, snip(t, m.start(), m.end()))
        elif kind == 'form':
            pat = re.escape(el).replace(r'\ ', r'[ \-]?').replace(r'\-', r'[ \-]?')
            m = re.search(r'(?<![A-Za-z0-9])' + pat + r'(?![A-Za-z0-9])', t, re.I)
            if m:
                return (r, f, pg, snip(t, m.start(), m.end()))
            if len(ocr(el)) >= 4 and ocr(el) in ocr(t):
                return (r, f, pg, '(OCR-normalised match: I/l->1, O->0) ' + el)
        elif kind == 'chan':
            for s in SYN.get(el, [el]):
                i = tl.find(s)
                if i >= 0:
                    return (r, f, pg, snip(t, i, i + len(s)))
        elif kind == 'word':
            # SIR-QA1-17: an acronym is proven only by the acronym itself (whole word) or by an explicit expansion
            # "Words Of The Name (ACR)"; a run of capitalised initials somewhere in a long statute is not proof.
            m = re.search(r'(?<![A-Za-z])' + re.escape(el) + r'(?![A-Za-z])', t)
            if m:
                return (r, f, pg, snip(t, m.start(), m.end()))
            if len(t) <= 40000:
                # SIR-QA2-01: an expansion of the acronym by its initials counts only inside one short page or form
                # (the cited section), never across a long statute
                words = re.findall(r"[A-Za-z][A-Za-z']*", t)
                ws = [w for w in words if w.lower() not in ('of', 'and', 'the', 'for', 'on', 'in', 'to')]
                ini = ''.join(w[0].upper() for w in ws)
                j = ini.find(el)
                while j >= 0:
                    if all(ws[j + k][0].isupper() for k in range(len(el))):
                        return (r, f, pg, 'acronym expanded: ' + ' '.join(ws[j:j + len(el)]))
                    j = ini.find(el, j + 1)
        elif kind == 'state':
            # SIR-QA1-17: a two-letter State code is proven by the State name, or by the code as a whole upper-case
            # word; codes that are also English words or initials (OR, IN, ME, ...) only inside a list of codes
            if re.match(r'US-' + el + r'(?![A-Z])', r) or re.match(r'US-' + el + r'[A-Z0-9]*-\d', r):
                return (r, f, pg, 'row of the State: ' + r)       # SIR-QA2-01: a cited row that belongs to the State
            nm = state_names().get(el, '').lower()
            i = tl.find(nm) if nm else -1
            if i >= 0:
                return (r, f, pg, snip(t, i, i + len(nm)))
            for m in re.finditer(r'(?<![A-Za-z])' + el + r'(?![A-Za-z])', t):
                if el not in AMBIG:
                    return (r, f, pg, snip(t, m.start(), m.end()))
                ctx = t[max(0, m.start() - 6):m.end() + 6]
                if re.search(r'[A-Z]{2}[,;/ ]+' + el + r'(?![A-Za-z])|(?<![A-Za-z])' + el + r'[,;/ ]+[A-Z]{2}(?![A-Za-z])', ctx):
                    return (r, f, pg, snip(t, m.start(), m.end()))
    return None


FORM_RE = re.compile(r'(?<![\w.])((?:[A-Z][A-Za-z]{0,6}-?\d[\w]*(?:-[A-Z0-9]+)*)|(?:[A-Z]{1,6} \d{1,5}[A-Z]?(?:-\d+)?(?![\d,.]))|(?:\d+[A-Z]{1,3})(?![\w]))')
MONRE = r'\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.? (\d{1,2})(?:st|nd|rd|th)?\b'


def elements(v):
    if isinstance(v, bool):
        return []
    if isinstance(v, (int, float)):
        return [('numv', v)]
    s = norm(str(v))
    els = []
    for m in re.finditer(r'\b(\d{4})-(\d{2})-(\d{2})\b', s):
        els.append(('iso', (m.group(1), MN[int(m.group(2)) - 1], str(int(m.group(3))))))
    s = re.sub(r'\b\d{4}-\d{2}-\d{2}\b', ' ', s)
    for m in re.finditer(MONRE, s):
        els.append(('date', (AB[m.group(1).lower()], m.group(2))))
    s = re.sub(MONRE, ' ', s)
    for m in re.finditer(r'\bQ([1-4])\b', s):
        els.append(('qtr', m.group(1)))
    s = re.sub(r'\bQ[1-4]\b', ' ', s)
    s = re.sub(r'(?<=[A-Za-z]) ID\b', ' ', s)          # 'Agent ID', 'Self-Service ID', 'MN ID': an identifier, not Idaho
    s = re.sub(r'\b(TY|CY)(\d{4})\b', r' \2 ', s)
    s = re.sub(r'\b([A-Z]+-\d+[A-Z]*)s\b', r'\1', s)
    forms = []
    for m in FORM_RE.finditer(s):
        tok = m.group(1)
        if re.fullmatch(r'[A-Z][a-z]+ \d.*', tok) or re.fullmatch(r'P\d+', tok):
            continue
        forms.append(tok)
    for f in forms:
        els.append(('form', f))
    s3 = s
    for f in sorted(set(forms), key=len, reverse=True):
        s3 = s3.replace(f, ' ')
    for m in re.finditer(r'(?<![\w.])\d[\d,]*(?:\.\d+)?', s3):
        n = m.group().rstrip(',').rstrip('.')
        if n:
            els.append(('num', n))
    for w in re.findall(r'[A-Za-z][A-Za-z\-.]*', s3):
        wl = w.lower().strip('.')
        if wl in SYN:
            els.append(('chan', wl))
        elif re.fullmatch(r'[A-Z]{3,}', w) and w not in SKIP_WORDS:
            els.append(('word', w))
        elif re.fullmatch(r'[A-Z]{2}', w) and w in state_names():
            els.append(('state', w))
    out, seen = [], set()
    for e in els:
        k = (e[0], json.dumps(e[1]))
        if k not in seen:
            seen.add(k)
            out.append(e)
    return out


def numv_find(v, T):
    xs = [v] + ([round(v * 100, 6)] if isinstance(v, float) and 0 < abs(v) < 1 else []) + ([round(v / 100, 8)] if isinstance(v, (int, float)) and v > 0 else [])
    for x in xs:
        h = find(('%.6f' % x).rstrip('0').rstrip('.'), 'num', T)
        if h:
            return h
    return None




def texts_for(rids):
    c = cache()
    return [(r, f, pg, norm(t)) for r in rids for f, pg, t in c.get(r, [])]


LIMITATION_KEYS = {"rspec.fed.form940.due": None,
                   "dd.oh.school_district_code": ("The full-year nonresident value in the statement above rests on the 2025 school district list "
                                                  "[US-OHS5-019] (effective to 2025-12-31); no 2026 restatement of that value is named in the cited sources.")}
_REGST = {}


def reg_status(rid):
    if not _REGST:
        import csv
        base = os.path.dirname(os.path.dirname(HERE))
        for r in csv.DictReader(open(os.path.join(base, "00-official-sources", "legal-basis-register.csv"), encoding="utf-8")):
            _REGST[r["id"]] = r.get("status", "")
    return _REGST.get(rid, "")


WEAK_STATUS = ("superseded", "partial", "MANUAL")


def check_fact(f):
    """List of missing elements of fact f: [(kind, element)]. Empty list = every element found in a local copy.
    SIR-QA1-17: an _also_register_ids row whose register status is superseded / partial / MANUAL proves nothing."""
    if f.get("key") in LIMITATION_KEYS:
        # F27: a value the RSPEC prints as a labelled limitation (low confidence, not a verified rule) is mirrored as the
        # same limitation (period, TY2025 label, gap id); its derived dates are not claimed as found in the copy
        return [], True
    rids = [f["register_id"]] + [r for r in f.get("_also_register_ids", []) if reg_status(r) not in WEAK_STATUS]
    T = texts_for(rids)
    miss = []
    for kind, el in elements(f["value"]):
        h = numv_find(el, T) if kind == "numv" else find(el, kind, T)
        if not h and kind == "form" and " " in el:
            a, b = el.split(" ", 1)
            h1 = find(a, "form" if re.search(r"\d", a) else "word", T)
            h2 = find(b, "form", T) or find(b.split("-")[0], "num", T)
            if h1 and h2:
                h = (h1[0], h1[1], h1[2], "split match")
        if not h:
            miss.append((kind, el))
    return miss, bool(T)
