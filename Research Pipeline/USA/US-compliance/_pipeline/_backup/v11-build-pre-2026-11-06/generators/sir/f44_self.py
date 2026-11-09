# -*- coding: utf-8 -*-
"""F44 self-check of the SIR index: for every [[FACT:key=value]] tag of the document, every text element of the value
(numbers, form names, dates, quarter tokens, channel words, acronyms) must appear in the local copy of a bound register
row (register_id + _also_register_ids). Misses must be 0: a miss is a research request plus the neutral gap cell.
Uses the saved copies through f44_lib (text cache rebuilt by f44_textcache.py).
usage: python f44_self.py [docx]   -> checks/f44_self.json"""
import json
import os
import re
import sys

import docx

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import sir_common as S  # noqa: E402
import f44_lib  # noqa: E402

TAG = re.compile(r"\[\[FACT:([A-Za-z0-9_.]+)=([^\]]*)\]\]")


def same(a, b):
    try:
        return abs(float(str(a).replace(",", "")) - float(str(b).replace(",", ""))) < 1e-9
    except ValueError:
        return str(a).strip() == str(b).strip()


def main():
    path = os.path.join(S.SIRDIR, S.FILENAME)
    args = [a for a in sys.argv[1:] if a.endswith(".docx")]
    if args:
        path = args[0]
    d = docx.Document(path)
    texts = [p.text for p in d.paragraphs]
    for t in d.tables:
        for r in t.rows:
            seen = set()
            for c in r.cells:
                if id(c._tc) not in seen:
                    seen.add(id(c._tc))
                    texts.append(c.text)
    seen_pairs, misses, checked, nocopy = set(), [], 0, []
    weak, partial = set(), set()
    for tx in texts:
        for m in TAG.finditer(tx):
            k, val = m.group(1), m.group(2)
            if (k, val) in seen_pairs:
                continue
            seen_pairs.add((k, val))
            facts = [f for f in S.C.FACTS.get(k, []) if same(val, f["value"])]
            if not facts:
                misses.append({"key": k, "value": val[:80], "why": "no fact with this value"})
                continue
            ok = False
            worst = None
            for f in facts:
                miss, has_copy = f44_lib.check_fact(f)
                if not has_copy:
                    nocopy.append(k)
                if not miss:
                    ok = True
                    break
                worst = (f, miss)
            checked += 1
            for f in facts:       # SIR-QA1-17: a cited row that is superseded / partial / MANUAL proves nothing
                for rid in S.rids(f):
                    st = f44_lib.reg_status(rid)
                    if st == "superseded" and k not in f44_lib.LIMITATION_KEYS:
                        weak.add((k, rid, st))
                    elif st in f44_lib.WEAK_STATUS:
                        partial.add((k, rid, st))
            if not ok:
                misses.append({"key": k, "value": val[:80], "register_ids": S.rids(worst[0]), "missing": worst[1]})
    for k, rid, st in sorted(weak):
        misses.append({"key": k, "register_ids": [rid], "why": f"cited register row {rid} has status {st}"})
    out = {"tags_checked": checked, "misses": misses, "no_local_copy": sorted(set(nocopy)), "partial_or_manual_rows_cited": sorted(partial),
           "checks": "2-letter State codes; acronym only as itself; _also rows superseded/partial/MANUAL ignored and flagged"}
    json.dump(out, open(os.path.join(S.CHECKS, "f44_self.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False, default=str)
    print(f"F44 self-check: {checked} distinct tags, {len(misses)} misses, {len(set(nocopy))} tags without a local copy")
    for m in misses[:20]:
        print("MISS", m)
    return 1 if misses or nocopy else 0


if __name__ == "__main__":
    sys.exit(main())
