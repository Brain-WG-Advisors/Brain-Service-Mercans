# Lote 1 da auditoria (22/10/2026) - regras erradas em artefatos entregues

Origem: `co-report-crosscheck/04-output/AUDIT-SUMMARY-2026-10-22.md` (auditorias A/B/C de 22/10), itens graves conferidos pessoalmente.

| Artefato | O que mudou | Fonte |
|---|---|---|
| CO-DIAN-001 C41, -002 C40, -004 C40, -005 C41, CO-CESANTIAS-006 C43 | PILA: tipo N (C >= A, sem devolução); atraso no tipo E; tipo M só antes do período de saúde março/2014 | AT2 v30 §2.1.1.2.2 campo 8; Disposiciones comunes a la Planilla N (texto alinhado à CO-PILA-003 C41/C49) |
| Os mesmos 5 + CO-PILA-003 C12; CO-PILA-003 Field Options D99 | Aprendizes: tipo 19 = "lectiva Ley 2466" a partir de ago/2025 (12 só antes); antes de ago/2025 o 19 era a fase produtiva; depois, o anexo não nomeia código para a fase produtiva | AT2 v30 §2.1.2.3.1 campo 5, tipos 12 e 19 |
| CO-DIAN-005 M32 / M33 | Numeral 25 = WT 25819 (como o 220 casilla 55); numeral 26 = WTs FVOL 25811-25815, 25823 (+21141), planos institucionais só pelo valor descontado do empregado (como o 220 casilla 56) | ET arts. 55 e 126-1; DUR 1625 arts. 1.2.1.12.9 e 1.2.1.22.41; resposta do BAU de 21/10 (Q11) |
| DD v1.3 (de v1.2) | Country Fields W80; Country Option Mappers F221, F60, F65, F66; Version Control linha 16 | idem acima |
| WTC v1.6 (de v1.5) | Linhas 156 e 324 (férias pagas em dinheiro): Q saúde, R FSP, S ARL, U pensão = No; T parafiscais = Yes; Version Control linha 18 | CE Sec. 4ª exp. 26941/2024; SU 25185/2021 regra 1; Ley 21/1982 art. 17; Ley 89/1988 art. 1 par. 1 |
| CCG v1.4 (de v1.3) | Módulo 5, tabela de novidades PILA: VAC/LR (IBC do mês anterior, sem ARL, férias na base CCF/SENA/ICBF) e IGE (valor da incapacidade como IBC, sem ARL); versão na capa, rodapé e Version Control | Decreto 780 arts. 3.2.1.10 e 3.2.5.1; Decreto 1072 art. 2.2.4.2.1.6 nums. 1.2 e 1.3 |

Conferência:
- Verificador independente: `LOTE1-verification.json` = PASS_WITH_MINOR_FIX; as 7 correções exigidas aplicadas com o texto exato (+ CO-PILA-003 C12/D99, mesma frase).
- make_final nas 6 specs: PASS (diff só nas células do mapa, 0 fórmulas, 0 tokens, 0 palavras de processo). Anteriores em `05-final/_previous/`.
- DD e WTC: diff célula a célula contra a versão anterior = só as células previstas + linha do Version Control; só sheet XML e sharedStrings mudaram.
- CCG: diff de parágrafos = só as 2 células da tabela, versão e linha 1.4; document.xml bem formado.

Pendente: Drive (com ok do usuário). Observações não bloqueantes do verificador: WTC F390 ("vacation INCLUDED" sem separar gozadas e em dinheiro) e falta do destaque azul nas células mudadas do WTC.

## 23/10 - adiantamento mensal das cesantías fora da spec (decisão do usuário: opção b)
Motivo: o decreto que regulamenta a Ley 2466 de 2025 art. 64 par. 1 ainda é minuta e o PILA AT2 v30 não tem tipo de cotização de cesantías (`co-report-crosscheck/04-output/RA-AUDIT2-RESEARCH-2026-10-23.md` Q2). O CCG v1.4 continua descrevendo a lei (sem citar campo de spec) e não muda.

| Arquivo | O que mudou |
|---|---|
| CO-CESANTIAS-006 (`05-final`) | Removidas as linhas 38-43 da Spec (cabeçalho + MA01-MA05), Report Matrix linha 43, Payroll Scope Summary linha 52, File Structure linhas 63-66; texto ajustado em Scope Summary C26 e C35, Spec M30 e M47, Population Rules C7 (passo g), Example Analysis D32 (limpo). Mapas: `04-output/final-prep/CO-CESANTIAS-006-remove-MA-map.json` e `-remove-MA2-map.json`; script `scripts/remove_block.py` |
| DD v1.3 | Country Fields I60 e W60, Country Option Mappers G151 (referências a MA01-MA05), Version Control D16 (frase acrescentada). Mapa `remove_MA_dd.json` |
| WTC v1.6 | Wage Type Catalogue Y387, Form Reference Guide E21, Version Control D18 (frase acrescentada). Mapa `remove_MA_wtc.json` |

Conferência: spec com diff célula a célula ajustado ao deslocamento das linhas = só as células do mapa; mesclagens deslocadas; 0 fórmulas, 0 tokens, 0 palavras de processo, 0 referências a MA0x/"monthly advance". DD e WTC: diff = só as células acima, estilos iguais, só o XML das abas mexidas. Anteriores em `_previous/`.
md5: DD v1.3 d4cdc3d42322…, WTC v1.6 f6378ece7689… (as md5 de 22/10 acima ficam como histórico).
Juros mensais (IN03, par. 2): com ok do usuário, Spec M41 (antiga M47) e Population Rules C20 sem a condição de "manter desligado" e sem o prazo da minuta; par. 2 relido na fonte (Ley 50 de 1990 art. 99 par. 2, texto compilado da Función Pública, `raw/docs/oficiais/CO/2026-10-22-Ley-50-1990-FuncionPublica.pdf`): só exige acordo escrito. Mapa `04-output/final-prep/CO-CESANTIAS-006-in03-map.json`, make_final PASS. md5 final da CO-CESANTIAS-006: 93b389077889…

## 26/10 - decisões #56 e #57 (o usuário pediu decidir pelas fontes oficiais) e subida ao Drive
Fontes: UGPP, ABC Empleadores 2025, p. 5 (`raw/docs/oficiais/CO/2026-10-22-UGPP-ABC-Empleadores-2025.pdf`): total remunerado = pagos salariales + pagos NO salariales pactados + licencias remuneradas (sem indemnizaciones, licencias no remuneradas, incapacidades, prestaciones sociales); CE SU 25185/2021 regra 3 (o limite de 40% é do pacto de desalarização); Decreto 780 de 2016 art. 3.2.5.1 (cotizaciones durante vacaciones "se causarán en su totalidad" sobre o último IBC reportado); CST art. 128 (primas extralegais de férias pactáveis como não salariais).

| Arquivo | O que mudou |
|---|---|
| WTC v1.6 | V1 e F395: denominador dos 40% citado na UGPP 2025 (o SU 25185 fica só para o numerador); F390: "vacation INCLUDED" → férias em dinheiro EXCLUDED, férias gozadas sobre o último IBC (Decreto 780 art. 3.2.5.1); linha 317 alinhada à 316 (V Non-Salary - pacted; Q/R/S/U Yes/No; T No; W No); VC D18 (frase acrescentada). Flags Q/R/U = Yes das linhas 154/155/323 mantidas (contribuição devida nos dias de férias). Mapa `decisao56_57_wtc.json` |
| DD v1.3 | Country Fields W37 (fonte do denominador); VC D16 (frase). Mapa `decisao57_dd.json` |
| CCG v1.4 | S23 (Módulo 4, "Scope of the 40% clamp"): a frase da guia UGPP 2021 (todos os não salariais) trocada pela regra de 2025; linha 1.4 do Version Control (frase). Script `ccg_decisao57.py` |
| Specs | CO-DIAN-001 M89, M161; CO-PILA-003 A25, C25, M108, C19 (mapas `co-report-crosscheck/04-output/final-prep/*-den40-map.json`, make_final PASS) |

Conferência: diff célula a célula do WTC e do DD contra `_previous/` = só as células acima; XML do CCG válido; make_final PASS nas 2 specs.
md5: WTC v1.6 05b839bbf8af…, DD v1.3 f5a14676f2db…, CCG v1.4 8b087e4d008c… (as anteriores ficam como histórico).
Drive (26/10): WTC → Google Sheet novo `03 - WTC/CO-WTC-001_v1.6` (14/14 abas iguais ao local, junto com o DD); DD → `02- DD/CO-DD-001_v1.3`; CCG → Google Doc novo `05 - Payroll Regulation Guide/CO-CCG-001_v1.4` (export txt conferido); anteriores em `Archived`; xlsx/docx de origem removidos; Monday atualizado (DD, WTC, CCG).

| Data | Frente | O quê |
|---|---|---|
| 2026-10-22 | geral (Colômbia) | Lote 1 construído, verificado e aplicado localmente |
| 2026-10-23 | geral (Colômbia) | Adiantamento mensal das cesantías retirado da CO-CESANTIAS-006; referências no DD v1.3 e WTC v1.6 ajustadas |
| 2026-10-23 | geral (Colômbia) | Juros mensais (IN03) sem a condição da minuta: Spec M41 e Population Rules C20 |
| 2026-10-26 | geral (Colômbia) | Decisões #56/#57 aplicadas (WTC, DD, CCG, CO-DIAN-001, CO-PILA-003); WTC v1.6, DD v1.3 e CCG v1.4 no Drive como versões novas; Monday atualizado |
