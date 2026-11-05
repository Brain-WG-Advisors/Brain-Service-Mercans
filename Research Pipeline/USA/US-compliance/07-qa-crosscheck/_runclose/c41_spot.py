import csv, re, collections, random, sys, os
sys.stdout.reconfigure(encoding="utf-8")
rows = list(csv.DictReader(open("00-official-sources/legal-basis-register.csv", encoding="utf-8")))
old = {r["id"]: r for r in csv.DictReader(open(sys.argv[1], encoding="utf-8"))}
c = collections.Counter(); pool = []
for r in rows:
    m = re.search(r"effective_from_basis:\s*([a-z_]+)", r["verification_method"])
    if m:
        c[m.group(1)] += 1
        o = old.get(r["id"], {})
        if not (o.get("effective_from") or "").strip():
            pool.append((m.group(1), r))
print(c.most_common()); print("newly dated", len(pool))
random.seed(41)
ret = [p for p in pool if p[0].startswith("retriev")]
print("retrieval-basis newly dated", len(ret))
for b, r in random.sample(ret, min(20, len(ret))):
    print(r["id"], "|", r["instrument_type"], "|", r["instrument_name"][:60], "| ef", r["effective_from"], "| pub", r["publication_date"], "| ret", r["retrieved_on"], "| st", r["status"])
