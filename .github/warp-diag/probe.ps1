# What the runner has: OS build, session, the software renderer (WARP) and the debuggers. Prints facts only.
$ErrorActionPreference = 'Continue'
"os: $([Environment]::OSVersion.VersionString)  arch: $env:PROCESSOR_ARCHITECTURE  cpus: $env:NUMBER_OF_PROCESSORS"
"user: $env:USERNAME  sessionname: '$env:SESSIONNAME'  interactive: $([Environment]::UserInteractive)"
try { (Get-Process -Id $PID).SessionId | ForEach-Object { "this process session id: $_" } } catch {}
foreach ($d in 'd3d10warp.dll','d3d12.dll','dxgi.dll','d3dcompiler_47.dll','dxcompiler.dll','dxil.dll','vulkan-1.dll','opengl32.dll') {
  $p = Join-Path $env:WINDIR "System32\$d"
  if (Test-Path $p) { "{0,-20} {1}" -f $d, (Get-Item $p).VersionInfo.FileVersion } else { "{0,-20} (not in System32)" -f $d }
}
"--- display adapters (Win32_VideoController)"
Get-CimInstance Win32_VideoController | ForEach-Object { "  $($_.Name) | driver $($_.DriverVersion) | status $($_.Status)" }
"--- debuggers"
foreach ($n in 'cdb.exe','windbg.exe','dbgeng.dll','procdump.exe','procdump64.exe') {
  $c = Get-Command $n -ErrorAction SilentlyContinue
  "{0,-15} on PATH: {1}" -f $n, ($(if ($c) { $c.Source } else { '-' }))
}
Get-ChildItem 'C:\Program Files (x86)\Windows Kits','C:\Program Files\Windows Kits' -Recurse -Filter cdb.exe -ErrorAction SilentlyContinue | Select-Object -First 5 | ForEach-Object { "cdb found: $($_.FullName)" }
"--- Windows Error Reporting"
foreach ($k in 'HKLM:\SOFTWARE\Microsoft\Windows\Windows Error Reporting','HKLM:\SOFTWARE\Microsoft\Windows\Windows Error Reporting\LocalDumps') {
  if (Test-Path $k) { "$k :"; Get-ItemProperty $k | Format-List | Out-String -Width 200 | ForEach-Object { $_.Trim() } } else { "$k : (absent)" }
}
Get-Service WerSvc -ErrorAction SilentlyContinue | ForEach-Object { "WerSvc: $($_.Status) / $($_.StartType)" }
"--- tools"
foreach ($n in 'git','python','python3','cargo','rustc','choco','winget','7z','curl','dumpbin','link') {
  $c = Get-Command $n -ErrorAction SilentlyContinue
  "{0,-8} {1}" -f $n, ($(if ($c) { $c.Source } else { '-' }))
}
