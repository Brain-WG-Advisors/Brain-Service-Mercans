# Prompt: varredura de alertas dos países do BAU List

> Frente Alertas, 2026-11-06. Uso: rodar na janela Alertas a cada nova rodada. Saída da 1ª rodada: [[rascunhos/2026-11-06-varredura-alertas-paises-ativos|varredura 06/11]]. Ligado a [[frentes/alertas/estado|estado da frente]].

## Passo 1: lista de países
Ler no monday o board **BAU Master Client List** (2072701698), grupo "BAU Master Client List", Status = BAU ou HyperCare. Agrupar por país (coluna Country).

## Passo 2: prompt por grupo de países (um subagente Sonnet por região)
```
You are doing a statutory payroll change sweep for Mercans. Today is <AAAA-MM-DD>. Countries: <lista>.
For EACH country, find statutory payroll changes with effective date between <início> and <fim> (income tax withholding, social security rates/ceilings, payroll levies, minimum wage, statutory reporting formats/deadlines, new employer obligations, payroll-relevant employment law). Every value must be confirmed on an OFFICIAL source (tax authority, social security agency, gazette, ministry). Secondary sources only to locate the official instrument. Status: Enacted / Approved budget / Proposal / Published value. If not officially confirmed, say "Not confirmed" and name the secondary source.
Also check whether Mercans already published an alert (mercans.com/resources/statutory-alerts).
Alerts already tracked in YouTrack: <país: CT-xxxx (assunto)>. Mark each change "already tracked: CT-xxxx" or "NEW".
Return per country: Change | Effective date | Status | Official source URL | Mercans alert | Tracked. Then "No change found after checking: <sources>". Do not invent values.
```

## Passo 3: conferência
1. YouTrack: `project: CT Epic: {Regulation Update}` e buscas por assunto em todos os projetos; estado de cada CT na API.
2. Itens só em fonte secundária: segunda passada pelo Claude in Chrome no portal oficial antes de virar alerta.
3. Entregar ao usuário só a lista de países com atualização relevante para payroll; ele diz quais são nossos.
