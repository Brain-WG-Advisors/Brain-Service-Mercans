p='build_annexes.py'; s=open(p,encoding='utf-8').read()
for w in ['"in": "IN", ','"or": "OR", ','"me": "ME", ','"hi": "HI", ','"id": "ID", ','"ok": "OK", ','"de": "DE", ','"ar": "AR", ','"al": "AL", ']:
    s=s.replace(w,'')
s=s.replace('"wy": "WY", "nc": "NC"}','"wy": "WY", "nc": "NC", "vi": "VI", "eo13706": "EO 13706", "de9c": "DE 9C", "gtl": "GTL", "pub701": "Pub. 701", "ssn": "SSN", "econsent": "electronic consent"}')
s=s.replace('''    close = OV.gap_close(unit, g["key"]) or clean(g.get("what_would_close_it", ""))''','''    close = OV.gap_close(unit, g["key"]) or clean_close(g.get("what_would_close_it", ""))''')
s=s.replace('''                            parts.append(f"⚠️ RESEARCH-GAP ({blk}): not established. Would close it: {clean(it.get('what_would_close_it', ''))}")''','''                            cl = OV.gap_close(unit, it["key"]) or clean_close(it.get("what_would_close_it", ""))
                            parts.append(f"⚠️ RESEARCH-GAP ({blk}): not established. Would close it: {cl}")''')
s=s.replace('''GAPLOC = {}''','''GAPLOC = {}


def clean_close(t):
    t = clean(t)
    t = re.sub(r"\s*\((?:[^()]*?(?:browser pass|Chrome pass|curl|md5|one fetch|VPN|held file|held PDF)[^()]*)\)", "", t)
    t = re.sub(r",?\s*(?:read )?(?:via|through|with) (?:the )?(?:orchestrator )?(?:browser pass|VPN|Wayback(?: route)?)", "", t)
    t = re.sub(r"\s*(?:Parallel|parallel) fan-out per [a-z]+\.?", "", t)
    t = re.sub(r";\s*$", "", t).strip()
    t = t.replace(" read via Wayback", "").replace(" on akleg", " (Alaska Legislature site)")
    return t''')
open(p,'w',encoding='utf-8').write(s)
