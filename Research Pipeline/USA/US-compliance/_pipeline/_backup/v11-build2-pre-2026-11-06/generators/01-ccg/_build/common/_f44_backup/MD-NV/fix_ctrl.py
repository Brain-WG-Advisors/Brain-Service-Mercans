import os
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "build_annexes.py")
lines = open(p, encoding="utf-8").read().split("\n")
out = []
skip = False
for l in lines:
    if l.startswith("SANITIZE = ["):
        skip = True
        out.append(r'''SANITIZE = [
    (r"\s*\blegacy\b(?= ?row)", ""), (r"(US-[A-Z0-9]+-\d{3}) legacy", r"\1"), (r"\blegacy\s+", ""),
    (r"\s*reproduced in Python", " reproduced"), (r"\s*\(Python\)", ""), (r"\(stage-5 derivation\)", "(derived)"),
    (r"\s*\(stage-5 finding\)", ""), (r"\s+in stage 5\b", ""), (r"G-DERIVE:\s*", "Derived: "),
    (r"annex_([A-Z]{2,5})", r"Annex \1"), (r"TRAP:\s*", "Caution: "), (r"\btier-B\b", "secondary"),
    (r"\s*\(Q\d+\)", ""), (r"\s*\([A-Z]{2}-OQ-\d+\)", ""), (r"WebFetch summary", "summary"),
    (r"webfetch quote \(summarizer\)", "summary quote"),
    (r"Synthesis C: rebound from", "also cited:"), (r"register row verification is weak:\s*", "source check: "),
    (r"register row is PARTIAL - carry the partial flag", "source graded partial"), (r"\s+this round", ""),
    (r"no verified register row carries it", "no verified source carries it"),
    (r"\s+\.", "."),
]''')
        continue
    if skip:
        if l.strip() == "]":
            skip = False
        continue
    l = l.replace('r"\x01"', 'r"\\1"')
    out.append(l)
s = "\n".join(out)
assert not any(ord(c) < 32 and c != "\n" for c in s), "control chars remain"
open(p, "w", encoding="utf-8").write(s)
print("ok")
