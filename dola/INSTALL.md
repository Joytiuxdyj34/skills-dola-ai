# 📦 INSTALL — ติดตั้ง LostHex แบบละเอียด

> **อ่าน 5 นาที ทำตามทีละขั้น — ติดตรงไหนมีวิธีแก้ให้ทุกจุด**  
> **5 minutes here saves an hour of debugging. Follow step by step.**

---

## 📚 สารบัญ / Contents

- [0) เช็คก่อนว่ามีอะไรแล้ว](#0-เช็คก่อนว่ามีอะไรแล้ว--pre-check)
- [1) วางสกิลเข้า Hermes](#1-วางสกิลเข้า-hermes--install-skills)
- [2) HexStrike 150 Tools — มือยิง](#2-hexstrike-150-tools--มือยิง)
- [3) CyberStrike — สมองเสริม (ข้ามได้)](#3-cyberstrike--สมองเสริม-ข้ามได้--optional)
- [4) Tools พื้นฐานเพิ่มเติม](#4-tools-พื้นฐานเพิ่มเติม--extra-tools)
- [5) ตรวจว่าพร้อม — Verify](#5-ตรวจว่าพร้อม--verify)
- [6) อัปเดต / Troubleshooting](#6-อัปเดต--update--troubleshooting)

---

## 0) (Windows) ลง WSL2 + Kali ก่อน — 5 นาทีจบ / WSL2 First

> **ข้ามได้ถ้าใช้ Linux/macOS อยู่แล้ว — ขั้นนี้สำหรับ Windows เท่านั้น**  
> **Skip if you're on Linux/macOS — Windows only.**

```powershell
# PowerShell — รันทีละบรรทัด (ไม่ต้อง admin ถ้า wsl --update ผ่าน)
wsl --version          # ถ้าไม่มี -> wsl --update
wsl --update           # อัปเดต kernel (ครั้งแรกอาจต้องรอ 1-2 นาที)
wsl --install -d kali-linux --no-launch
# ถ้าติดตั้งแล้วขึ้น "already installed" คือมีแล้ว ข้ามไปได้เลย

# เข้า Kali ครั้งแรก / Enter Kali first time
wsl -d kali-linux
```

ใน Kali (prompt เปลี่ยนเป็น `root@...`):

```bash
sudo apt update
sudo apt install -y nmap ffuf gobuster nuclei sqlmap hydra john hashcat \
  whatweb amass subfinder httpx dnsx impacket-scripts bloodhound smbclient
exit
# กลับมา Windows — WSL2 พร้อมแล้ว / Back to Windows — WSL2 ready
wsl --list --verbose  # ต้องเห็น kali-linux Running/Stopped
```

> **มี WSL2 อย่างเดียวไม่พอ:** HexStrike MCP เปิด endpoint 150 รายการ แต่แต่ละรายการต้องมี binary/dependency ใน environment ที่รัน server ด้วย ส่วนนี้ติดตั้งชุดหลักใน Kali; ใช้ `wsl-setup/setup-kali-tools.sh` สำหรับชุดเพิ่ม
> Windows PATH กับ Kali PATH แยกกัน — server จะรันและตรวจ binaries ใน Kali/WSL2 โดยตรง

---

## 0b) เช็คก่อนว่ามีอะไรแล้ว / Pre-check

เปิด terminal แล้วรัน — ถ้าขึ้นเวอร์ชันคือมีแล้ว ข้ามไปได้เลย

```bash
node -v        # ต้องขึ้น v22.x  — ถ้าไม่มี ดูข้างล่าง
python -V      # ต้องขึ้น Python 3.12.x
git --version  # ต้องขึ้น git version ...
hermes --version  # ต้องขึ้น Hermes ...
```

### ถ้ายังไม่มี / If missing

| ตัว / Tool | Windows | macOS | Linux / WSL2 Kali |
|---|---|---|---|
| **Node 22** | [nodejs.org](https://nodejs.org) หรือ `winget install OpenJS.NodeJS` | `brew install node@22` | `curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash - && sudo apt install -y nodejs` |
| **Python 3.12** | [python.org](https://python.org) หรือ `winget install Python.Python.3.12` | `brew install python@3.12` | `sudo apt install -y python3 python3-venv python3-pip` |
| **Git** | [git-scm.com](https://git-scm.com) | `brew install git` | `sudo apt install -y git` |
| **Hermes** | [hermes-agent.nousresearch.com/docs](https://hermes-agent.nousresearch.com/docs) | — | — |

> 💡 **Windows ทริค:** ถ้าลง Node/Python แบบ portable (zip) อย่าลืมเพิ่มเข้า `PATH` — ไม่งั้น `node -v` จะหาไม่เจอ

---

## 1) วางสกิลเข้า Hermes / Other Harnesses

> ใช้ harness อื่น? ดู [AGENTS.md](./AGENTS.md) หรือ `python ./scripts/harness.py --install <harness>`
> Hermes = `/LostHex`, Cursor/Claude Code/OpenCode ก็ได้ — หรืออ่าน `SKILL.md` ตรงๆ แบบ generic

**WorkBuddy AI:**

```bash
python ./scripts/install_workbuddy.py          # ติดตั้ง + แก้ต้นทางใน skills/ ให้ด้วย
python ./scripts/install_workbuddy.py --dry-run
```

สคริปต์นี้ทำ 2 อย่างในรันเดียว — **แก้ `skills/*/SKILL.md` ใน repo ให้ถูกต้องก่อน** (ชื่อ tool ของ WorkBuddy คือ
`mcp__hexstrike-ai__*`, ไม่ใช่ `mcp__hexstrike_ai_*`; ตัดคำสั่ง `hermes` ที่รันไม่ได้; แทรก operating
contract) แล้วคัดลอกลง `~/.workbuddy-ai/skills/` พร้อม `scripts/gate.py` และ `references/` ที่แต่ละสกิลเรียกใช้

รันซ้ำได้ไม่ทับซ้อน (idempotent) — รอบสองจะขึ้น `0 repo SKILL.md normalised in place`


---

## 1) Hermes (native) / Install Skills

### 0) เอา repo มา / Get the repo

> repo อยู่บน Cloudflare Workers git server (GitHub เดิมโดนระงับ) — เลือกทางใดทางหนึ่ง

```bash
# ทางที่ 1 — git clone (anonymous read)
git clone https://losthex-git.lostsky777.workers.dev/losthex-skills.git
cd LostHex-Skills
```

```bash
# ทางที่ 2 — ไม่มี git: โหลด zip จากเว็ปแล้วแตก
# https://losthex-skills.pages.dev/LostHex-Skills.zip
```

```bash
# ทางที่ 3 — เน็ตถูกบล็อก: bundle สำรอง (มีทุก commit)
git clone LostHex-Skills-latest.bundle LostHex-Skills
```

### วิธีที่ง่ายที่สุด — ก็อปปี้ตรงๆ / Easiest — direct copy

```bash
# Windows / Linux / macOS / WSL2 — ใช้ installer (คัดสกิล + references/ ให้ครบ)
python ./scripts/install_skills.py

# หรือก็อปเองแบบ manual (ระวัง: ไม่ได้ copy references/ ให้)
# PowerShell: Copy-Item -Recurse skills\losthex* $env:LOCALAPPDATA\hermes\skills\
# Linux:      cp -r skills/losthex* ~/.local/share/hermes/skills/
```

### ตรวจว่าเข้าแล้ว / Verify

1. รีสตาร์ท Hermes 1 ครั้ง / Restart Hermes once
2. พิมพ์ `/` ในแชท — ต้องเห็น `/LostHex`, `/LostHex-HACK`, `/LostHex-METHOD` … ขึ้นมา 26 อัน
3. ถ้าไม่ขึ้น → ลองเช็ค path:

```bash
# ดูว่าสกิลอยู่ถูกที่ไหม
ls $LOCALAPPDATA/hermes/skills/ | grep losthex   # Windows
ls ~/.local/share/hermes/skills/ | grep losthex  # Linux
```

> ถ้ายังไม่ขึ้น — ลอง `hermes skills list | grep losthex` ดูว่า Hermes เจอไหม

---

## 2) HexStrike 150 Tools — มือยิง

> **ทำไมต้องลง?** `/LostHex-HACK` ออโต้จะสั่ง `nmap`, `ffuf`, `nuclei`, `sqlmap` ฯลฯ ผ่าน HexStrike — ถ้าไม่ลงจะ fallback เป็น `curl` มือ ช้าลง ~40%

### 2.1 Clone + สร้าง venv

```bash
# โคลน
git clone https://github.com/0x4m4/hexstrike-ai.git
cd hexstrike-ai

# สร้าง venv + ลง deps
python -m venv .venv

# Windows
.venv\Scripts\pip install -r requirements.txt
# Linux / Kali
.venv/bin/pip install -r requirements.txt
```

เปิด HexStrike ด้วย `start-hexstrike.bat` ที่ราก repo นี้ (ดับเบิลคลิก) — สคริปต์จะหา
`wsl-setup\start-kali.sh` จากตำแหน่งไฟล์ตัวเอง และหา HexStrike checkout ที่
`%USERPROFILE%\hexstrike-ai` โดยอัตโนมัติ

> 📍 **ถ้า clone ไว้ที่อื่น หรือ HexStrike อยู่คนละที่** — ตั้งค่าแล้วรันใหม่:
> ```
> set HEXSTRIKE_REPO_WIN=D:\tools\hexstrike-ai
> start-hexstrike.bat
> ```
> ไม่มี path ไหน hardcode ไว้ในไฟล์ — ย้ายโฟลเดอร์ได้ตามใจ

ส่วน `scripts/gate.py` จะพยายามเปิด Kali/WSL และ HexStrike ให้อัตโนมัติก่อนรายงานว่า FAIL

> 🔁 **ถ้าขึ้น `Address already in use` ที่พอร์ต 8888** — ดับเบิลคลิก `start-hexstrike.bat` ซ้ำ
> มันจัดการเองได้: ถ้า `/health` ไม่ตอบภายใน 12 วิ มันจะ `wsl --shutdown` ล้าง relay ของ WSL
> (`wslrelay.exe` ที่ยึดพอร์ตใน VM — ตอบ 502 และ **มองไม่เห็นด้วย `ps` ใน Kali**) แล้วสตาร์ทใหม่
> และยืนยัน `/health` จากฝั่ง Windows ให้
> ตัวสคริปต์ฝั่ง Kali อยู่ที่ `wsl-setup\start-kali.sh` (probe loopback, ต้องได้ JSON จาก `/health`
> ก่อนนับว่าสำเร็จ, reap holder ที่ค้าง, หมุน log ที่ 8 MB)


### 2.2 รัน Server

```bash
# Windows — ใส่ -E ด้วย! (สำคัญมาก ดู pitfall ข้างล่าง)
.venv\Scripts\python.exe -E hexstrike_server.py
# -> ต้องขึ้น Flask on 127.0.0.1:8888

# Linux / Kali
.venv/bin/python -E hexstrike_server.py
```

> ⚠️ **Pitfall ยอดฮิต:** ถ้ารันแล้วเจอ `mcp_types` import error — ลืมใส่ `-E`  
> Hermes ตั้ง `PYTHONPATH` ทับ venv ทำให้ `mcp` import เพี้ยน — ใส่ `-E` เสมอ

ปล่อย server รันค้างไว้ — เปิดอีก terminal ทำขั้นต่อไป / Keep it running, open another terminal.

### 2.3 ต่อ MCP เข้า Hermes

```bash
# Windows — ใส่ python แบบ absolute path + -E หน้า args เสมอ
hermes mcp add hexstrike-ai \
  --command "C:/path/to/hexstrike-ai/.venv/Scripts/python.exe" \
  --connect-timeout 180 \
  --args -E C:/path/to/hexstrike-ai/hexstrike_mcp.py --server http://127.0.0.1:8888

# Linux
hermes mcp add hexstrike-ai \
  --command "/path/to/hexstrike-ai/.venv/bin/python" \
  --connect-timeout 180 \
  --args -E /path/to/hexstrike-ai/hexstrike_mcp.py --server http://127.0.0.1:8888
```

เมื่อถาม `Enable all 150 tools?` → ตอบ `Y`

### 2.4 ตรวจ / Verify

```bash
hermes mcp test hexstrike-ai
# ต้องขึ้น ✓ Connected  +  ✓ Tools discovered: 150
```

| ขึ้นอะไร / Output | แปลว่า / Means | แก้ยังไง / Fix |
|---|---|---|
| `✓ Connected, 150 tools` | พร้อมแล้ว / Ready | ลุยได้เลย |
| `timeout` | server ยังไม่รัน หรือ cold start ช้า | เช็คว่า `hexstrike_server.py` รันอยู่ + ใส่ `--connect-timeout 180` |
| `mcp_types error` | ลืม `-E` | ใส่ `-E` หน้า python |
| `150 MCP tools` แต่บางตัวรันไม่ได้ | tool endpoint ถูก register แล้ว แต่ binary/dependency ของมันยังไม่มีใน server runtime | ดู `tools_status` จาก `/health`; ติดตั้ง binary ที่ขาดใน Kali/WSL2 แล้ว refresh ด้วย `/health?refresh=1` |

---

## 3) CyberStrike — สมองเสริม (ข้ามได้) / Optional

> **ไม่บังคับ!** Hermes ที่คุยอยู่นี่คือสมองหลักแล้ว  
> CyberStrike เป็นแค่สมองที่ 2 — จะรัน `cyberstrike` CLI เพียวๆ ถึงค่อยต้องมี LLM key  
> **Optional!** Hermes IS the main brain. Only need a key if you run `cyberstrike` CLI standalone.

```bash
# ลงตัวหลัก
npm install -g @cyberstrike-io/cyberstrike

# ⚠️ ต้องลง platform binary แยก — ตัวหลักเป็นแค่ launcher!
# Windows
npm install -g @cyberstrike-io/cyberstrike-windows-x64
# Linux / Kali
npm install -g @cyberstrike-io/cyberstrike-linux-x64
```

```bash
# ตรวจ
cyberstrike --version        # ต้องขึ้น 1.1.16+
# ถ้า git-bash เพี้ยน
cyberstrike.CMD --version
```

### ถ้าจะรัน CLI เพียวๆ ค่อยตั้ง key / Only if you run CLI standalone

```bash
cyberstrike auth login
# หรือ
export ANTHROPIC_API_KEY=sk-ant-...
# หรือ
export OPENAI_API_KEY=sk-...
```

> ถ้าใช้ผ่าน `/LostHex-HACK` ใน Hermes — ข้ามขั้นนี้ไปได้เลย / If you use `/LostHex-HACK` in Hermes, skip this.

---

## 4) Tools พื้นฐานเพิ่มเติม / Extra Tools

> บางโหมดเรียก binary ตรง — ถ้า HexStrike ไม่มีตัวนั้นในเครื่อง จะ fallback เป็น manual  
> ดูตารางเต็ม → **[TOOLS.md](./TOOLS.md)**

**Kali / WSL2 — ลงครบสุด (แนะนำ):**

```bash
sudo apt update && sudo apt install -y \
  nmap ffuf gobuster nuclei sqlmap hydra john hashcat \
  whatweb masscan amass subfinder httpx dnsx \
  impacket-scripts bloodhound smbclient enum4linux-ng

go install github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
```

**Windows — ใช้ HexStrike dispatch เป็นหลัก**  
บางตัวไม่มีบน Windows (hydra, john, wpscan, responder …) — ใช้ Kali/WSL2 จะได้ครบ

---

## 5) ตรวจว่าพร้อม / Verify

```bash
# ปกติ — ต้อง PASS ถึงจะรัน full mode ได้
python ./scripts/verify.py

# ถ้าลง tools ไม่ได้ — degraded ก็พอ
python ./scripts/verify.py --degraded

# ดูละเอียด
python ./scripts/verify.py --verbose

# runtime gate — เช็ค HexStrike ที่รันอยู่จริง (ฝังมากับทุกสกิล)
python scripts/gate.py
```

ต้องขึ้น:

```
[ok] Hermes CLI
[ok] hermes skills contain losthex
[ok] hexstrike mcp: connected
[ok] cyberstrike (optional)
RESULT: PASS — พร้อมลุย /LostHex-HACK
```

ถ้ามี `[FAIL]` → กลับไปแก้ขั้นนั้นก่อน อย่าฝืนรัน

> ✅ **ติดตั้งเสร็จแล้ว → ไปต่อที่ [USAGE.md](./USAGE.md)**
> ที่นั้นมีตัวอย่าง prompt ที่ก๊อปใช้ได้เลย, ลำดับ phase ของแต่ละโหมด,
> กฎ scan budget ที่กัน timeout, และวิธีอ่านผลลัพธ์

---

## 6) อัปเดต / Update & Troubleshooting

### อัปเดต / Update

```bash
git pull
cd hexstrike-ai && git pull && .venv/Scripts/pip install -r requirements.txt
npm update -g @cyberstrike-io/cyberstrike @cyberstrike-io/cyberstrike-windows-x64
```

### ปัญหายอดฮิต / Common Issues

| อาการ / Symptom | สาเหตุ / Cause | แก้ / Fix |
|---|---|---|
| `/LostHex-*` ไม่ขึ้น | สกิลยังไม่ copy / Hermes ยังไม่ restart | กลับข้อ 1, restart Hermes |
| `mcp_types` error | `PYTHONPATH` ทับ venv | ใส่ `-E` หน้า `python` |
| `hexstrike timeout` | cold start >30s | `--connect-timeout 180` |
| `Address already in use` ที่ 8888 | relay ของ WSL ยึดพอร์ตใน VM (ตอบ 502, `ps` ใน Kali มองไม่เห็น) หรือ server เก่าค้าง | ดับเบิลคลิก `start-hexstrike.bat` อีกครั้ง — มันจะ `wsl --shutdown` แล้วสตาร์ทใหม่เอง; ถ้ายังไม่หายดูผู้ยึดด้วย `wsl -d kali-linux -- ss -tlnp "sport = :8888"` |
| nuclei/tool timeout ทั้งที่ HexStrike server ตอบ | timeout ถูกตั้งสูงกว่า server cap หรือ MCP client ตายก่อนส่งผลกลับ | ใช้ per-call `timeout` ใน MCP tool; defaults: server 240s, MCP HTTP 270s, watchdog 285s, Hermes 300s. Timeout ของ Nuclei ถูกส่งต่อถึง command executor แล้ว และ timed-out scan จะไม่ retry ซ้ำ |
| MCP ไม่เชื่อมหลัง restart | MCP client process เก่าค้าง หรือ API server ยังเริ่มต้นไม่เสร็จ | `hermes mcp test hexstrike-ai`; config ใช้ connect timeout 30s. เช็ค `http://127.0.0.1:8888/health`, จากนั้น restart Hermes session เพื่อโหลด MCP client/tool schema ใหม่ |
| `hermes mcp test` ผ่าน แต่ tool call ค้าง | MCP stdio client เก่าจาก session ก่อนหน้า | restart Hermes session เพื่อให้ Hermes สร้าง client ใหม่; server log ต้องมี `POST /api/tools/<tool>` ตอนเรียก tool |
| `/health` ตอบช้า ~20s | tool detection ไล่ probe ~150 binary ทุกครั้ง | patch cache แล้ว (`HEXSTRIKE_HEALTH_TTL=300`, refresh ด้วย `/health?refresh=1`) |
| ยิงคำสั่งเดิมแล้วได้ผลเดิมทันที | HexStrike cache ตาม command string (TTL 1 ชม.) | เปลี่ยน argument หรือ `POST /api/cache/clear` |
| gate ค้าง/ช้า | เรียก `/health` แทน process health | ใช้ `python scripts/gate.py` (เรียก `/api/process/health-check` ก่อน) |
| `cyberstrike: failed to install platform` | npm block optional dep | ลง `cyberstrike-windows-x64` แยก |
| `cyberstrike: command not found` (git-bash) | shim ต้องใช้ sed | เรียก `cyberstrike.CMD` ตรงๆ |
| `verify.py` timeout | hermes CLI ค้าง | รัน `python ./scripts/verify.py --degraded` แทน |

---

## 7) แจกจ่ายให้คนอื่น / Packaging for distribution

```bash
python scripts/make_dist.py --check   # ตรวจก่อน ไม่เขียนไฟล์
python scripts/make_dist.py           # -> dist/LostHex-Skills-<วันที่>.zip
```

`--check` จะสแกนห้า** path ที่ hardcode ชื่อผู้ใช้ไว้ในไฟล์ที่จะแจก** แล้ว FAIL ถ้าเจอ —
กันไม่ให้ `C:\Users\<ชื่อ>` หลุดไปกับ zip

**ไม่ถูกใส่ใน zip** (ตัดออกให้อัตโนมัติ):

| อะไร | ทำไม |
|---|---|
| `cfgit/` | Workers git server ของผู้เขียน (167 MB) — คนใช้ไม่ต้องมี |
| `site/` | เว็บที่ `build_site.py` generate (39 MB) |
| `.wrangler/` `.git/` `.venv/` `node_modules/` `__pycache__/` | dev artifacts |
| `PUBLISH.md` | โน้ต deploy ของผู้เขียน |

ขนาดที่ได้: **611 ไฟล์ / 8.0 MB** (จาก ~222 MB ถ้ารวมทุกอย่าง)

> **path ทั้งหมดอ้างอิงจากตำแหน่งไฟล์เอง** — `start-hexstrike.bat` หา `wsl-setup/start-kali.sh`
> จาก `%~dp0` และหา HexStrike checkout ที่ `%USERPROFILE%\hexstrike-ai` (override ด้วย
> `HEXSTRIKE_REPO_WIN`) ส่วน `scripts/gate.py` ใช้ `~` แทน path ตายตัว
> ย้ายโฟลเดอร์หรือ clone ไว้ที่ไหนก็ได้

---

<p align="center">ติดตรงไหน เปิด issue ได้เลย — หรือพิมพ์ <code>/LostHex</code> ถามในแชทก็ได้ 💬</p>
