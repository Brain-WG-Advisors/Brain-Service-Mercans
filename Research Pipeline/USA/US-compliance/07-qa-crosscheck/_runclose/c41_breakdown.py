import csv, datetime as dt, collections, os, sys
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
today = dt.date(2026, 11, 4)
def d(s):
    try: return dt.date.fromisoformat(str(s)[:10])
    except Exception: return None
c = collections.Counter(); by_status = collections.Counter(); n = 0
for r in csv.DictReader(open(os.path.join(BASE, "00-official-sources", "legal-basis-register.csv"), encoding="utf-8")):
    by_status[r.get("status")] += 1
    ef, et, vo = d(r.get("effective_from")), d(r.get("effective_to")), d(r.get("verified_on"))
    why = []
    if not ef: why.append("no effective_from")
    if et and et < today: why.append("effective_to past")
    if not vo: why.append("no verified_on")
    elif (today - vo).days > 120: why.append("verified_on > 120 days")
    if why and r.get("status","").lower() not in ("superseded","withdrawn","rejected"): c["; ".join(why)] += 1; n += 1
print("register rows", sum(by_status.values()), dict(by_status)); print("rows flagged (all statuses)", n); print(c.most_common())
