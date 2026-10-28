# REGISTRO — Lituânia, 27/10/2026 (entregas pedidas na call de 27/10)

Hub: [[Lituania]] · Conferências: [[Research Pipeline/Lithuania/2026-10-27-atualizacao-2026/CONFERENCIA]] · [[Research Pipeline/Lithuania/2026-10-27-reports/CONFERENCIA]] · [[Research Pipeline/Lithuania/2026-10-27-SIR/CONFERENCIA]] · Plano: [[rascunhos/2026-10-27-lituania-tasks-plano-e-rascunhos]]

Origem: call com o Wallisson (27/10) e SteerCo Accenture LT & LU (27/10). O cliente testou e o sistema ainda calcula com as regras de 2025 (HRBS-15253). Pedido: (1) regras de 2026 ao Development; (2) refazer a research dos reports, um ticket por report; (3) SIR para a Configuração.

## 1. Regras de 2026 (CCG, Alerta, WTC, DD)
Conferidos contra a lei e corrigidos (mudanças em azul-claro nos arquivos):
- **Faixas do IR:** 20% até €83.237,40; 25% até €138.729; 32% acima (36 e 60 × VDU €2.312,15). O Alerta tinha €82.962 / €138.270 e 0% na 1ª faixa.
- **Aplicação das faixas:** por pagamento (na prática 20%); pelo total anual só a pedido do empregado (GPMĮ art. 23(7)).
- **Teto anual da Sodra:** €138.729 (60 VDU), exceto PSD.
- **NPD:** fórmula única 747 − 0,49 × (renda − 1.153), zero acima de €2.677,49.
- **Seguro-saúde pago pelo empregador:** isento só até €350/ano, dentro do teto de 25%; o excesso entra no IR e na Sodra.
- **Acidentes, grupo II:** 0,49%.
- **Salário abaixo do mínimo:** o empregador paga as contribuições do empregado e do empregador sobre a diferença até €1.153 (5 exceções); exemplo 1 do CCG refeito (custo 59,09).
- **Residência e pensão adicional 2026–27:** textos alinhados à lei e à página da Sodra.
- **WTC V3.1:** 23610, 65630, 65810, 65835. **DD V3.1:** Elective Tax Rate (G12) e Incapacity Level (I10).
- Alinhamento CCG × Alerta × WTC × DD: sem divergência restante. Contas dos exemplos refeitas; validador PASS.

## 2. Reports (SAM, GPM313, GPM312)
Research refeita nas fontes oficiais vigentes (Sodra e VMI/EDS, formulários MXFD) e comparada com as specs v1.0 do Drive:
- **SAM (Sodra):** os 67 campos batem com o `sam-v07.mxfd` e a instrução vigente. **Sem mudança (v1.0).**
- **GPM313 (VMI):** conteúdo de 2026 correto; formato eletrônico errado (a spec dizia que não há XML; há FFData). **v1.1:** nomes XML, tamanhos (nome 116, valores 14), mês sem zero, canais de entrega.
- **GPM312 (VMI):** conteúdo VA-24 correto; mesmo erro de formato. **v1.1:** nomes XML, tamanhos, 10 linhas por folha L e 5 por folha U, U12 como data, alíquotas válidas em 2026 (L9 0/5/15/20/25/32; U9 + 7,5 e 10 só no código 62).
- 2 revisões independentes; validador PASS.

## 3. SIR — LT-SIR-001 v1.0
Documento novo de integração com os órgãos:
- **Sodra:** conta EDAS com assinatura qualificada; web service DataService (SOAP), com status e códigos de erro.
- **VMI:** EDS por formulário on-line, upload do FFData ou web service (EDSWebServiceUploadFile); a declaração precisa ser confirmada no EDS em 3 dias, senão é apagada; login só pelo e-gov gateway a partir de 01/09/2026.
- Lacunas listadas na seção 7 (ex.: canal de máquina para atestados da Sodra, XSD do FFData, ambiente de teste).
- 2 revisões independentes (14 achados, todos corrigidos).

## Onde está
- **Drive (arquivos novos; nenhum original alterado):** CCG 2026 v1.1, Alerta 2026 v1.1, WTC V3.1, DD V3.1, specs GPM313 e GPM312 v1.1, e a pasta nova `19 - Statutory Integrations` com o LT-SIR-001 v1.0. md5 conferido.
- **Cérebro:** `Research Pipeline/Lithuania/` (pastas `2026-10-27-atualizacao-2026`, `-reports`, `-SIR`, cada uma com `CONFERENCIA.md`); fontes oficiais em `raw/docs/oficiais/LT/`.

## Aguardando aval (nada postado nem enviado)
1. Corrigir o Google Doc oficial do Alerta (ligado à CT-4285) e importar as specs v1.1 nas planilhas.
2. Comentários nas tasks existentes: CT-4285 (regras 2026), SR-419/420/421 (specs), CT-3703/04/05 (opcional).
3. Task nova SR "LT: Lithuania Statutory Integration" (SIR).
4. Um e-mail único ao Mohit com a lista das tasks (substitui os 5 rascunhos atuais).
5. Resposta ao Kevin na HRBS-15253.

## Não conferido
Teto de 2025 citado no Alerta; códigos de erro do SAM; datas de vigência da VA-105 e VA-24; piso do Fundo de Longo Prazo nas exceções; lacunas da seção 7 do SIR.
