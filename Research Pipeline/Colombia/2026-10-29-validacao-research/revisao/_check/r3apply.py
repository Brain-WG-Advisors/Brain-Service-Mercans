import sys,glob,openpyxl,hashlib
sys.path.insert(0,'_check'); sys.stdout.reconfigure(encoding='utf-8')
from xsurg import edit
def get(f,sh,ref):
    w=openpyxl.load_workbook(f,read_only=True); v=w[sh][ref].value; w.close(); return v
def rep(f,sh,ref,old,new):
    v=get(f,sh,ref); assert old in v,(sh,ref,old); return v.replace(old,new)
g=lambda p: glob.glob(p)[0]
F2=g('FORMS/CO-DIAN-002*.xlsx');F4=g('FORMS/CO-DIAN-004*.xlsx');F5=g('FORMS/CO-DIAN-005*.xlsx')
NE=g('NE/*.xlsx');P3=g('PILA/CO-PILA-003*.xlsx');P7=g('PILA/CO-PILA-007*.xlsx');DD=g('DD/*.xlsx')
before={f:hashlib.md5(open(f,'rb').read()).hexdigest() for f in (F2,F4,F5,NE,P3,P7,DD)}
LEY="Ley 100 de 1993 art. 15 num. 2 (as modified by Ley 797 de 2003 art. 3)"
def vc(f,sh,ref,add): return get(f,sh,ref).rstrip().rstrip('.') + ', '+add+'.'
# 1. 004
K='7407000'
e4={('Formulario 220 Spec','K52'):K,('Formulario 220 Spec','K63'):K,
 ('Example Analysis','A27'):'7.407.000',('Example Analysis','A30'):'7.407.000',('Example Analysis','A36'):'7.407.000',
 ('Example Analysis','C27'):rep(F4,'Example Analysis','C27',"twelve ordinary months at COP 617,232 (unrounded, as carried by the electronic payroll) = 7,406,784,","twelve ordinary months at COP 617,232 (the withholding is not rounded per employee per month) = 7,406,784 unrounded annual sum; approximated to the nearest 1.000 per this spec's reporting rule (C12) = 7,407,000,"),
 ('Example Analysis','D33'):get(F4,'Example Analysis','D33').replace("33,888,000 / 7,406,784 = 4.58","33,888,000 / 7,407,000 = 4.58").replace("COP 7,406,784","COP 7,407,000"),
 ('Sample File','A79'):get(F4,'Sample File','A79').replace('7.406.784','7.407.000'),
 ('Sample File','A90'):get(F4,'Sample File','A90').replace('7.406.784','7.407.000')}
assert "7,407,000" in e4[('Example Analysis','D33')]
e4[('Version Control','D14')]=vc(F4,'Version Control','D14',"SIM-03 (casillas 60/75 = 7,407,000: 12 x 617,232 approximated to the nearest 1,000)")
edit(F4,e4)
# 2. 002
e2={('Population Rules','C5'):rep(F2,'Population Rules','C5',"Each employee's withholding is itself already approximated to the nearest 1,000 under ET art. 868; accumulate those approximated figures and then apply the art. 577 nearest-1,000 rounding to the total.","An employee's monthly withholding is not rounded: accumulate the unrounded figures. The approximation to the nearest 1,000 applies only to the Form 350 return values (DUR 1625 de 2016 art. 1.6.1.11.11), that is, to the casilla 93 total."),
 ('Version Control','D14'):vc(F2,'Version Control','D14',"SIM-03 (C5, C15, D15)")}
edit(F2,e2)
# 005 : only VC
edit(F5,{('Version Control','D14'):vc(F5,'Version Control','D14',"SIM-03 (N29 = 7,406,784, unrounded: no 1,000 approximation in this format)")})
# NE
edit(NE,{('Population Rules','C21'):rep(NE,'Population Rules','C21',"convert back to pesos, and approximate to the nearest 1,000 under ET art. 868.","convert back to pesos (two decimals). The monthly withholding is not rounded per employee: the approximation to the nearest 1,000 applies only to the Form 350 return values (DUR 1625 de 2016 art. 1.6.1.11.11)."),
 ('File Structure','B119'):'  |-- Reemplazar     (present only when TipoNota = 1)',
 ('File Structure','B121'):'  +-- Eliminar        (present only when TipoNota = 2)',
 ('Version Control','D14'):vc(NE,'Version Control','D14',"NE-05, SIM-03 (C21), adjustment-note XSD names (B119, B121)")})
# PILA VC
edit(P3,{('Version Control','D14'):get(P3,'Version Control','D14').replace(' See CHANGELOG.md.','').rstrip().rstrip('.')+', A-16, DD-07/DD-11 (L107, L152 system names). See CHANGELOG.md.'})
edit(P7,{('Version Control','D14'):get(P7,'Version Control','D14').replace(' See CHANGELOG.md.','').rstrip().rstrip('.')+', P-02 (M104). See CHANGELOG.md.'})
# DD
dd={}
dd[('Country Fields','G11')]=rep(DD,'Country Fields','G11',"and, together with proof of affiliation to a foreign pension system, the foreign-national pension-waiver flag.","and, for a foreign national under an employment contract, the voluntary pension affiliation option of "+LEY+" (see the Foreign National Not Pension Liable Flag field; kept as an option per employee).")
dd[('Country Fields','W61')]="Spec ref: Employee.Foreign_Not_Pension_Liable_Flag - CO-PILA-003 v1.1 (T2R2-007, Mandatory=C). Calculation-driving: where the option is set for the employee, the pension contribution is not reported (voluntary affiliation of foreigners under an employment contract not covered by a pension regime of their country of origin or any other: "+LEY+"). Option per employee. Health, occupational risk and the payroll levies continue to apply."
dd[('Country Fields','W36')]=rep(DD,'Country Fields','W36',"CO-PILA-003 (T2R2-041, Mandatory=C).","CO-PILA-003 v1.1 (T2R2-041, Mandatory=C; carried by Employee.PILA_Salary_Type, see the PILA Salary Type field).")
dd[('Country Fields','W38')]=rep(DD,'Country Fields','W38',"CO-PILA-003 (T2R2-079, Mandatory=C).","CO-PILA-003 v1.1 (T2R2-079, Mandatory=C; carried by Employee.PILA_Special_Pension_Rate_Indicator, see the PILA Special Pension Rate Indicator field).")
dd[('Country Fields','W112')]=rep(DD,'Country Fields','W112',"Spec ref: CO-PILA-003 (T2R2-041, Mandatory=C).","Spec ref: Employee.PILA_Salary_Type - CO-PILA-003 v1.1 (T2R2-041, Mandatory=C).")
dd[('Country Fields','W113')]=rep(DD,'Country Fields','W113',"Spec ref: CO-PILA-003 (T2R2-079, Mandatory=C).","Spec ref: Employee.PILA_Special_Pension_Rate_Indicator - CO-PILA-003 v1.1 (T2R2-079, Mandatory=C).")
dd[('Version Control','D17')]=get(DD,'Version Control','D17').rstrip().rstrip('.')+", A-16 (G11, G61, W61), PILA-003 v1.1 references (W36, W38, W112, W113)."
edit(DD,dd)
for f in before: print(f.split('/')[-1][:30],before[f],hashlib.md5(open(f,'rb').read()).hexdigest())


