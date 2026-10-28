# 🔧 TOOLS — ต้องลงอะไรบ้าง / Tool Requirements

> **อ่านก่อนรัน `/LostHex-HACK` — เช็คว่ามีอะไรแล้ว ขาดอะไรค่อยลง**  
> **Read before running `/LostHex-HACK` — check what you have, install what you miss.**

LostHex จะตรวจเองตอนรัน — ถ้าขาดจะบอกว่าขาดตัวไหน ไม่ได้มั่วต่อ  
LostHex checks on run — if something's missing it tells you, no guessing.

```bash
python ./scripts/verify.py --verbose  # ดูว่าขาดอะไร
```

---

## 🚦 Gate — แบ่ง 3 ระดับ

| ระดับ / Level | หมายถึง / Means | ถ้าไม่มีจะเป็นไง / Without it |
|---|---|---|
| 🔴 **required** | ต้องมี — ไม่มีแล้วออโต้ไม่รัน | `verify.py` ขึ้น FAIL |
| 🟡 **recommended** | แนะนำ — มีแล้วเก่งขึ้นมาก | บางโหมดจะ degraded / ข้ามเฟส |
| 🟢 **optional** | มีก็ดี — เพิ่ม coverage | ไม่กระทบหลัก |

---

## 🔴 Required — ต้องมี

| Tool / Component | เอาไว้ทำอะไร / Purpose | ลงยังไง / Install |
|---|---|---|
| **Hermes Agent** | รันสกิล `/LostHex-*` | [hermes-agent.nousresearch.com/docs](https://hermes-agent.nousresearch.com/docs) |
| **Python 3.12** | รัน hexstrike server + scripts | [python.org](https://python.org) / `sudo apt install python3` |
| **Node 22** | รัน cyberstrike (optional) | [nodejs.org](https://nodejs.org) / `sudo apt install nodejs` |
| **HexStrike server** | สั่ง 150 tools ผ่าน MCP | `git clone 0x4m4/hexstrike-ai && pip install -r requirements.txt` |
| **HexStrike MCP** | ต่อ tools เข้า Hermes | `hermes mcp add hexstrike-ai ...` |

> ถ้า 5 ตัวนี้ครบ → `verify.py` ขึ้น PASS → ลุย `/LostHex-HACK` ได้เลย

---

## 🟡 Recommended — แนะนำให้มี

| Tool | ใช้ในโหมด / Used in | Windows | Kali / WSL2 |
|---|---|---|---|
| **CyberStrike** | HACK (Dual-Brain) | `npm i -g @cyberstrike-io/cyberstrike` + `...-windows-x64` | `npm i -g ...-linux-x64` |
| **nmap** | RECON / AD / NETWORK | via HexStrike | `sudo apt install nmap` |
| **ffuf / gobuster** | RECON / WEB | via HexStrike | `sudo apt install ffuf gobuster` |
| **nuclei** | WEB / API | via HexStrike | `go install github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest` |
| **sqlmap** | WEB (SQLi) | via HexStrike | `sudo apt install sqlmap` |
| **httpx / dnsx / subfinder / amass** | RECON | via HexStrike | `sudo apt install httpx dnsx subfinder amass` |

> กลุ่มนี้ถ้าลงบน Kali/WSL2 จะได้ tools ครบ ~60 ตัวที่ Windows ไม่มี

---

## 🟢 Optional — เติมตามสาย / Add per specialty

| สาย / Specialty | Tools | ลงยังไง / Install (Kali) |
|---|---|---|
| **Brute / Creds** | hydra, medusa, patator, hashcat, john | `sudo apt install hydra medusa hashcat john` |
| **AD / Internal** | impacket, bloodhound, enum4linux-ng, responder, kerbrute | `pipx install impacket; sudo apt install bloodhound` |
| **Web Deep** | wpscan, commix, dalfox, xsstrike | `sudo apt install wpscan commix` |
| **Cloud / K8s** | kubectl, trivy, kube-hunter, prowler | ตาม docs แต่ละตัว |
| **Forensics** | volatility3, tshark, binwalk, foremost | `sudo apt install tshark binwalk foremost` |
| **Crypto** | hashcat, john, sage | `sudo apt install hashcat john` |

> 💡 **Windows ไม่มี** hydra / john / wpscan / commix / msfconsole / responder / aircrack / tshark … แบบ native — ใช้ Kali/WSL2 ถึงจะได้ครบ

---

## 📦 HexStrike Tool Families — 150 ตัวมีอะไรบ้าง

```
recon     : nmap, masscan, amass, subfinder, httpx, dnsx, theHarvester, shodan, censys
fuzz/web  : ffuf, gobuster, feroxbuster, wfuzz, nuclei, wpscan, nikto, dirsearch
sqli/xss  : sqlmap, xsstrike, dalfox, commix
brute     : hydra, medusa, patator, hashcat, john, ncrack
ad/net    : impacket, responder, enum4linux-ng, smbclient, kerbrute, bloodhound
exploit   : msfconsole, searchsploit, metasploit
forensics : volatility, tshark, binwalk, exiftool, steghide
cloud/k8s : kubectl, trivy, kube-hunter
osint     : theHarvester, recon-ng, spiderfoot
```

เช็คจริงบนเครื่อง: `hermes mcp test hexstrike-ai` — จะ list 150 tools ที่เจอ

---

## 📋 Copy/Paste — ลงทีเดียวจบ

### WSL2 Kali (ครบสุด / most complete)

```bash
sudo apt update && sudo apt install -y \
  nmap ffuf gobuster nuclei sqlmap hydra john hashcat \
  whatweb masscan amass subfinder httpx dnsx \
  impacket-scripts bloodhound smbclient enum4linux-ng \
  tshark binwalk foremost exiftool golang-go

go install github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
go install github.com/projectdiscovery/httpx/cmd/httpx@latest
go install github.com/projectdiscovery/dnsx/cmd/dnsx@latest
```

### Windows (เน้น HexStrike dispatch)

```powershell
# ใช้ HexStrike MCP เป็นหลัก — ลงเฉพาะที่ต้องรันตรงๆ
# nuclei / httpx มี Windows binary แยกถ้าต้องการ
# ที่เหลือใช้ Kali/WSL2 จะคุ้มกว่า
```

---

## ✅ Verify — เช็คว่าครบหรือยัง

```bash
python ./scripts/verify.py           # gate: required ต้องผ่าน
python ./scripts/verify.py --verbose # ดูทุก tool
python ./scripts/verify.py --strict  # recommended ก็ต้องผ่านด้วย
python ./scripts/verify.py --degraded # ข้าม hexstrike/cyberstrike — ใช้ curl+payload อย่างเดียว
```

---

<p align="center">มีครบ = เก่งเต็ม · มีน้อย = ก็ยังลุยได้แบบ degraded 💪</p>
