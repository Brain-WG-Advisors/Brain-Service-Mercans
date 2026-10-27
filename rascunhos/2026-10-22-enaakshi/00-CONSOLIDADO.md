# Consolidado 2026-10-22 — 7 tickets herdados da Enaakshi (agora wgomes)

> Janela Suporte. Análises profundas por ticket nesta pasta (uma nota cada). Só leitura: nada gravado no YouTrack, Drive ou arquivos compartilhados. Afirmações centrais relidas pela janela na fonte primária (coluna "Conferido").
> Insumos: tickets em `raw/tickets/api/2026-10-22-for-evats/`, anexos em `raw/tickets/api/anexos/<ID>/`, artefatos exportados do Drive em `raw/docs/drive-exports/2026-10-22/`, fontes novas em `raw/docs/oficiais/<CC>/`.

## Painel
| # | Ticket | Pergunta | Veredito | Conferido na fonte | Nota |
|---|---|---|---|---|---|
| 1 | HRBS-16252 Iêmen/BH (trava UAT) | Base do SS: mensal × janeiro; só basic?; transporte; joiners/leavers; 9% | **Base = salário de janeiro de cada ano** (ou do mês de admissão), básico + allowances permanentes e estáveis (transporte dentro); fora bônus de incentivo e OT. Sistema (mensal) e CCG divergem. Cliente certo em "janeiro", errado em "só basic" | Página oficial GCSS (seguro obrigatório): itens 1 e 3 ✅. Lei 26/1991 arts. 14/15/27/50 lidos pelo agente (PDF digitalizado) | [[HRBS-16252-iemen-base-SS]] |
| 2 | HRBS-16015 Iraque/BH | OT entra na base do SS? (Suman: não) | **Federal: entra** (Lei 18/2023 art. 1 Eleventh "allowances of all kinds"; art. 15; Labour Law 37/2015 art. 1(14) "wages due for the overtime"). KRI: fica fora (Lei 39/1971). O print do Suman é o nosso CCG §2.1, frase sem fonte | Lei 18/2023 EN arts. 1 e 15 ✅; Labour Law art. 1(14) ✅; CCG linha 217 ✅ | [[HRBS-16015-iraque-OT-SS]] |
| 3 | SR-369 Líbia SUF | 1.00% × 1.000% | **1.00%** (spec J14/K14/T14, comprimento 5). O 1.000% vem da aba Sample File da nossa spec (formato `0.000%`). Lei 20/2007 art. 3(1) = 1%; sem formulário oficial | Spec J14/K14/T14/I14 e Sample E14:E15 ✅ | [[SR-369-libia-SUF-taxa]] |
| 4 | SR-367 Líbia PIT | Gross inclui Exempt Income? | **Sim** (Lily certa). M25: base = Gross − Exempt − ...; com Gross = 58008 tributável o isento sai duas vezes; M18 já descreve Gross total | Spec M18/M19/M25/T18 ✅ | [[SR-367-libia-PIT-gross]] |
| 5 | HRBS-15863 Gana/BH | Teto de 15% do bônus: anual × YTD; lógica por cenário | **Anual**: L.I. 2244 reg. 5(2) "fifteen percent of the annual basic salary", reg. 5(6) "basic salary ... for the year of assessment to which the bonus relates"; GRA Practice Note DT/2016/011. Lei não traz fórmula para mudança de salário/joiner/leaver: lógica proposta é design | L.I. 2244 reg. 5(2) e 5(6) ✅; exemplo GRA ✅ | [[HRBS-15863-gana-bonus-15pct]] |
| 6 | HRBS-16234 Filipinas/McDermott (go-live 01/01/2027) | Maternity Benefit (79406) e Salary Differential (79452): imposto, 2316, SSS, PhilHealth, HDMF | **Imposto/2316 corretos** (isentos: NIRC 32(B)(6)(e); RR 2-98 2.78.1(B)(1)(e); RMC 105-2019). **PhilHealth divergente** (base = MBS, não reduzida por licença; prêmio continua na licença: PC 2020-0005 IV.F/V.D). SSS/HDMF do benefício: divergente pela definição; do differential: ⚠️ sem norma | WTC V2.9 linhas 384/392 ✅; RMC 105-2019 ✅. PhilHealth PC (digitalizado) lido só pelo agente ⚠️ | [[HRBS-16234-filipinas-maternidade]] |
| 7 | SR-472 Dinamarca eIndkomst | Submission ID (IndberetningsID) nos registros 3101/4101/5000 | **ID único gerado por nós** em cada 3101, 4101 e 5000 (Teknisk vejledning v11.6 §3.2); estorno só por IndberetningsID, nunca pelo Hoved-ID. Spec v3.5 errada: L64 mapeia SE-nr; ReferenceID aponta para o Hoved-ID | Teknisk vejledning §3.2 ✅ | [[SR-472-dinamarca-submission-id]] |

## O que precisamos fazer
| Prioridade | Ticket | Ação | Quem | Depende de |
|---|---|---|---|---|
| 1 | HRBS-16252 | Responder a)/d)/e) + pergunta do Aasim (base de janeiro, básico + allowances fixas, transporte dentro) | nós (rascunho na nota) | ok do usuário |
| 1 | HRBS-16252 | Configuração: base anual de janeiro; admissão = salário do mês de admissão; mês de saída sem contribuição | Suman / Config | resposta |
| 1 | HRBS-16252 | Corrigir CCG Step 2/5.2 (frases "fixed insured wage ... transport excluded" contraditórias), WTC linhas 307–308, DD, spec YE-SSF-001 | nós (local → Drive com ok) | — |
| 2 | HRBS-16015 | Responder: OT entra no SS federal (corrige o Suman); pedir a região das entidades (flag 58219) | nós | ok do usuário |
| 2 | HRBS-16015 | Corrigir CCG §2.1 e WTC v1.1 (OT 62110–62139 etc. SS Federal = Yes); Design (iq.json) exclui 6211–6213% | nós + Mohit (design) | resposta |
| 3 | SR-369 | Responder 1.00%; corrigir formato da Sample File (E14:E15 `0.00%`), v1.1 | nós | ok |
| 3 | SR-367 | Responder sim; ajustar textos M18/M19/G19/M21/M25 e Sample N16:N17, v1.1; pedir reteste com empregado com renda isenta | nós + Lily | ok |
| 4 | HRBS-15863 | Responder ao Mohit: anual, com a lógica por cenário; perguntar a que ano o bônus de março se refere | nós | ok |
| 4 | HRBS-15863 | Corrigir regs 9288161/9288141 (Mohit), WTC 2572/58120–58124, CCG (citar reg. 5; tirar "YTD accumulator" ambíguo) | Mohit + nós | resposta |
| 5 | HRBS-16234 | Responder ao Khoi com a tabela por elemento; WTC: PhilHealth/SSS/HDMF de 79406 (e 79452 após confirmação); 13º inclui 79452 | nós + Config | ok; DA 01-2019 e SSS Circ. 2019-009 (baixa manual: dole.gov.ph bloqueia) |
| 6 | SR-472 | Responder à Ruchi (prazo 30/10); spec v3.6: L64, ReferenceID L55/L65/L73 | nós + Ruchi/dev | ok |

## Achados fora do pedido (vão para os hubs no "fecha a sessão"; não para os tickets)
- Iêmen: 4% de acidente de trabalho só do empregador (Lei 26/1991 art. 27) — confirmar se é cobrado; DD sem campo "SI Insured / Contractual Wage".
- Iraque: CCG/WTC/Design divergentes em leave pay (62300/62305); vigência da Lei 18/2023 = 2023-11-26; Design com piso/teto anuais; alíquota de petróleo 25% não checada.
- Líbia: base legal da spec SUF só PwC; exclusão de isentos da base do SUF ⚠️ sem fonte; arredondamentos do dev × spec; mudança de 15/09 não versionada.
- Gana: CCG não cita L.I. 2244 reg. 5; simulação do Drive (aba "Terminated employee") usa básico mensal; 20% bônus de não residente não conferido.
- Filipinas: 62109 com PhilHealth = Yes; licenças pagas com flags de PhilHealth inconsistentes; Payslip Display = NA em 79406/79452; arquivo V2.9 com VC "3.0".
- Dinamarca: marcador "R" em off-cycle (L71); Sample com 4 registros 5000 com o mesmo ID; Nulangivelse "1/0"; Forud/Bagud no 3101; Indberetningsvejledning já v17.0.
- Hubs inexistentes: Iêmen, Iraque, Líbia, Gana (criar pela janela geral).

## Lacunas
- Iêmen: regulamento executivo e decisão ministerial das allowances não localizados; árabe da lei transcrito de imagem.
- Iraque: região das entidades; texto árabe da Labour Law; salário mínimo (fonte primária).
- Filipinas: DA 01-2019, SSS Circular 2019-009, norma do HDMF; RMC 105-2019 e 2316 só em espelho.
- Gana: Act 896 consolidado; L.I. 2244 em cópia da GNPC.
