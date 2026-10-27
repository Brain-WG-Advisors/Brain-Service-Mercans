---
tipo: pais
codigo: "MA"
etapa_research: "concluida"
etapa_research_data: 
etapa_design: "aguardando"
etapa_design_data: 
etapa_producao: 
etapa_suporte: "sem ticket no hub"
etapa_suporte_data: 
ccg: v1.0
ccg_data: 
wtc: v1.0
wtc_data: 
dd: v1.0
dd_data: 
report_specs: 
report_specs_data: 
sir: v1.0
sir_data: 
payslip: 
skill: "payroll-compliance-morocco"
tickets_abertos: 
tickets_conferidos_em: 
versoes_fonte: "nome do arquivo no Drive (Country Folders/Morocco), lido em 2026-10-27; sem data de versão"
atualizado_em: 2026-10-27
---
# Marrocos

> Hub do país. Índice: [[00-INDEX]] · Skill: `payroll-compliance-morocco` · Fronteiras: [[fronteiras]]

## Situação
| Etapa | Status | Data | Observação |
|---|---|---|---|
| [[research-pipeline]] | ✅ | [data?] | skill compilada |
| [[design]] | ⏳ | | |
| Produção (outro time) | — | | |
| [[suporte]] | ⏳ | | |

## Ficha do país (da skill)
> Resumo do que mais importa para o serviço. Fonte: skill `payroll-compliance-morocco`, lida em 2026-10-02. Valores exatos e tabelas: ler a skill. Se divergir, vale a skill.

- **Escopo:** 2026, setor privado, moeda MAD. Fora do escopo: setor público (CMR, RCAR), pescadores à parte, acidente de trabalho privado, autônomos AMO, acordos bilaterais, penhora.
- **Órgãos:** DGI (IR, CGI), CNSS (portal Damancom), Ministério do Trabalho, ACAPS.
- **Relatórios principais:** BDS da CNSS (declaração + pagamento, antes do dia 10 do mês seguinte `[S]`); declaração mensal do IR (recolhimento no mês seguinte, art. 174-I; na prática antes do dia 20 `[S]`); declaração anual de salários (antes de 1º de março, art. 79, modelo 9421 `[S]`); bordereau-avis.
- **Confiança da skill:** auto-auditoria MA-QA-REPORT v1.0, sem tier. `[P]` leitura primária (CGI 2026, NC 737, Código do Trabalho, dahir 1-72-184, décret 2-01-2723); 22 itens `[S]` (ex.: SMIG, AF 6,40%, IPE, art. 114 da Lei 65-00, prazo CNSS); 4 itens contestados `[S!]`.

**Armadilhas confirmadas** (correções da skill)
1. Barème do IR 2026 é o da LF 2025 (6 faixas, 37% topo); LF 2026 não mexeu; 38% valia até 2024 (engine) → `01-ccg.md` §0.1, §6.1
2. Única mudança salarial 2026: dedução por dependente de 500 para 600 MAD (teto 3.600, 6 dependentes) (engine) → `01-ccg.md` §0.3
3. Teto de 6.000 MAD vale só para curto e longo prazo, não para AF, AMO e TFP (engine) → décret 2-01-2723 art. 4; `01-ccg.md` §3.3
4. AMO do empregado sem teto (maior que a linha CNSS acima de ~6.000) (engine) → `02-wtc.md` §8
5. 0,67/0,33 e 1,05/0,52 são o mesmo dinheiro (IPE da Lei 03-14); rótulo "décès-invalidité" errado → `01-ccg.md` §5.2
6. 1,85% "AMO solidarité" está dentro dos 4,11% patronais; empregador com art. 114 paga só 1,85% (engine) → `01-ccg.md` §5.4, §12.5
7. Indenização de demissão por faixas cumulativas (96/144/192/240 h), não degrau (engine) → CT art. 53; `01-ccg.md` §12.4
8. Isenção de 1.000.000 MAD é um teto único; exclui aviso prévio e férias (engine) → CGI art. 57-7°
9. Prime d'ancienneté é legal e obrigatória (5/10/15/20/25%), base inclui horas extras (engine) → CT art. 350
10. Frais professionnels têm 3ª base que exclui benefícios (35%/25%, teto 35.000/ano) (engine) → CGI art. 59-I-A
11. Teto de vale-refeição: CNSS = 2 x SMIG horário (35,84), IR = 40/dia e 20%; nunca fixar o da CNSS (engine) → `01-ccg.md` §7.3
12. Listas de exclusão dos arts. 353 e 202 são diferentes (engine) → `02-wtc.md` §12
13. Teto de 6.000 é por empregador, não por pessoa (engine) → dahir art. 25
14. Desconto CNSS do empregado omitido é irrecuperável (dahir art. 23) → `03-sir.md` §7
15. Mudança de situação familiar vale no mês seguinte (engine) → CGI art. 74
16. Base legal do payslip é o arrêté 346-05 (não existe "Décret 2-05-2494"); 347-05 é do livre de paie → `06-payslip.md` §1, §3
17. Payslip assinado "lu et approuvé" não quita nada (CT art. 370) → `06-payslip.md` §2.1
18. Indenização compensatória de férias é devida em qualquer rescisão, inclusive justa causa (CT art. 254) → `05-data-dictionary.md` §12.5
19. Seis bases diferentes (bruto, imposável, CNSS, frais pro, ancienneté, horas extras): não forçar tax base = base CNSS → SKILL.md "five bases"

**O que mais dá errado** (do QA)
- Aplicar o teto de 6.000 a toda a CNSS.
- Faixas de indenização como degrau.
- Passar aviso prévio e férias pela isenção do art. 57-7°.
- Fixar o teto de vale-refeição da CNSS.
- Esquecer a isenção parcial do art. 114 (AMO).

**Lacunas abertas / não confirmado** (candidatos a ticket ou nova pesquisa)
- GAP 1: Arrêté 1314-25 (em vigor 2025-10-01): 43 dos 44 tetos de indenizações desconhecidos; padrão seguro é tudo contributivo até leitura (BO nº 7443).
- GAP 2: layouts eBDS (CNSS) e SIMPL-IR XML (DGI) não obtidos.
- GAP 3: texto verbatim do arrêté 346-05 (12 menções `[S]`); BO nº 5540 p. 900.
- GAP 4 `[S!]`: multa de mora CNSS (dahir 3%/1% vs 5%/0,5% reportado), dias do Aïd Al-Mawlid, feriados islâmicos 2026, taxas CIMR (contratuais).
- `[S]` sem fonte primária: SMIG 17,92 e SMAG 97,44 (BO nº 7469), AF 6,40%, PER 25.000 para 50.000 (3.20), prazos CNSS/IR na prática.
- Não pesquisados: acordos bilaterais, penhora, arrêté 344-05 e 347-05, CMR/RCAR, marins pêcheurs.

**Valores-âncora**
| Item | Valor | A partir de | Fonte |
|---|---|---|---|
| IR (barème) | 0/10/20/30/34/37%; isento até 40.000/ano | 2025-01-01 (vale 2026) | CGI art. 73-I; LF 60-24 art. 8 |
| Dedução por dependente | 600/ano, teto 3.600 (6 dependentes) | 2026-01-01 | CGI art. 74-I; LF 50-25 |
| CNSS empregado | 4,48% até 6.000 (máx. 268,80) + AMO 2,26% sem teto | 2026 | Décret 2-01-2723 arts. 1-4; dahir 1-72-184 |
| CNSS empregador | 8,98% até 6.000 + 12,11% sem teto = 21,09% (18,83% com art. 114) | 2026 | idem; CLEISS/ACAPS `[S]` |
| SMIG | 17,92 DH/h (SMAG 97,44 DH/dia desde 2026-04-01) | 2026-01-01 | décret 2.25.983, BO nº 7469 `[S]` |
| Frais professionnels | 35% até 78.000/ano; 25% acima; teto 35.000/ano | 2026 | CGI art. 59-I-A |

## Artefatos entregues
| Artefato | Versão | Data | Arquivo/local | Observação |
|---|---|---|---|---|
| | | | | |

## Valores-chave (com vigência)
| Item | Valor | A partir de | Até | Fonte |
|---|---|---|---|---|
| | | | | |

## Decisões
- AAAA-MM-DD: decisão, por quê, quem decidiu

## Suporte (tickets)
| Data | Ticket | Assunto | Resolução | Mudou artefato? |
|---|---|---|---|---|
| | | | | |

## Pendências
- [ ]

## Correções ligadas
- _(links para entradas de [[correcoes]])_

## Fontes
- skill payroll-compliance-morocco (lida em 2026-10-02)
