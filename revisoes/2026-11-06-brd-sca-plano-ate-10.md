# BRD SCA: plano para chegar à nota 10 (2026-11-06)

> Janela geral, 2026-11-06. Dono da execução: frente Alertas ([[frentes/alertas/CLAUDE|regras]] · [[frentes/alertas/estado|estado]]). Decisão do usuário: "vamos dar início para chegarmos até os 10" (06/11).
> BRD lido: `raw/drive/2026-11-06-brd-sca/BRD_Statutory_Change_Alert_Automation_v1_1.docx` (BRD-SCA-001 v1.1, 28/08/2026, rascunho não aprovado; md5 c2cd971e…, idêntico ao de Downloads) e o texto extraído `.txt` na mesma pasta.

## Avaliação da v1.1 (nota 7/10)
**Forte:** problema provado com erros reais (F7, F8, F13); travas certas (citação por faixa, rascunho nunca vai à Engenharia, aprovação nomeada obrigatória — GATE-06, "sem impacto" exige justificativa — SCOPE-04); testável (limites inclusivos/exclusivos, OFFICIAL × DERIVED, testes de QA sugeridos); metas e piloto (Espanha + Hungria).

**Lacunas (o que leva a 9, v1.2):**
1. Não fecha o ciclo: falta produção confirmada → alerta fechado → base de valores atualizada (o fluxo termina no QA, Stage 10).
2. Não diz quem atualiza CCG/WTC/DD/specs, nem a regra de mudar na versão atual com change log (regra 10 / regra da Manju de 05/11).
3. Domínios sem "declarações e prazos" (formulário, layout, XSD, data de entrega; ex.: Res. 1529 da PILA, CO). Liga ao Compliance Calendar.
4. Detecção mistura duas comparações: página × versão anterior da página (candidato) e valor novo × valor vigente (alerta). A base "sincronizada com o Drive" é inviável como escrita (Drive só pelo navegador; valores estão no CCG e nas skills, não no WTC).
5. Sem métrica de mudanças perdidas (as que descobrimos depois, por ticket ou cliente).
6. Exemplo 7.2 com conta absurda: imposto zero até 49.999,99 e 11.750 (23,5%) em 50.000, acima dos 15% da faixa 3. As contas da faixa 2 batem.
7. Desatualizado: não concilia o kit "Statutory Updates Tracking" (Manju, 05/11), o processo "Annual Statutory Updates" (02/11) e o fluxo CT + Epic Regulation Update (CT-4285); propõe série SCA-* sem acordo; sem dono da construção, esforço nem patrocinador confirmado.

## Plano até 10 (ordem)
| # | Etapa | Pronto quando | Leva a |
|---|---|---|---|
| 1 | Instalar e ler o kit da Manju (backup de `~/mercans-pipeline` antes) + ler o "Annual Statutory Updates" (`raw/drive/2026-11-03-weekly-research/`) | Kit rodou uma vez em teste; nota de 1 página: o que o kit vigia, como, saída, o que não cobre | base para 4 e 7 |
| 2 | BRD v1.2 (local, docx novo com change log no Version Control) | As 7 lacunas acima resolvidas, cada mudança com a linha do change log; exemplo 7.2 refeito e contas conferidas | 9 |
| 3 | Teste com o passado: mudanças reais de 2026 (LT limiares VDU; CI teto CNPS 70.000→75.000; CO Res. 1529 PILA; ES seguro-saúde €500; UK NLW £13,21; EUA OASDI 2027 $192.300) | Tabela: data de publicação, data em que soubemos, se o processo v1.2 pegaria, em quantos dias; % pegas × perdidas | metas medidas |
| 4 | Registro de fontes do piloto (Espanha + Hungria) | Lista com URL, órgão, frequência, formato (HTML/PDF/diário), como detectar mudança; partir dos `legal-basis-register.csv` e das skills | Stage 0 concreto |
| 5 | Um alerta real no formato do BRD (Espanha) | Alerta montado e conferido na fonte, pronto para o Mohit; nada enviado sem ok | prova com o Dev |
| 6 | Conciliação + esboço técnico | Tabela kit × processo anual × CT/Regulation Update × SCA (quem faz o quê); 1 página de como roda, custo em tokens por semana, quem mantém | viabilidade |
| 7 | Aceite (usuário leva) | Revisão da Manju, formato e destinos confirmados pelo Mohit, patrocínio do Marko | 10 |

Etapas 1–6 são locais; nada vai a Drive, e-mail, chat, monday ou ticket sem ok do usuário. Etapa 7 depende de terceiros.

Ligações: [[research-pipeline]] · [[correcoes]] · [[00-INDEX]]
