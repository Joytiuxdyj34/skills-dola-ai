#!/usr/bin/env python3
"""LostHex verify gate — ตรวจว่า tools พร้อมก่อนรัน /LostHex-HACK"""
import shutil, subprocess, sys, json, os, pathlib

def check(cmd, label):
    ok = shutil.which(cmd) is not None
    print(f"{'[ok]' if ok else '[FAIL]'} {label}: {cmd} {'found' if ok else 'MISSING'}")
    return ok

def main():
    strict = "--strict" in sys.argv
    verbose = "--verbose" in sys.argv or strict
    fail = False

    print("== LostHex verify ==")
    print("-- required --")
    if not check("hermes", "Hermes CLI"): fail = True
    if not check("python", "Python"): fail = True
    if not check("node", "Node"): fail = True
    # hermes skills
    try:
        r = subprocess.run(["hermes","skills","list"], capture_output=True, text=True, timeout=5)
        has = "losthex" in (r.stdout+r.stderr).lower()
        print(f"{'[ok]' if has else '[FAIL]'} hermes skills contain losthex: {has}")
        if not has: fail = True
    except Exception as e:
        print(f"[warn] hermes skills list skipped: {e}")
    # hexstrike mcp
    try:
        r = subprocess.run(["hermes","mcp","test","hexstrike-ai"], capture_output=True, text=True, timeout=8)
        out = r.stdout + r.stderr
        ok = "150" in out or "Connected" in out
        print(f"{'[ok]' if ok else '[FAIL]'} hexstrike mcp: {'connected' if ok else 'not connected — run hermes mcp add ...'}")
        if verbose: print(out[:600])
        if not ok and strict: fail = True
        if not ok: print("  -> ดู INSTALL.md ข้อ 2")
    except Exception as e:
        print(f"[warn] hexstrike mcp check skipped: {e}")
    # cyberstrike
    cs = shutil.which("cyberstrike") or shutil.which("cyberstrike.CMD")
    print(f"{'[ok]' if cs else '[warn]'} cyberstrike: {cs or 'not found (optional)'}")
    if strict and not cs: fail = True

    print("-- recommended --")
    for c in ["nmap","ffuf","nuclei","httpx","sqlmap"]:
        ok = shutil.which(c) is not None
        tag = "[ok]" if ok else ("[FAIL]" if strict else "[warn]")
        print(f"{tag} {c}: {'found' if ok else 'missing (via HexStrike ok)'}")
        # not fail unless strict

    if "--degraded" in sys.argv:
        print("[hint] รันแบบ degraded: ใช้ curl/payload มือโดยไม่ต้องมี HexStrike — ดู README > Degraded Mode")
    print()
    if fail and "--degraded" not in sys.argv:
        print("RESULT: FAIL — แก้ [FAIL] ก่อนรัน /LostHex-HACK")
        sys.exit(1)
    else:
        print("RESULT: PASS — พร้อมลุย /LostHex-HACK")
        if "--degraded" in sys.argv:
            print("DEGRADED: ข้าม HexStrike/CyberStrike ใช้ manual payload + curl เท่านั้น")

if __name__ == "__main__":
    main()
