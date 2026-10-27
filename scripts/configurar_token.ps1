<#
.SYNOPSIS
  Grava o token do YouTrack em brain-service\.env (YOUTRACK_TOKEN=...).
  O token e digitado de forma oculta e nunca aparece na tela.
.EXAMPLE
  powershell -ExecutionPolicy Bypass -File .\scripts\configurar_token.ps1
#>
$ErrorActionPreference = 'Stop'
$brainRoot = Split-Path -Parent $PSScriptRoot
$envPath   = Join-Path $brainRoot '.env'

Write-Host 'Cole o token do YouTrack (comeca com perm:) e tecle Enter. Nada vai aparecer enquanto digita.'
$sec = Read-Host -AsSecureString 'Token'
$ptr = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($sec)
try { $token = [Runtime.InteropServices.Marshal]::PtrToStringBSTR($ptr).Trim() }
finally { [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($ptr) }

if ([string]::IsNullOrWhiteSpace($token)) { Write-Host 'Nenhum token informado. Nada foi gravado.' -ForegroundColor Red; exit 1 }
if (-not $token.StartsWith('perm')) { Write-Host 'Aviso: o token normalmente comeca com "perm". Gravando mesmo assim.' -ForegroundColor Yellow }

# Mantem outras variaveis do .env, troca so a linha YOUTRACK_TOKEN
$lines = @()
if (Test-Path -LiteralPath $envPath) {
    $lines = @([System.IO.File]::ReadAllLines($envPath) | Where-Object { $_ -notmatch '^\s*YOUTRACK_TOKEN\s*=' })
}
$lines += "YOUTRACK_TOKEN=$token"
[System.IO.File]::WriteAllLines($envPath, $lines, (New-Object System.Text.UTF8Encoding($false)))
$token = $null

Write-Host "Token gravado em $envPath" -ForegroundColor Green
Write-Host 'Volte ao Claude e diga "pronto".'
