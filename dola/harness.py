#!/usr/bin/env python3
"""LostHex harness adapter — use LostHex from any harness (Hermes, Cursor, Claude Code, OpenCode, generic)."""
import pathlib, sys, shutil, os, argparse, textwrap

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"

HARNESS_PATHS = {
    "hermes":      ["%LOCALAPPDATA%/hermes/skills", "~/.local/share/hermes/skills", "~/.hermes/skills"],
    "cursor":      ["~/.cursor/skills", ".cursor/skills"],
    "claude-code": ["~/.claude/skills", ".claude/skills"],
    "opencode":    ["~/.config/opencode/skills", ".opencode/skills"],
}

def list_skills():
    for d in sorted(SKILLS.iterdir()):
        if not d.is_dir(): continue
        md = d / "SKILL.md"
        if not md.exists(): continue
        txt = md.read_text(encoding="utf-8", errors="ignore")
        # extract description first line
        desc = ""
        for l in txt.splitlines():
            if "description:" in l:
                desc = l.split("description:",1)[1].strip()[:90]
                break
        print(f"{d.name:20} {desc}")

def show_skill(name):
    md = SKILLS / name / "SKILL.md"
    if not md.exists():
        # try without prefix
        md = SKILLS / f"losthex-{name}" / "SKILL.md"
    if not md.exists():
        print(f"Skill not found: {name}")
        print("Available:")
        list_skills()
        sys.exit(1)
    print(md.read_text(encoding="utf-8", errors="ignore"))

def install(harness):
    harness = harness.lower()
    if harness not in HARNESS_PATHS:
        print(f"Unknown harness: {harness}")
        print(f"Supported: {', '.join(HARNESS_PATHS)}")
        sys.exit(1)
    installed = 0
    for raw in HARNESS_PATHS[harness]:
        # expand %LOCALAPPDATA% and ~
        p = raw.replace("%LOCALAPPDATA%", os.environ.get("LOCALAPPDATA",""))
        p = os.path.expanduser(p)
        dst = pathlib.Path(p)
        if not dst.parent.exists() and dst.as_posix().startswith(os.path.expanduser("~")):
            # generic: try cwd relative first
            pass
        # prefer first existing parent or cwd
        found = False
        for cand_raw in HARNESS_PATHS[harness]:
            c = cand_raw.replace("%LOCALAPPDATA%", os.environ.get("LOCALAPPDATA",""))
            c = os.path.expanduser(c)
            # also try relative to cwd
            rel = pathlib.Path(cand_raw.replace("%LOCALAPPDATA%","."))
            for cand in [pathlib.Path(c), ROOT / rel]:
                if cand.parent.exists() or cand.as_posix().startswith("."):
                    dst = cand
                    found = True
                    break
            if found:
                break
        # install
        for src in SKILLS.iterdir():
            if not src.is_dir(): continue
            target = dst / src.name
            if target.exists():
                shutil.rmtree(target) if target.is_dir() else target.unlink()
            shutil.copytree(src, target)
            # every installed skill carries the runtime gate
            gate = ROOT / "scripts" / "gate.py"
            if gate.exists():
                (target / "scripts").mkdir(exist_ok=True)
                shutil.copy2(gate, target / "scripts" / "gate.py")
            installed += 1
        # also copy references
        ref_src = ROOT / "references"
        ref_dst = dst / "_losthex-references"
        if ref_dst.exists():
            shutil.rmtree(ref_dst)
        shutil.copytree(ref_src, ref_dst)
        print(f"Installed {installed} skills to {dst}")
        return
    print(f"Could not find install path for {harness}")

def main():
    ap = argparse.ArgumentParser(description="LostHex harness adapter")
    ap.add_argument("--list", action="store_true", help="list all LostHex skills")
    ap.add_argument("--skill", metavar="NAME", help="print SKILL.md (e.g. losthex-hack)")
    ap.add_argument("--install", metavar="HARNESS", help="install to harness: hermes|cursor|claude-code|opencode|generic")
    ap.add_argument("--references", action="store_true", help="list reference files")
    ap.add_argument("--payload", metavar="CATEGORY", help="quick payload lookup: sqli|xss|ssrf|ssti|xxe|lfi|... (searches PayloadsAllTheThings)")
    args = ap.parse_args()
    if args.list: list_skills()
    elif args.skill: show_skill(args.skill)
    elif args.install: install(args.install)
    elif args.references:
        for f in sorted((ROOT/"references").iterdir()):
            print(f"{f.name:25} {f.stat().st_size:8} bytes")
    elif args.payload:
        pat = ROOT / "payloads/PayloadsAllTheThings"
        cat = args.payload.lower().strip()
        aliases = {
            "sqli": "SQL Injection",
            "sql": "SQL Injection",
            "xss": "XSS Injection",
            "ssrf": "Server Side Request Forgery",
            "ssti": "Server Side Template Injection",
            "xxe": "XXE Injection",
            "lfi": "File Inclusion",
            "rfi": "File Inclusion",
            "traversal": "Directory Traversal",
            "rce": "Command Injection",
            "cmdi": "Command Injection",
            "jwt": "JSON Web Token",
            "idor": "Insecure Direct Object References",
            "nosql": "NoSQL Injection",
            "nosqli": "NoSQL Injection",
            "saml": "SAML Injection",
            "openredirect": "Open Redirect",
            "redirect": "Open Redirect",
            "crlf": "CRLF Injection",
            "ssti2": "Server Side Template Injection",
        }
        # 1) alias exact first
        if cat in aliases:
            target = aliases[cat]
            matches = [d for d in pat.iterdir() if d.is_dir() and d.name.lower() == target.lower()]
        else:
            # 2) exact dir name match (case-insensitive)
            matches = [d for d in pat.iterdir() if d.is_dir() and d.name.lower() == cat.lower()]
            # 3) fallback: cat is substring of dir name with word boundary
            if not matches:
                matches = [d for d in pat.iterdir() if d.is_dir() and cat.lower() in d.name.lower()]
        if not matches:
            print(f"No payload category matching: {args.payload}")
            print("Available: (try --payload sqli|xss|ssrf|ssti|xxe|lfi|traversal|rce|jwt|idor|nosql)")
            for d in sorted(pat.iterdir()):
                if d.is_dir(): print(f"  {d.name}")
            sys.exit(1)
        for m in matches:
            print(f"=== {m.name} ===")
            readme = m / "README.md"
            if readme.exists():
                print(readme.read_text(encoding="utf-8", errors="ignore")[:4000])
            print()
    else:
        ap.print_help()
        print("\nExamples:")
        print("  python ./scripts/harness.py --list")
        print("  python ./scripts/harness.py --skill losthex-hack")
        print("  python ./scripts/harness.py --install cursor")

if __name__ == "__main__":
    main()
