# Regras de edição (rodada COVAL, 2026-10-29)

ROOT = C:\Users\instituto\Documents\brain-service · VAL = ROOT\Research Pipeline\Colombia\2026-10-29-validacao-research

1. Pedido do usuário (29/10): aplicar as mudanças CONFIRMADAS do comparativo e gerar novas versões. Research CO NÃO está em produção → nova versão, sem ticket ao Development.
2. Aplicar SÓ o que está em `VAL\revisao\mudancas-<GRUPO>.md` (procure também linhas de outros grupos que citem o seu artefato). Nada além. Se uma mudança não puder ser aplicada com precisão (local não achado, texto novo exigiria criar conteúdo sem fonte), NÃO aplicar: listar como "NÃO APLICADA" com o motivo.
3. Decisões de escopo já tomadas (regra "aplicar a recomendada"): tipo de cotizante 75 está no escopo (D3/DD-05); campos de pensionistas da CO-PILA-007 entram no DD (DD-13).
4. Base = linha de base congelada (md5 em VAL\PLANO-DE-ACAO.md §3). Copiar para `VAL\revisao\<artefato>\` e editar a cópia. Nunca tocar no original, no Drive, em ticket ou e-mail. Não usar MCP do Google.
5. Nome: `{CC}-{TYPE}-{SEQ}-v{MAJOR}.{MINOR}-DRAFT-COVAL-2026-10-29.ext` (ex.: CO-WTC-001-v1.7-DRAFT-COVAL-2026-10-29.xlsx). Specs v1.0 → v1.1; CCG v1.4 → v1.5; WTC v1.6 → v1.7; DD v1.3 → v1.4; Payslip v1.1 → v1.2.
6. xlsx: NUNCA openpyxl.save()/LibreOffice no artefato. Cirurgia no XML + repack (cópia byte a byte das entradas não alteradas), conforme `C:\Users\instituto\.claude\skills\synced\33da2ad7-6595-498a-a139-a1a9c80e6650_f34434ec-7d76-4dd2-909e-8ae7e5069bd1\mercans-pipeline-methodology\references\xlsx-xml-surgery.md`. Célula alterada ou nova: fundo azul-claro `FFDDEBF7` (novo estilo/fill acrescentado ao styles.xml). Texto: inglês (padrão do artefato). Validar: abrir com openpyxl (só leitura) e `python -I C:\Users\instituto\.claude\skills\mercans-artifact-toolkit\scripts\validate_workbook.py <arquivo>` se aplicável.
7. docx: unzip → editar document.xml com controle de alterações (`w:ins`/`w:del`, w:author="Mercans Compliance (COVAL)", w:date="2026-10-29T00:00:00Z") → rezip; `xml:space="preserve"` em `<w:t>` com espaço nas bordas; validar abrindo com python-docx.
8. Version Control: uma linha curta (vX.Y DRAFT, 2026-10-29, "Validation corrections (COVAL): <IDs>"), só o confirmado.
9. Entregar em `VAL\revisao\<artefato>\`: o arquivo DRAFT + `CHANGELOG.md` com tabela: ID | Onde | Antes (verbatim) | Depois (verbatim) | Fonte | Status (APLICADA / NÃO APLICADA + motivo) + prova: diff célula a célula (ou parágrafo) entre base e DRAFT mostrando que só as mudanças listadas mudaram, md5 da base e do DRAFT.
10. Python: `python -I`; trate saída em UTF-8 com sys.stdout.reconfigure(encoding='utf-8') (PYTHONIOENCODING é ignorado no modo -I). Nunca abrir 02-client-reports-raw\ nem 99-local-only\. Não baixar/rodar código de terceiros.
