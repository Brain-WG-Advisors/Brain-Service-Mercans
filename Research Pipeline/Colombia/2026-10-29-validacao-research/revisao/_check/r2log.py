import json,sys,hashlib,glob
sys.stdout.reconfigure(encoding='utf-8')
meta={
 ('PILA','P003'):{
  ('Report Matrix','A36'):('A-16','Ley 100 art. 15 num. 2 (mod. Ley 797 art. 3), texto lido em raw/docs/oficiais/CO (Ley-100-1993-FuncionPublica.html; Ley-797-2003-SecretariaSenado.html); AT2 v30 §2.1.2.3.3 campo 7','DECISOES-RODADA2 item 1'),
  ('PILA Spec','M69'):('A-16','idem','item 1'),('Population Rules','C22'):('A-16','idem','item 1'),
  ('Payroll Scope Summary','C46'):('A-16 (consequencia)','AT2 v30 §2.1.2.3.3 ("no deben diligenciar" os campos de pensao); retirada a palavra "waived"','item 1'),
  ('PILA Spec','M120'):('P-02','AT2 v30 p.157-158 (§2.1.2.3.18 e .19): a regra ACCAI se repete no campo 52; tabela da Ley 2381 art. 20 condicionada a vigencia (CCG: nao em vigor em 2026; Sentencia C-264/2026, vigencia 1-abr-2027)','item 2'),
  ('PILA Spec','G120'):('P-02 (consequencia)','idem','item 2'),
  ('PILA Spec','L107'):('DD-07 / S3','DD v1.4 Country Fields l.112 "PILA Salary Type" (X/F/V)','item 12'),
  ('PILA Spec','L152'):('DD-11 / S3','DD v1.4 Country Fields l.113 "PILA Special Pension Rate Indicator" (0-4)','item 12'),
  ('PILA Spec','J47'):('S4','AT2 v30 §2.1.1.1 campo 9 (branco quando nao se aplica); coerente com G47/K47','item 14')},
 ('PILA','P007'):{('PILA Pensioners Spec','M104'):('P-02 (mesma condicao)','AT3 v15 campo 46; Ley 2381 art. 20 condicionada a vigencia','item 2')},
 ('NE','NE'):{k:('NE-05','XSD 1.0.6 (NominaIndividualElectronicaXSDV1.0.6.xsd): elementos Novedad, Periodo, Empleador, Trabajador, Pago, Cesantias, Deducciones, Redondeo','item 4') for k in [('File Structure',x) for x in ['B23','B24','B39','B43','B51','B69','B92','B112']]},
 ('FORMS','D002'):{('Example Analysis','C15'):('SIM-03','DUR 1625/2016 art. 1.6.1.11.11 (aproximacao so em formularios de declaracoes e recibos de pago), lido em raw/docs/oficiais/CO','item 5'),
  ('Example Analysis','D15'):('SIM-03','idem; NE v1.1 carrega 617.232,00','item 5'),('Formulario 350 Spec','K20'):('S4','M20 mantem a explicacao (Oficio 15662/2026)','item 14')},
 ('FORMS','D004'):{k:('SIM-03','12 x 617.232 = 7.406.784; DUR 1.6.1.11.11 nao se aplica ao certificado','item 5') for k in [('Formulario 220 Spec','K52'),('Formulario 220 Spec','K63'),('Example Analysis','A27'),('Example Analysis','C27'),('Example Analysis','A30'),('Example Analysis','A36'),('Example Analysis','D33'),('Sample File','A79'),('Sample File','A90')]},
 ('FORMS','D005'):{k:('SIM-03','12 x 617.232 = 7.406.784; 7.406.784/169.440.000 = 4,37%','item 5') for k in [('Formato 2276 Spec','K37'),('Example Analysis','A27'),('Example Analysis','D33'),('Sample File','A77')]},
}
def cl(v):
    if v is None: return '(vazio)'
    return str(v).replace('|','\|').replace('\n',' ')
out={}
for (grp,k),m in meta.items():
    a=json.load(open(f'_check/{k}.json',encoding='utf-8')); b=json.load(open(f'_check/{k}_r2.json',encoding='utf-8'))
    A={(c['sheet'],c['cell']):c['new'] for c in a['cells']}
    rows=[]
    for c in b['cells']:
        key=(c['sheet'],c['cell'])
        if key in A and A[key]==c['new']: continue
        before=A[key] if key in A else c['old']
        i,src,dec=m[key]
        rows.append(f"| {i} | {c['sheet']}!{c['cell']} | {cl(before)} | {cl(c['new'])} | {src} ({dec}) | APLICADA |")
    out[k]=rows
json.dump(out,open('_check/r2rows.json','w',encoding='utf-8'),ensure_ascii=False)
for k,v in out.items(): print(k,len(v))
