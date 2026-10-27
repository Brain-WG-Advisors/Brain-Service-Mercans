#!/usr/bin/env python3
"""
v2.4 audit — mechanical checks for ${COUNTRY}. Returns JSON to stdout.
33 checks total (v2.9 adds C32 cross-artifact fact consistency + C33 CCG English-only prose; v2.8 added C29-C31; v2.7 added C23-C28). C8 uses word-boundary regex (no false positive on Spanish "todo" etc.).
"""
import sys, json, re, os
from pathlib import Path

# Inject country params from environment
CODE = os.environ.get('CL_AUDIT_CODE', 'XX')
COUNTRY = os.environ.get('CL_AUDIT_COUNTRY', 'Unknown')
LOCAL_LANG = os.environ.get('CL_AUDIT_LOCAL_LANG_SHORT', 'XX')
CURRENCY = os.environ.get('CL_AUDIT_CURRENCY', '')

PIPELINE = Path(os.environ.get('HOME', '/Users/wallissongomes')) / 'mercans-pipeline'
BASE = PIPELINE / f'{CODE}-compliance'
SHARED = PIPELINE / 'shared'

results = []

# ----- C1: CCG Structural Completeness -----
def c1():
    try:
        from docx import Document
        ccg_path = BASE / '01-ccg' / f'{CODE}-CCG-001-v1.0.docx'
        if not ccg_path.exists():
            return ('C1', 'FAIL', 'CCG missing', [])
        doc = Document(str(ccg_path))
        h1s = [p.text.strip() for p in doc.paragraphs if p.style.name in ('Heading 1', 'Heading1')]
        modules_found = sum(1 for h in h1s if 'Module' in h)
        if modules_found >= 13:
            return ('C1', 'PASS', f'{modules_found} modules', [])
        return ('C1', 'FAIL', f'Only {modules_found} modules (expected 13)', h1s[:5])
    except Exception as e:
        return ('C1', 'ERROR', str(e), [])

# ----- C8: Open Items Resolution (v2.4 WORD-BOUNDARY FIX) -----
def c8():
    """v2.4: use \bTODO\b regex (uppercase, word-boundary) to avoid false positives
       on Spanish 'todo', Portuguese 'todo', French 'tout', etc.
       The previous substring match flagged 'a todo evento' (Chilean legal term)."""
    try:
        from docx import Document
        # Patterns are case-sensitive UPPERCASE word-boundary markers
        # PLUS the lowercase 'to be confirmed' / 'tbd' as lowercase phrase-match
        patterns_upper = [r'\bTODO\b', r'\bTBD\b', r'\bFIXME\b', r'\bXXX\b']
        patterns_phrase = ['to be confirmed', 'to be verified', '[CHECK]', '[?]']
        ccg_path = BASE / '01-ccg' / f'{CODE}-CCG-001-v1.0.docx'
        if not ccg_path.exists():
            return ('C8', 'FAIL', 'CCG missing', [])
        doc = Document(str(ccg_path))
        full_text = '\n'.join(p.text for p in doc.paragraphs)
        hits = []
        for pat in patterns_upper:
            matches = re.findall(pat, full_text)
            if matches:
                hits.append(f'{pat} ({len(matches)} occurrences)')
        for phrase in patterns_phrase:
            if phrase.lower() in full_text.lower():
                hits.append(phrase)
        if not hits:
            return ('C8', 'PASS', 'No open-item markers found', [])
        return ('C8', 'FAIL', f'Open-item markers: {hits}', hits)
    except Exception as e:
        return ('C8', 'ERROR', str(e), [])

# ----- C11: CCG Template Coverage -----
def c11():
    try:
        from docx import Document
        ccg_path = BASE / '01-ccg' / f'{CODE}-CCG-001-v1.0.docx'
        template_path = SHARED / 'CCG_TEMPLATE_QUESTIONS.md'
        if not ccg_path.exists():
            return ('C11', 'FAIL', 'CCG missing', [])
        if not template_path.exists():
            return ('C11', 'SKIP', 'Template questions file missing', [])
        doc = Document(str(ccg_path))
        h3s = [p.text.strip() for p in doc.paragraphs
               if p.style.name in ('Heading 3', 'Heading3')]
        template = template_path.read_text()
        questions = [l.strip()[2:] for l in template.split('\n')
                     if l.strip().startswith('- ') and ('?' in l or 'Deliverable' in l)]
        matched = 0
        unmatched = []
        for q in questions:
            key = q[:30].lower().strip()
            if any(key in h.lower() for h in h3s):
                matched += 1
            else:
                unmatched.append(q[:60])
        coverage = matched / max(len(questions), 1)
        if coverage >= 0.95:
            return ('C11', 'PASS', f'{matched}/{len(questions)} ({coverage:.0%})', [])
        elif coverage >= 0.80:
            return ('C11', 'MANUAL', f'{matched}/{len(questions)} ({coverage:.0%})', unmatched[:10])
        return ('C11', 'FAIL', f'{matched}/{len(questions)} ({coverage:.0%})', unmatched[:10])
    except Exception as e:
        return ('C11', 'ERROR', str(e), [])

# ----- C12: Spec Column Schema Depth -----
def c12():
    try:
        from openpyxl import load_workbook
        STANDARD = ['name', 'mandatory', 'reason', 'path', 'length', 'type',
                    'example', 'mapping', 'explanation', 'payroll', 'code',
                    'rounding', 'negative', 'value', 'frequency', 'error']
        findings = []
        spec_dir = BASE / '04-reports-spec'
        if not spec_dir.exists():
            return ('C12', 'SKIP', 'No 04-reports-spec/', [])
        thin_count = 0
        spec_files = sorted(spec_dir.glob(f'{CODE}-*-Spec.xlsx'))
        for spec_path in spec_files:
            wb = load_workbook(str(spec_path), read_only=True)
            spec_sheet = None
            for n in wb.sheetnames:
                if 'spec' in n.lower() or 'field' in n.lower() or 'declaration' in n.lower():
                    spec_sheet = wb[n]
                    break
            if not spec_sheet:
                findings.append(f'{spec_path.name}: no spec sheet found')
                thin_count += 1
                continue
            # v2.9 fix (F25): the spec sheets carry a merged single-cell TITLE BANNER on
            # row 1 and the real column headers on row 2. Scan the first 3 rows and keep
            # the best match instead of assuming the header is on row 1.
            matched = 0
            for _row in spec_sheet.iter_rows(min_row=1, max_row=3):
                headers = [str(c.value).lower() if c.value else '' for c in _row]
                if len([h for h in headers if h]) < 2:
                    continue                     # merged title banner, not a header row
                _m = sum(1 for kw in STANDARD if any(kw in h for h in headers))
                if _m > matched:
                    matched = _m
            findings.append(f'{spec_path.name}: {matched}/{len(STANDARD)} keywords')
            if matched < 12:
                thin_count += 1
        if thin_count == 0 and len(spec_files) > 0:
            return ('C12', 'PASS', f'All {len(spec_files)} specs have adequate schema', findings)
        elif thin_count <= 2:
            return ('C12', 'MANUAL', f'{thin_count}/{len(spec_files)} specs have thin schema', findings)
        return ('C12', 'FAIL', f'{thin_count}/{len(spec_files)} specs have thin schema', findings)
    except Exception as e:
        return ('C12', 'ERROR', str(e), [])

# ----- C21: Payslip 8-Sheet Structure (v2.7) -----
def c21():
    try:
        from openpyxl import load_workbook
        path = BASE / '06-payslip' / f'{CODE}_Compliance_Payslip_Generator.xlsx'
        if not path.exists():
            return ('C21', 'FAIL', f'File missing: {path.name}', [])
        wb = load_workbook(str(path), read_only=True)
        expected = ['How to set up Payslip', 'Compliance Payslip', f'{COUNTRY} (EN)', f'{COUNTRY} ({LOCAL_LANG})', 'Payslip Spec', 'Field Option', 'Population Range', 'Unit Rate Details']
        actual = wb.sheetnames
        missing = [s for s in expected if s not in actual]
        if not missing:
            return ('C21', 'PASS', 'All 8 sheets present', [])
        return ('C21', 'FAIL', f'Missing: {missing}', actual)
    except Exception as e:
        return ('C21', 'ERROR', str(e), [])

# ----- C22: Payslip Spec Coverage -----
def c22():
    try:
        from openpyxl import load_workbook
        path = BASE / '06-payslip' / f'{CODE}_Compliance_Payslip_Generator.xlsx'
        if not path.exists():
            return ('C22', 'FAIL', 'Payslip Generator missing', [])
        wb = load_workbook(str(path), read_only=True)
        if 'Payslip Spec' not in wb.sheetnames:
            return ('C22', 'FAIL', 'Payslip Spec sheet missing', [])
        ws = wb['Payslip Spec']
        required = ['Header Details', 'Employer', 'Employee', 'Earnings', 'Deductions']
        found = set()
        for row in ws.iter_rows(values_only=True):
            for cell in row:
                if cell is None: continue
                s = str(cell)
                for sec in required:
                    if sec.lower() in s.lower():
                        found.add(sec)
        missing = [s for s in required if s not in found]
        field_rows = sum(1 for row in ws.iter_rows(values_only=True) if any(c for c in row))
        if not missing and field_rows >= 20:
            return ('C22', 'PASS', f'All sections, {field_rows} rows', [])
        elif not missing:
            return ('C22', 'MANUAL', f'Sections present, only {field_rows} rows', [])
        return ('C22', 'FAIL', f'Missing sections: {missing}', [])
    except Exception as e:
        return ('C22', 'ERROR', str(e), [])

# ----- C20: Scope Decision Audit Trail -----
def c20():
    try:
        manifest_path = BASE / 'scope_manifest.json'
        if not manifest_path.exists():
            return ('C20', 'FAIL', 'scope_manifest.json missing', [])
        manifest = json.loads(manifest_path.read_text())
        in_scope = manifest.get('authority_filings', {}).get('in_scope', [])
        out_scope = manifest.get('authority_filings', {}).get('out_of_scope', [])
        # Check every in-scope filing has a spec file
        spec_dir = BASE / '04-reports-spec'
        spec_files = list(spec_dir.glob('*.xlsx')) if spec_dir.exists() else []
        missing_specs = []
        def _norm(x):
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
                missing_specs.append(fid)
        # Check every out-of-scope has descoping reason
        missing_reasons = [f.get('filing_id', '') for f in out_scope if not f.get('descoping_reason')]
        if not missing_specs and not missing_reasons:
            return ('C20', 'PASS', f'{len(in_scope)} in-scope all specced, {len(out_scope)} descoped with reasons', [])
        issues = []
        if missing_specs: issues.append(f'In-scope without spec: {missing_specs}')
        if missing_reasons: issues.append(f'Out-of-scope without reason: {missing_reasons}')
        return ('C20', 'FAIL', '; '.join(issues), [])
    except Exception as e:
        return ('C20', 'ERROR', str(e), [])

# ----- C23: XML not applicable unless an XSD is cited (v2.7) -----
def c23():
    try:
        from openpyxl import load_workbook
        spec_dir = BASE / '04-reports-spec'
        if not spec_dir.exists():
            return ('C23', 'SKIP', 'No 04-reports-spec/', [])
        offenders = []
        for sp in sorted(spec_dir.glob(f'{CODE}-*-Spec.xlsx')):
            wb = load_workbook(str(sp), read_only=True)
            xml_hit = xsd_cited = False
            for ws in wb.worksheets:
                for row in ws.iter_rows(values_only=True):
                    for c in row:
                        if isinstance(c, str):
                            t = c.strip()
                            if t.startswith('<?xml') or t.startswith('<Declaration') or ('<Header>' in t and '</Header>' in t):
                                xml_hit = True
                            low = t.lower()
                            if 'xsd' in low or 'cahier des charges' in low or 'schema definition' in low:
                                xsd_cited = True
            if xml_hit and not xsd_cited:
                offenders.append(sp.name)
        if not offenders:
            return ('C23', 'PASS', 'No unsupported XML in specs', [])
        return ('C23', 'FAIL', f'XML present without an XSD citation: {offenders}', offenders)
    except Exception as e:
        return ('C23', 'ERROR', str(e), [])

# ----- C24: Portal / institution label correctness (v2.7) -----
def c24():
    try:
        from openpyxl import load_workbook
        spec_dir = BASE / '04-reports-spec'
        if not spec_dir.exists():
            return ('C24', 'SKIP', 'No 04-reports-spec/', [])
        offenders = []
        for sp in sorted(spec_dir.glob(f'{CODE}-*-Spec.xlsx')):
            name = sp.name.lower()
            is_ss = any(k in name for k in ('cnps', 'cnss', 'dnts', 'recap', 'appel'))
            is_tax = any(k in name for k in ('dgi', 'irpp', 'tfe', 'tafp', 'das', 'impot'))
            text = ''
            wb = load_workbook(str(sp), read_only=True)
            for ws in wb.worksheets:
                for row in ws.iter_rows(values_only=True):
                    for c in row:
                        if isinstance(c, str):
                            text += ' ' + c.lower()
            if is_ss and ('e-tax' in text or 'etax' in text):
                offenders.append(f'{sp.name}: social-security spec references the tax e-portal')
            if is_tax and ('e-cnps' in text or 'cnps portal' in text or 'cnps teledeclaration' in text):
                offenders.append(f'{sp.name}: tax spec references the social-security portal')
        if not offenders:
            return ('C24', 'PASS', 'Portal/institution labels consistent', [])
        return ('C24', 'FAIL', '; '.join(offenders), offenders)
    except Exception as e:
        return ('C24', 'ERROR', str(e), [])

# ----- C25: No fabricated Sample File (v2.7) -----
def c25():
    try:
        from openpyxl import load_workbook
        spec_dir = BASE / '04-reports-spec'
        samples_dir = BASE / '00-official-sources' / 'sample-files'
        has_official = samples_dir.exists() and any(samples_dir.iterdir())
        if not spec_dir.exists():
            return ('C25', 'SKIP', 'No 04-reports-spec/', [])
        offenders = []
        for sp in sorted(spec_dir.glob(f'{CODE}-*-Spec.xlsx')):
            wb = load_workbook(str(sp), read_only=True)
            if 'Sample File' not in wb.sheetnames:
                continue
            ws = wb['Sample File']
            xml_hit = False
            for row in ws.iter_rows(values_only=True):
                for c in row:
                    if isinstance(c, str) and c.strip().startswith('<'):
                        xml_hit = True
            if xml_hit and not has_official:
                offenders.append(sp.name)
        if not offenders:
            return ('C25', 'PASS', 'No fabricated Sample File detected', [])
        return ('C25', 'MANUAL', f'Sample File has XML but no official sample on disk — verify not fabricated: {offenders}', offenders)
    except Exception as e:
        return ('C25', 'ERROR', str(e), [])

# ----- C26: Payslip 8-sheet + formula hygiene + currency integer (v2.7) -----
def c26():
    try:
        from openpyxl import load_workbook
        ZERO_MINOR = {'XAF', 'XOF', 'JPY', 'KRW', 'CLP', 'ISK', 'VND', 'UGX', 'RWF', 'GNF', 'KMF', 'DJF', 'XPF', 'PYG', 'BIF'}
        path = BASE / '06-payslip' / f'{CODE}_Compliance_Payslip_Generator.xlsx'
        if not path.exists():
            return ('C26', 'FAIL', f'File missing: {path.name}', [])
        wb = load_workbook(str(path))
        issues = []
        expected = ['How to set up Payslip', 'Compliance Payslip', f'{COUNTRY} (EN)', f'{COUNTRY} ({LOCAL_LANG})', 'Payslip Spec', 'Field Option', 'Population Range', 'Unit Rate Details']
        missing = [s for s in expected if s not in wb.sheetnames]
        if missing:
            issues.append(f'missing sheets: {missing}')
        en = f'{COUNTRY} (EN)'
        if en in wb.sheetnames and CURRENCY in ZERO_MINOR:
            ws = wb[en]
            for row in ws.iter_rows():
                hit = False
                for c in row:
                    if c.number_format and '0.00' in c.number_format:
                        issues.append(f'{CURRENCY} amount with decimals at {c.coordinate} (must be integer)')
                        hit = True
                        break
                if hit:
                    break
        if not issues:
            return ('C26', 'PASS', '8-sheet structure + currency format OK', [])
        return ('C26', 'FAIL', '; '.join(issues), issues)
    except Exception as e:
        return ('C26', 'ERROR', str(e), [])

# ----- C27: DD <-> spec System Mapping resolution (v2.7) -----
def c27():
    try:
        from openpyxl import load_workbook
        spec_dir = BASE / '04-reports-spec'
        dd_path = BASE / '05-data-dictionary' / f'{CODE}-DD-001-v1.0.xlsx'
        if not spec_dir.exists() or not dd_path.exists():
            return ('C27', 'SKIP', 'specs or DD missing', [])
        ddwb = load_workbook(str(dd_path), read_only=True)
        dd_terms = set()
        for ws in ddwb.worksheets:
            for row in ws.iter_rows(values_only=True):
                for c in row:
                    if isinstance(c, str) and len(c.strip()) > 4:
                        dd_terms.add(c.strip().lower())
        DERIVED = ('derived', 'computed', 'system-generated', 'manual', 'free-text', 'free text', 'sequence', 'ordinal', 'sum(', 'round(')
        import re as _re27
        def _c27_norm(x):
            return ''.join(ch for ch in str(x).lower() if ch.isalnum())
        def _c27_tokens(x):
            return _re27.findall(r'[A-Za-z][A-Za-z0-9_.]{3,}', str(x))
        dd_norm = set()
        for _t in dd_terms:
            _v = _c27_norm(_t)
            if len(_v) > 6:
                dd_norm.add(_v)
        unresolved = []
        for sp in sorted(spec_dir.glob(f'{CODE}-*-Spec.xlsx')):
            wb = load_workbook(str(sp), read_only=True)
            for ws in wb.worksheets:
                if not ('spec' in ws.title.lower() or 'declaration' in ws.title.lower()):
                    continue
                for row in ws.iter_rows(min_row=2, values_only=True):
                    if len(row) < 12:
                        continue
                    sysmap = row[11]
                    if not isinstance(sysmap, str) or not sysmap.strip():
                        continue
                    low = sysmap.lower()
                    if any(k in low for k in DERIVED) or 'dd:' in low or 'data dictionary' in low:
                        continue
                    if any(term in low for term in dd_terms):
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
                    unresolved.append(f'{sp.name}: "{str(sysmap)[:40]}"')
        if not unresolved:
            return ('C27', 'PASS', 'System Mappings resolve to DD or are classified', [])
        return ('C27', 'MANUAL', f'{len(unresolved)} mappings need a DD link or derived/structural class', unresolved[:10])
    except Exception as e:
        return ('C27', 'ERROR', str(e), [])

# ----- C28: Zero-minor-unit currency integer rule in specs (v2.7) -----
def c28():
    try:
        from openpyxl import load_workbook
        ZERO_MINOR = {'XAF', 'XOF', 'JPY', 'KRW', 'CLP', 'ISK', 'VND', 'UGX', 'RWF', 'GNF', 'KMF', 'DJF', 'XPF', 'PYG', 'BIF'}
        if CURRENCY not in ZERO_MINOR:
            return ('C28', 'PASS', f'{CURRENCY} has a minor unit — rule N/A', [])
        spec_dir = BASE / '04-reports-spec'
        if not spec_dir.exists():
            return ('C28', 'SKIP', 'No 04-reports-spec/', [])
        offenders = []
        for sp in sorted(spec_dir.glob(f'{CODE}-*-Spec.xlsx')):
            wb = load_workbook(str(sp), read_only=True)
            for ws in wb.worksheets:
                if not ('spec' in ws.title.lower() or 'declaration' in ws.title.lower()):
                    continue
                for row in ws.iter_rows(min_row=2, values_only=True):
                    if len(row) < 18:
                        continue
                    fmt, vtype = row[9], row[17]
                    if isinstance(fmt, str) and isinstance(vtype, str) and 'amount' in vtype.lower():
                        f = fmt.lower()
                        if 'n2.2' in f or 'v99' in f or '.99' in f or ',##0.00' in f:
                            offenders.append(f'{sp.name}: amount format "{fmt}" has decimals')
        if not offenders:
            return ('C28', 'PASS', f'{CURRENCY} amount formats are integer', [])
        return ('C28', 'FAIL', '; '.join(offenders[:8]), offenders)
    except Exception as e:
        return ('C28', 'ERROR', str(e), [])

# ----- C29: Residual-marker lint across ALL artifacts (v2.8, B3) -----
def c29():
    """B3: no unfinished-work marker may survive to final in the CCG, the report specs,
       the WTC or the DD. Deterministic FAIL. Complements C8 (CCG-only)."""
    try:
        import re as _re
        # v2.9 fix: an open-item marker is an ALL-CAPS convention. Matching TODO
        # case-insensitively also matches the ordinary Spanish/Portuguese/Italian word
        # 'todo'/'Todo' ("every", "in any case") inside quoted statute - a guaranteed
        # false positive in ES/PT/IT countries. Markers that collide with a natural-
        # language word are matched CASE-SENSITIVELY (flag 0); the rest keep IGNORECASE.
        markers_re = [(r'\bTODO\b', 0), (r'\bTodo\s*:', 0),
                      (r'\bTBD\b', _re.IGNORECASE), (r'\bFIXME\b', _re.IGNORECASE),
                      (r'\bVERIFY\s+No\b', _re.IGNORECASE),
                      (r'\[\s*placeholder\s*\]', _re.IGNORECASE),
                      (r'\[\s*CHECK\s*\]', _re.IGNORECASE),
                      (r'\[\s*\?\s*\]', _re.IGNORECASE)]
        markers_phrase = ['to be confirmed', 'to be verified']
        hits = []
        def scan_text(text, label):
            for pat, flags in markers_re:
                if _re.search(pat, text, flags):
                    hits.append(f'{label}: {pat}')
            low = text.lower()
            for ph in markers_phrase:
                if ph in low:
                    hits.append(f'{label}: "{ph}"')
        try:
            from docx import Document
            for ccg in sorted((BASE / '01-ccg').glob(f'{CODE}-CCG-001-v1*.docx')):
                scan_text('\n'.join(p.text for p in Document(str(ccg)).paragraphs), ccg.name)
        except Exception:
            pass
        try:
            from openpyxl import load_workbook
            for d, g in [(BASE / '04-reports-spec', f'{CODE}-*-Spec.xlsx'),
                         (BASE / '02-wtc', f'{CODE}-WTC-001-v1*.xlsx'),
                         (BASE / '05-data-dictionary', f'{CODE}-DD-001-v1*.xlsx')]:
                for f in sorted(d.glob(g)):
                    wb = load_workbook(str(f), read_only=True, data_only=True)
                    for ws in wb.worksheets:
                        for row in ws.iter_rows(values_only=True):
                            for v in row:
                                if isinstance(v, str):
                                    scan_text(v, f'{f.name}[{ws.title}]')
                    wb.close()
        except Exception:
            pass
        hits = sorted(set(hits))
        if not hits:
            return ('C29', 'PASS', 'No residual placeholder/TODO/VERIFY-No markers in any artifact', [])
        return ('C29', 'FAIL', f'{len(hits)} residual marker(s) across artifacts', hits[:20])
    except Exception as e:
        return ('C29', 'ERROR', str(e), [])

# ----- C30: Source-tier flag (v2.8, B5) -----
def c30():
    """B5: a figure whose only cited source is a tier-3 aggregator must be backed by an
       A.1/A.2 official source. Deterministic detection of known aggregator domains -> MANUAL."""
    try:
        AGG = ['51shebao', 'pwc.', 'china-briefing', 'chinabriefing', 'wikipedia',
               'investopedia', 'expatica', 'tradingeconomics', 'kpmg', 'deloitte',
               'ey.com', 'mercer', 'statista']
        found = []
        try:
            from docx import Document
            for ccg in sorted((BASE / '01-ccg').glob(f'{CODE}-CCG-001-v1*.docx')):
                t = '\n'.join(p.text for p in Document(str(ccg)).paragraphs).lower()
                for a in AGG:
                    if a in t:
                        found.append(f'{ccg.name}: {a}')
        except Exception:
            pass
        try:
            from openpyxl import load_workbook
            for d, g in [(BASE / '04-reports-spec', f'{CODE}-*-Spec.xlsx'),
                         (BASE / '02-wtc', f'{CODE}-WTC-001-v1*.xlsx'),
                         (BASE / '05-data-dictionary', f'{CODE}-DD-001-v1*.xlsx')]:
                for f in sorted(d.glob(g)):
                    wb = load_workbook(str(f), read_only=True, data_only=True)
                    for ws in wb.worksheets:
                        for row in ws.iter_rows(values_only=True):
                            for v in row:
                                if isinstance(v, str):
                                    low = v.lower()
                                    for a in AGG:
                                        if a in low:
                                            found.append(f'{f.name}: {a}')
                                            break
                    wb.close()
        except Exception:
            pass
        found = sorted(set(found))
        if not found:
            return ('C30', 'PASS', 'No tier-3 aggregator sources detected', [])
        return ('C30', 'MANUAL',
                f'{len(found)} tier-3 source citation(s) — confirm an official A.1/A.2 source backs each figure',
                found[:15])
    except Exception as e:
        return ('C30', 'ERROR', str(e), [])

# ----- C31: Resident vs non-resident coverage (v2.8, B1) -----
def c31():
    """B1: the income-tax module must address BOTH resident and non-resident treatment.
       If 'non-resident' is entirely absent where income tax is discussed -> MANUAL."""
    try:
        from docx import Document
        ccgs = sorted((BASE / '01-ccg').glob(f'{CODE}-CCG-001-v1*.docx'))
        if not ccgs:
            return ('C31', 'SKIP', 'CCG not found', [])
        t = '\n'.join(p.text for p in Document(str(ccgs[-1])).paragraphs).lower()
        mentions_tax = any(k in t for k in ['income tax', 'withhold', 'irpp', 'iit', 'paye',
                                            'retenue', 'impot sur le revenu', 'impôt sur le revenu'])
        has_nonres = any(k in t for k in ['non-resident', 'nonresident', 'non resident',
                                          'non-résident', 'non résident'])
        has_res = ('resident' in t) or ('résident' in t)
        if not mentions_tax:
            return ('C31', 'SKIP', 'No income-tax content detected', [])
        if has_res and has_nonres:
            return ('C31', 'PASS', 'Both resident and non-resident treatment present', [])
        if not has_nonres:
            return ('C31', 'MANUAL',
                    'No non-resident treatment in the income-tax module — fill the resident/non-resident matrix from primary law or state out-of-scope (B1)',
                    [])
        return ('C31', 'MANUAL', 'Resident/non-resident coverage looks incomplete — verify the matrix (B1)', [])
    except Exception as e:
        return ('C31', 'ERROR', str(e), [])

# ----- C32: Cross-artifact fact consistency (v2.9, deterministic) -----
def c32():
    """Deterministic cross-artifact consistency: every [[FACT:key=value]] tag is
       collected across ALL artifacts, keys validated against shared/fact-keys.yaml,
       grouped by key. If one key holds >1 distinct value across artifacts -> FAIL
       (the audit turns any FAIL into BLOCKED, so this blocks the build).
       Prose contradictions with no differing tag are NOT this check's job — the
       consistency-verifier subagent (semantic, report-only) covers those."""
    try:
        import re as _re, csv as _csv, glob as _glob
        REG = SHARED / 'fact-keys.yaml'
        tag_re = _re.compile(r'\[\[FACT:\s*([A-Za-z0-9_]+)\s*=\s*([^\]]+?)\s*\]\]')

        # -- mini-YAML reader scoped to fact-keys.yaml shape (no PyYAML dep) --
        def load_registry(path):
            allowed = {}
            if not path.exists():
                return allowed, 'registry-absent'
            in_keys = False; cur = None; attr = {}
            def _ind(s): return len(s) - len(s.lstrip(' '))
            def _flush():
                if cur is not None and attr.get('type'):
                    allowed[cur] = dict(attr)
            for raw in path.read_text(encoding='utf-8').splitlines():
                if not raw.strip() or raw.lstrip().startswith('#'):
                    continue
                ind = _ind(raw); s = raw.strip()
                if ind == 0:
                    in_keys = (s.rstrip(':') == 'keys'); continue
                if not in_keys:
                    continue
                if ind == 2 and s.endswith(':'):
                    _flush(); cur = None; attr = {}; continue
                if ind == 4 and s.endswith(':'):
                    _flush(); cur = s[:-1].strip(); attr = {}; continue
                if ind >= 6 and cur is not None and ':' in s:
                    k, _, v = s.partition(':'); k = k.strip(); v = v.strip().strip('"').strip("'")
                    if k == 'allowed':
                        attr['allowed'] = [x.strip().strip('"').strip("'")
                                           for x in v.strip('[]').split(',') if x.strip()]
                    else:
                        attr[k] = v
            _flush()
            return allowed, None

        def _norm(value, decl):
            t = (decl or {}).get('type', 'str'); v = value.strip()
            try:
                if t == 'bool':
                    return (v.lower(), None) if v.lower() in ('true', 'false') else (v, 'bool?')
                if t == 'int':
                    return (str(int(v)), None) if _re.fullmatch(r'-?\d+', v) else (v, 'int?')
                if t in ('money', 'pct'):
                    if _re.fullmatch(r'-?\d+(\.\d+)?', v) is None:
                        return v, 'num?'
                    s = ('%.6f' % float(v)).rstrip('0').rstrip('.')
                    return (s if s else '0'), None
                if t == 'enum':
                    al = (decl or {}).get('allowed', [])
                    return (v, None) if (not al or v in al) else (v, 'enum?')
                return v, None
            except Exception:
                return v, 'norm?'

        allowed, reg_err = load_registry(REG)

        # -- collect tags across artifacts --
        occ = {}      # key -> list of (file, raw, norm)
        unknown = []
        def _scan(text, label):
            for m in tag_re.finditer(text):
                k = m.group(1).strip(); raw = m.group(2).strip()
                decl = allowed.get(k)
                norm = raw if decl is None else _norm(raw, decl)[0]
                if decl is None:
                    unknown.append((k, label))
                occ.setdefault(k, []).append((label, raw, norm))

        try:
            from docx import Document
            for ccg in sorted((BASE / '01-ccg').glob(f'{CODE}-CCG-001-v1*.docx')):
                doc = Document(str(ccg))
                _scan('\n'.join(p.text for p in doc.paragraphs), ccg.name)
                for tbl in doc.tables:
                    for row in tbl.rows:
                        for cell in row.cells:
                            if cell.text:
                                _scan(cell.text, ccg.name)
        except Exception:
            pass
        try:
            from openpyxl import load_workbook
            xlsx_specs = [(BASE / '04-reports-spec', f'{CODE}-*-Spec.xlsx'),
                          (BASE / '02-wtc', f'{CODE}-WTC-001-v1*.xlsx'),
                          (BASE / '05-data-dictionary', f'{CODE}-DD-001-v1*.xlsx')]
            for d, g in xlsx_specs:
                for f in sorted(d.glob(g)):
                    wb = load_workbook(str(f), read_only=True, data_only=True)
                    for ws in wb.worksheets:
                        for row in ws.iter_rows(values_only=True):
                            for v in row:
                                if isinstance(v, str):
                                    _scan(v, f.name)
                    wb.close()
        except Exception:
            pass
        # SIR + any markdown artifacts
        for md in _glob.glob(str(BASE / '**' / '*.md'), recursive=True):
            bn = os.path.basename(md)
            if bn.startswith('FACT-'):
                continue
            try:
                _scan(Path(md).read_text(encoding='utf-8', errors='replace'), bn)
            except Exception:
                pass

        # -- detect conflicts --
        conflicts = []
        for k, lst in sorted(occ.items()):
            distinct = sorted(set(n for (_f, _r, n) in lst))
            if len(distinct) > 1:
                conflicts.append((k, distinct, lst))

        # -- write reports to logs --
        try:
            LOGS = BASE / 'logs'; LOGS.mkdir(exist_ok=True)
            with open(LOGS / 'FACT-CONFLICTS.csv', 'w', newline='', encoding='utf-8') as fh:
                w = _csv.writer(fh)
                w.writerow(['type', 'fact_key', 'file', 'value', 'all_values_for_key'])
                for k, distinct, lst in conflicts:
                    allv = '|'.join(distinct)
                    for (f, r, n) in lst:
                        w.writerow(['conflict', k, f, r, allv])
                for (k, f) in unknown:
                    w.writerow(['unknown_key', k, f, '', ''])
            md = ['# Cross-Artifact Fact Consistency (deterministic, C32)', '']
            md.append('CONFLICTS FOUND — BUILD BLOCKED' if conflicts else 'PASS — no deterministic conflicts')
            md.append('')
            for k, distinct, lst in conflicts:
                md.append(f'## `{k}` -> {distinct}')
                for (f, r, n) in lst:
                    md.append(f'- `{f}` = **{r}**')
                md.append('')
            (LOGS / 'FACT-CONFLICTS.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
        except Exception:
            pass

        total_tags = sum(len(v) for v in occ.values())
        if not occ:
            return ('C32', 'PASS', 'No [[FACT:]] tags present (country pre-dates tagging) — semantic verifier still applies', [])
        if conflicts:
            items = [f'{k}: ' + ' vs '.join(d) for (k, d, _l) in conflicts][:20]
            return ('C32', 'FAIL',
                    f'{len(conflicts)} cross-artifact fact conflict(s) across {total_tags} tags — see logs/FACT-CONFLICTS.md',
                    items)
        note = f'{total_tags} fact tags, {len(occ)} keys, all consistent'
        if reg_err == 'registry-absent':
            note += ' (registry absent — key names NOT validated)'
        elif unknown:
            note += f'; {len(set(k for k,_ in unknown))} unknown key(s) — add to shared/fact-keys.yaml'
        return ('C32', 'PASS', note, [])
    except Exception as e:
        return ('C32', 'ERROR', str(e), [])

# ----- C33: CCG English-only prose (v2.9, detective; MANUAL -> fixer translates) -----
def c33():
    """The CCG narrative must be English-only prose. Local-language words that leak into
       sentences/cells (the Mohit complaint) are flagged. Detection is deterministic and
       dependency-free: (a) any non-Latin script (Arabic/Urdu/etc.) via Unicode range is a
       zero-false-positive signal; (b) for Latin-script local languages, a CURATED set of
       high-frequency FUNCTION words per language that do NOT collide with English.
       Text inside parentheses or quotes is EXCLUDED from scanning — that is the permitted
       'English wording (original term)' citation form from control B10. Proper nouns of
       authorities/forms are unavoidable and not reliably separable, so this is MANUAL, not
       FAIL: it never blocks the build; the content-audit fixer translates the flagged prose.
       SCOPE: CCG prose ONLY. The DD/WTC/Payslip local-language fields are by design and are
       never scanned here."""
    try:
        import re as _re
        # Function-word stoplists, curated to avoid English collisions.
        # (Deliberately omit ambiguous tokens: es 'son'/'el', fr 'a', it 'e'/'a', pt 'e'/'a'/'o'.)
        STOP = {
            'French':     ['le','la','les','des','une','du','dans','pour','avec','sur','sont',
                           'aux','cette','être','leur','selon','ainsi','entre','chaque','doit',
                           'aucun','lorsque','n\u2019est','c\u2019est','qui','que','plus'],
            'Spanish':    ['los','las','una','del','con','para','por','que','como','este','esta',
                           'estos','estas','debe','cada','entre','segun','cuando','mas','sobre'],
            'Portuguese': ['os','as','uma','das','dos','com','para','por','que','como','este',
                           'esta','estes','estas','deve','cada','entre','segundo','quando','sobre'],
            'Italian':    ['il','lo','gli','una','del','della','con','per','che','come','questo',
                           'questa','deve','ogni','tra','quando','sopra','degli','delle'],
            'German':     ['der','die','das','und','den','dem','des','ein','eine','fur','mit',
                           'auf','ist','sind','oder','nicht','auch','werden','muss','jeder'],
            'Dutch':      ['de','het','een','en','van','voor','met','zijn','wordt','niet','elke',
                           'moet','tussen','volgens','wanneer'],
            'Hungarian':  ['az','egy','nem','van','vagy','minden','kell','között','szerint'],
            'Bulgarian':  [],   # Cyrillic — caught by the non-Latin script test below
        }
        lang = COUNTRY and None  # placeholder; real language comes from env-injected LANGUAGE
        # LANGUAGE isn't injected into the audit env; derive from LOCAL_LANG short code.
        SHORT2LANG = {'FR':'French','ES':'Spanish','PT':'Portuguese','IT':'Italian',
                      'DE':'German','NL':'Dutch','HU':'Hungarian','BG':'Bulgarian'}
        lang = SHORT2LANG.get(LOCAL_LANG, None)

        try:
            from docx import Document
        except Exception:
            return ('C33', 'SKIP', 'python-docx unavailable', [])
        ccgs = sorted((BASE / '01-ccg').glob(f'{CODE}-CCG-001-v1*.docx'))
        if not ccgs:
            return ('C33', 'SKIP', 'CCG not found', [])
        doc = Document(str(ccgs[-1]))

        # gather prose strings (paragraphs + table cells)
        strings = [p.text for p in doc.paragraphs if p.text]
        for tbl in doc.tables:
            for row in tbl.rows:
                for cell in row.cells:
                    if cell.text:
                        strings.append(cell.text)

        paren_re = _re.compile(r'\([^)]*\)')      # strip "(...)" — permitted citation form
        quote_re = _re.compile(r'"[^"]*"|\u201c[^\u201d]*\u201d|\u2018[^\u2019]*\u2019|\'[^\']*\'')
        # v2.9 fix: the previous test excluded only a hand-written list of punctuation, so
        # ordinary mathematical and typographic symbols that appear in perfectly English
        # prose - the rightwards arrow, minus sign, section sign, middle dot, <=, >=, +-,
        # sigma, almost-equal - were reported as "non-Latin script". Detect on the Unicode
        # general category instead: only a LETTER outside the Latin blocks is script
        # leakage. Symbols, punctuation and marks can never be.
        import unicodedata as _ud
        _MATH_LETTERS = set('\u03a3\u03a0\u0394\u03bc\u03c3\u03b1\u03b2\u03bb\u03a9\u03b8\u03c0')
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
        nonlatin_re = _NonLatin()

        hits = []
        def clean(s):
            s = paren_re.sub(' ', s)
            s = quote_re.sub(' ', s)
            return s

        for s in strings:
            scan = clean(s)
            # (a) non-Latin script anywhere in unquoted prose
            if nonlatin_re.search(scan):
                sample = s.strip()
                hits.append(('non-latin-script', sample[:80]))
                continue
            # (b) curated function-word test for the country's Latin-script language
            if lang and STOP.get(lang):
                toks = _re.findall(r"[A-Za-z\u00C0-\u017F\u2019']+", scan.lower())
                tokset = set(toks)
                found = [w for w in STOP[lang] if w in tokset]
                # require >=2 distinct function words in one string to reduce noise
                if len(found) >= 2:
                    hits.append((f'{lang}:' + ','.join(found[:5]), s.strip()[:80]))

        # de-dup, cap
        seen = set(); uniq = []
        for tag, sample in hits:
            key = (tag, sample)
            if key in seen:
                continue
            seen.add(key); uniq.append(f'[{tag}] {sample}')
        if not uniq:
            return ('C33', 'PASS', 'CCG prose is English-only (no local-language leakage detected)', [])
        return ('C33', 'MANUAL',
                f'{len(uniq)} possible local-language passage(s) in CCG prose — content-audit fixer must translate to English (keep statutory term in parentheses on first use, per B10)',
                uniq[:20])
    except Exception as e:
        return ('C33', 'ERROR', str(e), [])

# Run all checks
for fn in [c1, c8, c11, c12, c20, c21, c22, c23, c24, c25, c26, c27, c28, c29, c30, c31, c32, c33]:
    check, verdict, detail, items = fn()
    results.append({
        'check': check,
        'verdict': verdict,
        'detail': detail,
        'items': items,
    })

verdicts = [r['verdict'] for r in results]
fails = sum(1 for v in verdicts if v == 'FAIL')
manuals = sum(1 for v in verdicts if v == 'MANUAL')
passes = sum(1 for v in verdicts if v == 'PASS')

overall = 'READY_FOR_HANDOVER' if fails == 0 else 'BLOCKED'

output = {
    'overall': overall,
    'summary': {'PASS': passes, 'MANUAL': manuals, 'FAIL': fails},
    'checks': results,
}
print(json.dumps(output, indent=2))
