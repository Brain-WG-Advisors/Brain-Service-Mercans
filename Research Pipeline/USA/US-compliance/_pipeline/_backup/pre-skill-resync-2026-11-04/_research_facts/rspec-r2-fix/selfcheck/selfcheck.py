"""RSPEC r2 self-check: every text element of every RSPEC-bound fact value must be found in the
local copy of the cited register row(s): register_id plus _also_register_ids.
Elements: dates (Mon D / ISO), quarter tokens, form identifiers, numbers, channel words, acronyms."""
import json, csv, re, sys, os, glob
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE, CACHE, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
cache = json.load(open(CACHE, encoding='utf-8'))
binds = list(csv.DictReader(open(os.path.join(BASE, '_pipeline/RSPEC-bindings.csv'), encoding='utf-8')))
bkeys = {(b['key'], b['facts_file']) for b in binds}
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
SKIP_WORDS = {'USD', 'FAQ', 'AND', 'THE', 'OR'}
QN = {'1': 'first', '2': 'second', '3': 'third', '4': 'fourth'}


def norm(t):
    for a in '‐‑‒–—':
        t = t.replace(a, '-')
    return re.sub(r'\s+', ' ', t.replace(' ', ' '))


def ocr(s):
    return re.sub(r'[\s\-/]', '', s.upper().replace('I', '1').replace('L', '1').replace('O', '0'))


def texts(rids):
    return [(r, f, pg, norm(t)) for r in rids for f, pg, t in cache.get(r, [])]


def snip(t, a, b):
    return t[max(0, a - 90):b + 90]


def find(el, kind, T):
    for r, f, pg, t in T:
        tl = t.lower()
        if kind == 'num':
            n = el.replace(',', '')
            NW = {'1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine','10':'ten','15':'fifteen','20':'twenty','30':'thirty'}
            if n in NW:
                mm = re.search(r'' + NW[n] + r'', tl)
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
            words = re.findall(r"[A-Za-z][A-Za-z']*", t)
            stop = {'of', 'and', 'the', 'for', 'on', 'in', '&', 'to'}
            ws = [w for w in words if w.lower() not in stop]
            L = len(el)
            ini = ''.join(w[0].upper() for w in ws)
            j = ini.find(el)
            if j >= 0 and all(ws[j + k][0].isupper() for k in range(L)):
                return (r, f, pg, 'acronym expanded: ' + ' '.join(ws[j:j + L]))
            m = re.search(r'(?<![A-Za-z])' + re.escape(el) + r'(?![A-Za-z])', t)
            if m:
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
    out, seen = [], set()
    for e in els:
        k = (e[0], json.dumps(e[1]))
        if k not in seen:
            seen.add(k)
            out.append(e)
    return out


def numv_find(v, T):
    xs = [v] + ([round(v * 100, 6)] if isinstance(v, float) and v < 1 else [])
    for x in xs:
        h = find(('%.6f' % x).rstrip('0').rstrip('.'), 'num', T)
        if h:
            return h
    return None


res, miss = [], []
for fn in sorted(glob.glob(os.path.join(BASE, '_research', '*-facts.json'))):
    ff = os.path.basename(fn)
    d = json.load(open(fn, encoding='utf-8'))
    for f in d.get('facts', []):
        if (f['key'], ff) not in bkeys:
            continue
        rids = [f['register_id']] + list(f.get('_also_register_ids', []))
        T = texts(rids)
        for kind, el in elements(f['value']):
            h = numv_find(el, T) if kind == 'numv' else find(el, kind, T)
            if not h and kind == 'form' and ' ' in el:
                a, b = el.split(' ', 1)
                h1 = find(a, 'form' if re.search(r'\d', a) else 'word', T)
                h2 = find(b, 'form', T) or find(b.split('-')[0], 'num', T)
                if h1 and h2:
                    h = (h1[0], h1[1], h1[2], 'split match: ' + h1[3] + ' || ' + h2[3])
            rec = {'file': ff, 'key': f['key'], 'effective_from': f.get('effective_from'), 'rids': rids, 'kind': kind,
                   'element': el, 'found': bool(h), 'where': list(h) if h else None, 'no_copy': not T}
            res.append(rec)
            if not h:
                miss.append(rec)
bound = {k for k, _ in bkeys}
seen_keys = {r['key'] for r in res}
json.dump({'checked_elements': len(res), 'keys_checked': len(seen_keys), 'bound_keys': len(bound),
           'misses': miss, 'all': res}, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('elements', len(res), 'keys', len(seen_keys), 'of bound', len(bound), 'misses', len(miss),
      'keys with miss', len({m['key'] for m in miss}))
