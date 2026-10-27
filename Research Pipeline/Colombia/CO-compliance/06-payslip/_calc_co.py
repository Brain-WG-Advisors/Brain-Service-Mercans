from decimal import Decimal as D, ROUND_HALF_EVEN, ROUND_UP
def r2(x): return D(x).quantize(D('0.01'), rounding=ROUND_HALF_EVEN)
UVT=D('52374'); SMMLV=D('1750905'); AUX=D('249095')
DIV=D('210')            # ordinary-hour divisor from 15 Jul 2026 (Ley 2101 42h week)
BAS=D('8000000')
hour=BAS/DIV
print('ordinary hour',r2(hour))
hed_h=D('6');  hed_rate=r2(hour*D('1.25')); hed=r2(hed_rate*hed_h)
rn_h=D('10');  rn_rate=r2(hour*D('0.35'));  rn=r2(rn_rate*rn_h)
com=D('1200000'); bonNS=D('500000'); aux=D('0')
print('HED rate',hed_rate,'amt',hed,'| RN rate',rn_rate,'amt',rn)
gross=r2(BAS+hed+rn+com+bonNS+aux); print('GROSS',gross)
# --- IBC ---
salary_items=BAS+hed+rn+com
clamp=r2(gross*D('0.40')); print('40% clamp',clamp,'non-salary',bonNS,'-> clamp bites?',bonNS>clamp)
ibc=D(salary_items).quantize(D('1'),rounding=ROUND_UP)
print('IBC',ibc,'floor ok',ibc>=SMMLV,'ceiling ok',ibc<=25*SMMLV)
salud=r2(ibc*D('0.04')); pens=r2(ibc*D('0.04'))
fsp = r2(ibc*D('0.01')) if ibc>=4*SMMLV else D('0')
fsp_sub = r2(ibc*D('0.002')) if ibc>=16*SMMLV else D('0')
print('salud',salud,'pension',pens,'fsp',fsp,'fsp_sub',fsp_sub,'4SMMLV',4*SMMLV,'16SMMLV',16*SMMLV)
# --- retencion ---
A=gross
B=salud+pens+fsp
C=r2(A-B)
prepaid=D('200000'); cap387=r2(16*UVT)
Ddec=min(prepaid,cap387)
E=r2((C-Ddec)*D('0.25')); cap790=r2(D('790')/12*UVT)
E=min(E,cap790)
cap40=r2(C*D('0.40')); cap1340=r2(D('1340')/12*UVT)
DE=min(Ddec+E,cap40,cap1340)
G=r2(C-DE)
print('A',A,'B',B,'C',C,'D',Ddec,'(cap',cap387,') E',E,'(cap790/12',cap790,') 40%cap',cap40,'1340cap',cap1340,'D+E',DE)
print('taxable base G',G,'UVT',r2(G/UVT))
bands=[(D('95'),D('0'),D('0')),(D('150'),D('0.19'),D('0')),(D('360'),D('0.28'),D('10')),
       (D('640'),D('0.33'),D('69')),(D('945'),D('0.35'),D('162')),(D('2300'),D('0.37'),D('268')),
       (None,D('0.39'),D('770'))]
def ret(base):
    u=base/UVT; lo=D('0')
    for top,rate,add in bands:
        if top is None or u<=top:
            return r2((u-lo)*rate*UVT+add*UVT), lo, rate
        lo=top
    return None
rf,lo,rate=ret(G); print('band lower',lo,'rate',rate,'RETENCION',rf)
libranza=D('350000')
ded=r2(salud+pens+fsp+rf+prepaid+libranza); print('TOTAL DED',ded)
net=r2(gross-ded); print('NET',net)
# --- employer ---
arl=r2(ibc*D('0.00522')); pen_er=r2(ibc*D('0.12')); ccf=r2(ibc*D('0.04'))
print('ER pension',pen_er,'ARL I',arl,'CCF',ccf,'(salud/SENA/ICBF exonerated 114-1, threshold 10 SMMLV',10*SMMLV,')')
er_tot=r2(pen_er+arl+ccf); print('ER TOTAL',er_tot)
# --- provisions ---
base_prest=r2(salary_items+aux)
prima=r2(base_prest*D('0.083333')); ces=r2(base_prest*D('0.083333')); inte=r2(base_prest*D('0.01'))
base_vac=r2(BAS+rn+com)   # CST 192 excludes overtime & rest-day work
vac=r2(base_vac*D('0.041667'))
print('base prestacional',base_prest,'prima',prima,'cesantias',ces,'intereses',inte)
print('base vacaciones',base_vac,'vacaciones',vac)
print('PROV TOTAL',r2(prima+ces+inte+vac))
print('EMPLOYER COST',r2(gross+er_tot+prima+ces+inte+vac))
# --- prima paid June 2026 (separate art.385 read) ---
primaJun=r2(base_prest*D('180')/D('360'))
pE=r2(primaJun*D('0.25')); pbase=r2(primaJun-min(pE,cap790))
print('June prima',primaJun,'taxable',pbase,'UVT',r2(pbase/UVT),'-> retencion',ret(pbase)[0])
# --- YTD (8 months constant + June prima) ---
ytd_gross=r2(gross*8+primaJun); ytd_ss=r2((salud+pens+fsp)*8); ytd_tax=r2(rf*8)
ytd_vol=r2((prepaid+libranza)*8); ytd_net=r2(ytd_gross-ytd_ss-ytd_tax-ytd_vol)
print('YTD gross',ytd_gross,'ss',ytd_ss,'tax',ytd_tax,'vol',ytd_vol,'net',ytd_net)
# CCG worked example cross-check
print('--- CCG cross-check: plain 8,000,000 ---')
b=r2(D('8000000')*D('0.09')); cc=r2(D('8000000')-b); ee=r2(cc*D('0.25')); gg=r2(cc-ee)
print('B',b,'C',cc,'E',ee,'G',gg,'ret',ret(gg)[0],'(CCG says 92,049.30)')
