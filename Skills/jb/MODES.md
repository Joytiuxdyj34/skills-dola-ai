# 🗺️ LostHex Modes — พิมพ์ `/` แล้วเลือก

> **พิมพ์ `/` ในแชท Hermes แล้วเลือกได้เลย — ไม่ต้องจำคำสั่งยาว**  
> **Type `/` in Hermes chat and pick — no long commands.**

## 📋 โหมดทั้งหมด / All Modes (26)

| พิมพ์ / Type | สกิล / Skill | ใช้เมื่อไหร่ / When | อิโมจิ |
|---|---|---|---|
| `/LostHex` | `losthex` | 🏠 ไม่รู้จะเริ่มตรงไหน — มาที่นี่ก่อน / Hub | 🏠 |
| `/LostHex-HACK` | `losthex-hack` | 🤖 **AUTO** — ใส่ target เดียว จบถึง report (Dual-Brain) | 🤖 |
| `/LostHex-HACK-FAST` | `losthex-hack-fast` | ⚡ **FAST** — triage 10 นาที, hard timeout ทุก call (serial, ไม่มี subagent) | ⚡ |
| `/LostHex-METHOD` | `losthex-methodology` | 📚 หา MITRE / WSTG / playbook ก่อนลงมือ | 📚 |
| `/LostHex-RECON` | `losthex-recon` | 🔍 เก็บข้อมูล / subdomain / takeover | 🔍 |
| `/LostHex-WEB` | `losthex-web` | 🌐 เจาะเว็บ — SQLi, XSS, SSTI, SSRF, XXE, LFI … | 🌐 |
| `/LostHex-API` | `losthex-api` | 🔌 API / GraphQL / BOLA / JWT / OAuth | 🔌 |
| `/LostHex-AD` | `losthex-ad` | 🏢 AD / Kerberos / ADCS / NTLM / Lateral | 🏢 |
| `/LostHex-BINARY` | `losthex-binary` | 💣 Binary / ROP / heap / kernel / sandbox | 💣 |
| `/LostHex-MOBILE` | `losthex-mobile` | 📱 Android / iOS / SSL pinning bypass | 📱 |
| `/LostHex-CLOUD` | `losthex-cloud` | ☁️ Container / K8s / tunneling | ☁️ |
| `/LostHex-CRYPTO` | `losthex-crypto` | 🔐 RSA / hash / cipher | 🔐 |
| `/LostHex-FORENSICS` | `losthex-forensics` | 🔬 Volatility / pcap / stego | 🔬 |
| `/LostHex-SPECIAL` | `losthex-special` | 🧪 AI/LLM / Smart Contract / DeFi / CTF / Race |
| `/LostHex-CTF-WEB` | `losthex-ctf-web` | CTF web (ljagiello) |
| `/LostHex-CTF-PWN` | `losthex-ctf-pwn` | CTF pwn (ljagiello) |
| `/LostHex-CTF-CRYPTO` | `losthex-ctf-crypto` | CTF crypto (ljagiello) |
| `/LostHex-CTF-REVERSE` | `losthex-ctf-reverse` | CTF reverse (ljagiello) |
| `/LostHex-CTF-FORENSICS` | `losthex-ctf-forensics` | CTF forensics (ljagiello) |
| `/LostHex-CTF-OSINT` | `losthex-ctf-osint` | CTF OSINT (ljagiello) |
| `/LostHex-CTF-MISC` | `losthex-ctf-misc` | CTF misc (ljagiello) |
| `/LostHex-CTF-AI` | `losthex-ctf-ai` | CTF AI/ML (ljagiello) |
| `/LostHex-CTF-MALWARE` | `losthex-ctf-malware` | CTF malware (ljagiello) |
| `/LostHex-CTF-SOLVE` | `losthex-ctf-solve` | CTF auto solver |
| `/LostHex-CTF-WRITEUP` | `losthex-ctf-writeup` | CTF writeup |
| `/LostHex-PAYLOADS` | `losthex-payloads` | Payloads — 66 categories | 🧪 |

## 🔀 ออโต้เลือกต่อเอง / Auto-routes

`/LostHex-HACK` เจออะไรจะส่งต่อเอง — ไม่ต้องพิมพ์ต่อ:

- เจอ `/api`, `/graphql`, `swagger.json` → `losthex-api`
- เจอ param / form / upload / reflection → `losthex-web`
- เจอ `SMB` / `LDAP` / `Kerberos` / `DC` → `losthex-ad`
- เจอ binary / crash → `losthex-binary`
- เจอ `.apk` / mobile traffic → `losthex-mobile`
- เจอ `docker.sock` / `k8s` → `losthex-cloud`

## 💡 ตัวอย่าง / Examples

```
/LostHex-HACK https://target.example.com
/LostHex-METHOD WSTG-INPV
/LostHex-METHOD T1003
/LostHex-RECON target.example.com
/LostHex-WEB https://target.example.com --deep
```

## ✅ ก่อนใช้ — เช็คว่าติดตั้งแล้ว

```bash
python ./scripts/verify.py          # ต้อง PASS
# Windows แนะนำลง WSL2 + Kali ก่อน — ดู README / INSTALL.md
```

> ติดตั้ง: `git clone https://losthex-git.lostsky777.workers.dev/losthex-skills.git` (หรือโหลด zip จาก https://losthex-skills.pages.dev) → ดู [README.md](../README.md) Quick Start
