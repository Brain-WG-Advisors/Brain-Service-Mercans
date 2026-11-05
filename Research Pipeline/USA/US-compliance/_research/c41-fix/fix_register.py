import csv, datetime as dt, sys, collections
P="00-official-sources/legal-basis-register.csv"
T=dt.date(2026,11,4)
def d(s):
    try: return dt.date.fromisoformat(str(s)[:10])
    except Exception: return None
fh=open(P,encoding="utf-8",newline=""); rd=csv.DictReader(fh); cols=rd.fieldnames; rows=list(rd); fh.close()
superseded_ids=set()
for r in rows:
    for tok in r["supersedes"].replace(";"," ").replace(","," ").split():
        superseded_ids.add(tok)
log=collections.Counter(); odd=[]
for r in rows:
    if r["status"].lower() in ("superseded","withdrawn","rejected"): continue
    ef,et,pub,ret,vo=d(r["effective_from"]),d(r["effective_to"]),d(r["publication_date"]),d(r["retrieved_on"]),d(r["verified_on"])
    notes=[]
    if r["id"]=="US-GAS5-018":
        r["status"]="rejected"; r["verification_method"]="never read: tier-B Justia lead only, no date; rejected as a source 2026-11-04 (C41 close); the GA SSN-display point needs an official-host read"; log["rejected"]+=1; continue
    if r["id"]=="US-RIS5-008":
        r["status"]="superseded"; r["verification_method"]+=" | status superseded 2026-11-04: the instrument's own index lists a second version effective 2026-01-01; start date of this version not stated, none invented"; log["ris"]+=1; continue
    if not ef:
        if pub and pub<=T and (not et or pub<=et): r["effective_from"]=str(pub); notes.append("effective_from_basis: publication_date"); log["ef_pub"]+=1
        elif ret and (not et or ret<=et): r["effective_from"]=str(ret); notes.append("effective_from_basis: retrieval (in force as at retrieved_on; not stated in the copy)"); log["ef_ret"]+=1
        else: odd.append((r["id"],"no usable effective_from",r["effective_to"],r["publication_date"],r["retrieved_on"]))
    if not vo and ret:
        r["verified_on"]=str(ret); notes.append("verified_on_basis: retrieved_on (date the copy was read)"); log["vo_ret"]+=1
    if et and et<T:
        r["status"]="superseded" if r["id"] in superseded_ids else "historical"; log["closed_"+r["status"]]+=1
    if notes:
        r["verification_method"]=(r["verification_method"]+" | " if r["verification_method"] else "")+"; ".join(notes)
print(log); print(odd)
if "--write" in sys.argv:
    with open(P,"w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=cols,lineterminator="\n"); w.writeheader(); w.writerows(rows)
