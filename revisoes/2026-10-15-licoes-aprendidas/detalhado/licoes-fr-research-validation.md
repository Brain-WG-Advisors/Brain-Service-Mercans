# Lições aprendidas — validação da research da França (fr-research-validation)

Fonte minerada (somente leitura): `C:\Users\instituto\Documents\fr-research-validation` (raiz do repositório git; o projeto fica na subpasta `fr-research-validation\`, abreviada abaixo como `FRV\`), a memória do Claude em `C:\Users\instituto\.claude\projects\c--Users-instituto-Documents-fr-research-validation\memory\` e as 6 transcrições `*.jsonl` da mesma pasta (só as mensagens do usuário e as respostas de plano/resultado foram extraídas).
Nada na fonte foi alterado. Os valores citados vêm dos arquivos indicados; quando um número vem só da transcrição, isso está dito.

---

## 1. Inventário

### 1.1 O que é o projeto
- **Objetivo declarado** (`FRV\HANDOFF.md`, "Goal"): validar a research da França (FR-CCG-001 v1.0 e os artefatos derivados) contra um **motor oficial, gratuito e independente**, com métodos de teste de desenvolvedor, medindo a acurácia contra a meta de **95 %**. Pedido original, nas palavras do usuário: "Realizar validação da research através de um third-party payroll software".
- **"Third-party software" escolhido:** o motor `modele-social` **v11.1.0** (o motor aberto por trás do mon-entreprise.urssaf.fr). O TESE da URSSAF foi rejeitado porque não tem modo de teste (tudo o que entra é declaração real). Softwares comerciais (Silae, Sage, Cegid, PayFit, ADP) ficaram como reserva.
- **Validador de formato:** o **DSN-Val** (DSN-VAL 2.8.0, plugin de norma P26V01) para a família DSN (FR-DSN-001/002/003 e os blocos PAS, DOETH e solde TA).
- **Artefatos validados:** FR-CCG-001 v1.0, FR-WTC-001 v1.0, FR-DD-001 v1.1, Payslip Generator, FR-SIR-INDEX-001 v1.0, as 15 report specs, o design técnico (Regulation Design, Taxability Matrices, Research Memo) e a skill `payroll-compliance-france`.

### 1.2 Método (resumo; detalhe na seção 4)
1. **Oráculo:** reimplementação em Python da research (`FRV\oracle\oracle.py`), alimentada por uma fonte única de parâmetros (`FRV\suite\params.json`) e de regras (`FRV\suite\rules.json`).
2. **Motor:** `FRV\engine\run.mjs` roda os casos de `FRV\engine\tc.json` no modele-social e grava `engine.json`.
3. **Comparação linha a linha** com tolerância de 0,01 EUR (coeficiente RGDU em 4 casas), por regra e por linha, com regressão contra uma linha de base (`FRV\baseline\baseline.json`). Um comando: `py run_suite.py`.
4. **Divergência não se resolve confiando em nenhum dos lados**: decide o texto oficial (Légifrance, BOSS, BOFiP, URSSAF, Agirc-Arrco, net-entreprises).
5. **Teste 0:** amostragem por risco de afirmações factuais de cada artefato, conferidas em fonte primária.
6. **DSN-Val** em modo batch sobre os arquivos de exemplo das specs, com triagem das anomalias em 3 baldes.
7. **Revisões adversariais** de CCG, WTC/DD/Payslip/SIR e das 15 specs (lotes A e B).
8. **Redlines** DRAFT com changelog célula a célula; aprovação humana nos portões G1–G7; promoção ao `mercans-pipeline`.

### 1.3 Período
- Arquivo de teste DSN `FR-DSN-TEST-01.txt`: mtime 2026-10-01.
- Commits: 2026-10-05 (`1078929`, suíte e drafts D-01..D-10) até 2026-10-09 (`1193039`, correções do Teste 0). Sessões continuaram até 2026-10-13 (upload do design para o Drive compartilhado).
- Quase todo o trabalho de revisão, redlines, D-11..D-19 e promoção aconteceu em **2026-10-06**.

### 1.4 Estado final
| Item | Situação | Evidência |
|---|---|---|
| Suíte de cálculo | 112 casos, **2.403 / 2.462 checagens (97,6 %)**, regras 25/37, 0 regressões. As 59 falhas são todas defeitos confirmados do motor | `FRV\results\run-20261006-093517\report.md`; HANDOFF "Latest" |
| Linha de base aprovada (G3) | run 20261006-073916: 106 casos, 2.268/2.324 (97,6 %), regras 25/35 | HANDOFF |
| Simulações | 1.776 de 1.855 linhas comparadas iguais ao modele-social; toda diferença é defeito confirmado do motor (D-19 em aberto) | commit `acc98fb`; `FRV\workbook\validation_evidence\README.md` |
| Teste 0 final (pacote v1.0) | **77,5 % → 94,1 % → 98,0 %** (50/51) após corrigir 2 frases no WTC/DD | commit `1193039`; transcrição 2026-10-09 13:06 |
| Artefatos finais | CCG, WTC, DD, Payslip, 15 specs, design, skill e simulações emitidos como **v1.0 única de 2026-10-06** em `FRV\final\` | commits `36de79c`, `03a4f1b` |
| Promoção | Promovidos ao `mercans-pipeline\FR-compliance` em 2026-10-06 (`promote.py`/`promote2.py`) e de novo em 2026-10-09 (`workbook\promote_to_pipeline.py`, 27 arquivos arquivados em `Archived\2026-10-09-promotion\`) | HANDOFF; transcrição 2026-10-09 12:30 |
| Defeitos | D-01..D-18 confirmados no G2; D-19 inconclusivo | `FRV\docs\defect-drafts\INDEX.md` |
| Notas abertas | 27 de 31 resolvidas; 4 sem fonte acessível | `FRV\docs\review\FR-open-notes-research-2026-10-06.md` |
| Fora de escopo por decisão | G7 (YouTrack, issues upstream, upload ao Drive) e a comparação com a saída de folha da Mercans | INDEX.md, "Decisions ... second round" |
| Melhoria do pipeline | `PIPELINE_IMPROVEMENT_PROMPT.md` e `IMPROVEMENT_LOG.md` criados em `C:\Users\instituto\mercans-pipeline\`; Fases 0–5 feitas, **Fase 6 (piloto num país novo) não rodou**; recomendação de piloto: Portugal | transcrição 2026-10-09 00:37 e 12:30 |

### 1.5 Números de "antes e depois"
| Indicador | Antes | Depois | Fonte |
|---|---|---|---|
| Suíte, run 1 (12 casos, 396 checagens) | 371/396 = 93,7 %, regras 8/12 | — | HANDOFF "Results of run 1" |
| Suíte de 32 casos | 872/928 = 94,0 %, regras 14/21 | 907/928 = 97,7 % (D-01 + D-03) | `results\run-20261006-024718` vs `-040734` |
| Suíte de 112 casos (research original vs corrigida) | 94,7 % (número da transcrição) | 97,6 % bruto; 100 % "pela lei" | transcrição 2026-10-08 13:22 |
| Teste 0 do CCG | 28/36 = 77,8 % | — | `FR-CCG-001-v1.0-review-2026-10-06.md` |
| Teste 0 WTC/DD | WTC 24/32 = 75,0 %; DD 7/8 = 87,5 %; combinado 31/40 = 77,5 % | 98,0 % (pacote v1.0) | `FR-WTC-DD-PAYSLIP-SIR-review-2026-10-06.md`; commit `1193039` |
| DSN-Val no exemplo da DSN Mensuelle | 51 anomalias (49 bloqueantes), envio KO | 0 | `FR-DSN-001-dsnval-triage-2026-10-06.md` |
| Regras de controle da norma cortadas | 71 controles faltando na FR-DSN-001; 23 de 138 na DGFIP-001 | 0 | triagem SD-03; Specs B SB-09 |
| Cobertura automática (traceability) | CCG 28,6 % AUTO (45,4 % com Teste 0); WTC 12,2 % AUTO (15,1 %); 46,9 % das regras do CCG e 80,2 % das verbas do WTC sem checagem nenhuma | — | `FR-TRACEABILITY-E2-2026-10-06.md` |
| Retrabalho no CCG | 211 tracked changes (233 `w:ins`, 185 `w:del`) | — | `redlines\FR-CCG-001-v1.1-DRAFT-FRVAL-2026-10-06-CHANGELOG.md` |
| Retrabalho no WTC / DD | WTC 178 células (passo 1) → 213 → 310 com o Form Reference Guide; DD 32 → 55 → 57 células | — | changelogs; HANDOFF "Final state" |
| Autoverificação do próprio CCG | "cerca de 17 de 149 perguntas (11 %) reverificadas em 2 set 2026" | — | revisão do CCG, observação 2 |

---

## 2. Catálogo de defeitos encontrados

Severidade (escala aprovada no G2 de 2026-10-06, `docs\defect-drafts\INDEX.md`): **S1** valor errado de contribuição ou líquido para toda a população, ou DSN rejeitada; **S2** base, teto ou condição errada para uma faixa da população; **S3** campo derivado ou informativo errado (net social, net taxable); **S4** texto, referência ou formatação, sem efeito no cálculo. Para specs: erro em aba normativa que faz o DSN-Val rejeitar = S1; em aba instrucional = S2; só em aba ilustrativa = S3/S4.

Detecção: **ORÁCULO** (suíte contra o modele-social), **SIM** (simulações FR-SIM-002), **T0** (Teste 0 em fonte primária), **REV** (revisão adversarial manual), **DSNVAL** (validador oficial), **DIFF** (diff célula a célula entre versões).

Abreviações de caminho: `DD\` = `FRV\docs\defect-drafts\`; `RV\` = `FRV\docs\review\`; `RL\` = `FRV\redlines\`.

### 2.1 Defeitos da research (cálculo e regra) — o que o pipeline errou

| ID | Artefato | O que estava errado | Sev. | Causa-raiz (estágio que falhou e por quê) | Detecção | Correção | Evidência |
|---|---|---|---|---|---|---|---|
| D-01 / CCG F-01 / WTC F-01 | CCG Mod. 3 Step 3, Tabelas 24/26/48/53/56; WTC FR-023, 21645, 23640 e boilerplate; `params.json` APEC_CAP | Apec aplicada nas faixas 1+2 (até 8 PMSS, EUR 32.040) | S2 | **Pesquisa de fontes (Estágio 1):** valor tirado de fonte secundária/antiga sem ler o barème oficial. O certo é **4 PSS = EUR 16.020/mês (192.240/ano)**, Circular Agirc-Arrco 2025-16-SG-DRJ, fonte "Protocole Agirc-Arrco - Apec du 24 avril 2024". A citação "Protocole Agirc-Apec 2 Feb 2011" não existe com esse nome. O erro se propagou de forma consistente para CCG, WTC e skill (todos errados "em concordância") | ORÁCULO (TC10–TC12, TC18, TC19) | APEC_CAP 8→4 (G1); CCG e WTC redline; skill regenerada | `DD\D-01-apec-cap.md`; PDFs em `FRV\docs\evidence\` |
| D-03 / CCG F-03 / Payslip F-31 | CCG Mod. 3 Step 4, Mod. 6.3 Ex. 1, Mod. 12 Ex. 1/2/3/5/6; Payslip Spec B66 | Montant net social somava a cobertura patronal (saúde, prévoyance, aposentadoria suplementar) | S3 (S2 se o produto seguir) | **Atualidade:** doutrina de 2023, anterior a 01/01/2024. Para 2026 vale CSS R844-1 II (Décret 2023-1378): bruto − contribuições do empregado, sem o financiamento patronal L911-1. Agravante: o BOSS de 02/10/2026 anuncia **inclusão a partir de 2027** (decreto em minuta), e o CCG não distinguia os dois anos | ORÁCULO (TC08–TC20) + REV | Fórmula 2026 no oráculo (G1); CCG com regra datada; Exemplo 1: net social 2.305,00 → 2.275,00 | `DD\D-03-net-social-cadre.md`; `RV\FR-CCG-001-v1.0-review...` F-03 |
| CCG F-04 / WTC F-06 (lado research do D-02) | CCG Mod. 4.2 T34, 4.6 T49, 6.1.1, 7.2 T111; WTC FR-011, 23671, 62615, 62616 | Prévoyance patronal (1,50 % cadre) somada ao líquido tributável; o próprio CCG Mod. 3 Step 5 dizia o contrário | S3 (S2 se alimentar a base do PAS) | **Construção do artefato:** a mesma regra escrita de duas formas em módulos diferentes, sem checagem de coerência interna. Correto: só a parte patronal de **saúde** e o excedente acima de 5 % PASS + 2 % da remuneração (teto 2 % × 8 PASS) entram (CGI 83 1° quater; BOI-RSA-BASE-30-10-20 §200/270/290) | REV + T0 (B7) | Redline CCG/WTC; flag de tributação "Yes-No" | revisões CCG e WTC |
| D-11 | CCG / WTC | **CPF-CDD 1 % ausente** da research (o motor estava certo). CDD convertido em CDI **não** é isento desde 2022 (D6331-72 4° e 5° revogados pelo Décret 2021-1917; BOSS ¶490) | S2 | **Escopo/cobertura (Estágio 1):** sem matriz obrigatória de situações especiais (tipo de contrato) | ORÁCULO (TC46a/TC46b: ER total 403,39 vs 425,39) | Oráculo e CCG/WTC corrigidos | `DD\D-11-cpf-cdd.md` |
| D-12 (lado research) | CCG | Indenização diária AT/MP: faltava o teto do ganho líquido a partir do 29º dia e se usava o divisor de doença 3/91,25 em vez de **1/30,42** (R433-4) | S3 | **Pesquisa:** regra de um benefício copiada de outro (doença → AT/MP) | ORÁCULO (TC45c) | Oráculo e CCG corrigidos | `DD\D-12-atmp-daily-benefit.md`; `RV\FR-WTC-DD-flags-research...` item 7 |
| D-17 | CCG / WTC | **Não residente fiscal coberto pela seguridade francesa:** research cobrava CSG/CRDS; o certo é **COTAM 5,50 %** (CSS L131-9, D242-3). EE 833,61 vs 672,40 (−161,20/mês num bruto de 4.000) | S2 | **Escopo:** a checagem de não residente (C31 no pipeline) só olha o imposto de renda, não a seguridade social | SIM (P1-03b / P2-03) | WTC v1.1 ganhou a verba **FR-079 COTAM**; CCG Exemplo 2 alterado | `DD\D-17-non-resident-cotam.md` |
| CCG F-05 | CCG Mod. 12 Ex. 2 | RGDU de tempo parcial a 80 % usando o SMIC anual de tempo integral (C = 0,3981 em vez de **0,3751**); redução superestimada em ~EUR 34,35/mês (~412/ano) | S2 | **Exemplo resolvido digitado, não calculado:** o oráculo já prorrateava (D241-7 IV) | REV + T0 (T11) | Redline (16 mudanças F-05) | revisão do CCG |
| CCG F-02 / WTC F-04 | CCG Tab. 50/56; WTC FR-019 e boilerplate 62135/62645 | Contribuição ao diálogo social (CDS) 0,016 % listada **também para o empregado** | S1 (população inteira; valor pequeno) | **Construção:** o boilerplate repetido em dezenas de células multiplicou o erro; contradiz a Tab. 26 do próprio CCG | REV + T0 (T17, W8) | Redline | revisões |
| WTC F-05 | WTC FR-019, FR-024 | CDS colocada dentro do perímetro da RGDU | S3 | Mesma causa (boilerplate) | REV + T0 (W7) | Redline | revisão WTC |
| CCG F-08 / F-09 / WTC F-17 / D-07 | CCG Mod. 4.3, 5.2, 11.1/11.2; WTC FR-013/041; Payslip Population Range | Proporcionalização do teto apresentada como automática e "pelo mesmo método do salário". Correto: fórmula fixa por dias calendário (R242-2); no tempo parcial é **opção do empregador**, renunciável em comum acordo, e o numerador inclui heures complémentaires (BOSS §760) | S3 | **Pesquisa:** leitura parcial do BOSS | REV + ORÁCULO (TC23/TC24) | Redline; novo flag `58218` no design | `DD\D-07-part-time-proration.md` |
| CCG F-11 | CCG Mod. 9.1 (Tabela 141) | Net taxable 3.447,70 sem somar os 485,00 de encargos não dedutíveis da fração não isenta da indenização → deveria ser **3.932,70**; PAS subestimado em 48,02 | S3 | **Exemplo resolvido digitado** | REV | Redline | revisão do CCG |
| CCG F-13 | CCG Mod. 6.3 Ex. 1/3, Mod. 12 Ex. 5 | Base da CSG/CRDS sem a prévoyance patronal de 1,50 % (o próprio Step 2 diz 100 %). Ex. 5: base 6.491,33, não 6.431,25 | S3 | Exemplo resolvido incoerente com o texto | REV | Redline (53 mudanças) | revisão do CCG |
| CCG F-12, F-14, F-10, F-20 | CCG Mod. 9.1, 4.2, 12 Ex. 6, Tab. 62 vs 167 | Média de 3 meses com bônus fora da janela; divisor 151,67 arredondado (OT 171,40 vs 171,43); mesmo teto 3.203,84 e 3.203,85; F-20 (1.352,09) **retirado** após recalcular | S4 | Exemplos sem recálculo e convenções de arredondamento não fixadas | REV | Redline (F-14 com 40 mudanças) | revisão do CCG; CHANGELOG |
| CCG Ex. 3 (Mod. 6.3) | CCG v1.1 | Teto de dezembro impresso **4.005,00**; com a regularização progressiva que o próprio exemplo invoca, **4.060,00** | S4 | Exemplo resolvido digitado | SIM (P2-05) | Dobrado na final v1.1 | `RV\FR-SIM-002-part2-notes.md` |
| CCG F-29 | CCG Mod. 12 Ex. 6 (Moselle) | Total patronal 1.231,29 só fecha com taxa de aprendizagem 0,68 %; o certo na Alsace-Moselle é 0,44 % (CT L6241-1-1) | S3 | Exemplo digitado | REV (redline) | Parágrafo F da pesquisa de lacunas | `RV\FR-CCG-001-gaps-research...` |
| CCG F-16 | CCG Mod. 5.2 | Assiette minimale (CSS R242-1; BOSS seção adicionada em 24/07/2026) ausente | S3 | **Atualidade:** mudança do BOSS posterior à build não capturada | REV | Parágrafo A inserido | pesquisa de lacunas |
| CCG (taxe sur les salaires) | CCG Mod. 6.1 | Só as taxas 4,25/8,50/13,60 %; **faltavam os limites de 2026** (9.229 / 18.423) | S3 | Cobertura incompleta | REV | Parágrafo B | pesquisa de lacunas |
| CCG F-21 / commit `1193039` | CCG Tab. 70; WTC 23671/62616; DD (2 células) | Empregador que não contrata a prévoyance do cadre responde por "três anos de salário"; o certo é **3 × PASS** (EUR 144.180 em 2026; ANI 17/11/2017) | S3 | **Pesquisa:** afirmação sem fonte primária; no CCG ficou corrigida, mas WTC/DD mantiveram o texto antigo | REV + T0 final | Corrigido em 2026-10-09 | commit `1193039` |
| T0 final (commit `1193039`) | WTC 62876 | IJ de acidente de trabalho descrita como "totalmente tributável"; correto: tributável sobre **50 %** (CGI 81 8°) | S3 | **Propagação:** CCG certo, WTC errado — não há checagem de coerência entre artefatos | T0 final | Corrigido | commit `1193039` |
| CCG F-23 / WTC F-14 | CCG; WTC FR-066 | Minimum garanti 4,22 (valor de 2025); correto **4,25** em 01/01/2026 (Décret 2025-1228) e 4,35 em 01/06/2026 (Arrêté de 22/05/2026, não decreto) | S3 | Atualidade | T0 (W26) + pesquisa A5 | Redline | revisões |
| CCG F-24 | CCG | Mínimo protegido 651,69 sem data: só vale **a partir de 01/04/2026** (Décret 2026-220) | S3 | Valor sem data de vigência | pesquisa C5 | Redline; design R-06 | revisão do CCG |
| CCG F-25 / F-26 | CCG Mod. 8.1 / 10.6 | Conteúdo errado atribuído à Loi 2026-492 e artigos errados da Loi 2026-534 | S3 | Citação sem leitura do texto | pesquisa C10/C11 | Redline | revisão do CCG |
| CCG F-06, F-07/D-08, F-28 | CCG | RGDU citando só o Décret 2025-1446 (correto: 2025-887 alterado por 2025-1446); FNAL citando o CSS L834-1 **revogado** (4 ocorrências; correto CCH L813-4/L813-5); limite de pagamento em espécie 1.500 citado no CT L3241-1 (está no Décret 85-1073) | S4 | Citação não conferida em Légifrance | REV + pesquisa A2/A3 | Redline | `DD\D-08-citation-corrections.md` |
| CCG F-17, F-18, F-19 | CCG | Tolerância BOSS do congelamento do SMIC não citada; norma DSN 2027 (CT2027.1.2 de 09/09/2026) não antecipada; **versão 1.3 dentro de um arquivo v1.0**, quatro versões "Released" sem mudar o nome | S4 | Atualidade e controle de versão | REV | Redline | revisão do CCG |
| WTC F-02 / F-03 | WTC 21640–21642, 23640, 62641, 21645 | Agirc-Arrco declarada com código **105** (só para regularizar períodos anteriores a 2025); correto **131** (retraite + CEG + CET) e **132** só Apec | S2 | **Pesquisa de DSN:** cahier de codificação Agirc-Arrco CT2025.1.2 não lido | T0 (W17) | Redline | revisão WTC |
| WTC F-07 | WTC 23640 col. R | Contribuição patronal Agirc-Arrco marcada como sujeita a CSG; o próprio FR-046 diz que não | S2 | Flag de taxabilidade contradizendo o texto da mesma planilha | REV | Redline | revisão WTC |
| WTC F-08 | WTC FR-049 | Montant net social mapeado para S21.G00.50.004 (que é o "montant net versé"); correto: **bloco S21.G00.58 tipo 03** | S1 | Mapeamento DSN não conferido no cahier | REV + T0 (W31) + DSNVAL (#27 CCH-14) | Redline | revisão WTC |
| WTC F-09 | WTC FR-027, 21212, 62334, 62335 | Horas extras isentas e prêmio de impatriado em S21.G00.50.011 (reservado a aprendiz/estagiário); horas extras vão em S21.G00.58 tipo 01 | S2 | Idem | REV | Redline | revisão WTC |
| WTC F-10 | WTC FR-005; CCG Mod. 3 Step 6, Mod. 6 | PAS arredondado ao euro; correto: **ao centavo** (CGI Ann. III 39 C 3° f; cahier S21.G00.50.009) | S1 (≤ EUR 0,50) | Regra sem fonte (o próprio `params.json` anotava "unsourced") | T0 (W32) | Redline | revisão WTC |
| WTC F-11, F-12, F-13, F-23 | WTC FR-058/059/060/061/039 | Rubricas DSN erradas (statut catégoriel .003 vs .004/.005; effectif no código APET; flag Alsace-Moselle no código INSEE da comuna; DOETH no status BOETH do empregado). O **DD estava certo** | S3/S4 | Sem checagem cruzada WTC × DD × spec | REV | Redline | revisão WTC |
| WTC F-16 | WTC FR-021 | Sobretaxas de contratos curtos (+0,5 %, +3 %, +1,5 %) apresentadas como vigentes (abolidas em 2017/2019); bonus-malus 2,95–5,00 % ausente | S2 | Atualidade | REV + pesquisa | Texto de substituição; campo novo no DD | `RV\FR-WTC-DD-flags-research...` 1a/1b |
| WTC F-21 / F-22 | WTC 62875–62877, 62190 | IJSS subrogadas codificadas como "avantage en nature" (S21.G00.54 tipo 06). Correto: S21.G00.60.004 = 01 + S21.G00.58.003 = 10 | S3 | Mapeamento DSN inventado por analogia | REV + pesquisa | Redline | flags research item 2 |
| WTC F-24 | WTC FR-027, 62135, Tax Credit C5 | Teto de 7.500 de horas extras "acumulado entre empregadores"; DD e CCG divergem entre si | S4 | Mesma regra escrita de três formas em três artefatos | REV | Redline | revisão WTC |
| WTC F-20 / DD F-36 / F-34 | WTC Version Control; DD | WTC no Drive com conteúdo v1.3 mas log só "1.0"; DD no Drive **desatualizado** (sem colunas de grupo de campos); DD dizia que a grade PAS de 2025 "não deve mais ser usada" (errado para pagamentos de jan–abr/2026) | S3/S4 | **Entrega/promoção:** cópia no Drive divergente da do pipeline | DIFF + T0 (D8) | DD v1.2 | revisão WTC/DD seção 2 |
| DD F-35 | DD ID Information | Faltava campo para a taxa modulada do seguro-desemprego (bonus-malus) | S3 | Cobertura | REV | Campo novo DD v1.2 | flags research 1c |
| SD-02 (DD) | DD | Faltava "Urssaf SIRET (collecting body)" no estabelecimento | S2 | Spec dizia "produzido pelo cálculo da folha" — é dado mestre | DSNVAL | Campo novo (ID Information row 34) | triagem SD-02 |

### 2.2 Payslip Generator

| ID | O que estava errado | Sev. | Causa-raiz | Detecção | Correção | Evidência |
|---|---|---|---|---|---|---|
| Payslip F-25 | Sem o velhice 6,90 % plafonado e sem a CSG dedutível 6,80 %; líquido mostrado 2.702,99, **superestimado em ~EUR 400** | S1 | **Edição visual destruiu o conteúdo:** o ajuste ao layout "modelo Espanha" (backups `.bak-visual-20260902-*`) apagou 8 linhas (FR-012, FR-016, 21900/FR-013, FR-015, FR-021, FR-001, FR-024, FR-050) e deslocou fórmulas uma linha (ex. I75 PAS = `I72*I73`, net social × net taxable) | DIFF + REV | Conteúdo restaurado do `.bak-visual2-20260902-120749` dentro do layout de 16/09 | revisão WTC/DD/Payslip seção 2; changelog do Payslip |
| Payslip F-26 | Sem saúde 13 %, velhice 8,55 %, família 5,25 %, AT/MP (2,08 % no cabeçalho, nunca calculado), desemprego 4,00 %; sem RGDU e sem custo total | S2 | Idem | REV | Idem | idem |
| Payslip F-27 | Faltavam itens obrigatórios do R3243-1 (3°, 4°, 5°, 9°, 9° bis, 11°, 13°, 14°, 15°): net antes do imposto, montant net social, net taxable, PAS, data de pagamento, convenção coletiva, classificação, horas, menção service-public | S1 | Idem; nenhum gate verificava o R3243-1 | REV | Idem | idem |
| Payslip F-28 | Benefício em espécie de refeição (115,50) somado ao bruto e **nunca deduzido** → líquido superestimado em 115,50 | S1 | Fórmula quebrada | REV | Idem | idem |
| Payslip F-29, F-30, F-32, F-33 | Códigos de verba que não batem com o WTC; Spec B58 com a taxa reduzida de família 3,45 % (abolida em 2026); 151,67 em vez da fração exata; "read from FR-DD-001-v1.0" quando o DD vivo era v1.1 | S2–S4 | Sem checagem Payslip × WTC × DD | REV | Idem; aba FR toda em francês | idem |

### 2.3 Report specs (15) — defeitos sistêmicos do gerador

A maioria dos defeitos das specs vem do **código compartilhado do gerador** (`04-reports-spec/_lib/`), não de pesquisa. Por isso se repetiram em todas.

| ID | Specs afetadas | O que estava errado | Sev. | Causa-raiz | Detecção | Correção | Evidência |
|---|---|---|---|---|---|---|---|
| SD-03 / SA-01 / SB-09 | DSN-001, DSN-002, DSN-003, URSSAF-003, URSSAF-004, DGFIP-001, DGFIP-003 | **Conditional Reason cortada em 2.500 caracteres:** `_lib/fr_norm.py` linha 292 `return "\n".join(bits)[:2500]` (e `[:3500]` na Field Explanation). FR-DSN-001: **71 controles** perdidos em 21 rubricas (610 controles, 539 presentes); DGFIP-001: 23 de 138; DGFIP-003: 4 de 11. Esconderam o CCH-16 (base 03 obrigatória) e o SB-01 | S1/S2 | **Construção:** truncamento silencioso por limite de célula do Excel | DSNVAL (#29 CCH-16) + comparação com `dsn-datatypes-CT2026.xlsx` | Sem corte; texto longo continua na linha seguinte com "(continued)". Maior célula: 14.643 caracteres | triagem SD-03; `RL\specs\README.md` §2 |
| SD-01 / SA-02 / SA-03 / SA-04 / SB-10 | DSN-001, DSN-002, DSN-003, DGFIP-001, URSSAF-003, URSSAF-004 | Árvore de blocos **genérica da DSN mensal copiada para todas**; blocos em ordem crescente de identificador (a norma proíbe: CT2026.1 §3 p.76); cardinalidades da aba genérica, não por natureza. S21.G00.50 posto sob S21.G00.40; 20/22/23 depois dos indivíduos; S21.G00.71/53/58/86 omitidos | S1 | **Construção:** template único sem árvore por natureza de declaração | DSNVAL (CST-01, CST-02) | `_lib/fr_trees.py` novo; specs reordenadas fisicamente; `ROW-REMAP.csv` | triagem SD-01; Specs A |
| SD-02 / SA-05 | DSN-001, URSSAF-003, URSSAF-004 | Identificador OPS (S21.G00.20.001 / 22.001 / 81.002 / 82.005) "sem contraparte no DD, produzido pelo cálculo"; exemplos inválidos (`1234`, `75056` = código INSEE, `01`) | S2 | **Construção:** campo obrigatório sem fonte de dado | DSNVAL (#11, #12, #17) | Dado mestre do estabelecimento; SIRET Urssaf `78861779300013`; tabelas IVO/IBC/ICI | triagem SD-02 |
| SD-04 / SA-07 / SB-11 | Praticamente todas | Exemplos e Sample File inválidos: SIREN/SIRET falham no Luhn (`839123456`, `83912345600024`, `55210055400016`, `49876543200017`); NIR masculino para nome/sexo feminino; código de risco `711CC` inexistente; deslocamento de campos; S90 com contagem errada. O arquivo de teste copiado do Sample da DSN-001 deu **44 anomalias de balde 1** | S3/S4 (S1 quando o sample é a única referência) | **Construção:** exemplos fictícios digitados, sem validação | DSNVAL | `_lib/fr_ids.py` (identificadores válidos verificados na importação); samples com 0 anomalias | triagem SD-04 |
| SD-05 / SA-06 / SB-34 | Todas as 15 | Cópia mais nova (04-reports-spec, 10/09) **perdeu o Version Control**: Document ID em branco, histórico v1.0–v1.3 colapsado em uma linha, bloco REMARKS perdido | S4 | **Entrega/promoção:** regeneração sobrescreveu o histórico | DIFF | Histórico restaurado das cópias "corrigidos" | Specs A §1 |
| Patches pós-build | Todas | Os .xlsx emitidos em 10/09 **não são o que os scripts de 27/08 produzem**: alinhamento com o DD, tradução das Field Options, cores e posições foram aplicados à mão no .xlsx. Regerar desfazia 2 semanas de correções. Um desses patches manuais (DGFIP-003, 03/09) **introduziu o SB-19** | S1 (pelo SB-19) | **Construção:** correção manual no binário em vez do script | DIFF + REV | Overlay por chave de linha (`_data/postbuild_overlay.json`), com rejeição explícita do patch errado (`overlay_rejects.json`) | `RL\specs\README.md` §2 |
| SB-19 | DGFIP-003 (taxe sur les salaires) | Aplicava 8,50 %/13,60 % sobre as faixas **além** dos 4,25 % na totalidade: dupla contagem, imposto **superestimado ~31–33 %**; o "exemplo oficial" foi alterado | S1 | Patch manual de 2026-09-03 sem recálculo do exemplo oficial (a nota da administração dá 2.550) | REV | 4,25 % adicional em A1, 9,35 % em A2 (CGI 231 §2 bis); exemplo 2.550 / 5.787 restaurado | Specs B |
| SB-01 / SB-02 / SB-03 | DGFIP-001 (PAS) | Grupo de correção de taxa com S21.G00.56.006 proibido (rejeição); controle do PAS sobre o net taxable em vez de S21.G00.50.013; gatilho do 182 A pelo S21.G00.30.022 (situação de trabalho) em vez do domicílio fiscal | S1/S2 | Regra lida do campo errado; controle escondido pelo truncamento | REV + DSNVAL | Redline regenerada | Specs B |
| SB-05 / SB-14 / SB-15 | DGFIP-002 (CRM PAS) | Taxa "só no contracheque seguinte" (errado: aplica-se o mais recente); validade "dois meses" (correto: até o fim do 2º mês seguinte); um CRM só (são dois, mais o "taux sur taux" de 2027) | S3 | Fonte (a_id 1937 da net-entreprises) dada como "não recuperável" | REV | Redline | Specs B |
| SB-06 / SB-07 | DGFIP-001/002 | Sample com taxa 3,50 % (correto 2,9 % → PAS 57,42); grades e datas de troca ausentes | S3 | Exemplo digitado | REV | Redline | Specs B |
| SA-08 / SA-19 / SIR-01 | DSN-002, DSN-003, CCG, SIR | Prazo da FCTU "5 dias após saber do evento" (correto: **5 dias úteis após o fim do contrato**); reprise só se antecipada, 5 dias úteis | S2 | Pesquisa; erro presente também no CCG e no SIR | REV | Redline | Specs A |
| SA-09, SA-10, SA-18 | DSN-002, DSN-003 | FCTU antes da folha final; último dia trabalhado em 62.008 (é 62.006); temps partiel thérapeutique nas naturezas 04/05 (proibido) | S2 | Pesquisa de norma por natureza | DSNVAL + REV | Redline | Specs A |
| SA-25 / SA-26 | URSSAF-001 (DPAE) | Spec dizia que o guia NAT/5492 "não foi obtido", mas o runbook do SIR já o tinha (formato 120); campo SPST (R1221-1 1°) ausente | S2 | **Propagação SIR → spec:** artefatos construídos sem ler um ao outro | REV | Spec reemitida sobre o formato 120 | Specs A |
| SA-40 / SA-41 / SA-42 / SA-43 | URSSAF-004 (solde TA) | Linha de pagamento CTP 995 (+996/997) ausente; CSA na DSN de **abril** (correto: março); solde aplicado à Alsace-Moselle (não é devido); entidades sem fins lucrativos sujeitas desde março/2026 omitidas | S1/S2 | Pesquisa e atualidade | REV + DSNVAL | Redline | Specs A |
| SB-25 | CARSAT-001 | Taxa AT/MP indexada só por SIRET (correto: SIRET + código de risco + taxa "B"); rubricas 40.040/40.043 não citadas | S2 | Pesquisa | REV | Redline | Specs B |
| SIR-01..09 | FR-SIR-INDEX-001 | Prazos simplificados; FR-URSSAF-002 descrito como "outbound" (é inbound CRM); "DSN Substitution" como ferramenta do declarante (é a natureza 09, emitida pela URSSAF); CRM 124 omitido; ID "FR-SIR-001" num arquivo FR-SIR-INDEX-001 | S2–S4 | Propagação e controle de nome | REV | Só achados; sem redline do SIR | Specs A §3.9 |

### 2.4 Defeitos de entrega e de vazamento entre países (encontrados depois das finais)

| ID | O que estava errado | Causa-raiz | Detecção | Correção | Evidência |
|---|---|---|---|---|---|
| Sobras de outros países | "REFERENCE_Payslip_Tunisia" no Payslip; "delivered Belgium catalogue" no WTC; "countries built so far" e códigos belgas "BE-NSSO-002/004" em 7 specs; "FR-NSSO / FR-FIN series" no CCG; "Descoped as FR-FIN-001" na DSN Mensuelle; frase "A previous jurisdiction in this pipeline had … wrongly propagated" no CCG e no WTC | **Construção por cópia de template/precedente** de outro país sem limpeza | Checagem de sobras (C42 no pipeline novo) | Removidas em 2026-10-09 | commits `3145c96`, `c480af7`; transcrição 2026-10-09 12:30 |
| Jargão do método interno | "v2.7 STEP 3.5", "C25 audit failure", "locked before Stage 1", "v2.8 check B4", caminhos `FR-compliance/...`, "A CORRECTION TO scope_manifest.json IS RECORDED HERE" dentro das specs | O pipeline escreve sua própria narrativa no entregável | Varredura `release_crosscheck.py` | Trocado por texto neutro | transcrição 2026-10-07 22:11 |
| Versões internas | Report Matrix com "Version 1.4–1.6" nas 15 specs; CCG v1.0 com "1.3" no título | Sem versão única de pacote | Varredura | Tudo v1.0 de 2026-10-06 | commits `03a4f1b`, `c480af7` |
| "NO DD COUNTERPART" | 264 anotações falsas de "sem contraparte no DD" nas specs (número da transcrição) | Índice spec ↔ DD inexistente no gerador | Plano de ação | `_data/dd_v11_index.json` no builder corrigido | `RL\specs\BUILDER-PATCH.diff`; transcrição 2026-10-07 23:26 |
| Design v1.0 | Condições que **nunca disparavam** (`LESS($58209;1)` e `LESS($58222;1)` para um flag 1/2); referências para frente (ordinais); fórmula de `58110` contradizendo o próprio texto; `0.49` em vez de `0.0049` | Design escrito sem ligação com a research nem teste de expressão | Comparação de lógica na simulação | Design v1.1 (72 → 79 regulações; 94 mudanças) | `FRV\docs\history\2026-10-06-final-release\FR-DESIGN-v1_1-CHANGES.md` (R-05, R-35, R-42, R-44) |
| Skill desatualizada | Referências da skill guardam o hash do artefato de origem, mas ninguém confere; `audit_refs.py` com nomes v1.0 fixos no código; `make_all.py` com "374 códigos" fixo (real: 379) | Ferramenta frágil (F28 existe no log, mas não é verificado) | Uso durante a revisão | Skill regenerada 4 vezes (commits `3a016bb`, `36de79c`, `535d807`, `3400eda`) | transcrição 2026-10-07 22:11 |
| Desvio pós-promoção | Finais alterados depois de promovidos; o pipeline ficou com outra versão; a conferência de hash falhou | Promoção sem verificação byte a byte | Medição da Fase 4 (49 inconsistências) | `promote_to_pipeline.py` com log MD5 | transcrição 2026-10-07 22:11 e 2026-10-09 00:37 |

### 2.5 Defeitos do motor oficial (não são da research, mas ensinam sobre o oráculo)

D-02 (motor soma toda a prévoyance patronal ao net taxable, +60,07), D-04 (RGDU com o SMIC 12,31 a partir de 01/06/2026 apesar do Décret 2026-509; +30,00 no TC28), D-05 (grade PAS 2026 desde 01/01 em vez de 01/05), D-05b (Guyane/Mayotte 2.393 vs 2.398), D-06 e D-14 (arredondamento ao euro sem base legal), D-12 (teto R433-4 aplicado como dedução de 21 %), D-13 (teto IJSS com SMIC do dia em vez do último dia do mês anterior), D-15 (abono de contrato curto 748/12 em vez de 748, erro de unidade), D-16 (teto anual de 7.500 rateado por mês), D-18 (maternidade acima do teto sem o desconto de 21 %: 131,67 vs 104,02/dia), D-19 (presidente de SAS sem Apec/CDS, inconclusivo). Os 11 issues upstream foram reproduzidos e redigidos em `FRV\docs\g7-drafts\upstream-modele-social\` (não enviados; G7 fora de escopo).

**Lição:** o simulador oficial **não é gabarito**. Em 112 casos, as 59 divergências restantes eram todas erro do motor. Sem a regra "decide a fonte primária", a research teria sido "corrigida" para pior em pelo menos 11 pontos.

---

## 3. Padrões de falha recorrentes (generalizados para qualquer país)

1. **Erro consistente é invisível para QA de consistência.** O teto da Apec estava errado de forma igual no CCG, no WTC, na skill e no `params.json`. Toda checagem cruzada passava. Só um cálculo independente (oráculo × motor oficial) e a leitura do barème oficial pegaram.
2. **Valor sem data de vigência.** Minimum garanti de 2025, mínimo protegido sem "a partir de 01/04", net social sem a troca de 2027, grade PAS sem data de troca, sobretaxas abolidas em 2017/2019. O pipeline guarda o número, mas não o intervalo em que ele vale.
3. **Doutrina anterior à mudança.** Montant net social (regra de 2023), Agirc-Arrco código 105 (válido antes de 2025), sobretaxas de contrato curto. A pesquisa achou uma fonte verdadeira, mas antiga.
4. **Situações especiais fora do mapa.** Não residente fiscal na seguridade (COTAM), CDD (CPF-CDD), AT/MP, maternidade acima do teto, tempo parcial (SMIC e teto prorrateados, opção de renúncia), presidente de SAS. Sem uma matriz obrigatória de populações, a research cobre o caso padrão e esquece as faixas.
5. **Exemplos resolvidos digitados à mão.** CCG Ex. 2 (RGDU parcial), Ex. 3 (4.005 vs 4.060), Ex. 5/6.3 (base CSG), Mod. 9.1 (net taxable), Ex. 6 (taxa de aprendizagem), sample da DGFIP-001 (3,50 %), DGFIP-003 (dupla tributação). Nenhum exemplo era recalculado por fórmula a partir dos parâmetros do próprio artefato.
6. **A mesma regra escrita em vários lugares, de formas diferentes.** Prévoyance no net taxable (CCG Mod. 3 × Mod. 4/6/7; WTC × CCG × Payslip), teto de 7.500 (WTC × DD × CCG), CSG da Agirc-Arrco patronal (col. R × FR-046). Boilerplate repetido multiplica um erro em dezenas de células (CDS "each side").
7. **Mapeamento DSN por analogia, sem o cahier aberto.** MNS em 50.004, horas extras em 50.011, IJSS como benefício em espécie, PCS-ESE/statut catégoriel trocados, Alsace-Moselle no código INSEE, DOETH no status BOETH. Curiosamente o DD estava certo onde o WTC errou: os artefatos não eram cruzados.
8. **Gerador compartilhado com defeito = defeito em todas as specs.** Truncamento em 2.500 caracteres, árvore genérica, ordem por identificador, OPS sem fonte, identificadores inválidos. Corrigir na raiz (`_lib`) corrigiu as 15 de uma vez.
9. **Correção manual no binário, fora do gerador.** Os patches pós-build no .xlsx eram desfeitos a cada regeneração, e um deles introduziu um S1 (SB-19). Regra: toda correção entra no script ou num overlay versionado, nunca só no arquivo.
10. **Sample/exemplo "ilustrativo" vira referência de fato.** O arquivo de teste foi copiado do Sample File (que tinha aviso "não usar como referência") e herdou 44 anomalias. Se existe um exemplo, ele precisa ser válido.
11. **Truncamento e perda silenciosa.** Corte de texto na célula, Version Control colapsado na regeneração, conteúdo do Payslip apagado num ajuste visual, cópia do Drive mais antiga que a do pipeline. Nenhuma dessas perdas gerou erro.
12. **Vazamento entre países e do processo interno.** Bélgica, Tunísia, Holanda e códigos do pipeline dentro dos entregáveis franceses. Causa: construção a partir de precedente/template sem varredura de saída.
13. **Versão e identidade inconsistentes.** "1.3" dentro de v1.0; quatro "Released" sem bump; ID do SIR diferente do nome do arquivo; Report Matrix 1.4–1.6; Field Option citando DD v1.0.
14. **Afirmação de "fonte não obtida" falsa.** DPAE (guia NAT/5492 estava no runbook do SIR), CRM PAS (a_id 1937 legível), BPIJ. Um artefato declarava lacuna que outro artefato da mesma build já tinha resolvido.
15. **Citação sem leitura.** FNAL num artigo revogado, decreto incompleto da RGDU, artigos errados da Loi 2026-534, Protocolo Apec inexistente, BOI-IR-BASE-20-20 §210 (página errada, vinha das próprias notas da suíte). Isso vale também para o validador: a própria suíte tinha citações erradas, corrigidas em `TEST-DESIGN-CORRECTIONS.md`.
16. **Autoverificação baixa e declarada.** O próprio CCG dizia ter reverificado só 11 % das perguntas. O QA do pipeline aprovou com nota 87/100 (dado da transcrição) um pacote com Teste 0 de 77,5 %.
17. **Fontes oficiais que se contradizem.** A página de taxas da URSSAF ainda mostrava 7 %/3,45 % (abolidas); a tabela de parâmetros do BOSS escrevia Tdelta 0,4021 contra 0,3821 do capítulo da RGDU; a Agirc-Arrco dava 192.400 para o teto anual da Apec (o certo é 192.240 = 4 × 48.060); o BOFiP BOI-TPS-TS-30 online tem valores de 2020. Regra: a notícia datada e o texto normativo controlam sobre a tabela-resumo.

---

## 4. Metodologia de validação reutilizável

### 4.1 Componentes e como reaproveitar em outro país

| Componente | Arquivo(s) | O que faz | Reuso em outro país |
|---|---|---|---|
| Fonte única de parâmetros | `FRV\suite\params.json` | Cada taxa/teto com chave, valor, unidade e **fonte que cita a seção do CCG**. Nada é digitado em código | Direto: trocar os valores. É o embrião do `facts.json` |
| Regras e metadados de caso | `FRV\suite\rules.json` | Regras R01..R37, linhas que cada regra "possui", técnica de cada caso (classe de equivalência, valor-limite, combinação) | Direto: reescrever as regras do país |
| Oráculo | `FRV\oracle\oracle.py` | Reimplementação **independente** da research (lê só `params.json`), com arredondamento ROUND_HALF_UP ao centavo | Reescrever as fórmulas por país; manter a regra de "zero valor hard-coded" |
| Motor externo | `FRV\engine\run.mjs`, `tc.json`, `package.json` (modele-social 11.1.0 fixado) | Roda os casos no simulador oficial | Trocar pelo simulador do país (OpenFisca, API do governo, tabelas oficiais de retenção). Onde não houver, usar **exemplos resolvidos oficiais** (BOSS, BOFiP, guias da autoridade) como oráculo |
| Runner de um comando | `FRV\run_suite.py` | motor → oráculo → comparação → regras → regressão → workbook; saída em `results\run-YYYYMMDD-HHMMSS\` (`report.md`, `report.json`, `engine.json`, xlsx). Exit 0 = sem regressão; 1 = regressão; 2 = não rodou | Direto |
| Linha de base | `FRV\baseline\baseline.json`; `--set-baseline` só no G3 | Regressão = checagem que passava e agora falha | Direto |
| Registro de defeitos | `FRV\suite\defects.json` + `docs\defect-drafts\D-xx.md` + `INDEX.md` | Cada defeito com classe (research / motor / limitação / inconclusivo), severidade S1–S4, casos, fonte primária com citação literal, status e portão | Direto (o template do draft é reaproveitável) |
| Traceability | `RV\FR-TRACEABILITY-E2-2026-10-06.csv/.md` | Cada regra do CCG (273) e verba do WTC (378) marcada AUTO / TEST0 / REVIEW / NONE | Direto; mostra o que **não** foi testado |
| Teste 0 | Seção B da revisão do CCG; seção 6 da revisão WTC/DD | 30–50 afirmações por risco, cada uma com fonte, citação e veredito | Direto; meta ≥ 95 % |
| DSN-Val batch + triagem em 3 baldes | `RV\FR-DSN-001-dsnval-triage-2026-10-06.md`; `inputs\dsnval-2026-10-06\work\build_fix.py` | Balde 1 = arquivo de teste; balde 2 = spec; balde 3 = aviso. Itera até restar só o balde 2, que vira redline | Para todo país com validador oficial de declaração |
| Builder de specs corrigido | `inputs\spec-builder-work\04-reports-spec\` (`_lib\fr_trees.py`, `fr_ids.py`, `fr_overlay.py`, `fr_samples.py`; `_tools\run_all.py`); `RL\specs\BUILDER-PATCH.diff`, `ROW-REMAP.csv` | Sem truncamento; árvore por natureza; identificadores válidos; OPS como dado mestre; samples que passam no validador; overlay de patches | Levar para uma biblioteca comum (a "Frente A" do plano já fez isso no pipeline, segundo o `IMPROVEMENT_LOG`) |
| Prova de que a validação é válida | `FRV\workbook\validation_evidence\` | `verify_live_engine.py` (2.147/2.147 iguais ao motor ao vivo); `verify_independence.py` (0 fórmulas da research leem célula oficial); `verify_coverage.py` (1.855 comparadas, 455 não disponíveis no simulador); `mutation_test.py` (3/3 erros plantados detectados) | Direto. **Toda suíte de validação deveria vir com esses quatro testes** |
| Simulações no formato pedido pelo time | `workbook\sim_fr\`, `tax_sim_fr\`, `simple_fr\`; `final\simulations\` | Duas planilhas lado a lado: simulador oficial × simulação interna, com fórmula, lógica, cenário e resultado | Transformar em template por país |
| Ferramentas de release | `workbook\release_crosscheck.py`, `finalize_release.py`, `promote_to_pipeline.py` | Varredura de sinais de retrabalho/IDs de achado/pessoas/datas de carimbo; metadados únicos; promoção com arquivamento e log MD5 | Direto (já viraram ferramentas do pipeline, segundo a transcrição) |
| Redline sem corromper o arquivo | Changelogs do CCG/WTC/DD/Payslip | docx: tracked changes por XML, `validate.py` com `--original`, "rejeitar tudo = original"; xlsx com comentários/desenhos: **cirurgia de XML + repack**, nunca `openpyxl.save()`; cada célula alterada com preenchimento âmbar ou fonte vermelha e listada | Direto |
| Agentes | `.claude\agents\suite-runner.md` (Haiku), `test-engineer.md` (Sonnet), `legal-researcher.md` (Sonnet), `compliance-auditor.md` (Opus) | Separação de papéis: quem roda não interpreta; quem pesquisa propõe, não decide; o auditor tenta derrubar o parecer antes do humano | Direto. Fluxo de defeito: researcher → auditor → humano (G2). Fluxo de caso novo: test-engineer → suite-runner → achados para o researcher |
| Runbook e portões | `FRV\docs\runbook.md` | O que pode ser feito sem perguntar; G1 (mudar valor de research), G2 (classificar defeito), G3 (baseline), G4 (redline), G5 (fonte ambígua/paywall), G6 (regressão inexplicada), G7 (sair da pasta); condições de parada | Direto |
| Critérios de aceite | `runbook.md` "Acceptance criteria (approved 2026-10-06)" | Tolerância 0,01 EUR por linha (coeficiente em 4 casas); linha ≥ 95 %; toda regra FAIL com defeito aberto; zero S1 aberto; zero regressão antes de baseline | Direto |
| Fontes e acesso | `FRV\docs\sources.md`; `docs\evidence\` | BOSS e URSSAF via `curl -s "https://r.jina.ai/<url>"`; Agirc-Arrco com curl simples; Légifrance via WebFetch (Cloudflare 403 no curl); PDFs salvos e lidos com pypdf; 22 páginas BOSS salvas | Para cada país, mapear no início quais portais bloqueiam e qual rota funciona |
| Guias interativos | `FRV\guides\guia-passo-a-passo.html`, `guia-plano-de-validacao.html` | Passo a passo com "o que deve aparecer" e "se der errado"; plano mestre A–G | Template |

### 4.2 Cuidados de método aprendidos
- **Tolerância esconde erro de coeficiente:** diferenças < 0,01 numa linha de coeficiente passam. Comparar coeficientes com 4 casas (`TEST-DESIGN-CORRECTIONS.md` item 2).
- **Casos na fronteira de arredondamento enganam:** TC27 saiu de 3.000 para 2.900 porque a 3.000 o coeficiente estava a 3,6e-7 de uma fronteira.
- **O oráculo pode carregar o erro da research de propósito:** o `params.json` reproduz o que a research diz (APEC_CAP 8). Mudar valor de research no oráculo é decisão humana (G1), não ajuste de teste.
- **Campos derivados pelo runner não testam o motor:** o PAS em `run.mjs` é `round(net taxable × rate, 2)`; os casos de PAS testam a consulta de taxa e o arredondamento, não uma regra do motor.
- **Motor monoperíodo:** regularização anual, regras de 2025, S21.G00.56 e 182 A não são expressáveis; marcar como "N/E" e cobrir por exemplo oficial.
- **Teste 0 por risco subestima a acurácia real**, mas é o que acha o erro. Reportar as duas coisas.
- **Fetch resumido não é citação literal:** os drafts marcam "quotes through a summarising fetch tool"; reler por olho antes de publicar.

---

## 5. Regras e melhorias de processo, por estágio

### 5.1 Escopo / mandato
- Separar o que o motor de folha calcula do que é responsabilidade legal do empregador (lente de provedor de software; `CLAUDE.md`).
- **Matriz de populações obrigatória**, cada linha com resposta + fonte ou "não se aplica" justificado: residente/não residente (imposto **e** seguridade), CDI/CDD/CDD convertido, tempo parcial (com e sem renúncia ao prorrateio), dirigente (presidente de SAS), aprendiz, maternidade/paternidade, doença, AT/MP, rescisão, admissão/saída no meio do mês, regularização anual, regimes locais (Alsace-Moselle, DOM), tamanho de empregador (< 11, < 50, ≥ 250).
- Definir no início a **escala de severidade** e os **critérios de aceite** (aqui só foram aprovados no meio do trabalho, em 06/10).
- Levantar no Estágio de escopo **qual simulador oficial e qual validador de declaração existem** no país e se têm modo de teste (TESE não tinha).

### 5.2 Pesquisa de fontes
- Fonte primária decide; blog, fornecedor, simulador e fórum só servem para achar a fonte (`legal-researcher.md`).
- **Todo número com data de vigência e instrumento** (lei/decreto/arrêté/circular), lido no período da build. Distinguir decreto de arrêté (SMIC de junho/2026 foi arrêté).
- **Varredura de atualidade antes da entrega:** notícias do BOSS/autoridade desde a data da pesquisa (aqui: assiette minimale 24/07/2026, net social 2027 em 02/10/2026, CT2027.1.2 em 09/09/2026, LFSS 2026 sobre afastamentos).
- Ler o **cahier de codificação** de cada organismo complementar (Agirc-Arrco 131/132) e o cahier técnico da norma antes de mapear qualquer rubrica.
- Quando duas páginas oficiais divergirem, registrar (G5) e usar o texto normativo e a notícia datada; nunca a tabela-resumo.
- Registrar a rota de acesso que funciona por portal (r.jina.ai para BOSS/URSSAF; WebFetch para Légifrance) e salvar a evidência (`docs\evidence\`).
- Quem pesquisa propõe classe e severidade com confiança e "o que mudaria a conclusão"; nunca substitui fonte bloqueada por secundária.

### 5.3 Construção do artefato
- **Exemplos resolvidos gerados e recalculados por fórmula** a partir dos parâmetros do próprio artefato; nenhum número digitado.
- **Uma regra, um lugar:** o texto da regra mora no CCG; WTC, DD, Payslip e specs referenciam. Proibir boilerplate repetido com valores embutidos.
- Gerador de specs: sem truncamento; árvore e ordem **por natureza** de declaração a partir da tabela de usos da norma; todo campo obrigatório com fonte (DD ou dado mestre); identificadores fictícios válidos (Luhn, NIR coerente com sexo/data/departamento); códigos de exemplo existentes nas tabelas de referência.
- **Correção só no gerador ou em overlay versionado**, nunca à mão no .xlsx emitido.
- xlsx com comentários/desenhos: só cirurgia de XML + repack. Ajuste visual (layout "modelo Espanha") não pode remover linha estatutária; conferir o R3243-1 (ou equivalente do país) depois de qualquer mudança de layout.
- O texto do artefato diz **só a regra vigente**, nunca a narrativa da correção, nem códigos de checagem ("v2.7 STEP 3.5"), nem referências a outros países ou builds.
- Regras com troca de data no ano (net social 2026/2027, grade PAS 01/05, SMIC 01/06, abono 748/766) precisam de flag/constante datada no design.

### 5.4 QA / auditoria
- **Validação externa numérica bloqueante** (o "Estágio 9b" do plano): suíte contra o simulador oficial, toda divergência resolvida por fonte primária e classificada (research / motor / limitação / inconclusivo).
- **Teste 0** por artefato (≥ 30–50 afirmações por risco, meta ≥ 95 %), com a planilha de verificação guardada.
- **Validador oficial de formato** (DSN-Val ou equivalente) rodando no sample de toda spec de declaração: 0 anomalias bloqueantes.
- **Checagem cruzada automática** WTC × DD × Payslip × specs × CCG: mesmo código de rubrica, mesma regra de tributação, mesmo valor.
- Comparar o texto de controles da spec com a lista oficial de mensagens/controles da norma (conta: presentes / faltando).
- Auditor adversarial independente (nunca quem construiu) antes de cada decisão humana; veredito Upheld / Upheld with corrections / Overturned / Insufficient evidence.
- Matriz de rastreabilidade com a categoria NONE explícita: mostrar o que ninguém testou.
- Provas de validade da própria validação: independência, cobertura, mutação, conferência com o motor ao vivo.

### 5.5 Entrega / promoção
- Humano no loop para escrita: correções como DRAFT/redline; nunca sobrescrever artefato vivo (`CLAUDE.md`).
- Nome: `{CC}-{TYPE}-{SEQ}-v{MAJOR}.{MINOR}[-DRAFT-{TICKET}-{YYYY-MM-DD}].ext`; versão atual = maior não-DRAFT; ID interno = nome do arquivo.
- **Versão única de pacote:** todos os artefatos de uma entrega com a mesma versão e data.
- **Trilha de auditoria fora do entregável:** changelogs, diffs, ROW-REMAP e notas em pasta própria (`docs\history\` aqui; `_audit\` proposto). O usuário pediu o pacote "sem sinal de retrabalho"; a forma limpa de fazer isso é separar a trilha de auditoria por construção, não reescrever a história do artefato à mão.
- Rodar `release_crosscheck.py` (versão ≠ pacote, palavras de revisão, IDs de achado, nomes de pessoas/reuniões, datas de carimbo, tracked changes, comentários, abas ocultas) e `finalize_release.py` (metadados; rodar **por último**, porque o recálculo do Excel reescreve as propriedades).
- Promoção com arquivamento (nada apagado), **log MD5** e verificação byte a byte do que foi promovido; regenerar a skill a partir dos finais e conferir o hash de cada referência.
- Propagação explícita: quando a spec muda de linha, re-apontar o WTC "Form Reference Guide" (`ROW-REMAP.csv`; 119 referências verificadas); quando o DD ganha campo, promover DD e specs juntos.
- Entregáveis em inglês, sem referência a reuniões, transcrições ou notas; sem PII; sem segredos.

### 5.6 Operação / infraestrutura
- Fatos do pipeline (número de estágio, ID de checagem, versão de script) são lidos do disco, nunca da memória (`CLAUDE.md`).
- O Drive pode estar desatualizado em relação ao pipeline (DD e WTC); diff célula a célula antes de revisar e decidir qual é a referência.
- Conector do Google Drive caiu (re-autenticação) e foi tirado do escopo; manter cópias .xlsx de referência locais.
- Gravar no `mercans-pipeline` chegou a ser bloqueado pelo classificador; promoção rodada pelo usuário com scripts (`promote.py`, `promote2.py`).
- Arquivo aberto no Excel trava a finalização de metadados (DSN Mensuelle aberta em 07/10).
- Python com `-I` e `sys.stdout.reconfigure(encoding='utf-8')` no Windows; zsh não aceita comentários `#` colados; amostras DSN em ISO-8859-1 com CR-LF (um patch pode remover o CR).
- Economia de tokens: Haiku para rodar, Sonnet para pesquisar/codar, Opus só nos portões.
- Instrução permanente do usuário (memória `feedback-always-recommended.md`): aplicar a opção recomendada sem pedir escolha, exceto bloqueios do harness e ações externas fora de escopo (G7, upload ao Drive).
- Guias passo a passo em HTML interativo para qualquer tarefa com mais de dois passos (`CLAUDE.md`).
- Sessões longas estouraram contexto; consolidar o estado em `HANDOFF.md` antes de trocar de sessão.

---

## 6. Recomendações concretas para o próximo pipeline (gates acionáveis)

| # | Gate / checagem | Estágio | Critério de bloqueio | Origem na França |
|---|---|---|---|---|
| G-01 | Matriz de populações e situações especiais preenchida | Escopo (Estágio 1) | Nenhuma linha vazia; "não se aplica" exige justificativa com fonte | D-11, D-17, D-12, D-18, D-19, F-05, F-09 |
| G-02 | C31 ampliada: residente/não residente **também nas contribuições sociais** | Escopo/Pesquisa | Regra de seguridade para não residente fiscal declarada e citada | D-17 (COTAM) |
| G-03 | Registro de fatos com vigência: cada valor com instrumento, artigo, data de início/fim, URL aberta na build | Pesquisa | Valor sem data ou sem URL aberta = FAIL | F-23, F-24, F-03, WTC F-16, DD F-34 |
| G-04 | Varredura de atualidade (notícias da autoridade desde a data da pesquisa até a entrega; norma do ano seguinte publicada?) | Pré-entrega | Lista de mudanças com veredito "afeta / não afeta" | F-16, F-18, F-03 (2027), CT2027.1.2 |
| G-05 | Recalcular todo exemplo resolvido a partir dos parâmetros do artefato | Construção do CCG | Diferença > 0,01 = FAIL | F-05, F-11, F-13, F-29, Ex. 3, SB-06, SB-19 |
| G-06 | Suíte de validação externa (Estágio 9b): oráculo independente × simulador oficial ou exemplos oficiais | QA | ≥ 98 % das linhas (meta do plano) e toda diferença com defeito classificado e fonte primária | Suíte FR: 94,7 % → 97,6 % |
| G-07 | Teste 0 por artefato (CCG, WTC, DD, specs) | QA | ≥ 95 %; cada falha vira defeito | 77,5 % → 98,0 % |
| G-08 | Validador oficial de formato sobre o sample de cada spec de declaração | Specs (Estágio 3) | 0 anomalias bloqueantes | 51 → 0 |
| G-09 | Contagem de controles: spec × lista oficial de mensagens da norma | Specs | 0 controles faltando; nenhuma célula cortada | 71 faltando na DSN-001 |
| G-10 | Árvore de blocos e ordem por natureza de declaração | Specs | Ordem da spec = ordem do arquivo da norma | SD-01 |
| G-11 | Validação de identificadores fictícios (Luhn SIREN/SIRET, NIR × sexo/data/departamento, códigos em tabela de referência) | Specs/Payslip | 0 inválidos | SD-04 |
| G-12 | Todo campo obrigatório com fonte de dado (DD ou dado mestre); proibir "produced by the payroll calculation" para dado de configuração | Specs × DD | 0 obrigatórios sem fonte | SD-02, "NO DD COUNTERPART" |
| G-13 | Coerência cruzada automática WTC × DD × Payslip × specs × CCG (código de rubrica, flag de tributação, valor, versão citada) | QA | 0 divergências | WTC F-06/F-07/F-11/F-13/F-24, Payslip F-29/F-33, commit `1193039` |
| G-14 | Conteúdo estatutário mínimo do contracheque (lista do R3243-1 ou equivalente) verificada depois de qualquer mudança de layout | Payslip | 100 % dos itens presentes; líquido recalculado | Payslip F-25..F-28 |
| G-15 | Proibir edição manual de binário gerado; diff "regerar = emitido" | Construção | Regeneração idêntica célula a célula (aqui: 15/15) | Patches pós-build; SB-19 |
| G-16 | Detector de truncamento/perda: comprimento máximo de célula, contagem de linhas de Version Control, linhas estatutárias antes × depois | Construção | 0 perdas | SD-03, SD-05, Payslip |
| G-17 | Design gerado a partir da research, com teste de expressões (condição que nunca dispara, referência para frente, unidade de taxa) | Design | 0 condições mortas | Design R-05, R-35, R-42, R-44 |
| G-18 | Varredura de sobras de outros países e de jargão interno (prefixos BE-/NSSO/FIN-, nomes de outros países fora de contexto legal, "STEP", "check C", caminhos) | Release | 0 ocorrências | commits `3145c96`, `c480af7` |
| G-19 | Versão única de pacote + nome = capa = Version Control = ID interno | Release | 0 divergências | F-19, F-37, SD-05, Report Matrix 1.4–1.6 |
| G-20 | Empacotamento limpo por construção: trilha de auditoria em `_audit\`; `release_crosscheck.py` + `finalize_release.py` | Release | 0 achados | commits `36de79c`, `03a4f1b` |
| G-21 | Promoção com log MD5 e verificação byte a byte; skill regenerada com conferência de hash por referência | Promoção | 100 % iguais | Desvio pós-promoção; 49 → 0 inconsistências |
| G-22 | Citação conferida no texto (artigo em vigor, não revogado) | Pesquisa/QA | 0 artigos revogados ou inexistentes | D-08, F-06, F-25, F-26, F-28 |
| G-23 | Afirmação "fonte não obtida" cruzada com SIR/runbooks da mesma build | QA | 0 lacunas falsas | SA-25, SB-16 |
| G-24 | Defeitos do simulador oficial registrados como "defeito do motor", sem alterar a research | QA | Toda divergência com classe | D-02, D-04, D-05, D-12..D-16, D-18 |
| G-25 | Registro no log de falhas (F40+) de cada causa acima, com a checagem que a previne | Contínuo | — | Plano de ação, Frente F |

**Ordem recomendada** (do plano de 2026-10-07): primeiro o gerador de specs (rápido, corrige tudo de uma vez), depois o Estágio 9b, depois a matriz de cobertura/atualidade, depois `facts.json` único e release limpo, e por fim um **piloto num país novo** medindo os indicadores (linhas iguais ao simulador ≥ 98 %, Teste 0 ≥ 95 %, 0 anomalias no validador, 0 controles cortados, 0 inconsistências entre artefatos, < 10 mudanças por artefato depois da entrega).

---

## 7. Pendências / itens abertos

| Item | Situação | Onde |
|---|---|---|
| D-19 presidente de SAS (Apec/CDS) | Inconclusivo; falta texto literal da Agirc-Arrco | `DD\D-19-sas-president-apec-cds.md` |
| SA-25 DPAE: C_APPLICATION para o canal API e lista C_URSSAF | Sem fonte acessível ("DUE + 1 blanc" vs 'CFT') | `RV\FR-open-notes-research-2026-10-06.md` |
| SA-45 sinal do solde TA 075 / CTP 996-997 (Population Rules D11) | Aberto (077/078 resolvido: sinal negativo correto) | idem |
| SB-33 BPIJ por API / esquema XML | Aberto | idem |
| Tamanho do registro do formato 120 da DPAE | Única afirmação pendente do Teste 0 final (site da URSSAF fora do ar) | transcrição 2026-10-09 13:06 |
| C46 (fatos com marcação `[[FACT:…]]` nos artefatos) | O arquivo de fatos passa (17 fontes, 171 fatos, 8 não resolvidos), mas os artefatos ainda não citam os fatos | transcrição 2026-10-09 12:48 |
| 8 fatos não resolvidos | Ex.: dedução de 10 % do 182 A; equivalente bruto de 8.037 do teto de horas extras; textos do Légifrance que bloqueiam acesso automatizado | idem |
| Net social 2027 | Depende da publicação do decreto (BOSS 02/10/2026, minuta); reverter a regra de 2026 a partir de 01/01/2027 | revisão do CCG F-03 |
| Watch item CSS R433-2 | Nova versão (Décret 2026-909, afastamentos a partir de 01/11/2026) mostra "0,226 %" em vez de 0,834 %; não verificado | `RV\FR-WTC-DD-flags-research-2026-10-06.md` |
| Comparação com a saída de folha da Mercans (Teste 4) | Fora de escopo por decisão | INDEX.md |
| G7: YouTrack (6 tickets), 11 issues upstream modele-social, upload ao Drive | Rascunhos prontos, não enviados | `FRV\docs\g7-drafts\` |
| Teste 5 (simuladores do Code du travail numérique e impots.gouv) e Teste 6 (modo teste da net-entreprises) | Não executados | `FRV\docs\test-plan.md` |
| Cobertura da suíte | Maior parte do que varia entre contracheques (BIK, rescisão, aprendiz, regularização acumulada) sem teste automático | traceability E2 |
| Lacunas de suíte | Caso de cadre em tempo parcial acima de 4 × PMSS prorrateado; caso perto do teto de 7.500 (oráculo já alinhado ao líquido) | `TEST-DESIGN-CORRECTIONS.md` itens 4 e 5 |
| SIR | Só achados (SIR-01..09, F-37); sem redline | `FRV\docs\g7-drafts\README.md` |
| Overlay de patches do builder | Deve ser incorporado aos scripts e retirado | `RL\specs\README.md` §5.6 |
| Piloto do pipeline melhorado | Fases 0–5 feitas; Fase 6 aguardando escolha do país (recomendado: Portugal) | `C:\Users\instituto\mercans-pipeline\IMPROVEMENT_LOG.md`; transcrição 2026-10-09 |
| Push ao GitHub / skill no Claude.ai | Commits locais não enviados (7 na última contagem); reenviar `final\skill\payroll-compliance-france.zip`, que mudou depois do commit `1193039` | transcrição 2026-10-09 |
