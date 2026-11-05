exec(open('base.py',encoding='utf-8').read())
m=json.load(open('m145.json')); M=m['M']; F=m['F']
ids={e['id'] for e in E}
print('M145 not in G2N:',[k for k in M if k not in ids]); print('G2N not in M145:',[k for k in ids if k not in M])
for e in E:
    mm=M.get(e['id'],{})
    desc=[y for y,i in mm.get('fam',[]) if y and y>=2002]
    asc=[y for y,i in mm.get('fam',[]) if y and y<1960]
    u3=[y for y in desc if y>=2024]
    print(e['id'],'sit',mm.get('sit'),'58216',f(e,'58216'),'68470',f(e,'68470'),'| desc',desc,'u3',u3,'asc',asc,'FS',F.get(e['id']),'| 58233',f(e,'58233'),'68473',f(e,'68473'),'58892',f(e,'58892'),'58890',f(e,'58890'),'age',f(e,'58210'),'58170',f(e,'58170'),'alim',mm.get('alim'),'viv',mm.get('viv'),'ent',mm.get('entero'))
