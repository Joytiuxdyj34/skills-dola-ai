#!/usr/bin/env bash
set -e
echo "== LostHex install (Linux/Kali/WSL2) =="
echo "[1/4] Node 22 + Python 3.12 check"
node -v || echo "MISSING node -> install nodejs 22"
python3 -V || echo "MISSING python3"
echo "[2/4] HexStrike AI"
if [ ! -d hexstrike-ai ]; then
  git clone https://github.com/0x4m4/hexstrike-ai.git
fi
cd hexstrike-ai
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
echo "  run: .venv/bin/python -E hexstrike_server.py  # -> 127.0.0.1:8888"
cd ..
echo "[3/4] CyberStrike"
npm install -g @cyberstrike-io/cyberstrike
npm install -g @cyberstrike-io/cyberstrike-linux-x64 || npm install -g @cyberstrike-io/cyberstrike-windows-x64 || true
cyberstrike --version || echo "cyberstrike not in PATH"
echo "[4/4] LostHex skills -> copy skills/losthex* to Hermes skills dir"
echo "  cp -r skills/losthex* ~/.local/share/hermes/skills/  (หรือ %LOCALAPPDATA%/hermes/skills)"
echo "[verify] python3 ./scripts/verify.py"
