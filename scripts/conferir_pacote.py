"""Confere se um pacote do pipeline traz todo arquivo que o script cita.

Uso: python scripts/conferir_pacote.py <pasta-ou-zip> [script.sh ...]

- A raiz do pacote é a pasta que contém o script (mercans_pipeline_v*.sh).
- Lê cada script e cada agente/README em .claude/agents e shared/si-runbook,
  extrai os caminhos ${PIPELINE}/..., $SHARED/..., shared/... e .claude/agents/...
  e confere se existem no pacote.
- Arquivo que o script "tolera" ausente (if [ -f ... ]) conta como FALTA.
- Sai com código 1 se faltar qualquer arquivo.
"""
import os
import re
import sys
import zipfile

PADROES = [
    (re.compile(r"\$\{?PIPELINE\}?/([A-Za-z0-9_./-]+)"), ""),
    (re.compile(r"\$\{?SHARED\}?/([A-Za-z0-9_./-]+)"), "shared/"),
    (re.compile(r"\$\{?SCRIPT_DIR\}?/([A-Za-z0-9_./-]+)"), "@script_dir/"),
    (re.compile(r"(?<![\w/$}])(\.claude/agents/[A-Za-z0-9_.-]+\.md)"), ""),
    (re.compile(r"(?<![\w/$}.])(shared/[A-Za-z0-9_./-]+)"), ""),
]


def carregar(origem):
    """Devolve {caminho relativo: bytes} para pasta ou zip."""
    arquivos = {}
    if zipfile.is_zipfile(origem):
        with zipfile.ZipFile(origem) as z:
            for n in z.namelist():
                if not n.endswith("/"):
                    arquivos[n] = z.read(n)
    else:
        # pasta: só indexa os nomes; o conteúdo é lido sob demanda (pastas grandes, caminhos longos)
        for raiz, dirs, nomes in os.walk(origem):
            dirs[:] = [d for d in dirs if not d.endswith("-compliance") and d not in ("dist", "__pycache__", "_backup")]
            for n in nomes:
                p = os.path.join(raiz, n)
                arquivos[os.path.relpath(p, origem).replace("\\", "/")] = Leitura(p)
    return arquivos


class Leitura:
    def __init__(self, caminho):
        self.caminho = caminho

    def decode(self, *a):
        try:
            return open(self.caminho, "rb").read().decode(*a)
        except OSError:
            return ""


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    arquivos = carregar(sys.argv[1])
    scripts = [k for k in arquivos if re.search(r"(^|/)mercans_pipeline_v[\d_]+\.sh$", k)]
    if not scripts:
        print("FALTA o script mercans_pipeline_v*.sh no pacote")
        return 1
    raiz = scripts[0].rsplit("/", 1)[0] + "/" if "/" in scripts[0] else ""
    existentes = {k[len(raiz):] for k in arquivos if k.startswith(raiz)}
    pastas = {p.rsplit("/", 1)[0] + "/" for p in existentes if "/" in p}
    pastas |= {"/".join(p.split("/")[:i]) + "/" for p in existentes for i in range(1, p.count("/") + 1)}

    leitura = [s[len(raiz):] for s in scripts] + sys.argv[2:]
    leitura += [p for p in existentes if p.startswith((".claude/agents/", "shared/si-runbook/")) and p.endswith((".md", ".sh"))]
    citados = {}
    for rel in leitura:
        dado = arquivos.get(raiz + rel)
        if dado is None:
            continue
        texto = dado.decode("utf-8", "replace")
        base_dir = rel.rsplit("/", 1)[0] + "/" if "/" in rel else ""
        for rx, prefixo in PADROES:
            for m in rx.finditer(texto):
                cam = m.group(1).rstrip(".,)")
                if prefixo == "@script_dir/":
                    cam = base_dir + cam
                else:
                    cam = prefixo + cam
                if "{" in cam or "$" in cam or cam.endswith("-"):
                    continue
                citados.setdefault(cam, set()).add(rel)

    falta = []
    for cam in sorted(citados):
        ok = cam in existentes or (cam.rstrip("/") + "/") in pastas
        if not ok and (cam + ".example") in existentes:
            print("OK    " + cam + "   (opcional: o pacote traz " + cam + ".example)")
            continue
        print(("OK    " if ok else "FALTA ") + cam + "   <- " + ", ".join(sorted(citados[cam])))
        if not ok:
            falta.append(cam)
    print(f"\n{len(citados)} caminhos citados, {len(falta)} faltando")
    return 1 if falta else 0


if __name__ == "__main__":
    sys.exit(main())
