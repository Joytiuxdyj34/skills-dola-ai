@echo off
setlocal EnableExtensions
title HexStrike - WSL API server

REM Single entry point. Three jobs, one file:
REM   1. hold the WSL VM open
REM   2. start hexstrike.service inside Kali
REM   3. if it will not come up, reset WSL and try once more
REM
REM WHY THE KEEPALIVE: WSL terminates a distro shortly after its last wsl.exe
REM client disconnects, and that takes hexstrike.service down with it. Without a
REM client held open, the server was healthy at the end of one run and dead a
REM minute later -- and the 12 s probe below had no client attached at all, so the
REM VM could die mid-probe.
REM
REM WHY A RESET IS EVER NEEDED: a stale WSL localhost-forwarding relay can keep
REM owning port 8888 inside the VM after the backend dies. It answers Windows
REM with 502, is invisible to `ps` inside Kali, and blocks the real server from
REM binding. `wsl --shutdown` is the only way to clear it, and that is a
REM Windows-side action -- which is why this file exists at all.

set "WSL_DISTRO=kali-linux"

where wsl.exe >nul 2>&1
if errorlevel 1 (
    echo WSL was not found. Install or enable Windows Subsystem for Linux first.
    pause
    exit /b 1
)

REM Nothing below is hardcoded to one machine. This script may be cloned anywhere and
REM the HexStrike checkout may live anywhere, so both paths are resolved at run time:
REM   HEXSTRIKE_REPO  <- %USERPROFILE%\hexstrike-ai, or HEXSTRIKE_REPO_WIN if set
REM   BOOT            <- wsl-setup\start-kali.sh next to this file
REM wslpath does the Windows-to-WSL conversion, so spaces and drive letters survive.
if not defined HEXSTRIKE_REPO_WIN set "HEXSTRIKE_REPO_WIN=%USERPROFILE%\hexstrike-ai"
for /f "usebackq delims=" %%i in (`wsl.exe -d %WSL_DISTRO% -- wslpath -u "%HEXSTRIKE_REPO_WIN%" 2^>nul`) do set "HEXSTRIKE_REPO=%%i"
for /f "usebackq delims=" %%i in (`wsl.exe -d %WSL_DISTRO% -- wslpath -u "%~dp0wsl-setup\start-kali.sh" 2^>nul`) do set "BOOT=%%i"

if not defined HEXSTRIKE_REPO (
    echo Could not resolve the HexStrike checkout path.
    echo Set it explicitly, then run again:
    echo     set HEXSTRIKE_REPO_WIN=C:\path\to\hexstrike-ai
    pause
    exit /b 1
)
if not defined BOOT (
    echo Could not resolve wsl-setup\start-kali.sh next to this file.
    pause
    exit /b 1
)

REM One detached client, minimised, holds the VM up for the rest of the run and
REM after this window closes. Skipped if one is already attached.
wsl.exe -d %WSL_DISTRO% -u root -- pgrep -f "sleep 2147483647" >nul 2>&1
if errorlevel 1 (
    echo Holding the WSL VM open...
    start "HexStrike keepalive - do not close" /min wsl.exe -d %WSL_DISTRO% -u root -- sleep 2147483647
)

echo [1/3] Starting HexStrike inside %WSL_DISTRO%...
call :boot
call :probe 12
if not errorlevel 1 goto ok

echo.
echo [2/3] Not healthy. Resetting WSL to clear a stale port 8888 relay...
wsl.exe --shutdown
%SystemRoot%\System32\timeout.exe /t 3 /nobreak >nul 2>&1
REM wsl --shutdown killed the keepalive with the VM; attach a fresh one.
start "HexStrike keepalive - do not close" /min wsl.exe -d %WSL_DISTRO% -u root -- sleep 2147483647

echo [3/3] Starting again...
call :boot
call :probe 25
if not errorlevel 1 goto ok
goto fail


:ok
echo.
echo OK - HexStrike is answering on http://127.0.0.1:8888
echo.
%SystemRoot%\System32\curl.exe -s -m 5 http://127.0.0.1:8888/health
echo.
echo.
echo The server runs inside Kali, kept alive by the minimised
echo "HexStrike keepalive" window. Closing that window stops it.
echo Stop cleanly: wsl -d %WSL_DISTRO% -u root -- systemctl stop hexstrike
pause
exit /b 0


:fail
echo.
echo [FAIL] HexStrike never answered /health.
echo   Log:     wsl -d %WSL_DISTRO% -- tail -40 /tmp/hexstrike-server.log
echo   Unit:    wsl -d %WSL_DISTRO% -u root -- systemctl status hexstrike --no-pager
echo   Holder:  wsl -d %WSL_DISTRO% -- ss -tlnp "sport = :8888"
echo   Server:  %HEXSTRIKE_REPO%/hexstrike_server.py
echo.
echo --- last 25 journal lines from hexstrike.service ---
wsl.exe -d %WSL_DISTRO% -u root -- journalctl -u hexstrike -n 25 --no-pager 2>&1
pause
exit /b 1


:boot
wsl.exe -d %WSL_DISTRO% -u root -- bash -lc "export HEXSTRIKE_REPO='%HEXSTRIKE_REPO%' HEXSTRIKE_HOST=0.0.0.0 HEXSTRIKE_PORT=8888 HEXSTRIKE_COMMAND_TIMEOUT=240 HEXSTRIKE_HEALTH_TTL=300; bash '%BOOT%'"
exit /b 0


:probe
REM Poll /health from the Windows side for %1 seconds. The Windows probe is the
REM only one that proves the whole path works, not just loopback inside Kali.
set /a p_tries=0
:probe_loop
set /a p_tries+=1
%SystemRoot%\System32\curl.exe -fsS -m 3 http://127.0.0.1:8888/health >nul 2>&1
if not errorlevel 1 exit /b 0
if %p_tries% geq %1 exit /b 1
%SystemRoot%\System32\timeout.exe /t 1 /nobreak >nul 2>&1
goto probe_loop
