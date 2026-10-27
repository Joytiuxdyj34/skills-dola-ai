# 🤖 LostHex — Agent Instructions (any harness)

> **ไฟล์นี้ทำให้ harness ไหนก็ใช้ LostHex ได้ — ไม่ใช่แค่ Hermes**  
> This file lets **any harness** (Hermes, OpenCode, Claude Code, Cursor, generic agent) load LostHex.

---

## 🧩 What is LostHex

13 skills + 898 MITRE + 125 WSTG + 33 playbooks + 150 tools — one prefix: `LostHex`

- 🇹🇭 ไทย/อังกฤษ — สกิลเขียนสองภาษา อ่านภาษาไหนก็เข้าใจ
- 🧠 Dual-Brain — Hermes สมองหลัก + CyberStrike วิธีคิด (ไม่ต้องมี LLM key)
- 🪟 Windows ใช้ HexStrike server ใน Kali/WSL2; MCP เปิด 150 endpoints แต่ต้องติดตั้ง binary/dependency ของแต่ละตัวใน Kali เอง

---

## 🚀 How to Load

### Option A — Hermes (native: slash triggers)

```powershell
Copy-Item -Recurse skills\losthex* $env:LOCALAPPDATA\hermes\skills\
# Restart Hermes -> type /LostHex
```

### Option B — Other harnesses (adapter)

```bash
python ./scripts/harness.py --list                    # ดูทุกโหมด
python ./scripts/harness.py --skill losthex-hack      # เปิด SKILL.md ตรง
python ./scripts/harness.py --install cursor          # ติดตั้งเข้า Cursor
python ./scripts/harness.py --install claude-code     # ติดตั้งเข้า Claude Code
python ./scripts/harness.py --install opencode        # ติดตั้งเข้า OpenCode
```

### Option C — Generic (อ่าน markdown ตรง / read markdown)

Any agent can read skills as plain markdown — no install needed:

```
Read: USAGE.md                            # how to drive it: prompts, phases, scan budget
Read: skills/losthex-hack/SKILL.md        # auto Dual-Brain
Read: skills/losthex-methodology/SKILL.md # MITRE/WSTG/playbooks index
Read: references/mitre-index.md           # 898 ATT&CK
Read: references/wstg-index.md            # 125 WSTG
Read: references/playbooks.md             # 33 playbooks
```

> **Before calling any HexStrike tool, read `USAGE.md` §7 (scan budget).** The default
> `nmap_scan(target)` scans 1000 ports with `-sV` and burns the full 240 s server cap,
> returning nothing. Always pass explicit `ports` plus
> `additional_args="-T4 -n --max-retries 1 --host-timeout 60s"`.

---

## 🗺️ Supported Harnesses

| Harness | Install command | Trigger |
|---|---|---|
| **Hermes** | `Copy-Item skills/losthex* $env:LOCALAPPDATA/hermes/skills/` | `/LostHex-HACK` |
| **Cursor** | `python ./scripts/harness.py --install cursor` | `@LostHex` |
| **Claude Code** | `python ./scripts/harness.py --install claude-code` | `/LostHex` |
| **OpenCode** | `python ./scripts/harness.py --install opencode` | `/LostHex` |
| **Generic** | `python ./scripts/harness.py --skill <name>` | Read `SKILL.md` |
| **MCP (tools)** | `hermes mcp add hexstrike-ai ...` (150 tools) | `mcp__hexstrike_ai_*` |

---

## 📋 Modes (26)

| Skill | Trigger | Purpose |
|---|---|---|
| `losthex` | `/LostHex` | 🏠 Hub |
| `losthex-hack` | `/LostHex-HACK` | 🤖 Auto Dual-Brain full-chain |
| `losthex-hack-fast` | `/LostHex-HACK-FAST` | ⚡ Time-boxed triage, hard timeout per call |
| `losthex-methodology` | `/LostHex-METHOD` | 📚 MITRE 898 + WSTG 125 + playbooks 33 |
| `losthex-recon` | `/LostHex-RECON` | 🔍 recon / takeover |
| `losthex-web` | `/LostHex-WEB` | 🌐 web vulns |
| `losthex-api` | `/LostHex-API` | 🔌 API / GraphQL / JWT |
| `losthex-ad` | `/LostHex-AD` | 🏢 AD / Kerberos / ADCS |
| `losthex-binary` | `/LostHex-BINARY` | 💣 binary / ROP / heap |
| `losthex-mobile` | `/LostHex-MOBILE` | 📱 Android / iOS |
| `losthex-cloud` | `/LostHex-CLOUD` | ☁️ container / k8s |
| `losthex-crypto` | `/LostHex-CRYPTO` | 🔐 RSA / hash / cipher |
| `losthex-forensics` | `/LostHex-FORENSICS` | 🔬 volatility / pcap |
| `losthex-special` | `/LostHex-SPECIAL` | 🧪 AI/LLM / DeFi / CTF |
| `losthex-ctf-web` | `/LostHex-CTF-WEB` | 🌐 CTF web (ljagiello) |
| `losthex-ctf-pwn` | `/LostHex-CTF-PWN` | 💣 CTF pwn (ljagiello) |
| `losthex-ctf-crypto` | `/LostHex-CTF-CRYPTO` | 🔐 CTF crypto (ljagiello) |
| `losthex-ctf-reverse` | `/LostHex-CTF-REVERSE` | 🔍 CTF reverse (ljagiello) |
| `losthex-ctf-forensics` | `/LostHex-CTF-FORENSICS` | 🔬 CTF forensics (ljagiello) |
| `losthex-ctf-osint` | `/LostHex-CTF-OSINT` | 🛰️ CTF OSINT (ljagiello) |
| `losthex-ctf-misc` | `/LostHex-CTF-MISC` | 🧩 CTF misc (ljagiello) |
| `losthex-ctf-ai` | `/LostHex-CTF-AI` | 🤖 CTF AI/ML (ljagiello) |
| `losthex-ctf-malware` | `/LostHex-CTF-MALWARE` | 🦠 CTF malware (ljagiello) |
| `losthex-ctf-solve` | `/LostHex-CTF-SOLVE` | 🎯 CTF auto solver |
| `losthex-ctf-writeup` | `/LostHex-CTF-WRITEUP` | 📝 CTF writeup |
| `losthex-payloads` | `/LostHex-PAYLOADS` | 📦 PayloadsAllTheThings 66 cats |

---

## 📖 References (no install needed)

- `references/mitre-index.md` — 898 ATT&CK (Enterprise / Mobile / ICS)
- `references/wstg-index.md` — 125 WSTG 4.2 (12 categories)
- `references/playbooks.md` — 33 operational playbooks
- `references/PAYLOAD_INDEX.md` — quick payloads (copy-paste)
- `references/TOOL_ROUTING.md` — tool mapping (HexStrike vs degraded)

---

## 🪟 Windows — แนะนำลง WSL2 ก่อน

```powershell
wsl --update
wsl --install -d kali-linux --no-launch
wsl -d kali-linux
# ใน Kali: sudo apt install -y nmap ffuf gobuster nuclei hydra john ...
```

ดูเพิ่ม: [INSTALL.md](./INSTALL.md) §0

---

## ✅ Verify

```bash
python ./scripts/harness.py --list
python ./scripts/verify.py          # full
python ./scripts/verify.py --degraded  # ถ้าลง tools ไม่ได้
```
