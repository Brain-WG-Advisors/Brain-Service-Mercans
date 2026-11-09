# Projeto: alertas sem perder o prazo da folha (rascunho, 06/11/2026)

> Frente Alertas. Origem: caso Namíbia (teto de 01/09/2026 só entrou em produção em 09/11) e RD Congo (INPP de 24/09/2025 ainda em "Ready for Development"). Fluxo de 12 passos em [[frentes/alertas/estado|estado da frente]].

## Problema
A mudança é descoberta tarde (pelo cliente, em reunião), e o alerta chega ao Development depois da vigência. Resultado: folha calculada errada e acerto retroativo (Gana CT-4598, Namíbia CT-4633).

## Meta
Todo alerta de país nosso vira ticket **até 30 dias antes da vigência** (ou em até 5 dias úteis da publicação, se a lei sair em cima da hora). Nenhuma mudança vista pela primeira vez pelo cliente.

## Peças
1. **Lista de países e donos:** Country Allocation (base) com os nossos 24 países.
2. **Varredura com data:** rodada fixa (kit da Manju, segunda e quinta; ou o prompt `prompts/varredura-alertas-bau.md`) → planilha de mudanças com coluna de vigência e de **prazo do ticket** (vigência − 30 dias).
3. **Calendário de "quando sai":** por país, as datas em que as mudanças costumam ser publicadas (ex.: Lei de Finanças em dezembro, orçamento do Reino Unido, Prinsjesdag na Holanda em setembro, decreto do salário mínimo). Itens "Anunciados" ficam em vigia até a publicação.
4. **Painel de prazos:** um item por mudança com status (Anunciado → Confirmado → Doc → Ticket → E-mail Usema → Em produção → Fechado) e semáforo pelo prazo do ticket.
5. **Fluxo de 12 passos** para cada item confirmado (modelo CT-4632 + Doc no Drive + e-mail à Usema).
6. **Fechamento:** conferir produção (ticket) e publicação no portal; comentar "Mercans Alert- <link>".

## Decisões do usuário
- Prazo mínimo: 30 dias antes da vigência?
- Cadência: segunda e quinta (kit da Manju) ou semanal?
- Onde fica o painel: board do monday de alertas (18227732675) ou página nossa?

## Etapas
1. Instalar o kit da Manju (pausado; backup já feito) e testar com os 24 países.
2. Montar o calendário de publicação dos 24 países.
3. Criar o painel com os itens já abertos (planilha Payroll_Changes v2).
4. Rodar 2 semanas e medir: itens achados antes de virar prazo × depois.
