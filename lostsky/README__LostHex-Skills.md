# 🐙 LostHex — Unified Offensive Skill Pack

> **พิมพ์ `/` ก็แฮกได้เลย** — รวม 106 สกิล + 898 MITRE + 125 WSTG + 33 playbooks + 150 tools ไว้ใน prefix เดียว

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Skills: 106](https://img.shields.io/badge/skills-106%20packed-red)](#-โหมดทั้งหมด--all-modes)
[![MITRE: 898](https://img.shields.io/badge/MITRE-898-critical)](#-references-มีมาให้แล้ว)
[![WSTG: 125](https://img.shields.io/badge/WSTG-4.2-blue)](#-references-มีมาให้แล้ว)
[![HexStrike: 150](https://img.shields.io/badge/HexStrike-150%20tools-black)](./TOOLS.md)
[![Hermes Agent](https://img.shields.io/badge/Hermes-Agent-6366f1)](https://hermes-agent.nousresearch.com/docs)

> LostHex bundles 106 offensive skills, 898 MITRE ATT&CK techniques, 125 OWASP WSTG tests and 150 security tools under one prefix. Dual-Brain auto mode plans with Hermes, cross-checks against CyberStrike playbooks, then executes — degraded mode works with just `curl` when tools aren't available.

---

## 📚 สารบัญ / Contents

> 🎯 **ติดตั้งเสร็จแล้ว? → [USAGE.md](./USAGE.md)** — วิธีใช้จริง, ตัวอย่าง prompt, scan budget, อ่านผลยังไง
> 📦 **จะแจกให้คนอื่น? → [INSTALL.md §7](./INSTALL.md#7-แจกจ่ายให้คนอื่น--packaging-for-distribution)** — `python scripts/make_dist.py`

- [LostHex คืออะไร?](#-losthex-คืออะไร--what-is-losthex)
- [⚠️ ก่อนเริ่ม — ต้องลงอะไรก่อน?](#️-ก่อนเริ่ม--ต้องลงอะไรก่อน--before-you-start)
- [🚀 โหมดทั้งหมด / All Modes](#-โหมดทั้งหมด--all-modes)
- [🧠 Dual-Brain คืออะไร?](#-dual-brain--สมองสองชั้น)
- [⚡ Quick Start — 3 ขั้นตอนจบ](#-quick-start--3-ขั้นตอนจบ)
- [📖 References มีมาให้แล้ว](#-references-มีมาให้แล้ว)
- [🔋 ไม่มี Tools ก็รันได้ — Degraded Mode](#-ไม่มี-tools-ก็รันได้--degraded-mode)
- [❓ FAQ](#-faq)
- [⚖️ Disclaimer](#️-disclaimer)

---

## 🧩 LostHex คืออะไร / What is LostHex

**LostHex** คือแพ็คที่ยัดทุกอย่างที่สายเจาะต้องใช้มารวมไว้ที่เดียว — ไม่ต้องจำชื่อสกิล 30+ อัน ไม่ต้องเปิด 5 repo

**LostHex is the one-pack that bundles everything a pentester needs** — no more memorizing 30+ skill names or juggling 5 repos.

| รวมอะไรบ้าง / Bundled | จำนวน / Count | มาจากไหน / Source |
|---|---|---|
| Offensive Skills | **106** | Hermes `offensive-security/*` |
| MITRE ATT&CK | **898** | Enterprise 691 + Mobile 124 + ICS 83 |
| OWASP WSTG 4.2 | **125** | 12 categories |
| Operational Playbooks | **33** | windows / linux / aws / azure / ad / llm … |
| Security Tools | **150** | HexStrike AI (MCP dispatch) |
| AI Agents | **22** | CyberStrike (optional — ไม่บังคับ) |

> 🔗 **git clone (ไม่ผ่าน GitHub — Cloudflare Workers git server):** `git clone https://losthex-git.lostsky777.workers.dev/losthex-skills.git`
> 🌐 **เว็ปอ่านออนไลน์ (static mirror):** https://losthex-skills.pages.dev — ทุกไฟล์ + search + ปุ่มโหลด zip
> สร้างใหม่ได้เอง: `python scripts/build_site.py` แล้ว `npx wrangler pages deploy site --project-name=losthex-skills`

> **Why LostHex?** One prefix replaces four scattered sources — no more switching repos, no more memorizing 30+ skill names. Install once, type `/LostHex` and go. Includes Dual-Brain auto, degraded mode for locked machines, and multi-harness support (Hermes/Cursor/Claude Code/OpenCode).

---

## ⚠️ ก่อนเริ่ม — ต้องลงอะไรก่อน / Before You Start

> **อ่านตรงนี้ก่อน 5 นาที จะไม่ต้องมานั่งแก้ทีหลัง**  
> **Read this for 5 minutes now, save an hour of troubleshooting later.**

### ขั้นต่ำที่ต้องมี / Minimum Requirements

| สิ่งที่ต้องมี / Required | เวอร์ชัน / Version | เช็คยังไง / Check | ถ้าไม่มีลงยังไง / Install |
|---|---|---|---|
| **Node.js** | 22.x | `node -v` | [nodejs.org](https://nodejs.org) หรือ `winget install OpenJS.NodeJS` |
| **Python** | 3.12 | `python -V` | [python.org](https://python.org) หรือ `winget install Python.Python.3.12` |
| **Git** | latest | `git --version` | [git-scm.com](https://git-scm.com) |
| **Hermes Agent** | latest | `hermes --version` | [hermes-agent.nousresearch.com/docs](https://hermes-agent.nousresearch.com/docs) |

### Tools ที่แนะนำให้ลงก่อนรัน `/LostHex-HACK` / Recommended before first run

| Tool | ทำอะไร / What it does | ถ้าไม่ลงจะเป็นไง / Without it |
|---|---|---|
| **HexStrike Server** | สั่ง `nmap`, `ffuf`, `nuclei`, `sqlmap` ฯลฯ ผ่าน MCP (150 ตัว) | ออโต้จะ fallback เป็น `curl + payload` มือ — ช้าลง ~40% |
| **HexStrike MCP** | ต่อ HexStrike เข้า Hermes (`hermes mcp add ...`) | พิมพ์ `/LostHex-HACK` แล้วจะขึ้นเตือนให้ติดตั้ง |
| **CyberStrike** | สมองเสริม + playbooks (optional) | **ข้ามได้** — Hermes ตัวนี้คือสมองหลักอยู่แล้ว ไม่ต้องมี LLM key |

> 💡 **ทริค / Tip:** ถ้าเครื่องลูกค้าล็อกไม่ให้ลง tools — ข้ามไปได้เลย ใช้ [Degraded Mode](#-ไม่มี-tools-ก็รันได้--degraded-mode) แทน

📖 วิธีลงแบบละเอียดทีละบรรทัด → **[INSTALL.md](./INSTALL.md)**  
🔧 ตาราง tools ทั้งหมด → **[TOOLS.md](./TOOLS.md)**

### 🪟 Windows — แนะนำให้ลง WSL2 ก่อน (5 นาที) / Recommended

> **ทำไมต้อง WSL2?** HexStrike MCP มี 150 endpoints แต่เครื่องมือแต่ละตัวต้องมี binary ใน environment ที่รัน server ด้วย; Windows PATH กับ Kali PATH แยกกัน
> **Why WSL2?** HexStrike exposes 150 MCP endpoints; install each tool binary in the server runtime. WSL2 provides the Kali runtime, not the binaries automatically.

```powershell
# PowerShell — รันครั้งเดียว (ไม่ต้องเป็น admin ก็ได้ ถ้า wsl --update ผ่าน)
wsl --update
wsl --install -d kali-linux --no-launch

# เข้า Kali ครั้งแรก / First time in Kali
wsl -d kali-linux
# ใน Kali:
sudo apt update && sudo apt install -y nmap ffuf gobuster nuclei sqlmap hydra john hashcat whatweb amass subfinder httpx dnsx
exit
```

> มี WSL2 แล้ว → HexStrike + LostHex จะรันบน Kali ได้เต็ม — ดู [TOOLS.md](./TOOLS.md) สำหรับ list เต็ม  
> เสร็จแล้วค่อยทำ Quick Start ข้างล่างต่อได้เลย

### เช็คว่าพร้อมหรือยัง / Verify

```bash
python ./scripts/verify.py          # ปกติ / normal
python ./scripts/verify.py --degraded  # ถ้าลง tools ไม่ได้ / if you can't install
# ต้องขึ้น PASS ถึงจะลุย / Must say PASS before you run /LostHex-HACK

# runtime gate (เรียกทุกครั้งก่อน /LostHex-*) — เช็ค HexStrike ที่รันอยู่
python scripts/gate.py               # ฝังมากับทุกสกิล / bundled with every skill
# gate.py = server alive? tools? MCP registered?  (health cache 300s -> ตอบทันที)
```

ถ้าต้องการเปิด HexStrike เองจากโฟลเดอร์นี้ ให้ดับเบิลคลิก `start-hexstrike.bat` (backend ทำงานใน Kali/WSL)

---

## 🚀 โหมดทั้งหมด / All Modes

> พิมพ์ `/` ในแชท Hermes แล้วเลือก — ไม่ต้องจำคำสั่งยาวๆ  
> Type `/` in Hermes chat and pick — no long commands to memorize.

| พิมพ์ / Type | สกิล / Skill | ใช้เมื่อไหร่ / When to use |
|---|---|---|
| `/LostHex-HACK` | `losthex-hack` | 🤖 **AUTO** — ใส่ target เดียว จบถึง report (Dual-Brain) |
| `/LostHex-HACK-FAST` | `losthex-hack-fast` | ⚡ **FAST** — triage ~10 นาที, ทุก call สั่ง `timeout` ได้ (serial, ไม่มี subagent) |
| `/LostHex` | `losthex` | 🏠 Hub — ไม่รู้จะเริ่มตรงไหน มาที่นี่ก่อน |
| `/LostHex-METHOD` | `losthex-methodology` | 📚 หา MITRE / WSTG / playbook ก่อนลงมือ |
| `/LostHex-RECON` | `losthex-recon` | 🔍 เก็บข้อมูล / subdomain / takeover |
| `/LostHex-WEB` | `losthex-web` | 🌐 เจาะเว็บ — SQLi, XSS, SSTI, SSRF, XXE, LFI, upload … |
| `/LostHex-API` | `losthex-api` | 🔌 API / GraphQL / BOLA / JWT / OAuth |
| `/LostHex-AD` | `losthex-ad` | 🏢 AD / Kerberos / ADCS / NTLM / Lateral |
| `/LostHex-BINARY` | `losthex-binary` | 💣 Binary / ROP / heap / kernel / sandbox |
| `/LostHex-MOBILE` | `losthex-mobile` | 📱 Android / iOS / SSL pinning bypass |
| `/LostHex-CLOUD` | `losthex-cloud` | ☁️ Container / K8s / tunneling |
| `/LostHex-CRYPTO` | `losthex-crypto` | 🔐 RSA / hash / cipher |
| `/LostHex-FORENSICS` | `losthex-forensics` | 🔬 Volatility / pcap / stego |
| `/LostHex-SPECIAL` | `losthex-special` | 🧪 AI/LLM / Smart Contract / DeFi / CTF / Race |
| `/LostHex-CTF-WEB` | `losthex-ctf-web` | 🌐 CTF web exploitation |
| `/LostHex-CTF-PWN` | `losthex-ctf-pwn` | 💣 CTF binary pwn |
| `/LostHex-CTF-CRYPTO` | `losthex-ctf-crypto` | 🔐 CTF crypto |
| `/LostHex-CTF-REVERSE` | `losthex-ctf-reverse` | 🔍 CTF reverse |
| `/LostHex-CTF-FORENSICS` | `losthex-ctf-forensics` | 🔬 CTF forensics |
| `/LostHex-CTF-OSINT` | `losthex-ctf-osint` | 🛰️ CTF OSINT |
| `/LostHex-CTF-MISC` | `losthex-ctf-misc` | 🧩 CTF misc / bashjails |
| `/LostHex-CTF-AI` | `losthex-ctf-ai` | 🤖 CTF AI/ML |
| `/LostHex-CTF-MALWARE` | `losthex-ctf-malware` | 🦠 CTF malware |
| `/LostHex-CTF-SOLVE` | `losthex-ctf-solve` | 🎯 CTF auto solver |
| `/LostHex-CTF-WRITEUP` | `losthex-ctf-writeup` | 📝 CTF writeup |
| `/LostHex-PAYLOADS` | `losthex-payloads` | 📦 PayloadsAllTheThings 66 categories |

**ตัวอย่าง / Examples:**

```
/LostHex-HACK https://target.example.com
/LostHex-METHOD WSTG-INPV          # หา input validation tests
/LostHex-METHOD T1003              # หา LSASS technique
/LostHex-RECON target.example.com
/LostHex-WEB https://target.example.com --deep
```

> **ออโต้เลือกโหมดต่อเอง / Auto-routes** — `/LostHex-HACK` เจอ `/api` → ส่งต่อ `losthex-api` เอง, เจอ `SMB/AD` → ส่งต่อ `losthex-ad` เอง ไม่ต้องพิมพ์ต่อ

---

## 🧠 Dual-Brain — สมองสองชั้น

> **ไม่ต้องมี LLM key ก็ใช้ได้** — Hermes ที่คุยอยู่นี่คือสมองหลัก  
> **No LLM key needed** — the Hermes model you're chatting with IS the brain.

```
/LostHex-HACK https://target.com
  │
  ├─ Brain A (Hermes + losthex-*)  → Plan A
  ├─ Brain B (Hermes + playbooks/WSTG/MITRE) → Plan B
  └─ Merge → เลือกทางที่ impact สูง + verify ได้ → ทำต่อ
              + เขียน evidence/dual-brain.md ว่าเลือกอะไรเพราะอะไร
```

| สถานการณ์ / Scenario | เลือกอะไร / Pick |
|---|---|
| B เจอทางที่ A มองข้าม (เช่น WSTG upload, T1003 LSASS) | เอา B |
| A/B ซ้ำกัน | เอาอันที่ verify ง่ายกว่า |
| A/B ขัดกัน | ลองทั้งคู่แบบ low-risk แล้วค่อยเลือก |

📖 รายละเอียด → `skills/losthex-hack/SKILL.md` §5

---

## ⚡ Quick Start — 3 ขั้นตอนจบ

### 🅰️ ติดตั้งจาก Cloudflare (แนะนำ / Recommended)

> repo ย้ายมา Cloudflare แล้ว (GitHub เดิมโดนระงับ) — clone จาก Workers git server หรือโหลด zip จากเว็ป

```bash
# ทางที่ 1 — git clone (anonymous read ไม่ต้องมี credential)
git clone https://losthex-git.lostsky777.workers.dev/losthex-skills.git
cd LostHex-Skills
python ./scripts/install_skills.py   # คัดสกิล + references/ + scripts/gate.py ลง Hermes skills dir
python ./scripts/gate.py             # gate = HexStrike health check
# PASS → พิมพ์ /LostHex-HACK ได้เลย
```

```bash
# ทางที่ 2 — ไม่มี git: โหลด zip จากเว็ปแล้วแตก
# https://losthex-skills.pages.dev/LostHex-Skills.zip
python ./scripts/install_skills.py
```

```bash
# ทางที่ 3 — เน็ตถูกบล็อก: ใช้ bundle สำรอง (มีทุก commit)
git clone LostHex-Skills-latest.bundle LostHex-Skills
```

> เว็ปอ่านโค้ด (GitHub-style, tree + search): **https://losthex-skills.pages.dev**
> พิมพ์ `/` ในแชท — ต้องเห็น `/LostHex`, `/LostHex-HACK`, `/LostHex-HACK-FAST` … ขึ้นมา **26 อัน** ถ้าไม่ขึ้น = ยังไม่วางถูกที่

### 🅱️ ติดตั้งแบบมี Tools ครบ (Full Mode)

> ⚠️ **กินพื้นที่เยอะ!** HexStrike + Kali tools + CyberStrike รวมกันกิน **~3–6 GB** (venv ~1 GB, Kali packages ~2–3 GB, CyberStrike binary ~180 MB, wordlists/cache อีก ~1 GB) — เช็คพื้นที่ก่อนลง ถ้าเครื่องเต็มแนะนำใช้ [Degraded Mode](#-ไม่มี-tools-ก็รันได้--degraded-mode) แทน


> อยากให้ออโต้ยิง `nmap/nuclei/sqlmap` ได้ — ทำเพิ่มขั้นนี้

```powershell
# Windows — รันครั้งเดียวจบ
powershell ./scripts/install.ps1
python ./scripts/verify.py
```

```bash
# Linux / WSL2 Kali
bash ./scripts/install.sh
python3 ./scripts/verify.py
```

> ติดตรงไหน → เปิด [INSTALL.md](./INSTALL.md) มีบอกทีละบรรทัด + วิธีแก้ pitfall ยอดฮิต

### 3️⃣ ลุยเลย / Go

```
/LostHex-HACK https://target.example.com
/LostHex-METHOD WSTG-INPV
```

### 🔄 อัปเดต / Update

```bash
# ทุก OS — remote = Cloudflare Workers git server (ไม่ใช่ GitHub แล้ว)
cd LostHex-Skills && git pull
python ./scripts/install_skills.py    # overwrite-on-conflict, includes references/ + gate.py
python ./scripts/gate.py              # ตรวจว่า HexStrike ยังขึ้น
```

---

## 📖 References มีมาให้แล้ว

> ไม่ต้องลง CyberStrike ก็อ่านได้ — ก็อปมาใส่ repo ให้แล้ว  
> No need to install CyberStrike — already bundled in this repo.

| ไฟล์ / File | อะไร / What | จำนวน / Count |
|---|---|---|
| `references/mitre-index.md` | MITRE ATT&CK (Enterprise / Mobile / ICS) | **898** |
| `references/wstg-index.md` | OWASP WSTG 4.2 (12 categories) | **125** |
| `references/playbooks.md` | Operational playbooks — windows / linux / aws / azure / ad / llm / ebpf … | **33** |

```bash
# เปิดอ่านตรงๆ ได้เลย / Read directly
cat references/wstg-index.md | grep WSTG-INPV
cat references/mitre-index.md | grep T1003
cat references/playbooks.md | grep -A 20 "ad-security"
```

หรือพิมพ์ `/LostHex-METHOD` แล้วถามเป็นภาษาคนได้เลย / Or just type `/LostHex-METHOD` and ask in plain language.

---

## 🔋 ไม่มี Tools ก็รันได้ — Degraded Mode

> เครื่องลูกค้าล็อกไม่ให้ลงอะไร? ไม่เป็นไร รันแบบนี้ได้  
> Client machine locked down? No problem — run like this.

```bash
python ./scripts/verify.py --degraded
/LostHex-HACK https://target.example.com --offline
```

- ใช้แค่ `curl` + payload ใน `references/PAYLOAD_INDEX.md` + wordlist ย่อที่ติดมากับสกิล
- ข้าม `nmap` / `nuclei` / `sqlmap` / `hydra` — ตรวจมือแทน
- Coverage ลด ~40% แต่ยังเจอ OWASP Top 10 ได้ — เหมาะสำหรับเครื่องที่ติดตั้งไม่ได้

---

## 🔌 ใช้กับ Harness อื่นได้ด้วย / Other Harnesses

> ไม่ได้ใช้ Hermes? ไม่เป็นไร — LostHex ใช้กับ harness ไหนก็ได้  
> Not on Hermes? No problem — works with any harness.

| Harness | ติดตั้ง / Install | เรียกใช้ / Trigger |
|---|---|---|
| **Hermes** | `Copy-Item skills/losthex* $env:LOCALAPPDATA/hermes/skills/` | `/LostHex-HACK` |
| **Cursor** | `python ./scripts/harness.py --install cursor` | `@LostHex` |
| **Claude Code** | `python ./scripts/harness.py --install claude-code` | `/LostHex` |
| **OpenCode** | `python ./scripts/harness.py --install opencode` | `/LostHex` |
| **Any LLM agent** | `python ./scripts/harness.py --skill losthex-hack` | อ่าน `SKILL.md` ตรงๆ / read markdown |

```bash
python ./scripts/harness.py --list              # ดูทุกโหมด
python ./scripts/harness.py --skill losthex-web # เปิดสกิลตรง
```

📖 รายละเอียด → [AGENTS.md](./AGENTS.md)

> 📤 ย้าย/mirror repo ไป host อื่น (GitLab / GitGud / self-host / bundle) → **[PUBLISH.md](./PUBLISH.md)**

## ❓ FAQ

**Q: ต้องลง CyberStrike ไหม? / Do I need CyberStrike?**  
A: ไม่ต้อง / No — Hermes ตัวนี้คือสมองหลักแล้ว CyberStrike เป็นแค่สมองเสริม จะรัน `cyberstrike` CLI เพียวๆ ถึงค่อยต้องมี LLM key

**Q: HexStrike 150 tools ต้องลงทุกตัวไหม? / Need all 150?**  
A: ไม่ต้อง / No — ลงแค่ `hexstrike-ai` repo + `pip install` ก็พอ ที่เหลือ HexStrike จะเรียก binary เท่าที่มีในเครื่อง ถ้าไม่มีมันจะบอกว่าขาดตัวไหน

**Q: ทำไมสกิลมีแค่ 26 โฟลเดอร์ แต่เขียน 106? / Why 26 folders but says 106?**  
A: 26 โฟลเดอร์ = 106 สกิลที่ยัดรวมไว้ข้างใน (เช่น `losthex-web` ยัด 26 สกิล) ถ้าแยก 106 โฟลเดอร์ พิมพ์ `/` แล้วจะสแปมจนเลือกไม่ถูก

**Q: รันบน Windows ได้ไหม? / Works on Windows?**  
A: ได้ / Yes — แต่บาง tools (hydra, john, wpscan, responder …) มีแค่บน Kali/WSL2 ถ้าอยากได้ครบ แนะนำ WSL2

---

## ⚖️ Disclaimer

For **authorized testing / CTF / lab only**. อย่าเอาไปยิงระบบที่ไม่ได้อนุญาต — ผู้ใช้รับผิดชอบการใช้งานเอง

## 🙏 Credits

- Methodology: Hermes `offensive-security/*` (106) · MITRE ATT&CK (898) / OWASP WSTG 4.2 (125) / playbooks (33) bundled from [**CyberStrike**](https://github.com/CyberStrikeus/CyberStrike) by [@CyberStrikeus](https://github.com/CyberStrikeus/CyberStrike)
- Tool dispatch: [HexStrike AI](https://github.com/0x4m4/hexstrike-ai) by [@0x4m4](https://github.com/0x4m4)
- Harness: [Hermes Agent](https://hermes-agent.nousresearch.com/docs) by Nous Research
- CTF Skills: [ljagiello/ctf-skills](https://github.com/ljagiello/ctf-skills) (MIT) — 11 CTF categories as `losthex-ctf-*`
- Payloads: [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) (MIT) — 66 categories at `payloads/PayloadsAllTheThings/` via `/LostHex-PAYLOADS`
- Packing & Dual-Brain routing: **LostHex** — hosted at https://losthex-skills.pages.dev

---

<p align="center">พิมพ์ <code>/LostHex-HACK</code> แล้วลุยได้เลย — ขอให้เจอช่องโหดๆ 🎯</p>
