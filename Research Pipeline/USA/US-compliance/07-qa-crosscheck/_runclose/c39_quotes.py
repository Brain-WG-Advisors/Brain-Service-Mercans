import json, re, os, sys
sys.stdout.reconfigure(encoding="utf-8")
S = "00-official-sources/ccg-sources/"
m = {"T42": "US-FED/SSA-cbb-2027.txt", "T43": "CO/CO-famli-employers.txt", "T44": "CA/CA-LC226.txt", "T45": "CA/CA-LC226.txt",
     "T47": "MA/MA-DFML-pfml.txt", "T48": "FL/FL-443-1217.txt", "T52": "MI/MI-446-withholding-guide-2026.txt",
     "T53": "CO/CO-DR0004-2026.txt", "T54": "US-FED/SSA-efw2.txt"}
A = {x["id"]: x for x in json.load(open("07-qa-crosscheck/US-TEST0.json", encoding="utf-8"))["assertions"]}
n = lambda s: re.sub(r"\s+", " ", s).strip().lower()
for i, f in m.items():
    t = n(open(S + f, encoding="utf-8", errors="ignore").read())
    q = A[i]["source"].get("quote", "")
    parts = [n(p) for p in re.split(r"\.\.\.|…", q) if p.strip()]
    ok = [p in t for p in parts]
    print(i, A[i]["source"].get("consulted_on"), f, "segments", sum(ok), "/", len(ok), "" if all(ok) else [p for p, k in zip(parts, ok) if not k])
for i in ("T46", "T49", "T50", "T51", "T55", "T56"):
    print(i, A[i]["result"], A[i]["assertion"][:50])
