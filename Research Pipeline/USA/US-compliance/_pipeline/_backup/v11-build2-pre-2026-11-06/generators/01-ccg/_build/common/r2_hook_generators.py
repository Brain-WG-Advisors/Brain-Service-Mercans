# -*- coding: utf-8 -*-
"""Round-2 (QA r1) one-off hook of the four annex generators into ccg_common (finalize + one
annex skeleton + [[GAPKEY:]] markers). Idempotent: a pair already applied is skipped.
usage: python r2_hook_generators.py <BASE>"""
import os
import sys

BASE = sys.argv[1]
MARK = "⚠️ RESEARCH-GAP"


def patch(rel, pairs):
    p = os.path.join(BASE, rel)
    raw = open(p, encoding="utf-8", newline="").read()
    crlf = raw.count("\r\n") > raw.count("\n") / 2
    t = raw.replace("\r\n", "\n")
    n = 0
    for a, b in pairs:
        if b in t:
            continue
        if a in t:
            if t.count(a) != 1:
                raise SystemExit(f"{rel}: {t.count(a)} occurrences of {a[:80]!r}")
            t = t.replace(a, b)
            n += 1
        elif b not in t:
            raise SystemExit(f"{rel}: neither old nor new text found: {a[:100]!r}")
    if crlf:
        t = t.replace("\n", "\r\n")
    open(p, "w", encoding="utf-8", newline="").write(t)
    print(rel, "applied", n, "of", len(pairs))


IMPORT = ('sys.path.insert(0, os.path.join(BASE, "01-ccg", "_build", "common"))\n'
          'import ccg_common as CC  # noqa: E402  round 2 (QA r1): finalize, annex skeleton, [[GAP:]] tags\n')

# ---------------------------------------------------------------- FED-CT
patch("01-ccg/_scratch/annex-FED-CT/build_annexes.py", [
    ('OUT = os.path.join(BASE, "01-ccg", "annexes")\n',
     'OUT = os.path.join(BASE, "01-ccg", "annexes")\n' + IMPORT),
    ('parts.append(f"' + MARK + ' ({blk}): not established. Would close it: {cl}")',
     'parts.append(f"' + MARK + ' [[GAPKEY:{it[\'key\']}]] ({blk}): not established. Would close it: {cl}")'),
    ('    return f"' + MARK + ' ({blk}): {topic}. Source that would close it: {close}"',
     '    return f"' + MARK + ' [[GAPKEY:{g[\'key\']}]] ({blk}): {topic}. Source that would close it: {close}"'),
    ('        path = os.path.join(OUT, f"annex_{u}.md")\n        open(path, "w", encoding="utf-8", newline="\\n").write(text)',
     '        path = os.path.join(OUT, f"annex_{u}.md")\n'
     '        text = CC.finalize(f"annex_{u}.md", CC.normalize_annex(f"annex_{u}.md", text, CC.MAP_FED_CT))\n'
     '        open(path, "w", encoding="utf-8", newline="\\n").write(text)'),
])

# ---------------------------------------------------------------- DC-MA
patch("01-ccg/_scratch/annex-DC-MA/build_annexes.py", [
    ('OUT = os.path.join(BASE, "01-ccg", "annexes")  # was 01-ccg/modules; moved at CCG assembly 2026-11-02\n',
     'OUT = os.path.join(BASE, "01-ccg", "annexes")  # was 01-ccg/modules; moved at CCG assembly 2026-11-02\n' + IMPORT),
    ('    open(os.path.join(OUT, f"annex_{jur}.md"), "w", encoding="utf-8").write(text)',
     '    text = CC.finalize(f"annex_{jur}.md", CC.normalize_annex(f"annex_{jur}.md", text, CC.MAP_FED_CT))\n'
     '    open(os.path.join(OUT, f"annex_{jur}.md"), "w", encoding="utf-8").write(text)'),
])

# ---------------------------------------------------------------- MD-NV
patch("_research/synthesis-B/_scratch-ccg-build-MD-NV/build_annexes.py", [
    ('OUTDIR = os.path.join(BASE, "01-ccg", "annexes")\n',
     'OUTDIR = os.path.join(BASE, "01-ccg", "annexes")\n' + IMPORT),
    ('"reciprocity mechanics) are in Annex MULTI. Neither is repeated here. Independent contractors and "\n'
     '             "Form 1099-NEC are out of scope. The pay statement is issued in English.")',
     '"reciprocity mechanics) are in Annex MULTI. Neither is repeated here. " + CC.CONTRACTOR_SENTENCE + '
     '" The pay statement is issued in English.")'),
    ('    text = "\\n".join(L)\n    open(os.path.join(OUTDIR, f"annex_{jur}.md"), "w", encoding="utf-8", newline="\\n").write(text)',
     '    text = "\\n".join(L)\n'
     '    text = CC.finalize(f"annex_{jur}.md", CC.normalize_annex(f"annex_{jur}.md", text, CC.MAP_MD_NV, renumber_refs=True))\n'
     '    open(os.path.join(OUTDIR, f"annex_{jur}.md"), "w", encoding="utf-8", newline="\\n").write(text)'),
])

# ---------------------------------------------------------------- NY-WY
patch("01-ccg/_build-annex-NY-WY/build.py", [
    ('OUT = os.path.join(BASE, "01-ccg", "annexes")\n',
     'OUT = os.path.join(BASE, "01-ccg", "annexes")\n'
     'sys.path.insert(0, os.path.join(BASE, "01-ccg", "_build", "common"))\n'
     'import ccg_common as CC  # noqa: E402  round 2 (QA r1): finalize, annex skeleton, [[GAP:]] tags\n'),
    ('"Independent contractors and Form 1099-NEC are out of scope (MANDATE, US-OWN-008). Payslip language: English; "',
     'CC.CONTRACTOR_SENTENCE + " Payslip language: English; "'),
    ('    L.append("Every value in this annex is bound to a key of `_research/CCG-annex_" + st + "-facts.json` and carries its "\n'
     '             "legal-basis register id. A value that changes during the year is shown with its effective dates. "\n'
     '             "`RESEARCH-GAP` marks a point the research has not closed; it is not filled with an estimate.")',
     '    L.append("Every value in this annex is bound to a verified fact and carries its "\n'
     '             "legal-basis register id. A value that changes during the year is shown with its effective dates. "\n'
     '             "A point marked as a research gap has not been closed by the research; it is not filled with an estimate.")'),
    ('            open(os.path.join(OUT, f"annex_{st}.md"), "w", encoding="utf-8", newline="\\n").write(txt)',
     '            txt = CC.finalize(f"annex_{st}.md", CC.normalize_annex(f"annex_{st}.md", txt, CC.MAP_NY_WY))\n'
     '            open(os.path.join(OUT, f"annex_{st}.md"), "w", encoding="utf-8", newline="\\n").write(txt)'),
])
