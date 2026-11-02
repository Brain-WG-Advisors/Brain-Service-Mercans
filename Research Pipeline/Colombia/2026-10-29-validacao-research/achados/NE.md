# NE — Verificação da spec CO-DIAN-001 (Nómina Electrónica) contra XSD 1.0.6 e Anexo Técnico V1.0

Data: 2026-10-29. Item testado: `co-report-crosscheck/05-final/CO-DIAN-001-NominaElectronica-Spec.xlsx` (somente leitura). Base de teste: Caja de Herramientas NE V1.0 (XSD 1.0.6, Anexo Técnico V1.0, Res. DIAN 000013/2021 impressa no Anexo; instrumento vigente Res. 000227/2025). Itens de lei fora do Anexo/XSD (Ley 2466/2025 etc.) NÃO foram verificados em fonte primária nesta rodada: ficam como LACUNA com confiança baixa.

## 1. Contagens e resultado XSD

| Medida | Valor |
|---|---|
| Linhas comparadas (aba Nomina Electronica Spec) | 197 (195 códigos NIE, +SchemaLocation, +TipoNota); NIE001 ocupa 2 linhas |
| Cobertura caminho XSD ↔ spec | 166 atributos + elementos-folha do XSD: 100% presentes na spec; 0 caminhos da spec fora do XSD (exceto `ds:Signature`, esperado). 195/195 códigos NIE do Anexo presentes, 0 faltando, 0 sobrando |
| Nome, caminho, ordem de sequência (aba File Structure), tipo, obrigatoriedade vs XSD/Anexo | OK em todas as linhas, salvo os itens abaixo |
| OK (por linha) | ~171 |
| DEFEITO (linhas de campo) | 13, mais 6 defeitos de nível de aba/amostra (12 itens NE-01..NE-12) |
| LACUNA | 13 linhas (8 itens NE-13..NE-20) |
| Tabelas de códigos (5.1.1, 5.1.2, 5.2.1, 5.3.3.1, 5.5.1–5.5.8, 16 TipoTrabajador, 2 SubTipo, 7 HE) | Valores idênticos ao Anexo; únicas divergências: NE-09, NE-17, NE-18 |
| Validação XSD do Sample File, como está na aba | **FALHA** (1 erro: raiz `NominaIndividual` sem namespace, "No matching global declaration"); também sem `SchemaLocation` (obrigatório) e `UBLExtensions` sem o prefixo `ext:` |
| Validação XSD após correção mecânica (xmlns, `ext:`, `SchemaLocation=""`) | **VÁLIDO** (lxml/libxml2 contra XSD 1.0.6; imports de `../common` apontados para `Schemes\`) |
| Aritmética dos totais (amostra residente) | OK: 480.000+480.000+60.000+60.000+617.000 = 1.697.000; 12.000.000 − 1.697.000 = 10.303.000. Variante não-residente: 3.480.000 e 8.520.000 OK. Redondeo ausente coerente. Retenção refeita: 8.190.000/52.374 = 156,3753 UVT → 11,7851 UVT → 617.232 → 617.000 OK |
| NIT/DV da amostra | Empleador 900123456-8 e Proveedor 901234567-7 conferem (módulo 11) |

Notas sem defeito: campos C na spec com `1-1` no Anexo (NIE149/150, 171–176, 204) estão dentro de pai opcional (0-N), logo C está correto. Os typos do Anexo (`OtroConceptos`, `FechaFIn`, "numeral 8.4.1" para TiempoLaborado) a spec corrigiu seguindo o XSD e a seção 8.3.1. O Anexo não traz enumerações no XSD (nenhuma `xsd:enumeration`); códigos vêm só das tabelas do Anexo. Não foi usado o CUNE de exemplo oficial como teste.

Arquivos de trabalho: `achados/ne-work/` (sample_asis.xml, sample_fixed.xml, xsd_flat.txt, anexo.txt, scripts).

## 2. Itens não-OK

| ID | Artefato | Local | Como está | O que pode mudar | Fonte primária | Classe | Grav. | Conf. |
|---|---|---|---|---|---|---|---|---|
| NE-01 | Spec | Sample File!A56–A161 | Amostra sem `xmlns`, sem `SchemaLocation`, `UBLExtensions` sem prefixo `ext:`; a aba diz "validar na habilitação". | Trazer `xmlns="dian:gov:co:facturaelectronica:NominaIndividual"`, `xmlns:ext`, `SchemaLocation=""`, `ext:UBLExtensions`. | XSD 1.0.6: `targetNamespace`, `elementFormDefault=qualified`, `SchemaLocation use=required`; Anexo regra NIE901 (R) "debe poseer todos los Namespace"; validação lxml reproduzida | DEFEITO | S2 | 99 |
| NE-02 | Spec | Sample File!A71; Example Analysis!C27 | TiempoLaborado="1850.00" (5a+1m+20d). | 11/01/2021→31/03/2026 = 5a+2m+20d = 1880.00 (1881 se inclusivo); 1850 não bate. (Contagem civil 1905 está certa.) | Anexo §8.3.1 "(5*360)+(3*30)+18 = 1908.00" (convenção 360/30) | DEFEITO | S3 | 93 |
| NE-03 | Spec | Spec!M85 (NIE069); Population Rules!C9 | DiasTrabajados conta dias de férias, incapacidade e licença remunerada (não subtrai), mas SueldoTrabajado exclui férias (NIE070). Inconsistente: dias ≠ valor. | Alinhar ao texto do Anexo: dias efetivamente trabalhados (pagos no Basico); ausências em blocos próprios. Confirmar com DIAN/habilitação. | Anexo NIE069: "días que el trabajador efectivamente estuvo ejecutando sus labores"; NIE125/130: "días inactivo por incapacidad/licencia" | DEFEITO | S2 | 70 |
| NE-04 | Spec | Spec!Q211; Population Rules!C17 | Diz que Redondeo (NIE186) pode ser negativo. | Anexo exige todos os valores monetários positivos (regra VLR01, R). Remover "Negative=Y" ou explicar como a diferença negativa é informada. | Anexo §1.1.3.1 "Todos los valores monetarios deberán ser expresados en valores positivos"; VLR01 (R) | DEFEITO | S3 | 80 |
| NE-05 | Spec | File Structure!B20–B123 | Árvore (dita "formato real do fio", B3) usa rótulos em inglês como nome de elemento: Employer, Employee, Payment, Period, Deductions, Change event, Rounding, Severance savings, Replace/Delete; B96 repete @PorcentajeSub @DeduccionSub. | Usar Empleador, Trabajador, Pago, Periodo, Deducciones, Novedad, Redondeo, Cesantias, Reemplazar, Eliminar. | XSD 1.0.6 nomes dos elementos; Anexo §7 (Reemplazar/Eliminar) | DEFEITO | S3 | 92 |
| NE-06 | Spec | Spec!M22–M24; Population Rules!C5; File Structure!B127 | Prefixo "atribuído pela DIAN", "faixa autorizada", padrão `^[A-Z]{1,4}$` / `^[A-Z]{1,4}[0-9]+$`. | Anexo diz que prefixo e consecutivo são "elegido por el Emisor"; não há padrão nem faixa. Marcar padrão como convenção Mercans ou retirar. Conferir Res. 227 art. 1.5.3.3.1 item 3 ("prefixo autorizado"). | Anexo NIE010 "Prefijo elegido por el Emisor"; NIE011 "consecutivo elegido por el Emisor"; NIE012 "no espacios o guiones" | DEFEITO | S3 | 70 |
| NE-07 | Spec | Sample File!A95–A96,A99,A91; Example Analysis!A44 | CUNE, HoraGen (10:53:10-05:00) e QR da amostra são os do exemplo do Anexo (NitNE 700085371, totais 3.500.000/1.000.000/2.500.000, N00001), não derivados dos dados da amostra (NE1042, 12.000.000...). | Marcar CUNE/QR como placeholder, ou calcular com PIN fictício. | Anexo §8.1.1.3 (composição "N000012020-01-161053:10-05:00...") | DEFEITO | S3 | 88 |
| NE-08 | Spec | Sample File!A55–A161 | XML indentado com quebras entre tags; nada avisa para minificar. | Avisar que o envio não pode ter caracteres de edição entre tags (e que ZB04 exige os prefixos do XSD). | Anexo §6.2.2 ZB02 (R) "No es permitida la presencia de caracteres de edición ... entre los tags"; ZB04 | DEFEITO | S4 | 70 |
| NE-09 | Spec | Field Options!A88; Spec!I72,J72 | Medio de pago: "catálogo 1 a 97"; Metodo "N, comprimento 2". | Anexo lista também 98 (CATS: Nequi, Daviplata) e ZZZ; XSD tipa Metodo como string. Incluir 98 (realista para folha) e ZZZ; relaxar comprimento/tipo. | Anexo tabela 5.3.3.2 (códigos 98 e ZZZ); XSD `Pago/@Metodo xsd:string`; NIE065 "A N 2" (Anexo inconsistente) | DEFEITO | S4 | 85 |
| NE-10 | Spec | File Structure!B7; Sample File!A33 | 500 KB descrito como limite do payload (ZIP/base64). | Anexo regra ZA01 fala do tamanho do arquivo XML. | Anexo §6.2.1 ZA01 "tamaño del archivo XML superior a 500 KB" | DEFEITO | S4 | 70 |
| NE-11 | Spec | Spec!J93,J98,J103,J108,J113,J118,J123 | Cantidad das 7 horas extras: "N (integer hours)". | XSD aceita decimal; horas fracionadas seriam válidas. Trocar para "N (decimal)" ou justificar a restrição como regra Mercans. | XSD `HED/@Cantidad xsd:decimal` (idem HEN...HRNDF); Anexo NIE076 "A N" sem tamanho | DEFEITO | S4 | 85 |
| NE-12 | Spec | Example Analysis!D44; Spec!M12 | "Todos os inputs do CUNE com 2 decimais TRUNCADOS" ok, mas a amostra mostra "Numero NE1042" como prefixo de 2 letras "positions 1-2" enquanto o padrão aceita 1–4 letras. | Reescrever como "prefixo + consecutivo, sem tamanho fixo". | Anexo §8.1.1.1 (NumNE = prefijo concatenado con consecutivo) | DEFEITO | S4 | 75 |
| NE-13 | Spec | File Structure!B21; Spec!F4 | UBLExtensions 1-1 (Anexo) mas XSD tem `minOccurs=0`; exemplo oficial com UBLExtensions vazio reprova no XSD ("Missing child UBLExtension"). | Registrar divergência Anexo×XSD; assinatura é obrigatória na prática. | XSD `ext:UBLExtensions minOccurs=0`; Anexo NIE001 "1-1" | LACUNA | S4 | 85 |
| NE-14 | Spec | Spec!I62,J62 (NIE050) | LugarTrabajoPais comprimento 3, formato "N / A"; a amostra usa "CO". | Anexo se contradiz (Tam 3 vs "Codigo alfa-2 de la tabla 5.4.1"). Confirmar em habilitação. | Anexo NIE050 "A N 3 ... Codigo alfa-2" | LACUNA | S4 | 80 |
| NE-15 | Spec | Spec!M78 (NIE002) | FechaIngreso tratada como data constante do vínculo. | Anexo diz para preencher "solamente en el registro del mes en que ... presenta ingreso", mas ocorrência 1-1. Ambiguidade a confirmar com DIAN; prática (constante) é compatível com o XSD. | Anexo NIE002 Descripción vs Oc 1-1 | LACUNA | S4 | 60 |
| NE-16 | Field Options | A57–A65 (HED..HRNDF %) | Mantém 25/75/35/100/75/150/110 (valores do Anexo) e já avisa que a sobretaxa dominical subiu. Hoje (29/10/2026) o recargo dominical estaria em 90% desde 01/07/2026 (80% desde 01/07/2025): % legal ≠ tabela 5.5.5 do Anexo. A nota atribui o aumento à Ley 2101/2021 além da Ley 2466/2025 (não verificado: Ley 2101 trata de jornada). | Manter valores do Anexo como padrão, decidir com DIAN qual % o validador aceita; corrigir a atribuição legal. Itens 4–7 (e HEN se aplicável). | Anexo tabela 5.5.5 (Anexo V1.0 não reeditado); lei: Ley 2466/2025 art. 14 (não lido nesta rodada) | LACUNA | S2 | 60 |
| NE-17 | Field Options | D60; Spec!M92; Population Rules!C15,D15 | Janela noturna 21:00–06:00 "conforme Ley 2101/2021". | Ley 2466/2025 art. 10 teria antecipado o início da noite para 19:00 (a confirmar); o bloco HRN e a divisão de blocos mudariam. Anexo nada diz sobre a janela. | Anexo silencioso; lei não verificada nesta rodada | LACUNA | S3 | 55 |
| NE-18 | Field Options | A66–A69 | Tipo de incapacidade 2 = doença profissional, 3 = acidente de trabalho. | Anexo só dá rótulos "Profesional" e "Laboral" sem definição; a leitura é interpretação. | Anexo tabela 5.5.6; NIE126 "tipo de incapacidad" | LACUNA | S4 | 65 |
| NE-19 | Spec | Population Rules!D5 | "Documento rejeitado consome o número; reenviar com novo consecutivo." | Regra 90 fala em "documento procesado anteriormente"; não diz que rejeitado consome o número. Reformular como cautela. | Anexo regra 90 (R) | LACUNA | S4 | 50 |
| NE-20 | Spec | Spec!K7,M7; Anexo×XSD | SchemaLocation="" e xsi:schemaLocation citados como "do anexo". | O XSD exige só `SchemaLocation`; `xsi:schemaLocation` é opcional e vem do exemplo oficial. | XSD `@SchemaLocation use=required`; exemplo oficial V1.0.2 | LACUNA | S4 | 75 |

NE-12 e NE-20 são menores; NE-12 não é falha de campo, só de redação.

## 3. Cinco mais graves
1. NE-01: amostra falha no XSD (namespace/SchemaLocation/ext).
2. NE-03: DiasTrabajados conta dias não trabalhados, contradizendo o Anexo e NIE070.
3. NE-16: percentuais de HE/recargo dominical divergem da lei vigente (Anexo desatualizado).
4. NE-02, NE-04, NE-05, NE-06, NE-07: S3 (TiempoLaborado errado, Redondeo negativo vs VLR01, árvore com nomes em inglês, prefixo "da DIAN", CUNE copiado do Anexo).
5. NE-17: janela noturna possivelmente defasada.

## Bloco de prova
- Pedido → resposta: (1) contagens e XSD acima; (2) tabela NE-01..NE-20; (3) validação XSD feita; (4) aritmética e listas de códigos conferidas.
- Fontes: XSD 1.0.6 lido por inteiro; Anexo V1.0 (PDF 269 p., extraído com pymupdf), tabelas 5.1–5.5, §1.1.1, §1.1.3, §6, §8.1–8.3, §9.7.2.
- Teste: lxml XMLSchema; comparação mecânica de caminhos/obrigatoriedade/tipo (166 folhas XSD, 195 NIE).
- Confiança: 90% nos itens de XSD/Anexo; itens de lei (NE-16, NE-17) não verificados em fonte primária.
