# The released 0.5.0 x86_64 package (public), checked against the release's own SHA256SUMS. Prints the exe's path.
param([Parameter(Mandatory)][string]$Dest)
$ErrorActionPreference = 'Stop'
New-Item -ItemType Directory -Force $Dest | Out-Null
$base = 'https://github.com/SpaceCorps/play/releases/download/v0.5.0'
Invoke-WebRequest "$base/SHA256SUMS" -OutFile "$Dest\SHA256SUMS"
Invoke-WebRequest "$base/SpaceCorps2027-windows-x86_64.zip" -OutFile "$Dest\pkg.zip"
$want = (Select-String -Path "$Dest\SHA256SUMS" -Pattern ' SpaceCorps2027-windows-x86_64.zip$').Line.Split(' ')[0]
$got = (Get-FileHash "$Dest\pkg.zip" -Algorithm SHA256).Hash.ToLower()
if ($want -ne $got) { throw "sha256 mismatch: $want vs $got" }
Expand-Archive "$Dest\pkg.zip" "$Dest\x64"
$exe = Join-Path $Dest 'x64\SpaceCorps 2027\spacecorps2027.exe'
"sha256 ok ($got), exe: $exe ($((Get-Item $exe).Length) bytes)"
