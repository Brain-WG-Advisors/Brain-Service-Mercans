# Kuwait

> Hub do país. Índice: [[00-INDEX]] · Skill: `payroll-compliance-kuwait` · Correções: [[correcoes]] · Fronteiras: [[fronteiras]]

## Situação
| Etapa | Status | Data | Observação |
|---|---|---|---|
| [[research-pipeline]] | ⏳ | | [INCERTO] Kuwait revisado no roadmap de automação (drift-sync); sem pipeline registrado |
| [[design]] | ⏳ | | [INCERTO] |
| Produção (outro time) | — | | |
| [[suporte]] | ⏳ | | HRBS-8606 (PIFSS) citado sem conteúdo |

## Ficha do país (da skill)
> Resumo do que mais importa para o serviço. Fonte: skill `payroll-compliance-kuwait`, lida em 2026-10-02. Valores exatos e tabelas: ler a skill. Se divergir, vale a skill.

- **Escopo:** ano 2026, setor privado e petróleo (Lei 6/2010; Lei 28/1969 onde diverge), empregados, moeda KWD (3 casas decimais, 1 dinar = 1.000 fils). Fora: governo, militares, domésticos, autônomos (Cap. V).
- **Órgãos:** PIFSS (previdência, único órgão de payroll), PAM / Public Authority for Manpower (trabalho), bancos (Wage Protection). Sem imposto de renda pessoal.
- **Relatórios principais:** form 55/تأمينات declaração salarial anual (janeiro); form 168/تأمينات movimentação mensal (só alterações, "delta feed"); forms 51 (registro do empregador), 53/54 (registro do empregado), 56 (fim de serviço); forms 166/171/172 (pagamento, vence dia 1, sem multa até dia 10). Não existe layout de arquivo publicado do PIFSS.
- **Confiança da skill:** auto-auditoria (sem auditor independente), relatório de 2026-09-11; sem tier atribuído. Lado PIFSS `[A]` (texto primário em árabe); lado Lei Trabalhista `[A-]` (manpower.gov.kw inacessível, Lei 6/2010 não lida na fonte); `[B]`: taxas GCC por país, Wage Protection, regras do setor petróleo; `[D]`: conteúdo do payslip (não há artigo legal).

**Armadilhas confirmadas** (correções da skill)
1. PIFSS são 5 fundos em 3 bases/3 tetos (1.500, 1.250, 2.750), não uma contribuição única (engine) → `01-ccg.md` §0.2
2. Taxa do empregado degrau: 10,5% até KWD 1.500 e 8,0% de 1.500,001 a 2.750; empregador 11,5% fixo (engine) → `01-ccg.md` §0.3
3. Base do suplementar = min(max(salário − 1500, 0), 1250), não salário − 1500 (engine) → `01-ccg.md` §12.4
4. Fundo de bônus financeiro 2,5%: sem parte do empregador, teto 1.500 (Lei 110/2014) (engine) → `07-qa-report.md` §5.1
5. Dois "2,5%" distintos do empregado (aumento de pensão, Lei 25/2001, com 1% patronal e teto 2.750; bônus financeiro, Lei 110/2014) (engine) → `01-ccg.md` §5.2
6. Salário contributivo congelado no valor de janeiro (SSL art. 85); admitido no ano usa o mês de admissão (engine) → `01-ccg.md` §3.2
7. Indenização de fim de serviço: limiar de 5 anos (art. 51), não 3; 3 anos/2/3 são da redução por demissão (art. 53) (engine) → `07-qa-report.md` §5.2
8. Indenização sobre o salário do art. 55 (básico + verbas regulares), não só básico; erro de 29,4% no exemplo (engine) → `01-ccg.md` §12.2
9. Lei 17/2018 aboliu, retroativamente, o abatimento PIFSS na indenização; só GCC mantém abatimento (engine) → `01-ccg.md` §9.5
10. Nacionalidade dirige o cálculo (kuwaitiano, GCC, expatriado não-GCC, doméstico) (engine) → `05-data-dictionary.md` §1.1
11. Nacional GCC: registro obrigatório no esquema do país de origem, teto de 11,5% da base kuwaitiana (engine) → Lei 44/2007 art. 5
12. Mês parcial assimétrico: integral no mês de início, nada no mês de saída (engine) → SSL art. 85
13. Ausência sem salário não suspende a contribuição; empregador paga os 15% integrais (engine) → Decisão 10/1977 art. 2 e 8
14. Vencimento no dia 1, não dia 15; sem multa de 1% até o dia 10 → `01-ccg.md` §1.2
15. Declaração de janeiro é insumo (âncora), movimentação mensal é só delta → `04-reports-spec.md` §§1, 2
16. Seguro de acidente de trabalho (Cap. IV) nunca entrou em vigor: sem linha de 2% → DL 126/1977 art. 1
17. Empresas 100% estatais: contribuição sobre o mês corrente e indenização substituída pelo bônus financeiro (engine) → `05-data-dictionary.md` §1.3
18. Multiemprego: só o trabalho original contribui (engine) → Decisão 13/1977
19. Dia substituto obrigatório no descanso semanal (+50%) e feriado (+100%); prêmio não quita → arts. 67, 68
20. Seis das nove ocasiões de feriado são lunares: tratar como dado → `01-ccg.md` §1.4
21. Base PIFSS do setor privado inclui subsídios regulares (moradia, transporte); a exclusão da Decisão 1/1997 vale só para governo/militares (engine) → `01-ccg.md` §4.3
22. Sem linha de imposto no payslip (nem zero) e, para expatriado não-GCC, sem bloco de seguro social → `06-payslip.md` §4
23. Não há artigo legal de payslip; o conteúdo é derivado → `06-payslip.md`
24. Mês = 30 dias (26 se descanso semanal não pago); KWD com 3 casas → SSL art. 85

**O que mais dá errado** (do QA)
- Recalcular a contribuição pelo bruto do mês corrente (ignorar âncora de janeiro).
- Indenização sobre o básico em vez do salário do art. 55.
- Uma taxa em um teto só, em vez de 5 fundos.
- Abater contribuições do empregador da indenização de kuwaitiano.
- Linha de imposto zero no payslip.

**Lacunas abertas / não confirmado** (candidatos a ticket ou nova pesquisa)
- KW-G-02: Lei 6/2010 não lida na fonte (todo conteúdo trabalhista é `[A-]`).
- KW-G-01: Wage Protection só como obrigação (sem nº da decisão, layout ou multas); pedir layout ao banco do empregador.
- KW-B-001: teto 2.750 do fundo de aumento de pensão vem da FAQ do PIFSS.
- KW-B-002: fração do art. 53 (metade) para 3 a <5 anos; uma fonte diverge (1/3). Reverificar antes de produção.
- KW-B-003: taxas GCC por país `[B]`.
- KW-D-002/003/004: bônus anual, base de hora extra e exclusão de hora extra na base PIFSS (configurados por derivação).
- KW-G-10: valores dos subsídios social e de filhos (Lei 19/2000) não obtidos.
- KW-G-04, 07, 08, 09: prazo do form 56, códigos de movimentação derivados, tamanhos de campo e formato do nº PIFSS não publicados.
- Nada foi testado de ponta a ponta; sem alinhamento com WTC Global nem mapeamento HRBLIZZ.

**Valores-âncora**
| Item | Valor | A partir de | Fonte |
|---|---|---|---|
| Empregado PIFSS | 10,5% até KWD 1.500; 8,0% de 1.500,001 a 2.750 (máx. KWD 257,500) | 2026 | SSL 61/1976, DL 128/1992, Leis 25/2001, 110/2014, DL 101/2013 |
| Empregador PIFSS | 11,5% fixo até KWD 2.750 (máx. KWD 316,250) | 2026 | idem |
| Tetos | 1.500 (básico, bônus) / 1.250 (suplementar) / 2.750 (aumento de pensão, desemprego) | 2026 | SSL art. 2; DL 128/1992 art. 1(3); FAQ PIFSS `[A-]` |
| Salário contributivo mínimo | KWD 230 | 2026 | SSL art. 1(m)(2) |
| Indenização | 15 dias/ano nos 5 primeiros anos, depois 1 mês/ano; teto 1,5 ano de salário | 2026 | Lei 6/2010 art. 51(b) `[A-]` |
| Salário mínimo | KWD 75 | 2026 | Res. Ministerial 14/2017 `[A-]` |

## Artefatos entregues
| Artefato | Versão | Data | Arquivo/local | Observação |
|---|---|---|---|---|
| Skill `payroll-compliance-kuwait` | n/a | n/a | skill Mercans | Existe |

## Valores-chave (com vigência)
| Item | Valor | A partir de | Até | Fonte |
|---|---|---|---|---|
| _(nenhum)_ | | | | |

## Decisões
- _(nenhuma decisão registrada nas fontes)_

## Suporte (tickets)
| Data | Ticket | Assunto | Resolução | Mudou artefato? |
|---|---|---|---|---|
| ⚠️ data? | HRBS-8606 | PIFSS | [INCERTO] conteúdo não registrado no chat mercans-compliance | n/a |

## Pendências
- [x] Recuperar o conteúdo do HRBS-8606 (PIFSS) no YouTrack — recuperado: base de SS ignorava o WT 64974 após aumento/promoção (fórmula 64974 corrigida; excesso Feb–Apr/2026 por ajuste manual; PIFSS corrigido pelo cliente; parte ER no HRBS-8233); fechado por Pradeep Duraisamy em 2026-06-12 — _fechada em 27/10 (HRBS-8606): Conteúdo recuperado do ticket (Resolved 12/06/2026): cálculo de SS não usava o WT 64974 (base de SS) após aumento/promoção, ~30 funcionários em 4 entidades; Wallisson (05/06) orientou ajuste manual positivo (21900 não serve) e…_

## Correções ligadas
- _(nenhuma)_

## Fontes
- raw/chats/2026-10-01-mercans-compliance.md
- raw/chats/2026-10-01-compliance-research.md
- skill payroll-compliance-kuwait (lida em 2026-10-02)
