---
name: losthex
description: >-
  LostHex modes, hub, or wants to pick a hacking mode. Routes to the correct LostHex sub-skill. Triggers: hacking mode selector, offensive security hub, pentest playbook router, red team.
---
# LostHex — Hub

> พิมพ์ `/` แล้วเลือกโหมด — สกิลนี้คือ router

## Modes

| Command | Skill | งาน |
|---|---|---|
| `/LostHex-HACK` | `losthex-hack` | AUTO full-chain |
| `/LostHex-RECON` | `losthex-recon` | recon / surface / takeover |
| `/LostHex-WEB` | `losthex-web` | web vulns |
| `/LostHex-API` | `losthex-api` | API / GraphQL / BOLA / JWT |
| `/LostHex-AD` | `losthex-ad` | AD / Kerberos / ADCS / lateral |
| `/LostHex-BINARY` | `losthex-binary` | binary / ROP / heap / kernel |
| `/LostHex-MOBILE` | `losthex-mobile` | Android / iOS / pinning |
| `/LostHex-CLOUD` | `losthex-cloud` | container / k8s / tunneling |
| `/LostHex-CRYPTO` | `losthex-crypto` | RSA / hash / cipher |
| `/LostHex-FORENSICS` | `losthex-forensics` | volatility / pcap / stego |
| `/LostHex-SPECIAL` | `losthex-special` | AI/LLM / smart contract / DeFi / deserialization / race / CTF |
| `/LostHex-CTF-WEB` | `losthex-ctf-web` | CTF web exploitation (ljagiello/ctf-skills) |
| `/LostHex-CTF-PWN` | `losthex-ctf-pwn` | CTF binary pwn (ljagiello/ctf-skills) |
| `/LostHex-CTF-CRYPTO` | `losthex-ctf-crypto` | CTF crypto (ljagiello/ctf-skills) |
| `/LostHex-CTF-REVERSE` | `losthex-ctf-reverse` | CTF reverse engineering (ljagiello/ctf-skills) |
| `/LostHex-CTF-FORENSICS` | `losthex-ctf-forensics` | CTF forensics (ljagiello/ctf-skills) |
| `/LostHex-CTF-OSINT` | `losthex-ctf-osint` | CTF OSINT (ljagiello/ctf-skills) |
| `/LostHex-CTF-MISC` | `losthex-ctf-misc` | CTF misc / bashjails / encodings (ljagiello/ctf-skills) |
| `/LostHex-CTF-AI` | `losthex-ctf-ai` | CTF AI/ML (ljagiello/ctf-skills) |
| `/LostHex-CTF-MALWARE` | `losthex-ctf-malware` | CTF malware analysis (ljagiello/ctf-skills) |
| `/LostHex-CTF-SOLVE` | `losthex-ctf-solve` | CTF auto solver — generic challenge |
| `/LostHex-CTF-WRITEUP` | `losthex-ctf-writeup` | CTF writeup generator |
| `/LostHex-PAYLOADS` | `losthex-payloads` | PayloadsAllTheThings 66 categories (swisskyrepo) |
| `/LostHex-METHOD` | `losthex-methodology` | MITRE 900 + WSTG 125 + playbooks 33 — methodology lookup |

## Gate (บังคับ)

ก่อนรันโหมดใดๆ:
```bash
python "$HOME/.workbuddy-ai/skills/losthex-hack/scripts/gate.py"   # bundled gate = HexStrike health check
```
ถ้า `[FAIL]` -> แก้ตาม `INSTALL.md` ก่อน — ทุก sub-skill จะ fail fast ถ้า tools ไม่พร้อม

## Routing

- มี URL/target ชัดเจน + อยากให้ทำเองทั้งหมด -> `/LostHex-HACK`
- อยากเก็บข้อมูลก่อน -> `/LostHex-RECON`
- เจอเว็บ/พารามิเตอร์ -> `/LostHex-WEB`
- เจอ API/GraphQL/mobile -> `/LostHex-API` หรือ `/LostHex-MOBILE`
- เจอ AD/DC/SMB -> `/LostHex-AD`
- เจอ binary/pwn/kernel -> `/LostHex-BINARY`
- เจอ AI/LLM/smart contract/CTF/deserialization/race -> `/LostHex-SPECIAL`
- หา methodology / technique / test ID -> `/LostHex-METHOD`

## Quick verify

```bash
curl -s http://127.0.0.1:8888/health   # expect "status":"healthy"
cyberstrike --version
```

ดูเพิ่ม: `references/MODES.md`, `TOOLS.md`