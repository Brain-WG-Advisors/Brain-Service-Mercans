# Consolidado 2026-10-23 — 10 tickets herdados da Shruti (agora wgomes)

> Janela Suporte. Uma nota por ticket nesta pasta. Só leitura: nada gravado no YouTrack, Drive ou arquivos compartilhados. Afirmações centrais relidas pela janela na fonte primária (coluna "Conferido").
> Insumos: tickets em `raw/tickets/api/2026-10-23-ex-skamble/` (sem comentário novo desde 22/10, só a troca de Assignee), anexos em `raw/tickets/api/anexos/<ID>/`, exportações do Drive em `raw/docs/drive-exports/2026-10-23/`, fontes novas em `raw/docs/oficiais/{EG,SG,TW,DZ}/`.
> Fora deste lote: HRBS-15253 (Lituânia) fica com a janela Pipeline por decisão do usuário (aviso de pipeline-c4, 23/10).

## Painel
| # | Ticket | Pergunta | Veredito | Conferido na fonte | Nota |
|---|---|---|---|---|---|
| 1 | HRBS-15790 Egito (todas as entidades; jan/2027) | Piso 3.200 / teto 19.300 / EE 11,5% / ER 19,25% a partir de 01/01/2027 | **Os 4 números estão certos.** Alíquotas: Lei 148/2019 art. 19 (+1 ponto a cada 7 anos, meio a meio; 1º aumento em 01/01/2027). Piso/teto: Regulamento (Decreto PM 2437/2021) art. 53, +15% ao ano com arredondamento para a centena acima. Atual = 18,75% (o 18,25% do texto original era erro). Anúncio da NOSI de 2027 ainda não saiu | Art. 19 lido na imagem da página 25 ✅; contas 2.700→3.200 e 16.700→19.300 refeitas ✅ | [[HRBS-15790-egito-SI-2027]] |
| 2 | HRBS-16029 Singapura/GSK | 62866 (Childbirth Allowance) deve ser CPF-able (e SDL)? | **Sim, CPF = Yes como AW** (pagamento único por evento), não OW como o Hayat pediu. SDL segue a base de wages do CPF (SDL Act s.2), teto de $4.500/mês (s.3(2)). 62878 idem se pago em dinheiro; 62867–62870 ficam | WTC V4.2 linhas 685 (62866 CPF No/NA), 697 (62878), 465 (62590 Yes/AW) ✅; SDL s.3(2) ✅; definição de AW ✅ | [[HRBS-16029-singapura-SDL-62866]] |
| 3 | HRBS-15941 Taiwan/British Council | Subsídio de creche anual: imposto, LI/EI/NHI/LP, payroll ou fora | **Tributável** (Income Tax Act art. 14 Cat. 3 item 4: "各種補助費"); formato 50 no anual. **Fora da base de LI/EI/LP e do insured amount NHI** se anual e discricionário (LSA ER art. 10 item 4: "子女教育補助費"). SNHI do empregado não; SNHI do empregador (art. 34) sim. Pagar pelo payroll com wage type próprio | ITA art. 14 ✅; LSA ER art. 10 ✅ (⚠️ "creche" não aparece pelo nome) | [[HRBS-15941-taiwan-subsidio-creche]] |
| 4 | HRBS-3466 Argélia/Henkel (prazo dez/2026) | Spec da DAS (um por local, arquivos E/S, nome, campos) | **Spec v2.1 certa no layout, não pronta para o dev**: falta a regra de geração por local (empregado → local → nº CNAS), 6 campos fora do DD, wage type da base CNAS, `#ERROR!`, prazo/penalidade errados. Lei: DAS "dans les trente (30) jours qui suivent la fin de chaque année civile", por trimestre | Guia CNAS (nomes D20E/D20S .TXT, cêntimos, sem separador) ✅; Loi 83-14 art. 14 (JORADP 05/07/1983 p. 1218) ✅ | [[HRBS-3466-argelia-DAS]] |
| 5 | SR-105 TW SI Salary Adjustment | Spec review + lacunas | **Não pronta**: nenhum mapeamento, M/C/O vazios; "Quarterly" errado (prazos de ago/fev); campo 11 = média de 3 meses sem bônus anual (precisa WT novo) | (amostra pelo agente) | [[SR-105-taiwan-SI-salary-adjustment]] |
| 6 | SR-106 TW SI Termination | idem | **Quase pronta**: mapeada, mas `residential_status` usado como nacionalidade (campos 8/10/11), nomes de campo inexistentes no DD (13/14), campo 15 omitido, guia de 2015 | (pelo agente) | [[SR-106-taiwan-SI-termination]] |
| 7 | SR-107 TW SI Joiner | idem + trocar 58212 | **Não pronta**: 27 campos, **0 mapeados**; 58212 = "Total Number of Tax Dependents" (sai); 58139 não existe no WTC; aba "New Specification" é de imposto | Spec Joiner 27/0 ✅; WTC 58212/58139 ✅ | [[SR-107-taiwan-SI-joiner]] |
| 8 | SR-108 TW SNHI | idem | **Não pronta**: posições ok com o formato NHIA tipo 62, mas 13 conflitos (periodicidade, BIG5, ano ROC, declaration number, 58139); totais da seção C = soma do arquivo, não YTD | (pelo agente) | [[SR-108-taiwan-SNHI]] |
| 9 | SR-109 TW Payslip | idem | **Quase pronta**: OT por tipo de dia resolvido; falta 議定工資總額 (LSA ER art. 14-1), data de pagamento, endereço, totais; ID em `$hr.id_card_number`; reteste numa entidade de Taiwan | (pelo agente) | [[SR-109-taiwan-payslip]] |
| 10 | SR-110 TW Tax Report | idem | **Não pronta**: as 3 issues do Mohit não estão na spec; campo 9 mapeado errado (58100+58105); formato oficial UTF-8 com "|"; "NORTIN" → "NOTIN"; pensão voluntária = 2517 | Spec linha 11 (Tax Exemption Amount → 58100+58105, "Withheld tax amount") ✅; linha 34 'NORTIN' ✅ | [[SR-110-taiwan-tax-report]] |

## O que precisamos fazer
| Prioridade | Ticket | Ação | Quem | Depende de |
|---|---|---|---|---|
| 1 | HRBS-15790 | Responder ao Mustafa: os 4 números confirmados, com art. 19 e art. 53 | nós (rascunho na nota) | ok do usuário |
| 1 | HRBS-15790 | Task CT (Development task, Epic Regulation Update, Mohit): Reg. 23 faixa <60: EE 10% → 10,5%, ER 14,75% → 15,25%; piso/teto anuais 32.400/200.400 → 38.400/231.600; em produção antes de 08/01/2027 sem afetar dez/2026 | nós (draft como o da CI) + Mohit | ok |
| 1 | HRBS-15790 | Atualizar CCG/WTC/DD (piso/teto e alíquotas com vigência 2027; fonte = art. 53 do Regulamento, não "ministerial decree") | nós (local → Drive com ok) | — |
| 2 | HRBS-3466 | Responder à Vaishali/Mohit: status, pedir nºs CNAS/centros/endereços dos 3 locais e decisão J × M; ETA proposto (spec ao dev 06/11, testes 04/12, UAT 15/12) | nós | ok |
| 2 | HRBS-3466 | Completar a spec v2.1 → v2.2 (geração por local, mapeamentos, prazo 30 dias, penalidade, `#ERROR!`) | nós | dados dos locais |
| 3 | HRBS-16029 | Responder ao Hayat (AW, não OW); WTC V4.3: 62866 CPF Yes / Additional Wages (+ 62878 se aprovado) + task de configuração | nós + Config | ok; escopo (62878, 62983) |
| 3 | HRBS-15941 | Responder ao Archit/Merlin (call já passou); propor wage type próprio no WTC V2.9 | nós | ok; fatos do cliente (valor, contratual?, comitê?) |
| 4 | SR-105 a SR-110 | Aplicar as propostas numa cópia de cada spec (azul claro), devolver ao Mohit com comentário curto | nós | ok do usuário; guias atuais do NHIA (eservice.nhi.gov.tw bloqueia daqui: pedir a alguém em Taiwan) |

## Decisões que são do usuário
1. HRBS-16029: escopo da V4.3 — só 62866, ou também 62878 e 62983 (Maternity Allowance com CPF No, CPFB diz Yes)?
2. SR-105 a SR-110: aplicar as propostas nas specs agora (local → Drive com ok) ou devolver ao Mohit só a lista?
3. HRBS-15790: criar o draft da task CT para o Mohit agora (como a da CI)?

## Achados fora do pedido (para os hubs no "fecha a sessão")
- Egito: CCG cita "ministerial decree" para piso/teto e prazo de recolhimento diferente do art. 121(1); 2.700/16.700 escritos à mão no WTC/DD; Training Fund com duas leituras de base que divergem em 2027; atividade de risco pode chegar a 19,75%; diretores 21% → provável 22% (dedução, sem texto).
- Singapura: 62866 > $200 é tributável (IRAS) e está Tax = No (subdeclaração no IR8A); 62983 Maternity Allowance CPF No × CPFB Yes; 62844/62854/62855/62859 com "CPF payable" na Remark e CPF = No; guia interno com teto OW de $6.800.
- Taiwan: `residential_status` usado como nacionalidade em várias specs; DD com `labor_insure_id`/`health_insure_id` como Number (perde zero/letra); 58009 sem o bônus anual 6220x (NHIA inclui 年終獎金 no SNHI); SOP com limites de 2025; WTC sem wage type de creche.
- Argélia: CCG diz DAS em dinares (guia: cêntimos); WTC DZ sem códigos Mercans; HRBS-11592 (base SS da Henkel) afeta a DAS.
- Hubs inexistentes: Taiwan, Argélia (Egito e Singapura existem).

## Lacunas
- Egito: anúncio NOSI 2027; Lei 11/2026; faixa 60+ da Reg. 23.
- Taiwan: guias atuais do NHIA (bloqueados daqui); 要點 do MOF 113/114; fórmulas dos PEs SNHI no WTC; interpretação oficial citando "托兒".
- Argélia: nºs CNAS dos 3 locais; alterações da Loi 83-14 após 2004; DAS 2025 submetida.
- Singapura: base 58534 do SDL (estrangeiros?) — confirmar com Mohit/Ruchi.
