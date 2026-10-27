# 🎯 USAGE — ใช้ LostHex ยังไง

> ติดตั้งเสร็จแล้ว (ดู [INSTALL.md](./INSTALL.md)) — ไฟล์นี้คือวิธีใช้งานจริง  
> **อ่าน 5 นาที แล้วยิงงานได้เลย**

---

## 📚 สารบัญ

- [1) TL;DR — 3 บรรทัดจบ](#1-tldr--3-บรรทัดจบ)
- [2) จะเรียกสกิลยังไง (ต่างกันตาม harness)](#2-จะเรียกสกิลยังไง-ต่างกันตาม-harness)
- [3) เลือกโหมดตามงาน](#3-เลือกโหมดตามงาน)
- [4) ตัวอย่าง prompt ที่ได้ผล](#4-ตัวอย่าง-prompt-ที่ได้ผล)
- [5) หนึ่งรอบทำงานจริงเป็นยังไง](#5-หนึ่งรอบทำงานจริงเป็นยังไง)
- [6) Artifacts ไปอยู่ไหน](#6-artifacts-ไปอยู่ไหน)
- [7) Scan budget — กฎที่ทำให้ไม่ timeout](#7-scan-budget--กฎที่ทำให้ไม่-timeout)
- [8) เรียก tool ตรง ๆ (ไม่ผ่านสกิล)](#8-เรียก-tool-ตรง-ๆ-ไม่ผ่านสกิล)
- [9) Dual-Brain คืออะไร ใช้ยังไง](#9-dual-brain-คืออะไร-ใช้ยังไง)
- [10) ปัญหาที่เจอบ่อย](#10-ปัญหาที่เจอบ่อย)

---

## 1) TL;DR — 3 บรรทัดจบ

```bash
python scripts/verify.py          # 1. พร้อมไหม
start-hexstrike.bat               # 2. เปิด HexStrike (Windows)
# 3. บอกงานเป็นภาษาคน — สกิลจะ route เอง
```

> **ไม่ต้องจำชื่อสกิล** — บอกเป้าหมายเป็นภาษาธรรมชาติ เดี๋ยวมันเลือกโหมดให้

---

## 2) จะเรียกสกิลยังไง (ต่างกันตาม harness)

สกิลเดียวกัน แต่ทางเรียกต่างกัน:

| Harness | วิธีเรียก | ตัวอย่าง |
|---|---|---|
| **Hermes** | slash command | `/LostHex-RECON example.com` |
| **WorkBuddy AI** | พิมพ์เป็นภาษาคน (ไม่มี slash) | `recon example.com หา subdomain กับ tech stack` |
| **Cursor / Claude Code / OpenCode** | พิมพ์เป็นภาษาคน | `run LostHex recon on example.com` |
| **อะไรก็ได้** | อ่าน `skills/losthex-*/SKILL.md` ตรง ๆ | — |

**WorkBuddy:** สกิลจะถูกเลือกจาก `description` — พูดถึงงานจริง ๆ (recon, SQLi, AD, CTF, pwn) แล้วมันจะโหลดตัวที่ตรงให้

> ถ้าอยากบังคับโหมด ใส่ชื่อโหมดลงไปตรง ๆ: `ใช้ losthex-web หา SSRF บน https://app.target.com`

---

## 3) เลือกโหมดตามงาน

| อยากได้อะไร | โหมด | ได้อะไรกลับมา |
|---|---|---|
| อยากให้ยิงจบทั้ง chain | `losthex-hack` | recon → surface → vuln → exploit → report |
| มีเวลา 10 นาที | `losthex-hack-fast` | triage เร็ว, serial, timeout แข็ง |
| อยากรู้ว่ามีอะไรอยู่ | `losthex-recon` | subdomain, port, tech, endpoint |
| หาช่องโหว่เว็บ | `losthex-web` | SQLi, XSS, SSTI, SSRF, XXE, LFI, upload |
| API / JWT / GraphQL | `losthex-api` | BOLA, BFLA, mass assignment, token abuse |
| เน็ตเวิร์กองค์กร | `losthex-ad` | Kerberos, ADCS, ACL, NTLM relay, lateral |
| binary / ROP / kernel | `losthex-binary` | overflow, heap, format string, sandbox escape |
| มือถือ | `losthex-mobile` | Android/iOS, SSL pinning bypass, Frida |
| container / k8s | `losthex-cloud` | escape, kube audit, tunneling |
| คริปโต | `losthex-crypto` | RSA, lattice, hash extension, padding oracle |
| ตรวจเครื่อง / log | `losthex-forensics` | memory, pcap, stego, disk |
| ต้องมี payload พร้อมใช้ | `losthex-payloads` | PayloadsAllTheThings 66 หมวด |
| อยากได้ methodology | `losthex-methodology` | MITRE 898 + WSTG 125 + playbook 33 |
| CTF | `losthex-ctf-solve` → `-ctf-web` / `-pwn` / `-crypto` / `-reverse` / `-forensics` / `-misc` / `-osint` / `-ai` / `-malware` | ตามหมวด |
| เขียน writeup | `losthex-ctf-writeup` | เอกสารส่งแข่ง |

> ยังไม่แน่ใจ → เริ่มที่ `losthex-recon` หรือ `losthex-ctf-solve` (ตัวหลังเป็น dispatcher ของ CTF)

---

## 4) ตัวอย่าง prompt ที่ได้ผล

**ก๊อปไปใช้ได้เลย** — แก้แค่ target

### Recon
```
recon https://app.example.com — subdomain, port, tech stack, endpoint
สแกนพอร์ต 10.10.10.5 แบบเร็ว ๆ แล้วบอกว่ามี service อะไรน่าสนใจ
หา subdomain ของ example.com แล้วเช็ค subdomain takeover
```

### Web
```
หา SSRF กับ open redirect บน https://app.example.com
ตรวจ auth bypass กับ IDOR — มี user ปกติ 1 account: user:pass
หา SQLi ในพารามิเตอร์ของ /search
```

### API
```
audit API ที่ https://api.example.com/v1 — เน้น BOLA กับ mass assignment
ถอด JWT ที่แนบมา แล้วบอกว่า forge ได้ไหม
```

### AD / Network
```
enumerate AD จาก 10.10.10.0/24 — หา Kerberoastable ก่อน
มี credential user:pass ลอง lateral ไปเครื่องอื่น
```

### Binary / CTF
```
binary อยู่ที่ ./chall — หา offset แล้วเขียน exploit
CTF web: โจทย์อยู่ที่ http://chal.ctf.local:8080
ไฟล์ pcap อยู่ที่ ./capture.pcap — หา flag
```

> **ยิ่งบอก impact ที่อยากได้ ยิ่งได้ผล** — "หา RCE" ดีกว่า "สแกนเว็บ" เพราะมันเลือก path ได้ตรง

---

## 5) หนึ่งรอบทำงานจริงเป็นยังไง

`losthex-hack` ทำงานเป็น phase — **ห้ามข้าม และห้ามหยุดกลางทาง**

```
Phase 1  RECON      nmap + httpx + subfinder + whatweb
                    └─> assets/urls.txt, assets/tech.json

Phase 2  SURFACE    ffuf / gobuster + nuclei baseline + param mining
                    └─> assets/params.json

Phase 3  VULN       route ตามที่เจอ:
                    web → losthex-web   api → losthex-api
                    AD  → losthex-ad    binary → losthex-binary

Phase 4  EXPLOIT    เลือก 2-3 เส้นที่ impact สูงสุด
                    ทุกเส้นต้อง verify จริง (curl / sqlmap / token reuse)
                    └─> exploit/<vuln>.py  (รันซ้ำได้)

Phase 5  EVIDENCE   request/response + screenshot
                    └─> evidence/<finding>/, reports/<target>.md
```

**กติกาที่สกิลบังคับ:**

- ทำ host ปัจจุบันให้จบก่อนขยาย — ไม่กระจายตื้น ๆ หลายที่
- ทุก phase จบต้องเขียน `assets/progress.md` 1 บรรทัด แล้วไปต่อ
- tool ไหน timeout → เขียน `[skip] <tool> timeout` แล้วไปต่อ **ไม่ถาม ไม่รอ**
- confirmed finding ต้องมี script ที่รันซ้ำได้ ไม่ใช่แค่ข้อความ
- **ห้ามจบ turn หลัง Phase 1** — ต้องไปจนถึง `reports/<target>.md`

> ถ้ามันหยุดกลางทาง ให้บอกว่า `ต่อ Phase 2` — อย่าปล่อยให้จบที่ recon

---

## 6) Artifacts ไปอยู่ไหน

ทุกอย่างลงโฟลเดอร์ทำงานปัจจุบัน (ปกติคือ root ของโปรเจกต์ที่คุณเปิด):

```
assets/
  urls.txt          endpoint ที่เจอ
  tech.json         fingerprint
  params.json       พารามิเตอร์ที่เจอ
  progress.md       log ต่อ phase (1 บรรทัด/phase)

evidence/
  <finding>/
    request.txt
    response.txt
    screenshot.png
  dual-brain.md     เทปบันทึกการตัดสินใจ (Plan A vs B)

exploit/
  <vuln>.py         PoC ที่รันซ้ำได้

reports/
  <target>.md       เฉพาะที่ verify แล้ว
```

**อ่านอะไรก่อน:** `reports/<target>.md` → ถ้าอยากรู้ว่าทำไมเลือกทางนั้น ดู `evidence/dual-brain.md`

> ไม่มี finding ก็ยังได้ report — มันจะบอกว่าเทสอะไรไปบ้างและขั้นต่อไปควรทำอะไร

---

## 7) Scan budget — กฎที่ทำให้ไม่ timeout

HexStrike รันคำสั่งแบบ **synchronous** — HTTP request ค้างจนคำสั่งจบ หรือชนเพดาน 240 วิ
คำสั่งที่ใช้เวลาเกิน timeout ของ tool call จะคืน **ศูนย์ผลลัพธ์**

วัดจริงบนเครื่องทดสอบ:

| การเรียก | เวลา |
|---|---|
| `nmap_scan(target)` เปล่า ๆ (default `-sV` บน 1000 พอร์ต) | **240 วิ** — ชนเพดาน ไม่ได้อะไร |
| `nmap_scan(target, ports="22,80,443", -T4 -n)` | **2.7 วิ** |
| `nmap_advanced_scan(...)` เปล่า ๆ (เติม NSE ทั้งชุด) | **50 วิ** |

**เรียกแบบนี้เสมอ:**

```
nmap_scan(
  target="<host>",
  scan_type="-sT",
  ports="21,22,23,25,53,80,110,111,135,139,143,443,445,993,995,1433,1521,2049,3306,3389,5432,5900,6379,8000,8080,8443,8888,9200,27017",
  additional_args="-T4 -n --max-retries 1 --host-timeout 60s"
)
```

- `-sV` เปิดเฉพาะพอร์ตที่ open แล้ว
- 1000 พอร์ตเต็ม → แบ่งช่วงละ 200
- `nmap_advanced_scan` ใช้เมื่อต้องการ NSE เจาะจงเท่านั้น
- `nuclei` / `ffuf` / `feroxbuster` → ใส่ `timeout=` ต่ำกว่า 240 และจำกัด scope รอบแรก

---

## 8) เรียก tool ตรง ๆ (ไม่ผ่านสกิล)

บางทีอยากยิงคำสั่งเดียว ไม่ต้องรันทั้ง chain

### WorkBuddy AI — 150 MCP tools

สกิลจะเรียกให้เอง แต่เรียกเองได้ถ้ารู้ชื่อ:

```
nmap_scan(target="10.10.10.5", ports="22,80,443", additional_args="-T4 -n")
nuclei_scan(target="https://app.example.com", severity="critical,high", timeout=180)
ffuf_scan(url="https://app.example.com/FUZZ", mode="directory")
sqlmap_scan(url="https://app.example.com/item?id=1")
```

> ชื่อ tool ขึ้นต้นด้วย `mcp__hexstrike-ai__` เสมอ (ขีดกลาง + ขีดล่างคู่)
> อยากรู้ว่ามีอะไรบ้าง → ถามว่า "list hexstrike tools"

### Hermes / อื่น ๆ — HTTP API ตรง

```bash
curl -s http://127.0.0.1:8888/health | jq '.status, .total_tools_available'
curl -s -X POST http://127.0.0.1:8888/api/tools/nmap \
  -H "Content-Type: application/json" \
  -d '{"target":"10.10.10.5","scan_type":"-sT","ports":"22,80,443","additional_args":"-T4 -n"}'
```

---

## 9) Dual-Brain คืออะไร ใช้ยังไง

สองสมอง ไม่ต้องตั้งค่าอะไร:

```
Phase N findings
  ├─ Brain A  โมเดลที่รันอยู่ + losthex-*          → Plan A
  ├─ Brain B  เปิด references/playbooks.md,
  │           wstg-index.md, mitre-index.md
  │           ที่ตรงกับ findings                   → Plan B
  └─ Merge    เทียบ impact + verify-ability         → ไป Phase N+1
```

**กติกา merge:** B เจอ path ที่ A มองข้าม → เอา B / ซ้ำกัน → เอาอันที่ verify ง่ายกว่า / ขัดกัน → ลองทั้งคู่แบบ low-risk

ไม่ต้องมี LLM key — `references/` มีมาให้แล้ว (playbook 33 + WSTG 125 + MITRE 898)

**อยากเปิดเอง:**
```
อ่าน references/playbooks.md แล้วบอกว่า playbook ไหนตรงกับ findings นี้
```

---

## 10) ปัญหาที่เจอบ่อย

| อาการ | สาเหตุ | แก้ |
|---|---|---|
| สกิลไม่ถูกเรียกเลย | ยังไม่ติดตั้ง / harness ไม่เห็น | `ls ~/.workbuddy-ai/skills \| grep losthex` (หรือ path ของ harness) |
| เรียกแล้วไม่ทำอะไร | tool ไม่มี / gate ไม่ผ่าน | `python scripts/gate.py` |
| tool ค้างนานแล้ว timeout | สแกนใหญ่เกิน budget | ดู[ข้อ 7](#7-scan-budget--กฎที่ทำให้ไม่-timeout) |
| `Address already in use` 8888 | relay ของ WSL ยึดพอร์ต | ดับเบิลคลิก `start-hexstrike.bat` ซ้ำ |
| `httpx: not found` | health ตรวจ Python module ไม่ใช่ binary | รัน `install-kali-tools.bat` |
| หยุดหลัง recon | anti-stall ถูกข้าม | พิมพ์ `ต่อ Phase 2` |
| ผลเดิมทุกครั้ง | HexStrike cache ตาม command string (TTL 1 ชม.) | เปลี่ยน argument |

---

## 🔐 ขอบเขตการทดสอบ / Scope discipline

สกิลยึดหลัก **impact-first** และ **finish-the-cluster**:

- **ให้ URL / host มา** = locked scope → ตามสินค้าเดียวกัน, gateway, API domain ที่ flow ธรรมชาติเปิดออกมา
- **ให้ชื่อองค์กรมา** = exploratory scope → จบ cluster ปัจจุบันก่อน เปิดอันใหม่
- **ทำปัจจุบันให้เสร็จก่อนขยาย** — ไม่ยิงหลาย host ตื้น ๆ
- **ทุก finding ต้อง verify จริง** — secret ที่ยังไม่ยิงถือเป็น clue ไม่ใช่ finding
- **หลักฐานต้อง reproduce ได้** — สรุปที่ไม่ตามด้วยขั้นตอนย้อนกลับ = สมมติฐาน

---

<p align="center">ติดตรงไหน → <a href="./INSTALL.md#6-อัปเดต--troubleshooting">INSTALL.md §6</a> หรือเปิด issue</p>
