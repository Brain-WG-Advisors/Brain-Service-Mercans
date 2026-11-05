exec(open('base.py',encoding='utf-8').read())
print(len(E))
e=E[0]
for k,v in e.items(): print(k,v, end=' | ')
