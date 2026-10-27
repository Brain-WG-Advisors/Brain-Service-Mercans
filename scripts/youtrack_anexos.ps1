<#
.SYNOPSIS
  Baixa os anexos de tickets do YouTrack para raw\tickets\api\anexos\<ID>\.
  Usa o mesmo token do .env (YOUTRACK_TOKEN). O token nunca e impresso.
.EXAMPLE
  .\youtrack_anexos.ps1 -Ids SR-162,HRBS-12110
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)][string[]]$Ids,
    [string]$TokenVar = 'YOUTRACK_TOKEN',
    [string]$BaseUrl  = 'https://youtrack.hrblizz.dev'
)
$ErrorActionPreference = 'Stop'
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$brainRoot = Split-Path -Parent $PSScriptRoot

$token = $null
foreach ($line in [System.IO.File]::ReadAllLines((Join-Path $brainRoot '.env'))) {
    if ($line -match "^\s*$TokenVar\s*=\s*(.+)$") { $token = $Matches[1].Trim().Trim('"').Trim("'") }
}
if (-not $token) { Write-Host "ERRO: $TokenVar nao encontrado no .env" -ForegroundColor Red; exit 1 }
$headers = @{ Authorization = "Bearer $token"; Accept = 'application/json' }
# Com -File, "-Ids A,B" chega como um texto so: separa pela virgula
$Ids = @($Ids | ForEach-Object { $_ -split ',' } | ForEach-Object { $_.Trim() } | Where-Object { $_ })

foreach ($id in $Ids) {
    $dir = Join-Path $brainRoot "raw\tickets\api\anexos\$id"
    New-Item -ItemType Directory -Force -Path $dir | Out-Null
    $list = Invoke-RestMethod -Uri "$BaseUrl/api/issues/$id/attachments?fields=name,url,size,created" -Headers $headers
    $n = 0
    foreach ($a in @($list)) {
        $n++
        $ts   = [DateTimeOffset]::FromUnixTimeMilliseconds([int64]$a.created).UtcDateTime.ToString('yyyyMMdd-HHmm')
        $safe = ($a.name -replace '[\\/:*?"<>|]', '_')
        $file = Join-Path $dir "$ts - $safe"
        Invoke-WebRequest -Uri ($BaseUrl + $a.url) -Headers @{ Authorization = "Bearer $token" } -OutFile $file -UseBasicParsing
        Write-Host ("  {0}  {1}  ({2} bytes)" -f $id, (Split-Path $file -Leaf), (Get-Item $file).Length)
    }
    if ($n -eq 0) { Write-Host "  $id  (sem anexos)" }
}
