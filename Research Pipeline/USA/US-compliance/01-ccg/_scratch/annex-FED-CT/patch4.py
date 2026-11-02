p='build_annexes.py'; s=open(p,encoding='utf-8').read()
old='''        if OV.keep_pack_prose(unit, sid):'''
new='''        use_pack = OV.keep_pack_prose(unit, sid) or (extra is None and not flist and sid not in ("SP", "LG", "OR"))
        if use_pack and narrative:
            PACKPROSE.append((unit, sid))
        if use_pack:'''
assert old in s; s=s.replace(old,new)
s=s.replace('''AMBIG = []
''','''AMBIG = []
PACKPROSE = []
''',1)
# empty-section fallback: after writing heading block, check if anything written
old2='''        for p in OV.after_section(unit, sid):
            W(fill(p, facts))
            W("")'''
new2='''        for p in OV.after_section(unit, sid):
            W(fill(p, facts))
            W("")
        if L[-1] == "" and L[-2].startswith("## "):
            W(f"No {title}-specific rule for this domain is recorded in the research.")
            W("")'''
assert old2 in s; s=s.replace(old2,new2)
# sources sorted by S number
old3='''    for rid in used:
        r = REG.get(rid, {})'''
new3='''    for rid in sorted(used, key=lambda x: int(SRC.get(x, "S9999")[1:]) if x in SRC else 9999):
        if rid not in SRC:
            src_cell({rid})
        r = REG.get(rid, {})'''
assert old3 in s; s=s.replace(old3,new3)
open(p,'w',encoding='utf-8').write(s)
