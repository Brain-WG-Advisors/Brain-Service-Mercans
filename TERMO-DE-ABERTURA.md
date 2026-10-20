# Termo de abertura: Brain Service

> Para aprovação do patrocinador. Rascunho de 2026-10-20 · Plano detalhado: [PLANO.md](PLANO.md)
> Proponente: Wallisson Gomes (Compliance & Research) · Patrocinador: ______________________

## 1. Problema
O claude.ai já é a ferramenta do time para pesquisa estatutária, artefatos (CCG, WTC, DD, Report Specs) e respostas de ticket. Mas ele **não aprende com os nossos erros**. Em 2026 já registramos **67 correções** (por exemplo, claves AEAT, posições de campo no Modelo 190, bases mínimas na Espanha e 25 itens na Ucrânia) que o claude.ai pode repetir na próxima pergunta. Decisões, versões vigentes e o histórico de tickets ficam espalhados entre monday, YouTrack, chats, reuniões e Drive.

## 2. Objetivo
Dar ao claude.ai, **sem mudar a ferramenta do time**, uma base de conhecimento verificada do nosso serviço (erros já cometidos e o certo, versão vigente de cada artefato, decisões e histórico), para que **acertemos mais e retrabalhemos menos antes do handover** para Dev e Implementation.

## 3. Entregas
1. **Projeto "Brain Service" no claude.ai**, com instruções que obrigam a consultar as correções, citar fonte e vigência e declarar a confiança. **MVP em 2026-11-04**, com o conhecimento que já existe.
2. **Pacotes de correção para as skills de país** (`payroll-compliance-*`), entregues a quem as publica.
3. **Relatório de resultado** com números (seção 5) em 2027-01-27.

## 4. Escopo
- **Dentro:** Research Pipeline, Design e Suporte sobre os artefatos que entregamos. Dados de **2026-01-01 em diante** de: monday (RCA, alertas, artefatos), YouTrack/HRBlizz, conversas do claude.ai, transcrições de reunião e Drive "Compliance Team" (só Version Control e QA).
- **Fora:** o trabalho de Dev, Implementation e ativação (só registramos a fronteira) e dados pessoais de funcionários de clientes.
- **Países:** ⬜ os 49 com hub hoje · ⬜ todos os ~80 do board Compliance Artifacts · ⬜ lista: ______________

## 5. Como saberemos que funcionou (metas propostas)
| Medida | Hoje | Meta |
|---|---|---|
| Teste A: 30 perguntas sobre erros já conhecidos, no claude.ai | medido em 2026-10-28 | ≥ 27/30 e **zero erro repetido** |
| Teste C: perguntas de tickets novos que o brain nunca viu (teste cego) | — | ≥ 75% |
| Defeitos em artefato nosso apontados por BA/Dev depois do handover (por mês) | linha de base jan–out/2026 | **−30%** em 3 meses |
| Respostas de ticket corrigidas depois ou reabertas | linha de base jan–out/2026 | **−30%** em 3 meses |

## 6. Uso de dados (precisa de aprovação)
- ⬜ **Aprovo** a coleta **só leitura** de transcrições de reunião e do Drive "Compliance Team" pelo Claude in Chrome, na conta do proponente, sem dados pessoais de funcionários de clientes.
- Onde a base fica guardada: ⬜ manter no repositório privado atual (conta pessoal do proponente) · ⬜ mover para conta/repositório da Mercans: ______________
- Transcrições e arquivos do Drive ficam **só na máquina de trabalho**, fora de qualquer repositório.

## 7. Papéis
| Papel | Quem | Responsabilidade |
|---|---|---|
| Patrocinador | ______________ | Aprova escopo, metas e uso de dados; recebe os relatórios |
| Dono do brain | Wallisson Gomes | Conduz, valida o conhecimento, publica no claude.ai, mede |
| Dono das skills | ______________ | Aplica os pacotes de correção nas skills `payroll-compliance-*` |
| Backup | ______________ | Mantém a rotina na ausência do dono |

## 8. Esforço e prazos
- **≈ 3–4,5 h por semana do proponente** durante ~14 semanas (extração e organização feitas pelo Claude Code; o proponente valida e decide). Depois, rotina de ~20 min por semana.
- Marcos: termo aprovado **2026-10-23** · linha de base **2026-10-28** · **MVP no claude.ai 2026-11-04** · monday e YouTrack ingeridos **2026-11-27** · coleta completa **2027-01-15** · relatório final **2027-01-27**.
- Relatório curto ao patrocinador no MVP e a cada fonte concluída.

## 9. Principais riscos
- **Tempo de validação** maior que o previsto → lotes limitados; prazos recalibrados e comunicados, sem cortar a validação.
- **Conhecimento que não chega ao uso** → o MVP publica em 2 semanas e cada fonte concluída é publicada.
- **Medição viciada** → teste cego (C) com tickets que o brain não viu, mais indicadores operacionais.

## 10. Aprovação
Patrocinador: ______________________ · Data: ____/____/______ · ⬜ Aprovado ⬜ Aprovado com ajustes: ______________
