# Abre as frentes (Suporte, Gmail, Chat, Pipeline, Certificacao) em abas separadas do Windows Terminal,
# cada uma com sua sessao do Claude Code na pasta da frente (frentes\<frente>), que carrega
# o CLAUDE.md da raiz + o CLAUDE.md da frente.
#
# Uso:
#   .\scripts\abrir_frentes.ps1                      # sessoes novas, ja abrindo a frente
#   .\scripts\abrir_frentes.ps1 -Retomar             # volta a ultima conversa de cada frente
#   .\scripts\abrir_frentes.ps1 -Frentes Suporte     # so uma (ou algumas) frente(s)
#   .\scripts\abrir_frentes.ps1 -Frentes Chade,EUA,ValidacaoCO   # frentes de 2026-10-29 (pastas chade, eua, validacaoco)
#   .\scripts\abrir_frentes.ps1 -DryRun              # so mostra o comando

param(
    [ValidateSet('Suporte', 'Gmail', 'Chat', 'Pipeline', 'Certificacao', 'Chade', 'EUA', 'ValidacaoCO')]
    [string[]]$Frentes = @('Suporte', 'Gmail', 'Chat', 'Pipeline', 'Certificacao'),
    [switch]$Retomar,
    [switch]$DryRun
)

$raiz = Split-Path -Parent $PSScriptRoot

$abas = foreach ($f in $Frentes) {
    $nome = "$f - Mercans"
    $pasta = Join-Path $raiz ('frentes\' + $f.ToLower())
    if ($Retomar) {
        # o historico do Claude Code e por pasta: --continue retoma a ultima conversa desta frente
        $claude = 'claude --continue'
    } else {
        $claude = "claude -n `"$nome`" `"Abre a sessao desta frente.`""
    }
    "new-tab -d `"$pasta`" --title `"$nome`" $claude"
}

$argumentos = $abas -join ' ; '

if ($DryRun) {
    Write-Output "wt $argumentos"
    return
}

Start-Process wt -ArgumentList $argumentos
