#!/usr/bin/env python3
"""LostHex skills installer — copies skills/losthex* (+ their references/) into the Hermes skills dir.

Idempotent, overwrite-on-conflict. No machine-specific paths: target comes from $HERMES_HOME.
Usage: python scripts/install_skills.py [--dry-run]
"""
import os, shutil, sys

# Files every skill gets a copy of, so a skill is self-contained wherever it is
# read from: scripts/gate.py = the runtime HexStrike health gate.
SKILL_SCRIPTS = ["gate.py"]

SKILL_REFS = {  # skill -> files it reads from references/ (repo root)
    "losthex-hack": ["playbooks.md", "wstg-index.md", "mitre-index.md", "PAYLOAD_INDEX.md"],
    "losthex-methodology": ["playbooks.md", "wstg-index.md", "mitre-index.md"],
    "losthex": ["MODES.md"],
    "losthex-payloads": ["PAYLOAD_INDEX.md"],
}

def hermes_home():
    h = os.environ.get("HERMES_HOME")
    if h:
        return h
    la = os.environ.get("LOCALAPPDATA")
    return os.path.join(la, "hermes") if la else os.path.expanduser("~/.hermes")

def main():
    dry = "--dry-run" in sys.argv
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    src, dst = os.path.join(root, "skills"), os.path.join(hermes_home(), "skills")
    print(f"src: {src}\ndst: {dst}")
    os.makedirs(dst, exist_ok=True)
    n = 0
    for name in sorted(os.listdir(src)):
        if not name.startswith("losthex"):
            continue
        s, d = os.path.join(src, name), os.path.join(dst, name)
        if dry:
            print(f"[dry] {name}")
        else:
            shutil.copytree(s, d, dirs_exist_ok=True)
            print(f"[ok]  {name}")
        n += 1
        for f in SKILL_SCRIPTS:
            sf = os.path.join(root, "scripts", f)
            if os.path.exists(sf) and not dry:
                sd = os.path.join(d, "scripts")
                os.makedirs(sd, exist_ok=True)
                shutil.copy2(sf, os.path.join(sd, f))
        for f in SKILL_REFS.get(name, []):
            sf = os.path.join(root, "references", f)
            if os.path.exists(sf) and not dry:
                rd = os.path.join(d, "references")
                os.makedirs(rd, exist_ok=True)
                shutil.copy2(sf, os.path.join(rd, f))
    print(f"{n} skills -> {dst}")
    print("next: python scripts/verify.py")

if __name__ == "__main__":
    main()
