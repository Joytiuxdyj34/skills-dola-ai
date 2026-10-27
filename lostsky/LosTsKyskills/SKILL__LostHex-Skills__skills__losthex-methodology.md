---
name: losthex-methodology
description: >-
  MITRE ATT&CK (900 techniques), OWASP WSTG 4.2 (125 tests), or operational playbooks (33). Methodology lookup — pick technique/test then route to exploit skill. Triggers: MITRE ATT&CK, OWASP WSTG, testing methodology, playbooks, technique lookup, test case index.
---
# LostHex-METHOD — MITRE / WSTG / Playbooks Index

> 900+ MITRE ATT&CK + 125 OWASP WSTG 4.2 + 33 operational playbooks — ค้นที่นี่แล้วส่งต่อไปสกิลเจาะ

## References (bundled, no install needed)

| File | อะไร | จำนวน |
|---|---|---|
| `references/mitre-index.md` | MITRE ATT&CK Enterprise/Mobile/ICS | **898** techniques |
| `references/wstg-index.md` | OWASP WSTG 4.2 | **125** tests (12 categories) |
| `references/playbooks.md` | Operational playbooks (condensed) | **33** playbooks |

Source เดิมมี 7,742 skills (รวม 5,000 CIS + 1,601 NIST แบบ compliance — ตัดทิ้ง, เก็บแต่ของโจมตี 900+125+33)

## วิธีใช้

### 1) หา WSTG test ที่ตรง surface
```
Surface: login form -> WSTG-ATHN (11 tests) + WSTG-INPV (29 tests)
Surface: API        -> WSTG-APIT (4) + WSTG-AUTHZ (7) + WSTG-INPV
Surface: file upload -> WSTG-INPV-08 + WSTG-CONF
```
เปิด `references/wstg-index.md` -> หา `WSTG-XXX-NN` -> อ่าน `what-to-check` + `key cmd` -> ส่งต่อ `losthex-web` / `losthex-api`

### 2) หา MITRE technique ที่ตรง tactic
```
Goal: credential access -> TA0006 (62 techs) -> T1003.001 LSASS, T1110 brute force
Goal: persistence      -> TA0003 (80 techs)
```
เปิด `references/mitre-index.md` -> หา `TA####` tactic -> เลือก `T####` technique -> อ่าน `How to Test` -> ส่งต่อ `losthex-ad` / `losthex-binary`

### 3) หา playbook สำเร็จรูป
```
windows-postexploit (59KB), linux-postexploit, aws/azure-postexploit, llm-security, ad-security, ebpf-attacks
```
เปิด `references/playbooks.md` -> หา playbook name -> copy commands/payloads

## Slash

```
/LostHex-METHOD                    # เปิด index นี้
/LostHex-METHOD WSTG-INPV          # ขอ input validation tests
/LostHex-METHOD T1003              # ขอ LSASS technique
```

Ponytail: ตัด CIS/NIST compliance — ceiling = offensive index only, upgrade เมื่อต้องทำ audit.