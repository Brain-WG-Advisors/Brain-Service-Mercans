# Austrália

> Hub do país. Índice: [[00-INDEX]] · Skill: `payroll-compliance-australia` · Correções: [[correcoes]] · Fronteiras: [[fronteiras]]

## Situação
| Etapa | Status | Data | Observação |
|---|---|---|---|
| [[research-pipeline]] | 🔄 | | [INCERTO] skill existe; Board de validação por IA tinha prazo 2026-09-21 (prioridade High), Not Started, vencido; "AU V2.0" citado como próximo país sugerido |
| [[design]] | 🔄 | 2026-06-25 | Implementar STSL é "1 mudança de design, a primeira implementação"; follow-up pendente |
| Produção (outro time) | — | | |
| [[suporte]] | 🔄 | 2026-06-25 | Escalação STSL pendente |

## Ficha do país (da skill)
> Resumo do que mais importa para o serviço. Fonte: skill `payroll-compliance-australia`, lida em 2026-10-02. Valores exatos e tabelas: ler a skill. Se divergir, vale a skill.

- **Escopo:** income year 2026-27 (2026-07-01 a 2027-06-30), setor privado, AUD; federal + 8 estados/territórios (payroll tax). Fora: servidores, militares, autônomos (só o "deeming" de contratados para SG e payroll tax) e conteúdo de modern awards (120+).
- **Órgãos:** ATO (tax, super, STP), Fair Work Ombudsman/Commission, 8 revenue offices estaduais (payroll tax), APRA/SMSF, autoridades de workers' compensation.
- **Relatórios principais:** STP Phase 2 pay event (PAYEVNT.0004, a cada pay run, M2M com o ATO); BAS/PAYGW (ciclos do withholder); relatórios anuais PAYG (14 ago / 28 ago / 31 out); FBT return (21 mai, FBTAA s 68); payroll tax por estado (portal, mensal dia 7 e reconciliação anual 21 jul, DERIVADO); SuperStream (contribuições).
- **Confiança da skill:** PASS WITH DISCLOSED GAPS (build do zero, 24-25 ago 2026, fontes primárias). Maioria das seções 95-99%. Abaixo do piso: long service leave ~75%, workers' compensation ~60% e layout wire do STP ~85% (DERIVED). Sem classificação TIER-B; usa categorias (a) feed vivo, (b) ambiguidade, (c) gap de pesquisa.

**Armadilhas confirmadas** (correções da skill)
1. Payday Super desde 2026-07-01: SG deixou de ser trimestral; sem teto trimestral de $62.500 nem SG statement; prazo = fundo RECEBER até o 7º dia útil (SGAA s 6, s 17A(1)); pagamento fora de ciclo conta a partir do próximo payday do ciclo (engine) → `01-ccg.md` §3
2. "Dia útil" do prazo de SG: feriado de estado inteiro em qualquer jurisdição para o país todo; nunca usar o calendário de um estado (engine) → `01-ccg.md` §3
3. Base de super é QE (SGAA s 10A), não OTE; divergem em AU321 (comissão só fora do horário: OTE No / QE Yes) e AU510 (aviso prévio pago em dinheiro: QE Yes) (engine) → `02-wtc.md`
4. Maximum contribution base anual de $270.830 por empregador/ano; YTD QE no STP deve PARAR no teto (engine) → `01-ccg.md` §3
5. $978,10/$25,74 é piso de AWARD, não segundo salário mínimo; a NMW Order 2026 só tem $1.004,90/semana e $26,44/hora; aplicar a quem não tem award subpaga (engine) → `01-ccg.md` §5.1
6. Mínimo semanal e horário são independentes ($26,44 x 38 = $1.004,72, não $1.004,90); vale a partir do primeiro período de pagamento completo em/após 2026-07-01 (engine) → `01-ccg.md` §5
7. Limiares do Medicare levy no withholding ($28.011 / $35.013) estão certos mesmo rotulados "2025-26"; não "corrigir" para cima (engine) → `01-ccg.md` §2.6
8. Regra dos "33 cents" do Schedule 1: somar 1 centavo antes de x3 / 13 (engine) → `01-ccg.md` Sch 1 e 8
9. Payroll tax WA e SA têm taper: calcular pela fórmula; tabela da RevenueSA é "indicativa" e tem 1 linha incoerente ($1.527.000) (engine) → `01-ccg.md` §4.1.1
10. Taxa de isenção de veículo de SA é 88c/km (ano anterior do ATO), não os 91c do ATO; diária de "other country centres" $132,50 vs $145,45 de capitais (engine) → `02-wtc.md` App. A
11. Redundancy cai de 16 para 12 semanas com 10+ anos (FW Act s 119(2)); verificado duas vezes (engine) → `01-ccg.md` §7
12. Licença FDV não pode aparecer no payslip como tal (FW Regs 3.47, 3.48): o engine precisa sintetizar linhas substitutas → `06-payslip.md`
13. Payroll tax não é M2M: os 8 revenue offices saíram do SBR; só o ATO é M2M. Não codificar checksum de TFN (validar formato e usar EmployerTICK); ABN mod-89 é publicado → `03-sir.md`, `05-data-dictionary.md`

**O que mais dá errado** (do QA)
- Qualquer texto que ainda diga "trimestral" para super; coluna OTE usada no lugar de QE; AU321 e AU510 mal classificados.
- Teto de $270.830 não congelando o YTD no STP; linha de 10 anos do redundancy; FDV no payslip.

**Lacunas abertas / não confirmado** (candidatos a ticket ou nova pesquisa)
- B1 long service leave: para 7 de 8 jurisdições sem período de qualificação, accrual, pro-rata ou cash-out verificados; nenhum esquema portátil examinado.
- B2 workers' compensation: sem taxas nem classificações; 8 definições de "wages" diferentes.
- B3 layout wire do STP PAYEVNT.0004 (elementos XBRL, tamanhos, validações): acesso restrito via Online services for DSPs.
- U2 checksum TFN (~70%); U4 coluna PT do WTC (~85%); U5 calendário de payroll tax (~80%, DERIVED); U8 TD 2026/4 Tabelas 3-8 (viagem ao exterior AU233/AU234 sem tabela em dólar).
- U3 loading de 17,5% de férias e 25% de casual para quem tem award: sem texto de award lido; U11 relógio de 6 meses (quebras, conversão casual, transferência de negócio) não documentado.
- U9 taxa GIC (feed vivo, nunca fixa); U10 conteúdo de modern awards fora do escopo.

**Valores-âncora** (2026-27; fonte: SKILL.md)
| Item | Valor | A partir de | Fonte |
|---|---|---|---|
| Alíquota de SG (charge percentage) | 12% (Norfolk Island 11%) | 2026-07-01 | SGAA 1992 (C2026C00272) |
| Maximum contribution base | $270.830 por empregador/ano | 2026-07-01 | SGAA s 10A(6); teto concessional $32.500 x 100 / 12 |
| Salário mínimo nacional | $1.004,90/semana; $26,44/hora; casual loading 25% | 1º período de pagamento em/após 2026-07-01 | National Minimum Wage Order 2026 (PR799279) cl 4.1 e 5.1 |
| Medicare levy (withholding) | $28.011 / $35.013; família $47.238 + $4.338/filho | 2026-27 | ATO Schedule 1 |
| Redundancy | 16 sem. com 9-10 anos; 12 sem. com 10+ anos | vigente | FW Act s 119(2) |
| Entry-level de award (não é NMW) | $978,10/sem; $25,74/h | 2026-07-01 | FWO, Minimum award wages (AWR 2026) |

## Artefatos entregues
| Artefato | Versão | Data | Arquivo/local | Observação |
|---|---|---|---|---|
| Skill `payroll-compliance-australia` | n/a | n/a | skill Mercans | Existe (ano 2026-27) |

## Valores-chave (com vigência)
| Item | Valor | A partir de | Até | Fonte |
|---|---|---|---|---|
| _(nenhum valor nas fontes; ver a skill)_ | | | | |

## Decisões
- 2026-06-25: implementar STSL (study/training loans) como mudança de design, a primeira implementação; follow-up — Mohit/time de design (chat: design-dev-kb) [INCERTO quem decidiu]

## Suporte (tickets)
| Data | Ticket | Assunto | Resolução | Mudou artefato? |
|---|---|---|---|---|
| 2026-06-25 | Escalação (sem ID) | Implementar STSL | Mudança de design; pendente | Pendente |

## Pendências
- [ ] Follow-up da implementação de STSL — a definir — (chat: design-dev-kb)
- [ ] [INCERTO] Prazo do Board de validação por IA (2026-09-21) já passou com status Not Started; o export pode estar desatualizado

## Correções ligadas
- _(nenhuma)_

## Fontes
- raw/chats/2026-10-01-mercans-design-dev-kb.md
- skill payroll-compliance-australia (lida em 2026-10-02)
