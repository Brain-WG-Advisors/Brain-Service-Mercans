exec(open('irpf.py',encoding='utf-8').read().split('bad={}')[0])
import math
def applied(e):
    return f(e,'2552')/f(e,'58552')*100 if f(e,'58552') else 0
# A1
tot=0; n=0; nc=0; ex=None
for e in E:
    if e['id']=='1018096': continue
    r=round(applied(e),2)
    expbase=f(e,'65500')+f(e,'65850')
    exp=round(expbase*r/100,2); d=exp-f(e,'2572')
    if abs(d)>0.005: n+=1; tot+=d
    if f(e,'65500'): nc+=1
    if e['id']=='1001440': ex=(r,expbase,exp,f(e,'2572'),f(e,'58572'))
print('A1 n',n,'tot',round(tot,2),'car emps',nc,'ex',ex, 'sum65500',round(sum(f(e,'65500') for e in E),2))
# A2 vol<calc
t=0
for e in E:
    c=f(e,'58118'); v=f(e,'58217')*100
    if v and v<c-0.001: d=round(f(e,'58552')*(c-v)/100,2); t+=d; print('A2',e['id'],c,round(v,2),d)
print('A2 tot',round(t,2))
# B min changes
def newrate(e,dmin=0,dbase=0,alim=None,viv=False):
    base=f(e,'58169')+dbase; mn=f(e,'58170')+dmin
    if alim:
        q1=scale(alim)+scale(base-alim); q2=scale(mn+1980)
    else: q1=scale(base); q2=scale(mn)
    tax=max(0,q1-q2)
    rem=tax+f(e,'58113')+f(e,'58114')
    r=math.floor(rem/f(e,'58117')*10000)/100
    if viv: r=max(0,r-2)
    return max(0,r)
for i,dm in [('1001455',1400),('1001469',1400),('1016187',1400),('1016646',1400),('1016838',1400),('1014186',1400),('1001484',1200)]:
    e=[x for x in E if x['id']==i][0]; nr=newrate(e,dm); print('B min',i,f(e,'58118'),'->',nr, 'Aug € at that rate', round(f(e,'58552')*(f(e,'58118')-nr)/100,2))
e=[x for x in E if x['id']=='1001454'][0]; nr=newrate(e,alim=9955); print('B alim 1001454',f(e,'58118'),'->',nr,round(f(e,'58552')*(f(e,'58118')-nr)/100,2))
e=[x for x in E if x['id']=='1001483'][0]; print('B viv 1001483',f(e,'58118'),'->',newrate(e,viv=True),f(e,'58163'))
e=[x for x in E if x['id']=='1001452'][0]; nr=newrate(e,2550); print('B asc 1001452',f(e,'58118'),'->',nr)
# 85.3 cap
thr={1:{0:17644,1:17644,2:18694},2:{0:17197,1:18130,2:19262},3:{0:15876,1:16342,2:16867}}
for e in E:
    if 0<f(e,'58163')<=35200:
        s=int(f(e,'58216')); k=min(int(f(e,'58233')),2)
        cap=0.43*max(0,f(e,'58163')-thr[s][k]); print('85.3',e['id'],f(e,'58163'),'quota',f(e,'58173'),'cap',round(cap,2))
# projection components
print('5x62512 per emp', 5*96.56, 'n62512',sum(1 for e in E if f(e,'62512')))
e=[x for x in E if x['id']=='1001440'][0]
print('1001440 58008',f(e,'58008'),'64992',f(e,'64992'),'58009',f(e,'58009'),'62875',f(e,'62875'))
print('n 62875>0',sum(1 for e in E if f(e,'62875')), 'sum', round(sum(f(e,'62875') for e in E),2))
print('58238=2 ids',[e['id'] for e in E if f(e,'58238')==2]); print('58140>0',[e['id'] for e in E if f(e,'58140')])
# truncation diff
print('trunc diffs',sum(1 for e in E if f(e,'58117') and abs(math.floor(f(e,'58115')/f(e,'58117')*10000)/100-f(e,'58118'))>0.001))
# 62147 ratio and 64993
from collections import Counter
print(Counter(round(f(e,'62147')/f(e,'62100'),4) for e in E if f(e,'62100')))
print('64993=62100+62182',sum(1 for e in E if abs(f(e,'64993')-f(e,'62100')-f(e,'62182'))<0.011),'64993=62100',sum(1 for e in E if abs(f(e,'64993')-f(e,'62100'))<0.011))
print('health tax effect: 176.39 x applied rate total', round(sum((-(f(e,'58105'))-0)*applied(e)/100 for e in E if e['id']!='1018096'),2))
print('car effect total', round(sum(f(e,'65500')*applied(e)/100 for e in E),2))
print('64440==64992',sum(1 for e in E if abs(f(e,'64440')-f(e,'64992'))<0.01))
