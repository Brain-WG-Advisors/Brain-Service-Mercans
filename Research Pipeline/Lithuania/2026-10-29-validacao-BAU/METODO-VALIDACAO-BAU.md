# Lituânia: validação dos Report Specs e do SIR com o BAU (método da Colômbia)

> Hub [[Lituania]] · Correções locais: `Research Pipeline/Lithuania/2026-10-29-correcoes/` · Validação de 28/10: [[Research Pipeline/Lithuania/2026-10-28-validacao/CONFERENCIA]] · Modelo da Colômbia: [[Research Pipeline/Colombia/co-report-crosscheck/MAPA]] (kit `co-report-crosscheck`, `CONFIRMACAO-PROCESSOS-CO-2026-10-26.xlsx`, `PENDING-2026-10-21.md`) · Rascunho anterior: [[rascunhos/2026-10-28-lituania-validacao-BAU]]

Status: **rascunho para o usuário (29/10). Nada enviado nem gravado em Drive, ticket ou e-mail.** É iniciativa nossa (ninguém pediu), e o texto ao BAU diz "para estarmos alinhados".

## 1. O que fizemos na Colômbia e como fica na Lituânia
| Passo na Colômbia | Na Lituânia |
|---|---|
| O BAU (Heidy) mandou os relatórios reais do cliente (NE, PILA, 350…, 871 arquivos NE) | Pedir ao Kevin os arquivos que o cliente enviou de verdade: SAM (Sodra), GPM313 e GPM312 (VMI), com o comprovante de envio |
| As cópias foram mascaradas na máquina (`02-raw` nunca lido; `03-masked`; chave em `99-local-only`) | Mesmo kit em `Research Pipeline/Lithuania/lt-report-crosscheck/`, com as mesmas pastas e o mesmo bloqueio no `.claude/settings.json` |
| Cross-check de cada spec campo a campo, com um verificador independente por spec | O mesmo, e mais um passo: **rodar a validação oficial** (o script do MXFD da VMI e a estrutura do FFData da Sodra) **sobre o arquivo real do cliente**. Assim sabemos se o nosso verificador aceita o que a VMI e a Sodra já aceitaram |
| Regra: a fonte primária decide a lei, e o relatório do cliente mostra a prática. Divergência vira CONFLITO, nunca correção automática | Igual |
| As mudanças entraram por mapa de mudança, com aprovação do usuário, aplicação e um verificador independente | Igual, partindo das versões corrigidas: SAM v1.1, GPM313/312 v1.2, SIR v1.1 |
| Perguntas de processo ao BAU numa planilha de confirmação (`CONFIRMACAO-PROCESSOS-CO`) | `CONFIRMACAO-PROCESSOS-LT.xlsx`: uma linha por passo do SIR e por regra das specs que dependa da prática do cliente |
| Pontos sem regra saíram da spec e foram para OPEN-POINTS | Igual (as lacunas G1–G16 do SIR e os pontos em aberto das specs) |

## 2. O que pedir ao BAU (Kevin, HRBS-15253)
**Arquivos (os últimos 3 meses disponíveis):**
1. SAM: o FFData enviado à Sodra e o comprovante ou estado no EDAS.
2. GPM313: o FFData mensal enviado à VMI e o estado no EDS. Se houve recusa, a mensagem de erro.
3. GPM312: a declaração anual de 2025 (prazo em 2026) e o estado no EDS.
4. A folha (payroll register) dos mesmos meses, para amarrar os totais: base, imposto e Sodra.
5. Se houver: NP-SD2 e os atestados de doença recebidos da Sodra (para as lacunas G1, G5 e G13).

**Processo (perguntas B1–B5 de [[rascunhos/2026-10-28-lituania-validacao-BAU]]):**
- canal de envio (upload no portal ou web service);
- quem gera e quem envia;
- quem confirma no EDS em até 3 dias;
- se um operador estrangeiro consegue entrar no EDS;
- atestados de doença;
- NP-SD2 e 9-SD;
- avisos da VMI.

**Teste:** os arquivos que o teste do Kevin gerar no sistema (o teste com alguns funcionários, combinado na call de 27/10, 11:11).

## 3. O que conferimos
**Em cada spec (SAM, GPM313, GPM312), campo a campo:**
- O campo existe no arquivo real, com o mesmo nome e tamanho do MXFD ou da descrição oficial (DSA).
- O formato bate: vírgula decimal, marcas 0/1, mês sem zero, datas, códigos.
- Os códigos que o cliente usa (renda, seguro, tipo de pagamento) estão na Field Options da spec.
- Os totais do arquivo fecham com a folha do mesmo mês, e as caixas de total com a soma das linhas.
- O arquivo real passa no nosso verificador do MXFD. Se não passar, o problema está no nosso verificador ou na spec.

**No SIR, cada fluxo (IN e OUT), canal, autenticação, tratamento de erro e prazo:** fonte oficial e confirmação do BAU (resposta escrita ou evidência no arquivo ou no comprovante).

## 4. Critério de "0 erros"
Um item só conta como certo quando cumpre tudo abaixo:

| # | Critério | Como se prova |
|---|---|---|
| 1 | Todo campo de cada spec tem fonte oficial citada (MXFD, DSA, lei ou instrução) | Coluna de fonte preenchida; auditoria independente com PASS |
| 2 | Todos os exemplos da spec passam na validação oficial | Verificador independente: 0 erros (REVAL-*) |
| 3 | Todo campo bate com o arquivo real do cliente ou foi confirmado por escrito pelo BAU | Planilha do cross-check: cada linha "OK" ou "confirmado pelo BAU" |
| 4 | Todo passo do SIR tem fonte e foi confirmado pelo BAU | `CONFIRMACAO-PROCESSOS-LT.xlsx` sem linha em aberto |
| 5 | O que não tem regra fica fora da spec e entra em OPEN-POINTS, com dono | Lista final de OPEN-POINTS aceita por você |
| 6 | O Drive é igual ao local | `conferir_import.py`, CSV por aba, sem `#ERROR!`; md5 nos .docx |
| 7 | O arquivo gerado pelo sistema no teste do Kevin passa na validação e é aceito no portal (teste real) | Arquivo do teste e o estado no EDS/EDAS |

"0 erros" quer dizer **nenhum erro conhecido e cada item provado**. O critério 7 é a única prova de que a VMI e a Sodra aceitam o arquivo, porque a validação do servidor não roda aqui.

## 5. Ordem
1. ✅ Correções locais (SAM v1.1, GPM313/312 v1.2, SIR v1.1). ⏳ Revalidação independente em andamento.
2. ⏳ **Você:** ok para Drive e tickets. A Lituânia está ativa, então a regra 9 pede ticket de alteração ao Development (CT-4285/CT-3703-05 ou um ticket novo) e comentários de correção nas SR-419/420/421/479. Isso fica com a janela Suporte.
3. ⏳ **Você:** ok no texto ao Kevin (seção 6) e no canal. Recomendo a HRBS-15253.
4. Quando os arquivos chegarem: mascarar, fazer o cross-check, rodar o verificador independente e montar os mapas de mudança. Você aprova antes de qualquer alteração.
5. Fechar a `CONFIRMACAO-PROCESSOS-LT` e o OPEN-POINTS. Gerar as versões finais e passar pela checagem do critério 6.

## 6. Texto ao Kevin (rascunho em inglês, para a HRBS-15253; enviar só depois do passo 2)
> Hi @kgunawan,
>
> To make sure we're aligned before Development builds the Lithuania reports, we'd like to check our specs and the integration document against what the client files today. The current versions are SAM v1.1 (SR-419), GPM313 v1.2 (SR-420), GPM312 v1.2 (SR-421) and the SIR v1.1 (SR-479).
>
> Could you share, for the last three months available:
> 1. The SAM files sent to Sodra and the GPM313 files sent to VMI, plus the 2025 GPM312, with their submission status (and any rejection messages).
> 2. The payroll register for the same months, so we can tie the totals.
> 3. How each of these is done today: who prepares the file, who submits it, and whether it goes by upload in EDAS/EDS or by web service. For VMI, who confirms the file in EDS within the 3 days.
> 4. For sick leave: how the client gets the certificate data from Sodra and whether it sends NP-SD2 (and 9-SD) itself.
>
> When you run the test with a few employees, please send us the files the system generates too. We'll compare everything field by field and come back with anything that needs a decision from your side.
>
> Thanks,

## 7. Observação sobre dados pessoais (decisão sua)
Na pasta do Drive `12- Country Report Codes/SODRA - Social Security` já existem arquivos reais:
- `SAM_2024_11 (1) - Client Example.pdf`;
- `Sick leave report NPSD2 November 1st run.pdf`;
- `2-SD-SAMPLE (1).FFDATA`.

Eles podem ser a "rodada 0" do cross-check sem esperar o Kevin, **depois de mascarados**. Em 29/10 autorizei os agentes da SAM a consultar o PDF do cliente só para conferir o formato, com a ordem de não copiar nenhum dado. Isso vai contra a regra do kit da Colômbia de "nunca ler o arquivo bruto" e não se repete: daqui em diante, só cópia mascarada. Os relatórios dos agentes não trazem dado pessoal (conferir na revalidação).
