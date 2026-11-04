# Start the game once and report how it ended (exit code in hex, seconds, the last game log line, screenshots).
# Environment variables of this process are inherited by the game.
param(
  [Parameter(Mandatory)][string]$Exe,
  [Parameter(Mandatory)][string]$Work,       # scratch folder for this start (HOME, shots, log)
  [int]$TimeoutSecs = 120,
  [string]$Label = 'run'
)
$ErrorActionPreference = 'Continue'
Remove-Item -Recurse -Force $Work -ErrorAction SilentlyContinue
New-Item -ItemType Directory -Force "$Work\home", "$Work\shots" | Out-Null
$env:HOME = "$Work\home"; $env:USERPROFILE = "$Work\home"
$env:APPDATA = "$Work\home\AppData\Roaming"; $env:LOCALAPPDATA = "$Work\home\AppData\Local"
$env:SPACE3D_AUDIO = 'off'; $env:SPACE3D_EXIT_AFTER_SECS = '12'; $env:SPACECORPS_SCREEN = 'login'
$env:SPACECORPS_SHOT_EVERY = '5'; $env:SPACECORPS_SHOTS = "$Work\shots"
$sw = [Diagnostics.Stopwatch]::StartNew()
$p = Start-Process -FilePath $Exe -PassThru -RedirectStandardOutput "$Work\out.txt" -RedirectStandardError "$Work\err.txt" -WorkingDirectory (Split-Path $Exe)
if (-not $p.WaitForExit($TimeoutSecs * 1000)) { $p.Kill(); "$Label: TIMEOUT after $TimeoutSecs s"; }
$p.WaitForExit()
$code = [uint32]($p.ExitCode -band 0xFFFFFFFF)
$txt = (Get-Content "$Work\out.txt","$Work\err.txt" -ErrorAction SilentlyContinue) -join "`n" -replace "\x1b\[[0-9;]*m",''
$last = ($txt -split "`n" | Where-Object { $_ -match '^20\d\d-' } | Select-Object -Last 1)
if ($last -and $last.Length -gt 130) { $last = $last.Substring(0,130) }
$n = @(Get-ChildItem "$Work\shots" -Filter 'shot_*.png' -ErrorAction SilentlyContinue).Count
"{0}: exit 0x{1:X8} after {2:N1} s, {3} screenshots, last log line: {4}" -f $Label, $code, $sw.Elapsed.TotalSeconds, $n, $last
[pscustomobject]@{ Code = $code; Shots = $n; Ok = ($code -eq 0 -and $n -gt 0) }
