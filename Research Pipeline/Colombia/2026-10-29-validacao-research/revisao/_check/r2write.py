import json,hashlib,glob,sys
sys.stdout.reconfigure(encoding='utf-8')
R=json.load(open('_check/r2rows.json',encoding='utf-8'))
def md5(p): return hashlib.md5(open(p,'rb').read()).hexdigest()
H="| ID | Onde | Antes (verbatim; para celula ja alterada na rodada 1 = texto do DRAFT da rodada 1, senao = base) | Depois (verbatim) | Fonte | Status |\n|---|---|---|---|---|---|\n"
def sect(title,files,body):
    s="\n\n## Rodada 2 (2026-10-29): "+title+"\n\n"
    s+="Decisoes: `revisao/DECISOES-RODADA2.md`; problemas: `revisao/CONFERENCIA-DRAFTS.md`. Edicao por cirurgia no XML (celulas trocadas em inlineStr, estilo clonado com FFDDEBF7, demais entradas do zip byte a byte).\n\n| Arquivo | md5 DRAFT apos a rodada 2 |\n|---|---|\n"
    for f in files: s+=f"| {f.split('/')[-1]} | {md5(f)} |\n"
    return s+"\n"+body
g=lambda p: glob.glob(p)[0]
pila=sect("CO-PILA-003 e CO-PILA-007",[g('PILA/CO-PILA-003*.xlsx'),g('PILA/CO-PILA-007*.xlsx')],
"### CO-PILA-003 (+6 celulas novas e 3 reescritas; total base x DRAFT = 61 celulas)\n\n"+H+"\n".join(R['P003'])+
"\n\n### CO-PILA-007 (+1 celula; total = 7)\n\n"+H+"\n".join(R['P007'])+
"""

### Nao aplicadas na rodada 2

| Item | Motivo |
|---|---|
| 007 M98 (Ley 2381, distribuicao pelo operador) | O texto descreve o que o operador de informacao faz segundo o AT3 v15 (a partir de jul/2025); nao aplica a tabela da Ley 2381 nem calcula valor. Condicionar a vigencia seria afirmar o contrario do anexo. Mantido. |
| 003 Field Options!D169 / D171, Population Rules!C21 (Decreto 1072 art. 2.2.4.x) | Sao artigos de riscos laborais, outro artigo; o item 1 trata so de art. 2.2.1.2.1.4. |

### Prova (rodada 2)

- Diff base x DRAFT (openpyxl so leitura, todas as abas): 003 = 61 celulas, 007 = 7; = 55+6 e 6+1 da rodada 1 mais esta secao; todas azul FFDDEBF7, nenhuma fora do log. Entradas do zip alteradas: so `styles.xml` e as planilhas editadas.
- Amostra PILA: segmentos 003 17/17 e 007 18/18 com o comprimento exato (`pilalen.py`); a rodada 2 nao tocou no Sample File.
- `validate_workbook.py`: PASS (blocker=0) nos dois.
- Texto de Ley 100 art. 15 num. 2 e Ley 797 art. 3 relido em `raw/docs/oficiais/CO`; AT2 v30 pp.157-158 relido (campos 51 e 52 trazem a regra ACCAI).
""")
ne=sect("CO-DIAN-001",[g('NE/*.xlsx')],
"### Aplicadas (NE-05; total base x DRAFT = 71 celulas)\n\n"+H+"\n".join(R['NE'])+
"""

B92 (Deductions para Deducciones) e B112 (Rounding para Redondeo) entram em "etc." da linha NE-05 (mesma arvore, nomes do XSD); B3 afirma que a arvore e o formato real de envio.

### Nao aplicadas na rodada 2

| Item | Motivo |
|---|---|
| Tipo 75 na NE (item 11) | O Anexo da NE nao traz regra para o tipo 75 (a tabela TipoTrabajador da propria spec, Field Options, nao o contem). Sem sustentacao no Anexo, a nota "PILA-only contributor type" nao foi acrescentada. Lacuna: o DD (mapper Worker Type) ainda mistura o 75 com a tabela da NE; decidir de-para ou campo so-PILA. |
| SIM-03 / D15 | Na NE ja estava aplicado na rodada 1 (617.232,00, C39/C40/C43 e P191). Nada a alterar. |

### Prova (rodada 2)

- Amostra `Sample File` A55:A161 reconstruida (`_check/ne_draft.xml`) validada contra `NominaIndividualElectronicaXSDV1.0.6.xsd`: **VALIDA** apos a rodada 2 (a rodada nao tocou no Sample File; XML identico ao anterior).
- Diff base x DRAFT: 71 celulas (63 + 8), todas azul FFDDEBF7. `validate_workbook.py`: PASS.
""")
forms=sect("FORMS (CO-DIAN-002, 004, 005; CO-CESANTIAS-006 sem alteracao)",[g('FORMS/CO-DIAN-002*.xlsx'),g('FORMS/CO-DIAN-004*.xlsx'),g('FORMS/CO-DIAN-005*.xlsx'),g('FORMS/CO-CESANTIAS-006*.xlsx')],
"### CO-DIAN-002 (total base x DRAFT = 17 celulas)\n\n"+H+"\n".join(R['D002'])+
"\n\n### CO-DIAN-004 (total = 29)\n\n"+H+"\n".join(R['D004'])+
"\n\n### CO-DIAN-005 (total = 61)\n\n"+H+"\n".join(R['D005'])+
"""

### Contas refeitas (rodada 2)

- Retencao mensal sem aproximar: (8.190.000 - 7.856.100) x 0,28 + 523.740 = 617.232 (= 11,785 UVT x 52.374 = 617.232,09; valor da NE).
- Anual: 12 x 617.232 = **7.406.784**. 33.888.000 / 7.406.784 = 4,575 (texto "4.58" mantido); 7.406.784 / 169.440.000 = 4,371% (texto "4.37%" mantido); 20% de 169.440.000 = 33.888.000.
- Formulario 350 (declaracao): casilla 93 = 617.000 apos aproximar ao mil (DUR 1.6.1.11.11); o certificado 220 e o Formato 2276 nao sao declaracoes nem recibos de pago, entao levam o valor sem aproximar.

### Nao aplicadas na rodada 2

| Item | Motivo |
|---|---|
| 006 (nenhuma mudanca de spec) | A inconsistencia da 006 L10 x DD W99 e corrigida no DD (W99), nao na 006 v1.1. |
| 004/005: F-03 (retencao da prima), F-05, F-08, F-09 | Nao estavam na lista de decisoes da rodada 2. |
| 002 K23, K58, K59, K61, K64, A120 e Sample (617.000) | Sao do Form. 350, que aproxima ao mil (DUR 1.6.1.11.11): corretos. |

### Prova (rodada 2)

- Diff base x DRAFT por celula: 002 = 17, 004 = 29, 005 = 61, 006 = 10 (inalterado); todas azul FFDDEBF7 (K20 da 002 fica vazia, com o fundo); nenhuma fora do log. Linhas do Sample File 004 A79/A90 e 005 A77 mantem a largura (mesmo numero de caracteres).
- `validate_workbook.py`: PASS nos quatro.
""")
for f,s in (('PILA/CHANGELOG.md',pila),('NE/CHANGELOG.md',ne),('FORMS/CHANGELOG.md',forms)):
    t=open(f,encoding='utf-8').read()
    assert 'Rodada 2 (2026-10-29)' not in t
    open(f,'w',encoding='utf-8').write(t.rstrip('\n')+s)
print('ok')
