"""Servidor MCP local "brain" (só leitura) para o chat do Claude Desktop.

Registrado no claude_desktop_config.json do Claude Desktop (instalação da Microsoft Store):
  %LOCALAPPDATA%\\Packages\\Claude_pzs8sxrjxfjjc\\LocalCache\\Roaming\\Claude\\claude_desktop_config.json
  comando: uv run --with "mcp<2" python <este arquivo>  (mcp 2.x renomeou o FastMCP)
Uso pessoal do usuário (decidido em 2026-10-27). Ferramentas só leem: nada grava, envia ou apaga.
Bloqueados: .env, .git, .obsidian, publicar/ e qualquer caminho fora da pasta do cérebro.
"""
import os
import re
import subprocess
import sys

from mcp.server.fastmcp import FastMCP

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY = sys.executable
FORA_BUSCA = ('raw', '.obsidian', '.git', 'publicar', '_arquivo', 'fr-research-validation', 'graphify-out',
              os.path.join('frentes', 'pipeline', 'mercans-pipeline'))
BLOQ = re.compile(r'(^|[\\/])(\.env|\.git|\.obsidian|publicar)([\\/]|$)', re.I)

mcp = FastMCP('brain')


def _run(args, timeout=300):
    r = subprocess.run(args, cwd=RAIZ, capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=timeout)
    return (r.stdout or '') + (('\n' + r.stderr) if r.returncode and r.stderr else '')


@mcp.tool()
def contexto_pais(pais: str, completo: bool = False) -> str:
    """Contexto de um país num passo: etapas, versões vigentes dos artefatos, tickets abertos, correções do país,
    pendências abertas e valores sem fonte. `pais` = nome do hub (ex.: Espanha, Colombia) ou código ISO (ES, CO).
    Usar no início de qualquer pergunta ou task sobre um país."""
    return _run([PY, 'scripts/contexto_pais.py', pais] + (['--completo'] if completo else []))


@mcp.tool()
def achar_versao(pais: str, artefato: str, termo: str = '') -> str:
    """Maior versão de um artefato em Downloads, Drive (G:) e Research Pipeline, com data e md5.
    `artefato` = ccg | wtc | dd | sir | payslip | spec. `termo` filtra (ex.: CRA, 190)."""
    return _run([PY, 'scripts/achar_versao.py', pais, artefato] + ([termo] if termo else []))


@mcp.tool()
def onde_estamos() -> str:
    """Painel: o que está pronto, esperando o usuário ou outros, por frente, e tickets abertos nos hubs."""
    return _run([PY, 'scripts/onde_estamos.py'])


@mcp.tool()
def buscar(texto: str, pasta: str = '', maximo: int = 40) -> str:
    """Busca texto (expressão regular, sem diferenciar maiúsculas) nas notas .md do cérebro.
    `pasta` restringe (ex.: paises, servicos, revisoes, Research Pipeline/Colombia). Devolve caminho:linha: trecho."""
    rx = re.compile(texto, re.I)
    base = os.path.normpath(os.path.join(RAIZ, pasta)) if pasta else RAIZ
    if not base.startswith(RAIZ) or BLOQ.search(os.path.relpath(base, RAIZ)):
        return 'Pasta fora do cérebro ou bloqueada.'
    out = []
    for dp, dn, fn in os.walk(base):
        rel = os.path.relpath(dp, RAIZ)
        dn[:] = [d for d in dn if not any(os.path.join(rel, d).replace('.' + os.sep, '').startswith(f) for f in FORA_BUSCA)]
        for f in fn:
            if not f.endswith('.md'):
                continue
            p = os.path.join(dp, f)
            try:
                for i, linha in enumerate(open(p, encoding='utf-8', errors='replace'), 1):
                    if rx.search(linha):
                        out.append('%s:%d: %s' % (os.path.relpath(p, RAIZ), i, linha.strip()[:300]))
                        if len(out) >= maximo:
                            return '\n'.join(out) + '\n… (limite de %d; refine a busca)' % maximo
            except OSError:
                continue
    return '\n'.join(out) or 'Nada encontrado.'


@mcp.tool()
def ler_nota(caminho: str) -> str:
    """Lê uma nota ou arquivo de texto do cérebro (ex.: correcoes.md, paises/Espanha.md,
    Research Pipeline/Colombia/.../CONFERENCIA.md). Até 80 mil caracteres."""
    p = os.path.normpath(os.path.join(RAIZ, caminho))
    if not p.startswith(RAIZ) or BLOQ.search(os.path.relpath(p, RAIZ)):
        return 'Caminho fora do cérebro ou bloqueado.'
    if not os.path.isfile(p):
        return 'Arquivo não encontrado: %s' % caminho
    if not p.lower().endswith(('.md', '.txt', '.csv', '.json', '.base')):
        return 'Só arquivos de texto (.md, .txt, .csv, .json).'
    t = open(p, encoding='utf-8', errors='replace').read()
    return t[:80000] + ('\n… (cortado)' if len(t) > 80000 else '')


@mcp.tool()
def grafo(pergunta: str) -> str:
    """Consulta o grafo de conhecimento (Graphify) do cérebro: conceitos e ligações relacionados à pergunta."""
    return _run(['graphify', 'query', pergunta], timeout=180)


if __name__ == '__main__':
    mcp.run()
