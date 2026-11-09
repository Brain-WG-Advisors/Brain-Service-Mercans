import re
p = 'build_annexes.py'
s = open(p, encoding='utf-8').read()
s = s.replace('\b', '')  # strip stray backspace characters introduced by an earlier patch
lines = s.split('\n')
for i, ln in enumerate(lines):
    if ln.startswith('NOTE_DROP_SENT = re.compile('):
        lines[i] = ('NOTE_DROP_SENT = re.compile(r"(Stage[- ]?\\d|Synthesis|tier[- ]?[ABC]\\b|\\bMANUAL\\b|PENDING|not a fact|register|'
                    'facts? file|legacy id|"')
    if ln.strip().startswith('r"browser pass|Chrome pass|OQ-|fan-out|unit)"'):
        lines[i] = '                            r"browser pass|Chrome pass|\\bOQ-|fan-out|\\bunit\\b|\\bFED unit|\\bState unit)", re.I)'
s = '\n'.join(lines)
old = '                note = re.sub(r"\\bin Python\\b|\\bReproduced in Python[:.]?|\\bre-derived in Python\\b", "", note).strip()'
old2 = '                note = clean(note)\n'
assert old2 in s
s = s.replace(old2 + old, '                note = clean_note(note)')
if 'note = clean_note(note)' not in s:
    # fallback: find the two lines loosely
    s = re.sub(r'                note = clean\(note\)\n                note = re\.sub\([^\n]*\n', '                note = clean_note(note)\n', s)
anchor = '    text = "\\n".join(L).rstrip() + "\\n"\n'
assert anchor in s, 'anchor'
s = s.replace(anchor, anchor + '''    present = set(re.findall(r"\\[\\[FACT:([a-z0-9_.]+)=", text))
    missing = sorted({f["key"] for f in facts} - present)
    if missing:
        print(unit, "MISSING FACT KEYS:", missing)
    for g in unresolved:
        if g["key"] not in GAPLOC:
            print(unit, "GAP NOT PLACED:", g["key"])
''', 1)
open(p, 'w', encoding='utf-8').write(s)
print('ok', 'clean_note(note)' in s)
