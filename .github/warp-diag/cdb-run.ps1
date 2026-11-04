# Start the game under cdb (a console debugger the runner image has) and print what it says at the crash.
param(
  [Parameter(Mandatory)][string]$Exe,
  [Parameter(Mandatory)][string]$Work,
  [string]$Script = "$PSScriptRoot\crash.cdb",
  [int]$TimeoutSecs = 240
)
$ErrorActionPreference = 'Continue'
$cdb = 'C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\cdb.exe'
Remove-Item -Recurse -Force $Work -ErrorAction SilentlyContinue
New-Item -ItemType Directory -Force "$Work\home", "$Work\shots", 'C:\sym' | Out-Null
$env:HOME = "$Work\home"; $env:USERPROFILE = "$Work\home"
$env:APPDATA = "$Work\home\AppData\Roaming"; $env:LOCALAPPDATA = "$Work\home\AppData\Local"
$env:SPACE3D_AUDIO = 'off'; $env:SPACE3D_EXIT_AFTER_SECS = '12'; $env:SPACECORPS_SCREEN = 'login'
$env:SPACECORPS_SHOT_EVERY = '5'; $env:SPACECORPS_SHOTS = "$Work\shots"
$p = Start-Process -FilePath $cdb -ArgumentList @('-cf', "`"$Script`"", '-o', "`"$Exe`"") -PassThru -RedirectStandardOutput "$Work\cdb.txt" -RedirectStandardError "$Work\cdb-err.txt" -WorkingDirectory (Split-Path $Exe)
if (-not $p.WaitForExit($TimeoutSecs * 1000)) { $p.Kill(); "cdb: TIMEOUT after $TimeoutSecs s" }
$p.WaitForExit()
"cdb exit code: $($p.ExitCode)"
Get-Content "$Work\cdb.txt" | ForEach-Object { $_ -replace "\x1b\[[0-9;]*m",'' } | Select-Object -First 400
Get-Content "$Work\cdb-err.txt" -ErrorAction SilentlyContinue | Select-Object -First 20
