# Credenciais e segredos em `internal-certification/` (varredura 2026-10-16, janela Certificação)

Pedido da janela geral (usuário): listar os arquivos com credenciais para tirá-los do git **sem mover nem alterar**. Nenhum valor foi copiado aqui, nem em parte. Dados pessoais de empregados ficam fora desta lista, por decisão do usuário.

## Arquivos com credencial real: 3 (1 já fora do git)

| # | Arquivo (relativo a `internal-certification/`) | Tipo de segredo | Onde | Já ignorado? |
|---|---|---|---|---|
| 1 | `United Kingdom/McDermott UK - 2026-09/02 Validation/_extracted/Sept26_MMCL UK reprots/FPS_McDermott Marine Construction Limited_202609.xml` | Government Gateway (HMRC): user ID (`SenderID`) e senha em texto claro (`<Authentication><Method>clear</Method><Value>`) | linhas 17–20 (SenderID na 17, Method na 19, Value na seguinte) | Não |
| 2 | `United Kingdom/McDermott UK - 2026-09/02 Validation/_extracted/Sept26_MMCL UK reprots/EPS_McDermott Marine Construction Limited_202609.xml` | O mesmo user ID e a mesma senha do Government Gateway | linhas 16–19 (SenderID na 16, Method na 18, Value na seguinte) | Não |
| 3 | `United Kingdom/McDermott UK - 2026-09/01 Received/Sept26_MMCL UK reprots.zip` | O FPS e o EPS acima, dentro do zip | membros FPS/EPS | Sim (`*.zip`) |

## Como a lista foi conferida
- **Varredura por palavra-chave:** senha em PT/EN/NL/NO/DA/SV/RU, token, api key, secret, private key, SenderID, Authentication, login, credential. Abrangeu `.txt/.md/.xml/.json/.py/.csv/.tsv`, células de `.xlsx`, texto de `.docx`, e bytes de `.xls/.DBF/.doc`.
- **Arquivos de certificado ou chave** (`.pem/.key/.p12/.pfx/.cer/.crt/.jks/.kdbx/.env`): nenhum.
- **Busca pelo próprio valor:** o user ID e a senha do Gateway foram procurados em todos os arquivos, inclusive dentro de xlsx, docx e zip não criptografados, sem exibir o valor. Só aparecem nos 3 arquivos acima. Workbook, Audit Report, scripts, `validators/uk/specs/mcdermott.py` e painel citam o achado sem o valor.

## Ocorrências descartadas (não são segredo)
- Achado RF-01 do Reino Unido, descrito sem o valor: `UK_McDermott_2026-09_Validation.xlsx` (Executive Summary!B4, Findings Register!D4/E4/G4/D10, Coverage!C28/F94), `UK_McDermott_2026-09_Audit_Report.docx`, `_scripts/build_workbook.py`, `validators/uk/specs/mcdermott.py`, `Acompanhamento_Internal_Certification.xlsx` (Achados!E62/G62/E68).
- **Azerbaijão:** `01 Received/received.txt` (linhas 11 e 16) diz que o zip é protegido e que a senha veio no corpo do e-mail. A senha não está no arquivo. Também citam a senha, sem o valor, `PLANO_DE_ACAO_VALIDACOES.md` (85, 110, 116), `PROMPT_VALIDACOES_PONTA_A_PONTA.md` (35), `validators/common/tracker.py` (92) e o painel (Ações!D24).
- **Coluna "login" dos cadastros de empregados:** é o e-mail de acesso de cada empregado, sem senha. Entra como dado pessoal, que o usuário liberou. Aparece em: DK Sherwin (BG), UK McDermott (U), NO Henkel (O), SE (AZ), NL Quest (GA).
- `references/`: páginas oficiais baixadas com links de "login" e campos de token de formulário. Nenhuma credencial.
- **Não lidos:** um `.xlsx` corrompido da Ucrânia (`Altium_Balance_08-2026_UKR_2.xlsx`, "no valid workbook part") e os PDFs. Os PDFs já estão fora do git por `*.pdf`.

## Padrões de .gitignore propostos (só esses arquivos)
```gitignore
# Credenciais do Government Gateway em texto claro nos FPS/EPS (RTI UK)
internal-certification/**/_extracted/**/FPS_*.xml
internal-certification/**/_extracted/**/EPS_*.xml
```
- Esses padrões também cobrem os FPS/EPS de pacotes UK futuros: todo envio RTI leva o bloco GovTalk de autenticação.
- O zip original já fica fora por `*.zip`.
- **Atenção:** se algum FPS/EPS já tiver sido versionado, o `.gitignore` não o remove do índice. A janela geral precisa rodar `git rm --cached` nos dois arquivos.
