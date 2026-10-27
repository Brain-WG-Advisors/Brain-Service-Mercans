<#
.SYNOPSIS
  Baixa tickets do YouTrack via REST API e salva cada um como Markdown.

.DESCRIPTION
  Le o token do arquivo .env da raiz do cerebro (variavel -TokenVar), busca as
  issues da consulta, e grava <OutDir>\<ID>.md para cada uma, mais _indice.md.
  O token nunca e impresso. Compativel com Windows PowerShell 5.1.

.EXAMPLE
  .\youtrack_fetch.ps1 -DryRun
  .\youtrack_fetch.ps1 -Since 2026-09-28
#>
[CmdletBinding()]
param(
    [string]$TokenVar = 'YOUTRACK_TOKEN',
    [string]$Since    = '2026-01-01',
    [string]$Query    = '',
    [string]$OutDir   = '',
    [string]$BaseUrl  = 'https://youtrack.hrblizz.dev',
    [switch]$DryRun
)

$ErrorActionPreference = 'Stop'

# --- Preparacao -------------------------------------------------------------
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

$scriptDir = $PSScriptRoot
if ([string]::IsNullOrEmpty($scriptDir)) { $scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path }
$brainRoot = Split-Path -Parent $scriptDir

if ($Since -notmatch '^\d{4}-\d{2}-\d{2}$') {
    Write-Host "ERRO: -Since deve estar no formato AAAA-MM-DD (recebido: '$Since')." -ForegroundColor Red
    exit 1
}
# Padrao: tickets atribuidos a mim. (Este YouTrack rejeita "(a or b) updated:" com HTTP 400;
# para abertos/comentados use -Query "reporter: me" ou -Query "commenter: me".)
if ([string]::IsNullOrWhiteSpace($Query)) { $Query = "for: me updated: $Since .. Today" }
# raw/ e imutavel: cada execucao grava numa pasta nova com a data do dia (nunca sobrescreve)
if ([string]::IsNullOrWhiteSpace($OutDir)) { $OutDir = Join-Path $brainRoot ('raw\tickets\api\' + (Get-Date -Format 'yyyy-MM-dd')) }
$BaseUrl = $BaseUrl.TrimEnd('/')

$utf8NoBom = New-Object System.Text.UTF8Encoding($false)

# --- Leitura do token no .env (sem exibir nada) -----------------------------
function Get-EnvValue {
    param([string]$Path, [string]$Name)
    if (-not (Test-Path -LiteralPath $Path)) { return $null }
    foreach ($line in [System.IO.File]::ReadAllLines($Path)) {
        $l = $line.Trim()
        if ($l -eq '' -or $l.StartsWith('#')) { continue }
        if ($l.StartsWith('export ')) { $l = $l.Substring(7).TrimStart() }
        $idx = $l.IndexOf('=')
        if ($idx -lt 1) { continue }
        $k = $l.Substring(0, $idx).Trim()
        if ($k -ne $Name) { continue }
        $v = $l.Substring($idx + 1).Trim()
        if ($v.Length -ge 2 -and (($v.StartsWith('"') -and $v.EndsWith('"')) -or ($v.StartsWith("'") -and $v.EndsWith("'")))) {
            $v = $v.Substring(1, $v.Length - 2)
        }
        return $v
    }
    return $null
}

$envPath = Join-Path $brainRoot '.env'
$token = Get-EnvValue -Path $envPath -Name $TokenVar
if ([string]::IsNullOrWhiteSpace($token)) {
    Write-Host "ERRO: nao encontrei a variavel '$TokenVar' (ou esta vazia) no arquivo .env da raiz do cerebro." -ForegroundColor Red
    Write-Host "Confira o nome da variavel (-TokenVar) e se existe uma linha $TokenVar=... no .env." -ForegroundColor Red
    exit 1
}

$headers = @{
    'Authorization' = "Bearer $token"
    'Accept'        = 'application/json'
}

# --- Chamada HTTP com tratamento de erros -----------------------------------
# Retorna objeto (ou array) em caso de sucesso; em falha, grava mensagem em
# $script:LastError e $script:LastStatus e retorna $null.
$script:LastError  = ''
$script:LastStatus = 0

function Invoke-YT {
    param([string]$Url)
    $script:LastError  = ''
    $script:LastStatus = 0
    try {
        $resp = Invoke-WebRequest -Uri $Url -Headers $headers -Method Get -UseBasicParsing -TimeoutSec 60
        # Decodifica manualmente como UTF-8 (evita acentos quebrados no PS 5.1)
        $ms = New-Object System.IO.MemoryStream
        $resp.RawContentStream.Position = 0
        $resp.RawContentStream.CopyTo($ms)
        $text = [System.Text.Encoding]::UTF8.GetString($ms.ToArray())
        if ([string]::IsNullOrWhiteSpace($text)) { return ,@() }
        $obj = ConvertFrom-Json -InputObject $text
        if ($null -eq $obj) { return ,@() }
        return ,$obj
    }
    catch {
        $ex = $_.Exception
        $code = 0
        if ($ex.Response -ne $null) {
            try { $code = [int]$ex.Response.StatusCode } catch { $code = 0 }
        }
        $script:LastStatus = $code
        switch ($code) {
            401     { $script:LastError = 'HTTP 401: token invalido ou expirado.' }
            403     { $script:LastError = 'HTTP 403: token sem permissao (confira o escopo YouTrack e o acesso ao projeto).' }
            404     { $script:LastError = 'HTTP 404: recurso nao encontrado.' }
            0       {
                if ($ex.Status -eq [System.Net.WebExceptionStatus]::Timeout) {
                    $script:LastError = 'Timeout: o servidor nao respondeu a tempo.'
                } else {
                    $script:LastError = 'Falha de conexao: ' + $ex.Message
                }
            }
            default { $script:LastError = "HTTP ${code}: " + $ex.Message }
        }
        return $null
    }
}

# --- Utilitarios ------------------------------------------------------------
function Convert-Ts {
    param($Ms)
    if ($null -eq $Ms -or "$Ms" -eq '') { return '' }
    try {
        return [DateTimeOffset]::FromUnixTimeMilliseconds([int64]$Ms).UtcDateTime.ToString('yyyy-MM-dd HH:mm')
    } catch { return '' }
}

function Format-Person {
    param($P)
    if ($null -eq $P) { return '' }
    $name = ''
    if ($P.PSObject.Properties['fullName'] -and $P.fullName) { $name = [string]$P.fullName }
    $login = ''
    if ($P.PSObject.Properties['login'] -and $P.login) { $login = [string]$P.login }
    if ($name -and $login) { return "$name ($login)" }
    if ($name) { return $name }
    return $login
}

# Converte o valor de um custom field em texto
function Format-FieldValue {
    param($V)
    if ($null -eq $V) { return '' }
    if ($V -is [array]) {
        $parts = @()
        foreach ($i in $V) { $t = Format-FieldValue $i; if ($t -ne '') { $parts += $t } }
        return ($parts -join ', ')
    }
    if ($V -is [string] -or $V -is [int] -or $V -is [long] -or $V -is [double] -or $V -is [bool]) { return [string]$V }
    if ($V.PSObject.Properties['fullName'] -and $V.fullName) { return (Format-Person $V) }
    if ($V.PSObject.Properties['login'] -and $V.login) { return [string]$V.login }
    if ($V.PSObject.Properties['name'] -and $V.name) { return [string]$V.name }
    if ($V.PSObject.Properties['text'] -and $V.text) { return [string]$V.text }
    return ''
}

function Get-SafeName {
    param([string]$S)
    return ($S -replace '[\\/:*?"<>|]', '_')
}

function Escape-Cell {
    param([string]$S)
    if ($null -eq $S) { return '' }
    return (($S -replace '\|', '\|') -replace '\r?\n', ' ').Trim()
}

# --- Indice anterior (para comparar novos/atualizados) ----------------------
# Indice acumulado fica fora de raw/ (e atualizavel)
$indexPath = Join-Path $scriptDir 'youtrack_indice.md'
$prev = @{}   # ID -> @{ Title; State; Updated }
if (Test-Path -LiteralPath $indexPath) {
    foreach ($line in [System.IO.File]::ReadAllLines($indexPath, $utf8NoBom)) {
        if ($line -match '^\|\s*([A-Za-z][A-Za-z0-9]*-\d+)\s*\|(.*)\|\s*([^|]*?)\s*\|\s*$') {
            $id = $Matches[1]
            $mid = $Matches[2]
            $upd = $Matches[3]
            $cells = $mid -split '(?<!\\)\|'
            $title = ''; $state = ''
            if ($cells.Count -ge 2) { $title = $cells[0].Trim(); $state = $cells[$cells.Count - 1].Trim() }
            elseif ($cells.Count -eq 1) { $title = $cells[0].Trim() }
            $prev[$id] = @{ Title = $title; State = $state; Updated = $upd }
        }
    }
}

# --- Busca de issues (paginada) ---------------------------------------------
$issueFields = 'idReadable,summary,description,created,updated,resolved,reporter(login,fullName),project(shortName),customFields(name,value(name,login,fullName,text))'
$pageSize = 50
$skip = 0
$issues = @()

Write-Host "YouTrack: $BaseUrl"
Write-Host "Consulta: $Query"
if ($DryRun) { Write-Host 'Modo DryRun: nada sera gravado.' -ForegroundColor Yellow }

while ($true) {
    $url = $BaseUrl + '/api/issues?query=' + [uri]::EscapeDataString($Query) +
           '&fields=' + [uri]::EscapeDataString($issueFields) +
           '&$top=' + $pageSize + '&$skip=' + $skip
    $page = Invoke-YT -Url $url
    if ($null -eq $page) {
        Write-Host "ERRO ao buscar a lista de issues (skip=$skip): $script:LastError" -ForegroundColor Red
        if ($script:LastStatus -eq 401 -or $script:LastStatus -eq 403) { exit 2 }
        if ($issues.Count -eq 0) { exit 2 }
        Write-Host 'Seguindo com as issues ja obtidas.' -ForegroundColor Yellow
        break
    }
    $arr = @($page)
    $issues += $arr
    if ($arr.Count -lt $pageSize) { break }
    $skip += $pageSize
}

Write-Host ("Issues encontradas: {0}" -f $issues.Count)

if ($DryRun) {
    foreach ($i in $issues) { Write-Host ("{0}  {1}" -f $i.idReadable, $i.summary) }
    Write-Host 'DryRun concluido (nada gravado).'
    exit 0
}

if (-not (Test-Path -LiteralPath $OutDir)) { New-Item -ItemType Directory -Force -Path $OutDir | Out-Null }

# --- Processamento de cada issue --------------------------------------------
$now = (Get-Date).ToString('yyyy-MM-dd HH:mm')
$rows = @{}       # ID -> @{ Title; State; Updated }
$countOk = 0; $countNew = 0; $countUpd = 0; $countSame = 0; $countFail = 0

# Nomes de campos "principais" (primeiro encontrado vence)
$mainFields = @(
    @{ Label = 'Estado';     Names = @('State', 'Estado', 'Status') },   # projeto CT usa 'Status' (2026-10-27)
    @{ Label = 'Prioridade'; Names = @('Priority', 'Prioridade') },
    @{ Label = 'Tipo';       Names = @('Type', 'Tipo') },
    @{ Label = 'Pais';       Names = @('Country', 'Pais', 'País') },
    @{ Label = 'Cliente';    Names = @('Customer', 'Client', 'Cliente') },
    @{ Label = 'Assignee';   Names = @('Assignee', 'Assignees', 'Responsavel', 'Responsável') }
)

foreach ($i in $issues) {
    $id = [string]$i.idReadable
    if ([string]::IsNullOrWhiteSpace($id)) { continue }

    try {
        # Custom fields -> lista nome/valor
        $cf = @()
        if ($i.customFields) {
            foreach ($f in @($i.customFields)) {
                $cf += @{ Name = [string]$f.name; Value = (Format-FieldValue $f.value) }
            }
        }
        $usedNames = @{}
        $metaLines = @()
        $projeto = ''
        if ($i.project -and $i.project.shortName) { $projeto = [string]$i.project.shortName }
        $metaLines += "- **Projeto:** $projeto"

        $stateText = ''
        foreach ($mf in $mainFields) {
            $val = ''
            foreach ($n in $mf.Names) {
                $hit = $cf | Where-Object { $_.Name -eq $n } | Select-Object -First 1
                if ($hit -and $hit.Value -ne '') { $val = $hit.Value; $usedNames[$hit.Name] = $true; break }
            }
            if ($mf.Label -eq 'Estado') { $stateText = $val }
            $metaLines += ("- **{0}:** {1}" -f $mf.Label, $val)
        }
        foreach ($f in $cf) {
            if (-not $usedNames.ContainsKey($f.Name) -and $f.Value -ne '') {
                $metaLines += ("- **{0}:** {1}" -f $f.Name, $f.Value)
            }
        }
        $metaLines += ("- **Reporter:** {0}" -f (Format-Person $i.reporter))
        $metaLines += ("- **Criado:** {0} UTC" -f (Convert-Ts $i.created))
        $metaLines += ("- **Atualizado:** {0} UTC" -f (Convert-Ts $i.updated))
        $metaLines += ("- **Resolvido:** {0}" -f $(if ($i.resolved) { (Convert-Ts $i.resolved) + ' UTC' } else { '' }))
        $metaLines += ("- **URL:** {0}/issue/{1}" -f $BaseUrl, $id)

        # Comentarios
        $comments = @()
        $curl = $BaseUrl + '/api/issues/' + $id + '/comments?fields=' + [uri]::EscapeDataString('text,created,author(login,fullName)') + '&$top=500'
        $cres = Invoke-YT -Url $curl
        $commentsFailed = $false
        if ($null -eq $cres) {
            Write-Host ("  [{0}] aviso: nao foi possivel obter comentarios. {1}" -f $id, $script:LastError) -ForegroundColor Yellow
            $commentsFailed = $true
        } else {
            $comments = @($cres) | Sort-Object { [int64]$_.created }
        }

        # Anexos (somente nomes)
        $attachments = @()
        $aurl = $BaseUrl + '/api/issues/' + $id + '/attachments?fields=' + [uri]::EscapeDataString('name,created')
        $ares = Invoke-YT -Url $aurl
        $attachFailed = $false
        if ($null -eq $ares) {
            Write-Host ("  [{0}] aviso: nao foi possivel obter anexos. {1}" -f $id, $script:LastError) -ForegroundColor Yellow
            $attachFailed = $true
        } else {
            $attachments = @($ares)
        }

        # Monta o Markdown
        $sb = New-Object System.Text.StringBuilder
        [void]$sb.AppendLine("# $id - $($i.summary)")
        [void]$sb.AppendLine('')
        [void]$sb.AppendLine("> Gerado por youtrack_fetch.ps1 em $now. Copia atualizavel: sera sobrescrita na proxima execucao. Nao editar aqui.")
        [void]$sb.AppendLine('')
        [void]$sb.AppendLine('## Metadados')
        foreach ($m in $metaLines) { [void]$sb.AppendLine($m) }
        [void]$sb.AppendLine('')
        [void]$sb.AppendLine('## Descricao')
        [void]$sb.AppendLine('')
        if ($i.description) { [void]$sb.AppendLine([string]$i.description) } else { [void]$sb.AppendLine('_(sem descricao)_') }
        [void]$sb.AppendLine('')
        [void]$sb.AppendLine('## Comentarios')
        [void]$sb.AppendLine('')
        if ($commentsFailed) {
            [void]$sb.AppendLine('_(falha ao obter comentarios nesta execucao)_')
        } elseif ($comments.Count -eq 0) {
            [void]$sb.AppendLine('_(sem comentarios)_')
        } else {
            foreach ($c in $comments) {
                [void]$sb.AppendLine(("### {0} - {1} UTC" -f (Format-Person $c.author), (Convert-Ts $c.created)))
                [void]$sb.AppendLine('')
                [void]$sb.AppendLine([string]$c.text)
                [void]$sb.AppendLine('')
            }
        }
        [void]$sb.AppendLine('## Anexos')
        [void]$sb.AppendLine('')
        if ($attachFailed) {
            [void]$sb.AppendLine('_(falha ao obter anexos nesta execucao)_')
        } elseif ($attachments.Count -eq 0) {
            [void]$sb.AppendLine('_(sem anexos)_')
        } else {
            foreach ($a in $attachments) {
                [void]$sb.AppendLine(("- {0} ({1} UTC)" -f $a.name, (Convert-Ts $a.created)))
            }
        }

        $file = Join-Path $OutDir ((Get-SafeName $id) + '.md')
        [System.IO.File]::WriteAllText($file, $sb.ToString(), $utf8NoBom)

        $updText = Convert-Ts $i.updated
        $rows[$id] = @{ Title = [string]$i.summary; State = $stateText; Updated = $updText }
        $countOk++

        if (-not $prev.ContainsKey($id)) { $countNew++; $tag = 'novo' }
        elseif ($prev[$id].Updated -ne $updText) { $countUpd++; $tag = 'atualizado' }
        else { $countSame++; $tag = 'sem mudanca' }
        Write-Host ("  {0}  [{1}]  {2}" -f $id, $tag, $i.summary)
    }
    catch {
        $countFail++
        Write-Host ("  [{0}] ERRO ao processar: {1}" -f $id, $_.Exception.Message) -ForegroundColor Red
    }
}

# --- Indice (mescla com entradas anteriores que nao vieram nesta execucao) --
$all = @{}
foreach ($k in $prev.Keys) { $all[$k] = $prev[$k] }
foreach ($k in $rows.Keys) { $all[$k] = $rows[$k] }

$idx = New-Object System.Text.StringBuilder
[void]$idx.AppendLine('# Indice de tickets (YouTrack)')
[void]$idx.AppendLine('')
[void]$idx.AppendLine("> Gerado por youtrack_fetch.ps1 em $now. Consulta da ultima execucao: ``$Query``")
[void]$idx.AppendLine('')
[void]$idx.AppendLine('| ID | Titulo | Estado | Atualizado |')
[void]$idx.AppendLine('|---|---|---|---|')
$sorted = $all.Keys | Sort-Object { $all[$_].Updated } -Descending
foreach ($k in $sorted) {
    $r = $all[$k]
    [void]$idx.AppendLine(("| {0} | {1} | {2} | {3} |" -f $k, (Escape-Cell $r.Title), (Escape-Cell $r.State), $r.Updated))
}
[System.IO.File]::WriteAllText($indexPath, $idx.ToString(), $utf8NoBom)

# --- Resumo -----------------------------------------------------------------
Write-Host ''
Write-Host '=== Resumo ===' -ForegroundColor Cyan
Write-Host ("Baixados:     {0}" -f $countOk)
Write-Host ("Novos:        {0}" -f $countNew)
Write-Host ("Atualizados:  {0}" -f $countUpd)
Write-Host ("Sem mudanca:  {0}" -f $countSame)
if ($countFail -gt 0) { Write-Host ("Com erro:     {0}" -f $countFail) -ForegroundColor Red }
Write-Host ("Pasta:        {0}" -f $OutDir)
Write-Host ("Indice:       {0}" -f $indexPath)
