# Lituânia — lista de validação com o BAU (Kevin)

Status: **rascunho interno (passo 1 do plano da janela Gmail, 28/10). Nada enviado nem gravado.** Canal (e-mail × call) decide o usuário.
Base: [[Research Pipeline/Lithuania/2026-10-27-reports/CONFERENCIA]] (D1–D4) · [[Research Pipeline/Lithuania/2026-10-27-SIR/CONFERENCIA]] (s08 G1–G12) · call Kevin 27/10 (`raw/reunioes/2026-10-27-call-kevin-wallisson-lituania.txt`, 04:15–05:55 e 11:11–12:38) · Hub [[Lituania]].

## A. O que mudou (para o BAU conferir na operação)
| # | Item | O que mudou | Fonte | Pergunta ao BAU |
|---|---|---|---|---|
| A1 | GPM313 v1.1 (SR-420) | Formato eletrônico: FFData do MXFD, nomes XML `B_MM_ID`… `G5–G12`; pagador 116, valores 14 (D1–D2) | GPM313.mxfd (EDS 31/12/2025) | No teste com alguns funcionários, o arquivo gerado abre/valida no EDS? |
| A2 | GPM312 v1.1 (SR-421) | Mesmo, + tamanhos L/U (D3–D4); GPM312L 10 linhas/página, U 5; U12 data | GPM312.mxfd (EDS 12/06/2026) | Idem; o cliente tem pagamentos a não residentes (anexo U)? |
| A3 | SAM v1.0 (SR-419) | Sem mudança | instrução Sodra p. 48–56; sam-v07.mxfd | Confirma que o cliente envia SAM mensal hoje pelo EDAS? |
| A4 | Regras 2026 (CT-4285) | Faixas 20/25/32%, teto Sodra €138 729, NPD nova, seguro saúde €350 | Alerta + CCG 2026 v1.1 | Os casos de teste batem com o cálculo do cliente em 2026? |

## B. Só o BAU/cliente responde (lacunas do SIR)
| # | Pergunta | Lacuna |
|---|---|---|
| B1 | Como o cliente envia hoje SAM e GPM313/312: upload no portal (EDAS/EDS) ou web service? Quem gera e quem submete? | resposta ao Kevin 04:15–05:55 ("produced by us… via API?") |
| B2 | Quem confirma o arquivo no EDS em 3 dias (senão a VMI apaga)? Um operador estrangeiro consegue entrar no EDS? | S8; G6, G7 |
| B3 | Como o cliente recebe hoje os atestados de doença da Sodra? | G1 |
| B4 | NP-SD2/licenças está no escopo do cliente? Como é enviado hoje? | G5 (sem spec NP-SD2) |
| B5 | O cliente recebe avisos da VMI (FR1025) e quem trata? | G4 |

## C. O que pedir ao BAU (modelo da Colômbia, PMI Review)
| # | Pedido | Base |
|---|---|---|
| C1 | Amostras dos relatórios que o cliente já entrega hoje (SAM, GPM313, GPM312: arquivo enviado e comprovante), para conferir contra as specs | call Wallisson 27/10, 01:04:28 ("eles mandaram o XML… você já pode validar"); CO: 871 arquivos NE da Heidy (#13, #47) |
| C2 | Depois do teste do Kevin (alguns funcionários pela jornada de cada report), os arquivos gerados, para o mesmo cross-check | call Kevin 27/10, 11:11 |
| C3 | Como cada relatório é feito hoje: sistema gera ou manual, quem submete, por qual canal (= B1/B2) | call Wallisson 01:00:12–01:02:46; Manju, weekly 27/10, 12:15 ("take from BAU") |

Amostra do cliente tem dado pessoal: guardar fora do git (como os 871 da CO).

## Fora (pesquisa nossa, não vai ao BAU)
G2 XSD do FFData · G3 ambientes de teste · G8/G9 limites e endpoints · G10 SAM tardio · G11 versão das docs · G12 SLA DataService.

## E-mail ao Kevin (rascunho v1, 28/10 — não gravado)
**Para:** Kevin Gunawan · **Cc:** Khoi Pham · **Assunto:** Lithuania – statutory reports: samples and current filing process

> Hi Kevin,
>
> Following our call on 27 Oct, we would like to check the Lithuania report specs and the integration document against what the client files today, before Development and Configuration build them. Could you help with the points below?
>
> 1. Samples of the last files the client submitted for SAM (Sodra), GPM313 and GPM312 (VMI), with the submission confirmation if available. Any recent period is fine.
> 2. How are these reports done today? Who prepares the file (payroll system, provider, or manually in the portal), who submits it, and how (upload in EDAS/EDS or web service)?
> 3. VMI requires files sent through the web service to be confirmed in EDS within 3 days, otherwise they are deleted. Who would confirm them for the client, and can that person log in to EDS?
> 4. Sick leave: how does the client receive the sick-leave certificate information from Sodra today, and does it send the NP-SD2 notification itself?
> 5. Does the client receive notices from VMI about these filings, and who handles them?
>
> When you run your test with a few employees, please also share the generated report files so we can compare them with the specs.
>
> Thanks,
