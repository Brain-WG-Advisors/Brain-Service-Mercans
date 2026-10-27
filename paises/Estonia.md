---
tipo: pais
codigo: "EE"
etapa_research: "concluida"
etapa_research_data: 2026-08-27
etapa_design: "aguardando"
etapa_design_data: 
etapa_producao: 
etapa_suporte: "sem ticket no hub"
etapa_suporte_data: 
ccg: 
ccg_data: 
wtc: 
wtc_data: 
dd: 
dd_data: 
report_specs: 
report_specs_data: 
sir: 
sir_data: 
payslip: 
skill: "payroll-compliance-estonia"
tickets_abertos: 
tickets_conferidos_em: 
atualizado_em: 2026-10-27
---
# Estônia

> Hub do país. Índice: [[00-INDEX]] · Skill: `payroll-compliance-estonia` · Fronteiras: [[fronteiras]]

## Situação
| Etapa | Status | Data | Observação |
|---|---|---|---|
| [[research-pipeline]] | ✅ | 2026-08-27 | skill compilada (data da pesquisa no QA da skill) |
| [[design]] | ⏳ | | |
| Produção (outro time) | — | | |
| [[suporte]] | ⏳ | | |

## Ficha do país (da skill)
> Resumo do que mais importa para o serviço. Fonte: skill `payroll-compliance-estonia`, lida em 2026-10-02. Valores exatos e tabelas: ler a skill. Se divergir, vale a skill.

- **Escopo:** ano fiscal 2026, setor privado, EUR; inclui membros de conselho e prestadores de serviço (tratamento diferente). Fora: servidores públicos, militares, juízes, parlamentares, FIE (autônomos), contas de negócio. A skill menciona que existe um payslip generator 2026 da Estônia em outro ponto do pipeline (a skill não derivou dele).
- **Órgãos:** Maksu- ja Tolliamet (EMTA); também Eesti Töötukassa, Tervisekassa, Sotsiaalkindlustusamet, Tööinspektsioon.
- **Relatórios principais:** formulário TSD mensal (EE-RPT-01) com anexo 1 (EE-RPT-02) e anexo 4 de fringe benefits (EE-RPT-04); registro de emprego TÖR (X-tee); ESD e INF (INF 14 é o mais relevante); certificado de rescisão da Töötukassa. A partir de 1 out 2026, TSD passa a ser data-based (anexos 1 e 2 se fundem, XBRL GL; CSV tolerado até fim de 2027).
- **Confiança da skill:** "READY FOR REVIEW", com 5 seções abaixo do piso de 95% e 1 não especificável. Núcleo de cálculo 97–99%. Abaixo do piso/derivado: layout XBRL GL (NOT SPECIFIED, §3.1); layouts ESD/INF (40% DERIVED); mínimos de acordos coletivos setoriais (50%); benefícios parentais PHS (60%, contido porque paga a Sotsiaalkindlustusamet); pesquisas da Statistics Estonia (50%); códigos `EE-###` do WTC são placeholders (não há mapeamento Mercans).

**Armadilhas confirmadas**
1. Imposto de renda é 22% (24% é IVA); o "security tax" de 2% não foi aprovado sobre salários; 10,64% é repasse ao município, nunca taxa de folha (engine) → `01-ccg.md`
2. Ordem de dedução estatutária: IR = 22% × max(0, bruto − desemprego 1,6% − II pilar 2/4/6% − alívio III pilar − isenção básica); social tax nunca entra na base do empregado (engine) → `01-ccg.md` (TSD anexo 1 código 1170)
3. Isenção básica só mediante requerimento, um pagador, teto 1/12 por mês, sem carry-forward; €700/mês (€8.400/ano) em 2026; "tax hump" (TuMS § 23 (2)–(5)) revogado em 1 jan 2026 (engine) → `01-ccg.md`
4. Atingir idade de aposentadoria em qualquer momento do ano muda o ANO INTEIRO para €776 (tipo 650 desde 1 jan; tipo 610 não se aplica); verificar no TÖR (engine) → `01-ccg.md`, `04-reports-spec.md`
5. Kuumäär €886 (social tax mínimo €292,38) não é o salário mínimo e part-time voluntário não escapa do piso (só encurtamento legal TLS § 43 (4)/(6) e casos de SMS § 2 (4)) (engine) → `01-ccg.md`
6. Multi-empregador: quem detém o requerimento da isenção carrega o social tax mínimo (SMS § 2 (2¹)); certificado atualizado até dia 5 do mês seguinte (engine) → `01-ccg.md`
7. Salário mínimo 2026 subiu em 1 ABRIL: €886/€5,31 por hora até 31 mar; €946/€5,67 desde 1 abr (VV 23.03.2026 nr 36) (engine) → `01-ccg.md` §12
8. Quatro encargos, quatro bases: severance legal (TLS § 100) = IR sim, social tax sim, desemprego NÃO, II pilar sim; auxílio-doença do empregador dias 4–8 = só IR (engine) → `02-wtc.md`
9. Membro de conselho: sem prêmio de desemprego, mas COM II pilar e social tax 33% (tipo TSD 21) (engine) → `02-wtc.md`
10. Taxa do II pilar é eleição por empregado (2/4/6%, 0% possível após reforma de 2021), consultar por isikukood (engine) → `01-ccg.md`
11. Prêmio de desemprego do empregado para no mês da idade de aposentadoria; o do empregador (0,8%) continua: 0% / 0,8% (engine) → `01-ccg.md`
12. Auxílio-natalidade do empregador (€3.500 por criança; €7.000 gêmeos) é livre só de imposto de renda; social tax, desemprego e KoPS incidem (tipo TSD 14) (engine) → `02-wtc.md`
13. Fringe benefits são imposto do empregador, gross-up 22/78 = 28,2051%, social tax 33% sobre benefício + seu IR, sem desemprego nem II pilar, reportados agregados no TSD anexo 4; carro €1,96/kW/mês (€1,47 se >5 anos); saúde €400 por ano (engine) → `01-ccg.md` §7
14. Hora extra: padrão legal é folga hora a hora (TLS § 44 (6)); 1,5× só se acordada compensação em dinheiro; noite 1,25×; feriado 2×; jornada agregada mede no fim do período (engine) → `01-ccg.md`
15. M2M via X-tee (`tsd/confirmTsd`, `getTsdStatus`, `getTsdFeedback`, `mkrliides/uploadMime/v1`, `tor/TOOTREG/v2`, sem SLA); em 1 out 2026 muda para XBRL GL e o XML atual deixa de valer → `03-sir.md` §2.2, `04-reports-spec.md` §8
16. Não existe payslip legal; TLS § 28 (2) 12) só exige dados salariais a pedido; a obrigação de divulgar está no contrato (TLS § 5 (1) 5) → `06-payslip.md`

**O que mais dá errado** (do QA)
- "Imposto de renda da Estônia 2026 é 24%" é falsidade ativa e perigosa (§4.1).
- Guia de preenchimento do TSD anexo 1 obtido é a edição 2025 (92%, §4.5); €126,87 de teto diário de doença não é número estatutário (§4.6); códigos 4010 e 4020 do anexo 4 não localizados.
- Auxílio-natalidade confundido com "isento de tudo" (§4.7); excesso de diária vs excesso de compensação de carro seguem rotas diferentes (§4.9, 85%).

**Lacunas abertas / não confirmado** (candidatos a ticket ou nova pesquisa)
- §3.1: layout de campos do TSD XBRL GL (data-based, desde 1 out 2026): documentação técnica da EMTA no 4º tri de 2026; não inventar nomes de elementos.
- §3.2: layouts ESD e INF (40%); INF 14 desconhecido.
- §3.4: mínimos de acordos coletivos setoriais/estendidos (~50%).
- §3.5: benefícios parentais PHS (~60%); §3.6: obrigação de relatório à Statistics Estonia (~50%).
- §4.3: tratamento de prêmio de desemprego sobre sentenças judiciais/comissão de disputas (80%).
- §4.4: limbo II pilar das contribuições do empregador ao III pilar (70%).
- §4.8: compensação de férias não gozadas na rescisão: tipo TSD 10 ou 33 (75%).
- §4.10: algoritmo do dígito verificador do isikukood (94%, EVS 585:2007 não lido).
- Certificado de rescisão da Töötukassa (formulário prescrito não lido, 65%); canais ESD/INF assumidos por analogia (60%).

**Valores-âncora**
| Item | Valor | A partir de | Fonte |
|---|---|---|---|
| Imposto de renda | 22%; isenção básica €700/mês (€8.400/ano); €776 na idade de aposentadoria | 2026-01-01 | TuMS § 4 (1), § 23 (1), § 23⁵ (1) |
| Social tax | 33% (20/13; 16/13/4 para membros do II pilar); mínimo €292,38 sobre kuumäär €886 | 2026-01-01 | SMS § 7 (1), § 10; Lei do Orçamento 2026 § 1 (6) |
| Desemprego | 1,6% empregado / 0,8% empregador (2026–2029) | 2026-01-01 | VV 25.09.2025 määrus nr 78 |
| II pilar | 2% padrão, eleição de 4% ou 6% | 2026-01-01 | KoPS § 9 |
| Salário mínimo | €886 / €5,31 até 31 mar; €946 / €5,67 | 2026-04-01 | VV 23.03.2026 määrus nr 36 |
| Teto diário de auxílio-doença | €126,87 (não estatutário; publicado até 1 dez) | 2026-01-01 | EMTA / Tervisekassa |

## Artefatos entregues
| Artefato | Versão | Data | Arquivo/local | Observação |
|---|---|---|---|---|
| | | | | |

## Valores-chave (com vigência)
| Item | Valor | A partir de | Até | Fonte |
|---|---|---|---|---|
| | | | | |

## Decisões
- 

## Suporte (tickets)
| Data | Ticket | Assunto | Resolução | Mudou artefato? |
|---|---|---|---|---|
| | | | | |

## Internal Certification (Análise de Reports)
> Frente 5: `frentes/certificacao/estado.md` · Método: [[analise-reports]] · Pasta: `internal-certification/Estonia`

- Sem pacote: Marju Martinson não respondeu (C-11). Report principal: TSD + anexos (formato data-based a partir de out/2026, a confirmar na fonte).

## Pendências
- [ ]

## Correções ligadas
- _(links para entradas de [[correcoes]])_

## Fontes
- skill payroll-compliance-estonia (lida em 2026-10-02)
