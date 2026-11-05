exec(open('base.py',encoding='utf-8').read())
w=json.load(open('wtc.json',encoding='utf-8'))['rows']
earn=['62100','62147','62148','62182','62512','62871','62875','79413','79414','79415','79416','65500','65630','65850']
bad={}
def chk(name,e,exp,got,tol=0.011):
    if abs(exp-got)>tol: bad.setdefault(name,[]).append((e['id'],round(exp,2),got,round(got-exp,2)))
fl={'1.0':'52981','3.0':'52983','5.0':'52984','2.0':'52982'}
def sol(x):
    mb=5101.2; ex=max(0,x-mb); t=[min(ex,mb*0.1), min(max(ex-mb*0.1,0),mb*0.4), max(ex-mb*0.5,0)]
    return t
for e in E:
    bccc=sum(f(e,k) for k in earn if w[k][15]=='Yes')
    bccp=sum(f(e,k) for k in earn if w[k][16]=='Yes')
    if f(e,'58235'): bccc+=f(e,'64552'); bccp+=f(e,'64553')
    bccc+=f(e,'58140'); bccp+=f(e,'58140')
    chk('58150 vs WTC-flag sum (+58140,+IT base)',e,bccc,f(e,'58150'))
    chk('58152 vs WTC-flag sum',e,bccp,f(e,'58152'))
    grp=str(f(e,'58239')); flo=f(e,fl[grp])
    cap=f(e,'52991')
    exp151=min(max(f(e,'58150'),flo),cap); exp153=min(max(f(e,'58152'),flo),cap)
    chk('58151 floor/cap',e,exp151,f(e,'58151')); chk('58153 floor/cap',e,exp153,f(e,'58153'))
    B=f(e,'58151'); P=f(e,'58153')
    r=lambda k: f(e,k)/100
    for code,base,pc in [('2551',B,'52551'),('2556',B,'52556'),('2555',P,'52555'),('2514',P,'52514'),('2550',B,'52550'),('2566',B,'52566'),('2565',P,'52565'),('2533',P,'52533'),('2534',P,'52534'),('2560',P,'52560')]:
        chk(code,e,round(base*r(pc)+1e-9,2),f(e,code))
    chk('58535=58150',e,f(e,'58150'),f(e,'58535'))
    t=sol(f(e,'58535'))
    ee=sum(round(a*b,2) for a,b in zip(t,[.0019,.0021,.0024])); er=sum(round(a*b,2) for a,b in zip(t,[.0096,.0104,.0122]))
    ee2=round(sum(a*b for a,b in zip(t,[.0019,.0021,.0024])),2); er2=round(sum(a*b for a,b in zip(t,[.0096,.0104,.0122])),2)
    if abs(ee-f(e,'2515'))>0.011 and abs(ee2-f(e,'2515'))>0.011: bad.setdefault('2515',[]).append((e['id'],f(e,'58535'),ee,ee2,f(e,'2515')))
    if abs(er-f(e,'2535'))>0.011 and abs(er2-f(e,'2535'))>0.011: bad.setdefault('2535',[]).append((e['id'],f(e,'58535'),er,er2,f(e,'2535')))
    if f(e,'58214')!=1: print('PT',e['id'],f(e,'58214'),f(e,'58150'),f(e,'58151'),flo,f(e,'52992'))
for k,v in bad.items(): print('##',k,len(v)); print('  ',v[:12])
from collections import Counter
for k in ['52551','52556','52555','52514','52550','52566','52565','52533','52534','52560','52991','52981','52983','52984','52517','52537']:
    print(k,Counter(f(e,k) for e in E))
