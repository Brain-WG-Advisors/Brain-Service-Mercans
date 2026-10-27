# SR-369: Líbia, LY-TAX-SUF-001 (Social Unity Fund Monthly): taxa "1.00%" ou "1.000%"

## Metadados
- **Ticket:** SR-369, LY-TAX-SUF-001-SocialUnityFund-Spec. Estado In Review, fase *Final Review Phase - Business Analyst*. Research Analyst: Enaakshi Vats. Assignee: wgomes desde 22/10 (ver `rascunhos/2026-10-22-triagem-tickets-enaakshi-shruti.md`). Dev: Michael Mukosi John. BA: Lily Li.
- **Relatório:** `ly-tax-social-unity-fund-monthly`, em **acceptance** no nível país Líbia ("LY Social Unity Fund Monthly Schedule"), teste REF-04-363 (Michael, 15/10).
- **Spec vigente:** LY-TAX-SUF-001 v1.0 (Version Control: só 1.0 de 2026-07-20). Export de 22/10: `raw/docs/drive-exports/2026-10-22/LY-TAX-SUF-001-SocialUnityFund-Spec-v1_0.xlsx`.
- **Fonte do ticket:** `raw/tickets/api/2026-10-22-for-evats/SR-369.md`. Anexos em `raw/tickets/api/anexos/SR-369/`.
- **Análise:** 2026-10-22, janela Suporte. Só leitura: nada foi postado nem alterado.

## O que foi pedido a nós
Lily, 20/10 10:58, com @evats: *"The below field is fixed as 1.00%, but the sample file shows 1.000%. Which one is correct?"*
- `image.png`: linha da aba de spec: `Social Unity Fund Rate | 5 | N (fixed 1.00%)` (colunas A, I, J).
- `image1.png`: tabela com **Ahmed Ali Mohamed / Sara Omar Ibrahim**, Gross 2,000.000 / 3,500.000, taxa **1.000%** em vermelho. São os nomes e valores da **aba Sample File da nossa própria spec**, não da amostra do dev (a do dev usa "LY 01/02/03" e Gross 10.000 / 500 / 14.000).

Só isto: qual formato de exibição está certo.

## Histórico do ticket
| Data | Quem | O quê |
|---|---|---|
| 2026-07-20 | Enaakshi | Abre o SR com o link da spec v1_0 |
| 2026-09-14 | Lily | "Report mapping done" |
| 2026-10-15 | Michael | Relatório desenvolvido e em acceptance; anexa template e amostra de teste (REF-04-363) |
| 2026-10-20 | Lily | Pergunta 1.00% × 1.000% (com @evats) |

## O que nossos artefatos dizem
**Spec LY-TAX-SUF-001 v1.0, aba "Social Unity Fund Spec", linha 14 (Social Unity Fund Rate):**
| Célula | Valor |
|---|---|
| E14 Payroll Field | N |
| F14 Mandatory | Y |
| I14 Field Length | **5** (comprimento exato de "1.00%"; "1.000%" tem 6) |
| J14 Format | **N (fixed 1.00%)** |
| K14 Example | **1.00%** (texto) |
| M14 Explanation | "Statutory rate of the Social Unity Fund levy — fixed at 1% of gross." |
| O14 | n/a (fixed 1%) |
| R14 | Rate / Constant |
| T14 BA Mapping | **1.00%** |

**A mesma spec, aba "Sample File":** E14 e E15 = número 0,01 com formato de célula **`0.000%`**, que aparece como **1.000%**. É daqui que vem o print da Lily. A divergência é **interna à nossa spec**: a definição do campo diz 1.00% e a amostra ilustrativa formata com três casas.

**Template do dev** (`20261015-1420 - ly-tax-social-unity-fund-monthly_template.xlsx`), aba Sample File: E11 = `%%report::@__COLUMN::Social Unity Fund Rate%%` com formato `0.000%` (copiado da nossa Sample File).

**Amostra do teste** (`20261015-1420 - LY Social Unity Fund Monthly Schedule test sample.xlsx`): E11:E13 = **texto `'1.00%'`** (tipo string, conferido com openpyxl), que ignora o formato `0.000%` da célula e aparece **1.00%**. Ou seja, o relatório gerado **já sai com 1.00%**, conforme a definição do campo (T14).

**CCG LY-CCG-001 v1.0:** "Social Unity Fund Contribution (1%) … 1% of monthly gross, employee-borne, collected by the Tax Department" (Mod. 7, item 3); "Social Unity Fund levy" citado sem lei nos *Legal basis*.

## Fonte primária
1. **Taxa e base: Lei nº 20 de 1428 (arquivo "Law-20-2007") sobre o Fundo de Assistência Social, art. 3(1)** (transcrição DCAF, p. 2, conferida visualmente na imagem da página):
   > "تتكون إيرادات صندوق التضامن الاجتماعي من: 1. اشتراك بنسبة 1% يستقطع من إجمالي دخول العاملين كافة سواء في الجهات العامة أو الخاصة، وكذلك من دخول العاملين لحساب أنفسهم."
   > (As receitas do Fundo de Solidariedade Social compõem-se de: 1. contribuição de **1%** descontada do **total dos rendimentos** de todos os trabalhadores, em entidades públicas ou privadas, e dos rendimentos dos autônomos.)
   Art. 1: cria o "صندوق التضامن الاجتماعي" (Fundo de Solidariedade Social).
   Arquivos: `G:\Drives compartilhados\Compliance Team\Country Folders\Libya\14 - Legislation\870-Law-20-2007_AR.pdf` (DCAF) e `451-Law-20-2007_AR.pdf` (mesmo texto).
   ⚠️ Transcrição não oficial (aviso DCAF no rodapé); não conferi se houve alteração posterior da taxa. A PwC (Worldwide Tax Summaries, revisada em 31/05/2026, `ref-Libya-Individual-Summary_PwC.pdf`, p. 2–3) confirma: "1% of the monthly gross salary of all individuals exercising employment in Libya is collected by the Tax Department as a contribution to the Social Unity Fund."
2. **Formulário oficial do relatório:** **não há** na pasta da Líbia. O único formulário fiscal (`Tax-model-1-report.pdf`) é o **Modelo nº 1 (Impostos), "إخطار بوجود ممول خاضع للضريبة"** (notificação da existência de contribuinte sujeito ao imposto), emitido com base no art. 1 do regulamento executivo da Lei 7/2010. É um cadastro com 9 campos de identificação (nome/nome comercial, documento, forma jurídica, objeto, endereço, e-mail, data de início, representante legal, registro comercial), sem taxa nem valores. A própria spec registra que o layout é **DERIVED**, com 60% de confiança (Report Matrix B21), e que não há schema publicado (B14).

**Conclusão sobre a pergunta:** a lei fixa a taxa (1%). **Como exibi-la (1.00% × 1.000%) não tem resposta legal**: nenhum formulário oficial define o formato. É decisão de formatação, e a spec já decidiu: J14/K14/T14 = 1.00%, comprimento 5.

## Veredito
**Confirmado: 1.00%.** É a definição do campo na spec (J14, K14, T14, I14 = 5) e é o que o relatório de teste já entrega. O "1.000%" é só o formato de célula `0.000%` da aba Sample File (ilustrativa) da nossa spec, que deve ser alinhada.

## Mudança na spec
Só na aba **Sample File** (o campo em si não muda):
| Célula | Antes | Depois |
|---|---|---|
| Sample File!E14 | 0,01, formato `0.000%` (exibe 1.000%) | 0,01, formato `0.00%` (exibe 1.00%) |
| Sample File!E15 | idem | idem |
| Version Control, nova linha | — | 1.1 · 2026-10-22 · "SR-369: Sample File rate shown as 1.00% (format aligned to field definition)" · wgomes |

Nada muda para o dev: o relatório já gera 1.00% (texto). Opcional para o dev, sem efeito hoje: trocar o formato `0.000%` da célula E11 do template para `0.00%`, caso o valor um dia passe a sair como número.

## Achados fora do pedido
(Não vão para o ticket; ficam como pendência no hub. A Líbia não tem hub em `paises/`: criar `paises/Libia.md` é tarefa da janela geral.)
1. **Base legal da spec cita só a PwC** (Report Matrix B16, B20). A fonte primária é a Lei 20/1428 (2007), art. 3(1). Sugestão para a próxima versão: B16 = "Law No. 20 of 1428 FDP (2007) on the Social Welfare Fund, Art. 3(1) — 1% of total income of all workers; collected by the Tax Department (PwC, 31 May 2026)".
2. **Base: renda isenta fora do SUF.** Payroll Scope Summary C16 diz "Statutory exclusions are not part of the salary base for the levy". A lei fala em "إجمالي دخول العاملين" (total dos rendimentos) e não exclui EOS nem férias pagas na rescisão. ⚠️ sem fonte para a exclusão: a exclusão do art. 55 da Lei 7/2010 vale para o imposto de renda, não para o fundo. Precisa de fonte (regulamento do fundo ou prática da Tax Department) antes de ser tratada como regra. Afeta o WT 58553 (Social Unity Fund Base) e o SR-367.
3. **Dedutibilidade do SUF no IRPF atribuída ao art. 55** (Payroll Scope Summary C13 e File Structure B13). A lista do art. 55 (Lei 7/2010) tem 5 itens (aposentadoria, despesas reais, multas disciplinares, férias acumuladas na rescisão, prêmio de fim de serviço) e **não inclui** o SUF. A fonte da dedução é só a PwC ("deducted from gross salary after deducting … employee social solidarity fund contribution"). Corrigir a citação para PwC / ⚠️ sem fonte primária.
4. **Autônomos:** a lei também cobra 1% dos autônomos (art. 3(1)). A spec os deixa fora (C9) por estarem fora da folha. Está certo para o relatório, mas a justificativa deveria ser "fora do escopo de payroll", não "out of employee-payroll scope (self-assessed under Art. 54)", que é regra do IR.
5. **Nome:** a lei usa "صندوق التضامن الاجتماعي" (Social Solidarity Fund); "Social Unity Fund" vem da PwC. Os rótulos em árabe da spec já estão certos (التضامن).

## Rascunho de resposta (EN)
> @lli 1.00% is correct. The field is defined as N (fixed 1.00%), length 5, example 1.00%, and the test output already shows 1.00%. The 1.000% came only from the cell format (0.000%) in the illustrative Sample File tab of the spec, now aligned to 0.00% (v1.1). The rate is 1% under Law No. 20/1428 (2007) on the Social Welfare Fund, Art. 3(1).

(A frase "now aligned to 0.00% (v1.1)" só entra depois de a spec ser alterada e aprovada. Sem a alteração, cortar a frase e manter o resto.)

## O que precisa ser feito
| # | Ação | Quem | Urgência |
|---|---|---|---|
| 1 | Aprovar o veredito e o rascunho | Usuário | Alta: relatório em acceptance, BA esperando desde 20/10 |
| 2 | Spec v1.1: E14:E15 da Sample File com formato `0.00%`, células alteradas em azul claro `FFDDEBF7`, linha no Version Control. Partir do export de 22/10; arquivar local (pasta do país em `Research Pipeline/`) e subir ao Drive só com ordem do usuário | Janela Suporte, com ok do usuário | Alta |
| 3 | Gravar o draftComment no SR-369 (não enviar) | Janela Suporte, com ok do usuário | Alta |
| 4 | Pendências 1–5 (fora do pedido) no hub da Líbia | Janela geral (criar `paises/Libia.md`) | Média |
| 5 | Achar fonte para a exclusão da renda isenta da base do SUF (achado 2) | Pipeline / pesquisa | Média: afeta também o SR-367 |

## Lacunas
- Não há formulário oficial nem print do portal da Tax Department para o relatório mensal, então o formato de exibição não é verificável contra a autoridade.
- O texto da Lei 20/2007 é a transcrição não oficial do DCAF. Não conferi alterações posteriores nem o regulamento do fundo.
- A base do SUF sobre renda isenta (EOS, férias na rescisão) está ⚠️ sem fonte.
