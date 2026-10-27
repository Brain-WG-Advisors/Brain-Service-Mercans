# DESCANSO — Gate pré-Marko (Mammoet NL) — pausado em 2026-10-20

> Assunto pausado pelo usuário. Palavra para retomar: **"descanso"**. Ao retomar: fechar a sessão anterior ("fecha a sessão"), reler este arquivo e continuar daqui.

## Pergunta do usuário
Como parar o ciclo: mandamos ao Marko e ele volta com mais erros. Precisamos de uma solução concreta e final.

## Base lida (20/10)
- `raw/chats/2026-10-20-mammoet-defects.md`, `raw/chats/2026-10-19-manju-mammoet-fnd03-fnd04.md`
- `raw/chats/2026-10-20-claude-nl-automation-resumo.md` (chat claude.ai NL AUTOMATION, 23/09–20/10)
- `rascunhos/2026-10-20-feedback-manju-montage-P09.md` (feedback Montage P09 V12, **não enviado**)

## Diagnóstico (causas)
1. Duas réguas: nosso gate (~40 checks) × skill do Marko `nl-payroll-forensic-validation-2` (94–96 testes).
2. Gate autorreferente: declaração comparada com a mesma fonte que a gerou (erro P09–P11: +€217.875,24 / −€239.303,66).
3. Regra corrigida só a partir do P12; P09–P11 não foram regerados.
4. Linhagens paralelas sem dono: nossa V5.1 × V12 do time × pasta "V2"; FND-01 é regressão do V12. Relatório de 19/10 cobria outro run do P10.
5. Gates pulados/N/T por falta de insumos (P01–P08, beschikking Whk, templates) viram achados do Marko.
6. Ritmo: entregas de madrugada, P09 até V23.

## Proposta (gate pré-Marko, bloqueante)
1. Rodar o skill file do Marko, versão do dia, antes de enviar: 0 Fail; cada Obs com decisão.
2. Todo achado do Marko (F-xx/FND-xx) vira check permanente no nosso gate.
3. Comparar com a última versão validada: teste que passava e agora falha bloqueia.
4. Âncora nos holerites por empregado × período (X-01/X-04/X-05).
5. Regra mudou: refazer a partir do 1º período afetado.
6. Manifesto do set: hash, versão, dono da linhagem, lista de N/T com motivo; insumos pedidos antes da entrega.

## Retomada de 20/10 (2ª parte): solução para o caso Holanda inteiro (Nederland + Montage, P09–P13)
> Só análise, sem execução nesta janela (decisão do usuário). Pausado de novo em 20/10 ("descansar").

### Os 4 combinados (governança)
1. Um dono por entidade e uma pasta FINAL com hash.
2. Um run de referência fixo por período e uma regra única, **declaração = holerite/G2N por empregado × período**, escrita e aprovada pelo Marko.
3. Uma régua só: a suíte do Marko, aceita antes como critério de aceite. Cada achado novo vira teste permanente.
4. Gerar a cadeia P01–P13 de uma vez, a partir do holerite/G2N, com um único gerador. Montage como piloto.

### Viabilidade
- **Alta** para a regeneração determinística (~3.500 registros; o P09 v1.1 já foi aprovado pelo Yoyo).
- **Média** para "o Marko não acha mais nada", a não ser que a suíte dele seja o gate de aceite.
- **Limites:**
  - decisão do run de referência (Marko/cliente);
  - evidência para FND-03, FND-04 e FND-08;
  - arquivos P01–P08 da Montage;
  - defeito raiz no motor do HR Blizz, que é do time de produto (sem isso, 2026 repete);
  - o nosso gate foi autorreferente, então precisamos de uma âncora independente.

### Crítica de especialista (o que fazemos de errado)
- **a) IA fazendo o papel de código.** Versões geradas por agente (`claude -p`, chat, kits como o chainfix) não se repetem igual; daí o P09 na V23 e regressões como o FND-01 no V12. Holerite → loonaangifte é tarefa determinística. A IA escreve e mantém o código; não mexe nos dados.
- **b) Geramos e validamos a mesma coisa.** É conflito de independência e contraria [[certificacao-so-validar]]. O gate autorreferente é o sintoma.
- **c) Não há modelo de dados.** Arquivos soltos por chat, versão no nome; falta a tabela única empregado × período × elemento.
- **d) Corrigimos a saída, não a origem.** O defeito nasce no HR Blizz (declaração montada a partir do registro de correção).
- **e) Cinco réguas e nenhum dono.**
- **f) Ritmo de crise.** Entregas de madrugada sem pipeline reproduzível.

### Grau de complexidade (1–5)
| Dimensão | Nota | Por quê |
|---|---|---|
| Volume | 1 | ~3.500 registros (Nederland) e ~35 (Montage) |
| Regras de negócio | 4 | blocos de correção, loon-over, prêmios Aof/AWf/Whk/Zvw, AOW, bijtelling, Handboek |
| Formato | 3 | XSD Gegevensspecificaties 2025; totais coletivo × nominativo |
| Processo e pessoas | 5 | muitos atores, sets paralelos, contexto judicial, CEO revisando |
| Rastreabilidade | 5 | cada número precisa ser defensável |

Resumo: o lado técnico é complicado, mas finito; o processo é complexo e não tem dono.

### Solução de engenharia: motor de reconciliação
```
[0 Intake]       arquivos HR Blizz → pasta imutável por entidade/período/run + manifesto sha256
[1 Modelo único] XML, G2N, holerites, SEPA, GL, cadastro → empregado × período × elemento
[2 Regras]       em código, cada uma com citação (Handboek/Gegevensspecificaties) e casos de teste
[3 Gerador]      declaração = holerite por empregado × período → blocos atuais e de correção → XML validado no XSD
[4 Validador]    código separado do gerador; âncora no holerite; catálogo único (Marko + Yoyo + nosso) com IDs F-xx/FND-xx;
                 invariantes (total anual por empregado inalterado; soma dos blocos = TotTeBet)
[5 Release]      só com 0 Fail; diff contra a versão anterior; manifesto; relatório de auditoria gerado dos resultados
```
- Mudou regra ou entrada → roda tudo de novo, P01–P13.
- Achado do Marko → vira teste no catálogo.
- Base existente para consolidar: pipeline B4 da Mammoet (Mac, ~40 checks), skills do Yoyo e do Marko.

### Entrega de consultor (fases)
| Fase | Entrega | Prazo estimado (premissa: insumos e decisões da fase 0) |
|---|---|---|
| 0. Governança | 4 combinados por escrito, RACI, congelar versões atuais | 1 dia (conversa com Manju/Yojana) |
| 1. Motor, piloto Montage | intake, modelo, gerador, validador, release P09–P13 | 3–5 dias |
| 2. Nederland | mesmo motor nos 5 períodos, conciliado com os achados do time e do Marko | 3–5 dias |
| 3. Durabilidade | relatório do defeito ao produto HR Blizz; reuso na Certificação NL (Quest, Excerpta, Sherwin) | contínuo |

**Métricas de sucesso:**
- no máximo 2 versões por período;
- 0 Fail na régua do Marko antes de enviar;
- cada achado vira teste no mesmo dia;
- nenhum relatório discutido sem o hash do set.

**Mudanças imediatas propostas:**
1. Parar de gerar versões por agente até o motor existir.
2. Separar papéis: nós geramos (Montage), e a validação fica com a régua do Marko, rodada por outra pessoa ou por código separado.
3. Levar a fase 0 à Manju e à Yojana como condição para a próxima entrega.

### Próximo passo ao retomar
- [ ] Usuário: aprovar ou ajustar a proposta.
- [ ] Preparar a pauta da fase 0 (para Manju e Yojana).
- [ ] Preparar o desenho técnico do motor: estrutura de pastas, modelo de dados e catálogo de testes.

## Pendente ao retomar
- [ ] Usuário: pedir à Manju/Marko o skill file vigente e a lista de achados com versão, num lugar fixo.
- [ ] Usuário: definir com a Manju o dono da linhagem da Montage (nossa V5.1 × V12 do time).
- [ ] Decidir: mandar a montagem do gate para a frente Certificação (`internal-certification/validators/`)?
- [ ] Decidir: registrar as lições 2–6 em `correcoes.md` e no hub [[Holanda]]?
- [ ] Feedback da Montage P09 (`rascunhos/2026-10-20-feedback-manju-montage-P09.md`) ainda não enviado; a Manju cobrou ("any feedback?").
