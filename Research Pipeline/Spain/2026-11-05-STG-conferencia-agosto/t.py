exec(open('base.py',encoding='utf-8').read())
D=['2514','2515','2551','2552','2555','2556','2572','21140','21142','2582']; R=['2533','2534','2535','2550','2560','2565','2566']
EA=['62100','62147','62148','62182','62512','62871','62875','79413','79414','79415','79416','65500','65630','65850']
b=0
for e in E:
    g=sum(f(e,k) for k in EA); td=sum(f(e,k) for k in D); te=sum(f(e,k) for k in R)
    for nm,x,y in [('gross',g,f(e,'GROSS')),('totded',td,f(e,'TOTDED')),('net',f(e,'GROSS')-f(e,'TOTDED'),f(e,'NET')),('toter',te,f(e,'TOTER'))]:
        if abs(x-y)>0.011: print(e['id'],nm,round(x,2),y); b+=1
print('mismatches',b)
