"""Pre-submission audit harness fixes (v2.9) applied during the Colombia v2.4 gate.

Fixes four matcher defects proven false-positive on CO (and, for F24/F25, previously on
BH/OM/TN/CI/CG):

  C12 (F25) — header row assumed to be row 1; every spec carries a merged title banner
              on row 1 and the real 21-column header on row 2.
  C20 (F24) — spec traceability strips separators from the filename but not the filing_id,
              so a semantic dashed id can never match a sequence-number filename.
  C27       — System Mapping values are dotted identifiers (Payroll.Basic_Salary) while the
              DD names fields in prose ("Employee Document Type"); the substring test can
              never match across that convention gap.
  C33       — the "non-Latin script" test excludes only a hand-list of punctuation, so
              ordinary mathematical/typographic symbols are misread as foreign script.

C29 was patched separately (ALL-CAPS marker convention vs the Spanish word "todo").
"""
from pathlib import Path

p = Path(__file__).with_name('_audit_v24_mechanical.py')
src = p.read_text(encoding='utf-8')
orig = src

# --------------------------------------------------------------------------- C12
old12 = """            headers = [str(c.value).lower() if c.value else ''
                       for c in next(spec_sheet.iter_rows(max_row=1))]
            matched = sum(1 for kw in STANDARD if any(kw in h for h in headers))"""
new12 = """            # v2.9 fix (F25): the spec sheets carry a merged single-cell TITLE BANNER on
            # row 1 and the real column headers on row 2. Scan the first 3 rows and keep
            # the best match instead of assuming the header is on row 1.
            matched = 0
            for _row in spec_sheet.iter_rows(min_row=1, max_row=3):
                headers = [str(c.value).lower() if c.value else '' for c in _row]
                if len([h for h in headers if h]) < 2:
                    continue                     # merged title banner, not a header row
                _m = sum(1 for kw in STANDARD if any(kw in h for h in headers))
                if _m > matched:
                    matched = _m"""
assert old12 in src, 'C12 anchor not found'
src = src.replace(old12, new12)

# --------------------------------------------------------------------------- C20
old20 = """        for filing in in_scope:
            fid = filing.get('filing_id', '')
            if not any(fid.lower().replace(' ', '') in s.name.lower().replace('_', '').replace('-', '') for s in spec_files):
                missing_specs.append(fid)"""
new20 = """        def _norm(x):
            return ''.join(ch for ch in str(x).lower() if ch.isalnum())
        for filing in in_scope:
            fid = filing.get('filing_id', '')
            # v2.9 fix (F24): prefer the explicit spec_file link when the manifest carries
            # one; only fall back to fuzzy matching when it is absent, and then strip the
            # separators from BOTH sides of the comparison.
            declared = filing.get('spec_file')
            if declared:
                if (spec_dir / declared).exists():
                    continue
                missing_specs.append(fid + ' (declared spec_file missing on disk: '
                                     + str(declared) + ')')
                continue
            if not any(_norm(fid) in _norm(s.name) for s in spec_files):
                missing_specs.append(fid)"""
assert old20 in src, 'C20 anchor not found'
src = src.replace(old20, new20)

# --------------------------------------------------------------------------- C27
old27 = """                    if any(term in low for term in dd_terms):
                        continue
                    unresolved.append(f'{sp.name}: \"{str(sysmap)[:40]}\"')"""
new27 = """                    if any(term in low for term in dd_terms):
                        continue
                    # v2.9 fix: System Mapping values are dotted identifiers
                    # (Payroll.Basic_Salary, Employee.Document_Type) while the DD names its
                    # fields in prose ("Employee Document Type"). Compare on an
                    # alphanumeric-only normalisation so the naming convention does not
                    # defeat the link. Also treat the canonical system namespaces as a
                    # structural class - they are pipeline-side, not country DD fields.
                    if sysmap.strip().lower() in ('system mapping',):
                        continue                 # header row picked up by min_row=2
                    if any(sysmap.strip().startswith(ns) for ns in
                           ('PayPeriod.', 'System.', 'Constant')):
                        continue                 # structural / system-derived
                    _n = _c27_norm(sysmap)
                    if any(t and (t in _n or _n in t) for t in dd_norm):
                        continue
                    _tail_hit = False
                    for _tok in _c27_tokens(sysmap):
                        _base = _c27_norm(_tok.split('.')[-1])
                        if len(_base) > 5 and any(_base in t for t in dd_norm):
                            _tail_hit = True
                            break
                    if _tail_hit:
                        continue
                    unresolved.append(f'{sp.name}: \"{str(sysmap)[:40]}\"')"""
assert old27 in src, 'C27 anchor not found'
src = src.replace(old27, new27)

old27h = """        DERIVED = ('derived', 'computed', 'system-generated', 'manual', 'free-text', 'free text', 'sequence', 'ordinal', 'sum(', 'round(')"""
new27h = """        DERIVED = ('derived', 'computed', 'system-generated', 'manual', 'free-text', 'free text', 'sequence', 'ordinal', 'sum(', 'round(')
        import re as _re27
        def _c27_norm(x):
            return ''.join(ch for ch in str(x).lower() if ch.isalnum())
        def _c27_tokens(x):
            return _re27.findall(r'[A-Za-z][A-Za-z0-9_.]{3,}', str(x))
        dd_norm = set()
        for _t in dd_terms:
            _v = _c27_norm(_t)
            if len(_v) > 6:
                dd_norm.add(_v)"""
assert old27h in src, 'C27 header anchor not found'
src = src.replace(old27h, new27h)

# --------------------------------------------------------------------------- C33
# The original is a dense regex literal; anchor on the assignment line and replace the
# comment line above it plus the literal itself, by index.
_lines = src.split('\n')
_i = [k for k, l in enumerate(_lines) if l.strip().startswith('nonlatin_re = _re.compile(')]
assert len(_i) == 1, 'C33 anchor not found (%d matches)' % len(_i)
_i = _i[0]
_start = _i - 1 if _lines[_i - 1].strip().startswith('# non-Latin letter') else _i
old33 = '\n'.join(_lines[_start:_i + 1])
new33 = """        # v2.9 fix: the previous test excluded only a hand-written list of punctuation, so
        # ordinary mathematical and typographic symbols that appear in perfectly English
        # prose - the rightwards arrow, minus sign, section sign, middle dot, <=, >=, +-,
        # sigma, almost-equal - were reported as "non-Latin script". Detect on the Unicode
        # general category instead: only a LETTER outside the Latin blocks is script
        # leakage. Symbols, punctuation and marks can never be.
        import unicodedata as _ud
        _MATH_LETTERS = set('\\u03a3\\u03a0\\u0394\\u03bc\\u03c3\\u03b1\\u03b2\\u03bb\\u03a9\\u03b8\\u03c0')
        def _nonlatin_chars(text):
            out = []
            for ch in text:
                if ch in _MATH_LETTERS:
                    continue                     # mathematical notation, not prose
                if not _ud.category(ch).startswith('L'):
                    continue                     # symbol / punctuation / digit / mark
                o = ord(ch)
                if o < 0x0250 or 0x1E00 <= o <= 0x1EFF:
                    continue                     # Basic Latin + Latin-1/Extended-A/B/Additional
                out.append(ch)
            return out
        class _NonLatin(object):
            @staticmethod
            def search(text):
                return bool(_nonlatin_chars(text))
        nonlatin_re = _NonLatin()"""
assert old33 in src, 'C33 anchor not found'
src = src.replace(old33, new33)

p.write_text(src, encoding='utf-8')
import py_compile
py_compile.compile(str(p), doraise=True)
print('patched OK  (+%d bytes)  compiles clean' % (len(src) - len(orig)))
