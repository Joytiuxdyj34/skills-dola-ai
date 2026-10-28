# 🧭 Tool Routing — LostHex เลือก tools ยังไง

> **มี HexStrike = ใช้ MCP ก่อนเสมอ — ไม่มีก็ fallback เป็น curl + payload มือ**  
> **Has HexStrike = use MCP first — without it, fallback to curl + manual payloads.**

## 📏 กฎ 3 ข้อ / 3 Rules

1. **มี HexStrike MCP** → เรียก `mcp__hexstrike_ai_*` ก่อนเสมอ; Nuclei MCP รับ `timeout` (default 300s) และ timeout ถูกส่งต่อถึง command executor
2. **ไม่มี MCP / offline** → fallback เป็นคำสั่ง shell เทียบเท่า (ถ้ามี binary)
3. **ไม่มี tool** → บอกว่าต้องติดตั้ง (ดู [TOOLS.md](../TOOLS.md)) — ไม่มั่ว payload ปลอม

## 🗺️ Map ย่อ / Quick Map

| งาน / Task | HexStrike MCP | Fallback (ถ้าไม่มี) |
|---|---|---|
| port scan | `nmap_scan` | `nmap -sV -Pn target` |
| dir fuzz | `ffuf_scan` / `gobuster_scan` | `ffuf -u URL/FUZZ -w raft-medium.txt` |
| nuclei (งานสั้น) | `nuclei_scan` | `nuclei -u URL -severity critical,high` |
| nuclei baseline / งานอาจนาน | `nuclei_scan` พร้อม `timeout` (server cap 240s; MCP/Hermes deadlines 270/300s) | `nuclei -u URL -severity critical,high` โดยครอบด้วย process timeout |
| SQLi | `sqlmap_scan` | `sqlmap -u URL --batch --risk 1` |
| XSS | `dalfox_scan` / `xsstrike` | payload มือ + `curl` |
| brute | `hydra_brute` | `hydra -l admin -P pass host http-post-form` |
| AD / SMB | `enum4linux_scan` / `impacket_*` | `impacket-*` scripts |
| hash crack | `hashcat_crack` / `john_crack` | `hashcat -m 0 hashes.txt wordlist` |

## 🧠 HexStrike vs CyberStrike vs Degraded

| ตัว | คืออะไร | ใช้เมื่อไหร่ | ออโต้ไหม |
|---|---|---|---|
| **HexStrike 150 tools** | 🔨 มือยิง — `nmap`, `ffuf`, `sqlmap` … ผ่าน MCP | ทุก phase ของออโต้ | ✅ ออโต้เรียกถ้ามี |
| **CyberStrike 22 agents** | 🧠 สมองสำรอง — planner + playbooks | อยากได้มุมมองที่ 2 | ⏭️ ข้ามได้ — Hermes คือสมองหลัก |
| **Degraded** | 🩹 `curl` + payload มือ (`--offline`) | ลง tools ไม่ได้ | ✅ fallback เอง |

> **สรุป:** Hermes (โมเดลที่คุยอยู่นี่) คือสมองหลัก — ไม่ต้องมี LLM key ก็ใช้ได้  
> CyberStrike CLI เพียวๆ ถึงค่อยต้องมี `ANTHROPIC_API_KEY` / `OPENAI_API_KEY`

## 🧪 Dual-Brain (ออโต้ใน `/LostHex-HACK`)

```
findings → Brain A (Hermes + losthex-*) → Plan A
         → Brain B (Hermes + playbooks/WSTG/MITRE) → Plan B
         → Merge → เลือกทาง impact สูง + verify ได้
```

## 🔍 เช็คว่า tools พร้อมไหม

```bash
hermes mcp test hexstrike-ai  # ต้องขึ้น ✓ Connected / 150 tools
python ./scripts/verify.py --verbose
# Windows ให้รัน HexStrike server ใน Kali/WSL2; 150 คือจำนวน MCP endpoints ส่วน binary ที่รันได้ขึ้นกับของที่ติดตั้งใน Kali
```
