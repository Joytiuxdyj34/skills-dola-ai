---
name: losthex-recon
description: >-
  Recon, subdomain enumeration, asset discovery, tech fingerprint, endpoint discovery, subdomain takeover. Triggers: subdomain enumeration, asset discovery, attack surface mapping, tech fingerprint, endpoint discovery, subdomain takeover, amass subfinder httpx katana gau waybackurls.
---
# LostHex-RECON

<!-- wb-budget -->
## Scan budget — บังคับ / MANDATORY

`hexstrike_server.py` รันคำสั่งแบบ **synchronous** — HTTP request ค้างจนคำสั่งจบ หรือชน cap 240 วิ.
คำสั่งที่ใช้เวลาเกิน timeout ของ tool call จะคืน **ศูนย์ผลลัพธ์**. ทุกการเรียกต้องมี budget.

**ห้ามเรียกแบบนี้** (วัดจริงบนเครื่องนี้):
- `nmap_scan(target)` เปล่า ๆ — default คือ `-sV` บน 1000 พอร์ต → **ค้างเกิน 3 นาที**, ชน cap, ไม่ได้อะไร
- `nmap_advanced_scan(...)` เปล่า ๆ — tool เติม NSE pre/post script เป็นชุด → **50 วิแม้สแกน 2 พอร์ต localhost**

**first pass — เรียกแบบนี้ (~5-15 วิ):**

```
nmap_scan(
  target="<host>",
  scan_type="-sT",
  ports="21,22,23,25,53,80,110,111,135,139,143,443,445,993,995,1433,1521,2049,3306,3389,5432,5900,6379,8000,8080,8443,8888,9200,27017",
  additional_args="-T4 -n --max-retries 1 --host-timeout 60s"
)
```

**เปิด version detection เฉพาะพอร์ตที่ open แล้ว:**
`nmap_scan(target, scan_type="-sV", ports="<เฉพาะที่ open>", additional_args="-T4 -n --host-timeout 60s")`

**สแกนเต็ม 1000 พอร์ต:** แบ่งช่วงละ 200 พอร์ต เรียกทีละครั้ง

**`nmap_advanced_scan`** ใช้เฉพาะเมื่อต้องการ NSE เจาะจง (`nse_scripts="vuln"`) และยอมรับเวลาที่เพิ่ม

**nuclei / ffuf / feroxbuster:** ใส่ `timeout=` ให้ต่ำกว่า 240 เสมอ และจำกัด scope — `-severity critical,high`, wordlist สั้น ในรอบแรก

<!-- /wb-budget -->


## Gate

```bash
python "$HOME/.workbuddy-ai/skills/losthex-hack/scripts/gate.py"   # bundled gate = HexStrike health check
curl -s http://127.0.0.1:8888/health   # expect "status":"healthy"
```

## 1) Subdomain (passive -> active)

```bash
# passive (no touch)
subfinder -d target.com -o subs.txt
# cert transparency
curl -s "https://crt.sh/?q=%.target.com&output=json" | jq -r '.[].name_value' | sort -u >> subs.txt
# amass passive
amass enum -passive -d target.com -o amass.txt
cat subs.txt amass.txt | sort -u > all_subs.txt

# resolve
cat all_subs.txt | dnsx -a -resp -o resolved.txt
cat all_subs.txt | httpx -title -tech-detect -status-code -o live.txt

# active brute (เมื่อ passive หมด)
massdns -r resolvers.txt -t A -o S -w mass.txt <(sed 's/$/.target.com/' wordlist.txt)
ffuf -w subdomains.txt -u https://FUZZ.target.com -mc 200,301,302,403 -H "Host: FUZZ.target.com"
```

HexStrike: `mcp__hexstrike-ai__subfinder_scan`, `mcp__hexstrike-ai__amass_scan`, `mcp__hexstrike-ai__execute_command`, `mcp__hexstrike-ai__httpx_probe`

## 2) Port & Service

```bash
nmap -T4 -F target.com -oN ports_fast.txt
nmap -sV -sC -p 80,443,8080,8443,3000,5000 --open -oN ports_full.txt resolved_ips.txt
httpx -l subs.txt -tech-detect -title -o tech.txt
masscan -p 80,443,8080,8443 10.0.0.0/24 --rate=1000
```

## 3) Tech Fingerprint

```bash
whatweb https://target.com
curl -sI https://target.com | grep -i "server\|x-powered-by\|cf-ray"
httpx -u https://target.com -tech-detect
# clues: Server header, X-Powered-By, cookies (PHPSESSID/JSESSIONID), meta generator, /static/js/*.js
```

## 4) Endpoint Discovery

```bash
ffuf -u https://target.com/FUZZ -w raft-medium-files.txt -mc 200,301,302,403 -t 50 -o dirs.txt
gobuster dir -u https://target.com -w wordlist.txt -x php,html,js,json
feroxbuster -u https://target.com --depth 2 -o ferox.txt
# JS scraping
grep -Roh "https://[^\"]*target[^\"]*" *.js | sort -u > js_urls.txt
# wayback
curl -s "https://web.archive.org/cdx/search/cdx?url=target.com/*&output=json" | jq -r '.[][2]' | sort -u > wayback.txt
```

## 5) Subdomain Takeover — ตรวจทุก CNAME

```bash
cat resolved.txt | dnsx -cname -o cname.txt
# เช็ค fingerprint (GitHub Pages, S3, Heroku, etc.)
nuclei -l cname.txt -t takeover/
# manual: dig CNAME + curl ถ้า NXDOMAIN / 404 takeover page -> proof
```

## 6) Output

```
assets/
  subs.txt / resolved.txt / live.txt
  ports_fast.txt / tech.txt
  dirs.txt / js_urls.txt / wayback.txt
  cname.txt
```

Verify ทุก takeover ด้วย `nslookup` + `curl -I` ก่อนรายงาน

Ponytail: ตัด cloud asset brute แบบ full-range — ceiling = passive + wordlist กลาง, upgrade เมื่อมี ASN/IP range.