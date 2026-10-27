@echo off
setlocal EnableExtensions
title Install missing Kali tools for HexStrike

REM Fills the gaps HexStrike reports as missing. Installs one package at a time so
REM a single unavailable name cannot abort the whole run.
REM
REM NOTE ON httpx: HexStrike's /health reports "httpx": true even when the binary
REM is absent -- it detects the Python httpx module, not the ProjectDiscovery CLI.
REM On Kali the package is called httpx-toolkit. That mismatch is why httpx_probe
REM returns "/bin/sh: 1: httpx: not found" while health looks green.

set "WSL_DISTRO=kali-linux"
set "PKGS=httpx-toolkit dirb feroxbuster dalfox katana arp-scan gdb xxd binutils libimage-exiftool-perl netexec evil-winrm autorecon testdisk foremost sleuthkit hashcat-utils volatility3"

where wsl.exe >nul 2>&1
if errorlevel 1 (
    echo WSL was not found. Install or enable Windows Subsystem for Linux first.
    pause
    exit /b 1
)

REM Hold the VM open; apt takes minutes and WSL kills the distro when the last
REM client disconnects.
start "HexStrike keepalive - do not close" /min wsl.exe -d %WSL_DISTRO% -u root -- sleep 2147483647

echo [1/3] apt-get update...
wsl.exe -d %WSL_DISTRO% -u root -- bash -lc "export DEBIAN_FRONTEND=noninteractive; apt-get update -qq"
if errorlevel 1 (
    echo apt-get update failed. Check networking inside Kali.
    pause
    exit /b 1
)

echo.
echo [2/3] installing (one at a time, failures are skipped)...
wsl.exe -d %WSL_DISTRO% -u root -- bash -lc "export DEBIAN_FRONTEND=noninteractive; for p in %PKGS%; do apt-get install -y -qq $p >/dev/null 2>&1 && echo   ok   $p || echo   skip $p; done"

echo.
echo [3/3] restarting hexstrike.service and refreshing tool detection...
wsl.exe -d %WSL_DISTRO% -u root -- bash -lc "systemctl restart hexstrike.service; sleep 5; curl -s 'http://127.0.0.1:8888/health?refresh=1' -o /dev/null -w 'health=%%{http_code}\n'"

echo.
echo Done. Re-check counts with:
echo   wsl -d %WSL_DISTRO% -u root -- curl -s http://127.0.0.1:8888/health
pause
