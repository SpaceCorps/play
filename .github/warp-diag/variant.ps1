# Start the released x64 game N times with the given environment ("A=1;B=2") and print the tally.
param(
  [Parameter(Mandatory)][string]$Exe,
  [Parameter(Mandatory)][string]$Name,
  [string]$Vars = '',
  [int]$Count = 8,
  [int]$TimeoutSecs = 90
)
foreach ($kv in ($Vars -split ';' | Where-Object { $_ })) { $k, $v = $kv -split '=', 2; Set-Item "env:$k" $v }
"variant '$Name': $Vars"
$ok = 0
foreach ($i in 1..$Count) {
  $r = & "$PSScriptRoot\run-once.ps1" -Exe $Exe -Work "$env:RUNNER_TEMP\v$i" -TimeoutSecs $TimeoutSecs -Label "$Name $i"
  $r | Select-Object -SkipLast 1
  if ($r[-1].Ok) { $ok++ }
}
"TALLY $Name on $env:RUNNER_NAME ($env:ImageOS): $ok of $Count starts ran and wrote screenshots"
