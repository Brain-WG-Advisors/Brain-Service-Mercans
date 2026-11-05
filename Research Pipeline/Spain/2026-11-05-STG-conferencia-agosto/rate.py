exec(open('base.py',encoding='utf-8').read())
import math, openpyxl
wb=openpyxl.load_workbook('C:/Users/instituto/Documents/brain-service/raw/tickets/api/anexos/HRBS-16884/20261104-2318 - 2608 ES03 %IRPF.xlsx',data_only=True)
ws=wb.active; ADP={str(r[0].value):r[3].value for r in ws.iter_rows(min_row=2) if r[0].value}
nr=nt=0; rows=[]
for e in E:
    calc=f(e,'58118'); vol=round(f(e,'58217')*100,4)
    q=f(e,'58115')/f(e,'58117')*100 if f(e,'58117') else 0
    tr=math.floor(q*100)/100; ro=round(q,2)
    if abs(calc-tr)>0.001: nt+=1
    if abs(calc-ro)>0.001: nr+=1
    cash=f(e,'58552'); 
    applied= f(e,'2552')/cash*100 if cash else 0
    appB = f(e,'2572')/f(e,'58572')*100 if f(e,'58572') else None
    exp_max=max(calc,vol)
    adp=ADP.get(e['id']); adp=adp*100 if adp is not None else None
    rows.append((e['id'],round(q,4),calc,vol,adp,round(applied,3),None if appB is None else round(appB,3),round(cash*calc/100,2),f(e,'2552'),round(f(e,'2552')-cash*calc/100,2)))
print('calc!=trunc',nt,'calc!=round',nr)
print('id q 58118 vol ADP applied_cash applied_bik 2552@calc 2552 diff')
tot=0
for r in rows: print(*r); tot+=r[-1]
print('total diff 2552 vs calc', round(tot,2))
print('ids in ADP not G2N',[k for k in ADP if k not in {e['id'] for e in E}])
# voluntary < calc
print('vol<calc',[ (r[0],r[2],r[3],r[5]) for r in rows if r[3] and r[3]<r[2]])
print('vol==0',[ (r[0],r[2],r[4],r[5]) for r in rows if not r[3]])
