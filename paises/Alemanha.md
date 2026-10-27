# Alemanha

> Hub do país. Índice: [[00-INDEX]] · Skill: `payroll-compliance-germany` · Fronteiras: [[fronteiras]]

## Situação
| Etapa | Status | Data | Observação |
|---|---|---|---|
| [[research-pipeline]] | ✅ | [data?] | skill compilada (QA da própria skill: país NÃO fechado; ver Ficha) |
| [[design]] | ⏳ | | |
| Produção (outro time) | — | | |
| [[suporte]] | ⏳ | | |

## Ficha do país (da skill)
> Resumo do que mais importa para o serviço. Fonte: skill `payroll-compliance-germany`, lida em 2026-10-02. Valores exatos e tabelas: ler a skill. Se divergir, vale a skill.

- **Escopo:** ano de renda 2026, setor privado, federal, empregados, EUR, idioma alemão. Fora: Beamte, autônomos, sócios-gerentes controladores (salvo fronteira), Kurzarbeit (colocado, não especificado), Tarifverträge (configuração por cliente), ajuste anual.
- **Órgãos:** BMF/Finanzamt (Lohnsteuer, ELStAM), Krankenkassen (Einzugsstelle de todo o GSV), Minijob-Zentrale, Datenstelle der Rentenversicherung (Sofortmeldung), ITSG, Berufsgenossenschaften.
- **Relatórios principais:** Lohnsteuer-Anmeldung (nível de campo), Lohnsteuerbescheinigung (nível de campo), Beitragsnachweis (estrutural, um por Krankenkasse), DEÜV/DSME (estrutural), UV-Jahresmeldung (estrutural).
- **Confiança da skill:** autoauditoria (sem `compliance-qa-auditor` independente). Veredito: país NÃO fechado. Lado fiscal bem fundamentado (BMF, PAP 2026 lido na íntegra); lado SV só estrutural. Sem veredito de tier (não citar). 31 marcadores TIER-B em 24 itens (TB-01..TB-24, TB-06 fechado), 14 lacunas (G-01..G-14). Nada foi round-tripped. Códigos `DE-E-/D-/B-/R-` do WTC são locais; sem alinhamento ao Global WTC nem mapeamento HRBLIZZ.

**Armadilhas confirmadas** (SKILL.md "Design clarifications"; engine = muda valor calculado)
1. Arbeitslohn e Arbeitsentgelt são dois brutos diferentes; a Vorsorgepauschale roda sobre o fiscal (BMF 2025-08-14 Rn. 8) → `01-ccg.md` M3.1 (engine)
2. Teilbetrag KV da Vorsorgepauschale usa 7,0%, não 7,3% (`KVSATZAN = KVZ/2/100 + 0,07`) → `01-ccg.md` M6 (engine)
3. Base do SolZ e da Kirchensteuer é `JBMG` (Lohnsteuer anual com Kinderfreibeträge, §51a), não o imposto retido; exemplo: 28,38/mês a mais → `01-ccg.md` M12 Ex. 4 (engine)
4. Pflegeversicherung tem 4 modificadores; Sachsen: empregado 2,30% / empregador 1,30% (sem filhos 2,90%), inclusive na Vorsorgepauschale → `01-ccg.md` M5.3, M12 Ex. 3 (engine)
5. Teilbetrag ALV (novo 2026) não é redução geral: classes I-V, teto conjunto de 1.900; no salário comum rende zero → `01-ccg.md` M6 (engine)
6. Mindestvorsorgepauschale abolida em 2026; KV/PV privados reais via ELStAM; `PKPV`/`PKPVAGZ` sempre mensais; Teilbetrag d não negativo → `01-ccg.md` M6 (engine)
7. Imposto de renda é fórmula (§32a EStG), não faixas → `01-ccg.md` M6 (engine)
8. Arredondamento por etapa: base e resultado do tarifa para baixo; Vorsorgepauschale para cima; Soli para cima → `01-ccg.md` M1.5
9. Kinderfreibetrag: ZKF x 9.756 nas classes I-III, x 4.878 na IV, zero em V/VI → `01-ccg.md` M6 (engine)
10. Não há contraparte única de SV: cada Krankenkasse coleta tudo; ex. 40 Kassen = 40 Beitragsnachweise; Minijobs vão à Minijob-Zentrale → `03-sir.md`
11. Contribuições vencem dentro do mês (3º último dia útil, §23 SGB IV); Beitragsnachweis no 5º último dia útil; Lohnsteuer no dia 10 do mês seguinte → `03-sir.md` (engine)
12. SV segue Entstehungsprinzip, imposto segue Zuflussprinzip; Märzklausel → `01-ccg.md` (engine)
13. Fünftelregelung saiu da folha do empregador desde 2025 (Wachstumschancengesetz); empregado reivindica §34 EStG → `01-ccg.md` (engine)
14. Abfindung é livre de contribuições; Urlaubsabgeltung é devida; não deixar o acordo juntar os dois (engine) → `01-ccg.md`
15. Prêmios §3b: teto tributário EUR 50/h e de contribuição EUR 25/h (entre os dois: isento de imposto, sujeito a SV; wage type próprio) (engine) → `02-wtc.md`
16. EUR 50/mês e EUR 1.080/ano são Freigrenzen; EUR 110 é Freibetrag (engine) → `02-wtc.md`
17. Feriados são dos Länder (por local de trabalho), sem dia substituto; só 3 out é federal; Buß- und Bettag e split de Sachsen são o mesmo fato → `01-ccg.md` M1.4
18. Férias mínimas: 24 Werktage = 20 dias em semana de 5 → `01-ccg.md` M8
19. Übergangsbereich reduz a base de contribuição mas é irrelevante para a Vorsorgepauschale (engine) → `01-ccg.md`
20. `KVZ` é o Zusatzbeitrag completo da Kasse do empregado; média de 2,9% é só ilustrativa; mudança de `KVZ` no ano bloqueia o Jahresausgleich (engine) → `01-ccg.md`
21. U1/U2 não têm taxa nacional (por Kasse; U1 só até 30 empregados; U2 todos); nunca citar taxa → `01-ccg.md` M5
22. BRSG II: Förderbetrag §100 EStG só sobe de 288 para 360 em 2027; em 2026 é 288 → `01-ccg.md`
23. ELStAM deve ser consultado mensalmente; desregistro imediato na rescisão (senão o próximo empregador cai em Steuerklasse VI) → `03-sir.md`
24. Lohnsteuerbescheinigung: Nr. 27 inclui contribuições estrangeiras, Nrn. 25/26 excluem; Nr. 28 vazio desde 2026 → `04-reports-spec.md` §2.3
25. bAV por conversão é neutra no Gesamtbrutto do payslip (§1 Abs. 3 EBV) → `06-payslip.md`

**O que mais dá errado** (do QA §6)
- Vorsorgepauschale sobre a base de contribuição em vez da base fiscal.
- KV Teilbetrag a 7,3% em vez de 7,0%.
- SolZ/Kirchensteuer sobre o imposto retido em vez de `JBMG`.
- Específico de 2026: tratar o Teilbetrag ALV como redução geral.

**Lacunas abertas / não confirmado** (candidatos a ticket ou nova pesquisa)
- G-01 (maior): *Gemeinsame Grundsätze* §28b SGB IV não obtidos; DEÜV, Beitragsnachweis, Abgabegründe, Beitragsgruppen e Personengruppenschlüssel incompletos (TB-07..TB-10, TB-21); Tätigkeitsschlüssel (TB-11).
- TIER-B que mudam valor: fator F = 0,6619 do Übergangsbereich (TB-01); limite de preço de lista de carro da empresa por data (TB-02); tabela de Kirchensteuer 8%/9% por Land e Kappung (TB-03/04); subsídio máximo a KV/PV privados (TB-05).
- Sem round-trip (G-04), sem revisão independente (G-05), sem Global WTC/HRBLIZZ (G-02/G-03), Kurzarbeit (G-06), Gefahrtarif das BGs (G-09), tabelas §850c ZPO só em uma faixa (G-12), WTC e DD não reconciliados entre si (G-14).

**Valores-âncora**
| Item | Valor | A partir de | Fonte |
|---|---|---|---|
| Tarifa §32a EStG | zero até 12.348; depois fórmula polinomial (0,42x - 11.135,63 até 277.825; 0,45x - 19.470,38 acima) | 2026-01-01 | §32a Abs. 1 EStG (skill) |
| Pflegeversicherung | 3,60% (1,8/1,8); Sachsen empregado 2,30% / empregador 1,30% | 2026-01-01 | `PAP 2026 A1`; §58 Abs. 3 SGB XI |
| Teto conjunto Teilbeträge da Vorsorgepauschale (b a e) | 1.900 | 2026-01-01 | §39b Abs. 2 Satz 5 Nr. 3 e EStG |
| Prêmios §3b | EUR 50/h (imposto); EUR 25/h (SV) | 2026-01-01 | §3b EStG; §1 SvEV |
| bAV-Förderbetrag | 288 (360 só a partir de 2027) | 2026-01-01 | §100 EStG; BRSG II |
| Kinderfreibetrag (PAP) | ZKF x 9.756 (cl. I-III); x 4.878 (cl. IV) | 2026-01-01 | `PAP 2026 A1` |

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
- skill payroll-compliance-germany (lida em 2026-10-02)
