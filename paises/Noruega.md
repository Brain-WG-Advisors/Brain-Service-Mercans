# Noruega

> Hub do país. Índice: [[00-INDEX]] · Skill: `payroll-compliance-norway`

## Situação
| Etapa | Status | Data | Observação |
|---|---|---|---|
| [[research-pipeline]] | ✅ | 2026-08-23 | skill compilada (build do zero em 2026-08-23; re-verificação em 2026-08-24) |
| [[design]] | ⏳ | | |
| Produção (outro time) | — | | |
| [[suporte]] | ⏳ | | |

## Ficha do país (da skill)
> Resumo do que mais importa para o serviço. Fonte: skill `payroll-compliance-norway`, lida em 2026-10-02. Valores exatos e tabelas: ler a skill. Se divergir, vale a skill.

- **Escopo:** Noruega continental, ano de renda 2026, setor privado, NOK. Svalbard/Jan Mayen documentados como regimes adjacentes, sem engine. Fora: servidores públicos, militares, autônomos; camada de acordos coletivos (tariffavtale) não coberta; AFP não modelado; yrkesskadeforsikring sem taxa legal.
- **Órgãos:** Skatteetaten, NAV, Arbeidstilsynet, Brønnøysundregistrene, Digdir (Altinn 3/Maskinporten).
- **Relatórios principais:** a-melding mensal (NO-RPT-001); Avstemmingsrapport; Sammenstilling anual ao empregado; pagamento de forskuddstrekk (1º dia útil após cada folha) e de arbeidsgiveravgift/finansskatt (bimestral, dia 15); RF-1354 (auxílio estatal 2025, último ano); inntektsmelding NAV (doença e benefícios familiares); Oppdragsregisteret; notificação Aa-register; payslip.
- **Confiança da skill:** "PASS WITH NOTES", 0 defeitos críticos, 14 itens abertos. Nenhuma seção abaixo do piso de 95% no nível de seção, mas 4 ficam em 85–93%: `04-reports-spec.md` 85% (layout de campos DERIVED 35–80%), CCG §14 88%, `03-sir.md` 90%, `02-wtc.md`/DD 90–91%. Abaixo do piso declarado: layout dos campos dos relatórios, formato IBAN/conta (~85%), idioma do payslip (~75%), retenção do payslip (~60%). Algoritmo de trekktabell validado em 1.063.799 linhas, 0 divergências.

**Armadilhas confirmadas**
1. Norway é lookup de tabela: nunca calcular o trekk pelas faixas legais; anualiza em 12,12, snap `floor(base/step)×step + step/2`, divide por 10,5 (engine) → `01-ccg.md` §§2, 3.2
2. Minstefradrag no desconto na fonte é 40,48% com teto 84.216 (não 46% / 95.700) (engine) → `01-ccg.md` §3.2
3. Fator 12,12 só nas tabelas ordinárias (VANLIG); padrão/Finnmark/SPESIAL/mar usam 12,0; divisor 10,5 ou 12 por tabela (engine) → `01-ccg.md` §3.2
4. Tabelas de mar truncam, as demais arredondam; Finnmark e mar também têm o standardfradrag de 10% (teto 40.000) (engine) → `01-ccg.md` §3.2
5. Trinnskatt trinn 4 e 5 = 16,8% e 17,8% (16,7/17,7 é a proposta superada) (engine) → `01-ccg.md` §3.1
6. Forskuddstrekk vence no 1º dia útil após o pagamento; skattetrekkskonto não existe mais (§ 5-12 revogado); data de pagamento é elemento obrigatório da a-melding (engine) → `01-ccg.md` §1
7. Deduções do § 5-9 do empregado (pensão, sindicato, teto 8.700/ano) reduzem a base do trekk, mas NÃO a base da arbeidsgiveravgift (engine) → `01-ccg.md` §4.1
8. Trabalho remoto não dá taxa AGA de zona menor; zona = onde a entidade deve estar registrada; cada underenhet calcula separado; mudança vale no mês seguinte (engine) → `01-ccg.md` §4.1
9. Feriepenger legal 10,2% (12% é coletivo); 25 virkedager = 4 semanas + 1 dia; uplift 60+ +2,3pp com teto de 6G medido em 31 dez do ano de acúmulo (engine) → `01-ccg.md` §5
10. Períodos trekkfri já embutidos nas tabelas (÷10,5), mas sem skattekort ou com kildeskatt não há trekkfritak (senão super-retenção de ~14%) (engine) → `01-ccg.md` §6
11. Kildeskatt på lønn: zero deduções; 25% (17,4% sem trygdeavgift), teto NOK 725.050, estourar joga a renda inteira nas regras ordinárias; empregador "fecha" o imposto pela a-melding (engine) → `01-ccg.md` §7
12. Três G com três datas: sykepenger 6G = 819.294 (G atual 136.549 desde 1 mai 2026); uplift feriepenger 6G com G de 31 dez (6 × 130.160 = 780.960); OTP mínimo 2% até 12G = 1.638.588 (engine) → `01-ccg.md` §§4.3, 5, 10
13. Sem salário mínimo geral nem prêmio legal de turno/sábado/domingo; hora extra ≥40% (aml § 10-6) e ≥50% em 1 e 17 maio; mínimos setoriais só em 10 setores → `01-ccg.md` §§8–9
14. Sem indenização rescisória legal e sem declaração anual do empregador (a-ordningen); modelar severance como wage type configurável tributável → `01-ccg.md` §11
15. Norway é M2M (Maskinporten + Altinn 3 systembruker + JSON REST); Altinn 2 desligado em 19 jun 2026; RF-1211 encerrado em 15 jun 2026; sistemas precisavam estar nas novas APIs até 1 abr 2026 → `03-sir.md`

**O que mais dá errado** (do QA)
- Mínimos salariais: 9 dos 10 setores ainda com taxas de 15 jun 2025 em 24 ago 2026; só bilbransjen tem data 2026 (O-5). Nunca cachear; reverificar antes de cada folha.
- Normrente de nov–dez 2026 não publicada (O-6): bloqueia a folha de novembro; nunca fixar. G muda todo 1º de maio.
- Confundir retenção com apuração: a super-retenção de ~1% é proposital. Surplus de quilometragem: Statens sats 5,30/km vs 3,50 isento = 1,80/km tributável e sujeito a trekk.
- Divergência na própria Skatteetaten: chave `fullycontinuousShiftAndOtherSchemes` (EN) vs `helkontinuerligSkiftOgAndreOrdninger336` (NO) (O-11); enum divergente rejeita a a-melding inteira.

**Lacunas abertas / não confirmado** (candidatos a ticket ou nova pesquisa)
- O-8 / O-9: literais de `inntektsbeskrivelse`, `beregningskode`, `arbeidstidsordning` e contratos de endpoint das APIs da Skatteetaten (atrás de Maskinporten, exige organisasjonsnummer norueguês). Não afirmar spec de payload.
- O-4 (alto): teto de kildeskatt NOK 725.050, base corrente ou anual e correção prática quando estourado.
- O-2: fribeløp da zona Ia com subunidades em várias zonas; O-3: qual G vale no teto de 12G do OTP quando G muda em 1 mai.
- O-10: cobertura da API NAV para benefícios familiares (NO-SIR-008 pode ser manual).
- O-12 / O-13: idioma e retenção do payslip; O-7: formato IBAN/BBAN (convenção bancária); O-14: sobreposição de acordos coletivos.
- O-1: exemplo trabalhado assume tabela 8000.

**Valores-âncora**
| Item | Valor | A partir de | Fonte |
|---|---|---|---|
| Trinnskatt trinn 4 / 5 | 16,8% / 17,8% (escada 1,7/4,0/13,7/16,8/17,8 a partir de 226.100) | 2026-01-01 | Innst. 3 S (2025–2026), skattevedtak 2026 |
| Trygdeavgift | 7,6% (5,1% na taxa reduzida) | 2026-01-01 | skattevedtak 2026 |
| Personfradrag | NOK 114.540 | 2026-01-01 | skattevedtak 2026 |
| Grunnbeløp (G) | NOK 136.549 (6G = 819.294) | 2026-05-01 | NAV |
| Feriepenger legal | 10,2% | 2026-01-01 | ferieloven § 10 (2) |
| Kildeskatt på lønn | 25% (17,4% sem trygdeavgift); teto NOK 725.050 | 2026-01-01 | skatteloven § 20-2/20-3 |

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
> Frente 5: `frentes/certificacao/estado.md` · Método: [[analise-reports]] · Pasta: `internal-certification/Norway`

| Pacote | Período | Pass / Finding / NT | Recibo | Situação |
|---|---|---|---|---|
| Henkel Norway AS (917472890) | set/26 | 34 / 9 / 4 | Sim (A-melding GODKJENT) | Fechado 2026-10-14 |

- Decisão 2026-10-14: sem skattekort no pacote, testa-se a consistência do trekk com os parâmetros do contracheque.
- Trekk 6/6 exato pelas trekktabeller 2026; AGA 14,1% ok.
- **High:** contribuição sindical fora da base do forskuddstrekk e sem fradrag "fagforeningskontingent" na A-melding (Skattebetalingsloven §5-9(1)(b)) → ação A-01 para implementation.

## Pendências
- [ ]

## Correções ligadas
- _(links para entradas de [[correcoes]])_

## Fontes
- skill payroll-compliance-norway (lida em 2026-10-02)
