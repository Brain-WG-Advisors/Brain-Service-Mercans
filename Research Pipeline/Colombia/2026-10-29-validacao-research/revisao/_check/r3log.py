import json,glob,hashlib,sys,openpyxl
sys.stdout.reconfigure(encoding='utf-8')
B=r"C:\Users\instituto\Documents\brain-service\Research Pipeline\Colombia"
g=lambda p: glob.glob(p)[0]
md5=lambda p: hashlib.md5(open(p,'rb').read()).hexdigest()
def val(f,sh,ref):
    w=openpyxl.load_workbook(f,read_only=True); v=w[sh][ref].value; w.close(); return v
def esc(s): return str(s).replace('|','\\|').replace('\n',' ')
cfg={
 'FORMS/CHANGELOG.md':[('CO-DIAN-002','FORMS/CO-DIAN-002*.xlsx',B+r"\co-report-crosscheck\05-final\CO-DIAN-002-Formulario350-Spec.xlsx",'D002_r2',[('SIM-03 / R3-2','Population Rules','C5',"DUR 1625 de 2016 art. 1.6.1.11.11 (approximation applies to Form 350 return values only); SIM-03 (12 x 617,232)"),('R3-6','Version Control','D14',"Regra 8")]),
   ('CO-DIAN-004','FORMS/CO-DIAN-004*.xlsx',B+r"\co-report-crosscheck\05-final\CO-DIAN-004-Formulario220-Spec.xlsx",'D004_r2',[('SIM-03 / R3-1',s,r,"Retencao nao arredondada por empregado/mes (12 x 617.232 = 7.406.784); o certificado mantem a regra propria da spec (J/P27-67, Population Rules C12, Sample A16: aproximar a 1.000), aplicada uma vez ao total anual = 7.407.000") for s,r in [('Formulario 220 Spec','K52'),('Formulario 220 Spec','K63'),('Example Analysis','A27'),('Example Analysis','C27'),('Example Analysis','A30'),('Example Analysis','D33'),('Example Analysis','A36'),('Sample File','A79'),('Sample File','A90')]]+[('R3-6','Version Control','D14',"Regra 8")]),
   ('CO-DIAN-005','FORMS/CO-DIAN-005*.xlsx',B+r"\co-report-crosscheck\05-final\CO-DIAN-005-Formato2276-Spec.xlsx",'D005_r2',[('R3-6','Version Control','D14',"Regra 8")])],
 'NE/CHANGELOG.md':[('CO-DIAN-001','NE/*.xlsx',B+r"\co-report-crosscheck\05-final\CO-DIAN-001-NominaElectronica-Spec.xlsx",'NE_r2',[('SIM-03 / R3-2','Population Rules','C21',"DUR 1625 de 2016 art. 1.6.1.11.11; contradizia Example C39 (617.232,00)"),('R3-5','File Structure','B119',"XSD NominaIndividualDeAjusteElectronicaXSDV1.0.6.xsd: xsd:element name=\"Reemplazar\""),('R3-5','File Structure','B121',"XSD ...DeAjuste...1.0.6: xsd:element name=\"Eliminar\""),('R3-6','Version Control','D14',"Regra 8")])],
 'PILA/CHANGELOG.md':[('CO-PILA-003','PILA/CO-PILA-003*.xlsx',B+r"\co-report-crosscheck\05-final\CO-PILA-003-AportesSeguridadSocial-Spec.xlsx",'P003_r2',[('R3-6','Version Control','D14',"Regra 8")]),('CO-PILA-007','PILA/CO-PILA-007*.xlsx',B+r"\co-report-crosscheck\05-final\CO-PILA-007-AportesPensionados-Spec.xlsx",'P007_r2',[('R3-6','Version Control','D14',"Regra 8")])],
 'DD/CHANGELOG.md':[('CO-DD-001','DD/CO-DD-001*.xlsx',B+r"\2026-10-22-auditoria-lote1\CO-DD-001-v1.3.xlsx",'DD',[('R3-3','Country Fields','G11',"Ley 100 de 1993 art. 15 num. 2 (mod. Ley 797 de 2003 art. 3), texto local raw/docs/oficiais/CO"),('R3-3','Country Fields','W61',"idem"),('R3-4','Country Fields','W36',"PILA-003 v1.1 L107 Employee.PILA_Salary_Type"),('R3-4','Country Fields','W38',"PILA-003 v1.1 L152 Employee.PILA_Special_Pension_Rate_Indicator"),('R3-4','Country Fields','W112',"PILA-003 v1.1 L107"),('R3-4','Country Fields','W113',"PILA-003 v1.1 L152"),('R3-6','Version Control','D17',"Regra 8")])]}
ANTES="| ID | Onde | Antes (verbatim, DRAFT da rodada 2) | Depois (verbatim) | Fonte | Status |\n|---|---|---|---|---|---|\n"
for cl,items in cfg.items():
    s="\n\n## Rodada 3 (2026-10-29): correcao residual (CONFERENCIA-DRAFTS-R2)\n\nDecisoes do usuario: retencao nao arredondada por empregado/mes (SIM-03); certificado 220 aproxima o total anual a 1.000 pela regra da propria spec (C12); 002/NE sem arredondamento por empregado (ET 868 retirado, DUR 1.6.1.11.11 so para os valores do Form. 350); DD G11/W61 alinhados a Ley 100 art. 15 num. 2; DD W36/W38/W112/W113 -> PILA-003 v1.1 com nomes `Employee.PILA_*`; NE ajuste com nomes do XSD; Version Control. Edicao por cirurgia no XML (inlineStr, fundo FFDDEBF7, demais entradas do zip byte a byte). As tabelas das rodadas 1 e 2 acima que citam 7.406.784 na 004 ficam superadas por esta secao.\n\n"
    for name,gl,basef,jn,rows in items:
        f=g(gl); old=json.load(open(f'_check/{jn}.json',encoding='utf-8')); od={(c['sheet'],c['cell']):c['new'] for c in old['cells']}
        s+=f"### {name} (md5 DRAFT apos a rodada 3: {md5(f)})\n\n"+ANTES
        for i,sh,ref,src in rows:
            before=od.get((sh,ref)); 
            if before is None: before=val(basef,sh,ref)
            s+=f"| {i} | {sh}!{ref} | {esc(before)} | {esc(val(f,sh,ref))} | {esc(src)} | APLICADA |\n"
        s+="\n"
    if cl=='FORMS/CHANGELOG.md':
        s+="""### Nao alterada na rodada 3

| Item | Motivo |
|---|---|
| 005 (N29 / K37 / Example A27 / D33 / Sample A77 = 7.406.784) | O Formato 2276 tem convencao propria em File Structure!B27: inteiros em pesos, sem aproximar a 1.000 ("Store the unrounded value once and apply each convention at output"). B27 so cita o 1.000 para os Formularios 350 e 220, e continua correto. Aproximar o N29 a 7.407.000 criaria regra sem fonte. Fica 7.406.784 (somente o Version Control mudou). Divergencia 220 x 2276 (7.407.000 x 7.406.784) e consequencia das duas convencoes documentadas. |
| 004 J/P27-67, Population Rules A12/C12, Sample A16 | Ja mandam aproximar cada casilla a 1.000; ficaram coerentes com 7.407.000 sem alteracao. |

"""
    s+="### Prova (rodada 3)\n\n- Diff base x DRAFT (todas as abas, openpyxl so leitura) e a rodada 3 isolada (r2 x r3): so as celulas listadas acima mudaram nesta rodada; todas FFDDEBF7 (`nonblue` vazio); nenhuma entrada de drawings/media/comments mudou.\n- `validate_workbook.py`: PASS (blocker=0) em todos.\n"
    if cl=='NE/CHANGELOG.md': s+="- Amostra `Sample File` A55:A161 validada contra `NominaIndividualElectronicaXSDV1.0.6.xsd`: VALIDA (nao tocada nesta rodada). Nomes `Reemplazar`/`Eliminar` conferidos em `NominaIndividualDeAjusteElectronicaXSDV1.0.6.xsd`.\n"
    if cl=='FORMS/CHANGELOG.md': s+="- Contas: 12 x 617.232 = 7.406.784; aproximado ao mil = 7.407.000; 33.888.000 / 7.407.000 = 4,575 (\"4.58\"); 7.407.000 / 169.440.000 = 4,371% (\"4.37%\").\n"
    t=open(cl,encoding='utf-8').read(); assert 'Rodada 3 (2026-10-29)' not in t
    open(cl,'w',encoding='utf-8').write(t.rstrip('\n')+s)
print('ok')
for f in glob.glob('*/*DRAFT*.xlsx'): print(md5(f),f.split('\\')[-1][:60])
