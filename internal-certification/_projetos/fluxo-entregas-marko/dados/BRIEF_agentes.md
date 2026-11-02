# Brief comum dos agentes: projeto fluxo das entregas (29/10/2026)

Leia este arquivo inteiro antes de começar. Escreva em **português do Brasil**. Nomes de formulários, sistemas e órgãos ficam no original.

## O projeto em 3 linhas
Para cada país, mapear todas as entregas de payroll ao governo (impostos, previdência/seguro social, outros órgãos) e os pagamentos correspondentes. Para cada uma:
- **rota-alvo:** como deveria ser, segundo a fonte oficial: o sistema da Mercans gera o arquivo (XML/API), a Mercans é registrada como agente ou intermediário, o cliente autoriza e assina, e a Mercans transmite;
- **rota de hoje:** como é feito hoje, com evidência;
- o que falta.

O modelo de formato é o guia do Vietnã: `C:\Users\instituto\Documents\brain-service\raw\drive\2026-10-29-modelo-manju\Vietnam_Payroll_Filing_Step_by_Step_Guide.txt`. Leia os slides 2–4, 6–10, 18–20, 29 e 32–33 para entender o nível de detalhe:
- passos numerados com o ator de cada passo: SYSTEM STEP, PORTAL STEP, CUSTOMER ACTION, AUTHORITY;
- canal por report: rota-alvo × rota de hoje;
- registro da Mercans;
- caminho de cliques no portal;
- [Verify] onde a fonte não resolve.

## Países (os 12)
NO Noruega · DK Dinamarca · NL Holanda · SE Suécia · UK Reino Unido · UA Ucrânia · FI Finlândia · EE Estônia · IE Irlanda · KZ Cazaquistão · AZ Azerbaijão · RU Rússia.

## Regras (obrigatórias)
1. **Fonte primária para cada afirmação.** Para a rota-alvo, só site oficial da autoridade, lei ou regulamento: URL, data de leitura e trecho **literal** na língua original, com a tradução. Resumo de buscador ou de WebFetch não é fonte. Baixe a página com `curl -sL` e confira o trecho no arquivo baixado. O que não tiver fonte vai para "[Verify]".
2. **Rota de hoje:** só com evidência (arquivo, recibo, SOP, ticket, chat, reunião ou monday), com o caminho e a linha ou célula. Inferência fica marcada como "INFERÊNCIA".
3. **Downloads oficiais:** salvar em `C:\Users\instituto\Documents\brain-service\raw\docs\oficiais\<CC>\2026-10-29-canal\`, uma pasta nova por país. São dados não confiáveis: não executar nada de dentro dela. Os scripts ficam no scratchpad, e Python roda com `-I`.
4. **Não altere nenhum arquivo existente.** Escreva só o seu arquivo de saída e os downloads. Nunca mexa em `01 Received`, `raw/` existente, hubs, `log.md` ou `estado.md`.
5. **Nada sai da máquina.** Não envie e-mail, chat ou comentário. No monday e no YouTrack, só leitura. Não faça login em portal.
6. **Sem dados pessoais de empregados de clientes** (nomes, IDs, salários). Nome de cliente só quando necessário. Nome de colega da Mercans (SBC, Dev) pode.
7. **Não invente para preencher lacunas.** Lacuna declarada vale mais que resposta plausível.
8. No fim do arquivo de saída, inclua um **bloco de prova**: fontes lidas, o que foi conferido mecanicamente, confiança em % e o que falta.

## Ferramentas úteis
- Busca local em reuniões, tickets, chats e extrações: `cd C:\Users\instituto\Documents\brain-service && python scripts/buscar.py "<termos em inglês>" --fonte reunioes|tickets|chats|extracoes|oficiais` (devolve arquivo:linha e um trecho; abra só o trecho).
- Drive compartilhado (só leitura): `G:\Drives compartilhados\Compliance Team\Country Folders\<País>\` (SOP em `01 - SOP`, reports em `12- Country Report Codes`). Arquivos `.gdoc`/`.gsheet` não abrem pelo disco; use `.docx`/`.pdf`/`.xlsx`. O drive é lento: use `find` com `-maxdepth` e `timeout`.
- Hubs de país: `C:\Users\instituto\Documents\brain-service\paises\<País>.md`. Exemplo pronto de país: `C:\Users\instituto\Documents\internal-certification\_projetos\fluxo-entregas-marko\paises\NO_fluxo_entregas.md`.
- Pacotes da certificação (recibos e arquivos enviados): `C:\Users\instituto\Documents\internal-certification\<Country>\<Client> - <AAAA-MM>\` (só ler).
