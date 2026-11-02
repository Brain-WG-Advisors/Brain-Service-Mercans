import sys,glob,openpyxl
sys.path.insert(0,'_check'); sys.stdout.reconfigure(encoding='utf-8')
from xsurg import edit
def get(f,sh,ref): return openpyxl.load_workbook(f)[sh][ref].value
def rep(f,sh,ref,old,new):
    v=get(f,sh,ref); assert old in v,(sh,ref,old); return v.replace(old,new)
P3=glob.glob('PILA/CO-PILA-003*.xlsx')[0]; P7=glob.glob('PILA/CO-PILA-007*.xlsx')[0]
NE=glob.glob('NE/*.xlsx')[0]
F2=glob.glob('FORMS/CO-DIAN-002*.xlsx')[0]; F4=glob.glob('FORMS/CO-DIAN-004*.xlsx')[0]; F5=glob.glob('FORMS/CO-DIAN-005*.xlsx')[0]
LEY="Ley 100 de 1993 art. 15 num. 2 (as modified by Ley 797 de 2003 art. 3)"
TXT=("foreigners who remain in the country under an employment contract and are not covered by a pension regime of their country of origin or of any other country are voluntary affiliates")
# ---- PILA 003
e={}
e[('Report Matrix','A36')]=("- The one immigration-related field is 'Foreign national not liable to contribute to pensions' (T2R2-007), and it is about PENSION AFFILIATION, not tax residence. AT2 v30 (24-07-2026) §2.1.2.3.3 (campo 7) defines it as a foreign citizen who is not obliged by law to contribute to the General Pension System but must contribute to the other subsystems. The legal text behind the configuration is "+LEY+": "+TXT+". The specification states no rule beyond that text; the flag is an option per employee, kept with this citation. Health, occupational risk and the parafiscal levies remain fully payable.")
e[('PILA Spec','M69')]=("Marks a foreign national who is not obliged by law to contribute to the General Pension System (AT2 v30 (24-07-2026) §2.1.2.3.3, campo 7). Legal text behind the configuration: "+LEY+": "+TXT+". The flag is an option per employee, kept with this citation; the specification states no rule beyond that text. Health, occupational risk and the parafiscal levies remain fully payable - only pension is not reported.")
e[('Population Rules','C22')]=("Mark T2R2-007 only for a foreign national for whom the employer has configured, as an option per employee and with the citation "+LEY+", that pension affiliation does not apply ("+TXT+"). Health, occupational risk and the parafiscal levies remain fully payable. The flag narrows the valid document types to CE, PA, CD, SC, PE and PT.")
e[('Payroll Scope Summary','C46')]="Flagged in campo 7. No pension contribution is reported for the flagged foreign national (AT2 v30 §2.1.2.3.3); health, occupational risk and the levies remain."
v=get(P3,'PILA Spec','M120')
a="For contributors reported 'N' in campo 5 of the file 'INFORMACION DE LA AFILIACION A PENSIONES' (Ley 2381 de 2024 art. 20), a second table applies"
assert a in v
v=v.replace(a,"For contributors reported 'N' in campo 5 of the file 'INFORMACION DE LA AFILIACION A PENSIONES', a second table (Ley 2381 de 2024 art. 20) applies")
old="The rule that, from July 2025, the value for contributors reported 'N' is sent only in the ACCAI output files belongs to campo 51 (solidarity sub-account, T2R2-051), not to this field."
assert old in v
v=v.replace(old,"This Ley 2381 table applies only from the date Ley 2381/2024 is in force; until then, Ley 797/2003 table (the CCG records Ley 2381 as not in force for 2026 payroll). The rule that, from July 2025, the value for contributors reported 'N' is sent only in the ACCAI output files applies to this field as well as to campo 51 (solidarity sub-account, T2R2-051) (AT2 v30 p.158 within §2.1.2.3.19; p.157 within §2.1.2.3.18).")
e[('PILA Spec','M120')]=v
e[('PILA Spec','G120')]=rep(P3,'PILA Spec','G120',"the Ley 2381 de 2024 table in M120 applies instead.","the Ley 2381 de 2024 table in M120 applies instead only from the date Ley 2381/2024 is in force; until then, Ley 797/2003 table.")
e[('PILA Spec','L107')]="Employee.PILA_Salary_Type"
e[('PILA Spec','L152')]="Employee.PILA_Special_Pension_Rate_Indicator"
e[('PILA Spec','J47')]="N(10) - numeric, right-justified, ZERO-filled to the left when populated; BLANK (10 spaces, positions 228-237) where the return type does not call for it (see G47)"
edit(P3,e)
# ---- PILA 007
edit(P7,{('PILA Pensioners Spec','M104'):rep(P7,'PILA Pensioners Spec','M104',"or, with N, 1.0% to 2.5% from 4 SMLMV (Ley 2381 de 2024 art. 20).","or, with N, 1.0% to 2.5% from 4 SMLMV (Ley 2381 de 2024 art. 20; applies only from the date Ley 2381/2024 is in force; until then, Ley 797/2003 table).")})
# ---- NE
ne={('File Structure','B23'):'  |-- Novedad  @CUNENov                                    NIE199 / NIE204   0-1',
    ('File Structure','B24'):'  |-- Periodo  @FechaIngreso @FechaRetiro',
    ('File Structure','B39'):'  |-- Empleador  @RazonSocial @PrimerApellido @SegundoApellido',
    ('File Structure','B43'):'  |-- Trabajador  @TipoTrabajador @SubTipoTrabajador',
    ('File Structure','B51'):'  |-- Pago  @Forma @Metodo @Banco @TipoCuenta',
    ('File Structure','B69'):'  |     |-- Cesantias @Pago @Porcentaje @PagoIntereses NIE120-NIE122    0-1',
    ('File Structure','B92'):'  |-- Deducciones',
    ('File Structure','B112'):'  |-- Redondeo                                        NIE186   0-1'}
edit(NE,ne)
# ---- FORMS
edit(F2,{('Example Analysis','C15'):rep(F2,'Example Analysis','C15',"x 52,374 = COP 617,232; approximated to the nearest 1,000 under ET art. 868 = COP 617,000.","x 52,374 = COP 617,232 (the amount withheld and carried unrounded by the electronic payroll); the form approximates it to the nearest 1,000 under DUR 1625 de 2016 art. 1.6.1.11.11 = COP 617,000."),
 ('Example Analysis','D15'):"Casilla 93 plus casilla 94 must equal SUM(NIE177) across the month's electronic payroll documents, apart from the form's approximation to the nearest 1,000 (DUR 1625 de 2016 art. 1.6.1.11.11). Here casilla 94 is nil and there is one document carrying 617,232.00 (unrounded); casilla 93 carries 617,000 after the form approximation.",
 ('Formulario 350 Spec','K20'):None})
edit(F4,{('Example Analysis','A27'):'7.406.784',('Example Analysis','A30'):'7.406.784',('Example Analysis','A36'):'7.406.784',
 ('Example Analysis','C27'):rep(F4,'Example Analysis','C27',"twelve ordinary months at COP 617,000 = 7,404,000","twelve ordinary months at COP 617,232 (unrounded, as carried by the electronic payroll) = 7,406,784"),
 ('Example Analysis','D33'):get(F4,'Example Analysis','D33').replace("7,404,000","7,406,784"),
 ('Formulario 220 Spec','K52'):'7406784',('Formulario 220 Spec','K63'):'7406784',
 ('Sample File','A79'):get(F4,'Sample File','A79').replace('7.404.000','7.406.784'),
 ('Sample File','A90'):get(F4,'Sample File','A90').replace('7.404.000','7.406.784')})
edit(F5,{('Formato 2276 Spec','K37'):'7406784',('Example Analysis','A27'):'7406784',
 ('Example Analysis','D33'):rep(F5,'Example Analysis','D33',"(7,404,000 / 169,440,000)","(7,406,784 / 169,440,000)"),
 ('Sample File','A77'):get(F5,'Sample File','A77').replace('7404000','7406784')})
print('done')
