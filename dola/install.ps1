Write-Host "== LostHex install (Windows) =="
Write-Host "[1/4] Node 22 + Python 3.12 check"
node -v; python -V; git --version
Write-Host "[2/4] HexStrike AI"
if (!(Test-Path hexstrike-ai)) { git clone https://github.com/0x4m4/hexstrike-ai.git }
Set-Location hexstrike-ai
python -m venv .venv
.\.venv\Scripts\pip install -r requirements.txt
Write-Host "  run: .\.venv\Scripts\python.exe -E hexstrike_server.py  # -> 127.0.0.1:8888"
Set-Location ..
Write-Host "[3/4] CyberStrike"
npm install -g @cyberstrike-io/cyberstrike
npm install -g @cyberstrike-io/cyberstrike-windows-x64
cyberstrike --version; if (!$?) { cyberstrike.CMD --version }
Write-Host "[4/4] LostHex skills -> copy skills/losthex* to %LOCALAPPDATA%\hermes\skills"
Write-Host "  Copy-Item -Recurse skills\losthex* $env:LOCALAPPDATA\hermes\skills\"
Write-Host "[verify] python .\scripts\verify.py"
