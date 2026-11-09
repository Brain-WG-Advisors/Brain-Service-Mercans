"""Re-point fact keys in the CCG generator inputs through KEY-ALIAS-MAP.csv (QA r1 fix 1).

Round 2 rebuild, artifact-builder. Re-runnable: a second run finds nothing to change.
Scans the generator sources only (never the generated .md units):
  01-ccg/_build-m01-m07, 01-ccg/_build/m08_m13, 01-ccg/_scratch/annex-FED-CT,
  01-ccg/_scratch/annex-DC-MA, _research/synthesis-B/_scratch-ccg-build-MD-NV,
  01-ccg/_build-annex-NY-WY (build.py + src/*.md + json), 01-ccg/_examples.
Rows whose canonical_key is not a single key (holiday fan-out, equity split) are
handled by hand in the generators and are skipped here.

usage: python -I repoint_aliases.py <BASE> [--dry]
"""
import csv, os, re, sys, json

BASE = sys.argv[1]
DRY = '--dry' in sys.argv
DIRS = ['01-ccg/_build-m01-m07', '01-ccg/_build/m08_m13', '01-ccg/_scratch/annex-FED-CT',
        '01-ccg/_scratch/annex-DC-MA', '_research/synthesis-B/_scratch-ccg-build-MD-NV',
        '01-ccg/_build-annex-NY-WY', '01-ccg/_examples', '01-ccg/_build/assemble']
EXT = ('.py', '.md', '.json')
SKIP_NAMES = {'bindings.json', 'build_result.json', 'request_ids.json', 'build-log-section.md',
              'buildlog_section.md', 'log_section.md', 'check_output.txt'}
KEYRE = re.compile(r'^[a-z0-9_]+(\.[a-z0-9_]+)+$')

rows = list(csv.DictReader(open(os.path.join(BASE, '_research/qa-r1-fix/KEY-ALIAS-MAP.csv'), encoding='utf-8')))
amap = {r['old_key']: r['canonical_key'] for r in rows if KEYRE.match(r['canonical_key'])}
skipped = [r['old_key'] for r in rows if not KEYRE.match(r['canonical_key'])]
# longest first so a key that is a prefix of another is never replaced inside it
olds = sorted(amap, key=len, reverse=True)
pat = re.compile(r'(?<![A-Za-z0-9_.])(' + '|'.join(re.escape(o) for o in olds) + r')(?![A-Za-z0-9_]|\.[A-Za-z0-9_])')

report = {}
for d in DIRS:
    root = os.path.join(BASE, d)
    for dp, dn, fn in os.walk(root):
        dn[:] = [x for x in dn if x not in ('__pycache__', 'out', '_backup')]
        for f in fn:
            if not f.endswith(EXT) or f in SKIP_NAMES:
                continue
            p = os.path.join(dp, f)
            t = open(p, encoding='utf-8', newline='').read()
            hits = pat.findall(t)
            if not hits:
                continue
            nt = pat.sub(lambda m: amap[m.group(1)], t)
            report[os.path.relpath(p, BASE).replace('\\', '/')] = len(hits)
            if not DRY:
                open(p, 'w', encoding='utf-8', newline='').write(nt)
print(json.dumps({'files': report, 'total': sum(report.values()), 'skipped_non_key_rows': skipped}, indent=1))
