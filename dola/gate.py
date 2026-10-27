#!/usr/bin/env python3
"""LostHex gate — is HexStrike alive before /LostHex-* runs?

This is the gate the skills call. It checks the running HexStrike server (the
real gate), whether Hermes has the MCP server registered, and which scan
binaries are visible to the connected HexStrike server. The repo-level scripts/verify.py is the *install* check;
this one is the *runtime* check.

    python scripts/gate.py             # normal
    python scripts/gate.py --degraded  # tools not installable -> warn only
    python scripts/gate.py --quiet     # exit code only

Exit 0 = PASS (or DEGRADED with --degraded), 1 = FAIL.
"""
import json, os, shutil, subprocess, sys, time, urllib.request

HOST = os.environ.get("HEXSTRIKE_HOST", "127.0.0.1")
PORT = os.environ.get("HEXSTRIKE_PORT", "8888")
BASE = f"http://{HOST}:{PORT}"
REQUIRED_SCAN_TOOLS = ["nmap", "nuclei", "ffuf", "httpx", "subfinder"]
WSL_DISTRO = os.environ.get("HEXSTRIKE_WSL_DISTRO", "kali-linux")
# The HexStrike checkout is not part of this repo. Resolve it instead of hardcoding
# a path: env override first, then the conventional sibling location in the user's
# home directory.
HEXSTRIKE_REPO = (os.environ.get("HEXSTRIKE_REPO")
                  or os.path.join(os.path.expanduser("~"), "hexstrike-ai"))


def get(path, timeout):
    with urllib.request.urlopen(BASE + path, timeout=timeout) as r:
        return json.loads(r.read())


def start_wsl_backend(say):
    """Wake the configured WSL distro and start HexStrike, with a bounded wait."""
    wsl = shutil.which("wsl.exe")
    if os.name != "nt" or not wsl:
        return False, "WSL auto-start is only available on Windows."
    drive, tail = os.path.splitdrive(HEXSTRIKE_REPO)
    if not drive:
        return False, f"HexStrike repository must be on a Windows drive: {HEXSTRIKE_REPO}"
    script = f"/mnt/{drive[0].lower()}{tail.replace(os.sep, '/')}/wsl-setup/start-kali.sh"
    command = (
        "export HEXSTRIKE_HOST=0.0.0.0 HEXSTRIKE_PORT=" + PORT +
        " HEXSTRIKE_COMMAND_TIMEOUT=240 HEXSTRIKE_HEALTH_TTL=300; bash " +
        __import__("shlex").quote(script)
    )
    try:
        say(f"[info] starting HexStrike in WSL/{WSL_DISTRO} (wait limit 45s)")
        # Prefer the existing systemd unit (runs as its configured unprivileged
        # account), but invoke the control action as WSL root. Starting a unit
        # is the only privileged operation here; a non-root WSL shell cannot
        # control system units and would otherwise fall through after a delay.
        try:
            unit = subprocess.run(
                [wsl, "-d", WSL_DISTRO, "-u", "root", "--", "systemctl", "start", "hexstrike.service"],
                stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL, timeout=10, check=False,
                creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
            )
        except Exception:
            unit = None
        if unit is not None and unit.returncode == 0:
            deadline = time.monotonic() + 25
            while time.monotonic() < deadline:
                try:
                    get("/api/process/health-check", 2)
                    return True, "WSL HexStrike systemd service is responding."
                except Exception:
                    time.sleep(1)

        # Fallback for installations without the systemd unit or when unit
        # startup fails: the script starts one PID-tracked WSL process.
        proc = subprocess.Popen(
            [wsl, "-d", WSL_DISTRO, "--", "bash", "-lc", command],
            stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
        )
        deadline = time.monotonic() + 20
        while time.monotonic() < deadline:
            try:
                get("/api/process/health-check", 2)
                return True, "WSL HexStrike is responding."
            except Exception:
                if proc.poll() is not None:
                    break
                time.sleep(1)
        return False, f"WSL start command exited ({proc.poll()}); check {HEXSTRIKE_REPO}\\wsl-setup\\start-kali.sh"
    except Exception as exc:
        return False, f"Could not start WSL HexStrike: {exc}"


def main():
    quiet = "--quiet" in sys.argv
    degraded = "--degraded" in sys.argv
    say = (lambda *a: None) if quiet else print
    fail = []

    say(f"== LostHex gate == {BASE}")
    # 1) server alive + tools (health payload is cached server-side, TTL 300s)
    try:
        h = get("/api/process/health-check", 10)
        say(f"[ok]   hexstrike server: {h['health_report']['overall_status']} "
            f"({h['health_report']['health_score']}/100)")
    except Exception as e:
        say(f"[warn] HexStrike is not responding yet: {e}")
        started, detail = start_wsl_backend(say)
        if started:
            try:
                h = get("/api/process/health-check", 5)
                say(f"[ok]   hexstrike server started: {h['health_report']['overall_status']} "
                    f"({h['health_report']['health_score']}/100)")
            except Exception as retry_error:
                say(f"[FAIL] HexStrike did not respond after WSL start: {retry_error}")
                say("       fallback: use --degraded for manual checks, or start the WSL service directly")
                fail.append("server")
                h = None
        else:
            say(f"[FAIL] HexStrike auto-start failed: {detail}")
            say("       fallback: run with --degraded for manual checks")
            fail.append("server")
            h = None

    tools = None
    if h:
        try:
            tools = get("/health", 60)
            avail, total = tools["total_tools_available"], tools["total_tools_count"]
            runtime = tools.get("runtime", {})
            backend = (f"WSL/{runtime['distro']}" if runtime.get("wsl")
                       else runtime.get("platform", "unknown"))
            say(f"[ok]   execution backend: {backend}")
            say(f"[ok]   detected server tools: {avail}/{total} "
                f"| essential={tools['all_essential_tools_available']}")
            missing = [k for k, v in tools["tools_status"].items() if not v]
            if missing:
                say(f"[warn] missing ({len(missing)}): {', '.join(missing[:12])}"
                    + (" ..." if len(missing) > 12 else ""))
            missing_required = [t for t in REQUIRED_SCAN_TOOLS
                                if not tools["tools_status"].get(t, False)]
            if missing_required:
                say(f"[FAIL] required scan tools missing in {backend}: "
                    f"{', '.join(missing_required)}")
                if not degraded:
                    fail.append("tools")
        except Exception as e:
            say(f"[FAIL] /health tool check failed: {e}")
            if not degraded:
                fail.append("tool-health")

    # 2) Hermes MCP registration
    config_roots = []
    if os.environ.get("HERMES_HOME"):
        config_roots.append(os.environ["HERMES_HOME"])
    if os.name == "nt" and os.environ.get("LOCALAPPDATA"):
        config_roots.append(os.path.join(os.environ["LOCALAPPDATA"], "hermes"))
    config_roots.append(os.path.expanduser("~/.hermes"))
    cfg = next((os.path.join(root, "config.yaml") for root in config_roots
                if os.path.isfile(os.path.join(root, "config.yaml"))), None)
    try:
        if not cfg:
            raise FileNotFoundError("Hermes config.yaml not found in known config locations")
        text = open(cfg, encoding="utf-8", errors="replace").read()
        if "hexstrike-ai:" in text:
            say(f"[ok]   hermes mcp: hexstrike-ai registered ({cfg})")
        else:
            say(f"[warn] hermes mcp: hexstrike-ai not in {cfg} -> hermes mcp add ...")
            if not degraded:
                fail.append("mcp")
    except Exception as e:
        say(f"[warn] config unreadable: {e}")

    # Binary availability comes from the connected server's runtime, not the
    # Windows PATH of this gate process. This matters when HexStrike runs in WSL.

    if fail and not degraded:
        say(f"\nRESULT: FAIL ({', '.join(fail)}) — fix before /LostHex-*")
        return 1
    say("\nRESULT: PASS" + (" (degraded: curl + manual payloads only)" if degraded else " — ready"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
