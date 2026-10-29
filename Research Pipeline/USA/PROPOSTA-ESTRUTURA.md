# EUA: proposta de estrutura da research (rascunho, espera ok do usuário)

> Frente EUA ([[frentes/eua/estado|estado]]), 2026-10-29. Hub: [[EUA]] (a criar depois do ok). Nada foi gravado no Drive nem no monday.

## 1. Inventário (2026-10-29)
| Fonte | O que tem |
|---|---|
| Drive `Country Folders/USA` | Só o esqueleto: 16 pastas (01 SOP … 16 RCA); 14 têm apenas o `Testfile for copying folders.gdoc`, 15 e 16 vazias. **Nenhum material de research.** |
| `~/mercans-pipeline` | Nenhuma pasta `US-compliance` nem referência aos EUA. |
| Reuniões | Weekly 29/09 (`raw/reunioes/2026-09-29-research-team-weekly*.txt`): Manju libera começar; tarefa "perguntar à Yoyo quais estados". Biweekly do Marko 21/10 (`raw/chats/2026-10-21-research-team-biweekly-marko-transcript.txt:23-54`): Yoyo ainda não confirmou os estados; federal só não basta, o que importa é **multi-estado** (trabalha num estado, mora em outro); municipal é irrelevante na maioria dos casos; o difícil são **"those tables that we have to maintain and upload"**; filings estaduais por **provedor terceiro**, sem integração com ADP → pesquisar o processo de filing por terceiro. |
| Precedente | Canadá ([[Canada]]): CCG único federal + Québec, mesmo pipeline. |

## 2. Estrutura proposta
```
Research Pipeline/USA/
  00-federal/          FIT (Pub. 15-T), FICA (SS + Medicare + Additional Medicare), FUTA (+ crédito reduzido),
                       W-4, 941/940/944, W-2/W-3, depósitos, supplemental wages, fringe benefits
  00-multiestado/      regra de sourcing (onde trabalha × onde mora), crédito de residente, reciprocidade,
                       convenience-of-employer, limiar de dias, SUI localization (4 testes)
  00-filing-terceiros/ processo de filing por provedor terceiro (pedido do Marko): o que o provedor recebe,
                       formato, quem é o "agent" (Form 8655 / reporting agent), opções de mercado
  <UF>/                dossiê estadual (modelo abaixo), um por estado + DC
  USA-ESTADOS-MATRIZ.xlsx   uma linha por estado: status, tem IR?, local tax?, SUI (alíquota novo empregador,
                            wage base), SDI/PFML, reciprocidade, filings, órgão — cada valor com vigência e fonte
  USA-TABELAS/          as tabelas que o Marko citou (faixas, deduções, wage bases) em formato de carga,
                        com vigência: é o que a Mercans terá de manter todo ano
```
**Artefatos do pipeline** (como no Canadá, sem 51 pacotes separados): 1 CCG (módulo federal + módulo multi-estado + 1 anexo por estado), 1 WTC (colunas de tributação federal e por estado), 1 DD (campos de estado de trabalho/residência, local, W-4 estadual), Report Specs por filing (941, 940, W-2 e, por estado, retenção + UI trimestral + W-2 estadual), SIR (filing por terceiro).

## 3. Modelo do dossiê estadual (`<UF>/DOSSIE.md`, mesmo para todos)
1. Órgãos e portais (Department of Revenue; workforce agency de UI)
2. Imposto de renda estadual: tem/não tem; método (tabela, flat, % do federal); W-4 estadual próprio ou federal; supplemental rate
3. Impostos locais (cidade, condado, school district): existe? quem administra?
4. SUI: alíquota de novo empregador, faixa, wage base, parte do empregado (se houver)
5. SDI / PFML / outros (ex.: transit, workforce training): empregado e empregador, teto
6. Multi-estado: reciprocidade, crédito de residente, convenience rule, limiar de dias
7. Filings: retenção (frequência), reconciliação anual, UI trimestral, W-2 estadual, new-hire reporting
8. Particularidades (ex.: pagamento final, salário mínimo estadual só como referência)
9. Fontes (URL oficial + data de leitura) e lacunas (`NOT LOCATED` / `⚠️ sem fonte`)

## 4. Ordem
1. **Federal** (00-federal) + **multi-estado** (00-multiestado): base para todo o resto.
2. **Estados sem IR sobre salário** (AK, FL, NV, NH, SD, TN, TX, WA, WY — lista a confirmar na fonte oficial de cada um): dossiê curto, só SUI/PFML/filings.
3. **Estados com clientes ativos**: **a confirmar** (Yoyo não respondeu até 21/10; ver BAU master list).
4. Resto, começando pelos de imposto local (NY, PA, OH, MD, MI, IN, KY, NJ, CA).
5. Filing por terceiro em paralelo, depois do federal.

## 5. Esforço estimado (sessões de trabalho)
| Bloco | Sessões |
|---|---|
| Federal | 2 |
| Multi-estado | 2 |
| 9 estados sem IR (≈0,5 cada) | 4–5 |
| ≈32 estados com IR simples (≈1 cada) | 30–32 |
| ≈10 estados com imposto local/complexos (≈2 cada) | 20 |
| Filing por terceiro | 1–2 |
| Artefatos (CCG/WTC/DD/Specs/SIR) + QA | 8–10 |
| **Total** | **≈ 67–73** |
Com subagentes baratos na coleta mecânica (Haiku/Sonnet lendo site do DoR e preenchendo a matriz), cai para ≈ 40–45. É inferência minha, não medição.

## 6. Decisões do usuário
- Estrutura e modelo acima: ok?
- Quais estados têm clientes ativos (Yoyo / BAU master list)?
- Artefatos: 1 pacote único EUA (como Canadá) ou pacote por estado?
- Escopo: setor privado, ano fiscal 2026 (e 2027 quando sair a Pub. 15-T 2027)?
